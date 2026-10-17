---
title: 概率母函数、矩母函数、特征函数
---

分布列、密度与分布函数从"每个点或每个区间的概率"出发刻画随机变量；本章介绍另一种完整刻画分布的方式：把分布变换成一个函数，再在这个函数上做运算。三种变换都是某个函数 $h(X)$ 的期望——概率母函数取 $h(X) = s^X$，矩母函数取 $\mathrm{e}^{sX}$，特征函数取 $\mathrm{e}^{\mathrm{i}tX}$。它们的共同优点来自指数的性质：独立随机变量之和的分布（卷积，[3.1.7](/3.1.7)）变成母函数的乘积，随机个随机变量之和变成母函数的复合；同时，矩可以由导数读出，分布又能由母函数唯一确定。三者的适用范围依次扩大：概率母函数只用于取非负整值的随机变量，矩母函数要求 $\mathrm{e}^{sX}$ 在 $0$ 附近可积，特征函数对一切随机变量都存在。本章的最后引入依分布收敛与连续性定理，它们是下面大数定律（[3.1.12](/3.1.12)）与中心极限定理（[3.1.13](/3.1.13)）的主要工具。特征函数本质上就是分布的 Fourier 变换，与 [2.5](/2.5) 中的 Fourier 分析相通。

## 11.1. 概率母函数

概率母函数把非负整值随机变量的分布列 $p_0, p_1, p_2, \dots$ 编码成一个幂级数的系数，从而可以用微积分的工具计算概率、期望和方差。

**定义 11.1.1（概率母函数）** 设 $X$ 是取非负整值的随机变量，称

$$
g(s) = \mathbb{E}(s^X) = \sum_{j=0}^{\infty} s^j\, \mathbb{P}(X = j), \quad s \in [-1, 1]
$$
为 $X$ 的**概率母函数**（probability generating function，PGF），约定 $0^0 = 1$。

由 $\sum_j \lvert s^j \rvert \mathbb{P}(X = j) \le \sum_j \mathbb{P}(X = j) = 1$，级数在 $[-1, 1]$ 上绝对收敛，且 $g(1) = 1$。概率母函数在 $(-1, 1)$ 内可以逐项求任意阶导数。

**性质 11.1.1** 设 $g(s)$ 是 $X$ 的概率母函数，$g^{(k)}(s)$ 是它的 $k$ 阶导数（在 $s = 1$ 处理解为左导数，即 $s \uparrow 1$ 时的极限，可以为 $+\infty$），则

1. $\mathbb{P}(X = k) = \dfrac{g^{(k)}(0)}{k!}$，$k = 0, 1, \dots$；
2. $\mathbb{E}X = g^{(1)}(1)$；
3. 如果 $\mathbb{E}X^2 < \infty$，则 $\operatorname{Var}(X) = g^{(2)}(1) + g^{(1)}(1) - [g^{(1)}(1)]^2$；
4. 如果 $X_1, \dots, X_n$ 相互独立，$g_i(s) = \mathbb{E}(s^{X_i})$ 是 $X_i$ 的概率母函数，则 $Y = X_1 + \cdots + X_n$ 的概率母函数为

$$
g_Y(s) = g_1(s) g_2(s) \cdots g_n(s), \quad s \in [-1, 1].
$$

**证明** 1. 逐项求导，

$$
\frac{g^{(k)}(0)}{k!} = \frac{1}{k!} \sum_{j=k}^{\infty} \frac{\mathrm{d}^k}{\mathrm{d}s^k} s^j\, \mathbb{P}(X = j) \Bigg|_{s=0} = \mathbb{P}(X = k).
$$

2. $g^{(1)}(1) = \sum_{j=0}^{\infty} j\, \mathbb{P}(X = j) = \mathbb{E}X$（由 Abel 定理，$s \uparrow 1$ 时左导数收敛到这个级数，级数发散时两边都是 $+\infty$）。

3. 同理 $g^{(2)}(1) = \sum_j j(j-1) \mathbb{P}(X = j) = \mathbb{E}[X(X-1)]$，于是

$$
g^{(2)}(1) + g^{(1)}(1) - [g^{(1)}(1)]^2 = \mathbb{E}[X(X-1)] + \mathbb{E}X - (\mathbb{E}X)^2 = \mathbb{E}X^2 - (\mathbb{E}X)^2 = \operatorname{Var}(X).
$$

4. $s^{X_1}, \dots, s^{X_n}$ 相互独立，独立随机变量乘积的期望等于期望的乘积：$\mathbb{E}(s^{X_1 + \cdots + X_n}) = \prod_i \mathbb{E}(s^{X_i})$。 $\square$

由性质 1，概率母函数与分布列相互唯一决定：已知母函数，可以求导或作 Taylor 展开读出各项系数。性质 4 是母函数最有用的地方：求独立和的分布不必做卷积，只需把母函数相乘，再从乘积的形式认出分布。

### 11.1.1. 常见分布的概率母函数

**例 11.1.1（二项分布）** $X \sim \mathrm{Bin}(n, p)$，$q = 1 - p$，则

$$
g(s) = \sum_{j=0}^{n} s^j \binom{n}{j} p^j q^{n-j} = (q + sp)^n.
$$
应用：若 $X_1, \dots, X_m$ 相互独立，$X_i \sim \mathrm{Bin}(n_i, p)$，则 $Y = X_1 + \cdots + X_m$ 的母函数为 $(q + sp)^{n_1 + \cdots + n_m}$，所以 $Y \sim \mathrm{Bin}(n_1 + \cdots + n_m, p)$。

**例 11.1.2（Poisson 分布）** $X \sim \mathrm{Poi}(\lambda)$，则

$$
g(s) = \sum_{k=0}^{\infty} s^k \frac{\lambda^k}{k!} \mathrm{e}^{-\lambda} = \mathrm{e}^{\lambda(s-1)}.
$$
应用：若 $X_1, \dots, X_m$ 相互独立，$X_i \sim \mathrm{Poi}(\lambda_i)$，则 $X_1 + \cdots + X_m \sim \mathrm{Poi}(\lambda_1 + \cdots + \lambda_m)$。

**例 11.1.3（几何分布与 Pascal 分布）** $X \sim \mathrm{Geo}(p)$（取值 $1, 2, \dots$），则

$$
g(s) = \sum_{k=1}^{\infty} s^k p q^{k-1} = \frac{sp}{1 - sq}.
$$
设 $X_1, \dots, X_m$ 相互独立，都服从 $\mathrm{Geo}(p)$，则 $S_m = X_1 + \cdots + X_m$ 有母函数 $g_m(s) = \left(\dfrac{sp}{1 - sq}\right)^m$。用负二项级数 $(1 - x)^{-m} = \sum_{j \ge 0} \binom{m + j - 1}{m - 1} x^j$ 展开：

$$
g_m(s) = (sp)^m \sum_{j=0}^{\infty} \binom{m + j - 1}{m - 1} (sq)^j = \sum_{k=m}^{\infty} \binom{k - 1}{m - 1} p^m q^{k-m} s^k,
$$
读出系数即得 Pascal 分布 $\mathrm{Pascal}(m, p)$：

$$
\mathbb{P}(S_m = k) = \binom{k - 1}{m - 1} p^m q^{k-m}, \quad k = m, m+1, \dots
$$
这与"第 $m$ 次成功所需的试验次数"的直接计算一致。

### 11.1.2. 随机个随机变量之和

保险公司一年的总赔付是"理赔次数"个"单笔赔付"之和，其中次数本身也是随机的。这类随机和的分布用母函数处理最为简洁。

**定理 11.1.1** 设

1. $\{X_j\}$ 是一列独立同分布的非负整值随机变量，$X_1$ 的概率母函数为 $g_X(s) = \sum_{k=0}^{\infty} p_k s^k$，$p_k = \mathbb{P}(X_1 = k)$；
2. $N$ 是取正整数值的随机变量，概率母函数为 $g_N(s) = \sum_{n=1}^{\infty} s^n \mathbb{P}(N = n)$；
3. $N$ 与 $\{X_j\}$ 相互独立。

则 $W = X_1 + X_2 + \cdots + X_N$ 的概率母函数为

$$
g_W(s) = g_N(g_X(s)).
$$

**证明** 由全期望公式（定理 9.2.2），

$$
\begin{aligned}
g_W(s) = \mathbb{E}(s^W) &= \sum_{n=1}^{\infty} \mathbb{E}(s^W \mid N = n)\, \mathbb{P}(N = n) = \sum_{n=1}^{\infty} \mathbb{E}(s^{X_1 + \cdots + X_n} \mid N = n)\, \mathbb{P}(N = n) \\
&= \sum_{n=1}^{\infty} \mathbb{E}(s^{X_1 + \cdots + X_n})\, \mathbb{P}(N = n) = \sum_{n=1}^{\infty} [g_X(s)]^n\, \mathbb{P}(N = n) = g_N(g_X(s)),
\end{aligned}
$$
其中第三个等号用到 $N$ 与 $\{X_j\}$ 独立，第四个等号用到性质 11.1.1 的第 4 条。 $\square$

$N$ 允许取 $0$（此时约定 $W = 0$）时，结论同样成立。

**例 11.1.4** 母鸡产蛋的个数 $N \sim \mathrm{Poi}(\lambda)$，每个蛋独立地以概率 $p$ 孵出小鸡，则孵出小鸡的蛋数 $W \sim \mathrm{Poi}(\lambda p)$。

**解** 令 $X_i = 1$ 或 $0$，表示第 $i$ 个蛋是否孵出小鸡，则 $W = X_1 + \cdots + X_N$，$\{X_i\}$ 独立同分布，与 $N$ 独立。$g_X(s) = q + ps$，$g_N(s) = \mathrm{e}^{\lambda(s-1)}$，由定理 11.1.1，

$$
g_W(s) = g_N(g_X(s)) = \mathrm{e}^{\lambda((q + ps) - 1)} = \mathrm{e}^{\lambda p(s-1)}.
$$
这正是 $\mathrm{Poi}(\lambda p)$ 的母函数，由母函数与分布列的相互唯一决定，$W \sim \mathrm{Poi}(\lambda p)$。这一现象称为 Poisson 分布的稀疏化（thinning）。

![Poisson 稀疏化：N ~ Poi(10) 个蛋中每个以 p = 0.3 孵化，模拟所得 W 的频率与 Poi(3) 的分布列](./plots/poisson-thinning.py)

### 11.1.3. 随机向量的概率母函数

**定义 11.1.2** 设 $(X, Y)$ 是取非负整值的二维随机向量，分布列为 $p_{ik} = \mathbb{P}(X = i, Y = k)$，$i, k = 0, 1, 2, \dots$，称

$$
g(s, t) = \mathbb{E}(s^X t^Y) = \sum_{i=0}^{\infty} \sum_{k=0}^{\infty} p_{ik}\, s^i t^k, \quad s, t \in [-1, 1]
$$
为 $(X, Y)$ 的概率母函数。

**性质 11.1.2** 设 $g(s, t)$ 是 $(X, Y)$ 的概率母函数，$g_X$、$g_Y$ 是 $X$、$Y$ 的概率母函数，则

1. $\lvert g(s, t) \rvert \le g(1, 1) = 1$，$\lvert s \rvert \le 1$，$\lvert t \rvert \le 1$；
2. 对非负整数 $a, b, c$，$g_{aX + bY + c}(s) = s^c g(s^a, s^b)$；
3. $X$ 与 $Y$ 独立当且仅当 $g(s, t) = g_X(s) g_Y(t)$ 对一切 $s, t$ 成立；
4. $g(s, 1) = g_X(s)$，$g(1, t) = g_Y(t)$；
5. $p_{ik} = \dfrac{1}{i!\,k!} \dfrac{\partial^{i+k} g(s, t)}{\partial s^i\, \partial t^k}\Big|_{s=t=0}$，$i, k = 0, 1, 2, \dots$；
6. 如果 $\mathbb{E}X, \mathbb{E}Y < \infty$，则 $\mathbb{E}X = \dfrac{\partial g}{\partial s}\Big|_{s=t=1}$，$\mathbb{E}Y = \dfrac{\partial g}{\partial t}\Big|_{s=t=1}$；
7. 如果 $\mathbb{E}X^2, \mathbb{E}Y^2 < \infty$，则

$$
\mathbb{E}X^2 = \frac{\partial^2 g}{\partial s^2}\Big|_{s=t=1} + \frac{\partial g}{\partial s}\Big|_{s=t=1}, \quad \mathbb{E}Y^2 = \frac{\partial^2 g}{\partial t^2}\Big|_{s=t=1} + \frac{\partial g}{\partial t}\Big|_{s=t=1}, \quad \mathbb{E}(XY) = \frac{\partial^2 g}{\partial s\, \partial t}\Big|_{s=t=1}.
$$

第 3 条中"当"的方向由独立性直接得到；"仅当"的方向是因为乘积 $g_X(s) g_Y(t)$ 的展开系数是 $\mathbb{P}(X = i)\mathbb{P}(Y = k)$，由第 5 条，母函数相同则联合分布列相同。

## 11.2. 矩母函数

概率母函数只适用于非负整值的随机变量。把 $s^X$ 换成 $\mathrm{e}^{sX}$（即令 $s = \mathrm{e}^u$），就得到可以用于一般随机变量的矩母函数。

**定义 11.2.1（矩母函数）** 设 $X$ 是随机变量，称

$$
M_X(s) = \mathbb{E}(\mathrm{e}^{sX})
$$
为 $X$ 的**矩母函数**（moment generating function，MGF）。离散型时 $M_X(s) = \sum_j \mathrm{e}^{s x_j}\, \mathbb{P}(X = x_j)$，连续型时 $M_X(s) = \int_{-\infty}^{\infty} \mathrm{e}^{sx} f_X(x)\,\mathrm{d}x$。仅当 $\mathbb{E}(\mathrm{e}^{sX}) < \infty$ 时称 $M_X(s)$ 在 $s$ 处存在。

$M_X(0) = 1$ 总是存在，但对 $s \ne 0$ 可能是 $+\infty$。名称的来历：若 $M_X$ 在 $0$ 的某个邻域内存在，则由 $\mathrm{e}^x$ 的 Taylor 展开，

$$
M_X(s) = \mathbb{E} \sum_{n=0}^{\infty} \frac{(sX)^n}{n!} = \sum_{n=0}^{\infty} \frac{\mathbb{E}X^n}{n!} s^n,
$$
各阶矩恰好是展开式的系数（乘以 $n!$）。

**性质 11.2.1** 设 $M(s)$ 是 $X$ 的矩母函数，$M^{(k)}(s)$ 是它的 $k$ 阶导数，则

1. $Y = aX + b$ 的矩母函数为 $M_Y(s) = \mathrm{e}^{sb} M(sa)$；
2. 若 $M(s)$ 在 $0$ 的某个邻域内存在，则 $\mathbb{E}X^k = M^{(k)}(0)$，$k = 1, 2, \dots$；
3. $M(0) = 1$；当 $X$ 只取非负整数值时，$\mathbb{P}(X = 0) = \lim_{s \to -\infty} M(s)$；
4. 唯一性：如果存在正数 $a$，使得对任意 $s \in [-a, a]$ 有 $M(s) < \infty$，则 $M(s)$ 唯一地决定 $X$ 的分布函数；
5. 如果 $X_1, \dots, X_n$ 相互独立，则 $Y = X_1 + \cdots + X_n$ 的矩母函数为 $M_Y(s) = M_{X_1}(s) \cdots M_{X_n}(s)$。

第 3 条：$X$ 取非负整数值时 $M(s) = \sum_k \mathrm{e}^{sk} \mathbb{P}(X = k)$，$s \to -\infty$ 时除 $k = 0$ 外各项趋于 $0$。第 4 条的证明超出本课程范围；注意它要求矩母函数在 $0$ 的一个邻域内有限，只在 $s = 0$ 处有限是不够的。

**例 11.2.1** 离散型随机变量 $X$ 取 $2, 3, 5$ 的概率分别为 $\frac{1}{2}, \frac{1}{6}, \frac{1}{3}$，求 $M(s)$、$\mathbb{E}X$、$\mathbb{E}X^2$。

**解** $M(s) = \frac{1}{2}\mathrm{e}^{2s} + \frac{1}{6}\mathrm{e}^{3s} + \frac{1}{3}\mathrm{e}^{5s}$，于是

$$
\mathbb{E}X = M^{(1)}(0) = \frac{1}{2} \cdot 2 + \frac{1}{6} \cdot 3 + \frac{1}{3} \cdot 5 = \frac{19}{6}, \qquad \mathbb{E}X^2 = M^{(2)}(0) = \frac{1}{2} \cdot 4 + \frac{1}{6} \cdot 9 + \frac{1}{3} \cdot 25 = \frac{71}{6}.
$$

**例 11.2.2（指数分布）** $X \sim \mathrm{Exp}(\lambda)$，密度 $f(x) = \lambda \mathrm{e}^{-\lambda x}\boldsymbol{1}_{\{x \ge 0\}}$。当 $s < \lambda$ 时

$$
M(s) = \lambda \int_0^{\infty} \mathrm{e}^{sx} \mathrm{e}^{-\lambda x}\,\mathrm{d}x = \frac{\lambda}{\lambda - s} = \left(1 - \frac{s}{\lambda}\right)^{-1},
$$
当 $s \ge \lambda$ 时积分为 $+\infty$。于是 $\mathbb{E}X = M^{(1)}(0) = \frac{\lambda}{(\lambda - s)^2}\big|_{s=0} = \frac{1}{\lambda}$，$\mathbb{E}X^2 = M^{(2)}(0) = \frac{2\lambda}{(\lambda - s)^3}\big|_{s=0} = \frac{2}{\lambda^2}$。也可以直接把 $(1 - s/\lambda)^{-1} = \sum_n s^n/\lambda^n$ 展开，读出 $\mathbb{E}X^n = n!/\lambda^n$。

**例 11.2.3（混合分布）** 银行有三位柜员，服务时间都服从指数分布：两位快速柜员的参数为 $\lambda = 6$，一位慢速柜员的参数为 $\lambda = 4$。顾客等可能地随机选择一位柜员，求其服务时间的矩母函数。

**解** 由全概率公式，服务时间 $X$ 的密度为 $f_X(x) = \left[\frac{2}{3} \cdot 6\mathrm{e}^{-6x} + \frac{1}{3} \cdot 4\mathrm{e}^{-4x}\right] \boldsymbol{1}_{\{x \ge 0\}}$。当 $s < 4$ 时

$$
M_X(s) = \int_0^{\infty} \mathrm{e}^{sx} \left[\frac{2}{3} \cdot 6\mathrm{e}^{-6x} + \frac{1}{3} \cdot 4\mathrm{e}^{-4x}\right] \mathrm{d}x = \frac{2}{3} \cdot \frac{6}{6 - s} + \frac{1}{3} \cdot \frac{4}{4 - s}.
$$
反过来，由唯一性，若已知 $X$ 的矩母函数形如 $p_1 \frac{\lambda_1}{\lambda_1 - s} + p_2 \frac{\lambda_2}{\lambda_2 - s}$（$p_1 + p_2 = 1$），则 $X$ 是 $\mathrm{Exp}(\lambda_1)$ 与 $\mathrm{Exp}(\lambda_2)$ 以概率 $p_1, p_2$ 混合而成的，密度为 $p_1 f_{X_1}(x) + p_2 f_{X_2}(x)$。

**例 11.2.4（正态分布）** 设 $X \sim \mathcal{N}(\mu_1, \sigma_1^2)$，$Y \sim \mathcal{N}(\mu_2, \sigma_2^2)$ 相互独立，求 $Z = X + Y$ 的分布。

**解** 若 $V \sim \mathcal{N}(0, 1)$，配方得

$$
M_V(s) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \mathrm{e}^{sx - x^2/2}\,\mathrm{d}x = \mathrm{e}^{s^2/2} \cdot \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \mathrm{e}^{-(x - s)^2/2}\,\mathrm{d}x = \mathrm{e}^{s^2/2}.
$$
$W = \mu + \sigma V \sim \mathcal{N}(\mu, \sigma^2)$，由性质 11.2.1 的第 1 条，$M_W(s) = \mathrm{e}^{\mu s + \sigma^2 s^2/2}$。再由第 5 条，

$$
M_Z(s) = M_X(s) M_Y(s) = \exp\left\{(\mu_1 + \mu_2)s + \frac{(\sigma_1^2 + \sigma_2^2)s^2}{2}\right\},
$$
它对一切 $s$ 有限，且是 $\mathcal{N}(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$ 的矩母函数，由第 4 条，$Z \sim \mathcal{N}(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$。独立正态随机变量之和仍是正态的。

顺便求出标准正态分布的各阶矩：$M_V(s) = \mathrm{e}^{s^2/2} = \sum_{k=0}^{\infty} \frac{s^{2k}}{2^k k!}$，与 $\sum_n \frac{\mathbb{E}V^n}{n!} s^n$ 比较系数，得 $\mathbb{E}V^{2k-1} = 0$，$\mathbb{E}V^{2k} = \frac{(2k)!}{2^k k!} = (2k-1)!!$。例如 $\mathbb{E}V^4 = 3$。

### 11.2.1. 随机个随机变量之和

**定理 11.2.1** 设 $X_1, X_2, \dots$ 独立同分布，有共同的矩母函数 $M_X(s)$；$N$ 是取正整数值的随机变量，与 $\{X_j\}$ 独立；$W = X_1 + \cdots + X_N$。则

$$
M_W(s) = \mathbb{E}\left[(M_X(s))^N\right] = \sum_{n=1}^{\infty} (M_X(s))^n\, \mathbb{P}(N = n).
$$

**证明** 由独立性，$\mathbb{E}(\mathrm{e}^{sW} \mid N = n) = \mathbb{E}(\mathrm{e}^{sX_1} \cdots \mathrm{e}^{sX_n}) = (M_X(s))^n$，再由重期望公式（定理 9.3.1），$M_W(s) = \mathbb{E}[\mathbb{E}(\mathrm{e}^{sW} \mid N)] = \mathbb{E}[(M_X(s))^N]$。 $\square$

与 $M_N(s) = \sum_n (\mathrm{e}^s)^n \mathbb{P}(N = n)$ 比较：$M_W$ 就是在 $M_N$ 中把 $\mathrm{e}^s$ 换成 $M_X(s)$。这与定理 11.1.1 中"把 $g_N$ 中的 $s$ 换成 $g_X(s)$"是同一件事。

**例 11.2.5** 小明沿一条满是书店的街道找一本书。每家店有此书的概率都是 $p$，各店相互独立；他在每家店花费的时间服从 $\mathrm{Exp}(\lambda)$，与其他一切独立；他一直逛下去直到买到为止。求逛书店的总时间 $W$ 的分布。

**解** 设逛的店数为 $N \sim \mathrm{Geo}(p)$，在各店花费的时间为 $X_i \sim \mathrm{Exp}(\lambda)$，$W = X_1 + \cdots + X_N$。当 $s < \lambda$ 时 $M_X(s) = \frac{\lambda}{\lambda - s}$，而 $M_N(s) = \frac{p\mathrm{e}^s}{1 - (1 - p)\mathrm{e}^s}$，所以

$$
M_W(s) = \frac{p M_X(s)}{1 - (1 - p) M_X(s)} = \frac{p\lambda}{p\lambda - s}, \quad s < p\lambda,
$$
即 $W \sim \mathrm{Exp}(p\lambda)$。对比：固定个数的和 $X_1 + \cdots + X_n$ 的矩母函数是 $\left(\frac{\lambda}{\lambda - s}\right)^n$，服从 $\Gamma(n, \lambda)$。

### 11.2.2. 随机向量的矩母函数与矩母函数的局限

**定义 11.2.2** 设 $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T}$ 是随机向量，称

$$
M_{\boldsymbol{X}}(\boldsymbol{s}) = \mathbb{E}\left(\mathrm{e}^{\boldsymbol{s}^{\mathsf T}\boldsymbol{X}}\right) = \mathbb{E}\left(\mathrm{e}^{s_1 X_1 + \cdots + s_n X_n}\right), \quad \boldsymbol{s} = (s_1, \dots, s_n)^{\mathsf T} \in \mathbb{R}^n
$$
为 $\boldsymbol{X}$ 的（多元）矩母函数。

矩母函数的局限在于它可能不存在。例如标准 Cauchy 分布（密度 $\frac{1}{\pi(1 + x^2)}$）对任何 $s > 0$，

$$
\mathbb{E}\mathrm{e}^{sX} = \int_{-\infty}^{\infty} \frac{\mathrm{e}^{sx}}{\pi(1 + x^2)}\,\mathrm{d}x \ge \int_0^{\infty} \frac{\mathrm{e}^{sx}}{\pi(1 + x^2)}\,\mathrm{d}x = +\infty,
$$
因为被积函数在 $x \to +\infty$ 时趋于无穷；$s < 0$ 同理。所以 Cauchy 分布的矩母函数只在 $s = 0$ 处有限，性质 11.2.1 中的唯一性与求矩都无从谈起。

**注 11.2.1** 矩与矩母函数的关系有两点容易误解。

- 各阶矩都存在，矩母函数也可能不存在。例如 $X \sim \mathcal{N}(\mu, \sigma^2)$，$Y = \mathrm{e}^X$（对数正态分布）的各阶矩 $\mathbb{E}Y^n = \mathrm{e}^{n\mu + n^2\sigma^2/2}$ 都有限，但对任何 $s > 0$，$\mathbb{E}\mathrm{e}^{sY} = +\infty$。
- 两个随机变量的各阶矩完全相同，分布也可能不同。例如 $X_1$ 有密度 $f_1(x) = \frac{1}{\sqrt{2\pi}\,x} \mathrm{e}^{-(\ln x)^2/2}\boldsymbol{1}_{\{x > 0\}}$（标准对数正态），$X_2$ 有密度 $f_2(x) = f_1(x)[1 + \sin(2\pi \ln x)]$，两者各阶矩都相同，但分布不同。只有在矩母函数存在于 $0$ 的邻域内时，矩序列才唯一决定分布。

## 11.3. 特征函数

把矩母函数中的实数 $s$ 换成纯虚数 $\mathrm{i}t$，被积函数 $\mathrm{e}^{\mathrm{i}tX}$ 的模恒为 $1$，期望对一切随机变量和一切 $t$ 都存在。这就是特征函数，它是三种工具中适用范围最广的一种。

**定义 11.3.1（特征函数）** 对随机变量 $X$，称

$$
\varphi(t) = \mathbb{E}(\mathrm{e}^{\mathrm{i}tX}) = \mathbb{E}\cos(tX) + \mathrm{i}\,\mathbb{E}\sin(tX), \quad t \in \mathbb{R}
$$
为 $X$ 的**特征函数**（characteristic function，CF），其中 $\mathrm{i} = \sqrt{-1}$。

若 $X$ 有密度 $f$，则 $\varphi(t) = \int_{-\infty}^{\infty} \mathrm{e}^{\mathrm{i}tx} f(x)\,\mathrm{d}x$，即密度的 Fourier 变换（相差一个符号约定）。

**性质 11.3.1** 设 $\varphi(t) = \mathbb{E}(\mathrm{e}^{\mathrm{i}tX})$，则

1. $\lvert \varphi(t) \rvert \le \varphi(0) = 1$，$\varphi(-t) = \overline{\varphi(t)}$；
2. $\varphi(t)$ 在 $(-\infty, \infty)$ 上一致连续：$\lvert \varphi(t + h) - \varphi(t) \rvert \le \mathbb{E}\lvert \mathrm{e}^{\mathrm{i}hX} - 1 \rvert$，右端与 $t$ 无关，且 $h \to 0$ 时趋于 $0$；
3. 如果 $\mathbb{E}\lvert X \rvert^k < \infty$，则 $\varphi^{(k)}(t) = \mathrm{i}^k \mathbb{E}(X^k \mathrm{e}^{\mathrm{i}tX})$，特别地 $\varphi^{(k)}(0) = \mathrm{i}^k \mathbb{E}X^k$；
4. 对任意常数 $a, b$，$\varphi_{aX + b}(t) = \mathrm{e}^{\mathrm{i}tb} \varphi_X(at)$；
5. 如果 $X_k$ 有特征函数 $\varphi_k(t)$，且 $X_1, \dots, X_n$ 相互独立，则 $Y = X_1 + \cdots + X_n$ 的特征函数为 $\varphi_Y(t) = \prod_{k=1}^{n} \varphi_k(t)$。

第 1 条由 $\lvert \mathrm{e}^{\mathrm{i}tX} \rvert = 1$ 与 $\mathrm{e}^{-\mathrm{i}tX} = \overline{\mathrm{e}^{\mathrm{i}tX}}$ 得到。第 2 条：$\lvert \mathrm{e}^{\mathrm{i}(t+h)X} - \mathrm{e}^{\mathrm{i}tX} \rvert = \lvert \mathrm{e}^{\mathrm{i}hX} - 1 \rvert \le 2$，由控制收敛定理，$h \to 0$ 时期望趋于 $0$。第 3 条是在期望号下求导，由 $\lvert X^k \mathrm{e}^{\mathrm{i}tX} \rvert = \lvert X \rvert^k$ 可积保证。

### 11.3.1. 常见分布的特征函数

**例 11.3.1（二项分布）** $X \sim \mathrm{Bin}(n, p)$：$\varphi(t) = \sum_{j=0}^{n} \mathrm{e}^{\mathrm{i}tj} \binom{n}{j} p^j q^{n-j} = (q + p\mathrm{e}^{\mathrm{i}t})^n$。

**例 11.3.2（Poisson 分布）** $X \sim \mathrm{Poi}(\lambda)$：$\varphi(t) = \sum_{k=0}^{\infty} \mathrm{e}^{\mathrm{i}tk} \frac{\lambda^k}{k!} \mathrm{e}^{-\lambda} = \mathrm{e}^{\lambda(\mathrm{e}^{\mathrm{i}t} - 1)}$。

**例 11.3.3（几何分布）** $X \sim \mathrm{Geo}(p)$：$\varphi(t) = \sum_{k=1}^{\infty} \mathrm{e}^{\mathrm{i}tk} p q^{k-1} = \dfrac{p\mathrm{e}^{\mathrm{i}t}}{1 - q\mathrm{e}^{\mathrm{i}t}}$。

**例 11.3.4（均匀分布）** $X \sim \mathrm{U}(a, b)$：$\varphi(t) = \dfrac{\mathrm{e}^{\mathrm{i}tb} - \mathrm{e}^{\mathrm{i}ta}}{\mathrm{i}t(b - a)}$（$t \ne 0$）。特别地，$\mathrm{U}(-c, c)$ 的特征函数是 $\dfrac{\sin(ct)}{ct}$。

**例 11.3.5（指数分布）** $X \sim \mathrm{Exp}(\lambda)$：$\varphi(t) = \left(1 - \dfrac{\mathrm{i}t}{\lambda}\right)^{-1}$。与例 11.2.2 的矩母函数 $(1 - s/\lambda)^{-1}$ 对照，形式上就是 $s$ 换成 $\mathrm{i}t$。

**例 11.3.6（正态分布）** $X \sim \mathcal{N}(\mu, \sigma^2)$ 的特征函数为

$$
\varphi(t) = \exp\left(\mathrm{i}\mu t - \frac{1}{2}\sigma^2 t^2\right).
$$

**解** (i) 先求 $\mathcal{N}(0, 1)$ 的特征函数。形式上把 $\mathrm{i}$ 当作常数配方，$\varphi(t) = \mathrm{e}^{-t^2/2} \cdot \frac{1}{\sqrt{2\pi}} \int \mathrm{e}^{-(x - \mathrm{i}t)^2/2}\,\mathrm{d}x = \mathrm{e}^{-t^2/2}$；这一步的严格化需要复变函数的围道积分。下面给出只用实分析的推导。由对称性，

$$
\varphi(t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \cos(tx)\, \mathrm{e}^{-x^2/2}\,\mathrm{d}x,
$$
在积分号下求导并分部积分，

$$
\varphi'(t) = -\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} x \sin(tx)\, \mathrm{e}^{-x^2/2}\,\mathrm{d}x = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \sin(tx)\,\mathrm{d}\mathrm{e}^{-x^2/2} = -\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} t\cos(tx)\, \mathrm{e}^{-x^2/2}\,\mathrm{d}x = -t\varphi(t).
$$
于是 $\frac{\mathrm{d}}{\mathrm{d}t}\left[\varphi(t)\mathrm{e}^{t^2/2}\right] = [\varphi'(t) + t\varphi(t)]\mathrm{e}^{t^2/2} = 0$，$\varphi(t)\mathrm{e}^{t^2/2} \equiv \varphi(0) = 1$，即 $\varphi(t) = \mathrm{e}^{-t^2/2}$。

(ii) 设 $Y \sim \mathcal{N}(\mu, \sigma^2)$，则 $Y = \mu + \sigma X$，$X \sim \mathcal{N}(0, 1)$，由性质 11.3.1 的第 4 条，$\mathbb{E}\mathrm{e}^{\mathrm{i}tY} = \mathrm{e}^{\mathrm{i}t\mu} \mathbb{E}\mathrm{e}^{\mathrm{i}t\sigma X} = \exp\left(\mathrm{i}\mu t - \frac{1}{2}\sigma^2 t^2\right)$。 $\square$

由第 5 条，若 $X_1, \dots, X_m$ 相互独立，$X_j \sim \mathcal{N}(\mu_j, \sigma_j^2)$，则 $X_1 + \cdots + X_m \sim \mathcal{N}\left(\sum_j \mu_j, \sum_j \sigma_j^2\right)$。

下面两例的计算需要复变函数或较繁的积分技巧，结论可以直接使用。

**例 11.3.7（Cauchy 分布）** 标准 Cauchy 分布（密度 $f(x) = \frac{1}{\pi(1 + x^2)}$，$x \in \mathbb{R}$）的特征函数为 $\varphi(t) = \mathrm{e}^{-\lvert t \rvert}$。它在 $t = 0$ 处不可导，与 Cauchy 分布期望不存在相吻合。

**例 11.3.8（Laplace 分布）** 密度为 $f(x) = \frac{1}{2}\mathrm{e}^{-\lvert x \rvert}$ 的 Laplace 分布的特征函数为 $\varphi(t) = \dfrac{1}{1 + t^2}$。

例 11.3.7 与例 11.3.8 互为对偶：Laplace 密度的 Fourier 变换是 Cauchy 型函数，反之亦然。

![几种对称分布的特征函数：N(0,1)、U(-1,1)、Laplace 与标准 Cauchy；对称分布的特征函数是实值偶函数](./plots/characteristic-functions.py)

三种母函数对照如下（$q = 1 - p$；"—"表示不适用或不存在）：

| 分布 | 概率母函数 $g(s)$ | 矩母函数 $M(s)$ | 特征函数 $\varphi(t)$ |
|---|---|---|---|
| $\mathrm{Bin}(n, p)$ | $(q + ps)^n$ | $(q + p\mathrm{e}^s)^n$ | $(q + p\mathrm{e}^{\mathrm{i}t})^n$ |
| $\mathrm{Poi}(\lambda)$ | $\mathrm{e}^{\lambda(s - 1)}$ | $\mathrm{e}^{\lambda(\mathrm{e}^s - 1)}$ | $\mathrm{e}^{\lambda(\mathrm{e}^{\mathrm{i}t} - 1)}$ |
| $\mathrm{Geo}(p)$ | $\dfrac{ps}{1 - qs}$ | $\dfrac{p\mathrm{e}^s}{1 - q\mathrm{e}^s}$，$s < -\ln q$ | $\dfrac{p\mathrm{e}^{\mathrm{i}t}}{1 - q\mathrm{e}^{\mathrm{i}t}}$ |
| $\mathrm{U}(a, b)$ | — | $\dfrac{\mathrm{e}^{sb} - \mathrm{e}^{sa}}{s(b - a)}$ | $\dfrac{\mathrm{e}^{\mathrm{i}tb} - \mathrm{e}^{\mathrm{i}ta}}{\mathrm{i}t(b - a)}$ |
| $\mathrm{Exp}(\lambda)$ | — | $\dfrac{\lambda}{\lambda - s}$，$s < \lambda$ | $\left(1 - \dfrac{\mathrm{i}t}{\lambda}\right)^{-1}$ |
| $\mathcal{N}(\mu, \sigma^2)$ | — | $\mathrm{e}^{\mu s + \sigma^2 s^2/2}$ | $\mathrm{e}^{\mathrm{i}\mu t - \sigma^2 t^2/2}$ |
| 标准 Cauchy | — | —（仅 $s = 0$ 有限） | $\mathrm{e}^{-\lvert t \rvert}$ |

### 11.3.2. 特征函数与分布函数

特征函数之所以能代替分布函数，是因为两者相互唯一决定，而且可以由特征函数显式地反求分布函数。

**定理 11.3.1（逆转公式）** 设 $\varphi(t)$ 是 $X$ 的特征函数，$F(x)$ 是 $X$ 的分布函数。如果 $F$ 在 $a, b$（$a < b$）处连续，则

$$
F(b) - F(a) = \frac{1}{2\pi} \lim_{T \to \infty} \int_{-T}^{T} \frac{\mathrm{e}^{-\mathrm{i}ta} - \mathrm{e}^{-\mathrm{i}tb}}{\mathrm{i}t} \varphi(t)\,\mathrm{d}t.
$$

**推论 11.3.1（唯一性定理）** 随机变量的特征函数与分布函数相互唯一决定：两个随机变量的特征函数相同，当且仅当它们同分布。

**证明** 分布函数决定特征函数是定义本身。反之，$F$ 的连续点在 $\mathbb{R}$ 中稠密（不连续点至多可列），由定理 11.3.1，$\varphi$ 决定了 $F$ 在任意两个连续点处的差；令 $a \to -\infty$ 沿连续点趋于负无穷，得 $F(b)$ 在每个连续点的值，再由右连续性得到 $F$ 在所有点的值。 $\square$

**定理 11.3.2** 如果 $X$ 的特征函数满足 $\int_{\mathbb{R}} \lvert \varphi(t) \rvert\,\mathrm{d}t < \infty$，则 $X$ 有连续的密度函数

$$
f(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \mathrm{e}^{-\mathrm{i}tx} \varphi(t)\,\mathrm{d}t.
$$

这正是 **Fourier 反演定理**的概率版本。例如由 $\int \mathrm{e}^{-\lvert t \rvert}\,\mathrm{d}t < \infty$ 和例 11.3.7 可以验证 Cauchy 密度；由 Laplace 分布的特征函数 $\frac{1}{1 + t^2}$ 反过来可以算出 Cauchy 分布的特征函数。这两个定理的证明需要较多的分析技巧，这里不作要求，重要的是推论 11.3.1 的结论：求出一个随机变量的特征函数并认出它属于哪个分布，就确定了这个随机变量的分布。

### 11.3.3. 特征函数与矩

**定理 11.3.3** 如果 $\mathbb{E}\lvert X \rvert^n < \infty$，则 $X$ 的特征函数满足

$$
\varphi(t) = \sum_{m=0}^{n} \frac{\mathbb{E}[(\mathrm{i}tX)^m]}{m!} + o(t^n), \quad t \to 0.
$$
特别地，如果 $\mathbb{E}X^2 < \infty$，则

$$
\varphi(t) = 1 + \mathrm{i}t\,\mathbb{E}X - \frac{1}{2}t^2\,\mathbb{E}X^2 + o(t^2). \tag{11.1}
$$

这是性质 11.3.1 第 3 条与 Taylor 公式的结合。注意 $\mathbb{E}\lvert X \rvert^n < \infty$ 蕴含所有低阶矩有限：由 **Jensen 不等式**（或 $\lvert x \rvert^m \le 1 + \lvert x \rvert^n$，$m \le n$），高阶矩存在则低阶矩存在。式 (11.1) 是中心极限定理证明的出发点（[3.1.13](/3.1.13)）。

### 11.3.4. 混合分布与随机向量的特征函数

**定理 11.3.4（混合分布）** 设分布函数 $F_1(x), \dots, F_m(x)$ 的特征函数分别为 $\varphi_1(t), \dots, \varphi_m(t)$，$\lambda_k \ge 0$，$\sum_{k=1}^{m} \lambda_k = 1$，则混合分布 $\sum_{k=1}^{m} \lambda_k F_k$ 的特征函数为 $\sum_{k=1}^{m} \lambda_k \varphi_k(t)$。

混合分布的例子见例 11.2.3。注意 $Y \sim \sum_k \lambda_k F_k$ 的含义是"$Y$ 以概率 $\lambda_k$ 取分布为 $F_k$ 的 $X_k$ 的值"，对 $X_1, \dots, X_m$ 之间的独立性没有要求；此时 $Y$ 一般不等于线性组合 $\sum_k \lambda_k X_k$。

**定义 11.3.2** 设 $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T}$ 是随机向量，称

$$
\varphi(\boldsymbol{t}) = \mathbb{E}\left(\mathrm{e}^{\mathrm{i}\boldsymbol{t}^{\mathsf T}\boldsymbol{X}}\right), \quad \boldsymbol{t} = (t_1, \dots, t_n)^{\mathsf T} \in \mathbb{R}^n
$$
为 $\boldsymbol{X}$ 的特征函数。

与一维情形一样，随机向量的特征函数与联合分布函数相互唯一决定。由此得到独立性的特征函数判别法。

**定理 11.3.5** 设 $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T}$ 是随机向量，$\varphi_k(t_k)$ 是 $X_k$ 的特征函数，则 $X_1, \dots, X_n$ 相互独立的充要条件是

$$
\varphi(\boldsymbol{t}) = \varphi_1(t_1) \varphi_2(t_2) \cdots \varphi_n(t_n), \quad \boldsymbol{t} \in \mathbb{R}^n.
$$

**证明** 必要性：$\mathrm{e}^{\mathrm{i}t_1 X_1}, \dots, \mathrm{e}^{\mathrm{i}t_n X_n}$ 相互独立，乘积的期望等于期望的乘积。充分性：取 $Y_1, \dots, Y_n$ 相互独立且 $Y_k$ 与 $X_k$ 同分布，则 $(Y_1, \dots, Y_n)$ 的特征函数也是 $\prod_k \varphi_k(t_k)$，由唯一性，$\boldsymbol{X}$ 与 $(Y_1, \dots, Y_n)^{\mathsf T}$ 同分布，故 $X_1, \dots, X_n$ 相互独立。 $\square$

**例 11.3.9** 设 $X$ 服从标准 Cauchy 分布，$Y = aX$（$a > 0$），则 $\varphi_{X+Y}(t) = \varphi_X(t)\varphi_Y(t)$，但 $X$ 与 $Y$ 并不独立。

**解** $\varphi_X(t) = \mathrm{e}^{-\lvert t \rvert}$，$\varphi_Y(t) = \mathbb{E}\mathrm{e}^{\mathrm{i}(at)X} = \mathrm{e}^{-a\lvert t \rvert}$，$\varphi_{X+Y}(t) = \mathbb{E}\mathrm{e}^{\mathrm{i}t(1 + a)X} = \mathrm{e}^{-(1 + a)\lvert t \rvert} = \varphi_X(t)\varphi_Y(t)$。

此例说明：和的特征函数等于特征函数之积，推不出独立；判断独立性必须用定理 11.3.5 中的联合特征函数 $\varphi(t_1, t_2)$。

至此我们有三套完整刻画随机变量全部信息的工具：离散型随机变量用分布列、分布函数、特征函数；连续型随机变量用密度、分布函数、特征函数；一般的随机变量用分布函数、特征函数。相应地，独立性有三种等价的判别方式。

**推论 11.3.2** 设随机向量 $\boldsymbol{X}_1$、$\boldsymbol{X}_2$ 的联合分布函数、联合密度（若存在）、联合特征函数分别为 $F(\boldsymbol{x}_1, \boldsymbol{x}_2)$、$f(\boldsymbol{x}_1, \boldsymbol{x}_2)$、$\varphi(\boldsymbol{t}_1, \boldsymbol{t}_2)$，各自的边缘分布函数、密度、特征函数为 $F_i$、$f_i$、$\varphi_i$。则 $\boldsymbol{X}_1$ 与 $\boldsymbol{X}_2$ 相互独立的充要条件是下列任一条成立：

1. $F(\boldsymbol{x}_1, \boldsymbol{x}_2) = F_1(\boldsymbol{x}_1) F_2(\boldsymbol{x}_2)$；
2. $f(\boldsymbol{x}_1, \boldsymbol{x}_2) = f_1(\boldsymbol{x}_1) f_2(\boldsymbol{x}_2)$（连续型）；
3. $\varphi(\boldsymbol{t}_1, \boldsymbol{t}_2) = \varphi_1(\boldsymbol{t}_1) \varphi_2(\boldsymbol{t}_2)$。

### 11.3.5. 特征函数与依分布收敛

特征函数的另一项重要用途是判断随机变量序列的分布是否收敛。先给出分布收敛的定义，它将在 [3.1.13](/3.1.13) 与 [3.1.14](/3.1.14) 中详细讨论。

**定义 11.3.3（依分布收敛）** 设 $X$ 有分布函数 $F(x)$，$X_n$ 有分布函数 $F_n(x)$。如果在 $F(x)$ 的每个连续点 $x$ 处都有

$$
\lim_{n \to \infty} F_n(x) = F(x),
$$
则称 $X_n$ **依分布收敛**到 $X$（convergence in distribution），记作 $X_n \xrightarrow{d} X$；也称 $F_n$ **弱收敛**到 $F$（weak convergence），记作 $F_n \xrightarrow{w} F$。

只要求在 $F$ 的连续点处收敛，是因为在跳跃点处要求收敛过于苛刻：例如 $X_n \equiv 1/n$ 应当"收敛"到 $X \equiv 0$，但 $F_n(0) = 0 \not\to F(0) = 1$。

**定理 11.3.6（连续性定理）** 设 $X_n$ 的特征函数为 $\varphi_n(t)$，$X$ 的特征函数为 $\varphi(t)$，则 $X_n \xrightarrow{d} X$ 的充分必要条件是

$$
\lim_{n \to \infty} \varphi_n(t) = \varphi(t), \quad \forall t \in \mathbb{R}.
$$

这是概率论中最常用、最重要的定理之一：要证明依分布收敛，只需证明特征函数逐点收敛，而独立和的特征函数是乘积，计算起来比分布函数容易得多。它也有不预先知道极限分布的形式。

**定理 11.3.7** 设随机向量 $\boldsymbol{X}_n$ 的特征函数 $\varphi_n(\boldsymbol{t})$ 逐点收敛到一个在 $\boldsymbol{t} = \boldsymbol{0}$ 处连续的函数 $\varphi(\boldsymbol{t})$，则 $\varphi(\boldsymbol{t})$ 是某个随机向量 $\boldsymbol{X}$ 的特征函数，并且对任何与 $\boldsymbol{X}$ 同维的常数向量 $\boldsymbol{a}$，有 $\boldsymbol{a}^{\mathsf T}\boldsymbol{X}_n \xrightarrow{d} \boldsymbol{a}^{\mathsf T}\boldsymbol{X}$。

此定理建立了多元与一元的联系，其推论与应用见 [3.1.14](/3.1.14)。在满足唯一性条件（性质 11.2.1 第 4 条）时，概率母函数、矩母函数也可以代替特征函数用于连续性定理。

## 小结

三种母函数的对照（$X_1, X_2, \dots$ 独立；随机和中 $\{X_i\}$ 独立同分布且与 $N$ 独立）：

| | 概率母函数 | 矩母函数 | 特征函数 |
|---|---|---|---|
| 定义 | $g(s) = \mathbb{E}s^X = \sum_k p_k s^k$ | $M(s) = \mathbb{E}\mathrm{e}^{sX} = \sum_n \frac{\mathbb{E}X^n}{n!}s^n$ | $\varphi(t) = \mathbb{E}\mathrm{e}^{\mathrm{i}tX} = \sum_n \frac{\mathbb{E}X^n}{n!}(\mathrm{i}t)^n$ |
| 适用范围 | 非负整值 | $0$ 附近有限的随机变量 | 一切随机变量 |
| 唯一性 | 与分布列一一对应 | $0$ 的邻域内有限时决定分布 | 与分布函数一一对应 |
| 求矩 | $\mathbb{E}X = g'(1)$，$\mathbb{E}X(X-1) = g''(1)$ | $\mathbb{E}X^k = M^{(k)}(0)$ | $\mathbb{E}X^k = \varphi^{(k)}(0)/\mathrm{i}^k$ |
| 独立和 $\sum X_i$ | $\prod g_i(s)$ | $\prod M_i(s)$ | $\prod \varphi_i(t)$ |
| $aX + b$ | $s^b g(s^a)$（$a, b$ 为非负整数） | $\mathrm{e}^{sb}M(as)$ | $\mathrm{e}^{\mathrm{i}tb}\varphi(at)$ |
| 随机和 $X_1 + \cdots + X_N$ | $g_N(g_X(s))$ | $M_N$ 中 $\mathrm{e}^s \to M_X(s)$ | $\varphi_N$ 中 $\mathrm{e}^{\mathrm{i}t} \to \varphi_X(t)$ |
| 二维 | $\mathbb{E}(s^X t^Y)$ | $\mathbb{E}(\mathrm{e}^{sX + tY})$ | $\mathbb{E}(\mathrm{e}^{\mathrm{i}t_1X + \mathrm{i}t_2Y})$ |

使用这些工具的基本套路是：由已知的母函数（如 $g_X$、$g_N$）通过乘积或复合求出未知随机变量的母函数，再利用唯一性，求导或 Taylor 展开读出分布列，或者直接从母函数的形式认出分布及其参数。解题时选择能解决问题的最简单的工具：非负整值的问题用概率母函数，矩母函数存在时用它求矩，一般情形与极限问题用特征函数。
