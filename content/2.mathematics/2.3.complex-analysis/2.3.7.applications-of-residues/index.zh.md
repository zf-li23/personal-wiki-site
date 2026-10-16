---
title: 留数的应用
source_hash: 7322b56f3e16
---

[2.3.6](/2.3.6) 的**留数定理**把围道积分化为有限个留数之和。本章把这一观察发展成一套实用的方法。许多 $[0, 2\pi]$ 上或实轴上的定积分（包括原函数不是初等函数的积分），只要选取适当的闭围道并证明辅助部分的贡献趋于零，就成为某个围道积分的实部。同样的估计（大圆弧引理、Jordan 引理与小圆弧引理）也用来计算 Fourier 变换、用留数求 Laplace 逆变换，[2.5.6](/2.5.6) 正是这样把这些变换用于偏微分方程的。留数还可以把某些级数求成闭合形式。

最后一节的被积函数是对数导数 $f'/f$。它的留数计数零点与极点，由此得到辐角原理与 Rouché 定理——不必求出零点就能确定多项式和超越函数零点位置的工具。它们还给出解析映射的局部信息（开映射定理与局部单射性），下一章（[2.3.8](/2.3.8)）讨论共形映射时要用到。

## 7.1. 三角函数有理式的积分

设 $R(x, y)$ 是二元有理函数，在单位圆周 $x^2 + y^2 = 1$ 上取有限值，考虑

$$
I = \int_0^{2\pi}R(\cos\theta, \sin\theta)\,\mathrm{d}\theta.
$$

在单位圆周 $z = \mathrm{e}^{\mathrm{i}\theta}$ 上，

$$
\cos\theta = \frac{1}{2}\left(z + \frac1z\right), \qquad \sin\theta = \frac{1}{2\mathrm{i}}\left(z - \frac1z\right), \qquad \mathrm{d}\theta = \frac{\mathrm{d}z}{\mathrm{i}z},
$$

且 $\theta$ 取遍 $[0, 2\pi]$ 时，$z$ 沿 $\lvert z\rvert = 1$ 逆时针绕行一周。因此 $I$ 是 $z$ 的有理函数在单位圆周上的积分：

$$
I = \oint_{\lvert z\rvert = 1}R\left(\frac{z + z^{-1}}{2}, \frac{z - z^{-1}}{2\mathrm{i}}\right)\frac{\mathrm{d}z}{\mathrm{i}z} = 2\pi\mathrm{i}\sum_{\lvert z_k\rvert < 1}\operatorname{Res}(F, z_k), \tag{7.1}
$$

其中 $F$ 表示关于 $z$ 的被积函数，求和遍及它在单位圆内的极点。

**例 7.1.1** 设 $a > \lvert b\rvert > 0$，则

$$
\int_0^{2\pi}\frac{\mathrm{d}\theta}{a + b\cos\theta} = \oint_{\lvert z\rvert = 1}\frac{2\,\mathrm{d}z}{\mathrm{i}(bz^2 + 2az + b)} = \frac{2\pi}{\sqrt{a^2 - b^2}}.
$$

$bz^2 + 2az + b$ 的根是 $z_\pm = \frac{-a \pm \sqrt{a^2 - b^2}}{b}$。它们是实数，乘积为 $1$，且 $\lvert z_+\rvert < 1 < \lvert z_-\rvert$。单极点 $z_+$ 处的留数是 $\frac{2}{\mathrm{i}b(z_+ - z_-)} = \frac{1}{\mathrm{i}\sqrt{a^2 - b^2}}$，由式 (7.1) 即得结果。

**例 7.1.2** 设实数 $p$ 满足 $0 < \lvert p\rvert < 1$，$n \ge 0$ 为整数。下面证明

$$
\int_0^{2\pi}\frac{\cos n\theta}{1 - 2p\cos\theta + p^2}\,\mathrm{d}\theta = \frac{2\pi p^n}{1 - p^2}.
$$

若写 $\cos n\theta = \frac12(z^n + z^{-n})$，会在 $0$ 处产生 $n$ 阶极点。更好的做法是积分 $\mathrm{e}^{\mathrm{i}n\theta} = z^n$ 再取实部。由于 $1 - 2p\cos\theta + p^2 = (1 - pz)(1 - p/z) = \frac{(1 - pz)(z - p)}{z}$，

$$
J = \int_0^{2\pi}\frac{\mathrm{e}^{\mathrm{i}n\theta}\,\mathrm{d}\theta}{1 - 2p\cos\theta + p^2} = \oint_{\lvert z\rvert = 1}\frac{z^n\,\mathrm{d}z}{\mathrm{i}(1 - pz)(z - p)}.
$$

单位圆内唯一的极点是 $z = p$，留数为 $\frac{p^n}{\mathrm{i}(1 - p^2)}$，所以 $J = \frac{2\pi p^n}{1 - p^2}$。它是实数，因此就是余弦积分的值（正弦积分为零，这由对称性也可以看出）。例如取 $p = \frac12$、$n = 2$，由 $5 - 4\cos\theta = 4\left(1 - \cos\theta + \frac14\right)$，

$$
\int_0^{2\pi}\frac{\cos2\theta}{5 - 4\cos\theta}\,\mathrm{d}\theta = \frac14\cdot\frac{2\pi\cdot\frac14}{1 - \frac14} = \frac{\pi}{6}.
$$

## 7.2. 有理函数在实轴上的积分

对 $\mathbb{R}$ 上的积分，用一段圆弧把区间 $[-R, R]$ 封闭起来，再令 $R \to \infty$。被积函数衰减得足够快时，圆弧没有贡献：

**引理 7.2.1（大圆弧引理）** 设对一切充分大的 $R$，$f$ 在圆弧 $C_R = \{R\mathrm{e}^{\mathrm{i}\theta} : \theta_1 \le \theta \le \theta_2\}$ 上连续，且 $R \to \infty$ 时 $\max_{z\in C_R}\lvert zf(z)\rvert \to 0$，则 $\int_{C_R}f(z)\,\mathrm{d}z \to 0$。

**证明** 由长大不等式（定理 4.1.2），$\left\lvert\int_{C_R}f\,\mathrm{d}z\right\rvert \le \max_{C_R}\lvert f\rvert\cdot R(\theta_2 - \theta_1) = (\theta_2 - \theta_1)\max_{C_R}\lvert zf(z)\rvert \to 0$。$\square$

**定理 7.2.1** 设 $R = \frac PQ$ 是有理函数，$\deg Q \ge \deg P + 2$，且在实轴上没有极点，则

$$
\int_{-\infty}^{\infty}R(x)\,\mathrm{d}x = 2\pi\mathrm{i}\sum_{\operatorname{Im}z_k > 0}\operatorname{Res}(R, z_k). \tag{7.2}
$$

**证明** 由 $\lvert R(x)\rvert = O(x^{-2})$，积分绝对收敛。取 $R$ 大于所有极点的模，对由 $[-R, R]$ 与上半圆周 $C_R$ 组成的闭围道（§7.4 图中的 (a)）用留数定理：$\int_{-R}^RR(x)\,\mathrm{d}x + \int_{C_R}R(z)\,\mathrm{d}z = 2\pi\mathrm{i}\sum_{\operatorname{Im}z_k > 0}\operatorname{Res}(R, z_k)$。由于 $zR(z) = O(1/z)$，由引理 7.2.1，圆弧上的积分趋于 $0$。$\square$

也可以在下半平面封闭围道；这时结果是下半平面内留数之和乘以 $-2\pi\mathrm{i}$，由于 $\operatorname{Res}(R, \infty) = 0$，这与定理 6.3.3 一致。

**例 7.2.1** 1. $\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{(x^2 + 1)^2}$：上半平面内唯一的极点是二阶极点 $\mathrm{i}$，留数为 $\frac{\mathrm{d}}{\mathrm{d}z}(z + \mathrm{i})^{-2}\big|_{z=\mathrm{i}} = -2(2\mathrm{i})^{-3} = \frac{1}{4\mathrm{i}}$。积分等于 $2\pi\mathrm{i}\cdot\frac{1}{4\mathrm{i}} = \frac\pi2$。
2. $\int_0^\infty\frac{\mathrm{d}x}{x^4 + 1} = \frac12\int_{-\infty}^\infty\frac{\mathrm{d}x}{x^4 + 1}$。上半平面内的极点是 $\mathrm{e}^{\mathrm{i}\pi/4}$ 与 $\mathrm{e}^{3\mathrm{i}\pi/4}$，留数为 $-\frac{z_k}{4}$（例 6.3.1），之和为 $-\frac{\mathrm{i}\sqrt2}{4}$。因此 $\int_0^\infty\frac{\mathrm{d}x}{x^4 + 1} = \frac12\cdot2\pi\mathrm{i}\cdot\left(-\frac{\mathrm{i}\sqrt2}{4}\right) = \frac{\pi}{2\sqrt2}$。

被积函数有旋转对称性时，半圆以外的围道也很有用。

**例 7.2.2** 设整数 $n \ge 2$，则

$$
\int_0^\infty\frac{\mathrm{d}x}{1 + x^n} = \frac{\pi/n}{\sin(\pi/n)}.
$$

沿扇形 $0 \le \arg z \le \frac{2\pi}{n}$、$\lvert z\rvert \le R$ 的边界积分 $f(z) = \frac1{1 + z^n}$。在射线 $z = t\mathrm{e}^{2\pi\mathrm{i}/n}$ 上 $z^n = t^n$，所以这条边（向内走）的贡献是 $-\mathrm{e}^{2\pi\mathrm{i}/n}I$，其中 $I$ 是所求积分。由引理 7.2.1，圆弧的贡献在极限中为 $0$。扇形内唯一的极点是 $z_0 = \mathrm{e}^{\mathrm{i}\pi/n}$，留数为 $\frac{1}{nz_0^{n-1}} = \frac{z_0}{nz_0^n} = -\frac{z_0}{n}$。因此

$$
\left(1 - \mathrm{e}^{2\pi\mathrm{i}/n}\right)I = -\frac{2\pi\mathrm{i}}{n}\mathrm{e}^{\mathrm{i}\pi/n}, \qquad I = \frac{2\pi\mathrm{i}}{n\left(\mathrm{e}^{\mathrm{i}\pi/n} - \mathrm{e}^{-\mathrm{i}\pi/n}\right)} = \frac{\pi}{n\sin(\pi/n)}.
$$

$n = 3$ 时得 $\frac{2\pi}{3\sqrt3}$；$n = 4$ 时得例 7.2.1 中的 $\frac{\pi}{2\sqrt2}$。

## 7.3. Fourier 型积分与 Jordan 引理

### 7.3.1. Jordan 引理

计算 Fourier 变换时总会遇到积分 $\int_{-\infty}^\infty R(x)\mathrm{e}^{\mathrm{i}ax}\,\mathrm{d}x$。若 $\deg Q = \deg P + 1$，大圆弧引理不适用；但 $a > 0$ 时因子 $\mathrm{e}^{\mathrm{i}az}$ 在上半平面内衰减，因为 $\lvert\mathrm{e}^{\mathrm{i}az}\rvert = \mathrm{e}^{-a\operatorname{Im}z}$。Jordan 引理把这种衰减定量化。

**引理 7.3.1（Jordan 引理）** 设 $a > 0$，对一切充分大的 $R$，$g$ 在上半圆周 $C_R = \{R\mathrm{e}^{\mathrm{i}\theta} : 0 \le \theta \le \pi\}$ 上连续，且 $M(R) = \max_{C_R}\lvert g\rvert \to 0$，则

$$
\lim_{R\to\infty}\int_{C_R}g(z)\,\mathrm{e}^{\mathrm{i}az}\,\mathrm{d}z = 0.
$$

**证明** 在 $C_R$ 上 $\lvert\mathrm{e}^{\mathrm{i}az}\rvert = \mathrm{e}^{-aR\sin\theta}$。由 Jordan 不等式 $\sin\theta \ge \frac{2\theta}{\pi}$（$0 \le \theta \le \frac\pi2$，由 $\sin$ 的凹性）与对称性 $\theta \mapsto \pi - \theta$，

$$
\left\lvert\int_{C_R}g\,\mathrm{e}^{\mathrm{i}az}\,\mathrm{d}z\right\rvert \le M(R)\int_0^\pi\mathrm{e}^{-aR\sin\theta}R\,\mathrm{d}\theta = 2M(R)\int_0^{\pi/2}\mathrm{e}^{-aR\sin\theta}R\,\mathrm{d}\theta \le 2M(R)\int_0^{\pi/2}\mathrm{e}^{-2aR\theta/\pi}R\,\mathrm{d}\theta < \frac{\pi}{a}M(R),
$$

它趋于 $0$。$\square$

这里只需要 $M(R) \to 0$，不需要 $RM(R) \to 0$：缺少的衰减由指数因子补足。$a < 0$ 时在下半圆周上有同样的结论；下面讨论 Laplace 变换时，要用到对左半圆周 $\{c + R\mathrm{e}^{\mathrm{i}\theta} : \frac\pi2 \le \theta \le \frac{3\pi}2\}$ 与因子 $\mathrm{e}^{st}$（$t > 0$）的类似结论。

### 7.3.2. 含振荡因子的积分

**定理 7.3.1** 设 $R = \frac PQ$ 是有理函数，$\deg Q \ge \deg P + 1$，在实轴上没有极点，$a > 0$，则

$$
\int_{-\infty}^{\infty}R(x)\,\mathrm{e}^{\mathrm{i}ax}\,\mathrm{d}x = 2\pi\mathrm{i}\sum_{\operatorname{Im}z_k > 0}\operatorname{Res}\left(R(z)\mathrm{e}^{\mathrm{i}az}, z_k\right). \tag{7.3}
$$

$a < 0$ 时在下半平面封闭围道：积分等于 $\operatorname{Im}z_k < 0$ 的留数之和乘以 $-2\pi\mathrm{i}$。若 $R$ 在 $\mathbb{R}$ 上取实值，式 (7.3) 的实部与虚部分别给出 $\int R(x)\cos ax\,\mathrm{d}x$ 与 $\int R(x)\sin ax\,\mathrm{d}x$。

**证明** 用上半圆周封闭 $[-R, R]$，对 $g = R$（它在 $\infty$ 处趋于 $0$）用 Jordan 引理。$\square$

$\deg Q = \deg P + 1$ 时积分只是条件收敛，半圆的论证只证明了对称极限 $\int_{-R}^R$ 的收敛。由积分的 **Dirichlet 判别法**，$[0, B]$ 与 $[-A, 0]$ 上的积分分别收敛，所以通常意义下的反常积分存在。

**例 7.3.1** 计算 $\int_{-\infty}^{\infty}\frac{\cos x}{x^2 - 2x + 5}\,\mathrm{d}x$ 与 $\int_{-\infty}^{\infty}\frac{\sin x}{x^2 - 2x + 5}\,\mathrm{d}x$。

$\frac{\mathrm{e}^{\mathrm{i}z}}{z^2 - 2z + 5}$ 的极点是 $1 \pm 2\mathrm{i}$，只有 $1 + 2\mathrm{i}$ 在上半平面内，留数为 $\frac{\mathrm{e}^{\mathrm{i}(1 + 2\mathrm{i})}}{4\mathrm{i}} = \frac{\mathrm{e}^{-2}\mathrm{e}^{\mathrm{i}}}{4\mathrm{i}}$。由式 (7.3)，

$$
\int_{-\infty}^{\infty}\frac{\mathrm{e}^{\mathrm{i}x}}{x^2 - 2x + 5}\,\mathrm{d}x = \frac{\pi}{2\mathrm{e}^2}(\cos1 + \mathrm{i}\sin1),
$$

所以两个积分分别等于 $\frac{\pi\cos1}{2\mathrm{e}^2}$ 与 $\frac{\pi\sin1}{2\mathrm{e}^2}$。

**例 7.3.2** $\int_0^\infty\frac{x\sin x}{x^2 + 4}\,\mathrm{d}x$。这里 $\deg Q = \deg P + 1$，必须用 Jordan 引理。$\frac{z\mathrm{e}^{\mathrm{i}z}}{z^2 + 4}$ 在 $2\mathrm{i}$ 处的留数是 $\frac{2\mathrm{i}\,\mathrm{e}^{-2}}{4\mathrm{i}} = \frac{\mathrm{e}^{-2}}{2}$，所以 $\int_{-\infty}^\infty\frac{x\mathrm{e}^{\mathrm{i}x}}{x^2 + 4}\,\mathrm{d}x = \pi\mathrm{i}\,\mathrm{e}^{-2}$。取虚部，并利用被积函数是偶函数，得 $\int_0^\infty\frac{x\sin x}{x^2 + 4}\,\mathrm{d}x = \frac{\pi}{2\mathrm{e}^2}$。

### 7.3.3. Fourier 变换与 Laplace 变换

采用 [2.5.6](/2.5.6) 的约定 $\hat f(\xi) = \int_{\mathbb{R}}f(x)\,\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x$，定理 7.3.1 可以计算有理函数的 Fourier 变换。$\xi$ 的符号决定围道应在哪个半平面封闭。

**例 7.3.3** 设 $b > 0$，$f(x) = \frac{1}{x^2 + b^2}$。$\xi < 0$ 时因子 $\mathrm{e}^{-\mathrm{i}\xi z}$ 在上半平面内衰减，由 $\mathrm{i}b$ 处的留数得 $\hat f(\xi) = 2\pi\mathrm{i}\cdot\frac{\mathrm{e}^{\xi b}}{2\mathrm{i}b} = \frac\pi b\mathrm{e}^{\xi b}$。$\xi > 0$ 时在下半平面封闭：$\hat f(\xi) = -2\pi\mathrm{i}\cdot\frac{\mathrm{e}^{-\xi b}}{-2\mathrm{i}b} = \frac\pi b\mathrm{e}^{-\xi b}$。合起来，并由 $\xi = 0$ 处的连续性，

$$
\hat f(\xi) = \frac{\pi}{b}\,\mathrm{e}^{-b\lvert\xi\rvert}.
$$

这一对函数（Lorentz 函数与双边指数函数）在 [2.5.6](/2.5.6) 中以及上半平面的 Poisson 核中还会出现。

$F(s)$ 的 Laplace 逆变换由 Bromwich 积分给出

$$
f(t) = \frac{1}{2\pi\mathrm{i}}\int_{c - \mathrm{i}\infty}^{c + \mathrm{i}\infty}F(s)\,\mathrm{e}^{st}\,\mathrm{d}s, \qquad t > 0,
$$

积分路径是位于 $F$ 所有奇点右侧的竖直线 $\operatorname{Re}s = c$（推导见 [2.5.6](/2.5.6)）。若 $F$ 是有理函数且 $\deg Q > \deg P$，可以用向左的大半圆周封闭这条直线；$t > 0$ 时因子 $\mathrm{e}^{st}$ 在那里衰减，左半圆周形式的 Jordan 引理使圆弧上的积分趋于零，于是

$$
f(t) = \sum_k\operatorname{Res}\left(F(s)\,\mathrm{e}^{st}, s_k\right), \tag{7.4}
$$

求和遍及 $F$ 的所有极点 $s_k$。

**例 7.3.4** 1. $F(s) = \frac{1}{s^2 + 1}$：$\frac{\mathrm{e}^{st}}{s^2 + 1}$ 在 $\pm\mathrm{i}$ 处的留数是 $\pm\frac{\mathrm{e}^{\pm\mathrm{i}t}}{2\mathrm{i}}$，之和为 $\sin t$。
2. $F(s) = \frac{1}{s(s+1)^2}$：$0$ 处的留数是 $1$，二阶极点 $-1$ 处的留数是 $\frac{\mathrm{d}}{\mathrm{d}s}\frac{\mathrm{e}^{st}}{s}\big|_{s=-1} = \frac{(st - 1)\mathrm{e}^{st}}{s^2}\big|_{s=-1} = -(1 + t)\mathrm{e}^{-t}$。因此 $f(t) = 1 - (1 + t)\mathrm{e}^{-t}$。$m$ 阶极点产生 $t^k\mathrm{e}^{s_kt}$（$k < m$）形式的项，这正是常系数线性微分方程中熟悉的共振项。

## 7.4. 实轴上的极点与主值

若被积函数在实轴上有单极点，积分在通常意义下发散，但对称的极限可能存在。

**定义 7.4.1** 设 $f$ 在 $\mathbb{R}$ 上除 $x_0$ 外连续。若极限

$$
\operatorname{PV}\int_{-\infty}^{\infty}f(x)\,\mathrm{d}x = \lim_{\substack{\varepsilon\to0^+\\R\to\infty}}\left(\int_{-R}^{x_0 - \varepsilon} + \int_{x_0 + \varepsilon}^{R}\right)f(x)\,\mathrm{d}x
$$

存在，则称它为积分的 **Cauchy 主值**（有多个点 $x_0$ 时作显然的修改）。

例如 $\operatorname{PV}\int_{-1}^{1}\frac{\mathrm{d}x}{x} = 0$，尽管 $\int_0^1\frac{\mathrm{d}x}{x}$ 发散。计算主值时，用绕极点的小半圆周把围道"挖去"一小块（下图中的 (b)），小半圆周的贡献由下面的引理计算。

**引理 7.4.1（小圆弧引理）** 设 $z_0$ 是 $f$ 的单极点，$C_\varepsilon$ 是逆时针方向的圆弧 $z_0 + \varepsilon\mathrm{e}^{\mathrm{i}\theta}$，$\theta_1 \le \theta \le \theta_1 + \alpha$，则

$$
\lim_{\varepsilon\to0}\int_{C_\varepsilon}f(z)\,\mathrm{d}z = \mathrm{i}\alpha\operatorname{Res}(f, z_0).
$$

**证明** 写 $f = \frac{c_{-1}}{z - z_0} + g(z)$，其中 $g$ 在 $z_0$ 附近解析，从而有界。则 $\int_{C_\varepsilon}\frac{c_{-1}\,\mathrm{d}z}{z - z_0} = c_{-1}\int_{\theta_1}^{\theta_1+\alpha}\mathrm{i}\,\mathrm{d}\theta = \mathrm{i}\alpha c_{-1}$，而 $\left\lvert\int_{C_\varepsilon}g\,\mathrm{d}z\right\rvert \le \alpha\varepsilon\max\lvert g\rvert \to 0$。$\square$

取整个圆周（$\alpha = 2\pi$）就回到留数的定义；半圆周给出它的一半。对于阶数 $\ge 2$ 的极点，小圆弧上的积分一般没有有限极限，主值也不存在。

**定理 7.4.1** 设 $R = \frac PQ$，$\deg Q \ge \deg P + 1$，$R$ 的实极点 $x_j$ 都是单极点。对 $a > 0$，

$$
\operatorname{PV}\int_{-\infty}^{\infty}R(x)\,\mathrm{e}^{\mathrm{i}ax}\,\mathrm{d}x = 2\pi\mathrm{i}\sum_{\operatorname{Im}z_k > 0}\operatorname{Res}\left(R\,\mathrm{e}^{\mathrm{i}az}, z_k\right) + \pi\mathrm{i}\sum_j\operatorname{Res}\left(R\,\mathrm{e}^{\mathrm{i}az}, x_j\right).
$$

**证明** 用挖去小半圆的围道：沿 $[-R, R]$ 走，在每个 $x_j$ 处绕半径为 $\varepsilon$ 的上半小圆周，再用上半圆周 $C_R$ 封闭。由留数定理，围道积分等于上半平面内留数之和乘以 $2\pi\mathrm{i}$。每个小半圆周沿顺时针方向（$\alpha = -\pi$），由引理 7.4.1，它的积分趋于 $-\pi\mathrm{i}\operatorname{Res}(\cdot, x_j)$；由 Jordan 引理，大圆弧上的积分趋于零。把小圆弧的贡献移到右端即得公式。$\square$

**例 7.4.1** **Dirichlet 积分**：$\int_0^\infty\frac{\sin x}{x}\,\mathrm{d}x = \frac\pi2$。函数 $\frac{\mathrm{e}^{\mathrm{i}z}}{z}$ 只在 $0$ 处有单极点，留数为 $1$，所以 $\operatorname{PV}\int_{-\infty}^\infty\frac{\mathrm{e}^{\mathrm{i}x}}{x}\,\mathrm{d}x = \pi\mathrm{i}$。取虚部得 $\int_{-\infty}^{\infty}\frac{\sin x}{x}\,\mathrm{d}x = \pi$；这里不需要主值，因为 $\frac{\sin x}{x}$ 在 $0$ 处连续。（实部给出 $\operatorname{PV}\int\frac{\cos x}{x}\,\mathrm{d}x = 0$，这由奇函数性质是显然的。）

**例 7.4.2** $\int_0^\infty\frac{1 - \cos x}{x^2}\,\mathrm{d}x = \frac\pi2$。考虑 $f(z) = \frac{1 - \mathrm{e}^{\mathrm{i}z}}{z^2}$。由于 $1 - \mathrm{e}^{\mathrm{i}z} = -\mathrm{i}z + \frac{z^2}{2} + \cdots$，$f$ 在 $0$ 处有单极点，留数为 $-\mathrm{i}$；在大半圆周上 $\lvert f\rvert \le 2/R^2$。定理 7.4.1 的论证给出 $\operatorname{PV}\int_{-\infty}^\infty f(x)\,\mathrm{d}x = \pi\mathrm{i}\cdot(-\mathrm{i}) = \pi$。取实部得 $\int_{-\infty}^\infty\frac{1 - \cos x}{x^2}\,\mathrm{d}x = \pi$，而被积函数是偶函数。

![三种常用围道。(a) 用上半圆周 C_R 封闭的线段 [-R, R]；只有上半平面内的极点（红色）有贡献，圆弧上的积分由大圆弧引理或 Jordan 引理趋于零。(b) 同一围道在实轴上的单极点处用小半圆周 C_ε 挖去一小块。(c) 用于沿正实轴有支割线的被积函数的锁孔围道：割线的上下两岸上 z^α 或 log z 取不同的值](./plots/contours.py)

## 7.5. 含多值函数的积分

### 7.5.1. 幂函数：锁孔围道

对于 $\alpha$ 不是整数时的 $\int_0^\infty x^{\alpha - 1}R(x)\,\mathrm{d}x$，取 $z^{\alpha - 1} = \mathrm{e}^{(\alpha - 1)\log z}$ 的 $0 < \arg z < 2\pi$ 的分支，它在 $\mathbb{C}$ 去掉**支割线** $[0, +\infty)$ 后解析（[2.3.3](/2.3.3)）。锁孔围道（上图中的 (c)）沿割线上岸从 $\varepsilon$ 走到 $R$，绕大圆周一圈，沿下岸返回，再顺时针绕小圆周。在上岸 $z^{\alpha - 1} = x^{\alpha - 1}$；在下岸 $\arg z = 2\pi$，$z^{\alpha - 1} = x^{\alpha - 1}\mathrm{e}^{2\pi\mathrm{i}(\alpha - 1)} = x^{\alpha - 1}\mathrm{e}^{2\pi\mathrm{i}\alpha}$。所以两岸的积分并不抵消，合起来贡献 $\left(1 - \mathrm{e}^{2\pi\mathrm{i}\alpha}\right)\int_\varepsilon^Rx^{\alpha - 1}R(x)\,\mathrm{d}x$。

**例 7.5.1** 设 $0 < \alpha < 1$，则

$$
\int_0^\infty\frac{x^{\alpha - 1}}{1 + x}\,\mathrm{d}x = \frac{\pi}{\sin\pi\alpha}. \tag{7.5}
$$

在大圆周上 $\lvert zf(z)\rvert \approx R^{\alpha - 1} \to 0$，在小圆周上 $\lvert zf(z)\rvert \approx \varepsilon^\alpha \to 0$，所以两个圆周在极限中都没有贡献（引理 7.2.1 及其 $\varepsilon \to 0$ 的类似形式）。唯一的极点是 $-1 = \mathrm{e}^{\mathrm{i}\pi}$（在所取的分支上），那里的留数是 $\mathrm{e}^{\mathrm{i}\pi(\alpha - 1)} = -\mathrm{e}^{\mathrm{i}\pi\alpha}$。因此

$$
\left(1 - \mathrm{e}^{2\pi\mathrm{i}\alpha}\right)I = -2\pi\mathrm{i}\,\mathrm{e}^{\mathrm{i}\pi\alpha}, \qquad I = \frac{2\pi\mathrm{i}}{\mathrm{e}^{\mathrm{i}\pi\alpha} - \mathrm{e}^{-\mathrm{i}\pi\alpha}} = \frac{\pi}{\sin\pi\alpha}.
$$

令 $x = t^n$、$\alpha = \frac1n$，式 (7.5) 就成为例 7.2.2 的公式。用 Gamma 函数表示，式 (7.5) 就是余元公式 $\Gamma(\alpha)\Gamma(1 - \alpha) = \frac{\pi}{\sin\pi\alpha}$。

同样的论证给出：若有理函数 $R$ 在 $[0, \infty)$ 上没有极点，且在 $0$ 与 $\infty$ 处 $\lvert x^\alpha R(x)\rvert \to 0$，则

$$
\int_0^\infty x^{\alpha - 1}R(x)\,\mathrm{d}x = \frac{2\pi\mathrm{i}}{1 - \mathrm{e}^{2\pi\mathrm{i}\alpha}}\sum_k\operatorname{Res}\left(z^{\alpha - 1}R(z), z_k\right),
$$

求和遍及 $R$ 的所有极点，其中 $0 < \arg z_k < 2\pi$。

### 7.5.2. 对数函数

插入一个对数，锁孔围道也可以计算没有对称性的有理函数在 $[0, \infty)$ 上的积分。取 $\log z$ 的 $0 < \arg z < 2\pi$ 的分支，上下两岸的值分别是 $\ln x$ 与 $\ln x + 2\pi\mathrm{i}$。对 $\int_0^\infty R(x)\,\mathrm{d}x$，对数项相互抵消，留下 $2\pi\mathrm{i}$ 一项：

$$
\int_0^\infty R(x)\,\mathrm{d}x = -\sum_k\operatorname{Res}\left(R(z)\log z, z_k\right), \tag{7.6}
$$

其中 $\deg Q \ge \deg P + 2$，$R$ 在 $[0, \infty)$ 上没有极点（由于在 $0$ 与 $\infty$ 处 $\lvert zR(z)\log z\rvert \to 0$，两个圆周的贡献趋于零）。

**例 7.5.2** $\int_0^\infty\frac{\mathrm{d}x}{1 + x^3}$。在所取的分支上，极点 $z_k = \mathrm{e}^{\mathrm{i}\pi/3}, \mathrm{e}^{\mathrm{i}\pi}, \mathrm{e}^{5\mathrm{i}\pi/3}$ 处 $\log z_k = \frac{\mathrm{i}\pi}{3}, \mathrm{i}\pi, \frac{5\mathrm{i}\pi}{3}$，且 $\operatorname{Res}\left(\frac{\log z}{1 + z^3}, z_k\right) = \frac{\log z_k}{3z_k^2} = -\frac{z_k\log z_k}{3}$。由式 (7.6)，

$$
I = \frac{1}{3}\sum_kz_k\log z_k = \frac{\mathrm{i}\pi}{9}\left(\mathrm{e}^{\mathrm{i}\pi/3} - 3 + 5\,\mathrm{e}^{-\mathrm{i}\pi/3}\right) = \frac{\mathrm{i}\pi}{9}\left(-2\sqrt3\,\mathrm{i}\right) = \frac{2\pi}{3\sqrt3},
$$

与例 7.2.2 一致。

## 7.6. 级数求和

函数 $\pi\cot\pi z$ 在每个整数 $n$ 处有单极点，留数为 $\frac{\pi\cos\pi n}{\pi\cos\pi n} = 1$。因此乘以 $f(z)$ 后在整数处得到留数 $f(n)$，一个围道积分就能把整个级数包含进来。

**定理 7.6.1** 设 $f = \frac PQ$ 是有理函数，$\deg Q \ge \deg P + 2$，且 $f$ 的极点 $z_1, \dots, z_m$ 都不是整数，则

$$
\sum_{n=-\infty}^{\infty}f(n) = -\sum_{k=1}^m\operatorname{Res}\left(\pi\cot(\pi z)f(z), z_k\right).
$$

**证明**（概要）设 $C_N$ 是以 $\left(N + \frac12\right)(\pm1 \pm \mathrm{i})$ 为顶点的正方形的边界。可以验证 $\lvert\cot\pi z\rvert$ 在所有 $C_N$ 上有与 $N$ 无关的界（在竖直边上 $\lvert\cot\pi z\rvert = \lvert\tanh\pi y\rvert < 1$，在水平边上 $\lvert\cot\pi z\rvert \le \coth\frac{\pi}{2}$）。由于在 $C_N$ 上 $\lvert f\rvert = O(N^{-2})$，而 $C_N$ 的长度是 $O(N)$，$\pi\cot(\pi z)f(z)$ 沿 $C_N$ 的积分趋于 $0$。由留数定理，$C_N$ 内全部留数之和，即 $\sum_{\lvert n\rvert\le N}f(n)$ 加上各 $z_k$ 处的留数，趋于 $0$。$\square$

**例 7.6.1** 设 $a > 0$，$f(z) = \frac{1}{z^2 + a^2}$ 有单极点 $\pm\mathrm{i}a$。利用 $\cot(\mathrm{i}y) = -\mathrm{i}\coth y$，$\frac{\pi\cot\pi z}{z^2 + a^2}$ 的两个留数都等于 $-\frac{\pi\coth\pi a}{2a}$。因此

$$
\sum_{n=-\infty}^{\infty}\frac{1}{n^2 + a^2} = \frac{\pi}{a}\coth\pi a, \qquad \sum_{n=1}^\infty\frac{1}{n^2 + a^2} = \frac{\pi a\coth\pi a - 1}{2a^2}.
$$

令 $a \to 0$，利用 $\pi a\coth\pi a = 1 + \frac{\pi^2a^2}{3} + O(a^4)$，得 $\sum_{n\ge1}\frac1{n^2} = \frac{\pi^2}{6}$。把 $\pi\cot\pi z$ 换成 $\frac{\pi}{\sin\pi z}$（它在 $n$ 处的留数是 $(-1)^n$），可以同样地对交错级数求和。

## 7.7. 辐角原理与 Rouché 定理

### 7.7.1. 零点与极点的计数

若 $z_0$ 是 $f$ 的 $m$ 阶零点，则 $f = (z - z_0)^m\varphi$，$\varphi(z_0) \ne 0$，且

$$
\frac{f'(z)}{f(z)} = \frac{m}{z - z_0} + \frac{\varphi'(z)}{\varphi(z)},
$$

所以对数导数 $\frac{f'}{f}$ 以 $z_0$ 为单极点，留数为 $m$。在 $m$ 阶极点处 $f = (z - z_0)^{-m}\varphi$，$\frac{f'}{f}$ 的留数为 $-m$。由留数定理得：

**定理 7.7.1（辐角原理）** 设 $C$ 是正向的分段光滑简单闭曲线，$f$ 在 $C$ 上及 $C$ 内部除 $C$ 内有限个极点外解析，在 $C$ 上既无零点也无极点。记 $N$、$P$ 分别为 $f$ 在 $C$ 内的零点个数与极点个数（按阶数计重数），则

$$
\frac{1}{2\pi\mathrm{i}}\oint_C\frac{f'(z)}{f(z)}\,\mathrm{d}z = N - P. \tag{7.7}
$$

这个名称来自左端的解释。局部地 $\frac{f'}{f} = (\log f)'$，所以积分度量的是 $z$ 沿 $C$ 绕行一周时 $\log f(z) = \ln\lvert f(z)\rvert + \mathrm{i}\arg f(z)$ 的总改变量。模回到初值，所以

$$
N - P = \frac{1}{2\pi}\Delta_C\arg f(z),
$$

即像曲线 $f(C)$ 绕原点的圈数。于是零点计数化为观察像曲线怎样旋转，控制理论中的 Nyquist 稳定性判据也基于这一方法。

### 7.7.2. Rouché 定理

**定理 7.7.2（Rouché 定理）** 设 $f$、$g$ 在简单闭曲线 $C$ 上及其内部解析，且在 $C$ 上 $\lvert g(z)\rvert < \lvert f(z)\rvert$，则 $f$ 与 $f + g$ 在 $C$ 内的零点个数（按阶数计重数）相同。

**证明** 对 $t \in [0, 1]$，在 $C$ 上 $\lvert f + tg\rvert \ge \lvert f\rvert - \lvert g\rvert > 0$，所以 $f + tg$ 在 $C$ 上没有零点，由式 (7.7)，它在 $C$ 内的零点个数为

$$
N(t) = \frac{1}{2\pi\mathrm{i}}\oint_C\frac{f'(z) + tg'(z)}{f(z) + tg(z)}\,\mathrm{d}z.
$$

被积函数关于 $(t, z) \in [0, 1] \times C$ 连续，所以 $N(t)$ 关于 $t$ 连续。$N(t)$ 只取整数值，因而是常数，$N(0) = N(1)$。$\square$

直观地说，$\lvert g\rvert < \lvert f\rvert$ 意味着扰动 $g$ 无法把 $f + g$ 的像曲线拖过原点，所以绕数不变。使用这个定理时，把函数拆成零点已知的主项 $f$ 与在 $C$ 上较小的余项 $g$。

**例 7.7.1** $p(z) = z^7 - 5z^3 + z - 2$ 在 $\lvert z\rvert < 1$ 与 $1 < \lvert z\rvert < 2$ 内各有几个零点？

- 在 $\lvert z\rvert = 1$ 上取 $f = -5z^3$、$g = z^7 + z - 2$：$\lvert g\rvert \le 1 + 1 + 2 = 4 < 5 = \lvert f\rvert$。所以 $p$ 在 $\lvert z\rvert < 1$ 内的零点个数与 $-5z^3$ 相同，为 $3$。
- 在 $\lvert z\rvert = 2$ 上取 $f = z^7$：$\lvert -5z^3 + z - 2\rvert \le 40 + 2 + 2 = 44 < 128$。所以全部 $7$ 个零点都在 $\lvert z\rvert < 2$ 内。
- 在 $\lvert z\rvert = 1$ 上 $\lvert p\rvert \ge 5 - 4 > 0$。因此圆环 $1 < \lvert z\rvert < 2$ 内恰有 $7 - 3 = 4$ 个零点。

![p(z) = z^7 - 5z^3 + z - 2 的辐角原理。左：p 的定义域着色图与它的七个零点；三个在 |z| = 1（白色虚线）内，七个都在 |z| = 2（深色虚线）内。中、右：像曲线 p(|z| = 1) 与 p(|z| = 2) 分别绕原点 3 圈与 7 圈](./plots/argument-principle.py)

**例 7.7.2** 1. Rouché 定理给出**代数基本定理**的一个简短证明。设 $p(z) = z^n + a_{n-1}z^{n-1} + \cdots + a_0$，$R > \max\left(1, \sum\lvert a_k\rvert\right)$，则在 $\lvert z\rvert = R$ 上 $\lvert a_{n-1}z^{n-1} + \cdots + a_0\rvert \le R^{n-1}\sum\lvert a_k\rvert < R^n = \lvert z^n\rvert$。所以 $p$ 与 $z^n$ 一样，在 $\lvert z\rvert < R$ 内恰有 $n$ 个零点。
2. 若 $\lvert a\rvert > \mathrm{e}$，$n \ge 1$，则方程 $\mathrm{e}^z = az^n$ 在 $\lvert z\rvert < 1$ 内恰有 $n$ 个根：在 $\lvert z\rvert = 1$ 上 $\lvert\mathrm{e}^z\rvert = \mathrm{e}^{\operatorname{Re}z} \le \mathrm{e} < \lvert az^n\rvert$，所以 $az^n - \mathrm{e}^z$ 与 $az^n$ 的零点个数相同。

### 7.7.3. 解析映射的局部性态

对 $w$ 在 $w_0 = f(z_0)$ 附近时的 $f(z) - w$ 用 Rouché 定理，可以描述解析函数怎样映射一点的邻域。

**定理 7.7.3** 设 $f$ 在 $z_0$ 处解析，$w_0 = f(z_0)$，$z_0$ 是 $f - w_0$ 的 $m$ 阶零点。则存在 $\rho > 0$ 与 $\delta > 0$，使对每个满足 $0 < \lvert w - w_0\rvert < \delta$ 的 $w$，方程 $f(z) = w$ 在 $\lvert z - z_0\rvert < \rho$ 内恰有 $m$ 个解，且都是单根。特别地，若 $f'(z_0) \ne 0$，则 $f$ 在 $z_0$ 附近是单射。

**证明** $f - w_0$ 与 $f'$ 的零点都是孤立的（定理 5.4.2；由于 $m$ 有限，$f'$ 不恒为零），所以可以取 $\rho$，使 $f - w_0$ 与 $f'$ 在 $0 < \lvert z - z_0\rvert \le \rho$ 内都没有零点。令 $\delta = \min_{\lvert z - z_0\rvert = \rho}\lvert f(z) - w_0\rvert > 0$。对 $\lvert w - w_0\rvert < \delta$，取 $F = f - w_0$、$G = w_0 - w$ 用 Rouché 定理：$f - w$ 在圆盘内有 $m$ 个零点。$w \ne w_0$ 时它们都不是 $z_0$，且在每个零点处 $f' \ne 0$，所以都是单零点，因而互不相同。$\square$

**定理 7.7.4（开映射定理）** 区域上不为常数的解析函数把开集映为开集。

**证明** 由定理 7.7.3，对每个 $z_0$，$z_0$ 的每个小圆盘的像都包含以 $f(z_0)$ 为中心的一个圆盘。$\square$

开映射定理给出**最大模原理**（[2.3.4](/2.3.4)）的另一个证明：若 $\lvert f\rvert$ 在 $z_0$ 处取局部极大值，则 $z_0$ 的邻域的像包含以 $f(z_0)$ 为中心的圆盘，从而包含模更大的点。定理 7.7.3 还说明，在 $f'(z_0) = 0$ 的点附近（$z_0$ 是 $f - w_0$ 的 $m \ge 2$ 阶零点），$f$ 是 $m$ 对一的；这正是共形性恰好在 $f$ 的临界点处失效的原因（[2.3.8](/2.3.8)）。

## 小结

| 积分 | 围道 | 结果 |
|---|---|---|
| $\int_0^{2\pi}R(\cos\theta, \sin\theta)\,\mathrm{d}\theta$ | 单位圆周，$z = \mathrm{e}^{\mathrm{i}\theta}$ | $2\pi\mathrm{i}\sum_{\lvert z_k\rvert<1}\operatorname{Res}$ |
| $\int_{-\infty}^\infty R(x)\,\mathrm{d}x$，$\deg Q \ge \deg P + 2$ | 上半圆周；大圆弧引理 | $2\pi\mathrm{i}\sum_{\operatorname{Im}z_k>0}\operatorname{Res}$ |
| $\int_{-\infty}^\infty R(x)\mathrm{e}^{\mathrm{i}ax}\,\mathrm{d}x$，$a > 0$，$\deg Q \ge \deg P + 1$ | 上半圆周；Jordan 引理 | $2\pi\mathrm{i}\sum_{\operatorname{Im}z_k>0}\operatorname{Res}(R\mathrm{e}^{\mathrm{i}az})$ |
| 实轴上的单极点 | 挖去小半圆；小圆弧引理 | 主值；实极点以 $\pi\mathrm{i}$ 计入 |
| $\int_0^\infty x^{\alpha-1}R(x)\,\mathrm{d}x$，$\int_0^\infty R(x)\,\mathrm{d}x$ | 绕割线 $[0, \infty)$ 的锁孔围道 | 两岸相差因子 $\mathrm{e}^{2\pi\mathrm{i}\alpha}$ 或相差 $2\pi\mathrm{i}$ |
| Laplace 逆变换 | 向左封闭的 Bromwich 直线 | $\sum\operatorname{Res}(F(s)\mathrm{e}^{st})$ |
| $\sum_nf(n)$ | 正方形 $C_N$ | $-\sum\operatorname{Res}(\pi\cot(\pi z)f)$（在 $f$ 的极点处） |
| $f$ 的零点 | 辐角原理、Rouché 定理 | $N - P = \frac{1}{2\pi}\Delta_C\arg f$；主项决定零点个数 |
