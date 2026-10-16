---
title: 存在和唯一性定理
---

大多数微分方程不能用初等积分法求解，但这不意味着它们没有解。本章回答常微分方程理论的第一个基本问题：一阶显式方程 $y'=f(x,y)$ 的**初值问题**在什么条件下有解，有解时是否唯一。[2.2.15](/2.2.15) 只陈述了**存在唯一性定理**（定理 15.1.1），这里给出完整证明：先用 Picard 逐次逼近在 Lipschitz 条件下同时得到存在性与唯一性；再把唯一性的条件减弱为 Osgood 条件；最后去掉一切关于 $y$ 的正则性假设，只要求 $f$ 连续，用 Euler 折线与 Ascoli 引理证明 Peano 存在定理。这里得到的解都只在初值点附近的小区间上存在，把它延伸到尽可能大的区间是下一章的内容；推广到方程组与高阶方程见 [2.4.7](/2.4.7)。

本章始终考虑初值问题

$$
y'=f(x,y),\qquad y(x_0)=y_0, \tag{4.1}
$$
其中 $f$ 在矩形 $R=\{(x,y)\mid\lvert x-x_0\rvert\le a,\ \lvert y-y_0\rvert\le b\}$ 上连续，记 $M=\max_R\lvert f\rvert$。

## 4.1. Lipschitz 条件与等价的积分方程

### 4.1.1. Lipschitz 条件

**定义 4.1.1（Lipschitz 条件）** 若存在常数 $L\ge0$，使对 $R$ 中任意两点 $(x,y_1)$、$(x,y_2)$ 都有

$$
\lvert f(x,y_1)-f(x,y_2)\rvert\le L\lvert y_1-y_2\rvert,
$$
则称 $f$ 在 $R$ 上关于 $y$ 满足 **Lipschitz 条件**，$L$ 称为 Lipschitz 常数。

**定义 4.1.2（局部 Lipschitz 条件）** 设 $f$ 定义在区域 $G$ 上。若 $G$ 中每一点都有一个邻域（矩形），使 $f$ 在其中关于 $y$ 满足 Lipschitz 条件（常数可以随邻域而变），则称 $f$ 在 $G$ 内关于 $y$ 满足**局部 Lipschitz 条件**。

**命题 4.1.1** 设 $f$ 与 $f_y$ 在 $R$ 上连续，则 $f$ 在 $R$ 上关于 $y$ 满足 Lipschitz 条件，可取 $L=\max_R\lvert f_y\rvert$。因此 $f,f_y$ 在区域 $G$ 内连续时，$f$ 在 $G$ 内满足局部 Lipschitz 条件。

**证明** 对固定的 $x$，由 **Lagrange 中值定理**，$f(x,y_1)-f(x,y_2)=f_y(x,\xi)(y_1-y_2)$，$\xi$ 在 $y_1,y_2$ 之间，仍在 $R$ 中。 $\square$

Lipschitz 条件介于"连续"和"有连续偏导数"之间：$f(y)=\lvert y\rvert$ 在 $y=0$ 处不可导，但满足 Lipschitz 条件（$L=1$）；$f(y)=\sqrt{\lvert y\rvert}$ 连续，但 $\lvert f(y)-f(0)\rvert/\lvert y\rvert=\lvert y\rvert^{-1/2}$ 在 $0$ 附近无界，不满足 Lipschitz 条件。

### 4.1.2. 等价的积分方程

**引理 4.1.1** 设 $\varphi$ 在区间 $I\ni x_0$ 上连续，图形含于 $R$。则 $\varphi$ 是初值问题 (4.1) 在 $I$ 上的解，当且仅当它满足积分方程

$$
\varphi(x)=y_0+\int_{x_0}^x f(t,\varphi(t))\,\mathrm{d}t,\qquad x\in I. \tag{4.2}
$$

**证明** 若 $\varphi$ 是解，则 $\varphi'(t)=f(t,\varphi(t))$ 连续，从 $x_0$ 到 $x$ 积分并用 $\varphi(x_0)=y_0$ 即得 (4.2)。反之，若 $\varphi$ 满足 (4.2)，被积函数 $f(t,\varphi(t))$ 连续，由变上限积分的求导公式，$\varphi$ 可导且 $\varphi'(x)=f(x,\varphi(x))$；又 $\varphi(x_0)=y_0$。 $\square$

积分方程的好处是只要求 $\varphi$ 连续，并且积分运算对一致收敛的极限稳定。下面的两种构造（Picard 序列、Euler 折线）都是先造出 (4.2) 的近似解，再取极限。

## 4.2. Picard 定理

**定理 4.2.1（Picard 定理）** 设 $f$ 在 $R$ 上连续，且关于 $y$ 满足 Lipschitz 条件。令

$$
h=\min\Big\{a,\frac bM\Big\}
$$
（$M=0$ 时取 $h=a$），则初值问题 (4.1) 在区间 $I=[x_0-h,x_0+h]$ 上有且只有一个解。

$h$ 的取法有直观的几何意义：积分曲线的斜率不超过 $M$，所以它停留在以 $(x_0,y_0)$ 为顶点、斜率为 $\pm M$ 的两条直线所夹的角形区域内。$M$ 较小时积分曲线平缓，先到达 $R$ 的左右两边，$h=a$；$M$ 较大时积分曲线陡峭，可能先碰到上下两边，只能取 $h=b/M<a$。

**证明** 只证右半区间 $[x_0,x_0+h]$，左半区间同理。分四步。

第一步：构造 Picard 序列（Picard iteration）。令 $\varphi_0(x)\equiv y_0$，

$$
\varphi_{n+1}(x)=y_0+\int_{x_0}^x f(t,\varphi_n(t))\,\mathrm{d}t,\qquad n=0,1,2,\dots \tag{4.3}
$$
用归纳法证明每个 $\varphi_n$ 在 $I$ 上有定义、连续，且 $\lvert\varphi_n(x)-y_0\rvert\le M(x-x_0)\le b$。$n=0$ 显然。若 $\varphi_n$ 满足这些性质，则 $f(t,\varphi_n(t))$ 有定义且连续，$\varphi_{n+1}$ 连续，并且

$$
\lvert\varphi_{n+1}(x)-y_0\rvert\le\int_{x_0}^x\lvert f(t,\varphi_n(t))\rvert\,\mathrm{d}t\le M(x-x_0)\le Mh\le b.
$$
所以 (4.3) 的每一步都不会离开 $R$，这正是取 $h\le b/M$ 的原因。

第二步：估计相邻两项之差。用归纳法证明

$$
\lvert\varphi_{n+1}(x)-\varphi_n(x)\rvert\le\frac{ML^n(x-x_0)^{n+1}}{(n+1)!},\qquad x\in[x_0,x_0+h]. \tag{4.4}
$$
$n=0$ 时就是第一步的估计 $\lvert\varphi_1-\varphi_0\rvert\le M(x-x_0)$。设 (4.4) 对 $n$ 成立，由 Lipschitz 条件，

$$
\lvert\varphi_{n+2}(x)-\varphi_{n+1}(x)\rvert\le\int_{x_0}^x L\lvert\varphi_{n+1}(t)-\varphi_n(t)\rvert\,\mathrm{d}t\le L\int_{x_0}^x\frac{ML^n(t-x_0)^{n+1}}{(n+1)!}\,\mathrm{d}t=\frac{ML^{n+1}(x-x_0)^{n+2}}{(n+2)!}.
$$

第三步：一致收敛到解。$\varphi_n=\varphi_0+\sum_{k=0}^{n-1}(\varphi_{k+1}-\varphi_k)$ 是函数项级数的部分和，由 (4.4)，它的各项被收敛的数项级数 $\sum_k\dfrac{ML^kh^{k+1}}{(k+1)!}$ 控制，由 **Weierstrass 判别法**，$\{\varphi_n\}$ 在 $[x_0,x_0+h]$ 上**一致收敛**到一个连续函数 $\varphi$，且 $\lvert\varphi(x)-y_0\rvert\le M(x-x_0)\le b$。由 Lipschitz 条件，

$$
\lvert f(t,\varphi_n(t))-f(t,\varphi(t))\rvert\le L\lvert\varphi_n(t)-\varphi(t)\rvert,
$$
所以 $f(t,\varphi_n(t))$ 一致收敛到 $f(t,\varphi(t))$，可以在 (4.3) 中对积分取极限，得到 $\varphi$ 满足积分方程 (4.2)。由引理 4.1.1，$\varphi$ 是 (4.1) 的解。

第四步：唯一性。设 $\psi$ 是 (4.1) 在 $[x_0,x_0+c]$（$0<c\le h$）上的任一解，它的图形含于 $R$。与第二步完全相同地用归纳法可证

$$
\lvert\psi(x)-\varphi_n(x)\rvert\le\frac{ML^n(x-x_0)^{n+1}}{(n+1)!}:
$$
$n=0$ 时 $\lvert\psi(x)-y_0\rvert=\Big\lvert\int_{x_0}^xf(t,\psi(t))\,\mathrm{d}t\Big\rvert\le M(x-x_0)$；归纳步骤只用到 $\psi$ 满足积分方程 (4.2)。令 $n\to\infty$，右端趋于 $0$，所以 $\psi=\lim\varphi_n=\varphi$。 $\square$

在第四步中取 $\psi=\varphi$，就得到逐次逼近的误差估计。

**推论 4.2.1（误差估计）** 在定理 4.2.1 的条件下，对 $x\in I$，

$$
\lvert\varphi(x)-\varphi_n(x)\rvert\le\frac{ML^n\lvert x-x_0\rvert^{n+1}}{(n+1)!}\le\frac{ML^nh^{n+1}}{(n+1)!}.
$$

**注 4.2.1** 证明也可以用压缩映射的语言叙述：在连续函数空间上定义算子 $(T\varphi)(x)=y_0+\int_{x_0}^xf(t,\varphi(t))\,\mathrm{d}t$，积分方程 (4.2) 就是不动点方程 $\varphi=T\varphi$，Picard 序列就是迭代 $\varphi_{n+1}=T\varphi_n$。估计 (4.4) 中的阶乘说明 $T$ 的高次幂是压缩的，因此不需要把 $h$ 取得使 $Lh<1$。

**例 4.2.1** 对 $y'=y$，$y(0)=1$，$f(x,y)=y$ 在整个平面上满足 Lipschitz 条件（$L=1$）。Picard 序列为

$$
\varphi_0=1,\quad\varphi_1=1+x,\quad\varphi_2=1+x+\frac{x^2}{2},\quad\dots,\quad\varphi_n=\sum_{k=0}^n\frac{x^k}{k!},
$$
正是 $\mathrm{e}^x$ 的 Taylor 多项式，在任何有界区间上一致收敛到解 $\mathrm{e}^x$。

![初值问题 y' = y, y(0) = 1 的 Picard 迭代 phi_0, ..., phi_4 与精确解 e^x：迭代函数在初值点附近最先贴近解，逼近的范围随 n 增大而扩大](./plots/picard-iterates.py)

**例 4.2.2** 对 $y'=x^2+y^2$，$y(0)=0$，取 $R:\lvert x\rvert\le1$，$\lvert y\rvert\le1$。则 $M=2$，$L=\max_R\lvert2y\rvert=2$，$h=\min\{1,1/2\}=\dfrac12$。前几次迭代是

$$
\varphi_1=\frac{x^3}{3},\qquad\varphi_2=\frac{x^3}{3}+\frac{x^7}{63},
$$
由推论 4.2.1，在 $\lvert x\rvert\le\dfrac12$ 上 $\lvert\varphi-\varphi_2\rvert\le\dfrac{2\cdot2^2\cdot(1/2)^3}{3!}=\dfrac16$。这个误差界很保守：实际误差小于 $10^{-4}$。这个方程的解不能用初等函数表示，但定理保证它存在唯一；它的实际存在区间见例 5.4.1。

## 4.3. Osgood 唯一性定理

Lipschitz 条件只是唯一性的充分条件。迄今没有一个既充分又必要、又便于验证的唯一性条件；下面的 Osgood 条件比 Lipschitz 条件弱，并且在某种意义上是最优的（注 4.3.1）。

**定义 4.3.1（Osgood 条件）** 设 $f$ 在区域 $G$ 内连续。若对 $G$ 中任意两点 $(x,y_1)$、$(x,y_2)$ 都有

$$
\lvert f(x,y_1)-f(x,y_2)\rvert\le F(\lvert y_1-y_2\rvert),
$$
其中 $F(r)$ 是 $r>0$ 时的正连续函数，且对某个 $r_1>0$，瑕积分

$$
\int_0^{r_1}\frac{\mathrm{d}r}{F(r)}=+\infty,
$$
则称 $f$ 在 $G$ 内关于 $y$ 满足 **Osgood 条件**。

Lipschitz 条件是 $F(r)=Lr$ 的特例：$\int_0^{r_1}\frac{\mathrm{d}r}{Lr}=+\infty$。

**定理 4.3.1（Osgood 定理）** 设 $f$ 在区域 $G$ 内关于 $y$ 满足 Osgood 条件，则方程 $y'=f(x,y)$ 经过 $G$ 内每一点的解至多有一个。

**证明** 设有两个解 $y=y_1(x)$、$y=y_2(x)$ 都经过点 $(x_0,y_0)\in G$，而存在 $x_1$ 使 $y_1(x_1)\ne y_2(x_1)$。不妨设 $x_1>x_0$，$y_1(x_1)>y_2(x_1)$（$x_1<x_0$ 的情形同理）。令

$$
\bar x=\sup\{x\in[x_0,x_1]\mid y_1(x)=y_2(x)\},
$$
由连续性 $y_1(\bar x)=y_2(\bar x)$，所以 $x_0\le\bar x<x_1$，且 $r(x)=y_1(x)-y_2(x)$ 满足 $r(\bar x)=0$，$r(x)>0$（$\bar x<x\le x_1$）。在 $(\bar x,x_1]$ 上

$$
r'(x)=f(x,y_1(x))-f(x,y_2(x))\le F(\lvert y_1(x)-y_2(x)\rvert)=F(r(x)),
$$
即 $\dfrac{r'(x)}{F(r(x))}\le1$。对 $\bar x<\xi<x_1$，从 $\xi$ 到 $x_1$ 积分并换元 $r=r(x)$：

$$
\int_{r(\xi)}^{r(x_1)}\frac{\mathrm{d}r}{F(r)}\le x_1-\xi.
$$
令 $\xi\to\bar x^+$，$r(\xi)\to0^+$，左端趋于 $\int_0^{r(x_1)}\frac{\mathrm{d}r}{F(r)}=+\infty$（$F$ 在 $(0,+\infty)$ 上正且连续，积分是否发散只取决于 $0$ 附近），而右端有界，矛盾。 $\square$

**例 4.3.1** 讨论 $y'=\lvert y\rvert^\alpha$（$\alpha>0$）满足 $y(0)=0$ 的解是否唯一。$y\equiv0$ 总是解。

（1）$\alpha\ge1$：$f(y)=\lvert y\rvert^\alpha$ 在 $\lvert y\rvert\le1$ 上满足 Lipschitz 条件（$\alpha=1$ 时 $L=1$；$\alpha>1$ 时 $f$ 连续可导，$L=\alpha$），所以零解唯一，且任何非零解永不为零。例如 $\alpha>1$、$y(0)=y_0>0$ 时，分离变量得

$$
y=\frac{y_0}{\big(1-(\alpha-1)y_0^{\alpha-1}x\big)^{1/(\alpha-1)}},
$$
它在 $x\to\dfrac{1}{(\alpha-1)y_0^{\alpha-1}}$ 时趋于无穷，但在存在区间内保持正号；$\alpha=1$ 时 $y=y_0\mathrm{e}^x$（$y_0>0$）或 $y=y_0\mathrm{e}^{-x}$（$y_0<0$）。

（2）$0<\alpha<1$：$f$ 在 $y=0$ 附近不满足 Lipschitz 条件，而对 $F(r)=r^\alpha$ 有 $\int_0^{r_1}r^{-\alpha}\,\mathrm{d}r=\dfrac{r_1^{1-\alpha}}{1-\alpha}<+\infty$，Osgood 条件也不成立。此时唯一性确实失去：对任意 $c_1\le0\le c_2$，

$$
y=\begin{cases}-\big((1-\alpha)(c_1-x)\big)^{1/(1-\alpha)},&x<c_1,\\0,&c_1\le x\le c_2,\\\big((1-\alpha)(x-c_2)\big)^{1/(1-\alpha)},&x>c_2\end{cases}
$$
都是满足 $y(0)=0$ 的解。注意 $y'=\lvert y\rvert^\alpha\ge0$，解必须单调不减，所以 $x<0$ 一侧只能取负的一支。

![y' = |y|^{1/2} 过原点的解族：沿 x 轴走一段后，向右在任意 c_2 >= 0 处分出 y = (x - c_2)^2/4，向左在任意 c_1 <= 0 处分出 y = -(c_1 - x)^2/4；所有解都单调不减](./plots/osgood-nonuniqueness.py)

**例 4.3.2** 方程

$$
y'=f(y)=\begin{cases}y\ln\lvert y\rvert,&y\ne0,\\0,&y=0\end{cases}
$$
满足 $y(0)=0$ 的解唯一，但 $f$ 在 $y=0$ 附近不满足 Lipschitz 条件：$\dfrac{\lvert f(y)-f(0)\rvert}{\lvert y\rvert}=\lvert\ln\lvert y\rvert\rvert\to+\infty$。在带形 $\lvert y\rvert<\dfrac14$ 内，利用 $-t\ln t$ 在 $(0,\mathrm{e}^{-1})$ 上的单调性与凹性可以验证 $\lvert f(y_1)-f(y_2)\rvert\le F(\lvert y_1-y_2\rvert)$，其中 $F(r)=2r\lvert\ln r\rvert$（$0<r<\frac12$），而

$$
\int_0^{r_1}\frac{\mathrm{d}r}{r\lvert\ln r\rvert}=\Big[-\ln\lvert\ln r\rvert\Big]_0^{r_1}=+\infty,
$$
Osgood 条件成立，零解唯一；在 $y\ne0$ 处 $f$ 连续可导，局部 Lipschitz 条件成立。事实上，$y(0)=y_0\ne0$ 的解是 $y=\operatorname{sgn}(y_0)\exp\!\big(\mathrm{e}^x\ln\lvert y_0\rvert\big)$，永不为零。这个例子说明 Lipschitz 条件对唯一性不是必要的。

**注 4.3.1** 对右端只依赖 $y$ 的方程，Osgood 条件是最优的：设 $F$ 连续，$F(0)=0$，$F(r)>0$（$r>0$）。若 $\int_0^{r_1}\frac{\mathrm{d}r}{F(r)}<+\infty$，则 $y'=F(\lvert y\rvert)$、$y(0)=0$ 除零解外还有解：$x\le0$ 时取 $0$，$x>0$ 时取由 $x=\int_0^y\frac{\mathrm{d}r}{F(r)}$ 反解出的正函数 $y(x)$。唯一性失去，例 4.3.1（2）就是这种情形。

## 4.4. Peano 存在定理

去掉 Lipschitz 条件、只要求 $f$ 连续时，解仍然存在，只是可能不唯一（例 4.3.1）。Picard 序列此时可能不收敛，需要换一种近似解，并用紧性代替压缩。

### 4.4.1. Euler 折线

沿用 $h=\min\{a,b/M\}$。由 **方向场**的几何意义，最自然的近似解是沿线素走折线。

**定义 4.4.1（Euler 折线）** 把 $[x_0,x_0+h]$ 分成 $n$ 等份，分点 $x_k=x_0+kh/n$。令 $y_0$ 为初值，

$$
y_{k+1}=y_k+f(x_k,y_k)(x_{k+1}-x_k),\qquad k=0,1,\dots,n-1,
$$
依次连接 $(x_0,y_0),(x_1,y_1),\dots,(x_n,y_n)$ 得到的折线 $y=\varphi_n(x)$ 称为初值问题 (4.1) 的 **Euler 折线**。向左同样作出 $[x_0-h,x_0]$ 上的折线。

在每一段 $(x_k,x_{k+1})$ 上 $\varphi_n'(x)=f(x_k,\varphi_n(x_k))$：折线在每个分点沿该点的线素方向出发。这就是数值分析中最简单的 Euler 法。

**引理 4.4.1** Euler 折线 $\varphi_n$ 在 $[x_0,x_0+h]$ 上有定义，且

1. $\lvert\varphi_n(x)-y_0\rvert\le M(x-x_0)\le b$，即折线不离开 $R$；
2. $\lvert\varphi_n(x)-\varphi_n(x')\rvert\le M\lvert x-x'\rvert$；
3. $\varphi_n(x)=y_0+\displaystyle\int_{x_0}^xf(t,\varphi_n(t))\,\mathrm{d}t+\delta_n(x)$，其中 $\delta_n\to0$ 在 $[x_0,x_0+h]$ 上一致成立。

**证明** （1）对 $k$ 归纳：若 $(x_j,y_j)\in R$（$j\le k$），则每段斜率的绝对值不超过 $M$，$\lvert y_{k+1}-y_0\rvert\le M(x_{k+1}-x_0)\le Mh\le b$，$(x_{k+1},y_{k+1})\in R$，$f(x_{k+1},y_{k+1})$ 有定义。（2）折线各段斜率的绝对值不超过 $M$。

（3）记 $g_n(t)=f(x_k,\varphi_n(x_k))$（$x_k\le t<x_{k+1}$），则 $\varphi_n(x)=y_0+\int_{x_0}^xg_n(t)\,\mathrm{d}t$，所以

$$
\delta_n(x)=\int_{x_0}^x\big(g_n(t)-f(t,\varphi_n(t))\big)\,\mathrm{d}t.
$$
$f$ 在有界闭集 $R$ 上**一致连续**：任给 $\varepsilon>0$，有 $\eta>0$，使 $\lvert t-s\rvert<\eta$、$\lvert y-z\rvert<\eta$ 时 $\lvert f(t,y)-f(s,z)\rvert<\varepsilon$。当 $n$ 充分大，使 $\dfrac hn<\eta$ 且 $\dfrac{Mh}n<\eta$ 时，对 $x_k\le t<x_{k+1}$ 有 $\lvert t-x_k\rvert<\eta$，$\lvert\varphi_n(t)-\varphi_n(x_k)\rvert\le M\dfrac hn<\eta$，于是 $\lvert g_n(t)-f(t,\varphi_n(t))\rvert<\varepsilon$，$\lvert\delta_n(x)\rvert\le\varepsilon h$。 $\square$

![初值问题 y' = x + y, y(0) = 0 在 [0, 1] 上的 Euler 折线（n = 2, 4, 8, 16）与精确解 y = e^x - x - 1：折线随 n 增大一致逼近解](./plots/euler-polygons.py)

### 4.4.2. Ascoli 引理

Euler 折线序列不一定收敛（解不唯一时，不同的子序列可以逼近不同的解），但它有收敛的子序列。保证这一点的是函数序列的紧性。

**定义 4.4.2** 设 $\{g_n\}$ 是区间 $I$ 上的函数序列。

1. 若存在常数 $K$，使 $\lvert g_n(x)\rvert\le K$ 对所有 $n$ 和 $x\in I$ 成立，则称 $\{g_n\}$ 在 $I$ 上**一致有界**。
2. 若任给 $\varepsilon>0$，存在与 $n$ 无关的 $\delta>0$，使 $x,x'\in I$、$\lvert x-x'\rvert<\delta$ 时 $\lvert g_n(x)-g_n(x')\rvert<\varepsilon$ 对所有 $n$ 成立，则称 $\{g_n\}$ 在 $I$ 上**等度连续**。

例如满足同一个 Lipschitz 估计 $\lvert g_n(x)-g_n(x')\rvert\le M\lvert x-x'\rvert$ 的序列是等度连续的（取 $\delta=\varepsilon/M$）。

**引理 4.4.2（Ascoli 引理）** 设函数序列 $\{g_n\}$ 在有界闭区间 $I$ 上一致有界且等度连续，则它有在 $I$ 上一致收敛的子序列。

**证明** 第一步：在可数稠密集上收敛。把 $I$ 中的有理点排成一列 $r_1,r_2,\dots$。数列 $\{g_n(r_1)\}$ 有界，由**列紧性定理**有收敛子列 $\{g_{1,n}\}$；$\{g_{1,n}(r_2)\}$ 有界，又可从中选出在 $r_2$ 收敛的子列 $\{g_{2,n}\}$；如此继续，第 $k$ 个子序列 $\{g_{k,n}\}$ 在 $r_1,\dots,r_k$ 都收敛，且是前一个的子序列。取对角线序列 $G_n=g_{n,n}$，它从第 $k$ 项起是 $\{g_{k,n}\}$ 的子序列，所以在每个 $r_k$ 都收敛。

第二步：一致收敛。任给 $\varepsilon>0$，取等度连续性中的 $\delta$。$I$ 有界闭，可以用有限个长度小于 $\delta$ 的子区间覆盖，每个子区间中取一个有理点，得到有限个点 $r_{k_1},\dots,r_{k_N}$，使 $I$ 中每一点到其中某一点的距离小于 $\delta$。由第一步，存在 $N_0$，当 $m,n\ge N_0$ 时 $\lvert G_m(r_{k_j})-G_n(r_{k_j})\rvert<\varepsilon$（$j=1,\dots,N$）。对任意 $x\in I$，取 $\lvert x-r_{k_j}\rvert<\delta$，则

$$
\lvert G_m(x)-G_n(x)\rvert\le\lvert G_m(x)-G_m(r_{k_j})\rvert+\lvert G_m(r_{k_j})-G_n(r_{k_j})\rvert+\lvert G_n(r_{k_j})-G_n(x)\rvert<3\varepsilon.
$$
由一致收敛的 Cauchy 准则，$\{G_n\}$ 在 $I$ 上一致收敛。 $\square$

这个结论在分析中通常称为 Arzelà–Ascoli 定理，是有界闭区间上连续函数空间中"列紧"的刻画。

### 4.4.3. Peano 存在定理

**定理 4.4.1（Peano 存在定理）** 设 $f$ 在矩形 $R$ 上连续，则初值问题 (4.1) 在 $I=[x_0-h,x_0+h]$ 上至少有一个解，$h=\min\{a,b/M\}$。

**证明** 先看右半区间。由引理 4.4.1，Euler 折线序列 $\{\varphi_n\}$ 在 $[x_0,x_0+h]$ 上一致有界（$\lvert\varphi_n\rvert\le\lvert y_0\rvert+b$）且等度连续（共同的 Lipschitz 常数 $M$）。由 Ascoli 引理，有子序列 $\varphi_{n_k}$ 一致收敛到连续函数 $\varphi$，且 $\lvert\varphi(x)-y_0\rvert\le M(x-x_0)\le b$。$f$ 在 $R$ 上一致连续，所以 $f(t,\varphi_{n_k}(t))$ 一致收敛到 $f(t,\varphi(t))$；又 $\delta_{n_k}\to0$ 一致成立。在

$$
\varphi_{n_k}(x)=y_0+\int_{x_0}^xf(t,\varphi_{n_k}(t))\,\mathrm{d}t+\delta_{n_k}(x)
$$
中令 $k\to\infty$，得到 $\varphi$ 满足积分方程 (4.2)，由引理 4.1.1 是右半区间上的解。同理在左半区间上得到解；两者在 $x_0$ 处都取值 $y_0$，拼起来的函数在整个 $I$ 上满足 (4.2)，因而是 (4.1) 的解。 $\square$

**推论 4.4.1** 在定理 4.4.1 的条件下，若初值问题 (4.1) 在 $I$ 上的解唯一，则整个 Euler 折线序列一致收敛到这个解。

**证明** 若不然，存在 $\varepsilon>0$ 和子序列 $\varphi_{n_k}$，使 $\max_I\lvert\varphi_{n_k}-\varphi\rvert\ge\varepsilon$。对这个子序列再用 Ascoli 引理，它有一致收敛的子序列，按定理的证明其极限是 (4.1) 的解，由唯一性就是 $\varphi$，矛盾。 $\square$

所以在 Lipschitz 条件下，Euler 法是收敛的数值方法；没有唯一性时，Euler 折线的不同子序列可能逼近不同的解。

## 小结

| 定理 | 条件 | 结论 | 方法 |
|---|---|---|---|
| Picard 定理（定理 4.2.1） | $f$ 连续，关于 $y$ 满足 Lipschitz 条件 | 在 $[x_0-h,x_0+h]$ 上存在唯一 | 逐次逼近，Weierstrass 判别法 |
| Osgood 定理（定理 4.3.1） | $f$ 连续，满足 Osgood 条件 | 过每点至多一个解 | 反证，比较 $\int\frac{\mathrm{d}r}{F(r)}$ |
| Peano 定理（定理 4.4.1） | $f$ 连续 | 在 $[x_0-h,x_0+h]$ 上存在 | Euler 折线，Ascoli 引理 |

三个定理的结论都是局部的：$h=\min\{a,b/M\}$ 可能远小于解的实际存在区间。下一章用延伸定理把局部解延伸为最大存在区间上的解，并用比较定理估计这个区间。
