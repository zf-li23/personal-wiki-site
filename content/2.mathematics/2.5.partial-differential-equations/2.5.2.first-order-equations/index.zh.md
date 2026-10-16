---
title: 一阶方程与特征线法
source_hash: 3de38de62dec
---

一阶方程是最简单的偏微分方程，也是原则上只用常微分方程就能求解的唯一一类偏微分方程。关键的想法在 [2.4.14](/2.4.14) 中已经出现：线性齐次方程 $\sum f_iu_{x_i}=0$ 的解沿**特征线**（向量场 $\boldsymbol{f}$ 的积分曲线）为常数，所以求解偏微分方程化为求解特征方程组，并在每条特征线上给定一个值。本章把这一想法发展为特征线法（method of characteristics）。我们从输运方程开始，那里的特征线是被流动携带的质点的轨迹；然后讨论一般的拟线性方程与 Cauchy 问题，数据在一条曲线上给出，决定性的条件是这条曲线与特征线横截。非线性带来新的现象：对 Burgers 方程，特征线在有限时间内相交，光滑解失效，形成激波。最后讨论完全非线性方程与 Charpit 方法，这完成了 [2.4.14](/2.4.14#sec-14.5) 中从 Clairaut 方程开始的关于完全积分的讨论。对二阶方程，特征线仍然处于中心地位：对波动方程（[2.5.3](/2.5.3)），它们就是 [2.5.1](/2.5.1#sec-1.5.2) 中求得的直线 $x\pm ct=\text{常数}$。

## 2.1. 输运方程

### 2.1.1. 常速度

考虑以常速度 $c$ 沿直渠道流动的水中溶解的污染物，设 $u(x,t)$ 是它的浓度。若污染物既不扩散也不衰减，它的浓度分布就只是随水一起被携带。用质量守恒来表述，区间 $[a,b]$ 中的污染物总量只通过在 $a$ 处流入、在 $b$ 处流出的通量 $cu$ 而改变：$\frac{\mathrm{d}}{\mathrm{d}t}\int_a^bu\,\mathrm{d}x=cu(a,t)-cu(b,t)$。对 $b$ 求导得 $u_t=-cu_x$。

**定义 2.1.1（输运方程）** 方程

$$
u_t+cu_x=0,\qquad x\in\mathbb{R},\ t>0,\tag{2.1}
$$
（$c$ 为常数）称为**输运方程**（或对流方程）。

式 (2.1) 的左端是 $u$ 在 $(x,t)$ 平面中沿方向 $(c,1)$ 的**方向导数**乘以 $\sqrt{1+c^2}$。所以方程说的是 $u$ 沿每条直线 $x-ct=x_0$ 为常数：这些直线就是式 (2.1) 的特征线。

**定理 2.1.1** 对每个 $f\in C^1(\mathbb{R})$，初值问题 $u_t+cu_x=0$，$u(x,0)=f(x)$ 恰有一个 $C^1$ 解，即

$$
u(x,t)=f(x-ct).\tag{2.2}
$$

**证明** 函数 (2.2) 是 $C^1$ 的，且 $u_t+cu_x=-cf'(x-ct)+cf'(x-ct)=0$，$u(x,0)=f(x)$。反之，设 $u$ 是任一 $C^1$ 解，固定 $x_0$。沿特征线，$v(t)=u(x_0+ct,t)$ 满足 $v'(t)=cu_x+u_t=0$，所以 $v(t)=v(0)=f(x_0)$。每个点 $(x,t)$ 都在 $x_0=x-ct$ 的那条直线上，因此 $u(x,t)=f(x-ct)$。$\square$

$u(\cdot,t)$ 的图像是 $f$ 的图像平移 $ct$：初始波形以速度 $c$ 向右传播（$c<0$ 时向左），形状不变。形如 $f(x-ct)$ 的解称为行波。

公式 (2.2) 对任何函数 $f$（即使不连续）都有意义。这时它不是古典解，但它是以逼近 $f$ 的光滑数据为初值的古典解的极限；数据有角点或跳跃时就需要这种广义解，它们说明对输运方程，数据中的间断沿特征线传播。

有源项时，同样的想法仍然适用：沿特征线，方程成为常微分方程。

**定理 2.1.2** 设 $f\in C^1(\mathbb{R})$，$g$ 与 $g_x$ 连续。则

$$
u_t+cu_x=g(x,t),\qquad u(x,0)=f(x)
$$
的唯一 $C^1$ 解是

$$
u(x,t)=f(x-ct)+\int_0^tg\big(x-c(t-s),s\big)\,\mathrm{d}s.\tag{2.3}
$$

**证明** 把过 $(x,t)$ 的特征线参数化为 $X(s)=x-c(t-s)$，$0\le s\le t$，则函数 $v(s)=u(X(s),s)$ 满足 $v'(s)=cu_x+u_t=g(X(s),s)$，$v(0)=f(x-ct)$；从 $0$ 到 $t$ 积分即得式 (2.3)，这同时证明了唯一性。用**积分号下求导**可以验证 (2.3) 确实是解。$\square$

式 (2.3) 中的积分汇集了沿那个在时刻 $t$ 到达 $x$ 的流体质点的路径上源项的贡献。这是 Duhamel 原理最简单的例子，波动方程中还会再次出现（[2.5.3](/2.5.3#sec-3.3)）。

**例 2.1.1** 被水流携带、同时以速率 $\lambda>0$ 衰减的污染物满足 $u_t+cu_x=-\lambda u$，$u(x,0)=f(x)$。沿特征线 $X(s)=x_0+cs$ 有 $\frac{\mathrm{d}}{\mathrm{d}s}u(X(s),s)=-\lambda u$，所以 $u$ 沿每条特征线指数衰减，

$$
u(x,t)=f(x-ct)\,\mathrm{e}^{-\lambda t}.
$$

### 2.1.2. 变速度

若流速依赖于位置与时间，方程成为

$$
u_t+a(x,t)u_x=0,\tag{2.4}
$$
其中 $a$ 连续可微。沿曲线 $x=X(t)$ 有 $\frac{\mathrm{d}}{\mathrm{d}t}u(X(t),t)=u_x X'+u_t$，当 $X'(t)=a(X(t),t)$ 时它为零。所以式 (2.4) 的特征线是常微分方程

$$
\frac{\mathrm{d}x}{\mathrm{d}t}=a(x,t)\tag{2.5}
$$
的解，即流体质点的轨迹，$u$ 沿每一条都是常数。由**存在唯一性定理**，过每一点恰有一条特征线，所以特征线互不相交。求解初值 $u(x,0)=f(x)$ 的问题时，沿过 $(x,t)$ 的特征线回溯到时刻 $t=0$，它从某点 $x_0(x,t)$ 出发，于是令 $u(x,t)=f(x_0(x,t))$。

**例 2.1.2** 求解 $u_t+xu_x=0$，$u(x,0)=f(x)$。

**解** 特征线满足 $\frac{\mathrm{d}x}{\mathrm{d}t}=x$，所以 $x=x_0\mathrm{e}^t$，回溯得 $x_0=x\mathrm{e}^{-t}$。因此

$$
u(x,t)=f(x\mathrm{e}^{-t}).
$$
验证：$u_t=-x\mathrm{e}^{-t}f'(x\mathrm{e}^{-t})$，$xu_x=x\mathrm{e}^{-t}f'(x\mathrm{e}^{-t})$。流动 $a(x,t)=x$ 使质点越来越快地远离原点，所以初始波形被拉伸 $\mathrm{e}^t$ 倍。

![沿特征线的输运。左：对 u_t + u_x = 0，特征线是平行直线，波形整体平移。右：对 u_t + x u_x = 0，特征线 x = x₀eᵗ 呈扇形散开，波形被拉伸](./plots/transport-characteristics.py)

## 2.2. 拟线性方程

### 2.2.1. 特征线与积分曲面

现在考虑两个自变量的一般拟线性方程

$$
P(x,y,u)\,u_x+Q(x,y,u)\,u_y=R(x,y,u),\tag{2.6}
$$
其中 $P,Q,R$ 连续可微，$P,Q$ 不同时为零。解 $u(x,y)$ 在几何上用它在 $(x,y,z)$ 空间中的图像 $z=u(x,y)$ 表示，称为式 (2.6) 的积分曲面。在每一点，向量 $(u_x,u_y,-1)$ 是曲面的**法向量**，而式 (2.6) 说的是

$$
(P,Q,R)\cdot(u_x,u_y,-1)=0.
$$
也就是说，$(x,y,z)$ 空间中的向量场 $(P,Q,R)$（称为特征方向场）与每个积分曲面相切。

**定义 2.2.1（拟线性方程的特征线）** $(x,y,z)$ 空间中方程组

$$
\frac{\mathrm{d}x}{\mathrm{d}s}=P(x,y,z),\qquad\frac{\mathrm{d}y}{\mathrm{d}s}=Q(x,y,z),\qquad\frac{\mathrm{d}z}{\mathrm{d}s}=R(x,y,z)\tag{2.7}
$$
的积分曲线称为式 (2.6) 的**特征线**，它们在 $(x,y)$ 平面上的投影称为投影特征线。消去参数 $s$，方程组成为对称形式 $\dfrac{\mathrm{d}x}{P}=\dfrac{\mathrm{d}y}{Q}=\dfrac{\mathrm{d}z}{R}$。

对线性方程（$P,Q$ 与 $z$ 无关），投影特征线与解无关；对拟线性方程则不然，因为 $P$ 与 $Q$ 依赖于 $z=u$。下面的定理是这一方法的几何核心。

**定理 2.2.1** 设 $u\in C^2$ 是式 (2.6) 的解，积分曲面为 $S$。若一条特征线有一点在 $S$ 上，则它整个位于 $S$ 上（只要它还在 $u$ 的定义域内）。因此每个积分曲面都是特征线的并。

**证明** 设 $(x(s),y(s),z(s))$ 是满足 $z(0)=u(x(0),y(0))$ 的特征线，令 $U(s)=z(s)-u(x(s),y(s))$。则 $(x,y,U)$ 满足方程组

$$
x'=P(x,y,u+U),\qquad y'=Q(x,y,u+U),\qquad U'=R(x,y,u+U)-u_x(x,y)P(x,y,u+U)-u_y(x,y)Q(x,y,u+U),
$$
其中 $u,u_x,u_y$ 都在 $(x,y)$ 处取值。由于 $u\in C^2$，右端是 $C^1$ 的。另一方面，设 $(\tilde x(s),\tilde y(s))$ 满足 $\tilde x'=P(\tilde x,\tilde y,u(\tilde x,\tilde y))$，$\tilde y'=Q(\tilde x,\tilde y,u(\tilde x,\tilde y))$，初始点相同。由于 $u$ 是式 (2.6) 的解，$(\tilde x,\tilde y,0)$ 也满足上面的方程组，初值同样是 $U(0)=0$。由存在唯一性定理，两个解重合，所以 $U\equiv0$：特征线始终在 $S$ 上。$\square$

反之，由单参数特征线族扫出的曲面是积分曲面，因为特征方向与它相切。这就是特征线法：用特征线拼成解曲面。若已知方程组 (2.7) 的两个独立的**首次积分** $\Psi_1(x,y,z)$ 与 $\Psi_2(x,y,z)$，则每条特征线由 $\Psi_1=C_1$、$\Psi_2=C_2$ 给出；在两个常数之间加上一个关系，就得到单参数特征线族；由此得到 Lagrange 的通解

$$
G\big(\Psi_1(x,y,u),\Psi_2(x,y,u)\big)=0,\tag{2.8}
$$
其中 $G$ 是任意函数，与 [2.4.14](/2.4.14#sec-14.2) 中一样。通解很少是问题的终点：实践中 $G$ 必须由数据确定。

### 2.2.2. Cauchy 问题

**定义 2.2.2（Cauchy 问题）** 设 $\Gamma_0\colon x=x_0(\tau)$，$y=y_0(\tau)$（$\tau\in I$）是 $(x,y)$ 平面中的 $C^1$ 曲线，$u_0(\tau)$ 是 $C^1$ 函数。式 (2.6) 的 Cauchy 问题是求在 $\Gamma_0$ 附近有定义、满足

$$
u\big(x_0(\tau),y_0(\tau)\big)=u_0(\tau),\qquad\tau\in I
$$
的解 $u$。几何上，就是求包含空间曲线 $\Gamma\colon(x_0(\tau),y_0(\tau),u_0(\tau))$ 的积分曲面。若

$$
P\big(x_0,y_0,u_0\big)\,y_0'(\tau)-Q\big(x_0,y_0,u_0\big)\,x_0'(\tau)\ne0,\tag{2.9}
$$
即过该点的投影特征线不与 $\Gamma_0$ 相切，则称 $\Gamma_0$ 在 $\tau$ 处满足**非特征条件**。

§2.1 的初值问题 $u(x,0)=f(x)$ 是 $x_0(\tau)=\tau$、$y_0(\tau)=0$ 的特殊情形（$y$ 起 $t$ 的作用）；这时 (2.9) 成为 $Q\ne0$，对式 (2.1) 由于 $Q=1$ 而成立。

**定理 2.2.2（局部存在唯一性）** 设 $P,Q,R\in C^1$，$x_0,y_0,u_0\in C^1(I)$，且非特征条件 (2.9) 在 $\tau=\tau_0$ 处成立。则在点 $(x_0(\tau_0),y_0(\tau_0))$ 的某个邻域内，Cauchy 问题恰有一个 $C^1$ 解。

**证明** 对每个 $\tau$，以 $s=0$ 时的 $(x_0(\tau),y_0(\tau),u_0(\tau))$ 为初值求解特征方程组 (2.7)。由解对初值的可微依赖性（[2.4.7](/2.4.7)），得到的函数 $x(s,\tau)$、$y(s,\tau)$、$z(s,\tau)$ 关于两个变量都是 $C^1$ 的。在 $s=0$ 处它们的 Jacobi 行列式为

$$
\frac{\partial(x,y)}{\partial(s,\tau)}\bigg|_{s=0}=x_sy_\tau-y_sx_\tau=P\,y_0'-Q\,x_0'\ne0.
$$
由**逆映射定理**，在 $(0,\tau_0)$ 附近映射 $(s,\tau)\mapsto(x,y)$ 有 $C^1$ 的逆 $s=s(x,y)$，$\tau=\tau(x,y)$。令 $u(x,y)=z(s(x,y),\tau(x,y))$。$s=0$ 时它给出数据。此外，由链式法则与式 (2.7)，

$$
R=z_s=u_xx_s+u_yy_s=Pu_x+Qu_y,
$$
所以 $u$ 是式 (2.6) 的解。唯一性：若 $u$ 是具有给定数据的 $C^2$ 解，则它的积分曲面包含 $\Gamma$，由定理 2.2.1，它包含过 $\Gamma$ 的每条特征线，因此与刚才构造的曲面重合。（用稍细致一些的论证，$C^1$ 解的唯一性同样成立。）$\square$

若 $\Gamma_0$ 是特征的，即沿它 $Py_0'-Qx_0'\equiv0$，则数据不能任意给定：若 $\Gamma$ 本身是特征线，过它的积分曲面有无穷多个；若 $\Gamma_0$ 是投影特征线而 $\Gamma$ 不是特征线，则无解，因为方程已经决定了 $u$ 沿 $\Gamma_0$ 怎样变化。

### 2.2.3. 例题

**例 2.2.1** 求解 $u_x+2xu_y=y$，$u(0,y)=f(y)$。

**解** 数据曲线为 $x_0=0$，$y_0=\tau$，$u_0=f(\tau)$，且 $Py_0'-Qx_0'=1\ne0$：处处满足非特征条件。特征方程组为 $x_s=1$，$y_s=2x$，$z_s=y$，解为

$$
x=s,\qquad y=\tau+s^2,\qquad z=f(\tau)+\tau s+\frac{s^3}{3}.
$$
反解得 $s=x$，$\tau=y-x^2$，因此

$$
u(x,y)=f(y-x^2)+(y-x^2)x+\frac{x^3}{3}=f(y-x^2)+xy-\frac23x^3.
$$
验证：$u_x=-2xf'+y-2x^2$，$u_y=f'+x$，所以 $u_x+2xu_y=y$。投影特征线是抛物线 $y-x^2=\text{常数}$，每条都恰好与 $y$ 轴相交一次。

**例 2.2.2（特征数据）** 考虑 $yu_x-xu_y=0$。由特征方程组 $x_s=y$，$y_s=-x$，$z_s=0$，投影特征线是圆周 $x^2+y^2=r^2$（方程说的是 $u$ 在绕原点的旋转下不变），$u$ 在每个圆周上为常数。若在正 $x$ 轴上给出数据 $u(x,0)=f(x)$（$x>0$），唯一解为 $u=f\big(\sqrt{x^2+y^2}\big)$。若在整个 $x$ 轴上给出数据，每个圆周与它相交两次，所以只有当 $f(-x)=f(x)$ 时解才存在。在原点处非特征条件不成立：那里 $Py_0'-Qx_0'=y_0\cdot0+x_0\cdot1=x_0=0$。

**例 2.2.3** 求解 $(y+u)u_x+yu_y=x-y$，在直线 $y=1$ 上 $u=1+x$。

**解** 数据曲线 $x_0=\tau$，$y_0=1$ 给出 $Py_0'-Qx_0'=-y_0=-1\ne0$：满足非特征条件。用可积组合（[2.4.14](/2.4.14#sec-14.1.3)）求 $\frac{\mathrm{d}x}{y+z}=\frac{\mathrm{d}y}{y}=\frac{\mathrm{d}z}{x-y}$ 的首次积分。第一与第三个比式相加，$\frac{\mathrm{d}(x+z)}{x+z}=\frac{\mathrm{d}y}{y}$，所以 $\Psi_1=\frac{x+z}{y}$。二者相减，$\frac{\mathrm{d}(x-z)}{\mathrm{d}s}=2y-(x-z)$，其中 $y=C\mathrm{e}^s$，由此得 $x-z=y+C'\mathrm{e}^{-s}$，从而 $\Psi_2=y(x-z-y)$。在数据曲线上，对每个 $\tau$ 都有 $\Psi_2=1\cdot(\tau-1-\tau-1)=-2$。所以过 $\Gamma$ 的积分曲面是 $y(x-u-y)=-2$，即

$$
u(x,y)=x-y+\frac2y,\qquad y>0.
$$
验证：$u_x=1$，$u_y=-1-\frac2{y^2}$，且 $(y+u)-y-\frac2y=x-y$。这里数据确定了式 (2.8) 中的 $G$ 为 $G(\Psi_1,\Psi_2)=\Psi_2+2$。

对 $n$ 个自变量，一切都可以照搬：方程 $\sum_{i=1}^nP_i(x,u)u_{x_i}=R(x,u)$ 的特征方程组为 $\frac{\mathrm{d}x_i}{\mathrm{d}s}=P_i$，$\frac{\mathrm{d}z}{\mathrm{d}s}=R$，数据在 $n-1$ 维超曲面上给出，非特征条件是投影特征方向 $(P_1,\dots,P_n)$ 不与超曲面相切。

## 2.3. 无粘 Burgers 方程与激波

### 2.3.1. 波的破裂

输运方程最简单的非线性形式，是让速度依赖于被输运的量本身。

**定义 2.3.1（Burgers 方程）** 拟线性方程

$$
u_t+uu_x=0\tag{2.10}
$$
称为**无粘 Burgers 方程**。（右端加上粘性项 $\nu u_{xx}$ 时称为粘性 Burgers 方程。）

它描述一维的互不作用的粒子流，每个粒子以常速度运动：$u(x,t)$ 是时刻 $t$ 位于 $x$ 的粒子的速度，$u_t+uu_x$ 是它的加速度。由特征方程组 $\frac{\mathrm{d}t}{\mathrm{d}s}=1$，$\frac{\mathrm{d}x}{\mathrm{d}s}=u$，$\frac{\mathrm{d}u}{\mathrm{d}s}=0$，$u$ 沿每条特征线为常数，所以特征线是直线。对初始条件 $u(x,0)=f(x)$，从 $x_0$ 出发的特征线是

$$
x=x_0+f(x_0)\,t,\qquad\text{其上}\qquad u=f(x_0),\tag{2.11}
$$
消去 $x_0$ 得到解的隐式形式 $u=f(x-ut)$。波形中较快的部分追上较慢的部分。若 $f$ 单调增加，特征线呈扇形散开，波展宽；若 $f$ 在某处减少，从那一部分出发的特征线相互靠拢并最终相交，在交点处有两个不同的 $u$ 值被带入：解不再是单值的。

**定理 2.3.1（破裂时间）** 设 $f\in C^1(\mathbb{R})$，$f$ 与 $f'$ 有界。

1. 若处处 $f'\ge0$，则式 (2.10) 在 $u(x,0)=f(x)$ 下的初值问题对一切 $t\ge0$ 有唯一的 $C^1$ 解。
2. 若 $\inf f'<0$，则 $C^1$ 解在 $0\le t<T^*$ 上存在，其中

$$
T^*=-\frac{1}{\inf_{x}f'(x)},\tag{2.12}
$$
且它不能作为 $C^1$ 解延拓到 $T^*$ 以后：若下确界在 $x_0$ 处取到，则 $t\to T^*$ 时沿从 $x_0$ 出发的特征线 $u_x\to-\infty$。

**证明** 对固定的 $t$，考虑映射 $x_0\mapsto x=x_0+f(x_0)t$。它的导数是 $1+f'(x_0)t$，若 $f'\ge0$，或 $0\le t<T^*$，则它对一切 $x_0$ 为正。由于 $f$ 有界，$x_0\to\pm\infty$ 时 $x\to\pm\infty$，所以这个映射是 $\mathbb{R}$ 的 $C^1$ 双射，有 $C^1$ 的逆 $x_0(x,t)$：过每一点 $(x,t)$ 恰有一条特征线。令 $u(x,t)=f(x_0(x,t))$。对 $x_0+f(x_0)t=x$ 求导得

$$
\frac{\partial x_0}{\partial x}=\frac{1}{1+f'(x_0)t},\qquad\frac{\partial x_0}{\partial t}=-\frac{f(x_0)}{1+f'(x_0)t},
$$
因此

$$
u_t+uu_x=f'(x_0)\frac{\partial x_0}{\partial t}+f(x_0)f'(x_0)\frac{\partial x_0}{\partial x}=0,\qquad u_x=\frac{f'(x_0)}{1+f'(x_0)t}.\tag{2.13}
$$
由于每个解都沿特征线 (2.11) 为常数，唯一性由定理 2.2.1 得到。最后，若 $f'(x_0)=\inf f'<0$，由式 (2.13)，$t\to T^*$ 时沿这条特征线 $u_x\to-\infty$。$\square$

**例 2.3.1** 对 $f(x)=\mathrm{e}^{-x^2}$，$f'(x)=-2x\mathrm{e}^{-x^2}$，其最小值在 $x=\frac{1}{\sqrt2}$ 处取到，等于 $-\sqrt2\,\mathrm{e}^{-1/2}$。破裂时间为

$$
T^*=\frac{\mathrm{e}^{1/2}}{\sqrt2}=\sqrt{\frac{\mathrm e}{2}}\approx1.166.
$$
驼峰的前沿变陡，在 $t=T^*$ 时变成竖直的，此后公式 (2.11) 描述的是多值的"破碎波"，就像海滩上翻卷的浪。

![初值 u(x, 0) = exp(-x²) 的 Burgers 方程。左：特征线 x = x₀ + f(x₀)t 在破裂时间 T* ≈ 1.17 之后相交。右：波形变陡，t > T* 时成为多值的；激波（虚线）取代了翻卷的部分](./plots/burgers-breaking.py)

### 2.3.2. 守恒律与激波

对物理量而言，多值的波形没有意义；实际形成的是间断，即激波（shock wave）。为了描述它，必须回到推导微分方程时所用的平衡律的积分形式。式 (2.10) 可以写成 $u_t+\big(\frac12u^2\big)_x=0$，这是

$$
u_t+F(u)_x=0\tag{2.14}
$$
的特殊情形；式 (2.14) 称为通量为 $F$ 的守恒律（conservation law）：在 $[a,b]$ 上积分，

$$
\frac{\mathrm{d}}{\mathrm{d}t}\int_a^bu(x,t)\,\mathrm{d}x=F\big(u(a,t)\big)-F\big(u(b,t)\big),\tag{2.15}
$$
所以 $[a,b]$ 中 $u$ 的总量只通过两端的通量而改变。积分形式 (2.15) 对不连续的 $u$ 也有意义。对一切 $a<b$ 满足式 (2.15) 的（分段 $C^1$ 的）函数称为式 (2.14) 的弱解（weak solution）；它在光滑之处满足微分方程。

**定理 2.3.2（Rankine–Hugoniot 条件）** 设 $u$ 是式 (2.14) 的弱解，在 $C^1$ 曲线 $x=\xi(t)$ 的两侧都是 $C^1$ 的，在曲线上的单侧极限为 $u_l$（左）与 $u_r$（右）。则

$$
\xi'(t)=\frac{F(u_l)-F(u_r)}{u_l-u_r}.\tag{2.16}
$$
对 Burgers 方程，$F(u)=\frac12u^2$，激波速度为 $\xi'=\frac12(u_l+u_r)$。

**证明** 取 $a<\xi(t)<b$，把积分拆成 $\int_a^b=\int_a^{\xi(t)}+\int_{\xi(t)}^b$。对 $t$ 求导（变动的积分限贡献 $\xi'u_l$ 与 $-\xi'u_r$），并在两侧利用 $u_t=-F(u)_x$，

$$
\frac{\mathrm{d}}{\mathrm{d}t}\int_a^bu\,\mathrm{d}x=\xi'u_l+\big[F(u(a,t))-F(u_l)\big]-\xi'u_r+\big[F(u_r)-F(u(b,t))\big].
$$
与式 (2.15) 比较得 $\xi'(u_l-u_r)=F(u_l)-F(u_r)$。$\square$

**例 2.3.2（Riemann 问题）** 求解初始数据分段为常数的 Burgers 方程：$x<0$ 时 $u(x,0)=u_l$，$x>0$ 时 $u(x,0)=u_r$。

1. $u_l=1$，$u_r=0$。从 $x_0<0$ 出发的特征线 $x=x_0+t$ 撞上从 $x_0>0$ 出发的竖直特征线。速度为 $\frac12(1+0)=\frac12$ 的激波化解了这一冲突：

$$
u(x,t)=\begin{cases}1,&x<t/2,\\0,&x>t/2.\end{cases}
$$
2. $u_l=0$，$u_r=1$。以 $x=t/2$ 为激波的同一公式仍是弱解，但其中特征线从激波发出，仿佛信息在那里被创造出来。另一个弱解是连续的稀疏波（rarefaction wave）

$$
u(x,t)=\begin{cases}0,&x\le0,\\x/t,&0<x<t,\\1,&x\ge t,\end{cases}
$$
其中一束过原点的扇形特征线填补了空隙（验证：$u=x/t$ 给出 $u_t+uu_x=-\frac{x}{t^2}+\frac xt\cdot\frac1t=0$）。这才是物理上正确的解：它是 $\nu\to0$ 时粘性 Burgers 方程的解的极限，也是实际观察到的现象。

![Burgers 方程在 (x, t) 平面中的 Riemann 问题。左：u_l = 1 > u_r = 0，特征线汇入激波 x = t/2。右：u_l = 0 < u_r = 1，扇形稀疏波 u = x/t](./plots/riemann-problems.py)

因此弱解不唯一，需要附加的选择原则。对 Burgers 方程，这就是熵条件（entropy condition）$u_l>\xi'>u_r$：特征线必须从两侧汇入激波，而不能从激波发出。加上这一条件，通量 $F$ 为凸函数时式 (2.14) 的初值问题恰有一个弱解（Oleinik，Kruzhkov），相关理论是现代气体动力学的重要组成部分。

同样的数学也描述交通流。设 $\rho(x,t)$ 是道路上车辆的密度，车速为 $v(\rho)=v_{\max}(1-\rho/\rho_{\max})$，则车辆守恒给出 $\rho_t+F(\rho)_x=0$，$F(\rho)=\rho\,v(\rho)$。激波是堵车队尾的突然刹车；稀疏波是红灯转绿后车队的逐渐疏散。

## 2.4. 完全非线性方程

两个自变量的完全非线性一阶方程具有形式

$$
F(x,y,u,p,q)=0,\qquad p=u_x,\quad q=u_y.\tag{2.17}
$$
这时方程不在解曲面的每一点规定一个方向，而只规定一个单参数的可能切平面族（"Monge 锥"）。若沿特征线的未知量不仅取 $(x,y,u)$，还取切平面 $(p,q)$，特征线法仍然适用：一条曲线连同沿它的切平面场称为特征带。沿特征带对式 (2.17) 求导，得到 Lagrange–Charpit 方程组

$$
\frac{\mathrm{d}x}{F_p}=\frac{\mathrm{d}y}{F_q}=\frac{\mathrm{d}u}{pF_p+qF_q}=-\frac{\mathrm{d}p}{F_x+pF_u}=-\frac{\mathrm{d}q}{F_y+qF_u}.\tag{2.18}
$$
对拟线性方程 $F=Pp+Qq-R$，前三个比式就化为方程组 (2.7)。

我们不讨论一般的 Cauchy 问题，而说明式 (2.18) 怎样给出**完全积分**，即双参数解族 $u=\Phi(x,y;a,b)$（[2.4.14](/2.4.14#sec-14.5)）；其他解都可以作为包络得到。

Charpit 方法（Charpit's method）分为三步。

1. 求方程组 (2.18) 的一个与 $F$ 无关的首次积分 $\Phi(x,y,u,p,q)=a$（常由最后两个比式得到）。
2. 由 $F=0$ 与 $\Phi=a$ 解出 $p=p(x,y,u;a)$ 与 $q=q(x,y,u;a)$。
3. 这时 **Pfaff 方程** $\mathrm{d}u=p\,\mathrm{d}x+q\,\mathrm{d}y$ 是**完全可积**的（这正是首次积分所保证的）；积分它，引入第二个常数 $b$，就得到完全积分。

**例 2.4.1（程函方程）** 求 $u_x^2+u_y^2=1$ 的完全积分。

**解** 这里 $F=p^2+q^2-1$，所以 $F_x=F_y=F_u=0$，式 (2.18) 的最后两个比式给出 $\mathrm{d}p=\mathrm{d}q=0$：$p$ 是首次积分。令 $p=\cos\alpha$，得 $q=\sin\alpha$，积分 $\mathrm{d}u=\cos\alpha\,\mathrm{d}x+\sin\alpha\,\mathrm{d}y$ 得完全积分

$$
u=x\cos\alpha+y\sin\alpha+b,
$$
这是一族斜率为 $1$ 的平面。单参数子族 $b=0$ 的包络由 $\frac{\partial}{\partial\alpha}(x\cos\alpha+y\sin\alpha)=0$，即 $\tan\alpha=\frac yx$ 得到，为 $u=\pm\sqrt{x^2+y^2}$：到原点的距离，一个锥面。在几何光学中，$u$ 是光在均匀介质中的传播时间，它的等值线是波前，投影特征线（光线）是垂直于波前的直线。

**例 2.4.2** 求 $u_xu_y=u$ 的完全积分。

**解** 这里 $F=pq-u$，$F_p=q$，$F_q=p$，$F_u=-1$，$F_x=F_y=0$，式 (2.18) 的最后两个比式为 $\frac{\mathrm{d}p}{p}=\frac{\mathrm{d}q}{q}$。因此 $\frac pq=a$ 是首次积分。由 $p=aq$ 与 $pq=u$ 得 $q=\sqrt{u/a}$，$p=\sqrt{au}$（$a,u>0$），所以

$$
\mathrm{d}u=\sqrt{au}\,\mathrm{d}x+\sqrt{\frac ua}\,\mathrm{d}y,\qquad\frac{\mathrm{d}u}{\sqrt u}=\sqrt a\,\mathrm{d}x+\frac{\mathrm{d}y}{\sqrt a}.
$$
积分得 $2\sqrt u=\sqrt a\,x+\frac{y}{\sqrt a}+b$，即

$$
u=\frac{(ax+y+c)^2}{4a},\qquad c=b\sqrt a.
$$
验证：$u_x=\frac{ax+y+c}{2}$，$u_y=\frac{ax+y+c}{2a}$，二者之积为 $u$。

对 **Clairaut 方程** $u=xp+yq+f(p,q)$（[2.4.14](/2.4.14#sec-14.5)），式 (2.18) 直接给出 $\mathrm{d}p=\mathrm{d}q=0$，这解释了为什么它的完全积分是平面族 $u=ax+by+f(a,b)$。经典力学中的 Hamilton–Jacobi 方程 $S_t+H(x,\nabla S)=0$ 是同一类的完全非线性一阶方程；对它，特征方程组 (2.18) 恰好就是 Hamilton 运动方程。

## 小结

| 方程 | 特征线 | 解 |
|---|---|---|
| $u_t+cu_x=g$ | 直线 $x-ct=\text{常数}$ | $u=f(x-ct)+\int_0^tg(x-c(t-s),s)\,\mathrm{d}s$ |
| $u_t+a(x,t)u_x=0$ | 质点轨迹 $\frac{\mathrm{d}x}{\mathrm{d}t}=a$ | $u=f(x_0(x,t))$，沿特征线为常数 |
| $Pu_x+Qu_y=R$ | $\frac{\mathrm{d}x}{P}=\frac{\mathrm{d}y}{Q}=\frac{\mathrm{d}u}{R}$ | 通解 $G(\Psi_1,\Psi_2)=0$；数据满足非特征条件 $Py_0'-Qx_0'\ne0$ 时，Cauchy 问题在其附近可解 |
| $u_t+uu_x=0$ | 直线 $x=x_0+f(x_0)t$ | 在 $T^*=-1/\inf f'$ 之前 $u=f(x-ut)$；此后出现速度为 $\frac12(u_l+u_r)$ 的激波或扇形稀疏波 |
| $F(x,y,u,p,q)=0$ | 特征带，方程组 (2.18) | 用 Charpit 方法求完全积分；其他解作为包络得到 |

- 积分曲面是特征线的并（定理 2.2.1）；这既给出了解的构造，也给出了解的唯一性。
- 特征线上的数据不能任意给定；数据曲线与特征线横截，是 Cauchy 问题适定的关键。
- 对非线性方程，特征线依赖于解，可能相交；这时古典解不再存在，由守恒律的积分形式、Rankine–Hugoniot 条件与熵条件确定激波。
