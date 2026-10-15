---
title: 原函数与不定积分
---

微分学的基本问题是：已知函数，求它的导数。本章讨论逆问题：已知导数 $f$，求函数 $F$ 使 $F' = f$。这就是求原函数，或者说求不定积分，它是求导的逆运算。由于求导法则可以机械地使用，任何初等函数的导数都能算出；而求原函数没有通用的算法，只有几种基本方法——换元积分法、分部积分法，以及对有理函数、三角函数有理式和几类无理函数的系统处理——每种方法都是某条求导法则的逆用。被积函数形式上的细微变化，可能使积分从容易变为困难，甚至原函数不能用初等函数表示。本章依赖 [2.2.4](/2.2.4) 的求导公式与 [2.2.5](/2.2.5) 的 **Lagrange 中值定理**；下一章（[2.2.7](/2.2.7)）的**微积分基本定理**把定积分的计算归结为求原函数，常微分方程（[2.2.15](/2.2.15)）的求解也大量用到本章的积分技巧。

## 6.1. 不定积分的概念与性质

### 6.1.1. 原函数

**定义 6.1.1（原函数）** 设 $f$ 在区间 $I$ 上有定义。若存在函数 $F$，使得在 $I$ 上 $F'(x) = f(x)$，则称 $F$ 是 $f$ 在区间 $I$ 上的一个**原函数**。

例如在 $(-\infty,+\infty)$ 上，$\frac12x^2$ 是 $x$ 的一个原函数，$-\cos x$ 是 $\sin x$ 的一个原函数。原函数若存在就不唯一：$F$ 是原函数，$F+C$ 也是。反过来，原函数之间只差一个常数：

**定理 6.1.1** 设 $F$ 与 $G$ 都是 $f$ 在区间 $I$ 上的原函数，则 $G(x) = F(x)+C$，$C$ 为常数。

**证明** $(G-F)' = f-f = 0$，由推论 5.1.1，$G-F$ 在 $I$ 上是常数。 $\square$

"区间"这一条件不能去掉：在 $(-\infty,0)\cup(0,+\infty)$ 上，$\ln|x|$ 与 $\ln|x|+\operatorname{sgn}x$ 都是 $\frac1x$ 的原函数，但它们的差不是常数。

### 6.1.2. 不定积分

**定义 6.1.2（不定积分）** $f$ 在区间 $I$ 上原函数的全体，即所有满足 $\mathrm{d}F(x) = f(x)\,\mathrm{d}x$ 的函数 $F$ 的全体，称为 $f$ 在 $I$ 上的**不定积分**，记作 $\int f(x)\,\mathrm{d}x$。其中 $f$ 称为被积函数，$f(x)\,\mathrm{d}x$ 称为被积表达式。

由定理 6.1.1，若 $F$ 是 $f$ 在 $I$ 上的一个原函数，则

$$
\int f(x)\,\mathrm{d}x = F(x)+C,
$$

$C$ 为任意常数（积分常数）。不定积分是"反微分"运算：从微分 $f(x)\,\mathrm{d}x = \mathrm{d}F(x)$ 求出所有的 $F$。两种运算互逆（相差一个常数）：

$$
\int\mathrm{d}F(x) = F(x)+C,\qquad\mathrm{d}\Bigl(\int f(x)\,\mathrm{d}x\Bigr) = f(x)\,\mathrm{d}x,\qquad\Bigl(\int f(x)\,\mathrm{d}x\Bigr)' = f(x).
$$

几何上，原函数 $y = F(x)$ 的图形称为 $f$ 的一条积分曲线。不定积分是一族积分曲线 $y = F(x)+C$，它们由其中一条沿 $y$ 轴平移得到；在同一横坐标 $x_0$ 处，各条曲线的切线互相平行，斜率都是 $f(x_0)$。指定曲线经过的一点（初值条件）就确定了常数 $C$——这是最简单的微分方程 $y' = f(x)$ 的初值问题。

![f(x) = x² − 1 的积分曲线族 y = x³/3 − x + C 与斜率场：每一点的线段斜率只依赖于 x，在 x = x₀ 处各条曲线的切线平行](./plots/integral-curves.py)

### 6.1.3. 基本积分公式

把 [2.2.4](/2.2.4) 中的导数表反过来读，就得到基本积分公式：

| 积分 | 结果 | 积分 | 结果 |
|---|---|---|---|
| $\int0\,\mathrm{d}x$ | $C$ | $\int\mathrm{d}x$ | $x+C$ |
| $\int x^p\,\mathrm{d}x$（$p\ne-1$） | $\frac{x^{p+1}}{p+1}+C$ | $\int\frac1x\,\mathrm{d}x$ | $\ln\lvert x\rvert+C$ |
| $\int a^x\,\mathrm{d}x$（$a>0$，$a\ne1$） | $\frac{a^x}{\ln a}+C$ | $\int\mathrm{e}^x\,\mathrm{d}x$ | $\mathrm{e}^x+C$ |
| $\int\sin x\,\mathrm{d}x$ | $-\cos x+C$ | $\int\cos x\,\mathrm{d}x$ | $\sin x+C$ |
| $\int\sec^2x\,\mathrm{d}x$ | $\tan x+C$ | $\int\csc^2x\,\mathrm{d}x$ | $-\cot x+C$ |
| $\int\sec x\tan x\,\mathrm{d}x$ | $\sec x+C$ | $\int\csc x\cot x\,\mathrm{d}x$ | $-\csc x+C$ |
| $\int\frac{\mathrm{d}x}{\sqrt{1-x^2}}$ | $\arcsin x+C = -\arccos x+C_1$ | $\int\frac{\mathrm{d}x}{1+x^2}$ | $\arctan x+C = -\operatorname{arccot}x+C_1$ |

最后一行说明：同一个不定积分的结果可以有不同的形式，它们只差一个常数（$\arcsin x+\arccos x = \frac\pi2$）。验证积分结果是否正确，只需对结果求导。

### 6.1.4. 原函数的存在条件

**定理 6.1.2** 若 $f$ 在区间 $I$ 上连续，则 $f$ 在 $I$ 上存在原函数。

这个定理的证明要用定积分（变上限积分），见 [2.2.7](/2.2.7)。所以**初等函数**在其定义区间上都有原函数。

连续是原函数存在的充分条件，而不是必要条件。设 $F(x) = x^2\sin\frac1x$（$x\ne0$），$F(0) = 0$，由例 4.1.6，

$$
F'(x) = f(x) = \begin{cases}2x\sin\frac1x-\cos\frac1x, & x\ne0,\\ 0, & x = 0,\end{cases}
$$

$f$ 在 $(-\infty,+\infty)$ 上有原函数 $F$，但 $f$ 在 $0$ 点不连续。另一方面，由 **Darboux 定理**，导函数没有**第一类间断点**，所以在区间内有**跳跃间断点**或**可去间断点**的函数没有原函数，例如**符号函数** $\operatorname{sgn}x$ 在 $(-\infty,+\infty)$ 上没有原函数（在不含 $0$ 的区间上当然有）。

还要注意，"有原函数"与"原函数是初等函数"是两回事。$\mathrm{e}^{-x^2}$、$\frac{\sin x}{x}$、$\frac1{\ln x}$、$\sqrt{1-k^2\sin^2x}$（$0<k<1$）都是连续函数，有原函数，但可以证明（Liouville）它们的原函数都不是初等函数，即"积不出来"。这些函数在概率论（正态分布）、信号处理与椭圆积分中非常重要，只能用定积分、级数或数值方法研究。

### 6.1.5. 不定积分的线性性质

**定理 6.1.3** 若 $f$ 与 $g$ 在区间 $I$ 上都有原函数，$k, l$ 为常数，则

$$
\int\bigl(kf(x)+lg(x)\bigr)\,\mathrm{d}x = k\int f(x)\,\mathrm{d}x+l\int g(x)\,\mathrm{d}x,
$$
其中 $k, l$ 不同时为零（等式两边都含任意常数，理解为两个函数族相等）。

**证明** 对右端求导，由求导的线性性得 $kf+lg$。 $\square$

利用线性性把被积函数拆成基本积分公式中的函数之和，是最直接的积分方法。

**例 6.1.1** 求不定积分：(1) $\int(x^2+2^x)\,\mathrm{d}x$；(2) $\int\frac{x^4}{1+x^2}\,\mathrm{d}x$；(3) $\int\frac{\mathrm{d}x}{a^2-x^2}$（$a>0$）；(4) $\int\frac{\cos2x}{\sin x-\cos x}\,\mathrm{d}x$；(5) $\int f(x)\,\mathrm{d}x$，其中 $f(x) = 2x$（$x\le1$），$f(x) = 2x^2$（$x>1$）。

解：(1) $\frac13x^3+\frac{2^x}{\ln2}+C$。

(2) 
$$
\int\frac{x^4-1+1}{1+x^2}\,\mathrm{d}x = \int\Bigl(x^2-1+\frac1{1+x^2}\Bigr)\,\mathrm{d}x = \frac13x^3-x+\arctan x+C.
$$

(3) 
$$
\int\frac1{2a}\Bigl(\frac1{a+x}+\frac1{a-x}\Bigr)\,\mathrm{d}x = \frac1{2a}\bigl(\ln\lvert a+x\rvert-\ln\lvert a-x\rvert\bigr)+C = \frac1{2a}\ln\Bigl\lvert\frac{a+x}{a-x}\Bigr\rvert+C.
$$

(4) $\cos2x = (\cos x-\sin x)(\cos x+\sin x)$，所以原式 $= -\int(\sin x+\cos x)\,\mathrm{d}x = \cos x-\sin x+C$。

(5) 分段求原函数：$x<1$ 时为 $x^2+C$，$x>1$ 时为 $\frac23x^3+C_1$。原函数可导，从而在 $x = 1$ 连续，所以 $1+C = \frac23+C_1$，$C_1 = C+\frac13$。于是

$$
\int f(x)\,\mathrm{d}x = \begin{cases}x^2, & x\le1,\\ \frac23x^3+\frac13, & x>1\end{cases}\ +\ C.
$$

（还应验证这个函数在 $x = 1$ 处可导且导数为 $f(1) = 2$：左、右导数都是 $2$。）

## 6.2. 换元积分法

### 6.2.1. 第一换元法

链式法则 $\bigl(F(\varphi(x))\bigr)' = F'(\varphi(x))\varphi'(x)$ 反过来读，就是第一换元法。

**定理 6.2.1（第一换元法）** 若 $\int f(u)\,\mathrm{d}u = F(u)+C$，$\varphi$ 可导，则

$$
\int f(\varphi(x))\varphi'(x)\,\mathrm{d}x = \int f(\varphi(x))\,\mathrm{d}\varphi(x) \overset{u = \varphi(x)}{=} \int f(u)\,\mathrm{d}u = F(\varphi(x))+C.
$$

**证明** 由链式法则，$\bigl(F(\varphi(x))\bigr)' = f(\varphi(x))\varphi'(x)$。 $\square$

由**一阶微分形式不变性**，$\varphi'(x)\,\mathrm{d}x = \mathrm{d}\varphi(x)$，所以第一换元法也叫凑微分法：把被积表达式凑成 $f(\varphi(x))\,\mathrm{d}\varphi(x)$ 的形式。给定 $\int g(x)\,\mathrm{d}x$，关键不在于做替换，而在于把 $g$ 分解为 $f(\varphi(x))\varphi'(x)$。有两种观察方法：

1. 被积函数 $g = g_1g_2$ 中有一个较复杂的复合函数因子 $f(\varphi(x))$，试着令 $u = \varphi(x)$，看剩下的因子是否恰为 $\varphi'(x)$（至多差常数倍）。例如 $\frac{\cos(\ln x)}{x}$、$\cos^3x\sin x$、$\frac{\sin(\arctan x)}{1+x^2}$、$a^{\cos x}\sin x$。
2. 被积函数中有一个因子 $g_2$ 是某个 $\varphi$ 的导数，再看其余部分能否写成 $\varphi$ 的函数。例如

$$
\frac{\cos x}{\sin x} = \frac{(\sin x)'}{\sin x},\qquad\frac1{\sin x} = \frac{\sin x}{1-\cos^2x} = -\frac{(\cos x)'}{1-\cos^2x},\qquad\frac1{x\ln x} = \frac{(\ln x)'}{\ln x},\qquad\frac1{x\ln x\ln\ln x} = \frac{(\ln\ln x)'}{\ln\ln x}.
$$

常用的凑微分：$\mathrm{d}x = \frac1a\mathrm{d}(ax+b)$，$x\,\mathrm{d}x = \frac12\mathrm{d}(x^2)$，$\frac{\mathrm{d}x}{x} = \mathrm{d}\ln x$，$\frac{\mathrm{d}x}{\sqrt x} = 2\,\mathrm{d}\sqrt x$，$\cos x\,\mathrm{d}x = \mathrm{d}\sin x$，$\sec^2x\,\mathrm{d}x = \mathrm{d}\tan x$，$\frac{\mathrm{d}x}{1+x^2} = \mathrm{d}\arctan x$，$\mathrm{e}^x\,\mathrm{d}x = \mathrm{d}\,\mathrm{e}^x$。

**例 6.2.1** 求不定积分：

(1) $\int x\sin x^2\,\mathrm{d}x\overset{u = x^2}{=}\frac12\int\sin u\,\mathrm{d}u = -\frac12\cos x^2+C$。

(2) $\int\frac{\cos(\ln x)}{x}\,\mathrm{d}x = \int\cos(\ln x)\,\mathrm{d}\ln x = \sin(\ln x)+C$。

(3) $\int\tan x\,\mathrm{d}x = -\int\frac{\mathrm{d}\cos x}{\cos x} = -\ln\lvert\cos x\rvert+C$；同理 $\int\cot x\,\mathrm{d}x = \ln\lvert\sin x\rvert+C$。

(4) $\int\frac{\mathrm{d}x}{a^2+x^2} = \frac1a\int\frac{\mathrm{d}(x/a)}{1+(x/a)^2} = \frac1a\arctan\frac xa+C$。

(5) $\int\frac{\mathrm{d}x}{\sqrt{a^2-x^2}} = \int\frac{\mathrm{d}(x/a)}{\sqrt{1-(x/a)^2}} = \arcsin\frac xa+C$（$a>0$）。

(6) 
$$
\int\sec x\,\mathrm{d}x = \int\frac{\cos x\,\mathrm{d}x}{\cos^2x} = \int\frac{\mathrm{d}\sin x}{1-\sin^2x} = \frac12\ln\Bigl\lvert\frac{1+\sin x}{1-\sin x}\Bigr\rvert+C = \ln\Bigl\lvert\frac{1+\sin x}{\cos x}\Bigr\rvert+C = \ln\lvert\sec x+\tan x\rvert+C,
$$

其中第三步用了例 6.1.1 (3)，第四步把分子分母同乘 $1+\sin x$。同理 $\int\csc x\,\mathrm{d}x = \ln\lvert\csc x-\cot x\rvert+C$。

(7) 在定义域 $(0,1)$ 上，$\int\frac{\mathrm{d}x}{\sqrt{x(1-x)}} = 2\int\frac{\mathrm{d}\sqrt x}{\sqrt{1-(\sqrt x)^2}} = 2\arcsin\sqrt x+C$。

(8) $\int\frac{(x-1)\,\mathrm{d}x}{\sqrt{2-2x+x^2}}\overset{u = x-1}{=}\int\frac{u\,\mathrm{d}u}{\sqrt{1+u^2}} = \frac12\int\frac{\mathrm{d}(1+u^2)}{\sqrt{1+u^2}} = \sqrt{2-2x+x^2}+C$。

(9) 令 $u = x^2$，再把分子拆成分母的导数与常数：

$$
\int\frac{x^3\,\mathrm{d}x}{x^4-2x^2+2} = \frac12\int\frac{u\,\mathrm{d}u}{u^2-2u+2} = \frac14\int\frac{\mathrm{d}(u^2-2u+2)}{u^2-2u+2}+\frac12\int\frac{\mathrm{d}(u-1)}{(u-1)^2+1} = \frac14\ln(x^4-2x^2+2)+\frac12\arctan(x^2-1)+C.
$$

**例 6.2.2** 设 $f'(\cos x+2) = \sin^2x+\tan^2x$，求 $f(x)$。

解：令 $u = \cos x+2$，则 $\cos x = u-2$，$\sin^2x+\tan^2x = 1-\cos^2x+\frac1{\cos^2x}-1 = -(u-2)^2+\frac1{(u-2)^2}$。所以 $f'(x) = -(x-2)^2+\frac{1}{(x-2)^2}$，

$$
f(x) = -\frac13(x-2)^3-\frac1{x-2}+C.
$$

### 6.2.2. 第二换元法

第一换元法把 $f(\varphi(x))\varphi'(x)$ 化简为 $f(u)$。有时需要反方向的操作：被积函数 $f(x)$ 本身不好积，代入 $x = \varphi(t)$ 后 $f(\varphi(t))\varphi'(t)$ 反而容易积，最典型的是去掉根号。

**定理 6.2.2（第二换元法）** 设 $f$ 连续，$x = \varphi(t)$ 有连续导数且 $\varphi'(t)\ne0$（从而有反函数 $t = \varphi^{-1}(x)$）。若

$$
\int f(\varphi(t))\varphi'(t)\,\mathrm{d}t = G(t)+C,
$$
则 $\int f(x)\,\mathrm{d}x = G\bigl(\varphi^{-1}(x)\bigr)+C$。

**证明** 由链式法则与反函数求导法则，

$$
\frac{\mathrm{d}}{\mathrm{d}x}G\bigl(\varphi^{-1}(x)\bigr) = G'(t)\frac{\mathrm{d}t}{\mathrm{d}x} = f(\varphi(t))\varphi'(t)\cdot\frac1{\varphi'(t)} = f(\varphi(t)) = f(x). \qquad\square
$$

与第一换元法相比，两者形式相反：

$$
\int f(\varphi(x))\varphi'(x)\,\mathrm{d}x\overset{u = \varphi(x)}{=}\int f(u)\,\mathrm{d}u,\qquad\int f(x)\,\mathrm{d}x\overset{x = \varphi(t)}{=}\int f(\varphi(t))\varphi'(t)\,\mathrm{d}t.
$$

第二换元法的替换必须可逆，因为最后要用 $t = \varphi^{-1}(x)$ 回代。被积函数含根号时常用的代换：

| 被积函数含有 | 代换 | 范围 |
|---|---|---|
| $\sqrt{x+1}$ 等 $\sqrt[n]{ax+b}$ | $ax+b = t^n$ | $t\ge0$（$n$ 为偶数） |
| $\sqrt{a^2-x^2}$ | $x = a\sin t$ | $t\in\bigl(-\frac\pi2,\frac\pi2\bigr)$ |
| $\sqrt{a^2+x^2}$ | $x = a\tan t$ | $t\in\bigl(-\frac\pi2,\frac\pi2\bigr)$ |
| $\sqrt{x^2-a^2}$ | $x = a\sec t$ | $x>a$ 时 $t\in\bigl(0,\frac\pi2\bigr)$ |

三角代换后，回代时可以画一个直角三角形读出 $\sin t$、$\cos t$、$\tan t$ 与 $x$ 的关系。

**例 6.2.3** 求不定积分：(1) $\int\frac{\mathrm{d}x}{1+\sqrt{x+1}}$；(2) $\int\sqrt{a^2-x^2}\,\mathrm{d}x$；(3) $\int\frac{\mathrm{d}x}{\sqrt{x^2-a^2}}$；(4) $\int\frac{\mathrm{d}x}{\sqrt{x^2+a^2}}$；(5) $\int\frac{\mathrm{d}x}{x^2\sqrt{1+x^2}}$。（$a>0$）

解：(1) 令 $x+1 = t^2$，$t\ge0$，$\mathrm{d}x = 2t\,\mathrm{d}t$：

$$
\int\frac{2t\,\mathrm{d}t}{1+t} = 2\int\Bigl(1-\frac1{1+t}\Bigr)\mathrm{d}t = 2t-2\ln(1+t)+C = 2\sqrt{x+1}-2\ln\bigl(1+\sqrt{x+1}\bigr)+C.
$$

(2) 令 $x = a\sin t$，$t\in\bigl[-\frac\pi2,\frac\pi2\bigr]$，则 $\sqrt{a^2-x^2} = a\cos t$，$\mathrm{d}x = a\cos t\,\mathrm{d}t$：

$$
\int a^2\cos^2t\,\mathrm{d}t = \frac{a^2}2\int(1+\cos2t)\,\mathrm{d}t = \frac{a^2}2(t+\sin t\cos t)+C = \frac12\Bigl(a^2\arcsin\frac xa+x\sqrt{a^2-x^2}\Bigr)+C,
$$

回代时用了 $\sin t = \frac xa$，$\cos t = \frac1a\sqrt{a^2-x^2}$。

(3) 当 $x>a$ 时，令 $x = a\sec t$，$t\in\bigl(0,\frac\pi2\bigr)$，$\sqrt{x^2-a^2} = a\tan t$，$\mathrm{d}x = a\sec t\tan t\,\mathrm{d}t$：

$$
\int\sec t\,\mathrm{d}t = \ln\lvert\sec t+\tan t\rvert+C = \ln\Bigl\lvert\frac xa+\frac{\sqrt{x^2-a^2}}a\Bigr\rvert+C = \ln\bigl\lvert x+\sqrt{x^2-a^2}\bigr\rvert+C_1,
$$

其中 $C_1 = C-\ln a$。当 $x<-a$ 时，令 $x = -u$ 化为 $u>a$ 的情形，结果的形式相同（也可以取 $t\in\bigl(\pi,\frac{3\pi}2\bigr)$）。

(4) 令 $x = a\tan t$，$t\in\bigl(-\frac\pi2,\frac\pi2\bigr)$，$\sqrt{x^2+a^2} = a\sec t$：

$$
\int\frac{a\sec^2t\,\mathrm{d}t}{a\sec t} = \ln\lvert\sec t+\tan t\rvert+C = \ln\bigl(x+\sqrt{x^2+a^2}\bigr)+C_1.
$$

(5) 方法一（第二换元法）：令 $x = \tan t$，

$$
\int\frac{\sec^2t\,\mathrm{d}t}{\tan^2t\sec t} = \int\frac{\cos t}{\sin^2t}\,\mathrm{d}t = -\frac1{\sin t}+C = -\frac{\sqrt{1+x^2}}{x}+C.
$$

方法二（倒代换）：对 $x>0$，令 $x = \frac1u$（$u>0$），$\mathrm{d}x = -\frac{\mathrm{d}u}{u^2}$，$x^2\sqrt{1+x^2} = \frac{\sqrt{u^2+1}}{u^3}$，于是原式 $= -\int\frac{u\,\mathrm{d}u}{\sqrt{u^2+1}} = -\sqrt{1+u^2}+C = -\frac{\sqrt{x^2+1}}{x}+C$；$x<0$ 时同理。分母中 $x$ 的次数较高时，倒代换往往有效。

## 6.3. 分部积分法

乘积的求导法则 $(uv)' = u'v+uv'$ 两边积分，就得到分部积分法。

**定理 6.3.1（分部积分法）** 设 $u, v$ 可导，且 $u'v$ 有原函数，则

$$
\int u\,\mathrm{d}v = uv-\int v\,\mathrm{d}u,\qquad\text{即}\qquad\int uv'\,\mathrm{d}x = uv-\int u'v\,\mathrm{d}x.
$$

**证明** $\mathrm{d}(uv) = v\,\mathrm{d}u+u\,\mathrm{d}v$，所以 $u\,\mathrm{d}v = \mathrm{d}(uv)-v\,\mathrm{d}u$，两边积分即得。 $\square$

分部积分把 $\int u\,\mathrm{d}v$ 转化为 $\int v\,\mathrm{d}u$，只要后者容易求出，前者也随之得到。

**例 6.3.1** $\int x\sin3x\,\mathrm{d}x = \int x\,\mathrm{d}\Bigl(-\frac13\cos3x\Bigr) = -\frac13x\cos3x+\frac13\int\cos3x\,\mathrm{d}x = -\frac19(3x\cos3x-\sin3x)+C$。

用分部积分计算 $\int f_1(x)f_2(x)\,\mathrm{d}x$ 时，怎样选择 $u$ 与 $v'$？原则是：$v'$ 要容易积分，$u$ 求导后要变简单。

1. 乘积中有 $\mathrm{e}^{ax}$、$\sin ax$（$\cos ax$）、$x^m$ 之一时，常选为 $v'$，优先顺序为 $\mathrm{e}^{ax}$，$\sin ax$（$\cos ax$），$x^m$；
2. 乘积中有 $\arcsin x$、$\arccos x$、$\arctan x$、$\operatorname{arccot}x$、$\ln x$ 之一时，常选为 $u$，其余因子作为 $v'$（只有一个因子时取 $v' = 1$）。

**例 6.3.2** 求不定积分：

(1) $\int x^2\ln x\,\mathrm{d}x = \int\ln x\,\mathrm{d}\frac{x^3}3 = \frac{x^3}3\ln x-\int\frac{x^3}3\cdot\frac1x\,\mathrm{d}x = \frac13x^3\ln x-\frac19x^3+C$。

(2) 两次分部积分，每次都把多项式的次数降低一次：

$$
\int x^2\mathrm{e}^{2x}\,\mathrm{d}x = \frac12x^2\mathrm{e}^{2x}-\int x\mathrm{e}^{2x}\,\mathrm{d}x = \frac12x^2\mathrm{e}^{2x}-\frac12x\mathrm{e}^{2x}+\frac12\int\mathrm{e}^{2x}\,\mathrm{d}x = \Bigl(\frac12x^2-\frac12x+\frac14\Bigr)\mathrm{e}^{2x}+C.
$$

(3) $\int\arctan x\,\mathrm{d}x = x\arctan x-\int\frac{x\,\mathrm{d}x}{1+x^2} = x\arctan x-\frac12\ln(1+x^2)+C$；同理 $\int\ln x\,\mathrm{d}x = x\ln x-x+C$。

(4) 
$$
\int\frac{\ln x}{(1+x)^2}\,\mathrm{d}x = -\int\ln x\,\mathrm{d}\frac1{1+x} = -\frac{\ln x}{1+x}+\int\Bigl(\frac1x-\frac1{1+x}\Bigr)\mathrm{d}x = -\frac{\ln x}{1+x}+\ln\frac{x}{1+x}+C = \frac{x\ln x}{1+x}-\ln(1+x)+C.
$$

(5) 循环积分：

$$
\int\sqrt{a^2+x^2}\,\mathrm{d}x = x\sqrt{a^2+x^2}-\int\frac{x^2\,\mathrm{d}x}{\sqrt{a^2+x^2}} = x\sqrt{a^2+x^2}-\int\sqrt{a^2+x^2}\,\mathrm{d}x+a^2\int\frac{\mathrm{d}x}{\sqrt{a^2+x^2}}.
$$

右端又出现了所求的积分，移项并用例 6.2.3 (4)：

$$
\int\sqrt{a^2+x^2}\,\mathrm{d}x = \frac12\Bigl(x\sqrt{a^2+x^2}+a^2\ln\bigl(x+\sqrt{a^2+x^2}\bigr)\Bigr)+C.
$$

同理 $\int\sqrt{x^2-a^2}\,\mathrm{d}x = \frac12\bigl(x\sqrt{x^2-a^2}-a^2\ln\lvert x+\sqrt{x^2-a^2}\rvert\bigr)+C$，$\int\sqrt{a^2-x^2}\,\mathrm{d}x$ 的结果与例 6.2.3 (2) 相同。

(6) 递推公式：令 $I_n = \int\cos^nx\,\mathrm{d}x$，

$$
I_n = \int\cos^{n-1}x\,\mathrm{d}\sin x = \cos^{n-1}x\sin x+(n-1)\int\cos^{n-2}x\sin^2x\,\mathrm{d}x = \cos^{n-1}x\sin x+(n-1)(I_{n-2}-I_n),
$$

所以

$$
I_n = \frac1n\cos^{n-1}x\sin x+\frac{n-1}nI_{n-2},\qquad n\ge2,
$$

由 $I_0 = x+C$、$I_1 = \sin x+C$ 可以逐个算出 $I_n$。$\int\sin^nx\,\mathrm{d}x$ 有类似的递推公式。

(7)、(8) 设 $ab\ne0$。分部积分两次：

$$
\int\mathrm{e}^{ax}\cos bx\,\mathrm{d}x = \frac{\mathrm{e}^{ax}}{a}\cos bx+\frac ba\int\mathrm{e}^{ax}\sin bx\,\mathrm{d}x,\qquad\int\mathrm{e}^{ax}\sin bx\,\mathrm{d}x = \frac{\mathrm{e}^{ax}}{a}\sin bx-\frac ba\int\mathrm{e}^{ax}\cos bx\,\mathrm{d}x,
$$

联立解得

$$
\int\mathrm{e}^{ax}\cos bx\,\mathrm{d}x = \frac{\mathrm{e}^{ax}(a\cos bx+b\sin bx)}{a^2+b^2}+C,\qquad\int\mathrm{e}^{ax}\sin bx\,\mathrm{d}x = \frac{\mathrm{e}^{ax}(a\sin bx-b\cos bx)}{a^2+b^2}+C.
$$

用复数可以一步得到：$\int\mathrm{e}^{(a+\mathrm{i}b)x}\,\mathrm{d}x = \frac{\mathrm{e}^{(a+\mathrm{i}b)x}}{a+\mathrm{i}b}+C$，分别取实部与虚部（**欧拉公式**）。

(9) 先分部积分，再用根式代换：

$$
\int\frac{x\mathrm{e}^x}{\sqrt{\mathrm{e}^x-3}}\,\mathrm{d}x = 2\int x\,\mathrm{d}\sqrt{\mathrm{e}^x-3} = 2x\sqrt{\mathrm{e}^x-3}-2\int\sqrt{\mathrm{e}^x-3}\,\mathrm{d}x.
$$

令 $t = \sqrt{\mathrm{e}^x-3}$，$x = \ln(t^2+3)$，$\mathrm{d}x = \frac{2t\,\mathrm{d}t}{t^2+3}$：

$$
\int\sqrt{\mathrm{e}^x-3}\,\mathrm{d}x = \int\frac{2t^2}{t^2+3}\,\mathrm{d}t = 2t-2\sqrt3\arctan\frac t{\sqrt3}+C,
$$

所以原式 $= 2x\sqrt{\mathrm{e}^x-3}-4\sqrt{\mathrm{e}^x-3}+4\sqrt3\arctan\sqrt{\frac{\mathrm{e}^x-3}{3}}+C$。

(10) 
$$
\int\sec^3x\,\mathrm{d}x = \int\sec x\,\mathrm{d}\tan x = \sec x\tan x-\int\sec x\tan^2x\,\mathrm{d}x = \sec x\tan x-\int\sec^3x\,\mathrm{d}x+\int\sec x\,\mathrm{d}x,
$$

所以 $\int\sec^3x\,\mathrm{d}x = \frac12\bigl(\sec x\tan x+\ln\lvert\sec x+\tan x\rvert\bigr)+C$。

**例 6.3.3** 令 $I_k = \int\frac{\mathrm{d}x}{(x^2+a^2)^k}$（$a>0$，$k\ge1$），求递推公式。

解：取 $u = \frac1{(x^2+a^2)^k}$，$v = x$：

$$
I_k = \frac{x}{(x^2+a^2)^k}+2k\int\frac{x^2\,\mathrm{d}x}{(x^2+a^2)^{k+1}} = \frac{x}{(x^2+a^2)^k}+2k\int\frac{(x^2+a^2)-a^2}{(x^2+a^2)^{k+1}}\,\mathrm{d}x = \frac{x}{(x^2+a^2)^k}+2kI_k-2ka^2I_{k+1}.
$$

所以

$$
I_{k+1} = \frac{2k-1}{2ka^2}I_k+\frac{x}{2ka^2(x^2+a^2)^k},\qquad I_1 = \frac1a\arctan\frac xa+C.
$$

这个递推公式在 6.4 节有理函数的积分中要用到。

先换元再分部积分也很常见：

**例 6.3.4（1）** $\int\frac{\ln^2x\cos(\ln x)}{x}\,\mathrm{d}x\overset{u = \ln x}{=}\int u^2\cos u\,\mathrm{d}u = u^2\sin u+2u\cos u-2\sin u+C$，即 $(\ln^2x-2)\sin\ln x+2\ln x\cos\ln x+C$。

(2) $\int\frac{\arctan x\,\mathrm{e}^{\arctan x}}{1+x^2}\,\mathrm{d}x\overset{u = \arctan x}{=}\int u\mathrm{e}^u\,\mathrm{d}u = (u-1)\mathrm{e}^u+C = (\arctan x-1)\mathrm{e}^{\arctan x}+C$。

## 6.4. 有理函数的积分

### 6.4.1. 有理函数的积分

**定义 6.4.1** 形如 $\frac{P_m(x)}{Q_n(x)}$ 的函数称为**有理函数**（有理分式函数），其中 $P_m, Q_n$ 分别是 $m$ 次、$n$ 次实系数多项式。$m<n$ 时称为**真分式**，$m\ge n$ 时称为**假分式**。

由多项式的**带余除法**，$P_m = q\,Q_n+r$，$\deg r<n$，所以假分式总等于一个多项式与一个真分式之和：$\frac{P_m}{Q_n} = q+\frac{r}{Q_n}$。多项式的积分是容易的，问题归结为真分式的积分。

**例 6.4.1** 用 $g(x) = x^2+x+1$ 除 $f(x) = x^4+4x^3+2x^2+4x+1$：商 $q(x) = x^2+3x-2$，余式 $r(x) = 3x+3$，所以 $\frac{f}{g} = x^2+3x-2+\frac{3x+3}{x^2+x+1}$。又如 $\frac{2x^4+1}{x^2+1} = 2x^2-2+\frac{3}{x^2+1}$。

**定义 6.4.2** 下面四类真分式称为**最简分式**（$a\ne0$，$k\ge2$ 为正整数，$q^2-4pr<0$）：

$$
\text{(1)}\ \frac{A}{ax+b};\qquad\text{(2)}\ \frac{A}{(ax+b)^k};\qquad\text{(3)}\ \frac{Bx+D}{px^2+qx+r};\qquad\text{(4)}\ \frac{Bx+D}{(px^2+qx+r)^k}.
$$

条件 $q^2-4pr<0$ 表示 $px^2+qx+r$ 没有实根，即它在实数域上是**不可约多项式**。由代数基本定理，实系数多项式在实数域上可以分解为一次因式与不可约二次因式的乘积（[2.1.9](/2.1.9)），由此可以证明：

**定理 6.4.1（部分分式分解）** 真分式 $\frac{P_m(x)}{Q_n(x)}$ 可以唯一地分解成最简分式之和。把 $Q_n$ 分解为一次因式与不可约二次因式的方幂之积，分解规则为：

1. $Q_n$ 的一次单因式 $ax+b$ 对应一项 $\frac{A}{ax+b}$；
2. $Q_n$ 的 $k$ 重因式 $(ax+b)^k$ 对应 $k$ 项 $\frac{A_1}{ax+b}+\frac{A_2}{(ax+b)^2}+\cdots+\frac{A_k}{(ax+b)^k}$；
3. $Q_n$ 的二次单因式 $px^2+qx+r$ 对应一项 $\frac{Bx+D}{px^2+qx+r}$；
4. $Q_n$ 的 $k$ 重因式 $(px^2+qx+r)^k$ 对应 $k$ 项 $\frac{B_1x+D_1}{px^2+qx+r}+\cdots+\frac{B_kx+D_k}{(px^2+qx+r)^k}$。

待定系数的个数恰好等于 $n$。求系数时，可以通分后比较分子的系数（待定系数法），也可以代入适当的 $x$ 值（例如 $Q_n$ 的根）。

**例 6.4.2** 把下面的真分式分解成最简分式之和：(1) $\frac{x-2}{x^3-2x^2+x}$；(2) $\frac{3x^2+2}{x^2(x^2+1)}$。

解：(1) $x^3-2x^2+x = x(x-1)^2$，设 $\frac{x-2}{x(x-1)^2} = \frac Ax+\frac{B}{x-1}+\frac{C}{(x-1)^2}$，通分得 $x-2 = A(x-1)^2+Bx(x-1)+Cx$。令 $x = 0$ 得 $A = -2$；令 $x = 1$ 得 $C = -1$；比较 $x^2$ 的系数得 $A+B = 0$，$B = 2$。所以

$$
\frac{x-2}{x^3-2x^2+x} = -\frac2x+\frac2{x-1}-\frac1{(x-1)^2}.
$$

(2) 设 $\frac{3x^2+2}{x^2(x^2+1)} = \frac Ax+\frac B{x^2}+\frac{Cx+D}{x^2+1}$，比较系数得 $A = 0$，$B = 2$，$C = 0$，$D = 1$，即 $\frac{3x^2+2}{x^2(x^2+1)} = \frac2{x^2}+\frac1{x^2+1}$。

四类最简分式都可以积出：

$$
\begin{aligned}
&\text{(1)}\ \int\frac{A}{ax+b}\,\mathrm{d}x = \frac Aa\ln\lvert ax+b\rvert+C;\qquad\text{(2)}\ \int\frac{A}{(ax+b)^k}\,\mathrm{d}x = -\frac{A}{a(k-1)}(ax+b)^{-k+1}+C;\\
&\text{(3)}\ \int\frac{Bx+D}{px^2+qx+r}\,\mathrm{d}x = \frac B{2p}\int\frac{2px+q}{px^2+qx+r}\,\mathrm{d}x+\frac{2pD-Bq}{2p}\int\frac{\mathrm{d}x}{px^2+qx+r}\\
&\qquad = \frac{B}{2p}\ln\lvert px^2+qx+r\rvert+\frac{2pD-Bq}{p\sqrt{4pr-q^2}}\arctan\frac{2px+q}{\sqrt{4pr-q^2}}+C.
\end{aligned}
$$

(3) 的做法是把分子拆成"分母的导数的倍数"与常数，前者用 $\int\frac{\mathrm{d}u}{u}$，后者配方后用 $\int\frac{\mathrm{d}x}{(x+\alpha)^2+\beta^2} = \frac1\beta\arctan\frac{x+\alpha}\beta+C$。(4) 同样拆开：

$$
\int\frac{Bx+D}{(px^2+qx+r)^k}\,\mathrm{d}x = -\frac{B}{2p(k-1)}(px^2+qx+r)^{-k+1}+\frac{2pD-Bq}{2p^{k+1}}\int\frac{\mathrm{d}x}{\bigl[\bigl(x+\frac q{2p}\bigr)^2+\frac{4pr-q^2}{4p^2}\bigr]^k},
$$

最后一个积分令 $u = x+\frac{q}{2p}$ 后就是例 6.3.3 的 $I_k$，由递推公式求出。

**算法 6.4.1（有理函数的积分）**

1. 若 $\frac{P_m}{Q_n}$ 是假分式，用带余除法化为多项式与真分式之和；
2. 把分母 $Q_n$ 分解为一次因式与不可约二次因式的方幂之积；
3. 按定理 6.4.1 写出部分分式，用待定系数法求系数；
4. 对多项式与各最简分式分别积分（公式 (1)–(4) 与例 6.3.3 的递推公式），相加。

由此得到一个重要结论：有理函数的原函数总是初等函数，它由有理函数、对数函数与反正切函数组成。困难在于第 2 步：高次多项式的因式分解一般不能精确求出。实际计算时，要先观察能否用凑微分等方法绕过部分分式分解。

**例 6.4.3** 求不定积分：

(1) $\int\frac{x+5}{(x+1)^2}\,\mathrm{d}x = \int\Bigl(\frac{1}{x+1}+\frac{4}{(x+1)^2}\Bigr)\mathrm{d}x = \ln\lvert x+1\rvert-\frac{4}{x+1}+C$。

(2) $\int\frac{x+1}{x^2-4x+3}\,\mathrm{d}x = \int\Bigl(\frac2{x-3}-\frac1{x-1}\Bigr)\mathrm{d}x = 2\ln\lvert x-3\rvert-\ln\lvert x-1\rvert+C$。

(3) 不必对 $x(x^{10}+1)^2$ 做分解，令 $u = x^{10}$，$\frac{\mathrm{d}x}x = \frac{\mathrm{d}u}{10u}$：

$$
\int\frac{\mathrm{d}x}{x(x^{10}+1)^2} = \frac1{10}\int\frac{\mathrm{d}u}{u(u+1)^2} = \frac1{10}\int\Bigl(\frac1u-\frac1{u+1}-\frac1{(u+1)^2}\Bigr)\mathrm{d}u = \frac1{10}\Bigl(\ln\frac{x^{10}}{x^{10}+1}+\frac1{x^{10}+1}\Bigr)+C.
$$

(4) $\int\frac{x\,\mathrm{d}x}{x^2+4x+5} = \frac12\int\frac{(2x+4)\,\mathrm{d}x}{x^2+4x+5}-2\int\frac{\mathrm{d}x}{(x+2)^2+1} = \frac12\ln(x^2+4x+5)-2\arctan(x+2)+C$。

(5) $\int\frac{2x+5}{x^2+2x+3}\,\mathrm{d}x = \int\frac{(2x+2)\,\mathrm{d}x}{x^2+2x+3}+3\int\frac{\mathrm{d}x}{(x+1)^2+2} = \ln(x^2+2x+3)+\frac3{\sqrt2}\arctan\frac{x+1}{\sqrt2}+C$。

### 6.4.2. 三角函数有理式的积分

对 $\sin x$、$\cos x$ 与常数做有限次四则运算得到的表达式，称为三角函数有理式，记作 $R(\sin x,\cos x)$，其中 $R(u,v)$ 是 $u, v$ 的有理函数。先看能否用三角恒等式化简。

**例 6.4.4** 求不定积分：(1) $\int\sin mx\sin nx\,\mathrm{d}x$；(2) $\int\frac{\mathrm{d}x}{1+\sin x+\cos x}$；(3) $\int\frac{\mathrm{d}x}{a\cos x+b\sin x}$（$a^2+b^2\ne0$）。

解：(1) 积化和差：$m\ne\pm n$ 时，

$$
\int\sin mx\sin nx\,\mathrm{d}x = \frac12\int\bigl[\cos(m-n)x-\cos(m+n)x\bigr]\mathrm{d}x = \frac{\sin(m-n)x}{2(m-n)}-\frac{\sin(m+n)x}{2(m+n)}+C.
$$

（这个积分在 $[-\pi,\pi]$ 上为零，是 [2.2.9](/2.2.9) 中三角函数系正交性的来源。）

(2) 用半角公式：

$$
\int\frac{\mathrm{d}x}{2\sin\frac x2\cos\frac x2+2\cos^2\frac x2} = \int\frac{\frac12\sec^2\frac x2\,\mathrm{d}x}{\tan\frac x2+1} = \int\frac{\mathrm{d}\bigl(\tan\frac x2+1\bigr)}{\tan\frac x2+1} = \ln\Bigl\lvert1+\tan\frac x2\Bigr\rvert+C.
$$

(3) 用辅助角：$a\cos x+b\sin x = \sqrt{a^2+b^2}\sin(x+\varphi)$，其中 $\sin\varphi = \frac{a}{\sqrt{a^2+b^2}}$，$\cos\varphi = \frac{b}{\sqrt{a^2+b^2}}$，由例 6.2.1 (6) 后的公式

$$
\int\frac{\mathrm{d}x}{a\cos x+b\sin x} = \frac1{\sqrt{a^2+b^2}}\int\csc(x+\varphi)\,\mathrm{d}x = \frac{1}{\sqrt{a^2+b^2}}\ln\bigl\lvert\csc(x+\varphi)-\cot(x+\varphi)\bigr\rvert+C.
$$

没有简便方法时，总可以用代换 $t = \tan\frac x2$ 把三角函数有理式化为有理函数，这称为万能代换（Weierstrass substitution）。在 $(-\pi,\pi)$ 上 $x = 2\arctan t$，并且

$$
\sin x = \frac{2t}{1+t^2},\qquad\cos x = \frac{1-t^2}{1+t^2},\qquad\mathrm{d}x = \frac{2\,\mathrm{d}t}{1+t^2},
$$

于是

$$
\int R(\sin x,\cos x)\,\mathrm{d}x = \int R\Bigl(\frac{2t}{1+t^2},\frac{1-t^2}{1+t^2}\Bigr)\frac{2}{1+t^2}\,\mathrm{d}t,
$$

右端是有理函数的积分，由算法 6.4.1 可以求出。万能代换总是可行的，但得到的有理函数次数往往较高，应作为最后的手段。

**例 6.4.5** 求 $\int\frac{\mathrm{d}x}{3+5\cos x}$。

解：令 $t = \tan\frac x2$，

$$
\int\frac{\mathrm{d}x}{3+5\cos x} = \int\frac{1}{3+5\frac{1-t^2}{1+t^2}}\cdot\frac{2\,\mathrm{d}t}{1+t^2} = \int\frac{\mathrm{d}t}{4-t^2} = \frac14\ln\Bigl\lvert\frac{2+t}{2-t}\Bigr\rvert+C = \frac14\ln\Bigl\lvert\frac{2+\tan\frac x2}{2-\tan\frac x2}\Bigr\rvert+C.
$$

这里的结果在每个不含 $(2k+1)\pi$ 与 $3+5\cos x$ 零点的区间上成立。一般地，**周期函数**的原函数等于一个周期函数与一个线性函数之和（例如 $\int(1+\cos x)\,\mathrm{d}x = x+\sin x$），所以用 $\tan\frac x2$ 表示的原函数在 $x = (2k+1)\pi$ 处要分段拼接，才能得到整个实轴上连续的原函数。

## 6.5. 无理函数的积分

下面 $R(u,v)$ 表示 $u, v$ 的有理函数。对下面三类无理函数，适当的代换可以去掉根号，化为有理函数或三角函数有理式的积分（第二换元法）。

一、$\int R\bigl(x,\sqrt[n]{ax+b}\bigr)\,\mathrm{d}x$（$a\ne0$）：令 $ax+b = t^n$（$n$ 为偶数时 $t\ge0$），则

$$
x = \frac{t^n-b}{a},\qquad\mathrm{d}x = \frac{nt^{n-1}}{a}\,\mathrm{d}t,\qquad\int R\bigl(x,\sqrt[n]{ax+b}\bigr)\,\mathrm{d}x = \int R\Bigl(\frac{t^n-b}a,t\Bigr)\frac{nt^{n-1}}{a}\,\mathrm{d}t.
$$

被积函数中同时有 $\sqrt[m]{ax+b}$ 与 $\sqrt[n]{ax+b}$ 时，取 $m, n$ 的最小公倍数作为根指数。

二、$\int R\Bigl(x,\sqrt[n]{\frac{ax+b}{cx+d}}\Bigr)\,\mathrm{d}x$（$ad-bc\ne0$）：令 $\frac{ax+b}{cx+d} = t^n$（$n$ 为偶数时 $t\ge0$），则

$$
x = \frac{dt^n-b}{a-ct^n},\qquad\mathrm{d}x = \frac{n(ad-bc)t^{n-1}}{(a-ct^n)^2}\,\mathrm{d}t.
$$

（$ad-bc = 0$ 时 $\frac{ax+b}{cx+d}$ 是常数，根号本来就可以提出。）

三、$\int R\bigl(x,\sqrt{ax^2+bx+c}\bigr)\,\mathrm{d}x$（$a\ne0$）：配方 $ax^2+bx+c = a\bigl(x+\frac b{2a}\bigr)^2+\frac{4ac-b^2}{4a}$，提出常数后化为下列三种情形之一，再用三角代换化为三角函数有理式：

1. $\int R\bigl(x,\sqrt{(x+p)^2-q^2}\bigr)\,\mathrm{d}x$，令 $x+p = q\sec t$；
2. $\int R\bigl(x,\sqrt{(x+p)^2+q^2}\bigr)\,\mathrm{d}x$，令 $x+p = q\tan t$；
3. $\int R\bigl(x,\sqrt{q^2-(x+p)^2}\bigr)\,\mathrm{d}x$，令 $x+p = q\sin t$。

**例 6.5.1** 求 $\int\frac{\mathrm{d}x}{\sqrt x+\sqrt[3]x}$。

解：$2$ 与 $3$ 的最小公倍数为 $6$，令 $x = t^6$（$t>0$），$\mathrm{d}x = 6t^5\,\mathrm{d}t$：

$$
\int\frac{6t^5\,\mathrm{d}t}{t^3+t^2} = 6\int\frac{t^3}{t+1}\,\mathrm{d}t = 6\int\Bigl(t^2-t+1-\frac1{t+1}\Bigr)\mathrm{d}t = 2\sqrt x-3\sqrt[3]x+6\sqrt[6]x-6\ln\bigl(1+\sqrt[6]x\bigr)+C.
$$

**例 6.5.2** 求 $\int\frac1x\sqrt{\frac{1+x}{x}}\,\mathrm{d}x$（$x>0$）。

解：令 $t = \sqrt{\frac{1+x}{x}}$（$t>1$），$x = \frac{1}{t^2-1}$，$\mathrm{d}x = -\frac{2t\,\mathrm{d}t}{(t^2-1)^2}$：

$$
\int(t^2-1)\,t\cdot\frac{-2t}{(t^2-1)^2}\,\mathrm{d}t = -2\int\frac{t^2}{t^2-1}\,\mathrm{d}t = -2\int\Bigl(1+\frac{1}{t^2-1}\Bigr)\mathrm{d}t = -2t-\ln\frac{t-1}{t+1}+C,
$$

其中 $t = \sqrt{\frac{1+x}x}$。

**例 6.5.3** 求 $\int\sqrt{3+2x-x^2}\,\mathrm{d}x$。

解：$3+2x-x^2 = 4-(x-1)^2$，属于情形 3。令 $x-1 = 2\sin t$，$t\in\bigl[-\frac\pi2,\frac\pi2\bigr]$，与例 6.2.3 (2) 相同地得到

$$
\int\sqrt{4-(x-1)^2}\,\mathrm{d}x = \frac{x-1}{2}\sqrt{3+2x-x^2}+2\arcsin\frac{x-1}{2}+C.
$$

## 小结

不定积分的方法，每一种都是某条求导法则的逆用：

| 方法 | 公式 | 对应的求导法则 | 适用场合 |
|---|---|---|---|
| 线性性 | $\int(kf+lg) = k\int f+l\int g$ | 求导的线性性 | 拆成基本积分 |
| 第一换元法 | $\int f(\varphi(x))\varphi'(x)\,\mathrm{d}x = \int f(u)\,\mathrm{d}u$ | 链式法则 | 凑微分 |
| 第二换元法 | $\int f(x)\,\mathrm{d}x = \int f(\varphi(t))\varphi'(t)\,\mathrm{d}t$ | 链式法则、反函数求导 | 去根号：三角代换、根式代换、倒代换 |
| 分部积分法 | $\int u\,\mathrm{d}v = uv-\int v\,\mathrm{d}u$ | 乘积法则 | 多项式乘指数、三角；反三角、对数；循环与递推 |
| 有理函数 | 带余除法 + 部分分式 | — | 总能积出（分母能分解时） |
| 三角函数有理式 | $t = \tan\frac x2$ | — | 化为有理函数 |
| 无理函数 | $t = \sqrt[n]{ax+b}$、$t = \sqrt[n]{\frac{ax+b}{cx+d}}$、三角代换 | — | 化为有理函数或三角有理式 |

除 6.1.3 节的基本积分公式外，下列结果也常用（$a>0$）：

| 积分 | 结果 |
|---|---|
| $\int\tan x\,\mathrm{d}x$，$\int\cot x\,\mathrm{d}x$ | $-\ln\lvert\cos x\rvert+C$，$\ln\lvert\sin x\rvert+C$ |
| $\int\sec x\,\mathrm{d}x$，$\int\csc x\,\mathrm{d}x$ | $\ln\lvert\sec x+\tan x\rvert+C$，$\ln\lvert\csc x-\cot x\rvert+C$ |
| $\int\frac{\mathrm{d}x}{a^2+x^2}$ | $\frac1a\arctan\frac xa+C$ |
| $\int\frac{\mathrm{d}x}{a^2-x^2}$ | $\frac1{2a}\ln\bigl\lvert\frac{a+x}{a-x}\bigr\rvert+C$ |
| $\int\frac{\mathrm{d}x}{\sqrt{a^2-x^2}}$ | $\arcsin\frac xa+C$ |
| $\int\frac{\mathrm{d}x}{\sqrt{x^2\pm a^2}}$ | $\ln\bigl\lvert x+\sqrt{x^2\pm a^2}\bigr\rvert+C$ |
| $\int\sqrt{a^2-x^2}\,\mathrm{d}x$ | $\frac12\bigl(x\sqrt{a^2-x^2}+a^2\arcsin\frac xa\bigr)+C$ |
| $\int\sqrt{x^2\pm a^2}\,\mathrm{d}x$ | $\frac12\bigl(x\sqrt{x^2\pm a^2}\pm a^2\ln\lvert x+\sqrt{x^2\pm a^2}\rvert\bigr)+C$ |
| $\int\mathrm{e}^{ax}\cos bx\,\mathrm{d}x$ | $\frac{\mathrm{e}^{ax}(a\cos bx+b\sin bx)}{a^2+b^2}+C$ |
| $\int\mathrm{e}^{ax}\sin bx\,\mathrm{d}x$ | $\frac{\mathrm{e}^{ax}(a\sin bx-b\cos bx)}{a^2+b^2}+C$ |
| $\int\cos^nx\,\mathrm{d}x$ | $I_n = \frac1n\cos^{n-1}x\sin x+\frac{n-1}nI_{n-2}$ |
| $\int\frac{\mathrm{d}x}{(x^2+a^2)^{k}}$ | $I_{k+1} = \frac{2k-1}{2ka^2}I_k+\frac{x}{2ka^2(x^2+a^2)^k}$ |
