---
title: 原子中的电子
description: 氢原子光谱的规律与 Bohr 理论；氢原子的量子力学处理：角动量与空间量子化、能级与简并、电子云与径向概率分布；精细结构、Zeeman 效应、Stern–Gerlach 实验、电子自旋、自旋–轨道耦合与光谱项、碱金属能级；全同粒子、费米子与玻色子、Pauli 不相容原理、Fermi–Dirac 与 Bose–Einstein 分布；原子的电子排布；量子力学小结。
---

原子光谱是量子论的起点，也是检验量子力学的第一块试金石。从 1885 年 Balmer 总结出氢光谱的经验公式，到 1913 年 Bohr 的原子理论、1925—1926 年 Heisenberg 与 Born 的矩阵力学和 Schrödinger 的波动力学，再到 1927 年的**不确定关系**与第五届 Solvay 会议上的争论，量子力学的建立几乎都围绕着原子中的电子展开。本章先用上一章（[5.5.3](/5.5.3)）的方法求解氢原子：在球坐标中对**定态 Schrödinger 方程**分离变量，角向部分就是数学中的**球面调和函数**（[2.5.5](/2.5.5#sec-5.4.2)），径向部分给出能级；Bohr 理论的结果自动包含在其中。然后引入电子自旋（§4.2）与全同粒子的对称性（§4.3），由 Pauli 不相容原理解释元素周期表中的电子排布（§4.4）。§4.3 中的 Fermi–Dirac 分布与 Bose–Einstein 分布是 Maxwell–Boltzmann 统计（[5.2.1](/5.2.1)）的量子推广，[5.5.6](/5.5.6) 中的金属与半导体理论要用到它们；原子的电子结构也是化学中原子结构与化学键理论的物理基础。§4.5 总结整个量子力学部分。

## 4.1. 氢原子

### 4.1.1. 氢原子光谱的实验规律

氢原子是结构最简单的原子，它的光谱和电子能级直接相关。19 世纪中叶，Ångström 从氢放电管中测得了可见光区的几条谱线（红线 $656.3\,\mathrm{nm}$、蓝绿线 $486.1\,\mathrm{nm}$、两条紫线 $434.0\,\mathrm{nm}$ 与 $410.2\,\mathrm{nm}$，均为空气中的波长）。1885 年，瑞士的中学数学教师 Balmer 发现它们满足

$$
\lambda=B\frac{n^2}{n^2-4},\qquad n=3,4,5,\dots,\qquad B=364.56\,\mathrm{nm}.
$$
用波数 $\tilde\nu=1/\lambda$ 表示，就是 $\tilde\nu=\frac4B\big(\frac1{2^2}-\frac1{n^2}\big)$。Rydberg 把它推广为一般的形式。

**公式 4.1.1（Rydberg 公式）** 氢原子光谱的所有谱线的波数为

$$
\tilde\nu=\frac1\lambda=R\Big(\frac1{n_{\mathrm{f}}^2}-\frac1{n_{\mathrm{i}}^2}\Big),\qquad n_{\mathrm{f}}=1,2,3,\dots,\quad n_{\mathrm{i}}=n_{\mathrm{f}}+1,n_{\mathrm{f}}+2,\dots
\tag{4.1}
$$
其中 $R=4/B$ 称为 Rydberg 常量（Rydberg constant），氢的实验值为 $R_{\mathrm{H}}=1.096\,776\times10^7\,\mathrm{m^{-1}}$。

$n_{\mathrm{f}}$ 相同的谱线组成一个谱线系：

| $n_{\mathrm{f}}$ | 谱线系 | 波段 | 发现年份 |
|---|---|---|---|
| 1 | Lyman 系 | 紫外 | 1906—1914 |
| 2 | Balmer 系（Balmer series） | 可见光与近紫外 | 1885 |
| 3 | Paschen 系 | 红外 | 1908 |
| 4 | Brackett 系 | 红外 | 1922 |
| 5 | Pfund 系 | 红外 | 1924 |
| 6 | Humphreys 系 | 远红外 | 1953 |

每个谱线系在 $n_{\mathrm{i}}\to\infty$ 时趋于一个系限 $R/n_{\mathrm{f}}^2$。谱线的波数总是两项之差，这条"组合原则"暗示原子有一系列分立的能量状态，而光谱线来自状态之间的跃迁。

### 4.1.2. 原子模型的演变

19 世纪初 Dalton 把原子看作不可再分的实心小球。1897 年 J. J. Thomson 测出阴极射线粒子的荷质比，发现了电子，随后提出"葡萄干布丁"模型：电子镶嵌在均匀分布的正电荷之中。1909 年 Geiger 与 Marsden 用 α 粒子轰击金箔，发现少数 α 粒子被大角度散射，布丁模型无法解释；1911 年 Rutherford 据此提出核式结构模型：原子的全部正电荷和几乎全部质量集中在很小的原子核内，电子在核外绕核运动。

核式模型与经典电磁理论有根本的矛盾：绕核运动的电子有加速度，会不断辐射**电磁波**（[5.3.10](/5.3.10)），能量减少，按经典理论约 $10^{-11}\,\mathrm{s}$ 内就会螺旋落入原子核，并且辐射的频率连续变化。实际的原子却是稳定的，并且发出分立的谱线。

### 4.1.3. Bohr 理论

1913 年，Bohr 把 Planck 的量子假设用于 Rutherford 的核式模型，提出了氢原子的 Bohr 模型（Bohr model），后来称为旧量子论。

**性质 4.1.1（Bohr 的假设）**

1. 定态条件：电子只能在一些特定的圆轨道上绕核运动，此时原子处于具有确定能量的定态，不辐射电磁波；
2. 频率条件：原子从能量为 $E_{\mathrm{i}}$ 的定态跃迁到能量为 $E_{\mathrm{f}}$ 的定态时，发射（$E_{\mathrm{i}}>E_{\mathrm{f}}$）或吸收频率为 $\nu=\lvert E_{\mathrm{i}}-E_{\mathrm{f}}\rvert/h$ 的**光子**；
3. 量子化条件：定态轨道上电子的**角动量**是 $\hbar$ 的整数倍，$L=m_{\mathrm{e}}vr=n\hbar$，$n=1,2,3,\dots$

由 Coulomb 力提供向心力，$\frac{m_{\mathrm{e}}v^2}{r}=\frac{e^2}{4\pi\varepsilon_0r^2}$，与 $m_{\mathrm{e}}vr=n\hbar$ 联立，得轨道半径与能量

$$
r_n=n^2a_0,\quad a_0=\frac{4\pi\varepsilon_0\hbar^2}{m_{\mathrm{e}}e^2}=5.29\times10^{-11}\,\mathrm{m};\qquad E_n=-\frac{e^2}{8\pi\varepsilon_0r_n}=\frac{E_1}{n^2},\quad E_1=-\frac{m_{\mathrm{e}}e^4}{2(4\pi\varepsilon_0)^2\hbar^2}=-13.6\,\mathrm{eV}.
\tag{4.2}
$$
$a_0$ 称为 Bohr 半径（Bohr radius），它给出了原子大小的量级；$\lvert E_1\rvert=13.6\,\mathrm{eV}$ 是氢原子的电离能。由频率条件，从 $n_{\mathrm{i}}$ 跃迁到 $n_{\mathrm{f}}$ 发出的光的波数为

$$
\tilde\nu=\frac{E_{n_{\mathrm{i}}}-E_{n_{\mathrm{f}}}}{hc}=\frac{m_{\mathrm{e}}e^4}{8\varepsilon_0^2h^3c}\Big(\frac1{n_{\mathrm{f}}^2}-\frac1{n_{\mathrm{i}}^2}\Big),
$$
这正是 Rydberg 公式 (4.1)，并且给出了 Rydberg 常量的理论值 $R_\infty=\frac{m_{\mathrm{e}}e^4}{8\varepsilon_0^2h^3c}=1.097\,373\,157\times10^7\,\mathrm{m^{-1}}$。下标 $\infty$ 表示假定原子核不动（质量无穷大）；考虑原子核的运动，应把 $m_{\mathrm{e}}$ 换成电子与质子的**约化质量**（[5.1.4](/5.1.4)），$R_{\mathrm{H}}=R_\infty/(1+m_{\mathrm{e}}/m_{\mathrm{p}})=1.096\,776\times10^7\,\mathrm{m^{-1}}$，与光谱实验相符，剩下的相对差别只有 $10^{-5}$ 量级，来自精细结构等更小的效应（§4.2）。

![氢原子的能级 E_n = -13.6 eV/n² 与前四个谱线系：Lyman 系（跃迁到 n = 1，紫外）、Balmer 系（n = 2，可见光）、Paschen 系与 Brackett 系（n = 3、4，红外）](./plots/hydrogen-levels.py)

只有一个电子、核电荷数为 $Z$ 的离子（$\ce{He+}$、$\ce{Li^2+}$、$\ce{Be^3+}$ 等）称为类氢离子，把上面的 $e^2$ 换成 $Ze^2$，得 $r_n=n^2a_0/Z$，$E_n=-13.6\,\mathrm{eV}\cdot Z^2/n^2$。

对 Bohr 理论可以这样评价。它成功地算出了氢原子和类氢离子光谱的波长，但不能给出谱线的强度，也不能解释精细结构和多电子原子（甚至只有两个电子的氦）的光谱。它在逻辑上也不自洽：一方面用经典力学计算圆轨道，另一方面又硬性规定加速运动的电子不辐射；角动量量子化条件是人为加上的；它也没有说明电子在两个定态之间跃迁的过程（Rutherford 曾问：电子怎么"事先知道"要跳到哪个轨道上去？）。尽管如此，Bohr 理论中的定态、能级、频率条件与角动量量子化至今仍是正确的概念，只有确定的电子轨道这一图像被量子力学否定。Bohr 因此获得 1922 年的诺贝尔物理学奖，他在哥本哈根建立的研究所成为量子力学的中心。

### 4.1.4. 氢原子的量子力学处理

氢原子中的电子在原子核的 Coulomb 场中运动，势能 $U(r)=-\frac{e^2}{4\pi\varepsilon_0r}$ 只与距离有关（有心力场）。定态 Schrödinger 方程为

$$
-\frac{\hbar^2}{2m_{\mathrm{e}}}\nabla^2\psi-\frac{e^2}{4\pi\varepsilon_0r}\psi=E\psi.
$$
势能是球对称的，所以用球坐标 $(r,\theta,\varphi)$。**Laplace 算子**在球坐标中可以写成（[2.5.5](/2.5.5#sec-5.1.1)）

$$
\nabla^2=\frac1{r^2}\frac{\partial}{\partial r}\Big(r^2\frac{\partial}{\partial r}\Big)-\frac{\hat L^2}{\hbar^2r^2},\qquad
\hat L^2=-\hbar^2\Big[\frac1{\sin\theta}\frac{\partial}{\partial\theta}\Big(\sin\theta\frac{\partial}{\partial\theta}\Big)+\frac1{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2}\Big],
$$
其中 $\hat L^2$ 是轨道角动量平方 $\hat{\boldsymbol{L}}^2=(\hat{\boldsymbol{r}}\times\hat{\boldsymbol{p}})^2$ 的算符，只作用于角度。角动量 $z$ 分量的算符为 $\hat L_z=-\mathrm{i}\hbar\,\partial/\partial\varphi$。用**分离变量法**，令 $\psi(r,\theta,\varphi)=R(r)Y(\theta,\varphi)$，方程分为角向与径向两部分。

先看角向部分。$\hat L_z$ 的本征方程 $-\mathrm{i}\hbar\,\mathrm{d}\Phi/\mathrm{d}\varphi=L_z\Phi$ 的解是 $\Phi=\mathrm{e}^{\mathrm{i}L_z\varphi/\hbar}$；**波函数**必须单值，$\Phi(\varphi+2\pi)=\Phi(\varphi)$，所以 $L_z=m_l\hbar$，$m_l$ 为整数。$\hat L^2$ 与 $\hat L_z$ 有共同的**本征函数**，它们的本征方程

$$
\hat L^2Y=\lambda\hbar^2Y,\qquad \hat L_zY=m_l\hbar Y
$$
正是 [2.5.5](/2.5.5#sec-5.4.2) 中球面上的**特征值**问题：在两极处有界的解只在 $\lambda=l(l+1)$、$l\ge\lvert m_l\rvert$ 时存在，解是**球面调和函数** $Y_l^{m_l}(\theta,\varphi)\propto P_l^{\lvert m_l\rvert}(\cos\theta)\,\mathrm{e}^{\mathrm{i}m_l\varphi}$（$P_l^{\lvert m_l\rvert}$ 是**连带 Legendre 函数**）。球面调和函数在球面上正交归一：$\int Y_l^{m*}Y_{l'}^{m'}\,\mathrm{d}\Omega=\delta_{ll'}\delta_{mm'}$。例如

$$
Y_0^0=\frac1{\sqrt{4\pi}},\qquad Y_1^0=\sqrt{\frac3{4\pi}}\cos\theta,\qquad Y_1^{\pm1}=\mp\sqrt{\frac3{8\pi}}\sin\theta\,\mathrm{e}^{\pm\mathrm{i}\varphi}.
$$

**定理 4.1.1（轨道角动量的量子化）** 在有心力场中，电子轨道角动量的大小与 $z$ 分量只能取

$$
L=\sqrt{l(l+1)}\,\hbar,\quad l=0,1,2,\dots;\qquad L_z=m_l\hbar,\quad m_l=0,\pm1,\dots,\pm l.
\tag{4.3}
$$

对给定的 $l$，$L_z$ 有 $2l+1$ 个可能的值，即角动量在空间的取向只有 $2l+1$ 种（$\cos\theta=m_l/\sqrt{l(l+1)}$），这称为空间量子化（space quantization）。例如 $l=2$ 时 $L=\sqrt6\,\hbar$，$L_z=0,\pm\hbar,\pm2\hbar$，共 5 种取向。因为 $\lvert L_z\rvert<L$（$l\ge1$ 时），$\boldsymbol{L}$ 不可能精确地沿 $z$ 轴；$L_x$、$L_y$ 不确定，$\boldsymbol{L}$ 可以想象成分布在以 $z$ 轴为对称轴的圆锥面上。

再看径向部分。代入 $\psi=RY_l^{m_l}$，得径向方程

$$
-\frac{\hbar^2}{2m_{\mathrm{e}}}\frac1{r^2}\frac{\mathrm{d}}{\mathrm{d}r}\Big(r^2\frac{\mathrm{d}R}{\mathrm{d}r}\Big)+\Big[\frac{l(l+1)\hbar^2}{2m_{\mathrm{e}}r^2}-\frac{e^2}{4\pi\varepsilon_0r}\Big]R=ER.
$$
方括号中的第一项是"离心势能"，整个方括号就是经典有心力问题中的**有效势能** $\frac{L^2}{2mr^2}+U(r)$（[5.1.4](/5.1.4)），只是 $L^2$ 换成了 $l(l+1)\hbar^2$。求 $E<0$ 的**束缚态**解，并要求 $R$ 在 $r=0$ 处有限、在 $r\to\infty$ 时趋于零，得到：

**定理 4.1.2（氢原子的能级）** 氢原子的束缚态能量只能取

$$
E_n=-\frac{m_{\mathrm{e}}e^4}{2(4\pi\varepsilon_0)^2\hbar^2}\frac1{n^2}=-\frac{13.6\,\mathrm{eV}}{n^2},\qquad n=1,2,3,\dots,
\tag{4.4}
$$
并且角量子数必须满足 $l\le n-1$。

这与 Bohr 理论的结果 (4.2) 完全相同，但这里的量子化是方程与标准条件的自然结果，不是硬加的假设。径向函数 $R_{nl}$ 有 $n-l-1$ 个节点，前几个为

$$
R_{10}=\frac2{a_0^{3/2}}\mathrm{e}^{-r/a_0},\qquad
R_{20}=\frac1{2\sqrt2\,a_0^{3/2}}\Big(2-\frac r{a_0}\Big)\mathrm{e}^{-r/(2a_0)},\qquad
R_{21}=\frac1{2\sqrt6\,a_0^{3/2}}\frac r{a_0}\mathrm{e}^{-r/(2a_0)}.
$$

**定义 4.1.1（量子数）** 氢原子中电子的定态 $\psi_{nlm_l}=R_{nl}(r)Y_l^{m_l}(\theta,\varphi)$ 由三个量子数确定：

| 量子数 | 取值 | 决定 |
|---|---|---|
| **主量子数** $n$ | $1,2,3,\dots$ | 能量 $E_n=-13.6\,\mathrm{eV}/n^2$ |
| **角量子数**（轨道量子数）$l$ | $0,1,\dots,n-1$ | 轨道角动量的大小 $L=\sqrt{l(l+1)}\hbar$ |
| **磁量子数** $m_l$ | $0,\pm1,\dots,\pm l$ | 轨道角动量的 $z$ 分量 $L_z=m_l\hbar$ |

能量只与主量子数有关：同一个 $n$ 下有 $\sum_{l=0}^{n-1}(2l+1)=n^2$ 个不同的状态，能量却相同。几个线性无关的状态具有同一能量，称为能级的简并（degeneracy），这些状态称为简并态。$m_l$ 的简并来自势场的球对称性（空间没有特殊方向）；$l$ 的简并是 Coulomb 势 $1/r$ 特有的，在碱金属等多电子原子中被解除（§4.2.5）。按光谱学的习惯，$l=0,1,2,3,\dots$ 的状态记作 s、p、d、f、…，与主量子数合写为 1s、2s、2p、3d 等。

### 4.1.5. 电子云与概率分布

量子力学中，电子没有确定的轨道，只能给出它在各处出现的概率。$\lvert\psi_{nlm_l}(r,\theta,\varphi)\rvert^2$ 是电子在 $(r,\theta,\varphi)$ 处出现的概率密度；用小点的疏密表示这一分布，就得到形象的电子云（electron cloud）图。化学中把单电子的空间波函数 $\psi_{nlm_l}$ 称为原子轨道（atomic orbital），这里的"轨道"指一种概率分布，而不是 Bohr 模型中的圆轨道。由于 $R$ 与 $Y$ 分别归一化，

$$
\int\lvert\psi\rvert^2\,\mathrm{d}V=\int_0^\infty\lvert R_{nl}\rvert^2r^2\,\mathrm{d}r\int\lvert Y_l^{m_l}\rvert^2\,\mathrm{d}\Omega=1,\qquad \mathrm{d}\Omega=\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi.
$$

先看角向分布。电子出现在 $(\theta,\varphi)$ 方向的立体角 $\mathrm{d}\Omega$ 内的概率为 $\lvert Y_l^{m_l}\rvert^2\mathrm{d}\Omega$，它与 $\varphi$ 无关，所以电子云总是绕 $z$ 轴旋转对称的。s 电子（$l=0$）的分布是球对称的；p 电子中，$m_l=0$ 的 $\lvert Y_1^0\rvert^2\propto\cos^2\theta$ 集中在 $z$ 轴两侧，$m_l=\pm1$ 的 $\lvert Y_1^{\pm1}\rvert^2\propto\sin^2\theta$ 集中在 $xy$ 平面附近。

**定义 4.1.2（径向概率密度）** 电子出现在半径 $r$ 到 $r+\mathrm{d}r$ 的球壳内的概率为 $P_{nl}(r)\,\mathrm{d}r$，

$$
P_{nl}(r)=\lvert R_{nl}(r)\rvert^2r^2
$$
称为**径向概率密度**。

![氢原子 n = 1、2、3 各状态的径向概率密度 r²R_nl²（以 a_0 为长度单位）。l = n - 1 的状态只有一个极大，位于 r = n²a_0，即 Bohr 模型的轨道半径；其他状态有 n - l - 1 个节点](./plots/radial-distribution.py)

对基态 1s，$P_{10}=\frac{4r^2}{a_0^3}\mathrm{e}^{-2r/a_0}$ 在 $r=a_0$ 处取极大：电子最可能出现在 Bohr 半径处的单位厚度球壳内，但它在任何半径上都有出现的概率（平均半径为 $\frac32a_0$）。一般地，$l=n-1$ 的状态（2p、3d、…）只有一个极大，恰在 $r=n^2a_0$ 处，这就是 Bohr 轨道在量子力学中的对应。同一 $n$ 下 $l$ 越小，径向分布的内侧小峰越靠近原子核，这一点对多电子原子的能级很重要（§4.2.5）。

## 4.2. 电子自旋与自旋–轨道耦合

### 4.2.1. 精细结构与 Zeeman 效应

用分辨率更高的光谱仪观察，原子的许多谱线是由两条或多条靠得很近的谱线组成的，这称为光谱的精细结构（fine structure）。最著名的是钠的黄色 D 线，它是波长 $589.0\,\mathrm{nm}$ 与 $589.6\,\mathrm{nm}$ 的双线。只用三个量子数 $(n,l,m_l)$ 无法解释精细结构。

另一个线索来自磁场。绕核运动的电子相当于一个圆电流，有轨道**磁矩**。经典地，电荷 $-e$、质量 $m_{\mathrm{e}}$ 的轨道运动的磁矩与角动量成正比，$\boldsymbol{\mu}=-\frac{e}{2m_{\mathrm{e}}}\boldsymbol{L}$（[5.3.8](/5.3.8)）；量子力学中这一关系仍成立，于是 $\mu_z=-m_l\mu_{\mathrm{B}}$。

**定义 4.2.1（Bohr 磁子）** 常量

$$
\mu_{\mathrm{B}}=\frac{e\hbar}{2m_{\mathrm{e}}}=9.274\times10^{-24}\,\mathrm{J/T}=5.788\times10^{-5}\,\mathrm{eV/T}
$$
称为 **Bohr 磁子**，它是原子磁矩的自然单位。

在沿 $z$ 方向的外磁场 $\boldsymbol{B}$ 中，磁矩的附加能量为

$$
E_B=-\boldsymbol{\mu}\cdot\boldsymbol{B}=m_l\mu_{\mathrm{B}}B,\qquad m_l=0,\pm1,\dots,\pm l,
$$
一个能级分裂成 $2l+1$ 个等间距的能级，相应地一条谱线分裂成几条。把光源放在强磁场中，谱线分裂为几条靠近的谱线，这称为 Zeeman 效应（Zeeman effect），由 Zeeman 于 1896 年发现。在 $1\,\mathrm{T}$ 的磁场中，分裂的间隔 $\mu_{\mathrm{B}}B$ 只有约 $6\times10^{-5}\,\mathrm{eV}$。由于跃迁只发生在 $\Delta m_l=0,\pm1$ 的能级之间，上述理论预言每条谱线分裂为三条（正常 Zeeman 效应）。但 1897 年 Preston 就发现，多数谱线的分裂条数并非如此，间隔也各不相同（反常 Zeeman 效应），这同样需要新的**自由度**来解释。

### 4.2.2. Stern–Gerlach 实验

1922 年，Stern 与 Gerlach 用原子束直接检验角动量的空间量子化，这就是 Stern–Gerlach 实验（Stern–Gerlach experiment）。在沿 $z$ 方向不均匀的磁场中，磁矩的势能 $-\mu_zB_z$ 随位置变化，原子受力

$$
F_z=\mu_z\frac{\partial B_z}{\partial z}.
$$
若 $\mu_z$ 只能取几个分立的值，原子束经过磁场后就分裂成几束，在屏上沉积成分立的几条，而不是经典预言的连续的一片。实验中，银原子束确实分成了上下两束，证明了空间量子化的存在；分离出特定状态的原子束，至今仍是原子物理中常用的"态选择"技术。

但结果也带来了新的矛盾。银原子的最外层只有一个 5s 电子，内层电子的角动量与磁矩全部抵消，原子的轨道角动量 $l=0$，$\mu_z$ 应只有 0 一个值，原子束不应分裂；即使轨道角动量不为零，分裂的条数 $2l+1$ 也是奇数，而不是 2。氢原子基态的同类实验（1927 年）也得到两束。这说明用 $(n,l,m_l)$ 描述原子中的电子是不完备的。

### 4.2.3. 电子自旋

1925 年，Uhlenbeck 与 Goudsmit 提出：电子除轨道运动外，还有固有的角动量，即自旋，以及与之相联系的自旋磁矩；电子带负电，自旋磁矩与自旋角动量方向相反。

把电子看作自转的小球，这一图像是不能成立的：取经典电子半径 $2.8\times10^{-15}\,\mathrm{m}$，要得到 $\hbar/2$ 量级的角动量，球面的速率要达到光速的几十倍。电子自旋没有经典的对应，它是电子的内禀性质，就像质量和电荷一样。量子力学中所有角动量服从相同的量子化规则，所以可以与轨道角动量类比。

**定义 4.2.2（电子自旋）** 电子固有的角动量 $\boldsymbol{S}$ 称为**电子自旋**。它的大小与 $z$ 分量为

$$
S=\sqrt{s(s+1)}\,\hbar=\frac{\sqrt3}2\hbar,\qquad S_z=m_s\hbar,\quad m_s=\pm\frac12,
$$
其中 $s=\frac12$ 称为**自旋量子数**，$m_s$ 称为**自旋磁量子数**。

类比 $m_l$ 有 $2l+1$ 个值，$m_s$ 应有 $2s+1$ 个值；Stern–Gerlach 实验显示只有两个，所以 $2s+1=2$，$s=\frac12$ 不是整数。自旋磁矩的 $z$ 分量为 $\mu_{s,z}=-g_{\mathrm{e}}m_s\mu_{\mathrm{B}}\approx\mp\mu_{\mathrm{B}}$，$g_{\mathrm{e}}\approx2.002$（[5.3.8](/5.3.8#sec-8.2.2)）：自旋的磁矩与角动量之比是轨道的两倍。银原子在磁场中分成两束，正是 5s 电子 $m_s=\pm\frac12$ 的两种取向。1928 年，Dirac 的相对论量子力学从理论上导出了电子自旋和 $g_{\mathrm{e}}=2$。

### 4.2.4. 自旋–轨道耦合与光谱项

电子同时有轨道角动量 $\boldsymbol{L}$ 和自旋角动量 $\boldsymbol{S}$，电子的状态与总角动量

$$
\boldsymbol{J}=\boldsymbol{L}+\boldsymbol{S}
$$
有关。两种角动量的合成源于它们之间的磁相互作用（见下），称为自旋–轨道耦合（spin–orbit coupling）。$\boldsymbol{J}$ 也是量子化的：

$$
J=\sqrt{j(j+1)}\,\hbar,\qquad j=l\pm\frac12\ (l\ge1),\quad j=\frac12\ (l=0);\qquad J_z=m_j\hbar,\quad m_j=-j,\dots,j,
$$
$j$ 称为总角动量量子数。例如 $l=1$ 时 $L=\sqrt2\hbar$，$j=\frac32$ 或 $\frac12$，$J=\frac{\sqrt{15}}2\hbar$ 或 $\frac{\sqrt3}2\hbar$；在经典的矢量模型中，$\boldsymbol{L}$ 与 $\boldsymbol{S}$ 大致"平行"或"反平行"。

**定义 4.2.3（光谱项）** 原子的能量状态用符号

$$
n\,{}^{2s+1}L_j
$$
表示，称为**光谱项**。其中 $n$ 是主量子数；$L$ 是轨道角量子数的代号，$l=0,1,2,3,\dots$ 分别写作 $\mathrm{S},\mathrm{P},\mathrm{D},\mathrm{F},\dots$（直立的大写字母）；左上标 $2s+1$ 是自旋多重度，右下标是 $j$。

例如 $n=3$、$l=1$、$s=\frac12$、$j=\frac32$ 的状态写作 $3\,{}^2\mathrm{P}_{3/2}$。对单个价电子，$2s+1=2$（双重态）。多电子原子中，光谱项的 $L$、$S$、$J$ 是各电子合成的总角量子数、总自旋量子数和总角动量量子数（LS 耦合），记号相同。

### 4.2.5. 碱金属原子的能级

锂、钠、钾等碱金属原子的最外层只有一个价电子，内层电子与原子核组成一个净电荷为 $+e$ 的原子实（atomic core）。这种结构与氢原子相似，所以碱金属的光谱也与氢相似；不同的是，它们的能级不仅与 $n$ 有关，还与 $l$ 有关。原因有二：

- 轨道贯穿：$l$ 小的电子（尤其是 s 电子）的径向分布有伸入原子实内部的小峰（§4.1.5 的图），在那里它感受到的核电荷大于 $+e$，能量因而降低。
- 原子实极化：价电子排斥原子实中的电子，使原子实中负电荷的中心偏离原子核，原子实成为一个指向价电子的**电偶极子**，对价电子产生附加的吸引，能量也降低。

两种效应都使价电子感受到更多的正电荷，能量低于氢原子同一 $n$ 的能级。碱金属的能级常写成

$$
E_{nl}=-\frac{13.6\,\mathrm{eV}}{(n-\Delta_l)^2},
$$
$\Delta_l$ 称为量子数亏损（quantum defect），$l$ 越小越大。钠的 $\Delta_{\mathrm{s}}\approx1.37$、$\Delta_{\mathrm{p}}\approx0.88$、$\Delta_{\mathrm{d}}\approx0.01$；由此算出钠基态 3s 的电离能 $13.6/(3-1.37)^2\,\mathrm{eV}\approx5.1\,\mathrm{eV}$，与实验值 $5.14\,\mathrm{eV}$ 相符。d 电子几乎不贯穿原子实，能级与氢几乎相同。

精细结构来自自旋–轨道耦合。在电子的参考系中，原子核绕电子运动，产生磁场 $\boldsymbol{B}$。电子的自旋磁矩在这个磁场中有附加能量 $E_{\mathrm{so}}=-\boldsymbol{\mu}_s\cdot\boldsymbol{B}\approx\pm\mu_{\mathrm{B}}B$（自旋–轨道耦合能，它是一种相对论效应），所以 $l\ge1$ 的每个能级按 $j=l\pm\frac12$ 分裂成两个，对应的谱线也分成两条。钠的 3P 能级分裂为 $3\,{}^2\mathrm{P}_{3/2}$ 与 $3\,{}^2\mathrm{P}_{1/2}$，跃迁到基态 $3\,{}^2\mathrm{S}_{1/2}$（$l=0$，不分裂）分别发出 D2 线（$589.0\,\mathrm{nm}$）和 D1 线（$589.6\,\mathrm{nm}$）。两者的能量差为

$$
\Delta E=hc\Big(\frac1{\lambda_2}-\frac1{\lambda_1}\Big)\approx2.1\times10^{-3}\,\mathrm{eV},
$$
相当于价电子处在约 $18\,\mathrm{T}$ 的内部磁场中。精细结构的分裂随原子序数迅速增大：氢原子 $n=2$ 能级的分裂只有 $4.5\times10^{-5}\,\mathrm{eV}$。碱金属的双线也是 Uhlenbeck 与 Goudsmit 提出自旋假设的依据之一。

## 4.3. 全同粒子与 Pauli 不相容原理

### 4.3.1. 微观粒子的全同性

**定义 4.3.1（全同粒子）** 质量、电荷、自旋等固有属性完全相同的微观粒子称为**全同粒子**，如所有的电子、所有的质子。

经典粒子即使完全相同，也可以按各自的轨道追踪而加以区分。量子粒子没有确定的轨道，两个电子的波函数一旦重叠，就无法分辨哪个是哪个：全同粒子是不可分辨的。因此交换两个粒子，系统的物理状态不变，概率密度不变：

$$
\lvert\psi(1,2)\rvert^2=\lvert\psi(2,1)\rvert^2,
$$
其中 1、2 代表两个粒子的全部坐标（位置与自旋）。由此 $\psi(2,1)=\pm\psi(1,2)$：全同粒子系统的波函数只能是交换对称的（取 $+$）或交换反对称的（取 $-$）。

用单粒子波函数构造两粒子系统的波函数：设单粒子状态为 $A$、$B$，则 $\psi_A(1)\psi_B(2)$ 与 $\psi_A(2)\psi_B(1)$ 都满足两粒子的 **Schrödinger 方程**（不计相互作用时），但都没有确定的交换对称性。由于两者出现的概率相等，体系的波函数应是它们的等权叠加：

$$
\psi_{\mathrm{S}}(1,2)=\frac1{\sqrt2}\big[\psi_A(1)\psi_B(2)+\psi_A(2)\psi_B(1)\big],\qquad
\psi_{\mathrm{A}}(1,2)=\frac1{\sqrt2}\big[\psi_A(1)\psi_B(2)-\psi_A(2)\psi_B(1)\big].
$$

### 4.3.2. 费米子与玻色子

**定义 4.3.2** 自旋量子数 $s$ 为半整数（$\frac12,\frac32,\dots$）的粒子称为**费米子**，它们组成的系统的波函数是交换反对称的；$s$ 为零或整数的粒子称为**玻色子**，它们组成的系统的波函数是交换对称的。

自旋与对称性之间的这种联系是实验事实，Pauli 于 1940 年从相对论量子场论证明了它（自旋–统计定理）。$s=\frac12$ 的费米子有电子、质子、中子、中微子、μ 子、夸克，以及 $\ce{^3He}$ 原子核；$\Delta$ 重子的 $s=\frac32$。玻色子有光子（$s=1$）、π 介子与 K 介子（$s=0$）、$\ce{^4He}$ 原子核（$s=0$）、氘核（$s=1$）等。由偶数个费米子组成的复合粒子是玻色子，由奇数个组成的是费米子，所以 $\ce{^4He}$ 原子是玻色子，$\ce{^3He}$ 原子是费米子，两种液氦在低温下的性质截然不同。

**定理 4.3.1（Pauli 不相容原理）** 两个（或更多）全同的费米子不能处于同一个单粒子状态。

**证明** 令 $A=B$，反对称波函数 $\psi_{\mathrm{A}}(1,2)=\frac1{\sqrt2}[\psi_A(1)\psi_A(2)-\psi_A(2)\psi_A(1)]=0$，即这样的状态不存在。$N$ 个费米子的反对称波函数可以写成以 $\psi_{A_i}(j)$ 为元素的行列式（Slater 行列式），两个单粒子状态相同时有两行相同，行列式为零。$\square$

玻色子的对称波函数在 $A=B$ 时不为零，任意多个玻色子可以占据同一个单粒子状态，不受不相容原理的限制，而且全同玻色子倾向于聚集在同一状态。光子是玻色子，大量光子可以处在同一状态，形成宏观的经典光波，激光（[5.5.5](/5.5.5)）就是这样的状态；电子是费米子，不能大量聚集在同一状态，所以没有"经典的电子波"，电子的**干涉**只能以单个电子的**概率幅**干涉的形式出现。

反对称性还使自旋平行的两个电子在空间上互相回避，从而影响它们的静电相互作用能。这种纯量子的"交换作用"是共价键、Hund 规则（§4.4.3）和铁磁性（[5.3.8](/5.3.8)）的根源。

### 4.3.3. Fermi–Dirac 统计与 Bose–Einstein 统计

经典的 Maxwell–Boltzmann 统计把粒子看作可以分辨的。考虑全同性与不相容原理之后，量子统计给出了平衡态下粒子在各单粒子状态上的平均数目。

**定理 4.3.2（Fermi–Dirac 分布）** 温度为 $T$ 的平衡态下，由全同费米子组成的**理想气体**中，能量为 $E$ 的一个单粒子状态上的平均粒子数为

$$
\bar N(E)=\frac1{\mathrm{e}^{(E-\mu)/(k_{\mathrm{B}}T)}+1},
\tag{4.5}
$$
其中化学势 $\mu=\mu(T)$ 由粒子总数确定。

由于不相容原理，$0\le\bar N\le1$。$T=0$ 时 $\bar N$ 是一个台阶：$E<\mu(0)$ 的状态全部被占据，$E>\mu(0)$ 的状态全部空着；$E_{\mathrm{F}}=\mu(0)$ 称为 Fermi 能量（[5.5.6](/5.5.6)）。温度不太高（$k_{\mathrm{B}}T\ll E_{\mathrm{F}}$）时 $\mu\approx E_{\mathrm{F}}$，热激发的能量只有 $k_{\mathrm{B}}T$ 的量级，只有 $E_{\mathrm{F}}$ 附近宽约 $k_{\mathrm{B}}T$ 的范围内的粒子能被激发到更高的状态，台阶的棱角被磨圆成一个过渡带；$k_{\mathrm{B}}T\gg E_{\mathrm{F}}$ 时台阶完全消失。金属中电子的 $E_{\mathrm{F}}$ 为几个电子伏特，远大于室温的 $k_{\mathrm{B}}T\approx0.026\,\mathrm{eV}$，所以室温下金属的电子气几乎处于 $T=0$ 的状态，这解释了经典理论无法说明的电子比热很小的事实。

**定理 4.3.3（Bose–Einstein 分布）** 在同样的条件下，由全同玻色子组成的理想气体中，能量为 $E$ 的一个单粒子状态上的平均粒子数为

$$
\bar N(E)=\frac1{\mathrm{e}^{(E-\mu)/(k_{\mathrm{B}}T)}-1}.
\tag{4.6}
$$

对所有状态都要求 $0\le\bar N<\infty$，所以 $\mu$ 必须小于最低的单粒子能量 $E_0$；取 $E_0=0$，则 $\mu<0$。粒子数密度一定时，温度降低，$\mu$ 从下方趋于 0，基态上的粒子数 $\bar N_0=1/(\mathrm{e}^{-\mu/(k_{\mathrm{B}}T)}-1)$ 迅速增大。理论表明，存在一个**临界温度** $T_{\mathrm{c}}$，

$$
k_{\mathrm{B}}T_{\mathrm{c}}=\frac{2\pi\hbar^2}{m}\Big(\frac{n}{2.612}\Big)^{2/3},
$$
低于 $T_{\mathrm{c}}$ 时，宏观数量的粒子聚集在同一个最低能量状态上，$T\to0$ 时全部粒子都处于基态。这种现象称为 Bose–Einstein 凝聚（Bose–Einstein condensation），简称 BEC，由 Einstein 于 1925 年预言。对稀薄原子气体，$T_{\mathrm{c}}$ 只有 $10^{-7}\,\mathrm{K}$ 的量级。1995 年 Cornell、Wieman 用激光冷却与蒸发冷却的铷原子、Ketterle 用钠原子分别实现了 BEC，三人获得 2001 年的诺贝尔物理学奖。BEC 中大量原子处在同一量子态，原子的**物质波**像激光一样相干，可以用来制作原子干涉仪和精密的量子频标；液氦的超流性也与 BEC 密切相关。

最后看经典极限。若 $E-\mu\gg k_{\mathrm{B}}T$，两种分布分母中的 $\pm1$ 都可以忽略：

$$
\bar N(E)\approx\mathrm{e}^{\mu/(k_{\mathrm{B}}T)}\,\mathrm{e}^{-E/(k_{\mathrm{B}}T)},
$$
这正是经典统计的 **Boltzmann 因子**，量子统计过渡到 Maxwell–Boltzmann 统计（**Boltzmann 分布**，[5.2.1](/5.2.1)）。这一条件等价于 $\bar N\ll1$：每个状态上平均远少于一个粒子，粒子很少有机会处在同一状态，全同性的影响也就可以忽略。定量地说，条件是粒子数密度 $n$ 与热 **de Broglie 波长** $\lambda_{\mathrm{th}}=h/\sqrt{2\pi mk_{\mathrm{B}}T}$ 满足 $n\lambda_{\mathrm{th}}^3\ll1$，即粒子的平均间距远大于它的 de Broglie 波长。常温常压下的氮气 $n\lambda_{\mathrm{th}}^3\approx2\times10^{-7}$，经典统计完全适用；金属中的自由电子质量小、密度大，室温下 $n\lambda_{\mathrm{th}}^3\sim10^4$，必须用 Fermi–Dirac 统计。

![左：Fermi–Dirac 分布在几个温度下的形状（取 μ ≈ E_F），T = 0 时是台阶，温度升高时 E_F 附近宽约 k_BT 的范围被磨圆；右：三种分布随 (E - μ)/k_BT 的变化（对数坐标），E - μ ≫ k_BT 时三者重合](./plots/quantum-statistics.py)

## 4.4. 原子的电子排布

### 4.4.1. 四个量子数

多电子原子中的每个电子，近似地可以看作在原子核与其他电子共同形成的平均有心力场中独立运动，它的状态由四个量子数 $(n,l,m_l,m_s)$ 完备地描述：

| 量子数 | 取值 | 物理意义 |
|---|---|---|
| 主量子数 $n$ | $1,2,3,\dots$ | 决定能量的主要因素 |
| 角量子数 $l$ | $0,1,\dots,n-1$ | 轨道角动量 $L=\sqrt{l(l+1)}\hbar$；对能量有重要影响，$l$ 小的能量低 |
| 磁量子数 $m_l$ | $0,\pm1,\dots,\pm l$ | $L_z=m_l\hbar$；引起磁场中能级的分裂 |
| 自旋磁量子数 $m_s$ | $\pm\frac12$ | $S_z=m_s\hbar$；产生精细结构 |

### 4.4.2. Pauli 不相容原理与壳层

把 Pauli 不相容原理用于原子中的电子，就是 Pauli 在 1925 年最初的表述：一个原子中不能有两个电子的四个量子数 $(n,l,m_l,m_s)$ 完全相同。

**定义 4.4.1** 原子中主量子数 $n$ 相同的电子状态组成一个**壳层**，$n=1,2,3,4,5,\dots$ 的壳层依次记作 K、L、M、N、O、…；$n$ 与 $l$ 都相同的状态组成一个**支壳层**（次壳层），依次记作 s、p、d、f、g、…

一个支壳层中 $m_l$ 有 $2l+1$ 个值、$m_s$ 有 2 个值，最多容纳 $2(2l+1)$ 个电子：s、p、d、f 支壳层分别为 2、6、10、14 个。第 $n$ 壳层最多容纳

$$
Z_n=\sum_{l=0}^{n-1}2(2l+1)=2n^2
$$
个电子：K、L、M、N 壳层分别为 2、8、18、32 个。原子中各支壳层上的电子数称为原子的电子组态（electron configuration），写成 $1\mathrm{s}^2\,2\mathrm{s}^2\,2\mathrm{p}^6\cdots$，右上角是该支壳层中的电子数。

### 4.4.3. 能量最低原理与 Hund 规则

基态原子中，电子在不违背不相容原理的前提下优先占据能量最低的状态，这称为能量最低原理（aufbau principle）。多电子原子中支壳层的能量既与 $n$ 有关，也与 $l$ 有关（§4.2.5 的轨道贯穿），所以填充顺序并不总是先填满一个壳层再填下一个：

$$
1\mathrm{s}<2\mathrm{s}<2\mathrm{p}<3\mathrm{s}<3\mathrm{p}<4\mathrm{s}<3\mathrm{d}<4\mathrm{p}<5\mathrm{s}<4\mathrm{d}<5\mathrm{p}<6\mathrm{s}<4\mathrm{f}<5\mathrm{d}<6\mathrm{p}<7\mathrm{s}<5\mathrm{f}<\cdots
$$
这一顺序可以用 Madelung 规则概括：按 $n+l$ 从小到大填充，$n+l$ 相同时先填 $n$ 小的。我国化学家徐光宪给出了另一个近似规则：支壳层的能量随 $n+0.7l$ 增大。例如 3d 的 $n+0.7l=4.4$，大于 4s 的 $4.0$，所以钾、钙的最后一个电子填入 4s 而不是 3d。由这一顺序还可以推出：任何壳层作为最外层时最多有 8 个电子，作为次外层时最多有 18 个。

Hund 规则（Hund's rule）：电子填入一组能量相同的简并轨道（如 3 个 2p 轨道）时，总是先以自旋平行的方式分别占据不同的轨道，然后才成对；这样做使总自旋最大、能量最低，其根源是 §4.3.2 的交换作用。例如氮原子 $1\mathrm{s}^2\,2\mathrm{s}^2\,2\mathrm{p}^3$ 的三个 2p 电子分占三个轨道，自旋平行。等价轨道全满（$\mathrm{p}^6$、$\mathrm{d}^{10}$、$\mathrm{f}^{14}$）、半满（$\mathrm{p}^3$、$\mathrm{d}^5$、$\mathrm{f}^7$）或全空时比较稳定（Hund 规则的特例），这解释了填充顺序的一些例外：

- 铬（$Z=24$）：$1\mathrm{s}^2\,2\mathrm{s}^2\,2\mathrm{p}^6\,3\mathrm{s}^2\,3\mathrm{p}^6\,3\mathrm{d}^5\,4\mathrm{s}^1$，即 $[\ce{Ar}]\,3\mathrm{d}^5\,4\mathrm{s}^1$，而不是按顺序的 $3\mathrm{d}^4\,4\mathrm{s}^2$；
- 铜（$Z=29$）：$[\ce{Ar}]\,3\mathrm{d}^{10}\,4\mathrm{s}^1$，而不是 $3\mathrm{d}^9\,4\mathrm{s}^2$。

元素周期表的结构就是这样形成的：每一周期从一个新的 s 支壳层开始，到 p 支壳层填满（稀有气体）结束；第 4、5 周期中间插入 d 支壳层（过渡元素），第 6、7 周期再插入 f 支壳层（镧系、锕系）。同一族元素有相同的价电子组态，因而有相似的化学性质。这是量子力学对化学最重要的贡献之一。

## 4.5. 量子力学小结

### 4.5.1. 基本概念与方法

量子力学部分（[5.5.1](/5.5.1)—本章）的主要内容可以归纳为：

- 两个重要概念：**波粒二象性**与量子化；
- 一个重要关系：**不确定关系**；
- 两个基本假设：波函数的统计解释与 Schrödinger 方程（[5.5.3](/5.5.3)）；
- 两个基本原理：**态叠加原理**与 Pauli 不相容原理；
- 一个关键常量：**Planck 常量** $h$；一个重要效应：**隧道效应**；
- 三个重要实验：电子在晶体上的**衍射**、电子的单缝衍射与双缝干涉、Stern–Gerlach 实验。

量子力学处理问题的方法是：

1. 体系的状态由波函数（概率幅）$\Psi$ 描述；
2. 力学量用 Hermite 算符表示，由经典力学量"算符化"得到（$\boldsymbol{p}\to-\mathrm{i}\hbar\nabla$），如**哈密顿量** $\hat H$、角动量 $\hat L^2$、$\hat L_z$；
3. 力学量 $A$ 的本征方程为 $\hat A\psi_n=A_n\psi_n$；根据波函数的标准条件解本征方程，求出**本征值** $A_n$ 与本征函数 $\psi_n$，力学量能取的值就是这些本征值；
4. 体系处于 $\hat A$ 的本征态时，测量 $A$ 得到确定的值 $A_n$；处于本征态的叠加 $\Psi=\sum_nC_n\psi_n$（$\psi_n$ 正交归一）时，测量得到 $A_n$ 的概率为 $\lvert C_n\rvert^2$，所以 $A$ 有确定的平均值

$$
\langle A\rangle=\sum_n\lvert C_n\rvert^2A_n=\int\Psi^*\hat A\Psi\,\mathrm{d}x.
$$

### 4.5.2. 量子物理与经典物理

当 $h\to0$（作用量远大于 $h$ 的宏观过程）或量子数 $n\to\infty$ 时，量子物理的结论趋于经典物理的结论，这就是**对应原理**（[5.5.3](/5.5.3)）。例如方势阱中粒子的能级在 $n\to\infty$ 时趋于连续、概率分布趋于均匀；不确定关系对宏观物体的影响远小于测量精度；大量子数的谐振子的概率分布趋于经典分布。量子力学并不否定经典物理，而是确定了它的适用范围。

### 4.5.3. 关于量子力学诠释的争论

以 Bohr、Heisenberg、Born、Pauli 为代表的哥本哈根学派认为：

1. 波动性与粒子性是互补的：两者不会出现在同一次测量中，但对完整地描述微观现象都是必需的，这称为互补原理（complementarity principle）；
2. 量子力学是统计性的理论，不确定关系是粒子波动性的表现，原则上不可避免；
3. 量子力学的现有形式及其诠释是完备的。

以 Einstein、de Broglie、Schrödinger 为代表的反对者则认为：波函数的统计诠释只对大量粒子组成的系综有意义（Einstein 说"上帝不掷骰子"），量子力学并不完备，应当进一步探索波与粒子统一的本质。

1930 年第六届 Solvay 会议上，Einstein 提出"光子箱"理想实验来反驳能量–时间不确定关系：箱中充满辐射，箱壁上的快门由箱内的钟控制，在准确的时刻打开极短的时间放出一个光子；称量光子放出前后箱子的质量，由**质能关系** $E=mc^2$ 就能精确地得到光子的能量，于是 $\Delta E$ 与 $\Delta t$ 似乎可以同时任意小。Bohr 经过一夜的思考给出了反驳：称量质量要测量箱子在引力场中的位置，位置的不确定使箱子的动量不确定；而按广义相对论，钟在引力场中的快慢与它的高度有关，位置的不确定又带来钟的读数的不确定，两者结合恰好给出 $\Delta E\,\Delta t\gtrsim h$。Einstein 此后不再质疑不确定关系的内在一致性，但始终认为量子力学不是最终的理论。

1935 年，Einstein、Podolsky 与 Rosen 用两个纠缠粒子的思想实验（EPR 佯谬）论证量子力学不完备。1964 年 Bell 证明，任何满足定域性的隐变量理论都必须服从一个不等式（Bell 不等式），而量子力学预言它在某些情况下被违反，这样哲学争论就变成了可以检验的问题。从 Clauser（1972）、Aspect（1982）到 2015 年堵住主要漏洞的实验，结果都违反 Bell 不等式而与量子力学一致，Aspect、Clauser 与 Zeilinger 因此获得 2022 年的诺贝尔物理学奖。对量子力学的诠释至今仍有不同的观点，但它们对一切可观测结果的预言相同，迄今没有任何实验与量子力学的预言相矛盾。

## 小结

| 内容 | 主要结论 |
|---|---|
| 氢原子 | $E_n=-13.6\,\mathrm{eV}/n^2$；$L=\sqrt{l(l+1)}\hbar$，$l\le n-1$；$L_z=m_l\hbar$，$\lvert m_l\rvert\le l$；能级简并度 $n^2$（计自旋为 $2n^2$） |
| 电子自旋 | $s=\frac12$，$S=\frac{\sqrt3}2\hbar$，$S_z=\pm\frac12\hbar$；$\mu_{\mathrm{B}}=e\hbar/(2m_{\mathrm{e}})$ |
| 自旋–轨道耦合 | $\boldsymbol{J}=\boldsymbol{L}+\boldsymbol{S}$，$j=l\pm\frac12$；光谱项 $n\,{}^{2s+1}L_j$；精细结构 |
| 全同粒子 | 费米子（半整数自旋）波函数反对称，服从 Pauli 不相容原理与 Fermi–Dirac 分布；玻色子（整数自旋）波函数对称，服从 Bose–Einstein 分布 |
| 电子排布 | 四个量子数 $(n,l,m_l,m_s)$；支壳层容纳 $2(2l+1)$、壳层容纳 $2n^2$ 个电子；能量最低原理与 Hund 规则 |

## 思考题

1. 为什么基态银原子（$l=0$）在 Stern–Gerlach 实验中分成两束而不是一束或三束？

   **答** 分裂来自 5s 价电子的自旋，$m_s=\pm\frac12$ 两种取向；轨道角动量引起的分裂条数 $2l+1$ 总是奇数。

2. 铜原子（$Z=29$）的核外电子如何排布？

   **答** $[\ce{Ar}]\,3\mathrm{d}^{10}\,4\mathrm{s}^1$，3d 全满比 $3\mathrm{d}^9\,4\mathrm{s}^2$ 更稳定。

3. 在氢原子中，主量子数为 $n$ 的能级（计自旋）有几个状态？在碱金属原子中，这些状态的能量还相同吗？

   **答** $2n^2$ 个。碱金属中不同 $l$ 的能级因轨道贯穿和原子实极化而分开，$l\ge1$ 的能级又因自旋–轨道耦合按 $j$ 分成两个。

4. 为什么室温下空气分子可以用经典统计处理，而金属中的电子不行？

   **答** 比较 $n\lambda_{\mathrm{th}}^3$；电子质量小、热波长大，金属中电子密度又高，$n\lambda_{\mathrm{th}}^3\gg1$。
