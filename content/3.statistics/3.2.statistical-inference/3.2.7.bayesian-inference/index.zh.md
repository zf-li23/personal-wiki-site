---
title: 贝叶斯推断
description: 贝叶斯推断方法——先验、似然与后验，共轭先验，均匀先验、Jeffreys 先验、最大熵先验与分层先验，贝叶斯估计与后验均方误差，可信区间与最高后验密度区间，贝叶斯检验与贝叶斯因子，后验预测与贝叶斯决策。
source_hash: e19ca0a85a4c
---

本课程前面各章的内容都属于经典统计，即频率学派统计：参数 $\theta$ 是固定的未知常数，概率是重复抽样下的长期频率，统计方法按其在实验假想重复中的表现来评价。这一理论给出了三类推断：点估计（无偏性、相合性、有效性、极大似然、矩估计、UMVUE；[3.2.3](/3.2.3)）、具有频率解释的区间估计（[3.2.4](/3.2.4)），以及**假设检验**（似然比检验、Neyman–Pearson 引理、UMP 检验、非参数检验；[3.2.5](/3.2.5)、[3.2.6](/3.2.6)）。贝叶斯统计则把参数看作随机变量。推断从先验分布出发，它表达了看到数据之前对 $\theta$ 的认识；贝叶斯公式（[3.1.2](/3.1.2)）把它转化为给定观测数据下的后验分布，此后的一切推断都以后验分布为基础。本章先比较两种观点（§7.1），介绍先验—后验的计算与共轭先验（§7.2–§7.3），讨论如何选择先验（§7.4），然后以贝叶斯方式重新处理三类推断问题：点估计（§7.5）、可信区间（§7.6）与检验（§7.7），最后讨论预测（§7.8）与决策理论（§7.9）。贝叶斯方法在 [3.7](/3.7) 中深入展开。

## 7.1. 频率学派与贝叶斯学派

### 7.1.1. 两种概率观

在频率学派统计中，事件的概率是无穷多次可重复试验中该事件发生比例的极限，参数是没有分布的固定量。在主观贝叶斯推断中，概率度量的是信念的强弱。收集数据之前，参数的取值是不确定的，这种不确定性用参数的一个概率密度来刻画；然后通过实验收集带有参数信息的数据，再用贝叶斯公式把先验信念与数据结合起来，得到对不确定性的更新描述。

例如，有人给我们一枚硬币，说它有一点不均匀。我们可以用 $\mathrm{Beta}(4,4)$ 分布表示对正面概率 $\theta$ 的认识：它关于 $0.5$ 对称，但相当分散。如果接着观察到 $30$ 次正面、$10$ 次反面，概率论给出 $\theta$ 的后验分布 $\mathrm{Beta}(34,14)$，它集中在 $0.7$ 附近（例 7.2.1）。

贝叶斯方法起源于 Bayes 和 Laplace（18 世纪末到 19 世纪中叶）。20 世纪 20 年代，Fisher 提出相反的观点：统计推断必须完全建立在具有直接实验解释的概率之上，即重复抽样原则。Jeffreys 的著作《概率论》（*Theory of Probability*，1939）开启了贝叶斯推断的复兴，并随着频率方法的问题逐渐显现而贯穿 20 世纪五六十年代。近几十年来，基于模拟的计算方法彻底改变了贝叶斯统计，使它在现代统计中占有重要地位。

### 7.1.2. 频率推断的问题

第一个问题是，频率推断一般不以观测数据为条件。置信区间是数据的集值函数 $C(\boldsymbol{X})\subseteq\Theta$，它在 $\boldsymbol{X}$ 的重复抽取中有比例 $1-\alpha$ 覆盖真值 $\theta$。这并不等于说：给定数据 $\boldsymbol{X}=\boldsymbol{x}$，区间 $C(\boldsymbol{x})$ 以概率 $1-\alpha$ 覆盖 $\theta$——尽管这正是我们想作出的那种陈述。

**例 7.1.1** 设 $X_1,X_2\overset{\text{iid}}{\sim}\mathrm{U}(\theta-0.5,\theta+0.5)$，次序统计量为 $X_{(1)}\le X_{(2)}$。$\theta$ 位于 $X_1$ 与 $X_2$ 之间，当且仅当两者一个低于 $\theta$、一个高于 $\theta$，故 $\mathbb{P}_\theta\big(X_{(1)}\le\theta\le X_{(2)}\big)=2\cdot\frac12\cdot\frac12=\frac12$：区间 $[X_{(1)},X_{(2)}]$ 是置信水平为 $0.5$ 的置信区间。假设观测数据满足 $x_{(2)}-x_{(1)}>0.5$，这在四分之一的数据集中发生（两个这样的均匀变量的极差超过 $0.5$ 的概率为 $(1-0.5)^2=1/4$）。此时两点都在 $\theta$ 的 $0.5$ 以内，而彼此相距超过 $0.5$，所以必然有 $\theta\in[x_{(1)},x_{(2)}]$。对这样的数据，我们确知区间覆盖 $\theta$，频率陈述却仍然报告置信度 $0.5$。

第二个问题是，频率推断依赖于从未观测到的数据。

**定义 7.1.1（似然原理）** **似然原理**是说：若关于 $\theta$ 的两个实验 $E_1,E_2$ 得到数据 $y_1,y_2$，其似然函数成比例，即存在常数 $c>0$ 使

$$
L(\theta;y_1,E_1)=c\,L(\theta;y_2,E_2)\qquad\text{对一切 }\theta,
$$
则两个实验对 $\theta$ 应得出相同的结论。

**极大似然估计**遵从似然原理：两个实验中的 MLE 相同。显著性检验则不然。在纯显著性检验中，我们只给出 $H_0$，选择检验统计量 $T(\boldsymbol{X})$，并把观测值 $T(\boldsymbol{x})=t$ 的 $p$ 值定义为

$$
p=\mathbb{P}\big(T(\boldsymbol{X})\ \text{至少与}\ t\ \text{一样极端}\mid H_0\big).
$$
$T(\boldsymbol{X})$ 的选择本身就是对偏离零假设的可能方向的陈述，已经涉及备择模型。而且，$p$ 值是对未观测到的数据求和（或积分），因而可能依赖于实验的形式；$p$ 值也不是 $\mathbb{P}\big(H_0\mid T(\boldsymbol{x})=t\big)$。

**例 7.1.2** 一个 Bernoulli 试验成功的概率为 $p$。实验 $E_1$ 做固定的 $n=12$ 次试验，记成功次数 $Y$；实验 $E_2$ 一直做到成功固定的 $y=3$ 次为止，记试验次数 $N$。假设 $12$ 次试验中成功 $3$ 次，且第 $12$ 次成功，这在两种设计下都可能出现。似然函数

$$
L(p;y_1,E_1)=\binom{12}{3}p^3(1-p)^9\quad(\text{二项}),\qquad L(p;y_2,E_2)=\binom{11}{2}p^3(1-p)^9\quad(\text{Pascal})
$$
成比例，两种情形下的 MLE 都是 $\hat p=1/4$。但检验 $H_0\colon p=0.5$ 对 $H_1\colon p<0.5$：在 $E_1$ 下 $p$ 值为

$$
\mathbb{P}(Y\le3\mid p=0.5)=\sum_{k=0}^{3}\binom{12}{k}0.5^{12}=0.073,
$$
在 $E_2$ 下为

$$
\mathbb{P}(N\ge12\mid p=0.5)=\sum_{k=12}^{\infty}\binom{k-1}{2}0.5^{k}=0.033 .
$$
在水平 $0.05$ 下，两个实验得出不同的结论，尽管数据与似然函数相同。$p$ 值不一致，是因为它们对两个不同样本空间的不同部分求和。

### 7.1.3. 概览

本章介绍的贝叶斯方法包括：先验（共轭先验、广义先验、Jeffreys 先验等），按"后验 $\propto$ 似然 $\times$ 先验"进行的后验推断，用可信区间与最高后验密度区间作区间估计，以及用后验概率、边际似然和贝叶斯因子作假设检验。当无法得到解析解时，使用近似计算技术：马尔可夫链蒙特卡洛（MCMC）方法，它模拟一条以后验为平稳分布的马尔可夫链；边际似然的近似（变分近似、Laplace 近似、贝叶斯信息准则 BIC）；以及 EM 算法，它在缺失数据问题的频率推断和贝叶斯推断中都很有用。最后，统计决策理论（§7.9）在后验之外加入损失函数，选择期望损失最小的行动。

## 7.2. 先验分布与后验分布

**定义 7.2.1（先验与后验）** 设数据 $\boldsymbol{x}$ 的密度（或概率质量函数）为 $f(\boldsymbol{x}\mid\theta)$，$\theta\in\Theta$。参数空间 $\Theta$ 上的任一概率分布都可作为**先验分布**，其密度记为 $\pi(\theta)$，它度量观测数据之前对 $\theta$ 的信念强弱。给定 $\boldsymbol{x}$ 时 $\theta$ 的条件分布称为**后验分布**：

$$
\pi(\theta\mid\boldsymbol{x})=\frac{f(\boldsymbol{x}\mid\theta)\pi(\theta)}{m(\boldsymbol{x})},\qquad m(\boldsymbol{x})=\int_\Theta f(\boldsymbol{x}\mid\theta)\pi(\theta)\,\mathrm{d}\theta,
$$
其中归一化常数 $m(\boldsymbol{x})$ 是把 $\theta$ 积分掉之后 $\boldsymbol{x}$ 的密度，称为**边际似然**。

这里 $f(\boldsymbol{x}\mid\theta)\pi(\theta)=f_{\boldsymbol{X},\theta}(\boldsymbol{x},\theta)$ 是数据与参数的联合密度。作为 $\theta$ 的函数，后验满足

$$
\pi(\theta\mid\boldsymbol{x})\propto f(\boldsymbol{x}\mid\theta)\pi(\theta),\qquad\text{后验}\propto\text{似然}\times\text{先验},
$$
对离散的 $\theta$，把积分换成求和即可。贝叶斯推断（Bayesian inference）把一切推断建立在后验分布之上。它遵从似然原理：若两个似然函数成比例，比例常数在贝叶斯公式的分子分母中相消，两个后验相同。如果对 Bernoulli 试验的成功概率 $p$ 一无所知，可取先验 $\mathrm{U}(0,1)$；一般如何确定先验，是 §7.4 的内容。

**例 7.2.1（二项数据，Beta 先验）** 设 $X\sim\mathrm{Bin}(n,\theta)$，$n$ 已知，用 Beta 分布表示对 $\theta$ 的先验认识：

$$
\pi(\theta)=\frac{\theta^{a-1}(1-\theta)^{b-1}}{\mathrm{B}(a,b)},\qquad0<\theta<1 .
$$
参数 $a,b>0$ 给出一个灵活的分布族：$a=b=1$ 为均匀分布，$a=b=20$ 集中在 $0.5$ 附近，$a<b$ 偏向较小的 $\theta$，等等。似然为 $f(x\mid\theta)=\binom nx\theta^x(1-\theta)^{n-x}$，$x=0,\dots,n$，故

$$
\pi(\theta\mid x)\propto\theta^{a-1}(1-\theta)^{b-1}\theta^x(1-\theta)^{n-x}=\theta^{a+x-1}(1-\theta)^{n-x+b-1},
$$
后验与先验形式相同，只是 $a,b$ 换成了 $a+x$、$b+n-x$：

$$
\theta\mid x\sim\mathrm{Beta}(a+x,\ b+n-x),\qquad \pi(\theta\mid x)=\frac{\theta^{a+x-1}(1-\theta)^{n-x+b-1}}{\mathrm{B}(a+x,b+n-x)}.
$$
§7.1.1 中的硬币就是 $a=b=4$，$n=40$，$x=30$ 的情形。由于 $\mathrm{Beta}(a,b)$ 的均值为 $\frac{a}{a+b}$，方差为 $\frac{ab}{(a+b)^2(a+b+1)}$，后验均值与方差为

$$
\mathbb{E}[\theta\mid X]=\frac{a+X}{a+b+n},\qquad \operatorname{Var}(\theta\mid X)=\frac{(a+X)(b+n-X)}{(a+b+n)^2(a+b+n+1)}.
$$
若 $X=n$ 且 $a=b=1$，后验均值为 $\frac{n+1}{n+2}$：只观察到一种结果时，点估计也不是 $0$ 或 $1$，这在小样本时尤为合理。$n$ 很大时，后验均值与方差约为 $\frac Xn$ 与 $\frac{X(n-X)}{n^3}$，即经典估计 $\hat\theta=X/n$ 及其估计方差 $\hat\theta(1-\hat\theta)/n$。

**例 7.2.2** 设真值 $\theta=0.3$，但先验均值为 $0.7$、标准差为 $0.1$，即 $\mathrm{Beta}(14,6)$。观察 $n=10$ 次试验得 $X=3$，后验为 $\mathrm{Beta}(17,13)$，仍被先验拉向右边；观察 $n=100$ 次试验得 $X=30$，后验为 $\mathrm{Beta}(44,76)$，已接近真值。随着 $n$ 增大，似然压倒了先验中的信息。

![左：不同参数的 Beta 先验密度。右：以 0.7 为中心的 Beta(14, 6) 先验，以及观察到 10 次中成功 3 次、100 次中成功 30 次后的后验；虚线为真值 0.3。](./plots/beta-prior-posterior.py)

## 7.3. 共轭先验

**定义 7.3.1（共轭先验）** 设 $\mathcal{P}$ 是一族先验分布。若对 $\mathcal{P}$ 中的每个先验和每组数据，后验仍属于 $\mathcal{P}$，则称 $\mathcal{P}$ 对模型 $\{f(x\mid\theta)\}$ 是**共轭**的，其中的分布称为**共轭先验**。

采用共轭先验时，后验只需更新有限个参数即可得到，贝叶斯计算可以显式完成。Beta 族对二项数据是共轭的（例 7.2.1）。常见的共轭对如下（$X_1,\dots,X_n$ 独立同分布，相关处 $x=\sum_ix_i$）：

| 模型 | 先验 | 后验 |
|---|---|---|
| $\mathrm{Bin}(n,\theta)$，一次观测 $x$ | $\mathrm{Beta}(a,b)$ | $\mathrm{Beta}(a+x,\ b+n-x)$ |
| $\mathrm{Ber}(\theta)$ | $\mathrm{Beta}(a,b)$ | $\mathrm{Beta}(a+x,\ b+n-x)$ |
| $\mathrm{Poi}(\theta)$ | $\Gamma(\alpha,\lambda)$ | $\Gamma(\alpha+x,\ \lambda+n)$ |
| $\mathrm{Exp}(\theta)$ | $\Gamma(\alpha,\lambda)$ | $\Gamma(\alpha+n,\ \lambda+x)$ |
| $\mathcal{N}(\theta,\sigma^2)$，$\sigma^2$ 已知 | $\mathcal{N}(\mu,\tau^2)$ | $\mathcal{N}\big(\mu_n(\boldsymbol{x}),\eta_n^2\big)$，例 7.5.1 |
| $\mathcal{N}(\mu,1/\tau)$，均未知 | 正态–Gamma | 正态–Gamma，例 7.3.1 |

（Gamma 分布采用速率参数化。）

**例 7.3.1（正态数据，均值与方差均未知）** 设 $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$，两个参数都未知，记 $\tau=1/\sigma^2$（称为精度（precision）），$\theta=(\tau,\mu)$。取先验 $\tau\sim\Gamma(\alpha,\beta)$（$\alpha,\beta>0$），并在给定 $\tau$ 时 $\mu\sim\mathcal{N}\big(\nu,\frac{1}{k\tau}\big)$，$k>0$，$\nu\in\mathbb{R}$：

$$
\pi(\tau,\mu)=\frac{\beta^\alpha}{\Gamma(\alpha)}\tau^{\alpha-1}\mathrm{e}^{-\beta\tau}\cdot(2\pi)^{-1/2}(k\tau)^{1/2}\exp\Big\{-\frac{k\tau}{2}(\mu-\nu)^2\Big\}\propto\tau^{\alpha-1/2}\exp\Big[-\tau\Big\{\beta+\frac k2(\mu-\nu)^2\Big\}\Big].
$$
似然为 $f(\boldsymbol{x}\mid\mu,\tau)=(2\pi)^{-n/2}\tau^{n/2}\exp\big\{-\frac\tau2\sum_{i=1}^n(x_i-\mu)^2\big\}$，故

$$
\pi(\tau,\mu\mid\boldsymbol{x})\propto\tau^{\alpha+n/2-1/2}\exp\Big[-\tau\Big\{\beta+\frac k2(\mu-\nu)^2+\frac12\sum_{i=1}^n(x_i-\mu)^2\Big\}\Big].
$$
配方得

$$
k(\mu-\nu)^2+\sum_{i=1}^n(x_i-\mu)^2=(k+n)\Big(\mu-\frac{k\nu+n\bar x}{k+n}\Big)^2+\frac{nk}{n+k}(\bar x-\nu)^2+\sum_{i=1}^n(x_i-\bar x)^2 .
$$
因此

$$
\pi(\tau,\mu\mid\boldsymbol{x})\propto\tau^{\alpha'-1/2}\exp\Big[-\tau\Big\{\beta'+\frac{k'}{2}(\mu-\nu')^2\Big\}\Big],
$$
其中

$$
\alpha'=\alpha+\frac n2,\quad \beta'=\beta+\frac12\cdot\frac{nk}{n+k}(\bar x-\nu)^2+\frac12\sum_{i=1}^n(x_i-\bar x)^2,\quad k'=k+n,\quad \nu'=\frac{k\nu+n\bar x}{k+n}.
$$
后验与先验形式相同，所以正态–Gamma 族是共轭的。$\mu$ 的后验均值 $\nu'$ 是先验均值 $\nu$ 与 $\bar x$ 以 $k$ 与 $n$ 为权的加权平均：先验相当于 $k$ 个额外的观测。

这些例子都是指数族（定义 2.2.1）的一个一般事实的特例。

**定理 7.3.1（指数族的共轭先验）** 设样本具有指数族密度

$$
f(\boldsymbol{x}\mid\theta)=C(\theta)^n\exp\Big\{\sum_{j=1}^kQ_j(\theta)\sum_{i=1}^nT_j(x_i)\Big\}\prod_{i=1}^nh(x_i),
$$
则以常数 $\tau_0,\dots,\tau_k$（使右端可积）为指标的先验族

$$
\pi(\theta\mid\tau_0,\dots,\tau_k)\propto C(\theta)^{\tau_0}\exp\Big\{\sum_{j=1}^kQ_j(\theta)\tau_j\Big\}
$$
是共轭的：后验为

$$
f(\boldsymbol{x}\mid\theta)\pi(\theta\mid\tau_0,\dots,\tau_k)\propto C(\theta)^{n+\tau_0}\exp\Big\{\sum_{j=1}^kQ_j(\theta)\Big[\sum_{i=1}^nT_j(x_i)+\tau_j\Big]\Big\},
$$
即参数更新为 $\tau_0'=n+\tau_0$、$\tau_j'=\sum_{i=1}^nT_j(x_i)+\tau_j$ 的先验。

先验参数进入后验的方式与充分统计量完全一样：$\tau_0$ 相当于先验样本量，$\tau_j$ 相当于 $T_j$ 的先验总和。

## 7.4. 先验的构造

### 7.4.1. 主观先验与非主观先验

主观先验（subjective prior）是表示数据获得之前关于参数的知识的分布；如果可能，应当为参数建立模型。若不同的科学家有不同的先验，或不清楚如何把先验知识表示成分布，就应考虑几种不同的先验，重复分析，检查结论对代表"不同观点"的先验是否不敏感（敏感性分析）。

有几种方法承诺给出"自动的"甚至"客观的"先验，即无信息先验（non-informative prior）：均匀先验、Jeffreys 先验和最大熵先验。实践中，如果这样的先验与真实的先验知识冲突，我们就不会用它。在考虑了主观因素之后，这些方法可用来补全先验分布的设定。

### 7.4.2. 均匀先验与广义先验

均匀先验是 $\pi(\theta)\propto\text{常数}$。若 $\Theta$ 无界，它就不是概率密度。

**定义 7.4.1（广义先验）** 满足 $\int_\Theta\pi(\theta)\,\mathrm{d}\theta=\infty$ 的非负先验"密度" $\pi(\theta)$ 称为**广义先验**（广义先验密度）。

只要后验是正常的，广义先验仍可使用。在均匀先验下，后验为

$$
\pi(\theta\mid x)=\frac{L(\theta;x)}{\int_\Theta L(\theta;x)\,\mathrm{d}\theta},
$$
它是概率密度当且仅当 $\int_\Theta L(\theta;x)\,\mathrm{d}\theta<\infty$。若该积分为无穷，后验也是广义的，基于它的一切推断都没有意义。

**例 7.4.1** 设 $X\sim\mathrm{Exp}(1/\mu)$（均值为 $\mu$），只观测 $N=\boldsymbol{1}_{\{X<1\}}\in\{0,1\}$。假设观测到 $N=0$，则 $L(\mu;0)=\mathbb{P}(X\ge1)=\exp(-1/\mu)$；在 $\mu>0$ 上取 $\pi(\mu)\propto1$，得 $\pi(\mu\mid N=0)\propto\exp(-1/\mu)$。这是广义的：$\mu\to\infty$ 时 $\exp(-1/\mu)\to1$，所以 $\int_0^\infty\exp(-1/\mu)\,\mathrm{d}\mu$ 发散。

若先验是均匀的（可能是广义的）而后验正常，并且可以说明"所有参数值先验地等可能"是对先验知识的合理表示，那么均匀先验可能是有用的（另见例 7.4.4）。

### 7.4.3. Jeffreys 先验

均匀先验的一个缺点是它不具有不变性：$\theta$ 上的均匀分布不是 $\theta^2$ 或 $\log\theta$ 上的均匀分布。Jeffreys 的想法是：构造先验的规则无论用于 $\theta$，还是用于另一参数化 $\psi$（$\theta=g(\psi)$），都应给出同一个分布。

**定义 7.4.2（Jeffreys 先验）** **Jeffreys 先验**为

$$
\pi(\theta)\propto\sqrt{I(\theta)},\qquad I(\theta)=\mathbb{E}_\theta\Big[\Big(\frac{\partial l}{\partial\theta}\Big)^2\Big],
$$
其中 $l=\log f(X\mid\theta)$，$I(\theta)$ 为 Fisher 信息（[3.2.3](/3.2.3)）。对向量参数 $\boldsymbol{\theta}$，取 $\pi(\boldsymbol{\theta})\propto\sqrt{\det I(\boldsymbol{\theta})}$，$I(\boldsymbol{\theta})$ 为 Fisher 信息矩阵。

**命题 7.4.1** Jeffreys 规则在重新参数化下不变：若 $\theta=g(\psi)$，$g$ 光滑且一一对应，则由 $\pi(\theta)\propto\sqrt{I_\theta}$ 导出的 $\psi$ 的先验为 $\pi_\Psi(\psi)\propto\sqrt{I_\psi}$。

**证明** 由变量替换公式，$\pi_\Psi(\psi)\propto\pi(g(\psi))\lvert g'(\psi)\rvert=\sqrt{I_{g(\psi)}}\,\lvert g'(\psi)\rvert$。由链式法则 $\frac{\partial l}{\partial\psi}=\frac{\partial l}{\partial\theta}g'(\psi)$，故 $I_\psi=g'(\psi)^2I_{g(\psi)}$。因此 $\pi_\Psi(\psi)\propto\sqrt{I_\psi}$。$\square$

**例 7.4.2** 对 $X\sim\mathrm{Ber}(\theta)$，$I(\theta)=\frac{1}{\theta(1-\theta)}$，Jeffreys 先验为 $\pi(\theta)\propto\theta^{-1/2}(1-\theta)^{-1/2}$，即 $\mathrm{Beta}(\frac12,\frac12)$ 分布。对 $\sigma^2$ 已知的 $X\sim\mathcal{N}(\mu,\sigma^2)$，$I(\mu)=1/\sigma^2$ 为常数，$\mu$ 的 Jeffreys 先验就是（广义的）均匀先验。

有时出于主观上的理由，希望先验在重新参数化下不变；Jeffreys 先验满足这一要求。

### 7.4.4. 最大熵先验

**定义 7.4.3（最大熵先验）** 在满足给定约束的所有密度 $\pi$ 中，使熵

$$
\phi[\pi]=-\int_\Theta\pi(\theta)\log\pi(\theta)\,\mathrm{d}\theta
$$
最大的密度 $\pi(\theta)$ 称为**最大熵先验**。求它是一个变分问题。

**定理 7.4.1** 在约束 $\mathbb{E}[t_j(\theta)]=t_j$（$j=1,\dots,p$）下使 $\phi[\pi]$ 最大的密度 $\pi$ 具有 $p$ 参数指数族的形式

$$
\pi(\theta)\propto\exp\Big\{\sum_{j=1}^p\lambda_jt_j(\theta)\Big\},\qquad\theta\in\Theta,
$$
其中 $\lambda_1,\dots,\lambda_p$ 由约束确定。

**例 7.4.3** (1) 在 $\Theta=\mathbb{R}$ 上满足

$$
\int_{-\infty}^\infty\pi(\theta)\,\mathrm{d}\theta=1,\qquad\int_{-\infty}^\infty\theta\,\pi(\theta)\,\mathrm{d}\theta=\mu,\qquad\int_{-\infty}^\infty(\theta-\mu)^2\pi(\theta)\,\mathrm{d}\theta=\sigma^2
$$
的所有密度中，熵最大的是正态密度 $\pi(\theta)=\frac{1}{\sqrt{2\pi\sigma^2}}\mathrm{e}^{-(\theta-\mu)^2/(2\sigma^2)}$：由定理 7.4.1，$\pi(\theta)\propto\exp\{\lambda_1\theta+\lambda_2\theta^2\}$，约束迫使它就是 $\mathcal{N}(\mu,\sigma^2)$。

(2) 设给定了各区间的先验概率 $\mathbb{P}(a_{j-1}<\theta\le a_j)=\phi_j$，$j=1,\dots,p$，$\sum_j\phi_j=1$，$\theta\in(a_0,a_p]$，$a_0<a_1<\cdots<a_p$。这些条件就是 $\mathbb{E}[t_j(\theta)]=\phi_j$，其中 $t_j(\theta)=\boldsymbol{1}_{(a_{j-1},a_j]}(\theta)$，故最大熵先验密度为

$$
\pi(\theta)\propto\exp\Big\{\sum_{j=1}^p\lambda_j\boldsymbol{1}_{(a_{j-1},a_j]}(\theta)\Big\},\qquad a_0<\theta\le a_p,
$$
它在每个区间上为常数：是以 $(a_0,a_1],\dots,(a_{p-1},a_p]$ 为组、高度为 $\phi_j/(a_j-a_{j-1})$ 的直方图。

### 7.4.5. 分层模型

**定义 7.4.4（分层模型）** 在**分层模型**中，先验本身的参数也被赋予概率分布：数据 $x$ 的密度为 $f(x\mid\theta)$，$\theta$ 的先验为 $\pi(\theta\mid\psi)$，超参数 $\psi\in\Psi$ 的先验为 $g(\psi)$。

分层模型只是间接地给出 $\theta$ 的先验：

$$
\pi(\theta)=\int_\Psi\pi(\theta\mid\psi)g(\psi)\,\mathrm{d}\psi .
$$
可以使用联合后验 $\pi(\theta,\psi\mid x)\propto f(x\mid\theta)\pi(\theta\mid\psi)g(\psi)$，也可以使用 $\pi(\theta\mid x)\propto f(x\mid\theta)\pi(\theta)$。分层模型适合具有分组结构的参数。

**例 7.4.4** 对 $i=1,\dots,k$，在第 $i$ 个总体上做 $n_i$ 次观测 $X_{i1},\dots,X_{in_i}$，$X_{ij}\sim\mathcal{N}(\theta_i,\sigma^2)$；均值 $\theta_i$ 未知，$\sigma^2$ 已知。设均值的先验模型为 $\theta_1,\dots,\theta_k\overset{\text{iid}}{\sim}\mathcal{N}(\phi,\tau^2)$：各总体不同但相似。记 $\psi=(\phi,\tau)$，

$$
\pi(\theta_1,\dots,\theta_k\mid\psi)=\prod_{i=1}^k(2\pi\tau^2)^{-1/2}\exp\Big\{-\frac{1}{2\tau^2}(\theta_i-\phi)^2\Big\}.
$$
还需要 $\phi$ 与 $\tau$ 的先验；设取 $g(\phi,\tau)=\text{常数}$，即先验地认为所有取值等可能（这是广义先验，使用时须小心）。联合后验为

$$
\pi(\boldsymbol{\theta},\psi\mid x)\propto\Big[\prod_{i=1}^k\exp\Big\{-\frac{1}{2\sigma^2}\sum_{j=1}^{n_i}(x_{ij}-\theta_i)^2\Big\}\Big]\Big[\prod_{i=1}^k\tau^{-1}\exp\Big\{-\frac{1}{2\tau^2}(\theta_i-\phi)^2\Big\}\Big].
$$
先对 $\phi$、再对 $\tau$ 积分（一个正态积分和一个 Gamma 型积分，留作练习），得 $\boldsymbol{\theta}$ 的边际后验

$$
\pi(\boldsymbol{\theta}\mid x)\propto\Big[\prod_{i=1}^k\exp\Big\{-\frac{n_i}{2\sigma^2}(\theta_i-\bar x_i)^2\Big\}\Big]\Big[\sum_{i=1}^k(\theta_i-\bar\theta)^2\Big]^{1-k/2},
$$
其中 $\bar x_i$ 为第 $i$ 组样本均值，$\bar\theta=\frac1k\sum_i\theta_i$（用到了 $\sum_j(x_{ij}-\theta_i)^2=n_i(\theta_i-\bar x_i)^2+\text{常数}$）。第一个因子把每个 $\theta_i$ 拉向本组的样本均值；第二个因子在各 $\theta_i$ 彼此接近时增大，把它们向公共均值收缩。$(\phi,\tau)$ 的先验是广义的，但这个后验是正常的（$k\ge3$ 时）。

## 7.5. 贝叶斯点估计

### 7.5.1. 贝叶斯估计

贝叶斯分析可以只基于后验分布，也可以考虑损失函数（统计决策理论，§7.9）。不考虑损失函数时，自然的点估计是后验分布的各种概括。

**定义 7.5.1（贝叶斯估计）** 设 $\pi(\theta\mid x)$ 为后验分布。

1. **最大后验估计**（MAP，即后验众数估计，也称广义极大似然估计）为 $\hat\theta_{\mathrm{MAP}}=\arg\max_{\theta\in\Theta}\pi(\theta\mid x)$。
2. **后验中位数**估计 $\hat\theta_{\mathrm{median}}$ 是 $\pi(\theta\mid x)$ 的中位数。
3. **后验均值**估计为 $\hat\theta_{\mathrm{mean}}=\mathbb{E}[\theta\mid x]=\int_\Theta\theta\,\pi(\theta\mid x)\,\mathrm{d}\theta$。

后验分布对称且单峰时，三种估计相同。

**例 7.5.1（正态均值，共轭先验）** 设 $X_1,\dots,X_n$ 是来自 $\mathcal{N}(\theta,\sigma^2)$ 的样本，$\sigma^2$ 已知，取共轭先验 $\theta\sim\mathcal{N}(\mu,\tau^2)$，$\mu,\tau^2$ 已知。则

$$
\begin{aligned}
\pi(\theta\mid\boldsymbol{x})&\propto f(\boldsymbol{x}\mid\theta)\pi(\theta)\propto\exp\Big\{-\frac{1}{2\sigma^2}\sum_{i=1}^n(x_i-\theta)^2-\frac{1}{2\tau^2}(\theta-\mu)^2\Big\}\\
&\propto\exp\Big\{-\frac{1}{2\sigma^2\tau^2/(n\tau^2+\sigma^2)}\Big(\theta-\frac{\sigma^2\mu+n\tau^2\bar x}{n\tau^2+\sigma^2}\Big)^2\Big\},
\end{aligned}
$$
所以后验为 $\mathcal{N}\big(\mu_n(\boldsymbol{x}),\eta_n^2\big)$，

$$
\mu_n(\boldsymbol{x})=\frac{\sigma^2/n}{\sigma^2/n+\tau^2}\mu+\frac{\tau^2}{\sigma^2/n+\tau^2}\bar x,\qquad \eta_n^2=\frac{\sigma^2\tau^2}{n\tau^2+\sigma^2}. \tag{7.1}
$$
三种贝叶斯估计都等于 $\mu_n(\boldsymbol{x})$，它是先验均值 $\mu$ 与样本均值 $\bar x$ 的加权平均，权重分别正比于精度 $1/\tau^2$ 与 $n/\sigma^2$。等价地，后验精度是先验精度与数据精度之和：$1/\eta_n^2=1/\tau^2+n/\sigma^2$。

**例 7.5.2（Bernoulli 数据，Beta 先验）** 设 $X_1,\dots,X_n$ 是来自 $\mathrm{Ber}(\theta)$ 的样本，取先验 $\mathrm{Beta}(a,b)$，$a,b$ 已知。记 $x=\sum_ix_i$，后验为 $\mathrm{Beta}(a+x,b+n-x)$（例 7.2.1），故

$$
\hat\theta_{\mathrm{MAP}}=\frac{x+a-1}{n+a+b-2},\qquad \hat\theta_{\mathrm{mean}}=\frac{x+a}{n+a+b}
$$
（众数公式要求 $a+x>1$，$b+n-x>1$）。$a=b=1$ 即均匀先验 $\mathrm{U}(0,1)$ 时，

$$
\hat\theta_{\mathrm{MAP}}=\frac xn,\qquad\hat\theta_{\mathrm{mean}}=\frac{x+1}{n+2}.
$$
因此 MLE 就是均匀先验下的 MAP 估计；更一般地，许多经典估计都是某种先验下的 MAP 估计。后验均值往往比 MAP 更合适。用 $n$ 件受检产品中的废品数 $x$ 估计废品率 $\theta$：

| $n$ | $x$ | $\hat\theta_{\mathrm{MAP}}=x/n$ | $\hat\theta_{\mathrm{mean}}=(x+1)/(n+2)$ |
|---|---|---|---|
| 3 | 0 | 0 | 0.200 |
| 10 | 0 | 0 | 0.083 |
| 3 | 3 | 1 | 0.800 |
| 10 | 10 | 1 | 0.917 |

MAP（这里即 MLE）区分不了 $3$ 件中 $0$ 件废品和 $10$ 件中 $0$ 件废品，并断言废品率恰为 $0$ 或 $1$；后验均值则反映了证据的多少。

**例 7.5.3** 设 $X\sim f(x\mid\theta)=\mathrm{e}^{-(x-\theta)}\boldsymbol{1}_{[\theta,\infty)}(x)$，$-\infty<\theta<\infty$，取 Cauchy 先验 $\pi(\theta)=\frac{1}{\pi(1+\theta^2)}$。后验为

$$
\pi(\theta\mid x)=\frac{f(x\mid\theta)\pi(\theta)}{m(x)}=\frac{\mathrm{e}^{-(x-\theta)}}{m(x)\,\pi(1+\theta^2)}\boldsymbol{1}_{(-\infty,x]}(\theta),
$$
对 $\theta<x$，

$$
\frac{\mathrm{d}\pi(\theta\mid x)}{\mathrm{d}\theta}=\frac{\mathrm{e}^{-x}}{\pi m(x)}\Big[\frac{\mathrm{e}^\theta}{1+\theta^2}-\frac{2\theta\mathrm{e}^\theta}{(1+\theta^2)^2}\Big]=\frac{\mathrm{e}^{-x}}{\pi m(x)}\cdot\frac{\mathrm{e}^\theta(\theta-1)^2}{(1+\theta^2)^2}\ge0 .
$$
所以 $\pi(\theta\mid x)$ 在 $(-\infty,x]$ 上递增，$\hat\theta_{\mathrm{MAP}}=x$。后验中位数与后验均值没有显式表达式，需数值计算。

### 7.5.2. 贝叶斯估计的精度

**定义 7.5.2（后验均方误差）** 估计 $\delta(x)$ 的精度用**后验均方误差**度量：

$$
\operatorname{PMSE}(\delta(x))=\mathbb{E}^{\theta\mid x}\big[(\theta-\delta(x))^2\big],
$$
这里对观测到的 $x$，按后验分布对 $\theta$ 求期望。

**定理 7.5.1** 记后验均值与后验方差为 $\mu^\pi(x)=\mathbb{E}[\theta\mid x]$ 与 $V^\pi(x)=\operatorname{Var}(\theta\mid x)$。对任一估计 $\delta$，

$$
\operatorname{PMSE}(\delta(x))=V^\pi(x)+\big(\mu^\pi(x)-\delta(x)\big)^2\ge V^\pi(x),
$$
等号成立当且仅当 $\delta(x)=\mu^\pi(x)$。因此后验均值在使 PMSE 最小的意义下是最优的，其 PMSE 就是后验方差。

**证明** 把 $\theta-\delta(x)$ 写成 $\big(\theta-\mu^\pi(x)\big)+\big(\mu^\pi(x)-\delta(x)\big)$，平方后取后验期望。给定 $x$ 时第二项是常数，交叉项因 $\mathbb{E}^{\theta\mid x}[\theta-\mu^\pi(x)]=0$ 而为零。$\square$

因此后验方差是贝叶斯点估计不确定性的自然度量，作用相当于频率理论中估计量的方差；但它是在给定观测数据的条件下计算的，而不是对重复样本计算的。

**例 7.5.4** 在例 7.5.1 中比较后验均值 $\hat\theta=\mu_n(\boldsymbol{x})$ 与经典 MLE $\delta(\boldsymbol{x})=\bar x$。后验方差 $V^\pi(\boldsymbol{x})=\eta_n^2=\frac{\sigma^2\tau^2}{n\tau^2+\sigma^2}$ 就是 $\hat\theta$ 的 PMSE，而

$$
\operatorname{PMSE}(\bar x)=V^\pi(\boldsymbol{x})+\big(\mu^\pi(\boldsymbol{x})-\bar x\big)^2=V^\pi(\boldsymbol{x})+\Big(\frac{\sigma^2/n}{\sigma^2/n+\tau^2}\Big)^2(\mu-\bar x)^2\ge V^\pi(\boldsymbol{x}).
$$

**例 7.5.5** 在同一模型中取均匀先验 $\pi(\theta)\propto1$，则

$$
\pi(\theta\mid\boldsymbol{x})\propto(2\pi\sigma^2)^{-n/2}\exp\Big\{-\frac{1}{2\sigma^2}\sum_{i=1}^n(x_i-\theta)^2\Big\}\propto\exp\Big\{-\frac{1}{2\sigma^2/n}(\theta-\bar x)^2\Big\},
$$
即正态分布 $\mathcal{N}(\bar x,\sigma^2/n)$。后验均值为 $\hat\theta=\bar x$，PMSE 为 $V^\pi(\boldsymbol{x})=\sigma^2/n$：数值上就是经典估计及其方差，只是现在具有条件解释。这是例 7.5.1 中 $\tau^2\to\infty$ 的极限。

**例 7.5.6** 设 $X\sim\mathrm{Bin}(n,\theta)$，先验为 $\mathrm{Beta}(a,b)$。后验均值估计 $\hat\theta_{\mathrm{mean}}=\frac{x+a}{n+a+b}$ 的 PMSE 等于后验方差

$$
V^\pi(x)=\frac{(x+a)(n-x+b)}{(a+b+n)^2(a+b+n+1)}.
$$
在均匀先验 $\mathrm{U}(0,1)=\mathrm{Beta}(1,1)$ 下，$\hat\theta_{\mathrm{mean}}=\frac{x+1}{n+2}$，$\hat\theta_{\mathrm{MAP}}=\frac xn$，$V^\pi(x)=\frac{(x+1)(n-x+1)}{(n+2)^2(n+3)}$，且

$$
\operatorname{PMSE}(\hat\theta_{\mathrm{MAP}})=V^\pi(x)+\big(\mu^\pi(x)-\hat\theta_{\mathrm{MAP}}\big)^2=\frac{(x+1)(n-x+1)}{(n+2)^2(n+3)}+\Big(\frac{x+1}{n+2}-\frac xn\Big)^2\ge V^\pi(x).
$$

## 7.6. 贝叶斯区间估计

**定义 7.6.1（可信区间）** 设 $\pi(\theta\mid\boldsymbol{x})$ 为给定 $\boldsymbol{x}$ 时 $\theta$ 的后验分布，$0<\alpha<1$。

1. 若存在统计量 $\hat\theta_1=\hat\theta_1(\boldsymbol{x})$ 与 $\hat\theta_2=\hat\theta_2(\boldsymbol{x})$ 使 $\mathbb{P}\big(\hat\theta_1\le\theta\le\hat\theta_2\mid\boldsymbol{x}\big)\ge1-\alpha$，则称 $[\hat\theta_1,\hat\theta_2]$ 为 $\theta$ 的可信水平为 $1-\alpha$ 的**可信区间**（贝叶斯可信区间）。
2. 若 $\mathbb{P}(\theta\ge\hat\theta_L\mid\boldsymbol{x})\ge1-\alpha$，则称 $\hat\theta_L=\hat\theta_L(\boldsymbol{x})$ 为可信水平为 $1-\alpha$ 的贝叶斯可信下限。
3. 若 $\mathbb{P}(\theta\le\hat\theta_U\mid\boldsymbol{x})\ge1-\alpha$，则称 $\hat\theta_U=\hat\theta_U(\boldsymbol{x})$ 为可信水平为 $1-\alpha$ 的贝叶斯可信上限。

可信区间的解释是直接的。若给定观测 $\boldsymbol{x}$，可信水平 $0.90$ 的可信区间为 $[1.2,2.0]$，则（对连续后验）$\mathbb{P}(1.2\le\theta\le2.0\mid\boldsymbol{x})=0.90$：$\theta$ 落在这个具体区间中的概率为 $0.90$——这正是**置信区间**所不能作出的陈述（§7.1.2）。可信区间往往也更容易构造，因为不需要枢轴量，只需后验的分位数。最简单的选择是后验 $\alpha/2$ 与 $1-\alpha/2$ 分位数之间的等尾区间。在可信水平相同的所有区间中，把后验密度最高的参数值收集起来，就得到最短的区间。

**定义 7.6.2（最高后验密度区间）** 设 $k$ 是使 $\mathbb{P}(\theta\in C\mid\boldsymbol{x})\ge1-\alpha$ 成立的最大常数，称集合 $C=\{\theta\colon\pi(\theta\mid\boldsymbol{x})\ge k\}$ 为可信水平 $1-\alpha$ 的**最高后验密度**（HPD）区域；它是区间时称为 HPD 区间。

HPD 区域内每一点的后验密度都高于区域外的每一点。后验单峰时，HPD 区域是区间，而且是给定水平下最短的可信区间；后验对称单峰时，它与等尾区间相同。

![偏斜的 Beta(3, 12) 后验的等尾与 HPD 90% 可信区间：HPD 区间更短，且两端点的后验密度相等。](./plots/credible-intervals.py)

**例 7.6.1** 在例 7.5.1 中后验为 $\mathcal{N}\big(\mu_n(\boldsymbol{x}),\eta_n^2\big)$，故

$$
\mathbb{P}\big(\mu_n(\boldsymbol{x})-\eta_nz_{\alpha/2}\le\theta\le\mu_n(\boldsymbol{x})+\eta_nz_{\alpha/2}\mid\boldsymbol{x}\big)=1-\alpha,
$$
$\big[\mu_n(\boldsymbol{x})-\eta_nz_{\alpha/2},\ \mu_n(\boldsymbol{x})+\eta_nz_{\alpha/2}\big]$ 是可信水平为 $1-\alpha$ 的可信区间，也是 HPD 区间。

**例 7.6.2（智商）** 一名儿童的智商测验分数 $X\sim\mathcal{N}(\theta,100)$，$\theta$ 是其真实智商；$\theta$ 的先验（儿童总体）为 $\mathcal{N}(100,225)$。某儿童得分 $x=115$。由式 (7.1)（$n=1$），后验为 $\mathcal{N}(\mu(x),\eta^2)$，

$$
\mu(x)=\frac{\sigma^2}{\sigma^2+\tau^2}\mu+\frac{\tau^2}{\sigma^2+\tau^2}x=\frac{100}{325}\cdot100+\frac{225}{325}\cdot115=110.38,\qquad \eta^2=\frac{\sigma^2\tau^2}{\sigma^2+\tau^2}=\frac{100\cdot225}{325}=8.32^2 .
$$
$\theta$ 的 $95\%$ 可信区间为 $[\mu(x)-1.96\eta,\ \mu(x)+1.96\eta]=[94.08,\ 126.69]$。经典的 $95\%$ 置信区间为 $[x-1.96\sigma,\ x+1.96\sigma]=[115-19.6,\ 115+19.6]=[95.4,\ 134.6]$。可信区间更短，因为它利用了先验信息；它也向总体均值 $100$ 偏移：异常高的分数部分来自运气。

## 7.7. 贝叶斯假设检验

检验 $H_0\colon\theta\in\Theta_0$ 对 $H_1\colon\theta\in\Theta_1$ 时，贝叶斯方法直接计算两个假设的后验概率

$$
\alpha_0=\mathbb{P}(\theta\in\Theta_0\mid x),\qquad\alpha_1=\mathbb{P}(\theta\in\Theta_1\mid x),
$$
$\alpha_0<\alpha_1$ 时拒绝 $H_0$，否则接受 $H_0$。比值 $\alpha_0/\alpha_1$ 称为 $H_0$ 的后验优势比（posterior odds）。与 $p$ 值不同，$\alpha_0$ 是给定数据时 $H_0$ 的概率。

**例 7.7.1** 设 $X\sim\mathrm{Bin}(n,\theta)$，取均匀先验 $\mathrm{U}(0,1)$，检验 $H_0\colon\theta\le1/2$ 对 $H_1\colon\theta>1/2$。后验为 $\mathrm{Beta}(x+1,n-x+1)$，$\pi(\theta\mid x)=\frac{\theta^x(1-\theta)^{n-x}}{\mathrm{B}(x+1,n-x+1)}$，故

$$
\alpha_0=\mathbb{P}(\theta\in\Theta_0\mid x)=\frac{1}{\mathrm{B}(x+1,n-x+1)}\int_0^{1/2}\theta^x(1-\theta)^{n-x}\,\mathrm{d}\theta .
$$
取 $n=5$：

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $\alpha_0$ | 63/64 | 57/64 | 42/64 | 22/64 | 7/64 | 1/64 |
| $\alpha_1$ | 1/64 | 7/64 | 22/64 | 42/64 | 57/64 | 63/64 |
| $\alpha_0/\alpha_1$ | 63.0 | 8.14 | 1.91 | 0.52 | 0.12 | 0.016 |

$x=0,1,2$ 时接受 $H_0$，$x=3,4,5$ 时拒绝 $H_0$。

**例 7.7.2（智商）** 在例 7.6.2 中检验 $H_0\colon\theta\le100$ 对 $H_1\colon\theta>100$。由后验 $\mathcal{N}(110.38,8.32^2)$，

$$
\alpha_0=\mathbb{P}(\theta\le100\mid x)=0.106,\qquad\alpha_1=\mathbb{P}(\theta>100\mid x)=0.894,
$$
故拒绝 $H_0$。

后验优势比依赖于先验概率 $\pi_0=\mathbb{P}(\theta\in\Theta_0)$ 与 $\pi_1=\mathbb{P}(\theta\in\Theta_1)$。把它们除掉，就分离出数据所提供的证据。

**定义 7.7.1（贝叶斯因子）** 支持 $H_1$ 的**贝叶斯因子**是后验优势比与先验优势比之比：

$$
\mathrm{BF}_{10}=\frac{\alpha_1/\alpha_0}{\pi_1/\pi_0}=\frac{m_1(x)}{m_0(x)},\qquad m_i(x)=\int_{\Theta_i}f(x\mid\theta)\,\pi_i(\theta)\,\mathrm{d}\theta,
$$
其中 $\pi_i$ 是先验密度限制在 $\Theta_i$ 上并重新归一化所得，因而 $m_i(x)$ 是 $H_i$ 下数据的边际似然。

第二个等式来自贝叶斯公式，因为 $\alpha_i\propto\pi_im_i(x)$。于是后验优势比 $=$ 贝叶斯因子 $\times$ 先验优势比。对两个简单假设，贝叶斯因子就是似然比 $f(x\mid\theta_1)/f(x\mid\theta_0)$；一般情形下，它比较两个模型的平均似然，并可用来比较同一数据的任意两个模型 $M_0,M_1$。$\mathrm{BF}_{10}>1$ 表示数据支持 $H_1$。在例 7.7.1 中均匀先验给出 $\pi_0=\pi_1=1/2$，故贝叶斯因子等于后验优势比 $\alpha_1/\alpha_0$。

这一方法可以直接推广到多个假设。在 $H_i\colon\theta\in\Theta_i$（$i=1,\dots,k$，$\Theta_1\cup\cdots\cup\Theta_k=\Theta$）中选择时，计算 $\alpha_i=\mathbb{P}(\theta\in\Theta_i\mid x)$，接受满足 $\alpha_j=\max_{1\le i\le k}\alpha_i$ 的假设 $H_j$。

**例 7.7.3（智商，三个假设）** 在例 7.6.2 中考虑 $H_1\colon\theta\le90$，$H_2\colon90<\theta<110$，$H_3\colon\theta\ge110$。由后验 $\mathcal{N}(110.38,8.32^2)$，

$$
\alpha_1=\mathbb{P}(\theta\le90\mid x)=0.007,\qquad\alpha_2=\mathbb{P}(90<\theta<110\mid x)=0.474,\qquad\alpha_3=\mathbb{P}(\theta\ge110\mid x)=0.518,
$$
故接受 $H_3$，尽管只比 $H_2$ 略占优势。

## 7.8. 贝叶斯预测

设 $X\sim f(x\mid\theta)$，$\boldsymbol{X}=(X_1,\dots,X_n)$ 是来自 $X$ 的样本，未来的随机变量 $Z$ 的密度为 $g(z\mid\theta)$。如何预测 $Z$？通常假定给定 $\theta$ 时 $Z$ 与 $\boldsymbol{X}$ 独立。于是给定 $\boldsymbol{X}=\boldsymbol{x}$ 时 $(Z,\theta)$ 的联合密度为 $g(z\mid\theta)\pi(\theta\mid\boldsymbol{x})$，把 $\theta$ 积分掉就得到给定 $\boldsymbol{x}$ 时 $Z$ 的分布。

**定义 7.8.1（后验预测分布）** 设 $\pi(\theta\mid\boldsymbol{x})$ 为给定 $\boldsymbol{x}$ 时 $\theta$ 的后验密度。$Z$ 的**后验预测分布**的密度为

$$
p(z\mid\boldsymbol{x})=\int_\Theta g(z\mid\theta)\,\pi(\theta\mid\boldsymbol{x})\,\mathrm{d}\theta .
$$

预测分布同时考虑了两种不确定性：给定 $\theta$ 时 $Z$ 的抽样变异，以及关于 $\theta$ 尚存的不确定性；代入点估计 $\hat\theta$ 则忽略了后者。

**例 7.8.1（赌徒）** 一名赌徒在前 $10$ 局中赢了 $3$ 局，预测他在接下来 $5$ 局中赢的局数。用 $X\sim\mathrm{Bin}(n,\theta)$ 描述 $n$ 局中赢的局数，$f(x\mid\theta)=\binom nx\theta^x(1-\theta)^{n-x}$，取共轭先验 $\mathrm{Beta}(a,b)$，则

$$
\pi(\theta\mid x)=\frac{\Gamma(n+a+b)}{\Gamma(x+a)\Gamma(n-x+b)}\theta^{x+a-1}(1-\theta)^{n-x+b-1}.
$$
记 $Z$ 为接下来 $k$ 局中赢的局数，$g(z\mid\theta)=\binom kz\theta^z(1-\theta)^{k-z}$，$z=0,1,\dots,k$。于是

$$
\begin{aligned}
p(z\mid x)&=\int_0^1\binom kz\theta^z(1-\theta)^{k-z}\pi(\theta\mid x)\,\mathrm{d}\theta=c\int_0^1\theta^{z+x+a-1}(1-\theta)^{k-z+n-x+b-1}\,\mathrm{d}\theta\\
&=c\,\frac{\Gamma(z+x+a)\Gamma(k-z+n-x+b)}{\Gamma(k+n+a+b)},\qquad c=\binom kz\frac{\Gamma(n+a+b)}{\Gamma(x+a)\Gamma(n-x+b)},
\end{aligned}
$$
这是 Beta-二项分布（beta-binomial distribution）。这里 $n=10$，$x=3$，$k=5$；取均匀先验 $a=b=1$，

$$
p(z\mid x=3)=\binom5z\frac{\Gamma(12)\Gamma(4+z)\Gamma(13-z)}{\Gamma(4)\Gamma(8)\Gamma(17)},\qquad z=0,1,\dots,5,
$$
计算得

| $z$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $p(z\mid 3)$ | 0.1813 | 0.3022 | 0.2747 | 0.1648 | 0.0641 | 0.0128 |

因此 $\mathbb{P}(0\le Z\le3\mid x)=0.923$：赌徒在接下来 $5$ 局中至多赢 $3$ 局的概率约为 $92\%$。

## 7.9. 统计决策理论

决策理论通过给行动赋予代价，把不确定性下的选择形式化。看一个例子：你接触了一种致命病毒。接触者中约 $1/3$ 会被感染，感染者若不接种疫苗都会死亡；而等到出现症状，疫苗已经无效。现在有人以 500 英镑的价格向你提供疫苗，你接种吗？最可能的情形是你没有被感染，但仅据此作决定，忽略了与各决策相联系的损失——而我们会给死亡赋予极高的损失。

**定义 7.9.1（贝叶斯行动）** 设 $\mathcal{A}$ 为可能行动的集合，$L(a,\theta)\ge0$ 为**损失函数**，即参数为 $\theta$ 时采取行动 $a$ 的损失。行动 $a$ 的后验期望损失为

$$
R(a\mid x)=\mathbb{E}\big[L(a,\theta)\mid x\big]=\int_\Theta L(a,\theta)\,\pi(\theta\mid x)\,\mathrm{d}\theta,
$$
使之最小的行动 $a^*=\arg\min_{a\in\mathcal{A}}R(a\mid x)$ 称为**贝叶斯行动**。

在疫苗的例子中，状态为"已感染"（概率 $1/3$）或"未感染"（$2/3$）。接种在两种状态下的损失都是 $500$；不接种时，未感染的损失为 $0$，已感染的损失为 $L_{\mathrm{death}}$。两者的期望损失分别为 $500$ 与 $L_{\mathrm{death}}/3$，所以只要死亡的损失被估价在 1500 英镑以上（这是显然的），贝叶斯行动就是接种疫苗。

点估计与检验都是决策问题，行动集分别为 $\mathcal{A}=\Theta$ 与 $\mathcal{A}=\{\text{接受 }H_0,\text{拒绝 }H_0\}$；§7.5 的贝叶斯估计就是特定损失下的贝叶斯行动。

**定理 7.9.1** 对实参数：

1. 在平方损失 $L(a,\theta)=(a-\theta)^2$ 下，贝叶斯行动是后验均值（定理 7.5.1）；
2. 在绝对损失 $L(a,\theta)=\lvert a-\theta\rvert$ 下，贝叶斯行动是后验中位数；
3. 检验 $H_0\colon\theta\in\Theta_0$ 对 $H_1\colon\theta\in\Theta_1$ 时，在 $0$–$1$ 损失（判断错误损失为 $1$，正确为 $0$）下，贝叶斯行动选择后验概率较大的假设，这就是 §7.7 的规则。

**证明** 第 1 条即定理 7.5.1。第 2 条：对连续后验，$\frac{\mathrm{d}}{\mathrm{d}a}\mathbb{E}[\lvert a-\theta\rvert\mid x]=\mathbb{P}(\theta<a\mid x)-\mathbb{P}(\theta>a\mid x)$，它在 $a$ 小于中位数时为负、大于中位数时为正。第 3 条：接受 $H_0$ 的期望损失为 $\alpha_1$，拒绝的期望损失为 $\alpha_0$，所以恰在 $\alpha_0<\alpha_1$ 时拒绝。$\square$

若损失不对称，例如第一类错误的损失为 $c_{\mathrm{I}}$、第二类错误为 $c_{\mathrm{II}}$，同样的论证给出：$c_{\mathrm{I}}\alpha_0<c_{\mathrm{II}}\alpha_1$ 时拒绝 $H_0$。疫苗问题的决策正是这样作出的。

## 小结 {#summary}

| | 频率学派 | 贝叶斯学派 |
|---|---|---|
| 参数 $\theta$ | 固定的未知常数 | 随机变量，先验为 $\pi(\theta)$ |
| 概率 | 长期频率 | 信念程度 |
| 推断依据 | 统计量在重复样本下的抽样分布 | 给定观测数据的后验 $\pi(\theta\mid\boldsymbol{x})\propto f(\boldsymbol{x}\mid\theta)\pi(\theta)$ |
| 点估计 | MLE、UMVUE、矩估计；按偏差、方差、MSE 评价 | 后验均值（平方损失）、中位数（绝对损失）、众数（MAP）；按 PMSE 评价 |
| 区间 | 置信区间：在 $1-\alpha$ 比例的重复中覆盖 $\theta$ | 可信区间：$\mathbb{P}(\theta\in C\mid\boldsymbol{x})\ge1-\alpha$；HPD 最短 |
| 检验 | $p$ 值 $=\mathbb{P}(\text{同样极端的数据}\mid H_0)$ | 后验概率 $\alpha_0,\alpha_1$；贝叶斯因子 $m_1(x)/m_0(x)$ |
| 预测 | 代入 $g(z\mid\hat\theta)$ | 后验预测 $\int g(z\mid\theta)\pi(\theta\mid\boldsymbol{x})\,\mathrm{d}\theta$ |
| 似然原理 | $p$ 值违反 | 遵从 |

先验既是这一方法的长处，也是它的薄弱环节。共轭先验使计算可以显式完成；无信息先验（均匀、Jeffreys、最大熵）追求客观性，但可能是广义的，此时必须检验后验是否正常；分层先验在相关的各组之间汇集信息。随着样本量增大，似然主导先验，贝叶斯与经典方法的答案通常趋于一致（例 7.2.1、例 7.5.5）。
