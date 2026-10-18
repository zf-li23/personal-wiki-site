---
title: 点估计
description: 估计量的评价准则（无偏性、有效性、均方误差、相合性、渐近正态性），矩估计法，极大似然估计，一致最小方差无偏估计理论（Rao–Blackwell 定理、Lehmann–Scheffé 定理与 Cramér–Rao 不等式），线性回归中的估计，核密度估计，以及高维稀疏估计简介。
source_hash: 8595ebd0180d
---

点估计用一个统计量去估计未知参数，例如总体的平均收入或 Bernoulli 试验的成功概率。估计量是随机样本的函数，其取值随样本而变，因此要问的不是某一个估计值对不对，而是估计量在重复抽样下表现如何。本章先建立比较估计量的准则（无偏性、有效性、均方误差、相合性与渐近正态性），再介绍两种构造估计量的一般方法——矩估计法与极大似然估计，最后寻求最优估计量：借助 [3.2.2](/3.2.2) 的**充分统计量**与**完备统计量**得到一致最小方差无偏估计，并用 Cramér–Rao 下界衡量无偏估计所能达到的精度。本章以两个应用收尾：线性回归模型中的估计（在课程 [3.3](/3.3) 中深入讨论），以及核密度估计这一最初的非参数方法（参见 [3.6](/3.6)）；选读一节简述参数个数超过样本量时的估计。所用的概率工具是**大数定律**、**中心极限定理**和 [3.1.14](/3.1.14) 中的各种收敛概念。给点估计附上精度度量的区间估计见 [3.2.4](/3.2.4)。

## 3.1. 估计量的评价准则

### 3.1.1. 点估计量

**统计推断**根据随机样本 $\boldsymbol{X}=(X_1,\dots,X_n)$ 对总体作出推断。在参数问题中，总体属于一个**分布族** $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$，$\Theta$ 为**参数空间**，$\theta$ 可以是 $k$ 维向量，目标是估计 $\theta$ 或其函数 $g(\theta)$；例如对来自 $\mathcal{N}(\mu,\sigma^2)$ 的样本，可能要估计 $\theta=(\mu,\sigma^2)$ 本身，也可能要估计 $g(\theta)=\mu/\sigma^2$。一旦用好的估计代替 $\theta$，总体的各种特征（均值、方差、分位数）也就随之得到估计。在非参数问题中，总体分布 $F$ 的形式未知，我们估计它的某些特征 $g(F)$，例如年收入的总体均值或总体方差，这些特征也称为参数。参数估计有两种形式：本章讨论的点估计，以及区间估计（[3.2.4](/3.2.4)）。

**定义 3.1.1（点估计量）** 用来估计未知参数 $g(\theta)$ 的统计量 $\hat g(\boldsymbol{X})=\hat g(X_1,\dots,X_n)$ 称为 $g(\theta)$ 的**点估计量**（简称估计量）。对于样本观测值 $\boldsymbol{x}=(x_1,\dots,x_n)$，它的取值 $\hat g(\boldsymbol{x})$ 称为 $g(\theta)$ 的**估计值**。

$\theta$ 的估计量记作 $\hat\theta(\boldsymbol{X})$，或简记为 $\hat\theta$。总体均值 $\mu$ 与总体方差 $\sigma^2$ 的典型估计量是**样本均值**与**样本方差**

$$
\bar X=\frac1n\sum_{i=1}^nX_i,\qquad S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2,
$$

相应的估计值为 $\bar x$ 与 $s^2$。估计量是随机样本的函数，因而本身是随机变量，其性质由它的**抽样分布**（[3.2.2](/3.2.2)）描述。同一个参数通常有许多候选估计量：总体均值 $\mu$ 可以用样本均值、样本中位数、样本众数来估计，甚至可以用常数 $10$ 来估计。为了挑选合理的估计量，我们要求它具有一些性质：无偏性、有效性、较小的均方误差、相合性与渐近正态性。

### 3.1.2. 无偏性

估计量在平均意义下应当接近参数，即 $\mathbb{E}(\hat\theta-\theta)$ 应尽可能小，最好对参数的每个取值都等于零。

**定义 3.1.2（无偏估计）** 设 $\boldsymbol{X}=(X_1,\dots,X_n)$ 是来自 $\{f(x;\theta)\colon\theta\in\Theta\}$ 的随机样本，$g(\theta)$ 是定义在 $\Theta$ 上的函数。若 $g(\theta)$ 的估计量 $\hat g(\boldsymbol{X})$ 满足

$$
\mathbb{E}_\theta[\hat g(\boldsymbol{X})]=g(\theta)\qquad\text{对一切 }\theta\in\Theta,
$$
则称 $\hat g(\boldsymbol{X})$ 是 $g(\theta)$ 的**无偏估计**；否则称它是**有偏**的，$\operatorname{Bias}_\theta(\hat g)=\mathbb{E}_\theta[\hat g(\boldsymbol{X})]-g(\theta)$ 称为它的**偏差**。对每个样本量 $n$ 给定一个估计量 $\hat g_n(\boldsymbol{X})$，若 $\lim_{n\to\infty}\mathbb{E}_\theta[\hat g_n(\boldsymbol{X})]=g(\theta)$ 对一切 $\theta\in\Theta$ 成立，则称估计量序列 $\hat g_n$ 是**渐近无偏**的。

无偏性有两种解释。

- 没有系统误差：$\hat g(\boldsymbol{X})$ 对有的样本大于 $g(\theta)$，对有的样本小于 $g(\theta)$；无偏意味着高估与低估相互抵消，估计量在平均意义下是准确的。
- 反复使用：某商店每天以单价 $a$ 从工厂购进 $N$ 件产品，工厂的长期废品率为 $p_0$；双方约定商店每天支付 $N(1-\hat p)a$，其中 $\hat p$ 是由当天样本估计出的废品率。每一天的 $\hat p$ 可能大于也可能小于 $p_0$，但只要 $\hat p$ 无偏，从长期看这一约定对双方都是公平的：由强**大数定律**，$m$ 天估计值的平均 $\frac1m\sum_{i=1}^m\hat g(\boldsymbol{X}^{(i)})$ 当 $m\to\infty$ 时几乎必然收敛到 $g(\theta)$。

无偏性只涉及一阶矩，数学上简单；在没有其他准则时，无偏估计似乎比有偏估计更可取。不过无偏性在非线性变换下不能保持：若 $\hat\theta$ 是 $\theta$ 的无偏估计，$g(\hat\theta)$ 一般不是 $g(\theta)$ 的无偏估计。

**定理 3.1.1** 设 $X_1,\dots,X_n$ 是来自均值为 $\mu$、方差为 $\sigma^2$ 的总体的随机样本，则 $\bar X$ 与 $S^2$ 分别是 $\mu$ 与 $\sigma^2$ 的无偏估计。

**证明** $\mathbb{E}\bar X=\frac1n\sum_{i=1}^n\mathbb{E}X_i=\mu$。由于 $\sum_{i=1}^n(X_i-\bar X)^2=\sum_{i=1}^nX_i^2-n\bar X^2$，$\mathbb{E}X_i^2=\sigma^2+\mu^2$，$\mathbb{E}\bar X^2=\operatorname{Var}(\bar X)+\mu^2=\sigma^2/n+\mu^2$，

$$
\mathbb{E}S^2=\frac1{n-1}\left[\sum_{i=1}^n\mathbb{E}X_i^2-n\,\mathbb{E}\bar X^2\right]=\frac n{n-1}\left[(\sigma^2+\mu^2)-\left(\frac{\sigma^2}n+\mu^2\right)\right]=\sigma^2.\qquad\square
$$

这正是样本方差除以 $n-1$ 而不是 $n$ 的原因：估计量 $S_n^2=\frac1n\sum_{i=1}^n(X_i-\bar X)^2=\frac{n-1}nS^2$ 满足 $\mathbb{E}S_n^2=\frac{n-1}n\sigma^2$，它有偏，但渐近无偏。

### 3.1.3. 有效性

无偏估计不唯一：对总体均值，$\bar X$、$X_1$、$(X_1+X_n)/2$ 都是无偏的。在无偏估计之中，抽样分布越集中在参数附近越好。

**定义 3.1.3（相对有效性）** 设 $\hat g_1(\boldsymbol{X})$ 与 $\hat g_2(\boldsymbol{X})$ 都是 $g(\theta)$ 的无偏估计。若

$$
\operatorname{Var}_\theta[\hat g_1(\boldsymbol{X})]\le\operatorname{Var}_\theta[\hat g_2(\boldsymbol{X})]\qquad\text{对一切 }\theta\in\Theta,
$$
且至少对一个 $\theta\in\Theta$ 严格不等式成立，则称 $\hat g_1$ 比 $\hat g_2$ **更有效**。

**例 3.1.1** 设 $X_1,\dots,X_n$ 是来自均值为 $\theta$、方差为 $\sigma^2$ 的总体的随机样本，令 $\hat\theta_1=X_1$，$\hat\theta_2=\bar X$。两者都无偏，且 $\operatorname{Var}(\hat\theta_1)=\sigma^2$，$\operatorname{Var}(\hat\theta_2)=\sigma^2/n$。因此 $n\ge2$ 时 $\bar X$ 比 $X_1$ 更有效，而且 $n$ 越大越有效。

### 3.1.4. 均方误差

估计量的好坏可以用它与参数的距离 $|\hat\theta-\theta|$ 来衡量。对距离取平均得到平均绝对误差 $\mathbb{E}|\hat\theta-\theta|$；任何关于 $|\hat\theta-\theta|$ 的增函数都可以用，其中平方最为方便。

**定义 3.1.4（均方误差）** 参数 $\theta$ 的估计量 $\hat\theta$ 的**均方误差**（MSE）是 $\theta$ 的函数

$$
\operatorname{MSE}_\theta(\hat\theta)=\mathbb{E}_\theta(\hat\theta-\theta)^2.
$$

均方误差便于解析计算，而且含义清楚：在 $\mathbb{E}_\theta\hat\theta$ 处展开平方，交叉项为零，得

$$
\operatorname{MSE}_\theta(\hat\theta)=\operatorname{Var}_\theta(\hat\theta)+(\mathbb{E}_\theta\hat\theta-\theta)^2=\operatorname{Var}_\theta(\hat\theta)+[\operatorname{Bias}_\theta(\hat\theta)]^2.
$$

因此均方误差综合了估计量的波动（精度）与偏差（准确度），均方误差小的估计量方差与偏差的总和小。无偏估计的均方误差就是方差；在无偏估计中寻找方差最小者，就引出 §3.4 的一致最小方差无偏估计。但这个分解也说明了偏差–方差权衡（bias–variance trade-off）：有些估计量允许少量偏差以换取方差的大幅下降，其均方误差反而小于任何无偏估计。对 $g(\theta)$ 的估计，准则表述为：若 $\mathbb{E}_\theta[\hat g_1-g(\theta)]^2\le\mathbb{E}_\theta[\hat g_2-g(\theta)]^2$ 对一切 $\theta$ 成立，且对某个 $\theta$ 严格成立，则在均方误差意义下 $\hat g_1$ 优于 $\hat g_2$。对每个 $\theta$ 都不劣于其他任何估计量的 $\hat g^*$ 可称为一致最小均方误差估计，但它一般不存在：常数估计 $\hat g\equiv g(\theta_0)$ 在 $\theta=\theta_0$ 处的均方误差为 $0$，于是 $\hat g^*$ 的均方误差必须处处为零。

**例 3.1.2** 设 $X_1,\dots,X_n$ 是来自 $\mathcal{N}(\mu,\sigma^2)$ 的随机样本。由定理 3.1.1，$\bar X$ 与 $S^2$ 无偏，因而均方误差等于方差：

$$
\mathbb{E}(\bar X-\mu)^2=\operatorname{Var}(\bar X)=\frac{\sigma^2}n,\qquad\mathbb{E}(S^2-\sigma^2)^2=\operatorname{Var}(S^2)=\frac{2\sigma^4}{n-1},
$$

后者是因为 $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$（[3.2.2](/3.2.2)）的方差为 $2(n-1)=(n-1)^2\operatorname{Var}(S^2)/\sigma^4$。$\sigma^2$ 的另一个估计量是 $\hat\sigma^2=S_n^2=\frac{n-1}nS^2$，后面会看到它就是极大似然估计。它有偏，$\mathbb{E}\hat\sigma^2=\frac{n-1}n\sigma^2$，方差 $\operatorname{Var}(\hat\sigma^2)=\left(\frac{n-1}n\right)^2\frac{2\sigma^4}{n-1}=\frac{2(n-1)\sigma^4}{n^2}$，于是

$$
\mathbb{E}(\hat\sigma^2-\sigma^2)^2=\frac{2(n-1)\sigma^4}{n^2}+\left(\frac{n-1}n\sigma^2-\sigma^2\right)^2=\frac{2n-1}{n^2}\sigma^4<\frac2{n-1}\sigma^4=\mathbb{E}(S^2-\sigma^2)^2.
$$

**注 3.1.1** 例 3.1.2 并不意味着应当放弃 $S^2$。在均方误差意义下 $\hat\sigma^2$ 平均更接近 $\sigma^2$，但它系统性地低估 $\sigma^2$。这里得不到绝对的结论，得到的是关于估计量的更多信息，以便针对具体情形选择合适的估计量。由于均方误差是参数的函数，一般不存在唯一最好的估计量：两个估计量的均方误差曲线常常相交，各自只在参数空间的一部分上更好。

偏差、方差与均方误差都依赖于样本量，增大 $n$ 通常使三者都减小。模拟可以使这一点具体化。对 $n=10,20,\dots,100$，各从 $\mathcal{N}(0,1)$ 抽取 $10\,000$ 个样本，$S_n^2$ 的偏差约为 $-1/n$，$S^2$ 的偏差为零，而 $S_n^2$ 的方差与均方误差略小于 $S^2$，差别随 $n$ 增大而消失。对位置参数，可以类似地比较样本均值 $\bar X$、**样本中位数** $m_{0.5}$ 与截尾均值 $\bar X_\alpha$；截尾均值先去掉最小与最大的各 $\alpha$ 比例的观测，再对其余观测取平均。截尾均值对异常值不如样本均值敏感，但对许多模型仍能合理地估计中心位置，是一种稳健估计量。从 $25\,000$ 名 18 岁香港儿童的身高（近似对称的总体，均值 $68$ 英寸，约 $172.7$ 厘米）中重复抽样，三种估计量的偏差都可以忽略，中位数的方差最大。从美国艾奥瓦州 Ames 约 $2000$ 套房屋的售价（右偏的总体，均值约 $18$ 万美元，中位数约 $16$ 万美元）中重复抽样，中位数与截尾均值作为均值的估计有明显的负偏差，但轻度截尾的均值的均方误差却小于样本均值：少量偏差换来了更大幅度的方差下降。

### 3.1.5. 相合性

无偏性与有效性是固定样本量下的性质。相合性则要求随着信息的积累，估计量收敛到参数。

**定义 3.1.5（相合估计）** 对每个样本量 $n$，设 $\hat g_n(\boldsymbol{X})=\hat g_n(X_1,\dots,X_n)$ 是 $g(\theta)$ 的估计量。

1. 若 $\hat g_n(\boldsymbol{X})\xrightarrow{p}g(\theta)$，即对一切 $\theta\in\Theta$ 与一切 $\varepsilon>0$ 有 $\lim_{n\to\infty}\mathbb{P}_\theta(|\hat g_n(\boldsymbol{X})-g(\theta)|\ge\varepsilon)=0$，则称 $\hat g_n$ 是 $g(\theta)$ 的（弱）**相合估计**。
2. 若对一切 $\theta\in\Theta$ 有 $\mathbb{P}_\theta\left(\lim_{n\to\infty}\hat g_n(\boldsymbol{X})=g(\theta)\right)=1$，则称 $\hat g_n$ 是 $g(\theta)$ 的**强相合**估计。
3. 若对某个 $r>0$ 与一切 $\theta\in\Theta$ 有 $\lim_{n\to\infty}\mathbb{E}_\theta|\hat g_n(\boldsymbol{X})-g(\theta)|^r=0$，则称 $\hat g_n$ 是 **$r$ 阶矩相合**的；$r=2$ 时称为**均方相合**。

这三者分别对应 [3.1.14](/3.1.14) 中的**依概率收敛**、**几乎处处收敛**与 $r$ 阶矩收敛：强相合与 $r$ 阶矩相合都蕴含弱相合。均方相合等价于均方误差趋于零，即偏差与方差都趋于零，这往往是验证相合性最简便的途径。由强大数定律，$\bar X$ 是 $\mu$ 的强相合估计；更一般地，样本矩是相应总体矩的强相合估计。由连续映射定理（[3.1.14](/3.1.14)），强相合估计的连续函数仍是强相合的。

**例 3.1.3** 设 $X_1,\dots,X_n$ 是来自 $\mathrm{U}(0,\theta)$ 的随机样本，则几何平均 $T(\boldsymbol{X})=\left(\prod_{i=1}^nX_i\right)^{1/n}$ 是 $g(\theta)=\theta\mathrm{e}^{-1}$ 的强相合估计。

**证明** 令 $Y_i=\log X_i$，则 $Y_1,\dots,Y_n$ 独立同分布，密度为 $f(y;\theta)=\frac1\theta\mathrm{e}^y\boldsymbol{1}_{(-\infty,\log\theta)}(y)$。分部积分得

$$
\mathbb{E}Y_1=\frac1\theta\int_{-\infty}^{\log\theta}y\mathrm{e}^y\,\mathrm{d}y=\frac1\theta\left[y\mathrm{e}^y\Big|_{-\infty}^{\log\theta}-\int_{-\infty}^{\log\theta}\mathrm{e}^y\,\mathrm{d}y\right]=\log\theta-1.
$$

由强大数定律，$\log T(\boldsymbol{X})=\frac1n\sum_{i=1}^n\log X_i=\bar Y\to\log\theta-1$ 几乎必然成立，故 $T(\boldsymbol{X})=\mathrm{e}^{\bar Y}\to\mathrm{e}^{\log\theta-1}=\theta\mathrm{e}^{-1}$ 几乎必然成立。$\square$

### 3.1.6. 渐近正态性

相合性说明 $\hat g_n-g(\theta)\to0$；渐近正态性刻画剩余误差的大小与形状，这正是大样本置信区间与检验所需要的。

**定义 3.1.6（相合渐近正态估计）** 若存在函数 $\sigma^2(\theta)>0$，使得

$$
\sqrt n\,[\hat g_n(\boldsymbol{X})-g(\theta)]\xrightarrow{d}\mathcal{N}(0,\sigma^2(\theta))\qquad\text{对一切 }\theta\in\Theta,
$$
则称 $g(\theta)$ 的估计量序列 $\hat g_n$ 是**相合渐近正态估计**，$\sigma^2(\theta)$ 称为 $\hat g_n$ 的**渐近方差**。

粗略地说，$n$ 很大时 $\hat g_n\overset{\cdot}{\sim}\mathcal{N}(g(\theta),\sigma^2(\theta)/n)$，误差的量级为 $1/\sqrt n$。由中心极限定理，只要 $\sigma^2<\infty$，就有 $\sqrt n(\bar X-\mu)\xrightarrow{d}\mathcal{N}(0,\sigma^2)$。同一参数的两个相合渐近正态估计中，渐近方差较小者更好。

## 3.2. 矩估计法

### 3.2.1. 动机

**例 3.2.1** 设对 $100$ 部手机测量单次充电的通话时长（模拟数据），要估计通话时长的均值与方差。以随机变量 $X$ 表示总体，目标是 $\mu=\mathbb{E}X$ 与 $\sigma^2=\operatorname{Var}(X)=\mathbb{E}(X-\mathbb{E}X)^2$。不假定任何统计模型，就可以用相应的样本量来估计：

$$
\hat\mu=\bar X=\frac1n\sum_{i=1}^nX_i\colon\ \bar x=24.5,\qquad\hat\sigma^2=S_n^2=\frac1n\sum_{i=1}^n(X_i-\bar X)^2\colon\ s_n^2=0.15.
$$

在点估计之外作推断（例如求置信区间）则需要 bootstrap 等重抽样方法。若总体可以用 $\mathcal{N}(\mu,\sigma^2)$ 近似，则仍有 $\mathbb{E}X=\mu$、$\operatorname{Var}(X)=\sigma^2$，使用同样的估计量，而推断可以借助正态理论或中心极限定理。

**例 3.2.2** 对 $n=500$ 名 18 岁儿童，以 $(X,Y)$ 表示体重（磅）与身高（英寸），记 $\mu_1=\mathbb{E}X$，$\mu_2=\mathbb{E}Y$，$\sigma_1^2=\operatorname{Var}(X)$，$\sigma_2^2=\operatorname{Var}(Y)$，相关系数 $\rho=\operatorname{Corr}(X,Y)$。不借助任何模型，用相应的样本量得到

$$
\hat\mu_1=\bar X=126.7,\quad\hat\mu_2=\bar Y=67.9,\quad\hat\sigma_1^2=S_{nX}^2=143.3,\quad\hat\sigma_2^2=S_{nY}^2=3.9,\quad\hat\rho=\frac{S_{nXY}}{S_{nX}S_{nY}}=\frac{\frac1n\sum_{i=1}^n(X_i-\bar X)(Y_i-\bar Y)}{S_{nX}S_{nY}}=0.48,
$$

即平均体重 $57.5$ 千克、平均身高 $172.5$ 厘米。若假定 $(X,Y)$ 服从二元正态分布，得到的估计量相同，而模型还可以用来构造置信区间。

### 3.2.2. 定义与例子

这一想法来自 K. Pearson（1894）：把参数表示为总体矩的函数，再用样本矩代替总体矩。总体 $X$ 的 $k$ 阶原点矩与 $k$ 阶中心矩为 $\alpha_k=\mathbb{E}X^k$ 与 $\mu_k=\mathbb{E}(X-\mathbb{E}X)^k$；相应的样本量是 [3.2.1](/3.2.1) 中的样本原点矩 $a_{n,k}=\frac1n\sum_{i=1}^nX_i^k$（$k=1,2,\dots$）与样本中心矩 $m_{n,k}=\frac1n\sum_{i=1}^n(X_i-\bar X)^k$（$k=2,3,\dots$）。

**定义 3.2.1（矩估计法）** 设 $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$ 是分布族，参数的函数 $g(\theta)$ 可以写成总体矩的函数

$$
g(\theta)=G(\alpha_1,\dots,\alpha_k;\mu_2,\dots,\mu_s).
$$
对随机样本 $\boldsymbol{X}=(X_1,\dots,X_n)$，用样本矩代替总体矩，得到

$$
\hat g(\boldsymbol{X})=G(a_{n,1},\dots,a_{n,k};m_{n,2},\dots,m_{n,s}),
$$
称为 $g(\theta)$ 的**矩估计**。这种构造估计量的方法称为**矩估计法**。

例如，变异系数 $\nu=\sigma/\mu$ 与偏度 $\beta_1=\mu_3/\mu_2^{3/2}$ 的矩估计为

$$
\hat\nu=\frac S{\bar X}\ \ (\text{或 }S_n/\bar X),\qquad\hat\beta_1=\frac{m_{n,3}}{m_{n,2}^{3/2}}=\frac{\sqrt n\sum_{i=1}^n(X_i-\bar X)^3}{\left[\sum_{i=1}^n(X_i-\bar X)^2\right]^{3/2}}.
$$

在许多情形下，矩估计不需要知道密度的形式，即不需要统计模型，只需要所涉及的矩存在。对参数为 $\boldsymbol{\theta}=(\theta_1,\dots,\theta_r)$ 的参数族，记 $\mathbb{E}_{\boldsymbol{\theta}}X^k=m_k(\theta_1,\dots,\theta_r)$，$k=1,\dots,r$，解方程组

$$
\frac1n\sum_{i=1}^nX_i^k=m_k(\theta_1,\dots,\theta_r),\qquad k=1,\dots,r,
$$

得到 $\boldsymbol{\theta}$ 的矩估计；方程组可能没有闭式解，这时用数值方法求解。

**例 3.2.3** 对来自 $\mathrm{Ber}(\theta)$（$0<\theta<1$）的随机样本，$\mathbb{E}_\theta X_1=\theta$，故 $\bar X$ 是 $\theta$ 的矩估计，$\bar X(1-\bar X)$ 是 $g(\theta)=\theta(1-\theta)$ 的矩估计。

**例 3.2.4** 对来自 $\mathcal{N}(\mu,\sigma^2)$ 且两个参数都未知的随机样本，$\mathbb{E}X_1=\mu$，$\mathbb{E}X_1^2=\sigma^2+\mu^2$。解 $\bar X=\mu$ 与 $\frac1n\sum X_i^2=\sigma^2+\mu^2$ 得

$$
\tilde\mu=\bar X,\qquad\tilde\sigma^2=\frac1n\sum_{i=1}^nX_i^2-\bar X^2=\frac1n\sum_{i=1}^n(X_i-\bar X)^2=S_n^2.
$$

**例 3.2.5** 对来自 $\mathrm{U}(\alpha,\beta)$ 且两个端点都未知的随机样本，$\mathbb{E}X_1=\frac{\alpha+\beta}2$，$\operatorname{Var}(X_1)=\frac{(\beta-\alpha)^2}{12}$。解 $\bar X=\frac{\alpha+\beta}2$ 与 $S_n^2=\frac{(\beta-\alpha)^2}{12}$ 得

$$
\hat\alpha=\bar X-\sqrt3\,S_n,\qquad\hat\beta=\bar X+\sqrt3\,S_n.
$$

注意 $\hat\alpha$ 可能大于最小观测值，因此矩估计可能与数据矛盾；例 3.3.10 的极大似然估计没有这个缺点。

**例 3.2.6** 对来自二维总体的随机样本 $(X_i,Y_i)$，$i=1,\dots,n$，协方差 $\sigma_{12}=\mathbb{E}[(X-\mathbb{E}X)(Y-\mathbb{E}Y)]$ 的矩估计是**样本协方差** $m_{12}=\frac1n\sum_{i=1}^n(X_i-\bar X)(Y_i-\bar Y)$，相关系数 $\rho=\sigma_{12}/(\sigma_1\sigma_2)$ 的矩估计是样本相关系数

$$
r=\frac{\sum_{i=1}^n(X_i-\bar X)(Y_i-\bar Y)}{\sqrt{\sum_{i=1}^n(X_i-\bar X)^2\sum_{i=1}^n(Y_i-\bar Y)^2}}.
$$

**例 3.2.7（不唯一性）** 矩估计不一定唯一。对密度为 $\theta\mathrm{e}^{-\theta x}$（$x>0$）的 $\mathrm{Exp}(\theta)$，$\mathbb{E}X=\theta^{-1}$ 与 $\operatorname{Var}(X)=\theta^{-2}$ 都能确定 $\theta$，分别给出矩估计

$$
\hat\theta_1=\bar X^{-1},\qquad\hat\theta_2=S_n^{-1}.
$$

取 $\theta=2$，对 $n=10,30,50,\dots$ 各重复 $10\,000$ 次模拟，结果表明对每个 $n$，$\hat\theta_1$ 的偏差、方差与均方误差都小于 $\hat\theta_2$。一般的经验是使用低阶矩，因为低阶矩估计得更精确；例 3.3.4 将表明 $\hat\theta_1$ 也是极大似然估计。

### 3.2.3. 性质

1. 无偏性：样本原点矩是无偏的，$\mathbb{E}a_{n,k}=\alpha_k$；样本中心矩一般有偏（例如 $\mathbb{E}m_{n,2}=\frac{n-1}n\mu_2$）；矩估计 $\hat g(\boldsymbol{X})=G(a_{n,1},\dots;m_{n,2},\dots)$ 一般是 $g(\theta)$ 的有偏估计。许多矩估计是渐近无偏的。
2. 相合性：由强大数定律，样本原点矩与样本中心矩都是强相合的。若 $G$ 连续，则矩估计 $\hat g(\boldsymbol{X})$ 是 $g(\theta)=G(\alpha_1,\dots,\alpha_k;\mu_2,\dots,\mu_s)$ 的强相合估计。
3. 渐近正态性：在一定的正则条件下（$2\max(k,s)$ 阶矩有限且 $G$ 可微），$\hat g(\boldsymbol{X})$ 是相合渐近正态估计；这由多元中心极限定理与 Delta 方法（[3.1.14](/3.1.14)）推出。例如 $\sqrt n(\bar X-\mu)\xrightarrow{d}\mathcal{N}(0,\sigma^2)$，$\sqrt n(S_n^2-\sigma^2)\xrightarrow{d}\mathcal{N}(0,\mu_4-\sigma^4)$。

## 3.3. 极大似然估计

### 3.3.1. 似然函数

对分布族 $\mathcal{F}=\{f(\boldsymbol{x};\theta)\colon\theta\in\Theta\}$（$\theta$ 可以是向量），样本的联合密度也记作 $f_\theta(\boldsymbol{x})$ 或 $f(\boldsymbol{x}\mid\theta)$。对固定的观测值 $\boldsymbol{x}$，把它看作 $\theta$ 的函数，就是似然 $L(\theta;\boldsymbol{x})=f(\boldsymbol{x};\theta)$，也记作 $L(\theta\mid\boldsymbol{x})$ 或 $L(\theta,\boldsymbol{x})$；它的对数 $l(\theta;\boldsymbol{x})=\log L(\theta;\boldsymbol{x})$ 是对数似然。

**例 3.3.1** 设 $X_1,\dots,X_{10}$ 是来自 $\mathrm{Ber}(\theta)$（$0<\theta<1$）的随机样本，观测值为 $x_1,\dots,x_{10}$，记 $t=x_1+\cdots+x_{10}$。设 $10$ 次试验中有 $6$ 次成功，即 $t=6$。观测到恰好这些结果的概率为

$$
L(\theta;\boldsymbol{x})=\theta^6(1-\theta)^4,\qquad0<\theta<1,
$$

它是未知参数 $\theta$ 的函数。对 $\theta=0.1,0.2,\dots,0.9$：

| $\theta$ | $0.1$ | $0.2$ | $0.3$ | $0.4$ | $0.5$ | $0.6$ | $0.7$ | $0.8$ | $0.9$ |
|---|---|---|---|---|---|---|---|---|---|
| $L(\theta;\boldsymbol{x})\times10^{4}$ | $0.0066$ | $0.262$ | $1.75$ | $5.31$ | $9.77$ | $11.94$ | $9.53$ | $4.19$ | $0.53$ |

如果 $\theta$ 只可能取这九个值，人们自然会选 $\theta=0.6$，因为它使观测到的 $6$ 次成功最可能发生。注意 $0.6=6/10=t/n$；事实上 $t/n$ 在一切 $0<\theta<1$ 中使似然达到最大（例 3.3.2），$\hat\theta=t/n$ 就是极大似然估计值。

![左：例 3.3.1 中 n = 10 次试验 t = 6 次成功的似然，在 t/n = 0.6 处达到最大，以及 n = 100、t = 60 时的似然，两者都缩放到最大值为 1；样本越大峰越尖。右：例 3.3.12 捕获–再捕获模型的似然，在 N = 49 与 N = 50 处同时达到最大。](./plots/likelihood-functions.py)

**定义 3.3.1（似然函数）** 设 $\boldsymbol{X}=(X_1,\dots,X_n)$ 是来自 $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$ 的随机样本，$f(x;\theta)$ 为密度函数（或概率质量函数），$\boldsymbol{x}=(x_1,\dots,x_n)$ 为观测值。称

$$
L(\theta;\boldsymbol{x})=\prod_{i=1}^nf(x_i;\theta),\qquad\theta\in\Theta
$$
为**似然函数**，$l(\theta;\boldsymbol{x})=\log L(\theta;\boldsymbol{x})=\sum_{i=1}^n\log f(x_i;\theta)$ 为**对数似然函数**。

**定义 3.3.2（极大似然估计）** 在定义 3.3.1 的设定下，设统计量 $\hat\theta=\hat\theta(\boldsymbol{X})$ 满足

$$
L(\hat\theta(\boldsymbol{x});\boldsymbol{x})=\sup_{\theta\in\Theta}L(\theta;\boldsymbol{x})\qquad\text{对一切 }\boldsymbol{x}\in\mathcal{X},
$$
或等价地 $l(\hat\theta(\boldsymbol{x});\boldsymbol{x})=\sup_{\theta\in\Theta}l(\theta;\boldsymbol{x})$，其中 $\mathcal{X}$ 为样本空间。则称 $\hat\theta(\boldsymbol{X})$ 为 $\theta$ 的**极大似然估计量**（MLE），$\hat\theta(\boldsymbol{x})$ 为 $\theta$ 的极大似然估计值。以这种方式估计参数称为**极大似然估计**。

这一定义对离散分布族与连续分布族都适用，也不要求样本独立同分布：对任何联合密度为 $f(\boldsymbol{x};\theta)$ 的模型，都可以极大化 $L(\theta;\boldsymbol{x})=f(\boldsymbol{x};\theta)$。极大似然原理就是选取使观测数据出现的可能性最大的参数值。写出似然之后，求极大似然估计就是纯粹的数学问题，通常有三种做法：

- 求导：$l(\theta;\boldsymbol{x})$ 的驻点若二阶导数为负，则是局部极大值点，还需验证它是全局最大值点；
- 直接分析似然函数，用于似然关于 $\theta$ 不可微的情形（例如支撑依赖于 $\theta$）；
- 数值方法，用计算机极大化 $L(\theta;\boldsymbol{x})$。

### 3.3.2. 用求导法求极大似然估计

当 $l(\theta;\boldsymbol{x})$ 可微且最大值点位于 $\Theta$ 内部时，极大似然估计满足似然方程（likelihood equation）

$$
\frac{\partial l(\theta;\boldsymbol{x})}{\partial\theta_i}=0,\qquad i=1,\dots,k.
$$

单参数时，满足 $l''(\theta_0)<0$ 的解 $\theta_0$ 是局部极大值点。$k$ 个参数时，若 **Hesse 矩阵** $\left(\frac{\partial^2l}{\partial\theta_i\partial\theta_j}\right)$ 在解 $\boldsymbol{\theta}_0$ 处是**负定矩阵**，即对一切非零 $\boldsymbol{\lambda}\in\mathbb{R}^k$ 有 $\boldsymbol{\lambda}^{\mathsf T}\left(\frac{\partial^2l}{\partial\theta_i\partial\theta_j}\Big|_{\boldsymbol{\theta}_0}\right)\boldsymbol{\lambda}<0$，则 $\boldsymbol{\theta}_0$ 是局部极大值点（[2.2](/2.2)）。

**例 3.3.2** 设 $X_1,\dots,X_n$ 是来自 $\mathrm{Ber}(\theta)$（$\theta\in(0,1)$）的随机样本。由 $f(x_i;\theta)=\theta^{x_i}(1-\theta)^{1-x_i}$，$x_i\in\{0,1\}$，

$$
L(\theta;\boldsymbol{x})=\theta^t(1-\theta)^{n-t},\qquad l(\theta;\boldsymbol{x})=t\log\theta+(n-t)\log(1-\theta),\qquad t=x_1+\cdots+x_n.
$$

似然方程 $\frac{t}{\theta}-\frac{n-t}{1-\theta}=0$ 给出 $\theta=t/n$，且 $l''(\theta)=-\frac t{\theta^2}-\frac{n-t}{(1-\theta)^2}<0$ 对一切 $\theta$ 成立。因此 $0<t<n$ 时 $\hat\theta=t/n=\bar x$；$t=0$ 或 $t=n$ 时似然单调，上确界在边界处取到，若把 $\Theta$ 取为 $[0,1]$，仍有 $\hat\theta=\bar x$。

**例 3.3.3** 对来自 $\mathrm{Poi}(\theta)$（$\theta\in(0,\infty)$）的随机样本，$f(x_i;\theta)=\mathrm{e}^{-\theta}\theta^{x_i}/x_i!$，

$$
l(\theta;\boldsymbol{x})=-n\theta+(n\bar x)\log\theta-\log\prod_{i=1}^nx_i!.
$$

由 $l'(\theta)=-n+n\bar x/\theta=0$ 得 $\theta=\bar x$，且 $l''(\theta)=-n\bar x/\theta^2<0$，故 $\hat\theta=\bar x$。

**例 3.3.4** 对来自密度为 $f(x;\theta)=\theta\mathrm{e}^{-\theta x}$（$x>0$）的 $\mathrm{Exp}(\theta)$ 的随机样本，$l(\theta;\boldsymbol{x})=n\log\theta-n\bar x\theta$，$l'(\theta)=n/\theta-n\bar x=0$，$l''(\theta)=-n/\theta^2<0$，故 $\hat\theta=1/\bar x$。

**例 3.3.5** 设 $X_1,\dots,X_n$ 是来自 $\mathcal{N}(\mu,\sigma^2)$ 的随机样本。

1. $\mu$ 未知，$\sigma^2$ 已知：由 $l(\mu)=-n\log(\sqrt{2\pi}\sigma)-\frac1{2\sigma^2}\sum_{i=1}^n(x_i-\mu)^2$ 得 $l'(\mu)=n(\bar x-\mu)/\sigma^2=0$，$l''(\mu)=-n/\sigma^2<0$，故 $\hat\mu=\bar x$。
2. $\sigma^2$ 未知，$\mu$ 已知：由 $l(\sigma^2)=-\frac n2\log(2\pi)-\frac n2\log\sigma^2-\frac1{2\sigma^2}\sum_{i=1}^n(x_i-\mu)^2$，

   $$
   \frac{\partial l}{\partial\sigma^2}=-\frac n{2\sigma^2}+\frac1{2\sigma^4}\sum_{i=1}^n(x_i-\mu)^2=0\quad\Longrightarrow\quad\sigma^2=\frac1n\sum_{i=1}^n(x_i-\mu)^2=:s_\mu^2,
   $$
   且 $\frac{\partial^2l}{\partial(\sigma^2)^2}\Big|_{\sigma^2=s_\mu^2}=\frac n{2s_\mu^4}-\frac{2ns_\mu^2}{2s_\mu^6}=-\frac n{2s_\mu^4}<0$。因此 $\hat\sigma^2=\frac1n\sum_{i=1}^n(x_i-\mu)^2$，它是无偏的。
3. 两者都未知：两个似然方程有唯一解 $\mu=\bar x$，$\sigma^2=\frac1n\sum_{i=1}^n(x_i-\bar x)^2=s_n^2$，该点的 Hesse 矩阵为 $\operatorname{diag}\left(-\frac n{s_n^2},-\frac n{2s_n^4}\right)$，是负定的。因此 $\hat\mu=\bar x$，$\hat\sigma^2=s_n^2$，后者此时是有偏的（例 3.1.2）。

**例 3.3.6** 一个有 $r$ 种结果的多项试验独立重复 $n$ 次。各结果出现次数为 $x_1,\dots,x_r\ge0$，$x_1+\cdots+x_r=n$，似然为

$$
L(p_1,\dots,p_r;\boldsymbol{x})=\frac{n!}{x_1!\cdots x_r!}p_1^{x_1}\cdots p_r^{x_r},\qquad0<p_i<1,\quad p_1+\cdots+p_r=1.
$$

由于 $p_r=1-p_1-\cdots-p_{r-1}$，自由参数有 $r-1$ 个。对 $p_i$（$i=1,\dots,r-1$）求 $\log L$ 的偏导数，得 $\frac{x_i}{p_i}-\frac{x_r}{p_r}=0$，其唯一解为 $p_i=x_i/n$，$i=1,\dots,r$。该点处 $(r-1)\times(r-1)$ 的 Hesse 矩阵的元素为 $-\frac{n^2}{x_i}\delta_{ij}-\frac{n^2}{x_r}$，是正对角矩阵与全 1 矩阵的正倍数之和的相反数，因而负定。故 $\hat p_i=x_i/n$。

**例 3.3.7（Hardy–Weinberg 平衡）** 某基因有两个等位基因 $A$ 与 $a$，$A$ 在总体中的频率为 $\theta$。二倍体的基因型由两个基因组成，在随机交配下各基因型的概率为

| 基因型 | $AA$ | $Aa$ | $aa$ |
|---|---|---|---|
| 概率 | $\theta^2$ | $2\theta(1-\theta)$ | $(1-\theta)^2$ |

在一个随机样本中，$k_1=13$ 人为 $AA$，$k_2=24$ 人为 $Aa$，$k_3=19$ 人为 $aa$。似然为

$$
\mathbb{P}(k_1,k_2,k_3\mid\theta)=\binom{k_1+k_2+k_3}{k_1}\binom{k_2+k_3}{k_2}\theta^{2k_1}[2\theta(1-\theta)]^{k_2}(1-\theta)^{2k_3},
$$

故 $l(\theta)=\text{常数}+(2k_1+k_2)\log\theta+(k_2+2k_3)\log(1-\theta)$。令 $\frac{2k_1+k_2}\theta-\frac{k_2+2k_3}{1-\theta}=0$ 得

$$
\hat\theta=\frac{2k_1+k_2}{2(k_1+k_2+k_3)}=\frac{50}{112}\approx0.446,
$$

即样本中全部基因里 $A$ 所占的比例。

### 3.3.3. 由定义求极大似然估计

**例 3.3.8** 对单个观测 $X\sim\mathrm{U}(0,\theta)$（$\theta>0$），似然为 $L(\theta;x)=\theta^{-1}\boldsymbol{1}_{[x,\infty)}(\theta)$：$\theta<x$ 时为 $0$，$\theta\ge x$ 时为 $1/\theta$，在 $\theta=x$ 处向上跳跃，此后递减。似然方程无解，最大值在跳跃点取到，$\hat\theta=x$。

**例 3.3.9** 设 $X_1,\dots,X_n$ 是来自 $\mathrm{U}(\alpha,\beta)$（$\alpha<\beta$）的随机样本，只有一个端点未知。由 $f(x_i)=\frac1{\beta-\alpha}\boldsymbol{1}_{[\alpha,\beta]}(x_i)$，

$$
L(\alpha,\beta;\boldsymbol{x})=\frac1{(\beta-\alpha)^n}\boldsymbol{1}_{[\alpha,\infty)}(x_{(1)})\,\boldsymbol{1}_{(-\infty,\beta]}(x_{(n)}),
$$

其中 $x_{(1)}=\min_ix_i$ 与 $x_{(n)}=\max_ix_i$ 是两个极端的**次序统计量**。若 $\alpha$ 未知，极大化 $L$ 一方面要求示性函数为 $1$，即 $\alpha\le x_{(1)}$，另一方面要求 $(\beta-\alpha)^{-n}$ 尽可能大，即 $\alpha$ 尽可能接近 $\beta$；因此 $\hat\alpha=x_{(1)}$。若 $\beta$ 未知，同理得 $\hat\beta=x_{(n)}$。

**例 3.3.10** 若 $\alpha$ 与 $\beta$ 都未知，$L(\alpha,\beta;\boldsymbol{x})$ 在 $\alpha\le x_{(1)}$、$x_{(n)}\le\beta$ 且 $\beta-\alpha$ 尽可能小时达到最大，即 $\hat\alpha=x_{(1)}$，$\hat\beta=x_{(n)}$。

极大似然估计不一定唯一，也不一定有闭式解；后一种情形下要用数值方法极大化 $L(\theta;\boldsymbol{x})$，并注意找到的是全局最大值而不是局部极大值。

**例 3.3.11（不唯一性）** 设 $X_1,\dots,X_n$ 是来自 $\mathrm{U}(\theta,\theta+1)$（$\theta\in\mathbb{R}$）的随机样本。若 $\theta\le x_{(1)}$ 且 $x_{(n)}\le\theta+1$，似然等于 $1$，否则为 $0$，即 $L(\theta;\boldsymbol{x})=\boldsymbol{1}\{x_{(n)}-1\le\theta\le x_{(1)}\}$。区间 $[x_{(n)}-1,x_{(1)}]$ 中的每一点都使它达到最大，因此对每个 $0\le\lambda\le1$，

$$
\hat\theta_\lambda=\lambda X_{(1)}+(1-\lambda)(X_{(n)}-1)
$$

都是 $\theta$ 的极大似然估计；在它们之中如何选择须另作考虑（由对称性，取 $\lambda=\frac12$ 较为自然）。

**例 3.3.12（捕获–再捕获）** 为估计某野生动物种群的数量 $N$，先捕获 $10$ 只动物，做标记后放回。几个月后再捕获 $20$ 只，发现其中 $4$ 只带有标记。假定每只动物被捕获的可能性相同，直观的估计由 $10/N=4/20$ 得到 $N=50$。求极大似然估计：若第 $i$ 只再捕获的动物带标记，令 $X_i=1$，否则 $X_i=0$，则 $t=\sum_{i=1}^{20}x_i=4$。$20$ 只中带标记的数目服从超几何分布，故

$$
L(N;x_1,\dots,x_{20})=\frac{\binom{N-10}{16}\binom{10}{4}}{\binom N{20}},\qquad N\ge26.
$$

$N$ 是整数，因此比较相邻的值：$L(N)/L(N-1)=\frac{(N-10)(N-20)}{N(N-26)}\ge1$ 当且仅当 $N\le\frac{10\cdot20}4=50$，且 $N=50$ 时取等号。所以 $L$ 递增到 $N=49$，$L(49)=L(50)$，此后递减：$\hat N=49$ 与 $\hat N=50$ 都是极大似然估计，后者与直观估计一致。一般地，若有 $M$ 只带标记的动物，再捕获 $n$ 只，其中 $t$ 只带标记，则极大似然估计为 $\lfloor Mn/t\rfloor$，当 $Mn/t$ 为整数时出现并列。

### 3.3.4. 指数族中的极大似然估计

对自然形式的**指数族**（[3.2.2](/3.2.2)），似然方程可以一次性写出。设 $\boldsymbol{X}$ 是来自

$$
f(x;\boldsymbol{\theta})=C(\boldsymbol{\theta})\exp\left\{\sum_{i=1}^k\theta_iT_i(x)\right\}h(x),\qquad\boldsymbol{\theta}\in\Theta
$$

的随机样本，其中 $\Theta$ 为自然参数空间，$\Theta_0$ 为 $\Theta$ 的内点集。则

$$
L(\boldsymbol{\theta};\boldsymbol{x})=C^n(\boldsymbol{\theta})\exp\left\{\sum_{i=1}^k\theta_i\sum_{j=1}^nT_i(x_j)\right\}h(\boldsymbol{x}),\qquad l(\boldsymbol{\theta};\boldsymbol{x})=n\log C(\boldsymbol{\theta})+\sum_{i=1}^k\theta_i\sum_{j=1}^nT_i(x_j)+\log h(\boldsymbol{x}),
$$

其中 $h(\boldsymbol{x})=\prod_{j=1}^nh(x_j)$。

**定理 3.3.1** 设该表示是满秩的，即 $T_1(X),\dots,T_k(X)$ 不以概率一满足任何仿射关系。若对样本 $\boldsymbol{x}$，似然方程

$$
\frac n{C(\boldsymbol{\theta})}\frac{\partial C(\boldsymbol{\theta})}{\partial\theta_i}=-\sum_{j=1}^nT_i(x_j),\qquad i=1,\dots,k
$$

在 $\Theta_0$ 中有解，则解唯一，且就是 $\boldsymbol{\theta}$ 的极大似然估计。

**证明** 由推论 2.2.1，记 $D=\log C$，左边等于 $n\,\partial D/\partial\theta_i=-n\,\mathbb{E}_{\boldsymbol{\theta}}T_i(X)$，所以方程组就是 $\mathbb{E}_{\boldsymbol{\theta}}T_i(X)=\frac1n\sum_jT_i(x_j)$：充分统计量的总体均值与样本均值相等。此外 $l$ 的 Hesse 矩阵为 $n\,\partial^2D/\partial\theta_i\partial\theta_j=-n\operatorname{Cov}_{\boldsymbol{\theta}}(T_i(X),T_j(X))$，在满秩假设下负定。因此 $l$ 在凸集 $\Theta$ 上严格凹，$\Theta_0$ 中的驻点是唯一的全局最大值点，而且驻点至多一个。$\square$

因此在指数族中无需检验二阶导数。例如，设 $X_1,\dots,X_m\overset{\text{iid}}{\sim}\mathcal{N}(\mu_1,\sigma^2)$ 与 $Y_1,\dots,Y_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu_2,\sigma^2)$ 是方差相同的两个独立样本，联合密度构成三参数指数族，充分完备统计量为 $\left(\sum X_i,\sum Y_j,\sum X_i^2+\sum Y_j^2\right)$，由似然方程得

$$
\hat\mu_1=\bar X,\qquad\hat\mu_2=\bar Y,\qquad\hat\sigma^2=\frac1{m+n}\left[\sum_{i=1}^m(X_i-\bar X)^2+\sum_{j=1}^n(Y_j-\bar Y)^2\right].
$$

### 3.3.5. 无偏性与不变性

极大似然估计是否无偏取决于具体问题。例 3.3.5 中，$\sigma^2$ 的极大似然估计在 $\mu$ 已知时无偏，在 $\mu$ 未知时有偏。

**例 3.3.13** 设 $X_1,\dots,X_n$ 是来自 $\mathrm{U}(0,\beta)$ 的随机样本。极大似然估计 $\hat\beta=X_{(n)}$（例 3.3.9）的密度为 $\frac{nx^{n-1}}{\beta^n}\boldsymbol{1}_{[0,\beta]}(x)$，故

$$
\mathbb{E}X_{(n)}=\int_0^\beta x\frac{nx^{n-1}}{\beta^n}\,\mathrm{d}x=\frac n{n+1}\beta,
$$

$\hat\beta$ 有偏；纠偏后的 $\hat\beta^*=\frac{n+1}nX_{(n)}$ 无偏。矩估计 $\hat\beta_1=2\bar X$ 也无偏，且

$$
\operatorname{Var}(\hat\beta^*)=\frac{\beta^2}{n(n+2)},\qquad\operatorname{Var}(\hat\beta_1)=\frac{4}{n}\cdot\frac{\beta^2}{12}=\frac{\beta^2}{3n},
$$

所以 $n\ge2$ 时 $\hat\beta^*$ 比 $\hat\beta_1$ 更有效，其方差以 $n^{-2}$ 而不是 $n^{-1}$ 的速度下降。极大似然估计本身是弱相合的：对 $0<\varepsilon<\beta$，

$$
\mathbb{P}(|\hat\beta-\beta|<\varepsilon)=\mathbb{P}(\beta-\varepsilon<X_{(n)}\le\beta)=\int_{\beta-\varepsilon}^\beta\frac{nx^{n-1}}{\beta^n}\,\mathrm{d}x=1-\left(1-\frac\varepsilon\beta\right)^n\to1.
$$

![U(0, 2) 下三个估计量——矩估计 2 倍样本均值、极大似然估计 X_(n) 与纠偏后的 (n+1)/n X_(n)——的偏差、方差与均方误差，每个样本量模拟 5000 个样本。极大似然估计向下偏，但其均方误差远低于无偏的矩估计。](./plots/uniform-estimators.py)

第二个性质与重新参数化有关。在例 3.3.3 中，我们可能想估计概率 $\mathbb{P}_\theta(X=0)=\mathrm{e}^{-\theta}$ 而不是 $\theta$；在例 3.3.4 中 $\mathbb{E}_\theta X=1/\theta$，估计均值 $1/\theta$ 可能更自然。$g(\theta)$ 的极大似然估计如何确定？若 $g$ 不是一一的，不同的 $\theta$ 可以给出同一个值 $\theta^*=g(\theta)$，这时定义诱导似然

$$
L^*(\theta^*;\boldsymbol{x})=\sup_{\{\theta\colon g(\theta)=\theta^*\}}L(\theta;\boldsymbol{x}),
$$

并把 $L^*$ 的最大值点称为 $g(\theta)$ 的极大似然估计。

**定理 3.3.2（极大似然估计的不变性）** 若 $\hat\theta$ 是 $\theta$ 的极大似然估计，则对任意函数 $g(\theta)$，$g(\theta)$ 的极大似然估计为 $g(\hat\theta)$。

**证明** 若 $g$ 是从 $\Theta$ 到 $\Theta^*$ 上的一一映射，则 $L(\theta;\boldsymbol{x})=L(g^{-1}(\theta^*);\boldsymbol{x})=L^*(\theta^*;\boldsymbol{x})$，于是 $\max_{\theta\in\Theta}L(\theta;\boldsymbol{x})=\max_{\theta^*\in\Theta^*}L^*(\theta^*;\boldsymbol{x})$，而由 $L^*(g(\hat\theta);\boldsymbol{x})=L(\hat\theta;\boldsymbol{x})$，$\hat\theta^*=g(\hat\theta)$ 达到这个最大值。一般情形，令 $\hat\theta^*=g(\hat\theta)$。由于 $\hat\theta$ 属于集合 $\{\theta\colon g(\theta)=g(\hat\theta)\}$ 且使 $L$ 整体最大，$L^*(\hat\theta^*;\boldsymbol{x})=\sup_{\{\theta\colon g(\theta)=g(\hat\theta)\}}L(\theta;\boldsymbol{x})=L(\hat\theta;\boldsymbol{x})$。对每个 $\theta^*\in\Theta^*$，

$$
L^*(\theta^*;\boldsymbol{x})=\sup_{\{\theta\colon g(\theta)=\theta^*\}}L(\theta;\boldsymbol{x})\le\max_{\theta\in\Theta}L(\theta;\boldsymbol{x})=L(\hat\theta;\boldsymbol{x})=L^*(\hat\theta^*;\boldsymbol{x}).
$$

因此 $g(\hat\theta)$ 是 $g(\theta)$ 的极大似然估计。$\square$

这个定理来自 P. W. Zehna（*Annals of Mathematical Statistics* 第 37 卷，1966），论证与 $\theta$ 的维数无关。于是 Poisson 模型中 $\mathrm{e}^{-\theta}$ 的极大似然估计为 $\mathrm{e}^{-\bar x}$；$\mathrm{Exp}(\theta)$ 的均值 $1/\theta$ 的极大似然估计为 $\bar x$；$\sigma$ 的极大似然估计在 $\mu$ 已知时为 $\left[\frac1n\sum(x_i-\mu)^2\right]^{1/2}$，在 $\mu$ 未知时为 $\left[\frac1n\sum(x_i-\bar x)^2\right]^{1/2}$。相比之下，无偏性没有不变性：$S^2$ 是 $\sigma^2$ 的无偏估计，$S$ 却是 $\sigma$ 的有偏估计。

### 3.3.6. 充分性、相合性与渐近正态性

**定理 3.3.3** 设 $\boldsymbol{X}$ 是来自 $\{f(x;\theta)\colon\theta\in\Theta\}$ 的随机样本，$T=T(\boldsymbol{X})$ 是 $\theta$ 的充分统计量。若 $\theta$ 的极大似然估计存在，则可以取为 $T$ 的函数；若极大似然估计唯一，则它是 $T$ 的函数。

**证明** 由因子分解定理（定理 2.3.1），$L(\theta;\boldsymbol{x})=g(T(\boldsymbol{x});\theta)h(\boldsymbol{x})$，其中 $h\ge0$ 与 $\theta$ 无关。对 $h(\boldsymbol{x})>0$ 的 $\boldsymbol{x}$，关于 $\theta$ 极大化 $L(\theta;\boldsymbol{x})$ 等价于极大化 $g(T(\boldsymbol{x});\theta)$，而后者只通过 $T(\boldsymbol{x})$ 依赖于 $\boldsymbol{x}$。$\square$

例 3.3.11 说明了这个限定的必要性：若 $\lambda$ 的选取依赖于 $(X_{(1)},X_{(n)})$ 以外的样本信息，不唯一的极大似然估计就不一定是充分统计量的函数。

一般地证明极大似然估计的相合性并不容易。H. Cramér（1946）证明了在正则条件下似然方程的某个根是弱相合的；A. Wald（1949）首次证明了极大似然估计的强相合性，但所用条件相当复杂。

**定理 3.3.4** 设 $\hat\theta_n=\hat\theta_n(X_1,\dots,X_n)$ 是基于密度为 $f(\cdot;\theta)$ 的随机样本的 $\theta\in\Theta\subseteq\mathbb{R}$ 的极大似然估计。在适当的正则条件下，当 $n\to\infty$ 时，在 $\mathbb{P}_\theta$ 下 $\hat\theta_n\xrightarrow{p}\theta$。

证明思路：由弱大数定律，$\frac1n[l(\theta';\boldsymbol{X})-l(\theta;\boldsymbol{X})]\xrightarrow{p}\mathbb{E}_\theta\log\frac{f(X;\theta')}{f(X;\theta)}$；当分布族可识别时，由 Jensen 不等式，它对 $\theta'\ne\theta$ 为负，所以 $n$ 充分大时，真值处的似然大于任何固定的其他值处的似然。

大样本下极大似然估计的精度由下文定义 3.4.3 的 Fisher 信息量 $I(\theta)$ 决定。

**定理 3.3.5** 在定理 3.3.4 的设定和适当的正则条件下，极大似然估计是渐近正态的：在 $\mathbb{P}_\theta$ 下，

$$
\sqrt n(\hat\theta_n-\theta)\xrightarrow{d}\mathcal{N}(0,\sigma_\theta^2),\qquad\sigma_\theta^2=\frac1{I(\theta)},\qquad I(\theta)=\mathbb{E}_\theta\left[\frac\partial{\partial\theta}\log f(X;\theta)\right]^2,\quad X\sim f(\cdot;\theta).
$$

粗略地说，$n$ 很大时 $\hat\theta_n\overset{\cdot}{\sim}\mathcal{N}(\theta,\sigma_\theta^2/n)$，与 $\hat\theta_n$ 有关的概率都可以据此近似计算。证明思路是：用 **Taylor 公式**把得分 $l'(\theta;\boldsymbol{X})$ 在真值 $\theta$ 处展开，利用 $l'(\hat\theta_n;\boldsymbol{X})=0$ 得 $\sqrt n(\hat\theta_n-\theta)\approx\frac{n^{-1/2}l'(\theta)}{-n^{-1}l''(\theta)}$，再对分子（均值为 $0$、方差为 $I(\theta)$ 的独立同分布项之和）用中心极限定理，对分母（趋于 $I(\theta)$）用弱大数定律，并结合 Slutsky 定理（定理 2.1.4）。再结合 Delta 方法（[3.1.14](/3.1.14)），对可微的 $g$ 有

$$
\sqrt n[g(\hat\theta_n)-g(\theta)]\xrightarrow{d}\mathcal{N}\left(0,\frac{[g'(\theta)]^2}{I(\theta)}\right).
$$

由 §3.4.5 的 Cramér–Rao 不等式，$[g'(\theta)]^2/(nI(\theta))$ 是 $g(\theta)$ 的无偏估计所能达到的最小方差，所以极大似然估计是渐近有效的。例 3.3.13 不满足正则条件（支撑依赖于 $\beta$），而 $X_{(n)}$ 也确实以更快的速度 $1/n$ 收敛。

### 3.3.7. 与矩估计的比较

**例 3.3.14** 对 $n=500$ 名香港儿童的身高样本，平均身高的矩估计为 $\bar x=67.9$ 英寸（$172.5$ 厘米）；假定 $\mathcal{N}(\mu,\sigma^2)$，极大似然估计与之相同。对某品牌的 $5$ 只灯泡做寿命试验，寿命分别为 $2,3,1,3,4$ 年。平均寿命的矩估计为 $\bar x=2.6$ 年；假定 $\mathrm{Exp}(\theta)$，$\mathbb{E}X=\theta^{-1}=g(\theta)$，由不变性，$g(\theta)$ 的极大似然估计也是 $\bar x=2.6$。从 $\mathrm{Exp}(2.6)$（均值 $1/2.6\approx0.385$）中模拟抽样，均值的极大似然估计 $\bar X$ 在 $n=5,50,100,500$ 时的经验方差为 $0.0307$、$0.00293$、$0.00149$、$0.000301$，接近精确值 $\frac{1}{2.6^2n}=0.0296$、$0.00296$、$0.00148$、$0.000296$。

| | 矩估计法 | 极大似然估计 |
|---|---|---|
| 模型 | 只需矩存在，不需要分布形式 | 必须知道密度的形式 |
| 计算 | 通常有显式解 | 可能需要数值优化 |
| 无偏性 | 原点矩无偏，其余一般有偏 | 取决于具体问题 |
| 大样本性质 | 相合、渐近正态 | 相合、渐近正态且渐近有效 |
| 不变性 | 不具有不变性（如例 3.2.7） | 具有不变性（定理 3.3.2） |
| 稳健性 | 对模型误差常较稳健 | 模型错误时可能很差 |

若统计模型是良好的近似，极大似然估计通常比矩估计更有效；若不是，极大似然估计可能很差，而矩估计往往更稳健。

## 3.4. 一致最小方差无偏估计

### 3.4.1. 定义与存在性

在无偏估计类中，均方误差等于方差，因此自然的最优准则是对参数的每个取值方差都最小。

**定义 3.4.1（一致最小方差无偏估计）** 设 $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$ 是参数分布族，$\boldsymbol{X}=(X_1,\dots,X_n)$ 是随机样本。若 $g(\theta)$ 的无偏估计 $U(\boldsymbol{X})$ 对 $g(\theta)$ 的每个无偏估计 $V(\boldsymbol{X})$ 都满足

$$
\operatorname{Var}_\theta(U)\le\operatorname{Var}_\theta(V)\qquad\text{对一切 }\theta\in\Theta,
$$
则称 $U(\boldsymbol{X})$ 为 $g(\theta)$ 的**一致最小方差无偏估计**（UMVUE）。

无偏估计不一定存在。存在无偏估计的函数 $g(\theta)$ 称为可估的。

**例 3.4.1** 设 $X\sim\mathrm{Bin}(n,p)$，$0<p<1$，则 $g(p)=1/p$ 没有无偏估计。事实上，若 $\delta(X)$ 无偏，则对一切 $p\in(0,1)$ 有 $\sum_{i=0}^n\delta(i)\binom ni p^i(1-p)^{n-i}=\frac1p$，即

$$
\sum_{i=0}^n\delta(i)\binom nip^{i+1}(1-p)^{n-i}-1=0\qquad\text{对一切 }p\in(0,1).
$$

左边是 $p$ 的次数至多为 $n+1$ 的多项式，且不恒为零（它在 $p=0$ 处的值为 $-1$），至多有 $n+1$ 个根，矛盾。

求一致最小方差无偏估计有三种方法：零无偏估计法、充分完备统计量法（Lehmann–Scheffé）以及 Cramér–Rao 不等式。它们都以 Rao–Blackwell 定理为基础。

### 3.4.2. Rao–Blackwell 定理

**定理 3.4.1（Rao–Blackwell 定理）** 设 $T=T(\boldsymbol{X})$ 是 $\theta$ 的充分统计量，$\hat g(\boldsymbol{X})$ 是 $g(\theta)$ 的无偏估计。则 $h(T)=\mathbb{E}_\theta[\hat g(\boldsymbol{X})\mid T]$ 是 $g(\theta)$ 的无偏估计，且

$$
\operatorname{Var}_\theta(h(T))\le\operatorname{Var}_\theta(\hat g(\boldsymbol{X}))\qquad\text{对一切 }\theta\in\Theta,
$$

对给定的 $\theta$ 等号成立当且仅当 $\mathbb{P}_\theta(\hat g(\boldsymbol{X})=h(T))=1$。

**证明** 由于 $T$ 充分，给定 $T$ 时 $\boldsymbol{X}$ 的条件分布与 $\theta$ 无关，所以 $h(T)$ 不依赖于 $\theta$，是统计量。由重期望公式（[3.1.9](/3.1.9)），$\mathbb{E}_\theta h(T)=\mathbb{E}_\theta\{\mathbb{E}[\hat g\mid T]\}=\mathbb{E}_\theta\hat g=g(\theta)$。又

$$
\operatorname{Var}_\theta(\hat g)=\mathbb{E}_\theta[\hat g-h(T)+h(T)-g(\theta)]^2=\mathbb{E}_\theta[\hat g-h(T)]^2+\operatorname{Var}_\theta(h(T))+2\,\mathbb{E}_\theta\{[\hat g-h(T)][h(T)-g(\theta)]\}.
$$

对 $T$ 取条件，交叉项为 $2\,\mathbb{E}_\theta\{[h(T)-g(\theta)]\,\mathbb{E}[\hat g-h(T)\mid T]\}=0$。因此 $\operatorname{Var}_\theta(\hat g)=\operatorname{Var}_\theta(h(T))+\mathbb{E}_\theta[\hat g-h(T)]^2\ge\operatorname{Var}_\theta(h(T))$，等号成立当且仅当 $\hat g=h(T)$ 以概率一成立。$\square$

因此，把无偏估计对充分统计量取条件期望不会增大方差，而且只要该估计不是 $T$ 的函数，方差就严格减小。由此，若一致最小方差无偏估计存在，它可以取为充分统计量的函数。

**例 3.4.2** 设 $X_1,\dots,X_n$ 是来自 $\mathrm{Ber}(p)$ 的随机样本。估计量 $X_1$ 是 $p$ 的无偏估计，$T=\sum_{i=1}^nX_i$ 是充分统计量。对 $t\ge1$，

$$
h(t)=\mathbb{E}(X_1\mid T=t)=\frac{\mathbb{P}(X_1=1,\ X_2+\cdots+X_n=t-1)}{\mathbb{P}(T=t)}=\frac{p\binom{n-1}{t-1}p^{t-1}(1-p)^{n-t}}{\binom ntp^t(1-p)^{n-t}}=\frac tn,
$$

且 $h(0)=0$。可见 Rao–Blackwell 化把 $X_1$ 变成了 $\bar X$，方差从 $p(1-p)$ 降为 $p(1-p)/n$。$\bar X$ 是一致最小方差无偏估计吗？下面两小节给出肯定的回答。

### 3.4.3. 零无偏估计法

若统计量 $l(\boldsymbol{X})$ 对一切 $\theta$ 满足 $\mathbb{E}_\theta l(\boldsymbol{X})=0$，则它是零的无偏估计。把它加到一个无偏估计上仍保持无偏，因此一个无偏估计是最优的，恰好当它不能用这种方式改进。

**定理 3.4.2** 设 $\hat g(\boldsymbol{X})$ 是 $g(\theta)$ 的无偏估计，且对一切 $\theta\in\Theta$ 有 $\operatorname{Var}_\theta(\hat g)<\infty$。若对每个对一切 $\theta$ 满足 $\mathbb{E}_\theta l(\boldsymbol{X})=0$ 与 $\operatorname{Var}_\theta(l)<\infty$ 的统计量 $l(\boldsymbol{X})$，都有

$$
\operatorname{Cov}_\theta(\hat g,l)=\mathbb{E}_\theta[\hat g(\boldsymbol{X})l(\boldsymbol{X})]=0\qquad\text{对一切 }\theta\in\Theta,
$$

则 $\hat g(\boldsymbol{X})$ 是 $g(\theta)$ 的一致最小方差无偏估计。

**证明** 设 $\hat g_1$ 是 $g(\theta)$ 的任一方差有限的无偏估计（方差无限时无需证明），令 $l=\hat g_1-\hat g$。则 $\mathbb{E}_\theta l=0$，且

$$
\operatorname{Var}_\theta(\hat g_1)=\operatorname{Var}_\theta(\hat g+l)=\operatorname{Var}_\theta(\hat g)+\operatorname{Var}_\theta(l)+2\operatorname{Cov}_\theta(\hat g,l)=\operatorname{Var}_\theta(\hat g)+\operatorname{Var}_\theta(l)\ge\operatorname{Var}_\theta(\hat g).\qquad\square
$$

这个条件也是必要的：若对某个 $l$ 与 $\theta_0$ 有 $\operatorname{Cov}_{\theta_0}(\hat g,l)\ne0$，则取 $c=\operatorname{Cov}_{\theta_0}(\hat g,l)/\operatorname{Var}_{\theta_0}(l)$，$\hat g-cl$ 在 $\theta_0$ 处的方差更小。这个准则能验证候选估计是一致最小方差无偏估计，却不能构造它。结合 Rao–Blackwell 定理，只需检验充分统计量的函数。

**推论 3.4.1** 设 $T$ 是充分统计量，$h(T)$ 是 $g(\theta)$ 的方差有限的无偏估计。若对每个对一切 $\theta$ 满足 $\mathbb{E}_\theta\delta(T)=0$ 的 $\delta(T)$，都有 $\operatorname{Cov}_\theta(h(T),\delta(T))=0$ 对一切 $\theta$ 成立，则 $h(T)$ 是 $g(\theta)$ 的一致最小方差无偏估计。

**例 3.4.3** 在例 3.4.2 中，设 $\delta(T)$ 对一切 $p$ 满足 $\mathbb{E}_p\delta(T)=0$，记 $a_i=\delta(i)$。则 $\sum_{i=0}^na_i\binom nip^i(1-p)^{n-i}=0$；两边除以 $(1-p)^n$ 并令 $\varphi=p/(1-p)\in(0,\infty)$，得 $\sum_{i=0}^na_i\binom ni\varphi^i=0$ 对一切 $\varphi>0$ 成立，所以一切 $a_i=0$，$\delta\equiv0$。于是 $\operatorname{Cov}_p(\bar X,\delta(T))=0$，$\bar X$ 是 $p$ 的一致最小方差无偏估计。

**例 3.4.4** 设 $X_1,\dots,X_n$ 是来自 $\mathrm{U}(0,\theta)$ 的随机样本。极大似然估计 $T=X_{(n)}$ 充分但有偏，$h(T)=\frac{n+1}nT$ 无偏，方差为 $\frac{\theta^2}{n(n+2)}$（例 3.3.13）。若 $\mathbb{E}_\theta\delta(T)=\int_0^\theta\delta(t)\frac{nt^{n-1}}{\theta^n}\,\mathrm{d}t=0$ 对一切 $\theta>0$ 成立，则 $\int_0^\theta\delta(t)t^{n-1}\,\mathrm{d}t=0$ 对一切 $\theta$ 成立，求导得 $\delta(\theta)\theta^{n-1}=0$，所以 $\delta=0$（几乎处处）。因此 $\frac{n+1}nX_{(n)}$ 是 $\theta$ 的一致最小方差无偏估计，$\frac{n+1}{2n}X_{(n)}$ 是均值 $\theta/2$ 的一致最小方差无偏估计，优于无偏的 $\bar X$。可见哪个估计量最优取决于模型：对正态总体，$\bar X$ 是均值的一致最小方差无偏估计（例 3.4.7）。

在这两个例子中，$T$ 的零无偏估计都被迫为零，这恰好是 $T$ 的完备性（定义 2.3.3）。由此得到一般的方法。

### 3.4.4. Lehmann–Scheffé 定理

**定理 3.4.3（Lehmann–Scheffé 定理）** 设 $T(\boldsymbol{X})$ 是 $\theta$ 的充分完备统计量。若 $\hat g(T)$ 是 $g(\theta)$ 的无偏估计，则 $\hat g(T)$ 是 $g(\theta)$ 的（以概率一）唯一的一致最小方差无偏估计。特别地，对 $g(\theta)$ 的任一无偏估计 $U$，$\mathbb{E}(U\mid T)$ 就是一致最小方差无偏估计。

**证明** 先证在 $T$ 的函数中的唯一性：若 $\hat g_1(T)$ 是另一个无偏估计，则 $\delta(T)=\hat g(T)-\hat g_1(T)$ 对一切 $\theta$ 满足 $\mathbb{E}_\theta\delta(T)=0$，由完备性 $\mathbb{P}_\theta(\delta(T)=0)=1$。

再证最优性：设 $U$ 是任一无偏估计。由 Rao–Blackwell 定理，$h(T)=\mathbb{E}(U\mid T)$ 无偏，且 $\operatorname{Var}_\theta(h(T))\le\operatorname{Var}_\theta(U)$。由唯一性，$\hat g(T)=h(T)$ 以概率一成立，故 $\operatorname{Var}_\theta(\hat g(T))\le\operatorname{Var}_\theta(U)$ 对一切 $\theta$ 成立。$\square$

这个定理（E. L. Lehmann 与 H. Scheffé，1950）对多维 $\theta$ 同样成立。它给出两种做法：找一个充分完备统计量的无偏函数，通常是计算 $T$ 的简单函数的期望再加以调整；或者把任一简单的无偏估计对 $T$ 取条件期望。对满秩指数族，自然充分统计量是完备的（定理 2.3.2）。

**例 3.4.5** 对 $\mathrm{Ber}(\theta)$，$T=\sum_{i=1}^nX_i\sim\mathrm{Bin}(n,\theta)$ 是充分完备统计量（例 2.3.7），所以 $\bar X=T/n$ 是 $\theta$ 的一致最小方差无偏估计。对 $g(\theta)=\theta(1-\theta)$：$\mathbb{E}T=n\theta$，$\mathbb{E}T^2=n\theta(1-\theta)+n^2\theta^2=\mathbb{E}T+n(n-1)\theta^2$，故 $\theta^2=\mathbb{E}\left[\frac{T^2-T}{n(n-1)}\right]$，从而

$$
\frac Tn-\frac{T^2-T}{n(n-1)}=\frac{T(n-T)}{n(n-1)}
$$

是 $\theta(1-\theta)$ 的无偏估计；它是 $T$ 的函数，因而是一致最小方差无偏估计。注意它等于 $\frac n{n-1}\bar X(1-\bar X)$，即例 3.2.3 中矩估计的纠偏形式。

**例 3.4.6** 设 $X_1,\dots,X_n$ 是来自 $\mathrm{Poi}(\theta)$ 的随机样本，$T=\sum X_i\sim\mathrm{Poi}(n\theta)$ 是充分完备统计量。

1. $\bar X$ 是 $\theta$ 的一致最小方差无偏估计。
2. 对 $g(\theta)=\theta^r$（$r$ 为正整数），无偏的 $\delta(T)$ 必须满足 $\sum_{t=0}^\infty\delta(t)\frac{(n\theta)^t}{t!}\mathrm{e}^{-n\theta}=\theta^r$，即

   $$
   \sum_{t=0}^\infty\delta(t)\frac{n^t\theta^t}{t!}=\theta^r\mathrm{e}^{n\theta}=\sum_{t=r}^\infty\frac{n^{t-r}\theta^t}{(t-r)!}.
   $$
   比较系数，$t<r$ 时 $\delta(t)=0$，$t\ge r$ 时 $\delta(t)=\frac{n^{t-r}/(t-r)!}{n^t/t!}=\frac{t(t-1)\cdots(t-r+1)}{n^r}$，这就是 $\theta^r$ 的一致最小方差无偏估计。
3. 对 $g(\theta)=\mathbb{P}_\theta(X_1=x)=\mathrm{e}^{-\theta}\theta^x/x!$，示性函数 $U=\boldsymbol{1}\{X_1=x\}$ 无偏；由于 $X_1$ 与 $X_2+\cdots+X_n\sim\mathrm{Poi}((n-1)\theta)$ 独立，

   $$
   \mathbb{E}(U\mid T=t)=\frac{\mathbb{P}(X_1=x)\,\mathbb{P}(X_2+\cdots+X_n=t-x)}{\mathbb{P}(T=t)}=\binom tx\frac{(n-1)^{t-x}}{n^t}=\binom tx\left(\frac1n\right)^x\left(1-\frac1n\right)^{t-x}
   $$
   （$t\ge x$；$t<x$ 时为 $0$）是一致最小方差无偏估计。与之比较，极大似然估计 $\mathrm{e}^{-\bar X}\bar X^x/x!$ 是有偏的。

**例 3.4.7** 设 $X_1,\dots,X_n$ 是来自 $\mathcal{N}(\mu,\sigma^2)$ 的随机样本。则 $T_1=\bar X$ 与 $T_2=\sum_{i=1}^n(X_i-\bar X)^2$ 独立，$T_1\sim\mathcal{N}(\mu,\sigma^2/n)$，$T_2/\sigma^2\sim\chi^2_{n-1}$，且 $(T_1,T_2)$ 是充分完备统计量（例 2.3.10）。

1. $\bar X$ 是 $\mu$ 的一致最小方差无偏估计，$S^2=T_2/(n-1)$ 是 $\sigma^2$ 的一致最小方差无偏估计。
2. 对 $g=\sigma^r$（$r>-(n-1)$），利用 $\mathbb{E}(\chi^2_{n-1})^{r/2}=2^{r/2}\Gamma\left(\frac{n-1+r}2\right)/\Gamma\left(\frac{n-1}2\right)$，

   $$
   \mathbb{E}\left[K_{n-1,r}T_2^{r/2}\right]=\sigma^r,\qquad K_{n-1,r}=\frac{\Gamma\left(\frac{n-1}2\right)}{2^{r/2}\Gamma\left(\frac{n-1+r}2\right)},
   $$
   所以 $K_{n-1,r}T_2^{r/2}$ 是 $\sigma^r$ 的一致最小方差无偏估计；$r=1$ 时它修正了 $S$ 作为 $\sigma$ 的估计的偏差。
3. 对 $g=\mu/\sigma^2$ 与 $n>3$：$\mathbb{E}(1/T_2)=\frac1{(n-3)\sigma^2}$，由独立性 $\mathbb{E}\left[\frac{(n-3)T_1}{T_2}\right]=\frac{\mu}{\sigma^2}$，所以 $(n-3)\bar X/T_2$ 是 $\mu/\sigma^2$ 的一致最小方差无偏估计。

### 3.4.5. Cramér–Rao 不等式

Cramér–Rao 不等式（C. R. Rao，1945；H. Cramér，1946）给出无偏估计方差的下界。达到下界的无偏估计就是一致最小方差无偏估计。但下界可能连一致最小方差无偏估计也达不到，所以这一方法不总是奏效；它更广泛的意义在于定义了估计量的效率与 Fisher 信息量，而后者是大样本理论的核心。除非另作说明，以下 $\theta$ 都是一维的。

**定义 3.4.2（Cramér–Rao 正则分布族）** 若分布族 $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$ 满足以下条件，则称它为 **Cramér–Rao 正则分布族**：

1. $\Theta$ 是 $\mathbb{R}$ 中的开区间；
2. 支撑 $\{x\colon f(x;\theta)>0\}$ 与 $\theta$ 无关；
3. 对支撑中的一切 $x$ 与一切 $\theta\in\Theta$，$\frac{\partial f(x;\theta)}{\partial\theta}$ 存在；
4. 积分与求导可以交换：$\frac\partial{\partial\theta}\int f(x;\theta)\,\mathrm{d}x=\int\frac{\partial f(x;\theta)}{\partial\theta}\,\mathrm{d}x$；
5. 对一切 $\theta\in\Theta$ 有 $0<I(\theta)<\infty$，其中 $I(\theta)$ 的定义见下。

**定义 3.4.3（Fisher 信息量）** 对满足定义 3.4.2 中条件 1–3 的分布族，单个观测的**得分函数**为 $s(x;\theta)=\frac{\partial}{\partial\theta}\log f(x;\theta)$，称

$$
I(\theta)=\mathbb{E}_\theta\left[\frac{\partial\log f(X;\theta)}{\partial\theta}\right]^2
$$
为单个观测所含的 **Fisher 信息量**。

$I(\theta)$ 衡量一个观测所含关于 $\theta$ 的信息：密度随 $\theta$ 变化越剧烈，$I(\theta)$ 越大。对随机样本，各观测的得分相加，$(X_1,\dots,X_n)$ 所含的信息量为 $nI(\theta)$。Fisher 信息量也决定了极大似然估计的渐近精度（定理 3.3.5）。若进一步 $f$ 关于 $\theta$ 二阶可微且二阶导数也可以在积分号下求得，则 $I(\theta)=-\mathbb{E}_\theta\left[\frac{\partial^2\log f(X;\theta)}{\partial\theta^2}\right]$，这往往更容易计算。

**定理 3.4.4（Cramér–Rao 不等式）** 设 $\mathcal{F}$ 是 Cramér–Rao 正则分布族，$g(\theta)$ 是 $\Theta$ 上的可微函数，$\hat g(\boldsymbol{X})$ 是基于容量为 $n$ 的随机样本的 $g(\theta)$ 的无偏估计，且 $\int\hat g(\boldsymbol{x})f(\boldsymbol{x};\theta)\,\mathrm{d}\boldsymbol{x}$ 可以在积分号下求导。则

$$
\operatorname{Var}_\theta(\hat g(\boldsymbol{X}))\ge\frac{[g'(\theta)]^2}{nI(\theta)}\qquad\text{对一切 }\theta\in\Theta.
$$

特别地，$\theta$ 的无偏估计满足 $\operatorname{Var}_\theta(\hat\theta)\ge\frac1{nI(\theta)}$。

**证明** 令 $S(\boldsymbol{x};\theta)=\frac\partial{\partial\theta}\log f(\boldsymbol{x};\theta)=\sum_{i=1}^n\frac\partial{\partial\theta}\log f(x_i;\theta)$ 为样本的得分。由条件 3、4，

$$
\mathbb{E}_\theta\left[\frac\partial{\partial\theta}\log f(X_i;\theta)\right]=\int\frac{\partial f(x;\theta)}{\partial\theta}\,\mathrm{d}x=\frac\partial{\partial\theta}\int f(x;\theta)\,\mathrm{d}x=0,
$$

所以 $\mathbb{E}_\theta S=0$，由独立性 $\operatorname{Var}_\theta(S)=nI(\theta)$。对 $g(\theta)=\int\hat g(\boldsymbol{x})f(\boldsymbol{x};\theta)\,\mathrm{d}\boldsymbol{x}$ 在积分号下求导，

$$
g'(\theta)=\int\hat g(\boldsymbol{x})\frac{\partial f(\boldsymbol{x};\theta)}{\partial\theta}\,\mathrm{d}\boldsymbol{x}=\mathbb{E}_\theta[\hat g(\boldsymbol{X})S(\boldsymbol{X};\theta)]=\operatorname{Cov}_\theta(\hat g,S).
$$

由 Cauchy–Schwarz 不等式（[3.1.8](/3.1.8)），$[g'(\theta)]^2\le\operatorname{Var}_\theta(\hat g)\operatorname{Var}_\theta(S)=nI(\theta)\operatorname{Var}_\theta(\hat g)$。$\square$

**注 3.4.1** 对给定的 $\theta$，等号成立当且仅当 $\hat g-g(\theta)$ 与 $S$ 以概率一线性相关，$S(\boldsymbol{X};\theta)=a(\theta)[\hat g(\boldsymbol{X})-g(\theta)]$。要求这对每个 $\theta$ 成立并关于 $\theta$ 积分，可知 $f(\boldsymbol{x};\theta)$ 必须具有指数族的形式，且 $\hat g$ 是其充分统计量。因此：

- 方差对每个 $\theta$ 都达到下界的无偏估计是一致最小方差无偏估计；
- 指数族（在通常的参数空间上）满足正则条件；
- 下界只能在指数族中达到，而且即使在指数族中，也只有自然充分统计量 $T$ 的特定函数 $g(\theta)=\mathbb{E}_\theta T$（及其仿射变换）的无偏估计能达到；
- 因此一致最小方差无偏估计的方差可能大于下界，例如例 3.4.10 中的 $\sigma^2$。

**例 3.4.8** 对 $\mathrm{Ber}(\theta)$，$\log f=x\log\theta+(1-x)\log(1-\theta)$，$\frac{\partial\log f}{\partial\theta}=\frac x\theta-\frac{1-x}{1-\theta}=\frac{x-\theta}{\theta(1-\theta)}$，故 $I(\theta)=\frac{\operatorname{Var}(X)}{\theta^2(1-\theta)^2}=\frac1{\theta(1-\theta)}$。$\theta$ 的无偏估计的下界为 $\frac{\theta(1-\theta)}n=\operatorname{Var}(\bar X)$。

**例 3.4.9** 对 $\mathrm{Poi}(\theta)$，$\frac{\partial\log f}{\partial\theta}=\frac x\theta-1$，$I(\theta)=\frac1\theta$，下界 $\frac\theta n$ 等于 $\operatorname{Var}(\bar X)$。对密度为 $\theta\mathrm{e}^{-\theta x}$ 的 $\mathrm{Exp}(\theta)$，$\frac{\partial\log f}{\partial\theta}=\frac1\theta-x$，$I(\theta)=\operatorname{Var}(X)=\frac1{\theta^2}$；对 $g(\theta)=1/\theta$，下界为 $\frac{(1/\theta^2)^2}{n/\theta^2}=\frac1{n\theta^2}=\operatorname{Var}(\bar X)$，所以 $\bar X$ 是均值 $1/\theta$ 的一致最小方差无偏估计。对 $\sigma^2$ 已知的 $\mathcal{N}(\mu,\sigma^2)$，$I(\mu)=1/\sigma^2$，下界 $\sigma^2/n$ 由 $\bar X$ 达到。若 $\mu$ 已知，$I(\sigma^2)=\frac1{2\sigma^4}$，下界 $\frac{2\sigma^4}n$ 由 $S_\mu^2=\frac1n\sum_{i=1}^n(X_i-\mu)^2$ 达到，因此它是 $\sigma^2$ 的一致最小方差无偏估计。

对 $k$ 维参数 $\boldsymbol{\theta}=(\theta_1,\dots,\theta_k)^{\mathsf T}$，若 $A-B$ 是**半正定矩阵**，记 $A\succeq B$。在类似的正则条件下，$\boldsymbol{\theta}$ 的每个无偏估计 $\hat{\boldsymbol{\theta}}$ 满足

$$
\operatorname{Cov}_{\boldsymbol{\theta}}(\hat{\boldsymbol{\theta}})\succeq[nI(\boldsymbol{\theta})]^{-1},\qquad I_{ij}(\boldsymbol{\theta})=\mathbb{E}_{\boldsymbol{\theta}}\left[\frac{\partial\log f(X;\boldsymbol{\theta})}{\partial\theta_i}\frac{\partial\log f(X;\boldsymbol{\theta})}{\partial\theta_j}\right],
$$

其中 $I(\boldsymbol{\theta})=(I_{ij}(\boldsymbol{\theta}))$ 是 Fisher 信息矩阵（Fisher information matrix）。特别地，由对角元得 $\operatorname{Var}(\hat\theta_i)\ge\{[nI(\boldsymbol{\theta})]^{-1}\}_{ii}$。

**例 3.4.10** 对 $\mathcal{N}(\mu,\sigma^2)$，取 $\boldsymbol{\theta}=(\theta_1,\theta_2)=(\mu,\sigma^2)$，

$$
\frac{\partial\log f}{\partial\theta_1}=\frac{x-\theta_1}{\theta_2},\qquad\frac{\partial\log f}{\partial\theta_2}=\frac{(x-\theta_1)^2-\theta_2}{2\theta_2^2},
$$

故 $I_{11}=\frac1{\sigma^2}$，$I_{22}=\frac{\mathbb{E}[(X-\mu)^2-\sigma^2]^2}{4\sigma^8}=\frac1{2\sigma^4}$，$I_{12}=\frac{\mathbb{E}(X-\mu)^3-\sigma^2\mathbb{E}(X-\mu)}{2\sigma^6}=0$。因此

$$
[nI(\boldsymbol{\theta})]^{-1}=\begin{bmatrix}\sigma^2/n&0\\0&2\sigma^4/n\end{bmatrix}.
$$

$\bar X$ 对 $\mu$ 达到下界，而一致最小方差无偏估计 $S^2$ 的方差 $\operatorname{Var}(S^2)=\frac{2\sigma^4}{n-1}>\frac{2\sigma^4}n$。

### 3.4.6. 有效估计

**定义 3.4.4（效率）** 在定理 3.4.4 的条件下，$g(\theta)$ 的无偏估计 $\hat g(\boldsymbol{X})$ 的**效率**为

$$
e_{\hat g}(\theta)=\frac{[g'(\theta)]^2/(nI(\theta))}{\operatorname{Var}_\theta(\hat g(\boldsymbol{X}))},\qquad0<e_{\hat g}(\theta)\le1.
$$
若对一切 $\theta$ 有 $e_{\hat g}(\theta)=1$，则称 $\hat g$ 为**有效估计**；若对一切 $\theta$ 有 $\lim_{n\to\infty}e_{\hat g}(\theta)=1$，则称它是**渐近有效**的。

由例 3.4.8–3.4.10，在 Bernoulli 与 Poisson 模型中 $\bar X$ 是 $\theta$ 的有效估计，对 $\mathrm{Exp}(\theta)$ 的均值 $1/\theta$ 以及正态模型中的 $\mu$ 也是有效估计。在 $\mu$ 未知的正态模型中，$S^2$ 的效率为 $\frac{2\sigma^4/n}{2\sigma^4/(n-1)}=\frac{n-1}n<1$：它是一致最小方差无偏估计但不是有效估计，只是渐近有效。效率是相对 Cramér–Rao 下界定义的，只有在定理 3.4.4 的正则条件成立时才有意义；$\mathrm{U}(0,\theta)$ 不满足这些条件，其一致最小方差无偏估计 $\frac{n+1}nX_{(n)}$ 的方差是 $n^{-2}$ 阶的，低于任何形如 $c/n$ 的下界。

## 3.5. 线性回归中的矩估计与极大似然估计

### 3.5.1. 简单线性回归模型

Ames 房价数据记录了美国艾奥瓦州 Ames 约 $2000$ 笔房屋交易（2006–2010），含 $82$ 个变量。为了用地上居住面积 $x$（自变量）预测售价 $y$（因变量），考虑简单线性回归模型（simple linear regression model）

$$
y_i=\beta_0+\beta_1x_i+\varepsilon_i,\qquad i=1,\dots,n,
$$

其中 $x_i$ 视为固定的，$\beta_0,\beta_1$ 是未知系数，不可观测的随机误差满足 $\mathbb{E}\varepsilon_i=0$、$\operatorname{Var}(\varepsilon_i)=\sigma^2$ 且独立同分布。直线 $y=\beta_0+\beta_1x$ 是总体回归直线；对估计值 $\hat\beta_0,\hat\beta_1$，样本回归直线 $\hat y=\hat\beta_0+\hat\beta_1x$ 给出拟合值 $\hat y_i=\hat\beta_0+\hat\beta_1x_i$ 与残差 $\hat\varepsilon_i=y_i-\hat y_i$。

### 3.5.2. 最小二乘、矩估计与似然

普通**最小二乘法**的估计量使残差平方和最小，

$$
(\hat\beta_0,\hat\beta_1)=\arg\min_{\beta_0,\beta_1}\operatorname{RSS}(\beta_0,\beta_1),\qquad\operatorname{RSS}(\beta_0,\beta_1)=\sum_{i=1}^n(y_i-\beta_0-\beta_1x_i)^2,
$$

令偏导数为零得

$$
\hat\beta_1=\frac{S_{xy}}{S_{xx}}=\frac{\sum_{i=1}^n(x_i-\bar x)(y_i-\bar y)}{\sum_{i=1}^n(x_i-\bar x)^2},\qquad\hat\beta_0=\bar y-\hat\beta_1\bar x.
$$

使用平方是因为它给出显式公式；另一种选择是最小一乘法，极小化 $\sum|y_i-\hat y_i|$，它对异常值更稳健。误差方差用 $\hat\sigma_n^2=\frac1n\sum_{i=1}^n\hat\varepsilon_i^2$ 估计，或用纠偏后的无偏估计 $\hat\sigma^2=\frac1{n-2}\sum_{i=1}^n\hat\varepsilon_i^2$。对 Ames 数据，拟合直线为 $\widehat{\text{SalePrice}}=6759.9+115.79\times\text{LivingArea}$（单位为美元与平方英尺），$\hat\sigma_n=54\,387$，$\hat\sigma=54\,414$。

就矩估计而言，假定 $\mathbb{E}(\varepsilon\mid x)=0$ 蕴含矩条件 $\mathbb{E}\varepsilon=0$ 与 $\mathbb{E}(x\varepsilon)=0$。它们的样本形式

$$
\frac1n\sum_{i=1}^n(y_i-\beta_0-\beta_1x_i)=0,\qquad\frac1n\sum_{i=1}^nx_i(y_i-\beta_0-\beta_1x_i)=0
$$

恰好是最小二乘的正规方程，所以矩估计与最小二乘估计相同；$\sigma^2$ 的矩估计是 $\hat\sigma_n^2$，$\hat\sigma^2$ 是它的纠偏形式。

就极大似然估计而言，再假定 $\varepsilon_i\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$，等价地 $y_i\mid x_i\sim\mathcal{N}(\beta_0+\beta_1x_i,\sigma^2)$ 相互独立。似然为

$$
L(\beta_0,\beta_1,\sigma^2)=(2\pi\sigma^2)^{-n/2}\exp\left\{-\frac1{2\sigma^2}\sum_{i=1}^n(y_i-\beta_0-\beta_1x_i)^2\right\},
$$

故 $l=-\frac n2\log(2\pi\sigma^2)-\frac{\operatorname{RSS}(\beta_0,\beta_1)}{2\sigma^2}$。对每个 $\sigma^2$，$l$ 关于 $(\beta_0,\beta_1)$ 的极大化就是 RSS 的极小化，所以系数的极大似然估计就是最小二乘估计；再由 $\partial l/\partial\sigma^2=0$ 得 $\hat\sigma^2_{\mathrm{MLE}}=\frac1n\operatorname{RSS}(\hat\beta_0,\hat\beta_1)=\hat\sigma_n^2$。

### 3.5.3. 多元线性回归

有 $p$ 个自变量时，模型为 $y_i=\beta_0+\beta_1x_{i1}+\cdots+\beta_px_{ip}+\varepsilon_i$。对 Ames 数据，用居住面积、地块面积与是否有中央空调（$0/1$ 变量）得到 $\widehat{\text{SalePrice}}=-39\,570+107.7\times\text{LivingArea}+1.03\times\text{LotArea}+51\,710\times\text{CentralAir}$，残差标准误为 $52\,420$。记 $\boldsymbol{\beta}=(\beta_0,\beta_1,\dots,\beta_p)^{\mathsf T}$，$\boldsymbol{x}_i=(1,x_{i1},\dots,x_{ip})^{\mathsf T}$，模型为 $y_i=\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}+\varepsilon_i$，写成矩阵形式即

$$
\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon},
$$

其中 $\boldsymbol{Y}=(y_1,\dots,y_n)^{\mathsf T}$，$\boldsymbol{\varepsilon}=(\varepsilon_1,\dots,\varepsilon_n)^{\mathsf T}$，$n\times(p+1)$ 的设计矩阵（design matrix）$X$ 以 $\boldsymbol{x}_i^{\mathsf T}$ 为行。要回答的问题是：如何估计 $\boldsymbol{\beta}$，如何预测，如何对 $\boldsymbol{\beta}$ 作推断，以及如何检验模型。

Gauss–Markov 假定为：

1. 零均值：$\mathbb{E}(\varepsilon_i\mid\boldsymbol{x}_i)=0$，从而 $\mathbb{E}(y_i\mid\boldsymbol{x}_i)=\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}$；
2. 同方差性（homoscedasticity）：对一切 $i$，$\operatorname{Var}(\varepsilon_i)=\sigma^2$；
3. 误差不相关：$i\ne j$ 时 $\operatorname{Cov}(\varepsilon_i,\varepsilon_j)=0$。

最小二乘估计极小化 $\operatorname{RSS}(\boldsymbol{\beta})=\sum_{i=1}^n(y_i-\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta})^2=\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2$。若 $\operatorname{rank}(X)=p+1$，极小值点唯一，由**正规方程** $X^{\mathsf T}X\boldsymbol{\beta}=X^{\mathsf T}\boldsymbol{Y}$（[2.1](/2.1)）给出：

$$
\hat{\boldsymbol{\beta}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y},\qquad\hat\sigma_n^2=\frac1n\operatorname{RSS}(\hat{\boldsymbol{\beta}}),\qquad\hat\sigma^2=\frac1{n-p-1}\operatorname{RSS}(\hat{\boldsymbol{\beta}}).
$$

与简单情形一样，矩条件 $\mathbb{E}(\boldsymbol{x}_i\varepsilon_i)=\boldsymbol{0}$ 给出同一个估计量。在正态误差下，给定 $\boldsymbol{x}_i$ 时 $\boldsymbol{Y}$ 的条件似然为

$$
L(\boldsymbol{\beta},\sigma^2)=\prod_{i=1}^n\frac1{\sqrt{2\pi}\sigma}\exp\left\{-\frac{(y_i-\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta})^2}{2\sigma^2}\right\},
$$

由似然方程得 $\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}=\left(\sum_i\boldsymbol{x}_i\boldsymbol{x}_i^{\mathsf T}\right)^{-1}\sum_i\boldsymbol{x}_iy_i=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$，$\hat\sigma^2_{\mathrm{MLE}}=\frac1n\|\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}\|^2$。

该估计量有以下性质。

1. 无偏性：在零均值假定下，$\mathbb{E}\hat{\boldsymbol{\beta}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}X\boldsymbol{\beta}=\boldsymbol{\beta}$；在同方差、误差不相关时 $\operatorname{Cov}(\hat{\boldsymbol{\beta}})=\sigma^2(X^{\mathsf T}X)^{-1}$。
2. 最优性：由下面的 Gauss–Markov 定理，$\hat{\boldsymbol{\beta}}$ 是最优线性无偏估计（BLUE）。
3. 正态性：在正态误差下，$\hat{\boldsymbol{\beta}}\sim\mathcal{N}_{p+1}(\boldsymbol{\beta},\sigma^2(X^{\mathsf T}X)^{-1})$，服从**多元正态分布**，且 $(n-p-1)\hat\sigma^2/\sigma^2\sim\chi^2_{n-p-1}$。
4. 独立性：在正态误差下，$\hat{\boldsymbol{\beta}}$ 与 $\hat\sigma^2$（等价地，与 $\hat\sigma_n^2$）独立。

**定理 3.5.1（Gauss–Markov 定理）** 在 Gauss–Markov 假定下且 $\operatorname{rank}(X)=p+1$，对 $\boldsymbol{\beta}$ 的每个线性无偏估计 $\tilde{\boldsymbol{\beta}}=C\boldsymbol{Y}$（$C$ 为 $(p+1)\times n$ 常数矩阵，且对一切 $\boldsymbol{\beta}$ 有 $\mathbb{E}\tilde{\boldsymbol{\beta}}=\boldsymbol{\beta}$），$\operatorname{Cov}(\tilde{\boldsymbol{\beta}})-\operatorname{Cov}(\hat{\boldsymbol{\beta}})$ 半正定。

**证明** 对一切 $\boldsymbol{\beta}$ 无偏意味着 $CX=I_{p+1}$。记 $C=(X^{\mathsf T}X)^{-1}X^{\mathsf T}+D$，则 $DX=O$。于是 $\operatorname{Cov}(\tilde{\boldsymbol{\beta}})=\sigma^2CC^{\mathsf T}=\sigma^2(X^{\mathsf T}X)^{-1}+\sigma^2DD^{\mathsf T}$，交叉项因 $DX=O$ 而为零，且 $\sigma^2DD^{\mathsf T}$ 半正定。$\square$

与 Cramér–Rao 下界不同，这一最优性不需要分布假定，但只限于关于 $\boldsymbol{Y}$ 线性的估计量。在正态误差下，$\hat{\boldsymbol{\beta}}$ 甚至是一致最小方差无偏估计，因为此时模型是指数族，$(X^{\mathsf T}\boldsymbol{Y},\boldsymbol{Y}^{\mathsf T}\boldsymbol{Y})$ 是其充分完备统计量。

## 3.6. 核密度估计

### 3.6.1. 从直方图到核估计

前面的估计量针对有限个参数。核密度估计则在不假定参数族的情况下，由样本估计整个未知密度 $f$。熟悉的估计是直方图，但它依赖于分组的选择（组数太多则过拟合，太少则过度光滑），而且密度通常连续，直方图却不连续，整体误差也可能较大。核估计用放在每个观测处的光滑"小山包"代替分组。

对连续分布，密度是分布函数的导数，

$$
f(x)=F'(x)=\lim_{h\to0}\frac{F(x+h)-F(x-h)}{2h}.
$$

用**经验分布函数** $F_n$ 代替 $F$，用小的 $h_n>0$ 代替 $h$，得到自然的估计

$$
f_n(x)=\frac{F_n(x+h_n)-F_n(x-h_n)}{2h_n}=\frac1{nh_n}\sum_{i=1}^nK_0\left(\frac{x-X_i}{h_n}\right),\qquad K_0(u)=\frac12\boldsymbol{1}_{[-1,1)}(u),
$$

这是因为 $F_n(x+h_n)-F_n(x-h_n)$ 是落在 $(x-h_n,x+h_n]$ 中的观测所占的比例。把矩形 $K_0$ 换成光滑函数 $K$，就得到光滑的估计。

**定义 3.6.1（核密度估计）** 设 $X_1,\dots,X_n$ 是来自密度为 $f$ 的分布的随机样本。称

$$
f_n(x)=\frac1{nh_n}\sum_{i=1}^nK\left(\frac{x-X_i}{h_n}\right)
$$
为 $f$ 的**核密度估计量**，函数 $K$ 为**核函数**，常数 $h_n>0$（$n\to\infty$ 时 $h_n\to0$）为**带宽**。以这种方式估计密度称为**核密度估计**。

通常 $K$ 本身是密度，这时 $f_n$ 也是密度：它是以各观测为中心、缩放到宽度 $h_n$ 的 $n$ 个 $K$ 的平均。对 $K$ 的典型要求是：

1. $K(x)\ge0$，$\sup_xK(x)\le M<\infty$，且 $\lim_{|x|\to\infty}|x|K(x)=0$；
2. $K(-x)=K(x)$，$\int_{-\infty}^\infty K(x)\,\mathrm{d}x=1$，且 $\int_{-\infty}^\infty x^2K(x)\,\mathrm{d}x<\infty$；
3. （某些结论需要）$K$ 的 Fourier 变换，即密度 $K$ 的**特征函数**，绝对可积。

| 核 | $K(u)$ |
|---|---|
| 均匀核 | $\frac12\boldsymbol{1}\{\lvert u\rvert\le1\}$ |
| 三角核 | $(1-\lvert u\rvert)\boldsymbol{1}\{\lvert u\rvert\le1\}$ |
| Epanechnikov 核 | $\frac34(1-u^2)\boldsymbol{1}\{\lvert u\rvert\le1\}$ |
| 四次核（双权核） | $\frac{15}{16}(1-u^2)^2\boldsymbol{1}\{\lvert u\rvert\le1\}$ |
| 三权核 | $\frac{35}{32}(1-u^2)^3\boldsymbol{1}\{\lvert u\rvert\le1\}$ |
| Gauss 核 | $\frac1{\sqrt{2\pi}}\mathrm{e}^{-u^2/2}$ |
| 余弦核 | $\frac\pi4\cos\left(\frac{\pi u}2\right)\boldsymbol{1}\{\lvert u\rvert\le1\}$ |

Epanechnikov 核在渐近积分均方误差意义下最优，但改用其他常用核造成的效率损失很小；Gauss 核因数学性质方便而常被使用。带宽的选择比核的选择重要得多。

### 3.6.2. 带宽选择

带宽控制着偏差–方差权衡。$h$ 小时估计紧跟数据，噪声大，偏差小而方差大；$h$ 大时过度光滑，方差小而偏差大，众数等特征会丢失。每一点处 $\operatorname{MSE}=\operatorname{Bias}^2+\operatorname{Var}$，全局的准则是积分均方误差

$$
\operatorname{MISE}(h)=\mathbb{E}\int[f_n(x)-f(x)]^2\,\mathrm{d}x.
$$

对二阶可微的 $f$ 与满足条件 1–2 的核，Taylor 展开给出 $\mathbb{E}f_n(x)-f(x)\approx\frac{h^2}2m_2(K)f''(x)$ 与 $\operatorname{Var}(f_n(x))\approx\frac{f(x)R(K)}{nh}$，其中 $R(g)=\int g(x)^2\,\mathrm{d}x$，$m_2(K)=\int x^2K(x)\,\mathrm{d}x$。积分得 $\operatorname{MISE}(h)=\operatorname{AMISE}(h)+o\left(\frac1{nh}+h^4\right)$，其中渐近积分均方误差

$$
\operatorname{AMISE}(h)=\frac{R(K)}{nh}+\frac14m_2(K)^2h^4R(f''),
$$

其最小值点为

$$
h_{\mathrm{AMISE}}=\left[\frac{R(K)}{m_2(K)^2R(f'')\,n}\right]^{1/5}.
$$

最优带宽为 $n^{-1/5}$ 阶，最优积分均方误差为 $n^{-4/5}$ 阶，慢于参数估计的 $n^{-1}$。这个公式不能直接使用，因为 $R(f'')$ 含有未知的密度。实用的选择方法或者代入 $R(f'')$ 的估计（插入法；把 $f$ 换成正态密度得到经验法则 $h=0.9\min(\hat\sigma,\widehat{\mathrm{IQR}}/1.34)\,n^{-1/5}$，即 R 中 `density` 的默认选项 `bw.nrd0`），或者极小化积分均方误差的无偏估计（交叉验证）。自适应（可变）带宽，例如 balloon 估计与样本点估计，让 $h$ 随 $x$ 或随观测而变化。

![对 N(0, 1) 的 100 个观测（以短竖线标出）用 Gauss 核作核密度估计，三种带宽：h = 0.05 光滑不足，h = 0.35（正态参照法则）接近真实密度（虚线），h = 2 过度光滑。](./plots/kde-bandwidth.py)

在 R 中，`density(x, bw = "nrd0", adjust = 1, kernel = "gaussian")` 计算核估计；`bw` 选择带宽规则（如 `"nrd0"` 或插入法 `"SJ"`），`kernel` 选择核（如 `"epanechnikov"` 或 `"rectangular"`），实际使用的带宽为 `adjust * bw`。

### 3.6.3. 渐近性质

若 $f$ 在 $x$ 处连续，$K$ 满足条件 1–2，$h_n\to0$ 且 $nh_n\to\infty$，则核估计：

1. 渐近无偏：$\lim_{n\to\infty}\mathbb{E}f_n(x)=f(x)$；
2. 均方相合：$\lim_{n\to\infty}\mathbb{E}[f_n(x)-f(x)]^2=0$，从而弱相合，$f_n(x)\xrightarrow{p}f(x)$；
3. 在更强的条件 $nh_n/\log n\to\infty$ 下强相合，$f_n(x)\xrightarrow{\text{a.s.}}f(x)$；
4. 渐近正态：若 $f(x)>0$，则

   $$
   \frac{f_n(x)-\mathbb{E}f_n(x)}{\sqrt{\operatorname{Var}(f_n(x))}}\xrightarrow{d}\mathcal{N}(0,1).
   $$

## 3.7. 高维数据与稀疏估计（选读）

### 3.7.1. 高维问题

二十年来，高维统计与稀疏建模一直是统计学最活跃的领域之一。在高维数据中，变量个数 $p$ 与样本量 $n$ 相当，甚至远大于 $n$。在基因组学中，一项研究可能只有几百名病人，却有数万个基因的表达水平，要解决的问题是对病人分类、找出驱动基因并估计其效应。在视觉皮层的功能磁共振成像研究中，单个体素的响应用图像的 $10\,921$ 个小波（Gabor）特征来建模，训练图像只有 $n=1750$ 幅。关键的结构假定是稀疏性：只有少数自变量起作用，大多数系数 $\beta_j$ 为零。稀疏性在基因组学和成像中较为合理，但在经济、金融等领域可能不成立，那里许多微小的效应都可能起作用。

考虑线性模型 $\boldsymbol{Y}=X\boldsymbol{\beta}^*+\boldsymbol{\varepsilon}$，其中 $X\in\mathbb{R}^{n\times p}$ 是确定的，$p\gg n$，噪声独立同分布，$\boldsymbol{\beta}^*$ 稀疏，至多有 $s<p$ 个非零分量，支撑为 $\mathcal{S}=\{j\colon\beta_j^*\ne0\}$。这时最小二乘是不适定的：$p>n$ 时 $X^{\mathsf T}X$ 奇异，有无穷多个 $\boldsymbol{\beta}$ 能完全拟合数据。最优子集选择

$$
\min_{\boldsymbol{\beta}}\|\boldsymbol{Y}-X\boldsymbol{\beta}\|_2^2\quad\text{满足}\quad\|\boldsymbol{\beta}\|_0\le k,
$$

（$\|\boldsymbol{\beta}\|_0$ 为非零分量的个数）直接施加稀疏性，但它是组合优化问题（NP 难）。

### 3.7.2. Lasso

把 $\ell_0$ 约束换成 $\ell_1$ 范数 $\|\boldsymbol{\beta}\|_1=\sum_j|\beta_j|$，就得到基追踪（S. Chen 与 D. Donoho，1994）、非负 garrote（L. Breiman，1995），以及 R. Tibshirani（1996）提出的 Lasso（least absolute shrinkage and selection operator）：

$$
\hat{\boldsymbol{\beta}}=\arg\min_{\boldsymbol{\beta}}\left\{\|\boldsymbol{Y}-X\boldsymbol{\beta}\|_2^2+\lambda\|\boldsymbol{\beta}\|_1\right\},\qquad\lambda\ge0.
$$

$\ell_1$ 惩罚有两个关键性质。$\ell_1$ 球的顶点位于坐标轴上，因此 $\hat{\boldsymbol{\beta}}$ 的许多分量恰好为零，Lasso 同时完成了变量选择；而且问题是凸的，是 $\ell_0$ 问题的凸松弛，即使 $p$ 很大也能高效求解。调节参数 $\lambda$ 在拟合与稀疏之间权衡，通常用交叉验证选取。

在 $X$ 满足一定条件（如限制特征值条件或不可表示条件）且 $\lambda$ 取 $\sigma\sqrt{n\log p}$ 阶时，Lasso 理论研究三类保证：

- 估计误差 $\|\hat{\boldsymbol{\beta}}-\boldsymbol{\beta}^*\|_2^2$，其阶为 $s\log p/n$（P. Bickel、Y. Ritov 与 A. Tsybakov，2009；S. Negahban 等，2009）；
- 预测误差 $\|X\hat{\boldsymbol{\beta}}-X\boldsymbol{\beta}^*\|_2^2$（F. Bunea 等，2006）；
- 模型选择相合性：估计的支撑 $\hat{\mathcal{S}}=\{j\colon\hat\beta_j\ne0\}$ 满足 $\mathbb{P}(\hat{\mathcal{S}}=\mathcal{S})\to1$（P. Zhao 与 B. Yu，2006）。

目前的前沿是变量选择之后的不确定性量化，即在高维情形下给出有效的置信区间与 $p$ 值，方法包括样本分割、bootstrap、去偏（去稀疏化）Lasso、选择后推断与 knockoff。

## 小结

| 方法 | 优点 | 缺点 | 典型用途 |
|---|---|---|---|
| 矩估计法 | 简单；只需矩，不需要模型 | 可能不唯一、效率低或超出参数空间 | 初步估计、复杂模型、迭代初值 |
| 极大似然估计 | 具有不变性；相合、渐近正态且渐近有效 | 需要模型；可能没有闭式解；对模型误差敏感 | 参数模型、大样本 |
| 一致最小方差无偏估计 | 对每个 $n$ 都在无偏估计中最优 | 不一定存在；构造需要充分完备统计量 | 指数族中的精确小样本推断 |
| 核密度估计 | 不需要参数假定；灵活 | 收敛速度慢（$n^{-4/5}$）；对带宽敏感 | 探索性分析、非参数密度估计 |

- 固定 $n$ 时用偏差、方差与均方误差比较估计量，$n$ 很大时用相合性与渐近方差比较。均方误差 $=$ 方差 $+$ 偏差$^2$，少量偏差可以换来方差的大幅下降。
- 极大似然估计使似然最大；它是任一充分统计量的函数，在重新参数化下不变，在正则条件下渐近服从 $\mathcal{N}(\theta,1/(nI(\theta)))$。
- Rao–Blackwell 定理通过对充分统计量取条件期望改进无偏估计；Lehmann–Scheffé 定理表明，充分完备统计量的无偏函数是唯一的一致最小方差无偏估计。
- Cramér–Rao 不等式给出无偏估计方差的下界 $[g'(\theta)]^2/(nI(\theta))$；下界只在指数族中才能达到，并据此定义估计量的效率。
- 在正态误差的线性回归中，最小二乘、矩估计与极大似然给出相同的系数估计，在 Gauss–Markov 假定下它是最优线性无偏估计。
