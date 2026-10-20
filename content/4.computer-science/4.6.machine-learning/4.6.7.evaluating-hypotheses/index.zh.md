---
title: 假设评估与学习算法比较
description: 样本错误率与真实错误率；用二项分布与正态近似给出错误率的置信区间；比较两个假设的错误率；用 k 折交叉验证与配对 t 检验、5×2 交叉验证检验和 McNemar 检验比较学习算法。
---

学到一个假设之后，我们关心它在没有见过的数据上表现如何；比较两个模型或两个算法时，关心观察到的差异是真实的还是偶然的。数据总是有限的，测试集上的准确率本身是一个随机变量，所以这些都是统计问题。本章回答假设评估的三个问题：

1. 一个假设在有限样本上的准确率，能在多大程度上代表它在整个实例空间上的准确率？
2. 假设 $h_1$ 在一个样本上比 $h_2$ 好，那么一般情况下 $h_1$ 更好的可能性有多大？
3. 数据有限时，怎样最好地同时用于学习和评估，并比较两个学习算法？

所用的统计工具都已在统计学中讲过：**二项分布**与**中心极限定理**（[3.1.4](/3.1.4)、[3.1.13](/3.1.13)）、**置信区间**（[3.2.4](/3.2.4)）、**假设检验**与 **t 检验**（[3.2.5](/3.2.5)）。本章把它们用到机器学习的评估中，并补充机器学习特有的问题：训练集与测试集的依赖、交叉验证中各折之间的相关，以及为此设计的检验方法。评价指标与实验设计的基本原则见 [4.6.2](/4.6.2)。

## 7.1. 样本错误率与真实错误率

设实例空间 $X$ 中的实例按某个固定而未知的分布 $\mathcal{D}$ 出现，目标概念 $c\colon X \to \{0, 1\}$ 给出每个实例的真实标记，学习算法从假设空间 $H$ 中选出假设 $h$。我们希望 $h(x) = c(x)$ 对一切 $x \in X$ 成立，但 $X$ 通常极大：若实例由 $n$ 个二值属性描述，$X$ 就有 $2^n$ 个元素，$X$ 上的概念多达 $2^{2^n}$ 个（每个概念是 $X$ 的一个子集）。我们只能在能够获取的样例集合 $S \subseteq X$ 上检查 $h$，而真正关心的是它在整个 $X$ 上的表现。

**定义 7.1.1（样本错误率与真实错误率）** 假设 $h$ 关于目标概念 $c$ 和分布 $\mathcal{D}$ 的**真实错误率**是 $h$ 误分类一个按 $\mathcal{D}$ 随机抽取的实例的概率

$$
\operatorname{error}_{\mathcal{D}}(h) = \mathbb{P}_{x \sim \mathcal{D}}\big(c(x) \ne h(x)\big).
$$
$h$ 在含 $n$ 个样例的样本 $S$ 上的**样本错误率**是 $S$ 中被 $h$ 误分类的样例所占的比例

$$
\operatorname{error}_S(h) = \frac1n\sum_{x \in S}\boldsymbol{1}\{c(x) \ne h(x)\}.
$$

真实错误率是我们想知道却无法直接观测的量，样本错误率是可以直接算出的量。本章的问题都是：$\operatorname{error}_S(h)$ 作为 $\operatorname{error}_{\mathcal{D}}(h)$ 的估计有多好？

## 7.2. 估计假设的错误率

### 7.2.1. 错误率估计的分布

设 $S$ 中的 $n$ 个样例独立地按 $\mathcal{D}$ 抽取，并且与 $h$ 独立（没有参与 $h$ 的训练与选择）。每个样例被误分类与否是一次 Bernoulli 试验，成功（误分类）的概率是 $p = \operatorname{error}_{\mathcal{D}}(h)$。误分类的个数 $r$ 服从**二项分布** $\mathrm{Bin}(n, p)$：

$$
\mathbb{P}(r = k) = \binom nk p^k(1 - p)^{n-k},\qquad \mathbb{E}[r] = np,\qquad \operatorname{Var}(r) = np(1 - p).
$$
于是 $\operatorname{error}_S(h) = r/n$ 满足

$$
\mathbb{E}\big[\operatorname{error}_S(h)\big] = \operatorname{error}_{\mathcal{D}}(h),\qquad
\sigma_{\operatorname{error}_S(h)} = \sqrt{\frac{\operatorname{error}_{\mathcal{D}}(h)\big(1 - \operatorname{error}_{\mathcal{D}}(h)\big)}{n}} \approx \sqrt{\frac{\operatorname{error}_S(h)\big(1 - \operatorname{error}_S(h)\big)}{n}} .
$$

**例 7.2.1** $h$ 在 $n = 100$ 个测试样例上错了 $r = 12$ 个，$\operatorname{error}_S(h) = 0.12$，标准差约为 $\sqrt{0.12 \times 0.88/100} \approx 0.032$；若只在 $n = 25$ 个样例上错了 3 个，样本错误率同样是 $0.12$，标准差却约为 $0.065$。同样的点估计，前者可信得多。

### 7.2.2. 估计的偏差与方差

估计量 $\operatorname{error}_S(h)$ 的偏差是 $\mathbb{E}[\operatorname{error}_S(h)] - \operatorname{error}_{\mathcal{D}}(h)$。上面的无偏性要求 $h$ 与 $S$ 独立。如果 $S$ 是训练集，$h$ 正是为了在 $S$ 上表现好而选出的，$\operatorname{error}_S(h)$ 就是有偏的，而且偏向乐观，模型越复杂、越**过拟合**，偏差越大。由此得到评估的两条基本纪律：不要把训练集上的结果报告为测试结果；不要在测试集上调参或选择模型（那样测试集就变成了训练的一部分）。

即使估计无偏，单次的 $\operatorname{error}_S(h)$ 仍可能与 $\operatorname{error}_{\mathcal{D}}(h)$ 相差不少（例 7.2.1 中标准差为 3.2% 与 6.5%）。在无偏的估计中，应选择方差最小的；对错误率而言，就是用尽可能多的独立测试样例。

### 7.2.3. 错误率的置信区间

$p$ 的 $N\%$ **置信区间**是一个以 $N\%$ 的概率包含 $p$ 的随机区间，$N\%$ 称为**置信水平**。它描述估计的不确定性：区间以点估计为中心，宽度取决于估计的方差。直接由二项分布求区间比较麻烦，而正态分布的区间很容易求：若 $Y \sim \mathcal{N}(\mu, \sigma^2)$，则 $Y$ 以 $N\%$ 的概率落在 $\mu \pm z_N\sigma$ 中，其中 $z_N$ 是标准正态分布的双侧分位数：

| 置信水平 $N\%$ | 50% | 68% | 80% | 90% | 95% | 98% | 99% |
|---|---|---|---|---|---|---|---|
| $z_N$ | 0.67 | 1.00 | 1.28 | 1.64 | 1.96 | 2.33 | 2.58 |

由 **de Moivre–Laplace 中心极限定理**，$n$ 较大时 $\mathrm{Bin}(n, p)$ 可以用**正态分布**很好地近似（经验法则：$n \ge 30$ 且 $np(1-p) \ge 5$）。于是：

**命题 7.2.1** 设测试样本 $S$ 含 $n$ 个独立抽取、与 $h$ 独立的样例，$h$ 在其上错了 $r$ 个，且 $n$ 足够大。则 $\operatorname{error}_{\mathcal{D}}(h)$ 的近似 $N\%$ 置信区间为

$$
\operatorname{error}_S(h) \pm z_N\sqrt{\frac{\operatorname{error}_S(h)\big(1 - \operatorname{error}_S(h)\big)}{n}} .
$$

例 7.2.1 中，$n = 100$ 时 95% 置信区间为 $0.12 \pm 1.96 \times 0.032 = [0.056, 0.184]$。这就是 [3.2.4](/3.2.4) 中 Bernoulli 比例的 Wald 区间；那里也说明了它在 $n$ 小或 $p$ 接近 0、1 时覆盖率不足，甚至延伸到 $0$ 以下，此时应改用 Wilson 得分区间：

```python
from math import sqrt
from statistics import NormalDist

z = NormalDist().inv_cdf


def wald(r, n, level=0.95):
    """Normal-approximation interval error_S +- z * sqrt(error_S (1 - error_S) / n)."""
    e = r / n
    h = z(0.5 + level / 2) * sqrt(e * (1 - e) / n)
    return e - h, e + h


def wilson(r, n, level=0.95):
    """Wilson score interval; better for small n or error rates near 0 or 1."""
    e, zz = r / n, z(0.5 + level / 2)
    center = (e + zz**2 / (2 * n)) / (1 + zz**2 / n)
    half = zz * sqrt(e * (1 - e) / n + zz**2 / (4 * n**2)) / (1 + zz**2 / n)
    return center - half, center + half


for r, n in [(12, 100), (3, 25), (1, 40)]:
    lo, hi = wald(r, n)
    wlo, whi = wilson(r, n)
    print(f"r={r:2d} n={n:3d}  error_S={r / n:.3f}  Wald [{lo:.3f}, {hi:.3f}]  Wilson [{wlo:.3f}, {whi:.3f}]")
```

```text
r=12 n=100  error_S=0.120  Wald [0.056, 0.184]  Wilson [0.070, 0.198]
r= 3 n= 25  error_S=0.120  Wald [-0.007, 0.247]  Wilson [0.042, 0.300]
r= 1 n= 40  error_S=0.025  Wald [-0.023, 0.073]  Wilson [0.004, 0.129]
```

置信区间的含义是：如果反复抽取测试集并按同样的方法构造区间，大约 $N\%$ 的区间会包含真实错误率。下图模拟了这一点；区间的半宽与 $\sqrt n$ 成反比，测试集扩大 4 倍，区间才缩小一半。

![左：真实错误率为 0.2 时，100 个大小为 50 的测试集各自给出的 95% Wald 区间，红色的 8 个没有覆盖真实错误率（名义上应约为 5 个，n 较小时正态近似的覆盖率略低）；右：95% 区间的半宽随测试集大小 n 的变化，虚线为 0.05](./plots/error-rate-intervals.py)

**例 7.2.2** 已知某假设的真实错误率在 $0.2$ 到 $0.6$ 之间。要使 95% 双侧置信区间的宽度小于 $0.1$，至少需要多少个测试样例？半宽 $1.96\sqrt{p(1-p)/n} \le 0.05$，而 $p(1-p)$ 在 $[0.2, 0.6]$ 上的最大值在 $p = 0.5$ 处取得，为 $0.25$，所以 $n \ge (1.96/0.05)^2 \times 0.25 \approx 384.2$，至少需要 385 个样例。

### 7.2.4. 单侧置信区间

有时只关心错误率不超过多少，即上界。由正态分布的对称性，若 $[L, U]$ 是置信水平为 $100(1 - \alpha)\%$ 的双侧区间，则 $(-\infty, U]$ 是置信水平为 $100(1 - \alpha/2)\%$ 的单侧区间：双侧 95% 区间的上端 $\mu + 1.96\sigma$ 是 97.5% 的单侧上界；95% 的单侧上界则是 $\mu + 1.645\sigma$，对应 90% 双侧区间的上端。

### 7.2.5. 推导置信区间的一般方法

上面的推导可以概括成一般的步骤，适用于许多其他问题：

1. 确定要估计的参数 $p$，如 $\operatorname{error}_{\mathcal{D}}(h)$；
2. 选择估计量 $Y$，如 $\operatorname{error}_S(h)$，最好是方差尽可能小的无偏估计；
3. 确定 $Y$ 的分布，包括均值与方差；
4. 由分布求出 $N\%$ 置信区间 $[L, U]$（可以有 $L = -\infty$ 或 $U = \infty$），例如对正态分布查 $z_N$。

中心极限定理使第 3 步大为简化：若 $Y_1, \dots, Y_n$ 独立同分布，均值为 $\mu$，方差 $\sigma^2$ 有限，则不论 $Y_i$ 是什么分布，样本均值 $\bar Y$ 都近似服从 $\mathcal{N}(\mu, \sigma^2/n)$，标准化后近似服从标准正态分布。机器学习中的大多数评价指标（错误率、平均损失）都是某种平均，所以都可以这样构造近似的置信区间；不是平均的指标（如 AUC、F1）可以用**自助法**（[3.5.7](/3.5.7)）构造区间。

## 7.3. 比较两个假设

### 7.3.1. 错误率之差

设 $h_1$ 在含 $n_1$ 个独立样例的样本 $S_1$ 上测试，$h_2$ 在含 $n_2$ 个样例的独立样本 $S_2$ 上测试。要估计的参数是真实错误率之差

$$
d = \operatorname{error}_{\mathcal{D}}(h_1) - \operatorname{error}_{\mathcal{D}}(h_2),
$$
无偏估计量是 $\hat d = \operatorname{error}_{S_1}(h_1) - \operatorname{error}_{S_2}(h_2)$。两个样本错误率都近似服从正态分布且相互独立，所以 $\hat d$ 也近似服从正态分布，均值为 $d$，方差是两个方差之和：

$$
\sigma_{\hat d}^2 \approx \frac{\operatorname{error}_{S_1}(h_1)\big(1 - \operatorname{error}_{S_1}(h_1)\big)}{n_1} + \frac{\operatorname{error}_{S_2}(h_2)\big(1 - \operatorname{error}_{S_2}(h_2)\big)}{n_2} .
$$
$d$ 的近似 $N\%$ 置信区间为 $\hat d \pm z_N\sigma_{\hat d}$。

### 7.3.2. 单侧检验

现在问：观察到 $\hat d > 0$，$\operatorname{error}_{\mathcal{D}}(h_1) > \operatorname{error}_{\mathcal{D}}(h_2)$（即 $h_2$ 更好）的把握有多大？这是一个**单侧检验**：$d > 0$ 的置信度就是使单侧区间 $(0, \infty)$ 恰好包含 $d$ 的置信水平，即 $\Phi(\hat d/\sigma_{\hat d})$，其中 $\Phi$ 是标准正态分布函数。用**假设检验**的语言，这是检验**原假设** $d \le 0$ 的 z 检验，**p 值**为 $1 - \Phi(\hat d/\sigma_{\hat d})$。

**例 7.3.1** $n_1 = n_2 = 100$，$\operatorname{error}_{S_1}(h_1) = 0.30$，$\operatorname{error}_{S_2}(h_2) = 0.20$，则 $\hat d = 0.10$，

$$
\sigma_{\hat d} \approx \sqrt{\frac{0.3 \times 0.7}{100} + \frac{0.2 \times 0.8}{100}} \approx 0.061,\qquad z = \frac{0.10}{0.061} \approx 1.64 .
$$
$z = 1.64$ 对应 90% 的双侧置信水平，即 95% 的单侧置信水平：我们有 95% 的把握认为 $h_2$ 的真实错误率更低（p 值约为 0.05）。

**例 7.3.2** 错误率不变，但 $n_1 = n_2 = 30$。则 $\sigma_{\hat d} \approx 0.111$，$z \approx 0.90$，$\Phi(0.90) \approx 0.82$：单侧置信度只有约 82%（对应约 63% 的双侧置信水平），远不足以下结论。同样 10 个百分点的差距，测试集太小就无法区分。

### 7.3.3. 同一测试集上的比较：McNemar 检验

上面假设 $S_1, S_2$ 独立。实践中两个分类器更常在同一个测试集上比较，这时两个样本错误率正相关，上面的方差公式高估了 $\hat d$ 的方差，检验偏于保守。更合适的是只看两个分类器意见不同的样例。

**定义 7.3.1（McNemar 检验）** 在同一个含 $n$ 个样例的测试集上，记 $n_{01}$ 为 $h_1$ 分对而 $h_2$ 分错的样例数，$n_{10}$ 为 $h_1$ 分错而 $h_2$ 分对的样例数。在两者错误率相同的原假设下，每个意见不同的样例落入两类的概率各为 $1/2$。**McNemar 检验**用统计量

$$
\chi^2 = \frac{(\lvert n_{01} - n_{10}\rvert - 1)^2}{n_{01} + n_{10}},
$$
它在原假设下近似服从自由度为 1 的**卡方分布**（$-1$ 是连续性校正）；$n_{01} + n_{10}$ 较小时，改用 $\mathrm{Bin}(n_{01} + n_{10}, 1/2)$ 的精确检验。

两个分类器都分对或都分错的样例不提供关于差异的信息，所以不进入统计量。Dietterich（1998）的模拟表明，只能训练一次时（例如训练很昂贵），McNemar 检验的第一类错误概率接近名义水平，是比较两个分类器的好选择。

## 7.4. 比较学习算法

### 7.4.1. 问题

比较两个假设之外，我们更常想比较两个学习算法 $L_A$ 与 $L_B$："一般来说"哪个更好？理想的量是在所有按 $\mathcal{D}$ 抽取的、大小为 $n$ 的训练集 $S$ 上平均的差异

$$
\mathbb{E}_{S \sim \mathcal{D}^n}\Big[\operatorname{error}_{\mathcal{D}}\big(L_A(S)\big) - \operatorname{error}_{\mathcal{D}}\big(L_B(S)\big)\Big],
$$
其中 $L(S)$ 是算法 $L$ 在训练集 $S$ 上输出的假设。实际上只有一个固定的有限数据集 $D_0$。最简单的做法是把 $D_0$ 分成训练集 $S_0$ 与测试集 $T_0$，计算 $\operatorname{error}_{T_0}(L_A(S_0)) - \operatorname{error}_{T_0}(L_B(S_0))$；把这一过程重复多次再求平均会更好。每次两个算法都在同样的训练集上训练、同样的测试集上测试，这样的比较是配对的（paired test），可以消去由数据划分带来的差异。

### 7.4.2. k 折交叉验证与配对 t 检验

**算法 7.4.1（用 k 折交叉验证比较两个学习算法）**

1. 把 $D_0$ 随机分成 $k$ 个大小相同、互不相交的子集 $T_1, \dots, T_k$，每个子集至少含 30 个样例；
2. 对 $i = 1, \dots, k$：以 $T_i$ 为测试集、其余数据 $S_i = D_0 \setminus T_i$ 为训练集，计算 $\delta_i = \operatorname{error}_{T_i}(L_A(S_i)) - \operatorname{error}_{T_i}(L_B(S_i))$；
3. 输出 $\bar\delta = \frac1k\sum_i\delta_i$，以及 $\bar\delta$ 的近似 $N\%$ 置信区间 $\bar\delta \pm t_{k-1}\,s_{\bar\delta}$，其中

   $$
   s_{\bar\delta} = \sqrt{\frac{1}{k(k-1)}\sum_{i=1}^k(\delta_i - \bar\delta)^2},
   $$
   $t_{k-1}$ 是自由度为 $k - 1$ 的 **t 分布**的相应双侧分位数。

这里用 t 分布而不用正态分布，是因为只有 $k$（通常为 10）个差值，样本方差本身的不确定性不能忽略。这正是配对 t 检验：

**定义 7.4.1（配对 t 检验）** 设两个模型在 $n$ 对配对的实验（同样的训练集与测试集）上的结果为 $x_{1i}, x_{2i}$，差值 $d_i = x_{1i} - x_{2i}$ 独立且来自正态分布。**配对 t 检验**以

$$
t = \frac{\bar x_1 - \bar x_2}{\sqrt{\sum_{i=1}^n(d_i - \bar d)^2/\big(n(n-1)\big)}}
$$
为检验统计量，在两者没有差异的原假设下 $t$ 服从自由度为 $n - 1$ 的 t 分布。

它就是对差值做的单样本 t 检验（[3.2.5](/3.2.5) 中成对数据的情形）。如果两组实验不配对（例如各自独立地重复实验 $n_1$ 次和 $n_2$ 次），样本量与方差都可能不等，则用 **Welch t 检验**：

$$
t = \frac{\bar x_1 - \bar x_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}},\qquad
\mathrm{df} = \frac{\big(s_1^2/n_1 + s_2^2/n_2\big)^2}{\dfrac{(s_1^2/n_1)^2}{n_1 - 1} + \dfrac{(s_2^2/n_2)^2}{n_2 - 1}},
$$
其中 $s_j^2 = \frac{1}{n_j - 1}\sum_i(x_{ji} - \bar x_j)^2$ 是样本方差。配对时差值消去了各次划分之间的差异，检验的功效高得多，所以只要能配对就应配对。

k 折交叉验证的配对 t 检验有一个缺陷：各折的测试集互不相交，但训练集大量重叠（任意两折的训练集共享 $(k-2)/(k-1)$ 的数据），$\delta_i$ 并不独立，而是正相关的。于是 $s_{\bar\delta}$ 低估了真实的变异，检验过于乐观，第一类错误的概率高于名义水平（Dietterich，1998）。Nadeau 与 Bengio（2003）提出校正：把方差的估计 $\frac1k s_\delta^2$ 换成 $\big(\frac1k + \frac{n_{\mathrm{test}}}{n_{\mathrm{train}}}\big)s_\delta^2$，其中 $s_\delta^2$ 是 $\delta_i$ 的样本方差，对 k 折交叉验证 $n_{\mathrm{test}}/n_{\mathrm{train}} = 1/(k-1)$。尽管如此，k 折交叉验证的比较仍然比不做任何比较要好。

另一种做法是每次随机抽取一个测试集（至少 30 个样例），其余作训练集，重复多次；但数据集不够大时，这些测试集也彼此重叠、不独立，问题更严重。

### 7.4.3. 5×2 交叉验证 t 检验

Dietterich（1998）比较了多种检验的第一类错误概率，提出 5×2 交叉验证（5×2cv）配对 t 检验：

**算法 7.4.2（5×2 交叉验证 t 检验）** 重复 5 次（$i = 1, \dots, 5$）：把数据随机对半分成 $S_1, S_2$，先在 $S_1$ 上训练、$S_2$ 上测试，再交换，得到两个错误率之差 $p_i^{(1)}, p_i^{(2)}$；记 $\bar p_i = (p_i^{(1)} + p_i^{(2)})/2$，$s_i^2 = (p_i^{(1)} - \bar p_i)^2 + (p_i^{(2)} - \bar p_i)^2$。统计量

$$
\tilde t = \frac{p_1^{(1)}}{\sqrt{\frac15\sum_{i=1}^5 s_i^2}}
$$
在两个算法没有差异的原假设下近似服从自由度为 5 的 t 分布。

二折交叉验证的两个训练集不重叠，所以每次重复内部的两个差值近似独立；重复 5 次是为了更稳定地估计方差。Dietterich 的模拟中，5×2cv t 检验与 McNemar 检验的第一类错误概率都接近名义水平，而重复随机划分的 t 检验与 10 折交叉验证的 t 检验都偏高。分子只用了 $p_1^{(1)}$，结果依赖于第一次划分；Alpaydin（1999）用全部 10 个差值构造合并的 F 统计量

$$
F = \frac{\sum_{i=1}^5\sum_{j=1}^2\big(p_i^{(j)}\big)^2}{2\sum_{i=1}^5 s_i^2},
$$
在原假设下近似服从 $F_{10,5}$，更稳定、功效也更高。

### 7.4.4. 例子

下面在同一个数据集上比较 logistic 回归与随机森林（[4.6.6](/4.6.6)），依次做 10 折交叉验证配对 t 检验、Nadeau–Bengio 校正、5×2cv t 检验与 McNemar 检验：

```python
import numpy as np
from scipy import stats
from sklearn.base import clone
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, StratifiedKFold, train_test_split

X, y = make_classification(n_samples=1000, n_features=20, n_informative=6,
                           flip_y=0.05, random_state=1)
A = LogisticRegression(max_iter=1000)
B = RandomForestClassifier(n_estimators=200, random_state=0)


def error(model, Xtr, ytr, Xte, yte):
    return np.mean(clone(model).fit(Xtr, ytr).predict(Xte) != yte)


# 1. k-fold cross-validated paired t-test (same folds for both algorithms)
k = 10
delta = np.array([error(A, X[tr], y[tr], X[te], y[te]) - error(B, X[tr], y[tr], X[te], y[te])
                  for tr, te in StratifiedKFold(k, shuffle=True, random_state=0).split(X, y)])
t = delta.mean() / (delta.std(ddof=1) / np.sqrt(k))
print(f"mean difference {delta.mean():.4f}; paired t = {t:.2f}, p = {2 * stats.t.sf(abs(t), k - 1):.4f}")
# Nadeau-Bengio correction for the overlap of training sets
t_c = delta.mean() / np.sqrt((1 / k + 1 / (k - 1)) * delta.var(ddof=1))
print(f"corrected t = {t_c:.2f}, p = {2 * stats.t.sf(abs(t_c), k - 1):.4f}")

# 2. Dietterich's 5x2cv paired t-test
p1, s2 = None, []
for i in range(5):
    folds = list(KFold(2, shuffle=True, random_state=i).split(X))
    p = [error(A, X[a], y[a], X[b], y[b]) - error(B, X[a], y[a], X[b], y[b]) for a, b in folds]
    p1 = p[0] if p1 is None else p1
    s2.append((p[0] - np.mean(p)) ** 2 + (p[1] - np.mean(p)) ** 2)
t52 = p1 / np.sqrt(np.mean(s2))
print(f"5x2cv t = {t52:.2f}, p = {2 * stats.t.sf(abs(t52), 5):.4f}")

# 3. McNemar's test on a single test set
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
ra = clone(A).fit(Xtr, ytr).predict(Xte) == yte
rb = clone(B).fit(Xtr, ytr).predict(Xte) == yte
n01, n10 = int(np.sum(ra & ~rb)), int(np.sum(~ra & rb))
chi2 = (abs(n01 - n10) - 1) ** 2 / (n01 + n10)
print(f"McNemar: n01={n01}, n10={n10}, chi2 = {chi2:.2f}, p = {stats.chi2.sf(chi2, 1):.4f}")
```

```text
mean difference 0.0260; paired t = 2.57, p = 0.0304
corrected t = 1.77, p = 0.1112
5x2cv t = 1.08, p = 0.3312
McNemar: n01=9, n10=13, chi2 = 0.41, p = 0.5224
```

随机森林在 10 折交叉验证中平均少错 2.6 个百分点。未经校正的配对 t 检验在 $0.05$ 水平上认为差异显著，而校正后的检验、5×2cv 检验和 McNemar 检验都不显著：未校正的检验忽略了训练集之间的重叠，夸大了证据。在报告"算法 A 优于算法 B"之前，应当选用第一类错误受控的检验，并同时报告差异的大小与置信区间。

### 7.4.5. 小样本与大样本、多个数据集

z 检验与 t 检验的选择取决于随机变量的样本个数：

| | z 检验（正态近似） | t 检验 |
|---|---|---|
| 随机变量 | 每个测试样例分对与否 | 每次实验（每一折、每次重复）的指标 |
| 样本个数 | 多（测试样例数，至少 30） | 少（如 10 折、5×2） |
| 典型用途 | 单次评测：一个测试集上的置信区间、两个假设的比较 | 多次评测：重复实验、交叉验证 |
| 依据 | 中心极限定理 | 差值近似正态，方差需要估计 |

在多个数据集上比较算法时，各数据集的错误率不可比，也不服从同一个正态分布。Demšar（2006）建议：比较两个算法用 **Wilcoxon 符号秩检验**（对每个数据集上的差异排秩）；比较多个算法用 Friedman 检验（对每个数据集上各算法的表现排秩），显著时再做事后两两比较（如 Nemenyi 检验）。同时比较许多对算法时，还要注意多重比较的问题。

## 小结

| 问题 | 方法 | 要点 |
|---|---|---|
| 1. 假设的准确率能否代表未见实例上的效果 | 二项分布 → 正态近似 → 置信区间 | $\operatorname{error}_S(h) \pm z_N\sqrt{\operatorname{error}_S(h)(1-\operatorname{error}_S(h))/n}$；测试集必须独立于 $h$；小样本用 Wilson 区间 |
| 2. 一般情况下 $h_1$ 比 $h_2$ 好的可能性 | 错误率之差的正态近似，单侧置信度 | 独立测试集：$\hat d \pm z_N\sigma_{\hat d}$；同一测试集：McNemar 检验 |
| 3. 怎样用有限数据比较学习算法 | k 折交叉验证 + 配对 t 检验，t 分布的置信区间 | 训练集重叠使检验偏乐观：用校正的 t、5×2cv t 或 F 检验；多个数据集用秩检验 |

评估一个学习系统的基本原则是：测试数据独立于训练与模型选择；重复实验；配对比较；用统计显著性检验判断差异，并报告置信区间。
