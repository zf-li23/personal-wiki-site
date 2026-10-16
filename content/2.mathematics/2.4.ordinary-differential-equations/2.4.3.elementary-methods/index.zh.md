---
title: 变量分离、线性方程与初等变换
---

本章讨论能用初等积分法求解的几类一阶方程，以及与它们相关的理论问题。变量分离方程与一阶线性方程是最基本的两类：前者的解可以通过反函数严格写出，并且只在右端为零处可能失去唯一性；后者的解有显式公式，由此可以完整地回答周期解与有界解的存在性问题。齐次型方程、Bernoulli 方程与 Riccati 方程则通过变量代换化为前两类；Riccati 方程是最简单的非线性方程之一，它与二阶线性方程等价，一般不能用求积法求解。最后一节用这些方法求曲线族的等角轨线与正交轨线。

例行解法与例题已在微积分 [2.2.15](/2.2.15) 中给出（变量分离与可化为变量分离的方程见 [15.2 节](/2.2.15#sec-15.2)，一阶线性方程与 Bernoulli 方程见 [15.3 节](/2.2.15#sec-15.3)），这里从简，侧重证明与专题。所有这些方程都可以看作上一章恰当方程的特例：变量分离方程有积分因子 $\dfrac{1}{X_1(x)Y_1(y)}$（例 2.3.2），一阶线性方程有积分因子 $\mathrm{e}^{\int p\,\mathrm{d}x}$（例 2.3.1）。

## 3.1. 变量分离方程

**定义 3.1.1** 形如

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=f(x)g(y)\tag{3.1}
$$
的方程，或对称形式 $X(x)Y_1(y)\,\mathrm{d}x+X_1(x)Y(y)\,\mathrm{d}y=0$ 的方程，称为**变量分离方程**。

**定理 3.1.1** 设 $f$ 在区间 $I$ 上连续，$g$ 在开区间 $J$ 上连续，$x_0\in I$，$y_0\in J$，$g(y_0)\ne0$。则初值问题 (3.1)、$y(x_0)=y_0$ 在 $x_0$ 的某邻域内有唯一解，它由

$$
\int_{y_0}^y\frac{\mathrm{d}s}{g(s)}=\int_{x_0}^xf(t)\,\mathrm{d}t\tag{3.2}
$$
确定。

**证明** 设 $J_0\subset J$ 是包含 $y_0$、其上 $g\ne0$ 的最大开区间。$g$ 在 $J_0$ 上不变号，所以 $G(y)=\displaystyle\int_{y_0}^y\frac{\mathrm{d}s}{g(s)}$ 在 $J_0$ 上连续可微且严格单调，$G(y_0)=0$，它把 $J_0$ 映为包含 $0$ 的开区间 $G(J_0)$，有连续可微的反函数 $G^{-1}$。记 $F(x)=\int_{x_0}^xf(t)\,\mathrm{d}t$，它连续且 $F(x_0)=0$，所以在 $x_0$ 的某邻域 $I_0$ 内 $F(x)\in G(J_0)$。

存在性：令 $\varphi=G^{-1}\circ F$，则 $G(\varphi(x))=F(x)$，两边求导得 $\dfrac{\varphi'(x)}{g(\varphi(x))}=f(x)$，即 $\varphi$ 是解，且 $\varphi(x_0)=G^{-1}(0)=y_0$。

唯一性：设 $\psi$ 是另一个满足 $\psi(x_0)=y_0$ 的解。由连续性，在 $x_0$ 附近 $\psi(x)\in J_0$，于是 $\dfrac{\mathrm{d}}{\mathrm{d}x}G(\psi(x))=\dfrac{\psi'(x)}{g(\psi(x))}=f(x)$，$G(\psi(x))=F(x)$，即 $\psi=G^{-1}\circ F=\varphi$。 $\square$

因此变量分离方程的唯一性只可能在直线 $y=c$（$g(c)=0$）上失去，而 $y\equiv c$ 本身总是解。分离变量求通解时除以 $g(y)$，会丢失这些解，必须单独检查（[2.2.15 例 15.2.1](/2.2.15#ex-15.2.1)）。

**注 3.1.1** 设 $g(c)=0$，且 $g$ 在 $c$ 的右侧附近为正。由式 (3.2)，从 $y>c$ 出发的解要在有限的 $x$ 处到达 $c$，需要 $\displaystyle\int_c^{c+\varepsilon}\frac{\mathrm{d}s}{g(s)}<+\infty$。所以：

- 若这个积分发散（例如 $g$ 在 $c$ 附近满足 **Lipschitz 条件**，$\lvert g(s)\rvert\le L\lvert s-c\rvert$，或 $g(s)=(s-c)\lvert\ln(s-c)\rvert$），其他解不会与 $y=c$ 相交，过 $y=c$ 上各点的解唯一；
- 若积分收敛（例如 $g(y)=3y^{2/3}$，$c=0$），解可以在有限处到达 $y=c$，沿它走一段再离开，唯一性失去（[2.2.15 例 15.1.5](/2.2.15#ex-15.1.5)）。

这一判别正是 [2.4.4](/2.4.4) 中 Osgood 唯一性定理的原型。

## 3.2. 一阶线性方程

### 3.2.1. 求解公式

一阶线性方程的标准形式是

$$
y'+p(x)y=q(x),\tag{3.3}
$$
$q\equiv0$ 时称为齐次线性方程。求解公式的推导（积分因子或**常数变易公式**）见 [2.2.15 定理 15.3.1](/2.2.15#thm-15.3.1)，这里给出初值问题的形式。

**定理 3.2.1** 设 $p,q$ 在区间 $I$ 上连续，$x_0\in I$。则对任意 $y_0$，方程 (3.3) 满足 $y(x_0)=y_0$ 的解在整个区间 $I$ 上存在且唯一，为

$$
y(x)=y_0\mathrm{e}^{-\int_{x_0}^xp(t)\,\mathrm{d}t}+\int_{x_0}^xq(s)\mathrm{e}^{-\int_s^xp(t)\,\mathrm{d}t}\,\mathrm{d}s.\tag{3.4}
$$

**证明** 令 $\mu(x)=\mathrm{e}^{\int_{x_0}^xp(t)\,\mathrm{d}t}$，则 $\mu'=p\mu$，$\mu>0$。对 $I$ 的任一子区间上的任一解 $y$，

$$
(\mu y)'=\mu(y'+py)=\mu q.
$$
从 $x_0$ 到 $x$ 积分得 $\mu(x)y(x)-y_0=\int_{x_0}^x\mu(s)q(s)\,\mathrm{d}s$，除以 $\mu(x)$ 即得式 (3.4)；所以解若存在必由 (3.4) 给出，唯一性成立。反之，式 (3.4) 右端在整个 $I$ 上有定义，直接验证它满足方程与初始条件。 $\square$

### 3.2.2. 解的性质

**命题 3.2.1** 设 $p,q$ 在区间 $I$ 上连续。

1. 方程 (3.3) 的每个解都可以延伸到整个区间 $I$ 上（整体存在）。
2. 齐次方程 $y'+p(x)y=0$ 的解或者恒为零，或者处处不为零。
3. 齐次方程的解的全体是一维线性空间 $\big\{C\mathrm{e}^{-\int_{x_0}^xp}\mid C\in\mathbb{R}\big\}$；方程 (3.3) 的解的全体是 $y^*+\big\{C\mathrm{e}^{-\int_{x_0}^xp}\big\}$，其中 $y^*$ 是任一特解。特别地，通解包含全部解。
4. （**叠加原理**）若 $y_k$ 是 $y'+py=q_k$ 的解（$k=1,2$），则 $\alpha y_1+\beta y_2$ 是 $y'+py=\alpha q_1+\beta q_2$ 的解。

**证明** 1 与 3 由定理 3.2.1 直接得到（式 (3.4) 关于 $y_0$ 是仿射的）。2：齐次方程的解为 $y_0\mathrm{e}^{-\int_{x_0}^xp}$，指数因子处处为正。4：算子 $L(y)=y'+py$ 是线性的。 $\square$

性质 1 是线性方程区别于非线性方程的重要特征：$y'=y^2$ 的右端在整个平面上光滑，它的解 $\dfrac{1}{C-x}$ 却在有限处趋于无穷。非线性方程的解能延伸多远是 [2.4.5](/2.4.5) 的问题。

**命题 3.2.2** 设 $u_1,u_2,u_3$ 是方程 (3.3) 在区间 $I$ 上的三个互不相同的解，则

$$
\frac{u_1(x)-u_3(x)}{u_2(x)-u_3(x)}\equiv C\quad(\text{常数}).
$$

**证明** $u_1-u_3$ 与 $u_2-u_3$ 都是齐次方程的解，由命题 3.2.1 的 3，$u_k-u_3=C_k\mathrm{e}^{-\int_{x_0}^xp}$（$k=1,2$），且 $C_2\ne0$（$u_2\ne u_3$），由 2 知 $u_2-u_3$ 处处不为零。比值等于 $C_1/C_2$。 $\square$

几何上，命题 3.2.2 说的是：一阶线性方程的任意三条积分曲线在每条竖直线上截出的线段之比不变。下一节的 Riccati 方程有类似的、关于四个解的结论。

## 3.3. 周期解与有界解

本节考虑定义在整个实轴上的方程

$$
y'+p(x)y=q(x),\qquad x\in\mathbb{R},\tag{3.5}
$$
$p,q$ 连续。记 $P(x)=\int_0^xp(t)\,\mathrm{d}t$，由式 (3.4)，满足 $y(0)=y_0$ 的解为

$$
y(x)=\mathrm{e}^{-P(x)}\Big(y_0+\int_0^xq(s)\mathrm{e}^{P(s)}\,\mathrm{d}s\Big).\tag{3.6}
$$

### 3.3.1. 有界解

**命题 3.3.1** 设 $p(x)\equiv\alpha>0$ 是常数，$q$ 在 $\mathbb{R}$ 上连续且有界，$\lvert q\rvert\le M$。则方程 (3.5) 有唯一的在 $\mathbb{R}$ 上有界的解

$$
y^*(x)=\int_{-\infty}^xq(s)\mathrm{e}^{-\alpha(x-s)}\,\mathrm{d}s,\qquad\lvert y^*(x)\rvert\le\frac M\alpha,\tag{3.7}
$$
并且任一解 $y$ 满足 $y(x)-y^*(x)\to0$（$x\to+\infty$）。

**证明** 因为 $\lvert q(s)\mathrm{e}^{-\alpha(x-s)}\rvert\le M\mathrm{e}^{-\alpha(x-s)}$，积分 (3.7) 收敛，且

$$
\lvert y^*(x)\rvert\le\int_{-\infty}^xM\mathrm{e}^{-\alpha(x-s)}\,\mathrm{d}s=\frac M\alpha.
$$
写成 $y^*(x)=\mathrm{e}^{-\alpha x}\int_{-\infty}^xq(s)\mathrm{e}^{\alpha s}\,\mathrm{d}s$ 求导，得 $y^{*\prime}=-\alpha y^*+q$，所以 $y^*$ 是有界解；它就是式 (3.6) 中取 $y_0=\int_{-\infty}^0q(s)\mathrm{e}^{\alpha s}\,\mathrm{d}s$ 的解。由命题 3.2.1，任一解是 $y=y^*+C\mathrm{e}^{-\alpha x}$。$C\ne0$ 时 $\lvert C\mathrm{e}^{-\alpha x}\rvert\to+\infty$（$x\to-\infty$），解无界；所以有界解唯一。又 $C\mathrm{e}^{-\alpha x}\to0$（$x\to+\infty$），所有解都趋近于 $y^*$。 $\square$

$\alpha>0$ 意味着系统有"阻尼"：初值的影响 $C\mathrm{e}^{-\alpha x}$ 随时间衰减，长时间后只剩下由外力 $q$ 决定的响应 $y^*$。式 (3.7) 中 $y^*(x)$ 是过去全部外力 $q(s)$（$s\le x$）以权 $\mathrm{e}^{-\alpha(x-s)}$ 加权的累积，越久远的外力权重越小。

### 3.3.2. 周期解

**定义 3.3.1** 设 $T>0$。若方程的解 $y(x)$ 在 $\mathbb{R}$ 上有定义且 $y(x+T)\equiv y(x)$，则称 $y$ 为方程的 $T$ **周期解**。

**命题 3.3.2** 设 $p,q$ 是以 $T$ 为周期的连续函数。

1. 若 $y(x)$ 是方程 (3.5) 的解，则 $y(x+T)$ 也是它的解；
2. 解 $y$ 是 $T$ 周期解，当且仅当 $y(T)=y(0)$。

**证明** 1：$y'(x+T)+p(x)y(x+T)=y'(x+T)+p(x+T)y(x+T)=q(x+T)=q(x)$。2：必要性显然。充分性：$z(x)=y(x+T)-y(x)$ 是齐次方程 $z'+p(x)z=0$ 的解且 $z(0)=0$，由命题 3.2.1 的 2，$z\equiv0$。 $\square$

所以周期解的问题化为一个关于初值 $y_0=y(0)$ 的代数方程。由式 (3.6)，$y(T)=y(0)$ 即

$$
y_0\big(\mathrm{e}^{P(T)}-1\big)=\int_0^Tq(s)\mathrm{e}^{P(s)}\,\mathrm{d}s.\tag{3.8}
$$

**定理 3.3.1** 设 $p,q$ 是以 $T$ 为周期的连续函数，$\displaystyle\bar p=\frac1T\int_0^Tp(x)\,\mathrm{d}x$ 为 $p$ 的平均值。

1. 齐次方程 $y'+p(x)y=0$ 有非零 $T$ 周期解，当且仅当 $\bar p=0$；此时它的所有解都是 $T$ 周期的。
2. 若 $\bar p\ne0$，方程 (3.5) 有唯一的 $T$ 周期解，它是式 (3.6) 中取

$$
y_0=\frac{\int_0^Tq(s)\mathrm{e}^{P(s)}\,\mathrm{d}s}{\mathrm{e}^{P(T)}-1}
$$
的解。
3. 若 $\bar p=0$，则当 $\displaystyle\int_0^Tq(s)\mathrm{e}^{P(s)}\,\mathrm{d}s=0$ 时方程 (3.5) 的所有解都是 $T$ 周期的，否则方程 (3.5) 没有 $T$ 周期解。

**证明** $P(T)=T\bar p$。1：$q=0$ 时式 (3.8) 为 $y_0(\mathrm{e}^{P(T)}-1)=0$，有非零解 $y_0$ 当且仅当 $P(T)=0$，此时它对一切 $y_0$ 成立。2：$P(T)\ne0$ 时式 (3.8) 唯一地解出 $y_0$。3：$P(T)=0$ 时式 (3.8) 左端为零，它对一切 $y_0$ 成立或对任何 $y_0$ 都不成立，取决于右端是否为零。各情形由命题 3.3.2 的 2 转化为周期解的结论。 $\square$

结论 2 的唯一性也可以这样看：两个 $T$ 周期解之差是齐次方程的 $T$ 周期解，$\bar p\ne0$ 时它只能是零。

**推论 3.3.1** 设 $p\equiv\alpha>0$，$q$ 是以 $T$ 为周期的连续函数，则命题 3.3.1 中的有界解 (3.7) 就是方程 (3.5) 唯一的 $T$ 周期解。

**证明** 唯一性由定理 3.3.1 的 2 得到。周期性：在式 (3.7) 中作代换 $s=t+T$，

$$
y^*(x+T)=\int_{-\infty}^{x+T}q(s)\mathrm{e}^{-\alpha(x+T-s)}\,\mathrm{d}s=\int_{-\infty}^xq(t+T)\mathrm{e}^{-\alpha(x-t)}\,\mathrm{d}t=y^*(x).\qquad\square
$$

**例 3.3.1** $y'+y=\sin x$。这里 $\alpha=1$，周期解为

$$
y^*(x)=\int_{-\infty}^x\sin s\,\mathrm{e}^{-(x-s)}\,\mathrm{d}s=\frac{\sin x-\cos x}{2}=\frac{1}{\sqrt2}\sin\Big(x-\frac\pi4\Big),
$$
通解为 $y=y^*+C\mathrm{e}^{-x}$。所有解都以指数速度趋于这个周期解：它的振幅是外力振幅的 $1/\sqrt2$，相位落后 $\pi/4$。

![y' + y = sin x 的若干个解（细线，初值 y(0) 取 -3 到 3）都以速率 e^{-x} 趋于唯一的周期解 y* = (sin x - cos x)/2（粗线）；向左看，除 y* 外的解都以指数速度发散](./plots/periodic-solution.py)

## 3.4. 齐次型方程与 Bernoulli 方程

以下两类方程通过换未知函数化为前两节的类型。解法与例题见 [2.2.15 算法 15.2.2](/2.2.15#alg-15.2.2) 与 [算法 15.3.2](/2.2.15#alg-15.3.2)。

齐次型方程 $y'=f\Big(\dfrac yx\Big)$：令 $y=xu$，得变量分离方程 $xu'=f(u)-u$。$f(u_0)=u_0$ 的根给出解 $y=u_0x$，它们是分离变量时丢失的解；由定理 3.1.1，在 $f(u)\ne u$ 处解唯一。方程在相似变换 $(x,y)\mapsto(\lambda x,\lambda y)$ 下不变，所以把一条积分曲线以原点为中心放缩，得到的仍是积分曲线；这正是用 $u=y/x$ 降低复杂度的原因。

**Bernoulli 方程** $y'+p(x)y=q(x)y^n$（$n\ne0,1$）：在 $y\ne0$ 处两边乘以 $(1-n)y^{-n}$，令 $z=y^{1-n}$，得线性方程

$$
z'+(1-n)p(x)z=(1-n)q(x).
$$
求出 $z$ 后 $y=z^{1/(1-n)}$（$y^{1-n}$ 只对 $y>0$ 有定义时，在 $y>0$ 的区域内求解）。$n>0$ 时 $y\equiv0$ 也是解。当 $0<n<1$ 时，$y^n$ 在 $y=0$ 处不满足 Lipschitz 条件，由注 3.1.1 的同样分析，解可以在有限处到达 $y=0$，唯一性可能失去：例如 $y'=y^{1/2}$ 有解 $y\equiv0$ 与 $y=\dfrac{(x-c)^2}{4}$（$x\ge c$，此前为零）。

## 3.5. Riccati 方程

### 3.5.1. 定义与初等变换

**定义 3.5.1** 形如

$$
y'=p(x)y^2+q(x)y+r(x)\tag{3.9}
$$
的方程称为 **Riccati 方程**，其中 $p,q,r$ 在区间 $I$ 上连续，$p\not\equiv0$。

右端是 $y$ 的二次多项式，所以 Riccati 方程是"仅次于线性"的最简单的非线性方程。$r\equiv0$ 时它是 Bernoulli 方程（$n=2$）。右端关于 $y$ 连续可微，满足局部 Lipschitz 条件，所以过每一点的解唯一（[2.4.4](/2.4.4)），不同的解互不相交；但解一般不能延伸到整个 $I$（如 $y'=y^2$）。

**命题 3.5.1** 令 $Q(x)=\mathrm{e}^{\int_{x_0}^xq(t)\,\mathrm{d}t}$，$y=Q(x)z$，则方程 (3.9) 化为

$$
z'=p(x)Q(x)z^2+\frac{r(x)}{Q(x)}.
$$
所以总可以设 $q\equiv0$。

**证明** $Q'=qQ$，$y'=qQz+Qz'$，代入 (3.9)：$qQz+Qz'=pQ^2z^2+qQz+r$，即 $Qz'=pQ^2z^2+r$。 $\square$

### 3.5.2. 已知特解时的求解

**定理 3.5.1** 设 $y=\varphi(x)$ 是方程 (3.9) 的一个解。则代换 $y=\varphi(x)+\dfrac{1}{u}$ 把方程 (3.9) 化为一阶线性方程

$$
u'+\big(2p(x)\varphi(x)+q(x)\big)u+p(x)=0.\tag{3.10}
$$
因此方程 (3.9) 的其余解都是 $y=\varphi+\dfrac1u$，$u$ 取遍式 (3.10) 的解（在 $u\ne0$ 的区间上）。

**证明** 令 $z=y-\varphi$，则

$$
z'=p(y^2-\varphi^2)+q(y-\varphi)=p\big((z+\varphi)^2-\varphi^2\big)+qz=pz^2+(2p\varphi+q)z,
$$
这是 $n=2$ 的 Bernoulli 方程。由于解互不相交，$y\ne\varphi$ 时 $z$ 处处不为零，令 $u=1/z$，$u'=-z'/z^2=-p-(2p\varphi+q)u$，即式 (3.10)。 $\square$

所以知道一个特解，再做两次求积（解线性方程）就得到通解。知道更多特解时，求积的次数还可以减少。

**定理 3.5.2** 设 $y_1,y_2$ 是方程 (3.9) 的两个不同的解，则其余的解 $y$ 满足

$$
\frac{y-y_1}{y-y_2}=C\exp\Big(\int p(x)\big(y_1(x)-y_2(x)\big)\,\mathrm{d}x\Big),\tag{3.11}
$$
只需一次求积。

**证明** 记 $w=\dfrac{y-y_1}{y-y_2}$。由 (3.9)，$y'-y_k'=p(y^2-y_k^2)+q(y-y_k)$，所以 $\dfrac{y'-y_k'}{y-y_k}=p(y+y_k)+q$。于是

$$
\frac{w'}{w}=\frac{y'-y_1'}{y-y_1}-\frac{y'-y_2'}{y-y_2}=p(y_1-y_2),
$$
积分即得式 (3.11)。 $\square$

**定理 3.5.3** 设 $y_1,y_2,y_3,y_4$ 是方程 (3.9) 在区间 $J\subset I$ 上的四个互不相同的解，则它们的交比为常数：

$$
\frac{y_3-y_1}{y_4-y_1}\cdot\frac{y_4-y_2}{y_3-y_2}\equiv C.\tag{3.12}
$$

**证明** 解互不相交，所以各差处处不为零。取定理 3.5.1 中的 $\varphi=y_4$，令 $u_k=\dfrac{1}{y_k-y_4}$（$k=1,2,3$），它们是线性方程 (3.10) 的三个互不相同的解。由 $y_k-y_4=1/u_k$，

$$
\frac{y_3-y_1}{y_4-y_1}=\frac{\frac1{u_3}-\frac1{u_1}}{-\frac1{u_1}}=-\frac{u_1-u_3}{u_3},\qquad\frac{y_4-y_2}{y_3-y_2}=\frac{-\frac1{u_2}}{\frac1{u_3}-\frac1{u_2}}=-\frac{u_3}{u_2-u_3},
$$
两式相乘得 $\dfrac{u_1-u_3}{u_2-u_3}$，由命题 3.2.2 它是常数。 $\square$

**推论 3.5.1** 若已知方程 (3.9) 的三个不同的解 $y_1,y_2,y_3$，则其余的解 $y$ 由代数关系

$$
\frac{y_3-y_1}{y-y_1}\cdot\frac{y-y_2}{y_3-y_2}=C
$$
给出，不需要求积。

定理 3.5.1–3.5.3 可以统一地理解：解的全体与 (3.10) 的解（即一条直线上的点）一一对应，而 $y=\varphi+1/u$ 是分式线性变换。线性方程的解保持"三点的比"，分式线性变换保持"四点的交比"。

**例 3.5.1** 解 $y'=y^2-\dfrac{2}{x^2}$（$x>0$）。试探 $y=\dfrac ax$：$-\dfrac{a}{x^2}=\dfrac{a^2-2}{x^2}$，$a^2+a-2=0$，$a=1$ 或 $a=-2$。取 $y_1=\dfrac1x$，$y_2=-\dfrac2x$，$p=1$，由式 (3.11)，

$$
\frac{y-\frac1x}{y+\frac2x}=C\exp\int\frac3x\,\mathrm{d}x=Cx^3,\qquad\text{即}\qquad y=\frac{1+2Cx^3}{x\,(1-Cx^3)}.
$$
$C=0$ 给出 $y_1$，$y_2$ 对应 $C=\infty$。

### 3.5.3. 与二阶线性方程的关系

**命题 3.5.2** （1）二阶齐次线性方程 $y''+P(x)y'+Q(x)y=0$ 在 $y\ne0$ 处经代换 $z=\dfrac{y'}{y}$（即 $y=\mathrm{e}^{\int z\,\mathrm{d}x}$）化为 Riccati 方程

$$
z'+z^2+P(x)z+Q(x)=0.
$$
（2）反之，设 $p$ 连续可微且不为零，Riccati 方程 (3.9) 经代换 $y=-\dfrac{u'}{p(x)u}$ 化为二阶线性方程

$$
u''-\Big(q(x)+\frac{p'(x)}{p(x)}\Big)u'+p(x)r(x)u=0.
$$

**证明** （1）$y'=zy$，$y''=(z'+z^2)y$，代入后除以 $y$。（2）由 $y=-\dfrac{u'}{pu}$ 直接计算，

$$
y'=-\frac{u''}{pu}+\frac{p'u'}{p^2u}+\frac{u'^2}{pu^2},\qquad py^2=\frac{u'^2}{pu^2},\qquad qy=-\frac{qu'}{pu},
$$
所以 $y'=py^2+qy+r$ 等价于 $-\dfrac{u''}{pu}+\dfrac{p'u'}{p^2u}=-\dfrac{qu'}{pu}+r$，两边乘以 $-pu$ 即得结论。 $\square$

因此求解 Riccati 方程与求解二阶齐次线性方程是同一个问题。二阶线性方程一般也不能用初等函数求解，这从另一个角度说明了 Riccati 方程的困难。例如 $y'=x^2+y^2$ 经 $y=-\dfrac{u'}{u}$ 化为 $u''+x^2u=0$，它的解可以用 Bessel 函数表示为 $\sqrt{x}\,J_{\pm1/4}\Big(\dfrac{x^2}{2}\Big)$（[2.4.10](/2.4.10)），而不是初等函数。命题 3.5.2 的（1）在 Sturm 理论中也有用：二阶方程解的零点与 Riccati 方程解的爆破相对应（[2.4.12](/2.4.12)）。

### 3.5.4. Liouville 定理

**定理 3.5.4（Liouville）** 设 $a\ne0$，$b\ne0$。Riccati 方程

$$
y'+ay^2=bx^m
$$
可以用初等函数的有限次求积求解，当且仅当

$$
m=0,\qquad m=-2,\qquad m=\frac{-4k}{2k+1},\qquad m=\frac{-4k}{2k-1}\qquad(k=1,2,\dots).
$$

这里只说明充分性的思路（必要性的证明较长，略去）。作自变量的伸缩可设 $a=1$。$m=0$ 时方程 $y'=b-y^2$ 是变量分离方程。$m=-2$ 时令 $u=xy$，方程化为 $xu'=b+u-u^2$，也是变量分离方程（例 3.5.1 是这种情形）。其余情形用两种代换降低 $k$：

- $T_1$：$\xi=x^{m+1}$，$y=\dfrac{b}{m+1}\cdot\dfrac1\eta$，把 $y'+y^2=bx^m$ 化为 $\dfrac{\mathrm{d}\eta}{\mathrm{d}\xi}+\eta^2=\dfrac{b}{(m+1)^2}\xi^{n}$，$n=-\dfrac{m}{m+1}$；它把 $m=\dfrac{-4k}{2k+1}$ 变为 $n=\dfrac{-4k}{2k-1}$。
- $T_2$：$x=\dfrac1t$，$y=t-zt^2$，把 $y'+y^2=cx^n$ 化为 $\dfrac{\mathrm{d}z}{\mathrm{d}t}+z^2=ct^{-n-4}$；它把 $n=\dfrac{-4k}{2k-1}$ 变为 $\dfrac{-4(k-1)}{2(k-1)+1}$。

从 $m=\dfrac{-4k}{2k+1}$ 出发交替使用 $T_1,T_2$（从 $m=\dfrac{-4k}{2k-1}$ 出发则先用 $T_2$），$k$ 轮之后指数化为 $0$。

Liouville 定理（1841）说明，即使形式上很简单的方程 $y'=x^2+y^2$（$m=2$ 不在上述序列中）也不能用求积法求解。这是微分方程的研究从"求通解"转向存在性理论与定性理论的一个重要契机（[2.4.1](/2.4.1#sec-1.3)）。

## 3.6. 等角轨线与正交轨线

**定义 3.6.1** 给定平面上的单参数曲线族。若曲线 $L$ 与族中的每一条曲线都相交成定角 $\alpha$（指交点处切线的夹角），则称 $L$ 为该曲线族的**等角轨线**；$\alpha=\dfrac\pi2$ 时称为**正交轨线**。

等角轨线在物理中常见：静电场的电力线是等势线族的正交轨线，流体的流线是等势线的正交轨线；热传导中热流线是等温线的正交轨线。

设曲线族满足一阶方程 $y'=f(x,y)$（由族的方程消去参数得到），所求轨线满足 $y'=g(x,y)$。在交点处，设族中曲线的切线倾角为 $\theta_1$，轨线的切线倾角为 $\theta_2$，$\alpha=\theta_2-\theta_1$。当 $\alpha\ne\dfrac\pi2$ 时，记 $k=\tan\alpha$，

$$
k=\tan(\theta_2-\theta_1)=\frac{\tan\theta_2-\tan\theta_1}{1+\tan\theta_1\tan\theta_2}=\frac{g-f}{1+gf},
$$
解出 $g$ 得等角轨线的方程

$$
y'=\frac{f(x,y)+k}{1-kf(x,y)};\tag{3.13}
$$
当 $\alpha=\dfrac\pi2$ 时 $fg=-1$，正交轨线的方程为

$$
y'=-\frac{1}{f(x,y)}.\tag{3.14}
$$
若曲线族的方程是隐式的 $F(x,y,y')=0$，则由 $f=\dfrac{g-k}{1+kg}$，等角轨线满足

$$
F\Big(x,y,\frac{y'-k}{1+ky'}\Big)=0,
$$
正交轨线满足 $F\Big(x,y,-\dfrac{1}{y'}\Big)=0$。

**例 3.6.1** 求直线族 $y=Cx$ 的等角轨线与正交轨线。

由 $y=Cx$ 消去 $C$ 得 $f=\dfrac yx$。代入式 (3.13)，

$$
y'=\frac{k+\frac yx}{1-k\frac yx},
$$
这是齐次型方程。令 $y=xu$，

$$
xu'=\frac{k+u}{1-ku}-u=\frac{k(1+u^2)}{1-ku},\qquad\frac{\mathrm{d}u}{1+u^2}-\frac{ku\,\mathrm{d}u}{1+u^2}=\frac{k\,\mathrm{d}x}{x}.
$$
积分得 $\arctan u-\dfrac k2\ln(1+u^2)=k\ln\lvert x\rvert+c$，代回 $u=y/x$，

$$
\arctan\frac yx=k\ln\sqrt{x^2+y^2}+c.
$$
在极坐标中即 $\rho=C\mathrm{e}^{\theta/k}$（$C>0$），是对数螺线：对数螺线与每条过原点的射线交成定角，这正是它又称"等角螺线"的原因。$\alpha=\dfrac\pi2$ 时由式 (3.14)，$y'=-\dfrac xy$，即 $x\,\mathrm{d}x+y\,\mathrm{d}y=0$，正交轨线是同心圆 $x^2+y^2=C^2$。

![直线族 y = Cx（灰色）与它的等角轨线：交角 alpha = pi/3 时为对数螺线 rho = C e^{theta/k}，k = tan alpha（蓝色），alpha = pi/2 时为同心圆（红色虚线）](./plots/isogonal-spirals.py)

**例 3.6.2** 求椭圆族 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=C^2$（$C>0$，$a,b$ 固定）的正交轨线。

对 $x$ 求导，$\dfrac{2x}{a^2}+\dfrac{2yy'}{b^2}=0$，得 $f=-\dfrac{b^2x}{a^2y}$。由式 (3.14)，

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=\frac{a^2y}{b^2x},\qquad\frac{\mathrm{d}y}{y}=\frac{a^2}{b^2}\cdot\frac{\mathrm{d}x}{x},
$$
积分得 $y=C\lvert x\rvert^{a^2/b^2}$（$C$ 为任意常数），另外 $x=0$（$y$ 轴）也是正交轨线。正交轨线是一族幂函数曲线，都从原点（椭圆族的公共中心）发出；$a=b$ 时椭圆是同心圆，正交轨线退化为过原点的直线，与例 3.6.1 一致。

![椭圆族 x^2/a^2 + y^2/b^2 = C^2（a = 2，b = 1，灰色）与它的正交轨线 y = C|x|^{a^2/b^2} = C x^4（蓝色，C = 0 时为 x 轴）及 y 轴](./plots/orthogonal-ellipses.py)

## 小结

| 方程 | 变换 | 要点 |
|---|---|---|
| 变量分离 $y'=f(x)g(y)$ | $\int\frac{\mathrm{d}y}{g}=\int f\,\mathrm{d}x$ | $g(y_0)\ne0$ 处解唯一；$g(c)=0$ 给出解 $y=c$，唯一性取决于 $\int\frac{\mathrm{d}s}{g}$ 在 $c$ 处是否发散 |
| 一阶线性 $y'+py=q$ | 积分因子 $\mathrm{e}^{\int p}$ | 公式 (3.4)；整体存在；解集是一维仿射空间 |
| 周期系数 | $y(T)=y(0)$ | $\bar p\ne0$：唯一周期解；$\bar p=0$：全是或全不是 |
| 齐次型 $y'=f(y/x)$ | $y=xu$ | 化为变量分离 |
| Bernoulli | $z=y^{1-n}$ | 化为线性 |
| Riccati | $y=\varphi+1/u$ | 一个特解：两次求积；两个：一次；三个：代数关系；交比不变；等价于二阶线性方程 |
| 等角轨线 | $y'=\frac{f+k}{1-kf}$；正交 $y'=-\frac1f$ | 直线族 → 对数螺线；椭圆族 → 幂函数 |
