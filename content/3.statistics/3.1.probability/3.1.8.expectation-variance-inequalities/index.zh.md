---
title: 期望、方差、相关不等式
---

分布完整地刻画了一个随机变量，但在很多问题中我们需要用一两个数来概括它：投资时比较两种理财产品，人们首先看"平均收益"和"风险"；赌局中断时分配赌金，需要知道各方"预期能赢多少"。本章引入最重要的两个数字特征：数学期望描述分布的中心位置，方差描述分布在期望附近的集中程度。期望有三种互相补充的解读——代数上是加权平均，物理上是分布的质心，优化上是均方误差意义下的最佳常数预测。期望的线性性质使许多复杂的计算化为简单的计算（"大问题拆成小问题"）。本章最后介绍几个基本的概率不等式（Markov、Chebyshev、Cauchy–Schwarz、Jensen 不等式），它们在不知道分布细节时给出概率与期望的界，是大数定律（[3.1.12](/3.1.12)）等极限定理的工具。本章用到 [3.1.4](/3.1.4) 的常见分布与 [3.1.6](/3.1.6)、[3.1.7](/3.1.7) 的随机向量；条件期望与协方差分别见 [3.1.9](/3.1.9)、[3.1.10](/3.1.10)。

## 8.1. 数学期望的定义

先看一个历史上的问题。甲、乙两人赌技相当，约定先赢满 5 局者获得全部赌金 100 金币。甲赢了 4 局、乙赢了 3 局时赌局被迫中断，赌金该如何分配？按已赢局数 $4:3$ 分配忽略了此后的可能性。Pascal 与 Fermat 在 1654 年的通信中给出的思路是：再赌两局必能分出胜负，而乙只有连赢两局才能获胜，概率为 $\frac{1}{4}$。于是甲的收益 $X$ 以概率 $\frac{3}{4}$ 取 100、以概率 $\frac{1}{4}$ 取 0，甲的"预期收益"为 $100 \times \frac{3}{4} + 0 \times \frac{1}{4} = 75$，应按 $3:1$ 分配。把随机变量的取值按概率加权平均，就得到数学期望。

**定义 8.1.1（数学期望）** 设离散型随机变量 $X$ 有分布列 $\mathbb{P}(X = x_j)$，$j = 1, 2, \dots$。如果 $\sum_{j=1}^{\infty} \lvert x_j \rvert \mathbb{P}(X = x_j) < \infty$，称

$$
\mathbb{E}X = \sum_{j=1}^{\infty} x_j \mathbb{P}(X = x_j)
$$
为 $X$ 的**数学期望**或均值。设连续型随机变量 $X$ 有概率密度 $f(x)$，如果 $\int_{-\infty}^{\infty} \lvert x \rvert f(x)\,\mathrm{d}x < \infty$，称

$$
\mathbb{E}X = \int_{-\infty}^{\infty} x f(x)\,\mathrm{d}x
$$
为 $X$ 的数学期望或均值。

要求绝对收敛，是为了保证级数的和与求和次序无关，从而期望只依赖于分布。只取有限个值的随机变量的期望总是存在。期望记作 $\mathbb{E}X$ 或 $\mathbb{E}(X)$。把 $\mathbb{P}(X = x_j)$ 看作放在位置 $x_j$ 的质量，$\mathbb{E}X$ 就是这组质量的质心；连续型的情形把密度看作质量的线密度。

### 8.1.1. 常见分布的期望

**例 8.1.1** 设 $X \sim \mathrm{Ber}(p)$，则 $\mathbb{E}X = 1 \cdot p + 0 \cdot (1 - p) = p$。特别地，对事件 $A$，示性函数 $\boldsymbol{1}_A \sim \mathrm{Ber}(\mathbb{P}(A))$，所以

$$
\mathbb{E}\boldsymbol{1}_A = \mathbb{P}(A).
$$
这个等式是连接概率与期望的桥梁：概率是示性函数的期望。

**例 8.1.2** 设 $X \sim \mathrm{Bin}(n, p)$，则 $\mathbb{E}X = np$。

**证明** 利用 $j\binom{n}{j} = n\binom{n-1}{j-1}$ 和二项分布列的归一性，

$$
\mathbb{E}X = \sum_{j=0}^n j\binom{n}{j}p^j(1 - p)^{n-j} = np\sum_{j=1}^n \binom{n-1}{j-1}p^{j-1}(1 - p)^{n-j} = np\sum_{k=0}^{n-1}\binom{n-1}{k}p^k(1 - p)^{n-1-k} = np. \qquad \square
$$
直观上，$n$ 次试验、每次成功概率 $p$，平均成功 $np$ 次；例 8.2.4 将用期望的线性性质给出更简单的证明。

**例 8.1.3** 设 $X \sim \mathrm{Poi}(\lambda)$，则由归一性 $\mathbb{E}X = \sum_{k=1}^{\infty} k\frac{\lambda^k}{k!}\mathrm{e}^{-\lambda} = \lambda\sum_{k=1}^{\infty}\frac{\lambda^{k-1}}{(k - 1)!}\mathrm{e}^{-\lambda} = \lambda$。

**例 8.1.4** 设 $X \sim \mathrm{Geo}(p)$，$\mathbb{P}(X = k) = p q^{k-1}$（$k \ge 1$，$q = 1 - p$），则对幂级数逐项求导，

$$
\mathbb{E}X = \sum_{k=1}^{\infty} k p q^{k-1} = p\Big(\sum_{k=0}^{\infty} q^k\Big)' = \frac{p}{(1 - q)^2} = \frac{1}{p}.
$$
成功概率为 $p$ 时，平均要等 $1/p$ 次才首次成功。例 9.2.3 将用条件期望给出另一种算法。

**例 8.1.5** 设 $X \sim \mathrm{U}(a, b)$，则 $\mathbb{E}X = \int_a^b \frac{x}{b - a}\,\mathrm{d}x = \frac{a + b}{2}$，即区间的中点。

**例 8.1.6** 设 $X \sim \Gamma(\alpha, \lambda)$，密度 $f(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}\mathrm{e}^{-\lambda x}$（$x > 0$），令 $t = \lambda x$，

$$
\mathbb{E}X = \int_0^{\infty} \frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha}\mathrm{e}^{-\lambda x}\,\mathrm{d}x = \frac{1}{\lambda\Gamma(\alpha)}\int_0^{\infty} t^{(\alpha+1)-1}\mathrm{e}^{-t}\,\mathrm{d}t = \frac{\Gamma(\alpha + 1)}{\lambda\Gamma(\alpha)} = \frac{\alpha}{\lambda}.
$$
$\alpha = 1$ 时 $\Gamma(1, \lambda) = \mathrm{Exp}(\lambda)$，$\mathbb{E}X = 1/\lambda$：参数 $\lambda$ 是速率，均值是它的倒数。

**例 8.1.7** 设 $X$ 的数学期望存在，密度关于 $x = \mu$ 对称，即 $f(\mu + x) = f(\mu - x)$，则 $\mathbb{E}X = \mu$。

**证明** $g(t) = t f(t + \mu)$ 是奇函数，且 $\int \lvert g \rvert < \infty$，故

$$
\mathbb{E}X = \int_{-\infty}^{\infty} \mu f(x)\,\mathrm{d}x + \int_{-\infty}^{\infty}(x - \mu)f(x)\,\mathrm{d}x = \mu + \int_{-\infty}^{\infty} t f(t + \mu)\,\mathrm{d}t = \mu. \qquad \square
$$
特别地 $X \sim \mathcal{N}(\mu, \sigma^2)$ 时 $\mathbb{E}X = \mu$。这正是"质心"直观的应用。条件"期望存在"不能省略：Cauchy 分布的密度关于 0 对称，但期望不存在（例 8.2.7）。

### 8.1.2. 一般随机变量的期望

**例 8.1.8** 抛一枚均匀硬币，正面直接得 0.5 元；反面则转一个幸运转盘，得到的钱数服从 $\mathrm{U}(0, 1)$。记最终得到的钱数为 $X$，它既不是离散型也不是连续型：分布函数在 0.5 处有高度 $\frac{1}{2}$ 的跳跃，其余部分有密度 $\frac{1}{2}\boldsymbol{1}_{(0,1)}(x)$。把离散部分与连续部分分别按定义计算再相加，

$$
\mathbb{E}X = 0.5 \times \frac{1}{2} + \int_0^1 x \cdot \frac{1}{2}\,\mathrm{d}x = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}.
$$

一般地（了解即可），设 $X$ 的分布函数为 $F$，可以统一地定义 $\mathbb{E}X = \int_{\mathbb{R}} x\,\mathrm{d}F(x)$（Lebesgue–Stieltjes 积分）。若 $F = F_1 + F_2$，其中 $F_1(x) = \int_{-\infty}^x f_0(s)\,\mathrm{d}s$ 有密度，$F_2$ 只在可列个点 $x_j$ 处跳跃，跳跃高度为 $\mathbb{P}(X = x_j)$，则只要 $\int \lvert x \rvert f_0(x)\,\mathrm{d}x + \sum_j \lvert x_j \rvert\mathbb{P}(X = x_j) < \infty$，

$$
\mathbb{E}X = \int_{-\infty}^{\infty} x f_0(x)\,\mathrm{d}x + \sum_j x_j\,\mathbb{P}(X = x_j) = \int x\,\mathrm{d}F_1(x) + \int x\,\mathrm{d}F_2(x).
$$
由此可见期望只依赖于分布：同分布的随机变量（若期望存在）有相同的期望。

## 8.2. 随机向量函数的期望与期望的性质

### 8.2.1. 随机向量函数的期望

设 $X \sim \mathrm{U}(0, \pi/2)$，要计算 $\mathbb{E}\cos X$，一种思路是先求 $Y = \cos X$ 的密度，再按定义计算 $\mathbb{E}Y$。但这一步其实不必要。以离散情形为例，设 $X$ 取 $-1, 1, 2$，$Y = X^2$ 取 $1, 4$，则

$$
\mathbb{E}Y = 1 \cdot \mathbb{P}(Y = 1) + 4 \cdot \mathbb{P}(Y = 4) = 1 \cdot [\mathbb{P}(X = -1) + \mathbb{P}(X = 1)] + 4 \cdot \mathbb{P}(X = 2) = \sum_{x} g(x)\mathbb{P}(X = x),
$$
即可以直接对 $X$ 的分布求 $g(X)$ 的加权平均。

**定理 8.2.1** 设随机向量 $\boldsymbol{X} = (X_1, \dots, X_n)$ 有联合分布函数 $F(\boldsymbol{x})$，$g(\boldsymbol{x})$ 是实函数，如果 $\int_{\mathbb{R}^n} \lvert g(\boldsymbol{x}) \rvert\,\mathrm{d}F(\boldsymbol{x}) < \infty$，则 $Y = g(\boldsymbol{X})$ 的数学期望存在，且

$$
\mathbb{E}g(\boldsymbol{X}) = \int_{\mathbb{R}^n} g(\boldsymbol{x})\,\mathrm{d}F(\boldsymbol{x}).
$$
具体地，$\boldsymbol{X}$ 是离散型时 $\mathbb{E}g(\boldsymbol{X}) = \sum_{\boldsymbol{x}} g(\boldsymbol{x})\mathbb{P}(\boldsymbol{X} = \boldsymbol{x})$；$\boldsymbol{X}$ 有联合密度 $f$ 时 $\mathbb{E}g(\boldsymbol{X}) = \int_{\mathbb{R}^n} g(\boldsymbol{x})f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}$。

这个定理的方便之处在于：计算 $g(\boldsymbol{X})$ 的期望不需要先推导 $g(\boldsymbol{X})$ 的分布。

**例 8.2.1** 设 $X \sim \mathrm{U}(0, \pi/2)$，则 $\mathbb{E}\cos X = \int_0^{\pi/2} \frac{2}{\pi}\cos x\,\mathrm{d}x = \frac{2}{\pi}$。

**例 8.2.2** 设 $X \sim \mathcal{N}(0, 1)$，$\alpha$ 是常数，计算 $\mathbb{E}\lvert X \rvert^\alpha$。

**解** 对 $\alpha > -1$，令 $x = \sqrt{2t}$，

$$
\mathbb{E}\lvert X \rvert^\alpha = \frac{2}{\sqrt{2\pi}}\int_0^{\infty} x^\alpha\mathrm{e}^{-x^2/2}\,\mathrm{d}x = \frac{2^{\alpha/2}}{\sqrt{\pi}}\int_0^{\infty} t^{\frac{\alpha+1}{2}-1}\mathrm{e}^{-t}\,\mathrm{d}t = \sqrt{\frac{2^\alpha}{\pi}}\,\Gamma\Big(\frac{\alpha + 1}{2}\Big).
$$
特别地（利用 $\Gamma(1/2) = \sqrt{\pi}$），$\mathbb{E}X^2 = 1$，$\mathbb{E}\lvert X \rvert = \sqrt{2/\pi}$；$\alpha \le -1$ 时积分在 0 附近发散，$\mathbb{E}\lvert X \rvert^\alpha = \infty$。

**例 8.2.3** 设 $(X, Y)$ 在单位圆 $D = \{x^2 + y^2 \le 1\}$ 内均匀分布，则

$$
\mathbb{E}X = \int_{\mathbb{R}^2} x\cdot\frac{1}{\pi}\boldsymbol{1}_D(x, y)\,\mathrm{d}x\,\mathrm{d}y = \frac{1}{\pi}\int_{-1}^{1}\Big(\int_{-\sqrt{1-y^2}}^{\sqrt{1-y^2}} x\,\mathrm{d}x\Big)\mathrm{d}y = 0,
$$
同理 $\mathbb{E}Y = 0$：质心在圆心。

### 8.2.2. 期望的性质

一般来说 $\mathbb{E}g(X) \ne g(\mathbb{E}X)$，但对线性函数等号成立。

**定理 8.2.2** 设 $\mathbb{E}\lvert X \rvert < \infty$，$\mathbb{E}\lvert Y \rvert < \infty$，$a, b, c$ 是实数，则

1. $\mathbb{E}c = c$；
2. $\lvert \mathbb{E}X \rvert \le \mathbb{E}\lvert X \rvert$；
3. （线性性）$\mathbb{E}(aX + bY) = a\mathbb{E}X + b\mathbb{E}Y$；
4. （单调性）若 $X \le Y$ a.s.，则 $\mathbb{E}X \le \mathbb{E}Y$；
5. 若 $X$ 与 $Y$ 独立，则 $\mathbb{E}(XY) = \mathbb{E}X \cdot \mathbb{E}Y$。

**证明** 以 $(X, Y)$ 有联合密度 $f$ 的情形为例，离散情形把积分换成求和。1、2 由定义直接得到。3：由定理 8.2.1，

$$
\mathbb{E}(aX + bY) = \int\!\!\int (ax + by)f(x, y)\,\mathrm{d}x\,\mathrm{d}y = a\int x f_X(x)\,\mathrm{d}x + b\int y f_Y(y)\,\mathrm{d}y = a\mathbb{E}X + b\mathbb{E}Y,
$$
其中积分的拆分由 $\lvert ax + by \rvert \le \lvert a \rvert\lvert x \rvert + \lvert b \rvert\lvert y \rvert$ 的可积性保证。4：$Y - X \ge 0$ a.s.，非负随机变量的期望非负，再用 3。5：由定理 6.3.3，$f(x, y) = f_X(x)f_Y(y)$，由 Fubini 定理 $\mathbb{E}(XY) = \int x f_X(x)\,\mathrm{d}x \int y f_Y(y)\,\mathrm{d}y$（先对 $\lvert xy \rvert$ 验证可积）。 $\square$

线性性不需要任何独立性假设，这使它成为最有力的计算工具：把复杂的随机变量写成简单随机变量（常常是示性函数）之和。

**例 8.2.4** 设 $X \sim \mathrm{Bin}(n, p)$，则 $X$ 与 $X_1 + \cdots + X_n$ 同分布，其中 $X_i$ 是第 $i$ 次试验成功的示性函数，$X_i \sim \mathrm{Ber}(p)$。由线性性 $\mathbb{E}X = np$。同样，由例 7.1.5，$\Gamma(k, \lambda)$（$k$ 为正整数）与 $k$ 个独立 $\mathrm{Exp}(\lambda)$ 之和同分布，故其期望为 $k/\lambda$。

**例 8.2.5（质量抽查）** $N$ 件产品中有 $M$ 件正品，从中无放回地任取 $n$ 件，期望抽到几件正品？

**解** 抽到的正品数 $X$ 服从超几何分布 $\mathrm{H}(n, M, N)$，$\mathbb{P}(X = k) = \binom{M}{k}\binom{N-M}{n-k}\big/\binom{N}{n}$，按定义计算较繁。记 $X_k$ 为第 $k$ 次是否抽到正品的示性函数，则 $X = X_1 + \cdots + X_n$。由抽签的公平性，每个 $X_k \sim \mathrm{Ber}(M/N)$（虽然 $X_k$ 之间不独立），由线性性

$$
\mathbb{E}X = \mathbb{E}X_1 + \cdots + \mathbb{E}X_n = n\frac{M}{N}.
$$

**例 8.2.6（机器人打字）** 一个机器人在只有 $N = 26$ 个小写字母的键盘上打字，每次独立地等可能地选择一个字母。要打出 $k$ 个不同的字母，平均需要打字多少次？

**解** 用 $S_k$ 表示出现第 $k$ 个新字母时的打字次数，$S_0 = 0$，$X_k = S_k - S_{k-1}$ 是等待第 $k$ 个新字母的次数。出现 $k - 1$ 个不同字母后，每次打出新字母的概率为 $p_k = \frac{N - k + 1}{N}$，所以 $X_k \sim \mathrm{Geo}(p_k)$，$\mathbb{E}X_k = \frac{N}{N - k + 1}$。由 $S_k = X_1 + \cdots + X_k$，

$$
\mathbb{E}S_k = \sum_{j=1}^k \frac{N}{N - j + 1} = N\sum_{m=N-k+1}^{N}\frac{1}{m}.
$$
特别地 $\mathbb{E}S_N = N\big(1 + \frac{1}{2} + \cdots + \frac{1}{N}\big) \approx N(\ln N + \gamma)$（$\gamma \approx 0.577$ 是 Euler 常数），而 $N$ 较大时 $\mathbb{E}S_{N/2} = N\sum_{m=N/2+1}^{N}\frac{1}{m} \approx N\ln 2 \approx 0.693N$。这说明打出一半的字母比较容易，打出全部字母则困难得多，最后几个字母要等很久。例如键盘上有 50 个不同的符号时，打出全部符号平均需要 $50 \times (1 + \frac{1}{2} + \cdots + \frac{1}{50}) \approx 225$ 次，而打出其中 25 个只需约 34 次。这就是"集卡问题"（coupon collector problem）。

**例 8.2.7** 设 $X \sim t_1$，即 Cauchy 分布，则 $\mathbb{E}X$ 不存在。由例 7.1.6，$X$ 与 $Z/W$ 同分布（$Z, W$ 独立且都服从 $\mathcal{N}(0, 1)$），但不能由此推出 $\mathbb{E}X = \mathbb{E}Z/\mathbb{E}W$：期望的性质没有关于商的结论。按定义，

$$
\int_{-\infty}^{\infty}\frac{\lvert x \rvert}{\pi(1 + x^2)}\,\mathrm{d}x = \frac{2}{\pi}\int_0^{\infty}\frac{x}{1 + x^2}\,\mathrm{d}x = \infty,
$$
不满足绝对收敛的要求，因此期望不存在（尽管密度关于 0 对称）。

**例 8.2.8** 如果 $\mathbb{E}\lvert X \rvert = 0$，则 $X = 0$ a.s.

**证明** 对每个 $n$，$\mathbb{P}(\lvert X \rvert > 1/n) = \mathbb{E}\boldsymbol{1}\{n\lvert X \rvert > 1\} \le \mathbb{E}\big(n\lvert X \rvert\boldsymbol{1}\{n\lvert X \rvert > 1\}\big) \le n\mathbb{E}\lvert X \rvert = 0$。由概率的连续性，

$$
\mathbb{P}(\lvert X \rvert > 0) = \mathbb{P}\Big(\bigcup_{n=1}^{\infty}\{\lvert X \rvert > 1/n\}\Big) = \lim_{n\to\infty}\mathbb{P}(\lvert X \rvert > 1/n) = 0. \qquad \square
$$

### 8.2.3. 期望的其他计算公式

**定理 8.2.3** 设 $X \ge 0$。若 $X$ 是连续型随机变量（或一般地），则

$$
\mathbb{E}X = \int_0^{\infty}\mathbb{P}(X > x)\,\mathrm{d}x;
$$
若 $X$ 只取非负整数值，则 $\mathbb{E}X = \sum_{k=1}^{\infty}\mathbb{P}(X \ge k) = \sum_{k=0}^{\infty}\mathbb{P}(X > k)$。更一般地，对 $r \ge 1$，$\mathbb{E}X^r = \int_0^{\infty} r x^{r-1}\mathbb{P}(X > x)\,\mathrm{d}x$。

**证明** 设 $X$ 有密度 $f$。由 $x^r = \int_0^x r t^{r-1}\,\mathrm{d}t$ 和 Fubini 定理（被积函数非负），

$$
\mathbb{E}X^r = \int_0^{\infty}\Big(\int_0^x r t^{r-1}\,\mathrm{d}t\Big)f(x)\,\mathrm{d}x = \int_0^{\infty} r t^{r-1}\Big(\int_t^{\infty}f(x)\,\mathrm{d}x\Big)\mathrm{d}t = \int_0^{\infty} r t^{r-1}\mathbb{P}(X > t)\,\mathrm{d}t.
$$
整数值情形把 $\mathbb{E}X = \sum_k k\mathbb{P}(X = k)$ 中的每一项 $k\mathbb{P}(X = k)$ 拆成 $k$ 个 $\mathbb{P}(X = k)$，再按列重新求和即得。 $\square$

例如 $X \sim \mathrm{Geo}(p)$ 时 $\mathbb{P}(X \ge k) = q^{k-1}$，$\mathbb{E}X = \sum_{k\ge1}q^{k-1} = 1/p$；$X \sim \mathrm{Exp}(\lambda)$ 时 $\mathbb{E}X = \int_0^{\infty}\mathrm{e}^{-\lambda x}\,\mathrm{d}x = 1/\lambda$。

**例 8.2.9** 在 $[0, 1]$ 上按均匀分布随机取一点 $X$ 把线段断开，求包含固定点 $p_0 \in (0, 1)$ 的那一段的长度 $L$ 的期望。

**解** $X < p_0$ 时包含 $p_0$ 的是右段，$L = 1 - X$；$X \ge p_0$ 时是左段，$L = X$。由定理 8.2.1，

$$
\mathbb{E}L = \int_0^{p_0}(1 - x)\,\mathrm{d}x + \int_{p_0}^1 x\,\mathrm{d}x = p_0 - \frac{p_0^2}{2} + \frac{1 - p_0^2}{2} = \frac{1}{2} + p_0(1 - p_0).
$$
它大于两段的平均长度 $\frac{1}{2}$（$p_0$ 在中点时最大，为 $\frac{3}{4}$）：长的一段更容易包含 $p_0$。这种"按长度加权的抽样偏差"在等车时间等问题中常见。

### 8.2.4. 期望的优化解释

**定理 8.2.4** 设 $\mathbb{E}X = \mu$，$\mathbb{E}X^2 < \infty$，则

$$
\mathbb{E}(X - \mu)^2 \le \mathbb{E}(X - c)^2, \quad \forall c \in \mathbb{R},
$$
即 $\mathbb{E}X = \operatorname*{argmin}_{c\in\mathbb{R}}\mathbb{E}(X - c)^2$。

**证明** $\mathbb{E}(X - c)^2 = \mathbb{E}(X - \mu)^2 + 2(\mu - c)\mathbb{E}(X - \mu) + (\mu - c)^2 = \mathbb{E}(X - \mu)^2 + (\mu - c)^2$。 $\square$

所以如果要用一个常数 $c$ 去"预测"随机变量 $X$，并以均方误差 $\mathbb{E}(X - c)^2$ 衡量预测的好坏，最佳的常数预测就是期望。[3.1.9](/3.1.9) 将把这一结论推广到用另一个随机变量的函数去预测 $X$。期望不是唯一合理的数字特征：换用绝对误差，最佳常数就变成中位数。

**定理 8.2.5** 设 $\mathbb{E}\lvert X \rvert < \infty$，$m$ 是 $X$ 的中位数（满足 $\mathbb{P}(X \le m) \ge \frac{1}{2}$、$\mathbb{P}(X \ge m) \ge \frac{1}{2}$ 的数，例如 $F^{-1}(1/2)$），则 $m = \operatorname*{argmin}_{c\in\mathbb{R}}\mathbb{E}\lvert X - c \rvert$。

**证明** 设 $c > m$。当 $x \le m$ 时 $\lvert x - c \rvert - \lvert x - m \rvert = c - m$；当 $x > m$ 时 $\lvert x - c \rvert - \lvert x - m \rvert \ge -(c - m)$（三角不等式）。于是

$$
\mathbb{E}\lvert X - c \rvert - \mathbb{E}\lvert X - m \rvert \ge (c - m)\big[\mathbb{P}(X \le m) - \mathbb{P}(X > m)\big] \ge 0,
$$
因为 $\mathbb{P}(X \le m) \ge \frac{1}{2} \ge \mathbb{P}(X > m)$。$c < m$ 的情形对称，利用 $\mathbb{P}(X \ge m) \ge \frac{1}{2}$。 $\square$

中位数总是存在，不易受极端值影响，因此在收入等社会统计资料中常用；但概率统计中期望更重要，因为它有线性性等良好的数学性质，而中位数可能不唯一，也没有可加性。

## 8.3. 方差

### 8.3.1. 定义与计算

期望相同的两个随机变量可以有截然不同的分散程度。例如投资中，平均收益相同的两种产品，风险可能相差很大。

**定义 8.3.1（方差）** 如果随机变量 $X$ 的期望 $\mu = \mathbb{E}X$ 有限，则称 $\mathbb{E}(X - \mu)^2$ 为 $X$ 的**方差**，记作 $\operatorname{Var}(X)$ 或 $\sigma_X^2$。当 $\operatorname{Var}(X) < \infty$ 时称 $X$ 的方差有限。称 $\sigma_X = \sqrt{\operatorname{Var}(X)}$ 为 $X$ 的**标准差**。

方差表示 $X$ 在期望附近的集中程度，标准差与 $X$ 有相同的量纲。展开平方并用期望的线性性，得到常用的计算公式

$$
\operatorname{Var}(X) = \mathbb{E}X^2 - (\mathbb{E}X)^2.
$$
对整数值的分布，计算阶乘矩 $\mathbb{E}[X(X - 1)]$ 往往比 $\mathbb{E}X^2$ 简便，再用 $\mathbb{E}X^2 = \mathbb{E}[X(X - 1)] + \mathbb{E}X$。

**例 8.3.1** 常见分布的方差。

- $X \sim \mathrm{Ber}(p)$：$X^2 = X$，$\operatorname{Var}(X) = p - p^2 = pq$。
- $X \sim \mathrm{Poi}(\lambda)$：$\mathbb{E}[X(X - 1)] = \sum_{k\ge2}k(k - 1)\frac{\lambda^k}{k!}\mathrm{e}^{-\lambda} = \lambda^2$，故 $\mathbb{E}X^2 = \lambda^2 + \lambda$，$\operatorname{Var}(X) = \lambda$。
- $X \sim \mathrm{Geo}(p)$：$\mathbb{E}[X(X - 1)] = \sum_{j\ge1}j(j - 1)pq^{j-1} = pq\big(\sum_{j\ge0}q^j\big)'' = \frac{2pq}{(1 - q)^3} = \frac{2q}{p^2}$，故 $\mathbb{E}X^2 = \frac{2q}{p^2} + \frac{1}{p}$，$\operatorname{Var}(X) = \frac{2q}{p^2} + \frac{1}{p} - \frac{1}{p^2} = \frac{q}{p^2}$。
- $X \sim \mathrm{U}(a, b)$：$\mathbb{E}X^2 = \frac{b^3 - a^3}{3(b - a)} = \frac{a^2 + ab + b^2}{3}$，$\operatorname{Var}(X) = \frac{(b - a)^2}{12}$。
- $X \sim \Gamma(\alpha, \lambda)$：与例 8.1.6 同样计算，$\mathbb{E}X^2 = \frac{\Gamma(\alpha + 2)}{\lambda^2\Gamma(\alpha)} = \frac{\alpha(\alpha + 1)}{\lambda^2}$，$\operatorname{Var}(X) = \frac{\alpha}{\lambda^2}$；特别地 $\mathrm{Exp}(\lambda)$ 的方差为 $\frac{1}{\lambda^2}$。
- $X \sim \mathcal{N}(\mu, \sigma^2)$：令 $t = (x - \mu)/\sigma$，$\operatorname{Var}(X) = \frac{\sigma^2}{\sqrt{2\pi}}\int t^2\mathrm{e}^{-t^2/2}\,\mathrm{d}t = \sigma^2$（例 8.2.2）。
- $X \sim \mathrm{Bin}(n, p)$：$\operatorname{Var}(X) = npq$，由下面的定理 8.3.1 的第 4 条和 $X$ 是 $n$ 个独立 $\mathrm{Ber}(p)$ 之和立即得到。

正态分布的两个参数就是它的期望与方差，Poisson 分布的期望与方差相等，这些是常见分布参数的直观意义。

**定理 8.3.1** 设 $\mathbb{E}X = \mu$，$\operatorname{Var}(X) < \infty$，则

1. $\operatorname{Var}(aX + b) = a^2\operatorname{Var}(X)$，$a, b \in \mathbb{R}$；
2. $\operatorname{Var}(X) = \mathbb{E}(X - \mu)^2 \le \mathbb{E}(X - c)^2$，$\forall c \in \mathbb{R}$；
3. $\operatorname{Var}(X) = 0 \iff X = \mu$ a.s.；
4. 若 $X_1, \dots, X_n$ 相互独立且方差有限，则 $\operatorname{Var}\big(\sum_{k=1}^n X_k\big) = \sum_{k=1}^n \operatorname{Var}(X_k)$。

**证明** 1. $\operatorname{Var}(aX + b) = \mathbb{E}(aX + b - a\mu - b)^2 = a^2\mathbb{E}(X - \mu)^2$。2. 即定理 8.2.4。3. 由例 8.2.8（对 $(X - \mu)^2$ 应用）。4. 记 $\mu_k = \mathbb{E}X_k$，

$$
\operatorname{Var}\Big(\sum_k X_k\Big) = \mathbb{E}\Big(\sum_k (X_k - \mu_k)\Big)^2 = \sum_k \mathbb{E}(X_k - \mu_k)^2 + \sum_{j\ne k}\mathbb{E}[(X_j - \mu_j)(X_k - \mu_k)],
$$
由定理 8.2.2 的第 5 条，独立时交叉项 $\mathbb{E}[(X_j - \mu_j)(X_k - \mu_k)] = \mathbb{E}(X_j - \mu_j)\,\mathbb{E}(X_k - \mu_k) = 0$。 $\square$

第 4 条中的独立性条件可以减弱为两两不相关，交叉项正是 [3.1.10](/3.1.10) 中的协方差。

**例 8.3.2（配对问题）** 某人写了 $n$ 封信，把它们随机地装入写好 $n$ 个不同地址的信封，记 $X$ 为装对的封数，求 $\mathbb{E}X$ 与 $\operatorname{Var}(X)$。

**解** 记 $I_k$ 为第 $k$ 封信装对的示性函数，$X = \sum_{k=1}^n I_k$。$\mathbb{P}(I_k = 1) = \frac{1}{n}$，$j \ne k$ 时 $\mathbb{P}(I_j = I_k = 1) = \frac{1}{n(n - 1)}$。于是 $\mathbb{E}X = n \cdot \frac{1}{n} = 1$，

$$
\mathbb{E}X^2 = \sum_k \mathbb{E}I_k^2 + \sum_{j\ne k}\mathbb{E}(I_jI_k) = n\cdot\frac{1}{n} + n(n - 1)\cdot\frac{1}{n(n - 1)} = 2,
$$
$\operatorname{Var}(X) = 2 - 1 = 1$。$I_k$ 之间不独立，但期望的线性性照样适用；期望与方差都与 $n$ 无关，与 $n$ 很大时 $X$ 近似服从 $\mathrm{Poi}(1)$ 相符。

**例 8.3.3** 三大统计分布的期望与方差。

1. $X \sim \chi^2_n$：$X$ 与 $Z_1^2 + \cdots + Z_n^2$ 同分布（定理 7.1.6），$\mathbb{E}Z_i^2 = 1$，$\mathbb{E}Z_i^4 = 3$（例 8.2.2 取 $\alpha = 4$），故 $\mathbb{E}X = n$，$\operatorname{Var}(X) = n(3 - 1) = 2n$。
2. $T \sim t_n$：$n \ge 2$ 时期望存在，由对称性 $\mathbb{E}T = 0$；$n \ge 3$ 时，由 $T = Z/\sqrt{X/n}$ 与独立性，$\operatorname{Var}(T) = \mathbb{E}Z^2 \cdot n\mathbb{E}X^{-1} = \frac{n}{n - 2}$，其中 $\mathbb{E}X^{-1} = \frac{1}{n - 2}$ 由 $\chi^2_n = \Gamma(n/2, 1/2)$ 的密度直接积分得到。$n = 1$ 时期望不存在（例 8.2.7），$n = 2$ 时方差为无穷。
3. $F \sim F_{m,n}$：$n \ge 3$ 时，$\mathbb{E}F = \mathbb{E}\frac{X}{m}\cdot\mathbb{E}\frac{n}{Y} = 1\cdot\frac{n}{n - 2} = \frac{n}{n - 2}$。

这里用的方法是：利用三大分布与正态分布的关系把期望化为独立变量乘积的期望，或者利用密度函数的归一性（把积分凑成另一个密度）。

### 8.3.2. 标准化

**定义 8.3.2（标准化）** 设 $0 < \operatorname{Var}(X) < \infty$，令

$$
Y = \frac{X - \mathbb{E}X}{\sqrt{\operatorname{Var}(X)}},
$$
则 $\mathbb{E}Y = 0$，$\operatorname{Var}(Y) = 1$，称 $Y$ 为 $X$ 的**标准化**。

特别地，$X \sim \mathcal{N}(\mu, \sigma^2)$ 时 $\frac{X - \mu}{\sigma} \sim \mathcal{N}(0, 1)$。标准化去掉了位置与尺度的信息，使不同量纲、不同数量级的随机变量可以比较，例如比较两门成绩分布不同的考试中的名次。

### 8.3.3. 常见分布的期望与方差

| 分布 | 期望 | 方差 |
|---|---|---|
| $\mathrm{Ber}(p)$ | $p$ | $p(1 - p)$ |
| $\mathrm{Bin}(n, p)$ | $np$ | $np(1 - p)$ |
| $\mathrm{Poi}(\lambda)$ | $\lambda$ | $\lambda$ |
| $\mathrm{Geo}(p)$ | $1/p$ | $(1 - p)/p^2$ |
| $\mathrm{H}(n, M, N)$ | $nM/N$ | $n\frac{M}{N}\big(1 - \frac{M}{N}\big)\frac{N - n}{N - 1}$ |
| $\mathrm{U}(a, b)$ | $(a + b)/2$ | $(b - a)^2/12$ |
| $\mathrm{Exp}(\lambda)$ | $1/\lambda$ | $1/\lambda^2$ |
| $\Gamma(\alpha, \lambda)$ | $\alpha/\lambda$ | $\alpha/\lambda^2$ |
| $\mathrm{Beta}(\alpha, \beta)$ | $\frac{\alpha}{\alpha + \beta}$ | $\frac{\alpha\beta}{(\alpha + \beta)^2(\alpha + \beta + 1)}$ |
| $\mathcal{N}(\mu, \sigma^2)$ | $\mu$ | $\sigma^2$ |
| $\chi^2_n$ | $n$ | $2n$ |
| $t_n$ | $0$（$n \ge 2$） | $\frac{n}{n - 2}$（$n \ge 3$） |

超几何分布的方差可以由 [3.1.10](/3.1.10) 的协方差计算得到；Beta 分布的矩直接由 Beta 函数积分得到，例如 $\mathbb{E}X = \frac{\mathrm{B}(\alpha + 1, \beta)}{\mathrm{B}(\alpha, \beta)} = \frac{\alpha}{\alpha + \beta}$，由此 $\mathbb{E}U_{(k)} = \frac{k}{n + 1}$（例 7.2.3）。

## 8.4. 矩

期望与方差是一类更一般的数字特征的特例。

**定义 8.4.1（矩）** 设 $X$ 是随机变量，$m$ 是正整数。如果 $\mathbb{E}\lvert X \rvert^m < \infty$，称 $\mathbb{E}X^m$ 为 $X$ 的 $m$ 阶**原点矩**，称 $\mathbb{E}(X - \mathbb{E}X)^m$ 为 $X$ 的 $m$ 阶**中心矩**。$m > 2$ 时原点矩与中心矩统称为高阶矩。

一阶原点矩是期望，二阶中心矩是方差。若 $k$ 阶矩存在，则对 $0 < j \le k$，$j$ 阶矩也存在：由 $\lvert x \rvert^j \le 1 + \lvert x \rvert^k$（分 $\lvert x \rvert \le 1$ 与 $\lvert x \rvert > 1$ 讨论）得 $\mathbb{E}\lvert X \rvert^j \le 1 + \mathbb{E}\lvert X \rvert^k < \infty$。

**定义 8.4.2（偏度与峰度）** 设 $X$ 的四阶矩有限，$\mu = \mathbb{E}X$，$\sigma^2 = \operatorname{Var}(X) > 0$，称

$$
\frac{\mathbb{E}(X - \mu)^3}{\sigma^3} = \mathbb{E}\Big(\frac{X - \mu}{\sigma}\Big)^3, \qquad \frac{\mathbb{E}(X - \mu)^4}{\sigma^4} - 3 = \mathbb{E}\Big(\frac{X - \mu}{\sigma}\Big)^4 - 3
$$
分别为 $X$ 的**偏度**与**峰度**（后者也称超额峰度）。

偏度与峰度都是标准化后的矩，与位置和尺度无关。偏度衡量分布的不对称性：对称分布的偏度为 0，右侧拖着长尾的分布偏度为正。峰度衡量尾部相对于正态分布的厚重程度：减去 3 使正态分布的峰度为 0（$\mathbb{E}Z^4 = 3$）。例如 $\mathrm{Exp}(\lambda)$ 的偏度为 2、峰度为 6；$\mathrm{U}(a, b)$ 的峰度为 $-1.2$；$t_\nu$（$\nu > 4$）的峰度为 $\frac{6}{\nu - 4} > 0$。

![偏度与峰度：左图比较对称与右偏的分布，右图比较尾部轻重不同的对称分布（都已标准化为均值 0、方差 1）](./plots/skewness-kurtosis.py)

## 8.5. 概率不等式

不知道分布的全部信息、只知道某些矩时，下面的不等式给出概率与期望的界。它们未必精确，却在理论推导中十分有用：在推断中抓住主要矛盾，适当运用不等式，可以在计算精度与计算复杂度之间取得平衡。

**定理 8.5.1（Markov 不等式）** 对随机变量 $X$ 和 $\varepsilon > 0$，$\alpha > 0$，有

$$
\mathbb{P}(\lvert X \rvert \ge \varepsilon) \le \frac{\mathbb{E}\lvert X \rvert^\alpha}{\varepsilon^\alpha}.
$$

**证明** 在事件 $\{\lvert X \rvert \ge \varepsilon\} = \{\lvert X \rvert^\alpha \ge \varepsilon^\alpha\}$ 上 $\lvert X \rvert^\alpha/\varepsilon^\alpha \ge 1$，因此

$$
\mathbb{P}(\lvert X \rvert \ge \varepsilon) = \mathbb{E}\boldsymbol{1}\{\lvert X \rvert^\alpha \ge \varepsilon^\alpha\} \le \mathbb{E}\Big(\frac{\lvert X \rvert^\alpha}{\varepsilon^\alpha}\boldsymbol{1}\{\lvert X \rvert^\alpha \ge \varepsilon^\alpha\}\Big) \le \mathbb{E}\frac{\lvert X \rvert^\alpha}{\varepsilon^\alpha}. \qquad \square
$$

$\alpha = 1$ 是最常见的形式：非负随机变量取大值的概率受其期望控制，$\mathbb{P}(X \ge \varepsilon) \le \mathbb{E}X/\varepsilon$。

**推论 8.5.1（Chebyshev 不等式）** 设 $X$ 的方差有限，则对 $\varepsilon > 0$，

$$
\mathbb{P}(\lvert X - \mathbb{E}X \rvert \ge \varepsilon) \le \frac{\operatorname{Var}(X)}{\varepsilon^2}.
$$

这是对 $X - \mathbb{E}X$ 取 $\alpha = 2$ 的 Markov 不等式。它定量地刻画了 $X$ 在期望附近的集中程度：例如任何方差有限的分布，落在 $\mu \pm 2\sigma$ 之外的概率不超过 $\frac{1}{4}$，落在 $\mu \pm 3\sigma$ 之外的不超过 $\frac{1}{9}$。对正态分布这两个概率实际约为 0.046 与 0.0027，可见 Chebyshev 不等式的界是对所有分布都成立的保守估计。

![Chebyshev 上界 1/k^2 与几种标准化分布的实际尾概率 P(|X - mu| >= k sigma) 的比较](./plots/chebyshev-bound.py)

**例 8.5.1** 抛一枚均匀硬币 $N$ 次，用 Chebyshev 不等式估计"至少得到 $\frac{3N}{4}$ 个正面"的概率。

**解** 正面次数 $X \sim \mathrm{Bin}(N, 1/2)$，$\mathbb{E}X = N/2$，$\operatorname{Var}(X) = N/4$。

$$
\mathbb{P}\Big(X \ge \frac{3N}{4}\Big) \le \mathbb{P}\Big(\Big\lvert X - \frac{N}{2}\Big\rvert \ge \frac{N}{4}\Big) \le \frac{N/4}{(N/4)^2} = \frac{4}{N}.
$$
本题中 $X$ 的分布关于 $N/2$ 对称，所以 $\mathbb{P}(X - \frac{N}{2} \ge \frac{N}{4}) = \frac{1}{2}\mathbb{P}(\lvert X - \frac{N}{2} \rvert \ge \frac{N}{4})$，上界可以改进为 $\frac{2}{N}$；但对不对称的分布，单侧概率不等于双侧概率的一半，不能这样折半。

**定理 8.5.2（Cauchy–Schwarz 不等式）** 设 $\mathbb{E}X^2 < \infty$，$\mathbb{E}Y^2 < \infty$，则

$$
\lvert \mathbb{E}(XY) \rvert \le \sqrt{\mathbb{E}X^2\,\mathbb{E}Y^2}.
$$
等号成立的充分必要条件是存在不全为零的常数 $a, b$，使得 $aX + bY = 0$ a.s.

**证明** 由 $\lvert xy \rvert \le \frac{1}{2}(x^2 + y^2)$，$\mathbb{E}(XY)$ 存在。对任意实数 $a, b$，

$$
0 \le \mathbb{E}(aX + bY)^2 = a^2\mathbb{E}X^2 + 2ab\,\mathbb{E}(XY) + b^2\mathbb{E}Y^2 = (a, b)\,\Sigma\,(a, b)^{\mathsf T}, \qquad \Sigma = \begin{pmatrix} \mathbb{E}X^2 & \mathbb{E}(XY) \\ \mathbb{E}(XY) & \mathbb{E}Y^2 \end{pmatrix}.
$$
所以 $\Sigma$ 是**半正定矩阵**，$\det\Sigma = \mathbb{E}X^2\,\mathbb{E}Y^2 - [\mathbb{E}(XY)]^2 \ge 0$，即所证不等式。等号成立当且仅当 $\det\Sigma = 0$，当且仅当存在非零向量 $(a, b)$ 使 $(a, b)\Sigma(a, b)^{\mathsf T} = 0$，即 $\mathbb{E}(aX + bY)^2 = 0$，由例 8.2.8 这等价于 $aX + bY = 0$ a.s. $\square$

这正是线性代数中内积空间的 Cauchy–Schwarz 不等式（[2.1](/2.1)），内积取为 $\langle X, Y \rangle = \mathbb{E}(XY)$。它是 [3.1.10](/3.1.10) 中相关系数的绝对值不超过 1 的根据。

**定理 8.5.3（Jensen 不等式）** 设 $\psi$ 是 $\mathbb{R}$ 上的**凸函数**，$X$ 与 $\psi(X)$ 的期望都有限，则

$$
\psi(\mathbb{E}X) \le \mathbb{E}\psi(X).
$$
若 $\psi$ 严格凸，则等号成立当且仅当 $X = \mathbb{E}X$ a.s.

**证明** 凸函数在每一点 $a$ 处有右导数 $c = \psi'_+(a)$，且其图像位于该点的支撑线上方：$\psi(b) - \psi(a) \ge c(b - a)$，$\forall b \in \mathbb{R}$。取 $a = \mathbb{E}X$，$b = X$，得 $\psi(X) - \psi(\mathbb{E}X) \ge c(X - \mathbb{E}X)$，两边取期望，

$$
\mathbb{E}\psi(X) - \psi(\mathbb{E}X) \ge c\,\mathbb{E}(X - \mathbb{E}X) = 0.
$$
若 $\psi$ 严格凸，则 $b \ne a$ 时支撑线不等式严格成立，于是非负随机变量 $\psi(X) - \psi(\mathbb{E}X) - c(X - \mathbb{E}X)$ 的期望为 0 时它几乎必然为 0（例 8.2.8），即 $X = \mathbb{E}X$ a.s. $\square$

例如取 $\psi(x) = x^2$ 得 $(\mathbb{E}X)^2 \le \mathbb{E}X^2$（即 $\operatorname{Var}(X) \ge 0$）；取 $\psi(x) = \lvert x \rvert$ 得 $\lvert \mathbb{E}X \rvert \le \mathbb{E}\lvert X \rvert$；对正随机变量取凹函数 $\ln x$ 得 $\mathbb{E}\ln X \le \ln\mathbb{E}X$。Jensen 不等式在统计中用于 EM 算法的推导、证明极大似然估计的相合性等。

## 小结

- 期望 $\mathbb{E}X = \sum x_j\mathbb{P}(X = x_j)$ 或 $\int x f(x)\,\mathrm{d}x$，要求绝对收敛；三种解读：加权平均、质心、最佳常数预测 $\operatorname*{argmin}_c\mathbb{E}(X - c)^2$。
- 计算 $\mathbb{E}g(\boldsymbol{X})$ 直接对 $\boldsymbol{X}$ 的分布积分，不必先求 $g(\boldsymbol{X})$ 的分布。
- 线性性 $\mathbb{E}(c + aX + bY) = c + a\mathbb{E}X + b\mathbb{E}Y$ 无需独立；乘法 $\mathbb{E}(XY) = \mathbb{E}X\,\mathbb{E}Y$ 需要独立（或不相关）。
- 方差 $\operatorname{Var}(X) = \mathbb{E}X^2 - (\mathbb{E}X)^2$；$\operatorname{Var}(aX + b) = a^2\operatorname{Var}(X)$；独立和的方差等于方差之和。
- 不等式：Markov $\mathbb{P}(\lvert X \rvert \ge \varepsilon) \le \mathbb{E}\lvert X \rvert^\alpha/\varepsilon^\alpha$；Chebyshev $\mathbb{P}(\lvert X - \mu \rvert \ge \varepsilon) \le \sigma^2/\varepsilon^2$；Cauchy–Schwarz $\lvert\mathbb{E}XY\rvert \le \sqrt{\mathbb{E}X^2\mathbb{E}Y^2}$；Jensen $\psi(\mathbb{E}X) \le \mathbb{E}\psi(X)$。
- 计算技巧：利用归一性（把积分凑成已知密度）与对称性；离散分布用阶乘矩、对幂级数求导；用示性函数把计数写成和（抽样、配对、集卡问题）；利用随机变量之间的关系（如 $\chi^2_n$ 与正态平方和）计算期望。
