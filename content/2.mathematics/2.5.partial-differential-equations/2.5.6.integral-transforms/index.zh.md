---
title: Fourier 变换与 Laplace 变换
source_hash: ea7bae66ae45
---

在有界区间上分离变量，得到的是离散的特征值和 **Fourier 级数**。在整条直线上，没有边界条件把频率"量子化"：每个频率 $\xi\in\mathbb{R}$ 都是允许的，级数变成了积分。Fourier 变换把函数分解为平面波 $\mathrm{e}^{\mathrm{i}\xi x}$，它们是求导运算的特征函数：$\frac{\mathrm{d}}{\mathrm{d}x}\mathrm{e}^{\mathrm{i}\xi x}=\mathrm{i}\xi\,\mathrm{e}^{\mathrm{i}\xi x}$。在变换之下，求导变为乘以 $\mathrm{i}\xi$，$\mathbb{R}$ 上的常系数线性偏微分方程变为关于其余变量的常微分方程，解的公式则以卷积的形式出现。Fourier 变换在偏微分方程之外同样基本：信号处理、光学、概率论（分布的特征函数就是 Fourier 变换）、量子力学和数值分析都离不开它。

本章仔细地建立这套理论，因为通常的微积分课程只给出公式，却不说明公式何时成立、为什么成立。我们从 Fourier 级数过渡到 Fourier 积分（§6.1），定义变换并证明其主要性质，包括卷积定理，以及通过在复平面上平移积分路径算出的 Gauss 函数的变换（§6.2）。然后证明反演公式与 Plancherel 定理，并导出不确定性原理（§6.3），再用变换求解无界区域上的热方程、波动方程和 Laplace 方程（§6.4）。最后讨论 Laplace 变换——适用于初值问题的单边变换，它的反演是一个围道积分，用留数计算（§6.5）。全章都要用到复变函数（[2.3](/2.3)）；这里得到的热核将在 [2.5.7](/2.5.7) 中研究，上半平面的 Poisson 核则在 [2.5.8](/2.5.8) 中再次出现。

## 6.1. 从 Fourier 级数到 Fourier 积分

设 $f$ 是 $\mathbb{R}$ 上在无穷远处衰减的函数。它在 $[-l,l]$ 上有复形式的 Fourier 级数（[2.2.9](/2.2.9#sec-9.3.3)）

$$
f(x)=\sum_{n=-\infty}^{\infty}c_n\mathrm{e}^{\mathrm{i}\xi_nx},\qquad c_n=\frac1{2l}\int_{-l}^lf(y)\mathrm{e}^{-\mathrm{i}\xi_ny}\,\mathrm{d}y,\qquad\xi_n=\frac{n\pi}{l}.
$$
允许的频率 $\xi_n$ 之间的间隔为 $\Delta\xi=\pi/l$。记 $F_l(\xi)=\int_{-l}^lf(y)\mathrm{e}^{-\mathrm{i}\xi y}\,\mathrm{d}y$，则 $c_n=F_l(\xi_n)/(2l)=F_l(\xi_n)\Delta\xi/(2\pi)$，于是

$$
f(x)=\frac1{2\pi}\sum_{n=-\infty}^\infty F_l(\xi_n)\,\mathrm{e}^{\mathrm{i}\xi_nx}\,\Delta\xi.
$$
当 $l\to\infty$ 时，频率布满整条直线，$F_l(\xi)$ 趋于 $\hat f(\xi)=\int_{\mathbb{R}}f(y)\mathrm{e}^{-\mathrm{i}\xi y}\,\mathrm{d}y$，而和式看起来像一个积分的 Riemann 和：

$$
f(x)=\frac1{2\pi}\int_{-\infty}^{\infty}\hat f(\xi)\,\mathrm{e}^{\mathrm{i}\xi x}\,\mathrm{d}\xi.\tag{6.1}
$$
把 $f$ 表示为平面波的连续叠加，这就是 Fourier 积分（Fourier integral）。上面的论证只是启发式的（Riemann 和的范围无界，而且 $F_l$ 随 $l$ 变化），本章其余部分要说明 (6.1) 何时真正成立。周期函数的系数构成离散谱；对整条直线上的函数，$\hat f(\xi)\,\mathrm{d}\xi/(2\pi)$ 是 $[\xi,\xi+\mathrm{d}\xi]$ 中频率的振幅，构成连续谱。

![把 exp(-|x|) 限制在 [-l, l] 上，放大后的 Fourier 系数 2l c_n 位于频率 n pi / l 处；随着 l 增大，它们填满 Fourier 变换 2 / (1 + xi^2) 的曲线](./plots/series-to-integral.py)

## 6.2. Fourier 变换

### 6.2.1. 定义与基本例子

称 $f\colon\mathbb{R}\to\mathbb{C}$ 绝对可积，是指它在每个有界区间上可积，且 $\int_{\mathbb{R}}\lvert f\rvert\,\mathrm{d}x<\infty$（绝对收敛的**反常积分**）。

**定义 6.2.1（Fourier 变换）** 设 $f$ 在 $\mathbb{R}$ 上绝对可积。函数

$$
\hat f(\xi)=\mathscr{F}\{f\}(\xi)=\int_{-\infty}^{\infty}f(x)\,\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x,\qquad\xi\in\mathbb{R},\tag{6.2}
$$
称为 $f$ 的 **Fourier 变换**。对 $\mathbb{R}$ 上绝对可积的 $g$，函数

$$
\mathscr{F}^{-1}\{g\}(x)=\frac1{2\pi}\int_{-\infty}^\infty g(\xi)\,\mathrm{e}^{\mathrm{i}\xi x}\,\mathrm{d}\xi\tag{6.3}
$$
称为 $g$ 的 **Fourier 逆变换**。

若 $x$ 是时间（或位置），变量 $\xi$ 就是角频率（或波数）。其他书中常数因子的放法不同：有的在两个方向都用 $\frac1{\sqrt{2\pi}}$；信号处理中常用普通频率 $\nu=\xi/(2\pi)$ 写成 $\int f(x)\mathrm{e}^{-2\pi\mathrm{i}\nu x}\,\mathrm{d}x$，这样所有的 $2\pi$ 因子都消失了。理论是相同的，只是下面公式中的常数会变，查表之前必须先确认所用的约定。

**定理 6.2.1** 若 $f$ 绝对可积，则 $\hat f$ 有界，$\lvert\hat f(\xi)\rvert\le\int_{\mathbb{R}}\lvert f\rvert\,\mathrm{d}x$，在 $\mathbb{R}$ 上一致连续，且当 $\xi\to\pm\infty$ 时 $\hat f(\xi)\to0$。最后这一结论称为 Riemann–Lebesgue 引理（Riemann–Lebesgue lemma）。

**证明** 有界性由 $\lvert f(x)\mathrm{e}^{-\mathrm{i}\xi x}\rvert=\lvert f(x)\rvert$ 得到。对连续性，$\lvert\hat f(\xi+h)-\hat f(\xi)\rvert\le\int\lvert f(x)\rvert\,\lvert\mathrm{e}^{-\mathrm{i}hx}-1\rvert\,\mathrm{d}x$。任给 $\varepsilon>0$，取 $A$ 使 $\int_{\lvert x\rvert>A}\lvert f\rvert<\varepsilon$；在 $\lvert x\rvert\le A$ 上 $\lvert\mathrm{e}^{-\mathrm{i}hx}-1\rvert\le\lvert h\rvert A$。因此差不超过 $\lvert h\rvert A\int\lvert f\rvert+2\varepsilon$，与 $\xi$ 无关。

对 Riemann–Lebesgue 引理，先设 $f=\boldsymbol{1}_{[a,b]}$ 是一个区间的示性函数。则 $\hat f(\xi)=\frac{\mathrm{e}^{-\mathrm{i}a\xi}-\mathrm{e}^{-\mathrm{i}b\xi}}{\mathrm{i}\xi}$ 趋于 $0$，因而每个阶梯函数（示性函数的有限线性组合）的变换也趋于 $0$。一般的绝对可积函数 $f$ 可以用阶梯函数 $s$ 逼近，使 $\int\lvert f-s\rvert<\varepsilon$（先截去尾部，再用 Riemann 和逼近），于是当 $\lvert\xi\rvert$ 充分大时 $\lvert\hat f(\xi)\rvert\le\lvert\hat s(\xi)\rvert+\varepsilon<2\varepsilon$。$\square$

衰减性 $\hat f(\xi)\to0$ 说明函数不可能含有可观数量的任意高频成分。下面更精细的结论表明，$\hat f$ 衰减的快慢度量了 $f$ 的光滑程度。

**例 6.2.1（矩形脉冲）** 对 $a>0$，$f=\boldsymbol{1}_{[-a,a]}$ 的变换为

$$
\hat f(\xi)=\int_{-a}^a\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x=\frac{2\sin a\xi}{\xi}\qquad(\hat f(0)=2a).
$$
这个变换不是绝对可积的，因为 $\lvert\sin a\xi/\xi\rvert$ 只按 $1/\lvert\xi\rvert$ 衰减。这是 $f$ 有跳跃的代价。

**例 6.2.2（指数函数）** 对 $a>0$，

$$
\mathscr{F}\{\mathrm{e}^{-a\lvert x\rvert}\}(\xi)=\int_{-\infty}^\infty\mathrm{e}^{-a\lvert x\rvert}\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x=\frac{1}{a+\mathrm{i}\xi}+\frac{1}{a-\mathrm{i}\xi}=\frac{2a}{a^2+\xi^2},
$$
因为 $\int_0^\infty\mathrm{e}^{-(a+\mathrm{i}\xi)x}\,\mathrm{d}x=\frac1{a+\mathrm{i}\xi}$。单看第一项可知，单边指数函数 $H(x)\mathrm{e}^{-ax}$ 的变换为 $\frac1{a+\mathrm{i}\xi}$，其中 $H$ 是 Heaviside 阶跃函数（$x>0$ 时 $H(x)=1$，$x<0$ 时 $H(x)=0$）。函数 $\mathrm{e}^{-a\lvert x\rvert}$ 连续，但在 $0$ 处有尖角，它的变换按 $1/\xi^2$ 衰减。

### 6.2.2. Gauss 函数

最重要的变换对是 Gauss 函数的变换对。我们用复积分来计算：思路是先配方，再把积分路径平移回实轴。

**定理 6.2.2（Gauss 函数的 Fourier 变换）** 对 $a>0$，

$$
\mathscr{F}\{\mathrm{e}^{-ax^2}\}(\xi)=\sqrt{\frac\pi a}\,\mathrm{e}^{-\xi^2/(4a)}.\tag{6.4}
$$
特别地，$\mathscr{F}\{\mathrm{e}^{-x^2/2}\}=\sqrt{2\pi}\,\mathrm{e}^{-\xi^2/2}$：除去一个常数因子，标准 Gauss 函数是它自己的 Fourier 变换。

**证明** 配方得 $-ax^2-\mathrm{i}\xi x=-a(x+\mathrm{i}b)^2-\frac{\xi^2}{4a}$，其中 $b=\frac{\xi}{2a}$，所以

$$
\hat f(\xi)=\mathrm{e}^{-\xi^2/(4a)}\int_{-\infty}^\infty\mathrm{e}^{-a(x+\mathrm{i}b)^2}\,\mathrm{d}x.
$$
最后这个积分是整函数 $h(z)=\mathrm{e}^{-az^2}$ 沿水平直线 $\operatorname{Im}z=b$ 的积分。设 $\gamma_R$ 是以 $-R$、$R$、$R+\mathrm{i}b$、$-R+\mathrm{i}b$ 为顶点的矩形的边界。由 **Cauchy 积分定理**（[2.3.4](/2.3.4)），$\oint_{\gamma_R}h(z)\,\mathrm{d}z=0$。在竖直边 $z=R+\mathrm{i}y$（$y$ 介于 $0$ 与 $b$ 之间）上，$\lvert h(z)\rvert=\mathrm{e}^{-a(R^2-y^2)}\le\mathrm{e}^{-aR^2+ab^2}$，所以沿这条边的积分不超过 $\lvert b\rvert\mathrm{e}^{ab^2}\mathrm{e}^{-aR^2}$，当 $R\to\infty$ 时趋于 $0$；$-R$ 处的边同理。因此由 **Gauss 积分**，

$$
\int_{-\infty}^\infty\mathrm{e}^{-a(x+\mathrm{i}b)^2}\,\mathrm{d}x=\int_{-\infty}^\infty\mathrm{e}^{-ax^2}\,\mathrm{d}x=\sqrt{\frac\pi a}.\ \square
$$

另一种证明不用复分析。函数 $f=\mathrm{e}^{-ax^2}$ 满足 $f'=-2axf$。由下面定理 6.2.3 中的求导与乘法法则，$\mathrm{i}\xi\hat f=-2a\cdot\mathrm{i}\hat f'$，即 $\hat f'=-\frac{\xi}{2a}\hat f$，所以 $\hat f=\hat f(0)\mathrm{e}^{-\xi^2/(4a)}$，其中 $\hat f(0)=\int\mathrm{e}^{-ax^2}\,\mathrm{d}x=\sqrt{\pi/a}$。

公式 (6.4) 显示了一种将反复出现的反比关系：窄的 Gauss 函数（$a$ 大，宽度约为 $1/\sqrt a$）有宽的变换（宽度约为 $\sqrt a$），反之亦然。

![三个变换对：矩形脉冲与 2 sin(xi)/xi，双边指数函数与 Lorentz 函数 2/(1 + xi^2)，以及三种宽度 s 的 Gauss 函数，其变换的宽度为 1/s](./plots/fourier-pairs.py)

### 6.2.3. 性质

**定理 6.2.3** 设 $f$ 绝对可积，$a,b\in\mathbb{R}$，$b\ne0$。

1. （线性）$\mathscr{F}\{\alpha f+\beta g\}=\alpha\hat f+\beta\hat g$；
2. （平移）$\mathscr{F}\{f(x-a)\}=\mathrm{e}^{-\mathrm{i}a\xi}\hat f(\xi)$；
3. （调制）$\mathscr{F}\{\mathrm{e}^{\mathrm{i}ax}f(x)\}=\hat f(\xi-a)$；
4. （伸缩）$\mathscr{F}\{f(bx)\}=\frac1{\lvert b\rvert}\hat f\big(\frac\xi b\big)$；
5. （共轭）$\mathscr{F}\{\bar f\}(\xi)=\overline{\hat f(-\xi)}$；因此若 $f$ 是实函数，则 $\hat f(-\xi)=\overline{\hat f(\xi)}$；若 $f$ 是实的偶函数，则 $\hat f$ 也是实的偶函数；
6. （求导）若 $f$ 连续且分段 $C^1$，$f'$ 绝对可积，则 $\mathscr{F}\{f'\}=\mathrm{i}\xi\hat f$；更一般地，在相应假设下 $\mathscr{F}\{f^{(k)}\}=(\mathrm{i}\xi)^k\hat f$；
7. （乘以 $x$）若 $xf(x)$ 绝对可积，则 $\hat f\in C^1$，且 $\mathscr{F}\{xf(x)\}=\mathrm{i}\hat f'(\xi)$。

**证明** 性质 1–5 由在 (6.2) 中作代换 $x\mapsto x+a$ 与 $x\mapsto x/b$ 得到（$b<0$ 时代换使积分上下限颠倒，从而出现 $\lvert b\rvert$）。

6：由于 $f(x)=f(0)+\int_0^xf'$ 且 $f'$ 绝对可积，$f(x)$ 在 $x\to\pm\infty$ 时有极限；又因 $f$ 绝对可积，这些极限只能是 $0$。在 $[-R,R]$ 上分部积分，

$$
\int_{-R}^Rf'(x)\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x=\Big[f(x)\mathrm{e}^{-\mathrm{i}\xi x}\Big]_{-R}^R+\mathrm{i}\xi\int_{-R}^Rf(x)\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x,
$$
令 $R\to\infty$ 即得 $\mathscr{F}\{f'\}=\mathrm{i}\xi\hat f$。

7：被积函数对 $\xi$ 的导数为 $-\mathrm{i}xf(x)\mathrm{e}^{-\mathrm{i}\xi x}$，它被与 $\xi$ 无关的可积函数 $\lvert xf(x)\rvert$ 控制。因此求导后的积分一致收敛（Weierstrass 判别法），**积分号下求导**是合理的：$\hat f'(\xi)=\int(-\mathrm{i}x)f(x)\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x=-\mathrm{i}\,\mathscr{F}\{xf\}$。$\square$

性质 6 与 7 是问题的核心，二者互为对偶：

- $f$ 的光滑性给出 $\hat f$ 的衰减：若 $f,f',\dots,f^{(k)}$ 都绝对可积，则 $(\mathrm{i}\xi)^k\hat f$ 有界并趋于 $0$（定理 6.2.1），所以 $\hat f(\xi)=o(\lvert\xi\rvert^{-k})$。
- $f$ 的衰减给出 $\hat f$ 的光滑性：若 $x^kf$ 绝对可积，则 $\hat f\in C^k$。

Gauss 函数既无穷光滑又迅速衰减，它的变换也是如此。矩形脉冲有跳跃，其变换只按 $1/\xi$ 衰减；函数 $\mathrm{e}^{-a\lvert x\rvert}$ 有尖角，其变换按 $1/\xi^2$ 衰减，但它本身指数衰减，所以变换 $\frac{2a}{a^2+\xi^2}$ 无穷次可微。

### 6.2.4. 卷积

**定义 6.2.2（卷积）** 设 $f,g$ 绝对可积，且其中之一有界。函数

$$
(f*g)(x)=\int_{-\infty}^\infty f(x-y)g(y)\,\mathrm{d}y
$$
称为 $f$ 与 $g$ 的**卷积**。

作代换 $y\mapsto x-y$ 可知 $f*g=g*f$；卷积还满足结合律与双线性，且 $\int\lvert f*g\rvert\le\int\lvert f\rvert\int\lvert g\rvert$。若 $g\ge0$ 且 $\int g=1$，则 $(f*g)(x)$ 是 $f$ 在 $x$ 附近取值的加权平均，即 $f$ 的光滑化：例如 $f*\frac1{2h}\boldsymbol{1}_{[-h,h]}$ 就是滑动平均 $\frac1{2h}\int_{x-h}^{x+h}f$。卷积描述了每一个线性、平移不变的系统：若系统对 $y$ 处单位脉冲的响应为 $g(x-y)$，则由叠加，它对输入 $f$ 的响应为 $f*g$。

**定理 6.2.4（卷积定理）** 在定义 6.2.2 的假设下，

$$
\mathscr{F}\{f*g\}=\hat f\,\hat g.\tag{6.5}
$$

**证明** 由于 $\int\!\!\int\lvert f(x-y)\rvert\,\lvert g(y)\rvert\,\mathrm{d}x\,\mathrm{d}y=\int\lvert f\rvert\cdot\int\lvert g\rvert<\infty$，下面的二重积分绝对收敛，可以交换积分次序（Fubini 定理）。把 $\mathrm{e}^{-\mathrm{i}\xi x}$ 写成 $\mathrm{e}^{-\mathrm{i}\xi(x-y)}\mathrm{e}^{-\mathrm{i}\xi y}$，

$$
\mathscr{F}\{f*g\}(\xi)=\int_{-\infty}^\infty g(y)\mathrm{e}^{-\mathrm{i}\xi y}\Big(\int_{-\infty}^\infty f(x-y)\mathrm{e}^{-\mathrm{i}\xi(x-y)}\,\mathrm{d}x\Big)\mathrm{d}y=\hat f(\xi)\int_{-\infty}^\infty g(y)\mathrm{e}^{-\mathrm{i}\xi y}\,\mathrm{d}y=\hat f(\xi)\hat g(\xi).\ \square
$$

这个定理正是卷积出现在解的公式中的原因：若变换后的问题通过把变换后的数据乘以某个函数 $\hat K(\xi)$ 来求解，那么解就是数据与 $K$ 的卷积。对偶地，在适当的假设下（例如 §6.3 的反演公式对 $f$ 与 $g$ 适用时），$\mathscr{F}\{fg\}=\frac1{2\pi}\hat f*\hat g$。

**例 6.2.3** 设 $p=\boldsymbol{1}_{[-1,1]}$。则 $(p*p)(x)$ 是 $[-1,1]\cap[x-1,x+1]$ 的长度，即三角形函数 $\max(2-\lvert x\rvert,0)$。由定理 6.2.4 与例 6.2.1，

$$
\mathscr{F}\{\max(2-\lvert x\rvert,0)\}=\Big(\frac{2\sin\xi}{\xi}\Big)^2=\frac{4\sin^2\xi}{\xi^2},
$$
这可以直接积分验证。三角形函数连续但有尖角，它的变换按 $1/\xi^2$ 衰减。

### 6.2.5. 多元情形

对 $\mathbb{R}^n$ 上绝对可积的 $f$，定义 $\hat f(\xi)=\int_{\mathbb{R}^n}f(x)\,\mathrm{e}^{-\mathrm{i}\xi\cdot x}\,\mathrm{d}x$，$\mathscr{F}^{-1}\{g\}(x)=(2\pi)^{-n}\int_{\mathbb{R}^n}g(\xi)\mathrm{e}^{\mathrm{i}\xi\cdot x}\,\mathrm{d}\xi$。本章的所有结果作显然的修改后都成立：$\partial/\partial x_j$ 变为乘以 $\mathrm{i}\xi_j$，所以 Laplace 算子变为乘以 $-\lvert\xi\rvert^2$；卷积定理对 $\int_{\mathbb{R}^n}$ 成立；又因 $\mathrm{e}^{-a\lvert x\rvert^2}=\prod_j\mathrm{e}^{-ax_j^2}$，公式 (6.4) 给出

$$
\mathscr{F}\{\mathrm{e}^{-a\lvert x\rvert^2}\}(\xi)=\Big(\frac\pi a\Big)^{n/2}\mathrm{e}^{-\lvert\xi\rvert^2/(4a)}.
$$

## 6.3. 反演与 Plancherel 定理

### 6.3.1. 近似单位元与 δ 函数

反演公式的证明基于一个简单而影响深远的想法：与一个总质量为 1 的窄核作卷积，几乎能还原原来的函数。

**引理 6.3.1（近似单位元）** 设 $K$ 绝对可积，$\int_{\mathbb{R}}K\,\mathrm{d}x=1$，对 $\varepsilon>0$ 令 $K_\varepsilon(x)=\frac1\varepsilon K\big(\frac x\varepsilon\big)$。若 $f$ 在 $\mathbb{R}$ 上有界且在 $x$ 处连续，则当 $\varepsilon\to0^+$ 时 $(K_\varepsilon*f)(x)\to f(x)$。若 $f$ 有界且一致连续，则收敛关于 $x$ 是一致的。

**证明** 由于 $\int K_\varepsilon=1$，作代换 $y=\varepsilon z$，

$$
(K_\varepsilon*f)(x)-f(x)=\int_{-\infty}^\infty K_\varepsilon(y)\big(f(x-y)-f(x)\big)\,\mathrm{d}y=\int_{-\infty}^\infty K(z)\big(f(x-\varepsilon z)-f(x)\big)\,\mathrm{d}z.
$$
设 $\lvert f\rvert\le M$，$\eta>0$。取 $A$ 使 $\int_{\lvert z\rvert>A}\lvert K\rvert<\eta$，再取 $\varepsilon_0$ 使 $\lvert w\rvert<\varepsilon_0A$ 时 $\lvert f(x-w)-f(x)\rvert<\eta$。当 $\varepsilon<\varepsilon_0$ 时，在 $\lvert z\rvert\le A$ 上的积分不超过 $\eta\int\lvert K\rvert$，在 $\lvert z\rvert>A$ 上的积分不超过 $2M\eta$。若 $f$ 一致连续，$\varepsilon_0$ 与 $x$ 无关。$\square$

当 $\varepsilon\to0^+$ 时，核 $K_\varepsilon$ 把全部质量集中到原点。物理学家把这个极限描述为 δ 函数（Dirac delta function）$\delta$：一个在 $x\ne0$ 处为零、并且满足

$$
\int_{-\infty}^\infty\delta(x)\varphi(x)\,\mathrm{d}x=\varphi(0)\qquad\text{对每个连续函数 }\varphi
$$
的"函数"。没有真正的函数具有这一性质；$\delta$ 是广义函数（分布），而 $K_\varepsilon\to\delta$ 的确切含义是 $\int K_\varepsilon\varphi\to\varphi(0)$，这正是 $x=0$ 时的引理 6.3.1。用这种语言，$\delta*f=f$，系统的脉冲响应就是它对 $\delta$ 的响应，并且

$$
\mathscr{F}\{\delta\}=1,\qquad\mathscr{F}\{1\}=2\pi\delta,\qquad\mathscr{F}\{\mathrm{e}^{\mathrm{i}ax}\}=2\pi\delta(\xi-a).
$$
第一个公式与 $\hat K_\varepsilon(\xi)=\hat K(\varepsilon\xi)\to\hat K(0)=1$ 一致；最后一个公式说明，纯振荡的全部频谱集中在一个频率上。我们只把 $\delta$ 当作这类极限的简便记法。

### 6.3.2. 反演定理

**定理 6.3.1（Fourier 反演定理）** 设 $f$ 在 $\mathbb{R}$ 上绝对可积。

1. 若 $f$ 连续且 $\hat f$ 绝对可积，则对每个 $x\in\mathbb{R}$，
$$
f(x)=\frac1{2\pi}\int_{-\infty}^\infty\hat f(\xi)\,\mathrm{e}^{\mathrm{i}\xi x}\,\mathrm{d}\xi,\qquad\text{即}\quad\mathscr{F}^{-1}\{\mathscr{F}\{f\}\}=f.
$$
2. 若 $f$ 在每个有界区间上分段光滑，则对每个 $x$，
$$
\lim_{R\to\infty}\frac1{2\pi}\int_{-R}^R\hat f(\xi)\,\mathrm{e}^{\mathrm{i}\xi x}\,\mathrm{d}\xi=\frac{f(x^+)+f(x^-)}2.
$$

**证明** 我们证明第 1 条。思路是插入一个 Gauss 因子 $\mathrm{e}^{-\varepsilon\xi^2}$，使所有积分绝对收敛，然后令 $\varepsilon\to0^+$。令

$$
I_\varepsilon(x)=\frac1{2\pi}\int_{-\infty}^\infty\hat f(\xi)\,\mathrm{e}^{-\varepsilon\xi^2}\mathrm{e}^{\mathrm{i}\xi x}\,\mathrm{d}\xi.
$$
代入 $\hat f$ 的定义，由于 $\int\!\!\int\lvert f(y)\rvert\mathrm{e}^{-\varepsilon\xi^2}\,\mathrm{d}y\,\mathrm{d}\xi<\infty$，二重积分绝对收敛，可以交换次序：

$$
I_\varepsilon(x)=\int_{-\infty}^\infty f(y)\Big(\frac1{2\pi}\int_{-\infty}^\infty\mathrm{e}^{-\varepsilon\xi^2}\mathrm{e}^{\mathrm{i}\xi(x-y)}\,\mathrm{d}\xi\Big)\mathrm{d}y=\int_{-\infty}^\infty f(y)\,g_\varepsilon(x-y)\,\mathrm{d}y,
$$
其中由 (6.4)（取 $a=\varepsilon$；由于 Gauss 函数是偶函数，指数中 $\xi$ 的符号无关紧要），

$$
g_\varepsilon(z)=\frac1{2\pi}\sqrt{\frac\pi\varepsilon}\,\mathrm{e}^{-z^2/(4\varepsilon)}=\frac{1}{\sqrt{4\pi\varepsilon}}\mathrm{e}^{-z^2/(4\varepsilon)}.
$$
这就是总积分为 1 的 Gauss 函数 $K(z)=\frac1{\sqrt{4\pi}}\mathrm{e}^{-z^2/4}$ 所对应的 $K_{\sqrt\varepsilon}$。连续的绝对可积函数不一定有界，所以把 $f$ 拆成 $f=f\boldsymbol{1}_{[x-1,x+1]}+f\boldsymbol{1}_{\mathbb{R}\setminus[x-1,x+1]}$。第一部分有界，可以应用引理 6.3.1；第二部分的贡献不超过 $\sup_{\lvert z\rvert\ge1}g_\varepsilon(z)\int\lvert f\rvert\to0$。因此 $I_\varepsilon(x)\to f(x)$。

另一方面，$\lvert\hat f(\xi)(\mathrm{e}^{-\varepsilon\xi^2}-1)\rvert\le\lvert\hat f(\xi)\rvert$ 可积，且被积函数对每个 $\xi$ 趋于 $0$。任给 $\eta>0$，取 $A$ 使 $\int_{\lvert\xi\rvert>A}\lvert\hat f\rvert<\eta$；在 $\lvert\xi\rvert\le A$ 上 $1-\mathrm{e}^{-\varepsilon\xi^2}\le\varepsilon A^2$。于是 $\big\lvert I_\varepsilon(x)-\frac1{2\pi}\int\hat f\mathrm{e}^{\mathrm{i}\xi x}\big\rvert\le\frac1{2\pi}\big(\varepsilon A^2\int\lvert\hat f\rvert+\eta\big)$，当 $\varepsilon$ 很小时它很小。比较两个极限即证得第 1 条。

第 2 条的证明与 Fourier 级数的 **Dirichlet 收敛定理**（[2.2.9](/2.2.9#thm-9.3.1)）的证明平行：截断积分等于 $\int f(x-y)\frac{\sin Ry}{\pi y}\,\mathrm{d}y$，核 $\frac{\sin Ry}{\pi y}$ 起着 Dirichlet 核的作用；细节从略。$\square$

证明中出现的核 $g_\varepsilon$，取 $\varepsilon=k t$ 时就是 §6.4.1 中得到的热方程的解：这个证明是让热量扩散一小段时间来光滑化 $f$。

**推论 6.3.1（唯一性）** 若 $f,g$ 连续且绝对可积，$\hat f=\hat g$，则 $f=g$。

**证明** 对 $f-g$ 应用定理 6.3.1 的第 1 条，它的变换 $0$ 是绝对可积的。$\square$

唯一性使变换表有用：一旦认出一个变换，就知道了原来的函数。反演公式还给出对偶关系 $\mathscr{F}\{\hat f\}(x)=2\pi f(-x)$（在第 1 条中把 $x$ 换成 $-x$），它使每张变换表的内容加倍。

**例 6.3.1** 由例 6.2.2 与对偶关系，$\mathscr{F}\big\{\frac{2a}{a^2+x^2}\big\}=2\pi\mathrm{e}^{-a\lvert\xi\rvert}$，即

$$
\mathscr{F}\Big\{\frac{a}{\pi(a^2+x^2)}\Big\}(\xi)=\mathrm{e}^{-a\lvert\xi\rvert}.\tag{6.6}
$$
把 $\xi$ 与 $x$ 互换后写出来，$\mathrm{e}^{-a\lvert x\rvert}$ 的反演公式就是 $\int_{-\infty}^\infty\frac{\cos\xi x}{a^2+\xi^2}\,\mathrm{d}\xi=\frac\pi a\mathrm{e}^{-a\lvert x\rvert}$，这个积分通常用留数和 **Jordan 引理**（[2.3.7](/2.3.7)）来计算。两种方法是同一事实的两种视角。

**例 6.3.2** 把定理 6.3.1 的第 2 条应用于例 6.2.1 中 $a=1$ 的矩形脉冲，取 $x=0$，得 $\frac1{2\pi}\lim_{R\to\infty}\int_{-R}^R\frac{2\sin\xi}{\xi}\,\mathrm{d}\xi=1$，即 **Dirichlet 积分** $\int_0^\infty\frac{\sin\xi}{\xi}\,\mathrm{d}\xi=\frac\pi2$。在跳跃点 $x=1$ 处，逆变换给出平均值 $\frac12$。

### 6.3.3. Plancherel 定理

**定理 6.3.2（Plancherel 定理）** 设 $f,g$ 在 $\mathbb{R}$ 上绝对可积且平方可积，并设定理 6.3.1（第 1 条）的反演公式对 $f$ 成立。则

$$
\int_{-\infty}^\infty f(x)\overline{g(x)}\,\mathrm{d}x=\frac1{2\pi}\int_{-\infty}^\infty\hat f(\xi)\overline{\hat g(\xi)}\,\mathrm{d}\xi,\qquad\int_{-\infty}^\infty\lvert f\rvert^2\,\mathrm{d}x=\frac1{2\pi}\int_{-\infty}^\infty\lvert\hat f\rvert^2\,\mathrm{d}\xi.\tag{6.7}
$$

**证明** 代入 $f$ 的反演公式并交换积分次序（由于 $\hat f$ 与 $g$ 绝对可积，二重积分绝对收敛）：

$$
\int f\bar g\,\mathrm{d}x=\int\Big(\frac1{2\pi}\int\hat f(\xi)\mathrm{e}^{\mathrm{i}\xi x}\,\mathrm{d}\xi\Big)\overline{g(x)}\,\mathrm{d}x=\frac1{2\pi}\int\hat f(\xi)\,\overline{\int g(x)\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x}\,\mathrm{d}\xi=\frac1{2\pi}\int\hat f\,\overline{\hat g}\,\mathrm{d}\xi.
$$
取 $g=f$ 即得第二个公式。$\square$

(6.7) 中的第二个公式是 Fourier 级数 Parseval 等式的连续形式：信号的能量等于其各频率成分的总能量，$\lvert\hat f(\xi)\rvert^2/(2\pi)$ 是能量谱密度。定理的假设可以完全去掉：对每个平方可积的 $f$，截断变换 $\int_{-R}^Rf(x)\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x$ 在均方意义下收敛于一个满足 (6.7) 的函数 $\hat f$，于是 Fourier 变换成为平方可积函数空间 $L^2(\mathbb{R})$ 到自身的双射，并且在相差因子 $2\pi$ 的意义下保持内积（不加证明）。这是量子力学中 Fourier 变换的自然框架。

**例 6.3.3** 对 $f=\boldsymbol{1}_{[-a,a]}$，$\int\lvert f\rvert^2=2a$，由 (6.7) 得 $\frac1{2\pi}\int\frac{4\sin^2a\xi}{\xi^2}\,\mathrm{d}\xi=2a$，即 $\int_{-\infty}^\infty\frac{\sin^2a\xi}{\xi^2}\,\mathrm{d}\xi=\pi a$。（这里 $f$ 不连续，上面叙述的定理 6.3.2 不适用，但 $L^2$ 形式适用。）

### 6.3.4. 不确定性原理

从 (6.4) 可以看出 $f$ 与 $\hat f$ 的宽度之间的反比关系，它对每个函数都成立。

**定理 6.3.3（不确定性原理）** 设 $f\in C^1(\mathbb{R})$，$f$、$xf$、$f'$ 平方可积，$f$ 与 $f'$ 绝对可积，且当 $x\to\pm\infty$ 时 $x\lvert f(x)\rvert^2\to0$。则

$$
\Big(\int_{-\infty}^\infty x^2\lvert f(x)\rvert^2\,\mathrm{d}x\Big)\Big(\int_{-\infty}^\infty\xi^2\lvert\hat f(\xi)\rvert^2\,\mathrm{d}\xi\Big)\ge\frac\pi2\Big(\int_{-\infty}^\infty\lvert f(x)\rvert^2\,\mathrm{d}x\Big)^2,
$$
等号成立当且仅当 $f(x)=C\mathrm{e}^{-ax^2}$，其中 $a>0$。

**证明** 分部积分，并利用 $(\lvert f\rvert^2)'=f'\bar f+f\bar f'=2\operatorname{Re}\big(f\bar f'\big)$，

$$
\int_{-\infty}^\infty\lvert f\rvert^2\,\mathrm{d}x=\Big[x\lvert f\rvert^2\Big]_{-\infty}^\infty-\int_{-\infty}^\infty x\big(\lvert f\rvert^2\big)'\,\mathrm{d}x=-2\operatorname{Re}\int_{-\infty}^\infty xf(x)\overline{f'(x)}\,\mathrm{d}x.
$$
由 **Cauchy–Schwarz 不等式**，$\big(\int\lvert f\rvert^2\big)^2\le4\int x^2\lvert f\rvert^2\int\lvert f'\rvert^2$。由定理 6.2.3（第 6 条）以及对 $f'$（其变换为 $\mathrm{i}\xi\hat f$）应用 Plancherel 定理，$\int\lvert f'\rvert^2=\frac1{2\pi}\int\xi^2\lvert\hat f\rvert^2$，这就给出了不等式。Cauchy–Schwarz 不等式取等号要求 $f'=-2axf$，其中 $a$ 为常数；为使实部达到上界、且 $f$ 平方可积，$a$ 必须是正实数，因此 $f=C\mathrm{e}^{-ax^2}$。反之，直接计算可知 Gauss 函数使等号成立。$\square$

用 $\sigma_x^2=\int x^2\lvert f\rvert^2/\int\lvert f\rvert^2$ 与 $\sigma_\xi^2=\int\xi^2\lvert\hat f\rvert^2/\int\lvert\hat f\rvert^2$ 定义 $f$ 与 $\hat f$ 关于原点的分散程度。由于 $\int\lvert\hat f\rvert^2=2\pi\int\lvert f\rvert^2$，定理表明

$$
\sigma_x\,\sigma_\xi\ge\frac12.
$$
（对 $\mathrm{e}^{-\mathrm{i}\xi_0x}f(x+x_0)$ 应用定理，可以得到关于任意中心 $x_0$、$\xi_0$ 的分散程度的同样的界。）信号不可能在时间和频率上同时高度集中：短脉冲含有宽频带，纯音必须持续很长时间。在量子力学中，粒子在动量变量 $p=\hbar\xi$ 下的波函数是它在位置变量下的波函数的 Fourier 变换，这个不等式就成为 Heisenberg 的 $\sigma_x\sigma_p\ge\hbar/2$。

## 6.4. 用 Fourier 变换解偏微分方程

**算法 6.4.1（Fourier 变换法）** 对 $x$ 取遍 $\mathbb{R}$（或 $\mathbb{R}^n$）的常系数线性偏微分方程：

1. 关于 $x$ 作变换：$u(x,t)\mapsto\hat u(\xi,t)$。导数 $\partial_x^k$ 变为乘以 $(\mathrm{i}\xi)^k$，偏微分方程变为以 $\xi$ 为参数的关于 $t$（或另一个变量）的常微分方程；
2. 对数据作变换并求解常微分方程，必要时利用有界性舍去增长的解；
3. 作逆变换，把乘积识别为卷积（定理 6.2.4），并利用变换表、对偶关系和平移法则。

这一计算是形式的：它假定 $u$ 有 Fourier 变换，且对 $t$ 求导与变换可以交换次序。所得的公式随后要直接验证，[2.5.7](/2.5.7) 对热方程正是这样做的。

### 6.4.1. 直线上的热方程

考虑无限长杆上的**热方程**：

$$
u_t=k u_{xx},\quad x\in\mathbb{R},\ t>0;\qquad u(x,0)=\varphi(x).
$$
关于 $x$ 作变换，得 $\hat u_t=-k\xi^2\hat u$，$\hat u(\xi,0)=\hat\varphi(\xi)$，所以 $\hat u(\xi,t)=\hat\varphi(\xi)\,\mathrm{e}^{-k\xi^2t}$。每个频率以速率 $k\xi^2$ 衰减：高频（精细的细节）衰减得最快。由 (6.4)（取 $a=\frac1{4k t}$），$\mathrm{e}^{-k\xi^2t}$ 是

$$
\Phi(x,t)=\frac{1}{\sqrt{4\pi k t}}\,\mathrm{e}^{-x^2/(4k t)},\qquad t>0,\tag{6.8}
$$
的变换，再由卷积定理，

$$
u(x,t)=(\Phi(\cdot,t)*\varphi)(x)=\frac1{\sqrt{4\pi k t}}\int_{-\infty}^\infty\mathrm{e}^{-(x-y)^2/(4k t)}\varphi(y)\,\mathrm{d}y.\tag{6.9}
$$
函数 $\Phi$ 称为热核（heat kernel）。它是 $0$ 时刻在原点释放单位热量（初始数据为 $\delta$）所产生的温度，而 (6.9) 把强度为 $\varphi(y)\,\mathrm{d}y$ 的点源叠加起来。在 [2.5.7](/2.5.7) 中我们将验证：对每个有界连续的 $\varphi$，即使 $\varphi$ 没有 Fourier 变换，(6.9) 也给出问题的解。

**例 6.4.1** 设 $\varphi=\boldsymbol{1}_{[-1,1]}$：杆的一段初始温度为 1，其余部分为 0。由 (6.9) 并作代换 $s=(y-x)/\sqrt{4k t}$，

$$
u(x,t)=\frac1{\sqrt\pi}\int_{(-1-x)/\sqrt{4k t}}^{(1-x)/\sqrt{4k t}}\mathrm{e}^{-s^2}\,\mathrm{d}s=\frac12\Big[\operatorname{erf}\Big(\frac{1-x}{\sqrt{4k t}}\Big)+\operatorname{erf}\Big(\frac{1+x}{\sqrt{4k t}}\Big)\Big],
$$
其中

$$
\operatorname{erf}(x)=\frac2{\sqrt\pi}\int_0^x\mathrm{e}^{-s^2}\,\mathrm{d}s,\qquad\operatorname{erfc}(x)=1-\operatorname{erf}(x)=\frac2{\sqrt\pi}\int_x^\infty\mathrm{e}^{-s^2}\,\mathrm{d}s
$$
分别是误差函数（error function）与余误差函数。$\operatorname{erf}$ 是奇函数，从 $-1$ 递增到 $1$，在 $0$ 附近 $\operatorname{erf}(x)\approx\frac{2x}{\sqrt\pi}$。$\varphi$ 的跳跃被瞬间抹平，而且当 $t>0$ 时解处处为正。

### 6.4.2. 直线上的波动方程

对 $\mathbb{R}$ 上的**波动方程** $u_{tt}=c^2u_{xx}$，$u(x,0)=\varphi(x)$，$u_t(x,0)=\psi(x)$，作变换得 $\hat u_{tt}=-c^2\xi^2\hat u$，所以

$$
\hat u(\xi,t)=\hat\varphi(\xi)\cos(c\xi t)+\hat\psi(\xi)\frac{\sin(c\xi t)}{c\xi}.
$$
而 $\cos(c\xi t)\hat\varphi=\frac12\big(\mathrm{e}^{\mathrm{i}c\xi t}+\mathrm{e}^{-\mathrm{i}c\xi t}\big)\hat\varphi$，由平移法则，它是 $\frac12\big(\varphi(x+ct)+\varphi(x-ct)\big)$ 的变换。由例 6.2.1（取 $a=ct$），$\frac{\sin(c\xi t)}{c\xi}$ 是 $\frac1{2c}\boldsymbol{1}_{[-ct,ct]}$ 的变换，它与 $\hat\psi$ 的乘积是卷积 $\frac1{2c}\int_{x-ct}^{x+ct}\psi(y)\,\mathrm{d}y$ 的变换。因此

$$
u(x,t)=\frac{\varphi(x+ct)+\varphi(x-ct)}2+\frac1{2c}\int_{x-ct}^{x+ct}\psi(y)\,\mathrm{d}y,
$$
这正是 **d'Alembert 公式**（[2.5.3](/2.5.3)）。在频域中比较这两个方程，就能解释它们不同的行为：对热方程，因子 $\mathrm{e}^{-k\xi^2t}$ 使每个频率都衰减；对波动方程，因子 $\mathrm{e}^{\pm\mathrm{i}c\xi t}$ 的模为 1，没有任何频率被衰减，所以数据的奇性不经光滑化地传播下去。

### 6.4.3. 上半平面上的 Laplace 方程

求上半平面上具有给定边界值的有界**调和函数**：

$$
u_{xx}+u_{yy}=0,\quad x\in\mathbb{R},\ y>0;\qquad u(x,0)=f(x),\qquad u\text{ 有界}.
$$
关于 $x$ 作变换得 $\hat u_{yy}=\xi^2\hat u$，所以 $\hat u=A(\xi)\mathrm{e}^{-\lvert\xi\rvert y}+B(\xi)\mathrm{e}^{\lvert\xi\rvert y}$。第二项随 $y$ 指数增长，由有界性排除，而 $A=\hat f$：

$$
\hat u(\xi,y)=\hat f(\xi)\,\mathrm{e}^{-\lvert\xi\rvert y}.
$$
由 (6.6)（取 $a=y$），$\mathrm{e}^{-\lvert\xi\rvert y}$ 是 $P_y(x)=\frac{y}{\pi(x^2+y^2)}$ 的变换，由卷积定理得

$$
u(x,y)=(P_y*f)(x)=\frac y\pi\int_{-\infty}^\infty\frac{f(s)}{(x-s)^2+y^2}\,\mathrm{d}s.\tag{6.10}
$$
函数 $P_y$ 是上半平面的 Poisson 核；它是正的，积分为 1，并且对 $K(x)=\frac1{\pi(1+x^2)}$ 有 $P_y=K_y$，所以由引理 6.3.1，在有界函数 $f$ 的每个连续点处，当 $y\to0^+$ 时 $u(x,y)\to f(x)$。在 [2.5.8](/2.5.8) 中，同一个公式将由 Green 函数得到，圆盘的情形则由共形映射得到。

**例 6.4.2** 设 $f=\boldsymbol{1}_{[-1,1]}$。则

$$
u(x,y)=\frac1\pi\int_{-1}^1\frac{y\,\mathrm{d}s}{(s-x)^2+y^2}=\frac1\pi\Big[\arctan\frac{1-x}y+\arctan\frac{1+x}y\Big]=\frac{\alpha(x,y)}\pi,
$$
其中 $\alpha$ 是从点 $(x,y)$ 看线段 $[-1,1]$ 的张角。由圆周角定理，等值线 $\alpha=\text{常数}$ 是过 $\pm1$ 的圆弧。这个角是 $\frac{z-1}{z+1}$ 的辐角，即一个解析函数的虚部，这说明了它为什么是调和的（[2.5.8](/2.5.8)）。

![左：若干高度 y 下上半平面的 Poisson 核，当 y → 0 时它是近似单位元。右：在 (-1, 1) 上边界值为 1、其余处为 0 的有界调和函数；其等值线是过 ±1 的圆弧](./plots/half-plane-poisson.py)

## 6.5. Laplace 变换

Fourier 变换要求 $f$ 在整条直线上（绝对）可积。像 $t\ge0$ 上的 $\mathrm{e}^{t}$ 或 $\sin t$ 这类初值问题中典型的函数就不满足这一要求；乘以衰减因子 $\mathrm{e}^{-\sigma t}$ 并限制在 $t\ge0$ 上，就弥补了这一点。结果就是 Laplace 变换，它能处理增长的函数，并把初始条件纳入变换之中。

### 6.5.1. 定义与性质

称 $f\colon[0,\infty)\to\mathbb{C}$ 为 $\sigma_0$ 指数阶的，是指它分段连续，且存在常数 $M$ 使 $\lvert f(t)\rvert\le M\mathrm{e}^{\sigma_0t}$ 对所有 $t\ge0$ 成立。

**定义 6.5.1（Laplace 变换）** 设 $f$ 是 $\sigma_0$ 指数阶的。复变量 $s$ 的函数

$$
F(s)=\mathscr{L}\{f\}(s)=\int_0^\infty f(t)\,\mathrm{e}^{-st}\,\mathrm{d}t,\qquad\operatorname{Re}s>\sigma_0,\tag{6.11}
$$
称为 $f$ 的 **Laplace 变换**。

对 $s=\sigma+\mathrm{i}\omega$，$\sigma>\sigma_0$，$F(\sigma+\mathrm{i}\omega)$ 是 $H(t)f(t)\mathrm{e}^{-\sigma t}$（关于 $\omega$）的 Fourier 变换：Laplace 变换就是经过衰减的单边函数的 Fourier 变换，只是看作复频率 $s$ 的函数。

**定理 6.5.1** 若 $f$ 是 $\sigma_0$ 指数阶的，则积分 (6.11) 在 $\operatorname{Re}s>\sigma_0$ 时绝对收敛，$F$ 是这个半平面上的**解析函数**，$F'(s)=-\mathscr{L}\{tf(t)\}(s)$，且当 $\operatorname{Re}s\to+\infty$ 时 $F(s)\to0$。

**证明** 对 $\operatorname{Re}s=\sigma>\sigma_0$，$\lvert f(t)\mathrm{e}^{-st}\rvert\le M\mathrm{e}^{-(\sigma-\sigma_0)t}$ 可积，且 $\lvert F(s)\rvert\le\frac{M}{\sigma-\sigma_0}\to0$。在每个半平面 $\operatorname{Re}s\ge\sigma_1>\sigma_0$ 上，被积函数及其对 $s$ 的导数 $-tf(t)\mathrm{e}^{-st}$ 分别被 $M\mathrm{e}^{-(\sigma_1-\sigma_0)t}$ 与 $Mt\mathrm{e}^{-(\sigma_1-\sigma_0)t}$ 控制，所以积分一致收敛，可以在积分号下对 $s$ 求导；复导数存在且等于 $-\mathscr{L}\{tf\}$。$\square$

**定理 6.5.2** 设 $f,g$ 是指数阶的，记 $F=\mathscr{L}\{f\}$，$G=\mathscr{L}\{g\}$。

1. （求导）若 $f$ 连续且 $f'$ 是指数阶的，则 $\mathscr{L}\{f'\}=sF(s)-f(0)$；从而 $\mathscr{L}\{f''\}=s^2F(s)-sf(0)-f'(0)$；
2. （积分）$\mathscr{L}\big\{\int_0^tf(\tau)\,\mathrm{d}\tau\big\}=\frac{F(s)}s$；
3. （关于 $s$ 的平移）$\mathscr{L}\{\mathrm{e}^{at}f(t)\}=F(s-a)$；
4. （延迟）对 $a>0$，$\mathscr{L}\{H(t-a)f(t-a)\}=\mathrm{e}^{-as}F(s)$；
5. （卷积）记 $(f*g)(t)=\int_0^tf(t-\tau)g(\tau)\,\mathrm{d}\tau$，则 $\mathscr{L}\{f*g\}=F(s)G(s)$。

**证明** 1：分部积分得 $\int_0^Rf'\mathrm{e}^{-st}\,\mathrm{d}t=f(R)\mathrm{e}^{-sR}-f(0)+s\int_0^Rf\mathrm{e}^{-st}\,\mathrm{d}t$，当 $\operatorname{Re}s$ 充分大时 $f(R)\mathrm{e}^{-sR}\to0$。2 由对 $\int_0^tf$ 应用 1 得到。3 与 4 是变量代换。5 是对函数 $H(t)f(t)\mathrm{e}^{-\sigma t}$ 与 $H(t)g(t)\mathrm{e}^{-\sigma t}$ 应用卷积定理（定理 6.2.4），它们在 $\mathbb{R}$ 上的卷积为 $H(t)(f*g)(t)\mathrm{e}^{-\sigma t}$。$\square$

性质 1 是使用 Laplace 变换的原因：常系数线性常微分方程连同其初始条件变成了关于 $F$ 的一个代数方程。5 中的卷积是单边卷积；对在 $t<0$ 上为零的函数，它与定义 6.2.2 一致。

| $f(t)$，$t>0$ | $F(s)$ | 区域 |
|---|---|---|
| $1$ | $\dfrac1s$ | $\operatorname{Re}s>0$ |
| $t^n$（$n\in\mathbb{N}$） | $\dfrac{n!}{s^{n+1}}$ | $\operatorname{Re}s>0$ |
| $t^\alpha$（$\alpha>-1$） | $\dfrac{\Gamma(\alpha+1)}{s^{\alpha+1}}$ | $\operatorname{Re}s>0$ |
| $\mathrm{e}^{at}$ | $\dfrac1{s-a}$ | $\operatorname{Re}s>\operatorname{Re}a$ |
| $\cos\omega t$，$\sin\omega t$ | $\dfrac{s}{s^2+\omega^2}$，$\dfrac{\omega}{s^2+\omega^2}$ | $\operatorname{Re}s>0$ |
| $\operatorname{erfc}\dfrac{a}{2\sqrt t}$（$a>0$） | $\dfrac{\mathrm{e}^{-a\sqrt s}}{s}$ | $\operatorname{Re}s>0$ |
| $\dfrac{a}{2\sqrt\pi\,t^{3/2}}\mathrm{e}^{-a^2/(4t)}$（$a>0$） | $\mathrm{e}^{-a\sqrt s}$ | $\operatorname{Re}s>0$ |

$t^\alpha$ 一行在代换 $st=u$ 后就是定义 **Gamma 函数**的积分（对复数 $s$，由实数 $s$ 解析延拓）；最后两行中的 $\sqrt s$ 取主值支。$-1<\alpha<0$ 时函数 $t^\alpha$ 在 $0$ 处不是分段连续的，但 (6.11) 仍然收敛。

### 6.5.2. 反演：Bromwich 积分

**定理 6.5.3（Bromwich 反演公式）** 设 $f$ 是 $\sigma_0$ 指数阶的，且在每个有界区间上分段光滑，$\gamma>\sigma_0$。则当 $t>0$ 时，

$$
\frac{f(t^+)+f(t^-)}2=\frac1{2\pi\mathrm{i}}\lim_{R\to\infty}\int_{\gamma-\mathrm{i}R}^{\gamma+\mathrm{i}R}F(s)\,\mathrm{e}^{st}\,\mathrm{d}s,\tag{6.12}
$$
其中积分沿竖直直线 $\operatorname{Re}s=\gamma$ 进行。当 $t<0$ 时右边等于 $0$。

**证明** 函数 $g(t)=H(t)f(t)\mathrm{e}^{-\gamma t}$ 在 $\mathbb{R}$ 上绝对可积且分段光滑，$\hat g(\omega)=\int_0^\infty f(t)\mathrm{e}^{-(\gamma+\mathrm{i}\omega)t}\,\mathrm{d}t=F(\gamma+\mathrm{i}\omega)$。由定理 6.3.1 的第 2 条，

$$
\frac{g(t^+)+g(t^-)}2=\frac1{2\pi}\lim_{R\to\infty}\int_{-R}^RF(\gamma+\mathrm{i}\omega)\,\mathrm{e}^{\mathrm{i}\omega t}\,\mathrm{d}\omega.
$$
两边乘以 $\mathrm{e}^{\gamma t}$，并作代换 $s=\gamma+\mathrm{i}\omega$，$\mathrm{d}s=\mathrm{i}\,\mathrm{d}\omega$。$\square$

(6.12) 中的积分称为 Bromwich 积分（Bromwich integral），直线 $\operatorname{Re}s=\gamma$ 称为 Bromwich 围道。它的值与 $\gamma>\sigma_0$ 的选取无关：由 **Cauchy 积分定理**，两条这样的直线可以用水平线段连接，而水平线段的贡献趋于零。实际计算时，向左闭合围道（$t>0$ 时因子 $\mathrm{e}^{st}$ 在左边很小），用**留数定理**求积分。

**定理 6.5.4（用留数反演）** 设 $F=\mathscr{L}\{f\}$ 可以延拓为除有限个孤立奇点 $s_1,\dots,s_N$ 外在 $\mathbb{C}$ 上解析的函数，且当 $R\to\infty$ 时 $\max_{\lvert s\rvert=R}\lvert F(s)\rvert\to0$。则当 $t>0$ 时，在 $f$ 的连续点处，

$$
f(t)=\sum_{k=1}^N\operatorname{Res}\big(F(s)\mathrm{e}^{st},s_k\big).
$$

**证明**（概要。）取 $\gamma$ 位于所有 $s_k$ 的右侧，用圆周 $\lvert s-\gamma\rvert=R$ 在 $\operatorname{Re}s<\gamma$ 中的弧 $C_R$ 把从 $\gamma-\mathrm{i}R$ 到 $\gamma+\mathrm{i}R$ 的线段闭合起来。当 $R$ 很大时，闭围道包围了所有奇点，由留数定理 $\frac1{2\pi\mathrm{i}}\big(\int_{\text{线段}}+\int_{C_R}\big)F\mathrm{e}^{st}\,\mathrm{d}s=\sum_k\operatorname{Res}(F\mathrm{e}^{st},s_k)$。在 $C_R$ 上 $\lvert\mathrm{e}^{st}\rvert=\mathrm{e}^{t\operatorname{Re}s}$，把 Jordan 引理（[2.3.7](/2.3.7)）旋转四分之一圈，可知 $t>0$ 时 $\int_{C_R}F\mathrm{e}^{st}\,\mathrm{d}s\to0$。令 $R\to\infty$ 并利用 (6.12) 即得结论。$\square$

对 $\deg P<\deg Q$ 的有理函数 $F=P/Q$，定理的假设成立。若所有极点都是单极点，则 $\operatorname{Res}(F\mathrm{e}^{st},s_k)=\frac{P(s_k)}{Q'(s_k)}\mathrm{e}^{s_kt}$，$f(t)=\sum_k\frac{P(s_k)}{Q'(s_k)}\mathrm{e}^{s_kt}$，这与把 $F$ 的**部分分式**逐项反演相同。每个极点 $s_k$ 贡献一个模态 $\mathrm{e}^{s_kt}$：左半平面的极点给出衰减的模态，虚轴上的极点给出振荡，$m$ 阶极点则产生因子 $t^{m-1}$。

**例 6.5.1** 求 $F(s)=\dfrac1{s(s+1)^2}$ 的逆变换。

**解** 极点 $s=0$ 是单极点，留数为 $\frac{\mathrm{e}^{st}}{(s+1)^2}\big|_{s=0}=1$。极点 $s=-1$ 是二阶极点，留数为 $\frac{\mathrm{d}}{\mathrm{d}s}\frac{\mathrm{e}^{st}}{s}\big|_{s=-1}=\big(\frac{t}{s}-\frac1{s^2}\big)\mathrm{e}^{st}\big|_{s=-1}=-(t+1)\mathrm{e}^{-t}$。因此 $f(t)=1-(1+t)\mathrm{e}^{-t}$。

### 6.5.3. 应用

**例 6.5.2（共振）** 求解**初值问题** $y''+y=\sin t$，$y(0)=y'(0)=0$。

**解** 由定理 6.5.2，$(s^2+1)Y(s)=\frac{1}{s^2+1}$，所以 $Y=\frac1{(s^2+1)^2}$，在 $\pm\mathrm{i}$ 处有二阶极点。在 $s=\mathrm{i}$ 处，

$$
\operatorname{Res}\Big(\frac{\mathrm{e}^{st}}{(s-\mathrm{i})^2(s+\mathrm{i})^2},\mathrm{i}\Big)=\frac{\mathrm{d}}{\mathrm{d}s}\frac{\mathrm{e}^{st}}{(s+\mathrm{i})^2}\Big|_{s=\mathrm{i}}=\frac{t\mathrm{e}^{\mathrm{i}t}}{(2\mathrm{i})^2}-\frac{2\mathrm{e}^{\mathrm{i}t}}{(2\mathrm{i})^3}=-\frac{t\mathrm{e}^{\mathrm{i}t}}4-\frac{\mathrm{i}\,\mathrm{e}^{\mathrm{i}t}}{4},
$$
而在 $-\mathrm{i}$ 处的留数是它的复共轭（因为 $Y$ 在实轴上取实值）。相加得

$$
y(t)=2\operatorname{Re}\Big(-\frac{t\mathrm{e}^{\mathrm{i}t}}4-\frac{\mathrm{i}\,\mathrm{e}^{\mathrm{i}t}}{4}\Big)=\frac{\sin t-t\cos t}2.
$$
外力频率等于固有频率，二阶极点产生因子 $t$，振幅线性增长：这就是共振。

**例 6.5.3（一端加热的半无界杆）** 杆 $x>0$ 的初始温度为 $0$，从 $0$ 时刻起端点保持恒温 $T_0$：

$$
u_t=k u_{xx}\ (x>0,\ t>0),\qquad u(x,0)=0,\qquad u(0,t)=T_0,\qquad u\text{ 有界}.
$$

**解** 关于 $t$ 作变换，记 $U(x,s)=\mathscr{L}\{u(x,\cdot)\}(s)$。由定理 6.5.2 与 $u(x,0)=0$，$sU=k U_{xx}$，所以 $U=A(s)\mathrm{e}^{-x\sqrt{s/k}}+B(s)\mathrm{e}^{x\sqrt{s/k}}$，平方根取主值支（$\operatorname{Re}\sqrt s>0$）。关于 $x$ 的有界性迫使 $B=0$，而 $U(0,s)=T_0/s$ 给出

$$
U(x,s)=T_0\frac{\mathrm{e}^{-x\sqrt{s/k}}}{s}.
$$
由变换表（取 $a=x/\sqrt k$），

$$
u(x,t)=T_0\operatorname{erfc}\Big(\frac{x}{2\sqrt{k t}}\Big).
$$
可以直接验证这个函数满足方程和条件。这里 $F$ 在 $s=0$ 处有支点，所以定理 6.5.4 不适用；表中的反演是通过把 Bromwich 围道变形为绕过负实轴上支割线的围道得到的。热量渗透的深度为 $\sqrt{k t}$ 量级，所以深度加倍需要四倍的时间。若端点温度是函数 $h(t)$ 而不是 $T_0$，则 $U=\mathscr{L}\{h\}\cdot\mathrm{e}^{-x\sqrt{s/k}}$，由卷积法则和变换表的最后一行得

$$
u(x,t)=\int_0^th(\tau)\,\frac{x}{2\sqrt{\pi k}\,(t-\tau)^{3/2}}\,\mathrm{e}^{-x^2/(4k(t-\tau))}\,\mathrm{d}\tau.
$$

## 小结

| | Fourier 变换 | Laplace 变换 |
|---|---|---|
| 定义 | $\hat f(\xi)=\int_{\mathbb{R}}f(x)\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x$ | $F(s)=\int_0^\infty f(t)\mathrm{e}^{-st}\,\mathrm{d}t$ |
| 函数类 | $\mathbb{R}$ 上绝对（或平方）可积 | $[0,\infty)$ 上指数阶 |
| 反演 | $f=\frac1{2\pi}\int_{\mathbb{R}}\hat f(\xi)\mathrm{e}^{\mathrm{i}\xi x}\,\mathrm{d}\xi$ | $f=\frac1{2\pi\mathrm{i}}\int_{\gamma-\mathrm{i}\infty}^{\gamma+\mathrm{i}\infty}F(s)\mathrm{e}^{st}\,\mathrm{d}s$，用留数计算 |
| 导数 | $f'\mapsto\mathrm{i}\xi\hat f$ | $f'\mapsto sF-f(0)$ |
| 卷积 | $\int_{\mathbb{R}}f(x-y)g(y)\,\mathrm{d}y\mapsto\hat f\hat g$ | $\int_0^tf(t-\tau)g(\tau)\,\mathrm{d}\tau\mapsto FG$ |
| 典型用途 | $\mathbb{R}$ 上的空间变量：热方程、波动方程、Laplace 方程 | 带初始数据的时间变量：常微分方程、半无界问题 |

重要的变换对：$\mathrm{e}^{-ax^2}\mapsto\sqrt{\pi/a}\,\mathrm{e}^{-\xi^2/(4a)}$；$\mathrm{e}^{-a\lvert x\rvert}\mapsto\frac{2a}{a^2+\xi^2}$；$\boldsymbol{1}_{[-a,a]}\mapsto\frac{2\sin a\xi}{\xi}$；$\frac{a}{\pi(a^2+x^2)}\mapsto\mathrm{e}^{-a\lvert\xi\rvert}$。重要的事实：$f$ 的光滑性 $\leftrightarrow$ $\hat f$ 的衰减；Plancherel 定理 $\int\lvert f\rvert^2=\frac1{2\pi}\int\lvert\hat f\rvert^2$；不确定性原理 $\sigma_x\sigma_\xi\ge\frac12$。
