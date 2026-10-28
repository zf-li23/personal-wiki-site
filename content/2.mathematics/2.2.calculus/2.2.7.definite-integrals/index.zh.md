---
title: 定积分
---

[第 6 章](/2.2.6)的不定积分是求导的逆运算；本章的定积分来自完全不同的问题：曲边梯形的面积、变密度细棒的质量、变力做的功。它们都可以用"分割、近似、求和、取极限"四步算出，抽象出来就是 Riemann 积分。本章先给出定义和可积的条件（7.1），列出积分的性质（7.2）；然后证明微积分基本定理（7.3）：连续函数的变上限积分是它的原函数，于是定积分可以用**原函数**计算，微分学与积分学由此联系起来。7.4 把换元法与分部积分法搬到定积分上，7.5、7.6 是几何与物理应用（面积、弧长、曲率、旋转体，以及物理中常用的微元法）。7.7 把积分推广到无穷区间和无界函数上，这里建立的比较判别法、绝对收敛等概念，在[第 8 章](/2.2.8)的级数中会几乎原样重现；Gamma 函数与 Beta 函数也在这里定义，[概率论](/3.1)中的 Gamma 分布、Beta 分布都以它们为基础。

## 7.1. 定积分的定义和存在条件

### 7.1.1. 引例

求曲边梯形的面积：设 $f \in C[a,b]$，$f(x) \ge 0$，求曲线 $y = f(x)$、直线 $x = a$、$x = b$ 与 $x$ 轴围成的曲边梯形的面积 $S$：

1. 分区间：插入分点 $a = x_0 < x_1 < \cdots < x_n = b$，直线 $x = x_i$ 把曲边梯形分成 $n$ 个小曲边梯形；
2. 取点作乘：在 $[x_{i-1}, x_i]$ 上任取 $\xi_i$，第 $i$ 块面积 $S_i \approx f(\xi_i)\Delta x_i$，$\Delta x_i = x_i - x_{i-1}$；
3. 求和：$S \approx \sum_{i=1}^n f(\xi_i)\Delta x_i$；
4. 取极限：令 $\lambda = \max_{1\le i\le n}\Delta x_i$，$S = \lim_{\lambda\to 0}\sum_{i=1}^n f(\xi_i)\Delta x_i$。

求质线的质量：位于 $[a,b]$ 上、线密度为 $\rho(x) \in C[a,b]$ 的细棒，同样四步得到质量 $m = \lim_{\lambda\to0}\sum_{i=1}^n \rho(\xi_i)\Delta x_i$。

两个问题的数学结构完全相同：一个定义在有界闭区间上的函数，按"分割、近似、求和、取极限"得到一个数。

### 7.1.2. Riemann 积分的定义

**定义 7.1.1（定积分）** 设 $f$ 是有界闭区间 $[a,b]$ 上的**有界函数**。任取分割 $T\colon a = x_0 < x_1 < \cdots < x_n = b$，任取 $\xi_i \in [x_{i-1}, x_i]$，作和式

$$
\sum_{i=1}^n f(\xi_i)\Delta x_i, \qquad \Delta x_i = x_i - x_{i-1},
$$
称为 $f$ 的一个 **Riemann 和**。令 $\lambda = \max_i \Delta x_i$。若极限 $\lim_{\lambda\to0}\sum_{i=1}^n f(\xi_i)\Delta x_i$ 存在（且与分割方式、$\xi_i$ 的取法无关），则称 $f$ 在 $[a,b]$ 上（Riemann）可积，记作 $f \in \mathcal{R}[a,b]$，称该极限为 $f$ 在 $[a,b]$ 上的**定积分**（Riemann 积分），记作 $\int_a^b f(x)\,\mathrm{d}x$。

其中 $a$、$b$ 分别称为积分下限、积分上限，$f(x)$ 称为被积函数，$\mathrm{d}x$ 是长度微元。几点说明：

- 定积分是一种特殊的极限：极限过程由分割和取点共同决定，但极限值与二者都无关。"$\lambda \to 0$"比"$n \to \infty$"更强：$n$ 很大而某个小区间不变短时，和式不必接近积分。
- 积分值只依赖于 $f$ 和 $[a,b]$，与积分变量的记号无关：$\int_a^b f(x)\,\mathrm{d}x = \int_a^b f(t)\,\mathrm{d}t$。
- 常数函数可积：$\int_a^b c\,\mathrm{d}x = c(b-a)$。
- 几何意义：$f \in C[a,b]$ 且 $f \ge 0$ 时，$\int_a^b f(x)\,\mathrm{d}x$ 是上述曲边梯形的面积；一般地，它是 $x$ 轴上方面积减去下方面积。例如 $0 < a < b$ 时，$\int_a^b x\,\mathrm{d}x = \frac12(a+b)(b-a) = \frac12(b^2 - a^2)$（梯形面积）。

### 7.1.3. 积分存在的条件

直接按定义判断可积性很不方便，因为要同时控制所有的分割与取点。办法是用每个小区间上的上确界、下确界把 Riemann 和夹住。

**定义 7.1.2（Darboux 和）** 设 $f$ 是 $[a,b]$ 上的有界函数，$T\colon a = x_0 < \cdots < x_n = b$ 是一个分割。记

$$
M_i = \sup_{x\in[x_{i-1},x_i]} f(x), \qquad m_i = \inf_{x\in[x_{i-1},x_i]} f(x),
$$
称 $\omega_i = M_i - m_i$ 为 $f$ 在 $[x_{i-1}, x_i]$ 上的**振幅**，称 $S(T) = \sum_i M_i\Delta x_i$、$s(T) = \sum_i m_i\Delta x_i$ 为 $f$ 关于 $T$ 的 Darboux 上和与 Darboux 下和。

对任意取点，$s(T) \le \sum_i f(\xi_i)\Delta x_i \le S(T)$，而且让 $\xi_i$ 遍历 $[x_{i-1},x_i]$，Riemann 和可以任意接近 $s(T)$ 与 $S(T)$。因此 Riemann 和有极限，当且仅当上和与下和之差

$$
S(T) - s(T) = \sum_{i=1}^n \omega_i\Delta x_i
$$
随 $\lambda \to 0$ 趋于 $0$。这就是下面的判别定理（证明的细节从略）。

**定理 7.1.1** 设 $f$ 在有界闭区间 $[a,b]$ 上有界，则

$$
f \in \mathcal{R}[a,b] \iff \lim_{\lambda\to0}\sum_{i=1}^n \omega_i\Delta x_i = 0.
$$

等价的说法（Darboux）是：对任意 $\varepsilon > 0$，存在一个分割 $T$ 使 $S(T) - s(T) < \varepsilon$。注意是"对每个 $\varepsilon$ 存在一个分割"，而不是"存在一个分割使极限为零"。

![x^2 在 [0,1] 上的 Darboux 上和与下和：等分为 n 份时 S - s = 1/n，两者都趋于 1/3](./plots/darboux-sums.py)

**例 7.1.1** **Dirichlet 函数** $D(x) = \boldsymbol{1}_{\mathbb{Q}}(x)$（有理点取 $1$，无理点取 $0$）在任何区间 $[a,b]$ 上不可积。

**证明** 有理数与无理数都在实数中稠密，所以对任意分割，每个小区间上 $M_i = 1$、$m_i = 0$，$\omega_i = 1$，从而 $\sum_i\omega_i\Delta x_i = b - a \not\to 0$。由定理 7.1.1，$D$ 不可积。$\square$

**定理 7.1.2** 设 $f$ 在有界闭区间 $[a,b]$ 上有界。

1. 若 $f \in C[a,b]$，则 $f \in \mathcal{R}[a,b]$；
2. 若 $f$ 在 $[a,b]$ 上单调，则 $f \in \mathcal{R}[a,b]$；
3. 若 $f$ 在 $[a,b]$ 上只有有限个间断点，则 $f \in \mathcal{R}[a,b]$。

**证明** 只证 1、2。

1. 由 **Heine–Cantor 定理**，$f$ 在 $[a,b]$ 上**一致连续**：对 $\varepsilon > 0$，存在 $\delta > 0$，当 $|u - v| < \delta$ 时 $|f(u) - f(v)| < \varepsilon/(b-a)$。于是只要 $\lambda < \delta$，就有 $\omega_i \le \varepsilon/(b-a)$（闭区间上连续函数取到最大值与最小值），$\sum_i\omega_i\Delta x_i \le \varepsilon$。由定理 7.1.1，$f$ 可积。
2. 不妨设 $f$ 单调增加且 $f(b) > f(a)$。此时 $\omega_i = f(x_i) - f(x_{i-1})$，当 $\lambda < \varepsilon/(f(b) - f(a))$ 时

$$
\sum_{i=1}^n\omega_i\Delta x_i \le \lambda\sum_{i=1}^n\bigl(f(x_i) - f(x_{i-1})\bigr) = \lambda\bigl(f(b) - f(a)\bigr) < \varepsilon. \qquad \square
$$

单调函数可以有无穷多个间断点（例如在 $x = 1/n$ 处跳跃的阶梯函数），所以 2 不包含在 3 中。

## 7.2. 定积分的性质

以下设 $f, g \in \mathcal{R}[a,b]$。

**性质 7.2.1（线性）** 对常数 $\alpha, \beta$，$\alpha f + \beta g \in \mathcal{R}[a,b]$，且 $\int_a^b(\alpha f + \beta g)\,\mathrm{d}x = \alpha\int_a^b f\,\mathrm{d}x + \beta\int_a^b g\,\mathrm{d}x$。

**性质 7.2.2（区间可加性）** 若 $c \in (a,b)$，则 $f \in \mathcal{R}[a,c]$，$f \in \mathcal{R}[c,b]$，且 $\int_a^b f\,\mathrm{d}x = \int_a^c f\,\mathrm{d}x + \int_c^b f\,\mathrm{d}x$。

**性质 7.2.3（方向性）** 规定 $\int_b^a f\,\mathrm{d}x = -\int_a^b f\,\mathrm{d}x$，$\int_a^a f\,\mathrm{d}x = 0$。有了这个规定，性质 7.2.2 对 $a, b, c$ 的任意大小顺序都成立（只要涉及的积分存在）。

**性质 7.2.4（保号性）** 若 $f(x) \ge 0$（$x \in [a,b]$），则 $\int_a^b f\,\mathrm{d}x \ge 0$。

**性质 7.2.5（保序性）** 若 $f(x) \le g(x)$（$x \in [a,b]$），则 $\int_a^b f\,\mathrm{d}x \le \int_a^b g\,\mathrm{d}x$。

**性质 7.2.6（可积必绝对可积）** $|f| \in \mathcal{R}[a,b]$，且 $\left|\int_a^b f\,\mathrm{d}x\right| \le \int_a^b |f|\,\mathrm{d}x$。

反之不成立：$f(x) = 1$（$x$ 为有理数），$f(x) = -1$（$x$ 为无理数）在 $[0,1]$ 上不可积（每个小区间上振幅为 $2$），但 $|f| \equiv 1$ 可积。

**性质 7.2.7（估值）** 若 $m \le f(x) \le M$（$x \in [a,b]$），则 $m(b-a) \le \int_a^b f\,\mathrm{d}x \le M(b-a)$。

**性质 7.2.8（积分中值定理）** 若 $f \in C[a,b]$，则存在 $\xi \in [a,b]$，使 $\int_a^b f(x)\,\mathrm{d}x = f(\xi)(b-a)$。

**证明** 设 $m$、$M$ 是 $f$ 在 $[a,b]$ 上的最小值与最大值（**最大最小值定理**）。由性质 7.2.7，$m \le \frac{1}{b-a}\int_a^b f\,\mathrm{d}x \le M$。由连续函数的**介值定理**，存在 $\xi \in [a,b]$ 使 $f(\xi)$ 等于这个平均值。$\square$

$\frac{1}{b-a}\int_a^b f\,\mathrm{d}x$ 称为 $f$ 在 $[a,b]$ 上的平均值；几何上，曲边梯形的面积等于一个以 $f(\xi)$ 为高的矩形面积。

**性质 7.2.9（乘积可积）** $fg \in \mathcal{R}[a,b]$。

**证明** 先设 $0 \le f \le M$，$0 \le g \le N$。记 $\omega_i, \omega_i', \omega_i''$ 分别为 $f, g, fg$ 在 $[x_{i-1}, x_i]$ 上的振幅。对该区间中任意 $u, v$，

$$
|f(u)g(u) - f(v)g(v)| \le |f(u)|\,|g(u) - g(v)| + |g(v)|\,|f(u) - f(v)| \le M\omega_i' + N\omega_i,
$$
故 $\omega_i'' \le M\omega_i' + N\omega_i$，由定理 7.1.1 得 $fg$ 可积。一般情形，令 $f_1 = \frac12(|f| + f)$、$f_2 = \frac12(|f| - f)$（都非负、可积，$f = f_1 - f_2$），$g_1, g_2$ 同理，则 $fg = f_1g_1 - f_1g_2 - f_2g_1 + f_2g_2$，由线性性可积。$\square$

**性质 7.2.10（推广的积分中值定理）** 若 $f \in C[a,b]$，$g \in \mathcal{R}[a,b]$ 且在 $[a,b]$ 上不变号，则存在 $\xi \in [a,b]$，使

$$
\int_a^b f(x)g(x)\,\mathrm{d}x = f(\xi)\int_a^b g(x)\,\mathrm{d}x.
$$

**证明** 不妨设 $g \ge 0$。由 $m \le f \le M$ 得 $m\int_a^b g \le \int_a^b fg \le M\int_a^b g$。若 $\int_a^b g = 0$，则 $\int_a^b fg = 0$，任取 $\xi$ 即可；否则 $\int_a^b fg\big/\int_a^b g \in [m, M]$，由**介值定理**存在 $\xi$ 使 $f(\xi)$ 等于它。$\square$

$g \equiv 1$ 时就是性质 7.2.8。两个中值定理的证明都只用到连续函数的介值定理，与微分中值定理无关。

**例 7.2.1** 设 $f \in C[a,b]$，$f \ge 0$，$\int_a^b f(x)\,\mathrm{d}x = 0$，则 $f \equiv 0$。

**证明** 反设存在 $x_0$ 使 $f(x_0) > 0$，由连续性可设 $x_0 \in (a,b)$，并存在 $\delta > 0$ 使 $[x_0 - \delta, x_0 + \delta] \subset [a,b]$ 且其上 $f(x) > f(x_0)/2$。于是

$$
\int_a^b f\,\mathrm{d}x \ge \int_{x_0-\delta}^{x_0+\delta} f\,\mathrm{d}x \ge 2\delta\cdot\frac{f(x_0)}{2} = \delta f(x_0) > 0,
$$
矛盾。$\square$

这个结论说明非负连续函数的积分"不会凭空为零"，它是 $\langle f, g\rangle = \int_a^b fg\,\mathrm{d}x$ 构成**内积**（正定性）的依据，见[线性代数 2.1.12](/2.1.12)。

**例 7.2.2** 设 $f(0) = 0$，$f$ 在 $[0,a]$ 上可导且 $M = \sup_{[0,a]}|f'| < +\infty$，则 $\left|\int_0^a f(x)\,\mathrm{d}x\right| \le \frac12 a^2M$。

**证明** 由 **Lagrange 中值定理**，$f(x) = f(x) - f(0) = f'(\eta)x$，故 $|f(x)| \le Mx$，$\left|\int_0^a f\right| \le \int_0^a Mx\,\mathrm{d}x = \frac12a^2M$。$\square$

**例 7.2.3** 设 $f$ 在 $[a,b]$ 上二阶可导且 $f'' \le 0$，则 $\int_a^b f(x)\,\mathrm{d}x \le (b-a)f\left(\frac{a+b}{2}\right)$。

**证明** $f'' \le 0$ 说明 $f$ 是**凹函数**（中文教材称"上凸"），曲线位于它在 $c = \frac{a+b}{2}$ 处的**切线**下方：$f(x) \le f(c) + f'(c)(x - c)$。两边积分，$\int_a^b (x - c)\,\mathrm{d}x = 0$，得 $\int_a^b f \le (b-a)f(c)$。$\square$

几何上，切线、$x = a$、$x = b$ 与 $x$ 轴围成的梯形面积恰为 $(b-a)f(c)$，而曲边梯形在它里面。

## 7.3. 变上限积分和 Newton–Leibniz 公式

### 7.3.1. 变上限积分

**定义 7.3.1（变上限积分）** 设 $f \in \mathcal{R}[a,b]$。由性质 7.2.2，对每个 $x \in [a,b]$，$\int_a^x f(t)\,\mathrm{d}t$ 存在，于是

$$
F(x) = \int_a^x f(t)\,\mathrm{d}t, \qquad a \le x \le b
$$
是 $[a,b]$ 上的函数，称为 $f$ 的变上限积分，$F(a) = 0$。

**定理 7.3.1** 设 $f \in \mathcal{R}[a,b]$，$F(x) = \int_a^x f(t)\,\mathrm{d}t$，则

1. $F$ 在 $[a,b]$ 上连续；
2. 若 $f$ 在 $x_0 \in [a,b]$ 处连续，则 $F$ 在 $x_0$ 处可导，且 $F'(x_0) = f(x_0)$（端点处为单侧导数）；
3. 若 $f \in C[a,b]$，则 $F'(x) = f(x)$ 在 $[a,b]$ 上处处成立。

**证明** 1. 可积函数有界，设 $|f| \le M$，则 $|F(x + \Delta x) - F(x)| = \left|\int_x^{x+\Delta x} f(t)\,\mathrm{d}t\right| \le M|\Delta x| \to 0$。

2. 对 $\varepsilon > 0$，由 $f$ 在 $x_0$ 连续，存在 $\delta > 0$，$|t - x_0| < \delta$ 时 $|f(t) - f(x_0)| < \varepsilon$。于是 $0 < |\Delta x| < \delta$ 时

$$
\left|\frac{F(x_0 + \Delta x) - F(x_0)}{\Delta x} - f(x_0)\right| = \left|\frac{1}{\Delta x}\int_{x_0}^{x_0+\Delta x}\bigl(f(t) - f(x_0)\bigr)\,\mathrm{d}t\right| \le \varepsilon.
$$

3 由 2 立得。$\square$

**推论 7.3.1** 区间上的连续函数一定有**原函数**：$\int_a^x f(t)\,\mathrm{d}t$ 就是一个。这补上了[第 6 章](/2.2.6)中"连续函数存在原函数"的证明。

结合**链式法则**，得到变限积分的求导公式：设 $f$ 连续，$u, v$ 可导，则

$$
\frac{\mathrm{d}}{\mathrm{d}x}\int_a^x f(t)\,\mathrm{d}t = f(x), \qquad \frac{\mathrm{d}}{\mathrm{d}x}\int_x^b f(t)\,\mathrm{d}t = -f(x), \qquad \frac{\mathrm{d}}{\mathrm{d}x}\int_{u(x)}^{v(x)} f(t)\,\mathrm{d}t = f\bigl(v(x)\bigr)v'(x) - f\bigl(u(x)\bigr)u'(x).
$$

最后一式的证明：取定 $c$，写成 $\int_c^{v(x)} f - \int_c^{u(x)} f$，令 $G(v) = \int_c^v f(t)\,\mathrm{d}t$，则 $\frac{\mathrm{d}}{\mathrm{d}x}G(v(x)) = G'(v)v'(x) = f(v(x))v'(x)$。注意被积函数里不能含 $x$；若含 $x$（如 $\int_0^x xf(t)\,\mathrm{d}t$），先把 $x$ 提到积分号外。

**例 7.3.1** 求 $\lim_{x\to0}\dfrac{1}{x^3}\displaystyle\int_0^x\left(\int_{\sin s}^0 t\,\mathrm{d}t\right)\mathrm{d}s$。

**解** $\frac00$ 型，两次使用 **L'Hôpital 法则**：

$$
\lim_{x\to0}\frac{\int_0^x\left(\int_{\sin s}^0 t\,\mathrm{d}t\right)\mathrm{d}s}{x^3} = \lim_{x\to0}\frac{\int_{\sin x}^0 t\,\mathrm{d}t}{3x^2} = \lim_{x\to0}\frac{-\sin x\cos x}{6x} = -\frac16.
$$

**例 7.3.2** 当 $x \to +\infty$ 时，$\int_a^x \mathrm{e}^{t^2}\,\mathrm{d}t \sim \dfrac{1}{2x}\mathrm{e}^{x^2}$。

**解** 由 L'Hôpital 法则（$\frac{\infty}{\infty}$ 型），

$$
\lim_{x\to+\infty}\frac{\int_a^x\mathrm{e}^{t^2}\,\mathrm{d}t}{\mathrm{e}^{x^2}/(2x)} = \lim_{x\to+\infty}\frac{\mathrm{e}^{x^2}}{\mathrm{e}^{x^2}\left(1 - \frac{1}{2x^2}\right)} = 1.
$$

$\mathrm{e}^{t^2}$ 的原函数不是**初等函数**，但变上限积分仍然能给出它的增长速度。

### 7.3.2. Newton–Leibniz 公式

**定理 7.3.2（微积分基本定理）** 设 $f \in C[a,b]$，$G$ 是 $f$ 在 $[a,b]$ 上的任一原函数，则

$$
\int_a^b f(x)\,\mathrm{d}x = G(b) - G(a) \;\eqqcolon\; G(x)\Big|_a^b.
$$

**证明** 由推论 7.3.1，$F(x) = \int_a^x f(t)\,\mathrm{d}t$ 是 $f$ 的原函数。同一函数的两个原函数相差常数，$G = F + C$，故 $G(b) - G(a) = F(b) - F(a) = \int_a^b f\,\mathrm{d}x$。$\square$

这个公式也称为 Newton–Leibniz 公式。它把定积分（一个和式的极限）的计算化为求原函数，[第 6 章](/2.2.6)的全部积分技巧因此可以用于定积分。定理要求 $f$ 连续；对只有有限个跳跃间断点的可积函数，可以分段使用。

**例 7.3.3**

1. $\int_0^1\frac{x}{\sqrt{1+x^2}}\,\mathrm{d}x = \sqrt{1+x^2}\Big|_0^1 = \sqrt2 - 1$；$\int_1^{\mathrm{e}}\frac{\ln^2 x}{x}\,\mathrm{d}x = \frac13\ln^3x\Big|_1^{\mathrm{e}} = \frac13$。
2. $\int_{-\pi/2}^{\pi/2}\sqrt{1 - \cos x}\,\mathrm{d}x$：由 $1 - \cos x = 2\sin^2\frac{x}{2}$，被积函数是 $\sqrt2\,\bigl|\sin\frac{x}{2}\bigr|$，开方后的绝对值不能丢。它是**偶函数**，所以积分等于 $2\sqrt2\int_0^{\pi/2}\sin\frac{x}{2}\,\mathrm{d}x = 2\sqrt2\left(-2\cos\frac x2\right)\Big|_0^{\pi/2} = 4(\sqrt2 - 1)$。

Riemann 和的极限与分割、取点无关。反过来，若已知 $f \in C[0,1]$，就可以取等分点与右端点，把某些和式的极限化为积分。

**算法 7.3.1（用定积分求和式极限）** 设 $f \in C[0,1]$，则

$$
\lim_{n\to\infty}\frac1n\sum_{i=1}^n f\left(\frac in\right) = \int_0^1 f(x)\,\mathrm{d}x.
$$

1. 把和式写成 $\frac1n\sum f(i/n)$ 的形式（提出 $\frac1n$，使通项只依赖于 $i/n$）；
2. 认出 $f$，必要时把区间换成 $[0,k]$：$\frac1n\sum_{i=1}^{kn} f(i/n) \to \int_0^k f$；
3. 乘积型先取对数化为和式。

**例 7.3.4**

1. $\displaystyle\lim_{n\to\infty}\sum_{i=1}^n\frac{n}{n^2+i^2} = \lim_{n\to\infty}\frac1n\sum_{i=1}^n\frac{1}{1+(i/n)^2} = \int_0^1\frac{\mathrm{d}x}{1+x^2} = \frac\pi4$。
2. $\displaystyle\lim_{n\to\infty}\frac{1^2 + 2^2 + \cdots + (2n)^2}{n^3} = \lim_{n\to\infty}\frac1n\sum_{i=1}^{2n}\left(\frac in\right)^2 = \int_0^2 x^2\,\mathrm{d}x = \frac83$。
3. 设 $f \in C[0,1]$，$f > 0$，则 $\displaystyle\lim_{n\to\infty}\sqrt[n]{f\left(\tfrac1n\right)f\left(\tfrac2n\right)\cdots f\left(\tfrac nn\right)} = \lim_{n\to\infty}\exp\left(\frac1n\sum_{i=1}^n\ln f\left(\frac in\right)\right) = \exp\left(\int_0^1\ln f(x)\,\mathrm{d}x\right)$。
4. 对 $p > 0$，$\displaystyle\lim_{n\to\infty}\frac{1^p + 2^p + \cdots + n^p}{n^{p+1}} = \int_0^1 x^p\,\mathrm{d}x = \frac{1}{p+1}$。

## 7.4. 换元积分法与分部积分法

### 7.4.1. 换元积分法

**定理 7.4.1（第一换元法）** 设 $f \in C[\alpha,\beta]$，$u = \varphi(x)$ 在 $[a,b]$ 上连续可导，值域含于 $[\alpha,\beta]$，$\varphi(a) = \alpha'$，$\varphi(b) = \beta'$，则

$$
\int_a^b f\bigl(\varphi(x)\bigr)\varphi'(x)\,\mathrm{d}x = \int_{\alpha'}^{\beta'} f(u)\,\mathrm{d}u.
$$

**定理 7.4.2（第二换元法）** 设 $f \in C[a,b]$，$x = \varphi(t)$ 在 $[\alpha,\beta]$ 上连续可导，值域含于 $[a,b]$，$\varphi(\alpha) = a$，$\varphi(\beta) = b$，则

$$
\int_a^b f(x)\,\mathrm{d}x = \int_\alpha^\beta f\bigl(\varphi(t)\bigr)\varphi'(t)\,\mathrm{d}t.
$$

**证明** 两者相同：设 $F$ 是 $f$ 的原函数，则 $F(\varphi)$ 是 $f(\varphi)\varphi'$ 的原函数（**链式法则**），两边分别用 Newton–Leibniz 公式，都等于 $F(\varphi(\text{上限})) - F(\varphi(\text{下限}))$。$\square$

与不定积分的**换元积分法**相比：

- 换元必换限，算完不必代回原变量；
- 第二换元法不要求 $x = \varphi(t)$ 有反函数（不定积分需要反函数才能代回），也允许 $\alpha > \beta$；
- 但 $\varphi$ 必须连续可导，值域不能越出 $f$ 的定义区间，且端点必须对应。

**例 7.4.1（换元的陷阱）**

1. $\int_0^3 x\sqrt[3]{1-x^2}\,\mathrm{d}x$ 不能令 $x = \sin t$：$\sin t$ 取不到 $(1,3]$ 中的值。应令 $u = 1 - x^2$（第一换元法）。
2. $\int_0^1\sqrt{1-x^2}\,\mathrm{d}x$ 令 $x = \sin t$ 时，可以取 $t$ 从 $\pi$ 到 $\frac\pi2$，但此时 $\sqrt{1-\sin^2t} = |\cos t| = -\cos t$，结果 $\int_\pi^{\pi/2}(-\cos t)\cos t\,\mathrm{d}t = \frac\pi4$ 仍然正确；忘记绝对值就会得到错误的符号。
3. $\int_{-1}^2 x\,\mathrm{d}x$ 不能令 $x = \sqrt t$（$\sqrt t \ge 0$ 取不到负值）；令 $t = x^2$ 作第一换元是可以的：$\int_{-1}^2 x\,\mathrm{d}x = \frac12\int_1^4\mathrm{d}t = \frac32$，这里 $\varphi(x) = x^2$ 不必单调。
4. $\int_{-1}^1\frac{\mathrm{d}x}{1+x^2}$ 不能令 $t = 1/x$：它在 $x = 0$ 处无定义。硬算会得到 $-\int_{-1}^1\frac{\mathrm{d}t}{1+t^2} = -\frac\pi2$，而正确值是 $\frac\pi2$。

**例 7.4.2**

1. $\int_1^4\frac{\mathrm{d}x}{1+\sqrt x}$，令 $x = t^2$：$= \int_1^2\frac{2t}{1+t}\,\mathrm{d}t = 2\bigl(t - \ln(1+t)\bigr)\Big|_1^2 = 2 + 2\ln\frac23$。
2. $\int_0^a\sqrt{a^2-x^2}\,\mathrm{d}x$，令 $x = a\sin t$：$= a^2\int_0^{\pi/2}\cos^2t\,\mathrm{d}t = \frac{\pi a^2}{4}$（四分之一圆的面积）。
3. $\int_0^{\pi/2}\frac{\sin x}{1+\cos^2x}\,\mathrm{d}x$，令 $u = \cos x$：$= \int_0^1\frac{\mathrm{d}u}{1+u^2} = \frac\pi4$。

**定理 7.4.3** 设 $f$ 连续。

1. 若 $f$ 是 $[-a,a]$ 上的**偶函数**，则 $\int_{-a}^a f\,\mathrm{d}x = 2\int_0^a f\,\mathrm{d}x$；若是**奇函数**，则 $\int_{-a}^a f\,\mathrm{d}x = 0$。
2. 若 $f$ 是以 $T$ 为周期的**周期函数**，则对任意 $a$，$\int_a^{a+T} f\,\mathrm{d}x = \int_0^T f\,\mathrm{d}x$。
3. $\int_0^\pi xf(\sin x)\,\mathrm{d}x = \frac\pi2\int_0^\pi f(\sin x)\,\mathrm{d}x$。

**证明** 1. 在 $\int_{-a}^0 f(x)\,\mathrm{d}x$ 中令 $x = -t$，得 $\int_0^a f(-t)\,\mathrm{d}t$，再按奇偶性合并。

2. $\int_a^{a+T} = \int_a^0 + \int_0^T + \int_T^{a+T}$，在最后一项中令 $x = t + T$，得 $\int_0^a f(t)\,\mathrm{d}t$，与第一项抵消。

3. 令 $x = \pi - t$，$I = \int_0^\pi(\pi - t)f(\sin t)\,\mathrm{d}t = \pi\int_0^\pi f(\sin t)\,\mathrm{d}t - I$。$\square$

**例 7.4.3**

1. $\int_{-\pi/2}^{\pi/2}\tan x\,(1 + x^2)\,\mathrm{d}x = 0$（奇函数）。
2. $\int_0^{100\pi}\sqrt{1 - \cos 2x}\,\mathrm{d}x = 100\int_0^\pi\sqrt2\,|\sin x|\,\mathrm{d}x = 200\sqrt2$（周期 $\pi$）。
3. $\int_{-1}^1\left(\sqrt{1-x^2} + x\mathrm{e}^{x^2}\right)\mathrm{d}x = 2\int_0^1\sqrt{1-x^2}\,\mathrm{d}x = \frac\pi2$。
4. $\int_0^\pi\frac{x\sin x}{1+\cos^2x}\,\mathrm{d}x = \frac\pi2\int_0^\pi\frac{\sin x}{1+\cos^2x}\,\mathrm{d}x = \frac\pi2\cdot\frac\pi2 = \frac{\pi^2}{4}$。

### 7.4.2. 分部积分法

**定理 7.4.4** 设 $u, v$ 在 $[a,b]$ 上连续可导，则

$$
\int_a^b u(x)v'(x)\,\mathrm{d}x = u(x)v(x)\Big|_a^b - \int_a^b u'(x)v(x)\,\mathrm{d}x.
$$

**证明** 对 $(uv)' = u'v + uv'$ 两边在 $[a,b]$ 上积分，用 Newton–Leibniz 公式。$\square$

选 $u$ 与 $v'$ 的原则与不定积分的**分部积分法**相同；好处是边界项 $uv|_a^b$ 常常为零或很简单。

**例 7.4.4**

1. $\int_0^{1/2}\arcsin x\,\mathrm{d}x = x\arcsin x\Big|_0^{1/2} - \int_0^{1/2}\frac{x\,\mathrm{d}x}{\sqrt{1-x^2}} = \frac{\pi}{12} + \frac{\sqrt3}{2} - 1$。
2. $\int_0^\pi\mathrm{e}^x\sin x\,\mathrm{d}x$：分部积分两次回到原积分，$I = \mathrm{e}^\pi + 1 - I$，$I = \frac12(\mathrm{e}^\pi + 1)$。
3. $\int_0^1\mathrm{e}^{\sqrt x}\,\mathrm{d}x \overset{x = t^2}{=} 2\int_0^1 t\mathrm{e}^t\,\mathrm{d}t = 2\bigl(t\mathrm{e}^t - \mathrm{e}^t\bigr)\Big|_0^1 = 2$。
4. $\int_0^1(\arcsin x)^2\,\mathrm{d}x = x(\arcsin x)^2\Big|_0^1 - 2\int_0^1\frac{x\arcsin x}{\sqrt{1-x^2}}\,\mathrm{d}x = \frac{\pi^2}{4} + 2\left(\sqrt{1-x^2}\arcsin x\Big|_0^1 - \int_0^1\mathrm{d}x\right) = \frac{\pi^2}{4} - 2$。

**公式 7.4.1（Wallis 积分）** 记 $I_n = \int_0^{\pi/2}\sin^nx\,\mathrm{d}x$，则 $\int_0^{\pi/2}\cos^nx\,\mathrm{d}x = I_n$，且

$$
I_n = \frac{n-1}{n}I_{n-2}, \qquad I_n = \begin{cases}\dfrac{(n-1)!!}{n!!}\cdot\dfrac\pi2, & n \text{ 为偶数},\\[2ex] \dfrac{(n-1)!!}{n!!}, & n \text{ 为奇数},\end{cases}
$$
其中 $n!! = n(n-2)(n-4)\cdots$（乘到 $2$ 或 $1$）。

**证明** 令 $u = \sin^{n-1}x$，$\mathrm{d}v = \sin x\,\mathrm{d}x$：

$$
I_n = -\sin^{n-1}x\cos x\Big|_0^{\pi/2} + (n-1)\int_0^{\pi/2}\sin^{n-2}x\cos^2x\,\mathrm{d}x = (n-1)(I_{n-2} - I_n),
$$
即 $I_n = \frac{n-1}{n}I_{n-2}$；再由 $I_0 = \frac\pi2$、$I_1 = 1$ 递推。令 $x = \frac\pi2 - t$ 即得 $\cos^n$ 的积分与 $I_n$ 相等。$\square$

例如 $\int_0^{\pi/2}\cos^2x\,\mathrm{d}x = \frac12\cdot\frac\pi2 = \frac\pi4$，$\int_0^{\pi/2}\sin^4x\,\mathrm{d}x = \frac34\cdot\frac12\cdot\frac\pi2 = \frac{3\pi}{16}$，$\int_0^{\pi/2}\sin^5x\,\mathrm{d}x = \frac45\cdot\frac23 = \frac{8}{15}$。

**例 7.4.5** 求 $I_n = \int_0^{\pi/4}\tan^{2n}x\,\mathrm{d}x$。

**解** 由 $\tan^2x = \sec^2x - 1$，$I_n = \int_0^{\pi/4}\tan^{2n-2}x\,\mathrm{d}(\tan x) - I_{n-1} = \frac{1}{2n-1} - I_{n-1}$，$I_0 = \frac\pi4$，于是

$$
I_n = (-1)^n\left[\frac\pi4 - \left(1 - \frac13 + \frac15 - \cdots + \frac{(-1)^{n-1}}{2n-1}\right)\right].
$$

由于 $[0,\frac\pi4]$ 上 $0 \le \tan x \le \frac{4x}{\pi}$（$\tan$ 在该区间上是**凸函数**，图像在连接两端点的弦下方），$0 \le I_n \le \int_0^{\pi/4}\left(\frac{4x}{\pi}\right)^{2n}\mathrm{d}x = \frac{\pi}{4(2n+1)} \to 0$。所以 $1 - \frac13 + \frac15 - \cdots = \frac\pi4$，这是 Leibniz 级数。

## 7.5. 定积分的几何应用

### 7.5.1. 平面图形的面积

在直角坐标下，连续曲线 $y = f(x)$ 与 $x = a$、$x = b$、$x$ 轴围成的图形面积为 $S = \int_a^b|f(x)|\,\mathrm{d}x$；两条连续曲线 $y = f(x)$、$y = g(x)$ 与 $x = a$、$x = b$ 围成的面积为

$$
S = \int_a^b|f(x) - g(x)|\,\mathrm{d}x.
$$

对参数方程表示的曲线，若 $x = x(t)$、$y = y(t)$（$x(\alpha) = a$，$x(\beta) = b$，$x(t)$ 单调），则 $\int_a^b y\,\mathrm{d}x = \int_\alpha^\beta y(t)x'(t)\,\mathrm{d}t$（第二换元法）。

**例 7.5.1** $y = x^2$ 与 $y^2 = x$ 围成的图形，交点 $(0,0)$、$(1,1)$，$S = \int_0^1(\sqrt x - x^2)\,\mathrm{d}x = \frac23 - \frac13 = \frac13$。

**例 7.5.2** 旋轮线 $x = a(t - \sin t)$、$y = a(1 - \cos t)$（$0 \le t \le 2\pi$，$a > 0$）的一拱与 $x$ 轴围成的面积为

$$
S = \int_0^{2\pi a}y\,\mathrm{d}x = \int_0^{2\pi}a^2(1 - \cos t)^2\,\mathrm{d}t = a^2(2\pi + \pi) = 3\pi a^2.
$$

最后是极坐标。在平面上取极点 $O$ 与从 $O$ 出发的极轴 $Ox$，点 $P$ 由它到 $O$ 的距离 $r$（极径）与 $OP$ 和极轴的夹角 $\theta$（极角）确定，$(r,\theta)$ 称为 $P$ 的极坐标（polar coordinates）。以直角坐标的原点为极点、$x$ 轴正向为极轴时，$x = r\cos\theta$，$y = r\sin\theta$。曲线写成 $r = r(\theta)$，例如 $r = a$ 是以极点为圆心的圆，$\theta = \theta_0$ 是从极点出发的射线。

设 $r = r(\theta)$ 在 $[\alpha,\beta]$ 上连续非负，求它与射线 $\theta = \alpha$、$\theta = \beta$ 围成的曲边扇形 $D$ 的面积。分割 $[\alpha,\beta]$，射线 $\theta = \theta_i$ 把 $D$ 分成小块，第 $i$ 块近似为半径 $r(\xi_i)$、圆心角 $\Delta\theta_i$ 的扇形，面积 $\frac12r(\xi_i)^2\Delta\theta_i$。求和取极限：

$$
S = \frac12\int_\alpha^\beta r(\theta)^2\,\mathrm{d}\theta.
$$

![极坐标下的面积：心形线用小扇形逼近（左），双纽线（右）](./plots/polar-area.py)

**例 7.5.3** 双纽线 $r^2 = 2a^2\cos2\theta$（$-\frac\pi4 \le \theta \le \frac\pi4$ 或 $\frac{3\pi}4 \le \theta \le \frac{5\pi}4$）围成的面积为

$$
S = 2\cdot\frac12\int_{-\pi/4}^{\pi/4}2a^2\cos2\theta\,\mathrm{d}\theta = a^2\sin2\theta\Big|_{-\pi/4}^{\pi/4} = 2a^2.
$$

心形线 $r = a(1 + \cos\theta)$ 围成的面积为 $\frac12\int_0^{2\pi}a^2(1 + \cos\theta)^2\,\mathrm{d}\theta = \frac{a^2}{2}(2\pi + \pi) = \frac32\pi a^2$。

### 7.5.2. 曲线的长度

没有自交点的曲线称为简单曲线。设简单曲线 $L$ 的参数方程为 $x = x(t)$、$y = y(t)$（$\alpha \le t \le \beta$）。

**定义 7.5.1** 在 $L$ 上按参数顺序取分点 $M_0, M_1, \dots, M_n$，作内接折线。若分点加密（$\max_i\Delta t_i \to 0$）时折线长 $\sum_i|M_{i-1}M_i|$ 的极限存在，则称 $L$ 为**可求长曲线**，该极限称为 $L$ 的**弧长**。

**定理 7.5.1** 若 $x(t)$、$y(t)$ 在 $[\alpha,\beta]$ 上连续可导，则 $L$ 可求长，且

$$
l = \int_\alpha^\beta\sqrt{x'(t)^2 + y'(t)^2}\,\mathrm{d}t.
$$

**证明** 由 **Lagrange 中值定理**，$|M_{i-1}M_i| = \sqrt{x'(\xi_i)^2 + y'(\eta_i)^2}\,\Delta t_i$，$\xi_i, \eta_i \in [t_{i-1}, t_i]$。由于 $y'$ **一致连续**，把 $\eta_i$ 换成 $\xi_i$ 引起的误差随 $\lambda \to 0$ 趋于零，于是折线长趋于 $\sqrt{x'^2 + y'^2}$ 的 Riemann 和的极限，即上述积分。$\square$

$\mathrm{d}l = \sqrt{x'(t)^2 + y'(t)^2}\,\mathrm{d}t$ 称为弧长微元。几种特殊形式：

| 曲线 | 弧长 |
|---|---|
| 参数方程 $x(t), y(t)$ | $\int_\alpha^\beta\sqrt{x'^2 + y'^2}\,\mathrm{d}t$ |
| 空间曲线 $x(t), y(t), z(t)$ | $\int_\alpha^\beta\sqrt{x'^2 + y'^2 + z'^2}\,\mathrm{d}t$ |
| $y = f(x)$，$a \le x \le b$（取 $x$ 为参数） | $\int_a^b\sqrt{1 + f'(x)^2}\,\mathrm{d}x$ |
| 极坐标 $r = r(\theta)$（$x = r\cos\theta$，$y = r\sin\theta$） | $\int_\alpha^\beta\sqrt{r^2 + r'^2}\,\mathrm{d}\theta$ |

**例 7.5.4**

1. 星形线 $x = a\cos^3t$、$y = a\sin^3t$（$0 \le t \le 2\pi$）：$\sqrt{x'^2 + y'^2} = 3a|\sin t\cos t|$，$l = \frac{3a}{2}\int_0^{2\pi}|\sin2t|\,\mathrm{d}t = 6a$。
2. 螺旋线 $x = a\sin t$、$y = a\cos t$、$z = ct$（$0 \le t \le 2\pi$）：$l = \int_0^{2\pi}\sqrt{a^2 + c^2}\,\mathrm{d}t = 2\pi\sqrt{a^2 + c^2}$。
3. 抛物线 $y = x^2$（$0 \le x \le 1$）：$l = \int_0^1\sqrt{1 + 4x^2}\,\mathrm{d}x \overset{t=2x}{=} \frac12\int_0^2\sqrt{1+t^2}\,\mathrm{d}t = \frac14\left(t\sqrt{1+t^2} + \ln\bigl(t + \sqrt{1+t^2}\bigr)\right)\Big|_0^2 = \frac{\sqrt5}{2} + \frac14\ln(2 + \sqrt5)$。
4. 心形线 $r = a(1 + \cos\theta)$：$r^2 + r'^2 = 2a^2(1 + \cos\theta) = 4a^2\cos^2\frac\theta2$，$l = \int_0^{2\pi}2a\left|\cos\frac\theta2\right|\mathrm{d}\theta = 8a$。

### 7.5.3. 平面曲线的曲率

**定义 7.5.2（光滑曲线）** 若 $x'(t)$、$y'(t)$ 连续且 $x'(t)^2 + y'(t)^2 \ne 0$，则称曲线 $L\colon x = x(t), y = y(t)$ 为光滑曲线。光滑曲线上每一点都有切线，且切线方向随点连续变化。

曲线弯曲得越厉害，沿曲线走过单位长度时切线转过的角度越大。设 $M$、$M'$ 是 $L$ 上两点，两点处切线的夹角为 $\Delta\varphi$，两点间的弧长为 $\Delta l$，则 $|\Delta\varphi/\Delta l|$ 是 $M$ 到 $M'$ 之间的平均弯曲程度。

**定义 7.5.3（曲率）** 若极限 $k = \lim_{M'\to M}\left|\frac{\Delta\varphi}{\Delta l}\right|$ 存在，则称 $k$ 为 $L$ 在 $M$ 处的曲率，称 $R = \frac1k$ 为 $L$ 在 $M$ 处的**曲率半径**。

设 $\varphi$ 是切线与 $x$ 轴的夹角，$\tan\varphi = \frac{y'(t)}{x'(t)}$，则 $\frac{\mathrm{d}\varphi}{\mathrm{d}t} = \frac{y''x' - y'x''}{x'^2 + y'^2}$，又 $\frac{\mathrm{d}l}{\mathrm{d}t} = \sqrt{x'^2 + y'^2}$，于是

$$
k = \left|\frac{\mathrm{d}\varphi/\mathrm{d}t}{\mathrm{d}l/\mathrm{d}t}\right| = \frac{|x'y'' - x''y'|}{(x'^2 + y'^2)^{3/2}}.
$$

特殊情形：

$$
y = f(x)\colon\; k = \frac{|y''|}{(1 + y'^2)^{3/2}}; \qquad r = r(\theta)\colon\; k = \frac{|r^2 + 2r'^2 - rr''|}{(r^2 + r'^2)^{3/2}}.
$$

**例 7.5.5** 抛物线 $y = x^2$ 在 $(x, x^2)$ 处 $k = \frac{2}{(1 + 4x^2)^{3/2}}$，$R = \frac12(1 + 4x^2)^{3/2}$，顶点处弯曲最厉害。圆 $r = R_0$（$r' = r'' = 0$）处处 $k = \frac{R_0^2}{R_0^3} = \frac{1}{R_0}$，曲率半径就是圆的半径；直线的曲率为零。

### 7.5.4. 旋转体的体积和旋转曲面的面积

由连续曲线 $y = y(x)$、直线 $x = a$、$x = b$ 与 $x$ 轴围成的平面图形绕 $x$ 轴旋转一周，得到一个旋转体（solid of revolution）。用垂直于 $x$ 轴的平面把它切成薄片，$[x, x + \mathrm{d}x]$ 上的薄片近似为圆柱，体积 $\mathrm{d}V = \pi y(x)^2\,\mathrm{d}x$，于是

$$
V = \pi\int_a^b y(x)^2\,\mathrm{d}x.
$$

**例 7.5.6** 椭圆 $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ 绕 $x$ 轴旋转：$V = \pi\int_{-a}^a\frac{b^2}{a^2}(a^2 - x^2)\,\mathrm{d}x = \frac43\pi ab^2$；$a = b = R$ 时得球的体积 $\frac43\pi R^3$。

参数方程与极坐标的情形：

- 曲线 $x = x(t)$、$y = y(t)$ 绕 $x$ 轴：$V = \pi\int_\alpha^\beta y(t)^2x'(t)\,\mathrm{d}t$。例如旋轮线一拱绕 $x$ 轴旋转，$V = \pi a^3\int_0^{2\pi}(1 - \cos t)^3\,\mathrm{d}t = 5\pi^2a^3$。
- 曲边扇形 $0 \le r \le r(\theta)$，$\alpha \le \theta \le \beta$（$0 \le \alpha < \beta \le \pi$）绕极轴旋转：小扇形绕极轴旋转得到的体积约为 $\frac{2\pi}{3}r^3\sin\theta\,\mathrm{d}\theta$，故 $V = \frac{2\pi}{3}\int_\alpha^\beta r(\theta)^3\sin\theta\,\mathrm{d}\theta$。例如 $r = R$、$0 \le \theta \le \pi$ 给出球的体积 $\frac{2\pi}{3}R^3\cdot2 = \frac43\pi R^3$。

设 $y(x) \ge 0$ 在 $[a,b]$ 上连续可导，曲线 $y = y(x)$ 绕 $x$ 轴旋转一周得到旋转曲面（surface of revolution）。用平面 $x = x_i$ 把它切成小环带，每条近似为圆台的侧面，面积 $\pi\bigl(y(x_{i-1}) + y(x_i)\bigr)|P_{i-1}P_i|$，而 $|P_{i-1}P_i| = \sqrt{1 + y'(\xi_i)^2}\,\Delta x_i$。求和取极限，得

$$
S = 2\pi\int_a^b y(x)\sqrt{1 + y'(x)^2}\,\mathrm{d}x = 2\pi\int y\,\mathrm{d}l.
$$

这里不能用圆柱侧面 $2\pi y\,\mathrm{d}x$ 近似：薄片的侧面是倾斜的，要用弧长微元 $\mathrm{d}l$ 而不是 $\mathrm{d}x$。

**例 7.5.7** $y = \sqrt x$（$0 \le x \le 1$）绕 $x$ 轴：$S = 2\pi\int_0^1\sqrt x\sqrt{1 + \frac{1}{4x}}\,\mathrm{d}x = \pi\int_0^1\sqrt{4x+1}\,\mathrm{d}x = \frac\pi6(5\sqrt5 - 1)$。半圆 $y = \sqrt{R^2 - x^2}$ 绕 $x$ 轴：$y\sqrt{1 + y'^2} = R$，$S = 2\pi R\cdot2R = 4\pi R^2$。

## 7.6. 定积分的物理应用

数学上按"四步法"（分割、近似、求和、取极限）定义积分；物理中更常用下面的简化写法。

**算法 7.6.1（微元法）** 求一个分布在 $[a,b]$ 上、对区间具有可加性的量 $Q$：

1. 取典型小区间 $[x, x + \mathrm{d}x]$，写出 $Q$ 在其上的近似值 $\mathrm{d}Q = q(x)\,\mathrm{d}x$（误差是 $\mathrm{d}x$ 的**高阶无穷小**）；
2. $Q = \int_a^b q(x)\,\mathrm{d}x$。

微元法直观简明，本质上就是 Newton–Leibniz 公式：$Q(x)$ 是"从 $a$ 到 $x$ 的那部分量"，第 1 步是在说 $Q'(x) = q(x)$。7.5 节的旋转体体积就是这样推出的。

**例 7.6.1（引力）** 均匀细棒长 $2l$、质量 $M$，在其延长线上距中心 $a$（$a > l$）处有单位质点。以棒的中点为原点，$[x, x + \mathrm{d}x]$ 段的质量为 $\frac{M}{2l}\mathrm{d}x$，对质点的引力为 $\mathrm{d}F = \frac{GM}{2l}\frac{\mathrm{d}x}{(a - x)^2}$，故

$$
F = \frac{GM}{2l}\int_{-l}^l\frac{\mathrm{d}x}{(a - x)^2} = \frac{GM}{a^2 - l^2}.
$$

$l \to 0$ 时回到质点间的引力 $GM/a^2$。

**例 7.6.2（变力做功）** $40\,\mathrm{N}$ 的力使弹簧伸长 $5\,\mathrm{cm}$，再拉伸 $3\,\mathrm{cm}$ 需做多少功？由 Hooke 定律 $F = kx$，$k = 40/0.05 = 800\,\mathrm{N/m}$，$W = \int_{0.05}^{0.08}800x\,\mathrm{d}x = 1.56\,\mathrm{J}$。

**例 7.6.3（抽水做功）** 高 $5\,\mathrm{m}$、底面半径 $3\,\mathrm{m}$ 的圆柱形水桶装满水，从顶部全部抽出。取向下的 $x$ 轴，原点在桶顶，把深度 $[x, x + \mathrm{d}x]$ 的薄层提到顶部做功 $\mathrm{d}W = \rho g\cdot9\pi\,\mathrm{d}x\cdot x$，故 $W = 9\pi\rho g\int_0^5x\,\mathrm{d}x = \frac{225}{2}\pi\rho g \approx 3.46 \times 10^6\,\mathrm{J}$（$\rho = 10^3\,\mathrm{kg/m^3}$，$g = 9.8\,\mathrm{m/s^2}$）。

## 7.7. 反常积分

定积分要求区间有界、被积函数有界。去掉这两个条件中的一个，就得到反常积分（improper integral）：在无穷区间上的积分，与无界函数的积分。两者都定义为定积分的极限。

### 7.7.1. 无穷积分

**定义 7.7.1（无穷积分）** 设 $f$ 在 $[a, +\infty)$ 上有定义，且对任意 $A > a$，$f \in \mathcal{R}[a,A]$。称

$$
\int_a^{+\infty}f(x)\,\mathrm{d}x = \lim_{A\to+\infty}\int_a^A f(x)\,\mathrm{d}x
$$
为 $f$ 在 $[a,+\infty)$ 上的无穷积分（不论极限是否存在）。极限存在时称该积分收敛，否则称它发散。类似地定义 $\int_{-\infty}^b f(x)\,\mathrm{d}x$。若存在 $a$ 使 $\int_{-\infty}^a f$ 与 $\int_a^{+\infty}f$ 都收敛，则称 $\int_{-\infty}^{+\infty}f$ 收敛，且 $\int_{-\infty}^{+\infty}f = \int_{-\infty}^a f + \int_a^{+\infty}f$。

$\int_{-\infty}^{+\infty}f$ 的收敛性与和都与 $a$ 的选取无关（由区间可加性）。注意它要求两端分别收敛，不能用 $\lim_{A\to+\infty}\int_{-A}^A f$ 代替：$\int_{-A}^A x\,\mathrm{d}x = 0$，但 $\int_{-\infty}^{+\infty}x\,\mathrm{d}x$ 发散。

**例 7.7.1** 设 $p > 0$。$p = 1$ 时 $\int_1^A\frac{\mathrm{d}x}{x} = \ln A \to +\infty$；$p \ne 1$ 时 $\int_1^A\frac{\mathrm{d}x}{x^p} = \frac{A^{1-p} - 1}{1-p}$。于是

$$
\int_1^{+\infty}\frac{\mathrm{d}x}{x^p}\;\begin{cases}= \dfrac{1}{p-1}, & p > 1,\\[1ex] \text{发散}, & 0 < p \le 1.\end{cases}
$$

收敛的无穷积分可以照常使用换元法、分部积分法和 Newton–Leibniz 公式，只要把 $G(+\infty)$ 理解为 $\lim_{x\to+\infty}G(x)$。

**例 7.7.2**

1. $\int_0^{+\infty}x^3\mathrm{e}^{-x^2}\,\mathrm{d}x \overset{u = x^2}{=} \frac12\int_0^{+\infty}u\mathrm{e}^{-u}\,\mathrm{d}u = \frac12\left(-u\mathrm{e}^{-u}\Big|_0^{+\infty} + \int_0^{+\infty}\mathrm{e}^{-u}\,\mathrm{d}u\right) = \frac12$。
2. $\int_1^{+\infty}\frac{\arctan x}{x^2}\,\mathrm{d}x = -\frac{\arctan x}{x}\Big|_1^{+\infty} + \int_1^{+\infty}\frac{\mathrm{d}x}{x(1+x^2)} = \frac\pi4 + \frac12\ln\frac{x^2}{1+x^2}\Big|_1^{+\infty} = \frac\pi4 + \frac12\ln2$。

### 7.7.2. 瑕积分

**定义 7.7.2（瑕积分）** 设 $f$ 在 $(a,b]$ 上有定义，在 $a$ 的右侧附近无界，且对任意 $\eta \in (0, b-a)$，$f \in \mathcal{R}[a+\eta, b]$。称

$$
\int_a^b f(x)\,\mathrm{d}x = \lim_{\eta\to0^+}\int_{a+\eta}^b f(x)\,\mathrm{d}x
$$
为 $f$ 在 $(a,b]$ 上的瑕积分，$a$ 称为**瑕点**。极限存在时称瑕积分收敛，否则称它发散。类似地定义以 $b$ 为瑕点的瑕积分；瑕点在区间内部时，在瑕点处拆开，要求两部分分别收敛。

**例 7.7.3** 设 $p > 0$，$0 < \eta < 1$。$\int_\eta^1\frac{\mathrm{d}x}{x^p}$ 等于 $-\ln\eta$（$p = 1$）或 $\frac{1 - \eta^{1-p}}{1-p}$（$p \ne 1$）。令 $\eta \to 0^+$，一般地

$$
\int_a^b\frac{\mathrm{d}x}{(x-a)^p}\;\begin{cases}= \dfrac{(b-a)^{1-p}}{1-p}, & 0 < p < 1,\\[1ex] \text{发散}, & p \ge 1.\end{cases}
$$

与例 7.7.1 方向相反：在无穷远处，$x^{-p}$ 要衰减得足够快（$p > 1$）；在瑕点附近，$x^{-p}$ 要增长得足够慢（$p < 1$）。$p = 1$ 在两边都发散。

![x 的 -p 次幂在 [1, +∞) 与 (0, 1] 上积分收敛的条件恰好相反（左、中）；Gamma 函数（右）](./plots/improper-p-integrals.py)

**例 7.7.4**

1. $\int_1^{\sqrt2}\frac{\mathrm{d}x}{x\sqrt{x^2-1}} = \lim_{\eta\to0^+}\left(-\arcsin\frac1x\right)\Big|_{1+\eta}^{\sqrt2} = \frac\pi2 - \frac\pi4 = \frac\pi4$。
2. $\int_0^1\ln x\,\mathrm{d}x = \lim_{\eta\to0^+}\left(x\ln x\Big|_\eta^1 - \int_\eta^1\mathrm{d}x\right) = -1$（$\eta\ln\eta \to 0$）。
3. $\int_1^{\mathrm{e}}\frac{\mathrm{d}x}{x\sqrt{1 - \ln^2x}} = \lim_{\eta\to0^+}\arcsin(\ln x)\Big|_1^{\mathrm{e}-\eta} = \frac\pi2$。

**例 7.7.5** 求 $\lim_{n\to\infty}\dfrac{\sqrt[n]{n!}}{n}$。

**解** 取对数，$\ln\frac{\sqrt[n]{n!}}{n} = \frac1n\sum_{i=1}^n\ln\frac in$，这是 $\ln x$ 在 $(0,1]$ 上的 Riemann 和。$\ln x$ 在 $0$ 附近无界，严格地说要对瑕积分单独论证（$\ln x$ 单调，可以用单调函数的上下和夹逼）；结果是 $\frac1n\sum\ln\frac in \to \int_0^1\ln x\,\mathrm{d}x = -1$，故极限为 $\mathrm{e}^{-1}$。

瑕积分可以化成无穷积分：设 $a$ 是瑕点，令 $x = a + \frac1u$，

$$
\int_{a+\eta}^b f(x)\,\mathrm{d}x = \int_{1/(b-a)}^{1/\eta}f\left(a + \frac1u\right)\frac{\mathrm{d}u}{u^2}, \qquad \int_a^b f(x)\,\mathrm{d}x = \int_{1/(b-a)}^{+\infty}f\left(a + \frac1u\right)\frac{\mathrm{d}u}{u^2}.
$$

所以两类反常积分的理论是平行的，下面以无穷积分为主叙述，瑕积分的对应结论只列出。

### 7.7.3. 反常积分的收敛判别法

很多反常积分算不出原函数，只能判断它是否收敛。

**定理 7.7.1（无穷积分的 Cauchy 收敛准则）** $\int_a^{+\infty}f(x)\,\mathrm{d}x$ 收敛的充分必要条件是：对任意 $\varepsilon > 0$，存在 $M > a$，当 $A_2 > A_1 > M$ 时，$\left|\int_{A_1}^{A_2}f(x)\,\mathrm{d}x\right| < \varepsilon$。

**证明** 记 $F(A) = \int_a^A f$。收敛即 $\lim_{A\to+\infty}F(A)$ 存在；由函数极限的 **Cauchy 收敛准则**，这等价于 $|F(A_2) - F(A_1)| = \left|\int_{A_1}^{A_2}f\right| < \varepsilon$ 对充分大的 $A_1, A_2$ 成立。$\square$

**定义 7.7.3（绝对收敛）** 若 $\int_a^{+\infty}|f(x)|\,\mathrm{d}x$ 收敛，则称 $\int_a^{+\infty}f(x)\,\mathrm{d}x$ **绝对收敛**；若 $\int_a^{+\infty}f$ 收敛而不绝对收敛，则称它**条件收敛**。瑕积分同样定义。

**定理 7.7.2** 绝对收敛的反常积分必收敛。

**证明** 由 Cauchy 收敛准则，$\left|\int_{A_1}^{A_2}f\right| \le \int_{A_1}^{A_2}|f| < \varepsilon$。$\square$

对照性质 7.2.6：定积分"可积必绝对可积"，反之不成立；反常积分"绝对收敛必收敛"，反之不成立。例如 $\int_1^{+\infty}\frac{\sin x}{x}\,\mathrm{d}x$ 条件收敛：分部积分 $\int_1^A\frac{\sin x}{x}\,\mathrm{d}x = \cos1 - \frac{\cos A}{A} - \int_1^A\frac{\cos x}{x^2}\,\mathrm{d}x$，右端在 $A \to +\infty$ 时收敛（最后一项绝对收敛）；而 $|\sin x| \ge \sin^2x = \frac12(1 - \cos2x)$，$\int_1^{+\infty}\frac{1 - \cos2x}{2x}\,\mathrm{d}x$ 发散。

下面设 $f, g$ 在 $[a,+\infty)$ 上非负，且在每个 $[a,A]$ 上可积。此时 $F(A) = \int_a^A f$ 单调不减，收敛当且仅当 $F$ 有上界。

**定理 7.7.3（比较判别法）** 设 $0 \le f(x) \le g(x)$（$x \ge a$）。若 $\int_a^{+\infty}g$ 收敛，则 $\int_a^{+\infty}f$ 收敛；若 $\int_a^{+\infty}f$ 发散，则 $\int_a^{+\infty}g$ 发散。

**证明** $\int_a^A f \le \int_a^A g \le \int_a^{+\infty}g$，单调有上界的函数在 $+\infty$ 处有极限。后一半是前一半的逆否命题。$\square$

**定理 7.7.4（比较判别法的极限形式）** 设 $f \ge 0$，$g > 0$，$\lim_{x\to+\infty}\frac{f(x)}{g(x)} = q$。

1. 若 $0 \le q < +\infty$ 且 $\int_a^{+\infty}g$ 收敛，则 $\int_a^{+\infty}f$ 收敛；
2. 若 $0 < q \le +\infty$ 且 $\int_a^{+\infty}g$ 发散，则 $\int_a^{+\infty}f$ 发散。

特别地，$0 < q < +\infty$ 时两者同敛散。

**证明** 1. 存在 $A$，$x > A$ 时 $0 \le f/g < q + 1$，即 $f < (q+1)g$，由定理 7.7.3 及"收敛性与有限区间无关"得证。2. $q$ 有限时，存在 $A$ 使 $x > A$ 时 $f > \frac q2g$；$q = +\infty$ 时 $f > g$。由定理 7.7.3 得证。$\square$

取 $g = x^{-p}$（例 7.7.1）作比较对象，得到最常用的判别法。

**定理 7.7.5（比阶判别法）** 设 $f \ge 0$。

1. 若存在 $p > 1$，使 $\lim_{x\to+\infty}x^pf(x)$ 存在（有限），则 $\int_a^{+\infty}f$ 收敛；
2. 若存在 $p \le 1$，使 $\lim_{x\to+\infty}x^pf(x)$ 存在且不为零，或为 $+\infty$，则 $\int_a^{+\infty}f$ 发散。

直观地说：$f$ 在无穷远处是比 $1/x$ 更高阶的**无穷小量**（至少像某个 $x^{-p}$，$p > 1$）时收敛。

**例 7.7.6**

1. 对任意 $\alpha$，$\int_1^{+\infty}x^\alpha\mathrm{e}^{-x}\,\mathrm{d}x$ 收敛：$\lim_{x\to+\infty}x^2\cdot x^\alpha\mathrm{e}^{-x} = 0$，取 $p = 2$。
2. $\int_1^{+\infty}\frac{\ln(x+2) - \ln x}{\sqrt x}\,\mathrm{d}x$ 收敛：$x^{3/2}\cdot\frac{\ln(1 + 2/x)}{\sqrt x} = x\ln\left(1 + \frac2x\right) \to 2$，取 $p = \frac32$。
3. $\int_1^{+\infty}x^2\mathrm{e}^{-x}\sin x\,\mathrm{d}x$ 绝对收敛：$x^2\cdot x^2\mathrm{e}^{-x}|\sin x| \to 0$。被积函数变号时，先判断 $|f|$ 的积分是否收敛。

瑕积分的对应结论：设 $a$ 是 $\int_a^b f$ 的瑕点。

**定理 7.7.6（瑕积分的 Cauchy 收敛准则）** $\int_a^b f$ 收敛 $\iff$ 对任意 $\varepsilon > 0$，存在 $\delta \in (0, b-a)$，当 $0 < \eta_1 < \eta_2 < \delta$ 时 $\left|\int_{a+\eta_1}^{a+\eta_2}f(x)\,\mathrm{d}x\right| < \varepsilon$。

比较判别法及其极限形式对瑕积分照样成立（把 $x \to +\infty$ 换成 $x \to a^+$）。比较对象换成 $(x-a)^{-p}$，由例 7.7.3，$p$ 的方向与无穷积分相反：

**定理 7.7.7（瑕积分的比阶判别法）** 设 $f \ge 0$，$a$ 是瑕点。

1. 若存在 $p < 1$，使 $\lim_{x\to a^+}(x-a)^pf(x)$ 存在（有限），则 $\int_a^b f$ 收敛；
2. 若存在 $p \ge 1$，使 $\lim_{x\to a^+}(x-a)^pf(x)$ 存在且不为零，或为 $+\infty$，则 $\int_a^b f$ 发散。

**例 7.7.7** $\int_0^1\frac{\ln x}{x^\alpha}\,\mathrm{d}x$（被积函数在 $(0,1)$ 上不变号，可以对 $-\ln x/x^\alpha \ge 0$ 用比阶判别法）：

- $\alpha < 1$ 时取 $p = \frac{1+\alpha}{2} \in (\alpha, 1)$，$x^p\cdot\frac{|\ln x|}{x^\alpha} = x^{p-\alpha}|\ln x| \to 0$，收敛；
- $\alpha \ge 1$ 时取 $p = \alpha$，$x^\alpha\cdot\frac{|\ln x|}{x^\alpha} = |\ln x| \to +\infty$，发散（$\alpha \le 0$ 时 $0$ 不是瑕点，积分是正常的，结论"收敛"也成立）。

一个积分可能同时是无穷积分和瑕积分，此时把它拆成每段只含一种"反常"的积分，要求各段都收敛。概率论中两个最重要的含参反常积分就是这样讨论的。

**定义 7.7.4（Gamma 函数）** 对 $s > 0$，令

$$
\Gamma(s) = \int_0^{+\infty}x^{s-1}\mathrm{e}^{-x}\,\mathrm{d}x.
$$

**例 7.7.8** 这个积分收敛当且仅当 $s > 0$。拆成 $I_1 = \int_0^1x^{s-1}\mathrm{e}^{-x}\,\mathrm{d}x$ 与 $I_2 = \int_1^{+\infty}x^{s-1}\mathrm{e}^{-x}\,\mathrm{d}x$。$I_2$ 对一切 $s$ 收敛（例 7.7.6）。$s < 1$ 时 $0$ 是 $I_1$ 的瑕点，取 $p = 1 - s$，$x^p\cdot x^{s-1}\mathrm{e}^{-x} \to 1$：$s > 0$ 即 $p < 1$ 时收敛，$s \le 0$ 即 $p \ge 1$ 时发散。

Gamma 函数的基本性质：

1. $\Gamma(1) = 1$；$\Gamma(s+1) = s\Gamma(s)$（分部积分：$\int_0^{+\infty}x^s\mathrm{e}^{-x}\,\mathrm{d}x = -x^s\mathrm{e}^{-x}\Big|_0^{+\infty} + s\int_0^{+\infty}x^{s-1}\mathrm{e}^{-x}\,\mathrm{d}x$）；
2. 因此 $\Gamma(n+1) = n!$：Gamma 函数是阶乘在正实数上的推广；
3. $\Gamma\left(\frac12\right) = \int_0^{+\infty}x^{-1/2}\mathrm{e}^{-x}\,\mathrm{d}x \overset{x = t^2}{=} 2\int_0^{+\infty}\mathrm{e}^{-t^2}\,\mathrm{d}t = \sqrt\pi$，最后一步是 **Gauss 积分**，在[第 12 章](/2.2.12)用二重积分计算。

**定义 7.7.5（Beta 函数）** 对 $\alpha > 0$，$\beta > 0$，令

$$
\mathrm{B}(\alpha,\beta) = \int_0^1x^{\alpha-1}(1-x)^{\beta-1}\,\mathrm{d}x.
$$

**例 7.7.9** 这个积分收敛当且仅当 $\alpha > 0$ 且 $\beta > 0$。可能的瑕点是 $0$ 与 $1$，在 $\frac12$ 处拆开。在 $0$ 附近，取 $p = 1 - \alpha$，$x^p\cdot x^{\alpha-1}(1-x)^{\beta-1} \to 1$，收敛 $\iff p < 1 \iff \alpha > 0$；在 $1$ 附近同理，取 $p = 1 - \beta$，收敛 $\iff \beta > 0$。

令 $x = 1 - t$ 得 $\mathrm{B}(\alpha,\beta) = \mathrm{B}(\beta,\alpha)$；令 $x = \sin^2\theta$ 得 $\mathrm{B}(\alpha,\beta) = 2\int_0^{\pi/2}\sin^{2\alpha-1}\theta\cos^{2\beta-1}\theta\,\mathrm{d}\theta$，例如 $\mathrm{B}\left(\frac12,\frac12\right) = \pi$，这与 Wallis 积分是同一类积分。两个函数之间有关系 $\mathrm{B}(\alpha,\beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$，证明同样要用二重积分（[第 12 章](/2.2.12)）。

## 小结

| 内容 | 要点 |
|---|---|
| 定义 | Riemann 和的极限（$\lambda \to 0$，与分割、取点无关）；可积 $\iff \sum\omega_i\Delta x_i \to 0$ |
| 可积的充分条件 | 连续；单调；有界且只有有限个间断点。Dirichlet 函数不可积 |
| 性质 | 线性、区间可加、保序、$\lvert\int f\rvert \le \int\lvert f\rvert$、估值、积分中值定理（证明用介值定理） |
| 微积分基本定理 | $\left(\int_a^x f\right)' = f(x)$（$f$ 连续）；$\int_a^b f = G(b) - G(a)$ |
| 计算 | 换元必换限、注意开方的绝对值；奇偶性与周期性；Wallis 积分 $\frac{(n-1)!!}{n!!}\left(\frac\pi2\right)$ |
| 和式极限 | $\frac1n\sum f(i/n) \to \int_0^1 f$ |

| 几何量 | 直角坐标 $y = f(x)$ | 参数方程 $x(t), y(t)$ | 极坐标 $r(\theta)$ |
|---|---|---|---|
| 面积 | $\int_a^b\lvert f - g\rvert\,\mathrm{d}x$ | $\int_\alpha^\beta y(t)x'(t)\,\mathrm{d}t$ | $\frac12\int_\alpha^\beta r^2\,\mathrm{d}\theta$ |
| 弧长 | $\int_a^b\sqrt{1 + f'^2}\,\mathrm{d}x$ | $\int_\alpha^\beta\sqrt{x'^2 + y'^2}\,\mathrm{d}t$ | $\int_\alpha^\beta\sqrt{r^2 + r'^2}\,\mathrm{d}\theta$ |
| 曲率 | $\frac{\lvert y''\rvert}{(1 + y'^2)^{3/2}}$ | $\frac{\lvert x'y'' - x''y'\rvert}{(x'^2 + y'^2)^{3/2}}$ | $\frac{\lvert r^2 + 2r'^2 - rr''\rvert}{(r^2 + r'^2)^{3/2}}$ |
| 绕 $x$ 轴（极轴）的体积 | $\pi\int_a^b f^2\,\mathrm{d}x$ | $\pi\int_\alpha^\beta y^2x'\,\mathrm{d}t$ | $\frac{2\pi}{3}\int_\alpha^\beta r^3\sin\theta\,\mathrm{d}\theta$ |
| 旋转曲面面积 | $2\pi\int_a^b f\sqrt{1 + f'^2}\,\mathrm{d}x$ | $2\pi\int_\alpha^\beta y\sqrt{x'^2 + y'^2}\,\mathrm{d}t$ | — |

| 反常积分 | 无穷积分 $\int_a^{+\infty}f$ | 瑕积分 $\int_a^b f$（瑕点 $a$） |
|---|---|---|
| 基准 | $\int_1^{+\infty}x^{-p}\,\mathrm{d}x$ 收敛 $\iff p > 1$ | $\int_a^b(x-a)^{-p}\,\mathrm{d}x$ 收敛 $\iff p < 1$ |
| 比阶判别法（$f \ge 0$） | $x^pf(x)$ 有极限，$p > 1$：收敛；极限非零或 $+\infty$，$p \le 1$：发散 | $(x-a)^pf(x)$ 有极限，$p < 1$：收敛；极限非零或 $+\infty$，$p \ge 1$：发散 |
| 一般函数 | Cauchy 收敛准则；绝对收敛必收敛 | 同左 |
| Gamma 与 Beta | $\Gamma(s)$ 收敛 $\iff s > 0$，$\Gamma(n+1) = n!$，$\Gamma(\frac12) = \sqrt\pi$ | $\mathrm{B}(\alpha,\beta)$ 收敛 $\iff \alpha, \beta > 0$ |
