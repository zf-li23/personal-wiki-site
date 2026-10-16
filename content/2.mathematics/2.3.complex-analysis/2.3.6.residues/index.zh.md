---
title: 孤立奇点与留数
source_hash: 444707a55419
---

解析函数的大部分信息集中在它不解析的那些点上。有理函数除去一个常数之外由各极点处的主要部分决定；函数沿闭曲线的积分只取决于曲线内部的奇点；整函数在无穷远处的增长速度决定了它是不是多项式。本章用 [2.3.5](/2.3.5) 的 Laurent 级数把孤立奇点分为可去奇点、极点与本性奇点三类（包括无穷远点），并用 $f(z)$ 在该点附近的性态刻画每一类。

Laurent 级数的系数 $c_{-1}$ 就是留数。留数定理把围道积分的计算化为有限个留数的计算，后者基本上是代数运算；下一章（[2.3.7](/2.3.7)）把它用于实积分、偏微分方程中用到的 Fourier 逆变换与 Laplace 逆变换（[2.5.6](/2.5.6)）以及零点计数。这里的"奇点"指函数不解析的点，不要与 [2.4](/2.4) 中微分方程的奇点混淆，尽管两者有关：解析系数线性方程的奇点正是系数的奇点。

## 6.1. 孤立奇点

### 6.1.1. 按 Laurent 级数分类

**定义 6.1.1** 若 $f$ 在去心圆盘 $0 < \lvert z - z_0\rvert < \delta$ 内解析，但在 $z_0$ 处不解析（可以无定义），则称 $z_0$ 为 $f$ 的**孤立奇点**。

例如 $0$ 是 $\frac{\sin z}{z}$、$\frac1{z^2}$ 与 $\mathrm{e}^{1/z}$ 的孤立奇点。奇点并不都是孤立的：

- $f(z) = \frac{1}{\sin(1/z)}$ 在 $z = \frac{1}{k\pi}$（$k \in \mathbb{Z}\setminus\{0\}$）与 $0$ 处都不解析。每个 $\frac1{k\pi}$ 是孤立的，$0$ 却不是，因为 $0$ 的任何邻域都含有点 $\frac{1}{k\pi}$。
- $\operatorname{Log} z$ 在 $0$ 的任何去心圆盘内都不解析，因为 $\log z$ 没有在绕 $0$ 的整个圆周上连续的分支（[2.3.3](/2.3.3)）。因此支点 $0$ 不是孤立奇点。

在孤立奇点处，Laurent 定理（定理 5.5.2）给出展开式

$$
f(z) = \sum_{n=-\infty}^{\infty}c_n(z - z_0)^n = \underbrace{\sum_{n=1}^\infty\frac{c_{-n}}{(z - z_0)^n}}_{\text{主要部分}} + \underbrace{\sum_{n=0}^\infty c_n(z - z_0)^n}_{\text{解析部分}}, \qquad 0 < \lvert z - z_0\rvert < \delta. \tag{6.1}
$$

**定义 6.1.2** 式 (6.1) 中负幂项之和称为 $f$ 在 $z_0$ 处的**主要部分**。孤立奇点 $z_0$ 称为

1. **可去奇点**，若主要部分为零（对一切 $n \ge 1$，$c_{-n} = 0$）；
2. $m$ 阶**极点**，若主要部分只有有限项，且 $c_{-m} \ne 0$，$n > m$ 时 $c_{-n} = 0$；正整数 $m$ 称为**极点的阶**，一阶极点称为**单极点**；
3. **本性奇点**，若主要部分有无穷多个非零项。

$f$ 中只有主要部分"感受"得到奇点：解析部分是在 $\lvert z - z_0\rvert < \delta$ 内收敛的幂级数。三类奇点的性态截然不同，下面三小节用 $z \to z_0$ 时 $f(z)$ 的极限分别刻画它们。

### 6.1.2. 可去奇点

**定理 6.1.1（Riemann 可去奇点定理）** 设 $z_0$ 是 $f$ 的孤立奇点，则下列条件等价：

1. $z_0$ 是可去奇点；
2. $\lim_{z\to z_0}f(z)$ 存在且有限；
3. $f$ 在某个去心圆盘 $0 < \lvert z - z_0\rvert < \delta'$ 内有界。

此时令 $f(z_0) = c_0 = \lim_{z\to z_0}f(z)$，$f$ 就在 $z_0$ 处解析。

**证明** (1)$\Rightarrow$(2)：$f$ 在去心圆盘内等于一个收敛幂级数，其和函数在 $z_0$ 处连续，值为 $c_0$。(2)$\Rightarrow$(3) 显然。(3)$\Rightarrow$(1)：设 $0 < \lvert z - z_0\rvert < \delta'$ 时 $\lvert f\rvert \le M$。对 $n \ge 1$ 与 $0 < \rho < \delta'$，由式 (5.4) 的系数公式与长大不等式（定理 4.1.2），

$$
\lvert c_{-n}\rvert = \left\lvert\frac{1}{2\pi\mathrm{i}}\oint_{\lvert z - z_0\rvert = \rho}f(z)(z - z_0)^{n-1}\,\mathrm{d}z\right\rvert \le \frac{1}{2\pi}\cdot M\rho^{n-1}\cdot2\pi\rho = M\rho^n.
$$

令 $\rho \to 0$ 得 $c_{-n} = 0$。$\square$

这个定理说明，有界解析函数的奇点都不是真正的奇点。它常用来证明某个商其实是解析的。

**例 6.1.1** 1. $\frac{\sin z}{z} = 1 - \frac{z^2}{6} + \cdots$ 与 $\frac{\mathrm{e}^z - 1}{z} = 1 + \frac z2 + \cdots$ 以 $0$ 为可去奇点，补充定义的值都是 $1$。
2. $\frac{1}{z^2} - \frac{1}{z\sin z}$ 以 $0$ 为可去奇点：由 $\frac{z}{\sin z} = 1 + \frac{z^2}{6} + \frac{7z^4}{360} + \cdots$ 得 $\frac{1}{z\sin z} = \frac{1}{z^2} + \frac16 + \frac{7z^2}{360} + \cdots$，所以差趋于 $-\frac16$。

### 6.1.3. 极点

**定理 6.1.2** 设 $z_0$ 是 $f$ 的孤立奇点，$m \ge 1$，则下列条件等价：

1. $z_0$ 是 $m$ 阶极点；
2. 在 $z_0$ 附近 $f(z) = \dfrac{g(z)}{(z - z_0)^m}$，其中 $g$ 在 $z_0$ 处解析且 $g(z_0) \ne 0$；
3. $\lim_{z\to z_0}(z - z_0)^mf(z)$ 存在、有限且不为零；
4. $z_0$ 是 $\frac1f$ 的 $m$ 阶零点（去掉 $\frac1f$ 在 $z_0$ 处的可去奇点之后）。

特别地，$z_0$ 是极点当且仅当 $\lim_{z\to z_0}f(z) = \infty$。

**证明** (1)$\Leftrightarrow$(2)：式 (6.1) 乘以 $(z - z_0)^m$ 得 $g(z) = c_{-m} + c_{-m+1}(z - z_0) + \cdots$，它解析且 $g(z_0) = c_{-m}$；反之，$g$ 的 Taylor 级数除以 $(z - z_0)^m$，得到的主要部分止于 $c_{-m} = g(z_0) \ne 0$。(2)$\Leftrightarrow$(3)：对 $(z - z_0)^mf$ 用定理 6.1.1。(2)$\Leftrightarrow$(4)：$\frac1f = (z - z_0)^m\frac{1}{g}$，其中 $\frac1g$ 在 $z_0$ 处解析且不为零；再用定理 5.4.1。最后一句：若 $z_0$ 是极点，则 $\lvert f\rvert = \lvert g\rvert/\lvert z - z_0\rvert^m \to \infty$；反之，若 $f \to \infty$，则 $\frac1f \to 0$，于是 $\frac1f$ 以 $z_0$ 为可去奇点，且 $z_0$ 是它的零点；由于 $\frac1f \not\equiv 0$，由定理 5.4.2 这个零点有有限的阶 $m$，再用 (4)。$\square$

对于商，极点的阶可以由零点的阶读出：

**定理 6.1.3** 设 $P$、$Q$ 在 $z_0$ 处解析且不恒为零，$z_0$ 是 $P$ 的 $k$ 阶零点（$P(z_0) \ne 0$ 时 $k = 0$），是 $Q$ 的 $l$ 阶零点（$l \ge 1$）。则 $l > k$ 时 $\frac{P}{Q}$ 以 $z_0$ 为 $l - k$ 阶极点，$l \le k$ 时以 $z_0$ 为可去奇点。

**证明** 写 $P = (z - z_0)^k\varphi$，$Q = (z - z_0)^l\psi$，其中 $\varphi(z_0), \psi(z_0) \ne 0$；则 $\frac PQ = (z - z_0)^{k-l}\frac{\varphi}{\psi}$，而 $\frac\varphi\psi$ 在 $z_0$ 处解析且不为零。$\square$

**例 6.1.2** 1. $\frac{1}{\sin z}$、$\cot z$ 与 $\frac{1}{\mathrm{e}^z - 1}$ 以分母的单零点为单极点，分别是 $z = k\pi$、$z = k\pi$ 与 $z = 2k\pi\mathrm{i}$（$k \in \mathbb{Z}$）。
2. $\frac{z}{1 - \cos z}$ 在 $0$ 处：分子有一阶零点，$1 - \cos z = \frac{z^2}{2} - \cdots$ 有二阶零点，所以 $0$ 是单极点。
3. $\frac{\mathrm{e}^z - 1}{z^4}$ 以 $0$ 为三阶极点；$\frac{z - \sin z}{z^5}$ 以 $0$ 为二阶极点，因为 $z - \sin z$ 有三阶零点。只看分母的幂次会得出错误的阶。

### 6.1.4. 本性奇点

由定理 6.1.1 与定理 6.1.2，孤立奇点是可去奇点当且仅当 $f$ 有有限极限，是极点当且仅当 $f \to \infty$。因此剩下的一类由"没有任何极限"来刻画：

**定理 6.1.4** $f$ 的孤立奇点 $z_0$ 是本性奇点，当且仅当 $\lim_{z\to z_0}f(z)$ 既不存在有限值，也不是 $\infty$。

**例 6.1.3** $0$ 是 $\mathrm{e}^{1/z} = \sum_{n\ge0}\frac{1}{n!z^n}$ 的本性奇点。沿正实轴 $\mathrm{e}^{1/x} \to +\infty$；沿负实轴 $\mathrm{e}^{1/x} \to 0$；在虚轴上 $\lvert\mathrm{e}^{1/(\mathrm{i}y)}\rvert = 1$。同样，$\sin\frac1z$ 与 $\cos\frac1z$ 以 $0$ 为本性奇点。

事实上，本性奇点附近的性态已经杂乱到了极点：

**定理 6.1.5（Casorati–Weierstrass 定理）** 若 $z_0$ 是 $f$ 的本性奇点，则对任意 $A \in \mathbb{C}$，存在数列 $z_n \to z_0$ 使 $f(z_n) \to A$。等价地，每个去心圆盘 $0 < \lvert z - z_0\rvert < \delta$ 的像在 $\mathbb{C}$ 中稠密。

**证明** 若不然，则存在 $A \in \mathbb{C}$、$\varepsilon > 0$ 与 $\delta > 0$，使 $0 < \lvert z - z_0\rvert < \delta$ 时 $\lvert f(z) - A\rvert \ge \varepsilon$。函数 $g(z) = \frac{1}{f(z) - A}$ 在那里解析且以 $\frac1\varepsilon$ 为界，由定理 6.1.1，$z_0$ 是 $g$ 的可去奇点。若 $g(z_0) \ne 0$，则 $f = A + \frac1g$ 在 $z_0$ 处有有限极限；若 $g(z_0) = 0$，则 $f \to \infty$。两种情形下 $z_0$ 都不是本性奇点，矛盾。$\square$

一个深刻得多的结果（这里不加证明）说，稠密可以加强为"取到"，至多有一个例外：

**定理 6.1.6（Picard 大定理）** 在本性奇点的任何去心邻域内，$f$ 取到每个复数值无穷多次，至多有一个例外值。

**例 6.1.4** 对 $\mathrm{e}^{1/z}$，例外值是 $0$。对任意 $w \ne 0$，方程 $\mathrm{e}^{1/z} = w$ 即 $\frac1z = \operatorname{Log}w + 2k\pi\mathrm{i}$，它的解

$$
z_k = \frac{1}{\operatorname{Log}w + 2k\pi\mathrm{i}}, \qquad k \in \mathbb{Z},
$$

在 $\lvert k\rvert \to \infty$ 时趋于 $0$。所以在 $0$ 的每个邻域内，每个非零值都被取到无穷多次。

![1/z^2（左）与 e^{1/z}（右）在 0 附近的定义域着色图：色相表示 f(z) 的辐角，亮带是 log2 |f(z)| 的等值线。二阶极点周围每种颜色出现两次，模均匀增大；本性奇点附近颜色与亮带挤在一起，每个值都被取到无穷多次。白点是 e^{1/z} = 1 + i 的解，它们聚集于 0](./plots/singularity-types.py)

分类总结如下。

| $z_0$ 的类型 | Laurent 级数的主要部分 | $z \to z_0$ 时 $f(z)$ 的性态 |
|---|---|---|
| 可去奇点 | $0$ | 有有限极限；$f$ 在附近有界 |
| $m$ 阶极点 | 有限项，止于 $c_{-m}(z - z_0)^{-m}$ | $f \to \infty$；$(z - z_0)^mf \to c_{-m} \ne 0$ |
| 本性奇点 | 无穷多项 | 无极限；每个去心圆盘的像稠密（Casorati–Weierstrass） |

## 6.2. 无穷远点

### 6.2.1. 无穷远点的分类

研究 $\lvert z\rvert$ 很大时 $f$ 的性态，可以把 $\infty$ 看作扩充复平面 $\hat{\mathbb{C}}$ 中的一点，作代换 $z = \frac1w$。

**定义 6.2.1** 若 $f$ 在某个 $R < \lvert z\rvert < \infty$（$R \ge 0$）内解析，则称 $\infty$ 为 $f$ 的孤立奇点。它的类型（可去奇点、$m$ 阶极点、本性奇点）定义为 $g(w) = f\left(\frac1w\right)$ 的孤立奇点 $w = 0$ 的类型。

用 $f$ 在圆环 $R < \lvert z\rvert < \infty$ 内的 Laurent 级数表示，

$$
f(z) = \sum_{n=-\infty}^{\infty}c_nz^n, \qquad g(w) = \sum_{n=-\infty}^{\infty}c_nw^{-n},
$$

$\infty$ 处的主要部分由正幂项 $\sum_{n\ge1}c_nz^n$ 组成。因此：$f$ 没有正幂项时 $\infty$ 是可去奇点（等价于 $z \to \infty$ 时 $f$ 有有限极限）；最高次项是 $c_mz^m$（$c_m \ne 0$）时 $\infty$ 是 $m$ 阶极点（等价于 $f \to \infty$）；有无穷多个正幂项时 $\infty$ 是本性奇点（等价于 $f$ 既无有限极限也不趋于 $\infty$）。

**例 6.2.1** 1. $m$ 次多项式（$m \ge 1$）以 $\infty$ 为 $m$ 阶极点。
2. 有理函数 $\frac{P}{Q}$ 在 $\deg P \le \deg Q$ 时以 $\infty$ 为可去奇点，否则以 $\infty$ 为 $\deg P - \deg Q$ 阶极点。
3. $\mathrm{e}^z$、$\sin z$、$\cos z$ 以 $\infty$ 为本性奇点：它们的 Maclaurin 级数也就是在 $0 < \lvert z\rvert < \infty$ 内的 Laurent 级数。
4. $z^2\mathrm{e}^{1/z} = z^2 + z + \frac12 + \frac{1}{6z} + \cdots$ 以 $\infty$ 为二阶极点（以 $0$ 为本性奇点）。
5. $\tan z$ 与 $\frac{1}{\sin z}$：极点 $\frac\pi2 + k\pi$（相应地 $k\pi$）趋于 $\infty$，所以 $\infty$ 不是孤立奇点。

**例 6.2.2** 求

$$
f(z) = z\,\mathrm{e}^{1/(z-1)} + \frac{1}{z^2} - \frac{1}{z\sin z}
$$

在 $\hat{\mathbb{C}}$ 中的全部奇点并判断类型。

第一项除 $z = 1$ 外解析；后两项除 $z\sin z$ 的零点 $z = k\pi$（$k \in \mathbb{Z}$）外解析。

- $z = 0$：第一项在此解析，后两项合起来是可去奇点（例 6.1.1）。所以 $0$ 是可去奇点。
- $z = k\pi$，$k \ne 0$：$z\sin z$ 有单零点，$\frac{1}{z\sin z}$ 有单极点，其余各项解析。所以每个 $k\pi$ 是单极点。
- $z = 1$：$z\,\mathrm{e}^{1/(z-1)}$ 含 $z - 1$ 的无穷多个负幂项（例 5.5.4），其余各项在 $1$ 处解析。所以 $1$ 是本性奇点。
- $z = \infty$：极点 $k\pi$ 聚集于 $\infty$，所以 $\infty$ 是非孤立奇点。

注意，和的奇点可能比各加项的奇点"好"（如 $0$ 处），但在只有一个加项有奇点的点，和的奇点类型不会变好。

### 6.2.2. 整函数与有理函数

**整函数** $f(z) = \sum_{n\ge0}c_nz^n$ 的 Maclaurin 级数在整个 $\mathbb{C}$ 上收敛，因此它也是 $\infty$ 处的 Laurent 级数。$\infty$ 处的主要部分是 $\sum_{n\ge1}c_nz^n$，$\infty$ 的类型决定了 $f$ 是哪一种函数：

**定理 6.2.1** 设 $f$ 是整函数，则

1. $\infty$ 是 $f$ 的可去奇点当且仅当 $f$ 是常数；
2. $\infty$ 是 $m$ 阶极点当且仅当 $f$ 是 $m$ 次多项式；
3. 其余情形 $\infty$ 是本性奇点（此时称 $f$ 为超越整函数）。

第 1 条包含了 **Liouville 定理**（定理 4.5.2）：有界整函数以 $\infty$ 为可去奇点（对 $f(1/w)$ 用定理 6.1.1），因而是常数。下面的推广是处理"求所有满足……的整函数"一类问题的标准工具。

**定理 6.2.2（广义 Liouville 定理）** 设 $f$ 是整函数，且存在常数 $M, R_0 > 0$ 与整数 $m \ge 0$，使 $\lvert z\rvert \ge R_0$ 时 $\lvert f(z)\rvert \le M\lvert z\rvert^m$。则 $f$ 是次数不超过 $m$ 的多项式。

**证明** 在圆周 $\lvert z\rvert = \rho \ge R_0$ 上用式 (5.2) 的系数公式，

$$
\lvert c_n\rvert \le \frac{1}{2\pi}\cdot\frac{M\rho^m}{\rho^{n+1}}\cdot2\pi\rho = M\rho^{m-n}.
$$

$n > m$ 时右端在 $\rho \to \infty$ 时趋于 $0$，所以 $c_n = 0$。$\square$

**例 6.2.3** 求所有满足"对一切 $z \in \mathbb{C}$，$\lvert f(z)\rvert \le \lvert z\rvert^2$"且 $f(1 + \mathrm{i}) = \mathrm{i}$ 的整函数。

函数 $g(z) = \frac{f(z)}{z^2}$ 在 $0 < \lvert z\rvert < \infty$ 内解析且以 $1$ 为界。由定理 6.1.1，$0$ 是它的可去奇点，所以 $g$ 是有界整函数，从而是常数 $c$，$\lvert c\rvert \le 1$。于是 $f(z) = cz^2$，由 $f(1 + \mathrm{i}) = 2\mathrm{i}c = \mathrm{i}$ 得 $c = \frac12$。所求函数只有 $f(z) = \frac{z^2}{2}$（且 $\lvert c\rvert = \frac12 \le 1$，它确实满足不等式）。

**例 6.2.4** 对实部或虚部的限制，与适当的函数复合之后，同样迫使函数为常数。

1. 若 $f$ 是整函数且对一切 $z$ 有 $\operatorname{Re}f(z) \le M$，则 $\lvert\mathrm{e}^{f(z)}\rvert = \mathrm{e}^{\operatorname{Re}f(z)} \le \mathrm{e}^M$，所以 $\mathrm{e}^f$ 是常数；由 $f'\mathrm{e}^f = 0$ 得 $f' = 0$，$f$ 是常数。
2. 若 $f$ 是整函数且 $\operatorname{Im}f(z) \ge -1$，则 $\lvert f(z) + 2\mathrm{i}\rvert \ge \operatorname{Im}f(z) + 2 \ge 1$，所以 $\frac{1}{f + 2\mathrm{i}}$ 是有界整函数，$f$ 是常数。
3. 求所有对一切 $z$ 满足 $0 \le \operatorname{Re}f'(z) \le 1$ 的整函数 $f$。对 $f'$ 用第 1 条，$f'$ 是常数 $a$，$0 \le \operatorname{Re}a \le 1$。因此这类函数的集合是 $\{az + b : b \in \mathbb{C},\ 0 \le \operatorname{Re}a \le 1\}$，而这种形式的函数显然都满足条件。

**定义 6.2.2** 若函数在区域 $D$ 内除孤立奇点外解析，且这些孤立奇点都是极点，则称它在 $D$ 内亚纯。在 $\mathbb{C}$ 上亚纯的函数称为**亚纯函数**。

有理函数、$\tan z$ 与 $\frac{1}{\mathrm{e}^z - 1}$ 都是亚纯函数；$\mathrm{e}^{1/z}$ 不是。把 $\infty$ 也考虑进来，就刻画了有理函数：

**定理 6.2.3** 若 $f$ 在 $\hat{\mathbb{C}}$ 上除极点外解析（$\infty$ 是极点或可去奇点），则 $f$ 是有理函数，并且等于它在各有限极点处的主要部分之和，加上 $\infty$ 处的主要部分（一个多项式），再加上一个常数。

**证明** 由于 $\infty$ 至多是孤立奇点，$f$ 在某个圆环 $R < \lvert z\rvert < \infty$ 内解析，所以有限极点都位于某个圆盘 $\lvert z\rvert \le R$ 内；它们也不能聚集于有限点（聚点将是非孤立奇点），因此只有有限个，记为 $a_1, \dots, a_k$。设 $P_j(z)$ 是 $a_j$ 处的主要部分，它是 $\frac{1}{z - a_j}$ 的多项式；$P_\infty(z)$ 是 $\infty$ 处的主要部分，它是 $z$ 的不含常数项的多项式。则 $h = f - P_\infty - \sum_jP_j$ 在 $\mathbb{C}$ 中只有可去奇点；在 $\infty$ 处，各 $P_j \to 0$，而 $f - P_\infty$ 有有限极限。所以 $h$ 是有界整函数，由 Liouville 定理它是常数。$\square$

这个定理就是部分分式分解在复分析中的含义。

## 6.3. 留数

### 6.3.1. 留数定理

**定义 6.3.1** 设 $z_0 \in \mathbb{C}$ 是 $f$ 的孤立奇点，Laurent 级数如式 (6.1)。$f$ 在 $z_0$ 处的**留数**是

$$
\operatorname{Res}(f, z_0) = c_{-1} = \frac{1}{2\pi\mathrm{i}}\oint_{\lvert z - z_0\rvert = \rho}f(z)\,\mathrm{d}z, \qquad 0 < \rho < \delta.
$$

第二个等号是式 (5.4) 取 $n = -1$；它解释了这个名称：$f$ 绕 $z_0$ 积分时，Laurent 级数中除 $c_{-1}(z - z_0)^{-1}$ 外每一项的积分都是 $0$，"留下"的只有 $2\pi\mathrm{i}\,c_{-1}$。

**定理 6.3.1（留数定理）** 设 $C$ 是正向的分段光滑简单闭曲线，$f$ 在 $C$ 上及 $C$ 内部除 $C$ 内有限个孤立奇点 $z_1, \dots, z_n$ 外解析，则

$$
\oint_Cf(z)\,\mathrm{d}z = 2\pi\mathrm{i}\sum_{k=1}^n\operatorname{Res}(f, z_k). \tag{6.2}
$$

**证明** 在 $C$ 内以每个 $z_k$ 为圆心作正向小圆周 $C_k$，使它们互不相交。在 $C$ 与各 $C_k$ 之间的多连通区域内 $f$ 解析，由多连通区域上的 Cauchy 积分定理（[2.3.4](/2.3.4)），$\oint_Cf\,\mathrm{d}z = \sum_k\oint_{C_k}f\,\mathrm{d}z = \sum_k2\pi\mathrm{i}\operatorname{Res}(f, z_k)$。$\square$

Cauchy 积分定理（$f$ 在内部解析，所有留数为零）与 **Cauchy 积分公式**（$\frac{f(z)}{z - z_0}$ 在 $z_0$ 处的留数是 $f(z_0)$）都是它的特例。

### 6.3.2. 留数的计算

在本性奇点处，留数只能从 Laurent 级数读出。在极点处则有不必展开级数的公式。

**定理 6.3.2** 设 $z_0 \in \mathbb{C}$ 是 $f$ 的孤立奇点。

1. 若 $z_0$ 是可去奇点，则 $\operatorname{Res}(f, z_0) = 0$。
2. 若 $z_0$ 是单极点，则 $\operatorname{Res}(f, z_0) = \lim_{z\to z_0}(z - z_0)f(z)$。
3. 若 $f = \frac PQ$，$P$、$Q$ 在 $z_0$ 处解析，$P(z_0) \ne 0$，$Q(z_0) = 0$，$Q'(z_0) \ne 0$，则 $\operatorname{Res}(f, z_0) = \dfrac{P(z_0)}{Q'(z_0)}$。
4. 若 $z_0$ 是阶数不超过 $m$ 的极点，则

$$
\operatorname{Res}(f, z_0) = \frac{1}{(m-1)!}\lim_{z\to z_0}\frac{\mathrm{d}^{m-1}}{\mathrm{d}z^{m-1}}\left[(z - z_0)^mf(z)\right]. \tag{6.3}
$$

**证明** 第 1 条由定义即得。对第 4 条，$(z - z_0)^mf(z) = c_{-m} + c_{-m+1}(z - z_0) + \cdots + c_{-1}(z - z_0)^{m-1} + \cdots$ 在 $z_0$ 处解析（若实际阶数小于 $m$，开头几个系数可能为零），它在 $z_0$ 处的 $m-1$ 阶导数是 $(m-1)!\,c_{-1}$。第 2 条是 $m = 1$ 的情形。对第 3 条，$z_0$ 是单极点，且 $(z - z_0)\frac{P(z)}{Q(z)} = \frac{P(z)}{(Q(z) - Q(z_0))/(z - z_0)} \to \frac{P(z_0)}{Q'(z_0)}$。$\square$

$m$ 大于真实阶数时式 (6.3) 仍然成立，确定准确阶数较麻烦时这很方便，只是求导会更长。若 $f$ 是偶函数，$f(-z) = f(z)$，则它在 $0$ 处的 Laurent 级数只含偶次幂，$\operatorname{Res}(f, 0) = 0$。

**例 6.3.1** 1. $f(z) = \frac{\mathrm{e}^z}{z^2(z-1)}$。在单极点 $1$ 处：$\operatorname{Res}(f, 1) = \frac{\mathrm{e}^z}{z^2}\big|_{z=1} = \mathrm{e}$。在二阶极点 $0$ 处：

$$
\operatorname{Res}(f, 0) = \frac{\mathrm{d}}{\mathrm{d}z}\frac{\mathrm{e}^z}{z - 1}\bigg|_{z=0} = \frac{\mathrm{e}^z(z - 2)}{(z-1)^2}\bigg|_{z=0} = -2.
$$

因此 $\oint_{\lvert z\rvert = 2}f\,\mathrm{d}z = 2\pi\mathrm{i}(\mathrm{e} - 2)$，而 $\oint_{\lvert z\rvert = 1/2}f\,\mathrm{d}z = -4\pi\mathrm{i}$。
2. $\cot z = \frac{\cos z}{\sin z}$ 在 $k\pi$ 处：由第 3 条，$\operatorname{Res}(\cot z, k\pi) = \frac{\cos k\pi}{\cos k\pi} = 1$。
3. $\frac{1}{z^4 + 1}$ 在 $z^4 = -1$ 的根 $z_k$ 处：$\operatorname{Res} = \frac{1}{4z_k^3} = \frac{z_k}{4z_k^4} = -\frac{z_k}{4}$。
4. $\frac{z}{1 - \cos z}$ 在单极点 $0$ 处（例 6.1.2）：$\lim_{z\to0}\frac{z^2}{1 - \cos z} = 2$，留数为 $2$。
5. $z^2\sin\frac1z = z^2\left(\frac1z - \frac{1}{6z^3} + \frac{1}{120z^5} - \cdots\right) = z - \frac{1}{6z} + \cdots$ 在本性奇点 $0$ 处：留数为 $-\frac16$。
6. 例 6.2.2 中的函数：$\operatorname{Res}(f, 0) = 0$（可去奇点）。在 $k\pi$（$k \ne 0$）处，对 $-\frac{1}{z\sin z}$ 用第 3 条得 $-\frac{1}{(\sin z + z\cos z)|_{z=k\pi}} = -\frac{(-1)^k}{k\pi}$。在本性奇点 $1$ 处，由例 5.5.4，$\operatorname{Res}(f, 1) = c_{-1} = \frac32$。

### 6.3.3. 无穷远点的留数

**定义 6.3.2** 设 $\infty$ 是 $f$ 的孤立奇点，$f$ 在 $R < \lvert z\rvert < \infty$ 内的 Laurent 级数为 $\sum c_nz^n$。$f$ 在 $\infty$ 处的留数是

$$
\operatorname{Res}(f, \infty) = \frac{1}{2\pi\mathrm{i}}\oint_{C^-}f(z)\,\mathrm{d}z = -c_{-1},
$$

其中 $C^-$ 是顺时针方向的圆周 $\lvert z\rvert = \rho > R$（使 $\infty$ 的邻域在左侧）。

有两点要注意。第一，$\infty$ 处的留数是 $z^{-1}$ 的系数的相反数，而不是某个正幂项的系数。第二，即使 $\infty$ 是可去奇点，留数也可以不为零：$\operatorname{Res}\left(\frac1z, \infty\right) = -1$。在积分中代换 $z = \frac1w$，得到实用的公式

$$
\operatorname{Res}(f, \infty) = -\operatorname{Res}\left(\frac{1}{w^2}f\left(\frac1w\right), 0\right); \qquad \operatorname{Res}(f, \infty) = -\lim_{z\to\infty}zf(z) \ \text{（若 } z \to \infty \text{ 时 } f(z) \to 0\text{）}.
$$

特别地，若在 $\infty$ 处 $f(z) = O(z^{-2})$，则 $\operatorname{Res}(f, \infty) = 0$。

**定理 6.3.3** 若 $f$ 在 $\mathbb{C}$ 中除有限个孤立奇点 $z_1, \dots, z_n$ 外解析，则 $f$ 在 $\hat{\mathbb{C}}$ 中全部留数之和为零：

$$
\sum_{k=1}^n\operatorname{Res}(f, z_k) + \operatorname{Res}(f, \infty) = 0.
$$

**证明** 取 $\rho$ 充分大，使所有 $z_k$ 都在 $\lvert z\rvert = \rho$ 内部。由留数定理，逆时针方向的积分等于 $2\pi\mathrm{i}\sum_k\operatorname{Res}(f, z_k)$；由定义，顺时针方向的积分等于 $2\pi\mathrm{i}\operatorname{Res}(f, \infty)$。$\square$

这个定理把曲线内部的许多留数换成曲线外部的少数几个留数。

**例 6.3.2** 计算 $\oint_{\lvert z\rvert = 2}\frac{z^{15}}{(z^2+1)^2(z^4+2)^3}\,\mathrm{d}z$。

全部奇点——$\pm\mathrm{i}$（二阶极点）与 $z^4 = -2$ 的四个根（三阶极点，模为 $2^{1/4}$）——都在圆周内部，直接计算它们的留数很繁琐。外部只有 $\infty$。分母的次数是 $16$，所以 $zf(z) \to 1$，$\operatorname{Res}(f, \infty) = -1$。因此积分等于 $-2\pi\mathrm{i}\operatorname{Res}(f, \infty) = 2\pi\mathrm{i}$。

**例 6.3.3** 计算 $I = \oint_{\lvert z\rvert = 2}\frac{z^2\,\mathrm{e}^{1/z}}{(z-1)(z-3)}\,\mathrm{d}z$。

圆周内部有本性奇点 $0$ 与单极点 $1$。外部有单极点 $3$ 与 $\infty$，所以 $I = -2\pi\mathrm{i}\left[\operatorname{Res}(f, 3) + \operatorname{Res}(f, \infty)\right]$。首先 $\operatorname{Res}(f, 3) = \frac{9\,\mathrm{e}^{1/3}}{2}$。当 $\lvert z\rvert > 3$ 时，

$$
f(z) = \mathrm{e}^{1/z}\left(1 - \frac1z\right)^{-1}\left(1 - \frac3z\right)^{-1} = \left(1 + \frac1z + \cdots\right)\left(1 + \frac1z + \cdots\right)\left(1 + \frac3z + \cdots\right) = 1 + \frac5z + \cdots,
$$

所以 $\operatorname{Res}(f, \infty) = -5$。因此 $I = -2\pi\mathrm{i}\left(\frac92\mathrm{e}^{1/3} - 5\right) = (10 - 9\,\mathrm{e}^{1/3})\pi\mathrm{i}$。本性奇点 $0$ 处的留数始终不需要计算。

**例 6.3.4** $z\,\mathrm{e}^{1/(z-1)}$ 唯一的有限奇点是 $1$，留数为 $\frac32$（例 5.5.4）。由定理 6.3.3，$\operatorname{Res}\left(z\,\mathrm{e}^{1/(z-1)}, \infty\right) = -\frac32$；也可以把 $\frac{1}{w^2}f\left(\frac1w\right)$ 在 $w = 0$ 处展开来验证。

## 小结

| 主题 | 要点 |
|---|---|
| 可去奇点 | 在 $z_0$ 附近有界 $\Leftrightarrow$ 有有限极限 $\Leftrightarrow$ 没有主要部分（Riemann） |
| $m$ 阶极点 | $f = g/(z - z_0)^m$，$g(z_0) \ne 0$ $\Leftrightarrow$ $f \to \infty$；对 $P/Q$ 用零点的阶相减 |
| 本性奇点 | 无极限；Casorati–Weierstrass 定理、Picard 定理 |
| 无穷远点 | 看 $f(1/w)$ 在 $0$ 处的类型；主要部分 = 正幂项；整函数 $f$：常数 / 多项式 / 超越整函数 |
| Liouville 型结果 | $\lvert f\rvert \le M\lvert z\rvert^m$ $\Rightarrow$ 次数 $\le m$ 的多项式；实部或虚部有界 $\Rightarrow$ 常数 |
| 留数 | $\operatorname{Res}(f, z_0) = c_{-1}$；单极点：$\lim(z - z_0)f$ 或 $P/Q'$；$m$ 阶：式 (6.3)；本性奇点：Laurent 级数 |
| 留数定理 | $\oint_Cf\,\mathrm{d}z = 2\pi\mathrm{i}\sum$（$C$ 内的 $\operatorname{Res}$） |
| $\infty$ 处的留数 | $-c_{-1}$；$\hat{\mathbb{C}}$ 中全部留数之和为 $0$ |
