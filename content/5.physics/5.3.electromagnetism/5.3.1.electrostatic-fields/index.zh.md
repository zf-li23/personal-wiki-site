---
title: 静电场
description: 电荷的基本性质、Coulomb 定律、电场强度与场强叠加原理、电偶极子与连续带电体的场、电场线与电通量、立体角与高斯定理的证明、用高斯定理求对称分布的场。
---

电磁学研究电荷与电流怎样产生电场和磁场、电磁场怎样作用于电荷与电流、电场与磁场怎样相互转化，以及电磁场与物质的相互作用。它与力学、热学的着眼点不同：力学追踪粒子的运动，热学用统计方法处理大量粒子的无规运动，电磁学的主角则是场——定义在空间每一点、随时间变化的矢量 $\boldsymbol{E}(\boldsymbol{r},t)$、$\boldsymbol{B}(\boldsymbol{r},t)$，带电粒子只是场的源。描述一个**向量场**有两个基本的整体量：穿过曲面的**通量**和沿闭合路径的**环量**，它们以及对应的局部量**散度**、**旋度**都已在 [2.2.13](/2.2.13)、[2.2.14](/2.2.14) 中讲过。电磁学的基本规律正是用这两种量写成的：本章的高斯定理讲静电场的通量，下一章 [5.3.2](/5.3.2) 的环路定理讲它的环量；两者合起来完全确定静电场，到 [5.3.10](/5.3.10) 推广为 Maxwell 方程组。

本章讨论真空中静止电荷产生的电场，即静电场。先给出电荷的基本性质与 Coulomb 定律，引入电场强度和场强叠加原理，计算电偶极子和几种连续带电体的场；然后引入电场线与电通量，证明高斯定理，并用它求对称分布电荷的场。之后的 [5.3.3](/5.3.3)、[5.3.4](/5.3.4) 分别讨论导体和电介质中的静电场。

## 1.1. 电荷

物体经摩擦等方式获得吸引轻小物体的性质，称为带了电。物质的这种属性称为电荷（electric charge），电荷的多少称为电荷量，SI 单位是库仑（$\mathrm{C}$）。电荷有以下四条基本性质。

### 1.1.1. 正电荷与负电荷

自然界只有两种电荷：同种电荷相互排斥，异种电荷相互吸引（Du Fay，1733 年）。按 Franklin 的约定，质子带正电，电子带负电。宏观物体通常含有等量的正负电荷而呈电中性，带电是正负电荷的数量失去平衡（多为电子的转移）的结果。

### 1.1.2. 电荷量子化

**性质 1.1.1（电荷量子化）** 任何带电体的电荷量都是一个基本单元的整数倍：

$$
q = Ne,\qquad N=0,\pm1,\pm2,\dots
$$

基本单元 $e$ 是质子所带的电荷量，称为元电荷（elementary charge），电子的电荷量为 $-e$。Millikan 用油滴实验（1909 年起）首先精确地证明了电荷量的变化是不连续的。自 2019 年起，SI 把元电荷的数值规定为精确值：

$$
e = 1.602\,176\,634\times10^{-19}\,\mathrm{C}.
$$

夸克带 $\pm\frac13e$、$\pm\frac23e$ 的分数电荷，但它们被禁闭在强子内部，没有观测到自由的夸克。由于 $e$ 极小，宏观电荷量可以看作连续变化的量，这是 §1.4 中引入电荷密度的依据。

### 1.1.3. 电荷守恒

**定理 1.1.1（电荷守恒定律）** 一个系统若没有净电荷出入其边界，则系统内正负电荷的代数和保持不变。

电荷守恒是迄今所知最精确的守恒律之一，在一切宏观和微观过程中都成立。电荷可以产生和消失，但总是成对地出现：高能光子在原子核附近转化为一对正负电子 $\gamma\to\mathrm{e}^-+\mathrm{e}^+$，正负电子相遇时又湮灭为光子，过程前后电荷的代数和都是零。更强的说法是局域守恒：一个区域内电荷的减少等于同一时间内穿过区域边界流出的电荷，电荷不能在一处消失而同时在远处出现。这一陈述的数学形式是电流连续性方程（[5.3.5](/5.3.5)）。

### 1.1.4. 电荷的相对论不变性

一个粒子的电荷量与它的运动状态无关：在不同的参考系中观测，同一电荷的运动状态不同，电荷量却相同。证据之一是原子与分子的电中性：氦原子核中两个质子的运动能量比氢分子中两个质子的大约 $10^6$ 倍，而两者都严格地呈电中性，说明质子的电荷量与它的速度无关。电荷不变性是用狭义相对论（[5.1.8](/5.1.8)）由电场导出磁场的出发点（[5.3.7](/5.3.7)）。

## 1.2. Coulomb 定律

**定理 1.2.1（Coulomb 定律）** 真空中两个静止的点电荷之间的相互作用力与它们电荷量的乘积成正比，与它们之间距离的平方成反比，方向沿两者的连线，同种电荷相斥，异种电荷相吸。点电荷 $q_1$ 对 $q_2$ 的作用力为

$$
\boldsymbol{F}_{21}=\frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r_{21}^2}\,\boldsymbol{e}_{21}=-\boldsymbol{F}_{12},
$$
其中 $r_{21}$ 是两者的距离，$\boldsymbol{e}_{21}$ 是由 $q_1$ 指向 $q_2$ 的单位矢量。

点电荷（point charge）是带电体的理想模型：带电体的线度远小于所讨论的距离时，它的形状和电荷分布可以忽略。式中的常量 $\varepsilon_0$ 称为真空介电常量（vacuum permittivity），也称真空电容率，

$$
\varepsilon_0 = 8.854\,187\,8188(14)\times10^{-12}\,\mathrm{F\,m^{-1}},\qquad k=\frac{1}{4\pi\varepsilon_0}\approx8.988\times10^{9}\,\mathrm{N\,m^2\,C^{-2}}.
$$
2019 年以前 $\varepsilon_0$ 由 $\mu_0$ 的规定值和 $c$ 导出，是精确值；现行 SI 中 $e$、$h$、$c$ 是精确值，$\varepsilon_0=e^2/(2\alpha hc)$ 要通过精细结构常数 $\alpha$ 的测量确定，相对不确定度约为 $10^{-10}$。把 $4\pi$ 写进 Coulomb 定律（称为有理化）的好处是：$4\pi$ 只出现在与球对称有关的公式中，更基本的方程（高斯定理、Maxwell 方程组）里不再出现它。

Coulomb 于 1785 年用扭秤得到这一定律；在此之前 Robison（1769 年）和 Cavendish（1773 年，未发表）已经得到同样的结论。把距离的指数写成 $2+\delta$，Cavendish 式的实验检验的是带电导体壳内是否有电场（见 [5.3.3](/5.3.3)），现代实验（Williams 等，1971 年）在约 $10^{-16}$ 的精度内测得 $\delta=0$。在原子和原子核的尺度上，平方反比律仍然成立。

Coulomb 定律的适用条件：一是点电荷；二是施力电荷相对观测者静止，受力电荷可以运动。运动电荷之间的作用力还包含磁力（[5.3.6](/5.3.6)），而且不再满足 **Newton 第三定律**，守恒的是电荷与电磁场的总动量。

实验还表明，两个点电荷之间的作用力不因第三个电荷的存在而改变，这称为电力叠加原理。因此 $n$ 个点电荷 $q_1,\dots,q_n$ 对点电荷 $q_0$ 的合力是各个电荷单独作用的力的矢量和：

$$
\boldsymbol{F}=\sum_{i=1}^n\frac{1}{4\pi\varepsilon_0}\frac{q_iq_0}{r_i^2}\,\boldsymbol{e}_{r_i}.
$$
叠加原理是一条实验规律，它说明静电学的方程是线性的（**叠加原理**），Coulomb 定律加上叠加原理就完备地描述了静电相互作用。

**例 1.2.1（电力与万有引力的比较）** Coulomb 定律与万有引力定律都是平方反比律。氢原子中电子与质子之间的电力与引力之比为

$$
\frac{F_{\mathrm{e}}}{F_{\mathrm{g}}}=\frac{e^2}{4\pi\varepsilon_0Gm_{\mathrm{e}}m_{\mathrm{p}}}\approx\frac{2.31\times10^{-28}\,\mathrm{J\,m}}{1.02\times10^{-67}\,\mathrm{J\,m}}\approx2.3\times10^{39},
$$
与距离无关。原子、分子乃至宏观物体之间的弹力、摩擦力都来源于电磁相互作用（[5.1.2](/5.1.2)）；引力之所以支配天体，是因为宏观物体的正负电荷几乎完全抵消，而引力只有吸引。

## 1.3. 电场和电场强度

### 1.3.1. 电场

Coulomb 力是怎样跨越空间传递的？一种观点是超距作用：相隔一定距离的两个物体直接、瞬时地相互作用，不需要媒介，也不需要时间。Faraday 提出另一种观点：电荷在周围空间激发电场（electric field），电场再对处在其中的其他电荷施加作用力，即"电荷—电场—电荷"的近距作用。对静止电荷，两种观点给出同样的结果；电荷运动或变化时，扰动以光速 $c$ 在场中传播（[5.3.10](/5.3.10)），只有场的观点与实验相符。引力也是如此：2015 年 LIGO 直接探测到以光速传播的引力波（2017 年获诺贝尔物理学奖）。

场的观点有两层含义。一是局域性：只要知道某个小区域内的电场，就能确定电荷在这里的受力，无需关心产生电场的电荷在哪里。二是物质性：电场和实物一样具有能量（[5.3.2](/5.3.2)）和动量（光压，[5.3.10](/5.3.10)），只是它不由原子、分子构成，而且可以叠加，几个场可以同时占据同一空间。

### 1.3.2. 电场强度

**定义 1.3.1（电场强度）** 设静止的**检验电荷** $q_0$ 在电场中某点受到电场力 $\boldsymbol{F}$，该点的**电场强度**（简称场强）为

$$
\boldsymbol{E}=\frac{\boldsymbol{F}}{q_0}.
$$
检验电荷的电荷量要充分小，以免改变原有的电荷分布；线度要足够小，使它能代表一个点。

电场中某点的场强等于单位正电荷在该点所受的电场力，与检验电荷无关，是电场本身的性质。场强的 SI 单位是 $\mathrm{N\,C^{-1}}$，也写作 $\mathrm{V\,m^{-1}}$（[5.3.2](/5.3.2)）。反过来，电荷 $q$ 在场强为 $\boldsymbol{E}$ 处受的电场力为 $\boldsymbol{F}=q\boldsymbol{E}$。一些典型的场强：空气的击穿场强约 $3\times10^6\,\mathrm{V\,m^{-1}}$，地表晴天的大气电场约 $10^2\,\mathrm{V\,m^{-1}}$，氢原子中电子所在处的场强约 $5\times10^{11}\,\mathrm{V\,m^{-1}}$。

## 1.4. 点电荷电场及叠加原理

### 1.4.1. 点电荷的场强

由 Coulomb 定律和场强的定义，静止的点电荷 $q$（源电荷）在场点 $P$ 产生的场强为

$$
\boldsymbol{E}=\frac{q}{4\pi\varepsilon_0r^2}\,\boldsymbol{e}_r,
$$
其中 $r$ 是 $q$ 到 $P$ 的距离，$\boldsymbol{e}_r$ 是由 $q$ 指向 $P$ 的单位矢量。点电荷的场是球对称的，大小与 $r^2$ 成反比；$q>0$ 时沿径向向外，$q<0$ 时向内。

### 1.4.2. 场强叠加原理

**性质 1.4.1（场强叠加原理）** 点电荷系在某点产生的场强，等于各个点电荷单独存在时在该点产生的场强的矢量和：

$$
\boldsymbol{E}=\sum_i\boldsymbol{E}_i=\sum_i\frac{q_i}{4\pi\varepsilon_0r_i^2}\,\boldsymbol{e}_{r_i}.
$$

它由电力叠加原理和场强的定义直接得到。对连续分布的电荷，把带电体分成许多电荷元，求和变为积分。

**定义 1.4.1（电荷密度）** 电荷连续分布在体积、曲面或曲线上时，把电荷元写成 $\mathrm{d}q=\rho\,\mathrm{d}V$、$\mathrm{d}q=\sigma\,\mathrm{d}S$ 或 $\mathrm{d}q=\lambda\,\mathrm{d}l$，$\rho$、$\sigma$、$\lambda$ 分别称为体、面、线**电荷密度**。带电体在 $P$ 点的场强为

$$
\boldsymbol{E}=\int_q\mathrm{d}\boldsymbol{E}=\int_q\frac{\mathrm{d}q}{4\pi\varepsilon_0r^2}\,\boldsymbol{e}_r .
$$

这是一个矢量积分：要先把 $\mathrm{d}\boldsymbol{E}$ 分解成分量，利用对称性判断哪些分量相互抵消，再对剩下的分量积分。面电荷和线电荷是带电层或带电细线厚度趋于零的模型，在它们上面场强会出现跃变或发散（§1.7）。

### 1.4.3. 电偶极子

**定义 1.4.2（电偶极子）** 一对相距很近的等量异号点电荷 $+q$、$-q$ 组成的电荷系称为**电偶极子**。设 $\boldsymbol{l}$ 是由 $-q$ 指向 $+q$ 的位矢，称

$$
\boldsymbol{p}=q\boldsymbol{l}
$$
为它的**电偶极矩**，单位 $\mathrm{C\,m}$。电偶极子的概念用于场点到电偶极子的距离 $r\gg l$ 的情形。

有极分子（如 $\ce{H2O}$，$p\approx6.2\times10^{-30}\,\mathrm{C\,m}$）的正负电荷中心不重合，在远处看就是电偶极子；电介质的极化（[5.3.4](/5.3.4)）和天线辐射（[5.3.10](/5.3.10)）都要用到它。

**例 1.4.1（电偶极子轴线上的场强）** 取电偶极子中点为原点，场点 $P$ 在轴线上、位于 $+q$ 一侧，距中点 $r$。两个电荷的场都沿轴线，

$$
\boldsymbol{E}=\frac{q\boldsymbol{e}_l}{4\pi\varepsilon_0}\Big[\frac{1}{(r-l/2)^2}-\frac{1}{(r+l/2)^2}\Big]=\frac{q\boldsymbol{e}_l}{4\pi\varepsilon_0}\frac{2rl}{(r^2-l^2/4)^2},
$$
其中 $\boldsymbol{e}_l=\boldsymbol{l}/l$。当 $r\gg l$ 时

$$
\boldsymbol{E}\approx\frac{2\boldsymbol{p}}{4\pi\varepsilon_0r^3}.
$$

**例 1.4.2（电偶极子中垂面上的场强）** 场点在中垂面上、距中点 $r$。两个电荷的场强大小都是 $\frac{q}{4\pi\varepsilon_0(r^2+l^2/4)}$，垂直于轴线的分量抵消，沿轴线的分量相加，方向与 $\boldsymbol{p}$ 相反：

$$
\boldsymbol{E}=-\frac{\boldsymbol{p}}{4\pi\varepsilon_0(r^2+l^2/4)^{3/2}}\approx-\frac{\boldsymbol{p}}{4\pi\varepsilon_0r^3}\quad(r\gg l).
$$

一般位置的场强可以把 $\boldsymbol{p}$ 分解为沿 $\boldsymbol{e}_r$ 的分量 $p\cos\theta$ 与垂直于 $\boldsymbol{e}_r$ 的分量 $p\sin\theta$（$\theta$ 是 $\boldsymbol{r}$ 与 $\boldsymbol{p}$ 的夹角），场点分别位于这两个"分偶极子"的轴线和中垂面上，由例 1.4.1 与例 1.4.2 叠加，得到下面的公式。

**公式 1.4.1（电偶极子的场强）**

$$
\boldsymbol{E}=\frac{1}{4\pi\varepsilon_0r^3}\big[3(\boldsymbol{p}\cdot\boldsymbol{e}_r)\boldsymbol{e}_r-\boldsymbol{p}\big],\qquad E_r=\frac{2p\cos\theta}{4\pi\varepsilon_0r^3},\quad E_\theta=\frac{p\sin\theta}{4\pi\varepsilon_0r^3}\qquad(r\gg l).
$$

电偶极子的场与 $r^3$ 成反比，比点电荷的场衰减得快：远处看去，$+q$ 与 $-q$ 的场几乎抵消。场只通过乘积 $p=ql$ 依赖于 $q$ 和 $l$，所以电偶极矩是描述电偶极子的唯一参量。[5.3.2](/5.3.2) 中将由电势更简单地导出公式 1.4.1。

**例 1.4.3（均匀外电场中电偶极子受的力矩）** 电偶极子放在均匀电场 $\boldsymbol{E}$ 中，$+q$、$-q$ 受力 $\pm q\boldsymbol{E}$，合力为零，但构成力偶。以中点为参考点，设 $\boldsymbol{r}_\pm=\pm\boldsymbol{l}/2$，力矩为

$$
\boldsymbol{M}=\boldsymbol{r}_+\times q\boldsymbol{E}+\boldsymbol{r}_-\times(-q\boldsymbol{E})=q\boldsymbol{l}\times\boldsymbol{E}=\boldsymbol{p}\times\boldsymbol{E},\qquad M=pE\sin\theta .
$$
力矩使 $\boldsymbol{p}$ 转向外电场的方向；$\boldsymbol{p}$ 与 $\boldsymbol{E}$ 同向时是稳定平衡。在非均匀电场中，电偶极子除受力矩外还受合力 $\boldsymbol{F}=(\boldsymbol{p}\cdot\nabla)\boldsymbol{E}$，被拉向场强较大处，这就是带电体吸引轻小物体的原因：轻小物体被极化成电偶极子，再被非均匀电场吸引。

### 1.4.4. 任意电荷系在远处的场

场点到电荷系的距离 $r$ 远大于电荷系的线度时，在电荷系内任取一点为原点 $O$，场的主要部分依次是：

- 若总电荷 $Q=\sum q_i\ne0$，场近似为位于 $O$ 的点电荷 $Q$ 的场，$E\propto r^{-2}$；
- 若 $Q=0$ 而电偶极矩 $\boldsymbol{p}=\sum q_i\boldsymbol{r}_i\ne\boldsymbol{0}$（此时 $\boldsymbol{p}$ 与原点的选取无关），场以电偶极子的场为主，$E\propto r^{-3}$；
- 若 $\boldsymbol{p}$ 也为零，再看电四极矩，$E\propto r^{-4}$，依此类推。

这就是多极展开。它的数学基础是 $\frac{1}{\lvert\boldsymbol{r}-\boldsymbol{r}'\rvert}=\sum_{l\ge0}\frac{r'^l}{r^{l+1}}P_l(\cos\gamma)$（$r'<r$，$\gamma$ 是 $\boldsymbol{r}$ 与 $\boldsymbol{r}'$ 的夹角），右端的系数正是 **Legendre 多项式** $P_l$（[2.5.5](/2.5.5)）。

### 1.4.5. 连续带电体的场

**例 1.4.4（均匀带电圆环面轴线上的场强）** 圆环面（内半径 $R_1$、外半径 $R_2$）均匀带电，面电荷密度为 $\sigma$。求轴线上距环心 $x$ 处的场强。

取半径 $r_\perp$、宽 $\mathrm{d}r_\perp$、张角 $\mathrm{d}\phi$ 的电荷元 $\mathrm{d}q=\sigma r_\perp\,\mathrm{d}r_\perp\,\mathrm{d}\phi$。由对称性，各电荷元的场垂直于轴线的分量两两抵消，只剩沿轴线（$x$ 方向）的分量 $\mathrm{d}E_x=\frac{\mathrm{d}q}{4\pi\varepsilon_0r^2}\cos\theta$，其中 $r^2=x^2+r_\perp^2$，$\cos\theta=x/r$。所以

$$
E_x=\int_0^{2\pi}\!\!\int_{R_1}^{R_2}\frac{\sigma x\,r_\perp\,\mathrm{d}r_\perp\,\mathrm{d}\phi}{4\pi\varepsilon_0(x^2+r_\perp^2)^{3/2}}=\frac{\sigma x}{2\varepsilon_0}\Big[\frac{1}{\sqrt{x^2+R_1^2}}-\frac{1}{\sqrt{x^2+R_2^2}}\Big].
$$

检验结果：量纲正确；$x=0$ 处 $E=0$，符合对称性；当 $\lvert x\rvert\gg R_2$ 时，由 $\frac{1}{\sqrt{x^2+R^2}}\approx\frac{1}{\lvert x\rvert}\big(1-\frac{R^2}{2x^2}\big)$ 得

$$
E_x\approx\frac{\sigma(R_2^2-R_1^2)}{4\varepsilon_0x^2}\cdot\frac{x}{\lvert x\rvert}=\frac{q}{4\pi\varepsilon_0x^2}\cdot\frac{x}{\lvert x\rvert},\qquad q=\sigma\pi(R_2^2-R_1^2),
$$
即远处看去是点电荷。两个特殊情形：

1. 均匀带电圆盘（$R_1\to0$，$R_2=R$）：$E_x=\dfrac{\sigma}{2\varepsilon_0}\Big[\dfrac{x}{\lvert x\rvert}-\dfrac{x}{\sqrt{x^2+R^2}}\Big]$，在盘面两侧 $x\to0^\pm$ 处趋于 $\pm\frac{\sigma}{2\varepsilon_0}$，跃变量为 $\sigma/\varepsilon_0$。
2. 无限大均匀带电平面（$R_1\to0$，$R_2\to\infty$）：

$$
\boldsymbol{E}=\frac{\sigma}{2\varepsilon_0}\,\boldsymbol{e}_{\mathrm{n}},
$$
大小处处相同，方向垂直于平面，两侧相反（$\boldsymbol{e}_{\mathrm{n}}$ 是由平面指向场点一侧的单位法向量）。这一结果在 §1.7 中将用高斯定理更简单地得到。

## 1.5. 电场线和电通量

### 1.5.1. 电场线

**定义 1.5.1（电场线）** 在电场中画一族有向曲线，使曲线上每一点的切线方向都是该点场强的方向，曲线的疏密表示场强的大小：通过垂直于场强的单位面积的曲线条数等于该处场强的大小，

$$
E=\frac{\mathrm{d}N}{\mathrm{d}S_\perp},
$$
这族曲线称为**电场线**。

电场线是描述场的几何工具，不是真实存在的线（它就是**向量场**的积分曲线）。静电场的电场线有以下性质：起于正电荷（或无穷远），止于负电荷（或无穷远），在没有电荷处不中断；任意两条电场线不相交，因为每一点的场强只有一个方向；电场线不闭合（[5.3.2](/5.3.2) 证明）。电场线一般也不是带电粒子的运动轨迹：电场力决定的是加速度而不是速度的方向，只有在电场线是直线、粒子由静止释放等特殊情形下两者才重合。

![电场线。左：电偶极子，电场线由正电荷出发、终止于负电荷；右：两个等量正电荷，电场线都伸向无穷远，两电荷连线的中点处场强为零，电场线在那里分开](./plots/field-lines.py)

### 1.5.2. 电通量

**定义 1.5.2（电通量）** 穿过曲面 $S$ 的电场线的条数称为通过该面的**电通量**：

$$
\Phi_{\mathrm{e}}=\iint_S\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S},\qquad\mathrm{d}\Phi_{\mathrm{e}}=\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}=E\cos\theta\,\mathrm{d}S=E\,\mathrm{d}S_\perp=\mathrm{d}N,
$$
其中 $\mathrm{d}\boldsymbol{S}=\boldsymbol{e}_{\mathrm{n}}\,\mathrm{d}S$ 是有向面元，$\theta$ 是 $\boldsymbol{E}$ 与面元法向的夹角。对闭合曲面约定外法线方向为正，记作 $\Phi_{\mathrm{e}}=\oiint_S\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}$。

电通量就是电场的**通量**，数学上是一个**第二型曲面积分**（[2.2.13](/2.2.13)）。它是对一个曲面而言的，不是点的函数；它是代数量，有正有负，对闭合曲面而言，$\Phi_{\mathrm{e}}>0$ 表示净穿出的电场线，$\Phi_{\mathrm{e}}<0$ 表示净穿入的电场线。

## 1.6. 高斯定理

### 1.6.1. 立体角

**定义 1.6.1（立体角）** 设 $\mathrm{d}\boldsymbol{S}$ 是距点 $O$ 为 $r$ 处的有向面元（线度远小于 $r$），$\boldsymbol{e}_r$ 是由 $O$ 指向面元的单位矢量。面元对 $O$ 所张的**立体角**为

$$
\mathrm{d}\Omega=\frac{\mathrm{d}\boldsymbol{S}\cdot\boldsymbol{e}_r}{r^2}=\frac{\mathrm{d}S\cos\theta}{r^2}=\frac{\mathrm{d}S_\perp}{r^2},
$$
即面元在以 $O$ 为球心的单位球面上的投影面积，单位是球面度（$\mathrm{sr}$），量纲为一。

立体角是平面角在三维中的推广。由定义，$\mathrm{d}\Omega$ 只取决于面元从 $O$ 看去的"视面积"，与面元的远近和倾斜无关；它也带有正负号。对闭合曲面 $S$（外法线为正）：

- $O$ 在 $S$ 内时，$S$ 上的面元与以 $O$ 为球心的小球面 $S_0$（半径 $r_0$）上的面元按射线一一对应，$\mathrm{d}\Omega$ 相同，所以 $\Omega=\oiint_S\frac{\mathrm{d}\boldsymbol{S}\cdot\boldsymbol{e}_r}{r^2}=\frac{1}{r_0^2}\oiint_{S_0}\mathrm{d}S_0=4\pi$。
- $O$ 在 $S$ 外时，从 $O$ 出发的每个小锥体与 $S$ 相交偶数次，一次穿入、一次穿出，两处 $\mathrm{d}\Omega$ 大小相等、符号相反，所以 $\Omega=0$。

这两条就是 [例 14.2.6](/2.2.14#ex-14.2.6) 中 $\boldsymbol{e}_r/r^2$ 通过闭曲面的通量为 $4\pi$ 或 $0$ 的几何解释。

### 1.6.2. 高斯定理

**定理 1.6.1（高斯定理）** 在静电场中，通过任意闭合曲面 $S$ 的电通量等于该曲面所包围的电荷量的代数和除以 $\varepsilon_0$：

$$
\oiint_S\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}=\frac{q_{\mathrm{enc}}}{\varepsilon_0}=\frac{1}{\varepsilon_0}\iiint_V\rho\,\mathrm{d}V,
$$
其中 $V$ 是 $S$ 所围的区域。闭合曲面 $S$ 常称为高斯面。

**证明** 分四步。

1. 点电荷 $q$、以 $q$ 为球心的球面 $S_0$：场强处处沿外法向、大小相同，$\Phi_{\mathrm{e}}=\frac{q}{4\pi\varepsilon_0r^2}\cdot4\pi r^2=\frac{q}{\varepsilon_0}$，与半径 $r$ 无关。这说明点电荷的电场线在空间中连续不断。
2. 点电荷 $q$、任意闭合曲面 $S$：$\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}=\frac{q}{4\pi\varepsilon_0}\frac{\boldsymbol{e}_r\cdot\mathrm{d}\boldsymbol{S}}{r^2}=\frac{q}{4\pi\varepsilon_0}\mathrm{d}\Omega$，由立体角的结论，$\Phi_{\mathrm{e}}=q/\varepsilon_0$（$q$ 在 $S$ 内）或 $0$（$q$ 在 $S$ 外）。
3. 点电荷系：由场强叠加原理，$\Phi_{\mathrm{e}}=\sum_i\oiint_S\boldsymbol{E}_i\cdot\mathrm{d}\boldsymbol{S}$，$S$ 外的电荷贡献为零，$S$ 内的电荷各贡献 $q_i/\varepsilon_0$，所以 $\Phi_{\mathrm{e}}=\sum_{\text{inside}}q_i/\varepsilon_0=q_{\mathrm{enc}}/\varepsilon_0$。
4. 连续分布的电荷：把带电体分成电荷元，第 3 步的和变为积分 $\frac{1}{\varepsilon_0}\iiint_V\rho\,\mathrm{d}V$。$\square$

**定理 1.6.2（高斯定理的微分形式）** 在电荷密度 $\rho$ 连续的地方，

$$
\nabla\cdot\boldsymbol{E}=\frac{\rho}{\varepsilon_0}.
$$

**证明** 由 **Gauss 公式**（[定理 14.2.1](/2.2.14#thm-14.2.1)），$\oiint_S\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}=\iiint_V\nabla\cdot\boldsymbol{E}\,\mathrm{d}V$。它对任意区域 $V$ 都等于 $\frac{1}{\varepsilon_0}\iiint_V\rho\,\mathrm{d}V$，被积函数连续，所以两者处处相等。$\square$

式中的 $\nabla$ 是 **Hamilton 算子**。按 [定理 14.2.2](/2.2.14#thm-14.2.2) 的解释，**散度**是单位体积向外的通量，所以微分形式说：静电场的源头就是电荷密度不为零的点。对点电荷，$\nabla\cdot\frac{\boldsymbol{e}_r}{r^2}=4\pi\delta(\boldsymbol{r})$，即点电荷的电荷密度是 **δ 函数** $q\,\delta(\boldsymbol{r})$。

关于高斯定理的几点说明：

- 高斯定理是平方反比律（加上叠加原理）的必然结果：证明的第 1 步用到了场强与 $r^2$ 成反比。若 Coulomb 定律的指数不是 2，第 1 步的通量就会依赖于 $r$，定理不再成立。万有引力也是平方反比律，所以引力场有同样形式的高斯定理（[例 14.5.1](/2.2.14#ex-14.5.1)）。
- 通量只由高斯面内电荷的代数和决定，与面内电荷怎样分布无关，也与面外的电荷无关；但式中的 $\boldsymbol{E}$ 是所有电荷（面内与面外）产生的总场强。
- 高斯面是几何面，面内、面外的电荷总能分清；电荷恰好分布在高斯面上时，应稍微移动高斯面。
- 高斯定理对运动电荷与变化的电场也成立，是 Maxwell 方程组之一（[5.3.10](/5.3.10)）；Coulomb 定律只适用于静止的电荷。在这个意义上，高斯定理由 Coulomb 定律导出，却比它更普遍。

高斯定理表明静电场是有源场：电荷是静电场的源，电场线发于正电荷、止于负电荷；在有电场而无电荷的区域，$\nabla\cdot\boldsymbol{E}=0$，电场线连续不断。高斯定理只说明了静电场的一半性质，另一半——静电场的电场线不闭合——是 [5.3.2](/5.3.2) 的环路定理。

## 1.7. 高斯定理应用举例

当电荷分布具有足够高的对称性时，可以选取适当的高斯面，把 $\boldsymbol{E}$ 从积分中提出来，直接由高斯定理求出场强。常见的对称性有三类：

| 对称性 | 带电体 | 高斯面 |
|---|---|---|
| 球对称 | 均匀带电的球体、球壳、球面（点电荷） | 同心球面 |
| 轴对称 | 无限长均匀带电的圆柱体、圆柱面、直线 | 同轴圆柱面 |
| 面对称 | 无限大均匀带电的平板、平面 | 垂直于平面的柱面 |

**例 1.7.1（均匀带电球壳）** 球壳内半径 $R_1$、外半径 $R_2$，均匀带电，体电荷密度 $\rho$，总电荷 $q=\frac{4\pi}{3}\rho(R_2^3-R_1^3)$。求场强分布。

先分析对称性。对任一场点 $P$，可以把电荷元关于直线 $OP$ 成对地选取，它们的场合成后沿 $OP$ 方向；电荷分布绕球心任意转动不变，所以 $\boldsymbol{E}=E(r)\boldsymbol{e}_r$。取半径为 $r$ 的同心球面为高斯面，$\oiint_S\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}=4\pi r^2E(r)=q_{\mathrm{enc}}/\varepsilon_0$，所以

$$
E(r)=\frac{q_{\mathrm{enc}}}{4\pi\varepsilon_0r^2}=\begin{cases}0,&r<R_1,\\[1mm]\dfrac{\rho}{3\varepsilon_0}\Big(r-\dfrac{R_1^3}{r^2}\Big),&R_1<r<R_2,\\[3mm]\dfrac{q}{4\pi\varepsilon_0r^2},&r>R_2.\end{cases}
$$
球壳外的场与全部电荷集中在球心的点电荷的场相同；空腔中的场为零。两种特殊情形：

1. 均匀带电球体（$R_1=0$，总电荷 $Q$，半径 $R$）：球内 $\boldsymbol{E}=\dfrac{\rho\boldsymbol{r}}{3\varepsilon_0}=\dfrac{Q\boldsymbol{r}}{4\pi\varepsilon_0R^3}$，与 $r$ 成正比；球外同点电荷。
2. 均匀带电球面（$R_1=R_2=R$，$q$ 不变）：球面内 $E=0$，球面外同点电荷。在 $r=R$ 处场强从 $0$ 跃变到 $\frac{q}{4\pi\varepsilon_0R^2}=\frac{\sigma}{\varepsilon_0}$。跃变是忽略电荷层厚度的结果。一般地，穿过面电荷密度为 $\sigma$ 的带电面，场强的法向分量跃变 $\sigma/\varepsilon_0$（对跨过带电面的扁柱形高斯面用高斯定理即得）。

![均匀带电球体、球壳与球面（总电荷 Q 相同、外半径 R₂ 相同）的场强 E(r)。三者在外部都与球心处的点电荷 Q 的场（虚线）相同；球体内部 E 与 r 成正比，球面在 r = R₂ 处跃变](./plots/sphere-fields.py)

**例 1.7.2（无限长均匀带电直线）** 线电荷密度为 $\lambda$。由轴对称性，$\boldsymbol{E}=E(r)\boldsymbol{e}_r$，$\boldsymbol{e}_r$ 垂直于直线向外。取半径 $r$、长 $l$ 的同轴圆柱面为高斯面：两个底面上 $\boldsymbol{E}\perp\mathrm{d}\boldsymbol{S}$，通量为零；侧面上 $\boldsymbol{E}$ 与 $\mathrm{d}\boldsymbol{S}$ 同向且大小相同，通量为 $E\cdot2\pi rl$。由高斯定理 $E\cdot2\pi rl=\lambda l/\varepsilon_0$，

$$
\boldsymbol{E}=\frac{\lambda}{2\pi\varepsilon_0r}\,\boldsymbol{e}_r .
$$
场强与 $r$ 成反比。$r\to0$ 时 $E\to\infty$，这表明在离导线很近处，带电直线的几何模型失效，必须考虑导线的粗细。

**例 1.7.3（无限大均匀带电平面）** 面电荷密度为 $\sigma$。由面对称性，场强垂直于平面，两侧对称处大小相等、方向相反。取轴线垂直于平面、两底面（面积 $\Delta S$）对称地位于平面两侧的柱面为高斯面，侧面通量为零，$2E\Delta S=\sigma\Delta S/\varepsilon_0$，所以 $E=\frac{\sigma}{2\varepsilon_0}$，与例 1.4.4 的结果一致。两个平行的无限大平面分别带 $+\sigma$、$-\sigma$ 时，由场强叠加原理，两平面之间 $E=\frac{\sigma}{2\varepsilon_0}+\frac{\sigma}{2\varepsilon_0}=\frac{\sigma}{\varepsilon_0}$，方向由正指向负；两平面外侧场强为零。这正是平行板电容器的场（[5.3.4](/5.3.4)）。

用高斯定理求场强的步骤：

1. 分析电荷分布的对称性，确定场强的方向和它依赖于哪个坐标。
2. 选取高斯面：要求场点在高斯面上；在待求场强的部分，$\boldsymbol{E}$ 与 $\mathrm{d}\boldsymbol{S}$ 平行且大小相同，使 $\oiint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}=E\oiint\mathrm{d}S$；在其余部分 $\boldsymbol{E}=\boldsymbol{0}$ 或 $\boldsymbol{E}\perp\mathrm{d}\boldsymbol{S}$。
3. 由高斯定理求出场强分布。
4. 对称性不够时（如有限长带电直线、带电圆盘），高斯定理仍然成立，但不能单独用它求场强，要回到叠加原理。

## 小结

- 电荷：电荷量子化 $q = Ne$（性质 1.1.1），电荷守恒（定理 1.1.1），电荷量是相对论不变量。
- Coulomb 定律（定理 1.2.1）$\boldsymbol{F}_{21} = \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r_{21}^2}\boldsymbol{e}_{21}$ 与叠加原理是静电学的两条实验基础。
- 场强 $\boldsymbol{E} = \boldsymbol{F}/q_0$（定义 1.3.1）是电场本身的性质；计算场强的三条途径：

| 方法 | 适用情形 | 例子 |
|---|---|---|
| 点电荷场强 + 叠加原理（性质 1.4.1），连续分布时积分（定义 1.4.1） | 任意分布，常配合对称性减少分量 | 电偶极子（例 1.4.1、例 1.4.2，公式 1.4.1）、圆环面轴线（例 1.4.4） |
| 远场展开 | $r$ 远大于电荷系线度 | 总电荷不为零时像点电荷，为零时像电偶极子 $\boldsymbol{p}$（定义 1.4.2），场 $\propto 1/r^3$ |
| 高斯定理（定理 1.6.1） | 球、轴、面对称的分布 | 球壳（例 1.7.1）、无限长直线（例 1.7.2）、无限大平面（例 1.7.3） |

- 电场线（定义 1.5.1）起于正电荷、止于负电荷，不相交、在无电荷处不中断；电通量 $\Phi_{\mathrm{e}} = \iint_S\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}$（定义 1.5.2）。
- 高斯定理 $\oiint_S\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S} = q_{\mathrm{enc}}/\varepsilon_0$ 由平方反比律与立体角（定义 1.6.1）证明，微分形式 $\nabla\cdot\boldsymbol{E} = \rho/\varepsilon_0$（定理 1.6.2）说明电荷是静电场的源。

## 思考题

1. 为什么电偶极子远处的场不遵循平方反比律？

   **答** $+q$ 与 $-q$ 的场在远处几乎抵消，剩下的是两者的差，相当于对点电荷的场求一次导数，所以多一个 $1/r$ 因子（§1.4.4）。

2. 电场线能否相交？能否相切？

   **答** 都不能（场强为零的点除外）。相交或相切意味着交点处场强有两个方向。

3. 为什么静电场的电场线不能闭合？

   **答** 若有一条闭合的电场线，沿它的环量 $\oint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l}>0$，与静电场的环路定理矛盾（[5.3.2](/5.3.2)）。

4. 高斯定理与 Coulomb 定律是什么关系？

   **答** 对静止电荷，由 Coulomb 定律和叠加原理可以导出高斯定理；反之，由高斯定理加上点电荷场的球对称性也能导出 Coulomb 定律。但高斯定理对运动电荷也成立，Coulomb 定律不成立。

5. 两块平行的大平板相距 $d$，面积都是 $S$，分别带电 $+q$、$-q$。有人说按 Coulomb 定律两板间的作用力为 $\frac{q^2}{4\pi\varepsilon_0d^2}$；有人说板间场强为 $\frac{q}{\varepsilon_0S}$，所以力为 $\frac{q^2}{\varepsilon_0S}$；还有人说一块板在另一块板处的场强为 $\frac{q}{2\varepsilon_0S}$，所以力为 $\frac{q^2}{2\varepsilon_0S}$。哪种说法对？

   **答** 第三种。两板不能看作点电荷（$d\ll\sqrt S$），第一种不对；板间场强 $\frac{q}{\varepsilon_0S}$ 包含了受力板自身的场，而一个带电体自身的场对它的合力为零，第二种不对。

6. 在面电荷密度为 $\sigma$ 的无限大均匀带电平面上挖去一个半径为 $R$ 的圆孔，求圆孔轴线上的场强。

   **答** 在例 1.4.4 中令 $R_1=R$、$R_2\to\infty$，得 $E_x=\dfrac{\sigma x}{2\varepsilon_0\sqrt{x^2+R^2}}$；也可以看作无限大平面的场减去半径为 $R$ 的圆盘的场。
