---
title: 常用分布与共轭族
description: 贝叶斯数据分析的参考章节。本站的记号与 Gelman 等及 scipy.stats 的对照，由核识别分布，连续与离散分布的密度、均值、方差与众数表，分布之间的关系，共轭族及其先验与后验预测分布的汇总，以及用 scipy 计算。
source_hash: 9ab786c44872
---

贝叶斯计算中不断产生密度的乘积，需要把它们识别为某个已知族的成员，再从该族的均值、方差、众数与分位数读出答案。本章把 [3.7.1](/3.7.1)–[3.7.3](/3.7.3) 及本课程其余部分用到的分布集中在一处，采用同一套记号。本章的主要用途是查阅：同一个分布在不同的书和程序里参数化不同，把速率与尺度、方差与尺度的平方、尺度矩阵与其逆混淆，是错误数值最常见的来源。§4.1 确定记号，并与 Gelman 等的 *Bayesian Data Analysis*（其分布表是标准的参考）和 `scipy.stats` 对照，还说明如何由核识别分布。§4.2 与 §4.3 以表格列出连续与离散分布，§4.4 列出它们之间的关系，§4.5 汇总前面各章的共轭族，§4.6 用 Python 展示相应的计算。多数分布已在 [3.1](/3.1)、[3.4.3](/3.4.3) 或 [3.7.2](/3.7.2)–[3.7.3](/3.7.3) 中定义；另有四个族（Laplace、logistic、对数 logistic 与 LKJ）在此处定义。

## 4.1. 记号与参数化

### 4.1.1. 三种约定

下表对每个分布列出本站使用的记号（全站约定，加上 [3.7.2](/3.7.2)–[3.7.3](/3.7.3) 的补充）、Gelman 等的记号，以及对应的 `scipy.stats` 对象。字母相同的参数含义相同，除非表中给出了换算。

| 分布 | 本站 | Gelman 等 | `scipy.stats` |
|---|---|---|---|
| 均匀 | $\mathrm{U}(a,b)$ | $\mathrm{U}(\alpha,\beta)$ | `uniform(loc=a, scale=b-a)` |
| 正态 | $\mathcal{N}(\mu,\sigma^2)$ | $\mathrm{N}(\mu,\sigma^2)$ | `norm(loc=mu, scale=sigma)` |
| 对数正态 | $\mathrm{LN}(\mu,\sigma^2)$ | $\mathrm{lognormal}(\mu,\sigma^2)$ | `lognorm(s=sigma, scale=exp(mu))` |
| 多元正态 | $\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$ | $\mathrm{N}(\mu,\Sigma)$ | `multivariate_normal(mean=mu, cov=Sigma)` |
| Gamma，速率 $\beta$ | $\Gamma(\alpha,\beta)$ | $\mathrm{Gamma}(\alpha,\beta)$ | `gamma(a=alpha, scale=1/beta)` |
| 逆 Gamma，尺度 $\beta$ | $\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$ | $\mathrm{Inv\text{-}gamma}(\alpha,\beta)$ | `invgamma(a=alpha, scale=beta)` |
| 卡方 | $\chi^2_\nu$ | $\chi^2_\nu$ | `chi2(df=nu)` |
| 逆卡方 | $\mathrm{Inv}\text{-}\chi^2_\nu$ | $\mathrm{Inv}\text{-}\chi^2_\nu$ | `invgamma(a=nu/2, scale=1/2)` |
| 尺度逆卡方 | $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$ | $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$ | `invgamma(a=nu/2, scale=nu*s2/2)` |
| 指数，速率 $\beta$ | $\mathrm{Exp}(\beta)$ | $\mathrm{Expon}(\beta)$ | `expon(scale=1/beta)` |
| Laplace | $\mathrm{Laplace}(\mu,\sigma)$ | $\mathrm{Laplace}(\mu,\sigma)$ | `laplace(loc=mu, scale=sigma)` |
| Weibull | $\mathrm{Weibull}(\alpha,\lambda)$，$\lambda=\beta^{-\alpha}$ | $\mathrm{Weibull}(\alpha,\beta)$，尺度 $\beta$ | `weibull_min(c=alpha, scale=beta)` |
| Wishart | $W_d(\nu,S)$ | $\mathrm{Wishart}_\nu(S)$ | `wishart(df=nu, scale=S)` |
| 逆 Wishart | $\mathrm{Inv}\text{-}W_d(\nu,\Psi)$ | $\mathrm{Inv\text{-}Wishart}_\nu(\Psi^{-1})$ | `invwishart(df=nu, scale=Psi)` |
| LKJ | $\mathrm{LKJ}(\eta)$ | $\mathrm{LkjCorr}(\eta)$ | 无（Stan：`lkj_corr(eta)`） |
| $t$，位置–尺度 | $t_\nu(\mu,\sigma^2)$ | $t_\nu(\mu,\sigma^2)$ | `t(df=nu, loc=mu, scale=sigma)` |
| 多元 $t$ | $t_\nu(\boldsymbol{\mu},\Sigma)$ | $t_\nu(\mu,\Sigma)$ | `multivariate_t(loc=mu, shape=Sigma, df=nu)` |
| Beta | $\mathrm{Beta}(\alpha,\beta)$ | $\mathrm{Beta}(\alpha,\beta)$ | `beta(a=alpha, b=beta)` |
| Dirichlet | $\mathrm{Dir}(\boldsymbol{\alpha})$ | $\mathrm{Dirichlet}(\alpha_1,\dots,\alpha_k)$ | `dirichlet(alpha)` |
| logistic | $\mathrm{Logistic}(\mu,\sigma)$ | $\mathrm{Logistic}(\mu,\sigma)$ | `logistic(loc=mu, scale=sigma)` |
| 对数 logistic | $\mathrm{LogLogistic}(\alpha,\beta)$ | $\mathrm{Log\text{-}logistic}(\alpha,\beta)$ | `fisk(c=beta, scale=alpha)` |
| Poisson | $\mathrm{Poi}(\lambda)$ | $\mathrm{Poisson}(\lambda)$ | `poisson(mu=lam)` |
| 二项 | $\mathrm{Bin}(n,p)$ | $\mathrm{Bin}(n,p)$ | `binom(n, p)` |
| 多项 | $\mathrm{Mult}(n,\boldsymbol{p})$ | $\mathrm{Multin}(n;p_1,\dots,p_k)$ | `multinomial(n, p)` |
| 负二项 | $\mathrm{NB}\big(\alpha,\frac{\beta}{\beta+1}\big)$ | $\mathrm{Neg\text{-}bin}(\alpha,\beta)$ | `nbinom(n=alpha, p=beta/(beta+1))` |
| Beta-二项 | $\mathrm{BetaBin}(n,\alpha,\beta)$ | $\mathrm{Beta\text{-}bin}(n,\alpha,\beta)$ | `betabinom(n, a=alpha, b=beta)` |
| Dirichlet-多项 | $\mathrm{DirMult}(n,\boldsymbol{\alpha})$ | 未列入表 | `dirichlet_multinomial(alpha, n)` |

Gelman 等还把在 $\theta$ 处取值的密度写成 $p(\theta)=\mathrm{N}(\theta\mid\mu,\sigma^2)$、$\mathrm{Beta}(\theta\mid\alpha,\beta)$ 等；我们偶尔也用这种形式，例如 [3.7.2](/3.7.2) 中的 $\mathcal{N}(\theta\mid\mu_n,\tau_n^2)$。

### 4.1.2. 需要注意之处

- *速率还是尺度。* 在 $\Gamma(\alpha,\beta)$ 与 $\mathrm{Exp}(\beta)$ 中，参数 $\beta$ 是速率（尺度的倒数）：均值为 $\alpha/\beta$。在 $\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$ 中同一个字母是尺度：若 $X\sim\Gamma(\alpha,\beta)$，则 $1/X\sim\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$，均值为 $\beta/(\alpha-1)$。scipy 总是使用尺度：`gamma(a, scale=1/beta)` 而 `invgamma(a, scale=beta)`。
- *方差还是尺度。* $\mathcal{N}(\mu,\sigma^2)$ 与 $t_\nu(\mu,\sigma^2)$ 写成尺度的平方，但 scipy 的 `norm` 与 `t` 取 `scale=sigma`。对 $t_\nu(\mu,\sigma^2)$，$\sigma^2$ 不是方差：方差为 $\frac{\nu}{\nu-2}\sigma^2$。在 `multivariate_normal` 中参数是协方差矩阵，在 `multivariate_t` 中是尺度矩阵 `shape`。
- *尺度矩阵还是它的逆。* Gelman 等把尺度矩阵为 $\Psi$、均值为 $\Psi/(\nu-d-1)$ 的分布写成 $\mathrm{Inv\text{-}Wishart}_\nu(\Psi^{-1})$；这里与 scipy 中则是 $\mathrm{Inv}\text{-}W_d(\nu,\Psi)$（[3.7.3](/3.7.3)）。[3.4.3](/3.4.3) 的 Wishart 记号 $W_d(\nu,S)$ 在三种约定中都把尺度矩阵放在变元中。
- *负二项分布。* 这里的 $\mathrm{NB}(r,p)$ 与 Gelman 等的 $\mathrm{Neg\text{-}bin}(\alpha,\beta)$ 都计失败次数（取值 $0,1,2,\dots$），并允许实数形状 $\alpha>0$；Gelman 等用 Poisson–Gamma 混合中 Gamma 的参数来参数化，$p=\beta/(\beta+1)$。scipy 的 `nbinom(n, p)` 与 $\mathrm{NB}(n,p)$ 相同。
- *Weibull 分布。* [3.1.4](/3.1.4) 把密度写成 $\lambda\alpha x^{\alpha-1}\mathrm{e}^{-\lambda x^\alpha}$，其中 $\lambda$ 是速率型的；Gelman 等与 scipy 使用尺度 $\beta=\lambda^{-1/\alpha}$。
- *对数正态分布。* $\mu$ 与 $\sigma^2$ 是 $\log\theta$ 的均值与方差，而不是 $\theta$ 的；scipy 的 `lognorm` 取 `s=sigma` 与 `scale=exp(mu)`。

### 4.1.3. 由核识别分布

由 Bayes 公式，后验只要知道到一个常数就已知，$p(\theta\mid y)\propto p(\theta)p(y\mid\theta)$。在共轭模型中，右端作为 $\theta$ 的函数（其余固定），是某个标准密度的核，于是归一化常数、矩与分位数就是该族的相应量。需要识别的核有：

| $\theta$ 的核 | 取值范围 | 分布 |
|---|---|---|
| $\theta^{a-1}\mathrm{e}^{-b\theta}$ | $\theta>0$ | $\Gamma(a,b)$ |
| $\theta^{-(a+1)}\mathrm{e}^{-b/\theta}$ | $\theta>0$ | $\mathrm{Inv}\text{-}\Gamma(a,b)$；当 $a=\frac\nu2$，$b=\frac{\nu s^2}{2}$ 时：$\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$ |
| $\theta^{a-1}(1-\theta)^{b-1}$ | $0<\theta<1$ | $\mathrm{Beta}(a,b)$ |
| $\prod_j\theta_j^{a_j-1}$ | 单纯形 | $\mathrm{Dir}(\boldsymbol{a})$ |
| $\exp\big(-\frac12(A\theta^2-2B\theta)\big)$，$A>0$ | $\mathbb{R}$ | $\mathcal{N}(B/A,1/A)$ |
| $\exp\big(-\frac12(\boldsymbol{\theta}^{\mathsf T}A\boldsymbol{\theta}-2\boldsymbol{b}^{\mathsf T}\boldsymbol{\theta})\big)$ | $\mathbb{R}^d$ | $\mathcal{N}_d(A^{-1}\boldsymbol{b},A^{-1})$ |
| $\big(1+\frac{(\theta-m)^2}{\nu c}\big)^{-(\nu+1)/2}$ | $\mathbb{R}$ | $t_\nu(m,c)$ |
| $\sigma^{-1}(\sigma^2)^{-(\nu/2+1)}\exp\big(-\frac{\nu s^2+\kappa(\mu-m)^2}{2\sigma^2}\big)$ | $(\mu,\sigma^2)$ | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(m,s^2/\kappa;\nu,s^2)$ |
| $(\det W)^{(\nu-d-1)/2}\exp\big(-\frac12\operatorname{tr}(S^{-1}W)\big)$ | 正定矩阵 | $W_d(\nu,S)$ |
| $(\det\Sigma)^{-(\nu+d+1)/2}\exp\big(-\frac12\operatorname{tr}(\Psi\Sigma^{-1})\big)$ | 正定矩阵 | $\mathrm{Inv}\text{-}W_d(\nu,\Psi)$ |

两个正态行就是配方：$A$ 是精度，$B/A$ 是均值。核只有在可积时才能匹配，这也是识别广义后验的方法：$a=0$ 的 $\theta^{a-1}(1-\theta)^{b-1}$ 或 $b=0$ 的 $\theta^{a-1}\mathrm{e}^{-b\theta}$ 都不是密度。

**例 4.1.1** 设 $y_1,\dots,y_n\mid\theta\overset{\text{iid}}{\sim}\mathcal{N}(0,1/\theta)$，即精度为 $\theta$ 的正态分布，并设 $\theta\sim\Gamma(\alpha,\beta)$。则

$$
p(\theta\mid y)\propto\theta^{\alpha-1}\mathrm{e}^{-\beta\theta}\cdot\theta^{n/2}\exp\Big(-\frac\theta2\sum_iy_i^2\Big)=\theta^{\alpha+n/2-1}\exp\Big(-\Big(\beta+\frac12\sum_iy_i^2\Big)\theta\Big),
$$
所以 $\theta\mid y\sim\Gamma\big(\alpha+\frac n2,\beta+\frac12\sum_iy_i^2\big)$，后验均值为 $\frac{2\alpha+n}{2\beta+\sum_iy_i^2}$。对方差 $\sigma^2=1/\theta$，这是逆 Gamma 后验 $\mathrm{Inv}\text{-}\Gamma\big(\alpha+\frac n2,\beta+\frac12\sum_iy_i^2\big)$，即 [3.7.2](/3.7.2) 的分析换了一种参数化：$\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2)$ 就是 $\mathrm{Inv}\text{-}\Gamma(\frac{\nu_0}2,\frac{\nu_0\sigma_0^2}2)$。

## 4.2. 连续分布

### 4.2.1. 实直线上的分布

除正态分布与 $t$ 分布外，贝叶斯建模中还出现两个尾部比正态分布更重的对称族。

**定义 4.2.1（Laplace 分布）** 设 $\mu\in\mathbb{R}$，$\sigma>0$。**Laplace 分布**（双指数分布）$\mathrm{Laplace}(\mu,\sigma)$ 的密度为

$$
p(\theta)=\frac{1}{2\sigma}\exp\Big(-\frac{\lvert\theta-\mu\rvert}{\sigma}\Big),\qquad\theta\in\mathbb{R}.
$$

两个独立的 $\mathrm{Exp}(1/\sigma)$ 变量之差，平移 $\mu$ 后服从 $\mathrm{Laplace}(\mu,\sigma)$。把它用作回归系数的先验，后验众数等于 lasso 估计，正如正态先验给出岭回归一样（[3.3.12](/3.3.12)）。

**定义 4.2.2（logistic 分布）** 设 $\mu\in\mathbb{R}$，$\sigma>0$。**logistic 分布** $\mathrm{Logistic}(\mu,\sigma)$ 的分布函数与密度为

$$
F(\theta)=\frac{1}{1+\mathrm{e}^{-(\theta-\mu)/\sigma}},\qquad p(\theta)=\frac{\mathrm{e}^{-(\theta-\mu)/\sigma}}{\sigma\big(1+\mathrm{e}^{-(\theta-\mu)/\sigma}\big)^2},\qquad\theta\in\mathbb{R}.
$$

它的分布函数是 logit 的反函数，$F(\theta)=\operatorname{logit}^{-1}((\theta-\mu)/\sigma)$，所以当 $U\sim\mathrm{U}(0,1)$ 时 $\mu+\sigma\log\frac{U}{1-U}\sim\mathrm{Logistic}(\mu,\sigma)$。logistic 回归就是这样一种模型：误差服从 logistic 分布的潜变量越过某个阈值。

| 分布 | 密度 | 均值 | 方差 | 众数 |
|---|---|---|---|---|
| $\mathrm{U}(a,b)$，$a<b$ | $\frac{1}{b-a}$，$\theta\in[a,b]$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ | 无 |
| $\mathcal{N}(\mu,\sigma^2)$ | $\frac{1}{\sqrt{2\pi}\sigma}\exp\big(-\frac{(\theta-\mu)^2}{2\sigma^2}\big)$ | $\mu$ | $\sigma^2$ | $\mu$ |
| $t_\nu(\mu,\sigma^2)$ | $\frac{\Gamma(\frac{\nu+1}2)}{\Gamma(\frac\nu2)\sqrt{\nu\pi}\sigma}\big(1+\frac1\nu(\frac{\theta-\mu}{\sigma})^2\big)^{-\frac{\nu+1}{2}}$ | $\mu$（$\nu>1$） | $\frac{\nu}{\nu-2}\sigma^2$（$\nu>2$） | $\mu$ |
| $\mathrm{Laplace}(\mu,\sigma)$ | $\frac{1}{2\sigma}\exp\big(-\frac{\lvert\theta-\mu\rvert}{\sigma}\big)$ | $\mu$ | $2\sigma^2$ | $\mu$ |
| $\mathrm{Logistic}(\mu,\sigma)$ | $\frac{\exp(-(\theta-\mu)/\sigma)}{\sigma(1+\exp(-(\theta-\mu)/\sigma))^2}$ | $\mu$ | $\frac{\pi^2}{3}\sigma^2$ | $\mu$ |

$t$ 族包含没有均值的 **Cauchy 分布** $t_1(\mu,\sigma^2)$，并在 $\nu\to\infty$ 时趋于正态分布。在方差相等的条件下比较，正态分布的尾部最轻，按 $\mathrm{e}^{-\theta^2/2}$ 衰减；logistic 与 Laplace 的尾部按指数衰减，$t$ 的尾部则只按幂 $\lvert\theta\rvert^{-(\nu+1)}$ 衰减。

![标准分布的形状。左图：正态分布、5 个自由度的尺度化 t 分布、Laplace 分布与 logistic 分布的密度，均值均为 0，方差均为 1。中图：它们的右尾（对数坐标）。右图：均值均为 1、方差均为 1/4 的 Gamma 分布、逆 Gamma 分布与对数正态分布的密度。](./plots/distribution_shapes.py)

### 4.2.2. 正半直线上的分布

**定义 4.2.3（对数 logistic 分布）** 设 $\alpha,\beta>0$。若 $\log\theta\sim\mathrm{Logistic}(\log\alpha,1/\beta)$，则称正随机变量 $\theta$ 服从尺度为 $\alpha$、形状为 $\beta$ 的**对数 logistic 分布** $\mathrm{LogLogistic}(\alpha,\beta)$，等价地，

$$
\mathbb{P}(\theta\le x)=\frac{1}{1+(x/\alpha)^{-\beta}},\qquad p(\theta)=\frac{(\beta/\alpha)(\theta/\alpha)^{\beta-1}}{\big(1+(\theta/\alpha)^\beta\big)^2},\qquad\theta>0.
$$

它的中位数为 $\alpha$。它用于生存分析，因为与 Weibull 分布不同，它的风险函数可以先升后降。

| 分布 | 密度，$\theta>0$ | 均值 | 方差 | 众数 |
|---|---|---|---|---|
| $\mathrm{LN}(\mu,\sigma^2)$ | $\frac{1}{\sqrt{2\pi}\sigma\theta}\exp\big(-\frac{(\log\theta-\mu)^2}{2\sigma^2}\big)$ | $\mathrm{e}^{\mu+\sigma^2/2}$ | $\mathrm{e}^{2\mu+\sigma^2}(\mathrm{e}^{\sigma^2}-1)$ | $\mathrm{e}^{\mu-\sigma^2}$ |
| $\Gamma(\alpha,\beta)$ | $\frac{\beta^\alpha}{\Gamma(\alpha)}\theta^{\alpha-1}\mathrm{e}^{-\beta\theta}$ | $\frac\alpha\beta$ | $\frac{\alpha}{\beta^2}$ | $\frac{\alpha-1}{\beta}$（$\alpha\ge1$） |
| $\mathrm{Exp}(\beta)=\Gamma(1,\beta)$ | $\beta\mathrm{e}^{-\beta\theta}$ | $\frac1\beta$ | $\frac1{\beta^2}$ | $0$ |
| $\chi^2_\nu=\Gamma(\frac\nu2,\frac12)$ | $\frac{2^{-\nu/2}}{\Gamma(\nu/2)}\theta^{\nu/2-1}\mathrm{e}^{-\theta/2}$ | $\nu$ | $2\nu$ | $\nu-2$（$\nu\ge2$） |
| $\mathrm{Weibull}$，形状 $\alpha$，尺度 $\beta$ | $\frac\alpha\beta\big(\frac\theta\beta\big)^{\alpha-1}\exp\big(-(\frac\theta\beta)^\alpha\big)$ | $\beta\,\Gamma(1+\frac1\alpha)$ | $\beta^2\big[\Gamma(1+\frac2\alpha)-\Gamma(1+\frac1\alpha)^2\big]$ | $\beta(1-\frac1\alpha)^{1/\alpha}$（$\alpha\ge1$） |
| $\mathrm{LogLogistic}(\alpha,\beta)$ | $\frac{(\beta/\alpha)(\theta/\alpha)^{\beta-1}}{(1+(\theta/\alpha)^\beta)^2}$ | $\frac{\alpha b}{\sin b}$，$b=\frac\pi\beta$（$\beta>1$） | $\alpha^2\big(\frac{2b}{\sin2b}-\frac{b^2}{\sin^2b}\big)$（$\beta>2$） | $\alpha\big(\frac{\beta-1}{\beta+1}\big)^{1/\beta}$（$\beta>1$） |
| $\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$ | $\frac{\beta^\alpha}{\Gamma(\alpha)}\theta^{-(\alpha+1)}\mathrm{e}^{-\beta/\theta}$ | $\frac{\beta}{\alpha-1}$（$\alpha>1$） | $\frac{\beta^2}{(\alpha-1)^2(\alpha-2)}$（$\alpha>2$） | $\frac{\beta}{\alpha+1}$ |
| $\mathrm{Inv}\text{-}\chi^2_\nu=\mathrm{Inv}\text{-}\Gamma(\frac\nu2,\frac12)$ | $\frac{2^{-\nu/2}}{\Gamma(\nu/2)}\theta^{-(\nu/2+1)}\mathrm{e}^{-1/(2\theta)}$ | $\frac{1}{\nu-2}$（$\nu>2$） | $\frac{2}{(\nu-2)^2(\nu-4)}$（$\nu>4$） | $\frac{1}{\nu+2}$ |
| $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)=\mathrm{Inv}\text{-}\Gamma(\frac\nu2,\frac{\nu s^2}2)$ | $\frac{(\nu/2)^{\nu/2}}{\Gamma(\nu/2)}s^\nu\theta^{-(\nu/2+1)}\mathrm{e}^{-\nu s^2/(2\theta)}$ | $\frac{\nu}{\nu-2}s^2$（$\nu>2$） | $\frac{2\nu^2}{(\nu-2)^2(\nu-4)}s^4$（$\nu>4$） | $\frac{\nu}{\nu+2}s^2$ |

**对数正态分布**、Gamma 分布与逆 Gamma 分布可以有相同的均值与方差，形状却大不相同：在上图中，逆 Gamma 分布的左尾最轻、右尾最重，因为 $1/\theta$ 服从 Gamma 分布。逆 Gamma 分布、逆卡方分布与**尺度逆卡方分布**在 [3.7.2](/3.7.2) 中定义（定义 2.4.1）。

在 Gelman 等的表中，对数 logistic 分布的各项需要小心阅读：均值一栏给出的表达式 $1/(1+(x/\alpha)^{-\beta})$ 是分布函数，方差一栏给出的 $\alpha^2\frac{2\pi/\beta}{\sin(2\pi/\beta)}$ 是二阶矩 $\mathbb{E}\theta^2$；均值与方差是上表中的表达式（已对照 `scipy.stats.fisk` 作了数值验证）。

### 4.2.3. 单位区间与单纯形上的分布

| 分布 | 密度 | 均值 | 方差与协方差 | 众数 |
|---|---|---|---|---|
| $\mathrm{Beta}(\alpha,\beta)$ | $\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\theta^{\alpha-1}(1-\theta)^{\beta-1}$，$\theta\in[0,1]$ | $\frac{\alpha}{\alpha+\beta}$ | $\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ | $\frac{\alpha-1}{\alpha+\beta-2}$（$\alpha,\beta>1$） |
| $\mathrm{Dir}(\boldsymbol{\alpha})$，$\alpha_0=\sum_j\alpha_j$ | $\frac{\Gamma(\alpha_0)}{\prod_j\Gamma(\alpha_j)}\prod_j\theta_j^{\alpha_j-1}$，$\boldsymbol{\theta}$ 在单纯形内 | $\mathbb{E}\theta_j=\frac{\alpha_j}{\alpha_0}$ | $\operatorname{Var}\theta_j=\frac{\alpha_j(\alpha_0-\alpha_j)}{\alpha_0^2(\alpha_0+1)}$，$\operatorname{Cov}(\theta_i,\theta_j)=-\frac{\alpha_i\alpha_j}{\alpha_0^2(\alpha_0+1)}$ | $\frac{\alpha_j-1}{\alpha_0-k}$（所有 $\alpha_j>1$） |

Gelman 等把这两个族的参数称为“先验样本量”，与它们作为先验计数的解释一致（[3.7.1](/3.7.1)、[3.7.3](/3.7.3)）。**Beta 分布**与 **Dirichlet 分布**分别在 [3.1](/3.1) 与 [3.7.3](/3.7.3) 中定义（定义 3.2.1）。

### 4.2.4. 多元分布

向量的层次模型需要协方差矩阵的先验。逆 Wishart 先验把方差与相关性捆在一起；现代的替代做法是把它们分开，$\Sigma=\operatorname{diag}(\boldsymbol{\tau})\,\Omega\,\operatorname{diag}(\boldsymbol{\tau})$，其中尺度 $\boldsymbol{\tau}$ 与相关矩阵 $\Omega$ 分别取先验。对 $\Omega$，标准的选择是下面这个族，由 Lewandowski、Kurowicka 与 Joe（2009）提出。

**定义 4.2.4（LKJ 分布）** 设 $\eta>0$。$d\times d$ 相关矩阵（对角线为 1 的对称正定矩阵）的集合上的 **LKJ 分布** $\mathrm{LKJ}(\eta)$ 的密度为

$$
p(\Omega)\propto(\det\Omega)^{\eta-1}.
$$

当 $\eta=1$ 时它在相关矩阵上均匀；当 $\eta>1$ 时它集中在单位矩阵附近，当 $\eta<1$ 时它偏向强相关。每个相关系数 $\omega_{ij}$ 满足 $\frac{\omega_{ij}+1}{2}\sim\mathrm{Beta}(\eta-1+\frac d2,\eta-1+\frac d2)$，所以 $\mathbb{E}\Omega=I_d$，$\operatorname{Var}\omega_{ij}=\frac{1}{2\eta+d-1}$。当 $d=2$ 时，单个相关系数 $r$ 的密度正比于 $(1-r^2)^{\eta-1}$。

| 分布 | 密度 | 均值 | 方差 | 众数 |
|---|---|---|---|---|
| $\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$ | $(2\pi)^{-d/2}(\det\Sigma)^{-1/2}\exp\big(-\frac12(\boldsymbol{\theta}-\boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{\theta}-\boldsymbol{\mu})\big)$ | $\boldsymbol{\mu}$ | $\Sigma$ | $\boldsymbol{\mu}$ |
| $t_\nu(\boldsymbol{\mu},\Sigma)$ | $\frac{\Gamma(\frac{\nu+d}2)}{\Gamma(\frac\nu2)(\nu\pi)^{d/2}}(\det\Sigma)^{-1/2}\big(1+\frac1\nu(\boldsymbol{\theta}-\boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{\theta}-\boldsymbol{\mu})\big)^{-\frac{\nu+d}2}$ | $\boldsymbol{\mu}$（$\nu>1$） | $\frac{\nu}{\nu-2}\Sigma$（$\nu>2$） | $\boldsymbol{\mu}$ |
| $W_d(\nu,S)$，$\nu>d-1$ | $\frac{(\det W)^{(\nu-d-1)/2}\exp(-\frac12\operatorname{tr}(S^{-1}W))}{2^{\nu d/2}(\det S)^{\nu/2}\Gamma_d(\nu/2)}$ | $\nu S$ | $\operatorname{Var}W_{ij}=\nu(s_{ij}^2+s_{ii}s_{jj})$ | $(\nu-d-1)S$（$\nu\ge d+1$） |
| $\mathrm{Inv}\text{-}W_d(\nu,\Psi)$，$\nu>d-1$ | $\frac{(\det\Psi)^{\nu/2}(\det\Sigma)^{-(\nu+d+1)/2}\exp(-\frac12\operatorname{tr}(\Psi\Sigma^{-1}))}{2^{\nu d/2}\Gamma_d(\nu/2)}$ | $\frac{\Psi}{\nu-d-1}$（$\nu>d+1$） | | $\frac{\Psi}{\nu+d+1}$ |
| $\mathrm{LKJ}(\eta)$ | $\propto(\det\Omega)^{\eta-1}$ | $I_d$ | $\operatorname{Var}\omega_{ij}=\frac{1}{2\eta+d-1}$ | $I_d$（$\eta>1$） |

这里 $\Gamma_d(a)=\pi^{d(d-1)/4}\prod_{i=1}^d\Gamma(a+\frac{1-i}{2})$ 是多元 Gamma 函数。**多元正态分布**在 [3.1](/3.1) 中定义，**Wishart 分布**在 [3.4.3](/3.4.3) 中定义，**逆 Wishart 分布**与**多元 t 分布**在 [3.7.3](/3.7.3) 中定义（定义 3.6.1 与 3.6.2）。

## 4.3. 离散分布

Beta-二项分布与 Dirichlet-多项分布分别是二项–Beta 模型与多项–Dirichlet 模型的先验预测分布。后者是多元的 Beta-二项分布：若 $\boldsymbol{\theta}\mid\boldsymbol{p}\sim\mathrm{Mult}(n,\boldsymbol{p})$，$\boldsymbol{p}\sim\mathrm{Dir}(\boldsymbol{\alpha})$，则称 $\boldsymbol{\theta}=(\theta_1,\dots,\theta_k)$ 服从 Dirichlet-多项分布（Dirichlet-multinomial distribution）$\mathrm{DirMult}(n,\boldsymbol{\alpha})$；把 $\boldsymbol{p}$ 积分掉，得到表中的概率函数。

| 分布 | 概率函数 | 均值 | 方差与协方差 | 众数 |
|---|---|---|---|---|
| $\mathrm{Poi}(\lambda)$ | $\frac{\lambda^\theta}{\theta!}\mathrm{e}^{-\lambda}$，$\theta=0,1,\dots$ | $\lambda$ | $\lambda$ | $\lfloor\lambda\rfloor$ |
| $\mathrm{Bin}(n,p)$ | $\binom n\theta p^\theta(1-p)^{n-\theta}$，$\theta=0,\dots,n$ | $np$ | $np(1-p)$ | $\lfloor(n+1)p\rfloor$ |
| $\mathrm{Mult}(n,\boldsymbol{p})$ | $\frac{n!}{\theta_1!\cdots\theta_k!}p_1^{\theta_1}\cdots p_k^{\theta_k}$，$\sum_j\theta_j=n$ | $np_j$ | $np_j(1-p_j)$；$\operatorname{Cov}(\theta_i,\theta_j)=-np_ip_j$ | |
| $\mathrm{NB}\big(\alpha,\frac{\beta}{\beta+1}\big)$ | $\binom{\theta+\alpha-1}{\theta}\big(\frac{\beta}{\beta+1}\big)^\alpha\big(\frac{1}{\beta+1}\big)^\theta$，$\theta=0,1,\dots$ | $\frac\alpha\beta$ | $\frac{\alpha}{\beta^2}(\beta+1)$ | $\lfloor\frac{\alpha-1}{\beta}\rfloor$（$\alpha>1$），否则 $0$ |
| $\mathrm{BetaBin}(n,\alpha,\beta)$ | $\binom n\theta\frac{\mathrm{B}(\alpha+\theta,\beta+n-\theta)}{\mathrm{B}(\alpha,\beta)}$，$\theta=0,\dots,n$ | $\frac{n\alpha}{\alpha+\beta}$ | $\frac{n\alpha\beta(\alpha+\beta+n)}{(\alpha+\beta)^2(\alpha+\beta+1)}$ | |
| $\mathrm{DirMult}(n,\boldsymbol{\alpha})$ | $\frac{n!}{\prod_j\theta_j!}\frac{\Gamma(\alpha_0)}{\Gamma(\alpha_0+n)}\prod_j\frac{\Gamma(\alpha_j+\theta_j)}{\Gamma(\alpha_j)}$，$\sum_j\theta_j=n$ | $\frac{n\alpha_j}{\alpha_0}$ | $\frac{n\alpha_j(\alpha_0-\alpha_j)(\alpha_0+n)}{\alpha_0^2(\alpha_0+1)}$ | |

在负二项一行中，对实数 $\alpha$，$\binom{\theta+\alpha-1}{\theta}=\frac{\Gamma(\theta+\alpha)}{\Gamma(\alpha)\,\theta!}$。当 $\lambda$ 为整数时，Poisson 分布的众数在 $\lambda-1$ 处也达到，二项分布类似地在 $(n+1)p$ 为整数时于 $(n+1)p-1$ 处也达到。与均值相同的二项分布与多项分布相比，Beta-二项分布与 Dirichlet-多项分布是过度离散的，倍数为 $\frac{\alpha_0+n}{\alpha_0+1}$（对 Beta-二项分布 $\alpha_0=\alpha+\beta$），正如负二项分布相对于 Poisson 分布是过度离散的。**Poisson 分布**、**二项分布**、**负二项分布**与**多项分布**在 [3.1](/3.1) 中定义，**Beta-二项分布**在 [3.2.7](/3.2.7) 中定义。

## 4.4. 分布之间的关系

上面的大多数分布由少数几个构造而成：Gamma 分布（连同指数分布与卡方分布）、正态分布，以及它们的倒数、比值与混合。下面的关系不断被用到，既用来推导后验，也用来用它们计算。

| 关系 | 陈述 |
|---|---|
| Gamma 族 | $\mathrm{Exp}(\beta)=\Gamma(1,\beta)$，$\chi^2_\nu=\Gamma(\frac\nu2,\frac12)$；若 $X\sim\Gamma(\alpha,\beta)$，则 $cX\sim\Gamma(\alpha,\beta/c)$，$2\beta X\sim\chi^2_{2\alpha}$；独立的 $\Gamma(\alpha_i,\beta)$ 相加得 $\Gamma(\sum_i\alpha_i,\beta)$ |
| 倒数 | $X\sim\Gamma(\alpha,\beta)\iff1/X\sim\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$；$\mathrm{Inv}\text{-}\chi^2_\nu=\mathrm{Inv}\text{-}\Gamma(\frac\nu2,\frac12)$；$X\sim\mathrm{Inv}\text{-}\chi^2(\nu,s^2)\iff\nu s^2/X\sim\chi^2_\nu$，所以 $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)=\mathrm{Inv}\text{-}\Gamma(\frac\nu2,\frac{\nu s^2}{2})$ |
| 倒数的分布函数 | $\mathbb{P}(X\le x)=1-F_G(1/x)$，其中 $F_G$ 是 Gamma 分布函数；$\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$ 的下 $p$ 分位数为 $1/F_G^{-1}(1-p)$；$\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$ 的下 $p$ 分位数为 $\nu s^2/\chi^2_{\nu,p}$，其中 $\chi^2_{\nu,p}$ 是 $\chi^2_\nu$ 的上 $p$ 分位数 |
| Beta 与 Dirichlet | 对独立的 $G_j\sim\Gamma(\alpha_j,1)$，$(G_j/\sum_iG_i)_j\sim\mathrm{Dir}(\boldsymbol{\alpha})$；$\mathrm{Dir}(\alpha_1,\alpha_2)$ 就是 $\mathrm{Beta}(\alpha_1,\alpha_2)$；合并的分量是 Dirichlet，单个分量是 Beta（命题 3.2.1） |
| 正态尺度混合 | $\theta\mid V\sim\mathcal{N}(\mu,V)$，$V\sim\mathrm{Inv}\text{-}\chi^2(\nu,\sigma^2)$ 给出 $\theta\sim t_\nu(\mu,\sigma^2)$；$V\sim\mathrm{Exp}(1/(2\sigma^2))$（均值为 $2\sigma^2$）给出 $\theta\sim\mathrm{Laplace}(\mu,\sigma)$；$t_1$ 是 Cauchy 分布，$\nu\to\infty$ 时 $t_\nu\to\mathcal{N}$ |
| 多元 $t$ | 对独立的 $\boldsymbol{z}\sim\mathcal{N}_d(\boldsymbol{0},\Sigma)$、$u\sim\chi^2_\nu$，$\boldsymbol{\mu}+\boldsymbol{z}/\sqrt{u/\nu}\sim t_\nu(\boldsymbol{\mu},\Sigma)$；$\frac1d(\boldsymbol{\theta}-\boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{\theta}-\boldsymbol{\mu})\sim F_{d,\nu}$ |
| 正态–逆卡方的边缘分布 | 若 $(\mu,\sigma^2)\sim\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_0,\sigma_0^2/\kappa_0;\nu_0,\sigma_0^2)$，则 $\mu\sim t_{\nu_0}(\mu_0,\sigma_0^2/\kappa_0)$，$\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2)$（[3.7.3](/3.7.3)） |
| 计数的混合 | $\theta\sim\Gamma(\alpha,\beta)$ 的 $\mathrm{Poi}(\theta)$ 是 $\mathrm{NB}(\alpha,\frac{\beta}{\beta+1})$（[3.7.2](/3.7.2)）；$\theta\sim\mathrm{Beta}(\alpha,\beta)$ 的 $\mathrm{Bin}(n,\theta)$ 是 $\mathrm{BetaBin}(n,\alpha,\beta)$（[3.7.1](/3.7.1)）；$\boldsymbol{p}\sim\mathrm{Dir}(\boldsymbol{\alpha})$ 的 $\mathrm{Mult}(n,\boldsymbol{p})$ 是 $\mathrm{DirMult}(n,\boldsymbol{\alpha})$ |
| 对数 | $\theta\sim\mathrm{LN}(\mu,\sigma^2)\iff\log\theta\sim\mathcal{N}(\mu,\sigma^2)$；$\theta\sim\mathrm{LogLogistic}(\alpha,\beta)\iff\log\theta\sim\mathrm{Logistic}(\log\alpha,1/\beta)$ |
| 一维的 Wishart | $W_1(\nu,s^2)=s^2\chi^2_\nu$；$\mathrm{Inv}\text{-}W_1(\nu,\psi)=\mathrm{Inv}\text{-}\Gamma(\frac\nu2,\frac\psi2)=\mathrm{Inv}\text{-}\chi^2(\nu,\psi/\nu)$；$W\sim W_d(\nu,S)$ 的对角元为 $s_{ii}\chi^2_\nu$ |

尺度逆卡方分布的分位数规则就是手算时借助卡方分布表所用的规则，如例 2.4.1：由于 $\nu s^2/X\sim\chi^2_\nu$ 是 $X$ 的减函数，事件 $X\le\nu s^2/c$ 就是事件 $\nu s^2/X\ge c$。

## 4.5. 共轭族

第一个表汇总 [3.7.1](/3.7.1)–[3.7.3](/3.7.3) 的共轭分析与标准的无信息先验，第二个表汇总相应的预测分布。除非另有说明，各行中的数据都是 $n$ 个 iid 观测，$\bar y$ 是样本均值，$s^2$ 是样本方差，$S$ 是关于 $\bar{\boldsymbol{y}}$ 的平方和矩阵，对已知的均值 $\theta$ 或 $\boldsymbol{\mu}$，$v=\frac1n\sum_i(y_i-\theta)^2$，$S_0=\sum_i(\boldsymbol{y}_i-\boldsymbol{\mu})(\boldsymbol{y}_i-\boldsymbol{\mu})^{\mathsf T}$。

| 模型 | 共轭先验 | 后验 | 无信息先验 |
|---|---|---|---|
| $y\sim\mathrm{Bin}(n,\theta)$ | $\mathrm{Beta}(\alpha,\beta)$ | $\mathrm{Beta}(\alpha+y,\beta+n-y)$ | Jeffreys $\mathrm{Beta}(\frac12,\frac12)$；均匀 $\mathrm{Beta}(1,1)$ |
| $y_i\sim\mathrm{Poi}(x_i\theta)$，暴露量 $x_i$ | $\Gamma(\alpha,\beta)$ | $\Gamma(\alpha+\sum_iy_i,\beta+\sum_ix_i)$ | Jeffreys $\theta^{-1/2}$ |
| $y_i\sim\mathrm{Exp}(\theta)$ | $\Gamma(\alpha,\beta)$ | $\Gamma(\alpha+n,\beta+n\bar y)$ | Jeffreys $\theta^{-1}$ |
| $y_i\sim\mathcal{N}(\theta,\sigma^2)$，$\sigma^2$ 已知 | $\mathcal{N}(\mu_0,\tau_0^2)$ | $\mathcal{N}(\mu_n,\tau_n^2)$，$\frac1{\tau_n^2}=\frac1{\tau_0^2}+\frac n{\sigma^2}$，$\mu_n=\tau_n^2\big(\frac{\mu_0}{\tau_0^2}+\frac{n\bar y}{\sigma^2}\big)$ | 平坦：$\mathcal{N}(\bar y,\frac{\sigma^2}n)$ |
| $y_i\sim\mathcal{N}(\theta,\sigma^2)$，$\theta$ 已知 | $\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2)$ | $\mathrm{Inv}\text{-}\chi^2\big(\nu_0+n,\frac{\nu_0\sigma_0^2+nv}{\nu_0+n}\big)$ | Jeffreys $\sigma^{-2}$：$\mathrm{Inv}\text{-}\chi^2(n,v)$ |
| $y_i\sim\mathcal{N}(\mu,\sigma^2)$ | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_0,\frac{\sigma_0^2}{\kappa_0};\nu_0,\sigma_0^2)$ | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_n,\frac{\sigma_n^2}{\kappa_n};\nu_n,\sigma_n^2)$（定理 3.4.1） | $\sigma^{-2}$：$\mu\mid y\sim t_{n-1}(\bar y,\frac{s^2}n)$，$\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(n-1,s^2)$ |
| $\boldsymbol{y}\sim\mathrm{Mult}(n,\boldsymbol{\theta})$ | $\mathrm{Dir}(\boldsymbol{\alpha})$ | $\mathrm{Dir}(\boldsymbol{\alpha}+\boldsymbol{y})$ | Jeffreys $\mathrm{Dir}(\frac12,\dots,\frac12)$；均匀 $\mathrm{Dir}(1,\dots,1)$ |
| $\boldsymbol{y}_i\sim\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$，$\Sigma$ 已知 | $\mathcal{N}_d(\boldsymbol{\mu}_0,\Lambda_0)$ | $\mathcal{N}_d(\boldsymbol{\mu}_n,\Lambda_n)$，$\Lambda_n^{-1}=\Lambda_0^{-1}+n\Sigma^{-1}$，$\boldsymbol{\mu}_n=\Lambda_n(\Lambda_0^{-1}\boldsymbol{\mu}_0+n\Sigma^{-1}\bar{\boldsymbol{y}})$ | 平坦：$\mathcal{N}_d(\bar{\boldsymbol{y}},\frac\Sigma n)$ |
| $\boldsymbol{y}_i\sim\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$，$\boldsymbol{\mu}$ 已知 | $\mathrm{Inv}\text{-}W_d(\nu_0,\Lambda_0)$ | $\mathrm{Inv}\text{-}W_d(\nu_0+n,\Lambda_0+S_0)$ | $(\det\Sigma)^{-(d+1)/2}$：$\mathrm{Inv}\text{-}W_d(n,S_0)$ |
| $\boldsymbol{y}_i\sim\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$ | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}W(\boldsymbol{\mu}_0,\frac{\Lambda_0}{\kappa_0};\nu_0,\Lambda_0)$ | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}W(\boldsymbol{\mu}_n,\frac{\Lambda_n}{\kappa_n};\nu_n,\Lambda_n)$（定理 3.6.1） | $(\det\Sigma)^{-(d+1)/2}$：$\boldsymbol{\mu}\mid\boldsymbol{y}\sim t_{n-d}(\bar{\boldsymbol{y}},\frac{S}{n(n-d)})$，$\Sigma\mid\boldsymbol{y}\sim\mathrm{Inv}\text{-}W_d(n-1,S)$ |

| 模型 | 单个观测的先验预测 | 单个新观测的后验预测 |
|---|---|---|
| $y\sim\mathrm{Bin}(n,\theta)$，Beta 先验 | $y\sim\mathrm{BetaBin}(n,\alpha,\beta)$ | $\tilde n$ 次新试验中的 $\tilde y$：$\mathrm{BetaBin}(\tilde n,\alpha+y,\beta+n-y)$ |
| $\mathrm{Poi}(x\theta)$，Gamma 先验 | $\mathrm{NB}\big(\alpha,\frac{\beta}{\beta+x}\big)$ | 暴露量 $\tilde x$：$\mathrm{NB}\big(\alpha',\frac{\beta'}{\beta'+\tilde x}\big)$，后验为 $\Gamma(\alpha',\beta')$ |
| $\mathrm{Exp}(\theta)$，Gamma 先验 | $p(y)=\frac{\alpha\beta^\alpha}{(\beta+y)^{\alpha+1}}$，$y>0$ | 同样的形式，取 $(\alpha+n,\beta+n\bar y)$ |
| $\mathcal{N}(\theta,\sigma^2)$，$\sigma^2$ 已知 | $\mathcal{N}(\mu_0,\sigma^2+\tau_0^2)$ | $\mathcal{N}(\mu_n,\sigma^2+\tau_n^2)$ |
| $\mathcal{N}(\theta,\sigma^2)$，$\theta$ 已知 | $t_{\nu_0}(\theta,\sigma_0^2)$ | $t_{\nu_0+n}\big(\theta,\frac{\nu_0\sigma_0^2+nv}{\nu_0+n}\big)$ |
| $\mathcal{N}(\mu,\sigma^2)$，共轭先验 | $t_{\nu_0}\big(\mu_0,\frac{\kappa_0+1}{\kappa_0}\sigma_0^2\big)$ | $t_{\nu_n}\big(\mu_n,\frac{\kappa_n+1}{\kappa_n}\sigma_n^2\big)$；取 $\sigma^{-2}$：$t_{n-1}\big(\bar y,(1+\frac1n)s^2\big)$ |
| $\mathrm{Mult}(n,\boldsymbol{\theta})$，Dirichlet 先验 | $\boldsymbol{y}\sim\mathrm{DirMult}(n,\boldsymbol{\alpha})$ | $\mathbb{P}(\tilde y=j\mid\boldsymbol{y})=\frac{\alpha_j+y_j}{\alpha_0+n}$；$m$ 个新观测：$\mathrm{DirMult}(m,\boldsymbol{\alpha}+\boldsymbol{y})$ |
| $\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$，$\Sigma$ 已知 | $\mathcal{N}_d(\boldsymbol{\mu}_0,\Sigma+\Lambda_0)$ | $\mathcal{N}_d(\boldsymbol{\mu}_n,\Sigma+\Lambda_n)$ |
| $\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$，共轭先验 | $t_{\nu_0-d+1}\big(\boldsymbol{\mu}_0,\frac{(\kappa_0+1)\Lambda_0}{\kappa_0(\nu_0-d+1)}\big)$ | $t_{\nu_n-d+1}\big(\boldsymbol{\mu}_n,\frac{(\kappa_n+1)\Lambda_n}{\kappa_n(\nu_n-d+1)}\big)$ |

所有 $t$ 的条目都是 §4.4 的正态尺度混合的实例，所有计数的条目都是计数混合的实例。每个共轭先验都可以解释为先验数据（先验计数、先验暴露量、关于均值的先验观测数 $\kappa_0$ 与关于方差的先验观测数 $\nu_0$），并且表中每个无信息先验都是共轭族的极限；在正态模型中，这些极限重现经典的枢轴量（[3.7.3](/3.7.3)）。

## 4.6. 用 scipy 计算

§4.1 的换算用代码表示，并与前面各章的结果核对：

```python
import numpy as np
from scipy import stats

# Gamma(alpha, beta), beta a rate: scipy's scale is 1/beta
post = stats.gamma(32.25, scale=1 / 10.5)               # traffic accidents (Example 2.2.1)
print(np.round([post.mean(), *post.ppf([0.025, 0.975]), post.sf(3)], 4))

# Inv-chi2(nu, s2) = Inv-Gamma(nu/2, nu*s2/2): scipy's invgamma has scale = nu*s2/2
nu, nus2 = 11, 160.37                                   # powder milk (Example 2.4.1)
sigma2 = stats.invgamma(nu / 2, scale=nus2 / 2)
print(np.round(np.sqrt(sigma2.ppf([0.025, 0.5, 0.975])), 3))
# the same quantiles by hand: nu*s2 divided by upper chi-square quantiles
print(np.round(np.sqrt(nus2 / stats.chi2(nu).ppf([0.975, 0.5, 0.025])), 3))

# t_nu(mu, sigma^2): scipy's scale is sigma, not sigma^2
mu_post = stats.t(24, loc=42.208, scale=np.sqrt(95.618 / 24 / 25))  # cheese, Ann (Example 3.4.1)
print(np.round(mu_post.ppf([0.025, 0.975]), 2))

# NB(alpha, beta/(beta+1)) = Gelman et al.'s Neg-bin(alpha, beta): scipy's nbinom(n, p) counts failures
pred = stats.nbinom(32.25, 10.5 / 11.5)                 # next week's accidents
print(np.round([pred.mean(), pred.var(), pred.pmf(0)], 3))

# Inv-W_d(nu, Psi) = Gelman et al.'s Inv-Wishart_nu(Psi^{-1}): scipy uses the scale matrix Psi
Psi = np.array([[2.0, 0.5], [0.5, 1.0]])
draws = stats.invwishart(df=7, scale=Psi).rvs(size=100000, random_state=0)
print(np.round(draws.mean(axis=0), 3), np.round(Psi / (7 - 2 - 1), 3), sep="\n")
```

```text
[3.0714 2.1043 4.2186 0.5296]
[2.705 3.938 6.483]
[2.705 3.938 6.483]
[41.38 43.03]
[3.071 3.364 0.053]
[[0.496 0.124]
 [0.124 0.249]]
[[0.5   0.125]
 [0.125 0.25 ]]
```

这些数值重现了例 2.2.1、例 2.4.1 中 $\sigma$ 的区间 $[2.70,6.48]$（分别用 `invgamma` 与卡方分位数计算）、例 3.4.1 中 Ann 的区间，以及 [3.7.2](/3.7.2) 中下周事故数的预测分布；逆 Wishart 抽样的模拟均值与 $\Psi/(\nu-d-1)$ 一致，这证实了 scipy 的 `scale` 是 $\Psi$ 而不是 $\Psi^{-1}$。当 scipy 中缺少某个分布时，可以借助 §4.4 的关系来模拟：尺度逆卡方分布用 $\nu s^2/X$（$X\sim\chi^2_\nu$），Dirichlet 分布用归一化的 Gamma 变量，正态–逆卡方对则先抽 $\sigma^2$ 再抽 $\mu\mid\sigma^2$。

## 小结

- 记号：$\Gamma(\alpha,\beta)$ 与 $\mathrm{Exp}(\beta)$ 的 $\beta$ 是速率；$\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$ 的 $\beta$ 是尺度；$\mathrm{Inv}\text{-}\chi^2(\nu,s^2)=\mathrm{Inv}\text{-}\Gamma(\frac\nu2,\frac{\nu s^2}2)$；$t_\nu(\mu,\sigma^2)$ 用尺度的平方 $\sigma^2$，方差为 $\frac{\nu}{\nu-2}\sigma^2$；$\mathrm{NB}(\alpha,\frac{\beta}{\beta+1})$ 对应 Gelman 等的 $\mathrm{Neg\text{-}bin}(\alpha,\beta)$；$\mathrm{Inv}\text{-}W_d(\nu,\Psi)$ 对应他们的 $\mathrm{Inv\text{-}Wishart}_\nu(\Psi^{-1})$（§4.1.1）。
- scipy 处处使用尺度：`gamma(a, scale=1/beta)`、`invgamma(a, scale=beta)`、`norm(loc, scale=sigma)`、`t(df, loc, scale=sigma)`、`invwishart(df, scale=Psi)`。
- 共轭模型中的后验由其核识别（§4.1.3）；不可积的核表明后验是广义的。
- 此处新定义的族：Laplace（定义 4.2.1）、logistic（定义 4.2.2）、对数 logistic（定义 4.2.3）、相关矩阵的 LKJ（定义 4.2.4），以及 Dirichlet-多项分布（§4.3）。
- 关系（§4.4）：Gamma 变量的倒数；由归一化的 Gamma 变量得到 Dirichlet；作为正态尺度混合的 $t$ 与 Laplace 分布；作为计数混合的负二项、Beta-二项与 Dirichlet-多项分布；由 Gamma 与卡方的分位数得到逆分布的分位数。
- 带后验、无信息先验与预测分布的共轭族列于 §4.5。

## 思考题

1. 一位同事报告了后验 $\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(10,4)$。把同一个分布写成逆 Gamma 分布，写出 scipy 调用，并借助卡方分布表（$\chi^2_{10,0.5}=9.342$）计算 $\sigma$ 的后验中位数。

   **答** $\mathrm{Inv}\text{-}\chi^2(10,4)=\mathrm{Inv}\text{-}\Gamma(5,20)$，因为 $\frac{\nu s^2}{2}=\frac{10\times4}{2}=20$；在 scipy 中是 `invgamma(5, scale=20)`。由于 $\sigma^2=40/X$，$X\sim\chi^2_{10}$，$\sigma^2$ 的中位数为 $40/9.342=4.282$，$\sigma$ 的中位数为 $\sqrt{4.282}=2.069$（中位数在递增映射 $\sigma^2\mapsto\sigma$ 下保持不变）。$\sigma^2$ 的均值 $\frac{10}{8}\times4=5$ 与众数 $\frac{10}{12}\times4=3.33$ 把尺度 $s^2=4$ 夹在中间。
2. Gelman 等的表给出 $\theta\sim\mathrm{Neg\text{-}bin}(\alpha,\beta)$ 的均值为 $\alpha/\beta$，方差为 $\frac{\alpha}{\beta^2}(\beta+1)$。证明在 $r=\alpha$，$p=\frac{\beta}{\beta+1}$ 下，它们与 $\mathrm{NB}(r,p)$ 的矩 $\mathbb{E}\theta=\frac{r(1-p)}{p}$ 与 $\operatorname{Var}\theta=\frac{r(1-p)}{p^2}$ 一致，并写出 scipy 调用。

   **答** 当 $p=\frac{\beta}{\beta+1}$ 时，$\frac{1-p}{p}=\frac{1/(\beta+1)}{\beta/(\beta+1)}=\frac1\beta$，所以 $\mathbb{E}\theta=\frac\alpha\beta$；又 $\frac{1-p}{p^2}=\frac1\beta\cdot\frac{\beta+1}{\beta}$，所以 $\operatorname{Var}\theta=\frac{\alpha(\beta+1)}{\beta^2}$。在 scipy 中：`nbinom(n=alpha, p=beta/(beta+1))`。
3. 以三种记号识别核为 $p(\theta\mid y)\propto\theta^{-7}\exp(-12/\theta)$（$\theta>0$）的分布，并给出它的均值与众数。

   **答** 核 $\theta^{-(\alpha+1)}\mathrm{e}^{-\beta/\theta}$ 中 $\alpha=6$，$\beta=12$，是 $\mathrm{Inv}\text{-}\Gamma(6,12)$；它是 $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$，其中 $\frac\nu2=6$，$\frac{\nu s^2}2=12$，即 $\mathrm{Inv}\text{-}\chi^2(12,2)$；在 scipy 中是 `invgamma(6, scale=12)`。均值为 $\frac{12}{5}=2.4$，众数为 $\frac{12}{7}=1.714$。
4. 在 scipy 中，`stats.t(df=5, loc=0, scale=2)` 用来表示 $t_5(0,4)$ 先验。这样对吗？这个分布的方差与 $97.5\%$ 分位数是多少？`stats.t(df=5, loc=0, scale=4)` 用我们的记号是什么？

   **答** 对：$t_5(0,4)$ 的尺度平方为 $\sigma^2=4$，所以 `scale=2`。它的方差为 $\frac{5}{3}\times4=6.67$，不是 $4$，$97.5\%$ 分位数为 $2\,t_{5,0.025}=2\times2.571=5.14$。`scale=4` 的调用是 $t_5(0,16)$，方差为 $26.7$：把尺度与它的平方混淆，会使分散程度相差一倍。
5. 证明若 $\theta\mid V\sim\mathcal{N}(\mu,V)$，$V\sim\mathrm{Exp}(\lambda)$（速率 $\lambda$），则 $\theta$ 服从 Laplace 分布，并求其尺度参数。（利用 $\int_0^\infty V^{-1/2}\exp(-\frac{a}{V}-bV)\,\mathrm{d}V=\sqrt{\pi/b}\,\mathrm{e}^{-2\sqrt{ab}}$，$a\ge0$，$b>0$。）

   **答** $p(\theta)=\int_0^\infty\frac{1}{\sqrt{2\pi V}}\mathrm{e}^{-(\theta-\mu)^2/(2V)}\lambda\mathrm{e}^{-\lambda V}\,\mathrm{d}V=\frac{\lambda}{\sqrt{2\pi}}\sqrt{\frac\pi\lambda}\exp\big(-2\sqrt{\lambda(\theta-\mu)^2/2}\big)=\sqrt{\frac\lambda2}\exp\big(-\sqrt{2\lambda}\lvert\theta-\mu\rvert\big)$，其中 $a=(\theta-\mu)^2/2$，$b=\lambda$。这就是 $\mathrm{Laplace}(\mu,\sigma)$，$\sigma=1/\sqrt{2\lambda}$，即 $\lambda=\frac{1}{2\sigma^2}$，$\mathbb{E}V=2\sigma^2$，与 $\operatorname{Var}\theta=\mathbb{E}V=2\sigma^2$ 一致。
6. 设 $\Sigma\sim\mathrm{Inv}\text{-}W_2(\nu,\Psi)$ 是 $2\times2$ 协方差矩阵的先验。选取 $\nu$ 与 $\Psi$，使先验均值为单位矩阵，并用 Gelman 等的记号写出这个先验。在均值相同的条件下，更大的 $\nu$ 表达什么？

   **答** 当 $\nu>3$ 时 $\mathbb{E}\Sigma=\Psi/(\nu-3)$，所以 $\Psi=(\nu-3)I_2$；例如 $\nu=5$，$\Psi=2I_2$。用 Gelman 等的记号，这是 $\mathrm{Inv\text{-}Wishart}_5\big((2I_2)^{-1}\big)=\mathrm{Inv\text{-}Wishart}_5(\frac12I_2)$，在 scipy 中是 `invwishart(df=5, scale=2*np.eye(2))`。取 $\Psi=(\nu-3)I_2$ 时更大的 $\nu$ 保持均值不变，并使先验更集中在均值周围：$\nu$ 是协方差矩阵的先验观测数（[3.7.3](/3.7.3)），$\Psi$ 是相应的先验平方和。
7. 推导单个指数观测 $y\mid\theta\sim\mathrm{Exp}(\theta)$、$\theta\sim\Gamma(\alpha,\beta)$ 的先验预测密度 $p(y)=\frac{\alpha\beta^\alpha}{(\beta+y)^{\alpha+1}}$ 及其均值。

   **答** $p(y)=\int_0^\infty\theta\mathrm{e}^{-\theta y}\frac{\beta^\alpha}{\Gamma(\alpha)}\theta^{\alpha-1}\mathrm{e}^{-\beta\theta}\,\mathrm{d}\theta=\frac{\beta^\alpha}{\Gamma(\alpha)}\cdot\frac{\Gamma(\alpha+1)}{(\beta+y)^{\alpha+1}}=\frac{\alpha\beta^\alpha}{(\beta+y)^{\alpha+1}}$，这里识别出了 $\Gamma(\alpha+1,\beta+y)$ 的核。由**全期望公式**，当 $\alpha>1$ 时 $\mathbb{E}y=\mathbb{E}[\mathbb{E}(y\mid\theta)]=\mathbb{E}(1/\theta)=\frac{\beta}{\alpha-1}$，即 $\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$ 的均值。尾概率 $\mathbb{P}(y>t)=(\frac{\beta}{\beta+t})^\alpha$ 只按多项式衰减：对未知速率混合指数分布，产生重尾分布。
