---
title: 刚体的转动
description: 刚体的运动形式与角速度，定轴转动定律与转动惯量（平行轴定理、垂直轴定理），定轴转动的功能关系与角动量守恒，角动量与角速度的关系、进动与章动，自由度与 Euler 角，刚体平面运动（瞬心、纯滚动、König 定理）。
---

刚体是**质点**系的一个理想化模型：各质点之间的距离保持不变。因此 [5.1.3](/5.1.3) 与 [5.1.4](/5.1.4) 中质点系的规律（**质心运动定理**、**角动量定理**、**功能原理**）对刚体全部适用，而刚体的约束又使这些规律化为特别简单的形式：定轴转动只需要一个角坐标，**动力学**方程 $M=J\alpha$ 与 **Newton 第二定律** $F=ma$ 一一对应，转动惯量扮演质量的角色。本章先讲刚体的**运动学**（**角速度**与基点无关），然后是定轴转动的转动定律、转动惯量的计算、功能关系与角动量定理，再讨论**角动量**与角速度不平行时出现的进动，并由此引出自由度的概念，最后简介刚体的平面运动（滚动）。数学上用到**向量积**（$\boldsymbol{v}=\boldsymbol{\omega}\times\boldsymbol{r}$）、作为积分的**转动惯量**（[2.2.12](/2.2.12)），以及**对称矩阵**的主轴（惯性张量）。自由度的概念在热学的能量均分定理（[5.2.1](/5.2.1)）中还会用到。

## 5.1. 刚体的运动

### 5.1.1. 刚体的概念

**定义 5.1.1（刚体）** 在任何外力作用下形状和大小都不变的物体称为**刚体**，即其中任意两点之间的距离保持不变的质点系。

刚体是理想化的模型：无限刚硬，受力不变形，力的作用可以瞬时传遍整个物体。作为特殊的质点系，质点系的规律对它都适用；它又有自己独特的运动学与动力学规律。

### 5.1.2. 刚体的运动形式

**定义 5.1.2** 刚体运动的基本形式：

1. **平动**：刚体内任意两点的连线在运动中始终保持平行。平动刚体上各点的运动完全相同，常用质心的运动代表整体的平动。
2. **定点转动**：刚体上只有一点固定不动，刚体在每一瞬时绕通过该点的某条瞬时轴转动；若瞬时轴固定不变，则为**定轴转动**。
3. **平面运动**：刚体上各点都平行于某一固定平面运动，各点的轨道平面平行或重合。
4. **一般运动**：不受任何限制的自由运动，可以分解为随基点 $O$（可任意选取）的平动与绕通过 $O$ 的瞬时轴的定点转动。

基点不同，平动的部分不同，但转动的部分（角速度）相同：转动与基点的选取无关。例如车轮在地面上滚动，以轮心为基点是"轮心平动加绕轮心转动"，以轮缘上一点为基点是"该点的平动加绕该点转动"，两种分解中转动的角速度相同。

### 5.1.3. 定点转动的运动学量

**定义 5.1.3** 刚体绕基点 $O$ 作定点转动，瞬时轴的方向与转动的快慢用**角速度**矢量 $\boldsymbol{\omega}$ 描述：$\boldsymbol{\omega}$ 沿瞬时轴，方向按右手法则由转动方向确定，大小 $\omega=\mathrm{d}\theta/\mathrm{d}t$ 是转动的角**速率**。**角加速度**为 $\boldsymbol{\alpha}=\dfrac{\mathrm{d}\boldsymbol{\omega}}{\mathrm{d}t}$。

**性质 5.1.1** 刚体上一点 $P$ 相对基点 $O$ 的**位矢**为 $\boldsymbol{r}$，则

$$
\boldsymbol{v}=\boldsymbol{\omega}\times\boldsymbol{r},\qquad
\boldsymbol{a}=\frac{\mathrm{d}\boldsymbol{\omega}}{\mathrm{d}t}\times\boldsymbol{r}+\boldsymbol{\omega}\times\frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}t}=\boldsymbol{\alpha}\times\boldsymbol{r}+\boldsymbol{\omega}\times\boldsymbol{v},
$$
$\boldsymbol{v}$ 的大小为 $\omega r_\perp$，$r_\perp$ 是 $P$ 到瞬时轴的距离。$\boldsymbol{\alpha}\times\boldsymbol{r}$ 称为转动**加速度**，$\boldsymbol{\omega}\times\boldsymbol{v}=\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r})$ 指向瞬时轴，称为向轴加速度。

角速度与基点的选取无关：设以 $O$ 与 $O'$ 为基点时角速度分别为 $\boldsymbol{\omega}$、$\boldsymbol{\omega}'$，对刚体上任一点 $P$，

$$
\boldsymbol{v}_P=\boldsymbol{v}_O+\boldsymbol{\omega}\times\overrightarrow{OP}=\boldsymbol{v}_{O'}+\boldsymbol{\omega}'\times\overrightarrow{O'P}.
$$
取 $P=O'$ 得 $\boldsymbol{v}_{O'}=\boldsymbol{v}_O+\boldsymbol{\omega}\times\overrightarrow{OO'}$，代回并利用 $\overrightarrow{OP}=\overrightarrow{OO'}+\overrightarrow{O'P}$ 得 $(\boldsymbol{\omega}-\boldsymbol{\omega}')\times\overrightarrow{O'P}=\boldsymbol{0}$ 对所有 $P$ 成立，所以 $\boldsymbol{\omega}'=\boldsymbol{\omega}$。正因为如此，"刚体的角速度"才有意义。

一般情况下 $\boldsymbol{\alpha}$ 与 $\boldsymbol{\omega}$ 的方向不同，也不一定沿瞬时轴（例如陀螺的瞬时轴本身在转动）。

### 5.1.4. 定轴转动

定轴转动时 $\boldsymbol{\omega}$ 与 $\boldsymbol{\alpha}$ 都沿固定轴（取为 $z$ 轴），都退化为代数量：用一个角坐标 $\theta$（相对某个参考方向）就确定了刚体的位置，$\omega=\dot\theta$，$\alpha=\dot\omega=\ddot\theta$，正负号表示沿 $z$ 轴的正向或负向。到轴距离为 $r_\perp$ 的点作圆周运动，

$$
v=r_\perp\omega,\qquad a_{\mathrm{t}}=\frac{\mathrm{d}v}{\mathrm{d}t}=r_\perp\alpha,\qquad a_{\mathrm{n}}=r_\perp\omega^2 .
$$
$\alpha$ 恒定（匀加速转动）时，与匀加速直线运动的公式一一对应：

$$
\omega=\omega_0+\alpha t,\qquad \theta-\theta_0=\omega_0t+\frac12\alpha t^2,\qquad \omega^2-\omega_0^2=2\alpha(\theta-\theta_0).
$$

## 5.2. 刚体的定轴转动定律

把刚体看作由无限多个质元 $\Delta m_i$ 组成的质点系。质点系对定点 $O$ 与对定轴 $z$ 的**角动量定理**（[5.1.3](/5.1.3)）为

$$
\boldsymbol{M}_{\mathrm{ext}}=\frac{\mathrm{d}\boldsymbol{L}}{\mathrm{d}t},\qquad M_{\mathrm{ext},z}=\frac{\mathrm{d}L_z}{\mathrm{d}t}.
$$
定轴转动时质元 $\Delta m_i$ 在垂直于轴的平面内作半径为 $r_{i\perp}$ 的圆周运动，**速度** $v_i=r_{i\perp}\omega$ 与半径垂直，所以

$$
L_z=\sum_i\Delta m_i\,v_ir_{i\perp}=\Big(\sum_i\Delta m_ir_{i\perp}^2\Big)\omega .
$$

**定义 5.2.1（转动惯量）** 刚体对 $z$ 轴的**转动惯量**，对质点系与连续体分别为

$$
J_z=\sum_i\Delta m_ir_{i\perp}^2,\qquad J_z=\int_mr_\perp^2\,\mathrm{d}m,
$$
其中 $r_\perp$ 是质元到轴的距离。单位 $\mathrm{kg\,m^2}$。

于是 $L_z=J_z\omega$，而 $M_{\mathrm{ext},z}=\sum_iF_{i\perp}r_{i\perp}\sin\varphi_i$ 是外力在垂直于轴的平面内的分力对轴的**力矩**之和（内力矩成对抵消）。

**定理 5.2.1（转动定律）** 刚体绕定轴转动时，所受外力对该轴的合力矩等于刚体对该轴的转动惯量与角加速度的乘积：

$$
M=J\alpha .
$$

这里略去了下标 $z$。与 Newton 第二定律对照，$M\leftrightarrow F$、$J\leftrightarrow m$、$\alpha\leftrightarrow a$：转动惯量是刚体转动惯性的量度。

## 5.3. 转动惯量的计算

### 5.3.1. 常用的转动惯量

转动惯量由刚体的质量以及质量相对于轴的分布决定（质量 $m$，均匀分布）：

| 刚体 | 转轴 | $J$ |
|---|---|---|
| 细圆环（半径 $R$） | 过环心、垂直于环面 | $mR^2$ |
| 圆盘或圆柱（半径 $R$） | 中心轴 | $\frac12mR^2$ |
| 细杆（长 $l$） | 过中点、垂直于杆 | $\frac1{12}ml^2$ |
| 细杆（长 $l$） | 过一端、垂直于杆 | $\frac13ml^2$ |
| 球体（半径 $R$） | 直径 | $\frac25mR^2$ |
| 薄球壳（半径 $R$） | 直径 | $\frac23mR^2$ |

例如细杆过中点：取杆为 $x$ 轴，线密度 $m/l$，$J_C=\int_{-l/2}^{l/2}x^2\frac{m}{l}\,\mathrm{d}x=\frac1{12}ml^2$。球体的计算见 [例 12.5.2](/2.2.12#ex-12.5.2)。

### 5.3.2. 计算转动惯量的规律

1. 可加性：对同一转轴，由几部分组成的刚体的转动惯量等于各部分转动惯量之和，$J=\sum_iJ_i$。

**定理 5.3.1（平行轴定理）** 刚体对任一轴的转动惯量 $J$，等于它对过质心的平行轴的转动惯量 $J_C$ 加上 $md^2$，$d$ 是两轴之间的距离：

$$
J=J_C+md^2 .
$$

**证明** 取过质心的轴为 $z$ 轴，另一轴过点 $(d,0)$（在垂直于轴的平面内）。质元的位置为 $(x_i,y_i)$，

$$
J=\sum_i\Delta m_i\big[(x_i-d)^2+y_i^2\big]=\sum_i\Delta m_i(x_i^2+y_i^2)-2d\sum_i\Delta m_ix_i+d^2\sum_i\Delta m_i=J_C+md^2,
$$
因为质心在原点，$\sum_i\Delta m_ix_i=0$。$\square$

由此可知，在一组平行轴中，对过质心的轴的转动惯量最小。细杆过一端的 $J_A=\frac1{12}ml^2+m\big(\frac l2\big)^2=\frac13ml^2$。

**定理 5.3.2（垂直轴定理）** 薄平板对垂直于板面的 $z$ 轴的转动惯量，等于它对板面内过同一点、互相垂直的 $x$ 轴与 $y$ 轴的转动惯量之和：

$$
J_z=J_x+J_y .
$$

**证明** 板上质元 $\Delta m_i$ 到 $z$ 轴的距离平方是 $x_i^2+y_i^2$，到 $x$ 轴、$y$ 轴的距离平方分别是 $y_i^2$、$x_i^2$（板很薄，$z_i\approx0$），所以 $J_z=\sum_i\Delta m_i(x_i^2+y_i^2)=J_y+J_x$。$\square$

**例 5.3.1** 求均匀薄圆盘对一条直径的转动惯量。

**解** 已知 $J_z=\frac12mR^2$，由对称性 $J_x=J_y$，由垂直轴定理 $J_x=J_y=\frac12J_z=\frac14mR^2$。

**例 5.3.2** 均匀圆柱体质量 $m$、长 $l$、直径 $D$，求它对过一个端面中心、垂直于圆柱轴线的轴 $z$ 的转动惯量。

**解** 把圆柱沿轴线切成厚 $\mathrm{d}x$ 的薄圆盘，距端面 $x$ 处的薄圆盘质量 $\mathrm{d}m=\frac{m}{l}\mathrm{d}x$。由例 5.3.1，它对自身一条平行于 $z$ 的直径的转动惯量是 $\frac14\mathrm{d}m\big(\frac D2\big)^2$；由平行轴定理，它对 $z$ 轴的转动惯量为 $\mathrm{d}J_z=\frac14\big(\frac D2\big)^2\mathrm{d}m+x^2\,\mathrm{d}m$。积分得

$$
J_z=\int_0^l\Big[\frac{D^2}{16}+x^2\Big]\frac{m}{l}\,\mathrm{d}x=\frac{mD^2}{16}+\frac13ml^2 .
$$
$D\to0$ 时回到细杆绕一端的结果。

## 5.4. 转动定律应用举例

**例 5.4.1（用落体法测转动惯量）** 半径为 $R$ 的轮子可绕光滑水平轴 $O$ 转动，轮缘上绕有轻绳，绳下端挂质量为 $m$ 的物体。物体由静止释放，测得在时间 $t$ 内下落高度 $h$。绳与轮之间无相对滑动，绳不可伸长，求轮对 $O$ 轴的转动惯量 $J$。

**解** 设绳的张力为 $T$。动力学关系：对轮，$TR=J\alpha$；对物体，$mg-T=ma$。运动学关系：$a=\alpha R$，$h=\frac12at^2$。联立解得

$$
J=\Big(\frac{gt^2}{2h}-1\Big)mR^2 .
$$
检验：**量纲**正确；$h$、$m$ 一定时 $J$ 越大下落越慢，$t$ 越大，合理；$J=0$ 时得 $h=\frac12gt^2$，即自由落体。这是实验上测定转动惯量的一种方法。

## 5.5. 定轴转动中的功能关系

### 5.5.1. 力矩的功

力 $\boldsymbol{F}$ 作用在刚体上到轴距离为 $r_\perp$ 的点，刚体转过 $\mathrm{d}\theta$ 时作用点的**位移**大小为 $r_\perp\,\mathrm{d}\theta$，只有 $\boldsymbol{F}$ 在转动平面内的切向分量做**功**：

$$
\mathrm{d}W=F_\perp\cos\varphi\cdot r_\perp\,\mathrm{d}\theta=M\,\mathrm{d}\theta,\qquad W=\int_{\theta_1}^{\theta_2}M\,\mathrm{d}\theta,
$$
其中 $\varphi$ 是 $F_\perp$ 与切向的夹角，$M$ 是力对轴的力矩。这是力矩对空间的积累；**功率** $P=M\omega$。

考虑刚体的能量时，内力的功可以不计：一对内力的功只取决于两质点的相对位移（[性质 4.3.1](/5.1.4#pty-4.3.1)），而刚体中任意两点之间的距离不变，所以内力的总功为零，只需计算外力（外力矩）的功。

### 5.5.2. 定轴转动动能定理

由转动定律，

$$
W=\int_{\theta_1}^{\theta_2}J\frac{\mathrm{d}\omega}{\mathrm{d}t}\,\mathrm{d}\theta=\int_{\omega_1}^{\omega_2}J\omega\,\mathrm{d}\omega=\frac12J\omega_2^2-\frac12J\omega_1^2 .
$$
$\frac12J\omega^2$ 称为刚体的转动动能（rotational kinetic energy）。它正是各质元**动能**之和：$\sum_i\frac12\Delta m_iv_i^2=\frac12\big(\sum_i\Delta m_ir_{i\perp}^2\big)\omega^2=\frac12J\omega^2$。

**定理 5.5.1（定轴转动动能定理）** 合外力矩对定轴转动刚体所做的功等于刚体转动动能的增量：

$$
W=\Delta\Big(\frac12J\omega^2\Big).
$$

### 5.5.3. 刚体的重力势能

刚体与地球系统的重力**势能**等于各质元重力势能之和：

$$
E_{\mathrm{p}}=\sum_i\Delta m_igh_i=mg\frac{\sum_i\Delta m_ih_i}{m}=mgh_C,
$$
即把全部质量集中在质心时的重力势能。

### 5.5.4. 应用举例

对包含刚体的系统，功能原理与**机械能守恒定律**仍然成立。

**例 5.5.1** 均匀直杆 $AB$ 质量为 $m$、长为 $l$，可绕光滑水平轴 $O$ 转动，$AO=l/4$。杆从水平位置由静止释放，求杆下摆到与水平方向成 $\theta$ 角时的角速度 $\omega$ 与轴对杆的作用力 $\boldsymbol{N}$。

**解** 质心 $C$ 到轴的距离 $OC=l/4$，由平行轴定理

$$
J_O=\frac1{12}ml^2+m\Big(\frac l4\Big)^2=\frac7{48}ml^2 .
$$
杆与地球系统只有重力做功，**机械能**守恒：$\frac12J_O\omega^2-mg\frac l4\sin\theta=0$，

$$
\omega=\sqrt{\frac{24g\sin\theta}{7l}}=2\sqrt{\frac{6g\sin\theta}{7l}} .
$$
求轴力要用**质心运动定理** $\boldsymbol{N}+m\boldsymbol{g}=m\boldsymbol{a}_C$。取 $\boldsymbol{e}_{\mathrm{n}}$ 由 $C$ 指向 $O$，$\boldsymbol{e}_{\mathrm{t}}$ 沿质心的运动方向（垂直于杆、斜向下）。质心作半径 $l/4$ 的圆周运动，

$$
a_{C\mathrm{n}}=\omega^2\frac l4=\frac67g\sin\theta,\qquad a_{C\mathrm{t}}=\alpha\frac l4=\frac{mg\frac l4\cos\theta}{J_O}\cdot\frac l4=\frac37g\cos\theta .
$$
重力在两个方向的分量为 $-mg\sin\theta$ 与 $mg\cos\theta$，所以

$$
N_{\mathrm{n}}-mg\sin\theta=ma_{C\mathrm{n}},\qquad N_{\mathrm{t}}+mg\cos\theta=ma_{C\mathrm{t}},
$$
解得 $N_{\mathrm{n}}=\frac{13}7mg\sin\theta$，$N_{\mathrm{t}}=-\frac47mg\cos\theta$，即

$$
\boldsymbol{N}=\frac{13}{7}mg\sin\theta\,\boldsymbol{e}_{\mathrm{n}}-\frac47mg\cos\theta\,\boldsymbol{e}_{\mathrm{t}},\qquad N=\frac{mg}{7}\sqrt{153\sin^2\theta+16} .
$$

## 5.6. 刚体定轴转动的角动量定理

把质点系对轴的角动量定理对时间积分，并用 $L_z=J_z\omega$：

**定理 5.6.1（定轴转动的角动量定理）** 定轴转动刚体所受合外力矩的**冲量矩**等于刚体角动量的增量：

$$
\int_{t_1}^{t_2}M_{\mathrm{ext},z}\,\mathrm{d}t=J_z\omega_2-J_z\omega_1,\qquad M_{\mathrm{ext},z}\,\mathrm{d}t=\mathrm{d}(J_z\omega).
$$
写成 $\mathrm{d}(J_z\omega)$ 是为了也包括转动惯量会变化的物体（如转动的人收拢手臂）。

**定理 5.6.2（定轴转动的角动量守恒定律）** 若 $M_{\mathrm{ext},z}=0$，则 $L_z=J_z\omega$ 保持不变。

转动惯量可以改变的系统中，$J$ 减小时 $\omega$ 增大：花样滑冰运动员收拢手臂转速加快，跳水运动员抱膝增加翻转圈数。

陀螺仪是角动量守恒的重要应用：高速自转的转子装在由两个或三个互相垂直的框架组成的万向支架上，支架对转子的力矩几乎为零，转子的自转轴就在空间中保持方向不变，可以用于导航。西汉已有的"被中香炉"利用同样的万向支架，使香炉无论怎样翻滚，炉口始终朝上（它利用的是重力使炉体保持竖直，不是角动量守恒）。

**例 5.6.1（两轮磨合）** 两个轮子分别绕各自的固定平行轴转动，转动惯量 $J_1$、$J_2$，半径 $r_1$、$r_2$，初角速度 $\omega_{10}$、$\omega_{20}$。使两轮的边缘接触，摩擦力使两轮最终无相对滑动地转动。能否用对轴的角动量守恒求末角速度？

**解** 不能。角动量可以在一个刚体系内的各个刚体之间传递，刚体系对某一转轴的总角动量守恒，但必须是同一个轴。这里两轮绕不同的轴转动，接触点的摩擦力对两轴的力矩并不抵消，各自的轴承还要提供外力，所以两轮对任一个轴的总角动量都不守恒。

正确的做法是对每个轮分别用角动量定理。取各轮转动的正方向，使两轮在接触点的线速度 $v_1=\omega_1r_1$、$v_2=\omega_2r_2$ 沿同一方向为正。设 $v_1>v_2$，摩擦力大小为 $f$，对轮 1 起阻碍作用、对轮 2 起带动作用：

$$
J_1\frac{\mathrm{d}\omega_1}{\mathrm{d}t}=-fr_1,\qquad J_2\frac{\mathrm{d}\omega_2}{\mathrm{d}t}=fr_2 .
$$
消去 $f$，得到守恒量 $\dfrac{J_1\omega_1}{r_1}+\dfrac{J_2\omega_2}{r_2}$（不是角动量）。末态无相对滑动，$\omega_1r_1=\omega_2r_2=v$，

$$
v=\frac{J_1\omega_{10}/r_1+J_2\omega_{20}/r_2}{J_1/r_1^2+J_2/r_2^2},\qquad \omega_1=\frac v{r_1},\quad\omega_2=\frac v{r_2} .
$$

**例 5.6.2** 质量为 $2m$、半径为 $R$ 的均质圆盘可绕光滑水平轴 $O$ 在竖直平面内转动，开始时静止。质量为 $m$ 的粘土块以速度 $v_0$ 斜射到圆盘的最高点 $P$ 并与圆盘粘在一起，$\boldsymbol{v}_0$ 与水平方向成 $\theta=60^\circ$ 角。求 $P$ 转到与 $O$ 等高（$x$ 轴上）时圆盘的角速度 $\omega$、角加速度 $\alpha$ 与轴对圆盘的作用力 $\boldsymbol{N}$。

**解** 过程分两步。碰撞过程：对粘土块与圆盘组成的系统，碰撞瞬间重力与轴力对 $O$ 轴的力矩为零（轴力过 $O$；碰撞时间极短，重力矩的冲量矩可忽略），对 $O$ 轴的角动量守恒。设碰后瞬间角速度为 $\omega_0$，只有 $\boldsymbol{v}_0$ 的水平分量对 $O$ 有力矩：

$$
Rmv_0\cos\theta=\Big(\frac12\cdot2mR^2+mR^2\Big)\omega_0=2mR^2\omega_0,\qquad \omega_0=\frac{v_0}{4R}.
$$
转动过程：粘土块与圆盘形成一个刚体，$J=2mR^2$。对粘土块、圆盘与地球系统，机械能守恒。取 $P$ 在 $x$ 轴上时粘土块的重力势能为零：

$$
\frac12J\omega_0^2+mgR=\frac12J\omega^2,\qquad \omega=\frac{\sqrt{v_0^2+16gR}}{4R}.
$$
此时合外力矩 $mgR$（圆盘的重力过轴），$\alpha=\dfrac{mgR}{2mR^2}=\dfrac{g}{2R}$。

求轴力用质心运动定理。系统的质心 $C$ 在 $O$ 与粘土块的连线上，$OC=\dfrac{mR}{3m}=\dfrac R3$。质心的**切向加速度** $a_{C\mathrm{t}}=\alpha R/3$ 沿 $-y$ 方向，**法向加速度** $a_{C\mathrm{n}}=\omega^2R/3$ 沿 $-x$ 方向（指向 $O$）。由 $\boldsymbol{N}+3m\boldsymbol{g}=3m\boldsymbol{a}_C$：

$$
N_x=-3m\cdot\frac{\omega^2R}3=-m\Big(\frac{v_0^2}{16R}+g\Big),\qquad N_y-3mg=-3m\cdot\frac{\alpha R}3,\quad N_y=\frac52mg .
$$
$N_x<0$ 表示轴力的水平分量指向 $-x$。也可以对粘土块与圆盘分别作隔离体分析，用 Newton 定律求出同样的结果。

## 5.7. 进动

### 5.7.1. 刚体的角动量与角速度的关系

刚体的角动量 $\boldsymbol{L}$ 与角速度 $\boldsymbol{\omega}$ 的方向不一定相同。例如一根轻杆两端各固连一个质量为 $m$ 的小球，杆的中点 $O$ 在 $z$ 轴上，杆与 $z$ 轴斜交，在约束下绕 $z$ 轴转动。每个小球的角动量 $\boldsymbol{r}\times m\boldsymbol{v}$ 都垂直于杆，而不沿 $z$ 轴，所以对 $O$ 的总角动量 $\boldsymbol{L}_O$ 不平行于 $\boldsymbol{\omega}$，并随杆一起绕 $z$ 轴转动；维持这种转动需要轴承不断提供力矩（转子不平衡时轴承受到周期性的力就是这个原因）。

一般地，对定点 $O$，

$$
\boldsymbol{L}=\sum_i\Delta m_i\,\boldsymbol{r}_i\times(\boldsymbol{\omega}\times\boldsymbol{r}_i)=J\boldsymbol{\omega},\qquad
J=\begin{bmatrix}J_{xx}&J_{xy}&J_{xz}\\J_{xy}&J_{yy}&J_{yz}\\J_{xz}&J_{yz}&J_{zz}\end{bmatrix},
$$
其中 $J_{xx}=\sum\Delta m_i(y_i^2+z_i^2)$，$J_{xy}=-\sum\Delta m_ix_iy_i$，等等。矩阵 $J$ 称为惯性张量，它是实**对称矩阵**，由**谱定理**（[2.1.7](/2.1.7)），存在三个互相垂直的主轴，即 $J$ 的特征向量；绕第 $k$ 个主轴转动时 $\boldsymbol{L}=J_k\boldsymbol{\omega}$，二者平行，对应的**特征值** $J_k$ 称为主转动惯量。质量均匀、几何对称的刚体，对称轴就是主轴：绕几何对称轴自转时，自转角动量平行于自转角速度。

在上面的例子中，若剪断约束（使系统对 $O$ 不受力矩），杆将怎样运动？此时 $\boldsymbol{L}_O$ 守恒，而 $\boldsymbol{\omega}$ 不再沿 $z$ 轴：杆绕 $\boldsymbol{L}_O$ 的方向（过 $O$、与杆垂直的那根轴 $OO'$）转动。

### 5.7.2. 进动

高速自转的物体，其自转轴绕另一个轴转动的现象称为进动（precession），如玩具陀螺的自转轴绕竖直轴缓慢转动。

分析对称陀螺：支点 $O$ 固定，质心 $C$ 在对称轴上，$OC=r_C$，对称轴与竖直方向成 $\theta$ 角，陀螺绕对称轴高速自转，角速度 $\boldsymbol{\omega}$。高速自转时总角动量近似等于自转角动量 $\boldsymbol{L}=J\boldsymbol{\omega}$，沿对称轴。重力对 $O$ 的力矩 $\boldsymbol{M}=\boldsymbol{r}_C\times m\boldsymbol{g}$ 水平且垂直于 $\boldsymbol{L}$，由角动量定理 $\mathrm{d}\boldsymbol{L}=\boldsymbol{M}\,\mathrm{d}t$，$\mathrm{d}\boldsymbol{L}\parallel\boldsymbol{M}\perp\boldsymbol{L}$：每一瞬时 $\boldsymbol{L}$ 只改变方向而不改变大小，而力矩 $\boldsymbol{M}$ 也随之改变方向，使这一关系始终成立。因此 $\boldsymbol{L}$ 的端点在水平面内作圆周运动，自转轴绕竖直轴转动，即陀螺在进动，而不是倒下。

设 $\mathrm{d}t$ 内自转轴绕竖直轴转过 $\mathrm{d}\Theta$，则 $\lvert\mathrm{d}\boldsymbol{L}\rvert=L\sin\theta\,\mathrm{d}\Theta=M\,\mathrm{d}t$，进动角速度

$$
\varOmega=\frac{\mathrm{d}\Theta}{\mathrm{d}t}=\frac{M}{L\sin\theta}=\frac{mgr_C}{J\omega} .
$$
自转越快，进动越慢。进动稳定后，刚体的总角速度为 $\boldsymbol{\omega}+\boldsymbol{\varOmega}$；高速自转时 $\varOmega\ll\omega$，总角速度近似等于 $\boldsymbol{\omega}$，这正是上面的近似成立的条件。精确分析表明，自转轴在进动的同时还会有微小的上下周期性摆动，称为章动（nutation）。

这种回转效应有利也有弊。轮船转弯时，船上高速旋转的涡轮机转子的角动量要改变方向，轴承必须提供相应的力矩，承受附加的力，严重时会损坏轴承；反过来，大型陀螺稳定器的回转效应可以抵抗海浪引起的横摇，使船体保持稳定。

**例 5.7.1（地球的进动）** 地球近似为一个绕自转轴高速自转的扁球体，自转轴与公转轨道面（黄道面）的法线成约 $23.4^\circ$ 角。太阳和月球对地球赤道隆起部分的引力不均匀（离它们近的一侧受力大），产生一个力矩，使地球的自转轴绕黄道面的法线进动，周期约 $2.58\times10^4$ 年（岁差），其中月球的贡献约为太阳的两倍。结果北天极的方向在星空中缓慢移动：现在的北极星是小熊座 $\alpha$（勾陈一），约 1.2 万年后北天极将接近天琴座 $\alpha$（织女星）。

### 5.7.3. 自由度

**定义 5.7.1（自由度）** 确定一个力学系统在空间中的位置（位形）所需的独立坐标的数目，称为系统的**自由度**。

自由度与几何约束条件直接相关：

- 不受约束的质点自由度为 3，$x$、$y$、$z$ 互相独立；约束在曲面上运动的质点自由度为 2，如 $z=z(x,y)$；约束在曲线上运动的质点自由度为 1，如 $y=y(x)$、$z=z(x)$。
- 自由刚体的自由度为 6。刚体上不共线的三点 $A$、$B$、$C$ 一旦固定，刚体就被完全固定：$A$ 固定后刚体还能绕 $A$ 转动，再固定 $B$ 还能绕 $AB$ 转动，再固定 $C$ 刚体就不能动了。三点共有 9 个坐标，而 $AB$、$BC$、$CA$ 三个距离不变的条件使独立坐标减少 3 个，所以自由度为 6。

刚体的 6 个自由度可以分为基点平动的 3 个与绕基点转动的 3 个。转动常用三个 Euler 角（Euler angles）描述：进动角 $\psi$（自转轴绕固定轴转过的角度）、章动角 $\theta$（自转轴与固定轴的夹角）、自转角 $\varphi$（绕自转轴转过的角度）。受约束的刚体自由度减少：定点转动 3，平面运动 3，定轴转动 1。

这里的自由度是力学系统的位形自由度，与统计学中的自由度（独立观测数减去约束数）是不同的概念，尽管二者都是"独立变量的个数"。热学中分子的平动、转动与振动自由度（[5.2.1](/5.2.1)）就是本节概念的应用。

## 5.8. 刚体平面运动简介

### 5.8.1. 基本概念与运动学关系

刚体作平面运动时，任选一个与各点轨道平面平行的平面作为基面：与基面垂直的任一直线上的各点运动相同，所以基面上各点的运动就代表了刚体的运动。在基面上任选一点作为基点，过基点垂直于基面的直线称为基轴。基面上各点的运动可以分解为基点的平动（2 个自由度）与绕基点的转动（1 个自由度）；整个刚体的平面运动就是基轴的平动加绕基轴的转动。选质心为基点，便于分析动力学问题。

基面上任一点 $A$ 的速度为

$$
\boldsymbol{v}_A=\boldsymbol{v}_O+\boldsymbol{\omega}\times\boldsymbol{R},\qquad \boldsymbol{R}=\overrightarrow{OA},
$$
$\boldsymbol{v}_O$ 是基点 $O$ 的速度，$\boldsymbol{\omega}$ 垂直于基面，且与基点的选择无关（5.1.3 节）。

**定义 5.8.1（瞬心）** 刚体作平面运动时（$\omega\ne0$），基面上存在唯一一个瞬时速度为零的点 $P$，称为**瞬心**（瞬时转动中心）；过瞬心垂直于基面的直线称为瞬轴。

以瞬心为基点，$\boldsymbol{v}_A=\boldsymbol{\omega}\times\boldsymbol{R}$，$\boldsymbol{R}=\overrightarrow{PA}$，$\boldsymbol{v}_A\perp\boldsymbol{R}$：每一瞬时，刚体的运动就像绕瞬轴的纯转动，所以选瞬心为基点便于分析运动学问题。瞬心的位置一般随时间变化；瞬心的速度为零，加速度却不一定为零；瞬心可能在刚体内，也可能在刚体外。求瞬心的两个简便方法：

1. 已知一点 $A$ 的速度 $\boldsymbol{v}_A$ 与 $\boldsymbol{\omega}$：瞬心在过 $A$ 垂直于 $\boldsymbol{v}_A$ 的直线上，距离 $PA=v_A/\omega$，方向沿 $\boldsymbol{\omega}\times\boldsymbol{v}_A$。
2. 已知两点 $A$、$B$ 的速度方向（不平行）：过 $A$、$B$ 分别作速度的垂线，交点就是瞬心。

均匀圆柱（圆盘、圆环、球）在平面或曲面上滚动而无相对滑动，称为纯滚动（rolling without slipping）。纯滚动时接触点 $P$ 相对接触面静止，是瞬心。若接触面静止，半径为 $r$ 的滚动体质心 $C$ 的速度与切向加速度满足

$$
v_C=\omega r,\qquad a_C=\alpha r,
$$
在平面上 $a_C$ 就是质心的加速度。

### 5.8.2. 动力学关系

1. **质心运动定理**：$\boldsymbol{F}_{\mathrm{ext}}=m\boldsymbol{a}_C$。
2. 对通过质心的基轴的转动定律：$M_{\mathrm{ext},C}=J_C\alpha$。**质心系**一般不是**惯性系**，但平动**惯性力**等效地作用在质心上，对过质心的轴的力矩为零，所以转动定律形式不变（[5.1.3](/5.1.3) 中质心系的角动量定理）。
3. 对瞬轴：若瞬心的加速度沿瞬心与质心的连线，惯性力对瞬轴的力矩也为零，于是对瞬轴也有 $M_{\mathrm{ext},P}=J_P\alpha$。均匀圆柱在平面上纯滚动时，接触点的加速度指向质心，满足这一条件。
4. 角动量：对过质心的基轴，$M_{\mathrm{ext},C}=\dfrac{\mathrm{d}L_C}{\mathrm{d}t}$，$L_C=J_C\omega$；对平行于质心轴的固定轴 $O$，$L_O=J_C\omega+(\boldsymbol{r}_C\times m\boldsymbol{v}_C)_z$，$\boldsymbol{r}_C$ 是质心相对 $O$ 轴的垂直位矢。

**例 5.8.1** 质量 $m$、半径 $R$ 的均匀圆球在水平面上以质心速度 $v_C$ 作纯滚动。求它对地面内一条与运动方向垂直的固定轴 $O$ 的角动量，它守恒吗？

**解** $L_O=J_C\omega+mv_CR=\frac25mR^2\cdot\frac{v_C}{R}+mv_CR=\frac75mv_CR$（两项方向相同）。圆球匀速滚动时，重力（作用于质心）与支持力（作用于接触点）的作用线都竖直，与 $O$ 轴的水平距离相同、方向相反，对 $O$ 轴的力矩相互抵消，不需要摩擦力，所以 $L_O$ 守恒。

能量关系由 **König 定理**（[定理 4.10.1](/5.1.4#thm-4.10.1)），刚体的动能等于质心平动动能与绕过质心的基轴的转动动能之和：

$$
E_{\mathrm{k}}=\frac12mv_C^2+\frac12J_C\omega^2 .
$$
相应地，**动能定理**分为两部分：

$$
\Delta\Big(\frac12mv_C^2\Big)=\int\boldsymbol{F}_{\mathrm{ext}}\cdot\mathrm{d}\boldsymbol{r}_C,\qquad
\Delta\Big(\frac12J_C\omega^2\Big)=\int M_{\mathrm{ext},C}\,\mathrm{d}\theta,
$$
质心平动能的改变等于外力"对质心"所做的功（力乘以质心的位移），转动能的改变等于外力矩对过质心的基轴所做的功；二者之和 $\Delta E_{\mathrm{k}}$ 等于外力的总功。

**例 5.8.2** 质量 $m$、半径 $R$ 的均匀圆球在水平力 $F$ 作用下在水平面上作纯滚动，力的作用点 $A$ 在接触点 $P$ 与质心 $C$ 的连线上，$AC=d$（$A$ 在 $C$ 上方）。求接触点处的静摩擦力 $f$。

**解** 设摩擦力与 $F$ 同向（向前）。质心运动定理：$F+f=ma_C$。以使球向前滚动的转动方向为正，对质心轴的转动定律：$Fd-fR=J_C\alpha=\frac25mR^2\alpha$。纯滚动条件：$a_C=R\alpha$。解得

$$
f=\frac{5d-2R}{7R}F,\qquad a_C=\frac{5(d+R)}{7mR}F>0,\qquad \alpha=\frac{5(d+R)}{7mR^2}F>0 .
$$
$d>\frac25R$ 时 $f$ 与 $F$ 同向，$d=\frac25R$ 时 $f=0$（这一点是相对接触点的打击中心），$d<\frac25R$ 时 $f$ 与 $F$ 反向。球总是加速前进、加速转动。

**例 5.8.3** 质量 $m$、半径 $R$、对质心轴转动惯量 $J$ 的圆柱体在倾角为 $\theta$ 的固定斜面上由静止开始纯滚动。（1）接触点是否有摩擦力？若有，它起什么作用，是否做功？（2）求圆柱体下降高度 $h$ 时质心的速度 $v_C$、角速度 $\omega$ 与摩擦力 $f$。

**解**（1）在斜面**参考系**中不易直接判断。在以质心为基点的参考系中圆柱体作定轴转动，重力与斜面支持力对质心轴的力矩都为零；要使圆柱体加速转动，必须有静摩擦力，方向沿斜面向上（与质心运动方向相反），它对质心轴的力矩不为零。

在斜面参考系中，静摩擦力不做功：接触点 $O$ 的元位移

$$
\mathrm{d}W_f=\boldsymbol{f}\cdot\mathrm{d}\boldsymbol{r}_O=\boldsymbol{f}\cdot(\boldsymbol{v}_{O,C}+\boldsymbol{v}_C)\,\mathrm{d}t=f(\omega R-v_C)\,\mathrm{d}t=0,
$$
其中 $\boldsymbol{v}_{O,C}$ 是接触点相对质心的速度。也就是说，摩擦力对质心平动做负功 $-fv_C\,\mathrm{d}t$，同时它的力矩对转动做正功 $fR\,\mathrm{d}\theta=fR\omega\,\mathrm{d}t$，二者相等，总功为零：静摩擦力的作用是把一部分平动能转化为转动能。

（2）机械能守恒、质心运动定理与质心运动学：

$$
\frac12mv_C^2+\frac12J\omega^2=mgh,\qquad mg\sin\theta-f=ma_C,\qquad v_C^2=2a_C\frac{h}{\sin\theta},\qquad v_C=\omega R .
$$
解得

$$
v_C=\sqrt{\frac{2gh}{1+J/(mR^2)}},\qquad \omega=\frac{v_C}{R},\qquad f=\frac{mg\sin\theta}{1+mR^2/J}.
$$
求摩擦力也可以用质心运动定理、$a_C=R\alpha$ 加上对质心轴的转动定律 $fR=J\alpha$，或者加上对瞬轴的转动定律 $mgR\sin\theta=J_O\alpha$（$J_O=J+mR^2$）。由 $v_C$ 的表达式，$J/(mR^2)$ 越小滚得越快：同时从同一高度释放，实心球（$\frac25$）先于实心圆柱（$\frac12$），实心圆柱先于薄圆环（$1$）到达底部，与质量和半径无关。

**例 5.8.4（悠悠球）** 质量 $m$、半径 $R$ 的扁圆柱体（看作均匀圆盘，$J_C=\frac12mR^2$）上绕有细绳，绳的上端握在手中。（1）手不动，圆柱体自行下滚，求它下降的加速度与绳的拉力；（2）若手向上提使拉力 $T=2mg$，求圆柱体上升的加速度与手向上提的加速度。

**解**（1）质心运动定理 $mg-T=ma_C$，对质心轴的转动定律 $TR=\frac12mR^2\alpha$，绳不打滑且手不动时 $a_C=R\alpha$。解得 $a_C=\frac23g$，$T=\frac13mg$。

（2）$T-mg=ma_C$ 给出 $a_C=g$（向上）；$TR=\frac12mR^2\alpha$ 给出 $\alpha=4g/R$。绳与圆柱边缘之间不打滑，绳相对质心的加速度 $a'=R\alpha=4g$（向上），所以手向上的加速度 $a=a'+a_C=5g$。

## 小结

| 平动（质点） | 定轴转动（刚体） |
|---|---|
| 位移 $\Delta x$，速度 $v$，加速度 $a$ | 角位移 $\Delta\theta$，角速度 $\omega$，角加速度 $\alpha$ |
| 质量 $m$ | 转动惯量 $J=\int r_\perp^2\,\mathrm{d}m$ |
| 力 $F$，Newton 第二定律 $F=ma$ | 力矩 $M$，转动定律 $M=J\alpha$ |
| 功 $\int F\,\mathrm{d}x$，动能 $\frac12mv^2$ | 功 $\int M\,\mathrm{d}\theta$，转动动能 $\frac12J\omega^2$ |
| 动量 $mv$，冲量 $\int F\,\mathrm{d}t$ | 角动量 $J\omega$，冲量矩 $\int M\,\mathrm{d}t$ |
| 动量守恒 | 对轴的角动量守恒 |

平面运动 = 质心的平动（质心运动定理）+ 绕质心轴的转动（对质心轴的转动定律），动能由 König 定理相加；纯滚动的条件是 $v_C=\omega R$、$a_C=\alpha R$，静摩擦力不做功。

## 思考题

1. 实验室中怎样测量一个形状不规则的物体的转动惯量？
   提示：例 5.4.1 的落体法；或者把物体作为复摆、扭摆，测量小振动的周期（[5.1.6](/5.1.6)），由周期求 $J$。
2. 例 5.6.2 中，如果改用对粘土块与圆盘分别作隔离体分析，粘土块与圆盘之间的相互作用力该如何处理？
   提示：粘合后二者之间有未知的内力；分别列出粘土块的 Newton 方程与圆盘的转动定律、质心运动定理，内力在相加时抵消，结果与用整体的质心运动定理相同。
