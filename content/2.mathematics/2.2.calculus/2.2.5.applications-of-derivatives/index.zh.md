---
title: 用导数研究函数
---

上一章（[2.2.4](/2.2.4)）定义了**导数**并建立了求导法则；本章用导数研究函数本身：单调性、极值与最值、凸性与拐点、渐近线与作图，以及用导数求极限（L'Hôpital 法则）、证明不等式、用多项式逼近函数（Taylor 公式）。联系导数（局部信息）与函数值（整体信息）的桥梁是微分中值定理，它依赖闭区间上**连续函数**的**最大最小值定理**（[2.2.3](/2.2.3)）；本章其余内容几乎都由它推出。Taylor 公式是本章的另一个核心，它把**等价无穷小**的思想推进到任意阶，是计算极限、误差估计的有力工具，也是 [2.2.9](/2.2.9) 中 Taylor 级数、[2.2.11](/2.2.11) 中多元 Taylor 公式与极值判别的基础。凸函数与 Jensen 不等式在概率论中也经常用到。

## 5.1. 微分中值定理

### 5.1.1. 极值与 Fermat 定理

**定义 5.1.1（极值）** 若存在 $x_0$ 的邻域 $N(x_0,\delta)$，使得对其中一切 $x$ 有 $f(x)\le f(x_0)$（$f(x)\ge f(x_0)$），则称 $x_0$ 为 $f$ 的一个**极大值点**（**极小值点**），$f(x_0)$ 为 $f$ 的一个**极大值**（**极小值**）。极大值与极小值统称**极值**，极大值点与极小值点统称**极值点**。

极值是局部概念：极大值不一定大于极小值，也不一定是最大值；而且极值点必须是定义域的内点。

**定理 5.1.1（Fermat 定理）** 若 $f$ 在 $x_0$ 点取得极值，且 $f'(x_0)$ 存在，则 $f'(x_0) = 0$。

**证明** 不妨设 $f$ 在 $x_0$ 取极大值，则在 $x_0$ 附近 $f(x)-f(x_0)\le0$，于是

$$
f'_+(x_0) = \lim_{x\to x_0^+}\frac{f(x)-f(x_0)}{x-x_0}\le0,\qquad f'_-(x_0) = \lim_{x\to x_0^-}\frac{f(x)-f(x_0)}{x-x_0}\ge0.
$$

由 $f'(x_0) = f'_-(x_0) = f'_+(x_0)$ 得 $f'(x_0) = 0$。 $\square$

**定义 5.1.2** 称满足 $f'(x_0) = 0$ 的点 $x_0$ 为 $f$ 的**驻点**（也称临界点）。

Fermat 定理说：对可导函数，"导数为零"是极值点的必要条件，但不充分，例如 $x^3$ 在 $0$ 点。几何上，在可导的极值点处切线是水平的。

### 5.1.2. Rolle 中值定理与 Lagrange 中值定理

下面"$f$ 在 $[a,b]$ 上连续、在 $(a,b)$ 内可导"记作 $f\in C[a,b]$ 且在 $(a,b)$ 内可导。

**定理 5.1.2（Rolle 定理）** 设 $f\in C[a,b]$，在 $(a,b)$ 内可导，且 $f(a) = f(b)$，则存在 $\xi\in(a,b)$ 使得 $f'(\xi) = 0$。

**证明** 由**最大最小值定理**，$f$ 在 $[a,b]$ 上有最大值 $M$ 和最小值 $m$。若 $M = m$，$f$ 是常数，任取 $\xi\in(a,b)$ 即可。若 $M>m$，由 $f(a) = f(b)$，$M$ 与 $m$ 中至少有一个在某个内点 $\xi\in(a,b)$ 取得，$\xi$ 是极值点，由 Fermat 定理 $f'(\xi) = 0$。 $\square$

**定理 5.1.3（Lagrange 中值定理）** 设 $f\in C[a,b]$，在 $(a,b)$ 内可导，则存在 $\xi\in(a,b)$ 使得

$$
f'(\xi) = \frac{f(b)-f(a)}{b-a}.
$$

**证明** 构造辅助函数（曲线与弦的纵坐标之差）$\varphi(x) = f(x)-\frac{f(b)-f(a)}{b-a}(x-a)$，则 $\varphi\in C[a,b]$，在 $(a,b)$ 内可导，且 $\varphi(a) = \varphi(b) = f(a)$。由 Rolle 定理，存在 $\xi\in(a,b)$ 使 $\varphi'(\xi) = f'(\xi)-\frac{f(b)-f(a)}{b-a} = 0$。 $\square$

几何意义：曲线 $y = f(x)$ 上至少有一点的切线平行于连接两端点的弦；Rolle 定理是弦水平的特殊情形。运动学意义：平均速度一定在某一时刻被瞬时速度取到。Lagrange 中值定理常写成有限增量公式

$$
f(b)-f(a) = f'(\xi)(b-a),\quad\xi\in(a,b),\qquad\text{或}\qquad f(b)-f(a) = f'\bigl(a+\theta(b-a)\bigr)(b-a),\quad0<\theta<1.
$$

后一种写法对 $a>b$ 也成立。与 $\Delta y\approx f'(x_0)\Delta x$ 相比，它是精确的等式，代价是 $\xi$ 的位置未知。

![Lagrange 中值定理：在 ξ₁、ξ₂ 处曲线的切线平行于连接 (a, f(a)) 与 (b, f(b)) 的弦](./plots/mean-value-theorem.py)

**推论 5.1.1**（1） 若在区间 $I$ 上 $f'(x)\equiv0$，则 $f$ 在 $I$ 上是常数；(2) 若在 $I$ 上 $f'(x)\equiv g'(x)$，则 $f(x) = g(x)+c$，$c$ 为常数。

**证明** (1) 任取 $x_1<x_2$ 属于 $I$，$f(x_2)-f(x_1) = f'(\xi)(x_2-x_1) = 0$。(2) 对 $f-g$ 用 (1)。 $\square$

推论 5.1.1 (2) 是 [2.2.6](/2.2.6) 中"原函数相差一个常数"的依据。

**推论 5.1.2（单调性判别）** 设 $f\in C[a,b]$，在 $(a,b)$ 内可导。

1. 若在 $(a,b)$ 内 $f'(x)\ge0$（$\le0$），则 $f$ 在 $[a,b]$ 上单调非减（非增）；
2. 若在 $(a,b)$ 内 $f'(x)>0$（$<0$），则 $f$ 在 $[a,b]$ 上严格单调增加（减少）；
3. 若 $f$ 在 $[a,b]$ 上单调非减（非增），则在 $(a,b)$ 内 $f'(x)\ge0$（$\le0$）。

**证明** 1、2：任取 $a\le x<y\le b$，$f(y)-f(x) = f'(\xi)(y-x)$，$\xi\in(x,y)$，符号由 $f'(\xi)$ 决定。3：单调非减时差商 $\frac{f(x+h)-f(x)}{h}\ge0$，取极限即得。 $\square$

所以 1 与 3 合起来是**单调函数**（非严格意义）的充分必要条件；2 只是充分条件：$y = x^3$ 严格增加，但 $y'(0) = 0$。

Rolle 定理常用来讨论函数零点的个数：若 $f$ 有 $k$ 个不同零点，则 $f'$ 至少有 $k-1$ 个不同零点。

**例 5.1.1** 证明方程 $\mathrm{e}^x = ax^2+bx+c$ 至多有 3 个实根。

**证明** 设 $f(x) = \mathrm{e}^x-ax^2-bx-c$ 有 4 个零点 $x_1<x_2<x_3<x_4$，由 Rolle 定理 $f'(x) = \mathrm{e}^x-2ax-b$ 至少有 3 个不同零点，$f''(x) = \mathrm{e}^x-2a$ 至少有 2 个，$f'''(x) = \mathrm{e}^x$ 至少有 1 个，矛盾。 $\square$

**例 5.1.2** 证明 $P_n(x) = \frac{\mathrm{d}^n}{\mathrm{d}x^n}(x^2-1)^n$ 在 $(-1,1)$ 内恰有 $n$ 个不同的零点。

**证明** 设 $f(x) = (x^2-1)^n = (x-1)^n(x+1)^n$，则 $\pm1$ 是 $f, f', \dots, f^{(n-1)}$ 的零点。由 Rolle 定理，$f'$ 在 $(-1,1)$ 内有零点，连同 $\pm1$，$f'$ 在 $[-1,1]$ 上有 3 个零点；于是 $f''$ 在 $(-1,1)$ 内有 2 个零点，在 $[-1,1]$ 上有 4 个；依此类推，$f^{(n-1)}$ 在 $[-1,1]$ 上有 $n+1$ 个零点，$f^{(n)} = P_n$ 在 $(-1,1)$ 内至少有 $n$ 个不同零点。$P_n$ 是 $2n-n = n$ 次**多项式**，至多有 $n$ 个零点，所以恰有 $n$ 个。 $\square$

（$P_n$ 除常数因子外就是 Legendre 多项式。）

**例 5.1.3** 证明 $x>0$ 时 $\frac{x}{1+x}<\ln(1+x)<x$，并证明 $\lim\limits_{n\to\infty}\Bigl(\sum\limits_{k=1}^n\frac1k-\ln n\Bigr)$ 存在。

**证明** 对 $\ln t$ 在 $[1,1+x]$ 上用 Lagrange 中值定理：$\ln(1+x) = \frac{x}{\xi}$，$\xi\in(1,1+x)$，于是 $\frac{x}{1+x}<\ln(1+x)<x$。以 $\frac1n$ 代 $x$ 得

$$
\frac{1}{n+1}<\ln\Bigl(1+\frac1n\Bigr)<\frac1n.
$$

令 $a_n = \sum_{k=1}^n\frac1k-\ln n$。$a_{n+1}-a_n = \frac1{n+1}-\ln\bigl(1+\frac1n\bigr)<0$，$\{a_n\}$ 单调下降；又 $\ln n = \sum_{k=1}^{n-1}\ln\bigl(1+\frac1k\bigr)$，

$$
a_n = \sum_{k=1}^{n-1}\Bigl[\frac1k-\ln\Bigl(1+\frac1k\Bigr)\Bigr]+\frac1n>0,
$$

$\{a_n\}$ 有下界。由**单调收敛定理** $\{a_n\}$ 收敛，其极限记为 $\gamma$（Euler 常数，$\gamma\approx0.5772$），即 $1+\frac12+\cdots+\frac1n = \ln n+\gamma+o(1)$。 $\square$

**例 5.1.4** 证明 $f(x) = \bigl(1+\frac1x\bigr)^x$ 在 $(0,+\infty)$ 上单调增加。

**证明** $f'(x) = \bigl(1+\frac1x\bigr)^x\Bigl[\ln\bigl(1+\frac1x\bigr)-\frac{1}{x+1}\Bigr]>0$，由例 5.1.3 的不等式。 $\square$

**例 5.1.5** 设 $b>a>0$，证明：(1) 当 $0<p<1$ 时 $b^p-a^p<(b-a)^p$；(2) 当 $p>1$ 时 $b^p-a^p>(b-a)^p$。

**证明** 令 $f(x) = x^p-a^p-(x-a)^p$（$x\ge a$），$f(a) = 0$，$f'(x) = p\bigl[x^{p-1}-(x-a)^{p-1}\bigr]$。$0<p<1$ 时 $x>a$ 处 $f'(x)<0$，$f$ 在 $[a,+\infty)$ 上严格减少，$f(b)<f(a) = 0$；$p>1$ 时 $f'(x)>0$，$f(b)>0$。 $\square$

特别地，$\sqrt[n]{b}-\sqrt[n]{a}<\sqrt[n]{b-a}$（$n\ge2$）。

**例 5.1.6** 设 $f$ 在 $(-\infty,+\infty)$ 上二阶可导且 $f''\equiv0$，证明 $f(x) = ax+b$。

**证明** 由推论 5.1.1，$f'\equiv a$；再由 Lagrange 中值定理 $f(x)-f(0) = f'(\xi)x = ax$，$f(x) = ax+b$，$b = f(0)$。 $\square$

归纳可得：若 $f^{(n+1)}\equiv0$，则 $f$ 是次数不超过 $n$ 的多项式。

### 5.1.3. Cauchy 中值定理

**定理 5.1.4（Cauchy 中值定理）** 设 $f, g\in C[a,b]$，在 $(a,b)$ 内可导，且在 $(a,b)$ 内 $g'(x)\ne0$，则存在 $\xi\in(a,b)$ 使得

$$
\frac{f'(\xi)}{g'(\xi)} = \frac{f(b)-f(a)}{g(b)-g(a)}.
$$

**证明** 先说明 $g(b)\ne g(a)$：否则由 Rolle 定理 $g'$ 在 $(a,b)$ 内有零点。令

$$
\varphi(x) = f(x)-\frac{f(b)-f(a)}{g(b)-g(a)}\bigl(g(x)-g(a)\bigr),
$$

则 $\varphi(a) = \varphi(b) = f(a)$，由 Rolle 定理存在 $\xi$ 使 $\varphi'(\xi) = f'(\xi)-\frac{f(b)-f(a)}{g(b)-g(a)}g'(\xi) = 0$。 $\square$

另一种理解：把 $(g(t), f(t))$（$t\in[a,b]$）看成平面曲线的参数方程，$\frac{f(b)-f(a)}{g(b)-g(a)}$ 是弦的斜率，$\frac{f'(\xi)}{g'(\xi)}$ 是 $t = \xi$ 处切线的斜率（4.3.2 节），定理就是参数曲线上的 Lagrange 中值定理。取 $g(x) = x$ 即回到 Lagrange 中值定理。注意不能对分子分母分别用 Lagrange 中值定理再相除，那样得到的两个中值点一般不同。

### 5.1.4. 导数介值定理与中值问题

**定理 5.1.5（Darboux 定理）** 设 $f$ 在 $[a,b]$ 上可导（端点处为单侧导数），$f'_+(a)\ne f'_-(b)$，$\mu$ 介于 $f'_+(a)$ 与 $f'_-(b)$ 之间，则存在 $\xi\in(a,b)$ 使 $f'(\xi) = \mu$。

这一定理又称导数介值定理：导函数即使不连续，也像连续函数一样具有介值性。

**证明** 不妨设 $f'_+(a)<\mu<f'_-(b)$。令 $h(x) = f(x)-\mu x$，则 $h$ 在 $[a,b]$ 上连续，$h'_+(a) = f'_+(a)-\mu<0$，$h'_-(b) = f'_-(b)-\mu>0$。由 $h'_+(a)<0$，在 $a$ 右侧附近 $h(x)<h(a)$；由 $h'_-(b)>0$，在 $b$ 左侧附近 $h(x)<h(b)$。所以 $h$ 在 $[a,b]$ 上的最小值只能在内点 $\xi$ 取得，由 Fermat 定理 $h'(\xi) = f'(\xi)-\mu = 0$。 $\square$

推论：导函数没有**第一类间断点**。例如符号函数 $\operatorname{sgn}x$ 在 $0$ 点有跳跃，所以它在 $\mathbb{R}$ 上不是任何函数的导数（[2.2.6](/2.2.6) 中原函数的存在问题）。

证明"存在 $\xi$ 使某个含 $f(\xi)$、$f'(\xi)$ 的等式成立"时，关键是构造辅助函数 $h$，使所求等式恰好是 $h'(\xi) = 0$，再验证 $h$ 满足 Rolle 定理的条件；或者把等式整理成 $\frac{f'(\xi)}{g'(\xi)}$ 的形式，用 Cauchy 中值定理。

**例 5.1.7** 设 $f, g\in C[a,b]$，在 $(a,b)$ 内可导，$f(a) = f(b) = 0$，证明存在 $\xi\in(a,b)$ 使 $f'(\xi)+g'(\xi)f(\xi) = 0$。

**证明** 令 $h(x) = \mathrm{e}^{g(x)}f(x)$，则 $h(a) = h(b) = 0$。由 Rolle 定理存在 $\xi$ 使 $h'(\xi) = \mathrm{e}^{g(\xi)}\bigl(f'(\xi)+g'(\xi)f(\xi)\bigr) = 0$，而 $\mathrm{e}^{g(\xi)}>0$。 $\square$

因子 $\mathrm{e}^{g}$ 的来历：要使 $(\mathrm{e}^{g}f)' = \mathrm{e}^{g}(f'+g'f)$，这与一阶线性微分方程的积分因子是同一个想法（[2.2.15](/2.2.15)）。

**例 5.1.8** 设 $f\in C[1,2]$，在 $(1,2)$ 内可导，证明：(1) 存在 $\xi\in(1,2)$ 使 $f(2)-f(1) = \frac12\xi^2f'(\xi)$；(2) 存在 $\eta\in(1,2)$ 使 $f(2)-f(1) = \eta f'(\eta)\ln2$。

**证明** (1) 取 $g(x) = \frac1x$，由 Cauchy 中值定理 $\frac{f(2)-f(1)}{\frac12-1} = \frac{f'(\xi)}{-1/\xi^2}$，即得。(2) 取 $g(x) = \ln x$，$\frac{f(2)-f(1)}{\ln2} = \frac{f'(\eta)}{1/\eta}$。 $\square$

**例 5.1.9（构造辅助函数）** 设 $f\in C[0,2]$，在 $(0,2)$ 内可导，$f(1) = 0$。用括号内的辅助函数可以证明：

1. 存在 $\xi\in(0,1)$，$f(\xi)+\xi f'(\xi) = 0$（$h(x) = xf(x)$，在 $[0,1]$ 上用 Rolle 定理）；
2. 存在 $\xi\in(1,2)$，$f(\xi) = (2-\xi)f'(\xi)$（$h(x) = (x-2)f(x)$）；
3. 存在 $\xi\in(0,2)$，$f\bigl(\frac\xi2\bigr)+\frac\xi2f'\bigl(\frac\xi2\bigr) = 0$（$h(x) = xf\bigl(\frac x2\bigr)$，$h(0) = h(2) = 0$）；
4. 存在 $\xi\in(0,1)$，$f(1)-f(0) = \sqrt{1-\xi^2}\,\frac{\pi}{2}f'(\xi)$（$g(x) = \arcsin x$，Cauchy 中值定理）；
5. 存在 $\xi\in(0,2)$，$f(2)-f(0) = (1+\xi^2)\arctan2\cdot f'(\xi)$（$g(x) = \arctan x$，Cauchy 中值定理）。

## 5.2. L'Hôpital 法则

两个无穷小量之比或两个无穷大量之比的极限可能是任何值，也可能不存在，这类极限称为不定式（indeterminate form），分别记作 $\frac00$ 型和 $\frac\infty\infty$ 型。前面用**等价无穷小**替换处理过一些不定式；Cauchy 中值定理给出了一种更系统的方法：用导数之比代替函数之比。

**定理 5.2.1（L'Hôpital 法则）** 设

1. $\lim\limits_{x\to x_0^-}f(x) = \lim\limits_{x\to x_0^-}g(x) = 0$；
2. 存在 $\delta>0$，$f$ 与 $g$ 在 $(x_0-\delta,x_0)$ 内可导，且 $g'(x)\ne0$；
3. $\lim\limits_{x\to x_0^-}\frac{f'(x)}{g'(x)} = a$（$a$ 为实数，或为 $+\infty$、$-\infty$、$\infty$），

则 $\lim\limits_{x\to x_0^-}\frac{f(x)}{g(x)} = a$。对 $x\to x_0^+$ 与 $x\to x_0$ 有同样的结论（可导区间相应地取 $(x_0,x_0+\delta)$ 与去心邻域 $N^*(x_0,\delta)$）。

**证明** 补充定义 $f(x_0) = g(x_0) = 0$，则 $f, g$ 在 $(x_0-\delta,x_0]$ 上连续。对任意 $x\in(x_0-\delta,x_0)$，$f, g$ 在 $[x,x_0]$ 上满足 Cauchy 中值定理的条件，所以存在 $\xi_x\in(x,x_0)$ 使

$$
\frac{f(x)}{g(x)} = \frac{f(x)-f(x_0)}{g(x)-g(x_0)} = \frac{f'(\xi_x)}{g'(\xi_x)}.
$$

$x\to x_0^-$ 时 $\xi_x\to x_0^-$，由条件 3 得 $\frac{f(x)}{g(x)}\to a$。 $\square$

**定理 5.2.2** 设 $\lim\limits_{x\to+\infty}f(x) = \lim\limits_{x\to+\infty}g(x) = 0$，$f$ 与 $g$ 在 $[b,+\infty)$ 上可导，$g'(x)\ne0$，且 $\lim\limits_{x\to+\infty}\frac{f'(x)}{g'(x)} = a$（$a$ 为实数或 $\pm\infty$、$\infty$），则 $\lim\limits_{x\to+\infty}\frac{f(x)}{g(x)} = a$。对 $x\to-\infty$（在 $(-\infty,b]$ 上可导）与 $x\to\infty$ 有同样的结论。

**证明** 令 $x = \frac1u$，$F(u) = f\bigl(\frac1u\bigr)$，$G(u) = g\bigl(\frac1u\bigr)$。$x\to+\infty\iff u\to0^+$，而 $\frac{F'(u)}{G'(u)} = \frac{-f'(1/u)/u^2}{-g'(1/u)/u^2} = \frac{f'(x)}{g'(x)}$，对 $F, G$ 用定理 5.2.1 即可。 $\square$

**定理 5.2.3（$\frac\infty\infty$ 型）** 定理 5.2.1、5.2.2 中把条件 1 换成 $\lim f(x) = \lim g(x) = \infty$，结论仍然成立。事实上只需要 $\lim g(x) = \infty$，对 $f$ 的极限没有要求（$\frac{*}{\infty}$ 型）。

**证明**（$x\to x_0^-$，$a$ 有限的情形） 任给 $\varepsilon>0$，取 $c\in(x_0-\delta,x_0)$，使 $(c,x_0)$ 内 $\bigl\lvert\frac{f'}{g'}-a\bigr\rvert<\varepsilon$。对 $x\in(c,x_0)$，由 Cauchy 中值定理，$\frac{f(x)-f(c)}{g(x)-g(c)} = \frac{f'(\xi)}{g'(\xi)}$，$\xi\in(c,x)$，于是

$$
\frac{f(x)}{g(x)} = \frac{f'(\xi)}{g'(\xi)}\Bigl(1-\frac{g(c)}{g(x)}\Bigr)+\frac{f(c)}{g(x)}.
$$

固定 $c$，令 $x\to x_0^-$，由 $g(x)\to\infty$，右端括号趋于 $1$，最后一项趋于 $0$，所以 $\limsup\bigl\lvert\frac{f(x)}{g(x)}-a\bigr\rvert\le\varepsilon$。由 $\varepsilon$ 的任意性即得。 $a$ 为无穷的情形类似。 $\square$

使用 L'Hôpital 法则时要注意：

- 每一步都要先验证是 $\frac00$ 或 $\frac\infty\infty$ 型。若 $f, g$ 的 $1$ 到 $n-1$ 阶导数在该极限过程中仍趋于 $0$（或 $\infty$），且 $\lim\frac{f^{(n)}}{g^{(n)}} = a$，则可以连续使用 $n$ 次：$\lim\frac fg = \lim\frac{f'}{g'} = \cdots = \lim\frac{f^{(n)}}{g^{(n)}} = a$。
- 条件 3 不满足时法则不给出任何结论。例如 $\lim\limits_{x\to\infty}\frac{x+\sin x}{x} = 1$，而 $\frac{(x+\sin x)'}{x'} = 1+\cos x$ 没有极限。
- 先用等价无穷小替换乘除因子、先把极限非零的因子分离出去，往往能大大简化求导。

**例 5.2.1** 求 $\lim\limits_{x\to0}\frac{\mathrm{e}^x-x-\cos x}{x^2}$。

解：两次使用 L'Hôpital 法则（每次都是 $\frac00$ 型）：

$$
\lim_{x\to0}\frac{\mathrm{e}^x-x-\cos x}{x^2} = \lim_{x\to0}\frac{\mathrm{e}^x-1+\sin x}{2x} = \lim_{x\to0}\frac{\mathrm{e}^x+\cos x}{2} = 1.
$$

对比：若题目是 $\lim\limits_{x\to0}\frac{\mathrm{e}^x-\cos x}{x^2}$，写成 $\lim\frac{\mathrm{e}^x+\sin x}{2x} = \lim\frac{\mathrm{e}^x+\cos x}{2} = 1$ 是错的：第一步之后分子趋于 $1$，已不是不定式。正确结果是 $\lim\frac{\mathrm{e}^x+\sin x}{2x} = \infty$。

**例 5.2.2** 求 $\lim\limits_{x\to0}\frac{x-\sin x}{x-x\cos x}$。

解：方法一，直接用三次 L'Hôpital 法则：

$$
\lim_{x\to0}\frac{1-\cos x}{1-\cos x+x\sin x} = \lim_{x\to0}\frac{\sin x}{2\sin x+x\cos x} = \lim_{x\to0}\frac{\cos x}{3\cos x-x\sin x} = \frac13.
$$

方法二，先用 $1-\cos x\sim\frac{x^2}2$ 替换分母，再用 L'Hôpital 法则：

$$
\lim_{x\to0}\frac{x-\sin x}{x(1-\cos x)} = \lim_{x\to0}\frac{x-\sin x}{\frac12x^3} = \lim_{x\to0}\frac{1-\cos x}{\frac32x^2} = \frac13.
$$

**例 5.2.3** 求 $\lim\limits_{x\to+\infty}\frac{\frac\pi2-\arctan x}{\sin\frac1x}$。

解：$\sin\frac1x\sim\frac1x$，

$$
\lim_{x\to+\infty}\frac{\frac\pi2-\arctan x}{1/x} = \lim_{x\to+\infty}\frac{-1/(1+x^2)}{-1/x^2} = \lim_{x\to+\infty}\frac{x^2}{1+x^2} = 1.
$$

**例 5.2.4** 证明 $\lim\limits_{x\to+\infty}\frac{x^\alpha}{a^x} = 0$（$a>1$，$\alpha>0$）。

**证明** 取正整数 $k$ 使 $k-1<\alpha\le k$，连续使用 $k$ 次 L'Hôpital 法则（每次都是 $\frac\infty\infty$ 型）：

$$
\lim_{x\to+\infty}\frac{x^\alpha}{a^x} = \lim_{x\to+\infty}\frac{\alpha x^{\alpha-1}}{a^x\ln a} = \cdots = \lim_{x\to+\infty}\frac{\alpha(\alpha-1)\cdots(\alpha-k+1)x^{\alpha-k}}{(\ln a)^ka^x} = 0. \qquad\square
$$

**例 5.2.5** 证明对任意 $\alpha>0$，$\beta>0$，$\lim\limits_{x\to+\infty}\frac{(\ln x)^\beta}{x^\alpha} = 0$。

**证明** $\lim\limits_{x\to+\infty}\frac{(\ln x)^\beta}{x^\alpha} = \lim\limits_{x\to+\infty}\frac{\beta(\ln x)^{\beta-1}}{\alpha x^\alpha}$，每用一次法则 $\ln x$ 的幂次降低 $1$；用 $k$ 次（$k-1<\beta\le k$）后分子的幂次 $\beta-k\le0$，极限为 $0$。也可令 $x = \mathrm{e}^t$ 化为例 5.2.4。 $\square$

例 5.2.4、5.2.5 说明，$x\to+\infty$ 时三类无穷大的增长速度满足

$$
(\ln x)^\beta\ll x^\alpha\ll a^x\qquad(\alpha,\beta>0,\ a>1),
$$

其中 $u\ll v$ 表示 $u/v\to0$。

其他不定式。$0\cdot\infty$、$\infty-\infty$、$0^0$、$1^\infty$、$\infty^0$ 型都可以化为 $\frac00$ 或 $\frac\infty\infty$ 型：

- $0\cdot\infty$：$fg = \frac{f}{1/g}$ 或 $\frac{g}{1/f}$；
- $\infty-\infty$：通分或有理化；
- $0^0$、$1^\infty$、$\infty^0$：$u^v = \mathrm{e}^{v\ln u}$，指数 $v\ln u$ 是 $0\cdot\infty$ 型，再由指数函数的连续性与**复合极限定理**取极限。

**例 5.2.6** 求极限：(1) $\lim\limits_{x\to0}\Bigl(\frac1{x^2}-\cot^2x\Bigr)$；(2) $\lim\limits_{x\to0^+}\ln x\tan x$；(3) $\lim\limits_{x\to+\infty}\bigl(\frac\pi2-\arctan x\bigr)^{\frac1{\ln x}}$；(4) $\lim\limits_{x\to0^+}(\cot x)^{\frac1{\ln x}}$。

解：(1) $\infty-\infty$ 型，通分后用 $\sin^2x\sim x^2$：

$$
\lim_{x\to0}\frac{\sin^2x-x^2\cos^2x}{x^2\sin^2x} = \lim_{x\to0}\frac{\sin^2x-x^2\cos^2x}{x^4} = \lim_{x\to0}\frac{\sin x\cos x-x\cos^2x+x^2\sin x\cos x}{2x^3}.
$$

分子 $= \frac12\sin2x-x\cos^2x+\frac12x^2\sin2x$，再用一次法则：

$$
\lim_{x\to0}\frac{\cos2x-\cos^2x+x\sin2x+x\sin2x+x^2\cos2x}{6x^2} = \lim_{x\to0}\frac{-\sin^2x+2x\sin2x+x^2\cos2x}{6x^2} = \frac{-1+4+1}{6} = \frac23.
$$

(2) $0\cdot\infty$ 型：$\lim\limits_{x\to0^+}\frac{\ln x}{\cot x} = \lim\limits_{x\to0^+}\frac{1/x}{-\csc^2x} = -\lim\limits_{x\to0^+}\frac{\sin^2x}{x} = 0$。

(3) $0^0$ 型：指数 $\frac{\ln(\frac\pi2-\arctan x)}{\ln x}$ 是 $\frac\infty\infty$ 型，

$$
\lim_{x\to+\infty}\frac{\ln(\frac\pi2-\arctan x)}{\ln x} = \lim_{x\to+\infty}\frac{-x}{(\frac\pi2-\arctan x)(1+x^2)} = -1,
$$

最后一步用例 5.2.3 的结果 $\frac\pi2-\arctan x\sim\frac1x$。所以原极限为 $\mathrm{e}^{-1}$。

(4) $\infty^0$ 型：

$$
\lim_{x\to0^+}\frac{\ln\cot x}{\ln x} = \lim_{x\to0^+}\frac{-\csc^2x/\cot x}{1/x} = -\lim_{x\to0^+}\frac{x}{\sin x\cos x} = -1,
$$

原极限为 $\mathrm{e}^{-1}$。

## 5.3. 函数的极值及其应用

### 5.3.1. 函数的极值

由 Fermat 定理，可导函数的极值点一定是驻点，但驻点只是可能的极值点。不可导的点也可能是极值点（如 $|x|$ 在 $0$ 点）。所以初等函数的极值点只可能是驻点或不可导点，需要逐个判断。

**定理 5.3.1（第一判别法）** 设 $f$ 在 $x_0$ 点连续，在某个去心邻域 $N^*(x_0,\delta)$ 内可导。

1. 若在 $(x_0-\delta,x_0)$ 内 $f'(x)\ge0$，在 $(x_0,x_0+\delta)$ 内 $f'(x)\le0$，则 $f$ 在 $x_0$ 取极大值；
2. 若在 $(x_0-\delta,x_0)$ 内 $f'(x)\le0$，在 $(x_0,x_0+\delta)$ 内 $f'(x)\ge0$，则 $f$ 在 $x_0$ 取极小值。

**证明** 1. 由推论 5.1.2，$f$ 在 $(x_0-\delta,x_0]$ 上单调非减，在 $[x_0,x_0+\delta)$ 上单调非增（这里用到 $f$ 在 $x_0$ 连续），所以 $x_0$ 是极大值点。2 同理。 $\square$

$x_0$ 处的连续性不能省略：$f(x) = |x|$（$x\ne0$）、$f(0) = 1$ 在 $0$ 点两侧满足 2 的条件，但 $0$ 是极大值点。若 $f'$ 在 $x_0$ 两侧不变号，则 $x_0$ 不是极值点。

**定理 5.3.2（第二判别法）** 设 $f$ 在 $x_0$ 的某邻域内可导，$f'(x_0) = 0$，$f''(x_0)$ 存在。若 $f''(x_0)>0$，则 $f$ 在 $x_0$ 取极小值；若 $f''(x_0)<0$，则 $f$ 在 $x_0$ 取极大值。

**证明** 设 $f''(x_0)>0$。由 $\lim\limits_{x\to x_0}\frac{f'(x)}{x-x_0} = \lim\limits_{x\to x_0}\frac{f'(x)-f'(x_0)}{x-x_0} = f''(x_0)>0$ 及函数极限的局部保号性，存在 $\delta>0$，在 $N^*(x_0,\delta)$ 内 $\frac{f'(x)}{x-x_0}>0$，即 $f'$ 在 $x_0$ 左侧为负、右侧为正。由定理 5.3.1，$x_0$ 是极小值点。 $\square$

$f''(x_0) = 0$ 时第二判别法失效：$x^4$、$-x^4$、$x^3$ 在 $0$ 点分别取极小值、取极大值、不取极值。这时可用更高阶导数（5.5 节的 Taylor 公式）或第一判别法。

**例 5.3.1** 求 $f(x) = x^{2/3}(x^2-4)$ 的极值。

解：$f'(x) = \frac23x^{-1/3}(x^2-4)+2x\cdot x^{2/3} = \frac83(x^2-1)x^{-1/3}$，驻点 $x = \pm1$，另外 $x = 0$ 是不可导点。$f''(x) = \frac89(5x^2+1)x^{-4/3}$，$f''(\pm1)>0$，所以 $f(\pm1) = -3$ 是极小值。在 $0$ 点左侧附近 $f'(x)>0$，右侧附近 $f'(x)<0$，由定理 5.3.1，$f(0) = 0$ 是极大值。

**例 5.3.2** 设 $f(x) = a\sin x+\frac13\sin3x$ 在 $x = \frac\pi3$ 取得极值，求 $a$，并判断是极大值还是极小值。

解：$f'(x) = a\cos x+\cos3x$，$f'\bigl(\frac\pi3\bigr) = \frac a2-1 = 0$，$a = 2$。$f''(x) = -2\sin x-3\sin3x$，$f''\bigl(\frac\pi3\bigr) = -\sqrt3<0$，所以 $f\bigl(\frac\pi3\bigr) = \sqrt3$ 是极大值。

**例 5.3.3** 设 $y = y(x)$ 由方程 $2y^3-2y^2+2xy-x^2 = 1$ 确定，求 $y(x)$ 的极值。

解：两边对 $x$ 求导：$(6y^2-4y+2x)y'+2y-2x = 0$，$y' = \frac{x-y}{3y^2-2y+x}$。由 $y' = 0$ 得 $x = y$，代入方程得 $2x^3-x^2-1 = (x-1)(2x^2+x+1) = 0$，$x = 1$，$y(1) = 1$。在 $x = 1$ 处（用 $y' = 0$）

$$
y''(1) = \frac{(1-y')(3y^2-2y+x)-(x-y)(6yy'-2y'+1)}{(3y^2-2y+x)^2}\bigg|_{x=y=1} = \frac{2}{4} = \frac12>0,
$$

所以 $y(1) = 1$ 是极小值。

### 5.3.2. 函数的最大值和最小值

闭区间上的连续函数一定有最大值和最小值（**最大最小值定理**）。最值点要么是区间内部的极值点（从而是驻点或不可导点），要么是区间的端点。所以求最值时，只需比较内部驻点、不可导点与端点处的函数值。

**例 5.3.4** 求 $f(x) = \frac{x^2-5x+6}{x^2+1}$ 在 $[-1,3]$ 上的最大值和最小值。

解：$f'(x) = \frac{5(x^2-2x-1)}{(x^2+1)^2}$，驻点 $x_1 = 1-\sqrt2$，$x_2 = 1+\sqrt2$，都在 $[-1,3]$ 内。

$$
f(x_1) = \frac{4+3\sqrt2}{4-2\sqrt2} = \frac{7+5\sqrt2}{2}\approx7.04,\qquad f(x_2) = \frac{4-3\sqrt2}{4+2\sqrt2} = \frac{7-5\sqrt2}{2}\approx-0.036,
$$

端点处 $f(-1) = 6$，$f(3) = 0$。比较得最大值 $f(1-\sqrt2) = \frac{7+5\sqrt2}{2}$，最小值 $f(1+\sqrt2) = \frac{7-5\sqrt2}{2}$。

**例 5.3.5** 求 $f(x) = x\mathrm{e}^{-x^2}$ 在 $(-\infty,+\infty)$ 上的最大值和最小值。

解：区间无界，先说明最值存在。$x\to\infty$ 时 $f(x)\to0$，而 $f(1)>0$，$f(-1)<0$，所以存在 $M>1$，$|x|>M$ 时 $f(-1)<f(x)<f(1)$。$f$ 在 $[-M,M]$ 上的最值就是在 $\mathbb{R}$ 上的最值，且不在端点 $\pm M$ 取得，因此在内部驻点取得。由 $f'(x) = (1-2x^2)\mathrm{e}^{-x^2} = 0$ 得 $x = \pm\frac{1}{\sqrt2}$，最大值 $f\bigl(\frac1{\sqrt2}\bigr) = \frac{1}{\sqrt{2\mathrm{e}}}$，最小值 $f\bigl(-\frac1{\sqrt2}\bigr) = -\frac{1}{\sqrt{2\mathrm{e}}}$。

实际问题中常常只有一个驻点，这时有下面的简便判别。

**定理 5.3.3（唯一驻点定理）** 设 $f$ 在区间 $I$ 上处处可导，在 $I$ 的内部只有唯一的驻点 $x_0$。若 $f(x_0)$ 是极小值，则它是 $f$ 在 $I$ 上的最小值；若 $f(x_0)$ 是极大值，则它是 $f$ 在 $I$ 上的最大值。

**证明** 设 $f(x_0)$ 是极小值但不是最小值，则存在 $x_1\in I$ 使 $f(x_1)<f(x_0)$，不妨设 $x_1<x_0$。在 $x_0$ 左侧附近 $f(x)\ge f(x_0)$。若这些点上都有 $f(x) = f(x_0)$，则 $f$ 在一个区间上是常数，那里的点都是驻点，与唯一性矛盾；否则存在 $x_2\in(x_1,x_0)$ 使 $f(x_2)>f(x_0)>f(x_1)$。于是 $f$ 在 $[x_1,x_0]$ 上的最大值大于两端点的值，在内点 $\xi$ 取得，$\xi$ 是另一个驻点，矛盾。极大值的情形同理。 $\square$

**例 5.3.6** 电源电动势为 $E$、内阻为 $r$，外接负载电阻 $R$。$R$ 多大时负载得到的功率最大？

解：电流 $I = \frac{E}{r+R}$，负载功率 $P(R) = I^2R = \frac{E^2R}{(r+R)^2}$，$R\in(0,+\infty)$。$P'(R) = \frac{E^2(r-R)}{(r+R)^3} = 0$ 得唯一驻点 $R = r$，且 $P''(r) = -\frac{E^2}{8r^3}<0$，$R = r$ 是极大值点。由定理 5.3.3，$R = r$ 时功率最大，最大功率为 $\frac{E^2}{4r}$（阻抗匹配）。

### 5.3.3. 用极值证明不等式

要证明 $f(x)\le g(x)$（$x\in I$），可令 $F = g-f$，求 $F$ 在 $I$ 上的最小值（或下确界）；若它非负，不等式成立。常常配合单调性：若 $F(a) = 0$ 且 $F'\ge0$，则 $x\ge a$ 时 $F(x)\ge0$。

**例 5.3.7** 设 $p, q, a, b$ 都是正数，$\frac1p+\frac1q = 1$，证明 $ab\le\frac{a^p}{p}+\frac{b^q}{q}$。

**证明** 令 $F(x) = \frac{a^p}{p}+\frac{x^q}{q}-ax$（$x>0$），$F'(x) = x^{q-1}-a$，唯一驻点 $x_0 = a^{\frac1{q-1}}$。由 $\frac1p+\frac1q = 1$ 知 $q>1$，$F''(x_0) = (q-1)x_0^{q-2}>0$，$x_0$ 是极小值点，由定理 5.3.3 也是最小值点。又 $\frac{q}{q-1} = p$，

$$
F(x_0) = \frac{a^p}{p}+\frac{a^{p}}{q}-a^{p} = a^p\Bigl(\frac1p+\frac1q-1\Bigr) = 0.
$$

所以 $F(x)\ge0$，取 $x = b$ 即得。 $\square$

这个不等式称为 Young 不等式（Young's inequality for products），等号当且仅当 $a^p = b^q$ 时成立。$p = q = 2$ 时就是 $ab\le\frac{a^2+b^2}{2}$。由它可以推出 Hölder 不等式，后者推广了 **Cauchy–Schwarz 不等式**。

**例 5.3.8** 证明：(1) $x>0$ 时 $\ln(1+x)>\frac{\arctan x}{1+x}$；(2) $x\in[0,1]$，$p>1$ 时 $\frac{1}{2^{p-1}}\le x^p+(1-x)^p\le1$。

**证明** (1) 令 $f(x) = (1+x)\ln(1+x)-\arctan x$，$f(0) = 0$，$x>0$ 时 $f'(x) = \ln(1+x)+1-\frac1{1+x^2}>0$，$f$ 在 $[0,+\infty)$ 上严格增加，故 $f(x)>0$。

(2) $f(x) = x^p+(1-x)^p$ 在 $[0,1]$ 上的最值只能在端点或内部驻点取得。$f'(x) = p\bigl[x^{p-1}-(1-x)^{p-1}\bigr] = 0$ 得 $x = \frac12$。$f(0) = f(1) = 1$，$f\bigl(\frac12\bigr) = \frac1{2^{p-1}}$，所以最小值为 $\frac1{2^{p-1}}$，最大值为 $1$。 $\square$

**例 5.3.9** 设 $f$ 在 $\mathbb{R}$ 上二阶可导且 $f''>0$，证明对任意 $x$ 与非零实数 $h$，$f(x+h)+f(x-h)>2f(x)$。

**证明** 固定 $x$，令 $F(h) = f(x+h)+f(x-h)-2f(x)$，$F(0) = 0$。$F'(h) = f'(x+h)-f'(x-h)$，$F'(0) = 0$；$F''(h) = f''(x+h)+f''(x-h)>0$，所以 $F'$ 严格增加，$h = 0$ 是唯一驻点，且为极小值点。由定理 5.3.3，$F(0) = 0$ 是唯一的最小值，$h\ne0$ 时 $F(h)>0$。 $\square$

（这是 5.4 节中凸函数的一个性质：$f\bigl(\frac{u+v}2\bigr)<\frac{f(u)+f(v)}{2}$。）

**例 5.3.10** 已知方程 $kx+\frac1{x^2} = 1$ 在 $(0,+\infty)$ 内有唯一的根，求 $k$。

解：令 $F(x) = kx+\frac1{x^2}-1$（$x>0$），$F'(x) = k-\frac2{x^3}$。

- $k\le0$ 时 $F'<0$，$F$ 严格减少；$x\to0^+$ 时 $F\to+\infty$，$x\to+\infty$ 时 $F\to-\infty$（$k<0$）或 $F\to-1$（$k = 0$），$F$ 有唯一零点。
- $k>0$ 时 $F$ 有唯一驻点 $x_0 = \sqrt[3]{2/k}$，$F''(x_0)>0$，$F(x_0) = \frac{3}{\sqrt[3]4}k^{2/3}-1$ 是最小值。$F(x_0) = 0$，即 $k = \frac{2\sqrt3}{9}$ 时方程有唯一根；$k>\frac{2\sqrt3}9$ 时 $F>0$，无根；$0<k<\frac{2\sqrt3}9$ 时 $F(x_0)<0$，而 $x\to0^+$ 与 $x\to+\infty$ 时 $F\to+\infty$，方程有两个根。

所以 $k\le0$ 或 $k = \frac{2\sqrt3}{9}$。

## 5.4. 函数图形的描绘

### 5.4.1. 曲线的凸性

单调性只说明曲线上升还是下降，同样是上升，曲线可以向上弯曲（如 $\mathrm{e}^x$），也可以向下弯曲（如 $\ln x$）。凸性刻画弯曲的方向：曲线上任意两点之间的弧位于弦的下方（或上方）。设 $x = \lambda_1x_1+\lambda_2x_2$（$\lambda_1,\lambda_2\ge0$，$\lambda_1+\lambda_2 = 1$）是 $x_1, x_2$ 之间的点，弦上对应的纵坐标是 $\lambda_1f(x_1)+\lambda_2f(x_2)$。

**定义 5.4.1** 设 $f$ 在 $[a,b]$ 上有定义。若对任意 $x_1,x_2\in[a,b]$ 及满足 $\lambda_1+\lambda_2 = 1$ 的任意非负数 $\lambda_1,\lambda_2$，都有

$$
f(\lambda_1x_1+\lambda_2x_2)\le\lambda_1f(x_1)+\lambda_2f(x_2),
$$
则称 $f$ 为 $[a,b]$ 上的**凸函数**（课件称为下凸函数）；若不等号反向（$\ge$），则称 $f$ 为 $[a,b]$ 上的**凹函数**（课件称为上凸函数）。若 $x_1\ne x_2$、$\lambda_1\lambda_2\ne0$ 时不等号严格成立，称为严格凸（凹）。

本站采用国际通行的叫法：凸函数（convex）是"弧在弦下"，如 $x^2$、$\mathrm{e}^x$；凹函数（concave）是"弧在弦上"，如 $\ln x$、$\sqrt x$。$f$ 是凹函数当且仅当 $-f$ 是凸函数，所以下面只叙述凸函数。

**定理 5.4.1（Jensen 不等式）** $f$ 在 $[a,b]$ 上为凸函数，当且仅当对任意 $x_1,\dots,x_n\in[a,b]$ 及满足 $\lambda_1+\cdots+\lambda_n = 1$ 的任意非负实数 $\lambda_i$，都有

$$
f(\lambda_1x_1+\cdots+\lambda_nx_n)\le\lambda_1f(x_1)+\cdots+\lambda_nf(x_n).
$$

凹函数的不等号反向。

**证明** 充分性：取 $n = 2$。必要性：对 $n$ 归纳，$n = 1, 2$ 成立。设 $n = k$ 时成立，考察 $k+1$ 个点。若 $\lambda_k+\lambda_{k+1} = 0$，归结为 $n = k-1$ 的情形；否则把最后两项合并：

$$
\begin{aligned}
f\Bigl(\sum_{i=1}^{k+1}\lambda_ix_i\Bigr) &= f\Bigl(\sum_{i=1}^{k-1}\lambda_ix_i+(\lambda_k+\lambda_{k+1})\Bigl(\frac{\lambda_k}{\lambda_k+\lambda_{k+1}}x_k+\frac{\lambda_{k+1}}{\lambda_k+\lambda_{k+1}}x_{k+1}\Bigr)\Bigr)\\
&\le\sum_{i=1}^{k-1}\lambda_if(x_i)+(\lambda_k+\lambda_{k+1})f\Bigl(\frac{\lambda_kx_k+\lambda_{k+1}x_{k+1}}{\lambda_k+\lambda_{k+1}}\Bigr)\\
&\le\sum_{i=1}^{k-1}\lambda_if(x_i)+\lambda_kf(x_k)+\lambda_{k+1}f(x_{k+1}),
\end{aligned}
$$

第一个不等号用归纳假设（$k$ 个点），第二个用 $n = 2$ 的情形。 $\square$

几何上，$\sum\lambda_i(x_i,f(x_i))$ 是曲线上 $n$ 个点的加权平均（重心），它落在这些点构成的凸多边形内，而凸函数图形上方的区域是凸集。在概率论中，Jensen 不等式写成 $f(\mathbb{E}[X])\le\mathbb{E}[f(X)]$。

**定理 5.4.2（凸性的导数判别）** (1) 设 $f\in C[a,b]$ 且在 $(a,b)$ 内可导，则 $f$ 在 $[a,b]$ 上为凸函数（凹函数）当且仅当 $f'$ 在 $(a,b)$ 内单调非减（非增）。

(2) 设 $f\in C[a,b]$ 且在 $(a,b)$ 内二阶可导，则 $f$ 在 $[a,b]$ 上为凸函数（凹函数）当且仅当在 $(a,b)$ 内 $f''(x)\ge0$（$\le0$）。

**证明** (1) 只证凸函数的情形。必要性：任取 $a<x_1<x<x_2<b$，把 $x = \frac{x_2-x}{x_2-x_1}x_1+\frac{x-x_1}{x_2-x_1}x_2$ 代入凸性定义，整理得三条弦的斜率关系

$$
\frac{f(x)-f(x_1)}{x-x_1}\le\frac{f(x_2)-f(x_1)}{x_2-x_1}\le\frac{f(x_2)-f(x)}{x_2-x}.
$$

令左端 $x\to x_1^+$、右端 $x\to x_2^-$，得 $f'(x_1)\le\frac{f(x_2)-f(x_1)}{x_2-x_1}\le f'(x_2)$。

充分性：设 $f'$ 单调非减，$a\le x_1<x_2\le b$，$\lambda_1,\lambda_2>0$，$\lambda_1+\lambda_2 = 1$，$x = \lambda_1x_1+\lambda_2x_2$，则 $x-x_1 = \lambda_2(x_2-x_1)$，$x_2-x = \lambda_1(x_2-x_1)$。由 Lagrange 中值定理，存在 $\xi\in(x_1,x)$，$\eta\in(x,x_2)$ 使

$$
\lambda_1f(x_1)+\lambda_2f(x_2)-f(x) = \lambda_1\bigl(f(x_1)-f(x)\bigr)+\lambda_2\bigl(f(x_2)-f(x)\bigr) = \lambda_1\lambda_2(x_2-x_1)\bigl(f'(\eta)-f'(\xi)\bigr)\ge0.
$$

(2) 由 (1) 与推论 5.1.2：$f'$ 单调非减 $\iff$ $f''\ge0$。 $\square$

由证明可知，$f''>0$ 时 $f$ 严格凸。几何上 $f$ 凸当且仅当切线斜率随 $x$ 增加，此时曲线位于每条切线的上方：$f(x)\ge f(x_0)+f'(x_0)(x-x_0)$。

**定义 5.4.2** 设 $M$ 是曲线 $y = f(x)$ 上的一点，若曲线在 $M$ 点两侧有不同的凸性，则称 $M$ 为曲线的**拐点**。

**推论 5.4.1** 设 $f$ 在 $x_0$ 的某邻域内可导，$f''(x_0)$ 存在。若 $M(x_0,f(x_0))$ 是拐点，则 $f''(x_0) = 0$。

**证明** 由定理 5.4.2 (1)，$f'$ 在 $x_0$ 两侧单调性相反，所以 $x_0$ 是 $f'$ 的极值点，由 Fermat 定理 $(f')'(x_0) = f''(x_0) = 0$。 $\square$

所以拐点只可能出现在 $f'' = 0$ 的点或 $f''$ 不存在的点，例如 $y = \sqrt[3]x$ 在 $0$ 点二阶导数不存在，$(0,0)$ 却是拐点。反过来 $f''(x_0) = 0$ 不保证拐点：$x^4$ 在 $0$ 点 $f'' = 0$，但它处处凸。

**例 5.4.1** 讨论 $y = \mathrm{e}^{-x^2}$ 的凸性与拐点。

解：$y' = -2x\mathrm{e}^{-x^2}$，$y'' = (4x^2-2)\mathrm{e}^{-x^2}$，由 $y'' = 0$ 得 $x = \pm\frac1{\sqrt2}$。

| $x$ | $\bigl(-\infty,-\frac1{\sqrt2}\bigr)$ | $-\frac1{\sqrt2}$ | $\bigl(-\frac1{\sqrt2},\frac1{\sqrt2}\bigr)$ | $\frac1{\sqrt2}$ | $\bigl(\frac1{\sqrt2},+\infty\bigr)$ |
|---|---|---|---|---|---|
| $y''$ | $+$ | $0$ | $-$ | $0$ | $+$ |
| $y$ | 凸 | 拐点 | 凹 | 拐点 | 凸 |

拐点为 $\bigl(\pm\frac1{\sqrt2},\mathrm{e}^{-1/2}\bigr)$。这条钟形曲线是正态分布密度的形状，拐点到对称轴的距离就是标准差（这里 $\sigma = \frac1{\sqrt2}$）。

**例 5.4.2** 证明：若 $x_1,\dots,x_n$ 为非负实数，则 $\sqrt[n]{x_1x_2\cdots x_n}\le\frac{x_1+\cdots+x_n}{n}$。

**证明** $f(x) = \ln x$ 在 $(0,+\infty)$ 上 $f''(x) = -\frac1{x^2}<0$，由定理 5.4.2 是凹函数。由 Jensen 不等式（取 $\lambda_i = \frac1n$），

$$
\ln\frac{x_1+\cdots+x_n}{n}\ge\frac{\ln x_1+\cdots+\ln x_n}{n} = \ln\sqrt[n]{x_1\cdots x_n},
$$

再由 $\ln$ 的单调性即得。$x_i$ 中有 $0$ 时不等式显然。 $\square$

这就是算术–几何平均不等式（inequality of arithmetic and geometric means）。同样的论证给出加权形式与幂平均形式：若 $x_i\ge0$，$\lambda_i\ge0$，$\sum\lambda_i = 1$，则

$$
x_1^{\lambda_1}\cdots x_n^{\lambda_n}\le\lambda_1x_1+\cdots+\lambda_nx_n,\qquad x_1^{\lambda_1}\cdots x_n^{\lambda_n}\le\bigl(\lambda_1x_1^q+\cdots+\lambda_nx_n^q\bigr)^{1/q}\ \ (q>0).
$$

第二式由第一式用 $x_i^q$ 代 $x_i$ 得到。加权形式取 $n = 2$、$\lambda_1 = \frac1p$、$x_1 = a^p$、$x_2 = b^q$，就是例 5.3.7 的 Young 不等式。又如对凸函数 $x^p$（$p\ge1$）用 Jensen 不等式，得 $\bigl(\frac{x_1+x_2+x_3}{3}\bigr)^p\le\frac{x_1^p+x_2^p+x_3^p}{3}$（$x_i\ge0$）。

至此，证明不等式有三种常用方法：(1) 求函数的最大值或最小值（5.3.3 节）；(2) 利用函数的凸性（Jensen 不等式）；(3) 利用 Lagrange 中值定理：若 $f'$ 在 $x, y$ 之间满足 $m\le f'\le M$，则 $m(y-x)\le f(y)-f(x)\le M(y-x)$（$y>x$），如例 5.1.3。

### 5.4.2. 函数的作图

函数 $f$ 的图形是点 $(x,f(x))$ 的轨迹。作图时不可能描出所有的点，只能描出"关键点"并确定各段的形状：定义域；对称性（奇偶性）与周期性；单调区间与极值点；凸性区间与拐点；渐近线。前四项前面已经讨论，下面讨论渐近线。

**定义 5.4.3** 若曲线 $y = f(x)$ 上的点沿曲线无限远离原点时，它到某条直线的距离趋于零，则称该直线为曲线的一条**渐近线**。按方向分为**竖直渐近线**、**水平渐近线**与**斜渐近线**。

1. 直线 $x = x_0$ 是竖直渐近线，当且仅当 $x\to x_0^+$ 或 $x\to x_0^-$ 时 $f(x)\to\infty$。此时 $x_0$ 是 $f$ 的无穷间断点（或定义域的端点）。
2. 直线 $y = y_0$ 是水平渐近线，当且仅当 $y_0 = \lim\limits_{x\to+\infty}f(x)$ 或 $y_0 = \lim\limits_{x\to-\infty}f(x)$。

**定理 5.4.3（斜渐近线）** 设 $f$ 在 $[c,+\infty)$ 上有定义，则直线 $y = ax+b$ 是曲线 $y = f(x)$ 在 $x\to+\infty$ 时的渐近线，当且仅当

$$
\lim_{x\to+\infty}\frac{f(x)}{x} = a,\qquad\lim_{x\to+\infty}\bigl(f(x)-ax\bigr) = b.
$$

$x\to-\infty$ 时类似。$a = 0$ 时就是水平渐近线。

**证明** 点 $(x,f(x))$ 到直线的距离为 $\frac{|f(x)-ax-b|}{\sqrt{1+a^2}}$，所以 $y = ax+b$ 是渐近线当且仅当 $\lim\limits_{x\to+\infty}(f(x)-ax-b) = 0$，即 $\lim(f(x)-ax) = b$。此时 $\frac{f(x)}x-a = \frac{f(x)-ax-b}{x}+\frac bx\to0$。反之由两个极限直接得到 $f(x)-ax-b\to0$。 $\square$

**算法 5.4.1（函数作图）**

1. 求定义域，判断奇偶性、周期性（有对称性时只需作一部分）；
2. 求 $f'$，找出驻点与不可导点，确定单调区间与极值；
3. 求 $f''$，找出 $f'' = 0$ 与 $f''$ 不存在的点，确定凸性区间与拐点；
4. 把以上分点从小到大列表，逐段写出 $f'$、$f''$ 的符号与曲线的形状；
5. 求竖直、水平与斜渐近线；
6. 计算极值点、拐点及与坐标轴交点的坐标，描点连线。

**例 5.4.3** 作 $f(x) = \frac{(x-1)^3}{(x+1)^2}$ 的图形。

解：定义域为 $(-\infty,-1)\cup(-1,+\infty)$，没有奇偶性与周期性。

$$
f'(x) = \frac{(x-1)^2(x+5)}{(x+1)^3},\qquad f''(x) = \frac{24(x-1)}{(x+1)^4}.
$$

驻点 $x = -5$、$x = 1$；$f''(x) = 0$ 得 $x = 1$。列表：

| $x$ | $(-\infty,-5)$ | $-5$ | $(-5,-1)$ | $-1$ | $(-1,1)$ | $1$ | $(1,+\infty)$ |
|---|---|---|---|---|---|---|---|
| $f'$ | $+$ | $0$ | $-$ | 无定义 | $+$ | $0$ | $+$ |
| $f''$ | $-$ | $-$ | $-$ | 无定义 | $-$ | $0$ | $+$ |
| $f$ | 增，凹 | 极大值 $-13.5$ | 减，凹 | | 增，凹 | 拐点 $(1,0)$ | 增，凸 |

$x = 1$ 是驻点但 $f'$ 在两侧不变号，不是极值点，而是拐点（切线水平）。渐近线：$\lim\limits_{x\to-1}f(x) = -\infty$，$x = -1$ 是竖直渐近线；$\lim\limits_{x\to\infty}\frac{f(x)}{x} = 1$，$\lim\limits_{x\to\infty}(f(x)-x) = \lim\limits_{x\to\infty}\frac{-5x^2+2x-1}{(x+1)^2} = -5$，$y = x-5$ 是两侧的斜渐近线。

![f(x) = (x − 1)³/(x + 1)² 的图形：竖直渐近线 x = −1，斜渐近线 y = x − 5，极大值点 (−5, −13.5)，拐点 (1, 0)](./plots/curve-sketching.py)

**例 5.4.4** 作 $y = x\mathrm{e}^{-x^2}$ 的图形。

解：定义域为 $\mathbb{R}$，奇函数，图形关于原点对称，只需讨论 $x\ge0$。$y' = (1-2x^2)\mathrm{e}^{-x^2}$，驻点 $x = \frac1{\sqrt2}$；$y'' = 2x(2x^2-3)\mathrm{e}^{-x^2}$，$y'' = 0$ 得 $x = 0$、$x = \sqrt{3/2}$。

| $x$ | $0$ | $\bigl(0,\frac1{\sqrt2}\bigr)$ | $\frac1{\sqrt2}$ | $\bigl(\frac1{\sqrt2},\sqrt{\frac32}\bigr)$ | $\sqrt{\frac32}$ | $\bigl(\sqrt{\frac32},+\infty\bigr)$ |
|---|---|---|---|---|---|---|
| $y'$ | $+$ | $+$ | $0$ | $-$ | $-$ | $-$ |
| $y''$ | $0$ | $-$ | $-$ | $-$ | $0$ | $+$ |
| $y$ | 拐点 $(0,0)$ | 增，凹 | 极大值 $\frac1{\sqrt{2\mathrm{e}}}$ | 减，凹 | 拐点 | 减，凸 |

拐点 $\bigl(\pm\sqrt{3/2},\pm\sqrt{3/2}\,\mathrm{e}^{-3/2}\bigr)$ 与 $(0,0)$，极小值 $-\frac1{\sqrt{2\mathrm{e}}}$ 在 $x = -\frac1{\sqrt2}$ 取得；$\lim\limits_{x\to\infty}x\mathrm{e}^{-x^2} = 0$，$y = 0$ 是水平渐近线。

## 5.5. Taylor 公式及其应用

### 5.5.1. 函数在一点的 Taylor 公式

由微分，$f(x) = f(x_0)+f'(x_0)(x-x_0)+o(x-x_0)$，即在 $x_0$ 附近用一次多项式近似 $f$，误差是 $x-x_0$ 的高阶无穷小，精度不够。多项式是"简单、熟悉"的函数，自然想到用高次多项式

$$
p(x) = a_0+a_1(x-x_0)+a_2(x-x_0)^2+\cdots+a_n(x-x_0)^n
$$

在 $x_0$ 附近逼近 $f$。至少要求 $p$ 与 $f$ 在 $x_0$ 点"行为相同"：$p^{(k)}(x_0) = f^{(k)}(x_0)$（$k = 0,1,\dots,n$）。由 $p^{(k)}(x_0) = k!\,a_k$ 得 $a_k = \frac{f^{(k)}(x_0)}{k!}$。

**定义 5.5.1（Taylor 多项式）** 设 $f$ 在 $x_0$ 点 $n$ 阶可导，称

$$
P_n(x) = f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+\cdots+\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n
$$
为 $f$ 在 $x_0$ 点的 $n$ 阶 **Taylor 多项式**。

**定理 5.5.1（Taylor 公式）** 设 $f$ 在 $x_0$ 点存在 $1$ 到 $n$ 阶导数，则 $x\to x_0$ 时

$$
f(x) = f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+\cdots+\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n+o\bigl((x-x_0)^n\bigr).
$$

上式称为带 Peano 余项的 Taylor 公式，其中余项 $R_n(x) = f(x)-P_n(x) = o\bigl((x-x_0)^n\bigr)$ 称为 Peano 余项（Peano form of the remainder）。

**证明** 要证 $\lim\limits_{x\to x_0}\frac{R_n(x)}{(x-x_0)^n} = 0$。$f^{(n)}(x_0)$ 存在意味着 $f^{(n-1)}$ 在 $x_0$ 的某邻域内存在，且 $R_n(x_0) = R_n'(x_0) = \cdots = R_n^{(n-1)}(x_0) = 0$。连续使用 $n-1$ 次 L'Hôpital 法则（每次都是 $\frac00$ 型），再用 $f^{(n)}(x_0)$ 的定义：

$$
\lim_{x\to x_0}\frac{R_n(x)}{(x-x_0)^n} = \cdots = \lim_{x\to x_0}\frac{R_n^{(n-1)}(x)}{n!\,(x-x_0)} = \frac1{n!}\lim_{x\to x_0}\Bigl[\frac{f^{(n-1)}(x)-f^{(n-1)}(x_0)}{x-x_0}-f^{(n)}(x_0)\Bigr] = 0,
$$

这里用了 $R_n^{(n-1)}(x) = f^{(n-1)}(x)-f^{(n-1)}(x_0)-f^{(n)}(x_0)(x-x_0)$。 $\square$

Peano 余项只说明误差在 $x\to x_0$ 时是高阶无穷小，适合求极限；要估计误差的大小，需要余项的具体形式。

**定理 5.5.2（带 Lagrange 余项的 Taylor 公式）** 设 $f$ 在包含 $x_0$ 的开区间 $(a,b)$ 内存在 $1$ 到 $n+1$ 阶导数，则对任意 $x\in(a,b)$，

$$
f(x) = \sum_{k=0}^n\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k+\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1},
$$
其中 $\xi = x_0+\theta(x-x_0)$，$0<\theta<1$。

余项 $R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}$ 称为 Lagrange 余项（Lagrange form of the remainder）。$n = 0$ 时就是 Lagrange 中值定理，所以定理 5.5.2 是中值定理的高阶推广。

**证明** 设 $x\ne x_0$。$R_n = f-P_n$ 满足 $R_n(x_0) = R_n'(x_0) = \cdots = R_n^{(n)}(x_0) = 0$，$R_n^{(n+1)} = f^{(n+1)}$；而 $G(t) = (t-x_0)^{n+1}$ 满足 $G(x_0) = \cdots = G^{(n)}(x_0) = 0$，$G^{(n+1)} = (n+1)!$。对 $R_n$ 与 $G$ 反复使用 Cauchy 中值定理：

$$
\frac{R_n(x)}{G(x)} = \frac{R_n(x)-R_n(x_0)}{G(x)-G(x_0)} = \frac{R_n'(\xi_1)}{G'(\xi_1)} = \frac{R_n'(\xi_1)-R_n'(x_0)}{G'(\xi_1)-G'(x_0)} = \frac{R_n''(\xi_2)}{G''(\xi_2)} = \cdots = \frac{R_n^{(n+1)}(\xi)}{G^{(n+1)}(\xi)} = \frac{f^{(n+1)}(\xi)}{(n+1)!},
$$

其中 $\xi_1$ 在 $x_0$ 与 $x$ 之间，$\xi_2$ 在 $x_0$ 与 $\xi_1$ 之间，……，$\xi$ 在 $x_0$ 与 $x$ 之间。 $\square$

两个定理的条件不同：Peano 余项只需要 $f^{(n)}(x_0)$ 存在；Lagrange 余项需要 $n+1$ 阶导数在整个区间内存在，换来的是误差的显式表达式：若 $|f^{(n+1)}|\le M$，则 $|R_n(x)|\le\frac{M}{(n+1)!}|x-x_0|^{n+1}$。

$x_0 = 0$ 时的 Taylor 公式

$$
f(x) = f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+\cdots+\frac{f^{(n)}(0)}{n!}x^n+R_n(x)
$$

称为 Maclaurin 公式（Maclaurin's formula）。由 $(\mathrm{e}^x)^{(n)} = \mathrm{e}^x$、例 4.4.2、例 4.4.3 等，得到五个常用的 Maclaurin 公式（$0<\theta<1$）：

$$
\begin{aligned}
\mathrm{e}^x &= 1+x+\frac{x^2}{2!}+\cdots+\frac{x^n}{n!}+\frac{\mathrm{e}^{\theta x}}{(n+1)!}x^{n+1}, &&x\in\mathbb{R};\\
\sin x &= x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots+(-1)^{k-1}\frac{x^{2k-1}}{(2k-1)!}+\frac{\sin(\theta x+k\pi)}{(2k)!}x^{2k}, &&x\in\mathbb{R};\\
\cos x &= 1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots+(-1)^k\frac{x^{2k}}{(2k)!}+\frac{\cos\bigl(\theta x+\frac{(2k+1)\pi}{2}\bigr)}{(2k+1)!}x^{2k+1}, &&x\in\mathbb{R};\\
(1+x)^\alpha &= 1+\alpha x+\frac{\alpha(\alpha-1)}{2!}x^2+\cdots+\frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}x^n+\frac{\alpha(\alpha-1)\cdots(\alpha-n)}{(n+1)!}(1+\theta x)^{\alpha-n-1}x^{n+1}, &&x>-1;\\
\ln(1+x) &= x-\frac{x^2}{2}+\frac{x^3}{3}-\cdots+(-1)^{n-1}\frac{x^n}{n}+\frac{(-1)^n}{(n+1)(1+\theta x)^{n+1}}x^{n+1}, &&x>-1.
\end{aligned}
$$

把余项换成 $o(x^n)$（$\sin$、$\cos$ 分别为 $o(x^{2k})$、$o(x^{2k+1})$）就是带 Peano 余项的形式。取 $x = 1$，$\mathrm{e} = 1+1+\frac1{2!}+\cdots+\frac1{n!}+\frac{\mathrm{e}^\theta}{(n+1)!}$，误差小于 $\frac{3}{(n+1)!}$，由此可以快速计算**自然常数**。

问题：$x^\alpha$（$\alpha>0$ 不是整数）在 $0$ 点有没有 $n$ 阶 Taylor 公式？只有当 $n<\alpha$ 时才有（此时 Taylor 多项式为 $0$）；$n>\alpha$ 时 $f^{(n)}(0)$ 不存在（$x^\alpha$ 在 $x<0$ 处甚至可能无定义）。Taylor 公式要求函数在该点足够光滑。

![sin x 在 0 点的 Taylor 多项式 P₁, P₃, …, P₁₁：阶数越高，与 sin x 吻合的范围越宽](./plots/taylor-sine.py)

**例 5.5.1** 求 $f(x) = x^3\ln|x|$（$x\ne0$），$f(0) = 0$ 在 $x = 0$ 点的二阶 Taylor 公式。

解：$x\ne0$ 时 $f'(x) = 3x^2\ln|x|+x^2$，$f'(0) = \lim\limits_{x\to0}x^2\ln|x| = 0$；$f''(x) = 6x\ln|x|+5x$，$f''(0) = \lim\limits_{x\to0}\frac{f'(x)}{x} = \lim\limits_{x\to0}(3x\ln|x|+x) = 0$。所以带 Peano 余项的二阶 Taylor 公式为 $f(x) = o(x^2)$。注意 $f'''(0) = \lim\limits_{x\to0}(6\ln|x|+5)$ 不存在，所以没有三阶 Taylor 公式。

**例 5.5.2** 求 $f(x) = x^3+2x+1$ 在 $x = 0$ 与 $x = 1$ 处的 3 阶 Taylor 公式。

解：$f' = 3x^2+2$，$f'' = 6x$，$f''' = 6$，$f^{(4)} = 0$，Lagrange 余项为零。在 $0$ 处 $f(x) = 1+2x+x^3$；在 $1$ 处 $f(1) = 4$，$f'(1) = 5$，$\frac{f''(1)}{2!} = 3$，$\frac{f'''(1)}{3!} = 1$，

$$
f(x) = 4+5(x-1)+3(x-1)^2+(x-1)^3.
$$

一般地，$n$ 次多项式的 $n$ 阶 Taylor 多项式就是它自身，在 $x_0$ 处的 Taylor 公式就是按 $x-x_0$ 的幂重新展开（与 [2.1.9](/2.1.9) 中按 $x-c$ 的幂展开多项式的综合除法一致）。

下面的定理给出求 Taylor 多项式的另一种方法：不必逐阶求导，只要用任何方法得到形如"多项式 $+\,o((x-x_0)^n)$"的展开，它就是 Taylor 公式。

**定理 5.5.3（唯一性）** 设 $f$ 在 $x_0$ 点有 $1$ 到 $n$ 阶导数。若多项式 $a_0+a_1(x-x_0)+\cdots+a_n(x-x_0)^n$ 满足

$$
f(x) = a_0+a_1(x-x_0)+\cdots+a_n(x-x_0)^n+o\bigl((x-x_0)^n\bigr)\qquad(x\to x_0),
$$
则 $a_k = \frac{f^{(k)}(x_0)}{k!}$（$k = 0,1,\dots,n$），即这个多项式就是 $f$ 的 $n$ 阶 Taylor 多项式。

**证明** 由定理 5.5.1，$\sum_{k=0}^n\bigl(a_k-\frac{f^{(k)}(x_0)}{k!}\bigr)(x-x_0)^k = o\bigl((x-x_0)^n\bigr)$。若系数不全为零，设第一个非零系数是 $c_m$（$m\le n$），两边除以 $(x-x_0)^m$ 再令 $x\to x_0$，得 $c_m = 0$，矛盾。 $\square$

**例 5.5.3** 求 $f(x) = \mathrm{e}^{x^2}$ 在 $x = 0$ 处的 $2n$ 阶 Taylor 公式。

解：在 $\mathrm{e}^t$ 的 Maclaurin 公式中令 $t = x^2$：

$$
\mathrm{e}^{x^2} = 1+x^2+\frac{x^4}{2!}+\cdots+\frac{x^{2n}}{n!}+\frac{\mathrm{e}^{\theta x^2}}{(n+1)!}x^{2(n+1)}.
$$

余项是 $o(x^{2n})$，由定理 5.5.3，这就是 $\mathrm{e}^{x^2}$ 的 $2n$ 阶 Taylor 公式；顺便得到 $f^{(2k)}(0) = \frac{(2k)!}{k!}$，奇数阶导数为 $0$。

**例 5.5.4** 求 $f(x) = \ln x$ 在 $x = 3$ 处带 Lagrange 余项的 $n$ 阶 Taylor 公式。

解：$\ln x = \ln3+\ln\bigl(1+\frac{x-3}{3}\bigr)$，在 $\ln(1+t)$ 的 Maclaurin 公式中令 $t = \frac{x-3}3$（$x>0$）：

$$
\ln x = \ln3+\sum_{k=1}^n\frac{(-1)^{k-1}}{k}\Bigl(\frac{x-3}{3}\Bigr)^k+\frac{(-1)^n}{(n+1)\bigl(1+\theta\frac{x-3}{3}\bigr)^{n+1}}\Bigl(\frac{x-3}{3}\Bigr)^{n+1},\qquad0<\theta<1.
$$

**例 5.5.5** 求 $\sqrt[3]{\cos x}$ 在 $0$ 点带 Peano 余项的三阶 Taylor 公式。

解：$\cos x = 1+u$，$u = -\frac{x^2}{2}+o(x^3)$，而 $(1+u)^{1/3} = 1+\frac13u-\frac19u^2+o(u^2)$。$u^2 = o(x^3)$，所以

$$
\sqrt[3]{\cos x} = 1+\frac13\Bigl(-\frac{x^2}{2}+o(x^3)\Bigr)+o(x^3) = 1-\frac{x^2}{6}+o(x^3).
$$

（直接逐阶求导也能得到 $f(0) = 1$、$f'(0) = 0$、$f''(0) = -\frac13$、$f'''(0) = 0$，但计算量大得多。）

### 5.5.2. Taylor 公式的应用

误差估计。用 $P_n(x)$ 近似 $f(x)$ 的误差就是 Lagrange 余项 $|R_n(x)| = \frac{|f^{(n+1)}(\xi)|}{(n+1)!}|x-x_0|^{n+1}$。

**例 5.5.6** 用 Taylor 公式求 $\sin10^\circ$ 的近似值。

解：$10^\circ = \frac{\pi}{18}\approx0.174533$。用一阶 Taylor 多项式 $\sin10^\circ\approx0.174533$，误差 $|R_1| = \bigl\lvert\frac{\sin(\xi+\pi)}{2!}\bigr\rvert(0.174533)^2<0.02$；用三阶 Taylor 多项式 $\sin10^\circ\approx0.174533-\frac16(0.174533)^3\approx0.173647$，误差 $|R_3| = \bigl\lvert\frac{\sin(\xi+2\pi)}{4!}\bigr\rvert(0.174533)^4\le\frac{(0.174533)^5}{4!}<10^{-5}$（这里 $0<\xi<0.174533$，$|\sin\xi|\le\xi$；由于 $P_3 = P_4$，误差实际上不超过 $\frac{(0.174533)^5}{5!}\approx1.4\times10^{-6}$）。若要求误差不超过 $10^{-6}$，求使 $\frac{(0.174533)^{n+1}}{(n+1)!}<10^{-6}$ 的最小 $n$，得 $n = 5$（$n = 4$ 时约为 $1.4\times10^{-6}$，$n = 5$ 时约为 $3.9\times10^{-8}$）。

求极限。把分子分母展开到同一阶，就把不定式化为多项式之比；它是等价无穷小替换的精确化，可以处理加减运算中的抵消。

**例 5.5.7** 求 $\lim\limits_{x\to0}\frac{\sqrt[3]{\cos x}-1-x(\mathrm{e}^x-1)}{(2^x-1)\tan x}$。

解：分母 $\sim x\ln2\cdot x = x^2\ln2$。由例 5.5.5 与 $\mathrm{e}^x-1 = x+o(x)$，分子 $= -\frac{x^2}6-x^2+o(x^2) = -\frac76x^2+o(x^2)$，所以原极限为 $-\frac{7}{6\ln2}$。

**例 5.5.8** 求 $\lim\limits_{x\to0^+}\frac{\mathrm{e}^{x^2}-\cos(2\sqrt x)-2x}{x^2}$。

解：$\mathrm{e}^{x^2} = 1+x^2+o(x^2)$，$\cos(2\sqrt x) = 1-\frac{(2\sqrt x)^2}{2}+\frac{(2\sqrt x)^4}{4!}+o(x^2) = 1-2x+\frac23x^2+o(x^2)$，所以分子 $= \frac13x^2+o(x^2)$，原极限为 $\frac13$。

证明有界性与不等式。

**例 5.5.9** 设 $f$ 在 $(-\infty,+\infty)$ 上有三阶导数，$f$ 与 $f'''$ 有界，证明 $f'$ 与 $f''$ 也有界。

**证明** 设 $|f|\le M$，$|f'''|\le N$。对任意 $x$，把 $f(x\pm1)$ 在 $x$ 点展开成带 Lagrange 余项的二阶 Taylor 公式：

$$
f(x+1) = f(x)+f'(x)+\frac{f''(x)}{2}+\frac{f'''(\xi)}{6},\qquad f(x-1) = f(x)-f'(x)+\frac{f''(x)}{2}-\frac{f'''(\eta)}{6}.
$$

两式相减与相加，得

$$
f'(x) = \frac12\Bigl[f(x+1)-f(x-1)-\frac{f'''(\xi)+f'''(\eta)}{6}\Bigr],\qquad f''(x) = f(x+1)+f(x-1)-2f(x)-\frac{f'''(\xi)-f'''(\eta)}{6},
$$

所以 $|f'(x)|\le M+\frac N6$，$|f''(x)|\le4M+\frac N3$。 $\square$

## 小结

| 定理 | 条件 | 结论 |
|---|---|---|
| Fermat 定理 | $x_0$ 是极值点，$f'(x_0)$ 存在 | $f'(x_0) = 0$ |
| Rolle 定理 | $f\in C[a,b]$，$(a,b)$ 内可导，$f(a) = f(b)$ | $\exists\,\xi$，$f'(\xi) = 0$ |
| Lagrange 中值定理 | $f\in C[a,b]$，$(a,b)$ 内可导 | $f(b)-f(a) = f'(\xi)(b-a)$ |
| Cauchy 中值定理 | 另有 $g$，$g'\ne0$ | $\frac{f(b)-f(a)}{g(b)-g(a)} = \frac{f'(\xi)}{g'(\xi)}$ |
| Darboux 定理 | $f$ 在 $[a,b]$ 上可导 | $f'$ 取遍 $f'_+(a)$ 与 $f'_-(b)$ 之间的值 |
| L'Hôpital 法则 | $\frac00$ 或 $\frac{*}{\infty}$ 型，$g'\ne0$，$\lim\frac{f'}{g'}$ 存在或为无穷 | $\lim\frac fg = \lim\frac{f'}{g'}$ |
| 极值判别 | $f'$ 在 $x_0$ 两侧变号（$f$ 在 $x_0$ 连续）；或 $f'(x_0) = 0$，$f''(x_0)\ne0$ | 极值；$f''(x_0)>0$ 为极小 |
| 唯一驻点定理 | 区间内部唯一驻点且为极小（大）值点 | 最小（大）值 |
| 凸性判别 | $f'$ 单调非减，或 $f''\ge0$ | $f$ 凸；Jensen 不等式 |
| 斜渐近线 | $a = \lim\frac{f(x)}{x}$，$b = \lim(f(x)-ax)$ | $y = ax+b$ |
| Taylor 公式 | $f^{(n)}(x_0)$ 存在 / $f^{(n+1)}$ 在区间内存在 | 余项 $o((x-x_0)^n)$ / $\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}$ |

| 常用 Maclaurin 展开（Peano 余项） | |
|---|---|
| $\mathrm{e}^x$ | $1+x+\frac{x^2}{2!}+\cdots+\frac{x^n}{n!}+o(x^n)$ |
| $\sin x$ | $x-\frac{x^3}{3!}+\cdots+(-1)^{k-1}\frac{x^{2k-1}}{(2k-1)!}+o(x^{2k})$ |
| $\cos x$ | $1-\frac{x^2}{2!}+\cdots+(-1)^k\frac{x^{2k}}{(2k)!}+o(x^{2k+1})$ |
| $(1+x)^\alpha$ | $1+\alpha x+\frac{\alpha(\alpha-1)}{2!}x^2+\cdots+\binom{\alpha}{n}x^n+o(x^n)$ |
| $\ln(1+x)$ | $x-\frac{x^2}2+\cdots+(-1)^{n-1}\frac{x^n}{n}+o(x^n)$ |

其中 $\binom\alpha n = \frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}$ 是广义二项式系数。
