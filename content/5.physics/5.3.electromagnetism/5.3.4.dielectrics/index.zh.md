---
title: 静电场中的电介质
description: 电介质对电场的影响，位移极化与取向极化，极化强度、电极化率与极化电荷，电位移及其高斯定理，界面关系，电容器及其电容，有介质时的静电场能量。
---

前两章研究了真空中的静电场与**导体**：导体中有大量自由电荷，**静电平衡**时内部**场强**为零。本章研究另一类物质，即绝缘体，也称电介质。电介质中几乎没有自由电荷，但它的分子在电场中会被"拉长"或"转向"，在介质内部与表面出现不能自由移动的极化电荷；极化电荷的电场只能部分抵消外电场，于是介质中的场强减弱而不为零。描述这一现象需要两个新的宏观量：极化强度 $\boldsymbol{P}$ 与电位移 $\boldsymbol{D}$，后者使有介质时的**高斯定理**只含自由电荷。在此基础上讨论电容器（电介质最重要的应用）与有介质时的静电场能量。

数学上，极化电荷与 $\boldsymbol{P}$ 的关系是 **Gauss 公式**的直接应用（[2.2.14](/2.2.14)），各向异性介质的电极化率是一个**对称矩阵**；界面关系与上一章的边值问题（[5.3.3](/5.3.3)）一起决定有介质时的静电场。下一章 [5.3.5](/5.3.5) 转向运动的电荷，即恒定电流；磁介质（[5.3.8](/5.3.8)）的处理方法与本章完全平行。

## 4.1. 电介质对电场的影响

**定义 4.1.1（电介质）** 不导电的物质，即内部几乎没有可以自由移动的电荷的物质，称为**电介质**（绝缘体）。

演示实验：平行板电容器充电后与电源断开，极板电荷 $Q$ 保持不变，用静电计测极板间的电压。插入电介质后，静电计的张角减小；取出电介质，张角复原。若电介质充满极板间的空间，电压与场强都减小为原来的 $1/\varepsilon_{\mathrm{r}}$：

$$
U = \frac{U_0}{\varepsilon_{\mathrm{r}}},\qquad E = \frac{E_0}{\varepsilon_{\mathrm{r}}},
$$
其中 $\varepsilon_{\mathrm{r}}$ 是由电介质决定的常量，称为相对电容率（定义 4.3.2）。

**定义 4.1.2（电介质极化）** 电介质在电场作用下，内部或表面出现不能自由移动的电荷的现象称为**电介质极化**，这种电荷称为**极化电荷**（束缚电荷）。

与导体中的自由电荷不同，极化电荷被束缚在分子内，只能作微小的位移，它的电场不能完全抵消外电场，所以介质内的总场强减弱但不为零。

| 材料 | $\varepsilon_{\mathrm{r}}$ | 材料 | $\varepsilon_{\mathrm{r}}$ |
|---|---|---|---|
| 真空 | $1$（精确） | 玻璃 | $5$–$10$ |
| 空气（$20^\circ\mathrm{C}$，$1\,\mathrm{atm}$） | $1.00054$ | 云母 | $4$–$7$ |
| 煤油 | 约 $2$ | 水（$20^\circ\mathrm{C}$） | $80$ |
| 纸 | $2$–$4$ | 二氧化钛（金红石） | 约 $100$ |
| 甘油（$25^\circ\mathrm{C}$） | 约 $42$ | 钛酸钡 $\ce{BaTiO3}$ | $10^3$–$10^4$ |

钛酸钡这样 $\varepsilon_{\mathrm{r}}$ 极大的材料是铁电体（ferroelectrics），它的 $\boldsymbol{P}$ 与 $\boldsymbol{E}$ 不成线性关系并有电滞回线，与铁磁质（[5.3.8](/5.3.8)）相似。

## 4.2. 电介质的极化

### 4.2.1. 电介质的微观电结构

分子由原子核与电子云构成。考虑分子在远处产生的电场时，可以把分子中全部正电荷等效为位于"正电荷中心"的一个**点电荷** $q$，全部负电荷等效为位于"负电荷中心"的点电荷 $-q$。若负电荷中心指向正电荷中心的位矢为 $\boldsymbol{l}$，分子的**电偶极矩**为 $\boldsymbol{p} = q\boldsymbol{l}$。按无外场时这两个中心是否重合，电介质的分子分为两类：

**定义 4.2.1（有极分子与无极分子）** 无外场时正、负电荷中心重合、没有固有电偶极矩的分子称为**无极分子**（如 $\ce{He}$、$\ce{N2}$、$\ce{CH4}$、$\ce{CO2}$）；正、负电荷中心不重合、有固有电偶极矩的分子称为**有极分子**（如 $\ce{H2O}$、$\ce{NH3}$、$\ce{HCl}$）。

几种有极分子的固有电偶极矩（单位 $10^{-30}\,\mathrm{C\,m}$）：

| 分子 | $\ce{H2O}$ | $\ce{NH3}$ | $\ce{HCl}$ | $\ce{SO2}$ | $\ce{CO}$ | $\ce{C2H5OH}$ |
|---|---|---|---|---|---|---|
| $p$ | $6.2$ | $4.9$ | $3.6$ | $5.4$ | $0.37$ | $5.6$ |

化学中常用非 SI 单位 debye：$1\,\mathrm{D} \approx 3.336\times10^{-30}\,\mathrm{C\,m}$，如水分子 $p \approx 1.85\,\mathrm{D}$。分子是否有极取决于分子的几何构型：$\ce{CO2}$ 是直线形，两个 $\ce{C=O}$ 键的偶极矩抵消；$\ce{H2O}$ 是弯曲形，不能抵消。

### 4.2.2. 极化机制

**定义 4.2.2（位移极化与取向极化）** 在外电场作用下，分子的电子云相对原子核发生畸变，正、负电荷中心被拉开，产生沿外场方向的感生电偶极矩，这种极化称为**位移极化**（电子位移极化）；有极分子的固有电偶极矩受外电场的力矩作用而趋向沿外场方向排列，这种极化称为**取向极化**。

- 无极分子只有位移极化。感生电偶极矩与场强成正比、方向相同，无外场时为零。
- 有极分子无外场时，热运动使固有电偶极矩的取向随机分布，宏观上不显电性；有外场时，力矩 $\boldsymbol{p}\times\boldsymbol{E}$ 使它们趋向外场方向，而热运动阻碍这种排列，所以取向极化与温度有关。有极分子同时也有位移极化，但在静电场中取向极化是主要的。
- 离子晶体（如 $\ce{NaCl}$、$\ce{BaTiO3}$）中，正、负离子在电场作用下发生相对位移，也产生感生电偶极矩，称为离子位移极化。

三种机制的宏观效果相同：电介质端面出现极化电荷。

### 4.2.3. 极化过程

极化是一个自洽的平衡过程。外电场 $\boldsymbol{E}_0$（由自由电荷产生）使介质极化，极化电荷激发附加电场 $\boldsymbol{E}'$，按**场强叠加原理**，介质中的总场为

$$
\boldsymbol{E} = \boldsymbol{E}_0 + \boldsymbol{E}'.
$$
总场 $\boldsymbol{E}$ 又决定极化的程度，产生新的极化电荷与新的 $\boldsymbol{E}'$，如此反复，直到静电平衡。决定介质极化的是总场 $\boldsymbol{E}$，而不是外场 $\boldsymbol{E}_0$。这里忽略了 $\boldsymbol{E}'$ 对外场源电荷分布的反作用；当外场源是导体时，这种反作用一般不能忽略，需要联立求解（例 4.5.1）。

### 4.2.4. 极化强度

**定义 4.2.3（极化强度）** 介质中某点附近体积元 $\Delta V$ 内所有分子电偶极矩的矢量和除以 $\Delta V$，

$$
\boldsymbol{P} = \frac{\sum_i \boldsymbol{p}_i}{\Delta V},
$$
称为该点的**极化强度**，单位 $\mathrm{C\,m^{-2}}$，与面**电荷密度**的量纲相同。$\Delta V$ 要宏观上小（远小于 $\boldsymbol{P}$ 发生变化的尺度）、微观上大（远大于分子间距）。

若单位体积内有 $n$ 个分子，每个分子的平均电偶极矩为 $\boldsymbol{p}$，则 $\boldsymbol{P} = n\boldsymbol{p}$。$\boldsymbol{P}$ 既反映分子电偶极矩的大小，也反映它们排列的有序程度，可以看作电介质对总电场 $\boldsymbol{E}$ 的响应。

### 4.2.5. 电介质的极化规律

**定义 4.2.4（电极化率）** 场强不太强时，$\boldsymbol{P}$ 与 $\boldsymbol{E}$ 成线性关系，这样的电介质称为**线性电介质**。对各向同性的线性电介质，

$$
\boldsymbol{P} = \varepsilon_0\chi_{\mathrm{e}}\boldsymbol{E} = \varepsilon_0(\varepsilon_{\mathrm{r}} - 1)\boldsymbol{E},\qquad \varepsilon_{\mathrm{r}} = 1 + \chi_{\mathrm{e}},
$$
比例系数 $\chi_{\mathrm{e}}$ 称为**电极化率**。$\chi_{\mathrm{e}}$ 与 $\varepsilon_{\mathrm{r}}$ 都是量纲一的量，$\chi_{\mathrm{e}} > 0$，所以 $\boldsymbol{P}$ 与 $\boldsymbol{E}$ 同向。

对各向异性的线性电介质（如许多晶体），$\boldsymbol{P}$ 的每个分量是 $\boldsymbol{E}$ 各分量的线性组合：

$$
\begin{bmatrix} P_x \\ P_y \\ P_z \end{bmatrix}
= \varepsilon_0
\begin{bmatrix}
\chi_{xx} & \chi_{xy} & \chi_{xz} \\
\chi_{yx} & \chi_{yy} & \chi_{yz} \\
\chi_{zx} & \chi_{zy} & \chi_{zz}
\end{bmatrix}
\begin{bmatrix} E_x \\ E_y \\ E_z \end{bmatrix},
$$
电极化率是一个二阶张量，可以证明它是**对称矩阵**（由能量的存在性）。按**谱定理**，总可以选一组正交的坐标轴（晶体的主轴）使它对角化，三个**特征值**就是沿三个主轴的电极化率。一般情况下 $\boldsymbol{P}$ 与 $\boldsymbol{E}$ 不平行：介质沿不同方向的极化程度不同，这与晶体的结构和对称性有关。光学中的双折射（[5.4.3](/5.4.3)）就来源于这种各向异性。以下只讨论各向同性的线性电介质。

### 4.2.6. 极化电荷

在已极化的介质中任作一闭合曲面 $S$，计算 $S$ 所围体积 $V$ 内的极化电荷。完全在 $V$ 内或完全在 $V$ 外的分子对 $V$ 内的净电荷没有贡献，只有被 $S$ 截断的分子才有贡献：正电荷在 $V$ 内的贡献 $+q$，负电荷在 $V$ 内的贡献 $-q$。

在 $S$ 上取面元 $\mathrm{d}S$，外法向单位矢量 $\boldsymbol{e}_{\mathrm{n}}$，附近的极化可看作均匀，分子电偶极矩都是 $\boldsymbol{p} = q\boldsymbol{l}$，与 $\boldsymbol{e}_{\mathrm{n}}$ 的夹角为 $\theta$。以 $\mathrm{d}S$ 为中截面、沿 $\boldsymbol{l}$ 方向作长为 $l$ 的斜柱体，只有中心在这个柱体内的分子被 $\mathrm{d}S$ 截断。$\theta < \pi/2$ 时，这些分子的负电荷留在 $V$ 内，从 $V$ 内移出的正电荷为

$$
nq\,(l\cos\theta\,\mathrm{d}S) = n\boldsymbol{p}\cdot\boldsymbol{e}_{\mathrm{n}}\,\mathrm{d}S = \boldsymbol{P}\cdot\mathrm{d}\boldsymbol{S},
$$
$\theta > \pi/2$ 时结果的形式相同。对整个 $S$ 求和，得到：

**定理 4.2.1** 任意闭合曲面所包围的极化电荷，等于极化强度对该闭合曲面的**通量**的负值：

$$
q'_{\mathrm{enc}} = -\oint_S \boldsymbol{P}\cdot\mathrm{d}\boldsymbol{S}.
$$

由 **Gauss 公式**，令 $V$ 收缩到一点，得到极化电荷的体密度；在介质与真空的界面上作小扁柱面，得到面密度：

**公式 4.2.1（极化电荷密度）**

$$
\rho' = -\nabla\cdot\boldsymbol{P},\qquad \sigma' = \boldsymbol{P}\cdot\boldsymbol{e}_{\mathrm{n}} = P_{\mathrm{n}},
$$
其中 $\boldsymbol{e}_{\mathrm{n}}$ 是介质表面由介质指向外部的单位法向矢量。

**散度**刻画矢量场的"源"：$\boldsymbol{P}$ 线从负极化电荷发出、终止于正极化电荷。均匀极化时 $\nabla\cdot\boldsymbol{P} = 0$，极化电荷只出现在表面；非均匀极化时，内部和表面都可能有极化电荷。

### 4.2.7. 电介质的击穿

**定义 4.2.5（电介质击穿）** 外电场很强时，分子中的正、负电荷可能被拉开而成为自由电荷，电介质失去绝缘性能而变成导体，这种现象称为**电介质击穿**。电介质能承受的最大场强称为**介电强度**（击穿场强）。

空气的介电强度约为 $3\,\mathrm{kV\,mm^{-1}}$（$3\times10^6\,\mathrm{V\,m^{-1}}$），雷电与电火花就是空气的击穿；云母、陶瓷等可达 $10^2\,\mathrm{kV\,mm^{-1}}$ 量级。电容器的耐压由其中电介质的介电强度决定。

## 4.3. 有介质时静电场的规律

有电介质存在时，静电场由自由电荷 $q_0$ 与极化电荷 $q'$ 共同产生，它们都是静止的电荷，所以**高斯定理**与**静电场环路定理**仍然成立：

$$
\oint_S \boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S} = \frac{q_{0,\mathrm{enc}} + q'_{\mathrm{enc}}}{\varepsilon_0},\qquad \oint_L \boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l} = 0,
$$
其中 $\boldsymbol{E}$ 是全部电荷产生的总场强。

**例 4.3.1** 平行板电容器的极板很大，自由电荷面密度为 $\pm\sigma_0$，极板间充满相对电容率为 $\varepsilon_{\mathrm{r}}$ 的均匀各向同性线性电介质。求板间的场强。

**解** 介质均匀极化，极化电荷只出现在与极板相贴的两个表面上，面密度为 $\mp\sigma'$（与相邻极板的电荷异号）。板间的场是四个无限大带电平面的场的叠加：

$$
E = E_0 - E' = \frac{\sigma_0 - \sigma'}{\varepsilon_0}.
$$
又 $\sigma' = P = \varepsilon_0(\varepsilon_{\mathrm{r}} - 1)E$，联立得

$$
E = \frac{\sigma_0}{\varepsilon_0\varepsilon_{\mathrm{r}}} = \frac{E_0}{\varepsilon_{\mathrm{r}}},\qquad \sigma' = \Big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\Big)\sigma_0 .
$$

这正是 4.1 节的实验结果。类似地，点电荷 $Q_0$ 周围充满无限大的均匀线性介质时，$\boldsymbol{E} = \dfrac{Q_0}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}r^2}\boldsymbol{e}_r$。"场强减为 $1/\varepsilon_{\mathrm{r}}$"并不普遍成立：它要求均匀介质充满整个有电场的空间，或者介质的界面都是**等势面**（例 4.3.2 中介质外的场就没有减弱）。

### 4.3.1. 电位移及其高斯定理

实际问题中已知的是自由电荷（如电容器极板上的电荷），极化电荷是未知的，直接用 $\boldsymbol{E}$ 的高斯定理不方便。把定理 4.2.1 代入 $\boldsymbol{E}$ 的高斯定理，消去 $q'_{\mathrm{enc}}$：

$$
\oint_S(\varepsilon_0\boldsymbol{E} + \boldsymbol{P})\cdot\mathrm{d}\boldsymbol{S} = q_{0,\mathrm{enc}} .
$$

**定义 4.3.1（电位移）** 矢量

$$
\boldsymbol{D} = \varepsilon_0\boldsymbol{E} + \boldsymbol{P}
$$
称为**电位移**（电位移矢量），单位 $\mathrm{C\,m^{-2}}$。这是普遍成立的定义，与介质的性质无关。

**定理 4.3.1（$\boldsymbol{D}$ 的高斯定理）** 电位移对任意闭合曲面的通量，等于该曲面所包围的自由电荷的代数和：

$$
\oint_S\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S} = q_{0,\mathrm{enc}},\qquad \nabla\cdot\boldsymbol{D} = \rho_0 .
$$

$\boldsymbol{D}$ 是为了方便而引入的辅助量：决定电荷受力的仍然是 $\boldsymbol{E}$。$\boldsymbol{D}$ 的通量只与自由电荷有关，但 $\boldsymbol{D}$ 本身一般与极化电荷有关；只有在电荷分布与介质都有足够对称性（球、柱、平面对称）时，才能由 $\boldsymbol{D}$ 的高斯定理先求出 $\boldsymbol{D}$，再求 $\boldsymbol{E}$ 与 $\boldsymbol{P}$。

**定义 4.3.2（相对电容率）** 对各向同性线性电介质，

$$
\boldsymbol{D} = \varepsilon_0\boldsymbol{E} + \varepsilon_0\chi_{\mathrm{e}}\boldsymbol{E} = \varepsilon_0\varepsilon_{\mathrm{r}}\boldsymbol{E} = \varepsilon\boldsymbol{E},
$$
其中 $\varepsilon_{\mathrm{r}} = 1 + \chi_{\mathrm{e}}$ 称为**相对电容率**（相对介电常量），$\varepsilon = \varepsilon_0\varepsilon_{\mathrm{r}}$ 称为介质的**电容率**（介电常量）。此时

$$
\boldsymbol{P} = \varepsilon_0(\varepsilon_{\mathrm{r}} - 1)\boldsymbol{E} = \Big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\Big)\boldsymbol{D},
$$
$\boldsymbol{P}$、$\boldsymbol{E}$、$\boldsymbol{D}$ 三者同向；真空中 $\boldsymbol{P} = \boldsymbol{0}$，$\boldsymbol{D} = \varepsilon_0\boldsymbol{E}$。

### 4.3.2. 极化电荷的分布

**性质 4.3.1** 在均匀的各向同性线性电介质中（无论极化是否均匀），极化电荷体密度与自由电荷体密度成正比：

$$
\rho' = -\Big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\Big)\rho_0 .
$$
因此介质内部没有自由电荷的地方也没有极化电荷；若介质内部没有自由电荷，极化电荷只分布在介质的表面上。

**证明** $\varepsilon_{\mathrm{r}}$ 为常数，由公式 4.2.1 与定理 4.3.1，$\rho' = -\nabla\cdot\boldsymbol{P} = -\big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\big)\nabla\cdot\boldsymbol{D} = -\big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\big)\rho_0$。$\square$

极化电荷与它所包围的自由电荷异号，起部分屏蔽的作用。两种不同介质的交界面上、介质与带电导体的交界面上，一般出现极化面电荷。非均匀介质可以看成许多均匀小区域的集合，相邻区域的界面上有极化电荷，所以非均匀介质内部可以出现极化体电荷。

**例 4.3.2（均匀介质球壳）** 半径 $R_1$、带电 $q_0$ 的导体球外包一层均匀介质球壳，外半径 $R_2$，相对电容率 $\varepsilon_{\mathrm{r}}$。求 $\boldsymbol{E}$ 与极化电荷的分布。

**解** 电荷与介质都是球对称的，$\boldsymbol{D} = D(r)\boldsymbol{e}_r$。在导体球外作半径为 $r$ 的同心球面，由 $\boldsymbol{D}$ 的高斯定理，$4\pi r^2D = q_0$，

$$
\boldsymbol{D} = \frac{q_0}{4\pi r^2}\boldsymbol{e}_r\quad(r > R_1),
$$
于是

$$
\boldsymbol{E} = \begin{cases}
\dfrac{q_0}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}r^2}\boldsymbol{e}_r, & R_1 < r < R_2,\\[2ex]
\dfrac{q_0}{4\pi\varepsilon_0r^2}\boldsymbol{e}_r, & r > R_2,
\end{cases}
\qquad
\boldsymbol{P} = \Big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\Big)\frac{q_0}{4\pi r^2}\boldsymbol{e}_r\quad(R_1 < r < R_2).
$$

介质均匀且内部没有自由电荷，由性质 4.3.1，介质内部 $\rho' = 0$。内表面的法向由介质指向导体，$\boldsymbol{e}_{\mathrm{n}} = -\boldsymbol{e}_r$；外表面 $\boldsymbol{e}_{\mathrm{n}} = \boldsymbol{e}_r$。由公式 4.2.1，

$$
\sigma'_1 = -P(R_1) = -\Big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\Big)\frac{q_0}{4\pi R_1^2},\qquad
\sigma'_2 = P(R_2) = \Big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\Big)\frac{q_0}{4\pi R_2^2},
$$
内、外表面的极化电荷总量分别为 $\mp\big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\big)q_0$，等量异号。

注意起作用的仍是 $\boldsymbol{E}$：总场强就是三个均匀带电球面（$q_0$ 与两层极化电荷）的场的叠加。$\boldsymbol{D}$ 在 $r = R_1$ 以外连续；$\boldsymbol{E}$ 与 $\boldsymbol{P}$ 在介质的两个表面上跃变，因为那里有极化面电荷。

![导体球外包介质球壳（$\varepsilon_{\mathrm{r}} = 3$，$R_2 = 2R_1$）时 $D$、$E$、$P$ 随 $r$ 的变化：$D$ 连续，$E$ 与 $P$ 在介质表面跃变](./plots/dielectric-shell-field.py)

### 4.3.3. 静电场的界面关系

两种介质的交界面上，场量一般不连续。设界面上的自由电荷面密度为 $\sigma_0$，$\boldsymbol{e}_{\mathrm{n}}$ 是由介质 2 指向介质 1 的单位法向矢量，$\boldsymbol{e}_{\mathrm{t}}$ 是界面的单位切向矢量。

- 法向：在界面上作很扁的小柱面，两底面积为 $\Delta S$，分居界面两侧，高趋于零。由 $\boldsymbol{D}$ 的高斯定理，$(D_{1\mathrm{n}} - D_{2\mathrm{n}})\Delta S = \sigma_0\Delta S$。
- 切向：作跨越界面的小矩形回路，两长边 $\Delta l$ 分居界面两侧，短边趋于零。由环路定理，$(E_{1\mathrm{t}} - E_{2\mathrm{t}})\Delta l = 0$。

**定理 4.3.2（静电场的界面关系）**

$$
D_{1\mathrm{n}} - D_{2\mathrm{n}} = \sigma_0,\qquad E_{1\mathrm{t}} = E_{2\mathrm{t}} .
$$
界面上没有自由电荷时，$\boldsymbol{D}$ 的法向分量连续、$\boldsymbol{E}$ 的切向分量连续。

$\boldsymbol{E}$ 的法向分量由全部电荷决定：$\varepsilon_0(E_{1\mathrm{n}} - E_{2\mathrm{n}}) = \sigma_0 + \sigma'$，一般不连续。

对两种各向同性线性介质，界面上 $\sigma_0 = 0$ 时，$\varepsilon_1E_{1\mathrm{n}} = \varepsilon_2E_{2\mathrm{n}}$，$E_{1\mathrm{t}} = E_{2\mathrm{t}}$。设 $\boldsymbol{E}_1$、$\boldsymbol{E}_2$ 与法线的夹角为 $\theta_1$、$\theta_2$，两式相除得**电场线**的"**折射定律**"

$$
\frac{\tan\theta_1}{\tan\theta_2} = \frac{\varepsilon_1}{\varepsilon_2} .
$$
$\varepsilon_1 > \varepsilon_2$ 时 $\theta_1 > \theta_2$：电场线进入电容率大的介质时偏离法线。这两个界面关系与介质中的 **Poisson 方程** $\nabla\cdot(\varepsilon\nabla\varphi) = -\rho_0$ 一起构成有介质时的静电边值问题，**静电唯一性定理**（[5.3.3](/5.3.3)）对它仍然成立。

![界面上没有自由电荷时，电场线从 $\varepsilon_2 = \varepsilon_0$ 的介质进入 $\varepsilon_1 = 4\varepsilon_0$ 的介质，向远离法线的方向偏折](./plots/field-line-refraction.py)

## 4.4. 电容器及其电容

### 4.4.1. 孤立导体的电容

孤立导体带电 $Q$ 时，导体是等势体，**电势**为 $\varphi$（以无穷远为零点）。由叠加原理与**静电唯一性定理**，$Q$ 加倍时电荷分布的形状不变、各处面密度加倍，电势也加倍，所以 $Q/\varphi$ 是只与导体的形状、大小（以及周围介质）有关的常量。

**定义 4.4.1（电容）** 孤立导体所带的电荷 $Q$ 与其电势 $\varphi$ 之比

$$
C = \frac{Q}{\varphi}
$$
称为孤立导体的**电容**。单位是法拉，$1\,\mathrm{F} = 1\,\mathrm{C\,V^{-1}}$；常用 $\mu\mathrm{F}$、$\mathrm{pF}$。电容的量纲 $\dim C = \mathsf{L}^{-2}\,\mathsf{M}^{-1}\,\mathsf{T}^{4}\,\mathsf{I}^{2}$。

电容表示导体每升高单位电势所需的电荷，即导体"容纳"电荷的能力。半径为 $R$ 的孤立导体球，$\varphi = \dfrac{Q}{4\pi\varepsilon_0R}$，

$$
C = 4\pi\varepsilon_0R .
$$
电容为 $1\,\mathrm{F}$ 的导体球半径约为 $9\times10^9\,\mathrm{m}$，是地球半径的 1400 倍；地球本身的电容只有约 $7\times10^{-4}\,\mathrm{F}$。孤立导体的电容一般很小，而且其电势受周围带电体的影响。

### 4.4.2. 电容器

**定义 4.4.2（电容器）** 用导体壳把一个导体包围起来，利用静电屏蔽使两者之间的电场不受外界影响，就构成**电容器**，两个导体称为极板。两极板带等量异号电荷 $\pm Q$ 时，极板间的电压 $U$ 与 $Q$ 成正比，电容器的电容定义为

$$
C = \frac{Q}{U} .
$$
电容只取决于电容器的结构（极板的形状、大小、相对位置与其间的介质），与是否带电无关。实际的电容器（如平行板）并不完全封闭，但极板间距远小于极板尺寸时，电场集中在极板之间，外界的影响可以忽略。

求电容的一般步骤：设极板带 $\pm Q$，由 $\boldsymbol{D}$ 的高斯定理求 $\boldsymbol{D}$ 与 $\boldsymbol{E}$，积分求 $U = \int_+^-\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l}$，再求 $C = Q/U$。

**公式 4.4.1（常见电容器的电容）** 极板间充满相对电容率为 $\varepsilon_{\mathrm{r}}$ 的介质时：

| 电容器 | 电场 | 电容 |
|---|---|---|
| 平行板（面积 $S$，间距 $d$） | $E = \dfrac{Q}{\varepsilon_0\varepsilon_{\mathrm{r}}S}$ | $C = \dfrac{\varepsilon_0\varepsilon_{\mathrm{r}}S}{d}$ |
| 圆柱形（半径 $R_1 < R_2$，长 $L \gg R_2$） | $E = \dfrac{Q}{2\pi\varepsilon_0\varepsilon_{\mathrm{r}}Lr}$ | $C = \dfrac{2\pi\varepsilon_0\varepsilon_{\mathrm{r}}L}{\ln(R_2/R_1)}$ |
| 球形（半径 $R_1 < R_2$） | $E = \dfrac{Q}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}r^2}$ | $C = \dfrac{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}R_1R_2}{R_2 - R_1}$ |

例如球形电容器，$U = \displaystyle\int_{R_1}^{R_2}\frac{Q\,\mathrm{d}r}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}r^2} = \frac{Q}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}}\Big(\frac1{R_1} - \frac1{R_2}\Big)$，即得表中结果。$R_2 \to \infty$ 时它回到孤立导体球的电容（乘以 $\varepsilon_{\mathrm{r}}$）；$R_2 - R_1 = d \ll R_1$ 时，$C \approx \varepsilon_0\varepsilon_{\mathrm{r}}\cdot4\pi R_1^2/d$，回到平行板公式。三个公式都表明：充满介质后电容增大为真空时的 $\varepsilon_{\mathrm{r}}$ 倍，这是电容器中使用电介质的主要原因（另一原因是提高耐压）。

细胞膜是这一模型在生物学中的例子：厚约 $5\,\mathrm{nm}$ 的脂双层两侧是导电的溶液，构成平行板电容器，单位面积的电容约 $1\,\mu\mathrm{F\,cm^{-2}}$；神经冲动的传播就涉及这个电容的充放电（RC 电路见 [5.3.5](/5.3.5)）。

### 4.4.3. 电容器的串联与并联

**公式 4.4.2** $n$ 个电容器并联时各电容器电压相同、电荷相加；串联时各电容器电荷相同（中间的极板感应出等量异号的电荷）、电压相加：

$$
C_{\mathrm{par}} = \sum_{i=1}^nC_i,\qquad \frac{1}{C_{\mathrm{ser}}} = \sum_{i=1}^n\frac{1}{C_i} .
$$

并联可以增大电容，但电容器组的耐压受耐压最低的电容器限制；串联使电容减小，但总电压分配到各电容器上，电容器组的耐压比单个电容器高（电压按 $U_i \propto 1/C_i$ 分配，电容最小的分得最大的电压）。

## 4.5. 有介质时的静电场能量

### 4.5.1. 电容器储存的能量

使电容器带电的过程中，外界（如电源）把电荷从一个极板搬到另一个极板，要克服电场力做功，这个功以**静电能**的形式储存在电容器中。考虑充电的某一时刻，极板带电 $q$，电压 $u = q/C$，再把 $\mathrm{d}q$ 从负极板移到正极板，外力做功 $u\,\mathrm{d}q$。从 $0$ 充电到 $Q$：

**公式 4.5.1（电容器的能量）**

$$
W = \int_0^Q\frac{q}{C}\,\mathrm{d}q = \frac{Q^2}{2C} = \frac12CU^2 = \frac12QU .
$$
放电时，电场力做的功等于这些能量的减少。

### 4.5.2. 能量密度

以平行板电容器为例，极板间场强均匀，$U = Ed$，$C = \varepsilon S/d$，

$$
W = \frac12CU^2 = \frac12\frac{\varepsilon S}{d}(Ed)^2 = \frac12\varepsilon E^2\cdot(Sd) .
$$
$Sd$ 是电场所占的体积，所以单位体积的电场能量为 $\frac12\varepsilon E^2 = \frac12ED$。这个结论对一般的线性介质（包括各向异性的线性介质）都成立：

**公式 4.5.2（电场的能量密度）**

$$
w_{\mathrm{e}} = \frac12\boldsymbol{E}\cdot\boldsymbol{D},\qquad W = \int_V w_{\mathrm{e}}\,\mathrm{d}V = \int_V\frac12\boldsymbol{E}\cdot\boldsymbol{D}\,\mathrm{d}V .
$$
各向同性线性介质中 $w_{\mathrm{e}} = \frac12\varepsilon E^2$，真空中 $w_{\mathrm{e}} = \frac12\varepsilon_0E^2$，与 [5.3.2](/5.3.2) 的结果一致。

与真空相比，$w_{\mathrm{e}} = \frac12\varepsilon_0E^2 + \frac12\boldsymbol{E}\cdot\boldsymbol{P}$ 多出的部分是使介质极化所做的功：在电介质中，不仅电场储存能量，介质极化的过程中也吸收并储存了能量。

**例 4.5.1（一半浸在油中的导体球）** 半径为 $R$ 的导体球带电 $Q$，一半浸在相对电容率 $\varepsilon_{\mathrm{r}} = 3.0$ 的油中，一半在空气中（取 $\varepsilon_{\mathrm{r}} = 1$），油面是过球心的无限大平面。求：（1）上半球面（空气中）与下半球面（油中）上的自由电荷 $Q_1$、$Q_2$；（2）下半球面附近油中的极化电荷面密度。

**解**（1）方法一：猜解，再由**静电唯一性定理**说明它是唯一解。有介质时，定解条件除导体的总电荷与等势条件外，还要给定介质的形状、位置与 $\varepsilon_{\mathrm{r}}$，以及介质界面上的界面关系。设场仍是球对称的，

$$
\boldsymbol{E} = \frac{Q^*}{4\pi\varepsilon_0r^2}\boldsymbol{e}_r,
$$
其中 $Q^*$ 是球面上的自由电荷与紧贴球面的极化电荷之和（对上、下两半相同）。这个场满足：导体球是等势体；空气与油的界面上 $\boldsymbol{E}$ 沿径向、与界面相切，$E_{\mathrm{t}}$ 连续，$D_{\mathrm{n}} = 0$ 连续。剩下的条件是导体球的总电荷为 $Q$。由 $\boldsymbol{D}$ 的高斯定理，对包围导体球的同心球面，

$$
\varepsilon_0\frac{Q^*}{4\pi\varepsilon_0R^2}\cdot2\pi R^2 + \varepsilon_0\varepsilon_{\mathrm{r}}\frac{Q^*}{4\pi\varepsilon_0R^2}\cdot2\pi R^2 = Q
\quad\Longrightarrow\quad Q^* = \frac{2Q}{1 + \varepsilon_{\mathrm{r}}} .
$$
上半球面的自由电荷等于上半球面上的 $D$ 通量，下半球面同理：

$$
Q_1 = \frac{Q^*}{2} = \frac{Q}{1 + \varepsilon_{\mathrm{r}}} = \frac{Q}{4},\qquad Q_2 = \frac{\varepsilon_{\mathrm{r}}Q^*}{2} = \frac{\varepsilon_{\mathrm{r}}Q}{1 + \varepsilon_{\mathrm{r}}} = \frac{3Q}{4} .
$$

方法二：电容法。上、下两部分可以看作两个以导体球与无穷远为极板的"半球电容器"并联，它们的电压相同。半个孤立导体球的电容是 $C_1 = 2\pi\varepsilon_0R$，$C_2 = 2\pi\varepsilon_0\varepsilon_{\mathrm{r}}R$，电荷按电容分配：$Q_1 = \dfrac{C_1}{C_1 + C_2}Q = \dfrac{Q}{1 + \varepsilon_{\mathrm{r}}}$，与方法一相同。

（2）油中紧贴球面处 $\boldsymbol{P} = \varepsilon_0(\varepsilon_{\mathrm{r}} - 1)\boldsymbol{E}$，介质表面的法向由油指向导体，$\boldsymbol{e}_{\mathrm{n}} = -\boldsymbol{e}_r$：

$$
\sigma' = -\varepsilon_0(\varepsilon_{\mathrm{r}} - 1)\frac{Q^*}{4\pi\varepsilon_0R^2} = -\frac{\varepsilon_{\mathrm{r}} - 1}{\varepsilon_{\mathrm{r}} + 1}\cdot\frac{Q}{2\pi R^2} = -\frac{Q}{4\pi R^2} .
$$
下半球面附近的极化电荷总量为 $\sigma'\cdot2\pi R^2 = -\frac{\varepsilon_{\mathrm{r}} - 1}{\varepsilon_{\mathrm{r}} + 1}Q$，它与 $Q_2$ 之和恰好等于 $Q_1$：两半球面上的总电荷（自由电荷加极化电荷）相等，这正是场保持球对称的原因。

## 小结

| 量或规律 | 表达式 | 说明 |
|---|---|---|
| 极化强度 | $\boldsymbol{P} = \sum\boldsymbol{p}_i/\Delta V$ | 各向同性线性介质 $\boldsymbol{P} = \varepsilon_0(\varepsilon_{\mathrm{r}} - 1)\boldsymbol{E}$ |
| 极化电荷 | $q'_{\mathrm{enc}} = -\oint\boldsymbol{P}\cdot\mathrm{d}\boldsymbol{S}$，$\rho' = -\nabla\cdot\boldsymbol{P}$，$\sigma' = P_{\mathrm{n}}$ | $\boldsymbol{e}_{\mathrm{n}}$ 由介质指向外部 |
| 电位移 | $\boldsymbol{D} = \varepsilon_0\boldsymbol{E} + \boldsymbol{P}$ | 各向同性线性介质 $\boldsymbol{D} = \varepsilon_0\varepsilon_{\mathrm{r}}\boldsymbol{E}$ |
| $\boldsymbol{D}$ 的高斯定理 | $\oint\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S} = q_{0,\mathrm{enc}}$，$\nabla\cdot\boldsymbol{D} = \rho_0$ | 只含自由电荷 |
| 界面关系 | $D_{1\mathrm{n}} - D_{2\mathrm{n}} = \sigma_0$，$E_{1\mathrm{t}} = E_{2\mathrm{t}}$ | $\boldsymbol{e}_{\mathrm{n}}$ 由 2 指向 1 |
| 电容 | $C = Q/U$ | 只与结构有关；并联相加，串联倒数相加 |
| 能量 | $W = \frac{Q^2}{2C} = \frac12CU^2$，$w_{\mathrm{e}} = \frac12\boldsymbol{E}\cdot\boldsymbol{D}$ | 线性介质 |

## 思考题

1. 电容器两极板的电荷不是等量异号时（如 $Q_1$ 与 $Q_2$），怎样由 $C = Q/U$ 计算电容？

   **答** 电容是结构参量，与带电情况无关。对平行板电容器，由叠加原理，板间场强 $E = \frac{Q_1 - Q_2}{2\varepsilon_0S}$，只与电荷差的一半有关；取 $Q = \frac{Q_1 - Q_2}{2}$，仍有 $U = Q/C$。两板带不等量同号电荷时同理，多出的 $\frac{Q_1 + Q_2}{2}$ 分布在两板外侧，不影响板间电压。

2. 用静电场环路定理证明：平行板电容器边缘的电场不可能由均匀场突然变为零。

   **答** 作一个矩形回路，一条长边在板间平行于场强，另一条在板外场强为零处，两短边垂直于极板。若边缘处场强突变为零，环路积分等于 $El \ne 0$，与环路定理矛盾。所以边缘必有逐渐减弱的边缘场。

3. 为什么导体内部的场强为零，而电介质内部的场强可以不为零？

   **答** 导体中的自由电荷可以移动任意距离，只要内部有场强就继续移动，直到完全抵消外场；电介质中的极化电荷被束缚在分子内，只能作微小位移，极化程度由总场强决定，达到平衡时总场强不为零。

4. 有介质时，$\boldsymbol{E}$ 的环路定理是否成立？$\boldsymbol{D}$ 的环路积分是否一定为零？

   **答** $\boldsymbol{E}$ 的环路定理成立，因为全部电荷都是静止的。$\boldsymbol{D}$ 的环路积分不一定为零：在两种介质的界面上 $E_{\mathrm{t}}$ 连续，所以 $D_{\mathrm{t}} = \varepsilon E_{\mathrm{t}}$ 不连续，跨越界面的矩形回路上 $\oint\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{l} = (\varepsilon_1 - \varepsilon_2)E_{\mathrm{t}}\Delta l \ne 0$。
