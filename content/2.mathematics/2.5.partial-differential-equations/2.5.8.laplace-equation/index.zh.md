---
title: 调和函数与 Laplace 方程
source_hash: 68ed4922a387
---

**Laplace 方程** $\Delta u=0$ 与 **Poisson 方程** $-\Delta u=f$（[2.5.1](/2.5.1)）描述平衡状态：稳态温度、静电势与引力势、理想流体的速度势、受载张紧薄膜的形状、扩散的定常状态。它们的解——**调和函数**（[2.2.14](/2.2.14#sec-14.5.2)）——是分析学中最"刚性"的函数。调和函数等于它在每个球面上的平均值；它无穷次可微；它在定义域内部取不到最大值或最小值；它在一个区域中由边界值通过一个显式的积分公式所确定；在平面上，它是一个**解析函数**的实部。

本章按照这些性质相互依赖的顺序展开。Green 公式与基本解（§8.1）把任意函数用它的 Laplace 算子值和边界值表示出来。平均值性质与极值原理（§8.2）给出唯一性与稳定性。Green 函数（§8.3）——对半空间和球用镜像法构造——把表示公式变成解的公式，即 Poisson 积分。在二维情形，复分析通过共形映射提供了多得多的显式解（§8.4，用到 [2.3.8](/2.3.8)）。最后，Dirichlet 原理（§8.5）把解刻画为某个能量的极小元，把 Laplace 方程与**变分法**（[2.4.13](/2.4.13)）联系起来。本章始终设 $\Omega\subset\mathbb{R}^n$（$n\ge2$）是有界区域，边界 $\partial\Omega$ 分段光滑，外法向单位向量为 $\boldsymbol{n}$；$\omega_n$ 表示 $\mathbb{R}^n$ 中单位球面的面积（$\omega_2=2\pi$，$\omega_3=4\pi$）。

## 8.1. Green 公式与基本解

### 8.1.1. Green 公式

**Green 第一公式**（[2.2.14](/2.2.14#thm-14.5.2)）是说：对 $u,v\in C^2(\bar\Omega)$，

$$
\int_\Omega v\,\Delta u\,\mathrm{d}V=\oint_{\partial\Omega}v\frac{\partial u}{\partial\boldsymbol{n}}\,\mathrm{d}S-\int_\Omega\nabla u\cdot\nabla v\,\mathrm{d}V.\tag{8.1}
$$
（用 **Gauss 公式**的证明在任何维数中都成立。）交换 $u$ 与 $v$ 后相减，梯度项相互抵消。

**定理 8.1.1（Green 第二公式）** 对 $u,v\in C^2(\bar\Omega)$，

$$
\int_\Omega\big(u\,\Delta v-v\,\Delta u\big)\,\mathrm{d}V=\oint_{\partial\Omega}\Big(u\frac{\partial v}{\partial\boldsymbol{n}}-v\frac{\partial u}{\partial\boldsymbol{n}}\Big)\mathrm{d}S.\tag{8.2}
$$

这个恒等式是 Sturm–Liouville 算子的 Lagrange 恒等式（[2.4.12](/2.4.12#sec-12.5.1)）的高维类比：它说明 $\Delta$ 在满足齐次 Dirichlet 或 Neumann 条件的函数上是对称的。由它立即得到关于边值问题的两个推论。

**定理 8.1.2** 设 $u\in C^2(\bar\Omega)$。

1. （相容性条件）若在 $\Omega$ 内 $-\Delta u=f$，在 $\partial\Omega$ 上 $\frac{\partial u}{\partial\boldsymbol{n}}=g$，则
$$
\int_\Omega f\,\mathrm{d}V+\oint_{\partial\Omega}g\,\mathrm{d}S=0.
$$
2. （唯一性）Dirichlet 问题（在 $\Omega$ 内 $-\Delta u=f$，在 $\partial\Omega$ 上 $u=g$）的两个解相同；当 $\Omega$ 连通时，Neumann 问题的两个解相差一个常数。

**证明** 1：在 (8.1) 中取 $v\equiv1$。2：两个解之差 $w$ 满足 $\Delta w=0$，在 $\partial\Omega$ 上 $w=0$（或 $\frac{\partial w}{\partial\boldsymbol{n}}=0$）。在 (8.1) 中取 $u=v=w$，得 $\int_\Omega\lvert\nabla w\rvert^2\,\mathrm{d}V=0$，所以 $w$ 为常数；在 Dirichlet 情形该常数为 $0$。$\square$

相容性条件有明确的意义：在稳态下，内部产生的热量（$\int f$）必须从边界流出（$-\oint g$ 是向外的通量）。若它不成立，Neumann 问题无解，温度将持续上升或下降。这是 [2.4.12](/2.4.12#sec-12.4.3) 中 Fredholm 二择一定理的高维形式：齐次 Neumann 问题有非平凡解 $1$，数据必须与它正交。

### 8.1.2. 基本解

Laplace 方程在平移和旋转下不变，所以先寻找径向解 $u=v(r)$，$r=\lvert x\rvert$。在极坐标或球坐标中（[2.5.5](/2.5.5#sec-5.1.1)），$\Delta u=v''+\frac{n-1}rv'=r^{1-n}(r^{n-1}v')'$，所以 $r^{n-1}v'$ 为常数，由此 $n=2$ 时 $v=a\ln r+b$，$n\ge3$ 时 $v=ar^{2-n}+b$（与 [2.2.14](/2.2.14#sec-14.6) 中相同）。

**定义 8.1.1（Laplace 方程的基本解）** 函数

$$
\Gamma(x)=\begin{cases}-\dfrac{1}{2\pi}\ln\lvert x\rvert,&n=2,\\[3mm]\dfrac{1}{(n-2)\,\omega_n\lvert x\rvert^{n-2}},&n\ge3,\end{cases}\qquad x\ne0,\tag{8.3}
$$
称为 Laplace 方程的**基本解**。当 $n=3$ 时，$\Gamma(x)=\frac1{4\pi\lvert x\rvert}$。

常数的选取使得 $\nabla\Gamma=-\frac{x}{\omega_n\lvert x\rvert^n}$ 通过以 $0$ 为球心的每个球面向外的通量为 1：$-\oint_{\lvert x\rvert=r}\frac{\partial\Gamma}{\partial r}\,\mathrm{d}S=\frac{1}{\omega_nr^{n-1}}\cdot\omega_nr^{n-1}=1$。从物理上看，在使 $-\Delta(\text{势})=$ 电荷密度的单位制下，$\Gamma(x-y)$ 是位于 $y$ 的单位点电荷（或稳态下的点热源）在 $x$ 处产生的势。形式上 $-\Delta\Gamma=\delta$（**δ 函数**），下面的定理使这一点精确化。

**定理 8.1.3（Green 表示公式）** 对 $u\in C^2(\bar\Omega)$ 与 $x\in\Omega$，

$$
u(x)=\oint_{\partial\Omega}\Big(\Gamma(y-x)\frac{\partial u}{\partial\boldsymbol{n}}(y)-u(y)\frac{\partial\Gamma(y-x)}{\partial\boldsymbol{n}_y}\Big)\mathrm{d}S_y-\int_\Omega\Gamma(y-x)\,\Delta u(y)\,\mathrm{d}V_y.\tag{8.4}
$$

**证明** 函数 $v(y)=\Gamma(y-x)$ 在 $\Omega$ 中除 $y=x$ 外是调和的。挖去一个小球 $B_\varepsilon=B(x,\varepsilon)$，在 $\Omega_\varepsilon=\Omega\setminus\bar B_\varepsilon$ 上（那里 $\Delta v=0$）应用 (8.2)：

$$
-\int_{\Omega_\varepsilon}v\,\Delta u\,\mathrm{d}V=\oint_{\partial\Omega}\Big(u\frac{\partial v}{\partial\boldsymbol{n}}-v\frac{\partial u}{\partial\boldsymbol{n}}\Big)\mathrm{d}S+\oint_{\partial B_\varepsilon}\Big(u\frac{\partial v}{\partial\boldsymbol{n}}-v\frac{\partial u}{\partial\boldsymbol{n}}\Big)\mathrm{d}S.
$$
在 $\partial B_\varepsilon$ 上，$\Omega_\varepsilon$ 的外法向指向 $x$，所以把 $\Gamma$ 写成 $r$ 的函数，有 $\frac{\partial v}{\partial\boldsymbol{n}}=-\Gamma'(\varepsilon)=\frac{1}{\omega_n\varepsilon^{n-1}}$。因此 $\oint_{\partial B_\varepsilon}u\frac{\partial v}{\partial\boldsymbol{n}}\,\mathrm{d}S$ 是 $u$ 在 $\partial B_\varepsilon$ 上的平均值，趋于 $u(x)$。另一项不超过 $\lvert\Gamma(\varepsilon)\rvert\,\omega_n\varepsilon^{n-1}\max\lvert\nabla u\rvert$，$n=2$ 时为 $\varepsilon\lvert\ln\varepsilon\rvert$ 量级，$n\ge3$ 时为 $\varepsilon$ 量级，都趋于 $0$。由于 $\Gamma(y-x)$ 在 $y=x$ 附近可积，左边趋于 $-\int_\Omega v\Delta u$。令 $\varepsilon\to0$ 并整理即得 (8.4)。$\square$

若 $u$ 在 $\partial\Omega$ 附近为零，(8.4) 就是 $u(x)=\int\Gamma(y-x)(-\Delta u)(y)\,\mathrm{d}y$，即 $\Gamma*(-\Delta u)=u$，这正是 $-\Delta\Gamma=\delta$ 的确切含义。相应地，对合理的 $f$（例如具有紧支集的 $f\in C^2$），Newton 势 $u=\Gamma*f$ 在 $\mathbb{R}^n$ 中满足 $-\Delta u=f$：电荷分布的势是其各点电荷之势的叠加。

**推论 8.1.1** 区域 $\Omega$ 中的每个调和函数在 $\Omega$ 中都无穷次可微。

**证明** 设 $x_0\in\Omega$，取以 $x_0$ 为中心的球 $\bar B\subset\Omega$。在 $B$ 上应用 (8.4)，其中 $\Delta u=0$：对 $x_0$ 附近的 $x$，$u(x)$ 是 $\partial B$ 上函数 $\Gamma(y-x)$、$\frac{\partial\Gamma(y-x)}{\partial\boldsymbol{n}_y}$ 的积分，这些函数关于 $x$ 无穷次可微（因为 $y-x$ 远离 $0$），所以可以任意阶地**积分号下求导**。$\square$

事实上调和函数是实解析的（局部可以表示为 $x_1,\dots,x_n$ 的收敛幂级数），这一结论我们不证明。热方程的相应结论是 [2.5.7](/2.5.7#sec-7.1.3) 中的光滑化效应；对波动方程，相应的结论不成立。

## 8.2. 平均值性质与极值原理

### 8.2.1. 平均值性质

**定理 8.2.1（平均值性质）** 设 $u$ 在 $\Omega$ 中调和，闭球 $\bar B(x,r)$ 含于 $\Omega$。则

$$
u(x)=\frac{1}{\omega_nr^{n-1}}\oint_{\partial B(x,r)}u\,\mathrm{d}S=\frac{n}{\omega_nr^n}\int_{B(x,r)}u\,\mathrm{d}V,
$$
即球心处的值既等于球面上的平均值，也等于球体上的平均值。

**证明** 对 $0<\rho\le r$，令 $\phi(\rho)=\frac{1}{\omega_n}\oint_{\lvert\boldsymbol{e}\rvert=1}u(x+\rho\boldsymbol{e})\,\mathrm{d}S_{\boldsymbol{e}}$ 为 $u$ 在 $\partial B(x,\rho)$ 上的平均值，写成单位球面上的积分。积分号下求导，再换回 $\partial B(x,\rho)$ 上的积分，由 Gauss 公式，

$$
\phi'(\rho)=\frac{1}{\omega_n}\oint_{\lvert\boldsymbol{e}\rvert=1}\nabla u(x+\rho\boldsymbol{e})\cdot\boldsymbol{e}\,\mathrm{d}S_{\boldsymbol{e}}=\frac{1}{\omega_n\rho^{n-1}}\oint_{\partial B(x,\rho)}\frac{\partial u}{\partial\boldsymbol{n}}\,\mathrm{d}S=\frac{1}{\omega_n\rho^{n-1}}\int_{B(x,\rho)}\Delta u\,\mathrm{d}V=0.
$$
所以 $\phi$ 为常数，而由连续性，$\rho\to0^+$ 时 $\phi(\rho)\to u(x)$；这就证明了第一个等式。把 $u(x)=\phi(\rho)$ 乘以 $\omega_n\rho^{n-1}$ 并在 $0<\rho<r$ 上积分，得 $\frac{\omega_nr^n}{n}u(x)=\int_{B(x,r)}u\,\mathrm{d}V$，即第二个等式。$\square$

在平面上，平均值性质也可以由 **Cauchy 积分公式**（[2.3.4](/2.3.4)）得到：若 $u=\operatorname{Re}F$，$F$ 解析，则 $F(z_0)=\frac1{2\pi}\int_0^{2\pi}F(z_0+r\mathrm{e}^{\mathrm{i}\theta})\,\mathrm{d}\theta$，取实部即得 $n=2$ 时的定理。逆命题也成立（不加证明）：对 $\Omega$ 中每个球都满足平均值性质的连续函数是调和的。因此"调和"可以不借助导数来定义，即"等于其局部平均值"。这也是离散情形的图景：在间距为 $h$ 的正方形网格上，$\Delta u\approx\frac{1}{h^2}\big(\sum_{\text{4 个相邻点}}u-4u\big)$，所以离散 Laplace 方程是说每个值等于它四个相邻点上值的平均，这是迭代数值方法的基础。

### 8.2.2. 极值原理

**定理 8.2.2（强极值原理）** 设 $\Omega$ 连通，$u$ 在 $\Omega$ 中调和。若 $u$ 在 $\Omega$ 上的最大值在某个内点处取到，则 $u$ 在 $\Omega$ 中为常数。对最小值结论相同。

**证明** 令 $M=\max_\Omega u$，$S=\{x\in\Omega:u(x)=M\}$，由假设它非空，由连续性它在 $\Omega$ 中是闭的。若 $x\in S$ 且 $\bar B(x,r)\subset\Omega$，则由平均值性质 $M=u(x)=\frac{n}{\omega_nr^n}\int_{B(x,r)}u\,\mathrm{d}V$。由于 $u\le M$ 且 $u$ 连续，平均值等于 $M$ 只有在 $B(x,r)$ 上 $u\equiv M$ 时才可能；因此 $S$ 是开集。连通集除自身和空集之外没有既开又闭的子集，所以 $S=\Omega$。对最小值，把这一结论应用于 $-u$。$\square$

**推论 8.2.1（弱极值原理）** 设 $u\in C^2(\Omega)\cap C(\bar\Omega)$ 在有界区域 $\Omega$ 中调和。则

$$
\min_{\partial\Omega}u\le u(x)\le\max_{\partial\Omega}u\qquad\text{对所有 }x\in\Omega.
$$

**证明** 连续函数 $u$ 在紧集 $\bar\Omega$ 上取到最大值。若最大值只在内点处取到，则由定理 8.2.2，$u$ 为常数，最大值也在 $\partial\Omega$ 上取到，矛盾。$\square$

其含义与热方程（[2.5.7](/2.5.7#sec-7.2)）相同：没有热源的稳态温度在内部没有热点或冷点。那里用严格不等式的证明在这里同样适用，并且给出更多的结论：若在 $\Omega$ 中 $\Delta u\ge0$（$u$ 是下调和的），则 $\max_{\bar\Omega}u=\max_{\partial\Omega}u$（对 $u+\varepsilon\lvert x\rvert^2$ 应用这一论证，它满足 $\Delta>0$，因而没有内部最大值）。

![单位圆盘上的调和函数 u = Re(z^3 + z^2 / 2)：最大值和最小值都位于边界圆周上，圆心处的值是边界值的平均值](./plots/maximum-principle.py)

**推论 8.2.2（Dirichlet 问题的唯一性与稳定性）** 设 $u_1,u_2\in C^2(\Omega)\cap C(\bar\Omega)$ 在 $\Omega$ 中满足 $-\Delta u_i=f$，在 $\partial\Omega$ 上 $u_i=g_i$。则

$$
\max_{\bar\Omega}\lvert u_1-u_2\rvert\le\max_{\partial\Omega}\lvert g_1-g_2\rvert.
$$
特别地，Dirichlet 问题至多有一个解，且解在最大模范数下连续依赖于边界数据。

**证明** 对调和函数 $\pm(u_1-u_2)$ 应用推论 8.2.1。$\square$

与定理 8.1.2 不同，这里不要求直到边界的可微性，只要求连续性。结合解的存在性（球的情形见 §8.3，一般情形需要更深入的方法），Poisson 方程的 Dirichlet 问题是适定的。

### 8.2.3. Liouville 定理

**定理 8.2.3（调和函数的 Liouville 定理）** 在整个 $\mathbb{R}^n$ 上有界的调和函数是常数。

**证明** 设 $\lvert u\rvert\le M$，$x,y\in\mathbb{R}^n$，$d=\lvert x-y\rvert$。对半径 $R>d$ 的球应用平均值性质，记其体积为 $V_R=\frac{\omega_nR^n}{n}$，

$$
\lvert u(x)-u(y)\rvert=\frac1{V_R}\Big\lvert\int_{B(x,R)}u\,\mathrm{d}V-\int_{B(y,R)}u\,\mathrm{d}V\Big\rvert\le\frac{M}{V_R}\big\lvert B(x,R)\,\triangle\,B(y,R)\big\rvert,
$$
其中 $\triangle$ 表示对称差。对称差中的每一点到 $x$ 的距离都介于 $R-d$ 与 $R+d$ 之间，所以它的体积不超过 $V_{R+d}-V_{R-d}$，右边不超过 $M\frac{(R+d)^n-(R-d)^n}{R^n}$，当 $R\to\infty$ 时趋于 $0$。因此 $u(x)=u(y)$。$\square$

在平面上，由此可推出复分析中的 Liouville 定理（[2.3.4](/2.3.4)）：若 $F$ 是有界整函数，则它的实部和虚部都是 $\mathbb{R}^2$ 上有界的调和函数，因而为常数。

## 8.3. Green 函数

### 8.3.1. 定义与性质

表示公式 (8.4) 用 $\Delta u$、$u$ 的边界值和法向导数 $\frac{\partial u}{\partial\boldsymbol{n}}$ 来表示 $u$。对 Dirichlet 问题，最后一项是未知的。我们给 $\Gamma(y-x)$ 加上一个调和函数，使其和在边界上为零，从而消去这一项。

**定义 8.3.1（Dirichlet 问题的 Green 函数）** 对 $x\in\Omega$，设 $h^x\in C^2(\Omega)\cap C^1(\bar\Omega)$ 是问题

$$
\Delta_yh^x(y)=0\ \ (y\in\Omega),\qquad h^x(y)=\Gamma(y-x)\ \ (y\in\partial\Omega)
$$
的解。函数 $G(x,y)=\Gamma(y-x)-h^x(y)$（$x,y\in\Omega$，$x\ne y$）称为 $\Omega$ 中 Laplace 算子的 Dirichlet 问题的 **Green 函数**。

对固定的 $x$，$G(x,\cdot)$ 在 $\Omega\setminus\{x\}$ 中调和，在 $\partial\Omega$ 上为零，并在 $y=x$ 处具有基本解的奇性：它是位于接地导体面 $\partial\Omega$ 内部 $x$ 处的单位点电荷产生的势，而 $h^x$ 是导体上感应电荷产生的势。这是两点边值问题的 Green 函数（[2.4.12](/2.4.12#def-12.4.2)）——对单位点载荷的响应——在偏微分方程中的对应物。

**定理 8.3.1** 设 Green 函数存在，且关于 $y$ 直到 $\partial\Omega$ 都是 $C^1$ 的；设 $u\in C^2(\bar\Omega)$ 满足

$$
-\Delta u=f\ \text{ 在 }\Omega\text{ 内},\qquad u=g\ \text{ 在 }\partial\Omega\text{ 上}.
$$
则对 $x\in\Omega$，

$$
u(x)=\int_\Omega G(x,y)f(y)\,\mathrm{d}V_y-\oint_{\partial\Omega}g(y)\frac{\partial G}{\partial\boldsymbol{n}_y}(x,y)\,\mathrm{d}S_y.\tag{8.5}
$$

**证明** 对 $u$ 和在整个 $\Omega$ 中调和的 $h^x$ 应用 (8.2)：$-\int_\Omega h^x\Delta u=\oint_{\partial\Omega}\big(u\frac{\partial h^x}{\partial\boldsymbol{n}}-h^x\frac{\partial u}{\partial\boldsymbol{n}}\big)$。把这个恒等式写成 $0=\oint_{\partial\Omega}\big(u\frac{\partial h^x}{\partial\boldsymbol{n}}-h^x\frac{\partial u}{\partial\boldsymbol{n}}\big)\mathrm{d}S+\int_\Omega h^x\Delta u\,\mathrm{d}V$，加到 (8.4) 上。由于在 $\partial\Omega$ 上 $h^x=\Gamma(\cdot-x)$，含 $\frac{\partial u}{\partial\boldsymbol{n}}$ 的项相互抵消，剩下 $u(x)=-\oint u\frac{\partial G}{\partial\boldsymbol{n}_y}-\int G\Delta u$，这就是 (8.5)。$\square$

函数 $K(x,y)=-\frac{\partial G}{\partial\boldsymbol{n}_y}(x,y)$（$x\in\Omega$，$y\in\partial\Omega$）称为 $\Omega$ 的 Poisson 核（Poisson kernel）；用它，Laplace 方程的 Dirichlet 问题的解为 $u(x)=\oint_{\partial\Omega}K(x,y)g(y)\,\mathrm{d}S_y$。定理 8.3.1 假定了解的存在；对半空间和球，我们将直接验证 (8.5) 确实给出了解。

**定理 8.3.2** Green 函数有以下性质。

1. （对称性）当 $x\ne y$ 时 $G(x,y)=G(y,x)$；
2. （正性）当 $x\ne y$ 时 $G(x,y)>0$；当 $n\ge3$ 时还有 $G(x,y)<\Gamma(y-x)$；
3. $K(x,y)\ge0$，且对每个 $x\in\Omega$，$\displaystyle\oint_{\partial\Omega}K(x,y)\,\mathrm{d}S_y=1$。

**证明** 1：在 $\Omega$ 中固定 $x\ne z$，令 $v=G(x,\cdot)$，$w=G(z,\cdot)$。在挖去小球 $B(x,\varepsilon)$、$B(z,\varepsilon)$ 后的 $\Omega$ 上对 $v,w$ 应用 (8.2)。两个函数在那里都调和，并在 $\partial\Omega$ 上为零，所以两个小球面上的边界积分之和为 $0$。在 $x$ 附近，$w$ 光滑而 $v$ 具有 $\Gamma$ 的奇性；定理 8.1.3 证明中的计算表明，$\partial B(x,\varepsilon)$ 上的积分趋于 $-w(x)=-G(z,x)$，同样 $\partial B(z,\varepsilon)$ 上的积分趋于 $v(z)=G(x,z)$。因此 $G(x,z)=G(z,x)$。

2：由于 $h^x$ 在 $x$ 附近有界，$y\to x$ 时 $G(x,y)\to+\infty$。取 $\varepsilon$ 充分小，使 $G(x,\cdot)$ 在 $\bar B(x,\varepsilon)$ 上为正。在 $\Omega\setminus\bar B(x,\varepsilon)$ 上，$G(x,\cdot)$ 调和，在 $\partial B(x,\varepsilon)$ 上为正，在 $\partial\Omega$ 上为零，所以由强极小值原理，它在内部为正。当 $n\ge3$ 时，$h^x$ 是边界值 $\Gamma(y-x)$ 为正的调和函数，所以 $h^x>0$。

3：$G(x,\cdot)$ 在 $\Omega$ 中 $\ge0$，在 $\partial\Omega$ 上 $=0$，所以它的外法向导数 $\le0$。在 (8.5) 中取 $u\equiv1$（$f=0$，$g=1$）得 $\oint K\,\mathrm{d}S=1$。$\square$

对称性就是互易原理：$x$ 处的电荷在 $y$ 处产生的势，等于同一电荷位于 $y$ 时在 $x$ 处产生的势。求 $G$ 需要解一个 Dirichlet 问题，所以只有对特殊区域才知道 Green 函数的显式表达式。镜像法（method of images）对有对称性的区域给出 Green 函数：在 $\Omega$ 外放置一个虚构的电荷，使它的势在 $\partial\Omega$ 上与真实电荷的势相互抵消。

### 8.3.2. 半空间

设 $\Omega=\mathbb{R}^n_+=\{x:x_n>0\}$，$x^*=(x_1,\dots,x_{n-1},-x_n)$ 是 $x$ 关于平面 $x_n=0$ 的反射点。对该平面上的 $y$，$\lvert y-x\rvert=\lvert y-x^*\rvert$，所以

$$
G(x,y)=\Gamma(y-x)-\Gamma(y-x^*)
$$
在边界上为零；又因 $x^*\notin\Omega$，$\Gamma(\cdot-x^*)$ 在 $\Omega$ 中调和。外法向为 $-\boldsymbol{e}_n$。由 $\nabla\Gamma(z)=-\frac{z}{\omega_n\lvert z\rvert^n}$，在 $y_n=0$ 处

$$
\frac{\partial G}{\partial y_n}=-\frac{y_n-x_n}{\omega_n\lvert y-x\rvert^n}+\frac{y_n+x_n}{\omega_n\lvert y-x^*\rvert^n}=\frac{2x_n}{\omega_n\lvert y-x\rvert^n},
$$
所以半空间的 Poisson 核为 $K(x,y)=\frac{\partial G}{\partial y_n}=\frac{2x_n}{\omega_n\lvert x-y\rvert^n}$，而

$$
u(x)=\frac{2x_n}{\omega_n}\int_{\mathbb{R}^{n-1}}\frac{g(y)}{\lvert x-y\rvert^n}\,\mathrm{d}y\tag{8.6}
$$
是半空间中以 $g$ 为边界值的有界调和函数（对有界连续的 $g$；不加证明）。当 $n=2$ 时，把点记为 $(x,y)$，$y>0$，边界点记为 $(s,0)$，这就是 $u(x,y)=\frac y\pi\int\frac{g(s)}{(x-s)^2+y^2}\,\mathrm{d}s$，即 [2.5.6](/2.5.6#sec-6.4.3) 中用 Fourier 变换得到的公式。

### 8.3.3. 球与 Poisson 公式

设 $\Omega=B(0,R)$。对 $x\ne0$，令 $x^*=\frac{R^2}{\lvert x\rvert^2}x$ 为 $x$ 关于球面 $\lvert y\rvert=R$ 的反演点；它位于同一条射线上，在球外。对 $\lvert y\rvert=R$，

$$
\lvert y-x^*\rvert^2=R^2-\frac{2R^2\,x\cdot y}{\lvert x\rvert^2}+\frac{R^4}{\lvert x\rvert^2}=\frac{R^2}{\lvert x\rvert^2}\big(\lvert x\rvert^2-2x\cdot y+R^2\big)=\frac{R^2}{\lvert x\rvert^2}\lvert y-x\rvert^2,
$$
即 $\lvert y-x\rvert=\frac{\lvert x\rvert}{R}\lvert y-x^*\rvert$：球面是到 $x$ 与到 $x^*$ 的距离之比的一个等值面（Apollonius 球面）。由于 $\Gamma$ 只依赖于距离，函数

$$
G(x,y)=\Gamma(y-x)-\Gamma\Big(\frac{\lvert x\rvert}{R}(y-x^*)\Big)
$$
在 $\lvert y\rvert=R$ 时为零，且关于 $y\in B(0,R)\setminus\{x\}$ 调和：它就是球的 Green 函数（对 $x=0$，取 $G(0,y)=\Gamma(y)-\Gamma(R\boldsymbol{e})$，$\boldsymbol{e}$ 为任一单位向量）。当 $n=3$ 时，$G(x,y)=\frac1{4\pi}\big(\frac1{\lvert y-x\rvert}-\frac{R}{\lvert x\rvert\,\lvert y-x^*\rvert}\big)$：像电荷的强度为 $-R/\lvert x\rvert$。

![二维镜像法：Green 函数的等值线，源点 x（实心）与符号相反的像点 x*（空心）。左：半平面，像点是关于边界直线的反射。右：单位圆盘，像点位于反演点 x / |x|^2；边界圆周是一条等值线](./plots/method-of-images.py)

在 $\lvert y\rvert=R$ 上取 $\boldsymbol{n}=y/R$，利用 $\Gamma$ 的梯度计算法向导数，两项合并（利用 $\lvert y-x^*\rvert=\frac{R}{\lvert x\rvert}\lvert y-x\rvert$ 与 $x^*\cdot y=\frac{R^2}{\lvert x\rvert^2}x\cdot y$）为

$$
\frac{\partial G}{\partial\boldsymbol{n}_y}=-\frac{(R^2-x\cdot y)-(\lvert x\rvert^2-x\cdot y)}{R\,\omega_n\lvert x-y\rvert^n}=-\frac{R^2-\lvert x\rvert^2}{R\,\omega_n\lvert x-y\rvert^n}.
$$

**定理 8.3.3（Poisson 积分公式）** 设 $g$ 在球面 $\lvert y\rvert=R$ 上连续，定义

$$
u(x)=\frac{R^2-\lvert x\rvert^2}{\omega_nR}\oint_{\lvert y\rvert=R}\frac{g(y)}{\lvert x-y\rvert^n}\,\mathrm{d}S_y\quad(\lvert x\rvert<R),\qquad u(x)=g(x)\quad(\lvert x\rvert=R).\tag{8.7}
$$
则 $u$ 在球内调和，在闭球上连续：它就是 Dirichlet 问题的解。

**证明**（概要。）Poisson 核 $K(x,y)=\frac{R^2-\lvert x\rvert^2}{\omega_nR\lvert x-y\rvert^n}$ 当 $\lvert x\rvert<R$ 时关于 $x$ 调和（直接计算；或者：$K=-\frac{\partial G}{\partial\boldsymbol{n}_y}$，而由对称性 $G$ 关于 $x$ 调和），所以由积分号下求导，$u$ 调和。由定理 8.3.2，$K>0$ 且 $\oint K\,\mathrm{d}S_y=1$。在球面上固定 $y_0$ 与 $\delta>0$。当 $\lvert y-y_0\rvert\ge\delta$、$\lvert x-y_0\rvert<\delta/2$ 时，$\lvert x-y\rvert\ge\delta/2$，所以 $K(x,y)\le\frac{2^n(R^2-\lvert x\rvert^2)}{\omega_nR\delta^n}$，当 $x\to y_0$ 时趋于 $0$。因此 $K(x,\cdot)$ 集中于 $y_0$，[定理 7.1.2](/2.5.7#thm-7.1.2)（第 2 条）中近似单位元的论证表明 $u(x)\to g(y_0)$。$\square$

在 $x=0$ 处，公式 (8.7) 就是平均值性质。在平面上，令 $x=r\mathrm{e}^{\mathrm{i}\theta}$，$y=R\mathrm{e}^{\mathrm{i}\varphi}$，则 $\lvert x-y\rvert^2=R^2-2Rr\cos(\theta-\varphi)+r^2$，$\mathrm{d}S=R\,\mathrm{d}\varphi$，所以

$$
u(r,\theta)=\frac1{2\pi}\int_0^{2\pi}\frac{R^2-r^2}{R^2-2Rr\cos(\theta-\varphi)+r^2}\,g(\varphi)\,\mathrm{d}\varphi.\tag{8.8}
$$
对几何级数 $\sum_{m\in\mathbb{Z}}(r/R)^{\lvert m\rvert}\mathrm{e}^{\mathrm{i}m(\theta-\varphi)}$ 求和可知，核等于 $1+2\sum_{m\ge1}(r/R)^m\cos m(\theta-\varphi)$，所以 (8.8) 是 [2.5.4](/2.5.4) 中用**分离变量法**得到的圆盘上 Dirichlet 问题的 Fourier 级数解的闭合形式。

![左：单位圆盘的 Poisson 核作为 theta - phi 的函数；当 r → 1 时它集中于 theta = phi。右：在上半圆周上边界值为 1、下半圆周上为 0 的调和函数（例 8.4.1）](./plots/poisson-kernel-disk.py)

显式的核给出了对正调和函数的定量控制。

**定理 8.3.4（Harnack 不等式）** 设 $u\ge0$ 在 $B(0,R)$ 中调和，在其闭包上连续。则对 $\lvert x\rvert=r<R$，

$$
\frac{R^{n-2}(R-r)}{(R+r)^{n-1}}\,u(0)\le u(x)\le\frac{R^{n-2}(R+r)}{(R-r)^{n-1}}\,u(0).
$$

**证明** 对 $\lvert y\rvert=R$，$R-r\le\lvert x-y\rvert\le R+r$，所以 $\frac{R^2-r^2}{\omega_nR(R+r)^n}\le K(x,y)\le\frac{R^2-r^2}{\omega_nR(R-r)^n}$。乘以 $u(y)\ge0$，在球面上积分，并利用 $\oint u\,\mathrm{d}S=\omega_nR^{n-1}u(0)$（平均值性质）和 $R^2-r^2=(R-r)(R+r)$。$\square$

当 $n=2$ 时，上下界为 $\frac{R-r}{R+r}u(0)\le u(x)\le\frac{R+r}{R-r}u(0)$。Harnack 不等式说明，正调和函数不可能在一点很大、而在邻近的一点很小；令 $R\to\infty$，就得到正调和函数的 Liouville 定理的另一个证明。

## 8.4. 平面上的调和函数与共形映射

在二维情形，调和函数与解析函数是同一对象的两个侧面。

**定理 8.4.1** 设 $D\subset\mathbb{C}$ 是区域，把 $z=x+\mathrm{i}y$ 与 $(x,y)$ 等同。

1. 若 $F=u+\mathrm{i}v$ 在 $D$ 中解析，则 $u$ 与 $v$ 在 $D$ 中调和；
2. 若 $D$ 单连通，$u$ 在 $D$ 中调和，则 $u=\operatorname{Re}F$，其中 $F$ 是 $D$ 中的解析函数，在相差一个纯虚常数的意义下唯一。

**证明** 1：解析函数无穷次可微（[2.3.4](/2.3.4)），对 **Cauchy–Riemann 方程** $u_x=v_y$，$u_y=-v_x$ 求导得 $u_{xx}+u_{yy}=v_{yx}-v_{xy}=0$，$v$ 同理。2：$F'$ 应当是 $u_x-\mathrm{i}u_y$。由于 $u$ 调和且是 $C^2$ 的，这个函数满足 Cauchy–Riemann 方程，因而解析；在单连通区域上它有原函数 $F$（由 Cauchy 积分定理），调整常数即得 $\operatorname{Re}F=u$。共轭调和函数 $v=\operatorname{Im}F$ 的构造见 [2.3.2](/2.3.2)。$\square$

应用的关键在于：调和性在解析映射所作的变量代换下保持不变。

**定理 8.4.2** 设 $f$ 在 $D$ 中解析，把 $D$ 映入区域 $D'$，$U$ 在 $D'$ 中调和。则 $u=U\circ f$ 在 $D$ 中调和，且

$$
\Delta u(z)=\lvert f'(z)\rvert^2\,(\Delta U)(f(z)).
$$

**证明** 调和性是局部性质。在 $w_0=f(z_0)$ 附近，$U$ 在一个小圆盘上可以写成 $U=\operatorname{Re}H$，$H$ 解析（定理 8.4.1 第 2 条），所以在 $z_0$ 附近 $u=\operatorname{Re}(H\circ f)$ 是解析函数的实部，由第 1 条知它调和。公式由链式法则和 $f$ 的 Cauchy–Riemann 方程得到，后者说明 $f$ 的 Jacobi 矩阵是 $\lvert f'\rvert$ 乘以一个旋转。$\square$

这就给出了平面区域 $D$ 上 Dirichlet 问题的一种方法：找一个**共形映射** $w=f(z)$，把 $D$ 映到问题容易求解的区域 $D'$ 上（单位圆盘，用公式 (8.8)；或上半平面，用公式 (8.6)），把边界值转移过去，在 $D'$ 中求解，再与 $f$ 复合。Riemann 映射定理（[2.3.8](/2.3.8)）保证 $\mathbb{C}$ 的每个单连通真子区域都能共形映射到圆盘上，而 [2.3.8](/2.3.8) 中的显式映射目录涵盖了许多有实际意义的区域。

**例 8.4.1** 求单位圆盘中的调和函数，使其在上半圆周上的边界值为 $1$，在下半圆周上为 $0$。

**解** 在上半平面中，$U(w)=\frac1\pi\operatorname{Arg}w$ 调和（它等于 $\frac1\pi\operatorname{Im}\operatorname{Log}w$），在负实轴上等于 $1$，在正实轴上等于 $0$。分式线性变换 $w=f(z)=\mathrm{i}\frac{1+z}{1-z}$ 把单位圆盘映为上半平面，$f(1)=\infty$，$f(\mathrm{i})=-1$，$f(-1)=0$；因此它把上半圆周映为负实轴，把下半圆周映为正实轴。所以

$$
u(z)=\frac1\pi\operatorname{Arg}\Big(\mathrm{i}\frac{1+z}{1-z}\Big)=\frac12+\frac1\pi\arctan\frac{2r\sin\theta}{1-r^2},\qquad z=r\mathrm{e}^{\mathrm{i}\theta},
$$
其中第二种形式由 $\mathrm{i}\frac{1+z}{1-z}=\frac{-2r\sin\theta+\mathrm{i}(1-r^2)}{\lvert1-z\rvert^2}$（其虚部为正）得到。在圆心处 $u(0)=\frac12$，即边界值的平均值。用 Poisson 公式 (8.8) 计算也能得到同一个函数，但要费事得多；它的等值线是过 $\pm1$ 的圆弧，即 $w$ 平面中从 $0$ 出发的射线的像。

这种相互作用是双向的：复分析给出显式的调和函数，调和函数则是平面物理场的模型。对二维理想流体的流动或静电场，势 $\phi$ 与流函数（或通量函数）$\psi$ 组合成复势 $\phi+\mathrm{i}\psi$，它是一个解析函数；曲线族 $\phi=\text{常数}$ 与 $\psi=\text{常数}$ 是相互正交的等势线与流线（[2.3.8](/2.3.8)）。

## 8.5. Dirichlet 原理

薄膜或温度场的稳态使某个能量取极小值。对 Poisson 方程，能量为

$$
E[w]=\int_\Omega\Big(\frac12\lvert\nabla w\rvert^2-fw\Big)\mathrm{d}V,
$$
它定义在容许函数类 $\mathcal{A}=\{w\in C^2(\bar\Omega):\text{在 }\partial\Omega\text{ 上 }w=g\}$ 上。

**定理 8.5.1（Dirichlet 原理）** 函数 $u\in\mathcal{A}$ 在 $\Omega$ 中满足 $-\Delta u=f$，当且仅当 $E[u]=\min_{w\in\mathcal{A}}E[w]$。

**证明** 每个 $w\in\mathcal{A}$ 都可以写成 $w=u+v$，其中 $v\in C^2(\bar\Omega)$，在 $\partial\Omega$ 上 $v=0$。展开得

$$
E[u+v]=E[u]+\int_\Omega\big(\nabla u\cdot\nabla v-fv\big)\,\mathrm{d}V+\frac12\int_\Omega\lvert\nabla v\rvert^2\,\mathrm{d}V.
$$
由 (8.1) 以及在 $\partial\Omega$ 上 $v=0$，中间一项等于 $\int_\Omega(-\Delta u-f)v\,\mathrm{d}V$。

若 $-\Delta u=f$，则中间一项为零，$E[w]=E[u]+\frac12\int\lvert\nabla v\rvert^2\ge E[u]$：$u$ 是极小元（而且是唯一的极小元，因为等号成立迫使 $\nabla v\equiv\boldsymbol{0}$，从而 $v\equiv0$）。

反之，若 $u$ 使 $E$ 取极小值，则对每个这样的 $v$，函数 $i(\varepsilon)=E[u+\varepsilon v]=E[u]+\varepsilon\int(-\Delta u-f)v+\frac{\varepsilon^2}2\int\lvert\nabla v\rvert^2$ 在 $\varepsilon=0$ 处取极小值，所以 $i'(0)=\int_\Omega(-\Delta u-f)v\,\mathrm{d}V=0$。由于 $v$ 是在 $\partial\Omega$ 上为零的任意 $C^2$ 函数，由**变分学基本引理**的多元形式得 $-\Delta u-f\equiv0$。$\square$

因此方程 $-\Delta u=f$ 是泛函 $E$ 的 **Euler–Lagrange 方程**，与 [2.4.13](/2.4.13) 完全一样，只是换成了多元函数：能量取驻值给出平衡方程，而自由边界的自然边界条件是 $\frac{\partial u}{\partial\boldsymbol{n}}=0$。Riemann 在 1850 年前后用 Dirichlet 原理来断言解的存在，并认为极小值理所当然能够取到。Weierstrass 指出，有下界的泛函在给定的函数类中不一定能取到下确界；这一漏洞直到 1900 年前后才由 Hilbert 弥补，他的工作引出了现代的方法：在导数平方可积的更大的函数空间（Sobolev 空间）中求极小，那里极小元存在，然后再证明它是光滑的。同样的变分形式也是有限元方法的出发点，后者在网格上的分片多项式函数中使 $E$ 取极小。

## 小结

| 主题 | 内容 |
|---|---|
| Green 公式 | $\int(v\Delta u+\nabla u\cdot\nabla v)=\oint v\partial_{\boldsymbol{n}}u$；$\int(u\Delta v-v\Delta u)=\oint(u\partial_{\boldsymbol{n}}v-v\partial_{\boldsymbol{n}}u)$ |
| Neumann 问题 | 仅当 $\int_\Omega f+\oint_{\partial\Omega}g=0$ 时可解；解在相差一个常数的意义下唯一 |
| 基本解 | $-\frac1{2\pi}\ln\lvert x\rvert$（$n=2$），$\frac1{4\pi\lvert x\rvert}$（$n=3$）；$-\Delta\Gamma=\delta$ |
| 平均值性质 | $u(x)$ 是 $u$ 在以 $x$ 为中心的每个球面和球体上的平均值 |
| 极值原理 | 除非为常数，否则没有内部极值；$\min_{\partial\Omega}u\le u\le\max_{\partial\Omega}u$；唯一性与稳定性 |
| Liouville、Harnack | $\mathbb{R}^n$ 上有界的调和函数是常数；圆盘中 $\frac{R-r}{R+r}u(0)\le u(x)\le\frac{R+r}{R-r}u(0)$ |
| Green 函数 | $G(x,y)=\Gamma(y-x)-h^x(y)$，在 $\partial\Omega$ 上为零，对称，为正；$u=\int Gf-\oint g\,\partial_{\boldsymbol{n}_y}G$ |
| 镜像法 | 半空间：反射 $x$；球：反演点 $x^*=R^2x/\lvert x\rvert^2$，强度为 $(R/\lvert x\rvert)^{n-2}$ |
| Poisson 公式 | 球：$u=\frac{R^2-\lvert x\rvert^2}{\omega_nR}\oint\frac{g}{\lvert x-y\rvert^n}$；圆盘：核为 $\frac{R^2-r^2}{R^2-2Rr\cos(\theta-\varphi)+r^2}$ |
| 平面 | 解析函数的实部；在共形映射下不变 |
| Dirichlet 原理 | $-\Delta u=f$，$u=g$ $\iff$ $u$ 在边界值为 $g$ 的 $w$ 中使 $\int(\frac12\lvert\nabla w\rvert^2-fw)$ 取极小 |
