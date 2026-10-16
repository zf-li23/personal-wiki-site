---
title: 首次积分与 Pfaff 方程
---

一阶方程 $M\,\mathrm{d}x+N\,\mathrm{d}y=0$ 的通解 $u(x,y)=C$ 是一个沿着每条积分曲线保持不变的函数（[2.4.2](/2.4.2)）。本章把这一观点推广到高维，沿两个方向展开。

第一个方向是方程组。对 $n$ 维自治方程组，沿解保持不变的函数称为首次积分，物理中的能量、动量、角动量都是首次积分。知道了足够多的首次积分，轨线就是它们等值面的交线，方程组可以化为求积。首次积分恰好是一阶线性偏微分方程的解，这给出了偏微分方程（[2.5](/2.5)）中特征线方法的出发点。

第二个方向是"全微分方程"的高维形式：Pfaff 方程 $P\,\mathrm{d}x+Q\,\mathrm{d}y+R\,\mathrm{d}z=0$。二元时任何这样的方程（局部）都有积分因子；三元以上就不再如此：只有满足可积条件的方程才有积分曲面族。这里要区分两个概念：恰当（左边是某个函数的**全微分**，即向量场是**保守场**，[2.2.14](/2.2.14#sec-14.4)）与完全可积（乘以积分因子后恰当）。最后讨论多元 Clairaut 方程，它是一阶非线性偏微分方程的一个可以完全解出的例子，奇解的几何意义与一元情形（[2.4.6](/2.4.6)）相同。

## 14.1. 首次积分

### 14.1.1. 定义与判别

考虑 $n$ 维自治方程组

$$
\boldsymbol{x}'=\boldsymbol{f}(\boldsymbol{x}),\qquad\boldsymbol{x}\in D\subset\mathbb{R}^n,\tag{14.1}
$$
其中 $\boldsymbol{f}=(f_1,\dots,f_n)$ 在区域 $D$ 上连续可微。分量形式为 $x_i'=f_i(x_1,\dots,x_n)$，$i=1,\dots,n$。

**定义 14.1.1（首次积分）** 设 $\Phi\in C^1(D)$ 在 $D$ 的任何开子集上都不是常数。若对 (14.1) 在 $D$ 中的每个解 $\boldsymbol{x}(t)$，$\Phi(\boldsymbol{x}(t))$ 都是常数（与 $t$ 无关），则称 $\Phi$ 为方程组 (14.1) 在 $D$ 上的一个**首次积分**，$\Phi(\boldsymbol{x})=C$ 也称为首次积分。

"首次"的说法来自力学：二阶运动方程积分一次得到的守恒关系（如能量积分）只含速度而不含加速度，是对方程的"第一次积分"。

**定理 14.1.1** $\Phi\in C^1(D)$（不是局部常数）是 (14.1) 的首次积分，当且仅当在 $D$ 上恒有

$$
\sum_{i=1}^nf_i(\boldsymbol{x})\frac{\partial\Phi}{\partial x_i}(\boldsymbol{x})=\nabla\Phi\cdot\boldsymbol{f}=0.\tag{14.2}
$$

**证明** 沿解 $\boldsymbol{x}(t)$，由链式法则 $\frac{\mathrm{d}}{\mathrm{d}t}\Phi(\boldsymbol{x}(t))=\nabla\Phi(\boldsymbol{x}(t))\cdot\boldsymbol{f}(\boldsymbol{x}(t))$。若 (14.2) 成立，导数为零，$\Phi$ 沿解不变。反之，对任意 $\boldsymbol{x}_0\in D$，由**存在唯一性定理**有过 $\boldsymbol{x}_0$ 的解，$\Phi$ 沿它为常数，在 $t=0$ 处求导即得 (14.2) 在 $\boldsymbol{x}_0$ 处成立。$\square$

几何上，(14.2) 说的是向量场 $\boldsymbol{f}$ 处处与 $\Phi$ 的等值面相切（与**梯度** $\nabla\Phi$ 正交），所以每条轨线都落在某个等值面 $\Phi=C$ 上。

**例 14.1.1** 单摆方程 $\theta''+\sin\theta=0$ 化为方程组 $x'=y$，$y'=-\sin x$（$x=\theta$，$y=\theta'$）。$\Phi(x,y)=\frac12y^2-\cos x$ 满足 $y\Phi_x-\sin x\,\Phi_y=y\sin x-y\sin x=0$，是首次积分，即机械能守恒。轨线是能量的等值线：$\Phi<1$ 时是围绕平衡点的闭曲线（摆动），$\Phi>1$ 时是上下两条波浪线（旋转），$\Phi=1$ 时是连接鞍点 $(\pm\pi,0)$ 的分界线。

![单摆 x' = y, y' = -sin x 的轨线就是首次积分 y²/2 - cos x 的等值线](./plots/pendulum-first-integral.py)

**例 14.1.2** Lotka–Volterra 捕食模型 $x'=x(\alpha-\beta y)$，$y'=y(-\gamma+\delta x)$（$x,y>0$，参数为正）。用 $\frac{\mathrm{d}y}{\mathrm{d}x}=\frac{y(-\gamma+\delta x)}{x(\alpha-\beta y)}$ 分离变量，得首次积分

$$
\Phi(x,y)=\delta x-\gamma\ln x+\beta y-\alpha\ln y,
$$
可以直接用 (14.2) 验证。$\Phi$ 在平衡点 $(\gamma/\delta,\alpha/\beta)$ 处取严格最小值，等值线是围绕它的闭曲线，所以所有正解都是周期的（参见 [7.4.4](/7.4.4)）。

非自治方程组 $\boldsymbol{x}'=\boldsymbol{f}(t,\boldsymbol{x})$ 可以把 $t$ 当作第 $n+1$ 个未知函数（$t'=1$）化为自治方程组，首次积分相应地是 $\Phi(t,\boldsymbol{x})$，判别条件为 $\frac{\partial\Phi}{\partial t}+\sum_if_i\frac{\partial\Phi}{\partial x_i}=0$。

### 14.1.2. 独立的首次积分与求解

**定义 14.1.2** 设 $\Phi_1,\dots,\Phi_k$ 是 (14.1) 的首次积分。若在点 $\boldsymbol{x}_0$ 处 Jacobi 矩阵 $\frac{\partial(\Phi_1,\dots,\Phi_k)}{\partial(x_1,\dots,x_n)}$ 的秩为 $k$，则称它们在 $\boldsymbol{x}_0$ 附近**相互独立**。

由于首次积分的梯度都与 $\boldsymbol{f}$ 正交，在 $\boldsymbol{f}(\boldsymbol{x}_0)\ne\boldsymbol{0}$ 的点附近，独立首次积分最多有 $n-1$ 个。事实上恰好有这么多：

**定理 14.1.2** 设 $\boldsymbol{f}(\boldsymbol{x}_0)\ne\boldsymbol{0}$，则在 $\boldsymbol{x}_0$ 的某个邻域内，(14.1) 有 $n-1$ 个相互独立的首次积分 $\Phi_1,\dots,\Phi_{n-1}$；并且该邻域内的任何首次积分都可以表示为 $\Phi=G(\Phi_1,\dots,\Phi_{n-1})$，$G$ 是某个 $C^1$ 函数。

证明的思路是"拉直"：在 $\boldsymbol{x}_0$ 附近取一个与 $\boldsymbol{f}(\boldsymbol{x}_0)$ 横截的 $n-1$ 维超平面，每条轨线与它恰交于一点，交点的 $n-1$ 个坐标就是沿轨线不变的量；由解对初值的可微性（[2.4.7](/2.4.7)）和**隐函数定理**，它们是 $\boldsymbol{x}$ 的光滑函数且相互独立。在平衡点（$\boldsymbol{f}(\boldsymbol{x}_0)=\boldsymbol{0}$）附近一般不存在这样的首次积分，例如结点附近所有轨线都趋于同一点，连续的首次积分只能是常数。

已知 $n-1$ 个独立首次积分时，方程组的轨线就是交线 $\Phi_1=C_1,\dots,\Phi_{n-1}=C_{n-1}$；从中解出 $n-1$ 个变量（隐函数定理），代入剩下的一个方程 $x_n'=f_n$，求一次积分即得 $t$ 与 $x_n$ 的关系。所以首次积分的个数决定了方程组可以"降"多少维；每知道一个首次积分，方程组就降一维。对非自治方程组 $\boldsymbol{x}'=\boldsymbol{f}(t,\boldsymbol{x})$，$n$ 个独立首次积分 $\Phi_i(t,\boldsymbol{x})=C_i$ 就隐式地给出了**通解**。

### 14.1.3. 对称形式与可积组合

消去 $t$，方程组 (14.1) 写成对称形式

$$
\frac{\mathrm{d}x_1}{f_1}=\frac{\mathrm{d}x_2}{f_2}=\cdots=\frac{\mathrm{d}x_n}{f_n}.\tag{14.3}
$$
它描述的是方向场 $\boldsymbol{f}$ 的积分曲线（不关心参数），所有变量地位平等。求首次积分的常用技巧是可积组合（integrable combination）：利用等比性质，对任意函数 $\lambda_1,\dots,\lambda_n$，

$$
\frac{\mathrm{d}x_1}{f_1}=\cdots=\frac{\mathrm{d}x_n}{f_n}=\frac{\lambda_1\,\mathrm{d}x_1+\cdots+\lambda_n\,\mathrm{d}x_n}{\lambda_1f_1+\cdots+\lambda_nf_n}.
$$
若能选取 $\lambda_i$ 使分母 $\sum\lambda_if_i=0$，而分子 $\sum\lambda_i\,\mathrm{d}x_i$ 是某个函数的全微分 $\mathrm{d}\Phi$，则 $\mathrm{d}\Phi=0$，$\Phi=C$ 就是一个首次积分。

**例 14.1.3** 求 $\dfrac{\mathrm{d}x}{y-z}=\dfrac{\mathrm{d}y}{z-x}=\dfrac{\mathrm{d}z}{x-y}$ 的积分曲线。

**解** 取 $\lambda=(1,1,1)$：分母 $(y-z)+(z-x)+(x-y)=0$，得 $\mathrm{d}x+\mathrm{d}y+\mathrm{d}z=0$，$\Phi_1=x+y+z$。取 $\lambda=(x,y,z)$：分母 $x(y-z)+y(z-x)+z(x-y)=0$，得 $x\,\mathrm{d}x+y\,\mathrm{d}y+z\,\mathrm{d}z=0$，$\Phi_2=x^2+y^2+z^2$。两者在 $\boldsymbol{f}\ne\boldsymbol{0}$ 处独立，积分曲线为

$$
x+y+z=C_1,\qquad x^2+y^2+z^2=C_2,
$$
即垂直于直线 $x=y=z$ 的平面与以原点为心的球面的交线：以 $x=y=z$ 为轴的圆。这个方程组描述的正是绕轴 $(1,1,1)$ 的刚体旋转，$\boldsymbol{f}=(1,1,1)\times(x,y,z)$。

![dx/(y - z) = dy/(z - x) = dz/(x - y) 的积分曲线：平面 x + y + z = C₁ 与球面 x² + y² + z² = C₂ 的交线，都是以 x = y = z 为轴的圆](./plots/symmetric-form-circles.py)

**例 14.1.4** 求 $\dfrac{\mathrm{d}x}{xz}=\dfrac{\mathrm{d}y}{yz}=\dfrac{\mathrm{d}z}{-(x^2+y^2)}$ 的首次积分。

**解** 由前两项，$\frac{\mathrm{d}x}{x}=\frac{\mathrm{d}y}{y}$，得 $\Phi_1=\frac yx$。取 $\lambda=(x,y,z)$，分母 $x^2z+y^2z-z(x^2+y^2)=0$，得 $\Phi_2=x^2+y^2+z^2$。积分曲线是过 $z$ 轴的平面 $y=C_1x$ 与球面 $x^2+y^2+z^2=C_2$ 的交线（大圆的一部分）。

## 14.2. 首次积分与一阶线性偏微分方程

条件 (14.2) 本身是关于未知函数 $\Phi$ 的一个方程。反过来读，它是一个一阶线性齐次**偏微分方程**

$$
\sum_{i=1}^nf_i(\boldsymbol{x})\frac{\partial u}{\partial x_i}=0,\tag{14.4}
$$
而定理 14.1.1 与 14.1.2 合起来就给出了它的解法：

**定理 14.2.1** 设 $\boldsymbol{f}\in C^1(D)$，$\boldsymbol{f}(\boldsymbol{x}_0)\ne\boldsymbol{0}$，$\Phi_1,\dots,\Phi_{n-1}$ 是常微分方程组 (14.3) 在 $\boldsymbol{x}_0$ 附近的独立首次积分。则在 $\boldsymbol{x}_0$ 附近，$u\in C^1$ 是 (14.4) 的解当且仅当

$$
u=G\big(\Phi_1(\boldsymbol{x}),\dots,\Phi_{n-1}(\boldsymbol{x})\big),
$$
其中 $G$ 是任意 $C^1$ 函数。

**定义 14.2.1（特征线）** 常微分方程组 (14.3) 称为偏微分方程 (14.4) 的特征方程组，它的积分曲线称为 (14.4) 的**特征线**。

定理 14.2.1 的几何意义是：(14.4) 的解沿每条特征线为常数。于是解一个偏微分方程归结为解一个常微分方程组，再把"沿特征线的常数"任意地指定；初值或边界条件通过 $G$ 来满足。偏微分方程的通解含一个任意函数，而不是任意常数。

**例 14.2.1** 解 $x\dfrac{\partial u}{\partial x}+y\dfrac{\partial u}{\partial y}=0$（$x\ne0$）。

**解** 特征方程组 $\frac{\mathrm{d}x}{x}=\frac{\mathrm{d}y}{y}$，首次积分 $y/x$，通解 $u=G(y/x)$：零次**齐次函数**。特征线是过原点的射线，解沿射线不变。

对拟线性方程 $\sum_if_i(\boldsymbol{x},u)\frac{\partial u}{\partial x_i}=g(\boldsymbol{x},u)$，可以把 $u$ 也当作变量：若 $V(\boldsymbol{x},u)=0$ 隐式地给出解 $u$，则 $V$ 满足 $n+1$ 元齐次方程 $\sum_if_i\frac{\partial V}{\partial x_i}+g\frac{\partial V}{\partial u}=0$，相应的特征方程组为

$$
\frac{\mathrm{d}x_1}{f_1}=\cdots=\frac{\mathrm{d}x_n}{f_n}=\frac{\mathrm{d}u}{g}.
$$
求出 $n$ 个独立首次积分 $\Psi_1,\dots,\Psi_n$ 后，通解为 $G(\Psi_1,\dots,\Psi_n)=0$。

**例 14.2.2** 解 $x\dfrac{\partial u}{\partial x}+y\dfrac{\partial u}{\partial y}=u$（$x\ne0$）。

**解** $\frac{\mathrm{d}x}{x}=\frac{\mathrm{d}y}{y}=\frac{\mathrm{d}u}{u}$ 有首次积分 $\frac yx$、$\frac ux$，通解 $G\big(\frac yx,\frac ux\big)=0$，即 $u=x\,H\big(\frac yx\big)$，$H$ 任意：一次齐次函数。这正是齐次函数的 Euler 定理的逆。

## 14.3. 三元 Pfaff 方程

### 14.3.1. 基本概念

**定义 14.3.1（Pfaff 方程）** 设 $P,Q,R$ 在区域 $D\subset\mathbb{R}^3$ 上连续可微，且不同时为零。方程

$$
P(x,y,z)\,\mathrm{d}x+Q(x,y,z)\,\mathrm{d}y+R(x,y,z)\,\mathrm{d}z=0\tag{14.5}
$$
称为三元 **Pfaff 方程**（三元全微分方程）。若曲面 $S\subset D$ 上任一点处的任意切向量 $(\mathrm{d}x,\mathrm{d}y,\mathrm{d}z)$ 都满足 (14.5)，则称 $S$ 为 (14.5) 的**积分曲面**。

记 $\boldsymbol{F}=(P,Q,R)$，(14.5) 即 $\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{r}=0$：积分曲面就是处处与向量场 $\boldsymbol{F}$ 正交的曲面，$\boldsymbol{F}$ 是它的法向量。每一点处 (14.5) 规定了一个平面（与 $\boldsymbol{F}$ 垂直），问题是能否把这些小平面"拼"成曲面。

**定义 14.3.2（恰当与完全可积）** 对 Pfaff 方程 (14.5)：

1. 若存在函数 $U$ 使 $\mathrm{d}U=P\,\mathrm{d}x+Q\,\mathrm{d}y+R\,\mathrm{d}z$，则称 (14.5) 是**恰当的**；
2. 若过 $D$ 中每一点都（局部地）有一个积分曲面，并且这些积分曲面可以写成一族 $U(x,y,z)=C$，则称 (14.5) 是**完全可积的**。

恰当时 $U=C$ 就是积分曲面族，所以恰当一定完全可积。由保守场的判定定理（[2.2.14](/2.2.14#thm-14.4.2)），在曲面单连通区域上，(14.5) 恰当当且仅当 $\boldsymbol{F}$ 是无旋场：

$$
\operatorname{rot}\boldsymbol{F}=\Big(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z},\ \frac{\partial P}{\partial z}-\frac{\partial R}{\partial x},\ \frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Big)=\boldsymbol{0},
$$
此时 $U$ 就是 $\boldsymbol{F}$ 的**势函数**。完全可积则弱得多：若 $\mu\ne0$ 使 $\mu(P\,\mathrm{d}x+Q\,\mathrm{d}y+R\,\mathrm{d}z)=\mathrm{d}U$ 恰当，$\mu$ 称为 (14.5) 的**积分因子**，此时 $U=C$ 是积分曲面族；反之，若积分曲面族 $U=C$（$\nabla U\ne\boldsymbol{0}$）存在，则 $\nabla U$ 与 $\boldsymbol{F}$ 都是积分曲面的法向量，$\nabla U=\mu\boldsymbol{F}$，$\mu$ 就是积分因子。所以

$$
\text{完全可积}\iff\text{(局部地)存在积分因子}.
$$

二元方程 $P\,\mathrm{d}x+Q\,\mathrm{d}y=0$ 总是（局部）完全可积的：它等价于一阶方程 $\frac{\mathrm{d}y}{\mathrm{d}x}=-\frac PQ$，其通解 $U(x,y)=C$ 就是积分曲线族，积分因子总存在（[2.4.2](/2.4.2)）。三元情形则不然。

### 14.3.2. 可积条件

**定理 14.3.1** Pfaff 方程 (14.5) 完全可积（$P,Q,R\in C^1$）的充分必要条件是在 $D$ 上恒有

$$
\boldsymbol{F}\cdot\operatorname{rot}\boldsymbol{F}=P\Big(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z}\Big)+Q\Big(\frac{\partial P}{\partial z}-\frac{\partial R}{\partial x}\Big)+R\Big(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Big)=0.\tag{14.6}
$$

**证明**（必要性，方法一）设 $\mu\boldsymbol{F}=\nabla U$。由 $\operatorname{rot}\nabla U=\boldsymbol{0}$ 与公式 $\operatorname{rot}(\mu\boldsymbol{F})=\nabla\mu\times\boldsymbol{F}+\mu\operatorname{rot}\boldsymbol{F}$，

$$
\boldsymbol{0}=\nabla\mu\times\boldsymbol{F}+\mu\operatorname{rot}\boldsymbol{F}.
$$
两边与 $\boldsymbol{F}$ 作数量积，$(\nabla\mu\times\boldsymbol{F})\cdot\boldsymbol{F}=0$，得 $\mu\,\boldsymbol{F}\cdot\operatorname{rot}\boldsymbol{F}=0$，而 $\mu\ne0$。$\square$

**证明**（必要性，方法二）设在某点 $R\ne0$，则在其附近 (14.5) 可以写成 $\mathrm{d}z=-\frac PR\,\mathrm{d}x-\frac QR\,\mathrm{d}y$，积分曲面 $z=z(x,y)$ 满足一阶偏微分方程组

$$
\frac{\partial z}{\partial x}=-\frac PR=:M_1(x,y,z),\qquad\frac{\partial z}{\partial y}=-\frac QR=:M_2(x,y,z).\tag{14.7}
$$
过每一点有积分曲面，则在每一点都有 $\frac{\partial^2z}{\partial x\partial y}=\frac{\partial^2z}{\partial y\partial x}$。用链式法则展开并代入 (14.7)：

$$
\frac{\partial M_2}{\partial x}+\frac{\partial M_2}{\partial z}M_1=\frac{\partial M_1}{\partial y}+\frac{\partial M_1}{\partial z}M_2.\tag{14.8}
$$
把 $M_1=-P/R$，$M_2=-Q/R$ 代入，两边乘以 $R^3$ 并化简，正好得到 (14.6)。由于过每一点都有积分曲面，(14.8) 在 $D$ 中每一点都成立。$\square$

充分性是 Frobenius 定理（定理 14.4.1）的特例，其证明给出了下面的构造方法。

求积分曲面的方法如下。设 (14.6) 成立且 $R\ne0$。先把 $y$ 当作常数（$\mathrm{d}y=0$），解二元方程 $P\,\mathrm{d}x+R\,\mathrm{d}z=0$，得到通积分 $V(x,y,z)=\varphi(y)$，其中"任意常数" $\varphi(y)$ 可以依赖于 $y$。再要求 $V(x,y,z)=\varphi(y)$ 满足原方程，得到关于 $\varphi$ 的一个方程。可积条件 (14.6) 保证这个方程中 $x,z$ 能通过 $V$ 消去，只剩下 $V$ 与 $y$ 的一个一阶常微分方程，解出即得积分曲面族。

### 14.3.3. 例题

**例 14.3.1** 求 $yz\,\mathrm{d}x+2xz\,\mathrm{d}y+xy\,\mathrm{d}z=0$ 的积分曲面族。

**解** $\boldsymbol{F}=(yz,2xz,xy)$，$\operatorname{rot}\boldsymbol{F}=(x-2x,\,y-y,\,2z-z)=(-x,0,z)$，$\boldsymbol{F}\cdot\operatorname{rot}\boldsymbol{F}=-xyz+xyz=0$，方程完全可积（但 $\operatorname{rot}\boldsymbol{F}\ne\boldsymbol{0}$，不恰当）。乘以积分因子 $\mu=\frac{1}{xyz}$：

$$
\frac{\mathrm{d}x}{x}+\frac{2\,\mathrm{d}y}{y}+\frac{\mathrm{d}z}{z}=0,
$$
积分得 $xy^2z=C$。

**例 14.3.2** 求 $(y^2+yz)\,\mathrm{d}x+(xz+z^2)\,\mathrm{d}y+(y^2-xy)\,\mathrm{d}z=0$ 的积分曲面族。

**解** 直接计算可验证 (14.6) 成立。令 $\mathrm{d}y=0$：$y(y+z)\,\mathrm{d}x+y(y-x)\,\mathrm{d}z=0$，即 $(y+z)\,\mathrm{d}x-(x-y)\,\mathrm{d}z=0$。以 $(y+z)^2$ 除之，左边是 $\mathrm{d}\Big(\dfrac{x-y}{y+z}\Big)$（$y$ 看作常数），故 $V=\dfrac{x-y}{y+z}=\varphi(y)$。

现在把 $y$ 也看作变量。计算可得

$$
(y^2+yz)\,\mathrm{d}x+(xz+z^2)\,\mathrm{d}y+(y^2-xy)\,\mathrm{d}z=y(y+z)^2\,\mathrm{d}V+(x+z)(y+z)\,\mathrm{d}y.
$$
由 $x=y+V(y+z)$ 得 $x+z=(1+V)(y+z)$，所以原方程化为 $(y+z)^2\big[y\,\mathrm{d}V+(1+V)\,\mathrm{d}y\big]=0$，即

$$
\frac{\mathrm{d}V}{1+V}+\frac{\mathrm{d}y}{y}=0,\qquad y(1+V)=C.
$$
代回 $V$：积分曲面族为 $\dfrac{y(x+z)}{y+z}=C$。（相应地，$\mu=\frac{1}{(y+z)^2}$ 是积分因子。）

**例 14.3.3（不可积的例子）** $\mathrm{d}z-y\,\mathrm{d}x=0$。$\boldsymbol{F}=(-y,0,1)$，$\operatorname{rot}\boldsymbol{F}=(0,0,1)$，$\boldsymbol{F}\cdot\operatorname{rot}\boldsymbol{F}=1\ne0$，不完全可积。几何上，点 $(x,y,z)$ 处的平面 $\mathrm{d}z=y\,\mathrm{d}x$ 在 $x$ 方向的斜率等于 $y$：沿 $y$ 轴前进时，这些平面绕平行于 $y$ 轴的直线不断转动，无法拼成曲面。与此相反，满足 (14.5) 的曲线（积分曲线）非常多：可以证明任意两点都能用这样的曲线连接。这类方程在热力学（Carathéodory 的熵的公理化）和控制论中都有重要意义。

## 14.4. $n$ 元 Pfaff 方程与 Frobenius 定理

$n$ 元 Pfaff 方程为

$$
\sum_{k=1}^nM_k(x_1,\dots,x_n)\,\mathrm{d}x_k=0,\tag{14.9}
$$
恰当与完全可积的定义与三元情形相同：恰当指左边是某个 $U$ 的全微分，完全可积指（局部地）存在积分因子 $\mu$ 使 $\mu\sum M_k\,\mathrm{d}x_k=\mathrm{d}U$，此时 $U=C$ 是 $n-1$ 维的积分超曲面族。

在单连通（例如凸）区域上，(14.9) 恰当当且仅当

$$
\frac{\partial M_i}{\partial x_j}=\frac{\partial M_j}{\partial x_i},\qquad1\le i<j\le n,\tag{14.10}
$$
共 $\binom n2$ 个条件。$n=3$ 时就是 $\operatorname{rot}\boldsymbol{F}=\boldsymbol{0}$。条件 (14.10) 只是完全可积的充分条件，而不是必要条件。

**例 14.4.1** 求 $\dfrac{m_1\,\mathrm{d}x_1}{x_1}+\dfrac{m_2\,\mathrm{d}x_2}{x_2}+\cdots+\dfrac{m_n\,\mathrm{d}x_n}{x_n}=0$ 的积分曲面，$m_1,\dots,m_n$ 是实常数，$x_k\ne0$。

**解** $M_k=m_k/x_k$ 只依赖于 $x_k$，$\frac{\partial M_i}{\partial x_j}=0=\frac{\partial M_j}{\partial x_i}$（$i\ne j$），方程恰当。积分得 $\sum_km_k\ln|x_k|=\ln C$，即积分超曲面族

$$
|x_1|^{m_1}|x_2|^{m_2}\cdots|x_n|^{m_n}=C\quad(C>0).
$$

一般情形下完全可积的条件用外微分的语言表述最为简洁。记 $\omega=\sum_kM_k\,\mathrm{d}x_k$，可积条件为 $\omega\wedge\mathrm{d}\omega=0$，在坐标中即对所有 $i<j<k$，

$$
M_i\Big(\frac{\partial M_k}{\partial x_j}-\frac{\partial M_j}{\partial x_k}\Big)+M_j\Big(\frac{\partial M_i}{\partial x_k}-\frac{\partial M_k}{\partial x_i}\Big)+M_k\Big(\frac{\partial M_j}{\partial x_i}-\frac{\partial M_i}{\partial x_j}\Big)=0,\tag{14.11}
$$
也就是对任意三个变量 $x_i,x_j,x_k$（把其余变量当作参数）写出三元条件 (14.6)。

**定理 14.4.1（Frobenius 定理）** 设 $M_1,\dots,M_n\in C^1(D)$ 不同时为零。则 Pfaff 方程 (14.9) 完全可积的充分必要条件是 (14.11) 在 $D$ 上成立。

必要性的证明与 定理 14.3.1 必要性的方法一相同。Frobenius 定理的一般形式讨论的是"由若干个向量场张成的子空间场何时是某族子流形的切空间"，Pfaff 方程是余维数为 1 的情形；它是微分几何中的基本定理。

另一种常见的写法是把一个变量 $u=x_{n+1}$ 解出来：设积分曲面为 $u=u(x_1,\dots,x_n)$，方程写成

$$
\mathrm{d}u=\sum_{k=1}^nM_k(x_1,\dots,x_n,u)\,\mathrm{d}x_k,
$$
它等价于一阶偏微分方程组 $\frac{\partial u}{\partial x_k}=M_k(\boldsymbol{x},u)$，$k=1,\dots,n$。与定理 14.3.1 必要性的方法二相同，由混合偏导数相等得完全可积的必要条件

$$
\frac{\partial M_j}{\partial x_i}+\frac{\partial M_j}{\partial u}M_i=\frac{\partial M_i}{\partial x_j}+\frac{\partial M_i}{\partial u}M_j,\qquad1\le i<j\le n,\tag{14.12}
$$
由 Frobenius 定理它也是充分的：(14.12) 成立时，对任意初值 $u(\boldsymbol{x}_0)=u_0$，方程组在 $\boldsymbol{x}_0$ 附近有唯一解。$n=2$ 时 (14.12) 就是 (14.8)。当 $M_k$ 都与 $u$ 无关时，(14.12) 退化为恰当条件 (14.10)。

## 14.5. 多元 Clairaut 方程

一元 **Clairaut 方程** $y=xy'+f(y')$ 的通解是直线族 $y=cx+f(c)$，奇解是这族直线的**包络**（[2.4.6](/2.4.6)）。它的多元推广是一阶非线性偏微分方程

$$
z=\sum_{k=1}^np_kx_k+f(p_1,\dots,p_n),\qquad p_k=\frac{\partial z}{\partial x_k},\tag{14.13}
$$
其中 $f$ 连续可微。

**定义 14.5.1（完全积分与奇积分）** 一阶偏微分方程 $F(x_1,\dots,x_n,z,p_1,\dots,p_n)=0$ 的含 $n$ 个独立任意常数 $c_1,\dots,c_n$ 的解族 $z=\Phi(\boldsymbol{x};c_1,\dots,c_n)$ 称为它的**完全积分**（complete integral）；完全积分族的包络（若存在）也是方程的解，称为**奇积分**（singular integral）。

**定理 14.5.1** 多元 Clairaut 方程 (14.13) 有完全积分（超平面族）

$$
z=\sum_{k=1}^nc_kx_k+f(c_1,\dots,c_n);\tag{14.14}
$$
从

$$
x_k=-\frac{\partial f}{\partial c_k}(c_1,\dots,c_n),\qquad k=1,\dots,n
$$
与 (14.14) 中消去 $c_1,\dots,c_n$（在可以消去时），得到奇积分。

**证明** (14.14) 中 $p_k=c_k$，代入即满足 (14.13)。包络的求法与一元情形相同：对参数求偏导并令其为零，$\frac{\partial}{\partial c_k}\big[\sum c_jx_j+f(c)\big]=x_k+\frac{\partial f}{\partial c_k}=0$。在包络上，$c$ 成为 $\boldsymbol{x}$ 的函数，由这些条件 $\frac{\partial z}{\partial x_k}=c_k+\sum_j\big(x_j+\frac{\partial f}{\partial c_j}\big)\frac{\partial c_j}{\partial x_k}=c_k$，所以包络也满足 (14.13)。$\square$

**例 14.5.1** 求 $z=xp+yq+pq$（$p=z_x$，$q=z_y$）的完全积分与奇积分。

**解** 完全积分 $z=ax+by+ab$。对 $a,b$ 求偏导：$x+b=0$，$y+a=0$，即 $a=-y$，$b=-x$，代入得奇积分

$$
z=(-y)x+(-x)y+(-y)(-x)=-xy.
$$
直接验证：$z=-xy$ 时 $p=-y$，$q=-x$，$xp+yq+pq=-xy-xy+xy=-xy$。奇积分是双曲抛物面，完全积分中的每个平面都是它的切平面。

**例 14.5.2** 求 $z=xp+yq+\sqrt{1+p^2+q^2}$ 的奇积分。

**解** 完全积分 $z=ax+by+\sqrt{1+a^2+b^2}$。记 $s=\sqrt{1+a^2+b^2}$，包络条件为 $x=-\frac as$，$y=-\frac bs$，于是 $x^2+y^2=\frac{a^2+b^2}{s^2}=1-\frac1{s^2}$，而

$$
z=-\frac{a^2+b^2}{s}+s=\frac1s.
$$
所以 $x^2+y^2+z^2=1$（$z>0$）：奇积分是上半单位球面。几何上，完全积分是所有到原点距离为 $1$、且原点位于其下方的平面（$z=ax+by+s$ 到原点的距离为 $s/\sqrt{1+a^2+b^2}=1$），它们的包络自然是单位球面。

一般的一阶非线性偏微分方程也可以用特征线方法求解（Lagrange–Charpit 方法），完全积分与奇积分的理论在那里起核心作用，见 [2.5](/2.5)。

## 小结

| 对象 | 定义 / 条件 | 求法 |
|---|---|---|
| 首次积分 $\Phi$ | 沿解不变 ⟺ $\nabla\Phi\cdot\boldsymbol{f}=0$ | 可积组合；非平衡点附近有 $n-1$ 个独立的 |
| 线性齐次偏微分方程 $\sum f_iu_{x_i}=0$ | 解 = 首次积分的任意函数 | 特征方程组 $\frac{\mathrm{d}x_1}{f_1}=\cdots=\frac{\mathrm{d}x_n}{f_n}$ |
| Pfaff 方程恰当 | $\omega=\mathrm{d}U$ ⟺（单连通）$\operatorname{rot}\boldsymbol{F}=\boldsymbol{0}$ 或 (14.10) | 求势函数 |
| Pfaff 方程完全可积 | 存在积分因子 ⟺ $\boldsymbol{F}\cdot\operatorname{rot}\boldsymbol{F}=0$ 或 (14.11)（Frobenius） | 先固定一个变量求积，再定"常数" |
| 多元 Clairaut 方程 | $z=\sum p_kx_k+f(\boldsymbol{p})$ | 完全积分：超平面族；奇积分：其包络 |
