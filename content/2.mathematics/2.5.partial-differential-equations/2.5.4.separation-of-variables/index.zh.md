---
title: 分离变量法
source_hash: 38531a31512d
---

在有界区间上，d'Alembert 公式必须与无穷多次反射结合起来（[2.5.3](/2.5.3#sec-3.2.3)），而热方程和 Laplace 方程根本没有这样的公式。由 Daniel Bernoulli 和 Fourier 提出的分离变量法（separation of variables）则对简单有界区域上的三类经典方程都适用。我们寻找特殊形式 $u=X(x)T(t)$ 的解；方程于是分解为常微分方程，边界条件把关于 $X$ 的方程变成一个**特征值问题**（[2.4.12](/2.4.12#sec-12.4.1)），再把得到的乘积解叠加起来就得到一般解。初始（或边界）数据通过按**特征函数**展开来匹配；对最简单的边界条件，这恰好就是 **Fourier 级数**（[2.2.9](/2.2.9#sec-9.3)）。其物理内容是模态分解：振动的弦是一系列具有离散固有频率的驻波的叠加，冷却的杆是一系列以不同指数速率衰减的温度分布的叠加。本章依次讨论振动的弦，各种边界条件下杆中的热方程，一般方法及其 Sturm–Liouville 理论依据（[2.4.12](/2.4.12#sec-12.5)），非齐次方程与非齐次边界条件，以及矩形和圆盘上的 Laplace 方程——对后者求和级数可得 Poisson 积分公式。柱坐标与球坐标中的同一方法引出 Bessel 函数与 Legendre 多项式，是 [2.5.5](/2.5.5) 的内容；在无界区域上，级数变为 Fourier 积分（[2.5.6](/2.5.6)）。

## 4.1. 两端固定的弦振动

### 4.1.1. 分离变量

考虑长为 $l$、两端固定的弦：

$$
\begin{cases}u_{tt}=c^2u_{xx},&0<x<l,\ t>0,\\u(0,t)=u(l,t)=0,&t\ge0,\\u(x,0)=\varphi(x),\quad u_t(x,0)=\psi(x),&0\le x\le l.\end{cases}\tag{4.1}
$$
方程和边界条件都是线性齐次的，由**叠加原理**，解的和仍是解；初始条件留到最后再处理。寻找形如 $u(x,t)=X(x)T(t)$ 的非零解。代入方程得 $XT''=c^2X''T$，即

$$
\frac{T''(t)}{c^2T(t)}=\frac{X''(x)}{X(x)}.
$$
左边只依赖于 $t$，右边只依赖于 $x$，所以两边等于同一个常数，记为 $-\lambda$。边界条件 $X(0)T(t)=X(l)T(t)=0$ 对所有 $t$ 成立（且 $T\not\equiv0$），给出 $X(0)=X(l)=0$。于是

$$
X''+\lambda X=0,\quad X(0)=X(l)=0;\qquad T''+\lambda c^2T=0.\tag{4.2}
$$
关于 $X$ 的问题就是[例 12.4.1](/2.4.12#sec-12.4.1) 的 Dirichlet 特征值问题：它只在

$$
\lambda_n=\Big(\frac{n\pi}{l}\Big)^2,\qquad X_n(x)=\sin\frac{n\pi x}{l},\qquad n=1,2,\dots
$$
时有非平凡解。对 $\lambda=\lambda_n$，关于 $T$ 的方程给出 $T_n(t)=A_n\cos\frac{n\pi ct}{l}+B_n\sin\frac{n\pi ct}{l}$。把所有乘积解叠加，

$$
u(x,t)=\sum_{n=1}^\infty\Big(A_n\cos\frac{n\pi ct}{l}+B_n\sin\frac{n\pi ct}{l}\Big)\sin\frac{n\pi x}{l}.\tag{4.3}
$$
在级数及其对 $t$ 的导数中令 $t=0$，初始条件要求

$$
\varphi(x)=\sum_{n=1}^\infty A_n\sin\frac{n\pi x}{l},\qquad\psi(x)=\sum_{n=1}^\infty\frac{n\pi c}{l}B_n\sin\frac{n\pi x}{l},
$$
这是 $[0,l]$ 上的**正弦级数**（[2.2.9](/2.2.9#sec-9.3.2)）。由正交性，

$$
A_n=\frac2l\int_0^l\varphi(x)\sin\frac{n\pi x}{l}\,\mathrm{d}x,\qquad B_n=\frac{2}{n\pi c}\int_0^l\psi(x)\sin\frac{n\pi x}{l}\,\mathrm{d}x.\tag{4.4}
$$

### 4.1.2. 级数的收敛性

到目前为止的计算是形式的：必须验证以 (4.4) 为系数的级数 (4.3) 收敛、可以逐项求导两次，并取到初值。这取决于系数衰减的快慢，因而取决于数据的光滑性。

**定理 4.1.1** 设 $\varphi\in C^3[0,l]$，$\psi\in C^2[0,l]$，并满足相容性条件

$$
\varphi(0)=\varphi(l)=\varphi''(0)=\varphi''(l)=0,\qquad\psi(0)=\psi(l)=0.\tag{4.5}
$$
则以 (4.4) 为系数的级数 (4.3) 连同其不超过 $2$ 阶的偏导数在 $[0,l]\times[0,+\infty)$ 上一致收敛，其和是问题 (4.1) 唯一的 $C^2$ 解。

**证明** 对 $A_n$ 的公式分部积分三次，由 (4.5) 边界项都为零，得

$$
A_n=-\Big(\frac{l}{n\pi}\Big)^3a_n,\qquad a_n=\frac2l\int_0^l\varphi'''(x)\cos\frac{n\pi x}{l}\,\mathrm{d}x.
$$
$a_n$ 是 $\varphi'''$ 关于正交系 $\cos\frac{n\pi x}{l}$ 的系数，由正交性

$$
0\le\int_0^l\Big(\varphi'''-\sum_{n=1}^Na_n\cos\frac{n\pi x}{l}\Big)^2\mathrm{d}x=\int_0^l(\varphi''')^2\,\mathrm{d}x-\frac l2\sum_{n=1}^Na_n^2,
$$
这给出 Bessel 不等式 $\sum a_n^2\le\frac2l\int_0^l(\varphi''')^2\,\mathrm{d}x<+\infty$。由 **Cauchy–Schwarz 不等式**，

$$
\sum_{n=1}^\infty n^2\lvert A_n\rvert=\Big(\frac l\pi\Big)^3\sum_{n=1}^\infty\frac{\lvert a_n\rvert}{n}\le\Big(\frac l\pi\Big)^3\Big(\sum a_n^2\Big)^{1/2}\Big(\sum\frac1{n^2}\Big)^{1/2}<+\infty.
$$
同样，分部积分两次得 $B_n=-\frac{l^3}{c\,(n\pi)^3}b_n$，其中 $b_n$ 是 $\psi''$ 的正弦系数，且 $\sum n^2\lvert B_n\rvert<+\infty$。级数 (4.3) 及其一阶、二阶偏导数的每一项都不超过某常数乘以 $n^2(\lvert A_n\rvert+\lvert B_n\rvert)$，由 **Weierstrass 判别法**，这些级数都一致收敛。由[定理 1.1.1](/2.5.1#thm-1.1.1)，其和是 $C^2$ 解，边界条件和初始条件由构造成立（由 **Dirichlet 收敛定理**，$\varphi$ 与 $\psi$ 的正弦级数收敛于它们自身）。唯一性已由能量法证明（[定理 3.4.2](/2.5.3#thm-3.4.2)）。$\square$

条件 (4.5) 是自然的：$\varphi(0)=\psi(0)=0$ 表示数据与固定端相容，$\varphi''(0)=0$ 则由 $u_{tt}(0,t)=0$ 推出，与半无界弦的情形相同（[2.5.3](/2.5.3#thm-3.2.1)）。对于不满足这些条件的数据（如拨动的弦），级数仍然收敛，定义了一个广义解。事实上，由积化和差公式 $\sin\alpha\cos\beta=\frac12[\sin(\alpha+\beta)+\sin(\alpha-\beta)]$，级数 (4.3) 可以改写为对 $\varphi$、$\psi$ 的 $2l$ 周期奇延拓应用 d'Alembert 公式的结果（[2.5.3](/2.5.3#sec-3.2.3)）：两种方法给出同一个解。

### 4.1.3. 驻波与固有频率

级数 (4.3) 的每一项可以写成

$$
u_n(x,t)=C_n\sin\frac{n\pi x}{l}\cos\big(\omega_nt-\theta_n\big),\qquad\omega_n=\frac{n\pi c}{l},\quad C_n=\sqrt{A_n^2+B_n^2}.
$$
它是一个驻波（standing wave）：弦上每一点都以相同的频率同相振动，振幅 $C_n\lvert\sin\frac{n\pi x}{l}\rvert$ 随位置而变。振幅为零的点 $x=\frac{jl}{n}$（$j=1,\dots,n-1$）是波节，振幅最大的点是波腹。解 $u_n$ 是弦的简正模态，$\omega_n$ 是它的固有频率（natural frequency）。用张力和密度表示，频率为

$$
f_n=\frac{\omega_n}{2\pi}=\frac{n}{2l}\sqrt{\frac T\rho},\qquad n=1,2,\dots
$$
最低的 $f_1$ 是基频，其余是它的整数倍，即泛音。这就是弦能发出确定音高的原因，也解释了为什么更短、更紧或更轻的弦音调更高。弦的能量（[2.5.3](/2.5.3#sec-3.4.1)）等于各模态能量之和 $E=\frac{l}{4}\sum_n\omega_n^2C_n^2$，因为交叉项由正交性为零。

**例 4.1.1（拨动的弦）** 在点 $x=b$ 处把弦拉到高度 $h$ 后从静止释放：$\psi=0$，$0\le x\le b$ 时 $\varphi(x)=\frac{hx}{b}$，$b\le x\le l$ 时 $\varphi(x)=\frac{h(l-x)}{l-b}$。则 $B_n=0$，

$$
A_n=\frac2l\int_0^l\varphi(x)\sin\frac{n\pi x}{l}\,\mathrm{d}x=\frac{2hl^2}{\pi^2n^2b(l-b)}\sin\frac{n\pi b}{l},
$$
所以

$$
u(x,t)=\frac{2hl^2}{\pi^2b(l-b)}\sum_{n=1}^\infty\frac{1}{n^2}\sin\frac{n\pi b}{l}\sin\frac{n\pi x}{l}\cos\frac{n\pi ct}{l}.
$$
振幅按 $1/n^2$ 衰减，这反映了初始形状的尖角。在拨弦点处有波节的模态不出现：在中点 $b=l/2$ 拨弦时，弦不发出偶次泛音。吉他手正是利用这一点，通过在靠近或远离琴桥的位置拨弦来改变音色。

![左：两端固定的弦的前四个简正模态 sin(nπx/l) cos(ω_n t) 在若干时刻的形状。右：由级数计算的拨动的弦（b = l/4）在若干时刻的形状；尖角沿弦传播，与 d'Alembert 公式的预言一致](./plots/string-modes.py)

## 4.2. 有限杆中的热传导

### 4.2.1. 两端温度为零

对长为 $l$、两端保持温度 $0$ 的杆，

$$
\begin{cases}u_t=ku_{xx},&0<x<l,\ t>0,\\u(0,t)=u(l,t)=0,&t>0,\\u(x,0)=\varphi(x),&0\le x\le l.\end{cases}\tag{4.6}
$$
代入 $u=X(x)T(t)$ 得 $\frac{T'}{kT}=\frac{X''}{X}=-\lambda$，关于 $X$ 的特征值问题与前面相同，而 $T'+k\lambda T=0$，故 $T_n=\mathrm{e}^{-k\lambda_nt}$。因此（[2.4.12](/2.4.12#sec-12.5.4) 已经概述过）

$$
u(x,t)=\sum_{n=1}^\infty C_n\,\mathrm{e}^{-k(n\pi/l)^2t}\sin\frac{n\pi x}{l},\qquad C_n=\frac2l\int_0^l\varphi(x)\sin\frac{n\pi x}{l}\,\mathrm{d}x.\tag{4.7}
$$
指数因子使这个级数的性质远好于波动方程的级数。

**定理 4.2.1** 设 $\varphi$ 在 $[0,l]$ 上有界可积。

1. 当 $t>0$ 时，对每个 $t_0>0$，级数 (4.7) 连同其各阶偏导数在 $[0,l]\times[t_0,+\infty)$ 上一致收敛。其和 $u$ 在 $t>0$ 时无穷次可微，满足热方程和边界条件，且 $\lvert u(x,t)\rvert\le M\mathrm{e}^{-k\pi^2t/l^2}\sum_{n}\mathrm{e}^{-k(n^2-1)\pi^2t/l^2}$，其中 $M=\frac2l\int_0^l\lvert\varphi\rvert\,\mathrm{d}x$，所以当 $t\to+\infty$ 时 $u$ 指数地趋于 $0$。
2. 若进一步 $\varphi$ 连续、分段 $C^1$，且 $\varphi(0)=\varphi(l)=0$，则 $u$ 在 $[0,l]\times[0,+\infty)$ 上连续，且 $u(x,0)=\varphi(x)$。

**证明** (1) $\lvert C_n\rvert\le M$。当 $t\ge t_0$ 时，第 $n$ 项的偏导数 $\partial_t^j\partial_x^m$ 不超过 $M\big(k\frac{n^2\pi^2}{l^2}\big)^j\big(\frac{n\pi}{l}\big)^m\mathrm{e}^{-kn^2\pi^2t_0/l^2}$；由于指数衰减快于 $n$ 的任何幂次增长，这些上界构成收敛级数。由 Weierstrass 判别法与逐项求导（[2.2.9](/2.2.9#thm-9.1.6)）得到光滑性，而每一项都满足方程与边界条件。$\lvert u\rvert$ 的估计由 $\lvert C_n\rvert\le M$ 得到。

(2) 分部积分得 $C_n=\frac{l}{n\pi}c_n'$，其中 $c_n'$ 是 $\varphi'$ 的余弦系数；与定理 4.1.1 的证明一样，$\sum\lvert C_n\rvert<+\infty$。由于 $t\ge0$ 时 (4.7) 的每一项都不超过 $\lvert C_n\rvert$，级数在 $[0,l]\times[0,+\infty)$ 上一致收敛，其和连续，且在 $t=0$ 处就是 $\varphi$ 的正弦级数，由 Dirichlet 收敛定理收敛于 $\varphi$。$\square$

第 1 条是热方程的光滑化效应（smoothing effect）：无论初始温度如何（即使不连续），在任何正时刻温度都是无穷次可微的。原因从公式中就能看出：第 $n$ 个模态以速率 $kn^2\pi^2/l^2$ 衰减，所以精细的细节（$n$ 大）几乎瞬间消失。当 $t$ 很大时只有第一个模态保留下来：

$$
u(x,t)\approx C_1\,\mathrm{e}^{-k\pi^2t/l^2}\sin\frac{\pi x}{l},
$$
温度分布趋于正弦拱形，在时间尺度 $l^2/(k\pi^2)$ 上衰减。杆长加倍，冷却就慢四倍。这正是逆向热方程不适定（[2.5.1](/2.5.1#sec-1.4)）的另一面。与波动方程不同，这里的时间依赖不是振荡的，过程是不可逆的。

**例 4.2.1** 温度均匀为 $u_0$ 的杆在 $t=0$ 时两端浸入冰水：$\varphi\equiv u_0$。则 $C_n=\frac{2u_0}{n\pi}(1-(-1)^n)$，$n$ 为奇数时等于 $\frac{4u_0}{n\pi}$，$n$ 为偶数时为 $0$，

$$
u(x,t)=\frac{4u_0}{\pi}\sum_{m=0}^\infty\frac{1}{2m+1}\,\mathrm{e}^{-k(2m+1)^2\pi^2t/l^2}\sin\frac{(2m+1)\pi x}{l}.
$$
数据与边界条件不相容（$\varphi(0)=u_0\ne0$），所以定理 4.2.1 的第 2 条不适用，解在角点 $(0,0)$ 与 $(l,0)$ 处不连续；但由第 1 条，解在 $t>0$ 时光滑，并且可以证明对每个 $0<x<l$，当 $t\to0^+$ 时 $u(x,t)\to u_0$。

![初始温度为 1、两端保持为 0 的杆的冷却（k = l = 1）。温度分布在每个 t > 0 时都光滑，并迅速趋于第一个模态，其振幅按 exp(-π² t) 衰减（虚线：仅第一个模态）](./plots/heat-rod-cooling.py)

### 4.2.2. 其他边界条件

其他边界条件给出关于 $X$ 的其他特征值问题，从而给出其他展开；[2.4.12](/2.4.12#sec-12.4.1) 的表中列出了最常见的几种。级数的选取由边界条件决定，而不是由初始数据决定。

| 边界条件 | 特征函数 $X_n$ | 数据的展开 |
|---|---|---|
| $u(0)=u(l)=0$（两端温度为 $0$） | $\sin\frac{n\pi x}{l}$，$n\ge1$ | 正弦级数 |
| $u_x(0)=u_x(l)=0$（两端绝热） | $1$，$\cos\frac{n\pi x}{l}$，$n\ge1$ | 余弦级数 |
| $u(0)=0$，$u_x(l)=0$ | $\sin\frac{(2n-1)\pi x}{2l}$，$n\ge1$ | 半奇数倍频率的正弦级数 |
| 周期条件 $u(-l)=u(l)$，$u_x(-l)=u_x(l)$（圆环） | $1$，$\cos\frac{n\pi x}{l}$，$\sin\frac{n\pi x}{l}$ | 完整的 Fourier 级数 |
| $u(0)=0$，$u_x(l)+hu(l)=0$（Robin） | $\sin\mu_nx$，$\tan\mu_nl=-\mu_n/h$ | 非调和正弦函数的展开 |

**例 4.2.2（两端绝热）** 求解 $u_t=ku_{xx}$，$u_x(0,t)=u_x(l,t)=0$，$u(x,0)=x$。

**解** 特征值为 $\lambda_n=(n\pi/l)^2$，$n=0,1,2,\dots$，特征函数为 $\cos\frac{n\pi x}{l}$，解为 $u=\frac{a_0}{2}+\sum_{n\ge1}a_n\mathrm{e}^{-k(n\pi/l)^2t}\cos\frac{n\pi x}{l}$，其中系数是 $x$ 的余弦系数（[例 9.3.5](/2.2.9#sec-9.3.2)，把 $\pi$ 换成 $l$）：$\frac{a_0}{2}=\frac l2$，$a_n=\frac{2l((-1)^n-1)}{n^2\pi^2}$。所以

$$
u(x,t)=\frac l2-\frac{4l}{\pi^2}\sum_{m=0}^\infty\frac{1}{(2m+1)^2}\,\mathrm{e}^{-k(2m+1)^2\pi^2t/l^2}\cos\frac{(2m+1)\pi x}{l}.
$$
当 $t\to+\infty$ 时，温度趋于常数 $\frac l2$，即初始温度的平均值。这是能量守恒：对绝热杆，$\frac{\mathrm{d}}{\mathrm{d}t}\int_0^lu\,\mathrm{d}x=k\big[u_x\big]_0^l=0$。Dirichlet 条件下没有的零特征值，恰好承载了这个守恒量。

**例 4.2.3（一端热交换）** 设端点 $x=0$ 保持温度 $0$，端点 $x=l$ 按 Newton 冷却定律与温度为 $0$ 的环境交换热量：$u_x(l,t)+hu(l,t)=0$，$h>0$（**Robin 边界条件**）。求特征值与特征函数。

**解** 问题 $X''+\lambda X=0$，$X(0)=0$，$X'(l)+hX(l)=0$ 是正则 **Sturm–Liouville 问题**，所以特征值都是实的、单重的，且递增趋于 $+\infty$（[定理 12.5.2](/2.4.12#thm-12.5.2)）；由 [2.4.12](/2.4.12#sec-12.5.2) 中 Rayleigh 商的论证，它们非负，且 $\lambda=0$ 不是特征值（$X=x$ 给出 $X'(l)+hX(l)=1+hl\ne0$）。对 $\lambda=\mu^2>0$，$X=\sin\mu x$，第二个条件给出

$$
\mu\cos\mu l+h\sin\mu l=0,\qquad\text{即}\qquad\tan\mu l=-\frac{\mu}{h}.
$$
从图像上看，直线 $-\mu/h$ 与 $\tan\mu l$ 的每一支各交于一点，所以恰有一个根 $\mu_n$ 满足 $(n-\frac12)\pi<\mu_nl<n\pi$，且当 $n\to\infty$ 时 $\mu_nl-(n-\frac12)\pi\to0$。当 $l=h=1$ 时，数值上 $\mu_1\approx2.0288$，$\mu_2\approx4.9132$，$\mu_3\approx7.9787$。特征函数 $\sin\mu_nx$ 不是同一频率的谐波，但由[定理 12.5.1](/2.4.12#thm-12.5.1)，它们在 $[0,l]$ 上正交，$\int_0^l\sin^2\mu_nx\,\mathrm{d}x=\frac l2-\frac{\sin2\mu_nl}{4\mu_n}$，解为 $u=\sum c_n\mathrm{e}^{-k\mu_n^2t}\sin\mu_nx$，其中 $c_n=\int_0^l\varphi\sin\mu_nx\,\mathrm{d}x\big/\int_0^l\sin^2\mu_nx\,\mathrm{d}x$。

## 4.3. 一般方法

上面的例子遵循同一个模式；只要区域、方程和边界条件与乘积结构相容，这个模式就适用。

1. 把边界条件齐次化（§4.4.2）。
2. 把乘积 $u=X(x)T(t)$ 代入齐次方程，分离变量，分离常数记为 $-\lambda$。
3. 求解由分离后的方程与齐次边界条件给出的关于 $X$ 的特征值问题：特征值 $\lambda_n$，特征函数 $X_n$。
4. 对每个 $\lambda_n$ 求解关于 $T$ 的方程。
5. 叠加：$u=\sum_nT_n(t)X_n(x)$。
6. 用数据的**特征函数展开**，由初始条件确定其余常数。
7. 检验级数的收敛性（或把解理解为广义解）。

第 3 步与第 6 步由 Sturm–Liouville 理论保证。考虑非均匀杆中的热传导，其密度、比热和热导率都依赖于 $x$。[2.5.1](/2.5.1#sec-1.2.2) 的推导给出

$$
w(x)u_t=\big(p(x)u_x\big)_x-q(x)u,\qquad0<x<l,
$$
其中 $w=c_{\mathrm{p}}\rho>0$，$p=\kappa>0$，$q\ge0$ 描述通过侧面的热损失。在两端附加分离型边界条件，分离变量给出 $T'=-\lambda T$ 与正则 Sturm–Liouville 问题

$$
-(pX')'+qX=\lambda wX,\qquad\alpha_1X(0)-\alpha_2X'(0)=0,\quad\beta_1X(l)+\beta_2X'(l)=0.
$$
由[定理 12.5.1–12.5.3](/2.4.12#sec-12.5.2)，其特征值都是实的且递增趋于 $+\infty$，特征函数 $X_n$ 关于权 $w$ 正交，每个合理的初始温度都能按它们展开。解为

$$
u(x,t)=\sum_{n=1}^\infty c_n\mathrm{e}^{-\lambda_nt}X_n(x),\qquad c_n=\frac{\int_0^l\varphi X_nw\,\mathrm{d}x}{\int_0^lX_n^2w\,\mathrm{d}x}.
$$
变密度的弦振动也一样处理，只是 $T''=-\lambda T$。因此分离变量法推广了对称矩阵的对角化：带边界条件的算子 $-(pX')'+qX$ 在其特征函数构成的基下是"对角的"，在这组基下偏微分方程变为一个解耦的常微分方程组，每个模态一个方程。

这个方法要求区域在某个坐标系下是坐标矩形（区间、矩形，极坐标下的圆盘或圆环，球坐标下的球），并且每条边上的边界条件属于同一类型。对其他区域，就要依靠 Green 函数（[2.5.8](/2.5.8)）或数值方法。

## 4.4. 非齐次问题

### 4.4.1. 特征函数展开

考虑有内部热源的杆：

$$
u_t=ku_{xx}+f(x,t),\qquad u(0,t)=u(l,t)=0,\qquad u(x,0)=\varphi(x).\tag{4.8}
$$
这时不再有乘积解，但齐次问题的特征函数仍构成一组基。在每个时刻把未知解按特征函数展开，

$$
u(x,t)=\sum_{n=1}^\infty T_n(t)\sin\frac{n\pi x}{l},\qquad T_n(t)=\frac2l\int_0^lu(x,t)\sin\frac{n\pi x}{l}\,\mathrm{d}x,
$$
并记 $f_n(t)$、$\varphi_n$ 为 $f(\cdot,t)$ 与 $\varphi$ 的正弦系数。对 $T_n$ 在积分号下求导，利用方程，再分部积分两次（由于在端点处 $u=0$ 且 $\sin\frac{n\pi x}{l}=0$，边界项为零），

$$
T_n'=\frac2l\int_0^l\big(ku_{xx}+f\big)\sin\frac{n\pi x}{l}\,\mathrm{d}x=-k\lambda_nT_n+f_n(t),\qquad T_n(0)=\varphi_n,
$$
其中 $\lambda_n=(n\pi/l)^2$。每个模态满足一个一阶线性常微分方程，用常数变易法求解：

$$
T_n(t)=\varphi_n\mathrm{e}^{-k\lambda_nt}+\int_0^t\mathrm{e}^{-k\lambda_n(t-s)}f_n(s)\,\mathrm{d}s.\tag{4.9}
$$
这个积分又是齐次化原理（[2.5.3](/2.5.3#thm-3.3.1)），只是现在逐个模态地应用。对两端固定的弦 $u_{tt}=c^2u_{xx}+f$，同样的计算给出 $T_n''+\omega_n^2T_n=f_n(t)$，$\omega_n=\frac{n\pi c}{l}$，以及

$$
T_n(t)=A_n\cos\omega_nt+B_n\sin\omega_nt+\frac{1}{\omega_n}\int_0^t\sin\omega_n(t-s)\,f_n(s)\,\mathrm{d}s,\tag{4.10}
$$
其中 $A_n,B_n$ 由 (4.4) 给出。

**例 4.4.1（共振）** 两端固定、初始时静止于平衡位置的弦受外力 $f=F_0\sin\frac{\pi x}{l}\sin\omega t$ 驱动。只有第一个模态被激发：$f_1=F_0\sin\omega t$，$n\ge2$ 时 $f_n=0$，从而 $T_n\equiv0$。若 $\omega\ne\omega_1=\frac{\pi c}{l}$，式 (4.10) 给出

$$
T_1(t)=\frac{F_0}{\omega_1^2-\omega^2}\Big(\sin\omega t-\frac{\omega}{\omega_1}\sin\omega_1t\Big),
$$
它始终有界。令 $\omega\to\omega_1$，

$$
T_1(t)=\frac{F_0}{2\omega_1^2}\big(\sin\omega_1t-\omega_1t\cos\omega_1t\big),
$$
其振幅随 $t$ 线性增长：这就是**共振**。弦、桥梁或建筑物在受到频率等于其某个固有频率 $\omega_n$ 的外力作用时会强烈响应，只要外力在相应模态上的分量 $f_n$ 不为零；频率不是固有频率的外力只产生有界的响应。

### 4.4.2. 非齐次边界条件

若杆的两端保持给定的温度 $u(0,t)=g_1(t)$，$u(l,t)=g_2(t)$，特征函数法就不能直接应用，因为两个解的和不满足边界条件。我们先减去任意一个满足边界条件的函数，例如线性插值

$$
W(x,t)=g_1(t)+\frac xl\big(g_2(t)-g_1(t)\big).
$$
于是 $v=u-W$ 满足齐次边界条件和非齐次方程

$$
v_t=kv_{xx}+f-W_t,\qquad v(x,0)=\varphi(x)-W(x,0),
$$
它具有 (4.8) 的形式。对波动方程，新的源项为 $f-W_{tt}$。当边界值和源项都与时间无关时，最好减去稳态解 $U(x)$，即满足边界值的 $kU''+f=0$ 的解；这时 $v=u-U$ 满足一个齐次问题。

**例 4.4.2** 求解 $u_t=ku_{xx}$，$u(0,t)=0$，$u(l,t)=u_1$，$u(x,0)=0$（冷杆的右端突然被加热到 $u_1$）。

**解** 稳态解为 $U=\frac{u_1x}{l}$，$v=u-U$ 是问题 (4.6) 在 $\varphi=-\frac{u_1x}{l}$ 时的解，其正弦系数为 $C_n=\frac2l\int_0^l\big(-\frac{u_1x}{l}\big)\sin\frac{n\pi x}{l}\,\mathrm{d}x=\frac{2u_1(-1)^n}{n\pi}$。因此

$$
u(x,t)=\frac{u_1x}{l}+\frac{2u_1}{\pi}\sum_{n=1}^\infty\frac{(-1)^n}{n}\,\mathrm{e}^{-k(n\pi/l)^2t}\sin\frac{n\pi x}{l}.
$$
温度趋于线性的稳态，偏差按 $\mathrm{e}^{-k\pi^2t/l^2}$ 衰减。

## 4.5. 矩形与圆盘上的 Laplace 方程

### 4.5.1. 矩形

考虑矩形板 $0<x<a$，$0<y<b$ 中的稳态温度，三条边温度为 $0$，第四条边温度给定：

$$
\Delta u=0\ \ \text{在 }(0,a)\times(0,b)\text{ 内},\qquad u(0,y)=u(a,y)=0,\quad u(x,0)=0,\quad u(x,b)=f(x).\tag{4.11}
$$
代入 $u=X(x)Y(y)$ 得 $\frac{X''}{X}=-\frac{Y''}{Y}=-\lambda$。两条竖直边上的齐次条件给出特征值问题 $X''+\lambda X=0$，$X(0)=X(a)=0$，$X_n=\sin\frac{n\pi x}{a}$，$\lambda_n=(n\pi/a)^2$。方程 $Y''=\lambda_nY$ 与 $Y(0)=0$ 给出 $Y_n=\sinh\frac{n\pi y}{a}$：在 Laplace 方程中，第二个变量产生的是双曲函数，而不是指数衰减或振荡。叠加得

$$
u(x,y)=\sum_{n=1}^\infty c_n\sinh\frac{n\pi y}{a}\sin\frac{n\pi x}{a},\qquad c_n\sinh\frac{n\pi b}{a}=\frac2a\int_0^af(x)\sin\frac{n\pi x}{a}\,\mathrm{d}x.\tag{4.12}
$$
例如 $f(x)=\sin\frac{\pi x}{a}$ 给出只有一项的解 $u=\frac{\sinh(\pi y/a)}{\sinh(\pi b/a)}\sin\frac{\pi x}{a}$。由于 $0\le y\le b$ 时 $\frac{\sinh(n\pi y/a)}{\sinh(n\pi b/a)}\le\mathrm{e}^{-n\pi(b-y)/a}$，对任意有界可积的 $f$，级数在矩形内部收敛得极快，其和在内部无穷次可微：调和函数在内部是光滑的。四条边上都有非零数据的 Dirichlet 问题，是四个形如 (4.11)、各在一条边上有数据的问题之和；这是把叠加原理应用于边界数据。由 Dirichlet 问题的唯一性定理（[2.2.14](/2.2.14#thm-14.5.3)），这样得到的解是唯一的。

### 4.5.2. 圆盘

对圆盘 $r<a$ 上的 Dirichlet 问题，采用**极坐标**，此时（[2.2.14](/2.2.14#sec-14.6)）

$$
\Delta u=u_{rr}+\frac1ru_r+\frac{1}{r^2}u_{\theta\theta}.
$$
代入 $u=R(r)\Theta(\theta)$ 并乘以 $\frac{r^2}{R\Theta}$ 得

$$
\frac{r^2R''+rR'}{R}=-\frac{\Theta''}{\Theta}=\lambda.
$$
$\Theta$ 的"边界条件"是 $u$ 在平面上是单值函数，所以 $\Theta$ 必须以 $2\pi$ 为周期：周期特征值问题 $\Theta''+\lambda\Theta=0$ 的特征值为 $\lambda=n^2$（$n=0,1,2,\dots$），特征函数为 $1$ 与 $\cos n\theta$、$\sin n\theta$。关于 $R$ 的方程 $r^2R''+rR'-n^2R=0$ 是 Euler 方程，$n\ge1$ 时其解为 $r^n$ 与 $r^{-n}$，$n=0$ 时为 $1$ 与 $\ln r$。问题中隐含的第二个条件是 $u$ 在圆心有界，这排除了 $r^{-n}$ 与 $\ln r$。所以

$$
u(r,\theta)=\frac{a_0}{2}+\sum_{n=1}^\infty r^n\big(a_n\cos n\theta+b_n\sin n\theta\big).\tag{4.13}
$$
边界条件 $u(a,\theta)=f(\theta)$ 是 $f$ 在 $[0,2\pi]$ 上的 Fourier 级数，所以 $a^na_n$ 与 $a^nb_n$ 是 $f$ 的 Fourier 系数：

$$
a_n=\frac{1}{\pi a^n}\int_0^{2\pi}f(\varphi)\cos n\varphi\,\mathrm{d}\varphi,\qquad b_n=\frac{1}{\pi a^n}\int_0^{2\pi}f(\varphi)\sin n\varphi\,\mathrm{d}\varphi.
$$
用复变量 $z=x+\mathrm{i}y=r\mathrm{e}^{\mathrm{i}\theta}$ 表示，函数 $r^n\cos n\theta$ 与 $r^n\sin n\theta$ 就是 $\operatorname{Re}z^n$ 与 $\operatorname{Im}z^n$：式 (4.13) 是 $z$ 的一个幂级数的实部，这与调和函数和解析函数之间的关系（[2.3](/2.3)）一致。对圆盘外部 $r>a$，保留 $r^{-n}$ 而不是 $r^n$（无穷远处有界）；对圆环，四种解都需要。

级数 (4.13) 可以求出闭合形式的和。

**定理 4.5.1（Poisson 积分公式）** 设 $f$ 连续且以 $2\pi$ 为周期。当 $0\le r<a$ 时，级数 (4.13) 的和为

$$
u(r,\theta)=\frac{1}{2\pi}\int_0^{2\pi}\frac{a^2-r^2}{a^2-2ar\cos(\theta-\varphi)+r^2}\,f(\varphi)\,\mathrm{d}\varphi.\tag{4.14}
$$
函数 $u$ 在圆盘内调和，并可连续延拓到闭圆盘上，在边界圆周上 $u=f$。

**证明**（公式部分。）把系数代入式 (4.13)，记 $\rho=r/a<1$，

$$
u(r,\theta)=\frac1{2\pi}\int_0^{2\pi}f(\varphi)\Big[1+2\sum_{n=1}^\infty\rho^n\cos n(\theta-\varphi)\Big]\mathrm{d}\varphi;
$$
由于级数关于 $\varphi$ 一致收敛（各项不超过 $2\rho^n$），求和与积分可以交换。由**欧拉公式**，记 $\alpha=\theta-\varphi$，方括号是一个几何级数的实部：

$$
1+2\sum_{n=1}^\infty\rho^n\cos n\alpha=\operatorname{Re}\Big(1+2\sum_{n=1}^\infty\big(\rho\mathrm{e}^{\mathrm{i}\alpha}\big)^n\Big)=\operatorname{Re}\frac{1+\rho\mathrm{e}^{\mathrm{i}\alpha}}{1-\rho\mathrm{e}^{\mathrm{i}\alpha}}=\frac{1-\rho^2}{1-2\rho\cos\alpha+\rho^2},
$$
最后一步把分子分母同乘 $1-\rho\mathrm{e}^{-\mathrm{i}\alpha}$。分子分母再同乘 $a^2$ 即得式 (4.14)。$u$ 在边界上趋于 $f$ 的证明见 [2.5.8](/2.5.8)，那里将由圆盘的 Green 函数重新导出这个公式。$\square$

式 (4.14) 中的核是正的，积分为 $1$（取 $f\equiv1$，此时 $u\equiv1$），且当 $r\to a$ 时集中于 $\varphi=\theta$；所以 $u(r,\theta)$ 是边界值的加权平均，权重主要落在边界上邻近的部分。在圆心 $r=0$ 处，所有权重相等：

$$
u(0)=\frac{1}{2\pi}\int_0^{2\pi}f(\varphi)\,\mathrm{d}\varphi,
$$
这就是调和函数的平均值性质：圆心处的值等于边界圆周上的平均值。由它可以推出极值原理，这是 [2.5.8](/2.5.8) 的内容。

**例 4.5.1** 圆盘 $r<a$ 边界的上半圆保持温度 $1$，下半圆保持温度 $0$：$0<\theta<\pi$ 时 $f(\theta)=1$，$\pi<\theta<2\pi$ 时 $f(\theta)=0$。求稳态温度。

**解** $f$ 的 Fourier 系数为 $\frac{a_0}{2}=\frac12$，$a^na_n=0$，$a^nb_n=\frac1\pi\int_0^\pi\sin n\varphi\,\mathrm{d}\varphi=\frac{1-(-1)^n}{n\pi}$，$n$ 为奇数时等于 $\frac{2}{n\pi}$。所以

$$
u(r,\theta)=\frac12+\frac2\pi\sum_{m=0}^\infty\frac{1}{2m+1}\Big(\frac ra\Big)^{2m+1}\sin(2m+1)\theta=\frac12+\frac1\pi\arctan\frac{2ar\sin\theta}{a^2-r^2},
$$
这里用到求和公式 $\sum_{m\ge0}\frac{\rho^{2m+1}\sin(2m+1)\theta}{2m+1}=\frac12\arctan\frac{2\rho\sin\theta}{1-\rho^2}$（它是 $\frac12\log\frac{1+\rho\mathrm{e}^{\mathrm{i}\theta}}{1-\rho\mathrm{e}^{\mathrm{i}\theta}}$ 的虚部）。等温线 $u=\text{常数}$ 是过边界温度发生跳跃的两点 $(\pm a,0)$ 的圆弧；沿水平直径的温度为 $\frac12$。

![上半边界保持为 1、下半边界保持为 0 的圆盘中的稳态温度：等温线是过边界数据跳跃点 (±a, 0) 的圆弧](./plots/disk-dirichlet.py)

## 4.6. 收敛性与正则性

分离变量法所得级数的收敛性，反映了三类方程的定性行为（[2.5.1](/2.5.1#sec-1.5.3)）。

- 函数的光滑性对应于其 Fourier 系数的快速衰减：若周期延拓是 $C^k$ 的，分部积分 $k$ 次表明系数为 $o(n^{-k})$；跳跃使系数为 $1/n$ 阶，并在跳跃点附近产生 **Gibbs 现象**。起作用的是周期延拓，因此数据与边界条件的相容性和数据在区间内部的光滑性同样重要。
- 对热方程，因子 $\mathrm{e}^{-k\lambda_nt}$ 压倒了 $n$ 的任何增长，所以无论初始数据如何，解在每个 $t>0$ 时都无穷次可微（定理 4.2.1）。对平方可积的数据，初值在均方收敛的意义下取到；在数据连续且分段光滑的点处则逐点取到。
- 对波动方程，因子 $\cos\omega_nt$、$\sin\omega_nt$ 不衰减，所以解恰好与数据一样光滑，二次可微的数据还不足以给出古典解（定理 4.1.1 需要 $\varphi\in C^3$ 并满足相容性条件）。奇性保持并传播，与 [2.5.3](/2.5.3#sec-3.1.3) 一致。
- 对 Laplace 方程，因子 $(r/a)^n$ 或 $\frac{\sinh(n\pi y/a)}{\sinh(n\pi b/a)}$ 在内部按几何级数衰减，所以对任何可积的边界数据，解在区域内部都无穷次可微（实际上是实解析的）。

## 小结

| 问题 | 特征函数 | 时间（或第二个变量）因子 | 解 |
|---|---|---|---|
| 弦，两端固定 | $\sin\frac{n\pi x}{l}$ | $\cos\omega_nt$，$\sin\omega_nt$，$\omega_n=\frac{n\pi c}{l}$ | 驻波，式 (4.3) |
| 杆，两端温度为 $0$ | $\sin\frac{n\pi x}{l}$ | $\mathrm{e}^{-k(n\pi/l)^2t}$ | 式 (4.7)；光滑化，指数衰减 |
| 杆，两端绝热 | $1$，$\cos\frac{n\pi x}{l}$ | $\mathrm{e}^{-k(n\pi/l)^2t}$ | 趋于数据的平均值 |
| Robin 端 | $\sin\mu_nx$，$\tan\mu_nl=-\mu_n/h$ | $\mathrm{e}^{-k\mu_n^2t}$ | Sturm–Liouville 展开 |
| 矩形，Laplace 方程 | $\sin\frac{n\pi x}{a}$ | $\sinh\frac{n\pi y}{a}$ | 式 (4.12) |
| 圆盘，Laplace 方程 | $1$，$\cos n\theta$，$\sin n\theta$ | $r^n$ | 式 (4.13)，Poisson 积分公式 (4.14) |

- 分离变量法把乘积区域上的线性齐次问题化为一个变量的特征值问题和另一个变量的常微分方程；数据用特征函数展开来匹配，其依据是 Sturm–Liouville 理论。
- 非齐次方程逐个模态求解（对每个 $T_n$ 应用齐次化原理）；非齐次边界条件先通过减去一个满足它的函数（最好是稳态解）来消去。
- 按固有频率施加的外力产生共振；Neumann 问题的零特征值承载着守恒的总热量。
