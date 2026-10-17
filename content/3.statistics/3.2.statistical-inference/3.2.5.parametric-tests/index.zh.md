---
title: 参数假设检验
description: 原假设与备择假设、拒绝域与检验函数、两类错误、功效与 p 值；正态、两点与 Poisson 总体参数的检验；似然比检验与 Wilks 定理；Neyman–Pearson 引理与一致最大功效检验；与置信区间的对偶；线性回归与两因素方差分析中的检验。
source_hash: 602061cb542a
---

参数估计与假设检验是统计推断的两大任务。在参数问题中，总体分布的形式已知，为 $\{f(x;\theta)\colon\theta\in\Theta\}$，我们要判断感兴趣的参数是否落在参数空间的某个指定子集中；若分布形式未知，检验方法就不能依赖于它，这是 [3.2.6](/3.2.6) 非参数检验的内容。本章先建立基本概念（假设、拒绝域、两类错误、功效与 $p$ 值），并给出正态、两点与 Poisson 总体的经典检验，其检验统计量依赖于 [3.2.2](/3.2.2) 的抽样分布。然后介绍构造检验的两种一般原理：建立在**极大似然估计**（[3.2.3](/3.2.3)）之上的似然比检验，以及 Neyman–Pearson 的最大功效检验理论。最后说明检验与**置信区间**（[3.2.4](/3.2.4)）是同一对象的两种描述，并把理论用于线性回归与方差分析，它们在 [3.3](/3.3) 中进一步展开。

从历史上看，K. Pearson 于 1900 年对分类数据提出了 $\chi^2$ 检验；20 世纪 20 年代 R. A. Fisher 发展了基于 $t$ 分布和 $F$ 分布的显著性检验；J. Neyman 与 E. S. Pearson 自 1928 年起用十年时间研究比较不同检验的准则，把检验问题化为数学最优化问题（NP 理论）；1950 年前后 A. Wald 将其纳入统计决策理论，而贝叶斯方法（[3.2.7](/3.2.7)）作为频率学派之外的另一条路线同时发展。

## 5.1. 基本概念

### 5.1.1. 假设

下面的例子说明检验要回答的是哪一类问题。

**例 5.1.1** 某工厂生产的一种产品长期的废品率为 $p$。商店只在废品率低于 $0.01$ 时才进货。随机抽取 $100$ 件产品，发现其中 $3$ 件是废品。商店是否应当进货？有两种可能：

$$
H_0\colon 0<p\le0.01 \quad\text{vs.}\quad H_1\colon 0.01<p<1,
$$
商店需要判断数据更支持其中哪一个。

**例 5.1.2** 政府部门想通过对 $n$ 名劳动力的抽样，了解某城市的失业率 $\theta$ 是否可以接受，即是否低于 $\theta_0=6.25\%$。它检验 $H_0\colon\theta>\theta_0$ 对 $H_1\colon\theta\le\theta_0$：只有数据给出有力证据时，才宣布失业率可以接受。

**例 5.1.3** 城市卫生部门想知道湖滨浴场每单位体积水中的平均细菌数是否在安全标准 $200$ 以内。采用 Poisson 模型 $\mathrm{Poi}(\theta)$，根据 $n$ 个独立的水样，检验 $H_0\colon\theta>200$ 对 $H_1\colon\theta\le200$。

**例 5.1.4** 随机变量 $X\sim\mathcal{N}(\theta,\sigma^2)$（$\sigma$ 已知）的均值 $\theta$ 表示某种药物的剂量。药物既安全又有效，当且仅当对两个给定的值有 $\theta_1<\theta<\theta_2$，于是检验 $H_0\colon\theta\le\theta_1$ 或 $\theta\ge\theta_2$ 对 $H_1\colon\theta_1<\theta<\theta_2$。

**例 5.1.5** 有人声称一种新疗法比标准疗法更能延长晚期癌症患者的生命。设标准疗法与新疗法下的生存时间分别为 $X\sim\mathcal{N}(\theta_1,\sigma_1^2)$ 与 $Y\sim\mathcal{N}(\theta_2,\sigma_2^2)$，其中 $\theta_1$ 由长期经验已知。假设为 $H_0\colon\theta_2=\theta_1$ 与 $H_1\colon\theta_2>\theta_1$。也可以取 $H_0\colon\theta_2\le\theta_1$；写成 $\theta_2=\theta_1$ 表达了"新疗法不会更差"的前提。"两种疗法没有差别"正是英文 null 一词的来历。

**定义 5.1.1（原假设与备择假设）** 设 $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$ 是一个分布族，$\boldsymbol{X}=(X_1,\dots,X_n)$ 是来自它的随机样本。设 $\Theta_0$ 是 $\Theta$ 的非空真子集，$\Theta_1=\Theta\setminus\Theta_0$。

- **原假设**为 $H_0\colon\theta\in\Theta_0$，意即存在 $\theta_0\in\Theta_0$ 使 $X_i\sim f(x;\theta_0)$；**备择假设**为 $H_1\colon\theta\in\Theta_1$。检验问题记为 $H_0\colon\theta\in\Theta_0$ vs. $H_1\colon\theta\in\Theta_1$。
- 若 $\Theta_0$（或 $\Theta_1$）只含一个点，则称 $H_0$（或 $H_1$）为**简单假设**，否则称为**复合假设**。
- 根据观测值 $x_1,\dots,x_n$ 决定是否拒绝 $H_0$ 的过程称为**假设检验**（以 $H_1$ 为备择检验 $H_0$）。

当 $\Theta\subseteq\mathbb{R}$ 时，常见的形式有

| | $H_0$ | $H_1$ |
|---|---|---|
| 简单对简单 | $\theta=\theta_0$ | $\theta=\theta_1$ |
| 双侧 | $\theta=\theta_0$ | $\theta\ne\theta_0$ |
| 单侧 | $\theta=\theta_0$ 或 $\theta\le\theta_0$ | $\theta>\theta_0$ |
| 单侧 | $\theta=\theta_0$ 或 $\theta\ge\theta_0$ | $\theta<\theta_0$ |
| 区间 | $\theta\le\theta_1$ 或 $\theta\ge\theta_2$ | $\theta_1<\theta<\theta_2$ |

**注 5.1.1** $H_0$ 与 $H_1$ 的位置不能互换。5.1.3 节将说明，检验控制的是错误地拒绝 $H_0$ 的概率，而不是错误地接受 $H_0$ 的概率；因此 $H_0$ 应当是没有充分证据就不愿放弃的命题（现状、"没有效应"），$H_1$ 则是需要数据来证实的论断。

### 5.1.2. 拒绝域与检验函数

**例 5.1.6** 设 $X_1,\dots,X_{10}$ 是来自 $\mathcal{N}(\theta,1)$ 的样本，检验 $H_0\colon\theta=1$ vs. $H_1\colon\theta\ne1$。样本均值 $\bar X$ 是 $\theta$ 的估计，因此自然的做法是：当 $\lvert\bar X-1\rvert>A$ 时拒绝 $H_0$，当 $\lvert\bar X-1\rvert\le A$ 时接受 $H_0$，例如取 $A=1.96/\sqrt{10}=0.62$（5.2 节说明这样取的理由）。对观测值 $2.2, 3.7, 1.6, 1.2, 2.5, 1.3, 2.7, 2.5, 2.2, 2.0$，有 $\bar x=2.19$，$\lvert\bar x-1\rvert=1.19>0.62$，故拒绝 $H_0$。

**定义 5.1.2（拒绝域）** 作为判断依据的统计量 $T(\boldsymbol{X})$ 称为**检验统计量**。样本空间 $\mathcal{X}$ 的子集 $D$ 若满足"$\boldsymbol{x}\in D$ 时拒绝 $H_0$"，则称为**拒绝域**（或否定域），其补集 $D^{\mathsf c}=\mathcal{X}\setminus D$ 称为**接受域**。当 $D$ 形如 $\{T(\boldsymbol{X})>A\}$ 或 $\{\lvert T(\boldsymbol{X})\rvert>A\}$ 时，边界值 $A$ 称为**临界值**。

在例 5.1.6 中，检验统计量是 $\bar X$，临界值是 $A$，$D=\{\boldsymbol{X}\colon\lvert\bar X-1\rvert>A\}$。拒绝域必须能由数据算出，因此不能含有未知参数；要确定 $A$，需要知道检验统计量在 $H_0$ 下的抽样分布。

**定义 5.1.3（检验函数）** 定义在样本空间 $\mathcal{X}$ 上、取值于 $[0,1]$ 的函数 $\varphi(\boldsymbol{x})$ 称为**检验函数**；$\varphi(\boldsymbol{x})$ 表示观测到 $\boldsymbol{x}$ 时拒绝 $H_0$ 的概率。若 $\varphi$ 只取 $0$ 和 $1$ 两个值，则称该检验为**非随机化检验**，它等价于拒绝域 $D=\{\boldsymbol{x}\colon\varphi(\boldsymbol{x})=1\}$；若 $\varphi$ 在一个概率为正的集合上取 $(0,1)$ 中的值，则称为**随机化检验**。

例 5.1.6 的检验是：$\lvert\bar X-1\rvert>A$ 时 $\varphi(\boldsymbol{X})=1$，否则为 $0$。离散数据需要随机化。在例 5.1.1 中，第 $i$ 件产品是废品时令 $X_i=1$，否则 $X_i=0$，并令 $T(\boldsymbol{X})=\sum_{i=1}^{100}X_i$。当 $T<c$ 时接受 $H_0$，$T>c$ 时拒绝 $H_0$；当 $T=c$ 时折中处理，借助一个辅助的随机试验以概率 $r\in(0,1)$ 拒绝 $H_0$（就像奖学金评选中对成绩相同的候选人抽签）：

$$
\varphi(\boldsymbol{X})=\begin{cases}1, & T(\boldsymbol{X})>c,\\ r, & T(\boldsymbol{X})=c,\\ 0, & T(\boldsymbol{X})<c.\end{cases}
$$
5.2.3 节说明如何选取 $c$ 与 $r$。

**注 5.1.2** 刑事审判是一个很好的类比。陪审团从无罪推定出发：$H_0$ 为被告无罪，$H_1$ 为被告有罪。除非证据足够有力、超过某个门槛，否则陪审团坚持这一基本信念；证据足够时才拒绝 $H_0$、判定有罪，否则判无罪。无罪判决不是无罪的证明，有罪判决也不是有罪的证明：判决只是一个可能出错的决定。

### 5.1.3. 两类错误与功效函数

由于样本是随机的，两种决定都可能出错。

**定义 5.1.4（两类错误）** $H_0$ 为真而拒绝 $H_0$ 称为**第一类错误**（弃真，陪审团冤枉了无辜的被告）；$H_0$ 为假而接受 $H_0$ 称为**第二类错误**（取伪，陪审团放过了有罪的被告）。它们的概率是

$$
\begin{aligned}
\alpha(\theta)&=\mathbb{P}_\theta(\boldsymbol{X}\in D),&&\theta\in\Theta_0,\\
\beta(\theta)&=\mathbb{P}_\theta(\boldsymbol{X}\in D^{\mathsf c}),&&\theta\in\Theta_1.
\end{aligned}
$$

例如在例 5.1.1 中采用检验"$T>3$ 时拒绝"，若真实废品率 $p=0.005$ 而观测到 $T=5$，就犯了第一类错误。检验一旦确定，两类错误的概率随之确定；对每个 $\theta$，只可能犯其中一类错误。

**定义 5.1.5（检验的水平与显著性水平）** 犯第一类错误的最大概率 $\sup_{\theta\in\Theta_0}\alpha(\theta)$ 称为检验的**真实水平**（size）。若一个检验的真实水平不超过 $\alpha$，则称它的**显著性水平**为 $\alpha$（或称它为水平 $\alpha$ 的检验）。

本章的大多数检验的真实水平恰好等于预先给定的 $\alpha$，两个说法可以混用。平凡检验 $D=\varnothing$（总是接受 $H_0$）的真实水平为 $0$，但对每个 $\theta\in\Theta_1$ 都有 $\beta(\theta)=1$；样本量 $n$ 固定时，两类错误的概率不能同时变小。

**定义 5.1.6（功效函数）** 检验 $\varphi$ 的**功效函数**为

$$
\pi_\varphi(\theta)=\mathbb{P}_\theta(\text{$\varphi$ 拒绝 $H_0$})=\mathbb{E}_\theta[\varphi(\boldsymbol{X})],\qquad\theta\in\Theta;\tag{5.1}
$$
它在 $\Theta_1$ 上的值称为检验的功效。

对非随机化检验，$\pi_\varphi(\theta)=\mathbb{P}_\theta(\boldsymbol{X}\in D)$；对上面的随机化检验，$\pi_\varphi(\theta)=\mathbb{P}_\theta(T>c)+r\,\mathbb{P}_\theta(T=c)$。两类错误的概率可以从功效函数读出：

$$
\alpha(\theta)=\pi_\varphi(\theta)\ (\theta\in\Theta_0),\qquad \beta(\theta)=1-\pi_\varphi(\theta)\ (\theta\in\Theta_1).
$$
好的功效函数在 $\Theta_0$ 上很小（不超过 $\alpha$），在 $\Theta_1$ 上迅速升向 $1$。

![单侧检验（当 Z = √n (X̄ − μ₀)/σ > z_α 时拒绝 H₀: μ ≤ μ₀）犯两类错误的概率。临界值右移时 α 减小而 β 增大](./plots/type-errors.py)

由于两类错误不能同时控制，J. Neyman 与 E. S. Pearson 提出了 Neyman–Pearson 原则（Neyman–Pearson principle）：先把犯第一类错误的概率控制在预先给定的显著性水平 $\alpha$ 之下，再在所有水平为 $\alpha$ 的检验中，选取犯第二类错误的概率尽可能小（功效尽可能大）的检验。

**注 5.1.3** 在这一原则下，拒绝 $H_0$ 可能犯第一类错误，其概率很小（如 $0.05$）；接受 $H_0$ 可能犯第二类错误，其概率可能很大（如 $0.9$）。因此两种结论的可靠程度并不相同。当数据落在接受域中时，应当说"数据没有提供足够的证据拒绝 $H_0$"，而不是说"$H_0$ 被证明为真"。这就是为什么原假设应当选取错误地拒绝后果最严重的命题，即有把握、不能轻易否定的命题。在例 5.1.2 中，政府部门把"失业率过高"作为 $H_0$，从而只在证据有力时才宣布失业率可以接受。

**注 5.1.4** $\alpha$ 越小，犯第一类错误的概率越小，犯第二类错误的概率越大，越难拒绝 $H_0$，而一旦拒绝也越可靠。$\alpha$ 的选取不是数学问题：它可以由有关各方商定（例 5.1.1 中的商店与工厂），在第一类错误后果严重时取得很小（例 5.1.5 中批准一种无效的疗法），也可以依据先验信息。实践中，拒绝 $H_0$ 往往意味着推翻旧理论或以新方法取代旧方法，这需要数据提供显著的证据。习惯上取 $\alpha=0.05$ 或 $0.01$。

### 5.1.4. p 值

检验只报告"拒绝"或"接受"，并不说明证据有多强。

**例 5.1.7** 设 $X_1,\dots,X_{16}$ 是来自 $\mathcal{N}(\mu,1)$ 的样本，在 $\alpha=0.05$ 下用 $D=\{\lvert\sqrt{16}\,\bar X\rvert>1.96\}=\{\lvert\bar X\rvert>0.49\}$ 检验 $H_0\colon\mu=0$ vs. $H_1\colon\mu\ne0$。$\bar x=0.48$ 与 $\bar x=0.12$ 都导致接受，但前者几乎落入拒绝域，后者则远非如此。在 $H_0$ 下 $U=\sqrt{16}\,\bar X\sim\mathcal{N}(0,1)$；若以观测值作为临界值，得到至少同样极端的结果的概率为

$$
p=\mathbb{P}_{H_0}(\lvert\bar X\rvert\ge\lvert\bar x\rvert)=\mathbb{P}(\lvert U\rvert\ge4\lvert\bar x\rvert),
$$
对 $\bar x=0.48$ 为 $0.055$，对 $\bar x=0.12$ 为 $0.631$。

**定义 5.1.7（p 值）** 设 $T(\boldsymbol{X})$ 为检验统计量，$t(\boldsymbol{x})$ 为其观测值。在原假设下计算的、检验统计量取到至少与观测值同样极端的值的概率，称为 **p 值**；也就是以 $t(\boldsymbol{x})$ 作为临界值时拒绝域的概率：

| 检验问题 | 拒绝域 | $p$ 值 |
|---|---|---|
| $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta\ne\theta_0$ | $\lvert T\rvert>c$ | $\mathbb{P}_{\theta_0}(\lvert T(\boldsymbol{X})\rvert\ge\lvert t(\boldsymbol{x})\rvert)$ |
| $H_0\colon\theta\le\theta_0$ vs. $H_1\colon\theta>\theta_0$ | $T>c$ | $\mathbb{P}_{\theta_0}(T(\boldsymbol{X})\ge t(\boldsymbol{x}))$ |
| $H_0\colon\theta\ge\theta_0$ vs. $H_1\colon\theta<\theta_0$ | $T<c$ | $\mathbb{P}_{\theta_0}(T(\boldsymbol{X})\le t(\boldsymbol{x}))$ |

对复合的 $H_0$，概率在边界点 $\theta_0$ 处计算，对本章的检验而言这里的概率最大。对连续型统计量，不等号是否严格无关紧要。

![双侧与单侧检验的 p 值（阴影部分），检验统计量在 H₀ 下服从标准正态分布，观测值 t(x) = 2.2；虚线为 α = 0.05 时的临界值](./plots/p-values.py)

**命题 5.1.1** 设 $T(\boldsymbol{X})$ 在 $\theta_0$ 下服从连续分布。则水平为 $\alpha$ 的检验拒绝 $H_0$ 当且仅当 $p<\alpha$；也就是说，$p$ 值是观测数据导致拒绝的最小显著性水平。实践中的决策规则是：$p\le\alpha$ 时拒绝 $H_0$。

**证明** 考虑右侧检验，其余情形相同。水平为 $\alpha$ 的检验在 $t(\boldsymbol{x})>c_\alpha$ 时拒绝，其中 $c_\alpha$ 满足 $G(c_\alpha)=\alpha$，$G(c)=\mathbb{P}_{\theta_0}(T\ge c)$ 连续且不增，而 $p=G(t(\boldsymbol{x}))$。若 $t(\boldsymbol{x})>c_\alpha$，则 $p\le\alpha$，等号只在 $G$ 于 $[c_\alpha,t(\boldsymbol{x})]$ 上为常数时成立，这是概率为零的事件；反之，$p<\alpha=G(c_\alpha)$ 迫使 $t(\boldsymbol{x})>c_\alpha$。$\square$

**注 5.1.5** $p$ 值衡量反对 $H_0$ 的证据强度：它越小，拒绝越有力（$p=0.01$ 与 $p=10^{-8}$）。它通常随拒绝结论一同报告，很小的 $p$ 值称为结果高度统计显著。$p$ 值是在假定的模型下计算的，因此只与模型同样可靠。它不是 $H_0$ 为真的概率；统计显著也不等于实际显著：样本量很大时，小到无关紧要的差异也可能有极小的 $p$ 值。

### 5.1.5. 一般步骤

1. 提出原假设 $H_0$ 与备择假设 $H_1$。
2. 选取检验统计量 $T(\boldsymbol{X})$ 和拒绝域的形式，例如 $D=\{\lvert T(\boldsymbol{X})\rvert>A\}$，$A$ 待定。
3. 选定显著性水平 $\alpha$（如 $0.05$ 或 $0.01$），由 $T(\boldsymbol{X})$ 在 $H_0$ 下的抽样分布确定临界值 $A$。
4. 计算 $T$ 的观测值，作出拒绝或接受 $H_0$ 的结论；同时报告 $p$ 值。

**例 5.1.8** 某大学男生的平均身高是否超过 $174\,\mathrm{cm}$？普查代价高且没有必要，我们抽取 $15$ 名男生：

$$
174,\ 171,\ 175,\ 174,\ 176,\ 177,\ 175,\ 171,\ 178,\ 177,\ 175,\ 179,\ 176,\ 174,\ 177.
$$
假定身高服从 $\mathcal{N}(\mu,\sigma^2)$，在 $\alpha=0.05$ 下检验 $H_0\colon\mu=174$ vs. $H_1\colon\mu>174$。这里 $\bar x=175.27$，$s^2=5.21$，$s=2.28$。检验统计量与拒绝域为

$$
T(\boldsymbol{X})=\frac{\sqrt{n}(\bar X-174)}{S}\overset{H_0}{\sim}t_{n-1},\qquad D=\{T(\boldsymbol{X})>A\},
$$
由 $\mathbb{P}_{H_0}(T>A)=0.05$ 得 $A=t_{14,0.05}=1.761$。观测值 $t(\boldsymbol{x})=\sqrt{15}(175.27-174)/2.28=2.15>1.761$，故拒绝 $H_0$；$p$ 值为 $\mathbb{P}(t_{14}\ge2.15)=0.025<0.05$。数据支持平均身高超过 $174\,\mathrm{cm}$ 的结论。

## 5.2. 各种总体参数的检验

本节推导单个与两个正态总体、两点分布与 Poisson 总体参数的标准检验，以及基于**中心极限定理**的大样本检验。下文中 $\Phi$ 是 $\mathcal{N}(0,1)$ 的分布函数，$z_\alpha$、$t_{n,\alpha}$、$\chi^2_{n,\alpha}$、$F_{m,n,\alpha}$ 分别是 $\mathcal{N}(0,1)$、$t_n$、$\chi^2_n$、$F_{m,n}$ 的上 $\alpha$ 分位数。

### 5.2.1. 正态总体均值的检验

设 $\boldsymbol{X}=(X_1,\dots,X_n)$ 是来自 $\mathcal{N}(\mu,\sigma^2)$ 的样本，对给定的 $\mu_0$ 和水平 $\alpha$ 考虑

$$
\text{(1) } H_0\colon\mu=\mu_0 \text{ vs. } H_1\colon\mu\ne\mu_0;\quad
\text{(2) } H_0\colon\mu\le\mu_0 \text{ vs. } H_1\colon\mu>\mu_0;\quad
\text{(3) } H_0\colon\mu\ge\mu_0 \text{ vs. } H_1\colon\mu<\mu_0.
$$

**定义 5.2.1（单侧检验与双侧检验）** 像 (1) 这样备择假设位于原假设取值两侧的问题称为**双侧检验**；像 (2)、(3) 这样的问题称为**单侧检验**。

先设 $\sigma^2$ 已知，考虑问题 (1)。$\bar X$ 是 $\mu$ 的估计，$\lvert\bar X-\mu_0\rvert$ 较大时 $H_0$ 可疑，因此取 $D=\{\lvert\bar X-\mu_0\rvert>A\}$。在 $H_0$ 下 $\bar X\sim\mathcal{N}(\mu_0,\sigma^2/n)$，故

$$
Z=\frac{\sqrt{n}(\bar X-\mu_0)}{\sigma}\overset{H_0}{\sim}\mathcal{N}(0,1).
$$
以 $Z$ 为检验统计量、$\{\lvert Z\rvert>c\}$ 为拒绝域，条件 $\mathbb{P}_{H_0}(\lvert Z\rvert>c)=\alpha$ 给出 $c=z_{\alpha/2}$：

$$
D_1=\left\{\boldsymbol{X}\colon\left\lvert\frac{\sqrt{n}(\bar X-\mu_0)}{\sigma}\right\rvert>z_{\alpha/2}\right\}.
$$
把 $\bar X-\mu_0$ 写成 $(\bar X-\mu)+(\mu-\mu_0)$，其中在 $\mathbb{P}_\mu$ 下 $\sqrt{n}(\bar X-\mu)/\sigma\sim\mathcal{N}(0,1)$，即得功效函数

$$
\pi_1(\mu)=1-\Phi\left(z_{\alpha/2}+\frac{\sqrt{n}(\mu_0-\mu)}{\sigma}\right)+\Phi\left(-z_{\alpha/2}+\frac{\sqrt{n}(\mu_0-\mu)}{\sigma}\right).\tag{5.2}
$$

**命题 5.2.1** 功效函数 (5.2) 满足 $\pi_1(\mu_0)=\alpha$ 与 $\pi_1(\mu)=\pi_1(2\mu_0-\mu)$，且在 $\mu\ge\mu_0$ 时严格递增。对每个 $\mu\ne\mu_0$，$\pi_1(\mu)$ 随 $n$ 增大而增大、随 $\sigma$ 增大而减小，且 $n\to\infty$ 时 $\pi_1(\mu)\to1$。

**证明** 令 $d=\sqrt{n}(\mu-\mu_0)/\sigma$，(5.2) 化为 $g(d)=1-\Phi(z_{\alpha/2}-d)+\Phi(-z_{\alpha/2}-d)$；由 $\Phi(-x)=1-\Phi(x)$，它是 $d$ 的偶函数，这就是对称性。其导数 $g'(d)=\phi(z_{\alpha/2}-d)-\phi(z_{\alpha/2}+d)$（$\phi$ 为标准正态密度）在 $d>0$ 时为正，因为 $\lvert z_{\alpha/2}-d\rvert<z_{\alpha/2}+d$。因此 $\pi_1$ 随 $\lvert d\rvert$ 增大而增大，而 $\lvert d\rvert$ 随 $n$ 与 $\lvert\mu-\mu_0\rvert$ 增大而增大、随 $\sigma$ 增大而减小；又 $\lvert d\rvert\to\infty$ 时 $g(d)\to1$。$\square$

对问题 (2)，仍设 $\sigma^2$ 已知，我们同样用 $Z$，在 $Z>c$ 时拒绝。条件 $\mathbb{P}_{\mu_0}(Z>c)=\alpha$ 给出 $c=z_\alpha$，拒绝域

$$
D_2=\left\{\boldsymbol{X}\colon\frac{\sqrt{n}(\bar X-\mu_0)}{\sigma}>z_\alpha\right\}
$$
对简单原假设 $H_0^*\colon\mu=\mu_0$ 的水平为 $\alpha$。对复合原假设 $\mu\le\mu_0$，还必须验证 $\mu<\mu_0$ 时犯第一类错误的概率不超过 $\alpha$。

**命题 5.2.2** $D_2$ 的功效函数为 $\pi_2(\mu)=1-\Phi\big(z_\alpha+\sqrt{n}(\mu_0-\mu)/\sigma\big)$。它关于 $\mu$ 严格递增，因此对一切 $\mu\le\mu_0$ 有 $\pi_2(\mu)\le\pi_2(\mu_0)=\alpha$，$D_2$ 是问题 (2) 的水平 $\alpha$ 的拒绝域。同理，$D_3=\{\sqrt{n}(\bar X-\mu_0)/\sigma<-z_\alpha\}$ 是问题 (3) 的水平 $\alpha$ 的拒绝域。

**证明** $\pi_2(\mu)=\mathbb{P}_\mu\big(\sqrt{n}(\bar X-\mu)/\sigma>z_\alpha+\sqrt{n}(\mu_0-\mu)/\sigma\big)$，而在 $\mathbb{P}_\mu$ 下 $\sqrt{n}(\bar X-\mu)/\sigma\sim\mathcal{N}(0,1)$。$\Phi$ 的自变量关于 $\mu$ 递减。问题 (3) 是对称的。$\square$

基于在 $H_0$ 下服从 $\mathcal{N}(0,1)$ 的统计量的检验称为 Z 检验（Z-test），中文教材常称 $U$ 检验；上面的检验是单样本 Z 检验。

![正态均值 Z 检验的功效函数，μ₀ = 1，σ² = 4，α = 0.05。左：三种样本量下的双侧检验，曲线关于 μ₀ 对称，n 越大越陡。右：检验 μ = μ₀ 对 μ ≠ μ₀ 时，单侧拒绝域 D₂ 在 μ₀ 左侧的功效低于 α](./plots/power-functions.py)

当 $\sigma^2$ 未知时，用样本方差 $S^2=\sum_{i=1}^n(X_i-\bar X)^2/(n-1)$ 估计 $\sigma^2$，并采用

$$
T=\frac{\sqrt{n}(\bar X-\mu_0)}{S}\overset{H_0}{\sim}t_{n-1}.
$$
同样的论证给出问题 (1)、(2)、(3) 的拒绝域

$$
D_1'=\{\lvert T\rvert>t_{n-1,\alpha/2}\},\qquad D_2'=\{T>t_{n-1,\alpha}\},\qquad D_3'=\{T<-t_{n-1,\alpha}\}.
$$
基于 $t$ 统计量的检验（W. S. Gosset，1908）称为 t 检验（t-test）；这里的是单样本 $t$ 检验。它的功效函数，如 $\pi_1'(\mu)=\mathbb{P}_\mu(\lvert T\rvert>t_{n-1,\alpha/2})$，没有简单的闭式：在 $\mathbb{P}_\mu$ 下 $T$ 服从自由度为 $n-1$、非中心参数为 $\delta=\sqrt{n}(\mu-\mu_0)/\sigma$ 的非中心 $t$ 分布，因此功效依赖于未知的 $\sigma$。它可以数值计算，或用 Monte Carlo 模拟近似。

| | $H_0$ | $H_1$ | 检验统计量 | 拒绝域 |
|---|---|---|---|---|
| $\sigma^2$ 已知 | $\mu=\mu_0$ | $\mu\ne\mu_0$ | $Z=\sqrt{n}(\bar X-\mu_0)/\sigma$ | $\lvert Z\rvert>z_{\alpha/2}$ |
| | $\mu\le\mu_0$ | $\mu>\mu_0$ | $Z\overset{\mu=\mu_0}{\sim}\mathcal{N}(0,1)$ | $Z>z_\alpha$ |
| | $\mu\ge\mu_0$ | $\mu<\mu_0$ | | $Z<-z_\alpha$ |
| $\sigma^2$ 未知 | $\mu=\mu_0$ | $\mu\ne\mu_0$ | $T=\sqrt{n}(\bar X-\mu_0)/S$ | $\lvert T\rvert>t_{n-1,\alpha/2}$ |
| | $\mu\le\mu_0$ | $\mu>\mu_0$ | $T\overset{\mu=\mu_0}{\sim}t_{n-1}$ | $T>t_{n-1,\alpha}$ |
| | $\mu\ge\mu_0$ | $\mu<\mu_0$ | | $T<-t_{n-1,\alpha}$ |

**注 5.2.1** $\sigma^2$ 已知时，$D_1$ 与 $t$ 检验的拒绝域 $D_1'$ 对问题 (1) 的水平都是 $\alpha$。Z 检验的功效略高，因为它用已知的 $\sigma$ 代替了有噪声的估计 $S$（$\mu_0=1$，$\sigma^2=4$，$n=20$ 时两条功效曲线几乎重合，$t$ 检验略低）。随着 $n$ 增大，差别消失。

**注 5.2.2** 用单侧还是双侧拒绝域？对问题 (1)，单侧拒绝域 $D_2$ 在 $\mu_0$ 处的水平也是 $\alpha$，但在 $\mu<\mu_0$ 时功效低于 $\alpha$ 并趋于 $0$：它无法发现向左的偏离（图的右栏）。对问题 (2)，以及对 $H_0\colon\mu=\mu_0$ vs. $H_1\colon\mu>\mu_0$，$D$ 与 $D_2$ 的水平都是 $\alpha$，但 $D_2$ 在每个 $\mu>\mu_0$ 处功效都更大，因此单侧拒绝域更好。拒绝域的形状应当与备择假设一致。5.4 节将把"更好"精确化。

**例 5.2.1** 一台自动装罐机装罐头，每罐标准重量为 $500\,\mathrm{g}$。抽取 $10$ 罐，测得重量（单位：g）为 $495, 510, 505, 498, 503, 492, 502, 512, 497, 506$。设罐头重量服从 $\mathcal{N}(\mu,\sigma^2)$，$\sigma=6.5$。在 $\alpha=0.05$ 下机器工作是否正常？用 $D_1$ 检验 $H_0\colon\mu=500$ vs. $H_1\colon\mu\ne500$，$z_{0.025}=1.96$。由于 $\bar x=502$，

$$
\lvert z\rvert=\left\lvert\frac{\sqrt{10}(502-500)}{6.5}\right\rvert=0.973<1.96,
$$
没有足够的证据拒绝 $H_0$；$p$ 值为 $\mathbb{P}(\lvert Z\rvert\ge0.973)=0.331$。由 (5.2)，$\mu=505$ 处的功效为

$$
\pi(505)=1-\Phi\left(1.96+\frac{\sqrt{10}(500-505)}{6.5}\right)+\Phi\left(-1.96+\frac{\sqrt{10}(500-505)}{6.5}\right)=0.682,
$$
而 $\pi(510)=0.998$：偏离 $10\,\mathrm{g}$ 几乎必然被发现，偏离 $5\,\mathrm{g}$ 只有约 $2/3$ 的概率被发现。

**例 5.2.2** 某厂地砖的抗断强度服从 $\mathcal{N}(\mu,\sigma^2)$。随机抽取 $6$ 块，测得抗断强度（单位：$\mathrm{kg/cm^2}$）为 $32.56, 29.66, 31.64, 30.00, 31.87, 31.03$。能否认为平均抗断强度不低于 $32.50$（$\alpha=0.05$）？用单样本 $t$ 检验检验 $H_0\colon\mu\ge32.50$ vs. $H_1\colon\mu<32.50$，$D=\{T<-t_{5,0.05}\}$，$t_{5,0.05}=2.015$。这里 $\bar x=31.13$，$s=1.123$，故

$$
t=\frac{\sqrt{6}(31.13-32.50)}{1.123}=-2.99<-2.015,
$$
拒绝 $H_0$：平均抗断强度低于 $32.50$。$p$ 值为 $\mathbb{P}(t_5\le-2.99)=0.015$。$\mu=31$ 处的功效依赖于 $\sigma$，因为

$$
\frac{\sqrt{n}(\bar X-\mu_0)}{S}=\frac{\sqrt{n}(\bar X-31)}{S}+\frac{\sqrt{n}(31-\mu_0)}{S},
$$
在 $\mu=31$ 下第一项的分布与 $\sigma$ 无关，第二项则不然。若 $\sigma=1.123$，由非中心 $t$ 分布得 $\pi(31)=0.875$。

### 5.2.2. 正态总体方差的检验

对来自 $\mathcal{N}(\mu,\sigma^2)$ 的样本考虑

$$
\text{(4) } H_0\colon\sigma^2=\sigma_0^2 \text{ vs. } H_1\colon\sigma^2\ne\sigma_0^2;\quad
\text{(5) } H_0\colon\sigma^2\le\sigma_0^2 \text{ vs. } H_1\colon\sigma^2>\sigma_0^2;\quad
\text{(6) } H_0\colon\sigma^2\ge\sigma_0^2 \text{ vs. } H_1\colon\sigma^2<\sigma_0^2.
$$

先设 $\mu$ 未知。此时 $S^2$ 是 $\sigma^2$ 的估计，$S^2/\sigma_0^2$ 过小或过大时 (4) 中的 $H_0$ 可疑。在 $\sigma^2=\sigma_0^2$ 下

$$
\chi^2=\frac{(n-1)S^2}{\sigma_0^2}\sim\chi^2_{n-1},
$$
于是对拒绝域 $\{\chi^2<c_1\text{ 或 }\chi^2>c_2\}$ 可取等尾的 $c_1=\chi^2_{n-1,1-\alpha/2}$，$c_2=\chi^2_{n-1,\alpha/2}$。对 (5) 与 (6)，拒绝域为 $\{\chi^2>\chi^2_{n-1,\alpha}\}$ 与 $\{\chi^2<\chi^2_{n-1,1-\alpha}\}$；与命题 5.2.2 一样，它们的功效函数关于 $\sigma^2$ 单调。

当 $\mu$ 已知时，$S_\mu^2=\sum_{i=1}^n(X_i-\mu)^2/n$ 是 $\sigma^2$ 的估计，且

$$
\chi^2_\mu=\frac{nS_\mu^2}{\sigma_0^2}=\sum_{i=1}^n\left(\frac{X_i-\mu}{\sigma_0}\right)^2\overset{\sigma^2=\sigma_0^2}{\sim}\chi^2_n;
$$
拒绝域形式相同，只是自由度由 $n-1$ 换成 $n$。

| | $H_0$ | $H_1$ | 检验统计量 | 拒绝域 |
|---|---|---|---|---|
| $\mu$ 已知 | $\sigma^2=\sigma_0^2$ | $\sigma^2\ne\sigma_0^2$ | $\chi^2_\mu=nS_\mu^2/\sigma_0^2$ | $\chi^2_\mu<\chi^2_{n,1-\alpha/2}$ 或 $\chi^2_\mu>\chi^2_{n,\alpha/2}$ |
| | $\sigma^2\le\sigma_0^2$ | $\sigma^2>\sigma_0^2$ | $\chi^2_\mu\overset{\sigma^2=\sigma_0^2}{\sim}\chi^2_n$ | $\chi^2_\mu>\chi^2_{n,\alpha}$ |
| | $\sigma^2\ge\sigma_0^2$ | $\sigma^2<\sigma_0^2$ | | $\chi^2_\mu<\chi^2_{n,1-\alpha}$ |
| $\mu$ 未知 | $\sigma^2=\sigma_0^2$ | $\sigma^2\ne\sigma_0^2$ | $\chi^2=(n-1)S^2/\sigma_0^2$ | $\chi^2<\chi^2_{n-1,1-\alpha/2}$ 或 $\chi^2>\chi^2_{n-1,\alpha/2}$ |
| | $\sigma^2\le\sigma_0^2$ | $\sigma^2>\sigma_0^2$ | $\chi^2\overset{\sigma^2=\sigma_0^2}{\sim}\chi^2_{n-1}$ | $\chi^2>\chi^2_{n-1,\alpha}$ |
| | $\sigma^2\ge\sigma_0^2$ | $\sigma^2<\sigma_0^2$ | | $\chi^2<\chi^2_{n-1,1-\alpha}$ |

基于 $\chi^2$ 分布的检验称为 $\chi^2$ 检验。

**注 5.2.3** $\mu$ 已知时，基于 $S^2$ 与 $\chi^2_{n-1}$ 的检验仍然是合法的水平 $\alpha$ 的检验，但它浪费了"$\mu$ 已知"这一信息：用 $\bar X$ 估计 $\mu$ 损失一个自由度，基于 $S_\mu^2$ 的检验功效更高。

### 5.2.3. 两点分布参数的检验

设 $\boldsymbol{X}$ 是来自 $\mathrm{Ber}(\theta)$ 的样本，$T(\boldsymbol{X})=\sum_{i=1}^nX_i\sim\mathrm{Bin}(n,\theta)$。先考虑 $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta>\theta_0$。由于 $\bar X=T/n$ 是 $\theta$ 的估计，$T$ 大时拒绝；在 $H_0$ 下 $T\sim\mathrm{Bin}(n,\theta_0)$。$T$ 是离散的，一般不存在恰好使 $\mathbb{P}_{\theta_0}(T>c)=\alpha$ 的 $c$，因此采用随机化检验

$$
\varphi(\boldsymbol{X})=\begin{cases}1, & T>c,\\ r, & T=c,\\ 0, & T<c,\end{cases}\qquad
\mathbb{E}_{\theta_0}\varphi(\boldsymbol{X})=\mathbb{P}_{\theta_0}(T>c)+r\,\mathbb{P}_{\theta_0}(T=c)=\alpha,\tag{5.3}
$$
其中 $0\le r\le1$：$c$ 是满足 $\mathbb{P}_{\theta_0}(T>c)\le\alpha<\mathbb{P}_{\theta_0}(T\ge c)$ 的整数，然后 $r=\big(\alpha-\mathbb{P}_{\theta_0}(T>c)\big)/\mathbb{P}_{\theta_0}(T=c)$。功效函数 $\pi(\theta)=\mathbb{P}_\theta(T>c)+r\,\mathbb{P}_\theta(T=c)$ 关于 $\theta$ 递增（二项分布族关于 $\theta$ 随机递增），于是 $\theta\le\theta_0$ 时 $\pi(\theta)\le\pi(\theta_0)=\alpha$，(5.3) 也是 $H_0\colon\theta\le\theta_0$ vs. $H_1\colon\theta>\theta_0$ 的水平 $\alpha$ 的检验。

**例 5.2.3** 在例 5.1.1 中，$n=100$，$\theta_0=0.01$，$\alpha=0.05$，在 $H_0$ 下 $T\sim\mathrm{Bin}(100,0.01)$。这时 $\mathbb{P}_{\theta_0}(T>3)=0.0184\le0.05<\mathbb{P}_{\theta_0}(T\ge3)$，故

$$
c=3,\qquad r=\frac{0.05-0.01837}{0.06100}=0.518.
$$
观测值 $T=3$ 恰好落在边界上：检验以概率 $0.518$ 拒绝 $H_0$（拒绝进货）。

对 $H_0\colon\theta\ge\theta_0$ vs. $H_1\colon\theta<\theta_0$，检验在 $T$ 小时拒绝：$T<c$ 时 $\varphi=1$，$T=c$ 时为 $r$，$T>c$ 时为 $0$，其中 $\mathbb{P}_{\theta_0}(T<c)+r\,\mathbb{P}_{\theta_0}(T=c)=\alpha$。对双侧问题，

$$
\varphi(\boldsymbol{X})=\begin{cases}1, & T<c_1\text{ 或 }T>c_2,\\ r_i, & T=c_i\ (i=1,2),\\ 0, & c_1<T<c_2,\end{cases}
$$
其中 $\mathbb{P}_{\theta_0}(T<c_1)+r_1\mathbb{P}_{\theta_0}(T=c_1)=\alpha/2$，$\mathbb{P}_{\theta_0}(T>c_2)+r_2\mathbb{P}_{\theta_0}(T=c_2)=\alpha/2$。

**例 5.2.4** 在例 5.1.2 中，设 $n=500$ 人中有 $20$ 人失业，在 $\alpha=0.05$ 下检验 $H_0\colon\theta\ge0.0625$ vs. $H_1\colon\theta<0.0625$。左侧随机化检验的 $c=23$，$r=0.099$；由于 $T=20<23$，拒绝 $H_0$：失业率显著低于 $6.25\%$。

**注 5.2.4** 同样的论证适用于 Poisson 总体 $\mathrm{Poi}(\theta)$，此时 $T=\sum X_i\sim\mathrm{Poi}(n\theta)$。

### 5.2.4. 两个正态总体均值的比较

设 $\boldsymbol{X}=(X_1,\dots,X_m)$ 是来自 $\mathcal{N}(\mu_1,\sigma_1^2)$ 的样本，$\boldsymbol{Y}=(Y_1,\dots,Y_n)$ 是来自 $\mathcal{N}(\mu_2,\sigma_2^2)$ 的样本，两者相互独立。典型的问题有：新疗法是否优于标准疗法（例 5.1.5）？教授与助理教授、男性与女性的工资是否有显著差异？考虑

$$
\text{(7) } \mu_1-\mu_2=\mu_0 \text{ vs. } \mu_1-\mu_2\ne\mu_0;\quad
\text{(8) } \mu_1-\mu_2\le\mu_0 \text{ vs. } \mu_1-\mu_2>\mu_0;\quad
\text{(9) } \mu_1-\mu_2\ge\mu_0 \text{ vs. } \mu_1-\mu_2<\mu_0,
$$
分以下情形：(a) $\sigma_1^2,\sigma_2^2$ 已知；(b) $\sigma_1^2=\sigma_2^2=\sigma^2$ 未知；(c) $\sigma_1^2,\sigma_2^2$ 未知且可能不等；(d) $m=n$ 且样本成对，$X_i$ 与 $Y_i$ 可能相关。

情形 (a) 中，$\bar X-\bar Y$ 是 $\mu_1-\mu_2$ 的估计，在 $\mu_1-\mu_2=\mu_0$ 下

$$
U=\frac{\bar X-\bar Y-\mu_0}{\sqrt{\sigma_1^2/m+\sigma_2^2/n}}\sim\mathcal{N}(0,1).
$$
与 5.2.1 节一样，(7)、(8)、(9) 的拒绝域为 $\{\lvert U\rvert>z_{\alpha/2}\}$、$\{U>z_\alpha\}$、$\{U<-z_\alpha\}$（两样本 Z 检验）。

情形 (b) 中，用合并方差 $S_p^2=\big((m-1)S_X^2+(n-1)S_Y^2\big)/(m+n-2)$，

$$
T=\frac{\bar X-\bar Y-\mu_0}{S_p\sqrt{1/m+1/n}}\overset{\mu_1-\mu_2=\mu_0}{\sim}t_{m+n-2},
$$
拒绝域为 $\{\lvert T\rvert>t_{m+n-2,\alpha/2}\}$、$\{T>t_{m+n-2,\alpha}\}$、$\{T<-t_{m+n-2,\alpha}\}$（两样本 $t$ 检验）。

**例 5.2.5** 为比较正常成年男女红细胞数的差别，检查了某地正常成年男子 $156$ 人、女子 $74$ 人，样本均值与标准差（单位：$10^4/\mathrm{mm^3}$）为

$$
\bar x=465.13,\ s_X=54.80\ \text{（男）};\qquad \bar y=422.16,\ s_Y=49.20\ \text{（女）}.
$$
设两总体为方差相同的正态分布，红细胞数是否与性别有关（$\alpha=0.01$）？检验 $\mu_1-\mu_2=0$ vs. $\mu_1-\mu_2\ne0$。这里 $t_{228,0.005}=2.598$，而

$$
\lvert t\rvert=\frac{\lvert\bar x-\bar y\rvert}{s_p\sqrt{1/156+1/74}}=5.74>2.598,
$$
故拒绝 $H_0$；$p$ 值为 $\mathbb{P}(\lvert t_{228}\rvert\ge5.74)=3\times10^{-8}$。

情形 (c) 是 Behrens–Fisher 问题，它没有上述那种精确解。当 $m,n$ 不大时，B. L. Welch（1938）提出统计量

$$
T_*=\frac{\bar X-\bar Y-\mu_0}{\sqrt{S_X^2/m+S_Y^2/n}},
$$
它不服从 $t$ 分布，但在 $\mu_1-\mu_2=\mu_0$ 下的分布可以很好地用 $t_r$ 近似，其中 $r$ 取最接近

$$
\left(\frac{S_X^2}{m}+\frac{S_Y^2}{n}\right)^2\Bigg/\left[\frac{S_X^4}{m^2(m-1)}+\frac{S_Y^4}{n^2(n-1)}\right]
$$
的整数。拒绝域 $\{\lvert T_*\rvert>t_{r,\alpha/2}\}$、$\{T_*>t_{r,\alpha}\}$、$\{T_*<-t_{r,\alpha}\}$ 的水平近似为 $\alpha$；这就是 Welch t 检验（Welch's t-test）；统计软件直接使用非整数的 $r$。当 $m,n$ 都很大时，也可以改用 5.2.6 节的正态近似。

情形 (d) 出现在例如下面的研究中。为考察一种安眠药的效果，记录 $n$ 个失眠患者服药前的每晚睡眠时间 $X_i$ 与服药后的每晚睡眠时间 $Y_i$。这样的成对数据违背上面的假定：$X_i$ 与 $Y_i$ 相关（同一患者），$X_i$ 之间也不同分布（不同患者）。补救办法称为成对比较（paired comparison）：改用差值 $Z_i=Y_i-X_i$（它必须有实际意义，这里是安眠药对第 $i$ 个患者的效果），平均效果为 $\mu=\mathbb{E}Z_i$，并假定 $Z_1,\dots,Z_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$。于是检验 $H_0\colon\mu=0$ vs. $H_1\colon\mu\ne0$ 就是单样本 $t$ 检验，拒绝域为 $\{\lvert\sqrt{n}\,\bar Z/S_Z\rvert>t_{n-1,\alpha/2}\}$，其中 $\bar Z$、$S_Z^2$ 是差值的样本均值与样本方差。

**例 5.2.6** 用两台光谱仪 $A$ 与 $B$ 测量 $9$ 件金属含量不同的材料样品中某种金属的含量（单位：$\%$）：

| 样品 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| $A$ | 0.20 | 0.30 | 0.40 | 0.50 | 0.60 | 0.70 | 0.80 | 0.90 | 1.00 |
| $B$ | 0.10 | 0.21 | 0.52 | 0.32 | 0.78 | 0.59 | 0.68 | 0.77 | 0.89 |

在 $\alpha=0.01$ 下两台仪器的质量有无显著差异？不同样品的测量值不同分布，而 $X_i$、$Y_i$ 测的是同一样品，因此使用 $Z_i=X_i-Y_i$；若两台仪器同样好，则 $Z_i\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$。这里 $\bar z=0.06$，$s_Z^2=0.01505$，$s_Z=0.1227$，$t_{8,0.005}=3.355$，而

$$
\frac{\sqrt{9}\,\lvert\bar z\rvert}{s_Z}=\frac{3\times0.06}{0.1227}=1.47<3.355.
$$
数据没有提供足够的证据表明两者有差异；$p$ 值为 $0.18$。

### 5.2.5. 两个正态总体方差的比较

对同样的两个独立样本考虑

$$
\text{(10) } \frac{\sigma_2^2}{\sigma_1^2}=1 \text{ vs. } \frac{\sigma_2^2}{\sigma_1^2}\ne1;\quad
\text{(11) } \frac{\sigma_2^2}{\sigma_1^2}\le1 \text{ vs. } \frac{\sigma_2^2}{\sigma_1^2}>1;\quad
\text{(12) } \frac{\sigma_2^2}{\sigma_1^2}\ge1 \text{ vs. } \frac{\sigma_2^2}{\sigma_1^2}<1.
$$
若均值未知，$S_X^2$ 与 $S_Y^2$ 分别是 $\sigma_1^2$ 与 $\sigma_2^2$ 的无偏估计，$S_Y^2/S_X^2$ 过小或过大时 (10) 中的 $H_0$ 可疑。在 $\sigma_1^2=\sigma_2^2$ 下

$$
F=\frac{S_Y^2}{S_X^2}\sim F_{n-1,m-1},
$$
拒绝域为 $\{F<F_{n-1,m-1,1-\alpha/2}\text{ 或 }F>F_{n-1,m-1,\alpha/2}\}$、$\{F>F_{n-1,m-1,\alpha}\}$ 与 $\{F<F_{n-1,m-1,1-\alpha}\}$。若均值已知，则令 $S_{X*}^2=\sum_{i=1}^m(X_i-\mu_1)^2/m$，$S_{Y*}^2=\sum_{j=1}^n(Y_j-\mu_2)^2/n$，在 $H_0$ 下统计量 $F_*=S_{Y*}^2/S_{X*}^2\sim F_{n,m}$，自由度变为 $n,m$。基于 $F$ 分布的检验称为 F 检验（F-test）。

**例 5.2.7** 两批各 $6$ 个电子元件的电阻均值为 $\bar x=0.140$、$\bar y=0.139$，样本标准差为 $s_X=0.0026$、$s_Y=0.0024$。设电阻分别服从 $\mathcal{N}(\mu_1,\sigma_1^2)$ 与 $\mathcal{N}(\mu_2,\sigma_2^2)$，参数均未知，两组样本独立。两批元件的平均电阻是否相同（$\alpha=0.05$）？由于不知道 $\sigma_1^2=\sigma_2^2$ 是否成立，先用 $F$ 检验检验 $\sigma_2^2=\sigma_1^2$：$s_Y^2/s_X^2=0.0024^2/0.0026^2=0.85$，而 $F_{5,5,0.975}=0.14<0.85<F_{5,5,0.025}=7.15$，因此不拒绝方差相等。再用两样本 $t$ 检验检验 $\mu_1=\mu_2$：$\lvert t\rvert=0.693<t_{10,0.025}=2.228$，没有足够的证据表明平均电阻不同。

**例 5.2.8** 对美国 $397$ 位教授 2008–09 学年的工资（R 的 `Salaries` 数据），两步法给出：

| 比较 | $m$ | $n$ | $\bar x$ | $\bar y$ | $s_X$ | $s_Y$ | $F$ 检验 | 均值检验 |
|---|---|---|---|---|---|---|---|---|
| 教授 vs. 助理教授 | 266 | 67 | 126772 | 80776 | 27719 | 8174 | $F=11.50$，$p<10^{-15}$ | Welch：$t=23.33$，$r=324.3$，$p<10^{-15}$ |
| 男性 vs. 女性 | 358 | 39 | 115090 | 101002 | 30437 | 25922 | $F=1.38$，$p=0.23$ | 合并方差：$t=2.78$，$p=0.0057$ |

第一组的方差相差悬殊，因此用 Welch 检验；第二组的方差没有显著差异，因此用合并方差的 $t$ 检验。两组均值差异在 $\alpha=0.01$ 下都显著。

### 5.2.6. 大样本检验

设 $X_1,\dots,X_n\overset{\text{iid}}{\sim}F$，均值为 $\mu$，方差 $\sigma^2\in(0,\infty)$。若 $F$ 是正态分布，则 $\sqrt{n}(\bar X_n-\mu)/\sigma\sim\mathcal{N}(0,1)$，$\sqrt{n}(\bar X_n-\mu)/S\sim t_{n-1}$。否则这些精确分布未知，但由**中心极限定理**、**大数定律**（$S\to\sigma$ 几乎必然成立）与 Slutsky 定理，

$$
\frac{\sqrt{n}(\bar X_n-\mu)}{\sigma}\xrightarrow{d}\mathcal{N}(0,1),\qquad \frac{\sqrt{n}(\bar X_n-\mu)}{S}\xrightarrow{d}\mathcal{N}(0,1).
$$
把精确的分位数换成 $z_\alpha$，就得到 $n$ 较大时水平近似为 $\alpha$ 的检验。

**命题 5.2.3** 在两样本情形下，$\sigma_1^2,\sigma_2^2$ 未知，在 $\mu_1-\mu_2=\mu_0$ 下

$$
U^*=\frac{\bar X-\bar Y-\mu_0}{\sqrt{S_X^2/m+S_Y^2/n}}\xrightarrow{d}\mathcal{N}(0,1)\qquad(m,n\to\infty),
$$
无论总体是否为正态，只要方差有限且为正。因此 $\{\lvert U^*\rvert>z_{\alpha/2}\}$、$\{U^*>z_\alpha\}$、$\{U^*<-z_\alpha\}$ 是 (7)、(8)、(9) 的水平近似为 $\alpha$ 的拒绝域。

**证明** 写

$$
U^*=\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{\sqrt{\sigma_1^2/m+\sigma_2^2/n}}\cdot\sqrt{\frac{\sigma_1^2/m+\sigma_2^2/n}{S_X^2/m+S_Y^2/n}}.
$$
对正态总体，第一个因子恰好服从 $\mathcal{N}(0,1)$；一般情形下由中心极限定理它依分布收敛于 $\mathcal{N}(0,1)$。由于 $S_X^2\to\sigma_1^2$、$S_Y^2\to\sigma_2^2$ 几乎必然成立，比值 $\big(\sigma_1^2/m+\sigma_2^2/n\big)/\big(S_X^2/m+S_Y^2/n\big)$ 介于 $\min(\sigma_1^2/S_X^2,\sigma_2^2/S_Y^2)$ 与 $\max(\sigma_1^2/S_X^2,\sigma_2^2/S_Y^2)$ 之间，因此第二个因子趋于 $1$。由 Slutsky 定理即得结论。$\square$

**例 5.2.9** 在例 5.2.5 中去掉方差相等的假定。$z_{0.005}=2.576$，

$$
\lvert u^*\rvert=\frac{\lvert422.16-465.13\rvert}{\sqrt{54.80^2/156+49.20^2/74}}=5.96>2.576,
$$
仍然拒绝 $H_0$；$p$ 值为 $\mathbb{P}(\lvert\mathcal{N}(0,1)\rvert\ge5.96)=2.5\times10^{-9}$。

同样的思路适用于两点分布与 Poisson 分布的均值。对来自 $\mathrm{Ber}(\theta)$ 的样本，$\sqrt{n}(\bar X-\theta)/\sqrt{\theta(1-\theta)}\xrightarrow{d}\mathcal{N}(0,1)$，故在 $H_0\colon\theta=\theta_0$ 下

$$
U=\frac{\sqrt{n}(\bar X-\theta_0)}{\sqrt{\theta_0(1-\theta_0)}}\xrightarrow{d}\mathcal{N}(0,1),
$$
$\{\lvert U\rvert>z_{\alpha/2}\}$、$\{U>z_\alpha\}$（对 $\theta\le\theta_0$ vs. $\theta>\theta_0$）与 $\{U<-z_\alpha\}$（对 $\theta\ge\theta_0$ vs. $\theta<\theta_0$）的水平近似为 $\alpha$。对 $\mathrm{Poi}(\theta)$，统计量为 $U_0=\sqrt{n}(\bar X-\theta_0)/\sqrt{\theta_0}$，拒绝域相同。

**注 5.2.5** 大样本检验不需要正态假定。例如比较两位候选人的支持率时，可以设 $X_i\overset{\text{iid}}{\sim}\mathrm{Ber}(\theta_1)$、$Y_j\overset{\text{iid}}{\sim}\mathrm{Ber}(\theta_2)$ 并使用 $U^*$。总之，对方差未知且不等的两正态均值，$m$ 或 $n$ 较小时用 Welch 的 $t$ 近似，两者都大时用正态近似；样本小且总体非正态时，可以用 bootstrap 等重抽样方法。

## 5.3. 似然比检验

5.2 节的检验是凭直觉找到的。似然比检验由 J. Neyman 与 E. S. Pearson 于 1928 年提出，是一种一般的方法，它在检验中的地位相当于**极大似然估计**在点估计中的地位；它适用面很广，而且构造它所需的大部分工作在求极大似然估计时已经完成。

### 5.3.1. 定义

对简单问题 $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta=\theta_1$，自然的做法是在 $\theta_0$ 的似然相对于 $\theta_1$ 的似然很小时拒绝 $H_0$，即 $L(\theta_0;\boldsymbol{x})/L(\theta_1;\boldsymbol{x})<c$。对复合假设，则比较 $\Theta_0$ 内的最佳拟合与整体的最佳拟合。设 $L(\theta)=f(\boldsymbol{x};\theta)=\prod_{i=1}^nf(x_i;\theta)$ 为似然函数，$\hat\theta_{\mathrm{MLE},0}$ 与 $\hat\theta_{\mathrm{MLE}}$ 分别在 $\Theta_0$ 与 $\Theta$ 上使它达到最大：

$$
\sup_{\theta\in\Theta_0}L(\theta;\boldsymbol{x})=L(\hat\theta_{\mathrm{MLE},0}),\qquad \sup_{\theta\in\Theta}L(\theta;\boldsymbol{x})=L(\hat\theta_{\mathrm{MLE}}).
$$
若 $H_0$ 为真且 $L$ 关于 $\theta$ 连续，则随着 $n$ 增大，两个估计都趋于真值 $\theta_0\in\Theta_0$，两个最大似然值接近，其比值接近 $1$；若 $H_0$ 为假，两个估计不必接近，比值也不必接近 $1$。

**定义 5.3.1（似然比检验）** **似然比**为

$$
\lambda(\boldsymbol{x})=\frac{L(\hat\theta_{\mathrm{MLE},0})}{L(\hat\theta_{\mathrm{MLE}})}=\frac{\sup_{\theta\in\Theta_0}f(\boldsymbol{x};\theta)}{\sup_{\theta\in\Theta}f(\boldsymbol{x};\theta)}\in[0,1].
$$
相应的**似然比检验**在 $\lambda(\boldsymbol{x})<\lambda_0$ 时拒绝 $H_0$，等价地在 $-2\log\lambda(\boldsymbol{x})>C=-2\log\lambda_0$ 时拒绝：

$$
\varphi(\boldsymbol{x})=\begin{cases}1, & \lambda<\lambda_0,\\ r, & \lambda=\lambda_0,\\ 0, & \lambda>\lambda_0,\end{cases}
$$
其中对连续分布 $r=0$，对离散分布可能需要 $r\in(0,1)$。常数 $\lambda_0$（或 $C$）与 $r$ 由水平确定：对一切 $\theta\in\Theta_0$，$\mathbb{E}_\theta\varphi(\boldsymbol{X})\le\alpha$。

**注 5.3.1** 分母取 $\Theta$ 上而不是 $\Theta_1$ 上的上确界，保证了 $\lambda\le1$，并使分母就是最大似然值本身。实践中很少直接处理 $\lambda$ 的分布：要么证明 $\lambda$ 是某个熟悉的统计量的单调函数，把拒绝域改写成该统计量的形式；要么在大样本时利用 $-2\log\lambda$ 的极限分布（5.3.4 节）。

### 5.3.2. 两个例子

**例 5.3.1** 设 $X$ 是来自 Cauchy 密度 $f(x;\theta)=\dfrac{1}{\pi}\cdot\dfrac{1}{1+(x-\theta)^2}$（$\theta\in\mathbb{R}$）的一个观测值。求 $H_0\colon\theta=0$ vs. $H_1\colon\theta\ne0$ 的水平 $\alpha$ 的似然比检验。

似然 $f(x;\theta)$ 在 $\theta=x$ 处达到最大值 $1/\pi$，故

$$
\lambda=\frac{1/[\pi(1+x^2)]}{1/\pi}=\frac{1}{1+x^2},
$$
$\lambda<\lambda_0$ 当且仅当 $x^2>1/\lambda_0-1$，即 $\lvert x\rvert>C$。由 $f(x;0)$ 的对称性，$C$ 由 $\mathbb{P}_0(X>C)=\alpha/2$ 确定。作代换 $x=\tan t$，

$$
\mathbb{P}_0(X>C)=\int_C^\infty\frac{\mathrm{d}x}{\pi(1+x^2)}=\frac1\pi\left(\frac\pi2-\arctan C\right)=\frac\alpha2,
$$
所以 $C=\tan\big((1-\alpha)\pi/2\big)$。$\alpha=0.05$ 时 $C=\tan(0.475\pi)=12.706$，$\lvert x\rvert>12.706$ 时拒绝 $H_0$。

**例 5.3.2** 设 $X_1,\dots,X_n$ 是来自 $\mathrm{Exp}(\theta)$ 的样本，$f(x;\theta)=\theta\mathrm{e}^{-\theta x}$（$x>0$，$\theta>0$）。求 $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta\ne\theta_0$ 的似然比检验。

记 $t=\sum_{i=1}^nx_i$，则 $L(\theta)=\theta^n\mathrm{e}^{-\theta t}$，极大似然估计为 $\hat\theta=n/t$。于是

$$
\lambda=\frac{\theta_0^n\mathrm{e}^{-\theta_0t}}{(n/t)^n\mathrm{e}^{-n}}=\left(\frac{\mathrm{e}\theta_0}{n}\right)^nt^n\mathrm{e}^{-\theta_0t},
$$
$\lambda<\lambda_0$ 当且仅当 $g(t)=t\mathrm{e}^{-\theta_0t/n}<C_0$。函数 $g$ 在 $(0,n/\theta_0)$ 上递增、在 $(n/\theta_0,\infty)$ 上递减，在 $t=n/\theta_0$ 处取最大值，所以 $g(t)<C_0$ 当且仅当 $t<C_1$ 或 $t>C_2$，其中 $C_1<n/\theta_0<C_2$ 满足 $g(C_1)=g(C_2)=C_0$。记 $T=\sum X_i$，水平条件为 $\mathbb{P}_{\theta_0}(T<C_1)+\mathbb{P}_{\theta_0}(T>C_2)=\alpha$。在 $H_0$ 下 $T\sim\Gamma(n,\theta_0)$，即 $2\theta_0T\sim\chi^2_{2n}$。

精确的检验需要联立求解 $g(C_1)=g(C_2)$ 与水平条件。为简单起见，通常取等尾，$\mathbb{P}_{\theta_0}(T<C_1)=\mathbb{P}_{\theta_0}(T>C_2)=\alpha/2$，即 $C_1=\chi^2_{2n,1-\alpha/2}/(2\theta_0)$，$C_2=\chi^2_{2n,\alpha/2}/(2\theta_0)$；这是同水平似然比检验的一个近似。$n=2$，$\alpha=0.05$ 时，等尾方程对 $p=\theta_0C_1$、$q=\theta_0C_2$ 化为 $0.975\mathrm{e}^p-p=1$ 与 $0.025\mathrm{e}^q-q=1$，解得 $p=0.242$，$q=5.572$：$t<0.242/\theta_0$ 或 $t>5.572/\theta_0$ 时拒绝。精确的似然比检验则对应 $\theta_0C_1=0.304$，$\theta_0C_2=6.401$。

### 5.3.3. 正态总体的似然比检验

5.2 节中正态总体的检验都是似然比检验。下面记 $\omega=\Theta_0$，$\Omega=\Theta$，$\hat\omega$、$\hat\Omega$ 表示在其上的极大似然估计。

**例 5.3.3（均值，$\sigma$ 已知。）** 对 $H_0\colon\mu=\mu_0$，$\Omega=\{\mu\in\mathbb{R}\}$，

$$
L(\hat\omega)=(2\pi\sigma^2)^{-n/2}\exp\Big[-\frac{1}{2\sigma^2}\sum_{i=1}^n(x_i-\mu_0)^2\Big],\qquad L(\hat\Omega)=(2\pi\sigma^2)^{-n/2}\exp\Big[-\frac{1}{2\sigma^2}\sum_{i=1}^n(x_i-\bar x)^2\Big],
$$
故

$$
-2\log\lambda=\frac{1}{\sigma^2}\sum_{i=1}^n\big[(x_i-\mu_0)^2-(x_i-\bar x)^2\big]=\left[\frac{\sqrt{n}(\bar x-\mu_0)}{\sigma}\right]^2.
$$
于是 $-2\log\lambda>C^2$ 当且仅当 $\lvert\sqrt{n}(\bar x-\mu_0)/\sigma\rvert>C$，水平条件给出 $C=z_{\alpha/2}$：似然比检验就是双侧 Z 检验。

**例 5.3.4（均值，$\sigma$ 未知。）** 此时 $\omega=\{(\mu_0,\sigma^2)\colon\sigma^2>0\}$，$\Omega=\{(\mu,\sigma^2)\colon\mu\in\mathbb{R},\sigma^2>0\}$，$\hat\sigma_\omega^2=\frac1n\sum(x_i-\mu_0)^2$，$\hat\sigma_\Omega^2=\frac1n\sum(x_i-\bar x)^2$，两个最大似然值都形如 $(2\pi\hat\sigma^2)^{-n/2}\mathrm{e}^{-n/2}$。利用 $\sum(x_i-\mu_0)^2=\sum(x_i-\bar x)^2+n(\bar x-\mu_0)^2$，得

$$
\lambda^{2/n}=\frac{\hat\sigma_\Omega^2}{\hat\sigma_\omega^2}=\frac{\sum(x_i-\bar x)^2}{\sum(x_i-\bar x)^2+n(\bar x-\mu_0)^2}=\frac{1}{1+t^2/(n-1)},\qquad t=\frac{\sqrt{n}(\bar x-\mu_0)}{s}.
$$
由于 $\lambda$ 是 $t^2$ 的递减函数，检验在 $\lvert t\rvert>C$ 时拒绝，且 $C=t_{n-1,\alpha/2}$：双侧 $t$ 检验。

**例 5.3.5（单侧，$\sigma$ 未知。）** 对 $H_0\colon\mu\le\mu_0$，$\omega=\{(\mu,\sigma^2)\colon\mu\le\mu_0\}$，$L(\hat\Omega)$ 同前。由于

$$
L(\mu,\sigma^2)=(2\pi\sigma^2)^{-n/2}\exp\Big[-\frac{1}{2\sigma^2}\sum(x_i-\bar x)^2-\frac{n(\bar x-\mu)^2}{2\sigma^2}\Big],
$$
对每个 $\sigma^2$，似然在 $\mu\le\mu_0$ 上的最大值点为：$\bar x\le\mu_0$ 时 $\mu=\bar x$，$\bar x>\mu_0$ 时 $\mu=\mu_0$。因此

$$
\lambda=\begin{cases}1, & \bar x\le\mu_0,\\ \left(1+\dfrac{t^2}{n-1}\right)^{-n/2}, & \bar x>\mu_0,\end{cases}
$$
它是 $t$ 的不增函数。拒绝域 $\{\lambda<\lambda_0\}$ 就是 $\{t>c\}$，由 $\mathbb{P}_{\mu_0}(T>c)=\alpha$ 得 $c=t_{n-1,\alpha}$。这个检验在整个 $\omega$ 上的水平为 $\alpha$，是因为它的功效函数关于 $\mu$ 递增：在 $\mathbb{P}_{\mu,\sigma}$ 下，$T$ 服从非中心参数为 $\sqrt{n}(\mu-\mu_0)/\sigma$ 的非中心 $t$ 分布，而它关于非中心参数随机递增。

**例 5.3.6（方差，$\mu$ 已知。）** 对 $H_0\colon\sigma^2=\sigma_0^2$，$\hat\sigma_\Omega^2=\frac1n\sum(x_i-\mu)^2$，且

$$
\lambda=\left(\frac{\hat\sigma_\Omega^2}{\sigma_0^2}\right)^{n/2}\mathrm{e}^{n/2}\exp\Big[-\frac{1}{2\sigma_0^2}\sum(x_i-\mu)^2\Big]=\mathrm{e}^{n/2}u^{n/2}\mathrm{e}^{-nu/2},\qquad u=\frac1n\sum_{i=1}^n\left(\frac{x_i-\mu}{\sigma_0}\right)^2.
$$
函数 $\lambda(u)$（$u\ge0$）在 $u=0$ 处为 $0$，在 $[0,1]$ 上严格递增，在 $(1,\infty)$ 上严格递减，最大值为 $\lambda(1)=1$，且 $u\to\infty$ 时趋于 $0$。因此 $\lambda\le\lambda_0$ 当且仅当 $u\le C_1$ 或 $u\ge C_2$。在 $H_0$ 下 $nU=\sum((X_i-\mu)/\sigma_0)^2\sim\chi^2_n$，把 $\alpha$ 平分给两尾得 $nC_1=\chi^2_{n,1-\alpha/2}$，$nC_2=\chi^2_{n,\alpha/2}$：这就是 5.2.2 节的 $\chi^2$ 检验（同样采用了等尾简化）。

**例 5.3.7（方差，$\mu$ 未知。）** 此时 $\hat\mu_\omega=\hat\mu_\Omega=\bar x$，$\hat\sigma_\Omega^2=\frac1n\sum(x_i-\bar x)^2$，且

$$
\lambda=\left(\frac{\hat\sigma_\Omega^2}{\sigma_0^2}\right)^{n/2}\mathrm{e}^{n/2}\exp\Big[-\frac{1}{2\sigma_0^2}\sum(x_i-\bar x)^2\Big];
$$
对 $u=\frac1n\sum((x_i-\bar x)/\sigma_0)^2$ 作同样的论证，得到在 $\sum((x_i-\bar x)/\sigma_0)^2\le\chi^2_{n-1,1-\alpha/2}$ 或 $\ge\chi^2_{n-1,\alpha/2}$ 时拒绝。

**例 5.3.8（两个均值，方差相等且未知。）** 对来自 $\mathcal{N}(\mu_1,\sigma^2)$ 与 $\mathcal{N}(\mu_2,\sigma^2)$ 的两个独立样本，检验 $H_0\colon\mu_1=\mu_2$。在 $\Omega$ 上，$\hat\mu_1=\bar x$，$\hat\mu_2=\bar y$，$\hat\sigma_\Omega^2=\frac{1}{m+n}\big[\sum(x_i-\bar x)^2+\sum(y_j-\bar y)^2\big]$；在 $\omega=\{(\mu,\mu,\sigma^2)\}$ 上，$\hat\mu_\omega=(m\bar x+n\bar y)/(m+n)$，$\hat\sigma_\omega^2=\frac{1}{m+n}\big[\sum(x_i-\hat\mu_\omega)^2+\sum(y_j-\hat\mu_\omega)^2\big]$。两个最大似然值都形如 $(2\pi\hat\sigma^2)^{-(m+n)/2}\mathrm{e}^{-(m+n)/2}$，故 $\lambda^{2/(m+n)}=\hat\sigma_\Omega^2/\hat\sigma_\omega^2$。由于 $\sum(x_i-\hat\mu_\omega)^2=\sum(x_i-\bar x)^2+\frac{mn^2(\bar x-\bar y)^2}{(m+n)^2}$，对 $y$ 也类似，

$$
\hat\sigma_\omega^2=\hat\sigma_\Omega^2+\frac{mn(\bar x-\bar y)^2}{(m+n)^2},\qquad
\lambda^{2/(m+n)}=\left(1+\frac{t^2}{m+n-2}\right)^{-1},
$$
其中

$$
t=\sqrt{\frac{mn}{m+n}}\,(\bar x-\bar y)\Bigg/\sqrt{\frac{1}{m+n-2}\Big[\sum_{i=1}^m(x_i-\bar x)^2+\sum_{j=1}^n(y_j-\bar y)^2\Big]}
$$
是两样本 $t$ 统计量。似然比检验在 $\lvert t\rvert>t_{m+n-2,\alpha/2}$ 时拒绝。

**例 5.3.9（两个方差，均值未知。）** 对 $H_0\colon\sigma_1^2=\sigma_2^2$，记 $a=\sum(x_i-\bar x)^2$，$b=\sum(y_j-\bar y)^2$。则 $\hat\sigma_{1,\Omega}^2=a/m$，$\hat\sigma_{2,\Omega}^2=b/n$，$\hat\sigma_\omega^2=(a+b)/(m+n)$，且

$$
\lambda=\frac{(\hat\sigma_{1,\Omega}^2)^{m/2}(\hat\sigma_{2,\Omega}^2)^{n/2}}{(\hat\sigma_\omega^2)^{(m+n)/2}}=\frac{(m+n)^{(m+n)/2}}{m^{m/2}n^{n/2}}\cdot\frac{\big(\frac{m-1}{n-1}u\big)^{m/2}}{\big(1+\frac{m-1}{n-1}u\big)^{(m+n)/2}},\qquad u=\frac{a/(m-1)}{b/(n-1)}.
$$
作为 $u\ge0$ 的函数，$\lambda$ 先增至在 $u_0=\frac{m(n-1)}{n(m-1)}$ 处的最大值 $1$，再减至 $0$，所以 $\lambda\le\lambda_0$ 当且仅当 $u\le C_1$ 或 $u\ge C_2$。在 $H_0$ 下 $U=S_X^2/S_Y^2\sim F_{m-1,n-1}$；取等尾，$C_1=F_{m-1,n-1,1-\alpha/2}$，$C_2=F_{m-1,n-1,\alpha/2}$：这就是 $F$ 检验。

### 5.3.4. 似然比的极限分布

当 $\lambda$ 无法化为已知分布的统计量时，下面的定理给出近似检验。

**定理 5.3.1（Wilks 定理）** 设 $\Theta$ 的维数为 $k$，$\Theta_0$ 的维数为 $s$，$k-s=t>0$，且密度满足一定的正则条件。则对检验问题 $H_0\colon\theta\in\Theta_0$ vs. $H_1\colon\theta\in\Theta_1$，在 $H_0$ 下当 $n\to\infty$ 时

$$
-2\log\lambda(\boldsymbol{X})\xrightarrow{d}\chi^2_t.
$$
因此 $\{-2\log\lambda>\chi^2_{t,\alpha}\}$ 是水平近似为 $\alpha$ 的拒绝域。

**注 5.3.2** $\Theta$ 的维数必须严格大于 $\Theta_0$ 的维数；例如对正态样本与 $H_0\colon\mu=\mu_0$，$\Theta=\{(\mu,\sigma^2)\colon\mu\in\mathbb{R},\sigma^2>0\}$ 的维数为 $2$，$\Theta_0=\{(\mu_0,\sigma^2)\colon\sigma^2>0\}$ 的维数为 $1$。$\Theta_0$ 可以含有许多点：对每个 $\theta\in\Theta_0$，极限 $\chi^2_t$ 都相同。正则条件就是使极大似然估计渐近正态的那些条件（真值是内点，参数维数在 $n\to\infty$ 时固定，等等）。在例 5.3.4 中，$-2\log\lambda=n\log\big(1+T^2/(n-1)\big)\approx T^2\xrightarrow{d}\chi^2_1$，与定理一致。

**例 5.3.10** 设 $\boldsymbol{X}_i=(X_{i1},\dots,X_{in_i})$ 是来自 $\mathcal{N}(\mu_i,\sigma_i^2)$ 的相互独立的样本，$i=1,\dots,m$。求 $H_0\colon\sigma_1^2=\dots=\sigma_m^2$ 对"它们不全相等"的似然比检验。

令 $\theta=(\mu_1,\dots,\mu_m;\sigma_1^2,\dots,\sigma_m^2)$，则 $\Theta$ 的维数为 $k=2m$，$\Theta_0=\{\theta\colon\sigma_1^2=\dots=\sigma_m^2\}$ 的维数为 $s=m+1$。令

$$
\bar X_i=\frac{1}{n_i}\sum_{j=1}^{n_i}X_{ij},\qquad S_i^2=\frac{1}{n_i}\sum_{j=1}^{n_i}(X_{ij}-\bar X_i)^2,\qquad S^2=\frac1n\sum_{i=1}^mn_iS_i^2,\qquad n=\sum_{i=1}^mn_i.
$$
在 $\Theta$ 上，极大似然估计为 $\hat\mu_i=\bar X_i$，$\hat\sigma_i^2=S_i^2$，$L(\hat\theta_{\mathrm{MLE}})=(2\pi\mathrm{e})^{-n/2}\prod_iS_i^{-n_i}$；在 $H_0$ 下 $\hat\sigma^2=S^2$，$L(\hat\theta_{\mathrm{MLE},0})=(2\pi\mathrm{e})^{-n/2}S^{-n}$。因此

$$
\lambda=\prod_{i=1}^mS_i^{n_i}\Big/S^n,\qquad -2\log\lambda=n\log S^2-\sum_{i=1}^mn_i\log S_i^2.
$$
由定理 5.3.1，当 $\min\{n_1,\dots,n_m\}\to\infty$ 时，在 $H_0$ 下 $-2\log\lambda\xrightarrow{d}\chi^2_{m-1}$，$\{-2\log\lambda>\chi^2_{m-1,\alpha}\}$ 是水平近似为 $\alpha$ 的拒绝域。（加上小样本修正，这就是方差齐性的 Bartlett 检验。）

## 5.4. 一致最大功效检验

### 5.4.1. 定义

一个检验问题有许多水平相同的检验，应当如何比较？按照 Neyman–Pearson 原则，每个参与比较的检验在 $\Theta_0$ 上犯第一类错误的概率都不能超过 $\alpha$；在此前提下，犯第二类错误的概率越小，即在 $\Theta_1$ 上的功效越大，检验越好。对 $H_0\colon\mu\le0$ vs. $H_1\colon\mu>0$，一个水平 $0.05$ 的检验可能在每个 $\mu>0$ 处都优于另一个；但两个检验的功效曲线也可能交叉，这时哪一个都不是处处更好。理想的是一个同时在 $\Theta_1$ 的每一点都最好的检验。

**定义 5.4.1（一致最大功效检验）** 考虑 $H_0\colon\theta\in\Theta_0$ vs. $H_1\colon\theta\in\Theta_1$。设 $\varphi$ 是水平为 $\alpha$ 的检验。若对每个水平为 $\alpha$ 的检验 $\varphi^*$ 及一切 $\theta\in\Theta_1$ 都有 $\pi_\varphi(\theta)\ge\pi_{\varphi^*}(\theta)$，则称 $\varphi$ 为水平 $\alpha$ 的**一致最大功效检验**（UMP 检验）。当 $H_1$ 是简单假设 $\Theta_1=\{\theta_1\}$ 时，UMP 检验称为**最大功效检验**（MP 检验）。

**注 5.4.1** UMP 检验很少见。它基本上只在 $\theta$ 为实值、$H_0$ 与 $H_1$ 取某些形式（主要是单侧）、分布族 $f(x;\theta)$ 特殊时才存在。对多维参数，合理的检验要用其他原理构造：似然比检验、拟合优度检验（[3.2.6](/3.2.6)）、基于决策论的检验等。对简单原假设对简单备择假设，由下面的 Neyman–Pearson 引理，MP 检验总是存在。这个问题本身不现实，但它是通往单侧复合问题的第一步。

### 5.4.2. Neyman–Pearson 引理

**定理 5.4.1（Neyman–Pearson 引理）** 设 $\boldsymbol{X}$ 的密度（或概率质量函数）为 $f(\boldsymbol{x};\theta)$，在水平 $\alpha\in(0,1)$ 下考虑 $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta=\theta_1$。定义

$$
\varphi(\boldsymbol{x})=\begin{cases}1, & f(\boldsymbol{x};\theta_1)>Cf(\boldsymbol{x};\theta_0),\\ r, & f(\boldsymbol{x};\theta_1)=Cf(\boldsymbol{x};\theta_0),\\ 0, & f(\boldsymbol{x};\theta_1)<Cf(\boldsymbol{x};\theta_0).\end{cases}\tag{5.4}
$$
则：

1. 存在常数 $C\ge0$ 与 $r\in[0,1]$，使
   $$
   \mathbb{E}_{\theta_0}\varphi(\boldsymbol{X})=\mathbb{P}_{\theta_0}\big(f(\boldsymbol{X};\theta_1)>Cf(\boldsymbol{X};\theta_0)\big)+r\,\mathbb{P}_{\theta_0}\big(f(\boldsymbol{X};\theta_1)=Cf(\boldsymbol{X};\theta_0)\big)=\alpha;
   $$
2. 任何形如 (5.4) 且 $\mathbb{E}_{\theta_0}\varphi(\boldsymbol{X})=\alpha$ 的检验，都是所有水平为 $\alpha$ 的检验中的最大功效检验。

**证明** (1) 存在性。设 $G$ 是似然比 $f(\boldsymbol{X};\theta_1)/f(\boldsymbol{X};\theta_0)$ 在 $\mathbb{P}_{\theta_0}$ 下的分布函数（该比值以 $\mathbb{P}_{\theta_0}$-概率 $1$ 有限且非负），$G(y)=\mathbb{P}_{\theta_0}\big(f(\boldsymbol{X};\theta_1)/f(\boldsymbol{X};\theta_0)\le y\big)$。它单调不减且右连续，因此存在 $C\ge0$ 使 $G(C-0)\le1-\alpha\le G(C)$，其中 $G(C-0)=\lim_{y\uparrow C}G(y)$。于是

$$
\mathbb{E}_{\theta_0}\varphi(\boldsymbol{X})=1-G(C)+r\big[G(C)-G(C-0)\big].
$$
若 $G$ 在 $C$ 处连续，取 $r=0$；否则取 $r=\dfrac{G(C)-(1-\alpha)}{G(C)-G(C-0)}\in[0,1]$。两种情形都有 $\mathbb{E}_{\theta_0}\varphi=\alpha$。

(2) 最优性。设 $\varphi^*$ 是任一水平为 $\alpha$ 的检验，令 $S^+=\{\boldsymbol{x}\colon\varphi(\boldsymbol{x})>\varphi^*(\boldsymbol{x})\}$，$S^-=\{\boldsymbol{x}\colon\varphi(\boldsymbol{x})<\varphi^*(\boldsymbol{x})\}$。在 $S^+$ 上 $\varphi>\varphi^*\ge0$，故 $\varphi>0$，由 (5.4) 得 $f(\boldsymbol{x};\theta_1)-Cf(\boldsymbol{x};\theta_0)\ge0$；在 $S^-$ 上 $\varphi<\varphi^*\le1$，故 $\varphi<1$，从而 $f(\boldsymbol{x};\theta_1)-Cf(\boldsymbol{x};\theta_0)\le0$。两种情形下（在其余各处平凡地）都有

$$
\big[\varphi(\boldsymbol{x})-\varphi^*(\boldsymbol{x})\big]\big[f(\boldsymbol{x};\theta_1)-Cf(\boldsymbol{x};\theta_0)\big]\ge0.
$$
在 $\mathcal{X}$ 上积分（离散情形求和），

$$
\int_{\mathcal{X}}\varphi f(\boldsymbol{x};\theta_1)\,\mathrm{d}\boldsymbol{x}-\int_{\mathcal{X}}\varphi^*f(\boldsymbol{x};\theta_1)\,\mathrm{d}\boldsymbol{x}\ge C\left[\int_{\mathcal{X}}\varphi f(\boldsymbol{x};\theta_0)\,\mathrm{d}\boldsymbol{x}-\int_{\mathcal{X}}\varphi^*f(\boldsymbol{x};\theta_0)\,\mathrm{d}\boldsymbol{x}\right]=C\big[\alpha-\mathbb{E}_{\theta_0}\varphi^*\big]\ge0,
$$
因为 $\mathbb{E}_{\theta_0}\varphi^*\le\alpha$。所以 $\mathbb{E}_{\theta_1}\varphi(\boldsymbol{X})\ge\mathbb{E}_{\theta_1}\varphi^*(\boldsymbol{X})$。$\square$

**注 5.4.2** 对离散的 $X_i$，为了使水平恰好为 $\alpha$，一般必须有随机化 $r\in(0,1)$；对连续的 $X_i$，边界的概率为 $0$，$r=0$。引理对两个任意密度的检验 $H_0\colon f=f_0$ vs. $H_1\colon f=f_1$ 同样成立。由于 MP 检验只通过似然比依赖于 $\boldsymbol{x}$，而由因子分解定理（[3.2.2](/3.2.2)）似然比只依赖于充分统计量，MP 检验总可以取为充分统计量的函数。

**推论 5.4.1** 若 $\varphi$ 是 $H_0\colon\theta\in\Theta_0$ vs. $H_1\colon\theta\in\Theta_1$ 的水平 $\alpha$ 的 UMP 检验，则对一切 $\theta\in\Theta_1$ 有 $\mathbb{E}_\theta\varphi(\boldsymbol{X})\ge\alpha$。

**证明** 常数检验 $\varphi^*\equiv\alpha$ 的水平为 $\alpha$，故对 $\theta\in\Theta_1$ 有 $\mathbb{E}_\theta\varphi(\boldsymbol{X})\ge\mathbb{E}_\theta\varphi^*(\boldsymbol{X})=\alpha$。$\square$

**例 5.4.1** 设 $X$ 是来自 $f(x;\theta)=\theta x^{\theta-1}$（$0<x<1$，$\theta>1$）的一个观测值；由于 $\int_0^1\theta x^{\theta-1}\,\mathrm{d}x=1$，这确实是密度。求 $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta=\theta_1$ 的水平 $\alpha$ 的 MP 检验及其功效。

由引理，当

$$
\frac{\theta_1x^{\theta_1-1}}{\theta_0x^{\theta_0-1}}>C^*,\quad\text{即}\quad(\theta_1-\theta_0)\log x>\log\frac{\theta_0C^*}{\theta_1}
$$
时拒绝 $H_0$。若 $\theta_1>\theta_0$，这意味着 $x>C$，由 $\mathbb{P}_{\theta_0}(X>C)=1-C^{\theta_0}=\alpha$ 得 $C=(1-\alpha)^{1/\theta_0}$；若 $\theta_1<\theta_0$，这意味着 $x<C$，由 $\mathbb{P}_{\theta_0}(X<C)=C^{\theta_0}=\alpha$ 得 $C=\alpha^{1/\theta_0}$。功效为

$$
\pi(\theta_1)=1-(1-\alpha)^{\theta_1/\theta_0}\ (\theta_1>\theta_0),\qquad \pi(\theta_1)=\alpha^{\theta_1/\theta_0}\ (\theta_1<\theta_0).
$$
取 $\theta_0=4$，$\alpha=0.05$：若 $\theta_1=6$，$x>0.95^{1/4}=0.987$ 时拒绝，功效为 $1-0.95^{1.5}=0.074$；若 $\theta_1=2$，$x<0.05^{1/4}=0.473$ 时拒绝，功效为 $0.05^{1/2}=0.224$。只有一个观测值时功效很低。

### 5.4.3. 从最大功效检验到一致最大功效检验

**命题 5.4.1** 设 $\varphi$ 是 $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta=\theta_1$（$\theta_1>\theta_0$）的水平 $\alpha$ 的 MP 检验。若 $\varphi$ 不依赖于 $\theta_1$，则它是 $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta>\theta_0$ 的水平 $\alpha$ 的 UMP 检验。

**证明** $\varphi$ 对简单原假设 $\theta=\theta_0$ 的水平为 $\alpha$。设 $\varphi^*$ 是这一问题的任一水平 $\alpha$ 的检验。对每个固定的 $\theta_1>\theta_0$，$\varphi$ 与 $\varphi^*$ 都是 $\theta=\theta_0$ vs. $\theta=\theta_1$ 的水平 $\alpha$ 的检验，而 $\varphi$ 是其 MP 检验，故 $\mathbb{E}_{\theta_1}\varphi\ge\mathbb{E}_{\theta_1}\varphi^*$。$\square$

由此得到一般问题 $H_0\colon\theta\in\Theta_0$ vs. $H_1\colon\theta\in\Theta_1$（实参数）的一个构造方法：

1. 在 $\Theta_0$ 中取尽量靠近 $\Theta_1$ 的点 $\theta_0$（边界点），在 $\Theta_1$ 中任取一点 $\theta_1$；
2. 用 Neyman–Pearson 引理构造 $\theta=\theta_0$ vs. $\theta=\theta_1$ 的 MP 检验 $\varphi_{\theta_1}$；
3. 若 $\varphi_{\theta_1}=\varphi$ 不依赖于 $\theta_1$，则 $\varphi$ 是 $\theta=\theta_0$ vs. $\theta\in\Theta_1$ 的 UMP 检验；
4. 若进一步对一切 $\theta\in\Theta_0$ 有 $\mathbb{E}_\theta\varphi(\boldsymbol{X})\le\alpha$，则 $\varphi$ 是 $\theta\in\Theta_0$ vs. $\theta\in\Theta_1$ 的水平 $\alpha$ 的 UMP 检验（复合原假设的每个水平 $\alpha$ 的检验，也都是 $\theta=\theta_0$ 的水平 $\alpha$ 的检验）。

**例 5.4.2** 在例 5.4.1 中：

1. 在 $x>(1-\alpha)^{1/\theta_0}$ 时拒绝 $H_0\colon\theta=\theta_0$ 的检验，对每个固定的 $\theta_1>\theta_0$ 都是 MP 检验且不依赖于 $\theta_1$，因此是对 $H_1\colon\theta>\theta_0$ 的水平 $\alpha$ 的 UMP 检验；
2. 同理，在 $x<\alpha^{1/\theta_0}$ 时拒绝的检验是对 $H_1'\colon\theta<\theta_0$ 的 UMP 检验；
3. 对双侧备择 $H_1''\colon\theta\ne\theta_0$，$H_0\colon\theta=\theta_0$ 不存在 UMP 检验。这样的检验必须对每个 $\theta_1>\theta_0$ 与每个 $\theta_1<\theta_0$ 都是 MP 检验；由 MP 检验的唯一性（相差一个概率为零的集合），它的拒绝域必须同时是 $\big((1-\alpha)^{1/\theta_0},1\big)$ 和 $\big(0,\alpha^{1/\theta_0}\big)$，这不可能。

这是典型的情形：双侧问题没有 UMP 检验。

**例 5.4.3** 设 $X$ 是来自 $f(x;\theta)=1+\theta^2\big(\tfrac12-x\big)$（$0<x<1$，$-1\le\theta\le1$）的一个观测值；它非负且 $\int_0^1\big[1+\theta^2\big(\tfrac12-x\big)\big]\,\mathrm{d}x=1$，因而是密度。在水平 $\alpha$ 下检验 $H_0\colon\theta=0$（即均匀分布 $\mathrm{U}(0,1)$）。

对 $H_1\colon\theta=\theta_1\ne0$，引理在 $1+\theta_1^2\big(\tfrac12-x\big)>C^*$ 即 $x<C$ 时拒绝，且 $\mathbb{P}_0(X<C)=C=\alpha$。检验"$x<\alpha$ 时拒绝"不依赖于 $\theta_1$，因此是 $H_0\colon\theta=0$ 对双侧备择 $H_1'\colon\theta\ne0$ 的 UMP 检验（因为 $\theta$ 只通过 $\theta^2$ 出现）。$\alpha=0.05$ 时，$x<0.05$ 时拒绝。其功效为

$$
\pi(\theta)=\int_0^\alpha\Big[1+\theta^2\Big(\frac12-x\Big)\Big]\,\mathrm{d}x=\alpha+\frac12\alpha(1-\alpha)\theta^2,
$$
故 $\pi(\pm1)=0.074$，$\pi(\pm\frac12)=0.056$。这里双侧问题的拒绝域是单侧的：由于 $\mathbb{E}_\theta X=\frac12-\frac{\theta^2}{12}$，任何 $\theta\ne0$ 都使分布向左移。双侧问题的拒绝域不一定是双侧的。

**例 5.4.4** 设 $\boldsymbol{X}$ 是来自 $\mathrm{Ber}(\theta)$ 的样本，构造 $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta=\theta_1$（$\theta_1>\theta_0$）的水平 $\alpha$ 的 MP 检验。记 $T(\boldsymbol{x})=\sum x_i$，

$$
\frac{f(\boldsymbol{x};\theta_1)}{f(\boldsymbol{x};\theta_0)}=\left(\frac{1-\theta_1}{1-\theta_0}\right)^n\left(\frac{\theta_1(1-\theta_0)}{\theta_0(1-\theta_1)}\right)^{T(\boldsymbol{x})}.
$$
由于 $1>\theta_1>\theta_0>0$，有 $\theta_1(1-\theta_0)>\theta_0(1-\theta_1)$，比值关于 $T$ 严格递增。所以 MP 检验就是 (5.3)：$T>c$ 时 $\varphi=1$，$T=c$ 时为 $r$，$T<c$ 时为 $0$，其中

$$
\alpha_1=\sum_{k=c+1}^n\binom{n}{k}\theta_0^k(1-\theta_0)^{n-k}\le\alpha\le\sum_{k=c}^n\binom{n}{k}\theta_0^k(1-\theta_0)^{n-k},\qquad r=\frac{\alpha-\alpha_1}{\binom{n}{c}\theta_0^c(1-\theta_0)^{n-c}}.
$$
它不依赖于 $\theta_1$，由命题 5.4.1，它是 $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta>\theta_0$ 的 UMP 检验；又由于其功效递增（5.2.3 节），它也是 $H_0\colon\theta\le\theta_0$ vs. $H_1\colon\theta>\theta_0$ 的 UMP 检验。

### 5.4.4. 单参数指数族中的 UMP 检验

上面的例子之所以成立，是因为似然比关于某个统计量单调。这在单参数指数族（[3.2.2](/3.2.2)）中普遍成立，此时 5.4.3 节的方法对取值于 $\mathbb{R}$ 或某个区间的一维参数都有效。

**定理 5.4.2** 设 $\boldsymbol{X}$ 是来自单参数指数族

$$
f(x;\theta)=C(\theta)\mathrm{e}^{Q(\theta)T(x)}h(x),\qquad\theta\in\Theta\subseteq\mathbb{R}
$$
的样本，其中 $Q$ 严格递增，$h$ 不依赖于 $\theta$，记 $V(\boldsymbol{x})=\sum_{i=1}^nT(x_i)$。

1. 对 $H_0\colon\theta\le\theta_0$ vs. $H_1\colon\theta>\theta_0$，检验
   $$
   \varphi(\boldsymbol{x})=\begin{cases}1, & V(\boldsymbol{x})>C,\\ r, & V(\boldsymbol{x})=C,\\ 0, & V(\boldsymbol{x})<C,\end{cases}\qquad \mathbb{P}_{\theta_0}(V>C)+r\,\mathbb{P}_{\theta_0}(V=C)=\alpha,
   $$
   是水平 $\alpha$ 的 UMP 检验。
2. 对 $H_0\colon\theta\ge\theta_0$ vs. $H_1\colon\theta<\theta_0$，$V<C$ 时 $\varphi=1$、$V=C$ 时为 $r$、$V>C$ 时为 $0$ 且 $\mathbb{P}_{\theta_0}(V<C)+r\,\mathbb{P}_{\theta_0}(V=C)=\alpha$ 的检验是水平 $\alpha$ 的 UMP 检验。

**证明** 只证第 1 部分，第 2 部分是对称的。对 $\theta'<\theta''$，

$$
\frac{f(\boldsymbol{x};\theta'')}{f(\boldsymbol{x};\theta')}=\left(\frac{C(\theta'')}{C(\theta')}\right)^n\exp\big\{\big(Q(\theta'')-Q(\theta')\big)V(\boldsymbol{x})\big\}
$$
关于 $V(\boldsymbol{x})$ 严格递增，因为 $Q(\theta'')>Q(\theta')$。因此"$V>C$ 时拒绝、$V=C$ 时随机化"形式的检验对 $\theta'$ vs. $\theta''$ 具有 (5.4) 的形式，由定理 5.4.1 第 2 部分，它在自身的水平 $\mathbb{E}_{\theta'}\varphi$ 下是 MP 检验。

取 $\theta'=\theta_0$：$\varphi$ 对每个 $\theta''>\theta_0$ 都是水平 $\alpha$ 的 MP 检验，且不依赖于 $\theta''$，由命题 5.4.1，它是 $\theta=\theta_0$ vs. $\theta>\theta_0$ 的 UMP 检验。

功效的单调性：对任意 $\theta'<\theta''$，$\varphi$ 是 $\theta'$ 对 $\theta''$ 的水平 $\alpha'=\pi_\varphi(\theta')$ 的 MP 检验，由推论 5.4.1（用常数检验 $\alpha'$），$\pi_\varphi(\theta'')\ge\alpha'=\pi_\varphi(\theta')$。所以 $\pi_\varphi$ 不减，$\theta\le\theta_0$ 时 $\pi_\varphi(\theta)\le\pi_\varphi(\theta_0)=\alpha$，$\varphi$ 对复合原假设的水平为 $\alpha$。最后，$\theta\le\theta_0$ 的任一水平 $\alpha$ 的检验都是 $\theta=\theta_0$ 的水平 $\alpha$ 的检验，而 $\varphi$ 在每个 $\theta>\theta_0$ 处的功效都不低于它。$\square$

第 1 部分检验的功效曲线递增，在 $\theta_0$ 处经过 $\alpha$；第 2 部分检验的功效曲线递减，在 $\theta_0$ 处经过 $\alpha$。

**例 5.4.5（二项情形。）** 对 $\mathrm{Ber}(\theta)$，$f(x;\theta)=(1-\theta)\exp\{x\log\frac{\theta}{1-\theta}\}$，故 $T(x)=x$，$Q(\theta)=\log\frac{\theta}{1-\theta}$ 严格递增，$V=\sum X_i\sim\mathrm{Bin}(n,\theta)$。$\theta\le\theta_0$ vs. $\theta>\theta_0$ 的 UMP 检验就是 (5.3)；为了使用二项分布表，把它的水平条件写成 $\mathbb{P}_{\theta_0}(V\le C)-\gamma\,\mathbb{P}_{\theta_0}(V=C)=1-\alpha$，功效为 $\pi(\theta)=1-\mathbb{P}_\theta(V\le C)+\gamma\,\mathbb{P}_\theta(V=C)$。取 $n=25$，$\theta_0=0.125$，$\alpha=0.05$：$\mathbb{P}_{0.125}(V\le6)=0.9703$ 是第一个超过 $0.95$ 的值，$\mathbb{P}_{0.125}(V=6)=0.0534$，故

$$
C=6,\qquad\gamma=\frac{0.9703-0.95}{0.0534}=0.38.
$$
功效为 $\pi(0.1875)=0.230$，$\pi(0.25)=0.508$，$\pi(0.375)=0.909$。若观测到 $V=7$，$p$ 值为 $\mathbb{P}_{0.125}(V\ge7)=1-0.9703=0.030$：在水平 $0.05$ 下拒绝 $H_0$。

**例 5.4.6（正态均值。）** 对 $\sigma^2$ 已知的 $\mathcal{N}(\theta,\sigma^2)$，

$$
f(x;\theta)=\frac{1}{\sqrt{2\pi}\sigma}\mathrm{e}^{-\theta^2/(2\sigma^2)}\,\mathrm{e}^{\theta x/\sigma^2}\,\mathrm{e}^{-x^2/(2\sigma^2)},
$$
故 $T(x)=x$，$Q(\theta)=\theta/\sigma^2$ 严格递增。$\theta\le\theta_0$ vs. $\theta>\theta_0$ 的 UMP 检验在 $\sum x_i>C$ 时拒绝（$\gamma=0$），由 $\alpha=\mathbb{P}_{\theta_0}\big(\sqrt{n}(\bar X-\theta_0)/\sigma>(C-n\theta_0)/(\sigma\sqrt{n})\big)$ 得 $C=n\theta_0+z_\alpha\sigma\sqrt{n}$，即单侧 Z 检验 $\sqrt{n}(\bar x-\theta_0)/\sigma>z_\alpha$，功效为 $\pi(\theta)=1-\Phi\big(z_\alpha+\sqrt{n}(\theta_0-\theta)/\sigma\big)$。所以 5.2.1 节的单侧 Z 检验是最优的。

对例 5.1.4 的区间问题，UMP 检验也存在。

**定理 5.4.3** 在定理 5.4.2 的条件下，对 $H_0\colon\theta\le\theta_1$ 或 $\theta\ge\theta_2$ vs. $H_1\colon\theta_1<\theta<\theta_2$，检验

$$
\varphi(\boldsymbol{x})=\begin{cases}1, & C_1<V(\boldsymbol{x})<C_2,\\ r_i, & V(\boldsymbol{x})=C_i\ (i=1,2),\\ 0, & \text{其他},\end{cases}
$$
（常数 $C_1,C_2$ 与 $r_1,r_2\in[0,1]$ 由 $\mathbb{E}_{\theta_1}\varphi(\boldsymbol{X})=\mathbb{E}_{\theta_2}\varphi(\boldsymbol{X})=\alpha$ 确定）是水平 $\alpha$ 的 UMP 检验。

它的功效曲线在 $(\theta_1,\theta_2)$ 内有唯一的峰，在 $\theta_1$ 与 $\theta_2$ 处等于 $\alpha$。

**例 5.4.7** 对 $\sigma$ 已知的 $\mathcal{N}(\theta,\sigma^2)$，$\theta\le\theta_1$ 或 $\theta\ge\theta_2$ vs. $\theta_1<\theta<\theta_2$ 的 UMP 检验在 $C_1\le\sum x_i\le C_2$ 时拒绝；由于 $\sum X_i\sim\mathcal{N}(n\theta,n\sigma^2)$，常数满足

$$
\Phi\left(\frac{C_2-n\theta_i}{\sigma\sqrt{n}}\right)-\Phi\left(\frac{C_1-n\theta_i}{\sigma\sqrt{n}}\right)=\alpha,\quad i=1,2,
$$
功效为 $\pi(\theta)=\Phi\big((C_2-n\theta)/(\sigma\sqrt{n})\big)-\Phi\big((C_1-n\theta)/(\sigma\sqrt{n})\big)$。取 $n=25$，$\theta_1=1$，$\theta_2=3$，$\sigma=1$，$\alpha=0.01$。两个方程为

$$
\Phi\Big(\frac{C_2-25}{5}\Big)-\Phi\Big(\frac{C_1-25}{5}\Big)=\Phi\Big(\frac{C_2-75}{5}\Big)-\Phi\Big(\frac{C_1-75}{5}\Big)=0.01,
$$
由对称性，$C_1+C_2=100$ 时它们成立。令 $C_1=C$，由 $\Phi\big((75-C)/5\big)-\Phi\big((C-25)/5\big)=0.01$ 得 $C=36.6$。所以 $36.6\le\sum x_i\le63.4$ 时拒绝 $H_0$；功效为 $\pi(1.5)=\pi(2.5)=0.569$，$\pi(2)=0.992$。

对 $\theta=\theta_0$ vs. $\theta\ne\theta_0$ 这样的双侧问题，一般不存在 UMP 检验（例 5.4.2），必须缩小参与比较的检验类。推论 5.4.1 提示了一个自然的限制：合理的检验在 $H_1$ 为真时拒绝的概率应当不低于 $\alpha$。

**定义 5.4.2（无偏检验）** 水平为 $\alpha$ 的检验 $\varphi$ 若对一切 $\theta\in\Theta_0$ 有 $\pi_\varphi(\theta)\le\alpha$、对一切 $\theta\in\Theta_1$ 有 $\pi_\varphi(\theta)\ge\alpha$，则称为**无偏检验**。在所有水平 $\alpha$ 的无偏检验中一致最大功效的检验，称为**一致最大功效无偏检验**（UMPU 检验）。

**注 5.4.3** 由推论 5.4.1，UMP 检验是无偏的。用于双侧问题的单侧拒绝域 $D_2$（注 5.2.2）是有偏的：它在一侧的功效低于 $\alpha$。对单参数指数族，双侧问题 $\theta=\theta_0$ vs. $\theta\ne\theta_0$ 存在在 $V<C_1$ 或 $V>C_2$ 时拒绝的 UMPU 检验；双侧 Z 检验，以及（推广到含讨厌参数的分布族后）双侧 $t$ 检验，都是 UMPU 检验。

定理 5.4.2 的证明中本质的性质是似然比的单调性，定理可以推广到所有具有这一性质的分布族。

**定义 5.4.3（单调似然比）** 若对一切 $\theta'<\theta''$，比值 $f(\boldsymbol{x};\theta'')/f(\boldsymbol{x};\theta')$ 在两个密度至少有一个为正的集合上是 $T(\boldsymbol{x})$ 的不减函数，则称分布族 $\{f(\boldsymbol{x};\theta)\colon\theta\in\Theta\subseteq\mathbb{R}\}$ 关于统计量 $T(\boldsymbol{x})$ 具有**单调似然比**。

**定理 5.4.4（Karlin–Rubin 定理）** 若分布族关于 $T$ 具有单调似然比，则对 $H_0\colon\theta\le\theta_0$ vs. $H_1\colon\theta>\theta_0$，在 $T>C$ 时拒绝、在 $T=C$ 时以概率 $r$ 随机化（$\mathbb{P}_{\theta_0}(T>C)+r\,\mathbb{P}_{\theta_0}(T=C)=\alpha$）的检验是水平 $\alpha$ 的 UMP 检验，且其功效函数不减。

证明与定理 5.4.2 相同。$Q$ 递增的单参数指数族关于 $V$ 具有单调似然比；均匀分布族 $\mathrm{U}(0,\theta)$ 关于 $\max_iX_i$ 也具有单调似然比，而它不是指数族。

## 5.5. 假设检验与置信区间

检验与置信域可以互相构造：$1-\alpha$ **置信区间**由水平 $\alpha$ 的检验不拒绝的那些参数值组成。

### 5.5.1. 由检验构造置信区间

设 $\boldsymbol{X}$ 是来自 $\{f(x;\theta)\colon\theta\in\Theta\}$ 的样本，$\theta$ 为实数。为构造 $\theta$ 的 $1-\alpha$ 置信区间，考虑 $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta\ne\theta_0$ 及水平 $\alpha$ 的拒绝域 $D$，于是 $\mathbb{P}_{\theta_0}(D^{\mathsf c})=1-\alpha$。把定义接受域 $D^{\mathsf c}$ 的不等式对 $\theta_0$ 求解，得到 $\hat\theta_1(\boldsymbol{X})\le\theta_0\le\hat\theta_2(\boldsymbol{X})$；把 $\theta_0$ 换成 $\theta$，$[\hat\theta_1(\boldsymbol{X}),\hat\theta_2(\boldsymbol{X})]$ 就是 $1-\alpha$ 置信区间。同样地，由 $H_0\colon\theta\ge\theta_0$ vs. $H_1\colon\theta<\theta_0$ 得到置信上限，由 $H_0\colon\theta\le\theta_0$ vs. $H_1\colon\theta>\theta_0$ 得到置信下限。

**定理 5.5.1** 设 $\boldsymbol{X}$ 是来自 $f(x;\theta)$（$\theta\in\Theta\subseteq\mathbb{R}^k$）的样本。对每个 $\theta\in\Theta$，设 $A(\theta)=D^{\mathsf c}(\theta)\subseteq\mathbb{R}^n$ 是 $H_0\colon\theta^*=\theta$ vs. $H_1\colon\theta^*\ne\theta$ 的某个水平 $\alpha$ 的检验的接受域；对每个 $\boldsymbol{x}$，令 $T(\boldsymbol{x})=\{\theta\in\Theta\colon\boldsymbol{x}\in A(\theta)\}$。则 $T(\boldsymbol{X})$ 是 $\theta$ 的置信水平为 $1-\alpha$ 的置信域。

**证明** 对每个 $\theta$，$\mathbb{P}_\theta\big(\theta\in T(\boldsymbol{X})\big)=\mathbb{P}_\theta\big(\boldsymbol{X}\in A(\theta)\big)\ge1-\alpha$，当检验的水平恰为 $\alpha$ 时等号成立。$\square$

**例 5.5.1** 设 $\boldsymbol{X}$ 是来自 $\mathcal{N}(\mu,\sigma^2)$ 的样本，两个参数都未知。$\mu=\mu_0$ vs. $\mu\ne\mu_0$ 的水平 $\alpha$ 的 $t$ 检验的接受域为 $\big\{\lvert\sqrt{n}(\bar X-\mu_0)/S\rvert\le t_{n-1,\alpha/2}\big\}$，它在 $\mu=\mu_0$ 下的概率为 $1-\alpha$。对 $\mu_0$ 求解并换成 $\mu$，得置信区间

$$
\left[\bar X-\frac{S}{\sqrt{n}}t_{n-1,\alpha/2},\ \bar X+\frac{S}{\sqrt{n}}t_{n-1,\alpha/2}\right].
$$
$\mu\le\mu_0$ vs. $\mu>\mu_0$ 的检验的接受域 $\{\sqrt{n}(\bar X-\mu_0)/S\le t_{n-1,\alpha}\}$ 给出置信下限 $\bar X-St_{n-1,\alpha}/\sqrt{n}$，同理置信上限为 $\bar X+St_{n-1,\alpha}/\sqrt{n}$。5.2.2 节的 $\chi^2$ 检验以同样的方式给出 $\sigma^2$ 的区间 $\big[(n-1)S^2/\chi^2_{n-1,\alpha/2},\ (n-1)S^2/\chi^2_{n-1,1-\alpha/2}\big]$ 及相应的单侧置信限。

### 5.5.2. 由置信区间进行检验

**命题 5.5.1** 设 $\alpha\in(0,1)$。

1. 若 $[\hat\theta_1(\boldsymbol{X}),\hat\theta_2(\boldsymbol{X})]$ 是 $\theta$ 的 $1-\alpha$ 置信区间，则在 $\theta_0\notin[\hat\theta_1,\hat\theta_2]$ 时拒绝 $H_0\colon\theta=\theta_0$（备择 $\theta\ne\theta_0$）的检验的水平为 $\alpha$。
2. 若 $\hat\theta_U(\boldsymbol{X})$ 是 $1-\alpha$ 置信上限，则在 $\theta_0>\hat\theta_U$ 时拒绝 $H_0\colon\theta\ge\theta_0$（备择 $\theta<\theta_0$）的检验的水平为 $\alpha$。
3. 若 $\hat\theta_L(\boldsymbol{X})$ 是 $1-\alpha$ 置信下限，则在 $\theta_0<\hat\theta_L$ 时拒绝 $H_0\colon\theta\le\theta_0$（备择 $\theta>\theta_0$）的检验的水平为 $\alpha$。

**证明** 第 1 部分中，$\mathbb{P}_{\theta_0}(\text{拒绝})=1-\mathbb{P}_{\theta_0}\big(\theta_0\in[\hat\theta_1,\hat\theta_2]\big)\le\alpha$。第 2 部分中，对每个 $\theta\ge\theta_0$，$\mathbb{P}_\theta(\theta_0>\hat\theta_U)\le\mathbb{P}_\theta(\theta>\hat\theta_U)\le\alpha$；第 3 部分是对称的。$\square$

**例 5.5.2** 对例 5.2.8 的工资数据，设 $X$、$Y$ 分别是教授与助理教授的工资。在方差未知且不等的正态假定下，正态近似给出 $\mu_1-\mu_2$ 的 $95\%$ 置信区间 $[42133,\,49860]$，Welch 方法给出 $[42118,\,49874]$。由于 $0$ 不在区间内，在 $\alpha=0.05$ 下拒绝 $H_0\colon\mu_1-\mu_2=0$。教授的平均工资是否比助理教授高出 $40000$ 以上（$H_0\colon\mu_1-\mu_2\le40000$ vs. $H_1\colon\mu_1-\mu_2>40000$）？$95\%$ 的 Welch 置信下限为

$$
\bar x-\bar y-t_{r,0.05}\sqrt{s_X^2/m+s_Y^2/n}=42744>40000,
$$
故拒绝 $H_0$；相应地，单侧 Welch 检验给出 $t=3.04$，$p=0.0013$。

## 5.6. 线性模型中的假设检验

### 5.6.1. 回归系数的 t 检验

是什么因素决定房价？在 Ames 房屋数据中，记录了 $n=1598$ 套房屋的售价 $y$ 及 $p=8$ 个解释变量（居住面积、地块面积、全卫数、卧室数、中央空调、泳池面积、地下室面积、售出年份）。线性回归模型为

$$
y_i=\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}+\varepsilon_i,\quad i=1,\dots,n,\qquad\text{即}\qquad\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon},
$$
其中 $\boldsymbol{\beta}=(\beta_0,\beta_1,\dots,\beta_p)^{\mathsf T}$，$\boldsymbol{x}_i=(1,x_{i1},\dots,x_{ip})^{\mathsf T}$，$\boldsymbol{Y}=(y_1,\dots,y_n)^{\mathsf T}$ 是随机的响应，$X=(\boldsymbol{x}_1,\dots,\boldsymbol{x}_n)^{\mathsf T}$ 是固定的 $n\times(p+1)$ 设计矩阵（假定列满秩），$\boldsymbol{\varepsilon}$ 是随机误差。为进行推断，假定 $\varepsilon_1,\dots,\varepsilon_n\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$，于是数据的密度为 $\prod_{i=1}^n\frac{1}{\sqrt{2\pi}\sigma}\exp\big\{-(y_i-\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta})^2/(2\sigma^2)\big\}$。最小二乘估计（也是极大似然估计）与偏差修正的方差估计为

$$
\hat{\boldsymbol{\beta}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y},\qquad \hat\sigma^2=\frac{\mathrm{RSS}}{n-p-1},\qquad \mathrm{RSS}=\sum_{i=1}^n(y_i-\boldsymbol{x}_i^{\mathsf T}\hat{\boldsymbol{\beta}})^2=\|\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}\|_2^2.
$$
记 $c_{jj}=[(X^{\mathsf T}X)^{-1}]_{j+1,j+1}$ 为对应于 $\beta_j$ 的对角元（$j=0,\dots,p$）。

**定理 5.6.1** 在上述模型中，

1. $\mathbb{E}\hat{\boldsymbol{\beta}}=\boldsymbol{\beta}$；
2. $\hat{\boldsymbol{\beta}}\sim\mathcal{N}_{p+1}\big(\boldsymbol{\beta},\sigma^2(X^{\mathsf T}X)^{-1}\big)$，特别地 $\hat\beta_j\sim\mathcal{N}(\beta_j,\sigma^2c_{jj})$；
3. $(n-p-1)\hat\sigma^2/\sigma^2\sim\chi^2_{n-p-1}$；
4. $\hat{\boldsymbol{\beta}}$ 与 $\hat\sigma^2$ 相互独立。

基于**多元正态分布**和到 $X$ 的列空间的投影的证明见 [3.3](/3.3)。由此，对 $j=0,1,\dots,p$，

$$
T_j=\frac{\hat\beta_j-\beta_j}{\hat\sigma\sqrt{c_{jj}}}\sim t_{n-p-1}.
$$
$\beta_j$ 的 $1-\alpha$ 置信区间为 $\big[\hat\beta_j-\hat\sigma\sqrt{c_{jj}}\,t_{n-p-1,\alpha/2},\ \hat\beta_j+\hat\sigma\sqrt{c_{jj}}\,t_{n-p-1,\alpha/2}\big]$，$\sigma^2$ 的为 $\big[(n-p-1)\hat\sigma^2/\chi^2_{n-p-1,\alpha/2},\ (n-p-1)\hat\sigma^2/\chi^2_{n-p-1,1-\alpha/2}\big]$。对两个系数联合而言，把两个区间中的 $t_{n-p-1,\alpha/2}$ 换成 $t_{n-p-1,\alpha/4}$ 所得的矩形以至少 $1-\alpha$ 的概率覆盖 $(\beta_1,\beta_2)$（由 Bonferroni 不等式）。

为检验第 $j$ 个变量是否有影响，$H_{0j}\colon\beta_j=0$ vs. $H_{1j}\colon\beta_j\ne0$，我们在 $\lvert\hat\beta_j\rvert$ 相对其标准误较大时拒绝。在 $H_{0j}$ 下 $T_j=\hat\beta_j/(\hat\sigma\sqrt{c_{jj}})\sim t_{n-p-1}$，故水平 $\alpha$ 的检验为

$$
\varphi=\begin{cases}1, & \lvert\hat\beta_j\rvert/(\hat\sigma\sqrt{c_{jj}})>t_{n-p-1,\alpha/2},\\ 0, & \text{其他},\end{cases}
$$
$p$ 值为 $\mathbb{P}(\lvert t_{n-p-1}\rvert\ge\lvert t_j\rvert)$，其中 $t_j$ 是 $T_j$ 的观测值。

**例 5.6.1** 对 Ames 数据，拟合模型给出（$\hat\sigma=39210$，自由度 $1589$）：

| | 估计值 | $t_j$ | $p$ 值 |
|---|---|---|---|
| 截距 | $1.972\times10^6$ | $1.30$ | $0.192$ |
| 居住面积 | $98.22$ | $31.53$ | $<10^{-15}$ |
| 地块面积 | $0.877$ | $4.70$ | $2.9\times10^{-6}$ |
| 全卫数 | $1.791\times10^4$ | $7.74$ | $1.7\times10^{-14}$ |
| 卧室数 | $-2.520\times10^4$ | $-17.53$ | $<10^{-15}$ |
| 中央空调 | $2.427\times10^4$ | $6.35$ | $2.8\times10^{-10}$ |
| 泳池面积 | $-40.86$ | $-1.63$ | $0.103$ |
| 地下室面积 | $69.27$ | $25.82$ | $<10^{-15}$ |
| 售出年份 | $-995.4$ | $-1.32$ | $0.186$ |

在 $\alpha=0.05$ 下，居住面积、地块面积、全卫数、卧室数、中央空调与地下室面积的 $H_{0j}$ 被拒绝，截距、泳池面积与售出年份的则不被拒绝。（卧室数的系数为负，是在其他变量给定时的效应：居住面积固定时，卧室越多房间越小。）

### 5.6.2. 线性回归中的似然比检验

似然函数为 $L(\boldsymbol{\beta},\sigma^2)=(2\pi\sigma^2)^{-n/2}\exp\big\{-\|\boldsymbol{Y}-X\boldsymbol{\beta}\|_2^2/(2\sigma^2)\big\}$，参数空间为 $\Theta=\{(\boldsymbol{\beta},\sigma^2)\}\subseteq\mathbb{R}^{p+2}$。在 $\Theta$ 上，$\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$，$\hat\sigma^2_{\mathrm{MLE}}=\frac1n\|\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}\|_2^2$，最大值为 $(2\pi\hat\sigma^2_{\mathrm{MLE}})^{-n/2}\mathrm{e}^{-n/2}$。

先考虑单个系数。在 $H_{0j}\colon\beta_j=0$ 下，$\Theta_0\subseteq\mathbb{R}^{p+1}$。记 $\boldsymbol{\beta}_{-j}$ 为去掉 $\beta_j$ 的 $\boldsymbol{\beta}$，$X_{-j}$ 为去掉相应列的设计矩阵；则 $\hat{\boldsymbol{\beta}}_{\mathrm{MLE},0}=(X_{-j}^{\mathsf T}X_{-j})^{-1}X_{-j}^{\mathsf T}\boldsymbol{Y}$，$\hat\sigma^2_{\mathrm{MLE},0}=\frac1n\|\boldsymbol{Y}-X_{-j}\hat{\boldsymbol{\beta}}_{\mathrm{MLE},0}\|_2^2$，且

$$
\lambda=\left(\frac{\hat\sigma^2_{\mathrm{MLE}}}{\hat\sigma^2_{\mathrm{MLE},0}}\right)^{n/2}=\left(\frac{\|\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}\|_2^2}{\|\boldsymbol{Y}-X_{-j}\hat{\boldsymbol{\beta}}_{\mathrm{MLE},0}\|_2^2}\right)^{n/2}.
$$
由定理 5.3.1（维数为 $p+2$ 与 $p+1$），在 $H_{0j}$ 下当 $n\to\infty$ 时 $-2\log\lambda=n\log\|\boldsymbol{Y}-X_{-j}\hat{\boldsymbol{\beta}}_{\mathrm{MLE},0}\|_2^2-n\log\|\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}\|_2^2\xrightarrow{d}\chi^2_1$，$\{-2\log\lambda>\chi^2_{1,\alpha}\}$ 的水平近似为 $\alpha$。

**命题 5.6.1** $-2\log\lambda=n\log\big(1+T_j^2/(n-p-1)\big)$，其中 $T_j=\hat\beta_j/(\hat\sigma\sqrt{c_{jj}})$。因此 $H_{0j}$ 的精确似然比检验就是 5.6.1 节的 $t$ 检验。

**证明** 去掉第 $j$ 列时残差平方和的增量为 $\mathrm{RSS}_0-\mathrm{RSS}=\hat\beta_j^2/c_{jj}$（嵌套最小二乘拟合的一个标准恒等式，证明见 [3.3](/3.3)）。因此 $\mathrm{RSS}_0/\mathrm{RSS}=1+\hat\beta_j^2/(c_{jj}\mathrm{RSS})=1+T_j^2/(n-p-1)$，而 $-2\log\lambda=n\log(\mathrm{RSS}_0/\mathrm{RSS})$。$\square$

其次检验整体显著性：线性模型究竟有没有用，$H_0\colon\beta_1=\dots=\beta_p=0$ vs. $H_1$：某个 $\beta_j\ne0$？此时 $\Theta_0=\{(\beta_0,\sigma^2)\}$ 的维数为 $2$，$\hat\beta_0=\bar y$，$\hat\sigma^2=\frac1n\|\boldsymbol{Y}-\bar y\boldsymbol{1}\|_2^2$，且

$$
\lambda=\left(\frac{\|\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}\|_2^2}{\|\boldsymbol{Y}-\bar y\boldsymbol{1}\|_2^2}\right)^{n/2},\qquad -2\log\lambda\xrightarrow{d}\chi^2_p.
$$
这里有精确的检验。平方和分解为

$$
\|\boldsymbol{Y}-\bar y\boldsymbol{1}\|_2^2=\|\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}\|_2^2+\|X\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}-\bar y\boldsymbol{1}\|_2^2,
$$
在 $H_0$ 下 $Z_1=\|X\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}-\bar y\boldsymbol{1}\|_2^2/\sigma^2\sim\chi^2_p$ 与 $Z_2=\|\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}\|_2^2/\sigma^2\sim\chi^2_{n-p-1}$ 相互独立，故

$$
F=\frac{Z_1/p}{Z_2/(n-p-1)}\sim F_{p,n-p-1},\qquad \lambda^{2/n}=\left(1+\frac{p}{n-p-1}F\right)^{-1}.
$$
似然比检验在 $F>F_{p,n-p-1,\alpha}$ 时拒绝。对 Ames 数据，$F=621.4$，自由度为 $8$ 与 $1589$，$p<10^{-15}$，决定系数 $R^2=0.758$。

### 5.6.3. 两因素方差分析

**例 5.6.2** 某公司打算从 $I$ 个品牌中选一个，大量购买机器。让 $J$ 名工人每人使用每个品牌的机器各一天，品牌 $i$、工人 $j$ 的产量 $Y_{ij}$ 的模型为

$$
Y_{ij}=\mu+\alpha_i+\beta_j+e_{ij},\qquad\sum_{i=1}^I\alpha_i=0,\quad\sum_{j=1}^J\beta_j=0,\qquad e_{ij}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
其中 $I,J\ge2$：$\mu$ 是总平均，$\alpha_i$ 是行效应（品牌），$\beta_j$ 是列效应（工人），各效应是可加的。两个因素分别有 $I$ 与 $J$ 个水平，对这种设计的分析就是两因素方差分析（analysis of variance），简称 ANOVA。我们要估计 $\mu$、$\alpha_i$、$\beta_j$、$\sigma^2$，并检验行效应 $H_{0,A}\colon\alpha_1=\dots=\alpha_I=0$（品牌之间有无差异？）与列效应 $H_{0,B}\colon\beta_1=\dots=\beta_J=0$（工人之间有无差异？）。

似然函数为 $L(\boldsymbol{y};\mu,\boldsymbol{\alpha},\boldsymbol{\beta},\sigma^2)=(2\pi\sigma^2)^{-IJ/2}\exp\big[-\frac{1}{2\sigma^2}\sum_i\sum_j(y_{ij}-\mu-\alpha_i-\beta_j)^2\big]$，因此对每个 $\sigma^2$，使它最大等价于使 $\mathcal{S}(\mu,\boldsymbol{\alpha},\boldsymbol{\beta})=\sum_i\sum_j(y_{ij}-\mu-\alpha_i-\beta_j)^2$ 最小。记 $\bar y_{i\cdot}=\frac1J\sum_jy_{ij}$，$\bar y_{\cdot j}=\frac1I\sum_iy_{ij}$，$\bar y_{\cdot\cdot}=\frac{1}{IJ}\sum_i\sum_jy_{ij}$。

**引理 5.6.1** 在约束条件下，$\mathcal{S}$ 的唯一最小值点（最小二乘估计）为

$$
\hat\mu=\bar y_{\cdot\cdot},\qquad\hat\alpha_i=\bar y_{i\cdot}-\bar y_{\cdot\cdot},\qquad\hat\beta_j=\bar y_{\cdot j}-\bar y_{\cdot\cdot}.
$$

因此 $\sigma^2$ 的极大似然估计为 $\hat\sigma^2=\frac{1}{IJ}\sum_i\sum_j(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})^2$。在 $H_{0,A}$ 下同样的论证给出 $\hat\mu_A=\bar y_{\cdot\cdot}$，$\hat\beta_{j,A}=\bar y_{\cdot j}-\bar y_{\cdot\cdot}$，$\hat\sigma_A^2=\frac{1}{IJ}\sum_i\sum_j(y_{ij}-\bar y_{\cdot j})^2$。两个最大似然值都形如 $(2\pi\hat\sigma^2)^{-IJ/2}\mathrm{e}^{-IJ/2}$，故

$$
\lambda=\left(\hat\sigma^2/\hat\sigma_A^2\right)^{IJ/2},
$$
且 $\lambda<C$ 当且仅当 $\hat\sigma_A^2/\hat\sigma^2>C_0$。定义平方和

$$
\begin{aligned}
\mathrm{SS}_e&=\sum_i\sum_j(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})^2=IJ\hat\sigma^2, & \mathrm{SS}_A&=J\sum_i(\bar y_{i\cdot}-\bar y_{\cdot\cdot})^2,\\
\mathrm{SS}_B&=I\sum_j(\bar y_{\cdot j}-\bar y_{\cdot\cdot})^2, & \mathrm{SS}_T&=\sum_i\sum_j(y_{ij}-\bar y_{\cdot\cdot})^2.
\end{aligned}
$$

**引理 5.6.2** $IJ\hat\sigma_A^2=\mathrm{SS}_e+\mathrm{SS}_A$，且 $\mathrm{SS}_T=\mathrm{SS}_e+\mathrm{SS}_A+\mathrm{SS}_B$。此外 $\mathrm{SS}_A=J\sum_i\bar y_{i\cdot}^2-IJ\bar y_{\cdot\cdot}^2$，$\mathrm{SS}_B=I\sum_j\bar y_{\cdot j}^2-IJ\bar y_{\cdot\cdot}^2$，$\mathrm{SS}_T=\sum_i\sum_jy_{ij}^2-IJ\bar y_{\cdot\cdot}^2$。

**证明** 写 $y_{ij}-\bar y_{\cdot j}=(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})+(\bar y_{i\cdot}-\bar y_{\cdot\cdot})$；由于对每个 $i$ 有 $\sum_j(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})=0$，交叉项为零。把 $y_{ij}-\bar y_{\cdot\cdot}$ 拆成两两交叉和为零的三部分，同样可证 $\mathrm{SS}_T$ 的分解；展开平方即得计算公式。$\square$

由引理 5.6.2，$\hat\sigma_A^2/\hat\sigma^2=1+\mathrm{SS}_A/\mathrm{SS}_e$，因此似然比检验在 $\mathrm{SS}_A/\mathrm{SS}_e>C_1$ 时拒绝 $H_{0,A}$。

**定理 5.6.2** 把观测值换成随机变量 $Y_{ij}$。则 $\mathrm{SS}_e/\sigma^2\sim\chi^2_{(I-1)(J-1)}$，且 $\mathrm{SS}_e$、$\mathrm{SS}_A$、$\mathrm{SS}_B$ 相互独立。在 $H_{0,A}$ 下 $\mathrm{SS}_A/\sigma^2\sim\chi^2_{I-1}$，故

$$
F_A=\frac{\mathrm{SS}_A/(I-1)}{\mathrm{SS}_e/[(I-1)(J-1)]}\sim F_{I-1,(I-1)(J-1)};
$$
同样，在 $H_{0,B}$ 下 $F_B=\dfrac{\mathrm{SS}_B/(J-1)}{\mathrm{SS}_e/[(I-1)(J-1)]}\sim F_{J-1,(I-1)(J-1)}$。

水平 $\alpha$ 的检验在 $F_A>F_{I-1,(I-1)(J-1),\alpha}$ 时拒绝 $H_{0,A}$，在 $F_B>F_{J-1,(I-1)(J-1),\alpha}$ 时拒绝 $H_{0,B}$。计算列成方差分析表：

| 来源 | 平方和 | 自由度 | 均方 |
|---|---|---|---|
| 行 | $\mathrm{SS}_A=J\sum_i\hat\alpha_i^2$ | $I-1$ | $\mathrm{MS}_A=\mathrm{SS}_A/(I-1)$ |
| 列 | $\mathrm{SS}_B=I\sum_j\hat\beta_j^2$ | $J-1$ | $\mathrm{MS}_B=\mathrm{SS}_B/(J-1)$ |
| 残差 | $\mathrm{SS}_e$ | $(I-1)(J-1)$ | $\mathrm{MS}_e=\mathrm{SS}_e/[(I-1)(J-1)]$ |
| 总和 | $\mathrm{SS}_T$ | $IJ-1$ | |

且 $F_A=\mathrm{MS}_A/\mathrm{MS}_e$，$F_B=\mathrm{MS}_B/\mathrm{MS}_e$。

**注 5.6.1** 这里 $\Theta$ 的维数为 $I+J$（$\mu$、$I-1$ 个自由的 $\alpha_i$、$J-1$ 个自由的 $\beta_j$、$\sigma^2$），$H_{0,A}$ 下 $\Theta_0$ 的维数为 $J+1$，定理 5.3.1 似乎给出 $-2\log\lambda\approx\chi^2_{I-1}$。然而每个格子只有一个观测值时，参数个数随 $J$ 增长，正则条件不成立：由于 $-2\log\lambda=IJ\log(1+\mathrm{SS}_A/\mathrm{SS}_e)$，而 $J\to\infty$ 时 $\mathrm{SS}_e/(IJ)\to\frac{I-1}{I}\sigma^2$，在 $H_{0,A}$ 下的极限是 $\frac{I}{I-1}\chi^2_{I-1}$ 而不是 $\chi^2_{I-1}$。应当使用定理 5.6.2 的精确 $F$ 检验。

对下面的数据（三个品牌、四名工人），

| 品牌 | 工人 1 | 工人 2 | 工人 3 | 工人 4 | $\bar y_{i\cdot}$ |
|---|---|---|---|---|---|
| 1 | 3 | 7 | 5 | 4 | 19/4 |
| 2 | −1 | 2 | 0 | 2 | 3/4 |
| 3 | 1 | 2 | 4 | 0 | 7/4 |
| $\bar y_{\cdot j}$ | 1 | 11/3 | 3 | 2 | $\bar y_{\cdot\cdot}=29/12$ |

得 $\hat\mu=29/12=2.417$，$\hat\alpha_1=7/3$，$\hat\alpha_2=-5/3$，$\hat\alpha_3=-2/3$，$\hat\beta_1=-17/12$，$\hat\beta_2=5/4$，$\hat\beta_3=7/12$，$\hat\beta_4=-5/12$，且

$$
\mathrm{SS}_A=\frac{104}{3}=34.667,\qquad\mathrm{SS}_B=\frac{147}{12}=12.25,\qquad\mathrm{SS}_T=\frac{707}{12}=58.917,\qquad\mathrm{SS}_e=\mathrm{SS}_T-\mathrm{SS}_A-\mathrm{SS}_B=12.
$$
$\sigma^2$ 的无偏估计为 $\mathrm{SS}_e/[(I-1)(J-1)]=2$，而极大似然估计为 $12/12=1$。进一步，

$$
F_A=\frac{(104/3)/2}{12/6}=\frac{26}{3}=8.667>F_{2,6,0.05}=5.143,\qquad F_B=\frac{(147/12)/3}{12/6}=\frac{147}{72}=2.042<F_{3,6,0.05}=4.757,
$$
所以拒绝"品牌无差异"的假设，不拒绝"工人无差异"的假设。同样的论证可以推广到每个格子有多个观测值的两因素设计。

## 小结 {#summary}

| 情形 | 统计量及其零分布 | 小节 |
|---|---|---|
| 正态均值，$\sigma^2$ 已知 | $Z=\sqrt{n}(\bar X-\mu_0)/\sigma\sim\mathcal{N}(0,1)$ | 5.2.1 |
| 正态均值，$\sigma^2$ 未知 | $T=\sqrt{n}(\bar X-\mu_0)/S\sim t_{n-1}$ | 5.2.1 |
| 正态方差 | $(n-1)S^2/\sigma_0^2\sim\chi^2_{n-1}$（$\mu$ 已知时 $nS_\mu^2/\sigma_0^2\sim\chi^2_n$） | 5.2.2 |
| 两点分布、Poisson 分布 | 基于 $\sum X_i$ 的随机化检验；$n$ 大时 $U$、$U_0\overset{\cdot}{\sim}\mathcal{N}(0,1)$ | 5.2.3，5.2.6 |
| 两个均值，方差相等 | $T=(\bar X-\bar Y-\mu_0)/(S_p\sqrt{1/m+1/n})\sim t_{m+n-2}$ | 5.2.4 |
| 两个均值，方差不等 | Welch $T_*\overset{\cdot}{\sim}t_r$；大样本 $U^*\overset{\cdot}{\sim}\mathcal{N}(0,1)$ | 5.2.4，5.2.6 |
| 成对数据 | 对差值作单样本 $t$ 检验 | 5.2.4 |
| 两个方差 | $F=S_Y^2/S_X^2\sim F_{n-1,m-1}$ | 5.2.5 |
| 一般情形 | 似然比，$-2\log\lambda\overset{\cdot}{\sim}\chi^2_{k-s}$ | 5.3 |
| 回归系数、整个模型 | $T_j\sim t_{n-p-1}$；$F\sim F_{p,n-p-1}$ | 5.6 |

- Neyman–Pearson 框架把第一类错误控制在水平 $\alpha$ 之下并使功效最大；拒绝是可靠的，接受则不然，因此 $H_0$ 必须慎重选取。$p$ 值是数据拒绝 $H_0$ 的最小显著性水平。
- 似然比检验是通用的方法；经典的正态理论检验都是似然比检验，Wilks 定理给出大样本近似。
- Neyman–Pearson 引理给出简单假设的 MP 检验；在具有单调似然比的分布族（特别是单参数指数族）中，单侧问题存在 UMP 检验，双侧问题一般不存在，此时改用无偏检验。
- $1-\alpha$ 置信域是水平 $\alpha$ 的检验不拒绝的参数值的集合，反之亦然。
