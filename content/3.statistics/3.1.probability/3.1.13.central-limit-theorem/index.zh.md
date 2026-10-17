---
title: 中心极限定理
---

**大数定律**（[3.1.12](/3.1.12)）说明样本均值 $M_n = (X_1 + \cdots + X_n)/n$ 收敛到总体均值 $\mu$，但没有说收敛有多快、误差 $M_n - \mu$ 服从什么分布。模拟显示收敛的快慢与分布的离散程度有关：取值 $\pm 10$ 的变量比取值 $\pm 1$ 的变量收敛得慢得多，而把误差放大 $\sqrt{n}$ 倍、再除以标准差后，$\sqrt{n}\,(M_n - \mu)/\sigma$ 的分布趋于稳定。它稳定到什么分布？中心极限定理回答：无论原来的分布是什么，只要方差有限，标准化后的和都**依分布收敛**到标准正态分布。这解释了正态分布在自然界与统计学中的普遍性——大量独立的随机因素叠加的结果近似服从正态分布——也为估计样本量、计算概率的近似值和构造置信区间提供了统一的工具。

本章的证明依靠 [3.1.11](/3.1.11) 的**特征函数**与连续性定理（定理 11.3.6）。各种收敛模式之间的关系见 [3.1.14](/3.1.14)，随机向量的中心极限定理见 [3.1.15](/3.1.15)。

## 13.1. 基本定理

回顾依分布收敛（定义 11.3.3）：设 $Y_n, Y$ 的分布函数分别为 $F_n(x), F(x)$，若在 $F(x)$ 的每个连续点 $x$ 处 $\lim_{n \to \infty} F_n(x) = F(x)$，则称 $Y_n \xrightarrow{d} Y$。极限为标准正态分布时，$\Phi$ 处处连续，依分布收敛就是对一切 $x$，$\mathbb{P}(Y_n \le x) \to \Phi(x)$。

**定理 13.1.1（中心极限定理）** 设 $\{X_n\}$ 是独立同分布的随机变量序列，期望为 $\mu$，方差为 $0 < \sigma^2 < \infty$，记 $S_n = X_1 + \cdots + X_n$，则

$$
\frac{S_n - \mathbb{E}(S_n)}{\sqrt{\operatorname{Var}(S_n)}} = \frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1).
$$

此定理也称 Lindeberg–Lévy 中心极限定理。用样本均值 $M_n = S_n/n$ 表示，等价地有

$$
\frac{M_n - \mathbb{E}(M_n)}{\sqrt{\operatorname{Var}(M_n)}} = \frac{\sqrt{n}\,(M_n - \mu)}{\sigma} \xrightarrow{d} \mathcal{N}(0, 1).
$$
因此当 $n$ 充分大时，它提供了近似分布：

$$
S_n \overset{\cdot}{\sim} \mathcal{N}(n\mu, n\sigma^2), \qquad M_n \overset{\cdot}{\sim} \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right).
$$
前者常用于解释现象（大量独立同分布随机因素的叠加近似服从正态分布），后者是统计推断的基础（[3.2](/3.2)）。注意 $S_n$ 本身并不收敛，"近似服从"只是 $n$ 固定时对标准化量的极限陈述的改写。

**证明** 令 $Y_k = (X_k - \mu)/\sigma$，则 $\{Y_k\}$ 独立同分布，$\mathbb{E}Y_k = 0$，$\operatorname{Var}(Y_k) = 1$，且

$$
\frac{S_n - \mathbb{E}(S_n)}{\sqrt{\operatorname{Var}(S_n)}} = \frac{1}{\sqrt{n}}\sum_{k=1}^{n} \frac{X_k - \mu}{\sigma} = \frac{1}{\sqrt{n}}\sum_{k=1}^{n} Y_k.
$$
直接计算 $\mathbb{P}\left(\frac{1}{\sqrt{n}}\sum Y_k \le x\right)$ 需要 $n$ 重卷积，几乎不可行；改用特征函数。设 $\varphi(t) = \mathbb{E}\mathrm{e}^{\mathrm{i}tY_1}$，由性质 11.3.1，$\varphi'(0) = \mathrm{i}\,\mathbb{E}Y_1 = 0$，$\varphi''(0) = \mathrm{i}^2\mathbb{E}Y_1^2 = -1$，由式 (11.1)，

$$
\varphi(t) = \varphi(0) + \varphi'(0)t + \frac{1}{2}\varphi''(0)t^2 + o(t^2) = 1 - \frac{t^2}{2} + o(t^2), \quad t \to 0.
$$
由独立同分布，$\frac{1}{\sqrt{n}}\sum_{k=1}^{n} Y_k$ 的特征函数为

$$
\varphi_n(t) = \mathbb{E}\exp\left(\mathrm{i}t\,\frac{Y_1 + \cdots + Y_n}{\sqrt{n}}\right) = \left[\varphi\left(\frac{t}{\sqrt{n}}\right)\right]^n = \left(1 - \frac{t^2}{2n} + o\left(\frac{t^2}{n}\right)\right)^n \to \mathrm{e}^{-t^2/2}, \quad n \to \infty,
$$
这里对固定的 $t$，$t/\sqrt{n} \to 0$，极限是"$1^\infty$"型，用 $(1 + a_n/n)^n \to \mathrm{e}^a$（$a_n \to a$，对复数 $a_n$ 同样成立）。$\mathrm{e}^{-t^2/2}$ 是 $\mathcal{N}(0, 1)$ 的特征函数（例 11.3.6），由连续性定理（定理 11.3.6），结论成立。 $\square$

证明中"不失一般性地标准化为均值 $0$、方差 $1$"的做法可以大大简化计算。同样的方法给出 Khinchin 大数定律的证明：只要 $\mathbb{E}\lvert X_1 \rvert < \infty$，$\varphi_{X_1}(t) = 1 + \mathrm{i}\mu t + o(t)$，$M_n$ 的特征函数 $[\varphi_{X_1}(t/n)]^n \to \mathrm{e}^{\mathrm{i}\mu t}$，即 $M_n \xrightarrow{d} \mu$，而依分布收敛到常数等价于依概率收敛（[3.1.14](/3.1.14)）。

![Exp(1) 的标准化和 (S_n - n)/sqrt(n) 的精确密度（n = 1, 2, 5, 30）逐渐趋于标准正态密度](./plots/clt-exponential.py)

## 13.2. 应用举例

中心极限定理应用的本质是如下的近似：

$$
\mathbb{P}\left(c_1 \le \frac{\sqrt{n}}{\sigma}\left(\frac{S_n}{n} - \mu\right) \le c_2\right) \approx \Phi(c_2) - \Phi(c_1) = \alpha.
$$
其中三个量 $n$、$c$（区间端点）、$\alpha$（概率）知道两个就可以求第三个：已知 $c, \alpha$ 求 $n$（样本量）；已知 $n, \alpha$ 求 $c$（分位点）；已知 $n, c$ 求 $\alpha$（概率的近似）。

**例 13.2.1（样本量）** 设人群中疫苗有效的比例为 $\mu$，随机抽 $n$ 个人，$X_i$ 表示疫苗对第 $i$ 个人是否有效。需要多大的样本量，才能以 95% 的概率保证样本中的有效比例 $M_n = (X_1 + \cdots + X_n)/n$ 与 $\mu$ 的误差小于 3%？

**解** 求 $n$ 使 $\mathbb{P}(\lvert M_n - \mu \rvert < 0.03) \ge 0.95$。记 $\sigma = \sqrt{\operatorname{Var}(X_1)} = \sqrt{\mu(1 - \mu)} \le \frac{1}{2}$，$Z \sim \mathcal{N}(0, 1)$，

$$
\mathbb{P}(\lvert M_n - \mu \rvert < 0.03) = \mathbb{P}\left(\left\lvert \frac{M_n - \mu}{\sigma/\sqrt{n}} \right\rvert < \frac{0.03\sqrt{n}}{\sigma}\right) \approx \mathbb{P}\left(\lvert Z \rvert < \frac{0.03\sqrt{n}}{\sigma}\right) \ge \mathbb{P}(\lvert Z \rvert < 0.06\sqrt{n}).
$$
令 $\mathbb{P}(\lvert Z \rvert < 0.06\sqrt{n}) = 0.95$，即 $0.06\sqrt{n} = z_{0.025} = 1.96$，得 $n = (1.96/0.06)^2 \approx 1067.1$，取 $n = 1068$ 即可。

同样的问题用 Chebyshev 不等式（例 12.2.1）需要 $5556$ 人。两种方法的目标相同：Chebyshev 不等式的估计对任何 $n$ 都严格成立，但很保守；中心极限定理给出的是大样本下的近似，可以用时更精确。实际中只要样本量不太小，优先用中心极限定理。

**例 13.2.2（理论近似）** 有时前 $n$ 项和的分布计算复杂或没有简单的表达式。设 $\{X_n\}$ 独立同分布于 $\mathrm{U}(-1, 1)$，$S_n = X_1 + \cdots + X_n$ 的密度为

$$
f_{S_n}(x) = \begin{cases} \dfrac{1}{2^n (n-1)!}\displaystyle\sum_{k=0}^{\lfloor (n+x)/2 \rfloor} (-1)^k \binom{n}{k}(n + x - 2k)^{n-1}, & \lvert x \rvert \le n, \\ 0, & \lvert x \rvert > n. \end{cases}
$$
而 $\mu = 0$，$\sigma^2 = \frac{1}{3}$，中心极限定理给出 $S_n \overset{\cdot}{\sim} \mathcal{N}\left(0, \frac{n}{3}\right)$，$n = 10$ 时两者已几乎无法分辨。近似可以大大简化计算。

![U(-1, 1) 的独立和 S_n 的精确密度（实线）与正态近似 N(0, n/3)（虚线），n = 2, 4, 10](./plots/uniform-sum-density.py)

**例 13.2.3** 据说 Poincaré 总在同一家面包店买面包。店家称每块面包平均重 1000 克，上下浮动 50 克。Poincaré 把一年中买到的面包都称重，发现平均值总在 940 至 960 克之间。按店家的说法，$\mu = 1000$，$\sigma = 50$，$M_n \overset{\cdot}{\sim} \mathcal{N}(1000, 50^2/n)$，$n = 30$ 时

$$
\mathbb{P}(940 \le M_n \le 960) = \mathbb{P}\left(\frac{940 - 1000}{50/\sqrt{n}} \le \frac{M_n - 1000}{50/\sqrt{n}} \le \frac{960 - 1000}{50/\sqrt{n}}\right) \approx \Phi(-4.38) - \Phi(-6.57) \approx 6 \times 10^{-6}.
$$
这样小概率的事件发生了，说明店家的说法不可信，Poincaré 于是投诉了面包店。此后他继续称重，发现面包重量的分布在 950 克以下几乎没有、右侧却拖得很长，形状像截去左半边的钟形曲线——面包店依然做轻面包，只是把重一些的卖给了他。面包重量受面粉量、水量、酵母、温度等大量因素影响，按中心极限定理应近似服从正态分布，分布形状的异常本身就是作弊的证据。

## 13.3. 理论拓展

如果 $X_k$ 独立但不同分布，和是否仍近似正态？答案是：只要没有哪一项占主导地位。

**定理 13.3.1（Lindeberg–Feller 中心极限定理）** 设 $\{X_n\}$ 是独立的随机变量序列，方差有限，$\sigma_k^2 = \operatorname{Var}(X_k)$，且满足

$$
B_n^2 = \sum_{k=1}^{n} \sigma_k^2 \to \infty, \qquad \max_{1 \le k \le n} \frac{\sigma_k^2}{B_n^2} \to 0. \tag{13.1}
$$
则中心极限定理

$$
\frac{1}{B_n}\sum_{k=1}^{n} (X_k - \mathbb{E}X_k) \xrightarrow{d} \mathcal{N}(0, 1)
$$
成立的充分必要条件是 Lindeberg 条件（Lindeberg condition）成立：对任意 $\varepsilon > 0$，

$$
\lim_{n \to \infty} \frac{1}{B_n^2}\sum_{k=1}^{n} \mathbb{E}\left[(X_k - \mathbb{E}X_k)^2\boldsymbol{1}_{\{\lvert X_k - \mathbb{E}X_k \rvert > \varepsilon B_n\}}\right] = 0.
$$

式 (13.1) 中第二个条件称为 Feller 条件，它说每一项的方差在总方差中所占的比例都趋于 $0$；在 $B_n \to \infty$ 时它等价于 $\sigma_n^2/B_n^2 \to 0$。Lindeberg 条件蕴含 Feller 条件：$\sigma_k^2 \le \varepsilon^2 B_n^2 + \mathbb{E}[(X_k - \mathbb{E}X_k)^2\boldsymbol{1}_{\{\lvert X_k - \mathbb{E}X_k \rvert > \varepsilon B_n\}}]$。独立同分布且方差有限时，Lindeberg 条件中的和等于 $\frac{1}{\sigma^2}\mathbb{E}[(X_1 - \mu)^2\boldsymbol{1}_{\{\lvert X_1 - \mu \rvert > \varepsilon\sigma\sqrt{n}\}}] \to 0$（控制收敛），所以定理 13.1.1 是定理 13.3.1 的特例。Lindeberg 条件不易直接验证，常用的是下面更强但更容易检验的条件。

**推论 13.3.1（Lyapunov 中心极限定理）** 设 $\{X_n\}$ 独立，$B_n^2 = \sum_{k=1}^{n}\operatorname{Var}(X_k)$。若存在 $\delta > 0$，使得 Lyapunov 条件（Lyapunov condition）

$$
\lim_{n \to \infty} \frac{1}{B_n^{2+\delta}}\sum_{k=1}^{n} \mathbb{E}\lvert X_k - \mathbb{E}X_k \rvert^{2+\delta} = 0
$$
成立，则 $\frac{1}{B_n}\sum_{k=1}^{n}(X_k - \mathbb{E}X_k) \xrightarrow{d} \mathcal{N}(0, 1)$。

**证明** 在 $\{\lvert X_k - \mathbb{E}X_k \rvert > \varepsilon B_n\}$ 上 $(X_k - \mathbb{E}X_k)^2 \le \lvert X_k - \mathbb{E}X_k \rvert^{2+\delta}/(\varepsilon B_n)^\delta$，所以 Lindeberg 条件中的和不超过 $\frac{1}{\varepsilon^\delta B_n^{2+\delta}}\sum_k \mathbb{E}\lvert X_k - \mathbb{E}X_k \rvert^{2+\delta} \to 0$，再用定理 13.3.1 的充分性（充分性不需要式 (13.1)）。 $\square$

这些定理的意义是：大量"微小的"、相互独立的随机因素的叠加近似服从正态分布。Gauss 在处理观测误差时引进正态分布刻画误差的分布；工程中常假设噪声是 Gauss 白噪声；同型号、同批次产品的重量近似服从正态分布。正态分布可以说是自然法则之一。

## 13.4. 细致讨论

### 13.4.1. 离散型随机变量的修正

设 $X_i \overset{\text{iid}}{\sim} \mathrm{Ber}(p)$，$S_n = X_1 + \cdots + X_n \sim \mathrm{Bin}(n, p)$，例如 $n = 36$，$p = 0.5$。用正态分布近似时会遇到两个问题：

- $\mathbb{P}(S_n \le 21) = \mathbb{P}(S_n < 22)$，用 $21$ 还是 $22$ 代入正态分布函数？两者的结果不同。
- 单点概率：连续分布在一点的概率为 $0$，直接近似得 $\mathbb{P}(S_n = 19) \approx 0$，显然不对。

解决办法是把离散变量的每个取值 $k$ 看成区间 $[k - 0.5, k + 0.5]$ 上的一个矩形，用正态密度曲线下这一段的面积近似 $\mathbb{P}(S_n = k)$。

**定理 13.4.1（de Moivre–Laplace 中心极限定理）** 设 $S_n \sim \mathrm{Bin}(n, p)$，$n$ 充分大，$k \le m$ 是非负整数，则

$$
\mathbb{P}(k \le S_n \le m) \approx \Phi\left(\frac{m - np}{\sqrt{np(1-p)}}\right) - \Phi\left(\frac{k - np}{\sqrt{np(1-p)}}\right).
$$
其修正形式（近似更为精确）为

$$
\mathbb{P}(k \le S_n \le m) \approx \Phi\left(\frac{m + 0.5 - np}{\sqrt{np(1-p)}}\right) - \Phi\left(\frac{k - 0.5 - np}{\sqrt{np(1-p)}}\right).
$$
更重要的是，修正形式可以计算单点概率 $\mathbb{P}(S_n = k)$（取 $m = k$）。

这是定理 13.1.1 在 $X_i \sim \mathrm{Ber}(p)$ 时的特例，由 de Moivre（1733，$p = \frac{1}{2}$）与 Laplace（1812，一般的 $p$）得到，是历史上第一个中心极限定理。端点加减 $0.5$ 的方法称为连续性修正（continuity correction），对其他取整数值的随机变量同样适用。计算区间概率时修正与否只影响精度；计算单点概率时必须修正。

**例 13.4.1** 设 $S_n \sim \mathrm{Bin}(36, 0.5)$，求 $\mathbb{P}(S_n \le 21)$。

**解** 精确值为 $\mathbb{P}(S_n \le 21) = \sum_{k=0}^{21}\binom{36}{k}0.5^{36} = 0.8785$。这里 $np = 18$，$\sqrt{np(1-p)} = 3$。不作修正时

$$
\mathbb{P}(S_n \le 21) \approx \Phi\left(\frac{21 - 18}{3}\right) = \Phi(1) = 0.8413;
$$
修正后

$$
\mathbb{P}(S_n \le 21) \approx \Phi\left(\frac{21.5 - 18}{3}\right) = \Phi(1.167) = 0.8783,
$$
与精确值几乎一致。又如单点概率 $\mathbb{P}(S_n = 19) = 0.1251$，修正后的正态近似为 $\Phi\left(\frac{19.5 - 18}{3}\right) - \Phi\left(\frac{18.5 - 18}{3}\right) = 0.1253$。

![Bin(36, 0.5) 的分布列与正态近似：连续性修正把 P(S_n = k) 近似为正态密度在 [k - 0.5, k + 0.5] 上的面积](./plots/continuity-correction.py)

**例 13.4.2** 某地区原有一家小型电影院，拟筹建一所较大型的。据分析，该地区每日平均看电影者约有 $n = 1600$ 人，预计新影院开业后，平均约有 $3/4$ 的观众将去新影院。影院在计划座位数时，要求座位数尽可能多，但"空座达到 200 或更多"的概率不超过 10%。问设多少座位为好？

**解** 把每日看电影的人排号为 $1, 2, \dots, 1600$，令 $X_i = 1$ 表示第 $i$ 个观众去新影院，否则 $X_i = 0$，则 $\mathbb{P}(X_i = 1) = 3/4$。假定各观众去不去是独立选择，则 $X_1, \dots, X_{1600}$ 独立。设座位数为 $m$，要求

$$
\mathbb{P}(X_1 + \cdots + X_{1600} \le m - 200) \le 0.1,
$$
在此条件下取 $m$ 最大，即取等号。$np = 1200$，$\sqrt{np(1-p)} = 10\sqrt{3}$，按修正的近似公式，$m$ 应满足

$$
\Phi\left(\frac{m - 200 + 0.5 - 1200}{10\sqrt{3}}\right) = 0.1.
$$
$\Phi(x) = 0.1$ 时 $x = -1.2816$，由 $\frac{m - 1399.5}{10\sqrt{3}} = -1.2816$ 得 $m = 1377.3$，取 $m = 1377$。

### 13.4.2. 适用条件

$n \to \infty$ 时正态近似越来越精确，但实践中样本量 $n$ 是固定的、有限的，需要知道 $n$ 多大时近似可信。遗憾的是没有简单普遍的准则：这依赖于 $X_i$ 的分布与正态分布是否接近，特别是是否对称。例如 $X_i \sim \mathrm{U}(-1, 1)$ 时 $n = 10$ 已经很好（例 13.2.2），而偏斜的 $X_i \sim \mathrm{Exp}(\lambda)$ 需要大得多的 $n$。此外，近似 $\mathbb{P}(S_n \le c)$ 的精度与 $c$ 有关，一般说来 $c$ 在 $S_n$ 的均值附近时精度较高，在尾部的相对误差较大。

收敛速度的一个定量刻画是 Berry–Esseen 定理。

**定理 13.4.2（Berry–Esseen 定理）** 设 $X_1, X_2, \dots$ 独立同分布，$\mathbb{E}X_1 = 0$，$\operatorname{Var}(X_1) = 1$，$\mathbb{E}\lvert X_1 \rvert^3 < \infty$，$W_n = (X_1 + \cdots + X_n)/\sqrt{n}$，$Z \sim \mathcal{N}(0, 1)$，则

$$
\sup_{x \in \mathbb{R}}\lvert \mathbb{P}(W_n \le x) - \mathbb{P}(Z \le x) \rvert \le \frac{C\,\mathbb{E}\lvert X_1 \rvert^3}{\sqrt{n}},
$$
其中 $C$ 是与分布无关的常数（已知可取 $C = 0.4748$）。

所以误差的量级是 $1/\sqrt{n}$，三阶绝对矩越大（分布越偏、尾部越重），收敛越慢。中心极限定理刻画了大数定律的收敛速度：$M_n - \mu$ 的量级是 $\sigma/\sqrt{n}$；Berry–Esseen 定理又刻画了中心极限定理本身的收敛速度。

二项分布有两种近似，要注意各自的适用条件。

| | Poisson 近似 | 正态近似 |
|---|---|---|
| 条件 | $n$ 大，$p$ 小，$np = \lambda$ 适中 | $np(1-p)$ 大 |
| 结论 | $\mathrm{Bin}(n, p) \approx \mathrm{Poi}(np)$ | $\mathrm{Bin}(n, p) \approx \mathcal{N}(np, np(1-p))$ |
| 例 | $p = 1/100$，$n = 100$ | $\mathrm{Bin}(1600, 0.5)$；$p = 1/10$，$n = 500$ |

当 $np$ 固定且很大时两种近似都可用，这并不矛盾：$\mathrm{Poi}(\lambda)$ 是 $\lambda$ 个独立 $\mathrm{Poi}(1)$ 之和（$\lambda$ 为整数时），由中心极限定理，$\lambda$ 很大时 $\mathrm{Poi}(\lambda) \approx \mathcal{N}(\lambda, \lambda)$。

**例 13.4.3（Stirling 公式）** 中心极限定理也有理论上的应用。设 $X_1, X_2, \dots$ 独立同分布于 $\mathrm{Poi}(1)$，$S_n = \sum_{i=1}^{n} X_i \sim \mathrm{Poi}(n)$，则 $\mathbb{P}(S_n = n) = \mathrm{e}^{-n}\frac{n^n}{n!}$。另一方面，$\mathbb{E}S_n = \operatorname{Var}(S_n) = n$，用修正的正态近似，

$$
\mathbb{P}(S_n = n) = \mathbb{P}(n - 0.5 < S_n \le n + 0.5) \approx \Phi\left(\frac{0.5}{\sqrt{n}}\right) - \Phi\left(-\frac{0.5}{\sqrt{n}}\right) \approx \frac{1}{\sqrt{2\pi}} \cdot \frac{1}{\sqrt{n}}.
$$
两式联立得 Stirling 公式 $n! \approx \sqrt{2\pi n}\,(n/\mathrm{e})^n$。（这里的论证是启发式的：严格证明需要局部极限定理，它保证单点概率的相对误差趋于 $0$。）

**例 13.4.4** 设 $X_1, X_2, \dots$ 独立，都服从标准 Cauchy 分布，记 $M_n = (X_1 + \cdots + X_n)/n$。$M_n$ 服从什么分布？

**解** 由例 11.3.7，$M_n$ 的特征函数为 $[\mathrm{e}^{-\lvert t/n \rvert}]^n = \mathrm{e}^{-\lvert t \rvert}$，所以对一切 $n$，$M_n$ 仍服从标准 Cauchy 分布，不会集中，也不会近似正态。

这时中心极限定理（以及大数定律）不成立，因为定理要求方差有限，而 Cauchy 分布连期望都不存在。方差有限这个条件是否必要？对独立同分布序列，若存在常数 $a_n$ 使 $(S_n - a_n)/\sqrt{n}$ 依分布收敛到非退化的正态分布，则 $\mathbb{E}X_1^2 < \infty$，所以在 $\sqrt{n}$ 的标准化下这个条件是必要的；改用其他标准化常数时，有些方差无穷的分布（例如密度在尾部像 $\lvert x \rvert^{-3}$ 的分布）仍可以近似正态，而像 Cauchy 这样尾部更重的分布，极限是其他的稳定分布。

## 小结

- 中心极限定理（定理 13.1.1）：独立同分布、方差 $0 < \sigma^2 < \infty$ 时，$\frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)$，即 $S_n \overset{\cdot}{\sim} \mathcal{N}(n\mu, n\sigma^2)$，$M_n \overset{\cdot}{\sim} \mathcal{N}(\mu, \sigma^2/n)$。证明：标准化，特征函数的二阶 Taylor 展开，$(1 - \frac{t^2}{2n} + o(\frac{1}{n}))^n \to \mathrm{e}^{-t^2/2}$，再用连续性定理。
- 大数定律与中心极限定理的关系：前者说 $M_n \to \mu$，后者说偏差 $M_n - \mu$ 的量级是 $\sigma/\sqrt{n}$ 且近似正态。
- 应用：由 $\mathbb{P}(c_1 \le \frac{\sqrt{n}}{\sigma}(M_n - \mu) \le c_2) \approx \Phi(c_2) - \Phi(c_1)$，已知其中两个量求第三个（样本量、分位点、概率）。
- 独立不同分布：Lindeberg–Feller 定理（Lindeberg 条件，没有占主导地位的项），Lyapunov 条件是常用的充分条件。
- 离散型随机变量用连续性修正（端点 $\pm 0.5$）；单点概率必须修正。近似精度取决于分布的对称性与尾部，误差量级为 $1/\sqrt{n}$（Berry–Esseen）；方差无穷时（如 Cauchy 分布）定理不成立。
- 利用随机变量的特征函数（或矩母函数、概率母函数）的极限，可以确认随机变量极限的分布。
