---
title: 一阶微分方程
---

许多几何与物理问题给出的不是未知函数本身，而是它与导数之间的关系：曲线每点的切线斜率、物体的速度与加速度、种群的增长率。这样的关系式就是微分方程，求出满足它的函数就是"解微分方程"。一元积分学（[2.2.6](/2.2.6)、[2.2.7](/2.2.7)）求原函数，相当于解最简单的方程 $y'=f(x)$；本章把这件事推广到未知函数也出现在等式右边的情形。

本章先建立基本概念（解、通解、初值问题、积分曲线）并叙述解的存在唯一性定理，然后介绍几类能用初等积分法求出解析解的一阶方程：变量分离方程及可化为它的方程、一阶线性方程与 Bernoulli 方程、全微分方程与积分因子，最后是几类可以降阶为一阶方程的高阶方程。求解的共同思路是变量代换：把方程化为已经会解的类型。全微分方程用到 [2.2.10](/2.2.10) 中微分形式的原函数与 [2.2.14](/2.2.14) 的保守场。[下一章](/2.2.16)讨论高阶线性方程与线性方程组，那里线性代数的语言将起主要作用。常微分方程的一般理论（解的延拓、对初值的依赖性、稳定性等）留给 [2.4](/2.4)；生物学中的常微分方程模型见[系统生物学](/7.9)。

## 15.1. 微分方程的基本概念

### 15.1.1. 引例

**例 15.1.1** 求过点 $(0,1)$、每点切线斜率等于该点横坐标的曲线。设曲线为 $y=y(x)$，则 $y'=x$，积分得 $y=\dfrac{x^2}{2}+C$；由 $y(0)=1$ 得 $C=1$，所求曲线为 $y=\dfrac{x^2}{2}+1$。

**例 15.1.2（自由落体）** 设物体下落的距离为 $s(t)$，则 $s''(t)=g$。积分两次得 $s=\dfrac12gt^2+C_1t+C_2$。若 $t=0$ 时速度为 $v_0$、距离为 $s_0$，则 $C_1=v_0$，$C_2=s_0$，$s=\dfrac12gt^2+v_0t+s_0$。

**例 15.1.3（悬链线）** 两端固定的均匀柔软绳索在重力下自然下垂，求它的形状。取绳索最低点为原点，设绳索的线密度为 $\rho$，曲线为 $y=y(x)$。考察最低点到点 $(x,y)$ 的一段：它受最低点处的水平张力 $H$、端点处沿切线方向的张力 $T$ 与重力 $\rho g l$（$l$ 为这段的弧长）作用。设切线倾角为 $\theta$，平衡条件为 $T\cos\theta=H$，$T\sin\theta=\rho gl$，所以

$$
y'=\tan\theta=\frac{\rho g}{H}\int_0^x\sqrt{1+y'(s)^2}\,\mathrm{d}s.
$$

两边求导，记 $a=\rho g/H$，得 $y''=a\sqrt{1+y'^2}$，并且 $y(0)=0$，$y'(0)=0$。这是一个含二阶导数的方程，例 15.5.4 将解出 $y=\dfrac{\cosh ax-1}{a}$。

前两例只需要积分，第三例中未知函数的导数之间互相牵连，需要新的方法。

### 15.1.2. 基本概念

**定义 15.1.1** 含有未知函数及其导数的方程称为**微分方程**。未知函数是一元函数的微分方程称为**常微分方程**，未知函数是多元函数、方程中出现偏导数的称为**偏微分方程**。方程中未知函数的导数的最高阶数称为方程的阶。

$n$ 阶常微分方程的一般形式是 $F(x,y,y',\dots,y^{(n)})=0$。例如 $(y')^2+ay+b=0$ 是一阶方程，$y''+ay+b=0$ 是二阶方程；悬链线方程是二阶方程。以下"微分方程"均指常微分方程。

**定义 15.1.2** 若方程关于未知函数及其各阶导数都是一次的，即形如

$$
a_0(x)y^{(n)}+a_1(x)y^{(n-1)}+\cdots+a_{n-1}(x)y'+a_n(x)y=f(x),
$$
则称为 $n$ 阶**线性微分方程**；否则称为非线性微分方程。

线性方程的系数可以是 $x$ 的任意函数，"线性"只是对未知函数而言。悬链线方程 $y''=a\sqrt{1+y'^2}$ 是非线性的。

**定义 15.1.3** 设函数 $\varphi(x)$ 在区间 $I$ 上有 $n$ 阶导数，且 $F(x,\varphi(x),\varphi'(x),\dots,\varphi^{(n)}(x))=0$ 对所有 $x\in I$ 成立，则称 $y=\varphi(x)$ 是方程在 $I$ 上的一个解。$n$ 阶方程的含有 $n$ 个相互独立的任意常数的解称为它的**通解**；不含任意常数的解称为**特解**。确定通解中常数的条件称为定解条件。

"相互独立"指这些常数不能合并成更少的常数，例如 $C_1\mathrm{e}^{x+C_2}=C\mathrm{e}^x$ 实际只含一个常数。通解是一族解，但不一定包含方程的全部解，见例 15.2.1。

**定义 15.1.4** 方程连同条件 $y(x_0)=y_0$，$y'(x_0)=y_1$，…，$y^{(n-1)}(x_0)=y_{n-1}$ 称为**初值问题**（又称 Cauchy 问题），这些条件称为初始条件。一阶方程的初值问题记作

$$
\begin{cases}y'=f(x,y),\\ y(x_0)=y_0.\end{cases}
$$
定解条件也可以给在区间的两个端点，例如 $F(x,y,y',y'')=0$，$y(a)=A$，$y(b)=B$，称为边值问题。

**定义 15.1.5** 微分方程的解 $y=\varphi(x)$ 的图形称为方程的**积分曲线**；通解的图形是一族曲线，称为积分曲线族。

例如 $y'=2x$ 的积分曲线族是抛物线族 $y=x^2+C$；$y'=-\dfrac{x}{y}$ 即 $x\,\mathrm{d}x+y\,\mathrm{d}y=0$ 的积分曲线族是同心圆 $x^2+y^2=R^2$。

方程 $y'=f(x,y)$ 有直观的几何意义：它在区域内每一点 $(x,y)$ 指定了一个斜率 $f(x,y)$。在每点画一条以 $f(x,y)$ 为斜率的短线段，得到方程的方向场（direction field）；积分曲线就是处处与方向场相切的曲线。即使解不出方程，也可以从方向场看出解的大致走向。

![方程 y' = x - y 的方向场（短线段）与几条积分曲线 y = x - 1 + C e^{-x}；所有积分曲线都随 x 增大趋近于直线 y = x - 1（C = 0 的解）](./plots/direction-field.py)

### 15.1.3. 解的存在唯一性

求解之前先要问：解是否存在？过一点的解是否唯一？

**定义 15.1.6（Lipschitz 条件）** 设 $f(x,y)$ 在区域 $D$ 上有定义。若存在常数 $L>0$，使对 $D$ 中任意两点 $(x,y_1)$、$(x,y_2)$ 都有

$$
\lvert f(x,y_1)-f(x,y_2)\rvert\le L\lvert y_1-y_2\rvert,
$$
则称 $f$ 在 $D$ 上关于 $y$ 满足 **Lipschitz 条件**，$L$ 称为 Lipschitz 常数。

若 $f_y$ 在凸区域（例如矩形）$D$ 上连续且有界，由 Lagrange 中值定理 $f(x,y_1)-f(x,y_2)=f_y(x,\xi)(y_1-y_2)$，$f$ 关于 $y$ 满足 Lipschitz 条件。所以这个条件对常见的光滑函数总是成立的，例外出现在 $f_y$ 无界的地方。

**定理 15.1.1（存在唯一性定理）** 设 $f(x,y)$ 在矩形 $D=\{(x,y)\mid\lvert x-x_0\rvert\le a,\ \lvert y-y_0\rvert\le b\}$ 上连续，且关于 $y$ 满足 Lipschitz 条件。记 $M=\max_D\lvert f(x,y)\rvert$，$h=\min\{a,b/M\}$，则初值问题 $y'=f(x,y)$，$y(x_0)=y_0$ 在区间 $[x_0-h,x_0+h]$ 上有且只有一个解。

本课程不证明这个定理，证明（Picard 逐次逼近）见 [2.4.4](/2.4.4)。$h$ 的取法保证积分曲线在 $\lvert x-x_0\rvert\le h$ 内不会离开矩形：斜率不超过 $M$，走过水平距离 $h$ 时竖直方向至多变化 $Mh\le b$。几何上，定理说的是：满足条件的区域内，过每一点恰有一条积分曲线，不同的积分曲线互不相交。

**例 15.1.4** 设 $p(x)$ 在区间 $I$ 上连续，则方程 $y'=p(x)y$ 的积分曲线若与 $x$ 轴相交，则必与 $x$ 轴重合。

**证明** $f(x,y)=p(x)y$ 满足 $\lvert f(x,y_1)-f(x,y_2)\rvert=\lvert p(x)\rvert\lvert y_1-y_2\rvert$，在 $I$ 的任一有界闭子区间上 $\lvert p\rvert$ 有界，Lipschitz 条件成立。设积分曲线 $y=\varphi(x)$ 与 $x$ 轴交于 $x_0$，即 $\varphi(x_0)=0$。而 $y\equiv0$ 也是满足 $y(x_0)=0$ 的解，由唯一性，$\varphi\equiv0$。 $\square$

所以 $y'=p(x)y$ 的非零解永不为零，保持定号。Lipschitz 条件不满足时，唯一性可能失去。

**例 15.1.5** 初值问题 $y'=3y^{2/3}$，$y(0)=0$ 有无穷多个解。$y\equiv0$ 是解；当 $y\ne0$ 时分离变量 $\dfrac{\mathrm{d}y}{3y^{2/3}}=\mathrm{d}x$，得 $y^{1/3}=x-c$，即 $y=(x-c)^3$。对任意 $c\ge0$，

$$
y=\begin{cases}0,&x<c,\\(x-c)^3,&x\ge c\end{cases}
$$
在 $\mathbb{R}$ 上可导、满足方程且 $y(0)=0$。原因是 $f(y)=3y^{2/3}$ 在 $y=0$ 附近 $\dfrac{\lvert f(y)-f(0)\rvert}{\lvert y\rvert}=3\lvert y\rvert^{-1/3}$ 无界，不满足 Lipschitz 条件：积分曲线可以沿 $x$ 轴走任意一段，再在任意时刻"离开"。

![初值问题 y' = 3y^{2/3}, y(0) = 0 的几个解：沿 x 轴走到 x = c 后分出立方曲线 (x - c)^3；c 取遍非负实数，解有无穷多个](./plots/nonuniqueness.py)

对一阶线性方程 $y'+p(x)y=q(x)$，只要 $p,q$ 在区间 $I$ 上连续，初值问题的解就在整个 $I$ 上存在且唯一（定理 15.3.1 的公式直接给出了它）。

## 15.2. 变量分离方程及可化为变量分离的方程

### 15.2.1. 变量分离方程

**定义 15.2.1** 形如 $y'=f(x)g(y)$，或写成对称形式 $M_1(x)N_1(y)\,\mathrm{d}x+M_2(x)N_2(y)\,\mathrm{d}y=0$ 的方程称为**变量分离方程**。

**算法 15.2.1（分离变量法）** 求解 $y'=f(x)g(y)$：

1. 当 $g(y)\ne0$ 时，把方程写成 $\dfrac{\mathrm{d}y}{g(y)}=f(x)\,\mathrm{d}x$，两边积分：$\displaystyle\int\frac{\mathrm{d}y}{g(y)}=\int f(x)\,\mathrm{d}x+C$，这里两个不定积分各取一个原函数；
2. 若 $g(c)=0$，则常函数 $y=c$ 也是解，检查它是否已包含在第 1 步的通解中，不包含时要单独列出。

第 1 步得到的往往是隐式解 $G(y)=F(x)+C$，能解出 $y$ 时再化成显式。

**例 15.2.1** 解 $y'=y^2$。$y\ne0$ 时 $-\dfrac1y=x+C$，即 $y=-\dfrac{1}{x+C}$；$y=0$ 也是解，但它不能由任何 $C$ 得到。所以这个方程的通解没有包含全部解，$y=0$ 要另外写出。与之对照，$y'=-2xy$ 分离变量得 $\ln\lvert y\rvert=-x^2+C_1$，即 $y=\pm\mathrm{e}^{C_1}\mathrm{e}^{-x^2}$；把 $y=0$ 也并进来，通解为 $y=C\mathrm{e}^{-x^2}$，$C$ 为任意实数，此时通解包含了全部解（这与例 15.1.4 一致）。

**例 15.2.2** 解 $(x+1)^2y\,\mathrm{d}x+x^2(y-1)\,\mathrm{d}y=0$。两边除以 $x^2y$：

$$
\Big(1+\frac2x+\frac1{x^2}\Big)\mathrm{d}x=-\Big(1-\frac1y\Big)\mathrm{d}y,
$$
积分得 $x+2\ln\lvert x\rvert-\dfrac1x+y-\ln\lvert y\rvert=C$。另有解 $y=0$ 与 $x=0$（把 $x$ 看作 $y$ 的函数）。

**例 15.2.3** 曲线 $C$ 在两坐标轴之间的任一切线段都被切点平分，求 $C$。设切点为 $(x,y)$，切线与 $x$ 轴交于 $(2x,0)$，所以斜率 $y'=\dfrac{0-y}{2x-x}=-\dfrac yx$。分离变量得 $\ln\lvert y\rvert=-\ln\lvert x\rvert+C$，即 $xy=K$（$K\ne0$）：所求曲线是等轴双曲线。

**例 15.2.4（Logistic 方程）** 种群数量 $P(t)$ 的增长率与当前数量成正比、又受环境容纳量 $K$ 限制时，满足

$$
\frac{\mathrm{d}P}{\mathrm{d}t}=kP\Big(1-\frac PK\Big),\qquad k>0.
$$
这是变量分离方程，常数解 $P=0$ 与 $P=K$ 是两个平衡态。$0<P<K$ 时，$\dfrac{K\,\mathrm{d}P}{P(K-P)}=\Big(\dfrac1P+\dfrac1{K-P}\Big)\mathrm{d}P=k\,\mathrm{d}t$，积分得 $\ln\dfrac{P}{K-P}=kt+C$，所以

$$
P(t)=\frac{K}{1+A\mathrm{e}^{-kt}},\qquad A=\frac{K-P_0}{P_0},
$$
其中 $P_0=P(0)$；这个公式对 $P_0>K$ 同样成立。无论初值如何（$P_0>0$），$t\to+\infty$ 时 $P(t)\to K$。$0<P_0<K/2$ 时曲线呈 S 形，拐点在 $P=K/2$ 处，此时增长最快。这就是生物学中的逻辑斯谛增长（logistic growth），其建模见[生态学](/7.19)。

![Logistic 方程 P' = kP(1 - P/K)（k = 1, K = 1）的方向场与解曲线：P = 0 与 P = K 是平衡解，其余正解都单调趋于 K；从 P_0 < K/2 出发的解呈 S 形，在 P = K/2 处增长最快](./plots/logistic.py)

### 15.2.2. 齐次型方程

**定义 15.2.2** 形如 $y'=f\!\left(\dfrac yx\right)$ 的方程称为**齐次型方程**。

这里的"齐次"指右端是 $x,y$ 的零次**齐次函数**（[2.2.10](/2.2.10)）：若 $M,N$ 是同次齐次函数，$M\,\mathrm{d}x+N\,\mathrm{d}y=0$ 就是齐次型方程。它与下一章的"齐次线性方程"不是一回事。

**算法 15.2.2** 令 $u=\dfrac yx$，即 $y=xu$，则 $y'=u+xu'$，方程化为变量分离方程

$$
x\frac{\mathrm{d}u}{\mathrm{d}x}=f(u)-u,\qquad\frac{\mathrm{d}u}{f(u)-u}=\frac{\mathrm{d}x}{x}.
$$
解出 $u$ 后以 $u=y/x$ 代回；$f(u_0)=u_0$ 的根给出解 $y=u_0x$。

**例 15.2.5** 求解下列各题。（1）解 $y'=\dfrac yx+\tan\dfrac yx$。令 $y=xu$，$xu'=\tan u$，$\dfrac{\cos u}{\sin u}\mathrm{d}u=\dfrac{\mathrm{d}x}{x}$，得 $\ln\lvert\sin u\rvert=\ln\lvert x\rvert+\ln\lvert C\rvert$，通解 $\sin\dfrac yx=Cx$（$C=0$ 对应 $u=k\pi$ 的解 $y=k\pi x$）。

（2）解 $xy'-y=\sqrt{x^2-y^2}$（$x>0$）。方程化为 $y'=\dfrac yx+\sqrt{1-(y/x)^2}$，令 $y=xu$ 得 $xu'=\sqrt{1-u^2}$，$\dfrac{\mathrm{d}u}{\sqrt{1-u^2}}=\dfrac{\mathrm{d}x}{x}$，通解 $\arcsin\dfrac yx=\ln x+C$；另有解 $y=\pm x$（$u=\pm1$）。

### 15.2.3. 可化为变量分离的方程

类型（1）：$y'=f(ax+by+c)$（$b\ne0$）。令 $u=ax+by+c$，则 $u'=a+bf(u)$，是变量分离方程。

**例 15.2.6** 解 $y'=(2x+y+3)^2$。令 $u=2x+y+3$，$u'=2+u^2$，$\dfrac{\mathrm{d}u}{2+u^2}=\mathrm{d}x$，$\dfrac{1}{\sqrt2}\arctan\dfrac{u}{\sqrt2}=x+C$，所以通解为 $2x+y+3=\sqrt2\tan(\sqrt2x+C)$。

类型（2）：$y'=f\!\left(\dfrac{a_1x+b_1y+c_1}{a_2x+b_2y+c_2}\right)$。分三种情形：

- $c_1=c_2=0$：右端是 $y/x$ 的函数，为齐次型方程。
- $\begin{vmatrix}a_1&b_1\\a_2&b_2\end{vmatrix}\ne0$：直线 $a_ix+b_iy+c_i=0$（$i=1,2$）交于一点 $(x_0,y_0)$。平移坐标 $X=x-x_0$，$Y=y-y_0$，则 $a_ix+b_iy+c_i=a_iX+b_iY$，方程化为齐次型方程 $\dfrac{\mathrm{d}Y}{\mathrm{d}X}=f\!\left(\dfrac{a_1X+b_1Y}{a_2X+b_2Y}\right)$。
- $\begin{vmatrix}a_1&b_1\\a_2&b_2\end{vmatrix}=0$：$a_2x+b_2y$ 与 $a_1x+b_1y$ 成比例，右端是 $a_1x+b_1y$ 的函数，属于情形（1）。

**例 15.2.7** 解 $y'=\dfrac{2x-5y+3}{2x+4y-6}$。由 $2x_0-5y_0+3=0$，$2x_0+4y_0-6=0$ 得 $x_0=y_0=1$。令 $X=x-1$，$Y=y-1$，得 $\dfrac{\mathrm{d}Y}{\mathrm{d}X}=\dfrac{2-5w}{2+4w}$，$w=\dfrac YX$。再令 $Y=Xw$：

$$
X\frac{\mathrm{d}w}{\mathrm{d}X}=\frac{2-5w}{2+4w}-w=\frac{2-7w-4w^2}{2+4w}=-\frac{(4w-1)(w+2)}{2+4w},
$$

于是

$$
\frac{(2+4w)\,\mathrm{d}w}{(4w-1)(w+2)}=-\frac{\mathrm{d}X}{X},\qquad\frac{2+4w}{(4w-1)(w+2)}=\frac{1}{3}\cdot\frac{4}{4w-1}+\frac{2}{3}\cdot\frac{1}{w+2}.
$$
积分得 $\dfrac13\ln\lvert4w-1\rvert+\dfrac23\ln\lvert w+2\rvert=-\ln\lvert X\rvert+C$，即 $(4w-1)(w+2)^2X^3=C$，代回 $w=Y/X$ 得 $(4Y-X)(Y+2X)^2=C$。所以通解为

$$
(x-4y+3)(2x+y-3)^2=C.
$$

类型（3）：$yf(xy)\,\mathrm{d}x+xg(xy)\,\mathrm{d}y=0$。令 $z=xy$，则 $y=\dfrac zx$，$x\,\mathrm{d}y=\mathrm{d}z-\dfrac zx\,\mathrm{d}x$，代入得 $\dfrac zxf(z)\,\mathrm{d}x+g(z)\Big(\mathrm{d}z-\dfrac zx\mathrm{d}x\Big)=0$，即

$$
\frac{\mathrm{d}x}{x}=\frac{g(z)\,\mathrm{d}z}{z\big(g(z)-f(z)\big)}.
$$

**例 15.2.8** 解 $y(xy+1)\,\mathrm{d}x+x(1+xy+x^2y^2)\,\mathrm{d}y=0$。这里 $f(z)=z+1$，$g(z)=1+z+z^2$，$g-f=z^2$，所以

$$
\frac{\mathrm{d}x}{x}=\frac{(1+z+z^2)\,\mathrm{d}z}{z^3}=\Big(\frac1{z^3}+\frac1{z^2}+\frac1z\Big)\mathrm{d}z,
$$
积分得 $\ln\lvert x\rvert=-\dfrac1{2z^2}-\dfrac1z+\ln\lvert z\rvert+C$。代回 $z=xy$ 并利用 $\ln\lvert z\rvert-\ln\lvert x\rvert=\ln\lvert y\rvert$，通解为

$$
\ln\lvert y\rvert-\frac{1}{2x^2y^2}-\frac1{xy}=C.
$$

## 15.3. 一阶线性方程与 Bernoulli 方程

### 15.3.1. 解的结构

一阶线性方程的标准形式是

$$
y'+p(x)y=q(x),\tag{15.1}
$$
$q(x)$ 称为非齐次项（自由项）。$q\equiv0$ 时

$$
y'+p(x)y=0\tag{15.2}
$$
称为式 (15.1) 对应的齐次线性方程；$q\not\equiv0$ 时式 (15.1) 称为非齐次线性方程。

**命题 15.3.1** 设 $p,q$ 在区间 $I$ 上连续。

1. 若 $y_1,y_2$ 是式 (15.2) 的解，则对任意常数 $\alpha,\beta$，$\alpha y_1+\beta y_2$ 也是式 (15.2) 的解；
2. 若 $y_1$ 是式 (15.2) 的解，$y^*$ 是式 (15.1) 的解，则 $y_1+y^*$ 是式 (15.1) 的解；式 (15.1) 的两个解之差是式 (15.2) 的解。

**证明** 记 $L(y)=y'+p(x)y$，则 $L(\alpha y_1+\beta y_2)=\alpha L(y_1)+\beta L(y_2)$，即 $L$ 是线性映射。两条结论都由此直接得到。 $\square$

因此，式 (15.1) 的通解 = 式 (15.1) 的一个特解 + 式 (15.2) 的通解。这与线性方程组 $A\boldsymbol{x}=\boldsymbol{b}$ 的解的结构（[2.1.3](/2.1.3)）完全相同，[下一章](/2.2.16)将把它推广到 $n$ 阶。

齐次方程 (15.2) 是变量分离方程：$\dfrac{\mathrm{d}y}{y}=-p(x)\,\mathrm{d}x$，得 $\ln\lvert y\rvert=-\int p(x)\,\mathrm{d}x+C_1$；连同解 $y=0$，通解为

$$
y=C\mathrm{e}^{-\int p(x)\,\mathrm{d}x},\qquad C\in\mathbb{R}.
$$
这里 $\int p(x)\,\mathrm{d}x$ 表示 $p$ 的一个原函数。

### 15.3.2. 常数变易法

把齐次通解中的常数 $C$ 换成待定函数 $C(x)$，代入非齐次方程，是求非齐次方程特解的一般方法，称为**常数变易法**。

**定理 15.3.1** 设 $p,q$ 在区间 $I$ 上连续，则式 (15.1) 的通解为

$$
y=\mathrm{e}^{-\int p(x)\,\mathrm{d}x}\Big(\int q(x)\mathrm{e}^{\int p(x)\,\mathrm{d}x}\,\mathrm{d}x+C\Big).\tag{15.3}
$$
满足 $y(x_0)=y_0$（$x_0\in I$）的解唯一，为

$$
y=\mathrm{e}^{-\int_{x_0}^xp(t)\,\mathrm{d}t}\Big(y_0+\int_{x_0}^xq(s)\mathrm{e}^{\int_{x_0}^sp(t)\,\mathrm{d}t}\,\mathrm{d}s\Big).
$$

**证明** 令 $y=C(x)\mathrm{e}^{-\int p\,\mathrm{d}x}$，则 $y'=C'(x)\mathrm{e}^{-\int p\,\mathrm{d}x}-p(x)C(x)\mathrm{e}^{-\int p\,\mathrm{d}x}$，代入式 (15.1) 后含 $C(x)$ 的两项抵消，得 $C'(x)=q(x)\mathrm{e}^{\int p\,\mathrm{d}x}$，积分即得式 (15.3)。反过来，若 $y$ 是任一解，令 $C(x)=y\,\mathrm{e}^{\int p\,\mathrm{d}x}$，同样的计算表明 $C'(x)=q(x)\mathrm{e}^{\int p\,\mathrm{d}x}$，所以 $y$ 具有式 (15.3) 的形式。初值问题的公式是把原函数取成变上限积分的结果，$C=y_0$ 由初始条件唯一确定。 $\square$

另一种看法：方程两边乘以 $\mu(x)=\mathrm{e}^{\int p\,\mathrm{d}x}$，左边恰好是 $(\mu y)'$，于是 $(\mu y)'=\mu q$，积分即得同样的公式。$\mu$ 是 15.4 节所说的**积分因子**的一个特例。

**算法 15.3.1（一阶线性方程）**

1. 化为标准形式 $y'+p(x)y=q(x)$（$y'$ 的系数为 1）；
2. 求 $P(x)=\int p(x)\,\mathrm{d}x$（取一个原函数，不加常数）；
3. 代入公式 (15.3)：$y=\mathrm{e}^{-P}\big(\int q\,\mathrm{e}^{P}\,\mathrm{d}x+C\big)$；或按常数变易法逐步计算；
4. 有初始条件时由它定出 $C$。

若方程关于 $y$ 不是线性的、关于 $x$ 却是线性的，可以把 $x$ 看作 $y$ 的函数（例 15.3.2）。

**例 15.3.1** 求解下列各题。（1）解 $y'+2xy=4x$。$P=x^2$，$y=\mathrm{e}^{-x^2}\big(\int4x\mathrm{e}^{x^2}\,\mathrm{d}x+C\big)=\mathrm{e}^{-x^2}(2\mathrm{e}^{x^2}+C)=2+C\mathrm{e}^{-x^2}$。

（2）解 $xy'-y=x^3+3x^2-2x$。标准形式 $y'-\dfrac yx=x^2+3x-2$，$P=-\ln\lvert x\rvert$，$\mathrm{e}^{-P}=\lvert x\rvert$，绝对值的符号可并入常数，取 $\mathrm{e}^{-P}=x$：

$$
y=x\Big(\int\frac{x^2+3x-2}{x}\,\mathrm{d}x+C\Big)=x\Big(\frac{x^2}{2}+3x-2\ln\lvert x\rvert+C\Big).
$$

（3）解初值问题 $y'+y\cot x=5\mathrm{e}^{\cos x}$，$y\big(\frac\pi2\big)=-4$。$P=\ln\sin x$（在 $0<x<\pi$ 上），

$$
y=\frac{1}{\sin x}\Big(\int5\mathrm{e}^{\cos x}\sin x\,\mathrm{d}x+C\Big)=\frac{C-5\mathrm{e}^{\cos x}}{\sin x}.
$$
由 $y\big(\frac\pi2\big)=C-5=-4$ 得 $C=1$，解为 $y=\dfrac{1-5\mathrm{e}^{\cos x}}{\sin x}$。

**例 15.3.2** 解 $y'=\dfrac{1}{2x-y^2}$。关于 $y$ 不是线性的，但 $\dfrac{\mathrm{d}x}{\mathrm{d}y}=2x-y^2$ 是 $x(y)$ 的线性方程：$\dfrac{\mathrm{d}x}{\mathrm{d}y}-2x=-y^2$，

$$
x=\mathrm{e}^{2y}\Big(-\int y^2\mathrm{e}^{-2y}\,\mathrm{d}y+C\Big)=C\mathrm{e}^{2y}+\frac{2y^2+2y+1}{4}.
$$

### 15.3.3. Bernoulli 方程

**定义 15.3.1** 形如 $y'+p(x)y=q(x)y^n$（$n\ne0,1$）的方程称为 **Bernoulli 方程**。

$n=0$ 或 $1$ 时它就是线性方程。

**算法 15.3.2** 两边除以 $y^n$：$y^{-n}y'+p(x)y^{1-n}=q(x)$。令 $u=y^{1-n}$，则 $u'=(1-n)y^{-n}y'$，方程化为 $u$ 的线性方程

$$
u'+(1-n)p(x)u=(1-n)q(x),
$$
用公式 (15.3) 求出 $u$ 后代回。$n>0$ 时 $y=0$ 也是解。

**例 15.3.3** 求解下列各题。（1）解 $y'-y=xy^5$。令 $u=y^{-4}$，$u'=-4y^{-5}y'$，方程 $y^{-5}y'-y^{-4}=x$ 化为 $-\dfrac14u'-u=x$，即 $u'+4u=-4x$。由公式 (15.3)，

$$
u=\mathrm{e}^{-4x}\Big(\int(-4x)\mathrm{e}^{4x}\,\mathrm{d}x+C\Big)=\mathrm{e}^{-4x}\Big(-x\mathrm{e}^{4x}+\frac14\mathrm{e}^{4x}+C\Big),
$$
所以 $y^{-4}=-x+\dfrac14+C\mathrm{e}^{-4x}$；另有解 $y=0$。

（2）解 $y'+2xy=xy^4$。令 $u=y^{-3}$，得 $u'-6xu=-3x$，$u=\mathrm{e}^{3x^2}\big(\int(-3x)\mathrm{e}^{-3x^2}\,\mathrm{d}x+C\big)=\dfrac12+C\mathrm{e}^{3x^2}$，即 $\dfrac{1}{y^3}=\dfrac12+C\mathrm{e}^{3x^2}$；另有解 $y=0$。

（3）解 $y'+\dfrac yx=ay^2\ln x$。令 $u=y^{-1}$，$u'-\dfrac ux=-a\ln x$，$u=x\big(-\int\frac{a\ln x}{x}\,\mathrm{d}x+C\big)=x\Big(C-\dfrac a2\ln^2x\Big)$，即 $y=\dfrac{1}{x\big(C-\frac a2\ln^2x\big)}$；另有解 $y=0$。

Bernoulli 方程说明了变量代换的作用：表面上非线性的方程，换一个未知函数就成了线性方程。再如 $y'=1+\mathrm{e}^{-y}\sin x$，两边乘以 $\mathrm{e}^y$ 得 $(\mathrm{e}^y)'=\mathrm{e}^y+\sin x$，它是 $u=\mathrm{e}^y$ 的线性方程，解得 $\mathrm{e}^y=C\mathrm{e}^x-\dfrac12(\sin x+\cos x)$。

## 15.4. 全微分方程与积分因子

### 15.4.1. 全微分方程

一阶方程常写成对称形式

$$
M(x,y)\,\mathrm{d}x+N(x,y)\,\mathrm{d}y=0,\tag{15.4}
$$
这时 $x$ 与 $y$ 的地位相同，哪个是自变量都可以。

**定义 15.4.1** 若存在可微函数 $u(x,y)$，使 $\mathrm{d}u=M\,\mathrm{d}x+N\,\mathrm{d}y$，即 $u$ 是微分形式 $M\,\mathrm{d}x+N\,\mathrm{d}y$ 的原函数（[2.2.10](/2.2.10#sec-10.5.4)），则称式 (15.4) 为**全微分方程**（恰当方程）。此时式 (15.4) 的通解是 $u(x,y)=C$。

确实，沿解曲线 $y=y(x)$ 有 $\dfrac{\mathrm{d}}{\mathrm{d}x}u(x,y(x))=M+Ny'=0$，所以 $u$ 在解曲线上为常数；反之由隐函数定理（$N\ne0$ 处），$u(x,y)=C$ 确定的函数满足方程。

**定理 15.4.1** 设 $M,N$ 在**单连通区域** $D$ 上有连续的偏导数，则式 (15.4) 是全微分方程的充要条件是在 $D$ 上

$$
\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}.
$$

必要性就是混合偏导数相等（命题 10.5.1）；充分性要用到 Green 公式，即平面**保守场**的判别定理，见 [2.2.14](/2.2.14)。这时原函数可以沿折线积分得到。

**算法 15.4.1（求解全微分方程）** 先验证 $M_y=N_x$，再用下列方法之一求原函数 $u$：

1. 折线积分：取 $(x_0,y_0)\in D$，使折线 $(x_0,y_0)\to(x,y_0)\to(x,y)$ 在 $D$ 内，则 $u(x,y)=\displaystyle\int_{x_0}^xM(s,y_0)\,\mathrm{d}s+\int_{y_0}^yN(x,t)\,\mathrm{d}t$；
2. 偏积分：$u=\int M(x,y)\,\mathrm{d}x+\varphi(y)$（积分时把 $y$ 看作常数），由 $u_y=N$ 定出 $\varphi'(y)$，再积分得 $\varphi(y)$；
3. 凑微分：把 $M\,\mathrm{d}x+N\,\mathrm{d}y$ 的各项分组，利用常见的全微分直接凑出 $\mathrm{d}u$。

常用的全微分：

| 微分式 | 原函数的微分 | 微分式 | 原函数的微分 |
|---|---|---|---|
| $x\,\mathrm{d}y+y\,\mathrm{d}x$ | $\mathrm{d}(xy)$ | $x\,\mathrm{d}x+y\,\mathrm{d}y$ | $\frac12\mathrm{d}(x^2+y^2)$ |
| $\dfrac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2}$ | $\mathrm{d}\big(\frac yx\big)$ | $\dfrac{y\,\mathrm{d}x-x\,\mathrm{d}y}{y^2}$ | $\mathrm{d}\big(\frac xy\big)$ |
| $\dfrac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2+y^2}$ | $\mathrm{d}\big(\arctan\frac yx\big)$ | $\dfrac{x\,\mathrm{d}y-y\,\mathrm{d}x}{xy}$ | $\mathrm{d}\big(\ln\big\lvert\frac yx\big\rvert\big)$ |
| $\dfrac{x\,\mathrm{d}x+y\,\mathrm{d}y}{x^2+y^2}$ | $\frac12\mathrm{d}\ln(x^2+y^2)$ | $\dfrac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2-y^2}$ | $\frac12\mathrm{d}\big(\ln\big\lvert\frac{x+y}{x-y}\big\rvert\big)$ |

**例 15.4.1** 解 $(2x^3+3y)\,\mathrm{d}x+(3x+y-1)\,\mathrm{d}y=0$。$M_y=3=N_x$，是全微分方程。三种方法：

- 折线积分：取 $(x_0,y_0)=(0,0)$，$u=\int_0^x2s^3\,\mathrm{d}s+\int_0^y(3x+t-1)\,\mathrm{d}t=\dfrac{x^4}2+3xy+\dfrac{y^2}2-y$；
- 偏积分：$u=\int(2x^3+3y)\,\mathrm{d}x=\dfrac{x^4}2+3xy+\varphi(y)$，由 $u_y=3x+\varphi'(y)=3x+y-1$ 得 $\varphi=\dfrac{y^2}2-y$；
- 凑微分：$2x^3\,\mathrm{d}x+3(y\,\mathrm{d}x+x\,\mathrm{d}y)+(y-1)\,\mathrm{d}y=\mathrm{d}\Big(\dfrac{x^4}2+3xy+\dfrac{y^2}2-y\Big)$。

通解为 $x^4+6xy+y^2-2y=C$。

**例 15.4.2** 求解下列各题。（1）$2x(y\mathrm{e}^{x^2}-1)\,\mathrm{d}x+\mathrm{e}^{x^2}\,\mathrm{d}y=0$：$M_y=2x\mathrm{e}^{x^2}=N_x$。分组 $(2xy\mathrm{e}^{x^2}\,\mathrm{d}x+\mathrm{e}^{x^2}\,\mathrm{d}y)-2x\,\mathrm{d}x=\mathrm{d}(y\mathrm{e}^{x^2})-\mathrm{d}(x^2)$，通解 $y\mathrm{e}^{x^2}-x^2=C$。

（2）$(\cos y+y\cos x)\,\mathrm{d}x+(\sin x-x\sin y)\,\mathrm{d}y=0$：分组 $(\cos y\,\mathrm{d}x-x\sin y\,\mathrm{d}y)+(y\cos x\,\mathrm{d}x+\sin x\,\mathrm{d}y)=\mathrm{d}(x\cos y)+\mathrm{d}(y\sin x)$，通解 $x\cos y+y\sin x=C$。

### 15.4.2. 积分因子

$y\,\mathrm{d}x-x\,\mathrm{d}y=0$ 不是全微分方程（$M_y=1\ne-1=N_x$），但乘以 $\dfrac1{y^2}$ 后变成 $\mathrm{d}\big(\frac xy\big)=0$。这启发我们：先乘一个因子把方程变成全微分方程。

**定义 15.4.2** 若存在不恒为零的可微函数 $\mu(x,y)$，使 $\mu M\,\mathrm{d}x+\mu N\,\mathrm{d}y=0$ 是全微分方程，则称 $\mu$ 为式 (15.4) 的一个**积分因子**。

在 $\mu\ne0$ 处，乘以 $\mu$ 不改变方程的解；$\mu$ 的零点或奇点要另外检查是否给出解（或丢掉解）。积分因子不唯一：由上面的常用微分表，$\dfrac1{y^2}$、$\dfrac1{x^2}$、$\dfrac1{xy}$、$\dfrac1{x^2+y^2}$ 都是 $y\,\mathrm{d}x-x\,\mathrm{d}y=0$ 的积分因子。按定义，$\mu$ 是积分因子当且仅当 $(\mu M)_y=(\mu N)_x$，即

$$
N\mu_x-M\mu_y=(M_y-N_x)\mu.
$$
这是 $\mu$ 的偏微分方程，一般比原方程更难解。但若要求 $\mu$ 只依赖于一个变量，它就退化为常微分方程。

**定理 15.4.2** 设 $M,N$ 有连续的偏导数。

1. 若 $\dfrac{M_y-N_x}{N}=f(x)$ 只与 $x$ 有关，则 $\mu=\mathrm{e}^{\int f(x)\,\mathrm{d}x}$ 是一个积分因子；
2. 若 $\dfrac{M_y-N_x}{M}=g(y)$ 只与 $y$ 有关，则 $\mu=\mathrm{e}^{-\int g(y)\,\mathrm{d}y}$ 是一个积分因子。

**证明** （1）$\mu=\mu(x)$ 时 $\mu_y=0$，条件 $N\mu_x-M\mu_y=(M_y-N_x)\mu$ 化为 $\mu'(x)=f(x)\mu$，$\mu=\mathrm{e}^{\int f\,\mathrm{d}x}$ 满足它。（2）$\mu=\mu(y)$ 时条件化为 $-M\mu'(y)=(M_y-N_x)\mu$，即 $\mu'=-g(y)\mu$。 $\square$

一阶线性方程 $\mathrm{d}y+(p(x)y-q(x))\,\mathrm{d}x=0$ 中 $\dfrac{M_y-N_x}{N}=p(x)$，积分因子 $\mathrm{e}^{\int p\,\mathrm{d}x}$ 正是 15.3.2 节的 $\mu$。

**定理 15.4.3** 若 $M,N$ 是同次**齐次函数**，且 $Mx+Ny\ne0$，则 $\mu=\dfrac{1}{Mx+Ny}$ 是式 (15.4) 的一个积分因子。

**证明** 设 $M,N$ 是 $k$ 次齐次函数，由 Euler 齐次函数定理（定理 10.7.2），$xM_x+yM_y=kM$，$xN_x+yN_y=kN$。记 $S=Mx+Ny$，直接计算

$$
\Big(\frac MS\Big)_y-\Big(\frac NS\Big)_x=\frac{M_yS-MS_y-N_xS+NS_x}{S^2},
$$
其中 $S_y=xM_y+N+yN_y$，$S_x=M+xM_x+yN_x$。分子展开后为

$$
N(yM_y+xM_x)-M(xN_x+yN_y)=N\cdot kM-M\cdot kN=0.\qquad\square
$$

**例 15.4.3** 求解下列各题。（1）解 $(x^2+y^2+x)\,\mathrm{d}x+xy\,\mathrm{d}y=0$。$M_y-N_x=2y-y=y$，$\dfrac{M_y-N_x}{N}=\dfrac1x$，积分因子 $\mu=x$。乘以 $x$ 后 $(x^3+xy^2+x^2)\,\mathrm{d}x+x^2y\,\mathrm{d}y=0$ 是全微分方程，通解 $\dfrac{x^4}4+\dfrac{x^3}3+\dfrac{x^2y^2}2=C$。

（2）解 $(x^4+y^4)\,\mathrm{d}x-xy^3\,\mathrm{d}y=0$。$M,N$ 是 4 次齐次函数，$Mx+Ny=x^5$，积分因子 $\dfrac1{x^5}$：

$$
\frac{\mathrm{d}x}{x}+\Big(\frac{y^4}{x^5}\,\mathrm{d}x-\frac{y^3}{x^4}\,\mathrm{d}y\Big)=\mathrm{d}\Big(\ln\lvert x\rvert-\frac{y^4}{4x^4}\Big)=0,
$$
通解 $\ln\lvert x\rvert-\dfrac{y^4}{4x^4}=C$，即 $x=C\mathrm{e}^{y^4/(4x^4)}$。（它也是齐次型方程，可以用算法 15.2.2 求解。）

更多时候积分因子靠观察得到：把方程中能凑成某个常用微分（表中各式的分子）的项分出来，选一个积分因子使它变成全微分，同时剩下的项仍是全微分。

**例 15.4.4** 求解下列各题。（1）$x\,\mathrm{d}y-y\,\mathrm{d}x-(1-x^2)\,\mathrm{d}x=0$：乘以 $\dfrac1{x^2}$ 得 $\mathrm{d}\big(\frac yx\big)-\Big(\dfrac1{x^2}-1\Big)\mathrm{d}x=0$，通解 $\dfrac yx+\dfrac1x+x=C$。

（2）$x\,\mathrm{d}x+y\,\mathrm{d}y-4y^3(x^2+y^2)\,\mathrm{d}y=0$：乘以 $\dfrac1{x^2+y^2}$ 得 $\dfrac12\mathrm{d}\ln(x^2+y^2)-\mathrm{d}(y^4)=0$，通解 $\dfrac12\ln(x^2+y^2)-y^4=C$。

（3）$x^2y'+xy+\sqrt{1-x^2y^2}=0$：写成 $x(x\,\mathrm{d}y+y\,\mathrm{d}x)+\sqrt{1-x^2y^2}\,\mathrm{d}x=0$，乘以 $\dfrac{1}{x\sqrt{1-x^2y^2}}$ 得 $\dfrac{\mathrm{d}(xy)}{\sqrt{1-(xy)^2}}+\dfrac{\mathrm{d}x}{x}=0$，通解 $\arcsin(xy)+\ln\lvert x\rvert=C$。

（4）$(1+xy)y\,\mathrm{d}x+(1-xy)x\,\mathrm{d}y=0$：整理为 $(y\,\mathrm{d}x+x\,\mathrm{d}y)+xy(y\,\mathrm{d}x-x\,\mathrm{d}y)=0$，即 $\mathrm{d}(xy)+xy(y\,\mathrm{d}x-x\,\mathrm{d}y)=0$。乘以 $\dfrac{1}{x^2y^2}$：$\dfrac{\mathrm{d}(xy)}{(xy)^2}+\dfrac{\mathrm{d}x}{x}-\dfrac{\mathrm{d}y}{y}=0$，通解 $\ln\Big\lvert\dfrac xy\Big\rvert-\dfrac1{xy}=C$。

## 15.5. 可降阶的高阶方程

高阶方程一般比一阶方程难得多，但有几类可以通过换未知函数降低阶数，化为一阶方程。

### 15.5.1. $y^{(n)}=f(x)$

右端只含 $x$，积分一次降一阶，连续积分 $n$ 次即得含 $n$ 个任意常数的通解。

**例 15.5.1** 解 $y^{(4)}=\sin x+x$。依次积分：

$$
y'''=-\cos x+\frac{x^2}2+C_1,\quad y''=-\sin x+\frac{x^3}6+C_1x+C_2,\quad y'=\cos x+\frac{x^4}{24}+\frac{C_1}2x^2+C_2x+C_3,
$$
所以 $y=\sin x+\dfrac{x^5}{120}+\dfrac{C_1}6x^3+\dfrac{C_2}2x^2+C_3x+C_4$，常数 $C_1/6$、$C_2/2$ 可以重新记为任意常数。

### 15.5.2. 不显含 $y$ 的方程 $y''=f(x,y')$

令 $y'=p(x)$，则 $y''=p'$，方程化为一阶方程 $p'=f(x,p)$。解出 $p=\varphi(x,C_1)$ 后再积分一次。更一般地，不含 $y,y',\dots,y^{(k-1)}$ 的方程可令 $p=y^{(k)}$。

**例 15.5.2** 求解下列各题。（1）解 $x^2y''+xy'=1$（$x>0$）。令 $p=y'$，$p'+\dfrac px=\dfrac1{x^2}$，由公式 (15.3)，$p=\dfrac1x\big(\int\frac1x\,\mathrm{d}x+C_1\big)=\dfrac{\ln x+C_1}{x}$，所以 $y=\dfrac12\ln^2x+C_1\ln x+C_2$。

（2）解 $y^{(5)}=\dfrac1xy^{(4)}$。令 $p=y^{(4)}$，$\dfrac{\mathrm{d}p}{p}=\dfrac{\mathrm{d}x}{x}$，$p=C_1x$，再积分四次得 $y=\dfrac{C_1}{120}x^5+C_2x^3+C_3x^2+C_4x+C_5$（积分产生的系数 $\frac16$、$\frac12$ 已并入任意常数）。

（3）解初值问题 $y''+2x(y')^2=0$，$y(0)=1$，$y'(0)=0$。令 $p=y'$，$p'=-2xp^2$。$p\ne0$ 时 $\dfrac1p=x^2+C$；另有解 $p=0$。由 $p(0)=0$，只能取 $p\equiv0$（由 $\frac1p=x^2+C$ 得到的 $p$ 处处不为零），所以 $y'\equiv0$，$y\equiv1$。分离变量时若丢掉 $p=0$，就得不到这个解。

**例 15.5.3** 曲率恒为非零常数 $K$ 的平面曲线是圆。设曲线为 $y=y(x)$，由**曲率**公式（[2.2.7](/2.2.7)），$\dfrac{y''}{(1+y'^2)^{3/2}}=K$（适当选取方向使 $y''>0$ 的一段，$K>0$）。令 $p=y'$：

$$
\frac{\mathrm{d}p}{(1+p^2)^{3/2}}=K\,\mathrm{d}x,\qquad\frac{p}{\sqrt{1+p^2}}=K(x-C_1).
$$
解出 $p=\dfrac{K(x-C_1)}{\sqrt{1-K^2(x-C_1)^2}}$，再积分得 $y=-\dfrac1K\sqrt{1-K^2(x-C_1)^2}+C_2$，即

$$
(x-C_1)^2+(y-C_2)^2=\frac1{K^2},
$$
是半径为 $\dfrac1K$ 的圆。

**例 15.5.4（悬链线，续例 15.1.3）** 解 $y''=a\sqrt{1+y'^2}$，$y(0)=y'(0)=0$。令 $p=y'$，$\dfrac{\mathrm{d}p}{\sqrt{1+p^2}}=a\,\mathrm{d}x$。令 $p=\sinh s$，左边为 $\mathrm{d}s$，得 $s=ax+c$；由 $p(0)=0$ 得 $c=0$，即 $y'=\sinh ax$。再积分，由 $y(0)=0$ 得

$$
y=\frac{\cosh ax-1}{a}.
$$
悬链线是**双曲函数**的图形，这就是双曲余弦（"悬链线函数"）名称的来历。

### 15.5.3. 不显含 $x$ 的方程 $y''=f(y,y')$

把 $y$ 当作新的自变量，令 $y'=p(y)$，则由链式法则

$$
y''=\frac{\mathrm{d}p}{\mathrm{d}y}\cdot\frac{\mathrm{d}y}{\mathrm{d}x}=p\frac{\mathrm{d}p}{\mathrm{d}y},
$$
方程化为 $p$ 关于 $y$ 的一阶方程 $p\dfrac{\mathrm{d}p}{\mathrm{d}y}=f(y,p)$。解出 $p=\varphi(y,C_1)$ 后，$\dfrac{\mathrm{d}y}{\varphi(y,C_1)}=\mathrm{d}x$ 是变量分离方程。

注意两类方程的代换不同：不显含 $y$ 时 $p$ 是 $x$ 的函数，$y''=\dfrac{\mathrm{d}p}{\mathrm{d}x}$；不显含 $x$ 时 $p$ 是 $y$ 的函数，$y''=p\dfrac{\mathrm{d}p}{\mathrm{d}y}$。

**例 15.5.5** 求解下列各题。（1）解 $yy''-(y')^2=0$。令 $y'=p(y)$，$yp\dfrac{\mathrm{d}p}{\mathrm{d}y}-p^2=0$，所以 $p=0$ 或 $y\dfrac{\mathrm{d}p}{\mathrm{d}y}=p$。后者得 $p=C_1y$，即 $y'=C_1y$，$y=C_2\mathrm{e}^{C_1x}$；$p=0$ 给出 $y=C$，已包含在其中（$C_1=0$）。也可以凑微分：方程两边除以 $y^2$ 得 $\big(\frac{y'}{y}\big)'=0$。

（2）解 $y''=(y')^3+y'$。令 $y'=p(y)$，$p\dfrac{\mathrm{d}p}{\mathrm{d}y}=p^3+p$，所以 $p=0$（$y=C$）或 $\dfrac{\mathrm{d}p}{1+p^2}=\mathrm{d}y$，$\arctan p=y+C_1$，$y'=\tan(y+C_1)$。分离变量 $\cot(y+C_1)\,\mathrm{d}y=\mathrm{d}x$，得 $\ln\lvert\sin(y+C_1)\rvert=x+\ln\lvert C_2\rvert$，通解 $\sin(y+C_1)=C_2\mathrm{e}^x$。

## 小结

| 方程类型 | 形式 | 解法 |
|---|---|---|
| 变量分离方程 | $y'=f(x)g(y)$ | $\int\frac{\mathrm{d}y}{g(y)}=\int f\,\mathrm{d}x+C$；补上 $g(c)=0$ 的解 $y=c$ |
| 齐次型方程 | $y'=f(y/x)$ | $y=xu$，$\frac{\mathrm{d}u}{f(u)-u}=\frac{\mathrm{d}x}{x}$ |
| 线性组合的函数 | $y'=f(ax+by+c)$ | $u=ax+by+c$ |
| 分式线性 | $y'=f\big(\frac{a_1x+b_1y+c_1}{a_2x+b_2y+c_2}\big)$ | 行列式非零时平移到交点，化为齐次型；为零时化为上一类 |
| $xy$ 型 | $yf(xy)\,\mathrm{d}x+xg(xy)\,\mathrm{d}y=0$ | $z=xy$，$\frac{\mathrm{d}x}{x}=\frac{g\,\mathrm{d}z}{z(g-f)}$ |
| 一阶线性方程 | $y'+p(x)y=q(x)$ | 常数变易法，公式 (15.3) |
| Bernoulli 方程 | $y'+py=qy^n$ | $u=y^{1-n}$ 化为线性方程 |
| 全微分方程 | $M\,\mathrm{d}x+N\,\mathrm{d}y=0$，$M_y=N_x$ | 折线积分、偏积分或凑微分求原函数 $u$，$u=C$ |
| 积分因子 | $M_y\ne N_x$ | $\frac{M_y-N_x}{N}=f(x)$：$\mathrm{e}^{\int f\mathrm{d}x}$；$\frac{M_y-N_x}{M}=g(y)$：$\mathrm{e}^{-\int g\mathrm{d}y}$；同次齐次：$\frac1{Mx+Ny}$；观察法 |
| 可降阶方程 | $y^{(n)}=f(x)$；$y''=f(x,y')$；$y''=f(y,y')$ | 逐次积分；$y'=p(x)$；$y'=p(y)$，$y''=p\frac{\mathrm{d}p}{\mathrm{d}y}$ |

几点共同的注意事项：分离变量或除以某个式子时，检查被除式为零给出的解（例 15.2.1、例 15.5.2）；隐式解 $u(x,y)=C$ 已是合格的答案；通解不一定包含全部解，但线性方程的通解包含全部解（定理 15.3.1）。
