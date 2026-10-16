---
title: 初等函数
source_hash: 8afe39c4d34e
---

微积分中的初等函数可以推广到复变量，推广之后它们既得到了统一，也变得复杂了。统一在于：指数函数、正弦、余弦和双曲函数成了同一个函数 $\mathrm{e}^z$ 沿不同方向的表现，$\cos^2z+\sin^2z=1$ 之类的恒等式依然成立。复杂在于：$\mathrm{e}^z$ 以纯虚数 $2\pi\mathrm{i}$ 为周期，所以它的反函数对数是多值的，所有的幂 $z^\alpha$ 和反三角函数也随之多值。要使这类函数单值解析，就要在适当割开的区域上选取分支，这是本章的核心技能，在 [2.3.4](/2.3.4) 与 [2.3.7](/2.3.7) 的积分计算中经常用到。我们直接通过实部和虚部定义指数函数；它与幂级数 $\sum z^n/n!$ 一致，将在 [2.3.5](/2.3.5) 中证明。解析性用 [2.3.2](/2.3.2) 的 Cauchy–Riemann 方程验证。

## 3.1. 指数函数

**定义 3.1.1（复指数函数）** 对 $z=x+\mathrm{i}y$，**复指数函数**定义为

$$
\mathrm{e}^z=\exp z=\mathrm{e}^x(\cos y+\mathrm{i}\sin y).
$$

当 $z=x$ 为实数时，它就是实指数函数；当 $z=\mathrm{i}y$ 时，它就是**欧拉公式**。如果要求一个在实轴上与 $\mathrm{e}^x$ 一致的整函数，这个定义就是唯一的选择（由 [2.3.5](/2.3.5) 的唯一性定理）；它也是满足 $f'=f$、$f(0)=1$ 的唯一整函数。

**定理 3.1.1** 指数函数具有以下性质。

1. $\mathrm{e}^z$ 是整函数，且 $(\mathrm{e}^z)'=\mathrm{e}^z$。
2. $\mathrm{e}^{z_1+z_2}=\mathrm{e}^{z_1}\mathrm{e}^{z_2}$；因此对 $n\in\mathbb{Z}$ 有 $(\mathrm{e}^z)^n=\mathrm{e}^{nz}$，且 $1/\mathrm{e}^z=\mathrm{e}^{-z}$。
3. $|\mathrm{e}^z|=\mathrm{e}^{\operatorname{Re}z}$，$\arg\mathrm{e}^z=\{\operatorname{Im}z+2k\pi\}$；特别地，对一切 $z$ 有 $\mathrm{e}^z\ne0$。
4. $\mathrm{e}^z$ 以 $2\pi\mathrm{i}$ 为周期，且 $\mathrm{e}^{z_1}=\mathrm{e}^{z_2}$ 当且仅当 $z_1-z_2\in2\pi\mathrm{i}\,\mathbb{Z}$。
5. $\overline{\mathrm{e}^z}=\mathrm{e}^{\bar z}$，且 $\lim_{z\to\infty}\mathrm{e}^z$ 不存在。

**证明** 1. 设 $u=\mathrm{e}^x\cos y$，$v=\mathrm{e}^x\sin y$，则 $u_x=\mathrm{e}^x\cos y=v_y$，$u_y=-\mathrm{e}^x\sin y=-v_x$，且都连续；由推论 2.2.1，$\mathrm{e}^z$ 是整函数，导数为 $u_x+\mathrm{i}v_x=\mathrm{e}^z$。

2. $\mathrm{e}^{x_1}\mathrm{e}^{x_2}=\mathrm{e}^{x_1+x_2}$，而由和角公式，$(\cos y_1+\mathrm{i}\sin y_1)(\cos y_2+\mathrm{i}\sin y_2)=\cos(y_1+y_2)+\mathrm{i}\sin(y_1+y_2)$。

3. 由定义直接读出。

4. 由 2，只需求出所有满足 $\mathrm{e}^z=1$ 的 $z$：此时 $\mathrm{e}^x=1$，$\cos y=1$，$\sin y=0$，所以 $x=0$，$y\in2\pi\mathbb{Z}$。

5. 第一式是显然的。沿正实轴 $\mathrm{e}^z\to+\infty$，沿负实轴 $\mathrm{e}^z\to0$，沿虚轴 $|\mathrm{e}^z|=1$。$\square$

周期性意味着 $\mathrm{e}^z$ 在每个水平带形 $\{a<\operatorname{Im}z\le a+2\pi\}$ 中取到它的每个值。具体地说，$w=\mathrm{e}^z$ 把竖直线 $\operatorname{Re}z=x$ 映到圆周 $|w|=\mathrm{e}^x$ 上（绕无穷多圈），把水平线 $\operatorname{Im}z=y$ 映为射线 $\arg w=y$。

![映射 w = exp(z)。在带形 -pi < Im z <= pi 中，竖直线段映为以 0 为圆心的圆周，水平直线映为从 0 出发的射线；两条边 Im z = pi 与 Im z = -pi 都映到负实轴上。阴影带形 0 < Im z < pi/6 映为张角为 pi/6 的角形区域。整个带形恰好覆盖去掉 0 的平面一次。](./plots/exp-map.py)

**定理 3.1.2** 映射 $w=\mathrm{e}^z$ 是从带形 $\{-\pi<\operatorname{Im}z\le\pi\}$ 到 $\mathbb{C}\setminus\{0\}$ 的双射，也是从开带形 $\{-\pi<\operatorname{Im}z<\pi\}$ 到割去负实轴的平面 $\mathbb{C}\setminus(-\infty,0]$ 的解析双射。

**证明** 对 $w\ne0$，$\mathrm{e}^{x+\mathrm{i}y}=w$ 即 $\mathrm{e}^x=|w|$ 且 $y\in\arg w$；在带形内唯一的选择是 $x=\ln|w|$，$y=\operatorname{Arg}w$。开带形对应于 $\operatorname{Arg}w\ne\pi$。$\square$

**例 3.1.1** 解方程 $\mathrm{e}^z=1+\sqrt3\,\mathrm{i}$。由于 $|1+\sqrt3\,\mathrm{i}|=2$，$\operatorname{Arg}(1+\sqrt3\,\mathrm{i})=\frac\pi3$，解为 $z=\ln2+\mathrm{i}\big(\frac\pi3+2k\pi\big)$，$k\in\mathbb{Z}$。另外，$|\mathrm{e}^{z^2}|=\mathrm{e}^{\operatorname{Re}z^2}=\mathrm{e}^{x^2-y^2}$，而 $|\mathrm{e}^{\mathrm{i}z}|=\mathrm{e}^{-y}$ 在上半平面有界；后一事实是 [2.3.7](/2.3.7) 中 Jordan 引理的基础。

**例 3.1.2** 求整函数 $f$，使 $\operatorname{Re}f=u=\mathrm{e}^x(x\cos y-y\sin y)$ 且 $f(0)=0$。先算 $u_x=\mathrm{e}^x(x\cos y-y\sin y+\cos y)$，$u_y=\mathrm{e}^x(-x\sin y-\sin y-y\cos y)$。用 [§2.5.3](/2.3.2#sec-2.5.3) 的方法 3，$f'(z)=u_x(z,0)-\mathrm{i}u_y(z,0)=\mathrm{e}^z(z+1)$，所以 $f(z)=z\mathrm{e}^z+\mathrm{i}c$，$c$ 为实数，由 $f(0)=0$ 得 $f(z)=z\mathrm{e}^z$。验证：$\operatorname{Re}\big((x+\mathrm{i}y)\mathrm{e}^x(\cos y+\mathrm{i}\sin y)\big)=\mathrm{e}^x(x\cos y-y\sin y)$。

## 3.2. 对数函数

### 3.2.1. 多值的对数

由于 $\mathrm{e}^z$ 不是单射，它的反函数不是通常意义下的函数。与定理 3.1.2 一样，方程 $\mathrm{e}^w=z$（$z\ne0$）的解为 $w=\ln|z|+\mathrm{i}\theta$，$\theta\in\arg z$。

**定义 3.2.1（复对数）** 对 $z\ne0$，方程 $\mathrm{e}^w=z$ 的全体解 $w$ 组成的集合称为 $z$ 的**复对数**：

$$
\log z=\ln|z|+\mathrm{i}\arg z=\{\ln|z|+\mathrm{i}(\operatorname{Arg}z+2k\pi)\mid k\in\mathbb{Z}\},
$$
其中 $\ln$ 是实的自然对数。$k=0$ 的值
$$
\operatorname{Log}z=\ln|z|+\mathrm{i}\operatorname{Arg}z,\qquad -\pi<\operatorname{Im}\operatorname{Log}z\le\pi
$$
称为**对数主值**。$0$ 的对数没有定义。

各教材的记号不尽相同：国内教材多用 $\operatorname{Ln}z$ 表示多值的对数，用 $\ln z$ 表示它的主值。本站沿用多数英文文献的记号 $\log z$ 与 $\operatorname{Log}z$，$\ln$ 只用于实变量。

**例 3.2.1** $\operatorname{Log}(-1)=\mathrm{i}\pi$，$\log(-1)=\{(2k+1)\pi\mathrm{i}\}$；$\log\mathrm{i}=\{\mathrm{i}(\frac\pi2+2k\pi)\}$；$\operatorname{Log}(-1-\mathrm{i})=\frac12\ln2-\frac{3\pi}4\mathrm{i}$；$\log1=\{2k\pi\mathrm{i}\}$：即使是正实数，也有无穷多个复对数，其中只有主值是实数。

作为集合，

$$
\log(z_1z_2)=\log z_1+\log z_2,\qquad \log\frac{z_1}{z_2}=\log z_1-\log z_2,
$$

这由 $\arg$ 的相应等式（[2.3.1](/2.3.1) 的 §1.1.2）得到。有两条熟悉的法则不再成立。其一，一般地 $\operatorname{Log}(z_1z_2)\ne\operatorname{Log}z_1+\operatorname{Log}z_2$：$\operatorname{Log}\big((-1)(-1)\big)=0$，而 $\operatorname{Log}(-1)+\operatorname{Log}(-1)=2\pi\mathrm{i}$。其二，$n\ge2$ 时 $\log z^n\ne n\log z$：集合 $n\log z=\{n\ln|z|+\mathrm{i}n(\operatorname{Arg}z+2k\pi)\}$ 只含 $\log z^n$ 中每隔 $n$ 个取一个的值；例如 $\log\mathrm{i}^2=\log(-1)$ 含 $-\pi\mathrm{i}$，而 $2\log\mathrm{i}$ 不含。另一方面，对每个值都有 $\mathrm{e}^{\log z}=z$，且 $\log\mathrm{e}^z=\{z+2k\pi\mathrm{i}\}$。

### 3.2.2. 分支、支割线与支点

要对对数做分析，需要一个单值函数，而且希望它连续。

**定义 3.2.2（分支）** 设 $F$ 是多值函数，$D$ 是区域。若 $D$ 上的连续（单值）函数 $f$ 对每个 $z\in D$ 都满足 $f(z)$ 是 $F(z)$ 的值之一，则称 $f$ 为 $F$ 在 $D$ 上的一个**单值分支**。

**定理 3.2.1** $\operatorname{Log}z$ 是 $\log z$ 在割去负实轴的平面 $\mathbb{C}\setminus(-\infty,0]$ 上的一个分支，它在该区域上解析，且

$$
(\operatorname{Log}z)'=\frac1z.
$$

$\log z$ 在这个区域上的每个分支都具有 $\operatorname{Log}z+2k\pi\mathrm{i}$ 的形式（$k\in\mathbb{Z}$ 固定），导数相同。

**证明** $\ln|z|$ 在 $\mathbb{C}\setminus\{0\}$ 上连续，$\operatorname{Arg}z$ 在割去负实轴的平面上连续（[2.3.1](/2.3.1) 的例 1.4.3），所以 $\operatorname{Log}$ 在该区域上连续。它是从开带形 $|\operatorname{Im}w|<\pi$ 到割去负实轴的平面的解析双射 $\mathrm{e}^w$ 的反函数（定理 3.1.2），且 $(\mathrm{e}^w)'=\mathrm{e}^w\ne0$，由 [2.3.2](/2.3.2) §2.1 的反函数求导法则，它复可导，导数为 $\frac{1}{\mathrm{e}^w}=\frac1z$。（也可以用极坐标形式：$u=\ln r$，$v=\theta$ 满足 $u_r=\frac1r=\frac1rv_\theta$，$v_r=0=-\frac1ru_\theta$，由式 (2.4) 得 $f'=\mathrm{e}^{-\mathrm{i}\theta}\cdot\frac1r=\frac1z$。）若 $f$ 是另一个分支，则 $\frac{f(z)-\operatorname{Log}z}{2\pi\mathrm{i}}$ 是连通集上取整数值的连续函数，因而是常数。$\square$

对 $\log z$ 本身而言，负实轴并无特殊之处。也可以割去从 $0$ 到 $\infty$ 的任何一条射线：例如在 $\mathbb{C}\setminus[0,+\infty)$ 上，取辐角在 $(0,2\pi)$ 中，就得到分支 $\ln|z|+\mathrm{i}\theta$，$0<\theta<2\pi$。不可避免的是必须割去某条从 $0$ 到 $\infty$ 的曲线，原因在于下面的现象。

**定义 3.2.3（支点）** 设 $F$ 是多值函数。若对 $z_0\in\hat{\mathbb{C}}$ 周围每个充分小的圆周（$z_0=\infty$ 时：每个充分大的圆周 $|z|=R$），从圆周上一点处 $F$ 的某个值出发，沿圆周连续地变动绕行一周，回到出发点时得到的是另一个值，则称 $z_0$ 为 $F$ 的**支点**。

对 $\log z$，沿任何以 $0$ 为圆心的圆周按逆时针方向连续地追踪 $\ln|z|+\mathrm{i}\theta$ 绕行一周，$\theta$ 增加 $2\pi$，值增加 $2\pi\mathrm{i}$，所以 $0$ 是支点；这些圆周同时也是绕 $\infty$ 的大圆周，所以 $\infty$ 也是支点。为使函数单值而从区域中割去的曲线称为支割线（branch cut）；对 $\log z$，支割线必须连接两个支点 $0$ 与 $\infty$，因为若区域中有某条闭曲线绕 $0$，就不存在分支。沿负实轴割开时，$\operatorname{Log}$ 在割线上岸与下岸的值相差 $2\pi\mathrm{i}$：

$$
\lim_{\varepsilon\to0^+}\operatorname{Log}(x+\mathrm{i}\varepsilon)-\lim_{\varepsilon\to0^+}\operatorname{Log}(x-\mathrm{i}\varepsilon)=2\pi\mathrm{i}\qquad(x<0).
$$

[2.3.7](/2.3.7) 中钥匙孔形围道之所以奏效，正是因为这个跳跃。

### 3.2.3. Riemann 面

Riemann 的想法不是割开平面，而是扩大定义域。取可数个割去负实轴的平面的副本（"叶"）$S_k$，$k\in\mathbb{Z}$，$S_k$ 上取分支 $\operatorname{Log}z+2k\pi\mathrm{i}$，再把 $S_k$ 上割线的下岸与 $S_{k+1}$ 上割线的上岸粘合。得到一个连通的螺旋面，称为 $\log z$ 的 Riemann 面（Riemann surface），$\log$ 在它上面是单值解析函数：绕 $0$ 一周，就走到下一叶。对 $\sqrt z$，两叶就够了，沿割线交叉粘合，因为绕 $0$ 两周后回到原来的值。

![Riemann 面。左：高度为 Im log z = arg z，绕原点三周；每一周是一叶，各叶连成绕支点 0 的一个螺旋面。右：高度为 Re sqrt z，绕原点两周；绕一周后曲面以相反的符号回来，绕两周后闭合。](./plots/riemann-surfaces.py)

本课程中 Riemann 面只作为直观图像，计算都用割开的区域上的分支进行。

## 3.3. 幂函数与一般指数函数

**定义 3.3.1（复幂函数）** 对 $z\ne0$ 与 $\alpha\in\mathbb{C}$，

$$
z^\alpha=\mathrm{e}^{\alpha\log z}=\{\exp\big(\alpha(\operatorname{Log}z+2k\pi\mathrm{i})\big)\mid k\in\mathbb{Z}\};
$$

其中 $\mathrm{e}^{\alpha\operatorname{Log}z}$ 称为主值。类似地，对 $a\ne0$，一般指数函数为 $a^z=\mathrm{e}^{z\log a}$；约定 $\mathrm{e}^z$ 总是表示 §3.1 中的指数函数，而不是多值的 $\exp(z\log\mathrm{e})$。

$z^\alpha$ 有多少个不同的值，由因子 $\mathrm{e}^{2k\pi\mathrm{i}\alpha}$ 决定：

| $\alpha$ | $z^\alpha$ 的值 |
|---|---|
| 整数 $n$ | 一个值，即通常的幂 $z^n$ |
| 既约有理数 $p/q$，$q\ge2$ | 恰好 $q$ 个值，即 $z^p$ 的 $q$ 次方根 |
| 无理数或非实数 | 无穷多个值 |

**例 3.3.1** 计算 $\mathrm{i}^{\mathrm{i}}$、$\mathrm{i}^\pi$ 与 $1^{\sqrt2}$。

- $\mathrm{i}^{\mathrm{i}}=\exp\big(\mathrm{i}\cdot\mathrm{i}(\frac\pi2+2k\pi)\big)=\mathrm{e}^{-\pi/2-2k\pi}$，$k\in\mathbb{Z}$：无穷多个值，全是正实数；主值为 $\mathrm{e}^{-\pi/2}$。
- $\mathrm{i}^\pi=\exp\big(\pi\cdot\mathrm{i}(\frac\pi2+2k\pi)\big)=\cos\big(\frac{\pi^2}2+2k\pi^2\big)+\mathrm{i}\sin\big(\frac{\pi^2}2+2k\pi^2\big)$：单位圆周上的无穷多个值（因为 $\pi$ 是无理数，它们互不相同）；主值为 $\mathrm{e}^{\mathrm{i}\pi^2/2}$。
- $1^{\sqrt2}=\mathrm{e}^{2\sqrt2k\pi\mathrm{i}}$：单位圆周上的无穷多个点，在圆周上稠密，尽管主值为 $1$。

**定理 3.3.1** 在割去负实轴的平面 $\mathbb{C}\setminus(-\infty,0]$ 上，主值 $z^\alpha=\mathrm{e}^{\alpha\operatorname{Log}z}$ 解析，且 $(z^\alpha)'=\alpha\,\dfrac{z^\alpha}{z}$。对每个分支 $\mathrm{e}^{\alpha f(z)}$（$f$ 是 $\log$ 在区域 $D$ 上的分支），同一公式成立。

**证明** 由链式法则，$(\mathrm{e}^{\alpha f(z)})'=\mathrm{e}^{\alpha f(z)}\cdot\frac{\alpha}{z}$。$\square$

$\alpha$ 不是整数时，$z^\alpha$ 的支点与 $\log z$ 一样是 $0$ 与 $\infty$。平方根 $\sqrt z=z^{1/2}$ 在割去负实轴的平面上有两个分支 $\pm\sqrt{|z|}\,\mathrm{e}^{\mathrm{i}\operatorname{Arg}z/2}$；绕 $0$ 一周，值乘以 $\mathrm{e}^{\mathrm{i}\pi}=-1$。

**例 3.3.2** 设 $f$ 是 $\sqrt z$ 在 $\mathbb{C}\setminus[0,+\infty)$ 上满足 $f(-1)=\mathrm{i}$ 的分支，求 $f(\mathrm{i})$ 与 $f(-\mathrm{i})$。在这个区域上可以写 $z=r\mathrm{e}^{\mathrm{i}\theta}$，$0<\theta<2\pi$，两个分支为 $\pm\sqrt r\,\mathrm{e}^{\mathrm{i}\theta/2}$。在 $z=-1$（$\theta=\pi$）处，取正号得 $\mathrm{e}^{\mathrm{i}\pi/2}=\mathrm{i}$，所以 $f(z)=\sqrt r\,\mathrm{e}^{\mathrm{i}\theta/2}$。因此 $f(\mathrm{i})=\mathrm{e}^{\mathrm{i}\pi/4}=\frac{1+\mathrm{i}}{\sqrt2}$，$f(-\mathrm{i})=\mathrm{e}^{3\pi\mathrm{i}/4}=\frac{-1+\mathrm{i}}{\sqrt2}$。注意 $f(-\mathrm{i})$ 不是主值 $\mathrm{e}^{-\mathrm{i}\pi/4}$。

**例 3.3.3** 函数 $F(z)=\sqrt{z^2-1}=\sqrt{(z-1)(z+1)}$ 以 $1$ 与 $-1$ 为支点，但 $\infty$ 不是支点。沿一条闭曲线连续地追踪一个值，它乘以 $(-1)^{m}$，其中 $m$ 是曲线绕 $1$ 与绕 $-1$ 的总圈数。大圆周绕两者各一圈，$m=2$，值回到原来的值。因此 $F$ 在 $\mathbb{C}\setminus[-1,1]$ 上有两个解析分支，其中一个当 $z\to\infty$ 时性态像 $z$。一般地，哪些点是支点必须逐一检验，只看根号下表达式的零点是不够的。

## 3.4. 三角函数与双曲函数

由欧拉公式，对实数 $y$ 有 $\cos y=\frac{\mathrm{e}^{\mathrm{i}y}+\mathrm{e}^{-\mathrm{i}y}}{2}$，$\sin y=\frac{\mathrm{e}^{\mathrm{i}y}-\mathrm{e}^{-\mathrm{i}y}}{2\mathrm{i}}$。我们把它们作为复变量情形的定义。

**定义 3.4.1（复三角函数与双曲函数）** 对 $z\in\mathbb{C}$，

$$
\cos z=\frac{\mathrm{e}^{\mathrm{i}z}+\mathrm{e}^{-\mathrm{i}z}}{2},\qquad \sin z=\frac{\mathrm{e}^{\mathrm{i}z}-\mathrm{e}^{-\mathrm{i}z}}{2\mathrm{i}},\qquad \cosh z=\frac{\mathrm{e}^{z}+\mathrm{e}^{-z}}{2},\qquad \sinh z=\frac{\mathrm{e}^{z}-\mathrm{e}^{-z}}{2},
$$

并在分母不为零处定义 $\tan z=\frac{\sin z}{\cos z}$，$\cot z=\frac{\cos z}{\sin z}$，$\tanh z=\frac{\sinh z}{\cosh z}$。

它们推广了实三角函数与实**双曲函数**，由定义立即得到

$$
\cos(\mathrm{i}z)=\cosh z,\qquad \sin(\mathrm{i}z)=\mathrm{i}\sinh z,\qquad \cosh(\mathrm{i}z)=\cos z,\qquad \sinh(\mathrm{i}z)=\mathrm{i}\sin z.
$$

所以在 $\mathbb{C}$ 上，三角函数与双曲函数是同一组函数，只是自变量旋转了一下。

**定理 3.4.1** 对一切 $z,z_1,z_2\in\mathbb{C}$，下列结论成立。

1. $\sin z$ 与 $\cos z$ 是整函数，$(\sin z)'=\cos z$，$(\cos z)'=-\sin z$；$\sin$ 是奇函数，$\cos$ 是偶函数，两者都以 $2\pi$ 为周期。
2. 实的和角公式全部保持成立，例如 $\sin(z_1+z_2)=\sin z_1\cos z_2+\cos z_1\sin z_2$，$\sin^2z+\cos^2z=1$。
3. 设 $z=x+\mathrm{i}y$，则 $\sin z=\sin x\cosh y+\mathrm{i}\cos x\sinh y$，$\cos z=\cos x\cosh y-\mathrm{i}\sin x\sinh y$，且

$$
|\sin z|^2=\sin^2x+\sinh^2y,\qquad |\cos z|^2=\cos^2x+\sinh^2y.
$$

4. $\sin z$ 的零点恰为 $z=k\pi$，$\cos z$ 的零点恰为 $z=\frac\pi2+k\pi$（$k\in\mathbb{Z}$）。
5. $\sin z$ 与 $\cos z$ 在 $\mathbb{C}$ 上无界。

**证明** 1 由定义 3.4.1 与定理 3.1.1 得到。对 2，每个恒等式两边都是 $\mathrm{e}^{\pm\mathrm{i}z_1}$ 与 $\mathrm{e}^{\pm\mathrm{i}z_2}$ 的多项式，展开即可验证（或者：它们对实变量成立，由 [2.3.5](/2.3.5) 的唯一性定理推广到复变量）。对 3，利用和角公式以及 $\cos(\mathrm{i}y)=\cosh y$、$\sin(\mathrm{i}y)=\mathrm{i}\sinh y$，再由 $\cosh^2y=1+\sinh^2y$ 得 $|\sin z|^2=\sin^2x\cosh^2y+\cos^2x\sinh^2y=\sin^2x+\sinh^2y$；$\cos$ 同理。对 4，$\sin z=0$ 即 $\mathrm{e}^{2\mathrm{i}z}=1$，由定理 3.1.1 即 $2\mathrm{i}z\in2\pi\mathrm{i}\mathbb{Z}$；又 $\cos z=\sin\big(\frac\pi2-z\big)$。5 由 3 得到：$|\sin(\mathrm{i}y)|=|\sinh y|\to\infty$。$\square$

性质 5 与实的情形形成鲜明对比。这并非偶然：由 [2.3.4](/2.3.4) 的 Liouville 定理，有界整函数必为常数。性质 4 说明复化不产生新的零点，因此 $\tan z$ 与 $\cot z$ 除了 $\cos$ 与 $\sin$ 的实零点之外处处解析。

**例 3.4.1** 解方程 $\cos z=2$。令 $t=\mathrm{e}^{\mathrm{i}z}$，方程化为 $t+\frac1t=4$，即 $t^2-4t+1=0$，所以 $t=2\pm\sqrt3$。于是 $\mathrm{i}z\in\log(2\pm\sqrt3)=\{\ln(2\pm\sqrt3)+2k\pi\mathrm{i}\}$，又 $\ln(2-\sqrt3)=-\ln(2+\sqrt3)$，故

$$
z=2k\pi\pm\mathrm{i}\ln\big(2+\sqrt3\big),\qquad k\in\mathbb{Z}.
$$

所有的解都在竖直线 $\operatorname{Re}z=2k\pi$ 上，在这些直线上 $\cos(2k\pi+\mathrm{i}y)=\cosh y$ 取遍一切 $\ge1$ 的值。

**例 3.4.2** 解方程 $\sin z=\mathrm{i}$。令 $t=\mathrm{e}^{\mathrm{i}z}$，由 $\frac{t-t^{-1}}{2\mathrm{i}}=\mathrm{i}$ 得 $t^2+2t-1=0$，所以 $t=-1\pm\sqrt2$。对 $t=\sqrt2-1>0$：$\mathrm{i}z=\ln(\sqrt2-1)+2k\pi\mathrm{i}$，故 $z=2k\pi+\mathrm{i}\ln(1+\sqrt2)$。对 $t=-(1+\sqrt2)<0$：$\mathrm{i}z=\ln(1+\sqrt2)+\mathrm{i}(\pi+2k\pi)$，故 $z=(2k+1)\pi-\mathrm{i}\ln(1+\sqrt2)$。验证：$\sin\big(\mathrm{i}\ln(1+\sqrt2)\big)=\mathrm{i}\sinh\ln(1+\sqrt2)=\mathrm{i}\cdot\frac{(1+\sqrt2)-(\sqrt2-1)}{2}=\mathrm{i}$，再由 $\sin(\pi-w)=\sin w$ 得第二族解。

## 3.5. 反三角函数

像例 3.4.1 与例 3.4.2 那样从 $\cos w=z$、$\sin w=z$、$\tan w=z$ 中解出 $w$，会得到关于 $t=\mathrm{e}^{\mathrm{i}w}$ 的二次方程，进而得到对数。因此复的**反三角函数**是多值的，可以用 $\log$ 与平方根表示：

$$
\operatorname{Arccos}z=-\mathrm{i}\log\big(z+\sqrt{z^2-1}\big),\qquad \operatorname{Arcsin}z=-\mathrm{i}\log\big(\mathrm{i}z+\sqrt{1-z^2}\big),\qquad \operatorname{Arctan}z=\frac{1}{2\mathrm{i}}\log\frac{1+\mathrm{i}z}{1-\mathrm{i}z}\ (z\ne\pm\mathrm{i}),
$$

右端的平方根与对数取所有的值。例如，令 $t=\mathrm{e}^{\mathrm{i}w}$，则 $\tan w=\frac{t^2-1}{\mathrm{i}(t^2+1)}$；令它等于 $z$ 并解出 $t^2=\frac{1+\mathrm{i}z}{1-\mathrm{i}z}$，就得到 $\operatorname{Arctan}$ 的公式。在取定了平方根与对数的分支的区域上，它们解析，导数是熟悉的形式

$$
(\arcsin z)'=\frac{1}{\sqrt{1-z^2}},\qquad (\arctan z)'=\frac{1}{1+z^2},
$$

其中第一式的平方根取定义中所用的那个分支。$\operatorname{Arcsin}$ 与 $\operatorname{Arccos}$ 的支点是 $\pm1$ 与 $\infty$，$\operatorname{Arctan}$ 的支点是 $\pm\mathrm{i}$；对 $\operatorname{Arctan}$，$\infty$ 不是支点，因为当 $z\to\infty$ 时 $\frac{1+\mathrm{i}z}{1-\mathrm{i}z}\to-1$。

**例 3.5.1** $\operatorname{Arctan}(2\mathrm{i})=\frac1{2\mathrm{i}}\log\frac{1-2}{1+2}=\frac1{2\mathrm{i}}\log\big(-\tfrac13\big)=\frac1{2\mathrm{i}}\big(-\ln3+\mathrm{i}(2k+1)\pi\big)=\big(k+\tfrac12\big)\pi+\frac{\mathrm{i}}2\ln3$。

## 小结

| 函数 | 定义 | 取值 | 支点 | 主值支及其区域 |
|---|---|---|---|---|
| $\mathrm{e}^z$ | $\mathrm{e}^x(\cos y+\mathrm{i}\sin y)$ | 单值，周期 $2\pi\mathrm{i}$，不取 $0$ | 无 | 整函数 |
| $\log z$ | $\ln\lvert z\rvert+\mathrm{i}\arg z$ | 无穷多个，相差 $2\pi\mathrm{i}$ 的整数倍 | $0,\infty$ | $\operatorname{Log}z$，在 $\mathbb{C}\setminus(-\infty,0]$ 上，导数 $1/z$ |
| $z^\alpha$ | $\mathrm{e}^{\alpha\log z}$ | $1$ 个、$q$ 个或无穷多个 | $0,\infty$（$\alpha\notin\mathbb{Z}$） | $\mathrm{e}^{\alpha\operatorname{Log}z}$，导数 $\alpha z^\alpha/z$ |
| $\sin z$，$\cos z$ | $\mathrm{e}^{\pm\mathrm{i}z}$ 的组合 | 单值，周期 $2\pi$，无界 | 无 | 整函数；零点都是实数 |
| $\operatorname{Arcsin}$，$\operatorname{Arccos}$，$\operatorname{Arctan}$ | 代数式的 $\log$ | 无穷多个 | $\pm1,\infty$；$\pm\mathrm{i}$ | 割开的区域上的分支 |
