---
title: 变分法初步
---

微积分中的极值问题求的是使函数取极值的点；许多几何与物理问题求的却是使某个量取极值的**函数**或曲线：连接两点的最短曲线、旋转后面积最小的曲线、质点下滑最快的轨道、给定周长围出最大面积的曲线。这样的"函数的函数"称为泛函，研究泛函极值的学科称为变分法。它的基本结论是：极值曲线必须满足一个二阶常微分方程——Euler–Lagrange 方程。于是变分问题归结为微分方程的边值问题，这正是本章放在常微分方程课程中的原因；反过来，力学中的运动方程也可以看成某个泛函的 Euler–Lagrange 方程（Hamilton 原理）。

本章先给出泛函与变分问题的例子，再由变分学基本引理导出 Euler–Lagrange 方程，讨论它可以降阶的几种情形，然后解最小旋转曲面、最速降线、球面测地线三个经典问题，最后简述多个未知函数的情形和带约束的等周问题，后者是 **Lagrange 乘子法**（[2.2.11](/2.2.11#sec-11.6)）在无穷维中的类比。

## 13.1. 泛函与变分问题

**定义 13.1.1（泛函）** 设 $D$ 是某个函数类（例如 $[a,b]$ 上满足给定边界条件的 $C^1$ 函数全体）。若对每个 $y\in D$ 都对应一个实数 $J[y]$，则称 $J$ 为定义在 $D$ 上的**泛函**，$D$ 称为容许函数类。

本章讨论的泛函都是积分型的：

$$
J[y]=\int_a^bF\big(x,y(x),y'(x)\big)\,\mathrm{d}x,\qquad D=\{y\in C^1[a,b]\mid y(a)=A,\ y(b)=B\},\tag{13.1}
$$
其中 $F(x,y,p)$ 是给定的三元函数，称为被积函数（或 Lagrange 函数）。若存在 $y_0\in D$ 和 $\delta>0$，使对一切满足 $\max_{[a,b]}|y-y_0|+\max_{[a,b]}|y'-y_0'|<\delta$ 的 $y\in D$ 都有 $J[y]\ge J[y_0]$（或 $\le$），则称 $J$ 在 $y_0$ 处取极小值（或极大值）。求泛函的极值称为变分问题，研究它的学科称为变分法（calculus of variations）。

**例 13.1.1（最短线）** 连接平面上两点 $(a,A)$、$(b,B)$ 的曲线 $y=y(x)$ 的长度为

$$
J[y]=\int_a^b\sqrt{1+y'^2}\,\mathrm{d}x.
$$

**例 13.1.2（最小旋转曲面）** 在上半平面给定两点 $A(a_1,b_1)$、$B(a_2,b_2)$，$a_1<a_2$，$b_1,b_2>0$。连接 $A,B$ 的光滑曲线 $y=y(x)>0$ 绕 $x$ 轴旋转一周，所得旋转曲面的面积为（[2.2.7](/2.2.7)）

$$
S[y]=2\pi\int_{a_1}^{a_2}y\sqrt{1+y'^2}\,\mathrm{d}x.\tag{13.2}
$$
问：什么曲线使面积最小？

**例 13.1.3（最速降线）** 给定不在同一铅垂线上的两点 $A,B$，$A$ 高于 $B$。质点在重力作用下从 $A$ 由静止出发，沿连接 $A,B$ 的光滑轨道无摩擦地滑到 $B$。什么轨道用时最短？这是 Johann Bernoulli 于 1696 年提出的问题，变分法由此诞生。

取 $A$ 为原点，$y$ 轴竖直向下，$B=(x_B,y_B)$，$x_B,y_B>0$。由能量守恒，质点下降高度 $y$ 时速率 $v=\sqrt{2gy}$；弧长元 $\mathrm{d}s=\sqrt{1+y'^2}\,\mathrm{d}x$，用时 $\mathrm{d}t=\mathrm{d}s/v$。于是总时间

$$
T[y]=\frac{1}{\sqrt{2g}}\int_0^{x_B}\frac{\sqrt{1+y'^2}}{\sqrt y}\,\mathrm{d}x,\tag{13.3}
$$
其中 $g$ 是重力加速度。

## 13.2. Euler–Lagrange 方程

### 13.2.1. 变分学基本引理

**引理 13.2.1（变分学基本引理）** 设 $f\in C[a,b]$。若对任意满足 $\eta(a)=\eta(b)=0$ 的 $\eta\in C^1[a,b]$ 都有

$$
\int_a^bf(x)\eta(x)\,\mathrm{d}x=0,
$$
则 $f\equiv0$ 于 $[a,b]$。

**证明** 若 $f(x_0)\ne0$，由连续性不妨设 $x_0\in(a,b)$，$f(x_0)>0$，并存在 $\delta>0$，使 $(x_0-\delta,x_0+\delta)\subset[a,b]$ 且 $f>0$ 于其上。取

$$
\eta(x)=\begin{cases}(x-x_0+\delta)^2(x_0+\delta-x)^2,&|x-x_0|<\delta,\\0,&\text{其他},\end{cases}
$$
则 $\eta\in C^1[a,b]$，$\eta(a)=\eta(b)=0$，$\eta>0$ 于 $(x_0-\delta,x_0+\delta)$，于是 $\int_a^bf\eta\,\mathrm{d}x=\int_{x_0-\delta}^{x_0+\delta}f\eta\,\mathrm{d}x>0$，矛盾。$\square$

引理的意思是：一个连续函数若与"所有"试验函数的积分都为零，它本身只能是零。把 $(\cdot)^2$ 换成更高的幂可以让 $\eta$ 任意阶光滑，所以试验函数类可以取得更小，结论不变。

### 13.2.2. 必要条件

**定理 13.2.1（Euler–Lagrange 方程）** 设 $F(x,y,p)$ 有连续的二阶偏导数，泛函 (13.1) 在 $y_0\in D$ 处取极值，且 $y_0\in C^2[a,b]$。则 $y_0$ 满足

$$
F_y\big(x,y,y'\big)-\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}\big(x,y,y'\big)=0.\tag{13.4}
$$
这里 $F_y$、$F_{y'}$ 表示 $F(x,y,p)$ 对第二、第三个变量的偏导数在 $p=y'(x)$ 处的值。

**证明** 任取 $\eta\in C^1[a,b]$，$\eta(a)=\eta(b)=0$，则对任意实数 $\varepsilon$，$y_0+\varepsilon\eta\in D$。一元函数 $\Phi(\varepsilon)=J[y_0+\varepsilon\eta]$ 在 $\varepsilon=0$ 处取极值，故 $\Phi'(0)=0$。由**积分号下求导**，

$$
\Phi'(0)=\int_a^b\big(F_y\eta+F_{y'}\eta'\big)\,\mathrm{d}x=0.
$$
对第二项分部积分，利用 $\eta(a)=\eta(b)=0$：

$$
\int_a^bF_{y'}\eta'\,\mathrm{d}x=\Big[F_{y'}\eta\Big]_a^b-\int_a^b\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}\,\eta\,\mathrm{d}x=-\int_a^b\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}\,\eta\,\mathrm{d}x,
$$
于是 $\int_a^b\big(F_y-\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}\big)\eta\,\mathrm{d}x=0$ 对一切这样的 $\eta$ 成立，由引理 13.2.1 得 (13.4)。$\square$

$\Phi'(0)$ 称为泛函 $J$ 在 $y_0$ 处沿 $\eta$ 的一阶变分（first variation），记作 $\delta J$；定理说的是"极值处一阶变分为零"，与"可微函数的极值点处导数为零"完全类似。方程 (13.4) 称为泛函 (13.1) 的 Euler–Lagrange 方程（Euler–Lagrange equation），它的解称为泛函的极值曲线（extremal）。注意它只是必要条件：极值曲线不一定使泛函取极值，正如驻点不一定是极值点。

展开 $\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}$，(13.4) 成为

$$
F_{y'y'}\,y''+F_{yy'}\,y'+F_{xy'}-F_y=0,
$$
当 $F_{y'y'}\ne0$ 时这是一个二阶常微分方程，通解含两个任意常数，由边界条件 $y(a)=A$、$y(b)=B$ 确定。所以变分问题化为二阶方程的两点边值问题（[2.4.12](/2.4.12#sec-12.4)）。

关于正则性有两点补充。其一，定理中假设 $y_0\in C^2$ 只是为了分部积分；若只设 $y_0\in C^1$，可以改为对第一项分部积分，用 du Bois-Reymond 引理得到积分形式 $F_{y'}=\int_a^xF_y\,\mathrm{d}t+C$，并进一步证明：若沿 $y_0$ 有 $F_{y'y'}\ne0$，则 $y_0$ 自动属于 $C^2$。其二，使泛函取极小值的必要条件还包括 Legendre 条件 $F_{y'y'}\big(x,y_0,y_0'\big)\ge0$；充分条件需要讨论二阶变分与 Jacobi 条件，这里不展开。

### 13.2.3. 可降阶的情形

Euler–Lagrange 方程一般是非线性的二阶方程，难以求解。以下几种情形可以降阶，它们对应 [2.4.7](/2.4.7) 中可降阶的方程类型。

1. $F$ 不含 $y'$：$F=F(x,y)$。(13.4) 成为 $F_y(x,y)=0$，这是一个函数方程而不是微分方程，一般不能满足边界条件，变分问题通常无解。
2. $F$ 不含 $y$：$F=F(x,y')$。(13.4) 成为 $\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}=0$，得首次积分 $F_{y'}(x,y')=C$，这是一个不含 $y$ 的一阶方程。
3. $F$ 不含 $x$：$F=F(y,y')$。此时有下面的 Beltrami 恒等式，得一阶方程 $F-y'F_{y'}=C$。
4. $F$ 只含 $y'$：$F=F(y')$。(13.4) 成为 $F_{y'y'}(y')\,y''=0$，所以 $y''=0$ 或 $y'$ 是方程 $F_{y'y'}(p)=0$ 的根（常数）；两种情况下极值曲线都是直线。

**定理 13.2.2（Beltrami 恒等式）** 若 $F=F(y,y')$ 不显含 $x$，则 $y\in C^2$ 满足 Euler–Lagrange 方程 (13.4) 时

$$
F(y,y')-y'F_{y'}(y,y')=C\tag{13.5}
$$
为常数。反之，满足 (13.5) 且 $y'\ne0$ 的 $C^2$ 函数是 (13.4) 的解。

**证明** 因为 $F$ 不含 $x$，$\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}=F_{yy'}y'+F_{y'y'}y''$。直接计算

$$
\frac{\mathrm{d}}{\mathrm{d}x}\big(F-y'F_{y'}\big)=F_yy'+F_{y'}y''-y''F_{y'}-y'\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}=y'\Big(F_y-\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}\Big).
$$
两个方向的结论都由此得出。$\square$

在力学中 $x$ 是时间，$F$ 不显含时间时 (13.5) 就是能量守恒（§13.4.1）；它是 Euler–Lagrange 方程的一个首次积分（[2.4.14](/2.4.14)）。

例 13.1.1 属于第 4 种情形，$F=\sqrt{1+y'^2}$，$F_{y'y'}=(1+y'^2)^{-3/2}>0$，故 $y''=0$：两点之间极值曲线是直线段。

## 13.3. 经典问题

### 13.3.1. 最小旋转曲面与悬链线

**例 13.3.1** 求例 13.1.2 中的极值曲线。

**解** $F=y\sqrt{1+y'^2}$ 不含 $x$，由 (13.5)，

$$
y\sqrt{1+y'^2}-\frac{yy'^2}{\sqrt{1+y'^2}}=\frac{y}{\sqrt{1+y'^2}}=C\quad(C>0).
$$
令 $y'=p$，则 $y=C\sqrt{1+p^2}$，$\mathrm{d}x=\frac{\mathrm{d}y}{p}=\frac{C\,\mathrm{d}p}{\sqrt{1+p^2}}$，积分得 $x=C\ln\big(p+\sqrt{1+p^2}\big)+C'$。令 $t=\ln\big(p+\sqrt{1+p^2}\big)$，即 $p=\sinh t$，则 $\sqrt{1+p^2}=\cosh t$，曲线的参数方程为 $x=Ct+C'$，$y=C\cosh t$。消去 $t$：

$$
y=C\cosh\frac{x-C'}{C}.\tag{13.6}
$$
这是悬链线（catenary），常数 $C,C'$ 由 $A,B$ 确定；它绕 $x$ 轴旋转所得的曲面称为悬链面（catenoid）。

两个常数由非线性方程确定，解的个数取决于端点。以对称端点 $(\pm a,h)$ 为例：由对称性 $C'=0$，条件为 $C\cosh\frac aC=h$。令 $s=a/C$，即 $\frac{\cosh s}{s}=\frac ha$。函数 $\frac{\cosh s}{s}$ 在 $s>0$ 上的最小值约为 $1.5089$（在 $s\tanh s=1$，$s\approx1.1997$ 处取得），因此：

- $h/a>1.5089$ 时有两条悬链线，其中较"平"的（$C$ 较大）给出面积的局部极小，较深的一条不是极小；
- $h/a=1.5089$ 时恰有一条；
- $h/a<1.5089$ 时没有悬链线连接两端，此时面积的下确界由两个端点圆盘加上 $x$ 轴上的线段（Goldschmidt 解）给出，它不是光滑曲线，不在容许函数类中。

这说明 Euler–Lagrange 方程的边值问题可能有多解或无解，变分问题的解也不一定存在于预先设定的函数类中。肥皂膜实验可以直观地看到这一现象：两个圆环拉开到一定距离时，悬链面形状的肥皂膜会突然破裂成两张圆盘。

![连接 (-1, h) 与 (1, h) 的悬链线：h 大于临界值时有两条，等于临界值时一条，小于时没有](./plots/catenary-solutions.py)

### 13.3.2. 最速降线与旋轮线

**例 13.3.2** 求例 13.1.3 的极值曲线。

**解** $F=\frac{\sqrt{1+y'^2}}{\sqrt y}$ 不含 $x$（常数因子 $1/\sqrt{2g}$ 不影响极值曲线）。由 (13.5)，

$$
\frac{\sqrt{1+y'^2}}{\sqrt y}-\frac{y'^2}{\sqrt{y(1+y'^2)}}=\frac{1}{\sqrt{y(1+y'^2)}}=C_1,
$$
即 $y(1+y'^2)=C$，$C=1/C_1^2>0$。令 $y'=\cot t$，则

$$
y=\frac{C}{1+\cot^2t}=C\sin^2t=\frac C2(1-\cos2t),\qquad\mathrm{d}x=\frac{\mathrm{d}y}{y'}=\frac{2C\sin t\cos t\,\mathrm{d}t}{\cot t}=C(1-\cos2t)\,\mathrm{d}t,
$$
积分得 $x=\frac C2(2t-\sin2t)+C'$。由 $A$ 为原点得 $C'=0$；记 $\theta=2t$，$R=C/2$：

$$
x=R(\theta-\sin\theta),\qquad y=R(1-\cos\theta).\tag{13.7}
$$
这是半径为 $R$ 的圆沿 $x$ 轴（在其下方）滚动时圆周上一点的轨迹，称为旋轮线（cycloid），又称摆线；$R$ 由 $B$ 点确定（方程 $\frac{\theta-\sin\theta}{1-\cos\theta}=\frac{x_B}{y_B}$ 对 $\theta\in(0,2\pi)$ 有唯一解）。

沿旋轮线 (13.7) 从 $A$ 滑到参数 $\theta_B$ 处所需时间为 $T=\theta_B\sqrt{R/g}$。直线虽然最短，但开始时太平缓，速度增加慢；旋轮线先陡后缓，用较短的距离换来较大的速度。下图以 $B=(\pi,2)$（$R=1$，$\theta_B=\pi$）为例比较三条轨道的用时。旋轮线还有等时性：从旋轮线上任一点由静止释放，到达最低点的时间都是 $\pi\sqrt{R/g}$，与出发点无关。

![从 A = (0, 0) 到 B = (π, 2) 的三条轨道（y 轴向下）：旋轮线、直线与圆弧，图例给出 g = 1 时的下滑时间](./plots/brachistochrone.py)

### 13.3.3. 球面测地线

**例 13.3.3** 求球面上连接两点的最短曲线。

**解** 在半径为 $R$ 的球面上用球坐标 $x=R\sin\theta\cos\varphi$，$y=R\sin\theta\sin\varphi$，$z=R\cos\theta$，$\theta\in[0,\pi]$，$\varphi\in[0,2\pi)$。设曲线为 $\varphi=\varphi(\theta)$，则

$$
\mathrm{d}x^2+\mathrm{d}y^2+\mathrm{d}z^2=R^2\big(1+\varphi'^2\sin^2\theta\big)\,\mathrm{d}\theta^2,\qquad J[\varphi]=R\int_{\theta_1}^{\theta_2}\sqrt{1+\varphi'^2\sin^2\theta}\,\mathrm{d}\theta.
$$
被积函数不含 $\varphi$（情形 2），故

$$
F_{\varphi'}=\frac{R\,\varphi'\sin^2\theta}{\sqrt{1+\varphi'^2\sin^2\theta}}=RC.
$$
由球面的对称性，可以选取坐标使起点 $A$ 是北极 $\theta=0$。由于对任意实数 $u$ 都有 $\Big|\dfrac{u\sin^2\theta}{\sqrt{1+u^2\sin^2\theta}}\Big|\le|\sin\theta|$，令 $\theta\to0^+$ 得 $C=0$，从而 $\varphi'\equiv0$，$\varphi=\varphi_0$ 为常数：曲线是经线 $x=R\sin\theta\cos\varphi_0$，$y=R\sin\theta\sin\varphi_0$，$z=R\cos\theta$，即过 $A$、$B$ 和球心的平面与球面的交线——大圆的一段。若不把 $A$ 取为极点，$C$ 一般不为零，得到的仍是大圆，只是方程较复杂。

这样的"局部最短线"称为测地线（geodesic）。航空公司的远程航线沿大圆飞行，在墨卡托地图上看起来是弯曲的，原因就在这里。

## 13.4. 推广

### 13.4.1. 多个未知函数与 Hamilton 原理

设泛函依赖于 $n$ 个未知函数 $y_1,\dots,y_n$：

$$
J[y_1,\dots,y_n]=\int_a^bF\big(x,y_1,\dots,y_n,y_1',\dots,y_n'\big)\,\mathrm{d}x,
$$
两端的值都给定。每次只对一个函数作变分 $y_i+\varepsilon\eta_i$，其余不动，由定理 13.2.1 的证明得到 Euler–Lagrange 方程组

$$
F_{y_i}-\frac{\mathrm{d}}{\mathrm{d}x}F_{y_i'}=0,\qquad i=1,\dots,n.\tag{13.8}
$$
空间曲线的变分问题（如曲面上的测地线、空间中的最速降线）都属于这一类。

力学中最重要的例子是 Hamilton 原理：设力学系统的广义坐标为 $q_1,\dots,q_n$，动能为 $T$，势能为 $V$，Lagrange 量 $\mathcal{L}=T-V$。系统的真实运动使作用量 $\int_{t_1}^{t_2}\mathcal{L}(t,q,\dot q)\,\mathrm{d}t$ 取驻值，由 (13.8) 得 Lagrange 方程

$$
\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial\mathcal{L}}{\partial\dot q_i}-\frac{\partial\mathcal{L}}{\partial q_i}=0,\qquad i=1,\dots,n.
$$
例如长为 $l$ 的单摆，$q=\theta$，$\mathcal{L}=\frac12ml^2\dot\theta^2+mgl\cos\theta$，Lagrange 方程为 $ml^2\ddot\theta+mgl\sin\theta=0$，即 $\ddot\theta+\frac gl\sin\theta=0$。$\mathcal{L}$ 不显含 $t$ 时，Beltrami 恒等式的推广 $\sum_i\dot q_i\frac{\partial\mathcal{L}}{\partial\dot q_i}-\mathcal{L}=$ 常数，就是 $T+V=$ 常数（对动能是 $\dot q$ 的二次型的系统），即机械能守恒。

### 13.4.2. 等周问题

**例 13.4.1（Dido 问题）** 在所有长为 $l$、两端位于 $x$ 轴上的曲线中，哪一条与 $x$ 轴围成的面积最大？这要在约束

$$
K[y]=\int_a^b\sqrt{1+y'^2}\,\mathrm{d}x=l
$$
下求 $J[y]=\int_a^by\,\mathrm{d}x$ 的极大值。这类以另一个积分泛函为约束的变分问题称为等周问题（isoperimetric problem）。

**定理 13.4.1** 设 $F,G$ 有连续的二阶偏导数，$y_0\in C^2$ 在约束 $K[y]=\int_a^bG(x,y,y')\,\mathrm{d}x=l$ 与边界条件 $y(a)=A$、$y(b)=B$ 下使 $J[y]=\int_a^bF(x,y,y')\,\mathrm{d}x$ 取极值，且 $y_0$ 不是 $K$ 的极值曲线。则存在常数 $\lambda$，使 $y_0$ 是泛函

$$
\int_a^b\big(F+\lambda G\big)\,\mathrm{d}x
$$
的极值曲线，即满足 $(F+\lambda G)_y-\frac{\mathrm{d}}{\mathrm{d}x}(F+\lambda G)_{y'}=0$。

证明的思路：取两个试验函数作两参数变分 $y_0+\varepsilon_1\eta_1+\varepsilon_2\eta_2$，则 $(\varepsilon_1,\varepsilon_2)=(0,0)$ 是二元函数 $J$ 在约束 $K=l$ 下的条件极值点，由二元函数的 Lagrange 乘子法（[2.2.11](/2.2.11#sec-11.6)）得到乘子；"$y_0$ 不是 $K$ 的极值曲线"保证了约束的梯度不为零，并且乘子与试验函数的选取无关。通解中含两个积分常数与乘子 $\lambda$，由两个边界条件和约束确定。

**解**（例 13.4.1）$F+\lambda G=y+\lambda\sqrt{1+y'^2}$ 不含 $x$，由 (13.5)，

$$
y+\lambda\sqrt{1+y'^2}-\frac{\lambda y'^2}{\sqrt{1+y'^2}}=y+\frac{\lambda}{\sqrt{1+y'^2}}=c_2,
$$
即 $(y-c_2)^2(1+y'^2)=\lambda^2$。令 $y'=\tan t$，得 $y-c_2=\lambda\cos t$，$\mathrm{d}x=\frac{\mathrm{d}y}{y'}=-\lambda\cos t\,\mathrm{d}t$，$x-c_1=-\lambda\sin t$，于是

$$
(x-c_1)^2+(y-c_2)^2=\lambda^2:
$$
极值曲线是圆弧。这是等周定理（周长一定的闭曲线中圆所围面积最大）的一个变分形式。

**例 13.4.2（悬链线）** 长为 $l$、线密度均匀的柔软绳索两端固定，在重力下静止时的形状使势能 $\int_a^b\rho gy\sqrt{1+y'^2}\,\mathrm{d}x$ 最小，约束是 $\int_a^b\sqrt{1+y'^2}\,\mathrm{d}x=l$。由定理 13.4.1，$F+\lambda G=(y+\lambda)\sqrt{1+y'^2}$（已把 $\rho g$ 并入 $\lambda$ 的尺度），令 $Y=y+\lambda$，与例 13.3.1 完全相同，得

$$
y+\lambda=c\cosh\frac{x-c'}{c}.
$$
悬挂的绳索与最小旋转曲面的母线是同一种曲线，"悬链线"之名即由此而来。

## 小结

| 问题 | 被积函数 $F$ | 降阶方式 | 极值曲线 |
|---|---|---|---|
| 最短线 | $\sqrt{1+y'^2}$ | 只含 $y'$ | 直线 |
| 最小旋转曲面 | $y\sqrt{1+y'^2}$ | 不含 $x$：$\frac{y}{\sqrt{1+y'^2}}=C$ | 悬链线 $y=C\cosh\frac{x-C'}{C}$ |
| 最速降线 | $\frac{\sqrt{1+y'^2}}{\sqrt y}$ | 不含 $x$：$y(1+y'^2)=C$ | 旋轮线 $x=R(\theta-\sin\theta)$，$y=R(1-\cos\theta)$ |
| 球面测地线 | $\sqrt{1+\varphi'^2\sin^2\theta}$ | 不含 $\varphi$：$F_{\varphi'}=C$ | 大圆 |
| 等周问题 | $y+\lambda\sqrt{1+y'^2}$ | 乘子 + 不含 $x$ | 圆弧 |
| 悬挂的绳索 | $(y+\lambda)\sqrt{1+y'^2}$ | 乘子 + 不含 $x$ | 悬链线 |

变分法的基本路线是：极值 ⟹ 一阶变分为零 ⟹（变分学基本引理）Euler–Lagrange 方程 ⟹ 二阶方程的边值问题。被积函数不含 $x$ 时，Beltrami 恒等式把它降为一阶方程；有积分约束时，先用 Lagrange 乘子把约束并入被积函数。
