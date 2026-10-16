---
title: 复数与复平面
source_hash: bd627844d85c
---

复变函数论研究复变量的函数 $w=f(z)$ 中在复意义下可导的那一类。这类函数比实变量的可导函数刚性得多，也有用得多：可导一次就意味着可导无穷多次，曲线上的值决定曲线内部的值，微积分中各种技巧都对付不了的实积分，只要把几个留数加起来就能算出。在这一切之前，先要搭好舞台。本章复习复数的运算与几何（线性代数 [2.1.9](/2.1.9) 中已经见过），侧重复分析需要的部分：多值的辐角及其主值、方根、无穷远点与 Riemann 球面、平面点集的拓扑（区域、曲线、单连通性），以及复变函数的极限与连续性。平面拓扑就是多元微积分中 $\mathbb{R}^2$ 的拓扑（[2.2.10](/2.2.10)），本章的要点在于分辨哪些结论可以原样照搬，哪些新现象（点 $\infty$、辐角主值的间断）需要留意。导数在 [2.3.2](/2.3.2) 引入。

## 1.1. 复数

### 1.1.1. 代数形式

**复数**是形如 $z=x+\mathrm{i}y$ 的数，其中 $x,y\in\mathbb{R}$，$\mathrm{i}^2=-1$；$x=\operatorname{Re}z$ 与 $y=\operatorname{Im}z$ 分别称为它的实部与虚部，两个复数相等当且仅当实部与虚部分别相等。加法与乘法按多项式运算并利用 $\mathrm{i}^2=-1$，$\mathbb{C}$ 构成一个域。$z$ 的**共轭复数**是 $\bar z=x-\mathrm{i}y$，**模**是 $|z|=\sqrt{x^2+y^2}$。把 $z=x+\mathrm{i}y$ 与点 $(x,y)$ 等同，$\mathbb{C}$ 就成为复平面，实轴与虚轴为坐标轴；$|z_1-z_2|$ 就是点 $z_1$ 与 $z_2$ 之间的 Euclid 距离。

**命题 1.1.1** 对任意 $z,z_1,z_2\in\mathbb{C}$：

1. $\overline{z_1\pm z_2}=\bar z_1\pm\bar z_2$，$\overline{z_1z_2}=\bar z_1\bar z_2$，$\overline{z_1/z_2}=\bar z_1/\bar z_2$（$z_2\ne0$），$\bar{\bar z}=z$；
2. $z\bar z=|z|^2$，$\operatorname{Re}z=\dfrac{z+\bar z}{2}$，$\operatorname{Im}z=\dfrac{z-\bar z}{2\mathrm{i}}$；
3. $|z_1z_2|=|z_1|\,|z_2|$，$|\bar z|=|z|$，且 $\max\{|\operatorname{Re}z|,|\operatorname{Im}z|\}\le|z|\le|\operatorname{Re}z|+|\operatorname{Im}z|$；
4. （三角不等式）$\big||z_1|-|z_2|\big|\le|z_1+z_2|\le|z_1|+|z_2|$。

**证明** 1、2 直接计算即得。对 3，$|z_1z_2|^2=z_1z_2\overline{z_1z_2}=z_1\bar z_1\,z_2\bar z_2=|z_1|^2|z_2|^2$；不等式由 $x^2\le x^2+y^2\le(|x|+|y|)^2$ 得到。对 4，

$$
|z_1+z_2|^2=(z_1+z_2)(\bar z_1+\bar z_2)=|z_1|^2+|z_2|^2+2\operatorname{Re}(z_1\bar z_2)\le|z_1|^2+|z_2|^2+2|z_1|\,|z_2|=(|z_1|+|z_2|)^2,
$$

这里用到 $\operatorname{Re}(z_1\bar z_2)\le|z_1\bar z_2|=|z_1|\,|z_2|$。把它用于 $z_1=(z_1+z_2)+(-z_2)$ 得 $|z_1|-|z_2|\le|z_1+z_2|$，交换两者的地位即得左边的不等式。$\square$

由 2 可以在实坐标 $(x,y)$ 与数对 $(z,\bar z)$ 之间相互转换：$x=\frac{z+\bar z}{2}$，$y=\frac{z-\bar z}{2\mathrm{i}}$。这一变量替换是 [2.3.2](/2.3.2) 中 Wirtinger 导数的基础。

### 1.1.2. 三角形式与辐角

每个 $z\ne0$ 都可以写成**三角形式** $z=r(\cos\theta+\mathrm{i}\sin\theta)=r\mathrm{e}^{\mathrm{i}\theta}$，其中 $r=|z|$，$\theta$ 是 $z$ 的一个**辐角**，即从正实轴到向量 $z$ 的转角；后一种写法（指数形式）用到**欧拉公式** $\mathrm{e}^{\mathrm{i}\theta}=\cos\theta+\mathrm{i}\sin\theta$（[2.1.9](/2.1.9)）。由于 $\mathrm{e}^{\mathrm{i}\theta}$ 以 $2\pi$ 为周期，辐角只确定到 $2\pi$ 的整数倍。在复分析中这种不确定性不能置之不理：[2.3.3](/2.3.3) 中所有的多值函数都源于它。因此我们既给全体辐角组成的集合命名，也取定一个代表。

**定义 1.1.1（辐角主值）** 设 $z\ne0$，$z$ 的全体辐角组成的集合记作 $\arg z$。其中落在 $(-\pi,\pi]$ 内的唯一一个称为 $z$ 的**辐角主值**，记作 $\operatorname{Arg}z$。于是

$$
\arg z=\{\operatorname{Arg}z+2k\pi\mid k\in\mathbb{Z}\}.
$$

$0$ 的辐角没有定义。

本站采用国际通行的记号：小写 $\arg$ 表示多值的辐角，大写 $\operatorname{Arg}$ 表示主值。国内教材常用相反的记号，以 $\operatorname{Arg}z$ 表示全体辐角、$\arg z$ 表示主值，阅读时需要注意。

设 $z=x+\mathrm{i}y\ne0$，辐角主值由 $\arctan\frac yx\in\left(-\frac\pi2,\frac\pi2\right)$ 按象限修正得到：

$$
\operatorname{Arg}z=\begin{cases}\arctan\dfrac yx, & x>0,\\[2mm] \arctan\dfrac yx+\pi, & x<0,\ y\ge0,\\[2mm] \arctan\dfrac yx-\pi, & x<0,\ y<0,\\[2mm] \pm\dfrac\pi2, & x=0,\ y\gtrless0.\end{cases}
$$

例如 $\operatorname{Arg}(-1)=\pi$，$\operatorname{Arg}(-\mathrm{i})=-\frac\pi2$，$\operatorname{Arg}(-1-\sqrt3\,\mathrm{i})=\frac\pi3-\pi=-\frac{2\pi}3$。

乘法使模相乘、辐角相加：若 $z_k=r_k\mathrm{e}^{\mathrm{i}\theta_k}$，则

$$
z_1z_2=r_1r_2\mathrm{e}^{\mathrm{i}(\theta_1+\theta_2)},\qquad \frac{z_1}{z_2}=\frac{r_1}{r_2}\mathrm{e}^{\mathrm{i}(\theta_1-\theta_2)}.
$$

几何上，乘以 $z_2$ 就是把平面旋转 $\theta_2$ 并伸缩 $r_2$ 倍。作为集合之间的等式，$\arg(z_1z_2)=\arg z_1+\arg z_2$ 与 $\arg(z_1/z_2)=\arg z_1-\arg z_2$ 严格成立（两个集合的和指各取一个元素相加所得的全体）。对主值它们可能不成立：$\operatorname{Arg}(-1)+\operatorname{Arg}(-1)=2\pi\ne0=\operatorname{Arg}\big((-1)(-1)\big)$。因此涉及 $\operatorname{Arg}$ 的等式一般只在相差 $2\pi$ 的整数倍的意义下成立，这一点在对数函数中还会遇到。

反复使用乘积公式，得到 De Moivre 公式（de Moivre's formula）

$$
(\cos\theta+\mathrm{i}\sin\theta)^n=\cos n\theta+\mathrm{i}\sin n\theta\qquad(n\in\mathbb{Z}).
$$

**例 1.1.1** 计算 $\left(\dfrac{1+\sqrt3\,\mathrm{i}}{1-\mathrm{i}}\right)^{12}$。由于 $1+\sqrt3\,\mathrm{i}=2\mathrm{e}^{\mathrm{i}\pi/3}$，$1-\mathrm{i}=\sqrt2\,\mathrm{e}^{-\mathrm{i}\pi/4}$，商为 $\sqrt2\,\mathrm{e}^{\mathrm{i}7\pi/12}$，其 12 次幂为 $2^6\mathrm{e}^{\mathrm{i}7\pi}=-64$。

**例 1.1.2** 用二项式定理展开 $(\cos\theta+\mathrm{i}\sin\theta)^3$，与 De Moivre 公式比较实部和虚部，得 $\cos3\theta=\cos^3\theta-3\cos\theta\sin^2\theta=4\cos^3\theta-3\cos\theta$，$\sin3\theta=3\sin\theta-4\sin^3\theta$。同样地，对 $\theta\notin2\pi\mathbb{Z}$，求几何级数 $\sum_{k=0}^{n}\mathrm{e}^{\mathrm{i}k\theta}$ 的和再取实部，得

$$
\sum_{k=0}^{n}\cos k\theta=\frac12+\frac{\sin\big((n+\frac12)\theta\big)}{2\sin\frac\theta2},
$$

这就是 Fourier 级数中的 Dirichlet 核（[2.2.9](/2.2.9)）。

### 1.1.3. 方根

**定理 1.1.1（$n$ 次方根）** 设 $w=\rho\mathrm{e}^{\mathrm{i}\varphi}\ne0$，$n\ge1$。方程 $z^n=w$ 恰有 $n$ 个不同的解

$$
z_k=\sqrt[n]{\rho}\,\exp\Big(\mathrm{i}\,\frac{\varphi+2k\pi}{n}\Big),\qquad k=0,1,\dots,n-1.
$$

它们位于圆周 $|z|=\sqrt[n]\rho$ 上，是一个正 $n$ 边形的顶点。

**证明** 设 $z=r\mathrm{e}^{\mathrm{i}\theta}$，方程 $z^n=w$ 即 $r^n=\rho$ 且 $n\theta\in\varphi+2\pi\mathbb{Z}$，也就是 $r=\sqrt[n]\rho$，$\theta=\frac{\varphi+2k\pi}{n}$，$k\in\mathbb{Z}$。两个 $k$ 给出同一个 $z$ 当且仅当它们相差 $n$ 的倍数，所以 $k=0,\dots,n-1$ 恰好把每个解列出一次。$\square$

因此对复数 $w$，记号 $\sqrt[n]{w}$ 表示 $n$ 个值；$w=1$ 时它们是 $n$ 次**单位根** $\mathrm{e}^{2k\pi\mathrm{i}/n}$，$w$ 的每个方根都等于某个固定的方根乘以一个单位根。当 $w$ 变动时如何连续地选取其中一个值，是 [2.3.3](/2.3.3) 中分支的问题。

**例 1.1.3** 解方程 $z^4+16=0$。$-16=16\mathrm{e}^{\mathrm{i}\pi}$，故 $z_k=2\mathrm{e}^{\mathrm{i}(\pi/4+k\pi/2)}$，即 $z=\pm\sqrt2\pm\sqrt2\,\mathrm{i}$（四种符号组合），它们是一个正方形的顶点（[§1.3](#sec-1.3) 中插图的第一幅）。把共轭的根配对，得到实系数分解 $z^4+16=(z^2-2\sqrt2z+4)(z^2+2\sqrt2z+4)$。

### 1.1.4. 用复数方程表示的曲线与区域

由于 $|z-a|$ 是距离、$\operatorname{Arg}$ 是角度，许多平面图形都有简洁的复数表示：

| 方程或不等式 | 图形 |
|---|---|
| $\lvert z-z_0\rvert=r$，$\lvert z-z_0\rvert<r$ | 以 $z_0$ 为圆心、$r$ 为半径的圆周、开圆盘 |
| $\lvert z-a\rvert=\lvert z-b\rvert$ | 线段 $ab$ 的垂直平分线 |
| $\lvert z-a\rvert+\lvert z-b\rvert=2c$（$2c>\lvert a-b\rvert$） | 以 $a,b$ 为焦点的椭圆 |
| $\lvert z-a\rvert=k\lvert z-b\rvert$（$k>0$，$k\ne1$） | Apollonius 圆 |
| $\operatorname{Re}z>0$，$\operatorname{Im}z>0$ | 右半平面、上半平面 |
| $\alpha<\operatorname{Arg}z<\beta$ | 顶点在 $0$ 的开角形区域 |
| $\operatorname{Re}(\bar az)=c$（$a\ne0$，$c\in\mathbb{R}$） | 法方向为 $a$ 的直线 |

**例 1.1.4** 平面上的每个圆周和每条直线都有如下形式的方程：

$$
A z\bar z+\bar Bz+B\bar z+C=0,\qquad A,C\in\mathbb{R},\ B\in\mathbb{C},\ |B|^2>AC.
$$

事实上，$|z-z_0|^2=r^2$ 展开为 $z\bar z-\bar z_0z-z_0\bar z+|z_0|^2-r^2=0$，而直线 $\operatorname{Re}(\bar az)=c$ 即 $\bar az+a\bar z-2c=0$，是 $A=0$ 的情形。反之，若 $A\ne0$，两边除以 $A$ 再配方得 $|z+B/A|^2=(|B|^2-AC)/A^2>0$。这种"广义圆周"的形式立刻表明，反演 $w=1/z$ 把广义圆周映为广义圆周：代入 $z=1/w$ 并乘以 $w\bar w$，得 $Cw\bar w+Bw+\bar B\bar w+A=0$，形式相同，只是 $A$ 与 $C$ 互换了位置。这是分式线性变换理论（[2.3.8](/2.3.8)）中的关键一步。

## 1.2. 扩充复平面与 Riemann 球面

添加一个无穷远点之后，复分析的许多命题会更加简洁：$1/z$ 在 $z=0$ 处有了定义，直线成为经过 $\infty$ 的圆周，函数在 $|z|$ 很大时的性态成为它在单独一点附近的性态。实直线自然地用 $\pm\infty$ 两个点来补全；平面则只用一个点补全，因为沿任何方向 $|z|\to\infty$ 都应当到达同一处。

**定义 1.2.1（扩充复平面）** 在 $\mathbb{C}$ 中添加一个新元素 $\infty$，称为**无穷远点**。集合 $\hat{\mathbb{C}}=\mathbb{C}\cup\{\infty\}$ 称为**扩充复平面**。对 $a\in\mathbb{C}$ 规定

$$
a\pm\infty=\infty,\qquad a\cdot\infty=\infty\ (a\ne0),\qquad \frac a\infty=0,\qquad \frac a0=\infty\ (a\ne0),
$$

而 $\infty\pm\infty$、$0\cdot\infty$、$\frac00$、$\frac\infty\infty$ 不定义。$\infty$ 的实部、虚部与辐角都没有定义，$|\infty|=+\infty$。对 $R>0$，集合 $\{z\mid |z|>R\}\cup\{\infty\}$ 称为 $\infty$ 的一个邻域。

扩充复平面可以用一个球面来表示。设 $S=\{(x_1,x_2,x_3)\in\mathbb{R}^3\mid x_1^2+x_2^2+x_3^2=1\}$ 为单位球面，把复平面放在平面 $x_3=0$ 上（$z=x+\mathrm{i}y$ 对应点 $(x,y,0)$），$N=(0,0,1)$ 为北极。

**定义 1.2.2（Riemann 球面）** 对 $z\in\mathbb{C}$，过 $N$ 与 $z$ 的直线与 $S$ 恰交于一点 $P\ne N$；令 $z$ 对应 $P$，令 $\infty$ 对应 $N$。这个双射 $\hat{\mathbb{C}}\to S$（及其逆）称为**球极投影**，作为 $\hat{\mathbb{C}}$ 的模型的 $S$ 称为 **Riemann 球面**。

求直线 $N+t\big((x,y,0)-N\big)$ 与 $S$ 的交点，得到显式公式：设 $z=x+\mathrm{i}y$，则

$$
P=\Big(\frac{2x}{|z|^2+1},\ \frac{2y}{|z|^2+1},\ \frac{|z|^2-1}{|z|^2+1}\Big),\qquad z=\frac{x_1+\mathrm{i}x_2}{1-x_3}. \tag{1.1}
$$

单位圆周对应赤道，圆盘 $|z|<1$ 对应南半球（$0$ 对应南极），外部 $|z|>1$ 对应北半球；$|z|\to\infty$ 当且仅当 $P\to N$，所以定义 1.2.1 中 $\infty$ 的邻域正是 $N$ 附近小球冠的像。

![球极投影。左：从北极 N 出发经过平面上一点 z 的直线与球面再交于一点；单位圆外的点落在北半球，单位圆内的点落在南半球。右：平面上的圆周和直线（直线经过无穷远点）在球面上都成为圆周。](./plots/riemann-sphere.py)

**定理 1.2.1** 在球极投影下，$\mathbb{C}$ 中的圆周与直线恰好对应 $S$ 上的圆周；其中直线对应经过 $N$ 的圆周。

**证明** $S$ 上的圆周是 $S$ 与某个平面 $a_1x_1+a_2x_2+a_3x_3=a_0$（$a_1^2+a_2^2+a_3^2=1$，$|a_0|<1$）的交线。代入式 (1.1) 并乘以 $|z|^2+1$，得

$$
(a_3-a_0)(x^2+y^2)+2a_1x+2a_2y-(a_3+a_0)=0.
$$

若 $a_3\ne a_0$，这是一个圆周（半径的平方为 $\frac{a_1^2+a_2^2+a_3^2-a_0^2}{(a_3-a_0)^2}>0$）；若 $a_3=a_0$，即平面经过 $N$，这是一条直线。把计算倒过来，可知每个圆周和每条直线都可以这样得到。$\square$

由于在球面上直线经过 $\infty$，自然可以把直线看作经过 $\infty$ 的圆周；广义圆周（例 1.1.4）一词就同时指两者。球面还给出 $\hat{\mathbb{C}}$ 上的一个有界度量：$z_1$ 与 $z_2$ 的像之间的弦距离 $\frac{2|z_1-z_2|}{\sqrt{(1+|z_1|^2)(1+|z_2|^2)}}$，$z$ 到 $\infty$ 的距离为 $\frac{2}{\sqrt{1+|z|^2}}$。本课程主要把球面当作直观图像：关于 $f$ "在 $\infty$ 处"的命题，就是关于 $g(\zeta)=f(1/\zeta)$ 在 $\zeta=0$ 处的命题，球面说明了为什么这是恰当的代换。

## 1.3. 平面点集与曲线

### 1.3.1. 开集与区域

带距离 $|z_1-z_2|$ 的平面 $\mathbb{C}$ 就是 Euclid 平面 $\mathbb{R}^2$，所以 [2.2.10](/2.2.10) 的拓扑概念原样适用，这里只确定复分析中的记号。以 $z_0$ 为圆心、$r$ 为半径的开圆盘记作 $D(z_0,r)=\{z\mid |z-z_0|<r\}$，$\mathbb{D}=D(0,1)$ 为单位圆盘。$D(z_0,\delta)$ 是 $z_0$ 的 $\delta$ **邻域**，$0<|z-z_0|<\delta$ 是它的**去心邻域**。对集合 $E\subset\mathbb{C}$：

- 若 $z_0$ 有某个邻域含于 $E$，则 $z_0$ 是 $E$ 的内点；若 $E$ 的点都是内点，则 $E$ 是**开集**；
- 若 $z_0$ 的每个邻域中既有 $E$ 的点又有不属于 $E$ 的点，则 $z_0$ 是 $E$ 的**边界点**；边界点的全体是边界 $\partial E$，包含自身边界的 $E$ 是**闭集**；
- 若存在 $M$ 使 $E\subset D(0,M)$，则 $E$ 是**有界集**；有界闭集也称为紧集；
- 连通的开集称为**区域**，区域连同它的边界称为**闭区域**。

在复分析中，函数几乎总是在区域上研究。开集保证差商 $\frac{f(z_0+h)-f(z_0)}{h}$ 对一切方向上充分小的 $h$ 都有定义；连通性保证局部信息能传遍整个集合。例如，在区域上导数恒为零的函数是常数（[2.3.2](/2.3.2)），而在不连通的开集 $D(0,1)\cup D(3,1)$ 上这一结论不成立。

### 1.3.2. 曲线

**定义 1.3.1（曲线）** 连续映射 $\gamma\colon[a,b]\to\mathbb{C}$，$\gamma(t)=x(t)+\mathrm{i}y(t)$ 称为一条曲线，$\gamma(a)$ 与 $\gamma(b)$ 分别称为它的起点与终点。若

- $\gamma(a)=\gamma(b)$，则称曲线是闭的；
- 当 $a\le t_1<t_2\le b$ 时 $\gamma(t_1)\ne\gamma(t_2)$（$\gamma(a)=\gamma(b)$ 可以例外），则称曲线是简单的；简单闭曲线称为 **Jordan 曲线**；
- $\gamma'(t)=x'(t)+\mathrm{i}y'(t)$ 在 $[a,b]$ 上存在、连续且不为零，则称它是**光滑曲线**；
- $[a,b]$ 可以分成有限个子区间，$\gamma$ 在每个子区间上光滑，则称它是**分段光滑曲线**。

分段光滑曲线也称为围道，[2.3.4](/2.3.4) 正是沿这类曲线积分。非零向量 $\gamma'(t)$ 是曲线在 $\gamma(t)$ 处的切向量，$\operatorname{Arg}\gamma'(t)$ 是切线的方向；[2.3.2](/2.3.2) 就用它来度量两条曲线的夹角。例如，$\gamma(t)=z_0+r\mathrm{e}^{\mathrm{i}t}$（$0\le t\le2\pi$）是沿逆时针方向绕一周的圆周 $|z-z_0|=r$，是光滑的 Jordan 曲线；同一区间上的 $\gamma(t)=\mathrm{e}^{2\mathrm{i}t}$ 把单位圆周绕两周，不是简单曲线；正方形的边界是分段光滑但不光滑的 Jordan 曲线。

**定理 1.3.1（Jordan 曲线定理）** Jordan 曲线 $C$ 在 $\mathbb{C}$ 中的余集恰由两个区域组成：一个有界（$C$ 的内部），一个无界（$C$ 的外部），且 $C$ 是两者共同的边界。

这个命题看似显然，但对一般连续曲线的证明很难，属于拓扑学；对我们所积分的分段光滑曲线，可以用初等方法证明。这里不加证明地使用它。若沿 Jordan 曲线前进时其内部总在左侧，即曲线沿逆时针方向，则称它是正向的。

### 1.3.3. 单连通区域

若区域 $D$ 内任一 Jordan 曲线的内部都含于 $D$，则称 $D$ 为**单连通区域**（[2.2.13](/2.2.13)）；直观地说，$D$ 没有"洞"，$D$ 内的每条闭曲线都能在 $D$ 内收缩成一点。否则称 $D$ 为**复连通区域**。在 Riemann 球面上看，区域 $D\subset\mathbb{C}$ 单连通当且仅当 $\hat{\mathbb{C}}\setminus D$ 连通。

![典型的点集。-16 的四个四次方根构成一个正方形（例 1.1.3）。圆盘是单连通的；圆环 1 < |z| < 2 不是，因为圆周 |z| = 1.5 不能在其中收缩成一点；去掉负实轴和 0 的平面虽然无界，却是单连通的。](./plots/roots-and-regions.py)

图中的三种情形在本课程中反复出现：

- 圆盘、半平面、角形区域和整个平面都是单连通的；
- 圆环 $r<|z-z_0|<R$ 与去心圆盘 $0<|z-z_0|<R$ 不是单连通的：绕 $z_0$ 的圆周包围了被挖去的中心。它们是 Laurent 级数（[2.3.5](/2.3.5)）所在的区域；
- 割去负实轴的平面 $\mathbb{C}\setminus(-\infty,0]$ 是单连通的：从 $0$ 到 $\infty$ 割去一条射线，就破坏了所有绕 $0$ 的闭路。对数主值（[2.3.3](/2.3.3)）就定义在这个区域上。

[2.3.4](/2.3.4) 中的 Cauchy 定理在单连通区域上成立，在复连通区域上则需要加上修正项，这与 Green 公式完全一样。

## 1.4. 复变函数、极限与连续性

### 1.4.1. 复变函数

**定义 1.4.1（复变函数）** 设 $E\subset\mathbb{C}$。若按某一法则，对每个 $z\in E$ 都有复数 $w=f(z)$ 与之对应，则称 $f$ 为 $E$ 上的**复变函数**。若某些 $z$ 对应多个值，则称 $f$ 是多值的；除非特别说明，函数都是单值的。

记 $z=x+\mathrm{i}y$，$w=u+\mathrm{i}v$，一个复变函数就相当于一对二元实函数

$$
f(z)=u(x,y)+\mathrm{i}v(x,y),
$$

例如 $z^2=(x^2-y^2)+\mathrm{i}\,2xy$，$\frac1z=\frac{x}{x^2+y^2}-\mathrm{i}\frac{y}{x^2+y^2}$。$f$ 的图像在 $\mathbb{R}^4$ 中，无法直接画出，所以我们把 $f$ 看作从 $z$ 平面上的集合到 $w$ 平面上的集合的映射，研究它怎样变换曲线和区域：

- $w=z+b$ 是平移，$w=az$（$a=|a|\mathrm{e}^{\mathrm{i}\alpha}\ne0$）是旋转 $\alpha$ 再伸缩 $|a|$ 倍，$w=\bar z$ 是关于实轴的反射；
- $w=z^2$ 使辐角加倍、模平方：角形区域 $0<\operatorname{Arg}z<\frac\pi2$ 映为上半平面，双曲线 $x^2-y^2=1$ 映为直线 $\operatorname{Re}w=1$；
- $w=\frac1z$ 把 $r\mathrm{e}^{\mathrm{i}\theta}$ 映为 $\frac1r\mathrm{e}^{-\mathrm{i}\theta}$：先关于单位圆周作反演，再关于实轴作反射；圆周 $|z|=2$ 映为 $|w|=\frac12$，由例 1.1.4，广义圆周映为广义圆周。

### 1.4.2. 极限

**定义 1.4.2（极限）** 设 $f$ 在 $z_0\in\mathbb{C}$ 的某个去心邻域内有定义（或定义在以 $z_0$ 为**极限点**的集合上）。若对任意 $\varepsilon>0$，存在 $\delta>0$，使得当 $0<|z-z_0|<\delta$ 且 $z$ 属于 $f$ 的定义域时 $|f(z)-A|<\varepsilon$，则记 $\lim_{z\to z_0}f(z)=A$。$z_0=\infty$ 或 $A=\infty$ 的情形，把相应的圆盘换成 $\infty$ 的邻域即可：例如 $\lim_{z\to z_0}f(z)=\infty$ 指对任意 $M>0$，存在 $\delta>0$，使得当 $0<|z-z_0|<\delta$ 时 $|f(z)|>M$；$\lim_{z\to\infty}f(z)=A$ 指对任意 $\varepsilon>0$，存在 $R>0$，使得当 $|z|>R$ 时 $|f(z)-A|<\varepsilon$。

这就是用复数记号写出的二元实函数的**函数极限**，所以 $z$ 可以沿任何路径趋于 $z_0$，只有沿所有路径得到的值都相同时极限才存在。下面的定理把复极限化为实极限。

**定理 1.4.1** 设 $f=u+\mathrm{i}v$，$z_0=x_0+\mathrm{i}y_0$，$A=a+\mathrm{i}b$。则 $\lim_{z\to z_0}f(z)=A$ 当且仅当

$$
\lim_{(x,y)\to(x_0,y_0)}u(x,y)=a\quad\text{且}\quad\lim_{(x,y)\to(x_0,y_0)}v(x,y)=b.
$$

**证明** 由命题 1.1.1(3)，$|u-a|,|v-b|\le|f-A|\le|u-a|+|v-b|$，所以 $|f-A|$ 很小当且仅当 $|u-a|$ 与 $|v-b|$ 都很小。$\square$

因此，和、积、商的极限运算法则以及 Cauchy 收敛准则对复变函数都与实函数一样成立。

**例 1.4.1** 函数 $f(z)=\dfrac{\operatorname{Re}z}{|z|}$ 在 $0$ 处没有极限：沿射线 $z=t\mathrm{e}^{\mathrm{i}\theta}$（$t\to0^+$），它恒等于 $\cos\theta$，与方向有关。同样，$\dfrac{z}{\bar z}=\mathrm{e}^{2\mathrm{i}\theta}$ 在 $0$ 处没有极限。另一方面，$\dfrac{(\operatorname{Re}z)^2}{|z|}$ 不超过 $|z|$，所以趋于 $0$。

**例 1.4.2** 分子分母同除以 $z^2$，得 $\displaystyle\lim_{z\to\infty}\frac{3z^2+\mathrm{i}z}{z^2-2}=3$；又 $\displaystyle\lim_{z\to\mathrm{i}}\frac{z^2+1}{z-\mathrm{i}}=\lim_{z\to\mathrm{i}}(z+\mathrm{i})=2\mathrm{i}$。对 $n\ge1$ 次多项式 $p$，$\lim_{z\to\infty}p(z)=\infty$，因为 $|p(z)|\ge|a_n||z|^n\big(1-\sum_{k<n}\frac{|a_k|}{|a_n||z|^{n-k}}\big)$，而括号中的量趋于 $1$。

### 1.4.3. 连续性

**定义 1.4.3（连续性）** 设 $f$ 在 $z_0$ 附近有定义。若 $\lim_{z\to z_0}f(z)=f(z_0)$，则称 $f$ 在 $z_0$ 处连续；若 $f$ 在集合 $E$ 的每一点处连续（极限在 $E$ 内取），则称 $f$ 在 $E$ 上连续。

由定理 1.4.1，$f=u+\mathrm{i}v$ 是**连续函数**当且仅当 $u$ 与 $v$ 都连续。连续函数的和、积、商（分母不为零处）与复合仍连续；多项式和有理函数在有定义处连续，$\bar z$、$\operatorname{Re}z$、$|z|$ 也连续。对 $|f|$、$u$、$v$ 应用二元实函数的相应定理（[2.2.10](/2.2.10)），有界闭集 $E$ 上的连续函数有界，$|f|$ 在 $E$ 上取得最大值和最小值，且 $f$ 在 $E$ 上**一致连续**。

**例 1.4.3** 辐角主值 $\operatorname{Arg}z$ 在 $\mathbb{C}\setminus(-\infty,0]$ 上连续，在负实轴的每一点处间断。事实上，在点 $x_0<0$ 附近，实轴上方紧邻的点的 $\operatorname{Arg}z$ 接近 $\pi$，下方紧邻的点接近 $-\pi$。离开负实轴时，§1.1.2 的公式把 $\operatorname{Arg}$ 表示为连续函数（在正实轴附近只用到 $\arctan\frac yx$）。这个跳跃并不是公式的缺陷：在任何一个绕 $0$ 的圆周上都不存在连续的辐角选取，因为沿圆周连续地追踪辐角绕行一周，它会增加 $2\pi$。这就是 [2.3.3](/2.3.3) 中支点的现象。

## 小结

| 主题 | 要点 |
|---|---|
| 运算 | $\lvert z_1z_2\rvert=\lvert z_1\rvert\lvert z_2\rvert$，三角不等式，$z\bar z=\lvert z\rvert^2$，$x=\frac{z+\bar z}2$，$y=\frac{z-\bar z}{2\mathrm{i}}$ |
| 辐角 | $\arg z$ 是集合，$\operatorname{Arg}z\in(-\pi,\pi]$；$\arg(z_1z_2)=\arg z_1+\arg z_2$ 只作为集合等式成立 |
| 方根 | $z^n=w\ne0$ 有 $n$ 个根，位于 $\lvert z\rvert=\sqrt[n]{\lvert w\rvert}$ 上，相邻两根辐角相差 $2\pi/n$ |
| 无穷远点 | $\hat{\mathbb{C}}=\mathbb{C}\cup\{\infty\}$ 即 Riemann 球面；直线是经过 $\infty$ 的圆周 |
| 点集 | 区域（连通开集）；Jordan 曲线有内部与外部；单连通即没有洞 |
| 极限 | $f\to A$ 当且仅当 $u\to\operatorname{Re}A$ 且 $v\to\operatorname{Im}A$；$\operatorname{Arg}$ 在 $(-\infty,0)$ 两侧跳跃 |
