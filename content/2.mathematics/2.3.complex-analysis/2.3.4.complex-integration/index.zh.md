---
title: 复积分与 Cauchy 定理
source_hash: 1cbcf631ca38
---

本章是整门课程的核心。解析函数沿闭曲线的积分为零（Cauchy 积分定理）；先除以 $\zeta-z$ 再积分，得到 $2\pi\mathrm{i}f(z)$（Cauchy 积分公式）。由这两个事实，几乎不费什么力气就能推出使解析函数与众不同的几乎全部性质：解析函数无穷次可导，有界整函数是常数，每个多项式都有根，$|f|$ 在边界上取得最大值。后面各章也建立在同一基础上：把 Cauchy 核 $\frac1{\zeta-z}$ 展开成几何级数，就得到幂级数与 Laurent 级数（[2.3.5](/2.3.5)）；留数定理（[2.3.6](/2.3.6)）就是 Cauchy 定理在有洞区域上的应用。复积分实际上就是**第二型曲线积分**，证明最初几个定理的主要工具是 [2.2.13](/2.2.13) 的 **Green 公式**；所用的曲线、区域和定向都来自 [2.3.1](/2.3.1)。

## 4.1. 复积分

### 4.1.1. 定义与计算

**定义 4.1.1（复积分）** 设 $C$ 是从 $z_0$ 到 $z_n$ 的分段光滑有向曲线，$f$ 是定义在 $C$ 上的函数。沿 $C$ 的方向依次取分点 $z_0,z_1,\dots,z_n$，在从 $z_{k-1}$ 到 $z_k$ 的弧段上任取一点 $\zeta_k$，记 $\Delta z_k=z_k-z_{k-1}$。若当各弧段长度的最大值趋于 $0$ 时，和式 $\sum_{k=1}^{n}f(\zeta_k)\Delta z_k$ 收敛于一个与分点和 $\zeta_k$ 的取法都无关的极限，则称此极限为 $f$ 沿 $C$ 的**复积分**，记作 $\int_Cf(z)\,\mathrm{d}z$。若 $C$ 是闭曲线，记作 $\oint_Cf(z)\,\mathrm{d}z$；除非特别说明，闭曲线取正向（逆时针方向）。

**定理 4.1.1** 设 $f=u+\mathrm{i}v$ 在分段光滑曲线 $C$ 上连续。则 $\int_Cf(z)\,\mathrm{d}z$ 存在，且

$$
\int_Cf(z)\,\mathrm{d}z=\int_Cu\,\mathrm{d}x-v\,\mathrm{d}y+\mathrm{i}\int_Cv\,\mathrm{d}x+u\,\mathrm{d}y. \tag{4.1}
$$

若 $C$ 沿其方向的参数表示为 $z(t)$，$a\le t\le b$，则

$$
\int_Cf(z)\,\mathrm{d}z=\int_a^bf\big(z(t)\big)\,z'(t)\,\mathrm{d}t. \tag{4.2}
$$

**证明** 记 $\Delta z_k=\Delta x_k+\mathrm{i}\Delta y_k$，$f(\zeta_k)=u_k+\mathrm{i}v_k$，Riemann 和可以拆成

$$
\sum f(\zeta_k)\Delta z_k=\sum(u_k\Delta x_k-v_k\Delta y_k)+\mathrm{i}\sum(v_k\Delta x_k+u_k\Delta y_k),
$$

右边两个实和式正是连续函数沿分段光滑曲线的实曲线积分的积分和，它们收敛于式 (4.1) 的右端。在这些曲线积分中代入 $x=x(t)$、$y=y(t)$ 再重新组合，由 $(u+\mathrm{i}v)(x'+\mathrm{i}y')=(ux'-vy')+\mathrm{i}(vx'+uy')$ 即得式 (4.2)。$\square$

形式上，式 (4.1) 就是把 $(u+\mathrm{i}v)(\mathrm{d}x+\mathrm{i}\,\mathrm{d}y)$ 乘开。复积分继承了曲线积分的性质：

- 线性：对 $\alpha,\beta\in\mathbb{C}$，$\int_C(\alpha f+\beta g)\,\mathrm{d}z=\alpha\int_Cf\,\mathrm{d}z+\beta\int_Cg\,\mathrm{d}z$；
- 改变方向则变号：$\int_{C^-}f\,\mathrm{d}z=-\int_Cf\,\mathrm{d}z$；
- 可加性：若 $C$ 由 $C_1$ 接着 $C_2$ 组成，则 $\int_C=\int_{C_1}+\int_{C_2}$；
- 与参数化无关（只要保持方向）；
- $\big|\int_Cf(z)\,\mathrm{d}z\big|\le\int_C|f(z)|\,|\mathrm{d}z|$，其中 $|\mathrm{d}z|=\mathrm{d}s=|z'(t)|\,\mathrm{d}t$ 是**弧长**元素，所以右端是**第一型曲线积分**。

**例 4.1.1** 设 $C_r$ 是正向圆周 $|z-z_0|=r$，$n\in\mathbb{Z}$。则

$$
\oint_{C_r}(z-z_0)^n\,\mathrm{d}z=\begin{cases}2\pi\mathrm{i}, & n=-1,\\ 0, & n\ne-1.\end{cases} \tag{4.3}
$$

事实上，取 $z=z_0+r\mathrm{e}^{\mathrm{i}t}$，$0\le t\le2\pi$，$\mathrm{d}z=\mathrm{i}r\mathrm{e}^{\mathrm{i}t}\,\mathrm{d}t$，积分等于 $\mathrm{i}r^{n+1}\int_0^{2\pi}\mathrm{e}^{\mathrm{i}(n+1)t}\,\mathrm{d}t$，$n=-1$ 时为 $2\pi\mathrm{i}$，否则为 $0$。结果与 $r$ 无关。式 (4.3) 是本课程中用得最多的一个计算：与 Laurent 级数结合，它是留数定理的基础。

**例 4.1.2** 沿以下路径计算 $f(z)=\bar z$ 从 $0$ 到 $1+\mathrm{i}$ 的积分：(a) 线段 $z=t(1+\mathrm{i})$，$0\le t\le1$；(b) 折线 $0\to1\to1+\mathrm{i}$。

(a) $\int_0^1t(1-\mathrm{i})(1+\mathrm{i})\,\mathrm{d}t=\int_0^12t\,\mathrm{d}t=1$。

(b) 在 $[0,1]$ 上 $z=t$，积分为 $\int_0^1t\,\mathrm{d}t=\frac12$。在竖直线段上 $z=1+\mathrm{i}t$，$\mathrm{d}z=\mathrm{i}\,\mathrm{d}t$，积分为 $\int_0^1(1-\mathrm{i}t)\mathrm{i}\,\mathrm{d}t=\mathrm{i}+\frac12$。总和为 $1+\mathrm{i}$。

两个结果不同：$\bar z$ 的积分与路径有关。相反，对 $f(z)=z$，两条路径都给出 $\frac{(1+\mathrm{i})^2}{2}=\mathrm{i}$；我们将看到，这是 $z$ 的解析性所决定的（§4.3）。

### 4.1.2. 长大不等式

**定理 4.1.2（长大不等式）** 若在长度为 $L$ 的分段光滑曲线 $C$ 上 $|f(z)|\le M$，则

$$
\Big|\int_Cf(z)\,\mathrm{d}z\Big|\le ML.
$$

**证明** $\big|\int_Cf\,\mathrm{d}z\big|\le\int_C|f|\,\mathrm{d}s\le M\int_C\mathrm{d}s=ML$。$\square$

长大不等式用来证明沿小圆弧或大圆弧的积分趋于 $0$；它是否精确通常无关紧要。

**例 4.1.3** 设 $\Gamma_R$ 是圆周 $|z|=R$（$R>1$）的上半部分。对 $z\in\Gamma_R$，由三角不等式 $|z^2+1|\ge|z|^2-1=R^2-1$，所以

$$
\Big|\int_{\Gamma_R}\frac{\mathrm{d}z}{z^2+1}\Big|\le\frac{\pi R}{R^2-1}\to0\qquad(R\to\infty).
$$

这一估计是用留数计算 $\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{x^2+1}$ 的第一步（[2.3.7](/2.3.7)）。一般地，只要在 $\Gamma_R$ 上 $Rf(z)\to0$ 一致成立，即 $f$ 比 $1/|z|$ 衰减得快，就有 $\int_{\Gamma_R}f\,\mathrm{d}z\to0$。

## 4.2. Cauchy 积分定理

### 4.2.1. 定理

例 4.1.1 表明，$n\ge0$ 时沿圆周有 $\oint z^n\,\mathrm{d}z=0$；而例 4.1.2 表明，$\bar z$ 沿三角形 $0\to1\to1+\mathrm{i}\to0$ 的积分不为零（等于 $(1+\mathrm{i})-1=\mathrm{i}$）。区别在于解析性，Green 公式使这一点精确化。

**引理 4.2.1（Green 公式的复形式）** 设 $D$ 是有界区域，其边界 $\partial D$ 由有限条分段光滑的 Jordan 曲线组成，取正向；$f$ 在 $\bar D=D\cup\partial D$ 上有连续的一阶偏导数。则

$$
\oint_{\partial D}f(z)\,\mathrm{d}z=2\mathrm{i}\iint_D\frac{\partial f}{\partial\bar z}\,\mathrm{d}x\,\mathrm{d}y. \tag{4.4}
$$

**证明** 对复值 1-形式 $f\,\mathrm{d}x+\mathrm{i}f\,\mathrm{d}y$（即分别对其实部和虚部）应用 Green 公式（[2.2.13](/2.2.13#thm-13.4.1)）：

$$
\oint_{\partial D}f\,\mathrm{d}x+\mathrm{i}f\,\mathrm{d}y=\iint_D\Big(\mathrm{i}\frac{\partial f}{\partial x}-\frac{\partial f}{\partial y}\Big)\mathrm{d}x\,\mathrm{d}y=\mathrm{i}\iint_D\Big(\frac{\partial f}{\partial x}+\mathrm{i}\frac{\partial f}{\partial y}\Big)\mathrm{d}x\,\mathrm{d}y,
$$

而最后的被积函数就是 $2\frac{\partial f}{\partial\bar z}$（定义 2.4.1）。$\square$

**例 4.2.1** 对 $f=\bar z$，$\frac{\partial f}{\partial\bar z}=1$，所以对任何分段光滑的 Jordan 曲线 $C$，$\oint_C\bar z\,\mathrm{d}z=2\mathrm{i}\cdot$（$C$ 的内部的面积）。对上面的三角形，面积为 $\frac12$，积分为 $\mathrm{i}$，与计算结果一致。对椭圆 $\frac{x^2}{4}+y^2=1$（面积 $2\pi$），$\oint\bar z\,\mathrm{d}z=4\pi\mathrm{i}$；用参数表示 $z=2\cos t+\mathrm{i}\sin t$ 计算，结果相同。

**定理 4.2.1（Cauchy 积分定理）** 设 $f$ 在单连通区域 $D$ 上解析。则对 $D$ 内的每条分段光滑闭曲线 $C$，

$$
\oint_Cf(z)\,\mathrm{d}z=0.
$$

**证明** （附加假设 $f'$ 连续，且 $C$ 是 Jordan 曲线。）由于 $D$ 单连通，$C$ 的内部 $G$ 含于 $D$，所以 $f$ 在 $\bar G$ 上有连续偏导数，且由定理 2.4.1，在其上 $\frac{\partial f}{\partial\bar z}=0$。由式 (4.4) 得 $\oint_Cf\,\mathrm{d}z=0$。用实的语言说：由式 (4.1) 与 Green 公式，$\oint_C(u\,\mathrm{d}x-v\,\mathrm{d}y)=\iint_G(-v_x-u_y)\,\mathrm{d}x\,\mathrm{d}y$，$\oint_C(v\,\mathrm{d}x+u\,\mathrm{d}y)=\iint_G(u_x-v_y)\,\mathrm{d}x\,\mathrm{d}y$，由 Cauchy–Riemann 方程，两个被积函数都为零。自交有限次的闭曲线可以分成有限条 Jordan 曲线，对每一条应用上述论证；一般情形需要一个逼近论证，这里从略。$\square$

事后看来，附加假设并无妨碍：下面的定理 4.4.2 表明 $f'$ 自动连续。但那个定理是用 Cauchy 定理证明的，所以逻辑上完整的推导必须去掉这一假设，这正是 Goursat 的工作。

**定理 4.2.2（Goursat 定理）** 若 $f$ 在包含闭三角形 $T$（连同其内部）的某个开集上处处复可导，则 $\oint_{\partial T}f(z)\,\mathrm{d}z=0$。这里不假设 $f'$ 连续。

**证明** （概要）记 $I=\big|\oint_{\partial T}f\,\mathrm{d}z\big|$。连接各边中点，把 $T$ 分成四个相似的三角形，四者的边界积分之和等于沿 $\partial T$ 的积分（内部的边相互抵消）；所以其中某一个 $T_1$ 满足 $\big|\oint_{\partial T_1}f\big|\ge I/4$。重复这一过程，得到一列套在一起的三角形 $T_n$，周长为 $2^{-n}p$，$\big|\oint_{\partial T_n}f\big|\ge4^{-n}I$，它们收缩到一点 $z_0$。在 $z_0$ 附近，$f(z)=f(z_0)+f'(z_0)(z-z_0)+\varepsilon(z)(z-z_0)$，$\varepsilon(z)\to0$。线性部分有原函数，所以它沿 $\partial T_n$ 的积分为零（§4.3）；由长大不等式，余项的贡献不超过 $\sup_{T_n}|\varepsilon|\cdot2^{-n}p\cdot2^{-n}p$。因此 $I\le p^2\sup_{T_n}|\varepsilon|\to0$。$\square$

由三角形的情形可以得到沿每个闭多边形的积分，进而得到圆盘上原函数的存在性，再得到一般形式的定理 4.2.1；这里不再展开。定理对作为边界的闭曲线也成立：若 $D$ 由分段光滑的 Jordan 曲线 $C$ 围成，$f$ 在 $D$ 上解析、在 $\bar D$ 上连续，则 $\oint_Cf\,\mathrm{d}z=0$。

### 4.2.2. 复连通区域与闭路变形

**定理 4.2.3（复连通区域上的 Cauchy 定理）** 设 $C_0$ 是分段光滑的 Jordan 曲线，$C_1,\dots,C_n$ 是 $C_0$ 内部的分段光滑 Jordan 曲线，每一条都在其余各条的外部；$D$ 是 $C_0$ 内部且在所有 $C_k$ 外部的区域。若 $f$ 在包含 $\bar D$ 的某个开集上解析，则当所有曲线都取逆时针方向时，

$$
\oint_{C_0}f(z)\,\mathrm{d}z=\sum_{k=1}^{n}\oint_{C_k}f(z)\,\mathrm{d}z. \tag{4.5}
$$

等价地，对正向边界 $\partial D$（外边界逆时针，内边界顺时针），$\oint_{\partial D}f\,\mathrm{d}z=0$。

**证明** 若 $f'$ 连续，由于 $\partial f/\partial\bar z=0$，这就是式 (4.4) 用于 $D$。没有这一假设时，如图所示，用割线把 $C_0$ 连到 $C_1$，$C_1$ 连到 $C_2$，……，$C_n$ 连到 $C_0$。割线把 $D$ 分成两个单连通的部分，各由一条 Jordan 曲线围成；由 Cauchy 定理，每一部分的积分为零，而在两者之和中每条割线沿两个方向各经过一次，相互抵消，剩下的就是 $\oint_{\partial D}$。$\square$

![左：有两个洞的区域 D 及其正向边界，外边界 C0 为逆时针方向，内边界 C1、C2 为顺时针方向。右：连接各条边界曲线的割线把 D 分成上下两个单连通的部分；每条割线都属于两部分的边界，沿两个方向各经过一次，所以割线上的积分相互抵消。](./plots/multiply-connected.py)

$n=1$ 的情形用得最多。

**推论 4.2.1（闭路变形原理）** 设 $C_0$ 与 $C_1$ 是正向的分段光滑 Jordan 曲线，$C_1$ 在 $C_0$ 内部，$f$ 在包含两者之间的闭区域的某个开集上解析。则 $\oint_{C_0}f\,\mathrm{d}z=\oint_{C_1}f\,\mathrm{d}z$。

换句话说：积分路径可以连续地变形而不改变积分值，只要变形过程中不越过 $f$ 的奇点。于是沿复杂曲线的积分化为沿奇点周围小圆周的积分。

**例 4.2.2** 设 $C$ 是任意一条正向的分段光滑 Jordan 曲线，$a\notin C$。由推论 4.2.1 与式 (4.3)，

$$
\oint_C\frac{\mathrm{d}z}{(z-a)^n}=\begin{cases}2\pi\mathrm{i}, & n=1\text{ 且 }a\text{ 在 }C\text{ 内部},\\ 0, & \text{其他情形}\end{cases}\qquad(n\in\mathbb{Z}).
$$

若 $a$ 在 $C$ 的外部，被积函数在 $C$ 及其内部的某个单连通邻域上解析，由定理 4.2.1 积分为 $0$。

**例 4.2.3** 计算 $\displaystyle\oint_{|z|=2}\frac{2z-1}{z^2-z}\,\mathrm{d}z$ 与 $\displaystyle\oint_{|z|=2}\frac{\mathrm{d}z}{z^2-1}$。由部分分式 $\frac{2z-1}{z(z-1)}=\frac1z+\frac1{z-1}$，两个奇点都在 $|z|=2$ 内部，所以第一个积分为 $2\pi\mathrm{i}+2\pi\mathrm{i}=4\pi\mathrm{i}$。类似地，由 $\frac{1}{z^2-1}=\frac12\big(\frac1{z-1}-\frac1{z+1}\big)$，第二个积分为 $\frac12(2\pi\mathrm{i}-2\pi\mathrm{i})=0$，尽管被积函数在曲线内部并不解析：Cauchy 定理给出的是积分为零的充分条件，而不是必要条件。

## 4.3. 原函数

**定理 4.3.1** 设 $f$ 在区域 $D$ 上连续，且对 $D$ 内的分段光滑曲线 $C$，$\int_Cf\,\mathrm{d}z$ 只依赖于 $C$ 的端点（等价地，对 $D$ 内每条分段光滑闭曲线 $\oint_Cf\,\mathrm{d}z=0$）。取定 $z_0\in D$，令

$$
F(z)=\int_{z_0}^{z}f(\zeta)\,\mathrm{d}\zeta.
$$

则 $F$ 在 $D$ 上解析，且 $F'=f$。

**证明** 对 $z\in D$ 与充分小的 $h$，线段 $[z,z+h]$ 含于 $D$，由积分与路径无关，$F(z+h)-F(z)=\int_{[z,z+h]}f(\zeta)\,\mathrm{d}\zeta$。由于 $\int_{[z,z+h]}\mathrm{d}\zeta=h$，由长大不等式和 $f$ 的连续性，

$$
\Big|\frac{F(z+h)-F(z)}{h}-f(z)\Big|=\Big|\frac1h\int_{[z,z+h]}\big(f(\zeta)-f(z)\big)\,\mathrm{d}\zeta\Big|\le\max_{\zeta\in[z,z+h]}|f(\zeta)-f(z)|\to0.
$$
$\square$

与 [2.2.6](/2.2.6) 一样，在 $D$ 上满足 $F'=f$ 的函数 $F$ 称为 $f$ 在 $D$ 上的**原函数**。区域上的两个原函数相差一个常数（定理 2.3.2）。结合定理 4.2.1 与定理 4.3.1：

**推论 4.3.1** 单连通区域 $D$ 上的解析函数 $f$ 在 $D$ 上有原函数，且对任一原函数 $\Phi$ 和 $D$ 内从 $z_1$ 到 $z_2$ 的任一分段光滑曲线 $C$，

$$
\int_Cf(z)\,\mathrm{d}z=\Phi(z_2)-\Phi(z_1).
$$

**证明** 存在性上面已经证明。对任一原函数 $\Phi$ 与 $C$ 的参数表示 $z(t)$，$a\le t\le b$，有 $\frac{\mathrm{d}}{\mathrm{d}t}\Phi(z(t))=f(z(t))z'(t)$，所以由式 (4.2) 和微积分基本定理（分别用于实部与虚部）得 $\Phi(z_2)-\Phi(z_1)$。$\square$

第二个结论在 $f$ 有原函数的任何区域上都成立，不论是否单连通。因此微积分中的积分技巧（换元法、分部积分法）可以原样搬过来。

**例 4.3.1** 由于 $z\cos z$ 是整函数，沿任何路径都有 $\displaystyle\int_0^{\mathrm{i}}z\cos z\,\mathrm{d}z=\big[z\sin z+\cos z\big]_0^{\mathrm{i}}=\mathrm{i}\sin\mathrm{i}+\cos\mathrm{i}-1=-\sinh1+\cosh1-1=\mathrm{e}^{-1}-1$。

**例 4.3.2** 设 $\Gamma^+$ 与 $\Gamma^-$ 分别是单位圆周的上半部分与下半部分，都从 $1$ 到 $-1$。在包含 $\Gamma^+$ 的区域 $\mathbb{C}\setminus\{-\mathrm{i}t\mid t\ge0\}$ 上，分支 $\ln|z|+\mathrm{i}\theta$（$-\frac\pi2<\theta<\frac{3\pi}2$）是 $\frac1z$ 的原函数（[2.3.3](/2.3.3) 的定理 3.2.1），所以 $\int_{\Gamma^+}\frac{\mathrm{d}z}{z}=\mathrm{i}\pi-0=\mathrm{i}\pi$。对 $\Gamma^-$ 用 $-\frac{3\pi}2<\theta<\frac\pi2$ 的分支，得 $\int_{\Gamma^-}\frac{\mathrm{d}z}{z}=-\mathrm{i}\pi$。两者之差 $2\pi\mathrm{i}$ 就是沿整个圆周的积分。这也说明 $\frac1z$ 在 $\mathbb{C}\setminus\{0\}$ 上没有原函数，否则沿每条闭曲线的积分都应为零。

## 4.4. Cauchy 积分公式

### 4.4.1. 公式

**定理 4.4.1（Cauchy 积分公式）** 设 $f$ 在区域 $D$ 上解析，$C$ 是 $D$ 内的正向分段光滑 Jordan 曲线，其内部含于 $D$。则对 $C$ 内部的每一点 $z$，

$$
f(z)=\frac{1}{2\pi\mathrm{i}}\oint_C\frac{f(\zeta)}{\zeta-z}\,\mathrm{d}\zeta. \tag{4.6}
$$

**证明** 被积函数作为 $\zeta$ 的函数在 $D\setminus\{z\}$ 上解析，由闭路变形原理，积分等于沿 $C$ 内部任一小圆周 $|\zeta-z|=\rho$ 的积分：

$$
\oint_C\frac{f(\zeta)}{\zeta-z}\,\mathrm{d}\zeta=f(z)\oint_{|\zeta-z|=\rho}\frac{\mathrm{d}\zeta}{\zeta-z}+\oint_{|\zeta-z|=\rho}\frac{f(\zeta)-f(z)}{\zeta-z}\,\mathrm{d}\zeta.
$$

由式 (4.3)，第一项为 $2\pi\mathrm{i}f(z)$。由长大不等式，第二项不超过 $2\pi\rho\cdot\frac1\rho\max_{|\zeta-z|=\rho}|f(\zeta)-f(z)|$，由 $f$ 的连续性，它当 $\rho\to0$ 时趋于 $0$。左边与 $\rho$ 无关，所以第二项为 $0$。$\square$

Cauchy 积分公式表明，解析函数在曲线内部的值完全由它在曲线上的值决定，这对实可微函数没有任何类似的结论。它还把积分化为求函数值。

**例 4.4.1** 在式 (4.6) 中取 $f=\mathrm{e}^z$、$z=1$，得 $\displaystyle\oint_{|z|=2}\frac{\mathrm{e}^z}{z-1}\,\mathrm{d}z=2\pi\mathrm{i}\,\mathrm{e}$。

**例 4.4.2** 计算 $\displaystyle\oint_{|z|=2}\frac{\sin z}{z^2+1}\,\mathrm{d}z$。$\pm\mathrm{i}$ 都在曲线内部。可以拆成 $\frac1{z^2+1}=\frac1{2\mathrm{i}}\big(\frac1{z-\mathrm{i}}-\frac1{z+\mathrm{i}}\big)$，也可以把积分路径变形为绕 $\pm\mathrm{i}$ 的两个小圆周（定理 4.2.3）。对每一项应用式 (4.6)，

$$
\oint_{|z|=2}\frac{\sin z}{z^2+1}\,\mathrm{d}z=\frac{2\pi\mathrm{i}}{2\mathrm{i}}\big(\sin\mathrm{i}-\sin(-\mathrm{i})\big)=2\pi\sin\mathrm{i}=2\pi\mathrm{i}\sinh1.
$$

在式 (4.6) 中取 $C$ 为圆周 $|\zeta-z_0|=r$，$\zeta=z_0+r\mathrm{e}^{\mathrm{i}t}$，得到下面的推论。

**推论 4.4.1（平均值性质）** 若 $f$ 在包含闭圆盘 $|z-z_0|\le r$ 的某个开集上解析，则

$$
f(z_0)=\frac1{2\pi}\int_0^{2\pi}f\big(z_0+r\mathrm{e}^{\mathrm{i}t}\big)\,\mathrm{d}t.
$$

圆心处的值等于它在任一以之为圆心的圆周上的值的平均。取实部，调和函数也有同样的平均值性质（§4.6）。

### 4.4.2. 各阶导数

在积分号下对 $z$ 形式地求导，式 (4.6) 提示了各阶导数的公式。它们确实成立。

**定理 4.4.2（高阶导数公式）** 在定理 4.4.1 的条件下，$f$ 在 $C$ 内部的每一点 $z$ 处有各阶复导数，且

$$
f^{(n)}(z)=\frac{n!}{2\pi\mathrm{i}}\oint_C\frac{f(\zeta)}{(\zeta-z)^{n+1}}\,\mathrm{d}\zeta,\qquad n=0,1,2,\dots \tag{4.7}
$$

**证明** 我们证明 $n=1$ 的情形；归纳步骤是同样的计算，只是幂次更高。设 $d>0$ 是 $z$ 到 $C$ 的距离，$|h|<d/2$，$M=\max_C|f|$，$L$ 为 $C$ 的长度。由式 (4.6)，

$$
\frac{f(z+h)-f(z)}{h}-\frac1{2\pi\mathrm{i}}\oint_C\frac{f(\zeta)\,\mathrm{d}\zeta}{(\zeta-z)^2}=\frac{h}{2\pi\mathrm{i}}\oint_C\frac{f(\zeta)\,\mathrm{d}\zeta}{(\zeta-z-h)(\zeta-z)^2}.
$$

在 $C$ 上 $|\zeta-z|\ge d$，$|\zeta-z-h|\ge d/2$，所以由长大不等式，右端不超过 $\frac{|h|}{2\pi}\cdot\frac{2M}{d^3}\cdot L\to0$。$\square$

由于区域 $D$ 中每一点都在 $D$ 内某个小圆周的内部，我们得到一个基本的结构性事实。

**推论 4.4.2** 若 $f$ 在开集 $D$ 上解析，则 $f'$ 也在 $D$ 上解析；因此 $f$ 在 $D$ 上有各阶复导数。$f$ 的实部与虚部有各阶连续偏导数。

这就补全了 [2.3.2](/2.3.2) 中定理 2.5.1 的证明，也初次显示出解析函数理论与实可微函数理论的差别：复的情形中不存在可导一次却不可导两次的函数。在应用中，式 (4.7) 常反过来用于计算积分。

**例 4.4.3** $\displaystyle\oint_{|z|=1}\frac{\mathrm{e}^{2z}}{z^4}\,\mathrm{d}z=\frac{2\pi\mathrm{i}}{3!}\,\frac{\mathrm{d}^3}{\mathrm{d}z^3}\mathrm{e}^{2z}\Big|_{z=0}=\frac{2\pi\mathrm{i}\cdot8}{6}=\frac{8\pi\mathrm{i}}3$。

**例 4.4.4** 计算 $\displaystyle\oint_{|z-\mathrm{i}|=1}\frac{\mathrm{d}z}{(z^2+1)^2}$。圆周内部唯一的奇点是 $\mathrm{i}$（$-\mathrm{i}$ 到圆心的距离为 $2$）。把被积函数写成 $\frac{g(z)}{(z-\mathrm{i})^2}$，其中 $g(z)=\frac1{(z+\mathrm{i})^2}$ 在闭圆盘上解析。由 $n=1$ 时的式 (4.7)，

$$
\oint_{|z-\mathrm{i}|=1}\frac{\mathrm{d}z}{(z^2+1)^2}=2\pi\mathrm{i}\,g'(\mathrm{i})=2\pi\mathrm{i}\cdot\frac{-2}{(2\mathrm{i})^3}=2\pi\mathrm{i}\cdot\frac{-2}{-8\mathrm{i}}=\frac\pi2.
$$

## 4.5. 积分公式的推论

### 4.5.1. Cauchy 估计与 Liouville 定理

**定理 4.5.1（Cauchy 估计）** 设 $f$ 在包含闭圆盘 $|z-z_0|\le R$ 的某个开集上解析，$M(R)=\max_{|z-z_0|=R}|f(z)|$。则

$$
\big|f^{(n)}(z_0)\big|\le\frac{n!\,M(R)}{R^n},\qquad n=0,1,2,\dots
$$

**证明** 在圆周 $|\zeta-z_0|=R$ 上对式 (4.7) 应用长大不等式：$\big|f^{(n)}(z_0)\big|\le\frac{n!}{2\pi}\cdot\frac{M(R)}{R^{n+1}}\cdot2\pi R$。$\square$

**定理 4.5.2（Liouville 定理）** 有界整函数必为常数。

**证明** 若在 $\mathbb{C}$ 上 $|f|\le M$，则对每个 $z_0$ 和每个 $R>0$，由 $n=1$ 时的定理 4.5.1，$|f'(z_0)|\le M/R$。令 $R\to\infty$ 得 $f'(z_0)=0$。所以 $f'\equiv0$，$f$ 为常数（定理 2.3.2）。$\square$

在实数范围内，$\sin x$ 与 $\frac1{1+x^2}$ 有界、光滑且不是常数；Liouville 定理表明，它们的复延拓必定无界（$\sin z$ 见 [2.3.3](/2.3.3) 的定理 3.4.1），或者有奇点（$\frac1{1+z^2}$ 在 $\pm\mathrm{i}$ 处）。这个定理通常用于由 $f$ 构造的辅助函数，如下面几个例子。对 $|z|$ 很大时满足 $|f(z)|\le M|z|^m$ 的多项式增长的整函数，用同样的论证对 $f^{(m+1)}$ 应用 Cauchy 估计，可知它是次数不超过 $m$ 的多项式；这一推广及其应用在 [2.3.6](/2.3.6) 中讨论。

**例 4.5.1** 若 $f$ 是整函数，且对一切 $z$ 有 $\operatorname{Re}f(z)\le1$，则 $f$ 为常数。事实上，$g=\mathrm{e}^{f}$ 是整函数，$|g|=\mathrm{e}^{\operatorname{Re}f}\le\mathrm{e}$，由 Liouville 定理 $g$ 为常数；于是 $0=g'=f'\mathrm{e}^f$，又 $\mathrm{e}^f\ne0$，得 $f'\equiv0$。对 $\operatorname{Re}f$ 或 $\operatorname{Im}f$ 的任何单侧界，同样的论证都适用（用 $\mathrm{e}^{-f}$、$\mathrm{e}^{\pm\mathrm{i}f}$）。

**例 4.5.2** 若 $f$ 是整函数，且其像避开一个圆盘，即对一切 $z$ 有 $|f(z)-w_0|\ge\delta>0$，则 $g=\frac1{f-w_0}$ 是整函数且 $|g|\le\frac1\delta$，因而为常数，$f$ 也是常数。所以非常数整函数的像是稠密的。（实际上结论还强得多：由 Picard 小定理，非常数整函数至多取不到一个复数值。）

**例 4.5.3** 求所有整函数 $f$，使 $f'=A+\mathrm{i}B$ 处处满足 $A\ge-2$，且 $f(0)=0$，$f(1)=3$。对整函数 $-f'$（其实部不超过 $2$）应用例 4.5.1，$f'$ 为常数 $a$。于是 $f(z)=az+b$，由条件得 $b=0$，$a=3$；确实 $\operatorname{Re}f'=3\ge-2$。所以 $f(z)=3z$。

### 4.5.2. 代数基本定理

**定理 4.5.3（代数基本定理）** 每个次数 $n\ge1$ 的复系数多项式 $p(z)=a_nz^n+\cdots+a_1z+a_0$ 在 $\mathbb{C}$ 中都有根。因此它恰有 $n$ 个根（按重数计）。

**证明** 假设对一切 $z$ 有 $p(z)\ne0$。则 $g=1/p$ 是整函数。由于 $z\to\infty$ 时 $p(z)\to\infty$（[2.3.1](/2.3.1) 的例 1.4.2），存在 $R$ 使 $|z|\ge R$ 时 $|g(z)|\le1$，而由连续性，$|g|$ 在紧圆盘 $|z|\le R$ 上有界。所以 $g$ 是有界整函数，由 Liouville 定理为常数，$p$ 也是常数，矛盾。逐个除去一次因式 $z-z_1$ 即得第二个结论。$\square$

线性代数中正是用这个定理保证 $\mathbb{C}$ 上特征值的存在（[定理 9.8.1](/2.1.9#thm-9.8.1)），那里的证明推迟到了本课程。[2.3.7](/2.3.7) 将用 Rouché 定理计数零点，给出第二个证明。

### 4.5.3. Morera 定理

Cauchy 定理有逆定理。

**定理 4.5.4（Morera 定理）** 设 $f$ 在区域 $D$ 上连续，且对 $D$ 中的每个闭三角形 $T$ 有 $\oint_{\partial T}f(z)\,\mathrm{d}z=0$。则 $f$ 在 $D$ 上解析。

**证明** 解析性是局部性质，所以只需在以 $z_0$ 为圆心的圆盘 $B\subset D$ 上讨论。对 $z\in B$，令 $F(z)=\int_{[z_0,z]}f(\zeta)\,\mathrm{d}\zeta$。对 $z,z+h\in B$，以 $z_0,z,z+h$ 为顶点的三角形含于 $B$，由假设，$F(z+h)-F(z)=\int_{[z,z+h]}f\,\mathrm{d}\zeta$。于是定理 4.3.1 证明中的估计表明在 $B$ 上 $F'=f$。所以 $F$ 在 $B$ 上解析，由推论 4.4.2，$F'=f$ 也解析。$\square$

Morera 定理是证明由极限或积分定义的函数解析的标准工具。例如，若 $f_n$ 在 $D$ 上解析，且 $f_n$ 在 $D$ 上**内闭一致收敛**于 $f$，则 $f$ 连续且 $\oint_{\partial T}f=\lim\oint_{\partial T}f_n=0$，所以 $f$ 解析。这是 [2.3.5](/2.3.5) 中幂级数理论的基础。

## 4.6. 最大模原理与调和函数

### 4.6.1. 最大模原理

**定理 4.6.1（最大模原理）** 设 $f$ 在区域 $D$ 上解析。若 $|f|$ 在 $D$ 的某一点处取得它在 $D$ 上的最大值，则 $f$ 在 $D$ 上为常数。因此，若 $D$ 有界且 $f$ 在 $\bar D$ 上连续，则 $\max_{\bar D}|f|$ 在边界 $\partial D$ 上取得。

**证明** 设 $M=\max_D|f|=|f(z_0)|$，$E=\{z\in D\mid |f(z)|=M\}$；$E$ 非空且是 $D$ 中的闭集。若 $z_1\in E$ 且闭圆盘 $|z-z_1|\le r$ 含于 $D$，由推论 4.4.1，

$$
M=|f(z_1)|\le\frac1{2\pi}\int_0^{2\pi}\big|f(z_1+\rho\mathrm{e}^{\mathrm{i}t})\big|\,\mathrm{d}t\le M\qquad(0<\rho\le r).
$$

各处都取等号，迫使连续函数 $M-|f|\ge0$ 在每个圆周 $|z-z_1|=\rho$ 上为零，所以在圆盘上 $|f|=M$，圆盘含于 $E$。因此 $E$ 也是开集，又 $D$ 连通，故 $E=D$。所以 $|f|$ 在 $D$ 上为常数，由推论 2.3.1，$f$ 为常数。对第二个结论：$|f|$ 在紧集 $\bar D$ 上取得最大值；若只在内点处取得，则 $f$ 为常数，此时最大值也在 $\partial D$ 上取得。$\square$

由 [2.3.5](/2.3.5) 的唯一性定理，即使 $|f|$ 只在某个内点处取得局部最大值，$f$ 也必为常数。若 $f$ 在 $D$ 中没有零点，把定理用于 $1/f$，得到最小模原理：此时 $|f|$ 在 $\bar D$ 上的最小值也在 $\partial D$ 上取得。关于零点的条件是必要的：$\mathbb{D}$ 上的 $f(z)=z$ 在圆心处取得最小模 $0$。

![f(z) = z^2 + 2z - 1 在闭单位圆盘上的模。曲面 |f| 在圆盘内部没有峰；它的最大值 2 sqrt 2 在边界圆周上的 z = i 与 z = -i 处取得（右图）。最小值 0 在内部取得，即 f 的零点 sqrt 2 - 1 处。](./plots/max-modulus.py)

**例 4.6.1** 求 $\max_{|z|\le1}|z^2+2z-1|$。由定理 4.6.1，只需考虑 $z=\mathrm{e}^{\mathrm{i}t}$。除以 $|\mathrm{e}^{\mathrm{i}t}|=1$ 后，

$$
\big|\mathrm{e}^{2\mathrm{i}t}+2\mathrm{e}^{\mathrm{i}t}-1\big|=\big|\mathrm{e}^{\mathrm{i}t}+2-\mathrm{e}^{-\mathrm{i}t}\big|=|2+2\mathrm{i}\sin t|=2\sqrt{1+\sin^2t}.
$$

最大值为 $2\sqrt2$，在 $z=\pm\mathrm{i}$ 处取得。

### 4.6.2. 调和函数

通过定理 2.5.2，本章的结果可以转移到调和函数上。

**定理 4.6.2（调和函数的平均值性质与最大值原理）** 设 $u$ 在区域 $D$ 上调和。则

1. $u$ 在 $D$ 上有各阶连续偏导数；
2. 对 $D$ 中每个闭圆盘 $|z-z_0|\le r$，$u(z_0)=\frac1{2\pi}\int_0^{2\pi}u\big(z_0+r\mathrm{e}^{\mathrm{i}t}\big)\,\mathrm{d}t$；
3. 若 $u$ 在 $D$ 的某一点处取得它在 $D$ 上的最大值或最小值，则 $u$ 为常数。因此，若 $D$ 有界且 $u$ 在 $\bar D$ 上连续，则 $\max_{\bar D}u$ 与 $\min_{\bar D}u$ 都在 $\partial D$ 上取得。

**证明** $D$ 中的每个圆盘 $B$ 都是单连通的，所以由定理 2.5.2，存在 $B$ 上的解析函数 $f$ 使在 $B$ 上 $u=\operatorname{Re}f$。对推论 4.4.2 与推论 4.4.1 取实部，即得 1 与 2。由 2，用定理 4.6.1 证明中的开闭集论证（把 $|f|$ 换成 $u$，最小值的情形换成 $-u$）即得 3。$\square$

**推论 4.6.1** 设 $D$ 是有界区域，$u_1,u_2$ 在 $D$ 上调和、在 $\bar D$ 上连续，且在 $\partial D$ 上 $u_1=u_2$。则在 $D$ 上 $u_1=u_2$。

**证明** 差 $u_1-u_2$ 调和，在 $\bar D$ 上连续，在 $\partial D$ 上为零；由定理 4.6.2，它在 $\bar D$ 上的最大值和最小值都是 $0$。$\square$

所以 Laplace 方程的 Dirichlet 问题，即求 $D$ 上取给定边界值的调和函数 $u$，至多有一个解。存在性、Green 函数与 Poisson 公式在 [2.5.8](/2.5.8) 中讨论；共形映射（[2.3.8](/2.3.8)）则把圆盘或半平面上的显式解转移到其他区域。

## 小结

| 结论 | 内容 | 典型用途 |
|---|---|---|
| 参数化，式 (4.2) | $\int_Cf\,\mathrm{d}z=\int_a^bf(z(t))z'(t)\,\mathrm{d}t$ | 直接计算 |
| 式 (4.3) | $\oint_{\lvert z-z_0\rvert=r}(z-z_0)^n\,\mathrm{d}z$ 当 $n=-1$ 时为 $2\pi\mathrm{i}$，否则为 $0$ | 留数的基础 |
| 长大不等式 | $\lvert\int_Cf\,\mathrm{d}z\rvert\le ML$ | 证明圆弧上的积分趋于零 |
| Cauchy 定理 | 在单连通区域上 $\oint_Cf\,\mathrm{d}z=0$ | 积分与路径无关 |
| 闭路变形 | 积分路径避开奇点变形时积分不变 | 化为小圆周上的积分 |
| 原函数 | $\int_{z_1}^{z_2}f\,\mathrm{d}z=\Phi(z_2)-\Phi(z_1)$ | 整函数的积分 |
| 积分公式，式 (4.7) | $f^{(n)}(z)=\frac{n!}{2\pi\mathrm{i}}\oint_C\frac{f(\zeta)}{(\zeta-z)^{n+1}}\,\mathrm{d}\zeta$ | 计算积分；$f\in C^\infty$ |
| Cauchy 估计 | $\lvert f^{(n)}(z_0)\rvert\le n!M(R)/R^n$ | Liouville 定理，增长性论证 |
| Liouville 定理 | 有界整函数 $\Rightarrow$ 常数 | 代数基本定理 |
| Morera 定理 | 三角形上的积分为零 $\Rightarrow$ 解析 | 解析函数的极限 |
| 最大模原理 | $\max\lvert f\rvert$ 在边界上取得 | 估计、唯一性 |
