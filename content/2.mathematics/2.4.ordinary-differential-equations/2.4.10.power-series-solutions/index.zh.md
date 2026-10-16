---
title: 幂级数解法
---

变系数线性方程一般不能用初等函数求解。物理中最重要的一批变系数方程（Legendre 方程、Bessel 方程、Hermite 方程、Airy 方程等）来自用分离变量法解偏微分方程：在球坐标中分离 Laplace 方程得到 Legendre 方程，在柱坐标或极坐标中分离 Laplace 方程、波动方程、热方程得到 Bessel 方程。它们的解定义了新的"特殊函数"，最直接的研究方法是把解写成**幂级数**。

本章先讨论系数在一点附近可展开为幂级数（常点）的情形：解也是幂级数，系数由递推关系确定。然后讨论系数有"弱"奇性的正则奇点，Frobenius 方法给出形如 $x^\rho\sum a_kx^k$ 的解，必要时带有对数项；上一章的 Euler 方程是它的原型。最后用这两种方法研究 Legendre 多项式与 Bessel 函数，给出偏微分方程（[2.5](/2.5)）中分离变量所需的基本性质：正交性、递推公式、零点与渐近行为。这些函数的零点与正交性在 Sturm–Liouville 理论（[2.4.12](/2.4.12)）中得到统一的解释。

## 10.1. 常点处的幂级数解

### 10.1.1. 常点与 Cauchy 定理

考虑二阶齐次线性方程

$$
y''+p(x)y'+q(x)y=0.\tag{10.1}
$$

**定义 10.1.1** 若 $p(x)$、$q(x)$ 都能在 $x_0$ 的某个邻域内展开为收敛的幂级数 $\sum_kc_k(x-x_0)^k$，则称 $x_0$ 是方程 (10.1) 的**常点**；否则称 $x_0$ 是方程的奇点。

例如有理函数系数的方程，$x_0$ 是常点当且仅当它不是 $p$、$q$ 的分母（约分后）的零点。

**定理 10.1.1（Cauchy）** 设 $p$、$q$ 在 $\lvert x-x_0\rvert<R$ 内可展开为收敛的幂级数，则方程 (10.1) 的每个解在 $\lvert x-x_0\rvert<R$ 内都可展开为收敛的幂级数 $y=\sum_{k=0}^\infty a_k(x-x_0)^k$，其中 $a_0=y(x_0)$、$a_1=y'(x_0)$ 任意，其余系数由代入方程比较系数所得的递推关系唯一确定。

**证明** （思路）不妨 $x_0=0$。代入 $y=\sum a_kx^k$，由幂级数的乘法（**Cauchy 乘积**）比较 $x^k$ 的系数得

$$
(k+2)(k+1)a_{k+2}=-\sum_{j=0}^{k}\big((j+1)a_{j+1}p_{k-j}+a_jq_{k-j}\big),
$$
所以 $a_0,a_1$ 确定后所有 $a_k$ 被唯一确定，问题只在于所得级数是否收敛。任取 $0<r<R$，级数 $\sum p_kr^k$、$\sum q_kr^k$ 收敛，于是 $\lvert p_k\rvert,\lvert q_k\rvert\le M/r^k$。用 $M/r^k$ 代替 $\lvert p_k\rvert,\lvert q_k\rvert$、用 $\lvert a_0\rvert,\lvert a_1\rvert$ 作初值，得到一个比较方程，它的解可以显式写出，其幂级数系数 $A_k\ge\lvert a_k\rvert$ 且收敛半径为 $r$（强级数法）。由比较判别法 $\sum a_kx^k$ 在 $\lvert x\rvert<r$ 内收敛；$r<R$ 任意。收敛的幂级数可逐项求导，所以它确实是解；由唯一性，满足同样初值的解就是它。 $\square$

收敛半径至少是从 $x_0$ 到 $p$、$q$ 的最近（复）奇点的距离。例如 $y''+\frac{1}{1+x^2}y=0$ 的系数在整个实轴上光滑，但在 $x_0=0$ 处的幂级数解只能保证在 $\lvert x\rvert<1$ 内收敛，因为 $\frac1{1+x^2}$ 在 $\pm\mathrm{i}$ 处有奇点。这是复变函数（[2.3](/2.3)）的典型现象。

**算法 10.1.1（幂级数解法）** 求方程 (10.1) 在常点 $x_0$ 附近的解：

1. 设 $y=\sum_{k\ge0}a_k(x-x_0)^k$，把系数也展开为 $x-x_0$ 的幂级数（多项式系数时通常把方程乘以公分母，直接用多项式系数）；
2. 代入方程，合并同次幂，令各次幂的系数为零，得到递推关系；
3. 分别取 $(a_0,a_1)=(1,0)$ 与 $(0,1)$，得到两个线性无关的解（它们在 $x_0$ 处的 Wronski 行列式为 1）。

**例 10.1.1** 解 Airy 方程 $y''=xy$。设 $y=\sum a_kx^k$，$\sum_k(k+2)(k+1)a_{k+2}x^k=\sum_ka_{k-1}x^k$，所以 $a_2=0$，

$$
a_{k+2}=\frac{a_{k-1}}{(k+2)(k+1)}\qquad(k\ge1).
$$
系数按模 3 分成三组：$a_2=a_5=a_8=\cdots=0$，其余两组分别由 $a_0$、$a_1$ 决定。两个基本解为

$$
y_1=1+\frac{x^3}{3\cdot2}+\frac{x^6}{6\cdot5\cdot3\cdot2}+\cdots,\qquad y_2=x+\frac{x^4}{4\cdot3}+\frac{x^7}{7\cdot6\cdot4\cdot3}+\cdots,
$$
系数为整数的乘积分之一，增长极快，两个级数在整个 $\mathbb{R}$ 上收敛（与定理 10.1.1 一致：系数 $x$ 是整函数）。Airy 方程描述了光学中焦散线附近的光强与量子力学中转折点附近的波函数：$x<0$ 时解振荡，$x>0$ 时解指数增长或衰减。

## 10.2. Legendre 方程与 Legendre 多项式

### 10.2.1. Legendre 方程的级数解

**定义 10.2.1（Legendre 方程）** 称

$$
(1-x^2)y''-2xy'+\nu(\nu+1)y=0\tag{10.2}
$$
为 $\nu$ 阶 **Legendre 方程**（$\nu$ 为常数）。

在球坐标中对 Laplace 方程 $\Delta u=0$ 分离变量，并令 $x=\cos\theta$，就得到这个方程（轴对称情形）。$x=\pm1$ 是它的奇点，$x=0$ 是常点，由定理 10.1.1 幂级数解在 $\lvert x\rvert<1$ 内收敛。代入 $y=\sum a_kx^k$：

$$
\sum_k\Big((k+2)(k+1)a_{k+2}-\big(k(k-1)+2k-\nu(\nu+1)\big)a_k\Big)x^k=0,
$$
即

$$
a_{k+2}=\frac{(k-\nu)(k+\nu+1)}{(k+2)(k+1)}a_k.\tag{10.3}
$$
取 $(a_0,a_1)=(1,0)$ 得偶函数解 $y_1=1-\frac{\nu(\nu+1)}{2!}x^2+\frac{(\nu-2)\nu(\nu+1)(\nu+3)}{4!}x^4-\cdots$，取 $(0,1)$ 得奇函数解 $y_2=x-\frac{(\nu-1)(\nu+2)}{3!}x^3+\cdots$。

当 $\nu=n$ 是非负整数时，(10.3) 中 $k=n$ 那一项使 $a_{n+2}=0$，于是 $y_1$、$y_2$ 中与 $n$ 同奇偶的一个在 $x^n$ 处中断，成为 $n$ 次多项式。

### 10.2.2. Legendre 多项式

**定义 10.2.2（Legendre 多项式）** $n$ 阶 Legendre 方程的 $n$ 次多项式解中满足 $P_n(1)=1$ 的那一个称为 $n$ 次 **Legendre 多项式**，记作 $P_n(x)$。

前几个是

$$
P_0=1,\quad P_1=x,\quad P_2=\frac{3x^2-1}{2},\quad P_3=\frac{5x^3-3x}{2},\quad P_4=\frac{35x^4-30x^2+3}{8},\quad P_5=\frac{63x^5-70x^3+15x}{8}.
$$
它们也可以由对 $1,x,x^2,\dots$ 在 $[-1,1]$ 上做 Gram–Schmidt 正交化得到（[2.1.12](/2.1.12)），这一点由下面的正交性解释。

**定理 10.2.1（Rodrigues 公式）**

$$
P_n(x)=\frac{1}{2^nn!}\frac{\mathrm{d}^n}{\mathrm{d}x^n}(x^2-1)^n.
$$

**证明** 记 $u=(x^2-1)^n$，则 $(x^2-1)u'=2nxu$。对两边求 $n+1$ 阶导数，由 Leibniz 公式

$$
(x^2-1)u^{(n+2)}+2(n+1)xu^{(n+1)}+n(n+1)u^{(n)}=2nxu^{(n+1)}+2n(n+1)u^{(n)},
$$
整理得 $(1-x^2)v''-2xv'+n(n+1)v=0$，$v=u^{(n)}$。所以 $v$ 是 $n$ 次多项式解。$u=(x-1)^n(x+1)^n$，由 Leibniz 公式 $v(1)=n!\,2^n$（只有 $(x-1)^n$ 求 $n$ 次导数的那一项不含因子 $x-1$），除以 $2^nn!$ 后在 $x=1$ 处为 1。 $\square$

**定理 10.2.2** Legendre 多项式有以下性质。

1. $P_n(-x)=(-1)^nP_n(x)$，$P_n(1)=1$，$P_n(-1)=(-1)^n$，$\lvert P_n(x)\rvert\le1$（$\lvert x\rvert\le1$）；
2. （正交性）$\displaystyle\int_{-1}^1P_m(x)P_n(x)\,\mathrm{d}x=\begin{cases}0,&m\ne n,\\\dfrac{2}{2n+1},&m=n;\end{cases}$
3. （母函数）对 $\lvert x\rvert\le1$、$\lvert t\rvert<1$，$\displaystyle\frac{1}{\sqrt{1-2xt+t^2}}=\sum_{n=0}^\infty P_n(x)t^n$；
4. （递推公式）$(n+1)P_{n+1}(x)=(2n+1)xP_n(x)-nP_{n-1}(x)$，$(x^2-1)P_n'(x)=n\big(xP_n(x)-P_{n-1}(x)\big)$；
5. $P_n$ 在 $(-1,1)$ 内恰有 $n$ 个互不相同的零点。

**证明** 2 的第一部分：Legendre 方程可以写成自伴形式 $\big((1-x^2)y'\big)'+\nu(\nu+1)y=0$。于是

$$
\big((1-x^2)P_n'\big)'P_m-\big((1-x^2)P_m'\big)'P_n=\big(m(m+1)-n(n+1)\big)P_mP_n,
$$
左边等于 $\big((1-x^2)(P_n'P_m-P_m'P_n)\big)'$。在 $[-1,1]$ 上积分，左边的边界项含因子 $1-x^2$，为零；$m\ne n$ 时 $m(m+1)\ne n(n+1)$，所以 $\int_{-1}^1P_mP_n=0$。$m=n$ 时由 Rodrigues 公式分部积分 $n$ 次得 $\int_{-1}^1P_n^2=\frac{(2n)!}{2^{2n}(n!)^2}\int_{-1}^1(1-x^2)^n\,\mathrm{d}x=\frac{2}{2n+1}$。

5：$P_n$ 与所有次数小于 $n$ 的多项式正交（它们是 $P_0,\dots,P_{n-1}$ 的线性组合）。设 $P_n$ 在 $(-1,1)$ 内变号的点只有 $x_1,\dots,x_k$，$k<n$，则 $P_n(x)\prod_i(x-x_i)$ 在 $(-1,1)$ 内不变号且不恒为零，积分非零，与正交性矛盾。所以至少有 $n$ 个变号点，而 $n$ 次多项式至多 $n$ 个零点。

1 由定义与 (10.3) 的奇偶性得到（$\lvert P_n\rvert\le1$ 可由 Laplace 积分表示 $P_n(x)=\frac1\pi\int_0^\pi(x+\sqrt{x^2-1}\cos\varphi)^n\,\mathrm{d}\varphi$ 得到，此处从略）；3、4 可由母函数对 $t$、$x$ 求导比较系数得到，从略。 $\square$

所以 $\{P_n\}$ 是 $[-1,1]$ 上的**正交函数系**，并且是完备的：对 $[-1,1]$ 上分段光滑的函数 $f$，Legendre 级数

$$
f(x)\sim\sum_{n=0}^\infty c_nP_n(x),\qquad c_n=\frac{2n+1}{2}\int_{-1}^1f(x)P_n(x)\,\mathrm{d}x
$$
在 $f$ 的连续点收敛到 $f(x)$，在跳跃点收敛到左右极限的平均值（陈述，证明从略）。母函数在静电学中有直接的意义：$\frac{1}{\lvert\boldsymbol{r}-\boldsymbol{r}'\rvert}=\sum_n\frac{r'^n}{r^{n+1}}P_n(\cos\gamma)$（$r'<r$，$\gamma$ 为两个向量的夹角），这是多极展开。

![Legendre 多项式 P_0, …, P_5 在 [-1, 1] 上的图像：P_n 恰有 n 个零点，P_n(1) = 1，|P_n| ≤ 1，奇偶性与 n 相同](./plots/legendre-polynomials.py)

### 10.2.3. 有界解与第二类 Legendre 函数

$\nu=n$ 时另一个级数解不中断，记适当归一化后为 $Q_n(x)$（第二类 Legendre 函数）。例如

$$
Q_0(x)=\frac12\ln\frac{1+x}{1-x},\qquad Q_1(x)=\frac x2\ln\frac{1+x}{1-x}-1,
$$
它们在 $x\to\pm1$ 时对数地趋于无穷。一般地有下面的事实（陈述）：Legendre 方程在 $[-1,1]$ 上有不恒为零的有界解，当且仅当 $\nu(\nu+1)=n(n+1)$（$n$ 为非负整数），此时有界解是 $P_n$ 的常数倍。在球坐标中，$x=\cos\theta=\pm1$ 对应南北极，物理上要求解在两极有界，这就把分离常数限定为 $n(n+1)$。这是 [2.4.12](/2.4.12) 中奇异 Sturm–Liouville 问题的一个例子：特征值为 $n(n+1)$，特征函数为 $P_n$。

不轴对称时，球坐标的分离变量给出连带 Legendre 方程

$$
(1-x^2)y''-2xy'+\Big(n(n+1)-\frac{m^2}{1-x^2}\Big)y=0,
$$
它的有界解是连带 Legendre 函数 $P_n^m(x)=(1-x^2)^{m/2}\dfrac{\mathrm{d}^m}{\mathrm{d}x^m}P_n(x)$（$0\le m\le n$）。$P_n^m(\cos\theta)\mathrm{e}^{\mathrm{i}m\varphi}$ 就是球面调和函数。

## 10.3. 正则奇点与 Frobenius 方法

### 10.3.1. 正则奇点与指标方程

在奇点附近解一般不是幂级数。最简单的例子是 Euler 方程 $x^2y''+axy'+by=0$：$x=0$ 是奇点，解是 $x^\rho$ 或 $x^\rho\ln x$，$\rho$ 是 $\rho(\rho-1)+a\rho+b=0$ 的根（定理 9.5.1）。如果奇性不比 Euler 方程更强，就可以期望解形如"$x^\rho$ 乘以幂级数"。

**定义 10.3.1** 设 $x_0$ 是方程 (10.1) 的奇点。若 $(x-x_0)p(x)$ 与 $(x-x_0)^2q(x)$ 都能在 $x_0$ 的某邻域内展开为收敛的幂级数，则称 $x_0$ 为**正则奇点**，否则称为非正则奇点。

例如 $x=0$ 是 Euler 方程与 Bessel 方程 $x^2y''+xy'+(x^2-\nu^2)y=0$ 的正则奇点，$x=\pm1$ 是 Legendre 方程的正则奇点；$x=0$ 是 $x^3y''+y=0$ 的非正则奇点。

设 $x_0=0$ 是正则奇点，把方程乘以 $x^2$ 写成

$$
x^2y''+xP(x)y'+Q(x)y=0,\qquad P(x)=\sum_{k\ge0}p_kx^k,\quad Q(x)=\sum_{k\ge0}q_kx^k,\tag{10.4}
$$
两个级数在 $\lvert x\rvert<R$ 内收敛。在 $x>0$ 上代入 $y=x^\rho\sum_{k\ge0}a_kx^k$（$a_0\ne0$），比较 $x^{\rho+k}$ 的系数：

$$
F(\rho+k)a_k=-\sum_{j=0}^{k-1}\big((\rho+j)p_{k-j}+q_{k-j}\big)a_j,\qquad F(\rho)=\rho(\rho-1)+p_0\rho+q_0.\tag{10.5}
$$
$k=0$ 时得 $F(\rho)a_0=0$，所以 $\rho$ 必须是 $F$ 的根。

**定义 10.3.2** 方程 $F(\rho)=\rho(\rho-1)+p_0\rho+q_0=0$ 称为方程 (10.4) 在正则奇点 $x=0$ 处的**指标方程**，它的根称为指标。

$p_0=\lim_{x\to0}xp(x)$，$q_0=\lim_{x\to0}x^2q(x)$：指标方程就是把系数换成最低阶近似后所得 Euler 方程的特征方程。

### 10.3.2. Frobenius 定理

**定理 10.3.1（Frobenius）** 设 $x=0$ 是方程 (10.4) 的正则奇点，$P$、$Q$ 的级数在 $\lvert x\rvert<R$ 内收敛，指标为 $\rho_1,\rho_2$，$\operatorname{Re}\rho_1\ge\operatorname{Re}\rho_2$。则在 $0<x<R$ 上：

1. 方程有解 $y_1=x^{\rho_1}\sum_{k\ge0}a_kx^k$，$a_0=1$；
2. 若 $\rho_1-\rho_2\notin\mathbb{Z}$，另有线性无关解 $y_2=x^{\rho_2}\sum_{k\ge0}b_kx^k$，$b_0=1$；
3. 若 $\rho_1=\rho_2$，另有线性无关解 $y_2=y_1\ln x+x^{\rho_1}\sum_{k\ge1}b_kx^k$；
4. 若 $\rho_1-\rho_2=N$ 为正整数，另有线性无关解 $y_2=cy_1\ln x+x^{\rho_2}\sum_{k\ge0}b_kx^k$，$b_0=1$，常数 $c$ 可能为零。

以上幂级数都在 $\lvert x\rvert<R$ 内收敛。在 $-R<x<0$ 上把 $x^\rho$、$\ln x$ 换成 $\lvert x\rvert^\rho$、$\ln\lvert x\rvert$ 即可。

**证明** （思路）$F(\rho)=(\rho-\rho_1)(\rho-\rho_2)$。对 $\rho=\rho_1$，$F(\rho_1+k)=k(k+\rho_1-\rho_2)\ne0$（$k\ge1$，因为 $\operatorname{Re}(\rho_1-\rho_2)\ge0$），所以 (10.5) 逐个确定 $a_k$。收敛性的证明与定理 10.1.1 一样用强级数，关键是 $\lvert F(\rho_1+k)\rvert$ 像 $k^2$ 一样增长。对 $\rho=\rho_2$，只要 $F(\rho_2+k)=k(k-N)$ 对所有 $k\ge1$ 非零，即 $\rho_1-\rho_2$ 不是正整数，同样得到 $y_2$；$\rho_1\ne\rho_2$ 时两解的首项 $x^{\rho_1}$、$x^{\rho_2}$ 不同，线性无关。

在 3、4 的情形，递推在 $k=N$ 处遇到 $F(\rho_2+N)=0$：若 (10.5) 右端此时恰为零，$b_N$ 可任取，得到 $c=0$ 的情形；否则无解，需要对数项。对数项的形式可以用降阶公式 (9.6) 得到：$y_2=y_1\int\frac{\mathrm{e}^{-\int p}}{y_1^2}$，其中 $\mathrm{e}^{-\int p}=x^{-p_0}\cdot(\text{幂级数})$，$y_1^{-2}=x^{-2\rho_1}\cdot(\text{幂级数})$，而 $p_0=1-\rho_1-\rho_2$，所以被积函数为 $x^{-1-N}\cdot(\text{幂级数})$，积分时 $x^{-1}$ 项产生 $\ln x$，其余项给出 $x^{-N}\cdot(\text{幂级数})$。 $\square$

**算法 10.3.1（Frobenius 方法）** 在正则奇点 $x=0$ 附近求解：

1. 写成 (10.4)，求 $p_0,q_0$ 与指标方程的根 $\rho_1,\rho_2$；
2. 对 $\rho_1$ 用递推 (10.5) 求 $y_1$；
3. 按 $\rho_1-\rho_2$ 是否为整数，用定理 10.3.1 的形式设出 $y_2$ 代入，或用降阶公式 (9.6) 求 $y_2$。

**例 10.3.1** 解 $2xy''+y'+y=0$（$x>0$）。乘以 $\frac x2$：$x^2y''+\frac x2y'+\frac x2y=0$，$p_0=\frac12$，$q_0=0$，指标方程 $\rho(\rho-1)+\frac\rho2=0$，$\rho_1=\frac12$，$\rho_2=0$，差不是整数。直接代入原方程，$x^{\rho+k-1}$ 的系数给出

$$
(\rho+k)(2\rho+2k-1)a_k=-a_{k-1}.
$$
$\rho=0$：$a_k=-\frac{a_{k-1}}{k(2k-1)}$，$y_2=1-x+\frac{x^2}{6}-\frac{x^3}{90}+\cdots=\sum_k\frac{(-1)^k(2x)^k}{(2k)!}=\cos\sqrt{2x}$。$\rho=\frac12$：$a_k=-\frac{a_{k-1}}{k(2k+1)}$，$y_1=\sqrt x\big(1-\frac x3+\frac{x^2}{30}-\cdots\big)=\frac{1}{\sqrt2}\sin\sqrt{2x}$。通解 $y=C_1\cos\sqrt{2x}+C_2\sin\sqrt{2x}$（可以验证：令 $x=s^2/2$，方程化为 $y_{ss}+y=0$）。

**注 10.3.1** Gauss 超几何方程 $x(1-x)y''+\big(c-(a+b+1)x\big)y'-aby=0$ 有三个正则奇点 $0,1,\infty$，在 $x=0$ 处指标为 $0$ 与 $1-c$，$\rho=0$ 的 Frobenius 解是超几何级数

$$
F(a,b;c;x)=\sum_{k\ge0}\frac{(a)_k(b)_k}{(c)_k\,k!}x^k,\qquad(a)_k=a(a+1)\cdots(a+k-1).
$$
许多特殊函数是它的特例，例如 $P_n(x)=F\big(-n,n+1;1;\frac{1-x}{2}\big)$：Legendre 方程以 $x=\pm1,\infty$ 为正则奇点，换元 $t=\frac{1-x}{2}$ 后就是超几何方程。

## 10.4. Bessel 方程与 Bessel 函数

### 10.4.1. 第一类 Bessel 函数

**定义 10.4.1（Bessel 方程）** 称

$$
x^2y''+xy'+(x^2-\nu^2)y=0\qquad(\nu\ge0)\tag{10.6}
$$
为 $\nu$ 阶 **Bessel 方程**。

在极坐标中对 Helmholtz 方程 $\Delta u+k^2u=0$ 分离变量 $u=R(r)\mathrm{e}^{\mathrm{i}\nu\theta}$，令 $x=kr$，$R$ 就满足 (10.6)；圆膜的振动、圆柱中的热传导都归结为它（[2.5](/2.5)）。

$x=0$ 是正则奇点，$p_0=1$，$q_0=-\nu^2$，指标方程 $\rho^2-\nu^2=0$，$\rho=\pm\nu$。对 $\rho=\nu$，(10.5) 化为

$$
k(k+2\nu)a_k=-a_{k-2},\qquad a_1=0,
$$
所以奇数项为零，$a_{2m}=\dfrac{(-1)^ma_0}{2^{2m}m!\,(\nu+1)(\nu+2)\cdots(\nu+m)}$。取 $a_0=\dfrac{1}{2^\nu\Gamma(\nu+1)}$，用 **Gamma 函数**的性质 $\Gamma(\nu+m+1)=(\nu+m)\cdots(\nu+1)\Gamma(\nu+1)$ 整理：

**定义 10.4.2（第一类 Bessel 函数）** 称

$$
J_\nu(x)=\sum_{m=0}^\infty\frac{(-1)^m}{m!\,\Gamma(m+\nu+1)}\Big(\frac x2\Big)^{2m+\nu}\tag{10.7}
$$
为 $\nu$ 阶**第一类 Bessel 函数**。把 (10.7) 中的 $\nu$ 换成 $-\nu$（约定 $1/\Gamma$ 在非正整数处为零）定义 $J_{-\nu}$。

由比值判别法，(10.7) 中的级数对一切 $x$ 收敛。例如

$$
J_0(x)=1-\frac{x^2}{2^2}+\frac{x^4}{2^2\cdot4^2}-\frac{x^6}{2^2\cdot4^2\cdot6^2}+\cdots,\qquad J_1(x)=\frac x2-\frac{x^3}{2^2\cdot4}+\frac{x^5}{2^2\cdot4^2\cdot6}-\cdots.
$$

**定理 10.4.1** 

1. $\nu\notin\mathbb{Z}$ 时 $J_\nu$、$J_{-\nu}$ 是 (10.6) 的两个线性无关的解，$W[J_\nu,J_{-\nu}](x)=-\dfrac{2\sin\nu\pi}{\pi x}$；
2. $\nu=n$ 为整数时 $J_{-n}=(-1)^nJ_n$，二者线性相关；
3. $J_{1/2}(x)=\sqrt{\dfrac{2}{\pi x}}\sin x$，$J_{-1/2}(x)=\sqrt{\dfrac{2}{\pi x}}\cos x$。

**证明** 1：$x\to0^+$ 时 $J_{\pm\nu}\sim\frac{(x/2)^{\pm\nu}}{\Gamma(1\pm\nu)}$，行为不同，所以线性无关（这里 $2\nu$ 可以是奇数，即指标差为整数，但 $c=0$，没有对数项）。由 Liouville 公式（定理 9.1.2，标准形式中 $p_1=\frac1x$），$W=\frac{C}{x}$，常数 $C$ 由首项计算并用余元公式 $\Gamma(\nu)\Gamma(1-\nu)=\frac{\pi}{\sin\nu\pi}$ 得到。2：$1/\Gamma(m-n+1)=0$（$m<n$），从 $m=n$ 开始求和并令 $m=n+j$ 即得。3：代入 $\Gamma(\frac32)=\frac{\sqrt\pi}2$ 等，与 $\sin x$、$\cos x$ 的级数比较。 $\square$

### 10.4.2. 第二类 Bessel 函数

整数阶时需要第二个解，按定理 10.3.1 第 3、4 条它带有对数项。统一的做法是：

**定义 10.4.3（第二类 Bessel 函数）** 对 $\nu\notin\mathbb{Z}$ 令

$$
Y_\nu(x)=\frac{J_\nu(x)\cos\nu\pi-J_{-\nu}(x)}{\sin\nu\pi},
$$
对整数 $n$ 令 $Y_n(x)=\lim_{\nu\to n}Y_\nu(x)$。$Y_\nu$ 称为 $\nu$ 阶**第二类 Bessel 函数**（Neumann 函数）。

对一切 $\nu\ge0$，$J_\nu$ 与 $Y_\nu$ 线性无关，$W[J_\nu,Y_\nu]=\frac{2}{\pi x}$，Bessel 方程的通解为 $y=C_1J_\nu(x)+C_2Y_\nu(x)$。$x\to0^+$ 时 $Y_\nu$ 无界：

$$
Y_0(x)=\frac2\pi\Big(\ln\frac x2+\gamma\Big)J_0(x)+(\text{常数项为零的幂级数}),\qquad Y_\nu(x)\sim-\frac{\Gamma(\nu)}{\pi}\Big(\frac2x\Big)^\nu\quad(\nu>0),
$$
其中 $\gamma$ 是 **Euler 常数**。在包含圆心的区域中求解时，要求解在 $r=0$ 处有界，就只保留 $J_\nu$。

### 10.4.3. 基本性质

**定理 10.4.2** 对 $\nu\ge0$ 与 $x>0$：

1. （递推公式）$\big(x^\nu J_\nu\big)'=x^\nu J_{\nu-1}$，$\big(x^{-\nu}J_\nu\big)'=-x^{-\nu}J_{\nu+1}$，从而

$$
J_{\nu-1}+J_{\nu+1}=\frac{2\nu}{x}J_\nu,\qquad J_{\nu-1}-J_{\nu+1}=2J_\nu',\qquad J_0'=-J_1;
$$
$Y_\nu$ 满足同样的递推公式。

2. （渐近行为）$x\to+\infty$ 时

$$
J_\nu(x)=\sqrt{\frac{2}{\pi x}}\cos\Big(x-\frac{\nu\pi}{2}-\frac\pi4\Big)+O(x^{-3/2}),\qquad Y_\nu(x)=\sqrt{\frac{2}{\pi x}}\sin\Big(x-\frac{\nu\pi}{2}-\frac\pi4\Big)+O(x^{-3/2}).
$$

3. （零点）$J_\nu$ 有无穷多个正零点 $0<j_{\nu,1}<j_{\nu,2}<\cdots$，都是单零点，$j_{\nu,k+1}-j_{\nu,k}\to\pi$；$J_\nu$ 与 $J_{\nu+1}$ 的正零点互相交错。

4. （正交性）设 $\alpha$、$\beta$ 是 $J_\nu$ 的两个正零点，则

$$
\int_0^1xJ_\nu(\alpha x)J_\nu(\beta x)\,\mathrm{d}x=\begin{cases}0,&\alpha\ne\beta,\\\dfrac12J_{\nu+1}(\alpha)^2,&\alpha=\beta.\end{cases}
$$

**证明** 1：由 (10.7)，$x^\nu J_\nu=\sum_m\frac{(-1)^mx^{2m+2\nu}}{2^{2m+\nu}m!\,\Gamma(m+\nu+1)}$，逐项求导，$\frac{2m+2\nu}{\Gamma(m+\nu+1)}=\frac{2}{\Gamma(m+\nu)}$，得 $x^\nu\sum_m\frac{(-1)^m}{m!\,\Gamma(m+\nu)}(\frac x2)^{2m+\nu-1}=x^\nu J_{\nu-1}$。第二式同理。把两式展开（$\nu x^{\nu-1}J_\nu+x^\nu J_\nu'=x^\nu J_{\nu-1}$ 等）相加、相减即得后面的公式。

2：（思路）令 $u=\sqrt xy$，(10.6) 化为

$$
u''+\Big(1-\frac{\nu^2-\frac14}{x^2}\Big)u=0,
$$
$x$ 很大时它接近 $u''+u=0$，解近似为 $A\cos(x-\delta)$；精确的振幅与相位需要积分表示，从略。$\nu=\frac12$ 时修正项为零，$u$ 恰好是 $\sin x$、$\cos x$，与定理 10.4.1 第 3 条一致。

3：零点的存在与间距 $\to\pi$ 由上面 $u$ 的方程与 Sturm 比较定理（[2.4.12](/2.4.12)）得到。单零点：若 $J_\nu(x_0)=J_\nu'(x_0)=0$（$x_0>0$ 是常点），由唯一性 $J_\nu\equiv0$。交错性：由 1，$x^{-\nu}J_\nu$ 的相邻零点之间有其导数 $-x^{-\nu}J_{\nu+1}$ 的零点（Rolle 定理），$x^{\nu+1}J_{\nu+1}$ 的相邻零点之间有 $x^{\nu+1}J_\nu$ 的零点。

4：$u(x)=J_\nu(\alpha x)$ 满足 $(xu')'+\big(\alpha^2x-\frac{\nu^2}{x}\big)u=0$，$v(x)=J_\nu(\beta x)$ 满足同样的方程（$\alpha$ 换成 $\beta$）。两式分别乘以 $v$、$u$ 相减：

$$
\big(x(u'v-uv')\big)'=(\beta^2-\alpha^2)xuv.
$$
在 $[0,1]$ 上积分：$x=1$ 处 $u(1)=v(1)=0$，$x=0$ 处 $x(u'v-uv')\to0$（$u,v\sim x^\nu$），所以 $\alpha\ne\beta$ 时 $\int_0^1xuv=0$。$\alpha=\beta$ 的值可以对 $\beta\to\alpha$ 取极限并用 L'Hospital 法则求出，再由 1 把 $J_\nu'(\alpha)$ 换成 $-J_{\nu+1}(\alpha)$。 $\square$

$J_0$ 的前几个零点为 $j_{0,1}\approx2.4048$，$j_{0,2}\approx5.5201$，$j_{0,3}\approx8.6537$；$J_1$ 的为 $3.8317$、$7.0156$、$10.1735$。圆膜振动的固有频率正比于这些零点，它们的间距不是常数，所以鼓声不像弦那样有整数倍的泛音。

由正交性，$\{J_\nu(j_{\nu,k}x)\}_{k\ge1}$ 在 $[0,1]$ 上关于权函数 $x$ 正交，可以把 $[0,1]$ 上的函数展开为 Fourier–Bessel 级数

$$
f(x)\sim\sum_{k=1}^\infty c_kJ_\nu(j_{\nu,k}x),\qquad c_k=\frac{2}{J_{\nu+1}(j_{\nu,k})^2}\int_0^1xf(x)J_\nu(j_{\nu,k}x)\,\mathrm{d}x,
$$
它对分段光滑的 $f$ 收敛（陈述）。这正是用分离变量法解圆域上的偏微分方程时需要的展开。

![左：第一类 Bessel 函数 J_0, J_1, J_2，振幅按 x^{-1/2} 衰减，虚线为 J_0 的渐近式 √(2/(πx)) cos(x - π/4)；右：第二类 Bessel 函数 Y_0, Y_1，在 x → 0 时趋于 -∞](./plots/bessel-functions.py)

### 10.4.4. 其他表示与相关方程

1. （母函数与积分表示）对整数 $n$，$\exp\big(\frac x2(t-\frac1t)\big)=\sum_{n\in\mathbb{Z}}J_n(x)t^n$，$J_n(x)=\frac1\pi\int_0^\pi\cos(n\theta-x\sin\theta)\,\mathrm{d}\theta$（陈述）。
2. 对 $\lambda>0$，$x^2y''+xy'+(\lambda^2x^2-\nu^2)y=0$ 的通解为 $C_1J_\nu(\lambda x)+C_2Y_\nu(\lambda x)$（令 $s=\lambda x$）。分离变量中出现的通常是这种形式，$\lambda$ 由边界条件 $J_\nu(\lambda a)=0$ 确定为 $j_{\nu,k}/a$。
3. 修正 Bessel 方程 $x^2y''+xy'-(x^2+\nu^2)y=0$（把 $x$ 换成 $\mathrm{i}x$）的解是修正 Bessel 函数 $I_\nu(x)=\mathrm{i}^{-\nu}J_\nu(\mathrm{i}x)=\sum_m\frac{1}{m!\,\Gamma(m+\nu+1)}(\frac x2)^{2m+\nu}$ 与 $K_\nu$；它们不振荡，$I_\nu$ 指数增长，$K_\nu$ 指数衰减，出现在圆柱上的稳态热传导问题中。
4. Airy 方程 $y''+xy=0$ 在 $x>0$ 上的通解为 $\sqrt x\big(C_1J_{1/3}(\frac23x^{3/2})+C_2J_{-1/3}(\frac23x^{3/2})\big)$（例 10.1.1 中 $y''=xy$ 的解对应修正 Bessel 函数）。

## 小结

| 情形 | 解的形式 | 关键 |
|---|---|---|
| 常点 | $\sum a_k(x-x_0)^k$，收敛半径不小于系数的 | 代入比较系数得递推；$a_0,a_1$ 任意 |
| 正则奇点 | $x^\rho\sum a_kx^k$ | 指标方程 $\rho(\rho-1)+p_0\rho+q_0=0$ |
| 指标差 $\notin\mathbb{Z}$ | 两个 Frobenius 级数 | — |
| 指标差 $=0$ | $y_1\ln x+x^{\rho_1}\sum b_kx^k$ | 必有对数项 |
| 指标差为正整数 $N$ | $cy_1\ln x+x^{\rho_2}\sum b_kx^k$ | 递推在 $k=N$ 处的相容性决定 $c$ 是否为零 |

| 函数 | 方程 | 主要性质 |
|---|---|---|
| $P_n(x)$ | $(1-x^2)y''-2xy'+n(n+1)y=0$ | Rodrigues 公式；$\int_{-1}^1P_mP_n=\frac{2}{2n+1}\delta_{mn}$；在 $[-1,1]$ 上有界的唯一解 |
| $J_\nu(x)$ | $x^2y''+xy'+(x^2-\nu^2)y=0$ | 级数 (10.7)；在 $0$ 处有界；无穷多个零点；$\int_0^1xJ_\nu(\alpha x)J_\nu(\beta x)=0$ |
| $Y_\nu(x)$ | 同上 | 在 $0$ 处无界（整数阶有对数项）；$W[J_\nu,Y_\nu]=\frac2{\pi x}$ |
