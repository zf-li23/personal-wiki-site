---
title: 函数项级数、幂级数与 Fourier 级数
---

[第 8 章](/2.2.8)的级数每一项都是数；本章让每一项都是函数，例如 $\sum x^n$、$\sum\frac{\sin nx}{n}$。对每个固定的 $x$，它就是一个数项级数，第 8 章的判别法照样适用；新的问题是和函数的性质：连续函数的无穷和是否连续？能否逐项积分、逐项求导？答案一般是否定的，关键的附加条件是一致收敛（9.1）。

然后讨论两类最重要的函数项级数。幂级数 $\sum a_nx^n$ 是"无穷次的多项式"：它的收敛域是一个区间，在区间内部可以逐项求导和积分（9.2）；[第 5 章](/2.2.5)的 **Taylor 多项式**取到无穷项就是 Taylor 级数，$\mathrm{e}^x$、$\sin x$、$\ln(1 + x)$ 等初等函数都能展开成幂级数。Fourier 级数 $\frac{a_0}{2} + \sum(a_n\cos nx + b_n\sin nx)$ 用不同频率的三角函数叠加表示周期函数（9.3），它的系数是函数在**正交函数系**上的坐标，与[线性代数 2.1.12](/2.1.12) 中的内积空间是同一个思想。幂级数将在复变函数中成为核心工具，Fourier 级数则是求解偏微分方程、分析信号的基础。

## 9.1. 函数项级数

**定义 9.1.1（函数项级数）** 设 $u_n(x)$（$n = 1, 2, \dots$）是定义在区间 $I$ 上的一列函数，称 $\sum_{n=1}^\infty u_n(x)$ 为 $I$ 上的函数项级数，$S_n(x) = \sum_{k=1}^n u_k(x)$ 为其部分和。若对每个 $x \in I$，$\sum u_n(x)$ 都收敛，则 $S(x) = \sum_{n=1}^\infty u_n(x) = \lim_{n\to\infty}S_n(x)$ 是 $I$ 上的函数，称为该级数的**和函数**。

### 9.1.1. 收敛点与收敛域

**定义 9.1.2（收敛域）** 若 $\sum u_n(x_0)$ 收敛，则称 $x_0$ 为 $\sum u_n(x)$ 的收敛点；全体收敛点组成的集合称为它的收敛域。

求收敛域就是对每个 $x$ 判断一个数项级数，常用比值或根值判别法处理 $\sum|u_n(x)|$，再单独讨论判别法失效的点。

**例 9.1.1**

1. $\sum_{n=0}^\infty ax^n$（$a \ne 0$）：**几何级数**，收敛域为 $(-1,1)$，和函数为 $\frac{a}{1-x}$。
2. $\sum_{n=1}^\infty\frac{x^n}{n^p}$：$\left|\frac{u_{n+1}}{u_n}\right| \to |x|$，$|x| < 1$ 时绝对收敛，$|x| > 1$ 时通项不趋于零。在 $x = \pm1$ 处由 **p 级数**与 **Leibniz 判别法**：$p \le 0$ 时收敛域为 $(-1,1)$；$0 < p \le 1$ 时为 $[-1,1)$；$p > 1$ 时为 $[-1,1]$。
3. $\sum_{n=1}^\infty\left(\frac{n+1}{n}\right)^nx^n$：$\sqrt[n]{|u_n|} = \left(1 + \frac1n\right)|x| \to |x|$；$|x| = 1$ 时 $|u_n| \to \mathrm{e} \ne 0$。收敛域为 $(-1,1)$。

设 $I$ 含于收敛域，我们关心三个问题：

1. 若每个 $u_n$ 在 $x_0$ 处连续，$S$ 是否在 $x_0$ 处连续？即能否逐项求极限：$\lim_{x\to x_0}\sum u_n(x) = \sum\lim_{x\to x_0}u_n(x)$？
2. 若每个 $u_n$ 在 $[a,b]$ 上可积，能否逐项积分：$\int_a^b\sum u_n(x)\,\mathrm{d}x = \sum\int_a^b u_n(x)\,\mathrm{d}x$？
3. 若每个 $u_n$ 可导，能否逐项求导：$\left(\sum u_n(x)\right)' = \sum u_n'(x)$？

三个问题都是两个极限过程能否交换次序。一般不能：级数 $x + \sum_{n=2}^\infty(x^n - x^{n-1})$ 的部分和 $S_n(x) = x^n$，收敛域为 $(-1,1]$，和函数

$$
S(x) = \begin{cases}0, & -1 < x < 1,\\ 1, & x = 1,\end{cases}
$$
每一项都连续，和函数却在 $x = 1$ 处间断。

### 9.1.2. 一致收敛

对函数列 $\{f_n\}$，"在 $I$ 上收敛于 $f$"有两种强弱不同的含义。

**定义 9.1.3（一致收敛）** 设 $\{f_n(x)\}$ 与 $f(x)$ 都定义在区间 $I$ 上。

1. 若对每个 $x \in I$，$\lim_{n\to\infty}f_n(x) = f(x)$，则称 $\{f_n\}$ 在 $I$ 上**逐点收敛**于 $f$。用 $\varepsilon$-$N$ 语言：对任意 $x \in I$ 与 $\varepsilon > 0$，存在 $N = N(\varepsilon, x)$，当 $n > N$ 时 $|f_n(x) - f(x)| < \varepsilon$。
2. 若对任意 $\varepsilon > 0$，存在只依赖于 $\varepsilon$ 的 $N = N(\varepsilon)$，当 $n > N$ 时，对一切 $x \in I$ 都有 $|f_n(x) - f(x)| < \varepsilon$，则称 $\{f_n\}$ 在 $I$ 上**一致收敛**于 $f$。

若函数项级数 $\sum u_n(x)$ 的部分和函数列 $\{S_n(x)\}$ 在 $I$ 上一致收敛于和函数 $S(x)$，则称该级数在 $I$ 上一致收敛。

两者的区别在于 $N$ 能否与 $x$ 无关，正如**连续函数**与**一致连续**的区别。几何上，一致收敛说的是：对任意 $\varepsilon$，$n$ 充分大以后，$y = S_n(x)$ 的整条图像都落在带状区域 $S(x) - \varepsilon < y < S(x) + \varepsilon$ 之中；各点收敛的速度"差不多"，$S_n$ 与 $S$ 因此有相似的性质。

**定理 9.1.1** $\{f_n\}$ 在 $I$ 上一致收敛于 $f$ $\iff$ $\lim_{n\to\infty}\sup_{x\in I}|f_n(x) - f(x)| = 0$。

这是定义的直接改写，也是判断一致收敛最常用的方法：求出 $f_n - f$ 在 $I$ 上的最大偏差，看它是否趋于零。

**例 9.1.2** $f_n(x) = x^n$ 在 $(0,1)$ 上逐点收敛于 $0$，但不一致收敛：$\sup_{(0,1)}x^n = 1$。具体地，取 $\varepsilon = \frac12$，无论 $n$ 多大，$x = 2^{-1/n} \in (0,1)$ 处 $x^n = \frac12$，图像总有一部分在 $\varepsilon$ 带之外。但对任意 $0 < b < 1$，它在 $[0,b]$ 上一致收敛：$\sup_{[0,b]}x^n = b^n \to 0$。

![x^n 在 [0,1] 上逐点收敛于一个间断的极限，但图像始终伸出 ε 带（左）；x^n(1-x)^n 被 4^{-n} 控制，一致收敛（右）](./plots/uniform-convergence.py)

**定理 9.1.2（Cauchy 一致收敛准则）** $\sum u_n(x)$ 在 $I$ 上一致收敛 $\iff$ 对任意 $\varepsilon > 0$，存在 $N$，当 $n > N$ 时，对一切正整数 $p$ 与一切 $x \in I$，

$$
|u_{n+1}(x) + u_{n+2}(x) + \cdots + u_{n+p}(x)| < \varepsilon.
$$

**证明** 必要性：$|S_{n+p}(x) - S_n(x)| \le |S_{n+p}(x) - S(x)| + |S(x) - S_n(x)|$。充分性：条件说明对每个 $x$，$\{S_n(x)\}$ 是 **Cauchy 数列**，有极限 $S(x)$；在 $|S_{n+p}(x) - S_n(x)| < \varepsilon$ 中令 $p \to \infty$ 得 $|S(x) - S_n(x)| \le \varepsilon$ 对一切 $x$ 成立。$\square$

由此，若 $\sum|u_n(x)|$ 在 $I$ 上一致收敛，则 $\sum u_n(x)$ 也在 $I$ 上一致收敛（$|\sum_{k=n+1}^{n+p}u_k| \le \sum_{k=n+1}^{n+p}|u_k|$）。

**定理 9.1.3（Weierstrass 判别法）** 若存在收敛的正项级数 $\sum c_n$，使对一切 $x \in I$ 与一切 $n$，$|u_n(x)| \le c_n$，则 $\sum u_n(x)$ 在 $I$ 上（绝对且）一致收敛。

**证明** 对每个 $x$，由**比较判别法**，$\sum u_n(x)$ 绝对收敛。又由数项级数的 Cauchy 收敛准则，对 $\varepsilon > 0$ 存在 $N$，$n > N$ 时 $\sum_{k=n+1}^{n+p}c_k < \varepsilon$，于是对一切 $x \in I$，$\left|\sum_{k=n+1}^{n+p}u_k(x)\right| \le \sum_{k=n+1}^{n+p}c_k < \varepsilon$，由定理 9.1.2。$\square$

$\sum c_n$ 称为优级数（majorant）。Weierstrass 判别法简单好用，但只能判断绝对且一致收敛的级数。

**例 9.1.3** $\sum_{n=1}^\infty x^n(1-x)^n$ 在 $[0,1]$ 上一致收敛：$x(1-x) = \frac14 - \left(x - \frac12\right)^2 \le \frac14$，故 $0 \le x^n(1-x)^n \le \frac{1}{4^n}$，$\sum\frac{1}{4^n}$ 收敛。

**例 9.1.4** 对 $\delta > 0$，$\sum_{n=1}^\infty\frac{1}{n^x}$ 在 $[1+\delta, +\infty)$ 上一致收敛：$\frac{1}{n^x} \le \frac{1}{n^{1+\delta}}$。它在 $(1, +\infty)$ 上不一致收敛：$\sum_{k=n+1}^{2n}\frac{1}{k^x} \ge \frac{n}{(2n)^x} \to \frac12$（$x \to 1^+$），对固定的 $n$，左端的上确界不小于 $\frac12$，Cauchy 准则不成立。

### 9.1.3. 一致收敛级数的分析性质

下面三个定理都先对函数列叙述，再应用于部分和得到级数的结论。

**定理 9.1.4（逐项求极限）** 设 $I$ 是区间。

1. 若 $f_n \in C(I)$，且 $\{f_n\}$ 在 $I$ 上一致收敛于 $f$，则 $f \in C(I)$；
2. 若 $u_n \in C(I)$，且 $\sum u_n(x)$ 在 $I$ 上一致收敛，则和函数 $S \in C(I)$，即对 $x_0 \in I$，$\lim_{x\to x_0}\sum u_n(x) = \sum\lim_{x\to x_0}u_n(x)$。

**证明** 1. 任取 $x_0 \in I$ 与 $\varepsilon > 0$，

$$
|f(x) - f(x_0)| \le |f(x) - f_n(x)| + |f_n(x) - f_n(x_0)| + |f_n(x_0) - f(x_0)|.
$$
由一致收敛，取定 $n$ 使第一、三项对一切 $x$ 都小于 $\varepsilon/3$；对这个 $n$，由 $f_n$ 在 $x_0$ 连续，存在 $\delta$，$|x - x_0| < \delta$ 时第二项小于 $\varepsilon/3$。（这里用到了第一项对所有 $x$ 一致地小，逐点收敛不能保证这一点。）2. 对部分和 $S_n$ 用 1。$\square$

由此可以反过来判断不一致收敛：例 9.1.2 中 $x^n$ 连续，极限函数在 $x = 1$ 处间断，所以 $x^n$ 在 $[0,1]$ 上不一致收敛。

**定理 9.1.5（逐项积分）** 1. 若 $f_n \in C[a,b]$ 且 $\{f_n\}$ 在 $[a,b]$ 上一致收敛于 $f$，则 $f$ 在 $[a,b]$ 上可积，且

$$
\int_a^b\lim_{n\to\infty}f_n(x)\,\mathrm{d}x = \lim_{n\to\infty}\int_a^b f_n(x)\,\mathrm{d}x.
$$

2. 若 $u_n \in C[a,b]$ 且 $\sum u_n(x)$ 在 $[a,b]$ 上一致收敛，则 $\int_a^b\sum u_n(x)\,\mathrm{d}x = \sum\int_a^b u_n(x)\,\mathrm{d}x$。

**证明** 由定理 9.1.4，$f$ 连续，故可积。$n$ 充分大时 $|f_n(x) - f(x)| < \frac{\varepsilon}{b-a}$ 对一切 $x$ 成立，于是 $\left|\int_a^b f_n - \int_a^b f\right| \le \int_a^b|f_n - f| < \varepsilon$。$\square$

**定理 9.1.6（逐项求导）** 1. 设 $f_n \in C^1[a,b]$，$\{f_n\}$ 在 $[a,b]$ 上逐点收敛于 $f$，且 $\{f_n'\}$ 在 $[a,b]$ 上一致收敛，则 $f$ 在 $[a,b]$ 上可导，且 $f'(x) = \lim_{n\to\infty}f_n'(x)$。

2. 设 $u_n \in C^1[a,b]$，$\sum u_n(x)$ 在 $[a,b]$ 上收敛，且 $\sum u_n'(x)$ 在 $[a,b]$ 上一致收敛，则 $\sum u_n(x)$ 可导，且 $\left(\sum u_n(x)\right)' = \sum u_n'(x)$。

**证明** 设 $f_n' \to g$ 一致收敛，则 $g$ 连续（定理 9.1.4）。由**微积分基本定理**，$f_n(x) = f_n(a) + \int_a^x f_n'(t)\,\mathrm{d}t$，令 $n \to \infty$ 并用定理 9.1.5，得 $f(x) = f(a) + \int_a^x g(t)\,\mathrm{d}t$，故 $f' = g$。$\square$

逐项求导的条件加在导数的级数上，而不是原级数上。原级数一致收敛远远不够：

**例 9.1.5** $\sum_{n=1}^\infty\frac{\sin(n^2x)}{n^2}$ 在 $(-\infty, +\infty)$ 上一致收敛（优级数 $\sum\frac1{n^2}$），和函数连续；但逐项求导得到的 $\sum\cos(n^2x)$ 对每个 $x$ 都发散。事实上若 $\cos(n^2x) \to 0$，则 $\cos(4n^2x) = \cos\bigl((2n)^2x\bigr)$ 也趋于零，而 $\cos4\theta = 8\cos^4\theta - 8\cos^2\theta + 1$ 给出 $\cos(4n^2x) \to 1$，矛盾。

**例 9.1.6** $S(x) = \sum_{n=1}^\infty\frac{\sin nx}{n^3}$ 在 $(-\infty, +\infty)$ 上连续可导：原级数收敛，导数级数 $\sum\frac{\cos nx}{n^2}$ 有优级数 $\sum\frac{1}{n^2}$，一致收敛，由定理 9.1.6，$S'(x) = \sum\frac{\cos nx}{n^2}$，再由定理 9.1.4 知 $S'$ 连续。

**例 9.1.7** $S(x) = \sum_{n=1}^\infty n\mathrm{e}^{-nx}$ 在 $(0, +\infty)$ 内连续且可导。

**证明** 任取 $x_0 > 0$，令 $\delta = x_0/2$。在 $[\delta, +\infty)$ 上 $n\mathrm{e}^{-nx} \le n\mathrm{e}^{-n\delta}$，$\sum n\mathrm{e}^{-n\delta}$ 收敛（比值判别法），由 Weierstrass 判别法，级数在 $[\delta, +\infty)$ 上一致收敛，$S$ 在 $x_0$ 处连续。导数级数 $\sum(-n^2\mathrm{e}^{-nx})$ 有优级数 $\sum n^2\mathrm{e}^{-n\delta}$，同理 $S$ 在 $x_0$ 处可导。$\square$

两个级数在 $(0, +\infty)$ 上都不一致收敛（$x \to 0^+$ 时通项不一致地小），但连续、可导是局部性质，只需在每一点附近的闭区间上一致收敛，这称为内闭一致收敛（uniform convergence on compact subsets）。

## 9.2. 幂级数

**定义 9.2.1（幂级数）** 形如 $\sum_{n=0}^\infty a_n(x - x_0)^n = a_0 + a_1(x - x_0) + a_2(x - x_0)^2 + \cdots$ 的函数项级数称为幂级数，$a_n$ 称为系数。

令 $t = x - x_0$ 即可化为 $x_0 = 0$ 的情形，以下主要讨论 $\sum a_nx^n$。

### 9.2.1. 收敛半径和收敛域

$\sum\frac{x^n}{2^n}$、$\sum\frac{x^n}{n!}$、$\sum n!\,x^n$ 的收敛域分别是 $(-2,2)$、$(-\infty, +\infty)$、$\{0\}$，都是以 $0$ 为中心的区间。这不是巧合：

**定理 9.2.1（Abel 定理）** 1. 若 $\sum a_nx^n$ 在 $x = b \ne 0$ 处收敛，则它在 $(-|b|, |b|)$ 内处处绝对收敛；
2. 若 $\sum a_nx^n$ 在 $x = b$ 处发散，则它在 $[-|b|, |b|]$ 之外处处发散。

**证明** 1. $\sum a_nb^n$ 收敛，通项有界：$|a_nb^n| \le M$。对 $|x| < |b|$，记 $r = |x/b| < 1$，则 $|a_nx^n| = |a_nb^n|\cdot r^n \le Mr^n$，与几何级数比较。2. 若有 $|x_1| > |b|$ 使级数在 $x_1$ 处收敛，由 1，它在 $b$ 处绝对收敛，矛盾。$\square$

于是幂级数的收敛性只有三种情况：仅在 $x = 0$ 处收敛；在 $(-\infty, +\infty)$ 上处处收敛；存在 $R > 0$，在 $(-R, R)$ 内绝对收敛、在 $[-R,R]$ 之外发散（$R$ 是集合 $\{|b| : \sum a_nb^n \text{ 收敛}\}$ 的**上确界**）。

**定义 9.2.2（收敛半径）** 上述第三种情况中的 $R$ 称为幂级数的收敛半径；第一、二种情况分别规定 $R = 0$、$R = +\infty$。幂级数的收敛域是 $(-R, R)$ 加上收敛的端点，称为**收敛区间**。

收敛半径只决定开区间 $(-R,R)$；端点 $x = \pm R$ 处级数可能收敛也可能发散，要代入后作为数项级数单独判断（例 9.1.1 的 2）。

**定理 9.2.2** 若 $\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right| = \rho$，则收敛半径 $R = \frac1\rho$（$\rho = 0$ 时 $R = +\infty$，$\rho = +\infty$ 时 $R = 0$）。

**定理 9.2.3** 若 $\lim_{n\to\infty}\sqrt[n]{|a_n|} = \rho$，则收敛半径 $R = \frac1\rho$（同上约定）。

**证明** 对 $\sum|a_nx^n|$ 分别用**比值判别法**与**根值判别法**：$\left|\frac{a_{n+1}x^{n+1}}{a_nx^n}\right| \to \rho|x|$，$\sqrt[n]{|a_nx^n|} \to \rho|x|$。$\rho|x| < 1$ 时绝对收敛；$\rho|x| > 1$ 时通项不趋于零，发散。$\square$

一般情形（极限不存在时）有 Cauchy–Hadamard 公式 $R = 1\big/\limsup_{n\to\infty}\sqrt[n]{|a_n|}$，这里不展开。

**例 9.2.1**

1. $\sum_{n=1}^\infty\frac{x^n}{n^p}$：$\frac{n^p}{(n+1)^p} \to 1$，$R = 1$，收敛区间见例 9.1.1。
2. $\sum_{n=1}^\infty(2^n + 3^n)x^n$：$\sqrt[n]{2^n + 3^n} \to 3$，$R = \frac13$；$x = \pm\frac13$ 时通项不趋于零，收敛区间为 $\left(-\frac13, \frac13\right)$。
3. $\sum_{n=1}^\infty\frac{x^{2n+1}}{n\cdot3^n}$：缺奇数次以外的项，系数之比没有意义，直接对通项用比值判别法：$\left|\frac{u_{n+1}}{u_n}\right| \to \frac{x^2}{3}$，故 $R = \sqrt3$。$x = \pm\sqrt3$ 时通项为 $\pm\frac{\sqrt3}{n}$，发散。收敛区间为 $(-\sqrt3, \sqrt3)$。

### 9.2.2. 幂级数的分析性质

**引理 9.2.1** 设 $\sum a_nx^n$ 的收敛半径 $R > 0$，则对任意 $0 < b < R$，它在 $[-b, b]$ 上一致收敛。

**证明** $|a_nx^n| \le |a_nb^n|$，而 $b$ 在收敛区间内部，$\sum|a_nb^n|$ 收敛，由 **Weierstrass 判别法**。$\square$

即幂级数在 $(-R, R)$ 内闭一致收敛（但在 $(-R,R)$ 上未必一致收敛，例如 $\sum x^n$ 在 $(-1,1)$ 上不一致收敛）。

**引理 9.2.2** 逐项求导后的幂级数 $\sum_{n=1}^\infty na_nx^{n-1}$ 与原级数有相同的收敛半径；逐项积分得到的 $\sum\frac{a_n}{n+1}x^{n+1}$ 也是如此。

**证明** 设求导后的收敛半径为 $R'$。若 $R' < R$，取 $R' < x_0 < x_1 < R$，则

$$
n|a_n|x_0^{n-1} = \frac{n}{x_1}\left(\frac{x_0}{x_1}\right)^{n-1}|a_n|x_1^n \le M|a_n|x_1^n,
$$
（$n(x_0/x_1)^{n-1} \to 0$，有界），$\sum|a_n|x_1^n$ 收敛，故 $\sum n|a_n|x_0^{n-1}$ 收敛，与 $x_0 > R'$ 矛盾。若 $R' > R$，取 $R < x_0 < R'$，$n > x_0$ 时 $|a_n|x_0^n \le n|a_n|x_0^{n-1}$，后者之和收敛，与 $x_0 > R$ 矛盾。积分的情形：原级数是积分后的级数逐项求导的结果。$\square$

**定理 9.2.4** 设 $\sum a_nx^n$ 的收敛半径为 $R > 0$，和函数为 $f(x)$，则

1. $f$ 在 $(-R, R)$ 内连续；
2. $f$ 在 $(-R, R)$ 内可导，且可以逐项求导：$f'(x) = \sum_{n=1}^\infty na_nx^{n-1}$；
3. 对 $x \in (-R, R)$，可以逐项积分：$\int_0^x f(t)\,\mathrm{d}t = \sum_{n=0}^\infty\frac{a_n}{n+1}x^{n+1}$。

**证明** 任取 $x \in (-R, R)$，取 $|x| < b < R$。由引理 9.2.1，原级数与导数级数（收敛半径也是 $R$，引理 9.2.2）都在 $[-b, b]$ 上一致收敛，由定理 9.1.4、9.1.6、9.1.5 分别得到 1、2、3。$\square$

**推论 9.2.1** 幂级数的和函数在 $(-R, R)$ 内有任意阶导数，

$$
f^{(k)}(x) = \sum_{n=k}^\infty n(n-1)\cdots(n-k+1)a_nx^{n-k}, \qquad \text{特别地} \quad a_k = \frac{f^{(k)}(0)}{k!}.
$$

最后一式说明：若一个函数能展开成幂级数，展开式是唯一的，系数由函数在 $0$ 处的各阶导数决定。

定理 9.2.4 只涉及开区间 $(-R,R)$。若级数在端点收敛，和函数在端点处的单侧连续性需要另一个定理：

**定理 9.2.5（Abel 第二定理）** 若 $\sum a_nx^n$ 在 $x = R$ 处收敛，则它在 $[0, R]$ 上一致收敛，和函数在 $x = R$ 处左连续：$\lim_{x\to R^-}\sum a_nx^n = \sum a_nR^n$。$x = -R$ 处同理。

**证明** 写 $a_nx^n = a_nR^n\cdot\left(\frac xR\right)^n$。$\sum a_nR^n$ 收敛（与 $x$ 无关），$\left(\frac xR\right)^n$ 对每个 $x \in [0,R]$ 单调且 $\le 1$。重复 **Abel 判别法**的证明（引理 8.3.1 中的界与 $x$ 无关），由 Cauchy 一致收敛准则得一致收敛，再由定理 9.1.4 得连续性。$\square$

所以幂级数的和函数在整个收敛区间（含收敛的端点）上连续。

**例 9.2.2** 由 $\frac{1}{1-x} = \sum_{n=0}^\infty x^n$（$|x| < 1$），逐项求导与逐项积分得

$$
\frac{1}{(1-x)^2} = \sum_{n=1}^\infty nx^{n-1}, \qquad -\ln(1-x) = \sum_{n=1}^\infty\frac{x^n}{n}, \qquad |x| < 1.
$$

第二式在 $x = -1$ 处收敛（交错调和级数），由 Abel 第二定理，令 $x \to -1^+$ 得 $\ln2 = 1 - \frac12 + \frac13 - \cdots$。

### 9.2.3. 函数的幂级数展开

**定义 9.2.3（Taylor 级数）** 设 $f$ 在 $x_0$ 的某个**邻域**内有任意阶导数，称幂级数

$$
\sum_{n=0}^\infty\frac{f^{(n)}(x_0)}{n!}(x - x_0)^n = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(x_0)}{2!}(x - x_0)^2 + \cdots
$$
为 $f$ 在 $x_0$ 处的 Taylor 级数，记作 $f(x) \sim \sum\frac{f^{(n)}(x_0)}{n!}(x - x_0)^n$；$x_0 = 0$ 时称为 $f$ 的 **Maclaurin 级数**。

记号 $\sim$ 表示 Taylor 级数只是形式上写出来的，它未必收敛，收敛时也未必等于 $f(x)$。

**例 9.2.3** $f(x) = \mathrm{e}^{-1/x^2}$（$x \ne 0$），$f(0) = 0$。可以验证 $f$ 在 $\mathbb{R}$ 上无穷次可导，且 $f^{(n)}(0) = 0$ 对一切 $n$ 成立（每次求导得到 $P(1/x)\mathrm{e}^{-1/x^2}$ 的形式，$P$ 是多项式，$x \to 0$ 时趋于零）。于是 $f$ 的 Maclaurin 级数处处收敛于 $0$，但除 $x = 0$ 外不等于 $f(x)$。

什么时候 Taylor 级数等于 $f$？由**泰勒公式**，$f(x) = \sum_{k=0}^n\frac{f^{(k)}(x_0)}{k!}(x - x_0)^k + R_n(x)$，Taylor 级数的部分和恰好是 **Taylor 多项式**，于是：

**定理 9.2.6** 设 $f$ 在 $(x_0 - R, x_0 + R)$ 内有任意阶导数，则 $f$ 在该区间内可以展开成 Taylor 级数（即 Taylor 级数收敛于 $f(x)$）的充分必要条件是：对区间内每个 $x$，余项 $R_n(x) \to 0$（$n \to \infty$）。

余项可以用 **Lagrange 余项** $R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x - x_0)^{n+1}$（$\xi$ 介于 $x_0$ 与 $x$ 之间），也可以用积分余项

$$
R_n(x) = \frac{1}{n!}\int_{x_0}^x f^{(n+1)}(t)(x - t)^n\,\mathrm{d}t
$$
（对 $f(x) - f(x_0) = \int_{x_0}^x f'(t)\,\mathrm{d}t$ 反复分部积分即得）。

**定理 9.2.7** 设 $f$ 在 $(x_0 - R, x_0 + R)$ 内有任意阶导数，且存在 $M > 0$，使对区间内一切 $x$ 与一切 $n$，$|f^{(n)}(x)| \le M$，则 $f$ 在该区间内可以展开成 Taylor 级数。

**证明** $|R_n(x)| \le \frac{M}{(n+1)!}|x - x_0|^{n+1} \le \frac{MR^{n+1}}{(n+1)!} \to 0$。$\square$

**例 9.2.4（五个基本展开式）**

1. $\mathrm{e}^x$：对任意 $R > 0$，在 $(-R,R)$ 上 $|(\mathrm{e}^x)^{(n)}| = \mathrm{e}^x \le \mathrm{e}^R$，由定理 9.2.7，$\mathrm{e}^x = \sum_{n=0}^\infty\frac{x^n}{n!}$，$x \in \mathbb{R}$。
2. $\sin x$：$\sin^{(n)}x = \sin\left(x + \frac{n\pi}{2}\right)$，$|\sin^{(n)}x| \le 1$，故 $\sin x = \sum_{k=0}^\infty\frac{(-1)^k}{(2k+1)!}x^{2k+1}$，$x \in \mathbb{R}$；逐项求导得 $\cos x = \sum_{k=0}^\infty\frac{(-1)^k}{(2k)!}x^{2k}$，$x \in \mathbb{R}$。
3. $\ln(1 + x)$：对 $\frac{1}{1+t} = \sum(-1)^nt^n$ 在 $[0,x]$ 上逐项积分，得 $\ln(1 + x) = \sum_{n=1}^\infty\frac{(-1)^{n-1}}{n}x^n$，$|x| < 1$；$x = 1$ 时级数收敛，由 Abel 第二定理（或直接估计 Lagrange 余项 $|R_n(1)| \le \frac{1}{n+1}$），展开式在 $(-1, 1]$ 上成立。
4. $(1 + x)^\alpha$（$\alpha$ 不是非负整数）：记广义二项式系数 $\binom\alpha n = \frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}$。比值判别法给出 $\sum\binom\alpha nx^n$ 的收敛半径为 $1$；用积分余项可以证明 $|x| < 1$ 时 $R_n(x) \to 0$，于是

$$
(1 + x)^\alpha = \sum_{n=0}^\infty\binom\alpha nx^n, \qquad |x| < 1,
$$
右端称为二项式级数（binomial series）。$\alpha$ 是非负整数时它是有限和，即二项式定理，对一切 $x$ 成立。端点的情况依赖于 $\alpha$：$\alpha \le -1$ 时两端都发散，展开在 $(-1,1)$ 上成立；$-1 < \alpha < 0$ 时只在 $x = 1$ 处收敛，展开在 $(-1, 1]$ 上成立；$\alpha > 0$ 时两端都收敛，展开在 $[-1, 1]$ 上成立。$\alpha = -1$ 就是 $\frac{1}{1+x} = \sum(-1)^nx^n$。

![1/(1+x^2) 的 Taylor 部分和在 |x| < 1 内逼近函数，在 |x| > 1 处发散，尽管函数在整个实轴上光滑](./plots/taylor-radius.py)

收敛半径不一定能从函数在实轴上的表现看出来：$\frac{1}{1+x^2} = \sum(-1)^nx^{2n}$ 的收敛半径是 $1$，而这个函数在 $\mathbb{R}$ 上处处无穷次可导。原因在复平面上：$1 + z^2$ 在 $z = \pm\mathrm{i}$ 处为零，它们到原点的距离是 $1$。这在复变函数中会得到完整的解释。

求展开式时很少直接计算 $f^{(n)}(x_0)$，更常见的是由基本展开式经过代换、四则运算、逐项求导与积分得到（间接展开），展开式的唯一性（推论 9.2.1）保证结果就是 Taylor 级数。

**例 9.2.5**

1. $\frac{1}{(1-x)(2-x)} = \frac{1}{1-x} - \frac{1}{2-x} = \sum_{n=0}^\infty x^n - \frac12\sum_{n=0}^\infty\left(\frac x2\right)^n = \sum_{n=0}^\infty\left(1 - \frac{1}{2^{n+1}}\right)x^n$，$|x| < 1$（取两个收敛区间的交）。
2. 把 $\ln x$ 展开成 $x - 2$ 的幂级数：$\ln x = \ln2 + \ln\left(1 + \frac{x-2}{2}\right) = \ln2 + \sum_{n=1}^\infty\frac{(-1)^{n-1}}{n\,2^n}(x - 2)^n$，由 $-1 < \frac{x-2}{2} \le 1$，展开在 $(0, 4]$ 上成立。
3. $\arctan x = \int_0^x\frac{\mathrm{d}t}{1+t^2} = \sum_{n=0}^\infty\frac{(-1)^n}{2n+1}x^{2n+1}$，$|x| < 1$；$x = \pm1$ 时级数收敛，由 Abel 第二定理展开在 $[-1,1]$ 上成立。$x = 1$ 给出 $\frac\pi4 = 1 - \frac13 + \frac15 - \cdots$。

### 9.2.4. 幂级数求和

反过来，已知幂级数求和函数，进而求数项级数的和。

**算法 9.2.1（幂级数求和）**

1. 求收敛半径与收敛区间；
2. 通过逐项求导或逐项积分（必要时先乘除 $x$ 的幂），把级数化为已知和函数的级数（几何级数、$\mathrm{e}^x$ 等）；
3. 对第 2 步作逆运算（积分或求导）得到和函数，注意积分常数与 $x = 0$ 的特殊处理；
4. 数项级数 $\sum c_n$ 的和：找幂级数 $\sum c_nx^n$，代入适当的 $x$（端点处用 Abel 第二定理）。

**例 9.2.6** 求 $\sum_{n=1}^\infty\frac{n}{(n+1)!}$。

**解** 令 $S(x) = \sum_{n=1}^\infty\frac{n}{(n+1)!}x^{n-1}$，$R = +\infty$。逐项积分：对 $x \ne 0$，

$$
\int_0^x S(t)\,\mathrm{d}t = \sum_{n=1}^\infty\frac{x^n}{(n+1)!} = \frac1x\sum_{n=1}^\infty\frac{x^{n+1}}{(n+1)!} = \frac{\mathrm{e}^x - 1 - x}{x}.
$$

求导得 $S(x) = \frac{(x-1)\mathrm{e}^x + 1}{x^2}$，所求的和为 $S(1) = 1$。（也可以直接裂项：$\frac{n}{(n+1)!} = \frac{1}{n!} - \frac{1}{(n+1)!}$。）

**例 9.2.7** 求 $\sum_{n=1}^\infty(-1)^n\frac{n(n+1)}{2^n}$。

**解** 令 $S(x) = \sum_{n=1}^\infty(-1)^nn(n+1)x^{n-1}$，$|x| < 1$，所求为 $\frac12S\left(\frac12\right)$。积分两次：

$$
\int_0^x\left(\int_0^t S(s)\,\mathrm{d}s\right)\mathrm{d}t = \sum_{n=1}^\infty(-1)^nx^{n+1} = -\frac{x^2}{1+x} = 1 - x - \frac{1}{1+x}.
$$

求导两次得 $S(x) = -\frac{2}{(1+x)^3}$，所求的和为 $\frac12\cdot\left(-\frac{2}{(3/2)^3}\right) = -\frac{8}{27}$。

## 9.3. Fourier 级数

### 9.3.1. 周期函数的 Fourier 级数

以 $T$ 为周期的最简单的运动是简谐振动 $A\sin(\omega x + \varphi)$，其中 $A > 0$ 是振幅，$\omega = \frac{2\pi}{T}$ 是角频率，$\varphi$ 是初相位。对正整数 $n$，$A_n\sin(n\omega x + \varphi_n)$ 也以 $T$ 为周期，称为 $n$ 次谐波，它可以写成 $a_n\cos n\omega x + b_n\sin n\omega x$（$a_n = A_n\sin\varphi_n$，$b_n = A_n\cos\varphi_n$）。形如

$$
\frac{a_0}{2} + \sum_{n=1}^\infty(a_n\cos n\omega x + b_n\sin n\omega x)
$$
的级数称为三角级数（trigonometric series）。问题是：一个以 $T$ 为周期的函数，能否表示为谐波的叠加？思路是先假设能表示，求出系数应当是什么，再讨论级数是否真的收敛于 $f$。下面先取 $T = 2\pi$（$\omega = 1$）。

求系数的关键是三角函数的正交性。

**定义 9.3.1（正交函数系）** 设 $f, g$ 是区间 $[a,b]$（有限或无限）上的函数，若 $\int_a^b f(x)g(x)\,\mathrm{d}x = 0$，则称 $f$ 与 $g$ 在 $[a,b]$ 上正交。若函数列 $\varphi_0, \varphi_1, \varphi_2, \dots$ 满足 $\int_a^b\varphi_i(x)\varphi_j(x)\,\mathrm{d}x = 0$（$i \ne j$），则称它是 $[a,b]$ 上的正交函数系；若还满足 $\int_a^b\varphi_i^2\,\mathrm{d}x = 1$，则称它是规范正交的。

这就是函数空间中关于积分**内积** $\langle f, g\rangle = \int_a^b fg\,\mathrm{d}x$ 的**正交**（[2.1.12 §12.3](/2.1.12#sec-12.3)）。

**例 9.3.1** 三角函数系 $1, \cos x, \sin x, \cos2x, \sin2x, \dots$ 是 $[-\pi, \pi]$ 上的正交函数系：由积化和差，$m \ne n$ 时 $\int_{-\pi}^\pi\cos mx\cos nx\,\mathrm{d}x = \int_{-\pi}^\pi\sin mx\sin nx\,\mathrm{d}x = 0$，且对一切 $m, n$，$\int_{-\pi}^\pi\sin mx\cos nx\,\mathrm{d}x = 0$（奇函数）。又

$$
\int_{-\pi}^\pi1\,\mathrm{d}x = 2\pi, \qquad \int_{-\pi}^\pi\cos^2nx\,\mathrm{d}x = \int_{-\pi}^\pi\sin^2nx\,\mathrm{d}x = \pi \quad (n \ge 1),
$$
所以 $\frac{1}{\sqrt{2\pi}}, \frac{\cos x}{\sqrt\pi}, \frac{\sin x}{\sqrt\pi}, \dots$ 是规范正交的。一般地，$1, \cos\frac{n\pi x}{l}, \sin\frac{n\pi x}{l}$（$n \ge 1$）是任意长为 $2l$ 的区间上的正交函数系。

设 $f$ 以 $2\pi$ 为周期，$f(x) = \frac{a_0}{2} + \sum_{n=1}^\infty(a_n\cos nx + b_n\sin nx)$，且右端可以逐项积分（例如一致收敛）。两边在 $[-\pi,\pi]$ 上积分，由正交性只剩一项：$\int_{-\pi}^\pi f\,\mathrm{d}x = \pi a_0$；两边乘 $\cos nx$ 再积分，只剩 $\int_{-\pi}^\pi f(x)\cos nx\,\mathrm{d}x = a_n\pi$；乘 $\sin nx$ 同理。这正是"在正交基下求坐标只需作内积"。

**定义 9.3.2（Fourier 级数）** 设 $f$ 以 $2\pi$ 为周期，在 $[-\pi, \pi]$ 上可积。称

$$
a_n = \frac1\pi\int_{-\pi}^\pi f(x)\cos nx\,\mathrm{d}x \;(n = 0, 1, 2, \dots), \qquad b_n = \frac1\pi\int_{-\pi}^\pi f(x)\sin nx\,\mathrm{d}x \;(n = 1, 2, \dots)
$$
为 $f$ 的 **Fourier 系数**，称由它们构成的三角级数为 $f$ 的 Fourier 级数，记作

$$
f(x) \sim \frac{a_0}{2} + \sum_{n=1}^\infty(a_n\cos nx + b_n\sin nx).
$$

$a_0$ 的公式与 $a_n$ 统一，所以常数项写成 $\frac{a_0}{2}$。与 Taylor 级数一样，$\sim$ 只表示"由 $f$ 算出的级数"：可积函数的 Fourier 级数未必收敛，收敛时也未必收敛于 $f$。下面的定理给出一个便于验证的充分条件。

**定理 9.3.1（Dirichlet 收敛定理）** 设 $f$ 以 $2\pi$ 为周期，在 $[-\pi, \pi]$ 上分段单调（或只有有限个极值点），并且至多有有限个第一类间断点（可去或跳跃），则 $f$ 的 Fourier 级数处处收敛，且

1. 在 $f$ 的连续点 $x_0$ 处，级数的和等于 $f(x_0)$；
2. 在 $f$ 的间断点 $x_0$ 处，级数的和等于 $\frac12\bigl(f(x_0 - 0) + f(x_0 + 0)\bigr)$；
3. 在端点 $x = \pm\pi$ 处，级数的和等于 $\frac12\bigl(f(-\pi + 0) + f(\pi - 0)\bigr)$。

定理中的条件称为 **Dirichlet 条件**。第 3 条其实是第 2 条：把 $[-\pi,\pi]$ 上的函数按周期延拓后，$\pm\pi$ 一般是跳跃间断点。有的教材称这个定理为"Dirichlet 判别法"，为了与 8.3.4 节判断数项级数的 **Dirichlet 判别法**区分，这里称为 Dirichlet 收敛定理。证明要用 9.3.3 节的 Dirichlet 核，这里从略。

**例 9.3.2** 设 $f$ 以 $2\pi$ 为周期，$f(x) = -1$（$-\pi < x < 0$），$f(x) = 1$（$0 < x < \pi$）（方波）。$f$ 是**奇函数**，$a_n = 0$；

$$
b_n = \frac2\pi\int_0^\pi\sin nx\,\mathrm{d}x = \frac{2(1 - \cos n\pi)}{n\pi} = \begin{cases}\dfrac{4}{n\pi}, & n \text{ 为奇数},\\ 0, & n \text{ 为偶数}.\end{cases}
$$

由 Dirichlet 收敛定理，

$$
\frac4\pi\sum_{n=1}^\infty\frac{\sin(2n-1)x}{2n-1} = \begin{cases}1, & 0 < x < \pi,\\ 0, & x = -\pi, 0, \pi,\\ -1, & -\pi < x < 0.\end{cases}
$$

在跳跃点处，级数收敛到左右极限的平均值 $0$。取 $x = \frac\pi2$ 得 $1 - \frac13 + \frac15 - \cdots = \frac\pi4$。

![方波的 Fourier 部分和：在跳跃点收敛到 0（左）；跳跃点附近的过冲随项数增加而变窄，但高度不减，约为跳跃高度的 9%（右）](./plots/fourier-gibbs.py)

图中可以看到，在跳跃点附近，部分和总有一个约 $1.179$ 的峰（跳跃高度为 $2$，过冲约 $0.179$，即约 $9\%$），项数增加时峰向跳跃点靠拢、变窄，但高度不降低。这称为 Gibbs 现象（Gibbs phenomenon）。它与 Dirichlet 收敛定理并不矛盾：对每个固定的 $x \ne 0$，峰终将移到 $x$ 的左边，$S_N(x) \to 1$；但收敛在跳跃点附近不是一致的。这也是定理 9.1.4 的反面：连续函数（部分和）一致收敛的极限必连续，而方波不连续。

**例 9.3.3** 设 $f$ 以 $2\pi$ 为周期，$f(x) = \frac\pi2 - |x|$（$-\pi \le x \le \pi$）（三角波）。$f$ 是**偶函数**，$b_n = 0$，$a_0 = 0$，

$$
a_n = \frac2\pi\int_0^\pi\left(\frac\pi2 - x\right)\cos nx\,\mathrm{d}x = \frac{2(1 - \cos n\pi)}{\pi n^2}, \qquad a_{2k} = 0, \quad a_{2k+1} = \frac{4}{\pi(2k+1)^2}.
$$

$f$ 连续且 $f(-\pi) = f(\pi)$，由 Dirichlet 收敛定理，$f(x) = \frac4\pi\sum_{k=0}^\infty\frac{\cos(2k+1)x}{(2k+1)^2}$ 对一切 $x$ 成立（由 Weierstrass 判别法，收敛还是一致的）。取 $x = 0$：

$$
\sum_{k=0}^\infty\frac{1}{(2k+1)^2} = \frac{\pi^2}{8}, \qquad \text{于是} \quad \sum_{n=1}^\infty\frac{1}{n^2} = \frac{\pi^2}{8} + \frac14\sum_{n=1}^\infty\frac{1}{n^2} \;\Rightarrow\; \sum_{n=1}^\infty\frac{1}{n^2} = \frac{\pi^2}{6}.
$$

三角波连续，系数按 $\frac{1}{n^2}$ 衰减；方波有跳跃，系数只按 $\frac1n$ 衰减。函数越光滑，Fourier 系数衰减越快。

对周期为 $2l$ 的函数，令 $x = \frac{l}{\pi}t$，把周期 $2l$ 化为 $2\pi$，得到

$$
f(x) \sim \frac{a_0}{2} + \sum_{n=1}^\infty\left(a_n\cos\frac{n\pi x}{l} + b_n\sin\frac{n\pi x}{l}\right), \quad a_n = \frac1l\int_{-l}^lf(x)\cos\frac{n\pi x}{l}\,\mathrm{d}x, \quad b_n = \frac1l\int_{-l}^lf(x)\sin\frac{n\pi x}{l}\,\mathrm{d}x.
$$

由**周期函数**积分的性质（[定理 7.4.3](/2.2.7#thm-7.4.3)），系数可以在任意一个长为 $2l$ 的周期 $[a, a+2l]$ 上计算。Dirichlet 收敛定理照样成立。

**例 9.3.4** 把 $[0,2)$ 上的 $f(x) = 2x + 1$ 表示为 Fourier 级数。

**解** 把 $f$ 看作以 $2$ 为周期的函数（$l = 1$），在 $[0,2]$ 上计算系数：$a_0 = \int_0^2(2x+1)\,\mathrm{d}x = 6$，$a_n = \int_0^2(2x+1)\cos n\pi x\,\mathrm{d}x = 0$，$b_n = \int_0^2(2x+1)\sin n\pi x\,\mathrm{d}x = -\frac{4}{n\pi}$。由 Dirichlet 收敛定理，

$$
3 - \frac4\pi\sum_{n=1}^\infty\frac{\sin n\pi x}{n} = \begin{cases}2x + 1, & 0 < x < 2,\\ \frac12\bigl(f(0) + f(2 - 0)\bigr) = 3, & x = 0, 2.\end{cases}
$$

### 9.3.2. 正弦级数和余弦级数

若 $f$ 是 $[-\pi,\pi]$ 上的**奇函数**，则 $a_n = 0$，$b_n = \frac2\pi\int_0^\pi f(x)\sin nx\,\mathrm{d}x$，$f$ 的 Fourier 级数只含正弦项，称为正弦级数（Fourier sine series）。若 $f$ 是**偶函数**，则 $b_n = 0$，$a_n = \frac2\pi\int_0^\pi f(x)\cos nx\,\mathrm{d}x$，Fourier 级数只含常数项与余弦项，称为余弦级数（Fourier cosine series）。

只在 $[0, \pi]$ 上有定义的函数，可以先延拓到 $[-\pi, \pi]$ 上，再按周期 $2\pi$ 延拓，延拓方式不同，得到的级数也不同：

- 令 $f(x) = -f(-x)$（$-\pi \le x < 0$），称为奇延拓（odd extension），得到正弦级数 $f(x) \sim \sum_{n=1}^\infty b_n\sin nx$，$b_n = \frac2\pi\int_0^\pi f(x)\sin nx\,\mathrm{d}x$；
- 令 $f(x) = f(-x)$（$-\pi \le x < 0$），称为偶延拓（even extension），得到余弦级数 $f(x) \sim \frac{a_0}{2} + \sum_{n=1}^\infty a_n\cos nx$，$a_n = \frac2\pi\int_0^\pi f(x)\cos nx\,\mathrm{d}x$。

$[0, l]$ 上的函数同理：$b_n = \frac2l\int_0^lf(x)\sin\frac{n\pi x}{l}\,\mathrm{d}x$，$a_n = \frac2l\int_0^lf(x)\cos\frac{n\pi x}{l}\,\mathrm{d}x$。两种展开在 $(0,l)$ 内的连续点处都收敛于 $f$，区别在端点：奇延拓在 $x = 0, l$ 处一般产生跳跃，正弦级数在那里收敛于 $0$；偶延拓保持连续，余弦级数在端点收敛于 $f(0)$、$f(l)$。

**例 9.3.5** 把 $f(x) = x$（$0 \le x \le \pi$）分别展开成余弦级数与正弦级数。

**解** 余弦级数：$a_0 = \frac2\pi\int_0^\pi x\,\mathrm{d}x = \pi$，$a_n = \frac2\pi\int_0^\pi x\cos nx\,\mathrm{d}x = \frac{2\bigl((-1)^n - 1\bigr)}{\pi n^2}$，偶延拓后是连续的三角波，

$$
x = \frac\pi2 - \frac4\pi\sum_{k=0}^\infty\frac{\cos(2k+1)x}{(2k+1)^2}, \qquad 0 \le x \le \pi.
$$

正弦级数：$b_n = \frac2\pi\int_0^\pi x\sin nx\,\mathrm{d}x = \frac{2(-1)^{n-1}}{n}$，奇延拓后在 $x = \pi$ 处跳跃，

$$
x = 2\sum_{n=1}^\infty\frac{(-1)^{n-1}\sin nx}{n}, \qquad 0 \le x < \pi,
$$
而在 $x = \pi$ 处级数的和为 $0$。余弦级数的系数按 $\frac{1}{n^2}$ 衰减，正弦级数只按 $\frac1n$ 衰减，与例 9.3.2、9.3.3 的观察一致。

**例 9.3.6** 把 $f(x) = \sin\frac{\pi x}{l}$（$0 \le x < \frac l2$），$f(x) = 0$（$\frac l2 \le x \le l$）展开成正弦级数。

**解** $b_1 = \frac2l\int_0^{l/2}\sin^2\frac{\pi x}{l}\,\mathrm{d}x = \frac12$；$n \ge 2$ 时，由积化和差，$b_n = \frac2l\int_0^{l/2}\sin\frac{\pi x}{l}\sin\frac{n\pi x}{l}\,\mathrm{d}x$ 在 $n$ 为奇数时为 $0$，在 $n = 2k$ 时为 $-\frac{(-1)^k4k}{\pi(4k^2 - 1)}$。于是

$$
\frac12\sin\frac{\pi x}{l} - \frac4\pi\sum_{k=1}^\infty\frac{(-1)^kk}{4k^2 - 1}\sin\frac{2k\pi x}{l} = f(x), \qquad x \in \left[0, \frac l2\right) \cup \left(\frac l2, l\right],
$$
在跳跃点 $x = \frac l2$ 处级数的和为 $\frac12$。

### 9.3.3. Fourier 级数的复数形式

由**欧拉公式** $\mathrm{e}^{\mathrm{i}x} = \cos x + \mathrm{i}\sin x$，

$$
\cos nx = \frac{\mathrm{e}^{\mathrm{i}nx} + \mathrm{e}^{-\mathrm{i}nx}}{2}, \qquad \sin nx = \frac{\mathrm{e}^{\mathrm{i}nx} - \mathrm{e}^{-\mathrm{i}nx}}{2\mathrm{i}},
$$
代入 Fourier 级数得 $\frac{a_0}{2} + \sum_{n=1}^\infty\left(\frac{a_n - \mathrm{i}b_n}{2}\mathrm{e}^{\mathrm{i}nx} + \frac{a_n + \mathrm{i}b_n}{2}\mathrm{e}^{-\mathrm{i}nx}\right)$。令 $c_0 = \frac{a_0}{2}$，$c_n = \frac{a_n - \mathrm{i}b_n}{2}$，$c_{-n} = \frac{a_n + \mathrm{i}b_n}{2}$（$n \ge 1$），则三个公式统一为

$$
f(x) \sim \sum_{n=-\infty}^{+\infty}c_n\mathrm{e}^{\mathrm{i}nx}, \qquad c_n = \frac{1}{2\pi}\int_{-\pi}^\pi f(x)\mathrm{e}^{-\mathrm{i}nx}\,\mathrm{d}x, \quad n = 0, \pm1, \pm2, \dots
$$

注意两处指数的符号相反：级数中是 $\mathrm{e}^{\mathrm{i}nx}$，系数中是 $\mathrm{e}^{-\mathrm{i}nx}$；对称和 $\sum_{n=-\infty}^{+\infty}$ 理解为 $\lim_{N\to\infty}\sum_{n=-N}^N$，$c_0$ 只出现一次。实函数的系数满足 $c_{-n} = \overline{c_n}$（**共轭复数**）。函数系 $\{\mathrm{e}^{\mathrm{i}nx}\}$ 在复内积 $\langle f, g\rangle = \int_{-\pi}^\pi f\bar g\,\mathrm{d}x$ 下正交，$c_n = \frac{\langle f, \mathrm{e}^{\mathrm{i}nx}\rangle}{\langle\mathrm{e}^{\mathrm{i}nx}, \mathrm{e}^{\mathrm{i}nx}\rangle}$ 仍然是"坐标等于内积"。周期为 $2l$ 时，

$$
f(x) \sim \sum_{n=-\infty}^{+\infty}c_n\mathrm{e}^{\mathrm{i}n\pi x/l}, \qquad c_n = \frac{1}{2l}\int_{-l}^lf(x)\mathrm{e}^{-\mathrm{i}n\pi x/l}\,\mathrm{d}x.
$$

复数形式便于计算部分和。把系数代入 $S_n(x) = \sum_{k=-n}^nc_k\mathrm{e}^{\mathrm{i}kx}$，令 $t = u - x$，并利用被积函数的周期性，

$$
S_n(x) = \frac{1}{2\pi}\int_{-\pi}^\pi f(x + t)D_n(t)\,\mathrm{d}t, \qquad D_n(t) = \sum_{k=-n}^n\mathrm{e}^{-\mathrm{i}kt} = \frac{\sin\left(n + \frac12\right)t}{\sin\frac t2},
$$
最后一步是几何级数求和。$D_n$ 称为 Dirichlet 核：部分和是 $f$ 与 $D_n$ 的加权平均，Dirichlet 收敛定理的证明就从这个表达式出发，分析 $n \to \infty$ 时 $D_n$ 在 $t = 0$ 附近的集中。

## 小结

| 概念 | 要点 |
|---|---|
| 一致收敛 | $\sup_I\lvert S_n - S\rvert \to 0$；判别：Cauchy 一致收敛准则、Weierstrass 判别法 $\lvert u_n(x)\rvert \le c_n$ |
| 逐项求极限 | 连续项 + 一致收敛 $\Rightarrow$ 和函数连续 |
| 逐项积分 | 连续项 + 一致收敛 $\Rightarrow$ $\int\sum = \sum\int$ |
| 逐项求导 | 级数收敛 + 导数级数一致收敛 $\Rightarrow$ $(\sum u_n)' = \sum u_n'$ |
| 收敛半径 | Abel 定理；$R = 1/\lim\lvert a_{n+1}/a_n\rvert = 1/\lim\sqrt[n]{\lvert a_n\rvert}$；端点单独判断 |
| 和函数 | $(-R,R)$ 内任意阶可导，逐项求导、积分不改变 $R$；端点收敛则单侧连续（Abel 第二定理） |
| Taylor 级数 | 收敛于 $f$ $\iff$ $R_n(x) \to 0$；导数一致有界即可；$\mathrm{e}^{-1/x^2}$ 是反例 |
| Fourier 系数 | $a_n = \frac1\pi\int_{-\pi}^\pi f\cos nx$，$b_n = \frac1\pi\int_{-\pi}^\pi f\sin nx$，$c_n = \frac{1}{2\pi}\int_{-\pi}^\pi f\mathrm{e}^{-\mathrm{i}nx}$ |
| Dirichlet 收敛定理 | 分段单调、有限个第一类间断点：连续点收敛于 $f$，间断点收敛于左右极限的平均 |

| 函数 | Maclaurin 级数 | 展开成立的范围 |
|---|---|---|
| $\mathrm{e}^x$ | $\sum_{n=0}^\infty\frac{x^n}{n!}$ | $(-\infty, +\infty)$ |
| $\sin x$ | $\sum_{k=0}^\infty\frac{(-1)^kx^{2k+1}}{(2k+1)!}$ | $(-\infty, +\infty)$ |
| $\cos x$ | $\sum_{k=0}^\infty\frac{(-1)^kx^{2k}}{(2k)!}$ | $(-\infty, +\infty)$ |
| $\ln(1 + x)$ | $\sum_{n=1}^\infty\frac{(-1)^{n-1}x^n}{n}$ | $(-1, 1]$ |
| $\frac{1}{1-x}$ | $\sum_{n=0}^\infty x^n$ | $(-1, 1)$ |
| $\arctan x$ | $\sum_{n=0}^\infty\frac{(-1)^nx^{2n+1}}{2n+1}$ | $[-1, 1]$ |
| $(1 + x)^\alpha$ | $\sum_{n=0}^\infty\binom\alpha nx^n$ | $\alpha \le -1$：$(-1,1)$；$-1 < \alpha < 0$：$(-1,1]$；$\alpha > 0$：$[-1,1]$ |

| 展开 | 系数 | 端点 $x = 0, l$ 处的和 |
|---|---|---|
| 周期 $2l$ | $a_n = \frac1l\int_{-l}^lf\cos\frac{n\pi x}{l}$，$b_n = \frac1l\int_{-l}^lf\sin\frac{n\pi x}{l}$ | — |
| 正弦级数（奇延拓） | $b_n = \frac2l\int_0^lf\sin\frac{n\pi x}{l}$ | $0$ |
| 余弦级数（偶延拓） | $a_n = \frac2l\int_0^lf\cos\frac{n\pi x}{l}$ | $f(0)$，$f(l)$ |
