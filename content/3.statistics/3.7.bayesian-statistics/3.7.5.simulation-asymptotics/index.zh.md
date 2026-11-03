---
title: 后验模拟与大样本理论
description: 由模拟样本了解后验（参数的函数、联合与边缘抽样），离散格点抽样，后验众数处的正态近似，后验相合性与 Bernstein–von Mises 定理，贝叶斯与频率学派的渐近理论，渐近理论失效的情形，以及多个正态均值问题、Stein 的不可容许性结果、James–Stein 估计及其经验贝叶斯解释。
source_hash: bc3be1dcdcca
---

模型与先验一经确定，后验分布也就确定了，但仅有公式往往没有用处。我们想要它的均值与分位数、参数的函数的后验、预测，以及诸如 $\theta>3$ 这类陈述的概率。[3.7.1](/3.7.1)–[3.7.3](/3.7.3) 的共轭模型对其中一部分给出闭式解；多数模型则不能。本章发展两种互补的工具。第一种是模拟：来自后验的一组样本通过取平均回答所有这类问题（§5.1），并且在一维或二维时，可以在格点上对任何可计算的密度产生样本（§5.2）。第二种是渐近理论：数据很多时，后验近似为正态（§5.3），集中在参数的真值附近（§5.4），并与频率学派的大样本理论一致，只有实际中反复出现的若干情形除外（§5.5）。本章最后讨论估计多个正态均值的问题（§5.6）：显然的估计量在高维时失效，而被解释为经验贝叶斯规则的收缩估计，直接导向 [3.7.6](/3.7.6) 的层次模型。

这里的模拟方法产生独立样本，不需要迭代。迭代方法，即 **Markov 链 Monte Carlo** 与 **Gibbs 抽样**，在 [3.5.9](/3.5.9) 讨论，当后验无法化为一维或二维时就需要它们。与之前一样，$\Gamma(\alpha,\beta)$ 的形状为 $\alpha$，速率为 $\beta$。

## 5.1. 由模拟了解后验

设我们能从 $p(\theta\mid y)$ 中独立地抽取 $\theta^1,\dots,\theta^S$。于是每个后验概括量都用样本的相应概括量来估计：$\mathbb{E}(\theta\mid y)$ 用平均值，$\mathbb{P}(\theta\in A\mid y)$ 用落在 $A$ 中的样本比例，分位数与中心后验区间用经验分位数。这就是应用于后验的 **Monte Carlo 方法**（[3.1.12](/3.1.12)）：由**大数定律**，估计随 $S\to\infty$ 收敛，Monte Carlo 误差的量级为 $S^{-1/2}$，所以几千个样本就足以应付多数概括量。模拟的真正优势在于，在解析上很麻烦的问题变得轻而易举。

### 5.1.1. 例：空调故障

**例 5.1.1（空调故障）** Proschan（1963）记录了 13 架 Boeing 720 飞机空调系统相继两次故障之间的时间。对编号为 7910 的飞机，$n=15$ 个间隔（单位为小时）为

$$
74,\ 57,\ 48,\ 29,\ 502,\ 12,\ 70,\ 21,\ 29,\ 386,\ 59,\ 27,\ 153,\ 26,\ 326,
$$
总和 $n\bar y=1819$，均值 $\bar y=121.27$。把它们建模为 $y_i\mid\theta\overset{\text{iid}}{\sim}\mathrm{Exp}(\theta)$，其中 $\theta=1/\mathbb{E}(y\mid\theta)$ 是故障率（每小时的故障数）。似然为

$$
p(y\mid\theta)=\prod_{i=1}^n\theta\mathrm{e}^{-\theta y_i}=\theta^n\mathrm{e}^{-n\bar y\theta},
$$
**极大似然估计**量为 $\hat\theta=1/\bar y=0.00825$，约每运行 1000 小时发生 8 次故障。Gamma 族是共轭的（[3.7.2](/3.7.2)，§2.1）：取 $\theta\sim\Gamma(\alpha,\beta)$，

$$
p(\theta\mid y)\propto\theta^n\mathrm{e}^{-n\bar y\theta}\,\theta^{\alpha-1}\mathrm{e}^{-\beta\theta}=\theta^{\alpha+n-1}\mathrm{e}^{-(\beta+n\bar y)\theta},\qquad\theta\mid y\sim\Gamma(\alpha+n,\,\beta+n\bar y).
$$
更新把间隔个数加到形状上，把它们的总长度加到速率上。因此相对于平坦先验 $\Gamma(1,0)$，先验 $\Gamma(\alpha,\beta)$ 相当于总计 $\beta$ 小时的 $\alpha-1$ 个指数观测；相对于尺度不变先验 $p(\theta)\propto1/\theta$，即 $\Gamma(0,0)$，它相当于 $\alpha$ 个观测。

其他飞机提供了先验信息。其中四架飞机的 $\theta$ 的极大似然估计平均约为 $0.009$，标准差为 $0.003$。匹配 Gamma 分布的均值 $\alpha/\beta$ 与方差 $\alpha/\beta^2$，得 $\alpha=(0.009/0.003)^2=9$，$\beta=0.009/0.003^2=1000$，相当于总计 $1000$ 小时的 8 个故障间隔。为了看答案对这一选择的依赖程度，我们还使用一个较弱的先验，相当于一半数量的间隔、一半的时间，$\alpha=5$，$\beta=500$：

| 先验 | 先验均值 | 先验标准差 | 后验 | 后验均值 | 后验标准差 |
|---|---|---|---|---|---|
| 强，$\Gamma(9,1000)$ | 0.0090 | 0.0030 | $\Gamma(24,2819)$ | 0.00851 | 0.00174 |
| 弱，$\Gamma(5,500)$ | 0.0100 | 0.0045 | $\Gamma(20,2319)$ | 0.00862 | 0.00193 |

两个后验均值都介于先验均值与 $\hat\theta=0.00825$ 之间，并接近后者，两个分析的差别只有后验标准差的一小部分：十五个观测已经压倒了任何一个先验。

![7910 号飞机的空调故障。左图与中图：强先验 Gamma(9, 1000) 与弱先验 Gamma(5, 500) 下故障率的先验、归一化的似然与后验。右图：强先验下平均故障间隔时间 1/θ 的 10000 个模拟值，以及精确的逆 Gamma 密度。](./plots/ac_failures.py)

### 5.1.2. 参数的函数

**命题 5.1.1** 若 $\theta^1,\dots,\theta^S\overset{\text{iid}}{\sim}p(\theta\mid y)$，$\lambda=h(\theta)$，其中 $h$ 是某个函数，则 $\lambda^s=h(\theta^s)$，$s=1,\dots,S$ 是来自后验 $p(\lambda\mid y)$ 的独立样本。

**证明** $\lambda^s$ 是独立随机变量的函数，因而相互独立，并且每个都具有 $\theta\sim p(\theta\mid y)$ 时 $h(\theta)$ 的分布，按定义这就是 $p(\lambda\mid y)$。$\square$

不需要变量替换公式：只需把每个样本变换一下。特别地，$\bar\lambda=\frac1S\sum_sh(\theta^s)$ 是 $\mathbb{E}[h(\theta)\mid y]$ 的无偏估计，并由大数定律是相合估计。

在例 5.1.1 中，实际关心的量是平均故障间隔时间 $\lambda=1/\theta=\mathbb{E}(y\mid\theta)$，对指数模型，它也是故障间隔时间的标准差。这里可以得到精确的答案：$1/\theta$ 服从**逆 Gamma 分布**（[3.7.2](/3.7.2)，定义 2.4.1），在强先验下 $\lambda\mid y\sim\mathrm{Inv}\text{-}\Gamma(24,2819)$，均值为 $2819/23=122.6$ 小时，中位数为 $119.1$，$95\%$ 中心后验区间为 $[81.7,183.3]$。对一万个 Gamma 样本取倒数，得到均值 $122.3$ 与区间 $[81.6,183.6]$，并且 $\lambda>100$ 的样本比例估计 $\mathbb{P}(\lambda>100\mid y)=0.81$。注意 $\mathbb{E}(1/\theta\mid y)=122.6$ 不同于 $1/\mathbb{E}(\theta\mid y)=117.5$：后验概括量不与非线性函数交换，而模拟自动处理了这一点。模拟也回答没有简单闭式的问题，例如下一个间隔超过 $200$ 小时的概率 $h(\theta)=\mathrm{e}^{-200\theta}$ 的后验分布。

### 5.1.3. 从联合分布与边缘分布抽样

多参数后验通常通过分解 $p(\theta_1,\theta_2\mid y)=p(\theta_2\mid y)\,p(\theta_1\mid\theta_2,y)$ 得知，其中两个因子都是标准分布，尽管边缘分布 $p(\theta_1\mid y)$ 可能不是（[3.7.3](/3.7.3)）。模拟直接利用这一点。用 $(X,Y)$ 表示联合密度为 $p(x,y)=p(x)p(y\mid x)$ 的一般的一对变量。

**命题 5.1.2** 对 $i=1,\dots,m$ 独立地抽取 $x_i\sim p(x)$，再抽取 $y_i\sim p(y\mid x_i)$。则这些对 $(x_i,y_i)$ 是来自 $p(x,y)$ 的独立样本，并且仅 $y_1,\dots,y_m$ 就是来自**边缘分布** $p(y)=\int p(x,y)\,\mathrm{d}x$ 的独立样本。

**证明** 按构造，对 $(x_i,y_i)$ 的密度为 $p(x)p(y\mid x)=p(x,y)$。为了就样本的用途来看这一点，考虑联合**经验分布函数**

$$
\hat F(x,y)=\frac1m\sum_{i=1}^m\boldsymbol{1}\{x_i\le x\}\boldsymbol{1}\{y_i\le y\}.
$$
每个加项的期望为

$$
\mathbb{E}\big[\boldsymbol{1}\{x_i\le x\}\boldsymbol{1}\{y_i\le y\}\big]=\int_{-\infty}^x\int_{-\infty}^yp(y'\mid x')\,p(x')\,\mathrm{d}y'\,\mathrm{d}x'=\mathbb{P}(X\le x,Y\le y)=F(x,y),
$$
所以 $\hat F(x,y)$ 是联合分布函数 $F(x,y)$ 的无偏估计，方差为 $F(x,y)[1-F(x,y)]/m\to0$，并且由大数定律，当 $m\to\infty$ 时 $\hat F(x,y)\to F(x,y)$。对单独的 $y_i$，取 $\hat F(y)=\frac1m\sum_i\boldsymbol{1}\{y_i\le y\}$：每个加项的期望为 $\mathbb{P}(y_i\le y)=\int p(x)\int_{-\infty}^yp(y'\mid x)\,\mathrm{d}y'\,\mathrm{d}x=F(y)$，即边缘分布函数，同样的论证适用。$\square$

因此，丢弃联合样本的某个分量就是把它积分掉在模拟中的对应操作。由于边缘分布从未被计算过，即使积分没有闭式，这种做法也行得通。

**例 5.1.2（共轭先验下的正态模型）** 对 $y_i\mid\mu,\sigma^2\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$，取共轭先验 $\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2)$，$\mu\mid\sigma^2\sim\mathcal{N}(\mu_0,\sigma^2/\kappa_0)$，联合后验具有同样的形式，参数更新为 $(\mu_n,\kappa_n,\nu_n,\sigma_n^2)$（[3.7.3](/3.7.3)）：

$$
\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(\nu_n,\sigma_n^2),\qquad\mu\mid\sigma^2,y\sim\mathcal{N}(\mu_n,\sigma^2/\kappa_n).
$$
为了模拟，先从**尺度逆卡方分布**抽 $(\sigma^2)^s$（取 $\nu_n\sigma_n^2/Z$，$Z\sim\chi^2_{\nu_n}$），再从 $\mathcal{N}(\mu_n,(\sigma^2)^s/\kappa_n)$ 抽 $\mu^s$。这些对是来自联合后验的样本；仅 $\mu^s$ 就是来自边缘后验 $t_{\nu_n}(\mu_n,\sigma_n^2/\kappa_n)$ 的样本，且无需积分。再多一步 $\tilde y^s\sim\mathcal{N}(\mu^s,(\sigma^2)^s)$，就得到新观测的**后验预测分布**的样本。

## 5.2. 离散格点抽样

当先验不是共轭的时，后验仍可计算到一个常数，$q(\theta)=p(\theta)p(y\mid\theta)\propto p(\theta\mid y)$，但它不再属于我们可以抽样的族。一个简单的例子是半共轭先验下的正态模型，其中 $\mu$ 与 $\sigma^2$ 在先验中独立，

$$
\mu\sim\mathcal{N}(\mu_0,\tau_0^2),\qquad\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2),
$$
它的联合后验不具有正态–逆卡方的形式，因为 $\mu$ 的先验方差不再随 $\sigma^2$ 缩放。在一维或二维时，最简单的一般方法是在格点上用离散分布代替连续分布。

**算法 5.2.1（格点抽样）** 从后验 $p(\alpha,\beta\mid y)\propto q(\alpha,\beta)$ 抽取 $S$ 个值：

1. 经过一些试验（例如围绕众数，在每个方向取若干个近似后验标准差），选取一个几乎包含全部后验质量的矩形范围。
2. 在覆盖该范围、间距为 $\Delta_\alpha$、$\Delta_\beta$ 的格点的点 $(\alpha_i,\beta_k)$ 上计算 $q$。
3. 归一化：$p_{ik}=q(\alpha_i,\beta_k)/\sum_{i',k'}q(\alpha_{i'},\beta_{k'})$，这是格点上的离散分布。
4. 对 $\beta$ 求和，计算 $\alpha$ 的边缘分布：$p(\alpha_i\mid y)=\sum_kp_{ik}$。
5. 对 $s=1,\dots,S$：
   1. 从离散分布 $p(\alpha_i\mid y)$ 抽取 $\alpha^s$，这是**逆变换法**的离散版本；
   2. 给定刚抽得的值，从离散条件分布 $p(\beta_k\mid\alpha^s,y)=p_{ik}/p(\alpha_i\mid y)$ 抽取 $\beta^s$；
   3. 给 $\alpha^s$ 与 $\beta^s$ 分别加上 $(-\Delta_\alpha/2,\Delta_\alpha/2)$ 与 $(-\Delta_\beta/2,\Delta_\beta/2)$ 上的独立均匀扰动，使样本具有连续分布。

第 4 步与第 5 步就是把命题 5.1.2 应用于离散近似。实际中计算的是 $\log q$，在取指数之前减去它的最大值，因为 $q$ 本身可能下溢。格点最好布置在后验大致对称且无界的尺度上，如 $\log\sigma$ 或 $\operatorname{logit}\theta$；此时必须计算的是新尺度上的密度，包含变换的 Jacobi 因子（[3.7.6](/3.7.6)，§6.5）。

**例 5.2.1** 取格点 $\alpha\in\{0,0.2,0.4,0.6,0.8,1\}$，$\beta\in\{0.3,0.6,0.9\}$，设 $18$ 个未归一化的值 $q(\alpha_i,\beta_k)$ 之和为 $200$，且 $q(0.4,0.9)=4$，$q(0.8,0.6)=8$，$q(0.6,0.3)=6$。归一化后，$p(0.4,0.9\mid y)=4/200=0.02$，$p(0.8,0.6\mid y)=0.04$，$p(0.6,0.3\mid y)=0.03$。设对每列求和得到六个 $\alpha$ 值的边缘分布 $p(\alpha\mid y)=(0.1,0.2,0.2,0.1,0.3,0.1)$。一次抽样先按这些概率选一列；若选中 $\alpha=0.4$，则以条件概率 $0.02/0.2=0.1$ 选取 $\beta=0.9$。

![独立先验 μ ~ N(5, 2²) 与 σ² ~ Inv-χ²(3, 4) 下正态模型的格点抽样，12 个观测由 N(10, 2²) 模拟。左图：在 201 × 217 格点上计算的 (μ, σ) 的后验密度等高线。右图：由算法 5.2.1 得到的 1000 个样本。](./plots/grid_sampling.py)

格点的代价随维数指数增长：每个参数取 $K$ 个点需要 $K^d$ 次计算。因此格点抽样只有在问题已经化为一维或二维之后才有用，而这常常是可以做到的。若条件后验 $p(\theta_1\mid\theta_2,y)$ 是标准分布，则对 $\theta_1$ 的任何取值

$$
p(\theta_2\mid y)=\frac{p(\theta_1,\theta_2\mid y)}{p(\theta_1\mid\theta_2,y)},
$$
所以 $\theta_2$ 的边缘分布可以逐点计算，只需要对 $\theta_2$ 取格点；然后 $\theta_1$ 从它的条件分布中精确抽取。对半共轭的正态模型，给定 $\sigma^2$，问题就是方差已知的正态均值（[3.7.2](/3.7.2)，§2.3），所以 $\mu\mid\sigma^2,y\sim\mathcal{N}(\mu_n,\tau_n^2)$，其中

$$
\frac1{\tau_n^2}=\frac1{\tau_0^2}+\frac n{\sigma^2},\qquad\mu_n=\tau_n^2\Big(\frac{\mu_0}{\tau_0^2}+\frac{n\bar y}{\sigma^2}\Big),
$$
两者都依赖于 $\sigma^2$。在 $\mu=\mu_n$ 处计算这个比值，此时分母中的正态密度等于 $(2\pi\tau_n^2)^{-1/2}$，得到一维的边缘分布

$$
p(\sigma^2\mid y)\propto p(\sigma^2)\,\tau_n\,(\sigma^2)^{-n/2}\exp\Big(-\frac{(\mu_n-\mu_0)^2}{2\tau_0^2}-\frac{\sum_{i=1}^n(y_i-\mu_n)^2}{2\sigma^2}\Big),
$$
对它在一维格点上抽样；每抽一个 $\sigma^2$ 之后，再精确地抽一个正态的 $\mu$。同样的技巧，以超参数代替 $\sigma^2$ 的角色，是 [3.7.6](/3.7.6) 中层次模型计算的基础。

## 5.3. 后验的正态近似

### 5.3.1. 近似

若后验是单峰且大致对称的，用正态分布来近似它是很自然的。在后验众数 $\hat\theta$ 附近把 $\log p(\theta\mid y)$ 作 Taylor 展开：

$$
\log p(\theta\mid y)=\log p(\hat\theta\mid y)+\Big[\frac{\mathrm{d}}{\mathrm{d}\theta}\log p(\theta\mid y)\Big]^{\mathsf T}_{\theta=\hat\theta}(\theta-\hat\theta)+\frac12(\theta-\hat\theta)^{\mathsf T}\Big[\frac{\mathrm{d}^2}{\mathrm{d}\theta^2}\log p(\theta\mid y)\Big]_{\theta=\hat\theta}(\theta-\hat\theta)+\cdots.
$$
在内部的众数处，线性项为零。常数项只起归一化作用，二次项是正态核的对数。

**定义 5.3.1（正态近似）** 设 $\hat\theta$ 是后验众数，

$$
I(\theta)=-\frac{\mathrm{d}^2}{\mathrm{d}\theta^2}\log p(\theta\mid y)
$$
是观测信息（当 $\theta$ 是向量时为矩阵）。后验的**正态近似**为

$$
p(\theta\mid y)\approx\mathcal{N}\big(\hat\theta,\,[I(\hat\theta)]^{-1}\big).
$$

在平坦先验下，$\hat\theta$ 是极大似然估计，$I(\hat\theta)$ 是似然的**观测信息**（[3.5.5](/3.5.5)）。在本课程中，$J(\theta)$ 表示单个观测的期望 **Fisher 信息量**，如 [3.7.2](/3.7.2)，$I(\theta)$ 表示整个后验的观测信息。众数与 $I(\hat\theta)$ 可由 [3.5.4](/3.5.4)–[3.5.5](/3.5.5) 的优化方法求得；对单参数模型，通常可以手算。

### 5.3.2. 例

**例 5.3.1（二项模型）** 设 $y\mid\theta\sim\mathrm{Bin}(n,\theta)$，先验为 $\mathrm{Beta}(\alpha,\beta)$，后验为 $\mathrm{Beta}(\alpha+y,\beta+n-y)$，且

$$
\begin{aligned}
\log p(\theta\mid y)&=\text{const}+(\alpha+y-1)\log\theta+(\beta+n-y-1)\log(1-\theta),\\
\frac{\mathrm{d}}{\mathrm{d}\theta}\log p(\theta\mid y)&=\frac{\alpha+y-1}{\theta}-\frac{\beta+n-y-1}{1-\theta},\\
\frac{\mathrm{d}^2}{\mathrm{d}\theta^2}\log p(\theta\mid y)&=-\frac{\alpha+y-1}{\theta^2}-\frac{\beta+n-y-1}{(1-\theta)^2}.
\end{aligned}
$$
众数为 $\hat\theta=\frac{\alpha+y-1}{\alpha+\beta+n-2}$。由于 $\alpha+y-1=(\alpha+\beta+n-2)\hat\theta$，$\beta+n-y-1=(\alpha+\beta+n-2)(1-\hat\theta)$，众数处的观测信息为

$$
I(\hat\theta)=\frac{\alpha+\beta+n-2}{\hat\theta}+\frac{\alpha+\beta+n-2}{1-\hat\theta}=\frac{\alpha+\beta+n-2}{\hat\theta(1-\hat\theta)},\qquad p(\theta\mid y)\approx\mathcal{N}\Big(\hat\theta,\frac{\hat\theta(1-\hat\theta)}{\alpha+\beta+n-2}\Big).
$$
取均匀先验时，这是 $\mathcal{N}\big(\frac yn,\frac{(y/n)(1-y/n)}{n}\big)$，即样本比例熟悉的大样本分布，现在读作关于 $\theta$ 的陈述。

考虑 $n=41$ 次试验中有 $y=37$ 次成功。

- *先验 $\mathrm{Beta}(3,3)$。* 后验为 $\mathrm{Beta}(40,7)$，$\hat\theta=39/45=0.8667$，$I(\hat\theta)=45^3/(39\cdot6)=389.42$，$[I(\hat\theta)]^{-1/2}=0.0507$。近似的 $95\%$ 区间 $[0.767,0.966]$ 相对于精确的中心区间 $[0.737,0.937]$ 向右偏移：精确的后验向左偏斜，偏向内部，而正态近似甚至在 $\theta=1$ 之上放了 $0.004$ 的概率。
- *混合先验 $\frac12\mathrm{Beta}(8,2)+\frac12\mathrm{Beta}(2,8)$。* 这个双峰先验表达了 $\theta$ 要么大要么小的信念。由共轭先验混合的更新规则（[3.7.1](/3.7.1)，命题 1.6.1），后验是 $\mathrm{Beta}(45,6)$ 与 $\mathrm{Beta}(39,12)$ 的混合，权重正比于 $\mathrm{B}(45,6)/\mathrm{B}(8,2)$ 与 $\mathrm{B}(39,12)/\mathrm{B}(2,8)$，其比为 $15279:1$。数据选中了第一个分量：后验是单峰的，实际上就是 $\mathrm{Beta}(45,6)$，$\hat\theta=44/49=0.8980$，$I(\hat\theta)=534.8$，$[I(\hat\theta)]^{-1/2}=0.0432$，正态近似与之前一样好。
- *同一混合先验、数据含糊*：$n=10$ 中 $y=5$。此时由对称性两个分量都保持权重 $\frac12$，后验是双峰的，众数在 $0.34$ 与 $0.66$ 附近，以任一众数为中心的正态近似都漏掉了一半的后验质量。

![二项数据的精确后验（实线）与众数处的正态近似（虚线）。左图：Beta(3, 3) 先验，y = 37，n = 41。中图：同样数据下的混合先验 ½Beta(8, 2) + ½Beta(2, 8)；后验基本上就是 Beta(45, 6)。右图：y = 5，n = 10 的混合先验；后验是双峰的，近似失效。](./plots/normal_approximation.py)

因此，“单峰且大致对称”这一要求是本质的。当观测数很大时通常能满足它，下面的例子表明了这一点：取先验 $\mathrm{Beta}(10,10)$ 与固定的观测比例 $y/n=0.1$，精确后验与近似后验在 $n=50$ 时有明显差别（后验标准差精确值为 $0.0487$，近似值为 $0.0490$，但形状偏斜），而在 $n=400$ 时几乎无法区分，此时后验为 $\mathrm{Beta}(50,370)$，标准差为 $0.0158$。

**例 5.3.2（均值与方差都未知的正态模型）** 设 $y_i\mid\mu,\sigma\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$，取在 $(\mu,\log\sigma)$ 上均匀的无信息先验，等价于 $p(\mu,\sigma^2)\propto\sigma^{-2}$（[3.7.3](/3.7.3)）。记 $s^2=\frac1{n-1}\sum_i(y_i-\bar y)^2$，

$$
\log p(\mu,\log\sigma\mid y)=\text{const}-n\log\sigma-\frac{1}{2\sigma^2}\big[(n-1)s^2+n(\bar y-\mu)^2\big].
$$
一阶导数为

$$
\frac{\partial}{\partial\mu}\log p=\frac{n(\bar y-\mu)}{\sigma^2},\qquad\frac{\partial}{\partial(\log\sigma)}\log p=-n+\frac{(n-1)s^2+n(\bar y-\mu)^2}{\sigma^2},
$$
所以众数为 $(\hat\mu,\log\hat\sigma)=\big(\bar y,\log\big(\sqrt{(n-1)/n}\,s\big)\big)$。二阶导数为

$$
\frac{\partial^2}{\partial\mu^2}\log p=-\frac n{\sigma^2},\qquad\frac{\partial^2}{\partial\mu\,\partial(\log\sigma)}\log p=-\frac{2n(\bar y-\mu)}{\sigma^2},\qquad\frac{\partial^2}{\partial(\log\sigma)^2}\log p=-\frac{2}{\sigma^2}\big[(n-1)s^2+n(\bar y-\mu)^2\big].
$$
在众数处，混合导数为零，且 $(n-1)s^2=n\hat\sigma^2$，所以

$$
I(\hat\mu,\log\hat\sigma)=\begin{bmatrix}n/\hat\sigma^2&0\\0&2n\end{bmatrix},\qquad
\begin{bmatrix}\mu\\\log\sigma\end{bmatrix}\Bigm|y\approx\mathcal{N}_2\left(\begin{bmatrix}\bar y\\\log\hat\sigma\end{bmatrix},\begin{bmatrix}\hat\sigma^2/n&0\\0&1/(2n)\end{bmatrix}\right).
$$
对 $\mu$ 的近似是用正态分布代替精确的边缘分布 $t_{n-1}(\bar y,s^2/n)$，当 $n$ 适度大时它是准确的；对 $\log\sigma$ 的近似远好于对 $\sigma$ 或 $\sigma^2$ 的正态近似，因为 $\log\sigma$ 的取值遍及整条直线，其后验近乎对称。

### 5.3.3. 用途与注意事项

正态近似在若干方面有用。

- 它用一个点估计和一个标准误概括后验，这正是通常报告结果的形式，并且它给出了相对于众数解释后验密度的基准：在等高线图中，高度为最大值的 $\mathrm{e}^{-2}$ 倍的等高线，包含二维正态分布约 $86\%$ 的质量。
- 它把数据约化为少数几个概括量：近似地，后验只通过 $\hat\theta$ 与 $I(\hat\theta)$ 依赖于数据，这与**充分统计量**的精神一致。
- 它是对更复杂计算的检验：在大样本问题中，一个模拟程序的输出若与正态近似严重不符，则程序很可能有错误。它也为 [3.5.9](/3.5.9) 的迭代方法提供起点与建议分布。

两点说明决定了它的准确程度。第一，近似在低维时更准确：联合正态分布的边缘分布是正态的，但边缘分布是正态的并不蕴含联合分布是正态的，所以即使联合后验不是正态的，单个参数的边缘后验也常常接近正态。第二，通过对参数作变换，近似可以大大改进：正参数用对数尺度，概率用 logit 尺度。对有限的 $n$，同一个模型的不同参数化下，近似的接近程度可以相差很大（思考题 1）。

## 5.4. 大样本理论

### 5.4.1. 设定

后验为什么会变成正态的，又是围绕什么变成正态的？考虑一列实验，其中 $y_1,\dots,y_n$ 是来自真实分布 $f$ 的独立样本，用模型 $p(y\mid\theta)$ 与先验 $p(\theta)$ 分析，并令 $n\to\infty$。必须区分两种情形：真实分布属于该参数族，即对某个 $\theta_0$ 有 $f=p(\cdot\mid\theta_0)$，或者不属于。在第二种情形中不存在真参数值，我们需要一个替代：该族中最接近 $f$ 的成员。接近程度由 Kullback–Leibler 信息度量

$$
H(\theta)=\mathbb{E}_f\Big[\log\frac{f(y)}{p(y\mid\theta)}\Big]=\int\log\Big(\frac{f(y)}{p(y\mid\theta)}\Big)f(y)\,\mathrm{d}y,
$$
即从 $f$ 到 $p(\cdot\mid\theta)$ 的 **Kullback–Leibler 散度**。它非负，且仅当两个分布重合时为零。我们假设 $H$ 有唯一的极小点，记之为 $\theta_0$。若 $f=p(\cdot\mid\theta_0)$，则 $H(\theta_0)=0$，这个极小点就是真值，所以这一记号涵盖了两种情形。

### 5.4.2. 相合性

**定义 5.4.1（后验相合性）** 若对 $\theta_0$ 的每个邻域 $A$，当 $n\to\infty$ 时 $\mathbb{P}(\theta\in A\mid y_1,\dots,y_n)\to1$（当 $y_i$ 抽自 $f$ 时以概率一成立），则称后验分布在 $\theta_0$ 处是相合的。这一性质称为**后验相合性**。

**定理 5.4.1（有限参数空间中的相合性）** 设参数空间 $\Theta$ 有限，$\theta_0$ 是 $H$ 的唯一极小点，$\mathbb{P}(\theta=\theta_0)>0$，并且期望 $\mathbb{E}_f\lvert\log p(y\mid\theta)\rvert$ 有限。则

$$
\mathbb{P}(\theta=\theta_0\mid y_1,\dots,y_n)\to1\qquad(n\to\infty).
$$

**证明** 对 $\theta\neq\theta_0$，考虑对数后验优势比

$$
\log\frac{p(\theta\mid y)}{p(\theta_0\mid y)}=\log\frac{p(\theta)}{p(\theta_0)}+\sum_{i=1}^n\log\frac{p(y_i\mid\theta)}{p(y_i\mid\theta_0)}.
$$
若 $p(\theta)=0$，则对每个 $n$ 优势比都是 $0$。否则第一项是有限的常数，因为 $p(\theta_0)>0$。固定 $\theta$ 与 $\theta_0$，和式由 $n$ 个独立同分布的项构成，其均值为

$$
\mathbb{E}_f\Big[\log\frac{p(y_i\mid\theta)}{p(y_i\mid\theta_0)}\Big]=\mathbb{E}_f\Big[\log\frac{f(y_i)}{p(y_i\mid\theta_0)}\Big]-\mathbb{E}_f\Big[\log\frac{f(y_i)}{p(y_i\mid\theta)}\Big]=H(\theta_0)-H(\theta)<0,
$$
由于 $\theta_0$ 是唯一的极小点，所以严格为负。由**强大数定律**，和式以概率一趋于 $-\infty$，因而对数后验优势比也是如此，$p(\theta\mid y)/p(\theta_0\mid y)\to0$。由于 $\theta\ne\theta_0$ 只有有限多个，并且后验概率之和为一，

$$
p(\theta_0\mid y)=\Big(1+\sum_{\theta\ne\theta_0}\frac{p(\theta\mid y)}{p(\theta_0\mid y)}\Big)^{-1}\to1.\qquad\square
$$

证明展示了相合性的驱动力：每个观测平均为反对 $\theta_0$ 的对数优势比贡献 $H(\theta_0)-H(\theta)<0$，一个固定的量，而先验只贡献一次。只要给 $\theta_0$ 赋予正概率，似然最终总会压倒任何先验。在附加条件下，这个结果可以推广到可数无穷的参数空间，并按下面的方式推广到连续的参数。

**定理 5.4.2（连续参数空间中的相合性）** 设 $\theta$ 定义在紧集 $\Theta$ 上，$\theta_0$ 是 $H$ 的唯一极小点，$A$ 是 $\theta_0$ 的邻域，先验概率 $\mathbb{P}(\theta\in A)>0$。则在模型满足正则条件时，当 $n\to\infty$ 有 $\mathbb{P}(\theta\in A\mid y)\to1$。

证明沿用离散情形的思路：紧性使 $\Theta\setminus A$ 可以被有限个小集覆盖，在每个小集上，反对 $A$ 的后验优势比趋于零。对许多模型，$\Theta$ 不是紧的（正态均值的取值遍及 $\mathbb{R}$），但对大多数问题，紧性假设可以放宽。

### 5.4.3. 渐近正态性

相合性说明后验集中在何处；§5.3 的正态近似说明它取什么形状。对数后验为

$$
\log p(\theta\mid y)=\text{const}+\log p(\theta)+\sum_{i=1}^n\log p(y_i\mid\theta).
$$
先验项保持固定，而对数似然关于 $n$ 线性增长：似然压倒先验。因此后验众数 $\hat\theta$ 收敛到 $\theta_0$，并且众数处的曲率为

$$
I(\hat\theta)\approx-\sum_{i=1}^n\frac{\mathrm{d}^2}{\mathrm{d}\theta^2}\log p(y_i\mid\theta)\Big|_{\theta=\hat\theta}\approx n\cdot\mathbb{E}_f\Big[-\frac{\mathrm{d}^2}{\mathrm{d}\theta^2}\log p(y\mid\theta)\Big]_{\theta=\theta_0}=nJ(\theta_0),
$$
这由大数定律得到。当 $f=p(\cdot\mid\theta_0)$ 时，$J(\theta_0)$ 是单个观测的 Fisher 信息量；一般地，它由这个在 $f$ 下的期望定义。

**定理 5.4.3（Bernstein–von Mises 定理）** 设模型是可识别的，$\theta_0$ 是 $\Theta$ 的内点，对数似然在 $\theta_0$ 附近二阶连续可微，$J(\theta_0)$ 正定，并且先验密度在 $\theta_0$ 处连续且为正。则当 $n\to\infty$ 时，$\theta$ 的后验分布趋于正态，均值为 $\theta_0$，方差为 $[nJ(\theta_0)]^{-1}$；更精确地说，$\sqrt n(\theta-\hat\theta)$ 的后验分布（$\hat\theta$ 是后验众数或极大似然估计）按全变差收敛到 $\mathcal{N}\big(0,J(\theta_0)^{-1}\big)$。

实际中 $\theta_0$ 与 $J(\theta_0)$ 是未知的，人们使用定义 5.3.1 的近似 $\mathcal{N}(\hat\theta,[I(\hat\theta)]^{-1})$，它与前者渐近等价。该定理还解释了为什么在大样本中，合理先验之间的选择几乎无关紧要（[3.7.1](/3.7.1)，例 1.6.1）：先验只通过它在 $\theta_0$ 附近的取值进入，而这对后验的影响是 $1/n$ 的量级。

### 5.4.4. 贝叶斯与频率学派的渐近理论

贝叶斯的陈述与经典的极大似然大样本理论几乎完全相同：

$$
\text{贝叶斯：}[I(\hat\theta)]^{1/2}(\theta-\hat\theta)\mid y\;\overset{\cdot}{\sim}\;\mathcal{N}(0,I_d),\qquad
\text{频率学派：}[I(\hat\theta)]^{1/2}(\hat\theta-\theta)\mid\theta\;\overset{\cdot}{\sim}\;\mathcal{N}(0,I_d),
$$
其中 $I_d$ 是单位矩阵。在贝叶斯的陈述中，$\theta$ 是随机的，而后验众数 $\hat\theta$ 在给定数据时是固定的（渐近地它可以换成 $\theta_0$）。在频率学派的陈述中，$\theta$ 固定在真值 $\theta_0$，而极大似然估计 $\hat\theta$ 在实验的重复中是随机的。两个估计相差 $O(1/n)$，近似分布重合。

实际的后果涉及区间。区间 $\hat\theta\pm z_{\alpha/2}[I(\hat\theta)]^{-1/2}$ 既是近似的 $100(1-\alpha)\%$ **可信区间**，也是近似的 $100(1-\alpha)\%$ **置信区间**（Wald 区间）。因此在大样本中，贝叶斯可信区间近似地具有其名义的频率学派覆盖率，而置信区间在平坦先验下可以近似地读作后验概率陈述，尽管两种解释仍然不同。在小样本中，或在定理 5.4.3 的条件不成立时，它们可能相差很大。若模型设定有误，后验仍然集中在 $\theta_0$，方差为 $[nJ(\theta_0)]^{-1}$，而极大似然估计的抽样方差则是另一个“三明治”形式的表达式，所以可信区间不一定具有名义的覆盖率。

## 5.5. 渐近理论失效的情形

§5.4 的定理依赖于一些容易被违反的假设：数据对每个参数都提供信息，参数个数保持固定，后验是正常的，先验在 $\theta_0$ 附近给出正的密度，$\theta_0$ 位于内部，并且所问的问题涉及分布的中心。每一种失效都有典型的例子。

### 5.5.1. 欠识别的模型与不可识别的参数

**定义 5.5.1（可识别性）** 给定数据 $y$，若似然 $p(y\mid\theta)$ 对 $\theta$ 的一个范围内的取值相等，则称该模型是欠识别的。若参数的不同取值给出数据的不同分布，则称该参数是**可识别的**；数据完全不提供其信息的参数称为不可识别的。

**例 5.5.1** 设成对的 $(u,v)$ 服从二元正态分布，

$$
\begin{bmatrix}u\\v\end{bmatrix}\sim\mathcal{N}_2\left(\begin{bmatrix}0\\0\end{bmatrix},\begin{bmatrix}1&\rho\\\rho&1\end{bmatrix}\right),
$$
并设每一对中只观测到两个分量之一，一些对中观测到 $u_1,\dots,u_m$，另一些对中观测到 $v_1,\dots,v_k$。无论 $\rho$ 是多少，每个观测到的分量都服从 $\mathcal{N}(0,1)$，所以记 $\phi$ 为标准正态密度，

$$
p(\rho\mid y)\propto p(\rho)\prod_{i=1}^m\phi(u_i)\prod_{j=1}^k\phi(v_j)\propto p(\rho).
$$
无论作多少观测，后验都等于先验：$\rho$ 是不可识别的。在这类问题中，再多同类的数据也无济于事；需要更好的数据收集（这里是两个分量都被观测到的对），或关于该参数的真正的先验信息。

### 5.5.2. 标签交换

欠识别的一个特殊情形是：对每个数据集，不同的参数值给出相同的似然。这在混合模型中很典型。对两个分量的正态**混合模型**

$$
p(y_i\mid\mu_1,\mu_2,\sigma_1^2,\sigma_2^2,\lambda)=\lambda\frac{1}{\sigma_1\sqrt{2\pi}}\exp\Big(-\frac{(y_i-\mu_1)^2}{2\sigma_1^2}\Big)+(1-\lambda)\frac{1}{\sigma_2\sqrt{2\pi}}\exp\Big(-\frac{(y_i-\mu_2)^2}{2\sigma_2^2}\Big),
$$
交换 $(\mu_1,\sigma_1^2)$ 与 $(\mu_2,\sigma_2^2)$ 并把 $\lambda$ 换成 $1-\lambda$，对任何数据都给出同样的似然。若先验关于两个分量对称，后验就是两个镜像的 $50\%$–$50\%$ 混合。它不可能是正态的（它是双峰的），也不可能收敛到一个点。这种分量的标签不能由数据确定的现象称为**标签交换**（label switching），也称为混叠。通常的补救办法是重新参数化，使重复消失，例如限定 $\mu_1\le\mu_2$。在多维问题中这可能很困难，因为向量没有自然的顺序：可以按某一个坐标对分量排序，而这个坐标可能把它们分开，也可能分不开。

### 5.5.3. 参数个数随样本量增加

定理假设关于每个参数的信息随 $n$ 增长。在模型

$$
y_i\mid\pi_i\sim\mathrm{Bin}(n_i,\pi_i),\qquad\pi_i\sim p(\pi_i),\qquad i=1,2,\dots,
$$
中，先验相互独立，每个新的组带来一个新的参数，而

$$
p(\pi_i\mid y)\propto p(\pi_i)\,\pi_i^{y_i}(1-\pi_i)^{n_i-y_i}
$$
与观测了多少组无关。增加的组只提供关于它们各自的 $\pi_j$ 的信息，$\pi_i$ 的后验不收敛到一点；要做到这一点，需要在同一个 $\pi_i$ 下有更多的 Bernoulli 试验。层次模型（[3.7.6](/3.7.6)）通过一个共同的分布把各个 $\pi_i$ 联系起来，从而改变了这一局面，随着组的累积，该分布的参数的估计精度不断提高。

### 5.5.4. 不正常的后验分布

渐近结果以后验正常为前提；定理 5.4.1 的证明用到了 $\sum_kp(\theta_k\mid y)=1$。**广义先验**可能产生不正常的后验（[3.7.2](/3.7.2)，§2.6），此时理论完全不适用。补救办法很容易：正常的先验总是给出正常的后验。不正常的后验通常是似然性质不好的症状，即似然在某个方向上变平，此时似然分析也会失效（[3.7.6](/3.7.6)，§6.5 给出一个例子）。

### 5.5.5. 先验排除了收敛点

若 $p(\theta)=0$，则 $p(\theta\mid y)=0$。若先验排除了 $\theta_0$，后验就不可能收敛到它；即使收敛，也收敛到先验为正的最近的点。补救办法是 [3.7.1](/3.7.1) §1.6.1 的原则：先验在每个稍微合理的取值处都必须为正。

### 5.5.6. 尾部与边界

渐近正态性是关于后验中心的陈述，它由众数（接近后验均值与中位数）处的 Taylor 展开导出，而不是关于它的尾部的陈述。正态密度按 $\mathrm{e}^{-c\theta^2}$ 衰减，而后验的尾部可能重得多，如 **Cauchy 分布**（当 $\lvert\theta\rvert$ 大时 $p(\theta)\propto\theta^{-2}$）或 **Laplace 分布**（$p(\theta)\propto\mathrm{e}^{-c\lvert\theta\rvert}$）。即使中心被近似得很好，由正态近似算出的尾概率与极端分位数也可能严重错误。

有限样本中也会出现一个相关的问题。正态分布取值于整条直线，而许多参数，如二项概率，取值范围有界。在边界附近，后验是偏斜的，近似会把质量放到参数空间之外（例 5.3.1）。随着 $n$ 增大，后验集中，边界通常不再起作用，因为此时 $\theta_0$ 与它相距许多个后验标准差。例外是 $\theta_0$ 本身就在边界上，如方差分量等于 $0$（[3.7.6](/3.7.6)，§6.6），此时对每个 $n$ 渐近正态性都失效。

## 5.6. 多个正态均值问题与经验贝叶斯

渐近论证让 $n$ 增大而参数个数固定。许多现代问题的结构恰好相反：参数很多，每个参数的观测很少。最简单的这类问题表明，通常的估计量可能很差，并说明了在参数之间汇集信息如何修复它。

设 $x_1,\dots,x_p$ 独立，$x_j\sim\mathcal{N}(\theta_j,\sigma^2)$，$\sigma^2$ 已知，即 $\boldsymbol{x}\sim\mathcal{N}_p(\boldsymbol{\theta},\sigma^2I_p)$，目标是估计 $\boldsymbol{\theta}=(\theta_1,\dots,\theta_p)^{\mathsf T}$。从频率学派的观点看，$\boldsymbol{x}$ 是极大似然估计，也是 $\boldsymbol{\theta}$ 的**无偏估计量**。当 $p$ 很大时，这个看似显然的解在两个方面出了问题。

### 5.6.1. 估计量的长度

从频率学派的观点看，$\boldsymbol{x}\mid\boldsymbol{\theta}\sim\mathcal{N}_p(\boldsymbol{\theta},\sigma^2I_p)$，

$$
\mathbb{E}\big(\|\boldsymbol{x}\|^2\mid\boldsymbol{\theta}\big)=\|\boldsymbol{\theta}\|^2+p\sigma^2.
$$
从几何上看，噪声向量 $\boldsymbol{x}-\boldsymbol{\theta}$ 的长度平方约为 $p\sigma^2$，并且在高维时与 $\boldsymbol{\theta}$ 近乎正交，所以 $\boldsymbol{x}$ 比 $\boldsymbol{\theta}$ 长。概率 $\mathbb{P}(\|\boldsymbol{x}\|>\|\boldsymbol{\theta}\|\mid\boldsymbol{\theta})$ 很高，并且当 $p$ 增大而 $\|\boldsymbol{\theta}\|^2/p$ 有界时趋于 $1$（思考题 6）。

从贝叶斯的观点看，取独立先验 $\theta_j\sim\mathcal{N}(\mu_{0j},\tau_{0j}^2)$，由 [3.7.2](/3.7.2) 的正态均值结果，

$$
\theta_j\mid\boldsymbol{x}\sim\mathcal{N}\Big(\frac{\tau_{0j}^2x_j+\sigma^2\mu_{0j}}{\tau_{0j}^2+\sigma^2},\;\frac{\sigma^2\tau_{0j}^2}{\tau_{0j}^2+\sigma^2}\Big).
$$
令 $\tau_{0j}^2\to\infty$，即平坦先验的极限，得 $\boldsymbol{\theta}\mid\boldsymbol{x}\sim\mathcal{N}_p(\boldsymbol{x},\sigma^2I_p)$，于是

$$
\mathbb{E}\big(\|\boldsymbol{\theta}\|^2\mid\boldsymbol{x}\big)=\|\boldsymbol{x}\|^2+p\sigma^2,
$$
所以后验断言 $\|\boldsymbol{\theta}\|>\|\boldsymbol{x}\|$ 的概率很大。两种观点互相矛盾：观测到 $\boldsymbol{x}$ 之后，抽样的论证说真值很可能比 $\boldsymbol{x}$ 短，平坦先验的后验则说它很可能更长。罪魁祸首是平坦先验。对许多参数取独立的平坦先验，并不是对它们的每个函数都是无信息的：它们使 $\|\boldsymbol{\theta}\|$ 取大值的概率压倒性地大。在高维中，逐个坐标无害的先验，在联合意义下可以有很强的信息。

### 5.6.2. 不可容许性与 James–Stein 估计

要比较估计量 $\tilde{\boldsymbol{\theta}}=\tilde{\boldsymbol{\theta}}(\boldsymbol{x})$，需要一个准则。

**定义 5.6.1（风险函数与可容许性）** 在平方误差损失下，估计量 $\tilde{\boldsymbol{\theta}}$ 的**风险函数**为

$$
R(\tilde{\boldsymbol{\theta}},\boldsymbol{\theta})=\mathbb{E}_{\boldsymbol{\theta}}\|\tilde{\boldsymbol{\theta}}-\boldsymbol{\theta}\|^2=\mathbb{E}_{\boldsymbol{\theta}}\sum_{j=1}^p(\tilde\theta_j-\theta_j)^2,
$$
即总的均方误差，作为真值 $\boldsymbol{\theta}$ 的函数。若对所有 $\boldsymbol{\theta}$ 有 $R(\tilde{\boldsymbol{\theta}}_1,\boldsymbol{\theta})\le R(\tilde{\boldsymbol{\theta}}_2,\boldsymbol{\theta})$，且对某些 $\boldsymbol{\theta}$ 严格不等，则称估计量 $\tilde{\boldsymbol{\theta}}_1$ 优于 $\tilde{\boldsymbol{\theta}}_2$。不被任何其他估计量优于的估计量是**可容许估计**；被优于的估计量是不可容许的。

不可容许的估计量不应使用，因为无论真值如何，另一个估计量至少一样好。$\hat{\boldsymbol{\theta}}_{\mathrm{MLE}}=\boldsymbol{x}$ 的风险是常数，$R(\boldsymbol{x},\boldsymbol{\theta})=\mathbb{E}_{\boldsymbol{\theta}}\|\boldsymbol{x}-\boldsymbol{\theta}\|^2=p\sigma^2$，似乎不言而喻没有什么能一致地胜过它。Stein（1956）证明了当 $p\ge3$ 时它是不可容许的，James 与 Stein（1961）给出了一个明确的占优估计量。不失一般性，令 $\sigma^2=1$（否则除以 $\sigma$）；则 $R(\boldsymbol{x},\boldsymbol{\theta})=p$。

**定义 5.6.2（James–Stein 估计）** 设 $p\ge3$，$\boldsymbol{\mu}\in\mathbb{R}^p$ 是任意固定的向量。**James–Stein 估计**为

$$
\tilde{\boldsymbol{\theta}}_{\mathrm{JS}}=\boldsymbol{\mu}+\Big(1-\frac{p-2}{\|\boldsymbol{x}-\boldsymbol{\mu}\|^2}\Big)(\boldsymbol{x}-\boldsymbol{\mu})=\boldsymbol{x}-\frac{p-2}{\|\boldsymbol{x}-\boldsymbol{\mu}\|^2}(\boldsymbol{x}-\boldsymbol{\mu}).
$$

当 $\boldsymbol{\mu}=\boldsymbol{0}$ 时它是 $\big(1-\frac{p-2}{\|\boldsymbol{x}\|^2}\big)\boldsymbol{x}$，把每个坐标按同一个依赖于数据的比例向 $0$ 收缩。这类把各个单独的估计拉向同一点的估计量，称为**收缩估计**（shrinkage estimator）。

**定理 5.6.1（Stein）** 对 $p\ge3$ 与每个 $\boldsymbol{\theta}$，

$$
R(\tilde{\boldsymbol{\theta}}_{\mathrm{JS}},\boldsymbol{\theta})=p-(p-2)^2\,\mathbb{E}_{\boldsymbol{\theta}}\frac{1}{\|\boldsymbol{x}-\boldsymbol{\mu}\|^2}<p=R(\boldsymbol{x},\boldsymbol{\theta}).
$$
因此在平方误差损失下 $\boldsymbol{x}$ 是不可容许的。

**证明** 我们使用 Stein 恒等式：若 $z\sim\mathcal{N}(\theta,1)$，$g$ 绝对连续且 $\mathbb{E}\lvert g'(z)\rvert<\infty$，则 $\mathbb{E}[(z-\theta)g(z)]=\mathbb{E}[g'(z)]$。这由分部积分得到，因为 $(z-\theta)\phi(z-\theta)=-\frac{\mathrm{d}}{\mathrm{d}z}\phi(z-\theta)$。记 $S=\|\boldsymbol{x}-\boldsymbol{\mu}\|^2$。展开平方，

$$
R(\tilde{\boldsymbol{\theta}}_{\mathrm{JS}},\boldsymbol{\theta})=\mathbb{E}_{\boldsymbol{\theta}}\Big\|\boldsymbol{x}-\boldsymbol{\theta}-\frac{p-2}{S}(\boldsymbol{x}-\boldsymbol{\mu})\Big\|^2
=\mathbb{E}_{\boldsymbol{\theta}}\|\boldsymbol{x}-\boldsymbol{\theta}\|^2+(p-2)^2\,\mathbb{E}_{\boldsymbol{\theta}}\frac{1}{S}-2(p-2)\sum_{i=1}^p\mathbb{E}_{\boldsymbol{\theta}}\frac{(x_i-\mu_i)(x_i-\theta_i)}{S}.
$$
第一项为 $p$。对最后一项，固定其他坐标，对 $x_i$ 应用 Stein 恒等式，取 $g_i(\boldsymbol{x})=(x_i-\mu_i)/S$：

$$
\frac{\partial g_i}{\partial x_i}=\frac{1}{S}-\frac{2(x_i-\mu_i)^2}{S^2},\qquad\sum_{i=1}^p\frac{\partial g_i}{\partial x_i}=\frac pS-\frac2S=\frac{p-2}{S},
$$
所以和式等于 $(p-2)\,\mathbb{E}_{\boldsymbol{\theta}}(1/S)$。对 $p\ge3$，$S$ 是自由度为 $p$ 的非中心卡方变量，$\mathbb{E}_{\boldsymbol{\theta}}(1/S)$ 有限且为正，可积性条件成立。合起来，

$$
R(\tilde{\boldsymbol{\theta}}_{\mathrm{JS}},\boldsymbol{\theta})=p+(p-2)^2\,\mathbb{E}_{\boldsymbol{\theta}}\frac1S-2(p-2)^2\,\mathbb{E}_{\boldsymbol{\theta}}\frac1S=p-(p-2)^2\,\mathbb{E}_{\boldsymbol{\theta}}\frac1S<p.\qquad\square
$$

当 $\boldsymbol{\theta}$ 靠近 $\boldsymbol{\mu}$ 时收益最大。在 $\boldsymbol{\theta}=\boldsymbol{\mu}$ 处，$S\sim\chi^2_p$，$\mathbb{E}(1/S)=1/(p-2)$，所以风险是 $2$ 而不是 $p$；当 $\|\boldsymbol{\theta}-\boldsymbol{\mu}\|\to\infty$ 时，风险增大到 $p$ 但永远达不到。$\boldsymbol{\mu}$ 的选取是任意的：向任何固定点收缩都有帮助，尽管在远离该点处帮助可以忽略。这个结果令人惊讶，因为各个坐标是独立的，并且可能涉及互不相关的量，而把它们合在一个估计中却降低了总风险；它并不是说每个坐标都估计得更好。James–Stein 估计本身也是不可容许的：当 $S<p-2$ 时它的收缩因子为负，会越过 $\boldsymbol{\mu}$，而正部估计，即把该因子换成 $\max\big(0,1-\frac{p-2}{S}\big)$ 的估计量，优于它。向零收缩也是**岭回归**（[3.3.12](/3.3.12)）的思想。

![单位方差的 p = 10 个正态均值的三个估计量的风险，作为 θ 与收缩点 0 的距离的函数：极大似然估计 x（常数风险 10）、James–Stein 估计（定理 5.6.1 的精确公式）及其正部版本（每点 20000 次模拟）。](./plots/james_stein_risk.py)

### 5.6.3. 经验贝叶斯的解释

James–Stein 估计看起来像一个技巧；贝叶斯的论证解释了它的来源。保持 $\sigma^2=1$，并假设先验

$$
\theta_j\overset{\text{iid}}{\sim}\mathcal{N}(\mu_j,\tau_0^2),\qquad j=1,\dots,p,
$$
其中 $\boldsymbol{\mu}$ 已知，有共同的方差 $\tau_0^2$。则

$$
\theta_j\mid\boldsymbol{x}\sim\mathcal{N}\Big(\frac{\tau_0^2x_j+\mu_j}{\tau_0^2+1},\frac{\tau_0^2}{\tau_0^2+1}\Big),\qquad
\mathbb{E}(\theta_j\mid\boldsymbol{x})=\frac{\mu_j/\tau_0^2+x_j}{1/\tau_0^2+1}=\mu_j+\frac{\tau_0^2}{1+\tau_0^2}(x_j-\mu_j),
$$
后验均值，即平方误差损失下的 Bayes 估计量，为

$$
\hat{\boldsymbol{\theta}}_{\mathrm{Bayes}}=\boldsymbol{\mu}+\Big(1-\frac{1}{1+\tau_0^2}\Big)(\boldsymbol{x}-\boldsymbol{\mu}).
$$
它与 $\tilde{\boldsymbol{\theta}}_{\mathrm{JS}}$ 的形式完全相同，只是收缩比例 $\frac{1}{1+\tau_0^2}$ 取代了 $\frac{p-2}{\|\boldsymbol{x}-\boldsymbol{\mu}\|^2}$。若 $\tau_0^2$ 未知，数据可以估计它。把 $\theta_j$ 积分掉，$x_j$ 边缘地相互独立，$x_j\sim\mathcal{N}(\mu_j,\tau_0^2+1)$，所以 $S=\|\boldsymbol{x}-\boldsymbol{\mu}\|^2\sim(1+\tau_0^2)\chi^2_p$，并且

$$
\mathbb{E}\Big[\sum_{j=1}^p(x_j-\mu_j)^2\Big]=p(1+\tau_0^2),\qquad\mathbb{E}\frac{p-2}{S}=\frac{p-2}{1+\tau_0^2}\,\mathbb{E}\frac{1}{\chi^2_p}=\frac{1}{1+\tau_0^2}.
$$
于是 $\hat\tau_0^2=S/p-1$ 是 $\tau_0^2$ 的无偏估计，$(p-2)/S$ 是收缩比例 $1/(1+\tau_0^2)$ 的无偏（并且当 $p\to\infty$ 时相合）估计。把它代入 Bayes 估计量，就得到 James–Stein 估计。因此 James–Stein 估计是 Bayes 规则的“经验”版本，下面这个方法的名称正由此而来。

**定义 5.6.3（经验贝叶斯）** 考虑这样的模型：参数 $\theta_1,\dots,\theta_p$ 独立地抽自带有未知超参数 $\phi$ 的先验 $p(\theta\mid\phi)$，数据 $x_j\mid\theta_j\sim p(x_j\mid\theta_j)$。**经验贝叶斯**方法由全部数据的边缘分布 $p(\boldsymbol{x}\mid\phi)=\prod_j\int p(x_j\mid\theta_j)p(\theta_j\mid\phi)\,\mathrm{d}\theta_j$ 估计 $\phi$，例如用矩方法或把它最大化，然后把 $\hat\phi$ 当作已知，基于后验 $p(\theta_j\mid\hat\phi,x_j)$ 对每个 $\theta_j$ 作推断。

经验贝叶斯借用了力量：每个 $\theta_j$ 的估计都通过 $\hat\phi$ 使用全部数据，而 James–Stein 定理表明这在频率学派的风险上是有回报的。它的弱点是把估计出的超参数当作已知，忽略了 $\hat\phi$ 的不确定性，并且数据既用来选择先验又用来更新它。完全贝叶斯的替代做法是给 $\phi$ 本身取一个先验并对它积分；这就是 [3.7.6](/3.7.6) 的**分层模型**，同一个正态问题在那里以八所学校的例子重现。经验贝叶斯的大规模应用，如在基因组学中估计成千上万个效应，在 [7.7.20](/7.7.20) 中讨论。

## 小结

| 主题 | 要点 |
|---|---|
| 后验模拟 | 样本 $\theta^s\sim p(\theta\mid y)$ 可估计任何概括量；$h(\theta^s)\sim p(h(\theta)\mid y)$（命题 5.1.1）；$\mathbb{E}(1/\theta\mid y)\ne1/\mathbb{E}(\theta\mid y)$ |
| 联合与边缘 | $x_i\sim p(x)$，$y_i\sim p(y\mid x_i)$ 给出联合样本，仅 $y_i$ 给出边缘样本；由无偏且相合的经验分布函数保证（命题 5.1.2） |
| 指数–Gamma | $\Gamma(\alpha,\beta)\to\Gamma(\alpha+n,\beta+n\bar y)$；$1/\theta\mid y\sim\mathrm{Inv}\text{-}\Gamma(\alpha+n,\beta+n\bar y)$（例 5.1.1） |
| 格点抽样 | 范围、格点上未归一化的密度、归一化、边缘分布、离散的逆分布函数、条件分布、扰动（算法 5.2.1）；用 $p(\theta_2\mid y)=p(\theta_1,\theta_2\mid y)/p(\theta_1\mid\theta_2,y)$ 化为一维 |
| 正态近似 | $p(\theta\mid y)\approx\mathcal{N}(\hat\theta,[I(\hat\theta)]^{-1})$，$I=-\frac{\mathrm{d}^2}{\mathrm{d}\theta^2}\log p(\theta\mid y)$ 在众数处取值（定义 5.3.1）；二项：$\mathcal{N}\big(\hat\theta,\frac{\hat\theta(1-\hat\theta)}{\alpha+\beta+n-2}\big)$；正态：$(\mu,\log\sigma)\approx\mathcal{N}_2\big((\bar y,\log\hat\sigma),\operatorname{diag}(\hat\sigma^2/n,1/(2n))\big)$ |
| 何时有效 | 单峰、大致对称、低维、合适的参数化（对数、logit） |
| 相合性 | $\theta_0$ 使 Kullback–Leibler 信息 $H(\theta)$ 最小；有限 $\Theta$ 时 $\mathbb{P}(\theta=\theta_0\mid y)\to1$（定理 5.4.1），紧 $\Theta$ 时对邻域成立（定理 5.4.2） |
| 渐近正态性 | 似然压倒先验；$\theta\mid y\approx\mathcal{N}(\theta_0,[nJ(\theta_0)]^{-1})$（定理 5.4.3） |
| 贝叶斯与频率学派 | 同样的正态形式，$\theta$ 随机与 $\hat\theta$ 随机；可信区间与置信区间渐近一致 |
| 失效情形 | 不可识别的参数、标签交换、参数随 $n$ 增长、不正常的后验、先验排除 $\theta_0$、重尾、边界（§5.5） |
| 多个正态均值 | $\mathbb{E}\|\boldsymbol{x}\|^2=\|\boldsymbol{\theta}\|^2+p\sigma^2$；$p\ge3$ 时 $\boldsymbol{x}$ 不可容许；$R(\tilde{\boldsymbol{\theta}}_{\mathrm{JS}},\boldsymbol{\theta})=p-(p-2)^2\mathbb{E}(1/S)$（定理 5.6.1） |
| 经验贝叶斯 | Bayes 规则 $\boldsymbol{\mu}+\big(1-\frac1{1+\tau_0^2}\big)(\boldsymbol{x}-\boldsymbol{\mu})$，其中 $\frac{p-2}{S}$ 是 $\frac1{1+\tau_0^2}$ 的无偏估计，得到 James–Stein 估计（定义 5.6.3） |

## 思考题

1. 在例 5.1.1 的强先验下，后验为 $\Gamma(24,2819)$。求 $\theta$ 与 $\phi=\log\theta$ 的正态近似，并把由此得到的 $\theta$ 的 $95\%$ 区间与精确的中心区间 $[0.00545,0.01224]$ 比较。

   **答** 对 $\theta$：$\log p=23\log\theta-2819\theta$，所以 $\hat\theta=23/2819=0.008159$，$I(\hat\theta)=23/\hat\theta^2$，给出 $\mathcal{N}(0.008159,\,0.001701^2)$ 与区间 $[0.00482,0.01149]$，两端都偏左太多。对 $\phi=\log\theta$，密度含有 Jacobi 因子 $\theta$：$\log p(\phi\mid y)=24\phi-2819\mathrm{e}^\phi$，众数为 $\mathrm{e}^{\hat\phi}=24/2819$，$I(\hat\phi)=2819\mathrm{e}^{\hat\phi}=24$。近似 $\phi\mid y\approx\mathcal{N}(\log0.008514,1/24)$ 取指数后给出 $[0.00571,0.01270]$，其端点与精确值的距离约为前者的一半。对数尺度消除了 Gamma 后验的大部分偏斜。
2. 对 $y_1,\dots,y_n\mid\theta\overset{\text{iid}}{\sim}\mathrm{Poi}(\theta)$ 与先验 $\Gamma(\alpha,\beta)$，推导后验的正态近似，并证明它与定理 5.4.3 渐近一致。

   **答** 后验为 $\Gamma(\alpha+n\bar y,\beta+n)$，$\log p=(\alpha+n\bar y-1)\log\theta-(\beta+n)\theta+\text{const}$。众数为 $\hat\theta=\frac{\alpha+n\bar y-1}{\beta+n}$，$I(\hat\theta)=\frac{\alpha+n\bar y-1}{\hat\theta^2}=\frac{(\beta+n)^2}{\alpha+n\bar y-1}$，所以 $\theta\mid y\approx\mathcal{N}\big(\hat\theta,\frac{\alpha+n\bar y-1}{(\beta+n)^2}\big)$。当 $n\to\infty$ 时，$\hat\theta\to\theta_0$，方差 $\approx\bar y/n\approx\theta_0/n$。单个 Poisson 观测的 Fisher 信息量为 $J(\theta)=1/\theta$，所以 $[nJ(\theta_0)]^{-1}=\theta_0/n$，与定理所述一致；先验参数 $\alpha,\beta$ 只影响相对量级为 $1/n$ 的项。
3. Bernoulli 试验的成功概率 $\theta$ 的参数空间为 $\Theta=\{0.3,0.6\}$，先验给每个值的概率为 $\frac12$，而数据实际来自 $\mathrm{Ber}(0.5)$。后验收敛到哪个值？大约需要多少次试验才能使另一个值的后验优势比约为 $1:100$？

   **答** $H(\theta)=\mathbb{E}_f\log f(y)-[0.5\log\theta+0.5\log(1-\theta)]$。方括号在 $\theta=0.3$ 时为 $-0.7803$，在 $\theta=0.6$ 时为 $-0.7136$，所以 $H$ 在 $0.6$ 处较小，$\theta_0=0.6$，即在 Kullback–Leibler 散度意义下最接近真值的模型值（尽管就绝对距离而言，$0.5$ 到两者的距离大致相等）。由定理 5.4.1，后验集中在 $0.6$ 上。每次试验平均使 $0.3$ 对 $0.6$ 的对数优势比改变 $H(0.6)-H(0.3)=-0.0668$，所以期望对数优势比在约 $4.61/0.0668\approx69$ 次试验后达到 $\log0.01=-4.61$。每次试验增量的标准差为 $0.63$，所以对具体的一个序列，实际次数的变化相当大。
4. 证明若 $S\sim c\,\chi^2_p$，$p\ge3$，则 $\mathbb{E}(1/S)=\frac{1}{c(p-2)}$，并推出 James–Stein 估计在 $\boldsymbol{\theta}=\boldsymbol{\mu}$ 处的风险为 $2$。为什么必须有 $p\ge3$？

   **答** 用 $\chi^2_p$ 的密度，$\mathbb{E}(1/Z)=\int_0^\infty\frac{z^{p/2-2}\mathrm{e}^{-z/2}}{2^{p/2}\Gamma(p/2)}\,\mathrm{d}z=\frac{2^{p/2-1}\Gamma(p/2-1)}{2^{p/2}\Gamma(p/2)}=\frac{1}{2(p/2-1)}=\frac1{p-2}$，并且 $\mathbb{E}(1/S)=\mathbb{E}(1/Z)/c$。在 $\boldsymbol{\theta}=\boldsymbol{\mu}$（$\sigma^2=1$）处，$S\sim\chi^2_p$，所以 $R=p-(p-2)^2/(p-2)=2$。当 $p\le2$ 时积分 $\int_0z^{p/2-2}\,\mathrm{d}z$ 发散，$\mathbb{E}(1/S)=\infty$，风险公式失效；事实上 $p=1,2$ 时 $\boldsymbol{x}$ 是可容许的。
5. 对每个模型，说明渐近理论的哪条假设不成立，以及随着更多同类数据的到来后验会怎样。(a) $y_i\mid\theta_1,\theta_2\sim\mathcal{N}(\theta_1+\theta_2,1)$，取独立的正常先验。(b) 取对称先验的两个分量的 Poisson 混合。(c) 二项数据，先验 $\theta\sim\mathrm{U}(0,0.5)$，真值为 $0.6$。(d) 许多外科医生各自的成功率，每人只观测一例手术。

   **答** (a) 只有 $\theta_1+\theta_2$ 是可识别的：它的后验集中在真实的和上，而给定和时 $\theta_1-\theta_2$ 的后验保持为先验所蕴含的分布（不可识别的参数，§5.5.1）。(b) 标签交换：后验仍是双峰的，有两个镜像的峰；对两个均值加顺序约束可恢复单峰的后验（§5.5.2）。(c) 先验排除了收敛点：后验堆积在边界 $0.5$ 处（§5.5.5），并且正态近似在那里失效（§5.5.6）。(d) 参数个数随样本量增长：每位医生的后验基于一例手术，永远不会集中；需要一个在医生之间共享信息的层次模型（§5.5.3）。
6. 设 $\boldsymbol{x}\sim\mathcal{N}_p(\boldsymbol{\theta},I_p)$。证明若 $\|\boldsymbol{\theta}\|^2\le cp$（$c$ 为常数），则当 $p\to\infty$ 时 $\mathbb{P}(\|\boldsymbol{x}\|>\|\boldsymbol{\theta}\|\mid\boldsymbol{\theta})\to1$，并计算 $p=10$，$\|\boldsymbol{\theta}\|^2=10$ 时的值。

   **答** 记 $\boldsymbol{x}=\boldsymbol{\theta}+\boldsymbol{z}$。则 $D=\|\boldsymbol{x}\|^2-\|\boldsymbol{\theta}\|^2=2\boldsymbol{\theta}^{\mathsf T}\boldsymbol{z}+\|\boldsymbol{z}\|^2$ 的均值为 $p$，方差为 $4\|\boldsymbol{\theta}\|^2+2p\le(4c+2)p$（两项不相关，因为 $\boldsymbol{z}$ 的奇数阶矩为零）。由 Chebyshev 不等式，$\mathbb{P}(D\le0)\le\mathbb{P}(\lvert D-p\rvert\ge p)\le(4c+2)/p\to0$。对 $p=10$，$\|\boldsymbol{x}\|^2$ 是非中心参数为 $10$ 的非中心 $\chi^2_{10}$，$\mathbb{P}(\|\boldsymbol{x}\|^2>10)=0.92$：即使在十维中，观测向量在十次中有九次以上比真值长。
7. 在格点抽样（算法 5.2.1）中，为什么要加扰动？应如何检查格点间距与范围？该方法受到什么限制？

   **答** 若不加扰动，每个样本都恰好落在某个格点上，所以样本具有带结的离散分布；在一个格子内加均匀扰动，把每个样本散布到整个格子，得到的连续分布在格点分辨率的精度内近似后验。若归一化后的密度沿格点的边界可以忽略，则范围是合适的（否则质量被截掉，如 [3.7.6](/3.7.6) §6.5 中截断先验的情形）；若把格点加密不改变所关心的概括量，则间距是合适的。该方法受维数限制：每个坐标 $K$ 个点需要 $K^d$ 次计算，所以对 $d\le2$ 或 $3$ 是实用的，除非能通过从条件分布中精确抽取某些参数，把问题化为较少的维数。
8. 在 §5.6.3 的经验贝叶斯设定中，代入的估计 $\hat\tau_0^2=S/p-1$ 可能为负。证明在 Bayes 规则中把 $1/(1+\tau_0^2)$ 换成 $\min\{1,p/S\}$ 得到的估计量接近正部 James–Stein 估计，并解释为什么截断是合理的。

   **答** 取 $\hat\tau_0^2=\max(0,S/p-1)$，收缩比例为 $\frac{1}{1+\hat\tau_0^2}=\min\{1,p/S\}$，估计量为 $\boldsymbol{\mu}+\big(1-\min\{1,p/S\}\big)(\boldsymbol{x}-\boldsymbol{\mu})=\boldsymbol{\mu}+\max\big(0,1-\frac pS\big)(\boldsymbol{x}-\boldsymbol{\mu})$。这就是以 $p$ 代替 $p-2$ 的正部 James–Stein 估计，二者的差别只在 $p$ 小时才有意义。截断是合理的，因为方差不可能为负：当 $S<p$ 时，数据与 $\tau_0^2=0$ 相容，即所有 $\theta_j$ 都等于 $\mu_j$，最好的估计是完全收缩，绝不会越过 $\boldsymbol{\mu}$ 去收缩。
