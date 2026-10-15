---
title: 重积分与含参变量积分
---

定积分是区间上"分割、近似、求和、取极限"得到的量。把区间换成平面区域或空间区域，同样的四步就得到二重积分与三重积分，统称重积分：曲顶柱体的体积、非均匀薄板与物体的质量、质心与转动惯量都由它表示。重积分的定义与性质几乎照搬定积分，难点在计算。计算的基本思路有两条：一是化为累次积分，即逐次做定积分，关键是由区域的形状定出积分限；二是变量替换，把区域变成简单的形状，代价是面积元或体积元要乘以 **Jacobi 行列式**的绝对值——它正是线性代数中**行列式**作为[变积系数](/2.1.5#sec-5.3.1)的含义在局部的体现。

本章依赖一元的**定积分**、**反常积分**（[2.2.7](/2.2.7)）与 [2.2.10](/2.2.10) 的 Jacobi 矩阵。最后一节讨论含参变量积分，它在形式上是一元的，但证明要用到重积分与多元函数的连续性。本章的结论是概率论中联合分布、边缘分布与随机向量函数的分布（3.1）的计算工具，其中 Gauss 积分 $\int_{-\infty}^{+\infty}\mathrm{e}^{-x^2}\,\mathrm{d}x=\sqrt\pi$ 是正态分布的基础。曲线与曲面上的积分见 [2.2.13](/2.2.13)。

## 12.1. 重积分的概念与性质

### 12.1.1. 二重积分与三重积分的定义

两个引例。设 $z=f(x,y)\ge0$ 在有界闭区域 $D$ 上连续，以 $D$ 为底、曲面 $z=f(x,y)$ 为顶的曲顶柱体的体积 $V$：把 $D$ 分成小区域 $D_1,\dots,D_k$，面积为 $\Delta\sigma_i$，在每块上任取一点 $P_i$，小曲顶柱体近似为平顶柱体，$V\approx\sum f(P_i)\Delta\sigma_i$。面密度为 $\mu(x,y)$ 的薄板的质量同样近似为 $\sum\mu(P_i)\Delta\sigma_i$。分割越来越细时，近似值的极限就是所求的量。

**定义 12.1.1（二重积分）** 设 $D\subset\mathbb{R}^2$ 是有界闭区域，$f$ 是定义在 $D$ 上的函数。把 $D$ 任意分成 $k$ 个小区域 $D_1,\dots,D_k$（记为分割 $T$），$\Delta\sigma_i$ 为 $D_i$ 的面积，$\lambda(T)=\max_i\operatorname{diam}D_i$ 为各小区域直径的最大值，任取 $P_i\in D_i$，作和式 $\sum_{i=1}^kf(P_i)\Delta\sigma_i$。若存在常数 $I$，对任意 $\varepsilon>0$，存在 $\delta>0$，使对任意满足 $\lambda(T)<\delta$ 的分割和任意取点 $P_i$，都有

$$
\Big|\sum_{i=1}^kf(P_i)\Delta\sigma_i-I\Big|<\varepsilon,
$$

则称 $f$ 在 $D$ 上（Riemann）可积，记作 $f\in\mathcal{R}(D)$，称 $I$ 为 $f$ 在 $D$ 上的**二重积分**，记作

$$
\iint_Df(x,y)\,\mathrm{d}\sigma=\lim_{\lambda(T)\to0}\sum_{i=1}^kf(P_i)\Delta\sigma_i.
$$

$f$ 称为被积函数，$\mathrm{d}\sigma$ 称为面积元。上面的和式是 **Riemann 和**的二维版本，定义中有"分割任意"与"取点任意"两个任意性。

**定义 12.1.2（三重积分）** 设 $\Omega\subset\mathbb{R}^3$ 是有界闭区域，把 $\Omega$ 任意分成小区域 $\Omega_1,\dots,\Omega_k$，体积为 $\Delta V_i$，任取 $P_i\in\Omega_i$。若 $\lambda(T)\to0$ 时 $\sum f(P_i)\Delta V_i$ 有（与分割、取点无关的）极限，则称 $f$ 在 $\Omega$ 上可积，极限称为 $f$ 在 $\Omega$ 上的**三重积分**，记作 $\iiint_\Omega f(x,y,z)\,\mathrm{d}V$。

二重积分与三重积分统称**重积分**。$\iint_D1\,\mathrm{d}\sigma$ 是 $D$ 的面积，$\iiint_\Omega1\,\mathrm{d}V$ 是 $\Omega$ 的体积；$f\ge0$ 时 $\iint_Df\,\mathrm{d}\sigma$ 是曲顶柱体的体积，$\iiint_\Omega\rho\,\mathrm{d}V$ 是密度为 $\rho$ 的物体的质量。

### 12.1.2. 可积性与性质

与定积分一样，可积函数必有界；但有界不一定可积，例如 $D=[0,1]^2$ 上 $x,y$ 都是有理数时取 $1$、否则取 $0$ 的函数（**Dirichlet 函数**的二维版本），每个小区域上的振幅都是 $1$，Riemann 和的极限不存在。常用的充分条件是：

**定理 12.1.1** 若 $f$ 在有界闭区域 $D$ 上连续，则 $f\in\mathcal{R}(D)$。更一般地，若 $f$ 在 $D$ 上有界，且间断点位于有限条光滑曲线上，则 $f\in\mathcal{R}(D)$。

本课程中的区域边界都由有限条光滑曲线（曲面）组成，被积函数分片连续，所以重积分总存在。以下以二重积分叙述性质，三重积分完全相同。设 $f,g\in\mathcal{R}(D)$，$\sigma$ 为 $D$ 的面积。

**性质 12.1.1（线性）** $\iint_D(\alpha f+\beta g)\,\mathrm{d}\sigma=\alpha\iint_Df\,\mathrm{d}\sigma+\beta\iint_Dg\,\mathrm{d}\sigma$。

**性质 12.1.2（区域可加性）** 若 $D=D_1\cup\cdots\cup D_k$，且各 $D_i$ 两两之交的面积为零，则 $\iint_Df\,\mathrm{d}\sigma=\sum_{i=1}^k\iint_{D_i}f\,\mathrm{d}\sigma$。

**性质 12.1.3（保序性）** 若在 $D$ 上 $f\le g$，则 $\iint_Df\,\mathrm{d}\sigma\le\iint_Dg\,\mathrm{d}\sigma$。特别地，$|f|\in\mathcal{R}(D)$ 且 $\Big|\iint_Df\,\mathrm{d}\sigma\Big|\le\iint_D|f|\,\mathrm{d}\sigma$。

**性质 12.1.4（估值定理）** 若在 $D$ 上 $m\le f\le M$，则 $m\sigma\le\iint_Df\,\mathrm{d}\sigma\le M\sigma$。

**性质 12.1.5（积分中值定理）** 若 $f$ 在 $D$ 上连续，则存在 $(\xi,\eta)\in D$，使 $\iint_Df\,\mathrm{d}\sigma=f(\xi,\eta)\sigma$。

性质 12.1.5 由估值定理与有界闭区域上的**介值定理**得到，它说明连续函数在 $D$ 上的平均值 $\frac1\sigma\iint_Df\,\mathrm{d}\sigma$ 一定在某点取到。

**性质 12.1.6（对称性）** 设 $D$ 关于 $y$ 轴对称，$D_1$ 为 $D$ 在 $y$ 轴右侧的部分。若 $f(-x,y)=-f(x,y)$（$f$ 关于 $x$ 为奇函数），则 $\iint_Df\,\mathrm{d}\sigma=0$；若 $f(-x,y)=f(x,y)$，则 $\iint_Df\,\mathrm{d}\sigma=2\iint_{D_1}f\,\mathrm{d}\sigma$。关于 $x$ 轴、关于原点对称的情形类似；三重积分还有关于坐标平面的对称。

**性质 12.1.7（轮换对称性）** 若 $D$ 关于直线 $y=x$ 对称（即 $(x,y)\in D\Leftrightarrow(y,x)\in D$），则 $\iint_Df(x,y)\,\mathrm{d}\sigma=\iint_Df(y,x)\,\mathrm{d}\sigma$。

使用对称性时，区域的对称与被积函数的奇偶性必须是对同一个变量而言的。轮换对称性是多元积分特有的：定积分只有一个变量，无从轮换。

**例 12.1.1** 设 $D=\{x^2+y^2\le R^2\}$。

1. 若 $m,n$ 为非负整数且 $m,n$ 中至少一个是奇数，则 $\iint_Dx^my^n\,\mathrm{d}\sigma=0$（若 $m$ 为奇数，被积函数关于 $x$ 为奇函数，$D$ 关于 $y$ 轴对称）。
2. 由轮换对称性，$\iint_Dx^2\,\mathrm{d}\sigma=\iint_Dy^2\,\mathrm{d}\sigma=\frac12\iint_D(x^2+y^2)\,\mathrm{d}\sigma$，后者用极坐标（[12.2.4](#sec-12.2.4)）容易算出，为 $\frac{\pi R^4}{4}$。

**例 12.1.2** 估计 $I=\iint_D\dfrac{\mathrm{d}\sigma}{100+\cos^2x+\cos^2y}$，$D=\{|x|+|y|\le10\}$。$D$ 是对角线长 $20$ 的正方形，面积为 $200$；被积函数介于 $\frac1{102}$ 与 $\frac1{100}$ 之间，所以 $\frac{200}{102}\le I\le2$。

下表比较定积分与重积分的性质（曲线、曲面积分见 [2.2.13](/2.2.13)）：

| 性质 | 定积分 $\int_a^b$ | 重积分 |
|---|---|---|
| 积分方向 | $\int_a^b=-\int_b^a$ | 无方向，$\mathrm{d}\sigma,\mathrm{d}V>0$ |
| 线性、区域可加、保序、估值、中值 | 有 | 有 |
| 对称性 | 关于原点（奇偶函数） | 关于坐标轴、原点、坐标平面 |
| 轮换对称性 | 无 | 有 |

## 12.2. 二重积分的计算

### 12.2.1. 矩形区域上的累次积分

计算二重积分的基本方法是化为**累次积分**：先固定一个变量对另一个变量做定积分，再对剩下的变量做定积分。直观地看，用平面 $x=x_0$ 截曲顶柱体，截面面积为 $A(x_0)=\int_c^df(x_0,y)\,\mathrm{d}y$，再由"截面面积已知的立体体积" $V=\int_a^bA(x)\,\mathrm{d}x$（[2.2.7](/2.2.7)）得到体积。

**定理 12.2.1** 设 $f$ 在矩形 $D=[a,b]\times[c,d]$ 上连续，则

$$
\iint_Df(x,y)\,\mathrm{d}\sigma=\int_a^b\Big(\int_c^df(x,y)\,\mathrm{d}y\Big)\mathrm{d}x=\int_c^d\Big(\int_a^bf(x,y)\,\mathrm{d}x\Big)\mathrm{d}y.
$$

**证明** 记 $F(x)=\int_c^df(x,y)\,\mathrm{d}y$，它在 $[a,b]$ 上连续（定理 12.6.1）。用 $a=x_0<\cdots<x_m=b$、$c=y_0<\cdots<y_l=d$ 把 $D$ 分成小矩形 $D_{ij}$，$m_{ij}$、$M_{ij}$ 为 $f$ 在 $D_{ij}$ 上的下、上确界。对 $x\in[x_{i-1},x_i]$，

$$
\sum_jm_{ij}\Delta y_j\le F(x)\le\sum_jM_{ij}\Delta y_j,
$$

对 $x$ 积分并对 $i$ 求和，得 $\sum_{i,j}m_{ij}\Delta x_i\Delta y_j\le\int_a^bF(x)\,\mathrm{d}x\le\sum_{i,j}M_{ij}\Delta x_i\Delta y_j$。两端是二重积分的 **Darboux 和**，分割加细时都趋于 $\iint_Df\,\mathrm{d}\sigma$。另一个次序同理。$\square$

累次积分 $\int_a^b\Big(\int_c^df\,\mathrm{d}y\Big)\mathrm{d}x$ 通常简写为 $\int_a^b\mathrm{d}x\int_c^df(x,y)\,\mathrm{d}y$，称为先 $y$ 后 $x$ 的累次积分。在直角坐标系中，面积元记作 $\mathrm{d}\sigma=\mathrm{d}x\,\mathrm{d}y$，相当于用平行于坐标轴的直线"横平竖直"地分割区域。把重积分化为累次积分的这类定理一般称为 Fubini 定理。

### 12.2.2. 一般区域上的累次积分

**定理 12.2.2** 设 $f$ 在 $D$ 上连续。

1. 若 $D=\{(x,y)\mid a\le x\le b,\ y_1(x)\le y\le y_2(x)\}$（X 型区域：平行于 $y$ 轴的直线穿过 $D$ 内部时与边界恰有两个交点），$y_1,y_2$ 连续，则
$$
\iint_Df\,\mathrm{d}\sigma=\int_a^b\mathrm{d}x\int_{y_1(x)}^{y_2(x)}f(x,y)\,\mathrm{d}y;
$$
2. 若 $D=\{(x,y)\mid c\le y\le d,\ x_1(y)\le x\le x_2(y)\}$（Y 型区域），则 $\iint_Df\,\mathrm{d}\sigma=\int_c^d\mathrm{d}y\int_{x_1(y)}^{x_2(y)}f(x,y)\,\mathrm{d}x$。

**证明** 取包含 $D$ 的矩形 $[a,b]\times[c,d]$，把 $f$ 在 $D$ 外延拓为 $0$。延拓后的函数只在 $D$ 的边界上可能间断，仍可积，用定理 12.2.1 的方法即得。$\square$

**算法 12.2.1（二重积分化为累次积分）**

1. 画出积分区域 $D$，求出边界曲线的交点；
2. 选择积分次序：若平行于 $y$ 轴的直线穿过 $D$ 时与边界至多交于两点，可先 $y$ 后 $x$；否则用平行于坐标轴的直线把 $D$ 分成几块，分别处理；同时考虑被积函数，选择容易积出的次序；
3. 定限："后积先定限，限内画条线，先交下限写，后交上限见"——外层积分的限是 $D$ 在该坐标轴上的投影区间（常数）；在投影区间内任取一点作平行于另一坐标轴的直线，它穿入 $D$ 处的边界给出内层的下限，穿出处给出上限（一般是外层变量的函数）；
4. 计算累次积分。下限不能大于上限。

**例 12.2.1** 把 $\iint_Df\,\mathrm{d}\sigma$ 化为累次积分：

1. $D$ 由 $y=x$、$y=3x$、$x=1$、$x=3$ 围成：先 $y$ 后 $x$ 只需一个积分，$\int_1^3\mathrm{d}x\int_x^{3x}f\,\mathrm{d}y$；先 $x$ 后 $y$ 则要分成两块，$\int_1^3\mathrm{d}y\int_1^{y}f\,\mathrm{d}x+\int_3^9\mathrm{d}y\int_{y/3}^{3}f\,\mathrm{d}x$。
2. $D$ 是椭圆 $\frac{x^2}4+\frac{y^2}6\le1$：$\int_{-2}^2\mathrm{d}x\int_{-\sqrt{6(1-x^2/4)}}^{\sqrt{6(1-x^2/4)}}f\,\mathrm{d}y$。

**例 12.2.2** 计算下列二重积分。

1. $\iint_D|xy|\,\mathrm{d}\sigma$，$D=\{x^2+y^2\le a^2\}$：由对称性等于第一象限部分的 $4$ 倍，$4\int_0^a\mathrm{d}x\int_0^{\sqrt{a^2-x^2}}xy\,\mathrm{d}y=4\int_0^a\frac{x(a^2-x^2)}2\,\mathrm{d}x=\frac{a^4}2$。
2. $\iint_Dx\mathrm{e}^{xy}\,\mathrm{d}\sigma$，$D=[0,1]\times[-1,0]$：先对 $y$ 积分，$\int_0^1\mathrm{d}x\int_{-1}^0x\mathrm{e}^{xy}\,\mathrm{d}y=\int_0^1(1-\mathrm{e}^{-x})\,\mathrm{d}x=\frac1{\mathrm{e}}$。若先对 $x$ 积分则要用分部积分，繁得多。
3. $\iint_D\frac xy\,\mathrm{d}\sigma$，$D$ 由 $y=1$、$x=2$、$y=x^2$ 围成：先对 $x$ 积分，$\int_1^4\mathrm{d}y\int_{\sqrt y}^2\frac xy\,\mathrm{d}x=\int_1^4\frac{4-y}{2y}\,\mathrm{d}y=4\ln2-\frac32$。

### 12.2.3. 交换积分次序

同一个区域往往既是 X 型又是 Y 型（或可分块），两种次序的累次积分相等。交换积分次序的方法是：由累次积分的限画出区域，再按另一次序重新定限。

**例 12.2.3** 交换 $I=\int_0^1\mathrm{d}y\int_{y^2/2}^{\sqrt{3-y^2}}f(x,y)\,\mathrm{d}x$ 的积分次序。区域由抛物线 $y^2=2x$、圆 $x^2+y^2=3$、直线 $y=0$ 与 $y=1$ 围成，三者两两交于 $\big(\frac12,1\big)$、$(\sqrt2,1)$、$(\sqrt3,0)$。先对 $y$ 积分时上边界由三段组成，须分成三块：

$$
I=\int_0^{1/2}\mathrm{d}x\int_0^{\sqrt{2x}}f\,\mathrm{d}y+\int_{1/2}^{\sqrt2}\mathrm{d}x\int_0^1f\,\mathrm{d}y+\int_{\sqrt2}^{\sqrt3}\mathrm{d}x\int_0^{\sqrt{3-x^2}}f\,\mathrm{d}y.
$$

![例 12.2.3 的区域：按横条分割（先 x 后 y）只需一个累次积分，按竖条分割（先 y 后 x）要分成三块](./plots/integration-order.py)

有时必须交换次序才能积出，因为某些函数（如 $\mathrm{e}^{y^2}$、$\frac{\sin y}y$）的原函数不是初等函数。

**例 12.2.4** 计算 $\int_0^2\mathrm{d}x\int_x^2\mathrm{e}^{y^2}\,\mathrm{d}y$。内层积分积不出。区域为 $0\le x\le y\le2$，交换次序：

$$
\int_0^2\mathrm{d}y\int_0^y\mathrm{e}^{y^2}\,\mathrm{d}x=\int_0^2y\mathrm{e}^{y^2}\,\mathrm{d}y=\frac{\mathrm{e}^4-1}2.
$$

### 12.2.4. 极坐标下的二重积分

区域的边界是圆或射线、被积函数含 $x^2+y^2$ 时，用**极坐标** $x=r\cos\theta$，$y=r\sin\theta$ 更方便。用以原点为圆心的同心圆和从原点出发的射线分割区域，介于 $r$ 与 $r+\Delta r$、$\theta$ 与 $\theta+\Delta\theta$ 之间的小块面积为

$$
\frac12(r+\Delta r)^2\Delta\theta-\frac12r^2\Delta\theta=r\,\Delta r\,\Delta\theta+\frac12(\Delta r)^2\Delta\theta\approx r\,\Delta r\,\Delta\theta,
$$

所以面积元为 $\mathrm{d}\sigma=r\,\mathrm{d}r\,\mathrm{d}\theta$。这里的 $r$ 恰好是极坐标变换的 Jacobi 行列式（[2.2.10](/2.2.10) 例 10.7.4），一般原理见 [12.4](#sec-12.4)。

**定理 12.2.3** 设 $f$ 在 $D$ 上连续，$D$ 在极坐标下表示为 $\{(r,\theta)\mid\alpha\le\theta\le\beta,\ r_1(\theta)\le r\le r_2(\theta)\}$，则

$$
\iint_Df(x,y)\,\mathrm{d}\sigma=\int_\alpha^\beta\mathrm{d}\theta\int_{r_1(\theta)}^{r_2(\theta)}f(r\cos\theta,r\sin\theta)\,r\,\mathrm{d}r.
$$

注意不要漏掉面积元中的因子 $r$。极点在 $D$ 内部时 $\theta$ 从 $0$ 到 $2\pi$，$r$ 从 $0$ 开始。

**例 12.2.5** 常见区域的定限：圆盘 $x^2+y^2\le R^2$ 为 $0\le\theta\le2\pi$，$0\le r\le R$；圆环 $a^2\le x^2+y^2\le b^2$ 为 $0\le\theta\le2\pi$，$a\le r\le b$；圆盘 $x^2+y^2\le Rx$ 的边界 $r=R\cos\theta$，为 $-\frac\pi2\le\theta\le\frac\pi2$，$0\le r\le R\cos\theta$；三角形 $0\le x\le1$，$0\le y\le1-x$ 的斜边 $x+y=1$ 化为 $r=\frac1{\cos\theta+\sin\theta}$，为 $0\le\theta\le\frac\pi2$，$0\le r\le\frac1{\cos\theta+\sin\theta}$。

**例 12.2.6** 计算：

1. $\iint_Dx\sqrt{x^2+y^2}\,\mathrm{d}\sigma$，$D$ 为圆环 $4\le x^2+y^2\le16$ 在第一象限的部分：$\int_0^{\pi/2}\cos\theta\,\mathrm{d}\theta\int_2^4r^3\,\mathrm{d}r=1\cdot\frac{4^4-2^4}4=60$。
2. $\iint_D\sqrt{R^2-x^2-y^2}\,\mathrm{d}\sigma$，$D=\{x^2+y^2\le Rx\}$（球体被圆柱截下部分的体积之半）：
$$
\int_{-\pi/2}^{\pi/2}\mathrm{d}\theta\int_0^{R\cos\theta}\sqrt{R^2-r^2}\,r\,\mathrm{d}r=\int_{-\pi/2}^{\pi/2}\frac{R^3}3\big(1-|\sin\theta|^3\big)\,\mathrm{d}\theta=\frac{R^3}{3}\Big(\pi-\frac43\Big).
$$
注意 $\sqrt{1-\cos^2\theta}=|\sin\theta|$，绝对值不能丢。
3. 曲线 $(x^2+y^2)^2=3x^3$ 所围区域的面积：极坐标方程为 $r=3\cos^3\theta$（$-\frac\pi2\le\theta\le\frac\pi2$），面积为 $\int_{-\pi/2}^{\pi/2}\frac92\cos^6\theta\,\mathrm{d}\theta=9\int_0^{\pi/2}\cos^6\theta\,\mathrm{d}\theta=9\cdot\frac{5\cdot3\cdot1}{6\cdot4\cdot2}\cdot\frac\pi2=\frac{45\pi}{32}$，用到 **Wallis 积分**。

### 12.2.5. 反常二重积分与 Gauss 积分

在无界区域上，或被积函数无界时，二重积分定义为在一列"逐渐充满"区域的有界区域上积分的极限，与一元的**反常积分**类似。被积函数非负时，极限与区域列的选取无关。

**例 12.2.7** 讨论 $\iint_{\mathbb{R}^2}\dfrac{\mathrm{d}\sigma}{(1+x^2+y^2)^p}$ 的敛散性。在圆盘 $D_a=\{x^2+y^2\le a^2\}$ 上，

$$
\iint_{D_a}\frac{\mathrm{d}\sigma}{(1+x^2+y^2)^p}=2\pi\int_0^a\frac{r\,\mathrm{d}r}{(1+r^2)^p}=\begin{cases}\pi\ln(1+a^2),&p=1,\\[2pt] \dfrac{\pi}{1-p}\big[(1+a^2)^{1-p}-1\big],&p\ne1.\end{cases}
$$

$a\to+\infty$ 时，$p>1$ 收敛于 $\dfrac{\pi}{p-1}$，$p\le1$ 发散。对比一元的 $\int_1^{+\infty}\frac{\mathrm{d}x}{x^{q}}$ 在 $q>1$ 时收敛：二维的面积元多了一个因子 $r$，临界指数随维数升高。

**命题 12.2.1（Gauss 积分）** $\displaystyle\int_{-\infty}^{+\infty}\mathrm{e}^{-x^2}\,\mathrm{d}x=\sqrt\pi$，即 $\displaystyle\int_0^{+\infty}\mathrm{e}^{-x^2}\,\mathrm{d}x=\frac{\sqrt\pi}2$。

**证明** $\mathrm{e}^{-x^2}$ 的原函数不是初等函数，一元的方法无能为力；技巧是把它的平方写成二重积分，再用极坐标。记 $I(a)=\int_0^a\mathrm{e}^{-x^2}\,\mathrm{d}x$，由定理 12.2.1，

$$
I(a)^2=\int_0^a\mathrm{e}^{-x^2}\,\mathrm{d}x\int_0^a\mathrm{e}^{-y^2}\,\mathrm{d}y=\iint_{[0,a]^2}\mathrm{e}^{-(x^2+y^2)}\,\mathrm{d}\sigma.
$$

正方形 $[0,a]^2$ 夹在第一象限的两个四分之一圆盘 $D_1$（半径 $a$）与 $D_2$（半径 $\sqrt2a$）之间，被积函数为正，所以

$$
\frac\pi4\big(1-\mathrm{e}^{-a^2}\big)=\iint_{D_1}\mathrm{e}^{-(x^2+y^2)}\,\mathrm{d}\sigma\le I(a)^2\le\iint_{D_2}\mathrm{e}^{-(x^2+y^2)}\,\mathrm{d}\sigma=\frac\pi4\big(1-\mathrm{e}^{-2a^2}\big),
$$

其中 $\iint_{D_1}=\int_0^{\pi/2}\mathrm{d}\theta\int_0^a\mathrm{e}^{-r^2}r\,\mathrm{d}r$。令 $a\to+\infty$，由夹逼得 $I(+\infty)^2=\frac\pi4$。$\square$

作代换 $x=\sqrt t$ 得 $\Gamma\big(\frac12\big)=\int_0^{+\infty}t^{-1/2}\mathrm{e}^{-t}\,\mathrm{d}t=2\int_0^{+\infty}\mathrm{e}^{-x^2}\,\mathrm{d}x=\sqrt\pi$（**Gamma 函数**）；再作线性代换得 $\frac1{\sqrt{2\pi}\sigma}\int_{-\infty}^{+\infty}\mathrm{e}^{-(x-\mu)^2/(2\sigma^2)}\,\mathrm{d}x=1$，即正态分布 $\mathcal{N}(\mu,\sigma^2)$ 的密度函数积分为 $1$。

## 12.3. 三重积分的计算

### 12.3.1. 预备：二次曲面与投影

三重积分的积分区域常由二次曲面围成，定限时要知道它们的形状以及交线在坐标面上的投影。

| 名称 | 标准方程 | 特征 |
|---|---|---|
| 椭球面 | $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}+\dfrac{z^2}{c^2}=1$ | 横截面是椭圆，面积 $\pi ab\big(1-\frac{z^2}{c^2}\big)$ |
| 椭圆抛物面 | $z=\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}$ | $a=b$ 时为旋转抛物面 |
| 双曲抛物面（马鞍面） | $z=\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}$ | 原点是驻点但不是极值点 |
| 单叶双曲面 | $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}-\dfrac{z^2}{c^2}=1$ | 横截面是椭圆，$z=0$ 时最小 |
| 双叶双曲面 | $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}-\dfrac{z^2}{c^2}=-1$ | 只在 $\lvert z\rvert\ge c$ 处有点 |
| 二次锥面 | $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=\dfrac{z^2}{c^2}$ | 由过顶点的直线组成 |

![六种二次曲面：椭球面、椭圆抛物面、双曲抛物面、单叶双曲面、双叶双曲面与锥面](./plots/quadric-surfaces.py)

空间曲线 $F(x,y,z)=0$，$G(x,y,z)=0$ 在 $xOy$ 面上的投影：从两个方程中消去 $z$，得到投影柱面 $f(x,y)=0$，投影曲线为 $f(x,y)=0$，$z=0$。例如 $z=x^2+y^2$ 与 $x+y+z=1$ 的交线，消去 $z$ 得 $\big(x+\frac12\big)^2+\big(y+\frac12\big)^2=\frac32$，投影是 $xOy$ 面上的一个圆。区域 $\Omega$ 在 $xOy$ 面上的投影区域就是用这种方法得到的边界所围的区域。

### 12.3.2. 直角坐标：投影法与截面法

**定理 12.3.1（投影法，先一后二）** 设 $\Omega=\{(x,y,z)\mid(x,y)\in D_{xy},\ z_1(x,y)\le z\le z_2(x,y)\}$，其中 $D_{xy}$ 是 $\Omega$ 在 $xOy$ 面上的投影，$f$ 在 $\Omega$ 上连续，则

$$
\iiint_\Omega f\,\mathrm{d}V=\iint_{D_{xy}}\mathrm{d}\sigma\int_{z_1(x,y)}^{z_2(x,y)}f(x,y,z)\,\mathrm{d}z.
$$

几何上，这是用平行于 $z$ 轴的"竖条"分割 $\Omega$：在投影区域的每一点处，竖条从下曲面 $z=z_1$ 穿入、从上曲面 $z=z_2$ 穿出。内层的二重积分再化为累次积分，最终得到三次定积分。

**定理 12.3.2（截面法，先二后一）** 设 $\Omega$ 介于平面 $z=c_1$ 与 $z=c_2$ 之间，用平面 $z=z$ 截 $\Omega$ 所得截面为 $D_z$，则

$$
\iiint_\Omega f\,\mathrm{d}V=\int_{c_1}^{c_2}\mathrm{d}z\iint_{D_z}f(x,y,z)\,\mathrm{d}\sigma.
$$

这是用水平的"薄片"分割。当被积函数只含 $z$、截面 $D_z$ 的面积容易求出时，截面法特别简便。在直角坐标系中 $\mathrm{d}V=\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$。

**例 12.3.1** 计算 $\iiint_\Omega\dfrac{\mathrm{d}V}{(1+x+y+z)^3}$，$\Omega$ 由三个坐标面与平面 $x+y+z=1$ 围成。投影 $D_{xy}$ 为 $0\le x\le1$，$0\le y\le1-x$，$z$ 从 $0$ 到 $1-x-y$：

$$
\int_0^1\mathrm{d}x\int_0^{1-x}\mathrm{d}y\int_0^{1-x-y}\frac{\mathrm{d}z}{(1+x+y+z)^3}
=\int_0^1\mathrm{d}x\int_0^{1-x}\Big[\frac{1}{2(1+x+y)^2}-\frac18\Big]\mathrm{d}y
=\frac12\int_0^1\Big(\frac{1}{1+x}-\frac{3-x}{4}\Big)\mathrm{d}x=\frac{\ln2}2-\frac5{16}.
$$

**例 12.3.2** 计算 $\iiint_\Omega xyz\,\mathrm{d}V$，$\Omega=\{x^2+y^2+z^2\le1,\ x,y,z\ge0\}$。

$$
\int_0^1\mathrm{d}z\int_0^{\sqrt{1-z^2}}\mathrm{d}x\int_0^{\sqrt{1-z^2-x^2}}xyz\,\mathrm{d}y=\int_0^1\mathrm{d}z\int_0^{\sqrt{1-z^2}}\frac{xz(1-z^2-x^2)}2\,\mathrm{d}x=\int_0^1\frac{z(1-z^2)^2}8\,\mathrm{d}z=\frac1{48}.
$$

**例 12.3.3** 设 $\Omega$ 为椭球体 $\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}\le1$。用截面法，$D_z$ 是半轴为 $a\sqrt{1-z^2/c^2}$、$b\sqrt{1-z^2/c^2}$ 的椭圆，面积 $\pi ab\big(1-\frac{z^2}{c^2}\big)$，所以

$$
V=\int_{-c}^c\pi ab\Big(1-\frac{z^2}{c^2}\Big)\mathrm{d}z=\frac43\pi abc,\qquad
\iiint_\Omega z^2\,\mathrm{d}V=\int_{-c}^cz^2\pi ab\Big(1-\frac{z^2}{c^2}\Big)\mathrm{d}z=\frac4{15}\pi abc^3.
$$

由此（轮换）可得 $\iiint_\Omega\big(\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}\big)\mathrm{d}V=\frac45\pi abc$。

### 12.3.3. 柱坐标

**定义 12.3.1（柱坐标）** 空间点 $(x,y,z)$ 的**柱坐标**为 $(r,\theta,z)$，其中 $x=r\cos\theta$，$y=r\sin\theta$，$z=z$（$r\ge0$，$0\le\theta<2\pi$）。

柱坐标就是在 $xOy$ 面上用极坐标、$z$ 不变。$r=$ 常数是圆柱面，$\theta=$ 常数是半平面，$z=$ 常数是平面。体积元为 $\mathrm{d}V=r\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}z$。当 $\Omega$ 在坐标面上的投影用极坐标表示简单（区域由旋转面、圆柱面围成，被积函数含 $x^2+y^2$）时，先用投影法化为"$\iint_{D_{xy}}\mathrm{d}\sigma\int\mathrm{d}z$"，再对外层二重积分用极坐标。

**例 12.3.4** 计算：

1. $\iiint_\Omega z\,\mathrm{d}V$，$\Omega$ 由锥面 $z=\sqrt{x^2+y^2}$ 与平面 $z=2$ 围成。用截面法，$D_z$ 是半径为 $z$ 的圆盘：$\int_0^2z\cdot\pi z^2\,\mathrm{d}z=4\pi$。
2. $\iiint_\Omega(x^2+y^2)\,\mathrm{d}V$，$\Omega$ 由 $x^2+y^2=2z$ 与 $z=2$ 围成。投影法：投影为 $r\le2$，$z$ 从 $\frac{r^2}2$ 到 $2$，
$$
\int_0^{2\pi}\mathrm{d}\theta\int_0^2r^2\Big(2-\frac{r^2}2\Big)r\,\mathrm{d}r=2\pi\Big(8-\frac{16}{3}\Big)=\frac{16\pi}3;
$$
截面法：$\int_0^2\mathrm{d}z\int_0^{2\pi}\mathrm{d}\theta\int_0^{\sqrt{2z}}r^3\,\mathrm{d}r=\int_0^22\pi z^2\,\mathrm{d}z=\frac{16\pi}3$，结果相同。

### 12.3.4. 球坐标

**定义 12.3.2（球坐标）** 空间点 $(x,y,z)$ 的**球坐标**为 $(\rho,\varphi,\theta)$，其中

$$
x=\rho\sin\varphi\cos\theta,\qquad y=\rho\sin\varphi\sin\theta,\qquad z=\rho\cos\varphi,
$$

$\rho\ge0$ 是到原点的距离，$\varphi\in[0,\pi]$ 是与 $z$ 轴正向的夹角，$\theta\in[0,2\pi)$ 与柱坐标中相同。

$\rho=$ 常数是球面，$\varphi=$ 常数是以原点为顶点的半圆锥面，$\theta=$ 常数是半平面。体积元为 $\mathrm{d}V=\rho^2\sin\varphi\,\mathrm{d}\rho\,\mathrm{d}\varphi\,\mathrm{d}\theta$（由 Jacobi 行列式推出，见例 12.4.4；也可以从小"球面六面体"的三条棱长 $\mathrm{d}\rho$、$\rho\,\mathrm{d}\varphi$、$\rho\sin\varphi\,\mathrm{d}\theta$ 看出）。区域由球面、锥面围成，被积函数含 $x^2+y^2+z^2$ 时用球坐标。

**例 12.3.5** 用球坐标表示与计算：

1. 球体 $x^2+y^2+z^2\le R^2$：$\iiint_\Omega f\,\mathrm{d}V=\int_0^{2\pi}\mathrm{d}\theta\int_0^\pi\mathrm{d}\varphi\int_0^Rf\,\rho^2\sin\varphi\,\mathrm{d}\rho$，其中 $f$ 中代入球坐标。$f=1$ 时得球的体积 $\frac43\pi R^3$。
2. $\iiint_\Omega\sqrt{x^2+y^2+z^2}\,\mathrm{d}V$，$\Omega=\{x^2+y^2+z^2\le z\}$（球心 $(0,0,\frac12)$、半径 $\frac12$ 的球）：球面方程化为 $\rho=\cos\varphi$，
$$
\int_0^{2\pi}\mathrm{d}\theta\int_0^{\pi/2}\mathrm{d}\varphi\int_0^{\cos\varphi}\rho\cdot\rho^2\sin\varphi\,\mathrm{d}\rho=2\pi\int_0^{\pi/2}\frac{\cos^4\varphi}4\sin\varphi\,\mathrm{d}\varphi=\frac\pi{10}.
$$
3. 化累次积分 $\int_0^1\mathrm{d}x\int_0^{\sqrt{1-x^2}}\mathrm{d}y\int_{\sqrt{x^2+y^2}}^{\sqrt{2-x^2-y^2}}z^2\,\mathrm{d}z$ 为球坐标并计算。区域在锥面 $z=\sqrt{x^2+y^2}$（$\varphi=\frac\pi4$）之上、球面 $\rho=\sqrt2$ 之内、第一卦限：
$$
\int_0^{\pi/2}\mathrm{d}\theta\int_0^{\pi/4}\mathrm{d}\varphi\int_0^{\sqrt2}\rho^2\cos^2\varphi\cdot\rho^2\sin\varphi\,\mathrm{d}\rho=\frac\pi2\cdot\frac{1}{3}\Big(1-\frac{\sqrt2}{4}\Big)\cdot\frac{4\sqrt2}5=\frac{\pi}{15}(2\sqrt2-1).
$$

## 12.4. 重积分的变量替换

### 12.4.1. 二重积分的变量替换

直角坐标与极坐标都是特殊的分割方式。一般地，设变换 $x=x(u,v)$，$y=y(u,v)$ 把 $uv$ 平面上的区域 $D'$ 一一地映成 $xy$ 平面上的区域 $D$。用 $u=$ 常数、$v=$ 常数的坐标曲线网分割 $D$，$uv$ 平面上以 $(u,v)$ 为顶点、边长 $\Delta u,\Delta v$ 的小矩形被映成一个小曲边四边形，在一阶近似下它是以

$$
\boldsymbol{a}=(x_u,y_u)\Delta u,\qquad\boldsymbol{b}=(x_v,y_v)\Delta v
$$

为邻边的平行四边形（[2.2.10](/2.2.10) 中可微的含义：映射在局部近似于线性映射 $J$）。平行四边形的面积是以 $\boldsymbol{a},\boldsymbol{b}$ 为列的行列式的绝对值，所以

$$
\Delta\sigma\approx\Big|\det\frac{\partial(x,y)}{\partial(u,v)}\Big|\Delta u\,\Delta v,\qquad\text{即}\quad\mathrm{d}x\,\mathrm{d}y=\Big|\det\frac{\partial(x,y)}{\partial(u,v)}\Big|\mathrm{d}u\,\mathrm{d}v.
$$

这就是线性代数中"行列式是线性变换的变积系数"在局部的应用：可微映射在每一点附近近似于线性映射 $J_f$，它把面积放大 $|\det J_f|$ 倍。

**定理 12.4.1（二重积分的换元公式）** 设 $f$ 在有界闭区域 $D$ 上连续，变换 $x=x(u,v)$，$y=y(u,v)$ 有连续偏导数，把 $D'$ 一一地映成 $D$，且 $\det\dfrac{\partial(x,y)}{\partial(u,v)}\ne0$（允许在面积为零的集合上不成立），则

$$
\iint_Df(x,y)\,\mathrm{d}x\,\mathrm{d}y=\iint_{D'}f\big(x(u,v),y(u,v)\big)\Big|\det\frac{\partial(x,y)}{\partial(u,v)}\Big|\,\mathrm{d}u\,\mathrm{d}v.
$$

与定积分的换元法相比：定积分中 $\mathrm{d}x=x'(t)\,\mathrm{d}t$ 带符号，因为定积分有方向；重积分中面积为正，取 Jacobi 行列式的绝对值。重积分换元的主要目的往往是化简积分区域，而不是被积函数。由逆映射定理，$\det\dfrac{\partial(x,y)}{\partial(u,v)}=1\Big/\det\dfrac{\partial(u,v)}{\partial(x,y)}$，当新变量 $u,v$ 由 $x,y$ 直接给出时，用后者计算更方便。

![坐标网格在变换下的像：极坐标把 (r, θ) 平面的方格映成环形扇区，面积放大系数为 r；变换 x = u^(−2/5) v^(1/5), y = u^(−1/5) v^(3/5) 把方格映成曲边四边形（例 12.4.3）](./plots/change-of-variables-grid.py)

**例 12.4.1（极坐标）** $x=r\cos\theta$，$y=r\sin\theta$ 的 Jacobi 行列式为 $r$，由定理 12.4.1 即得定理 12.2.3。变换在 $r=0$ 处不是一一的，Jacobi 行列式为零，但这只是一个零面积集合，不影响公式。

**定义 12.4.1（广义极坐标）** 称变换 $x=x_0+ar\cos\theta$，$y=y_0+br\sin\theta$（$a,b>0$）为**广义极坐标**变换，其 Jacobi 行列式为 $abr$。

它把椭圆 $\frac{(x-x_0)^2}{a^2}+\frac{(y-y_0)^2}{b^2}\le1$ 化为 $r\le1$，遇到椭圆区域时使用。椭圆的面积为 $\int_0^{2\pi}\mathrm{d}\theta\int_0^1abr\,\mathrm{d}r=\pi ab$。

**例 12.4.2** 计算 $\iint_D\sqrt{1-\frac{x^2}{a^2}-\frac{y^2}{b^2}}\,\mathrm{d}\sigma$，$D$ 为椭圆 $\frac{x^2}{a^2}+\frac{y^2}{b^2}\le1$。用广义极坐标，

$$
\int_0^{2\pi}\mathrm{d}\theta\int_0^1\sqrt{1-r^2}\,abr\,\mathrm{d}r=2\pi ab\cdot\frac13=\frac{2\pi ab}3.
$$

**例 12.4.3** 计算 $\iint_Dxy\,\mathrm{d}x\,\mathrm{d}y$，$D$ 由 $y=ax^3$、$y=bx^3$、$y^2=px$、$y^2=qx$ 在第一象限围成（$0<a<b$，$0<p<q$）。令 $u=\dfrac y{x^3}$，$v=\dfrac{y^2}x$，$D$ 变为矩形 $[a,b]\times[p,q]$。

$$
\det\frac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}-3yx^{-4}&x^{-3}\\ -y^2x^{-2}&2yx^{-1}\end{vmatrix}=-\frac{5y^2}{x^5},\qquad\Big|\det\frac{\partial(x,y)}{\partial(u,v)}\Big|=\frac{x^5}{5y^2}.
$$

反解得 $x=u^{-2/5}v^{1/5}$，$y=u^{-1/5}v^{3/5}$，于是 $xy\cdot\dfrac{x^5}{5y^2}=\dfrac{x^6}{5y}=\dfrac15u^{-11/5}v^{3/5}$，

$$
\iint_Dxy\,\mathrm{d}x\,\mathrm{d}y=\frac15\int_a^bu^{-11/5}\,\mathrm{d}u\int_p^qv^{3/5}\,\mathrm{d}v=\frac5{48}\big(a^{-6/5}-b^{-6/5}\big)\big(q^{8/5}-p^{8/5}\big).
$$

### 12.4.2. 三重积分的变量替换

三维情形完全类似：变换 $x=x(u,v,w)$，$y=y(u,v,w)$，$z=z(u,v,w)$ 把小长方体近似地映成以 $\boldsymbol{r}_u\Delta u$、$\boldsymbol{r}_v\Delta v$、$\boldsymbol{r}_w\Delta w$ 为棱的平行六面体，其体积是混合积的绝对值，即 $\Big|\det\dfrac{\partial(x,y,z)}{\partial(u,v,w)}\Big|\Delta u\,\Delta v\,\Delta w$。

**定理 12.4.2（三重积分的换元公式）** 在与定理 12.4.1 相同的条件下，

$$
\iiint_\Omega f(x,y,z)\,\mathrm{d}V=\iiint_{\Omega'}f\big(x(u,v,w),y(u,v,w),z(u,v,w)\big)\Big|\det\frac{\partial(x,y,z)}{\partial(u,v,w)}\Big|\,\mathrm{d}u\,\mathrm{d}v\,\mathrm{d}w.
$$

**例 12.4.4（柱坐标与球坐标的体积元）** 柱坐标的 Jacobi 行列式为

$$
\det\frac{\partial(x,y,z)}{\partial(r,\theta,z)}=\begin{vmatrix}\cos\theta&-r\sin\theta&0\\ \sin\theta&r\cos\theta&0\\ 0&0&1\end{vmatrix}=r.
$$

球坐标的 Jacobi 行列式按第三行展开：

$$
\det\frac{\partial(x,y,z)}{\partial(\rho,\varphi,\theta)}=\begin{vmatrix}\sin\varphi\cos\theta&\rho\cos\varphi\cos\theta&-\rho\sin\varphi\sin\theta\\ \sin\varphi\sin\theta&\rho\cos\varphi\sin\theta&\rho\sin\varphi\cos\theta\\ \cos\varphi&-\rho\sin\varphi&0\end{vmatrix}
=\rho^2\cos^2\varphi\sin\varphi+\rho^2\sin^3\varphi=\rho^2\sin\varphi.
$$

**例 12.4.5（广义球坐标）** 求椭球体 $\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}\le1$ 的体积。令 $x=a\rho\sin\varphi\cos\theta$，$y=b\rho\sin\varphi\sin\theta$，$z=c\rho\cos\varphi$，Jacobi 行列式为 $abc\rho^2\sin\varphi$，区域变为 $\rho\le1$：

$$
V=\int_0^{2\pi}\mathrm{d}\theta\int_0^\pi\mathrm{d}\varphi\int_0^1abc\rho^2\sin\varphi\,\mathrm{d}\rho=2\pi\cdot2\cdot\frac{abc}3=\frac43\pi abc,
$$

与例 12.3.3 的结果一致。

**例 12.4.6** 计算 $\iiint_\Omega(x+y+z)\cos(x+y+z)^2\,\mathrm{d}V$，$\Omega$：$0\le x-y\le1$，$0\le x-z\le1$，$0\le x+y+z\le1$。令 $u=x-y$，$v=x-z$，$w=x+y+z$，$\Omega$ 变为单位立方体。

$$
\det\frac{\partial(u,v,w)}{\partial(x,y,z)}=\begin{vmatrix}1&-1&0\\ 1&0&-1\\ 1&1&1\end{vmatrix}=3,\qquad\mathrm{d}V=\frac13\,\mathrm{d}u\,\mathrm{d}v\,\mathrm{d}w,
$$

原式 $=\dfrac13\int_0^1\mathrm{d}u\int_0^1\mathrm{d}v\int_0^1w\cos w^2\,\mathrm{d}w=\dfrac{\sin1}6$。这是线性变换，Jacobi 行列式是常数，正是线性变换的变积系数。

### 12.4.3. 综合例题

**例 12.4.7** 证明：曲面 $z=x^2+y^2+a$（$a>0$）在任一点的切平面与曲面 $z=x^2+y^2$ 所围的体积都等于 $\frac{\pi a^2}2$。

**证明** 在 $(x_0,y_0,z_0)$ 处切平面为 $z=z_0+2x_0(x-x_0)+2y_0(y-y_0)=2x_0x+2y_0y-z_0+2a$（用到 $z_0=x_0^2+y_0^2+a$）。它与 $z=x^2+y^2$ 的交线在 $xOy$ 面的投影为 $(x-x_0)^2+(y-y_0)^2=a$。所围体积为

$$
V=\iint_{(x-x_0)^2+(y-y_0)^2\le a}\big[2x_0x+2y_0y-z_0+2a-(x^2+y^2)\big]\mathrm{d}\sigma=\iint_{u^2+v^2\le a}\big(a-u^2-v^2\big)\,\mathrm{d}u\,\mathrm{d}v,
$$

其中平移 $u=x-x_0$，$v=y-y_0$ 的 Jacobi 行列式为 $1$，被积函数化简后与切点无关。用极坐标，$V=2\pi\int_0^{\sqrt a}(a-r^2)r\,\mathrm{d}r=\frac{\pi a^2}2$。$\square$

**例 12.4.8** 设 $f\in C[0,1]$，证明 $\displaystyle\int_0^1\mathrm{d}x\int_x^1\mathrm{d}y\int_x^yf(x)f(y)f(z)\,\mathrm{d}z=\frac16\Big(\int_0^1f(t)\,\mathrm{d}t\Big)^3$。

**证明** 记 $F(u)=\int_0^uf(t)\,\mathrm{d}t$。逐次积分：最内层为 $f(x)f(y)\big(F(y)-F(x)\big)$；对 $y$ 积分，$\int_x^1f(y)\big(F(y)-F(x)\big)\,\mathrm{d}y=\frac12\big(F(1)-F(x)\big)^2$；最后 $\frac12\int_0^1f(x)\big(F(1)-F(x)\big)^2\,\mathrm{d}x=\frac16F(1)^3$。$\square$

另一个看法：积分区域是 $0\le x\le z\le y\le1$，被积函数关于 $x,y,z$ 对称，立方体 $[0,1]^3$ 按三个坐标的大小顺序分成 $6$ 个全等的部分，每部分上的积分相同。

## 12.5. 重积分的应用

面积与体积的公式已在前面多次使用：$\sigma(D)=\iint_D\mathrm{d}\sigma$，$V(\Omega)=\iiint_\Omega\mathrm{d}V$。曲面的面积要用到曲面上的面积元，放在 [2.2.13](/2.2.13)。

设物体 $\Omega$ 的密度为 $\rho(x,y,z)$，质量 $M=\iiint_\Omega\rho\,\mathrm{d}V$。质点系的质心是以质量为权的加权平均位置，把求和换成积分：

**定义 12.5.1（质心）** 密度为 $\rho$ 的物体 $\Omega$ 的**质心** $(\bar x,\bar y,\bar z)$ 为

$$
\bar x=\frac1M\iiint_\Omega x\rho\,\mathrm{d}V,\qquad\bar y=\frac1M\iiint_\Omega y\rho\,\mathrm{d}V,\qquad\bar z=\frac1M\iiint_\Omega z\rho\,\mathrm{d}V.
$$

平面薄板的质心类似地用二重积分定义。密度为常数时质心称为形心，只与形状有关；由对称性，形心在对称轴（对称面）上。

**定义 12.5.2（转动惯量）** 物体 $\Omega$ 绕某轴的**转动惯量**为 $I=\iiint_\Omega d^2\rho\,\mathrm{d}V$，其中 $d$ 是点到轴的距离。例如绕 $z$ 轴 $I_z=\iiint_\Omega(x^2+y^2)\rho\,\mathrm{d}V$；平面薄板绕 $x$ 轴 $I_x=\iint_Dy^2\mu\,\mathrm{d}\sigma$。

**例 12.5.1** 均匀半圆盘 $D=\{x^2+y^2\le a^2,\ y\ge0\}$ 的形心：由对称性 $\bar x=0$，

$$
\bar y=\frac{1}{\pi a^2/2}\int_0^\pi\mathrm{d}\theta\int_0^ar\sin\theta\cdot r\,\mathrm{d}r=\frac{2}{\pi a^2}\cdot2\cdot\frac{a^3}3=\frac{4a}{3\pi}.
$$

**例 12.5.2** 质量为 $M$、半径为 $R$ 的均匀球体绕直径的转动惯量。取直径为 $z$ 轴，密度 $\rho_0=\frac{3M}{4\pi R^3}$，用球坐标：

$$
I_z=\rho_0\int_0^{2\pi}\mathrm{d}\theta\int_0^\pi\mathrm{d}\varphi\int_0^R\rho^2\sin^2\varphi\cdot\rho^2\sin\varphi\,\mathrm{d}\rho=\rho_0\cdot2\pi\cdot\frac43\cdot\frac{R^5}5=\frac25MR^2.
$$

最后是引力。密度为 $\rho$ 的物体对位于 $P_0(x_0,y_0,z_0)$ 处单位质量质点的引力为 $\boldsymbol{F}=G\iiint_\Omega\dfrac{\rho\,(x-x_0,y-y_0,z-z_0)}{r^3}\,\mathrm{d}V$，$r$ 为 $(x,y,z)$ 到 $P_0$ 的距离，$G$ 为引力常数。每个分量都是一个三重积分。例如可以算出，均匀球体对球外质点的引力等于把全部质量集中在球心时的引力，这一结论在 [2.2.14](/2.2.14) 中用 Gauss 公式更简单地得到。

## 12.6. 含参变量积分

### 12.6.1. 含参变量的定积分

许多函数是用积分定义的，例如 **Gamma 函数** $\Gamma(s)=\int_0^{+\infty}x^{s-1}\mathrm{e}^{-x}\,\mathrm{d}x$。被积函数含有一个参数时，积分的值是参数的函数，我们关心它的连续性、可积性与可微性，即能否在积分号下取极限、积分与求导。

**定义 12.6.1（含参变量积分）** 设对区间 $I$ 中的每个 $x$，$g(x,y)$ 关于 $y$ 在 $[c,d]$ 上可积，则称

$$
f(x)=\int_c^dg(x,y)\,\mathrm{d}y,\qquad x\in I
$$

为**含参变量积分**（$x$ 为参变量）。积分限也可以依赖于 $x$：$\int_{\alpha(x)}^{\beta(x)}g(x,y)\,\mathrm{d}y$。

**定理 12.6.1（连续性）** 若 $g$ 在矩形 $[a,b]\times[c,d]$ 上连续，则 $f(x)=\int_c^dg(x,y)\,\mathrm{d}y$ 在 $[a,b]$ 上连续。

**证明** $g$ 在有界闭区域上连续，从而**一致连续**：对任意 $\varepsilon>0$，存在 $\delta>0$，当 $|x_1-x_2|<\delta$ 时，对一切 $y\in[c,d]$ 有 $|g(x_1,y)-g(x_2,y)|<\frac{\varepsilon}{d-c}$。于是 $|f(x_1)-f(x_2)|\le\int_c^d|g(x_1,y)-g(x_2,y)|\,\mathrm{d}y<\varepsilon$。$\square$

因此 $\lim\limits_{x\to x_0}\int_c^dg(x,y)\,\mathrm{d}y=\int_c^d\lim\limits_{x\to x_0}g(x,y)\,\mathrm{d}y$：连续时极限与积分可以交换。

**定理 12.6.2（积分次序交换）** 若 $g$ 在 $[a,b]\times[c,d]$ 上连续，则

$$
\int_a^b\mathrm{d}x\int_c^dg(x,y)\,\mathrm{d}y=\int_c^d\mathrm{d}y\int_a^bg(x,y)\,\mathrm{d}x.
$$

这就是定理 12.2.1：两者都等于 $g$ 在矩形上的二重积分。

**定理 12.6.3（积分号下求导）** 若 $g$ 与 $g_x$ 都在 $[a,b]\times[c,d]$ 上连续，则 $f(x)=\int_c^dg(x,y)\,\mathrm{d}y$ 在 $[a,b]$ 上可导，且

$$
f'(x)=\int_c^d\frac{\partial g}{\partial x}(x,y)\,\mathrm{d}y.
$$

**证明** 由 Lagrange 中值定理，

$$
\frac{f(x+\Delta x)-f(x)}{\Delta x}=\int_c^d\frac{g(x+\Delta x,y)-g(x,y)}{\Delta x}\,\mathrm{d}y=\int_c^dg_x(x+\theta\Delta x,y)\,\mathrm{d}y,
$$

$\theta=\theta(x,\Delta x,y)\in(0,1)$。$g_x$ 在矩形上一致连续，对任意 $\varepsilon>0$，$|\Delta x|$ 充分小时对一切 $y$ 有 $|g_x(x+\theta\Delta x,y)-g_x(x,y)|<\frac{\varepsilon}{d-c}$，所以上式与 $\int_c^dg_x(x,y)\,\mathrm{d}y$ 之差小于 $\varepsilon$。$\square$

**定理 12.6.4（变限的情形）** 若 $g$、$g_x$ 在 $[a,b]\times[c,d]$ 上连续，$\alpha(x),\beta(x)$ 在 $[a,b]$ 上可导且取值于 $[c,d]$，则 $f(x)=\int_{\alpha(x)}^{\beta(x)}g(x,y)\,\mathrm{d}y$ 可导，且

$$
f'(x)=\int_{\alpha(x)}^{\beta(x)}\frac{\partial g}{\partial x}(x,y)\,\mathrm{d}y+g\big(x,\beta(x)\big)\beta'(x)-g\big(x,\alpha(x)\big)\alpha'(x).
$$

**证明** 令 $\Phi(x,u,v)=\int_u^vg(x,y)\,\mathrm{d}y$，则 $f(x)=\Phi(x,\alpha(x),\beta(x))$。由定理 12.6.3 与**变上限积分**的求导，$\Phi_x=\int_u^vg_x\,\mathrm{d}y$，$\Phi_v=g(x,v)$，$\Phi_u=-g(x,u)$，三者都连续，故 $\Phi$ 可微，由链式法则即得。$\square$

两项"边界项"来自积分限的变化，第一项来自被积函数的变化。$g$ 不含 $x$ 时就是变上限积分的求导公式。

**例 12.6.1** 计算 $\displaystyle\int_0^\pi\ln\Big(1+\frac12\cos x\Big)\mathrm{d}x$。引入参数，令 $I(y)=\int_0^\pi\ln(1+y\cos x)\,\mathrm{d}x$（$|y|<1$），$I(0)=0$。由定理 12.6.3，

$$
I'(y)=\int_0^\pi\frac{\cos x}{1+y\cos x}\,\mathrm{d}x=\frac1y\int_0^\pi\Big(1-\frac1{1+y\cos x}\Big)\mathrm{d}x=\frac\pi y-\frac{\pi}{y\sqrt{1-y^2}}\qquad(y\ne0),
$$

其中 $\int_0^\pi\frac{\mathrm{d}x}{1+y\cos x}=\frac{\pi}{\sqrt{1-y^2}}$ 由**万能代换** $t=\tan\frac x2$ 求得。令 $y=\sin\varphi$ 积分得 $I(y)=\pi\ln\big(1+\sqrt{1-y^2}\big)+C$，由 $I(0)=0$ 得 $C=-\pi\ln2$。所以

$$
\int_0^\pi\ln\Big(1+\frac12\cos x\Big)\mathrm{d}x=I\Big(\frac12\Big)=\pi\ln\frac{2+\sqrt3}{4}.
$$

**例 12.6.2** 计算 $\displaystyle\int_0^1\frac{x^b-x^a}{\ln x}\,\mathrm{d}x$（$0<a<b$）。注意 $\dfrac{x^b-x^a}{\ln x}=\int_a^bx^y\,\mathrm{d}y$，被积函数 $x^y$ 在 $[0,1]\times[a,b]$ 上连续，由定理 12.6.2 交换积分次序：

$$
\int_0^1\mathrm{d}x\int_a^bx^y\,\mathrm{d}y=\int_a^b\mathrm{d}y\int_0^1x^y\,\mathrm{d}x=\int_a^b\frac{\mathrm{d}y}{y+1}=\ln\frac{1+b}{1+a}.
$$

### 12.6.2. 含参变量的反常积分

积分区间无穷（或被积函数无界）时，交换极限与积分需要比"对每个参数收敛"更强的条件，正如函数项级数需要**一致收敛**。

**定义 12.6.2（一致收敛）** 设对每个 $x\in I$，$\int_c^{+\infty}g(x,y)\,\mathrm{d}y$ 收敛于 $f(x)$。若对任意 $\varepsilon>0$，存在与 $x$ 无关的 $N$，使当 $T>N$ 时，对一切 $x\in I$ 都有

$$
\Big|\int_c^Tg(x,y)\,\mathrm{d}y-f(x)\Big|=\Big|\int_T^{+\infty}g(x,y)\,\mathrm{d}y\Big|<\varepsilon,
$$

则称含参变量的反常积分 $\int_c^{+\infty}g(x,y)\,\mathrm{d}y$ 关于 $x\in I$ **一致收敛**。

以下结论只叙述，证明与函数项级数的相应定理（[2.2.9](/2.2.9)）平行。

**定理 12.6.5（Cauchy 准则与 M 判别法）** $\int_c^{+\infty}g(x,y)\,\mathrm{d}y$ 关于 $x\in I$ 一致收敛，当且仅当对任意 $\varepsilon>0$，存在 $N$，使当 $T>S>N$ 时对一切 $x\in I$ 有 $\Big|\int_S^Tg(x,y)\,\mathrm{d}y\Big|<\varepsilon$。特别地，若存在 $M(y)$ 使 $|g(x,y)|\le M(y)$ 对一切 $x\in I$ 成立，且 $\int_c^{+\infty}M(y)\,\mathrm{d}y$ 收敛，则积分关于 $x\in I$ 一致收敛。

**定理 12.6.6** 设 $g$ 在 $I\times[c,+\infty)$ 上连续，$f(x)=\int_c^{+\infty}g(x,y)\,\mathrm{d}y$ 关于 $x\in I$ 一致收敛，则：

1. $f$ 在 $I$ 上连续；
2. 若 $I=[a,b]$，则 $\int_a^bf(x)\,\mathrm{d}x=\int_c^{+\infty}\mathrm{d}y\int_a^bg(x,y)\,\mathrm{d}x$；
3. 若 $g_x$ 也在 $I\times[c,+\infty)$ 上连续，$\int_c^{+\infty}g(x,y)\,\mathrm{d}y$ 对每个 $x\in I$ 收敛，且 $\int_c^{+\infty}g_x(x,y)\,\mathrm{d}y$ 关于 $x\in I$ 一致收敛，则 $f'(x)=\int_c^{+\infty}g_x(x,y)\,\mathrm{d}y$。

**命题 12.6.1（Dirichlet 积分）** 对常数 $a$，

$$
\int_0^{+\infty}\frac{\sin ax}{x}\,\mathrm{d}x=\frac\pi2\operatorname{sgn}a,\qquad\text{特别地}\quad\int_0^{+\infty}\frac{\sin x}{x}\,\mathrm{d}x=\frac\pi2.
$$

**证明** 这个积分条件收敛，不能直接对参数 $a$ 求导（$\int_0^{+\infty}\cos ax\,\mathrm{d}x$ 发散）。引入收敛因子 $\mathrm{e}^{-kx}$（$k>0$），令

$$
I(a)=\int_0^{+\infty}\mathrm{e}^{-kx}\frac{\sin ax}{x}\,\mathrm{d}x.
$$

对 $a$ 求导后的积分 $\int_0^{+\infty}\mathrm{e}^{-kx}\cos ax\,\mathrm{d}x$ 被 $\mathrm{e}^{-kx}$ 控制，由 M 判别法关于 $a\in\mathbb{R}$ 一致收敛；两次分部积分可得它等于 $\dfrac{k}{a^2+k^2}$。由定理 12.6.6 之 3，$I'(a)=\dfrac{k}{a^2+k^2}$，又 $I(0)=0$，所以 $I(a)=\arctan\dfrac ak$。

再把 $\int_0^{+\infty}\mathrm{e}^{-kx}\frac{\sin ax}{x}\,\mathrm{d}x$ 看作以 $k$ 为参数的积分（$a\ne0$ 固定）。用分部积分估计 $\int_S^T$ 可以证明它关于 $k\in[0,+\infty)$ 一致收敛，由定理 12.6.6 之 1 它在 $k=0$ 处右连续，所以

$$
\int_0^{+\infty}\frac{\sin ax}{x}\,\mathrm{d}x=\lim_{k\to0^+}\arctan\frac ak=\frac\pi2\operatorname{sgn}a.\qquad\square
$$

$\frac{\sin x}{x}$ 的原函数不是初等函数，这里的方法——引入参数、对参数求导、再积分回来——是计算这类定积分的典型手段。

## 小结

| 积分 | 坐标 | 面积元 / 体积元 | 适用情形 |
|---|---|---|---|
| 二重积分 | 直角坐标 | $\mathrm{d}x\,\mathrm{d}y$ | 边界由 $y=y_i(x)$ 或 $x=x_i(y)$ 给出 |
| | 极坐标 | $r\,\mathrm{d}r\,\mathrm{d}\theta$ | 圆、扇形、环形区域，被积函数含 $x^2+y^2$ |
| | 广义极坐标 | $abr\,\mathrm{d}r\,\mathrm{d}\theta$ | 椭圆区域 |
| | 一般换元 | $\Big\lvert\det\dfrac{\partial(x,y)}{\partial(u,v)}\Big\rvert\mathrm{d}u\,\mathrm{d}v$ | 边界由两族曲线 $u=$ 常数、$v=$ 常数组成 |
| 三重积分 | 直角坐标 | $\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$ | 投影法（先一后二）、截面法（先二后一） |
| | 柱坐标 | $r\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}z$ | 旋转体、圆柱，被积函数含 $x^2+y^2$ |
| | 球坐标 | $\rho^2\sin\varphi\,\mathrm{d}\rho\,\mathrm{d}\varphi\,\mathrm{d}\theta$ | 球、锥，被积函数含 $x^2+y^2+z^2$ |
| | 一般换元 | $\Big\lvert\det\dfrac{\partial(x,y,z)}{\partial(u,v,w)}\Big\rvert\mathrm{d}u\,\mathrm{d}v\,\mathrm{d}w$ | 区域由三族曲面围成 |

| 含参变量积分 | 条件 | 结论 |
|---|---|---|
| 正常积分 $\int_c^dg(x,y)\,\mathrm{d}y$ | $g$ 连续 | 连续，可交换积分次序 |
| | $g,g_x$ 连续 | 积分号下求导；变限时加边界项 $g(x,\beta)\beta'-g(x,\alpha)\alpha'$ |
| 反常积分 $\int_c^{+\infty}g(x,y)\,\mathrm{d}y$ | 一致收敛（M 判别法） | 连续、可交换次序；导数的积分一致收敛时可求导 |
