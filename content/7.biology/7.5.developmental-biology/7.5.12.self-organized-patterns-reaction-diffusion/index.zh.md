---
title: 自组织图式：反应扩散与侧向抑制
description: 图式如何在没有模板的情况下产生。水螅嫁接与短程激活–长程抑制的现象学；化学动力学、作为 Lyapunov 函数的 Gibbs 函数，以及为什么必须打破细致平衡；Turing 不稳定性、最快增长模式与 Turing 自己的例子；由能量积分得到的非均匀稳态、绝对与相对的大小调节、Lyapunov 泛函与 Edelstein 开关；Gierer–Meinhardt 模型、它的开关点与等面积规则、弱源与极性的放大、最小半周期；弱非线性振幅方程；预图式与模式选择；Glansdorff–Prigogine 判据；并列分泌式侧向抑制；以及从水螅水母、叶脉到毛囊与指的应用。
source_hash: ceef585620ef
---

上一章的**形态发生素**梯度（[7.5.11](/7.5.11)）是由不对称的源强加的。许多图式则产生于起初均匀或近乎均匀的细胞场：毛囊与羽毛的间距、变成指的周期性凝集、再生水螅的头、斑马鱼的条纹。这样的细胞场是自己组织起来的。Turing（1952）证明，两种以不同速率反应和扩散的物质可以使均匀状态失稳；Gierer 与 Meinhardt（1972）则指出其背后的生物学原理：局部自增强与长程抑制相耦合。本章按问题出现的顺序展开这一理论。化学反应究竟能不能产生图式？扩散何时使均匀状态失稳？随后形成什么样的定态图式，它们如何依赖组织的大小？一个微弱而不精确的偏置怎样选定方向？双物种不稳定性的线性理论在 [2.5.7](/2.5.7#sec-7.5.2) 中推导，**Brusselator** 在 [6.3.18](/6.3.18) 中讨论；这里把这些结果当作已知，集中讨论非线性图式及其发育学意义。本章最后讲由细胞直接接触实现的侧向抑制，这一机制已在 [7.3.24](/7.3.24) 中引入；以及后续各章将用到的应用：毛囊（[7.5.22](/7.5.22)）、指（[7.5.32](/7.5.32)）、左右不对称（[7.5.17](/7.5.17)）与再生（[7.5.35](/7.5.35)）。

## 12.1. 水螅与水螅水母中的自组织

**定义 12.1.1（自组织）** 若空间图式产生于起初等价的组分之间的相互作用，使确定图式的信息（其间距、数目或方向）由动力学本身产生，而不是继承自事先存在的模板，则称发育系统表现出**自组织**。

淡水水螅是经典的检验对象。体柱的一小块可以再生出一个完整的小个体，并保持原来的极性：原来靠近头的一端形成头。所以同一块体柱可以变成头或足，取决于它与什么相连。把体柱片段嫁接到宿主体柱上（用一根头发穿起来）可以回答更具体的问题。极性的逆转要很长时间，而头的决定很快。若原来的头离得很远，少量的头部组织就会在体柱上诱导出附近的头，芽只在离头一定范围之外出现。这种抑制看来是可扩散的，需要时间从新形成的头向外扩散。它的静态作用范围可以用图中那样的嫁接来测量：把体柱片段 1 嫁接到宿主体柱 1-2-3-4 上，交界处不产生头，嫁接 1-2 则产生；嫁接 H-1-2（带头）不产生第二个头，H-1-2-3 则产生。

![水螅的轴向嫁接。宿主体柱 1-2-3-4 接受来自身体上部的体柱片段。当嫁接片段足够大（1-2 而不是单独的 1）并且离已有的头足够远（三个体柱水平而不是两个）时，交界处形成第二个头：头的形成是自增强的，并在远处受到抑制](./plots/hydra-grafts.py)

这些结果概括了一个机制必须做到的事：短程激活、长程可扩散的抑制，以及图式对生物体大小的完美调节。今天，头激活物已确定为下口锥中通过 **β-连环蛋白**起作用的 Wnt3 信号，它激活自身的表达；抑制作用的一部分来自转录因子 Sp5，它由 Wnt 信号诱导，并阻遏 *Wnt3*（Vogg 等，2019）；水螅再生的生物学见 [7.5.35](/7.5.35)。在第 12.5 节的激活物–抑制物模型中，若弱的激活物源从头到足递减，则非激活组织中的抑制物满足 $\dot h=-\lambda h+\nu h''$，按 $\mathrm{e}^{-(\lambda/\nu)^{1/2}x}$ 衰减：抑制的范围是 $(\nu/\lambda)^{1/2}$。小个体的行为如理想化的开关点所预言（一个头，大小成比例）；在轴向嫁接中，头的最终数目主要由激活物源的初始图式决定，足够大的内部峰给出三个半周期的图式（两个头）；从嫁接体中部去除一个头之后，形成新头所需的时间遵循 [7.5.13](/7.5.13#sec-13.2) 中为黏菌推导的扩散延迟。

卵的大小提供了第二个更早的观察。在水螅水母和相关的刺胞动物中，大卵（*Liriope*，约 $0.15\,\mathrm{mm}$）直接发育成水母，中等的卵（*Gonionemus*，约 $0.07\,\mathrm{mm}$）形成浮浪幼虫，固着为水螅体，再出芽产生水母，极小的卵只有在从滋养细胞吸收物质之后才发育。系统的大小这一个参数就能在不同发育途径之间作出选择，这种想法对于自组织机制是自然的，因为被激活区域的数目取决于场的大小（第 12.11 节）；不过这些比较数据只是定性的，并且混合了生活史因多种原因而不同的物种。

## 12.2. 化学动力学：为什么封闭系统不产生图式

### 12.2.1. 自催化与双盒模型

设激活物 $X$ 催化自身由前体 $Y$ 的生成并衰减：$2X+Y\to3X$，$X\to B$，速率常数均取 1。$Y$ 固定时，$\dot X=X^2Y-X$ 有稳定态 $X=0$ 与不稳定态 $X=1/Y$，解 $X=1/(Y+C\mathrm{e}^t)$ 要么衰减，要么在有限时间内爆发。若前体由取之不尽的源供给，$A\to Y$，则 $\dot Y=A-X^2Y$，唯一的定态点为 $X_0=A$，$Y_0=1/A$。其 Jacobi 矩阵

$$
J=\begin{bmatrix}1&A^2\\-2&-A^2\end{bmatrix},\qquad 2\Omega=1-A^2\pm\sqrt{(1-A^2)^2-4A^2},
$$
表明该状态在 $A>1$ 时稳定：$1<A<1+\sqrt2$ 时为阻尼振荡，更大时为单调衰减。

现在把两个这样的盒子 $(X_1,Y_1)$ 与 $(X_2,Y_2)$ 以速率 $D$ 交换前体而耦合起来：$\dot Y_1=A-X_1^2Y_1+D(Y_2-Y_1)$，对称地写出另一个。用和与差表示，$x=\frac12(X_1-X_2)$，$y=\frac12(Y_1-Y_2)$，则均匀态处差模的 Jacobi 矩阵为 $\begin{bmatrix}1&A^2\\-2&-A^2-D\end{bmatrix}$，行列式为 $A^2-D$。只要 $D>A^2$，行列式为负，有一个特征值为正，两个盒子就变得不同：激活物稍多的盒子从邻居那里抽取前体的速度快于扩散把它送回的速度。人们期望能使二者均等的交换，反而使均匀态失稳。

### 12.2.2. 线性化的反应扩散系统

对 $N$ 种物种，浓度 $\xi_\alpha$，反应 $F_\alpha(\xi)$，扩散系数 $D_\alpha$，

$$
\dot\xi_\alpha=F_\alpha(\xi)+D_\alpha\Delta\xi_\alpha .
$$
在均匀稳态附近线性化，把扰动写成 $\mathrm{e}^{\Omega t}\mathrm{e}^{\mathrm{i}\boldsymbol{k}\cdot\boldsymbol{r}}$，则 $\Omega$ 必须是下列矩阵的特征值：

$$
M(k^2)=J-k^2\operatorname{diag}(D_1,\dots,D_N),\qquad J_{\alpha\beta}=\frac{\partial F_\alpha}{\partial\xi_\beta}.
\tag{12.1}
$$
在长度为 $L$、无通量边界的区间上，空间因子为 $\cos kx$，$k=p\pi/L$，$p=0,1,2,\dots$

**命题 12.2.1** 若 $J$ 稳定（所有特征值的实部为负），则在下列每种情形下，$M(k^2)$ 对每个 $k$ 也稳定：(a) 所有 $D_\alpha$ 相等；(b) $J$ 对称；(c) $J$ 是符号稳定的，即对具有相同符号模式的每个矩阵都稳定。

**证明** (a) $M=J-k^2DI$ 使每个特征值平移 $-k^2D$。(b) 对于对称矩阵，最大特征值是 Rayleigh 商的最大值，减去一个半正定的对角矩阵不会使它增大。(c) 符号稳定性由对角元、乘积 $J_{\alpha\beta}J_{\beta\alpha}$ 及更长的环上的符号条件刻画（Quirk 与 Ruppert）；减去一个正对角矩阵保持每个符号不变，所以 $M$ 与 $J$ 有相同的符号模式。$\square$

所以，扩散驱动的不稳定性需要不相等的扩散，并且 Jacobi 矩阵既不对称也不是符号稳定的：某些物种必须自我增强。

### 12.2.3. 热力学：Gibbs 函数是 Lyapunov 函数

为什么在处于平衡的烧杯中找不到图式？在恒温恒压的**理想稀溶液**中，溶质的**化学势**为 $\mu_X=k_{\mathrm{B}}T\ln(X/X_0)$，单位体积的 **Gibbs 自由能**为

$$
\phi=\mu_0+k_{\mathrm{B}}T\sum_X X\Big(\ln\frac X{X_0}-1\Big).
$$
平衡时，对反应所允许的每一种变化都有 $\mathrm{d}\phi=\sum\mu_X\,\mathrm{d}X=0$；对 $X+2A\rightleftharpoons B$，这给出 $\mu_X+2\mu_A=\mu_B$，即**质量作用定律** $XA^2/B=X_0A_0^2/B_0$。动力学取 $\dot X=-kA^2X+k'B$（以及 $\dot A=2\dot X$，$\dot B=-\dot X$），动力学平衡与热力学平衡一致要求 $k'/k=X_0A_0^2/B_0$。

**定理 12.2.1** 对服从质量作用动力学的**封闭系统**，若每个反应的速率常数都满足这些关系，则 $\phi$ 永不增加：$\dot\phi\le0$，等号只在平衡时成立。

**证明** 对上述反应，$\dot\phi=\dot X(\mu_X+2\mu_A-\mu_B)=-k'B_0k_{\mathrm{B}}T\,(y-z)(\ln y-\ln z)$，其中 $y=\frac{XA^2}{X_0A_0^2}$，$z=\frac B{B_0}$，而 $(y-z)(\ln y-\ln z)\ge0$，等号仅当 $y=z$ 时成立。每个反应贡献一个这种形式的项。$\square$

$\phi$ 是 **Lyapunov 函数**（[2.4.11](/2.4.11)）：具有唯一平衡态的封闭系统趋近这个平衡态。扩散并不改变这一点，因为相邻体积之间的交换 $A_1\rightleftharpoons A_2$ 只是又一个正反速率相等的单分子反应。要产生图式，需要一个各个反应不可能同时处于平衡的系统：**细致平衡条件**（每个正反应速率与逆反应速率相等，[6.3.18](/6.3.18)）必须失效。有三种理想化的情形可以打破它。

1. 反应环 $A\rightleftharpoons B\rightleftharpoons X\rightleftharpoons A$，速率常数为 $k,k'$，$l,l'$，$m,m'$：细致平衡要求 $k'l'm'=klm$，即沿环两个方向的速率常数乘积相同。若这一条件不成立，就存在带有循环电流的稳态，但它不是任何 Gibbs 函数的极小值。
2. 源与汇：$A\to X\rightleftharpoons Y\to B$，$A$ 与 $B$ 保持固定，没有返回反应（例如 $A\to\infty$，$k\to0$，$kA$ 固定）。中间物达到稳态 $\bar Y=kA/m$，$\bar X=(l'+m)kA/(lm)$，系统中有净通量通过。每种分子都有合成与降解的活组织就属于这种类型。
3. 无穷大的速率常数：在 $A\rightleftharpoons B+C$，$C\rightleftharpoons X+Y$ 中令 $l\to\infty$，中间物 $C$ 一生成就被消耗，净反应 $A\to B+X+Y$ 没有逆反应。

### 12.2.4. 消去快速的中间物

最后一种情形也说明了有效的**速率方程**是怎样产生的。若 $X+E\rightleftharpoons E^*$ 很快，**解离常数**为 $K=k'/k$，总酶量 $E+E^*=E_0$ 守恒，则每一时刻都有 $E^*=E_0X/(K+X)$。对 $X+E\rightleftharpoons E^*\rightleftharpoons Y+E$，这给出

$$
\dot Y=\frac{lE_0X-Kl'E_0Y}{K+X},
$$
这是 **Michaelis–Menten 方程**（[7.1.9](/7.1.9)）的可逆形式；由于 $\dot X+\dot Y=-\dot E^*$，总底物满足 $\frac{\mathrm{d}}{\mathrm{d}t}\big(X+\frac{E_0X}{K+X}\big)=-\dot Y$。竞争性抑制剂 $I$ 通过 $I+E\rightleftharpoons E^{**}$（解离常数 $K^*$）给分母加上一项，$E^*=E_0(X/K)/(1+I/K^*+X/K)$，这就是**竞争性抑制**。这类饱和项与抑制项出现在下面的每个模型中；它们是快速结合步骤的影子。

## 12.3. 线性不稳定性：Turing 条件

对一维中的两种物种 $a$（激活物）与 $h$（抑制物），

$$
a_t=f(a,h)+\varepsilon a_{xx},\qquad h_t=g(a,h)+\nu h_{xx},
\tag{12.2}
$$
并设均匀稳态对均匀扰动稳定（$f_a+g_h<0$，$f_ag_h-f_hg_a>0$），则模式 $\cos kx$ 的增长率 $\Omega(k^2)$ 满足 $(\Omega+\varepsilon k^2-f_a)(\Omega+\nu k^2-g_h)=f_hg_a$。

**定理 12.3.1（Turing 条件）** (12.2) 的均匀态对某个模式 $k>0$ 不稳定，当且仅当

$$
\nu f_a+\varepsilon g_h>2\sqrt{\varepsilon\nu\,(f_ag_h-f_hg_a)} .
$$
这要求 $f_a>0$（激活物自我增强）、$g_h<0$，以及 $\nu/\varepsilon$ 足够大：抑制物必须扩散得更快。

证明见 [2.5.7](/2.5.7#sec-7.5.2)：$M(k^2)$ 的迹始终为负，当行列式 $\varepsilon\nu k^4-(\varepsilon g_h+\nu f_a)k^2+\det J$ 变为负时发生不稳定。超过阈值后，一个波数带内的模式增长；哪一个增长最快，决定初始间距。

**公式 12.3.1（最快增长模式）** 设 $P=-f_hg_a>0$，$\nu>\varepsilon$，则实增长率 $\Omega(k^2)$ 在

$$
k^2_{\max}=\frac{(\nu+\varepsilon)\sqrt{P/(\varepsilon\nu)}+g_h-f_a}{\nu-\varepsilon},\qquad \Omega_{\max}=\frac{\nu f_a-\varepsilon g_h-2\sqrt{\varepsilon\nu P}}{\nu-\varepsilon}
$$
处最大。

**证明** 令 $u=\Omega-f_a+\varepsilon k^2$，$w=\Omega-g_h+\nu k^2$，则 $uw=-P$。在极大处（$\mathrm{d}\Omega/\mathrm{d}k^2=0$）对 $k^2$ 求导得 $\varepsilon w+\nu u=0$。于是 $w=-\nu u/\varepsilon$，$u^2=\varepsilon P/\nu$；$\Omega$ 较大的分支取 $u=-\sqrt{\varepsilon P/\nu}$，$w=\sqrt{\nu P/\varepsilon}$。令 $\Omega$ 的两个表达式相等，$f_a-\varepsilon k^2-\sqrt{\varepsilon P/\nu}=g_h-\nu k^2+\sqrt{\nu P/\varepsilon}$，得 $k^2_{\max}$；代回得 $\Omega_{\max}$。$\square$

**例 12.3.1（Turing 的例子）** 在适当单位下，Turing 的模型为

$$
f=\frac{a(h-1)}{16}-\frac34,\qquad g=1-\frac{ah}{16},
$$
均匀态为 $a_0=h_0=4$。于是 $f_a=\frac3{16}$，$f_h=\frac14$，$g_a=g_h=-\frac14$，所以 $f_a+g_h=-\frac1{16}$，$\det J=\frac1{64}$：充分混合的系统是稳定的。Turing 条件写为 $\frac3{16}r-\frac1{4r}>\frac14$，其中 $r=\sqrt{\nu/\varepsilon}$，即 $3r^2-4r-4>0$，$r>2$：抑制物的扩散必须比激活物快四倍以上。在化学上，该模型对应 $X+Y\to B$（抑制物使激活物降解）、$C+X+Y\to2X+Y$（激活由二者共同催化）、$A\to Y$（抑制物的供给）、$X\to M$（衰减），以及通过酶 $D$ 以恒定速率移除 $X$，该酶在极限 $D\to0$、$k\to\infty$ 中饱和（$X+D\rightleftharpoons F\to G+D$）。这里抑制物同时也是辅因子，这种"激活物–底物"的模糊性在真实系统中很常见。

![Turing 例子的线性稳定性。A：抑制物与激活物扩散比为 2、4（阈值）和 8 时，最大增长率对波数的曲线；圆点标出公式 12.3.1 的最快模式。B：在长度为 40、两端无通量的区间上只存在离散的模式 k = p pi / L，只有位于不稳定带之内的才增长](./plots/turing-dispersion.py)

## 12.4. 非均匀稳态

线性理论说明图式会开始形成；非线性项决定它最终成为哪种定态图式。由于增长可能终止于定态、振荡或不规则状态，我们集中讨论定态，因为它给细胞提供恒定的信息来解释。

### 12.4.1. 能量积分

不稳定性要求 $\nu/\varepsilon$ 很大。取极端情形 $\varepsilon=0$，并设 $f(a,h)=0$ 有唯一解 $a=A(h)$。定态问题变为

$$
\nu h''+g(A(h),h)=0,\qquad h'(0)=h'(L)=0,
\tag{12.3}
$$
乘以 $h'$ 得能量积分

$$
\frac\nu2h'^2+V(h)=E,\qquad V(h)=\int^hg(A(s),s)\,\mathrm{d}s,
$$
这是质量为 $\nu$ 的粒子在势 $V$ 中的运动，以 $x$ 为时间（单组分情形见 [7.5.11](/7.5.11#sec-11.3.4)）。粒子在 $x=0$ 处以零速度出发，必须在 $x=L$ 处再次停下；在转折点 $h_0(E)$ 与 $h_1(E)$ 之间走一趟所需的时间为

$$
\chi(E)=\sqrt{\frac\nu2}\int_{h_0(E)}^{h_1(E)}\frac{\mathrm{d}h}{\sqrt{E-V(h)}} .
$$

**命题 12.4.1** 设 $\chi_{\min}=\min_E\chi(E)$。若 $L<\chi_{\min}$，则只存在均匀态。若 $\chi_{\min}<L<2\chi_{\min}$，则存在一个半周期（一个高区与一个低区）的图式。一般地，当 $L=p\chi(E)$ 有解时，存在 $p$ 个半周期的图式；长组织中可能有若干组 $(p,E)$，究竟实现哪一个取决于初始扰动。

**例 12.4.1（第二 Turing 系统）** 对 Turing 的例子，$f=0$ 给出 $A(h)=12/(h-1)$，$g(A(h),h)=1-\frac{3h}{4(h-1)}$，所以

$$
V(h)=\int_4^h\Big(1-\frac{3s}{4(s-1)}\Big)\mathrm{d}s=\frac{h-4}4-\frac34\ln\frac{h-1}3 .
$$
在极小点附近，$V(4)=V'(4)=0$，$V''(4)=\frac3{4\cdot9}=\frac1{12}$，所以 $V\approx(h-4)^2/24$，

$$
\chi(E)\approx\sqrt{\frac\nu2}\int\frac{\mathrm{d}h}{\sqrt{E-(h-4)^2/24}}=\sqrt{\frac\nu2}\sqrt{24}\int_{-1}^1\frac{\mathrm{d}y}{\sqrt{1-y^2}}=\pi\sqrt{12\nu},
$$
与 $E$ 无关；由于 $\chi$ 随 $E$ 增大，这就是 $\chi_{\min}$。取 $\nu=\frac14$，$L=60$，约可容纳十一个半周期。因为 $\chi(E)$ 在小 $E$ 处几乎是平的，所以一个狭窄的线性不稳定模式带不能选定确定的半周期数。

![激活物不扩散的第二 Turing 系统的能量积分。A：带有三个能级的势 V(h)。B：(h, h') 平面中对应的闭曲线，稳定图式沿这些曲线以 x 为时间运动。C：半周期 chi(E) 在小 E 时趋于 pi sqrt(12 nu)，并随 E 增大](./plots/energy-integral.py)

### 12.4.2. 绝对与相对的大小调节

有两种极端情形在生物学上很重要。在绝对调节中，被激活区域的大小由扩散与降解决定而固定，与组织的大小无关；在相对调节中，它是组织的固定分数。一个模型属于哪一种，可以从 $V$ 在转折点附近的形状读出。在 $h_M$ 处的势极小值 $V_M$ 的左侧量取 $x_0$，右侧量取 $x_1$。在第一个半周期中把变量由 $h$ 换成 $V$，

$$
x_1(V)=\sqrt{\frac\nu2}\int_{V_M}^V\frac{h_1'(V')\,\mathrm{d}V'}{\sqrt{E-V'}}=\sqrt{2\nu}\,h_1'(E)\Big[(E-V_M)^{1/2}-(E-V)^{1/2}\Big]+\cdots,
$$
所以高 $h$ 区的范围是 $x_1(E)\approx\sqrt{2\nu}\,h_1'(E)(E-V_M)^{1/2}$，类似地 $x_0(E)\approx\sqrt{2\nu}\,(-h_0'(E))(E-V_M)^{1/2}$，且 $\chi=x_0+x_1$。

**命题 12.4.2** (a) 若 $h_1'(E)(E-V_M)^{1/2}$ 为常数，即 $V$ 是抛物线 $V=V_M+(h-h_M)^2/c^2$，则高区的大小与 $L$ 无关（绝对大小调节）。然而此时曲线本身通过 $(h-h_M)/(E-V_M)^{1/2}$ 依赖于 $E$；整条曲线要做到接近绝对调节，需要 $V$ 达到极大值 $\bar h$，在其附近 $E$ 的微小变化就能分配出无限长的组织。(b) 若 $x_1/x_0=h_1'(E)/(-h_0'(E))$ 为常数，则两个区保持固定比值（相对大小调节）。对幂律 $h_0=b_0-c_0(V-V_M)^{q_0}$ 与 $h_1=b_1+c_1(V-V_M)^{q_1}$，这要求 $q_0=q_1$；若幂律一直延伸到 $V_M$（于是 $b_0=b_1=h_M$），则 $V$ 的某一阶导数在 $V_M$ 处不连续；此时图式在重标度的变量 $x^*=x/(E-V_M)^{q_1-1/2}$ 与 $h^*=(h-h_M)/(E-V_M)^{q_1}$ 下不变。

极限情形 $q_0=q_1=1$，即带尖点的势，给出完美的相对调节，如 [7.5.11](/7.5.11)（命题 11.3.1）。尖点自然地产生于激活物两个分支之间的开关（第 12.5 节）。

### 12.4.3. 非均匀态的稳定性

对于动力学 $\dot a=f(a,h)$，$\dot h=g+\nu h''$，图式 (12.3) 稳定吗？由于 (12.3) 是 $\int(\frac\nu2h'^2-V)\,\mathrm{d}x$ 的 Euler–Lagrange 方程，试取泛函 $\mathcal{L}=\int\big(\frac\nu2h'^2-W(a,h)\big)\mathrm{d}x$。

**定理 12.4.1** 若可以选取 $W$ 使 $4fW_a\ge(W_h-g)^2$，且等号只在 $f=0=W_h-g$ 处成立，则 $\mathcal{L}$ 沿解递减，直到到达稳态 (12.3)，因此该稳态是稳定的。特别地，取 $W=w(a)+\int^hg(a,s)\,\mathrm{d}s$，使 $W_h=g$，$W_a=\int_{h(a)}^hg_a(a,s)\,\mathrm{d}s$（其中 $h(a)$ 是 $f(a,h)=0$ 的解），条件就是当 $h\ne h(a)$ 时 $fW_a>0$。

**证明** 利用方程并在无通量端点分部积分，

$$
\dot{\mathcal{L}}=\int\big[\nu h'\dot h'-\dot aW_a-\dot hW_h\big]=-\int\big[(g+\nu h'')^2+(W_h-g)(g+\nu h'')+fW_a\big],
$$
配方得

$$
\dot{\mathcal{L}}=-\int\Big[g+\nu h''+\tfrac12(W_h-g)\Big]^2\mathrm{d}x-\int\Big[fW_a-\tfrac14(W_h-g)^2\Big]\mathrm{d}x\le0 .\qquad\square
$$

**定义 12.4.1（Edelstein 开关）** **Edelstein 开关**是激活物–抑制物模型

$$
f(a,h)=\frac{1+\alpha h^2}{1+h^2}-a,\qquad g(a,h)=\lambda a-\mu h,\qquad\alpha>1,
$$
其均匀稳态的个数在 $\mu/\lambda$ 很小或很大时为一个，在中间范围内为三个（两个稳定），所以 $\lambda$ 的微小变化就能使工作点在低 $a$ 与高 $a$ 之间切换。

**例 12.4.2** 对 Edelstein 开关，$A(h)=\frac{1+\alpha h^2}{1+h^2}$，$g(A(h),h)=\lambda\alpha-\frac{\lambda(\alpha-1)}{1+h^2}-\mu h$，所以 $V(h)=\lambda\alpha h-\frac\mu2h^2-\lambda(\alpha-1)\tan^{-1}h$。它的两个极大值意味着，调节参数可以把无限长的组织分配给 $h$ 的任一极端；除非刻意避免，周期性图式是普遍的。非均匀态是稳定的：$h(a)=\big(\frac{a-1}{\alpha-a}\big)^{1/2}$，$\lambda^{-1}W_a=h-\big(\frac{a-1}{\alpha-a}\big)^{1/2}$，所以

$$
fW_a=\lambda\Big(\frac{1+\alpha h^2}{1+h^2}-a\Big)\Big(h-\Big(\frac{a-1}{\alpha-a}\Big)^{1/2}\Big),
$$
而 $\frac{1+\alpha h^2}{1+h^2}-a=\alpha-a-\frac{\alpha-1}{1+h^2}$ 随 $h$ 递增，并在 $h=h(a)$ 处为零，所以两个因子同号：$fW_a\ge0$（对 $1\le a\le\alpha$，在 $f=0$ 附近）。

## 12.5. 多稳态与 Gierer–Meinhardt 模型

**定义 12.5.1（Gierer–Meinhardt 模型）** **Gierer–Meinhardt 模型**是激活物–抑制物系统

$$
a_t=\frac{p_aa^2}{(1+k_aa^2)h}-\gamma_aa+\mu_a+D_a\Delta a,\qquad h_t=p_ha^2-\gamma_hh+\mu_h+D_h\Delta h,
$$
其中激活物 $a$ 协同地增强自身的产生（饱和系数为 $k_a$），抑制物 $h$ 与 $a^2$ 成正比地产生并抑制激活物，二者都衰减，$\mu_a$、$\mu_h$ 是基础源，且 $D_h\gg D_a$。取 $\mu_h=0$ 的标度形式为

$$
f(a,h)=\frac{a^2}{h(1+a^2)}-\frac a2+\mu,\qquad g(a,h)=a^2-\lambda h .
\tag{12.4}
$$

饱和是快速结合步骤的 Michaelis–Menten 影子（第 12.2.4 节）。与第 12.4 节的系统不同，现在 $f(a,h)=0$ 有一个或三个解：对 $\mu=0$，$A_0(h)=0$，以及 $h\le1$ 时的 $A_{1,2}(h)=\frac1h\mp\sqrt{\frac1{h^2}-1}$。设系统在开关点 $h_s$ 处从最低分支跳到最高分支。沿这样的路径，$V=\int g\,\mathrm{d}h$ 在 $h_s$ 附近分段线性，下方为 $V=V_s-\lvert g_0\rvert(h-h_s)$，上方为 $V_s+g_1(h-h_s)$，其中 $g_0=-\lambda h_s$，$g_1=A_2(h_s)^2-\lambda h_s$。

**命题 12.5.1（开关点处的相对调节）** 取 $V_s=0$，开关在 $x=0$ 处，则稳态图式为

$$
h=h_s+\frac E{g_1}-\frac{g_1}{2\nu}\Big(x-\frac{\sqrt{2\nu E}}{g_1}\Big)^2\ (x>0),\qquad h=h_s-\frac E{\lvert g_0\rvert}+\frac{\lvert g_0\rvert}{2\nu}\Big(x+\frac{\sqrt{2\nu E}}{\lvert g_0\rvert}\Big)^2\ (x<0),
$$
组织长度为 $L=\sqrt{2\nu E}\big(\frac1{g_1}+\frac1{\lvert g_0\rvert}\big)$。被激活的区域（$h>h_s$，$a=A_2$）占组织的分数 $\lvert g_0\rvert/(g_1+\lvert g_0\rvert)$，与 $L$ 无关。

**证明** 在每一侧，$\nu h''=-V'$ 是常数，为 $-g_1$ 或 $+\lvert g_0\rvert$；解在 $x=0$ 处通过 $h_s$，此处 $\frac\nu2h'^2=E$，转折点在 $x=\sqrt{2\nu E}/g_1$ 与 $-\sqrt{2\nu E}/\lvert g_0\rvert$。$\square$

随着 $E$ 增大，$V$ 偏离线性，首先出现水平切线，所以在大组织中图式趋向绝对调节；若先出现垂直切线，就会存在最大周期，更大的组织就必须重复图式。

开关点在哪里？$a$ 的跳变需要我们忽略了的激活物扩散。取 $\varepsilon a''+f(a,h)=0$，$\varepsilon$ 很小，则 $h$（甚至 $h'$，因为 $\nu h''=-g$ 有界）在跳变处连续，在拉伸变量 $x=x_s+\varepsilon^{1/2}X$ 下，内层问题为

$$
\frac{\mathrm{d}^2a}{\mathrm{d}X^2}+f(a,h_s)=0,\qquad \frac{\mathrm{d}a}{\mathrm{d}X}=0\ \text{at}\ a=A_0(h_s),\ A_2(h_s) .
$$

**定理 12.5.1（等面积规则）** 内层解存在，当且仅当

$$
\int_{A_0(h_s)}^{A_2(h_s)}f(a,h_s)\,\mathrm{d}a=0,
$$
即势 $U(a)=\int^af(s,h_s)\,\mathrm{d}s$ 在两个外侧分支处有相等的极大值（"反 Maxwell"规则）。跳变必须发生，因为中间分支在内层尺度上不稳定：该处的扰动在该尺度上以 $\Omega=f_a-\varepsilon k^2>0$（$k\to0$）增长。

**证明** 内层方程有积分 $\frac12(\mathrm{d}a/\mathrm{d}X)^2+U(a)=E'$；边界条件要求 $U(A_0)=E'=U(A_2)$。$\square$

**例 12.5.1** 对 (12.4)，$\mu=0$，$\int_0^{a_s}\Big(\frac{a^2}{h_s(1+a^2)}-\frac a2\Big)\mathrm{d}a=\frac{a_s-\tan^{-1}a_s}{h_s}-\frac{a_s^2}4=0$，且在上分支有 $h_s=2a_s/(1+a_s^2)$。因此

$$
\tan^{-1}a_s=a_s\,\frac{1+a_s^2/2}{1+a_s^2},\qquad a_s=1.515,\quad h_s=0.920 .
$$
开关点靠近三个分支汇合的 $h=1$，这表明系统可以被微小的外部信号所操纵。一个快速估计是用一般的三次函数代替 $f$，此时等面积条件把中间根放在两个外侧根的平均处，$A_1\approx\frac12(A_0+A_2)$：$\frac1h-\sqrt{h^{-2}-1}=\frac12\big(\frac1h+\sqrt{h^{-2}-1}\big)$ 给出 $h=(8/9)^{1/2}=0.943$。

![Gierer–Meinhardt 模型 (12.4)（mu = 0，lambda = 1）的开关点。A：激活物零倾线的三个分支；从 A0 到 A2 的跳变发生在 h_s。B：在 h_s 处，A0 与 A2 之间 f(a, h_s) 在坐标轴上方与下方的面积相互抵消（a_s = 1.515，h_s = 0.920）。C：由此得到的势 V(h) 在 h_s 处有尖点，这是相对大小调节的条件](./plots/gm-switch.py)

当 $\varepsilon\to0$ 时，所有三态系统在开关点附近的行为是类似的：开关一侧是位于 $A_2(h_s)$ 的激活平台，另一侧是 $A_0$，在较大的偏离时过渡到相应的分支 $A(h)$。

### 12.5.1. 弱源的放大与极性

到目前为止，图式的方向（哪一端被激活）是任意的。Gierer 与 Meinhardt 的要点是，反应扩散系统是一个巧妙的放大器，能把弱的、不规则的、分级的信号转换成强的、有序的图式。设 (12.4) 的激活物源 $\mu(x)$ 是弱的分级量，在无源的均匀态附近线性化，$t=0$ 时 $\delta a=\delta h=0$。对时间取 **Laplace 变换**（[2.5.6](/2.5.6)），对空间取余弦变换 $\hat a(k,\Omega)=\int_0^L\cos(kx)\,\tilde a(x,\Omega)\,\mathrm{d}x$，$k=p\pi/L$。则

$$
\begin{bmatrix}\hat a\\\hat h\end{bmatrix}=\frac{\hat\mu(k)}{\Omega\det(\Omega I-M(k^2))}\begin{bmatrix}\Omega-g_h+\nu k^2\\g_a\end{bmatrix},
$$
其中 $M(k^2)$ 如 (12.1)。极点在 $\Omega=0$ 与 $M(k^2)$ 的特征值处，长时间行为由实部最大的特征值主导，它在 $k^2$ 位于 $\det M(k^2)=0$ 的两根之间时为实的正数，

$$
\frac12\Big(\frac{g_h}\nu+\frac{f_a}\varepsilon\Big)\pm\Big[\frac14\Big(\frac{g_h}\nu-\frac{f_a}\varepsilon\Big)^2+\frac{f_hg_a}{\varepsilon\nu}\Big]^{1/2},
$$
其最大值由公式 12.3.1 给出。在这个极点附近展开，每个模式都按 $\hat\mu(k)\,\mathrm{e}^{\Omega_{\max}(k^2)t}$ 乘以一个固定因子增长。

**命题 12.5.2** 若不稳定带内只有一个模式 $k=p\pi/L$，则只有源的分量 $\hat\mu(k)$ 被放大，它的符号决定图式的极性。若源之后被去除或改变，新的源要与被指数放大了的旧源竞争，在线性近似成立的期间旧源占优势。若带内有几个增长率几乎相等的模式，则早期的图式取决于 $\mu(x)$ 的细节；当 $\varepsilon\to0$ 时，不稳定带无限变宽，许多模式以及两端的边界层同时被激发。

对于比一个半周期稍长的组织，源的最微小的梯度就这样决定哪一端成为头。越过线性阶段，当 $\varepsilon\to0$ 时，$f(a,h)+\mu(x)=0$，$\nu h''+g=0$；若 $a=A(h,\mu)$ 是单值的，则能量依赖于位置，$\frac\nu2h'^2+\int_{h_0(x)}^hg(s,x)\,\mathrm{d}s=E(x)$，且

$$
E'(x)=\int_{h_0(x)}^hg_x(s,x)\,\mathrm{d}s\approx-\mu'(x)\int_{h_0}^h\frac{g_a(A(s),s)}{f_a(A(s),s)}\,\mathrm{d}s,
$$
这里对小的 $\mu$ 用了 $A(h,\mu)\approx A(h)-\mu/f_a$。在自催化与交叉催化系统中 $g_a/f_a<0$（Edelstein 模型为 $-\lambda$，Turing 的模型为 $-h/(h-1)$），所以对 $\mu'>0$，能量在 $h$ 随 $x$ 上升处增大，在下降处减小。由于对 $h'>0$ 的轨迹，$\chi_{\min}=\pi\big(\nu/V_M''\big)^{1/2}$ 迅速增大，具有许多半周期的图式受到抑制，高 $h$ 区被安置在源大的地方。

**命题 12.5.3（分级源中的开关点）** 在三态情形、弱源 $\mu$ 下，开关点按下式移动：

$$
\frac{\partial h_s}{\partial\mu}=-\frac{A_1-A_0}{\int_{A_0}^{A_1}f_h(a,h_s)\,\mathrm{d}a},\qquad \frac{\partial A_i}{\partial\mu}=-\frac{1+f_h^{(i)}\,\partial h_s/\partial\mu}{f_a^{(i)}},
$$
（这里 $A_1$ 表示上外侧分支），并且在开关点的每一侧 $\nu h''=\gamma_{0,1}(x)$，$\gamma(x)=-g+\mu(x)\,(g_a-J\,\partial h_s/\partial\mu)/f_a$，$J=f_ag_h-f_hg_a$。对于在 $x=0$ 处从低值开始、开关点为 $x_1<\dots<x_p$ 的图式，条件 $h'(L)=0$ 与 $h(x_{i+1})-h(x_i)=\frac{\partial h_s}{\partial\mu}(\mu(x_{i+1})-\mu(x_i))$ 在 $p=1$ 时成为 $\int_0^{x_1}\gamma_0+\int_{x_1}^L\gamma_1=0$，而在 $p>1$ 时成为

$$
\int_0^{x_1}\gamma_0+\int_{x_1}^{x_2}\frac{x_2-y}{x_2-x_1}\gamma_1\,\mathrm{d}y=\nu\frac{\partial h_s}{\partial\mu}\frac{\mu(x_2)-\mu(x_1)}{x_2-x_1},
$$
后面的开关点有类似的条件（右端在内部约为 $0$，在线性 $\mu$ 的最后一个开关处约为 $-\nu\,\partial_\mu h_s\,\mu'$）。

**证明** 对 $f(A_0,h_s)+\mu=f(A_1,h_s)+\mu=\int_{A_0}^{A_1}(f(a,h_s)+\mu)\,\mathrm{d}a=0$ 在 $\mu=0$ 处对 $\mu$ 求导：积分的端点项因被积函数在该处为零而消失，留下 $\int_{A_0}^{A_1}(f_h\,\partial_\mu h_s+1)\,\mathrm{d}a=0$。各分支上 $h$ 的方程由 $g(A_i(h_s+\partial_\mu h_s\,\mu),\dots)$ 对 $\mu$ 展开到一阶得到。从 $0$ 起积分 $\nu h''=\gamma$ 并利用 $\int_a^b\int_a^xf\,\mathrm{d}y\,\mathrm{d}x=\int_a^b(b-y)f(y)\,\mathrm{d}y$ 即得这些条件；逐次相减把它们分离开。$\square$

取外侧分支上的典型符号 $f_h<0$（所以 $\partial h_s/\partial\mu>0$）、$f_a<0$、$g_a>0$、$g_h<0$，以及 $-g_0>0$、$-g_1<0$、$g_1/(-g_0)\gg1$。则随着 $\mu$ 增大，$\gamma_1$ 变得更负，而 $\gamma_0$ 从正值开始并递减。由此得到三种情形：源很陡（$\mu'$ 很大）时，$p=1$ 与 $p>1$ 的条件都无法满足，不存在开关点；斜率适中（$\nu\mu'>\max_x\int_0^x\gamma_0>0$）时，恰有一个开关，在源的高端有单个被激活的区域；源很平缓时可能有多个开关点，在极限 $\varepsilon\to0$ 时可有任意多个。有限的 $\varepsilon$ 限制了分辨率。

**公式 12.5.1（最小半周期）** 在开关附近用三次近似 $f=-\alpha(a-A_2)^3+\beta(a-A_2)$，则 $A_1-A_2=\sqrt{\beta/\alpha}$，$f_a(A_1)=-2\beta$，$\frac\varepsilon2(\mathrm{d}a/\mathrm{d}x)^2\big|_{A_2}=\int_{A_2}^{A_1}f\,\mathrm{d}a=\frac{\beta^2}{4\alpha}$，外侧分支之间的过渡至少需要

$$
\Delta x=\frac{A_1-A_0}{\mathrm{d}a/\mathrm{d}x}=\frac{2\sqrt{\beta/\alpha}}{\beta/\sqrt{2\varepsilon\alpha}}=4\Big(\frac{\varepsilon}{-f_a'}\Big)^{1/2},
$$
其中 $f_a'=f_a(A_1,h_s)$：没有任何半周期能比它更短。

![一维 Gierer–Meinhardt 图式。A：由随机噪声出发，抑制物的作用范围较短时，峰以大致规则的间距形成。B：抑制物作用范围较长、源密度在整个组织上只升高 2 % 时，源较大的一端形成单个峰。C：有饱和（kappa = 0.5）时，被激活的区域是一个平台，在长度为 1 和 2 的组织中占大致相同的分数（16 %）](./plots/gm-1d.py)

## 12.6. 弱非线性动力学

发育中的组织很少等待稳态，所以线性阶段之后的动力学很重要。把偏离不稳定均匀态的量写成 $q=(a-\bar a,h-\bar h)$，则

$$
\dot q=Mq+\Delta(q)+\boldsymbol{D}\Delta q,\qquad \boldsymbol{D}=\operatorname{diag}(D,D'),
$$
其中 $M$ 是 Jacobi 矩阵，$\Delta(q)$ 汇集二阶及更高阶的项。设 $\psi_0$ 是主导的不稳定模式，在无通量边界下 $(M+\boldsymbol{D}\Delta)\psi_0=\lambda_0\psi_0$，$\varphi_k$ 是伴随算子的对偶特征函数，按 $\int\varphi_k^*\psi_{k'}=\delta_{kk'}$ 归一化。写 $q=q_0(t)\psi_0+Q$，其中 $Q$ 与 $\psi_0$ 正交，并作投影，

$$
\dot q_0=\lambda_0q_0+\int\varphi_0^*\,\Delta\big(q_0\psi_0+Q\big)\,\mathrm{d}\boldsymbol{r}\approx\lambda_0q_0+\int\varphi_0^*\,\Delta(q_0\psi_0)\,\mathrm{d}\boldsymbol{r},
$$
这是应用于空间的"等效线性化"。

**例 12.6.1** 在 Gierer–Meinhardt 耗竭（激活物–底物）模型 $\dot a=c+a^2h-\gamma a+Da''$，$\dot h=c'-a^2h+D'h''$ 中，底物 $h$ 被 $a$ 的产生所消耗。均匀态为 $\bar a=(c+c')/\gamma$，$\bar h=c'\gamma^2/(c+c')^2$，且

$$
M=\begin{bmatrix}\gamma\frac{c'-c}{c'+c}&\frac{(c'+c)^2}{\gamma^2}\\-2\gamma\frac{c'}{c'+c}&-\frac{(c'+c)^2}{\gamma^2}\end{bmatrix},\qquad \Delta=\big(\bar h\,\delta a^2+2\bar a\,\delta a\,\delta h+\delta a^2\delta h\big)\begin{bmatrix}1\\-1\end{bmatrix}.
$$
主导模式为 $\psi_0\propto\cos kx$，$k=\pi K/L$。二次项只含 $\cos^2kx$，它没有 $\cos kx$ 分量，而 $\cos^3kx=\frac34\cos kx+\frac14\cos3kx$，所以只有三次项在投影后保留，于是

$$
\dot q_0=\lambda_0q_0-Bq_0^3,
$$
这是叉形分岔的正规形：当 $B>0$ 时，振幅在 $\sqrt{\lambda_0/B}$ 处饱和。这一投影忽略了二次项产生的二阶模式（$\cos0$ 与 $\cos2kx$）；在自洽的展开（中心流形约化）中，它们在同一阶上修正 $B$，甚至可以改变它的符号，使分岔成为亚临界的，如 [7.5.13](/7.5.13) 的**趋化性**模型那样。

## 12.7. 静态大小调节：小结

稳态、单组分、无通量反应扩散的两种一般的势是：光滑极小，给出绝对大小调节；斜率不连续，只要曲率保持较小就给出相对大小调节（[7.5.11](/7.5.11#sec-11.3.4)）。前者的生化例子很常见；后者需要一个开关。极限的**双组分系统**可以提供它：取 $D=0$，$f(a,h)=0$ 可以有多个分支 $A_i(h)$，其中 $f_a<0$ 的分支在没有扩散时是稳定的；在中间分支上 $\mathrm{d}a/\mathrm{d}h=-f_h/f_a$。无论沿哪个分支，抑制物都满足 $g(A(h),h)+D'h''=0$，$h$ 的无通量条件蕴含 $a$ 的无通量条件，而若中间分支（有扩散时）不稳定，则 $h$ 在由等面积规则（定理 12.5.1）确定的开关点处在外侧分支之间跳变。由此得到的能量积分 $\frac{D'}2h'^2+\varphi(h)=K$（$\varphi'=g(A(h),h)$）恰好具有相对调节所需的带尖点的形式。产生第三个分支的 Gierer–Meinhardt 模型的饱和产生项 $a^2/(1+k_aa^2)$，是快速酶促步骤 $S+E\rightleftharpoons C\to E+P$ 的 Michaelis–Menten 形式，其中 $K_M=k'/k$，$C=E_0S/(K_M+S)$，$\dot P=lE_0S/(K_M+S)$。所以大小调节并不是需要精细调节的性质：任何饱和的自增强反应，只要与快速的抑制物耦合，就能调节其图式的比例。

## 12.8. 预图式与模式选择

**定义 12.8.1（预图式）** **预图式**是弱的分级的不均匀性，例如随空间变化的源密度，它本身并不确定最终的图式，而是使自组织系统的某个模式偏向增长，从而固定图式的方向或位置。

在一维情形，构造一个能保持任意所需的单调分布 $\tilde a(x)$ 的模型太容易了。由 $F(\tilde a(x))=\tilde a''(x)$ 定义 $F$，并取

$$
\dot a=-F(a)+\sigma(a-h)+a'',\qquad \dot h=-\nu F(h)+\nu\sigma(a-h)+\nu h'' .
$$
则 $a=h=\tilde a$ 是一个稳态。把扰动按 $-F'(\tilde a(x))+\mathrm{d}^2/\mathrm{d}x^2$ 的特征函数 $\psi_l$（特征值为 $l$，有上界）展开，每个模式服从矩阵 $\begin{bmatrix}l+\sigma&-\sigma\\\nu\sigma&\nu l-\nu\sigma\end{bmatrix}$，特征方程为 $\Omega^2+[(\nu-1)\sigma-(\nu+1)l]\Omega+\nu l^2=0$。对 $\nu>1$ 与 $\sigma>\frac{\nu+1}{\nu-1}l_{\max}$，所有根的实部都为负：该分布是稳定的。这样，类 Bicoid 的梯度可以在没有任何源的情况下产生，但它不能调节：它的形状固定在绝对坐标中。

那么，为什么 Turing 机制在模型中如此普遍？因为它不是由打开扩散（$D=0\to D>0$，各点反应相互独立）产生的。理想化的初始状态在空间上完全相关，实际上相当于 $D=\infty$；随着相互作用变为局部的，$D$ 变为有限，均匀态失稳。这种不稳定性在 $(\delta a,\delta h)\to(-\delta a,-\delta h)$ 下不变，并允许若干个振幅未知的模式；由预图式与初始涨落决定其中哪一个胜出。

**命题 12.8.1（预图式的模式选择）** 设在 $\Omega$ 中 $\dot a=f+\mu(\boldsymbol{r})+D\Delta a$，$\dot h=g+D'\Delta h$，边界无通量，并把偏离量与源按 Neumann 特征函数 $\psi_k$（$\Delta\psi_k=-k^2\psi_k$）展开。每个分量 $\delta c_k=(\delta a_k,\delta h_k)$ 满足 $\dot{\delta c_k}=M_k\delta c_k+\mu_k(1,0)^{\mathsf T}$，所以

$$
\delta c_k(t)=\mathrm{e}^{tM_k}\delta c_k(0)+\big(\mathrm{e}^{tM_k}-I\big)M_k^{-1}\begin{bmatrix}\mu_k\\0\end{bmatrix}.
$$
若 $\lambda_k^\pm$ 是 $M_k$ 的特征值，$\operatorname{Re}\lambda_k^+\ge\operatorname{Re}\lambda_k^-$，则对大的 $t$，

$$
\delta c_k(t)\approx\frac{M_k-\lambda_k^-}{\lambda_k^+-\lambda_k^-}\Big[\delta c_k(0)+\frac{\mu_k}{\lambda_k^+}\begin{bmatrix}1\\0\end{bmatrix}\Big]\mathrm{e}^{t\lambda_k^+} .
$$
有效振幅是 $\delta a_k(0)+\mu_k/\lambda_k^+$：当几个模式的增长率几乎相等时，在源中占比最大的模式获胜，即使它的增长率略小。

**证明** 对特征值互异的 $2\times2$ 矩阵，任何函数都满足 $p(M)=p(\lambda^-)\frac{M-\lambda^+}{\lambda^--\lambda^+}+p(\lambda^+)\frac{M-\lambda^-}{\lambda^+-\lambda^-}$（Sylvester 公式）。把它应用于 $p=\mathrm{e}^{tz}$ 与 $p=(\mathrm{e}^{tz}-1)/z$，保留增长的指数项即得结果。$\square$

## 12.9. 热力学稳定性判据

非平衡态热力学自己提供了一个稳定性判据。对于化学计量系数为 $\nu_{k\alpha}$（被消耗的物种为负）的单位反应 $k$，**Gibbs 自由能**的变化为 $\Delta\phi_k=k_{\mathrm{B}}T\sum_\alpha\nu_{k\alpha}\ln(\xi_\alpha/A_\alpha)$，反应速度为 $u_k$ 时，$\dot\phi=k_{\mathrm{B}}T\sum_ku_k\sum_\alpha\nu_{k\alpha}\ln(\xi_\alpha/A_\alpha)$，其中扩散被当作单分子反应。Glansdorff 与 Prigogine 称一个状态是稳定的，若邻近的每个状态都放出自由能，$\sum\delta u_k\nu_{k\alpha}\delta\ln\xi_\alpha<0$；由于 $F_\alpha=\sum_ku_k\nu_{k\alpha}$，这就是 $\sum\delta F_\alpha\,\delta\ln\xi_\alpha<0$，即**超熵产生**为负的条件（[6.3.18](/6.3.18)）。写成二次型，

$$
\frac1{\xi_\alpha}\frac{\partial F_\alpha}{\partial\xi_\beta}+\frac1{\xi_\beta}\frac{\partial F_\beta}{\partial\xi_\alpha}\quad\text{is negative definite.}
\tag{12.5}
$$

**定理 12.9.1（Lyapunov 矩阵判据）** 矩阵 $M$ 稳定（所有特征值的实部为负），当且仅当存在正定 Hermite 矩阵 $Q$，使 $QM+M^{\mathsf H}Q$ 负定。

**证明**（"若"的部分）若 $M\psi=\lambda\psi$ 且 $\operatorname{Re}\lambda\ge0$，则 $\psi^{\mathsf H}(QM+M^{\mathsf H}Q)\psi=(\lambda+\bar\lambda)\psi^{\mathsf H}Q\psi\ge0$，所以 $QM+M^{\mathsf H}Q$ 不可能负定。$\square$

判据 (12.5) 是特殊选择 $Q=\operatorname{diag}(1/\xi_\alpha)$、$M=J$ 的情形。所以它是稳定的充分条件，却不能证明不稳定：违反 (12.5) 的状态仍可能是稳定的，其稳定性可由另一个 $Q$ 证明，反例不难构造。Turing 不稳定性是由色散关系发现的，而不是由这类判据。

## 12.10. 并列分泌式侧向抑制

在上皮中，抑制往往不是通过扩散，而是通过直接接触传递的：这就是 Delta–Notch 信号的**侧向抑制**（[7.3.24](/7.3.24#def-24.3.3)）。偶然产生稍多 Delta 的细胞更强地激活邻居的 Notch；Notch 活性在接收细胞中阻遏 Delta 与原神经基因（脊椎动物的 *neurogenin*、*NeuroD*；果蝇的 *achaete–scute*），所以这个细胞对邻居的抑制较弱。相邻细胞之间的双重负反馈环放大了微小的差异。Collier 等（1996）的模型，即 [7.3.24 的方程 (24.1)](/7.3.24#eq-24.1)，及其在六角形细胞层上的不稳定性条件已在那里推导。在一排细胞上，交替模式的邻居平均值是细胞自身偏离量的 $\kappa=-1$ 倍，当环路增益超过 1 时，均匀态失稳，$f'(D^*)\,\lvert g'(N^*)\rvert>1$。该分岔是超临界的：图式的振幅在越过阈值后从零连续增长。

**接触抑制**与 Turing 图式的区别在于长度尺度。间距由接触的范围决定，而不是由扩散系数之比决定：只有直接相邻的细胞接触时，最精细的图式是每两个细胞中有一个高细胞（一排细胞）或每三个中有一个（六角形排列）。细胞可以用基部的长突起延伸作用范围，如间隔果蝇胸背感觉刚毛的表皮细胞那样，这时刚毛之间间隔数个细胞（Cohen 等，2010）。顺式抑制，即一个细胞中的 Delta 使同一细胞中的 Notch 失活，使每个细胞要么是发送者要么是接收者，并使开关变得更锐利（Sprinzak 等，2010）。

![30 个细胞的环上的并列分泌式侧向抑制（Collier 模型，a = 0.01）。A：直接相邻细胞接触时，细胞排分解为交替的高 Delta（红）与低 Delta（灰）细胞；接触延伸到两个细胞（如通过长突起）时，高 Delta 细胞相距更远。随机初始状态留下了两个低细胞并排的缺陷。B：最终图式的振幅对反馈强度 b 的关系，在线性阈值 f'(D*) |g'(N*)| = 1 处从零开始上升](./plots/lateral-inhibition-row.py)

| 性质 | 扩散式激活物–抑制物（Turing） | 并列分泌式侧向抑制 |
|---|---|---|
| 抑制的传递方式 | 分泌分子的扩散 | 接触（Delta–Notch）、突起 |
| 激活物 | 自增强、扩散缓慢 | 细胞自主（原神经基因） |
| 间距由什么决定 | $\sqrt{D_h/\gamma_h}$，动力学 | 接触的细胞数 |
| 典型结果 | 点、条纹、迷宫、单个峰 | 椒盐式、棋盘式 |
| 例子 | 毛囊、指、水螅的头 | 神经前体、刚毛、毛细胞、肠分泌细胞 |

## 12.11. 应用

二维反应扩散依参数而产生斑点或条纹。在 Gierer–Meinhardt 模型中，由激活物的饱和决定：没有强饱和时，激活物集中在孤立的峰中；有饱和时，峰长不高，被激活的区域向侧面扩展，形成条纹。两种情形下的间距都是内禀的，数量级与最快模式的波长相当。

![在周期性方形区域上由噪声生长的二维 Gierer–Meinhardt 图式。弱饱和（kappa = 0.1）给出大致六角晶格上的孤立峰；较强的饱和（kappa = 0.45）给出具有相同内禀间距的条纹与迷宫](./plots/turing-2d.py)

水螅水母。若未激活的组织对应水螅体，被激活的组织对应水母，则理想化的开关机制在二维或三维中为：在 $h<h_s$ 处 $\nu\Delta h=-\lvert g_0\rvert$，在 $h>h_s$ 处 $\nu\Delta h=g_1$，这一问题类似于静电学，两个区域有符号相反的电荷密度，并有绝缘边界（$\partial h/\partial n=0$ 起外部介电常数为零的作用）。大卵很容易整个被激活；小卵的"热点"激活反映的是形状、边界条件还是局部抑制物降解的变化，模型无法判定。

血管图式。被激活的区域一旦形成，就能使细胞不可逆地转入新的状态，这改变了源，从而改变下一阶段的图式。在 Meinhardt 的叶脉模型中，激活物 $A$ 消耗底物 $S$，并通过 Edelstein 型开关使细胞转入分化状态 $Y$：

$$
\dot A=cA^2S-\mu A+D_a\Delta A,\qquad \dot S=c_0-cA^2S-\gamma S-\varepsilon YS+D_s\Delta S,\qquad \dot Y=dA-eY+\frac{Y^2}{1+fY^2}.
$$
在 $A=0$ 时，开关有稳定态 $Y_0=0$ 与 $Y_0=\big(1+\sqrt{1-4\mathrm{e}^2f}\big)/(2ef)$，正的 $A$ 使它们按 $A$ 的比例移动，所以高水平的 $A$ 触发持久的高 $Y$。分化的细胞消耗 $S$，使 $A$ 在局部降低；被激活的斑点于是继续前行，受到来自后方和任何边界的抑制，可以分裂成一条或两条通道，留下分化细胞的分支轨迹。当前的研究用 PIN 蛋白介导的生长素极性运输（渠化）解释叶脉形成，这是一种相关的自增强机制（[7.12](/7.12)）。

| 系统 | 提出的自组织相互作用 | 章 |
|---|---|---|
| 毛囊、羽毛 | WNT（激活物）与 DKK（抑制物），以及 EDA 与 BMP | [7.5.22](/7.5.22) |
| 指 | BMP、SOX9 与 WNT，Hox 基因决定波长 | [7.5.32](/7.5.32) |
| 左右不对称、中胚层 | Nodal（激活物）与 Lefty（抑制物，扩散更快） | [7.5.16](/7.5.16)，[7.5.17](/7.5.17) |
| 水螅的头 | Wnt3 与 β-连环蛋白，Sp5 | [7.5.35](/7.5.35) |
| 斑马鱼条纹 | 黑色素细胞与黄色素细胞之间依赖接触的相互作用，没有可扩散分子的类 Turing 系统 | — |
| 腭皱、牙 | FGF 与 SHH | — |

要证明某一图式由 Turing 机制产生，仅仅相似是不够的：该机制预测间距随扩散系数和动力学参数而变，而不随组织大小而变；去除抑制物使图式变密或变得均匀，而不是消失；扰动场（切割、嫁接）导致调节，而不是图式元素的丢失。

## 小结

| 主题 | 主要结果 |
|---|---|
| 自组织 | 定义 12.1.1；水螅嫁接：短程激活、长程抑制、大小调节 |
| 动力学 | 双盒模型在 $D>A^2$ 时不稳定；$D$ 相等、$J$ 对称或符号稳定时没有扩散驱动的不稳定性（命题 12.2.1）；Gibbs 函数是 **Lyapunov 函数**（定理 12.2.1）；图式需要打破细致平衡（环、源与汇、不可逆步骤）；快速结合给出 Michaelis–Menten 项与抑制项 |
| Turing | $\nu f_a+\varepsilon g_h>2\sqrt{\varepsilon\nu\det J}$（定理 12.3.1）；最快模式（公式 12.3.1）；Turing 的例子需要 $\nu/\varepsilon>4$（例 12.3.1） |
| 稳态 | 能量积分 $\frac\nu2h'^2+V=E$；半周期 $\chi(E)$，Turing 系统的 $\chi_{\min}=\pi\sqrt{12\nu}$（例 12.4.1）；抛物线 $V$：绝对调节，带尖点的 $V$：相对调节（命题 12.4.2）；若 $4fW_a\ge(W_h-g)^2$ 则稳定（定理 12.4.1）；Edelstein 开关（定义 12.4.1） |
| Gierer–Meinhardt | 定义 12.5.1；被激活的分数 $\lvert g_0\rvert/(g_1+\lvert g_0\rvert)$（命题 12.5.1）；等面积规则，$a_s=1.515$，$h_s=0.920$（定理 12.5.1，例 12.5.1）；弱源决定极性（命题 12.5.2–12.5.3）；最小半周期 $4(\varepsilon/-f_a')^{1/2}$（公式 12.5.1） |
| 动力学 | 向主导模式投影给出 $\dot q_0=\lambda_0q_0-Bq_0^3$（例 12.6.1） |
| 预图式 | 任何单调分布都可以被稳定，但不能调节；源的偏置选出有效振幅为 $\delta a_k(0)+\mu_k/\lambda_k^+$ 的模式（命题 12.8.1） |
| 热力学 | Glansdorff–Prigogine 判据 (12.5) 是 $Q=\operatorname{diag}(1/\xi)$ 时的 Lyapunov 判据：充分而非必要（定理 12.9.1） |
| 侧向抑制 | 由接触介导；一排细胞上的阈值为 $f'\lvert g'\rvert>1$；间距由接触范围决定 |

## 思考题

1. 为什么没有源的单一扩散物质不能形成稳定图式，而两种物质可以？请结合 [7.5.11](/7.5.11) 的定理 11.3.2 与命题 12.2.1 回答。

   **答** 对于一种物质与无通量边界，动力学是 Lyapunov 泛函的梯度流，每个非均匀稳态都有一个不稳定模式（分布曲线本身的导数提供了 Rayleigh 商非负的试探函数）。对于两种物质，动力学不必是梯度流：当 Jacobi 矩阵不对称、扩散系数不同时，扩散可以使均匀态失稳（Turing），而由此产生的非均匀态可以是稳定的（定理 12.4.1）。命题 12.2.1 列出了即使有几种物质也做不到这一点的情形：扩散相等、Jacobi 矩阵对称，或动力学是符号稳定的。

2. 在第 12.2.1 节的双盒模型中取 $A=2$，交换速率 $D$ 要多大，两个盒子才会变得不同？哪个盒子获胜？

   **答** 差模的行列式为 $A^2-D$，所以 $D>4$。起初激活物稍多的盒子获胜：它消耗前体更快，前体从邻居流入它，而被夺走前体的邻居失去它的激活物。注意扩散的是前体，而不是激活物：这是一种"激活物耗竭"机制。

3. 对 $\nu/\varepsilon=8$ 的 Turing 例子验证 Turing 条件，并取 $\varepsilon=1$，由公式 12.3.1 计算最快波数及其增长率。这给出的波长是多少？

   **答** $f_a=0.1875$，$f_h=0.25$，$g_a=g_h=-0.25$，$\det J=1/64$。左端 $8(0.1875)-0.25=1.25$，右端 $2\sqrt{8/64}=0.707$：不稳定。取 $P=1/16$：$k^2_{\max}=[9\sqrt{1/128}-0.25-0.1875]/7=(0.7955-0.4375)/7=0.0511$，$k_{\max}=0.226$；$\Omega_{\max}=[1.5+0.25-2\sqrt{0.5}]/7=(1.75-1.414)/7=0.048$。波长 $2\pi/k_{\max}\approx27.8$。（与图中的圆点一致。）

4. 解释为什么服从质量作用动力学并满足细致平衡的封闭化学系统不能形成图式，并指出活胚胎中起作用的是三种打破细致平衡的方式中的哪一种。

   **答** Gibbs 函数单调递减（定理 12.2.1），并在唯一的平衡态处达到极小；该平衡态是均匀的，因为扩散是使浓度均等的反应。图式要求并非所有反应都能同时处于平衡。在胚胎中，每种分子都由代谢供给的前体合成，并降解为被移走的产物：这就是源–汇的理想化，在发育的时间尺度上逆反应可以忽略，由 ATP 和其他代谢物的自由能来维持。

5. 利用命题 12.5.1，计算 $\mu=0$、$\lambda=1$ 的 Gierer–Meinhardt 模型 (12.4) 中被激活区域所占组织的分数。

   **答** $h_s=0.920$，$A_2(h_s)=a_s=1.515$。$g_0=-\lambda h_s=-0.920$，$g_1=a_s^2-\lambda h_s=2.295-0.920=1.375$。分数 $=\lvert g_0\rvert/(g_1+\lvert g_0\rvert)=0.920/2.295=0.40$。被激活的区域占组织的 40 %，与其长度无关（只要能容纳一个半周期且 $\varepsilon$ 很小）。

6. 证明等面积规则的三次近似把中间分支放在两个外侧分支的平均处，并用它估计 (12.4) 的 $h_s$。

   **答** 三次函数 $f=-\alpha(a-A_0)(a-A_1)(a-A_2)$，根为 $A_0<A_1<A_2$，当且仅当它关于中间根反对称，即 $A_1=\frac12(A_0+A_2)$ 时，$\int_{A_0}^{A_2}f\,\mathrm{d}a=0$ 精确成立。对 (12.4)，$A_0=0$，$A_{1,2}=\frac1h\mp s$，$s=\sqrt{h^{-2}-1}$；令 $\frac1h-s=\frac12(\frac1h+s)$，得 $s=\frac1{3h}$，$h^{-2}-1=\frac1{9h^2}$，$h^2=\frac89$，$h=0.943$，精确值为 $0.920$。

7. （实验设计）有人提出，周期性排列的羽芽由 Turing 机制产生。设计三个可以否定这一提议的实验。

   **答** (i) 改变皮肤外植体的大小：Turing 机制保持间距而改变羽芽的数目；预图式机制（由图谱安置羽芽）则会重新缩放或丢失羽芽。(ii) 减少抑制物（例如用 DKK 或 BMP 的拮抗物，或突变体）：Turing 机制预测羽芽变密或融合成扩大的区域；若羽芽只是消失或保持不变，则候选分子不是 Turing 对中的抑制物。(iii) 把真皮与表皮细胞解离再重新聚集：自组织机制在重新聚集的均匀皮肤中会重新形成具有相同间距的羽芽。定量检验还要求间距随实测的扩散系数和动力学速率按预测的方向变化。

8. 在例 12.4.1 中，证明 $\chi(E)$ 随 $E$ 增大。为什么这意味着狭窄的不稳定模式带不能确定半周期的数目？

   **答** $V$ 在左侧比其抛物线近似更陡（在 $h=1$ 处发散），而在右侧更平缓（只线性增长），缓慢的右侧起主导作用：随着 $E$ 增大，粒子在右转折点附近停留得更久，所以 $\chi$ 增大（图中给出了 $\chi(E)$ 的数值）。由于 $p$ 个半周期的图式要求 $L=p\chi(E)$，任何满足 $p\chi_{\min}<L$ 的 $p$ 都对应某个 $E$ 的解：稳态对一整个范围的 $p$ 都存在，出现哪一个取决于初始扰动，而不取决于狭窄的线性带。

9. 对最小半周期（公式 12.5.1），估计 $\varepsilon=10^{-4}$、$f_a'=-1$ 时的 $\Delta x$。与第 12.5 节一维模拟中峰的宽度比较。

   **答** $\Delta x=4\sqrt{10^{-4}}=0.04$。模拟中的峰（激活物扩散为 $\varepsilon^2$ 型的 $10^{-4}$，激活物衰减速率为 1）宽度为百分之几，与这一估计一致：激活物的扩散长度 $\sqrt{\varepsilon/\lvert f_a\rvert}$ 决定每个被激活区域的锐利程度。

10. 一排细胞中的某个细胞使用只与直接相邻者作用的 Delta–Notch 侧向抑制，发育成起抑制作用的命运。证明一排细胞中至多有一半细胞采取这种命运，而在六角形细胞层中至多是三分之一。生物体怎样用同一条信号通路使刚毛相隔四五个细胞？

    **答** 两个起抑制作用的细胞不能相邻，否则各自会阻遏对方；一排细胞中最密的排列是交替排列（每两个中有一个）。在六角形晶格上，其中没有两个细胞相邻的细胞集合至多包含三分之一的细胞（细胞中心三角晶格的三着色），而 $\kappa=-1/2$ 的最快增长模式恰好是这种排列。要使结构相距更远，抑制必须延伸得更远：通过携带 Delta 的基部长突起、通过可扩散的抑制物，或者把侧向抑制与原神经簇的预图式结合起来，由后者限制前体细胞可以出现的位置。
