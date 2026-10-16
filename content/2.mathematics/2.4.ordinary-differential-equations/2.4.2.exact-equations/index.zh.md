---
title: 恰当方程与积分因子
---

初等积分法的出发点是：对称形式的一阶方程 $P\,\mathrm{d}x+Q\,\mathrm{d}y=0$ 若左端恰好是某个函数的全微分，方程就立即"积出来"了。本章先严格证明判别这一点的充要条件 $\partial P/\partial y=\partial Q/\partial x$，给出两种构造原函数的积分路径与凑全微分的常用公式；然后讨论把一般方程化为恰当方程的积分因子：它满足的偏微分方程、只依赖一个变量的积分因子的充要条件、积分因子的全体，以及分组求积分因子的方法。下一章 [2.4.3](/2.4.3) 的变量分离方程与一阶线性方程都可以看作这里的特例。例行的解题步骤与较多的例题见微积分 [2.2.15](/2.2.15#sec-15.4)，这里侧重理论。

## 2.1. 恰当方程

### 2.1.1. 定义

考虑对称形式的一阶方程

$$
P(x,y)\,\mathrm{d}x+Q(x,y)\,\mathrm{d}y=0,\tag{2.1}
$$
其中 $P,Q$ 在区域 $D$ 上连续，且不同时为零。

**定义 2.1.1** 若存在 $D$ 上的可微函数 $\Phi(x,y)$，使

$$
\mathrm{d}\Phi(x,y)=P(x,y)\,\mathrm{d}x+Q(x,y)\,\mathrm{d}y,\quad\text{即}\quad\frac{\partial\Phi}{\partial x}=P,\quad\frac{\partial\Phi}{\partial y}=Q,\tag{2.2}
$$
则称方程 (2.1) 为**恰当方程**（**全微分方程**）。

**定理 2.1.1** 设方程 (2.1) 是恰当方程，$\Phi$ 满足式 (2.2)。则在 $Q\ne0$ 的区域内，可微函数 $y=\varphi(x)$ 是方程 (2.1) 的解，当且仅当 $\Phi\big(x,\varphi(x)\big)$ 为常数。因此 $\Phi(x,y)=C$ 是方程 (2.1) 的通积分；满足 $y(x_0)=y_0$ 的解由 $\Phi(x,y)=\Phi(x_0,y_0)$ 确定。

**证明** 由链式法则，

$$
\frac{\mathrm{d}}{\mathrm{d}x}\Phi\big(x,\varphi(x)\big)=P\big(x,\varphi(x)\big)+Q\big(x,\varphi(x)\big)\varphi'(x),
$$
所以 $\varphi$ 满足方程 $P+Qy'=0$ 当且仅当 $\Phi(x,\varphi(x))$ 的导数恒为零，即它为常数。反过来，在 $Q=\Phi_y\ne0$ 处，由**隐函数定理**，$\Phi(x,y)=\Phi(x_0,y_0)$ 在 $(x_0,y_0)$ 附近确定唯一的可微函数 $y=\varphi(x)$，$\varphi(x_0)=y_0$，它就是所求的解。$P\ne0$ 处同理，把 $x$ 看作 $y$ 的函数。 $\square$

几何上，恰当方程的积分曲线就是函数 $\Phi$ 的等值线。由证明还看到：在 $Q\ne0$ 处，过每一点恰有一条积分曲线，初值问题的解存在且唯一。

### 2.1.2. 判别条件

**定理 2.1.2** 设 $P,Q$ 在矩形 $D=\{(x,y)\mid a<x<b,\ c<y<d\}$ 上连续，且有连续的偏导数 $\dfrac{\partial P}{\partial y}$、$\dfrac{\partial Q}{\partial x}$。则方程 (2.1) 是恰当方程的充要条件是

$$
\frac{\partial P}{\partial y}(x,y)\equiv\frac{\partial Q}{\partial x}(x,y),\qquad(x,y)\in D.\tag{2.3}
$$
条件成立时，对任意 $(x_0,y_0)\in D$，方程的通积分为

$$
\int_{x_0}^xP(s,y)\,\mathrm{d}s+\int_{y_0}^yQ(x_0,t)\,\mathrm{d}t=C\tag{2.4}
$$
或

$$
\int_{x_0}^xP(s,y_0)\,\mathrm{d}s+\int_{y_0}^yQ(x,t)\,\mathrm{d}t=C.\tag{2.5}
$$

**证明** 必要性。设 $\Phi$ 满足式 (2.2)，则

$$
\frac{\partial P}{\partial y}=\frac{\partial^2\Phi}{\partial y\,\partial x},\qquad\frac{\partial Q}{\partial x}=\frac{\partial^2\Phi}{\partial x\,\partial y}.
$$
由假设，两个混合偏导数都连续，所以它们相等（[2.2.10 命题 10.5.1](/2.2.10#prop-10.5.1)），即得式 (2.3)。

充分性。设式 (2.3) 成立，要构造满足式 (2.2) 的 $\Phi$。先要求第一式成立，令

$$
\Phi(x,y)=\int_{x_0}^xP(s,y)\,\mathrm{d}s+\psi(y),
$$
其中 $\psi$ 待定；矩形保证线段 $[x_0,x]\times\{y\}$ 在 $D$ 内。因为 $P$ 与 $P_y$ 在 $D$ 上连续，可以**积分号下求导**（在包含所论点的闭矩形上应用），再用式 (2.3)：

$$
\frac{\partial\Phi}{\partial y}=\int_{x_0}^x\frac{\partial P}{\partial y}(s,y)\,\mathrm{d}s+\psi'(y)=\int_{x_0}^x\frac{\partial Q}{\partial x}(s,y)\,\mathrm{d}s+\psi'(y)=Q(x,y)-Q(x_0,y)+\psi'(y).
$$
为使第二式成立，只需取 $\psi'(y)=Q(x_0,y)$，即 $\psi(y)=\displaystyle\int_{y_0}^yQ(x_0,t)\,\mathrm{d}t$。这样构造出的

$$
\Phi(x,y)=\int_{x_0}^xP(s,y)\,\mathrm{d}s+\int_{y_0}^yQ(x_0,t)\,\mathrm{d}t
$$
满足式 (2.2)，由定理 2.1.1 得通积分 (2.4)。同理（先满足第二式）可构造

$$
\Psi(x,y)=\int_{x_0}^xP(s,y_0)\,\mathrm{d}s+\int_{y_0}^yQ(x,t)\,\mathrm{d}t.
$$
$\Phi$ 与 $\Psi$ 有相同的全微分，在连通的 $D$ 上只差一个常数；又 $\Phi(x_0,y_0)=\Psi(x_0,y_0)=0$，所以 $\Phi\equiv\Psi$，式 (2.5) 与 (2.4) 给出同一个通积分。 $\square$

式 (2.4) 是沿折线 $(x_0,y_0)\to(x_0,y)\to(x,y)$ 的第二型曲线积分，式 (2.5) 是沿 $(x_0,y_0)\to(x,y_0)\to(x,y)$ 的。证明中矩形的作用只是保证折线在 $D$ 内。定理对一般的**单连通区域**也成立：此时由 **Green 公式**，式 (2.3) 保证曲线积分与路径无关，$\Phi(x,y)=\int_{(x_0,y_0)}^{(x,y)}P\,\mathrm{d}x+Q\,\mathrm{d}y$ 是原函数（$P\boldsymbol{i}+Q\boldsymbol{j}$ 是**保守场**，[2.2.14](/2.2.14)）。区域不是单连通时结论可能不成立。

**例 2.1.1** 在去掉原点的平面上，

$$
\frac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2+y^2}=0
$$
满足式 (2.3)：$P=\dfrac{-y}{x^2+y^2}$，$Q=\dfrac{x}{x^2+y^2}$，$P_y=Q_x=\dfrac{y^2-x^2}{(x^2+y^2)^2}$。但沿单位圆逆时针一周，左端的积分为 $2\pi\ne0$，所以在整个去心平面上不存在单值的原函数，方程不是恰当方程。在任何不含原点、也不绕原点的单连通区域（例如右半平面）内，它是恰当的，$\Phi=\arctan\dfrac yx$（极角）。积分曲线是从原点出发的射线 $\theta=C$，与例 1.2.1 的 $y'=y/x$ 相同；只是"极角"这个通积分不能在整个去心平面上连续地取值。

### 2.1.3. 例题

偏积分与折线积分的详细步骤见 [2.2.15 算法 15.4.1](/2.2.15#alg-15.4.1)。

**例 2.1.2** 解 $(2x\sin y+3x^2y)\,\mathrm{d}x+(x^3+x^2\cos y+y^2)\,\mathrm{d}y=0$。

$P_y=2x\cos y+3x^2=Q_x$，是恰当方程。由 $\Phi_x=2x\sin y+3x^2y$ 对 $x$ 积分，$\Phi=x^2\sin y+x^3y+\psi(y)$；代入 $\Phi_y=x^2\cos y+x^3+\psi'(y)=x^3+x^2\cos y+y^2$，得 $\psi'(y)=y^2$，$\psi=\dfrac13y^3$。通积分为

$$
x^2\sin y+x^3y+\frac13y^3=C.
$$
也可以分组凑全微分：

$$
(2x\sin y\,\mathrm{d}x+x^2\cos y\,\mathrm{d}y)+(3x^2y\,\mathrm{d}x+x^3\,\mathrm{d}y)+y^2\,\mathrm{d}y=\mathrm{d}(x^2\sin y)+\mathrm{d}(x^3y)+\mathrm{d}\Big(\frac13y^3\Big).
$$

![例 2.1.2 的积分曲线即函数 Phi(x, y) = x^2 sin y + x^3 y + y^3/3 的等值线；图中给出 Phi = C 的若干条，颜色表示 C 的值](./plots/exact-level-curves.py)

**例 2.1.3** 解 $(3x^2+6xy^2)\,\mathrm{d}x+(6x^2y+4y^3)\,\mathrm{d}y=0$。$P_y=12xy=Q_x$。由式 (2.5) 取 $(x_0,y_0)=(0,0)$：

$$
\int_0^x3s^2\,\mathrm{d}s+\int_0^y(6x^2t+4t^3)\,\mathrm{d}t=x^3+3x^2y^2+y^4=C.
$$

## 2.2. 凑全微分

### 2.2.1. 常用的全微分公式

许多方程不必验证式 (2.3)，把左端的项适当分组，利用下列公式直接凑出全微分。各式在分母不为零的区域内成立。

| 微分式 | 全微分 | 微分式 | 全微分 |
|---|---|---|---|
| $y\,\mathrm{d}x+x\,\mathrm{d}y$ | $\mathrm{d}(xy)$ | $x\,\mathrm{d}x+y\,\mathrm{d}y$ | $\dfrac12\mathrm{d}(x^2+y^2)$ |
| $\dfrac{y\,\mathrm{d}x-x\,\mathrm{d}y}{y^2}$ | $\mathrm{d}\Big(\dfrac xy\Big)$ | $\dfrac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2}$ | $\mathrm{d}\Big(\dfrac yx\Big)$ |
| $\dfrac{y\,\mathrm{d}x-x\,\mathrm{d}y}{xy}$ | $\mathrm{d}\Big(\ln\Big\lvert\dfrac xy\Big\rvert\Big)$ | $\dfrac{y\,\mathrm{d}x+x\,\mathrm{d}y}{xy}$ | $\mathrm{d}(\ln\lvert xy\rvert)$ |
| $\dfrac{y\,\mathrm{d}x-x\,\mathrm{d}y}{x^2+y^2}$ | $\mathrm{d}\Big(\arctan\dfrac xy\Big)$ | $\dfrac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2+y^2}$ | $\mathrm{d}\Big(\arctan\dfrac yx\Big)$ |
| $\dfrac{y\,\mathrm{d}x-x\,\mathrm{d}y}{x^2-y^2}$ | $\dfrac12\mathrm{d}\Big(\ln\Big\lvert\dfrac{x-y}{x+y}\Big\rvert\Big)$ | $\dfrac{x\,\mathrm{d}x+y\,\mathrm{d}y}{x^2+y^2}$ | $\dfrac12\mathrm{d}\ln(x^2+y^2)$ |

左列与右列中分子为 $y\,\mathrm{d}x-x\,\mathrm{d}y$ 或 $x\,\mathrm{d}y-y\,\mathrm{d}x$ 的各式说明：同一个微分式乘以不同的因子（$1/y^2$、$1/x^2$、$1/(xy)$、$1/(x^2\pm y^2)$）都能成为全微分。这正是 2.3 节积分因子不唯一的例子。

### 2.2.2. 例题

**例 2.2.1** 解 $xf'(x^2+y^2)\,\mathrm{d}x+yf'(x^2+y^2)\,\mathrm{d}y=0$，其中 $f$ 连续可微。左端等于 $\dfrac12\mathrm{d}\big[f(x^2+y^2)\big]$，通积分为 $f(x^2+y^2)=C$。

**例 2.2.2** 解 $x\,\mathrm{d}x+\dfrac{(x+y)\,\mathrm{d}x-(x-y)\,\mathrm{d}y}{x^2+y^2}=0$。把分式拆成两组：

$$
x\,\mathrm{d}x+\frac{x\,\mathrm{d}x+y\,\mathrm{d}y}{x^2+y^2}+\frac{y\,\mathrm{d}x-x\,\mathrm{d}y}{x^2+y^2}=\mathrm{d}\Big[\frac{x^2}{2}+\frac12\ln(x^2+y^2)+\arctan\frac xy\Big]=0,
$$
通积分为 $\dfrac{x^2}{2}+\dfrac12\ln(x^2+y^2)+\arctan\dfrac xy=C$（在 $y\ne0$ 的区域内；跨过 $y=0$ 时 $\arctan\frac xy$ 要换成连续的分支）。

**例 2.2.3** 解初值问题 $xy\,\mathrm{d}x+\dfrac12(x^2+y)\,\mathrm{d}y=0$，$y(0)=2$。

左端 $=\Big(xy\,\mathrm{d}x+\dfrac{x^2}2\,\mathrm{d}y\Big)+\dfrac y2\,\mathrm{d}y=\mathrm{d}\Big(\dfrac{x^2y}{2}\Big)+\mathrm{d}\Big(\dfrac{y^2}{4}\Big)$，通积分 $2x^2y+y^2=C$。由 $y(0)=2$ 得 $C=4$。解关于 $y$ 的二次方程 $y^2+2x^2y-4=0$，取满足 $y(0)=2$ 的根：

$$
y=-x^2+\sqrt{x^4+4},\qquad x\in\mathbb{R}.
$$

![例 2.2.3 的积分曲线族 2x^2 y + y^2 = C（细线）与初值问题 y(0) = 2 的解 y = -x^2 + sqrt(x^4 + 4)（粗线），它在整个实轴上存在并随 |x| 增大趋于 0](./plots/ivp-family.py)

## 2.3. 积分因子

### 2.3.1. 定义与满足的方程

**定义 2.3.1** 若存在在区域 $D$ 上连续可微、处处不为零的函数 $\mu(x,y)$，使

$$
\mu(x,y)P(x,y)\,\mathrm{d}x+\mu(x,y)Q(x,y)\,\mathrm{d}y=0
$$
是恰当方程，则称 $\mu$ 为方程 (2.1) 的**积分因子**。

$\mu\ne0$ 保证乘以 $\mu$ 不改变方程的积分曲线。实际计算中得到的积分因子常在某些曲线上为零或无定义（例如 $1/y^2$ 在 $y=0$ 上），这些曲线要单独检查是否给出解。在矩形区域内由定理 2.1.2，$\mu$ 是积分因子当且仅当 $(\mu P)_y=(\mu Q)_x$，即

$$
Q\frac{\partial\mu}{\partial x}-P\frac{\partial\mu}{\partial y}=\Big(\frac{\partial P}{\partial y}-\frac{\partial Q}{\partial x}\Big)\mu.\tag{2.6}
$$
这是关于 $\mu$ 的一阶线性偏微分方程。可以证明（[2.4.14](/2.4.14) 的首次积分理论）：$P,Q$ 连续可微且不同时为零时，积分因子在局部上总是存在的；但求解式 (2.6) 一般要用到原方程 (2.1) 的特征线，也就是原方程的解，所以通常不能用来求积分因子。实用的办法是限定 $\mu$ 的形式，使式 (2.6) 退化为常微分方程。

### 2.3.2. 只依赖于一个变量的积分因子

**定理 2.3.1** 设 $P,Q$ 在区域 $D$ 上连续可微，$Q\ne0$。方程 (2.1) 有只依赖于 $x$ 的积分因子的充要条件是

$$
G=\frac{1}{Q}\Big(\frac{\partial P}{\partial y}-\frac{\partial Q}{\partial x}\Big)\tag{2.7}
$$
只依赖于 $x$，即 $G=G(x)$。此时 $\mu(x)=\mathrm{e}^{\int G(x)\,\mathrm{d}x}$ 是一个积分因子。

**证明** 必要性。若 $\mu=\mu(x)$ 是积分因子，则 $\mu_y=0$，式 (2.6) 化为 $Q\mu'(x)=(P_y-Q_x)\mu$，即

$$
\frac{\mu'(x)}{\mu(x)}=\frac{1}{Q}\Big(\frac{\partial P}{\partial y}-\frac{\partial Q}{\partial x}\Big).
$$
左端只依赖于 $x$，所以右端也只依赖于 $x$。

充分性。若 $G=G(x)$，令 $\mu=\mathrm{e}^{\int G\,\mathrm{d}x}$，则 $\mu'=G\mu$，$Q\mu'-P\cdot0=QG\mu=(P_y-Q_x)\mu$，式 (2.6) 成立。 $\square$

对称地，在 $P\ne0$ 时，方程有只依赖于 $y$ 的积分因子的充要条件是

$$
H=\frac{1}{P}\Big(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Big)
$$
只依赖于 $y$，此时 $\mu(y)=\mathrm{e}^{\int H(y)\,\mathrm{d}y}$ 是积分因子。

**例 2.3.1** 一阶线性方程 $y'+p(x)y=q(x)$ 写成 $\big(p(x)y-q(x)\big)\,\mathrm{d}x+\mathrm{d}y=0$，$P_y-Q_x=p(x)$，$G=p(x)$ 只依赖于 $x$，积分因子 $\mu=\mathrm{e}^{\int p(x)\,\mathrm{d}x}$。乘以 $\mu$ 后方程成为 $\mathrm{d}\Big(y\mathrm{e}^{\int p\,\mathrm{d}x}\Big)=q\mathrm{e}^{\int p\,\mathrm{d}x}\,\mathrm{d}x$，积分即得 [2.4.3](/2.4.3) 的求解公式。注意 $1/\mu=\mathrm{e}^{-\int p\,\mathrm{d}x}$ 正是对应齐次方程的一个非零解。

**例 2.3.2** 变量分离方程 $X(x)Y_1(y)\,\mathrm{d}x+X_1(x)Y(y)\,\mathrm{d}y=0$ 有积分因子 $\dfrac{1}{X_1(x)Y_1(y)}$（在 $X_1Y_1\ne0$ 处），乘以它后成为 $\dfrac{X}{X_1}\,\mathrm{d}x+\dfrac{Y}{Y_1}\,\mathrm{d}y=0$，两项各自是全微分。

同样的推导适用于形如 $\mu=\mu\big(\omega(x,y)\big)$ 的积分因子（$\omega$ 是给定的函数，如 $x+y$、$xy$、$x^2+y^2$）：代入式 (2.6) 得

$$
\frac{\mu'(\omega)}{\mu(\omega)}=\frac{P_y-Q_x}{Q\omega_x-P\omega_y},
$$
所以方程有这种形式的积分因子，当且仅当右端只是 $\omega$ 的函数。$\omega=x$、$\omega=y$ 就是定理 2.3.1 的两种情形。

**例 2.3.3** 解 $(x^2+y^2+x)\,\mathrm{d}x+xy\,\mathrm{d}y=0$。$P_y-Q_x=2y-y=y$，$G=\dfrac{y}{xy}=\dfrac1x$，积分因子 $\mu=x$，通积分 $\dfrac{x^4}{4}+\dfrac{x^3}{3}+\dfrac{x^2y^2}{2}=C$（[2.2.15 例 15.4.3](/2.2.15#ex-15.4.3)）。

### 2.3.3. 积分因子的全体

**定理 2.3.2** 设 $\mu$ 是方程 (2.1) 的积分因子，$\mu(P\,\mathrm{d}x+Q\,\mathrm{d}y)=\mathrm{d}\Phi$。则对任意连续可微且不为零的函数 $g$，$\mu g(\Phi)$ 也是方程 (2.1) 的积分因子。反之，在 $\nabla\Phi\ne\boldsymbol{0}$ 的点附近，方程 (2.1) 的任一积分因子都可以写成 $\mu g(\Phi)$ 的形式。

**证明** 取 $g$ 的一个原函数 $\tilde G$，则

$$
\mu g(\Phi)(P\,\mathrm{d}x+Q\,\mathrm{d}y)=g(\Phi)\,\mathrm{d}\Phi=\mathrm{d}\big(\tilde G(\Phi)\big),
$$
所以 $\mu g(\Phi)$ 是积分因子。反之，设 $\mu_1$ 也是积分因子，$\mu_1(P\,\mathrm{d}x+Q\,\mathrm{d}y)=\mathrm{d}\Phi_1$，则 $\nabla\Phi_1=\dfrac{\mu_1}{\mu}\nabla\Phi$，两个梯度平行，Jacobi 行列式 $\dfrac{\partial(\Phi_1,\Phi)}{\partial(x,y)}\equiv0$。在 $\nabla\Phi\ne\boldsymbol{0}$ 的点附近，不妨设 $\Phi_y\ne0$，作变量替换 $(x,y)\mapsto(x,\Phi)$（由**逆映射定理**局部可逆），把 $\Phi_1$ 看作 $x$ 与 $\Phi$ 的函数，则

$$
\frac{\partial\Phi_1}{\partial x}\Big|_{\Phi\ \text{固定}}=\frac{\partial\Phi_1}{\partial x}-\frac{\partial\Phi_1}{\partial y}\cdot\frac{\Phi_x}{\Phi_y}=\frac{1}{\Phi_y}\cdot\frac{\partial(\Phi_1,\Phi)}{\partial(x,y)}=0,
$$
所以局部地 $\Phi_1=F(\Phi)$。由 $\mathrm{d}\Phi_1=F'(\Phi)\,\mathrm{d}\Phi$ 得 $\mu_1=\mu F'(\Phi)$，取 $g=F'$ 即可。 $\square$

**推论 2.3.1** 若 $\mu_1,\mu_2$ 是方程 (2.1) 的两个积分因子，且 $\mu_1/\mu_2$ 不是常数，则 $\dfrac{\mu_1}{\mu_2}=C$ 是方程 (2.1) 的通积分。

**证明** 由定理 2.3.2，局部地 $\mu_1/\mu_2=g(\Phi)$。它在每条积分曲线 $\Phi=C$ 上是常数，而且不是常函数，所以 $\mu_1/\mu_2=C$ 给出的正是积分曲线族。 $\square$

例如对 $y\,\mathrm{d}x-x\,\mathrm{d}y=0$，$\dfrac1{y^2}$ 与 $\dfrac1{xy}$ 都是积分因子，比值 $\dfrac{x}{y}=C$ 正是积分曲线族（过原点的直线）。定理 2.3.2 也给出了下面分组法的依据。

### 2.3.4. 分组求积分因子

设方程 (2.1) 的左端可以分成两组：

$$
(P_1\,\mathrm{d}x+Q_1\,\mathrm{d}y)+(P_2\,\mathrm{d}x+Q_2\,\mathrm{d}y)=0,
$$
两组分别有积分因子 $\mu_1,\mu_2$：$\mu_1(P_1\,\mathrm{d}x+Q_1\,\mathrm{d}y)=\mathrm{d}\Phi_1$，$\mu_2(P_2\,\mathrm{d}x+Q_2\,\mathrm{d}y)=\mathrm{d}\Phi_2$。由定理 2.3.2，$\mu_1g_1(\Phi_1)$ 是第一组的任一积分因子，$\mu_2g_2(\Phi_2)$ 是第二组的任一积分因子。若能选取 $g_1,g_2$ 使

$$
\mu_1g_1(\Phi_1)=\mu_2g_2(\Phi_2)=\mu,
$$
则 $\mu$ 同时使两组成为全微分，从而是整个方程的积分因子。实际操作中常取 $g_1,g_2$ 为幂函数，比较两边的指数。

**例 2.3.4** 解 $(x^3y-2y^2)\,\mathrm{d}x+x^4\,\mathrm{d}y=0$。

分组为 $(x^3y\,\mathrm{d}x+x^4\,\mathrm{d}y)-2y^2\,\mathrm{d}x=0$。第一组 $=x^3(y\,\mathrm{d}x+x\,\mathrm{d}y)=x^3\,\mathrm{d}(xy)$，积分因子 $\mu_1=\dfrac1{x^3}$，$\Phi_1=xy$；第二组 $-2y^2\,\mathrm{d}x$ 的积分因子 $\mu_2=\dfrac1{y^2}$，$\Phi_2=x$。要找 $g_1,g_2$ 使

$$
\frac{1}{x^3}g_1(xy)=\frac{1}{y^2}g_2(x).
$$
取 $g_1(u)=u^{-2}$，左端 $=\dfrac{1}{x^5y^2}$；取 $g_2(x)=x^{-5}$，右端也是 $\dfrac{1}{x^5y^2}$。于是 $\mu=\dfrac{1}{x^5y^2}$，乘以它后方程成为

$$
\frac{\mathrm{d}(xy)}{(xy)^2}-\frac{2\,\mathrm{d}x}{x^5}=\mathrm{d}\Big(-\frac{1}{xy}+\frac{1}{2x^4}\Big)=0,
$$
通积分 $\dfrac{1}{2x^4}-\dfrac{1}{xy}=C$，即 $y-2x^3=2Cx^4y$。积分因子在 $x=0$、$y=0$ 上无定义，检查知 $x=0$ 与 $y=0$ 也是解；$y=0$ 不在通积分中（$C$ 取任何值都得不到），要单独列出。

## 小结

| 内容 | 结论 |
|---|---|
| 恰当方程 | $\mathrm{d}\Phi=P\,\mathrm{d}x+Q\,\mathrm{d}y$，通积分 $\Phi=C$，积分曲线是 $\Phi$ 的等值线 |
| 判别 | 矩形或单连通区域内 ⇔ $P_y=Q_x$；通积分 (2.4)、(2.5)；非单连通时可能不成立（例 2.1.1） |
| 积分因子的方程 | $Q\mu_x-P\mu_y=(P_y-Q_x)\mu$ |
| $\mu=\mu(x)$ | ⇔ $(P_y-Q_x)/Q$ 只依赖于 $x$；$\mu=\mathrm{e}^{\int G\,\mathrm{d}x}$ |
| $\mu=\mu(y)$ | ⇔ $(Q_x-P_y)/P$ 只依赖于 $y$；$\mu=\mathrm{e}^{\int H\,\mathrm{d}y}$ |
| $\mu=\mu(\omega)$ | ⇔ $(P_y-Q_x)/(Q\omega_x-P\omega_y)$ 只是 $\omega$ 的函数 |
| 全体积分因子 | $\mu g(\Phi)$；两个积分因子之比 $=C$ 是通积分 |
| 分组法 | 使 $\mu_1g_1(\Phi_1)=\mu_2g_2(\Phi_2)$ |
