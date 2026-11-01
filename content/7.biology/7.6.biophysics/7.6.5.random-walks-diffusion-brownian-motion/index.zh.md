---
title: 随机行走、扩散与 Brown 运动
description: 细胞中热运动的动力学。随机行走与均方位移、持续性行走与扩散系数；从蛋白质到轴突的扩散时间；扩散方程与 FRAP 的 Fourier 级数解；扩散捕获（4πDac、a/r₀）、细胞大小与反应速率的扩散极限以及 Péclet 数；漂移与扩散、Smoluchowski 方程、Einstein 与 Stokes–Einstein 关系、Nernst 电势与转动扩散；Langevin 方程、涨落–耗散定理与 Ornstein–Uhlenbeck 过程；主方程与 Fokker–Planck 方程；平均首达时间与 Kramers 越垒速率。
source_hash: fb4e84e06bf9
---

细胞里的一切都在抖动。细胞质中的蛋白质每秒被水分子撞击约 $10^{13}$ 次，每皮秒就改变一次运动方向，却仍能在百分之几秒内游过一个细菌。本章导出这种运动的规律，并说明它们如何塑造细胞。一系列独立的步骤产生随时间线性增长的**均方位移**（5.1），这使扩散在短距离上很快、在长距离上无望；扩散方程把同样的论断变成场论，解释光漂白实验，并给出分子找到靶标的速率（5.2）。力给扩散增加漂移，而要求漂移与扩散平衡成 [7.6.2](/7.6.2) 的 **Boltzmann 分布**，就确定了扩散与摩擦之间的关系（5.3）。Langevin 方程描述单个粒子，并表明摩擦与涨落是同样的碰撞的两个面（5.4）；主方程与 Fokker–Planck 方程描述概率（5.5）；而越过能垒的时间，即 Kramers 速率，把扩散与 [7.6.3](/7.6.3) 和 [7.6.4](/7.6.4) 中用到的构象变化速率联系起来（5.6）。**热传导方程**的数学见 [2.5.1](/2.5.1) 和 [2.5.7](/2.5.7)，胶体的 **Brown 运动**与 Perrin 对 Avogadro 常量的测量见 [6.3.21](/6.3.21)，**扩散控制反应**的速率见 [6.3.17](/6.3.17)，单粒子追踪与 FRAP 的显微术见 [7.3.2](/7.3.2)；这里使用它们而不重新推导。这些结果在整个课程中反复出现：分子大小的流体力学测量（[7.6.8](/7.6.8)）、单分子方法（[7.6.12](/7.6.12)、[7.6.17](/7.6.17)）、拥挤的细胞质（[7.6.23](/7.6.23)）、马达（[7.6.27](/7.6.27)）、基因表达的随机动力学（[7.6.32](/7.6.32)）以及感知的物理极限（[7.6.35](/7.6.35)）。

## 5.1. 随机行走

### 5.1.1. 随机行走及其均方位移

Brown 粒子，即蛋白质或一微米的小球，比周围的水分子重得多。每次碰撞只使它的速度略有改变，但碰撞如此频繁而又如此不相关，以至短时间之后粒子就忘记了它先前的方向。在长于这种记忆的时间尺度上，它的运动是一系列独立位移。

**定义 5.1.1（随机行走）** $d$ 维的**随机行走**是位置序列 $\boldsymbol{r}_N = \boldsymbol{r}_0 + \sum_{i=1}^{N}\Delta\boldsymbol{r}_i$，其中每隔 $\tau$ 走出的步 $\Delta\boldsymbol{r}_i$ 是独立同分布的随机向量。若 $\langle\Delta\boldsymbol{r}_i\rangle = \boldsymbol{0}$，则行走是无偏的。

**定理 5.1.1（随机行走的均方位移）** 对步方差为 $\langle\lvert\Delta\boldsymbol{r}\rvert^2\rangle = a^2$ 的无偏随机行走，$N$ 步后的位移均值为 $\boldsymbol{0}$，并且

$$
\langle\lvert\boldsymbol{r}_N - \boldsymbol{r}_0\rvert^2\rangle = Na^2 = 2dDt, \qquad D = \frac{a^2}{2d\tau}, \quad t = N\tau,
$$

对大的 $N$，每个直角分量近似服从方差为 $2Dt$ 的正态分布。

**证明** 均值为零，因为每一步的均值为零。把和平方，

$$
\left\lvert\sum_{i=1}^{N}\Delta\boldsymbol{r}_i\right\rvert^2 = \sum_{i=1}^{N}\lvert\Delta\boldsymbol{r}_i\rvert^2 + \sum_{i \ne j}\Delta\boldsymbol{r}_i\cdot\Delta\boldsymbol{r}_j ,
$$

由独立性，对 $i \ne j$ 有 $\langle\Delta\boldsymbol{r}_i\cdot\Delta\boldsymbol{r}_j\rangle = \langle\Delta\boldsymbol{r}_i\rangle\cdot\langle\Delta\boldsymbol{r}_j\rangle = 0$，所以只剩下 $N$ 个对角项。每个分量是 $N$ 个独立同分布变量之和，**中心极限定理**（[3.1.13](/3.1.13)）给出正态极限；由对称性，$d$ 个分量中每个每步贡献 $a^2/d$，方差为 $Na^2/d = 2Dt$。$\square$

平方根是扩散的本质：典型距离按 $\sqrt{t}$ 增长，所以走十倍远要花一百倍的时间。连接距离与时间的常数，是实验所测量的性质。

**定义 5.1.2（扩散系数）** 粒子的**扩散系数**为

$$
D = \lim_{t \to \infty}\frac{\langle\lvert\boldsymbol{r}(t) - \boldsymbol{r}(0)\rvert^2\rangle}{2dt},
$$

其中 $d$ 是粒子运动的维数；其 SI 单位是 $\mathrm{m^2\,s^{-1}}$，细胞生物学中通常用 $\mu\mathrm{m^2\,s^{-1}}$ 表示。

因此被追踪粒子的**均方位移**（见 [7.3.2](/7.3.2)）在一维中按 $2Dt$ 增长，二维中按 $4Dt$，三维中按 $6Dt$；对线性增长的偏离揭示限制、拥挤或定向运动（[7.6.12](/7.6.12)、[7.6.23](/7.6.23)）。图显示中心极限定理起作用很快：仅仅十步等长的步之后，一个坐标的分布就已接近 Gauss 分布。

![二维随机行走，每隔 τ 沿随机方向走长度为 a 的一步，所以 ⟨r²⟩ = Na² = 4Dt，D = a²/4τ。A：从原点出发的五条 1000 步行走；虚线圆的半径为 √N a。B：对 2000 个行走者平均的均方位移（点），以及三条单个行走的时间平均 MSD（细线），对 Na² 作图；单条轨迹围绕系综线散布，在可用独立区间较少的长滞后处更甚。C：x 坐标的分布，以 √N a 标度，经 10 步和 400 步后，与中心极限定理预言的方差为 1/2 的 Gauss 分布比较](./plots/random-walk.py)

### 5.1.2. 相关的步

如果相继的步相关，行走在长时间仍是扩散的，但系数不同。设每一步长为 $\ell$，相邻两步夹角的余弦平均为 $\alpha$，与更早的步无关；则 $\langle\Delta\boldsymbol{r}_i\cdot\Delta\boldsymbol{r}_{i+k}\rangle = \ell^2\alpha^k$。

**公式 5.1.1（持续性随机行走）** 对 $N \gg 1/(1 - \alpha)$ 步，

$$
\langle\lvert\boldsymbol{r}_N - \boldsymbol{r}_0\rvert^2\rangle = N\ell^2 + 2\ell^2\sum_{k=1}^{N-1}(N - k)\alpha^k \approx N\ell^2\frac{1 + \alpha}{1 - \alpha}, \qquad D = \frac{\ell^2}{2d\tau}\cdot\frac{1 + \alpha}{1 - \alpha}.
$$

正相关（$\alpha > 0$，持续性运动）使 $D$ 增大；负相关（$\alpha < 0$，有恢复的倾向）使之减小。同样的数学描述聚合物的形状：由 $N$ 段长度为 $a$ 的自由连接的链段构成的链是空间中的随机行走，所以它的端到端距离为 $\sqrt{\langle R^2\rangle} = \sqrt{N}a$（**自由连接链**），相继链段方向之间的相关使它按公式 5.1.1 的因子增大（[7.6.21](/7.6.21)）。

**例 5.1.1（游动的细菌）** *E. coli* 以 $v \approx 25\,\mu\mathrm{m\,s^{-1}}$ 的速度作持续约 $\tau = 1\,\mathrm{s}$ 的直线奔跑，其间被使它平均转向约 $68^\circ$ 的翻滚隔开，所以 $\alpha = \cos 68^\circ \approx 0.33$（Berg 与 Brown，1972）。把每次奔跑视为三维中 $\ell = 25\,\mu\mathrm{m}$ 的一步，$D = (25^2/6)(1.33/0.67) \approx 2\times10^{2}\,\mu\mathrm{m^2\,s^{-1}}$。游动的细菌因此像小分子一样扩散，比同样大小的被动粒子快一千倍（由下面的式 (5.3)，$D \approx 0.2\,\mu\mathrm{m^2\,s^{-1}}$）。**趋化性**通过使奔跑在上坡方向变长而使这种行走产生偏向（[7.6.35](/7.6.35)）。

### 5.1.3. 扩散时间

定理 5.1.1 变成细胞物理中最有用的估算：扩散距离 $L$ 所需的时间为

$$
t \approx \frac{L^2}{2dD}. \tag{5.1}
$$

典型的扩散系数跨越六个数量级。

| 分子与介质 | $D$ / ($\mu\mathrm{m^2\,s^{-1}}$) |
|---|---|
| 水中的 $\ce{O2}$，$25\,{}^\circ\mathrm{C}$ | $2\times10^{3}$ |
| 水中的葡萄糖 | $6\times10^{2}$ |
| 水中的 GFP（$27\,\mathrm{kDa}$） | $87$ |
| 哺乳动物细胞质中的 GFP | $20$–$30$ |
| *E. coli* 细胞质中的 GFP（Elowitz 等，1999） | $8$ |
| 流体双层中的脂质 | $1$ |
| 质膜中的膜蛋白 | $0.01$–$0.1$ |
| *E. coli* 中的 mRNA–蛋白质颗粒（Golding 与 Cox，2006） | $\sim 0.03$ |

一个 GFP 分子穿过细菌（$L = 1\,\mu\mathrm{m}$）需要 $1/(6 \times 8) \approx 0.02\,\mathrm{s}$，穿过哺乳动物细胞（$L = 20\,\mu\mathrm{m}$，$D = 25\,\mu\mathrm{m^2\,s^{-1}}$）约 $3\,\mathrm{s}$，但沿 $1\,\mathrm{m}$ 长的运动轴突扩散需要 $(10^6)^2/(6 \times 25)\,\mathrm{s} \approx 7\times10^{9}\,\mathrm{s}$，即两个世纪。驱动蛋白以 $1\,\mu\mathrm{m\,s^{-1}}$ 运载货物，走完同样的距离需要 $10^{6}\,\mathrm{s}$，约十二天，而快速轴突运输还要快几倍。当 $L/v < L^2/(6D)$ 时，速度为 $v$ 的定向运输胜过扩散，即超过 $L^* = 6D/v$：对以 $1\,\mu\mathrm{m\,s^{-1}}$ 运载的蛋白质约为 $150\,\mu\mathrm{m}$。在这一距离以下，细胞依靠扩散；在其以上，它们需要马达、胞质流动或循环。同样的算术说明了为什么细菌不需要运输机器，为什么大细胞（卵、神经元、植物细胞）有，以及为什么大于约一毫米的生物需要循环。

![扩散造成的扩展。A：一维中在 t = 0 时于 x = 0 释放的分子的浓度分布，D = 25 µm² s⁻¹（真核细胞质中 GFP 大小的蛋白质），t = 0.1、1、10 和 30 s；箭头标出 ±√(2Dt)，即 Gauss 分布的标准差。B：扩散距离 L 的时间，三维中 t = L²/6D（膜蛋白在二维中为 L²/4D），分别对小分子（D = 1000 µm² s⁻¹）、真核细胞质中的蛋白质（25）、*E. coli* 中的蛋白质（7.7）和膜蛋白（0.1），并与 1 µm s⁻¹（驱动蛋白马达）和 30 µm s⁻¹（游动的细菌）的定向运输比较；点线竖线标出蛋白质、细菌、真核细胞和 1 m 轴突的大小](./plots/diffusion-times.py)

## 5.2. 扩散方程

### 5.2.1. 守恒与 Fick 定律

许多粒子扩散时，它们的浓度 $c(\boldsymbol{r}, t)$ 遵守两条定律。守恒指出，任何体积中粒子数只因通过其表面的通量而改变，$\partial c/\partial t + \nabla\cdot\boldsymbol{J} = 0$。**Fick 定律**（[2.5.1](/2.5.1)）指出通量正比于浓度梯度，$\boldsymbol{J} = -D\nabla c$，因为从拥挤一侧迈出的粒子比从稀疏一侧迈出的多。一维的计数使常数明确：设 $x$ 处宽为 $a$ 的格子中有 $N(x)$ 个粒子，在时间 $\tau$ 内每个格子的粒子一半向右、一半向左，所以穿过格子之间边界的净粒子数为 $[N(x) - N(x + a)]/2 \approx -\frac{a}{2}\partial_xN$，除以 $\tau$ 和截面积得 $J = -(a^2/2\tau)\partial_xc = -D\partial_xc$，其中 $D$ 即定理 5.1.1 的 $D$。两条定律结合给出**热传导方程**（[2.5.1](/2.5.1)），这里即扩散方程

$$
\frac{\partial c}{\partial t} = D\nabla^2c. \tag{5.2}
$$

**公式 5.2.1（点源）** 若 $N$ 个粒子在 $t = 0$ 于无界的 $d$ 维空间的原点释放，则

$$
c(\boldsymbol{r}, t) = \frac{N}{(4\pi Dt)^{d/2}}\,\mathrm{e}^{-r^2/4Dt},
$$

这是 [2.5.7](/2.5.7) 的**热核**，各方向的方差为 $2Dt$ 的 Gauss 分布。

许多独立行走者的浓度场就是单个行走者的概率密度乘以其数目：宏观的扩散方程与微观的随机行走是同一理论（[2.5.7](/2.5.7#sec-7.5.1)）。

### 5.2.2. FRAP：由恢复曲线读出 $D$

在**光漂白后荧光恢复**（[7.3.2](/7.3.2#sec-2.6.1)）中，细胞的一个区域被漂白，然后追踪荧光分子的返回。对细长的细胞，细菌或神经突，一维模型是合适的，它有精确解，显示恢复曲线包含什么。

**公式 5.2.2（一维 FRAP）** 设荧光分子在 $-L \le x \le L$ 中扩散，两端为反射壁，浓度均匀为 $c_0$，直到 $t = 0$ 时带 $\lvert x\rvert < a$ 被漂白。则

$$
c(x, t) = c_0\left[1 - \frac{a}{L} - \sum_{n=1}^{\infty}\frac{2}{n\pi}\sin\frac{n\pi a}{L}\cos\frac{n\pi x}{L}\,\mathrm{e}^{-Dn^2\pi^2t/L^2}\right],
$$

被漂白带的荧光相对于其漂白前的值 $2ac_0$ 为

$$
\frac{F(t)}{F_{\mathrm{pre}}} = 1 - \frac{a}{L} - \sum_{n=1}^{\infty}\frac{2L}{a\,n^2\pi^2}\sin^2\frac{n\pi a}{L}\,\mathrm{e}^{-Dn^2\pi^2t/L^2}.
$$

**证明** 在 $x = \pm L$ 处的无通量条件 $\partial_xc = 0$ 和初始条件的对称性选出余弦模式 $\cos(n\pi x/L)$，每个模式在式 (5.2) 下按 $\mathrm{e}^{-Dk_n^2t}$ 衰减，$k_n = n\pi/L$。系数由初始条件 $c(x, 0)$ 得出，它在 $a < \lvert x\rvert \le L$ 时为 $c_0$，在 $\lvert x\rvert < a$ 时为 $0$：均值为 $A_0 = c_0(1 - a/L)$，且

$$
A_n = \frac{2}{L}\int_0^Lc(x, 0)\cos\frac{n\pi x}{L}\,\mathrm{d}x = \frac{2c_0}{L}\int_a^L\cos\frac{n\pi x}{L}\,\mathrm{d}x = -\frac{2c_0}{n\pi}\sin\frac{n\pi a}{L}.
$$

把 $c(x, t)$ 在 $\lvert x\rvert < a$ 上积分，用 $\int_{-a}^{a}\cos(n\pi x/L)\,\mathrm{d}x = (2L/n\pi)\sin(n\pi a/L)$，再除以 $2ac_0$，就得到 $F/F_{\mathrm{pre}}$。在 $t = 0$ 处，由 $0 \le \theta \le \pi$ 时的恒等式 $\sum_n\sin^2(n\theta)/n^2 = \theta(\pi - \theta)/2$，级数之和为 $1 - a/L$，所以 $F(0) = 0$，符合要求。$\square$

该公式有三个特点在实践中要紧。荧光恢复到 $1 - a/L$ 而不是 $1$，因为被漂白的分子仍留在隔室中；比这更小的平台说明有不动的部分。每个模式以速率 $Dn^2\pi^2/L^2$ 衰减，所以恢复曲线的时间轴按 $1/D$ 标度，可以通过拟合读出 $D$（图的 C 部分）。而最慢的模式，决定最终趋近平台的快慢，由隔室的大小 $L^2/(\pi^2D)$ 而不是被漂白区域的大小决定：在小细胞中必须对几何建模，这就是为什么无限大膜中光斑的公式（[7.3.2](/7.3.2#sec-2.6.1)）不适用于细菌。

一种互补的方法不用扰动而用涨落。在**荧光相关光谱**（FCS）中，激光聚焦到半径约 $0.3\,\mu\mathrm{m}$、体积 $1\,\mathrm{fL}$ 的体积，小到每次只有几个荧光分子在其中；随着它们扩散进出，荧光涨落，其自相关函数在分子穿过束腰 $w$ 所需的时间 $\tau_{\mathrm{D}} = w^2/4D$ 上衰减。对轴向与横向之比为 $\omega$ 的三维 Gauss 体积，$G(\tau) = \frac{1}{\langle N\rangle}\left(1 + \tau/\tau_{\mathrm{D}}\right)^{-1}\left(1 + \tau/\omega^2\tau_{\mathrm{D}}\right)^{-1/2}$：衰减时间给出 $D$，振幅给出体积中分子的平均数 $\langle N\rangle$，从而给出绝对浓度。FRAP 与 FCS 在不同尺度上测量同样的扩散系数，FRAP 追踪大扰动的弛豫，FCS 观察平衡涨落的弛豫；两者都有效，是 5.4 的涨落–耗散定理的结果。FCS 的推导以及建立在其上的单分子方法见 [7.6.12](/7.6.12)。

![一维 FRAP。长度 2L = 10 µm、两端为反射壁的隔室，荧光均匀，直到带 |x| < a = 1 µm（阴影）在 t = 0 时被漂白。A：D = 5 µm² s⁻¹ 时 t = 0、0.02、0.1、0.5 和 2 s 的浓度分布，来自公式 5.2.2 的 400 项 Fourier 级数。B：D = 1、5 和 25 µm² s⁻¹ 时被漂白带的荧光相对于其漂白前值的变化，对数时间轴：各曲线是彼此的平移，并在 1 − a/L = 0.8 处趋平。C：D = 5 µm² s⁻¹、噪声 3 % 的模拟恢复数据，用级数拟合：拟合的 D 与真值在其标准误差内一致](./plots/frap.py)

### 5.2.3. 扩散捕获

许多生物过程是分子扩散到吸收体：养分到细菌、氧到线粒体、配体到受体、酶到底物。最简单的情形有闭式解，它给出所有其他情形的标度。

**公式 5.2.3（到球体的扩散限制通量）** 半径为 $a$、吸收到达其表面的每个分子的球体，在远处浓度为 $c_0$ 的介质中，其稳态浓度场与总通量为

$$
c(r) = c_0\left(1 - \frac{a}{r}\right), \qquad J = 4\pi Dac_0 .
$$

在距离 $r_0 > a$ 处释放的分子最终被捕获的概率为 $a/r_0$。在其余部分为反射的平面上，半径为 $s$ 的完全吸收圆盘接收 $J = 4Dsc_0$。

**证明** 稳态时 $\nabla^2c = 0$；对球对称，$r^{-2}\,\mathrm{d}(r^2\,\mathrm{d}c/\mathrm{d}r)/\mathrm{d}r = 0$，所以 $c = B - A/r$。条件 $c(\infty) = c_0$ 和 $c(a) = 0$ 给出 $B = c_0$ 和 $A = c_0a$。通过表面的向内通量为 $4\pi a^2D\,(\mathrm{d}c/\mathrm{d}r)_{r=a} = 4\pi Dac_0$。捕获概率 $u(r_0)$ 也满足 $\nabla^2u = 0$（行走者被捕获的机会是它走一步之后机会的平均），且 $u(a) = 1$，$u(\infty) = 0$，所以 $u = a/r_0$。圆盘的结果是带电圆盘静电问题的经典解，圆盘的电容为 $8\varepsilon_0s$，而球为 $4\pi\varepsilon_0a$；这里直接引用。$\square$

通量正比于半径，而不是表面积：大一倍的球只捕获多一倍的分子，因为它附近的浓度梯度更平缓。并且在吸收体附近释放的分子很可能但并非必然被捕获；在三维中，随机行走者以概率 $1 - a/r_0$ 逃到无穷远，而在一维和二维中它总会返回。对细胞需要多少受体斑块才能几乎像完全吸收的表面一样有效地捕获分子（$N \approx \pi a/s$ 个斑块就足以得到最大通量的一半）以及细胞测量浓度的精度的分析，见 [7.6.35](/7.6.35)。

**例 5.2.1（细胞可以有多大？）** 以每单位体积速率 $q$ 消耗氧的球形细胞需要 $\frac43\pi R^3q \le 4\pi DRc_0$，所以如果氧只靠扩散到达，它的半径不能超过 $R_{\max} = \sqrt{3Dc_0/q}$。有氧生长的 *E. coli* 每克干质量每小时摄取约 $15\,\mathrm{mmol}$ 的 $\ce{O2}$；$1\,\mu\mathrm{m^3}$ 中有 $0.3\,\mathrm{pg}$ 的干质量，这是 $q \approx 1\,\mathrm{mM\,s^{-1}}$（每个细胞每秒约 $7\times10^{5}$ 个分子）。取 $D = 2\times10^{-9}\,\mathrm{m^2\,s^{-1}}$ 和空气饱和的水（$c_0 = 0.25\,\mathrm{mM}$），$R_{\max} = \sqrt{3 \times 2\times10^{-9} \times 0.25/1}\,\mathrm{m} \approx 40\,\mu\mathrm{m}$：细菌远没有到极限，而超过它的巨型硫细菌用液泡充满其大部分体积。呼吸的组织消耗较少，脑约 $0.03\,\mathrm{mM\,s^{-1}}$，但由溶解氧只有约 $0.13\,\mathrm{mM}$ 的血液供应；此时 $R_{\max} \approx 150\,\mu\mathrm{m}$，这就是为什么代谢活跃组织中没有细胞离毛细血管超过约 $100\,\mu\mathrm{m}$（Krogh 的分析，1919）。

同样的公式给出双分子反应可能的最快速率。如果半径为 $a_{\mathrm{A}}$、$a_{\mathrm{B}}$ 的分子 A 和 B 一接触就反应，则在 A 的参考系中，B 分子以相对扩散系数 $D_{\mathrm{A}} + D_{\mathrm{B}}$ 扩散到半径为 $a_{\mathrm{A}} + a_{\mathrm{B}}$ 的球，速率常数为 $k = 4\pi(D_{\mathrm{A}} + D_{\mathrm{B}})(a_{\mathrm{A}} + a_{\mathrm{B}})N_{\mathrm{A}}$。用 5.3 的 Stokes–Einstein 关系并取 $a_{\mathrm{A}} = a_{\mathrm{B}}$，它变成 $8RT/3\eta \approx 7\times10^{9}\,\mathrm{M^{-1}\,s^{-1}}$（$25\,{}^\circ\mathrm{C}$ 的水中），与大小无关，这就是**扩散控制反应**的极限（[6.3.17](/6.3.17)）。蛋白质的结合更慢，$10^5$–$10^7\,\mathrm{M^{-1}\,s^{-1}}$，因为每个表面只有一小片是有反应性的，分子还必须转到对齐的取向；静电导向可以使速率高于不带电的估计（[7.6.17](/7.6.17)）。

![扩散捕获。A：半径为 a 的完全吸收球周围的稳态浓度 c(r)/c0 = 1 − a/r（过球心的截面，等值线为 0.25、0.5 和 0.75）；耗竭区延伸几个半径，进入球的通量 J = 4πDac0 随半径而不是面积增长。B：在距离 r0 处释放的分子在游荡到 R = 50a 之外之前被捕获的概率：球面行走（walk-on-spheres）Monte Carlo 模拟（点，每个距离 4000 个分子；每一步跳到不接触任何边界的最大球面上的随机点，这精确地对 Brown 路径采样）与精确结果 (1/r0 − 1/R)/(1/a − 1/R) 及其极限 a/r0 的比较。C：只靠扩散供氧的球形细胞的最大半径 R_max = √(3Dc0/q) 随体积消耗率 q 的变化，D = 2000 µm² s⁻¹，c0 = 0.25 mM（空气饱和的水）或 0.13 mM（动脉血浆）；有氧细菌（约 1 mM s⁻¹）远低于极限，脑组织（约 0.03 mM s⁻¹）在约 150 µm 处达到它](./plots/capture.py)

### 5.2.4. 追逐还是等待：Péclet 数

细菌应当游动去收集食物，还是坐着等扩散把食物带来？游过距离 $L$ 需要 $L/v$；食物扩散同样的距离需要 $L^2/D$。两者之比是一个无量纲数，比较由运动或流动的输运与由扩散的输运。

**定义 5.2.1（Péclet 数）** 对长度 $L$ 上由速度为 $v$ 的流动或运动以及系数为 $D$ 的扩散进行的输运，**Péclet 数**为 $\mathrm{Pe} = vL/D$。$\mathrm{Pe} \gg 1$ 时对流占主导，$\mathrm{Pe} \ll 1$ 时扩散占主导。

**例 5.2.2** 对以 $30\,\mu\mathrm{m\,s^{-1}}$ 游过 $D = 10^3\,\mu\mathrm{m^2\,s^{-1}}$ 的小养分溶液的 *E. coli*，在 $L = D/v \approx 30\,\mu\mathrm{m}$，即十五个体长处，$\mathrm{Pe} = 1$。在细胞的尺度 $L = 1\,\mu\mathrm{m}$ 上，$\mathrm{Pe} = 0.03$：游动既不搅动细胞周围的流体，也不明显增加到其表面的养分通量，因为扩散补充耗竭区比细胞离开它更快（Purcell，1977）。细菌游动不是为了增加局部通量，而是为了找到浓度更高的区域，这需要穿过比 $30\,\mu\mathrm{m}$ 大得多的距离。这一论证背后的流体力学是 [7.6.22](/7.6.22) 的主题。

## 5.3. 力场中的扩散

### 5.3.1. 漂移、Smoluchowski 方程与 Einstein 关系

作用在粘性介质中粒子上的力 $F$，在速度弛豫之后产生稳定的漂移速度 $F/\gamma$，其中 $\gamma$ 是摩擦系数（对半径为 $a$ 的球，为 Stokes 值 $\gamma = 6\pi\eta a$）。于是群体除了扩散通量之外还带有漂移通量 $cF/\gamma$。

**公式 5.3.1（Smoluchowski 方程）** 对扩散系数为 $D$、摩擦系数为 $\gamma$、处于势 $U(x)$ 中的粒子，$F = -\mathrm{d}U/\mathrm{d}x$，

$$
\frac{\partial c}{\partial t} = -\frac{\partial J}{\partial x}, \qquad J = -D\frac{\partial c}{\partial x} + \frac{F}{\gamma}c = -D\,\mathrm{e}^{-U/k_{\mathrm{B}}T}\frac{\partial}{\partial x}\left(\mathrm{e}^{U/k_{\mathrm{B}}T}c\right),
$$

其中最后一个形式用了下面的 Einstein 关系；它用 $\nabla$ 推广到三维，也适用于单个粒子的概率密度。

**定理 5.3.1（Einstein 关系）** 若势中扩散的粒子在平衡时达到 Boltzmann 分布，则

$$
D\gamma = k_{\mathrm{B}}T.
$$

**证明** 平衡时通量处处为零，所以 $D\,\mathrm{d}c/\mathrm{d}x = cF/\gamma$。Boltzmann 分布 $c \propto \mathrm{e}^{-U/k_{\mathrm{B}}T}$ 有 $\mathrm{d}c/\mathrm{d}x = cF/k_{\mathrm{B}}T$。两者对每个势都一致，只有当 $D = k_{\mathrm{B}}T/\gamma$。$\square$

这就是 [6.3.21](/6.3.21) 的 **Einstein–Smoluchowski 关系**，在那里由**沉降平衡**得到。它说明，粒子的随机运动与它对力的响应不是独立的性质：两者都来自同样的分子碰撞，知道其一就给出另一个（5.4）。用 Stokes 摩擦，它成为 **Stokes–Einstein 方程**（[6.3.17](/6.3.17)）

$$
D = \frac{k_{\mathrm{B}}T}{6\pi\eta a}, \tag{5.3}
$$

对 $25\,{}^\circ\mathrm{C}$ 水中与 GFP 半径相同的球，它给出 $D = 4.11\times10^{-21}/(6\pi \times 0.89\times10^{-3} \times 2.4\times10^{-9})\,\mathrm{m^2\,s^{-1}} = 1.0\times10^{2}\,\mu\mathrm{m^2\,s^{-1}}$，接近测得的 $87\,\mu\mathrm{m^2\,s^{-1}}$。由于球状蛋白质的体积正比于其质量，$D \propto M^{-1/3}$：重十倍的蛋白质只慢约两倍。细胞质中较慢的扩散（5.1.3 的表）反映的是拥挤和结合，而不是水的黏度更高（[7.6.23](/7.6.23)），非球形分子的摩擦系数是流体力学方法的基础（[7.6.8](/7.6.8)）。

**例 5.3.1（Nernst 电势）** 对电荷为 $ze$、处于电势 $\varphi$ 的离子，$U = ze\varphi$，对只通透该离子的膜，零通量条件给出 $c_{\mathrm{in}}/c_{\mathrm{out}} = \mathrm{e}^{-ze(\varphi_{\mathrm{in}} - \varphi_{\mathrm{out}})/k_{\mathrm{B}}T}$，即 **Nernst 方程**（[6.3.13](/6.3.13)）

$$
\varphi_{\mathrm{in}} - \varphi_{\mathrm{out}} = \frac{k_{\mathrm{B}}T}{ze}\ln\frac{c_{\mathrm{out}}}{c_{\mathrm{in}}}.
$$

一价离子的十倍浓度比对应 $37\,{}^\circ\mathrm{C}$ 时的 $26.7\,\mathrm{mV} \times \ln 10 = 61\,\mathrm{mV}$（$25\,{}^\circ\mathrm{C}$ 时 $59\,\mathrm{mV}$）。对在神经元外浓度约高十倍的 $\ce{Na+}$，平衡电势约为 $+61\,\mathrm{mV}$（内正）。带电场力的 Smoluchowski 方程是 **Nernst–Planck 方程**，由它导出多种可透离子的 **Goldman–Hodgkin–Katz 方程**，见 [7.6.30](/7.6.30)。

### 5.3.2. 转动扩散

分子也会翻滚。它的取向，一个单位矢量 $\boldsymbol{u}$，在单位球面上作随机行走，取向的记忆指数衰减。

**定义 5.3.1（转动扩散）** **转动扩散**是分子被热碰撞随机地重新取向，由转动扩散系数 $D_{\mathrm{r}}$（单位 $\mathrm{rad^2\,s^{-1}}$，通常写成 $\mathrm{s^{-1}}$）描述，使绕任何轴的小转角方差为 $2D_{\mathrm{r}}t$，且 $D_{\mathrm{r}} = k_{\mathrm{B}}T/\gamma_{\mathrm{r}}$，其中 $\gamma_{\mathrm{r}}$ 是转动摩擦系数。

**公式 5.3.2（球的转动扩散）** 对半径为 $a$ 的球，$\gamma_{\mathrm{r}} = 8\pi\eta a^3$，$D_{\mathrm{r}} = k_{\mathrm{B}}T/8\pi\eta a^3$。取向相关函数为

$$
\langle\boldsymbol{u}(t)\cdot\boldsymbol{u}(0)\rangle = \mathrm{e}^{-2D_{\mathrm{r}}t}, \qquad \langle P_2(\boldsymbol{u}(t)\cdot\boldsymbol{u}(0))\rangle = \mathrm{e}^{-6D_{\mathrm{r}}t},
$$

其中 $P_2(x) = (3x^2 - 1)/2$，由荧光各向异性和 NMR 弛豫测得的转动相关时间为 $\tau_{\mathrm{rot}} = 1/6D_{\mathrm{r}} = \eta V/k_{\mathrm{B}}T$，$V = \frac43\pi a^3$。

两个相关函数衰减不同，因为它们是取向的第一和第二球谐函数，分别以速率 $l(l + 1)D_{\mathrm{r}}$（$l = 1$ 和 $2$）弛豫。转动与平动扩散对大小的依赖不同：平动按 $1/a$，转动按 $1/a^3$。半径 $2.5\,\mathrm{nm}$ 的蛋白质在 $25\,{}^\circ\mathrm{C}$ 水中有 $\tau_{\mathrm{rot}} = 0.89\times10^{-3} \times 6.5\times10^{-26}/4.11\times10^{-21}\,\mathrm{s} = 14\,\mathrm{ns}$，它的取向在几十纳秒内被随机化，这决定了荧光各向异性的时间窗口（[7.6.11](/7.6.11)）和 NMR 的线宽（[7.6.13](/7.6.13)）。对例 5.1.1 的细菌（$a \approx 1\,\mu\mathrm{m}$），$1/D_{\mathrm{r}} = 8\pi\eta a^3/k_{\mathrm{B}}T \approx 5\,\mathrm{s}$：仅靠 Brown 转动就会在几秒内使它的方向随机化，所以比这长得多的奔跑是无用的，无论怎么做，细菌都不能保持直线航向超过约十秒（Berg 与 Purcell，1977）。

必须以特定取向相遇的分子，因需要转到对齐而变慢：对 5.2.3 的扩散限制结合，反应的斑块必须找到彼此，速率常数下降到表面中有反应性部分的比例，同一次相遇中的重复碰撞对此有部分补偿。

## 5.4. Langevin 方程

### 5.4.1. 摩擦与噪声

扩散方程描述概率；单个粒子的运动由 Newton 方程描述，溶剂的力分成系统的部分与随机的部分。

**定义 5.4.1（Langevin 方程）** 质量为 $m$ 的粒子在一维中的 **Langevin 方程**为

$$
m\frac{\mathrm{d}v}{\mathrm{d}t} = -\gamma v + F(x) + \xi(t), \qquad \langle\xi(t)\rangle = 0, \quad \langle\xi(t)\xi(t')\rangle = \Gamma\,\delta(t - t'),
$$

其中 $-\gamma v$ 是溶剂的摩擦，$F(x)$ 是外力，随机力 $\xi(t)$ 是**白噪声**：不同时刻的值不相关、因而功率谱平坦的平稳 Gauss 过程。

摩擦和噪声都是对同样的分子碰撞的平均，它们的强度不可能独立。能量均分确定了这一关系。

**定理 5.4.1（Langevin 方程的涨落–耗散关系）** 对由定义 5.4.1 描述的自由粒子（$F = 0$），要在温度 $T$ 达到热平衡，噪声强度必须为

$$
\Gamma = 2\gamma k_{\mathrm{B}}T .
$$

平衡时速度自相关函数为 $\langle v(t)v(0)\rangle = (k_{\mathrm{B}}T/m)\,\mathrm{e}^{-\gamma\lvert t\rvert/m}$，均方位移为

$$
\langle[x(t) - x(0)]^2\rangle = 2Dt - 2D\frac{m}{\gamma}\left(1 - \mathrm{e}^{-\gamma t/m}\right), \qquad D = \int_0^\infty\langle v(t)v(0)\rangle\,\mathrm{d}t = \frac{k_{\mathrm{B}}T}{\gamma},
$$

对 $t \ll m/\gamma$ 是弹道的，$\langle x^2\rangle \approx (k_{\mathrm{B}}T/m)t^2$，对 $t \gg m/\gamma$ 是扩散的。

**证明** 线性方程的解为 $v(t) = v(0)\mathrm{e}^{-\gamma t/m} + \frac1m\int_0^t\mathrm{e}^{-\gamma(t - s)/m}\xi(s)\,\mathrm{d}s$。用噪声的相关，

$$
\langle v(t)^2\rangle = \langle v(0)^2\rangle\mathrm{e}^{-2\gamma t/m} + \frac{\Gamma}{m^2}\int_0^t\mathrm{e}^{-2\gamma(t - s)/m}\,\mathrm{d}s \to \frac{\Gamma}{2m\gamma} \quad (t \to \infty).
$$

能量均分要求 $\frac12m\langle v^2\rangle = \frac12k_{\mathrm{B}}T$，所以 $\Gamma = 2\gamma k_{\mathrm{B}}T$。把从 $v(0)$ 出发的解乘以 $v(0)$ 并平均（时间 $0$ 之后的噪声与 $v(0)$ 独立），得到指数的相关函数。最后 $x(t) - x(0) = \int_0^tv(s)\,\mathrm{d}s$，所以 $\langle[x(t) - x(0)]^2\rangle = \int_0^t\int_0^t\langle v(s)v(s')\rangle\,\mathrm{d}s\,\mathrm{d}s' = 2\int_0^t(t - u)\langle v(u)v(0)\rangle\,\mathrm{d}u$，求值即得所述的表达式；其长时间斜率 $2\int_0^\infty\langle v(u)v(0)\rangle\,\mathrm{d}u$ 为 $2k_{\mathrm{B}}T/\gamma$。$\square$

该定理第二次导出 Einstein 关系，这次是从单个粒子的动力学而不是群体的平衡，而公式 $D = \int_0^\infty\langle v(t)v(0)\rangle\,\mathrm{d}t$（Green–Kubo 关系）对任何平衡动力学都成立，而不仅仅是对 Langevin 模型。速度被记住的时间 $m/\gamma$ 在水中非常短：对 $50\,\mathrm{kDa}$ 的蛋白质（$m = 8.3\times10^{-23}\,\mathrm{kg}$，$\gamma = 6\pi\eta a = 4\times10^{-11}\,\mathrm{kg\,s^{-1}}$）是 $2\,\mathrm{ps}$，对直径 $1\,\mu\mathrm{m}$ 的小球约 $70\,\mathrm{ns}$。停止马达的游动细菌滑行不到一微秒，距离不到零点一纳米。在所有生物学时间尺度上惯性都无关紧要，Langevin 方程以其过阻尼形式使用，$\gamma\,\mathrm{d}x/\mathrm{d}t = F(x) + \xi(t)$。

噪声与摩擦之间的关系是一个一般原理的特例。

**定义 5.4.2（涨落–耗散定理）** **涨落–耗散定理**指出，对处于热平衡的系统，变量 $x$ 对与它共轭的弱力 $f$ 的线性响应，由 $x$ 的自发平衡涨落决定：在经典系统中，涨落的功率谱 $S_x(\omega) = \int_{-\infty}^{\infty}\langle x(t)x(0)\rangle\mathrm{e}^{\mathrm{i}\omega t}\,\mathrm{d}t$ 与响应函数 $\chi(\omega) = \hat x(\omega)/\hat f(\omega)$ 满足

$$
S_x(\omega) = \frac{2k_{\mathrm{B}}T}{\omega}\operatorname{Im}\chi(\omega).
$$

该定理是被动微流变学的基础：观察小球在材料中的涨落，就能得到材料的黏弹响应而无需推它。违反它的系统不处于平衡。在活细胞中，小球和囊泡在低频的涨落远大于测得的力学响应所预言的，因为马达搅动细胞质；比较主动与被动测量可以定量这些主动力（[7.6.23](/7.6.23)）。细胞为了功能也需要打破响应与涨落之间的平衡联系：应当响应强烈而涨落很小的传感器或马达，必须被驱动到远离平衡（[7.6.38](/7.6.38)）。

### 5.4.2. 谐振阱中的粒子

带线性恢复力的过阻尼 Langevin 方程，是从**光镊**到涨落的膜等每一种被束缚粒子的测量的原型。

**定义 5.4.3（Ornstein–Uhlenbeck 过程）** **Ornstein–Uhlenbeck 过程**是 $\gamma\,\mathrm{d}x/\mathrm{d}t = -\kappa x + \xi(t)$ 的解，其中白噪声强度为 $2\gamma k_{\mathrm{B}}T$：被刚度为 $\kappa$ 的弹簧束缚在原点的扩散粒子，**弛豫时间**为 $\tau = \gamma/\kappa$。

**公式 5.4.1（被束缚的 Brown 粒子）** 对 Ornstein–Uhlenbeck 过程，从 $x(0) = 0$ 出发的粒子有 $\langle x(t)^2\rangle = (k_{\mathrm{B}}T/\kappa)(1 - \mathrm{e}^{-2t/\tau})$。平衡时，

$$
\langle x(t)x(0)\rangle = \frac{k_{\mathrm{B}}T}{\kappa}\mathrm{e}^{-\lvert t\rvert/\tau}, \qquad
\langle[x(t) - x(0)]^2\rangle = \frac{2k_{\mathrm{B}}T}{\kappa}\left(1 - \mathrm{e}^{-t/\tau}\right), \qquad
S_x(\omega) = \frac{2\gamma k_{\mathrm{B}}T}{\kappa^2 + \gamma^2\omega^2}.
$$

在短时间（$t \ll \tau$），粒子自由扩散，$\langle[x(t) - x(0)]^2\rangle \approx 2(k_{\mathrm{B}}T/\gamma)t$；在长时间，其偏移饱和在能量均分的值 $\langle x^2\rangle = k_{\mathrm{B}}T/\kappa$。功率谱是转折频率为 $f_{\mathrm{c}} = \kappa/2\pi\gamma$ 的 Lorentz 型；用 $\chi(\omega) = 1/(\kappa - \mathrm{i}\omega\gamma)$，它精确地满足定义 5.4.2，只需计算 $\operatorname{Im}\chi$ 即可验证。

**例 5.4.1（标定光阱）** 半径 $0.5\,\mu\mathrm{m}$ 的小球在水中（$\gamma = 6\pi\eta a = 8.4\times10^{-9}\,\mathrm{N\,s\,m^{-1}}$）被刚度 $\kappa = 0.05\,\mathrm{pN\,nm^{-1}}$ 的阱束缚，涨落的标准差为 $\sqrt{k_{\mathrm{B}}T/\kappa} = \sqrt{4.1/0.05}\,\mathrm{nm} = 9\,\mathrm{nm}$，弛豫时间为 $\tau = \gamma/\kappa = 0.17\,\mathrm{ms}$，转折频率为 $0.95\,\mathrm{kHz}$。方差（能量均分）或功率谱的转折频率都给出 $\kappa$；两者一致则检验了标定（[7.6.17](/7.6.17)）。要分辨驱动蛋白的 $8\,\mathrm{nm}$ 步长（[7.3.14](/7.3.14)），必须用硬的阱或对长于 $\tau$ 的时间作平均来减小小球的热运动。

![Langevin 动力学（A 和 B 为过阻尼，单位取 γ = kBT = 1）。A：自由粒子与刚度 κ = 1 的谐振阱中粒子的轨迹（弛豫时间 τ = γ/κ = 1；阴影带为 ±√(kBT/κ)）。B：从 x(0) = 0 出发的均方位移，对 1000 个粒子平均（点），与自由粒子的 2Dt 和阱中的 (kBT/κ)(1 − e^−2t/τ) 比较：两者一开始都是扩散的，但被束缚的粒子饱和在能量均分的值 kBT/κ。C：有惯性时，从静止出发的粒子从噪声获得动能；只有当噪声强度为 2γkBT（定理 5.4.1）时，平均动能才稳定在 kBT/2；强度为其一半或两倍时，粒子的“温度”是错的（模拟，实线；理论，虚线）](./plots/langevin.py)

## 5.5. 主方程与 Fokker–Planck 方程

### 5.5.1. 主方程

对具有离散状态的随机系统，如在格点之间跳跃的粒子、在构象之间切换的通道、沿纤维步进的马达或产生分子的基因，概率描述就是主方程。

**定义 5.5.1（主方程）** 对具有离散状态 $i$、从状态 $j$ 到 $i$ 的跃迁速率为 $w_{ij}$ 的系统，概率 $p_i(t)$ 的**主方程**为

$$
\frac{\mathrm{d}p_i}{\mathrm{d}t} = \sum_{j \ne i}\left(w_{ij}p_j - w_{ji}p_i\right),
$$

即每个状态的概率流入与流出的平衡。

主方程描述连续时间的 **Markov 链**（[3.5.9](/3.5.9)）：未来只依赖于现在的状态。它的定态解对每个 $i$ 满足 $\sum_j(w_{ij}p_j - w_{ji}p_i) = 0$；在热平衡中每一项分别为零，$w_{ij}p_j^{\mathrm{eq}} = w_{ji}p_i^{\mathrm{eq}}$，这就是**细致平衡**，并要求 $w_{ij}/w_{ji} = \mathrm{e}^{-(G_i - G_j)/k_{\mathrm{B}}T}$（[7.6.4](/7.6.4) 的式 (4.2)）。有绕循环的非零净流的定态是**非平衡稳态**，是马达和一切由 ATP 驱动的过程的状态（[7.6.38](/7.6.38)）。[7.6.4](/7.6.4) 的两态通道是最小的例子；分子数的**化学主方程**在 [7.6.32](/7.6.32) 中发展。

### 5.5.2. 由跳跃到漂移与扩散

在间距为 $a$ 的一维格点上，以速率 $k_+$ 向右跳、速率 $k_-$ 向左跳的粒子满足

$$
\frac{\partial p(x, t)}{\partial t} = k_+p(x - a, t) + k_-p(x + a, t) - (k_+ + k_-)p(x, t).
$$

把 $p(x \pm a, t)$ 展开到 $a$ 的二阶，

$$
\frac{\partial p}{\partial t} = -v\frac{\partial p}{\partial x} + D\frac{\partial^2p}{\partial x^2}, \qquad v = a(k_+ - k_-), \quad D = \frac{a^2(k_+ + k_-)}{2},
$$

这是漂移–扩散方程，其系数是单位时间位移的均值和方差的一半。有偏的跳跃者同时漂移和扩展；比值 $2D/(va) = (k_+ + k_-)/(k_+ - k_-)$（**随机性参数**）度量它离确定性步进有多远，用来数马达循环中隐藏的步骤（[7.6.27](/7.6.27)）。这类方程的一般形式如下。

**定义 5.5.2（Fokker–Planck 方程）** 连续 Markov 过程的概率密度 $p(x, t)$ 的 **Fokker–Planck 方程**为

$$
\frac{\partial p}{\partial t} = -\frac{\partial}{\partial x}\left[A(x)p\right] + \frac12\frac{\partial^2}{\partial x^2}\left[B(x)p\right],
$$

其中漂移系数 $A(x) = \lim_{\Delta t \to 0}\langle\Delta x\rangle/\Delta t$，扩散系数 $B(x) = \lim_{\Delta t \to 0}\langle(\Delta x)^2\rangle/\Delta t$，是从 $x$ 出发在短时间内位移的前两个矩。

取 $A = F/\gamma$ 和常数 $B = 2D$，它就是 Smoluchowski 方程（公式 5.3.1）。当 $B$ 依赖于 $x$ 时，它位于二阶导数之内；有时写成 $\partial_x[\frac12B\,\partial_xp]$，则会增加一个虚假的漂移 $-\frac12B'(x)$，除非对噪声重新解释。对 Ornstein–Uhlenbeck 过程，$A = -\kappa x/\gamma$，$B = 2D$，定态解是 Gauss 分布 $p \propto \mathrm{e}^{-\kappa x^2/2k_{\mathrm{B}}T}$，即弹簧的 Boltzmann 分布。均值满足 $\mathrm{d}\langle x\rangle/\mathrm{d}t = \langle A(x)\rangle$，仅当漂移是线性时才等于 $A(\langle x\rangle)$。同一个方程，以漂移 $\nabla\ln p$ 在时间上倒着运行，就是机器学习中生成式扩散模型的原理（[4.7](/4.7)），它们学习反转把数据变成噪声的过程。

## 5.6. 首达与越垒

### 5.6.1. 平均首达时间

许多生物学问题问的不是粒子在哪里，而是它什么时候第一次到达某处：转录因子什么时候到达它的位点，蛋白质什么时候越过折叠能垒，马达什么时候完成一步。

**定义 5.6.1（首达时间）** 从 $x_0$ 出发的随机过程到目标集的**首达时间**，是过程第一次进入目标的随机时间。

**定理 5.6.1（一维平均首达时间）** 对扩散系数为 $D$、处于势 $U(x)$ 中的过阻尼运动，从位于 $x_{\mathrm{r}}$ 处的反射边界与 $x_{\mathrm{a}} > x_0$ 处的吸收边界之间的 $x_0$ 出发，到达 $x_{\mathrm{a}}$ 的平均首达时间为

$$
T(x_0) = \frac{1}{D}\int_{x_0}^{x_{\mathrm{a}}}\mathrm{d}y\,\mathrm{e}^{U(y)/k_{\mathrm{B}}T}\int_{x_{\mathrm{r}}}^{y}\mathrm{d}z\,\mathrm{e}^{-U(z)/k_{\mathrm{B}}T}.
$$

**证明** 对第一个短区间 $\Delta t$ 取条件：$T(x) = \Delta t + \langle T(x + \Delta x)\rangle$，其中 $\langle\Delta x\rangle = (F/\gamma)\Delta t$，$\langle\Delta x^2\rangle = 2D\Delta t$。展开到 $\Delta t$ 的一阶得到后向方程 $DT'' + (F/\gamma)T' = -1$，边界条件为 $T(x_{\mathrm{a}}) = 0$ 和 $T'(x_{\mathrm{r}}) = 0$。取 $F = -U'$ 和 $D\gamma = k_{\mathrm{B}}T$，左边为 $D\,\mathrm{e}^{\beta U}(\mathrm{e}^{-\beta U}T')'$，所以 $\mathrm{e}^{-\beta U(x)}T'(x) = -\frac1D\int_{x_{\mathrm{r}}}^{x}\mathrm{e}^{-\beta U(z)}\,\mathrm{d}z$；再从 $x_0$ 到 $x_{\mathrm{a}}$ 积分一次即得公式。$\square$

对从 $0$ 处的反射壁到 $L$ 处吸收体的自由扩散，$T(0) = L^2/2D$，即式 (5.1) 的一维版本；从半径为 $R$ 的球心出发的粒子，经平均时间 $R^2/6D$ 到达其表面。有指向目标的恒力时，一旦 Péclet 数 $vL/D$ 超过一，时间降向 $L/v$；有背离目标的力时，它随势差指数增长，这就是下一个结果的内容。

### 5.6.2. Kramers 速率

必须改变构象的分子，如蛋白质的解折叠、通道的开放或配体离开其口袋，位于自由能阱中，必须靠热涨落带过能垒。Kramers（1940）计算了在势中扩散的粒子的速率。

**定理 5.6.2（Kramers 速率）** 对势中的过阻尼扩散，势有极小点 $a$、垒顶 $b$，垒高 $\Delta U = U(b) - U(a) \gg k_{\mathrm{B}}T$，则逃离势阱的速率为

$$
k = \frac{\sqrt{U''(a)\,\lvert U''(b)\rvert}}{2\pi\gamma}\,\mathrm{e}^{-\Delta U/k_{\mathrm{B}}T}.
$$

**证明** 在定理 5.6.1 中取能垒之外的吸收点和 $x_0 = a$。对高的能垒，外层因子 $\mathrm{e}^{\beta U(y)}$ 在垒顶 $b$ 处有尖锐的峰，此处内层积分已达到它的全部值，即 $\mathrm{e}^{-\beta U}$ 在阱上的积分，它在 $a$ 处有尖锐的峰。把每个指数用其二次展开近似（Laplace 方法），

$$
\int_{\mathrm{well}}\mathrm{e}^{-\beta U(z)}\,\mathrm{d}z \approx \mathrm{e}^{-\beta U(a)}\sqrt{\frac{2\pi k_{\mathrm{B}}T}{U''(a)}}, \qquad
\int_{\mathrm{barrier}}\mathrm{e}^{\beta U(y)}\,\mathrm{d}y \approx \mathrm{e}^{\beta U(b)}\sqrt{\frac{2\pi k_{\mathrm{B}}T}{\lvert U''(b)\rvert}}.
$$

于是 $T \approx (2\pi k_{\mathrm{B}}T/D)\,\mathrm{e}^{\beta\Delta U}/\sqrt{U''(a)\lvert U''(b)\rvert}$，$k = 1/T$ 并用 $D = k_{\mathrm{B}}T/\gamma$ 即得结果。$\square$

速率与能垒呈指数关系，如 **Arrhenius 方程**（[6.3.17](/6.3.17)），而能垒就是活化自由能。Kramers 增加的是前因子：在过阻尼区，它是曲率除以摩擦，而不是**过渡态理论**（[6.3.16](/6.3.16)）的普适频率 $k_{\mathrm{B}}T/h = 6.2\times10^{12}\,\mathrm{s^{-1}}$，后者假定每一次越过垒顶都是最终的。在黏性介质中，系统在作出最终选择之前多次反复越过能垒，速率更小，并与摩擦成反比。蛋白质折叠和大构象变化的速率在加入黏滞剂时确实大致与溶剂黏度成反比地下降，其前因子估计为 $10^6$–$10^8\,\mathrm{s^{-1}}$，这就是为什么即使最快的蛋白质折叠也要微秒（[7.6.16](/7.6.16)）。Eyring 前因子适用于小分子的键重排，而不适用于水中大分子的运动。

**例 5.6.1** 垒高 $10\,k_{\mathrm{B}}T$、Kramers 前因子为 $10^7\,\mathrm{s^{-1}}$ 的构象转变以 $10^7\mathrm{e}^{-10} = 450\,\mathrm{s^{-1}}$ 发生，停留时间约 $2\,\mathrm{ms}$，在通道门控的范围内（[7.6.4](/7.6.4)）。用过渡态的前因子，同样的能垒会给出 $3\times10^{8}\,\mathrm{s^{-1}}$。能垒每多 $k_{\mathrm{B}}T$，转变慢 $2.7$ 倍，每 $2.3\,k_{\mathrm{B}}T$ 慢十倍；黏度加倍使速率减半而不改变平衡。

同样的图像推广到多个坐标：蛋白质的构象动力学是其构型空间中自由能景观上的扩散，势阱是状态，鞍点是过渡态，折叠是漏斗形景观的特例（[7.6.16](/7.6.16)）。使景观倾斜的力或膜电位降低一个能垒而升高另一个，这就是通道的速率如何依赖电压、键的寿命如何依赖力（**Bell 模型**，[7.6.17](/7.6.17)）；正向与逆向速率之比仍由末态的自由能差决定，如细致平衡所要求的。

![双阱 U(x) = ΔU(x² − 1)² 中的越垒（过阻尼 Langevin 动力学，γ = kBT = 1）。A：ΔU = 4 kBT 的势，极小点 a 在 x = ±1（曲率 U'' = 8ΔU），垒顶 b 在 x = 0（U'' = −4ΔU）。B：ΔU = 4 kBT 的一条轨迹：在每个阱中长时间停留，被只占一小部分时间的跳跃隔开，这种行为证明两态描述是合理的。C：逃逸速率，即从 x = −1 到 x = +1 的平均首达时间之倒数，每个垒高模拟 400 个粒子（点），来自定理 5.6.1 的精确首达积分（线）和 Kramers 公式（虚线）；速率随能垒指数下降，一旦能垒超过几个 kBT，Kramers 近似就变得准确](./plots/kramers.py)

## 小结

| 主题 | 主要结果 |
|---|---|
| 随机行走（定义 5.1.1、定理 5.1.1） | $\langle r^2\rangle = Na^2 = 2dDt$，$D = a^2/2d\tau$；由中心极限定理得 Gauss 分布 |
| 扩散系数（定义 5.1.2、公式 5.1.1、例 5.1.1） | $D = \lim\langle r^2\rangle/2dt$；持续性使 $D$ 乘以 $(1 + \alpha)/(1 - \alpha)$；游动的 *E. coli* $D \approx 200\,\mu\mathrm{m^2\,s^{-1}}$ |
| 扩散时间（式 (5.1)、5.1.3 的表） | $t \approx L^2/2dD$；GFP 穿过细菌 $0.02\,\mathrm{s}$，穿过 1 m 轴突需几个世纪；超过 $L^* = 6D/v$ 马达占优 |
| 扩散方程（式 (5.2)、公式 5.2.1） | 守恒 + Fick 定律，$\partial_tc = D\nabla^2c$；点源 $N(4\pi Dt)^{-d/2}\mathrm{e}^{-r^2/4Dt}$ |
| FRAP（公式 5.2.2） | 余弦级数；平台 $1 - a/L$；时间按 $1/D$ 标度；最慢模式 $L^2/\pi^2D$ 由隔室决定 |
| 捕获（公式 5.2.3、例 5.2.1） | $c = c_0(1 - a/r)$，$J = 4\pi Dac_0$（圆盘 $4Dsc_0$）；捕获概率 $a/r_0$；$R_{\max} = \sqrt{3Dc_0/q}$；$k_{\mathrm{D}} = 8RT/3\eta \approx 7\times10^9\,\mathrm{M^{-1}\,s^{-1}}$ |
| Péclet 数（定义 5.2.1、例 5.2.2） | $\mathrm{Pe} = vL/D$；细菌在约 $30\,\mu\mathrm{m}$ 以下跑不过扩散 |
| 漂移与扩散（公式 5.3.1、定理 5.3.1、式 (5.3)） | $J = -D\partial_xc + cF/\gamma$；$D\gamma = k_{\mathrm{B}}T$；$D = k_{\mathrm{B}}T/6\pi\eta a$；Nernst 在 $37\,{}^\circ\mathrm{C}$ 每十倍 $61\,\mathrm{mV}$ |
| 转动（定义 5.3.1、公式 5.3.2） | $D_{\mathrm{r}} = k_{\mathrm{B}}T/8\pi\eta a^3$；$\tau_{\mathrm{rot}} = 1/6D_{\mathrm{r}} = \eta V/k_{\mathrm{B}}T$，$a = 2.5\,\mathrm{nm}$ 时约 $14\,\mathrm{ns}$ |
| Langevin（定义 5.4.1、定理 5.4.1、定义 5.4.2） | 噪声 $2\gamma k_{\mathrm{B}}T$；$\langle v(t)v(0)\rangle = (k_{\mathrm{B}}T/m)\mathrm{e}^{-\gamma t/m}$；$D = \int\langle vv\rangle\,\mathrm{d}t$；$m/\gamma \sim$ ps–ns；$S_x = (2k_{\mathrm{B}}T/\omega)\operatorname{Im}\chi$ |
| 阱（定义 5.4.3、公式 5.4.1、例 5.4.1） | $\langle x^2\rangle = k_{\mathrm{B}}T/\kappa$，$\tau = \gamma/\kappa$，转折频率 $f_{\mathrm{c}} = \kappa/2\pi\gamma$ 的 Lorentz 型 |
| 主方程与 Fokker–Planck 方程（定义 5.5.1–5.5.2） | 概率平衡；跳跃给出 $v = a(k_+ - k_-)$，$D = a^2(k_+ + k_-)/2$；由前两个矩得漂移 $A$ 与扩散 $B$ |
| 首达与 Kramers（定义 5.6.1、定理 5.6.1–5.6.2、例 5.6.1） | 双重积分的 MFPT；自由：$L^2/2D$；$k = \sqrt{U''_aU''_b}\,\mathrm{e}^{-\Delta U/k_{\mathrm{B}}T}/2\pi\gamma$，$\propto 1/\eta$；蛋白质的前因子 $10^6$–$10^8\,\mathrm{s^{-1}}$ |

## 思考题

1. GFP 在 *E. coli* 中以 $D = 8\,\mu\mathrm{m^2\,s^{-1}}$ 扩散，mRNA–蛋白质颗粒以 $D = 0.03\,\mu\mathrm{m^2\,s^{-1}}$ 扩散。各需多长时间走过细胞 $2\,\mu\mathrm{m}$ 的长度（视为一维扩散）？这一结果对某个 mRNA 所编码的蛋白质相对于基因在何处合成意味着什么？

   **答** $t = L^2/2D$：GFP 为 $4/16 = 0.25\,\mathrm{s}$；mRNA 颗粒为 $4/0.06 \approx 67\,\mathrm{s}$，与细菌 mRNA 的寿命（几分钟）相当。蛋白质在一秒内就散布到整个细胞，但 mRNA 在其生命的大部分时间里留在转录它的地点附近，所以翻译局限在其基因的拟核区域附近；在细菌中，转录与翻译不仅在时间上而且在空间上耦合（[7.2.18](/7.2.18)）。

2. 估算 $100\,\mathrm{kDa}$ 球状蛋白质在 $25\,{}^\circ\mathrm{C}$ 水中的扩散系数和转动相关时间（$\eta = 0.89\,\mathrm{mPa\,s}$，蛋白质密度 $1.35\,\mathrm{g\,cm^{-3}}$）。水合会怎样改变估算？

   **答** 体积 $V = M/\rho N_{\mathrm{A}} = 10^5/(1.35 \times 6.02\times10^{23})\,\mathrm{cm^3} = 1.23\times10^{-19}\,\mathrm{cm^3} = 1.23\times10^{-25}\,\mathrm{m^3}$，半径 $a = (3V/4\pi)^{1/3} = 3.1\,\mathrm{nm}$。$D = k_{\mathrm{B}}T/6\pi\eta a = 4.11\times10^{-21}/(6\pi \times 0.89\times10^{-3} \times 3.1\times10^{-9}) = 7.9\times10^{-11}\,\mathrm{m^2\,s^{-1}} = 79\,\mu\mathrm{m^2\,s^{-1}}$；$\tau_{\mathrm{rot}} = \eta V/k_{\mathrm{B}}T = 0.89\times10^{-3} \times 1.23\times10^{-25}/4.11\times10^{-21} = 27\,\mathrm{ns}$。约 $0.3\,\mathrm{nm}$ 的水合壳层和对球形的偏离使流体力学半径增大 $10$–$20\,\%$，使 $D$ 降低同样的比例，使 $\tau_{\mathrm{rot}}$ 升高 $30$–$70\,\%$（它按 $a^3$ 标度）；这种大小的蛋白质实测值约为 $60\,\mu\mathrm{m^2\,s^{-1}}$ 和 $40\,\mathrm{ns}$（[7.6.8](/7.6.8)）。

3. 在对长度 $2L = 4\,\mu\mathrm{m}$ 的细菌的 FRAP 实验中，中央宽 $2a = 1\,\mu\mathrm{m}$ 的带被漂白。(a) 如果所有分子都可移动，该带恢复到漂白前值的多大比例？(b) 最终趋近平台是时间常数为 $0.1\,\mathrm{s}$ 的指数。$D$ 是多少？(c) 如果平台只有 $0.6$，不动分子的比例是多少？

   **答** (a) $1 - a/L = 1 - 0.5/2 = 0.75$。(b) 最慢的模式以速率 $D\pi^2/L^2$ 衰减，所以 $D = L^2/(\pi^2 \times 0.1\,\mathrm{s}) = 4/(9.87 \times 0.1) = 4.1\,\mu\mathrm{m^2\,s^{-1}}$。(c) 若比例 $f$ 不动，被漂白的不动分子永不恢复，可动分子恢复到其份额的 $(1 - f)(1 - a/L)$；令 $(1 - f) \times 0.75 = 0.6$ 得 $f = 0.2$（忽略不动分子的漂白对可动库造成的微小耗竭）。

4. 半径为 $R$ 的球形细胞以每单位体积速率 $q$ 均匀地消耗氧。(a) 证明如果 $R > R_{\max} = \sqrt{3Dc_0/q}$，表面通量跟不上。(b) 在不受氧限制的细胞内部，浓度也从表面向中心下降；解 $D\nabla^2c = q$，取 $c(R) = c_0$，求 $c(0) > 0$ 的条件。与 (a) 比较。

   **答** (a) 对完美吸收体的扩散供应至多为 $4\pi DRc_0$，需求为 $\frac43\pi R^3q$；供应 $\ge$ 需求给出 $R^2 \le 3Dc_0/q$。(b) 球对称解为 $c(r) = c_0 - q(R^2 - r^2)/6D$，所以 $c(0) = c_0 - qR^2/6D > 0$ 要求 $R < \sqrt{6D_{\mathrm{in}}c_0/q}$，其中 $D_{\mathrm{in}}$ 是内部的扩散系数。两个极限相差 $\sqrt2$ 倍，且代入的扩散系数不同：外部供应和内部分布都限制大小，对同样的 $D$，外部供应更为严格。

5. 用 **Nernst 方程**计算内 $140\,\mathrm{mM}$、外 $5\,\mathrm{mM}$ 的 $\ce{K+}$ 在 $37\,{}^\circ\mathrm{C}$ 的平衡电势，并说明为什么这由 Einstein 关系得出而无需任何关于通道的知识。

   **答** $\varphi_{\mathrm{in}} - \varphi_{\mathrm{out}} = (k_{\mathrm{B}}T/e)\ln(c_{\mathrm{out}}/c_{\mathrm{in}}) = 26.7\,\mathrm{mV} \times \ln(5/140) = 26.7 \times (-3.33) = -89\,\mathrm{mV}$。平衡时，由电场驱动的漂移通量与由浓度梯度驱动的扩散通量相互抵消；它们的比值只通过 Einstein 关系涉及 $D$ 和迁移率 $D/k_{\mathrm{B}}T$，所以通道的通透性（同时乘在两者上）消去了。平衡性质与动力学无关；只有当几种离子携带电流时通透性才要紧（GHK 方程，[7.6.30](/7.6.30)）。

6. 光阱在 $25\,{}^\circ\mathrm{C}$ 下束缚一个小球，其位置的标准差为 $10\,\mathrm{nm}$。(a) 阱的刚度是多少？(b) 对水中半径 $0.5\,\mu\mathrm{m}$ 的小球，功率谱的转折频率是多少？(c) 对 $10\,\mathrm{ms}$ 求平均，小球平均位置的测量精度是多少？

   **答** (a) $\kappa = k_{\mathrm{B}}T/\langle x^2\rangle = 4.11/100 = 0.041\,\mathrm{pN\,nm^{-1}}$。(b) $\gamma = 8.4\times10^{-9}\,\mathrm{N\,s\,m^{-1}} = 8.4\times10^{-6}\,\mathrm{pN\,s\,nm^{-1}}$，$f_{\mathrm{c}} = \kappa/2\pi\gamma = 0.041/(2\pi \times 8.4\times10^{-6}) = 780\,\mathrm{Hz}$，$\tau = 0.2\,\mathrm{ms}$。(c) 相隔超过约 $2\tau$ 的样本近似独立；$10\,\mathrm{ms}$ 含约 $10/(2 \times 0.2) = 25$ 个独立样本，所以标准误差为 $10/\sqrt{25} = 2\,\mathrm{nm}$（精确地说，Ornstein–Uhlenbeck 过程时间平均的方差在 $T_{\mathrm{av}} \gg \tau$ 时为 $2\langle x^2\rangle\tau/T_{\mathrm{av}}$，给出 $10 \times \sqrt{0.4/10} = 2\,\mathrm{nm}$）。

7. 某蛋白质的解折叠是水中速率为 $1\,\mathrm{s^{-1}}$ 的越垒。(a) 加入甘油，使黏度升高到三倍。如果能垒不变，Kramers 理论预言速率是多少？(b) 一个突变使能垒升高 $1.4\,k_{\mathrm{B}}T$。水中新的速率是多少？(c) 为什么解释折叠速率需要黏度和突变两种实验？

   **答** (a) 在过阻尼区 $k \propto 1/\gamma \propto 1/\eta$：$0.33\,\mathrm{s^{-1}}$（实际上甘油也稳定蛋白质，所以必须用在同一溶剂中测得的稳定性来修正能垒）。(b) $\mathrm{e}^{-1.4} = 0.25$，所以 $0.25\,\mathrm{s^{-1}}$。(c) 速率是前因子乘以 Boltzmann 因子。黏度依赖检验动力学是否是扩散的并使人得以得到前因子（以及内摩擦，如果依赖比 $1/\eta$ 弱），而突变改变能垒；φ 值分析利用这一点绘出过渡态的结构（[7.6.16](/7.6.16)）。

8. 由定理 5.6.1 证明，从 $0$ 处的反射壁到 $L$ 处的吸收体的自由扩散，平均时间为 $L^2/2D$。然后加上指向吸收体的恒力 $F$，证明当 $\mathrm{Pe} = vL/D \gg 1$ 时平均时间趋于 $L/v$，$v = F/\gamma$。

   **答** 取 $U = 0$，$T(0) = \frac1D\int_0^L\mathrm{d}y\int_0^y\mathrm{d}z = L^2/2D$。取 $U = -Fx$，$\beta U = -vx/D$，$T(0) = \frac1D\int_0^L\mathrm{e}^{-vy/D}\frac{D}{v}(\mathrm{e}^{vy/D} - 1)\,\mathrm{d}y = \frac{L}{v} - \frac{D}{v^2}(1 - \mathrm{e}^{-vL/D})$。对 $\mathrm{Pe} \gg 1$，第二项为 $L/v \cdot (1/\mathrm{Pe})$，可以忽略，所以 $T \to L/v$；对 $\mathrm{Pe} \ll 1$，把指数展开到二阶就回到 $L^2/2D$。

9. （概念）解释为什么在吸收球旁释放的三维随机行走者可能永不返回，而在一维中总会返回。这对从细胞表面受体上解离的配体意味着什么？

   **答** 捕获概率 $u$ 是在吸收体上等于 $1$ 的调和函数。在三维中 $u = a/r_0$ 在无穷远衰减为零，所以逃逸概率 $1 - a/r_0$ 是有限的；在一维中调和函数是线性的，唯一在吸收体处等于 $1$ 的有界函数是 $u = 1$（在二维中 $u$ 按对数变化，行走同样是常返的）。从半径为 $a$ 的细胞上的受体解离的配体，基本上从 $r_0 = a$ 出发，很可能再次撞上细胞；如果表面带有许多受体，它可能在逃逸之前重新结合许多次。这种重新结合增加配体在细胞上的表观停留时间，并影响浓度感知的精度（[7.6.35](/7.6.35)）。

10. （设计题）你想知道细胞中的囊泡是靠扩散运动还是被马达运载。描述如何根据单粒子轨迹判断，以及每种情形下你预期什么结果。

    **答** 以足以分辨其运动的帧率（比如 $20\,\mathrm{ms}$）追踪许多囊泡，并计算均方位移对滞后时间的关系（[7.3.2](/7.3.2)）。扩散给出像平面内的 $\mathrm{MSD} = 4Dt$（对数–对数图上斜率为 $1$）；马达运输在大于 $4D/v^2$ 的滞后处给出 $\mathrm{MSD} \approx 4Dt + v^2t^2$（斜率趋近 $2$），并且定向的奔跑显示相继步之间的速度相关；限制则给出平台。进一步的检验：使微管解聚或耗尽 ATP 应当消除定向奔跑；位移的分布对扩散是 Gauss 型，对间歇的运输有长尾。在活细胞中，由于拥挤和主动搅动，MSD 常以中间的指数增长，必须用这些对照把它与运输区分开（[7.6.23](/7.6.23)）。
