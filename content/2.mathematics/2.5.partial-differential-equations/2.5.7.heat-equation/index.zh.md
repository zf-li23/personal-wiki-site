---
title: 热方程
source_hash: 09f7acd73bfa
---

**热方程** $u_t=k\Delta u$（扩散系数 $k>0$，[2.5.1](/2.5.1)）支配着一切由随机的局部运动引起扩散的过程：固体中的热量、溶剂中的溶质、移动的生物种群、Brown 粒子的概率密度。它的解与**波动方程**（[2.5.3](/2.5.3)）的解表现迥异：热量瞬间传遍整个空间，但到达远处的量极小；粗糙的初始数据立即变得光滑；时间有方向，因为方程一般不能逆向求解；解通过极值原理由它在"抛物边界"上的值所控制。

在 [2.5.6](/2.5.6) 中，Fourier 变换给出了热核以及直线上的解的公式。本章在 $\mathbb{R}^n$ 中为它们建立严格的基础（§7.1）；证明极值原理，并结合能量法得到有界区域上的唯一性与稳定性（§7.2）；用反射法求解半直线上的问题（§7.3），用齐次化原理求解非齐次问题（§7.4）；最后从概率的角度解释扩散，并介绍反应扩散方程——生物学中空间斑图的基本模型（§7.5，在[生态学](/7.19)与[发育生物学](/7.5)中继续讨论）。有界区间上的级数解法已在 [2.5.4](/2.5.4) 和 [2.5.5](/2.5.5) 中讨论过。

## 7.1. 热核

### 7.1.1. 基本解

热核也可以不用 Fourier 变换，而由对称性求出。若 $u(x,t)$ 满足 $u_t=k u_{xx}$，则对每个 $\lambda>0$，$u(\lambda x,\lambda^2t)$ 也满足：空间按时间的平方根伸缩。此外总热量 $\int u\,\mathrm{d}x$ 守恒。因此描述在原点释放的单位热量的解应当具有自相似形式 $u=t^{-1/2}v(\eta)$，$\eta=x/\sqrt t$，它保持 $\int u\,\mathrm{d}x=\int v\,\mathrm{d}\eta$ 不变。代入得

$$
u_t=-\frac{1}{2t^{3/2}}\big(v+\eta v'\big),\qquad u_{xx}=\frac{1}{t^{3/2}}v'',
$$
所以 $k v''+\frac12(\eta v)'=0$，即 $k v'+\frac12\eta v=C$。对在无穷远处衰减的解 $C=0$，$v=A\mathrm{e}^{-\eta^2/(4k)}$。用 **Gauss 积分**把总热量归一化为 1，得 $A=(4\pi k)^{-1/2}$，这就是 [2.5.6](/2.5.6) 的热核 (6.8)。在 $\mathbb{R}^n$ 中，Laplace 算子是对各个变量的二阶导数之和，关于 $x_1,\dots,x_n$ 的一维热核之积满足热方程。

**定义 7.1.1（热方程的基本解）** 函数

$$
\Phi(x,t)=\frac{1}{(4\pi k t)^{n/2}}\exp\Big(-\frac{\lvert x\rvert^2}{4k t}\Big),\qquad x\in\mathbb{R}^n,\ t>0,\tag{7.1}
$$
称为热方程的**基本解**，或**热核**。

**定理 7.1.1** 热核有以下性质。

1. $\Phi\in C^\infty(\mathbb{R}^n\times(0,\infty))$，且 $\Phi_t=k\Delta\Phi$；
2. $\Phi>0$，且对每个 $t>0$，$\displaystyle\int_{\mathbb{R}^n}\Phi(x,t)\,\mathrm{d}x=1$；
3. 对每个 $\delta>0$，当 $t\to0^+$ 时 $\displaystyle\int_{\lvert x\rvert\ge\delta}\Phi(x,t)\,\mathrm{d}x\to0$；
4. （半群性质）对 $t,s>0$，$\Phi(\cdot,t)*\Phi(\cdot,s)=\Phi(\cdot,t+s)$。

**证明** 1：由于 $\ln\Phi=-\frac n2\ln(4\pi k t)-\frac{\lvert x\rvert^2}{4k t}$，

$$
\Phi_t=\Phi\Big(\frac{\lvert x\rvert^2}{4k t^2}-\frac{n}{2t}\Big),\qquad\partial_i\Phi=-\frac{x_i}{2k t}\Phi,\qquad\partial_i^2\Phi=\Phi\Big(\frac{x_i^2}{4k^2t^2}-\frac1{2k t}\Big),
$$
对 $i$ 求和得 $k\Delta\Phi=\Phi\big(\frac{\lvert x\rvert^2}{4k t^2}-\frac n{2t}\big)=\Phi_t$。

2 与 3：作代换 $x=\sqrt{4k t}\,z$，则 $\int_{\lvert x\rvert\ge\delta}\Phi\,\mathrm{d}x=\pi^{-n/2}\int_{\lvert z\rvert\ge\delta/\sqrt{4k t}}\mathrm{e}^{-\lvert z\rvert^2}\,\mathrm{d}z$。当 $\delta=0$ 时，由 Gauss 积分它等于 1；当 $\delta>0$ 时，它是一个收敛积分的尾部，其下限在 $t\to0^+$ 时趋于无穷。

4：由 (6.4) 的 $n$ 维形式（[2.5.6](/2.5.6#sec-6.2.5)），$\hat\Phi(\xi,t)=\mathrm{e}^{-k\lvert\xi\rvert^2t}$。由**卷积定理**，左边的变换为 $\mathrm{e}^{-k\lvert\xi\rvert^2t}\mathrm{e}^{-k\lvert\xi\rvert^2s}=\hat\Phi(\xi,t+s)$，而两边都连续且绝对可积，由唯一性（推论 6.3.1）二者相等。$\square$

性质 2 与 3 说明，当 $t\to0^+$ 时 $\Phi(\cdot,t)$ 是近似单位元（引理 6.3.1，取 $\varepsilon=\sqrt t$）：基本解的初始数据是 **δ 函数**，即单位点热源。性质 4 说明，先扩散时间 $t$、再扩散时间 $s$，等同于扩散时间 $t+s$。

![左：四个时刻的热核；总质量保持为 1，宽度按 sqrt(t) 增长。右：矩形的初始温度被瞬间光滑化并向外扩展](./plots/heat-kernel.py)

### 7.1.2. Cauchy 问题的解

**定理 7.1.2** 设 $\varphi$ 在 $\mathbb{R}^n$ 上连续有界，定义

$$
u(x,t)=\int_{\mathbb{R}^n}\Phi(x-y,t)\,\varphi(y)\,\mathrm{d}y=\frac{1}{(4\pi k t)^{n/2}}\int_{\mathbb{R}^n}\mathrm{e}^{-\lvert x-y\rvert^2/(4k t)}\varphi(y)\,\mathrm{d}y,\qquad t>0.\tag{7.2}
$$
则

1. $u\in C^\infty(\mathbb{R}^n\times(0,\infty))$，且 $t>0$ 时 $u_t=k\Delta u$；
2. 对每个 $x_0\in\mathbb{R}^n$，当 $(x,t)\to(x_0,0^+)$ 时 $u(x,t)\to\varphi(x_0)$；
3. $\inf\varphi\le u\le\sup\varphi$。

因此，令 $u(x,0)=\varphi(x)$ 延拓后，$u$ 是 Cauchy 问题 $u_t=k\Delta u$，$u(x,0)=\varphi(x)$ 在 $\mathbb{R}^n\times[0,\infty)$ 上连续的解。

**证明** 1：$\Phi(x-y,t)$ 关于 $x$ 与 $t$ 的每个偏导数都是 $\Phi(x-y,t)$ 乘以一个关于 $x-y$ 与 $1/t$ 的多项式。因此当 $\lvert x\rvert\le A$、$t_0\le t\le T$（$0<t_0<T$）时，对 $\lvert y\rvert\ge A$，它不超过 $C(1+\lvert y\rvert^m)\mathrm{e}^{-(\lvert y\rvert-A)^2/(4k T)}$，这是 $y$ 的可积函数；由于 $\varphi$ 有界，求导后的积分在这个集合上一致收敛。所以可以任意阶地**积分号下求导**，由定理 7.1.1 得 $u_t-k\Delta u=\int(\Phi_t-k\Delta\Phi)(x-y,t)\varphi(y)\,\mathrm{d}y=0$。

2：设 $\lvert\varphi\rvert\le M$，$\varepsilon>0$，取 $\delta>0$ 使 $\lvert y-x_0\rvert<\delta$ 时 $\lvert\varphi(y)-\varphi(x_0)\rvert<\varepsilon$。由定理 7.1.1 的第 2 条，

$$
\lvert u(x,t)-\varphi(x_0)\rvert\le\int_{\mathbb{R}^n}\Phi(x-y,t)\,\lvert\varphi(y)-\varphi(x_0)\rvert\,\mathrm{d}y.
$$
设 $\lvert x-x_0\rvert<\delta/2$。在 $\lvert y-x_0\rvert<\delta$ 上，被积函数小于 $\varepsilon\Phi$，贡献不超过 $\varepsilon$。在 $\lvert y-x_0\rvert\ge\delta$ 上，$\lvert x-y\rvert\ge\delta/2$，所以这部分的贡献不超过 $2M\int_{\lvert z\rvert\ge\delta/2}\Phi(z,t)\,\mathrm{d}z$，由定理 7.1.1 的第 3 条，当 $t$ 很小时它小于 $\varepsilon$。

3：$u(x,t)$ 是 $\varphi$ 的值以总质量为 1 的正权 $\Phi(x-\cdot,t)$ 所作的平均。$\square$

公式 (7.2) 有时称为热方程的 Poisson 公式。Cauchy 问题的有界解是唯一的，所以 (7.2) 就是唯一的有界解。没有增长条件时唯一性不成立：Tychonoff 构造了 $\mathbb{R}\times(0,\infty)$ 上的一个解，它不恒为零，当 $t\to0^+$ 时趋于 $0$，并且对每个 $a$ 都比 $\mathrm{e}^{ax^2}$ 增长得快。在函数类 $\lvert u(x,t)\rvert\le M\mathrm{e}^{a\lvert x\rvert^2}$ 中唯一性成立（不加证明）；这样的条件排除了物理上不合理的解。

### 7.1.3. 定性性质

公式 (7.2) 显示了扩散的典型特征。

1. 无穷传播速度：若 $\varphi\ge0$ 且 $\varphi\not\equiv0$，则由于 $\Phi$ 处处为正，对所有 $x$ 和所有 $t>0$ 有 $u(x,t)>0$。在小区域内释放的热量立即在任何距离处被感受到，尽管其数量只有 $\mathrm{e}^{-\lvert x\rvert^2/(4k t)}$ 量级。热方程是一种理想化，它忽略了底层分子运动的有限速度；在宏观尺度上这一误差可以忽略。
2. 光滑化：即使 $\varphi$ 只是有界连续（或分段连续）的，解在 $t>0$ 时也无穷次可微。用 Fourier 的语言说，每个频率都乘以 $\mathrm{e}^{-k\lvert\xi\rvert^2t}$，高频立即被消灭。
3. 衰减：若 $\varphi$ 绝对可积，则 $\lvert u(x,t)\rvert\le\sup_y\Phi(y,t)\int\lvert\varphi\rvert=(4\pi k t)^{-n/2}\int\lvert\varphi\rvert$，而总热量 $\int u\,\mathrm{d}x=\int\varphi\,\mathrm{d}x$ 守恒：热量散布在直径为 $\sqrt{k t}$ 量级的区域上。
4. 不可逆性：逆向问题在 Hadamard 意义下是不适定的（[2.5.1](/2.5.1)）。在直线上，函数 $u_n(x,t)=\frac1n\mathrm{e}^{k n^2(T-t)}\sin nx$ 满足热方程，终值为 $u_n(x,T)=\frac1n\sin nx$，当 $n\to\infty$ 时一致趋于 $0$，而它在 $t=0$ 时的振幅 $\frac1n\mathrm{e}^{k n^2T}\to\infty$。当前温度任意小的变化对应于过去温度任意大的变化：精细细节中的信息被扩散破坏了。

**例 7.1.1** 设 $n=1$，$\varphi(x)=\mathrm{e}^{-x^2/(2\sigma^2)}$。由 (6.4)，$\hat\varphi=\sigma\sqrt{2\pi}\,\mathrm{e}^{-\sigma^2\xi^2/2}$，$\hat u=\hat\varphi\,\mathrm{e}^{-k\xi^2t}=\sigma\sqrt{2\pi}\,\mathrm{e}^{-(\sigma^2+2k t)\xi^2/2}$。再用 (6.4) 反演，

$$
u(x,t)=\frac{\sigma}{\sqrt{\sigma^2+2k t}}\exp\Big(-\frac{x^2}{2(\sigma^2+2k t)}\Big).
$$
Gauss 形的温度分布保持为 Gauss 形；它的方差线性增长，$\sigma^2\mapsto\sigma^2+2k t$，高度则相应下降，使面积守恒。用概率的语言说（§7.5），与 $\Phi(\cdot,t)$ 作卷积相当于加上一个方差为 $2k t$ 的独立正态变量。

## 7.2. 极值原理

### 7.2.1. 弱极值原理

在有界区域上，物体内部在一段时间内的温度不会超过初始温度与边界上所加温度中的较大者：热量从热处流向冷处，不会产生新的极值。

设 $\Omega\subset\mathbb{R}^n$ 是有界区域，$T>0$。记 $Q_T=\Omega\times(0,T]$ 为时空柱体，其闭包为 $\bar Q_T=\bar\Omega\times[0,T]$。

**定义 7.2.1（抛物边界）** 集合

$$
\Gamma_T=\big(\bar\Omega\times\{0\}\big)\cup\big(\partial\Omega\times[0,T]\big)
$$
称为 $Q_T$ 的**抛物边界**：它由柱体的底面和侧面组成，不含顶面 $\Omega\times\{T\}$。

这恰好是热方程给定数据（初始条件与边界条件）的那部分边界；在终止时刻不加任何条件。

**定理 7.2.1（弱极值原理）** 设 $u\in C(\bar Q_T)$ 在 $Q_T$ 内有连续的导数 $u_t$、$u_{x_ix_j}$，且在 $Q_T$ 内 $u_t-k\Delta u\le0$。则

$$
\max_{\bar Q_T}u=\max_{\Gamma_T}u.
$$
同样，若 $u_t-k\Delta u\ge0$，则 $\min_{\bar Q_T}u=\min_{\Gamma_T}u$。特别地，热方程的解在抛物边界上取到最大值与最小值。

**证明** 先设具有同样正则性的函数 $v$ 在 $Q_T$ 内满足严格不等式 $v_t-k\Delta v<0$，并设 $v$ 在紧集 $\bar Q_T$ 上的最大值在 $(x_0,t_0)$ 处取到。若 $(x_0,t_0)\notin\Gamma_T$，则 $x_0\in\Omega$，$0<t_0\le T$。由于 $x\mapsto v(x,t_0)$ 在内点 $x_0$ 处取最大值，每个 $v_{x_ix_i}(x_0,t_0)\le0$，故 $\Delta v(x_0,t_0)\le0$。由于 $t\mapsto v(x_0,t)$ 在 $(0,t_0]$ 上于 $t_0$ 处取最大值，$v_t(x_0,t_0)\ge0$（$t_0<T$ 时等号成立；$t_0=T$ 时理解为单侧导数）。于是在 $(x_0,t_0)$ 处 $v_t-k\Delta v\ge0$，矛盾。因此 $\max_{\bar Q_T}v=\max_{\Gamma_T}v$。

一般情形，设 $\varepsilon>0$，令 $v=u+\varepsilon\lvert x\rvert^2$。则 $v_t-k\Delta v=u_t-k\Delta u-2nk\varepsilon<0$。记 $R=\max_{x\in\bar\Omega}\lvert x\rvert$，

$$
\max_{\bar Q_T}u\le\max_{\bar Q_T}v=\max_{\Gamma_T}v\le\max_{\Gamma_T}u+\varepsilon R^2,
$$
令 $\varepsilon\to0$ 得 $\max_{\bar Q_T}u\le\max_{\Gamma_T}u$；反向不等式是显然的。对 $-u$ 应用这一结论即得关于最小值的结论。$\square$

之所以需要严格不等式的技巧，是因为在内部最大值点处只知道 $\Delta u\le0$ 与 $u_t\ge0$，当二者都为零时这与 $u_t=k\Delta u$ 并不矛盾。更强的结论也成立（不加证明）：若 $\Omega$ 连通，且解在 $\bar Q_T$ 上的最大值在某点 $(x_0,t_0)$ 处取到，$x_0\in\Omega$，$0<t_0\le T$，则 $u$ 在 $\bar\Omega\times[0,t_0]$ 上为常数（强极值原理）。未来不能影响过去，所以对 $t>t_0$ 不作任何断言。

### 7.2.2. 唯一性、稳定性与比较

考虑初边值问题

$$
\begin{cases}
u_t-k\Delta u=f(x,t),&(x,t)\in Q_T,\\
u=g(x,t),&x\in\partial\Omega,\ 0\le t\le T,\\
u(x,0)=\varphi(x),&x\in\bar\Omega.
\end{cases}\tag{7.3}
$$

**推论 7.2.1（唯一性与稳定性）** 问题 (7.3) 至多有一个解 $u\in C(\bar Q_T)$，它在 $Q_T$ 内有连续的 $u_t$、$u_{x_ix_j}$。若 $u_1,u_2$ 分别是数据为 $(f,g_1,\varphi_1)$ 与 $(f,g_2,\varphi_2)$ 的解，则

$$
\max_{\bar Q_T}\lvert u_1-u_2\rvert\le\max\Big\{\max_{\bar\Omega}\lvert\varphi_1-\varphi_2\rvert,\ \max_{\partial\Omega\times[0,T]}\lvert g_1-g_2\rvert\Big\}.
$$

**证明** 差 $w=u_1-u_2$ 满足 $w_t-k\Delta w=0$，由定理 7.2.1，$w$ 与 $-w$ 在 $\bar Q_T$ 上都不超过它们在 $\Gamma_T$ 上的最大值，而在 $\Gamma_T$ 上 $w$ 等于 $\varphi_1-\varphi_2$ 或 $g_1-g_2$。这就是所要的估计；数据相同时得 $w\equiv0$。$\square$

结合解的存在性（[2.5.4](/2.5.4) 中用级数给出，或一般情形），这说明热方程的 Dirichlet 问题是适定的：初始温度和边界温度的小误差只引起解的小误差，而且关于空间和时间一致。对 $v-u$ 应用同样的论证，就得到比较原理。

**推论 7.2.2（比较原理）** 若在 $Q_T$ 内 $u_t-k\Delta u\le v_t-k\Delta v$，且在 $\Gamma_T$ 上 $u\le v$，则在 $\bar Q_T$ 中 $u\le v$。

**例 7.2.1** 设 $u$ 在 $(0,\pi)$ 上满足 $u_t=u_{xx}$，$u(0,t)=u(\pi,t)=0$，$u(x,0)=x(\pi-x)$。不求解，估计 $u$。

**解** 函数 $v=A\mathrm{e}^{-t}\sin x$ 满足同一方程，且在 $x=0,\pi$ 处为零。比值 $\frac{x(\pi-x)}{\sin x}$ 从 $\pi$（它在 $x=0^+$ 处的极限）递减到 $x=\frac\pi2$ 处的 $\frac{\pi^2}4$，并且关于 $\frac\pi2$ 对称，所以在 $[0,\pi]$ 上 $\frac{\pi^2}4\sin x\le x(\pi-x)\le\pi\sin x$。由推论 7.2.2，

$$
\frac{\pi^2}{4}\mathrm{e}^{-t}\sin x\le u(x,t)\le\pi\,\mathrm{e}^{-t}\sin x.
$$
精确解 $u=\sum_{n\text{ 为奇数}}\frac{8}{\pi n^3}\mathrm{e}^{-n^2t}\sin nx$ 的首项系数为 $\frac8\pi\approx2.55$，确实介于 $\frac{\pi^2}4\approx2.47$ 与 $\pi\approx3.14$ 之间。

### 7.2.3. 能量法

对 Neumann 问题，极值原理不能直接控制边界值，但一个积分恒等式可以。设 $u$ 在 $\Omega\times(0,T]$ 中满足 $u_t=k\Delta u$，在 $\partial\Omega$ 上 $u=0$ 或 $\frac{\partial u}{\partial\boldsymbol{n}}=0$，令

$$
E(t)=\int_\Omega u(x,t)^2\,\mathrm{d}x.
$$
积分号下求导并应用 **Green 第一公式**，

$$
E'(t)=2\int_\Omega uu_t\,\mathrm{d}x=2k\int_\Omega u\,\Delta u\,\mathrm{d}x=2k\oint_{\partial\Omega}u\frac{\partial u}{\partial\boldsymbol{n}}\,\mathrm{d}S-2k\int_\Omega\lvert\nabla u\rvert^2\,\mathrm{d}x=-2k\int_\Omega\lvert\nabla u\rvert^2\,\mathrm{d}x\le0.
$$
因此 $E(t)\le E(0)$。把它应用于数据相同的两个解之差，就证明了 Dirichlet 问题与 Neumann 问题（以及 $\beta\ge0$ 时的 Robin 条件 $\frac{\partial u}{\partial\boldsymbol{n}}+\beta u=0$）解的唯一性，以及均方意义下的稳定性。对 Dirichlet 问题，衰减还可以定量化：$-\Delta$ 的第一 Dirichlet 特征值 $\lambda_1$（[2.5.5](/2.5.5#sec-5.1.2)）是商 $\int\lvert\nabla w\rvert^2/\int w^2$ 在 $\partial\Omega$ 上为零的函数中的最小值（不加证明），所以 $E'\le-2k\lambda_1E$，

$$
E(t)\le E(0)\,\mathrm{e}^{-2k\lambda_1t},
$$
这与级数解中衰减最慢的模态 $\mathrm{e}^{-k\lambda_1t}$ 一致。

## 7.3. 半直线上的问题

### 7.3.1. 反射法

在半直线 $x>0$ 上，$x=0$ 处附加条件时，与波动方程（[2.5.3](/2.5.3)）一样，把初始数据延拓到整条直线上，使条件自动成立。

**定理 7.3.1** 设 $\varphi$ 在 $[0,\infty)$ 上有界连续，$\Phi$ 是一维热核。对 $t>0$、$x\ge0$，令

$$
u_{\mathrm{D}}(x,t)=\int_0^\infty\big[\Phi(x-y,t)-\Phi(x+y,t)\big]\varphi(y)\,\mathrm{d}y,\qquad u_{\mathrm{N}}(x,t)=\int_0^\infty\big[\Phi(x-y,t)+\Phi(x+y,t)\big]\varphi(y)\,\mathrm{d}y.
$$
则 $u_{\mathrm{D}}$ 与 $u_{\mathrm{N}}$ 在 $x>0$、$t>0$ 时满足 $u_t=k u_{xx}$，对每个 $x_0>0$，当 $(x,t)\to(x_0,0^+)$ 时趋于 $\varphi(x_0)$，并且当 $t>0$ 时分别满足 $u_{\mathrm{D}}(0,t)=0$ 与 $\partial_xu_{\mathrm{N}}(0,t)=0$。

**证明** 设 $\varphi_{\mathrm{odd}}$ 是 $\varphi$ 在 $\mathbb{R}$ 上的奇延拓（在 $0$ 处的值任意）。把 $\int_{\mathbb{R}}$ 在 $0$ 处拆开，并在 $(-\infty,0)$ 上作代换 $y\mapsto-y$，可知 $u_{\mathrm{D}}(x,t)=\int_{\mathbb{R}}\Phi(x-y,t)\varphi_{\mathrm{odd}}(y)\,\mathrm{d}y$。由定理 7.1.2（其第 1、2 条的证明只用到 $\varphi$ 的有界性与在 $x_0$ 处的连续性）得到方程与初始条件。由于 $\Phi$ 关于 $x$ 是偶函数，代换 $y\mapsto-y$ 表明 $u_{\mathrm{D}}(\cdot,t)$ 是奇函数，因而在 $x=0$ 处为零。对 $u_{\mathrm{N}}$ 用偶延拓；这时 $u_{\mathrm{N}}(\cdot,t)$ 是光滑的偶函数，所以其导数在 $0$ 处为零。$\square$

换句话说，半直线上满足 $u(0,t)=0$ 的解，是直线上以奇函数为数据的解的限制：在 $-y$ 处放一个符号相反的像源，恰好吸收了流过 $x=0$ 的热量。同样的想法用镜像法给出 Laplace 方程的 Green 函数（[2.5.8](/2.5.8)）。

**例 7.3.1** 温度均匀为 $1$ 的半无界杆，从 $0$ 时刻起端点保持为 $0$。取 $\varphi\equiv1$，

$$
u(x,t)=\int_0^\infty\Phi(x-y,t)\,\mathrm{d}y-\int_0^\infty\Phi(x+y,t)\,\mathrm{d}y=\frac12\Big(1+\operatorname{erf}\frac{x}{2\sqrt{k t}}\Big)-\frac12\Big(1-\operatorname{erf}\frac{x}{2\sqrt{k t}}\Big)=\operatorname{erf}\Big(\frac{x}{2\sqrt{k t}}\Big),
$$
其中 $\operatorname{erf}$ 是 [2.5.6](/2.5.6) 的**误差函数**。这与例 6.5.3 互补：那里杆是冷的而端点是热的，而 $T_0-T_0\operatorname{erfc}=T_0\operatorname{erf}$。端点处的温度梯度为 $u_x(0,t)=\frac1{\sqrt{\pi k t}}$。1862 年 Kelvin 把这个公式用于地球的冷却：根据观测到的地表附近温度随深度的增加、几千度的初始温度和岩石的热导率，他估计 $t$ 约为 $10^8$ 年量级。这个估计远远偏小，因为它忽略了放射性产生的热量（当时尚不知道）和地幔中的对流。

![反射法：x > 0 上满足 u(0, t) = 0 与 u(x, 0) = 1 的解，是整条直线上以奇函数为初始数据的解的限制，u = erf(x / (2 sqrt(t)))](./plots/half-line-reflection.py)

### 7.3.2. 随时间变化的边界数据

若边界温度随时间变化，$u(0,t)=h(t)$，$u(x,0)=0$，则 Laplace 变换给出例 6.5.3 末尾的公式：

$$
u(x,t)=\int_0^th(\tau)\,K(x,t-\tau)\,\mathrm{d}\tau,\qquad K(x,t)=\frac{x}{2\sqrt{\pi k}\,t^{3/2}}\mathrm{e}^{-x^2/(4k t)}=-2k\,\partial_x\Phi(x,t).
$$
核 $K$ 是对端点处一个短暂热脉冲的响应。通过叠加与定理 7.3.1 结合，就能求解具有任意初始数据和边界数据的半直线问题。周期性的边界温度 $h=\cos\omega t$（地表温度的日变化或年变化）在暂态消失后产生衰减的波 $\mathrm{e}^{-x\sqrt{\omega/2k}}\cos\big(\omega t-x\sqrt{\omega/2k}\big)$，这可以代入验证：年温度变化渗透的深度约为日变化的 $\sqrt{365}\approx19$ 倍；在深度 $\pi\sqrt{2k/\omega}$ 处（土壤中为几米），年变化的相位相反，那里的地下夏天最冷、冬天最暖。

## 7.4. 非齐次方程与齐次化原理

考虑 $\mathbb{R}^n$ 上带源项的热方程：

$$
u_t-k\Delta u=f(x,t),\quad t>0,\qquad u(x,0)=0.\tag{7.4}
$$
由 **Duhamel 原理**（[2.5.3](/2.5.3)），把在 $[s,s+\mathrm{d}s]$ 内起作用的源看作在 $s$ 时刻给出的初始温度 $f(\cdot,s)\,\mathrm{d}s$。设 $w(x,t;s)$ 在 $t>s$ 时满足齐次方程，且 $w(x,s;s)=f(x,s)$，即 $w(\cdot,t;s)=\Phi(\cdot,t-s)*f(\cdot,s)$。叠加得

$$
u(x,t)=\int_0^tw(x,t;s)\,\mathrm{d}s=\int_0^t\!\!\int_{\mathbb{R}^n}\Phi(x-y,t-s)f(y,s)\,\mathrm{d}y\,\mathrm{d}s.\tag{7.5}
$$

**定理 7.4.1** 设 $f$ 在 $\mathbb{R}^n\times[0,\infty)$ 上有界连续，且有有界连续的导数 $f_t$、$f_{x_i}$、$f_{x_ix_j}$。则 (7.5) 是 (7.4) 的解，在 $\mathbb{R}^n\times[0,\infty)$ 上连续，且 $u(x,0)=0$。$u_t-k\Delta u=f$、$u(x,0)=\varphi(x)$ 的解是 (7.2) 与 (7.5) 之和。

**证明**（概要。）形式上，对 (7.5) 关于上限求导并在积分号下求导，

$$
u_t=w(x,t;t)+\int_0^tw_t(x,t;s)\,\mathrm{d}s=f(x,t)+\int_0^tk\Delta w(x,t;s)\,\mathrm{d}s=f(x,t)+k\Delta u.
$$
困难在于 $\Phi(x-y,t-s)$ 的二阶导数在 $s=t$ 附近不可积。补救的办法是作代换 $y\mapsto x-y$、$s\mapsto t-s$，写成 $u=\int_0^t\int\Phi(y,s)f(x-y,t-s)\,\mathrm{d}y\,\mathrm{d}s$，使所有导数都落在 $f$ 上；然后对 $y$ 分部积分并利用 $\Phi_s=k\Delta\Phi$ 处理 $s=0$ 附近的奇异部分（见 Evans 的教材 §2.3）。由 $\int\Phi=1$ 得到的估计 $\lvert u\rvert\le t\sup\lvert f\rvert$ 给出 $t=0$ 处的连续性。$\square$

其结构与线性常微分方程的**常数变易公式**相同：把齐次问题的解算子作用于此前每个时刻的源项，再积分起来。在有界区间上，同一原理与 [2.5.4](/2.5.4) 的特征函数展开相结合，给出非齐次问题的级数解。

**例 7.4.1** 在 $\mathbb{R}$ 上求解 $u_t=k u_{xx}+\sin x$，$u(x,0)=0$。

**解** 在 $s$ 时刻以 $\sin x$ 为初值的齐次解为 $w(x,t;s)=\mathrm{e}^{-k(t-s)}\sin x$（因为 $\sin x$ 是 $\partial_x^2$ 的特征函数）。由 (7.5)，

$$
u(x,t)=\int_0^t\mathrm{e}^{-k(t-s)}\,\mathrm{d}s\,\sin x=\frac{1-\mathrm{e}^{-k t}}{k}\sin x.
$$
当 $t\to\infty$ 时，$u$ 趋于稳态 $\frac1k\sin x$，即 $-k u''=\sin x$ 的解：源项与扩散损失在时间尺度 $1/k$ 上达到平衡。

## 7.5. 扩散、随机游走与反应扩散方程

### 7.5.1. 热核的概率意义

设直线上的一个粒子每隔 $\tau$ 个时间单位向左或向右跳跃距离 $h$，概率各为 $\frac12$，且与过去无关。在 $t$ 时刻于格点 $x$ 处发现它的概率 $p(x,t)$ 满足

$$
p(x,t+\tau)=\tfrac12p(x-h,t)+\tfrac12p(x+h,t).
$$
用**泰勒公式**展开两边，$\tau p_t+O(\tau^2)=\frac{h^2}2p_{xx}+O(h^4)$。除以 $\tau$，令 $h,\tau\to0$ 并保持 $\frac{h^2}{2\tau}=k$ 不变，得 $p_t=k p_{xx}$：扩散方程是随机游走的连续极限，扩散系数为 $k=h^2/(2\tau)$。

由**中心极限定理**也能得到同样的结论。经过 $n=t/\tau$ 步后，位置是 $n$ 个独立的、均值为 $0$、方差为 $h^2$ 的步长 $\pm h$ 之和，所以近似服从方差为 $nh^2=2k t$ 的正态分布。而 $\mathcal{N}(0,2k t)$ 的密度恰好就是 $\Phi(x,t)$。在极限下随机游走成为 Brown 运动 $B_t$（对应 $k=\frac12$），公式 (7.2) 获得如下意义：

$$
u(x,t)=\mathbb{E}\big[\varphi\big(x+\sqrt{2k}\,B_t\big)\big]:
$$
$x$ 处的温度，是从 $x$ 出发的 Brown 粒子所到达的随机位置上初始温度的平均值。在 $\mathbb{R}^n$ 中，均方位移为 $\mathbb{E}\lvert X_t\rvert^2=2nk t$（Einstein 关系），扩散距离 $L$ 所需的时间为 $L^2/k$ 量级。

![左：步长 h = 0.1、每隔 tau = 0.005 跳跃一次的随机游走的样本路径大多位于 ±2 sqrt(2 k t) 之内。右：50000 个粒子在三个时刻的直方图与 k = h^2 / (2 tau) = 1 的热核吻合](./plots/random-walk.py)

扩散时间与距离的平方成正比，这在生物学中有直接的后果。细胞质中蛋白质的扩散系数为 $10\,\mathrm{\mu m^2\,s^{-1}}$ 量级：它几秒钟就能穿过尺寸为 $10\,\mathrm{\mu m}$ 的细胞，但移动 $1\,\mathrm{cm}$ 却需要几个月。扩散足以完成细胞内部和细胞之间短距离的运输；更大的生物体则需要循环系统和主动运输。

### 7.5.2. 反应扩散方程

当扩散的量还在局部产生或消耗时，热方程就多了一个非线性源项。形如

$$
u_t=D\Delta u+f(u),\tag{7.6}
$$
的方程，或由扩散系数构成对角矩阵 $D$ 的方程组 $\boldsymbol{u}_t=D\Delta\boldsymbol{u}+\boldsymbol{f}(\boldsymbol{u})$，称为反应扩散方程（reaction-diffusion equation）。扩散项使 $u$ 散开，反应项 $f$（出生与死亡、化学反应）则在每一点像相应的常微分方程那样起作用。有两种现象是任何一部分单独都没有的；二者分别见[生态学](/7.19)与[发育生物学](/7.5)。

1. 入侵前沿：对 Fisher–KPP 方程 $u_t=Du_{xx}+ru(1-u)$，向空旷领地扩展的种群形成一个行波解（traveling wave solution）$u=U(x-ct)$，连接前沿后方的 $u=1$ 与前方的 $u=0$。在前沿的最前端 $u$ 很小，方程近似为 $u_t=Du_{xx}+ru$；代入 $u=\mathrm{e}^{-\lambda(x-ct)}$ 得 $c=D\lambda+\frac r\lambda\ge2\sqrt{rD}$（由均值不等式）。由局部初始数据产生的前沿以最小速度 $c^*=2\sqrt{rD}$ 传播（不加证明）：入侵速度由增长率与扩散系数共同决定。
2. 扩散驱动的不稳定性：对两个物种 $u,v$，$u_t=D_u\Delta u+f(u,v)$，$v_t=D_v\Delta v+g(u,v)$，设 $(u^*,v^*)$ 是对常微分方程稳定的均匀稳态，即 Jacobi 矩阵 $J$ 满足 $\operatorname{tr}J<0$，$\det J>0$。正比于 $\mathrm{e}^{\mathrm{i}qx+\sigma t}$ 的扰动按 $J-q^2\operatorname{diag}(D_u,D_v)$ 的特征值 $\sigma$ 增长或衰减。迹仍为负，所以不稳定性恰好在行列式
$$
h(q^2)=D_uD_vq^4-\big(D_vf_u+D_ug_v\big)q^2+\det J
$$
对某个 $q$ 变为负时发生。这要求 $D_vf_u+D_ug_v>2\sqrt{D_uD_v\det J}$；尽管 $f_u+g_v<0$，只要 $f_u$ 与 $g_v$ 异号、且两个扩散系数相差足够大，这就是可能的：一个扩散慢的自增强激活子，与一个扩散快的抑制子。这时一段波数 $q$ 增长，非线性项使增长饱和，形成静止的、空间周期的斑图，称为图灵斑图（Turing pattern）。Turing 在 1952 年提出这一机制作为形态发生的化学基础，它被用来解释动物皮毛的花纹、指（趾）的间距和植被斑图。

单独作用时把一切抹平的扩散，竟能使均匀状态失稳——这是应用数学中最引人注目的事实之一。

## 小结

| 主题 | 内容 |
|---|---|
| 热核 | $\Phi=(4\pi k t)^{-n/2}\mathrm{e}^{-\lvert x\rvert^2/(4k t)}$；正，质量为 1，$t\to0^+$ 时为近似单位元，$\Phi(t)*\Phi(s)=\Phi(t+s)$ |
| Cauchy 问题 | 对有界连续的 $\varphi$，$u=\Phi(\cdot,t)*\varphi$；$t>0$ 时光滑；在有界解中唯一 |
| 定性行为 | 无穷传播速度，瞬间光滑化，按 $t^{-n/2}$ 衰减，逆向问题不适定 |
| 弱极值原理 | $u_t-k\Delta u\le0\Rightarrow\max_{\bar Q_T}u=\max_{\Gamma_T}u$；给出唯一性、稳定性、比较原理 |
| 能量法 | Dirichlet 或 Neumann 条件下 $\frac{\mathrm{d}}{\mathrm{d}t}\int u^2=-2k\int\lvert\nabla u\rvert^2$ |
| 半直线 | $u(0,t)=0$ 用奇延拓，$u_x(0,t)=0$ 用偶延拓；$\varphi\equiv1$ 给出 $\operatorname{erf}\frac{x}{2\sqrt{k t}}$ |
| 齐次化原理 | $u=\int_0^t\Phi(\cdot,t-s)*f(\cdot,s)\,\mathrm{d}s$ |
| 概率 | $\Phi(\cdot,t)$ 是 $\mathcal{N}(0,2k t)$ 的密度；$k=h^2/(2\tau)$ 的随机游走 |
| 反应扩散 | $u_t=D\Delta u+f(u)$：速度为 $2\sqrt{rD}$ 的行波前沿；$D_v\gg D_u$ 时的 Turing 不稳定性 |
