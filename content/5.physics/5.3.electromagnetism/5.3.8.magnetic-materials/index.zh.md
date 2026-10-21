---
title: 磁场中的磁介质
description: 顺磁质、抗磁质与铁磁质；原子的轨道、自旋与核磁矩，Larmor 进动与抗磁性；磁化强度与磁化电流；磁场强度 H 及其环路定理、界面关系与磁屏蔽；磁畴、磁化曲线、磁滞回线与 Curie 温度；简单磁路。
---

前面几章讨论的是真空中的磁场。实际的磁场中总有物质，而任何物质在磁场中都会被磁化，反过来改变磁场；从这个角度看，所有物质都称为磁介质。本章的结构与 [5.3.4](/5.3.4) 中的**电介质**完全平行：先从微观上说明物质为什么会被磁化（原子的磁矩，对应于分子的**电偶极矩**），再用磁化强度描述磁化的程度、用磁化电流描述磁化对磁场的贡献（对应于**极化强度**和**极化电荷**），最后引入辅助量磁场强度 $\boldsymbol{H}$，使环路定理中只出现可以控制的传导电流（对应于**电位移** $\boldsymbol{D}$）。与电介质不同的是铁磁质：它的磁化可以比外**场强**上千倍，而且与磁化的历史有关，这是电磁铁、变压器和永磁体的基础。磁性归根结底是量子现象，本章的经典图像只是一个可用的模型，电子自旋与原子磁矩的量子理论见 [5.5.4](/5.5.4)。§8.6 是选讲内容。

## 8.1. 磁介质对磁场的影响

在长直螺线管中充满某种均匀物质，管内的**磁感应强度**由真空时的 $B_0$ 变为

$$
B=\mu_{\mathrm{r}}B_0,
$$
比值 $\mu_{\mathrm{r}}$ 只与物质有关，称为该物质的相对磁导率（relative permeability）。这里的 $\boldsymbol{B}$ 是传导电流的场 $\boldsymbol{B}_0$ 与被磁化的物质产生的附加场 $\boldsymbol{B}'$ 之和，$\boldsymbol{B}=\boldsymbol{B}_0+\boldsymbol{B}'$。在磁场作用下物质产生磁性或磁性发生变化的现象称为磁化（magnetization），能被磁化的物质统称为磁介质（magnetic material）。按 $\mu_{\mathrm{r}}$ 的大小，磁介质分为三类：

| 类别 | $\mu_{\mathrm{r}}$ | 例子（室温，$\chi_{\mathrm{m}}=\mu_{\mathrm{r}}-1$） |
|---|---|---|
| 顺磁质 | 略大于 1 | 铝 $2.2\times10^{-5}$，铂 $2.6\times10^{-4}$，液氧（$90\,\mathrm{K}$）约 $3.6\times10^{-3}$ |
| 抗磁质 | 略小于 1 | 水 $-9.0\times10^{-6}$，铜 $-9.6\times10^{-6}$，银 $-2.4\times10^{-5}$，铋 $-1.7\times10^{-4}$ |
| 铁磁质 | 远大于 1 | $\mu_{\mathrm{r}}$ 的最大值：纯铁约 $5\times10^3$，硅钢 $10^3$–$10^4$，坡莫合金（镍铁合金）可达 $10^5$ |

顺磁质（paramagnetic substance）使磁场略微增强，抗磁质（diamagnetic substance）使磁场略微减弱，两者的 $\lvert\mu_{\mathrm{r}}-1\rvert$ 都只有 $10^{-6}$–$10^{-3}$ 量级，而且 $\mu_{\mathrm{r}}$ 是与外场无关的常量，属于线性磁介质。铁磁质（ferromagnetic substance）使磁场大大增强，它的 $\mu_{\mathrm{r}}$ 不是常量，随磁场和磁化历史而变（§8.5）。

## 8.2. 原子的磁矩

物质的磁性来自原子中电荷的运动。原子的**磁矩**（[5.3.7](/5.3.7)）有三个来源：核外电子绕核的轨道运动、电子的自旋，以及原子核的磁矩。

### 8.2.1. 电子的轨道磁矩

在 Bohr 的原子模型中，电子以速率 $v$ 沿半径为 $r$ 的圆轨道绕核运动，相当于一个圆电流

$$
I=\frac{e}{2\pi r/v}=\frac{ev}{2\pi r},
$$
其磁矩大小为 $m=I\cdot\pi r^2=\frac12evr$。电子的轨道**角动量**大小为 $L=m_{\mathrm{e}}vr$，而电子带负电，磁矩与角动量反向，所以

$$
\boldsymbol{m}_l=-\frac{e}{2m_{\mathrm{e}}}\boldsymbol{L}.
$$
磁矩与角动量之比称为旋磁比（gyromagnetic ratio），电子轨道运动的旋磁比为 $\gamma_l=-e/(2m_{\mathrm{e}})$；这与 [5.3.7](/5.3.7) 中旋转带电体的结果 $Q/(2m_0)$ 一致。量子力学中轨道角动量的分量是 $\hbar$ 的整数倍，相应的磁矩以

$$
\mu_{\mathrm{B}}=\frac{e\hbar}{2m_{\mathrm{e}}}\approx9.274\times10^{-24}\,\mathrm{J/T}
$$
为单位，称为 Bohr 磁子（[5.5.4](/5.5.4)）。

### 8.2.2. 电子的自旋磁矩

电子磁矩的第二个来源是电子的自旋。自旋是电子固有的角动量，不能理解为电子绕自身轴的转动；它在任一方向（如外磁场方向）上的分量只能取 $S_z=m_s\hbar$，$m_s=\pm\frac12$（详见 [5.5.4](/5.5.4)）。自旋磁矩与自旋角动量的关系为

$$
\boldsymbol{m}_s=-g_{\mathrm{e}}\frac{e}{2m_{\mathrm{e}}}\boldsymbol{S}\approx-\frac{e}{m_{\mathrm{e}}}\boldsymbol{S},\qquad m_{s,z}=\mp\mu_{\mathrm{B}},
$$
其中 $g_{\mathrm{e}}\approx2.002\,32$ 称为电子的 $g$ 因子。自旋的旋磁比约为轨道的两倍，这是经典模型给不出的；$g_{\mathrm{e}}=2$ 由 Dirac 的相对论量子力学导出，与 2 的微小差别由量子电动力学精确地算出。

### 8.2.3. 核磁矩

质子和中子也有自旋，相应的磁矩写成

$$
\boldsymbol{m}=g\frac{e}{2m_{\mathrm{p}}}\boldsymbol{S},\qquad g_{\mathrm{p}}\approx5.586,\qquad g_{\mathrm{n}}\approx-3.826,
$$
中子不带电，却有磁矩（与自旋反向），说明它有内部结构（由带电的夸克组成）。原子核的磁矩由核内质子与中子的自旋磁矩和质子的轨道磁矩合成，写成 $\boldsymbol{m}=g\frac{e}{2m_{\mathrm{p}}}\boldsymbol{I}$，$\boldsymbol{I}$ 是核的自旋角动量（核物理的通用记号），$g$ 由具体的核决定。因为 $m_{\mathrm{p}}\approx1836\,m_{\mathrm{e}}$，核磁矩的单位核磁子 $e\hbar/(2m_{\mathrm{p}})$ 比 Bohr 磁子小三个数量级，核磁矩对物质磁性的贡献通常可以忽略。但核磁矩在磁场中的**进动**（§8.2.5）可以被精确地测量：氢核在 $1\,\mathrm{T}$ 磁场中的进动频率为 $42.58\,\mathrm{MHz}$，用射频场与之共振，就是核磁共振（NMR），它是化学中测定分子结构的波谱方法和医学中磁共振成像（MRI）的基础。

### 8.2.4. 顺磁质与抗磁质的微观解释

一个分子中所有电子的轨道磁矩、自旋磁矩与核磁矩的矢量和，称为分子的固有磁矩 $\boldsymbol{m}_{\mathrm{mol}}$。在磁化问题中，可以把每个分子的固有磁矩看作一个等效的圆电流，这就是 Ampère 的分子电流假说。

顺磁质的分子有固有磁矩，量级为 $10^{-23}\,\mathrm{A\,m^2}$（约一个 Bohr 磁子），主要来自电子。没有外磁场时，热运动使各分子的磁矩完全混乱，宏观上不显磁性。加上外磁场 $\boldsymbol{B}_0$ 后，分子磁矩受力矩 $\boldsymbol{m}_{\mathrm{mol}}\times\boldsymbol{B}_0$，势能 $-\boldsymbol{m}_{\mathrm{mol}}\cdot\boldsymbol{B}_0$ 使磁矩倾向于沿外场排列，而热运动破坏这种排列，结果是部分有序：磁矩沿外场方向有一个净的平均值，介质内的磁场增强。由于 $m_{\mathrm{mol}}B_0\ll k_{\mathrm{B}}T$（$1\,\mathrm{T}$ 中约 $10^{-23}\,\mathrm{J}$，室温下 $k_{\mathrm{B}}T\approx4\times10^{-21}\,\mathrm{J}$），有序的程度很低，并且由 **Boltzmann 分布**可以算出平均磁矩与 $m_{\mathrm{mol}}B_0/(k_{\mathrm{B}}T)$ 成正比，所以顺磁质的磁化率与温度成反比，$\chi_{\mathrm{m}}=C/T$（Curie 定律）。宏观上，顺磁质像一块顺着外场放置的小磁铁，会被磁铁吸引。

抗磁质的分子中，各电子的轨道磁矩与自旋磁矩恰好抵消，固有磁矩为零。在外磁场中，每个电子的轨道运动都会产生一个与外场反向的附加磁矩（§8.2.5），这些附加磁矩的总和称为感生磁矩，它使介质内的磁场减弱。抗磁质像一块反着外场放置的小磁铁，会被磁铁排斥。感生磁矩与温度几乎无关，所以抗磁质的磁化率也与温度几乎无关。

### 8.2.5. Larmor 进动与感生磁矩

电子的轨道磁矩 $\boldsymbol{m}=-\frac{e}{2m_{\mathrm{e}}}\boldsymbol{L}$ 在外磁场 $\boldsymbol{B}_0$ 中受力矩 $\boldsymbol{m}\times\boldsymbol{B}_0$。由**角动量定理**，

$$
\frac{\mathrm{d}\boldsymbol{L}}{\mathrm{d}t}=\boldsymbol{m}\times\boldsymbol{B}_0=\frac{e}{2m_{\mathrm{e}}}\boldsymbol{B}_0\times\boldsymbol{L}.
$$
$\mathrm{d}\boldsymbol{L}$ 始终垂直于 $\boldsymbol{L}$ 和 $\boldsymbol{B}_0$，所以力矩不改变角动量的大小和它与 $\boldsymbol{B}_0$ 的夹角，只使 $\boldsymbol{L}$ 绕 $\boldsymbol{B}_0$ 以角速度

$$
\boldsymbol{\omega}_{\mathrm{L}}=\frac{e}{2m_{\mathrm{e}}}\boldsymbol{B}_0
$$
转动。这与重力矩使陀螺**进动**（[5.1.5](/5.1.5#sec-5.7.2)）是同一回事，称为 Larmor 进动（Larmor precession）。一般地，旋磁比为 $\gamma$ 的磁矩在磁场中以 $\omega=\lvert\gamma\rvert B$ 进动，与磁矩和磁场的夹角无关；$1\,\mathrm{T}$ 中电子轨道的 Larmor 频率约为 $14\,\mathrm{GHz}$，上面的核磁共振频率也是这样得到的。

进动相当于电子的整个轨道以角速度 $\boldsymbol{\omega}_{\mathrm{L}}$（沿 $\boldsymbol{B}_0$ 方向）附加地转动。带负电的电子随轨道这样转动，形成一个附加的圆电流，其磁矩与 $\boldsymbol{\omega}_{\mathrm{L}}$ 反向，即

$$
\Delta\boldsymbol{m}=-\frac{e^2\overline{\rho^2}}{4m_{\mathrm{e}}}\boldsymbol{B}_0,
$$
其中 $\overline{\rho^2}$ 是电子到通过核、平行于 $\boldsymbol{B}_0$ 的轴线的距离平方的平均值。无论电子原来沿哪个方向绕核运动，附加磁矩总是与外场反向：这就是抗磁性的来源。感生磁矩比固有磁矩小得多，所以一切物质都有抗磁性，但在有固有磁矩的物质中它被顺磁性掩盖。

**例 8.2.1（抗磁悬浮）** 抗磁质在非均匀磁场中受指向弱场区的力。磁化率为 $\chi_{\mathrm{m}}$（$\lvert\chi_{\mathrm{m}}\rvert\ll1$）的介质在磁场中每单位体积的能量为 $-\frac{\chi_{\mathrm{m}}B^2}{2\mu_0}$，沿竖直方向每单位体积受力 $\frac{\chi_{\mathrm{m}}}{\mu_0}B\frac{\mathrm{d}B}{\mathrm{d}z}$。要让密度为 $\rho$ 的抗磁物体悬浮，需要

$$
B\Big\lvert\frac{\mathrm{d}B}{\mathrm{d}z}\Big\rvert\ge\frac{\mu_0\rho g}{\lvert\chi_{\mathrm{m}}\rvert}.
$$
对水，$\rho=10^3\,\mathrm{kg/m^3}$，$\chi_{\mathrm{m}}=-9.0\times10^{-6}$，右边约为 $1.4\times10^{3}\,\mathrm{T^2/m}$，例如磁体端口附近 $B\approx16\,\mathrm{T}$、**梯度**约 $100\,\mathrm{T/m}$。生物体主要由水、蛋白质等抗磁物质组成，1997 年 Geim 与 Berry 正是用这样的强磁体让一只活青蛙悬浮起来（他们因此获 2000 年的搞笑诺贝尔物理学奖；Geim 后来因用胶带剥离法制得石墨烯，与 Novoselov 共获 2010 年 Nobel 物理学奖）。

## 8.3. 磁介质的磁化

### 8.3.1. 磁化强度

磁介质的磁化过程与电介质的极化过程类似：传导电流 $I_0$ 产生外场 $\boldsymbol{B}_0$，介质被磁化后产生附加场 $\boldsymbol{B}'$，介质中的总场是 $\boldsymbol{B}=\boldsymbol{B}_0+\boldsymbol{B}'$，而磁化的程度又由总场 $\boldsymbol{B}$ 决定。

**定义 8.3.1（磁化强度）** 介质中某点附近单位体积内分子磁矩的矢量和

$$
\boldsymbol{M}=\frac{\sum\boldsymbol{m}_{\mathrm{mol}}}{\Delta V}
$$
称为该点的**磁化强度**。$\Delta V$ 宏观上小（远小于 $\boldsymbol{M}$ 发生显著变化的尺度）、微观上大（远大于分子间距）。磁化强度的 SI 单位是 $\mathrm{A/m}$，与面**电流密度**的量纲相同。

$\boldsymbol{M}$ 反映了分子磁矩排列的有序程度，是介质对总磁场 $\boldsymbol{B}$ 的响应。实验表明，对各向同性线性磁介质，$\boldsymbol{M}$ 与 $\boldsymbol{B}$ 成正比：

$$
\boldsymbol{M}=\frac{\mu_{\mathrm{r}}-1}{\mu_0\mu_{\mathrm{r}}}\boldsymbol{B}.
$$
顺磁质的 $\boldsymbol{M}$ 与 $\boldsymbol{B}$ 同向，抗磁质反向。铁磁质的 $\boldsymbol{M}$ 与 $\boldsymbol{B}$ 的关系是非线性、非单值的，上式不适用。

### 8.3.2. 磁化电流

被磁化的介质中，分子电流的有序排列在宏观上表现为一种等效的电流分布，称为磁化电流（magnetization current），也称束缚电流。在产生磁场和受磁场作用这两方面，磁化电流与传导电流完全等效；不同的是它不伴随电荷的宏观移动，也不产生 Joule 热。在均匀磁化的介质内部，相邻分子电流相互抵消，只在表面留下没有抵消的部分；磁化不均匀时，介质内部也有磁化电流。

下面求磁化电流与磁化强度的关系。在介质中任取闭合路径 $L$，求与它套连的磁化电流 $I'$。设每个分子电流为 $i$、面积为 $S_{\mathrm{mol}}$，磁矩 $\boldsymbol{m}_{\mathrm{mol}}=iS_{\mathrm{mol}}\boldsymbol{e}_{\mathrm{n}}$，分子数密度为 $n$。只有被 $L$"穿过"的分子电流才与 $L$ 套连一次，它们对 $I'$ 有贡献；不被穿过的分子电流要么不与 $L$ 相交，要么两次穿过以 $L$ 为边界的曲面，贡献为零。线元 $\mathrm{d}\boldsymbol{l}$ 穿过的分子电流的中心位于以 $S_{\mathrm{mol}}$ 为底、以 $\mathrm{d}\boldsymbol{l}$ 为轴的斜柱体内，体积为 $S_{\mathrm{mol}}\,\mathrm{d}l\cos\theta$（$\theta$ 是 $\boldsymbol{e}_{\mathrm{n}}$ 与 $\mathrm{d}\boldsymbol{l}$ 的夹角），于是

$$
\mathrm{d}I'=n\,i\,S_{\mathrm{mol}}\cos\theta\,\mathrm{d}l=\boldsymbol{M}\cdot\mathrm{d}\boldsymbol{l}.
$$

**定理 8.3.1（磁化电流与磁化强度）** 与任一闭合回路 $L$ 套连的磁化电流（即穿过以 $L$ 为边界、与 $L$ 成右手螺旋关系的任一曲面 $S$ 的磁化电流）为

$$
I'=\oint_L\boldsymbol{M}\cdot\mathrm{d}\boldsymbol{l}.
$$
对应的微分形式与界面上的形式为

$$
\boldsymbol{J}'=\nabla\times\boldsymbol{M},\qquad \boldsymbol{K}'=\boldsymbol{M}\times\boldsymbol{e}_{\mathrm{n}},
$$
其中 $\boldsymbol{J}'$ 是磁化体电流密度，$\boldsymbol{K}'$ 是介质表面的磁化面电流密度（单位长度上的磁化电流，单位 $\mathrm{A/m}$），$\boldsymbol{e}_{\mathrm{n}}$ 是介质表面的单位外法向矢量。

**证明** 由 **Stokes 公式**（[2.2.14](/2.2.14#sec-14.3.1)），$\oint_L\boldsymbol{M}\cdot\mathrm{d}\boldsymbol{l}=\iint_S(\nabla\times\boldsymbol{M})\cdot\mathrm{d}\boldsymbol{S}$，而 $I'=\iint_S\boldsymbol{J}'\cdot\mathrm{d}\boldsymbol{S}$ 对任意曲面成立，所以 $\boldsymbol{J}'=\nabla\times\boldsymbol{M}$。在介质表面取一个跨越表面的扁矩形回路，长边 $\Delta l$ 沿单位切向矢量 $\boldsymbol{e}_{\mathrm{t}}$，一条在介质内、一条在介质外（$\boldsymbol{M}=\boldsymbol{0}$），短边趋于零，则 $\oint\boldsymbol{M}\cdot\mathrm{d}\boldsymbol{l}=\boldsymbol{M}\cdot\boldsymbol{e}_{\mathrm{t}}\,\Delta l$。这样绕行的回路，与绕向成右手螺旋关系的法向是 $\boldsymbol{e}_{\mathrm{t}}\times\boldsymbol{e}_{\mathrm{n}}$，穿过回路的面电流为 $\boldsymbol{K}'\cdot(\boldsymbol{e}_{\mathrm{t}}\times\boldsymbol{e}_{\mathrm{n}})\Delta l=(\boldsymbol{e}_{\mathrm{n}}\times\boldsymbol{K}')\cdot\boldsymbol{e}_{\mathrm{t}}\,\Delta l$。两者对所有切向 $\boldsymbol{e}_{\mathrm{t}}$ 相等，得 $\boldsymbol{M}$ 的切向分量 $\boldsymbol{M}_t=\boldsymbol{e}_{\mathrm{n}}\times\boldsymbol{K}'$；由于 $\boldsymbol{K}'$ 沿界面，这等价于 $\boldsymbol{K}'=\boldsymbol{M}\times\boldsymbol{e}_{\mathrm{n}}$，其大小等于 $\boldsymbol{M}$ 的切向分量。$\square$

这三个式子与电介质中极化电荷的关系 $q'=-\oiint\boldsymbol{P}\cdot\mathrm{d}\boldsymbol{S}$、$\rho'=-\nabla\cdot\boldsymbol{P}$、$\sigma'=\boldsymbol{P}\cdot\boldsymbol{e}_{\mathrm{n}}$（[5.3.4](/5.3.4)）一一对应：电介质中是通量与**散度**，磁介质中是环量与**旋度**。

**例 8.3.1（长直螺线管中的均匀磁化）** 长直螺线管内充满均匀的各向同性介质，被均匀磁化，磁化强度为 $\boldsymbol{M}$（沿轴线），求介质产生的磁场。

**解** 介质内部均匀磁化，$\nabla\times\boldsymbol{M}=\boldsymbol{0}$，没有体磁化电流。侧表面上 $\boldsymbol{M}$ 平行于表面，磁化面电流密度 $K'=M$，绕轴线环流，相当于一个每单位长度电流为 $M$ 的长直螺线管。由长直螺线管的磁场 $B=\mu_0nI$（[5.3.6](/5.3.6)），介质产生的附加场为

$$
\boldsymbol{B}'=\mu_0\boldsymbol{M}.
$$
磁化电流在这里完全等效于介质。

## 8.4. H 的环路定理

### 8.4.1. 磁场强度

有介质时，磁场仍由全部电流（传导电流 $I_0$ 与磁化电流 $I'$）产生，所以磁场的 **Gauss 定理**（**磁通连续定理**）与环路定理照样成立：

$$
\oiint_S\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}=0,\qquad \oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l}=\mu_0\big(I_{0,\mathrm{enc}}+I'_{\mathrm{enc}}\big).
$$
但磁化电流事先未知，它又取决于待求的磁场，直接用第二式并不方便。把定理 8.3.1 代入，移项得

$$
\oint_L\Big(\frac{\boldsymbol{B}}{\mu_0}-\boldsymbol{M}\Big)\cdot\mathrm{d}\boldsymbol{l}=I_{0,\mathrm{enc}}.
$$

**定义 8.4.1（磁场强度）** 辅助矢量

$$
\boldsymbol{H}=\frac{\boldsymbol{B}}{\mu_0}-\boldsymbol{M}
$$
称为**磁场强度**。它的 SI 单位是 $\mathrm{A/m}$；CGS 单位制中的单位是奥斯特，$1\,\mathrm{Oe}=\frac{10^3}{4\pi}\,\mathrm{A/m}\approx79.6\,\mathrm{A/m}$。

**定理 8.4.1（$\boldsymbol{H}$ 的环路定理）** 磁场强度沿任一闭合回路的环量，等于与该回路套连的传导电流的代数和：

$$
\oint_L\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{l}=I_{0,\mathrm{enc}},\qquad\text{微分形式}\quad\nabla\times\boldsymbol{H}=\boldsymbol{J}_0.
$$

$\boldsymbol{H}=\boldsymbol{B}/\mu_0-\boldsymbol{M}$ 是普遍成立的定义，对铁磁质也成立；真空中 $\boldsymbol{M}=\boldsymbol{0}$，$\boldsymbol{H}=\boldsymbol{B}/\mu_0$。需要注意，$\boldsymbol{H}$ 的环量只由传导电流决定，并不意味着 $\boldsymbol{H}$ 本身只由传导电流决定：$\boldsymbol{H}$ 的散度 $\nabla\cdot\boldsymbol{H}=-\nabla\cdot\boldsymbol{M}$ 一般不为零。只有在对称性足够高的问题中，才能单独用 $\boldsymbol{H}$ 的环路定理求出 $\boldsymbol{H}$。

### 8.4.2. 各向同性线性磁介质

把 §8.3.1 的实验规律用 $\boldsymbol{H}$ 表示：由 $\boldsymbol{B}=\mu_0(\boldsymbol{H}+\boldsymbol{M})$ 和 $\boldsymbol{M}=\frac{\mu_{\mathrm{r}}-1}{\mu_0\mu_{\mathrm{r}}}\boldsymbol{B}$ 解得

$$
\boldsymbol{M}=\chi_{\mathrm{m}}\boldsymbol{H},\qquad \boldsymbol{B}=\mu_0\mu_{\mathrm{r}}\boldsymbol{H}=\mu\boldsymbol{H},\qquad \mu_{\mathrm{r}}=1+\chi_{\mathrm{m}}.
$$
无量纲的比例系数 $\chi_{\mathrm{m}}$ 称为磁化率（magnetic susceptibility），$\mu=\mu_0\mu_{\mathrm{r}}$ 称为磁导率（permeability）。顺磁质 $\chi_{\mathrm{m}}>0$，抗磁质 $\chi_{\mathrm{m}}<0$。在各向同性线性介质中，$\boldsymbol{M}$、$\boldsymbol{B}$、$\boldsymbol{H}$ 三者方向相同。

**性质 8.4.1（磁化电流的分布）** 在均匀的各向同性线性磁介质中（$\mu_{\mathrm{r}}$ 为常量，不论磁化是否均匀），

$$
\boldsymbol{J}'=\nabla\times\boldsymbol{M}=\chi_{\mathrm{m}}\nabla\times\boldsymbol{H}=\chi_{\mathrm{m}}\boldsymbol{J}_0.
$$
因此介质内没有传导电流的地方，也没有体磁化电流；若介质内没有传导电流，磁化电流只分布在介质的表面上。

**例 8.4.1（载流的磁介质平板）** 厚 $2h$ 的无限大均匀平板（$-h<y<h$）由相对磁导率为 $\mu_{\mathrm{r}}$ 的各向同性线性介质制成，板中有均匀的传导电流，电流密度为 $\boldsymbol{J}_0=J_0\boldsymbol{e}_z$。求空间的磁场与板面上的磁化面电流。

**解** 对称性分析：系统沿 $x$、$z$ 方向平移不变，所以场只依赖于 $y$；任一平行于 $yz$ 面的平面都是系统的镜面，$\boldsymbol{B}$ 作为**轴矢量**必须垂直于镜面，即 $\boldsymbol{B}=B(y)\boldsymbol{e}_x$；$y=0$ 平面也是镜面，于是 $B(-y)=-B(y)$。$\boldsymbol{H}$ 有同样的性质。

在 $xy$ 平面内取一个矩形回路，两条长 $\Delta l$ 的边平行于 $x$ 轴，分别位于 $y$ 与 $-y$ 处，回路绕向与 $\boldsymbol{e}_z$ 成右手螺旋关系。由 $\boldsymbol{H}$ 的环路定理，

$$
\big[H_x(-y)-H_x(y)\big]\Delta l=-2H_x(y)\,\Delta l=2J_0\min(y,h)\,\Delta l\qquad(y>0),
$$
所以

$$
\boldsymbol{H}=\begin{cases}-J_0y\,\boldsymbol{e}_x,&\lvert y\rvert\le h,\\-J_0h\,\operatorname{sgn}(y)\,\boldsymbol{e}_x,&\lvert y\rvert>h,\end{cases}\qquad \boldsymbol{B}=\begin{cases}-\mu_0\mu_{\mathrm{r}}J_0y\,\boldsymbol{e}_x,&\lvert y\rvert\le h,\\-\mu_0J_0h\,\operatorname{sgn}(y)\,\boldsymbol{e}_x,&\lvert y\rvert>h.\end{cases}
$$
板内 $\boldsymbol{M}=(\mu_{\mathrm{r}}-1)\boldsymbol{H}=-(\mu_{\mathrm{r}}-1)J_0y\,\boldsymbol{e}_x$。上表面 $\boldsymbol{e}_{\mathrm{n}}=\boldsymbol{e}_y$，$\boldsymbol{K}'_{\text{top}}=\boldsymbol{M}\times\boldsymbol{e}_y=-(\mu_{\mathrm{r}}-1)J_0h\,\boldsymbol{e}_z$；下表面 $\boldsymbol{e}_{\mathrm{n}}=-\boldsymbol{e}_y$，$\boldsymbol{M}=(\mu_{\mathrm{r}}-1)J_0h\,\boldsymbol{e}_x$，同样得 $\boldsymbol{K}'_{\text{bottom}}=-(\mu_{\mathrm{r}}-1)J_0h\,\boldsymbol{e}_z$。两个表面的磁化电流同向，加起来不为零。这并不矛盾：板内还有体磁化电流 $\boldsymbol{J}'=\nabla\times\boldsymbol{M}=(\mu_{\mathrm{r}}-1)J_0\boldsymbol{e}_z$（性质 8.4.1），每单位宽度的体磁化电流 $2h(\mu_{\mathrm{r}}-1)J_0$ 恰好与两个表面的 $-2(\mu_{\mathrm{r}}-1)J_0h$ 抵消，总磁化电流为零。所以板外的磁场与没有介质时相同。

![载流磁介质平板（灰色区域）内外的磁感应强度 $B_x$。$\boldsymbol{H}$ 只由传导电流决定，与 $\mu_{\mathrm{r}}=1$ 的曲线相同；板内的 $B$ 增大为 $\mu_{\mathrm{r}}$ 倍，在板面上 $B$ 的切向分量跃变而 $H$ 的切向分量连续，板外的场与介质无关](./plots/slab-fields.py)

### 8.4.3. 磁场的界面关系与磁屏蔽

在两种介质的界面上，磁场一般不连续，微分形式的方程不能用，要用积分形式导出界面关系。设 $\boldsymbol{e}_{\mathrm{n}}$ 为由介质 2 指向介质 1 的单位法向矢量。

- 法向关系：跨越界面取一个扁圆柱面（两底面积为 $\Delta S$，高趋于零），由 $\oiint\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}=0$ 得 $(B_{1n}-B_{2n})\Delta S=0$，即 $B_{1n}=B_{2n}$：$\boldsymbol{B}$ 的法向分量连续。
- 切向关系：跨越界面取一个扁矩形回路，由 $\boldsymbol{H}$ 的环路定理得 $\boldsymbol{e}_{\mathrm{n}}\times(\boldsymbol{H}_1-\boldsymbol{H}_2)=\boldsymbol{K}_0$，$\boldsymbol{K}_0$ 是界面上的传导面电流密度。界面上没有传导电流时，$H_{1t}=H_{2t}$：$\boldsymbol{H}$ 的切向分量连续。

**例 8.4.2（磁感线的"折射"）** 两种各向同性线性介质的界面上没有传导电流，介质中的**磁感线**与界面法线的夹角分别为 $\theta_1$、$\theta_2$。由 $B_{1n}=B_{2n}$、$B_{1t}/\mu_1=B_{2t}/\mu_2$，

$$
\frac{\tan\theta_1}{\tan\theta_2}=\frac{B_{1t}/B_{1n}}{B_{2t}/B_{2n}}=\frac{\mu_1}{\mu_2}.
$$
若 $\mu_1\gg\mu_2$（介质 1 是铁磁质，介质 2 是空气），只要 $\theta_2$ 不为零，$\theta_1$ 就接近 $90^\circ$：铁中的磁感线几乎平行于界面，沿着铁芯走，而且铁中的 $B$ 远大于空气中的 $B$。这就是铁芯能够把磁感线约束在其中、引导磁通的原因，也是静磁屏蔽的原理：用高磁导率材料（如坡莫合金）制成的屏蔽罩为磁感线提供了磁阻很小的通路，外磁场的磁感线绝大部分从罩壁中通过，罩内的磁场大大减弱。精密的电子束仪器、磁传感器和古老的显像管都需要这样的磁屏蔽。与**导体**对静电场的完全屏蔽不同，静磁屏蔽只能使磁场减弱，不能完全隔绝。

## 8.5. 铁磁质

### 8.5.1. 磁畴

铁、钴、镍及其许多合金和化合物是铁磁质。它们的磁性主要来自电子的自旋磁矩：相邻原子中电子的自旋之间有一种很强的相互作用，使它们倾向于平行排列。这种交换作用（exchange interaction）是电子的全同性与 Pauli 不相容原理（[5.5.4](/5.5.4)）的结果，本质上是一种静电相互作用的量子效应，比磁矩之间的经典磁相互作用强得多。在 Curie 温度（§8.5.4）以下，交换作用使铁磁质内部形成许多自发磁化的小区域，每个区域内原子磁矩整齐地沿同一方向排列，称为磁畴（magnetic domain）。

磁畴的线度为 $10^{-6}$–$10^{-3}\,\mathrm{m}$，一个磁畴含 $10^{12}$–$10^{15}$ 个原子。畴内的磁矩沿晶体的易磁化方向排列，不同磁畴的磁化方向不同。整块铁磁体不会自发地磁化为一个整体，是两种能量竞争的结果：整体磁化时，表面出现的磁极在外部产生很强的磁场，静磁能很高；分成磁化方向不同的磁畴可以大大降低静磁能，但畴与畴之间的过渡层（畴壁）中相邻磁矩不平行，要付出交换能。两者平衡决定了磁畴的大小与形状。没有外磁场时，各磁畴的取向通常是无规的，宏观上不显磁性。磁畴可以用磁光 Kerr 效应等方法直接观察。

外加磁场后，磁化方向与外场接近的磁畴能量较低，畴壁移动使这些磁畴扩大、其他磁畴缩小；磁场再增大，留存的磁畴的磁化方向转向外场；最终所有磁畴都沿外场排列，磁化达到饱和。磁化的中间阶段，畴壁的移动是一跳一跳的（被晶体中的缺陷钉扎又挣脱），磁化强度随之作微小的跃变，在绕在样品上的线圈中产生噪声脉冲，这称为 Barkhausen 效应，它直接证明了铁磁体是以磁畴为单位完成磁化的。

### 8.5.2. 磁化曲线

铁磁质的 $\boldsymbol{B}$ 与 $\boldsymbol{H}$ 之间的关系是非线性的，而且不是单值的。形式上仍可写成 $B=\mu_0\mu_{\mathrm{r}}H$，但 $\mu_{\mathrm{r}}$ 既不是常量，也不由 $H$ 唯一确定。

测量方法：把待测材料做成圆环，环上密绕 $n$ 匝/单位长度的线圈，通以电流 $I_0$。由 $\boldsymbol{H}$ 的环路定理和圆环的对称性，环内 $H=nI_0$；再绕一个次级线圈接冲击电流计或磁通计，由电流变化时次级线圈中通过的电荷量求出**磁通量** $\Phi$ 的变化（[5.3.9](/5.3.9)），得到 $B=\Phi/S$。逐点改变 $I_0$，就得到 $B$ 与 $H$ 的关系。

从完全未磁化的状态（$H=0$，$B=0$）开始增大 $H$，得到的 $B$–$H$ 曲线称为起始磁化曲线：开始时 $B$ 增加较慢（畴壁的可逆移动），然后急剧增加（畴壁的不可逆移动），最后趋于平缓（磁畴转向），达到饱和磁感应强度 $B_{\mathrm{s}}$ 后 $B$ 只按 $\mu_0H$ 缓慢增长。相应地，$\mu_{\mathrm{r}}=B/(\mu_0H)$ 从起始值 $\mu_{\mathrm{i}}$ 增大到最大值 $\mu_{\mathrm{m}}$，再随饱和而减小。

### 8.5.3. 磁滞回线

磁化到饱和后减小 $H$，$B$ 并不沿起始磁化曲线返回，而是滞后于 $H$ 的变化，这称为磁滞。$H$ 减到零时，$B$ 仍保留一个值 $B_{\mathrm{r}}$，称为剩余磁感应强度，简称剩磁（remanence）；要使 $B$ 减到零，必须加反向磁场 $-H_{\mathrm{c}}$，$H_{\mathrm{c}}$ 称为矫顽力（coercivity）。继续反向磁化到饱和，再正向磁化回来，$B$–$H$ 曲线形成一条闭合曲线，称为磁滞回线（hysteresis loop）。磁滞来自畴壁移动的不可逆性。

![铁磁质的磁滞回线（简化模型）。左：软磁材料，回线窄，虚线为起始磁化曲线，标出了剩磁 $B_{\mathrm{r}}$ 与矫顽力 $H_{\mathrm{c}}$；右：硬磁材料，矫顽力大出数千倍（注意横轴的单位），回线宽](./plots/hysteresis-loops.py)

磁化一周，外界对单位体积的铁磁质所做的功等于磁滞回线所围的面积 $\oint H\,\mathrm{d}B$（[5.3.9](/5.3.9) 的磁场能量），这部分能量最终变为热，称为磁滞损耗。按回线的形状，铁磁材料分为两类：

| | 软磁材料 | 硬磁材料 |
|---|---|---|
| 矫顽力 $H_{\mathrm{c}}$ | 小，$<10^2\,\mathrm{A/m}$，坡莫合金可低于 $1\,\mathrm{A/m}$ | 大，$10^4$–$10^6\,\mathrm{A/m}$ |
| 磁滞回线 | 窄，磁导率高，磁滞损耗小 | 宽，剩磁大（$0.1$–$1.4\,\mathrm{T}$） |
| 例子 | 纯铁、硅钢、坡莫合金、软磁铁氧体 | 碳钢、钨钢、铝镍钴、钕铁硼 |
| 用途 | 变压器、电机与交流电磁铁的铁芯 | 永磁体、磁记录介质 |

### 8.5.4. Curie 温度

温度升高时，热运动破坏磁畴内磁矩的整齐排列，自发磁化强度减小。温度超过某一**临界温度** $T_{\mathrm{C}}$ 时，自发磁化消失，磁畴瓦解，铁磁质变为顺磁质；降温到 $T_{\mathrm{C}}$ 以下，铁磁性又恢复。$T_{\mathrm{C}}$ 称为 Curie 温度（Curie temperature），也称 Curie 点。几种铁磁质的 Curie 温度：铁 $1043\,\mathrm{K}$（$770\,^\circ\mathrm{C}$），钴 $1388\,\mathrm{K}$（$1115\,^\circ\mathrm{C}$），镍 $627\,\mathrm{K}$（$354\,^\circ\mathrm{C}$）。在 $T_{\mathrm{C}}$ 以上，磁化率近似满足 Curie–Weiss 定律 $\chi_{\mathrm{m}}=C/(T-T_{\mathrm{C}})$。铁磁性的出现与消失是一种相变，类似于液体在**临界点**附近的行为。

除铁磁性以外，交换作用还可以使相邻磁矩反平行排列：若反平行的磁矩相等，宏观磁矩为零，称为反铁磁性（如 $\ce{MnO}$）；若不相等，仍有宏观磁矩，称为亚铁磁性，铁氧体（如 $\ce{Fe3O4}$）就属于这一类，它们是高频电路中常用的软磁材料。

## 8.6. 简单磁路

铁芯被磁化后，磁感线几乎全部集中在铁芯内（§8.4.3），铁芯就像导线引导电流一样引导磁通。磁感线集中通过的路径称为磁路（magnetic circuit）。

考虑一个截面积为 $S$、平均长度为 $l$、磁导率为 $\mu$ 的环形铁芯，上面开有一个长为 $\delta$ 的窄气隙，铁芯上绕有 $N$ 匝通电流 $I$ 的线圈。忽略漏磁，铁芯与气隙中的磁通 $\Phi=BS$ 相同（$B_n$ 连续）。沿铁芯取 $\boldsymbol{H}$ 的环路定理：

$$
\oint\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{l}=Hl+H_\delta\delta=\frac{\Phi}{\mu S}l+\frac{\Phi}{\mu_0S}\delta=NI,
$$
所以

$$
\Phi=\frac{NI}{R_{\mathrm{m}}+R_{\mathrm{m}\delta}},\qquad R_{\mathrm{m}}=\frac{l}{\mu S},\qquad R_{\mathrm{m}\delta}=\frac{\delta}{\mu_0S}.
$$
$\mathcal{E}_{\mathrm{m}}=NI$ 称为磁通势（magnetomotive force），$R_{\mathrm{m}}=l/(\mu S)$ 称为磁阻（reluctance）。这与含**电动势**的电路（[5.3.5](/5.3.5)）完全类似：

| 磁路 | 电路 |
|---|---|
| 磁通势 $\mathcal{E}_{\mathrm{m}}=NI$ | 电动势 $\mathcal{E}$ |
| 磁通 $\Phi$ | 电流 $I$ |
| 磁阻 $R_{\mathrm{m}}=\dfrac{l}{\mu_0\mu_{\mathrm{r}}S}$ | 电阻 $R=\dfrac{l}{\sigma S}$ |
| 磁导率 $\mu$ | 电导率 $\sigma$ |

串联磁路的磁阻相加，并联磁路的磁导（磁阻的倒数）相加。气隙的磁阻与长 $\mu_{\mathrm{r}}\delta$ 的铁芯相同：若 $\mu_{\mathrm{r}}=10^3$，$1\,\mathrm{mm}$ 的气隙的磁阻就相当于 $1\,\mathrm{m}$ 长的铁芯，所以气隙对磁路的影响很大。磁路的计算是近似的：铁芯的 $\mu$ 随 $B$ 变化，实际计算要查磁化曲线，而且总有一部分磁通从铁芯外漏走。

## 小结

| | 电介质 | 磁介质 |
|---|---|---|
| 微观来源 | 分子电偶极矩 | 分子磁矩（轨道、自旋、核） |
| 描述 | 极化强度 $\boldsymbol{P}$ | 磁化强度 $\boldsymbol{M}$ |
| 束缚源 | $\rho'=-\nabla\cdot\boldsymbol{P}$，$\sigma'=\boldsymbol{P}\cdot\boldsymbol{e}_{\mathrm{n}}$ | $\boldsymbol{J}'=\nabla\times\boldsymbol{M}$，$\boldsymbol{K}'=\boldsymbol{M}\times\boldsymbol{e}_{\mathrm{n}}$ |
| 辅助量 | $\boldsymbol{D}=\varepsilon_0\boldsymbol{E}+\boldsymbol{P}$ | $\boldsymbol{H}=\boldsymbol{B}/\mu_0-\boldsymbol{M}$ |
| 规律 | $\oiint\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S}=q_0$ | $\oint\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{l}=I_0$ |
| 线性介质 | $\boldsymbol{P}=\varepsilon_0\chi_{\mathrm{e}}\boldsymbol{E}$，$\boldsymbol{D}=\varepsilon_0\varepsilon_{\mathrm{r}}\boldsymbol{E}$ | $\boldsymbol{M}=\chi_{\mathrm{m}}\boldsymbol{H}$，$\boldsymbol{B}=\mu_0\mu_{\mathrm{r}}\boldsymbol{H}$ |
| 界面关系 | $D_{1n}=D_{2n}$，$E_{1t}=E_{2t}$ | $B_{1n}=B_{2n}$，$H_{1t}=H_{2t}$ |
| 非线性 | 铁电体 | 铁磁质（磁畴、磁滞、Curie 温度） |

表中的对应是形式上的：物理上与 $\boldsymbol{E}$ 对应的基本场是 $\boldsymbol{B}$（两者都出现在 **Lorentz 力**中），$\boldsymbol{D}$ 与 $\boldsymbol{H}$ 都是辅助量。顺磁质 $\chi_{\mathrm{m}}>0$ 且与温度成反比，抗磁质 $\chi_{\mathrm{m}}<0$ 且几乎与温度无关。

## 思考题

1. 为什么磁铁可以吸引未被磁化的铁块？
   提示：铁块在磁铁的非均匀磁场中被磁化，其磁矩与磁场同向，受力 $\nabla(\boldsymbol{m}\cdot\boldsymbol{B})$ 指向强场区。
2. 顺磁质和铁磁质的磁导率明显地依赖于温度，而抗磁质的磁导率几乎与温度无关，为什么？
   提示：顺磁性与铁磁性都是固有磁矩的取向有序，热运动破坏这种有序；抗磁性来自 Larmor 进动产生的感生磁矩，与分子的热运动无关。
3. 一根沿轴线均匀磁化的短圆柱形永磁体中没有传导电流，$\boldsymbol{H}$ 的环路定理给出 $\oint\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{l}=0$。能否由此断定 $\boldsymbol{H}=\boldsymbol{0}$？
   提示：不能。$\boldsymbol{H}$ 的环量为零，但它的散度 $-\nabla\cdot\boldsymbol{M}$ 在两个端面上不为零（相当于"磁荷"），磁体内外都有 $\boldsymbol{H}$，磁体内的 $\boldsymbol{H}$ 与 $\boldsymbol{M}$ 反向（退磁场）。
4. 铁磁体内为什么会存在磁畴？
   提示：见 §8.5.1，分成磁畴可以降低静磁能，畴壁要付出交换能，两者竞争。
5. 为什么变压器的铁芯用软磁材料，而永磁体用硬磁材料？
   提示：铁芯反复磁化，磁滞损耗正比于回线面积，要用窄回线的软磁材料；永磁体要求撤去外场后保留大的剩磁且不易被退磁，要用剩磁和矫顽力都大的硬磁材料。
