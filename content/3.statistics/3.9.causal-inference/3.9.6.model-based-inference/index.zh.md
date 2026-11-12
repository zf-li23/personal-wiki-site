---
title: 完全随机化实验的基于模型的推断
description: 完全随机化实验中缺失潜在结果的 Bayes 模型插补。三项输入（分配机制、潜在结果的模型、先验）与得到有限样本平均效应后验分布的四个步骤；为什么随机化使分配机制可以略去；对六个 NSW 单元的正态模型与 Bernoulli–Beta 模型的解析例子；潜在结果之间不可识别的相关、协变量、Monte Carlo 实现、超总体效应，以及 NSW 职业培训数据的四个模型。
source_hash: 9b87a2b89fac
---

[3.9.1](/3.9.1) 的 Neyman–Rubin 框架是陈述因果问题的语言：它定义了单元、潜在结果与估计目标，[3.9.2](/3.9.2) 又补充了数据是如何收集的。但它并不规定推断方法。Fisher 检验、Neyman 估计量和回归（[3.9.3](/3.9.3)–[3.9.5](/3.9.5)）是建立在其上的三种方法；本章介绍第四种，它把因果推断直接看作缺失数据问题。有限样本中的每个因果估计目标，都是观测结果与缺失潜在结果的函数。对潜在结果建立统计模型，再配上参数的先验分布，就得到缺失结果的后验预测分布，从而得到任何估计目标的后验分布。这一方法是 Bayes 方法，以 [3.7](/3.7) 的一般理论为基础，这里只回顾所需的部分。与前面的方法相比，它更灵活，因为任何估计目标（分位数效应、受益单元的比例）都可以用同样的方式处理；它也更明确地表达其假定，因为一切都建立在模型之上。

## 6.1. 动机：插补缺失的结果

### 6.1.1. NSW 数据

全国扶持就业（NSW）示范项目是针对在劳动力市场上处境十分不利的男性的职业培训项目；LaLonde（1986）分析了它的实验数据。这里使用的样本有 $N = 445$ 名男性，其中 $N_{\mathrm{t}} = 185$ 人被完全随机化设计分配到培训项目，$N_{\mathrm{c}} = 260$ 人被分配到无积极处理。结果为 1978 年的收入（单位：千美元），分配之前记录了七个协变量：年龄、受教育年限、婚姻状况、是否没有高中学历、种族（黑人）以及 1974 年与 1975 年的收入。许多人在 1978 年完全没有收入，所以结果在零处有很大的质量，并且右尾很长，这一点对模型的选择很重要（6.8 节）。

前几章的估计量给出培训对 1978 年收入的效应：$\hat\tau^{\mathrm{dif}} = 1.79$，Neyman 标准误为 $0.67$；调整协变量的回归估计为 $1.67$，标准误为 $0.64$。

### 6.1.2. 作为缺失结果的函数的估计目标

前六个观测是本章的运行示例。

| 单元 | $Y_i(0)$ | $Y_i(1)$ | $W_i$ | $Y_i^{\mathrm{obs}}$ |
|---|---|---|---|---|
| 1 | 0 | ? | 0 | 0 |
| 2 | ? | 9.9 | 1 | 9.9 |
| 3 | 12.4 | ? | 0 | 12.4 |
| 4 | ? | 3.6 | 1 | 3.6 |
| 5 | 0 | ? | 0 | 0 |
| 6 | ? | 24.9 | 1 | 24.9 |

有限样本平均效应为 $\tau_{\mathrm{fs}} = \frac{1}{6}\sum_{i=1}^{6}(Y_i(1) - Y_i(0))$。由于 $W_i = 1$ 时 $Y_i(1) = Y_i^{\mathrm{obs}}$，$W_i = 0$ 时 $Y_i(1) = Y_i^{\mathrm{mis}}$，$Y_i(0)$ 则相反，

$$
\tau_{\mathrm{fs}} = \tilde\tau\bigl(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{Y}^{\mathrm{mis}}, \boldsymbol{W}\bigr) = \frac{1}{N}\sum_{i=1}^{N}(2W_i - 1)\bigl(Y_i^{\mathrm{obs}} - Y_i^{\mathrm{mis}}\bigr).
$$
给定 $\boldsymbol{Y}^{\mathrm{obs}}$ 与 $\boldsymbol{W}$，唯一未知的是 $\boldsymbol{Y}^{\mathrm{mis}}$。任何能在给定数据时给出 $\boldsymbol{Y}^{\mathrm{mis}}$ 的分布的方法，都能给出 $\tau_{\mathrm{fs}}$ 的分布。关键问题是如何插补缺失的结果。

### 6.1.3. 两种朴素的插补

*按组均值插补。* 把每个缺失的 $Y_i(0)$ 换成对照组均值 $\bar Y_{\mathrm{c}}^{\mathrm{obs}} = (0 + 12.4 + 0)/3 = 4.13$，把每个缺失的 $Y_i(1)$ 换成处理组均值 $\bar Y_{\mathrm{t}}^{\mathrm{obs}} = (9.9 + 3.6 + 24.9)/3 = 12.8$。补全后的数据给出 $\hat\tau = 12.8 - 4.13 = 8.67$，它恰是 $\hat\tau^{\mathrm{dif}}$。但这一插补机制是退化的：对对照单元 $\mathbb{P}(Y_i^{\mathrm{mis}} = 12.8 \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}) = 1$。它把缺失值当作毫无不确定性地填入，因而不给出任何精度的度量。

*按经验分布插补。* 对每个对照单元，以各 $1/3$ 的概率从三个观测到的处理结果 $\{9.9, 3.6, 24.9\}$ 中抽取 $Y_i(1)$；对每个处理单元，从 $\{0, 12.4, 0\}$ 中抽取 $Y_i(0)$。这样得到 $3^6 = 729$ 个等可能的补全数据集，以及 $\tau_{\mathrm{fs}}$ 的一个分布。它承认了结果围绕各组均值的变异，但把三个观测的经验分布当作潜在结果的真实分布，忽略了关于该分布本身的不确定性——每组只有三个观测时，这一不确定性是很大的。

两个问题都要求：(1) 对潜在结果的产生方式建立更灵活的模型，其参数本身也是不确定的；(2) 用系统的方法把这种不确定性传递到 $\boldsymbol{Y}^{\mathrm{mis}}$。Bayes 推断同时提供了这两点。

## 6.2. Bayes 推断简介

Bayes 推断把所有未知量，包括参数，都看作随机变量。它的要素是**先验分布** $p(\theta)$、抽样分布即**似然函数** $p(y \mid \theta)$、联合分布 $p(y, \theta) = p(\theta)p(y \mid \theta)$，以及由 Bayes 定理给出的**后验分布**

$$
p(\theta \mid y) = \frac{p(\theta)p(y \mid \theta)}{\int p(\theta)p(y \mid \theta)\,\mathrm{d}\theta} \propto p(\theta)p(y \mid \theta).
$$
对给定 $\theta$ 时与 $y$ 条件独立的新量或未观测量 $\tilde y$，预测使用**后验预测分布** $p(\tilde y \mid y) = \int p(\tilde y \mid \theta)p(\theta \mid y)\,\mathrm{d}\theta$，它对 $\theta$ 的后验不确定性取平均。Laplace 用于巴黎男婴出生比例的、带均匀先验的二项模型见[例 1.4.1](/3.7.1#ex-1.4.1)；$n$ 次试验中有 $y$ 次成功、先验为 $\mathrm{Beta}(\alpha, \beta)$ 时，后验为 $\mathrm{Beta}(\alpha + y, \beta + n - y)$，这是**共轭先验**的情形。

还需要两点推广。其一，数据可能只被部分观测，$y = (y^{\mathrm{obs}}, y^{\mathrm{mis}})$；此时观测数据的似然为 $p(y^{\mathrm{obs}} \mid \theta) = \int p(y^{\mathrm{obs}}, y^{\mathrm{mis}} \mid \theta)\,\mathrm{d}y^{\mathrm{mis}}$，缺失数据有后验预测分布 $p(y^{\mathrm{mis}} \mid y^{\mathrm{obs}}) = \int p(y^{\mathrm{mis}} \mid y^{\mathrm{obs}}, \theta)p(\theta \mid y^{\mathrm{obs}})\,\mathrm{d}\theta$。其二，我们可能只关心未知量的某些函数，其余的是**讨厌参数**，从联合后验中积分掉。在因果推断中，缺失的潜在结果扮演 $y^{\mathrm{mis}}$ 的角色，结果模型的参数是讨厌参数，所关心的量是估计目标 $\tau$。

Bayes 方法回答了研究者通常提出的问题（"效应为正的概率是多少？"），以有原则的方式合并多个来源的信息，并通过模拟处理复杂模型。它主要的争议点是先验的选择。下面的应用中先验都很弱，样本信息占主导。

## 6.3. 无相关、无协变量的理论

### 6.3.1. 三项输入与目标

**定义 6.3.1（基于模型的插补）** 因果估计目标 $\tau = \tau(\boldsymbol{Y}(0), \boldsymbol{Y}(1), \boldsymbol{X}, \boldsymbol{W})$ 的**基于模型的插补**，由三项输入推导其后验分布 $f(\tau \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}, \boldsymbol{X})$：

1. 分配机制 $\mathbb{P}(\boldsymbol{W} \mid \boldsymbol{X}, \boldsymbol{Y}(0), \boldsymbol{Y}(1))$，在 CRE 中对每个 $\boldsymbol{W} \in \mathcal{W}^+$ 都是 $\binom{N}{N_{\mathrm{t}}}^{-1}$；
2. 给定参数 $\theta$ 时潜在结果的模型 $f(\boldsymbol{Y}(0), \boldsymbol{Y}(1) \mid \boldsymbol{X}, \theta)$；
3. 先验分布 $p(\theta)$；

具体做法是计算 $\boldsymbol{Y}^{\mathrm{mis}}$ 的后验预测分布，并通过 $\tau = \tilde\tau(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{Y}^{\mathrm{mis}}, \boldsymbol{W})$ 对其作变换。

:::

潜在结果的模型通常由单元的可交换性在 [de Finetti 定理](/3.7.6#thm-6.3.1)的意义下构造：如果单元的标号不携带信息，联合分布可以写成独立同分布模型的混合，

$$
f\bigl(\boldsymbol{Y}(0), \boldsymbol{Y}(1) \mid \theta\bigr) = \prod_{i=1}^{N} f\bigl(Y_i(0), Y_i(1) \mid \theta\bigr),
$$
其中混合分布就是先验 $p(\theta)$。本节没有协变量，且给定 $\theta$ 时两个潜在结果独立：$f(Y_i(0), Y_i(1) \mid \theta) = f_{\mathrm{c}}(Y_i(0) \mid \theta_{\mathrm{c}})f_{\mathrm{t}}(Y_i(1) \mid \theta_{\mathrm{t}})$，$\theta = (\theta_{\mathrm{c}}, \theta_{\mathrm{t}})$。6.4 节讨论这一选择的含义。

### 6.3.2. 四个步骤

目标 $f(\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W})$ 分四步到达。

| 步骤 | 计算 | 公式 |
|---|---|---|
| 1 | 给定 $\theta$ 时缺失结果的条件分布 | $f(\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}, \theta) = \dfrac{f(\boldsymbol{Y}^{\mathrm{mis}}, \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta)}{\int f(\boldsymbol{y}^{\mathrm{mis}}, \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta)\,\mathrm{d}\boldsymbol{y}^{\mathrm{mis}}}$ |
| 2 | 参数的后验 | $p(\theta \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}) = \dfrac{p(\theta)f(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta)}{\int p(\theta)f(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta)\,\mathrm{d}\theta}$ |
| 3 | 缺失结果的后验预测分布 | $f(\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}) = \int f(\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}, \theta)\,p(\theta \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W})\,\mathrm{d}\theta$ |
| 4 | 估计目标的后验 | 在步骤 3 的分布下 $\tilde\tau(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{Y}^{\mathrm{mis}}, \boldsymbol{W})$ 的分布 |

这里 $f(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta) = \int f(\boldsymbol{y}^{\mathrm{mis}}, \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta)\,\mathrm{d}\boldsymbol{y}^{\mathrm{mis}}$ 是观测数据的似然，给定 $\theta$ 时所有量的联合分布为 $f(\boldsymbol{Y}(0), \boldsymbol{Y}(1), \boldsymbol{W} \mid \theta) = \mathbb{P}(\boldsymbol{W} \mid \boldsymbol{Y}(0), \boldsymbol{Y}(1))\,f(\boldsymbol{Y}(0), \boldsymbol{Y}(1) \mid \theta)$，并改用 $(\boldsymbol{Y}^{\mathrm{mis}}, \boldsymbol{Y}^{\mathrm{obs}})$ 重新写出；一旦 $\boldsymbol{W}$ 固定，它就是 $(\boldsymbol{Y}(0), \boldsymbol{Y}(1))$ 的一一对应的重新标记。

**定理 6.3.1** 设分配机制是无混杂的，且不依赖于 $\theta$（特别地，CRE 即是如此）。则分配机制在步骤 1 与 2 中消去：

$$
f(\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}, \theta) = \frac{f(\boldsymbol{Y}(0), \boldsymbol{Y}(1) \mid \theta)}{\int f(\boldsymbol{Y}(0), \boldsymbol{Y}(1) \mid \theta)\,\mathrm{d}\boldsymbol{Y}^{\mathrm{mis}}}, \qquad
p(\theta \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}) \propto p(\theta)\int f(\boldsymbol{Y}(0), \boldsymbol{Y}(1) \mid \theta)\,\mathrm{d}\boldsymbol{Y}^{\mathrm{mis}}.
$$
若进一步，给定 $\theta$ 时各单元独立同分布且潜在结果独立，则给定 $(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}, \theta)$ 时缺失结果相互独立，对照单元有 $Y_i^{\mathrm{mis}} \sim f_{\mathrm{t}}(\cdot \mid \theta_{\mathrm{t}})$，处理单元有 $Y_i^{\mathrm{mis}} \sim f_{\mathrm{c}}(\cdot \mid \theta_{\mathrm{c}})$，且似然为

$$
f(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta) \propto \prod_{i: W_i = 0}f_{\mathrm{c}}\bigl(Y_i^{\mathrm{obs}} \mid \theta_{\mathrm{c}}\bigr)\prod_{i: W_i = 1}f_{\mathrm{t}}\bigl(Y_i^{\mathrm{obs}} \mid \theta_{\mathrm{t}}\bigr).
$$

**证明** 对无混杂机制，$\mathbb{P}(\boldsymbol{W} \mid \boldsymbol{Y}(0), \boldsymbol{Y}(1)) = \mathbb{P}(\boldsymbol{W})$ 不涉及潜在结果，并且按假定也不涉及 $\theta$。因此它在步骤 1 的分子与分母中是约去的常数因子，在步骤 2 的似然 $f(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta)$ 中是被吸收进归一化常数的常数因子。这给出所显示的两个公式。在潜在结果独立且单元独立同分布时，$f(\boldsymbol{Y}(0), \boldsymbol{Y}(1) \mid \theta)$ 是各单元 $f_{\mathrm{c}}(Y_i(0) \mid \theta_{\mathrm{c}})f_{\mathrm{t}}(Y_i(1) \mid \theta_{\mathrm{t}})$ 的乘积。对对照单元，第一个因子是 $f_{\mathrm{c}}(Y_i^{\mathrm{obs}} \mid \theta_{\mathrm{c}})$，第二个是 $f_{\mathrm{t}}(Y_i^{\mathrm{mis}} \mid \theta_{\mathrm{t}})$，处理单元则相反。对 $\boldsymbol{Y}^{\mathrm{mis}}$ 积分时，每个含缺失结果的因子积分为一，得到似然；用似然去除乘积，剩下 $\prod_{W_i = 0}f_{\mathrm{t}}(Y_i^{\mathrm{mis}} \mid \theta_{\mathrm{t}})\prod_{W_i = 1}f_{\mathrm{c}}(Y_i^{\mathrm{mis}} \mid \theta_{\mathrm{c}})$，即所述的条件分布。$\square$

该定理是前面各章中随机化作用的 Bayes 对应：设计不需要建模，因为它不携带关于潜在结果的信息。对任何可忽略的机制（[3.9.2](/3.9.2)）同样的结论成立，这就是基于模型的插补在无混杂性下可以推广到观察性研究的原因。此外，若 $\theta_{\mathrm{c}}$ 与 $\theta_{\mathrm{t}}$ 的先验独立，则似然可分解，后验也可分解：$\theta_{\mathrm{c}}$ 只从对照单元学习，$\theta_{\mathrm{t}}$ 只从处理单元学习。

### 6.3.3. 六个单元的正态例子

**例 6.3.1** 对 6.1.2 节的六个 NSW 单元，取模型与先验

$$
\begin{pmatrix} Y_i(0) \\ Y_i(1) \end{pmatrix} \Bigm| \theta \sim \mathcal{N}\left(\begin{pmatrix} \mu_{\mathrm{c}} \\ \mu_{\mathrm{t}} \end{pmatrix}, \begin{pmatrix} 100 & 0 \\ 0 & 64 \end{pmatrix}\right), \qquad
\begin{pmatrix} \mu_{\mathrm{c}} \\ \mu_{\mathrm{t}} \end{pmatrix} \sim \mathcal{N}\left(\begin{pmatrix} 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 10\,000 & 0 \\ 0 & 10\,000 \end{pmatrix}\right),
$$
即 $\theta = (\mu_{\mathrm{c}}, \mu_{\mathrm{t}})$，结果的标准差 $\sigma_{\mathrm{c}} = 10$ 与 $\sigma_{\mathrm{t}} = 8$ 已知，先验非常弥散。求 $\tau_{\mathrm{fs}}$ 的后验。

*步骤 1。* 由定理 6.3.1，给定 $\theta$ 时缺失结果是独立正态：对对照单元 $i = 1, 3, 5$，$Y_i^{\mathrm{mis}} \sim \mathcal{N}(\mu_{\mathrm{t}}, 64)$；对处理单元 $i = 2, 4, 6$，$Y_i^{\mathrm{mis}} \sim \mathcal{N}(\mu_{\mathrm{c}}, 100)$。写成向量形式，$\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}, \theta \sim \mathcal{N}\bigl((\mu_{\mathrm{t}}, \mu_{\mathrm{c}}, \mu_{\mathrm{t}}, \mu_{\mathrm{c}}, \mu_{\mathrm{t}}, \mu_{\mathrm{c}})^{\mathsf T}, \operatorname{diag}(64, 100, 64, 100, 64, 100)\bigr)$。

*步骤 2。* 似然可分解，每个均值都有正态先验与方差已知的正态数据，这是 [3.7.2](/3.7.2) 的共轭情形。$\mu_{\mathrm{c}}$ 的后验精度为 $N_{\mathrm{c}}/\sigma_{\mathrm{c}}^2 + 1/10\,000 = 0.0301$，后验均值为 $\bar Y_{\mathrm{c}}^{\mathrm{obs}} \cdot \frac{N_{\mathrm{c}} \cdot 10\,000}{N_{\mathrm{c}} \cdot 10\,000 + 100} = 4.12$；$\mu_{\mathrm{t}}$ 同理，为 $\bar Y_{\mathrm{t}}^{\mathrm{obs}} \cdot \frac{N_{\mathrm{t}} \cdot 10\,000}{N_{\mathrm{t}} \cdot 10\,000 + 64} = 12.77$。因此

$$
\begin{pmatrix} \mu_{\mathrm{c}} \\ \mu_{\mathrm{t}} \end{pmatrix} \Bigm| \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \sim \mathcal{N}\left(\begin{pmatrix} 4.12 \\ 12.77 \end{pmatrix}, \begin{pmatrix} 5.76^2 & 0 \\ 0 & 4.61^2 \end{pmatrix}\right),
$$
方差为 $33.2$ 与 $21.3$。弥散先验把均值向零收缩的程度可以忽略。

*步骤 3。* 对对照单元写 $Y_i^{\mathrm{mis}} = \mu_{\mathrm{t}} + e_i$，对处理单元写 $\mu_{\mathrm{c}} + e_i$，其中 $e_i$ 是独立的正态误差，与 $\theta$ 独立。给定数据时，$(\mu_{\mathrm{c}}, \mu_{\mathrm{t}}, e_1, \dots, e_6)$ 联合正态，所以作为其线性函数的 $\boldsymbol{Y}^{\mathrm{mis}}$ 服从多元正态分布（[定理 15.3.2](/3.1.15#thm-15.3.2)）。不需要积分：只要求出它的均值与协方差矩阵。由全期望公式与全协方差公式，

$$
\mathbb{E}\bigl[Y_i^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}\bigr] = W_i \cdot 4.12 + (1 - W_i) \cdot 12.77,
$$
$$
\operatorname{Var}\bigl(Y_i^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}\bigr) = \mathbb{E}\bigl[\operatorname{Var}(Y_i^{\mathrm{mis}} \mid \cdot, \theta)\bigr] + \operatorname{Var}\bigl(\mathbb{E}[Y_i^{\mathrm{mis}} \mid \cdot, \theta]\bigr) = \begin{cases} 64 + 21.3 = 85.3, & W_i = 0,\\ 100 + 33.2 = 133.2, & W_i = 1, \end{cases}
$$
而 $\operatorname{Cov}(Y_i^{\mathrm{mis}}, Y_{i'}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W})$ 在两者都是对照单元时为 $21.3$（它们共享不确定的 $\mu_{\mathrm{t}}$），都是处理单元时为 $33.2$，其余情形为 $0$。于是

$$
\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \sim \mathcal{N}\left(\begin{pmatrix} 12.8 \\ 4.1 \\ 12.8 \\ 4.1 \\ 12.8 \\ 4.1 \end{pmatrix}, \begin{bmatrix}
85.3 & 0 & 21.3 & 0 & 21.3 & 0\\
0 & 133.2 & 0 & 33.2 & 0 & 33.2\\
21.3 & 0 & 85.3 & 0 & 21.3 & 0\\
0 & 33.2 & 0 & 133.2 & 0 & 33.2\\
21.3 & 0 & 21.3 & 0 & 85.3 & 0\\
0 & 33.2 & 0 & 33.2 & 0 & 133.2
\end{bmatrix}\right).
$$

*步骤 4。* $\tau_{\mathrm{fs}} = \frac{1}{6}\bigl[(Y_1^{\mathrm{mis}} + Y_3^{\mathrm{mis}} + Y_5^{\mathrm{mis}}) - 12.4 + 38.4 - (Y_2^{\mathrm{mis}} + Y_4^{\mathrm{mis}} + Y_6^{\mathrm{mis}})\bigr]$ 是 $\boldsymbol{Y}^{\mathrm{mis}}$ 的线性函数，因而是正态的，均值为 $\frac{1}{6}(3 \cdot 12.77 + 26.0 - 3 \cdot 4.12) = 8.66$。三个缺失 $Y(1)$ 之和的方差为 $3 \cdot 85.3 + 6 \cdot 21.3 = 383.6$，三个缺失 $Y(0)$ 之和的方差为 $3 \cdot 133.2 + 6 \cdot 33.2 = 598.8$，两个和相互独立，所以 $\operatorname{Var}(\tau_{\mathrm{fs}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}) = (383.6 + 598.8)/36 = 27.3$：

$$
\tau_{\mathrm{fs}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \sim \mathcal{N}(8.7, 5.2^2).
$$
后验均值基本就是 $\hat\tau^{\mathrm{dif}} = 8.67$，而后验标准差 $5.2$ 现在同时反映了结果的变异与关于其均值的不确定性。

### 6.3.4. 二值的例子

**例 6.3.2** 设结果为二值，$Y_i(0) \mid \theta \sim \mathrm{Ber}(\pi_{\mathrm{c}})$ 与 $Y_i(1) \mid \theta \sim \mathrm{Ber}(\pi_{\mathrm{t}})$ 独立，$\theta = (\pi_{\mathrm{c}}, \pi_{\mathrm{t}})$，先验独立：$\pi_{\mathrm{c}} \sim \mathrm{Beta}(a_{\mathrm{c}}, b_{\mathrm{c}})$，$\pi_{\mathrm{t}} \sim \mathrm{Beta}(a_{\mathrm{t}}, b_{\mathrm{t}})$。在 CRE 中，$Y^{\mathrm{obs}} = 1$ 的处理单元有 $y_{\mathrm{t}} = \sum_{W_i = 1}Y_i^{\mathrm{obs}}$ 个，对照单元有 $y_{\mathrm{c}} = \sum_{W_i = 0}Y_i^{\mathrm{obs}}$ 个。推导 $\tau_{\mathrm{fs}}$ 的后验，并在 $N_{\mathrm{t}} = N_{\mathrm{c}} = 5$、$y_{\mathrm{t}} = 4$、$y_{\mathrm{c}} = 2$ 与均匀先验下求值。

*步骤 1。* 给定 $\theta$，对照单元缺失的 $Y_i(1)$ 独立同分布于 $\mathrm{Ber}(\pi_{\mathrm{t}})$，处理单元缺失的 $Y_i(0)$ 独立同分布于 $\mathrm{Ber}(\pi_{\mathrm{c}})$。对 $\tau_{\mathrm{fs}}$ 只有它们的和起作用：$M_1 = \sum_{W_i = 0}Y_i^{\mathrm{mis}} \mid \theta \sim \mathrm{Bin}(N_{\mathrm{c}}, \pi_{\mathrm{t}})$，$M_0 = \sum_{W_i = 1}Y_i^{\mathrm{mis}} \mid \theta \sim \mathrm{Bin}(N_{\mathrm{t}}, \pi_{\mathrm{c}})$。

*步骤 2。* 似然为 $\pi_{\mathrm{t}}^{y_{\mathrm{t}}}(1 - \pi_{\mathrm{t}})^{N_{\mathrm{t}} - y_{\mathrm{t}}}\pi_{\mathrm{c}}^{y_{\mathrm{c}}}(1 - \pi_{\mathrm{c}})^{N_{\mathrm{c}} - y_{\mathrm{c}}}$，由共轭性，$\pi_{\mathrm{t}} \mid \text{数据} \sim \mathrm{Beta}(a_{\mathrm{t}} + y_{\mathrm{t}}, b_{\mathrm{t}} + N_{\mathrm{t}} - y_{\mathrm{t}})$，$\pi_{\mathrm{c}} \mid \text{数据} \sim \mathrm{Beta}(a_{\mathrm{c}} + y_{\mathrm{c}}, b_{\mathrm{c}} + N_{\mathrm{c}} - y_{\mathrm{c}})$，二者独立。

*步骤 3。* 把二项分布对 Beta 后验积分，得到 **Beta-二项分布**：

$$
M_1 \mid \text{数据} \sim \mathrm{BetaBin}\bigl(N_{\mathrm{c}}, a_{\mathrm{t}} + y_{\mathrm{t}}, b_{\mathrm{t}} + N_{\mathrm{t}} - y_{\mathrm{t}}\bigr), \qquad
M_0 \mid \text{数据} \sim \mathrm{BetaBin}\bigl(N_{\mathrm{t}}, a_{\mathrm{c}} + y_{\mathrm{c}}, b_{\mathrm{c}} + N_{\mathrm{c}} - y_{\mathrm{c}}\bigr),
$$
二者独立，其中 $\mathbb{P}(M = m) = \binom{n}{m}\frac{\mathrm{B}(m + \alpha, n - m + \beta)}{\mathrm{B}(\alpha, \beta)}$，均值为 $n\alpha/(\alpha + \beta)$，方差为 $\frac{n\alpha\beta(\alpha + \beta + n)}{(\alpha + \beta)^2(\alpha + \beta + 1)}$。与给定 $\theta$ 时的 Bernoulli 抽样不同，被插补的结果在单元之间是相依的，因为它们共享不确定的 $\pi_{\mathrm{t}}$ 或 $\pi_{\mathrm{c}}$。

*步骤 4。* $\tau_{\mathrm{fs}} = \frac{1}{N}\bigl[(y_{\mathrm{t}} + M_1) - (y_{\mathrm{c}} + M_0)\bigr]$，其分布是两个独立的 Beta-二项变量之差的分布。

在给定数值下，$M_1 \sim \mathrm{BetaBin}(5, 5, 2)$，$M_0 \sim \mathrm{BetaBin}(5, 3, 4)$，所以 $\mathbb{E}[M_1] = 25/7 = 3.57$，$\operatorname{Var}(M_1) = 1.53$，$\mathbb{E}[M_0] = 15/7 = 2.14$，$\operatorname{Var}(M_0) = 1.84$，且

$$
\mathbb{E}[\tau_{\mathrm{fs}} \mid \text{数据}] = \frac{4 + 3.57 - 2 - 2.14}{10} = 0.343, \qquad
\operatorname{sd}(\tau_{\mathrm{fs}} \mid \text{数据}) = \frac{\sqrt{1.53 + 1.84}}{10} = 0.18.
$$
后验是离散的，支撑在 $0.1$ 的整数倍上；对两个概率质量函数的乘积求和，得 $\mathbb{P}(\tau_{\mathrm{fs}} > 0 \mid \text{数据}) = 0.94$。均匀先验的均值为 $1/2$，把后验均值从 $\hat\tau^{\mathrm{dif}} = 0.4$ 向零拉动：每组有五个单元时，先验相当于每组增加了两个观测。

:::

## 6.4. 潜在结果之间的相关

给定 $\theta$ 时 $Y_i(0)$ 与 $Y_i(1)$ 独立，这是一个实质性的假定。更一般的正态模型为

$$
\begin{pmatrix} Y_i(0) \\ Y_i(1) \end{pmatrix} \Bigm| \theta \sim \mathcal{N}\left(\begin{pmatrix} \mu_{\mathrm{c}} \\ \mu_{\mathrm{t}} \end{pmatrix}, \begin{pmatrix} \sigma_{\mathrm{c}}^2 & \rho\sigma_{\mathrm{c}}\sigma_{\mathrm{t}} \\ \rho\sigma_{\mathrm{c}}\sigma_{\mathrm{t}} & \sigma_{\mathrm{t}}^2 \end{pmatrix}\right), \qquad p(\theta) = p(\rho)\,p(\mu_{\mathrm{c}}, \mu_{\mathrm{t}}, \sigma_{\mathrm{c}}^2, \sigma_{\mathrm{t}}^2).
$$
四个步骤不变，只是在步骤 1 中，对照单元缺失的结果现在有条件分布 $\mathcal{N}\bigl(\mu_{\mathrm{t}} + \rho\frac{\sigma_{\mathrm{t}}}{\sigma_{\mathrm{c}}}(Y_i^{\mathrm{obs}} - \mu_{\mathrm{c}}),\ (1 - \rho^2)\sigma_{\mathrm{t}}^2\bigr)$（[定理 15.5.1](/3.1.15#thm-15.5.1)），处理单元对称。

相关系数不同于其他参数。每个单元只通过其观测结果的边缘密度 $f_{\mathrm{c}}$ 或 $f_{\mathrm{t}}$ 对似然起作用，而 $\rho$ 并不出现在其中。因此在 $\rho$ 与其他参数独立的先验下，它的后验与先验完全相同：数据不含关于它的任何信息。这是定理 4.3.2 中已经看到的事实的 Bayes 形式——$S_{\mathrm{tc}}^2$ 无法估计，因为两个潜在结果从不同时被观测。$\tau_{\mathrm{fs}}$ 的后验确实依赖于 $\rho$，分析应当论证 $\rho$ 的选择，或展示一系列取值下的结果。

在六单元的例子中取 $\rho = 1$，即协方差为 $80 = \sqrt{100 \cdot 64}$。此时 $Y_i(1) = \mu_{\mathrm{t}} + 0.8(Y_i(0) - \mu_{\mathrm{c}})$ 严格成立，缺失的结果是观测结果与 $\theta$ 的确定性函数，$\tau_{\mathrm{fs}}$ 成为 $(\mu_{\mathrm{c}}, \mu_{\mathrm{t}})$ 的线性函数，即 $\tau_{\mathrm{fs}} = 1.125\mu_{\mathrm{t}} - 0.9\mu_{\mathrm{c}} - 2.01$。步骤 2 的后验不变，于是

$$
\tau_{\mathrm{fs}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \sim \mathcal{N}\bigl(8.6, 7.3^2\bigr) \quad (\rho = 1), \qquad \text{对比 } \mathcal{N}(8.7, 5.2^2) \quad (\rho = 0).
$$
点估计几乎不变，但不确定性增大了百分之四十。原因是 $\rho = 1$ 时被插补的结果不带有单元层面自己的噪声：每个都是观测结果经不确定参数平移和缩放后的结果，所以 $\mu_{\mathrm{c}}$ 与 $\mu_{\mathrm{t}}$ 的误差沿同一方向进入每一个插补，不会平均掉，系数 $1.125$ 与 $-0.9$ 又将其放大。这与 Neyman 的分析平行：潜在结果完全相关时，$\hat\tau^{\mathrm{dif}}$ 的抽样方差最大（定理 4.3.2）。独立性（$\rho = 0$）是方便的缺省选择，但分析者应当知道它是一种选择，而不是一项发现。

## 6.5. 协变量

协变量通过结果模型进入，例如

$$
Y_i(0) \mid X_i, \theta \sim \mathcal{N}\bigl(X_i\boldsymbol{\beta}_{\mathrm{c}}, \sigma_{\mathrm{c}}^2\bigr), \qquad
Y_i(1) \mid X_i, \theta \sim \mathcal{N}\bigl(X_i\boldsymbol{\beta}_{\mathrm{t}}, \sigma_{\mathrm{t}}^2\bigr),
$$
其中 $X_i$ 含截距，$\theta = (\boldsymbol{\beta}_{\mathrm{c}}, \boldsymbol{\beta}_{\mathrm{t}}, \sigma_{\mathrm{c}}^2, \sigma_{\mathrm{t}}^2)$。步骤相同：在步骤 1 中，对照单元缺失的 $Y_i(1)$ 从处理组回归在该单元自己的协变量处的取值抽取，步骤 2 是一对 Bayes 线性回归。这是 [3.9.5](/3.9.5) 中含交互回归的 Bayes 版本，并有一个额外好处：系数的不确定性被传递到各插补值。方差未知或使用非正态模型时，各步骤不再有闭式解，需要借助模拟。

## 6.6. 用模拟实现

在大多数模型中，步骤 2 与 3 无法解析计算。然而一个分布可以用来自它的大样本来表示：若 $\theta^{(1)}, \dots, \theta^{(S)}$ 是来自 $p(\theta \mid y)$ 的抽样，则 $\mathbb{E}[h(\theta) \mid y] \approx \frac{1}{S}\sum_{s}h(\theta^{(s)})$，由大数定律与中心极限定理，误差为 $S^{-1/2}$ 阶。未知量的任何函数的概率、分位数与密度都可以同样得到。四个步骤于是变成一个循环。

**算法 6.6.1（用模拟实现的基于模型的插补）** 对 $s = 1, \dots, S$：

1. 从后验 $p(\theta \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W})$ 中抽取 $\theta^{(s)}$，可以直接抽取，也可以取 Markov 链的当前状态；
2. 从 $f(\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}, \theta^{(s)})$ 中抽取 $\boldsymbol{Y}^{\mathrm{mis}, (s)}$；
3. 计算 $\tau^{(s)} = \tilde\tau(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{Y}^{\mathrm{mis}, (s)}, \boldsymbol{W})$。

抽样 $\tau^{(1)}, \dots, \tau^{(S)}$ 是来自 $\tau$ 后验的样本。

:::

先抽取 $\theta^{(s)}$、再给定它抽取 $\boldsymbol{Y}^{\mathrm{mis}, (s)}$，就是从二者的联合后验中抽取，所以 $\boldsymbol{Y}^{\mathrm{mis}, (s)}$ 是步骤 3 的边缘分布的一个抽样：对 $\theta$ 的积分是靠模拟完成的。当 $\theta$ 的后验不是标准形式时，步骤 1 使用 **Markov 链 Monte Carlo**（[3.5.9](/3.5.9)）。对方差未知的正态模型，$\theta$ 分成若干块，其完全条件分布是正态（均值）与尺度逆 $\chi^2$（方差），**Gibbs 抽样**依次抽取各块；对非共轭的块，如 logistic 回归的系数，则使用 **Metropolis–Hastings 算法**的一步。把该循环用于六单元的例子，可重现例 6.3.1 的解析后验。

![左：在例 6.3.1 的正态模型下，由算法 6.6.1 对六个 NSW 单元得到的有限样本平均效应的 20 000 个抽样，以及解析的正态后验。右：潜在结果独立（rho = 0）与完全相关（rho = 1）时有限样本效应的解析后验，以及超总体效应的解析后验](./plots/posterior_tau.py)

## 6.7. 超总体效应

对超总体估计目标，插补是不必要的。单元独立同分布时，$\tau_{\mathrm{sp}} = \mathbb{E}[Y_i(1) - Y_i(0) \mid \theta] = \tau(\theta)$ 只是参数的函数，所以它的后验直接由步骤 2 得到。在正态模型中，$\tau_{\mathrm{sp}} = \mu_{\mathrm{t}} - \mu_{\mathrm{c}}$，对六个单元，

$$
\tau_{\mathrm{sp}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \sim \mathcal{N}\bigl(12.77 - 4.12,\ 21.3 + 33.2\bigr) = \mathcal{N}\bigl(8.7, 7.4^2\bigr).
$$
后验标准差 $7.4$ 大于 $\tau_{\mathrm{fs}}$（$\rho = 0$）的 $5.2$。原因与 Neyman 方法中定理 4.6.1 发现的相同：有限样本效应有一部分是被观测到的，因为每个单元的两个潜在结果中有一个是已知的，而总体效应还必须考虑单元的抽样。若对 $\tau_{\mathrm{sp}}$ 使用算法 6.6.1 的模拟，则可以省去步骤 2，取 $\tau^{(s)} = \tau(\theta^{(s)})$。

## 6.8. 例：NSW 数据的四个模型

对完整的 NSW 数据拟合了四个模型，回归参数或均值参数各取独立的正态先验 $\mathcal{N}(0, 100^2)$，方差取尺度逆 $\chi^2$ 先验 $\mathrm{Inv}\text{-}\chi^2(2, 0.1^2)$（收入以千美元计），使数据起主导作用：

| 模型 | 均值依赖协变量 | 方差随处理而异 | 潜在结果独立 | 两部分模型 |
|---|---|---|---|---|
| $M_1$：正态，方差相同 | 否 | 否 | 否 | 否 |
| $M_2$：正态 | 否 | 是 | 是 | 否 |
| $M_3$：正态回归 | 是 | 是 | 是 | 否 |
| $M_4$：零膨胀对数正态回归 | 是 | 是 | 是 | 是 |

模型 $M_4$ 把收入看作两部分的结果：对收入为正的概率作 logistic 回归，对收入为正者的对数收入作正态线性回归，两个潜在结果各自分别建模。模型 $M_1$–$M_3$ 有共轭的完全条件分布，用 Gibbs 抽样拟合；在 $M_4$ 中，logistic 部分用独立 Metropolis–Hastings 步更新，建议分布取以极大似然估计为中心的正态分布，协方差为其估计协方差矩阵的两倍，对数正态部分用 Gibbs 抽样。初值取极大似然估计，每条链的前三分之一作为预烧期舍去。

有限样本效应对均值与四分位数的后验均值（标准差），其中分位数效应是 $N$ 个 $Y_i(1)$ 的分位数与 $N$ 个 $Y_i(0)$ 的分位数之差：

| 模型 | 均值效应 | 0.25 分位数 | 0.50 分位数 | 0.75 分位数 |
|---|---|---|---|---|
| $M_1$ | 1.79 (0.63) | 1.79 (0.63) | 1.79 (0.63) | 1.79 (0.63) |
| $M_2$ | 1.78 (0.49) | 0.63 (0.35) | 1.63 (0.55) | 3.07 (0.64) |
| $M_3$ | 1.57 (0.50) | 0.42 (0.34) | 1.40 (0.55) | 2.89 (0.63) |
| $M_4$ | 1.79 (0.85) | 0.25 (0.30) | 1.03 (0.53) | 1.69 (0.72) |

作为对比，Neyman 估计为 1.79 (0.67)，调整协变量的回归估计为 1.67 (0.64)。

由此得到三点结论。第一，所有模型都一致认为培训使平均收入提高了大约 1.6 至 1.8 千美元。第二，分位数效应强烈依赖于模型：$M_1$ 假定的是正态分布的纯平移，所以每个分位数效应都等于均值效应，而其他模型允许离散程度不同。第三，正态模型对这种许多人收入为零、其余人高度偏斜的结果描述不当；$M_4$ 兼顾了这两个特征，是四个模型中最现实的。它对均值效应给出较大的后验标准差，是偏斜性的诚实后果；它也表明，下四分位数处的效应很小（两组中大多数人收入都很低），而收益集中在分布的上部。基于模型的方法使这类分布型估计目标与均值一样容易估计，前面的方法都做不到这一点。

## 小结

| | Fisher | Neyman | 回归 | 基于模型 |
|---|---|---|---|---|
| 问题 | 有无效应？ | 平均效应 | 含协变量的平均效应 | 通过模型处理任何估计目标 |
| 随机的量 | $\boldsymbol{W}$ | $\boldsymbol{W}$（及抽样） | $\boldsymbol{W}$、抽样 | 一切未观测的量 |
| 输出 | 精确 p 值 | 估计、方差、区间 | 估计、稳健标准误 | 后验分布 |

- 输入：分配机制、模型 $f(Y_i(0), Y_i(1) \mid \theta)$（来自可交换性）与先验 $p(\theta)$（定义 6.3.1）。
- 四步：$f(\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}, \theta)$；$p(\theta \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W})$；对 $\theta$ 积分得到插补分布；变换到 $\tau$。在无混杂的分配下，分配机制消去（定理 6.3.1）。
- 独立的潜在结果：对照单元缺失的 $Y_i(1)$ 从处理组模型抽取，反之亦然；先验独立时，每组的参数由该组学习。
- 正态例子：插补值服从多元正态（共享的参数不确定性导致相关），$\tau_{\mathrm{fs}} \sim \mathcal{N}(8.7, 5.2^2)$；二值例子：被插补的计数服从 Beta-二项分布。
- 潜在结果的相关系数 $\rho$ 不可识别；它的后验等于先验，$\rho = 1$ 给出 $\tau_{\mathrm{fs}}$ 最宽的后验（$7.3$ 对 $5.2$）。
- 模拟（算法 6.6.1）：抽 $\theta$，抽 $\boldsymbol{Y}^{\mathrm{mis}}$，计算 $\tau$；必要时用 MCMC。
- $\tau_{\mathrm{sp}} = \tau(\theta)$ 不需要插补，其后验比 $\tau_{\mathrm{fs}}$ 的更宽（$7.4$ 对 $5.2$），与 Neyman 方法中一致。
- NSW：各模型的均值效应都在 1.8 千美元左右；分位数效应依赖于模型，零膨胀对数正态模型是现实的。

## 思考题

1. 在例 6.3.1 中，设 $\mu_{\mathrm{c}}$ 与 $\mu_{\mathrm{t}}$ 的先验方差趋于无穷。$\tau_{\mathrm{fs}}$ 的极限后验是什么？把它的方差与基于已知结果方差的 Neyman 方差估计作比较。

   **答** 在极限下，后验为 $\mu_{\mathrm{c}} \sim \mathcal{N}(\bar Y_{\mathrm{c}}^{\mathrm{obs}}, \sigma_{\mathrm{c}}^2/N_{\mathrm{c}}) = \mathcal{N}(4.13, 33.3)$，$\mu_{\mathrm{t}} \sim \mathcal{N}(12.8, 21.3)$。$\tau_{\mathrm{fs}}$ 的均值恰为 $\frac{1}{6}(3 \cdot 12.8 - 12.4 + 38.4 - 3 \cdot 4.13) = 8.67 = \hat\tau^{\mathrm{dif}}$。其方差为 $\frac{1}{36}\bigl[N_{\mathrm{c}}\sigma_{\mathrm{t}}^2 + N_{\mathrm{c}}^2\sigma_{\mathrm{t}}^2/N_{\mathrm{t}} + N_{\mathrm{t}}\sigma_{\mathrm{c}}^2 + N_{\mathrm{t}}^2\sigma_{\mathrm{c}}^2/N_{\mathrm{c}}\bigr] = \frac{1}{36}(192 + 192 + 300 + 300) = 27.3$。一般地，记 $N = N_{\mathrm{c}} + N_{\mathrm{t}}$，它等于 $\frac{N_{\mathrm{c}}}{N}\cdot\frac{\sigma_{\mathrm{t}}^2}{N_{\mathrm{t}}} + \frac{N_{\mathrm{t}}}{N}\cdot\frac{\sigma_{\mathrm{c}}^2}{N_{\mathrm{c}}}$，小于 Neyman 方差 $\sigma_{\mathrm{c}}^2/N_{\mathrm{c}} + \sigma_{\mathrm{t}}^2/N_{\mathrm{t}} = 54.7$：这里恰为其一半，因为 $N_{\mathrm{t}} = N_{\mathrm{c}}$。Neyman 方差针对超总体（对比 6.7 节的 $54.5$），$\tau_{\mathrm{fs}}$ 的后验针对有限样本，其中一半的潜在结果是已知的。

2. 证明在 Bernoulli 试验（每个单元独立地以已知概率 $q$ 接受处理）下，$\theta$ 的后验与观测数据相同时 CRE 下的后验一致。

   **答** Bernoulli 分配机制 $\prod_i q^{W_i}(1 - q)^{1 - W_i}$ 不依赖于潜在结果，也不依赖于 $\theta$。在步骤 2 中，它是 $f(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta)$ 的常数因子，正如 CRE 中的 $\binom{N}{N_{\mathrm{t}}}^{-1}$，在归一化时约去。因此两个后验都正比于 $p(\theta)\int f(\boldsymbol{Y}(0), \boldsymbol{Y}(1) \mid \theta)\,\mathrm{d}\boldsymbol{Y}^{\mathrm{mis}}$（定理 6.3.1）。

3. 给出一个使定理 6.3.1 不成立的分配机制，并解释出了什么问题。

   **答** 例 2.2.3：单元效应较大的单元接受处理。此时 $\mathbb{P}(\boldsymbol{W} \mid \boldsymbol{Y}(0), \boldsymbol{Y}(1))$ 是依赖于缺失结果的示性函数，不能在步骤 1 中约去：观测到的分配告诉我们缺失结果满足一个不等式，忽略这一点的插补会抽取与设计不相容的值。等价地，处理单元不是总体的随机样本，所以不能用处理组模型为对照单元插补 $Y_i(1)$。

4. （二值结果）在 $N_{\mathrm{t}} = N_{\mathrm{c}} = 4$ 的 CRE 中，三个处理单元与一个对照单元的结果为 $1$。取 $\mathrm{Beta}(1, 1)$ 先验与独立的潜在结果，求若接受处理则结果为 $1$ 的对照单元个数 $M_1$ 的后验分布，以及 $\tau_{\mathrm{fs}}$ 的后验均值。

   **答** $\pi_{\mathrm{t}} \mid \text{数据} \sim \mathrm{Beta}(4, 2)$，所以 $M_1 \sim \mathrm{BetaBin}(4, 4, 2)$，$\mathbb{P}(M_1 = m) = \binom{4}{m}\mathrm{B}(m + 4, 6 - m)/\mathrm{B}(4, 2)$。$\mathrm{B}(4, 2) = 1/20$，例如 $\mathbb{P}(M_1 = 4) = 20\,\mathrm{B}(8, 2) = 20/72 = 0.278$，$\mathbb{P}(M_1 = 0) = 20\,\mathrm{B}(4, 6) = 20/504 = 0.040$；$M_1 = 0, 1, \dots, 4$ 的完整分布为 $0.040, 0.127, 0.238, 0.317, 0.278$。其均值为 $\mathbb{E}[M_1] = 4 \cdot 4/6 = 2.67$；类似地 $\pi_{\mathrm{c}} \sim \mathrm{Beta}(2, 4)$，$\mathbb{E}[M_0] = 4 \cdot 2/6 = 1.33$。于是 $\mathbb{E}[\tau_{\mathrm{fs}}] = \frac{1}{8}(3 + 2.67 - 1 - 1.33) = 0.417$，对比 $\hat\tau^{\mathrm{dif}} = 0.75 - 0.25 = 0.5$。

5. 解释为什么在 6.4 节的模型中 $\rho$ 的后验等于其先验，以及为什么这并不使 $\rho$ 无关紧要。

   **答** 每个单元对观测数据似然的贡献，是其唯一被观测的潜在结果的边缘密度；在二元正态分布中，边缘只依赖于 $(\mu_{\mathrm{c}}, \sigma_{\mathrm{c}}^2)$ 或 $(\mu_{\mathrm{t}}, \sigma_{\mathrm{t}}^2)$。所以似然对 $\rho$ 是常数，而 $\rho$ 先验上与其他参数独立，Bayes 定理返回先验。但缺失结果对观测结果的条件分布依赖于 $\rho$（步骤 1），所以 $\tau_{\mathrm{fs}}$ 的后验，以及任何涉及联合分布的估计目标（如 $Y_i(1) > Y_i(0)$ 的单元所占的比例）的后验，都依赖于它。数据无法解决这个问题；分析者必须为某个值提供论据，或报告敏感性分析。

6. 对正态模型中的超总体估计目标，为什么不需要插补？对例 6.3.1 证明 $\tau_{\mathrm{sp}}$ 的后验方差减去 $\tau_{\mathrm{fs}}$ 的后验方差（$\rho = 0$）为正，并解释这个差。

   **答** $\tau_{\mathrm{sp}} = \mu_{\mathrm{t}} - \mu_{\mathrm{c}}$ 只是 $\theta$ 的函数，所以其后验由步骤 2 得到。两个方差为 $54.5$ 与 $27.3$，差为 $27.2 > 0$。把 $\tau_{\mathrm{fs}}$ 写成 $\frac{1}{N}\sum_i(Y_i(1) - Y_i(0))$，其中一半的项涉及观测值，给定数据时它们是固定的，另一半是被插补的，方差来自 $\theta$ 与单元层面的噪声两方面。$\tau_{\mathrm{sp}}$ 涉及整个总体，其中没有任何部分由数据固定。这个差对应于定理 4.6.1 中把有限样本方差与超总体方差分开的项 $\sigma_{\mathrm{tc}}^2/N$。

7. 写出 6.8 节中模型 $M_2$（独立正态，随处理而异的方差，先验 $\mu_w \sim \mathcal{N}(0, \omega^2)$ 与 $\sigma_w^2 \sim \mathrm{Inv}\text{-}\chi^2(M, S_0^2)$）的 Gibbs 抽样器，包括 $\tau_{\mathrm{fs}}$ 的插补步骤。

   **答** 对 $w \in \{\mathrm{c}, \mathrm{t}\}$，设 $w$ 组有 $N_w$ 个单元，均值为 $\bar Y_w^{\mathrm{obs}}$：(1) 抽取 $\mu_w \mid \sigma_w^2 \sim \mathcal{N}\Bigl(\frac{N_w\bar Y_w^{\mathrm{obs}}/\sigma_w^2}{N_w/\sigma_w^2 + 1/\omega^2}, \frac{1}{N_w/\sigma_w^2 + 1/\omega^2}\Bigr)$；(2) 从 $\mathrm{Inv}\text{-}\chi^2\Bigl(M + N_w, \frac{MS_0^2 + \sum_{i \in w}(Y_i^{\mathrm{obs}} - \mu_w)^2}{M + N_w}\Bigr)$ 中抽取 $\sigma_w^2 \mid \mu_w$，即 $\bigl(MS_0^2 + \sum_{i \in w}(Y_i^{\mathrm{obs}} - \mu_w)^2\bigr)/\sigma_w^2 \sim \chi^2_{M + N_w}$；两组在条件上独立。(3) 对对照单元插补 $Y_i^{\mathrm{mis}} \sim \mathcal{N}(\mu_{\mathrm{t}}, \sigma_{\mathrm{t}}^2)$，对处理单元插补 $\mathcal{N}(\mu_{\mathrm{c}}, \sigma_{\mathrm{c}}^2)$；(4) 计算 $\tau_{\mathrm{fs}} = \frac{1}{N}\sum_i(2W_i - 1)(Y_i^{\mathrm{obs}} - Y_i^{\mathrm{mis}})$。重复，并舍去预烧期。

8. 为什么零膨胀对数正态模型更适合 NSW 数据，以及它为什么可能对下四分位数给出相当不同的效应？

   **答** 相当大一部分男性（处理组约四分之一，对照组约三分之一）在 1978 年收入为零，而正的收入强烈右偏。正态模型给负收入赋予正概率，给恰为零的收入赋予零概率，并且把所有分位数与均值和方差绑定。两部分模型把培训对"有任何收入"的概率的效应与对收入金额的效应分开。在下四分位数处，两组中许多人无论接受哪种处理都是零收入或很低的收入，所以分位数效应接近于零（$M_4$ 中为 0.25），而正态模型外推出对称的形状并高估了它。
