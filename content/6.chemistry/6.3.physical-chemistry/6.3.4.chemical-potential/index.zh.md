---
title: 多组分系统与化学势
---

前三章处理的都是组成不变的系统：一定量的纯物质，状态由两个变量（如 $T$、$p$）确定。化学关心的却是组成会变的系统：溶液、气体混合物、正在进行的反应和相变。组成可变时，系统的广延性质不再等于各纯组分之和（$50\,\mathrm{mL}$ 水与 $50\,\mathrm{mL}$ 乙醇混合后不到 $100\,\mathrm{mL}$），热力学基本方程也要加上反映物质的量变化的一项。本章先给出多组分系统的分类与组成的表示（4.1），再引入偏摩尔量及其两条基本性质：加和公式与 Gibbs–Duhem 方程（4.2）；偏摩尔 Gibbs 自由能就是化学势，它把 [6.3.3](/6.3.3) 的四个基本方程推广到组成可变的系统，并给出物质传递（扩散、相变、化学反应）的统一判据（4.3）；最后写出各种气体的化学势表达式，用逸度处理实际气体（4.4）。[6.1.8](/6.1.8) 中用"摩尔 Gibbs 自由能"非正式地讨论的内容在这里得到严格的形式。本章是溶液热力学的起点：液态混合物与稀溶液中组分的化学势（[6.3.5](/6.3.5)、[6.3.6](/6.3.6)）都借助与之平衡的气相写出，化学平衡（[6.3.7](/6.3.7)）与相平衡（[6.3.8](/6.3.8)）的条件都是化学势之间的关系，电解质溶液与电化学中的平均活度和电化学势（[6.3.12](/6.3.12)、[6.3.13](/6.3.13)）也由此出发。在生物学中，跨膜的物质输运与渗透同样由化学势之差驱动。

## 4.1. 多组分系统及其组成

### 4.1.1. 混合物与溶液

单组分均相系统的组成固定，是双变量系统。含两种或两种以上物质的系统称为多组分系统，可以是均相的（溶液、气体混合物），也可以是多相的（溶液与其蒸气）。本章讨论多组分均相系统：每种物质都以分子、原子或离子的形式分散在其他物质中，组成可以在一定范围内连续变化。按处理方法分为两类。

**定义 4.1.1** 多组分均相系统中，若各组分都用相同的方法处理，服从相同的经验定律、选取相同的标准态，则称之为**混合物**；若把组分分为**溶剂**与**溶质**，两者服从不同的经验定律、选取不同的标准态，则称之为**溶液**。

混合物可以是气态、液态或固态（**固溶体**，[6.1.4](/6.1.4)）。溶液中，若各组分的聚集态不同，通常把液态物质称为溶剂，把溶于其中的气体或固体称为溶质；若都是液体，一般把含量多的称为溶剂。这种区分不是物质本身的属性，而是处理上的选择：同一个水–乙醇系统，在全浓度范围内讨论时作为混合物，只讨论少量乙醇溶于水时则作为溶液。

### 4.1.2. 组成的表示

组成是多组分均相系统的强度性质。描述物质 B 的含量常用四种量（A 表示溶剂）：

**定义 4.1.2** 设系统中物质 B 的物质的量为 $n_{\mathrm{B}}$、质量为 $m_{\mathrm{B}}$，系统的体积为 $V$，溶剂 A 的质量为 $m_{\mathrm{A}}$。称

$$
w_{\mathrm{B}} = \frac{m_{\mathrm{B}}}{\sum_{\mathrm{C}}m_{\mathrm{C}}}, \qquad c_{\mathrm{B}} = \frac{n_{\mathrm{B}}}{V}, \qquad b_{\mathrm{B}} = \frac{n_{\mathrm{B}}}{m_{\mathrm{A}}}
$$
分别为 B 的**质量分数**、**物质的量浓度**与**质量摩尔浓度**，后两者的常用单位为 $\mathrm{mol\,L^{-1}}$ 与 $\mathrm{mol\,kg^{-1}}$。

再加上**摩尔分数** $x_{\mathrm{B}} = n_{\mathrm{B}}/\sum_{\mathrm{C}}n_{\mathrm{C}}$（[6.1.1](/6.1.1)；气相常写作 $y_{\mathrm{B}}$），共四种。$x_{\mathrm{B}}$、$w_{\mathrm{B}}$、$b_{\mathrm{B}}$ 由称量确定，不随温度变化；$c_{\mathrm{B}}$ 依赖于溶液体积，随温度改变。质量摩尔浓度便于精确配制，在电化学与依数性中用得最多，标准值 $b^\circ = 1\,\mathrm{mol\,kg^{-1}}$；物质的量浓度的标准值 $c^\circ = 1\,\mathrm{mol\,L^{-1}}$（[6.1.6](/6.1.6#sec-6.3.3)）。

换算时取一份方便的溶液量计算。对二组分溶液，

$$
x_{\mathrm{B}} = \frac{b_{\mathrm{B}}M_{\mathrm{A}}}{1 + b_{\mathrm{B}}M_{\mathrm{A}}}, \qquad c_{\mathrm{B}} = \frac{\rho\,b_{\mathrm{B}}}{1 + b_{\mathrm{B}}M_{\mathrm{B}}},
$$
其中 $\rho$ 是溶液的密度，$M$ 是摩尔质量。很稀的溶液中 $x_{\mathrm{B}} \approx b_{\mathrm{B}}M_{\mathrm{A}}$，$c_{\mathrm{B}} \approx \rho_{\mathrm{A}}b_{\mathrm{B}}$，各种浓度彼此成正比；对水溶液 $\rho_{\mathrm{A}} \approx 1\,\mathrm{kg\,L^{-1}}$，$c_{\mathrm{B}}$ 与 $b_{\mathrm{B}}$ 的数值几乎相同。

**例 4.1.1** $w(\ce{H2SO4}) = 5\%$ 的硫酸溶液，$20\,^\circ\mathrm{C}$ 时密度 $1.032\,\mathrm{g\,cm^{-3}}$。取 $100\,\mathrm{g}$ 溶液：$n(\ce{H2SO4}) = 5/98.08\,\mathrm{mol} = 0.0510\,\mathrm{mol}$，$n(\ce{H2O}) = 95/18.015\,\mathrm{mol} = 5.273\,\mathrm{mol}$，所以 $x = 0.0096$，$b = 0.0510/0.095\,\mathrm{mol\,kg^{-1}} = 0.537\,\mathrm{mol\,kg^{-1}}$，$c = 0.0510\,\mathrm{mol}/(100\,\mathrm{g}/1.032\,\mathrm{g\,cm^{-3}}) = 0.526\,\mathrm{mol\,L^{-1}}$。

## 4.2. 偏摩尔量

### 4.2.1. 广延性质的非加和性

对纯物质，$V = nV^*_{\mathrm{m}}(T, p)$，广延性质等于物质的量乘以摩尔量（星号表示纯物质）。多组分系统不是这样。下表是 $20\,^\circ\mathrm{C}$ 下 $100\,\mathrm{g}$ 水（A）–乙醇（B）溶液的体积与混合前两种纯液体体积之和（由 CRC 手册的密度数据算出）：

| $w_{\mathrm{B}}$ | $V^*(\text{乙醇})/\mathrm{cm^3}$ | $V^*(\text{水})/\mathrm{cm^3}$ | 混合前之和$/\mathrm{cm^3}$ | 溶液 $V/\mathrm{cm^3}$ |
|---|---|---|---|---|
| 20% | 25.34 | 80.14 | 105.48 | 103.24 |
| 40% | 50.68 | 60.11 | 110.79 | 106.93 |
| 60% | 76.02 | 40.07 | 116.09 | 112.22 |
| 80% | 101.36 | 20.04 | 121.40 | 118.56 |

溶液的体积总小于混合前之和，原因是水与乙醇之间的氢键使分子堆积得更紧密。一般地，多组分系统的广延性质（质量与物质的量除外）不等于各组分纯态时该性质之和。因此对 $k$ 个组分的均相系统，广延性质是 $k + 2$ 个变量的函数 $X = X(T, p, n_1, \dots, n_k)$，强度性质是 $k + 1$ 个变量的函数（$T$、$p$ 与 $k - 1$ 个独立的摩尔分数）。

### 4.2.2. 偏摩尔量的定义

$X$ 的全微分为

$$
\mathrm{d}X = \left(\frac{\partial X}{\partial T}\right)_{p,n}\mathrm{d}T + \left(\frac{\partial X}{\partial p}\right)_{T,n}\mathrm{d}p + \sum_{\mathrm{B}}\left(\frac{\partial X}{\partial n_{\mathrm{B}}}\right)_{T,p,n_{\mathrm{C}}}\mathrm{d}n_{\mathrm{B}},
\tag{4.1}
$$
下标 $n$ 表示所有物质的量不变，$n_{\mathrm{C}}$ 表示除 B 以外的物质的量不变。

**定义 4.2.1（偏摩尔量）** 设 $X$ 是多组分均相系统的广延性质。称

$$
X_{\mathrm{B}} = \left(\frac{\partial X}{\partial n_{\mathrm{B}}}\right)_{T,p,n_{\mathrm{C}}}
$$
为物质 B 的**偏摩尔量**。$X = V$ 时称为 B 的**偏摩尔体积** $V_{\mathrm{B}}$；同样有偏摩尔内能 $U_{\mathrm{B}}$、偏摩尔焓 $H_{\mathrm{B}}$、偏摩尔熵 $S_{\mathrm{B}}$、偏摩尔 Helmholtz 自由能 $A_{\mathrm{B}}$ 与偏摩尔 Gibbs 自由能 $G_{\mathrm{B}}$。

$V_{\mathrm{B}}$ 的物理意义有两种等价的说法：在 $T$、$p$ 与其他组分的量不变时，系统体积随 B 的物质的量的变化率；或者，向一个很大的、组成给定的系统中加入 $1\,\mathrm{mol}$ B（组成几乎不变）时系统体积的增加。使用时注意：

1. 只有广延性质才有偏摩尔量；$C_{p,\mathrm{m}}$ 这样的强度性质没有。
2. 下标必须是 $T$、$p$、$n_{\mathrm{C}}$。在 $T$、$V$ 或 $S$、$p$ 不变时对 $n_{\mathrm{B}}$ 的偏导数（如 $(\partial H/\partial n_{\mathrm{B}})_{S,p,n_{\mathrm{C}}}$）不是偏摩尔量。
3. 偏摩尔量是两个广延量之比，是强度性质，由 $T$、$p$ 与组成确定，与系统的大小无关；它是溶液整体的性质，而不是 B 分子本身的性质。
4. 偏摩尔量只对均相系统定义：水与乙醇的气液两相系统的总体积没有偏摩尔量，但每一相各有自己的偏摩尔量。
5. 对纯物质，$X_{\mathrm{B}} = X^*_{\mathrm{m,B}}$；一般 $X_{\mathrm{B}} \ne X^*_{\mathrm{m,B}}$，甚至可以是负值。例如在无限稀的水溶液中 $\ce{MgSO4}$ 的偏摩尔体积约为 $-1.4\,\mathrm{cm^3\,mol^{-1}}$：离子使周围的水分子排列得更紧密（电致伸缩），加入的盐使溶液总体积减小。

### 4.2.3. 加和公式

**定理 4.2.1（偏摩尔量的加和公式）** 多组分均相系统的广延性质等于各组分的物质的量与其偏摩尔量的乘积之和：

$$
X = \sum_{\mathrm{B}}n_{\mathrm{B}}X_{\mathrm{B}}.
\tag{4.2}
$$

**证明** 在 $T$、$p$ 不变时，把每个组分的量都乘以 $\lambda$，系统扩大为原来的 $\lambda$ 倍，组成不变：$X(T, p, \lambda n_1, \dots, \lambda n_k) = \lambda X(T, p, n_1, \dots, n_k)$。即 $X$ 是 $n_1, \dots, n_k$ 的一次**齐次函数**。由 Euler 齐次函数定理（[2.2.10 定理 10.7.2](/2.2.10#thm-10.7.2)，一次齐次的情形），$\sum_{\mathrm{B}}n_{\mathrm{B}}(\partial X/\partial n_{\mathrm{B}}) = X$。$\square$

也可以这样理解：在 $T$、$p$ 不变下按最终组成的比例同时加入各组分，过程中组成不变，各 $X_{\mathrm{B}}$ 都是常数，积分 $\mathrm{d}X = \sum_{\mathrm{B}}X_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$ 即得式 (4.2)。式 (4.2) 说明，偏摩尔量是把系统的广延性质"分摊"给各组分的唯一自洽的方式；但 $n_{\mathrm{B}}V_{\mathrm{B}}$ 并不是 B 在溶液中实际占据的体积（它可以是负的）。对其他偏摩尔量同样有 $G = \sum_{\mathrm{B}}n_{\mathrm{B}}G_{\mathrm{B}}$、$H = \sum_{\mathrm{B}}n_{\mathrm{B}}H_{\mathrm{B}}$ 等，而且定义式之间的关系对偏摩尔量照样成立，例如 $G_{\mathrm{B}} = H_{\mathrm{B}} - TS_{\mathrm{B}}$（对 $G = H - TS$ 在 $T$、$p$、$n_{\mathrm{C}}$ 不变时求 $n_{\mathrm{B}}$ 的偏导数）。

除以总物质的量 $n$，得平均摩尔量 $X_{\mathrm{m}} = X/n = \sum_{\mathrm{B}}x_{\mathrm{B}}X_{\mathrm{B}}$。对二组分系统，偏摩尔量可以由 $X_{\mathrm{m}}$–$x_{\mathrm{B}}$ 曲线用截距法求出：

$$
X_{\mathrm{A}} = X_{\mathrm{m}} - x_{\mathrm{B}}\frac{\mathrm{d}X_{\mathrm{m}}}{\mathrm{d}x_{\mathrm{B}}}, \qquad X_{\mathrm{B}} = X_{\mathrm{m}} + (1 - x_{\mathrm{B}})\frac{\mathrm{d}X_{\mathrm{m}}}{\mathrm{d}x_{\mathrm{B}}}.
\tag{4.3}
$$
即在组成 $x_{\mathrm{B}}$ 处作曲线的切线，它在 $x_{\mathrm{B}} = 0$ 与 $x_{\mathrm{B}} = 1$ 处的截距分别是 $X_{\mathrm{A}}$ 与 $X_{\mathrm{B}}$。证明：$X = nX_{\mathrm{m}}(x_{\mathrm{B}})$，$x_{\mathrm{B}} = n_{\mathrm{B}}/(n_{\mathrm{A}} + n_{\mathrm{B}})$，在 $n_{\mathrm{A}}$ 不变时对 $n_{\mathrm{B}}$ 求导，$(\partial x_{\mathrm{B}}/\partial n_{\mathrm{B}})_{n_{\mathrm{A}}} = (1 - x_{\mathrm{B}})/n$，所以 $X_{\mathrm{B}} = X_{\mathrm{m}} + n\,\frac{\mathrm{d}X_{\mathrm{m}}}{\mathrm{d}x_{\mathrm{B}}}\cdot\frac{1 - x_{\mathrm{B}}}{n}$；$X_{\mathrm{A}}$ 由加和公式 $X_{\mathrm{m}} = x_{\mathrm{A}}X_{\mathrm{A}} + x_{\mathrm{B}}X_{\mathrm{B}}$ 得到。

![由上表数据计算的水–乙醇溶液平均摩尔体积及截距法（左）；用两参数 Redlich–Kister 式拟合超额体积后得到的两组分偏摩尔体积相对于纯液体摩尔体积的变化（右）。只有四个数据点，拟合在乙醇很稀的区域（$x_{\mathrm{B}} < 0.05$，未画出）不可靠。](./plots/ethanol-water-volume.py)

### 4.2.4. Gibbs–Duhem 方程

各组分的偏摩尔量并不独立。

**定理 4.2.2（Gibbs–Duhem 方程）** 多组分均相系统中，

$$
\sum_{\mathrm{B}}n_{\mathrm{B}}\,\mathrm{d}X_{\mathrm{B}} = \left(\frac{\partial X}{\partial T}\right)_{p,n}\mathrm{d}T + \left(\frac{\partial X}{\partial p}\right)_{T,n}\mathrm{d}p.
\tag{4.4}
$$
特别地，在 $T$、$p$ 不变时

$$
\sum_{\mathrm{B}}n_{\mathrm{B}}\,\mathrm{d}X_{\mathrm{B}} = 0, \qquad \sum_{\mathrm{B}}x_{\mathrm{B}}\,\mathrm{d}X_{\mathrm{B}} = 0.
\tag{4.5}
$$

**证明** 对加和公式 (4.2) 求全微分：$\mathrm{d}X = \sum_{\mathrm{B}}n_{\mathrm{B}}\,\mathrm{d}X_{\mathrm{B}} + \sum_{\mathrm{B}}X_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$。与式 (4.1) 比较即得式 (4.4)。$\square$

加和公式是同一状态下 $X$ 与 $X_{\mathrm{B}}$ 之间的关系；Gibbs–Duhem 方程则约束组成变化时各偏摩尔量的变化：二组分系统中 $x_{\mathrm{A}}\,\mathrm{d}X_{\mathrm{A}} = -x_{\mathrm{B}}\,\mathrm{d}X_{\mathrm{B}}$，一个增大时另一个必然减小，两者在同一组成处取极值，而且变化幅度与摩尔分数成反比（上图右）。知道一个组分的偏摩尔量随组成的变化，就能求出另一个；这也是检验实验数据的热力学一致性的依据（[6.3.6](/6.3.6)）。

**例 4.2.1** $298\,\mathrm{K}$ 时 $\ce{K2SO4}$ 水溶液中 $\ce{K2SO4}$（B）的偏摩尔体积与质量摩尔浓度 $b$ 的关系为 $V_{\mathrm{B}}/(\mathrm{cm^3\,mol^{-1}}) = 32.280 + 18.216\,(b/b^\circ)^{1/2}$。求水（A）的偏摩尔体积。

**解** 由式 (4.5)，$\mathrm{d}V_{\mathrm{A}} = -(n_{\mathrm{B}}/n_{\mathrm{A}})\,\mathrm{d}V_{\mathrm{B}}$，而 $n_{\mathrm{B}}/n_{\mathrm{A}} = bM_{\mathrm{A}}$。记 $\beta = b/b^\circ$，$\mathrm{d}V_{\mathrm{B}} = 9.108\,\beta^{-1/2}\,\mathrm{d}\beta\ \mathrm{cm^3\,mol^{-1}}$，所以

$$
V_{\mathrm{A}} - V^*_{\mathrm{m,A}} = -\int_0^{\beta}\beta' b^\circ M_{\mathrm{A}}\cdot 9.108\,\beta'^{-1/2}\,\mathrm{d}\beta' = -6.072\,b^\circ M_{\mathrm{A}}\,\beta^{3/2}\ \mathrm{cm^3\,mol^{-1}},
$$
其中 $b^\circ M_{\mathrm{A}} = 0.018015$（量纲一）。$V^*_{\mathrm{m,A}} = 18.068\,\mathrm{cm^3\,mol^{-1}}$，例如 $b = 0.5\,\mathrm{mol\,kg^{-1}}$ 时 $V_{\mathrm{A}} = (18.068 - 0.039)\,\mathrm{cm^3\,mol^{-1}} = 18.029\,\mathrm{cm^3\,mol^{-1}}$。溶质的偏摩尔体积变化很大（从 32.3 增至 45.2），溶剂的却只变化千分之二，正是 $x_{\mathrm{A}}\gg x_{\mathrm{B}}$ 的结果。$\square$

## 4.3. 化学势

### 4.3.1. 定义

**定义 4.3.1（化学势）** 多组分系统中物质 B 的偏摩尔 Gibbs 自由能

$$
\mu_{\mathrm{B}} = G_{\mathrm{B}} = \left(\frac{\partial G}{\partial n_{\mathrm{B}}}\right)_{T,p,n_{\mathrm{C}}}
$$
称为 B 的**化学势**，单位 $\mathrm{J\,mol^{-1}}$。

化学势是 Gibbs 在 1876 年引入的。它作为偏摩尔量满足加和公式与 Gibbs–Duhem 方程：

$$
G = \sum_{\mathrm{B}}n_{\mathrm{B}}\mu_{\mathrm{B}}, \qquad \sum_{\mathrm{B}}x_{\mathrm{B}}\,\mathrm{d}\mu_{\mathrm{B}} = 0 \quad (T, p\ \text{不变}).
$$
纯物质的化学势就是其摩尔 Gibbs 自由能，$\mu^*_{\mathrm{B}} = G^*_{\mathrm{m,B}}$。在所有偏摩尔量中化学势地位特殊：它决定物质在相之间、在反应物与产物之间转移的方向（4.3.3）。

### 4.3.2. 组成可变系统的热力学基本方程

把 $G$ 看成 $T$、$p$、$n_1, \dots, n_k$ 的函数。组成不变时它满足 $\mathrm{d}G = -S\,\mathrm{d}T + V\,\mathrm{d}p$（[6.3.3](/6.3.3) 定理 3.2.1），所以 $(\partial G/\partial T)_{p,n} = -S$，$(\partial G/\partial p)_{T,n} = V$，于是

$$
\mathrm{d}G = -S\,\mathrm{d}T + V\,\mathrm{d}p + \sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}.
\tag{4.6}
$$
由 $U = G - pV + TS$、$H = G + TS$、$A = G - pV$ 取微分，代入式 (4.6) 得到另外三式：

**定理 4.3.1（组成可变系统的基本方程）** 只做体积功、各相内部 $T$、$p$ 均匀的系统中，

$$
\begin{aligned}
\mathrm{d}U &= T\,\mathrm{d}S - p\,\mathrm{d}V + \textstyle\sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}, &
\mathrm{d}H &= T\,\mathrm{d}S + V\,\mathrm{d}p + \textstyle\sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}, \\
\mathrm{d}A &= -S\,\mathrm{d}T - p\,\mathrm{d}V + \textstyle\sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}, &
\mathrm{d}G &= -S\,\mathrm{d}T + V\,\mathrm{d}p + \textstyle\sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}.
\end{aligned}
\tag{4.7}
$$
因而化学势有四种等价的表示：

$$
\mu_{\mathrm{B}} = \left(\frac{\partial G}{\partial n_{\mathrm{B}}}\right)_{T,p,n_{\mathrm{C}}} = \left(\frac{\partial U}{\partial n_{\mathrm{B}}}\right)_{S,V,n_{\mathrm{C}}} = \left(\frac{\partial H}{\partial n_{\mathrm{B}}}\right)_{S,p,n_{\mathrm{C}}} = \left(\frac{\partial A}{\partial n_{\mathrm{B}}}\right)_{T,V,n_{\mathrm{C}}}.
$$

后三种是"保持该函数的自然变量与其他组分的量不变"时的偏导数，它们都等于化学势，但都不是偏摩尔量；只有第一种同时是偏摩尔量。不加说明时，化学势指偏摩尔 Gibbs 自由能。

关于适用条件：式 (4.7) 适用于开放系统；对发生相变或化学反应的封闭系统，把每一相（或把反应混合物）看成组成可变的子系统，同样适用（"大封闭、小开放"）。它是相邻平衡态之间的恒等式，只要各相内部处于热平衡与力学平衡，相之间的物质转移、相内的化学反应是否可逆都不影响它成立；化学势之间的差别正是这些过程不可逆的根源。$\sum\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$ 这一项消除了 [6.3.3](/6.3.3) 中"基本方程只适用于可逆的化学变化"的限制：组成不变或化学势达到平衡（$\sum\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}} = 0$）时，式 (4.7) 回到组成不变的形式。

对 $U$ 用 Euler 定理（$U$ 是 $S$、$V$、$n_{\mathrm{B}}$ 的一次齐次函数）还得到 $U = TS - pV + \sum_{\mathrm{B}}n_{\mathrm{B}}\mu_{\mathrm{B}}$，即 $G = \sum_{\mathrm{B}}n_{\mathrm{B}}\mu_{\mathrm{B}}$；把它的微分与式 (4.7) 比较，得到 Gibbs–Duhem 方程的一般形式

$$
S\,\mathrm{d}T - V\,\mathrm{d}p + \sum_{\mathrm{B}}n_{\mathrm{B}}\,\mathrm{d}\mu_{\mathrm{B}} = 0.
\tag{4.8}
$$
它说明一个均相中 $T$、$p$、$\mu_1, \dots, \mu_k$ 这 $k + 2$ 个强度量只有 $k + 1$ 个是独立的，这是相律（[6.3.8](/6.3.8)）计数自由度的出发点。

**例 4.3.1** $\ce{H2}$ 与 $\ce{O2}$ 在绝热的刚性容器中反应生成水蒸气。过程中 $Q = 0$、$W = 0$，$\mathrm{d}U = 0$、$\mathrm{d}V = 0$。由式 (4.7)，

$$
T\,\mathrm{d}S = -\sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}} = -\Big(\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}}\Big)\mathrm{d}\xi > 0.
$$
没有热交换，系统的熵却增加：增加的熵完全由反应的不可逆性产生，$-\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}}$ 是反应的推动力（称为反应的**亲和势**）。若错误地套用组成不变的 $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V$，就会得出 $\mathrm{d}S = 0$。这里的 $-\sum\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}/T$ 就是 [6.3.18](/6.3.18) 中化学反应引起的熵产生。

### 4.3.3. 化学势判据

先看最简单的传质过程。在等温、等压、$W' = 0$ 的条件下，设 $\mathrm{d}n_{\mathrm{B}} > 0$ 的物质 B 由 $\alpha$ 相转移到 $\beta$ 相，而其他量都不变。由式 (4.6)，

$$
\mathrm{d}G = \mathrm{d}G^\alpha + \mathrm{d}G^\beta = -\mu_{\mathrm{B}}^\alpha\,\mathrm{d}n_{\mathrm{B}} + \mu_{\mathrm{B}}^\beta\,\mathrm{d}n_{\mathrm{B}} = (\mu_{\mathrm{B}}^\beta - \mu_{\mathrm{B}}^\alpha)\,\mathrm{d}n_{\mathrm{B}}.
$$
由 Gibbs 判据，$\mu_{\mathrm{B}}^\beta < \mu_{\mathrm{B}}^\alpha$ 时 $\mathrm{d}G < 0$，转移自发进行；$\mu_{\mathrm{B}}^\beta = \mu_{\mathrm{B}}^\alpha$ 时两相平衡；$\mu_{\mathrm{B}}^\beta > \mu_{\mathrm{B}}^\alpha$ 时只有逆过程能自发进行。物质总是自发地从化学势高处流向化学势低处，正如热从高温流向低温、气体从高压流向低压；化学势常被称为物质的"逃逸倾向"。

再看化学反应 $0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B}$。反应进度改变 $\mathrm{d}\xi$ 时 $\mathrm{d}n_{\mathrm{B}} = \nu_{\mathrm{B}}\,\mathrm{d}\xi$（**反应进度**、**化学计量数**见 [6.1.6](/6.1.6#sec-6.3.2)），等温等压下 $\mathrm{d}G = (\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}})\,\mathrm{d}\xi$。反应自发地向 $\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}\xi < 0$ 的方向进行，平衡时 $\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}} = 0$：产物一侧与反应物一侧的化学势（按化学计量数加权）相等。

在等温等容条件下用 $\mathrm{d}A$、在等熵等容或等熵等压条件下用 $\mathrm{d}U$、$\mathrm{d}H$，由式 (4.7) 得到同样的结论。

**定理 4.3.2（化学势判据）** 在 $W' = 0$ 且 $(T, p)$、$(T, V)$、$(S, V)$、$(S, p)$ 之一保持不变的条件下，系统内的传质过程（扩散、相变、化学反应）满足

$$
\sum_{\alpha}\sum_{\mathrm{B}}\mu_{\mathrm{B}}^\alpha\,\mathrm{d}n_{\mathrm{B}}^\alpha \le 0 \qquad (< 0 \text{ 自发},\ = 0 \text{ 平衡}),
$$
求和遍及所有相 $\alpha$ 与其中的物质 B。

若 $T$、$p$、$V$、$S$ 都在变化，还能用化学势判断吗？可以，但要回到熵判据。设孤立系统由 $\alpha$、$\beta$ 两部分组成，两者可以交换能量、体积和物质 B。由式 (4.7) 写出 $\mathrm{d}S = (\mathrm{d}U + p\,\mathrm{d}V - \sum\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}})/T$，并用 $\mathrm{d}U^\beta = -\mathrm{d}U^\alpha$、$\mathrm{d}V^\beta = -\mathrm{d}V^\alpha$、$\mathrm{d}n_{\mathrm{B}}^\beta = -\mathrm{d}n_{\mathrm{B}}^\alpha$：

$$
\mathrm{d}S = \left(\frac{1}{T^\alpha} - \frac{1}{T^\beta}\right)\mathrm{d}U^\alpha + \left(\frac{p^\alpha}{T^\alpha} - \frac{p^\beta}{T^\beta}\right)\mathrm{d}V^\alpha - \left(\frac{\mu_{\mathrm{B}}^\alpha}{T^\alpha} - \frac{\mu_{\mathrm{B}}^\beta}{T^\beta}\right)\mathrm{d}n_{\mathrm{B}}^\alpha.
$$
平衡时熵极大，三个独立变化的系数都必须为零：$T^\alpha = T^\beta$（热平衡），$p^\alpha = p^\beta$（力学平衡），$\mu_{\mathrm{B}}^\alpha = \mu_{\mathrm{B}}^\beta$（物质平衡）。两部分温度相等时，熵增加要求物质向 $\mu_{\mathrm{B}}$ 低的一侧转移，与定理 4.3.2 一致。若两部分之间是刚性的壁（如半透膜两侧压力不同），第二个条件不再出现，平衡时压力可以不等，这正是渗透压的来源（[6.3.5](/6.3.5)）。

总结：在 $W' = 0$ 时，化学势是一切传质过程的统一判据；平衡的条件是每种物质在它所存在的各相中化学势相等，以及每个独立反应的 $\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}} = 0$。这两条是后面处理相平衡与化学平衡的共同依据。生物膜两侧的物质输运也是这样：物质顺化学势（对离子则是电化学势，[6.3.13](/6.3.13)）梯度的被动扩散自发进行，逆梯度的主动运输必须与 ATP 水解这样 $\Delta G < 0$ 的过程耦合（[6.3.18](/6.3.18)）。

### 4.3.4. 化学势与温度、压力的关系

**定理 4.3.3** 组成不变时，

$$
\left(\frac{\partial\mu_{\mathrm{B}}}{\partial p}\right)_{T,n} = V_{\mathrm{B}}, \qquad \left(\frac{\partial\mu_{\mathrm{B}}}{\partial T}\right)_{p,n} = -S_{\mathrm{B}}, \qquad \left[\frac{\partial(\mu_{\mathrm{B}}/T)}{\partial T}\right]_{p,n} = -\frac{H_{\mathrm{B}}}{T^2}.
\tag{4.9}
$$

**证明** 由式 (4.6)，$\mathrm{d}G$ 是 $T$、$p$、$n_{\mathrm{B}}$ 的全微分，二阶混合偏导数与次序无关：

$$
\left(\frac{\partial\mu_{\mathrm{B}}}{\partial p}\right)_{T,n} = \frac{\partial^2 G}{\partial p\,\partial n_{\mathrm{B}}} = \left[\frac{\partial}{\partial n_{\mathrm{B}}}\left(\frac{\partial G}{\partial p}\right)_{T,n}\right]_{T,p,n_{\mathrm{C}}} = \left(\frac{\partial V}{\partial n_{\mathrm{B}}}\right)_{T,p,n_{\mathrm{C}}} = V_{\mathrm{B}}.
$$
第二式同理。第三式与 Gibbs–Helmholtz 方程的证明相同，用到 $\mu_{\mathrm{B}} = H_{\mathrm{B}} - TS_{\mathrm{B}}$。$\square$

与纯物质的关系对照（[6.3.3](/6.3.3) 3.4.4）：把纯物质关系中的摩尔量换成偏摩尔量，就得到混合物中组分 B 的关系。

| 纯物质 B | 混合物中的 B |
|---|---|
| $(\partial G^*_{\mathrm{m}}/\partial p)_T = V^*_{\mathrm{m}}$ | $(\partial\mu_{\mathrm{B}}/\partial p)_{T,n} = V_{\mathrm{B}}$ |
| $(\partial G^*_{\mathrm{m}}/\partial T)_p = -S^*_{\mathrm{m}}$ | $(\partial\mu_{\mathrm{B}}/\partial T)_{p,n} = -S_{\mathrm{B}}$ |
| $[\partial(G^*_{\mathrm{m}}/T)/\partial T]_p = -H^*_{\mathrm{m}}/T^2$ | $[\partial(\mu_{\mathrm{B}}/T)/\partial T]_{p,n} = -H_{\mathrm{B}}/T^2$ |
| $G^*_{\mathrm{m}} = H^*_{\mathrm{m}} - TS^*_{\mathrm{m}}$ | $\mu_{\mathrm{B}} = H_{\mathrm{B}} - TS_{\mathrm{B}}$ |

一般 $V_{\mathrm{B}} > 0$、$S_{\mathrm{B}} > 0$，所以加压使化学势升高，升温使化学势降低。对纯物质的各相，$-S_{\mathrm{m}}$ 是 $\mu^*$–$T$ 曲线的斜率，而 $S_{\mathrm{m}}(\mathrm{g}) > S_{\mathrm{m}}(\mathrm{l}) > S_{\mathrm{m}}(\mathrm{s})$，气相的线最陡、固相的线最平。在每个温度下化学势最低的相是稳定相，两条线的交点就是两相平衡的温度（熔点、沸点）；曲线都向下弯曲，因为 $(\partial^2\mu^*/\partial T^2)_p = -C_{p,\mathrm{m}}/T < 0$。加压使各线上移 $V_{\mathrm{m}}\Delta p$：气相上移最多，沸点因此升高；液态水的摩尔体积比冰小，加压时液相线上移得比固相线少，熔点降低（[6.3.8](/6.3.8)）。

![纯水各相的化学势随温度的变化（用 CRC 的熵与热容数据计算，零点取在熔点）。1 bar 下三条线的交点给出熔点与沸点；压力增至 10 bar 时只有气相线显著上移，沸点升至约 456 K（实测 453 K）。](./plots/mu-temperature.py)

**例 4.3.2** 记水的正常沸点为 $T_{\mathrm{b}}$（$373.12\,\mathrm{K}$）。比较下列状态下水的化学势：(1) $T_{\mathrm{b}}$、$101.325\,\mathrm{kPa}$ 的液态水与 (2) 同温同压的水蒸气；(3) $T_{\mathrm{b}}$、$202.65\,\mathrm{kPa}$ 的液态水与 (4) 同温同压的水蒸气；(5) $T_{\mathrm{b}} + 1\,\mathrm{K}$、$101.325\,\mathrm{kPa}$ 的液态水与 (6) 同温同压的水蒸气。

**解** $T_{\mathrm{b}}$、$101.325\,\mathrm{kPa}$ 下液态水与水蒸气两相平衡，$\mu_1 = \mu_2$。等温加压，$\mathrm{d}\mu^* = V^*_{\mathrm{m}}\,\mathrm{d}p$，而 $V^*_{\mathrm{m}}(\mathrm{g}) \gg V^*_{\mathrm{m}}(\mathrm{l})$，所以 $\mu_4 - \mu_2 > \mu_3 - \mu_1 > 0$，得 $\mu_3 < \mu_4$：高压下液态稳定。等压升温，$\mathrm{d}\mu^* = -S^*_{\mathrm{m}}\,\mathrm{d}T$，而 $S^*_{\mathrm{m}}(\mathrm{g}) > S^*_{\mathrm{m}}(\mathrm{l})$，化学势都降低，但蒸气降得多，$\mu_5 > \mu_6$：沸点以上气态稳定。$\square$

## 4.4. 气体的化学势

化学势的绝对值无法确定（它包含内能的零点），能确定的只是同一物质在不同状态之间的差值。因此为每种物质选定一个**标准态**（[6.1.6](/6.1.6#sec-6.3.3)），把任意状态的化学势写成"标准态的化学势 + 一个可计算的修正项"。

### 4.4.1. 纯理想气体

气体的标准态是温度为 $T$、压力为**标准压力** $p^\circ = 10^5\,\mathrm{Pa}$ 的纯理想气体，其化学势记作 $\mu^\circ_{\mathrm{B}}(T)$，称为标准化学势，只是温度的函数。纯理想气体等温时 $(\partial\mu^*_{\mathrm{B}}/\partial p)_T = V^*_{\mathrm{m}} = RT/p$，从 $p^\circ$ 积分到 $p$：

$$
\mu^*_{\mathrm{B}}(T, p) = \mu^\circ_{\mathrm{B}}(T) + RT\ln\frac{p}{p^\circ}.
\tag{4.10}
$$
$RT\ln(p/p^\circ)$ 是纯理想气体 B 在 $(T, p)$ 与在标准态的化学势之差。

### 4.4.2. 理想气体混合物

设想一个容器被只允许 B 透过的膜分成两部分：一边是温度 $T$、总压 $p$、组成 $x_{\mathrm{B}}$ 的理想气体混合物，另一边是纯 B。平衡时 B 在两边的化学势相等，而实验表明（对理想气体混合物也可以由分子间无相互作用推出）此时纯 B 一侧的压力等于混合物中 B 的**分压** $p_{\mathrm{B}} = px_{\mathrm{B}}$。由式 (4.10)，

$$
\mu_{\mathrm{B}}(T, p, x_{\mathrm{B}}) = \mu^\circ_{\mathrm{B}}(T) + RT\ln\frac{p_{\mathrm{B}}}{p^\circ} = \mu^*_{\mathrm{B}}(T, p) + RT\ln x_{\mathrm{B}}.
\tag{4.11}
$$
这里 $\mu^\circ_{\mathrm{B}}(T)$ 仍是纯 B 在 $T$、$p^\circ$ 下的标准化学势，$\mu^*_{\mathrm{B}}(T, p)$ 是纯 B 在混合物的温度与总压下的化学势。混合物中 B 的化学势比同温同压的纯 B 低 $RT\ln(1/x_{\mathrm{B}})$；这一降低是混合自发进行的原因。

**例 4.4.1** 用化学势求理想气体 A 与 B 等温等压混合的 $\Delta_{\mathrm{mix}}G$、$\Delta_{\mathrm{mix}}S$、$\Delta_{\mathrm{mix}}H$、$\Delta_{\mathrm{mix}}V$。

**解** 由加和公式与式 (4.11)，

$$
\Delta_{\mathrm{mix}}G = (n_{\mathrm{A}}\mu_{\mathrm{A}} + n_{\mathrm{B}}\mu_{\mathrm{B}}) - (n_{\mathrm{A}}\mu^*_{\mathrm{A}} + n_{\mathrm{B}}\mu^*_{\mathrm{B}}) = RT(n_{\mathrm{A}}\ln x_{\mathrm{A}} + n_{\mathrm{B}}\ln x_{\mathrm{B}}).
$$
对 $T$ 求偏导得**混合熵** $\Delta_{\mathrm{mix}}S = -(\partial\Delta_{\mathrm{mix}}G/\partial T)_{p,n} = -R(n_{\mathrm{A}}\ln x_{\mathrm{A}} + n_{\mathrm{B}}\ln x_{\mathrm{B}})$；对 $p$ 求偏导，$\Delta_{\mathrm{mix}}V = (\partial\Delta_{\mathrm{mix}}G/\partial p)_{T,n} = 0$（$x_{\mathrm{B}}$ 与 $p$ 无关）；$\Delta_{\mathrm{mix}}H = \Delta_{\mathrm{mix}}G + T\Delta_{\mathrm{mix}}S = 0$，$\Delta_{\mathrm{mix}}U = 0$。与 [6.3.2](/6.3.2) 由熵直接计算的结果相同。$\square$

理想气体等温等压混合不吸热、不放热、体积不变，推动它的完全是熵。同样形式的结果将出现在理想液态混合物中（[6.3.5](/6.3.5)）。

### 4.4.3. 实际气体：逸度与逸度因子

实际气体的 $V^*_{\mathrm{m}} \ne RT/p$，式 (4.10) 不再成立。实际气体的物态方程形式各异，而且没有一个是普遍适用的；如果直接用某个物态方程积分 $\mathrm{d}\mu^* = V^*_{\mathrm{m}}\,\mathrm{d}p$，化学势的表达式就随物态方程而变。Lewis（1901）的办法是保持式 (4.10) 的形式，把偏离理想的全部效应归入一个"校正压力"。

**定义 4.4.1** 纯实际气体 B 的化学势写成

$$
\mu^*_{\mathrm{B}}(T, p) = \mu^\circ_{\mathrm{B}}(T) + RT\ln\frac{f}{p^\circ}, \qquad \lim_{p\to 0}\frac{f}{p} = 1
\tag{4.12}
$$
时，具有压力量纲的量 $f$ 称为该气体的**逸度**；$\varphi = f/p$ 称为**逸度因子**，量纲一。

几点说明：

1. 标准态仍是 $T$、$p^\circ$ 下的纯理想气体，对实际气体它是一个假想态，而不是 $p^\circ$ 下的实际气体。$RT\ln(f/p^\circ)$ 是实际气体在 $(T, p)$ 与假想标准态的化学势之差。
2. 定义中的极限条件确定了 $f$ 的零点：压力趋于零时一切气体都趋于理想气体，$\varphi \to 1$。理想气体 $\varphi = 1$、$f = p$。
3. $\varphi$ 是 $T$、$p$ 与气体本性的函数，不是气体的特性常数；它刻画实际气体在热力学上偏离理想气体的程度。
4. 逸度被称为"校正压力"，但 $fV = nRT$ 一般不成立：$f$ 只在化学势的表达式中代替 $p$，并不满足理想气体的物态方程。

逸度因子与**压缩因子** $Z = pV_{\mathrm{m}}/(RT)$（[6.1.1](/6.1.1)）有确定的关系：

**定理 4.4.1** 纯实际气体在温度 $T$ 下的逸度因子为

$$
\ln\varphi = \int_0^p\frac{Z - 1}{p'}\,\mathrm{d}p'.
\tag{4.13}
$$

**证明** 等温时由式 (4.12)，$\mathrm{d}\mu^* = RT\,\mathrm{d}\ln f$，又 $\mathrm{d}\mu^* = V^*_{\mathrm{m}}\,\mathrm{d}p$。减去理想气体的 $RT\,\mathrm{d}\ln p = (RT/p)\,\mathrm{d}p$：

$$
RT\,\mathrm{d}\ln\frac{f}{p} = \left(V^*_{\mathrm{m}} - \frac{RT}{p}\right)\mathrm{d}p = RT\,\frac{Z - 1}{p}\,\mathrm{d}p.
$$
从 $p' \to 0$（$\ln\varphi \to 0$）积分到 $p$ 即得。$\square$

所以在吸引作用占优势、$Z < 1$ 的压力范围内 $\varphi < 1$，排斥作用占优势、$Z > 1$ 时 $\varphi$ 逐渐超过 1；$\ln\varphi$ 等于 $(Z - 1)/p$ 曲线下的面积（图解法）。求逸度的方法有三：用物态方程积分（解析或数值）；由实验的 $p$–$V$–$T$ 数据作图积分；以及对应状态法。

对 **van der Waals 方程**，式 (4.13) 可以积出。用**对比参量** $T_{\mathrm{r}} = T/T_{\mathrm{c}}$、$p_{\mathrm{r}} = p/p_{\mathrm{c}}$ 表示，记 $\mathcal{A} = 27p_{\mathrm{r}}/(64T_{\mathrm{r}}^2)$、$\mathcal{B} = p_{\mathrm{r}}/(8T_{\mathrm{r}})$，压缩因子是三次方程 $Z^3 - (1 + \mathcal{B})Z^2 + \mathcal{A}Z - \mathcal{A}\mathcal{B} = 0$ 的根，

$$
\ln\varphi = Z - 1 - \ln(Z - \mathcal{B}) - \frac{\mathcal{A}}{Z}.
$$
$\varphi$ 只依赖于 $T_{\mathrm{r}}$ 与 $p_{\mathrm{r}}$：这是**对应状态原理**（[6.3.1](/6.3.1)）在逸度上的体现。实用中，处于相同对比状态的不同气体有近似相同的逸度因子，可以由普遍化的逸度因子图（Newton 图）查得；vdW 方程给出的是这类图的定性形状，定量上它高估了吸引作用的影响。式 (4.13) 也可以直接数值积分（`scipy.integrate.quad`，[4.4.4](/4.4.4#sec-4.3.1)），两种算法结果一致：

```python
import numpy as np
from scipy.integrate import quad

def Z_vdw(pr, Tr):
    """Gas-like root of the reduced van der Waals cubic."""
    A, B = 27 * pr / (64 * Tr**2), pr / (8 * Tr)
    r = np.roots([1, -(1 + B), A, -A * B])
    return r[np.abs(r.imag) < 1e-9].real.max()

Tr, pr = 1.2, 1.0
ln_phi, _ = quad(lambda p: (Z_vdw(p, Tr) - 1) / p, 1e-12, pr)
print(np.exp(ln_phi))  # 0.816
```

![van der Waals 气体的逸度因子（左）与压缩因子（右）随对比压力的变化。$T_{\mathrm{r}}$ 低于 Boyle 温度（vdW 气体为 $27/8 = 3.375$）时，低压下吸引占优，$\varphi < 1$；高压下排斥占优，$\varphi$ 回升。](./plots/vdw-fugacity.py)

**例 4.4.2** 实际气体从 $p_1$ 等温变到 $p_2$，求 $\Delta G$；能否用 $\Delta S = nR\ln(f_1/f_2)$ 计算熵变？

**解** $\Delta G = n(\mu_2^* - \mu_1^*) = nRT\ln(f_2/f_1)$，这与理想气体的 $nRT\ln(p_2/p_1)$ 形式相同。但熵变不能照搬理想气体的 $\Delta S = -\Delta G/T$：那个关系依赖于 $\Delta H = 0$，而实际气体等温变压时 $\Delta H \ne 0$（[6.3.3](/6.3.3) 定理 3.4.1）。正确的做法是由 $S^*_{\mathrm{m}} = -(\partial\mu^*/\partial T)_p$，

$$
S^*_{\mathrm{m}}(T, p) = S^\circ_{\mathrm{m}}(T) - R\ln\frac{p}{p^\circ} - R\ln\varphi - RT\left(\frac{\partial\ln\varphi}{\partial T}\right)_p,
$$
其中最后一项来自 $\varphi$ 对温度的依赖。所以 $\Delta S = nR\ln(f_1/f_2)$ 是错的，除非 $\varphi$ 与温度无关。$\square$

### 4.4.4. 实际气体混合物与 Lewis–Randall 规则

实际气体混合物中组分 B 的化学势同样写成

$$
\mu_{\mathrm{B}} = \mu^\circ_{\mathrm{B}}(T) + RT\ln\frac{f_{\mathrm{B}}}{p^\circ}, \qquad f_{\mathrm{B}} = \varphi_{\mathrm{B}}p_{\mathrm{B}}, \qquad \lim_{p\to 0}\varphi_{\mathrm{B}} = 1,
\tag{4.14}
$$
$f_{\mathrm{B}}$、$\varphi_{\mathrm{B}}$ 是 B 在混合物中的逸度与逸度因子，$p_{\mathrm{B}} = px_{\mathrm{B}}$ 是分压，$\mu^\circ_{\mathrm{B}}$ 仍是纯 B 的理想气体在 $p^\circ$ 下的化学势。严格地，$\varphi_{\mathrm{B}}$ 依赖于混合物的组成，要由混合物的物态方程求出。缺少这类数据时用下面的近似。

**定义 4.4.2（Lewis–Randall 规则）** 近似

$$
f_{\mathrm{B}}(T, p, x_{\mathrm{B}}) = x_{\mathrm{B}}f^*_{\mathrm{B}}(T, p), \quad \text{即}\quad \varphi_{\mathrm{B}} = \varphi^*_{\mathrm{B}}(T, p)
$$
称为 **Lewis–Randall 规则**，其中 $f^*_{\mathrm{B}}$、$\varphi^*_{\mathrm{B}}$ 是纯 B 在混合物的温度与总压下的逸度与逸度因子。

这一规则相当于把混合物看作实际气体的理想混合物：它考虑了温度、压力与 B 本身的性质，却忽略了不同分子之间的相互作用与同种分子之间的差别。严格地说它只适用于分子大小与相互作用都相近的气体（如 $\ce{N2}$–$\ce{O2}$），或某一组分含量很高时的该组分；对极性差别大的混合物（如 $\ce{H2}$–$\ce{NH3}$）误差可观。

**例 4.4.3** 估计 $298\,\mathrm{K}$、$10^7\,\mathrm{Pa}$ 的空气中 $\ce{O2}$（$x = 0.21$）与 $\ce{N2}$（$x = 0.79$）的逸度。

**解** 由 Lewis–Randall 规则，$f(\ce{O2}) = 0.21\,f^*(\ce{O2}, 298\,\mathrm{K}, 10^7\,\mathrm{Pa})$。$\ce{O2}$ 的 $T_{\mathrm{c}} = 154.58\,\mathrm{K}$、$p_{\mathrm{c}} = 5.043\,\mathrm{MPa}$，对比状态为 $T_{\mathrm{r}} = 1.93$、$p_{\mathrm{r}} = 1.98$；vdW 对比方程给出 $\varphi^* \approx 0.91$，所以 $f(\ce{O2}) \approx 0.21 \times 0.91 \times 10\,\mathrm{MPa} = 1.9\,\mathrm{MPa}$。$\ce{N2}$ 的 $T_{\mathrm{c}} = 126.19\,\mathrm{K}$、$p_{\mathrm{c}} = 3.396\,\mathrm{MPa}$，$T_{\mathrm{r}} = 2.36$、$p_{\mathrm{r}} = 2.94$，$\varphi^* \approx 0.95$，$f(\ce{N2}) \approx 0.79 \times 0.95 \times 10\,\mathrm{MPa} = 7.5\,\mathrm{MPa}$。vdW 方程高估了偏离，精确的物态方程给出的 $\varphi^*$ 更接近 1；用普遍化逸度因子图得到的值也是如此。$\square$

## 小结

| 系统 | 化学势 | 标准态 |
|---|---|---|
| 纯理想气体 | $\mu^* = \mu^\circ(T) + RT\ln(p/p^\circ)$ | 纯理想气体，$T$、$p^\circ$ |
| 理想气体混合物 | $\mu_{\mathrm{B}} = \mu^\circ_{\mathrm{B}}(T) + RT\ln(p_{\mathrm{B}}/p^\circ) = \mu^*_{\mathrm{B}}(T, p) + RT\ln x_{\mathrm{B}}$ | 同上 |
| 纯实际气体 | $\mu^* = \mu^\circ(T) + RT\ln(f/p^\circ)$，$f = \varphi p$ | 同上（假想态） |
| 实际气体混合物 | $\mu_{\mathrm{B}} = \mu^\circ_{\mathrm{B}}(T) + RT\ln(f_{\mathrm{B}}/p^\circ)$，$f_{\mathrm{B}} = \varphi_{\mathrm{B}}p_{\mathrm{B}}$ | 同上（假想态） |

- 偏摩尔量 $X_{\mathrm{B}} = (\partial X/\partial n_{\mathrm{B}})_{T,p,n_{\mathrm{C}}}$ 是强度性质；加和公式 $X = \sum n_{\mathrm{B}}X_{\mathrm{B}}$ 描述一个状态，Gibbs–Duhem 方程 $\sum x_{\mathrm{B}}\,\mathrm{d}X_{\mathrm{B}} = 0$（$T$、$p$ 不变）约束组成变化。
- 化学势 $\mu_{\mathrm{B}} = G_{\mathrm{B}}$；组成可变时基本方程加上 $\sum\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$。在 $W' = 0$ 时，物质从高化学势流向低化学势；平衡时每种物质在各相中的化学势相等，每个反应的 $\sum\nu_{\mathrm{B}}\mu_{\mathrm{B}} = 0$。
- $(\partial\mu_{\mathrm{B}}/\partial p)_T = V_{\mathrm{B}}$，$(\partial\mu_{\mathrm{B}}/\partial T)_p = -S_{\mathrm{B}}$；纯物质各相 $\mu^*$–$T$ 曲线的交点是相变点。
- 逸度保留了理想气体化学势的形式，$\ln\varphi = \int_0^p (Z - 1)\,\mathrm{d}p/p$；液态混合物与溶液中组分的化学势将借助与之平衡的蒸气写出（[6.3.5](/6.3.5)）。
