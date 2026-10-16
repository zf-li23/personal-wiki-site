---
title: 波动方程
source_hash: 6392ea2f7fa7
---

**波动方程** $u_{tt}=c^2\Delta u$（[2.5.1](/2.5.1#sec-1.2.1)）是双曲型方程的原型。在一维情形它可以完全解出：每个解都是两个以速度 $c$ 反向传播的波之和，d'Alembert 公式用初始位移和初始速度显式地写出初值问题的解。从这个公式可以读出双曲型方程的基本特征：信息沿特征线 $x\pm ct=\text{常数}$ 以有限速度传播，解在一点的值只依赖于一个有界区间上的数据，数据的奇性既不被光滑化、也不被放大，而是沿特征线传下去。边界用反射法处理，非齐次项用齐次化原理处理，能量守恒给出唯一性与稳定性，因此问题是适定的。在三维情形，球面平均法导出 Kirchhoff 公式；在二维情形，降维法导出 Poisson 公式。两者的比较揭示了一个显著差别：三维中尖锐的信号保持尖锐（Huygens 原理），二维中则留下拖尾。两端固定的有限弦在两端反射形成驻波，在 [2.5.4](/2.5.4) 中用分离变量法处理；[2.5.6](/2.5.6) 还会用 Fourier 变换给出另一种解法。

## 3.1. 无界弦：d'Alembert 公式

### 3.1.1. 通解

一维波动算子可以分解为两个输运算子之积：

$$
u_{tt}-c^2u_{xx}=\Big(\frac{\partial}{\partial t}-c\frac{\partial}{\partial x}\Big)\Big(\frac{\partial}{\partial t}+c\frac{\partial}{\partial x}\Big)u.
$$
每个因子都是沿一族特征线的**方向导数**，因此可以期望解由输运方程的解 $f(x-ct)$ 与 $g(x+ct)$（[2.5.2](/2.5.2#sec-2.1)）组成。

**定理 3.1.1** 方程 $u_{tt}=c^2u_{xx}$ 的每个解 $u\in C^2(\mathbb{R}^2)$ 都具有形式

$$
u(x,t)=F(x+ct)+G(x-ct)\tag{3.1}
$$
其中 $F,G\in C^2(\mathbb{R})$；反之，每个这样的函数都是解。

**证明** 引入特征坐标 $\xi=x+ct$，$\eta=x-ct$，记 $u(x,t)=w(\xi,\eta)$。由链式法则，$u_x=w_\xi+w_\eta$，$u_t=c(w_\xi-w_\eta)$，且

$$
u_{xx}=w_{\xi\xi}+2w_{\xi\eta}+w_{\eta\eta},\qquad u_{tt}=c^2\big(w_{\xi\xi}-2w_{\xi\eta}+w_{\eta\eta}\big),
$$
故 $u_{tt}-c^2u_{xx}=-4c^2w_{\xi\eta}$，这就是 [2.5.1](/2.5.1#thm-1.5.2) 的标准形。于是 $w_{\xi\eta}=0$，与 [2.5.1](/2.5.1#sec-1.1.2) 中一样得 $w=F(\xi)+G(\eta)$。反之可直接验证。$\square$

$G(x-ct)$ 是以速度 $c$ 向右平移、形状不变的波，$F(x+ct)$ 则向左平移；这样的解称为**行波解**。所以 $c$ 确实是传播速度，正如 [2.5.1](/2.5.1#sec-1.2.1) 所说。

### 3.1.2. d'Alembert 公式

**定理 3.1.2（d'Alembert 公式）** 设 $\varphi\in C^2(\mathbb{R})$，$\psi\in C^1(\mathbb{R})$。初值问题

$$
u_{tt}=c^2u_{xx},\quad x\in\mathbb{R},\ t>0,\qquad u(x,0)=\varphi(x),\quad u_t(x,0)=\psi(x)\tag{3.2}
$$
有唯一的解 $u\in C^2(\mathbb{R}\times[0,+\infty))$，它由下式给出：

$$
u(x,t)=\frac12\big[\varphi(x+ct)+\varphi(x-ct)\big]+\frac{1}{2c}\int_{x-ct}^{x+ct}\psi(s)\,\mathrm{d}s.\tag{3.3}
$$

**证明** 由定理 3.1.1（其证明在半平面 $t\ge0$ 上同样成立），任一解都具有形式 $u=F(x+ct)+G(x-ct)$。初始条件要求

$$
F(x)+G(x)=\varphi(x),\qquad c\big(F'(x)-G'(x)\big)=\psi(x).
$$
将第二式从 $0$ 到 $x$ 积分，得 $F(x)-G(x)=\frac1c\int_0^x\psi(s)\,\mathrm{d}s+K$，$K$ 为常数，因此

$$
F(x)=\frac12\varphi(x)+\frac{1}{2c}\int_0^x\psi\,\mathrm{d}s+\frac K2,\qquad G(x)=\frac12\varphi(x)-\frac{1}{2c}\int_0^x\psi\,\mathrm{d}s-\frac K2.
$$
把 $x+ct$ 代入 $F$、$x-ct$ 代入 $G$ 后相加，常数抵消，即得式 (3.3)。所以任何解都必须由式 (3.3) 给出，这就证明了唯一性。反之，在所给的正则性下，式 (3.3) 定义了形如 (3.1) 的 $C^2$ 函数，因而是解，并且满足 $u(x,0)=\varphi(x)$ 与 $u_t(x,0)=\frac12\big[c\varphi'(x)-c\varphi'(x)\big]+\frac{1}{2c}\big[c\psi(x)+c\psi(x)\big]=\psi(x)$。$\square$

这个公式的含义很直观：初始位移分成两半，分别向两侧传播；初始速度的贡献是 $\psi$ 在区间 $[x-ct,x+ct]$ 上的平均值乘以 $t$。

**例 3.1.1** 求解问题 (3.2)，其中 $\varphi(x)=x^2$，$\psi(x)=\sin x$。

**解** 由式 (3.3)，

$$
u=\frac12\big[(x+ct)^2+(x-ct)^2\big]+\frac{1}{2c}\big[\cos(x-ct)-\cos(x+ct)\big]=x^2+c^2t^2+\frac1c\sin x\,\sin ct.
$$
验证：$u_{tt}=2c^2-c\sin x\sin ct=c^2u_{xx}$。

**例 3.1.2（拨动的弦）** 设 $\psi=0$，$\varphi$ 是 $[-a,a]$ 上高为 $h$ 的三角形：$\lvert x\rvert\le a$ 时 $\varphi(x)=h(1-\lvert x\rvert/a)$，其余处为 $0$。则 $u=\frac12[\varphi(x+ct)+\varphi(x-ct)]$：三角形分裂成两个高为 $h/2$ 的三角形，相背而行；在 $t=a/c$ 时刻二者完全分离，此后两者之间的弦保持静止。

**例 3.1.3（锤击的弦）** 设 $\varphi=0$，在 $(-a,a)$ 上 $\psi=1$，其余处 $\psi=0$（锤子击打弦段 $(-a,a)$）。则

$$
u(x,t)=\frac{1}{2c}\,\big\lvert(x-ct,x+ct)\cap(-a,a)\big\rvert,
$$
其中 $\lvert\cdot\rvert$ 表示区间的长度。当 $t>a/c$ 时，弦的形状是高为 $a/c$ 的梯形，其平顶 $\lvert x\rvert<ct-a$ 以速度 $c$ 向两侧扩展：与拨动的弦不同，被击打的弦不会回到静止位置，而是产生永久位移。

![d'Alembert 公式。左：拨动的弦分裂为两个半高的脉冲。右：左端 x = 0 固定的半无界弦上，脉冲反射后上下翻转（奇延拓）](./plots/dalembert-reflection.py)

这两个例子中的数据都不是 $C^2$ 的（三角形有尖角，速度有跳跃），因此式 (3.3) 不是古典解，而是广义解：它是光滑化数据所对应古典解的一致极限，也是积分意义下的解。这两个例子说明了奇性的去向：三角形的尖角沿着 $t=0$ 时过尖角的特征线传播。对波动方程，数据的奇性会保持下来并沿特征线传播；与之相反，热方程会瞬间把奇性抹平（[2.5.4](/2.5.4#sec-4.2)）。

### 3.1.3. 依赖区间、决定区域与影响区域

式 (3.3) 表明，$u(x_0,t_0)$ 只依赖于 $\varphi$ 在两点 $x_0\pm ct_0$ 处的值，以及 $\psi$ 在这两点之间的区间上的值。

**定义 3.1.1（依赖区间、决定区域与影响区域）** 对波动方程 $u_{tt}=c^2u_{xx}$：

1. $x$ 轴上的区间 $[x_0-ct_0,x_0+ct_0]$ 称为点 $(x_0,t_0)$ 的**依赖区间**；
2. 对区间 $[a,b]$，由特征线 $x-ct=a$ 与 $x+ct=b$ 围成的三角形 $\{(x,t)\colon a+ct\le x\le b-ct,\ t\ge0\}$ 称为 $[a,b]$ 的**决定区域**；
3. 区域 $\{(x,t)\colon a-ct\le x\le b+ct,\ t\ge0\}$ 称为 $[a,b]$ 的**影响区域**。

无论 $[a,b]$ 以外的数据如何，$[a,b]$ 上的数据完全决定了解在决定区域内的值；而 $[a,b]$ 上的数据只能影响解在其影响区域内的值。特别地，若 $\varphi$、$\psi$ 在 $[a,b]$ 以外为零，则当 $x>b+ct$ 或 $x<a-ct$ 时 $u(x,t)=0$：扰动传播的速度不超过 $c$。这种有限传播速度（finite speed of propagation）是双曲型方程的标志。

![左：(x₀, t₀) 的依赖区间是特征三角形的底边。中：[a, b] 的决定区域。右：[a, b] 的影响区域，以特征线 x = a - ct 与 x = b + ct 为界](./plots/dependence-influence.py)

## 3.2. 半无界弦与反射法

### 3.2.1. 固定端

现在设弦占据 $x\ge0$，端点 $x=0$ 固定：

$$
\begin{cases}u_{tt}=c^2u_{xx},&x>0,\ t>0,\\u(0,t)=0,&t\ge0,\\u(x,0)=\varphi(x),\quad u_t(x,0)=\psi(x),&x\ge0.\end{cases}\tag{3.4}
$$
思路是把数据延拓到整条直线上，使延拓后问题的解在 $x=0$ 处自动为零。取**奇延拓**

$$
\varphi_{\mathrm{o}}(x)=\begin{cases}\varphi(x),&x\ge0,\\-\varphi(-x),&x<0,\end{cases}\qquad\psi_{\mathrm{o}}(x)=\begin{cases}\psi(x),&x\ge0,\\-\psi(-x),&x<0.\end{cases}
$$
若 $u$ 是奇数据初值问题的解，则 $-u(-x,t)$ 也是；由唯一性，$u(-x,t)=-u(x,t)$，特别地 $u(0,t)=0$。对 $\varphi_{\mathrm{o}},\psi_{\mathrm{o}}$ 应用 d'Alembert 公式，再改用 $\varphi,\psi$ 表示（当 $x<ct$ 时，积分在 $[x-ct,ct-x]$ 上的部分由奇性相互抵消），得到下面的结果。

**定理 3.2.1** 设 $\varphi\in C^2[0,+\infty)$，$\psi\in C^1[0,+\infty)$，并满足相容性条件 $\varphi(0)=\varphi''(0)=\psi(0)=0$。则问题 (3.4) 有唯一的 $C^2$ 解：

$$
u(x,t)=\begin{cases}\dfrac12\big[\varphi(x+ct)+\varphi(x-ct)\big]+\dfrac{1}{2c}\displaystyle\int_{x-ct}^{x+ct}\psi(s)\,\mathrm{d}s,&x\ge ct,\\[2ex]\dfrac12\big[\varphi(x+ct)-\varphi(ct-x)\big]+\dfrac{1}{2c}\displaystyle\int_{ct-x}^{x+ct}\psi(s)\,\mathrm{d}s,&0\le x<ct.\end{cases}\tag{3.5}
$$

相容性条件恰好保证奇延拓分别是 $C^2$ 与 $C^1$ 的：函数的奇延拓在 $0$ 处连续，当且仅当函数在 $0$ 处为零；此时一阶导数自动连续，但二阶导数是奇函数，只有 $\varphi''(0)=0$ 时才在 $0$ 处连续。（这些条件也是必要的：$u(0,t)=0$ 对所有 $t$ 成立，迫使 $u_{tt}(0,t)=0$，从而 $c^2\varphi''(0)=u_{tt}(0,0)=0$。）

在区域 $x\ge ct$ 内，过 $(x,t)$ 的特征线还没有到达边界，端点不起作用。当 $x<ct$ 时，项 $-\frac12\varphi(ct-x)$ 是在 $x=0$ 处反射回来的左行波：固定端使脉冲反射后反号，如 §3.1.2 图的右半部分所示。

### 3.2.2. 自由端

若端点可以自由滑动（$u_x(0,t)=0$，即 Neumann 条件，[2.5.1](/2.5.1#sec-1.3.2)），则 $\varphi,\psi$ 的**偶延拓**给出关于 $x$ 的偶函数解，因而 $u_x(0,t)=0$。当 $0\le x<ct$ 时得

$$
u(x,t)=\frac12\big[\varphi(x+ct)+\varphi(ct-x)\big]+\frac{1}{2c}\Big[\int_0^{x+ct}\psi(s)\,\mathrm{d}s+\int_0^{ct-x}\psi(s)\,\mathrm{d}s\Big],\tag{3.6}
$$
相容性条件为 $\varphi'(0)=\psi'(0)=0$。在自由端，脉冲反射后符号不变。

### 3.2.3. 有限弦

对两端固定的弦 $0\le x\le l$，数据在两端都要反射：把 $\varphi$ 和 $\psi$ 分别关于 $x=0$ 与 $x=l$ 作奇延拓，得到以 $2l$ 为周期的奇函数。对延拓后的数据应用 d'Alembert 公式即得问题的解。由于延拓后的数据以 $2l$ 为周期，解关于时间是周期的，周期为 $2l/c$：脉冲传到一端，反射，传到另一端，再反射，最后恢复原来的形状。[2.5.4](/2.5.4#sec-4.1) 把同一个解写成**正弦级数**。

## 3.3. 非齐次方程：齐次化原理

考虑受外力驱动的弦：

$$
u_{tt}=c^2u_{xx}+f(x,t),\quad x\in\mathbb{R},\ t>0,\qquad u(x,0)=\varphi(x),\quad u_t(x,0)=\psi(x).\tag{3.7}
$$
由**叠加原理**，$u=u_1+u_2$，其中 $u_1$ 是带给定数据的齐次方程的解（d'Alembert 公式），$u_2$ 是零数据下式 (3.7) 的解。第二个问题可以用下面的想法化为第一个：在短时间 $[s,s+\mathrm{d}s]$ 内作用的外力使弦的速度改变 $f(x,s)\,\mathrm{d}s$，而不改变位置；此后这一速度作为自由波传播。解就是所有这些自由波的叠加。

**定理 3.3.1（Duhamel 原理）** 设对每个 $s\ge0$，函数 $w(x,t;s)$ 是齐次问题

$$
w_{tt}=c^2w_{xx}\ \ (t>s),\qquad w(x,s;s)=0,\qquad w_t(x,s;s)=f(x,s)
$$
的解，并且 $w$、$w_t$、$w_{tt}$、$w_{xx}$ 关于 $(x,t,s)$ 连续。则

$$
u(x,t)=\int_0^tw(x,t;s)\,\mathrm{d}s\tag{3.8}
$$
满足 $u_{tt}=c^2u_{xx}+f$ 及 $u(x,0)=u_t(x,0)=0$。

**证明** 对变上限积分**积分号下求导**，并利用 $w(x,t;t)=0$，

$$
u_t=w(x,t;t)+\int_0^tw_t(x,t;s)\,\mathrm{d}s=\int_0^tw_t(x,t;s)\,\mathrm{d}s.
$$
再求导一次，利用 $w_t(x,t;t)=f(x,t)$，

$$
u_{tt}=f(x,t)+\int_0^tw_{tt}(x,t;s)\,\mathrm{d}s=f(x,t)+c^2\int_0^tw_{xx}(x,t;s)\,\mathrm{d}s=f(x,t)+c^2u_{xx}.
$$
显然 $u(x,0)=0$，由第一个式子知 $u_t(x,0)=0$。$\square$

由 d'Alembert 公式（以 $s$ 为时间起点），$w(x,t;s)=\frac{1}{2c}\int_{x-c(t-s)}^{x+c(t-s)}f(y,s)\,\mathrm{d}y$。再加上齐次问题的解，就得到式 (3.7) 的完整解。

**定理 3.3.2** 设 $\varphi\in C^2(\mathbb{R})$，$\psi\in C^1(\mathbb{R})$，$f$ 与 $f_x$ 连续。问题 (3.7) 的唯一 $C^2$ 解为

$$
u(x,t)=\frac12\big[\varphi(x+ct)+\varphi(x-ct)\big]+\frac{1}{2c}\int_{x-ct}^{x+ct}\psi(y)\,\mathrm{d}y+\frac{1}{2c}\iint_{\Delta(x,t)}f(y,s)\,\mathrm{d}y\,\mathrm{d}s,\tag{3.9}
$$
其中 $\Delta(x,t)=\{(y,s)\colon0\le s\le t,\ \lvert y-x\rvert\le c(t-s)\}$ 是以 $(x,t)$ 为顶点的特征三角形。

现在依赖区域是整个特征三角形：解在 $(x,t)$ 处只感受到这样一些点上的外力——从这些点出发、速度不超过 $c$ 的信号能够到达 $(x,t)$。唯一性由 §3.4 的能量法得到。

**例 3.3.1** 求解 $u_{tt}=c^2u_{xx}+\sin x$，$u(x,0)=u_t(x,0)=0$。

**解** 由式 (3.9)，

$$
u=\frac{1}{2c}\int_0^t\Big[\cos\big(x-c(t-s)\big)-\cos\big(x+c(t-s)\big)\Big]\,\mathrm{d}s=\frac{\sin x}{c}\int_0^t\sin c(t-s)\,\mathrm{d}s=\frac{\sin x\,(1-\cos ct)}{c^2}.
$$
验证：$u_{tt}=\sin x\cos ct$，$c^2u_{xx}+\sin x=-\sin x\,(1-\cos ct)+\sin x=\sin x\cos ct$。弦围绕静态挠度 $\frac{\sin x}{c^2}$ 振动，后者满足 $c^2u_{xx}+\sin x=0$。

## 3.4. 能量与唯一性

### 3.4.1. 能量守恒

设弦的线密度为 $\rho$，张力为 $T=\rho c^2$。小段 $[x,x+\mathrm{d}x]$ 的动能为 $\frac12\rho u_t^2\,\mathrm{d}x$，势能（克服张力把长度从 $\mathrm{d}x$ 拉长到 $\sqrt{1+u_x^2}\,\mathrm{d}x\approx(1+\frac12u_x^2)\,\mathrm{d}x$ 所做的功）为 $\frac12Tu_x^2\,\mathrm{d}x$。除以 $\rho$，定义解在区间 $I$ 上的能量为

$$
E(t)=\frac12\int_I\big(u_t^2+c^2u_x^2\big)\,\mathrm{d}x.\tag{3.10}
$$

**定理 3.4.1（能量守恒）** 设 $u\in C^2([0,l]\times[0,T])$ 满足 $u_{tt}=c^2u_{xx}$，且在每个端点满足 Dirichlet 条件 $u=0$ 或 Neumann 条件 $u_x=0$。则 $E(t)=\frac12\int_0^l(u_t^2+c^2u_x^2)\,\mathrm{d}x$ 是常数。在 $I=\mathbb{R}$ 上，若解在每个时刻当 $\lvert x\rvert$ 充分大时为零（例如 $\varphi$、$\psi$ 的支集有界），结论同样成立。

**证明** 积分号下求导，利用方程并分部积分，

$$
E'(t)=\int_0^l\big(u_tu_{tt}+c^2u_xu_{xt}\big)\,\mathrm{d}x=c^2\int_0^l\big(u_tu_{xx}+u_xu_{xt}\big)\,\mathrm{d}x=c^2\int_0^l\big(u_tu_x\big)_x\,\mathrm{d}x=c^2\Big[u_tu_x\Big]_{x=0}^{x=l}.
$$
在 Dirichlet 端，$u=0$ 对所有 $t$ 成立，故 $u_t=0$；在 Neumann 端，$u_x=0$。两种情形下边界项都为零。在 $\mathbb{R}$ 上，由于每个时刻 $u$ 在某个有界集之外为零（由有限传播速度），边界项也为零。$\square$

对 Robin 端 $u_x(l,t)+\alpha u(l,t)=0$（$\alpha>0$），边界项为 $c^2u_tu_x=-\frac{c^2\alpha}{2}\frac{\mathrm{d}}{\mathrm{d}t}u(l,t)^2$，因此守恒量是 $E(t)+\frac{c^2\alpha}{2}u(l,t)^2$，即弦的能量加上弹簧的势能。

**定理 3.4.2（唯一性）** 初边值问题

$$
u_{tt}=c^2u_{xx}+f,\quad0<x<l,\qquad u(x,0)=\varphi(x),\quad u_t(x,0)=\psi(x),
$$
在每个端点附加 Dirichlet、Neumann 或 Robin（$\alpha>0$）条件，至多有一个解 $u\in C^2([0,l]\times[0,T])$。

**证明** 两个解之差 $w$ 满足齐次方程、齐次边界条件和零初始数据。它的能量（Robin 情形加上弹簧项）守恒，且在 $t=0$ 时为 $0$。由于能量是非负项之和，$w_t\equiv0$，$w_x\equiv0$，故 $w$ 为常数，再由 $w(x,0)=0$ 得 $w\equiv0$。$\square$

这就是能量法（energy method）：要证明唯一性，就找一个初始为零且不增的非负量。

### 3.4.2. 收缩区间上的能量

对整条直线上的初值问题，不对数据作任何衰减假设，能量论证的局部形式能同时给出唯一性与有限传播速度。

**定理 3.4.3** 设 $u\in C^2$ 满足 $u_{tt}=c^2u_{xx}$，固定 $(x_0,t_0)$，$t_0>0$。则收缩区间上的能量

$$
e(t)=\frac12\int_{x_0-c(t_0-t)}^{x_0+c(t_0-t)}\big(u_t^2+c^2u_x^2\big)\,\mathrm{d}x,\qquad0\le t\le t_0,
$$
不增。特别地，若在依赖区间 $[x_0-ct_0,x_0+ct_0]$ 上 $\varphi=\psi=0$，则在以 $(x_0,t_0)$ 为顶点的整个特征三角形内 $u=0$。

**证明** 记 $\alpha(t)=x_0-c(t_0-t)$，$\beta(t)=x_0+c(t_0-t)$，则 $\alpha'=c$，$\beta'=-c$。对变限积分求导，并像定理 3.4.1 那样分部积分，

$$
e'(t)=c^2\Big[u_tu_x\Big]_\alpha^\beta-\frac c2\big(u_t^2+c^2u_x^2\big)\Big|_{\beta}-\frac c2\big(u_t^2+c^2u_x^2\big)\Big|_{\alpha}=-\frac c2\big(u_t-cu_x\big)^2\Big|_{\beta}-\frac c2\big(u_t+cu_x\big)^2\Big|_{\alpha}\le0.
$$
若数据在底边上为零，则 $e(0)=0$，从而 $0\le t\le t_0$ 时 $e(t)=0$；于是三角形内 $u_t=u_x=0$，$u$ 为常数，等于它在底边上的值 $0$。$\square$

把定理 3.4.3 应用于两个解之差，可知初值问题 (3.2) 的解无需任何无穷远条件就是唯一的，而且特征三角形内的值由其底边上的数据决定。同样的论证适用于变系数方程和高维情形（用锥代替三角形），那里没有显式公式可用；这正是能量估计成为双曲型方程理论基本工具的原因。

### 3.4.3. 连续依赖性

**定理 3.4.4** 设 $u_1,u_2$ 分别是初值问题 (3.2) 以 $(\varphi_1,\psi_1)$ 与 $(\varphi_2,\psi_2)$ 为数据的解。则当 $0\le t\le T$ 时，

$$
\sup_{x}\lvert u_1(x,t)-u_2(x,t)\rvert\le\sup_x\lvert\varphi_1-\varphi_2\rvert+T\sup_x\lvert\psi_1-\psi_2\rvert.
$$

**证明** $u_1-u_2$ 是问题 (3.2) 以 $(\varphi_1-\varphi_2,\psi_1-\psi_2)$ 为数据的解，对它应用 d'Alembert 公式：第一项不超过 $\sup\lvert\varphi_1-\varphi_2\rvert$，积分项不超过 $\frac{1}{2c}\cdot2ct\sup\lvert\psi_1-\psi_2\rvert$。$\square$

结合定理 3.1.2，这说明一维波动方程的初值问题在任何有限时间区间上都是适定的（[2.5.1](/2.5.1#def-1.4.1)）。在高维情形，能量

$$
E(t)=\frac12\iiint_{\mathbb{R}^3}\big(u_t^2+c^2\lvert\nabla u\rvert^2\big)\,\mathrm{d}V
$$
由同样的计算可知守恒，只是把分部积分换成 **Green 第一公式**（[2.2.14](/2.2.14#thm-14.5.2)），由此得到有界区域上初边值问题的唯一性。

## 3.5. 三维与二维的波

### 3.5.1. 球面平均与 Kirchhoff 公式

在三维情形无法分解波动算子，但可以通过在球面上取平均把问题化为一维。对 $\mathbb{R}^3$ 上的连续函数 $g$、点 $x$ 与 $r>0$，球面平均（spherical mean）定义为

$$
M_g(x,r)=\frac{1}{4\pi r^2}\iint_{\lvert y-x\rvert=r}g(y)\,\mathrm{d}S_y=\frac{1}{4\pi}\iint_{\lvert\omega\rvert=1}g(x+r\omega)\,\mathrm{d}S_\omega,
$$
即 $g$ 在以 $x$ 为球心、$r$ 为半径的球面上的平均值。当 $r\to0$ 时，$M_g(x,r)\to g(x)$。

**引理 3.5.1** 设 $u\in C^2$ 在 $\mathbb{R}^3\times\mathbb{R}$ 中满足 $u_{tt}=c^2\Delta u$，对固定的 $x$ 记 $M(r,t)=M_{u(\cdot,t)}(x,r)$。则

$$
M_{tt}=c^2\Big(M_{rr}+\frac2rM_r\Big),\tag{3.11}
$$
从而 $v(r,t)=rM(r,t)$ 在 $r>0$ 上满足一维波动方程 $v_{tt}=c^2v_{rr}$，且 $v(0,t)=0$。

**证明** 对平均值的第二种写法积分号下求导，并在球 $B_r=\{\lvert y-x\rvert<r\}$ 上应用 **Gauss 公式**，

$$
M_r=\frac1{4\pi}\iint_{\lvert\omega\rvert=1}\nabla u(x+r\omega)\cdot\omega\,\mathrm{d}S_\omega=\frac{1}{4\pi r^2}\iint_{\partial B_r}\frac{\partial u}{\partial\boldsymbol{n}}\,\mathrm{d}S=\frac{1}{4\pi r^2}\iiint_{B_r}\Delta u\,\mathrm{d}V=\frac{1}{4\pi c^2r^2}\iiint_{B_r}u_{tt}\,\mathrm{d}V.
$$
于是 $r^2M_r=\frac{1}{4\pi c^2}\int_0^r\Big(\iint_{\lvert y-x\rvert=\rho}u_{tt}\,\mathrm{d}S\Big)\mathrm{d}\rho$，对 $r$ 求导，

$$
\big(r^2M_r\big)_r=\frac{1}{4\pi c^2}\iint_{\lvert y-x\rvert=r}u_{tt}\,\mathrm{d}S=\frac{r^2}{c^2}M_{tt},
$$
这就是式 (3.11)。最后 $v_{rr}=rM_{rr}+2M_r$，故式 (3.11) 乘以 $r$ 即 $v_{tt}=c^2v_{rr}$；又因 $M$ 在 $r=0$ 附近有界，$v(0,t)=0$。$\square$

式 (3.11) 是径向函数的波动方程：$M_{rr}+\frac2rM_r$ 正是径向函数的 Laplace 算子在**球坐标**下的表达式（[2.2.14](/2.2.14#sec-14.6)）。

**定理 3.5.1（Kirchhoff 公式）** 设 $\varphi\in C^3(\mathbb{R}^3)$，$\psi\in C^2(\mathbb{R}^3)$。问题

$$
u_{tt}=c^2\Delta u,\quad x\in\mathbb{R}^3,\ t>0,\qquad u(x,0)=\varphi(x),\quad u_t(x,0)=\psi(x)
$$
的解为

$$
u(x,t)=\frac{\partial}{\partial t}\bigg(\frac{1}{4\pi c^2t}\iint_{\lvert y-x\rvert=ct}\varphi(y)\,\mathrm{d}S_y\bigg)+\frac{1}{4\pi c^2t}\iint_{\lvert y-x\rvert=ct}\psi(y)\,\mathrm{d}S_y.\tag{3.12}
$$

**证明**（推导。）固定 $x$，按引理 3.5.1 令 $v=rM$。则 $v$ 在半直线 $r>0$ 上满足波动方程，$r=0$ 为固定端，初始数据为 $v(r,0)=rM_\varphi(x,r)$，$v_t(r,0)=rM_\psi(x,r)$。由反射公式 (3.5)，当 $0\le r<ct$ 时，

$$
v(r,t)=\frac12\Big[(ct+r)M_\varphi(x,ct+r)-(ct-r)M_\varphi(x,ct-r)\Big]+\frac1{2c}\int_{ct-r}^{ct+r}\rho\,M_\psi(x,\rho)\,\mathrm{d}\rho.
$$
而 $u(x,t)=\lim_{r\to0}M(r,t)=\lim_{r\to0}\frac{v(r,t)}{r}=v_r(0,t)$，在 $r=0$ 处求导，

$$
u(x,t)=\frac{\mathrm{d}}{\mathrm{d}\rho}\big[\rho M_\varphi(x,\rho)\big]_{\rho=ct}+t\,M_\psi(x,ct)=\frac{\partial}{\partial t}\big[t\,M_\varphi(x,ct)\big]+t\,M_\psi(x,ct).
$$
由于 $tM_g(x,ct)=\frac{1}{4\pi c^2t}\iint_{\lvert y-x\rvert=ct}g\,\mathrm{d}S$，这就是式 (3.12)。可以直接验证，在所给假设下式 (3.12) 定义了一个 $C^2$ 解。$\square$

例如 $\varphi=0$，$\psi\equiv1$ 给出 $u=\frac{4\pi c^2t^2}{4\pi c^2t}=t$，与预期一致。注意正则性的损失：要得到 $u\in C^2$ 需要 $\varphi\in C^3$，因为第一项含球面平均的导数。与一维不同，三维中数据的奇性可能被聚焦而变强。

Kirchhoff 公式最引人注目的特点是：$u(x,t)$ 只依赖于球面 $\lvert y-x\rvert=ct$ 上的数据，与球面内部的数据无关。设数据在一个半径为 $a$ 的球外为零，球心与 $x$ 的距离为 $R>a$。当 $t<(R-a)/c$ 时，球面尚未到达这个球，$u(x,t)=0$；当 $t>(R+a)/c$ 时，球面已经越过它，$u(x,t)$ 又为零。尖锐的信号以清晰的前沿到达，又以清晰的后沿离开。这就是（强形式的）Huygens 原理（Huygens' principle），也正是三维空间中的声音能不失真地传递语言和音乐的原因。

**例 3.5.1** 设 $\varphi=0$，在球 $\lvert y\rvert<a$ 内 $\psi=1$，球外 $\psi=0$。在球心处，当 $ct<a$ 时球面 $\lvert y\rvert=ct$ 位于球内，当 $ct>a$ 时位于球外，故

$$
u(0,t)=\begin{cases}t,&0<t<a/c,\\0,&t>a/c.\end{cases}
$$
球心以单位速度上升，然后在 $t=a/c$ 时刻——来自球面边界的波到达之时——突然停止并回到平衡位置。（解不连续是因为数据不连续；数据光滑时解也光滑。）

### 3.5.2. 降维法：二维情形

二维波动方程的解可以看作不依赖于 $x_3$ 的三维方程的解。对这样的数据应用 Kirchhoff 公式，并把球面 $\lvert y-x\rvert=ct$ 投影到平面上：每个半球面都是圆盘 $\lvert y-x\rvert\le ct$ 上某个函数的图像，面积元为 $\mathrm{d}S=\frac{ct}{\sqrt{c^2t^2-\lvert y-x\rvert^2}}\,\mathrm{d}y$。两个半球面合起来给出下面的公式；这就是 Hadamard 的降维法（method of descent）。

**定理 3.5.2（二维 Poisson 公式）** 设 $\varphi\in C^3(\mathbb{R}^2)$，$\psi\in C^2(\mathbb{R}^2)$。问题 $u_{tt}=c^2(u_{x_1x_1}+u_{x_2x_2})$，$u(x,0)=\varphi(x)$，$u_t(x,0)=\psi(x)$ 的解为

$$
u(x,t)=\frac{\partial}{\partial t}\bigg(\frac{1}{2\pi c}\iint_{\lvert y-x\rvert<ct}\frac{\varphi(y)\,\mathrm{d}y}{\sqrt{c^2t^2-\lvert y-x\rvert^2}}\bigg)+\frac{1}{2\pi c}\iint_{\lvert y-x\rvert<ct}\frac{\psi(y)\,\mathrm{d}y}{\sqrt{c^2t^2-\lvert y-x\rvert^2}}.\tag{3.13}
$$

现在 $(x,t)$ 的依赖区域是整个圆盘 $\lvert y-x\rvert\le ct$，而不只是它的边界。局部的扰动仍以清晰的前沿在 $t=(R-a)/c$ 时到达，但永远不会完全停止。

**例 3.5.2** 设 $\varphi=0$，在圆盘 $\lvert y\rvert<a$ 内 $\psi=1$，圆盘外 $\psi=0$。在圆心处，用极坐标计算，

$$
u(0,t)=\frac{1}{2\pi c}\int_0^{b}\frac{2\pi r\,\mathrm{d}r}{\sqrt{c^2t^2-r^2}}=\frac1c\Big(ct-\sqrt{c^2t^2-b^2}\Big),\qquad b=\min(ct,a).
$$
当 $ct<a$ 时它等于 $t$，与三维相同；但当 $ct>a$ 时它等于 $t-\sqrt{t^2-a^2/c^2}\approx\frac{a^2}{2c^2t}$，只按 $1/t$ 衰减。这就像向池塘里投入石子后的涟漪：主波过去很久之后，水面仍在颤动。Huygens 原理在奇数维 $n\ge3$ 中成立，在所有偶数维中都不成立；在一维中，例 3.1.3 中被击打的弦是永久位移这一极端情形。

![距半径 a = 1 的区域 R = 3 处一点的响应，该区域被赋予单位初速度（c = 1）。三维中信号限于 R - a < t < R + a（Huygens 原理）；二维中有长拖尾；一维中位移是永久的](./plots/huygens-dimensions.py)

## 小结

| 问题 | 公式 | 要点 |
|---|---|---|
| 一维通解 | $u=F(x+ct)+G(x-ct)$ | 两个行波；特征线 $x\pm ct=\text{常数}$ |
| 一维初值问题 | d'Alembert 公式 (3.3) | 依赖区间 $[x-ct,x+ct]$；有限传播速度；奇性沿特征线传播 |
| 半直线 | 奇延拓（固定端）或偶延拓（自由端），式 (3.5)、(3.6) | 反射时反号或不反号；相容性条件 |
| 非齐次项 | 齐次化原理，式 (3.9) | 外力通过特征三角形起作用 |
| 唯一性与稳定性 | 能量 $\frac12\int(u_t^2+c^2u_x^2)$ 守恒；在收缩区间上不增 | 适定性 |
| 三维 | Kirchhoff 公式 (3.12)：球面 $\lvert y-x\rvert=ct$ 上的平均 | Huygens 原理：清晰的前沿与后沿 |
| 二维 | Poisson 公式 (3.13)：圆盘上的加权平均 | 清晰的前沿，缓慢衰减的拖尾 |
