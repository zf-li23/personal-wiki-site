---
title: 随机向量函数的分布、次序统计量、p 分位数
---

[3.1.5](/3.1.5) 讨论了一个随机变量的函数 $g(X)$ 的分布：一般方法是先求 $g(X)$ 的分布函数再求导，$g$ 单调或分段单调时可以直接由 $X$ 的密度写出 $g(X)$ 的密度。本章把这两条路推广到随机向量的函数 $g(X_1, \dots, X_n)$。一般方法仍然是"先求分布函数"；特殊情形中最重要的是和的分布（卷积公式），以及多个函数的联合密度（变量替换公式）。作为应用，我们推导统计中三大分布（$\chi^2$、$t$、$F$ 分布）与正态分布的关系，并研究一类特殊的函数——次序统计量，它描述样本中的最小值、最大值等极端值。最后定义一般分布函数的 $p$ 分位数（广义逆），它既是统计推断中临界值的来源，也给出了由均匀随机数生成任意分布随机数的方法。本章用到 [3.1.6](/3.1.6) 的联合密度、边缘密度与独立性判定；统计推断（[3.2](/3.2)）中的抽样分布以本章为基础。

## 7.1. 随机向量函数的分布

设 $\boldsymbol{X} = (X_1, \dots, X_n)$ 的分布已知，$Z = g(\boldsymbol{X})$。刻画 $Z$ 有两条路：

1. 一般方法：由 $\boldsymbol{X}$ 的联合分布求 $F_Z(z) = \mathbb{P}(g(\boldsymbol{X}) \le z)$，即计算 $\boldsymbol{X}$ 落入区域 $\{\boldsymbol{x} \mid g(\boldsymbol{x}) \le z\}$ 的概率，再根据需要求导得密度或作差得分布列。
2. 特殊情形：对和、差、商以及可逆变换，有直接由密度得到密度的公式。

同一问题往往两种方法都可以用，选择计算更简便的一种即可。

### 7.1.1. 一般方法：先求分布函数

**例 7.1.1** 设 $(X, Y)$ 在单位正方形 $(0, 1)^2$ 上均匀分布（由推论 6.3.1，$X, Y$ 独立且都服从 $\mathrm{U}(0, 1)$），求 $Z = Y/X$ 的概率密度。

**解** $\mathbb{P}(Z \le z)$ 是正方形中位于直线 $y = zx$ 下方部分的面积。$0 \le z \le 1$ 时这部分是以 $(0, 0)$、$(1, 0)$、$(1, z)$ 为顶点的三角形；$z > 1$ 时它是正方形去掉以 $(0, 0)$、$(0, 1)$、$(1/z, 1)$ 为顶点的三角形。于是

$$
F_Z(z) = \begin{cases} 0, & z < 0, \\ z/2, & 0 \le z \le 1, \\ 1 - \dfrac{1}{2z}, & z > 1, \end{cases} \qquad f_Z(z) = \begin{cases} 1/2, & 0 < z \le 1, \\ \dfrac{1}{2z^2}, & z > 1, \\ 0, & z \le 0. \end{cases}
$$

**例 7.1.2** 设 $X, Y$ 独立且都服从 $\mathcal{N}(0, 1)$，求 $Z = \sqrt{X^2 + Y^2}$ 的分布。

**解** $(X, Y)$ 的联合密度为 $f(x, y) = \frac{1}{2\pi}\exp\big(-\frac{x^2 + y^2}{2}\big)$。对 $z \ge 0$，用极坐标 $x = r\cos\theta$，$y = r\sin\theta$，

$$
F_Z(z) = \int_{\{x^2 + y^2 \le z^2\}} \frac{1}{2\pi} \exp\Big( -\frac{x^2 + y^2}{2} \Big) \mathrm{d}x\,\mathrm{d}y = \frac{1}{2\pi} \int_0^{2\pi} \mathrm{d}\theta \int_0^z r\mathrm{e}^{-r^2/2}\,\mathrm{d}r = \int_0^z r\mathrm{e}^{-r^2/2}\,\mathrm{d}r.
$$
求导得 $f_Z(z) = z\mathrm{e}^{-z^2/2}$（$z \ge 0$），即 $Z$ 服从 Rayleigh 分布。向原点 $(0, 0)$ 射击时，弹着点 $(X, Y)$ 常用二元正态分布描述，$Z$ 就是弹着点到目标的距离（脱靶量）。

### 7.1.2. 和与差的分布

**定理 7.1.1** 设 $(X, Y)$ 是离散型随机向量，则 $Z = X + Y$ 的分布列为

$$
\mathbb{P}(Z = z) = \sum_x \mathbb{P}(X = x, Y = z - x).
$$
特别地，当 $X, Y$ 独立时，

$$
\mathbb{P}(Z = z) = \sum_x \mathbb{P}(X = x)\,\mathbb{P}(Y = z - x),
$$
即 $Z$ 的分布列是 $X$ 与 $Y$ 的分布列的离散**卷积**。

例如 $X \sim \mathrm{Bin}(n, p)$ 与 $Y \sim \mathrm{Bin}(m, p)$ 独立时，由 Vandermonde 恒等式 $\sum_k \binom{n}{k}\binom{m}{z - k} = \binom{n + m}{z}$ 得 $X + Y \sim \mathrm{Bin}(n + m, p)$（也可以直接解释为 $n + m$ 次独立试验的成功次数）；类似地，$X \sim \mathrm{Poi}(\lambda)$ 与 $Y \sim \mathrm{Poi}(\mu)$ 独立时，由二项式定理得 $X + Y \sim \mathrm{Poi}(\lambda + \mu)$。

**定理 7.1.2（卷积公式）** 设 $(X, Y)$ 有联合密度 $f(x, y)$，则 $Z = X + Y$ 有密度

$$
f_Z(z) = \int_{-\infty}^{\infty} f(x, z - x)\,\mathrm{d}x = \int_{-\infty}^{\infty} f(z - y, y)\,\mathrm{d}y.
$$
特别地，当 $X, Y$ 独立时，

$$
f_Z(z) = \int_{-\infty}^{\infty} f_X(x) f_Y(z - x)\,\mathrm{d}x =: (f_X * f_Y)(z).
$$

**证明** 对任意 $a < b$，由 Fubini 定理和内层积分的换元 $y = z - x$，

$$
\mathbb{P}(a < Z \le b) = \int_{\mathbb{R}^2} \boldsymbol{1}\{a < x + y \le b\} f(x, y)\,\mathrm{d}x\,\mathrm{d}y = \int_{\mathbb{R}} \int_{a - x}^{b - x} f(x, y)\,\mathrm{d}y\,\mathrm{d}x = \int_{\mathbb{R}} \int_a^b f(x, z - x)\,\mathrm{d}z\,\mathrm{d}x = \int_a^b \int_{\mathbb{R}} f(x, z - x)\,\mathrm{d}x\,\mathrm{d}z,
$$
所以 $\int_{\mathbb{R}} f(x, z - x)\,\mathrm{d}x$ 是 $Z$ 的密度。交换 $x, y$ 的地位得第二种形式。 $\square$

**定理 7.1.3** 设 $(X, Y)$ 有联合密度 $f(x, y)$，则 $V = X - Y$ 有密度

$$
f_V(v) = \int_{-\infty}^{\infty} f(x, x - v)\,\mathrm{d}x;
$$
当 $X, Y$ 独立时 $f_V(v) = \int_{-\infty}^{\infty} f_X(x) f_Y(x - v)\,\mathrm{d}x$。

这只需把 $V$ 写成 $X + (-Y)$，对 $(X, -Y)$ 的联合密度 $f(x, -y)$ 应用卷积公式。这种"转化为已有结果"的技巧（减法化为加法，乘法化为除法）在求函数分布时很常用。

**例 7.1.3** 设 $X, Y$ 独立且都服从 $\mathrm{U}(0, 1)$，求 $Z = X + Y$ 的密度。

**解** $Z$ 在 $(0, 2)$ 中取值，$f_X(x) = f_Y(x) = \boldsymbol{1}\{0 < x < 1\}$。由卷积公式，令 $t = z - x$，

$$
f_Z(z) = \int_{-\infty}^{\infty} \boldsymbol{1}\{0 < x < 1\}\boldsymbol{1}\{0 < z - x < 1\}\,\mathrm{d}x = \int_{z-1}^{z} \boldsymbol{1}\{0 < t < 1\}\,\mathrm{d}t = \begin{cases} z, & 0 < z \le 1, \\ 2 - z, & 1 < z < 2, \\ 0, & \text{其他}, \end{cases}
$$
称为三角形分布。两个均匀分布之和不再是均匀分布：中间的值有更多的组合方式得到。

**例 7.1.4** 设 $X_1, X_2, \dots, X_n$ 独立同分布，都服从 $\mathrm{U}(-1, 1)$，记 $S_n = X_1 + \cdots + X_n$。反复应用卷积公式可得

$$
f_{S_2}(x) = \begin{cases} \dfrac{2 - \lvert x \rvert}{4}, & \lvert x \rvert \le 2, \\ 0, & \lvert x \rvert > 2, \end{cases} \qquad f_{S_3}(x) = \begin{cases} \dfrac{3 - x^2}{8}, & \lvert x \rvert \le 1, \\ \dfrac{(3 - \lvert x \rvert)^2}{16}, & 1 \le \lvert x \rvert \le 3, \\ 0, & \lvert x \rvert > 3, \end{cases}
$$
一般地（对 $n$ 用归纳法）

$$
f_{S_n}(x) = \begin{cases} \dfrac{1}{2^n (n - 1)!} \displaystyle\sum_{k=0}^{\lfloor (n + x)/2 \rfloor} (-1)^k \binom{n}{k} (n + x - 2k)^{n-1}, & \lvert x \rvert \le n, \\ 0, & \lvert x \rvert > n. \end{cases}
$$
$f_{S_2}$ 是折线，$f_{S_3}$ 已由三段抛物线光滑连接，随着 $n$ 增大，$f_{S_n}$ 迅速接近正态密度 $\mathcal{N}(0, n/3)$（$n/3$ 是 $S_n$ 的方差，见 [3.1.8](/3.1.8)）。这是**中心极限定理**（[3.1.13](/3.1.13)）的直观表现：许多独立小量的叠加近似服从正态分布。

![U(-1,1) 独立和 S_n 的精确密度（实线）与正态近似 N(0, n/3)（虚线）](./plots/uniform-sums.py)

**例 7.1.5** 设 $X \sim \Gamma(\alpha_1, \lambda)$ 与 $Y \sim \Gamma(\alpha_2, \lambda)$ 独立，则 $X + Y \sim \Gamma(\alpha_1 + \alpha_2, \lambda)$。

**证明** 对 $z > 0$，由卷积公式并令 $x = zt$，

$$
f_{X+Y}(z) = \int_0^z \frac{\lambda^{\alpha_1}}{\Gamma(\alpha_1)} x^{\alpha_1 - 1}\mathrm{e}^{-\lambda x} \cdot \frac{\lambda^{\alpha_2}}{\Gamma(\alpha_2)} (z - x)^{\alpha_2 - 1}\mathrm{e}^{-\lambda(z - x)}\,\mathrm{d}x = \frac{\lambda^{\alpha_1 + \alpha_2}}{\Gamma(\alpha_1)\Gamma(\alpha_2)} z^{\alpha_1 + \alpha_2 - 1}\mathrm{e}^{-\lambda z} \int_0^1 t^{\alpha_1 - 1}(1 - t)^{\alpha_2 - 1}\,\mathrm{d}t.
$$
最后的积分是 **Beta 函数** $\mathrm{B}(\alpha_1, \alpha_2) = \frac{\Gamma(\alpha_1)\Gamma(\alpha_2)}{\Gamma(\alpha_1 + \alpha_2)}$，代入即得 $\Gamma(\alpha_1 + \alpha_2, \lambda)$ 的密度。 $\square$

特别地，$n$ 个独立的 $\mathrm{Exp}(\lambda) = \Gamma(1, \lambda)$ 之和服从 $\Gamma(n, \lambda)$。

**例 7.1.6** 设 $(X, Y)$ 有联合密度 $f(x, y)$，则 $Z = X/Y$ 有密度 $f_Z(z) = \int_{-\infty}^{\infty} \lvert y \rvert f(zy, y)\,\mathrm{d}y$。特别地，$X, Y$ 独立且都服从 $\mathcal{N}(0, 1)$ 时，$Z$ 服从 Cauchy 分布。

**解** $\mathbb{P}(Y = 0) = 0$。按 $Y$ 的符号分解（全概率公式），

$$
F_Z(z) = \mathbb{P}(X \le zY, Y > 0) + \mathbb{P}(X \ge zY, Y < 0) = \int_0^{\infty} \int_{-\infty}^{zy} f(x, y)\,\mathrm{d}x\,\mathrm{d}y + \int_{-\infty}^{0} \int_{zy}^{\infty} f(x, y)\,\mathrm{d}x\,\mathrm{d}y.
$$
对 $z$ 求导得 $f_Z(z) = \int_0^{\infty} y f(zy, y)\,\mathrm{d}y - \int_{-\infty}^0 y f(zy, y)\,\mathrm{d}y = \int_{\mathbb{R}} \lvert y \rvert f(zy, y)\,\mathrm{d}y$。代入标准正态密度，

$$
f_Z(z) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \lvert y \rvert \mathrm{e}^{-(1 + z^2)y^2/2}\,\mathrm{d}y = \frac{1}{\pi} \int_0^{\infty} y\mathrm{e}^{-(1 + z^2)y^2/2}\,\mathrm{d}y = \frac{1}{\pi(1 + z^2)}, \quad z \in \mathbb{R}.
$$

### 7.1.3. 多个函数的联合密度

设 $\boldsymbol{X} = (X_1, \dots, X_n)$ 有联合密度 $f(\boldsymbol{x})$，$Y_1 = g_1(\boldsymbol{X}), \dots, Y_n = g_n(\boldsymbol{X})$ 是 $n$ 个函数，求 $\boldsymbol{Y} = (Y_1, \dots, Y_n)$ 的联合密度。回忆一元的结论（[3.1.5](/3.1.5)）：若 $\mathbb{P}(Y \in D) = 1$，对 $y \in D$ 有 $\{Y = y\} = \bigcup_{i=1}^n \{X = h_i(y)\}$，每个 $h_i$ 是 $D$ 到其值域 $D_i$ 的可逆映射且连续可导，$D_1, \dots, D_n$ 互不相交，则 $f_Y(y) = \sum_{i=1}^n f(h_i(y))\lvert h_i'(y) \rvert$（$y \in D$）。二维情形完全类似，导数换成 **Jacobi 行列式**。

**定理 7.1.4** 设 $(X, Y)$ 有联合密度 $f(x, y)$，$U = u(X, Y)$，$V = v(X, Y)$，$D$ 是平面上的区域，$\mathbb{P}((U, V) \in D) = 1$。如果存在 $D$ 上的函数 $x_i = x_i(u, v)$，$y_i = y_i(u, v)$（$i = 1, \dots, n$），使得

1. 对 $(u, v) \in D$，有 $\{U = u, V = v\} = \bigcup_{i=1}^n \{X = x_i(u, v), Y = y_i(u, v)\}$；
2. $\Delta_i\colon (u, v) \mapsto (x_i(u, v), y_i(u, v))$ 是 $D$ 到其值域 $D_i$ 的可逆映射，有连续的偏导数，并且 Jacobi 行列式 $J_i(u, v) = \dfrac{\partial(x_i, y_i)}{\partial(u, v)} \ne 0$，$(u, v) \in D$；
3. $D_1, \dots, D_n$ 互不相交，

则 $(U, V)$ 有联合密度

$$
g(u, v) = \begin{cases} \displaystyle\sum_{i=1}^n f\big(x_i(u, v), y_i(u, v)\big) \lvert J_i(u, v) \rvert, & (u, v) \in D, \\ 0, & (u, v) \notin D. \end{cases}
$$

其中

$$
\frac{\partial(x, y)}{\partial(u, v)} = \det\begin{bmatrix} \dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\[2mm] \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v} \end{bmatrix}.
$$
矩阵按行排 $x, y$、按列排 $u, v$（分子布局），或者取其转置（分母布局），行列式相同，因此公式与布局约定无关。实际计算时，若从 $(x, y)$ 解出 $(u, v)$ 较方便，可以利用 $\dfrac{\partial(x, y)}{\partial(u, v)} = \Big(\dfrac{\partial(u, v)}{\partial(x, y)}\Big)^{-1}$。定理可以直接推广到 $n$ 维。证明的思路是重积分的变量替换：对 $D$ 中的区域 $B$，$\mathbb{P}((U, V) \in B) = \sum_i \mathbb{P}((X, Y) \in \Delta_i(B)) = \sum_i \int_{\Delta_i(B)} f\,\mathrm{d}x\,\mathrm{d}y = \int_B \sum_i f(x_i, y_i)\lvert J_i \rvert\,\mathrm{d}u\,\mathrm{d}v$。

**例 7.1.7** 设 $X, Y$ 独立且都服从 $\mathcal{N}(0, 1)$，$(R, \Theta)$ 由极坐标变换 $X = R\cos\Theta$，$Y = R\sin\Theta$ 决定，求 $(R, \Theta)$ 的联合密度。

**解** 令 $D = \{(r, \theta) \mid r > 0, \theta \in [0, 2\pi)\}$，则 $\mathbb{P}((R, \Theta) \in D) = 1$。$x = r\cos\theta$，$y = r\sin\theta$ 是 $D$ 到 $D_1 = \mathbb{R}^2 \setminus \{(0, 0)\}$ 的可逆变换，$\{R = r, \Theta = \theta\} = \{X = x, Y = y\}$，$\frac{\partial(x, y)}{\partial(r, \theta)} = r > 0$。由定理 7.1.4，

$$
g(r, \theta) = f(r\cos\theta, r\sin\theta) \cdot r = \frac{1}{2\pi} \cdot r\mathrm{e}^{-r^2/2}, \quad (r, \theta) \in D.
$$
由推论 6.3.1，$R$ 与 $\Theta$ 独立，分别有密度 $g_R(r) = r\mathrm{e}^{-r^2/2}$（$r > 0$）与 $g_\Theta(\theta) = \frac{1}{2\pi}\boldsymbol{1}_{[0, 2\pi)}(\theta)$：$R$ 服从 Rayleigh 分布（与例 7.1.2 一致），$\Theta \sim \mathrm{U}(0, 2\pi)$。

**定理 7.1.5** 设 $n$ 维随机向量 $\boldsymbol{X}$ 与 $\boldsymbol{Y}$ 有相同的分布，$\boldsymbol{g}\colon \mathbb{R}^n \to \mathbb{R}^m$ 是可测函数，则 $\boldsymbol{g}(\boldsymbol{X})$ 与 $\boldsymbol{g}(\boldsymbol{Y})$ 有相同的分布。

这是因为 $\mathbb{P}(\boldsymbol{g}(\boldsymbol{X}) \in B) = \mathbb{P}(\boldsymbol{X} \in \boldsymbol{g}^{-1}(B)) = \mathbb{P}(\boldsymbol{Y} \in \boldsymbol{g}^{-1}(B)) = \mathbb{P}(\boldsymbol{g}(\boldsymbol{Y}) \in B)$。

**例 7.1.8（Box–Muller 方法）** 设 $U, V$ 独立且都服从 $\mathrm{U}(0, 1)$，令

$$
X = \sqrt{-2\ln U}\cos(2\pi V), \qquad Y = \sqrt{-2\ln U}\sin(2\pi V),
$$
则 $X, Y$ 独立且都服从 $\mathcal{N}(0, 1)$。

**证明** $R' = \sqrt{-2\ln U}$ 满足 $\mathbb{P}(R' > r) = \mathbb{P}(U < \mathrm{e}^{-r^2/2}) = \mathrm{e}^{-r^2/2}$，即服从 Rayleigh 分布；$\Theta' = 2\pi V \sim \mathrm{U}(0, 2\pi)$，且 $R'$ 与 $\Theta'$ 独立。由例 7.1.7，$(R', \Theta')$ 与 $(R, \Theta)$ 同分布，由定理 7.1.5，$(R'\cos\Theta', R'\sin\Theta')$ 与 $(R\cos\Theta, R\sin\Theta) = (X_0, Y_0)$（两个独立标准正态变量）同分布。 $\square$

这给出了由均匀随机数生成正态随机数的方法。

**例 7.1.9** 设 $X, Y$ 独立且都服从 $\mathcal{N}(0, 1)$，求 $U = X/Y$ 与 $V = X^2 + Y^2$ 的联合密度。

**解** $D = \{(u, v) \mid u \in \mathbb{R}, v > 0\}$。由 $u = x/y$，$v = x^2 + y^2$ 解出两组逆变换 $y = \pm\sqrt{v/(1 + u^2)}$，$x = uy$，分别把 $D$ 映到上、下半平面。两组的 Jacobi 行列式的绝对值都是 $\frac{1}{2(1 + u^2)}$（可由 $\frac{\partial(u, v)}{\partial(x, y)} = -\frac{2(x^2 + y^2)}{y^2} = -2(1 + u^2)$ 取倒数得到），而 $f(x, y) = \frac{1}{2\pi}\mathrm{e}^{-v/2}$ 在两组逆变换处取值相同。由定理 7.1.4，

$$
g(u, v) = 2 \cdot \frac{1}{2\pi}\mathrm{e}^{-v/2} \cdot \frac{1}{2(1 + u^2)} = \frac{1}{\pi(1 + u^2)} \cdot \frac{1}{2}\mathrm{e}^{-v/2}, \quad u \in \mathbb{R},\ v > 0.
$$
所以 $U, V$ 独立，$U$ 服从 Cauchy 分布（与例 7.1.6 一致），$V \sim \mathrm{Exp}(1/2)$。

### 7.1.4. 三大统计分布

统计推断中最常用的三个分布都由独立正态随机变量构造而来。它们的密度在 [3.1.4](/3.1.4) 中已经给出，这里重述定义并用本章的方法推导它们与正态分布的关系。

**定义 7.1.1（卡方分布）** 设 $\nu > 0$，如果 $X$ 的密度是

$$
f(x) = \frac{1}{2^{\nu/2}\Gamma(\nu/2)} x^{\nu/2 - 1}\mathrm{e}^{-x/2}, \quad x > 0,
$$
称 $X$ 服从自由度为 $\nu$ 的**卡方分布**，记作 $X \sim \chi^2_\nu$。

对比 Gamma 分布的密度可知 $\chi^2_\nu = \Gamma(\nu/2, 1/2)$，特别地 $\chi^2_2 = \mathrm{Exp}(1/2)$。

**定理 7.1.6** 设 $Z_1, \dots, Z_n \overset{\text{iid}}{\sim} \mathcal{N}(0, 1)$，则 $Z_1^2 + \cdots + Z_n^2 \sim \chi^2_n$。更一般地，若 $X \sim \chi^2_m$ 与 $Y \sim \chi^2_n$ 独立，则 $X + Y \sim \chi^2_{m+n}$。

**证明** 先求 $Z_1^2$ 的分布。对 $y > 0$，$\mathbb{P}(Z_1^2 \le y) = \Phi(\sqrt{y}) - \Phi(-\sqrt{y})$，求导得

$$
f_{Z_1^2}(y) = \frac{1}{\sqrt{y}}\varphi(\sqrt{y}) = \frac{1}{\sqrt{2\pi}} y^{-1/2}\mathrm{e}^{-y/2},
$$
这正是 $\chi^2_1 = \Gamma(1/2, 1/2)$ 的密度（$\Gamma(1/2) = \sqrt{\pi}$）。$Z_1^2, \dots, Z_n^2$ 独立，由例 7.1.5 的可加性，和服从 $\Gamma(n/2, 1/2) = \chi^2_n$。第二个结论同样由例 7.1.5 得到。 $\square$

$\chi^2$ 分布由 Karl Pearson 在研究拟合优度检验（$\chi^2$ 检验）时提出。

**定义 7.1.2（t 分布）** 设 $\nu > 0$，如果 $X$ 的密度是

$$
f(x) = \frac{\Gamma\big(\frac{\nu + 1}{2}\big)}{\sqrt{\nu\pi}\,\Gamma\big(\frac{\nu}{2}\big)} \Big(1 + \frac{x^2}{\nu}\Big)^{-\frac{\nu + 1}{2}}, \quad x \in \mathbb{R},
$$
称 $X$ 服从自由度为 $\nu$ 的 Student **t 分布**，记作 $X \sim t_\nu$。

**定理 7.1.7** 设 $Z \sim \mathcal{N}(0, 1)$ 与 $X \sim \chi^2_n$ 独立，则 $T = \dfrac{Z}{\sqrt{X/n}} \sim t_n$。

**证明** 对变换 $t = z/\sqrt{x/n}$，$w = x$（$x > 0$）应用定理 7.1.4，逆变换 $z = t\sqrt{w/n}$，$x = w$ 的 Jacobi 行列式为 $\sqrt{w/n}$。$(T, W)$ 的联合密度为

$$
g(t, w) = \frac{1}{\sqrt{2\pi}}\mathrm{e}^{-t^2 w/(2n)} \cdot \frac{w^{n/2 - 1}\mathrm{e}^{-w/2}}{2^{n/2}\Gamma(n/2)} \cdot \sqrt{\frac{w}{n}}, \quad w > 0.
$$
对 $w$ 积分，被积函数关于 $w$ 是 $\Gamma\big(\frac{n + 1}{2}, \frac{1}{2}(1 + \frac{t^2}{n})\big)$ 密度的核，

$$
f_T(t) = \frac{1}{\sqrt{2\pi n}\,2^{n/2}\Gamma(n/2)} \int_0^{\infty} w^{\frac{n+1}{2} - 1}\mathrm{e}^{-\frac{w}{2}(1 + t^2/n)}\,\mathrm{d}w = \frac{\Gamma\big(\frac{n + 1}{2}\big)}{\sqrt{n\pi}\,\Gamma\big(\frac{n}{2}\big)}\Big(1 + \frac{t^2}{n}\Big)^{-\frac{n + 1}{2}}. \qquad \square
$$

$t$ 分布由 W. S. Gosset 以笔名 Student 提出。它关于 0 对称（$T \sim t_\nu$ 时 $-T \sim t_\nu$），尾部按幂律衰减，比正态分布重尾；$\nu$ 很大时 $t_\nu$ 接近标准正态分布（以后用大数定律证明，[3.1.12](/3.1.12)）；$\nu = 1$ 时 $t_1$ 就是 Cauchy 分布（例 7.1.6）。

**定义 7.1.3（F 分布）** 设 $m, n$ 是正整数，如果 $X$ 的密度是

$$
f(x) = \frac{\Gamma\big(\frac{m + n}{2}\big) m^{m/2} n^{n/2}}{\Gamma\big(\frac{m}{2}\big)\Gamma\big(\frac{n}{2}\big)} \cdot \frac{x^{m/2 - 1}}{(mx + n)^{(m + n)/2}}, \quad x > 0,
$$
称 $X$ 服从自由度为 $(m, n)$ 的 **F 分布**，记作 $X \sim F_{m,n}$。

**定理 7.1.8** 设 $X \sim \chi^2_m$ 与 $Y \sim \chi^2_n$ 独立，则 $F = \dfrac{X/m}{Y/n} \sim F_{m,n}$。特别地，若 $X_1, \dots, X_m, Y_1, \dots, Y_n \overset{\text{iid}}{\sim} \mathcal{N}(0, 1)$，则 $\dfrac{\frac{1}{m}\sum_i X_i^2}{\frac{1}{n}\sum_j Y_j^2} \sim F_{m,n}$。

证明与定理 7.1.7 相同：对 $(F, W) = \big(\frac{X/m}{Y/n}, Y\big)$ 应用定理 7.1.4，再对 $W$ 积分。由定义还可以看出 $F \sim F_{m,n}$ 时 $1/F \sim F_{n,m}$，$T \sim t_n$ 时 $T^2 \sim F_{1,n}$。$F$ 分布由 R. A. Fisher 引入（1924 年），在方差分析与线性回归中有重要应用。三大分布的期望与方差见 [3.1.8](/3.1.8)，它们在正态总体抽样中的作用见统计推断的 [3.2.2](/3.2.2)。

## 7.2. 次序统计量

### 7.2.1. 定义

**定义 7.2.1（次序统计量）** 设 $X_1, X_2, \dots, X_n$ 是概率空间 $(\Omega, \mathcal{F}, \mathbb{P})$ 上的随机变量。对每个 $\omega \in \Omega$，将 $X_1(\omega), \dots, X_n(\omega)$ 从小到大排列得到

$$
X_{(1)}(\omega) \le X_{(2)}(\omega) \le \cdots \le X_{(n)}(\omega),
$$
称 $X_{(1)}, X_{(2)}, \dots, X_{(n)}$ 为 $X_1, \dots, X_n$ 的**次序统计量**。特别地 $X_{(1)} = \min\{X_1, \dots, X_n\}$，$X_{(n)} = \max\{X_1, \dots, X_n\}$。

**例 7.2.1** 某省有 3 位百米运动员，$X_i$ 表示第 $i$ 位运动员的成绩（秒）。设样本空间 $\Omega = \{\omega_1, \omega_2, \omega_3\}$，$\omega_k$ 表示第 $k$ 次训练，$X_{(i)}$ 是第 $i$ 名的成绩：

| 训练 | $X_1$ | $X_2$ | $X_3$ | $X_{(1)}$ | $X_{(2)}$ | $X_{(3)}$ |
|---|---|---|---|---|---|---|
| $\omega_1$ | 11.3 | 11.6 | 11.0 | 11.0 | 11.3 | 11.6 |
| $\omega_2$ | 11.0 | 11.5 | 11.8 | 11.0 | 11.5 | 11.8 |
| $\omega_3$ | 12.0 | 11.9 | 12.2 | 11.9 | 12.0 | 12.2 |

注意 $X_{(1)}$ 在不同的 $\omega$ 下可以来自不同的运动员：次序统计量是 $(X_1, \dots, X_n)$ 的函数，但不是其中某一个固定的分量。

### 7.2.2. 次序统计量的分布

以下设 $X_1, \dots, X_n$ 独立同分布，有公共的分布函数 $F(x)$ 与密度 $f(x)$。这时 $\mathbb{P}(X_i = X_j) = 0$（$i \ne j$），次序统计量几乎必然严格递增。

**性质 7.2.1** $(X_{(1)}, \dots, X_{(n)})$ 有联合密度

$$
g(x_1, \dots, x_n) = \begin{cases} n!\displaystyle\prod_{i=1}^n f(x_i), & x_1 < x_2 < \cdots < x_n, \\ 0, & \text{其他}. \end{cases}
$$

**证明** 对 $\{1, \dots, n\}$ 的每个排列 $\sigma$，记 $A_\sigma = \{X_{\sigma(1)} < X_{\sigma(2)} < \cdots < X_{\sigma(n)}\}$，这 $n!$ 个事件互不相交且并的概率为 1。在 $A_\sigma$ 上，$(X_{(1)}, \dots, X_{(n)}) = (X_{\sigma(1)}, \dots, X_{\sigma(n)})$。对 $B \subset \{x_1 < \cdots < x_n\}$，

$$
\mathbb{P}((X_{(1)}, \dots, X_{(n)}) \in B) = \sum_\sigma \mathbb{P}((X_{\sigma(1)}, \dots, X_{\sigma(n)}) \in B) = n! \int_B \prod_{i=1}^n f(x_i)\,\mathrm{d}\boldsymbol{x},
$$
因为 $(X_{\sigma(1)}, \dots, X_{\sigma(n)})$ 与 $(X_1, \dots, X_n)$ 有相同的联合密度 $\prod f(x_i)$。 $\square$

为了由联合密度积分求边缘密度，需要下面的积分公式。

**性质 7.2.2** 对 $-\infty \le a < b \le \infty$，有

$$
\int_{a < x_1 < \cdots < x_k < b} f(x_1) \cdots f(x_k)\,\mathrm{d}x_1 \cdots \mathrm{d}x_k = \frac{(F(b) - F(a))^k}{k!}.
$$

**证明** 对 $k$ 用归纳法。$k = 1$ 时结论成立。设结论对 $k - 1$ 成立，由 Fubini 定理，

$$
\int_{a < x_1 < \cdots < x_k < b} \prod_{i=1}^k f(x_i)\,\mathrm{d}\boldsymbol{x} = \int_a^b \Big( \int_{a < x_1 < \cdots < x_{k-1} < x_k} \prod_{i=1}^{k-1} f(x_i)\,\mathrm{d}x_1 \cdots \mathrm{d}x_{k-1} \Big) f(x_k)\,\mathrm{d}x_k = \int_a^b \frac{(F(x_k) - F(a))^{k-1}}{(k - 1)!} f(x_k)\,\mathrm{d}x_k = \frac{(F(b) - F(a))^k}{k!}. \qquad \square
$$

这个公式也可以由对称性理解：$k$ 个独立同分布的点都落在 $(a, b)$ 中的概率是 $(F(b) - F(a))^k$，其中按某一固定顺序排列的情形占 $1/k!$。

**性质 7.2.3** $X_{(k)}$ 有密度

$$
g_k(x) = n\binom{n - 1}{k - 1} [F(x)]^{k-1} [1 - F(x)]^{n-k} f(x).
$$

**证明** 对联合密度 $g$ 关于除 $x_k$ 外的变元积分，并对两侧分别应用性质 7.2.2（左侧 $a = -\infty$，$b = c$；右侧 $a = c$，$b = \infty$），

$$
g_k(c) = n! f(c) \int_{x_1 < \cdots < x_{k-1} < c} \prod_{i<k} f(x_i)\,\mathrm{d}x_1 \cdots \mathrm{d}x_{k-1} \cdot \int_{c < x_{k+1} < \cdots < x_n} \prod_{i>k} f(x_i)\,\mathrm{d}x_{k+1} \cdots \mathrm{d}x_n = n! f(c) \frac{F(c)^{k-1}}{(k - 1)!} \cdot \frac{(1 - F(c))^{n-k}}{(n - k)!},
$$
而 $\frac{n!}{(k-1)!(n-k)!} = n\binom{n-1}{k-1}$。 $\square$

公式也可以用微元法理解：$X_{(k)} \in (x, x + \Delta x]$ 近似等价于 $n$ 个点中恰有 $k - 1$ 个落在 $x$ 左侧、1 个落在 $(x, x + \Delta x]$、$n - k$ 个落在右侧（两个以上的点落入同一小区间的概率是 $o(\Delta x)$，可以忽略），由多项分布，其概率约为 $\frac{n!}{(k-1)!\,1!\,(n-k)!} F(x)^{k-1} \cdot f(x)\Delta x \cdot (1 - F(x))^{n-k}$。

$k = 1$ 与 $k = n$ 时得到最小值与最大值的密度 $g_1(x) = n[1 - F(x)]^{n-1} f(x)$、$g_n(x) = n[F(x)]^{n-1} f(x)$。它们也可以直接由分布函数求得，且不需要密度存在：

$$
\mathbb{P}(X_{(n)} \le x) = \mathbb{P}(X_1 \le x, \dots, X_n \le x) = F(x)^n, \qquad \mathbb{P}(X_{(1)} > x) = [1 - F(x)]^n.
$$

**性质 7.2.4** 对 $k_1 < k_2$，$(X_{(k_1)}, X_{(k_2)})$ 有联合密度：当 $x < y$ 时

$$
g(x, y) = \frac{n!}{(k_1 - 1)!\,(k_2 - k_1 - 1)!\,(n - k_2)!} F(x)^{k_1 - 1}[F(y) - F(x)]^{k_2 - k_1 - 1}[1 - F(y)]^{n - k_2} f(x) f(y),
$$
其余处为 0。

证明与性质 7.2.3 相同：对联合密度在 $x$ 左侧、$x$ 与 $y$ 之间、$y$ 右侧三段分别应用性质 7.2.2；微元法的解释是把实轴分成五段，各段分别有 $k_1 - 1$、1、$k_2 - k_1 - 1$、1、$n - k_2$ 个点。

**性质 7.2.5** $(X_{(1)}, \dots, X_{(n)})$ 的联合分布函数是连续函数。

**证明** 由例 6.3.4，只需证明每个 $X_{(k)}$ 的分布函数连续，即 $\mathbb{P}(X_{(k)} = x) = 0$。事件 $\{X_{(k)} = x\}$ 要求至少一个 $X_j$ 等于 $x$，而 $\mathbb{P}(X_j = x) = 0$，故 $\mathbb{P}(X_{(k)} = x) \le \sum_j \mathbb{P}(X_j = x) = 0$。 $\square$

**例 7.2.2** 某教学楼原来每个教室有 4 只灯泡，装修后每个教室有 24 只灯泡。管理员总觉得装修后灯泡更容易坏了，试解释原因。

**解** 设所有灯泡的寿命相互独立，都服从 $\mathrm{Exp}(\lambda)$。装修前等待第一只灯泡烧坏的时间为 $X = \min\{X_1, \dots, X_4\}$，装修后为 $Y = \min\{X_1, \dots, X_{24}\}$。由 $\mathbb{P}(X_{(1)} > t) = [1 - F(t)]^n = \mathrm{e}^{-n\lambda t}$ 得 $X \sim \mathrm{Exp}(4\lambda)$，$Y \sim \mathrm{Exp}(24\lambda)$，

$$
\mathbb{P}(X > t) = \mathrm{e}^{-4\lambda t}, \qquad \mathbb{P}(Y > t) = \mathrm{e}^{-24\lambda t}.
$$
取 $\lambda = 1/6000$（小时$^{-1}$，平均寿命 6000 小时）时，$\mathbb{P}(X > 400) = 0.7659$，$\mathbb{P}(X > 200) = 0.8752$，而 $\mathbb{P}(Y > 400) = 0.2019$，$\mathbb{P}(Y > 200) = 0.4493$。每只灯泡并没有变差，但 $Y$ 比 $X$ 随机地小很多：管理员关注的是"最先坏的那一只"。

### 7.2.3. 均匀分布的次序统计量与 Beta 分布

回忆 Beta 分布（[3.1.4](/3.1.4)）：$\alpha, \beta > 0$ 时密度为

$$
f(x) = \frac{1}{\mathrm{B}(\alpha, \beta)} x^{\alpha - 1}(1 - x)^{\beta - 1}, \quad 0 < x < 1, \qquad \mathrm{B}(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)},
$$
记作 $\mathrm{Beta}(\alpha, \beta)$。$\alpha = \beta = 1$ 时是 $\mathrm{U}(0, 1)$；$\alpha = 2, \beta = 1$ 时密度是直线 $2x$；$\alpha = \beta = 1/2$ 时密度呈 U 形；$\alpha = \beta = 2$ 时呈倒 U 形。Beta 分布常在贝叶斯统计中作为概率参数 $p$ 的先验分布：它是二项分布的共轭先验，$X \mid p \sim \mathrm{Bin}(n, p)$、先验 $p \sim \mathrm{Beta}(\alpha, \beta)$ 时，后验为 $p \mid X \sim \mathrm{Beta}(\alpha + X, \beta + n - X)$（[3.2.7](/3.2.7)）。

**例 7.2.3** 设 $U_1, \dots, U_n \overset{\text{iid}}{\sim} \mathrm{U}(0, 1)$，则 $U_{(k)} \sim \mathrm{Beta}(k, n - k + 1)$。

**证明** 此时 $F(x) = x$，$f(x) = 1$（$0 < x < 1$），由性质 7.2.3，

$$
g_k(x) = \frac{n!}{(k - 1)!\,(n - k)!} x^{k-1}(1 - x)^{n-k} = \frac{x^{k-1}(1 - x)^{n-k}}{\mathrm{B}(k, n - k + 1)}, \quad 0 < x < 1. \qquad \square
$$

所以 Beta 分布可以看作均匀分布的推广：整数参数的 Beta 分布就是均匀分布的次序统计量的分布。直观上，$n$ 个均匀点把 $(0, 1)$ 分成 $n + 1$ 段，第 $k$ 个点"平均"位于 $\frac{k}{n+1}$ 处（[3.1.8](/3.1.8) 中将算出 $\mathbb{E}U_{(k)} = \frac{k}{n+1}$）。

![n = 5 个独立 U(0,1) 的次序统计量 U_(k) 的密度，即 Beta(k, 6 - k)](./plots/uniform-order-statistics.py)

## 7.3. 随机变量的 p 分位数

### 7.3.1. 定义

设 $X$ 是 $(\Omega, \mathcal{F}, \mathbb{P})$ 上的随机变量，分布函数为 $F(x)$。直观上，对 $p \in (0, 1)$，若

$$
\mathbb{P}(X \le x) \ge p, \qquad \mathbb{P}(X \ge x) \ge 1 - p,
$$
就称 $x$ 是 $X$ 的 $p$ 分位数。这样确定的分位数不一定唯一（$F$ 在高度 $p$ 处有水平段时，整段都满足条件）。统计推断中通常不要求唯一性，例如问"抛 100 次均匀硬币，正面次数以 95% 的概率落在什么范围内"；但统计计算（例如随机数生成）要求唯一的定义。

**定义 7.3.1（分位数）** 对 $p \in (0, 1)$，定义

$$
F^{-1}(p) = \inf\{x \mid F(x) \ge p\},
$$
称 $F^{-1}(p)$ 为 $F$（或 $X$）的 $p$ **分位数**，通常记作 $\xi_p$。称 $\xi_{1/2}$ 为 $F$（或 $X$）的**中位数**。

等价地，$F^{-1}(p) = \sup\{x \mid F(x) < p\}$。$F^{-1}$ 称为分位数函数；$F$ 连续且严格递增时它就是通常的反函数，一般情形下它是 $F$ 的广义逆：在 $F$ 的跳跃处 $F^{-1}$ 是水平段，在 $F$ 的水平段处 $F^{-1}$ 跳跃。统计中常用上 $\alpha$ 分位数，即 $\xi_{1 - \alpha}$：例如标准正态分布的上 $\alpha$ 分位数 $z_\alpha = \Phi^{-1}(1 - \alpha)$ 满足 $\mathbb{P}(Z > z_\alpha) = \alpha$（[3.2.2](/3.2.2)）。

![一个既有跳跃又有水平段的分布函数 F（左）与它的分位数函数 F^{-1}（右）](./plots/quantile-function.py)

### 7.3.2. 分位数的性质

**性质 7.3.1** 设 $F$ 是分布函数，则

1. $F^{-1}(p)$ 关于 $p$ 单调不减；
2. $F^{-1}(F(x)) \le x$，$\forall x \in \mathbb{R}$（只要 $F(x) \in (0, 1)$）；
3. $F(F^{-1}(p)) \ge p$，$\forall p \in (0, 1)$；
4. $F^{-1}(p) \le t \iff p \le F(t)$；
5. $F^{-1}(p)$ 左连续；
6. 如果 $F$ 连续，则 $F(F^{-1}(p)) = p$，$\forall p \in (0, 1)$。

**证明** 1. 若 $p_1 < p_2$，则 $F(t) \ge p_2$ 蕴含 $F(t) \ge p_1$，即 $\{t \mid F(t) \ge p_1\} \supset \{t \mid F(t) \ge p_2\}$，取下确界得 $F^{-1}(p_1) \le F^{-1}(p_2)$。

2. $x \in \{t \mid F(t) \ge F(x)\}$，故 $F^{-1}(F(x)) = \inf\{t \mid F(t) \ge F(x)\} \le x$。

3. 由 $F$ 单调不减，$r \in \{t \mid F(t) \ge p\}$ 蕴含 $[r, \infty) \subset \{t \mid F(t) \ge p\}$，所以这个集合（非空，因为 $F(t) \to 1 > p$；有下界，因为 $F(t) \to 0 < p$）是 $[a, \infty)$ 或 $(a, \infty)$ 的形式，$a = F^{-1}(p)$。由于 $a + 1/n$ 属于该集合，$F(a + 1/n) \ge p$，令 $n \to \infty$，由 $F$ 的右连续性得 $F(a) \ge p$。这也说明该集合是闭区间 $[F^{-1}(p), \infty)$，下确界可以取到。

4. 若 $F(t) \ge p$，则 $t \in \{s \mid F(s) \ge p\}$，$t \ge F^{-1}(p)$。反之若 $F^{-1}(p) \le t$，由 $F$ 单调不减和性质 3，$F(t) \ge F(F^{-1}(p)) \ge p$。

5. 设 $p_n \uparrow p$。由性质 1，$F^{-1}(p_n)$ 单调不减且不超过 $F^{-1}(p)$，记其极限为 $b \le F^{-1}(p)$。对每个 $n$，$F^{-1}(p_n) \le b$，由性质 4 得 $p_n \le F(b)$；令 $n \to \infty$ 得 $p \le F(b)$，再由性质 4 得 $F^{-1}(p) \le b$。故 $\lim_n F^{-1}(p_n) = F^{-1}(p)$。

6. 由性质 3，$F(F^{-1}(p)) \ge p$。假设 $a = F^{-1}(p)$ 处 $F(a) > p$。由 $F$ 的连续性，存在 $\delta > 0$ 使 $F(a - \delta) \ge p$，于是由性质 4 得 $a = F^{-1}(p) \le a - \delta$，矛盾。 $\square$

性质 4 是分位数最常用的性质，它把关于 $F^{-1}$ 的不等式转化为关于 $F$ 的不等式。

### 7.3.3. 随机变量的生成

**定理 7.3.1（逆变换法）** 设 $U \sim \mathrm{U}(0, 1)$，$F$ 是任一分布函数，则 $Y = F^{-1}(U)$ 的分布函数是 $F$。

**证明** 由性质 7.3.1 的第 4 条，对任意 $y$，

$$
\mathbb{P}(Y \le y) = \mathbb{P}(F^{-1}(U) \le y) = \mathbb{P}(U \le F(y)) = F(y). \qquad \square
$$

**定理 7.3.2（概率积分变换）** 设 $X$ 的分布函数 $F$ 连续，则 $F(X) \sim \mathrm{U}(0, 1)$。

**证明** 对 $u \in (0, 1)$，由性质 7.3.1 的第 4 条，$\{F(X) \ge u\} = \{X \ge F^{-1}(u)\}$。由 $F$ 的连续性和第 6 条，

$$
\mathbb{P}(F(X) \ge u) = 1 - F(F^{-1}(u)) = 1 - u.
$$
所以 $\mathbb{P}(F(X) < u) = u$，再由右连续性 $\mathbb{P}(F(X) \le u) = \lim_{v \downarrow u}\mathbb{P}(F(X) < v) = u$。 $\square$

$F$ 有跳跃时结论不成立：例如 $X$ 只取两个值时 $F(X)$ 也只取两个值。

**例 7.3.1** 设可以方便地生成独立的 $\mathrm{U}(0, 1)$ 随机数 $U, V$，如何生成服从下列分布的随机数：(1) $\mathrm{Exp}(\lambda)$；(2) $\mathcal{N}(0, 1)$；(3) Cauchy 分布；(4) 经验分布函数 $F_n(x) = \frac{1}{n}\sum_{i=1}^n \boldsymbol{1}\{x_i \le x\}$，其中 $x_1, \dots, x_n$ 是给定的观测值。

**解** (1) $F(x) = 1 - \mathrm{e}^{-\lambda x}$，$F^{-1}(u) = -\lambda^{-1}\ln(1 - u)$，取 $X = -\lambda^{-1}\ln(1 - U)$（由于 $1 - U \sim \mathrm{U}(0, 1)$，也可取 $-\lambda^{-1}\ln U$）。

(2) 正态分布函数没有初等的反函数，用 Box–Muller 方法（例 7.1.8）：令 $\Theta = 2\pi U$，$R = \sqrt{-2\ln V}$，则 $X = R\cos\Theta$ 与 $Y = R\sin\Theta$ 独立，都服从 $\mathcal{N}(0, 1)$。

(3) 由例 7.1.6，取 $Z = X/Y$，其中 $X, Y$ 是 (2) 中生成的独立标准正态随机数；或用逆变换 $Z = \tan(\pi(U - 1/2))$。

(4) $F_n$ 是阶梯函数。设 $x_{(1)} \le \cdots \le x_{(n)}$ 是排序后的观测值，则 $F_n^{-1}(u) = x_{(k)}$，$\frac{k-1}{n} < u \le \frac{k}{n}$，于是

$$
\mathbb{P}(F_n^{-1}(U) = x_{(k)}) = \mathbb{P}\Big(\frac{k - 1}{n} < U \le \frac{k}{n}\Big) = \frac{1}{n}, \quad k = 1, \dots, n,
$$
即只需等概率地从观测值中有放回地抽样。这正是统计中 bootstrap 方法的基本操作。同样，两点分布 $\mathrm{Ber}(p)$ 可以取 $X = \boldsymbol{1}\{U > 1 - p\}$ 生成。

**例 7.3.2** 设 $X_1, \dots, X_n$ 独立同分布，分布函数 $F$ 连续，则 $T = -2\sum_{i=1}^n \ln F(X_i) \sim \chi^2_{2n}$。

**证明** 由定理 7.3.2，$U_i = F(X_i) \sim \mathrm{U}(0, 1)$，且相互独立。$Y_i = -2\ln U_i$ 满足 $\mathbb{P}(Y_i > y) = \mathbb{P}(U_i < \mathrm{e}^{-y/2}) = \mathrm{e}^{-y/2}$（$y > 0$），即 $Y_i \sim \mathrm{Exp}(1/2) = \chi^2_2$。由定理 7.1.6 的可加性，$T = \sum_i Y_i \sim \chi^2_{2n}$。 $\square$

这个结论是 Fisher 合并多个独立检验的 $p$ 值的方法的基础。

## 小结

| 问题 | 方法 | 结论 |
|---|---|---|
| 一般的 $g(\boldsymbol{X})$ | 先求 $F_Z(z) = \mathbb{P}(g(\boldsymbol{X}) \le z)$ 再求导 | 例 7.1.1、7.1.2 |
| $X + Y$ | 卷积公式 $f_Z(z) = \int f(x, z - x)\,\mathrm{d}x$ | 二项、Poisson、Gamma 分布的可加性 |
| $X - Y$，$X/Y$ | 化为已有结果，或先求分布函数 | $f_{X/Y}(z) = \int \lvert y \rvert f(zy, y)\,\mathrm{d}y$ |
| $(u(X, Y), v(X, Y))$ | 变量替换：$\sum_i f(x_i, y_i)\lvert J_i \rvert$ | 极坐标、Box–Muller |
| $X_{(k)}$ | 联合密度 $n!\prod f(x_i)$ 积分，或微元法 | $g_k = n\binom{n-1}{k-1}F^{k-1}(1-F)^{n-k}f$ |
| 随机数生成 | 逆变换 $F^{-1}(U) \sim F$ | $F$ 连续时 $F(X) \sim \mathrm{U}(0, 1)$ |

- 三大分布：$\sum Z_i^2 \sim \chi^2_n$，$Z/\sqrt{X/n} \sim t_n$，$\frac{X/m}{Y/n} \sim F_{m,n}$；$\chi^2_n = \Gamma(n/2, 1/2)$，$t_1$ 是 Cauchy 分布。
- 均匀分布的次序统计量服从 Beta 分布：$U_{(k)} \sim \mathrm{Beta}(k, n - k + 1)$。
- $p$ 分位数 $F^{-1}(p) = \inf\{x \mid F(x) \ge p\}$ 总是存在且唯一；关键性质是 $F^{-1}(p) \le t \iff p \le F(t)$。
- 技巧：蕴含独立性的联合密度可以直接拆分归一化；同一问题有多种解法，有时"先求分布函数"比直接用公式简便（例如 Cauchy 分布的密度）；微元法便于理解与记忆密度公式。
