---
title: 多参数模型
description: 感兴趣参数与讨厌参数，联合、条件与边缘后验；带 Dirichlet 先验的多项模型；均值与方差都未知的正态模型在无信息先验与正态–逆卡方先验下的后验、边际似然与后验预测分布；用模拟求解 Behrens–Fisher 问题；带正态–逆 Wishart 先验与无信息先验的多元正态模型。
source_hash: 3462f7d2e826
---

几乎每个实际的模型都有不止一个未知参数，而一个问题通常只涉及其中一部分。正态样本有均值和方差，但我们可能只关心均值；有 $k$ 个答案类别的调查有 $k-1$ 个自由的概率，但我们可能只关心其中两个之差。贝叶斯对这种情形的回答在原则上很简单：写出所有未知量的联合后验，把不感兴趣的量积分掉。本章先阐述这一原则（§3.1），再用它处理三个经典的多参数模型：带 Dirichlet 先验的多项模型（§3.2）；均值与方差都未知的正态模型，先在无信息先验下（§3.3），再在其共轭先验下（§3.4），并以两个正态均值的比较作为应用（§3.5）；以及多元正态模型（§3.6）。这些模型推广了 [3.7.2](/3.7.2) 的单参数模型并沿用其中的分布，首先是**尺度逆卡方分布**（定义 2.4.1）。首次出现于此的分布，连同它们在不同文献与软件中的参数化，汇总在 [3.7.4](/3.7.4)。这类精确结果只对共轭模型成立；一般的模型需要 [3.7.5](/3.7.5) 的模拟方法，而本章的分解正是其模板。

## 3.1. 讨厌参数与边缘后验

把参数分为 $\theta=(\theta_1,\theta_2)$，其中每一部分本身可以是向量。

**定义 3.1.1（感兴趣参数与讨厌参数）** 若只需要对 $\theta_1$ 作推断，则 $\theta_1$ 是感兴趣的参数，$\theta_2$ 是**讨厌参数**：它必须出现在模型中，模型才能描述数据，但它不是分析的目标。

对均值与方差都未知的正态数据 $y_i\mid\mu,\sigma^2\sim\mathcal{N}(\mu,\sigma^2)$，兴趣通常集中在 $\mu$ 上，$\sigma^2$ 是讨厌参数。多参数模型贝叶斯推断的一般框架是

$$
\begin{aligned}
\text{先验}\qquad&p(\theta_1,\theta_2),\\
\text{联合后验}\qquad&p(\theta_1,\theta_2\mid y)\propto p(y\mid\theta_1,\theta_2)\,p(\theta_1,\theta_2),\\
\text{边缘后验}\qquad&p(\theta_1\mid y)=\int p(\theta_1,\theta_2\mid y)\,\mathrm{d}\theta_2=\int p(\theta_1\mid\theta_2,y)\,p(\theta_2\mid y)\,\mathrm{d}\theta_2.
\end{aligned}
$$
感兴趣参数的边缘后验通过对讨厌参数取平均得到。最后一种形式说得更多：$p(\theta_1\mid y)$ 是条件后验 $p(\theta_1\mid\theta_2,y)$ 的混合，讨厌参数的每个取值对应一个，权重为讨厌参数的边缘后验 $p(\theta_2\mid y)$。频率学派方法消除讨厌参数的办法是：以某个统计量为条件、代入估计值，或寻找分布不含它们的**枢轴量**；贝叶斯方法只有一条规则，即积分，它总是适用。

混合的形式直接转化为模拟，即 [3.7.5](/3.7.5) 要发展的 **Monte Carlo 方法**。联合后验分解为

$$
p(\theta_1,\theta_2\mid y)=p(\theta_1\mid\theta_2,y)\,p(\theta_2\mid y),
$$
所以从它抽样分两步：先从边缘后验 $p(\theta_2\mid y)$ 抽 $\theta_2$，再在该值处从条件后验 $p(\theta_1\mid\theta_2,y)$ 抽 $\theta_1$。重复下去，得到来自联合后验的抽样 $(\theta_1^s,\theta_2^s)$，$s=1,\dots,S$；只保留 $\theta_1^s$，就得到来自边缘后验 $p(\theta_1\mid y)$ 的抽样，无需计算积分。在共轭模型中，两个因子都是标准分布。因子 $p(\theta_2\mid y)$ 本身常常不用积分就可由

$$
p(\theta_2\mid y)=\frac{p(\theta_1,\theta_2\mid y)}{p(\theta_1\mid\theta_2,y)}
$$
求得，该式对 $\theta_1$ 的每个取值都成立，因此所有含 $\theta_1$ 的因子必然抵消，这与 [3.7.2](/3.7.2) 中得出负二项先验预测分布的技巧相同。

## 3.2. 多项模型与 Dirichlet 先验

### 3.2.1. 模型

一份文档可以用词汇表中每个词在其中出现的次数来概括，而不管词的顺序：这就是**词袋**表示。若文档中的词是从含 $k$ 个词、概率为 $\theta_1,\dots,\theta_k$ 的词汇表中独立抽取的，则计数向量 $\boldsymbol{y}=(y_1,\dots,y_k)$，$\sum_jy_j=n$，服从**多项分布** $\mathrm{Mult}(n,\boldsymbol{\theta})$；文本的主题模型就是由这样的多项分量构成的。更一般地，多项模型描述 $n$ 个独立观测，每个落入 $k$ 个类别之一。它的似然为

$$
p(\boldsymbol{y}\mid\boldsymbol{\theta})\propto\prod_{j=1}^k\theta_j^{y_j},\qquad\boldsymbol{\theta}\in\Delta_k=\Big\{\boldsymbol{\theta}\colon\theta_j\ge0,\ \sum_{j=1}^k\theta_j=1\Big\},
$$
这是二项似然 $\theta^y(1-\theta)^{n-y}$（$k=2$ 的情形）的推广。参数有 $k-1$ 个自由分量。正如 Beta 族与二项分布共轭（[3.7.1](/3.7.1)），它的多元类似物与多项分布共轭。

### 3.2.2. Dirichlet 分布

**定义 3.2.1（Dirichlet 分布）** 设 $\boldsymbol{\alpha}=(\alpha_1,\dots,\alpha_k)$，所有 $\alpha_j>0$，$\alpha_0=\sum_{j=1}^k\alpha_j$。**Dirichlet 分布** $\mathrm{Dir}(\boldsymbol{\alpha})$ 是单纯形 $\Delta_k$ 上的分布，其密度为

$$
p(\boldsymbol{\theta}\mid\boldsymbol{\alpha})=\frac{\Gamma(\alpha_0)}{\Gamma(\alpha_1)\cdots\Gamma(\alpha_k)}\prod_{j=1}^k\theta_j^{\alpha_j-1},\qquad\boldsymbol{\theta}\in\Delta_k,
$$
相对于 $(\theta_1,\dots,\theta_{k-1})$ 上的 Lebesgue 测度，其中 $\theta_k=1-\sum_{j<k}\theta_j$。

当 $k=2$ 时它就是 **Beta 分布**：$(\theta_1,1-\theta_1)\sim\mathrm{Dir}(\alpha_1,\alpha_2)$ 当且仅当 $\theta_1\sim\mathrm{Beta}(\alpha_1,\alpha_2)$。矩为

$$
\mathbb{E}\theta_j=\frac{\alpha_j}{\alpha_0},\qquad\operatorname{Var}\theta_j=\frac{\alpha_j(\alpha_0-\alpha_j)}{\alpha_0^2(\alpha_0+1)},\qquad\operatorname{Cov}(\theta_i,\theta_j)=-\frac{\alpha_i\alpha_j}{\alpha_0^2(\alpha_0+1)}\quad(i\ne j),
$$
并且若所有 $\alpha_j>1$，则众数为 $\theta_j=\frac{\alpha_j-1}{\alpha_0-k}$。协方差为负，因为各分量之和必须为一。均值向量 $\boldsymbol{\alpha}/\alpha_0$ 给出位置，总和 $\alpha_0$ 给出集中程度：$\alpha_0$ 越大，所有方差越小。

**命题 3.2.1（Gamma 表示与合并）** 设 $G_1,\dots,G_k$ 相互独立，$G_j\sim\Gamma(\alpha_j,1)$，$G=\sum_jG_j$。则 $\boldsymbol{\theta}=(G_1/G,\dots,G_k/G)\sim\mathrm{Dir}(\boldsymbol{\alpha})$，且与 $G\sim\Gamma(\alpha_0,1)$ 独立。于是若 $\boldsymbol{\theta}\sim\mathrm{Dir}(\boldsymbol{\alpha})$：

1. 合并类别即把它们的参数相加：$(\theta_1+\theta_2,\theta_3,\dots,\theta_k)\sim\mathrm{Dir}(\alpha_1+\alpha_2,\alpha_3,\dots,\alpha_k)$，一般地，$\boldsymbol{\theta}$ 在类别的任一划分的各块上的和服从参数为相应和的 Dirichlet 分布；
2. 每个分量都是 Beta：$\theta_j\sim\mathrm{Beta}(\alpha_j,\alpha_0-\alpha_j)$。

**证明** $(G_1,\dots,G_k)$ 的联合密度为 $\prod_j\frac{1}{\Gamma(\alpha_j)}g_j^{\alpha_j-1}\mathrm{e}^{-g_j}$。作变量替换 $(\theta_1,\dots,\theta_{k-1},G)$，$g_j=G\theta_j$（$\theta_k=1-\sum_{j<k}\theta_j$）；Jacobi 行列式为 $G^{k-1}$。新的密度为

$$
\prod_{j=1}^k\frac{(G\theta_j)^{\alpha_j-1}}{\Gamma(\alpha_j)}\,\mathrm{e}^{-G}\,G^{k-1}=\frac{\prod_j\theta_j^{\alpha_j-1}}{\prod_j\Gamma(\alpha_j)}\,G^{\alpha_0-1}\mathrm{e}^{-G},
$$
它分解为 $\boldsymbol{\theta}$ 的 $\mathrm{Dir}(\boldsymbol{\alpha})$ 密度与 $G$ 的 $\Gamma(\alpha_0,1)$ 密度之积。对于合并的性质，$G_1+G_2\sim\Gamma(\alpha_1+\alpha_2,1)$ 与 $G_3,\dots,G_k$ 独立，并且 $\theta_1+\theta_2=(G_1+G_2)/G$；对 $k-1$ 个变量 $G_1+G_2,G_3,\dots,G_k$ 用第一部分即可。合并除 $j$ 之外的所有类别，得 $(\theta_j,1-\theta_j)\sim\mathrm{Dir}(\alpha_j,\alpha_0-\alpha_j)$。$\square$

这一表示也是从 Dirichlet 分布模拟抽样的标准方法。

### 3.2.3. 共轭后验

取先验 $\boldsymbol{\theta}\sim\mathrm{Dir}(\boldsymbol{\alpha})$，$p(\boldsymbol{\theta})\propto\prod_j\theta_j^{\alpha_j-1}$，则

$$
p(\boldsymbol{\theta}\mid\boldsymbol{y})\propto\prod_{j=1}^k\theta_j^{\alpha_j+y_j-1},\qquad\boldsymbol{\theta}\mid\boldsymbol{y}\sim\mathrm{Dir}(\boldsymbol{\alpha}+\boldsymbol{y}).
$$
与二项模型一样，**超参数**起先验计数的作用。相对于均匀基准 $\mathrm{Dir}(1,\dots,1)$，先验 $\mathrm{Dir}(\boldsymbol{\alpha})$ 相当于 $\sum_j\alpha_j-k$ 个观测，其中 $\alpha_j-1$ 个落在类别 $j$；相对于广义基准 $\mathrm{Dir}(0,\dots,0)$，它相当于 $\alpha_0$ 个观测，$\alpha_j$ 个在类别 $j$。后验均值

$$
\mathbb{E}(\theta_j\mid\boldsymbol{y})=\frac{\alpha_j+y_j}{\alpha_0+n}=\frac{n}{\alpha_0+n}\cdot\frac{y_j}{n}+\frac{\alpha_0}{\alpha_0+n}\cdot\frac{\alpha_j}{\alpha_0}
$$
是观测比例与先验均值的加权平均，权重为 $n$ 与 $\alpha_0$。在机器学习中，所有 $\alpha_j=1$ 的这个估计称为 Laplace 平滑（[4.6.3](/4.6.3)）。

*合并类别。* 由命题 3.2.1，单个概率的边缘后验为 $\theta_j\mid\boldsymbol{y}\sim\mathrm{Beta}(\alpha_j+y_j,\alpha_0-\alpha_j+n-y_j)$。这恰好就是只区分“类别 $j$”与“其他任何类别”、先验为 $\mathrm{Beta}(\alpha_j,\alpha_0-\alpha_j)$ 的二项分析的后验：不论在分析之前还是之后粗化类别，得到的答案相同。类似地，和 $\theta_1+\theta_2$ 的边缘后验也是 Beta。对比 $\theta_1-\theta_2$ 或比值 $\theta_1/\theta_2$ 则不是 Beta，需要通过模拟 $\boldsymbol{\theta}$ 来处理。

*后验预测分布。* 对一个新观测 $\tilde y$，由**全期望公式**，

$$
\mathbb{P}(\tilde y=j\mid\boldsymbol{y})=\mathbb{E}(\theta_j\mid\boldsymbol{y})=\frac{\alpha_j+y_j}{\alpha_0+n},
$$
这是 Laplace 继承律 $\frac{y+1}{n+2}$（[3.7.1](/3.7.1)）的多项形式。$m$ 个新观测的计数服从参数为 $m$ 与 $\boldsymbol{\alpha}+\boldsymbol{y}$ 的 Dirichlet-多项分布（[3.7.4](/3.7.4)）。

*无信息先验。* 常用的有三种选择：

| 先验 | 理由 | 后验的正常性 |
|---|---|---|
| 所有 $j$ 都有 $\alpha_j=\frac12$ | 多项模型的 **Jeffreys 先验** | 总是正常 |
| 所有 $j$ 都有 $\alpha_j=1$ | 在单纯形 $\Delta_k$ 上均匀 | 总是正常 |
| 所有 $j$ 都有 $\alpha_j=0$ | 在对数比 $\log(\theta_j/\theta_k)$（多元 logit）上平坦 | 仅当每个 $y_j\ge1$ 时正常 |

最后一行推广了 [3.7.2](/3.7.2) 的 $\mathrm{Beta}(0,0)$：在 $\phi_j=\log(\theta_j/\theta_k)$（$j<k$）之下，$(\phi_1,\dots,\phi_{k-1})$ 上的平坦密度对应于 $p(\boldsymbol{\theta})\propto\prod_j\theta_j^{-1}$。当 $k$ 相对于 $n$ 很大时，如词汇表中的词，这些先验远非无害：$\mathrm{Dir}(1,\dots,1)$ 给 $k$ 个类别各加一个先验计数，共 $k$ 个，对罕见的类别来说，这可能压过数据。

**例 3.2.1（症状词）** 在一批仅限于描述症状的四个词的病历集合中，计数为口渴 $y_1=10$、多尿 $y_2=8$、多食 $y_3=15$、体重下降 $y_4=13$，所以 $n=46$。取均匀先验 $\mathrm{Dir}(1,1,1,1)$，后验为 $\mathrm{Dir}(11,9,16,14)$，$\alpha_0+n=50$，后验均值为 $0.22,0.18,0.32,0.28$。“多食”的概率的边缘后验为 $\mathrm{Beta}(16,34)$，$95\%$ 中心后验区间为 $[0.199,0.454]$。“多食”比“口渴”更频繁吗？按命题 3.2.1 从 $\mathrm{Dir}(11,9,16,14)$ 模拟 $\boldsymbol{\theta}$，得 $\mathbb{P}(\theta_3>\theta_1\mid\boldsymbol{y})\approx0.84$，$\theta_3-\theta_1$ 的 $95\%$ 区间为 $[-0.10,0.30]$：数据偏向“多食”，但并不决定性。这几个词中下一个是“多食”的预测概率为 $0.32$。

## 3.3. 无信息先验下的正态模型

### 3.3.1. 位置–尺度 t 记号

正态均值的边缘后验是平移并缩放的 $t$ 分布，我们对它使用如下记号。

**注 3.3.1** 对 $\nu>0$、$\mu\in\mathbb{R}$ 与 $\sigma>0$，若 $(\theta-\mu)/\sigma$ 服从 **t 分布** $t_\nu$（[3.1.4](/3.1.4)），则记 $\theta\sim t_\nu(\mu,\sigma^2)$，即

$$
p(\theta)=\frac{\Gamma(\frac{\nu+1}{2})}{\Gamma(\frac\nu2)\sqrt{\nu\pi}\,\sigma}\Big(1+\frac1\nu\Big(\frac{\theta-\mu}{\sigma}\Big)^2\Big)^{-(\nu+1)/2},
$$
并且 $t_\nu=t_\nu(0,1)$。第二个参数 $\sigma^2$ 是尺度的平方，而不是方差：当 $\nu>2$ 时 $\operatorname{Var}\theta=\frac{\nu}{\nu-2}\sigma^2$。当 $\nu\to\infty$ 时，$t_\nu(\mu,\sigma^2)\to\mathcal{N}(\mu,\sigma^2)$。

### 3.3.2. 联合、条件与边缘后验

设 $y_1,\dots,y_n\mid\mu,\sigma^2\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$，两个参数都未知，记

$$
\bar y=\frac1n\sum_{i=1}^ny_i,\qquad s^2=\frac{1}{n-1}\sum_{i=1}^n(y_i-\bar y)^2.
$$
把 [3.7.2](/3.7.2) 中位置参数与尺度参数的先验结合起来，即在 $\mu$ 与 $\log\sigma$ 上平坦，并假设它们在先验中独立，就得到一个无信息先验：

$$
p(\mu,\sigma^2)\propto(\sigma^2)^{-1}.
$$
每个因子都是在另一个参数已知时对应参数的 **Jeffreys 先验**。（对 $(\mu,\sigma^2)$ 联合应用 Jeffreys 规则 $\lvert\det J\rvert^{1/2}$ 给出的是 $(\sigma^2)^{-3/2}$；独立的版本是标准的选择，因为它的后验重现下面的经典 $t$ 结果。）利用 $\sum_i(y_i-\mu)^2=(n-1)s^2+n(\bar y-\mu)^2$，联合后验为

$$
p(\mu,\sigma^2\mid y)\propto\sigma^{-n-2}\exp\Big(-\frac{1}{2\sigma^2}\sum_{i=1}^n(y_i-\mu)^2\Big)=\sigma^{-n-2}\exp\Big(-\frac{1}{2\sigma^2}\big[(n-1)s^2+n(\bar y-\mu)^2\big]\Big),
$$
它只通过**充分统计量** $(\bar y,s^2)$ 依赖于数据。

**命题 3.3.1** 在先验 $p(\mu,\sigma^2)\propto\sigma^{-2}$ 下，且 $n\ge2$：

1. $\mu\mid\sigma^2,y\sim\mathcal{N}(\bar y,\sigma^2/n)$；
2. $\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(n-1,s^2)$；
3. $\mu\mid y\sim t_{n-1}(\bar y,s^2/n)$，即 $\dfrac{\mu-\bar y}{s/\sqrt n}\;\Big|\;y\sim t_{n-1}$；
4. $\sigma^2\mid\mu,y\sim\mathrm{Inv}\text{-}\chi^2(n,v)$，其中 $v=\frac1n\sum_i(y_i-\mu)^2$。

**证明** (1) 对固定的 $\sigma^2$，联合后验正比于 $\exp\big(-\frac{n}{2\sigma^2}(\mu-\bar y)^2\big)$，这是 $\mu$ 的正态核；这就是 [3.7.2](/3.7.2) 中方差已知时、先验平坦的结果。

(2) 把 $\mu$ 积分掉；Gauss 积分为 $\int\exp\big(-\frac{n}{2\sigma^2}(\bar y-\mu)^2\big)\,\mathrm{d}\mu=\sqrt{2\pi\sigma^2/n}$，所以

$$
p(\sigma^2\mid y)\propto\sigma^{-n-2}\exp\Big(-\frac{(n-1)s^2}{2\sigma^2}\Big)\sqrt{2\pi\sigma^2/n}\propto(\sigma^2)^{-(n+1)/2}\exp\Big(-\frac{(n-1)s^2}{2\sigma^2}\Big),
$$
这是 $\mathrm{Inv}\text{-}\chi^2(n-1,s^2)$ 的核，因为 $(n+1)/2=(n-1)/2+1$。

(3) 把 $\sigma^2$ 积分掉。记 $A=(n-1)s^2+n(\mu-\bar y)^2$，作替换 $z=A/(2\sigma^2)$，$\mathrm{d}\sigma^2=-\frac{A}{2z^2}\,\mathrm{d}z$，

$$
p(\mu\mid y)\propto\int_0^\infty(\sigma^2)^{-(n+2)/2}\exp\Big(-\frac{A}{2\sigma^2}\Big)\,\mathrm{d}\sigma^2\propto A^{-n/2}\int_0^\infty z^{(n-2)/2}\mathrm{e}^{-z}\,\mathrm{d}z\propto\Big[1+\frac{n(\mu-\bar y)^2}{(n-1)s^2}\Big]^{-n/2},
$$
这就是注 3.3.1 中 $\nu+1=n$ 的 $t_{n-1}(\bar y,s^2/n)$ 的核。

(4) 对固定的 $\mu$，联合后验为 $(\sigma^2)^{-(n/2+1)}\exp\big(-\frac{nv}{2\sigma^2}\big)$，与 [3.7.2](/3.7.2) 中均值已知的正态方差相同。$\square$

(1) 与 (2) 给出 §3.1 的分解 $p(\mu,\sigma^2\mid y)=p(\mu\mid\sigma^2,y)\,p(\sigma^2\mid y)$，从而给出模拟方案：先从 $\mathrm{Inv}\text{-}\chi^2(n-1,s^2)$ 抽 $\sigma^2$，即取 $(n-1)s^2/X$，$X\sim\chi^2_{n-1}$，再从 $\mathcal{N}(\bar y,\sigma^2/n)$ 抽 $\mu$。(3) 展示了混合形式的作用：把正态的条件后验对 $\sigma^2$ 的不确定性取平均，产生尾部更重的 $t$ 分布。(1) 与 (4) 是后面章节中 Gibbs 抽样器所用的两个完全条件分布。

### 3.3.3. 与频率学派枢轴量的比较

关于正态均值与方差的经典推断建立在两个枢轴量上（[3.2.4](/3.2.4)）。在 $p(\mu,\sigma^2)\propto\sigma^{-2}$ 下，贝叶斯结果使同样的量具有同样的分布，只是数据与参数的角色互换：

| 量 | 贝叶斯，给定 $y$ | 频率学派，给定 $(\mu,\sigma^2)$ |
|---|---|---|
| $\dfrac{\mu-\bar y}{s/\sqrt n}$ | $t_{n-1}$；$\mu$ 随机，$\bar y$ 与 $s$ 固定 | $t_{n-1}$；$\bar y$ 与 $s$ 随机，$\mu$ 固定 |
| $\dfrac{(n-1)s^2}{\sigma^2}$ | $\chi^2_{n-1}$；$\sigma^2$ 随机 | $\chi^2_{n-1}$；$s^2$ 随机 |

因此 $95\%$ 中心后验区间 $\bar y\pm t_{n-1,0.025}\,s/\sqrt n$ 在数值上与经典的 $t$ **置信区间**一致，后验概率 $\mathbb{P}(\mu>\mu_0\mid y)$ 等于 $H_0\colon\mu\le\mu_0$ 的单侧 $t$ 检验的 **p 值**的补数。解释则不同：可信区间是关于给定观测数据时 $\mu$ 的概率陈述，置信区间则是关于重复抽样下程序的陈述。

新观测的后验预测分布由 $\tilde y=\mu+\varepsilon$ 得到：给定 $\sigma^2$ 与 $y$，$\tilde y\sim\mathcal{N}\big(\bar y,(1+\frac1n)\sigma^2\big)$，如命题 3.3.1 (3) 那样对 $\sigma^2\mid y$ 取平均，得

$$
\tilde y\mid y\sim t_{n-1}\Big(\bar y,\Big(1+\frac1n\Big)s^2\Big),
$$
其中心区间就是新的正态观测的经典预测区间。

## 3.4. 共轭先验下的正态模型

### 3.4.1. 正态–逆卡方族

§3.3 的后验具有这样的结构：“$\sigma^2$ 服从尺度逆卡方分布，给定 $\sigma^2$ 时 $\mu$ 服从方差正比于 $\sigma^2$ 的正态分布”。具有同样结构的先验是共轭的。

**定义 3.4.1（正态–逆卡方分布）** 设 $\mu_0\in\mathbb{R}$，$\kappa_0,\nu_0,\sigma_0^2>0$。若

$$
\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2),\qquad\mu\mid\sigma^2\sim\mathcal{N}(\mu_0,\sigma^2/\kappa_0),
$$
即联合密度为

$$
p(\mu,\sigma^2)\propto\sigma^{-1}(\sigma^2)^{-(\nu_0/2+1)}\exp\Big(-\frac{1}{2\sigma^2}\big[\nu_0\sigma_0^2+\kappa_0(\mu-\mu_0)^2\big]\Big),
$$
则称 $(\mu,\sigma^2)$ 服从**正态–逆卡方分布** $\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_0,\sigma_0^2/\kappa_0;\nu_0,\sigma_0^2)$。

四个超参数的含义如下，都是 [3.7.2](/3.7.2) 中“先验数据”的意义：

| 超参数 | 含义 |
|---|---|
| $\mu_0$ | $\mu$ 的先验均值 |
| $\kappa_0$ | $\mu_0$ 所基于的先验观测数 |
| $\sigma_0^2$ | 抽样方差 $\sigma^2$ 的先验估计 |
| $\nu_0$ | $\sigma_0^2$ 所基于的先验观测数（自由度） |

在这个族里，$\mu$ 与 $\sigma^2$ 在先验中是相依的：给定 $\sigma^2$ 时 $\mu$ 的先验方差为 $\sigma^2/\kappa_0$，正比于抽样方差，就好像 $\mu_0$ 是同一总体中 $\kappa_0$ 个先前观测的均值。当先验信息来自同类的早先数据时这是自然的，但并不总是合适；独立的先验 $\mu\sim\mathcal{N}(\mu_0,\tau_0^2)$，$\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2)$ 不是共轭的（它的条件后验是标准的，但边缘后验不是），要用 [3.7.5](/3.7.5) 的模拟方法处理。

### 3.4.2. 联合后验

**定理 3.4.1** 设 $y_1,\dots,y_n\mid\mu,\sigma^2\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$，$(\mu,\sigma^2)\sim\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_0,\sigma_0^2/\kappa_0;\nu_0,\sigma_0^2)$。则

$$
(\mu,\sigma^2)\mid y\sim\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_n,\sigma_n^2/\kappa_n;\nu_n,\sigma_n^2),
$$
其中

$$
\begin{aligned}
\mu_n&=\frac{\kappa_0}{\kappa_0+n}\mu_0+\frac{n}{\kappa_0+n}\bar y,\qquad\kappa_n=\kappa_0+n,\qquad\nu_n=\nu_0+n,\\
\nu_n\sigma_n^2&=\nu_0\sigma_0^2+(n-1)s^2+\frac{\kappa_0n}{\kappa_0+n}(\bar y-\mu_0)^2.
\end{aligned}
$$

**证明** 把先验密度乘以似然 $(\sigma^2)^{-n/2}\exp\big(-\frac{1}{2\sigma^2}[(n-1)s^2+n(\bar y-\mu)^2]\big)$：

$$
p(\mu,\sigma^2\mid y)\propto\sigma^{-1}(\sigma^2)^{-((\nu_0+n)/2+1)}\exp\Big(-\frac{1}{2\sigma^2}\big[\nu_0\sigma_0^2+(n-1)s^2+\kappa_0(\mu-\mu_0)^2+n(\bar y-\mu)^2\big]\Big).
$$
对 $\mu$ 配方。$\kappa_0(\mu-\mu_0)^2+n(\bar y-\mu)^2$ 中 $\mu^2$ 的系数是 $\kappa_n$，$-2\mu$ 的系数是 $\kappa_0\mu_0+n\bar y=\kappa_n\mu_n$，所以

$$
\kappa_0(\mu-\mu_0)^2+n(\bar y-\mu)^2=\kappa_n(\mu-\mu_n)^2+\kappa_0\mu_0^2+n\bar y^2-\kappa_n\mu_n^2=\kappa_n(\mu-\mu_n)^2+\frac{\kappa_0n}{\kappa_n}(\bar y-\mu_0)^2,
$$
其中最后一步用到 $\kappa_n(\kappa_0\mu_0^2+n\bar y^2)-(\kappa_0\mu_0+n\bar y)^2=\kappa_0n(\bar y-\mu_0)^2$。括号等于 $\nu_n\sigma_n^2+\kappa_n(\mu-\mu_n)^2$，后验具有定义 3.4.1 的形式，参数如上所述。$\square$

每个更新都有直接的解读。后验均值 $\mu_n$ 以权重 $\kappa_0$ 与 $n$ 对先验均值与样本均值取平均。两个先验样本量都增加 $n$。后验平方和 $\nu_n\sigma_n^2$ 由三部分相加：先验平方和 $\nu_0\sigma_0^2$、样本平方和 $(n-1)s^2$，以及先验均值与样本均值不一致的一项，当两者冲突时它增加关于 $\sigma^2$ 的后验不确定性。

### 3.4.3. 条件后验与边缘后验

由定义 3.4.1 与定理 3.4.1，

$$
\mu\mid\sigma^2,y\sim\mathcal{N}\Big(\mu_n,\frac{\sigma^2}{\kappa_n}\Big),\qquad\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(\nu_n,\sigma_n^2).
$$
$\mu$ 的条件后验就是 [3.7.2](/3.7.2) 中方差已知的结果，先验精度为 $\kappa_0/\sigma^2$，数据精度为 $n/\sigma^2$：

$$
\mu_n=\frac{\frac{\kappa_0}{\sigma^2}\mu_0+\frac{n}{\sigma^2}\bar y}{\frac{\kappa_0}{\sigma^2}+\frac{n}{\sigma^2}},\qquad\frac{\kappa_n}{\sigma^2}=\frac{\kappa_0}{\sigma^2}+\frac{n}{\sigma^2};
$$
因为两个精度都正比于 $1/\sigma^2$，权重不依赖于 $\sigma^2$。像命题 3.3.1 (3) 那样把 $\sigma^2$ 积分掉，现在取 $A=\nu_n\sigma_n^2+\kappa_n(\mu-\mu_n)^2$，幂为 $(\sigma^2)^{-(\nu_n+3)/2}$，得

$$
p(\mu\mid y)\propto\Big(1+\frac{\kappa_n(\mu-\mu_n)^2}{\nu_n\sigma_n^2}\Big)^{-(\nu_n+1)/2},\qquad\mu\mid y\sim t_{\nu_n}\Big(\mu_n,\frac{\sigma_n^2}{\kappa_n}\Big).
$$

### 3.4.4. 边际似然

对正常先验（$\kappa_0,\nu_0,\sigma_0^2>0$），**边际似然** $p(y)=\iint p(y\mid\mu,\sigma^2)\,p(\mu,\sigma^2)\,\mathrm{d}\mu\,\mathrm{d}\sigma^2$ 有闭式。它是计算贝叶斯因子所需的量（[3.7.8](/3.7.8)）。

**命题 3.4.1** 在定理 3.4.1 的设定下，

$$
p(y)=\frac{\Gamma(\nu_n/2)}{\Gamma(\nu_0/2)}\sqrt{\frac{\kappa_0}{\kappa_n}}\,\frac{(\nu_0\sigma_0^2)^{\nu_0/2}}{(\nu_n\sigma_n^2)^{\nu_n/2}}\,\pi^{-n/2}.
$$

**证明** 由 Bayes 公式，对每个 $(\mu,\sigma^2)$ 有 $p(y)=p(y\mid\mu,\sigma^2)\,p(\mu,\sigma^2)/p(\mu,\sigma^2\mid y)$。把归一化的 $\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_0,\sigma_0^2/\kappa_0;\nu_0,\sigma_0^2)$ 密度写成 $c(\kappa_0,\nu_0,\nu_0\sigma_0^2)\,\sigma^{-1}(\sigma^2)^{-(\nu_0/2+1)}\exp(\cdots)$，其中

$$
c(\kappa,\nu,S)=\sqrt{\frac{\kappa}{2\pi}}\cdot\frac{(S/2)^{\nu/2}}{\Gamma(\nu/2)},
$$
是正态与尺度逆卡方两个归一化常数之积。似然为 $(2\pi)^{-n/2}(\sigma^2)^{-n/2}\exp(\cdots)$。在比值中，由定理 3.4.1 的证明，$\sigma^2$ 的幂与指数函数都抵消了，剩下

$$
p(y)=(2\pi)^{-n/2}\,\frac{c(\kappa_0,\nu_0,\nu_0\sigma_0^2)}{c(\kappa_n,\nu_n,\nu_n\sigma_n^2)}.
$$
由于 $\nu_n-\nu_0=n$，$2$ 的幂合并为 $(2\pi)^{-n/2}\,2^{n/2}=\pi^{-n/2}$，得到公式。$\square$

因子 $\sqrt{\kappa_0/\kappa_n}$ 在 $\kappa_0\to0$ 时趋于 $0$：对 $\mu$ 取模糊的先验时，任何特定的数据集的先验预测密度都很小，而对 §3.3 的广义先验，边际似然根本没有定义。

### 3.4.5. 后验预测分布

新观测为 $\tilde y=\mu+\varepsilon$，$\varepsilon\sim\mathcal{N}(0,\sigma^2)$，在给定 $\sigma^2$ 时与 $\mu$ 独立。因此给定 $\sigma^2$ 与 $y$ 时，它服从 $\mathcal{N}\big(\mu_n,\sigma^2(1+\frac1{\kappa_n})\big)$，如 §3.4.3 那样对 $\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(\nu_n,\sigma_n^2)$ 取平均，得**后验预测分布**

$$
\tilde y\mid y\sim t_{\nu_n}\Big(\mu_n,\frac{\kappa_n+1}{\kappa_n}\sigma_n^2\Big).
$$
由边际似然也得到同样的结果：$p(\tilde y\mid y)=p(y,\tilde y)/p(y)$，对 $n+1$ 个观测应用命题 3.4.1，只有因子 $(\nu_{n+1}\sigma_{n+1}^2)^{-(\nu_n+1)/2}$ 依赖于 $\tilde y$，其中再用 $\tilde y$ 更新一次后验，得 $\nu_{n+1}\sigma_{n+1}^2=\nu_n\sigma_n^2+\frac{\kappa_n}{\kappa_n+1}(\tilde y-\mu_n)^2$。因此 $p(\tilde y\mid y)\propto\big(\nu_n\sigma_n^2+\frac{\kappa_n}{\kappa_n+1}(\tilde y-\mu_n)^2\big)^{-(\nu_n+1)/2}$，是同样的 $t$ 核。尺度因子 $\frac{\kappa_n+1}{\kappa_n}=1+\frac{1}{\kappa_n}$ 把关于 $\mu$ 的后验不确定性加到抽样变异上，与方差已知时的情形一样。

### 3.4.6. 例与无信息极限

**例 3.4.1（奶酪的含水量）** 某奶酪制品各块的含水量（百分数）用 $\mathcal{N}(\mu,\sigma^2)$ 建模。平均含水量 $\mu$ 的合理范围是多少？两位分析者使用同样的数据，即 $25$ 块的含水量：

$45.6, 41.1, 44.5, 44.0, 40.6, 44.1, 39.0, 39.5, 39.5, 41.7, 42.0, 42.6, 43.0, 42.5, 42.7, 42.1, 42.4, 44.8, 41.0, 39.9, 43.9, 41.3, 45.1, 38.5, 43.8$，

其中 $\bar y=42.208$，$(n-1)s^2=95.618$。Ann 没有先验信息，使用 $p(\mu,\sigma^2)\propto\sigma^{-2}$。Bob 使用共轭先验，$\mu_0=40$，$\kappa_0=1$，$\nu_0=1$，并认为 $\sigma$ 的中位数为 $3$。由于 $\sigma^2=\nu_0\sigma_0^2/X$，$X\sim\chi^2_1$，其中位数为 $0.4549$，$\sigma^2$ 的中位数为 $\sigma_0^2/0.4549=3^2$，所以 $\sigma_0^2=4.094$。后验参数为

| | $\mu_0$ | $\kappa_0$ | $\nu_0$ | $\nu_0\sigma_0^2$ | $\mu_n$ | $\kappa_n$ | $\nu_n$ | $\nu_n\sigma_n^2$ |
|---|---|---|---|---|---|---|---|---|
| Ann | — | — | — | — | $42.208$ | $25$ | $24$ | $95.618$ |
| Bob | $40$ | $1$ | $1$ | $4.094$ | $42.123$ | $26$ | $26$ | $95.618+4.094+\frac{25}{26}(42.208-40)^2=104.40$ |

$\mu$ 的边缘后验为

| | $\mu\mid y$ | $\mu$ 的 $95\%$ 中心后验区间 | $\sigma$ 的后验中位数 | $95\%$ 后验预测区间 |
|---|---|---|---|---|
| Ann | $t_{24}(42.208,\,0.3992^2)$ | $[41.38,\,43.03]$ | $2.02$ | $[38.01,\,46.41]$ |
| Bob | $t_{26}(42.123,\,0.3930^2)$ | $[41.32,\,42.93]$ | $2.03$ | $[37.93,\,46.32]$ |

Ann 的区间就是经典的 $t$ 区间（§3.3.3）。Bob 的先验均值比 $\bar y$ 低约 $5.5$ 个后验标准差，但它只有一个观测的权重，对抗 $25$ 个观测，所以只使后验均值移动了 $0.085$；他对 $\sigma\approx3$ 的先验猜测超过了样本标准差 $s=1.996$，但一个自由度对抗 $24$ 个，几乎没有改变 $\sigma$ 的后验。Bob 的区间略窄，因为 $\nu_n$ 与 $\kappa_n$ 更大。有 $25$ 个观测时，数据压倒了两个先验。

![奶酪含水量的例子。左图与中图：Ann（无信息先验）与 Bob（共轭先验）的 (μ, σ) 联合后验密度的等高线，以及先抽取 σ² 再抽取给定 σ² 的 μ 所得的 400 个后验样本。右图：μ 的边缘后验 t 密度与 Bob 的先验均值。](./plots/cheese_joint_posterior.py)

:::

*作为极限的无信息先验。* 在定义 3.4.1 的密度中令 $\kappa_0\to0$，$\nu_0\to-1$，$\sigma_0^2\to0$，得

$$
p(\mu,\sigma^2)\propto\sigma^{-1}(\sigma^2)^{-(-1/2+1)}=\sigma^{-2},
$$
即 §3.3 的先验，定理 3.4.1 的后验参数变为 $\mu_n=\bar y$，$\kappa_n=n$，$\nu_n=n-1$，$\nu_n\sigma_n^2=(n-1)s^2$，即命题 3.3.1 的结果。$\nu_0=-1$ 这一取值表明 $p(\mu,\sigma^2)\propto\sigma^{-2}$ 并不是“零先验数据”的共轭先验：它对应于方差的先验自由度为负一。正是这种记账方式使 $\sigma^2$ 的后验有 $n-1$ 个自由度，其中一个用于估计 $\mu$，与经典理论完全一致。

## 3.5. 两个正态均值的比较：Behrens–Fisher 问题

设 $y_{11},\dots,y_{1n_1}$ 是 iid 的 $\mathcal{N}(\mu_1,\sigma_1^2)$，并且独立地 $y_{21},\dots,y_{2n_2}$ 是 iid 的 $\mathcal{N}(\mu_2,\sigma_2^2)$，考虑 $\delta=\mu_1-\mu_2$，例如为了评价 $H_0\colon\delta=0$。当 $\sigma_1^2=\sigma_2^2$ 时，经典分析使用合并的双样本 $t$ 统计量，它是自由度为 $n_1+n_2-2$ 的精确枢轴量。当 $\sigma_1^2\ne\sigma_2^2$ 时，不存在不含方差比的精确枢轴量：这就是 **Behrens–Fisher 问题**（[3.2.4](/3.2.4)），频率学派的做法依赖于近似，如 **Welch t 检验**。

贝叶斯的处理不需要新的思想。给两组分别取独立的先验，例如共轭先验

$$
\mu_j\mid\sigma_j^2\sim\mathcal{N}(\mu_0,\sigma_j^2/\kappa_0),\qquad\sigma_j^2\sim\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2),\qquad j=1,2,
$$
或无信息先验 $p(\mu_j,\sigma_j^2)\propto\sigma_j^{-2}$。似然按组分解，所以 $(\mu_1,\sigma_1^2)$ 与 $(\mu_2,\sigma_2^2)$ 的后验相互独立，并且由 §3.4.3，

$$
\mu_j\mid y\sim t_{\nu_{jn}}\Big(\mu_{jn},\frac{\sigma_{jn}^2}{\kappa_{jn}}\Big),\qquad j=1,2,
$$
其中各组的后验参数取自定理 3.4.1（在无信息先验下为 $t_{n_j-1}(\bar y_j,s_j^2/n_j)$）。$\delta$ 的后验是两个自由度与尺度都不同的独立 $t$ 变量之差的分布。它没有标准的闭式，但容易模拟：从各自的后验抽取 $\mu_1^s$ 与 $\mu_2^s$，令 $\delta^s=\mu_1^s-\mu_2^s$，$s=1,\dots,S$。后验概率如 $\mathbb{P}(\delta>0\mid y)$ 与 $\delta$ 的区间则可以直接从抽样中读出。在无信息先验下，这个后验与 Fisher 的信仰推断论证所得的 Behrens–Fisher 分布一致，这是 Jeffreys 所观察到的。

**例 3.5.1** 考虑示意性的概括统计量 $n_1=10$，$\bar y_1=5.2$，$s_1=1.0$ 与 $n_2=15$，$\bar y_2=4.4$，$s_2=2.5$，取无信息先验。则 $\mu_1\mid y\sim t_9(5.2,\,0.316^2)$，$\mu_2\mid y\sim t_{14}(4.4,\,0.645^2)$。取 $S=4\times10^5$ 个样本，$\delta\mid y$ 的均值为 $0.80$，$95\%$ 中心后验区间为 $[-0.75,2.36]$，$\mathbb{P}(\delta>0\mid y)=0.85$。Welch 的近似 $95\%$ 置信区间为 $[-0.70,2.30]$，自由度为 $19.8$，与贝叶斯区间接近，但它得自对依赖于未知方差比的抽样分布的近似。

![用示意数据说明 Behrens–Fisher 问题：μ₁ 与 μ₂ 的边缘后验（左），以及 δ = μ₁ − μ₂ 的模拟样本的直方图及其 95% 中心后验区间（右）。](./plots/behrens_fisher.py)

## 3.6. 多元正态模型

### 3.6.1. 似然

设 $\boldsymbol{y}_1,\dots,\boldsymbol{y}_n\in\mathbb{R}^d$ 是 iid 的，服从**多元正态分布** $\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$。利用迹恒等式 $\boldsymbol{x}^{\mathsf T}\Sigma^{-1}\boldsymbol{x}=\operatorname{tr}(\Sigma^{-1}\boldsymbol{x}\boldsymbol{x}^{\mathsf T})$，似然为

$$
p(\boldsymbol{y}_1,\dots,\boldsymbol{y}_n\mid\boldsymbol{\mu},\Sigma)\propto(\det\Sigma)^{-n/2}\exp\Big(-\frac12\sum_{i=1}^n(\boldsymbol{y}_i-\boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{y}_i-\boldsymbol{\mu})\Big)=(\det\Sigma)^{-n/2}\exp\Big(-\frac12\operatorname{tr}(\Sigma^{-1}S_0)\Big),
$$
其中 $S_0=\sum_i(\boldsymbol{y}_i-\boldsymbol{\mu})(\boldsymbol{y}_i-\boldsymbol{\mu})^{\mathsf T}$。与一维情形一样，

$$
S_0=S+n(\bar{\boldsymbol{y}}-\boldsymbol{\mu})(\bar{\boldsymbol{y}}-\boldsymbol{\mu})^{\mathsf T},\qquad S=\sum_{i=1}^n(\boldsymbol{y}_i-\bar{\boldsymbol{y}})(\boldsymbol{y}_i-\bar{\boldsymbol{y}})^{\mathsf T},
$$
其中平方和矩阵 $S$ 是**样本协方差矩阵**的 $n-1$ 倍。

两个较简单的情形是 [3.7.2](/3.7.2) 的多元版本：

- *$\Sigma$ 已知。* 先验 $\boldsymbol{\mu}\sim\mathcal{N}_d(\boldsymbol{\mu}_0,\Lambda_0)$ 是共轭的，$\boldsymbol{\mu}\mid\boldsymbol{y}\sim\mathcal{N}_d(\boldsymbol{\mu}_n,\Lambda_n)$，其中 $\Lambda_n^{-1}=\Lambda_0^{-1}+n\Sigma^{-1}$，$\boldsymbol{\mu}_n=\Lambda_n(\Lambda_0^{-1}\boldsymbol{\mu}_0+n\Sigma^{-1}\bar{\boldsymbol{y}})$：精度矩阵相加，后验均值是按精度加权的平均。
- *$\boldsymbol{\mu}$ 已知。* 似然 $(\det\Sigma)^{-n/2}\exp(-\frac12\operatorname{tr}(\Sigma^{-1}S_0))$ 作为 $\Sigma$ 的函数，是下面定义的逆 Wishart 分布的核，即尺度逆卡方的矩阵类似物。

### 3.6.2. Wishart、逆 Wishart 与多元 t 分布

回忆 [3.4.3](/3.4.3) 的 **Wishart 分布**：若 $\boldsymbol{z}_1,\dots,\boldsymbol{z}_\nu\overset{\text{iid}}{\sim}\mathcal{N}_d(\boldsymbol{0},\Lambda)$，则 $W=\sum_{i=1}^\nu\boldsymbol{z}_i\boldsymbol{z}_i^{\mathsf T}\sim W_d(\nu,\Lambda)$，均值为 $\nu\Lambda$。它是缩放 $\chi^2$ 的多元类似物：当 $d=1$ 且 $z_i\sim\mathcal{N}(0,\tau^2)$ 时，$\sum_iz_i^2\sim\tau^2\chi^2_\nu$。

**定义 3.6.1（逆 Wishart 分布）** 设 $\nu>d-1$，$\Psi$ 是 $d\times d$ 对称正定矩阵。若 $\Sigma^{-1}\sim W_d(\nu,\Psi^{-1})$，则称随机对称正定矩阵 $\Sigma$ 服从自由度为 $\nu$、尺度矩阵为 $\Psi$ 的**逆 Wishart 分布** $\mathrm{Inv}\text{-}W_d(\nu,\Psi)$。其密度为

$$
p(\Sigma)=\frac{(\det\Psi)^{\nu/2}}{2^{\nu d/2}\,\Gamma_d(\nu/2)}\,(\det\Sigma)^{-(\nu+d+1)/2}\exp\Big(-\frac12\operatorname{tr}(\Psi\Sigma^{-1})\Big),
$$
其中 $\Gamma_d(a)=\pi^{d(d-1)/4}\prod_{i=1}^d\Gamma\big(a+\frac{1-i}{2}\big)$ 是多元 Gamma 函数。当 $\nu>d+1$ 时，其均值为 $\mathbb{E}\Sigma=\Psi/(\nu-d-1)$。

当 $d=1$ 时，$\mathrm{Inv}\text{-}W_1(\nu,\psi)=\mathrm{Inv}\text{-}\Gamma(\nu/2,\psi/2)=\mathrm{Inv}\text{-}\chi^2(\nu,\psi/\nu)$：逆 Wishart 分布是多元的尺度逆卡方分布，$\Psi$ 扮演先验平方和 $\nu\sigma_0^2$ 的角色。

参数化值得小心，因为同一个密度有两种约定在使用。Gelman 等把 $\Sigma\sim\mathrm{Inv}\text{-}\mathrm{Wishart}_\nu(\Psi^{-1})$ 的变元写成尺度矩阵的逆，即 $\Sigma^{-1}$ 的 Wishart 分布的尺度矩阵：在他们的记号中，$\Sigma\sim\mathrm{Wishart}_\nu(\Lambda)$ 蕴含 $\Sigma^{-1}\sim\mathrm{Inv}\text{-}\mathrm{Wishart}_\nu(\Lambda)$。软件如 scipy（`invwishart(df=nu, scale=Psi)`）与多数文献把尺度矩阵 $\Psi$ 本身放在变元中，所以 $\mathbb{E}\Sigma$ 正比于变元。本书一律使用尺度矩阵的形式 $\mathrm{Inv}\text{-}W_d(\nu,\Psi)$；换算时，Gelman 等的 $\mathrm{Inv}\text{-}\mathrm{Wishart}_\nu(\Psi^{-1})$ 就是我们的 $\mathrm{Inv}\text{-}W_d(\nu,\Psi)$。[3.7.4](/3.7.4) 的表同时列出了两者。

**定义 3.6.2（多元 t 分布）** 设 $\nu>0$，$\boldsymbol{\mu}\in\mathbb{R}^d$，$\Sigma$ 对称正定。**多元 t 分布** $t_\nu(\boldsymbol{\mu},\Sigma)$ 的密度为

$$
p(\boldsymbol{\theta})=\frac{\Gamma(\frac{\nu+d}{2})}{\Gamma(\frac\nu2)\,(\nu\pi)^{d/2}}(\det\Sigma)^{-1/2}\Big(1+\frac1\nu(\boldsymbol{\theta}-\boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{\theta}-\boldsymbol{\mu})\Big)^{-(\nu+d)/2},\qquad\boldsymbol{\theta}\in\mathbb{R}^d.
$$

等价地，$\boldsymbol{\theta}=\boldsymbol{\mu}+\boldsymbol{z}/\sqrt{u/\nu}$，其中 $\boldsymbol{z}\sim\mathcal{N}_d(\boldsymbol{0},\Sigma)$ 与 $u\sim\chi^2_\nu$ 独立。其均值为 $\boldsymbol{\mu}$（$\nu>1$），协方差矩阵为 $\frac{\nu}{\nu-2}\Sigma$（$\nu>2$）；当 $d=1$ 时就是注 3.3.1 的 $t_\nu(\mu,\sigma^2)$。二次型满足 $\frac1d(\boldsymbol{\theta}-\boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{\theta}-\boldsymbol{\mu})\sim F_{d,\nu}$，所以它的水平集给出椭球形的可信域。

### 3.6.3. 正态–逆 Wishart 共轭先验

**定义 3.6.3（正态–逆 Wishart 分布）** 设 $\boldsymbol{\mu}_0\in\mathbb{R}^d$，$\kappa_0>0$，$\nu_0>d-1$，$\Lambda_0$ 对称正定。若

$$
\Sigma\sim\mathrm{Inv}\text{-}W_d(\nu_0,\Lambda_0),\qquad\boldsymbol{\mu}\mid\Sigma\sim\mathcal{N}_d(\boldsymbol{\mu}_0,\Sigma/\kappa_0),
$$
联合密度为

$$
p(\boldsymbol{\mu},\Sigma)\propto(\det\Sigma)^{-((\nu_0+d)/2+1)}\exp\Big(-\frac12\operatorname{tr}(\Lambda_0\Sigma^{-1})-\frac{\kappa_0}{2}(\boldsymbol{\mu}-\boldsymbol{\mu}_0)^{\mathsf T}\Sigma^{-1}(\boldsymbol{\mu}-\boldsymbol{\mu}_0)\Big),
$$
则称 $(\boldsymbol{\mu},\Sigma)$ 服从**正态–逆 Wishart 分布** $\mathcal{N}\text{-}\mathrm{Inv}\text{-}W(\boldsymbol{\mu}_0,\Lambda_0/\kappa_0;\nu_0,\Lambda_0)$。

$\det\Sigma$ 的指数由逆 Wishart 密度的 $-(\nu_0+d+1)/2$ 与 $\boldsymbol{\mu}$ 的正态密度的 $-1/2$ 合并而成。

**定理 3.6.1** 设 $\boldsymbol{y}_1,\dots,\boldsymbol{y}_n\mid\boldsymbol{\mu},\Sigma\overset{\text{iid}}{\sim}\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$，$(\boldsymbol{\mu},\Sigma)\sim\mathcal{N}\text{-}\mathrm{Inv}\text{-}W(\boldsymbol{\mu}_0,\Lambda_0/\kappa_0;\nu_0,\Lambda_0)$。则 $(\boldsymbol{\mu},\Sigma)\mid\boldsymbol{y}\sim\mathcal{N}\text{-}\mathrm{Inv}\text{-}W(\boldsymbol{\mu}_n,\Lambda_n/\kappa_n;\nu_n,\Lambda_n)$，其中

$$
\begin{aligned}
\boldsymbol{\mu}_n&=\frac{\kappa_0}{\kappa_0+n}\boldsymbol{\mu}_0+\frac{n}{\kappa_0+n}\bar{\boldsymbol{y}},\qquad\kappa_n=\kappa_0+n,\qquad\nu_n=\nu_0+n,\\
\Lambda_n&=\Lambda_0+S+\frac{\kappa_0n}{\kappa_0+n}(\bar{\boldsymbol{y}}-\boldsymbol{\mu}_0)(\bar{\boldsymbol{y}}-\boldsymbol{\mu}_0)^{\mathsf T}.
\end{aligned}
$$
特别地，

$$
\boldsymbol{\mu}\mid\Sigma,\boldsymbol{y}\sim\mathcal{N}_d\Big(\boldsymbol{\mu}_n,\frac{\Sigma}{\kappa_n}\Big),\qquad\Sigma\mid\boldsymbol{y}\sim\mathrm{Inv}\text{-}W_d(\nu_n,\Lambda_n),\qquad\boldsymbol{\mu}\mid\boldsymbol{y}\sim t_{\nu_n-d+1}\Big(\boldsymbol{\mu}_n,\frac{\Lambda_n}{\kappa_n(\nu_n-d+1)}\Big),
$$
并且新观测的后验预测分布为 $\tilde{\boldsymbol{y}}\mid\boldsymbol{y}\sim t_{\nu_n-d+1}\big(\boldsymbol{\mu}_n,\frac{(\kappa_n+1)\Lambda_n}{\kappa_n(\nu_n-d+1)}\big)$。

**证明** 把每个二次型写成迹。先验与似然之积为

$$
(\det\Sigma)^{-((\nu_0+n+d)/2+1)}\exp\Big(-\frac12\operatorname{tr}\Big(\big[\Lambda_0+S+\kappa_0(\boldsymbol{\mu}-\boldsymbol{\mu}_0)(\boldsymbol{\mu}-\boldsymbol{\mu}_0)^{\mathsf T}+n(\bar{\boldsymbol{y}}-\boldsymbol{\mu})(\bar{\boldsymbol{y}}-\boldsymbol{\mu})^{\mathsf T}\big]\Sigma^{-1}\Big)\Big).
$$
定理 3.4.1 的证明中的标量恒等式对外积原样成立：

$$
\kappa_0(\boldsymbol{\mu}-\boldsymbol{\mu}_0)(\boldsymbol{\mu}-\boldsymbol{\mu}_0)^{\mathsf T}+n(\bar{\boldsymbol{y}}-\boldsymbol{\mu})(\bar{\boldsymbol{y}}-\boldsymbol{\mu})^{\mathsf T}=\kappa_n(\boldsymbol{\mu}-\boldsymbol{\mu}_n)(\boldsymbol{\mu}-\boldsymbol{\mu}_n)^{\mathsf T}+\frac{\kappa_0n}{\kappa_n}(\bar{\boldsymbol{y}}-\boldsymbol{\mu}_0)(\bar{\boldsymbol{y}}-\boldsymbol{\mu}_0)^{\mathsf T},
$$
所以括号等于 $\Lambda_n+\kappa_n(\boldsymbol{\mu}-\boldsymbol{\mu}_n)(\boldsymbol{\mu}-\boldsymbol{\mu}_n)^{\mathsf T}$，乘积具有定义 3.6.3 的形式，参数如上所述。对 $\boldsymbol{\mu}$ 的边缘分布，利用逆 Wishart 密度的归一化常数把 $\Sigma$ 积分掉：$\int(\det\Sigma)^{-(\nu+d+1)/2}\exp(-\frac12\operatorname{tr}(A\Sigma^{-1}))\,\mathrm{d}\Sigma\propto(\det A)^{-\nu/2}$，这里 $\nu=\nu_n+1$，$A=\Lambda_n+\kappa_n(\boldsymbol{\mu}-\boldsymbol{\mu}_n)(\boldsymbol{\mu}-\boldsymbol{\mu}_n)^{\mathsf T}$。由矩阵行列式引理 $\det A=\det\Lambda_n\,\big(1+\kappa_n(\boldsymbol{\mu}-\boldsymbol{\mu}_n)^{\mathsf T}\Lambda_n^{-1}(\boldsymbol{\mu}-\boldsymbol{\mu}_n)\big)$，所以

$$
p(\boldsymbol{\mu}\mid\boldsymbol{y})\propto\big(1+\kappa_n(\boldsymbol{\mu}-\boldsymbol{\mu}_n)^{\mathsf T}\Lambda_n^{-1}(\boldsymbol{\mu}-\boldsymbol{\mu}_n)\big)^{-(\nu_n+1)/2}.
$$
与定义 3.6.2 对比，$\nu+d=\nu_n+1$ 给出 $\nu=\nu_n-d+1$，$\frac1\nu\Sigma^{-1}=\kappa_n\Lambda_n^{-1}$ 给出尺度矩阵 $\Lambda_n/(\kappa_n(\nu_n-d+1))$。预测分布同样由 $\tilde{\boldsymbol{y}}\mid\Sigma,\boldsymbol{y}\sim\mathcal{N}_d\big(\boldsymbol{\mu}_n,(1+\frac1{\kappa_n})\Sigma\big)$ 得到。$\square$

一维与 $d$ 维的共轭分析逐项对应：

| | 一元正态（§3.4） | 多元正态 |
|---|---|---|
| 先验 | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_0,\sigma_0^2/\kappa_0;\nu_0,\sigma_0^2)$ | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}W(\boldsymbol{\mu}_0,\Lambda_0/\kappa_0;\nu_0,\Lambda_0)$ |
| 先验均值 | $\mu_0$ | $\boldsymbol{\mu}_0$ |
| 先验的方差信息 | 先验样本方差 $\sigma_0^2$ | 先验平方和矩阵 $\Lambda_0$ |
| 均值的先验数据 | $\kappa_0$ | $\kappa_0$ |
| 方差的先验数据 | $\nu_0$ | $\nu_0$ |
| 后验均值 | $\mu_n=\frac{\kappa_0\mu_0+n\bar y}{\kappa_0+n}$ | $\boldsymbol{\mu}_n=\frac{\kappa_0\boldsymbol{\mu}_0+n\bar{\boldsymbol{y}}}{\kappa_0+n}$ |
| 后验的方差信息 | $\nu_n\sigma_n^2=\nu_0\sigma_0^2+(n-1)s^2+\frac{\kappa_0n}{\kappa_n}(\bar y-\mu_0)^2$ | $\Lambda_n=\Lambda_0+S+\frac{\kappa_0n}{\kappa_n}(\bar{\boldsymbol{y}}-\boldsymbol{\mu}_0)(\bar{\boldsymbol{y}}-\boldsymbol{\mu}_0)^{\mathsf T}$ |
| 均值的边缘后验 | $t_{\nu_n}(\mu_n,\sigma_n^2/\kappa_n)$ | $t_{\nu_n-d+1}\big(\boldsymbol{\mu}_n,\Lambda_n/(\kappa_n(\nu_n-d+1))\big)$ |

当 $d=1$ 时，$\Lambda_0=\nu_0\sigma_0^2$，$\Lambda_n=\nu_n\sigma_n^2$，右列化为左列。

### 3.6.4. 无信息先验

与一维时一样，取共轭密度的极限 $\kappa_0\to0$，$\nu_0\to-1$，$\det\Lambda_0\to0$，得

$$
p(\boldsymbol{\mu},\Sigma)\propto(\det\Sigma)^{-(d+1)/2}.
$$
这是 $\sigma^{-2}$ 的多元版本：在 $\boldsymbol{\mu}$ 上平坦，对 $\Sigma$ 则是均值已知的正态分布协方差矩阵的 Jeffreys 先验，在位置与尺度的先验独立之下结合起来。后验参数变为 $\boldsymbol{\mu}_n=\bar{\boldsymbol{y}}$，$\kappa_n=n$，$\nu_n=n-1$，$\Lambda_n=S$，所以当 $n>d$ 时，

$$
\boldsymbol{\mu}\mid\Sigma,\boldsymbol{y}\sim\mathcal{N}_d\Big(\bar{\boldsymbol{y}},\frac{\Sigma}{n}\Big),\qquad\Sigma\mid\boldsymbol{y}\sim\mathrm{Inv}\text{-}W_d(n-1,S),\qquad\boldsymbol{\mu}\mid\boldsymbol{y}\sim t_{n-d}\Big(\bar{\boldsymbol{y}},\frac{S}{n(n-d)}\Big).
$$
用 Gelman 等的记号，第二个陈述写作 $\Sigma\mid\boldsymbol{y}\sim\mathrm{Inv}\text{-}\mathrm{Wishart}_{n-1}(S^{-1})$。与频率学派推断的联系又是精确的。由定义 3.6.2 的 $F$ 性质，取样本协方差矩阵 $S/(n-1)$，

$$
n(\boldsymbol{\mu}-\bar{\boldsymbol{y}})^{\mathsf T}\Big(\frac{S}{n-1}\Big)^{-1}(\boldsymbol{\mu}-\bar{\boldsymbol{y}})\;\Big|\;\boldsymbol{y}\sim\frac{(n-1)d}{n-d}F_{d,n-d},
$$
这就是 Hotelling $T^2$ 统计量的分布（[3.4.3](/3.4.3)）；$\boldsymbol{\mu}$ 的后验可信椭球与经典的置信椭球一致。

## 小结

| 模型 | 先验 | 后验 | 均值的边缘后验 | 后验预测 |
|---|---|---|---|---|
| $\mathrm{Mult}(n,\boldsymbol{\theta})$ | $\mathrm{Dir}(\boldsymbol{\alpha})$（定义 3.2.1） | $\mathrm{Dir}(\boldsymbol{\alpha}+\boldsymbol{y})$ | $\theta_j\mid\boldsymbol{y}\sim\mathrm{Beta}(\alpha_j+y_j,\alpha_0-\alpha_j+n-y_j)$（命题 3.2.1） | $\mathbb{P}(\tilde y=j\mid\boldsymbol{y})=\frac{\alpha_j+y_j}{\alpha_0+n}$ |
| $\mathcal{N}(\mu,\sigma^2)$ | $\sigma^{-2}$ | $\mu\mid\sigma^2,y\sim\mathcal{N}(\bar y,\frac{\sigma^2}{n})$，$\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(n-1,s^2)$ | $t_{n-1}(\bar y,\frac{s^2}{n})$（命题 3.3.1） | $t_{n-1}\big(\bar y,(1+\frac1n)s^2\big)$ |
| $\mathcal{N}(\mu,\sigma^2)$ | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_0,\frac{\sigma_0^2}{\kappa_0};\nu_0,\sigma_0^2)$（定义 3.4.1） | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_n,\frac{\sigma_n^2}{\kappa_n};\nu_n,\sigma_n^2)$（定理 3.4.1） | $t_{\nu_n}(\mu_n,\frac{\sigma_n^2}{\kappa_n})$ | $t_{\nu_n}\big(\mu_n,\frac{\kappa_n+1}{\kappa_n}\sigma_n^2\big)$ |
| $\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$ | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}W(\boldsymbol{\mu}_0,\frac{\Lambda_0}{\kappa_0};\nu_0,\Lambda_0)$（定义 3.6.3） | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}W(\boldsymbol{\mu}_n,\frac{\Lambda_n}{\kappa_n};\nu_n,\Lambda_n)$（定理 3.6.1） | $t_{\nu_n-d+1}\big(\boldsymbol{\mu}_n,\frac{\Lambda_n}{\kappa_n(\nu_n-d+1)}\big)$ | $t_{\nu_n-d+1}\big(\boldsymbol{\mu}_n,\frac{(\kappa_n+1)\Lambda_n}{\kappa_n(\nu_n-d+1)}\big)$ |
| $\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$ | $(\det\Sigma)^{-(d+1)/2}$ | $\Sigma\mid\boldsymbol{y}\sim\mathrm{Inv}\text{-}W_d(n-1,S)$ | $t_{n-d}\big(\bar{\boldsymbol{y}},\frac{S}{n(n-d)}\big)$ | |

- 讨厌参数被积分掉：$p(\theta_1\mid y)=\int p(\theta_1\mid\theta_2,y)\,p(\theta_2\mid y)\,\mathrm{d}\theta_2$，是条件后验的混合；模拟先抽 $\theta_2$，再抽 $\theta_1\mid\theta_2$（§3.1）。
- 共轭超参数就是先验数据：Dirichlet 先验计数；$\kappa_0$ 与 $\nu_0$ 分别是关于均值与方差的先验观测数；后验平方和含有先验与数据的冲突项 $\frac{\kappa_0n}{\kappa_n}(\bar y-\mu_0)^2$。
- 无信息先验是共轭先验的极限（$\kappa_0\to0$，$\nu_0\to-1$，$\sigma_0^2\to0$ 或 $\Lambda_0\to0$），并重现经典的枢轴量结果：$t$ 区间、方差的 $\chi^2$ 区间、Hotelling $T^2$ 椭球。
- 带正常共轭先验的正态模型的**边际似然**有命题 3.4.1 的闭式；在广义先验下它不存在。
- Behrens–Fisher 问题有直接的贝叶斯解：两组的后验相互独立，并模拟 $\delta=\mu_1-\mu_2$（§3.5）。
- 逆 Wishart 的参数化：这里与 scipy 中的 $\mathrm{Inv}\text{-}W_d(\nu,\Psi)$ 就是 Gelman 等的 $\mathrm{Inv}\text{-}\mathrm{Wishart}_\nu(\Psi^{-1})$；均值为 $\Psi/(\nu-d-1)$。

## 思考题

1. 在先验 $p(\mu,\sigma^2)\propto\sigma^{-2}$ 下，推导后验预测分布 $\tilde y\mid y\sim t_{n-1}\big(\bar y,(1+\frac1n)s^2\big)$，并计算例 3.4.1（Ann）中下一块奶酪的 $95\%$ 预测区间。把它与 $\mu$ 的区间比较。

   **答** 给定 $\sigma^2$ 与 $y$，$\tilde y=\mu+\varepsilon$，其中 $\mu\mid\sigma^2,y\sim\mathcal{N}(\bar y,\sigma^2/n)$，$\varepsilon\sim\mathcal{N}(0,\sigma^2)$ 与之独立，所以 $\tilde y\mid\sigma^2,y\sim\mathcal{N}(\bar y,(1+\frac1n)\sigma^2)$。记 $c=1+\frac1n$，对 $p(\sigma^2\mid y)\propto(\sigma^2)^{-(n+1)/2}\exp(-\frac{(n-1)s^2}{2\sigma^2})$ 积分，得 $p(\tilde y\mid y)\propto\int(\sigma^2)^{-(n+2)/2}\exp\big(-\frac{1}{2\sigma^2}[(n-1)s^2+(\tilde y-\bar y)^2/c]\big)\,\mathrm{d}\sigma^2\propto\big[1+\frac{(\tilde y-\bar y)^2}{(n-1)cs^2}\big]^{-n/2}$，这是 $t_{n-1}(\bar y,cs^2)$ 的核。对奶酪数据，$\sqrt{(1+\frac1{25})\times3.984}=2.036$，$t_{24,0.025}=2.064$，所以区间为 $42.208\pm4.20=[38.01,46.41]$。它大约是 $\mu$ 的区间 $[41.38,43.03]$ 的五倍宽，因为它包含各块之间的变异，而这种变异不随 $n$ 减小。
2. 例 3.4.1 中的 Bob 改变了想法，赋予先验均值 $\kappa_0=25$ 个观测的权重，保持 $\mu_0=40$，$\nu_0=1$，$\sigma_0^2=4.094$。计算 $\mu$ 的后验及其 $95\%$ 区间。解释为什么 $\sigma^2$ 的后验也随之改变。

   **答** 此时 $\kappa_n=50$，$\mu_n=\frac{25\times40+25\times42.208}{50}=41.104$，$\nu_n=26$，$\nu_n\sigma_n^2=4.094+95.618+\frac{25\times25}{50}(2.208)^2=160.65$，所以 $\sigma_n^2=6.179$，$\mu\mid y\sim t_{26}(41.104,\,0.3515^2)$。$95\%$ 区间为 $41.104\pm2.056\times0.3515=[40.38,41.83]$，不含样本均值 $42.208$。$\sigma^2$ 的后验上移，是因为冲突项 $\frac{\kappa_0n}{\kappa_n}(\bar y-\mu_0)^2$ 从 $4.69$ 增长到 $60.94$：在这个模型中，一个与数据不一致的、关于 $\mu$ 的强先验，部分地被更大的抽样方差所解释，因为 $\mu$ 的先验方差是 $\sigma^2/\kappa_0$。
3. 直接证明例 3.2.1 中 Dirichlet 后验的合并性质：证明无论在分析之前还是之后合并两个类别，$\theta_1+\theta_2$（口渴或多尿）的后验都相同，并给出它。

   **答** 分析之后：$\boldsymbol{\theta}\mid\boldsymbol{y}\sim\mathrm{Dir}(11,9,16,14)$，由命题 3.2.1，$(\theta_1+\theta_2,\theta_3,\theta_4)\mid\boldsymbol{y}\sim\mathrm{Dir}(20,16,14)$，所以 $\theta_1+\theta_2\mid\boldsymbol{y}\sim\mathrm{Beta}(20,30)$。分析之前：合并后的计数为 $(18,15,13)$，合并后的先验为 $\mathrm{Dir}(2,1,1)$（同样由命题 3.2.1 作用于 $\mathrm{Dir}(1,1,1,1)$）；后验为 $\mathrm{Dir}(20,16,14)$，结果相同。注意合并后的先验在较粗的单纯形上并不均匀：合并 $k$ 个均匀的类别所得的先验偏向合并后的那一类。$\theta_1+\theta_2$ 的后验均值为 $0.40$。
4. 设 $\theta\mid V\sim\mathcal{N}(\mu,V)$，$V\sim\mathrm{Inv}\text{-}\chi^2(\nu,\sigma^2)$。证明 $\theta\sim t_\nu(\mu,\sigma^2)$。本章的哪些结果是这一事实的实例？

   **答** $p(\theta)\propto\int V^{-1/2}\exp\big(-\frac{(\theta-\mu)^2}{2V}\big)V^{-(\nu/2+1)}\exp\big(-\frac{\nu\sigma^2}{2V}\big)\,\mathrm{d}V=\int V^{-((\nu+1)/2+1)}\exp\big(-\frac{A}{2V}\big)\,\mathrm{d}V$，其中 $A=\nu\sigma^2+(\theta-\mu)^2$。被积函数是未归一化的 $\mathrm{Inv}\text{-}\Gamma(\frac{\nu+1}2,\frac A2)$ 密度，其积分正比于 $A^{-(\nu+1)/2}\propto\big(1+\frac{(\theta-\mu)^2}{\nu\sigma^2}\big)^{-(\nu+1)/2}$，即 $t_\nu(\mu,\sigma^2)$ 的核。命题 3.3.1 与 §3.4.3 中的边缘后验 $\mu\mid y$（$V=\sigma^2/\kappa_n$，它服从 $\mathrm{Inv}\text{-}\chi^2(\nu_n,\sigma_n^2/\kappa_n)$）以及 §3.3.3 与 §3.4.5 的后验预测分布，都是这种形式：方差正比于 $\sigma^2$ 的正态分布，对 $\sigma^2$ 的尺度逆卡方后验取平均。
5. 两组的方差相等但未知：$y_{ji}\mid\mu_1,\mu_2,\sigma^2\sim\mathcal{N}(\mu_j,\sigma^2)$，先验为 $p(\mu_1,\mu_2,\sigma^2)\propto\sigma^{-2}$。求 $\delta=\mu_1-\mu_2$ 的后验，并与经典的合并 $t$ 区间比较。为什么方差不等的情形对频率学派方法更难而对贝叶斯方法并不更难？

   **答** 给定 $\sigma^2$，$\mu_1$ 与 $\mu_2$ 相互独立，分别服从 $\mathcal{N}(\bar y_j,\sigma^2/n_j)$，所以 $\delta\mid\sigma^2,y\sim\mathcal{N}\big(\bar y_1-\bar y_2,\sigma^2(\frac1{n_1}+\frac1{n_2})\big)$。把 $\mu_1,\mu_2$ 从联合后验中积分掉，得 $\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(n_1+n_2-2,s_p^2)$，其中合并方差 $s_p^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}$，再由思考题 4，$\delta\mid y\sim t_{n_1+n_2-2}\big(\bar y_1-\bar y_2,s_p^2(\frac1{n_1}+\frac1{n_2})\big)$。它的中心区间就是合并 $t$ 置信区间。方差不等时，频率学派需要一个抽样分布不依赖于 $\sigma_1^2/\sigma_2^2$ 的统计量，而这样的统计量并不存在；贝叶斯方法则对两个方差都积分，这总是可行的，只是计算（用模拟代替 $t$ 表）有所改变。
6. 证明 $d=1$ 时的正态–逆 Wishart 分析化为正态–逆卡方分析：确定 $\Lambda_0$ 与 $\Lambda_n$，并核对均值的边缘 $t$ 后验的自由度与尺度。

   **答** 当 $d=1$ 时，$\mathrm{Inv}\text{-}W_1(\nu_0,\Lambda_0)=\mathrm{Inv}\text{-}\chi^2(\nu_0,\Lambda_0/\nu_0)$，所以 $\Lambda_0=\nu_0\sigma_0^2$；后验公式给出 $\Lambda_n=\nu_0\sigma_0^2+(n-1)s^2+\frac{\kappa_0n}{\kappa_n}(\bar y-\mu_0)^2=\nu_n\sigma_n^2$，并且 $S=(n-1)s^2$。边缘后验 $t_{\nu_n-d+1}\big(\mu_n,\frac{\Lambda_n}{\kappa_n(\nu_n-d+1)}\big)$ 化为 $t_{\nu_n}\big(\mu_n,\frac{\nu_n\sigma_n^2}{\kappa_n\nu_n}\big)=t_{\nu_n}(\mu_n,\sigma_n^2/\kappa_n)$，与 §3.4.3 一致。密度的指数 $-((\nu_0+d)/2+1)$ 化为 $-((\nu_0+1)/2+1)$，即 $\sigma^{-1}(\sigma^2)^{-(\nu_0/2+1)}$。
7. Ann 想用贝叶斯因子把例 3.4.1 的正态模型与一个竞争模型比较。为什么她不能使用自己模型的边际似然？当 Bob 令 $\kappa_0\to0$ 时，他的边际似然会怎样？

   **答** 在广义先验 $p(\mu,\sigma^2)\propto\sigma^{-2}$ 下，先验密度只定义到一个任意常数 $c$，而 $p(y)=\iint p(y\mid\mu,\sigma^2)\,c\,\sigma^{-2}\,\mathrm{d}\mu\,\mathrm{d}\sigma^2$ 继承了这个常数，所以边际似然之比是任意的。在命题 3.4.1 中，因子 $\sqrt{\kappa_0/\kappa_n}$ 在 $\kappa_0\to0$ 时趋于 $0$，而后验几乎不变：对 $\mu$ 的先验越来越模糊的模型，把它的先验预测密度铺到越来越多的数据集上，受到越来越重的惩罚。因此贝叶斯因子对几乎不影响后验的先验的模糊程度很敏感，这是 [3.7.8](/3.7.8) 的一个主题。
8. 在先验为 $\mathrm{Dir}(0,\dots,0)$ 的多项模型中，证明后验是正常的，当且仅当每个类别至少被观测到一次。

   **答** 后验在单纯形上正比于 $\prod_j\theta_j^{y_j-1}$。若所有 $y_j\ge1$，这是 $\mathrm{Dir}(\boldsymbol{y})$ 的核，是正常的。设 $y_1=0$。用 $\theta_1$ 与 $\theta_j=(1-\theta_1)\phi_j$（$j\ge2$）把单纯形参数化，其中 $(\phi_2,\dots,\phi_k)$ 属于单纯形 $\Delta_{k-1}$；Jacobi 行列式为 $(1-\theta_1)^{k-2}$。核的积分变为

   $$
   \int_0^1\theta_1^{-1}(1-\theta_1)^{\sum_{j\ge2}(y_j-1)+k-2}\,\mathrm{d}\theta_1\cdot\int_{\Delta_{k-1}}\prod_{j\ge2}\phi_j^{y_j-1}\,\mathrm{d}\boldsymbol{\phi}=\int_0^1\theta_1^{-1}(1-\theta_1)^{n-1}\,\mathrm{d}\theta_1\cdot\int_{\Delta_{k-1}}\prod_{j\ge2}\phi_j^{y_j-1}\,\mathrm{d}\boldsymbol{\phi},
   $$
   第一个因子在 $\theta_1=0$ 处发散，第二个为正（可能为无穷）。所以后验不正常。这是 $y=0$ 时不正常的 $\mathrm{Beta}(0,0)$ 后验的多项版本（[3.7.2](/3.7.2)）。
