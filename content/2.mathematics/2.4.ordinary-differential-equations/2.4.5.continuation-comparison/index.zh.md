---
title: 解的延伸与比较定理
---

上一章的 Picard 定理与 Peano 定理只保证解在初值点附近的区间 $\lvert x-x_0\rvert\le h$ 上存在，$h=\min\{a,b/M\}$ 取决于所选的矩形，往往远小于解实际存在的范围。本章把局部解延伸到整体：延伸定理说明，在 $f$ 连续的开区域内，积分曲线可以一直延伸到区域的边界，解的最大存在区间是开区间，在端点处解要么趋于无穷，要么趋于区域的边界；当 $f$ 关于 $y$ 至多线性增长时，解在整个区间上存在。为了估计最大存在区间，本章再建立比较定理：两个方程的右端有大小关系时，它们过同一点的解也有大小关系。没有唯一性时，比较要通过最大解与最小解来进行。本章的结论在 [2.4.7](/2.4.7) 中推广到方程组。

本章中 $G$ 是平面上的**区域**（连通开集），$f$ 在 $G$ 内连续。

## 5.1. 解的延伸

### 5.1.1. 饱和解与最大存在区间

**定义 5.1.1** 设 $y=\varphi(x)$ 是方程 $y'=f(x,y)$ 在区间 $J$ 上的解。若有解 $y=\psi(x)$ 定义在真包含 $J$ 的区间 $J_1$ 上，且在 $J$ 上 $\psi=\varphi$，则称 $\psi$ 是 $\varphi$ 的一个**延伸**。不能再延伸的解称为**饱和解**，它的定义区间称为**最大存在区间**。

没有唯一性时，同一个解可能有不同的饱和延伸，它们的最大存在区间也可能不同；有唯一性时饱和延伸唯一（推论 5.1.2）。

**引理 5.1.1** 饱和解的最大存在区间是开区间。

**证明** 设饱和解 $\varphi$ 的定义区间含有右端点 $\beta$。解的图形在 $G$ 内，所以 $(\beta,\varphi(\beta))\in G$，取以它为中心、含于 $G$ 的矩形，由 Peano 存在定理（定理 4.4.1），有 $[\beta,\beta+h_1]$ 上的解 $\chi$，$\chi(\beta)=\varphi(\beta)$。令 $\psi=\varphi$（$x\le\beta$），$\psi=\chi$（$x\ge\beta$），则 $\psi$ 在 $\beta$ 处的左、右导数都等于 $f(\beta,\varphi(\beta))$，所以 $\psi$ 是 $\varphi$ 的延伸，与饱和性矛盾。左端点同理。 $\square$

**引理 5.1.2（一致的局部存在）** 设 $K\subset G$ 是有界闭集，则存在只依赖于 $K$ 的 $\eta>0$，使对任意 $(\xi,\zeta)\in K$，满足 $y(\xi)=\zeta$ 的解在 $[\xi-\eta,\xi+\eta]$ 上存在。

**证明** $K$ 有界闭、$G$ 是开集，所以 $K$ 到 $G$ 的边界的距离 $d>0$（$G$ 为全平面时取 $d=1$）。到 $K$ 的距离不超过 $d/2$ 的点组成有界闭集 $K'\subset G$，记 $M'=\max_{K'}\lvert f\rvert+1$。对 $(\xi,\zeta)\in K$，取 $a=\dfrac{d}{2\sqrt2}$，正方形 $\lvert x-\xi\rvert\le a$，$\lvert y-\zeta\rvert\le a$ 中的点到 $(\xi,\zeta)$ 的距离不超过 $d/2$，所以含于 $K'$。由 Peano 存在定理，解在 $\lvert x-\xi\rvert\le\eta$ 上存在，$\eta=\min\{a,a/M'\}$ 与 $(\xi,\zeta)$ 无关。 $\square$

### 5.1.2. 延伸定理

**定理 5.1.1（延伸定理）** 设 $f$ 在区域 $G$ 内连续。

1. 方程 $y'=f(x,y)$ 的每个解都可以延伸为饱和解。
2. 设 $y=\varphi(x)$ 是饱和解，最大存在区间为 $(\alpha,\beta)$。则当 $x\to\beta^-$ 时，点 $(x,\varphi(x))$ 最终离开 $G$ 内的任何有界闭集：对任意有界闭集 $K\subset G$，存在 $x_K<\beta$，使 $x_K<x<\beta$ 时 $(x,\varphi(x))\notin K$。$x\to\alpha^+$ 时同样。

几何上，过 $G$ 内任一点的积分曲线可以向两侧一直延伸到 $G$ 的边界。"到达边界"包括三种情形：$\beta=+\infty$；$\varphi(x)$ 无界；积分曲线趋近 $G$ 的边界点。

**证明** 先证（2）。$\beta=+\infty$ 时，$K$ 中点的横坐标有界，结论显然。设 $\beta<+\infty$。

第一步：积分曲线不能在 $(\beta-\varepsilon,\beta)$ 上整个停留在 $K$ 内。否则 $\lvert\varphi'\rvert\le M_K=\max_K\lvert f\rvert$，$\lvert\varphi(x)-\varphi(x')\rvert\le M_K\lvert x-x'\rvert$，由 Cauchy 收敛准则，极限 $\gamma=\lim_{x\to\beta^-}\varphi(x)$ 存在，且 $(\beta,\gamma)\in K\subset G$（$K$ 是闭集）。令 $\varphi(\beta)=\gamma$，在积分方程 $\varphi(x)=\varphi(x_1)+\int_{x_1}^xf(t,\varphi(t))\,\mathrm{d}t$ 中令 $x\to\beta^-$，可知 $\varphi$ 在 $(\alpha,\beta]$ 上仍是解，与饱和性矛盾。

第二步：设结论不成立，则有 $x_j\to\beta^-$，$(x_j,\varphi(x_j))\in K$。取引理 5.1.2 证明中的 $d$ 与 $K'$，$M'=\max_{K'}\lvert f\rvert+1$。对 $K'$ 用第一步，存在 $t_j\in(x_j,\beta)$ 使点 $P(x)=(x,\varphi(x))$ 在 $[x_j,t_j)$ 上留在 $K'$ 内、而 $P(t_j)$ 到 $K$ 的距离等于 $d/2$（取第一个这样的点）。在 $[x_j,t_j]$ 上斜率不超过 $M'$，所以

$$
\frac d2\le\lvert P(t_j)-P(x_j)\rvert\le(t_j-x_j)\sqrt{1+M'^2}\le(\beta-x_j)\sqrt{1+M'^2}\to0,
$$
矛盾。

再证（1）。只讨论向右延伸。令 $K_m=\{(x,y)\in G\mid x^2+y^2\le m^2,\ (x,y)\text{ 到 }G\text{ 的边界的距离}\ge1/m\}$，则 $K_1\subset K_2\subset\cdots$ 都是 $G$ 内的有界闭集，并且 $G$ 内的每个有界闭集都含于某个 $K_m$（它到边界的距离为正）。设 $\eta_m$ 是引理 5.1.2 对 $K_m$ 给出的步长。从给定的解出发，按 $m=1,2,\dots$ 分轮延伸：第 $m$ 轮中，只要当前解的右端点 $(b,\varphi(b))$ 在 $K_m$ 内，就把过该点、在 $[b,b+\eta_m]$ 上存在的解拼接上去（像引理 5.1.1 那样拼接仍是解）。$K_m$ 中点的横坐标有界，所以每轮只进行有限步，结束时右端点不在 $K_m$ 中，然后进入下一轮。由此得到 $[x_0,\beta)$ 上的解 $\varphi$，$\beta$ 是各步右端点的极限（右端点不能在有限步后停止变化，因为它属于某个 $K_m$）。

若 $\varphi$ 还能延伸到 $[x_0,\beta]$，则它在 $[x_0,\beta]$ 上的图形是 $G$ 内的有界闭集，含于某个 $K_{m_0}$。但对每个 $m\ge m_0$，第 $m$ 轮结束时的右端点是 $\varphi$ 图形上横坐标小于 $\beta$ 的点，却不在 $K_m\supset K_{m_0}$ 中，矛盾。所以 $\varphi$ 向右不能延伸；向左同样处理，得到饱和解。 $\square$

**推论 5.1.1** 设 $f$ 在带形 $S=\{(x,y)\mid a<x<b,\ y\in\mathbb{R}\}$（$a$ 可为 $-\infty$，$b$ 可为 $+\infty$）上连续，饱和解 $\varphi$ 的最大存在区间为 $(\alpha,\beta)$。若 $\beta<b$，则 $x\to\beta^-$ 时 $\lvert\varphi(x)\rvert\to+\infty$；左端同理。

**证明** 对任意 $N>0$，$K=[x_0,\beta]\times[-N,N]$ 是 $S$ 内的有界闭集，由延伸定理，$x$ 接近 $\beta$ 时 $(x,\varphi(x))\notin K$，即 $\lvert\varphi(x)\rvert>N$。 $\square$

这就是"爆破"（blow-up）：解只能以趋于无穷的方式在带形内部结束。

**推论 5.1.2** 设 $f$ 在 $G$ 内连续且关于 $y$ 满足局部 Lipschitz 条件，则过 $G$ 内每一点恰有一个饱和解，同一初值问题的任意两个解在公共区间上相等。

**证明** 设 $\varphi_1,\varphi_2$ 是同一初值问题在区间 $J$ 上的解，$E=\{x\in J\mid\varphi_1(x)=\varphi_2(x)\}$。$E$ 非空且在 $J$ 中是闭集；对 $x_1\in E$，在点 $(x_1,\varphi_1(x_1))$ 附近用 Picard 定理（定理 4.2.1）的唯一性，$\varphi_1,\varphi_2$ 在 $x_1$ 的一个邻域内相等，所以 $E$ 也是开集。区间是连通的，$E=J$。于是所有解的并（在各自的区间上取值）定义了一个解，它就是唯一的饱和解。 $\square$

**例 5.1.1** $y'=y^2$ 的右端在全平面上连续可导，但解不一定在整个 $\mathbb{R}$ 上存在。满足 $y(0)=y_0$ 的饱和解为

$$
y=\frac{y_0}{1-y_0x},
$$
$y_0>0$ 时最大存在区间为 $(-\infty,1/y_0)$，$x\to(1/y_0)^-$ 时 $y\to+\infty$；$y_0<0$ 时为 $(1/y_0,+\infty)$；$y_0=0$ 时为 $\mathbb{R}$。最大存在区间因解而异，并且初值越大，解越早爆破。

![y' = y^2 的几条饱和解：从 y(0) = y_0 > 0 出发的解在 x = 1/y_0 处爆破（虚线），y_0 < 0 的解在 x = 1/y_0 处向左爆破，零解在整个实轴上存在](./plots/blow-up.py)

**例 5.1.2** 在上半平面 $G=\{y>0\}$ 内考虑 $y'=-\dfrac xy$。过 $(0,R)$ 的饱和解是半圆 $y=\sqrt{R^2-x^2}$，最大存在区间为 $(-R,R)$。这里解是有界的，$x\to\pm R$ 时积分曲线趋于 $G$ 的边界点 $(\pm R,0)$，在那里方程的右端没有定义。

### 5.1.3. 整体存在

当 $f$ 关于 $y$ 至多线性增长时，爆破不会发生。

**定理 5.1.2** 设 $f$ 在带形 $S=\{(x,y)\mid\alpha<x<\beta,\ y\in\mathbb{R}\}$ 上连续，且

$$
\lvert f(x,y)\rvert\le A(x)\lvert y\rvert+B(x),
$$
其中 $A(x),B(x)\ge0$ 在 $(\alpha,\beta)$ 上连续。则方程 $y'=f(x,y)$ 的每个饱和解都以 $(\alpha,\beta)$ 为最大存在区间。

**证明** 设饱和解 $\varphi$ 过 $(x_0,y_0)$，最大存在区间的右端点 $\beta_1<\beta$。$A,B$ 在 $[x_0,\beta_1]$ 上连续，取 $A_0=\max A+1$，$B_0=\max B$。对 $x\in[x_0,\beta_1)$，

$$
\lvert\varphi(x)\rvert\le\lvert y_0\rvert+\int_{x_0}^x\big(A_0\lvert\varphi(t)\rvert+B_0\big)\,\mathrm{d}t=:u(x).
$$
$u'=A_0\lvert\varphi\rvert+B_0\le A_0u+B_0$，所以 $\Big(\mathrm{e}^{-A_0(x-x_0)}\big(u+\frac{B_0}{A_0}\big)\Big)'\le0$，

$$
\lvert\varphi(x)\rvert\le u(x)\le\Big(\lvert y_0\rvert+\frac{B_0}{A_0}\Big)\mathrm{e}^{A_0(\beta_1-x_0)}.
$$
$\varphi$ 在 $\beta_1$ 附近有界，与推论 5.1.1 矛盾。左端点同理。 $\square$

证明中从积分不等式推出指数估计的论证，在 [2.4.7](/2.4.7) 中整理为 Gronwall 不等式。

**例 5.1.3** （1）一阶线性方程 $y'=p(x)y+q(x)$（$p,q$ 在 $(\alpha,\beta)$ 上连续）满足 $\lvert f\rvert\le\lvert p\rvert\lvert y\rvert+\lvert q\rvert$，它的解都在整个 $(\alpha,\beta)$ 上存在，这与 [2.2.15](/2.2.15) 中的通解公式一致；线性方程组的相应结论见 [2.4.8](/2.4.8)。（2）$y'=\sin(xy)$ 的右端有界，每个解都在 $\mathbb{R}$ 上存在。（3）例 5.1.1 的 $y^2$ 是超线性增长的，定理不适用，解确实会爆破。

## 5.2. 第一比较定理

只靠延伸定理往往不能估计最大存在区间，需要比较方程的线素场。比较定理是这类估计的一般原理。

**定理 5.2.1（第一比较定理）** 设 $f(x,y)$、$F(x,y)$ 在区域 $G$ 内连续，且

$$
f(x,y)<F(x,y),\qquad(x,y)\in G.
$$
又设 $y=\varphi(x)$ 与 $y=\Phi(x)$ 在区间 $(a,b)$ 上分别是初值问题

$$
y'=f(x,y),\ y(x_0)=y_0\qquad\text{与}\qquad y'=F(x,y),\ y(x_0)=y_0
$$
的解，$(x_0,y_0)\in G$。则

$$
\varphi(x)<\Phi(x)\quad(x_0<x<b),\qquad\varphi(x)>\Phi(x)\quad(a<x<x_0).
$$

**证明** 令 $g(x)=\Phi(x)-\varphi(x)$，则 $g(x_0)=0$，$g'(x_0)=F(x_0,y_0)-f(x_0,y_0)>0$，所以存在 $\delta>0$，使 $x_0<x<x_0+\delta$ 时 $g(x)>0$，$x_0-\delta<x<x_0$ 时 $g(x)<0$。

若右侧的结论不成立，$g$ 在 $(x_0,b)$ 中有零点，令 $\zeta$ 为最小的零点（零点集是闭集，且与 $x_0$ 的距离不小于 $\delta$），则 $g>0$ 于 $(x_0,\zeta)$，$g(\zeta)=0$，所以 $g'(\zeta)=\lim\limits_{x\to\zeta^-}\dfrac{g(x)}{x-\zeta}\le0$。另一方面，记 $\gamma=\varphi(\zeta)=\Phi(\zeta)$，

$$
g'(\zeta)=F(\zeta,\gamma)-f(\zeta,\gamma)>0,
$$
矛盾。左侧类似：若 $g$ 在 $(a,x_0)$ 中有零点，取最大的零点 $\zeta$，则 $g<0$ 于 $(\zeta,x_0)$，$g'(\zeta)=\lim\limits_{x\to\zeta^+}\dfrac{g(x)}{x-\zeta}\le0$，同样矛盾。 $\square$

几何上：在两条积分曲线的交点处，$y'=F$ 的积分曲线总是更陡，所以它只能从下方穿到上方，交过一次之后再也回不来。同样的论证给出初值不同的情形。

**推论 5.2.1** 在定理 5.2.1 的条件下，若 $\varphi(x_0)<\Phi(x_0)$（不再要求初值相同），则 $\varphi(x)<\Phi(x)$ 对 $x_0<x<b$ 成立。

**证明** $g=\Phi-\varphi$ 在 $x_0$ 处为正。若它在 $(x_0,b)$ 中有零点，取最小的零点 $\zeta$，与定理的证明一样得到矛盾。 $\square$

严格不等式 $f<F$ 不能减弱为 $f\le F$：取 $f=F=\lvert y\rvert^{1/2}$，由例 4.3.1，过原点的两个不同的解没有确定的大小关系。在 $f\le F$ 的条件下要比较，需要从众多的解中选出最大解和最小解。

## 5.3. 最大解与最小解

**定义 5.3.1** 设 $f$ 在矩形 $R$ 上连续，$y=Z(x)$ 是初值问题 $y'=f(x,y)$，$y(x_0)=y_0$（式 (4.1)）在 $[x_0,x_0+\sigma]$ 上的解。若 (4.1) 在任一区间 $[x_0,c]\subset[x_0,x_0+\sigma]$ 上的任一解 $y$ 都满足 $y\le Z$，则称 $Z$ 是 (4.1) 的**右行最大解**；把 $\le$ 换成 $\ge$，称为**右行最小解**。在 $[x_0-\sigma,x_0]$ 上同样定义左行最大解与左行最小解。在 $[x_0-\sigma,x_0+\sigma]$ 上的解若在两侧都是最大（最小）的，就称为 (4.1) 的**最大解**（**最小解**）。

由定义，最大解与最小解若存在则唯一。

**定理 5.3.1** 设 $f$ 在矩形 $R$ 上连续，$\sigma=\min\{a,b/(M+1)\}$，则初值问题 (4.1) 在 $[x_0-\sigma,x_0+\sigma]$ 上存在最大解 $Z$ 与最小解 $W$，并且 (4.1) 在其子区间上的任一解 $y$ 满足

$$
W(x)\le y(x)\le Z(x).
$$

**证明** 对 $m=1,2,\dots$ 考虑初值问题 $y'=f(x,y)+\dfrac1m$，$y(x_0)=y_0$。在 $R$ 上 $\lvert f+\frac1m\rvert\le M+1$，由 Peano 存在定理，它在 $[x_0-\sigma,x_0+\sigma]$ 上有解 $Z_m$，图形在 $R$ 内。$\{Z_m\}$ 一致有界且有共同的 Lipschitz 常数 $M+1$，由 Ascoli 引理（引理 4.4.2），有子序列一致收敛到某个 $\tilde Z$；$f+\frac1m$ 一致收敛到 $f$，与定理 4.4.1 的证明一样，$\tilde Z$ 是 (4.1) 的解。

设 $y$ 是 (4.1) 在 $[x_0,c]$ 上的任一解。由 $f<f+\frac1m$ 和第一比较定理（它的证明只用到初值点附近与交点处的局部性质，对 $R$ 同样适用），$y<Z_m$ 于 $(x_0,c]$，取极限得 $y\le\tilde Z$。在左侧，第一比较定理给出 $y>Z_m$，所以 $y\ge\tilde Z$。因此 $\tilde Z$ 是右行最大解、同时是左行最小解。

同样，用 $y'=f-\frac1m$ 的解的极限得到 $\tilde W$，它是右行最小解、左行最大解。令 $Z$ 在右侧取 $\tilde Z$、左侧取 $\tilde W$，$W$ 在右侧取 $\tilde W$、左侧取 $\tilde Z$。它们在 $x_0$ 处都取值 $y_0$，两侧都满足积分方程 (4.2)，所以都是 (4.1) 的解，分别是最大解和最小解。 $\square$

由定理，(4.1) 的解唯一当且仅当 $Z\equiv W$。最大解与最小解也可以像定理 5.1.1 那样延伸到 $G$ 的边界；并且所有解在 $x$ 处的取值恰好填满区间 $[W(x),Z(x)]$（Kneser 定理）：对例 4.3.1 中的 $y'=\lvert y\rvert^{1/2}$，$Z$ 与 $W$ 就是图中最早离开 $x$ 轴的两条曲线，其余的解充满它们之间的"漏斗"。

## 5.4. 第二比较定理

**引理 5.4.1** 设 $F$ 在区域 $G$ 内连续，$\Phi$ 是初值问题 $y'=F(x,y)$，$y(x_0)=y_0$ 在 $[x_0,x_1]$ 上的右行最大解。设 $\Phi_m$ 是 $y'=F(x,y)+\dfrac1m$，$y(x_0)=y_0$ 的饱和解，则 $m$ 充分大时 $\Phi_m$ 在 $[x_0,x_1]$ 上存在，并且在 $[x_0,x_1]$ 上一致收敛到 $\Phi$。

**证明** $\Phi$ 的图形是 $G$ 内的有界闭集，可取 $d>0$，使"管子" $K=\{(x,y)\mid x_0\le x\le x_1,\ \lvert y-\Phi(x)\rvert\le d\}\subset G$。记 $M_K=\max_K\lvert F\rvert+1$。令 $c_m$ 为使 $\Phi_m$ 在 $[x_0,c)$ 上的图形留在 $K$ 内的最大的 $c\le x_1$。因为 $\lvert\Phi_m-\Phi\rvert\le2M_K(x-x_0)$ 在 $K$ 内成立，$c_m\ge x_0+\tau$，$\tau=\min\{d/(2M_K),x_1-x_0\}$ 与 $m$ 无关。

先证 $\varepsilon_m=\sup_{[x_0,c_m)}\lvert\Phi_m-\Phi\rvert\to0$。若不然，有子序列使 $\varepsilon_m\ge\varepsilon>0$ 且 $c_m\to c^*$。把 $\Phi_m$ 在 $c_m$ 之后延拓为常数，得到 $[x_0,x_1]$ 上一致有界、Lipschitz 常数为 $M_K$ 的序列，由 Ascoli 引理再取子序列一致收敛到 $\psi$。对 $x<c^*$，$m$ 充分大时 $x<c_m$，在 $\Phi_m$ 的积分方程中取极限，可知 $\psi$ 在 $[x_0,c^*]$ 上是 $y'=F$，$y(x_0)=y_0$ 的解，由最大性 $\psi\le\Phi$；另一方面由第一比较定理 $\Phi<\Phi_m$，故 $\psi\ge\Phi$。所以在 $[x_0,c^*]$ 上 $\psi=\Phi$。于是在 $[x_0,c_m)$ 上

$$
\lvert\Phi_m-\Phi\rvert\le\lvert\Phi_m-\psi\rvert+\lvert\psi-\Phi\rvert\le\lvert\Phi_m-\psi\rvert+2M_K\lvert c_m-c^*\rvert\to0
$$
一致成立，与 $\varepsilon_m\ge\varepsilon$ 矛盾。

再证 $m$ 充分大时 $c_m=x_1$ 且 $\Phi_m$ 在 $x_1$ 处有定义：取 $m$ 使 $\varepsilon_m<d/2$，则 $\Phi_m$ 的图形在 $[x_0,c_m)$ 上留在较小的管子 $\lvert y-\Phi\rvert\le d/2$ 中，由延伸定理，$\Phi_m$ 的最大存在区间越过 $c_m$，并由连续性在 $c_m$ 之后仍留在 $K$ 中一小段，除非 $c_m=x_1$。 $\square$

**定理 5.4.1（第二比较定理）** 设 $f(x,y)$、$F(x,y)$ 在区域 $G$ 内连续，且

$$
f(x,y)\le F(x,y),\qquad(x,y)\in G.
$$
设 $y=\varphi(x)$ 在 $(a,b)$ 上是 $y'=f(x,y)$，$y(x_0)=y_0$ 的解，$y=\Phi(x)$ 在 $(a,b)$ 上是 $y'=F(x,y)$，$y(x_0)=y_0$ 的右行最大解和左行最小解（在 $(a,b)$ 的每个包含 $x_0$ 的有界闭子区间上），则

$$
\varphi(x)\le\Phi(x)\quad(x_0\le x<b),\qquad\varphi(x)\ge\Phi(x)\quad(a<x\le x_0).
$$
若改设 $\varphi$ 是 $y'=f$ 的右行最小解和左行最大解（对 $\Phi$ 不作要求），结论同样成立。

**证明** 任取 $x_1\in(x_0,b)$。由引理 5.4.1，$y'=F+\frac1m$ 的解 $\Phi_m$ 在 $[x_0,x_1]$ 上一致收敛到 $\Phi$。因为 $f\le F<F+\frac1m$，由第一比较定理 $\varphi<\Phi_m$ 于 $(x_0,x_1]$，令 $m\to\infty$ 得 $\varphi\le\Phi$。左侧的论证对称：由第一比较定理，$\Phi_m$ 在左侧小于 $y'=F$ 的任何解，引理 5.4.1 的对称形式说明它们收敛到左行最小解 $\Phi$，而 $\varphi>\Phi_m$，取极限得 $\varphi\ge\Phi$。第二种假设下，改用 $y'=f-\frac1m$ 的解逼近 $\varphi$。 $\square$

当解唯一时，唯一的解自然既是最大解也是最小解，于是得到最常用的形式。

**推论 5.4.1** 设 $f\le F$ 在 $G$ 内连续，且 $f$ 与 $F$ 之一关于 $y$ 满足局部 Lipschitz 条件。若 $\varphi$、$\Phi$ 分别是 $y'=f$ 与 $y'=F$ 过 $(x_0,y_0)$ 的解，则在公共区间上，$x\ge x_0$ 时 $\varphi\le\Phi$，$x\le x_0$ 时 $\varphi\ge\Phi$。

**例 5.4.1** 估计初值问题 $y'=x^2+y^2$，$y(0)=0$ 的最大存在区间 $(\alpha,\beta)$。右端连续可导，解 $\varphi$ 唯一；$-\varphi(-x)$ 也是同一初值问题的解，所以 $\varphi$ 是奇函数，$\alpha=-\beta$。$x>0$ 时 $\varphi'\ge x^2>0$，所以 $\varphi(x)>0$。

下界：任取 $0<x_1<\sqrt{\pi/2}$，在带形 $G=\{\lvert x\rvert<x_1\}$ 内 $x^2+y^2\le x_1^2+y^2$，而 $y'=x_1^2+y^2$，$y(0)=0$ 的解 $\Phi=x_1\tan(x_1x)$ 在 $[0,x_1]$ 上有界（因为 $x_1^2<\pi/2$）。由推论 5.4.1，在 $[0,\min\{\beta,x_1\})$ 上 $0<\varphi\le\Phi$。若 $\beta<x_1$，$\varphi$ 在 $\beta$ 附近有界，与推论 5.1.1 矛盾，所以 $\beta\ge x_1$，从而 $\beta\ge\sqrt{\pi/2}\approx1.253$。

上界：由 $\varphi'\ge x^2$ 得 $\varphi(1)\ge\dfrac13$。在 $G=\{x>0\}$ 内取 $f(x,y)=\min\{x^2,1\}+y^2\le x^2+y^2$，它在 $x\ge1$ 时就是 $1+y^2$。$y'=1+y^2$，$y(1)=\varphi(1)$ 的解

$$
\psi=\tan\big(x-1+\arctan\varphi(1)\big)
$$
在 $x^*=1+\dfrac\pi2-\arctan\varphi(1)$ 处趋于 $+\infty$。由推论 5.4.1，$x\ge1$ 时 $\varphi\ge\psi$，所以 $\varphi$ 不能越过 $x^*$：

$$
\beta\le1+\frac\pi2-\arctan\frac13\approx2.249.
$$
数值计算给出 $\beta\approx2.003$。这个解不能用初等函数表示（它可以用 Bessel 函数表示），比较定理却直接给出了存在区间的两侧估计。

![y' = x^2 + y^2, y(0) = 0 的解（数值解）夹在两个比较函数之间：上方的 x_1 tan(x_1 x)（x_1 = 1.25）说明解至少存在到 sqrt(pi/2)，下方从 x = 1 出发的 tan(x - 1 + arctan phi(1)) 说明解在 2.249 之前爆破](./plots/comparison-bounds.py)

## 小结

| 结论 | 条件 | 用途 |
|---|---|---|
| 延伸定理（定理 5.1.1） | $f$ 在开区域 $G$ 内连续 | 饱和解的积分曲线延伸到 $G$ 的边界 |
| 爆破（推论 5.1.1） | $G$ 为带形 | 在带形内部结束的解必趋于无穷 |
| 整体存在（定理 5.1.2） | $\lvert f\rvert\le A(x)\lvert y\rvert+B(x)$ | 解在整个区间上存在 |
| 第一比较定理（定理 5.2.1） | $f<F$ | 过同一点的解：右侧 $\varphi<\Phi$，左侧 $\varphi>\Phi$ |
| 最大解与最小解（定理 5.3.1） | $f$ 连续 | 所有解夹在 $W$ 与 $Z$ 之间 |
| 第二比较定理（定理 5.4.1） | $f\le F$，与最大（小）解比较 | 估计解与最大存在区间 |
