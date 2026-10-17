---
title: 课程总结
description: 全课的简明回顾——抽样分布与数据压缩、点估计、置信区间、参数与非参数检验、贝叶斯推断——以对比表格组织，并给出构造估计、区间与检验的标准步骤。
source_hash: 26065b629ec6
---

概率论由已知的模型演绎出数据的行为；统计推断沿相反的方向推理，由样本推断产生它的总体。由于样本是随机的，每个结论都带有不确定性，这门学科的核心任务就是量化这种不确定性：用估计量的偏差、方差与均方误差，区间的置信水平，检验的显著性水平与功效，或者在贝叶斯方法中用后验分布本身。本页据此回顾全课：框架与数据压缩的工具（[3.2.1](/3.2.1)、[3.2.2](/3.2.2)），点估计（[3.2.3](/3.2.3)）、区间估计（[3.2.4](/3.2.4)）与假设检验（[3.2.5](/3.2.5)、[3.2.6](/3.2.6)）三类问题，以及贝叶斯方法（[3.2.7](/3.2.7)）。

## 8.1. 基本框架

来自总体 $F$ 的样本 $\boldsymbol{X}=(X_1,\dots,X_n)$ 用一族分布来建模：在参数模型 $\{f(x;\theta)\colon\theta\in\Theta\}$ 中 $\Theta$ 是有限维的，在非参数模型中 $F$ 的形式未知。统计量 $T(\boldsymbol{X})$ 是不含未知量的样本函数，其分布称为抽样分布。关于 $\theta$（或 $F$）的推断有三种形式：

| 问题 | 结果 | 频率学派的评价标准 | 章节 |
|---|---|---|---|
| 点估计 | 一个值 $\hat\theta(\boldsymbol{x})$ | 偏差、方差、MSE、相合性、有效性 | [3.2.3](/3.2.3) |
| 区间估计 | 一个集合 $C(\boldsymbol{x})\subseteq\Theta$ | 覆盖概率 $\mathbb{P}_\theta(\theta\in C(\boldsymbol{X}))\ge1-\alpha$、长度 | [3.2.4](/3.2.4) |
| 假设检验 | 拒绝或接受 $H_0$ | 第一类错误 $\le\alpha$、功效 | [3.2.5](/3.2.5)、[3.2.6](/3.2.6) |

在频率学派看来，$\theta$ 是固定常数，概率陈述指的是抽样的重复；在贝叶斯学派看来，$\theta$ 有先验分布，一切陈述都以观测数据为条件（[3.2.7](/3.2.7)）。

## 8.2. 抽样分布与数据压缩

### 8.2.1. 抽样分布

| 分布 | 构造（$Z,Z_i\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$，各部分相互独立） | 性质 |
|---|---|---|
| $\chi^2_r$ | $Z_1^2+\cdots+Z_r^2$ | 均值 $r$，方差 $2r$；$\chi^2_r=\Gamma(\frac r2,\frac12)$；对 $r$ 可加 |
| $t_r$ | $Z/\sqrt{Y/r}$，$Y\sim\chi^2_r$ | 对称，尾部比 $\mathcal{N}(0,1)$ 厚；$t_1$ 为 Cauchy 分布；$t_r\xrightarrow{d}\mathcal{N}(0,1)$ |
| $F_{r_1,r_2}$ | $(Y_1/r_1)/(Y_2/r_2)$，$Y_i\sim\chi^2_{r_i}$ | $1/F\sim F_{r_2,r_1}$；$t_r^2\sim F_{1,r}$；$F_{r_1,r_2,1-\alpha}=1/F_{r_2,r_1,\alpha}$ |

对正态样本 $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$，记样本均值为 $\bar X$，样本方差为 $S^2=\frac{1}{n-1}\sum_i(X_i-\bar X)^2$（定理 2.1.3）：

$$
\bar X\sim\mathcal{N}\Big(\mu,\frac{\sigma^2}{n}\Big),\qquad \frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1},\qquad \bar X\ \text{与}\ S^2\ \text{独立},\qquad \frac{\sqrt n(\bar X-\mu)}{S}\sim t_{n-1}.
$$
对非正态总体，只要方差有限，**中心极限定理**与 Slutsky 定理（定理 2.1.4）给出 $\sqrt n(\bar X-\mu)/S\xrightarrow{d}\mathcal{N}(0,1)$，这是一切大样本方法的基础。

### 8.2.2. 充分性、完全性与指数族

| 概念 | 定义或判别法 | 作用 |
|---|---|---|
| 充分统计量 $T$ | 给定 $T$ 时 $\boldsymbol{X}$ 的条件分布与 $\theta$ 无关；因子分解 $f(\boldsymbol{x};\theta)=g(T(\boldsymbol{x});\theta)h(\boldsymbol{x})$ | 不损失关于 $\theta$ 的信息；MLE 与贝叶斯方法只通过 $T$ 依赖于 $\boldsymbol{x}$ |
| 极小充分统计量 | 是每个充分统计量的函数 | 最大限度的压缩 |
| 完全统计量 | 对一切 $\theta$ 有 $\mathbb{E}_\theta\varphi(T)=0$ 蕴含 $\varphi(T)=0$ a.s. | 基于 $T$ 的无偏估计唯一 |
| 指数族 | $f(x;\theta)=C(\theta)\exp\{\sum_jQ_j(\theta)T_j(x)\}h(x)$ | $(\sum_iT_1(X_i),\dots,\sum_iT_k(X_i))$ 是充分的，自然参数空间有内点时是完全的 |
| Basu 定理 | 有界完全充分统计量 $T$ 与任一辅助统计量独立 | 例如 $\bar X$ 与 $S^2$ 独立 |

## 8.3. 点估计

### 8.3.1. 评价准则

| 准则 | 定义 | 说明 |
|---|---|---|
| 无偏性 | 对一切 $\theta$ 有 $\mathbb{E}_\theta\hat\theta=\theta$ | $S^2$ 是 $\sigma^2$ 的无偏估计，MLE $\frac{n-1}{n}S^2$ 不是 |
| 均方误差 | $\operatorname{MSE}(\hat\theta)=\mathbb{E}_\theta(\hat\theta-\theta)^2=\operatorname{Var}(\hat\theta)+\operatorname{Bias}(\hat\theta)^2$ | 在偏差与方差之间权衡 |
| 相合性 | $\hat\theta_n\xrightarrow{p}\theta$（强相合：$\xrightarrow{\text{a.s.}}$） | 大样本的最低要求 |
| 渐近正态性 | $\sqrt n(\hat\theta_n-\theta)\xrightarrow{d}\mathcal{N}(0,v(\theta))$ | 近似区间与检验的基础 |
| 有效性 | 方差达到 Cramér–Rao 下界 $\frac{[g'(\theta)]^2}{nI(\theta)}$ | $I(\theta)=\mathbb{E}_\theta\big[(\partial_\theta\log f(X;\theta))^2\big]$ 为 Fisher 信息 |
| UMVUE | 无偏且对每个 $\theta$ 方差最小 | 可能存在而不达到 Cramér–Rao 下界 |

### 8.3.2. 方法

| 方法 | 步骤 | 性质 |
|---|---|---|
| 矩估计 | 令样本矩 $\frac1n\sum X_i^k$ 等于总体矩 $\mathbb{E}_\theta X^k$ 并求解 | 简单、相合、渐近正态；不一定有效 |
| **极大似然估计** | 最大化 $L(\theta;\boldsymbol{x})=\prod f(x_i;\theta)$，通常解似然方程 $\partial_\theta\log L=0$；支撑依赖于 $\theta$ 时检查边界 | 不变性（$g(\hat\theta)$ 是 $g(\theta)$ 的 MLE）；是充分统计量的函数；正则条件下相合且 $\sqrt n(\hat\theta-\theta)\xrightarrow{d}\mathcal{N}(0,1/I(\theta))$，从而渐近有效 |
| 由充分性求 UMVUE | Rao–Blackwell：$\mathbb{E}[\hat\theta\mid T]$ 改进任一无偏估计 $\hat\theta$；Lehmann–Scheffé：完全充分统计量 $T$ 的无偏函数就是 UMVUE | 另有零无偏估计法 |
| 贝叶斯估计 | 后验均值、中位数或众数 | 分别在平方、绝对与 $0$–$1$ 型损失下最优 |
| 最小二乘、核密度估计 | 线性回归中的 OLS（正态误差下与 MLE 相同）；核密度估计 $\frac{1}{nh}\sum K\big(\frac{x-X_i}{h}\big)$ | 带宽 $h$ 控制偏差与方差的权衡 |

## 8.4. 区间估计

枢轴量法：找出分布与 $\theta$ 无关的 $G(\boldsymbol{X};\theta)$，取 $a,b$ 使 $\mathbb{P}(a\le G\le b)=1-\alpha$，再从 $a\le G(\boldsymbol{X};\theta)\le b$ 中解出 $\theta$。正态总体的情形：

| 参数 | 枢轴量 | $1-\alpha$ 置信区间 |
|---|---|---|
| $\mu$，$\sigma^2$ 已知 | $\frac{\sqrt n(\bar X-\mu)}{\sigma}\sim\mathcal{N}(0,1)$ | $\bar X\pm z_{\alpha/2}\,\sigma/\sqrt n$ |
| $\mu$，$\sigma^2$ 未知 | $\frac{\sqrt n(\bar X-\mu)}{S}\sim t_{n-1}$ | $\bar X\pm t_{n-1,\alpha/2}\,S/\sqrt n$ |
| $\sigma^2$，$\mu$ 未知 | $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$ | $\Big[\frac{(n-1)S^2}{\chi^2_{n-1,\alpha/2}},\ \frac{(n-1)S^2}{\chi^2_{n-1,1-\alpha/2}}\Big]$ |
| $\mu_1-\mu_2$，$\sigma_1^2=\sigma_2^2$ 未知 | $\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{S_w\sqrt{1/m+1/n}}\sim t_{m+n-2}$ | $\bar X-\bar Y\pm t_{m+n-2,\alpha/2}\,S_w\sqrt{1/m+1/n}$ |
| $\sigma_1^2/\sigma_2^2$ | $\frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}\sim F_{m-1,n-1}$ | $\Big[\frac{S_1^2/S_2^2}{F_{m-1,n-1,\alpha/2}},\ \frac{S_1^2/S_2^2}{F_{m-1,n-1,1-\alpha/2}}\Big]$ |

其中 $S_w^2=\frac{(m-1)S_1^2+(n-1)S_2^2}{m+n-2}$ 为合并方差。没有正态性时，近似区间来自渐近正态性 $\hat\theta\pm z_{\alpha/2}\widehat{\mathrm{se}}$（例如比例的 $\hat p\pm z_{\alpha/2}\sqrt{\hat p(1-\hat p)/n}$），或来自 bootstrap。单侧置信限只用枢轴量的一侧尾部；多个参数的置信区域把各枢轴量组合起来（或用 Bonferroni 不等式）。贝叶斯可信区间则取后验分位数，并以数据为条件来解释。

## 8.5. 参数假设检验

### 8.5.1. 基本概念与最优检验

$H_0\colon\theta\in\Theta_0$ 对 $H_1\colon\theta\in\Theta_1$ 的检验是一个拒绝域 $W$（或检验函数 $\varphi(\boldsymbol{x})\in[0,1]$）。功效函数为 $\beta_\varphi(\theta)=\mathbb{E}_\theta\varphi(\boldsymbol{X})$；$\theta\in\Theta_0$ 时 $\beta_\varphi(\theta)$ 是第一类错误概率，$\theta\in\Theta_1$ 时 $1-\beta_\varphi(\theta)$ 是第二类错误概率。Neyman–Pearson 原则先控制水平 $\sup_{\Theta_0}\beta_\varphi\le\alpha$，再使功效最大。$p$ 值是由观测数据可以拒绝 $H_0$ 的最小水平。

| 结果 | 内容 |
|---|---|
| Neyman–Pearson 引理 | 对简单假设 $H_0\colon\theta=\theta_0$ 对 $H_1\colon\theta=\theta_1$，水平 $\alpha$ 的最大功效检验在 $f(\boldsymbol{x};\theta_1)/f(\boldsymbol{x};\theta_0)>k$ 时拒绝（必要时在边界上随机化） |
| 指数族中的 UMP 检验 | 对 $Q(\theta)$ 单调的单参数指数族，单侧假设有基于 $T=\sum T(X_i)$ 的 UMP 检验；双侧假设一般不存在 UMP 检验 |
| 似然比检验 | $\lambda(\boldsymbol{x})=\frac{\sup_{\Theta_0}L(\theta;\boldsymbol{x})}{\sup_{\Theta}L(\theta;\boldsymbol{x})}\le c$ 时拒绝；正则条件下 $-2\log\lambda\xrightarrow{d}\chi^2_k$，$k=\dim\Theta-\dim\Theta_0$（Wilks） |
| 与区间的对偶 | $\{\theta_0\colon \text{水平}\ \alpha\ \text{下接受}\ H_0\colon\theta=\theta_0\}$ 是 $1-\alpha$ 置信集，反之亦然 |

### 8.5.2. 正态总体的检验

| 假设 | 统计量 | 零分布 |
|---|---|---|
| $\mu=\mu_0$，$\sigma^2$ 已知 | $Z=\frac{\sqrt n(\bar X-\mu_0)}{\sigma}$ | $\mathcal{N}(0,1)$ |
| $\mu=\mu_0$，$\sigma^2$ 未知 | $T=\frac{\sqrt n(\bar X-\mu_0)}{S}$ | $t_{n-1}$ |
| $\sigma^2=\sigma_0^2$，$\mu$ 未知 | $\chi^2=\frac{(n-1)S^2}{\sigma_0^2}$ | $\chi^2_{n-1}$ |
| $\mu_1-\mu_2=\delta$，方差相等且未知 | $T=\frac{(\bar X-\bar Y)-\delta}{S_w\sqrt{1/m+1/n}}$ | $t_{m+n-2}$ |
| $\sigma_1^2=\sigma_2^2$ | $F=S_1^2/S_2^2$ | $F_{m-1,n-1}$ |
| 成对数据，$\mathbb{E}(Y-X)=0$ | 对 $Z_i=Y_i-X_i$ 作单样本 $t$ 检验 | $t_{n-1}$ |

双侧备择下，$\lvert Z\rvert>z_{\alpha/2}$、$\lvert T\rvert>t_{\cdot,\alpha/2}$，或 $\chi^2$、$F$ 统计量落在其 $\alpha/2$ 与 $1-\alpha/2$ 分位数之外时拒绝；单侧备择下只用水平为 $\alpha$ 的一侧尾部。对 Bernoulli 与 Poisson 参数，以及方差不等且未知的两总体均值，用大样本 $Z$ 统计量代替精确枢轴量。

## 8.6. 非参数检验

| 问题 | 检验 | 统计量与零分布 |
|---|---|---|
| 中位数或成对差值 $=0$ | 符号检验 | $n_+\sim\mathrm{Bin}(n_0,\frac12)$ |
| 对称中心 $=0$ | Wilcoxon 符号秩检验 | $W^+$；均值 $\frac{n_0(n_0+1)}{4}$，方差 $\frac{n_0(n_0+1)(2n_0+1)}{24}$ |
| 两样本的位置平移 | Wilcoxon 秩和检验（Mann–Whitney） | $W$；均值 $\frac{n(N+1)}{2}$，方差 $\frac{mn(N+1)}{12}$ |
| 给定的离散分布或分组分布 | Pearson $\chi^2$ | $\sum\frac{(\text{观测}-\text{期望})^2}{\text{期望}}\approx\chi^2_{r-1-s}$ |
| $r\times s$ 表的独立性或齐一性 | 列联表 $\chi^2$ | $n\big(\sum\frac{n_{ij}^2}{n_{i\cdot}n_{\cdot j}}-1\big)\approx\chi^2_{(r-1)(s-1)}$ |
| 完全给定的连续 $F_0$ | Kolmogorov–Smirnov | $D_n=\sup\lvert F_n-F_0\rvert$，与分布无关 |
| 参数未知的正态性 | Shapiro–Wilk；QQ 图 | 正态性下 $W$ 接近 $1$ |

在正态性下秩检验损失的功效很少（Wilcoxon 检验的渐近相对效率为 $3/\pi\approx0.955$），而在厚尾或有异常值时可能获益很大。

## 8.7. 贝叶斯推断

$$
\pi(\theta\mid\boldsymbol{x})=\frac{f(\boldsymbol{x}\mid\theta)\pi(\theta)}{\int f(\boldsymbol{x}\mid\theta)\pi(\theta)\,\mathrm{d}\theta}\propto\text{似然}\times\text{先验}.
$$

| 任务 | 贝叶斯的做法 |
|---|---|
| 先验的选择 | 主观先验；共轭先验（Beta–二项、Gamma–Poisson、正态–正态、正态–Gamma）；无信息先验：均匀（可能是广义的）、Jeffreys $\propto\sqrt{I(\theta)}$（不变）、最大熵；分层先验 |
| 点估计 | 后验均值（使 PMSE 最小；平方损失）、后验中位数（绝对损失）、MAP（平坦先验下等于 MLE） |
| 不确定性 | 后验方差 $=$ 后验均值的 PMSE |
| 区间 | 可信区间 $\mathbb{P}(\theta\in C\mid\boldsymbol{x})\ge1-\alpha$；HPD 区间最短 |
| 检验 | 比较 $\alpha_0=\mathbb{P}(\Theta_0\mid\boldsymbol{x})$ 与 $\alpha_1=\mathbb{P}(\Theta_1\mid\boldsymbol{x})$；贝叶斯因子 $m_1(\boldsymbol{x})/m_0(\boldsymbol{x})$ |
| 预测 | 后验预测 $p(z\mid\boldsymbol{x})=\int g(z\mid\theta)\pi(\theta\mid\boldsymbol{x})\,\mathrm{d}\theta$ |
| 决策 | 使后验期望损失 $\mathbb{E}[L(a,\theta)\mid\boldsymbol{x}]$ 最小 |

贝叶斯方法遵从似然原理（$p$ 值违反它），其区间与检验陈述具有直接的条件意义；代价是需要指定先验，而先验的影响随样本增大而消失。

## 8.8. 解题步骤

1. 估计量。矩估计：把参数用矩表示，再代入样本矩。MLE：写出 $L(\theta)$，取 $\log L$，解似然方程，并验证是最大值；若支撑依赖于 $\theta$（如 $\mathrm{U}(0,\theta)$），直接求最大值，结果常为某个次序统计量。UMVUE：找出完全充分统计量 $T$ 及 $T$ 的无偏函数，或把任一无偏估计对 $T$ 取条件期望。
2. 置信区间。由 §8.2 的分布理论找出枢轴量，确定其两个分位数，再解出 $\theta$；大样本时把渐近正态的估计量标准化。
3. 检验。简单假设用 Neyman–Pearson 似然比；单调指数族中的单侧假设，基于 $T$ 的相应单侧检验是 UMP 的；一般情形用似然比检验及 Wilks 的 $\chi^2$ 近似。由零分布在水平 $\alpha$ 下确定临界值，或报告 $p$ 值。
4. 没有参数模型时，位置问题用符号与秩，频数和列联表用 Pearson $\chi^2$，分布假设用 Kolmogorov–Smirnov 或 Shapiro–Wilk 检验。
5. 贝叶斯分析。写出似然 $\times$ 先验，认出某个已知分布的核（共轭性），再读出后验均值、分位数与概率。
