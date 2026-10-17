---
title: 区间估计与置信区间
description: 置信区间、置信限与置信域；可靠度与精度的权衡；正态、均匀、指数总体以及两正态总体的枢轴量法；大样本近似置信区间、Behrens–Fisher 问题与 Welch 区间；Bonferroni 与 Šidák 校正构造的联合置信域。
source_hash: 49841f0689d7
---

点估计只是一个数，不反映自身的不确定性：观测到的样本只是众多可能样本之一，估计值也只是众多可能值之一。区间估计则给出一个取值范围，并以重复抽样下的概率保证这个范围包含参数。本章定义置信区间、置信限与置信域，以及可靠度与精度这两个相互冲突的要求（§4.1）；对正态、均匀、指数总体以及两个正态总体的比较，发展主要的构造方法——枢轴量法（§4.2）；转而讨论基于**中心极限定理**的大样本区间，包括 Behrens–Fisher 问题（§4.3）；最后讨论多个参数的联合置信域（§4.4）。枢轴量由 [3.2.3](/3.2.3) 中好的点估计量构造，通常是**充分统计量**的函数，其分布则是 [3.2.2](/3.2.2) 中的正态、$\chi^2$、$t$ 与 $F$ **抽样分布**。置信区间与假设检验是同一枚硬币的两面，二者的对偶关系见 [3.2.5](/3.2.5)；Bayes 方法中与之对应的可信区间见 [3.2.7](/3.2.7)。

## 4.1. 基本概念

### 4.1.1. 区间估计与置信区间

设 $\boldsymbol{X}=(X_1,\dots,X_n)$ 是来自 $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$ 的随机样本，要估计一维参数 $g(\theta)$。点估计 $\hat g(\boldsymbol{X})$ 不能直接反映自身的精度（或者说不确定性、风险），而均方误差也不是对单个估计值的直接评价。$g(\theta)$ 的区间估计由两个统计量 $\hat g_1(\boldsymbol{X})\le\hat g_2(\boldsymbol{X})$ 给出随机区间 $[\hat g_1(\boldsymbol{X}),\hat g_2(\boldsymbol{X})]$，并给出 $g(\theta)\in[\hat g_1(\boldsymbol{X}),\hat g_2(\boldsymbol{X})]$ 的概率。任何这样的一对统计量都给出一个区间估计；问题在于如何评价并构造好的区间估计。

**例 4.1.1** 对 18 岁香港儿童的身高，考虑容量 $n=100$ 的样本以及平均身高 $\mu$ 的区间 $[\bar X-1.96S/\sqrt n,\ \bar X+1.96S/\sqrt n]$。这个区间是随机的，随样本而移动。从均值为 $68$ 英寸的总体中重复抽样 $1000$ 次，有 $94.7\%$ 的区间覆盖了真实均值。较窄的区间 $[\bar X-0.5S/\sqrt n,\ \bar X+0.5S/\sqrt n]$ 只有 $38.2\%$ 的时候覆盖了真值。评价一个区间必须同时看它的覆盖率与长度。

评价区间估计有两个准则：

- 可靠度，即它覆盖参数的概率 $\mathbb{P}_\theta(g(\theta)\in[\hat g_1(\boldsymbol{X}),\hat g_2(\boldsymbol{X})])$；
- 精度，用平均长度 $\mathbb{E}_\theta[\hat g_2(\boldsymbol{X})-\hat g_1(\boldsymbol{X})]$ 衡量，它通常依赖于样本量。

样本量固定时二者不可兼得：区间越长越可靠，但越不精确。J. Neyman 的原则是先固定可靠度，再在达到这一可靠度的区间中寻找精度最高的。

本节以下设 $g(\theta)=\theta$，$\theta\in\Theta\subseteq\mathbb{R}$；一般情形只是记号上的改变。

**定义 4.1.1（置信区间）** 设 $\hat\theta_1(\boldsymbol{X})\le\hat\theta_2(\boldsymbol{X})$ 是统计量，于是 $[\hat\theta_1(\boldsymbol{X}),\hat\theta_2(\boldsymbol{X})]$ 是一个**随机区间**（端点为随机变量的区间）。给定 $0<\alpha<1$，若

$$
\mathbb{P}_\theta\left(\hat\theta_1(\boldsymbol{X})\le\theta\le\hat\theta_2(\boldsymbol{X})\right)\ge1-\alpha\qquad\text{对一切 }\theta\in\Theta,
$$
则称 $[\hat\theta_1(\boldsymbol{X}),\hat\theta_2(\boldsymbol{X})]$ 为 $\theta$ 的**置信水平**为 $1-\alpha$ 的**置信区间**。下确界

$$
\inf_{\theta\in\Theta}\mathbb{P}_\theta\left(\hat\theta_1(\boldsymbol{X})\le\theta\le\hat\theta_2(\boldsymbol{X})\right)
$$
称为该区间的**置信系数**，$\mathbb{E}_\theta(\hat\theta_2-\hat\theta_1)$ 称为它的精度（也可以用其他精度度量）。

$\mathbb{P}_\theta(\hat\theta_1\le\theta\le\hat\theta_2)$ 是 $\theta$ 处的覆盖概率。置信水平为 $1-\alpha$ 的置信区间处处覆盖概率不低于 $1-\alpha$，其置信系数是满足这一点的最大水平。Neyman 原则要求在置信系数不低于 $1-\alpha$ 的区间中寻找精度最高的；覆盖概率与 $\theta$ 无关时，置信水平与置信系数相同。

**例 4.1.2** 设 $X_1,\dots,X_n$ 是来自 $\mathcal{N}(\mu,\sigma^2)$（$\mu\in\mathbb{R}$，$\sigma^2>0$）的随机样本，**样本均值**为 $\bar X$，**样本方差**为 $S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2$，考虑 $\mu$ 的区间估计 $[\bar X-kS/\sqrt n,\ \bar X+kS/\sqrt n]$。记 $\theta=(\mu,\sigma^2)$，覆盖概率为

$$
\mathbb{P}_\theta\left(\bar X-\frac{kS}{\sqrt n}\le\mu\le\bar X+\frac{kS}{\sqrt n}\right)=\mathbb{P}_\theta\left(\left\lvert\frac{\sqrt n(\bar X-\mu)}S\right\rvert\le k\right)=\mathbb{P}(|T|\le k),\qquad T\sim t_{n-1},
$$

这是因为 $T=\sqrt n(\bar X-\mu)/S\sim t_{n-1}$（推论 2.1.4）。它与 $\theta$ 无关，因而就是置信系数，且随 $k$ 增大而增大。由 $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$，平均长度为

$$
l_k=\frac{2k\,\mathbb{E}S}{\sqrt n}=\frac{2\sqrt2\,k\sigma\,\Gamma(n/2)}{\sqrt{n(n-1)}\,\Gamma((n-1)/2)},
$$

也随 $k$ 增大而增大。给定 $n$，提高可靠度需要增大 $k$，提高精度需要减小 $k$：这就是可靠度与精度之间的权衡。

### 4.1.2. 置信区间的解释

取 $\alpha=0.05$，设抽样后得到 $\mu$ 的 $95\%$ 置信区间 $[0.5,1.5]$。能否说 $0.5\le\mu\le1.5$ 的概率不小于 $0.95$？不能。抽样之前，$[\hat\theta_1(\boldsymbol{X}),\hat\theta_2(\boldsymbol{X})]$ 是随机区间；抽样之后，$[\hat\theta_1(\boldsymbol{x}),\hat\theta_2(\boldsymbol{x})]$ 是观测到的区间，不再随机，固定的参数要么在其中，要么不在。概率指的是这一程序，按概率的频率解释理解：若试验重复 $N$ 次，得到样本 $\boldsymbol{x}^{(1)},\dots,\boldsymbol{x}^{(N)}$ 与区间 $[\hat\theta_1(\boldsymbol{x}^{(j)}),\hat\theta_2(\boldsymbol{x}^{(j)})]$，则从长期看，这些区间中至少约有 $0.95N$ 个包含 $\theta$。

![对 N(68, 3.6) 的均值，n = 100 时模拟的 100 个区间 [x_bar - k s / sqrt(n), x_bar + k s / sqrt(n)]。左：k = 1.96，几乎所有区间（灰色）都覆盖真实均值（竖线），未覆盖的以彩色标出。右：k = 0.5，区间更短，但大多数没有覆盖真值。](./plots/ci-coverage.py)

### 4.1.3. 置信限

常常只有一侧是重要的：新材料的强度应不低于某个值，次品率应不超过 $1\%$。

**定义 4.1.2（置信限）** 设 $\hat\theta_U(\boldsymbol{X})$ 与 $\hat\theta_L(\boldsymbol{X})$ 是统计量，$0<\alpha<1$。若

$$
\mathbb{P}_\theta\left(\theta\le\hat\theta_U(\boldsymbol{X})\right)\ge1-\alpha\quad\text{对一切 }\theta\in\Theta,\qquad\text{或}\qquad\mathbb{P}_\theta\left(\hat\theta_L(\boldsymbol{X})\le\theta\right)\ge1-\alpha\quad\text{对一切 }\theta\in\Theta,
$$
则分别称 $\hat\theta_U$ 为 $\theta$ 的置信水平为 $1-\alpha$ 的**置信上限**，$\hat\theta_L$ 为 $\theta$ 的置信水平为 $1-\alpha$ 的**置信下限**。

在给定水平下，置信上限的 $\mathbb{E}_\theta\hat\theta_U$ 越小越精确，置信下限的 $\mathbb{E}_\theta\hat\theta_L$ 越大越精确。两个单侧置信限可以合成一个区间。

**引理 4.1.1** 设 $\hat\theta_L(\boldsymbol{X})$ 是 $\theta$ 的置信水平为 $1-\alpha_1$ 的置信下限，$\hat\theta_U(\boldsymbol{X})$ 是置信水平为 $1-\alpha_2$ 的置信上限，且 $\hat\theta_L(\boldsymbol{X})\le\hat\theta_U(\boldsymbol{X})$。则 $[\hat\theta_L(\boldsymbol{X}),\hat\theta_U(\boldsymbol{X})]$ 是 $\theta$ 的置信水平为 $1-(\alpha_1+\alpha_2)$ 的置信区间。

**证明** 区间不覆盖 $\theta$ 当且仅当 $\theta<\hat\theta_L$ 或 $\theta>\hat\theta_U$。因此

$$
\mathbb{P}_\theta(\hat\theta_L\le\theta\le\hat\theta_U)=1-\mathbb{P}_\theta(\theta<\hat\theta_L)-\mathbb{P}_\theta(\theta>\hat\theta_U)\ge1-\alpha_1-\alpha_2,
$$

由于 $\hat\theta_L\le\hat\theta_U$，这两个事件互不相交。$\square$

### 4.1.4. 置信域

对 $k\ge2$ 维参数，例如一群儿童的平均身高与平均体重，区间换成区域。

**定义 4.1.3（置信域）** 设 $\mathcal{F}=\{f(x;\boldsymbol{\theta})\colon\boldsymbol{\theta}\in\Theta\}$，$\boldsymbol{\theta}=(\theta_1,\dots,\theta_k)\in\Theta\subseteq\mathbb{R}^k$，$k\ge2$，$\boldsymbol{X}$ 是来自 $f(x;\boldsymbol{\theta})$ 的随机样本，$S(\boldsymbol{X})$ 是统计量。若以下两条成立，则称 $S(\boldsymbol{X})$ 为 $\boldsymbol{\theta}$ 的置信水平为 $1-\alpha$ 的**置信域**，$\inf_{\boldsymbol{\theta}\in\Theta}\mathbb{P}_{\boldsymbol{\theta}}(\boldsymbol{\theta}\in S(\boldsymbol{X}))$ 称为它的置信系数：

1. 对每个 $\boldsymbol{X}$，$S(\boldsymbol{X})$ 是 $\Theta$ 的子集；
2. 对给定的 $0<\alpha<1$，$\mathbb{P}_{\boldsymbol{\theta}}(\boldsymbol{\theta}\in S(\boldsymbol{X}))\ge1-\alpha$ 对一切 $\boldsymbol{\theta}\in\Theta$ 成立。

置信域可以是椭圆、圆盘或任何其他集合。矩形 $[\hat\theta_{1L},\hat\theta_{1U}]\times[\hat\theta_{2L},\hat\theta_{2U}]$ 称为联合置信区间，或同时置信区间；它最便于报告，§4.4 就构造这样的矩形。

## 4.2. 枢轴量法

### 4.2.1. 方法

**例 4.2.1** 设 $X_1,\dots,X_n$ 是来自 $\mathcal{N}(\mu,\sigma^2)$ 的随机样本，$\mu$ 未知，$\sigma^2$ 已知。要构造 $\mu$ 的置信系数为 $1-\alpha$ 的置信区间，例如 18 岁香港儿童平均身高的 $95\%$ 区间。$\mu$ 的自然点估计是 $\bar X$，其分布为 $\mathcal{N}(\mu,\sigma^2/n)$。它的标准化

$$
Z=\frac{\sqrt n(\bar X-\mu)}\sigma\sim\mathcal{N}(0,1)
$$

的分布与 $\mu$ 无关。记 $z_{\alpha/2}$ 为 $\mathcal{N}(0,1)$ 的上 $\alpha/2$ 分位数，则

$$
\mathbb{P}_\mu\left(\left\lvert\frac{\sqrt n(\bar X-\mu)}\sigma\right\rvert\le z_{\alpha/2}\right)=1-\alpha,\qquad\text{即}\qquad\mathbb{P}_\mu\left(\bar X-\frac\sigma{\sqrt n}z_{\alpha/2}\le\mu\le\bar X+\frac\sigma{\sqrt n}z_{\alpha/2}\right)=1-\alpha.
$$

因此 $\left[\bar X-\frac{\sigma}{\sqrt n}z_{\alpha/2},\ \bar X+\frac{\sigma}{\sqrt n}z_{\alpha/2}\right]$ 是 $\mu$ 的置信水平（也是置信系数）为 $1-\alpha$ 的置信区间。它的长度 $l_n=2\sigma z_{\alpha/2}/\sqrt n$ 不是随机的，并且：

1. 样本量越大，$l_n$ 越短，精度越高；
2. $\sigma$ 越大，$l_n$ 越长；
3. $\alpha$ 越小，即置信水平 $1-\alpha$ 越大，$z_{\alpha/2}$ 越大，精度越低。

给定 $\sigma$ 与 $\alpha$，只有增大样本量才能提高精度。例如在 $\sigma=1$、$\alpha=0.05$ 时要保证长度 $l_n\le0.5$，需要 $2\sigma z_{\alpha/2}/\sqrt n\le0.5$，即 $n\ge(2\cdot1.96/0.5)^2=61.5$，故取 $n=62$。

为什么取对称区间？任何满足 $\mathbb{P}(a\le Z\le b)=1-\alpha$ 的 $a<b$ 都给出长度为 $(b-a)\sigma/\sqrt n$ 的区间；由于 $\mathcal{N}(0,1)$ 的密度对称且单峰，$b-a$ 在 $b=-a=z_{\alpha/2}$ 时最小。同样的原则——把区间放在枢轴量密度最高的地方——对其他单峰枢轴量给出最短区间；枢轴量分布偏斜时，等尾区间是方便的近似。

例 4.2.1 的方法由四步组成。

1. 找一个含有参数 $\theta$ 与样本 $X_1,\dots,X_n$ 的随机变量，最好通过充分统计量，其分布精确地或至少近似地已知。
2. 确定常数 $a<b$，使这个随机变量落在 $[a,b]$ 中的 $\mathbb{P}_\theta$ 概率不小于 $1-\alpha$。
3. 把第 2 步中的不等式改写成端点为统计量、包含 $\theta$ 的区间。
4. 第 3 步的区间就是所求的置信区间。

**定义 4.2.1（枢轴量）** 依赖于样本与参数 $\theta$、而分布与 $\theta$ 无关的随机变量 $G(\boldsymbol{X};\theta)$ 称为 $\theta$ 的**枢轴量**。按第 1–4 步构造置信区间的方法称为**枢轴量法**。

怎样寻找枢轴量？这取决于具体问题，但通常的途径是：取 $\theta$ 的一个好的估计量 $\hat\theta$，它往往是充分统计量的函数；求出它的分布（精确分布或极限分布），这个分布依赖于 $\theta$；再对 $\hat\theta$ 作变换，使变换后的随机变量的分布不再依赖于参数。

枢轴量不唯一。在例 4.2.1 中，即使 $\sigma^2$ 已知，$T=\frac{\sqrt n(\bar X-\mu)}S\sim t_{n-1}$ 也是枢轴量，由它得到区间 $\left[\bar X-\frac{S}{\sqrt n}t_{n-1,\alpha/2},\ \bar X+\frac{S}{\sqrt n}t_{n-1,\alpha/2}\right]$。哪一个更好？从 $\mathcal{N}(1,2)$ 中取 $n=100$ 作模拟，此时 $z_{0.025}=1.96$，$t_{99,0.025}=1.98$，两个 $95\%$ 区间为 $[\bar X\pm0.277]$ 与 $[\bar X\pm0.198S]$；重复 $1000$ 次，它们的经验覆盖率（覆盖 $\mu$ 的区间所占比例）为 $0.952$ 与 $0.948$，都接近 $0.95$。对 $n$ 从 $20$ 到 $500$ 重复，两者的覆盖率都在 $0.95$ 附近波动，但 $t$ 区间的平均长度略长，$n$ 小时尤其如此。$\sigma$ 已知时，$z$ 区间利用了这一信息，更为可取。

同一枢轴量也给出单侧置信限：在置信水平 $1-\alpha$ 下，$\bar X+\sigma z_\alpha/\sqrt n$ 是 $\mu$ 的置信上限，$\bar X-\sigma z_\alpha/\sqrt n$ 是 $\mu$ 的置信下限。

### 4.2.2. 单个正态总体

**例 4.2.2** 设 $X_1,\dots,X_n$ 是来自 $\mathcal{N}(\mu,\sigma^2)$ 的随机样本，$\mu$ 已知，$\sigma^2$ 未知。令 $S_\mu^2=\frac1n\sum_{i=1}^n(X_i-\mu)^2$，则

$$
\frac{nS_\mu^2}{\sigma^2}=\sum_{i=1}^n\left(\frac{X_i-\mu}\sigma\right)^2\sim\chi^2_n
$$

是枢轴量。对任何满足 $\mathbb{P}(a\le\chi^2_n\le b)=1-\alpha$ 的 $0<a<b$，

$$
\mathbb{P}_{\sigma^2}\left(a\le\frac{nS_\mu^2}{\sigma^2}\le b\right)=\mathbb{P}_{\sigma^2}\left(\frac{nS_\mu^2}b\le\sigma^2\le\frac{nS_\mu^2}a\right)=1-\alpha\qquad\text{对一切 }\sigma^2.
$$

取等尾 $a=\chi^2_{n,1-\alpha/2}$、$b=\chi^2_{n,\alpha/2}$（简单，但不是最短的），得到区间

$$
\left[\frac{nS_\mu^2}{\chi^2_{n,\alpha/2}},\ \frac{nS_\mu^2}{\chi^2_{n,1-\alpha/2}}\right].
$$

这里为什么不用 $S^2$？$\mu$ 已知时 $S_\mu^2$ 是充分统计量，并且是 $\sigma^2$ 的一致最小方差无偏估计（例 3.4.9）；$(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$ 也是枢轴量，但浪费了一个自由度，平均而言区间更长。

**例 4.2.3** 设 $X_1,\dots,X_n$ 是来自 $\mathcal{N}(\mu,\sigma^2)$ 的随机样本，两个参数都未知，$\boldsymbol{\theta}=(\mu,\sigma^2)$。我们有

$$
\frac{\sqrt n(\bar X-\mu)}\sigma\sim\mathcal{N}(0,1),\qquad\frac{(n-1)S^2}{\sigma^2}=\sum_{i=1}^n\left(\frac{X_i-\bar X}\sigma\right)^2\sim\chi^2_{n-1},
$$

且二者独立（定理 2.1.3），故

$$
\frac{\sqrt n(\bar X-\mu)/\sigma}{\sqrt{(n-1)S^2/[\sigma^2(n-1)]}}=\frac{\sqrt n(\bar X-\mu)}S\sim t_{n-1},
$$

这是 $\mu$ 的一个不含多余参数 $\sigma^2$ 的枢轴量。对满足 $\mathbb{P}(a\le t_{n-1}\le b)=1-\alpha$ 的 $a<b$，$\mathbb{P}_{\boldsymbol{\theta}}\left(\bar X-b\frac S{\sqrt n}\le\mu\le\bar X-a\frac S{\sqrt n}\right)=1-\alpha$ 对一切 $\boldsymbol{\theta}$ 成立；对称的选择 $b=-a=t_{n-1,\alpha/2}$ 给出最短区间

$$
\left[\bar X-t_{n-1,\alpha/2}\frac S{\sqrt n},\ \bar X+t_{n-1,\alpha/2}\frac S{\sqrt n}\right]=\bar X\pm t_{n-1,\alpha/2}\frac S{\sqrt n}.
$$

对 $\sigma^2$，用枢轴量 $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$ 重复例 4.2.2，得

$$
\left[\frac{(n-1)S^2}{\chi^2_{n-1,\alpha/2}},\ \frac{(n-1)S^2}{\chi^2_{n-1,1-\alpha/2}}\right].
$$

对儿童身高，从 $(\mu,\sigma^2)=(68,3.6)$ 的总体中抽取容量 $n=100$ 的样本，得 $\bar x=67.8$，$s^2=4.13$。由 $t_{99,0.025}=1.984$、$\chi^2_{99,0.025}=128.4$、$\chi^2_{99,0.975}=73.4$，$\mu$ 的 $95\%$ 置信区间为 $[67.4,68.2]$，$\sigma^2$ 的为 $[3.18,5.57]$，都包含真值。

正态总体的四个区间如下：

| 目标 | 条件 | 枢轴量 | 置信水平为 $1-\alpha$ 的置信区间 |
|---|---|---|---|
| $\mu$ | $\sigma^2$ 已知 | $\frac{\sqrt n(\bar X-\mu)}\sigma\sim\mathcal{N}(0,1)$ | $\bar X\pm z_{\alpha/2}\frac\sigma{\sqrt n}$ |
| $\mu$ | $\sigma^2$ 未知 | $\frac{\sqrt n(\bar X-\mu)}S\sim t_{n-1}$ | $\bar X\pm t_{n-1,\alpha/2}\frac S{\sqrt n}$ |
| $\sigma^2$ | $\mu$ 已知 | $\frac{nS_\mu^2}{\sigma^2}\sim\chi^2_n$ | $\left[\frac{nS_\mu^2}{\chi^2_{n,\alpha/2}},\frac{nS_\mu^2}{\chi^2_{n,1-\alpha/2}}\right]$ |
| $\sigma^2$ | $\mu$ 未知 | $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$ | $\left[\frac{(n-1)S^2}{\chi^2_{n-1,\alpha/2}},\frac{(n-1)S^2}{\chi^2_{n-1,1-\alpha/2}}\right]$ |

### 4.2.3. 均匀总体与指数总体

**例 4.2.4** 设 $X_1,\dots,X_n$ 是来自 $\mathrm{U}(0,\theta)$（$\theta>0$）的随机样本。**次序统计量** $X=X_{(n)}$ 是 $\theta$ 的充分统计量，密度为 $f_X(x;\theta)=\frac n{\theta^n}x^{n-1}$，$0\le x\le\theta$。变量 $Y=X_{(n)}/\theta$ 的密度为 $f_Y(y)=ny^{n-1}$，$0\le y\le1$，与 $\theta$ 无关，所以是枢轴量。对任何满足 $\int_a^bny^{n-1}\,\mathrm{d}y=b^n-a^n=1-\alpha$ 的 $0\le a<b\le1$，

$$
\mathbb{P}_\theta(a\le Y\le b)=\mathbb{P}_\theta\left(a\le\frac{X_{(n)}}\theta\le b\right)=\mathbb{P}_\theta\left(\frac{X_{(n)}}b\le\theta\le\frac{X_{(n)}}a\right)=1-\alpha\qquad\text{对一切 }\theta,
$$

$[X_{(n)}/b,\ X_{(n)}/a]$ 是置信水平为 $1-\alpha$ 的置信区间。其长度为 $X_{(n)}\left(\frac1a-\frac1b\right)$，其中 $a=a(b)=(b^n-1+\alpha)^{1/n}$；由于 $a<b$ 时 $\frac{\mathrm{d}}{\mathrm{d}b}\left(\frac1a-\frac1b\right)=\frac{1}{b^2}-\frac{b^{n-1}}{a^{n+1}}<0$，长度在 $b=1$、$a=\alpha^{1/n}$ 时最小。最短区间为

$$
\left[X_{(n)},\ \frac{X_{(n)}}{\alpha^{1/n}}\right].
$$

这里枢轴量的密度递增，所以最短区间把全部 $\alpha$ 放在 $Y$ 的左尾。

**例 4.2.5** 对某品牌的 $5$ 只灯泡做寿命试验，寿命分别为 $2,3,1,3,4$ 年。用矩估计法，以及在指数模型下用极大似然估计（[3.2.3](/3.2.3)），平均寿命都估计为 $\bar x=2.6$ 年。置信区间是什么？

设 $X_1,\dots,X_n$ 是来自密度为 $\lambda\mathrm{e}^{-\lambda x}\boldsymbol{1}_{(0,\infty)}(x)$（$\lambda>0$）的 $\mathrm{Exp}(\lambda)$ 的随机样本。$\bar X$ 是 $1/\lambda$ 的无偏估计（而且是一致最小方差无偏估计），所以以 $\bar X$ 为基础构造区间。由于 $2\lambda X_i\sim\mathrm{Exp}(1/2)=\chi^2_2$ 相互独立，

$$
2\lambda n\bar X=2\lambda\sum_{i=1}^nX_i\sim\chi^2_{2n}
$$

（推论 2.1.7）是枢轴量。由 $\mathbb{P}\left(\chi^2_{2n,1-\alpha/2}\le2\lambda n\bar X\le\chi^2_{2n,\alpha/2}\right)=1-\alpha$，$\lambda$ 的区间为

$$
\left[\frac{\chi^2_{2n,1-\alpha/2}}{2n\bar X},\ \frac{\chi^2_{2n,\alpha/2}}{2n\bar X}\right],
$$

取倒数，$\left[\frac{2n\bar X}{\chi^2_{2n,\alpha/2}},\frac{2n\bar X}{\chi^2_{2n,1-\alpha/2}}\right]$ 是平均寿命 $1/\lambda$ 的区间。对这批灯泡，$n=5$，$\bar x=2.6$，$\chi^2_{10,0.025}=20.48$，$\chi^2_{10,0.975}=3.25$，所以平均寿命的 $95\%$ 置信区间为

$$
\left[\frac{26}{20.48},\ \frac{26}{3.25}\right]=[1.27,\ 8.01]\ \text{年},
$$

由于样本极小，区间很宽。

### 4.2.4. 两个正态总体

比较两个总体是实践中最常见的问题之一：两种小麦的产量，两种温度下某工艺的产量，男性与女性的身高，某种药物的平均处理效应。设 $X_1,\dots,X_m$ 与 $Y_1,\dots,Y_n$ 分别是来自 $\mathcal{N}(\mu_1,\sigma_1^2)$ 与 $\mathcal{N}(\mu_2,\sigma_2^2)$ 的独立随机样本，四个参数都未知，记

$$
S_X^2=\frac1{m-1}\sum_{i=1}^m(X_i-\bar X)^2,\qquad S_Y^2=\frac1{n-1}\sum_{j=1}^n(Y_j-\bar Y)^2.
$$

我们要构造 $\mu_1-\mu_2$ 与 $\sigma_1^2/\sigma_2^2$ 的置信区间。

**例 4.2.6（均值差，方差相等）** 为了找到 $\mu_1-\mu_2$ 的枢轴量，假定两个方差虽然未知但相等，$\sigma_1^2=\sigma_2^2=\sigma^2$。由于 $\bar X-\mu_1\sim\mathcal{N}(0,\sigma^2/m)$ 与 $\bar Y-\mu_2\sim\mathcal{N}(0,\sigma^2/n)$ 独立，

$$
\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{\sigma\sqrt{\frac1m+\frac1n}}\sim\mathcal{N}(0,1).
$$

又 $(m-1)S_X^2/\sigma^2\sim\chi^2_{m-1}$ 与 $(n-1)S_Y^2/\sigma^2\sim\chi^2_{n-1}$ 独立，所以 $[(m-1)S_X^2+(n-1)S_Y^2]/\sigma^2\sim\chi^2_{m+n-2}$，且与两个均值独立。记合并方差 $S_w^2=\frac{(m-1)S_X^2+(n-1)S_Y^2}{m+n-2}$，得

$$
\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{S_w\sqrt{\frac1m+\frac1n}}\sim t_{m+n-2}
$$

（推论 2.1.5），与例 4.2.3 一样，

$$
(\bar X-\bar Y)\pm t_{m+n-2,\alpha/2}\,S_w\sqrt{\frac1m+\frac1n}
$$

是 $\mu_1-\mu_2$ 的置信水平为 $1-\alpha$ 的置信区间。

**例 4.2.7（方差比）** 由于 $(m-1)S_X^2/\sigma_1^2\sim\chi^2_{m-1}$ 与 $(n-1)S_Y^2/\sigma_2^2\sim\chi^2_{n-1}$ 独立，

$$
\frac{S_Y^2/\sigma_2^2}{S_X^2/\sigma_1^2}=\frac{\sigma_1^2}{\sigma_2^2}\cdot\frac{S_Y^2}{S_X^2}\sim F_{n-1,m-1}
$$

（推论 2.1.6 中统计量的倒数）是 $\sigma_1^2/\sigma_2^2$ 的枢轴量，对均值不作任何假定。对满足 $\mathbb{P}(a\le F_{n-1,m-1}\le b)=1-\alpha$ 的 $0<a<b$，$\mathbb{P}_{\boldsymbol{\theta}}\left(a\frac{S_X^2}{S_Y^2}\le\frac{\sigma_1^2}{\sigma_2^2}\le b\frac{S_X^2}{S_Y^2}\right)=1-\alpha$ 对一切 $\boldsymbol{\theta}=(\mu_1,\mu_2,\sigma_1^2,\sigma_2^2)$ 成立，取等尾得区间

$$
\left[\frac{S_X^2}{S_Y^2}F_{n-1,m-1,1-\alpha/2},\ \frac{S_X^2}{S_Y^2}F_{n-1,m-1,\alpha/2}\right].
$$

**例 4.2.8（教授薪水）** 为监测男女教员的薪水差异，收集了美国某学院 2008–09 学年 $397$ 名教员（助理教授、副教授与教授）的九个月薪水，以及职级、学科、获得博士学位以来的年数、任职年数与性别（R 包 `carData` 中的数据集 `Salaries`）。教授与助理教授的薪水有无差异？男性与女性呢？汇总统计量（单位：美元）如下：

| 比较 | $m$ | $n$ | $\bar X$ | $\bar Y$ | $S_X$ | $S_Y$ |
|---|---|---|---|---|---|---|
| 教授（$X$）与助理教授（$Y$） | $266$ | $67$ | $126\,772$ | $80\,776$ | $27\,719$ | $8\,174$ |
| 男性（$X$）与女性（$Y$） | $358$ | $39$ | $115\,090$ | $101\,002$ | $30\,437$ | $25\,922$ |

对教授与助理教授，$t_{331,0.025}=1.967$，$\mu_1-\mu_2$ 的等方差 $95\%$ 区间为 $[39\,255,\ 52\,737]$。但由 $F_{66,265,0.975}=0.666$ 与 $F_{66,265,0.025}=1.436$，$\sigma_1^2/\sigma_2^2$ 的 $95\%$ 区间为 $[7.66,\ 16.51]$，远离 $1$：等方差假定站不住，均值的区间并不合适。对男性与女性，$t_{395,0.025}=1.966$ 给出均值差的区间 $[4\,131,\ 24\,045]$，而方差比的区间 $[0.81,\ 2.12]$（由 $F_{38,357,0.975}=0.591$ 与 $F_{38,357,0.025}=1.541$ 得到）包含 $1$，所以这里等方差区间是可以接受的。方差不等的情形见 §4.3.3。

## 4.3. 近似置信区间

### 4.3.1. 大样本区间

自然的枢轴量的精确分布常常很复杂，或者未知。这时大样本理论，首先是中心极限定理，提供一个与参数无关的极限分布。这样的近似区间在许多数据问题中都要用到，而且往往是非参数的，不假定总体分布的形式。

**定义 4.3.1（渐近有效置信区间）** 若区间序列 $[\hat\theta_1(\boldsymbol{X}_n),\hat\theta_2(\boldsymbol{X}_n)]$（$\boldsymbol{X}_n=(X_1,\dots,X_n)$）满足

$$
\liminf_{n\to\infty}\mathbb{P}_\theta\left(\hat\theta_1(\boldsymbol{X}_n)\le\theta\le\hat\theta_2(\boldsymbol{X}_n)\right)\ge1-\alpha\qquad\text{对一切 }\theta\in\Theta,
$$
则称它为 $\theta$ 的置信水平为 $1-\alpha$ 的**渐近有效置信区间**。

这时对有限样本，置信水平只是近似为 $1-\alpha$，近似的好坏通常依赖于 $\theta$，必须加以检验，例如用模拟。所用的工具是中心极限定理、弱**大数定律**与 Slutsky 定理（定理 2.1.4），并假定 $n$ 大到足以应用它们。

### 4.3.2. Bernoulli、Poisson 与指数总体

**例 4.3.1（Bernoulli 比例）** 某产品的长期废品率为 $\theta$，商店只有在 $\theta<0.01$ 时才购进。随机抽取 $100$ 件产品，其中 $3$ 件是废品，点估计为 $\hat\theta=\bar x=0.03$。置信区间是什么？

设 $X_1,\dots,X_n$ 是来自 $\mathrm{Ber}(\theta)$ 的随机样本。由于 $\mathbb{E}_\theta X_1=\theta$，$\operatorname{Var}_\theta(X_1)=\theta(1-\theta)$，中心极限定理给出

$$
T=\frac{\sqrt n(\bar X_n-\theta)}{\sqrt{\theta(1-\theta)}}\xrightarrow{d}\mathcal{N}(0,1),
$$

其极限分布与 $\theta$ 无关，因而 $T$ 可以作为近似枢轴量，$n$ 大时 $\mathbb{P}_\theta(|T|\le z_{\alpha/2})\approx1-\alpha$。

方法 1：解二次不等式。不等式 $|T|\le z_{\alpha/2}$ 等价于 $n(\bar X_n-\theta)^2\le z_{\alpha/2}^2\theta(1-\theta)$，即

$$
\theta^2(n+z_{\alpha/2}^2)-\theta(2n\bar X_n+z_{\alpha/2}^2)+n\bar X_n^2\le0,
$$

它恰好在 $c_1\le\theta\le c_2$ 时成立，其中

$$
c_{1,2}=\frac n{n+z_{\alpha/2}^2}\left[\bar X_n+\frac{z_{\alpha/2}^2}{2n}\mp z_{\alpha/2}\sqrt{\frac{\bar X_n(1-\bar X_n)}n+\frac{z_{\alpha/2}^2}{4n^2}}\right].
$$

所以 $[c_1(\boldsymbol{X}),c_2(\boldsymbol{X})]$ 是置信水平近似为 $1-\alpha$ 的置信区间，称为 Wilson 得分区间。

方法 2：替换方差。方法 1 的区间有些复杂，而在其他问题中不等式 $|T|\le z_{\alpha/2}$ 可能没有闭式解。由弱大数定律，可以把分母换成相合估计。这里

$$
S_n^2=\frac1n\sum_{i=1}^n(X_i-\bar X_n)^2=\frac1n\sum_{i=1}^nX_i^2-\bar X_n^2=\bar X_n-\bar X_n^2=\bar X_n(1-\bar X_n)\xrightarrow{p}\theta(1-\theta),
$$

用到了 $X_i^2=X_i$，于是由 Slutsky 定理

$$
\frac{\sqrt n(\bar X_n-\theta)}{\sqrt{\bar X_n(1-\bar X_n)}}\xrightarrow{d}\mathcal{N}(0,1),\qquad\mathbb{P}_\theta\left(-z_{\alpha/2}\le\frac{\sqrt n(\bar X_n-\theta)}{\sqrt{\bar X_n(1-\bar X_n)}}\le z_{\alpha/2}\right)\approx1-\alpha.
$$

由此得到置信系数近似为 $1-\alpha$ 的置信区间

$$
\left[\bar X_n-z_{\alpha/2}\sqrt{\frac{\bar X_n(1-\bar X_n)}n},\ \bar X_n+z_{\alpha/2}\sqrt{\frac{\bar X_n(1-\bar X_n)}n}\right]=\bar X_n\pm z_{\alpha/2}\sqrt{\frac{\bar X_n(1-\bar X_n)}n},
$$

称为 Wald 区间，以及近似的置信下限 $\bar X_n-z_\alpha\sqrt{\bar X_n(1-\bar X_n)/n}$ 与置信上限 $\bar X_n+z_\alpha\sqrt{\bar X_n(1-\bar X_n)/n}$。

对废品率，$95\%$ Wald 区间为 $[-0.34\%,\ 6.34\%]$，$95\%$ 置信下限为 $0.19\%$，$95\%$ 置信上限为 $5.81\%$。置信上限远高于 $1\%$，所以数据并不能说明 $\theta<0.01$。Wald 区间还延伸到 $0$ 以下：$\theta$ 接近 $0$ 且只有 $3$ 件废品时，用估计方差的正态近似很差。方法 1 的 Wilson 区间避免了这个问题，这里为 $[1.03\%,\ 8.45\%]$；如下图所示，$n\theta$ 较小时它的覆盖率也更接近名义水平。

**例 4.3.2（Poisson 均值）** 对来自 $\mathrm{Poi}(\theta)$ 的随机样本，$\mathbb{E}_\theta X_1=\operatorname{Var}_\theta(X_1)=\theta$。与上例一样，

$$
\frac{\sqrt n(\bar X_n-\theta)}{\sqrt\theta}\xrightarrow{d}\mathcal{N}(0,1)\qquad\text{与}\qquad\frac{\sqrt n(\bar X_n-\theta)}{\sqrt{\bar X_n}}\xrightarrow{d}\mathcal{N}(0,1),
$$

后者给出置信系数近似为 $1-\alpha$ 的区间 $\bar X_n\pm z_{\alpha/2}\sqrt{\bar X_n/n}$。

**例 4.3.3（指数均值）** 设 $X_1,\dots,X_n$ 是来自均值为 $\theta$ 的指数分布的随机样本，密度 $f(x;\theta)=\frac1\theta\mathrm{e}^{-x/\theta}$，$x>0$，即 $\mathrm{Exp}(1/\theta)$。则 $\mathbb{E}_\theta X_1=\theta$，$\operatorname{Var}_\theta(X_1)=\theta^2$，故

$$
\frac{\sqrt n(\bar X_n-\theta)}\theta\xrightarrow{d}\mathcal{N}(0,1)\qquad\text{与}\qquad\frac{\sqrt n(\bar X_n-\theta)}{\bar X_n}\xrightarrow{d}\mathcal{N}(0,1),
$$

近似区间为 $\bar X_n\pm z_{\alpha/2}\bar X_n/\sqrt n$。取 $\theta=1$、$\alpha=0.05$、$n=100$ 作模拟，$1000$ 个这样的区间中有 $93.8\%$ 覆盖了 $\theta$，接近 $0.95$，且随 $n$ 增大覆盖率趋于 $0.95$。与例 4.2.5 的精确区间 $\left[\frac{2n\bar X_n}{\chi^2_{2n,\alpha/2}},\frac{2n\bar X_n}{\chi^2_{2n,1-\alpha/2}}\right]$ 相比，近似区间关于 $\bar X_n$ 对称，而 $\bar X_n$ 的抽样分布是右偏的，因此 $n$ 小时其覆盖率低于名义水平。有精确枢轴量时应优先使用精确区间；没有时才退而使用近似区间。

![名义水平 95% 的区间的覆盖概率。左：theta = 0.03 的 Bernoulli 比例，Wald 区间与 Wilson 区间的精确覆盖率随 n 的变化；Wald 区间严重且不规则地覆盖不足。右：指数均值，近似区间 x_bar +- 1.96 x_bar / sqrt(n) 与精确卡方区间的模拟覆盖率（每个 n 取 4000 个样本）。](./plots/approximate-coverage.py)

### 4.3.3. Behrens–Fisher 问题

**例 4.3.4（均值差，方差不等）** 回到两个独立正态样本，现在 $\sigma_1^2\ne\sigma_2^2$，都未知。我们有

$$
\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{\sqrt{\sigma_1^2/m+\sigma_2^2/n}}\sim\mathcal{N}(0,1),\qquad\frac{(m-1)S_X^2}{\sigma_1^2}+\frac{(n-1)S_Y^2}{\sigma_2^2}\sim\chi^2_{m+n-2},
$$

但与等方差情形不同，未知方差不能相互抵消，没有简单的精确枢轴量。在这种情形下（尤其是 $m,n$ 不大时）求 $\mu_1-\mu_2$ 的精确置信区间，就是 Behrens–Fisher 问题（Behrens–Fisher problem），由 W. Behrens（1929）提出，R. A. Fisher、H. Scheffé、B. L. Welch 等许多人都研究过。

若 $m$ 与 $n$ 都很大，把方差换成其估计，并应用中心极限定理与 Slutsky 定理，得

$$
Z=\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{\sqrt{S_X^2/m+S_Y^2/n}}\xrightarrow{d}\mathcal{N}(0,1)\qquad(m,n\to\infty),
$$

以及置信水平近似为 $1-\alpha$ 的区间

$$
(\bar X-\bar Y)\pm z_{\alpha/2}\sqrt{\frac{S_X^2}m+\frac{S_Y^2}n}.
$$

这一论证没有用到正态性，只需方差有限，所以这个区间对来自任何两个总体的大样本都成立。

对中等样本量，Welch（1938，1947）提出在正态假定下用 $t_r$ 分布近似

$$
T_*=\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{\sqrt{S_X^2/m+S_Y^2/n}}
$$

的分布。把方差估计 $S_X^2/m+S_Y^2/n$ 按前两阶矩与缩放后的 $\chi^2_r$ 相匹配，得自由度

$$
r=\frac{\left(\frac{S_X^2}m+\frac{S_Y^2}n\right)^2}{\frac{S_X^4}{m^2(m-1)}+\frac{S_Y^4}{n^2(n-1)}}
$$

（Welch–Satterthwaite 公式；$\min(m,n)-1\le r\le m+n-2$），查表时取最接近的整数，软件中则直接使用。近似区间为

$$
(\bar X-\bar Y)\pm t_{r,\alpha/2}\sqrt{\frac{S_X^2}m+\frac{S_Y^2}n}.
$$

这个 Welch 区间就是 R 的 `t.test` 默认（`var.equal = FALSE`）给出的区间；除非已知方差相等，推荐使用它而不是合并方差的区间。

对教授薪水（例 4.2.8），教授与助理教授的比较给出：等方差区间 $[39\,255,\ 52\,737]$；正态近似 $[42\,133,\ 49\,860]$；Welch 区间（$r=324.3$）$[42\,118,\ 49\,874]$。后两者一致，而且都与已被证明不合适的等方差区间明显不同。对男性与女性，正态近似给出约 $[5\,354,\ 22\,822]$，接近等方差区间 $[4\,131,\ 24\,045]$，这在方差比与 $1$ 相容时是预料之中的。

## 4.4. 置信域

### 4.4.1. 正态总体的均值与方差

**例 4.4.1** 设 $X_1,\dots,X_n$ 是来自 $\mathcal{N}(\mu,\sigma^2)$ 的随机样本，构造 $\boldsymbol{\theta}=(\mu,\sigma^2)$ 的置信系数为 $1-\alpha$ 的置信域。记 $S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2$，

$$
\frac{\sqrt n(\bar X-\mu)}\sigma\sim\mathcal{N}(0,1),\qquad\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1},
$$

且二者独立。取 $c>0$ 使 $Z\sim\mathcal{N}(0,1)$ 满足 $\mathbb{P}(-c\le Z\le c)=\sqrt{1-\alpha}$（$c$ 由此唯一确定），再取 $0<a<b$ 使 $\mathbb{P}(a\le\chi^2_{n-1}\le b)=\sqrt{1-\alpha}$。则对一切 $\boldsymbol{\theta}$，

$$
\mathbb{P}_{\boldsymbol{\theta}}\left(-c\le\frac{\sqrt n(\bar X-\mu)}\sigma\le c\right)=\mathbb{P}_{\boldsymbol{\theta}}\left((\mu-\bar X)^2\le\frac{c^2\sigma^2}n\right)=\sqrt{1-\alpha},
$$

$$
\mathbb{P}_{\boldsymbol{\theta}}\left(a\le\frac{(n-1)S^2}{\sigma^2}\le b\right)=\mathbb{P}_{\boldsymbol{\theta}}\left(\frac{(n-1)S^2}b\le\sigma^2\le\frac{(n-1)S^2}a\right)=\sqrt{1-\alpha},
$$

由独立性

$$
\mathbb{P}_{\boldsymbol{\theta}}\left((\mu-\bar X)^2\le\frac{c^2}n\sigma^2,\ \frac{(n-1)S^2}b\le\sigma^2\le\frac{(n-1)S^2}a\right)=\sqrt{1-\alpha}\cdot\sqrt{1-\alpha}=1-\alpha.
$$

事实上 $c=z_\gamma$，$\gamma=(1-\sqrt{1-\alpha})/2$；把概率 $1-\sqrt{1-\alpha}$ 平均分给 $\chi^2$ 分布的两尾，得 $b=\chi^2_{n-1,\gamma}$，$a=\chi^2_{n-1,1-\gamma}$。置信域为

$$
(\mu-\bar X)^2\le\frac{z_\gamma^2}n\sigma^2,\qquad\frac1{\chi^2_{n-1,\gamma}}\sum_{i=1}^n(X_i-\bar X)^2\le\sigma^2\le\frac1{\chi^2_{n-1,1-\gamma}}\sum_{i=1}^n(X_i-\bar X)^2,\qquad\gamma=\frac{1-\sqrt{1-\alpha}}2.
$$

在 $(\mu,\sigma^2)$ 平面上，它是抛物线 $(\mu-\bar x)^2=c^2\sigma^2/n$ 内部夹在两条水平直线之间的部分。

![例 4.4.1 中 (mu, sigma^2) 的 95% 置信域，由来自 N(0, 1) 的容量为 30 的模拟样本得到：阴影部分位于抛物线 (mu - x_bar)^2 = c^2 sigma^2 / n 内部、两条水平直线之间；叉号表示真实参数。](./plots/normal-confidence-region.py)

### 4.4.2. 多个均值：Šidák 校正与 Bonferroni 校正

**例 4.4.2（独立样本）** 考虑例 4.2.8 中教授与助理教授的平均薪水 $(\mu_1,\mu_2)$。设 $X_1,\dots,X_m$ 为教授的薪水，$Y_1,\dots,Y_n$ 为助理教授的薪水，$X_i\sim\mathcal{N}(\mu_1,\sigma_1^2)$，$Y_j\sim\mathcal{N}(\mu_2,\sigma_2^2)$，两个样本独立。Šidák 校正（Šidák correction）对 $\mu_1$ 与 $\mu_2$ 分别构造置信水平为 $\sqrt{1-\alpha}$ 的置信区间；记 $\gamma=(1-\sqrt{1-\alpha})/2$，由独立性，

$$
\left[\bar X-t_{m-1,\gamma}\frac{S_X}{\sqrt m},\ \bar X+t_{m-1,\gamma}\frac{S_X}{\sqrt m}\right]\times\left[\bar Y-t_{n-1,\gamma}\frac{S_Y}{\sqrt n},\ \bar Y+t_{n-1,\gamma}\frac{S_Y}{\sqrt n}\right]
$$

是置信水平为 $\sqrt{1-\alpha}\cdot\sqrt{1-\alpha}=1-\alpha$ 的置信域。对 $k$ 个独立样本，各取水平 $(1-\alpha)^{1/k}$ 的区间，联合水平即为 $1-\alpha$。

$\alpha=0.05$ 时 $\gamma=0.0127$，每个区间的水平为 $1-2\gamma=0.9747$。单独的 $95\%$ 区间为：$\mu_1$ 是 $[123\,426,\ 130\,118]$，$\mu_2$ 是 $[78\,782,\ 82\,770]$，但它们的乘积的联合水平只有 $0.95^2\approx0.90$；Šidák $95\%$ 置信域为

$$
[122\,950,\ 130\,595]\times[78\,491,\ 83\,061].
$$

**例 4.4.3（相依样本）** 对 $n=500$ 名 18 岁香港儿童的随机样本，以 $(X_i,Y_i)$ 表示体重与身高，设 $(X,Y)$ 服从二元正态分布，均值为 $(\mu_1,\mu_2)$，方差为 $\sigma_1^2,\sigma_2^2$，相关系数为 $\rho$；此时 $X$ 与 $Y$ 相依。点估计为 $\hat\mu_1=\bar X=126.7$，$\hat\mu_2=\bar Y=67.9$（即 $57.5$ 千克与 $172.5$ 厘米），$\hat\sigma_1^2=S_{nX}^2=143.3$，$\hat\sigma_2^2=S_{nY}^2=3.9$，$\hat\rho=0.48$（例 3.2.2）。为构造 $(\mu_1,\mu_2)$ 的 $95\%$ 置信域，Bonferroni 校正（Bonferroni correction）对 $\mu_1$ 与 $\mu_2$ 分别构造置信水平为 $1-\alpha/2$ 的区间。由于

$$
\frac{\sqrt n(\bar X-\mu_1)}{S_X}\sim t_{n-1},\qquad\frac{\sqrt n(\bar Y-\mu_2)}{S_Y}\sim t_{n-1},
$$

有 $\mathbb{P}\left(\left\lvert\frac{\sqrt n(\bar X-\mu_1)}{S_X}\right\rvert\le t_{n-1,\alpha/4}\right)=1-\frac\alpha2$，对 $Y$ 同理。由并集的概率上界，

$$
1-\mathbb{P}\left(\left\lvert\frac{\sqrt n(\bar X-\mu_1)}{S_X}\right\rvert\le t_{n-1,\alpha/4},\ \left\lvert\frac{\sqrt n(\bar Y-\mu_2)}{S_Y}\right\rvert\le t_{n-1,\alpha/4}\right)\le\mathbb{P}\left(\left\lvert\frac{\sqrt n(\bar X-\mu_1)}{S_X}\right\rvert>t_{n-1,\alpha/4}\right)+\mathbb{P}\left(\left\lvert\frac{\sqrt n(\bar Y-\mu_2)}{S_Y}\right\rvert>t_{n-1,\alpha/4}\right)=\frac\alpha2+\frac\alpha2=\alpha,
$$

无论 $X$ 与 $Y$ 如何相依。因此 $(\mu_1,\mu_2)$ 的（保守的）$1-\alpha$ 置信域为

$$
\left[\bar X-t_{n-1,\alpha/4}\frac{S_X}{\sqrt n},\ \bar X+t_{n-1,\alpha/4}\frac{S_X}{\sqrt n}\right]\times\left[\bar Y-t_{n-1,\alpha/4}\frac{S_Y}{\sqrt n},\ \bar Y+t_{n-1,\alpha/4}\frac{S_Y}{\sqrt n}\right].
$$

对这些儿童，$95\%$ 置信域为平均体重 $[125.5,\ 127.9]$ 磅乘以平均身高 $[67.75,\ 68.15]$ 英寸。Bonferroni 校正可以直接推广到 $(\mu_1,\dots,\mu_k)$，每个区间取水平 $1-\alpha/k$，并且不需额外处理就能适用于样本量不同的情形。一种不那么保守的改进是多重检验中使用的 Holm–Bonferroni 方法。

对教授薪水，Bonferroni $95\%$ 置信域为 $[122\,941,\ 130\,603]\times[78\,485,\ 83\,067]$，比 Šidák 置信域 $[122\,950,\ 130\,595]\times[78\,491,\ 83\,061]$ 略大。这一比较具有一般性：Šidák 校正要求独立（更一般地，要求适当形式的正相依），且由于 $(1-\alpha)^{1/k}<1-\alpha/k$，它略为不那么保守；Bonferroni 校正对独立与相依的估计量都成立。

## 小结

- 置信水平为 $1-\alpha$ 的置信区间对参数的每个取值都以不低于 $1-\alpha$ 的概率覆盖参数；这个概率指的是抽样前的随机区间，而不是观测到的区间。可靠度（置信系数）与精度（平均长度）相互冲突，Neyman 原则固定前者、优化后者。
- 枢轴量法把一个好的估计量变换为分布与参数无关的变量，再把关于它的概率陈述反解出来。常用的枢轴量有：

| 模型 | 目标 | 枢轴量 |
|---|---|---|
| $\mathcal{N}(\mu,\sigma^2)$ | $\mu$ | $\sqrt n(\bar X-\mu)/\sigma\sim\mathcal{N}(0,1)$ 或 $\sqrt n(\bar X-\mu)/S\sim t_{n-1}$ |
| $\mathcal{N}(\mu,\sigma^2)$ | $\sigma^2$ | $nS_\mu^2/\sigma^2\sim\chi^2_n$ 或 $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$ |
| $\mathrm{U}(0,\theta)$ | $\theta$ | $X_{(n)}/\theta$，在 $[0,1]$ 上的密度为 $ny^{n-1}$ |
| $\mathrm{Exp}(\lambda)$ | $\lambda$ | $2\lambda n\bar X\sim\chi^2_{2n}$ |
| 两个正态样本，$\sigma_1^2=\sigma_2^2$ | $\mu_1-\mu_2$ | $\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{S_w\sqrt{1/m+1/n}}\sim t_{m+n-2}$ |
| 两个正态样本 | $\sigma_1^2/\sigma_2^2$ | $\frac{S_Y^2/\sigma_2^2}{S_X^2/\sigma_1^2}\sim F_{n-1,m-1}$ |

- 近似区间来自中心极限定理，方差或者保留在枢轴量中（Wilson），或者换成相合估计（Wald）；其覆盖率必须检验，有精确枢轴量时应优先使用。方差不等时，Welch 区间是 Behrens–Fisher 问题的标准解法。
- 多个参数的联合置信域可以构造成矩形：估计量独立时用 Šidák 校正，任意相依时用 Bonferroni 校正。
