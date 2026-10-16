---
title: 实数与函数
---

微积分研究的对象是定义在实数集上的函数，研究的工具是极限。本章做两件准备工作：一是说明实数集的结构，特别是区间、邻域和确界——确界存在定理刻画了实数"没有空隙"，它是下一章一切极限存在定理的源头；二是整理函数的基本概念、常见属性和本课程要反复使用的初等函数。这里的许多内容在离散数学中已有更一般的处理：**实数**的构造见 [1.2.4](/1.2.4#sec-4.1)，函数作为关系、单射与满射、反函数见 [1.2.3](/1.2.3)，偏序集中的**上确界**见 [1.2.2](/1.2.2#def-2.8.6)。本章只在 $\mathbb{R}$ 上以微积分的语言重述，并补充分析中要用到的事实。

[第 2 章](/2.2.2)用本章的确界存在定理证明单调收敛定理，[第 3 章](/2.2.3)讨论初等函数的连续性。

## 1.1. 实数

### 1.1.1. 区间与邻域

实数集 $\mathbb{R}$ 的以下子集称为区间（$a < b$）：

| 名称 | 记号与定义 |
|---|---|
| 开区间 | $(a, b) = \{x \mid a < x < b\}$ |
| 闭区间 | $[a, b] = \{x \mid a \leq x \leq b\}$ |
| 半开半闭区间 | $(a, b] = \{x \mid a < x \leq b\}$，$[a, b) = \{x \mid a \leq x < b\}$ |
| 无穷区间 | $[a, +\infty) = \{x \mid x \geq a\}$，$(a, +\infty)$，$(-\infty, b]$，$(-\infty, b)$，$(-\infty, +\infty) = \mathbb{R}$ |

$+\infty$、$-\infty$ 只是记号，不是实数。极限的定义要描述"$x$ 充分靠近 $x_0$"，为此引入邻域。

**定义 1.1.1（邻域）** 设 $x_0 \in \mathbb{R}$，$\delta > 0$。称开区间

$$
N(x_0, \delta) = \{x \mid |x - x_0| < \delta\} = (x_0 - \delta, x_0 + \delta)
$$
为 $x_0$ 的 $\delta$ **邻域**；去掉中心 $x_0$ 后的集合

$$
N^*(x_0, \delta) = \{x \mid 0 < |x - x_0| < \delta\} = (x_0 - \delta, x_0) \cup (x_0, x_0 + \delta)
$$
称为 $x_0$ 的 $\delta$ **去心邻域**（空心邻域）。半径 $\delta$ 不重要时简写为 $N(x_0)$、$N^*(x_0)$。

去心邻域是函数极限的舞台：$x \to x_0$ 时的极限只与 $f$ 在某个 $N^*(x_0, \delta)$ 上的值有关，与 $f(x_0)$ 无关（[第 2 章](/2.2.2#sec-2.3)）。

绝对值满足三角不等式：对任意实数 $a, b, c$，

$$
\bigl||a| - |b|\bigr| \leq |a + b| \leq |a| + |b|, \qquad |a - b| \leq |a - c| + |c - b|.
$$

后一式是极限证明中"插项"的依据：要估计 $a$ 与 $b$ 的距离，就插入一个与两者都接近的 $c$。

**有理数**是可以写成 $\frac{m}{n}$（$m \in \mathbb{Z}$，$n \in \mathbb{N}_+$）的数，不是有理数的实数称为无理数。

**例 1.1.1** $\sqrt2$ 是无理数。

**证明** 设 $\sqrt2 = \frac{m}{n}$，$m, n \in \mathbb{N}_+$ 互素。则 $m^2 = 2n^2$ 是偶数，故 $m$ 是偶数；令 $m = 2k$，得 $n^2 = 2k^2$，$n$ 也是偶数，与 $m, n$ 互素矛盾。$\square$

**定理 1.1.1（Archimedes 性质）** 对任意 $p > 0$ 和 $q > 0$，存在 $N \in \mathbb{N}_+$ 使得 $Np > q$。

直观地说，无论 $p$ 多小、$q$ 多大，把 $p$ 累加足够多次总能超过 $q$；取 $N = \lfloor q/p \rfloor + 1$ 还满足 $(N - 1)p \leq q < Np$。它看似显然，实际上依赖实数的完备性，证明见例 1.1.3。由它可以推出 $\lim\limits_{n\to\infty} \frac1n = 0$ 这类最基本的事实。

**定理 1.1.2（有理数的稠密性）** 任意非空开区间 $(a, b)$ 中都含有有理数，因而含有无穷多个有理数。

**证明** 由定理 1.1.1，取 $n \in \mathbb{N}_+$ 使 $n(b - a) > 1$，再令 $m = \lfloor na \rfloor + 1$，则 $na < m \leq na + 1 < nb$，即 $a < \frac{m}{n} < b$。对 $(a, \frac mn)$ 重复这一论证，便得到无穷多个有理数。$\square$

### 1.1.2. 实数集的界和确界

**定义 1.1.2（界与确界）** 设 $E$ 是 $\mathbb{R}$ 的非空子集。

1. 若存在 $a \in \mathbb{R}$，使得对所有 $x \in E$ 都有 $x \leq a$（$x \geq a$），则称 $a$ 为 $E$ 的一个上界（下界）。既有上界又有下界的集合称为有界集。
2. 若存在 $a \in E$，使得对所有 $x \in E$ 都有 $x \leq a$（$x \geq a$），则称 $a$ 为 $E$ 的最大值（最小值），记为 $\max E$（$\min E$）。
3. 若 $E$ 有上界（下界），称最小的上界（最大的下界）为 $E$ 的**上确界**（**下确界**），记为 $\sup E$（$\inf E$）。

最大值必须属于 $E$，上确界则不必：$E = (0, 1)$ 没有最大值，但 $\sup E = 1$。三者的关系是

$$
E \text{ 有最大值} \implies E \text{ 有上确界（且 } \sup E = \max E\text{）} \implies E \text{ 有上界}.
$$

第二个箭头反过来是否成立，就是实数理论的核心问题。

**定理 1.1.3（确界存在定理）** 设 $E \subseteq \mathbb{R}$ 非空。

1. 若 $E$ 有上界，则 $E$ 必有上确界；
2. 若 $E$ 有下界，则 $E$ 必有下确界。

本课程把这条定理当作实数的基本性质（公理）使用，不加证明；从 Cauchy 序列出发构造实数时（[1.2.4](/1.2.4#sec-4.1)），它是可以证明的定理。它表达的是实数的完备性（completeness of the real numbers），也称实数的连续性：实数在数轴上没有"空隙"。有理数没有这一性质：$\{x \in \mathbb{Q} \mid x^2 < 2\}$ 在 $\mathbb{Q}$ 中有上界，却没有有理数的最小上界，因为它"应当"的上确界 $\sqrt2$ 不是有理数（例 1.1.1）。[第 3 章](/2.2.3#sec-3.2)将看到，单调收敛定理、区间套定理、列紧性定理和 Cauchy 收敛准则都与它等价。

**定理 1.1.4（确界的刻画）** 设 $E$ 为非空实数集合，$a, b \in \mathbb{R}$。则

1. $b = \sup E$ 当且仅当：(i) $b$ 是 $E$ 的上界；(ii) 对任意 $\varepsilon > 0$，存在 $x \in E$ 使得 $x > b - \varepsilon$；
2. $a = \inf E$ 当且仅当：(i) $a$ 是 $E$ 的下界；(ii) 对任意 $\varepsilon > 0$，存在 $x \in E$ 使得 $x < a + \varepsilon$。

**证明** 只证 1。条件 (ii) 说的正是"任何比 $b$ 小的数 $b - \varepsilon$ 都不是上界"，与 (i) 合起来即"$b$ 是最小的上界"。$\square$

条件 (ii) 是使用上确界的标准方式：从 $\sup E$ 往下退一点点，就能在 $E$ 中找到元素。[第 2 章](/2.2.2)证明单调收敛定理正是这样做的。

**例 1.1.2** 设 $E = \left\{1 - \frac1n \;\middle|\; n \in \mathbb{N}_+\right\}$，则 $\min E = \inf E = 0$，$\sup E = 1$ 但 $E$ 没有最大值。事实上 $1$ 是上界；对任意 $\varepsilon > 0$，由定理 1.1.1 取 $n > \frac1\varepsilon$，就有 $1 - \frac1n > 1 - \varepsilon$。

**例 1.1.3（Archimedes 性质的证明）** 设 $p, q > 0$，若对所有 $n \in \mathbb{N}_+$ 都有 $np \leq q$，则 $E = \{np \mid n \in \mathbb{N}_+\}$ 有上界，由定理 1.1.3 有上确界 $s$。由定理 1.1.4 存在 $n$ 使 $np > s - p$，于是 $(n + 1)p > s$，与 $s$ 是上界矛盾。

## 1.2. 函数

### 1.2.1. 函数的定义

**定义 1.2.1（函数）** 设 $D \subseteq \mathbb{R}$ 非空。如果对每个 $x \in D$，按照确定的法则 $f$，都有唯一的实数 $y$ 与之对应，则称 $f$ 为定义在 $D$ 上的一个**函数**，记为

$$
y = f(x), \quad x \in D.
$$
$x$ 称为自变量，$y$ 称为因变量，$D$ 称为定义域，记为 $D(f)$；函数值的全体 $R(f) = \{f(x) \mid x \in D\}$ 称为值域。

这是 [1.2.3](/1.2.3#def-3.1.1) 中一般**映射**在 $D \subseteq \mathbb{R}$、取值于 $\mathbb{R}$ 时的特例。函数由两个要素决定：对应法则 $f$ 与定义域 $D(f)$；自变量用什么字母无关紧要，$y = f(x)$ 与 $y = f(t)$ 是同一个函数。没有指明定义域时，约定定义域是使表达式（及实际问题）有意义的全体自变量。

**例 1.2.1** $y = x$ 与 $y = \frac{x^2}{x}$ 不是同一个函数：前者定义域为 $\mathbb{R}$，后者为 $\mathbb{R} \setminus \{0\}$。

### 1.2.2. 函数的一些重要属性

**定义 1.2.2（奇函数与偶函数）** 设 $f$ 的定义域 $D(f)$ 关于原点对称。若对任意 $x \in D(f)$ 都有 $f(-x) = f(x)$，则称 $f$ 为**偶函数**；若都有 $f(-x) = -f(x)$，则称 $f$ 为**奇函数**。

偶函数的图形关于 $y$ 轴对称，奇函数的图形关于原点对称。定义域关于原点对称的任意函数都可以唯一地分解为一个偶函数与一个奇函数之和：

$$
f(x) = \underbrace{\frac{f(x) + f(-x)}{2}}_{\text{偶}} + \underbrace{\frac{f(x) - f(-x)}{2}}_{\text{奇}}.
$$

例如 $\mathrm{e}^x = \cosh x + \sinh x$（双曲函数见 §1.2.4）。

**例 1.2.2** 判断奇偶性：(1) $y = x + \sin x$ 是奇函数。(2) $y = x\,\frac{2^x + 1}{2^x - 1}$：因子 $g(x) = \frac{2^x + 1}{2^x - 1}$ 满足 $g(-x) = \frac{1 + 2^x}{1 - 2^x} = -g(x)$，是奇函数，乘以奇函数 $x$ 后得到偶函数。(3) $y = \ln\bigl(x + \sqrt{1 + x^2}\bigr)$：由 $\bigl(-x + \sqrt{1+x^2}\bigr)\bigl(x + \sqrt{1+x^2}\bigr) = 1$ 得 $f(-x) = -f(x)$，是奇函数。

**定义 1.2.3（单调函数）** 设 $f$ 定义在集合 $D$ 上。若对任意 $x_1, x_2 \in D$，由 $x_1 < x_2$ 可推出 $f(x_1) < f(x_2)$（$f(x_1) > f(x_2)$），则称 $f$ 在 $D$ 上单调增加（单调减少）；若由 $x_1 < x_2$ 可推出 $f(x_1) \leq f(x_2)$（$f(x_1) \geq f(x_2)$），则称 $f$ 在 $D$ 上单调非减（单调非增）。这四类函数统称为**单调函数**。

注意术语：本课程（与教材）的"单调增加"指严格增加；[1.2.3](/1.2.3#def-3.1.7) 中的"单调递增"指非减。单调性与区间有关：$\sin x$ 在 $\left[-\frac\pi2, \frac\pi2\right]$ 上单调增加，在 $\left[\frac\pi2, \frac{3\pi}2\right]$ 上单调减少，在 $\mathbb{R}$ 上不是单调函数。

**定义 1.2.4（周期函数）** 若存在 $T > 0$，使得对任意 $x \in D(f)$ 都有 $x + T \in D(f)$ 且 $f(x + T) = f(x)$，则称 $f$ 是以 $T$ 为周期的**周期函数**。

周期不唯一（$T$ 是周期，$2T, 3T, \dots$ 也是）。通常说的周期指最小正周期，但它不一定存在：常函数以任意正数为周期；下例中的函数以任意正有理数为周期。若 $f$ 的周期为 $T$，则 $f(ax + b)$（$a \ne 0$）的周期为 $\frac{T}{|a|}$。

**例 1.2.3** Dirichlet 函数（Dirichlet function）

$$
D(x) = \begin{cases} 1, & x \in \mathbb{Q}, \\ 0, & x \notin \mathbb{Q} \end{cases}
$$
就是 $\mathbb{Q}$ 的**集合的特征函数** $\chi_{\mathbb{Q}}$。对任意正有理数 $r$，$x$ 与 $x + r$ 同为有理数或同为无理数，故 $D(x + r) = D(x)$；正有理数没有最小者，所以 $D$ 没有最小正周期。它也是后面"处处不连续"（[第 3 章](/2.2.3)）和"不可积"（[第 7 章](/2.2.7)）的标准例子。

**定义 1.2.5（有界函数）** 设 $f$ 在集合 $D$ 上有定义。若存在 $M > 0$ 使得

$$
|f(x)| \leq M, \quad \forall x \in D,
$$
则称 $f$ 在 $D$ 上有界，或称 $f$ 为 $D$ 上的**有界函数**。若对任意 $M > 0$ 都存在 $x \in D$ 使 $|f(x)| > M$，则称 $f$ 在 $D$ 上无界。

$f$ 在 $D$ 上有界，等价于值域 $f(D)$ 包含在一个有限区间内。有界性也与集合有关：$\frac1x$ 在 $[1, +\infty)$ 上有界，在 $(0, 1)$ 上无界。

### 1.2.3. 反函数与复合函数

回顾 [1.2.3](/1.2.3#def-3.1.4)：映射 $f\colon X \to Y$ 称为**单射**，若 $x_1 \ne x_2$ 蕴涵 $f(x_1) \ne f(x_2)$；称为**满射**，若 $R(f) = Y$；既单又满称为**双射**。双射 $f$ 有逆映射 $f^{-1}\colon Y \to X$，它把 $y$ 映到唯一满足 $f(x) = y$ 的 $x$，并满足

$$
f^{-1} \circ f = \mathrm{id}_X, \qquad f \circ f^{-1} = \mathrm{id}_Y.
$$

**定义 1.2.6（反函数）** 设函数 $y = f(x)$ 是从定义域 $D(f)$ 到值域 $R(f)$ 的双射，则其逆映射 $x = f^{-1}(y)$，$y \in R(f)$，称为 $f$ 的**反函数**。按习惯把自变量写作 $x$，反函数记为 $y = f^{-1}(x)$，$x \in R(f)$。

- 点 $(a, b)$ 在 $y = f(x)$ 的图形上，当且仅当 $(b, a)$ 在 $y = f^{-1}(x)$ 的图形上，所以两者的图形关于直线 $y = x$ 对称。
- 严格单调的函数是到其值域的双射，因此有反函数，且反函数与原函数的单调性相同。这是构造反三角函数的方法：把三角函数限制在一个单调区间上再求反函数。

![函数与反函数的图形关于 y = x 对称：指数与对数、正弦与反正弦、正切与反正切。虚线连接一对对称点 (a, b) 与 (b, a)](./plots/inverse-functions.py)

指数函数 $y = a^x$（$a > 0$，$a \ne 1$）的反函数是对数函数 $y = \log_a x$；$a = \mathrm{e}$ 时记为 $\ln x$。三角函数是周期函数，不是双射，要先限制在一个单调区间上。

**定义 1.2.7（反三角函数）** 把 $\sin x$、$\cos x$、$\tan x$、$\cot x$ 分别限制在 $\left[-\frac\pi2, \frac\pi2\right]$、$[0, \pi]$、$\left(-\frac\pi2, \frac\pi2\right)$、$(0, \pi)$ 上，它们的反函数 $\arcsin x$、$\arccos x$、$\arctan x$、$\operatorname{arccot} x$ 统称为**反三角函数**。

它们的性质如下：

| 函数 | 由哪个限制得到 | 定义域 | 值域 | 奇偶性与单调性 |
|---|---|---|---|---|
| $\arcsin x$ | $\sin x$，$x \in \left[-\frac\pi2, \frac\pi2\right]$ | $[-1, 1]$ | $\left[-\frac\pi2, \frac\pi2\right]$ | 奇函数，单调增加 |
| $\arccos x$ | $\cos x$，$x \in [0, \pi]$ | $[-1, 1]$ | $[0, \pi]$ | 非奇非偶，单调减少 |
| $\arctan x$ | $\tan x$，$x \in \left(-\frac\pi2, \frac\pi2\right)$ | $\mathbb{R}$ | $\left(-\frac\pi2, \frac\pi2\right)$ | 奇函数，单调增加 |
| $\operatorname{arccot} x$ | $\cot x$，$x \in (0, \pi)$ | $\mathbb{R}$ | $(0, \pi)$ | 非奇非偶，单调减少 |

![四个反三角函数的图形：左图定义域为 [-1, 1]，右图定义域为整个实轴，虚线为值域的边界](./plots/inverse-trig.py)

反三角函数之间有以下常用关系：

1. $\arcsin x + \arccos x = \frac\pi2$，$x \in [-1, 1]$；
2. $\arctan x + \operatorname{arccot} x = \frac\pi2$，$x \in \mathbb{R}$；
3. $\arctan x + \arctan\frac1x = \frac\pi2 \operatorname{sgn} x$，$x \ne 0$（符号函数 $\operatorname{sgn}$ 见 §1.2.5）；
4. $\arctan x + \arctan y = \arctan\frac{x + y}{1 - xy}$，$xy < 1$；当 $xy > 1$ 时右边还要加上 $\pi$（$x > 0$）或 $-\pi$（$x < 0$）；
5. $|\arcsin x| \geq |x|$，$x \in [-1, 1]$；$|\arctan x| \leq |x|$，$x \in \mathbb{R}$。

关系 4 来自 $\tan(\alpha + \beta)$ 的和角公式：$\alpha = \arctan x$、$\beta = \arctan y$ 时 $\alpha + \beta \in (-\pi, \pi)$，而它落在 $\left(-\frac\pi2, \frac\pi2\right)$ 内恰当 $xy < 1$。

**定义 1.2.8（复合函数）** 设 $y = f(u)$，$u = g(x)$ 都是函数，且 $R(g) \cap D(f) \ne \varnothing$。称

$$
(f \circ g)(x) = f(g(x)), \quad x \in \{x \in D(g) \mid g(x) \in D(f)\}
$$
为 $f$ 与 $g$ 的**复合函数**，$u$ 称为中间变量。

例如 $y = (\sin x)^2$ 由 $y = u^2$、$u = \sin x$ 复合而成（$y - u - x$）；$y = 3^{\sin(x^2)}$ 由 $y = 3^u$、$u = \sin v$、$v = x^2$ 复合而成（$y - u - v - x$）。把复合函数拆成简单函数的链条，是[第 4 章](/2.2.4)链式法则的出发点。

**例 1.2.4** 设 $f(x) = \begin{cases} 3x, & 0 \leq x \leq 3, \\ x^2, & 3 < x \leq 5, \end{cases}$ $g(x) = \ln x$，求 $f(g(x))$ 与 $g(f(x))$。

**解** 按 $g(x)$ 落在 $f$ 的哪一段分段：$0 \leq \ln x \leq 3 \iff 1 \leq x \leq \mathrm{e}^3$，于是

$$
f(g(x)) = \begin{cases} 3\ln x, & 1 \leq x \leq \mathrm{e}^3, \\ (\ln x)^2, & \mathrm{e}^3 < x \leq \mathrm{e}^5; \end{cases}
\qquad
g(f(x)) = \begin{cases} \ln(3x), & 0 < x \leq 3, \\ 2\ln x, & 3 < x \leq 5. \end{cases}
$$
注意 $g(f(x))$ 的定义域要去掉使 $f(x) = 0$ 的 $x = 0$。

**例 1.2.5**（1） 设 $f\left(x + \frac1x\right) = x^2 + \frac1{x^2}$，求 $f(x)$。(2) 设 $f\left(\frac{x - 1}{x + 1}\right) = 3x$，求 $f(x)$。

**解** (1) 令 $u = x + \frac1x$，则 $x^2 + \frac1{x^2} = u^2 - 2$，故 $f(x) = x^2 - 2$。由于 $\left|x + \frac1x\right| \geq 2$，这里 $f$ 的定义域是 $|x| \geq 2$。(2) 令 $u = \frac{x - 1}{x + 1}$，解得 $x = \frac{1 + u}{1 - u}$，故 $f(x) = \frac{3(1 + x)}{1 - x}$，$x \ne 1$。

### 1.2.4. 初等函数

**定义 1.2.9（基本初等函数）** 以下六类函数称为**基本初等函数**：

1. 常函数 $f(x) = c$；
2. 幂函数 $f(x) = x^\alpha$（$\alpha \in \mathbb{R}$）；
3. 指数函数 $f(x) = a^x$（$a > 0$，$a \ne 1$）；
4. 对数函数 $f(x) = \log_a x$（$a > 0$，$a \ne 1$），包括 $\lg x$、$\ln x$；
5. 三角函数 $\sin x, \cos x, \tan x, \cot x, \sec x, \csc x$；
6. 反三角函数 $\arcsin x, \arccos x, \arctan x, \operatorname{arccot} x$。

**定义 1.2.10（初等函数）** 由基本初等函数经过有限次四则运算和有限次复合得到的函数称为**初等函数**。

幂函数 $x^\alpha$ 的定义域随 $\alpha$ 而变：$\alpha \in \mathbb{N}_+$ 时为 $\mathbb{R}$，$\alpha$ 为负整数时为 $\mathbb{R} \setminus \{0\}$，$\alpha$ 为无理数时取 $(0, +\infty)$（此时 $x^\alpha = \mathrm{e}^{\alpha\ln x}$）。在 $(0, +\infty)$ 上，$\alpha > 0$ 时 $x^\alpha$ 单调增加，$\alpha < 0$ 时单调减少。

三角函数的常用公式汇总如下，后面的求极限、求导与积分会反复用到（推导从略）：

| 类型 | 公式 |
|---|---|
| 平方关系 | $\sin^2 x + \cos^2 x = 1$，$1 + \tan^2 x = \sec^2 x$，$1 + \cot^2 x = \csc^2 x$ |
| 和角 | $\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$，$\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$，$\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}$ |
| 倍角 | $\sin 2x = 2\sin x\cos x$，$\cos 2x = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x$，$\tan 2x = \frac{2\tan x}{1 - \tan^2 x}$ |
| 三倍角 | $\sin 3x = 3\sin x - 4\sin^3 x$，$\cos 3x = 4\cos^3 x - 3\cos x$ |
| 半角（降幂） | $\sin^2\frac x2 = \frac{1 - \cos x}{2}$，$\cos^2\frac x2 = \frac{1 + \cos x}{2}$，$\tan\frac x2 = \frac{\sin x}{1 + \cos x} = \frac{1 - \cos x}{\sin x}$ |
| 万能公式（$t = \tan\frac x2$） | $\sin x = \frac{2t}{1 + t^2}$，$\cos x = \frac{1 - t^2}{1 + t^2}$，$\tan x = \frac{2t}{1 - t^2}$ |
| 积化和差 | $\sin\alpha\cos\beta = \frac12[\sin(\alpha + \beta) + \sin(\alpha - \beta)]$，$\cos\alpha\cos\beta = \frac12[\cos(\alpha + \beta) + \cos(\alpha - \beta)]$，$\sin\alpha\sin\beta = -\frac12[\cos(\alpha + \beta) - \cos(\alpha - \beta)]$ |
| 和差化积 | $\sin\alpha \pm \sin\beta = 2\sin\frac{\alpha \pm \beta}2\cos\frac{\alpha \mp \beta}2$，$\cos\alpha + \cos\beta = 2\cos\frac{\alpha + \beta}2\cos\frac{\alpha - \beta}2$，$\cos\alpha - \cos\beta = -2\sin\frac{\alpha + \beta}2\sin\frac{\alpha - \beta}2$ |
| 辅助角 | $a\sin x + b\cos x = \sqrt{a^2 + b^2}\,\sin(x + \varphi)$，其中 $\cos\varphi = \frac{a}{\sqrt{a^2 + b^2}}$，$\sin\varphi = \frac{b}{\sqrt{a^2 + b^2}}$（$a > 0$ 时 $\varphi = \arctan\frac ba$） |

初等函数的一个重要例子是双曲函数，它们由指数函数组合而成。

**定义 1.2.11（双曲函数）** 称

$$
\sinh x = \frac{\mathrm{e}^x - \mathrm{e}^{-x}}{2}, \qquad \cosh x = \frac{\mathrm{e}^x + \mathrm{e}^{-x}}{2}, \qquad \tanh x = \frac{\sinh x}{\cosh x} = \frac{\mathrm{e}^x - \mathrm{e}^{-x}}{\mathrm{e}^x + \mathrm{e}^{-x}}
$$
为双曲正弦、双曲余弦、双曲正切，并称 $\coth x = \frac{1}{\tanh x}$、$\operatorname{sech} x = \frac{1}{\cosh x}$、$\operatorname{csch} x = \frac{1}{\sinh x}$ 为双曲余切、双曲正割、双曲余割。它们统称为**双曲函数**。

| 函数 | 定义域 | 值域 | 奇偶性 | 反函数 |
|---|---|---|---|---|
| $\sinh x$ | $\mathbb{R}$ | $\mathbb{R}$ | 奇 | $\operatorname{arsinh} x = \ln\bigl(x + \sqrt{x^2 + 1}\bigr)$，$x \in \mathbb{R}$ |
| $\cosh x$ | $\mathbb{R}$ | $[1, +\infty)$ | 偶 | $\operatorname{arcosh} x = \ln\bigl(x + \sqrt{x^2 - 1}\bigr)$，$x \geq 1$（取 $[0, +\infty)$ 上的一支） |
| $\tanh x$ | $\mathbb{R}$ | $(-1, 1)$ | 奇 | $\operatorname{artanh} x = \frac12\ln\frac{1 + x}{1 - x}$，$|x| < 1$ |
| $\coth x$ | $\mathbb{R} \setminus \{0\}$ | $(-\infty, -1) \cup (1, +\infty)$ | 奇 | $\operatorname{arcoth} x = \frac12\ln\frac{x + 1}{x - 1}$，$|x| > 1$ |

双曲函数的恒等式与三角函数的平行，只差一些符号：

$$
\cosh^2 x - \sinh^2 x = 1, \qquad 1 - \tanh^2 x = \operatorname{sech}^2 x,
$$

$$
\sinh(x \pm y) = \sinh x\cosh y \pm \cosh x\sinh y, \qquad \cosh(x \pm y) = \cosh x\cosh y \pm \sinh x\sinh y,
$$

$$
\sinh 2x = 2\sinh x\cosh x, \qquad \cosh 2x = \cosh^2 x + \sinh^2 x.
$$

第一个恒等式说明点 $(\cosh t, \sinh t)$ 在双曲线 $x^2 - y^2 = 1$ 的右支上，正如 $(\cos t, \sin t)$ 在单位圆上，"双曲"之名由此而来；参数 $t$ 恰是对应扇形面积的两倍（扇形面积可在[第 7 章](/2.2.7)学过定积分后验证）。

![左：双曲函数的图形，cosh x 与 sinh x 在 x 较大时都接近 e^x/2；右：单位圆与单位双曲线上的参数点，两块阴影扇形的面积都是 t/2](./plots/hyperbolic-functions.py)

### 1.2.5. 非初等函数

不是初等函数的函数在微积分中同样常见，主要有三类。

分段函数是在定义域的不同部分用不同表达式给出的函数。分段函数可能是初等函数（如 $|x| = \sqrt{x^2}$），也可能不是。

**定义 1.2.12（符号函数）** 称

$$
\operatorname{sgn} x = \begin{cases} 1, & x > 0, \\ 0, & x = 0, \\ -1, & x < 0 \end{cases}
$$
为**符号函数**。对任意 $x$ 有 $x = |x|\operatorname{sgn} x$。

**定义 1.2.13（取整函数）** 对 $x \in \mathbb{R}$，称不超过 $x$ 的最大整数为 $x$ 的整数部分，记为 $\lfloor x \rfloor$：

$$
\lfloor x \rfloor = n, \quad n \leq x < n + 1, \ n \in \mathbb{Z}.
$$
函数 $y = \lfloor x \rfloor$ 称为**取整函数**。

由定义 $x - 1 < \lfloor x \rfloor \leq x$，这个不等式在用夹逼法求极限时很有用（[第 2 章](/2.2.2#sec-2.4.3)）。例如 $\lfloor 2.5 \rfloor = 2$，$\lfloor -2.5 \rfloor = -3$。取整函数在每个整数点处"跳跃"，是第一类间断点的典型例子（[第 3 章](/2.2.3)）。

隐函数中，自变量与因变量的关系由方程 $F(x, y) = 0$ 给出，而不是由 $y = f(x)$ 直接给出。

**定义 1.2.14（隐函数）** 设 $D \subseteq \mathbb{R}$ 非空。若对每个 $x \in D$，方程 $F(x, y) = 0$ 都有唯一的解 $y$，则由此确定的函数 $y = y(x)$，$x \in D$，称为由方程 $F(x, y) = 0$ 确定的**隐函数**。

一个方程不一定确定唯一的函数：$x^2 + y^2 = 1$ 在 $y \geq 0$ 与 $y \leq 0$ 的限制下分别确定 $y = \sqrt{1 - x^2}$ 和 $y = -\sqrt{1 - x^2}$。隐函数何时存在、是否可导，是多元微积分中隐函数定理（[2.2.10](/2.2.10)）回答的问题。

**例 1.2.6** 方程 $2^y = xy + 2$ 在 $x < 0$ 时是否确定 $y$ 是 $x$ 的函数？

**解** 固定 $x_0 < 0$，在 $(y, u)$ 平面上考察曲线 $u = 2^y$ 与直线 $u = x_0 y + 2$。前者单调增加且取遍 $(0, +\infty)$，后者单调减少且取遍 $\mathbb{R}$，两者恰有一个交点 $(y_0, u_0)$。因此对每个 $x_0 < 0$，方程恰有唯一解 $y_0$，方程在 $(-\infty, 0)$ 上确定了一个隐函数。

参数方程表示的函数形如

$$
\begin{cases} x = x(t), \\ y = y(t), \end{cases} \quad t \in I.
$$
例如椭圆的参数方程为 $x = a\cos\theta$，$y = b\sin\theta$（$a, b > 0$，$0 \leq \theta < 2\pi$）；只取 $0 \leq \theta \leq \pi$ 得到上半椭圆，它确定函数 $y = \frac ba\sqrt{a^2 - x^2}$，$x \in [-a, a]$。若 $x(t)$ 严格单调，参数方程就确定了函数 $y = y\bigl(x^{-1}(x)\bigr)$，其求导法则见[第 4 章](/2.2.4)。

## 小结

| 内容 | 要点 |
|---|---|
| 邻域 | $N(x_0, \delta) = (x_0 - \delta, x_0 + \delta)$，去心邻域 $N^*(x_0, \delta)$ 去掉中心 |
| 确界存在定理 | 非空有上界的实数集必有上确界（实数的完备性，作为公理） |
| 确界的刻画 | $b = \sup E \iff$ $b$ 是上界，且 $\forall \varepsilon > 0$，$\exists x \in E$，$x > b - \varepsilon$ |
| Archimedes 性质、稠密性 | $\forall p, q > 0$，$\exists N$，$Np > q$；任意开区间都含有理数 |
| 函数的属性 | 奇偶（定义域对称）、单调（与区间有关）、周期（不一定有最小正周期）、有界（与集合有关） |
| 反函数 | 双射才有反函数；图形关于 $y = x$ 对称；严格单调函数有同样单调的反函数 |
| 初等函数 | 六类基本初等函数经有限次四则运算与复合；双曲函数 $\cosh^2 x - \sinh^2 x = 1$ |
| 非初等函数 | 分段函数（$\operatorname{sgn} x$、$\lfloor x \rfloor$、Dirichlet 函数）、隐函数、参数方程 |
