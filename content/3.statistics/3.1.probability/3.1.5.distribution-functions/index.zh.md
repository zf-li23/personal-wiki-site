---
title: 概率分布函数、随机变量函数的分布
description: 分布函数的定义、与分布列和概率密度的关系、基本性质（单调、极限、右连续）与类型判断；标准正态分布函数与 3σ 原则，几何分布与指数分布的比较，混合型与奇异分布；离散型与连续型随机变量函数的分布，单调变换与一般变换的密度公式。
---

[3.1.4](/3.1.4) 分别用分布列和概率密度描述了离散型与连续型随机变量，但这两种工具各有适用范围：有些随机变量既不是离散型也不是连续型。本章引入对一切随机变量都适用的分布函数 $F(x)=\mathbb{P}(X\le x)$。它完整地刻画了随机变量的分布，使我们可以在统一的框架下比较离散与连续的分布（例如几何分布与指数分布），并通过它判断随机变量的类型。本章后半讨论随机变量函数 $Y=g(X)$ 的分布：一般的方法是先求 $Y$ 的分布函数再求导，对单调或分段单调的 $g$ 则有直接由密度求密度的公式。这些方法在 [3.1.6](/3.1.6)、[3.1.7](/3.1.7) 推广到随机向量及其函数。

## 5.1. 概率分布函数

### 5.1.1. 定义及其与分布列、概率密度的关系

我们的目标是完整刻画一个随机变量的信息。已有的工具中，分布列只适用于离散型随机变量，概率密度只适用于连续型随机变量。回忆定义随机变量时的要求：对一切 $x\in\mathbb{R}$，$\{X\le x\}$ 都是事件。于是 $\mathbb{P}(X\le x)$ 对任何随机变量都有意义。

**定义 5.1.1（分布函数）** 对随机变量 $X$，称 $x$ 的函数

$$
F(x)=\mathbb{P}(X\le x),\qquad x\in\mathbb{R}
$$
为 $X$ 的概率分布函数或累积分布函数（cumulative distribution function，CDF），简称**分布函数**。需要区分不同随机变量时记作 $F_X$。

由分布函数可以算出 $X$ 落在任何区间中的概率，例如 $\mathbb{P}(a<X\le b)=F(b)-F(a)$，$\mathbb{P}(X>a)=1-F(a)$；进一步由测度论，$F$ 决定了一切 $\mathbb{P}(X\in A)$（$A$ 为 Borel 集），所以分布函数完整地刻画了 $X$ 的分布。两个随机变量同分布，即它们的分布函数相同。

对离散型随机变量，若 $X$ 有分布列 $p_k=\mathbb{P}(X=x_k)$，$k=1,2,\dots$，则

$$
F(x)=\mathbb{P}(X\le x)=\mathbb{P}\Big(\bigcup_{j\colon x_j\le x}\{X=x_j\}\Big)=\sum_{j\colon x_j\le x}p_j.
$$
$F$ 是单调不减的阶梯函数，在每个 $x_j$ 处有跳跃 $p_j$，称 $F$ 是分布列 $\{p_j\}$ 的分布函数。例如 $\mathbb{P}(X=1)=0.2$、$\mathbb{P}(X=2)=0.5$ 时，$F(1.5)=0.2$；反过来，由 $F$ 可以求出 $\mathbb{P}(X=2)=F(2)-F(2-)=0.5$，其中 $F(x-)=\lim_{t\uparrow x}F(t)$ 是左极限。若 $\{x_k\}$ 单调递增，则 $p_k=F(x_k)-F(x_{k-1})$。用 Heaviside 函数 $H(x)=\boldsymbol{1}_{[0,\infty)}(x)$ 可以写成

$$
F(x)=\sum_{k=1}^\infty p_kH(x-x_k).\tag{5.1}
$$
若分布函数可以表示为 (5.1) 的形式，称 $F$ 是离散的。

对连续型随机变量，若 $X$ 有概率密度 $f$，则

$$
F(x)=\mathbb{P}(X\le x)=\int_{-\infty}^xf(t)\,\mathrm{d}t,\qquad x\in\mathbb{R}
$$
是连续函数，并且在 $f$ 的连续点 $x$ 处 $F'(x)=f(x)$（**微积分基本定理**），称 $F$ 是 $f$ 的分布函数。例如 $\mathrm{U}(a,b)$ 的分布函数在 $(a,b)$ 上是 $\frac{x-a}{b-a}$，在 $x\le a$ 时为 0，在 $x\ge b$ 时为 1。由分布列可以确定分布函数，反之亦然；由密度可以确定分布函数，但由分布函数只能"几乎"确定密度（在个别点上可以任意改变密度的值）。

**例 5.1.1（标准正态分布函数）** 标准正态分布的分布函数记作

$$
\Phi(x)=\int_{-\infty}^x\varphi(t)\,\mathrm{d}t=\int_{-\infty}^x\frac1{\sqrt{2\pi}}\mathrm{e}^{-t^2/2}\,\mathrm{d}t.
$$
它没有初等函数的表达式，数值由标准正态分布表给出（例如 $\Phi(0.84)=0.7995$）。由 $\varphi$ 的对称性，$\Phi(x)+\Phi(-x)=1$，即 $\Phi(-x)=1-\Phi(x)$，所以表中只需列出 $x\ge0$ 的值。对一般的正态分布 $X\sim\mathcal{N}(\mu,\sigma^2)$，作变换 $y=(x-\mu)/\sigma$，

$$
\mathbb{P}(X\le a)=\frac1{\sigma\sqrt{2\pi}}\int_{-\infty}^a\exp\Big\{-\frac{(x-\mu)^2}{2\sigma^2}\Big\}\,\mathrm{d}x=\frac1{\sqrt{2\pi}}\int_{-\infty}^{(a-\mu)/\sigma}\mathrm{e}^{-y^2/2}\,\mathrm{d}y=\Phi\Big(\frac{a-\mu}\sigma\Big).
$$
于是

$$
\begin{aligned}
\mathbb{P}(\lvert X-\mu\rvert\le\sigma)&=2\Phi(1)-1=68.27\%,\\
\mathbb{P}(\lvert X-\mu\rvert\le2\sigma)&=2\Phi(2)-1=95.45\%,\\
\mathbb{P}(\lvert X-\mu\rvert\le3\sigma)&=2\Phi(3)-1=99.73\%,\\
\mathbb{P}(\lvert X-\mu\rvert\le6\sigma)&=2\Phi(6)-1=99.9999998\%.
\end{aligned}
$$
正态随机变量几乎总是落在 $\mu\pm3\sigma$ 之内。产品质量或服务质量管理中的 $3\sigma$ 或 $6\sigma$ 原则，就是要求产品的合格率、性能的可靠性或服务的满意度达到 $\mathbb{P}(\lvert X-\mu\rvert\le3\sigma)$ 或 $\mathbb{P}(\lvert X-\mu\rvert\le6\sigma)$。

### 5.1.2. 分布函数的功能

分布函数对一切随机变量都适用，因此可以用来讨论离散与连续随机变量之间的关系。

**例 5.1.2（几何分布与指数分布）** 设 $X_1\sim\mathrm{Geo}(p)$，$\mathbb{P}(X_1=k)=p(1-p)^{k-1}$。记 $n=\lfloor x\rfloor$，则 $x\ge1$ 时

$$
F_1(x)=F_1(n)=\sum_{k=1}^np(1-p)^{k-1}=p\cdot\frac{1-(1-p)^n}{1-(1-p)}=1-(1-p)^n.
$$
设 $X_2\sim\mathrm{Exp}(\lambda)$，则 $x>0$ 时 $F_2(x)=\int_0^x\lambda\mathrm{e}^{-\lambda t}\,\mathrm{d}t=1-\mathrm{e}^{-\lambda x}$。令 $\delta=-\ln(1-p)/\lambda$，即 $\mathrm{e}^{-\lambda\delta}=1-p$，则对 $n=1,2,\dots$，$F_1(n)=F_2(n\delta)$。这相当于快速抛掷硬币，每 $\delta$ 秒抛一次，每次得到正面的概率为 $p$：$X_1$ 表示首次得到正面所需的抛掷次数，$X_1\delta$ 表示这个时刻。从分布函数可以看到，$\delta$ 很小时 $X_1\delta$ 的分布近似于 $X_2$ 的分布：指数分布是几何分布在"时间连续化"之下的极限。

![几何分布在格点 nδ 上的阶梯分布函数与指数分布函数 1 − e^(−x) 的比较，δ = 0.5 与 δ = 0.1](./plots/geometric-exponential.py)

分布函数也可以描述既非离散型、也非连续型的随机变量。

**例 5.1.3（混合型随机变量）** 抛一枚均匀硬币，正面直接得钱 0.5 元，反面则转一个幸运转盘，得钱数服从 $\mathrm{U}(0,1)$（元）。所得钱数 $X$ 的分布函数为

$$
F(x)=\begin{cases}0, & x<0,\\ x/2, & 0\le x<1/2,\\ 1/2+x/2, & 1/2\le x<1,\\ 1, & x\ge1.\end{cases}
$$
$F$ 在 $x=1/2$ 处跳跃 $1/2$（$\mathbb{P}(X=1/2)=1/2$），在其余部分连续增长。这样的随机变量既没有分布列，也没有密度，只能用分布函数描述。

### 5.1.3. 分布函数的性质

**定理 5.1.1（分布函数的性质）** 随机变量 $X$ 的分布函数 $F$ 满足：

1. $F$ 单调非降；
2. $F(-\infty)=\lim_{x\to-\infty}F(x)=0$，$F(\infty)=\lim_{x\to\infty}F(x)=1$；
3. $F$ 右连续，即对每个 $x$，$\lim_{t\downarrow x}F(t)=F(x)$。

**证明** (1) 对任意 $x<y$，$F(y)-F(x)=\mathbb{P}(x<X\le y)\ge0$。

(2) 由单调性，只需沿整数取极限。事件 $\{X\le n\}$ 单调递增，并为 $\{X<\infty\}=\Omega$，由概率的连续性（[3.1.2](/3.1.2) 定理 2.2.1），

$$
F(\infty)=\lim_{n\to\infty}\mathbb{P}(X\le n)=\mathbb{P}\Big(\bigcup_{n=1}^\infty\{X\le n\}\Big)=\mathbb{P}(X<\infty)=1.
$$
同理，$\{X\le-n\}$ 单调递减，交为 $\varnothing$，所以 $F(-\infty)=0$。

(3) 由单调性，只需沿 $x+n^{-1}$ 取极限。事件 $\{X\le x+n^{-1}\}$ 单调递减，交为 $\{X\le x\}$，所以

$$
\lim_{n\to\infty}F(x+n^{-1})=\mathbb{P}\Big(\bigcap_{n=1}^\infty\{X\le x+n^{-1}\}\Big)=\mathbb{P}(X\le x)=F(x).\qquad\square
$$

同样的论证给出左极限 $F(x-)=\mathbb{P}(X<x)$，因此 $\mathbb{P}(X=x)=F(x)-F(x-)$ 是 $F$ 在 $x$ 处的跳跃。反过来可以证明：任何满足 (1)–(3) 的函数都是某个随机变量的分布函数，所以这三条性质刻画了分布函数。由于单调函数的间断点至多可列，任何随机变量取单个值的正概率点至多可列个。

### 5.1.4. 由分布函数判断随机变量的类型

**定理 5.1.2** 如果对一切 $x\in\mathbb{R}$ 都有 $\mathbb{P}(X=x)=0$，则分布函数 $F(x)=\mathbb{P}(X\le x)$ 是连续的。

**证明** 由概率的连续性，

$$
0=\mathbb{P}(X=x)=\mathbb{P}\Big(\bigcap_{m=1}^\infty\Big\{x-\frac1m<X\le x\Big\}\Big)=\lim_{m\to\infty}\big[F(x)-F(x-m^{-1})\big]=F(x)-F(x-),
$$
即 $F$ 左连续。又 $F$ 右连续，因此 $F$ 连续。 $\square$

由此，若 $F$ 不连续，则 $X$ 必非连续型随机变量（连续型随机变量取每个值的概率都是零）。反过来，当 $F$ 连续且几乎处处可导时，可以由导数得到密度。

**定理 5.1.3** 设 $X$ 的分布函数 $F$ 连续，数集 $A$ 中任何两点之间的距离都大于某个正数 $\delta$。如果在 $A^{\mathsf c}$ 上导数 $F'(x)$ 存在且连续，则

$$
f(x)=\begin{cases}F'(x), & x\notin A,\\ 0, & x\in A\end{cases}
$$
是 $X$ 的密度函数。

**证明** 对任意 $a<b$，区间 $(a,b)$ 中只有 $A$ 的有限个点（相邻两点距离大于 $\delta$），设为 $a_1<\cdots<a_k$，记 $a_0=a$，$a_{k+1}=b$。$F$ 在每个 $[a_j,a_{j+1}]$ 上连续，在其内部连续可导，由**微积分基本定理**（Newton–Leibniz 公式；端点处利用 $F$ 的连续性取极限），

$$
\mathbb{P}(a<X\le b)=\sum_{j=0}^k\big[F(a_{j+1})-F(a_j)\big]=\sum_{j=0}^k\int_{a_j}^{a_{j+1}}f(t)\,\mathrm{d}t=\int_a^bf(t)\,\mathrm{d}t.
$$
故 $f$ 是 $X$ 的概率密度。 $\square$

**注 5.1.1** 定理 5.1.3 中 $F$ 连续的条件是至关重要的。若 $X\sim\mathrm{Bin}(n,p)$，除去有限个点外 $F'(x)=0$，但 $X$ 没有密度。另一方面，$F$ 连续并不能保证 $X$ 是连续型随机变量，下面的例子说明了这一点，也说明定理中对数集 $A$ 的限制是必要的。

**例 5.1.4（Cantor 分布）** Cantor 集 $C$ 是从 $[0,1]$ 中去掉中间三分之一的开区间 $(1/3,2/3)$，再从剩下的每个区间中去掉中间三分之一，如此无限进行下去所剩的集合。定义 $F(x)=0$（$x\le0$），$F(x)=1$（$x\ge1$），在第一步去掉的区间 $[1/3,2/3]$ 上 $F=1/2$，在第二步去掉的区间 $[1/9,2/9]$、$[7/9,8/9]$ 上分别取 $1/4$、$3/4$，在第 $n$ 步去掉的 $2^{n-1}$ 个区间上从左到右依次取 $\frac1{2^n},\frac3{2^n},\dots,\frac{2^n-1}{2^n}$。可以证明 $F$ 在全体实数上有定义、单调不减、连续，$F(-\infty)=0$，$F(\infty)=1$，所以它是一个分布函数，称为 Cantor 函数（Lebesgue 奇异函数）。在 $C$ 以外的每一点 $F'(x)=0$，而 $C$ 的总长度为 $1-\sum_{n\ge1}2^{n-1}/3^n=0$，所以 $F'=0$ 几乎处处成立。若 $X$ 有密度 $f$，则 $f=F'=0$ 几乎处处，$\int f=0\ne1$，矛盾。所以服从 Cantor 分布的随机变量取每个值的概率都是零，却不是连续型随机变量。

连续、不恒为常数、几乎处处可导且导数几乎处处为零的分布函数称为奇异的（singular）。可以证明，任何分布函数都可以唯一地分解为离散的、绝对连续的（即有密度的）与奇异的三部分的凸组合（Lebesgue 分解）；初等概率论中只遇到前两部分及其混合。

![四类分布函数：离散型（阶梯函数）、连续型（U(1, 4) 与另一个密度的积分）、混合型（例 5.1.3）以及奇异的 Cantor 函数](./plots/cdf-types.py)

## 5.2. 随机变量函数的分布

设 $X$ 是随机变量，$g$ 是可测函数，则 $Y=g(X)$ 也是随机变量（[3.1.3](/3.1.3) 定理 3.2.2）。已知 $X$ 的分布，如何求 $Y$ 的分布？有两条途径：一般方法是由 $X$ 的分布函数求 $Y$ 的分布函数，再由分布函数得到 $Y$ 的分布列或密度；特殊情形（如 $g$ 单调）下可以由 $X$ 的分布列或密度直接得到 $Y$ 的分布列或密度。

### 5.2.1. 离散型随机变量的函数

若 $X$ 是离散型随机变量，$Y=g(X)$ 也是离散的，只需对 $Y$ 的每一个可能值 $y$ 计算 $\mathbb{P}(Y=y)=\sum_{k\colon g(x_k)=y}\mathbb{P}(X=x_k)$：几个不同的 $x_k$ 可能映到同一个 $y$。

**例 5.2.1** 设 $X$ 的概率分布为

$$
\begin{array}{c|ccccc}
X & -2 & -1 & 0 & 1 & 3\\
\hline
\mathbb{P} & 0.1 & 0.2 & 0.3 & 0.2 & 0.2
\end{array}
$$
求 $Y=X^2$ 的分布。$Y$ 可能的取值为 $0,1,4,9$，且 $\mathbb{P}(Y=0)=\mathbb{P}(X=0)=0.3$，$\mathbb{P}(Y=1)=\mathbb{P}(X=-1)+\mathbb{P}(X=1)=0.4$，$\mathbb{P}(Y=4)=\mathbb{P}(X=-2)=0.1$，$\mathbb{P}(Y=9)=\mathbb{P}(X=3)=0.2$。于是 $Y$ 的分布列为

$$
\begin{array}{c|cccc}
Y & 0 & 1 & 4 & 9\\
\hline
\mathbb{P} & 0.3 & 0.4 & 0.1 & 0.2
\end{array}
$$

### 5.2.2. 连续型随机变量的函数：分布函数法

设 $X$ 有密度 $f_X$，考察 $Y=g(X)$ 的分布。一般方法分两步：

1. 求 $Y$ 的分布函数 $F_Y(y)=\mathbb{P}(Y\le y)=\mathbb{P}(g(X)\le y)=\int_{\{x\colon g(x)\le y\}}f_X(x)\,\mathrm{d}x$；
2. 求导得到 $f_Y(y)=\dfrac{\mathrm{d}F_Y(y)}{\mathrm{d}y}$（用定理 5.1.3 验证它确是密度）。

**例 5.2.2（标准化）** 设 $X\sim\mathcal{N}(\mu,\sigma^2)$，则 $Y=(X-\mu)/\sigma\sim\mathcal{N}(0,1)$。事实上，令 $t=(x-\mu)/\sigma$，

$$
\mathbb{P}(Y\le y)=\mathbb{P}(X\le\mu+\sigma y)=\int_{-\infty}^{\mu+\sigma y}\frac1{\sigma\sqrt{2\pi}}\exp\Big\{-\frac{(x-\mu)^2}{2\sigma^2}\Big\}\,\mathrm{d}x=\int_{-\infty}^y\varphi(t)\,\mathrm{d}t=\Phi(y).
$$

**例 5.2.3** 设 $X\sim\mathcal{N}(0,1)$，求 $Y=X^2$ 的概率密度。由于 $Y\ge0$，$y\le0$ 时 $F_Y(y)=0$；对 $y>0$，

$$
F_Y(y)=\mathbb{P}(-\sqrt y\le X\le\sqrt y)=\Phi(\sqrt y)-\Phi(-\sqrt y)=2\Phi(\sqrt y)-1
$$
是连续函数，在 $y>0$ 时连续可导。由定理 5.1.3，$Y$ 的密度为

$$
f_Y(y)=F_Y'(y)=2\varphi(\sqrt y)\frac1{2\sqrt y}=\frac1{\sqrt{2\pi y}}\mathrm{e}^{-y/2},\qquad y>0,
$$
与 [3.1.4](/3.1.4) 的密度比较（$\Gamma(1/2)=\sqrt\pi$），即 $Y\sim\Gamma(1/2,1/2)=\chi^2_1$。

### 5.2.3. 线性变换与单调变换

有些特殊情形可以从 $f_X$ 直接得到 $f_Y$，无需计算分布函数。

**定理 5.2.1（线性变换）** 设 $X$ 有密度 $f_X$，$a\ne0$，$Y=aX+b$，则

$$
f_Y(y)=\frac1{\lvert a\rvert}f_X\Big(\frac{y-b}a\Big).
$$

**证明** 若 $a>0$，$F_Y(y)=\mathbb{P}(X\le(y-b)/a)=F_X((y-b)/a)$；若 $a<0$，$F_Y(y)=\mathbb{P}(X\ge(y-b)/a)=1-F_X((y-b)/a)$（$X$ 取单点的概率为零）。两种情形都写成积分后作变量替换即得。 $\square$

直观上，$aX$ 的密度把 $f_X$ 的图形沿横轴拉伸 $\lvert a\rvert$ 倍（$a<0$ 时再左右翻转）并把高度压缩为 $1/\lvert a\rvert$，使总面积仍为 1；加上 $b$ 再平移。由定理 5.2.1 可以重新验证例 5.2.2，并得到：若 $X\sim\mathcal{N}(\mu,\sigma^2)$，则 $aX+b\sim\mathcal{N}(a\mu+b,a^2\sigma^2)$；若 $X\sim\mathrm{Exp}(\lambda)$、$c>0$，则 $cX\sim\mathrm{Exp}(\lambda/c)$。

**定理 5.2.2（严格单调变换）** 设 $X$ 有密度 $f_X$，$g$ 在 $X$ 的取值区间 $I$ 上严格单调、连续可导，$h$ 是 $g$ 的反函数，则 $Y=g(X)$ 的密度为

$$
f_Y(y)=f_X\big(h(y)\big)\,\lvert h'(y)\rvert,\qquad y\in g(I),
$$
在 $g(I)$ 以外 $f_Y(y)=0$。

**证明** 设 $g$ 严格递增，则 $h$ 也严格递增，$F_Y(y)=\mathbb{P}(X\le h(y))=F_X(h(y))$，求导得 $f_Y(y)=f_X(h(y))h'(y)$。$g$ 严格递减时 $F_Y(y)=1-F_X(h(y))$，求导得 $f_Y(y)=-f_X(h(y))h'(y)=f_X(h(y))\lvert h'(y)\rvert$。 $\square$

直观上，事件 $\{x<X\le x+\delta\}=\{g(x)<Y\le g(x+\delta)\}$，后者近似为长度为 $\delta\lvert g'(x)\rvert$ 的区间，因此 $\delta f_X(x)\approx\delta f_Y(g(x))\lvert g'(x)\rvert$，即密度按局部的伸缩比例 $\lvert g'(x)\rvert$ 改变。

### 5.2.4. 一般变换

若 $g$ 不是单调的，一个 $y$ 可能有几个原像（"几对一"）：解方程 $g(x)=y$，看它有几个解，每个解对应一个反函数分支，各分支的贡献相加。例如 $g(x)=x^2$，$y>0$ 有两个原像 $x_1=\sqrt y$、$x_2=-\sqrt y$，于是

$$
f_Y(y)=f_X(x_1)\Big\lvert\frac{\mathrm{d}x_1}{\mathrm{d}y}\Big\rvert+f_X(x_2)\Big\lvert\frac{\mathrm{d}x_2}{\mathrm{d}y}\Big\rvert=\frac1{2\sqrt y}\big[f_X(\sqrt y)+f_X(-\sqrt y)\big],
$$
$X\sim\mathcal{N}(0,1)$ 时就是例 5.2.3 的结果。一般地：

**定理 5.2.3** 设 $X$ 有概率密度 $f$，$Y=g(X)$，$D\subset\mathbb{R}$ 是开区间，$\mathbb{P}(Y\in D)=1$。如果

1. 对 $y\in D$，$\{Y=y\}=\bigcup_{i=1}^n\{X=h_i(y)\}$；
2. 每个 $h_i$ 是从 $D$ 到其值域 $D_i$ 的可逆映射，在 $D$ 内有连续的导数；
3. $D_1,\dots,D_n$ 互不相交，

则 $Y$ 的密度函数为

$$
f_Y(y)=\begin{cases}\displaystyle\sum_{i=1}^nf\big(h_i(y)\big)\,\lvert h_i'(y)\rvert, & y\in D,\\ 0, & y\notin D.\end{cases}
$$

**证明** 由条件，$\mathbb{P}(X\in\bigcup_iD_i)=\mathbb{P}(Y\in D)=1$。对 $D$ 中的区间 $(a,b]$，$\{a<Y\le b\}$ 与 $\bigcup_i\{X\in h_i((a,b])\}$ 只相差概率为零的集合，后者是不相容的并。$h_i$ 连续可逆，因而严格单调，在每个 $D_i$ 上对积分作变量替换 $x=h_i(y)$，

$$
\mathbb{P}(a<Y\le b)=\sum_{i=1}^n\int_{h_i((a,b])}f(x)\,\mathrm{d}x=\sum_{i=1}^n\int_a^bf\big(h_i(y)\big)\lvert h_i'(y)\rvert\,\mathrm{d}y.\qquad\square
$$

**例 5.2.4** 设 $r$ 是正常数，$X\sim\mathrm{U}(0,2\pi)$，求 $Y=r\cos X$ 的概率密度。

方法一（定理 5.2.3）：取 $D=(-r,r)$，则 $\mathbb{P}(Y\in D)=1$。对 $y\in D$，

$$
\{Y=y\}=\{\cos X=y/r,\ X\in(0,\pi)\}\cup\{\cos(2\pi-X)=y/r,\ X\in(\pi,2\pi)\}=\{X=\arccos(y/r)\}\cup\{X=2\pi-\arccos(y/r)\}.
$$
$h_1(y)=\arccos(y/r)\colon D\to(0,\pi)$ 与 $h_2(y)=2\pi-\arccos(y/r)\colon D\to(\pi,2\pi)$ 都是可逆、连续可微的函数，值域不相交。利用 $f_X(x)=\frac1{2\pi}$（$x\in(0,2\pi)$）和 $[\arccos x]'=-\frac1{\sqrt{1-x^2}}$，

$$
f_Y(y)=\frac1{2\pi}\Big\lvert\frac{\mathrm{d}}{\mathrm{d}y}\arccos\frac yr\Big\rvert+\frac1{2\pi}\Big\lvert\frac{\mathrm{d}}{\mathrm{d}y}\Big[2\pi-\arccos\frac yr\Big]\Big\rvert=\frac1{\pi\sqrt{r^2-y^2}},\qquad y\in(-r,r).
$$

方法二（分布函数法）：对 $y\in(-r,r)$，$\{x\in(0,2\pi)\colon\cos x\le y/r\}=[\arccos(y/r),\,2\pi-\arccos(y/r)]$，所以

$$
\mathbb{P}(Y\le y)=\int_{\{x\colon\cos x\le y/r\}}\frac1{2\pi}\,\mathrm{d}x=\frac1{2\pi}\big\{2\pi-2\arccos(y/r)\big\},
$$
求导即得同样的结果。这个分布称为反正弦分布（arcsine distribution）：密度在 $\pm r$ 附近趋于无穷，因为匀速转动的点的投影在两端停留得最久。

![左：y = r cos x 在 (0, 2π) 上，每个 y ∈ (−r, r) 有两个原像 h1(y)、h2(y)；右：Y = r cos X 的 10 万次模拟的直方图与密度 1/(π√(r² − y²))](./plots/cosine-transform.py)

解题时不限定用哪种方法，只要能解决问题即可。分布函数法总是可行的；直接由密度求密度的公式更快捷，但要正确找出所有的反函数分支。另一个常用的技巧是识别密度的"核心部分"：若求出的密度正比于某个已知分布的密度（如例 5.2.3 中的 $y^{-1/2}\mathrm{e}^{-y/2}$），由归一化即可确定常数和分布。

## 小结

| 内容 | 要点 |
|---|---|
| 分布函数 | $F(x)=\mathbb{P}(X\le x)$ 对一切随机变量适用；单调非降、$F(-\infty)=0$、$F(\infty)=1$、右连续；跳跃 $F(x)-F(x-)=\mathbb{P}(X=x)$ |
| 与分布列、密度的关系 | 离散型：$F(x)=\sum_{x_j\le x}p_j$（阶梯函数）；连续型：$F(x)=\int_{-\infty}^xf(t)\,\mathrm{d}t$，$f=F'$（在连续点）；还有混合型与奇异型 |
| 正态分布函数 | $\Phi(-x)=1-\Phi(x)$，$\mathbb{P}(X\le a)=\Phi((a-\mu)/\sigma)$，$3\sigma$ 原则 |
| 随机变量函数的分布 | 离散：对每个 $y$ 把原像的概率相加；连续：分布函数法（先求 $F_Y$ 再求导），或公式 $f_Y(y)=\sum_if_X(h_i(y))\lvert h_i'(y)\rvert$ |
