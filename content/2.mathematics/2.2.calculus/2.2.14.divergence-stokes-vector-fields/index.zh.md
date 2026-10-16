---
title: Gauss 公式、Stokes 公式与场论
---

[2.2.13](/2.2.13) 的 Green 公式把平面区域上的二重积分与沿边界的**第二型曲线积分**联系起来。本章把它推广到空间：Gauss 公式把空间区域上的三重积分与边界闭曲面上的**第二型曲面积分**联系起来，Stokes 公式把曲面上的第二型曲面积分与沿边界曲线的第二型曲线积分联系起来。三个公式有共同的形式——"区域上某种导数的积分 = 边界上的积分"，与一元的**微积分基本定理**一脉相承；它们在现代数学中统一为微分形式的 Stokes 定理 $\int_M\mathrm{d}\omega=\int_{\partial M}\omega$。

公式中出现的"某种导数"就是向量场的散度与旋度。散度是单位体积流出的**通量**，度量场的"源"；旋度的分量是单位面积上的**环量**，度量场的"旋涡"。用梯度、散度、旋度这三种运算可以对向量场分类：积分与路径无关的保守场（引力场、静电场），没有源的无源场（不可压缩流体的速度场、磁场），以及两者兼备的调和场。保守场把 [2.2.10](/2.2.10) 中"微分形式的原函数"放到了向量场的语言里，也是物理中势能与能量守恒的数学基础。本章的公式是电磁学（Maxwell 方程组的积分形式与微分形式）、流体力学和偏微分方程（Laplace 方程、热方程）的基本工具。

## 14.1. 梯度、散度与旋度

### 14.1.1. Hamilton 算子与梯度

本节中 $f,g$ 是**数量场**，$\boldsymbol{u},\boldsymbol{v}$ 是**向量场**（定义 13.3.1），$\boldsymbol{v}=(X,Y,Z)=X\boldsymbol{i}+Y\boldsymbol{j}+Z\boldsymbol{k}$，所涉及的偏导数都假定连续。

**定义 14.1.1（Hamilton 算子）** 称形式向量

$$
\nabla=\frac{\partial}{\partial x}\boldsymbol{i}+\frac{\partial}{\partial y}\boldsymbol{j}+\frac{\partial}{\partial z}\boldsymbol{k}
$$
为 **Hamilton 算子**（读作 nabla）。它作用于数量场得到**梯度** $\operatorname{grad}f=\nabla f=(f_x,f_y,f_z)$（定义 10.6.2），是从数量场到向量场的运算。

梯度的运算法则与一元导数相同：$\nabla(\alpha f+\beta g)=\alpha\nabla f+\beta\nabla g$，$\nabla(fg)=f\nabla g+g\nabla f$，$\nabla\big(\frac fg\big)=\frac{g\nabla f-f\nabla g}{g^2}$，$\nabla\varphi(f)=\varphi'(f)\nabla f$。若 $\boldsymbol{v}=\nabla f$，则称 $f$ 为 $\boldsymbol{v}$ 的势函数（14.4 节）。

### 14.1.2. 散度

**定义 14.1.2（散度）** 向量场 $\boldsymbol{v}=(X,Y,Z)$ 的**散度**是数量场

$$
\operatorname{div}\boldsymbol{v}=\nabla\cdot\boldsymbol{v}=\frac{\partial X}{\partial x}+\frac{\partial Y}{\partial y}+\frac{\partial Z}{\partial z}.
$$
平面向量场 $\boldsymbol{v}=(X,Y)$ 的散度为 $\operatorname{div}\boldsymbol{v}=\frac{\partial X}{\partial x}+\frac{\partial Y}{\partial y}$。

"$\nabla\cdot$"只是记号：把 $\nabla$ 当作向量与 $\boldsymbol{v}$ 作**内积**。散度的物理意义（单位体积的通量）在 14.2.3 中由 Gauss 公式给出。

**性质 14.1.1** $\nabla\cdot(\alpha\boldsymbol{u}+\beta\boldsymbol{v})=\alpha\nabla\cdot\boldsymbol{u}+\beta\nabla\cdot\boldsymbol{v}$；$\nabla\cdot(f\boldsymbol{v})=f\,\nabla\cdot\boldsymbol{v}+\nabla f\cdot\boldsymbol{v}$。

**证明** 记 $\boldsymbol{v}=(v_1,v_2,v_3)$，由乘积的求导法则，$\frac{\partial(fv_1)}{\partial x}+\frac{\partial(fv_2)}{\partial y}+\frac{\partial(fv_3)}{\partial z}=f\Big(\frac{\partial v_1}{\partial x}+\frac{\partial v_2}{\partial y}+\frac{\partial v_3}{\partial z}\Big)+\Big(v_1\frac{\partial f}{\partial x}+v_2\frac{\partial f}{\partial y}+v_3\frac{\partial f}{\partial z}\Big)$。$\square$

### 14.1.3. 旋度

**定义 14.1.3（旋度）** 向量场 $\boldsymbol{v}=(X,Y,Z)$ 的**旋度**是向量场

$$
\operatorname{rot}\boldsymbol{v}=\nabla\times\boldsymbol{v}=\begin{vmatrix}\boldsymbol{i}&\boldsymbol{j}&\boldsymbol{k}\\ \dfrac{\partial}{\partial x}&\dfrac{\partial}{\partial y}&\dfrac{\partial}{\partial z}\\ X&Y&Z\end{vmatrix}=\Big(\frac{\partial Z}{\partial y}-\frac{\partial Y}{\partial z},\ \frac{\partial X}{\partial z}-\frac{\partial Z}{\partial x},\ \frac{\partial Y}{\partial x}-\frac{\partial X}{\partial y}\Big).
$$
平面向量场 $\boldsymbol{v}=(X(x,y),Y(x,y))$ 看作 $(X,Y,0)$，其旋度为 $\operatorname{rot}\boldsymbol{v}=\Big(\dfrac{\partial Y}{\partial x}-\dfrac{\partial X}{\partial y}\Big)\boldsymbol{k}$。

行列式按第一行展开，第二行的"乘以"第三行理解为求偏导（这是向量积公式的形式推广，定义 11.1.1）。英文文献多写作 $\operatorname{curl}\boldsymbol{v}$。

**性质 14.1.2**

- $\nabla\times(\alpha\boldsymbol{u}+\beta\boldsymbol{v})=\alpha\nabla\times\boldsymbol{u}+\beta\nabla\times\boldsymbol{v}$；
- $\nabla\times(f\boldsymbol{v})=f\,\nabla\times\boldsymbol{v}+\nabla f\times\boldsymbol{v}$；
- $\nabla\cdot(\boldsymbol{u}\times\boldsymbol{v})=\boldsymbol{v}\cdot(\nabla\times\boldsymbol{u})-\boldsymbol{u}\cdot(\nabla\times\boldsymbol{v})$。

**证明** 第二式的第一个分量为 $\frac{\partial(fv_3)}{\partial y}-\frac{\partial(fv_2)}{\partial z}=f\big(\frac{\partial v_3}{\partial y}-\frac{\partial v_2}{\partial z}\big)+\big(\frac{\partial f}{\partial y}v_3-\frac{\partial f}{\partial z}v_2\big)$，后一项正是 $\nabla f\times\boldsymbol{v}$ 的第一个分量，其余分量类似。第三式：$\boldsymbol{u}\times\boldsymbol{v}=(u_2v_3-u_3v_2,\,u_3v_1-u_1v_3,\,u_1v_2-u_2v_1)$，求散度后按乘积法则展开，把含 $\boldsymbol{u}$ 的导数的项归在一起得 $v_1\big(\frac{\partial u_3}{\partial y}-\frac{\partial u_2}{\partial z}\big)+v_2\big(\frac{\partial u_1}{\partial z}-\frac{\partial u_3}{\partial x}\big)+v_3\big(\frac{\partial u_2}{\partial x}-\frac{\partial u_1}{\partial y}\big)=\boldsymbol{v}\cdot(\nabla\times\boldsymbol{u})$，含 $\boldsymbol{v}$ 的导数的项归在一起得 $-\boldsymbol{u}\cdot(\nabla\times\boldsymbol{v})$。$\square$

**例 14.1.1** $\boldsymbol{v}=(y,z,x)$：$\operatorname{div}\boldsymbol{v}=0$，$\operatorname{rot}\boldsymbol{v}=(0-1,\,0-1,\,0-1)=(-1,-1,-1)$。$\boldsymbol{v}=(y^2,z^2,x^2)$：$\operatorname{div}\boldsymbol{v}=0$，$\operatorname{rot}\boldsymbol{v}=(-2z,-2x,-2y)$。刚体绕 $z$ 轴以角速度 $\omega$ 转动时，速度场 $\boldsymbol{v}=\omega(-y,x,0)$ 的旋度为 $(0,0,2\omega)$：旋度沿转轴方向，大小是角速度的两倍。

### 14.1.4. 二阶运算与 Laplace 算子

**定理 14.1.1** 设 $f$ 与 $\boldsymbol{v}$ 的各分量有连续的二阶偏导数，则

$$
\operatorname{rot}\operatorname{grad}f=\nabla\times\nabla f=\boldsymbol{0},\qquad\operatorname{div}\operatorname{rot}\boldsymbol{v}=\nabla\cdot(\nabla\times\boldsymbol{v})=0.
$$

**证明** $\nabla\times\nabla f$ 的第一个分量为 $f_{zy}-f_{yz}=0$（定理 10.4.1：连续的混合偏导数相等），其余类似。$\nabla\cdot(\nabla\times\boldsymbol{v})=(Z_{yx}-Y_{zx})+(X_{zy}-Z_{xy})+(Y_{xz}-X_{yz})=0$。$\square$

形式上，这对应于向量代数中的 $\boldsymbol{a}\times\boldsymbol{a}=\boldsymbol{0}$ 与 $\boldsymbol{a}\cdot(\boldsymbol{a}\times\boldsymbol{b})=0$。14.4、14.5 节将讨论它们的逆命题：无旋场是否是梯度场，无源场是否是旋度场——答案取决于区域的形状。

**定义 14.1.4（Laplace 算子）** 称

$$
\Delta f=\nabla\cdot\nabla f=\operatorname{div}\operatorname{grad}f=\frac{\partial^2f}{\partial x^2}+\frac{\partial^2f}{\partial y^2}+\frac{\partial^2f}{\partial z^2}
$$
为 $f$ 的 Laplace 算子，$\Delta=\nabla^2$ 称为 **Laplace 算子**。

用旋度与散度的语言，Green 公式的两种形式（定理 13.4.1、13.4.2）写成

$$
\oint_{\partial D}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\iint_D(\operatorname{rot}\boldsymbol{v})\cdot\boldsymbol{k}\,\mathrm{d}\sigma,\qquad\oint_{\partial D}\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}l=\iint_D\operatorname{div}\boldsymbol{v}\,\mathrm{d}\sigma.
$$
下面两节分别把它们推广到空间：后者成为 Gauss 公式，前者成为 Stokes 公式。

## 14.2. Gauss 公式

### 14.2.1. Gauss 公式

**定理 14.2.1（Gauss 公式）** 设 $\Omega\subset\mathbb{R}^3$ 是有界闭区域，其边界 $\partial\Omega$ 由有限片光滑曲面组成，取外侧；$\boldsymbol{v}=(X,Y,Z)$ 在 $\Omega$ 上连续可微。则

$$
\oiint_{\partial\Omega}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=\iiint_\Omega\operatorname{div}\boldsymbol{v}\,\mathrm{d}V,
$$
即

$$
\oiint_{\partial\Omega}X\,\mathrm{d}y\wedge\mathrm{d}z+Y\,\mathrm{d}z\wedge\mathrm{d}x+Z\,\mathrm{d}x\wedge\mathrm{d}y=\iiint_\Omega\Big(\frac{\partial X}{\partial x}+\frac{\partial Y}{\partial y}+\frac{\partial Z}{\partial z}\Big)\mathrm{d}V.
$$

**证明** 只需证 $\oiint_{\partial\Omega}Z\,\mathrm{d}x\wedge\mathrm{d}y=\iiint_\Omega\frac{\partial Z}{\partial z}\,\mathrm{d}V$，另两式同理。先设 $\Omega=\{(x,y,z)\mid(x,y)\in D_{xy},\ z_1(x,y)\le z\le z_2(x,y)\}$。用**三重积分**的投影法（定理 12.3.1），

$$
\iiint_\Omega\frac{\partial Z}{\partial z}\,\mathrm{d}V=\iint_{D_{xy}}\Big(\int_{z_1}^{z_2}\frac{\partial Z}{\partial z}\,\mathrm{d}z\Big)\mathrm{d}x\,\mathrm{d}y=\iint_{D_{xy}}\big[Z(x,y,z_2(x,y))-Z(x,y,z_1(x,y))\big]\mathrm{d}x\,\mathrm{d}y.
$$
另一方面，$\partial\Omega$ 由上底 $z=z_2$（外侧即上侧）、下底 $z=z_1$（外侧即下侧）和侧面（垂直于 $xOy$ 面，$\mathrm{d}x\wedge\mathrm{d}y=0$）组成，由定理 13.5.1，$\oiint_{\partial\Omega}Z\,\mathrm{d}x\wedge\mathrm{d}y$ 恰好等于上式右端。一般区域用辅助曲面分成有限块，每块都是上述情形；辅助曲面在相邻两块中取相反的侧，积分抵消。$\square$

Gauss 公式也称为散度定理。在平面上，它就是 Green 公式的通量形式。使用时注意：$\partial\Omega$ 取外侧（$\Omega$ 有空腔时，内层边界取内侧，即仍指向 $\Omega$ 之外）；$\boldsymbol{v}$ 在 $\Omega$ 的每一点都要连续可微。取 $\boldsymbol{v}=\frac13(x,y,z)$ 得到用曲面积分表示的体积：$V(\Omega)=\frac13\oiint_{\partial\Omega}x\,\mathrm{d}y\wedge\mathrm{d}z+y\,\mathrm{d}z\wedge\mathrm{d}x+z\,\mathrm{d}x\wedge\mathrm{d}y$。例如半径为 $R$ 的球，$\boldsymbol{v}\cdot\boldsymbol{n}=\frac R3$，$V=\frac R3\cdot4\pi R^2=\frac43\pi R^3$。

### 14.2.2. 应用

**例 14.2.1** 设 $\Omega=\{x^2+y^2\le1,\ 0\le z\le1\}$，计算 $\oiint_{\partial\Omega}(x^3+\sin yz)\,\mathrm{d}y\wedge\mathrm{d}z+(y^3+\mathrm{e}^{xz})\,\mathrm{d}z\wedge\mathrm{d}x+\big[3z+\ln(x^2+y^2+1)\big]\,\mathrm{d}x\wedge\mathrm{d}y$（外侧）。直接计算无从下手，而散度为 $3x^2+3y^2+3$，用**柱坐标**，

$$
\iiint_\Omega3(x^2+y^2+1)\,\mathrm{d}V=3\int_0^{2\pi}\mathrm{d}\theta\int_0^1(r^2+1)r\,\mathrm{d}r\int_0^1\mathrm{d}z=\frac{9\pi}2.
$$

**例 14.2.2** 用 Gauss 公式重算例 13.5.2：$\oiint_Sy^2z\,\mathrm{d}x\wedge\mathrm{d}y=\iiint_{x^2+y^2+z^2\le R^2}y^2\,\mathrm{d}V=\frac13\iiint\rho^2\,\mathrm{d}V=\frac13\cdot\frac{4\pi R^5}5=\frac{4\pi R^5}{15}$（由轮换对称性 $\iiint x^2=\iiint y^2=\iiint z^2$）。

**例 14.2.3（补面）** 用 Gauss 公式重算例 13.5.4（锥面 $S\colon z=\sqrt{x^2+y^2}$，$0\le z\le h$，外侧）。补上圆盘 $S_1\colon z=h$，$x^2+y^2\le h^2$，取上侧，$S+S_1$ 是锥体 $\Omega$ 的外侧边界。$\boldsymbol{v}=(y-z,z-x,x-y)$ 的散度为 $0$，所以

$$
\iint_S=\oiint_{S+S_1}-\iint_{S_1}=0-\iint_{x^2+y^2\le h^2}(x-y)\,\mathrm{d}x\,\mathrm{d}y=0.
$$
同样，例 13.5.3 补上上下两个圆面后，$\oiint=\iiint_\Omega(y-z)\,\mathrm{d}V=-\iiint_\Omega z\,\mathrm{d}V=-2\pi$，两个圆面上 $\iint(x-y)\,\mathrm{d}x\,\mathrm{d}y=0$、$\mathrm{d}y\wedge\mathrm{d}z=0$，所以积分为 $-2\pi$，与直接计算一致。

**例 14.2.4** 计算 $I=\iint_S(y^2-x)\,\mathrm{d}y\wedge\mathrm{d}z+(z^2-y)\,\mathrm{d}z\wedge\mathrm{d}x+(x^2-z)\,\mathrm{d}x\wedge\mathrm{d}y$，$S\colon z=1-x^2-y^2$，$z\ge0$，取上侧。补上 $S_1\colon z=0$，$x^2+y^2\le1$，取下侧，$\Omega$ 为抛物面与平面所围的立体。散度为 $-3$，$V(\Omega)=\int_0^{2\pi}\mathrm{d}\theta\int_0^1(1-r^2)r\,\mathrm{d}r=\frac\pi2$，所以 $\oiint_{S+S_1}=-\frac{3\pi}2$。$S_1$ 上 $z=0$，$\mathrm{d}y\wedge\mathrm{d}z=\mathrm{d}z\wedge\mathrm{d}x=0$，

$$
\iint_{S_1}x^2\,\mathrm{d}x\wedge\mathrm{d}y=-\iint_{x^2+y^2\le1}x^2\,\mathrm{d}x\,\mathrm{d}y=-\frac\pi4,\qquad I=-\frac{3\pi}2+\frac\pi4=-\frac{5\pi}4.
$$
直接计算（分前后两片向 $yOz$ 面投影等）也能得到 $-\frac{5\pi}4$，但要算三个各不相同的二重积分。

**例 14.2.5** 设 $\Omega$ 由柱面 $x^2+y^2=1$ 与平面 $z=0$、$x+z=1$ 围成，计算 $I=\oiint_{\partial\Omega}2xz\,\mathrm{d}y\wedge\mathrm{d}z+xz\cos y\,\mathrm{d}z\wedge\mathrm{d}x+3yz\sin x\,\mathrm{d}x\wedge\mathrm{d}y$（外侧）。由 Gauss 公式，

$$
I=\iiint_\Omega(2z-xz\sin y+3y\sin x)\,\mathrm{d}V.
$$
$\Omega$ 关于 $zOx$ 面对称，$xz\sin y$ 与 $y\sin x$ 关于 $y$ 是奇函数，积分为零。所以

$$
I=\iint_{x^2+y^2\le1}\mathrm{d}x\,\mathrm{d}y\int_0^{1-x}2z\,\mathrm{d}z=\iint_{x^2+y^2\le1}(1-x)^2\,\mathrm{d}x\,\mathrm{d}y=\pi+\frac\pi4=\frac{5\pi}4.
$$
若直接计算，底面贡献 $0$；斜面上 $\boldsymbol{n}=\frac{(1,0,1)}{\sqrt2}$，$\mathrm{d}S=\sqrt2\,\mathrm{d}x\,\mathrm{d}y$，贡献 $\iint[2x(1-x)+3y(1-x)\sin x]\,\mathrm{d}x\,\mathrm{d}y=-\frac\pi2$；侧面上 $\boldsymbol{n}=(x,y,0)$，用 $\mathrm{d}S=\mathrm{d}\theta\,\mathrm{d}z$，贡献 $\int_0^{2\pi}\mathrm{d}\theta\int_0^{1-\cos\theta}2\cos^2\theta\,z\,\mathrm{d}z=\frac{7\pi}4$（$xyz\cos y$ 一项由对称性为零）。合计 $\frac{5\pi}4$。比较可见 Gauss 公式把三个曲面积分换成一个简单的三重积分。

**例 14.2.6（挖去奇点）** 设 $S$ 是不经过原点的光滑闭曲面，取外侧，计算 $I=\oiint_S\dfrac{x\,\mathrm{d}y\wedge\mathrm{d}z+y\,\mathrm{d}z\wedge\mathrm{d}x+z\,\mathrm{d}x\wedge\mathrm{d}y}{(x^2+y^2+z^2)^{3/2}}$。记 $\rho=\sqrt{x^2+y^2+z^2}$，$\boldsymbol{v}=\frac{(x,y,z)}{\rho^3}$。在原点以外，$\frac{\partial}{\partial x}\frac x{\rho^3}=\frac{\rho^2-3x^2}{\rho^5}$，三项相加得 $\operatorname{div}\boldsymbol{v}=\frac{3\rho^2-3\rho^2}{\rho^5}=0$。

- 若 $S$ 不包围原点，由 Gauss 公式 $I=0$。
- 若 $S$ 包围原点，取小球面 $S_\varepsilon\colon\rho=\varepsilon$ 位于 $S$ 内部，在 $S$ 与 $S_\varepsilon$ 之间的区域上用 Gauss 公式（$S_\varepsilon$ 取内侧）得 $I=\oiint_{S_\varepsilon}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}$（$S_\varepsilon$ 取外侧）。在 $S_\varepsilon$ 上 $\boldsymbol{v}\cdot\boldsymbol{n}=\frac1{\varepsilon^2}$，所以 $I=\frac1{\varepsilon^2}\cdot4\pi\varepsilon^2=4\pi$。

这是例 13.4.6 的空间版本。物理上，点电荷 $q$ 的电场 $\boldsymbol{E}=\frac{q}{4\pi\varepsilon_0}\frac{(x,y,z)}{\rho^3}$ 穿过任一包围它的闭曲面的通量都是 $\frac q{\varepsilon_0}$，不包围时为 $0$：这就是 Gauss 定律。

### 14.2.3. 散度的物理意义

**定理 14.2.2** 设 $\boldsymbol{v}$ 在 $M_0$ 的某邻域内连续可微，$\Omega$ 是含 $M_0$ 的小区域（如以 $M_0$ 为中心的球），体积为 $V(\Omega)$，则

$$
\operatorname{div}\boldsymbol{v}(M_0)=\lim_{\Omega\to M_0}\frac1{V(\Omega)}\oiint_{\partial\Omega}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S},
$$
其中 $\Omega\to M_0$ 指 $\Omega$ 的直径趋于零。

**证明** 由 Gauss 公式与三重积分的**积分中值定理**，$\oiint_{\partial\Omega}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=\iiint_\Omega\operatorname{div}\boldsymbol{v}\,\mathrm{d}V=\operatorname{div}\boldsymbol{v}(M)\,V(\Omega)$，$M\in\Omega$。$\Omega\to M_0$ 时 $M\to M_0$，由 $\operatorname{div}\boldsymbol{v}$ 的连续性即得。$\square$

所以散度是通量的体密度：把 $\boldsymbol{v}$ 看作流速，$\operatorname{div}\boldsymbol{v}(M_0)$ 是单位时间内从 $M_0$ 附近单位体积中流出的流体量。$\operatorname{div}\boldsymbol{v}>0$ 的点是"源"，$<0$ 的点是"汇"，$=0$ 处既不产生也不吸收流体。这个极限式不依赖坐标系，因此散度是与坐标选取无关的量；以它作为散度的定义，再由 Gauss 公式推出坐标公式，是另一种常见的讲法。

![左：源（散度为正）与汇（散度为负），小圆上的外法向量与向外的通量；右：散度为零的场 (x, -y)，流入任一闭曲线的量等于流出的量](./plots/divergence-flux.py)

## 14.3. Stokes 公式

### 14.3.1. Stokes 公式

回忆有向曲面边界的定向（[2.2.13](/2.2.13) 有向曲面一节）：人站在曲面 $S$ 的正侧沿边界 $\partial S$ 前进时，$S$ 总在左侧。等价地，右手四指沿 $\partial S$ 的方向弯曲时，拇指指向 $S$ 的正侧法向量（右手法则）。

**定理 14.3.1（Stokes 公式）** 设 $S$ 是分片光滑的有界有向曲面，边界 $\partial S$ 是逐段光滑的闭曲线，按右手法则定向；$\boldsymbol{v}=(X,Y,Z)$ 在包含 $S$ 的某个区域上连续可微。则

$$
\oint_{\partial S}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\iint_S(\operatorname{rot}\boldsymbol{v})\cdot\mathrm{d}\boldsymbol{S},
$$
即

$$
\oint_{\partial S}X\,\mathrm{d}x+Y\,\mathrm{d}y+Z\,\mathrm{d}z=\iint_S\begin{vmatrix}\mathrm{d}y\wedge\mathrm{d}z&\mathrm{d}z\wedge\mathrm{d}x&\mathrm{d}x\wedge\mathrm{d}y\\ \dfrac{\partial}{\partial x}&\dfrac{\partial}{\partial y}&\dfrac{\partial}{\partial z}\\ X&Y&Z\end{vmatrix}.
$$

**证明** 设 $S$ 是 $z=z(x,y)$（$z$ 有连续的二阶偏导数）在 $D_{xy}$ 上的图像，取上侧；一般曲面分片后相加，公共边界上的曲线积分抵消。只证 $\oint_{\partial S}X\,\mathrm{d}x=\iint_S\frac{\partial X}{\partial z}\,\mathrm{d}z\wedge\mathrm{d}x-\frac{\partial X}{\partial y}\,\mathrm{d}x\wedge\mathrm{d}y$，$Y$、$Z$ 两项同理。$\partial S$ 在 $xOy$ 面上的投影是 $\partial D_{xy}$（正向），沿 $\partial S$ 有 $z=z(x,y)$，所以

$$
\oint_{\partial S}X(x,y,z)\,\mathrm{d}x=\oint_{\partial D_{xy}}X(x,y,z(x,y))\,\mathrm{d}x=-\iint_{D_{xy}}\Big(\frac{\partial X}{\partial y}+\frac{\partial X}{\partial z}z_y\Big)\mathrm{d}x\,\mathrm{d}y,
$$
后一步是 Green 公式与**链式法则**。另一方面，由定理 13.5.1（1），对向量场 $\big(0,\frac{\partial X}{\partial z},-\frac{\partial X}{\partial y}\big)$，

$$
\iint_S\frac{\partial X}{\partial z}\,\mathrm{d}z\wedge\mathrm{d}x-\frac{\partial X}{\partial y}\,\mathrm{d}x\wedge\mathrm{d}y=\iint_{D_{xy}}\Big(-\frac{\partial X}{\partial z}z_y-\frac{\partial X}{\partial y}\Big)\mathrm{d}x\,\mathrm{d}y.
$$
两式相等。$\square$

几点说明：

- $S$ 是 $xOy$ 面上的区域（取上侧）、$\boldsymbol{v}=(X(x,y),Y(x,y),0)$ 时，Stokes 公式就是 Green 公式。
- 只要边界相同、定向相容，$\iint_S\operatorname{rot}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}$ 与曲面 $S$ 的选取无关。若 $S_1$、$S_2$ 有相同的边界且 $S_1$ 与 $S_2^-$ 合成一个闭曲面（围成区域 $\Omega$，$\boldsymbol{v}$ 在 $\Omega$ 上连续可微），这也可由 Gauss 公式与 $\operatorname{div}\operatorname{rot}\boldsymbol{v}=0$ 看出。因此计算曲线积分时可以选最简单的曲面，通常是平面片。
- 闭曲面没有边界，所以 $\oiint_S\operatorname{rot}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=0$（把闭曲面切成两片，两片的边界相同、方向相反）。

### 14.3.2. 应用

**例 14.3.1** 计算 $I=\oint_L(y-z)\,\mathrm{d}x+(z-x)\,\mathrm{d}y+(x-y)\,\mathrm{d}z$，$L$ 为柱面 $x^2+y^2=R^2$ 与平面 $\frac xa+\frac zb=1$（$a,b>0$）的交线，从 $z$ 轴正向往下看为逆时针。$\operatorname{rot}\boldsymbol{v}=(-2,-2,-2)$。取 $S$ 为平面上被 $L$ 围成的椭圆片，取上侧（与 $L$ 的方向符合右手法则）。$S\colon z=b\big(1-\frac xa\big)$，$z_x=-\frac ba$，$z_y=0$，由定理 13.5.1（1），

$$
I=\iint_{x^2+y^2\le R^2}\Big[(-2)\frac ba+0+(-2)\Big]\mathrm{d}x\,\mathrm{d}y=-2\pi R^2\Big(1+\frac ba\Big).
$$
直接用参数 $x=R\cos t$，$y=R\sin t$，$z=b\big(1-\frac Ra\cos t\big)$ 计算，结果相同。

![Stokes 公式：平面 x/a + z/b = 1 上被柱面截出的椭圆片 S，取上侧时边界 L 的诱导方向（从上往下看逆时针）](./plots/stokes-surface.py)

**例 14.3.2** 计算 $I=\oint_Ly\,\mathrm{d}x+z\,\mathrm{d}y+x\,\mathrm{d}z$，$L$ 为球面 $x^2+y^2+z^2=a^2$ 与平面 $x+z=a$ 的交线，从上往下看为逆时针。$\operatorname{rot}\boldsymbol{v}=(-1,-1,-1)$。$L$ 是平面上的圆：球心到平面的距离为 $\frac a{\sqrt2}$，所以半径为 $\frac a{\sqrt2}$。取 $S$ 为平面上的圆盘，上侧单位法向量 $\boldsymbol{n}=\frac{(1,0,1)}{\sqrt2}$，化为第一型曲面积分：

$$
I=\iint_S(-1,-1,-1)\cdot\frac{(1,0,1)}{\sqrt2}\,\mathrm{d}S=-\sqrt2\cdot\pi\Big(\frac a{\sqrt2}\Big)^2=-\frac{\pi a^2}{\sqrt2}.
$$
也可以直接计算：$L$ 的参数方程为 $x=a\cos^2t$，$y=\sqrt2a\sin t\cos t$，$z=a\sin^2t$（$0\le t\le\pi$），代入得 $a^2\int_0^\pi(-2\sqrt2\sin^2t\cos^2t+\sqrt2\sin^2t\cos2t+2\sin t\cos^3t)\,\mathrm{d}t=-\frac{\pi a^2}{\sqrt2}$；参数方程好算，但不易想到。

**例 14.3.3** 计算 $I=\oint_L(y^2-z^2)\,\mathrm{d}x+(z^2-x^2)\,\mathrm{d}y+(x^2-y^2)\,\mathrm{d}z$，$L$ 为平面 $x+y+z=\frac32a$ 截立方体 $[0,a]^3$ 表面所得的截痕，从上往下看为逆时针。截痕是正六边形，顶点是立方体六条棱的中点，边长 $\frac a{\sqrt2}$，面积 $\frac{3\sqrt3}2\cdot\frac{a^2}2=\frac{3\sqrt3}4a^2$。$\operatorname{rot}\boldsymbol{v}=-2(y+z,\,z+x,\,x+y)$，平面上侧单位法向量 $\boldsymbol{n}=\frac{(1,1,1)}{\sqrt3}$，在 $S$ 上

$$
\operatorname{rot}\boldsymbol{v}\cdot\boldsymbol{n}=-\frac{4(x+y+z)}{\sqrt3}=-\frac{6a}{\sqrt3}=-2\sqrt3a,\qquad I=-2\sqrt3a\cdot\frac{3\sqrt3}4a^2=-\frac92a^3.
$$
若直接计算，要分六段；由轮换对称性只需算两段，结果相同。

**例 14.3.4** 设 $L$ 为柱面 $x^2+y^2=1$ 与平面 $x+2y+z=3$ 的交线，从 $z$ 轴正向往下看为逆时针。$\oint_Lx^2\,\mathrm{d}x+y^2\,\mathrm{d}y+z^2\,\mathrm{d}z=0$，因为被积式是 $\frac13\mathrm{d}(x^2+y^2+z^2)$（旋度为零）；而 $\oint_Lz\,\mathrm{d}x+x\,\mathrm{d}y+y\,\mathrm{d}z$ 中 $\operatorname{rot}\boldsymbol{v}=(1,1,1)$，取平面片 $z=3-x-2y$ 的上侧，$-z_x=1$，$-z_y=2$，积分为 $\iint_{x^2+y^2\le1}(1+2+1)\,\mathrm{d}x\,\mathrm{d}y=4\pi$。

### 14.3.3. 旋度的物理意义

**定理 14.3.2** 设 $\boldsymbol{v}$ 在 $M_0$ 的某邻域内连续可微，$\boldsymbol{n}_0$ 是单位向量，$S$ 是过 $M_0$、在 $M_0$ 处法向量为 $\boldsymbol{n}_0$ 的小曲面（如垂直于 $\boldsymbol{n}_0$ 的小圆盘），面积为 $A(S)$，边界按右手法则定向。则

$$
\lim_{S\to M_0}\frac1{A(S)}\oint_{\partial S}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\operatorname{rot}\boldsymbol{v}(M_0)\cdot\boldsymbol{n}_0.
$$

**证明** 由 Stokes 公式与积分中值定理，$\oint_{\partial S}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\iint_S\operatorname{rot}\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}S=(\operatorname{rot}\boldsymbol{v}\cdot\boldsymbol{n})(M)\,A(S)$，$M\in S$，令 $S\to M_0$ 即得。$\square$

左端称为 $\boldsymbol{v}$ 在 $M_0$ 处绕 $\boldsymbol{n}_0$ 的环量面密度。所以旋度在任一方向上的投影就是绕该方向的环量面密度；由 **Cauchy–Schwarz 不等式**，$\boldsymbol{n}_0$ 取 $\operatorname{rot}\boldsymbol{v}(M_0)$ 的方向时环量面密度最大，最大值为 $\|\operatorname{rot}\boldsymbol{v}(M_0)\|$。这给出旋度不依赖坐标系的刻画：旋度的方向是场在该点附近旋转最强的转轴（按右手法则），长度是最大的环量面密度。平面场的散度、旋度也可以分别看作单位面积的通量与环量（Green 公式的两种形式）。

![左：刚体转动场 (-y, x) 处处有旋度 2k，环量随圆周所围面积增大；右：涡旋场 (-y, x)/(x^2+y^2) 在原点外无旋，但绕原点的环量恒为 2π](./plots/curl-circulation.py)

## 14.4. 保守场与势函数

### 14.4.1. 基本概念

例 13.3.3 与例 13.3.6 表明，有些向量场沿两点之间任何路径的积分都相同。本节中 $\Omega$ 是 $\mathbb{R}^2$ 或 $\mathbb{R}^3$ 中的**区域**（连通开集），曲线都是 $\Omega$ 中逐段光滑的有向曲线。平面情形与空间情形完全平行，一并叙述。

**定义 14.4.1（保守场）** 设 $\boldsymbol{v}$ 是 $\Omega$ 上的连续向量场。若对 $\Omega$ 中任意两点 $A,B$，积分 $\int_L\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}$ 对 $\Omega$ 中所有从 $A$ 到 $B$ 的曲线 $L$ 都相同（即积分与路径无关），则称 $\boldsymbol{v}$ 为 $\Omega$ 上的**保守场**，此时积分记作 $\int_A^B\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}$。

**定义 14.4.2（有势场与势函数）** 若存在 $\Omega$ 上的可微函数 $f$，使 $\nabla f=\boldsymbol{v}$，即 $\mathrm{d}f=X\,\mathrm{d}x+Y\,\mathrm{d}y+Z\,\mathrm{d}z$，则称 $\boldsymbol{v}$ 为 $\Omega$ 上的**有势场**，$f$ 为 $\boldsymbol{v}$ 的**势函数**。

$f$ 是 $\boldsymbol{v}$ 的势函数，等价于 $f$ 是微分形式 $X\,\mathrm{d}x+Y\,\mathrm{d}y+Z\,\mathrm{d}z$ 的**原函数**（定义 10.5.2），此时称该微分形式为全微分式（恰当微分）。区域上的两个势函数之差为常数（梯度为零的函数在区域上为常数）。物理学中习惯取势能 $U=-f$，使 $\boldsymbol{F}=-\nabla U$。

**定义 14.4.3（无旋场）** 若连续可微向量场 $\boldsymbol{v}$ 在 $\Omega$ 上处处满足 $\operatorname{rot}\boldsymbol{v}=\boldsymbol{0}$，则称 $\boldsymbol{v}$ 为 $\Omega$ 上的**无旋场**。平面场无旋即 $\dfrac{\partial Y}{\partial x}=\dfrac{\partial X}{\partial y}$。

### 14.4.2. 保守场的判定

**定理 14.4.1** 设 $\boldsymbol{v}$ 是区域 $\Omega$ 上的连续向量场，则以下三条等价：

1. $\boldsymbol{v}$ 是 $\Omega$ 上的保守场；
2. 对 $\Omega$ 中任意逐段光滑的闭曲线 $L$，$\oint_L\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=0$；
3. $\boldsymbol{v}$ 是 $\Omega$ 上的有势场。

且此时对势函数 $f$ 有 $\int_A^B\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=f(B)-f(A)$（曲线积分的 Newton–Leibniz 公式）。若 $\boldsymbol{v}$ 还连续可微，则它是无旋场。

**证明** （1）⇒（2）：在闭曲线 $L$ 上任取两点 $A,B$，把 $L$ 分成从 $A$ 到 $B$ 的 $L_1$ 与从 $B$ 到 $A$ 的 $L_2$，则 $\oint_L=\int_{L_1}+\int_{L_2}=\int_{L_1}-\int_{L_2^-}=0$，因为 $L_1$、$L_2^-$ 都从 $A$ 到 $B$。（2）⇒（1）：若 $L_1,L_2$ 都从 $A$ 到 $B$，则 $L_1+L_2^-$ 是闭曲线，$\int_{L_1}-\int_{L_2}=\oint_{L_1+L_2^-}=0$。

（1）⇒（3）：取定 $A\in\Omega$，令 $f(P)=\int_A^P\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}$（与路径无关，所以有意义）。设 $P=(x,y,z)$，$\Omega$ 是开集，$|h|$ 很小时从 $P$ 到 $(x+h,y,z)$ 的线段在 $\Omega$ 内，沿此线段 $\mathrm{d}y=\mathrm{d}z=0$，于是

$$
\frac{f(x+h,y,z)-f(x,y,z)}{h}=\frac1h\int_x^{x+h}X(t,y,z)\,\mathrm{d}t=X(x+\theta h,y,z)\to X(x,y,z)\quad(h\to0),
$$
其中用了积分中值定理（$0<\theta<1$）与 $X$ 的连续性。同理 $f_y=Y$，$f_z=Z$。偏导数连续，所以 $f$ 可微，$\nabla f=\boldsymbol{v}$。

（3）⇒（1）：设 $L\colon\boldsymbol{r}(t)$，$t$ 从 $\alpha$ 到 $\beta$，由定理 13.3.1 与链式法则，

$$
\int_L\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\int_\alpha^\beta\nabla f(\boldsymbol{r}(t))\cdot\boldsymbol{r}'(t)\,\mathrm{d}t=\int_\alpha^\beta\frac{\mathrm{d}}{\mathrm{d}t}f(\boldsymbol{r}(t))\,\mathrm{d}t=f(B)-f(A)
$$
（逐段光滑时分段相加），与路径无关。最后，若 $\boldsymbol{v}=\nabla f$ 连续可微，则 $f$ 有连续的二阶偏导数，由定理 14.1.1，$\operatorname{rot}\boldsymbol{v}=\boldsymbol{0}$。$\square$

保守场的物理意义是能量守恒。设质量为 $m$ 的质点只在力 $\boldsymbol{F}=\nabla f$ 作用下运动，轨迹为 $\boldsymbol{r}(t)$，由 Newton 第二定律 $m\boldsymbol{r}''=\nabla f(\boldsymbol{r})$，

$$
\frac{\mathrm{d}}{\mathrm{d}t}\Big(\frac12m\|\boldsymbol{r}'\|^2-f(\boldsymbol{r})\Big)=m\boldsymbol{r}''\cdot\boldsymbol{r}'-\nabla f(\boldsymbol{r})\cdot\boldsymbol{r}'=0,
$$
即动能与势能 $-f$ 之和守恒。

定理 14.4.1 的条件（2）要对所有闭曲线验证，不便使用。对连续可微场，无旋是必要条件，但一般不充分：

**例 14.4.1** 平面场 $\boldsymbol{v}=\Big(\dfrac{-y}{x^2+y^2},\dfrac{x}{x^2+y^2}\Big)$ 在 $\mathbb{R}^2\setminus\{0\}$ 上无旋（例 13.4.6），但沿单位圆的环量为 $2\pi\ne0$，所以不是 $\mathbb{R}^2\setminus\{0\}$ 上的保守场。它在任何不含原点的单连通区域（如右半平面）上有势函数——极角 $\theta$，例如右半平面上 $\theta=\arctan\frac yx$；而极角不能在整个 $\mathbb{R}^2\setminus\{0\}$ 上连续地定义。空间场 $\Big(\dfrac{-y}{x^2+y^2},\dfrac{x}{x^2+y^2},z\Big)$ 在除去 $z$ 轴的空间上同样无旋而不保守。

问题出在区域有"洞"：绕洞一周的闭曲线不能在区域内收缩成一点，Green 公式或 Stokes 公式无法用在它所围的曲面上。为此需要空间区域的单连通概念。

**定义 14.4.4（曲面单连通区域）** 设 $\Omega\subset\mathbb{R}^3$ 是区域。若对 $\Omega$ 中任一逐段光滑的闭曲线 $L$，都存在 $\Omega$ 中以 $L$ 为边界的分片光滑曲面，则称 $\Omega$ 为**曲面单连通区域**。

球体、全空间、球壳 $a^2<x^2+y^2+z^2<b^2$ 都是曲面单连通的；圆环体（轮胎形）、除去一条直线的空间不是。曲面单连通即通常所说的（空间）**单连通区域**；平面区域按定义 13.4.1 单连通时，闭曲线所围的平面区域就是以它为边界的曲面。

**定理 14.4.2** 设 $\Omega$ 是平面单连通区域或空间曲面单连通区域，$\boldsymbol{v}$ 在 $\Omega$ 上连续可微，则 $\boldsymbol{v}$ 是保守场当且仅当 $\boldsymbol{v}$ 是无旋场。平面情形即：$X\,\mathrm{d}x+Y\,\mathrm{d}y$ 在单连通区域上是全微分式当且仅当 $\frac{\partial Y}{\partial x}=\frac{\partial X}{\partial y}$。

**证明** 必要性已在定理 14.4.1 中证明。充分性：设 $L$ 是 $\Omega$ 中的闭曲线，$S$ 是 $\Omega$ 中以 $L$ 为边界的曲面，由 Stokes 公式 $\oint_L\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\iint_S\operatorname{rot}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=0$；平面情形用 Green 公式。由定理 14.4.1 即得。（严格地说，自相交的闭曲线要先分解为若干简单闭曲线，或者只对简单闭曲线验证条件（2）后，再说明它足以推出与路径无关；这里不展开。）$\square$

### 14.4.3. 势函数的计算

**算法 14.4.1（判定保守场并求势函数）** 给定 $\Omega$ 上的连续可微场 $\boldsymbol{v}=(X,Y,Z)$：

1. 判定：检查 $\Omega$ 是否（曲面）单连通，计算 $\operatorname{rot}\boldsymbol{v}$。单连通且无旋则 $\boldsymbol{v}$ 是保守场；不是单连通时，还要检查绕每个"洞"的环量是否为零（如例 14.4.1）。
2. 曲线积分法：取定 $(x_0,y_0,z_0)\in\Omega$，沿平行于坐标轴的折线积分（折线须在 $\Omega$ 内），
   $$
   f(x,y,z)=\int_{x_0}^xX(t,y_0,z_0)\,\mathrm{d}t+\int_{y_0}^yY(x,t,z_0)\,\mathrm{d}t+\int_{z_0}^zZ(x,y,t)\,\mathrm{d}t.
   $$
3. 或不定积分法：由 $f_x=X$ 得 $f=\int X\,\mathrm{d}x+g(y,z)$；代入 $f_y=Y$ 定出 $g_y$，积分得 $g$ 到只差 $h(z)$；再由 $f_z=Z$ 定出 $h$。
4. 或凑微分：被积式能直接看成若干个全微分之和时（如 $y\,\mathrm{d}x+x\,\mathrm{d}y=\mathrm{d}(xy)$）最快。
5. 求积分：$\int_A^B\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=f(B)-f(A)$；也可以换一条简单的路径（折线）直接积分。

**例 14.4.2** $2xy^3\,\mathrm{d}x+3x^2y^2\,\mathrm{d}y$：$\frac{\partial}{\partial y}(2xy^3)=6xy^2=\frac{\partial}{\partial x}(3x^2y^2)$，$\mathbb{R}^2$ 单连通。沿 $(0,0)\to(x,0)\to(x,y)$ 积分：$f=\int_0^x0\,\mathrm{d}t+\int_0^y3x^2t^2\,\mathrm{d}t=x^2y^3$，原函数为 $x^2y^3+C$。

**例 14.4.3** 在 $\{x>0,y>0\}$ 上求 $\big(\frac yx+\frac{2x}y\big)\mathrm{d}x+\big(\ln x-\frac{x^2}{y^2}\big)\mathrm{d}y$ 的原函数。两个交叉偏导数都等于 $\frac1x-\frac{2x}{y^2}$，区域单连通。不定积分法：$f=\int\big(\frac yx+\frac{2x}y\big)\mathrm{d}x=y\ln x+\frac{x^2}y+g(y)$；$f_y=\ln x-\frac{x^2}{y^2}+g'(y)$，与 $Y$ 比较得 $g'=0$。所以原函数为 $y\ln x+\frac{x^2}y+C$。

**例 14.4.4** $(\mathrm{e}^x\sin y+y)\,\mathrm{d}x+(\mathrm{e}^x\cos y+x+2)\,\mathrm{d}y$：交叉偏导数都等于 $\mathrm{e}^x\cos y+1$。曲线积分法：$f=\int_0^x0\,\mathrm{d}t+\int_0^y(\mathrm{e}^x\cos t+x+2)\,\mathrm{d}t=\mathrm{e}^x\sin y+xy+2y$。凑微分也可直接看出：$\mathrm{d}(\mathrm{e}^x\sin y)+\mathrm{d}(xy)+\mathrm{d}(2y)$。

**例 14.4.5** 设 $f$ 有连续导数，$f(0)=0$，确定 $f$ 使 $(x\mathrm{e}^x+f(x))y\,\mathrm{d}x+f(x)\,\mathrm{d}y$ 为全微分式，并求原函数。条件 $\frac{\partial}{\partial y}[(x\mathrm{e}^x+f)y]=\frac{\partial}{\partial x}f$ 即 $f'(x)-f(x)=x\mathrm{e}^x$。两边乘以 $\mathrm{e}^{-x}$ 得 $(\mathrm{e}^{-x}f)'=x$，所以 $\mathrm{e}^{-x}f=\frac{x^2}2+C$，由 $f(0)=0$ 得 $f(x)=\frac{x^2\mathrm{e}^x}2$。原函数：$\frac{\partial}{\partial y}F=f(x)$ 给出 $F=\frac{x^2\mathrm{e}^x}2y+g(x)$，再由 $F_x=(x\mathrm{e}^x+\frac{x^2\mathrm{e}^x}2)y+g'(x)$ 得 $g'=0$，所以原函数为 $\frac12x^2\mathrm{e}^xy+C$。

**例 14.4.6** 设 $f(t)$ 在 $t\ne0$ 时有连续导数，$f(1)=0$。确定 $f$，使对任意与直线 $y=\pm x$ 不相交的闭曲线 $L$，$\oint_Ly\big(2-f(x^2-y^2)\big)\,\mathrm{d}x+xf(x^2-y^2)\,\mathrm{d}y=0$。直线 $y=\pm x$ 把平面分成四个角形区域，都是单连通的，且不含 $x^2-y^2=0$ 的点；与这两条直线不相交的闭曲线必落在其中一个区域内。由定理 14.4.2，条件等价于在这些区域上 $\frac{\partial}{\partial x}\big[xf(x^2-y^2)\big]=\frac{\partial}{\partial y}\big[y(2-f(x^2-y^2))\big]$，即

$$
f+2x^2f'=2-f+2y^2f',\qquad\text{即}\qquad tf'(t)+f(t)=1\quad(t=x^2-y^2).
$$
于是 $(tf(t))'=1$，$tf(t)=t+C$，由 $f(1)=0$ 得 $C=-1$，$f(t)=1-\frac1t$。

**例 14.4.7（1）**$\int_{(0,2)}^{(2,3)}x\,\mathrm{d}y+y\,\mathrm{d}x=xy\big|_{(0,2)}^{(2,3)}=6$。（2）$\int_{(0,0)}^{(a,b)}\mathrm{e}^x(\cos y\,\mathrm{d}x-\sin y\,\mathrm{d}y)=\mathrm{e}^x\cos y\big|_{(0,0)}^{(a,b)}=\mathrm{e}^a\cos b-1$。（3）在不含原点的路径上，$\int_{A}^{B}\dfrac{x\,\mathrm{d}x+y\,\mathrm{d}y+z\,\mathrm{d}z}{x^2+y^2+z^2}=\frac12\ln(x^2+y^2+z^2)\Big|_A^B=\ln\dfrac{\|B\|}{\|A\|}$，其中 $\|A\|$ 是点 $A$ 到原点的距离。

**例 14.4.8** $\boldsymbol{v}=(x+yz,\,y+zx,\,z+xy)$：$\operatorname{rot}\boldsymbol{v}=(x-x,\,y-y,\,z-z)=\boldsymbol{0}$，$\mathbb{R}^3$ 单连通，势函数为 $f=\frac12(x^2+y^2+z^2)+xyz$。所以沿任意从原点到 $(1,1,1)$ 的曲线，$\int\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=f(1,1,1)-f(0,0,0)=\frac52$。

**例 14.4.9** 判断 $z^2\,\mathrm{d}x+2yz\,\mathrm{d}y+(y^2+2xz+z^2)\,\mathrm{d}z$ 是否为全微分式。$\operatorname{rot}\boldsymbol{v}=(2y-2y,\,2z-2z,\,0)=\boldsymbol{0}$，是。沿 $(0,0,0)\to(x,0,0)\to(x,y,0)\to(x,y,z)$ 积分，前两段被积函数为零，

$$
f=\int_0^z(y^2+2xt+t^2)\,\mathrm{d}t=y^2z+xz^2+\frac{z^3}3.
$$

**例 14.4.10** 在 $A(1,0)$、$B(0,1)$ 处各有一个单位质点，另一单位质点从原点 $O$ 沿以 $A$ 为圆心、半径为 $1$ 的上半圆周移动到 $D(2,0)$，求引力做的功。引力场是保守场：单位质点 $Q$ 处的场 $\nabla\frac{G}{\|Q-P\|}$ 以 $\frac{G}{\|Q-P\|}$ 为势函数（$P$ 为施力质点），功只与起点、终点有关。$O$、$D$ 到 $A$ 的距离都是 $1$，所以 $A$ 的引力做功为零（事实上沿此圆周引力处处与位移垂直）；$B$ 的引力做功为 $G\big(\frac1{\|DB\|}-\frac1{\|OB\|}\big)=G\big(\frac1{\sqrt5}-1\big)$。总功为 $G\big(\frac1{\sqrt5}-1\big)$，为负值：质点在远离 $B$。

## 14.5. 无源场与调和场

### 14.5.1. 无源场

**定义 14.5.1（无源场）** 若连续可微向量场 $\boldsymbol{v}$ 在区域 $\Omega$ 上处处满足 $\operatorname{div}\boldsymbol{v}=0$，则称 $\boldsymbol{v}$ 为 $\Omega$ 上的**无源场**。

不可压缩流体的速度场、磁场都是无源场。由定理 14.1.1，连续可微场的旋度场 $\boldsymbol{v}=\nabla\times\boldsymbol{u}$ 必是无源场。

**例 14.5.1** 质量为 $m_i$ 的质点位于 $P_i$（$i=1,\dots,k$），它们对位于 $P=(x,y,z)$ 的单位质点的引力为

$$
\boldsymbol{F}=\sum_{i=1}^k\boldsymbol{F}_i=-G\sum_{i=1}^km_i\frac{\boldsymbol{r}_i}{\|\boldsymbol{r}_i\|^3},\qquad\boldsymbol{r}_i=P-P_i.
$$
由例 14.2.6 的计算，每一项在 $P_i$ 以外散度为零，所以 $\boldsymbol{F}$ 在除去各质点的区域上是无源场。但若闭曲面 $S$（外侧）包围了其中的 $m_{i_1},\dots,m_{i_s}$，挖去这些点周围的小球后用 Gauss 公式，得

$$
\oiint_S\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}=-4\pi G\,(m_{i_1}+\cdots+m_{i_s}),
$$
即引力场的 Gauss 定律：通量只取决于曲面包围的总质量。按定理 14.2.2 的观点，质点是引力场的"汇"，汇的强度与质量成正比。

无源场能否写成旋度场？与无旋场的情形类似，答案取决于区域有没有"空腔"。

**定义 14.5.2（空间单连通区域）** 设 $\Omega\subset\mathbb{R}^3$ 是区域。若 $\Omega$ 中任一分片光滑闭曲面所围的有界区域都含于 $\Omega$，则称 $\Omega$ 为空间单连通区域。

球体、全空间、圆环体是空间单连通的；球壳、除去一点的空间不是。空间单连通与曲面单连通是两个互不包含的条件：圆环体只满足前者，球壳只满足后者。

**定理 14.5.1** 设 $\Omega$ 是空间单连通区域，$\boldsymbol{v}$ 在 $\Omega$ 上连续可微。

1. $\boldsymbol{v}$ 是无源场，当且仅当对 $\Omega$ 中任意分片光滑闭曲面 $S$，$\oiint_S\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=0$。
2. 若 $\boldsymbol{v}$ 是无源场，则存在向量场 $\boldsymbol{u}$ 使 $\boldsymbol{v}=\nabla\times\boldsymbol{u}$（称 $\boldsymbol{u}$ 为向量势）。

**证明** （1）必要性：$S$ 所围的区域在 $\Omega$ 内，由 Gauss 公式通量为 $\iiint\operatorname{div}\boldsymbol{v}\,\mathrm{d}V=0$。充分性：若 $\operatorname{div}\boldsymbol{v}(M_0)\ne0$，由定理 14.2.2，以 $M_0$ 为中心的小球面上通量不为零，矛盾。（2）证明从略。$\square$

区域不是空间单连通时，结论（2）可能不成立：例 14.2.6 的场 $\frac{(x,y,z)}{\rho^3}$ 在 $\mathbb{R}^3\setminus\{0\}$ 上无源，但穿过单位球面的通量为 $4\pi$；而旋度场穿过闭曲面的通量总为零（定理 14.3.1 后的说明），所以它不是任何连续可微场的旋度。

### 14.5.2. 调和场与调和函数

**定义 14.5.3（调和场与调和函数）** 既有势又无源的向量场称为**调和场**。若 $\boldsymbol{v}=\nabla f$ 是调和场，则 $\Delta f=\nabla\cdot\nabla f=0$。在区域上有连续二阶偏导数且满足 Laplace 方程 $\Delta f=0$ 的函数称为**调和函数**。

例如 $\frac1{\sqrt{x^2+y^2+z^2}}$ 在 $\mathbb{R}^3\setminus\{0\}$ 上调和（它的梯度正是例 14.2.6 中的场乘以 $-1$）；平面上 $x^2-y^2$、$\mathrm{e}^x\sin y$、$\ln(x^2+y^2)$ 是调和函数。静电场中无电荷区域的电势、稳定温度场的温度都是调和函数。

**定理 14.5.2（Green 第一公式）** 设 $\Omega$ 是有界闭区域，边界 $\partial\Omega$ 分片光滑，$\boldsymbol{n}$ 是外法向量，$f,g$ 在 $\Omega$ 上有连续的二阶偏导数，则

$$
\oiint_{\partial\Omega}f\frac{\partial g}{\partial\boldsymbol{n}}\,\mathrm{d}S=\iiint_\Omega\big(f\Delta g+\nabla f\cdot\nabla g\big)\,\mathrm{d}V.
$$

**证明** **方向导数** $\frac{\partial g}{\partial\boldsymbol{n}}=\nabla g\cdot\boldsymbol{n}$，所以左端是 $f\nabla g$ 的通量。由 Gauss 公式与性质 14.1.1，它等于 $\iiint_\Omega\nabla\cdot(f\nabla g)\,\mathrm{d}V=\iiint_\Omega(f\Delta g+\nabla f\cdot\nabla g)\,\mathrm{d}V$。$\square$

**定理 14.5.3** 设 $\Omega$ 是有界区域，$f$ 在闭区域 $\bar\Omega$ 上有连续的二阶偏导数，在 $\Omega$ 内调和。若在边界上 $f=0$，则在 $\Omega$ 内 $f\equiv0$。

**证明** 在定理 14.5.2 中取 $g=f$：左端因 $f|_{\partial\Omega}=0$ 为零，右端 $\Delta f=0$，所以 $\iiint_\Omega\|\nabla f\|^2\,\mathrm{d}V=0$。被积函数连续非负，故 $\nabla f\equiv\boldsymbol{0}$，$f$ 在连通的 $\Omega$ 内为常数；再由连续性与边界值为零得 $f\equiv0$。$\square$

推论：若两个调和函数在边界上取相同的值，则它们相等（对差用定理 14.5.3）。也就是说，Laplace 方程的 Dirichlet 问题（给定边界值求调和函数）的解至多有一个——稳定温度分布由边界温度唯一确定。平面情形的 Green 第一公式由 Green 公式的通量形式同样得到（例 13.4.8 是 $f\equiv1$ 的情形）。

## 14.6. 正交曲线坐标中的场论算子

物理问题常有柱对称或球对称，在柱坐标、球坐标下写梯度、散度、旋度更方便。设点的位置由 $(q_1,q_2,q_3)$ 确定，$\boldsymbol{r}=\boldsymbol{r}(q_1,q_2,q_3)$。若三族坐标曲线（只让一个 $q_i$ 变化得到的曲线）在每点两两正交，就称 $(q_1,q_2,q_3)$ 为正交曲线坐标。记沿 $q_i$ 增大方向的单位切向量为 $\boldsymbol{e}_i$，设 $\boldsymbol{e}_1,\boldsymbol{e}_2,\boldsymbol{e}_3$ 构成右手系。

**定义 14.6.1（Lamé 系数）** 称 $H_i=\Big\|\dfrac{\partial\boldsymbol{r}}{\partial q_i}\Big\|=\sqrt{\Big(\dfrac{\partial x}{\partial q_i}\Big)^2+\Big(\dfrac{\partial y}{\partial q_i}\Big)^2+\Big(\dfrac{\partial z}{\partial q_i}\Big)^2}$（$i=1,2,3$）为正交曲线坐标的 **Lamé 系数**。

沿 $q_i$ 坐标曲线的弧长元为 $\mathrm{d}l_i=H_i\,\mathrm{d}q_i$，坐标面上的面积元为 $\mathrm{d}S_1=H_2H_3\,\mathrm{d}q_2\,\mathrm{d}q_3$ 等，体积元为 $\mathrm{d}V=H_1H_2H_3\,\mathrm{d}q_1\,\mathrm{d}q_2\,\mathrm{d}q_3$（$H_1H_2H_3$ 正是坐标变换的 **Jacobi 行列式**）。柱坐标 $(r,\theta,z)$ 的 Lamé 系数为 $1,r,1$；球坐标 $(\rho,\varphi,\theta)$（$x=\rho\sin\varphi\cos\theta$，$y=\rho\sin\varphi\sin\theta$，$z=\rho\cos\varphi$，与 [2.2.12](/2.2.12) 相同）的 Lamé 系数为 $1,\rho,\rho\sin\varphi$。

设 $\boldsymbol{v}=v_1\boldsymbol{e}_1+v_2\boldsymbol{e}_2+v_3\boldsymbol{e}_3$。梯度的分量是沿 $\boldsymbol{e}_i$ 的方向导数 $\frac1{H_i}\frac{\partial f}{\partial q_i}$；散度按定理 14.2.2 计算以 $\mathrm{d}l_1,\mathrm{d}l_2,\mathrm{d}l_3$ 为边的小曲边长方体的通量除以体积（例如两个 $q_3$ 坐标面上的通量之差约为 $\frac{\partial(v_3H_1H_2)}{\partial q_3}\Delta q_1\Delta q_2\Delta q_3$）；旋度按定理 14.3.2 计算坐标面上小曲边矩形的环量。结果为

$$
\begin{aligned}
\nabla f&=\sum_{i=1}^3\frac1{H_i}\frac{\partial f}{\partial q_i}\boldsymbol{e}_i,\qquad
\nabla\cdot\boldsymbol{v}=\frac1{H_1H_2H_3}\Big[\frac{\partial(v_1H_2H_3)}{\partial q_1}+\frac{\partial(v_2H_3H_1)}{\partial q_2}+\frac{\partial(v_3H_1H_2)}{\partial q_3}\Big],\\
\nabla\times\boldsymbol{v}&=\frac1{H_1H_2H_3}\begin{vmatrix}H_1\boldsymbol{e}_1&H_2\boldsymbol{e}_2&H_3\boldsymbol{e}_3\\ \dfrac{\partial}{\partial q_1}&\dfrac{\partial}{\partial q_2}&\dfrac{\partial}{\partial q_3}\\ H_1v_1&H_2v_2&H_3v_3\end{vmatrix},\qquad
\Delta f=\frac1{H_1H_2H_3}\sum_{i=1}^3\frac{\partial}{\partial q_i}\Big(\frac{H_1H_2H_3}{H_i^2}\frac{\partial f}{\partial q_i}\Big).
\end{aligned}
$$

**柱坐标** $(r,\theta,z)$，$\boldsymbol{v}=v_r\boldsymbol{e}_r+v_\theta\boldsymbol{e}_\theta+v_z\boldsymbol{e}_z$：

$$
\begin{aligned}
\nabla f&=\frac{\partial f}{\partial r}\boldsymbol{e}_r+\frac1r\frac{\partial f}{\partial\theta}\boldsymbol{e}_\theta+\frac{\partial f}{\partial z}\boldsymbol{e}_z,\qquad
\nabla\cdot\boldsymbol{v}=\frac1r\frac{\partial(rv_r)}{\partial r}+\frac1r\frac{\partial v_\theta}{\partial\theta}+\frac{\partial v_z}{\partial z},\\
\nabla\times\boldsymbol{v}&=\Big(\frac1r\frac{\partial v_z}{\partial\theta}-\frac{\partial v_\theta}{\partial z}\Big)\boldsymbol{e}_r+\Big(\frac{\partial v_r}{\partial z}-\frac{\partial v_z}{\partial r}\Big)\boldsymbol{e}_\theta+\frac1r\Big(\frac{\partial(rv_\theta)}{\partial r}-\frac{\partial v_r}{\partial\theta}\Big)\boldsymbol{e}_z,\\
\Delta f&=\frac1r\frac{\partial}{\partial r}\Big(r\frac{\partial f}{\partial r}\Big)+\frac1{r^2}\frac{\partial^2f}{\partial\theta^2}+\frac{\partial^2f}{\partial z^2}.
\end{aligned}
$$

**球坐标** $(\rho,\varphi,\theta)$，$\boldsymbol{v}=v_\rho\boldsymbol{e}_\rho+v_\varphi\boldsymbol{e}_\varphi+v_\theta\boldsymbol{e}_\theta$：

$$
\begin{aligned}
\nabla f&=\frac{\partial f}{\partial\rho}\boldsymbol{e}_\rho+\frac1\rho\frac{\partial f}{\partial\varphi}\boldsymbol{e}_\varphi+\frac1{\rho\sin\varphi}\frac{\partial f}{\partial\theta}\boldsymbol{e}_\theta,\qquad
\nabla\cdot\boldsymbol{v}=\frac1{\rho^2}\frac{\partial(\rho^2v_\rho)}{\partial\rho}+\frac1{\rho\sin\varphi}\frac{\partial(\sin\varphi\,v_\varphi)}{\partial\varphi}+\frac1{\rho\sin\varphi}\frac{\partial v_\theta}{\partial\theta},\\
\nabla\times\boldsymbol{v}&=\frac1{\rho\sin\varphi}\Big(\frac{\partial(\sin\varphi\,v_\theta)}{\partial\varphi}-\frac{\partial v_\varphi}{\partial\theta}\Big)\boldsymbol{e}_\rho+\frac1\rho\Big(\frac1{\sin\varphi}\frac{\partial v_\rho}{\partial\theta}-\frac{\partial(\rho v_\theta)}{\partial\rho}\Big)\boldsymbol{e}_\varphi+\frac1\rho\Big(\frac{\partial(\rho v_\varphi)}{\partial\rho}-\frac{\partial v_\rho}{\partial\varphi}\Big)\boldsymbol{e}_\theta,\\
\Delta f&=\frac1{\rho^2}\frac{\partial}{\partial\rho}\Big(\rho^2\frac{\partial f}{\partial\rho}\Big)+\frac1{\rho^2\sin\varphi}\frac{\partial}{\partial\varphi}\Big(\sin\varphi\frac{\partial f}{\partial\varphi}\Big)+\frac1{\rho^2\sin^2\varphi}\frac{\partial^2f}{\partial\theta^2}.
\end{aligned}
$$

例如径向场 $\boldsymbol{v}=\frac1{\rho^2}\boldsymbol{e}_\rho$（即例 14.2.6 的场）的散度为 $\frac1{\rho^2}\frac{\partial}{\partial\rho}(1)=0$；只依赖 $\rho$ 的调和函数满足 $(\rho^2f')'=0$，故 $f=\frac{C_1}\rho+C_2$。平面上只依赖 $r$ 的调和函数满足 $(rf')'=0$，故 $f=C_1\ln r+C_2$。在直角坐标下验证这些结论要繁得多。

## 小结

三大公式（$\boldsymbol{v}=(X,Y,Z)$ 连续可微，边界取诱导的正向）：

| 公式 | 形式 | 联系的积分 | 区域上的"导数" |
|---|---|---|---|
| Newton–Leibniz | $\int_a^bf'(x)\,\mathrm{d}x=f(b)-f(a)$ | 区间 ↔ 端点 | $f'$ |
| Green | $\oint_{\partial D}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\iint_D(Y_x-X_y)\,\mathrm{d}\sigma$ | 平面区域 ↔ 边界曲线 | 平面旋度 |
| Gauss | $\oiint_{\partial\Omega}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=\iiint_\Omega\operatorname{div}\boldsymbol{v}\,\mathrm{d}V$ | 空间区域 ↔ 边界曲面 | 散度 |
| Stokes | $\oint_{\partial S}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\iint_S\operatorname{rot}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}$ | 曲面 ↔ 边界曲线 | 旋度 |
| 曲线积分的 N–L 公式 | $\int_A^B\nabla f\cdot\mathrm{d}\boldsymbol{l}=f(B)-f(A)$ | 曲线 ↔ 端点 | 梯度 |

场论的基本运算：

| 运算 | 定义 | 物理意义 | 恒等式 |
|---|---|---|---|
| 梯度 $\nabla f$ | $(f_x,f_y,f_z)$ | 增长最快的方向与速率 | $\nabla\times\nabla f=\boldsymbol{0}$ |
| 散度 $\nabla\cdot\boldsymbol{v}$ | $X_x+Y_y+Z_z$ | 通量的体密度（源的强度） | $\nabla\cdot(\nabla\times\boldsymbol{v})=0$ |
| 旋度 $\nabla\times\boldsymbol{v}$ | $(Z_y-Y_z,\,X_z-Z_x,\,Y_x-X_y)$ | 最大环量面密度及其转轴 | |
| Laplace $\Delta f$ | $f_{xx}+f_{yy}+f_{zz}$ | $\nabla\cdot\nabla f$ | |

几类特殊的场：

| 场 | 定义 | 等价条件或性质 |
|---|---|---|
| 保守场 | 积分与路径无关 | ⇔ 闭曲线上积分为零 ⇔ 有势；单连通（曲面单连通）区域上 ⇔ 无旋 |
| 无源场 | $\operatorname{div}\boldsymbol{v}=0$ | 空间单连通区域上 ⇔ 闭曲面上通量为零，且是旋度场 |
| 调和场 | 有势且无源 | 势函数满足 $\Delta f=0$；边界值决定调和函数 |

计算第二型积分时，先看能否用三大公式或路径无关性化简：闭曲面用 Gauss 公式（不封闭时补面，有奇点时挖去小球）；空间闭曲线用 Stokes 公式（选最简单的曲面）；无旋场换路径或用势函数。
