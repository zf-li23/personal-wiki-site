---
title: 收敛性
---

概率论的主线是：概率空间 $(\Omega, \mathcal{F}, \mathbb{P})$ → 随机变量（向量）及其分布 → 数字特征 → 随机变量序列的极限 $X_n \to\ ?$。前两章的**大数定律**与**中心极限定理**分别用到依概率收敛、几乎处处收敛与依分布收敛，本章跳出这两个具体的定理，对一般的随机变量序列系统地讨论各种收敛模式：它们的定义、相互之间的强弱关系、说明差异的反例，以及在统计中反复使用的几个收敛性定理——连续映射定理、Slutsky 定理、Delta 方法与特征函数的连续性定理。这些工具是统计推断中大样本理论（[3.2.2](/3.2.2)、[3.2.3](/3.2.3)）的基础。

## 14.1. 收敛性定义

设 $(\Omega, \mathcal{F}, \mathbb{P})$ 是概率空间，$X_n$ 和 $X$ 是其上的随机变量，分布函数分别为 $F_n(x) = \mathbb{P}(X_n \le x)$ 与 $F(x) = \mathbb{P}(X \le x)$。各种收敛模式都从数列的收敛出发：$\lim_n a_n = a$ 是指对任意 $\varepsilon > 0$，存在正整数 $N$，使得 $n \ge N$ 时 $\lvert a_n - a \rvert \le \varepsilon$。区别在于先用什么方式把随机性去掉、得到一个数列。

**定义 14.1.1（依分布收敛）** 如果在 $F(x)$ 的每个连续点 $x$ 处都有 $\lim_{n \to \infty} F_n(x) = F(x)$，则称 $X_n$ **依分布收敛**到 $X$，记作 $X_n \xrightarrow{d} X$；也称 $F_n$ 弱收敛到 $F$，记作 $F_n \xrightarrow{w} F$。

**定义 14.1.2（几乎处处收敛）** 如果 $\mathbb{P}\left(\lim_{n \to \infty} X_n = X\right) = 1$，则称 $X_n$ **几乎处处收敛**到 $X$，记作 $X_n \xrightarrow{\text{a.s.}} X$ 或 $X_n \to X$ a.s.。

对任意 $\varepsilon > 0$，记 $A_n = \{\lvert X_n - X \rvert < \varepsilon\}$，由数列极限的定义，

$$
\left\{\lim_{n \to \infty} X_n = X\right\} = \left\{\omega\colon \lim_{n \to \infty} X_n(\omega) = X(\omega)\right\} \subset \bigcup_{n=1}^{\infty}\bigcap_{k=n}^{\infty}\{\lvert X_k - X \rvert < \varepsilon\} = \liminf_{n \to \infty} A_n. \tag{14.1}
$$
这里是"包含于"而不是"等于"：左边要求对所有 $\varepsilon > 0$ 都从某项起偏差小于 $\varepsilon$，右边只对一个 $\varepsilon$。事件列的下极限 $\liminf_n A_n$ 的直观意义是"从某时刻起 $A_n$ 一直发生"（定义 2.2.1），与数列极限"从某时刻起偏差都在控制范围内"恰好对应。

**定义 14.1.3（依概率收敛）** 如果对任意 $\varepsilon > 0$，$\lim_{n \to \infty} \mathbb{P}(\lvert X_n - X \rvert \ge \varepsilon) = 0$，则称 $X_n$ **依概率收敛**到 $X$，记作 $X_n \xrightarrow{p} X$。

由 $\mathbb{P}(\lvert X_n - X \rvert \ge \varepsilon) = \mathbb{P}(A_n^{\mathsf c}) = 1 - \mathbb{P}(A_n)$，$X_n \xrightarrow{p} X$ 当且仅当对每个 $\varepsilon > 0$，$\lim_n \mathbb{P}(A_n) = 1$。

**定义 14.1.4（r 阶矩收敛）** 设 $r > 0$，$\mathbb{E}\lvert X_n \rvert^r < \infty$，$\mathbb{E}\lvert X \rvert^r < \infty$。如果 $\lim_{n \to \infty} \mathbb{E}\lvert X_n - X \rvert^r = 0$，则称 $X_n$ **r 阶矩收敛**到 $X$，也称在 $L^r$ 中收敛，记作 $X_n \xrightarrow{L^r} X$。

例如 $\lim_n \mathbb{E}\lvert X_n - X \rvert = 0 \Leftrightarrow X_n \xrightarrow{L^1} X$；$r = 2$ 时称为均方收敛。

四种收敛模式的对照如下，各列给出判断收敛时"先固定什么"：

| | 依分布收敛 | 依概率收敛 | 几乎处处收敛 | $r$ 阶矩收敛 |
|---|---|---|---|---|
| 记号 | $X_n \xrightarrow{d} X$ | $X_n \xrightarrow{p} X$ | $X_n \xrightarrow{\text{a.s.}} X$ | $X_n \xrightarrow{L^r} X$ |
| 定义 | $F$ 的连续点处 $F_n(x) \to F(x)$ | $\forall \varepsilon > 0$，$\mathbb{P}(\lvert X_n - X \rvert \ge \varepsilon) \to 0$ | $\mathbb{P}(\lim X_n = X) = 1$ | $\mathbb{E}\lvert X_n - X \rvert^r \to 0$ |
| 判断步骤 | 固定 $x$，看数列 $F_n(x)$ 是否收敛；再对 $F$ 的所有连续点检查 | 固定 $n$，得到集合 $\{\lvert X_n - X \rvert \ge \varepsilon\}$ 的概率；再看这个数列是否趋于 $0$ | 固定 $\omega$，看数列 $X_n(\omega)$ 是否收敛；再看收敛的 $\omega$ 的集合概率是否为 $1$ | 固定 $n$，计算期望；再看数列是否趋于 $0$ |
| 比较的对象 | 分布（整体），用分布函数或特征函数刻画 | $X_n(\omega) - X(\omega)$ 的细节：关心大偏差是否出现，不关心大偏差具体多大 | 同左 | 还关心大偏差具体有多大（因为要求期望） |

依分布收敛只涉及分布，$X_n$ 与 $X$ 甚至可以定义在不同的概率空间上；其他三种收敛比较的是同一个 $\omega$ 上 $X_n(\omega)$ 与 $X(\omega)$ 的取值。

## 14.2. 收敛性关系

各种收敛之间的关系如下：

```mermaid
flowchart LR
  AS["几乎处处收敛 a.s."] --> P["依概率收敛 p"]
  LR["r 阶矩收敛 L^r"] --> P
  P --> D["依分布收敛 d"]
```

依分布收敛是其中最弱的一种，这也是它被称为"弱收敛"的原因。

**定理 14.2.1** 如果 $X_n \xrightarrow{\text{a.s.}} X$，则 $X_n \xrightarrow{p} X$。

**证明** 对任意 $\varepsilon > 0$，由式 (14.1) 与 $\mathbb{P}(\lim X_n = X) = 1$，$\mathbb{P}\left(\bigcup_{n}\bigcap_{k \ge n}\{\lvert X_k - X \rvert < \varepsilon\}\right) = 1$。利用概率的连续性（定理 2.2.1），

$$
\begin{aligned}
\lim_{n \to \infty}\mathbb{P}(\lvert X_n - X \rvert \ge \varepsilon) &\le \lim_{n \to \infty}\mathbb{P}\left(\bigcup_{k=n}^{\infty}\{\lvert X_k - X \rvert \ge \varepsilon\}\right) = \mathbb{P}\left(\bigcap_{n=1}^{\infty}\bigcup_{k=n}^{\infty}\{\lvert X_k - X \rvert \ge \varepsilon\}\right) \\
&= 1 - \mathbb{P}\left(\bigcup_{n=1}^{\infty}\bigcap_{k=n}^{\infty}\{\lvert X_k - X \rvert < \varepsilon\}\right) = 1 - 1 = 0. \quad \square
\end{aligned}
$$

**定理 14.2.2** 如果 $X_n \xrightarrow{L^r} X$，则 $X_n \xrightarrow{p} X$。

**证明** 对任意 $\varepsilon > 0$，由 Markov 不等式（定理 8.5.1），$\mathbb{P}(\lvert X_n - X \rvert \ge \varepsilon) \le \frac{1}{\varepsilon^r}\mathbb{E}\lvert X_n - X \rvert^r \to 0$。 $\square$

**定理 14.2.3** 如果 $X_n \xrightarrow{p} X$，则 $X_n \xrightarrow{d} X$。

**证明** 对任意 $\varepsilon > 0$，

$$
\begin{aligned}
F_n(x) &= \mathbb{P}(X_n \le x, \lvert X_n - X \rvert \le \varepsilon) + \mathbb{P}(X_n \le x, \lvert X_n - X \rvert > \varepsilon) \\
&\le \mathbb{P}(X \le x + \varepsilon) + \mathbb{P}(\lvert X_n - X \rvert > \varepsilon) = F(x + \varepsilon) + \mathbb{P}(\lvert X_n - X \rvert > \varepsilon).
\end{aligned}
$$
另一方面，

$$
\begin{aligned}
F_n(x) = 1 - \mathbb{P}(X_n > x) &= 1 - \mathbb{P}(X_n > x, \lvert X_n - X \rvert \le \varepsilon) - \mathbb{P}(X_n > x, \lvert X_n - X \rvert > \varepsilon) \\
&\ge 1 - \mathbb{P}(X > x - \varepsilon) - \mathbb{P}(\lvert X_n - X \rvert > \varepsilon) = F(x - \varepsilon) - \mathbb{P}(\lvert X_n - X \rvert > \varepsilon),
\end{aligned}
$$
其中用到 $\{X_n > x, \lvert X_n - X \rvert \le \varepsilon\} \subset \{X > x - \varepsilon\}$。因此

$$
F(x - \varepsilon) - \mathbb{P}(\lvert X_n - X \rvert > \varepsilon) \le F_n(x) \le F(x + \varepsilon) + \mathbb{P}(\lvert X_n - X \rvert > \varepsilon).
$$
令 $n \to \infty$，得 $F(x - \varepsilon) \le \liminf_n F_n(x) \le \limsup_n F_n(x) \le F(x + \varepsilon)$。若 $F$ 在 $x$ 处连续，令 $\varepsilon \downarrow 0$，$F(x - \varepsilon) \uparrow F(x)$，$F(x + \varepsilon) \downarrow F(x)$，所以 $\lim_n F_n(x) = F(x)$，即 $X_n \xrightarrow{d} X$。 $\square$

## 14.3. 反例

下面的反例说明上述蕴含关系一般不能反过来，从而可以直观地感受各种收敛的差异。

**例 14.3.1（依分布收敛不蕴含依概率收敛）** 设 $\{X_n\}$ 独立同分布于 $\mathcal{N}(0, 1)$，则 $X_n$ 与 $X_1$ 同分布，显然 $X_n \xrightarrow{d} X_1$。但 $n \ne 1$ 时 $X_n - X_1 \sim \mathcal{N}(0, 2)$，$\frac{X_n - X_1}{\sqrt{2}}$ 与 $X_1$ 同分布，从而

$$
\mathbb{P}(\lvert X_n - X_1 \rvert > 1) = \mathbb{P}\left(\left\lvert \frac{X_n - X_1}{\sqrt{2}} \right\rvert > \frac{1}{\sqrt{2}}\right) = \mathbb{P}\left(\lvert X_1 \rvert > \frac{1}{\sqrt{2}}\right) > 0
$$
不随 $n$ 变化，$X_n$ 不依概率收敛到 $X_1$。依分布收敛只说分布越来越像，不说取值越来越近。

极限是常数时，情况不同。

**例 14.3.2** 设 $C$ 为常数，则 $X_n \xrightarrow{d} C \Leftrightarrow X_n \xrightarrow{p} C$。

**证明** "$\Leftarrow$"是定理 14.2.3。"$\Rightarrow$"：常数 $C$ 的分布函数 $F(x) = \boldsymbol{1}_{\{x \ge C\}}$ 只在 $x = C$ 处不连续。对任意 $\varepsilon > 0$，$C - \varepsilon$ 与 $C + \varepsilon/2$ 都是连续点，所以

$$
\mathbb{P}(\lvert X_n - C \rvert \ge \varepsilon) \le F_n(C - \varepsilon) + 1 - F_n(C + \varepsilon/2) \to 0 + 1 - 1 = 0. \quad \square
$$

**例 14.3.3（依概率收敛不蕴含 $r$ 阶矩收敛）** 取概率空间为一维几何概型 $((0, 1), \mathcal{B}((0, 1)), \lambda)$，$\lambda$ 为长度。定义

$$
X_n(\omega) = \begin{cases} n, & \omega \in (0, n^{-r}], \\ 0, & \omega \in (n^{-r}, 1), \end{cases} \tag{14.2}
$$
且 $X \equiv 0$。对任意 $\varepsilon > 0$，$n > \varepsilon$ 时 $\mathbb{P}(\lvert X_n - 0 \rvert > \varepsilon) = \mathbb{P}(X_n = n) = \lambda((0, n^{-r}]) = n^{-r} \to 0$，所以 $X_n \xrightarrow{p} 0$；但 $\mathbb{E}\lvert X_n - 0 \rvert^r = n^r \cdot n^{-r} = 1$，$X_n$ 不 $r$ 阶矩收敛到 $0$。偏差出现的概率趋于 $0$，但偏差的大小增长得足够快，期望不趋于 $0$。

**例 14.3.4（$r$ 阶矩收敛不蕴含更高阶矩收敛）** 设 $0 < r < q$，在同一概率空间上令 $X_n = n\boldsymbol{1}_{(0, n^{-q}]}$，则 $\mathbb{E}\lvert X_n \rvert^r = n^{r - q} \to 0$，但 $\mathbb{E}\lvert X_n \rvert^q = 1$。所以 $X_n \xrightarrow{L^r} 0$，$X_n$ 不 $q$ 阶矩收敛到 $0$。（反方向成立：由 **Jensen 不等式**，$L^q$ 收敛蕴含 $L^r$ 收敛。）

**例 14.3.5（几乎处处收敛不蕴含 $r$ 阶矩收敛）** 取式 (14.2) 中的 $X_n$。对每个 $\omega \in (0, 1)$，当 $n$ 足够大使 $n^{-r} < \omega$ 时 $X_n(\omega) = 0$，所以对一切 $\omega$ 有 $X_n(\omega) \to 0$，$X_n \xrightarrow{\text{a.s.}} 0$；但 $\mathbb{E}\lvert X_n \rvert^r = 1$。

**例 14.3.6（$r$ 阶矩收敛与依概率收敛都不蕴含几乎处处收敛）** 设 $\{X_n\}$ 独立，$\mathbb{P}(X_n = 0) = 1 - n^{-1}$，$\mathbb{P}(X_n = 1) = n^{-1}$。则 $\mathbb{E}\lvert X_n \rvert = n^{-1} \to 0$，$X_n \xrightarrow{L^1} 0$，从而 $X_n \xrightarrow{p} 0$。但令 $A_n = \{X_n = 1\}$，$\{A_n\}$ 相互独立且

$$
\sum_{n=1}^{\infty}\mathbb{P}(A_n) = \sum_{n=1}^{\infty}\frac{1}{n} = \infty,
$$
由 Borel–Cantelli 引理的第二部分（定理 3.1.2），"$A_n$ 发生无穷多次"的概率为 $1$，即几乎每条样本轨道上 $X_n = 1$ 无穷多次，$X_n$ 不几乎处处收敛到 $0$。

不借助独立性，也可以在几何概型上直接构造依概率收敛但处处不收敛的序列。

**例 14.3.7** 在 $\Omega = [0, 1]$ 的几何概型上，令 $Y \equiv 0$，把 $[0, 1]$ 依次等分为 $2, 3, 4, \dots$ 段，$Y_n$ 依次取每一小段的示性函数：$Y_1 = \boldsymbol{1}_{[0, 1/2]}$，$Y_2 = \boldsymbol{1}_{[1/2, 1]}$，$Y_3 = \boldsymbol{1}_{[0, 1/3]}$，$Y_4 = \boldsymbol{1}_{[1/3, 2/3]}$，$Y_5 = \boldsymbol{1}_{[2/3, 1]}$，依此类推。属于第 $m$ 轮（等分为 $m$ 段）的 $Y_n$ 满足 $\mathbb{P}(Y_n \ne 0) = 1/m \to 0$，所以 $Y_n \xrightarrow{p} 0$；但每一轮中每个 $\omega$ 都落入某一小段，$Y_n(\omega) = 1$ 对无穷多个 $n$ 成立，同时 $Y_n(\omega) = 0$ 也对无穷多个 $n$ 成立，数列 $Y_n(\omega)$ 对每个 $\omega$ 都不收敛。

此例的直观启示：$Y_n \xrightarrow{\text{a.s.}} Y$ 要求在几乎每个 $\omega$ 上数列 $Y_n(\omega)$ 都收敛到 $Y(\omega)$；$Y_n \xrightarrow{p} Y$ 可以允许每个 $\omega$ 上数列都不收敛，只要偏离出现的范围越来越小，即偏离区域的概率收敛到 $0$。注意收敛定义中的 $Y$ 是一般的随机变量，这里取常数只是为了简单。

![例 14.3.7 的"滑动区间"序列：每一行是一个 Y_n 取 1 的区间，宽度 1/m 趋于 0，但每个 omega（竖线）被无穷多次覆盖](./plots/typewriter-sequence.py)

## 14.4. 常用定理

以下几个定理是今后（包括其他课程中）经常用到的工具，要求知道结论、会用。

**定理 14.4.1（连续映射定理）** 设 $X, X_n$ 是随机变量（或随机向量），$g$ 是连续函数，则

1. $X_n \xrightarrow{\text{a.s.}} X \Rightarrow g(X_n) \xrightarrow{\text{a.s.}} g(X)$；
2. $X_n \xrightarrow{p} X \Rightarrow g(X_n) \xrightarrow{p} g(X)$；
3. $X_n \xrightarrow{d} X \Rightarrow g(X_n) \xrightarrow{d} g(X)$。

第 1 条由连续函数保持数列极限直接得到。第 3 条要用到依分布收敛的一个等价刻画：$X_n \xrightarrow{d} X$ 当且仅当对一切有界连续函数 $h$，$\mathbb{E}h(X_n) \to \mathbb{E}h(X)$；对每个 $t$ 取 $h(x) = \mathrm{e}^{\mathrm{i}tg(x)}$（分别取实部与虚部），得 $g(X_n)$ 的特征函数逐点收敛到 $g(X)$ 的特征函数，再用连续性定理。对 $r$ 阶矩收敛，类似的结论不成立：在式 (14.2) 的概率空间上令 $X_n = n^{1/(2r)}\boldsymbol{1}_{(0, 1/n]}$，则 $\mathbb{E}\lvert X_n \rvert^r = n^{-1/2} \to 0$，但 $g(x) = x^2$ 时 $\mathbb{E}\lvert g(X_n) \rvert^r = 1$。

**定理 14.4.2（Slutsky 定理）** 设 $X_n \xrightarrow{d} X$，$Y_n \xrightarrow{d} c$（$c$ 为常数，由例 14.3.2 等价于 $Y_n \xrightarrow{p} c$），则

1. $X_n + Y_n \xrightarrow{d} X + c$；
2. $X_n Y_n \xrightarrow{d} cX$；
3. $X_n / Y_n \xrightarrow{d} X/c$（$c \ne 0$）。

**证明** 方法一：逐条证明。以第 1 条为例，设 $x$ 是 $X + c$ 的分布函数 $F_{X+c}(y) = F_X(y - c)$ 的连续点，对 $\varepsilon > 0$ 使 $x - c \pm \varepsilon$ 是 $F_X$ 的连续点，

$$
\mathbb{P}(X_n + Y_n \le x) \le \mathbb{P}(X_n \le x - c + \varepsilon) + \mathbb{P}(\lvert Y_n - c \rvert > \varepsilon) \to F_X(x - c + \varepsilon),
$$

$$
\mathbb{P}(X_n + Y_n \le x) \ge \mathbb{P}(X_n \le x - c - \varepsilon) - \mathbb{P}(\lvert Y_n - c \rvert > \varepsilon) \to F_X(x - c - \varepsilon),
$$
再令 $\varepsilon \downarrow 0$（沿 $F_X$ 的连续点）即得。第 2、3 条类似。

方法二（耦合）：先证明 $(X_n, Y_n) \xrightarrow{d} (X, c)$（随机向量的依分布收敛，可用联合特征函数验证），再对 $g(x, y) = x + y$、$xy$、$x/y$ 应用连续映射定理。 $\square$

**例 14.4.1（$t$ 分布收敛到正态分布）** 设 $T_n = Z/\sqrt{V_n/n}$，其中 $Z \sim \mathcal{N}(0, 1)$ 与 $V_n \sim \chi^2_n$ 独立，即 $T_n \sim t_n$（**t 分布**，定义 7.1.2）。把 $V_n$ 写成 $n$ 个独立 $\mathcal{N}(0, 1)$ 的平方和，由大数定律 $V_n/n \xrightarrow{p} \mathbb{E}Z^2 = 1$，由连续映射定理 $\sqrt{V_n/n} \xrightarrow{p} 1$。又 $Z \xrightarrow{d} Z$，由 Slutsky 定理，

$$
T_n = \frac{Z}{\sqrt{V_n/n}} \xrightarrow{d} \mathcal{N}(0, 1), \quad n \to \infty.
$$
同样的论证说明：用样本标准差代替总体标准差，$\sqrt{n}(\bar X - \mu)/S$ 仍渐近服从标准正态分布，这是大样本置信区间的依据。

![t_n 的密度（n = 1, 3, 10, 30）收敛到标准正态密度](./plots/t-to-normal.py)

**定理 14.4.3（Delta 方法）** 设 $\sqrt{n}(X_n - a) \xrightarrow{d} \mathcal{N}(0, V)$，$g\colon \mathbb{R} \to \mathbb{R}$ 是连续可导函数，则

$$
\sqrt{n}\left(g(X_n) - g(a)\right) \xrightarrow{d} \mathcal{N}\left(0, (g'(a))^2 V\right).
$$

**证明** 由 Slutsky 定理，$X_n - a = \frac{1}{\sqrt{n}} \cdot \sqrt{n}(X_n - a) \xrightarrow{d} 0$，即 $X_n \xrightarrow{p} a$。由中值定理，$g(X_n) - g(a) = g'(\xi_n)(X_n - a)$，$\xi_n$ 介于 $X_n$ 与 $a$ 之间，所以 $\xi_n \xrightarrow{p} a$；$g'$ 连续，由连续映射定理 $g'(\xi_n) \xrightarrow{p} g'(a)$。再由 Slutsky 定理，

$$
\sqrt{n}(g(X_n) - g(a)) = g'(\xi_n) \cdot \sqrt{n}(X_n - a) \xrightarrow{d} g'(a) \cdot \mathcal{N}(0, V) = \mathcal{N}(0, (g'(a))^2 V). \quad \square
$$

Delta 方法是统计推断中的常用定理：已知估计量的渐近正态性，就能得到它的光滑函数的渐近正态性。$g'(a) = 0$ 时极限退化为 $0$，需要用二阶展开。

**例 14.4.2** 设 $X_i \overset{\text{iid}}{\sim} \mathrm{Ber}(p)$，$0 < p < 1$，$\bar X_n$ 是**样本均值**。由中心极限定理，$\sqrt{n}(\bar X_n - p) \xrightarrow{d} \mathcal{N}(0, p(1-p))$。对 $g(x) = x(1 - x)$（方差的估计），$g'(p) = 1 - 2p$，由 Delta 方法，$p \ne \frac{1}{2}$ 时

$$
\sqrt{n}\left(\bar X_n(1 - \bar X_n) - p(1 - p)\right) \xrightarrow{d} \mathcal{N}\left(0, (1 - 2p)^2 p(1 - p)\right).
$$

连续性定理（定理 11.3.6）把依分布收敛转化为特征函数的逐点收敛，是概率论中最常用、最重要的定理之一。概率母函数、矩母函数在满足唯一性的条件下，也可以代替特征函数用于连续性定理。

**例 14.4.3** 用连续性定理可以证明 Khinchin 大数定律（定理 12.3.2，证明见 [3.1.13](/3.1.13) 定理 13.1.1 之后），以及二项分布的 Poisson 近似：设 $X_n \sim \mathrm{Bin}(n, p_n)$，$np_n = \lambda$，则 $X_n$ 的特征函数

$$
\left(1 - p_n + p_n\mathrm{e}^{\mathrm{i}t}\right)^n = \left(1 + \frac{\lambda(\mathrm{e}^{\mathrm{i}t} - 1)}{n}\right)^n \to \mathrm{e}^{\lambda(\mathrm{e}^{\mathrm{i}t} - 1)},
$$
后者是 $\mathrm{Poi}(\lambda)$ 的特征函数，所以 $X_n \xrightarrow{d} \mathrm{Poi}(\lambda)$。

对随机向量，依分布收敛（联合分布函数在极限的连续点处收敛）同样可以借助特征函数判断。

**定理 14.4.4** 设随机向量 $\boldsymbol{X}_n$ 的特征函数 $\varphi_n(\boldsymbol{t})$ 逐点收敛到一个在 $\boldsymbol{t} = \boldsymbol{0}$ 处连续的函数 $\varphi(\boldsymbol{t})$，则 $\varphi(\boldsymbol{t})$ 是某个随机向量 $\boldsymbol{X}$ 的特征函数，并且对任何常数向量 $\boldsymbol{a}$，$\boldsymbol{a}^{\mathsf T}\boldsymbol{X}_n \xrightarrow{d} \boldsymbol{a}^{\mathsf T}\boldsymbol{X}$。

**推论 14.4.1** 设随机变量 $X_n$ 的特征函数 $\varphi_n(t)$ 逐点收敛到一个在 $t = 0$ 处连续的函数 $\varphi(t)$，则 $\varphi(t)$ 是某个随机变量 $X$ 的特征函数，并且 $X_n \xrightarrow{d} X$。

推论 14.4.1 不需要事先知道极限分布是什么；"在 $0$ 处连续"不能去掉：例如 $X_n \sim \mathcal{N}(0, n)$ 的特征函数 $\mathrm{e}^{-nt^2/2}$ 收敛到 $\boldsymbol{1}_{\{t = 0\}}$，它在 $0$ 处不连续，$X_n$ 的分布"漏到无穷远"，不依分布收敛到任何随机变量。

**引理 14.4.1（Cramér–Wold 定理）** 设 $\boldsymbol{X}, \boldsymbol{Y}$ 都是 $p$ 维随机向量，则 $\boldsymbol{X}, \boldsymbol{Y}$ 同分布的充分必要条件是对任何常数向量 $\boldsymbol{a} \in \mathbb{R}^p$，$\boldsymbol{a}^{\mathsf T}\boldsymbol{X}$ 与 $\boldsymbol{a}^{\mathsf T}\boldsymbol{Y}$ 同分布。

**证明** 必要性显然。充分性：$\boldsymbol{X}$ 的特征函数 $\varphi_{\boldsymbol{X}}(\boldsymbol{a}) = \mathbb{E}\mathrm{e}^{\mathrm{i}\boldsymbol{a}^{\mathsf T}\boldsymbol{X}} = \varphi_{\boldsymbol{a}^{\mathsf T}\boldsymbol{X}}(1) = \varphi_{\boldsymbol{a}^{\mathsf T}\boldsymbol{Y}}(1) = \varphi_{\boldsymbol{Y}}(\boldsymbol{a})$ 对一切 $\boldsymbol{a}$ 成立，由特征函数的唯一性即得。 $\square$

**定理 14.4.5** 设随机向量序列 $\{\boldsymbol{X}_n\}$ 与随机向量 $\boldsymbol{X}$ 的维数相同，则 $\boldsymbol{X}_n \xrightarrow{d} \boldsymbol{X}$ 的充分必要条件是对任何常数向量 $\boldsymbol{a}$，$\boldsymbol{a}^{\mathsf T}\boldsymbol{X}_n \xrightarrow{d} \boldsymbol{a}^{\mathsf T}\boldsymbol{X}$。

这称为 Cramér–Wold 方法：向量的问题都可以转化为一维的问题。它是随机向量的中心极限定理（[3.1.15](/3.1.15)）的出发点。

## 小结

- 四种收敛：依分布（比较分布函数在连续点的值）、依概率（$\mathbb{P}(\lvert X_n - X \rvert \ge \varepsilon) \to 0$）、几乎处处（$\mathbb{P}(\lim X_n = X) = 1$）、$r$ 阶矩（$\mathbb{E}\lvert X_n - X \rvert^r \to 0$）。
- 强弱关系：a.s. $\Rightarrow$ p $\Rightarrow$ d，$L^r \Rightarrow$ p；极限为常数时 d $\Leftrightarrow$ p。其他方向都有反例：独立同分布正态序列（d 不推 p）、$n\boldsymbol{1}_{(0, n^{-r}]}$（a.s. 与 p 都不推 $L^r$）、独立的 $\mathrm{Ber}(1/n)$ 序列与滑动区间序列（p 与 $L^r$ 都不推 a.s.）。
- 常用定理：连续映射定理（一列变量，任意连续函数）、Slutsky 定理（两列变量，四则运算）、Delta 方法（光滑函数的渐近正态性）、连续性定理（连接分布函数与特征函数）、Cramér–Wold 方法（向量化为一维）。
- 技巧：用反例理解相似概念的差异；利用熟知的概念（数列的收敛）理解新概念（随机变量的收敛）。
