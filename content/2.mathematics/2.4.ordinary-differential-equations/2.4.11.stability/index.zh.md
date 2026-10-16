---
title: 稳定性与定性理论
---

绝大多数非线性方程求不出解的表达式，但应用中关心的往往不是解的公式，而是解的长期行为：平衡状态受到小扰动后能否恢复，系统是否会进入持续的振荡，轨线最终趋向哪里。定性理论不求解方程，直接从方程本身回答这些问题。这一思想由 Poincaré 与 Lyapunov 在 19 世纪末开创，今天是动力系统、控制理论与数学生物学的基础。

本章先给出 Lyapunov 稳定性的定义，用上一章的线性理论（[2.4.8](/2.4.8)）完全刻画常系数线性系统的稳定性，并给出只看特征多项式系数的 Routh–Hurwitz 判据；再证明非线性系统的平衡点可以按线性近似判断稳定性（Lyapunov 第一方法），以及不需要线性化的 Lyapunov 函数法（第二方法）。后半部分讨论平面自治系统：相平面与轨线、平面线性系统奇点的分类、极限环与 Poincaré–Bendixson 定理，以 van der Pol 方程为例。种群竞争与捕食者—猎物模型中的平衡点与相图（[7.4.4](/7.4.4)）是这些方法的直接应用。

## 11.1. Lyapunov 稳定性

### 11.1.1. 定义

考虑方程组

$$
\boldsymbol{x}'=\boldsymbol{f}(t,\boldsymbol{x}),\tag{11.1}
$$
设 $\boldsymbol{f}$ 在 $t\ge t_0$、$\|\boldsymbol{x}\|<H$ 上连续，且关于 $\boldsymbol{x}$ 满足局部 **Lipschitz 条件**，于是初值问题的解存在唯一（[2.4.4](/2.4.4)、[2.4.7](/2.4.7)）。要研究的是某个已知解 $\boldsymbol{\varphi}(t)$ 在初值扰动下的行为。令 $\boldsymbol{y}=\boldsymbol{x}-\boldsymbol{\varphi}(t)$，则 $\boldsymbol{y}'=\boldsymbol{f}(t,\boldsymbol{y}+\boldsymbol{\varphi})-\boldsymbol{f}(t,\boldsymbol{\varphi})$，右端在 $\boldsymbol{y}=\boldsymbol{0}$ 处为零，$\boldsymbol{\varphi}$ 对应零解。所以总可以假设 $\boldsymbol{f}(t,\boldsymbol{0})\equiv\boldsymbol{0}$，研究零解 $\boldsymbol{x}\equiv\boldsymbol{0}$。记 $\boldsymbol{x}(t;t_0,\boldsymbol{x}_0)$ 为满足 $\boldsymbol{x}(t_0)=\boldsymbol{x}_0$ 的解。

**定义 11.1.1** 设 $\boldsymbol{f}(t,\boldsymbol{0})\equiv\boldsymbol{0}$。

1. 若对任意 $\varepsilon>0$，存在 $\delta>0$，使 $\|\boldsymbol{x}_0\|<\delta$ 时解 $\boldsymbol{x}(t;t_0,\boldsymbol{x}_0)$ 在 $[t_0,+\infty)$ 上存在且 $\|\boldsymbol{x}(t;t_0,\boldsymbol{x}_0)\|<\varepsilon$（$t\ge t_0$），则称零解是 **Lyapunov 稳定**的（简称稳定）；
2. 若零解稳定，且存在 $\delta_0>0$ 使 $\|\boldsymbol{x}_0\|<\delta_0$ 时 $\lim_{t\to+\infty}\boldsymbol{x}(t;t_0,\boldsymbol{x}_0)=\boldsymbol{0}$，则称零解**渐近稳定**；
3. 零解不稳定时称为不稳定的。

稳定性说的是"初值的小扰动在整个无穷时间区间上只引起解的小偏离"，它比解对初值的连续依赖性（只在有限区间上成立，[2.4.7](/2.4.7)）强得多。

**例 11.1.1** 下面是几个一维的例子。

- $x'=-x$：$x=x_0\mathrm{e}^{-(t-t_0)}$，零解渐近稳定；
- $x'=0$：$x\equiv x_0$，稳定但不渐近稳定；
- $x'=x$：$x=x_0\mathrm{e}^{t-t_0}$，不稳定；
- $x'=-x^3$：$x^{-2}=x_0^{-2}+2(t-t_0)$，$\lvert x\rvert$ 单调减少到 $0$，渐近稳定，但衰减比指数慢；$x'=x^3$ 的零解不稳定（解在有限时间内爆破）。

后两个方程的线性近似都是 $x'=0$，说明线性近似有时不能决定稳定性（定理 11.4.1 的临界情形）。

渐近稳定的定义中"稳定"一条不能省略：存在平面自治系统，所有解都趋于原点，但从原点任意近处出发的某些解会先远离到固定距离再回来（Vinograd 的例子）。

### 11.1.2. 线性系统的稳定性

对线性方程组 $\boldsymbol{x}'=A(t)\boldsymbol{x}+\boldsymbol{f}(t)$，两个解之差满足齐次方程组，所以任一解的稳定性与齐次方程组零解的稳定性相同，可以说"线性系统稳定"。

**定理 11.1.1** 设 $A(t)$ 在 $[t_0,+\infty)$ 上连续，$\Phi(t)$ 是 $\boldsymbol{x}'=A(t)\boldsymbol{x}$ 的基解矩阵。则零解

1. 稳定 $\Leftrightarrow$ 所有解在 $[t_0,+\infty)$ 上有界 $\Leftrightarrow$ $\Phi(t)$ 在 $[t_0,+\infty)$ 上有界；
2. 渐近稳定 $\Leftrightarrow$ 所有解在 $t\to+\infty$ 时趋于 $\boldsymbol{0}$ $\Leftrightarrow$ $\Phi(t)\to O$。

**证明** 解为 $\boldsymbol{x}(t)=\Phi(t)\Phi^{-1}(t_0)\boldsymbol{x}_0$。若 $\|\Phi(t)\|\le K$，则 $\|\boldsymbol{x}(t)\|\le K\|\Phi^{-1}(t_0)\|\,\|\boldsymbol{x}_0\|$，取 $\delta=\varepsilon/(K\|\Phi^{-1}(t_0)\|+1)$ 即得稳定。反之若零解稳定，取 $\varepsilon=1$ 对应的 $\delta$，则对 $\|\boldsymbol{x}_0\|<\delta$ 有 $\|\boldsymbol{x}(t)\|<1$，由线性，任一解都有界，$\Phi$ 的各列有界。2 同理：线性系统中"小初值的解趋于零"等价于"所有解趋于零"。 $\square$

对常系数方程组，$\Phi=\mathrm{e}^{tA}$ 的结构由推论 8.5.1 给出，于是：

**定理 11.1.2** 常系数方程组 $\boldsymbol{x}'=A\boldsymbol{x}$ 的零解

1. 渐近稳定 $\Leftrightarrow$ $A$ 的所有**特征值**的实部都是负的；此时存在 $C,\alpha>0$ 使 $\|\mathrm{e}^{tA}\|\le C\mathrm{e}^{-\alpha t}$（$t\ge0$），称为指数稳定；
2. 稳定 $\Leftrightarrow$ 所有特征值的实部 $\le0$，且实部为零的特征值都是**半单特征值**（对应的 Jordan 块都是一阶的）；
3. 其余情形不稳定。

**证明** 由推论 8.5.1，$\mathrm{e}^{tA}$ 的元素是 $t^k\mathrm{e}^{\lambda_jt}$ 的线性组合，$k$ 小于 $\lambda_j$ 的最大 Jordan 块的阶数。若所有 $\operatorname{Re}\lambda_j<0$，取 $0<\alpha<-\max\operatorname{Re}\lambda_j$，由推论 8.5.1 的估计（$\varepsilon=-\max\operatorname{Re}\lambda_j-\alpha$）得指数估计。若实部 $\le0$ 且纯虚特征值只有一阶块，每一项有界。反过来，若某个 $\operatorname{Re}\lambda>0$，特征向量 $\boldsymbol{r}$ 给出解 $\mathrm{e}^{\lambda t}\boldsymbol{r}$，无界；若某个 $\operatorname{Re}\lambda=0$ 的 $\lambda$ 有二阶以上的 Jordan 块，Jordan 链给出解 $\mathrm{e}^{\lambda t}(t\boldsymbol{p}_1+\boldsymbol{p}_2)$，无界；若某个 $\operatorname{Re}\lambda\ge0$，$\mathrm{e}^{\lambda t}\boldsymbol{r}$ 不趋于零。由定理 11.1.1 得结论。 $\square$

$n$ 阶常系数方程 $y^{(n)}+a_1y^{(n-1)}+\cdots+a_ny=0$ 的稳定性指方程组 $\boldsymbol{x}=(y,\dots,y^{(n-1)})^{\mathsf T}$ 的稳定性。友矩阵的每个特征值只有一个 Jordan 块（命题 9.4.1），所以：所有解（连同各阶导数）趋于零 $\Leftrightarrow$ 所有**特征根**实部为负；所有解有界 $\Leftrightarrow$ 特征根实部 $\le0$ 且实部为零的特征根都是单根。

**例 11.1.2** 对 $y''+py'+qy=0$（$p,q$ 为实常数），讨论解在 $x\to+\infty$ 时的行为。特征根 $\lambda_{1,2}=-\frac p2\pm\sqrt{\Delta}$，$\Delta=\frac{p^2-4q}{4}$。

1. 所有解 $\to0$ $\Leftrightarrow$ $p>0$ 且 $q>0$。$\Delta>0$ 时两个实根同为负 $\Leftrightarrow$ 和 $-p<0$、积 $q>0$；$\Delta=0$ 时二重根 $-\frac p2<0$ $\Leftrightarrow$ $p>0$（此时 $q=\frac{p^2}4>0$）；$\Delta<0$ 时实部 $-\frac p2<0$ $\Leftrightarrow$ $p>0$，而 $\Delta<0$ 蕴含 $q>0$。
2. 所有解在 $[0,+\infty)$ 上有界 $\Leftrightarrow$ $p\ge0$，$q\ge0$，且 $p,q$ 不同时为零。比 1 多出的情形是 $p=0,q>0$（根 $\pm\mathrm{i}\sqrt q$，单根）与 $p>0,q=0$（根 $0,-p$，$0$ 是单根）；$p=q=0$ 时有解 $y=x$。
3. 所有解在 $(-\infty,+\infty)$ 上有界 $\Leftrightarrow$ $p=0$ 且 $q>0$。由 2 对 $x$ 与 $-x$（方程变为 $y''-py'+qy=0$）分别应用，需要 $p\ge0$、$-p\ge0$ 且 $q\ge0$，$(p,q)\ne(0,0)$，即 $p=0,q>0$；此时 $y=A\sin(\sqrt q\,x+\theta)$ 是周期函数，确实有界。

## 11.2. Routh–Hurwitz 判据

由定理 11.1.2，常系数方程的渐近稳定性归结为特征多项式的根是否都在左半平面。不求根就能判断这一点的方法是 Routh–Hurwitz 判据。

**定义 11.2.1** 所有根的实部都为负的实系数多项式称为**稳定多项式**（Hurwitz 多项式）。

**命题 11.2.1** 若 $f(\lambda)=\lambda^n+a_1\lambda^{n-1}+\cdots+a_n$ 是稳定多项式，则所有 $a_k>0$。

**证明** 实系数多项式分解为一次因式 $\lambda+c$（实根 $-c<0$，$c>0$）与二次因式 $(\lambda-\alpha)^2+\beta^2=\lambda^2-2\alpha\lambda+\alpha^2+\beta^2$（复根 $\alpha\pm\mathrm{i}\beta$，$\alpha<0$）的乘积，每个因式的系数都是正的，乘积的系数也都是正的。 $\square$

$n\le2$ 时条件也是充分的（例 11.1.2），$n\ge3$ 时不充分：$\lambda^3+\lambda^2+\lambda+1=(\lambda+1)(\lambda^2+1)$ 有纯虚根。

**定理 11.2.1（Hurwitz）** 设 $f(\lambda)=\lambda^n+a_1\lambda^{n-1}+\cdots+a_n$ 为实系数多项式，记 $a_0=1$，$k<0$ 或 $k>n$ 时 $a_k=0$。作 $n$ 阶 Hurwitz 矩阵 $H=(a_{2i-j})_{i,j=1}^n$：

$$
H=\begin{bmatrix}a_1&a_0&0&0&\cdots&0\\a_3&a_2&a_1&a_0&\cdots&0\\a_5&a_4&a_3&a_2&\cdots&0\\\vdots&\vdots&\vdots&\vdots&&\vdots\\0&0&0&0&\cdots&a_n\end{bmatrix}.
$$
则 $f$ 是稳定多项式，当且仅当 $H$ 的顺序主子式全为正：

$$
\Delta_1=a_1>0,\quad\Delta_2=\begin{vmatrix}a_1&1\\a_3&a_2\end{vmatrix}>0,\quad\Delta_3=\begin{vmatrix}a_1&1&0\\a_3&a_2&a_1\\a_5&a_4&a_3\end{vmatrix}>0,\quad\dots,\quad\Delta_n=a_n\Delta_{n-1}>0.
$$

证明较长，依赖于复变函数中的辐角原理或 Sturm 序列，此处从略。$H$ 的最后一列只有右下角的 $a_n$ 非零，所以 $\Delta_n=a_n\Delta_{n-1}$。

**例 11.2.1** 低次多项式的稳定性条件：

| $n$ | $f(\lambda)$ 是稳定多项式的充要条件 |
|---|---|
| 2 | $a_1>0$，$a_2>0$ |
| 3 | $a_1>0$，$a_3>0$，$a_1a_2>a_3$ |
| 4 | $a_1>0$，$a_4>0$，$a_1a_2>a_3$，$a_1a_2a_3>a_1^2a_4+a_3^2$ |
| 5 | $a_1>0$，$a_5>0$，$a_1a_2>a_3$，$a_1(a_2a_3-a_1a_4+a_5)>a_3^2$，$a_1(a_2a_3a_4-a_2^2a_5-a_1a_4^2+2a_4a_5)-a_3^2a_4+a_2a_3a_5-a_5^2>0$ |

例如 $n=3$：$\Delta_2=a_1a_2-a_3$，$\Delta_3=a_3\Delta_2$，三个条件 $a_1>0$、$\Delta_2>0$、$a_3>0$ 已经蕴含 $a_2>0$。一般地，$n$ 次多项式的稳定性由 $n$ 个独立的不等式刻画。

实际计算中常用等价的 Routh 表：第一、二行依次写 $a_0,a_2,a_4,\dots$ 与 $a_1,a_3,a_5,\dots$，以后每一行由它上面的两行算出：若这两行依次为 $u_1,u_2,\dots$ 与 $v_1,v_2,\dots$，新的一行为 $w_i=\dfrac{v_1u_{i+1}-u_1v_{i+1}}{v_1}$（缺项记为 0）；$f$ 稳定当且仅当表的第一列（共 $n+1$ 个数）全为正。

**例 11.2.2** 求 $y'''+2y''+3y'+ky=0$ 渐近稳定的条件。$a_1=2$，$a_2=3$，$a_3=k$，条件为 $k>0$ 且 $2\cdot3>k$，即 $0<k<6$。用 Routh 表：

$$
\begin{matrix}1&3\\2&k\\\frac{6-k}{2}&0\\k&\end{matrix}
$$
第一列 $1,2,\frac{6-k}2,k$ 全为正，同样得 $0<k<6$。$k=6$ 时 $f(\lambda)=(\lambda+2)(\lambda^2+3)$，有纯虚根 $\pm\sqrt3\,\mathrm{i}$，解中出现持续的振荡；这是控制系统中增益过大导致失稳的典型情形。

## 11.3. 按线性近似判定稳定性

设方程组可以写成

$$
\boldsymbol{x}'=A\boldsymbol{x}+\boldsymbol{g}(t,\boldsymbol{x}),\qquad\|\boldsymbol{g}(t,\boldsymbol{x})\|\le\gamma(\|\boldsymbol{x}\|)\,\|\boldsymbol{x}\|,\quad\lim_{r\to0^+}\gamma(r)=0,\tag{11.2}
$$
即 $\boldsymbol{g}$ 关于 $t$ 一致地是 $o(\|\boldsymbol{x}\|)$；$A$ 是常数矩阵，$\boldsymbol{g}$ 连续且关于 $\boldsymbol{x}$ 局部 Lipschitz。$\boldsymbol{x}'=A\boldsymbol{x}$ 称为 (11.2) 的线性近似（一次近似）。

**定理 11.3.1（Lyapunov 第一方法）** 

1. 若 $A$ 的所有特征值实部为负，则 (11.2) 的零解渐近稳定，并且存在 $\delta,C,\beta>0$，使 $\|\boldsymbol{x}_0\|<\delta$ 时 $\|\boldsymbol{x}(t)\|\le C\|\boldsymbol{x}_0\|\mathrm{e}^{-\beta(t-t_0)}$；
2. 若 $A$ 有实部为正的特征值，则 (11.2) 的零解不稳定；
3. 若所有特征值实部 $\le0$ 且有实部为零的，线性近似不能判定（临界情形）。

**证明** 1：由定理 11.1.2，存在 $C\ge1$、$\alpha>0$ 使 $\|\mathrm{e}^{tA}\|\le C\mathrm{e}^{-\alpha t}$（$t\ge0$）。取 $r_0>0$ 使 $\gamma(r)\le\frac{\alpha}{2C}$（$0<r\le r_0$），令 $\delta=r_0/C$。设 $\|\boldsymbol{x}_0\|<\delta$，只要解满足 $\|\boldsymbol{x}(s)\|\le r_0$（$t_0\le s\le t$），由常数变易公式 (8.5)，

$$
\|\boldsymbol{x}(t)\|\le C\mathrm{e}^{-\alpha(t-t_0)}\|\boldsymbol{x}_0\|+\int_{t_0}^tC\mathrm{e}^{-\alpha(t-s)}\frac{\alpha}{2C}\|\boldsymbol{x}(s)\|\,\mathrm{d}s.
$$
令 $u(t)=\mathrm{e}^{\alpha(t-t_0)}\|\boldsymbol{x}(t)\|$，得 $u(t)\le C\|\boldsymbol{x}_0\|+\frac\alpha2\int_{t_0}^tu(s)\,\mathrm{d}s$。由 Gronwall 不等式（[2.4.7](/2.4.7)）$u(t)\le C\|\boldsymbol{x}_0\|\mathrm{e}^{\frac\alpha2(t-t_0)}$，即

$$
\|\boldsymbol{x}(t)\|\le C\|\boldsymbol{x}_0\|\mathrm{e}^{-\frac\alpha2(t-t_0)}<r_0.
$$
所以解永远不会到达球面 $\|\boldsymbol{x}\|=r_0$（若首次到达的时刻为 $t_1$，则在 $[t_0,t_1]$ 上上式成立，$\|\boldsymbol{x}(t_1)\|<r_0$，矛盾）；由解的延伸定理（[2.4.5](/2.4.5)），解在 $[t_0,+\infty)$ 上存在，估计对一切 $t\ge t_0$ 成立，$\beta=\frac\alpha2$。稳定性：对 $\varepsilon>0$ 取 $\delta'=\min(r_0,\varepsilon)/C$。

2 的证明用下一节的不稳定性定理，构造二次型的 Lyapunov 函数，从略；3 见例 11.1.1 与例 11.4.2。 $\square$

对自治系统 $\boldsymbol{x}'=\boldsymbol{f}(\boldsymbol{x})$，$\boldsymbol{f}\in C^1$。

**定义 11.3.1** 满足 $\boldsymbol{f}(\boldsymbol{x}^*)=\boldsymbol{0}$ 的点 $\boldsymbol{x}^*$ 称为自治系统的**平衡点**（奇点），$\boldsymbol{x}\equiv\boldsymbol{x}^*$ 是常数解。若 **Jacobi 矩阵** $D\boldsymbol{f}(\boldsymbol{x}^*)$ 没有实部为零的特征值，称 $\boldsymbol{x}^*$ 为**双曲平衡点**。

令 $\boldsymbol{y}=\boldsymbol{x}-\boldsymbol{x}^*$，由 Taylor 公式 $\boldsymbol{f}(\boldsymbol{x}^*+\boldsymbol{y})=D\boldsymbol{f}(\boldsymbol{x}^*)\boldsymbol{y}+o(\|\boldsymbol{y}\|)$，满足 (11.2)。所以：

**推论 11.3.1** 设 $\boldsymbol{f}\in C^1$，$\boldsymbol{x}^*$ 是平衡点。若 $D\boldsymbol{f}(\boldsymbol{x}^*)$ 的所有特征值实部为负，则 $\boldsymbol{x}^*$ 渐近稳定；若有实部为正的特征值，则 $\boldsymbol{x}^*$ 不稳定。

双曲平衡点附近，非线性系统的轨线结构与线性近似的在拓扑意义下相同（Hartman–Grobman 定理，陈述）。

**例 11.3.1** 有阻尼的单摆 $\theta''+k\theta'+\sin\theta=0$（$k\ge0$），写成 $x'=y$，$y'=-\sin x-ky$。平衡点为 $(m\pi,0)$，$m\in\mathbb{Z}$。

- 在 $(0,0)$ 处 $D\boldsymbol{f}=\begin{bmatrix}0&1\\-1&-k\end{bmatrix}$，特征多项式 $\lambda^2+k\lambda+1$。$k>0$ 时实部为负，下垂的平衡位置渐近稳定；$k=0$ 时特征值 $\pm\mathrm{i}$，临界情形（由例 11.4.1，它是稳定的）。
- 在 $(\pi,0)$ 处 $D\boldsymbol{f}=\begin{bmatrix}0&1\\1&-k\end{bmatrix}$，$\det=-1<0$，有一个正特征值，倒立的平衡位置不稳定。

![单摆的相图：左，无阻尼 θ'' + sin θ = 0，原点附近是闭轨线（中心），(±π, 0) 是鞍点，粗线为连接鞍点的分界线（separatrix）；右，有阻尼 k = 0.25，原点成为稳定焦点，分界线把相平面分成趋于不同平衡点 (2mπ, 0) 的区域](./plots/pendulum-phase-portrait.py)

## 11.4. Lyapunov 函数法

### 11.4.1. 稳定性定理

线性近似在临界情形失效，也不能给出吸引区域的大小。Lyapunov 第二方法推广了能量的思想：如果某个"能量"沿轨线不增加，平衡点就是稳定的。考虑自治系统

$$
\boldsymbol{x}'=\boldsymbol{f}(\boldsymbol{x}),\qquad\boldsymbol{f}(\boldsymbol{0})=\boldsymbol{0},\tag{11.3}
$$
$\boldsymbol{f}$ 在原点的邻域 $\Omega$ 内局部 Lipschitz。

**定义 11.4.1** 设 $V$ 在 $\Omega$ 内连续可微，$V(\boldsymbol{0})=0$。若 $V(\boldsymbol{x})>0$（$\boldsymbol{x}\ne\boldsymbol{0}$），称 $V$ 为**正定函数**；若 $-V$ 正定，称 $V$ 负定；若 $V\ge0$（$V\le0$），称 $V$ 半正定（半负定）。称

$$
\dot V(\boldsymbol{x})=\nabla V(\boldsymbol{x})\cdot\boldsymbol{f}(\boldsymbol{x})=\sum_i\frac{\partial V}{\partial x_i}f_i(\boldsymbol{x})
$$
为 $V$ 沿方程组 (11.3) 的全导数。

由链式法则，对 (11.3) 的解 $\boldsymbol{x}(t)$，$\frac{\mathrm{d}}{\mathrm{d}t}V(\boldsymbol{x}(t))=\dot V(\boldsymbol{x}(t))$：不需要求出解，就能知道 $V$ 沿解如何变化。

**定理 11.4.1（Lyapunov）** 设 $V$ 在 $\Omega$ 内正定。

1. 若 $\dot V(\boldsymbol{x})\le0$（$\boldsymbol{x}\in\Omega$），则零解稳定；
2. 若 $\dot V$ 负定，则零解渐近稳定。

满足 1 或 2 的 $V$ 称为 Lyapunov 函数（Lyapunov function）。

**证明** 1：任取 $\varepsilon>0$，使闭球 $\|\boldsymbol{x}\|\le\varepsilon$ 含于 $\Omega$。$V$ 在球面 $\|\boldsymbol{x}\|=\varepsilon$ 上连续、正，最小值 $m>0$。由 $V(\boldsymbol{0})=0$ 与连续性，存在 $\delta\in(0,\varepsilon)$ 使 $\|\boldsymbol{x}\|<\delta$ 时 $V(\boldsymbol{x})<m$。设 $\|\boldsymbol{x}_0\|<\delta$，只要解留在球内，$V(\boldsymbol{x}(t))$ 不增，$V(\boldsymbol{x}(t))\le V(\boldsymbol{x}_0)<m$，所以解永远到不了球面。于是解留在紧集内，可以延伸到 $[t_0,+\infty)$，且 $\|\boldsymbol{x}(t)\|<\varepsilon$。

2：由 1 零解稳定；取 $\varepsilon$ 与对应的 $\delta$，设 $\|\boldsymbol{x}_0\|<\delta$。$V(\boldsymbol{x}(t))$ 单调减少，有极限 $c\ge0$。若 $c>0$，由 $V$ 的连续性，存在 $\rho>0$ 使 $\|\boldsymbol{x}(t)\|\ge\rho$ 对所有 $t$ 成立；$\dot V$ 在紧集 $\rho\le\|\boldsymbol{x}\|\le\varepsilon$ 上有负的最大值 $-\mu$，于是 $V(\boldsymbol{x}(t))\le V(\boldsymbol{x}_0)-\mu(t-t_0)\to-\infty$，矛盾。所以 $V(\boldsymbol{x}(t))\to0$。对任意 $\eta\in(0,\varepsilon)$，$V$ 在 $\eta\le\|\boldsymbol{x}\|\le\varepsilon$ 上有正的最小值，$V(\boldsymbol{x}(t))$ 最终小于它，所以 $\|\boldsymbol{x}(t)\|$ 最终小于 $\eta$，即 $\boldsymbol{x}(t)\to\boldsymbol{0}$。 $\square$

**定理 11.4.2（不稳定性，Chetaev）** 设 $V$ 在 $\Omega$ 内连续可微，$V(\boldsymbol{0})=0$，在原点的任意邻域内都有使 $V>0$ 的点，且 $\dot V$ 在 $\Omega$ 内正定，则零解不稳定。

**证明** （思路）取 $\boldsymbol{x}_0$ 任意接近原点而 $V(\boldsymbol{x}_0)>0$。$V(\boldsymbol{x}(t))$ 单调增加，所以解离开原点的某个邻域；否则在 $V\ge V(\boldsymbol{x}_0)$ 的区域中 $\dot V$ 有正的下界，$V(\boldsymbol{x}(t))\to+\infty$，与 $V$ 在紧集上有界矛盾。 $\square$

**定理 11.4.3（LaSalle 不变原理）** 设 $V$ 正定，$\dot V\le0$，且集合 $E=\{\boldsymbol{x}\in\Omega:\dot V(\boldsymbol{x})=0\}$ 中除原点外不含 (11.3) 的整条正半轨线，则零解渐近稳定（陈述）。

### 11.4.2. 例子

**例 11.4.1** 单摆 $x'=y$，$y'=-\sin x-ky$（$k\ge0$）的能量 $V=\frac12y^2+(1-\cos x)$ 在 $\lvert x\rvert<2\pi$ 内正定，

$$
\dot V=y\cdot(-\sin x-ky)+\sin x\cdot y=-ky^2\le0.
$$
由定理 11.4.1，原点稳定，$k=0$ 的临界情形也得到解决。$k>0$ 时 $\dot V$ 只是半负定（在 $x$ 轴上为零），定理 11.4.1 的第 2 条不适用；但 $x$ 轴上 $y=0$、$y'=-\sin x\ne0$（$x\ne0$），轨线不能停留在 $E=\{y=0\}$ 上，由 LaSalle 不变原理原点渐近稳定，与例 11.3.1 一致。

**例 11.4.2** 方程组

$$
x'=-y-x^3,\qquad y'=x-y^3
$$
的线性近似 $\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ 的特征值为 $\pm\mathrm{i}$，属于临界情形。取 $V=x^2+y^2$，

$$
\dot V=2x(-y-x^3)+2y(x-y^3)=-2(x^4+y^4)
$$
负定，零解渐近稳定：线性化的中心被非线性项变成了稳定焦点。把 $-x^3,-y^3$ 换成 $+x^3,+y^3$，$\dot V=2(x^4+y^4)$ 正定，由 Chetaev 定理零解不稳定。线性近似相同，稳定性相反，这就是"临界情形不能判定"的含义。

**例 11.4.3** 线性系统 $\boldsymbol{x}'=A\boldsymbol{x}$ 的二次型 Lyapunov 函数 $V=\boldsymbol{x}^{\mathsf T}P\boldsymbol{x}$：$\dot V=\boldsymbol{x}^{\mathsf T}(A^{\mathsf T}P+PA)\boldsymbol{x}$。可以证明，$A$ 的特征值实部全为负，当且仅当对某个（等价地，任意）**正定矩阵** $Q$，Lyapunov 方程 $A^{\mathsf T}P+PA=-Q$ 有正定解 $P$（陈述）。这个 $V$ 对 (11.2) 中的非线性系统在原点附近仍是 Lyapunov 函数，这给出了定理 11.3.1 第 1 条的另一个证明，并且 $V<c$ 的小椭球都含在吸引区域内。

构造 Lyapunov 函数没有通用的方法，物理系统常取能量，生态模型常取 $\sum_i(x_i-x_i^*-x_i^*\ln\frac{x_i}{x_i^*})$ 一类函数。

## 11.5. 平面自治系统

### 11.5.1. 相平面与轨线

本节与下两节考虑平面自治系统

$$
x'=P(x,y),\qquad y'=Q(x,y),\tag{11.4}
$$
$P,Q$ 在区域 $G\subset\mathbb{R}^2$ 内连续可微。

**定义 11.5.1** $(x,y)$ 所在的平面称为 (11.4) 的**相平面**。(11.4) 的解 $(x(t),y(t))$ 在相平面上描出的有向曲线称为**轨线**，$t\ge t_0$ 的部分称为正半轨线。全部轨线的图像称为 (11.4) 的**相图**。

解是 $(t,x,y)$ 空间中的**积分曲线**，轨线是它在相平面上的投影。自治系统的右端与 $t$ 无关，向量场 $(P,Q)$ 在每一点给出轨线的切方向，这使轨线有很好的性质：

**定理 11.5.1** 

1. 若 $(x(t),y(t))$ 是解，则对任意常数 $c$，$(x(t+c),y(t+c))$ 也是解，二者轨线相同；
2. 过 $G$ 内每一点恰有一条轨线，不同的轨线不相交；
3. 平衡点本身是一条轨线；非平衡点出发的轨线不能在有限时间内到达平衡点；
4. 一条轨线是闭曲线（且不是平衡点），当且仅当对应的解是非常数的周期解。

**证明** 1：$(x(t+c))'=P(x(t+c),y(t+c))$，右端不显含 $t$。2：若两条轨线都过点 $\boldsymbol{p}$，设 $\boldsymbol{x}_1(t_1)=\boldsymbol{x}_2(t_2)=\boldsymbol{p}$，则 $\boldsymbol{x}_1(t+t_1-t_2)$ 与 $\boldsymbol{x}_2(t)$ 是在 $t_2$ 处取值相同的解，由唯一性相等，轨线相同。3：若 $\boldsymbol{x}(t_1)=\boldsymbol{x}^*$，由唯一性 $\boldsymbol{x}\equiv\boldsymbol{x}^*$。4：若轨线闭合，存在 $T>0$ 使 $\boldsymbol{x}(t_0+T)=\boldsymbol{x}(t_0)$，$\boldsymbol{x}(t+T)$ 与 $\boldsymbol{x}(t)$ 在 $t_0$ 处取值相同，由唯一性相等。 $\square$

在 $P\ne0$ 处，轨线满足一阶方程 $\dfrac{\mathrm{d}y}{\mathrm{d}x}=\dfrac{Q(x,y)}{P(x,y)}$，可以用前几章的方法求出轨线（但不知道时间参数）。例如 $x'=y$，$y'=-x$ 的轨线满足 $x\,\mathrm{d}x+y\,\mathrm{d}y=0$，即圆 $x^2+y^2=C$。一般地，若 $H(x,y)$ 沿解为常数（首次积分，[2.4.14](/2.4.14)），轨线就落在等高线 $H=C$ 上；无阻尼单摆的能量与 Lotka–Volterra 捕食者—猎物模型的守恒量都是这样的函数，所以它们的平衡点周围都是闭轨线（[7.4.4](/7.4.4)）。

### 11.5.2. 平面线性系统奇点的分类

考虑 $\boldsymbol{x}'=A\boldsymbol{x}$，$A$ 是 2 阶实矩阵，$\det A\ne0$（于是原点是孤立的平衡点）。记

$$
p=\operatorname{tr}(A),\qquad q=\det A,\qquad\Delta=p^2-4q,
$$
特征值为 $\lambda_{1,2}=\frac{p\pm\sqrt\Delta}{2}$，$\lambda_1+\lambda_2=p$，$\lambda_1\lambda_2=q$。实可逆的线性变换 $\boldsymbol{x}=T\boldsymbol{\xi}$ 把方程组化为 $\boldsymbol{\xi}'=T^{-1}AT\boldsymbol{\xi}$，相图只受到一个线性变形，所以只需讨论 $T^{-1}AT$ 的实标准形：

$$
\text{(i)}\ \begin{bmatrix}\lambda_1&0\\0&\lambda_2\end{bmatrix}\ (\lambda_1,\lambda_2\text{ 为实数}),\qquad\text{(ii)}\ \begin{bmatrix}\lambda&1\\0&\lambda\end{bmatrix},\qquad\text{(iii)}\ \begin{bmatrix}\alpha&-\beta\\\beta&\alpha\end{bmatrix}\ (\beta\ne0).
$$

**定理 11.5.2** 平面线性系统 $\boldsymbol{x}'=A\boldsymbol{x}$（$q=\det A\ne0$）的原点按 $p,q$ 分类如下。

| 条件 | 特征值 | 类型 | 稳定性 |
|---|---|---|---|
| $q<0$ | 异号实根 | 鞍点（saddle） | 不稳定 |
| $q>0$，$\Delta>0$ | 同号相异实根 | 结点（node） | $p<0$ 渐近稳定，$p>0$ 不稳定 |
| $q>0$，$\Delta=0$，$A=\lambda I$ | 二重实根，两个一阶块 | 星形结点（临界结点） | 同上 |
| $q>0$，$\Delta=0$，$A\ne\lambda I$ | 二重实根，一个二阶块 | 退化结点 | 同上 |
| $q>0$，$\Delta<0$，$p\ne0$ | 共轭复根，实部 $\frac p2\ne0$ | 焦点（focus） | $p<0$ 渐近稳定，$p>0$ 不稳定 |
| $q>0$，$p=0$ | 纯虚根 $\pm\mathrm{i}\sqrt q$ | 中心（center） | 稳定，不渐近稳定 |

**证明** 稳定性由定理 11.1.2 得到，下面说明轨线的形状。

（i）$\xi=c_1\mathrm{e}^{\lambda_1t}$，$\eta=c_2\mathrm{e}^{\lambda_2t}$。$\lambda_1\lambda_2>0$ 时消去 $t$ 得 $\lvert\eta\rvert=C\lvert\xi\rvert^{\lambda_2/\lambda_1}$，是一族"抛物线"，所有轨线进入（或离开）原点；若 $\lvert\lambda_1\rvert<\lvert\lambda_2\rvert$，指数 $>1$，除 $\eta$ 轴外的轨线都在原点处与 $\xi$ 轴（慢方向，$\lambda_1$ 的特征向量）相切。这是结点；$\lambda_1=\lambda_2$ 时轨线是射线，称为星形结点。$\lambda_1<0<\lambda_2$ 时 $\lvert\eta\rvert=C\lvert\xi\rvert^{-\lvert\lambda_2/\lambda_1\rvert}$，是"双曲线"；只有 $\xi$ 轴上的轨线进入原点、$\eta$ 轴上的离开原点，这四条半轴称为分界线，这是鞍点。

（ii）$\xi=(c_1+c_2t)\mathrm{e}^{\lambda t}$，$\eta=c_2\mathrm{e}^{\lambda t}$。$c_2\ne0$ 时 $\xi/\eta=c_1/c_2+t$，$t\to\mp\infty$（$\lambda\gtrless0$）时 $\xi/\eta\to\infty$：所有轨线都在原点处与 $\xi$ 轴（唯一的特征向量方向）相切，且轨线绕过原点的一侧"转弯"。这是退化结点。

（iii）令 $\xi=r\cos\theta$，$\eta=r\sin\theta$，方程组化为 $r'=\alpha r$，$\theta'=\beta$，所以 $r=r_0\mathrm{e}^{\alpha t}$，$\theta=\theta_0+\beta t$，轨线是对数螺线 $r=r_0\mathrm{e}^{\frac\alpha\beta(\theta-\theta_0)}$；$\alpha=0$ 时是圆。回到原坐标，螺线与圆分别变形为一般的螺线与椭圆。前者是焦点，后者是中心。 $\square$

焦点与中心的旋转方向可以直接看：在点 $(1,0)$ 处速度为 $(a_{11},a_{21})$，$a_{21}>0$ 时逆时针旋转。六种相图见 [2.1.11 的 11.9 节](/2.1.11#sec-11.9)，下图把分类画在 $(p,q)$ 平面上。

![平面线性系统在迹—行列式平面 (p, q) = (tr A, det A) 上的分类：q < 0 为鞍点；抛物线 p^2 = 4q 之上为焦点，之下（q > 0）为结点；p < 0 的一侧渐近稳定，p > 0 的一侧不稳定；正 q 轴为中心，抛物线本身为星形结点或退化结点](./plots/trace-determinant-plane.py)

**例 11.5.1** 求解下列各题。（1）$A=\begin{bmatrix}1&2\\3&2\end{bmatrix}$：$q=-4<0$，鞍点。（2）$A=\begin{bmatrix}-1&1\\-4&-1\end{bmatrix}$：$p=-2$，$q=5$，$\Delta=-16<0$，稳定焦点；$a_{21}=-4<0$，顺时针旋转。（3）$A=\begin{bmatrix}-3&1\\1&-3\end{bmatrix}$：$p=-6$，$q=8$，$\Delta=4>0$，稳定结点，特征值 $-2,-4$，轨线在原点处与慢方向 $(1,1)^{\mathsf T}$ 相切。

对非线性系统 (11.4)，在平衡点处取 Jacobi 矩阵作分类。若 $P,Q\in C^2$，线性近似为鞍点、相异特征值的结点或焦点时，非线性系统在平衡点附近的轨线类型与稳定性都与线性近似相同；线性近似为中心时，非线性系统可能是中心（如无阻尼单摆），也可能是焦点（例 11.4.2），需要另行判断。

## 11.6. 极限环

### 11.6.1. 定义与例子

线性系统的闭轨线总是成族出现（中心），不能描述"无论初值如何，系统最终都进入同一个振荡"的现象，例如心跳、电子振荡器与捕食者—猎物种群的持续振荡。这需要孤立的闭轨线。

**定义 11.6.1（极限环）** 平面自治系统的一条闭轨线 $\Gamma$ 若是孤立的（存在 $\Gamma$ 的一个环形邻域，其中没有别的闭轨线），则称为**极限环**。若两侧附近的轨线当 $t\to+\infty$ 时都趋于 $\Gamma$，称它是稳定的；都在 $t\to-\infty$ 时趋于 $\Gamma$，称为不稳定的；一侧趋近、一侧远离，称为半稳定的。

**例 11.6.1** 方程组

$$
x'=-y+x(1-x^2-y^2),\qquad y'=x+y(1-x^2-y^2)
$$
在极坐标下为 $r'=r(1-r^2)$，$\theta'=1$。解得 $r(t)=\big(1+C\mathrm{e}^{-2t}\big)^{-1/2}$：$r_0<1$ 与 $r_0>1$ 时都有 $r\to1$，轨线螺旋地趋于单位圆。单位圆是稳定的极限环，原点（线性近似特征值 $1\pm\mathrm{i}$）是不稳定焦点。

### 11.6.2. 存在与不存在的判据

**定义 11.6.2** 设正半轨线 $\gamma^+$ 对应解 $\boldsymbol{x}(t)$，$t\ge t_0$。若存在 $t_k\to+\infty$ 使 $\boldsymbol{x}(t_k)\to\boldsymbol{p}$，称 $\boldsymbol{p}$ 为 $\gamma^+$ 的 $\omega$ 极限点，全体 $\omega$ 极限点构成 $\omega$ **极限集**。

**定理 11.6.1（Poincaré–Bendixson）** 设平面自治系统 (11.4) 的正半轨线 $\gamma^+$ 含于 $G$ 内的有界闭集 $K$ 中，且 $K$ 中没有平衡点，则 $\gamma^+$ 的 $\omega$ 极限集是一条闭轨线：$\gamma^+$ 本身是闭轨线，或者螺旋地趋于一条闭轨线（陈述）。

常用的形式：若环形区域 $K$ 内没有平衡点，并且在 $K$ 的边界上向量场都指向 $K$ 的内部（$K$ 是正不变的"捕获区域"），则 $K$ 内至少有一条闭轨线。例 11.6.1 中可取 $K=\{\frac12\le r\le2\}$：$r=\frac12$ 处 $r'>0$，$r=2$ 处 $r'<0$。这一定理是平面特有的（它依赖于 Jordan 曲线定理）；三维以上的自治系统可以有混沌的有界轨线，如 Lorenz 方程。

**定理 11.6.2（Bendixson 判据）** 设 $D\subset G$ 是单连通区域，$\dfrac{\partial P}{\partial x}+\dfrac{\partial Q}{\partial y}$ 在 $D$ 内不变号，且不在 $D$ 的任何子区域内恒为零，则 (11.4) 在 $D$ 内没有闭轨线。

**证明** 设 $\Gamma\subset D$ 是闭轨线，周期为 $T$，所围区域为 $\Sigma$（由单连通性 $\Sigma\subset D$）。由 **Green 公式**，

$$
\iint_\Sigma\Big(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}\Big)\mathrm{d}x\,\mathrm{d}y=\oint_\Gamma P\,\mathrm{d}y-Q\,\mathrm{d}x=\pm\int_0^T\big(P\,y'-Q\,x'\big)\,\mathrm{d}t=\pm\int_0^T(PQ-QP)\,\mathrm{d}t=0,
$$
而左边的被积函数不变号且不恒为零，积分不为零，矛盾。 $\square$

更一般地，若存在 $C^1$ 函数 $B(x,y)$ 使 $\frac{\partial(BP)}{\partial x}+\frac{\partial(BQ)}{\partial y}$ 满足同样的条件，结论仍成立（Dulac 判据）。例如阻尼振子 $x'=y$，$y'=-g(x)-ky$（$k>0$）的散度为 $-k<0$，没有闭轨线。

### 11.6.3. van der Pol 方程

**例 11.6.2** van der Pol 方程

$$
x''-\mu(1-x^2)x'+x=0\qquad(\mu>0)
$$
描述带有非线性电阻的振荡电路：$\lvert x\rvert<1$ 时阻尼为负，振幅被放大；$\lvert x\rvert>1$ 时阻尼为正，振幅被削弱。写成 $x'=y$，$y'=-x+\mu(1-x^2)y$。

- 唯一的平衡点是原点，Jacobi 矩阵 $\begin{bmatrix}0&1\\-1&\mu\end{bmatrix}$，$p=\mu>0$，$q=1$：不稳定焦点（$\mu<2$）或不稳定结点（$\mu>2$）。
- 能量 $E=\frac12(x^2+y^2)$ 满足 $\dot E=\mu(1-x^2)y^2$：在带形 $\lvert x\rvert<1$ 内增加，在外面可以减少。可以证明（Liénard 定理，陈述）方程有唯一的极限环，它是稳定的，所有非零解都趋于它。
- $\mu$ 很小时极限环接近半径为 2 的圆，振荡近似于简谐振动；$\mu$ 很大时是"张弛振荡"：缓慢变化与快速跳跃交替，周期约为 $(3-2\ln2)\mu$。

![van der Pol 方程：左，μ = 1 的相平面，从内部（靠近不稳定焦点）与外部出发的轨线都趋于同一个极限环（粗线）；右，x(t) 在 μ = 1 时接近正弦振荡，在 μ = 5 时是缓慢变化与快速跳跃交替的张弛振荡](./plots/van-der-pol.py)

### 11.6.4. Hopf 分岔

依赖参数的系统，当参数经过某个临界值时相图的拓扑结构（平衡点、闭轨线的个数与稳定性）发生改变，称为分岔（bifurcation）。考虑

$$
r'=r(\mu-r^2),\qquad\theta'=1.
$$
$\mu<0$ 时原点是稳定焦点，没有闭轨线；$\mu>0$ 时原点变为不稳定焦点，同时出现半径为 $\sqrt\mu$ 的稳定极限环。原点的线性近似特征值为 $\mu\pm\mathrm{i}$，$\mu$ 增加时一对复特征值从左向右穿过虚轴。一般地，平面系统的平衡点在一对复特征值以非零速度穿过虚轴时，在非退化条件下会产生或消失一个小振幅的极限环，这称为 Hopf 分岔（陈述）。van der Pol 方程在 $\mu$ 从负到正经过 $0$ 时也是如此。生物模型中种群从稳定共存转为持续振荡，常常就是这种分岔（[7.4.4](/7.4.4)）。

## 小结

| 主题 | 结论 |
|---|---|
| 稳定性 | 小扰动在 $[t_0,\infty)$ 上只引起小偏离；渐近稳定还要求趋于零 |
| 线性系统 | 稳定 $\Leftrightarrow$ $\Phi$ 有界；常系数：渐近稳定 $\Leftrightarrow$ $\operatorname{Re}\lambda<0$；稳定 $\Leftrightarrow$ $\operatorname{Re}\lambda\le0$ 且纯虚特征值半单 |
| Routh–Hurwitz | 稳定多项式 $\Leftrightarrow$ Hurwitz 矩阵的顺序主子式全为正；必要条件：系数全为正 |
| 线性近似 | $\operatorname{Re}\lambda<0$ 全成立 $\Rightarrow$ 渐近稳定；有 $\operatorname{Re}\lambda>0$ $\Rightarrow$ 不稳定；其余为临界情形 |
| Lyapunov 函数 | $V$ 正定，$\dot V\le0$ $\Rightarrow$ 稳定；$\dot V$ 负定 $\Rightarrow$ 渐近稳定；LaSalle 原理处理 $\dot V$ 半负定 |
| 平面线性系统 | $q<0$ 鞍点；$q>0$ 时 $\Delta>0$ 结点、$\Delta<0$ 焦点、$p=0$ 中心；$p$ 的符号决定稳定性 |
| 极限环 | 孤立闭轨线；Poincaré–Bendixson 保证存在，Bendixson–Dulac 判据排除存在；van der Pol 方程有唯一稳定极限环 |
