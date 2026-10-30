---
title: 组织力学与形态动力学
description: 作为高黏度液体的胚胎组织：Maxwell 黏弹性，组织流变学的黏附位点膜模型（在底物上的滑动作为 Stefan 问题，间质膜及其有效弹性常数与黏度），形态动力学的连续介质方程，表面力（Laplace 与 Marangoni），量纲分析与 Stokes 流，带体积势的层状组织的耗散与能量平衡，Rayleigh 耗散原理，洋葱状分层的稳定性，表面活性剂不稳定性与卵裂的力学，皮层张力与肌动球蛋白，以及组织流固转变的顶点模型。
source_hash: 92d4a6d5c801
---

7.5.7 的分选实验表明，胚胎组织的行为像互不相溶的液体：它们变圆、融合并互相包围，仿佛由表面张力驱动。本章把这个类比当真，建立与之配套的力学。我们要问：组织是哪一类材料（具有极高黏度的黏弹性液体）；它的黏度和弹性如何能从细胞之间的黏附接触中产生；当表面张力作用在这种材料的边界和内部界面上时，什么方程支配它的缓慢流动；这样的流动有多快（慢到惯性完全不起作用）；以及流动耗散了驱动它的表面能，这一事实有什么推论。同一套框架用于单个细胞的表面，就给出**卵裂**的力学模型；张力的分子来源是肌动球蛋白皮层；而在单个细胞的尺度上，现行的工具是顶点模型，它也解释了组织如何在流体与固体行为之间转换。这里用到的数学（一阶线性方程、热方程、Laplace 变换、散度定理、球谐函数）取自数学课程，只作链接而不重新推导；在**原肠作用**、**下包**和**内陷**中的应用见 7.5.9。

## 8.1. 作为黏弹性液体的组织

有几项观察表明组织会流动。不规则的胚胎组织碎片会变成球；两个压在一起的球形聚集体融合为一，它们之间的颈部不断变宽，如同两个液滴合并；聚集体在离心时在自身重量下变扁，其平衡形状给出它的表面张力（7.5.7）。用黏性流动的方程拟合这些形变，得到约 $10^5$–$10^7\,\mathrm{Pa\,s}$（$10^6$–$10^8$ 泊）的有效黏度，与沥青相当，是甘油**黏度**的约 $10^5$ 倍（见 [5.2.2](/5.2.2)）。但组织并不是简单液体：突然压缩时，它表现出弹性，只有经过几分钟，应力才松弛，材料才流动。短时间尺度上是弹性的，长时间尺度上是黏性的：这正是 Maxwell 液体的行为。

**定义 8.1.1（Maxwell 黏弹性液体）** **Maxwell 黏弹性液体**是这样的材料，其剪切应力 $\tau$ 与剪切应变 $\varepsilon$ 满足

$$
\frac{\mathrm{d}\tau}{\mathrm{d}t} + \frac{\tau}{t_{\mathrm{r}}} = G\,\frac{\mathrm{d}\varepsilon}{\mathrm{d}t}, \qquad t_{\mathrm{r}} = \frac{\eta}{G},
\tag{8.1}
$$
其中 $G$ 是剪切模量，$\eta$ 是黏度，$t_{\mathrm{r}}$ 是松弛时间。它的力学类比是劲度为 $G$ 的无质量弹簧与黏度为 $\eta$ 的阻尼器串联：应变率相加，$\dot\varepsilon = \dot\tau/G + \tau/\eta$。

式 (8.1) 是 $\tau$ 的一阶线性方程（[2.2.15](/2.2.15)）。三个标准实验（图 1）：阶跃应变 $\varepsilon_0$ 之后，应力按 $\tau = G\varepsilon_0\mathrm{e}^{-t/t_{\mathrm{r}}}$ 松弛；在阶跃应力 $\tau_0$ 下，应变跃升到 $\tau_0/G$，然后线性增长，$\varepsilon = \tau_0/G + \tau_0t/\eta$（蠕变）；在 Couette 层中，即两壁之间，其中一壁开始以恒定速度运动，没有惯性时剪切率 $\dot\varepsilon = \mathrm{d}u/\mathrm{d}y$ 是均匀的，并且

$$
\tau = \eta\,\frac{\mathrm{d}u}{\mathrm{d}y}\bigl(1 - \mathrm{e}^{-t/t_{\mathrm{r}}}\bigr).
$$
当 $t \gg t_{\mathrm{r}}$ 时这是 Newton 定律 $\tau = \eta\,\mathrm{d}u/\mathrm{d}y$；当 $t \ll t_{\mathrm{r}}$ 时，$\tau \approx \eta\dot\varepsilon\,t/t_{\mathrm{r}} = G\varepsilon$，即 Hooke 定律。形态发生运动持续数小时，远长于数分钟的松弛时间，因此液体类比对它们适用。

![Maxwell 黏弹性液体（定义 8.1.1）。A：力学类比，剪切模量为 G 的弹簧与黏度为 η 的阻尼器串联，松弛时间 t_r = η/G。B：阶跃应变后的应力松弛，τ = Gε0 exp(−t/t_r)。C：阶跃应力下的蠕变：先有 τ0/G 的弹性跃升，随后以速率 τ0/η 作黏性流动。D：以恒定速率开始剪切：应力按 η(dε/dt)(1 − exp(−t/t_r)) 增长，t ≪ t_r 时为弹性的（τ ≈ Gε，虚线），t ≫ t_r 时为 Newton 型](./plots/maxwell.py)

弹性和黏度从何而来？一种自然的看法是：高黏度反映了组织流动时细胞必须滑动、断开并重新建立的黏附接触，而短时间的弹性反映了细胞膜与皮层的拉伸。下一节用一个模型使这一点具体化，在该模型中黏附集中在离散的位点上，因此位点密度同时度量膜的伸展和局部黏附能。

## 8.2. 组织流变学的黏附位点模型

在二维中讨论（沿 Couette 层可忽略方向排列的细胞行相当于二维细胞）。沿弧长为 $s$ 的膜，设 $n(s, t)$ 为黏附位点的数密度，$u(s, t)$ 为它们的切向速度，$T(s, t)$ 为膜张力。位点在线段 $(s, s + \Delta s)$ 上守恒，给出

$$
\frac{\partial n}{\partial t} + \frac{\partial(un)}{\partial s} = q,
$$
其中 $q$ 是位点的源（下面取零；它可以描述从细胞内部插入的位点）。位点是可伸展膜的组成部分，所以张力是它们密度的函数，$T = g(n, t)$，随 $n$ 递减（被拉伸的膜位点较稀疏，张力较高）；显式的时间依赖可以描述黏附随时间的硬化或软化。模型还需要位点所受摩擦的定律才封闭，$\partial T/\partial s = F(u, n, t)$。

### 8.2.1. 在底物上的滑动

设一段初始长度为 $L_0$、位点密度为 $n_0$ 的膜，从 $t = 0$ 起在右端施加对应于密度 $n_1 < n_0$ 的张力，沿平坦的底物拉动；左端自由，$g(n_0) = 0$。如果位点各自独立地响应底物，摩擦就是 $n$ 乘以位点速度的函数。在线性化的模型中，

$$
T = -k(n - n_0), \qquad \frac{\partial T}{\partial s} = n\,n_{\mathrm{s}}fu,
$$
其中 $k$ 是弹性常数，$f$ 是摩擦因子，$n_{\mathrm{s}}$ 是底物上结合位点的密度。于是 $nu = -K\,\partial n/\partial s$，$K = k/(n_{\mathrm{s}}f)$，位点守恒给出热方程

$$
\frac{\partial n}{\partial t} = K\frac{\partial^2n}{\partial s^2}, \qquad s_0(t) < s < s_1(t),
$$
其端点 $s_0(t), s_1(t)$ 随位点运动：在 $s = s_0$ 处 $-K\,\partial n/\partial s = \dot s_0n_0$，$n = n_0$；在 $s = s_1$ 处 $-K\,\partial n/\partial s = \dot s_1n_1$，$n = n_1$。这是 Stefan 型的**热方程**（[2.5.7](/2.5.7)）动边界问题。用变量 $s/L_0$、$tK/L_0^2$、$n/n_0$，剩下的唯一参数是 $n_1/n_0$：线段在时间尺度 $L_0^2/K$ 上松弛到稳定滑动。

**命题 8.2.1（稳定滑动）** 长时间后，所有位点以共同的速度 $U$ 运动，在随尾端运动的坐标系中（$s' = s - s_0(t)$），密度分布为 $n = n_0\mathrm{e}^{-Us'/K}$，并且

$$
U = \frac{K}{L_0}\Bigl(1 - \frac{n_1}{n_0}\Bigr), \qquad L = L_0\,\frac{\ln(n_0/n_1)}{1 - n_1/n_0}.
$$

**证明** 由 $u = U$，$nu = -Kn'$ 给出 $n' = -(U/K)n$，$n = n_0\mathrm{e}^{-Us'/K}$，而 $n(L) = n_1$ 给出 $UL/K = \ln(n_0/n_1)$。位点守恒，$n_0L_0 = \int_0^Ln\,\mathrm{d}s' = (n_0K/U)(1 - n_1/n_0)$，由此得 $U$；再得 $L = (K/U)\ln(n_0/n_1)$。$\square$

瞬态问题没有初等解。在小时间内，靠近被拉端处，解是边界值突然改变的误差函数分布，$n \approx n_0 + 2(n_1 - n_0)\pi^{-1/2}\int_{-\infty}^{(s - s_1)/2\sqrt{Kt}}\mathrm{e}^{-z^2}\mathrm{d}z$，所以前端按 $s_1 - L_0 = O(\sqrt t)$ 运动，而尾端起初梯度为零，不动。用给位点编号的 Lagrange 坐标，问题就变得简单（图 2）。它的行为并不完全是 Maxwell 元件：当力突然作用于串联的弹簧和阻尼器时，弹簧立即伸长，阻尼器立即开始运动，而这里伸展是从被拉端扩散进来的。

![沿底物被拉动的黏附位点膜（8.2.1）：线性位点模型，n_1 = n_0/2 在 t = 0 时施加于右端，用 Lagrange 坐标（左边的位点数）求解，在该坐标中移动的端点固定不动。A：t = 0.02、0.1、0.3、1 和 4（单位 L0²/K）时位点密度随位置的分布：伸展从被拉端扩散进来，整个线段同时开始滑动。B：线段长度与尾端速度在时间尺度 L0²/K 上趋近命题 8.2.1 的稳定滑动值 L = 1.386 L0 与 U = 0.5 K/L0（虚线）](./plots/membrane-sliding.py)

### 8.2.2. 间质膜

更接近组织流变学的模型考虑充满细胞的 Couette 层，可以把细胞想象成充满黏性流体的、有黏性的弹性袋，在水平薄层中互相滚过。由于相邻的薄层以不同的速度运动，相邻细胞的膜在接触区域内互相滑过。把一个接触区建模为两层膜在 $\lvert s\rvert < L(t)/2$ 上压在一起，在 $s \to -s$ 下对称，相对运动由对角相对的两个边缘处增强的张力 $T_1 = T_0 + k(n_0 - n)$ 驱动。设 $n, u$ 指下层膜。如果两层膜的位点密度各自独立地产生摩擦（如 7.5.7 中 Steinberg 的稀疏位点规则），且摩擦与相对速度成线性关系，

$$
-k\frac{\partial n}{\partial s} = f\,n(s, t)\,n(-s, t)\bigl[u(s, t) + u(-s, t)\bigr].
$$
右端是 $s$ 的偶函数，所以 $\partial n/\partial s$ 是偶函数，$n(s, t) + n(-s, t)$ 不依赖于 $s$；在边缘处求值，它等于 $n_0 + n_1(t)$，其中 $n_1$ 是被拉伸边缘处的密度。两层膜合计，位点守恒：$(n_0 + n_1)L(t) = 2n_0L_0$，所以接触长度可以显式写出，$L(t) = 2n_0L_0/(n_0 + n_1(t))$。

当 $n_1$ 为常数时，稳态有 $un = u_0n_0 = u_1n_1$（$u_0, u_1$ 为边缘速度），所以 $-k\,\partial n/\partial s = f(n_0 + n_1)n_0u_0$ 是常数，分布是线性的，并且

$$
u_0 = \frac{K}{2L_0}\Bigl(1 - \frac{n_1}{n_0}\Bigr), \qquad u_1 = \frac{n_0u_0}{n_1}, \qquad K = \frac{k}{fn_0}.
$$
对于瞬态，守恒与对称给出 $u(-s)n(-s) = u(s)n(s) + s\dot n_1$，消去 $u$，

$$
f(n_0 + n_1)\frac{\partial n}{\partial t} - k\frac{\partial^2n}{\partial s^2} = f\dot n_1\frac{\partial(sn)}{\partial s}.
$$
对于小偏差，$n = n_0(1 - g)$，$n_1 = n_0(1 - \nu)$，$\lvert g\rvert, \lvert\nu\rvert \ll 1$，它变成

$$
2\frac{\partial g}{\partial t} - K\frac{\partial^2g}{\partial s^2} - \dot\nu = 0, \qquad g\Bigl(\frac{L_0}{2}, t\Bigr) = \nu, \quad g\Bigl(-\frac{L_0}{2}, t\Bigr) = 0.
\tag{8.2}
$$

**定理 8.2.2（有效 Maxwell 常数）** 设 $\nu$ 与 $g$ 在 $t = 0$ 时为零，定义剪切应力 $\tau = kn_0\nu/L_0$，剪切率为边缘速度加弹性伸展，$\dot\varepsilon = (u_0 + u_1)/L_0 + \dot\nu/2$。则 Laplace 变换（[2.5.6](/2.5.6)）满足

$$
\frac{\hat\varepsilon}{\hat\tau} = \frac{L_0\sigma}{2kn_0} + \frac{1}{2n_0^2f}\sqrt{\frac{2\sigma}{K}}\coth\Bigl(\sqrt{\frac{\sigma L_0^2}{2K}}\Bigr)
= \frac{1}{L_0n_0^2f} + \frac{2L_0}{3kn_0}\,\sigma + O(\sigma^2),
$$
所以在长时间（小 $\sigma$）下，接触的行为像 Maxwell 液体，$\hat\varepsilon/\hat\tau = \sigma/k_{\mathrm{eff}} + 1/\eta_{\mathrm{eff}}$，其中

$$
k_{\mathrm{eff}} = \frac{3kn_0}{2L_0}, \qquad \eta_{\mathrm{eff}} = L_0n_0^2f, \qquad t_{\mathrm{r}} = \frac{\eta_{\mathrm{eff}}}{k_{\mathrm{eff}}} = \frac{2L_0^2}{3K}.
$$

**证明** 对式 (8.2) 在零初始条件下作变换，$2\sigma\hat g - K\hat g'' = \sigma\hat\nu$。一个特解是 $\hat\nu/2$；加上 $A\sinh\lambda s + B\cosh\lambda s$，其中 $\lambda = \sqrt{2\sigma/K}$，并施加边界条件，得 $B = 0$ 与

$$
\hat g = \frac{\hat\nu}{2}\Bigl[1 + \frac{\sinh\lambda s}{\sinh(\lambda L_0/2)}\Bigr].
$$
线性化摩擦定律，$kn_0\,\partial_sg = fn_0^2\bigl[u(s) + u(-s)\bigr]$，所以在边缘处 $u_0 + u_1 = K\,\partial_sg(L_0/2) = \frac K2\bigl[\partial_sg(L_0/2) + \partial_sg(-L_0/2)\bigr]$，变换后 $\hat u_0 + \hat u_1 = \frac K2\hat\nu\lambda\coth(\lambda L_0/2)$。因此 $\hat\varepsilon = \frac{K\lambda}{2L_0}\coth(\lambda L_0/2)\hat\nu + \frac\sigma2\hat\nu$，除以 $\hat\tau = kn_0\hat\nu/L_0$（$K = k/fn_0$）即得第一个表达式。令 $z = \lambda L_0/2$，展开 $\coth z = 1/z + z/3 + O(z^3)$：$\lambda\coth z = 2/L_0 + \lambda^2L_0/6 + \dots = 2/L_0 + \sigma L_0/(3K) + \dots$，由此得常数项 $1/(L_0n_0^2f)$，以及 $\sigma$ 的系数 $L_0/(2kn_0) + L_0/(6kn_0) = 2L_0/(3kn_0)$。$\square$

因此，模型预测，对于比 $t_{\mathrm{r}} \sim L_0^2/K$ 更慢的运动，聚集体表现出 Newton 型黏性行为，黏度由黏附位点的摩擦决定。它不止是一个 Maxwell 元件：在大 $\sigma$（短时间）下，柔度趋于 $L_0/(2kn_0)$，比 $1/k_{\mathrm{eff}}$ 更硬，因为伸展沿接触的扩散引入了一整个松弛时间谱（图 3）。实测的聚集体黏度（$10^5$–$10^7\,\mathrm{Pa\,s}$）确定了 $\eta_{\mathrm{eff}}$，而 $k_{\mathrm{eff}}$ 可以由弹性响应测量；模型做不到的是把 $k$ 和 $f$ 与决定表面张力的黏附能联系起来。允许位点之间有相关性的随机版本是自然的推广。

![间质膜模型的蠕变（8.2.2）。A：两层细胞膜在长度为 L(t) 的区域内接触并互相滑过；靠近前缘的黏附位点被拉伸，摩擦正比于两层膜上位点密度的乘积以及它们的相对速度。B：阶跃应力后的蠕变柔度，由式 (8.2) 用 Fourier 级数精确算出（实线），以及定理 8.2.2 的 Maxwell 近似 1/k_eff + t/η_eff（虚线）：t ≫ L0²/K 时二者一致，而在短时间内精确的柔度趋于较小的值 L0/(2kn0)（点线）](./plots/interstitial-membrane.py)

## 8.3. 形态动力学的连续介质方程

在远大于细胞的尺度上、长于 $t_{\mathrm{r}}$ 的时间内，可以把组织当作 Newton 黏性液体。这是一个粗糙的近似：细胞并不是各向同性的（带有极性轴的细胞使材料在局部是各向异性的，更像液晶，所以"细胞状态"一般应当是张量），而且它们是主动的。但这是正确的第一步。

**定义 8.3.1（形态动力学）** **形态动力学**是用连续介质力学方程描述形态发生运动：组织质量与动量的守恒律，联系应力与形变的本构律，以及表达表面张力和界面张力所施加的力的边界条件。

运动的连续介质有两种描述。Euler 描述给出空间固定点上的场，如密度 $\rho(\boldsymbol{x}, t)$ 和速度 $\boldsymbol{u}(\boldsymbol{x}, t)$；Lagrange 描述跟随每个质点，$\boldsymbol{x} = \boldsymbol{X}(\boldsymbol{b}, t)$，$\boldsymbol{X}(\boldsymbol{b}, 0) = \boldsymbol{b}$（下面对重复指标求和）。

质量。对组织内部一个固定的小体积 $V'$，外法向为 $\boldsymbol{n}$，设生长产生物质的速率为 $q$（单位时间的密度），则 $\frac{\mathrm{d}}{\mathrm{d}t}\int\rho\,\mathrm{d}V' = -\oint\rho u_in_i\,\mathrm{d}S' + \int q\,\mathrm{d}V'$。由**Gauss 公式**（[2.2.14](/2.2.14)）和 $V'$ 的任意性，

$$
\frac{\partial\rho}{\partial t} + \frac{\partial(\rho u_i)}{\partial x_i} = q,
\tag{8.3}
$$
这就是**连续性方程**。用物质导数 $\frac{\mathrm{d}}{\mathrm{d}t} = \frac{\partial}{\partial t} + u_j\frac{\partial}{\partial x_j}$，即跟随质点的变化率，式 (8.3) 写成 $\mathrm{d}\rho/\mathrm{d}t + \rho\,\partial_iu_i = q$。"不可压缩"（$\partial_iu_i = q/\rho$）并不意味着 $\rho$ 为常数：它的意思是 $\mathrm{d}\rho/\mathrm{d}t = 0$，沿每条质点轨迹密度为常数，但不同质点之间可以不同（密度不同的细胞类型）。没有源时，不可压缩性在 Euler 形式中是 $\partial_iu_i = 0$，在 Lagrange 形式中是 $\det(\partial X_i/\partial b_j) = 1$：流映射保持体积。

动量。质点的加速度是 $a_i = \ddot X_i = \partial_tu_i + u_j\partial_ju_i = \mathrm{d}u_i/\mathrm{d}t$，Newton 定律为 $\rho a_i = \partial_j\sigma_{ij} + f_i$，其中 $\sigma_{ij}$ 是应力张量（$\sigma_{ij}n_j$ 是 $\boldsymbol{n}$ 所指一侧的物质通过法向为 $\boldsymbol{n}$ 的面元施加的单位面积的力），$f_i$ 是体力。对于黏度为 $\eta$、黏性应力无迹的 Newton 液体，

$$
\sigma_{ij} = -p\,\delta_{ij} + \eta\Bigl(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i} - \frac23\frac{\partial u_k}{\partial x_k}\delta_{ij}\Bigr),
$$
其中 $p$ 是压强：黏性应力由速度梯度产生，如同弹性应力由位移梯度产生。代入得

$$
\rho\Bigl(\frac{\partial u_i}{\partial t} + u_j\frac{\partial u_i}{\partial x_j}\Bigr) + \frac{\partial p}{\partial x_i} - \eta\nabla^2u_i = f_i + \frac{\eta}{3\rho}\frac{\partial q}{\partial x_i},
\tag{8.4}
$$
这是带生长项的 Navier–Stokes 方程；Laplace 项描述动量的扩散，扩散系数为 $\eta/\rho$（运动黏度）。对于 Maxwell 液体，黏性应力 $\tau_{ij}$ 满足 $t_{\mathrm{r}}\,\mathrm{d}\tau_{ij}/\mathrm{d}t + \tau_{ij} = \eta(\partial_ju_i + \partial_iu_j - \frac23\partial_ku_k\delta_{ij})$；对于大形变，物质导数必须换成坐标系不变的（上随体）导数，这一改进对下面的缓慢流动不需要。

## 8.4. 表面力

设组织占据区域 $V$，边界是光滑曲面 $S$，外法向为 $\boldsymbol{n}$，并设表面张力 $\gamma(\boldsymbol{x}, t)$ 作用于 $S$，外部不施加应力。

**定理 8.4.1（表面力）** 组织表面所受的牵引力为

$$
f_i^{\mathrm{s}} = \sigma_{ij}n_j = -\gamma\Bigl(\frac1{R_1} + \frac1{R_2}\Bigr)n_i + \Bigl(\frac{\partial\gamma}{\partial x_i} - n_in_j\frac{\partial\gamma}{\partial x_j}\Bigr),
$$
其中 $R_1, R_2$ 是主曲率半径（凸面为正）。法向部分是 **Young–Laplace 方程**（[定理 19.2.1](/6.3.19#thm-19.2.1)）的 Laplace 压强；切向部分是 $\gamma$ 在表面内的梯度，它把表面拉向张力较高的区域（Marangoni 力）。

**证明** 法向部分：把 $S$ 沿法向位移 $\delta\zeta(\boldsymbol{x})$。沿主方向的面元 $\mathrm{d}\xi_1\mathrm{d}\xi_2$ 变成 $\mathrm{d}\xi_1(1 + \delta\zeta/R_1)\,\mathrm{d}\xi_2(1 + \delta\zeta/R_2)$，所以 $\delta(\mathrm{d}S) \approx (1/R_1 + 1/R_2)\delta\zeta\,\mathrm{d}S$。应力的虚功与表面能的改变必须平衡：对所有 $\delta\zeta$，$\int\delta\zeta\bigl[\sigma_{ij}n_in_j + \gamma(1/R_1 + 1/R_2)\bigr]\mathrm{d}S = 0$，所以 $\sigma_{ij}n_in_j = -\gamma(1/R_1 + 1/R_2)$。切向部分：在由曲线 $C'$ 围成的近似平坦的小片 $S'$ 上，张力以力 $\oint_{C'}\gamma\boldsymbol{t}\,\mathrm{d}s$ 拉动边界，其中 $\boldsymbol{t}$ 是 $C'$ 在表面内的外单位法向；由切平面内的散度定理，这等于 $\int_{S'}\nabla_{\mathrm{s}}\gamma\,\mathrm{d}S'$，其中 $\nabla_{\mathrm{s}}\gamma = \nabla\gamma - \boldsymbol{n}(\boldsymbol{n}\cdot\nabla\gamma)$ 是表面梯度。$\square$

**命题 8.4.2** 若把 $S$ 的单位法向延拓成 $S$ 附近的光滑单位矢量场 $\boldsymbol{n}(\boldsymbol{x})$，则在 $S$ 上 $\nabla\cdot\boldsymbol{n} = 1/R_1 + 1/R_2$（平均**曲率**的两倍）。

**证明** 考虑薄区域 $\{\boldsymbol{x} + r\boldsymbol{n}(\boldsymbol{x}) : 0 \le r \le \delta\zeta, \boldsymbol{x} \in \mathrm{d}S\}$。对 $\partial_in_i$ 在其上积分，散度定理只留下两个端面（侧面上 $\boldsymbol{n}$ 是相切的），它们的面积相差 $(1/R_1 + 1/R_2)\,\mathrm{d}S\,\delta\zeta$；该积分同时 $\approx\partial_in_i\,\mathrm{d}S\,\delta\zeta$。$\square$

![组织上的表面力（定理 8.4.1）。A：组织表面的一块曲面，按局部张力着色（越深越高）：法向力 −γ(1/R1 + 1/R2)n 指向曲率中心（Laplace 压强），切向力 ∇sγ 沿表面指向张力较高处（Marangoni 力）。B：对于张力在一个极处最高的聚集体的后果：表面被拉向该极，内部形成两个环流（Stokes 流示意）](./plots/surface-forces.py)

## 8.5. 量纲分析与 Stokes 流

设 $\gamma_0$ 为典型的表面张力，$U_0$ 为典型的速度，$L_0$ 为聚集体的尺寸。当 $\eta U_0/L_0 \sim \gamma_0/L_0$，即 $U_0 \sim \gamma_0/\eta$ 时，$S$ 上的黏性应力与表面张力平衡。取 $\gamma_0 \approx 15\,\mathrm{mN\,m^{-1}}$，$\eta \approx 10^6\,\mathrm{Pa\,s}$（细胞聚集体的值），得 $U_0 \approx 1.5\times10^{-8}\,\mathrm{m\,s^{-1}}$，所以宽 $1\,\mathrm{mm}$ 的聚集体在 $L_0/U_0 \approx 7\times10^4\,\mathrm{s}$（约一天）内明显变形。这些数值本身是在假定液体类比的前提下得到的，但令人鼓舞的是，得到的时间正是形态发生运动的时间尺度。

惯性与黏性力之比为 $\rho U_0^2/L_0$ 比 $\eta U_0/L_0^2$，其比值是 Reynolds 数 $\operatorname{Re} = \rho U_0L_0/\eta \approx 10^3\times1.5\times10^{-8}\times10^{-3}/10^6 \approx 10^{-14}$。惯性完全可以忽略：流动由当前的表面力即刻建立，力一消失就立即停止（对比游动细菌的 $\operatorname{Re} \sim 10^{-5}$，[7.3.14](/7.3.14)）。

用 $L_0$ 标度 $\boldsymbol{x}$，用 $\eta L_0/\gamma_0$ 标度 $t$，用 $\gamma_0/\eta$ 标度 $\boldsymbol{u}$，用 $\gamma_0/L_0$ 标度 $p$，用 $\gamma_0$ 标度 $\gamma$，用 $L_0$ 标度 $R_i$，用 $\gamma_0/L_0^2$ 标度 $\boldsymbol{f}$，用典型生长率 $q_0$ 标度 $q$。略去惯性，无量纲方程为

$$
\frac{\partial p}{\partial x_i} - \nabla^2u_i = f_i + \frac{\Pi}{3}\frac{\partial q}{\partial x_i}, \qquad \frac{\partial u_i}{\partial x_i} = \Pi q, \qquad
\sigma_{ij}n_j = -\gamma\Bigl(\frac1{R_1} + \frac1{R_2}\Bigr)n_i + \nabla_{\mathrm{s}}\gamma \ \text{在 } S \text{ 上},
$$
其中生长数 $\Pi = (q_0/\rho)(\eta L_0/\gamma_0)$ 是张力驱动流动的时间尺度与生长时间尺度之比。当 $\Pi$ 小时，形状变化与生长无关。系统由运动学条件封闭，即边界随物质运动：若 $S$ 是水平集 $\Sigma(\boldsymbol{x}, t) = 0$，则在 $S$ 上 $\mathrm{d}\Sigma/\mathrm{d}t = \partial_t\Sigma + u_i\partial_i\Sigma = 0$，再加上 $\gamma$ 的定律（7.5.7 以及 8.6、8.8）。

**定义 8.5.1（Stokes 流）** **Stokes 流**（蠕动流）是 Reynolds 数趋于零时的流动，由 $\nabla p - \eta\nabla^2\boldsymbol{u} = \boldsymbol{f}$ 与 $\nabla\cdot\boldsymbol{u} = 0$（无生长时）支配：方程是线性的，不含时间导数，所以时间只通过移动的边界以及作用于其上的变化的力进入。

然而问题仍是非线性的，因为求解线性方程的区域随解而变。两个经典解给出了组织变圆和融合的时间尺度。当周围介质的黏度小得多时，半径为 $R$ 的球的小椭球形变按速率 $\frac{20}{19}\gamma/(\eta R)$ 指数衰减（Rallison 关于另一种液体中的液滴的结果的极限），波数为 $k$ 的短表面波按速率 $\gamma k/(2\eta)$ 衰减，所以小的皱褶最先消失。两个半径为 $a$ 的接触球通过黏性烧结而融合：在 Frenkel 的分析中，颈半径 $x$ 按 $(x/a)^2 = 3\gamma t/(2\eta a)$ 增长。用这个定律拟合聚集体融合，是估计组织黏度的方法之一。

**例 8.5.1** 取 $\gamma = 10\,\mathrm{mN\,m^{-1}}$，$\eta = 2\times10^5\,\mathrm{Pa\,s}$，$a = 200\,\mu\mathrm{m}$，时间单位 $\eta a/\gamma$ 为 $4\times10^3\,\mathrm{s}$；颈达到半径一半时 $3\gamma t/(2\eta a) = 1/4$，$t = \frac16\eta a/\gamma \approx 670\,\mathrm{s}$，约 11 分钟，同样大小的变形聚集体以时间常数 $\frac{19}{20}\eta a/\gamma \approx 1\,\mathrm{h}$ 变圆。若 $\eta = 10^7\,\mathrm{Pa\,s}$，时间长五十倍。

![聚集体的张力驱动 Stokes 流。A：高黏度液滴的小椭球（l = 2）形变以速率 (20/19)γ/(ηR) 衰减（实线），kR = 6 的短表面波以平面速率 γk/(2η) 衰减（虚线）。B：两个半径为 a 的球因黏性烧结（Frenkel）而早期融合：(x/a)² = 3γt/(2ηa)；上轴以小时为单位，对应 γ = 10 mN/m，η = 2 × 10⁵ Pa s，a = 200 µm。C：颈半径 x/a = 0.2、0.5 和 0.8 时两个融合球的轮廓](./plots/aggregate-rounding.py)

## 8.6. 耗散与能量平衡

把 Stokes 方程乘以 $u_i$ 并在 $V$ 上积分，利用散度定理和定理 8.4.1 的表面牵引力，得到能量平衡。与表面能的变化率结合，$\frac{\mathrm{d}}{\mathrm{d}t}\int_S\gamma\,\mathrm{d}S = \int_S\partial_t\gamma\,\mathrm{d}S + \int_S\gamma(1/R_1 + 1/R_2)u_in_i\,\mathrm{d}S$（第二项是法向运动下面积的变化，命题 8.4.2），得到：

**定理 8.6.1（能量平衡）** 对于表面张力为 $\gamma$、体力为 $\boldsymbol{f}$、生长为 $q$ 的组织的 Stokes 流，

$$
\frac{\mathrm{d}}{\mathrm{d}t}\int_S\gamma\,\mathrm{d}S - \int_S\Bigl(\frac{\partial\gamma}{\partial t} + u_i\frac{\partial\gamma}{\partial x_i} - u_in_in_j\frac{\partial\gamma}{\partial x_j}\Bigr)\mathrm{d}S = \int_Vu_if_i\,\mathrm{d}V + \Pi\int_Vpq\,\mathrm{d}V - \Phi,
$$
其中黏性耗散（无量纲）为

$$
\Phi = \frac12\int_V\Bigl[\Bigl(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}\Bigr)^2 - \frac43\Pi^2q^2\Bigr]\mathrm{d}V \ge 0.
$$
自由表面能因体力和生长所做的功而升高，因黏性耗散而降低。当张力是表面的物质性质时（沿表面质点的运动 $\gamma$ 为常数，法向运动除外），左边的积分为零。

现在把 $V$ 分成单一细胞类型的区域 $V_\alpha$，界面 $S_{\alpha\beta}$ 上的张力 $\gamma_{\alpha\beta}$ 为常数，黏度为 $\eta_\alpha$。界面是物质的（$\mathrm{d}\Sigma_{\alpha\beta}/\mathrm{d}t = 0$），应力在界面两侧的跳变由 Laplace 项给出：在 $S_{\alpha\beta}$ 上 $(\sigma^\beta_{ij} - \sigma^\alpha_{ij})n_j = \gamma_{\alpha\beta}(\partial_jn_j)n_i$。同样的计算给出

$$
\frac{\mathrm{d}}{\mathrm{d}t}\sum_{\alpha<\beta}\int_{S_{\alpha\beta}}\gamma_{\alpha\beta}\,\mathrm{d}S = \sum_\alpha\int_{V_\alpha}\bigl(\boldsymbol{u}\cdot\boldsymbol{f}_\alpha + p\tilde q_\alpha\bigr)\mathrm{d}V - \sum_\alpha\Phi_\alpha.
$$
没有源和体力时，总界面能单调下降，速率等于总黏性耗散。这是**细胞分选**中表面势最小化的动力学对应（公式 7.2.1）：由于动能可以忽略，热力学第一定律说明表面张力做功的速率等于产热的速率。它本身并不能确定流动；确定流动的是下面的变分原理。

接下来设组织是分层的，细胞类型在曲面上为常数，并且层数多到细胞类型是光滑函数。设 $\phi$ 是一个函数，它在相继各层之间的界面上有跳变 $\phi_\alpha - \phi_\beta = \gamma_{\alpha\beta} \ge 0$（法向 $\boldsymbol{n}$ 从 $\alpha$ 指向 $\beta$）。对于支撑在含许多层的小体积 $V'$ 内的虚位移 $\delta\boldsymbol{\xi}$，把界面力求和并过渡到光滑的 $\phi$，界面张力起体力的作用：

$$
f_i = \frac{\partial\phi}{\partial x_i}\frac{\partial n_j}{\partial x_j}, \qquad \boldsymbol{n} = \frac{\nabla\phi}{\lvert\nabla\phi\rvert}.
$$
这里 $\phi$ 是由黏附能（$2\gamma_{\alpha\beta} = E_{\alpha\alpha} + E_{\beta\beta} - 2E_{\alpha\beta}$）与初始分层构造出的光滑近似；此后它是细胞的性质，由细胞携带，$\mathrm{d}\phi/\mathrm{d}t = 0$。是否存在定义在细胞类型本身上的 $\phi$，使每一对都有 $\gamma_{\alpha\beta} = \phi_\alpha - \phi_\beta$，并不是自动成立的：由于 $E_{\alpha\beta}$ 一般不能从 $E_{\alpha\alpha}$ 与 $E_{\beta\beta}$ 预测，界面张力不能由孤立细胞类型的性质预测。稀疏位点模型给出由细胞性质决定的张力，但不是差；**浮动位点模型**给出 $\mathrm{d}\phi = k\,\mathrm{d}N$（7.5.7，定义 7.3.1）。

**定理 8.6.2（体积自由能）** 若组织的一部分 $V'$ 由连续分布的细胞类型组成，具有体积势 $\phi$（在 $V'$ 的边界附近取常数），则在无体力和生长时

$$
\frac{\mathrm{d}}{\mathrm{d}t}\Bigl[\int_{V'}\lvert\nabla\phi\rvert\,\mathrm{d}V + V_{\mathrm{fs}}\Bigr] = -\Phi,
$$
其中 $V_{\mathrm{fs}}$ 是所有离散表面和界面的自由能，$\int\lvert\nabla\phi\rvert\,\mathrm{d}V$ 是连续分层的*体积自由能*。

**证明**（概要） 在表面处，下方的各层沿 $\phi$ 的等值线拉动，所以表面牵引力多出一项 $-\lvert\nabla\phi\rvert(\boldsymbol{n} - \gamma_{\boldsymbol{n}}\tilde{\boldsymbol{n}})$，其中 $\tilde{\boldsymbol{n}}$ 是各层的法向，$\gamma_{\boldsymbol{n}} = \boldsymbol{n}\cdot\tilde{\boldsymbol{n}}$。由于 $\phi$ 是物质的，$\partial_t\phi = -\boldsymbol{u}\cdot\nabla\phi$，并且

$$
\frac{\mathrm{d}}{\mathrm{d}t}\int\lvert\nabla\phi\rvert\,\mathrm{d}V' = -\int\frac{\nabla\phi\cdot\nabla(\boldsymbol{u}\cdot\nabla\phi)}{\lvert\nabla\phi\rvert}\mathrm{d}V' + \int\boldsymbol{u}\cdot\boldsymbol{n}\lvert\nabla\phi\rvert\,\mathrm{d}S'.
$$
分部积分后，体积项变成 $\int\nabla\cdot\bigl(\nabla\phi/\lvert\nabla\phi\rvert\bigr)\,\boldsymbol{u}\cdot\nabla\phi\,\mathrm{d}V' = -\int\boldsymbol{u}\cdot\boldsymbol{f}\,\mathrm{d}V'$ 加一个表面项；与含修正牵引力的能量平衡结合，所有表面项相消。$\square$

平衡式 $\mathrm{d}E/\mathrm{d}t = -\Phi$（$E$ 为总的表面（和体积）自由能）只是一个标量方程，不能确定流动。变分原理可以。对于坐标为 $r_i$、速度为 $u_i = \dot r_i$ 的系统：

**定义 8.6.1（Rayleigh 耗散函数）** 系统的 **Rayleigh 耗散函数** $\Phi(\boldsymbol{u})$ 是它的能量耗散率表示为速度的函数；对于线性摩擦和黏性，它是正的二次型，是速度的二次齐次式。对于黏性液体，$\Phi = \frac\eta2\int(\partial_ju_i + \partial_iu_j)^2\,\mathrm{d}V$（对于不可压缩流和适当的边界条件，剪切部分化为 $\eta\int\sum_{ij}(\partial_ju_i)^2\,\mathrm{d}V$）。

**定理 8.6.3（Rayleigh 原理）** 设在每个时刻，运动使自由能 $E(\boldsymbol{r})$ 在所有耗散相同的速度场中下降得最快，并满足能量平衡 $\dot E + \Phi = 0$。则速度满足

$$
\delta\Bigl(\dot E + \tfrac12\Phi\Bigr) = 0, \qquad\text{即}\qquad \frac{\partial E}{\partial r_i} + \frac12\frac{\partial\Phi}{\partial u_i} = 0,
$$
变分是在固定构型下对速度进行的。

**证明** 在 $\Phi$ 固定下，用 Lagrange 乘子 $\lambda(t)$（**Lagrange 乘子法**）使 $-\dot E$ 最大，得 $\delta(\dot E + \lambda\Phi) = 0$。由 $\dot E = \sum_i(\partial E/\partial r_i)u_i$ 与 $\delta = \partial/\partial u_i$，得 $\partial E/\partial r_i + \lambda\,\partial\Phi/\partial u_i = 0$。乘以 $u_i$ 并求和：由于 $\Phi$ 是二次**齐次函数**，Euler 定理给出 $\sum_iu_i\,\partial\Phi/\partial u_i = 2\Phi$，所以 $\dot E + 2\lambda\Phi = 0$。再由能量平衡 $\dot E = -\Phi$ 得 $\lambda = \frac12$。$\square$

**例 8.6.1** 设构型由少数几个坐标 $\boldsymbol{q}$ 描述，$\Phi = \sum_{ij}C_{ij}\dot q_i\dot q_j$，$C$ 为对称正定矩阵（摩擦或阻力矩阵）。Rayleigh 原理给出 $\partial E/\partial q_i + \sum_jC_{ij}\dot q_j = 0$，即 $\dot{\boldsymbol{q}} = -C^{-1}\nabla E$：过阻尼运动是自由能的梯度流，迁移率为 $C^{-1}$，且 $\dot E = -\nabla E\cdot C^{-1}\nabla E = -\Phi \le 0$。这就是 7.5.10（§10.2–10.3）中对其奇点分类的"带阻力矩阵的准静态动力学"。对于 Stokes 流，该原理等价于 Helmholtz 的经典定理，即 Stokes 解使耗散在边界速度相同的所有不可压缩流中最小，并且它允许由少数形状参数以变分方式计算组织流动；用这种方法处理的底物上柱状细胞的形状变化以及上皮环的内陷见 7.5.9。

## 8.7. 层状聚集体的稳定性

液体类比有一个局限，在稳定性问题中表现得很清楚。取三种细胞类型排成洋葱，$A$ 在最内，然后是 $B$，然后是 $C$。离散的 $A$ 细胞可以突破 $B$ 层，直接接触 $C$。而均匀的液体层在光滑形变下做不到：液体层会变薄，但绝不会破裂。所以，即使是"错误的"洋葱（尽管 $B$ 包围 $A$，$B$ 却在 $A$ 之下），小的流体扰动也不一定会把它翻转过来，这很像局部的动力学分选规则不能达到全局极小（7.5.7，§7.6）。这在线性稳定性分析中如何表现？

具有球形界面的离散液体层只是中性稳定的：界面必须是球面，但不必保持同心。对于连续分层，设平衡时的体积势为 $\phi = \Psi(r)$，$r$ 为径向坐标，$S$ 上 $r = 1$。若 $\Psi(1) \ne 0$，$S$ 上有表面张力，$S$ 的任何形变都要耗能，因此考虑保持 $S$ 固定的形变，它们由与 $S$ 相切的无散速度 $\boldsymbol{u}$ 产生：$\boldsymbol{X} \approx \boldsymbol{b} + t\boldsymbol{u}(\boldsymbol{b})$，位移 $\delta\boldsymbol{X} \approx t\boldsymbol{u}$。

**定理 8.7.1（连续洋葱的中性稳定性）** 若 $\Psi'$ 没有零点，体积自由能的改变到位移的二阶为

$$
\delta\int\lvert\nabla\phi\rvert\,\mathrm{d}V = \frac12\int\lvert\Psi'\rvert\Bigl[\lvert\nabla_{\mathrm{s}}\delta X_r\rvert^2 - 2\Bigl(\frac{\delta X_r}{r}\Bigr)^2\Bigr]\mathrm{d}V \ge 0,
$$
对非平凡位移可以取等号，其中 $\delta X_r$ 是位移的径向分量，$\nabla_{\mathrm{s}}$ 是半径为 $r$ 的球面上的梯度：连续分层至多是中性稳定的。若 $\Psi'$ 在半径 $r_\alpha$ 处为零，则会出现一个附加项 $-\sum_\alpha\lvert\Psi''(r_\alpha)\rvert\int(\delta X_r)^2\,\mathrm{d}S_{r_\alpha}$，它起失稳作用。

**证明**（概要） 因为 $\phi$ 是物质的，$\partial_t\delta\phi = -\boldsymbol{u}\cdot\nabla\Psi - \boldsymbol{u}\cdot\nabla\delta\phi$，积分得 $\delta\phi = -\delta\boldsymbol{X}\cdot\nabla\Psi + \frac12\delta\boldsymbol{X}\cdot\nabla(\delta\boldsymbol{X}\cdot\nabla\Psi) + O(\delta X^3)$。把 $\lvert\nabla\Psi + \nabla\delta\phi\rvert$ 展开到二阶，并利用 $\Psi$ 只依赖于 $r$，

$$
\lvert\nabla\phi\rvert = \lvert\Psi'\rvert\Bigl[1 - \frac{1}{\Psi'}\frac{\partial}{\partial r}(\delta X_r\Psi') + \frac{1}{2\Psi'}\frac{\partial}{\partial r}\bigl[\delta\boldsymbol{X}\cdot\nabla(\delta X_r\Psi')\bigr] + \frac12\lvert\nabla_{\mathrm{s}}\delta X_r\rvert^2\Bigr] + O(\delta X^3).
$$
一阶项（在球坐标中，$S$ 上 $\delta X_r = 0$）积分为 $\int(2/r)\lvert\Psi'\rvert\delta X_r\,\mathrm{d}V$，它为零，因为无散场通过 $S$ 内每个球面 $r = \mathrm{const}$ 的通量为零。若 $\Psi'$ 符号不变，第一个二次项经分部积分变成 $-\int\lvert\Psi'\rvert(\delta X_r/r)^2\,\mathrm{d}V$，得到所述形式。在半径为 $r$ 的球面上，每个均值为零的函数 $\psi$ 满足 $\int\lvert\nabla_{\mathrm{s}}\psi\rvert^2\,\mathrm{d}S \ge (2/r^2)\int\psi^2\,\mathrm{d}S$，因为球面上 Laplace 算子最小的非零特征值是 $l(l + 1)/r^2$，$l = 1$（球谐函数，[2.5.5](/2.5.5)），$\psi \propto x_1$ 时取等号；$\delta X_r$ 在每个球面上均值为零，所以对每个球面积分后被积函数非负。当 $\Psi'$ 变号时，分部积分在它的零点处产生边界项，给出失稳的贡献。$\square$

等号情形 $l = 1$ 是各层相对彼此的平移，是不同心球的连续对应。$\Psi'$ 零点处的失稳有明确的含义：在这样的半径附近，局部张力向外增大，交换两层可以降低自由能。由于流体图像在复原内部化的分层方面并不比局部动力学分选更好，就不应指望它解释复杂结构的最终排列。幸运的是，脊椎动物发育的早期运动（原肠作用）主要与内部化本身有关，较难描述的结构出现在后面；实际上，胚胎倾向于表现出洋葱状结构的居中，而不是它们的破裂，仅靠差异黏附无法解释这一点（7.5.7，§7.2）。

## 8.8. 单个细胞的力学：表面不稳定性与卵裂

同样的方程适用于单个细胞，其表面带有控制张力的分子。设 $c(\boldsymbol{x}, t)$ 是 $S$ 上一种表面物质（"表面活性剂"）的浓度，且 $\gamma = \gamma(c)$。若 $c$ 在随表面运动的小片 $S'$ 上守恒，则 $\frac{\mathrm{d}}{\mathrm{d}t}\int_{S'}c\,\mathrm{d}S' = F$，即穿过其边界的通量。变化率包含局部变化与面积变化，$\int(\partial_tc + c\,(\nabla\cdot\boldsymbol{n})\,\boldsymbol{u}\cdot\boldsymbol{n})\,\mathrm{d}S'$；切向流动带来的通量由 Stokes 定理计算。加上表面扩散和源，得到

**公式 8.8.1（运动表面上的表面活性剂守恒）**

$$
\frac{\partial c}{\partial t} + \boldsymbol{u}_{\mathrm{t}}\cdot\nabla_{\mathrm{s}}c + c\,\Gamma = D\nabla_{\mathrm{s}}^2c + r(c), \qquad
\Gamma = (\boldsymbol{u}\cdot\boldsymbol{n})\,\nabla\cdot\boldsymbol{n} + \nabla_{\mathrm{s}}\cdot\boldsymbol{u}_{\mathrm{t}},
$$
其中 $\boldsymbol{u}_{\mathrm{t}} = \boldsymbol{u} - (\boldsymbol{u}\cdot\boldsymbol{n})\boldsymbol{n}$ 是切向速度，$\Gamma$ 是表面积的膨胀率（来自弯曲表面的法向运动和切向流动的散度），$\nabla_{\mathrm{s}}^2$ 是表面上的 Laplace 算子，$D$ 是表面扩散系数（无量纲，$\eta D_{\mathrm{dim}}/(\gamma_0L_0)$），$r$ 是反应项。当 $r \ne 0$ 时，这是运动表面上的反应扩散系统（7.5.12）；对于多种物质，$c$ 与 $D$ 成为向量与对角矩阵。

张力与输运的耦合使均匀态不稳定。Greenspan（1977）分析了一个均匀覆盖着守恒表面活性剂的黏性球，该表面活性剂使表面张力升高（$\gamma'(c) > 0$），并证明当表面活性剂的扩散系数足够小时，均匀态变得不稳定。机制是一个正反馈：$c$ 的局部过量使那里的 $\gamma$ 升高；Marangoni 力（定理 8.4.1）把表面拉向高张力区域；流动把更多的表面活性剂带到那里。扩散对抗积累。随着 $D$ 减小，$P_1$ 模式（极化的帽）首先被激发，其次是 $P_2$ 模式；$P_2$ 模式把张力集中在赤道带，使细胞在那里缢缩，这是卵裂的力学模型，不过由于线性理论的对称性，相反的符号（两极处的凹陷）同样是可能的。

一个最小模型显示了机制和模式的次序。考虑半径为 $R$ 的球形细胞的一条子午线（弧长为 $s$）上的薄收缩表面层，其中有一种使张力升高的物质 $c$，张力为 $T(c)$，与细胞内部的摩擦为 $\xi$，表面黏度为 $\eta_{\mathrm{s}}$：

$$
\xi v - \eta_{\mathrm{s}}\frac{\partial^2v}{\partial s^2} = \frac{\partial T(c)}{\partial s}, \qquad
\frac{\partial c}{\partial t} = -\frac{\partial(cv)}{\partial s} + D\frac{\partial^2c}{\partial s^2} + k(c_0 - c),
\tag{8.5}
$$
其中 $k$ 是朝向均匀水平 $c_0$ 的周转速率。在 $c = c_0$ 附近线性化，$c - c_0 \propto \mathrm{e}^{\mathrm{i}qs + st}$，力平衡给出 $\hat v = \mathrm{i}qT'(c_0)\hat c/(\xi + \eta_{\mathrm{s}}q^2)$，增长率为

$$
s(q) = q^2\Bigl[\frac{c_0T'(c_0)}{\xi + \eta_{\mathrm{s}}q^2} - D\Bigr] - k.
$$
在封闭的子午线上 $q = n/R$。由于括号中的第一项随 $q$ 减小，阈值扩散系数 $c_0T'(c_0)/(\xi + \eta_{\mathrm{s}}n^2/R^2)$ 对 $n = 1$ 最大，其次是 $n = 2$，与 Greenspan 的结果一致；表面黏度与扩散抑制短波。子午线上的模式 $n = 2$ 在圆上给出两个相对的极大值，在细胞上这是赤道处的一个环（图 6）。

![收缩表面层是不稳定的（式 (8.5)）。A：三个扩散系数下子午线上模式 cos(ns/R) 的增长率（ξ = 1，η_s = 0.25，c0T′(c0) = 2，k = 0.1）：随着 D 下降，模式 1（极帽）和模式 2（两个相对的极大值）首先变得不稳定，短波保持稳定。B：D = 0.5 时从 1% 噪声出发的模拟：浓度聚集成两个相对的峰并达到饱和。C：细胞轮廓上的最终图案，旋转使一个峰位于赤道：一个高张力环，即卵裂沟的几何形状](./plots/cortical-instability.py)

这与真实的卵裂相比如何？**胞质分裂**（[7.3.21](/7.3.21)）的现代观点保留了力学，但改变了图案的成因。表面层是肌动球蛋白皮层，使张力升高的物质是活性的 II 型**肌球蛋白**，式 (8.5) 是皮层流动的主动凝胶模型（Bois、Jülicher 和 Grill，2011）的一维版本，这些模型重现了胞质分裂中看到的朝向赤道的流动，以及在 *C. elegans* 合子中建立 PAR 极性的极化流动（7.5.6）。但是**收缩环**的位置不是由自发的不稳定性选择的：它由**有丝分裂纺锤体**指定，纺锤体的中央纺锤体和星体**微管**把 RhoA 的激活因子（centralspindlin 及其伴侣 Ect2）送到赤道区，并抑制两极的收缩性。自我增强的流动随后使纺锤体播下的图案变得清晰并维持下去。因此，Greenspan 的模型对于使张力升高的、被平流输运的表面物质的力学是正确的，而把不稳定性当作卵裂沟位置的原因这一点则是错误的。

在胚胎的尺度上，同样的想法以另一种形式出现：Turing 晚期关于生长球壳上反应扩散图案的工作表明，当球壳生长超过临界尺寸时，一个模式可以被激发；如果**形态发生素**使表面张力升高，所得的张力图案就驱动组织流动；这一点，以及被它所引起的流动平流的张力分布的非线性变陡，将在 7.5.9 中针对两栖类原肠作用讨论。

## 8.9. 主动力：肌动球蛋白皮层

上述模型中的张力不是被动的。动物细胞的表面衬有**细胞皮层**，这是由**肌动蛋白丝**组成、被 II 型**肌球蛋白**交联并收缩的薄网络（[7.3.13](/7.3.13)）。它的收缩使细胞表面处于张力之下，在圆形细胞中这与内部的静水压平衡。

**定义 8.9.1（皮层张力）** 细胞的**皮层张力**是它表面中的张力（单位长度的力），主要由肌动蛋白皮层的肌球蛋白 II 收缩产生，在较小程度上由膜张力产生；它起液滴表面张力的作用。

皮层张力用微管吸吮测量：把半径为 $R_{\mathrm{c}}$ 的细胞吸入半径为 $R_{\mathrm{p}}$ 的吸管，在被吸入的舌状部分长度达到 $R_{\mathrm{p}}$（半球）时的压差 $\Delta P$ 下，对两个曲面应用 Young–Laplace 方程，得 $\sigma_{\mathrm{c}} = \Delta P/\bigl[2(1/R_{\mathrm{p}} - 1/R_{\mathrm{c}})\bigr]$。其值依细胞类型而异，约从 $10^{-5}$ 到 $10^{-3}\,\mathrm{N\,m^{-1}}$，远低于**组织表面张力**的 $10^{-3}$–$2\times10^{-2}\,\mathrm{N\,m^{-1}}$，后者不是单个细胞的张力，而是组织的性质。

皮层也解释了黏附如何起作用（7.5.7，§7.5）：接触的张力是接触两侧的皮层张力减去黏附能，**钙黏蛋白**连接在局部发出信号，使皮层收缩性降低。组织内收缩性的梯度产生形态发生的主动力。在顶端收缩中，顶端皮层的收缩使上皮细胞的顶面变窄并使其成楔形，从而使细胞片弯曲：在果蝇腹沟中，在转录因子 Twist 和 Snail 的控制下，顶端肌动球蛋白网络以脉冲方式收缩，一个棘轮机制使每一步稳定下来（Martin、Kaschube 和 Wieschaus，2009）；在脊椎动物的**神经板**细胞中，蛋白质 Shroom 把 Rho 激酶招募到顶端连接（7.5.18）。连接本身的平面极化收缩性驱动邻居交换（8.10）和**汇聚伸展**中的组织伸长（7.5.9）。力学反馈（张力使肌球蛋白稳定，拉伸激活信号）把本章的力学与细胞信号联系起来。

## 8.10. 顶点模型与流固转变

在连续介质力学与基于细胞的模拟之间是上皮的顶点模型，其中每个细胞是一个多边形，自由度是它的顶点的位置。

**算法 8.10.1（顶点模型）**（Farhadifar 等，2007；Bi 等，2015）上皮是平面被多边形 $\alpha$ 的铺砌，多边形的面积为 $A_\alpha$，周长为 $P_\alpha$。

1. 定义能量 $E = \sum_\alpha\bigl[K_A(A_\alpha - A_0)^2 + K_P(P_\alpha - P_0)^2\bigr]$：面积项表示细胞体积与高度对改变的抵抗，周长项表示皮层收缩性（倾向于小的 $P$）与黏附（倾向于长的接触）之间的竞争，具有偏好周长 $P_0$。
2. 用过阻尼动力学移动顶点，$\zeta\,\dot{\boldsymbol{r}}_i = -\partial E/\partial\boldsymbol{r}_i$（梯度流，例 8.6.1），可以加上主动力和随机力。
3. 当某个连接短于阈值时，进行 T1 转变：连接收缩成四重顶点，后者在垂直方向上化解为新的连接，于是两个细胞失去接触，另两个细胞获得接触（图 7A）。
4. 可选地加入细胞分裂和挤出。

T1 转变是细胞交换邻居、使组织流动的基本步骤。在模型的无量纲形式中，关键参数是目标形状指数 $p_0 = P_0/\sqrt{A_0}$。Bi、Lopez、Schwarz 和 Manning（2015）证明，当 $p_0$ 超过临界值 $p_0^* \approx 3.81$ 时，T1 转变的能垒消失：低于它组织是固体（细胞被邻居困住），高于它则是流体。细胞的观察形状指数 $q = P/\sqrt{A}$ 是实验的序参量：在类固体组织中细胞大致各向同性且紧凑（$q$ 低），在类流体组织中则伸长且不规则（图 7B）。这已被用来证明气道上皮在与哮喘相关的应激下解除堵塞（Park 等，2015），以及脊椎动物的体轴通过堵塞转变伸长，尾芽中类流体的组织在前体节**中胚层**中变成类固体（Mongera 等，2018，斑马鱼）。这类主动材料的统计物理现在是组织力学的一种主要方法，并且回到了 Percus 和 Childress 的补充说明所提出的问题：细胞所做的远不止黏附。它们变形、伸出突起、断开和形成接触、相对彼此运动，并在**细胞骨架**中产生应力，对聚集体中细胞变形和运动的合适模型仍在构建中。

![顶点模型。A：T1 转变：细胞 1 和 3 共有的连接收缩成四重顶点，细胞 2 与 4 之间形成新的连接，于是邻居被交换；T1 转变是组织流动以及汇聚伸展使其变窄变长的方式。B：几种规则形状的形状指数 p = P/√A（圆 3.545，正六边形 3.722，正方形 4.0），以及顶点模型在目标形状指数 p0* ≈ 3.81 处的刚性转变：低于它的组织表现为固体，高于它的表现为流体](./plots/vertex-t1.py)

## 小结

| 主题 | 主要结果 |
|---|---|
| 作为液体的组织（8.1） | 黏度 $10^5$–$10^7\,\mathrm{Pa\,s}$，短时间内为弹性：Maxwell 液体（定义 8.1.1，式 (8.1)），$t_{\mathrm{r}} = \eta/G$；松弛、蠕变、启动 |
| 位点模型（8.2） | 位点守恒 $n_t + (un)_s = q$，$T = g(n)$；滑动：端点移动的热方程，$U$ 与 $L$（命题 8.2.1），时间尺度 $L_0^2/K$；间质膜：$L = 2n_0L_0/(n_0 + n_1)$，Laplace 变换解，$k_{\mathrm{eff}} = 3kn_0/2L_0$，$\eta_{\mathrm{eff}} = L_0n_0^2f$，$t_{\mathrm{r}} = 2L_0^2/3K$（定理 8.2.2） |
| 连续介质方程（8.3） | 形态动力学（定义 8.3.1）；带生长的连续性方程（式 (8.3)）；Newton 应力，Navier–Stokes（式 (8.4)）；物质导数；不可压缩 ≠ 密度为常数；Maxwell 流体 |
| 表面力（8.4） | 牵引力 $-\gamma(1/R_1 + 1/R_2)\boldsymbol{n} + \nabla_{\mathrm{s}}\gamma$（定理 8.4.1）；$\nabla\cdot\boldsymbol{n} = 1/R_1 + 1/R_2$（命题 8.4.2） |
| 尺度（8.5） | $U_0 \sim \gamma_0/\eta \sim 10^{-8}\,\mathrm{m\,s^{-1}}$，每毫米一天；$\operatorname{Re} \sim 10^{-14}$：Stokes 流（定义 8.5.1）；生长数 $\Pi$；变圆速率 $\frac{20}{19}\gamma/\eta R$，融合 $(x/a)^2 = 3\gamma t/2\eta a$（例 8.5.1） |
| 能量（8.6） | 表面能以耗散的速率下降（定理 8.6.1）；体积势 $\phi$，体力 $\nabla\phi\,\nabla\cdot\boldsymbol{n}$，体积自由能 $\int\lvert\nabla\phi\rvert$（定理 8.6.2）；Rayleigh 耗散函数（定义 8.6.1）与原理 $\delta(\dot E + \Phi/2) = 0$（定理 8.6.3）→ 带阻力矩阵的梯度流（例 8.6.1） |
| 稳定性（8.7） | 液体层变薄而不破裂；连续洋葱中性稳定（球面不等式，$l = 1$），在 $\Psi'$ 的零点处不稳定（定理 8.7.1） |
| 单个细胞（8.8） | 带膨胀项的表面活性剂守恒（公式 8.8.1）；$\gamma'(c) > 0$、$D$ 小时的 Greenspan 不稳定性；$s(q) = q^2[c_0T'/(\xi + \eta_{\mathrm{s}}q^2) - D] - k$（式 (8.5)）：先是模式 1，然后是模式 2（赤道环）；在细胞中由纺锤体定位 RhoA 区 |
| 主动力（8.9） | 皮层张力（定义 8.9.1），微管吸吮；顶端收缩（脉冲式、棘轮式），Shroom，平面极化收缩性 |
| 顶点模型（8.10） | $E = \sum K_A(A - A_0)^2 + K_P(P - P_0)^2$，T1 转变（算法 8.10.1）；$p_0^* \approx 3.81$ 处的刚性转变；气道上皮和斑马鱼尾芽中的堵塞 |

## 思考题

1. 一块组织聚集体被突然压缩，保持压缩所需的力在 $4\,\mathrm{min}$ 内降到初始值的 $1/\mathrm{e}$。瞬时剪切模量估计为 $G = 500\,\mathrm{Pa}$。黏度是多少？在持续 $2\,\mathrm{h}$ 的原肠作用运动中，聚集体表现为弹性固体还是液体？

   **答** 衰减时间就是松弛时间，$t_{\mathrm{r}} = 240\,\mathrm{s}$，所以 $\eta = Gt_{\mathrm{r}} = 500 \times 240 = 1.2\times10^5\,\mathrm{Pa\,s}$，在测量范围之内。两小时是 $t/t_{\mathrm{r}} = 30$，所以弹性应力已完全松弛，组织表现为黏性液体；只有快于几分钟的运动才会感受到它的弹性。

2. 利用命题 8.2.1，求 $L_0 = 10\,\mu\mathrm{m}$、$K = 10^{-14}\,\mathrm{m^2\,s^{-1}}$、被拉到 $n_1/n_0 = 0.8$ 的膜线段的稳定滑动速度与长度，以及达到这一状态所需的时间。

   **答** $U = (K/L_0)(1 - 0.8) = (10^{-14}/10^{-5})\times0.2 = 2\times10^{-10}\,\mathrm{m\,s^{-1}}$（约每小时 $0.7\,\mu\mathrm{m}$）；$L = L_0\ln(1.25)/0.2 = 10\times0.223/0.2 \approx 11.2\,\mu\mathrm{m}$。松弛时间的量级是 $L_0^2/K = 10^{-10}/10^{-14} = 10^4\,\mathrm{s}$，约 3 小时（图 2 表明在 $tK/L_0^2 \approx 1$ 时达到稳态）。

3. 在间质膜模型中，有效黏度和松弛时间如何依赖接触长度 $L_0$ 与位点密度 $n_0$？这对增加钙黏蛋白表达的细胞预测什么？

   **答** $\eta_{\mathrm{eff}} = L_0n_0^2f$ 随接触长度线性增长，随位点密度二次增长；$t_{\mathrm{r}} = 2L_0^2/(3K) = 2L_0^2fn_0/(3k)$ 按 $L_0^2$ 增长，并随 $n_0$ 线性增长。黏附位点更多（钙黏蛋白更多）的细胞应当形成黏度更高、松弛更慢的组织（并且更强的黏附使接触更大，使两者进一步增大），这与内聚性强的组织运动缓慢的定性观察一致；模型没有给出 $f$ 与黏附能之间的联系，所以不能预测表面张力。

4. 证明对半径为 $R$、张力均匀的球，定理 8.4.1 给出熟悉的压强跃变，并且均匀张力在球形聚集体中不产生流动。如果一个极处的张力较高，会怎样？

   **答** 在球上 $R_1 = R_2 = R$，$\nabla_{\mathrm{s}}\gamma = 0$，所以牵引力是 $-2\gamma/R$ 乘外法向：内部压强比外部大 $2\gamma/R$。均匀的内部压强 $p = 2\gamma/R$ 与 $\boldsymbol{u} = \boldsymbol{0}$ 满足 Stokes 方程和边界条件，由 Stokes 流的唯一性，它就是解：没有流动。若一个极处张力较高，切向牵引力 $\nabla_{\mathrm{s}}\gamma$ 在整个表面上指向该极，把表面物质拖向它；内部通过两个环流使物质返回（图 4B）；球也发生变形，张力梯度强时在张力高处变扁。

5. 估计在黏度为 $10^5\,\mathrm{Pa\,s}$ 的组织中，以 $1\,\mu\mathrm{m\,min^{-1}}$ 迁移 $100\,\mu\mathrm{m}$ 距离的中胚层细胞运动的 Reynolds 数。这对建模有什么实际后果？

   **答** $U = 1.7\times10^{-8}\,\mathrm{m\,s^{-1}}$，$L = 10^{-4}\,\mathrm{m}$，$\rho = 10^3\,\mathrm{kg\,m^{-3}}$：$\operatorname{Re} = 10^3\times1.7\times10^{-8}\times10^{-4}/10^5 \approx 1.7\times10^{-14}$。惯性可以完全略去：力在每一时刻都平衡（Stokes 流，过阻尼的细胞运动），速度与力成正比，历史只通过变化的几何形状和材料的黏弹性记忆进入。

6. 利用 Rayleigh 原理，对自由能 $E(q) = \frac12\kappa(q - q_0)^2$、耗散 $\Phi = c\,\dot q^2$ 的单个形状坐标 $q$ 推导运动方程。松弛时间是多少？把结果与例 8.5.1 联系起来。

   **答** $\partial E/\partial q + \frac12\partial\Phi/\partial\dot q = \kappa(q - q_0) + c\dot q = 0$，所以 $q - q_0 \propto \mathrm{e}^{-t\kappa/c}$，松弛时间为 $c/\kappa$。对于变形的液滴，$\kappa \sim \gamma$（单位形变振幅平方的表面能，至多差几何因子），$c \sim \eta R$（速度为 $\dot q$ 的流动在体积 $R^3$ 上、梯度为 $\dot q/R$ 时的耗散，按单位振幅变化率的平方计，同样至多差因子），给出时间 $\sim\eta R/\gamma$，与精确速率 $\frac{20}{19}\gamma/(\eta R)$ 一致。

7. 从物理上解释，在定理 8.7.1 中为什么 $\delta X_r \propto x_1$（即 $l = 1$）的位移到二阶不耗能，以及为什么 $\Psi'$ 的零点起失稳作用。对混合聚集体可以做什么实验来检验"内部分层不会被类流体运动破坏"这一预测？

   **答** $l = 1$ 的位移逐层看，是每个球形层相对邻层的刚性平移：界面面积以及表面能到二阶都不变，正如不同心的球形界面不需要额外的能量。在 $\Psi'$ 的零点处，张力的次序反转：局部上，张力高的材料位于张力低的材料之外，这对于**包围**是错误的次序，交换相邻的层会降低能量，所以扰动增长。检验：构造一个次序"错误"的聚集体（例如在内聚性强的核外面包上内聚性较弱的组织壳，再加上本应在内部的第三种组织），观察错误次序的层是破裂（离散的细胞可以突破）还是只是变薄并持续存在；并与细胞追踪比较，看细胞是否逐个穿过该层。

8. 在式 (8.5) 中取 $\xi = 1$、$\eta_{\mathrm{s}} = 0.25$、$c_0T'(c_0) = 2$、$k = 0.1$、$R = 1$，求模式 $n = 2$（赤道环）不稳定的扩散系数 $D$ 的范围，以及 $n = 2$ 是增长最快模式的范围。

   **答** $s_2 = 4[2/(1 + 1) - D] - 0.1 = 3.9 - 4D > 0$ 当 $D < 0.975$。比较各模式，$s_n = n^2[2/(1 + 0.25n^2) - D] - 0.1$；$s_2 > s_1$ 要求 $4 - 4D > 1.6 - D$，即 $D < 0.8$；$s_2 > s_3$ 要求 $4 - 4D > 9(2/3.25) - 9D = 5.54 - 9D$，即 $D > 0.308$。所以 $0.31 < D < 0.8$ 时 $n = 2$ 增长最快（$D = 0.5$ 时：$s_1 = 1.0$，$s_2 = 1.9$，$s_3 = 0.94$，如图 6A）；$D$ 更小时，更高的模式取而代之。

9. （实验设计）你如何检验卵裂沟的位置是由自发的皮层不稳定性（如 Greenspan 模型）还是由来自纺锤体的信号决定的？

   **答** 移动纺锤体（显微操作，或如 Rappaport 实验那样离心卵，或光遗传学牵引），看卵裂沟是否随之移动：如果它在新的纺锤体中区之上形成，就是纺锤体指定位置。Rappaport 的环形实验中，在两个没有纺锤体相连的星体之间形成卵裂沟，表明星体微管就足够了。反过来，在没有纺锤体信号的细胞皮层的异位位置光遗传学激活 RhoA，检验仅靠皮层反馈能否产生并维持卵裂沟。测量皮层流动（追踪肌球蛋白颗粒）检验式 (8.5) 的平流反馈：流动应当向卵裂沟汇聚，减弱它们（降低肌球蛋白活性）应使带变宽。

10. 一片多边形细胞的平均周长为 $P = 16\,\mu\mathrm{m}$，平均面积为 $A = 16\,\mu\mathrm{m^2}$；经过实验处理后，数值变为 $P = 15\,\mu\mathrm{m}$，$A = 18\,\mu\mathrm{m^2}$。用顶点模型的判据，处理前后组织是类流体还是类固体？处理可能产生了什么细胞水平的变化？

    **答** 处理前：$q = 16/\sqrt{16} = 4.0 > 3.81$，类流体。处理后：$q = 15/\sqrt{18} \approx 3.54 < 3.81$，类固体（近乎圆形，低于正六边形的值 3.72）。细胞变得更紧凑：连接收缩性增强或黏附降低，使偏好周长 $P_0$ 相对于 $\sqrt{A_0}$ 下降，在顶点模型中这提高了 T1 转变的能垒，使组织堵塞。可以通过测量邻居交换率（每个细胞每小时的 T1 事件数）来检验，它应当下降。
