---
title: 共形映射
source_hash: 36040de11e63
---

到目前为止，解析函数是通过级数与积分来研究的。本章换成几何的观点：解析函数 $w = f(z)$ 是从 $z$ 平面的区域到 $w$ 平面的区域的映射，在 $f' \ne 0$ 处它保持角度。这样的共形映射把一个区域变成另一个区域，同时把解析函数变为解析函数、调和函数变为调和函数。因此，复杂平面区域上 Laplace 方程的边值问题可以移植到圆盘或半平面上，在那里用显式公式求解。这是处理二维稳态热传导、静电场与理想流体流动的经典方法，与 [2.5.8](/2.5.8) 中求解 Laplace 方程的方法相互补充。

核心的理论结果是 Riemann 映射定理：$\mathbb{C}$ 的每个单连通真子区域都可以共形映射到单位圆盘上。它的证明不是构造性的，所以实践中用一小套工具拼装映射：分式线性变换（把圆周映为圆周，由三个点决定），以及幂函数、指数函数与 Joukowski 映射。本章要用到 [2.3.2](/2.3.2) 中导数的几何意义、[2.3.3](/2.3.3) 的初等函数，以及 [2.3.7](/2.3.7) 的局部映射定理（定理 7.7.3）。

## 8.1. 共形性

### 8.1.1. 解析函数保持角度

设 $\gamma(t)$ 是光滑曲线，$\gamma(t_0) = z_0$，$\gamma'(t_0) \ne 0$，$f$ 在 $z_0$ 处解析。像曲线 $\Gamma = f\circ\gamma$ 的切向量为

$$
\Gamma'(t_0) = f'(z_0)\,\gamma'(t_0).
$$

若 $f'(z_0) = \rho\,\mathrm{e}^{\mathrm{i}\varphi} \ne 0$，则 $\arg\Gamma'(t_0) = \arg\gamma'(t_0) + \varphi$：过 $z_0$ 的每条曲线都转过同一个角 $\varphi = \arg f'(z_0)$。此外 $\lvert f(z) - f(z_0)\rvert = \rho\lvert z - z_0\rvert + o(\lvert z - z_0\rvert)$：$z_0$ 处的无穷小长度在各个方向上都伸缩同一倍数 $\rho = \lvert f'(z_0)\rvert$。

**定义 8.1.1** 设连续映射 $f$ 在 $z_0$ 附近有定义。若过 $z_0$ 的任意两条切向量非零的光滑曲线，它们的像在 $f(z_0)$ 处的夹角与原曲线的夹角大小相同、方向相同，则称 $f$ 在 $z_0$ 处是共形的。

**定理 8.1.1** 若 $f$ 在 $z_0$ 处解析且 $f'(z_0) \ne 0$，则 $f$ 在 $z_0$ 处是共形的，旋转角为 $\arg f'(z_0)$，伸缩率为 $\lvert f'(z_0)\rvert$。

两个条件都不可少。在临界点处角度被放大：若 $f - f(z_0)$ 有 $m \ge 2$ 阶零点，则 $f(z) - f(z_0) \approx c(z - z_0)^m$，$z_0$ 处的角度扩大为 $m$ 倍（$w = z^2$ 在 $0$ 处把正实轴与正虚轴之间的直角张成平角）。反射 $z \mapsto \bar z$ 保持角度的大小，但改变其方向。反之，平面区域上保持角度大小与方向、Jacobi 行列式不为零的实 $C^1$ 映射满足 Cauchy–Riemann 方程（定理 2.2.1），所以共形映射恰好是 $f' \ne 0$ 的解析函数。

**定义 8.1.2** 设 $D$、$G$ 是 $\mathbb{C}$（或 $\hat{\mathbb{C}}$）中的区域。双射的解析映射 $f\colon D \to G$ 称为 $D$ 到 $G$ 上的**共形映射**；此时称 $D$ 与 $G$ 共形等价。$D$ 到自身的共形映射称为 $D$ 的共形自同构。

**定理 8.1.2** 若 $f$ 在区域 $D$ 上解析且是单射，则对一切 $z \in D$，$f'(z) \ne 0$；像 $G = f(D)$ 是区域；$f^{-1}\colon G \to D$ 解析，且当 $w = f(z)$ 时 $(f^{-1})'(w) = \dfrac{1}{f'(z)}$。

**证明** 若 $f'(z_0) = 0$，则 $z_0$ 是 $f - f(z_0)$ 的 $m \ge 2$ 阶零点（$f$ 是单射，因而不是常数），由定理 7.7.3，$f(z_0)$ 附近的值在 $z_0$ 附近被取到 $m$ 次，与单射矛盾。由开映射定理（定理 7.7.4），$G$ 是开集；作为连通集的连续像，它是连通的。同一定理说明 $f^{-1}$ 连续。最后，若在 $G$ 中 $w_1 \to w$，则 $z_1 = f^{-1}(w_1) \to z$，且 $\frac{f^{-1}(w_1) - f^{-1}(w)}{w_1 - w} = \left(\frac{f(z_1) - f(z)}{z_1 - z}\right)^{-1} \to \frac{1}{f'(z)}$。$\square$

因此每个共形映射在每一点都是定义 8.1.1 意义下共形的，它的逆映射也是共形映射。

### 8.1.2. Riemann 映射定理

这一理论的基本问题是：给定两个区域，求一个把其中一个映到另一个上的共形映射。共形映射保持拓扑性质，所以单连通区域不能映到圆环上。整个平面也不能映到圆盘上，因为这样的映射是有界整函数，由 **Liouville 定理**它是常数。障碍只有这些：

**定理 8.1.3（Riemann 映射定理）** 设 $D \subsetneq \mathbb{C}$ 是单连通区域，$z_0 \in D$。则存在唯一的把 $D$ 映到单位圆盘 $\mathbb{D}$ 上的共形映射 $f$，满足 $f(z_0) = 0$、$f'(z_0) > 0$。

存在性不作证明；唯一性由 Schwarz 引理得到（§8.4）。另外两个事实同样不加证明，应用中经常用到。

- 若 $D$ 的边界是 Jordan 曲线，则 $f$ 可以延拓为闭包之间的同胚 $\overline{D} \to \overline{\mathbb{D}}$（Carathéodory 定理），因此边界点对应边界点。
- 边界对应原理：若 $f$ 在以 Jordan 曲线 $C$ 为边界的区域上解析，连续到 $C$，且把 $C$ 一一地映到 Jordan 曲线 $\Gamma$ 上，则 $f$ 把 $C$ 的内部共形映射到 $\Gamma$ 的内部上。实践中：沿边界行进，使区域位于左侧；像区域就位于像边界的左侧。

Riemann 映射定理保证了存在性，却不给出公式。显式的映射由下面两节的初等映射构造。

## 8.2. 分式线性变换

### 8.2.1. 定义与基本性质

**定义 8.2.1** 形如

$$
w = T(z) = \frac{az + b}{cz + d}, \qquad a, b, c, d \in \mathbb{C}, \quad ad - bc \ne 0, \tag{8.1}
$$
的映射称为**分式线性变换**（或 Möbius 变换）。$c \ne 0$ 时令 $T(-d/c) = \infty$、$T(\infty) = a/c$，$c = 0$ 时令 $T(\infty) = \infty$，把它延拓到 $\hat{\mathbb{C}}$ 上。

条件 $ad - bc \ne 0$ 排除了常数：$T'(z) = \frac{ad - bc}{(cz + d)^2}$。解出 $z$ 得逆映射 $z = \frac{dw - b}{-cw + a}$，它仍是分式线性变换，所以 $T$ 是 $\hat{\mathbb{C}}$ 的双射。系数只确定到一个公共因子，复合对应于系数矩阵 $\begin{bmatrix}a & b\\ c & d\end{bmatrix}$ 的乘法；分式线性变换在复合下构成群。

$c \ne 0$ 时，

$$
T(z) = \frac{a}{c} + \frac{bc - ad}{c}\cdot\frac{1}{cz + d},
$$

所以 $T$ 是三类初等映射的复合：平移 $z \mapsto z + h$，旋转伸缩 $z \mapsto kz$（$k \ne 0$），以及反演 $z \mapsto \frac1z$。（$c = 0$ 时 $T$ 是线性映射 $z \mapsto \frac adz + \frac bd$。）平移与旋转伸缩都是相似变换；反演 $\frac1z = \frac{1}{\lvert z\rvert}\mathrm{e}^{-\mathrm{i}\arg z}$ 是关于单位圆周的反射（$z \mapsto z/\lvert z\rvert^2$）再接关于实轴的反射。

**定理 8.2.1** 每个分式线性变换都是 $\hat{\mathbb{C}}$ 到自身上的共形映射。这里 $\infty$ 处与 $-d/c$ 处的共形性，是在 $\infty$ 附近的坐标 $\zeta = 1/z$（相应地，$w = \infty$ 附近的 $1/w$）下理解的。

**证明** 在 $\mathbb{C}\setminus\{-d/c\}$ 上 $T' \ne 0$。在 $z = -d/c$ 附近，函数 $1/T(z) = \frac{cz + d}{az + b}$ 解析且导数不为零；在 $\infty$ 附近，函数 $T(1/\zeta) = \frac{a + b\zeta}{c + d\zeta}$ 关于 $\zeta$ 解析，且在 $\zeta = 0$ 处导数不为零。$\square$

### 8.2.2. 圆周与对称点

在 Riemann 球面上，直线是过 $\infty$ 的圆周。圆周与直线统称为广义圆周（generalized circle）。广义圆周可以写成

$$
A z\bar z + \bar\beta z + \beta\bar z + D = 0, \qquad A, D \in \mathbb{R}, \quad \beta \in \mathbb{C}, \quad \lvert\beta\rvert^2 > AD, \tag{8.2}
$$

$A = 0$ 时是直线，$A \ne 0$ 时是圆周（由 $x^2 + y^2 = z\bar z$ 与 $x = \frac{z + \bar z}{2}$、$y = \frac{z - \bar z}{2\mathrm{i}}$，式 (8.2) 就是一般方程 $A(x^2 + y^2) + Bx + Cy + D = 0$）。

**定理 8.2.2（保圆性）** 分式线性变换把广义圆周映为广义圆周。

**证明** 平移与旋转伸缩显然保持圆周与直线，所以由上面的分解，只需考虑 $w = \frac1z$。把 $z = \frac1w$ 代入式 (8.2) 并乘以 $w\bar w$，得 $A + \bar\beta\bar w + \beta w + Dw\bar w = 0$，这是同一形式的方程，只是 $A$ 与 $D$ 互换、$\beta$ 换成 $\bar\beta$。$\square$

过 $T$ 的极点 $-d/c$ 的广义圆周被映为直线，其余的被映为圆周。这是化简由圆弧围成的区域的主要手段：把圆弧的一个交点送到 $\infty$，圆弧就变成射线或直线。

**定义 8.2.2** 若两点 $z$ 与 $z^*$ 位于从 $a$ 出发的同一条射线上，且 $\lvert z - a\rvert\,\lvert z^* - a\rvert = r^2$，即

$$
z^* = a + \frac{r^2}{\bar z - \bar a},
$$

则称 $z$ 与 $z^*$ 是关于圆周 $\lvert z - a\rvert = r$ 的**对称点**；圆心 $a$ 与 $\infty$ 也看作对称的。关于直线的对称点就是镜像点。

例如，$z$ 与 $\frac{1}{\bar z}$ 关于单位圆周对称，$z$ 与 $\bar z$ 关于实轴对称。由初等几何（圆幂定理）可以得到一个几何刻画：$z$ 与 $z^*$ 关于广义圆周 $\Gamma$ 对称，当且仅当过 $z$ 与 $z^*$ 的每个广义圆周都与 $\Gamma$ 正交。分式线性变换保持广义圆周（定理 8.2.2）与角度（定理 8.2.1），所以保持这一刻画：

**定理 8.2.3（保对称性）** 若分式线性变换 $T$ 把广义圆周 $\Gamma$ 映到 $\Gamma'$ 上，则它把每一对关于 $\Gamma$ 的对称点映为一对关于 $\Gamma'$ 的对称点。

### 8.2.3. 交比

分式线性变换有三个复的自由参数（四个系数，相差一个公共因子），三个点决定它。

**定义 8.2.3** 对互异的点 $z_1, z_2, z_3 \in \hat{\mathbb{C}}$ 与 $z \in \hat{\mathbb{C}}$，**交比**定义为

$$
(z, z_1, z_2, z_3) = \frac{z - z_1}{z - z_3}\cdot\frac{z_2 - z_3}{z_2 - z_1},
$$

其中某个点为 $\infty$ 时略去含 $\infty$ 的因子（例如 $(z, z_1, z_2, \infty) = \frac{z - z_1}{z_2 - z_1}$）。

作为 $z$ 的函数，交比是把 $z_1, z_2, z_3$ 分别送到 $0, 1, \infty$ 的唯一的分式线性变换。

**定理 8.2.4** 1. 分式线性变换保持交比：$(Tz, Tz_1, Tz_2, Tz_3) = (z, z_1, z_2, z_3)$。
2. 对互异的 $z_1, z_2, z_3$ 与互异的 $w_1, w_2, w_3$，存在唯一的分式线性变换使 $T(z_k) = w_k$（$k = 1, 2, 3$）。从下面的方程中解出 $w$ 即得：

$$
(w, w_1, w_2, w_3) = (z, z_1, z_2, z_3). \tag{8.3}
$$

**证明** 分式线性变换 $S \ne \mathrm{id}$ 在 $\hat{\mathbb{C}}$ 中至多有两个不动点：$\mathbb{C}$ 中的不动点满足 $cz^2 + (d - a)z - b = 0$，除非它是零多项式（$S = \mathrm{id}$），至多有两个根；$c = 0$ 时 $\infty$ 是不动点，而方程的次数至多为 $1$。因此在三个点处取值相同的两个分式线性变换相等。这证明了第 2 条中的唯一性。令 $S(z) = (z, z_1, z_2, z_3)$，$S'(w) = (w, w_1, w_2, w_3)$。则 $S'^{-1}\circ S$ 把 $z_k$ 送到 $w_k$，这证明了存在性。对第 1 条，对 $S\circ T^{-1}$ 与 $z \mapsto (z, Tz_1, Tz_2, Tz_3)$ 用同样的唯一性论证，二者都把 $Tz_1, Tz_2, Tz_3$ 送到 $0, 1, \infty$。$\square$

**例 8.2.1** 求把 $1, \mathrm{i}, -1$ 送到 $0, 1, \infty$ 的分式线性变换，以及单位圆盘的像。

由式 (8.3)，$w = (z, 1, \mathrm{i}, -1) = \frac{z - 1}{z + 1}\cdot\frac{\mathrm{i} + 1}{\mathrm{i} - 1} = \mathrm{i}\,\frac{1 - z}{1 + z}$。单位圆周过 $1, \mathrm{i}, -1$，所以它的像是过 $0, 1, \infty$ 的广义圆周，即实轴。由于 $w(0) = \mathrm{i}$，单位圆盘被映到上半平面上。（另一种看法：沿圆周逆时针经过 $1, \mathrm{i}, -1$ 时圆盘在左侧，像沿实轴经过 $0, 1, \infty$，上半平面在左侧。）

### 8.2.4. 圆盘与半平面

记 $\mathbb{H} = \{z : \operatorname{Im}z > 0\}$ 为上半平面。下面这些映射是大多数构造的基本部件。

**定理 8.2.5** 把 $\mathbb{H}$ 映到 $\mathbb{D}$ 上的分式线性变换恰好是

$$
w = \mathrm{e}^{\mathrm{i}\theta}\,\frac{z - a}{z - \bar a}, \qquad a \in \mathbb{H}, \quad \theta \in \mathbb{R}, \tag{8.4}
$$

且这样的映射把 $a$ 送到 $0$。

**证明** 设 $T$ 把 $\mathbb{H}$ 映到 $\mathbb{D}$ 上，令 $a = T^{-1}(0) \in \mathbb{H}$。实轴被映为单位圆周。由于 $a$ 与 $\bar a$ 关于实轴对称，$0$ 与 $\infty$ 关于单位圆周对称，由保对称性得 $T(\bar a) = \infty$。所以 $T(z) = k\frac{z - a}{z - \bar a}$；对实数 $x$ 有 $\lvert x - a\rvert = \lvert x - \bar a\rvert$，所以 $\lvert T(x)\rvert = \lvert k\rvert = 1$。反之，式 (8.4) 把实轴映到单位圆周上，把 $a \in \mathbb{H}$ 映为 $0 \in \mathbb{D}$，从而把 $\mathbb{H}$ 映到 $\mathbb{D}$ 上。$\square$

$a = \mathrm{i}$、$\theta = 0$ 的情形是 Cayley 映射 $w = \frac{z - \mathrm{i}}{z + \mathrm{i}}$，见下图。

![Cayley 映射 w = (z - i)/(z + i) 把上半平面（左）映到单位圆盘（右）上。水平直线 Im z = c 变为在 w = 1 处与单位圆周相切的圆周，竖直直线 Re z = c 变为过 w = 1 且与单位圆周正交的圆弧，点 i 变为圆心。两族曲线保持正交，这正是共形性的要求](./plots/cayley-grid.py)

**定理 8.2.6** 把 $\mathbb{D}$ 映到自身上的分式线性变换恰好是

$$
w = \mathrm{e}^{\mathrm{i}\theta}\,\frac{z - a}{1 - \bar az}, \qquad \lvert a\rvert < 1, \quad \theta \in \mathbb{R}. \tag{8.5}
$$

**证明** 与前面一样，若 $T(a) = 0$，则由关于单位圆周的对称性，$T\left(1/\bar a\right) = \infty$（$a = 0$ 时 $T(\infty) = \infty$）。所以 $T(z) = k\frac{z - a}{1 - \bar az}$。当 $\lvert z\rvert = 1$ 时，$\lvert 1 - \bar az\rvert = \lvert z\rvert\,\lvert\bar z - \bar a\rvert = \lvert z - a\rvert$，因此 $\lvert k\rvert = 1$。反之，式 (8.5) 把单位圆周映到自身上，把 $a$ 映为 $0$。$\square$

式 (8.5) 中的映射满足 $w'(a) = \frac{\mathrm{e}^{\mathrm{i}\theta}}{1 - \lvert a\rvert^2}$，所以 $\theta$ 是 $a$ 处的旋转角。由 §8.4，这些就是 $\mathbb{D}$ 的全部共形自同构，而不只是其中的分式线性变换。

**定理 8.2.7** 设 $T(z) = \frac{az + b}{cz + d}$ 的系数都是实数。若 $ad - bc > 0$，则 $T$ 把 $\mathbb{H}$ 映到 $\mathbb{H}$ 上；若 $ad - bc < 0$，则把 $\mathbb{H}$ 映到下半平面上。

**证明** 分子分母同乘 $\overline{cz + d} = c\bar z + d$，

$$
T(z) = \frac{ac\lvert z\rvert^2 + adz + bc\bar z + bd}{\lvert cz + d\rvert^2}, \qquad \operatorname{Im}T(z) = \frac{(ad - bc)\operatorname{Im}z}{\lvert cz + d\rvert^2}.
$$

所以 $\operatorname{Im}T(z)$ 与 $(ad - bc)\operatorname{Im}z$ 同号。由于 $T$ 把 $\hat{\mathbb{R}} = \mathbb{R}\cup\{\infty\}$ 映到自身上，且是 $\hat{\mathbb{C}}$ 的双射，第一种情形下它把 $\mathbb{H}$ 映到 $\mathbb{H}$ 上，第二种情形下映到下半平面上。$\square$

$\mathbb{H}$ 的每个共形自同构都具有这种形式，且 $ad - bc > 0$（用 Cayley 映射共轭定理 8.2.6 即得）。

**例 8.2.2** 1. 把 $\mathbb{D}$ 映到自身上、$\frac12 \mapsto 0$ 且 $f'\left(\frac12\right) > 0$ 的映射是 $w = \frac{z - 1/2}{1 - z/2} = \frac{2z - 1}{2 - z}$，$w'\left(\frac12\right) = \frac43$。
2. $w = \frac{z - 1}{z + 1}$ 把右半平面 $\operatorname{Re}z > 0$ 映到 $\mathbb{D}$ 上，且 $1 \mapsto 0$：$1$ 关于虚轴的对称点是 $-1$，它必须被送到 $\infty$。
3. 把圆盘 $\lvert z - z_0\rvert < r$ 映到 $\lvert w - w_0\rvert < R$ 上、$z_1 \mapsto w_0$ 的映射，可以把两个圆盘都标准化为 $\mathbb{D}$ 得到：令 $\zeta = \frac{z - z_0}{r}$、$\zeta_1 = \frac{z_1 - z_0}{r}$，

$$
\frac{w - w_0}{R} = \mathrm{e}^{\mathrm{i}\theta}\,\frac{\zeta - \zeta_1}{1 - \bar\zeta_1\zeta}.
$$

## 8.3. 初等函数构成的映射

### 8.3.1. 幂函数与指数函数

对幂函数，用极坐标表示，$w = z^\alpha$（主值支，$\alpha > 0$）把 $z = r\mathrm{e}^{\mathrm{i}\theta}$ 送到 $r^\alpha\mathrm{e}^{\mathrm{i}\alpha\theta}$，所以它把原点处的角度扩大为 $\alpha$ 倍。角形域 $0 < \arg z < \beta$（$0 < \beta \le 2\pi$）由

$$
w = z^{\pi/\beta}
$$

共形映射到上半平面上。例如 $z^2$ 把第一象限映到 $\mathbb{H}$ 上，$\sqrt z$（取 $0 < \arg z < 2\pi$）把沿 $[0, \infty)$ 割开的平面映到 $\mathbb{H}$ 上。映射在顶点 $0$ 处不是共形的，那里的角度扩大为 $\frac\pi\beta$ 倍；正是这一点把角"拉直"。

对指数函数，写 $z = x + \mathrm{i}y$，$w = \mathrm{e}^z = \mathrm{e}^x\mathrm{e}^{\mathrm{i}y}$ 把水平直线 $y = c$ 映为射线 $\arg w = c$，把竖直线段 $x = c$、$0 < y < 2\pi$ 映为去掉一点的圆周 $\lvert w\rvert = \mathrm{e}^c$。因此：

| $z$ 平面中的区域 | 在 $\mathrm{e}^z$ 下的像 |
|---|---|
| 带形域 $0 < \operatorname{Im}z < \pi$ | 上半平面 $\mathbb{H}$ |
| 带形域 $0 < \operatorname{Im}z < 2\pi$ | 沿 $[0, +\infty)$ 割开的平面 |
| 半带形域 $\operatorname{Re}z < 0$，$0 < \operatorname{Im}z < \pi$ | 上半圆盘 $\lvert w\rvert < 1$，$\operatorname{Im}w > 0$ |
| 带形域 $0 < \operatorname{Im}z < \beta$（$\beta \le 2\pi$） | 角形域 $0 < \arg w < \beta$ |

任意方向、宽为 $h$ 的带形域，先用旋转与平移移到 $0 < \operatorname{Im}z < h$，再伸缩 $\frac\pi h$ 倍。逆映射是对数函数的分支：$\operatorname{Log}$ 把 $\mathbb{H}$ 映到带形域 $0 < \operatorname{Im}z < \pi$ 上。

**例 8.3.1** $w = \frac{\mathrm{e}^z - \mathrm{i}}{\mathrm{e}^z + \mathrm{i}}$ 把带形域 $0 < \operatorname{Im}z < \pi$ 映到 $\mathbb{D}$ 上：先用 $\mathrm{e}^z$ 映到 $\mathbb{H}$ 上，再用 Cayley 映射。点 $z = \frac{\mathrm{i}\pi}{2}$ 被送到 $0$。

### 8.3.2. Joukowski 映射

Joukowski 映射（Joukowski map）是

$$
w = J(z) = \frac12\left(z + \frac1z\right). \tag{8.6}
$$

由于 $J(z) = J(1/z)$，且 $J(z_1) - J(z_2) = \frac12(z_1 - z_2)\left(1 - \frac{1}{z_1z_2}\right)$，$J(z_1) = J(z_2)$ 当且仅当 $z_1 = z_2$ 或 $z_1z_2 = 1$。所以 $J$ 在 $\lvert z\rvert > 1$ 上与 $0 < \lvert z\rvert < 1$ 上都是单射，且 $J'(z) = \frac12\left(1 - \frac{1}{z^2}\right)$ 只在 $\pm1$ 处为零。用极坐标 $z = r\mathrm{e}^{\mathrm{i}\theta}$，

$$
u = \frac12\left(r + \frac1r\right)\cos\theta, \qquad v = \frac12\left(r - \frac1r\right)\sin\theta.
$$

- 圆周 $\lvert z\rvert = r > 1$ 被映到椭圆 $\frac{u^2}{a^2} + \frac{v^2}{b^2} = 1$ 上，其中 $a = \frac12\left(r + \frac1r\right)$，$b = \frac12\left(r - \frac1r\right)$。由于 $a^2 - b^2 = 1$，这些椭圆的焦点都是 $\pm1$。
- 单位圆周被映到线段 $[-1, 1]$ 上，经过两次（$J(\mathrm{e}^{\mathrm{i}\theta}) = \cos\theta$）。
- 射线 $\arg z = \theta$、$r > 1$ 被映到双曲线 $\frac{u^2}{\cos^2\theta} - \frac{v^2}{\sin^2\theta} = 1$ 的一支上，焦点相同。

**定理 8.3.1** Joukowski 映射是 $\{\lvert z\rvert > 1\}$ 到 $\mathbb{C}\setminus[-1, 1]$ 上的共形映射；它把 $\{\lvert z\rvert > 1, \operatorname{Im}z > 0\}$ 映到 $\mathbb{H}$ 上，把上半圆盘 $\{\lvert z\rvert < 1, \operatorname{Im}z > 0\}$ 映到下半平面上。

**证明** 上面已证明 $J$ 在 $\lvert z\rvert > 1$ 上是单射。对 $w \notin [-1, 1]$，方程 $J(z) = w$，即 $z^2 - 2wz + 1 = 0$，有两个乘积为 $1$ 的根，它们都不在单位圆周上（因为 $J$ 把圆周映入 $[-1, 1]$）；所以恰有一个根位于 $\lvert z\rvert > 1$ 内，$J$ 是满射。关于半平面的结论由 $v$ 的符号得到：$\sin\theta > 0$ 时，$r > 1$ 则 $v > 0$，$r < 1$ 则 $v < 0$。$\square$

在 $\mathbb{C}\setminus[-1, 1]$ 上的逆映射是 $z = w + \sqrt{w^2 - 1}$，其中平方根取使 $\lvert z\rvert > 1$ 的分支。过 $z = 1$ 且包围 $z = -1$ 的圆周被映为在 $J(1) = 1$ 处有尖点的闭曲线：由于 $J'(1) = 0$，圆周在 $1$ 处的平角被加倍为周角。这样的像就是 Joukowski 翼型，历史上第一批能以闭合形式计算升力的机翼剖面。

![Joukowski 映射 w = (z + 1/z)/2。左：圆周 |z| = r ≥ 1 的像（焦点为 ±1 的椭圆；r = 1 时为线段 [-1, 1]）与从原点出发的射线的像（焦点相同的双曲线）。右：过 z = 1、圆心略偏离原点的圆周（虚线）及其像——在 w = 1 处有尖锐后缘的 Joukowski 翼型](./plots/joukowski.py)

### 8.3.3. 复合映射

大多数映射问题都由几个标准步骤复合解决：

| 步骤 | 映射 | 效果 |
|---|---|---|
| 交于 $p$、$q$ 的圆弧 | $\dfrac{z - p}{z - q}$ | 过 $p, q$ 的圆弧变为从 $0$ 出发的射线 |
| 切于 $p$ 的两个圆周 | $\dfrac{1}{z - p}$ | 圆周变为平行直线 |
| 顶点在 $0$、张角为 $\beta$ 的角形域 | $z^{\pi/\beta}$ | 上半平面 |
| 宽为 $\pi$ 的带形域 | $\mathrm{e}^z$ | 上半平面 |
| 上半平面 | $\dfrac{z - a}{z - \bar a}$ | 单位圆盘，$a \mapsto 0$ |

每一步都检查几个边界点与一个内点的像。

**例 8.3.2** 把上半圆盘 $D_+ = \{\lvert z\rvert < 1, \operatorname{Im}z > 0\}$ 映到 $\mathbb{D}$ 上。

两段边界（线段 $[-1, 1]$ 与上半圆周）在 $\pm1$ 处正交。映射 $\zeta_1 = \frac{1 + z}{1 - z}$ 把 $-1 \mapsto 0$，$1 \mapsto \infty$，$0 \mapsto 1$，$\mathrm{i} \mapsto \mathrm{i}$；它把线段映到正实轴上，把半圆周映到正虚轴上，所以 $D_+$ 被映到第一象限上。再用 $\zeta_2 = \zeta_1^2$ 把第一象限映到 $\mathbb{H}$ 上，最后用 Cayley 映射：

$$
w = \frac{\zeta_2 - \mathrm{i}}{\zeta_2 + \mathrm{i}} = \frac{(1 + z)^2 - \mathrm{i}(1 - z)^2}{(1 + z)^2 + \mathrm{i}(1 - z)^2}.
$$

**例 8.3.3** 把月牙形区域 $D = \{\lvert z - 1\rvert < 1,\ \lvert z - \frac12\rvert > \frac12\}$ 映到 $\mathbb{D}$ 上。

两个边界圆周切于 $0$。反演 $w_1 = \frac1z$ 把圆周 $\lvert z - 1\rvert = 1$（过 $0$ 与 $2$）映为直线 $\operatorname{Re}w_1 = \frac12$，把圆周 $\lvert z - \frac12\rvert = \frac12$（过 $0$ 与 $1$）映为直线 $\operatorname{Re}w_1 = 1$。点 $z = \frac32 \in D$ 被送到 $\frac23$，所以 $D$ 被映到带形域 $\frac12 < \operatorname{Re}w_1 < 1$ 上。接着，$w_2 = 2\pi\mathrm{i}\left(w_1 - \frac12\right)$ 把它旋转伸缩为 $0 < \operatorname{Im}w_2 < \pi$；$w_3 = \mathrm{e}^{w_2}$ 把它映到 $\mathbb{H}$ 上；$w = \frac{w_3 - \mathrm{i}}{w_3 + \mathrm{i}}$ 再映到 $\mathbb{D}$ 上。由于 $\mathrm{e}^{w_2} = \mathrm{e}^{2\pi\mathrm{i}/z}\mathrm{e}^{-\mathrm{i}\pi} = -\mathrm{e}^{2\pi\mathrm{i}/z}$，

$$
w = \frac{\mathrm{e}^{2\pi\mathrm{i}/z} + \mathrm{i}}{\mathrm{e}^{2\pi\mathrm{i}/z} - \mathrm{i}}.
$$

**例 8.3.4** 把扇形 $S = \{\lvert z\rvert < 1,\ 0 < \arg z < \frac\pi2\}$（四分之一圆盘）映到 $\mathbb{H}$ 上。映射 $\zeta = z^2$ 把它张开为上半圆盘，例 8.3.2 中的 $\frac{1 + \zeta}{1 - \zeta}$ 把上半圆盘映到第一象限上；再平方一次得

$$
w = \left(\frac{1 + z^2}{1 - z^2}\right)^2.
$$

## 8.4. Schwarz 引理

最大模原理给出圆盘到自身的映射的一个刚性定理，它确定了 $\mathbb{D}$ 的全部共形自同构，并给出 Riemann 映射定理中的唯一性。

**定理 8.4.1（Schwarz 引理）** 设 $f$ 在 $\mathbb{D}$ 上解析，$\lvert f(z)\rvert < 1$，$f(0) = 0$，则

$$
\lvert f(z)\rvert \le \lvert z\rvert \quad (z \in \mathbb{D}), \qquad \lvert f'(0)\rvert \le 1.
$$

若对某个 $z_0 \ne 0$ 有 $\lvert f(z_0)\rvert = \lvert z_0\rvert$，或 $\lvert f'(0)\rvert = 1$，则 $f(z) = \mathrm{e}^{\mathrm{i}\theta}z$，$\theta$ 为某个实数。

**证明** 函数 $g(z) = \frac{f(z)}{z}$（令 $g(0) = f'(0)$）以 $0$ 为可去奇点，在 $\mathbb{D}$ 上解析。对 $0 < r < 1$，在 $\lvert z\rvert = r$ 上 $\lvert g\rvert \le \frac1r$，由**最大模原理**，在 $\lvert z\rvert \le r$ 上也是如此。令 $r \to 1$ 得在 $\mathbb{D}$ 上 $\lvert g\rvert \le 1$，这就是两个不等式。若 $\lvert g\rvert$ 在某个内点处等于 $1$，则 $\lvert g\rvert$ 在那里取到最大值，所以 $g$ 是模为 $1$ 的常数。$\square$

**推论 8.4.1** $\mathbb{D}$ 的每个共形自同构都是式 (8.5) 形式的分式线性变换。

**证明** 设 $f$ 是 $\mathbb{D}$ 的共形自同构，令 $a = f^{-1}(0)$，$\varphi_a(z) = \frac{z - a}{1 - \bar az}$。则 $h = f\circ\varphi_a^{-1}$ 是满足 $h(0) = 0$ 的共形自同构。对 $h$ 与 $h^{-1}$ 用 Schwarz 引理，得 $\lvert h'(0)\rvert \le 1$ 与 $\lvert 1/h'(0)\rvert \le 1$，所以 $\lvert h'(0)\rvert = 1$，$h(z) = \mathrm{e}^{\mathrm{i}\theta}z$。因此 $f = \mathrm{e}^{\mathrm{i}\theta}\varphi_a$。$\square$

同样的论证证明了定理 8.1.3 中的唯一性：若 $f_1, f_2$ 都把 $D$ 映到 $\mathbb{D}$ 上，$z_0 \mapsto 0$，且导数为正，则 $f_2\circ f_1^{-1}$ 是 $\mathbb{D}$ 的保持 $0$ 不动、导数为正的自同构，因而是恒等映射。

**例 8.4.1** 设 $f$ 在 $\mathbb{D}$ 上解析，$\lvert f\rvert < 1$，$f\left(\frac12\right) = 0$。$\lvert f(0)\rvert$ 最大可以是多少？令 $\varphi(z) = \frac{2z - 1}{2 - z}$（例 8.2.2），它把 $\mathbb{D}$ 映到自身上，$\varphi\left(\frac12\right) = 0$，$\varphi(0) = -\frac12$。函数 $g = f\circ\varphi^{-1}$ 满足 Schwarz 引理的条件，所以 $\lvert f(0)\rvert = \lvert g(\varphi(0))\rvert \le \lvert\varphi(0)\rvert = \frac12$，等号恰好在 $f = \mathrm{e}^{\mathrm{i}\theta}\varphi$ 时成立。

## 8.5. 在 Laplace 方程中的应用

### 8.5.1. 共形映射下的调和函数

**定理 8.5.1** 设 $f\colon D \to G$ 解析，$u$ 在 $G$ 上调和，则 $u\circ f$ 在 $D$ 上调和。此外，对 $G$ 上每个 $C^2$ 函数 $u$，

$$
\Delta(u\circ f)(z) = \lvert f'(z)\rvert^2\,(\Delta u)(f(z)).
$$

**证明** 设 $z_0 \in D$，$B$ 是 $G$ 中以 $f(z_0)$ 为中心的圆盘。在单连通区域 $B$ 上，**调和函数** $u$ 有**共轭调和函数** $v$（[2.3.2](/2.3.2)），所以 $u = \operatorname{Re}F$，其中 $F = u + \mathrm{i}v$ 在 $B$ 上解析。在 $z_0$ 附近，$u\circ f = \operatorname{Re}(F\circ f)$ 是解析函数的实部，因而调和。一般 $u$ 的公式由链式法则与 $f$ 的 Cauchy–Riemann 方程得到。$\square$

边界条件的变换也很简单。Dirichlet 边值逐点随之搬运（$\partial G$ 上的 $u = \varphi$ 变为 $\partial D$ 上的 $u\circ f = \varphi\circ f$）。齐次 Neumann 条件 $\frac{\partial u}{\partial\boldsymbol{n}} = 0$（绝热边界或壁面）保持不变，因为共形映射保持等值线与边界的正交性。因此，为了在单连通区域 $D$ 上求解 Dirichlet 问题

$$
\Delta u = 0 \ \text{ 在 } D \text{ 内}, \qquad u = \varphi \ \text{ 在 } \partial D \text{ 上},
$$

先用某个 $f$ 把 $D$ 共形映射到 $\mathbb{H}$ 或 $\mathbb{D}$ 上，在那里用 Poisson 积分公式（[2.5.8](/2.5.8)）或直接观察求解，再与 $f$ 复合。对分段常数的边值，$\mathbb{H}$ 上的解是初等的：$\operatorname{Arg}(z - x_0) = \operatorname{Im}\operatorname{Log}(z - x_0)$ 在 $\mathbb{H}$ 上调和，在实轴上 $x_0$ 左侧等于 $\pi$，右侧等于 $0$。

**例 8.5.1** 在 $\mathbb{H}$ 上，设边值在 $(-\infty, x_1)$ 上为 $T_0$，在 $(x_1, x_2)$ 上为 $T_1$，……，在 $(x_n, +\infty)$ 上为 $T_n$。则

$$
u(z) = T_n + \frac1\pi\sum_{k=1}^n(T_{k-1} - T_k)\operatorname{Arg}(z - x_k)
$$

是具有这些边值的有界调和函数：对实数 $x \in (x_j, x_{j+1})$，$k > j$ 时辐角为 $\pi$，$k \le j$ 时为 $0$，求和逐项相消后得 $T_j$。$n = 1$ 时等温线是从 $x_1$ 出发的射线；$n = 2$ 且 $T_0 = T_2$ 时等温线是过 $x_1$ 与 $x_2$ 的圆弧。

**例 8.5.2** 第一象限中的稳态温度，正实轴上 $u = T_1$，正虚轴上 $u = T_2$。映射 $z^2$ 把第一象限映到 $\mathbb{H}$ 上，把正实轴映为正实轴，把正虚轴映为负实轴。由例 8.5.1（$n = 1$），

$$
u = T_1 + \frac{T_2 - T_1}{\pi}\operatorname{Arg}z^2 = T_1 + \frac{2(T_2 - T_1)}{\pi}\operatorname{Arg}z,
$$

等温线是从角点出发的射线。

**例 8.5.3** 求 $\mathbb{D}$ 内在上半圆周上取值 $1$、在下半圆周上取值 $0$ 的调和函数。

映射 $\zeta = \mathrm{i}\frac{1 + z}{1 - z}$ 是例 8.2.1 中的映射与旋转 $z \mapsto -z$ 的复合，所以它把 $\mathbb{D}$ 映到 $\mathbb{H}$ 上。在边界上，$z = \mathrm{e}^{\mathrm{i}\theta}$ 给出 $\frac{1 + z}{1 - z} = \mathrm{i}\cot\frac\theta2$，所以 $\zeta = -\cot\frac\theta2$：上半圆周（$0 < \theta < \pi$）被映到负实轴上，下半圆周被映到正实轴上。函数 $\frac1\pi\operatorname{Arg}\zeta$ 在 $\mathbb{H}$ 上调和，在负实轴上等于 $1$，在正实轴上等于 $0$。由于 $\frac{1 + z}{1 - z} = \frac{1 - \lvert z\rvert^2 + 2\mathrm{i}y}{\lvert 1 - z\rvert^2}$ 位于右半平面，

$$
u(x, y) = \frac1\pi\operatorname{Arg}\left(\mathrm{i}\,\frac{1 + z}{1 - z}\right) = \frac12 + \frac1\pi\arctan\frac{2y}{1 - x^2 - y^2}.
$$

在圆心处 $u = \frac12$，是边值的平均，这正是**平均值性质**的要求。等温线是过 $\pm1$ 的圆弧。

### 8.5.2. 平面流动的复势

考虑平面区域中理想流体的定常、不可压缩、无旋流动，速度场为 $\boldsymbol{v} = (v_1, v_2)$。不可压缩条件 $\operatorname{div}\boldsymbol{v} = 0$ 与无旋条件 $\partial_xv_2 - \partial_yv_1 = 0$ 说明，局部地存在速度势 $\phi$ 使 $\boldsymbol{v} = \nabla\phi$，存在流函数 $\psi$ 使 $(v_1, v_2) = (\psi_y, -\psi_x)$。于是 $\phi_x = \psi_y$，$\phi_y = -\psi_x$，这正是 Cauchy–Riemann 方程。

**定义 8.5.1** 对这样的流动，解析函数 $F = \phi + \mathrm{i}\psi$ 称为流动的**复势**；$\phi$ 是它的速度势，$\psi$ 是它的**流函数**。

由于 $F' = \phi_x + \mathrm{i}\psi_x = v_1 - \mathrm{i}v_2$，速度对应于 $\boldsymbol{v} \leftrightarrow \overline{F'(z)}$，速率为 $\lvert F'(z)\rvert$。流线是等值线 $\psi = \text{常数}$，与等势线 $\phi = \text{常数}$ 正交。流体不能穿过固壁，所以固壁必须是流线。

**例 8.5.4** 1. 沿 $x$ 方向、速率为 $U$ 的均匀流：$F = Uz$。
2. 绕圆柱 $\lvert z\rvert \le a$、在无穷远处为均匀流的流动：

$$
F(z) = U\left(z + \frac{a^2}{z}\right).
$$

在 $\lvert z\rvert = a$ 上 $\frac{a^2}{z} = \bar z$，所以 $F = 2U\operatorname{Re}z$ 是实数，$\psi = 0$：圆周是一条流线，且在无穷远处 $F \approx Uz$。速度 $\overline{F'} = U\left(1 - \frac{a^2}{\bar z^2}\right)$ 在驻点 $\pm a$ 处为零，在 $\pm\mathrm{i}a$ 处达到最大值 $2U$。除去因子 $2Ua$，$F$ 就是式 (8.6) 的 Joukowski 映射作用于 $z/a$；再与把圆周映为翼型的 Joukowski 映射复合，就得到绕翼型的流动。
3. 原点处强度为 $m$ 的源：$F = \frac{m}{2\pi}\operatorname{Log}z$，流线是射线 $\arg z = \text{常数}$。

![两个应用。左：单位圆盘内的稳态温度，上半圆周边值为 1，下半圆周边值为 0（例 8.5.3）；等温线是过 ±1 的圆弧。右：绕圆柱流动 F(z) = z + 1/z 的流线 Im F = 常数（例 8.5.4）；单位圆周本身是一条流线](./plots/laplace-applications.py)

## 小结

| 主题 | 要点 |
|---|---|
| 共形性 | $f'(z_0) \ne 0$：旋转角 $\arg f'(z_0)$，伸缩率 $\lvert f'(z_0)\rvert$；解析且单射 $\Rightarrow$ $f' \ne 0$，逆映射解析 |
| Riemann 映射定理 | 单连通区域 $D \subsetneq \mathbb{C}$ $\cong$ $\mathbb{D}$，满足 $f(z_0) = 0$、$f'(z_0) > 0$ 的映射唯一 |
| 分式线性变换 | 平移、旋转伸缩、反演的复合；广义圆周映为广义圆周；对称点映为对称点；三个点经由交比决定映射 |
| 标准的分式线性变换 | $\mathbb{H} \to \mathbb{D}$：$\mathrm{e}^{\mathrm{i}\theta}\frac{z - a}{z - \bar a}$；$\mathbb{D} \to \mathbb{D}$：$\mathrm{e}^{\mathrm{i}\theta}\frac{z - a}{1 - \bar az}$；实系数且 $ad - bc > 0$：$\mathbb{H} \to \mathbb{H}$ |
| 初等映射 | $z^{\pi/\beta}$：角形域 $\to \mathbb{H}$；$\mathrm{e}^z$：宽为 $\pi$ 的带形域 $\to \mathbb{H}$；Joukowski 映射：$\lvert z\rvert > 1 \to \mathbb{C}\setminus[-1, 1]$ |
| Schwarz 引理 | $f(\mathbb{D}) \subseteq \mathbb{D}$，$f(0) = 0$ $\Rightarrow$ $\lvert f(z)\rvert \le \lvert z\rvert$；$\mathbb{D}$ 的自同构都是分式线性变换 |
| Laplace 方程 | 调和函数 $\circ$ 解析函数仍调和；映到 $\mathbb{H}$ 或 $\mathbb{D}$，求解，再复合回来；复势 $F = \phi + \mathrm{i}\psi$，速度 $\overline{F'}$ |
