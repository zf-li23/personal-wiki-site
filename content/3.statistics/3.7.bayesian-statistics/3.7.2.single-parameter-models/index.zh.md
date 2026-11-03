---
title: 单参数模型与先验的分类
description: 带与不带暴露量的 Poisson–Gamma 模型与负二项先验预测分布，方差已知的正态均值及其后验预测，均值已知的正态方差与尺度逆卡方族，指数族的共轭先验，正常与广义先验，Jeffreys 先验，枢轴量与参考先验。
source_hash: 012b4b1757bd
---

单参数模型只有一个未知的标量 $\theta$。这类模型是后面一切内容的基本构件：它们以闭式展示先验与数据如何结合、后验如何用于预测，以及当我们试图表达“无知”时会出什么问题。[3.7.1](/3.7.1) 讨论了带 Beta 先验的二项模型。本章处理其他几个标准模型，即 Poisson 模型（§2.2）、方差已知的正态模型（§2.3）与均值已知的正态模型（§2.4），并指出它们的共轭先验背后的共同结构，即指数族（§2.5）。后半部分继续 [3.7.1](/3.7.1) §1.6 开始的先验分类：在信息共轭先验之后是无信息先验、正常与广义先验（§2.6）、Jeffreys 先验（§2.7）、由枢轴量导出的先验（§2.8）与参考先验（§2.9）。这些模型的多参数版本见 [3.7.3](/3.7.3)；这里用到的所有分布汇总在 [3.7.4](/3.7.4)。

本章中 $\Gamma(\alpha,\beta)$ 表示形状为 $\alpha$、速率为 $\beta$ 的 **Gamma 分布**，其密度为 $\frac{\beta^\alpha}{\Gamma(\alpha)}x^{\alpha-1}\mathrm{e}^{-\beta x}$（$x>0$），均值为 $\alpha/\beta$，方差为 $\alpha/\beta^2$。速率 $\beta$ 是尺度的倒数：$X\sim\Gamma(\alpha,\beta)$ 当且仅当 $\beta X\sim\Gamma(\alpha,1)$。

## 2.1. 标准的单参数模型

| 模型 | $y=(y_1,\dots,y_n)$ 的似然 | 共轭先验 | 后验 |
|---|---|---|---|
| 二项，$y\sim\mathrm{Bin}(n,\theta)$ | $\binom ny\theta^y(1-\theta)^{n-y}$ | $\mathrm{Beta}(\alpha,\beta)$ | $\mathrm{Beta}(\alpha+y,\beta+n-y)$ |
| Poisson，$y_i\sim\mathrm{Poi}(\theta)$ | $\propto\theta^{n\bar y}\mathrm{e}^{-n\theta}$ | $\Gamma(\alpha,\beta)$ | $\Gamma(\alpha+n\bar y,\beta+n)$ |
| 指数，$y_i\sim\mathrm{Exp}(\theta)$ | $\theta^n\mathrm{e}^{-\theta n\bar y}$ | $\Gamma(\alpha,\beta)$ | $\Gamma(\alpha+n,\beta+n\bar y)$ |
| 正态，方差已知，$y_i\sim\mathcal{N}(\theta,\sigma^2)$ | $\propto\exp\big(-\frac{n}{2\sigma^2}(\bar y-\theta)^2\big)$ | $\mathcal{N}(\mu_0,\tau_0^2)$ | $\mathcal{N}(\mu_n,\tau_n^2)$，§2.3 |
| 正态，均值已知，$y_i\sim\mathcal{N}(\theta,\sigma^2)$ | $\propto(\sigma^2)^{-n/2}\exp\big(-\frac{n}{2\sigma^2}v\big)$，$v=\frac1n\sum_i(y_i-\theta)^2$ | $\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2)$ | $\mathrm{Inv}\text{-}\chi^2\big(\nu_0+n,\frac{\nu_0\sigma_0^2+nv}{\nu_0+n}\big)$，§2.4 |

在每种情形中，似然只通过**充分统计量**（$y$、$n\bar y$、$\bar y$ 或 $v$）依赖于数据，共轭先验作为 $\theta$ 的函数与似然具有相同的函数形式。二项一行已在 [3.7.1](/3.7.1) 中推导；指数一行是思考题 6。

## 2.2. Poisson 模型

### 2.2.1. Gamma 共轭先验

对计数 $y_1,\dots,y_n\mid\theta\overset{\text{iid}}{\sim}\mathrm{Poi}(\theta)$，似然为

$$
p(y\mid\theta)=\prod_{i=1}^n\frac{\theta^{y_i}\mathrm{e}^{-\theta}}{y_i!}\propto\theta^{n\bar y}\mathrm{e}^{-n\theta}.
$$
作为 $\theta$ 的函数，它是 Gamma 密度的核，所以 Gamma 族是共轭的：取先验 $p(\theta)\propto\theta^{\alpha-1}\mathrm{e}^{-\beta\theta}$，$\theta\sim\Gamma(\alpha,\beta)$，则

$$
p(\theta\mid y)\propto\theta^{\alpha+n\bar y-1}\mathrm{e}^{-(\beta+n)\theta},\qquad\theta\mid y\sim\Gamma(\alpha+n\bar y,\,\beta+n).
$$
先验可以看成附加的数据：它把一个总计数加到观测总数 $n\bar y$ 上，把一些观测时段数加到 $n$ 上。相对于广义的基准 $p(\theta)\propto\theta^{-1}$（$\Gamma(0,0)$，§2.8 的 Jeffreys 尺度先验），先验 $\Gamma(\alpha,\beta)$ 相当于在 $\beta$ 个时段内总计数为 $\alpha$；相对于平坦的基准 $p(\theta)\propto1$（$\Gamma(1,0)$），它相当于在 $\beta$ 个时段内有 $\alpha-1$ 个计数。后验均值

$$
\mathbb{E}(\theta\mid y)=\frac{\alpha+n\bar y}{\beta+n}=\frac{n}{\beta+n}\,\bar y+\frac{\beta}{\beta+n}\cdot\frac\alpha\beta
$$
同样是样本均值与先验均值的折中，权重为 $n$ 与 $\beta$。

**例 2.2.1（交通事故）** 某校园每周的交通事故数用 $\mathrm{Poi}(\theta)$ 建模。8 周的计数为 $3,2,0,8,2,4,6,1$，所以 $n=8$，$n\bar y=26$，$\bar y=3.25$。先验信息表明每周均值约为 $2.5$，标准差为 $1$。对 Gamma 先验作矩匹配，$\alpha/\beta=2.5$，$\alpha/\beta^2=1$，得 $\beta=2.5$，$\alpha=6.25$：先验相当于在 $2.5$ 周内观测到约 $6$ 起事故。后验为

$$
\theta\mid y\sim\Gamma(6.25+26,\,2.5+8)=\Gamma(32.25,\,10.5),
$$
其概括量为

| 均值 | 中位数 | 众数 | 标准差 | $95\%$ 中心后验区间 | $\mathbb{P}(\theta>3\mid y)$ |
|---|---|---|---|---|---|
| 3.071 | 3.040 | 2.976 | 0.5408 | $[2.104,\,4.219]$ | 0.5296 |

众数为 $(\alpha+n\bar y-1)/(\beta+n)$。诸如 $H_0\colon\theta\le3$ 对 $H_1\colon\theta>3$ 这样的单侧问题，直接由后验概率 $0.53$ 回答：数据对两者几乎一视同仁。点假设 $H_0\colon\theta=3$ 不能这样处理，因为连续的后验给出 $\mathbb{P}(\theta=3\mid y)=0$；它需要一个对 $\theta=3$ 赋予正概率的先验，这就引出**贝叶斯因子**（[3.7.8](/3.7.8)）。

### 2.2.2. 带暴露量的 Poisson 模型

计数常常来自规模不同的单位：人口不同的城市中的死亡数、不同运行时间内的故障数。扩展后的模型为

$$
y_i\mid\theta\sim\mathrm{Poi}(x_i\theta),\qquad i=1,\dots,n,
$$
其中已知的正数 $x_i$ 是单位 $i$ 的暴露量，未知的 $\theta$ 是每单位暴露量的发生率。似然为 $p(y\mid\theta)\propto\theta^{\sum_iy_i}\mathrm{e}^{-\theta\sum_ix_i}$（因子 $x_i^{y_i}$ 不含 $\theta$），Gamma 族仍然是共轭的，并且

$$
\theta\mid y\sim\Gamma\Big(\alpha+\sum_{i=1}^ny_i,\;\beta+\sum_{i=1}^nx_i\Big).
$$

**例 2.2.2（哮喘死亡率）** 一项关于某个 $200{,}000$ 人口城市一年内死因的研究发现 $y=3$ 例死于哮喘，粗发病率为每年每 $100{,}000$ 人 $1.5$ 例。以每年每 $100{,}000$ 人的病例数度量 $\theta$；则暴露量为 $x=2.0$，$y\sim\mathrm{Poi}(2.0\,\theta)$。对可比国家哮喘死亡率的综述表明，高于每 $100{,}000$ 人 $1.5$ 例的发生率是罕见的，典型值约为 $0.6$。均值为 $0.6$、$97.5\%$ 分位数约为 $1.44$ 的 Gamma 先验是 $\Gamma(3.0,5.0)$；它给出 $\mathbb{P}(\theta>1.5)=0.02$。后验为

$$
\theta\mid y\sim\Gamma(3+3,\,5+2)=\Gamma(6,7),
$$
均值为 $0.86$，远低于粗估计 $1.5$：一年里的三例死亡只是微弱的证据，先验把估计强烈地拉向典型值。长期发生率超过 $1$ 的后验概率为 $\mathbb{P}(\theta>1\mid y)=0.30$。若在同一人群中十年里观测到 $y=30$ 例死亡，则暴露量为 $x=20$，后验为 $\Gamma(33,25)$，均值为 $1.32$，$\mathbb{P}(\theta>1\mid y)=0.93$：数据多了十倍，后验大部分移向粗发病率，并且集中得多。

![Poisson–Gamma 更新。左图：交通事故，含先验、归一化的似然与后验。右图：哮喘死亡率，含先验 Gamma(3, 5)，以及一年内 3 例死亡与十年内 30 例死亡之后的后验。](./plots/poisson_gamma.py)

### 2.2.3. 先验预测分布是负二项分布

对单个观测 $y\mid\theta\sim\mathrm{Poi}(\theta)$，$\theta\sim\Gamma(\alpha,\beta)$，后验为 $\Gamma(\alpha+y,\beta+1)$。**先验预测分布** $p(y)=\int p(y\mid\theta)p(\theta)\,\mathrm{d}\theta$ 不必积分就可求得。Bayes 公式 $p(\theta\mid y)=p(y\mid\theta)p(\theta)/p(y)$ 对每个 $\theta$ 成立，所以

$$
p(y)=\frac{p(y\mid\theta)\,p(\theta)}{p(\theta\mid y)}=\frac{\mathrm{Poi}(y\mid\theta)\,\Gamma(\theta\mid\alpha,\beta)}{\Gamma(\theta\mid\alpha+y,\beta+1)}
=\frac{\Gamma(\alpha+y)\,\beta^\alpha}{\Gamma(\alpha)\,y!\,(1+\beta)^{\alpha+y}}
=\binom{\alpha+y-1}{y}\Big(\frac{\beta}{\beta+1}\Big)^\alpha\Big(\frac{1}{\beta+1}\Big)^y,
$$
其中所有含 $\theta$ 的因子都抵消了，并且对实数 $\alpha>0$，$\binom{\alpha+y-1}{y}=\frac{\Gamma(\alpha+y)}{\Gamma(\alpha)\,y!}$。这就是**负二项分布**

$$
y\sim\mathrm{NB}\Big(\alpha,\frac{\beta}{\beta+1}\Big),\qquad y=0,1,2,\dots,
$$
采用 [3.1.6](/3.1.6) 的约定：当 $\alpha$ 为整数时，它是在成功概率为 $\beta/(\beta+1)$ 的独立 Bernoulli 试验中，第 $\alpha$ 次成功之前的失败次数，并且公式可推广到实数 $\alpha>0$。Gelman 等把这个分布写作 $\mathrm{Neg\text{-}bin}(\alpha,\beta)$，直接用 Gamma 的参数来参数化。上面的推导表明，负二项分布是 Poisson 分布的**混合分布**，其均值服从 Gamma 分布。由**全期望公式**与**全方差公式**，

$$
\mathbb{E}y=\mathbb{E}\theta=\frac\alpha\beta,\qquad\operatorname{Var}y=\mathbb{E}\theta+\operatorname{Var}\theta=\frac\alpha\beta+\frac{\alpha}{\beta^2},
$$
所以相对于同均值的 Poisson 分布，这个混合分布是过度离散的；这就是负二项分布成为方差超过均值的计数数据的标准模型的原因。

用后验代替先验，同样的论证给出**后验预测分布**。对暴露量为 $\tilde x$ 的新计数 $\tilde y$，设数据的后验为 $\Gamma(\alpha',\beta')$，$\alpha'=\alpha+\sum_iy_i$，$\beta'=\beta+\sum_ix_i$，则

$$
\tilde y\mid y\sim\mathrm{NB}\Big(\alpha',\frac{\beta'}{\beta'+\tilde x}\Big),
$$
这是因为 $\tilde x\theta\mid y\sim\Gamma(\alpha',\beta'/\tilde x)$。

## 2.3. 方差已知的正态均值

### 2.3.1. 一个观测

设 $y\mid\theta\sim\mathcal{N}(\theta,\sigma^2)$，$\sigma^2$ 已知。作为 $\theta$ 的函数，似然是二次函数的指数，所以共轭族由形如 $p(\theta)=\mathrm{e}^{A\theta^2+B\theta+C}$（$A<0$）的密度构成，也就是正态分布 $\theta\sim\mathcal{N}(\mu_0,\tau_0^2)$：

$$
p(\theta)\propto\exp\Big(-\frac{1}{2\tau_0^2}(\theta-\mu_0)^2\Big).
$$
于是

$$
p(\theta\mid y)\propto\exp\Big(-\frac12\Big[\frac{(y-\theta)^2}{\sigma^2}+\frac{(\theta-\mu_0)^2}{\tau_0^2}\Big]\Big)\propto\exp\Big(-\frac{1}{2\tau_1^2}(\theta-\mu_1)^2\Big),
$$
这由对 $\theta$ 配方得到：括号中 $\theta^2$ 的系数是 $\frac{1}{\sigma^2}+\frac1{\tau_0^2}$，$-2\theta$ 的系数是 $\frac{y}{\sigma^2}+\frac{\mu_0}{\tau_0^2}$。因此 $\theta\mid y\sim\mathcal{N}(\mu_1,\tau_1^2)$，其中

$$
\mu_1=\frac{\frac{1}{\tau_0^2}\mu_0+\frac{1}{\sigma^2}y}{\frac{1}{\tau_0^2}+\frac{1}{\sigma^2}},\qquad\frac{1}{\tau_1^2}=\frac{1}{\tau_0^2}+\frac{1}{\sigma^2}.
$$
方差的倒数称为精度。后验精度是先验精度与数据精度之和，后验均值是先验均值与观测值按精度加权的平均。等价的形式把这种折中表达得更明显：

$$
\mu_1=\mu_0+(y-\mu_0)\frac{\tau_0^2}{\sigma^2+\tau_0^2}=y-(y-\mu_0)\frac{\sigma^2}{\sigma^2+\tau_0^2}:
$$
先验均值向观测值调整，或者观测值向先验均值收缩。

### 2.3.2. 多个观测

对 $y_1,\dots,y_n\mid\theta\overset{\text{iid}}{\sim}\mathcal{N}(\theta,\sigma^2)$，

$$
p(\theta\mid y)\propto p(\theta)\prod_{i=1}^np(y_i\mid\theta)\propto\exp\Big(-\frac12\Big[\frac{(\theta-\mu_0)^2}{\tau_0^2}+\frac{1}{\sigma^2}\sum_{i=1}^n(y_i-\theta)^2\Big]\Big).
$$
由于 $\sum_i(y_i-\theta)^2=\sum_i(y_i-\bar y)^2+n(\bar y-\theta)^2$，后验只通过 $\bar y$ 依赖数据，并且就是把单个观测的结果中的 $y$ 换成 $\bar y\mid\theta\sim\mathcal{N}(\theta,\sigma^2/n)$：

$$
p(\theta\mid y_1,\dots,y_n)=p(\theta\mid\bar y)=\mathcal{N}(\theta\mid\mu_n,\tau_n^2),\qquad
\mu_n=\frac{\frac{1}{\tau_0^2}\mu_0+\frac{n}{\sigma^2}\bar y}{\frac{1}{\tau_0^2}+\frac{n}{\sigma^2}},\qquad
\frac{1}{\tau_n^2}=\frac{1}{\tau_0^2}+\frac{n}{\sigma^2}.
$$
数据精度关于 $n$ 线性增长。记 $\sigma^2=\kappa_0\tau_0^2$，则先验相当于 $\kappa_0$ 个观测，$\mu_n=\frac{\kappa_0\mu_0+n\bar y}{\kappa_0+n}$。

### 2.3.3. 后验预测分布

未来的观测 $\tilde y$ 满足 $\tilde y\mid\theta\sim\mathcal{N}(\theta,\sigma^2)$，在给定 $\theta$ 时与 $y$ 独立。它的后验预测密度为

$$
p(\tilde y\mid y)=\int p(\tilde y\mid\theta)p(\theta\mid y)\,\mathrm{d}\theta\propto\int\exp\Big(-\frac{(\tilde y-\theta)^2}{2\sigma^2}\Big)\exp\Big(-\frac{(\theta-\mu_n)^2}{2\tau_n^2}\Big)\,\mathrm{d}\theta.
$$
被积函数是 $(\tilde y,\theta)$ 的二次型的指数，所以给定 $y$ 时 $(\tilde y,\theta)$ 服从二元正态分布，边缘分布 $\tilde y\mid y$ 是正态的。它的矩由**全期望公式**与**全方差公式**得到：

$$
\begin{aligned}
\mathbb{E}(\tilde y\mid y)&=\mathbb{E}\big[\mathbb{E}(\tilde y\mid\theta,y)\mid y\big]=\mathbb{E}(\theta\mid y)=\mu_n,\\
\operatorname{Var}(\tilde y\mid y)&=\mathbb{E}\big[\operatorname{Var}(\tilde y\mid\theta,y)\mid y\big]+\operatorname{Var}\big[\mathbb{E}(\tilde y\mid\theta,y)\mid y\big]=\sigma^2+\tau_n^2.
\end{aligned}
$$
所以 $\tilde y\mid y\sim\mathcal{N}(\mu_n,\sigma^2+\tau_n^2)$。等价地，$\tilde y=\theta+\varepsilon$，其中 $\theta\mid y\sim\mathcal{N}(\mu_n,\tau_n^2)$，$\varepsilon\sim\mathcal{N}(0,\sigma^2)$ 与之独立。预测方差有两部分：抽样方差 $\sigma^2$，无论数据有多少它都存在；以及关于 $\theta$ 的后验不确定性 $\tau_n^2$，它在 $n\to\infty$ 时消失。在没有任何数据时，单个观测的先验预测分布是 $\mathcal{N}(\mu_0,\sigma^2+\tau_0^2)$，它更宽，因为 $\tau_0^2>\tau_n^2$。

**例 2.3.1（鱼的长度）** 池塘里鱼的长度（单位为厘米）服从 $\mathcal{N}(\theta,2^2)$。先验知识：平均长度约为 $30\,\mathrm{cm}$，平均长度低于 $18$ 或高于 $42\,\mathrm{cm}$ 几乎不可能。把“几乎不可能”理解为三个标准差，则 $\mu_0=30$，$\tau_0=12/3=4$。捕到的 $n=12$ 条鱼的平均长度为 $\bar y=32$。于是

$$
\mu_n=\frac{\frac{1}{4^2}\cdot30+\frac{12}{2^2}\cdot32}{\frac{1}{4^2}+\frac{12}{2^2}}=31.96,\qquad\frac{1}{\tau_n^2}=\frac{1}{4^2}+\frac{12}{2^2}=\frac{1}{0.5714^2},
$$
所以 $\theta\mid y\sim\mathcal{N}(31.96,0.5714^2)$，$95\%$ 中心后验区间为 $31.96\pm1.96\times0.5714=[30.84,33.08]$。数据精度 $3$ 是先验精度 $1/16$ 的 48 倍，所以后验均值接近 $\bar y$。下一条捕到的鱼的长度满足

$$
\tilde y\mid y\sim\mathcal{N}(31.96,\;2^2+0.5714^2)=\mathcal{N}(31.96,\;2.080^2),
$$
$95\%$ 预测区间为 $[27.88,36.04]$。预测分布比 $\theta$ 的后验宽得多，因为单条鱼围绕均值的变化标准差为 $2$；它只比 $\theta$ 已知时的 $\mathcal{N}(\theta,2^2)$ 略宽，因为 $\theta$ 已经被很好地确定。

![鱼长度的例子：平均长度 θ 的先验与后验、单条鱼的先验预测分布，以及下一条鱼的后验预测分布。](./plots/normal_mean_predictive.py)

## 2.4. 均值已知的正态方差

### 2.4.1. 逆 Gamma 分布与逆卡方分布

设 $y_1,\dots,y_n\mid\sigma^2\overset{\text{iid}}{\sim}\mathcal{N}(\theta,\sigma^2)$，均值 $\theta$ 已知。$\sigma^2$ 的似然为

$$
p(y\mid\sigma^2)\propto\sigma^{-n}\exp\Big(-\frac{1}{2\sigma^2}\sum_{i=1}^n(y_i-\theta)^2\Big)=(\sigma^2)^{-n/2}\exp\Big(-\frac{n}{2\sigma^2}v\Big),\qquad v=\frac1n\sum_{i=1}^n(y_i-\theta)^2,
$$
充分统计量为 $v$。作为 $\sigma^2$ 的函数，它是 $\sigma^2$ 的幂乘以 $\exp(-c/\sigma^2)$，也就是下面这个族的核。

**定义 2.4.1（逆 Gamma 分布与逆卡方分布）** 设 $\alpha,\beta>0$。若 $1/X\sim\Gamma(\alpha,\beta)$，则称正随机变量 $X$ 服从**逆 Gamma 分布** $\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$，其密度为

$$
p(x)=\frac{\beta^\alpha}{\Gamma(\alpha)}x^{-(\alpha+1)}\mathrm{e}^{-\beta/x},\qquad x>0,
$$
其中 $\beta$ 是 $X$ 的尺度参数。自由度为 $\nu>0$ 的**逆卡方分布**为 $\mathrm{Inv}\text{-}\chi^2_\nu=\mathrm{Inv}\text{-}\Gamma(\nu/2,1/2)$，即 $Z\sim\chi^2_\nu$ 时 $1/Z$ 的分布。自由度为 $\nu$、尺度为 $s^2>0$ 的**尺度逆卡方分布**为

$$
\mathrm{Inv}\text{-}\chi^2(\nu,s^2)=\mathrm{Inv}\text{-}\Gamma\Big(\frac\nu2,\frac{\nu s^2}{2}\Big),\qquad p(x)\propto x^{-(\nu/2+1)}\exp\Big(-\frac{\nu s^2}{2x}\Big),
$$
即 $Z\sim\chi^2_\nu$ 时 $X=\nu s^2/Z$ 的分布。

密度由变量替换 $x=1/u$，$\lvert\mathrm{d}u/\mathrm{d}x\rvert=x^{-2}$ 得到。矩与众数为

| | $\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$ | $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$ |
|---|---|---|
| 均值 | $\frac{\beta}{\alpha-1}$（$\alpha>1$） | $\frac{\nu}{\nu-2}s^2$（$\nu>2$） |
| 方差 | $\frac{\beta^2}{(\alpha-1)^2(\alpha-2)}$（$\alpha>2$） | $\frac{2\nu^2}{(\nu-2)^2(\nu-4)}s^4$（$\nu>4$） |
| 众数 | $\frac{\beta}{\alpha+1}$ | $\frac{\nu}{\nu+2}s^2$ |

分位数由**卡方分布**的分位数得出，手算时就这样计算。记 $\chi^2_{\nu,p}$ 为 $\chi^2_\nu$ 的上 $p$ 分位数，事件 $X\le\nu s^2/\chi^2_{\nu,p}$ 就是事件 $Z\ge\chi^2_{\nu,p}$，所以 $X\sim\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$ 的下 $p$ 分位数为 $\nu s^2/\chi^2_{\nu,p}$。尺度 $s^2$ 位于众数与均值之间，当 $\nu\to\infty$ 时分布集中在 $s^2$ 处。

![自由度 ν = 1, 2, 3, 5, 10 的逆卡方分布的密度（左），以及 ν = 5、尺度 s² 不同的尺度逆卡方分布的密度（右）。](./plots/inv_chi2_family.py)

### 2.4.2. 共轭更新

取先验 $\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2)$，$p(\sigma^2)\propto(\sigma^2)^{-(\nu_0/2+1)}\exp\big(-\frac{\nu_0\sigma_0^2}{2\sigma^2}\big)$，则

$$
p(\sigma^2\mid y)\propto(\sigma^2)^{-(\nu_0/2+1)}\exp\Big(-\frac{\nu_0\sigma_0^2}{2\sigma^2}\Big)\cdot(\sigma^2)^{-n/2}\exp\Big(-\frac{nv}{2\sigma^2}\Big)
=(\sigma^2)^{-((n+\nu_0)/2+1)}\exp\Big(-\frac{\nu_0\sigma_0^2+nv}{2\sigma^2}\Big),
$$
所以

$$
\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2\Big(\nu_0+n,\;\frac{\nu_0\sigma_0^2+nv}{\nu_0+n}\Big).
$$
先验相当于 $\nu_0$ 个均方偏差为 $\sigma_0^2$ 的观测：自由度相加，后验尺度是先验尺度与数据估计 $v$ 按自由度加权的平均。

**例 2.4.1（奶粉）** 一罐奶粉的重量（克）服从 $\mathcal{N}(1015,\sigma^2)$，均值 $1015$ 已知。$\sigma$ 的合理范围是多少？先验信息是 $\sigma$ 的中位数为 $5\,\mathrm{g}$。取 $\nu_0=1$ 的共轭先验，这是仍为正常先验的最弱者。由于 $\sigma^2=\sigma_0^2/Z$，$Z\sim\chi^2_1$，且 $\sigma^2$ 是 $Z$ 的减函数，$\sigma^2$ 的中位数是 $\sigma_0^2$ 除以 $\chi^2_1$ 的中位数 $0.4549$；令其等于 $5^2$，得

$$
\sigma_0^2=25\times0.4549=11.37,\qquad\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(1,11.37).
$$
$10$ 罐的重量为 $1011,1009,1019,1012,1011,1016,1018,1021,1016,1012$。它们与 $1015$ 的偏差为 $-4,-6,4,-3,-4,1,3,6,1,-3$，所以 $nv=\sum_i(y_i-1015)^2=149$，$v=14.9$（$\sqrt v=3.862$）。后验为

$$
\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2\Big(11,\;\frac{11.37+149}{11}\Big)=\mathrm{Inv}\text{-}\chi^2(11,\;14.58).
$$
$\sigma$ 的后验中位数为 $\sqrt{160.37/\chi^2_{11,0.5}}=\sqrt{160.37/10.34}=3.938$，$\sigma$ 的 $95\%$ 中心后验区间为

$$
\Big[\sqrt{160.37/\chi^2_{11,0.025}},\;\sqrt{160.37/\chi^2_{11,0.975}}\Big]=\Big[\sqrt{160.37/21.92},\;\sqrt{160.37/3.816}\Big]=[2.70,\;6.48].
$$
中位数与中心区间可以直接从 $\sigma^2$ 变换到 $\sigma=\sqrt{\sigma^2}$，因为平方根是递增的。均值与众数则不行：$\sqrt{\mathbb{E}(\sigma^2\mid y)}=\sqrt{160.37/9}=4.221$，$\sqrt{\operatorname{mode}(\sigma^2\mid y)}=\sqrt{160.37/13}=3.512$，而 $\sigma$ 本身的后验均值为 $4.106$，众数为 $3.656$（思考题 5）。与其他先验的比较见例 2.7.1。

## 2.5. 指数族的共轭先验

§2.1–§2.4 的共轭对都是同一种构造的实例。设抽样分布属于**指数族**，

$$
p(y_i\mid\theta)=f(y_i)\exp\big(\boldsymbol{\phi}(\theta)^{\mathsf T}\boldsymbol{u}(y_i)-g(\theta)\big),
$$
其中 $\boldsymbol{\phi}(\theta)$ 是**自然参数**。对 iid 样本 $y=(y_1,\dots,y_n)$，似然为

$$
p(y\mid\theta)=\Big(\prod_{i=1}^nf(y_i)\Big)\exp\Big(\boldsymbol{\phi}(\theta)^{\mathsf T}\sum_{i=1}^n\boldsymbol{u}(y_i)-n\,g(\theta)\Big)\propto\exp\big(\boldsymbol{\phi}(\theta)^{\mathsf T}\boldsymbol{t}(y)-n\,g(\theta)\big),
$$
充分统计量为 $\boldsymbol{t}(y)=\sum_{i=1}^n\boldsymbol{u}(y_i)$。

**命题 2.5.1** 对上述指数族，先验

$$
p(\theta)\propto\exp\big(\boldsymbol{\phi}(\theta)^{\mathsf T}\boldsymbol{\nu}-n_0\,g(\theta)\big),
$$
以使右端可积的超参数 $(\boldsymbol{\nu},n_0)$ 为指标，构成一个共轭族，且后验为

$$
p(\theta\mid y)\propto\exp\big(\boldsymbol{\phi}(\theta)^{\mathsf T}(\boldsymbol{\nu}+\boldsymbol{t}(y))-(n_0+n)\,g(\theta)\big),
$$
即超参数为 $(\boldsymbol{\nu}+\boldsymbol{t}(y),\,n_0+n)$ 的成员。

**证明** 把先验与似然相乘；指数相加。$\square$

这就是 [3.2.7](/3.2.7) 中[定理 7.3.1](/3.2.7#thm-7.3.1) 换一种参数化的形式。超参数的行为类似数据：$n_0$ 是先验样本量，$\boldsymbol{\nu}$ 是充分统计量的先验值。因此指数族的共轭先验总是存在的，并且总可以解释为附加的数据。反过来，除支撑集依赖于 $\theta$ 的不正则情形之外，只有指数族对每个 $n$ 都存在固定维数的充分统计量（Pitman–Koopman–Darmois 定理），从而存在固定维数的自然共轭族。

对 Poisson 模型，$p(y_i\mid\theta)=\frac{1}{y_i!}\exp(y_i\log\theta-\theta)$，所以 $\phi(\theta)=\log\theta$，$u(y_i)=y_i$，$g(\theta)=\theta$，共轭先验为 $\exp(\nu\log\theta-n_0\theta)=\theta^\nu\mathrm{e}^{-n_0\theta}$，即 Gamma 密度 $\Gamma(\nu+1,n_0)$。对只有一个观测的二项模型，$\phi(\theta)=\log\frac{\theta}{1-\theta}$，$u(y)=y$，$g(\theta)=-n\log(1-\theta)$，共轭先验 $\theta^\nu(1-\theta)^{n_0n-\nu}$ 是 Beta 密度。

## 2.6. 无信息先验

### 2.6.1. 动机

当先验分布没有总体基础时，它可能很难构造，因此人们长期希望找到这样的先验：保证它在后验中起最小的作用。这样的**无信息先验**也称为模糊先验、平坦先验或弥散先验。其理由是让数据自己说话，使推断不受当前数据之外的信息影响。

当参数位于有界区间内，如二项概率 $\theta\in[0,1]$ 时，均匀分布是显然的候选，此时后验与似然成比例。当参数在无限区间上取值时，不存在均匀的概率分布。对方差已知的正态均值（§2.3），考虑共轭先验在 $\tau_0^2\to\infty$ 时的极限，此时先验在实直线上越来越平坦。后验公式存在极限：

$$
\mu_n\to\bar y,\qquad\tau_n^2\to\frac{\sigma^2}{n},\qquad p(\theta\mid y)\to\mathcal{N}\Big(\theta\;\Big|\;\bar y,\frac{\sigma^2}{n}\Big).
$$
由 $\mathbb{R}$ 上的“平坦先验” $p(\theta)\propto1$ 直接得到同样的后验。这个先验不是概率分布，但它是一列正常先验的极限，并且在此情形中后验仍是正常的分布。在鱼的例子（例 2.3.1）中，平坦先验给出 $\theta\mid y\sim\mathcal{N}(32,\,2^2/12)=\mathcal{N}(32,\,0.5774^2)$，与先验 $\mathcal{N}(30,4^2)$ 的结果几乎相同，因为后者本来就已经很弱。

### 2.6.2. 正常先验与广义先验

**定义 2.6.1（正常先验与广义先验）** 若 $\Theta$ 上的先验密度 $p(\theta)\ge0$ 满足 $\int_\Theta p(\theta)\,\mathrm{d}\theta<\infty$，使得归一化后它是一个概率分布，则称它为**正常先验**；若 $\int_\Theta p(\theta)\,\mathrm{d}\theta=\infty$，则称它为**广义先验**。

先验只需要指定到一个归一化常数，所以正常性只要求积分有限。若先验是正常的，则后验也是正常的：$p(y)=\int p(y\mid\theta)p(\theta)\,\mathrm{d}\theta$ 对几乎所有 $y$ 有限（它对 $y$ 的积分是 $\int p(\theta)\,\mathrm{d}\theta<\infty$），后验为 $p(y\mid\theta)p(\theta)/p(y)$。若先验是广义的，则后验可能正常也可能不正常，必须加以检验。理论上，只要后验是正常的，任何先验都可以接受；对许多常见问题，只要数据足够多，常用的广义先验都导出正常的后验：

- 正态均值：设 $y_1,\dots,y_n\mid\theta\overset{\text{iid}}{\sim}\mathcal{N}(\theta,\sigma^2)$，$p(\theta)\propto1$，则只要 $n\ge1$，后验 $\mathcal{N}(\bar y,\sigma^2/n)$ 就是正常的；
- 取 $p(\theta)\propto\theta^{-1}(1-\theta)^{-1}$（形式上是 $\mathrm{Beta}(0,0)$）的二项模型：后验 $\propto\theta^{y-1}(1-\theta)^{n-y-1}$ 在 $0<y<n$ 时是正常的 $\mathrm{Beta}(y,n-y)$，但在 $y=0$ 或 $y=n$ 时不正常，因为 $\int_0^1\theta^{-1}(1-\theta)^{n-1}\,\mathrm{d}\theta$ 在 $0$ 处发散。

不正常的后验不是“非常模糊”的回答，而是根本没有回答：它不定义概率。凡需要边际分布 $p(y)$ 本身之处，如用贝叶斯因子进行模型比较（[3.7.8](/3.7.8)），也必须避免使用广义先验，因为此时 $p(y)$ 含有任意常数。

### 2.6.3. 均匀先验依赖于参数化

选取无信息先验并不像“取均匀分布”那么简单，因为均匀性取决于参数所用的尺度。回忆变量替换：若 $\theta$ 的密度为 $p(\theta)$，$\phi=h(\theta)$ 是一一对应，则

$$
p_\phi(\phi)=p(\theta)\Big\lvert\frac{\mathrm{d}\theta}{\mathrm{d}\phi}\Big\rvert=p(\theta)\,\lvert h'(\theta)\rvert^{-1},\qquad\theta=h^{-1}(\phi).
$$
对均值已知、方差未知的正态观测，标准差上的均匀先验 $p(\sigma)\propto1$ 在 $h(\sigma)=\sigma^2$ 下对应于

$$
p(\sigma^2)\propto\frac{1}{2\sigma}\propto(\sigma^2)^{-1/2},
$$
它不是均匀的：它是递减的，所以与方差上的均匀先验相比，它偏向小的方差。反过来，$\sigma^2$ 上的均匀先验对应于 $p(\sigma)\propto2\sigma$，偏向大的标准差。用区间来说：在 $\sigma^2$ 的均匀先验下，方差的每个区间 $[a,a+0.1]$ 都与 $[0.1,0.2]$ 有相同的先验概率；对应的标准差区间 $[\sqrt a,\sqrt{a+0.1}]$ 随 $a$ 增大而变短，所以 $\sigma$ 的先验密度必须递增。因此，关于无知的陈述必须说明这种无知是在哪个尺度上成立的。

## 2.7. Jeffreys 先验

### 2.7.1. 不变性原理

能否用一条与度量尺度无关的规则来选取先验？以 $\pi(\cdot)$ 表示这条规则，它给模型与参数指定一个先验密度。设 $\phi=h(\theta)$ 是一一对应的重新参数化。得到 $\phi$ 的先验有两种方式：把为 $\theta$ 得到的先验 $\pi(\theta)$ 变换过来，得到 $p_\phi(\phi)=\pi(\theta)\lvert\mathrm{d}\theta/\mathrm{d}\phi\rvert$；或者把规则直接用于以 $\phi$ 写出的模型。

**定义 2.7.1（Jeffreys 不变性原理）** 若对每个一一对应的重新参数化 $\phi=h(\theta)$，把规则用于 $\phi$ 所给出的都是变换后的先验，

$$
\pi(\phi)=\pi(\theta)\Big\lvert\frac{\mathrm{d}\theta}{\mathrm{d}\phi}\Big\rvert,\qquad\theta=h^{-1}(\phi),
$$
则称这种构造先验密度的规则满足 **Jeffreys 不变性原理**。

均匀规则违反这条原理（§2.6.3）。满足它的一种规则使用模型的 **Fisher 信息量**（[3.2.3](/3.2.3)），

$$
J(\theta)=\mathbb{E}\Big[\Big(\frac{\mathrm{d}\log p(y\mid\theta)}{\mathrm{d}\theta}\Big)^2\;\Big|\;\theta\Big]=-\mathbb{E}\Big[\frac{\mathrm{d}^2\log p(y\mid\theta)}{\mathrm{d}\theta^2}\;\Big|\;\theta\Big],
$$
第二个等号在通常的正则条件下成立。对 $n$ 个 iid 观测，信息量为 $nJ_1(\theta)$，是单个观测信息量的 $n$ 倍；**观测信息** $-\frac{\mathrm{d}^2}{\mathrm{d}\theta^2}\log p(y\mid\theta)$ 的期望等于它。

**定义 2.7.2（Jeffreys 先验）** **Jeffreys 先验**为 $p(\theta)\propto J(\theta)^{1/2}$。对向量参数，它为 $p(\boldsymbol{\theta})\propto\lvert\det J(\boldsymbol{\theta})\rvert^{1/2}$，其中 $J(\boldsymbol{\theta})$ 是 **Fisher 信息矩阵**。

**定理 2.7.1** 在一一对应的可微重新参数化 $\phi=h(\theta)$ 下，

$$
J(\phi)=J(\theta)\Big(\frac{\mathrm{d}\theta}{\mathrm{d}\phi}\Big)^2,\qquad\text{从而}\qquad J(\phi)^{1/2}=J(\theta)^{1/2}\Big\lvert\frac{\mathrm{d}\theta}{\mathrm{d}\phi}\Big\rvert,
$$
所以 Jeffreys 先验满足 Jeffreys 不变性原理。

**证明** 记 $\ell(\theta)=\log p(y\mid\theta)$，用链式法则对 $\ell(\theta(\phi))$ 求二阶导数：

$$
\frac{\mathrm{d}^2\ell}{\mathrm{d}\phi^2}=\frac{\mathrm{d}^2\ell}{\mathrm{d}\theta^2}\Big(\frac{\mathrm{d}\theta}{\mathrm{d}\phi}\Big)^2+\frac{\mathrm{d}\ell}{\mathrm{d}\theta}\,\frac{\mathrm{d}^2\theta}{\mathrm{d}\phi^2}.
$$
取 $-\mathbb{E}(\cdot\mid\theta)$。得分的期望为零，$\mathbb{E}\big(\frac{\mathrm{d}\ell}{\mathrm{d}\theta}\mid\theta\big)=0$，所以第二项消失，$J(\phi)=J(\theta)\big(\frac{\mathrm{d}\theta}{\mathrm{d}\phi}\big)^2$。两边开平方得到第二种形式，它恰好就是定义 2.7.1 的变换规则。$\square$

### 2.7.2. 例

*正态标准差。* 对 $\theta$ 已知的 $y\mid\sigma\sim\mathcal{N}(\theta,\sigma^2)$，$\ell=-\log\sigma-\frac{(y-\theta)^2}{2\sigma^2}$，$\frac{\mathrm{d}^2\ell}{\mathrm{d}\sigma^2}=\frac{1}{\sigma^2}-\frac{3(y-\theta)^2}{\sigma^4}$，所以 $J(\sigma)=-\frac1{\sigma^2}+\frac{3}{\sigma^2}=\frac{2}{\sigma^2}$，Jeffreys 先验为

$$
p(\sigma)\propto\frac1\sigma,\qquad\text{等价地}\qquad p(\sigma^2)\propto\frac{1}{\sigma^2},\qquad p(\log\sigma)\propto1.
$$
这三种形式描述的是不同尺度上的同一个先验；由不变性，从哪个参数出发无关紧要。取这个先验，§2.4 的正态方差模型给出

$$
p(\sigma^2\mid y)\propto(\sigma^2)^{-1}\cdot(\sigma^2)^{-n/2}\exp\Big(-\frac{nv}{2\sigma^2}\Big)=(\sigma^2)^{-(n/2+1)}\exp\Big(-\frac{nv}{2\sigma^2}\Big),\qquad\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(n,v),
$$
这是 $\nu_0=0$ 的共轭后验：Jeffreys 先验是共轭族在 $\nu_0\to0$ 时的极限。

*指数数据。* 对 $y_i\overset{\text{iid}}{\sim}\mathrm{Exp}(\theta)$，速率 $\theta=1/\mathbb{E}(y\mid\theta)$，$\ell=\log\theta-\theta y$，$J(\theta)=1/\theta^2$，所以 $p(\theta)\propto1/\theta$。以均值 $\lambda=1/\theta$ 参数化，Jeffreys 先验仍是 $p(\lambda)\propto1/\lambda$，正如不变性所要求的：$\frac1\theta\lvert\frac{\mathrm{d}\theta}{\mathrm{d}\lambda}\rvert=\lambda\cdot\lambda^{-2}$。

*Poisson。* $\ell=y\log\theta-\theta$，$J(\theta)=\mathbb{E}(y)/\theta^2=1/\theta$，所以 $p(\theta)\propto\theta^{-1/2}$，即广义极限 $\Gamma(\frac12,0)$；后验为 $\Gamma(n\bar y+\frac12,n)$。

*二项。* $\log p(y\mid\theta)=\text{const}+y\log\theta+(n-y)\log(1-\theta)$ 给出 $J(\theta)=\frac{n}{\theta(1-\theta)}$，所以 Jeffreys 先验为

$$
p(\theta)\propto\theta^{-1/2}(1-\theta)^{-1/2},\qquad\mathrm{Beta}\big(\tfrac12,\tfrac12\big).
$$
另有两种“无信息”的选择与之竞争：

| 原则 | $\theta$ 的先验 | Beta 形式 |
|---|---|---|
| Jeffreys 先验 | $\theta^{-1/2}(1-\theta)^{-1/2}$ | $\mathrm{Beta}(\frac12,\frac12)$，正常 |
| Bayes–Laplace 均匀先验 | $1$ | $\mathrm{Beta}(1,1)$，正常 |
| 自然参数 $\operatorname{logit}\theta$ 上均匀 | $\theta^{-1}(1-\theta)^{-1}$ | $\mathrm{Beta}(0,0)$，广义 |

最后一行由变量替换得到，其中 $\frac{\mathrm{d}}{\mathrm{d}\theta}\operatorname{logit}\theta=\frac{1}{\theta(1-\theta)}$。不同的原则导出不同的无信息先验。差别至多相当于一次先验成功与一次先验失败，所以样本相当大时实际差异很小；当 $y$ 为 $0$ 或 $n$，或 $n$ 很小时，差异才会起作用。

对参数空间无限的参数，如正态均值或方差，Jeffreys 先验在通常的参数化下常常是广义的，必须像 §2.6.2 那样检验后验的正常性。

**例 2.7.1（奶粉，三种先验）** 回到例 2.4.1，$n=10$，$nv=149$。除共轭先验之外，考虑 Jeffreys 先验 $p(\sigma^2)\propto\sigma^{-2}$，它给出 $\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(10,14.9)$；以及均匀先验 $p(\sigma)\propto1$，它等价于 $p(\sigma^2)\propto(\sigma^2)^{-1/2}$，给出

$$
p(\sigma^2\mid y)\propto(\sigma^2)^{-((n-1)/2+1)}\exp\Big(-\frac{nv}{2\sigma^2}\Big),\qquad\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2\Big(n-1,\frac{nv}{n-1}\Big)=\mathrm{Inv}\text{-}\chi^2(9,16.56).
$$
每个后验都有 $\sigma^2=S/Z$ 的形式，$Z\sim\chi^2_\nu$；$\sigma$ 的概括量为

| 先验 | $\sigma^2\mid y$ | $\sqrt{\operatorname{mode}(\sigma^2\mid y)}$ | $\sqrt{\mathbb{E}(\sigma^2\mid y)}$ | $\sigma$ 的众数 | $\sigma$ 的均值 | $\sigma$ 的中位数 | $\sigma$ 的 $95\%$ 区间 |
|---|---|---|---|---|---|---|---|
| 共轭 $\mathrm{Inv}\text{-}\chi^2(1,11.37)$ | $\mathrm{Inv}\text{-}\chi^2(11,14.58)$ | 3.512 | 4.221 | 3.656 | 4.106 | 3.938 | $[2.70,\,6.48]$ |
| Jeffreys $p(\sigma^2)\propto\sigma^{-2}$ | $\mathrm{Inv}\text{-}\chi^2(10,14.9)$ | 3.524 | 4.316 | 3.680 | 4.183 | 3.994 | $[2.70,\,6.77]$ |
| 均匀 $p(\sigma)\propto1$ | $\mathrm{Inv}\text{-}\chi^2(9,16.56)$ | 3.680 | 4.614 | 3.860 | 4.452 | 4.226 | $[2.80,\,7.43]$ |

对 $\sigma^2=S/Z$，$\sigma$ 的后验密度正比于 $\sigma^{-(\nu+1)}\exp(-S/(2\sigma^2))$，众数为 $\sqrt{S/(\nu+1)}$，均值为 $\sqrt{S/2}\,\Gamma(\frac{\nu-1}{2})/\Gamma(\frac\nu2)$。在 $\sigma$ 的均匀先验下，$\sigma$ 的后验众数就是极大似然估计 $\sqrt v=3.862$，当先验在所考虑的参数上平坦时必然如此。只有一个先验自由度的共轭先验与 Jeffreys 先验相比变化很小。$\sigma$ 的均匀先验相对于 Jeffreys 先验偏向较大的值，使后验明显上移，尤其是右尾：只有十个观测时，先验在哪个尺度上平坦是有影响的。

![奶粉的例子：共轭先验、Jeffreys 先验与 σ 的均匀先验下 σ 的后验密度，以及 σ 的共轭先验（虚线）。](./plots/powder_milk_priors.py)

## 2.8. 枢轴量

在某些情形中，不同的方法对无信息先验的看法一致。这就是位置模型与尺度模型，其中**枢轴量**确定先验。

**定义 2.8.1（位置参数与尺度参数）** 若给定 $\theta$ 时 $u=y-\theta$ 的密度是不依赖于 $\theta$ 的固定函数 $f(u)$，则 $y-\theta$ 是枢轴量，$\theta$ 是纯粹的**位置参数**；该模型是位置族，$p(y\mid\theta)=f(y-\theta)$。若 $\theta>0$，且给定 $\theta$ 时 $u=y/\theta$ 的密度是固定函数 $g(u)$，则 $y/\theta$ 是枢轴量，$\theta$ 是纯粹的**尺度参数**；该模型是尺度族，$p(y\mid\theta)=\frac1\theta g(y/\theta)$。

例如，对 $y\sim\mathcal{N}(\theta,1)$，均值是位置参数，$f(u)=\frac{1}{\sqrt{2\pi}}\mathrm{e}^{-u^2/2}$；对 $y\sim\mathcal{N}(0,\theta^2)$，标准差是尺度参数，$g=f$。正态分布的标准差与指数分布的均值都是尺度参数。

给定 $\theta$ 时枢轴量的分布对每个 $\theta$ 都相同，且不含 $y$。对无信息先验的一个自然要求是保持这一点：给定 $y$ 时枢轴量的后验分布应当是同一个固定的分布。

*位置族。* 要求 $p(y-\theta\mid y)=f(y-\theta)$。对固定的 $y$，$\theta\mapsto u=y-\theta$ 的 Jacobi 因子为 $1$，所以 $\theta$ 的后验为 $p(\theta\mid y)=f(y-\theta)=p(y\mid\theta)$。与 $p(\theta\mid y)\propto p(\theta)p(y\mid\theta)$ 比较，得 $p(\theta)\propto1$。

*尺度族。* 要求 $u=y/\theta$ 的后验密度为 $g(u)$。对固定的 $y>0$，$\theta=y/u$，$\lvert\mathrm{d}u/\mathrm{d}\theta\rvert=y/\theta^2$，所以

$$
p(\theta\mid y)=g\Big(\frac y\theta\Big)\frac{y}{\theta^2}=\frac y\theta\cdot\frac1\theta g\Big(\frac y\theta\Big)=\frac{y}{\theta}\,p(y\mid\theta)\propto\frac1\theta\,p(y\mid\theta),
$$
由此得 $p(\theta)\propto1/\theta$。

对正态标准差，这又是 Jeffreys 先验。在某种意义上，尺度参数的“正确”尺度是 $\log\theta$，先验在这个尺度上平坦：

$$
p(\theta)\propto\frac1\theta,\qquad p(\theta^2)\propto\frac1{\theta^2},\qquad p(\log\theta)\propto1.
$$
枢轴量也是标准频率学派推断的基础。对 $y_1,\dots,y_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$，样本均值为 $\bar y$，样本方差为 $s^2$，有

$$
\frac{\sqrt n(\bar y-\mu)}{s}\sim t_{n-1},\qquad\frac{(n-1)s^2}{\sigma^2}\sim\chi^2_{n-1},
$$
通常的**置信区间**与检验就利用了这些分布不依赖于参数这一事实。在先验 $p(\mu,\sigma^2)\propto\sigma^{-2}$ 下（它对 $\mu$ 与 $\log\sigma$ 平坦），给定数据时同样的量在后验意义下有同样的分布（[3.7.3](/3.7.3)）；贝叶斯可信区间与经典置信区间在数值上因而一致，尽管解释不同。

## 2.9. 无信息先验的困难；参考先验

寻找一个总是模糊的先验会遇到若干困难。

- 若在某个问题中似然确实占主导，则在一系列相对平坦的先验之间如何选择无关紧要，所以并不需要唯一“正确”的模糊先验；若似然不占主导，则选择就有影响，而先验无论如何都必须基于实质性的理由来论证。
- 对许多问题没有明确的选择，因为在一种参数化下平坦的密度在另一种参数化下并不平坦（§2.6.3），并且不同的原则给出不同的答案（§2.7.2 的二项表）。
- 在用广义先验对相互竞争的模型取平均或比较时会产生进一步的困难，因为它们的边际似然只定义到任意常数。

一个系统的回答是参考先验，由 Bernardo（1979）提出，并由 Berger、Bernardo 等人自 1980 年代起发展。其想法是数据与参数应当最大限度地联系起来，使先验的影响最小：先验应当是使实验预期能教给我们最多的那一个。

**定义 2.9.1（参考先验）** 设 $T=T(y)$ 是充分统计量。在先验 $p(\theta)$ 下，实验提供的关于 $\theta$ 的期望信息为

$$
I(\Theta,T)=\int p(t)\int p(\theta\mid t)\log\frac{p(\theta\mid t)}{p(\theta)}\,\mathrm{d}\theta\,\mathrm{d}t=\iint p(\theta,t)\log\frac{p(\theta,t)}{p(\theta)p(t)}\,\mathrm{d}\theta\,\mathrm{d}t,
$$
即先验相对于后验的期望 **Kullback–Leibler 散度**，它等于 $\theta$ 与 $T$ 之间的互信息。**参考先验**是使它最大的先验，$p^*(\theta)=\arg\max_{p(\theta)}I(\Theta,T)$；确切地说，它定义为实验重复 $k$ 次、$k\to\infty$ 时这些最大化者的极限，因为对单次实验，最大化者往往是离散分布。

对一维的正则问题，其后验渐近正态，参考先验与 Jeffreys 先验一致。在多参数问题中，Jeffreys 规则 $\lvert\det J(\boldsymbol{\theta})\rvert^{1/2}$ 可能表现不佳，而按重要性对参数排序来构造的参考先验仍给出合理的答案。

在 Jeffreys 先验与参考先验这两种方法中，先验都是通过对数据取期望来选取的，而不是针对手头的具体数据集。因此先验依赖于抽样模型，而不仅依赖于所观测数据的似然，所以这些先验并不完全遵循**似然原理**：二项抽样与负二项抽样给出成比例的似然，却导出不同的 Jeffreys 先验（思考题 4）。

## 小结

| 模型 | 共轭先验与后验 | 预测分布 | Jeffreys 先验 |
|---|---|---|---|
| $y_i\sim\mathrm{Poi}(x_i\theta)$ | $\Gamma(\alpha,\beta)\to\Gamma(\alpha+\sum y_i,\beta+\sum x_i)$ | 先验预测（一个计数，$x=1$）$\mathrm{NB}\big(\alpha,\frac{\beta}{\beta+1}\big)$ | $\theta^{-1/2}$ |
| $y_i\sim\mathrm{Exp}(\theta)$ | $\Gamma(\alpha,\beta)\to\Gamma(\alpha+n,\beta+n\bar y)$ | | $\theta^{-1}$ |
| $y_i\sim\mathcal{N}(\theta,\sigma^2)$，$\sigma^2$ 已知 | $\mathcal{N}(\mu_0,\tau_0^2)\to\mathcal{N}(\mu_n,\tau_n^2)$，$\frac1{\tau_n^2}=\frac1{\tau_0^2}+\frac n{\sigma^2}$，$\mu_n$ 按精度加权 | 后验预测 $\mathcal{N}(\mu_n,\sigma^2+\tau_n^2)$ | $1$ |
| $y_i\sim\mathcal{N}(\theta,\sigma^2)$，$\theta$ 已知 | $\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2)\to\mathrm{Inv}\text{-}\chi^2\big(\nu_0+n,\frac{\nu_0\sigma_0^2+nv}{\nu_0+n}\big)$ | | $\sigma^2$ 上的 $\sigma^{-2}$，给出 $\mathrm{Inv}\text{-}\chi^2(n,v)$ |
| $y\sim\mathrm{Bin}(n,\theta)$ | $\mathrm{Beta}(\alpha,\beta)\to\mathrm{Beta}(\alpha+y,\beta+n-y)$ | Beta-二项 | $\mathrm{Beta}(\frac12,\frac12)$ |

- 后验是先验与数据的折中；共轭的超参数起先验数据的作用（先验计数与暴露量、先验精度、先验自由度），对指数族这是一个一般事实（命题 2.5.1）。
- 先验预测分布 $p(y)$ 描述实验之前的数据，是抽样分布在先验下的混合（对 Poisson–Gamma 模型是负二项分布）；后验预测分布 $p(\tilde y\mid y)$ 在后验下混合，其方差是抽样方差与后验不确定性之和。
- $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$ 是 $\nu s^2/Z$（$Z\sim\chi^2_\nu$）的分布（定义 2.4.1）；它的分位数由卡方分布的分位数得到，并且中位数与区间可以从 $\sigma^2$ 移到 $\sigma$，均值与众数则不能。
- 无信息先验：正常与广义（定义 2.6.1），要求后验正常；均匀性依赖于参数化；Jeffreys 先验 $J(\theta)^{1/2}$ 具有不变性（定理 2.7.1）；对位置参数，枢轴量给出 $p(\theta)\propto1$，对尺度参数给出 $p(\theta)\propto1/\theta$（定义 2.8.1）；参考先验使期望信息最大，在一维时与 Jeffreys 先验一致（定义 2.9.1）。

## 思考题

1. 对交通事故（例 2.2.1），求下周事故数的后验预测分布、它的均值与方差，以及一周内没有事故的概率。

   **答** 后验为 $\Gamma(32.25,10.5)$，暴露量 $\tilde x=1$，所以 $\tilde y\mid y\sim\mathrm{NB}(32.25,\,10.5/11.5)$。其均值为 $\mathbb{E}(\theta\mid y)=32.25/10.5=3.071$，方差为 $\mathbb{E}(\theta\mid y)+\operatorname{Var}(\theta\mid y)=3.071+32.25/10.5^2=3.364$，因 $\theta$ 的不确定性而略高于均值。没有事故的概率为 $(10.5/11.5)^{32.25}=0.053$，比代入估计值的结果 $\mathrm{e}^{-3.071}=0.046$ 略大。
2. 在鱼的例子（例 2.3.1）中，要使 $\theta$ 的后验标准差不超过 $0.25\,\mathrm{cm}$，需要测量多少条鱼？答案是否依赖于观测到的长度？

   **答** 需要 $\frac{1}{\tau_n^2}=\frac1{16}+\frac n4\ge\frac{1}{0.25^2}=16$，即 $n\ge4(16-\frac1{16})=63.75$，所以 $n=64$。在这个模型中后验方差只依赖于 $n$、$\sigma^2$ 与 $\tau_0^2$，不依赖于数据，所以样本量可以事先规划。
3. 求 Poisson 模型的 Jeffreys 先验以及交通数据所得的后验，并与共轭分析比较。

   **答** $J(\theta)=1/\theta$ 给出 $p(\theta)\propto\theta^{-1/2}$，后验为 $\Gamma(26+\frac12,8)=\Gamma(26.5,8)$，只要 $n\ge1$ 它对任何数据都是正常的。其均值为 $3.31$，$95\%$ 中心区间为 $[2.17,4.69]$。均值为 $2.5$ 的信息先验把后验均值拉低到 $3.07$，并把区间收窄为 $[2.10,4.22]$，因为它相当于增加了 $2.5$ 周的数据。
4. 在负二项模型中，$y$ 是第 $r$ 次成功之前的失败次数，$p(y\mid\theta)=\binom{y+r-1}{y}\theta^r(1-\theta)^y$。求 Jeffreys 先验，并与二项情形比较。这个比较对 Jeffreys 先验与似然原理说明了什么？

   **答** $\ell=r\log\theta+y\log(1-\theta)+\text{const}$，所以 $-\frac{\mathrm{d}^2\ell}{\mathrm{d}\theta^2}=\frac{r}{\theta^2}+\frac{y}{(1-\theta)^2}$。由 $\mathbb{E}(y\mid\theta)=r(1-\theta)/\theta$，

   $$
   J(\theta)=\frac{r}{\theta^2}+\frac{r}{\theta(1-\theta)}=\frac{r}{\theta^2(1-\theta)},\qquad p(\theta)\propto\theta^{-1}(1-\theta)^{-1/2},
   $$
   这是广义先验，而二项抽样给出 $\mathrm{Beta}(\frac12,\frac12)$。若观测到 $r$ 次成功与 $y$ 次失败，两个似然都与 $\theta^r(1-\theta)^y$ 成比例，但在两种 Jeffreys 先验下的后验分别是 $\mathrm{Beta}(r,y+\frac12)$ 与 $\mathrm{Beta}(r+\frac12,y+\frac12)$。本应只依赖于似然的推断，通过先验而依赖于停止规则，因为 Jeffreys 先验是对实验样本空间取的期望。
5. 设 $\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$。证明 $\sigma$ 的密度正比于 $\sigma^{-(\nu+1)}\exp\big(-\frac{\nu s^2}{2\sigma^2}\big)$，并求其众数。验证例 2.4.1 中共轭后验的值 $3.656$。

   **答** 由 $p(\sigma^2)\propto(\sigma^2)^{-(\nu/2+1)}\exp(-\frac{\nu s^2}{2\sigma^2})$ 与 $\frac{\mathrm{d}\sigma^2}{\mathrm{d}\sigma}=2\sigma$，$p(\sigma)\propto\sigma^{-\nu-2}\cdot\sigma\exp(-\frac{\nu s^2}{2\sigma^2})=\sigma^{-(\nu+1)}\exp(-\frac{\nu s^2}{2\sigma^2})$。对数的导数 $-\frac{\nu+1}{\sigma}+\frac{\nu s^2}{\sigma^3}$ 在 $\sigma^2=\frac{\nu s^2}{\nu+1}$ 处为零。在例 2.4.1 中，$\nu s^2=160.37$，$\nu=11$，所以众数为 $\sqrt{160.37/12}=3.656$，不同于 $\sqrt{\operatorname{mode}(\sigma^2\mid y)}=\sqrt{160.37/13}=3.512$：众数在变换 $\sigma^2\mapsto\sigma$ 下不具有不变性。
6. 把指数分布 $p(y\mid\theta)=\theta\mathrm{e}^{-\theta y}$ 写成指数族形式，由命题 2.5.1 求其共轭族，并给出 $n$ 个观测的后验。证明均值 $\lambda=1/\theta$ 是尺度参数，并由枢轴量导出 $p(\lambda)\propto1/\lambda$。

   **答** $p(y\mid\theta)=\exp(-\theta y+\log\theta)$，所以 $\phi(\theta)=-\theta$，$u(y)=y$，$g(\theta)=-\log\theta$，$f(y)=1$。共轭先验为 $\exp(-\nu\theta+n_0\log\theta)=\theta^{n_0}\mathrm{e}^{-\nu\theta}$，即 Gamma 族 $\Gamma(n_0+1,\nu)$；取 $\theta\sim\Gamma(\alpha,\beta)$，后验为 $\Gamma(\alpha+n,\beta+n\bar y)$。以均值表示，$p(y\mid\lambda)=\frac1\lambda\mathrm{e}^{-y/\lambda}=\frac1\lambda g(y/\lambda)$，$g(u)=\mathrm{e}^{-u}$，所以 $y/\lambda\sim\mathrm{Exp}(1)$ 是枢轴量，$\lambda$ 是尺度参数。由 §2.8，枢轴量的论证给出 $p(\lambda)\propto1/\lambda$，与该模型的 Jeffreys 先验一致（§2.7.2）。
