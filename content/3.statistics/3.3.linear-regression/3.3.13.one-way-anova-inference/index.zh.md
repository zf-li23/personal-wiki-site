---
title: 单因子方差分析的推断
description: 单元格均值模型与因子效应模型作为示性变量上的回归、可估性与约束；作为一般线性检验的 F 检验；水平均值的置信区间；多重性问题与 LSD、Bonferroni、Tukey、Scheffé 方法；线性组合、对照与对照平方和。
source_hash: 830107d2572f
---

上一章介绍了单因子方差分析的两种模型：单元格均值模型 $Y_{ij}=\mu_i+\varepsilon_{ij}$ 与因子效应模型 $Y_{ij}=\mu+\tau_i+\varepsilon_{ij}$（[3.3.12](/3.3.12)）。本章先把两者写成线性回归，给出明确的**设计矩阵**，并说明为什么因子效应模型需要约束。然后进行推断：把各均值相等的 $F$ 检验看作**一般线性检验**（[3.3.9](/3.3.9)），构造各水平均值的置信区间，并在拒绝原假设之后进一步找出哪些均值不同。比较许多对均值会引出 **Bonferroni 校正**（[3.2.4](/3.2.4)）中已经遇到的多重性问题；我们比较几种控制**族错误率**的标准方法，大量检验的情形在 [3.4.12](/3.4.12) 中还会讨论。本章最后讨论对照，即表达有关均值的研究问题的线性组合。两个因子的情形见 [3.3.14](/3.3.14)。

## 13.1. 作为回归模型的单因子方差分析

### 13.1.1. 单元格均值模型

把观测按水平排列：前 $n_1$ 个观测来自水平 $1$，接下来 $n_2$ 个来自水平 $2$，依此类推。单元格均值模型 $Y_{ij}=\mu_i+\varepsilon_{ij}$ 就是有 $r$ 个示性列、没有截距的回归 $\boldsymbol{Y}=X\boldsymbol\beta+\boldsymbol\varepsilon$：

$$
X=\begin{bmatrix}\boldsymbol{1}_{n_1}&\boldsymbol{0}&\cdots&\boldsymbol{0}\\\boldsymbol{0}&\boldsymbol{1}_{n_2}&\cdots&\boldsymbol{0}\\\vdots&&\ddots&\vdots\\\boldsymbol{0}&\boldsymbol{0}&\cdots&\boldsymbol{1}_{n_r}\end{bmatrix}_{n_T\times r},\qquad \boldsymbol\beta=\begin{bmatrix}\mu_1\\\mu_2\\\vdots\\\mu_r\end{bmatrix},
$$
其中 $\boldsymbol{1}_{n_i}$ 是 $n_i$ 个 1 构成的向量。

**命题 13.1.1** 在单元格均值模型中 $X^{\mathsf T}X=\operatorname{diag}(n_1,\dots,n_r)$，$X^{\mathsf T}\boldsymbol{Y}=(n_1\bar Y_{1\cdot},\dots,n_r\bar Y_{r\cdot})^{\mathsf T}$，因此最小二乘估计量为

$$
\boldsymbol{b}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}=(\bar Y_{1\cdot},\dots,\bar Y_{r\cdot})^{\mathsf T},\qquad \operatorname{Cov}(\boldsymbol{b})=\sigma^2\operatorname{diag}(1/n_1,\dots,1/n_r).
$$

这就用 [3.3.7](/3.3.7) 的矩阵公式重新得到了定理 12.2.1：$\hat\mu_i=\bar Y_{i\cdot}$，每个观测的拟合值是它所在水平的均值，$\hat\mu_i$ 的估计标准误是 $s/\sqrt{n_i}$，其中 $s=\sqrt{\mathrm{MSE}}$ 是合并的标准差。

### 13.1.2. 因子效应模型及其约束

因子效应模型 $Y_{ij}=\mu+\tau_i+\varepsilon_{ij}$ 的参数是 $\mu,\tau_1,\dots,\tau_r$ 与 $\sigma^2$，共 $r+2$ 个，而单元格均值模型只有 $r+1$ 个。它自然的设计矩阵由一列全 1 和 $r$ 个示性列组成：

$$
X\boldsymbol\beta=\begin{bmatrix}\boldsymbol{1}_{n_1}&\boldsymbol{1}_{n_1}&\boldsymbol{0}&\cdots&\boldsymbol{0}\\\boldsymbol{1}_{n_2}&\boldsymbol{0}&\boldsymbol{1}_{n_2}&\cdots&\boldsymbol{0}\\\vdots&&&\ddots&\vdots\\\boldsymbol{1}_{n_r}&\boldsymbol{0}&\boldsymbol{0}&\cdots&\boldsymbol{1}_{n_r}\end{bmatrix}\begin{bmatrix}\mu\\\tau_1\\\vdots\\\tau_r\end{bmatrix}.
$$
第一列是其余各列之和，所以 $X$ 的**秩**为 $r<r+1$，$X^{\mathsf T}X$ 不可逆：参数不能全部唯一地估计。

**例 13.1.1** 设 $r=3$，$\mu_1=10$，$\mu_2=20$，$\mu_3=30$。凡满足 $\mu+\tau_i=\mu_i$ 的参数都描述同样的分布，例如

1. $\mu=0$，$\tau_1=10$，$\tau_2=20$，$\tau_3=30$；
2. $\mu=20$，$\tau_1=-10$，$\tau_2=0$，$\tau_3=10$；
3. $\mu=5000$，$\tau_1=-4990$，$\tau_2=-4980$，$\tau_3=-4970$。

三组参数给出相同的均值，任何数据都无法区分它们。

存在线性无偏估计的参数线性函数称为可估函数（estimable function）；等价地，它是各单元格均值 $\mu_i=\mu+\tau_i$ 的线性函数。组合 $\mu+\tau_i$ 是可估的，由样本均值 $\bar Y_{i\cdot}$ 估计，差 $\tau_i-\tau_k=\mu_i-\mu_k$ 也是可估的；但 $\mu$ 与单个 $\tau_i$ 不可估。解决办法是对 $\tau_i$ 加一个线性约束，使自由参数减少一个，设计矩阵变为列满秩。常用的选择有：

| 约束 | $\mu$ 的含义 | 设计矩阵 |
|---|---|---|
| $\sum_i\tau_i=0$ | 各 $\mu_i$ 的不加权平均 | 去掉 $\tau_r$ 的列；由于 $\tau_r=-\tau_1-\cdots-\tau_{r-1}$，水平 $r$ 的行在每个 $\tau$ 列上取 $-1$ |
| $\tau_1=0$（R 的默认） | 基线水平 $1$ 的均值 | 去掉 $\tau_1$ 的列 |
| $\tau_r=0$ | 水平 $r$ 的均值 | 去掉 $\tau_r$ 的列 |
| $\sum_in_i\tau_i=0$ | 加权平均 $\sum_in_i\mu_i/n_T$ | 同 $\sum_i\tau_i=0$，但带权重 |

还可以有许多其他约束（甚至 $\sum_i\tau_i=100$），它们只改变 $\mu$ 与 $\tau_i$ 的含义。无论用哪种约束，总有 $\mu_i=\mu+\tau_i$ 与 $\hat\mu_i=\bar Y_{i\cdot}$；拟合值、残差和方差分析表都相同。

**命题 13.1.2** 在约束 $\sum_{i=1}^r\tau_i=0$ 下，

$$
\mu=\frac{1}{r}\sum_{i=1}^r\mu_i,\qquad \tau_i=\mu_i-\mu,\qquad \hat\mu=\frac{1}{r}\sum_{i=1}^r\bar Y_{i\cdot},\qquad \hat\tau_i=\bar Y_{i\cdot}-\hat\mu.
$$
若所有 $n_i=n$，则 $\hat\mu=\bar Y_{\cdot\cdot}$。如果一开始就需要加权平均，就定义 $\mu=\sum_in_i\mu_i/n_T=\sum_iw_i\mu_i$，$w_i=n_i/n_T$；约束变为 $\sum_iw_i\tau_i=0$，此时对任意 $n_i$ 都有 $\hat\mu=\bar Y_{\cdot\cdot}$。

**证明** 对 $i$ 求和 $\mu_i=\mu+\tau_i$ 得 $\sum_i\mu_i=r\mu$；代入 $\hat\mu_i=\bar Y_{i\cdot}$ 即得估计。加权的情形相同，只是带权重 $w_i$。$\square$

所以总均值 $\hat\mu$ 是各子样本均值的平均，当 $n_i$ 不等时它与总样本均值 $\bar Y_{\cdot\cdot}$ 不同。用效应表示，$F$ 检验的假设变为

$$
H_0\colon\tau_1=\tau_2=\cdots=\tau_r=0\qquad\text{versus}\qquad H_1\colon\text{at least one }\tau_i\ne0.
$$

### 13.1.3. 例：麦片包装设计

**例 13.1.2** 一家麦片厂商比较 $r=4$ 种包装设计。每种设计在若干商店中使用，$Y$ 为售出的箱数；有一家商店的数据丢失，所以 $n_i=5,5,4,5$，$n_T=19$。

| 设计 | 售出箱数 | $n_i$ | $\bar Y_{i\cdot}$ | $s_i$ |
|---|---|---|---|---|
| 1 | 11, 17, 16, 14, 15 | 5 | 14.6 | 2.302 |
| 2 | 12, 10, 15, 19, 11 | 5 | 13.4 | 3.647 |
| 3 | 23, 20, 18, 17 | 4 | 19.5 | 2.646 |
| 4 | 27, 33, 22, 26, 28 | 5 | 27.2 | 3.962 |

数据对设计的散点图显示各均值不同、散布相近；观测来自不同的商店，独立性是合理的；每种设计只有四五个观测，正态性只能粗略检查（方差分析模型的诊断见 [3.3.14](/3.3.14)）。

```r
a1 <- read.table("CH16TA01.txt")
colnames(a1) <- c("cases", "design", "store")
a2 <- aggregate(a1$cases, list(a1$design), mean)      # level means
a2$sd <- tapply(a1$cases, a1$design, sd)
fit <- lm(cases ~ design, data = a1)                 # wrong: design treated as numeric
a1$design <- factor(a1$design)                       # inform R that design is a factor
fit1 <- lm(cases ~ 0 + design, data = a1)            # cell means model
fit  <- lm(cases ~ design, data = a1)                # factor effects model, tau_1 = 0
```

如果 `design` 仍是数值型，`lm` 会对编码 $1,2,3,4$ 拟合一条直线（斜率 $4.42$，残差标准误 $3.936$，自由度 17），这对分类变量没有意义。把 `design` 设为因子后，两种参数化给出：

| 单元格均值模型（`0 + design`） | 估计 | 标准误 | 因子效应模型（`design`） | 估计 | 标准误 |
|---|---|---|---|---|---|
| design1 | 14.6 | 1.452 | (Intercept) | 14.6 | 1.452 |
| design2 | 13.4 | 1.452 | design2 | −1.2 | 2.054 |
| design3 | 19.5 | 1.624 | design3 | 4.9 | 2.179 |
| design4 | 27.2 | 1.452 | design4 | 12.6 | 2.054 |

两者的残差标准误都是 $s=\sqrt{158.2/15}=3.248$，自由度 $15$。单元格均值的标准误是 $s/\sqrt{n_i}$（而不是 $s_i/\sqrt{n_i}$）：$3.248/\sqrt5=1.452$，$3.248/\sqrt4=1.624$，这依赖于方差齐性的假设。R 去掉了设计 1 的列，对应约束 $\tau_1=0$：截距 $\hat\mu=14.6$ 是基线水平的样本均值，$\hat\tau_i$ 是（水平 $i$ 的样本均值）减（水平 $1$ 的样本均值），例如 $\hat\tau_2=13.4-14.6=-1.2$，$\hat\tau_4=27.2-14.6=12.6$。

两种拟合的整体 $F$ 统计量不同：因子效应模型的 $F=18.59$（自由度 $3$ 与 $15$）检验 $H_0\colon\tau_2=\tau_3=\tau_4=0$，即各均值相等；无截距的单元格均值模型的 $F=170.3$（自由度 $4$ 与 $15$）检验 $\mu_1=\cdots=\mu_4=0$，其 $R^2=0.9785$ 是围绕零而不是围绕 $\bar Y_{\cdot\cdot}$ 计算的。后两者都不是我们关心的。

## 13.2. 检验与置信区间

### 13.2.1. 作为一般线性检验的 F 检验

定理 12.2.3 的方差分析 **F 检验**——在 $H_0\colon\mu_1=\cdots=\mu_r$ 下 $F^*=\mathrm{MSTR}/\mathrm{MSE}\sim F_{r-1,n_T-r}$——就是 [3.3.4](/3.3.4) 与 [3.3.9](/3.3.9) 中的**一般线性检验**，全模型为 $Y_{ij}=\mu_i+\varepsilon_{ij}$，简化模型为 $Y_{ij}=\mu+\varepsilon_{ij}$。简化模型的 $\mathrm{SSE}(R)=\mathrm{SSTO}$，自由度 $n_T-1$；全模型的 $\mathrm{SSE}(F)=\mathrm{SSE}$，自由度 $n_T-r$。于是

$$
F^*=\frac{[\mathrm{SSE}(R)-\mathrm{SSE}(F)]/[(n_T-1)-(n_T-r)]}{\mathrm{SSE}(F)/(n_T-r)}=\frac{\mathrm{SSTR}/(r-1)}{\mathrm{SSE}/(n_T-r)}.
$$
通常在给出结论的同时报告 $p$ 值。

```r
ful <- lm(cases ~ design, data = a1)
red <- lm(cases ~ 1, data = a1)
anova(red, ful)                     # general linear test
summary(aov(cases ~ design, data = a1))   # the same F-test as an ANOVA table
```

对麦片数据，$\mathrm{SSE}(R)=746.42$，自由度 $18$；$\mathrm{SSE}(F)=158.20$，自由度 $15$；故 $\mathrm{SSTR}=588.22$，$\mathrm{MSTR}=196.07$，$\mathrm{MSE}=10.547$，$F^*=18.59$，$p=2.6\times10^{-5}$：四种设计的平均销量不同。

### 13.2.2. 水平均值的置信区间

由于 $\bar Y_{i\cdot}\sim\mathcal{N}(\mu_i,\sigma^2/n_i)$ 且 $\mathrm{SSE}/\sigma^2\sim\chi^2_{n_T-r}$ 与之独立，$\mu_i$ 的 $1-\alpha$ **置信区间**为

$$
\bar Y_{i\cdot}\pm t_{n_T-r,\alpha/2}\,\frac{s}{\sqrt{n_i}},\qquad s=\sqrt{\mathrm{MSE}}=\sqrt{\frac{\sum_i(n_i-1)s_i^2}{n_T-r}}.
$$
自由度 $n_T-r$ 大于单组的 $n_i-1$，因为我们把各组方差合并成一个估计 $s$；在模型假设恰当时，这是方差分析的优势。对麦片数据，$\mathrm{SSE}=4(2.30)^2+4(3.65)^2+3(2.65)^2+4(3.96)^2=158.2$，$s=3.25$，$t_{15,0.025}=2.131$。

| 设计 | $\bar Y_{i\cdot}$ | $s_i$ | 用合并的 $s$ 的 95% 置信区间 | 用 $s_i$（自由度 $n_i-1$）的 95% 置信区间 |
|---|---|---|---|---|
| 1 | 14.6 | 2.302 | $[11.50,\ 17.70]$ | $[11.74,\ 17.46]$ |
| 2 | 13.4 | 3.647 | $[10.30,\ 16.50]$ | $[8.87,\ 17.93]$ |
| 3 | 19.5 | 2.646 | $[16.04,\ 22.96]$ | $[15.29,\ 23.71]$ |
| 4 | 27.2 | 3.962 | $[24.10,\ 30.30]$ | $[22.28,\ 32.12]$ |

不合并的区间为 $\bar Y_{i\cdot}\pm t_{n_i-1,\alpha/2}\,s_i/\sqrt{n_i}$。合并的区间通常更窄，主要原因是自由度 $15$ 的 $t$ 分位数（$2.13$）比自由度 $3$ 或 $4$ 的（$3.18$、$2.78$）小得多；设计 1 的合并区间略宽一些，因为它自己的 $s_1=2.30$ 小于 $s=3.25$。

```r
fit1 <- lm(cases ~ 0 + design, data = a1)
confint(fit1)                       # pooled intervals
```

![左：各包装设计下的麦片销量及各水平均值。右：四个水平均值的 95% 置信区间，分别使用合并标准差与各水平自己的标准差。](./plots/cereal-means-intervals.py)

## 13.3. 多重比较

### 13.3.1. 多重性问题

我们构造了四个（一般为 $r$ 个）95% 置信区间。每个区间以概率 $0.95$ 覆盖其均值，但所有区间同时覆盖各自均值的概率，即总的置信水平，小于 $0.95$。检验也是如此：许多科学研究同时评估不止一个问题，每多一个检验就多一次错误拒绝的机会，因此至少犯一次**第一类错误**的概率随检验个数增大（$\alpha$ 膨胀）。在做过的许多比较中只报告显著的那些，得到的发现往往无法重复；选择性地发表这类结果（发表偏倚）是虚假发现的一个著名来源。

因此必须区分两种错误率。逐比较错误率（comparisonwise error rate）是单独考虑一次比较时犯第一类错误的概率；**族错误率**（FWER，又称实验错误率）是整族比较中至少有一次错误拒绝的概率。"族"意味着"同时"：$r=4$ 个均值有 $6$ 个两两比较的假设 $H_0\colon\mu_i=\mu_k$；若所有均值都相等，只要六个中任何一个被错误拒绝，这次研究就犯了错误。把研究重复 $100$ 次、每个检验都取水平 $0.05$，单个比较 $\mu_1=\mu_2$ 大约被错误拒绝 $5$ 次；而把族错误率控制在 $0.05$，意味着 $100$ 次研究中大约只有 $5$ 次出现任何错误拒绝。若六个检验相互独立且各取水平 $0.05$，族错误率将是 $1-0.95^6=0.26$。

多重比较方法分两类。单步法对所有比较使用同一个临界值，因此每个比较的结论不依赖于其他比较的结果；下面的四种方法都属于此类。逐步法按顺序进行比较，临界值（或是否进行某个比较）依赖于前面的结果；例如 Fisher 的受保护 LSD 只在整体 $F$ 检验显著时才做两两检验，Holm 方法把排好序的 $p$ 值依次与递增的阈值比较。

我们已经知道的调整是 Bonferroni 方法：对 $g$ 个区间各取水平 $1-\alpha/g$，就能保证联合覆盖率至少为 $1-\alpha$。对麦片数据的四个均值：

```r
confint(fit1, level = 1 - 0.05/4)   # Bonferroni simultaneous 95% intervals
```

得到 $[10.48,\ 18.72]$、$[9.28,\ 17.52]$、$[14.89,\ 24.11]$ 与 $[23.08,\ 31.32]$，比上面的单个区间宽。

对单个均值检验 $H_0\colon\mu_i=0$ 通常没有意义。要检验常数 $c$ 下的 $H_0\colon\mu_i=c$，可以把该水平的观测都减去 $c$（或者直接看 $c$ 是否落在 $\mu_i$ 的置信区间内）。

### 13.3.2. 均值的两两比较

通常的后续问题关心均值之差。由于 $\bar Y_{i\cdot}-\bar Y_{k\cdot}\sim\mathcal{N}\big(\mu_i-\mu_k,\ \sigma^2(1/n_i+1/n_k)\big)$，$\mu_i-\mu_k$ 的区间具有形式

$$
\bar Y_{i\cdot}-\bar Y_{k\cdot}\pm t_c\,s(\bar Y_{i\cdot}-\bar Y_{k\cdot}),\qquad s(\bar Y_{i\cdot}-\bar Y_{k\cdot})=s\sqrt{\frac{1}{n_i}+\frac{1}{n_k}},
$$
区间不含 $0$ 时检验拒绝 $\mu_i=\mu_k$。两两比较共有 $\binom r2=r(r-1)/2$ 个，多重性问题通过 $t_c$ 的选取来处理：要么像 Bonferroni 那样改变水平，要么改用别的分布。

**定义 13.3.1（最小显著差数）** **Fisher 最小显著差数**（LSD）法对每个比较都取 $t_c=t_{n_T-r,\alpha/2}$：每个两两比较的区间都是用合并的 $s$ 构造的普通 $1-\alpha$ 区间。

LSD 法忽略了多重性问题：它控制的是逐比较错误率，而不是族错误率。Bonferroni 法采用误差预算的思想：$g=r(r-1)/2$ 个比较各用 $\alpha/g$ 代替 $\alpha$，$t_c=t_{n_T-r,\alpha/(2g)}$，于是族错误率至多为 $\alpha$。

**定义 13.3.2（学生化极差分布）** 设 $Z_1,\dots,Z_r$ 独立同分布于 $\mathcal{N}(0,1)$，$V\sim\chi^2_\nu$ 与它们独立。

$$
Q=\frac{\max_iZ_i-\min_iZ_i}{\sqrt{V/\nu}}
$$
的分布称为参数为 $r$ 与 $\nu$ 的**学生化极差分布**，其上 $\alpha$ 分位数记为 $q_{r,\nu,\alpha}$。

**定理 13.3.1（Tukey 方法）** 设所有 $n_i=n$。则区间

$$
\bar Y_{i\cdot}-\bar Y_{k\cdot}\pm\frac{q_{r,n_T-r,\alpha}}{\sqrt2}\,s\sqrt{\frac2n},\qquad 1\le i<k\le r,
$$
的联合覆盖概率恰为 $1-\alpha$。特别地，在 $H_0\colon\mu_1=\cdots=\mu_r$ 下，

$$
\mathbb{P}\Big(\max_{i,k}\frac{\lvert\bar Y_{i\cdot}-\bar Y_{k\cdot}\rvert}{s\sqrt{2/n}}>\frac{q_{r,n_T-r,\alpha}}{\sqrt2}\Big)=\mathbb{P}\Big(\frac{\bar Y_{\max}-\bar Y_{\min}}{s/\sqrt n}>q_{r,n_T-r,\alpha}\Big)=\alpha.
$$

**证明** 令 $Z_i=(\bar Y_{i\cdot}-\mu_i)/(\sigma/\sqrt n)$，它们独立同分布于 $\mathcal{N}(0,1)$；令 $V=\mathrm{SSE}/\sigma^2\sim\chi^2_{n_T-r}$，它与各 $Z_i$ 独立。所有区间同时覆盖，当且仅当对所有的对都有 $\lvert Z_i-Z_k\rvert\le q_{r,n_T-r,\alpha}\sqrt{V/(n_T-r)}$，即当且仅当 $(\max_iZ_i-\min_iZ_i)/\sqrt{V/(n_T-r)}\le q_{r,n_T-r,\alpha}$，其概率为 $1-\alpha$。$\square$

因此 Tukey 的真正显著差（HSD）检验把 $t_c$ 换成 $q_c/\sqrt2$。$n_i$ 不等时，用同样的 $t_c$ 配合 $s\sqrt{1/n_i+1/n_k}$ 得到 Tukey–Kramer 区间，其族覆盖率至少为 $1-\alpha$。

**定理 13.3.2（Scheffé 方法）** 对每个对照 $L=\sum_ic_i\mu_i$（$\sum_ic_i=0$，定义 13.4.1），记 $\hat L=\sum_ic_i\bar Y_{i\cdot}$，$s^2(\hat L)=\mathrm{MSE}\sum_ic_i^2/n_i$。则区间

$$
\hat L\pm t_c\,s(\hat L),\qquad t_c=\sqrt{(r-1)F_{r-1,n_T-r,\alpha}},
$$
以概率 $1-\alpha$ 同时覆盖所有对照。

**证明** 令 $D_i=\bar Y_{i\cdot}-\mu_i$，$\bar D=\sum_in_iD_i/n_T$。对于对照，$\hat L-L=\sum_ic_i(D_i-\bar D)$，由 Cauchy–Schwarz 不等式

$$
(\hat L-L)^2=\Big(\sum_i\frac{c_i}{\sqrt{n_i}}\sqrt{n_i}(D_i-\bar D)\Big)^2\le\sum_i\frac{c_i^2}{n_i}\cdot\sum_in_i(D_i-\bar D)^2,
$$
当 $c_i=n_i(D_i-\bar D)$ 时取等号，而这也是一个对照。因此 $\sup_{\boldsymbol c}(\hat L-L)^2/s^2(\hat L)=\sum_in_i(D_i-\bar D)^2/\mathrm{MSE}$。分子是由各 $D_i$ 算出的处理平方和，服从 $\sigma^2\chi^2_{r-1}$ 且与 $\mathrm{MSE}$ 独立（定理 12.2.3）；于是上确界除以 $r-1$ 服从 $F_{r-1,n_T-r}$ 分布，所有区间同时覆盖当且仅当它不超过 $F_{r-1,n_T-r,\alpha}$。$\square$

Scheffé 方法处理的是均值的所有线性组合（所有对照）的多重性，而不只是两两比较；它与整体 $F$ 检验一致：$F^*>F_{r-1,n_T-r,\alpha}$ 当且仅当至少有一个对照按 Scheffé 准则显著。代价是只关心少数比较时区间很宽。

| 方法 | 麦片数据的 $t_c$（$\alpha=0.05$，$n_T-r=15$） | 控制的错误率 | 评价 |
|---|---|---|---|
| LSD | $t_{15,0.025}=2.131$ | 逐比较错误率 | 过于宽松（第一类错误过多） |
| Bonferroni | $t_{15,0.05/12}=3.036$ | 族错误率，任意 $g$ 个比较 | $g$ 较小时适用 |
| Tukey | $q_{4,15,0.05}/\sqrt2=4.076/\sqrt2=2.882$ | 族错误率，所有两两比较 | 两两比较的推荐方法 |
| Scheffé | $\sqrt{3F_{3,15,0.05}}=\sqrt{3\times3.287}=3.140$ | 族错误率，所有对照 | 用于两两比较时过于保守（功效低） |

选择方法之前，先想清楚：关注的是否是族错误率，总共有多少个比较，关心的是两两比较还是一般的线性组合。还有其他值得考虑的方法，例如与对照组比较的 Dunnett 方法，以及上面提到的逐步法。

### 13.3.3. 再看麦片的例子

**例 13.3.1** 麦片数据的两两比较，及同时（LSD 为单个）95% 区间：

| 比较 | $\bar Y_{i\cdot}-\bar Y_{k\cdot}$ | LSD | Bonferroni | Tukey | Scheffé |
|---|---|---|---|---|---|
| 2 − 1 | −1.2 | $[-5.58,\ 3.18]$ | $[-7.44,\ 5.04]$ | $[-7.12,\ 4.72]$ | $[-7.65,\ 5.25]$ |
| 3 − 1 | 4.9 | $[0.26,\ 9.54]$ | $[-1.71,\ 11.51]$ | $[-1.38,\ 11.18]$ | $[-1.94,\ 11.74]$ |
| 4 − 1 | 12.6 | $[8.22,\ 16.98]$ | $[6.36,\ 18.84]$ | $[6.68,\ 18.52]$ | $[6.15,\ 19.05]$ |
| 3 − 2 | 6.1 | $[1.46,\ 10.74]$ | $[-0.51,\ 12.71]$ | $[-0.18,\ 12.38]$ | $[-0.74,\ 12.94]$ |
| 4 − 2 | 13.8 | $[9.42,\ 18.18]$ | $[7.56,\ 20.04]$ | $[7.88,\ 19.72]$ | $[7.35,\ 20.25]$ |
| 4 − 3 | 7.7 | $[3.06,\ 12.34]$ | $[1.09,\ 14.31]$ | $[1.42,\ 13.98]$ | $[0.86,\ 14.54]$ |

LSD 法判定六对中有五对不同（除设计 1 与 2 外）；Bonferroni、Tukey 与 Scheffé 各判定三对：设计 4 的销量高于其他三种，而设计 1、2、3 在族水平上无法区分。在三种控制族错误率的方法中，Tukey 的区间最短，Scheffé 的最长，与临界值的大小一致。

```r
pairwise.t.test(a1$cases, a1$design, p.adjust = "none", pool.sd = TRUE)        # Fisher's LSD
pairwise.t.test(a1$cases, a1$design, p.adjust = "bonferroni", pool.sd = TRUE)  # Bonferroni
mod1 <- aov(cases ~ design, data = a1)
TukeyHSD(mod1, conf.level = 0.95)              # Tukey's HSD
library(agricolae)
LSD.test(mod1, trt = "design", group = FALSE, console = TRUE)
scheffe.test(mod1, trt = "design", group = FALSE, console = TRUE)
```

![用 LSD、Bonferroni、Tukey 与 Scheffé 方法得到的麦片均值六个两两差的同时 95% 区间；不含零的区间画成实线。](./plots/pairwise-comparisons.py)

## 13.4. 对照

### 13.4.1. 线性组合与对照

许多研究问题涉及各水平均值的线性组合 $L=\sum_ic_i\mu_i$，例如"设计 1 与 2 的平均销量是否低于设计 3 与 4？"。系数应当来自研究问题，而不是来自对数据的观察（看过数据再选系数是一种隐蔽的多重比较；Scheffé 方法涵盖这种情形）。估计量为

$$
\hat L=\sum_ic_i\bar Y_{i\cdot}\sim\mathcal{N}\big(L,\operatorname{Var}(\hat L)\big),\qquad \operatorname{Var}(\hat L)=\sum_ic_i^2\operatorname{Var}(\bar Y_{i\cdot})=\sigma^2\sum_i\frac{c_i^2}{n_i},\qquad \widehat{\operatorname{Var}}(\hat L)=\mathrm{MSE}\sum_i\frac{c_i^2}{n_i},
$$
线性模型给出任意线性组合的 $t$ 检验：在 $H_0\colon L=L_0$ 下，

$$
T=\frac{\hat L-L_0}{\sqrt{\widehat{\operatorname{Var}}(\hat L)}}\sim t_{n_T-r}.
$$

**定义 13.4.1（对照）** 若 $\sum_ic_i=0$，则线性组合 $L=\sum_ic_i\mu_i$ 称为一个**对照**。

对照比较的是几组均值，与总体水平无关：在任何约束下都有 $\sum_ic_i\mu_i=\sum_ic_i\tau_i$，所以对照在因子效应模型中是可估的。例如 $\mu_1-\mu_2$、$\mu_1-(\mu_2+\mu_3)/2$ 与 $(\mu_1+\mu_2)/2-(\mu_3+\mu_4)/2$。

### 13.4.2. 对照平方和

对 $H_0\colon L=0$，统计量为 $T=\sum_ic_i\bar Y_{i\cdot}\big/\sqrt{\mathrm{MSE}\sum_ic_i^2/n_i}\sim t_{n_T-r}$；由于 $t_{n_T-r}^2$ 服从 $F_{1,n_T-r}$ 分布，

$$
T^2=\frac{\big(\sum_ic_i\bar Y_{i\cdot}\big)^2}{\mathrm{MSE}\sum_ic_i^2/n_i}=\frac{\mathrm{SSC}/1}{\mathrm{MSE}}\sim F_{1,n_T-r},\qquad \mathrm{SSC}=\frac{\big(\sum_ic_i\bar Y_{i\cdot}\big)^2}{\sum_ic_i^2/n_i}.
$$
自由度为 1 的对照平方和（contrast sum of squares）$\mathrm{SSC}$ 表示由这个对照引起的变差。定理 13.3.2 的证明表明，对每个对照都有 $\mathrm{SSC}\le\mathrm{SSTR}$，最优的对照取等号。

也可以同时检验一组对照，每个线性无关的对照占一个自由度。$H_0\colon\mu_2=\mu_3=\mu_4$ 由两个对照（$\mu_2-\mu_3=0$，$\mu_3-\mu_4=0$）组成，其 $F$ 统计量服从 $F_{2,n_T-r}$ 分布；$H_0\colon\mu_1=(\mu_2+\mu_3+\mu_4)/3$ 是单个对照，服从 $F_{1,n_T-r}$ 分布。两者都是一般线性检验。

**例 13.4.1** 对麦片数据，程序包 `multcomp` 可以同时估计并检验几个对照：

```r
mod1 <- aov(cases ~ 0 + design, data = a1)
cntrMat <- rbind("1&2 v 3&4"  = c(0.5, 0.5, -0.5, -0.5),
                 "1 v 2&3&4"  = c(1, -1/3, -1/3, -1/3),
                 "1 v 2&3&4 (x3)" = c(3, -1, -1, -1),
                 "2 v 3"      = c(0, 1, -1, 0))
library(multcomp)
summary(glht(mod1, linfct = cntrMat))      # simultaneous tests, single-step adjustment
```

| 对照 | $\hat L$ | 标准误 | $t$ | 调整后的 $p$ |
|---|---|---|---|---|
| $(\mu_1+\mu_2)/2-(\mu_3+\mu_4)/2$ | $-9.350$ | $1.497$ | $-6.25$ | $<0.001$ |
| $\mu_1-(\mu_2+\mu_3+\mu_4)/3$ | $-5.433$ | $1.694$ | $-3.21$ | $0.015$ |
| $3\mu_1-\mu_2-\mu_3-\mu_4$ | $-16.300$ | $5.083$ | $-3.21$ | $0.015$ |
| $\mu_2-\mu_3$ | $-6.100$ | $2.179$ | $-2.80$ | $0.033$ |

例如 $\hat L_1=(14.6+13.4)/2-(19.5+27.2)/2=-9.35$，标准误为 $\sqrt{10.547\,(0.25/5+0.25/5+0.25/4+0.25/5)}=1.497$。把对照乘以常数（$3\mu_1-\mu_2-\mu_3-\mu_4$ 与 $\mu_1-(\mu_2+\mu_3+\mu_4)/3$）会改变 $\hat L$ 及其标准误，但不改变检验。这些 $p$ 值针对四个同时进行的检验做了调整，所以比未调整的 $t$ 检验 $p$ 值大。

一般线性检验与一组多重比较回答的是不同的问题。比较设计 2、3、4：

```r
library(car)
linearHypothesis(fit1, rbind(c(0, 1, -1, 0), c(0, 0, 1, -1)))    # one F-test, 2 d.f.
summary(glht(fit1, rbind(c(0, 1, -1, 0), c(0, 0, 1, -1))))       # two adjusted t-tests
```

一般线性检验比较受约束模型（$\mathrm{SSE}=636.13$，自由度 $17$）与单元格均值模型（$158.20$，自由度 $15$）：$F=\frac{(636.13-158.20)/2}{10.547}=22.66$，自由度 $2$ 与 $15$，$p=2.9\times10^{-5}$，所以 $\mu_2,\mu_3,\mu_4$ 不全相等。多重比较则指出是哪些差异造成的：$\mu_2-\mu_3$（$\hat L=-6.1$，调整后 $p=0.024$）与 $\mu_3-\mu_4$（$\hat L=-7.7$，调整后 $p=0.0056$）。

## 小结 {#summary}

- 在单元格均值模型中，$X$ 由 $r$ 个示性列组成，$\hat\mu_i=\bar Y_{i\cdot}$，标准误为 $s/\sqrt{n_i}$。在因子效应模型中，全 1 列使 $X$ 秩亏：$\mu+\tau_i$ 与对照可估，而 $\mu$ 与 $\tau_i$ 在施加约束（$\sum\tau_i=0$，或 R 中的 $\tau_1=0$）之前不可估。
- 方差分析的 $F$ 检验是 $Y_{ij}=\mu+\varepsilon_{ij}$ 对 $Y_{ij}=\mu_i+\varepsilon_{ij}$ 的一般线性检验。$\mu_i$ 的区间使用合并的 $s$，自由度 $n_T-r$。
- 比较很多时，族错误率超过 $\alpha$。LSD 忽略多重性；Bonferroni 用比较个数除 $\alpha$；Tukey 的学生化极差方法在 $n_i$ 相等时对所有两两比较是精确的；Scheffé 方法涵盖所有对照。
- 对照 $\sum c_i\mu_i$（$\sum c_i=0$）用 $T=\hat L/s(\hat L)\sim t_{n_T-r}$ 检验，等价于 $\mathrm{SSC}/\mathrm{MSE}\sim F_{1,n_T-r}$；几个对照合在一起构成一般线性检验。
