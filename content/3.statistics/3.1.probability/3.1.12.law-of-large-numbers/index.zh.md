---
title: 大数定律
---

疫苗研发要做临床试验：随机招募 $n$ 位受试者，第 $i$ 位受试者有效记 $X_i = 1$、无效记 $X_i = 0$，$X_1, X_2, \dots$ 独立同分布，$\mathbb{P}(X_i = 1) = p$。我们只能观察到试验中的有效比例 $\frac{1}{n}\sum_{i=1}^{n} X_i$（**样本均值**），想知道的却是整个人群的有效比例 $p = \mathbb{E}X_1$（总体均值）。样本均值能否可靠地估计总体均值？大数定律（law of large numbers）回答了这个问题：在相当一般的条件下，独立同分布随机变量的算术平均当 $n \to \infty$ 时收敛到期望。它是"频率稳定于概率"的数学表述，连接了单次试验的偶然性与大量重复的必然性，也是统计推断（[3.2](/3.2)）与随机模拟的理论依据。

本章先引入刻画随机变量序列极限的两种收敛模式，再给出弱大数定律与强大数定律，最后讨论频率、经验分布与蒙特卡洛方法等应用。本章用到 [3.1.8](/3.1.8) 的 Chebyshev 不等式（推论 8.5.1）与 [3.1.2](/3.1.2) 中事件列的极限；各种收敛模式之间的关系在 [3.1.14](/3.1.14) 中系统讨论。

## 12.1. 两种收敛模式

数列的收敛 $a_n \to a$ 是确定的概念。随机变量 $Y_n$ 是样本点 $\omega$ 的函数，"$Y_n \to Y$"可以有不同的含义，取决于先怎样"去掉随机性"。下面的两种定义适用于一般的随机变量序列，不局限于大数定律。

**定义 12.1.1（依概率收敛）** 设 $Y_n, Y$ 是同一概率空间上的随机变量。如果对任意 $\varepsilon > 0$，有

$$
\lim_{n \to \infty} \mathbb{P}(\lvert Y_n - Y \rvert \ge \varepsilon) = 0,
$$
则称 $Y_n$ **依概率收敛**到 $Y$（convergence in probability），记作 $Y_n \xrightarrow{p} Y$。

记 $A_n = \{\omega\colon \lvert Y_n(\omega) - Y(\omega) \rvert < \varepsilon\}$，则 $\mathbb{P}(\lvert Y_n - Y \rvert \ge \varepsilon) = \mathbb{P}(A_n^{\mathsf c}) = 1 - \mathbb{P}(A_n)$，所以 $Y_n \xrightarrow{p} Y$ 等价于对每个 $\varepsilon > 0$，$\lim_{n \to \infty} \mathbb{P}(A_n) = 1$。

**定义 12.1.2（几乎处处收敛）** 如果

$$
\mathbb{P}\left(\lim_{n \to \infty} Y_n = Y\right) = 1,
$$
则称 $Y_n$ **几乎处处收敛**到 $Y$，也称以概率 $1$ 收敛或几乎必然收敛（almost sure convergence），记作 $Y_n \xrightarrow{\text{a.s.}} Y$，或 $Y_n \to Y$ a.s.。

由数列极限的定义，$\lim_n a_n = a$ 当且仅当对任意 $\varepsilon > 0$，存在 $n$，使得对一切 $k \ge n$ 有 $\lvert a_k - a \rvert < \varepsilon$。于是对固定的 $\varepsilon > 0$，

$$
\left\{\lim_{n \to \infty} Y_n = Y\right\} \subset \bigcup_{n=1}^{\infty} \bigcap_{k=n}^{\infty} \{\lvert Y_k - Y \rvert < \varepsilon\} = \liminf_{n \to \infty} A_n,
$$
左边的事件是右边对所有 $\varepsilon = 1/m$（$m = 1, 2, \dots$）取交。因此 $Y_n \xrightarrow{\text{a.s.}} Y$ 蕴含对每个 $\varepsilon > 0$，$\mathbb{P}(\liminf_n A_n) = 1$。

两种收敛"把随机性去掉、变成数列"的方式不同：

- 依概率收敛先对每个固定的 $n$ 计算概率 $\mathbb{P}(A_n^{\mathsf c})$，把随机性去掉，再看这个数列是否趋于 $0$。极限号在最外层，"偏差大于 $\varepsilon$"的事件的概率可以始终不为 $0$，只要趋于 $0$ 即可。
- 几乎处处收敛先固定一个试验结果 $\omega$，看数列 $Y_n(\omega)$ 是否收敛，再要求"不收敛的 $\omega$"全体的概率为 $0$。极限号在最里层。

把每个 $\omega$ 对应的 $Y_1(\omega), Y_2(\omega), \dots$ 画成一条曲线（下图）：依概率收敛是"先竖着看截面比例"——给定 $n$，落在 $\varepsilon$ 带之外的曲线所占的概率随 $n$ 增大而趋于 $0$；几乎处处收敛是"先横着看每条曲线"——几乎每条曲线最终都进入并停留在任意窄的带内（各条曲线进入的时刻可以不同）。

由 $\mathbb{P}(\liminf_n A_n) = \lim_{n} \mathbb{P}\left(\bigcap_{k \ge n} A_k\right) \le \liminf_{n} \mathbb{P}(A_n)$（概率的连续性，定理 2.2.1），几乎处处收敛蕴含依概率收敛；反之不然，反例见 [3.1.14](/3.1.14)。

![抛均匀硬币时样本均值 M_n 的 20 条样本轨道与 p +- 0.03 的带；每条曲线对应一个 omega](./plots/sample-mean-paths.py)

## 12.2. 弱大数定律

**定理 12.2.1（弱大数定律）** 设 $\{X_n\}$ 是独立同分布的随机变量序列，且 $\operatorname{Var}(X_1) < \infty$，则对任意给定的 $\varepsilon > 0$，

$$
\lim_{n \to \infty} \mathbb{P}\left(\left\lvert \frac{1}{n}\sum_{i=1}^{n} X_i - \mathbb{E}X_1 \right\rvert \ge \varepsilon\right) = 0,
$$
即 $\dfrac{1}{n}\displaystyle\sum_{k=1}^{n} X_k \xrightarrow{p} \mathbb{E}X_1$。

**证明** 记 $M_n = \frac{1}{n}\sum_{i=1}^{n} X_i$。由同分布，$\mathbb{E}M_n = \mathbb{E}X_1$；由独立同分布，$\operatorname{Var}(M_n) = \frac{1}{n^2} \cdot n\operatorname{Var}(X_1) = \frac{\operatorname{Var}(X_1)}{n}$。由 Chebyshev 不等式（推论 8.5.1），

$$
\mathbb{P}(\lvert M_n - \mathbb{E}X_1 \rvert \ge \varepsilon) = \mathbb{P}(\lvert M_n - \mathbb{E}M_n \rvert \ge \varepsilon) \le \frac{\operatorname{Var}(M_n)}{\varepsilon^2} = \frac{\operatorname{Var}(X_1)}{n\varepsilon^2} \to 0, \quad n \to \infty. \quad \square
$$

定理的含义：当 $n$ 很大时，我们有很大的把握（但不是 100%）断言 $\frac{1}{n}\sum X_i$ 很接近 $\mathbb{E}X_1$。证明还给出了定量的界 $\frac{\operatorname{Var}(X_1)}{n\varepsilon^2}$，可以用来确定样本量。

**例 12.2.1** 设人群中疫苗有效的比例为 $p$，随机抽 $n$ 个人，用 $X_i$ 表示疫苗对第 $i$ 个人是否有效，则样本中的有效比例为 $M_n = (X_1 + \cdots + X_n)/n$。大数定律告诉我们，可以通过样本均值 $M_n$ 认识总体均值 $p$。需要多大的样本量，才能保证误差不小于 3% 的概率不超过 5%？

**解** 目标是 $\mathbb{P}(\lvert M_n - p \rvert \ge 0.03) \le 0.05$。由定理 12.2.1 的证明，并利用 $\operatorname{Var}(X_1) = p(1 - p) \le \frac{1}{4}$，

$$
\mathbb{P}(\lvert M_n - p \rvert \ge 0.03) \le \frac{\operatorname{Var}(X_1)}{n(0.03)^2} \le \frac{1}{4n(0.03)^2} \le 0.05,
$$
解得 $n \ge 5555.6$，取 $n = 5556$ 即可。这个估计不依赖于 $p$ 的值，也不需要大样本近似，但相当保守；用中心极限定理只需约 $1068$ 人（[3.1.13](/3.1.13) 例 13.2.1）。

## 12.3. 理论深化

定理 12.2.1 的条件（独立同分布、方差有限）可以放宽，结论（依概率收敛）也可以加强。

### 12.3.1. 放宽条件

**定理 12.3.1（Markov 大数定律）** 设 $\{X_n\}$ 是方差有限的随机变量序列（不要求独立或同分布），若

$$
\frac{1}{n^2}\operatorname{Var}\left(\sum_{k=1}^{n} X_k\right) \to 0,
$$
则 $\dfrac{1}{n}\displaystyle\sum_{k=1}^{n} (X_k - \mathbb{E}X_k) \xrightarrow{p} 0$。

证明与定理 12.2.1 完全相同：对 $\frac{1}{n}\sum_k (X_k - \mathbb{E}X_k)$ 用 Chebyshev 不等式。若 $\{X_n\}$ 两两不相关且方差一致有界，条件自然满足。

去掉方差有限的条件，只要求一阶矩存在，结论仍成立。

**定理 12.3.2（Khinchin 大数定律）** 设 $\{X_n\}$ 独立同分布，且 $\mathbb{E}\lvert X_1 \rvert < \infty$，则

$$
\frac{1}{n}\sum_{k=1}^{n} X_k \xrightarrow{p} \mathbb{E}X_1.
$$

这时 Chebyshev 不等式不再适用，但可以用特征函数证明（[3.1.14](/3.1.14)）。对独立同分布序列，弱大数定律最一般的形式如下（证明超出本课程范围）。

**定理 12.3.3** 设 $\{X_n\}$ 是独立同分布的随机变量序列，则存在实数列 $\{a_n\}$ 使得

$$
\frac{1}{n}\sum_{k=1}^{n} X_k - a_n \xrightarrow{p} 0
$$
的充分必要条件是 $n\mathbb{P}(\lvert X_1 \rvert \ge n) \to 0$。此时可取 $a_n = \mathbb{E}(X_1\boldsymbol{1}_{\{\lvert X_1 \rvert < n\}})$。

条件之间的关系是 $\operatorname{Var}(X_1) < \infty \Rightarrow \mathbb{E}\lvert X_1 \rvert < \infty \Rightarrow n\mathbb{P}(\lvert X_1 \rvert \ge n) \to 0$。第二个蕴含：$n\mathbb{P}(\lvert X_1 \rvert \ge n) \le \mathbb{E}(\lvert X_1 \rvert \boldsymbol{1}_{\{\lvert X_1 \rvert \ge n\}}) \to 0$（控制收敛）。当 $\mathbb{E}\lvert X_1 \rvert < \infty$ 时 $a_n \to \mathbb{E}X_1$，定理 12.3.3 就化为定理 12.3.2；而 $n\mathbb{P}(\lvert X_1 \rvert \ge n) \to 0$ 时 $\mathbb{E}X_1$ 可以不存在，这时样本均值并不收敛到"期望"，只是与 $a_n$ 越来越近。

### 12.3.2. 加强结论：强大数定律

**定理 12.3.4（强大数定律）** 设 $\{X_n\}$ 是独立同分布的随机变量序列。

1. 若 $\mathbb{E}\lvert X_1 \rvert < \infty$，则 $\dfrac{1}{n}\displaystyle\sum_{k=1}^{n} X_k \xrightarrow{\text{a.s.}} \mathbb{E}X_1$；
2. 反之，若 $\dfrac{1}{n}\displaystyle\sum_{k=1}^{n} X_k \xrightarrow{\text{a.s.}} C$（$C$ 为有限常数），则 $\mathbb{E}\lvert X_1 \rvert < \infty$，且 $C = \mathbb{E}X_1$。

即 $\mathbb{P}\left(\lim_{n \to \infty} \frac{1}{n}\sum_{k=1}^{n} X_k = \mathbb{E}X_1\right) = 1$，$\mathbb{E}\lvert X_1 \rvert < \infty$ 是充分必要条件。（此定理称为 Kolmogorov 强大数定律，证明超出本课程范围。）

**例 12.3.1** 在例 12.2.1 中，强大数定律告诉我们：随着 $n$ 增加，样本均值 $M_n$ 几乎一定渐近地接近总体均值 $p$——几乎每一次试验序列的有效比例最终都稳定在 $p$ 附近。

对独立同分布序列，强、弱大数定律对比如下：

| | 弱大数定律 | 强大数定律 |
|---|---|---|
| 条件（充要） | $n\mathbb{P}(\lvert X_1 \rvert \ge n) \to 0$ | $\mathbb{E}\lvert X_1 \rvert < \infty$ |
| 结论 | $\frac{1}{n}\sum X_k - a_n \xrightarrow{p} 0$ | $\frac{1}{n}\sum X_k \xrightarrow{\text{a.s.}} \mathbb{E}X_1$ |
| 直观 | 样本均值接近总体均值的可能性越来越大 | 采样次数越多，样本均值几乎一定渐近地接近总体均值 |

条件强弱不同，结论强弱也不同。当 $\mathbb{E}\lvert X_1 \rvert < \infty$ 时两者都成立，并不矛盾：由强大数定律与"几乎处处收敛蕴含依概率收敛"可得 $\frac{1}{n}\sum X_k \xrightarrow{p} \mathbb{E}X_1$，Khinchin 大数定律也直接给出这个结论。只有在 $\mathbb{E}\lvert X_1 \rvert = \infty$ 但 $n\mathbb{P}(\lvert X_1 \rvert \ge n) \to 0$ 时，两者才有区别，下例就是这种情形。

**例 12.3.2** 设 $X, X_1, X_2, \dots$ 独立同分布，

$$
\mathbb{P}(X = m) = \mathbb{P}(X = -m) = \frac{C}{2m^2 \ln m}, \quad m = 3, 4, \dots,
$$
其中 $C$ 为归一化常数。则 $\bar X_n = \frac{1}{n}\sum_{k=1}^{n} X_k$ 服从弱大数定律（$\bar X_n \xrightarrow{p} 0$），但不服从强大数定律。

**解** 对 $n \ge 4$，

$$
\begin{aligned}
n\mathbb{P}(\lvert X \rvert \ge n) &= Cn\sum_{m=n}^{\infty} \frac{1}{m^2 \ln m} \le \frac{Cn}{\ln n}\sum_{m=n}^{\infty} \frac{1}{m^2} \le \frac{Cn}{\ln n}\sum_{m=n}^{\infty} \frac{1}{m(m-1)} \\
&= \frac{Cn}{\ln n}\sum_{m=n}^{\infty}\left(\frac{1}{m-1} - \frac{1}{m}\right) = \frac{C}{\ln n} \cdot \frac{n}{n-1} \to 0,
\end{aligned}
$$
由定理 12.3.3，$\bar X_n - a_n \xrightarrow{p} 0$；由对称性 $a_n = \mathbb{E}(X\boldsymbol{1}_{\{\lvert X \rvert < n\}}) = 0$，即 $\bar X_n \xrightarrow{p} 0$。另一方面

$$
\mathbb{E}X^+ = \mathbb{E}X^- = \sum_{m=3}^{\infty} m \cdot \frac{C}{2m^2 \ln m} = \frac{C}{2}\sum_{m=3}^{\infty} \frac{1}{m \ln m} = \infty,
$$
所以 $\mathbb{E}\lvert X \rvert = \infty$，由定理 12.3.4 的第 2 条，$\bar X_n$ 不几乎处处收敛到任何有限常数。

另一个极端是 Cauchy 分布：$n\mathbb{P}(\lvert X_1 \rvert \ge n) \to \frac{2}{\pi} \ne 0$，连弱大数定律也不成立。事实上由特征函数（例 11.3.7），$\bar X_n$ 的特征函数是 $[\mathrm{e}^{-\lvert t \rvert/n}]^n = \mathrm{e}^{-\lvert t \rvert}$，$\bar X_n$ 与 $X_1$ 同分布，无论 $n$ 多大都不会集中。

![标准正态与标准 Cauchy 样本的均值轨迹：前者稳定在 0，后者不时出现大跳跃、始终不收敛](./plots/cauchy-vs-normal-means.py)

## 12.4. 经典应用

### 12.4.1. 频率与概率

如何确定一枚不均匀硬币正面朝上的概率？取 $X_n \sim \mathrm{Ber}(p)$ 为第 $n$ 次试验中事件是否发生的示性变量，大数定律的这一特例称为 Bernoulli 大数定律：

$$
\frac{1}{n}\sum_{k=1}^{n} X_k \xrightarrow{p} p \quad \text{（由强大数定律，也几乎处处收敛）}.
$$
大数定律表明频率稳定于概率，这为用频率确定概率提供了理论依据，是统计学中频率学派的基础。

### 12.4.2. 经验分布

**例 12.4.1** 设 $\{X_j\}$ 是概率空间 $(\Omega, \mathcal{F}, \mathbb{P})$ 上独立同分布的随机序列，分布函数为 $F(x)$，用 $x_j = X_j(\omega)$ 表示一次实现中的观测值。则以概率 $1$，观测数列 $\{x_j\}$ 决定 $F(x)$。

**证明** 对任意确定的 $x \in \mathbb{R}$，令 $g(X_j) = \boldsymbol{1}_{\{X_j \le x\}}$，则 $\{g(X_j)\}$ 独立同分布，$\mathbb{E}g(X_1) = \mathbb{P}(X_1 \le x) = F(x)$。由强大数定律，

$$
F_n(x) := \frac{1}{n}\sum_{j=1}^{n} \boldsymbol{1}_{\{X_j \le x\}} \xrightarrow{\text{a.s.}} F(x),
$$
即以概率 $1$ 有 $\lim_n \frac{1}{n}\sum_{j=1}^{n} \boldsymbol{1}_{\{x_j \le x\}} = F(x)$。 $\square$

$F_n(x)$ 是 [3.2](/3.2) 中的**经验分布函数**。上面只证明了对每个固定的 $x$ 几乎处处收敛；更强的 **Glivenko–Cantelli 定理**断言 $\sup_x \lvert F_n(x) - F(x) \rvert \xrightarrow{\text{a.s.}} 0$。

### 12.4.3. 蒙特卡洛方法

蒙特卡洛方法（Monte Carlo method）又称随机模拟方法，由 von Neumann、Ulam 等人在 20 世纪 40 年代研制核武器时提出：把要计算的量表示成某个随机变量的期望，再用大量独立模拟的样本均值去近似它。由强大数定律，近似以概率 $1$ 收敛；由中心极限定理，误差的量级是 $1/\sqrt{n}$，与问题的维数无关。它是统计计算的核心基础，特别适用于解析方法难以求解甚至不能求解的问题。

**例 12.4.2（计算 $\pi$）** 在正方形 $[-1, 1]^2$ 中独立均匀地投点 $(U_j, V_j)$，令 $I_j = \boldsymbol{1}_{\{U_j^2 + V_j^2 \le 1\}}$，则 $\mathbb{E}I_j = \mathbb{P}(I_j = 1) = \frac{\pi}{4}$。由强大数定律，$\hat\pi_n = 4 \cdot \frac{1}{n}\sum_{j=1}^{n} I_j \xrightarrow{\text{a.s.}} \pi$。

**例 12.4.3（投点法求积分）** 设 $0 \le f(x) \le c$（$a \le x \le b$），要估计 $\int_a^b f(x)\,\mathrm{d}x$。在矩形 $A = [a, b] \times [0, c]$ 中独立均匀地投 $n$ 个点 $(X_j, Y_j)$，用 $I_j$ 表示第 $j$ 个点是否落入曲线下方的区域 $B = \{(x, y)\colon 0 \le y \le f(x)\}$。则以概率 $1$，

$$
\frac{1}{n}\sum_{j=1}^{n} I_j \to \mathbb{E}I_j = \mathbb{P}(I_j = 1) = \frac{\int_a^b f(x)\,\mathrm{d}x}{c(b - a)}, \qquad \text{故} \quad \int_a^b f(x)\,\mathrm{d}x \approx c(b - a)\frac{1}{n}\sum_{j=1}^{n} I_j.
$$

![蒙特卡洛估计 pi：左为 2000 个随机点，右为估计值 4 * (落入圆内比例) 随点数 n 的变化](./plots/monte-carlo-pi.py)

大数定律的思想还出现在许多其他地方。机器学习中的随机森林：大数定律保证随着树的数目增加，泛化误差收敛到一个常数，而不会无限制地增大，因此增加树的数目不会导致过拟合。随机过程中的遍历定理：在一定条件下，沿一条轨道的时间平均收敛到对状态空间的空间平均，是大数定律在相依序列上的推广。

## 小结

- 依概率收敛 $Y_n \xrightarrow{p} Y$：$\forall \varepsilon > 0$，$\mathbb{P}(\lvert Y_n - Y \rvert \ge \varepsilon) \to 0$；几乎处处收敛 $Y_n \xrightarrow{\text{a.s.}} Y$：$\mathbb{P}(\lim Y_n = Y) = 1$。后者蕴含前者。
- 弱大数定律（定理 12.2.1）：独立同分布、方差有限 $\Rightarrow$ $\frac{1}{n}\sum X_k \xrightarrow{p} \mathbb{E}X_1$。证明的核心是 $\operatorname{Var}(M_n) = \operatorname{Var}(X_1)/n$ 与 Chebyshev 不等式，同时给出样本量的保守估计。
- 推广：Markov 大数定律去掉独立同分布，Khinchin 大数定律只要求 $\mathbb{E}\lvert X_1 \rvert < \infty$；独立同分布时弱大数定律的充要条件是 $n\mathbb{P}(\lvert X_1 \rvert \ge n) \to 0$。
- 强大数定律（定理 12.3.4）：独立同分布时 $\frac{1}{n}\sum X_k \xrightarrow{\text{a.s.}} \mathbb{E}X_1$ 当且仅当 $\mathbb{E}\lvert X_1 \rvert < \infty$。
- 应用：样本均值认识总体均值（频率估计概率、经验分布函数、蒙特卡洛方法）；样本量的计算（大数定律加 Chebyshev 不等式）。统计学"由已知（样本均值）认识未知（总体均值）"，概率论"由规律（必然）主导现象（偶然）"，大数定律正是两者的桥梁。
