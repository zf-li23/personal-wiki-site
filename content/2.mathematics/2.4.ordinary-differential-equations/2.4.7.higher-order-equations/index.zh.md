---
title: 高阶方程与解对初值的依赖性
---

本章从一阶方程过渡到高阶方程与方程组。先介绍几类可以降阶的高阶方程，补充 [2.2.15](/2.2.15) §15.5 的内容；然后说明任何标准形式的高阶方程或方程组都等价于一阶方程组 $\boldsymbol{y}'=\boldsymbol{f}(x,\boldsymbol{y})$，只要在 $\mathbb{R}^n$ 中引入范数，[2.4.4](/2.4.4) 与 [2.4.5](/2.4.5) 的存在唯一性定理、延伸定理就逐字推广过来。最后讨论解对初值和参数的依赖性：Lipschitz 条件下解连续地依赖于初值与参数（误差至多指数增长，由 Gronwall 不等式控制），右端光滑时解可微，其导数满足变分方程。这是方程能够描述物理现象的前提，也是 [2.4.11](/2.4.11) 稳定性理论的出发点。线性方程组与高阶线性方程的系统理论见 [2.4.8](/2.4.8)、[2.4.9](/2.4.9)。

## 7.1. 可降阶的高阶方程

降阶的思路是：通过换未知函数或换自变量，把 $n$ 阶方程化为较低阶的方程，求出低阶方程的解后再积分。[2.2.15](/2.2.15) 已经讨论了 $y^{(n)}=f(x)$、$y''=f(x,y')$ 与 $y''=f(y,y')$ 三类，这里给出它们的一般形式和更多的类型。

### 7.1.1. Cauchy 重积分公式

**命题 7.1.1（Cauchy 公式）** 设 $f$ 在区间 $I$ 上连续，$x_0\in I$，则 $y^{(n)}=f(x)$ 满足 $y(x_0)=y'(x_0)=\cdots=y^{(n-1)}(x_0)=0$ 的解为

$$
y(x)=\frac{1}{(n-1)!}\int_{x_0}^x(x-t)^{n-1}f(t)\,\mathrm{d}t, \tag{7.1}
$$
通解为

$$
y(x)=\frac{1}{(n-1)!}\int_{x_0}^x(x-t)^{n-1}f(t)\,\mathrm{d}t+\sum_{k=0}^{n-1}c_k(x-x_0)^k.
$$

**证明** 记 (7.1) 的右端为 $y_n(x)$。由**积分号下求导**（积分上限也含 $x$，但 $k<n-1$ 时被积函数在 $t=x$ 处为零），

$$
y_n^{(k)}(x)=\frac{1}{(n-1-k)!}\int_{x_0}^x(x-t)^{n-1-k}f(t)\,\mathrm{d}t,\qquad k=0,1,\dots,n-1,
$$
所以 $y_n^{(k)}(x_0)=0$，$y_n^{(n-1)}(x)=\int_{x_0}^xf(t)\,\mathrm{d}t$，$y_n^{(n)}=f$。齐次方程 $y^{(n)}=0$ 的解是次数小于 $n$ 的多项式。 $\square$

公式 (7.1) 把 $n$ 重积分 $\int_{x_0}^x\int_{x_0}^{t_{n-1}}\cdots\int_{x_0}^{t_1}f(t)\,\mathrm{d}t\,\mathrm{d}t_1\cdots\mathrm{d}t_{n-1}$ 化成一个积分，$n=2$ 时就是 $y=\int_{x_0}^x(x-t)f(t)\,\mathrm{d}t+c_1(x-x_0)+c_0$。

### 7.1.2. 不显含未知函数的方程

方程 $F(x,y^{(k)},y^{(k+1)},\dots,y^{(n)})=0$ 不含 $y,y',\dots,y^{(k-1)}$。令 $z=y^{(k)}$，它化为 $n-k$ 阶方程 $F(x,z,z',\dots,z^{(n-k)})=0$；求出 $z=\omega(x,c_1,\dots,c_{n-k})$ 后，由 Cauchy 公式积分 $k$ 次得到 $y$。

特别地，$y''=f(y')$ 令 $z=y'$ 得变量分离方程 $z'=f(z)$，$x=\displaystyle\int_{z_0}^z\frac{\mathrm{d}t}{f(t)}+c$，反解出 $z$ 后再积分一次。

### 7.1.3. 不显含自变量的方程与能量积分

方程 $y''=f(y,y')$ 不含 $x$，以 $y$ 为自变量、令 $y'=z(y)$，则 $y''=z\dfrac{\mathrm{d}z}{\mathrm{d}y}$，方程化为一阶方程 $z\dfrac{\mathrm{d}z}{\mathrm{d}y}=f(y,z)$。最重要的特例是右端只含 $y$ 的方程。

**命题 7.1.2（能量积分）** 设 $f$ 连续，$\mathcal{V}(y)=-\displaystyle\int_{y_0}^yf(s)\,\mathrm{d}s$。则 $y''=f(y)$ 的每个解满足

$$
\frac12(y')^2+\mathcal{V}(y)=E \tag{7.2}
$$
（$E$ 为常数），并且在 $y'\ne0$ 的区间上

$$
x=\pm\int\frac{\mathrm{d}y}{\sqrt{2\big(E-\mathcal{V}(y)\big)}}+c.
$$

**证明** 两边乘以 $y'$：$y''y'=f(y)y'$，即 $\dfrac{\mathrm{d}}{\mathrm{d}x}\Big(\dfrac12(y')^2\Big)=-\dfrac{\mathrm{d}}{\mathrm{d}x}\mathcal{V}(y)$，积分得 (7.2)。解出 $y'=\pm\sqrt{2(E-\mathcal{V}(y))}$ 后分离变量。 $\square$

物理上，$y''=f(y)$ 是单位质量的质点在保守力 $f(y)$ 作用下的运动方程，$\frac12(y')^2$ 是动能，$\mathcal{V}$ 是势能，(7.2) 是能量守恒。这样的 $E$ 称为方程的一个首次积分（[2.4.14](/2.4.14)）。

**例 7.1.1** 解 $y''=2y^3$，$y(0)=1$，$y'(0)=1$。由 (7.2)，$(y')^2=y^4+c_1$，由初值 $c_1=0$；又 $y'(0)>0$，所以 $y'=y^2$，$-\dfrac1y=x-1$，

$$
y=\frac{1}{1-x},\qquad x<1.
$$
解在 $x\to1^-$ 时爆破，最大存在区间为 $(-\infty,1)$。

**例 7.1.2（单摆）** 无阻尼单摆的摆角满足 $\theta''+\omega^2\sin\theta=0$。能量积分为 $\dfrac12(\theta')^2-\omega^2\cos\theta=E$。$E<\omega^2$ 时 $\theta$ 在 $\lvert\theta\rvert\le\theta_{\max}$ 内往复摆动（$\cos\theta_{\max}=-E/\omega^2$），周期为

$$
T=4\int_0^{\theta_{\max}}\frac{\mathrm{d}\theta}{\sqrt{2\omega^2(\cos\theta-\cos\theta_{\max})}},
$$
是一个椭圆积分，振幅越大周期越长；$E>\omega^2$ 时单摆越过最高点不停旋转；$E=\omega^2$ 的分界情形对应趋于倒立位置的运动。在 $(\theta,\theta')$ 平面上，能量积分的等值线就是解的轨线。

![单摆 theta'' + sin theta = 0 的能量等值线 (theta')^2/2 - cos theta = E：闭曲线是往复摆动，上下两侧的曲线是旋转运动，经过 (±pi, 0) 的分界线（E = 1）把两者分开](./plots/pendulum-energy.py)

$y''=f(ax+by)$（$b\ne0$）也可化为这一类型：令 $z=ax+by$，则 $z''=by''=bf(z)$。

### 7.1.4. 只含两个相邻或相隔一阶的导数的方程

（1）$F(y^{(n-1)},y^{(n)})=0$。令 $z=y^{(n-1)}$，得一阶方程 $F(z,z')=0$：若能解出 $z'=f(z)$，它是变量分离方程，$\int\frac{\mathrm{d}z}{f(z)}=x+c_1$；不能解出时用参数法（[2.4.6](/2.4.6)）。求出 $z=\omega(x,c_1)$ 后，由 Cauchy 公式

$$
y(x)=\frac{1}{(n-2)!}\int_{x_0}^x(x-t)^{n-2}\omega(t,c_1)\,\mathrm{d}t+\sum_{k=0}^{n-2}c_{k+2}(x-x_0)^k.
$$

（2）$F(y^{(n-2)},y^{(n)})=0$。令 $z=y^{(n-2)}$，得 $F(z,z'')=0$；若能解出 $z''=f(z)$，就是能量积分的情形：$(z')^2=2\int f(z)\,\mathrm{d}z+c_1$，再分离变量得 $z=\omega(x,c_1,c_2)$，然后积分 $n-2$ 次。

**例 7.1.3** 解 $a^2y^{(4)}=y''$（$a>0$）。令 $z=y''$，$a^2z''=z$。乘以 $2z'$ 积分得 $a^2(z')^2=z^2+c_1$，分离变量 $\dfrac{\mathrm{d}z}{\sqrt{z^2+c_1}}=\pm\dfrac{\mathrm{d}x}{a}$，积分并整理得 $z=c_2\mathrm{e}^{x/a}+c_3\mathrm{e}^{-x/a}$。再积分两次：

$$
y=A\mathrm{e}^{x/a}+B\mathrm{e}^{-x/a}+Cx+D,
$$
$A,B,C,D$ 为任意常数。这个方程也是常系数线性方程，用**特征方程** $a^2\lambda^4=\lambda^2$（根 $0,0,\pm1/a$）可以直接写出同样的通解（[2.2.16](/2.2.16)）。

### 7.1.5. 关于未知函数及其导数齐次的方程

若 $F(x,ty,ty',\dots,ty^{(n)})=t^mF(x,y,y',\dots,y^{(n)})$ 对 $t\ne0$ 成立，令 $y=\mathrm{e}^{\int z\,\mathrm{d}x}$，即 $z=y'/y$，则 $y'=yz$，$y''=y(z'+z^2)$，……，每个 $y^{(k)}$ 都是 $y$ 乘以 $z,z',\dots,z^{(k-1)}$ 的多项式，提出因子 $y^m$ 后方程降低一阶。二阶齐次线性方程用这个代换化为 Riccati 方程（[2.4.3](/2.4.3)）。

**例 7.1.4** 解 $x^2yy''=(y-xy')^2$（$x>0$）。方程关于 $y,y',y''$ 是二次齐次的。令 $y'=yz$，$y''=y(z'+z^2)$，除以 $y^2$：

$$
x^2(z'+z^2)=(1-xz)^2,\qquad\text{即}\qquad x^2z'+2xz=1,\quad(x^2z)'=1.
$$
所以 $z=\dfrac1x+\dfrac{c_1}{x^2}$，$\ln\lvert y\rvert=\ln x-\dfrac{c_1}{x}+c$，通解 $y=c_2x\mathrm{e}^{-c_1/x}$（$c_2=0$ 给出解 $y=0$）。

## 7.2. 化为一阶方程组

设 $n$ 阶方程已解出最高阶导数：

$$
y^{(n)}=F\big(x,y,y',\dots,y^{(n-1)}\big). \tag{7.3}
$$
令 $y_1=y$，$y_2=y'$，……，$y_n=y^{(n-1)}$，则 (7.3) 等价于方程组

$$
y_1'=y_2,\quad y_2'=y_3,\quad\dots,\quad y_{n-1}'=y_n,\quad y_n'=F(x,y_1,\dots,y_n): \tag{7.4}
$$
若 $y$ 是 (7.3) 的解，则 $(y,y',\dots,y^{(n-1)})$ 是 (7.4) 的解；反之，若 $(y_1,\dots,y_n)$ 是 (7.4) 的解，则由前 $n-1$ 个方程 $y_k=y_1^{(k-1)}$，最后一个方程说明 $y_1$ 是 (7.3) 的解。初始条件 $y^{(k)}(x_0)=\eta_k$（$k=0,\dots,n-1$）对应 $y_{k+1}(x_0)=\eta_k$。

多个未知函数的高阶方程组也可以同样化为一阶方程组，新的未知函数的个数等于各未知函数的最高阶数之和。

**定义 7.2.1** 方程组

$$
y_i'=f_i(x,y_1,\dots,y_n),\qquad i=1,\dots,n
$$
称为**标准形式的方程组**，$n$ 称为它的阶。记列向量 $\boldsymbol{y}=(y_1,\dots,y_n)^{\mathsf T}$，$\boldsymbol{f}=(f_1,\dots,f_n)^{\mathsf T}$，它写成向量形式

$$
\boldsymbol{y}'=\boldsymbol{f}(x,\boldsymbol{y}), \tag{7.5}
$$
其初值问题为 (7.5) 连同 $\boldsymbol{y}(x_0)=\boldsymbol{\eta}$，$(x_0,\boldsymbol{\eta})\in\mathbb{R}^{n+1}$。

(7.5) 的解 $\boldsymbol{y}(x)$ 在 $\mathbb{R}^n$ 中取值，它的图形是 $\mathbb{R}^{n+1}$ 中的积分曲线；把 $x$ 看作时间，$\boldsymbol{y}(x)$ 在 $\mathbb{R}^n$ 中描出的曲线称为轨线，$\mathbb{R}^n$ 称为相空间。例 7.1.2 中单摆方程化为 $\theta'=\omega_1$，$\omega_1'=-\omega^2\sin\theta$，图中的曲线就是相平面上的轨线。

## 7.3. $\mathbb{R}^n$ 中的存在唯一性与延伸

一阶方程的理论中只用到了绝对值的几条性质。在 $\mathbb{R}^n$ 中用范数代替绝对值，全部证明都可以照搬。

**定义 7.3.1** 满足下列三条的函数 $\boldsymbol{y}\mapsto\|\boldsymbol{y}\|$ 称为 $\mathbb{R}^n$ 上的**范数**：

1. $\|\boldsymbol{y}\|\ge0$，且 $\|\boldsymbol{y}\|=0$ 当且仅当 $\boldsymbol{y}=\boldsymbol{0}$；
2. $\|\lambda\boldsymbol{y}\|=\lvert\lambda\rvert\|\boldsymbol{y}\|$（$\lambda\in\mathbb{R}$）；
3. $\|\boldsymbol{y}+\boldsymbol{z}\|\le\|\boldsymbol{y}\|+\|\boldsymbol{z}\|$（三角不等式）。

常用的范数有 Euclid 范数 $\|\boldsymbol{y}\|_2=\sqrt{y_1^2+\cdots+y_n^2}$（**长度**）、$\|\boldsymbol{y}\|_1=\lvert y_1\rvert+\cdots+\lvert y_n\rvert$ 与 $\|\boldsymbol{y}\|_\infty=\max_i\lvert y_i\rvert$，后者在估计中最方便。它们彼此等价：

$$
\|\boldsymbol{y}\|_\infty\le\|\boldsymbol{y}\|_2\le\|\boldsymbol{y}\|_1\le n\|\boldsymbol{y}\|_\infty,
$$
所以收敛、有界、Lipschitz 条件等概念与范数的选取无关（实际上 $\mathbb{R}^n$ 上任意两个范数都等价）。向量值函数的积分按分量定义，由 Riemann 和与三角不等式，

$$
\Big\|\int_{x_0}^x\boldsymbol{g}(t)\,\mathrm{d}t\Big\|\le\Big\lvert\int_{x_0}^x\|\boldsymbol{g}(t)\|\,\mathrm{d}t\Big\rvert.
$$

设 $\boldsymbol{f}$ 在 $R=\{(x,\boldsymbol{y})\mid\lvert x-x_0\rvert\le a,\ \|\boldsymbol{y}-\boldsymbol{\eta}\|\le b\}$ 上连续。若 $\|\boldsymbol{f}(x,\boldsymbol{y}_1)-\boldsymbol{f}(x,\boldsymbol{y}_2)\|\le L\|\boldsymbol{y}_1-\boldsymbol{y}_2\|$，称 $\boldsymbol{f}$ 关于 $\boldsymbol{y}$ 满足 Lipschitz 条件。若 **Jacobi 矩阵** $\dfrac{\partial\boldsymbol{f}}{\partial\boldsymbol{y}}=\Big(\dfrac{\partial f_i}{\partial y_j}\Big)$ 在 $R$ 上连续，则由

$$
\boldsymbol{f}(x,\boldsymbol{y}_1)-\boldsymbol{f}(x,\boldsymbol{y}_2)=\int_0^1\frac{\partial\boldsymbol{f}}{\partial\boldsymbol{y}}\big(x,\boldsymbol{y}_2+s(\boldsymbol{y}_1-\boldsymbol{y}_2)\big)\,\mathrm{d}s\,(\boldsymbol{y}_1-\boldsymbol{y}_2)
$$
（$R$ 关于 $\boldsymbol{y}$ 是凸的），Lipschitz 条件成立，$L$ 可取 Jacobi 矩阵的**矩阵范数**的最大值。

**定理 7.3.1** 设 $\boldsymbol{f}$ 在 $R$ 上连续，$M=\max_R\|\boldsymbol{f}\|$，$h=\min\{a,b/M\}$。

1. （Peano）初值问题 $\boldsymbol{y}'=\boldsymbol{f}(x,\boldsymbol{y})$，$\boldsymbol{y}(x_0)=\boldsymbol{\eta}$ 在 $[x_0-h,x_0+h]$ 上至少有一个解。
2. （Picard）若 $\boldsymbol{f}$ 还关于 $\boldsymbol{y}$ 满足 Lipschitz 条件，则解唯一，并且 Picard 序列 $\boldsymbol{\varphi}_{n+1}(x)=\boldsymbol{\eta}+\int_{x_0}^x\boldsymbol{f}(t,\boldsymbol{\varphi}_n(t))\,\mathrm{d}t$ 在 $[x_0-h,x_0+h]$ 上一致收敛到它。

**证明** 把定理 4.2.1 与定理 4.4.1 的证明中的 $\lvert\cdot\rvert$ 换成 $\|\cdot\|$ 即可。用到的性质只有：三角不等式、上面的积分不等式、$\mathbb{R}^n$ 中的 Weierstrass 判别法与 Cauchy 准则（逐个分量应用即可），以及 Ascoli 引理（对每个分量依次抽取子序列）。 $\square$

**定理 7.3.2** 设 $\boldsymbol{f}$ 在 $\mathbb{R}^{n+1}$ 的区域 $G$ 内连续。

1. （延伸）(7.5) 的每个解可以延伸为饱和解，最大存在区间是开区间 $(\alpha,\beta)$，$x\to\beta^-$ 时点 $(x,\boldsymbol{y}(x))$ 最终离开 $G$ 内的任何有界闭集；$x\to\alpha^+$ 时同样。若 $\boldsymbol{f}$ 还关于 $\boldsymbol{y}$ 满足局部 Lipschitz 条件，饱和解由初值唯一确定。
2. （整体存在）若 $G=(\alpha,\beta)\times\mathbb{R}^n$ 且 $\|\boldsymbol{f}(x,\boldsymbol{y})\|\le A(x)\|\boldsymbol{y}\|+B(x)$，$A,B\ge0$ 在 $(\alpha,\beta)$ 上连续，则每个饱和解的最大存在区间都是 $(\alpha,\beta)$。

**证明** 与定理 5.1.1、推论 5.1.2、定理 5.1.2 的证明相同。 $\square$

特别地，线性方程组 $\boldsymbol{y}'=A(x)\boldsymbol{y}+\boldsymbol{b}(x)$（$A,\boldsymbol{b}$ 在 $(\alpha,\beta)$ 上连续）满足 $\|\boldsymbol{f}\|\le\|A(x)\|\|\boldsymbol{y}\|+\|\boldsymbol{b}(x)\|$，它的解都在整个 $(\alpha,\beta)$ 上存在且唯一，这是 [2.4.8](/2.4.8) 的出发点。

**推论 7.3.1** 设 $F(x,u_1,\dots,u_n)$ 在 $\mathbb{R}^{n+1}$ 的区域 $G$ 内连续，且关于 $u_1,\dots,u_n$ 有连续的偏导数，则对任意 $(x_0,\eta_0,\dots,\eta_{n-1})\in G$，$n$ 阶方程 (7.3) 满足 $y^{(k)}(x_0)=\eta_k$（$k=0,\dots,n-1$）的解在 $x_0$ 附近存在且唯一，并可延伸到 $G$ 的边界。

**证明** 对等价的方程组 (7.4) 应用定理 7.3.1 与定理 7.3.2：它的右端 $(y_2,\dots,y_n,F)^{\mathsf T}$ 的 Jacobi 矩阵连续。 $\square$

## 7.4. 解对初值和参数的依赖性

初值和方程中的参数往往来自测量，只是近似值。如果初值的微小变化可以引起解的巨大变化，方程就失去了预测能力。本节证明：在 Lipschitz 条件下，解在有限区间上连续地依赖于初值和参数；右端光滑时解还是可微的。

记 (7.5) 满足 $\boldsymbol{y}(x_0)=\boldsymbol{\eta}$ 的解为 $\boldsymbol{y}=\boldsymbol{\varphi}(x;x_0,\boldsymbol{\eta})$。方程含参数 $\boldsymbol{\lambda}\in\Lambda\subset\mathbb{R}^m$ 时写作 $\boldsymbol{y}'=\boldsymbol{f}(x,\boldsymbol{y},\boldsymbol{\lambda})$，解记为 $\boldsymbol{\varphi}(x;x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$。

### 7.4.1. Gronwall 不等式

**引理 7.4.1（Gronwall 不等式）** 设 $u(x)$ 与 $L(x)$ 在 $[x_0,x_1]$ 上连续且非负，$K\ge0$ 为常数。若

$$
u(x)\le K+\int_{x_0}^xL(t)u(t)\,\mathrm{d}t,\qquad x_0\le x\le x_1,
$$
则

$$
u(x)\le K\exp\Big(\int_{x_0}^xL(t)\,\mathrm{d}t\Big),\qquad x_0\le x\le x_1.
$$

**证明** 令 $v(x)=K+\int_{x_0}^xL(t)u(t)\,\mathrm{d}t$，则 $u\le v$，$v'=Lu\le Lv$。记 $\Lambda(x)=\int_{x_0}^xL$，则 $\big(v\mathrm{e}^{-\Lambda}\big)'=(v'-Lv)\mathrm{e}^{-\Lambda}\le0$，所以 $v(x)\mathrm{e}^{-\Lambda(x)}\le v(x_0)=K$，$u\le v\le K\mathrm{e}^{\Lambda}$。 $\square$

$x<x_0$ 时有对称的形式：$u(x)\le K+\Big\lvert\int_{x_0}^xLu\,\mathrm{d}t\Big\rvert$ 蕴含 $u(x)\le K\exp\Big\lvert\int_{x_0}^xL\,\mathrm{d}t\Big\rvert$。取 $K=0$ 得 $u\equiv0$：这又一次证明了 Lipschitz 条件下的唯一性（对两个解之差的范数应用）。定理 5.1.2 的证明中用到的正是这个论证。

**定理 7.4.1（解的误差估计）** 设 $\boldsymbol{f},\boldsymbol{g}$ 在区域 $G\subset\mathbb{R}^{n+1}$ 内连续，$\boldsymbol{f}$ 关于 $\boldsymbol{y}$ 满足 Lipschitz 条件（常数 $L$），且在 $G$ 内 $\|\boldsymbol{f}-\boldsymbol{g}\|\le\varepsilon$。设 $\boldsymbol{\varphi}$、$\boldsymbol{\psi}$ 在区间 $J\ni x_0$ 上分别是 $\boldsymbol{y}'=\boldsymbol{f}(x,\boldsymbol{y})$ 与 $\boldsymbol{y}'=\boldsymbol{g}(x,\boldsymbol{y})$ 的解，$\boldsymbol{\varphi}(x_0)=\boldsymbol{\eta}$，$\boldsymbol{\psi}(x_0)=\boldsymbol{\zeta}$，则对 $x\in J$，

$$
\|\boldsymbol{\varphi}(x)-\boldsymbol{\psi}(x)\|\le\big(\|\boldsymbol{\eta}-\boldsymbol{\zeta}\|+\varepsilon\lvert x-x_0\rvert\big)\mathrm{e}^{L\lvert x-x_0\rvert}.
$$

**证明** 设 $x>x_0$。由积分方程，

$$
\boldsymbol{\varphi}(s)-\boldsymbol{\psi}(s)=\boldsymbol{\eta}-\boldsymbol{\zeta}+\int_{x_0}^s\Big(\big(\boldsymbol{f}(t,\boldsymbol{\varphi})-\boldsymbol{f}(t,\boldsymbol{\psi})\big)+\big(\boldsymbol{f}(t,\boldsymbol{\psi})-\boldsymbol{g}(t,\boldsymbol{\psi})\big)\Big)\,\mathrm{d}t,
$$
所以 $u(s)=\|\boldsymbol{\varphi}(s)-\boldsymbol{\psi}(s)\|$ 在 $[x_0,x]$ 上满足 $u(s)\le\|\boldsymbol{\eta}-\boldsymbol{\zeta}\|+\varepsilon(x-x_0)+\int_{x_0}^sLu\,\mathrm{d}t$。由 Gronwall 不等式（常数 $K=\|\boldsymbol{\eta}-\boldsymbol{\zeta}\|+\varepsilon(x-x_0)$），在 $s=x$ 处即得结论。$x<x_0$ 同理。 $\square$

估计中的因子 $\mathrm{e}^{L\lvert x-x_0\rvert}$ 说明：初值的误差在有限区间上是可控的，但随区间长度可能指数增长。在混沌系统中这种指数增长确实发生，长期预测因而不可能；有限区间上的连续依赖性并不与此矛盾。

![y' = y - y^3 从 y(0) = 0.01 与 y(0) = 0.011 出发的两个解之差（对数纵轴）：在不稳定平衡点 y = 0 附近差按 e^x 增长，始终低于 Gronwall 界 0.001 e^{2x}（L = max |1 - 3y^2| = 2），两个解都趋于 y = 1 后差又衰减](./plots/initial-value-sensitivity.py)

### 7.4.2. 连续依赖性

**定理 7.4.2（解对初值和参数的连续依赖性）** 设 $\boldsymbol{f}(x,\boldsymbol{y},\boldsymbol{\lambda})$ 在 $G\times\Lambda$ 上连续（$G\subset\mathbb{R}^{n+1}$ 为区域，$\Lambda\subset\mathbb{R}^m$ 为开集），且关于 $\boldsymbol{y}$ 满足局部 Lipschitz 条件。设 $\boldsymbol{\varphi}(x;x_0^*,\boldsymbol{\eta}^*,\boldsymbol{\lambda}^*)$ 在有界闭区间 $[a,b]\ni x_0^*$ 上存在。则存在 $\delta>0$，当

$$
\lvert x_0-x_0^*\rvert+\|\boldsymbol{\eta}-\boldsymbol{\eta}^*\|+\|\boldsymbol{\lambda}-\boldsymbol{\lambda}^*\|<\delta
$$
时，饱和解 $\boldsymbol{\varphi}(x;x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$ 在 $[a,b]$ 上存在，并且 $\boldsymbol{\varphi}$ 作为 $(x,x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$ 的函数在这个集合上连续。

证明思路：取 $\boldsymbol{\varphi}^*=\boldsymbol{\varphi}(x;x_0^*,\boldsymbol{\eta}^*,\boldsymbol{\lambda}^*)$ 的图形的一个管状邻域 $K=\{(x,\boldsymbol{y})\mid a\le x\le b,\ \|\boldsymbol{y}-\boldsymbol{\varphi}^*(x)\|\le d\}\subset G$，它是有界闭集，$\boldsymbol{f}$ 在 $K\times\bar B(\boldsymbol{\lambda}^*,r)$ 上有界（界为 $M$）、关于 $\boldsymbol{y}$ 满足 Lipschitz 条件（常数 $L$，由局部 Lipschitz 条件与紧性得到），并且关于 $\boldsymbol{\lambda}$ 一致连续，所以 $\|\boldsymbol{\lambda}-\boldsymbol{\lambda}^*\|$ 小时 $\|\boldsymbol{f}(\cdot,\cdot,\boldsymbol{\lambda})-\boldsymbol{f}(\cdot,\cdot,\boldsymbol{\lambda}^*)\|\le\varepsilon$ 在 $K$ 上成立。新解在 $x_0^*$ 处的值与 $\boldsymbol{\eta}^*$ 相差不超过 $\|\boldsymbol{\eta}-\boldsymbol{\eta}^*\|+M\lvert x_0-x_0^*\rvert$。由定理 7.4.1，只要它留在 $K$ 中，就有

$$
\|\boldsymbol{\varphi}(x;x_0,\boldsymbol{\eta},\boldsymbol{\lambda})-\boldsymbol{\varphi}^*(x)\|\le\big(\|\boldsymbol{\eta}-\boldsymbol{\eta}^*\|+M\lvert x_0-x_0^*\rvert+\varepsilon(b-a)\big)\mathrm{e}^{L(b-a)}.
$$
$\delta$ 取得足够小时右端小于 $d/2$，由延伸定理，新解在到达 $x=b$（或 $x=a$）之前不能离开 $K$，所以它在整个 $[a,b]$ 上存在，并且上式说明它一致地接近 $\boldsymbol{\varphi}^*$。对 $(x,x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$ 的联合连续性，再加上 $\|\boldsymbol{\varphi}(x)-\boldsymbol{\varphi}(x')\|\le M\lvert x-x'\rvert$ 即可。

去掉 Lipschitz 条件（没有唯一性）时，"解"不再是初值的函数，结论需要改写为解集的连续性，这里不讨论。

### 7.4.3. 可微性与变分方程

**定理 7.4.3（解对初值和参数的可微性）** 设 $\boldsymbol{f}(x,\boldsymbol{y},\boldsymbol{\lambda})$ 及其偏导数 $\dfrac{\partial\boldsymbol{f}}{\partial\boldsymbol{y}}$、$\dfrac{\partial\boldsymbol{f}}{\partial\boldsymbol{\lambda}}$ 在 $G\times\Lambda$ 上连续，则 $\boldsymbol{\varphi}(x;x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$ 在其定义域上连续可微，并且沿解 $\boldsymbol{\varphi}(x)=\boldsymbol{\varphi}(x;x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$，记 $A(x)=\dfrac{\partial\boldsymbol{f}}{\partial\boldsymbol{y}}\big(x,\boldsymbol{\varphi}(x),\boldsymbol{\lambda}\big)$：

1. $n\times n$ 矩阵 $Y(x)=\dfrac{\partial\boldsymbol{\varphi}}{\partial\boldsymbol{\eta}}$ 是线性方程组初值问题

$$
Y'=A(x)Y,\qquad Y(x_0)=I_n \tag{7.6}
$$
的解；
2. $\dfrac{\partial\boldsymbol{\varphi}}{\partial x_0}=-Y(x)\,\boldsymbol{f}(x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$；
3. $n\times m$ 矩阵 $Z(x)=\dfrac{\partial\boldsymbol{\varphi}}{\partial\boldsymbol{\lambda}}$ 是 $Z'=A(x)Z+\dfrac{\partial\boldsymbol{f}}{\partial\boldsymbol{\lambda}}\big(x,\boldsymbol{\varphi}(x),\boldsymbol{\lambda}\big)$，$Z(x_0)=O$ 的解。

**定义 7.4.1** 线性方程组 (7.6) 称为方程 (7.5) 沿解 $\boldsymbol{\varphi}$ 的**变分方程**。

变分方程是把方程在已知解附近线性化的结果：若 $\boldsymbol{\varphi}+\boldsymbol{\xi}$ 是邻近的解，则 $\boldsymbol{\xi}'=\boldsymbol{f}(x,\boldsymbol{\varphi}+\boldsymbol{\xi})-\boldsymbol{f}(x,\boldsymbol{\varphi})=A(x)\boldsymbol{\xi}+o(\|\boldsymbol{\xi}\|)$，略去高阶项就得到 $\boldsymbol{\xi}'=A(x)\boldsymbol{\xi}$。$Y(x)$ 是它的**基解矩阵**，$\boldsymbol{\xi}(x)\approx Y(x)\,\delta\boldsymbol{\eta}$ 给出了初值扰动 $\delta\boldsymbol{\eta}$ 的一阶效应。

证明思路：形式上，对积分方程 $\boldsymbol{\varphi}(x)=\boldsymbol{\eta}+\int_{x_0}^x\boldsymbol{f}(t,\boldsymbol{\varphi}(t),\boldsymbol{\lambda})\,\mathrm{d}t$ 关于 $\boldsymbol{\eta}$ 求导，得 $Y=I_n+\int_{x_0}^xA(t)Y\,\mathrm{d}t$，即 (7.6)；关于 $x_0$ 求导得 $\dfrac{\partial\boldsymbol{\varphi}}{\partial x_0}=-\boldsymbol{f}(x_0,\boldsymbol{\eta},\boldsymbol{\lambda})+\int_{x_0}^xA\dfrac{\partial\boldsymbol{\varphi}}{\partial x_0}\,\mathrm{d}t$，它满足同一个线性方程，初值为 $-\boldsymbol{f}(x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$，所以等于 $-Y(x)\boldsymbol{f}(x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$；关于 $\boldsymbol{\lambda}$ 求导同理。严格地，考虑差商 $\boldsymbol{q}_h(x)=\dfrac1h\big(\boldsymbol{\varphi}(x;x_0,\boldsymbol{\eta}+h\boldsymbol{e}_j,\boldsymbol{\lambda})-\boldsymbol{\varphi}(x;x_0,\boldsymbol{\eta},\boldsymbol{\lambda})\big)$，由积分形式的中值公式它满足线性方程

$$
\boldsymbol{q}_h'=A_h(x)\boldsymbol{q}_h,\qquad\boldsymbol{q}_h(x_0)=\boldsymbol{e}_j,\qquad A_h(x)=\int_0^1\frac{\partial\boldsymbol{f}}{\partial\boldsymbol{y}}\big(x,\boldsymbol{\varphi}+s(\boldsymbol{\varphi}_h-\boldsymbol{\varphi}),\boldsymbol{\lambda}\big)\,\mathrm{d}s.
$$
由连续依赖性（定理 7.4.2），$h\to0$ 时 $A_h\to A$ 一致成立；再对这个线性方程用定理 7.4.1，得 $\boldsymbol{q}_h$ 一致收敛到 (7.6) 的解的第 $j$ 列。偏导数的连续性由定理 7.4.2 应用于原方程与变分方程联立的方程组得到。

含参数的情形也可以化为初值的情形：把 $\boldsymbol{\lambda}$ 看作新的未知函数，补充方程 $\boldsymbol{\lambda}'=\boldsymbol{0}$、初值 $\boldsymbol{\lambda}(x_0)=\boldsymbol{\lambda}$，参数就变成了扩大的方程组的初值。若 $\boldsymbol{f}$ 是 $C^k$ 的，对变分方程反复应用定理 7.4.3 可知 $\boldsymbol{\varphi}$ 也是 $C^k$ 的。

**例 7.4.1** $y'=y^2$，$y(0)=\eta$ 的解为 $\varphi(x;\eta)=\dfrac{\eta}{1-\eta x}$，直接求导得 $\dfrac{\partial\varphi}{\partial\eta}=\dfrac{1}{(1-\eta x)^2}$。用变分方程：$A(x)=2\varphi(x)=\dfrac{2\eta}{1-\eta x}$，$Y'=A(x)Y$，$Y(0)=1$ 的解为

$$
Y(x)=\exp\int_0^x\frac{2\eta}{1-\eta t}\,\mathrm{d}t=\exp\big(-2\ln(1-\eta x)\big)=\frac{1}{(1-\eta x)^2},
$$
两者一致。又 $\dfrac{\partial\varphi}{\partial x_0}$ 在 $x_0=0$ 处应为 $-Y(x)\eta^2=-\dfrac{\eta^2}{(1-\eta x)^2}$：确实，$y(x_0)=\eta$ 的解为 $\dfrac{\eta}{1-\eta(x-x_0)}$，对 $x_0$ 求导并令 $x_0=0$ 即得。

**例 7.4.2** 含参数的方程 $y'=\lambda y$，$y(0)=\eta$：$\varphi=\eta\mathrm{e}^{\lambda x}$。$Z=\dfrac{\partial\varphi}{\partial\lambda}$ 满足 $Z'=\lambda Z+\varphi=\lambda Z+\eta\mathrm{e}^{\lambda x}$，$Z(0)=0$，解得 $Z=\eta x\mathrm{e}^{\lambda x}$，与直接求导一致。增长率 $\lambda$ 的测量误差对解的影响随 $x$ 线性放大（相对误差 $x\,\delta\lambda$）。

## 小结

| 内容 | 要点 |
|---|---|
| 降阶 | Cauchy 公式 (7.1)；不含 $y$ 时令 $z=y^{(k)}$；不含 $x$ 时令 $y'=z(y)$；$y''=f(y)$ 的能量积分 (7.2)；齐次方程令 $y'=yz$ |
| 方程组 | $n$ 阶方程等价于 $n$ 个一阶方程的标准形式方程组 (7.4) |
| 存在唯一与延伸 | 用范数代替绝对值，Picard、Peano、延伸定理逐字成立；线性增长时整体存在 |
| 连续依赖 | Gronwall 不等式：误差不超过 $(\Vert\delta\boldsymbol{\eta}\Vert+\varepsilon\lvert x-x_0\rvert)\mathrm{e}^{L\lvert x-x_0\rvert}$ |
| 可微性 | $\partial\boldsymbol{\varphi}/\partial\boldsymbol{\eta}$ 满足变分方程 $Y'=\frac{\partial\boldsymbol{f}}{\partial\boldsymbol{y}}Y$，$Y(x_0)=I_n$ |
