---
title: 次序统计量、秩与经验分布函数
description: 次序统计量及其分布，均匀次序统计量与概率积分变换；秩与反秩、秩向量的均匀分布与秩的矩；无分布统计量与秩统计量；U 统计量及其核；经验分布函数、Kolmogorov 距离、它的无分布性与 DKW 不等式；分布函数的逐点置信区间与置信带；经验分位数函数与带置信带的 Q–Q 图。
source_hash: 18db6f2012b5
---

[3.6.1](/3.6.1) 的置换检验通过重排观测数据得到零分布，所以参照分布必须对每个数据集重新计算。本章引入把这一想法变成现成的、有表可查的方法的对象。若舍弃观测的数值而只保留它们的次序，即秩，则结果在每个连续总体下分布都相同：秩统计量是无分布的，它的零分布可以一次算好、永远适用。在另一个极端，我们保留全部数值，但通过经验分布函数来看它们，经验分布函数估计整个总体分布；它与假设的分布函数之间的距离同样是无分布的，而 Dvoretzky–Kiefer–Wolfowitz 不等式把它变成对每个总体、每个样本量都成立的置信带。二者之间是次序统计量，它联系着秩与数值；以及 U 统计量，它为后面各章的许多估计量与检验统计量提供共同的框架。

其中几个对象已经出现过：概率论中的次序统计量与分位数（[3.1.7](/3.1.7)），[3.2.1](/3.2.1) 中的**经验分布函数**与 **Glivenko–Cantelli 定理**，以及 [3.2.6](/3.2.6) 中的 Kolmogorov–Smirnov 检验。这里汇集非参数推断需要的内容，并展开其中新的部分：秩及其分布（§2.2–2.3）、U 统计量（§2.4）、Kolmogorov 距离的无分布性与 DKW 不等式（§2.6）、置信带（§2.7）以及带置信带的 Q–Q 图（§2.8）。Kolmogorov–Smirnov 检验背后经验过程的极限理论见 [3.6.6](/3.6.6)。

## 2.1. 次序统计量

### 2.1.1. 定义

我们通常不关心样本观测 $X_1, \dots, X_n$ 到达的先后顺序。然而许多问题涉及的是排好序的值：一次考试的最高分超过 $98$ 的概率、一组心率样本的第 $80$ 百分位数、一组测量值的极差。

**定义 2.1.1（次序统计量）** 设 $X_1, \dots, X_n$ 是来自分布函数 $F$ 连续的总体的独立观测。连续性蕴含对 $i \ne j$ 有 $\mathbb{P}(X_i = X_j) = 0$，所以以概率 1 可以把观测按严格不等式排序，

$$
X_{(1)} < X_{(2)} < \cdots < X_{(n)},
$$
称 $X_{(i)}$ 为第 $i$ 个**次序统计量**。

特别令人感兴趣的次序统计量是最小值 $X_{(1)}$、最大值 $X_{(n)}$ 与**样本中位数**

$$
\tilde X = \begin{cases} X_{((n+1)/2)}, & n \text{ 为奇数},\\[2pt] \tfrac12\bigl(X_{(n/2)} + X_{(n/2+1)}\bigr), & n \text{ 为偶数},\end{cases}
$$
以及由它们构成的离散程度度量：极差 $X_{(n)} - X_{(1)}$、**四分位距**（样本上、下四分位数之差）和半四分位距（其一半）。在 R 中，若 `x` 含缺失值，则 `median(x)` 返回 `NA`，而 `median(x, na.rm = TRUE)` 计算其余值的中位数；对 `x <- c(2, 3, 5, NA, 4, NA, 6)`，后者给出 $4$。

### 2.1.2. 分布

次序统计量的分布已在 [3.1.7](/3.1.7) 中导出，这里为方便起见重述。

**定理 2.1.1** 设 $X_1, \dots, X_n$ i.i.d.，分布函数为 $F$，密度为 $f$。

1. $X_{(i)}$ 的分布函数是 $n$ 个观测中至少有 $i$ 个不超过 $x$ 的概率：
   $$
   F_{(i)}(x) = \mathbb{P}(X_{(i)} \le x) = \sum_{k=i}^n \binom nk F(x)^k\bigl(1 - F(x)\bigr)^{n-k};
   $$
   特别地，$F_{(1)}(x) = 1 - \bigl(1 - F(x)\bigr)^n$，$F_{(n)}(x) = F(x)^n$。
2. $X_{(i)}$ 的密度为
   $$
   f_{(i)}(x) = \frac{n!}{(i-1)!\,(n-i)!}F(x)^{i-1}\bigl(1 - F(x)\bigr)^{n-i}f(x).
   $$
3. 对 $j < k$，$(X_{(j)}, X_{(k)})$ 的联合密度在 $x < y$ 时为
   $$
   f_{(j,k)}(x, y) = \frac{n!}{(j-1)!\,(k-j-1)!\,(n-k)!}F(x)^{j-1}\bigl(F(y) - F(x)\bigr)^{k-j-1}\bigl(1 - F(y)\bigr)^{n-k}f(x)f(y);
   $$
   特别地，$f_{(1,n)}(x, y) = n(n-1)\bigl(F(y) - F(x)\bigr)^{n-2}f(x)f(y)$。
4. 全部次序统计量的联合密度在 $x_1 < \cdots < x_n$ 时为 $n!\,f(x_1)\cdots f(x_n)$。

**证明** 第 1 部分：$\{X_{(i)} \le x\}$ 是至少有 $i$ 个观测不超过 $x$ 的事件，而这样的观测个数服从 $\mathrm{Bin}(n, F(x))$。第 2 部分由求导得到（和式逐项抵消），或直观地：要使 $X_{(i)}$ 落在 $[x, x + \mathrm{d}x]$ 中，必须有一个观测落在那里，$i - 1$ 个在 $x$ 之下，$n - i$ 个在 $x$ 之上，多项系数数出选取它们的方式数。第 3、4 部分由同样的多项论证（分别分成三组和 $n$ 组）得到。$\square$

均匀情形是本章其余部分的关键。

**推论 2.1.1** 若 $U_1, \dots, U_n \overset{\text{iid}}{\sim} \mathrm{U}(0, 1)$，则 $U_{(i)} \sim \mathrm{Beta}(i, n - i + 1)$，且 $\mathbb{E}U_{(i)} = \frac{i}{n+1}$。若 $F$ 连续且 $X_1, \dots, X_n \overset{\text{iid}}{\sim} F$，则无论 $F$ 是什么，$\bigl(F(X_{(1)}), \dots, F(X_{(n)})\bigr)$ 都与 $(U_{(1)}, \dots, U_{(n)})$ 同分布。

**证明** 在 $(0, 1)$ 上取 $F(x) = x$、$f = 1$，则定理 2.1.1 的第 2 部分就是 $\mathrm{Beta}(i, n - i + 1)$ 的密度（[3.1.7](/3.1.7)，那里画出了这些密度）。对连续的 $F$，**概率积分变换**给出 $F(X_i) \overset{\text{iid}}{\sim} \mathrm{U}(0, 1)$，又因 $F$ 不减，$F(X_i)$ 的次序与 $X_i$ 的次序相同（$F(X_i)$ 之间出现结的概率为零）。$\square$

第二个陈述说的是，在概率尺度上，每个连续总体的次序统计量表现相同。例如，对每个连续的 $F$ 有 $\mathbb{P}\bigl(F(X_{(n)}) > 1 - \varepsilon\bigr) = 1 - (1 - \varepsilon)^n$。

**例 2.1.1** 从 $\mathrm{U}(0, 1)$ 中取 $12$ 个观测的样本。只有十二个值全都不超过 $0.95$，最大值才不会超过 $0.95$，所以 $\mathbb{P}(X_{(12)} > 0.95) = 1 - 0.95^{12} = 0.460$。由推论 2.1.1，这个数也是来自任意连续总体的 $12$ 个观测中最大者超过该总体 $95\%$ 分位数的概率。

## 2.2. 秩

### 2.2.1. 秩与反秩

**定义 2.2.1（秩）** 设 $X_1, \dots, X_n$ 是来自连续分布的样本，其次序统计量为 $X_{(1)} < \cdots < X_{(n)}$。若 $X_i = X_{(R_i)}$，则称观测 $X_i$ 在 $X_1, \dots, X_n$ 中的**秩**为 $R_i$；无结时它是良定义的，而这以概率 1 成立。等价地，

$$
R_i = 1 + \sum_{j \ne i}\boldsymbol{1}\{X_j < X_i\},
$$
即 $1$ 加上小于 $X_i$ 的观测个数。向量 $\boldsymbol{R} = (R_1, \dots, R_n)$ 是秩向量；$R_i$ 也称为第 $i$ 个秩次序统计量。由 $X_{(i)} = X_{D_i}$ 定义的逆置换 $\boldsymbol{D} = (D_1, \dots, D_n)$ 给出排好序的观测的下标（反秩）。

函数形式常用 $I_+(t) = \boldsymbol{1}\{t > 0\}$ 写成 $R_i = 1 + \sum_{j\ne i}I_+(X_i - X_j)$；计算秩统计量的期望时用的就是这种形式。在 R 中，`rank(x)` 返回秩，`order(x)` 返回反秩：

```r
set.seed(1)
x <- sample(1:30, 5)
x
rank(x)      # x[1] = 8 is the 2nd smallest value
order(x)     # the smallest value is x[5]
x[order(x)]  # sorting
```

```text
[1]  8 11 17 25  6
[1] 2 3 4 5 1
[1] 5 1 2 3 4
[1]  6  8 11 17 25
```

### 2.2.2. 秩向量的分布

**定理 2.2.1** 设 $X_1, \dots, X_n$ i.i.d. 来自连续分布（更一般地，可交换且以概率 1 无结），并设 $\mathcal{R}$ 为 $(1, 2, \dots, n)$ 的全部 $n!$ 个置换之集。则秩向量 $\boldsymbol{R}$ 在 $\mathcal{R}$ 上均匀分布：

$$
\mathbb{P}(\boldsymbol{R} = \boldsymbol{r}) = \frac{1}{n!}\quad\text{对每个 } \boldsymbol{r} \in \mathcal{R}.
$$
此外，对 i.i.d. 的观测，$\boldsymbol{R}$ 与次序统计量向量独立。

**证明** 对置换 $\pi$，记 $\boldsymbol{X}^\pi = (X_{\pi(1)}, \dots, X_{\pi(n)})$。它的第 $i$ 个坐标的秩是 $R_{\pi(i)}$，所以 $\boldsymbol{X}^\pi$ 的秩向量是 $\boldsymbol{R}\circ\pi$。由可交换性（定义 1.4.1），$\boldsymbol{X}^\pi \overset{d}{=} \boldsymbol{X}$，因而 $\boldsymbol{R}\circ\pi \overset{d}{=} \boldsymbol{R}$，且 $\mathbb{P}(\boldsymbol{R} = \boldsymbol{r}) = \mathbb{P}(\boldsymbol{R}\circ\pi = \boldsymbol{r}) = \mathbb{P}(\boldsymbol{R} = \boldsymbol{r}\circ\pi^{-1})$。当 $\pi$ 遍历全部置换时，$\boldsymbol{r}\circ\pi^{-1}$ 遍历整个 $\mathcal{R}$，所以这 $n!$ 个概率相等；由于结的概率为零，它们的和为一。关于独立性，次序统计量的联合密度 $n!\prod f(x_{(i)})$（定理 2.1.1）与由哪个 $\boldsymbol{r}$ 产生它们无关：$\mathbb{P}\bigl(\boldsymbol{R} = \boldsymbol{r},\ (X_{(1)},\dots,X_{(n)}) \in A\bigr) = \int_A\prod_i f(x_i)\,\mathrm{d}\boldsymbol{x} = \frac{1}{n!}\mathbb{P}\bigl((X_{(1)},\dots,X_{(n)}) \in A\bigr)$。$\square$

**推论 2.2.1** 在定理 2.2.1 的条件下，对 $i \ne j$ 与互异的 $r, s \in \{1, \dots, n\}$，

$$
\mathbb{P}(R_i = r) = \frac1n,\qquad \mathbb{P}(R_i = r, R_j = s) = \frac{1}{n(n-1)},
$$
$$
\mathbb{E}R_i = \frac{n+1}{2},\quad \operatorname{Var}(R_i) = \frac{(n+1)(n-1)}{12},\quad \operatorname{Cov}(R_i, R_j) = -\frac{n+1}{12},\quad \operatorname{Corr}(R_i, R_j) = -\frac{1}{n-1}.
$$

**证明** 这些概率是数出在一个或两个位置上取指定值的置换个数：$(n-1)!/n!$ 与 $(n-2)!/n!$。所以 $R_i$ 在 $\{1, \dots, n\}$ 上均匀分布，均值为 $\frac{n+1}{2}$，方差为 $\frac1n\sum_{r=1}^nr^2 - \bigl(\frac{n+1}{2}\bigr)^2 = \frac{(n+1)(2n+1)}{6} - \frac{(n+1)^2}{4} = \frac{(n+1)(n-1)}{12}$。关于协方差，$\sum_iR_i = \frac{n(n+1)}{2}$ 是常数，所以

$$
0 = \operatorname{Var}\Bigl(\sum_iR_i\Bigr) = n\operatorname{Var}(R_1) + n(n-1)\operatorname{Cov}(R_1, R_2),
$$
由此得 $\operatorname{Cov}(R_i, R_j) = -\operatorname{Var}(R_1)/(n-1) = -\frac{n+1}{12}$，相关系数为 $-\frac{1}{n-1}$。$\square$

另一条性质解释了秩的大部分吸引力：它们在严格增变换下不变。若 $g$ 严格增，则 $g(X_1), \dots, g(X_n)$ 的秩与 $X_1, \dots, X_n$ 的秩相同。因此，无论数据在原尺度、对数尺度或任何其他单调重标度下分析，秩方法给出的答案都一样；离群值离其余观测多远也不影响它：最大的观测不论多大，秩都是 $n$。

## 2.3. 无分布统计量与秩统计量

**定义 2.3.1（无分布统计量）** 设 $Y_1, \dots, Y_n$ 的联合分布 $D$ 属于某个可能的联合分布族 $\mathcal{F}$。若 $T$ 的分布对每个 $D \in \mathcal{F}$ 都相同，则称统计量 $T(Y_1, \dots, Y_n)$ 在 $\mathcal{F}$ 上是**无分布的**。

**定义 2.3.2（秩统计量）** 只通过秩向量 $\boldsymbol{R}$ 依赖于 $X_1, \dots, X_n$ 的统计量称为**秩统计量**。

**定理 2.3.1** 设 $\mathcal{F}$ 为 $n$ 个 i.i.d. 连续随机变量的联合分布族。每个秩统计量 $V(\boldsymbol{R})$ 在 $\mathcal{F}$ 上都是无分布的。

**证明** 由定理 2.2.1，对 $\mathcal{F}$ 的每个成员，$\boldsymbol{R}$ 在 $\mathcal{R}$ 上均匀分布，所以 $\mathbb{P}\bigl(V(\boldsymbol{R}) = v\bigr) = \#\{\boldsymbol{r}\in\mathcal{R}\colon V(\boldsymbol{r}) = v\}/n!$ 不依赖于分布。$\square$

这就是我们可以舍弃数值而只保留秩的原因：检验统计量的零分布成为一个组合对象，不需要知道总体就可以计算或制表。无分布性指的是原假设：在备择假设下，秩统计量的分布确实依赖于总体，它的功效也是如此。

**例 2.3.1（平移问题）** 设 $X_1, \dots, X_n$ 与 $Y_1, \dots, Y_m$ 是来自连续分布的独立样本，分布函数分别为 $F(x)$ 与 $G(x) = F(x - \Delta)$，$-\infty < \Delta < \infty$，所以 $\Delta$ 是平移参数。如何检验 $H_0\colon\Delta = 0$ 对 $H_1\colon\Delta > 0$？

[3.6.1](/3.6.1) 的置换思想适用：若 $H_0$ 为真，打乱后的数据集看起来像真实数据；否则看起来不同，而观测统计量在打乱后的统计量中的位置给出 $p$ 值。为了得到零分布不依赖于数据的检验，把两个样本合并，设 $R_1, \dots, R_n$ 与 $Q_1, \dots, Q_m$ 分别是 $X$ 与 $Y$ 在合并样本中的秩；$(R_1, \dots, R_n, Q_1, \dots, Q_m)$ 是 $(1, 2, \dots, m + n)$ 的一个置换。要比较 $X$ 的秩与 $Y$ 的秩，只需考虑 $X$ 的秩的某个统计量，Wilcoxon 提出了秩和

$$
W = \sum_{i=1}^nR_i.
$$
$W$ 只通过秩向量依赖于数据。在 $H_0$ 下 $m + n$ 个观测 i.i.d. 且连续，所以由定理 2.3.1，对每个连续的 $F$，$W$ 的分布都相同：它是从 $\{1, \dots, m + n\}$ 中无放回抽取 $n$ 个数之和的置换分布。$W$ 的小值（$X$ 倾向于较小）支持 $H_1$。这就是 [3.2.6](/3.2.6) 的 **Wilcoxon 秩和检验**，其理论在 [3.6.9](/3.6.9) 中展开。

## 2.4. U 统计量

### 2.4.1. 定义

许多常见的估计量，如样本均值、样本方差和样本协方差，具有共同的结构：它们对样本的所有子集平均某个少数几个观测的函数。认识到这一结构，就能用一个框架处理它们的性质（无偏性、相合性、渐近正态性），而不必逐个孤立地处理；它把次序与秩信息的使用推广到相关系数之类的数值特征；它也是后面各章 Wilcoxon 符号秩统计量与 Mann–Whitney 统计量的基础。

**定义 2.4.1（U 统计量）** 设 $X_1, \dots, X_n$ i.i.d.，并设 $\theta = \mathbb{E}\,h(X_1, \dots, X_k)$ 是总体的一个特征，其中 $k \le n$，核 $h$ 是 $k$ 个自变量的对称函数：$h(x_{i_1}, \dots, x_{i_k})$ 在自变量的任何置换下不变。以 $h$ 为核的 **U 统计量**是

$$
U_n = \binom nk^{-1}\sum_{1\le i_1 < \cdots < i_k \le n}h(X_{i_1}, \dots, X_{i_k}),
$$
即 $h$ 在样本的全部 $\binom nk$ 个大小为 $k$ 的子集上的平均。数 $k$ 称为核的次数（或阶）。

由期望的线性性，$\mathbb{E}U_n = \theta$：每个 U 统计量都是其特征的**无偏估计**。对称性并不构成代价：满足 $\mathbb{E}\,h(X_1, \dots, X_k) = \theta$ 的非对称核 $h$ 可以换成它的对称化 $h^*(x_1, \dots, x_k) = \frac{1}{k!}\sum_\pi h(x_{\pi(1)}, \dots, x_{\pi(k)})$，两者期望相同。例如，$h(x_1, x_2) = \boldsymbol{1}\{x_1 \le x_2\}$ 不对称，因为一般 $h(x_1, x_2) \ne h(x_2, x_1)$；它的对称化是 $\frac12\bigl(1 + \boldsymbol{1}\{x_1 = x_2\}\bigr)$，对连续总体几乎必然等于 $\frac12$。这类示性函数在有两个样本时才有信息量，此时 $\mathbb{P}(X \le Y)$ 比较的是两个总体。

### 2.4.2. 例子

**例 2.4.1** (1) *均值。* 取 $k = 1$ 与 $h(x) = x$，$U_n = \frac1n\sum_iX_i = \bar X$：样本均值是一次 U 统计量。

(2) *方差。* 若 $\mu$ 已知，$h(x) = (x - \mu)^2$ 给出无偏的 $\frac1n\sum_i(X_i - \mu)^2$。若 $\mu$ 未知，取 $k = 2$ 与 $h(x_1, x_2) = \frac12(x_1 - x_2)^2$，因为 $\mathbb{E}\frac12(X_1 - X_2)^2 = \sigma^2$。于是

$$
U_n = \frac{1}{n(n-1)}\sum_{i<j}(X_i - X_j)^2 = \frac{1}{n-1}\sum_i(X_i - \bar X)^2 = S^2,
$$
即无偏的**样本方差**。

(3) *均值的平方。* 对 $\theta = \mu^2$，核 $h(x_1, x_2) = x_1x_2$ 给出 $U_n = \binom n2^{-1}\sum_{i<j}X_iX_j$，它用到全部两两乘积且是无偏的，而 $\bar X^2$ 的期望是 $\mu^2 + \sigma^2/n$，不是无偏的。

(4) *Gini 平均差。* 对 $\theta = \mathbb{E}\lvert X_1 - X_2\rvert$，这是一种离散程度的度量，核为对称的 $h(x_1, x_2) = \lvert x_1 - x_2\rvert$。生态学家在四天内测量溶解氧，得到 $6.2, 5.8, 6.5, 5.9\,\mathrm{mg\,L^{-1}}$；六个绝对差为 $0.4, 0.3, 0.3, 0.7, 0.1, 0.6$，所以 $U_4 = 2.4/6 = 0.4\,\mathrm{mg\,L^{-1}}$。

(5) *Wilcoxon 符号秩统计量。* 对 $\theta = \mathbb{P}(X_1 + X_2 > 0)$，核 $h(x_1, x_2) = \boldsymbol{1}\{x_1 + x_2 > 0\}$ 是对称的。[3.6.3](/3.6.3) 的符号秩统计量 $S_+$ 可以写成 $\sum_{i\le j}\boldsymbol{1}\{X_i + X_j > 0\}$，即正的两两平均的个数；除去 $i = j$ 的 $n$ 项和一个因子 $\binom n2$，它就是这个 U 统计量。

(6) *两个样本。* 定义可以推广到两个样本，核 $h(x_1, \dots, x_k; y_1, \dots, y_l)$ 在两个样本的子集上平均。取 $h(x; y) = \boldsymbol{1}\{x < y\}$，两样本 U 统计量 $\frac{1}{nm}\sum_{i,j}\boldsymbol{1}\{X_i < Y_j\}$ 估计 $\mathbb{P}(X < Y)$；它是例 2.3.1 秩和统计量的 Mann–Whitney 形式（[3.6.9](/3.6.9)）。

### 2.4.3. 性质

除无偏性外，U 统计量还有两条重要性质，这里不加证明地陈述。

- *最优性。* 每个对称统计量都是次序统计量的函数，而 $U_n$ 是 $h(X_1, \dots, X_k)$ 关于次序统计量的条件期望。对于 $\theta$ 存在的所有分布构成的非参数族，次序统计量是完全充分的，所以 $U_n$ 是 $\theta$ 在该族中的**一致最小方差无偏估计**（Halmos，1946）。因此，当对总体不做任何假定时，它的精度保证就是最佳无偏估计量的精度。
- *渐近正态性*（Hoeffding，1948）。设 $h_1(x) = \mathbb{E}\,h(x, X_2, \dots, X_k)$，$\zeta_1 = \operatorname{Var}\bigl(h_1(X_1)\bigr)$。若 $\mathbb{E}h^2 < \infty$ 且 $\zeta_1 > 0$，则
  $$
  \sqrt n\,(U_n - \theta) \xrightarrow{d} \mathcal{N}(0, k^2\zeta_1).
  $$
  对样本均值，$k = 1$，$\zeta_1 = \sigma^2$，这就是通常的中心极限定理。

**注 2.4.1** 次序统计量有时被描述为 $k = n$ 的"平凡"U 统计量：核 $h(x_1, \dots, x_n) = \operatorname{median}(x_1, \dots, x_n)$ 是对称的，大小为 $n$ 的子集只有一个，所以 $U_n$ 就是样本中位数。这是没有平均的极限情形，而正是平均赋予 U 统计量那些性质；它只无偏地估计 $\mathbb{E}\operatorname{median}(X_1, \dots, X_n)$，后者随 $n$ 变化，一般不同于总体中位数。上述理论针对的是固定次数 $k$ 的核。还要注意，这里"核"一词指函数 $h$，与密度估计的**核函数**（[3.2.3](/3.2.3)）无关。

## 2.5. 经验分布函数

**定义 2.5.1（经验分布函数）** 设 $X_1, \dots, X_n$ i.i.d.，分布函数为 $F$。经验分布函数（EDF）为

$$
F_n(x) = \frac1n\sum_{i=1}^n\boldsymbol{1}\{X_i \le x\},\qquad x \in \mathbb{R}.
$$

$F_n$ 是阶梯函数，在每个观测处上升 $1/n$（在观测到 $k$ 次的值处上升 $k/n$）；它本身是分布函数，即观测值上的均匀分布的分布函数。它的基本性质（[3.2.1](/3.2.1)）都来自一个事实：对每个固定的 $x$，

$$
nF_n(x) = \sum_{i=1}^n\boldsymbol{1}\{X_i \le x\} \sim \mathrm{Bin}\bigl(n, F(x)\bigr).
$$
因此 $\mathbb{E}F_n(x) = F(x)$，$\operatorname{Var}\bigl(F_n(x)\bigr) = \frac1nF(x)\bigl(1 - F(x)\bigr)$：$F_n(x)$ 是 $F(x)$ 的无偏估计，它是相合的（$F_n(x) \xrightarrow{p} F(x)$，事实上几乎必然），并且由 de Moivre–Laplace 定理它是渐近正态的，$\sqrt n\bigl(F_n(x) - F(x)\bigr) \xrightarrow{d} \mathcal{N}\bigl(0, F(x)(1 - F(x))\bigr)$。Glivenko–Cantelli 定理把相合性加强为一致收敛，$\sup_x\lvert F_n(x) - F(x)\rvert \xrightarrow{\text{a.s.}} 0$，常被称为（非参数）统计学的基本定理。

EDF 也可以看作非参数极大似然估计。在全部分布函数 $G$ 中考虑似然 $L(G) = \prod_{i=1}^n\mathbb{P}_G(\{x_i\})$，即 $G$ 赋予观测值的概率。若互异的值 $x_1, \dots, x_m$ 分别出现 $k_1, \dots, k_m$ 次，$p_j = \mathbb{P}_G(\{x_j\})$，则 $L = \prod_jp_j^{k_j}$，且 $\sum_jp_j \le 1$；在此约束下最大化 $\sum_jk_j\log p_j$ 得 $p_j = k_j/n$，这恰好就是 $F_n$。任何在观测值之外还有质量的分布，特别是任何连续分布，似然都为零。

在 R 中，`ecdf(x)` 以函数形式返回 EDF，可以对它求值与作图：

```r
n <- 30
x <- rnorm(n)
Fn <- ecdf(x)                 # Fn is a function
plot(Fn, verticals = TRUE, do.points = FALSE)
curve(pnorm(x), add = TRUE, col = 2)   # the true CDF
```

形如"p 后接分布名"的函数（`pnorm`、`pexp`、`pbinom` 等）给出用于比较的理论分布函数；随着 $n$ 增大，EDF 越来越接近 CDF。

## 2.6. Kolmogorov 距离

### 2.6.1. 定义与计算

一个给定的样本是指数分布的样本吗？画上指数密度的直方图有提示作用，但依赖于分组；把 EDF 与假设的分布函数比较更直接，而最大偏差的大小概括了这一比较。

**定义 2.6.1（Kolmogorov 距离）** 两个分布函数 $G$ 与 $F$ 之间的 **Kolmogorov 距离**是 $D_{\mathrm{K}}(G, F) = \sup_x\lvert G(x) - F(x)\rvert$。对 EDF 为 $F_n$ 的样本和假设的连续 $F$，记

$$
D_n = D_{\mathrm{K}}(F_n, F) = \sup_x\lvert F_n(x) - F(x)\rvert = \max_{1\le i\le n}\max\Bigl\{\frac in - F(x_{(i)}),\ F(x_{(i)}) - \frac{i-1}{n}\Bigr\},
$$
其中 $x_{(1)} < \cdots < x_{(n)}$ 是排好序的样本。

公式成立是因为在相邻次序统计量之间 $F_n$ 是常数而 $F$ 不减，所以在每个区间上最大的差距出现在端点：恰在 $x_{(i)}$ 之前（此处 $F_n = \frac{i-1}{n}$）或在 $x_{(i)}$ 处（此处 $F_n = \frac in$）。计算只需要排好序的数据：

```r
ksdist <- function(x, CDF, ...) {
  sortx <- sort(x); n <- length(x)
  distup   <- (1:n) / n - CDF(sortx, ...)        # right end of each jump
  distdown <- CDF(sortx, ...) - (0:(n - 1)) / n  # left end of each jump
  max(pmax(distup, distdown))                    # Kolmogorov distance
}
set.seed(10)
x <- rexp(100)
ksdist(x, pexp, rate = 1)
ks.test(x, "pexp", rate = 1)$statistic
ks.test(x, "pnorm", mean = 0, sd = 0.1)$statistic
```

```text
[1] 0.08466882
         D
0.08466882
        D
0.8077886
```

到真实的 $\mathrm{Exp}(1)$ 分布的距离是 $0.085$；到严重错误的目标 $\mathcal{N}(0, 0.1^2)$ 的距离是 $0.81$。距离随目标分布如此剧烈地变化，是否说明 Kolmogorov 检验不是无分布的？不是：无分布性是关于 $D_n$ 的零分布的陈述，计算的是目标 $F$ 为真实分布时的情形，对到错误目标的距离什么也没说。对错误的目标距离很大，恰恰是检验有功效的原因。

其他距离比较的是整条曲线，而不是最大的偏差。*单侧* Kolmogorov 统计量是 $D_n^+ = \sup_x\bigl(F_n(x) - F(x)\bigr)$ 与 $D_n^- = \sup_x\bigl(F(x) - F_n(x)\bigr)$，$D_n = \max(D_n^+, D_n^-)$；它们用于检验单侧备择假设，由下面的论证它们是无分布的，由均匀分布的对称性 $u \mapsto 1 - u$，$D_n^+$ 与 $D_n^-$ 同分布，并且它们的精确分布比 $D_n$ 的容易推导得多（[3.6.6](/3.6.6)）。Cramér–von Mises 距离

$$
D_{\mathrm{CvM}}(F_n, F) = \int\bigl(F_n(x) - F(x)\bigr)^2\,\mathrm{d}F(x)
$$
对偏差的平方取平均，而 Anderson–Darling 距离以 $1/\bigl(F(1 - F)\bigr)$ 加权以突出尾部；它们导出 **Cramér–von Mises 检验**与 **Anderson–Darling 检验**（[3.3.5](/3.3.5)）。

### 2.6.2. 无分布性

要用统计量 $D_n$ 检验 $H_0\colon X_1, \dots, X_n \overset{\text{iid}}{\sim} F$ 对"其他情形"，需要它的零分布，并且应当证明它不依赖于 $F$。想法是：对 $x$ 轴做单调变换不改变竖直方向的距离。

**定理 2.6.1** 若 $F$ 连续且 $X_1, \dots, X_n \overset{\text{iid}}{\sim} F$，则 $D_n = D_{\mathrm{K}}(F_n, F)$ 与 $D_{\mathrm{K}}(U_n, F_{\mathrm{U}})$ 同分布，其中 $U_n$ 是来自 $\mathrm{U}(0, 1)$ 的大小为 $n$ 的样本的 EDF，$F_{\mathrm{U}}(y) = y$。因此 $D_n$ 在连续分布族上是无分布的。

**证明** 令 $U_i = F(X_i)$。由概率积分变换，$U_1, \dots, U_n \overset{\text{iid}}{\sim} \mathrm{U}(0, 1)$，因为对连续的 $F$，$\mathbb{P}(F(X) \le y) = \mathbb{P}(X \le F^{-1}(y)) = F(F^{-1}(y)) = y$。设 $U_n(y) = \frac1n\sum_i\boldsymbol{1}\{U_i \le y\}$ 是它们的 EDF。对每个 $x$，几乎必然有 $\boldsymbol{1}\{X_i \le x\} = \boldsymbol{1}\{F(X_i) \le F(x)\}$，所以 $F_n(x) = U_n(F(x))$，且

$$
\sup_{x\in\mathbb{R}}\lvert F_n(x) - F(x)\rvert = \sup_{x\in\mathbb{R}}\bigl\lvert U_n(F(x)) - F(x)\bigr\rvert = \sup_{0<y<1}\lvert U_n(y) - y\rvert,
$$
最后一步是因为连续的 $F$ 取遍 $(0, 1)$ 中的每个值（端点没有贡献）。因此对每个 $t$ 有 $\mathbb{P}(D_n \le t) = \mathbb{P}\bigl(\sup_y\lvert U_n(y) - y\rvert \le t\bigr)$。$\square$

于是 $D_n$ 的零分布可以对均匀分布一次算好，用于每个连续的 $F$。若 $F$ 有跳跃，同样的论证表明 $D_n$ 在随机序意义下比连续情形小，所以采用连续情形临界值的检验是保守的。

![左：大小为 100 的指数样本的 EDF 与 Exp(1) 分布函数，图中标出 Kolmogorov 距离。右：来自四个不同连续总体的、大小为 20 的 10000 个样本上 sqrt(n) D_n 的经验分布，它们如定理 2.6.1 所断言的那样重合，并给出 n 增大时的极限。](./plots/ks-distance.py)

### 2.6.3. 极限分布与 DKW 不等式

距离 $D_n$ 以速率 $1/\sqrt n$ 缩小，Kolmogorov（1933）找到了重新标度后的距离的极限分布。

**定理 2.6.2（Kolmogorov）** 若 $F$ 连续，则对每个 $d > 0$，

$$
\lim_{n\to\infty}\mathbb{P}\bigl(\sqrt n\,D_n \le d\bigr) = K(d) = 1 - 2\sum_{k=1}^\infty(-1)^{k-1}\mathrm{e}^{-2k^2d^2}.
$$

分位数 $K^{-1}(0.95) = 1.358$ 与 $K^{-1}(0.99) = 1.628$ 给出 Kolmogorov–Smirnov 检验的大样本临界值 $1.358/\sqrt n$ 与 $1.628/\sqrt n$。对中等样本这一近似已经够用；$n$ 小时精确零分布有表可查，而当 $n < 100$ 且无结时，R 的 `ks.test` 默认计算精确 $p$ 值。在 [3.6.6](/3.6.6) 中我们将看到，$K$ 是 Brown 桥 $B$ 的 $\sup_t\lvert B(t)\rvert$ 的分布，即均匀经验过程 $\sqrt n\bigl(U_n(t) - t\bigr)$ 的极限。

对每个样本量都成立的一个方便的非渐近补充如下。

**定理 2.6.3（Dvoretzky–Kiefer–Wolfowitz 不等式）** 对每个分布函数 $F$、每个 $n \ge 1$ 与每个 $\varepsilon > 0$，

$$
\mathbb{P}\Bigl(\sup_x\lvert F_n(x) - F(x)\rvert > \varepsilon\Bigr) \le 2\mathrm{e}^{-2n\varepsilon^2}.
$$

Dvoretzky、Kiefer 与 Wolfowitz（1956）证明了这个不等式，其中用一个未指明的常数代替 $2$；Massart（1990）证明常数 $2$ 是可用的，并且它不可改进，因为由定理 2.6.2，$1 - K(\varepsilon\sqrt n)$ 的首项是 $2\mathrm{e}^{-2n\varepsilon^2}$。该不等式不需要 $F$ 连续，并给出 Glivenko–Cantelli 定理的明确速率：一致误差大于 $\varepsilon$ 的概率随 $n$ 指数衰减。

## 2.7. $F$ 的置信区间与置信带

### 2.7.1. 逐点区间

回忆参数 $\theta$ 的置信水平为 $1 - \alpha$ 的置信区间是随机区间 $\bigl(l(\boldsymbol{X}), u(\boldsymbol{X})\bigr)$，对每个 $\theta$ 满足 $\mathbb{P}\bigl(l(\boldsymbol{X}) < \theta < u(\boldsymbol{X})\bigr) \ge 1 - \alpha$。对分布函数，有两个不同的问题。逐点问题固定 $x$，要求一个区间 $C(x) = \bigl(L(x), U(x)\bigr)$，使得对每个 $F$，

$$
\mathbb{P}\bigl(F(x) \in C(x)\bigr) \ge 1 - \alpha.
$$
由于 $nF_n(x) \sim \mathrm{Bin}(n, F(x))$，这是关于二项比例的问题。取 $k = nF_n(x)$，精确的 **Clopper–Pearson 区间**（[3.6.5](/3.6.5)）为

$$
\Bigl(\beta_{\alpha/2}(k, n - k + 1),\ \beta_{1-\alpha/2}(k + 1, n - k)\Bigr),
$$
其中 $\beta_q(a, b)$ 是 $\mathrm{Beta}(a, b)$ 的 $q$ 分位数（$k = 0$ 时下限取 $0$，$k = n$ 时上限取 $1$）。在 R 中，`binom.test(sum(x <= x0), n)$conf.int` 计算它。

### 2.7.2. 同时置信带

**定义 2.7.1（分布函数的置信带）** 若对每个 $F$，

$$
\mathbb{P}\bigl(L(x) \le F(x) \le U(x)\ \text{对所有 } x\bigr) \ge 1 - \alpha,
$$
则由样本算出的一对函数 $L(x) \le U(x)$ 称为 $F$ 的 $1 - \alpha$ 置信带。这样的带也称为同时置信区间或置信包络。

把逐点区间连起来并不给出置信带。设 $A$ 与 $B$ 是 $x_1$ 与 $x_2$ 处的区间覆盖的事件，各自的概率为 $1 - \alpha$，但 $\mathbb{P}(A\cap B)$ 一般更小：只有当两个事件独立时它才等于 $(1 - \alpha)^2$（它们并不独立；$F_n(x_1)$ 与 $F_n(x_2)$ 正相关），而 Bonferroni 不等式只给出 $\mathbb{P}(A\cap B) \ge 1 - 2\alpha$。在连续统的 $x$ 上，连起来的逐点区间的同时覆盖率可以远低于 $1 - \alpha$。因此在同一水平下，置信带比逐点区间更宽。它的优点是可用来评判整个候选分布：任何离开带的 $F$ 都在水平 $\alpha$ 下被拒绝。

Kolmogorov 距离在这里是一个枢轴量。由定理 2.6.2，

$$
1 - \alpha \approx \mathbb{P}\Bigl(\sqrt n\sup_x\lvert F_n(x) - F(x)\rvert \le K^{-1}(1 - \alpha)\Bigr) = \mathbb{P}\Bigl(F_n(x) - \frac{K^{-1}(1-\alpha)}{\sqrt n} \le F(x) \le F_n(x) + \frac{K^{-1}(1-\alpha)}{\sqrt n}\ \forall x\Bigr).
$$
等价地，不借助任何渐近性，令 DKW 不等式的右端等于 $\alpha$：

$$
2\mathrm{e}^{-2n\varepsilon^2} = \alpha\quad\Longrightarrow\quad \varepsilon = \sqrt{\frac{1}{2n}\log\frac2\alpha}.
$$
于是

$$
L(x) = \max\{F_n(x) - \varepsilon, 0\},\qquad U(x) = \min\{F_n(x) + \varepsilon, 1\}
$$
对任意 $F$ 与任意 $n$ 定义一个 $1 - \alpha$ 置信带。对 $\alpha = 0.05$，$\varepsilon = \sqrt{\log 40/(2n)} = 1.358/\sqrt n$，数值上与渐近的 Kolmogorov 带相同：在通常的水平下，DKW 不等式基本上是精确的。

```r
Fn <- ecdf(x); x <- sort(x); n <- length(x)
l1 <- u1 <- l2 <- u2 <- numeric(n)
epsilon <- sqrt((1 / (2 * n)) * log(2 / 0.05))
for (i in 1:n) {
  ci <- binom.test(sum(x <= x[i]), n)$conf.int   # pointwise Clopper-Pearson
  l1[i] <- ci[1]; u1[i] <- ci[2]
  l2[i] <- max(Fn(x[i]) - epsilon, 0)             # DKW band
  u2[i] <- min(Fn(x[i]) + epsilon, 1)
}
plot(Fn, verticals = TRUE, do.points = FALSE, main = "Confidence interval & band")
polygon(c(x, rev(x)), c(l2, rev(u2)), col = "gray85", border = FALSE)
polygon(c(x, rev(x)), c(l1, rev(u1)), col = "gray70", border = FALSE)
plot(Fn, verticals = TRUE, do.points = FALSE, add = TRUE)
```

![大小为 50 的标准正态样本的 EDF，及 95% 逐点 Clopper-Pearson 区间（深色）、95% DKW 置信带（浅色）和真实分布函数（位于带内）。](./plots/edf-bands.py)

## 2.8. 经验分位数函数与 Q–Q 图

### 2.8.1. 经验分位数函数

对连续且严格增的 $F$，反函数 $F^{-1}$ 唯一，且 $F^{-1}(p) \le x \iff p \le F(x)$。像 $F_n$ 这样的阶梯函数没有反函数，我们使用 [3.1.7](/3.1.7) 的广义逆，即分位数函数 $F^{-1}(p) = \inf\{x\colon F(x) \ge p\}$。

**定义 2.8.1（经验分位数函数）** 样本的**经验分位数函数**为

$$
F_n^{-1}(p) = \inf\{y\colon F_n(y) \ge p\} = X_{(\lceil np\rceil)},\qquad 0 < p \le 1.
$$

第二个表达式成立是因为 $F_n(X_{(i)}) = i/n$：$F_n$ 达到 $p$ 的最小次序统计量是满足 $i \ge np$ 的那个。与每个分位数函数一样，$F_n^{-1}$ 不减且左连续：$F^{-1}(p) \le x$ 当且仅当 $p \le F(x)$，所以 $\{p\colon F^{-1}(p) \le x\} = (0, F(x)]$ 右端是闭的，这等价于 $F^{-1}$ 左连续。它是阶梯函数，在 $p = i/n$ 处跳跃。

**例 2.8.1** 对样本 $-1.55, -0.67, -0.39, 0.60$（$n = 4$），$F_n^{-1}(0.25) = X_{(1)} = -1.55$，$F_n^{-1}(0.4) = X_{(\lceil1.6\rceil)} = X_{(2)} = -0.67$。R 的 `quantile(x, p, type = 1)` 计算这一反函数；默认的 `type = 7` 在次序统计量之间线性插值，所以报告的样本分位数取决于所用的约定。

### 2.8.2. Q–Q 图

分位数–分位数图通过分位数函数比较两个分布：对 $0$ 与 $1$ 之间的 $p$ 画点 $\bigl(F^{-1}(p), F_n^{-1}(p)\bigr)$，实际中画的是点

$$
\Bigl(F^{-1}(p_i),\ x_{(i)}\Bigr),\qquad p_i = \frac{i - 1/2}{n},\quad i = 1, \dots, n.
$$
使用作图位置 $p_i = (i - 1/2)/n$ 而不是 $i/n$，是因为对支撑无界的分布 $F^{-1}(1)$ 是无穷的。$F$ 的常见选择是标准正态分布，得到 [3.2.6](/3.2.6) 的**正态 QQ 图**，但可以用任何指定的分布。若样本来自 $F$ 的位置–尺度族，即来自 $F\bigl((x - \mu)/\sigma\bigr)$，则点落在截距为 $\mu$、斜率为 $\sigma$ 的直线附近；这就是为什么该图不需要参数已知。在正态 Q–Q 图上，系统性的偏离有典型的形状：

| 总体 | 正态 Q–Q 图的形状 |
|---|---|
| 正态 | 直线 |
| 右偏（指数） | 下凸曲线：上分位数过大，下分位数过于靠近 |
| 重尾（Cauchy） | S 形，两端变陡 |
| 轻尾（均匀） | 倒 S 形，两端变平 |

### 2.8.3. 带置信带的 Q–Q 图

当点看起来偏离直线时需要小心，因为有抽样变异：即使来自假设分布的样本也会偏离直线，尾部尤其如此。把抽样变异的可能范围标在图上很有用，而 $F$ 的同时置信带可以直接变换成 Q–Q 图的置信带。正态分布 $\mathcal{N}(\mu, \sigma^2)$ 位于带 $F_n \pm k$ 之内，当且仅当

$$
F_n(x) - k \le \Phi\Bigl(\frac{x - \mu}{\sigma}\Bigr) \le F_n(x) + k\quad\text{对所有 } x,
$$
而这等价于

$$
\Phi^{-1}\bigl(F_n(x) - k\bigr) \le \frac{x - \mu}{\sigma} \le \Phi^{-1}\bigl(F_n(x) + k\bigr)\quad\text{对所有 } x,
$$
即直线 $z = (x - \mu)/\sigma$ 位于两条变换后的界之间。取 DKW 不等式（或 Kolmogorov 分位数）给出的 $k$，该带同时以至少 $1 - \alpha$ 的概率成立，并且若有某条直线能放进带内，则数据在水平 $\alpha$ 下与正态性相容。在高度 $x_{(i)}$ 处，直线必须从 $\Phi^{-1}(i/n - k)$ 与 $\Phi^{-1}\bigl((i-1)/n + k\bigr)$ 之间通过，它们是界恰在 $F_n$ 跳跃处与恰在跳跃之前的值。

![由 DKW 带导出的、带 95% 同时置信带的正态 Q-Q 图，左为正态样本，右为指数样本，样本量均为 50。若有某条直线穿过每一段水平的带，则正态分布在水平 0.05 下与数据相容。指数样本的弯曲可以看出，但 n = 50 时带很宽。](./plots/qq-bands.py)

有两点提醒。第一，该带针对的是完全指定的 $F$；若 $\mu$ 与 $\sigma$ 由数据估计，拟合的直线比真实直线更靠近各点，用该带判断"带某些参数的正态性"是保守的，这个问题将在 [3.6.6](/3.6.6) 随 Lilliefors 检验一并讨论。第二，这种带在图的尾部很宽，那里正态分位数变化很快，所以 Q–Q 图首先仍然是一种视觉诊断：正式检验量化总体的拟合程度，而图显示拟合在何处、以何种方式失败。

## 小结

| 对象 | 定义 | 关键的分布事实 |
|---|---|---|
| 次序统计量 $X_{(i)}$（定义 2.1.1） | 排好序的样本 | 对每个连续的 $F$，$F(X_{(i)}) \sim \mathrm{Beta}(i, n - i + 1)$（推论 2.1.1） |
| 秩 $R_i$（定义 2.2.1） | $X_i = X_{(R_i)}$ | $\boldsymbol{R}$ 在 $n!$ 个置换上均匀（定理 2.2.1）；$\mathbb{E}R_i = \frac{n+1}{2}$，$\operatorname{Var}R_i = \frac{n^2-1}{12}$，$\operatorname{Cov} = -\frac{n+1}{12}$ |
| 秩统计量（定义 2.3.2） | 只是 $\boldsymbol{R}$ 的函数 | 在 i.i.d. 连续总体上无分布（定理 2.3.1）；在增变换下不变 |
| U 统计量（定义 2.4.1） | 对称核在全部 $k$ 子集上的平均 | 无偏；在非参数族中是无偏估计里方差最小的；渐近正态 |
| EDF $F_n$（定义 2.5.1） | 不超过 $x$ 的观测所占比例 | $nF_n(x) \sim \mathrm{Bin}(n, F(x))$；一致收敛（Glivenko–Cantelli）；非参数 MLE |
| Kolmogorov 距离 $D_n$（定义 2.6.1） | $\sup_x\lvert F_n - F\rvert$，在跳跃处计算 | 对连续的 $F$ 无分布（定理 2.6.1）；$\sqrt nD_n \to K$（定理 2.6.2）；DKW：$\mathbb{P}(D_n > \varepsilon) \le 2\mathrm{e}^{-2n\varepsilon^2}$（定理 2.6.3） |
| 经验分位数函数（定义 2.8.1） | $F_n^{-1}(p) = X_{(\lceil np\rceil)}$ | 左连续阶梯函数；Q–Q 图的基础 |

- $F(x)$ 的逐点区间：对 $nF_n(x)$ 用 Clopper–Pearson。同时置信带（定义 2.7.1）：$F_n \pm \varepsilon$，$\varepsilon = \sqrt{\log(2/\alpha)/(2n)}$，在 $\alpha = 0.05$ 时等于 $1.358/\sqrt n$。把逐点区间连起来并不给出置信带；置信带更宽。
- Q–Q 图：$(F^{-1}(p_i), x_{(i)})$，$p_i = (i - \frac12)/n$；对 $F$ 的位置–尺度族是直线；DKW 带可以变换成图的置信带。

## 思考题

1. 对 i.i.d. 连续样本，其秩为 $R_1, \dots, R_n$，证明对 $i \ne j$、$r \ne s$ 有 $\mathbb{P}(R_i = r, R_j = s) = \frac{1}{n(n-1)}$，并直接由这一联合分布推出 $\operatorname{Cov}(R_i, R_j)$。

   **答** 由定理 2.2.1，全部 $n!$ 个秩向量等可能，其中有 $(n-2)!$ 个在位置 $i$ 取 $r$、在位置 $j$ 取 $s$，所以概率为 $(n-2)!/n! = \frac{1}{n(n-1)}$。于是

   $$
   \mathbb{E}R_iR_j = \frac{1}{n(n-1)}\sum_{r\ne s}rs = \frac{1}{n(n-1)}\Bigl[\Bigl(\sum_rr\Bigr)^2 - \sum_rr^2\Bigr] = \frac{1}{n(n-1)}\Bigl[\frac{n^2(n+1)^2}{4} - \frac{n(n+1)(2n+1)}{6}\Bigr] = \frac{(n+1)(3n+2)}{12},
   $$
   且 $\operatorname{Cov}(R_i, R_j) = \frac{(n+1)(3n+2)}{12} - \frac{(n+1)^2}{4} = \frac{(n+1)(3n + 2 - 3n - 3)}{12} = -\frac{n+1}{12}$，与推论 2.2.1 一致。
2. 分位数函数 $F^{-1}(p) = \inf\{x\colon F(x) \ge p\}$ 是左连续还是右连续？为什么？

   **答** 左连续。因为 $F$ 右连续，下确界可以取到，所以 $F^{-1}(p) \le x \iff p \le F(x)$。设 $p_k \uparrow p$。值 $F^{-1}(p_k)$ 递增到某个极限 $x^* \le F^{-1}(p)$；对每个 $k$，$F^{-1}(p_k) \le x^*$，所以 $p_k \le F(x^*)$，令 $k \to \infty$ 得 $p \le F(x^*)$，即 $F^{-1}(p) \le x^*$。因此 $F^{-1}(p_k) \to F^{-1}(p)$。它不一定右连续：若 $F$ 在区间 $[a, b)$ 上于高度 $p$ 处是平的，则 $F^{-1}(p) = a$，但对每个 $\delta > 0$ 有 $F^{-1}(p + \delta) \ge b$。
3. 生成 $100$ 个观测，计算 $95\%$ DKW 置信带，并重复 $1000$ 次，记录该带包含真实分布函数的频率，分别对 $F = \mathcal{N}(0, 1)$ 与标准 Cauchy 分布做一次。你预期会怎样？

   **答** 两种情形下比例都应至少约为 $95\%$（事实上接近 $95\%$ 而略高，因为 $\varepsilon = 1.358/\sqrt{100}$ 几乎恰是 Kolmogorov 分位数，而 $\sqrt nD_n$ 的有限样本分布在随机序意义下略小于其极限）。Cauchy 分布的重尾没有任何影响：由定理 2.6.1，事件 $\{\sup_x\lvert F_n - F\rvert \le \varepsilon\}$ 对每个连续的 $F$ 概率相同，而 DKW 不等式对每个 $F$ 成立。重复 $4000$ 次的模拟给出的覆盖率为 $0.955$（正态）与 $0.954$（Cauchy）。
4. 二十四个观测来自 $\mathrm{U}(0, 10)$ 或 $(0, 10)$ 上的对称三角分布：$4.17, 8.42, 3.02, 2.89, 9.77, 6.06, 2.72, 5.12, 6.00, 4.78, 2.62, 7.20, 1.61, 5.92, 7.25, 8.01, 4.76, 5.36, 5.34, 7.59, 0.66, 7.27, 3.39, 1.40$。用 Kolmogorov 距离与 $95\%$ DKW 置信带比较这两个候选分布。哪个更合理？

   **答** Kolmogorov 距离到 $\mathrm{U}(0, 10)$ 为 $D = 0.137$（最大偏差在 $x = 2.62$），到三角分布为 $D = 0.135$（在 $x = 7.20$），而 $95\%$ DKW 半宽为 $\varepsilon = \sqrt{\log 40/48} = 0.277$。两个分布函数都舒适地落在带内，两个 Kolmogorov–Smirnov $p$ 值都约为 $0.7$。数据无法区分这两个候选：$n = 24$ 时带太宽。对每个候选画的 Q–Q 图看上去都大致是直线（三角分布的在中部略好，均匀分布的在尾部略好），这证实需要更多数据才能做出判断。
5. 现要用 U 统计量估计 $\theta = \mathbb{E}\lvert X_1 - X_2\rvert$，即两个独立日期溶解氧水平的平均绝对差。它为什么是无偏的？为什么没有一次核能完成这一任务？

   **答** 取对称核 $h(x_1, x_2) = \lvert x_1 - x_2\rvert$，每一项 $h(X_i, X_j)$（$i < j$）都涉及总体的两个独立观测，所以其期望为 $\theta$，而期望为 $\theta$ 的各项的平均，期望也是 $\theta$（例 2.4.1 (4) 对四次测量给出 $U_4 = 0.4$）。一次核要求有函数 $g$ 使得对该族中的每个分布都有 $\mathbb{E}g(X) = \mathbb{E}\lvert X_1 - X_2\rvert$，这是不可能的，因为 $\theta$ 是分布的非线性泛函（例如它不是混合线性的：两个分布的混合的 $\theta$ 并不是它们各自 $\theta$ 的相应混合）。特征的次数是存在无偏核的最小 $k$，这里是 $k = 2$。
