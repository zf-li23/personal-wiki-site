---
title: 曲线积分与曲面积分
---

[2.2.12](/2.2.12) 的**重积分**在平面区域与空间区域上积分。物理中还有许多量分布在曲线或曲面上：弯曲细丝的质量、薄壳的质量与转动惯量，是数量函数沿曲线、曲面的积分，与方向无关，称为第一型积分；变力沿路径做的功、流体穿过曲面的流量，是向量场沿有向曲线、有向曲面的积分，改变方向就变号，称为第二型积分。四类积分的定义都沿用"分割、近似、求和、取极限"，计算的基本方法都是参数化：把曲线积分化为**定积分**，把曲面积分化为**二重积分**，关键在于弧长元 $\mathrm{d}l$、面积元 $\mathrm{d}S$ 的表达式和方向的处理。

本章的另一个主题是 Green 公式：平面区域上的二重积分等于沿边界的第二型曲线积分。它是**微积分基本定理** $\int_a^bf'(x)\,\mathrm{d}x=f(b)-f(a)$ 在二维的推广——"区域上导数的积分 = 边界上的积分"。[2.2.14](/2.2.14) 把它推广为空间中的 Gauss 公式与 Stokes 公式，并用散度、旋度、保守场的语言系统地解释这些公式；复变函数中的 Cauchy 积分定理也以 Green 公式为基础。本章用到 [2.2.11](/2.2.11) 的切向量、法向量与向量积，以及 [2.2.12](/2.2.12) 的重积分计算与变量替换。

## 13.1. 第一型曲线积分

### 13.1.1. 定义与性质

设一根弯曲的细丝 $L$ 上各点的线密度为 $\rho(x,y,z)$，求其质量。把 $L$ 分成小段 $L_1,\dots,L_n$，第 $i$ 段长 $\Delta l_i$，在其上任取一点 $P_i$，小段的质量近似为 $\rho(P_i)\Delta l_i$，求和后令分割无限加细，就得到质量。

**定义 13.1.1（第一型曲线积分）** 设 $L\subset\mathbb{R}^3$ 是一条可求长曲线，函数 $f$ 在 $L$ 上有定义。把 $L$ 任意分成 $n$ 个小弧段 $L_1,\dots,L_n$，$\Delta l_i$ 为 $L_i$ 的弧长，$\lambda=\max_i\Delta l_i$，任取 $P_i\in L_i$。若极限 $\lim\limits_{\lambda\to0}\sum_{i=1}^nf(P_i)\Delta l_i$ 存在，且与分割和取点无关，则称它为 $f$ 在 $L$ 上的**第一型曲线积分**，记作

$$
\int_Lf(x,y,z)\,\mathrm{d}l.
$$
$L$ 是闭曲线时记作 $\oint_Lf\,\mathrm{d}l$；平面曲线上的积分 $\int_Lf(x,y)\,\mathrm{d}l$ 同样定义。

$f\equiv1$ 时积分是 $L$ 的**弧长**；$f=\rho$ 时是质量；$L$ 在 $xOy$ 平面内且 $f\ge0$ 时，$\int_Lf\,\mathrm{d}l$ 是以 $L$ 为准线、母线平行于 $z$ 轴、高为 $f(x,y)$ 的柱面片的面积。

**性质 13.1.1** 设 $f,g$ 在 $L$ 上的第一型曲线积分都存在。

- 线性：$\int_L(\alpha f+\beta g)\,\mathrm{d}l=\alpha\int_Lf\,\mathrm{d}l+\beta\int_Lg\,\mathrm{d}l$。
- 可加性：若 $L$ 由 $L_1$、$L_2$ 首尾相接而成，则 $\int_L=\int_{L_1}+\int_{L_2}$。
- 保序性：若在 $L$ 上 $f\le g$，则 $\int_Lf\,\mathrm{d}l\le\int_Lg\,\mathrm{d}l$。
- 无方向性：积分与 $L$ 的走向无关，因为 $\Delta l_i$ 总是正的。

与**重积分**一样，第一型曲线积分可以利用对称性：若 $L$ 关于 $y$ 轴对称，$f$ 关于 $x$ 是奇函数，则 $\int_Lf\,\mathrm{d}l=0$；若 $L$ 的方程关于 $x,y$ 轮换对称，则 $\int_Lf(x,y)\,\mathrm{d}l=\int_Lf(y,x)\,\mathrm{d}l$。

### 13.1.2. 计算

**定理 13.1.1** 设 $L$ 是**光滑曲线** $\boldsymbol{r}(t)=(x(t),y(t),z(t))$，$\alpha\le t\le\beta$（$x,y,z$ 有连续导数且 $\boldsymbol{r}'(t)\ne\boldsymbol{0}$），$f$ 在 $L$ 上连续，则

$$
\int_Lf\,\mathrm{d}l=\int_\alpha^\beta f(x(t),y(t),z(t))\sqrt{x'(t)^2+y'(t)^2+z'(t)^2}\,\mathrm{d}t.
$$

**证明** 取 $[\alpha,\beta]$ 的分割 $\alpha=t_0<t_1<\cdots<t_n=\beta$，对应 $L$ 的分割。由弧长公式与**积分中值定理**，$\Delta l_i=\int_{t_{i-1}}^{t_i}\|\boldsymbol{r}'(t)\|\,\mathrm{d}t=\|\boldsymbol{r}'(\tau_i)\|\Delta t_i$，$\tau_i\in[t_{i-1},t_i]$。取 $P_i=\boldsymbol{r}(\tau_i)$，则 $\sum f(P_i)\Delta l_i=\sum f(\boldsymbol{r}(\tau_i))\|\boldsymbol{r}'(\tau_i)\|\Delta t_i$ 是右端定积分的 **Riemann 和**。由于 $\|\boldsymbol{r}'\|$ 有正的下界，$\max\Delta t_i\to0$ 与 $\lambda\to0$ 等价，取极限即得。$\square$

公式中的 $\mathrm{d}l=\|\boldsymbol{r}'(t)\|\,\mathrm{d}t$ 是弧长元。由于 $\mathrm{d}l>0$，定积分的下限必须小于上限，这与后面的第二型积分不同。常用的弧长元：

| 曲线的表示 | 弧长元 $\mathrm{d}l$ |
|---|---|
| 空间参数曲线 $\boldsymbol{r}(t)$ | $\sqrt{x'^2+y'^2+z'^2}\,\mathrm{d}t$ |
| 平面曲线 $y=y(x)$ | $\sqrt{1+y'(x)^2}\,\mathrm{d}x$ |
| **极坐标** $r=r(\theta)$ | $\sqrt{r^2+r'(\theta)^2}\,\mathrm{d}\theta$ |

**例 13.1.1** 圆周 $x^2+y^2=2y$ 上分布着质量，点 $(x,y)$ 处的线密度为 $\sqrt{x^2+y^2}$，求总质量 $M$。

解法一：参数方程 $x=\cos t$，$y=1+\sin t$，$0\le t\le2\pi$，$\mathrm{d}l=\mathrm{d}t$，

$$
M=\int_0^{2\pi}\sqrt{2+2\sin t}\,\mathrm{d}t=\int_0^{2\pi}\sqrt{2}\sqrt{1+\sin t}\,\mathrm{d}t=8.
$$
（令 $t=s-\frac\pi2$，$1+\sin t=1-\cos s=2\sin^2\frac s2$，积分为 $2\int_0^{2\pi}\sin\frac s2\,\mathrm{d}s=8$。）

解法二：极坐标方程 $r=2\sin\theta$，$0\le\theta\le\pi$，$\mathrm{d}l=\sqrt{r^2+r'^2}\,\mathrm{d}\theta=2\,\mathrm{d}\theta$，被积函数 $\sqrt{x^2+y^2}=r$，所以 $M=\int_0^\pi2\sin\theta\cdot2\,\mathrm{d}\theta=8$。选好坐标可以大大简化计算。

**例 13.1.2** 求柱面 $x^2+y^2=ax$（$a>0$）含在球面 $x^2+y^2+z^2=a^2$ 内的部分的面积。柱面的准线是 $xOy$ 面上的圆 $L\colon r=a\cos\theta$（$|\theta|\le\frac\pi2$），$\mathrm{d}l=a\,\mathrm{d}\theta$；柱面在点 $(x,y)$ 上方、下方的高度都是 $\sqrt{a^2-x^2-y^2}$。由第一型曲线积分的几何意义，

$$
S=2\int_L\sqrt{a^2-x^2-y^2}\,\mathrm{d}l=2\int_{-\pi/2}^{\pi/2}\sqrt{a^2-a^2\cos^2\theta}\,a\,\mathrm{d}\theta=2a^2\int_{-\pi/2}^{\pi/2}|\sin\theta|\,\mathrm{d}\theta=4a^2.
$$

**例 13.1.3** 曲线 $L\colon x^2+y^2+z^2=4$，$x^2+y^2=2x$，$z\ge0$ 上点 $(x,y,z)$ 处的线密度为 $|xyz|$，求 $L$ 的质量。参数方程为 $x=1+\cos t$，$y=\sin t$，$z=\sqrt{4-2x}=2\sin\frac t2$（$0\le t\le2\pi$），$\mathrm{d}l=\sqrt{1+\cos^2\frac t2}\,\mathrm{d}t$。用半角写 $x=2\cos^2\frac t2$，$y=2\sin\frac t2\cos\frac t2$，令 $u=\frac t2$，

$$
m=\int_0^{\pi}8\,|\cos^3u|\sin^2u\sqrt{1+\cos^2u}\cdot2\,\mathrm{d}u=32\int_0^{\pi/2}\cos^3u\sin^2u\sqrt{1+\cos^2u}\,\mathrm{d}u.
$$
令 $s=\sin u$，化为 $32\int_0^1(1-s^2)s^2\sqrt{2-s^2}\,\mathrm{d}s$；再令 $s=\sqrt2\sin\varphi$，被积式变为 $\cos2\varphi\sin^22\varphi\,\mathrm{d}\varphi$，所以

$$
m=32\int_0^{\pi/4}\cos2\varphi\sin^22\varphi\,\mathrm{d}\varphi=32\cdot\frac16=\frac{16}3.
$$

**例 13.1.4** 设 $L$ 为椭圆 $x^2+4y^2=4$，计算 $\oint_L\sqrt{1+3y^2}\,\mathrm{d}l$。取 $x=2\cos t$，$y=\sin t$，$\mathrm{d}l=\sqrt{4\sin^2t+\cos^2t}\,\mathrm{d}t=\sqrt{1+3\sin^2t}\,\mathrm{d}t$，恰与被积函数相同，所以积分为 $\int_0^{2\pi}(1+3\sin^2t)\,\mathrm{d}t=2\pi+3\pi=5\pi$。

## 13.2. 曲面面积与第一型曲面积分

### 13.2.1. 曲面面积

一元情形中，弧长由内接折线的极限定义。曲面的面积不能用内接多面体的极限定义（Schwarz 给出过内接多面体面积趋于无穷的例子），而用切平面来近似：把曲面 $S$ 分成小片 $\Delta S_i$，每一小片用它在某点的**切平面**上的一小片代替。若小片在 $xOy$ 面上的投影面积为 $\Delta\sigma_i$，切平面与 $xOy$ 面的夹角为 $\gamma_i$（即**法向量**与 $z$ 轴的夹角），则 $\Delta S_i\approx\Delta\sigma_i/|\cos\gamma_i|$。

**定义 13.2.1（曲面面积）** 设光滑曲面 $S$ 的方程为 $z=z(x,y)$，$(x,y)\in D_{xy}$，$z$ 在有界闭区域 $D_{xy}$ 上有连续偏导数。称

$$
\iint_{D_{xy}}\frac{\mathrm{d}\sigma}{|\cos\gamma|}=\iint_{D_{xy}}\sqrt{1+z_x^2+z_y^2}\,\mathrm{d}x\,\mathrm{d}y
$$
为 $S$ 的**曲面面积**，$\mathrm{d}S=\sqrt{1+z_x^2+z_y^2}\,\mathrm{d}x\,\mathrm{d}y$ 称为面积元。

这里法向量为 $(-z_x,-z_y,1)$，$|\cos\gamma|=1/\sqrt{1+z_x^2+z_y^2}$。曲面写成 $x=x(y,z)$ 或 $y=y(z,x)$ 时，向相应的坐标面投影，公式类似。

**定理 13.2.1（参数曲面的面积元）** 设光滑曲面 $S$ 由 $\boldsymbol{r}(u,v)=(x(u,v),y(u,v),z(u,v))$，$(u,v)\in D_{uv}$ 一一地给出，各分量有连续偏导数，$\boldsymbol{r}_u\times\boldsymbol{r}_v\ne\boldsymbol{0}$，则 $S$ 的面积为

$$
\iint_{D_{uv}}\|\boldsymbol{r}_u\times\boldsymbol{r}_v\|\,\mathrm{d}u\,\mathrm{d}v=\iint_{D_{uv}}\sqrt{A^2+B^2+C^2}\,\mathrm{d}u\,\mathrm{d}v=\iint_{D_{uv}}\sqrt{EG-F^2}\,\mathrm{d}u\,\mathrm{d}v,
$$
其中 $A=\det\dfrac{\partial(y,z)}{\partial(u,v)}$，$B=\det\dfrac{\partial(z,x)}{\partial(u,v)}$，$C=\det\dfrac{\partial(x,y)}{\partial(u,v)}$ 是 $\boldsymbol{r}_u\times\boldsymbol{r}_v$ 的分量（定义 11.1.1 与 [2.2.11](/2.2.11) 的参数曲面一节），$E=\|\boldsymbol{r}_u\|^2$，$F=\boldsymbol{r}_u\cdot\boldsymbol{r}_v$，$G=\|\boldsymbol{r}_v\|^2$。

**证明** 参数域中的小矩形 $[u,u+\Delta u]\times[v,v+\Delta v]$ 被映成曲面上的小片，它近似于以 $\boldsymbol{r}_u\Delta u$、$\boldsymbol{r}_v\Delta v$ 为邻边的平行四边形，面积为 $\|\boldsymbol{r}_u\times\boldsymbol{r}_v\|\Delta u\Delta v$。与定义 13.2.1 一致：若在某块上 $C\ne0$，由**隐函数定理**可把曲面写成 $z=z(x,y)$，此时 $z_x=-A/C$，$z_y=-B/C$，按**二重积分**的换元公式（定理 12.4.1）$\mathrm{d}x\,\mathrm{d}y=|C|\,\mathrm{d}u\,\mathrm{d}v$，故

$$
\sqrt{1+z_x^2+z_y^2}\,\mathrm{d}x\,\mathrm{d}y=\frac{\sqrt{A^2+B^2+C^2}}{|C|}\,|C|\,\mathrm{d}u\,\mathrm{d}v.
$$
等式 $\|\boldsymbol{r}_u\times\boldsymbol{r}_v\|^2=\|\boldsymbol{r}_u\|^2\|\boldsymbol{r}_v\|^2-(\boldsymbol{r}_u\cdot\boldsymbol{r}_v)^2$ 由向量积的定义直接验证。$\square$

球面 $\boldsymbol{r}(\varphi,\theta)=(R\sin\varphi\cos\theta,R\sin\varphi\sin\theta,R\cos\varphi)$（**球坐标**中 $\rho=R$）的面积元为 $\mathrm{d}S=R^2\sin\varphi\,\mathrm{d}\varphi\,\mathrm{d}\theta$，球面面积为 $\int_0^{2\pi}\mathrm{d}\theta\int_0^\pi R^2\sin\varphi\,\mathrm{d}\varphi=4\pi R^2$。若用 $z=\sqrt{R^2-x^2-y^2}$ 投影计算，面积元 $\frac{R}{\sqrt{R^2-x^2-y^2}}\,\mathrm{d}x\,\mathrm{d}y$ 在赤道上无界，二重积分是**反常积分**；参数法避免了这个问题。

**例 13.2.1** 球面 $x^2+y^2+z^2=a^2$ 与柱面 $x^2+y^2=ax$（$a>0$）。

（1）球面含在柱面内的部分的面积。上半球面 $z_x=-\frac xz$，$z_y=-\frac yz$，$\sqrt{1+z_x^2+z_y^2}=\frac{a}{z}$，投影区域 $D\colon r\le a\cos\theta$，

$$
S_1=2\iint_D\frac{a}{\sqrt{a^2-x^2-y^2}}\,\mathrm{d}\sigma=2\int_{-\pi/2}^{\pi/2}\mathrm{d}\theta\int_0^{a\cos\theta}\frac{ar}{\sqrt{a^2-r^2}}\,\mathrm{d}r=4a^2\int_0^{\pi/2}(1-\sin\theta)\,\mathrm{d}\theta=2a^2(\pi-2).
$$

（2）柱面含在球面内的部分的面积已在例 13.1.2 中算出，为 $4a^2$。若用投影法，柱面垂直于 $xOy$ 面，在 $xOy$ 面上的投影是一条曲线，不能向 $xOy$ 面投影；应把柱面写成 $y=\pm\sqrt{ax-x^2}$ 向 $zOx$ 面投影，投影区域由交线消去 $y$ 得到：$z^2\le a(a-x)$，$0\le x\le a$，计算结果相同。

**例 13.2.2** 旋转抛物面 $z=x^2+y^2$ 被 $z=2$ 截下的部分（即 $(x,y)\in\{x^2+y^2\le2\}$）的面积为

$$
\iint_{x^2+y^2\le2}\sqrt{1+4x^2+4y^2}\,\mathrm{d}x\,\mathrm{d}y=2\pi\int_0^{\sqrt2}\sqrt{1+4r^2}\,r\,\mathrm{d}r=\frac{\pi}{6}(1+4r^2)^{3/2}\Big|_0^{\sqrt2}=\frac{13\pi}3.
$$

### 13.2.2. 第一型曲面积分

**定义 13.2.2（第一型曲面积分）** 设 $S\subset\mathbb{R}^3$ 是有界光滑（或分片光滑）曲面，$f$ 在 $S$ 上有定义。把 $S$ 任意分成小片 $S_1,\dots,S_n$，$\Delta S_i$ 为 $S_i$ 的面积，$\lambda$ 为各小片直径的最大值，任取 $P_i\in S_i$。若 $\lim\limits_{\lambda\to0}\sum_{i=1}^nf(P_i)\Delta S_i$ 存在，且与分割和取点无关，则称它为 $f$ 在 $S$ 上的**第一型曲面积分**，记作 $\iint_Sf(x,y,z)\,\mathrm{d}S$；$S$ 是闭曲面时记作 $\oiint_Sf\,\mathrm{d}S$。

$f\equiv1$ 时积分是曲面面积，$f$ 为面密度时是曲面薄壳的质量。性质与第一型曲线积分相同：线性、对曲面的可加性（分片）、保序性、无方向性，以及对称性与轮换对称性。

**定理 13.2.2** 设 $f$ 在 $S$ 上连续。

- 若 $S\colon z=z(x,y)$，$(x,y)\in D_{xy}$，则 $\iint_Sf\,\mathrm{d}S=\iint_{D_{xy}}f(x,y,z(x,y))\sqrt{1+z_x^2+z_y^2}\,\mathrm{d}x\,\mathrm{d}y$。
- 若 $S\colon\boldsymbol{r}(u,v)$，$(u,v)\in D_{uv}$，则 $\iint_Sf\,\mathrm{d}S=\iint_{D_{uv}}f(\boldsymbol{r}(u,v))\,\|\boldsymbol{r}_u\times\boldsymbol{r}_v\|\,\mathrm{d}u\,\mathrm{d}v$。

证明与定理 13.1.1 相同：面积元的公式加上积分中值定理。向坐标面投影时要注意：投影必须是一一的。若曲面在投影方向上有"两层"（如球面向 $xOy$ 面投影），要分成上下两片分别计算；若曲面某部分垂直于投影面，则它不能向该面投影。

**例 13.2.3** 设 $S$ 是四面体 $x+y+z\le1$，$x,y,z\ge0$ 的表面，计算 $\oiint_S\dfrac{\mathrm{d}S}{(1+x+y)^2}$。分四个面计算。底面 $z=0$：$\mathrm{d}S=\mathrm{d}x\,\mathrm{d}y$，

$$
\int_0^1\mathrm{d}x\int_0^{1-x}\frac{\mathrm{d}y}{(1+x+y)^2}=\int_0^1\Big(\frac1{1+x}-\frac12\Big)\mathrm{d}x=\ln2-\frac12.
$$
斜面 $z=1-x-y$：$\mathrm{d}S=\sqrt3\,\mathrm{d}x\,\mathrm{d}y$，积分为 $\sqrt3(\ln2-\frac12)$。侧面 $x=0$：向 $yOz$ 面投影，$\int_0^1\mathrm{d}y\int_0^{1-y}\frac{\mathrm{d}z}{(1+y)^2}=\int_0^1\frac{1-y}{(1+y)^2}\,\mathrm{d}y=1-\ln2$；侧面 $y=0$ 同理为 $1-\ln2$。所以

$$
\oiint_S\frac{\mathrm{d}S}{(1+x+y)^2}=(1+\sqrt3)\Big(\ln2-\frac12\Big)+2(1-\ln2)=(\sqrt3-1)\ln2+\frac{3-\sqrt3}2.
$$

**例 13.2.4** 设 $S$ 是球面 $x^2+y^2+z^2=R^2$ 在 $z\ge0$ 的部分，计算 $\iint_S(x+y+z)\,\mathrm{d}S$。$S$ 关于 $yOz$ 面、$zOx$ 面对称，$x$、$y$ 分别是奇函数，所以 $\iint_Sx\,\mathrm{d}S=\iint_Sy\,\mathrm{d}S=0$。

解法一（投影）：$\mathrm{d}S=\frac Rz\,\mathrm{d}x\,\mathrm{d}y$，$\iint_Sz\,\mathrm{d}S=\iint_{x^2+y^2\le R^2}R\,\mathrm{d}x\,\mathrm{d}y=\pi R^3$。

解法二（参数）：$\mathrm{d}S=R^2\sin\varphi\,\mathrm{d}\varphi\,\mathrm{d}\theta$，$\iint_Sz\,\mathrm{d}S=\int_0^{2\pi}\mathrm{d}\theta\int_0^{\pi/2}R\cos\varphi\cdot R^2\sin\varphi\,\mathrm{d}\varphi=\pi R^3$。

所以积分为 $\pi R^3$。

**例 13.2.5** 求锥面 $z=\sqrt{x^2+y^2}$ 被柱面 $x^2+y^2=ax$（$a>0$）割下部分的形心（均匀薄壳的**质心**）。$z_x^2+z_y^2=1$，$\mathrm{d}S=\sqrt2\,\mathrm{d}x\,\mathrm{d}y$，投影区域 $D\colon r\le a\cos\theta$ 是半径 $\frac a2$ 的圆盘。

$$
\iint_S\mathrm{d}S=\frac{\sqrt2\pi a^2}4,\qquad\iint_Sx\,\mathrm{d}S=\sqrt2\iint_Dx\,\mathrm{d}\sigma=\sqrt2\cdot\frac{\pi a^2}4\cdot\frac a2,
$$

$$
\iint_Sz\,\mathrm{d}S=\sqrt2\int_{-\pi/2}^{\pi/2}\mathrm{d}\theta\int_0^{a\cos\theta}r^2\,\mathrm{d}r=\frac{\sqrt2a^3}3\int_{-\pi/2}^{\pi/2}\cos^3\theta\,\mathrm{d}\theta=\frac{4\sqrt2a^3}9.
$$
由对称性 $\bar y=0$，所以形心为 $\big(\frac a2,0,\frac{16a}{9\pi}\big)$。

**例 13.2.6** 设 $S$ 是圆柱体 $x^2+y^2\le R^2$，$0\le z\le H$ 的表面，求 $\oiint_S(x^2+y^2+z^2)\,\mathrm{d}S$（均匀薄壳关于原点的**转动惯量**）。下底 $z=0$：$\iint(x^2+y^2)\,\mathrm{d}x\,\mathrm{d}y=\frac{\pi R^4}2$；上底 $z=H$：$\frac{\pi R^4}2+\pi R^2H^2$；侧面用柱面参数 $x=R\cos\theta$，$y=R\sin\theta$，$z=z$，$\mathrm{d}S=R\,\mathrm{d}\theta\,\mathrm{d}z$：

$$
\int_0^{2\pi}\mathrm{d}\theta\int_0^H(R^2+z^2)R\,\mathrm{d}z=2\pi R\Big(R^2H+\frac{H^3}3\Big).
$$
总和为 $\pi R^4+2\pi R^3H+\pi R^2H^2+\frac23\pi RH^3$。侧面也可写成 $x=\pm\sqrt{R^2-y^2}$ 向 $yOz$ 面投影（分前后两片），结果相同，但计算更繁。

## 13.3. 有向曲线与第二型曲线积分

### 13.3.1. 向量场与有向曲线

物理学把发生某种物理现象的空间区域称为场。温度、密度、电势在每点取一个数，速度、力、电场强度在每点取一个向量。

**定义 13.3.1（数量场与向量场）** 设 $\Omega\subset\mathbb{R}^3$ 是区域。定义在 $\Omega$ 上的函数 $f\colon\Omega\to\mathbb{R}$ 称为 $\Omega$ 上的**数量场**；映射 $\boldsymbol{v}\colon\Omega\to\mathbb{R}^3$，

$$
\boldsymbol{v}(x,y,z)=X(x,y,z)\boldsymbol{i}+Y(x,y,z)\boldsymbol{j}+Z(x,y,z)\boldsymbol{k}=(X,Y,Z),
$$
称为 $\Omega$ 上的**向量场**。若 $X,Y,Z$ 都连续，称 $\boldsymbol{v}$ 为连续向量场；若 $X,Y,Z$ 都有连续偏导数，称 $\boldsymbol{v}$ 为连续可微向量场。平面向量场 $\boldsymbol{v}=(X(x,y),Y(x,y))$ 同样定义。

例如，位于 $P_0(x_0,y_0,z_0)$、质量为 $M$ 的质点对位于 $P(x,y,z)$、质量为 $m$ 的质点的万有引力为

$$
\boldsymbol{F}(x,y,z)=-\frac{GMm}{\|\boldsymbol{r}\|^3}\boldsymbol{r},\qquad\boldsymbol{r}=(x-x_0,y-y_0,z-z_0),
$$
大小为 $\frac{GMm}{\|\boldsymbol{r}\|^2}$，方向指向 $P_0$。它是除 $P_0$ 外的连续可微向量场。

**定义 13.3.2（有向曲线）** 规定了起点与终点（即规定了走向）的曲线称为**有向曲线**。与 $L$ 走向相反的有向曲线记作 $L^-$。参数方程给出的曲线，未特别说明时以参数增大的方向为正向；平面上的闭曲线，未特别说明时以逆时针方向为正向。

有向光滑曲线 $L$ 上每点有与走向一致的单位切向量 $\boldsymbol{\tau}=(\cos\alpha,\cos\beta,\cos\gamma)$。若 $L$ 由参数方程 $\boldsymbol{r}(t)$ 给出且参数增大的方向为正向，则 $\boldsymbol{\tau}=\boldsymbol{r}'(t)/\|\boldsymbol{r}'(t)\|$。

### 13.3.2. 定义与性质

常力 $\boldsymbol{F}$ 使质点沿直线产生位移 $\boldsymbol{s}$ 时，做功 $W=\boldsymbol{F}\cdot\boldsymbol{s}$。变力 $\boldsymbol{F}(x,y,z)$ 使质点沿有向曲线 $L$ 从 $A$ 移动到 $B$ 时，按走向把 $L$ 分成小段，第 $i$ 段近似为位移 $\Delta\boldsymbol{l}_i=(\Delta x_i,\Delta y_i,\Delta z_i)$，力近似为常力 $\boldsymbol{F}(P_i)$，所以

$$
W=\lim_{\lambda\to0}\sum_{i=1}^n\boldsymbol{F}(P_i)\cdot\Delta\boldsymbol{l}_i=\lim_{\lambda\to0}\sum_{i=1}^n\boldsymbol{F}(P_i)\cdot\boldsymbol{\tau}(P_i)\Delta l_i.
$$
后一个和式的极限正是数量函数 $\boldsymbol{F}\cdot\boldsymbol{\tau}$ 的第一型曲线积分。

**定义 13.3.3（第二型曲线积分）** 设 $\boldsymbol{v}=(X,Y,Z)$ 是区域 $\Omega\subset\mathbb{R}^3$ 上的连续向量场，$L$ 是 $\Omega$ 中一条逐段光滑的有向曲线，$\boldsymbol{\tau}$ 是 $L$ 的正向单位切向量。若第一型曲线积分 $\int_L\boldsymbol{v}\cdot\boldsymbol{\tau}\,\mathrm{d}l$ 存在，则称它为 $\boldsymbol{v}$ 沿有向曲线 $L$ 的**第二型曲线积分**，记作

$$
\int_L\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\int_LX\,\mathrm{d}x+Y\,\mathrm{d}y+Z\,\mathrm{d}z,
$$
其中 $\mathrm{d}\boldsymbol{l}=\boldsymbol{\tau}\,\mathrm{d}l=(\mathrm{d}x,\mathrm{d}y,\mathrm{d}z)$ 称为有向弧元。$\int_LX\,\mathrm{d}x$ 称为 $X$ 沿 $L$ 对坐标 $x$ 的曲线积分，其余类似。$L$ 是闭曲线时，$\oint_L\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}$ 称为 $\boldsymbol{v}$ 沿 $L$ 的**环量**。

物理上，$\boldsymbol{F}$ 是力时第二型曲线积分是功，$\boldsymbol{v}$ 是流速时环量度量流体沿 $L$ 旋转的强弱。由定义与第一型积分的性质立即得到：

**性质 13.3.1**

- 有向性：$\int_{L^-}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=-\int_L\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}$（反向时 $\boldsymbol{\tau}$ 变号）。
- 线性，以及对路径的可加性：$L$ 由 $L_1$、$L_2$ 首尾相接（方向一致）而成时 $\int_L=\int_{L_1}+\int_{L_2}$。
- 与第一型的关系：$\int_LX\,\mathrm{d}x+Y\,\mathrm{d}y+Z\,\mathrm{d}z=\int_L(X\cos\alpha+Y\cos\beta+Z\cos\gamma)\,\mathrm{d}l$。

### 13.3.3. 计算

**定理 13.3.1** 设有向光滑曲线 $L\colon\boldsymbol{r}(t)=(x(t),y(t),z(t))$，起点对应 $t=\alpha$，终点对应 $t=\beta$（$\alpha$ 可以大于 $\beta$），$\boldsymbol{v}=(X,Y,Z)$ 在 $L$ 上连续，则

$$
\int_LX\,\mathrm{d}x+Y\,\mathrm{d}y+Z\,\mathrm{d}z=\int_\alpha^\beta\big[X(\boldsymbol{r}(t))x'(t)+Y(\boldsymbol{r}(t))y'(t)+Z(\boldsymbol{r}(t))z'(t)\big]\,\mathrm{d}t.
$$

**证明** 设 $\alpha<\beta$。由定理 13.1.1 与 $\boldsymbol{\tau}=\boldsymbol{r}'/\|\boldsymbol{r}'\|$，

$$
\int_L\boldsymbol{v}\cdot\boldsymbol{\tau}\,\mathrm{d}l=\int_\alpha^\beta\boldsymbol{v}(\boldsymbol{r}(t))\cdot\frac{\boldsymbol{r}'(t)}{\|\boldsymbol{r}'(t)\|}\,\|\boldsymbol{r}'(t)\|\,\mathrm{d}t=\int_\alpha^\beta\boldsymbol{v}(\boldsymbol{r}(t))\cdot\boldsymbol{r}'(t)\,\mathrm{d}t.
$$
若 $\alpha>\beta$，则 $\boldsymbol{\tau}=-\boldsymbol{r}'/\|\boldsymbol{r}'\|$，而 $\int_\beta^\alpha$ 换成 $\int_\alpha^\beta$ 恰好再变一次号。$\square$

计算方法就是"代入"：把曲线方程代入被积表达式，$\mathrm{d}x=x'(t)\,\mathrm{d}t$ 等，定积分的下限对应起点、上限对应终点。平面曲线 $y=y(x)$ 从 $x=a$ 到 $x=b$ 时，$\int_LX\,\mathrm{d}x+Y\,\mathrm{d}y=\int_a^b[X(x,y(x))+Y(x,y(x))y'(x)]\,\mathrm{d}x$。

**例 13.3.1**（1）$L\colon y=x^2$ 从 $x=0$ 到 $x=2$，$\int_L(x^2-y^2)\,\mathrm{d}x=\int_0^2(x^2-x^4)\,\mathrm{d}x=\frac83-\frac{32}5=-\frac{56}{15}$。

（2）$L$ 为椭圆 $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ 的上半部分，逆时针方向（从 $(a,0)$ 到 $(-a,0)$）。取 $x=a\cos t$，$y=b\sin t$，$t$ 从 $0$ 到 $\pi$：

$$
\int_L(x^2+2xy)\,\mathrm{d}y=\int_0^\pi(a^2\cos^2t+2ab\cos t\sin t)\,b\cos t\,\mathrm{d}t=0+2ab^2\int_0^\pi\cos^2t\sin t\,\mathrm{d}t=\frac43ab^2.
$$

**例 13.3.2** 设 $\boldsymbol{v}=y\boldsymbol{i}-x\boldsymbol{j}+(x+y+z)\boldsymbol{k}$，$A(a,0,0)$，$B(a,0,c)$。$L_1$ 是螺旋线 $x=a\cos t$，$y=a\sin t$，$z=\frac{ct}{2\pi}$ 从 $A$（$t=0$）到 $B$（$t=2\pi$），$L_2$ 是从 $A$ 到 $B$ 的直线段。

$$
\int_{L_1}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\int_0^{2\pi}\Big[-a^2\sin^2t-a^2\cos^2t+\Big(a\cos t+a\sin t+\frac{ct}{2\pi}\Big)\frac{c}{2\pi}\Big]\mathrm{d}t=-2\pi a^2+\frac{c^2}2,
$$
而 $L_2\colon x=a$，$y=0$，$z$ 从 $0$ 到 $c$，$\int_{L_2}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\int_0^c(a+z)\,\mathrm{d}z=ac+\frac{c^2}2$。两条路径起点、终点相同，积分却不同：一般地，第二型曲线积分与路径有关。

**例 13.3.3** 设 $\boldsymbol{u}=(2xy,x^2)$，$\boldsymbol{v}=(xy,y-x)$，$L_1,L_2,L_3$ 分别是沿 $y=x$，$y=x^2$，$y=x^3$ 从 $(0,0)$ 到 $(1,1)$ 的曲线。

$$
\int_{L_1}\boldsymbol{u}\cdot\mathrm{d}\boldsymbol{l}=\int_0^1(2x^2+x^2)\,\mathrm{d}x=1,\quad\int_{L_2}\boldsymbol{u}\cdot\mathrm{d}\boldsymbol{l}=\int_0^1(2x^3+2x^3)\,\mathrm{d}x=1,\quad\int_{L_3}\boldsymbol{u}\cdot\mathrm{d}\boldsymbol{l}=\int_0^1(2x^4+3x^4)\,\mathrm{d}x=1;
$$

$$
\int_{L_1}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\int_0^1x^2\,\mathrm{d}x=\frac13,\quad\int_{L_2}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\int_0^1(3x^3-2x^2)\,\mathrm{d}x=\frac1{12},\quad\int_{L_3}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\int_0^1(3x^5+x^4-3x^3)\,\mathrm{d}x=-\frac1{20}.
$$
$\boldsymbol{u}$ 沿三条路径做功相同，$\boldsymbol{v}$ 则不同。原因是 $\boldsymbol{u}$ 是函数 $x^2y$ 的**梯度**：$\boldsymbol{u}\cdot\mathrm{d}\boldsymbol{l}=\mathrm{d}(x^2y)$，积分等于 $x^2y$ 在终点与起点的差。何时积分与路径无关，是 [2.2.14](/2.2.14) 保守场一节的主题。

![两个平面向量场沿三条路径从 (0,0) 到 (1,1) 做的功：左边的梯度场与路径无关，右边的场与路径有关](./plots/work-path-dependence.py)

**例 13.3.4** 计算 $\oint_L(x^2-2xy)\,\mathrm{d}x+(y^2-2xy)\,\mathrm{d}y$，$L$ 从 $(-1,1)$ 沿直线到 $(1,-1)$，再到 $(1,1)$，最后回到 $(-1,1)$。第一段 $y=-x$，$x$ 从 $-1$ 到 $1$：$\int_{-1}^1[(x^2+2x^2)-(x^2+2x^2)]\,\mathrm{d}x=0$；第二段 $x=1$，$y$ 从 $-1$ 到 $1$：$\int_{-1}^1(y^2-2y)\,\mathrm{d}y=\frac23$；第三段 $y=1$，$x$ 从 $1$ 到 $-1$：$\int_1^{-1}(x^2-2x)\,\mathrm{d}x=-\frac23$。所以积分为 $0$。

**例 13.3.5** 计算 $\oint_Lx\,\mathrm{d}y-y\,\mathrm{d}x+(x+y)\,\mathrm{d}z$，$L$ 为半球面 $z=\sqrt{1-x^2-y^2}$ 与柱面 $x^2+y^2=x$ 的交线，从 $z$ 轴正向往下看为逆时针方向。参数方程

$$
x=\frac12+\frac12\cos\theta,\quad y=\frac12\sin\theta,\quad z=\sqrt{1-x}=\sin\frac\theta2,\qquad0\le\theta\le2\pi,
$$
$\theta$ 增大时投影逆时针。$x\,\mathrm{d}y-y\,\mathrm{d}x=\frac14(1+\cos\theta)\,\mathrm{d}\theta$，$(x+y)\,\mathrm{d}z=\frac14(1+\cos\theta+\sin\theta)\cos\frac\theta2\,\mathrm{d}\theta=\frac14\big(2\cos^3\frac\theta2+2\sin\frac\theta2\cos^2\frac\theta2\big)\mathrm{d}\theta$，所以

$$
\oint_L=\frac14\int_0^{2\pi}\Big(1+\cos\theta+2\cos^3\frac\theta2+2\sin\frac\theta2\cos^2\frac\theta2\Big)\mathrm{d}\theta=\frac14\Big(2\pi+0+\frac83\Big)=\frac\pi2+\frac23.
$$

**例 13.3.6** 原点处有质量为 $m$ 的质点，单位质点在引力作用下从 $A(0,2)$ 移动到 $B(1,1)$：$L_1$ 是折线 $A\to C(1,2)\to B$，$L_2$ 是圆周 $x^2+y^2=2y$ 上从 $A$ 到 $B$ 的劣弧。引力 $\boldsymbol{F}=-Gm\dfrac{(x,y)}{(x^2+y^2)^{3/2}}$，做功 $W=-Gm\int_L\dfrac{x\,\mathrm{d}x+y\,\mathrm{d}y}{(x^2+y^2)^{3/2}}$。沿 $L_1$：

$$
W_1=-Gm\int_0^1\frac{x\,\mathrm{d}x}{(x^2+4)^{3/2}}-Gm\int_2^1\frac{y\,\mathrm{d}y}{(1+y^2)^{3/2}}=Gm\Big[\Big(\frac1{\sqrt5}-\frac12\Big)+\Big(\frac1{\sqrt2}-\frac1{\sqrt5}\Big)\Big]=\frac{Gm}2(\sqrt2-1).
$$
沿 $L_2$（$x=\cos t$，$y=1+\sin t$，$t$ 从 $\frac\pi2$ 到 $0$）：$W_2=Gm\int_0^{\pi/2}\frac{\cos t\,\mathrm{d}t}{(2+2\sin t)^{3/2}}=\frac{Gm}2(\sqrt2-1)=W_1$。事实上 $\boldsymbol{F}=\nabla\frac{Gm}{\sqrt{x^2+y^2}}$，功等于 $Gm\big(\frac1{|OB|}-\frac1{|OA|}\big)$，只与起点、终点有关：引力场是保守场。

## 13.4. Green 公式

### 13.4.1. 单连通区域与边界的定向

**定义 13.4.1（单连通区域与复连通区域）** 设 $D\subset\mathbb{R}^2$ 是平面**区域**。若 $D$ 内任意一条简单闭曲线所围的有界区域都含于 $D$，则称 $D$ 为**单连通区域**；否则称 $D$ 为**复连通区域**。

直观地说，单连通区域没有"洞"：圆盘、半平面是单连通的；圆环 $1<x^2+y^2<4$、去掉一点的平面 $\mathbb{R}^2\setminus\{0\}$ 是复连通的。

**定义 13.4.2（边界的正向）** 设 $D$ 是有界闭区域，其边界 $\partial D$ 由有限条逐段光滑的简单闭曲线组成。规定 $\partial D$ 的正向为：沿此方向前进时，$D$ 总在左侧。即外边界逆时针、内边界顺时针。

![复连通区域的正向边界：外边界逆时针，内边界顺时针，沿边界前进时区域总在左侧](./plots/green-region.py)

### 13.4.2. Green 公式

**定理 13.4.1（Green 公式）** 设 $D\subset\mathbb{R}^2$ 是有界闭区域，边界 $\partial D$ 由有限条逐段光滑的简单闭曲线组成，取正向；$X(x,y),Y(x,y)$ 在 $D$ 上有连续偏导数（即在包含 $D$ 的某个开集上有连续偏导数）。则

$$
\oint_{\partial D}X\,\mathrm{d}x+Y\,\mathrm{d}y=\iint_D\Big(\frac{\partial Y}{\partial x}-\frac{\partial X}{\partial y}\Big)\mathrm{d}x\,\mathrm{d}y.
$$

**证明** （1）设 $D=\{(x,y)\mid a\le x\le b,\ y_1(x)\le y\le y_2(x)\}$。化为**累次积分**，

$$
\iint_D\frac{\partial X}{\partial y}\,\mathrm{d}x\,\mathrm{d}y=\int_a^b\mathrm{d}x\int_{y_1(x)}^{y_2(x)}\frac{\partial X}{\partial y}\,\mathrm{d}y=\int_a^b\big[X(x,y_2(x))-X(x,y_1(x))\big]\mathrm{d}x.
$$
另一方面，$\partial D$ 由下边 $y=y_1(x)$（$x$ 从 $a$ 到 $b$）、上边 $y=y_2(x)$（$x$ 从 $b$ 到 $a$）和两条竖直线段组成，竖直线段上 $\mathrm{d}x=0$，所以 $\oint_{\partial D}X\,\mathrm{d}x=\int_a^bX(x,y_1(x))\,\mathrm{d}x-\int_a^bX(x,y_2(x))\,\mathrm{d}x$。于是 $\oint_{\partial D}X\,\mathrm{d}x=-\iint_D\frac{\partial X}{\partial y}\,\mathrm{d}x\,\mathrm{d}y$。

（2）若 $D$ 又可写成 $\{c\le y\le d,\ x_1(y)\le x\le x_2(y)\}$，同理 $\oint_{\partial D}Y\,\mathrm{d}y=\iint_D\frac{\partial Y}{\partial x}\,\mathrm{d}x\,\mathrm{d}y$，两式相加即得。

（3）一般区域用有限条辅助线分成若干块，每块都是（1）（2）中的情形。对每块用 Green 公式后相加：二重积分相加得到 $D$ 上的积分；每条辅助线在相邻两块的正向边界中各出现一次、方向相反，曲线积分互相抵消，剩下的恰好是 $\partial D$ 的正向。复连通区域同样处理：用辅助线把洞与外边界连起来，切成单连通的块。$\square$

Green 公式把区域上的二重积分与边界上的曲线积分联系起来，与 Newton–Leibniz 公式一样，是"内部的导数 = 边界的值"。使用时有三点要注意：边界取正向；$X,Y$ 在 $D$ 的每一点都要有连续偏导数（$D$ 内有奇点时不能直接用，见例 13.4.6）；曲线不封闭时可以补上一段，使之封闭。

**推论 13.4.1（面积公式）** 在定理 13.4.1 的条件下，$D$ 的面积为

$$
\sigma(D)=\oint_{\partial D}x\,\mathrm{d}y=-\oint_{\partial D}y\,\mathrm{d}x=\frac12\oint_{\partial D}x\,\mathrm{d}y-y\,\mathrm{d}x.
$$

例如星形线 $x=a\cos^3t$，$y=b\sin^3t$（$0\le t\le2\pi$）所围的面积为

$$
\frac12\int_0^{2\pi}(3ab\cos^4t\sin^2t+3ab\sin^4t\cos^2t)\,\mathrm{d}t=\frac{3ab}2\int_0^{2\pi}\sin^2t\cos^2t\,\mathrm{d}t=\frac{3\pi ab}8.
$$
椭圆 $x=a\cos t$，$y=b\sin t$ 的面积为 $\frac12\int_0^{2\pi}ab\,\mathrm{d}t=\pi ab$。

### 13.4.3. 应用

**例 13.4.1** $L$ 是上半圆 $y=\sqrt{a^2-x^2}$ 与直径组成的逆时针闭曲线，$D$ 是半圆盘。

$$
\oint_L(y^2+x)\,\mathrm{d}x+x^2\,\mathrm{d}y=\iint_D(2x-2y)\,\mathrm{d}x\,\mathrm{d}y=-2\iint_Dy\,\mathrm{d}x\,\mathrm{d}y=-\int_{-a}^a(a^2-x^2)\,\mathrm{d}x=-\frac43a^3,
$$
其中 $\iint_Dx\,\mathrm{d}x\,\mathrm{d}y=0$ 由对称性得到。

**例 13.4.2** 例 13.3.4 中的折线是三角形 $D$（顶点 $(-1,1),(1,-1),(1,1)$）的正向边界，由 Green 公式

$$
\oint_L(x^2-2xy)\,\mathrm{d}x+(y^2-2xy)\,\mathrm{d}y=\iint_D(-2y+2x)\,\mathrm{d}x\,\mathrm{d}y=\int_{-1}^1\mathrm{d}x\int_{-x}^1(2x-2y)\,\mathrm{d}y=\int_{-1}^1(3x^2+2x-1)\,\mathrm{d}x=0,
$$
与直接计算一致。$D$ 关于直线 $y=x$ 对称，由轮换对称性也可直接看出 $\iint_D(x-y)\,\mathrm{d}x\,\mathrm{d}y=0$。

**例 13.4.3（补线）** 用 Green 公式重算例 13.3.1（2）。补上 $L_1$：$x$ 轴上从 $(-a,0)$ 到 $(a,0)$ 的线段，$L$ 与 $L_1$ 合成上半椭圆盘 $D$ 的正向边界。$L_1$ 上 $\mathrm{d}y=0$，所以

$$
\int_L(x^2+2xy)\,\mathrm{d}y=\oint_{L+L_1}(x^2+2xy)\,\mathrm{d}y=\iint_D(2x+2y)\,\mathrm{d}x\,\mathrm{d}y=\iint_D2y\,\mathrm{d}x\,\mathrm{d}y.
$$
用**广义极坐标** $x=ar\cos\theta$，$y=br\sin\theta$，$\mathrm{d}x\,\mathrm{d}y=abr\,\mathrm{d}r\,\mathrm{d}\theta$，积分为 $\int_0^\pi\mathrm{d}\theta\int_0^12br\sin\theta\cdot abr\,\mathrm{d}r=\frac43ab^2$。

**例 13.4.4** 计算 $I=\int_L(\mathrm{e}^x\sin y-3y+x^2)\,\mathrm{d}x+(\mathrm{e}^x\cos y-x)\,\mathrm{d}y$，$L$ 是从 $A(a,0)$ 经上半圆 $x^2+y^2=a^2$ 到 $B(-a,0)$ 的弧。直接参数化很繁，补上从 $B$ 到 $A$ 的直径 $L_1$，$D$ 为上半圆盘：

$$
I=\oint_{L+L_1}-\int_{L_1}=\iint_D\big[(\mathrm{e}^x\cos y-1)-(\mathrm{e}^x\cos y-3)\big]\mathrm{d}\sigma-\int_{-a}^ax^2\,\mathrm{d}x=\pi a^2-\frac23a^3.
$$
被积表达式中的 $\mathrm{e}^x\sin y\,\mathrm{d}x+\mathrm{e}^x\cos y\,\mathrm{d}y=\mathrm{d}(\mathrm{e}^x\sin y)$ 在偏导数之差中消掉了，这是补线法的典型用途。

**例 13.4.5** 有向曲线 $L\colon y=\sqrt{\pi^2-x^2}$，起点 $(\pi,0)$，终点 $(-\pi,0)$，计算 $I=\int_L(\sin x-x^2y)\,\mathrm{d}x+(\sin y+xy^2)\,\mathrm{d}y$。补上从 $(-\pi,0)$ 到 $(\pi,0)$ 的线段 $L_1$（其上 $y=0$，积分为 $\int_{-\pi}^\pi\sin x\,\mathrm{d}x=0$），

$$
I=\iint_D(y^2+x^2)\,\mathrm{d}x\,\mathrm{d}y=\int_0^\pi\mathrm{d}\theta\int_0^\pi r^3\,\mathrm{d}r=\frac{\pi^5}4.
$$

**例 13.4.6（挖去奇点）** 设 $L$ 是不经过原点的逐段光滑简单闭曲线，逆时针方向，计算 $I=\oint_L\dfrac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2+y^2}$。记 $X=\frac{-y}{x^2+y^2}$，$Y=\frac{x}{x^2+y^2}$，在原点以外

$$
\frac{\partial Y}{\partial x}=\frac{y^2-x^2}{(x^2+y^2)^2}=\frac{\partial X}{\partial y}.
$$

- 若 $L$ 不包围原点，$X,Y$ 在 $L$ 所围的闭区域上连续可微，由 Green 公式 $I=0$。
- 若 $L$ 包围原点，Green 公式不能直接用。取 $\varepsilon>0$ 足够小，使圆周 $C_\varepsilon\colon x^2+y^2=\varepsilon^2$ 位于 $L$ 所围区域的内部，在 $L$ 与 $C_\varepsilon$ 之间的复连通区域 $D$ 上用 Green 公式（$C_\varepsilon$ 取顺时针）：$\oint_L+\oint_{C_\varepsilon^-}=\iint_D0\,\mathrm{d}\sigma=0$。所以

$$
I=\oint_{C_\varepsilon}\frac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2+y^2}=\frac1{\varepsilon^2}\oint_{C_\varepsilon}x\,\mathrm{d}y-y\,\mathrm{d}x=\frac1{\varepsilon^2}\cdot2\pi\varepsilon^2=2\pi.
$$

例如 $L$ 为椭圆 $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ 顺时针时，$I=-2\pi$；直接用参数 $x=a\cos t$，$y=b\sin t$ 计算，要算 $-\int_0^{2\pi}\frac{ab\,\mathrm{d}t}{a^2\cos^2t+b^2\sin^2t}$，通过 $\tan t$ 换元同样得到 $-2\pi$，但繁得多。积分值只取决于 $L$ 是否绕原点，与 $L$ 的形状无关；它的几何意义是 $L$ 绕原点转过的总角度（$\frac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2+y^2}$ 局部上是极角的微分 $\mathrm{d}\theta$）。

**例 13.4.7** 当光滑简单闭曲线 $L$（逆时针）为何曲线时，$I=\oint_L(y^3-y)\,\mathrm{d}x-2x^3\,\mathrm{d}y$ 最大？由 Green 公式，$I=\iint_D(1-6x^2-3y^2)\,\mathrm{d}x\,\mathrm{d}y$，$D$ 为 $L$ 所围的区域。被积函数在椭圆 $6x^2+3y^2<1$ 内为正、外为负，所以 $D$ 恰取这个椭圆盘时 $I$ 最大，即 $L$ 为椭圆 $6x^2+3y^2=1$。

### 13.4.4. Green 公式的通量形式

设 $\boldsymbol{v}=(X,Y)$ 是平面流体的流速，$\boldsymbol{n}$ 是 $\partial D$ 的单位外法向量。单位时间内穿过边界小段 $\mathrm{d}l$ 流出 $D$ 的流体面积为 $\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}l$，所以 $\oint_{\partial D}\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}l$ 是单位时间内从 $D$ 流出的总量。

**定理 13.4.2（Green 公式的通量形式）** 在定理 13.4.1 的条件下，设 $\boldsymbol{v}=(X,Y)$，$\boldsymbol{n}$ 是 $\partial D$ 的单位外法向量，则

$$
\oint_{\partial D}\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}l=\iint_D\Big(\frac{\partial X}{\partial x}+\frac{\partial Y}{\partial y}\Big)\mathrm{d}x\,\mathrm{d}y.
$$

**证明** 正向单位切向量 $\boldsymbol{\tau}=(\cos\alpha,\sin\alpha)$ 顺时针旋转 $\frac\pi2$ 得到外法向量（区域在左侧），$\boldsymbol{n}=(\sin\alpha,-\cos\alpha)$，所以 $\boldsymbol{n}\,\mathrm{d}l=(\mathrm{d}y,-\mathrm{d}x)$。于是 $\oint_{\partial D}\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}l=\oint_{\partial D}-Y\,\mathrm{d}x+X\,\mathrm{d}y$，对它用 Green 公式即得。$\square$

两种形式分别说明：沿边界的环量等于区域上 $\frac{\partial Y}{\partial x}-\frac{\partial X}{\partial y}$ 的积分，向外的流出量等于区域上 $\frac{\partial X}{\partial x}+\frac{\partial Y}{\partial y}$ 的积分。这两个被积函数就是 [2.2.14](/2.2.14) 中平面向量场的旋度与散度。

**例 13.4.8** 设 $f$ 在有界闭区域 $D$ 上有二阶连续偏导数，$\frac{\partial f}{\partial\boldsymbol{n}}$ 是 $f$ 沿 $\partial D$ 外法向的**方向导数**，则

$$
\oint_{\partial D}\frac{\partial f}{\partial\boldsymbol{n}}\,\mathrm{d}l=\iint_D\Big(\frac{\partial^2f}{\partial x^2}+\frac{\partial^2f}{\partial y^2}\Big)\mathrm{d}x\,\mathrm{d}y.
$$
这是因为 $\frac{\partial f}{\partial\boldsymbol{n}}=\nabla f\cdot\boldsymbol{n}$，对 $\boldsymbol{v}=\nabla f=(f_x,f_y)$ 用定理 13.4.2。特别地，满足 $f_{xx}+f_{yy}=0$ 的函数沿任意闭曲线的法向导数积分为零。

## 13.5. 有向曲面与第二型曲面积分

### 13.5.1. 有向曲面

若曲面 $S$ 在每点都有非零法向量 $\boldsymbol{n}$，且 $\boldsymbol{n}$ 随点连续变化，则称 $S$ 是光滑曲面。光滑曲面在每点有两个相反的单位法向量；要讨论流体从曲面的哪一侧流向另一侧，必须能在整个曲面上连续地选定其中一个。

**定义 13.5.1（有向曲面）** 设 $S$ 是光滑曲面。若在 $S$ 上任取一点 $M_0$ 与该点的一个单位法向量，当点从 $M_0$ 出发沿 $S$ 上任意一条不越过 $S$ 边界的闭曲线连续移动一周回到 $M_0$ 时，法向量随之连续变化后仍回到原来的法向量，则称 $S$ 为双侧曲面。选定了一侧（即选定了连续的单位法向量场 $\boldsymbol{n}$）的双侧曲面称为**有向曲面**，$\boldsymbol{n}$ 所指的一侧称为正侧。与 $S$ 方向相反的有向曲面记作 $S^-$。

日常的曲面（球面、柱面、$z=f(x,y)$ 的图像）都是双侧的。Möbius 带（把长纸条扭转半圈后两端粘合）是单侧曲面：法向量沿中线走一圈后变成相反的方向，无法定向，本课程不讨论这类曲面。常用的约定：$z=z(x,y)$ 有上侧（$\cos\gamma>0$）与下侧；闭曲面以外侧为正向；夹在两个闭曲面之间的立体，其边界曲面的正向是外层的外侧与内层的内侧（都指向立体外部）。

有向曲面 $S$ 的边界曲线按右手法则定向：人站在曲面正侧（头指向 $\boldsymbol{n}$），沿边界前进时曲面总在左侧。这一约定在 [2.2.14](/2.2.14) 的 Stokes 公式中使用；$S$ 是 $xOy$ 平面上取上侧的区域时，它就是定义 13.4.2 的正向。

### 13.5.2. 定义与性质

设不可压缩流体的流速 $\boldsymbol{v}(x,y,z)$ 不随时间变化，求单位时间内流过有向曲面 $S$（从负侧流向正侧）的流体体积。把 $S$ 分成小片 $\Delta S_i$，每片近似为平面片，单位法向量为 $\boldsymbol{n}(P_i)$，流速近似为常量 $\boldsymbol{v}(P_i)$，则单位时间内流过它的流体是一个斜柱体，体积为 $\boldsymbol{v}(P_i)\cdot\boldsymbol{n}(P_i)\Delta S_i$。总流量为 $\lim\sum\boldsymbol{v}\cdot\boldsymbol{n}\,\Delta S_i$。

**定义 13.5.2（第二型曲面积分与通量）** 设 $\boldsymbol{v}=(X,Y,Z)$ 是区域 $\Omega\subset\mathbb{R}^3$ 上的连续向量场，$S$ 是 $\Omega$ 中的有向光滑（或分片光滑）曲面，$\boldsymbol{n}$ 是其正侧的单位法向量。称第一型曲面积分 $\iint_S\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}S$ 为 $\boldsymbol{v}$ 在有向曲面 $S$ 上的**第二型曲面积分**，也称为 $\boldsymbol{v}$ 穿过 $S$ 的**通量**，记作

$$
\iint_S\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=\iint_SX\,\mathrm{d}y\wedge\mathrm{d}z+Y\,\mathrm{d}z\wedge\mathrm{d}x+Z\,\mathrm{d}x\wedge\mathrm{d}y,
$$
其中 $\mathrm{d}\boldsymbol{S}=\boldsymbol{n}\,\mathrm{d}S$ 称为有向面积元。记 $\boldsymbol{n}=(\cos\alpha,\cos\beta,\cos\gamma)$，则 $\mathrm{d}y\wedge\mathrm{d}z=\cos\alpha\,\mathrm{d}S$，$\mathrm{d}z\wedge\mathrm{d}x=\cos\beta\,\mathrm{d}S$，$\mathrm{d}x\wedge\mathrm{d}y=\cos\gamma\,\mathrm{d}S$。闭曲面上的积分记作 $\oiint_S$。

$\mathrm{d}x\wedge\mathrm{d}y$ 是有向面积元在 $xOy$ 面上的有向投影：$\cos\gamma>0$ 时它等于投影面积元 $\mathrm{d}x\,\mathrm{d}y$，$\cos\gamma<0$ 时等于 $-\mathrm{d}x\,\mathrm{d}y$，$\cos\gamma=0$（曲面垂直于 $xOy$ 面）时为零。这一点与重积分中恒正的 $\mathrm{d}x\,\mathrm{d}y$ 不同，也是计算中最容易出错之处。

**性质 13.5.1**

- 有向性：$\iint_{S^-}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=-\iint_S\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}$。
- 线性，以及对曲面的可加性（分片时各片的定向与 $S$ 一致）。
- 若 $S$ 垂直于 $xOy$ 面（例如母线平行于 $z$ 轴的柱面），则 $\iint_SZ\,\mathrm{d}x\wedge\mathrm{d}y=0$；其余坐标面类似。

### 13.5.3. 计算

**定理 13.5.1** 设 $\boldsymbol{v}=(X,Y,Z)$ 在有向光滑曲面 $S$ 上连续。

（1）若 $S\colon z=z(x,y)$，$(x,y)\in D_{xy}$，取上侧，则

$$
\iint_SZ\,\mathrm{d}x\wedge\mathrm{d}y=\iint_{D_{xy}}Z(x,y,z(x,y))\,\mathrm{d}x\,\mathrm{d}y,\qquad\iint_S\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=\iint_{D_{xy}}\big(-Xz_x-Yz_y+Z\big)\,\mathrm{d}x\,\mathrm{d}y;
$$
取下侧时右端都改变符号。$x=x(y,z)$（前侧为正）、$y=y(z,x)$（右侧为正）的情形类似。

（2）若 $S\colon\boldsymbol{r}(u,v)$，$(u,v)\in D_{uv}$，则

$$
\iint_S\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=\pm\iint_{D_{uv}}\boldsymbol{v}(\boldsymbol{r}(u,v))\cdot(\boldsymbol{r}_u\times\boldsymbol{r}_v)\,\mathrm{d}u\,\mathrm{d}v=\pm\iint_{D_{uv}}(XA+YB+ZC)\,\mathrm{d}u\,\mathrm{d}v,
$$
$\boldsymbol{r}_u\times\boldsymbol{r}_v=(A,B,C)$ 指向正侧时取正号，否则取负号。

**证明** （2）由定义与定理 13.2.2：正侧单位法向量为 $\boldsymbol{n}=\pm\frac{\boldsymbol{r}_u\times\boldsymbol{r}_v}{\|\boldsymbol{r}_u\times\boldsymbol{r}_v\|}$，$\mathrm{d}S=\|\boldsymbol{r}_u\times\boldsymbol{r}_v\|\,\mathrm{d}u\,\mathrm{d}v$，相乘即得。（1）是（2）取 $u=x$，$v=y$ 的特例：$\boldsymbol{r}_x\times\boldsymbol{r}_y=(-z_x,-z_y,1)$ 指向上侧。$\square$

公式（1）说明，在显式曲面上通量的三个分量可以统一投影到 $xOy$ 面上计算，不必分别向三个坐标面投影。

**算法 13.5.1（第二型曲面积分的计算）** 计算 $\iint_S\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}$：

1. 先看能否简化：$S$ 封闭或补上简单曲面后封闭时，考虑用 [2.2.14](/2.2.14) 的 Gauss 公式；利用对称性与性质 13.5.1 中"垂直于坐标面的部分贡献为零"去掉一些项。
2. 分项投影：对 $\iint Z\,\mathrm{d}x\wedge\mathrm{d}y$，把 $S$ 分成若干片，每片可写成 $z=z(x,y)$ 且一一投影到 $xOy$ 面；按该片正侧法向量与 $z$ 轴的夹角是锐角还是钝角，取正号或负号化为二重积分。另两项同理。
3. 或统一投影：$S$ 是 $z=z(x,y)$ 时用定理 13.5.1（1），只投影一次。
4. 或参数化：用定理 13.5.1（2），按 $\boldsymbol{r}_u\times\boldsymbol{r}_v$ 的方向定号。
5. 或化为第一型：求出正侧单位法向量 $\boldsymbol{n}$，计算 $\iint_S\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}S$；$\boldsymbol{v}\cdot\boldsymbol{n}$ 在 $S$ 上很简单时（如球面上 $\boldsymbol{n}=\frac{(x,y,z)}R$）最省事。

**例 13.5.1** 设 $f,g,h$ 连续，$S$ 是长方体 $[0,a]\times[0,b]\times[0,c]$ 表面的外侧，计算 $\oiint_Sf(x)\,\mathrm{d}y\wedge\mathrm{d}z+g(y)\,\mathrm{d}z\wedge\mathrm{d}x+h(z)\,\mathrm{d}x\wedge\mathrm{d}y$。$\iint h(z)\,\mathrm{d}x\wedge\mathrm{d}y$ 只在上下两面不为零：上面 $z=c$ 取上侧，为 $abh(c)$；下面 $z=0$ 取下侧，为 $-abh(0)$。其余两项同理，所以

$$
\oiint_S=bc\big[f(a)-f(0)\big]+ca\big[g(b)-g(0)\big]+ab\big[h(c)-h(0)\big].
$$

**例 13.5.2** 计算 $\oiint_Sy^2z\,\mathrm{d}x\wedge\mathrm{d}y$，$S$ 为球面 $x^2+y^2+z^2=R^2$ 的外侧。

解法一（分片投影）：上半球面 $z=\sqrt{R^2-x^2-y^2}$ 取上侧，下半球面 $z=-\sqrt{R^2-x^2-y^2}$ 取下侧。下半球面上 $z<0$，取下侧又带一个负号，两片的值相等（不是抵消）：

$$
\oiint_S=2\iint_{x^2+y^2\le R^2}y^2\sqrt{R^2-x^2-y^2}\,\mathrm{d}x\,\mathrm{d}y=2\int_0^{2\pi}\sin^2\theta\,\mathrm{d}\theta\int_0^Rr^3\sqrt{R^2-r^2}\,\mathrm{d}r=2\pi\cdot\frac{2R^5}{15}=\frac{4\pi R^5}{15}.
$$

解法二（化为第一型）：外法向量 $\boldsymbol{n}=\frac{(x,y,z)}R$，$\boldsymbol{v}\cdot\boldsymbol{n}=\frac{y^2z^2}R$。用球面参数，$\mathrm{d}S=R^2\sin\varphi\,\mathrm{d}\varphi\,\mathrm{d}\theta$，

$$
\oiint_S\frac{y^2z^2}R\,\mathrm{d}S=R^5\int_0^{2\pi}\sin^2\theta\,\mathrm{d}\theta\int_0^\pi\sin^3\varphi\cos^2\varphi\,\mathrm{d}\varphi=R^5\cdot\pi\cdot\frac4{15}=\frac{4\pi R^5}{15}.
$$

**例 13.5.3** 计算 $I=\iint_Sx(y-z)\,\mathrm{d}y\wedge\mathrm{d}z+(x-y)\,\mathrm{d}x\wedge\mathrm{d}y$，$S$ 为柱面 $x^2+y^2=1$（$0\le z\le2$）的外侧。$S$ 垂直于 $xOy$ 面，$\iint_S(x-y)\,\mathrm{d}x\wedge\mathrm{d}y=0$。

解法一（分片投影）：前半柱面 $x=\sqrt{1-y^2}$ 取前侧（法向量与 $x$ 轴夹锐角），后半柱面 $x=-\sqrt{1-y^2}$ 取后侧，投影区域都是 $D\colon-1\le y\le1$，$0\le z\le2$：

$$
I=\iint_D\sqrt{1-y^2}(y-z)\,\mathrm{d}y\,\mathrm{d}z-\iint_D\big(-\sqrt{1-y^2}\big)(y-z)\,\mathrm{d}y\,\mathrm{d}z=2\int_{-1}^1\sqrt{1-y^2}\,\mathrm{d}y\int_0^2(y-z)\,\mathrm{d}z=2\int_{-1}^1\sqrt{1-y^2}(2y-2)\,\mathrm{d}y=-2\pi.
$$

解法二（化为第一型）：$\boldsymbol{n}=(x,y,0)$，$\boldsymbol{v}\cdot\boldsymbol{n}=x^2(y-z)$，侧面用 $x=\cos\theta$，$y=\sin\theta$，$\mathrm{d}S=\mathrm{d}\theta\,\mathrm{d}z$：

$$
I=\int_0^2\mathrm{d}z\int_0^{2\pi}\cos^2\theta(\sin\theta-z)\,\mathrm{d}\theta=\int_0^2(-\pi z)\,\mathrm{d}z=-2\pi.
$$

**例 13.5.4** 计算 $I=\iint_S(y-z)\,\mathrm{d}y\wedge\mathrm{d}z+(z-x)\,\mathrm{d}z\wedge\mathrm{d}x+(x-y)\,\mathrm{d}x\wedge\mathrm{d}y$，$S$ 为锥面 $z=\sqrt{x^2+y^2}$（$0\le z\le h$）的外侧（下侧）。由定理 13.5.1（1），$z_x=\frac xz$，$z_y=\frac yz$，取下侧：

$$
I=-\iint_{x^2+y^2\le h^2}\Big[-(y-z)\frac xz-(z-x)\frac yz+(x-y)\Big]\mathrm{d}x\,\mathrm{d}y=-\iint_{x^2+y^2\le h^2}2(x-y)\,\mathrm{d}x\,\mathrm{d}y=0,
$$
其中方括号内 $\frac{-xy+xz-yz+xy}{z}+(x-y)=2(x-y)$，最后由对称性积分为零。也可分项看出：$\iint(y-z)\,\mathrm{d}y\wedge\mathrm{d}z$ 的前后两片投影区域相同、被积函数相同、符号相反，抵消为零，其余两项类似。

**例 13.5.5** 单位点电荷置于原点，在点 $(x,y,z)$ 处产生的电场强度为 $\boldsymbol{E}=k\dfrac{(x,y,z)}{(x^2+y^2+z^2)^{3/2}}$。它穿过球面 $x^2+y^2+z^2=R^2$（外侧）的电通量为

$$
\oiint_S\boldsymbol{E}\cdot\boldsymbol{n}\,\mathrm{d}S=\oiint_Sk\frac{(x,y,z)}{R^3}\cdot\frac{(x,y,z)}R\,\mathrm{d}S=\frac k{R^2}\oiint_S\mathrm{d}S=4\pi k,
$$
与半径无关。这是电磁学中 Gauss 定律的最简单情形，[2.2.14](/2.2.14) 将说明它对任意包围电荷的闭曲面成立。

**例 13.5.6** 计算 $\oiint_S\dfrac{\mathrm{d}y\wedge\mathrm{d}z}x+\dfrac{\mathrm{d}z\wedge\mathrm{d}x}y+\dfrac{\mathrm{d}x\wedge\mathrm{d}y}z$，$S$ 为椭球面 $\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1$ 的外侧。用参数 $x=a\sin\varphi\cos\theta$，$y=b\sin\varphi\sin\theta$，$z=c\cos\varphi$，

$$
\boldsymbol{r}_\varphi\times\boldsymbol{r}_\theta=(bc\sin^2\varphi\cos\theta,\ ca\sin^2\varphi\sin\theta,\ ab\sin\varphi\cos\varphi)=abc\sin\varphi\Big(\frac x{a^2},\frac y{b^2},\frac z{c^2}\Big),
$$
指向外侧。$\boldsymbol{v}=\big(\frac1x,\frac1y,\frac1z\big)$，$\boldsymbol{v}\cdot(\boldsymbol{r}_\varphi\times\boldsymbol{r}_\theta)=abc\sin\varphi\big(\frac1{a^2}+\frac1{b^2}+\frac1{c^2}\big)$，所以积分为

$$
abc\Big(\frac1{a^2}+\frac1{b^2}+\frac1{c^2}\Big)\int_0^{2\pi}\mathrm{d}\theta\int_0^\pi\sin\varphi\,\mathrm{d}\varphi=4\pi abc\Big(\frac1{a^2}+\frac1{b^2}+\frac1{c^2}\Big).
$$
被积函数在坐标面上无定义，但曲面积分作为反常积分收敛；参数化后奇点自动消失。

**例 13.5.7** 设 $S\colon z=xy$，$|x|\le1$，$|y|\le1$，取上侧，计算 $I=\iint_S\mathrm{e}^y\,\mathrm{d}y\wedge\mathrm{d}z+\mathrm{e}^x\,\mathrm{d}z\wedge\mathrm{d}x+\mathrm{d}x\wedge\mathrm{d}y$。由定理 13.5.1（1），$z_x=y$，$z_y=x$，

$$
I=\iint_{[-1,1]^2}\big(-y\mathrm{e}^y-x\mathrm{e}^x+1\big)\,\mathrm{d}x\,\mathrm{d}y=-2\int_{-1}^1y\mathrm{e}^y\,\mathrm{d}y-2\int_{-1}^1x\mathrm{e}^x\,\mathrm{d}x+4=4-\frac8{\mathrm{e}},
$$
其中 $\int_{-1}^1x\mathrm{e}^x\,\mathrm{d}x=(x-1)\mathrm{e}^x\big|_{-1}^1=\frac2{\mathrm{e}}$。

![曲面 z = xy 及其上侧的单位法向量场：法向量随点连续变化，选定一侧后曲面成为有向曲面](./plots/oriented-surface.py)

## 小结

四类线面积分的对照：

| | 第一型曲线积分 | 第二型曲线积分 | 第一型曲面积分 | 第二型曲面积分 |
|---|---|---|---|---|
| 被积对象 | 数量函数 $f$ | 向量场 $\boldsymbol{v}$ | 数量函数 $f$ | 向量场 $\boldsymbol{v}$ |
| 记号 | $\int_Lf\,\mathrm{d}l$ | $\int_L\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\int_LX\,\mathrm{d}x+Y\,\mathrm{d}y+Z\,\mathrm{d}z$ | $\iint_Sf\,\mathrm{d}S$ | $\iint_S\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=\iint_SX\,\mathrm{d}y\wedge\mathrm{d}z+\cdots$ |
| 方向 | 无 | 反向变号 | 无 | 换侧变号 |
| 物理意义 | 质量、弧长 | 功、环量 | 质量、面积 | 通量（流量） |
| 微元 | $\mathrm{d}l=\Vert\boldsymbol{r}'(t)\Vert\,\mathrm{d}t$ | $\mathrm{d}\boldsymbol{l}=\boldsymbol{r}'(t)\,\mathrm{d}t$ | $\mathrm{d}S=\Vert\boldsymbol{r}_u\times\boldsymbol{r}_v\Vert\,\mathrm{d}u\,\mathrm{d}v$ | $\mathrm{d}\boldsymbol{S}=\pm\boldsymbol{r}_u\times\boldsymbol{r}_v\,\mathrm{d}u\,\mathrm{d}v$ |
| 化为 | 定积分，下限 $<$ 上限 | 定积分，下限对应起点 | 二重积分 | 二重积分，按侧定号 |
| 两型的关系 | | $\int_L\boldsymbol{v}\cdot\boldsymbol{\tau}\,\mathrm{d}l$ | | $\iint_S\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}S$ |

Green 公式的两种形式（$\boldsymbol{v}=(X,Y)$，$\partial D$ 取正向，$\boldsymbol{n}$ 为外法向量）：

| 形式 | 公式 | 物理意义 |
|---|---|---|
| 环量形式 | $\oint_{\partial D}X\,\mathrm{d}x+Y\,\mathrm{d}y=\iint_D(Y_x-X_y)\,\mathrm{d}\sigma$ | 边界环量 = 内部旋转强度之和 |
| 通量形式 | $\oint_{\partial D}\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}l=\iint_D(X_x+Y_y)\,\mathrm{d}\sigma$ | 向外流出量 = 内部源强度之和 |
| 面积 | $\sigma(D)=\frac12\oint_{\partial D}x\,\mathrm{d}y-y\,\mathrm{d}x$ | |

平面第二型曲线积分的常用方法：直接参数化；封闭曲线用 Green 公式，不封闭时补线；有奇点时挖去小圆；积分与路径无关时换一条简单路径或用原函数（[2.2.14](/2.2.14)）。
