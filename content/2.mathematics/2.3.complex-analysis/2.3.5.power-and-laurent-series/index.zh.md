---
title: 幂级数与 Laurent 级数
source_hash: 3056da1329f3
---

在实分析中，一个函数可以无穷次可导却不等于它的 Taylor 级数之和，而 Taylor 级数的收敛半径往往无法单从实轴上得到解释（[2.2.9](/2.2.9)）。在复平面上，这两个疑问都消失了。Cauchy 积分公式（[2.3.4](/2.3.4)）表明，解析函数在每一点附近都是一个收敛的**幂级数**之和，而且这个级数在函数保持解析的最大圆盘内收敛。因此解析性就是局部可展开为幂级数的性质，由此又得到零点的孤立性和唯一性定理：区域上的解析函数由它在任何一个有极限点的集合上的值所决定。

在函数不解析的点附近，幂级数不再够用，还需要含负幂次的级数。这种 Laurent 级数在圆环中收敛，其系数由围道积分给出。$(z - z_0)^{-1}$ 的系数就是下一章（[2.3.6](/2.3.6)）的留数，[2.3.7](/2.3.7) 的全部应用都由它驱动。本章假定读者熟悉 [2.2.9](/2.2.9) 中实幂级数的内容；把绝对值读作模，多数证明可以原样照搬。

## 5.1. 复数项级数与函数项级数

### 5.1.1. 复数项级数

**定义 5.1.1** 设 $z_n = a_n + \mathrm{i}b_n$ 为复数。若级数 $\sum_{n=1}^\infty z_n$ 的部分和 $S_n = \sum_{k=1}^n z_k$ 满足 $\lvert S_n - S\rvert \to 0$，则称该级数收敛于 $S$；否则称它发散。若 $\sum\lvert z_n\rvert$ 收敛，则称该级数**绝对收敛**；若它收敛但不绝对收敛，则称它**条件收敛**。

由于 $\max(\lvert a_n\rvert, \lvert b_n\rvert) \le \lvert z_n\rvert \le \lvert a_n\rvert + \lvert b_n\rvert$，收敛性问题可以化为实级数的问题：

**定理 5.1.1** 1. $\sum z_n$ 收敛当且仅当 $\sum a_n$ 与 $\sum b_n$ 都收敛，此时 $\sum z_n = \sum a_n + \mathrm{i}\sum b_n$。
2. 若 $\sum z_n$ 收敛，则 $z_n \to 0$。
3. 绝对收敛的级数收敛，且任意重排其各项不改变和。

**Cauchy 收敛准则**、对 $\sum \lvert z_n\rvert$ 使用的比较判别法、比值判别法和根值判别法，以及两个绝对收敛级数的 **Cauchy 乘积**，都与实级数一样成立。对复数 $b_n$，**Dirichlet 判别法**也成立：若实数 $a_n$ 单调递减趋于 $0$，且 $\sum b_n$ 的部分和有界，则 $\sum a_nb_n$ 收敛（[2.2.8](/2.2.8) 中用 Abel 变换给出的证明只用到三角不等式）。

**例 5.1.1** 当 $\theta \notin 2\pi\mathbb{Z}$ 时，$\sum_{n\ge1}\mathrm{e}^{\mathrm{i}n\theta}$ 的部分和有界：

$$
\left\lvert\sum_{k=1}^n \mathrm{e}^{\mathrm{i}k\theta}\right\rvert = \left\lvert\frac{\mathrm{e}^{\mathrm{i}\theta}(1 - \mathrm{e}^{\mathrm{i}n\theta})}{1 - \mathrm{e}^{\mathrm{i}\theta}}\right\rvert \le \frac{2}{\lvert 1 - \mathrm{e}^{\mathrm{i}\theta}\rvert} = \frac{1}{\lvert\sin(\theta/2)\rvert}.
$$

因此对每个 $p > 0$ 与 $\theta \notin 2\pi\mathbb{Z}$，$\sum_{n\ge1}\frac{\mathrm{e}^{\mathrm{i}n\theta}}{n^p}$ 收敛；只有 $p > 1$ 时才绝对收敛。下面研究幂级数在收敛圆周上的性态时，这个估计会反复用到。

### 5.1.2. 函数项级数与一致收敛

对集合 $E \subseteq \mathbb{C}$ 上的**函数项级数** $\sum f_n(z)$，逐点收敛、**一致收敛**和 **Weierstrass 判别法**的定义与证明都与 [2.2.9](/2.2.9) 相同：若在 $E$ 上 $\lvert f_n(z)\rvert \le M_n$ 且 $\sum M_n < \infty$，则该级数在 $E$ 上绝对且一致收敛。连续函数的一致极限连续；由于 $\left\lvert\int_\gamma g\,\mathrm{d}z\right\rvert \le L(\gamma)\sup_\gamma\lvert g\rvert$，一致收敛的连续函数项级数可以沿任何分段光滑曲线 $\gamma \subseteq E$ 逐项积分。

对解析函数，结论要强得多。自然的收敛方式是**内闭一致收敛**（在区域的每个紧子集上一致收敛，等价地，在区域所含的每个闭圆盘上一致收敛），而且它在求导下保持，不需要任何附加条件。

**定理 5.1.2（Weierstrass 定理）** 设 $f_n$ 在区域 $D$ 上解析，$\sum f_n$ 在 $D$ 上内闭一致收敛于 $f$。则 $f$ 在 $D$ 上解析，且对每个 $k \ge 1$，逐项求导所得的级数 $\sum f_n^{(k)}$ 在 $D$ 上内闭一致收敛于 $f^{(k)}$。

**证明** 设 $\overline{D(z_0, r)} \subseteq D$。在这个闭圆盘上 $f$ 是连续函数的一致极限，因而连续。对 $D(z_0, r)$ 中的每个闭三角形 $\Delta$，由逐项积分和 **Cauchy 积分定理**，$\oint_{\partial\Delta} f\,\mathrm{d}z = \sum_n\oint_{\partial\Delta} f_n\,\mathrm{d}z = 0$，所以由 **Morera 定理**，$f$ 在 $D(z_0, r)$ 内解析。对于导数，设 $C$ 为圆周 $\lvert \zeta - z_0\rvert = r$，$\lvert z - z_0\rvert \le r/2$。由导数的 **Cauchy 积分公式**（定理 4.4.2），

$$
\left\lvert f^{(k)}(z) - \sum_{n=1}^N f_n^{(k)}(z)\right\rvert = \left\lvert\frac{k!}{2\pi\mathrm{i}}\oint_C\frac{f(\zeta) - \sum_{n=1}^N f_n(\zeta)}{(\zeta - z)^{k+1}}\,\mathrm{d}\zeta\right\rvert \le \frac{k!\,2^{k+1}}{r^k}\sup_{\zeta\in C}\left\lvert f(\zeta) - \sum_{n=1}^N f_n(\zeta)\right\rvert,
$$

它在 $\lvert z - z_0\rvert \le r/2$ 上一致地趋于 $0$。$D$ 的每个紧子集都能被有限个这样的半径减半的圆盘覆盖。$\square$

与实分析的对比十分鲜明：在 $\mathbb{R}$ 上，由 Weierstrass 逼近定理，多项式的一致极限可以处处不可导；而在 $\mathbb{C}$ 中，解析函数的一致极限自动解析。

## 5.2. 幂级数

### 5.2.1. Abel 定理与收敛半径

**定义 5.2.1** 形如

$$
\sum_{n=0}^\infty c_n(z - z_0)^n = c_0 + c_1(z - z_0) + c_2(z - z_0)^2 + \cdots, \qquad c_n \in \mathbb{C}
$$

的级数称为以 $z_0$ 为中心、以 $c_n$ 为系数的（复）幂级数。

作代换 $w = z - z_0$，可以设 $z_0 = 0$。基本事实与实轴上相同：

**定理 5.2.1（Abel 定理）** 若 $\sum c_nz^n$ 在 $z_1 \ne 0$ 处收敛，则它对每个 $\lvert z\rvert < \lvert z_1\rvert$ 绝对收敛，并在每个闭圆盘 $\lvert z\rvert \le \rho$（$\rho < \lvert z_1\rvert$）上一致收敛。因此，若它在 $z_2$ 处发散，则对每个 $\lvert z\rvert > \lvert z_2\rvert$ 都发散。

**证明** 通项 $c_nz_1^n$ 趋于 $0$，所以 $\lvert c_nz_1^n\rvert \le M$。当 $\lvert z\rvert \le \rho < \lvert z_1\rvert$ 时，$\lvert c_nz^n\rvert \le M(\rho/\lvert z_1\rvert)^n$，这是一个收敛的**几何级数**；由 Weierstrass 判别法即得绝对收敛与一致收敛。$\square$

令 $R = \sup\{\lvert z\rvert : \sum c_nz^n \text{ 收敛}\}$（可以是 $0$ 或 $+\infty$）。由 Abel 定理，级数在开圆盘 $\lvert z\rvert < R$ 内绝对收敛，在 $\lvert z\rvert > R$ 处发散，所以**收敛域**是这个圆盘再加上其边界圆周的某个子集。

**定义 5.2.2** 上面的数 $R \in [0, +\infty]$ 称为幂级数的**收敛半径**；当 $0 < R < \infty$ 时，圆盘 $D(z_0, R)$ 称为它的**收敛圆**，圆周 $\lvert z - z_0\rvert = R$ 称为它的**收敛圆周**。

**定理 5.2.2（Cauchy–Hadamard 公式）** $\sum c_n(z - z_0)^n$ 的收敛半径为

$$
R = \frac{1}{\limsup_{n\to\infty}\sqrt[n]{\lvert c_n\rvert}}, \tag{5.1}
$$

其中约定 $1/0 = +\infty$，$1/\infty = 0$。若 $\lim\lvert c_{n+1}/c_n\rvert = \rho$ 存在，则也有 $R = 1/\rho$。

**证明** 对 $\sum\lvert c_n\rvert\lvert z - z_0\rvert^n$ 应用根值判别法：$\limsup\sqrt[n]{\lvert c_n\rvert\lvert z - z_0\rvert^n} = \lvert z - z_0\rvert/R$，当 $\lvert z - z_0\rvert < R$ 时它 $< 1$（绝对收敛），当 $\lvert z - z_0\rvert > R$ 时它 $> 1$（此时有无穷多项的模 $\ge 1$，通项不趋于 $0$）。比值形式成立，是因为 $\lim\lvert c_{n+1}/c_n\rvert = \rho$ 蕴含 $\lim\sqrt[n]{\lvert c_n\rvert} = \rho$。$\square$

对于缺项级数，相邻系数之比没有定义，这时必须用 $\limsup$ 的形式。

**例 5.2.1** 1. $\sum_{n\ge1}\frac{n^n}{n!}z^{2n}$。级数只含偶次幂：$z^k$ 的系数为 $c_{2n} = \frac{n^n}{n!}$，$c_{2n+1} = 0$。由 Stirling 公式 $\sqrt[n]{n^n/n!} \to \mathrm{e}$，故 $\limsup\sqrt[k]{\lvert c_k\rvert} = \lim\left(\frac{n^n}{n!}\right)^{1/(2n)} = \sqrt{\mathrm{e}}$，$R = \mathrm{e}^{-1/2}$。等价地，令 $w = z^2$：关于 $w$ 的级数收敛半径为 $1/\mathrm{e}$，所以当 $\lvert z\rvert^2 < 1/\mathrm{e}$ 时收敛。
2. $\sum_{n\ge0} 2^{n^2}z^{n^2}$：当 $k = n^2$ 时 $\sqrt[k]{\lvert c_k\rvert} = 2^{n}$，否则为 $0$，所以 $\limsup$ 为 $+\infty$，$R = 0$。
3. $\sum_{n\ge1}(1 - \mathrm{i})^n n^{-2} z^n$：$\sqrt[n]{\lvert c_n\rvert} = \sqrt2\,n^{-2/n} \to \sqrt2$，所以 $R = 1/\sqrt2$。

### 5.2.2. 在收敛圆周上的性态

在收敛圆周上，收敛半径不提供任何信息：级数可能处处绝对收敛，可能处处发散，也可能在不同的点表现不同。

**例 5.2.2** 下面三个级数的收敛半径都是 $R = 1$。

1. $\sum z^n$ 在 $\lvert z\rvert = 1$ 的每一点处发散，因为通项的模为 $1$。
2. $\sum \frac{z^n}{n}$ 在 $z = 1$ 处发散（调和级数），由 Dirichlet 判别法与例 5.1.1，它在圆周上其余每一点 $z = \mathrm{e}^{\mathrm{i}\theta}$ 处条件收敛。
3. 由于 $\sum\frac1{n^2} < \infty$，$\sum \frac{z^n}{n^2}$ 在整个圆周上绝对收敛。

要判断级数在圆周上一点 $z^*$ 处的收敛情况（绝对收敛、条件收敛或发散），先考察 $\sum\lvert c_n\rvert R^n$；若它发散，就把通项写成 $c_n(z^* - z_0)^n = a_n\mathrm{e}^{\mathrm{i}n\theta}$，尝试 Dirichlet 判别法，或者检验通项是否趋于 $0$。

**例 5.2.3** 考虑 $\sum_{n\ge1}\frac{z^{2n}}{\sqrt n\,4^n}$。用变量 $w = z^2/4$，它就是 $\sum w^n/\sqrt n$，在 $\lvert w\rvert < 1$ 时收敛，所以 $R = 2$。在 $\lvert z\rvert = 2$ 上 $w = \mathrm{e}^{\mathrm{i}\theta}$，$\sum\lvert w^n\rvert/\sqrt n = \sum 1/\sqrt n$ 发散，所以在圆周上处处不绝对收敛。

- 在 $z = \sqrt3 + \mathrm{i}$ 处：$z^2 = 2 + 2\sqrt3\,\mathrm{i}$，故 $w = \mathrm{e}^{\mathrm{i}\pi/3} \ne 1$。由于 $1/\sqrt n$ 单调递减趋于 $0$，级数条件收敛。
- 在 $z = 2\mathrm{i}$ 处：$w = -1$，是交错级数，条件收敛。
- 在 $z = \pm2$ 处：$w = 1$，级数 $\sum 1/\sqrt n$ 发散。

**例 5.2.4** 考虑 $\sum_{n\ge1}\frac{1}{\sqrt n}\sin\frac{\mathrm{i}}{n}\,z^n$。由于 $\sin(\mathrm{i}t) = \mathrm{i}\sinh t$，系数为 $c_n = \frac{\mathrm{i}}{\sqrt n}\sinh\frac1n$，$\lvert c_n\rvert \sim n^{-3/2}$。因此 $R = 1$，又因为 $\sum n^{-3/2} < \infty$，级数在 $\lvert z\rvert = 1$ 的每一点处（例如 $z = \mathrm{e}^{\mathrm{i}\pi/4}$）都绝对收敛。

### 5.2.3. 幂级数的和函数解析

**定理 5.2.3** 设 $\sum c_n(z - z_0)^n$ 的收敛半径 $R > 0$，在 $D = D(z_0, R)$ 内的和函数为 $f(z)$。则：

1. $f$ 在 $D$ 内解析，且 $f'(z) = \sum_{n\ge1}nc_n(z - z_0)^{n-1}$，这是一个收敛半径同为 $R$ 的幂级数；
2. $f$ 在 $D$ 内有各阶导数，且 $c_n = \dfrac{f^{(n)}(z_0)}{n!}$；
3. 对 $D$ 内从 $z_0$ 到 $z$ 的每条分段光滑曲线 $\gamma$，$\displaystyle\int_\gamma f(\zeta)\,\mathrm{d}\zeta = \sum_{n\ge0}\frac{c_n}{n+1}(z - z_0)^{n+1}$。

**证明** 由 Abel 定理，级数在每个闭圆盘 $\lvert z - z_0\rvert \le \rho < R$ 上一致收敛，因而在 $D$ 上内闭一致收敛，且每一项都是多项式。由定理 5.1.2 得 1，再由归纳法得到 $f^{(n)}$ 的逐项求导公式；令 $z = z_0$ 即得 2。逐项积分得 3。由于 $\sqrt[n]{n} \to 1$，由式 (5.1)，$\sum nc_n(z - z_0)^{n-1}$ 的收敛半径为 $R$。$\square$

特别地，幂级数的系数由其和函数决定：若两个中心相同的幂级数在中心周围的一个圆盘上相等，则它们完全相同。逐项求导与逐项积分是求和函数的主要工具。

**例 5.2.5** 1. 当 $\lvert z\rvert < 1$ 时，对 $\sum_{n\ge0}z^n = \frac1{1-z}$ 两次应用算子 $z\frac{\mathrm{d}}{\mathrm{d}z}$，得

$$
\sum_{n\ge1}nz^n = \frac{z}{(1-z)^2}, \qquad \sum_{n\ge1}n^2z^n = z\frac{\mathrm{d}}{\mathrm{d}z}\frac{z}{(1-z)^2} = \frac{z(1+z)}{(1-z)^3}.
$$

2. 对一切 $z \in \mathbb{C}$（$R = \infty$），$\sum_{n\ge0}\frac{n+1}{n!}z^n = \sum_{n\ge1}\frac{z^n}{(n-1)!} + \sum_{n\ge0}\frac{z^n}{n!} = (z + 1)\mathrm{e}^z$。

## 5.3. Taylor 级数

### 5.3.1. Taylor 定理

**定理 5.3.1（Taylor 定理）** 设 $f$ 在区域 $D$ 内解析，$z_0 \in D$，$d$ 是 $z_0$ 到 $D$ 的边界的距离（$D = \mathbb{C}$ 时 $d = +\infty$）。则对每个满足 $\lvert z - z_0\rvert < d$ 的 $z$，

$$
f(z) = \sum_{n=0}^\infty c_n(z - z_0)^n, \qquad c_n = \frac{f^{(n)}(z_0)}{n!} = \frac{1}{2\pi\mathrm{i}}\oint_{\lvert\zeta - z_0\rvert = r}\frac{f(\zeta)}{(\zeta - z_0)^{n+1}}\,\mathrm{d}\zeta \quad (0 < r < d), \tag{5.2}
$$

且这一展开式是唯一的。

**证明** 固定满足 $\lvert z - z_0\rvert < d$ 的 $z$，取 $r$ 使 $\lvert z - z_0\rvert < r < d$，设 $C$ 为正向圆周 $\lvert\zeta - z_0\rvert = r$。对 $\zeta \in C$，$q = \lvert z - z_0\rvert/r < 1$，所以

$$
\frac{1}{\zeta - z} = \frac{1}{(\zeta - z_0) - (z - z_0)} = \frac{1}{\zeta - z_0}\cdot\frac{1}{1 - \frac{z - z_0}{\zeta - z_0}} = \sum_{n=0}^\infty\frac{(z - z_0)^n}{(\zeta - z_0)^{n+1}},
$$

第 $n$ 项的模不超过 $q^n/r$，所以级数关于 $\zeta \in C$ 一致收敛。乘以在 $C$ 上有界的 $f(\zeta)/(2\pi\mathrm{i})$ 并逐项积分。由 Cauchy 积分公式，左边成为 $f(z)$，右边成为 $\sum c_n(z - z_0)^n$，其中 $c_n$ 由式 (5.2) 中的积分给出，由高阶导数公式它等于 $f^{(n)}(z_0)/n!$。唯一性由定理 5.2.3 得到。$\square$

式 (5.2) 中的幂级数称为 $f$ 在 $z_0$ 处的 **Taylor 级数**（$z_0 = 0$ 时称为 **Maclaurin 级数**）。结合定理 5.2.3 与定理 5.3.1：

**推论 5.3.1** 函数在 $z_0$ 处解析，当且仅当它在某个圆盘 $D(z_0, r)$ 内是一个收敛幂级数的和。$f$ 在 $z_0$ 处的 Taylor 级数在含于 $f$ 的解析区域内、以 $z_0$ 为圆心的最大开圆盘中收敛于 $f$。

这是与实分析的决定性区别。在 $\mathbb{R}$ 上，$x \ne 0$ 时等于 $\mathrm{e}^{-1/x^2}$、在 $0$ 处等于 $0$ 的函数在 $0$ 处各阶导数都为 $0$，所以它的 Taylor 级数恒为零，不能表示这个函数。在 $\mathbb{C}$ 中这个函数在 $0$ 处甚至不连续：沿虚轴，$\mathrm{e}^{-1/(\mathrm{i}y)^2} = \mathrm{e}^{1/y^2} \to \infty$。

### 5.3.2. 收敛半径与奇点

推论 5.3.1 说明 $R \ge d$。反过来，收敛半径也不能超出函数所允许的范围：

**定理 5.3.2** 设 $f$ 在 $\mathbb{C}$ 上除有限个点 $a_1, \dots, a_m$ 外处处解析，且对每个 $j$，当 $z \to a_j$ 时 $\lvert f(z)\rvert \to \infty$。则 $f$ 在任一点 $z_0 \ne a_j$ 处的 Taylor 级数的收敛半径等于 $\min_j\lvert z_0 - a_j\rvert$。

**证明** 令 $d = \min_j\lvert z_0 - a_j\rvert$；由定理 5.3.1，$R \ge d$。假设 $R > d$，设 $g$ 是级数在 $D(z_0, R)$ 内的和函数，$a_j$ 是满足 $\lvert z_0 - a_j\rvert = d$ 的点。$f$ 与 $g$ 在 $D(z_0, d)$ 上相等，而 $D(z_0, R)$ 去掉有限个点 $a_k$ 后仍连通，所以由唯一性定理（下面的定理 5.4.3），$f = g$ 在其上成立。但 $g$ 在 $a_j$ 处连续，而 $\lvert f\rvert \to \infty$，矛盾。$\square$

这就解释了 [2.2.9](/2.2.9) 中的例子：$\frac{1}{1+x^2} = \sum(-1)^nx^{2n}$ 的收敛半径为 $1$，尽管这个函数在整个实轴上光滑，原因是 $\frac{1}{1+z^2}$ 在到原点距离为 $1$ 的点 $z = \pm\mathrm{i}$ 处趋于无穷。同样，$\tan z$ 的 Maclaurin 级数的收敛半径为 $\frac{\pi}{2}$（$\cos z$ 的零点 $\pm\frac\pi2$），$\frac{z}{\mathrm{e}^z - 1}$ 的为 $2\pi$（分母的零点 $\pm2\pi\mathrm{i}$；$z = 0$ 无碍，因为商在该处趋于 $1$）。

![1/(1 - z) 与 1/(1 + z^2) 在中心 0 处取 30 项的 Taylor 部分和的误差。两种情形下部分和都恰在单位圆盘（虚线）内收敛，其半径等于到最近奇点（红色叉号）的距离；对 1/(1 + z^2)，奇点 ±i 不在实轴上](./plots/taylor-convergence.py)

### 5.3.3. 常用展开式与间接展开法

由式 (5.2)，或由相应的实展开式结合定理 5.4.3，得到以下展开式：

| 函数 | Maclaurin 级数 | 范围 |
|---|---|---|
| $\mathrm{e}^z$ | $\sum_{n\ge0}\dfrac{z^n}{n!}$ | $\mathbb{C}$ |
| $\sin z$，$\cos z$ | $\sum_{n\ge0}\dfrac{(-1)^nz^{2n+1}}{(2n+1)!}$，$\ \sum_{n\ge0}\dfrac{(-1)^nz^{2n}}{(2n)!}$ | $\mathbb{C}$ |
| $\sinh z$，$\cosh z$ | $\sum_{n\ge0}\dfrac{z^{2n+1}}{(2n+1)!}$，$\ \sum_{n\ge0}\dfrac{z^{2n}}{(2n)!}$ | $\mathbb{C}$ |
| $\dfrac{1}{1-z}$ | $\sum_{n\ge0}z^n$ | $\lvert z\rvert < 1$ |
| $\operatorname{Log}(1+z)$ | $\sum_{n\ge1}\dfrac{(-1)^{n-1}}{n}z^n$ | $\lvert z\rvert < 1$ |
| $(1+z)^\alpha = \mathrm{e}^{\alpha\operatorname{Log}(1+z)}$ | $\sum_{n\ge0}\dbinom{\alpha}{n}z^n$ | $\lvert z\rvert < 1$ |

这里 $\operatorname{Log}$ 是主值支（[2.3.3](/2.3.3)），由于 $1 + z$ 总在右半平面内，它在 $\lvert z\rvert < 1$ 内解析；最后一行是复的**二项式级数**。实际计算中很少直接求 $f^{(n)}(z_0)$。由唯一性，任何得到收敛幂级数的方法给出的都是 Taylor 级数：代换、逐项求导与逐项积分、乘法（Cauchy 乘积）、除以常数项不为零的级数，以及部分分式。

**例 5.3.1** 设 $f(z) = \operatorname{Log}(1 + z^4)$，求 $f^{(2024)}(0)$ 与 $f^{(2025)}(0)$。

把 $z^4$ 代入对数的级数，当 $\lvert z\rvert < 1$ 时

$$
\operatorname{Log}(1 + z^4) = \sum_{k\ge1}\frac{(-1)^{k-1}}{k}z^{4k}.
$$

$z^{2024} = z^{4\cdot506}$ 的系数为 $\frac{(-1)^{505}}{506} = -\frac1{506}$，所以 $f^{(2024)}(0) = -\frac{2024!}{506} = -4\cdot2023!$。由于 $2025$ 不是 $4$ 的倍数，$f^{(2025)}(0) = 0$。

**例 5.3.2** 1. 当 $\lvert z\rvert < 1$ 时求 $\frac{\mathrm{e}^z}{1-z}$ 的展开式：$\sum z^n/n!$ 与 $\sum z^n$ 的 Cauchy 乘积为 $\sum_{n\ge0}\left(\sum_{k=0}^n\frac1{k!}\right)z^n = 1 + 2z + \frac52z^2 + \frac83z^3 + \cdots$。
2. $\tan z = \frac{\sin z}{\cos z}$：设 $\tan z = a_1z + a_3z^3 + a_5z^5 + \cdots$（奇函数），在 $\left(z - \frac{z^3}{6} + \frac{z^5}{120} - \cdots\right) = \left(1 - \frac{z^2}{2} + \frac{z^4}{24} - \cdots\right)(a_1z + a_3z^3 + a_5z^5 + \cdots)$ 中比较系数，得 $a_1 = 1$，$a_3 = \frac13$，$a_5 = \frac2{15}$。级数在 $\lvert z\rvert < \frac\pi2$ 时收敛。
3. 当 $\lvert z\rvert < 1$ 时，$\frac{1}{(1-z)^2} = \frac{\mathrm{d}}{\mathrm{d}z}\frac1{1-z} = \sum_{n\ge0}(n+1)z^n$。

## 5.4. 零点与唯一性定理

### 5.4.1. 零点的阶

**定义 5.4.1** 设 $f$ 在 $z_0$ 处解析，在 $z_0$ 附近不恒为零，且 $f(z_0) = 0$。若

$$
f(z_0) = f'(z_0) = \cdots = f^{(m-1)}(z_0) = 0, \qquad f^{(m)}(z_0) \ne 0,
$$
则称 $z_0$ 为 $f$ 的 $m$ 阶零点，$m$ 称为**零点的阶**；一阶零点称为**单零点**。

这样的 $m$ 总是存在：若 $f$ 的各阶导数在 $z_0$ 处都为零，则 Taylor 级数为零，$f$ 在 $z_0$ 附近恒为零。

**定理 5.4.1** $z_0$ 是 $f$ 的 $m$ 阶零点，当且仅当在 $z_0$ 附近 $f(z) = (z - z_0)^m\varphi(z)$，其中 $\varphi$ 在 $z_0$ 处解析且 $\varphi(z_0) \ne 0$。

**证明** 由 Taylor 定理，$f(z) = \sum_{n\ge m}c_n(z - z_0)^n = (z - z_0)^m\sum_{k\ge0}c_{m+k}(z - z_0)^k$，且 $\varphi(z_0) = c_m = f^{(m)}(z_0)/m! \ne 0$。对乘积求导即得逆命题。$\square$

例如，$z = 0$ 是 $z - \sin z = \frac{z^3}{6} - \frac{z^5}{120} + \cdots$ 的 $3$ 阶零点；由于 $\cos k\pi \ne 0$，每个 $z = k\pi$ 都是 $\sin z$ 的单零点。相乘时阶数相加：若 $z_0$ 是 $f$ 的 $m$ 阶零点、$g$ 的 $k$ 阶零点，则它是 $fg$ 的 $m + k$ 阶零点。

### 5.4.2. 零点的孤立性与唯一性定理

**定理 5.4.2** 设 $f$ 在区域 $D$ 上解析且不恒为零。则 $f$ 的零点是孤立的：每个零点 $z_0$ 都有一个不含零点的去心邻域 $0 < \lvert z - z_0\rvert < \delta$。

**证明** 设 $E$ 是 $D$ 中使 $f$ 的各阶导数（包括 $f$ 本身）都为零的点组成的集合。由各阶导数的连续性，$E$ 是 $D$ 中的闭集。$E$ 也是开集：若 $z_1 \in E$，则 $f$ 在 $z_1$ 处的 Taylor 级数为零，所以 $f$ 在 $z_1$ 周围的一个圆盘上恒为零，这个圆盘含于 $E$。由于 $D$ 连通且 $f \not\equiv 0$，$E = \varnothing$。所以每个零点 $z_0$ 都有有限的阶 $m$，由定理 5.4.1，$f(z) = (z - z_0)^m\varphi(z)$，$\varphi$ 连续且 $\varphi(z_0) \ne 0$；因此 $\varphi$ 在 $z_0$ 周围的一个圆盘上不为零，$f$ 在该圆盘上除 $z_0$ 外不为零。$\square$

**定理 5.4.3（唯一性定理）** 设 $f$ 与 $g$ 在区域 $D$ 上解析，且在一个在 $D$ 中有极限点的集合 $E \subseteq D$ 上 $f = g$（例如一列点 $z_n \to z^* \in D$，$z_n \ne z^*$，或者一段曲线弧）。则在 $D$ 上 $f \equiv g$。

**证明** 对 $f - g$ 应用定理 5.4.2：由连续性，$z^*$ 是 $f - g$ 的零点，而且不是孤立零点，所以 $f - g \equiv 0$。$\square$

因此区域上的解析函数由它在任意小的圆盘或线段上的值所决定。这有以下几个推论：

- 实的恒等式可以推广到 $\mathbb{C}$：$\sin^2z + \cos^2z - 1$ 是整函数，在 $\mathbb{R}$ 上为零，所以处处为零。同样的论证证明了 [2.3.3](/2.3.3) 中 $\mathrm{e}^z$、$\sin z$、$\cos z$ 的和角公式。
- 若 $D$ 上的解析函数 $f$ 与更大区域 $G \supseteq D$ 上的解析函数 $g$ 在 $D$ 上相等，则 $g$ 是 $f$ 到 $G$ 上的唯一这样的延拓，称为 $f$ 到 $G$ 上的解析延拓（analytic continuation）。例如 $\sum z^n$（$\lvert z\rvert < 1$）解析延拓为 $\mathbb{C}\setminus\{1\}$ 上的 $\frac1{1-z}$。
- 这个定理对光滑实函数不成立：$\mathrm{e}^{-1/x^2}$（在 $0$ 处补充定义为 $0$）与零函数在 $(-\infty, 0]$ 上相等，却并不相同。

**例 5.4.1** 是否存在在 $\mathbb{D}$ 内解析的函数 $f$，使 $f\left(\frac1n\right) = \frac{(-1)^n}{n}$，$n = 2, 3, \dots$？点列 $\frac1{2k}$ 聚集于 $0 \in \mathbb{D}$，且 $f\left(\frac1{2k}\right) = \frac1{2k}$，由唯一性定理 $f(z) = z$。于是 $f\left(\frac1{2k+1}\right) = \frac1{2k+1} \ne -\frac1{2k+1}$，矛盾；所以这样的 $f$ 不存在。另一方面，$f(z) = z^2$ 满足 $f\left(\frac1n\right) = \frac1{n^2}$，而且是 $\mathbb{D}$ 上唯一满足这一条件的解析函数。

**例 5.4.2** 极限点在 $D$ 中这一条件是必不可少的。函数 $\sin\frac{\pi}{z}$ 在 $D = \mathbb{C}\setminus\{0\}$ 上解析，在 $z = \frac1n$ 处为零，但 $\frac1n \to 0 \notin D$，而这个函数并不恒为零。

## 5.5. Laurent 级数

### 5.5.1. 含正负幂次的级数

$\mathrm{e}^{1/z}$ 或 $\frac{1}{z(1-z)}$ 这样的函数在去心圆盘或圆环内解析，但在中心处不解析，所以在那里没有 Taylor 级数。合适的替代是同时含正幂次和负幂次的级数。

**定义 5.5.1** 形如

$$
\sum_{n=-\infty}^{\infty}c_n(z - z_0)^n = \sum_{n=1}^\infty\frac{c_{-n}}{(z - z_0)^n} + \sum_{n=0}^\infty c_n(z - z_0)^n \tag{5.3}
$$
的级数称为以 $z_0$ 为中心的 **Laurent 级数**。若右端两个级数在 $z$ 处都收敛，则称它在 $z$ 处收敛，其和为两者之和。

右端第二个级数是 $z - z_0$ 的幂级数，当 $\lvert z - z_0\rvert < R$ 时收敛，$R = 1/\limsup\sqrt[n]{\lvert c_n\rvert}$。第一个级数是 $w = \frac{1}{z - z_0}$ 的幂级数，收敛半径为 $1/r$，其中 $r = \limsup\sqrt[n]{\lvert c_{-n}\rvert}$；它当 $\lvert z - z_0\rvert > r$ 时收敛。因此：

**定理 5.5.1** 设 $r$ 与 $R$ 如上。若 $r < R$，则式 (5.3) 那样的 Laurent 级数在圆环 $r < \lvert z - z_0\rvert < R$ 内绝对收敛，在每个闭子圆环 $r < \rho_1 \le \lvert z - z_0\rvert \le \rho_2 < R$ 上一致收敛，其和函数在圆环内解析。它在满足 $\lvert z - z_0\rvert < r$ 或 $\lvert z - z_0\rvert > R$ 的每一点处发散。

**定义 5.5.2** 定理 5.5.1 中的圆环 $r < \lvert z - z_0\rvert < R$ 称为该 Laurent 级数的**收敛圆环**；允许 $r = 0$（去心圆盘）和 $R = +\infty$。

**例 5.5.1** 1. $\sum_{n=-\infty}^{\infty}\frac{z^n}{2^n + 3^n}$。当 $n \ge 0$ 时 $c_n \sim 3^{-n}$，所以 $R = 3$。当 $n = -m < 0$ 时 $c_{-m} = \frac{1}{2^{-m} + 3^{-m}} = \frac{6^m}{2^m + 3^m} \sim 2^m$，所以 $r = 2$。收敛圆环为 $2 < \lvert z\rvert < 3$。
2. $\sum_{n=-\infty}^{\infty}2^{-n^2}z^n$：两个方向上都有 $\sqrt[\lvert n\rvert]{\lvert c_n\rvert} = 2^{-\lvert n\rvert} \to 0$，所以 $r = 0$，$R = \infty$，级数在 $0 < \lvert z\rvert < \infty$ 内收敛。
3. $\sum_{n=-\infty}^{\infty}z^n$：$r = R = 1$，级数处处不收敛。

### 5.5.2. Laurent 定理

定理 5.5.1 的逆命题是本章的主要结果：在圆环内解析的每个函数，在该圆环内都是一个 Laurent 级数的和。

**定理 5.5.2（Laurent 定理）** 设 $f$ 在圆环 $A = \{r < \lvert z - z_0\rvert < R\}$ 内解析，$0 \le r < R \le +\infty$。则对每个 $z \in A$，

$$
f(z) = \sum_{n=-\infty}^{\infty}c_n(z - z_0)^n, \qquad c_n = \frac{1}{2\pi\mathrm{i}}\oint_{\lvert\zeta - z_0\rvert = \rho}\frac{f(\zeta)}{(\zeta - z_0)^{n+1}}\,\mathrm{d}\zeta \quad (n \in \mathbb{Z}), \tag{5.4}
$$

其中 $\rho \in (r, R)$ 任意，圆周取正向。展开式是唯一的：若对某组系数 $a_n$ 在 $A$ 内 $f(z) = \sum a_n(z - z_0)^n$，则 $a_n = c_n$。

**证明** 由两圆周之间区域上的 Cauchy 积分定理，式 (5.4) 中的积分与 $\rho$ 无关。固定 $z \in A$，取 $r < \rho_1 < \lvert z - z_0\rvert < \rho_2 < R$；设 $C_1$ 与 $C_2$ 分别是半径为 $\rho_1$ 与 $\rho_2$ 的正向圆周。由两者之间圆环上的 Cauchy 积分公式（[2.3.4](/2.3.4)），

$$
f(z) = \frac{1}{2\pi\mathrm{i}}\oint_{C_2}\frac{f(\zeta)}{\zeta - z}\,\mathrm{d}\zeta - \frac{1}{2\pi\mathrm{i}}\oint_{C_1}\frac{f(\zeta)}{\zeta - z}\,\mathrm{d}\zeta.
$$

在 $C_2$ 上 $\lvert z - z_0\rvert < \lvert\zeta - z_0\rvert$，与 Taylor 定理的证明完全一样，第一个积分等于 $\sum_{n\ge0}c_n(z - z_0)^n$。在 $C_1$ 上 $\lvert\zeta - z_0\rvert < \lvert z - z_0\rvert$，我们按另一个方向展开：

$$
-\frac{1}{\zeta - z} = \frac{1}{(z - z_0) - (\zeta - z_0)} = \sum_{k=0}^\infty\frac{(\zeta - z_0)^k}{(z - z_0)^{k+1}},
$$

它关于 $\zeta \in C_1$ 一致收敛。逐项积分，第二个积分（连同它前面的负号）成为 $\sum_{k\ge0}(z - z_0)^{-k-1}\frac{1}{2\pi\mathrm{i}}\oint_{C_1}f(\zeta)(\zeta - z_0)^k\,\mathrm{d}\zeta = \sum_{n\ge1}c_{-n}(z - z_0)^{-n}$。

关于唯一性：级数 $\sum a_n(z - z_0)^n$ 在圆周 $\lvert z - z_0\rvert = \rho$ 上一致收敛（定理 5.5.1）。乘以 $(z - z_0)^{-k-1}$ 并逐项积分；由于 $\oint(z - z_0)^{n-k-1}\,\mathrm{d}z$ 当 $n = k$ 时等于 $2\pi\mathrm{i}$，否则等于 $0$，得 $2\pi\mathrm{i}\,c_k = 2\pi\mathrm{i}\,a_k$。$\square$

几点说明：

- Taylor 定理是 $f$ 在整个圆盘 $\lvert z - z_0\rvert < R$ 内解析的特殊情形：此时对 $n \le -1$，$f(\zeta)(\zeta - z_0)^{-n-1}$ 在圆周内部解析，所以 $n < 0$ 时 $c_n = 0$。一般地 $c_n \ne f^{(n)}(z_0)/n!$，因为 $f$ 在 $z_0$ 处甚至可以没有定义。
- 同一个函数以同一点为中心可以有几个不同的 Laurent 展开式，每个解析圆环对应一个；唯一性只在每个圆环内成立。
- 当 $n = -1$ 时，式 (5.4) 给出 $\oint_{\lvert\zeta - z_0\rvert = \rho}f(\zeta)\,\mathrm{d}\zeta = 2\pi\mathrm{i}\,c_{-1}$。把这个公式从右往左读，即由一个 Laurent 系数算出围道积分，就是 [2.3.6](/2.3.6) 中留数定理的思想。

### 5.5.3. Laurent 展开式的计算

式 (5.4) 中的积分很少直接计算。由唯一性，在正确的圆环内收敛的任何展开式都是 Laurent 级数。主要工具是部分分式、如下形式的几何级数

$$
\frac{1}{z - a} = \begin{cases}-\displaystyle\sum_{n\ge0}\frac{z^n}{a^{n+1}}, & \lvert z\rvert < \lvert a\rvert,\\[2ex] \displaystyle\sum_{n\ge1}\frac{a^{n-1}}{z^n}, & \lvert z\rvert > \lvert a\rvert,\end{cases}
$$

以及代入已知的 Taylor 级数。

**例 5.5.2** 把 $f(z) = \frac{1}{(z-1)(z-2)} = \frac{1}{z-2} - \frac{1}{z-1}$ 在以 $0$ 或 $1$ 为中心、$f$ 在其中解析的每个圆环内展开。

以 $0$ 为中心时，极点 $1$ 与 $2$ 把平面分成三个区域。

1. $\lvert z\rvert < 1$（Taylor 级数）：$f(z) = -\sum\frac{z^n}{2^{n+1}} + \sum z^n = \sum_{n\ge0}\left(1 - \frac1{2^{n+1}}\right)z^n$。
2. $1 < \lvert z\rvert < 2$：这里 $\frac1{z-2}$ 按正幂次展开，$\frac1{z-1}$ 按负幂次展开：

$$
f(z) = -\sum_{n\ge0}\frac{z^n}{2^{n+1}} - \sum_{n\ge1}\frac{1}{z^n}.
$$

3. $\lvert z\rvert > 2$：$f(z) = \sum_{n\ge1}\frac{2^{n-1} - 1}{z^n} = \sum_{n\ge2}\frac{2^{n-1} - 1}{z^n} = \frac1{z^2} + \frac3{z^3} + \frac7{z^4} + \cdots$。

以 $1$ 为中心时，令 $w = z - 1$，则 $f = \frac{1}{w(w-1)}$。

4. $0 < \lvert z - 1\rvert < 1$：$f = -\frac1w\cdot\frac1{1-w} = -\frac{1}{z-1} - \sum_{n\ge0}(z-1)^n$。
5. $\lvert z - 1\rvert > 1$：$f = \frac1{w^2}\cdot\frac{1}{1 - 1/w} = \sum_{n\ge2}\frac{1}{(z-1)^n}$。

在区域 4 中 $(z-1)^{-1}$ 的系数为 $-1$，所以 $\oint_{\lvert z-1\rvert = 1/2}f\,\mathrm{d}z = -2\pi\mathrm{i}$；在区域 3 和 5 中该系数为 $0$，所以 $f$ 沿任何包围两个极点的圆周的积分为零。

![左：f(z) = 1/((z - 1)(z - 2)) 以 0 为中心有 Laurent 展开式的三个区域 |z| < 1、1 < |z| < 2 与 |z| > 2。右：以 1 为中心的两个区域 0 < |z - 1| < 1 与 |z - 1| > 1。各圆环的边界都经过极点](./plots/laurent-annuli.py)

**例 5.5.3** 1. 在 $0 < \lvert z\rvert < \infty$ 内，$\mathrm{e}^{1/z} = \sum_{n\ge0}\frac{1}{n!\,z^n} = 1 + \frac1z + \frac{1}{2z^2} + \cdots$：有无穷多个负幂次项。
2. 在 $0 < \lvert z\rvert < \infty$ 内，$\frac{\sin z}{z^3} = \frac{1}{z^2} - \frac16 + \frac{z^2}{120} - \cdots$：只有有限个负幂次项。
3. 在 $\lvert z\rvert > \frac{1}{\sqrt2}$ 内展开 $\frac{1}{(1 + 2z^2)^2}$。把它写成 $\frac{1}{4z^4}\left(1 + \frac{1}{2z^2}\right)^{-2}$，并对 $u = \frac{1}{2z^2}$ 利用 $(1+u)^{-2} = \sum_{k\ge0}(-1)^k(k+1)u^k$（$\lvert u\rvert < 1$）：

$$
\frac{1}{(1 + 2z^2)^2} = \sum_{k\ge0}\frac{(-1)^k(k+1)}{2^{k+2}}\,z^{-2k-4} = \frac{1}{4z^4} - \frac{1}{4z^6} + \frac{3}{16z^8} - \cdots.
$$

在 $\lvert z\rvert < \frac1{\sqrt2}$ 内，同一个函数的 Taylor 级数为 $\sum_{k\ge0}(-1)^k(k+1)2^kz^{2k}$。

**例 5.5.4** 设 $f(z) = z\,\mathrm{e}^{1/(z-1)}$，$0 < \lvert z - 1\rvert < \infty$，求它以 $1$ 为中心的 Laurent 级数的系数 $c_n$。

令 $w = z - 1$，

$$
f = (1 + w)\sum_{k\ge0}\frac{w^{-k}}{k!} = \sum_{k\ge0}\frac{w^{-k}}{k!} + \sum_{k\ge0}\frac{w^{1-k}}{k!}.
$$

合并同次幂：$c_1 = 1$，$c_0 = 1 + 1 = 2$，对 $n \ge 1$，$c_{-n} = \frac1{n!} + \frac1{(n+1)!} = \frac{n+2}{(n+1)!}$；其余系数为零。例如 $c_{-2025} = \frac{2027}{2026!}$，又 $c_{-1} = \frac32$，所以 $\oint_{\lvert z - 1\rvert = 1}z\,\mathrm{e}^{1/(z-1)}\,\mathrm{d}z = 3\pi\mathrm{i}$。

## 小结

| 主题 | 要点 |
|---|---|
| 幂级数 | Abel 定理；$R = 1/\limsup\sqrt[n]{\lvert c_n\rvert}$；在 $\lvert z - z_0\rvert = R$ 上先查绝对收敛，再用 Dirichlet 判别法 |
| 幂级数的和函数 | 在圆盘内解析；可逐项求导和逐项积分；$c_n = f^{(n)}(z_0)/n!$ |
| Taylor 定理 | 在 $D(z_0, d)$ 内解析 $\Rightarrow$ Taylor 级数在其中收敛；收敛半径 = 到最近奇点的距离 |
| 零点 | $f = (z - z_0)^m\varphi$，$\varphi(z_0) \ne 0$；零点孤立；唯一性定理 |
| Laurent 级数 | 在圆环 $r < \lvert z - z_0\rvert < R$ 内收敛；在圆环内解析 $\Rightarrow$ Laurent 展开式唯一，系数由式 (5.4) 给出 |
| 计算 | 部分分式，关于 $z/a$ 或 $a/z$ 的几何级数，代换；不要直接求导 |
| 与留数的联系 | $\oint_{\lvert z - z_0\rvert = \rho}f\,\mathrm{d}z = 2\pi\mathrm{i}\,c_{-1}$ |
