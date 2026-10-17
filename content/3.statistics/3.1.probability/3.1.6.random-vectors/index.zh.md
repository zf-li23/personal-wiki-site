---
title: 随机向量的分布
---

前几章研究的是单个随机变量：它的分布由分布函数完整刻画，离散型用分布列、连续型用概率密度计算（[3.1.4](/3.1.4)、[3.1.5](/3.1.5)）。实际问题中常常要同时观察同一个试验的几个数量指标，例如一个人的身高与体重、两颗骰子的点数，这时只知道每个指标各自的分布是不够的，还需要知道它们如何共同变化。本章把分布函数、分布列与概率密度推广到随机向量：先定义联合分布与边缘分布，再分别讨论离散型与连续型随机向量，给出独立性的判定法则；然后介绍最重要的连续型随机向量——二元正态分布；最后定义条件分布，它描述在已知一个分量取值的条件下另一个分量的分布。阅读本章时要抓住两组对照：全面与片面（联合与边缘），以及分布函数与分布列、密度之间的转换。本章是后面随机向量函数的分布（[3.1.7](/3.1.7)）、条件期望（[3.1.9](/3.1.9)）、协方差（[3.1.10](/3.1.10)）和多元正态分布（[3.1.15](/3.1.15)）的基础。

## 6.1. 随机向量与联合分布

**定义 6.1.1（随机向量）** 如果 $X_1, \dots, X_n$ 都是概率空间 $(\Omega, \mathcal{F}, \mathbb{P})$ 上的随机变量，称 $\boldsymbol{X} = (X_1, \dots, X_n)$ 是 $(\Omega, \mathcal{F}, \mathbb{P})$ 上的 $n$ 维**随机向量**。

随机向量把每个样本点 $\omega$ 映为 $\mathbb{R}^n$ 中的一点 $\boldsymbol{X}(\omega) = (X_1(\omega), \dots, X_n(\omega))$。对 $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^n$，下面记 $\boldsymbol{x} \le \boldsymbol{y}$ 表示 $x_j \le y_j$（$j = 1, \dots, n$）。

**定义 6.1.2（联合分布函数）** 设 $\boldsymbol{X} = (X_1, \dots, X_n)$ 是随机向量，称 $\mathbb{R}^n$ 上的 $n$ 元函数

$$
F(x_1, \dots, x_n) = \mathbb{P}(X_1 \le x_1, \dots, X_n \le x_n), \quad \text{即 } F(\boldsymbol{x}) = \mathbb{P}(\boldsymbol{X} \le \boldsymbol{x}),
$$
为 $\boldsymbol{X}$ 的**联合分布函数**，简称分布函数或联合分布。

与一元分布函数类似，联合分布函数关于每个自变元单调不减、右连续；令某个 $x_j \to -\infty$ 时 $F \to 0$，令全部 $x_j \to +\infty$ 时 $F \to 1$。

**例 6.1.1** 设 $F(x, y)$ 是 $(X, Y)$ 的联合分布函数，$a < b$，$c < d$。对矩形 $D = \{(x, y) \mid a < x \le b,\ c < y \le d\}$，由概率的加减运算得

$$
\mathbb{P}((X, Y) \in D) = \mathbb{P}(a < X \le b,\ c < Y \le d) = F(b, d) - F(b, c) - F(a, d) + F(a, c).
$$
因此联合分布函数还满足 $F(b, d) - F(b, c) - F(a, d) + F(a, c) \ge 0$。这一条不能由"关于每个变元单调"推出，是二元分布函数特有的条件。

**定义 6.1.3（边缘分布）** 设 $1 \le k < n$，$S_k = \{i_1, \dots, i_k\} \subset \{1, \dots, n\}$ 是指标集，称 $\boldsymbol{X}_{S_k} = (X_{i_1}, \dots, X_{i_k})$ 的联合分布函数

$$
F_{S_k}(x_{i_1}, \dots, x_{i_k}) = \mathbb{P}(X_{i_1} \le x_{i_1}, \dots, X_{i_k} \le x_{i_k}) = \mathbb{P}(X_j \le x_j,\ j \in S_k;\ X_t < \infty,\ t \notin S_k)
$$
为 $F(x_1, \dots, x_n)$ 的 $k$ 维**边缘分布**（也称边际分布）。

$n$ 维分布函数共有 $2^n - 2$ 个边缘分布。特别地，二维情形

$$
F_X(x) = \mathbb{P}(X \le x, Y < \infty) = F(x, +\infty), \qquad F_Y(y) = F(+\infty, y).
$$
即由联合分布函数得到边缘分布函数，只需把不关心的分量取为 $+\infty$，不需要积分（对密度才需要积分，见 §6.3）。

**注 6.1.1** 联合分布唯一决定所有边缘分布，反之不然：只知道 $X$ 与 $Y$ 各自的分布，一般无法确定 $(X, Y)$ 的联合分布。例如 $X \sim \mathcal{N}(0,1)$，取 $Y = X$ 或取与 $X$ 独立的 $Y \sim \mathcal{N}(0,1)$，两者的边缘分布相同，联合分布却完全不同。边缘分布能决定联合分布的重要情形是独立：按 [3.1.3](/3.1.3) 的定义，$X_1, \dots, X_n$ 相互独立当且仅当

$$
F(x_1, \dots, x_n) = F_1(x_1) F_2(x_2) \cdots F_n(x_n), \quad \forall (x_1, \dots, x_n) \in \mathbb{R}^n,
$$
其中 $F_i$ 是 $X_i$ 的分布函数。下面两节分别把这一判定法则改写成分布列和密度的形式。

## 6.2. 离散型随机向量

### 6.2.1. 联合分布列与边缘分布列

**定义 6.2.1（离散型随机向量）** 如果 $X_1, \dots, X_n$ 都是离散型随机变量，则称 $\boldsymbol{X} = (X_1, \dots, X_n)$ 为**离散型随机向量**。如果 $\boldsymbol{X}$ 的所有不同取值是

$$
\boldsymbol{x}(j_1, \dots, j_n) = (x_1(j_1), \dots, x_n(j_n)), \quad j_1, \dots, j_n \ge 1,
$$
则称

$$
p_{j_1, \dots, j_n} = \mathbb{P}(\boldsymbol{X} = \boldsymbol{x}(j_1, \dots, j_n)), \quad j_1, \dots, j_n \ge 1
$$
为 $\boldsymbol{X}$ 的**联合分布列**。

联合分布列满足 $p_{j_1, \dots, j_n} \ge 0$ 与 $\sum_{j_1, \dots, j_n} p_{j_1, \dots, j_n} = 1$。二维情形 $p_{ij} = \mathbb{P}(X = x_i, Y = y_j)$ 规律性不强时，常用表格表示：

| $p_{ij}$ | $y_1$ | $y_2$ | $\cdots$ | $y_n$ | $\cdots$ | $p_i$ |
|---|---|---|---|---|---|---|
| $x_1$ | $p_{11}$ | $p_{12}$ | $\cdots$ | $p_{1n}$ | $\cdots$ | $p_1$ |
| $x_2$ | $p_{21}$ | $p_{22}$ | $\cdots$ | $p_{2n}$ | $\cdots$ | $p_2$ |
| $\vdots$ | $\vdots$ | $\vdots$ | | $\vdots$ | | $\vdots$ |
| $q_j$ | $q_1$ | $q_2$ | $\cdots$ | $q_n$ | $\cdots$ | $1$ |

其中 $p_i = \sum_j p_{ij}$ 是所在行之和，$q_j = \sum_i p_{ij}$ 是所在列之和。由可列可加性，$\{p_i\}$、$\{q_j\}$ 分别是 $X$、$Y$ 的分布列。例如同时抛掷红、黑两颗均匀的四面骰子，记 $X$、$Y$ 为红、黑骰子的点数，则表中 16 个 $p_{ij}$ 都等于 $1/16$，行和与列和都是 $1/4$。

**定义 6.2.2（边缘分布列）** 设离散型随机向量 $\boldsymbol{X}$ 的联合分布列为 $p_{j_1, \dots, j_n}$，$1 \le k < n$，称

$$
\mathbb{P}(X_1 = x_1(j_1), \dots, X_k = x_k(j_k)) = \sum_{j_{k+1}, \dots, j_n} p_{j_1, \dots, j_n}, \quad j_1, \dots, j_k \ge 1
$$
为 $(X_1, \dots, X_k)$ 的**边缘分布列**。其他分量组合的边缘分布列类似地对其余下标求和得到。

### 6.2.2. 独立性的判定

**定理 6.2.1** 设离散型随机向量 $\boldsymbol{X} = (X_1, \dots, X_n)$ 有联合分布列 $p_{j_1, \dots, j_n}$，则 $X_1, \dots, X_n$ 相互独立的充分必要条件是：对任意的 $(x_1(j_1), \dots, x_n(j_n))$，

$$
\mathbb{P}(X_1 = x_1(j_1), \dots, X_n = x_n(j_n)) = \prod_{i=1}^n \mathbb{P}(X_i = x_i(j_i)).
$$

**推论 6.2.1** 设离散型随机向量 $(X, Y)$ 的所有不同取值是 $(x_i, y_j)$，$i, j \ge 1$，则 $X, Y$ 相互独立的充分必要条件是：对任意的 $(x_i, y_j)$，

$$
\mathbb{P}(X = x_i, Y = y_j) = \mathbb{P}(X = x_i)\,\mathbb{P}(Y = y_j).
$$

**证明** 充分性：对任意 $x, y \in \mathbb{R}$，由概率的可列可加性，

$$
\begin{aligned}
\mathbb{P}(X \le x, Y \le y) &= \sum_{i: x_i \le x} \sum_{j: y_j \le y} \mathbb{P}(X = x_i, Y = y_j) = \sum_{i: x_i \le x} \sum_{j: y_j \le y} \mathbb{P}(X = x_i)\,\mathbb{P}(Y = y_j) \\
&= \Big(\sum_{i: x_i \le x} \mathbb{P}(X = x_i)\Big)\Big(\sum_{j: y_j \le y} \mathbb{P}(Y = y_j)\Big) = \mathbb{P}(X \le x)\,\mathbb{P}(Y \le y).
\end{aligned}
$$
必要性：单点集 $\{x_i\}$、$\{y_j\}$ 都是 Borel 集，由独立随机变量的性质（[3.1.3](/3.1.3)），事件 $\{X = x_i\}$ 与 $\{Y = y_j\}$ 独立，于是 $\mathbb{P}(X = x_i, Y = y_j) = \mathbb{P}(X = x_i)\,\mathbb{P}(Y = y_j)$。也可以不借助这一性质，直接由 $\mathbb{P}(X = x_i, Y = y_j) = \lim_{h \downarrow 0} \mathbb{P}(x_i - h < X \le x_i,\ y_j - h < Y \le y_j)$ 和例 6.1.1 的矩形公式把联合分布函数的乘积形式化为分布列的乘积形式。 $\square$

定理 6.2.1 的证明与此相同。

### 6.2.3. 多项分布

**定义 6.2.3（多项分布）** 设 $A_1, \dots, A_r$ 是试验 $S$ 的完备事件组，$p_i = \mathbb{P}(A_i)$，$\sum_{i=1}^r p_i = 1$。对 $S$ 进行 $n$ 次独立重复试验，用 $X_i$ 表示 $A_i$ 发生的次数，则（对 $r$ 用归纳法可得）

$$
\mathbb{P}(X_1 = k_1, \dots, X_r = k_r) = \frac{n!}{k_1! \cdots k_r!}\, p_1^{k_1} \cdots p_r^{k_r}, \quad k_i \ge 0,\ \sum_{i=1}^r k_i = n.
$$
称 $(X_1, \dots, X_r)$ 服从**多项分布**，记作 $(X_1, \dots, X_r) \sim \mathrm{Mult}(n, \boldsymbol{p})$，$\boldsymbol{p} = (p_1, \dots, p_r)^{\mathsf T}$。

$r = 2$ 时就是二项分布。系数 $\frac{n!}{k_1! \cdots k_r!}$ 是把 $n$ 次试验分成 $r$ 组、各组分别有 $k_1, \dots, k_r$ 次的方法数。

**性质 6.2.1** 设 $(X_1, \dots, X_r) \sim \mathrm{Mult}(n, \boldsymbol{p})$，$1 \le m < r$，$j_1, \dots, j_m$ 是互不相同的指标，则 $(X_{j_1}, \dots, X_{j_m})$ 的边缘分布为

$$
\mathbb{P}(X_{j_1} = k_1, \dots, X_{j_m} = k_m) = \frac{n!}{k_1! \cdots k_m!\, k!}\, p_{j_1}^{k_1} \cdots p_{j_m}^{k_m}\, q^{k},
$$
其中 $k = n - \sum_{i=1}^m k_i \ge 0$，$q = 1 - \sum_{i=1}^m p_{j_i}$。特别地，$X_j \sim \mathrm{Bin}(n, p_j)$。

这是因为把其余事件合并为一个事件"$A_{j_1}, \dots, A_{j_m}$ 都不发生"（概率为 $q$）后，$(X_{j_1}, \dots, X_{j_m}, n - \sum_i X_{j_i})$ 仍服从多项分布。多项分布的分量不独立：它们的和恒为 $n$。分量间的协方差见 [3.1.10](/3.1.10)。

## 6.3. 连续型随机向量

### 6.3.1. 联合密度与边缘密度

**定义 6.3.1（连续型随机向量）** 设 $\boldsymbol{X} = (X_1, \dots, X_n)$ 是随机向量。如果存在 $\mathbb{R}^n$ 上的非负可积函数 $f(\boldsymbol{x}) = f(x_1, \dots, x_n)$，使得对 $\mathbb{R}^n$ 的任何子立方体 $D = \{(x_1, \dots, x_n) \mid a_i < x_i \le b_i,\ 1 \le i \le n\}$，有

$$
\mathbb{P}(\boldsymbol{X} \in D) = \int_D f(x_1, \dots, x_n)\,\mathrm{d}x_1 \cdots \mathrm{d}x_n =: \int_D f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x},
$$
就称 $\boldsymbol{X}$ 是**连续型随机向量**，并称 $f$ 是 $\boldsymbol{X}$ 的**联合密度**（联合概率密度函数，简称概率密度）。

**定理 6.3.1** 设 $f$ 是 $\boldsymbol{X}$ 的联合密度，则对任意 $n$ 维 Borel 集 $B$，

$$
\mathbb{P}(\boldsymbol{X} \in B) = \int_B f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}.
$$
特别地 $\int_{\mathbb{R}^n} f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x} = \mathbb{P}(\boldsymbol{X} \in \mathbb{R}^n) = 1$。

联合密度不唯一：在一个零测集上改变 $f$ 的值，所有积分都不变。计算多重积分时常用下面的工具（会用即可，证明属于实分析）。

**定理 6.3.2（Fubini 定理）** 设 $D$ 是 $\mathbb{R}^n$ 中的区域，$\varphi$ 是 $D$ 上的非负函数或绝对可积函数（取绝对值后积分有限），则 $n$ 重积分 $\int_D \varphi(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}$ 可以化为累次积分计算，且积分次序可以交换。

设 $1 \le k < n$，$D_k$ 是 $\mathbb{R}^k$ 中的子立方体。由 Fubini 定理，

$$
\mathbb{P}((X_1, \dots, X_k) \in D_k) = \mathbb{P}(\boldsymbol{X} \in D_k \times \mathbb{R}^{n-k}) = \int_{D_k} \left( \int_{\mathbb{R}^{n-k}} f(x_1, \dots, x_n)\,\mathrm{d}x_{k+1} \cdots \mathrm{d}x_n \right) \mathrm{d}x_1 \cdots \mathrm{d}x_k.
$$
括号中的函数正是 $(X_1, \dots, X_k)$ 的联合密度，于是有下面的定义。

**定义 6.3.2（边缘密度）** 设 $f$ 是 $\boldsymbol{X}$ 的联合密度，$1 \le k < n$，称

$$
f_{1, \dots, k}(x_1, \dots, x_k) = \int_{\mathbb{R}^{n-k}} f(x_1, \dots, x_n)\,\mathrm{d}x_{k+1} \cdots \mathrm{d}x_n
$$
为 $(X_1, \dots, X_k)$ 的**边缘密度**（边际密度）。任意一组分量 $(X_{j_1}, \dots, X_{j_k})$ 的边缘密度同样由联合密度对其余 $n - k$ 个变元积分得到。

二维情形最常用：$(X, Y)$ 有联合密度 $f(x, y)$ 时，

$$
f_X(x) = \int_{-\infty}^{\infty} f(x, y)\,\mathrm{d}y, \qquad f_Y(y) = \int_{-\infty}^{\infty} f(x, y)\,\mathrm{d}x.
$$

**例 6.3.1** 设 $(X, Y)$ 在单位圆 $D = \{(x, y) \mid x^2 + y^2 \le 1\}$ 内均匀分布，求 $X$、$Y$ 的概率密度。

**解** $(X, Y)$ 的联合密度为 $f(x, y) = \frac{1}{\pi} \boldsymbol{1}_D(x, y)$。$X$ 只在 $[-1, 1]$ 中取值，对 $\lvert x \rvert \le 1$，

$$
f_X(x) = \frac{1}{\pi} \int_{-\infty}^{\infty} \boldsymbol{1}\{x^2 + y^2 \le 1\}\,\mathrm{d}y = \frac{1}{\pi} \int_{-\infty}^{\infty} \boldsymbol{1}\{\lvert y \rvert \le \sqrt{1 - x^2}\}\,\mathrm{d}y = \frac{2}{\pi}\sqrt{1 - x^2},
$$
$\lvert x \rvert > 1$ 时 $f_X(x) = 0$。同理 $f_Y(y) = \frac{2}{\pi}\sqrt{1 - y^2}$（$\lvert y \rvert \le 1$）。边缘分布不再是均匀分布。

### 6.3.2. 独立性的判定

**定理 6.3.3** 设对每个 $i$（$1 \le i \le n$），随机变量 $X_i$ 有概率密度 $f_i(x_i)$，则 $X_1, \dots, X_n$ 相互独立的充分必要条件是随机向量 $\boldsymbol{X} = (X_1, \dots, X_n)$ 有联合密度

$$
f(x_1, \dots, x_n) = f_1(x_1) f_2(x_2) \cdots f_n(x_n), \quad (x_1, \dots, x_n) \in \mathbb{R}^n.
$$

**证明** 充分性：对任意 $(x_1, \dots, x_n) \in \mathbb{R}^n$，由 Fubini 定理，

$$
\mathbb{P}(X_1 \le x_1, \dots, X_n \le x_n) = \int_{-\infty}^{x_1} \cdots \int_{-\infty}^{x_n} \prod_{i=1}^n f_i(t_i)\,\mathrm{d}t_1 \cdots \mathrm{d}t_n = \prod_{i=1}^n \int_{-\infty}^{x_i} f_i(t_i)\,\mathrm{d}t_i = \prod_{i=1}^n \mathbb{P}(X_i \le x_i),
$$
故 $X_1, \dots, X_n$ 相互独立。

必要性：设 $X_1, \dots, X_n$ 相互独立。对 $\mathbb{R}^n$ 的任何子立方体 $D = \{a_i < x_i \le b_i,\ 1 \le i \le n\}$，利用独立性和 Fubini 定理，

$$
\mathbb{P}(\boldsymbol{X} \in D) = \prod_{i=1}^n \mathbb{P}(a_i < X_i \le b_i) = \prod_{i=1}^n \int_{a_i}^{b_i} f_i(t_i)\,\mathrm{d}t_i = \int_D f_1(t_1) \cdots f_n(t_n)\,\mathrm{d}t_1 \cdots \mathrm{d}t_n,
$$
所以 $f_1(x_1) \cdots f_n(x_n)$ 是 $\boldsymbol{X}$ 的联合密度。 $\square$

实际判定时常用下面的拆分法，它省去了求边缘密度的积分。

**推论 6.3.1** 设 $(X, Y)$ 有联合密度 $f(x, y)$。如果存在非负函数 $g$、$h$，使得对一切 $(x, y) \in \mathbb{R}^2$ 都有 $f(x, y) = g(x) h(y)$，则 $X$ 与 $Y$ 独立，且 $f_X = g / \int g$，$f_Y = h / \int h$。

**证明** 由 $1 = \int\!\!\int f = \int g \cdot \int h$ 知 $c = \int g \in (0, \infty)$，$\int h = 1/c$。于是 $f_X(x) = \int f(x, y)\,\mathrm{d}y = g(x)/c$，$f_Y(y) = c\,h(y)$，且 $f(x, y) = f_X(x) f_Y(y)$，由定理 6.3.3 得独立。 $\square$

**注 6.3.1** 使用拆分法时必须把密度连同取值范围（示性函数）完整写出。例 6.3.1 中单位圆内均匀分布的密度在圆内是常数 $\frac{1}{\pi}$，看似可以拆分，但完整的密度是 $\frac{1}{\pi}\boldsymbol{1}\{x^2 + y^2 \le 1\}$，示性函数不能写成 $x$ 的函数与 $y$ 的函数之积，所以 $X, Y$ 不独立；事实上 $f_X(x) f_Y(y) \ne f(x, y)$。反之，若 $f(x, y) = \lambda\mu\,\mathrm{e}^{-\lambda x - \mu y} \boldsymbol{1}\{x > 0\} \boldsymbol{1}\{y > 0\}$，取值范围是乘积集合，可以拆分，$X \sim \mathrm{Exp}(\lambda)$ 与 $Y \sim \mathrm{Exp}(\mu)$ 独立。

**例 6.3.2（Buffon 投针问题）** 平面上画满间距为 $a$ 的平行线，向平面任意投一根长度为 $L$（$L < a$）的针，求针与平行线相交的概率。

**解** 设 $X$ 为针的中点到最近一条平行线的距离，$\Theta$ 为针与平行线的夹角。"任意投针"理解为 $X \sim \mathrm{U}(0, a/2)$ 与 $\Theta \sim \mathrm{U}(0, \pi/2)$ 独立，联合密度为 $\frac{4}{\pi a}$（在 $(0, a/2) \times (0, \pi/2)$ 上）。针与平行线相交当且仅当 $X \le \frac{L}{2}\sin\Theta$，故

$$
\mathbb{P}\Big(X \le \frac{L}{2}\sin\Theta\Big) = \frac{4}{\pi a} \int_0^{\pi/2} \int_0^{\frac{L}{2}\sin\theta} \mathrm{d}x\,\mathrm{d}\theta = \frac{4}{\pi a} \cdot \frac{L}{2} \int_0^{\pi/2} \sin\theta\,\mathrm{d}\theta = \frac{2L}{\pi a}.
$$
（若 $\Theta$ 取为针与平行线垂线的夹角，则把 $\sin$ 换成 $\cos$，结果相同。）这给出了用随机试验估计 $\pi$ 的经典方法。

### 6.3.3. 联合分布函数与联合密度

已知联合密度 $f(x, y)$ 时，联合分布函数为

$$
F(x, y) = \int_{-\infty}^{x} \int_{-\infty}^{y} f(u, v)\,\mathrm{d}v\,\mathrm{d}u.
$$
反过来，在 $f$ 的连续点处 $f(x, y) = \dfrac{\partial^2 F(x, y)}{\partial x \partial y}$。

**例 6.3.3** 如果在 $(x, y)$ 的邻域内 $\dfrac{\partial F}{\partial x}$、$\dfrac{\partial F}{\partial y}$、$\dfrac{\partial^2 F}{\partial x \partial y}$、$\dfrac{\partial^2 F}{\partial y \partial x}$ 连续，则由例 6.1.1 的矩形公式与微分中值定理，

$$
\lim_{\substack{\Delta x \downarrow 0 \\ \Delta y \downarrow 0}} \frac{\mathbb{P}(x - \Delta x < X \le x,\ y - \Delta y < Y \le y)}{\Delta x\,\Delta y} = \frac{\partial^2 F(x, y)}{\partial x \partial y} = \frac{\partial^2 F(x, y)}{\partial y \partial x}.
$$
这说明联合密度可以理解为"落在点 $(x, y)$ 附近小矩形内的概率除以矩形面积"，这种微元的观点在推导公式时很有用。更一般地有下面的判别法（了解即可）。

**定理 6.3.4** 设 $(X, Y)$ 有连续的联合分布函数 $F(x, y)$。令 $f(x, y) = \dfrac{\partial^2 F(x, y)}{\partial x \partial y}$（当该混合偏导数存在时），其余点处 $f(x, y) = 0$。如果 $\int_{\mathbb{R}^2} f(x, y)\,\mathrm{d}x\,\mathrm{d}y = 1$，则 $f$ 是 $(X, Y)$ 的联合密度。

定理中的条件"积分为 1"不能省略，下面两例说明这一点。

**例 6.3.4** 如果 $X$、$Y$ 的分布函数都连续，则它们的联合分布函数 $F(x, y)$ 连续。

**证明** 对任意 $(x_0, y_0)$ 和 $\varepsilon > 0$，存在 $\delta > 0$，使得 $\lvert x - x_0 \rvert < \delta$、$\lvert y - y_0 \rvert < \delta$ 时 $\lvert F_X(x) - F_X(x_0) \rvert < \varepsilon/2$，$\lvert F_Y(y) - F_Y(y_0) \rvert < \varepsilon/2$。于是对这样的 $(x, y)$，

$$
\begin{aligned}
\lvert F(x, y) - F(x_0, y_0) \rvert &\le \lvert F(x, y) - F(x_0, y) \rvert + \lvert F(x_0, y) - F(x_0, y_0) \rvert \\
&\le \mathbb{P}(x \wedge x_0 < X \le x \vee x_0) + \mathbb{P}(y \wedge y_0 < Y \le y \vee y_0) \\
&= \lvert F_X(x) - F_X(x_0) \rvert + \lvert F_Y(y) - F_Y(y_0) \rvert < \varepsilon. \qquad \square
\end{aligned}
$$

**例 6.3.5** 存在随机向量 $(X, Y)$，它有连续的联合分布函数，但不是连续型随机向量。设 $X \sim \mathrm{U}(0, 1)$，$Y = X$，则

$$
F(x, y) = \mathbb{P}(X \le \min\{x, y\}) = \begin{cases} 0, & \min\{x, y\} \le 0, \\ \min\{x, y\}, & 0 < \min\{x, y\} \le 1, \\ 1, & \min\{x, y\} > 1 \end{cases}
$$
连续。如果 $(X, Y)$ 有联合密度 $f$，记直线 $y = x$ 为 $D$，则 $1 = \mathbb{P}(X = Y) = \mathbb{P}((X, Y) \in D) = \int_D f(x, y)\,\mathrm{d}x\,\mathrm{d}y = 0$（直线的面积为零），矛盾。这里 $F$ 除去有限条直线外混合偏导数存在且连续（都等于 0），但积分为 0 而不是 1。

由此也回答了一个自然的问题：两个连续型随机变量 $X_1, X_2$ 组成的随机向量不一定是连续型随机向量；即使 $(X_1, X_2)$ 有联合密度，也不能只由两个边缘密度求出它（注 6.1.1），除非已知两者独立。

## 6.4. 二元正态分布

先看一个特例。设 $(X, Y)$ 有联合密度

$$
f(x, y) = \frac{1}{2\pi} \exp\left( -\frac{x^2 + y^2}{2} \right) = \frac{1}{\sqrt{2\pi}} \mathrm{e}^{-x^2/2} \cdot \frac{1}{\sqrt{2\pi}} \mathrm{e}^{-y^2/2}.
$$
由推论 6.3.1，$X \sim \mathcal{N}(0, 1)$ 与 $Y \sim \mathcal{N}(0, 1)$ 独立。一般的二元正态分布还要允许两个分量有不同的均值、方差，并且相互关联，这需要五个参数。

**定义 6.4.1（二元正态分布）** 设 $\mu_1, \mu_2$ 是常数，$\sigma_1, \sigma_2$ 是正常数，$\rho \in (-1, 1)$。如果随机向量 $(X, Y)$ 有联合密度

$$
f(x, y) = \frac{1}{2\pi\sigma_1\sigma_2\sqrt{1 - \rho^2}} \exp\left\{ -\frac{1}{2(1 - \rho^2)} \left[ \frac{(x - \mu_1)^2}{\sigma_1^2} - \frac{2\rho(x - \mu_1)(y - \mu_2)}{\sigma_1\sigma_2} + \frac{(y - \mu_2)^2}{\sigma_2^2} \right] \right\},
$$
则称 $(X, Y)$ 服从**二元正态分布**，记作 $(X, Y) \sim \mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$。

记 $\boldsymbol{x} = (x, y)^{\mathsf T}$，$\boldsymbol{\mu} = (\mu_1, \mu_2)^{\mathsf T}$，

$$
\Sigma = \begin{pmatrix} \sigma_1^2 & \rho\sigma_1\sigma_2 \\ \rho\sigma_1\sigma_2 & \sigma_2^2 \end{pmatrix}, \qquad \lvert \Sigma \rvert = \det\Sigma = \sigma_1^2\sigma_2^2(1 - \rho^2) > 0,
$$
则密度可以简写为与一元正态密度 $\frac{1}{\sqrt{2\pi\sigma^2}}\exp\{-\frac{(x - \mu)^2}{2\sigma^2}\}$ 完全类似的形式

$$
f(\boldsymbol{x}) = \frac{1}{2\pi\lvert\Sigma\rvert^{1/2}} \exp\left\{ -\frac{1}{2}(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu}) \right\}.
$$
密度的等高线 $(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu}) = c^2$ 是以 $\boldsymbol{\mu}$ 为中心的椭圆；$\rho = 0$ 且 $\sigma_1 = \sigma_2$ 时是圆，$\rho > 0$ 时椭圆的长轴沿 $y = x$ 方向倾斜。后面会看到 $\mu_1, \mu_2$ 是两个分量的期望，$\sigma_1^2, \sigma_2^2$ 是方差，$\rho$ 是相关系数（[3.1.10](/3.1.10)），$\Sigma$ 是协方差矩阵；一般维数的情形见 [3.1.15](/3.1.15)。

![二元正态分布的密度曲面与等高线：左列 rho = 0，右列 rho = 0.75（sigma1 = sigma2 = 1）](./plots/bivariate-normal.py)

**性质 6.4.1** 设 $(X, Y) \sim \mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$，则 $X \sim \mathcal{N}(\mu_1, \sigma_1^2)$，$Y \sim \mathcal{N}(\mu_2, \sigma_2^2)$。

**证明** 令 $u = \frac{x - \mu_1}{\sigma_1}$，$v = \frac{y - \mu_2}{\sigma_2}$。方括号内的二次型为 $u^2 - 2\rho uv + v^2 = (v - \rho u)^2 + (1 - \rho^2)u^2$，于是

$$
f_X(x) = \int_{-\infty}^{\infty} f(x, y)\,\mathrm{d}y = \frac{\mathrm{e}^{-u^2/2}}{\sqrt{2\pi}\,\sigma_1} \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi(1 - \rho^2)}} \exp\left\{ -\frac{(v - \rho u)^2}{2(1 - \rho^2)} \right\} \mathrm{d}v = \frac{1}{\sqrt{2\pi}\,\sigma_1} \exp\left\{ -\frac{(x - \mu_1)^2}{2\sigma_1^2} \right\},
$$
其中用到被积函数是 $\mathcal{N}(\rho u, 1 - \rho^2)$ 的密度、积分为 1。$Y$ 的情形对称。 $\square$

所以边缘分布与参数 $\rho$ 无关：不同的 $\rho$ 给出边缘分布相同、联合分布不同的随机向量，这是注 6.1.1 的又一个例子。

**定理 6.4.1** 设 $(X, Y) \sim \mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$，则 $X, Y$ 独立的充分必要条件是 $\rho = 0$。

**证明** 由性质 6.4.1，$X, Y$ 独立当且仅当 $f(x, y) = f_X(x) f_Y(y)$ 对一切 $(x, y)$ 成立（两边都连续，几乎处处相等即处处相等）。$\rho = 0$ 时 $f$ 的指数部分分离为 $-\frac{(x - \mu_1)^2}{2\sigma_1^2} - \frac{(y - \mu_2)^2}{2\sigma_2^2}$，等式成立，故 $X, Y$ 独立。反之，若 $X, Y$ 独立，在 $(x, y) = (\mu_1, \mu_2)$ 处比较两边得

$$
\frac{1}{2\pi\sigma_1\sigma_2\sqrt{1 - \rho^2}} = \frac{1}{2\pi\sigma_1\sigma_2},
$$
即 $\sqrt{1 - \rho^2} = 1$，$\rho = 0$。 $\square$

## 6.5. 条件分布

联合分布描述"全面"的信息。很多问题关心的是：已知某个分量的取值后，另一个分量的分布如何变化。例如已知身高 $Y = y$，体重 $X$ 的分布是怎样的。这就是条件分布。

### 6.5.1. 离散型条件分布

**定义 6.5.1（条件分布列）** 设 $(X, Y)$ 是离散型随机向量，联合分布列为 $p_{ij} = \mathbb{P}(X = x_i, Y = y_j)$，$X, Y$ 的边缘分布列分别为 $p_i = \mathbb{P}(X = x_i)$、$q_j = \mathbb{P}(Y = y_j)$。对每个满足 $q_j > 0$ 的 $j$，称

$$
\mathbb{P}(X = x_i \mid Y = y_j) = \frac{\mathbb{P}(X = x_i, Y = y_j)}{\mathbb{P}(Y = y_j)} = \frac{p_{ij}}{q_j}, \quad i = 1, 2, \dots
$$
为给定条件 $Y = y_j$ 下 $X$ 的**条件分布列**。

对固定的 $j$，$\{p_{ij}/q_j\}_i$ 非负且和为 1，确实是一个分布列：它就是联合分布列表中第 $j$ 列除以列和。例如两颗四面骰子的例子中，$\mathbb{P}(X = 3 \mid Y = 2) = \frac{1/16}{1/4} = \frac{1}{4} = \mathbb{P}(X = 3)$。由条件概率的乘法公式，$p_{ij} = q_j\,\mathbb{P}(X = x_i \mid Y = y_j)$：边缘分布与条件分布合起来决定联合分布。

**定理 6.5.1** 离散型随机变量 $X, Y$ 独立的充分必要条件是：对任何满足 $q_j > 0$ 的 $i, j$，

$$
\mathbb{P}(X = x_i \mid Y = y_j) = \mathbb{P}(X = x_i).
$$

这与推论 6.2.1 中 $p_{ij} = p_i q_j$ 等价：独立就是"知道 $Y$ 的值不改变 $X$ 的分布"。

**例 6.5.1** 甲向一个目标独立重复射击，每次击中的概率为 $p = 1 - q$。用 $S_n$ 表示第 $n$ 次击中目标时的射击次数，求 $(X, Y) = (S_1, S_2)$ 的条件分布。

**解** 事件 $\{S_1 = i, S_2 = j\}$ 表示前 $j$ 次中恰在第 $i$、第 $j$ 次击中，故联合分布为

$$
\mathbb{P}(X = i, Y = j) = p^2 q^{j-2}, \quad j > i \ge 1.
$$
边缘分布为

$$
\mathbb{P}(X = i) = \sum_{j=i+1}^{\infty} p^2 q^{j-2} = p q^{i-1}, \qquad \mathbb{P}(Y = j) = \sum_{i=1}^{j-1} p^2 q^{j-2} = (j - 1)p^2 q^{j-2}, \quad j \ge 2.
$$
于是对确定的 $i$，

$$
\mathbb{P}(Y = j \mid X = i) = \frac{p^2 q^{j-2}}{p q^{i-1}} = p q^{j-i-1}, \quad j > i,
$$
即已知第一次击中在第 $i$ 次，再等待的次数 $Y - i$ 仍服从 $\mathrm{Geo}(p)$；对确定的 $j \ge 2$，

$$
\mathbb{P}(X = i \mid Y = j) = \frac{p^2 q^{j-2}}{(j - 1)p^2 q^{j-2}} = \frac{1}{j - 1}, \quad 1 \le i < j,
$$
即已知 $S_2 = j$ 时，$S_1$ 在 $\{1, 2, \dots, j - 1\}$ 中等可能取值。此外，令 $X_1 = S_1$，$X_2 = S_2 - S_1$，则

$$
\mathbb{P}(X_1 = i, X_2 = j) = \mathbb{P}(S_1 = i, S_2 = i + j) = p^2 q^{i+j-2} = p q^{i-1} \cdot p q^{j-1},
$$
由推论 6.2.1，$X_1, X_2$ 独立同分布，都服从 $\mathrm{Geo}(p)$。

### 6.5.2. 连续型条件分布

对连续型随机向量，$\mathbb{P}(Y = y) = 0$，不能直接用条件概率的定义。自然的做法是先以 $\{y - \varepsilon < Y \le y\}$ 为条件，再令 $\varepsilon \to 0$。设 $(X, Y)$ 有联合密度 $f(x, y)$，边缘密度 $f_Y(y) = \int f(x, y)\,\mathrm{d}x$ 在 $y$ 处连续且 $f_Y(y) > 0$，$\partial F(x, y)/\partial y$ 存在，则

$$
\lim_{\varepsilon \to 0} \mathbb{P}(X \le x \mid y - \varepsilon < Y \le y) = \lim_{\varepsilon \to 0} \frac{[F(x, y) - F(x, y - \varepsilon)]/\varepsilon}{[F_Y(y) - F_Y(y - \varepsilon)]/\varepsilon} = \frac{\frac{\partial}{\partial y}\int_{-\infty}^{x}\int_{-\infty}^{y} f(s, t)\,\mathrm{d}t\,\mathrm{d}s}{f_Y(y)} = \frac{\int_{-\infty}^{x} f(s, y)\,\mathrm{d}s}{f_Y(y)}.
$$
这启发了下面的定义。

**定义 6.5.2（条件分布函数）** 设随机向量 $(X, Y)$ 有联合密度 $f(x, y)$，$Y$ 有边缘密度 $f_Y(y)$。若在确定的 $y$ 处 $f_Y(y) > 0$，则称

$$
F_{X|Y}(x \mid y) = \mathbb{P}(X \le x \mid Y = y) = \frac{\int_{-\infty}^{x} f(s, y)\,\mathrm{d}s}{f_Y(y)}, \quad x \in \mathbb{R}
$$
为给定条件 $Y = y$ 下 $X$ 的**条件分布函数**，简称条件分布；称

$$
f_{X|Y}(x \mid y) = \frac{f(x, y)}{f_Y(y)} = \frac{f(x, y)}{\int_{-\infty}^{\infty} f(x, y)\,\mathrm{d}x}, \quad x \in \mathbb{R}
$$
为给定条件 $Y = y$ 下 $X$ 的**条件密度**（条件概率密度）。

几何上，条件密度就是把联合密度曲面沿 $Y = y$ 切下的截线 $x \mapsto f(x, y)$ 除以它下方的面积 $f_Y(y)$，重新归一化为一个密度。条件密度与条件分布函数的关系同一元情形：对使 $f_Y(y) > 0$ 的 $y$，

1. $F_{X|Y}(x \mid y) = \int_{-\infty}^{x} f_{X|Y}(s \mid y)\,\mathrm{d}s$；
2. 如果 $F_{X|Y}(x \mid y)$ 关于 $x$ 连续，且除去至多可列个点外有连续的导数，则 $\frac{\partial}{\partial x} F_{X|Y}(x \mid y)$（导数存在处，其余点取 0）是条件密度。

由定义立即得到连续型的乘法公式

$$
f(x, y) = f_Y(y)\,f_{X|Y}(x \mid y),
$$
它是由边缘与条件构造联合密度的基本工具。

**定理 6.5.2** 设 $(X, Y)$ 有联合密度，则 $X, Y$ 独立的充分必要条件是：对 $\{y \mid f_Y(y) > 0\}$ 中的 $y$，

$$
f_{X|Y}(x \mid y) = f_X(x), \quad x \in \mathbb{R},
$$
即 $f(x, y) = f_X(x) f_Y(y)$（定理 6.3.3）。

![二元正态分布（rho = 0.75）的条件密度：在不同的 y 处截取联合密度并归一化，条件均值随 y 线性移动](./plots/conditional-slices.py)

**例 6.5.2** 设 $(X, Y) \sim \mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$，求已知 $X = x$ 时 $Y$ 的条件密度。

**解** 由性质 6.4.1，$X \sim \mathcal{N}(\mu_1, \sigma_1^2)$。沿用性质 6.4.1 证明中的记号 $u = \frac{x - \mu_1}{\sigma_1}$、$v = \frac{y - \mu_2}{\sigma_2}$，

$$
f_{Y|X}(y \mid x) = \frac{f(x, y)}{f_X(x)} = \frac{1}{\sigma_2\sqrt{2\pi(1 - \rho^2)}} \exp\left\{ -\frac{(v - \rho u)^2}{2(1 - \rho^2)} \right\} = \frac{1}{\sigma_2\sqrt{2\pi(1 - \rho^2)}} \exp\left\{ -\frac{(y - \mu_{x})^2}{2(1 - \rho^2)\sigma_2^2} \right\},
$$
其中 $\mu_{x} = \mu_2 + \rho\frac{\sigma_2}{\sigma_1}(x - \mu_1)$。这说明

$$
Y \mid X = x \ \sim\ \mathcal{N}\Big( \mu_2 + \rho\frac{\sigma_2}{\sigma_1}(x - \mu_1),\ (1 - \rho^2)\sigma_2^2 \Big),
$$
同理 $X \mid Y = y \sim \mathcal{N}\big( \mu_1 + \rho\frac{\sigma_1}{\sigma_2}(y - \mu_2),\ (1 - \rho^2)\sigma_1^2 \big)$。条件分布仍是正态分布，条件均值是条件取值的线性函数，条件方差 $(1 - \rho^2)\sigma_2^2$ 不依赖于 $x$，且不超过无条件方差 $\sigma_2^2$：知道 $X$ 的值减少了 $Y$ 的不确定性，$\lvert\rho\rvert$ 越大减少得越多。$\rho = 0$ 时 $f_{Y|X}(y \mid x) = f_Y(y)$，与定理 6.4.1 一致。

**例 6.5.3** 设计算机使用环境的指标 $Y \sim \Gamma(\alpha, \lambda)$，概率密度为

$$
f_Y(y) = \frac{\lambda^{\alpha}}{\Gamma(\alpha)} y^{\alpha-1} \mathrm{e}^{-\lambda y}, \quad y > 0.
$$
已知 $Y = y$ 时，软件的使用寿命 $X \mid Y = y \sim \mathrm{Exp}(y)$。求 $X$ 的分布。

**解** $X$ 的条件密度为 $f_{X|Y}(x \mid y) = y\mathrm{e}^{-xy}$（$x > 0$）。由乘法公式，$(X, Y)$ 的联合密度为

$$
f(x, y) = f_{X|Y}(x \mid y) f_Y(y) = \frac{\lambda^{\alpha}}{\Gamma(\alpha)} y^{\alpha} \mathrm{e}^{-y(x + \lambda)}, \quad x, y > 0.
$$
对 $x > 0$，令 $t = y(x + \lambda)$，并利用 $\Gamma(\alpha + 1) = \alpha\Gamma(\alpha)$，

$$
f_X(x) = \int_0^{\infty} f(x, y)\,\mathrm{d}y = \frac{\lambda^{\alpha}}{\Gamma(\alpha)} \cdot \frac{1}{(x + \lambda)^{\alpha+1}} \int_0^{\infty} t^{\alpha} \mathrm{e}^{-t}\,\mathrm{d}t = \frac{\alpha\lambda^{\alpha}}{(x + \lambda)^{\alpha+1}}, \quad x > 0.
$$
这个分布的尾部 $\mathbb{P}(X > x) = \big(\frac{\lambda}{x + \lambda}\big)^{\alpha}$ 按幂律衰减，比任何指数分布都重：环境指标的随机性使寿命的分布出现重尾。

### 6.5.3. 随机向量的条件分布

上述定义可以直接推广到随机向量（了解即可）。设 $\boldsymbol{X} = (X_1, \dots, X_n)$、$\boldsymbol{Y} = (Y_1, \dots, Y_m)$，$(\boldsymbol{X}, \boldsymbol{Y})$ 有联合密度 $f(\boldsymbol{x}, \boldsymbol{y})$，$\boldsymbol{Y}$ 的边缘密度为 $f_{\boldsymbol{Y}}(\boldsymbol{y}) = \int_{\mathbb{R}^n} f(\boldsymbol{x}, \boldsymbol{y})\,\mathrm{d}\boldsymbol{x}$。若在确定的 $\boldsymbol{y}$ 处 $f_{\boldsymbol{Y}}(\boldsymbol{y}) > 0$，则给定 $\boldsymbol{Y} = \boldsymbol{y}$ 时 $\boldsymbol{X}$ 的条件分布函数与条件密度分别为

$$
F_{\boldsymbol{X}|\boldsymbol{Y}}(\boldsymbol{x} \mid \boldsymbol{y}) = \frac{\int_{\boldsymbol{s} \le \boldsymbol{x}} f(\boldsymbol{s}, \boldsymbol{y})\,\mathrm{d}\boldsymbol{s}}{f_{\boldsymbol{Y}}(\boldsymbol{y})}, \qquad f_{\boldsymbol{X}|\boldsymbol{Y}}(\boldsymbol{x} \mid \boldsymbol{y}) = \frac{f(\boldsymbol{x}, \boldsymbol{y})}{f_{\boldsymbol{Y}}(\boldsymbol{y})}.
$$

条件分布的乘法公式、全概率公式与贝叶斯公式在 [3.1.9](/3.1.9) 中与事件的情形一起汇总。

## 小结

| 对象 | 离散型 | 连续型 |
|---|---|---|
| 联合分布 | 联合分布列 $p_{ij} = \mathbb{P}(X = x_i, Y = y_j)$ | 联合密度 $f(x, y)$，$\mathbb{P}((X, Y) \in B) = \int_B f$ |
| 边缘分布 | 对其余下标求和：$p_i = \sum_j p_{ij}$ | 对其余变元积分：$f_X(x) = \int f(x, y)\,\mathrm{d}y$ |
| 条件分布 | $\mathbb{P}(X = x_i \mid Y = y_j) = p_{ij}/q_j$ | $f_{X\mid Y}(x \mid y) = f(x, y)/f_Y(y)$ |
| 独立性 | $p_{ij} = p_i q_j$ 对一切 $i, j$ | $f(x, y) = f_X(x) f_Y(y)$；拆分时连同取值范围 |
| 典型例子 | 多项分布 $\mathrm{Mult}(n, \boldsymbol{p})$ | 二元正态分布 $\mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$ |

- 联合分布函数 $F(x, y)$ 对一切随机向量适用：边缘分布函数是 $F(x, +\infty)$，不需要积分；矩形概率是 $F(b, d) - F(b, c) - F(a, d) + F(a, c)$。
- 联合分布决定边缘分布，反之不然；独立时边缘分布决定联合分布。
- 条件分布 + 边缘分布 = 联合分布（乘法公式），由此可以求另一个分量的边缘分布（例 6.5.3）。
- 二元正态分布的边缘分布与条件分布都是正态分布；分量独立当且仅当 $\rho = 0$。
