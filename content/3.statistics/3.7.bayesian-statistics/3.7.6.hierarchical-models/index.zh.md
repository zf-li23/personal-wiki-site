---
title: 层次模型
description: 为什么相关各组的参数应当一起建模；大鼠肿瘤的例子与由历史数据确定先验的问题；无合并、完全合并与部分合并；可交换性与 de Finetti 定理；完全贝叶斯层次模型的结构、超先验与共轭层次模型的三步分析；大鼠肿瘤的 Beta-二项模型，包括超先验的选取、格点计算与收缩；八所学校的正态层次模型，组间标准差的后验，以及对已有组与新组的预测。
source_hash: 5ec0ea82ea71
---

数据常常是分组的：许多实验室实验中的肿瘤数、若干学校的成绩提高、许多医院的结局。每一组有自己的参数 $\theta_j$，各组之间有关联，所以我们对一组了解到的东西也说明了关于其他组的一些情况。把 $\theta_j$ 当作互不相关的，浪费了这些信息，并且当每组数据很少时，分开的估计噪声很大；把它们当作相等的，则忽略了真实的差异。层次模型取其中道：$\theta_j$ 本身抽自一个总体分布，其参数（即超参数）由所有组合在一起来估计。[3.2.7](/3.2.7) 的入门介绍定义了**分层模型**；本章对它作完整的发展。

我们从一个由历史数据构造先验的例子出发（§6.1），并说明为什么完整的模型更好（§6.2）。把各组参数建模为抽自同一分布的概率论依据是可交换性与 de Finetti 定理（§6.3）。然后把一般结构与共轭层次模型的三步方法（§6.4）应用于两个标准例子：总体分布为 Beta 分布的二项数据（§6.5），以及总体分布为正态分布的正态数据（§6.6）。计算把 [3.7.1](/3.7.1)–[3.7.3](/3.7.3) 的共轭结果与 [3.7.5](/3.7.5) 的格点抽样结合起来；[3.7.5](/3.7.5) §5.6 的经验贝叶斯论证是完全贝叶斯分析所取代的非贝叶斯捷径。对这些例子所作的模型检验见 [3.7.7](/3.7.7)，它们的比较见 [3.7.8](/3.7.8)。在实验设计中，同样的结构以随机效应模型的形式出现（[3.8.5](/3.8.5)）。

## 6.1. 动机：一组大鼠的肿瘤风险

**例 6.1.1（大鼠肿瘤）** 在一项关于某药物致癌性的实验室实验中，$n=14$ 只未用药的对照组大鼠出现了 $y=4$ 个某类型的肿瘤。我们想估计这类大鼠发生此类肿瘤的风险 $\theta$。另有 70 次以往实验中同类大鼠对照组的数据（Tarone，1982）：

| $y_j/n_j$ | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| 0/20 | 0/20 | 0/20 | 0/20 | 0/20 | 0/20 | 0/20 | 0/19 | 0/19 | 0/19 |
| 0/19 | 0/18 | 0/18 | 0/17 | 1/20 | 1/20 | 1/20 | 1/20 | 1/19 | 1/19 |
| 1/18 | 1/18 | 2/25 | 2/24 | 2/23 | 2/20 | 2/20 | 2/20 | 2/20 | 2/20 |
| 2/20 | 1/10 | 5/49 | 2/19 | 5/46 | 3/27 | 2/17 | 7/49 | 7/47 | 3/20 |
| 3/20 | 2/13 | 9/48 | 10/50 | 4/20 | 4/20 | 4/20 | 4/20 | 4/20 | 4/20 |
| 4/20 | 10/48 | 4/19 | 4/19 | 4/19 | 5/22 | 11/46 | 12/49 | 5/20 | 5/20 |
| 6/23 | 5/19 | 6/22 | 6/20 | 6/20 | 6/20 | 16/52 | 15/47 | 15/46 | 9/24 |

把当前实验建模为 $y\mid\theta\sim\mathrm{Bin}(14,\theta)$。取 $\mathrm{Beta}(\alpha,\beta)$ 先验，后验为 $\mathrm{Beta}(\alpha+4,\beta+10)$（[3.7.1](/3.7.1)，§1.6.2）；问题是如何选取 $\alpha$ 与 $\beta$，即控制先验形状的**超参数**。

首先想到的是让历史数据来决定它们。假设以往实验的肿瘤概率 $\theta_1,\dots,\theta_{70}$ 与当前实验的 $\theta_{71}=\theta$ 都抽自同一个总体分布 $\mathrm{Beta}(\alpha,\beta)$。观测到的比率 $y_j/n_j$，$j=1,\dots,70$，均值为 $0.136$，标准差为 $0.103$。把它们与 Beta 分布的均值和方差匹配，

$$
\frac{\alpha}{\alpha+\beta}=0.136,\qquad\alpha+\beta=\frac{\mathbb{E}\theta\,(1-\mathbb{E}\theta)}{\operatorname{Var}\theta}-1=\frac{0.136\times0.864}{0.103^2}-1\approx10,
$$
得 $\alpha\approx1.4$，$\beta\approx8.6$。于是当前实验的后验为 $\mathrm{Beta}(5.4,18.6)$，均值为 $0.223$，标准差为 $0.083$，远低于原始比率 $4/14=0.286$。

这是一个**经验贝叶斯**分析（[3.7.5](/3.7.5)，定义 5.6.3），它是合理的，但有缺陷。

- 它不是贝叶斯计算，因为它不是基于对全部数据的完整概率模型。$\alpha$ 与 $\beta$ 的点估计带有一定的任意性，并且忽略了它们的不确定性：70 次实验、每次约 20 只大鼠，远不足以精确地知道 $\alpha$ 与 $\beta$。
- 若把估计出的先验用于关于前 70 次实验本身的推断，数据就被用了两次，一次用来形成先验，一次出现在似然中。
- 矩估计还混淆了两种变异来源。$y_j/n_j$ 的方差是 $\theta_j$ 的方差加上二项方差 $\theta_j(1-\theta_j)/n_j$，所以观测到的离散程度夸大了 $\theta_j$ 的离散程度，$\alpha+\beta$ 被低估了。

完全贝叶斯方法把超参数与其他参数一样当作未知量，并给它们一个先验分布 $p(\alpha,\beta)$。所有参数的联合先验为

$$
p(\alpha,\beta,\theta_1,\dots,\theta_{71})=p(\alpha,\beta)\,p(\theta_1,\dots,\theta_{71}\mid\alpha,\beta),
$$
联合后验为

$$
p(\alpha,\beta,\theta_1,\dots,\theta_{71}\mid y)\propto p(\alpha,\beta,\theta_1,\dots,\theta_{71})\,p(y_1,\dots,y_{71}\mid\theta_1,\dots,\theta_{71},\alpha,\beta)=p(\alpha,\beta,\theta_1,\dots,\theta_{71})\,p(y_1,\dots,y_{71}\mid\theta_1,\dots,\theta_{71}),
$$
因为数据只通过 $\theta_j$ 依赖于超参数。这是一个有 $73$ 个参数的普通多参数问题（[3.7.3](/3.7.3)），§6.5 将求解它。

## 6.2. 为什么用层次模型

层次模型把复杂的联合分布拆成较简单的条件部分来描述，每个部分都易于理解，合起来就确定了全部数据与参数的联合分布。在某种意义上，到目前为止的所有模型都是两层的层次模型：给定参数时的数据，以及给定事先固定的超参数时的参数；新的一步是使上层也不确定。每个部分内部还可以有进一步的层次结构。

动机是模型选择中熟悉的权衡。参数很少的非层次模型，如对所有组取同一个 $\theta$，通常对分组数据拟合不好。参数很多的非层次模型，如给每组取一个互不相关的 $\theta_j$，对数据拟合得好，但预测得差，即过拟合问题。层次模型用少量的有效参数拟合数据，并且预测得好。它们甚至可以有比数据点更多的参数而仍然给出合理的答案，因为总体分布约束着各组参数。这三种可能性各有名称。

**定义 6.2.1（无合并、完全合并与部分合并）** 对带有各组参数 $\theta_1,\dots,\theta_J$ 的分组数据：**无合并**只用第 $j$ 组自己的数据估计每个 $\theta_j$；**完全合并**假设 $\theta_1=\dots=\theta_J$，并用全部数据估计这个共同值；**部分合并**把 $\theta_j$ 建模为抽自带有未知参数的同一总体分布，使每个估计都把本组的数据与其他组的信息结合起来。

无合并与完全合并分别是总体方差趋于无穷与趋于零时部分合并的极限；八所学校的例子（§6.6）展示了整个范围。

## 6.3. 可交换性

### 6.3.1. 定义

凭什么把 $\theta_j$ 当作抽自同一分布？如果除数据 $y$ 之外没有其他信息可以把任何一个 $\theta_j$ 与其他的区别开来，并且无法对参数作出任何排序或分组，那么我们必须在它们的先验分布中假设参数之间是对称的。

**定义 6.3.1（可交换性）** 若随机变量 $\theta_1,\dots,\theta_J$ 的联合分布在下标的置换下不变，即对 $(1,\dots,J)$ 的每个置换 $\pi$ 有 $p(\theta_1,\dots,\theta_J)=p(\theta_{\pi(1)},\dots,\theta_{\pi(J)})$，则称它们具有**可交换性**。若无穷序列的每个有限子序列都具有可交换性，则称该序列具有可交换性。

在大鼠肿瘤的例子中，没有先验的理由认为 $\theta_{70}<\theta_{71}$ 比 $\theta_{70}>\theta_{71}$ 更可能；就所给的信息而言，实验列出的顺序没有意义，可交换的先验是合理的。若下标中含有信息，可交换性通常就不合理了。假设实验 50–71 所用的纯种大鼠品系与实验 1–49 不同。那么交换下标 49 与 50 会改变参数的含义，更好的模型是把参数在品系内部当作可交换的，或者把品系作为组水平的协变量，使参数在给定它的条件下可交换。

可交换性并不蕴含独立性。二元正态分布

$$
\begin{bmatrix}\theta_1\\\theta_2\end{bmatrix}\sim\mathcal{N}_2\left(\begin{bmatrix}\mu\\\mu\end{bmatrix},\begin{bmatrix}\sigma^2&\rho\sigma^2\\\rho\sigma^2&\sigma^2\end{bmatrix}\right),\qquad\rho\ne0,
$$
是可交换的，因为交换 $\theta_1$ 与 $\theta_2$ 它不变，但显然不是独立的。可交换性蕴含所有边缘分布相同（$\theta_j$ 同分布），以及任意两个分量之间的相依性相同，但对独立性什么也没说。反过来，每个独立同分布的序列都是可交换的。

### 6.3.2. de Finetti 定理

构造可交换分布最简单的办法是让 $\theta_j$ 在给定未知参数 $\phi$ 时独立，而 $\phi$ 本身是随机的：

$$
p(\theta_1,\dots,\theta_J)=\int\Big[\prod_{j=1}^Jp(\theta_j\mid\phi)\Big]p(\phi)\,\mathrm{d}\phi.
$$
被积函数关于下标是对称的，混合也是。值得注意的事实是，对无穷序列，实质上没有别的办法。

**定理 6.3.1（de Finetti 定理）** 设 $\theta_1,\theta_2,\dots$ 是随机变量的无穷可交换序列（性质适当良好，例如取实值）。则存在随机参数 $\phi$（一般是一个随机的概率分布），使得给定 $\phi$ 时 $\theta_j$ 独立同分布，并且对每个 $J$

$$
p(\theta_1,\dots,\theta_J)=\int\prod_{j=1}^Jp(\theta_j\mid\phi)\,p(\phi)\,\mathrm{d}\phi.
$$

de Finetti 对二值序列证明了该定理（1931），Hewitt 与 Savage（1955）把它推广到一般空间；我们不给出证明。用话来说：在 $J\to\infty$ 的极限下，$(\theta_1,\dots,\theta_J)$ 上任何性质适当良好的可交换分布，都可以表示为独立同分布的混合。对有限的 $J$，这一表示近似成立；如果这 $J$ 个变量可以看作更长的可交换序列的一部分，则精确成立。这就是层次模型的理论支撑：若我们判断各组参数是可交换的，就不妨把它们建模为抽自总体分布 $p(\theta\mid\phi)$ 的独立样本，并给它的参数取先验 $p(\phi)$。在大鼠肿瘤模型与多数层次模型中成立的、$\theta_j$ 在给定 $\phi$ 时的条件独立性，对 **Gibbs 抽样**（[3.5.9](/3.5.9)）也是有用的。

有限与无穷的情形确有不同。独立同分布变量的混合总有 $\operatorname{Cov}(\theta_1,\theta_2)=\operatorname{Var}\big(\mathbb{E}(\theta_1\mid\phi)\big)\ge0$，所以上面 $\rho<0$ 的二元正态分布是可交换的，但不具有这种形式；它不能延拓为较长的可交换序列（思考题 6）。

### 6.3.3. 可交换性反映的是信息，而不是世界

一组参数是否可交换，取决于我们知道什么，而不是参数本身。

**例 6.3.1** 一位研究者想知道六个国家中经常参加某种运动的人的比例 $\theta_1,\dots,\theta_6$。在收集任何数据之前，关于 $\theta_6$ 能说什么？

1. *没有信息区分这些国家。* 必须把六个比率建模为可交换的。若随后观测到五个国家的比率，它们就告诉我们关于总体分布的信息，从而也告诉我们关于 $\theta_6$ 的信息。
2. *我们知道哪个国家是第六个，并且知道这项运动在那里比任何其他地方都流行得多，而观测到的五个国家是其余的国家。* 即使在看到五个观测比率之前，我们也不能给六个比率指定可交换的先验。一旦观测到那五个，$\theta_6$ 的合理后验应当把大部分质量放在它们全部之上：$\mathbb{P}\big(\theta_6>\max(\theta_1,\dots,\theta_5)\mid\theta_1,\dots,\theta_5\big)$ 应当很大。
3. *我们知道这六个国家，包括其中一个是特殊的，但不知道哪个下标对应哪个国家。* 六个比率又是可交换的，因为没有什么区分下标。但总体分布此时必须允许有一个值远离其他值，例如采用重尾分布而不是正态分布。

同样的参数在情形 1 与 3 中是可交换的，在情形 2 中则不是；而且仅凭可交换性不能确定总体分布的形式，它还必须反映我们所知道的。

## 6.4. 完全贝叶斯层次模型

### 6.4.1. 结构

带有数据 $y_j$（第 $j$ 组中的观测向量）的 $J$ 组层次模型有三层：

$$
y_j\mid\theta,\phi\sim p(y_j\mid\theta_j),\qquad\theta\mid\phi\sim p(\theta\mid\phi)=\prod_{j=1}^Jp(\theta_j\mid\phi),\qquad\phi\sim p(\phi).
$$
这里 $\theta=(\theta_1,\dots,\theta_J)$，分布 $p(\theta_j\mid\phi)$ 是总体分布，并且

**定义 6.4.1（超先验）** 在层次模型中，超参数 $\phi$ 的先验分布 $p(\phi)$ 称为**超先验**。

联合先验为 $p(\theta,\phi)=p(\phi)p(\theta\mid\phi)$，联合后验为

$$
p(\theta,\phi\mid y)\propto p(\phi)\,p(\theta\mid\phi)\,p(y\mid\theta,\phi)=p(\phi)\,p(\theta\mid\phi)\,p(y\mid\theta)=p(\phi)\prod_{j=1}^Jp(\theta_j\mid\phi)\prod_{j=1}^Jp(y_j\mid\theta_j).
$$
所关心的量有两类。

- 各组参数的后验 $p(\theta\mid y)=\int p(\theta,\phi\mid y)\,\mathrm{d}\phi$，通过 $(\theta,\phi)$ 的联合后验得到。
- **后验预测分布**，分两种情形：(1) 来自已有组 $j$ 的未来观测 $\tilde y$，其分布 $p(\tilde y\mid\theta_j)$ 对 $\theta_j$ 的后验取平均；(2) 来自新组的观测 $\tilde y$，其参数 $\tilde\theta$ 是从总体分布 $p(\tilde\theta\mid\phi)$ 中新抽取的，对 $\phi$ 的后验取平均。

超先验通常选为弱信息的或无信息的，因为模型的目的是从各组学习总体分布。但如 §6.5 与 §6.6 所示，超参数上的**广义先验**很容易产生不正常的后验，所以选取时需要小心。

### 6.4.2. 共轭层次模型：三步

当总体分布与似然共轭时，后验可以分三步分析。

1. 把联合后验 $p(\theta,\phi\mid y)$ 写成未归一化的形式，即超先验 $p(\phi)$、总体分布 $p(\theta\mid\phi)$ 与似然 $p(y\mid\theta)$ 的乘积。
2. 解析地确定给定超参数时 $\theta$ 的条件后验 $p(\theta\mid\phi,y)$。对固定的观测 $y$，它是 $\phi$ 的函数；由共轭性与条件独立性，它是标准分布的乘积，每组一个。
3. 用贝叶斯的方式估计 $\phi$，即求它的边缘后验 $p(\phi\mid y)$。

第 3 步的边缘后验有两种求法。一是蛮力积分 $p(\phi\mid y)=\int p(\theta,\phi\mid y)\,\mathrm{d}\theta$，这是高维积分，通常很困难。二是条件概率公式

$$
p(\phi\mid y)=\frac{p(\theta,\phi\mid y)}{p(\theta\mid\phi,y)},
$$
它对每个 $\theta$ 都成立。在第二种方法中，$p(\theta\mid\phi,y)$ 的归一化常数依赖于 $\phi$，必须保留，这正是需要小心之处。等价地，$p(\phi\mid y)\propto p(\phi)p(y\mid\phi)$，其中**边际似然**为

$$
p(y\mid\phi)=\prod_{j=1}^J\int p(y_j\mid\theta_j)\,p(\theta_j\mid\phi)\,\mathrm{d}\theta_j,
$$
是各组先验预测密度的乘积，对共轭模型有闭式。要从联合后验抽样，把第 3 步与第 2 步反过来：由于 $\phi$ 是低维的，通常在格点上（[3.7.5](/3.7.5)，算法 5.2.1）从 $p(\phi\mid y)$ 抽取 $\phi^s$；再从标准分布 $p(\theta\mid\phi^s,y)$ 抽取 $\theta^s$；然后在需要时抽取预测值 $\tilde y^s$。这就是 [3.7.5](/3.7.5) 的命题 5.1.2，其中 $\phi$ 扮演 $x$ 的角色。

## 6.5. Beta–二项层次模型：大鼠肿瘤

### 6.5.1. 后验

对大鼠肿瘤数据（例 6.1.1），共 $J=71$ 次实验，层次模型为

$$
y_j\mid\theta_j\sim\mathrm{Bin}(n_j,\theta_j),\qquad\theta_j\mid\alpha,\beta\overset{\text{iid}}{\sim}\mathrm{Beta}(\alpha,\beta),\qquad(\alpha,\beta)\sim p(\alpha,\beta),
$$
其中有肿瘤数 $y_j$、已知的样本量 $n_j$，以及超参数 $(\alpha,\beta)$，其超先验有待确定。按三步进行：

1. 联合后验为
   $$
   p(\theta,\alpha,\beta\mid y)\propto p(\alpha,\beta)\prod_{j=1}^J\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\theta_j^{\alpha-1}(1-\theta_j)^{\beta-1}\prod_{j=1}^J\theta_j^{y_j}(1-\theta_j)^{n_j-y_j}.
   $$
2. 给定 $(\alpha,\beta)$，各 $\theta_j$ 独立，其后验为 Beta 分布，
   $$
   p(\theta\mid\alpha,\beta,y)=\prod_{j=1}^J\frac{\Gamma(\alpha+\beta+n_j)}{\Gamma(\alpha+y_j)\Gamma(\beta+n_j-y_j)}\theta_j^{\alpha+y_j-1}(1-\theta_j)^{\beta+n_j-y_j-1},\qquad\theta_j\mid\alpha,\beta,y\sim\mathrm{Beta}(\alpha+y_j,\beta+n_j-y_j).
   $$
3. 把第一个表达式除以第二个，
   $$
   p(\alpha,\beta\mid y)\propto p(\alpha,\beta)\prod_{j=1}^J\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\cdot\frac{\Gamma(\alpha+y_j)\Gamma(\beta+n_j-y_j)}{\Gamma(\alpha+\beta+n_j)}.
   $$
   每个因子是 $\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)/\mathrm{B}(\alpha,\beta)$，即 $y_j$ 的 **Beta-二项分布**去掉二项系数：这就是 §6.4.2 的边际似然 $p(y\mid\alpha,\beta)$。它作为 $(\alpha,\beta)$ 的函数不是标准密度，但易于在格点上计算。

### 6.5.2. 超先验的选取

超先验应当表达对 $(\alpha,\beta)$ 的无知，同时给出正常的后验。几个自然的选择都不行。

*广义的均匀先验 $p(\alpha,\beta)\propto1$ 给出不正常的后验。* 固定先验均值 $\mu=\alpha/(\alpha+\beta)$，令先验样本量 $s=\alpha+\beta$ 趋于无穷。则 $\mathrm{Beta}(\alpha,\beta)$ 集中在 $\mu$ 处，边际似然的每个因子趋于正的常数，

$$
\frac{\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)}{\mathrm{B}(\alpha,\beta)}=\frac{\prod_{k=0}^{y_j-1}(\alpha+k)\prod_{k=0}^{n_j-y_j-1}(\beta+k)}{\prod_{k=0}^{n_j-1}(\alpha+\beta+k)}\to\mu^{y_j}(1-\mu)^{n_j-y_j},
$$
即在值 $\mu$ 处完全合并的似然。数据不能排除所有组共享同一个比率，所以似然在 $\alpha,\beta\to\infty$ 时不衰减，并且 $\int\!\!\int p(\alpha,\beta\mid y)\,\mathrm{d}\alpha\,\mathrm{d}\beta=\infty$。要使后验正常，$p(\alpha,\beta)$ 必须在这个方向上有足够轻的尾部。

*有界区域上的均匀先验是正常的，但不能截断后验。* 取独立的 $\alpha\sim\mathrm{U}(0,20)$，$\beta\sim\mathrm{U}(0,20)$，

$$
p(\alpha,\beta\mid y)\propto\boldsymbol{1}\{\alpha\le20\}\boldsymbol{1}\{\beta\le20\}\prod_{j=1}^J\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\cdot\frac{\Gamma(\alpha+y_j)\Gamma(\beta+n_j-y_j)}{\Gamma(\alpha+\beta+n_j)},
$$
后验被 $\beta$ 的上限截掉了，而它的大部分质量本应在那里。把界限扩大到 $\alpha\sim\mathrm{U}(0,40)$，$\beta\sim\mathrm{U}(0,100)$ 能够容纳后验，但答案仍依赖于任意的界限，因为后验向大的 $\alpha+\beta$ 有很长的尾部。

*重新参数化。* 在尺度

$$
(\alpha,\beta)\longmapsto\Big(\log\frac\alpha\beta,\;\log(\alpha+\beta)\Big)
$$
上考虑超参数更容易，其中 $\log(\alpha/\beta)=\operatorname{logit}\frac{\alpha}{\alpha+\beta}$ 是先验均值的 logit，而 $\alpha+\beta$ 是先验样本量，即先验所代表的附加数据的大小（[3.7.1](/3.7.1)，§1.6.2）。好处是“先验均值”与“先验样本量”被分开了，可以独立地赋予先验分布，并且两个新参数都遍及整条实直线。但在 $\big(\log\frac\alpha\beta,\log(\alpha+\beta)\big)$ 上的广义均匀先验又给出不正常的后验：当 $\log(\alpha+\beta)\to\infty$ 时似然趋于正的常数。

*后验正常的弥散先验。* 取在 $\big(\frac{\alpha}{\alpha+\beta},(\alpha+\beta)^{-1/2}\big)$ 上的均匀先验，即先验均值与大致的先验标准差尺度，因为 $\mathrm{Beta}(\alpha,\beta)$ 的标准差是 $\sqrt{\mu(1-\mu)/(\alpha+\beta+1)}$。记 $u=\frac{\alpha}{\alpha+\beta}$，$v=(\alpha+\beta)^{-1/2}$，$s=\alpha+\beta$，Jacobi 行列式为

$$
\Big\lvert\frac{\partial(u,v)}{\partial(\alpha,\beta)}\Big\rvert=\left\lvert\det\begin{bmatrix}\beta/s^2&-\alpha/s^2\\-\frac12s^{-3/2}&-\frac12s^{-3/2}\end{bmatrix}\right\rvert=\frac12s^{-7/2}(\alpha+\beta)=\frac12(\alpha+\beta)^{-5/2},
$$
所以

$$
p(\alpha,\beta)\propto(\alpha+\beta)^{-5/2},\qquad\text{等价地}\qquad p\Big(\log\frac\alpha\beta,\log(\alpha+\beta)\Big)\propto\alpha\beta(\alpha+\beta)^{-5/2},
$$
因为 $(\alpha,\beta)\mapsto(\log\frac\alpha\beta,\log(\alpha+\beta))$ 的 Jacobi 因子为 $\frac{1}{\alpha\beta}$。在坐标 $(\mu,s)$ 中，这个先验对大的 $s$ 表现为 $s^{-3/2}$，它是可积的，后验是正常的。其他尾部足够轻的选择也是可能的；重要的是结论对合理选择之间的取舍不敏感。

### 6.5.3. 计算

在先验 $p(\alpha,\beta)\propto(\alpha+\beta)^{-5/2}$ 下，计算

$$
p\Big(\log\frac\alpha\beta,\log(\alpha+\beta)\Bigm|y\Big)\propto\alpha\beta(\alpha+\beta)^{-5/2}\prod_{j=1}^{71}\frac{\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)}{\mathrm{B}(\alpha,\beta)}
$$
的对数，在变换后的坐标的格点上，并包含 Jacobi 因子 $\alpha\beta$。后验在这个尺度上大致对称，其众数在 $\big(\log\frac\alpha\beta,\log(\alpha+\beta)\big)=(-1.79,2.74)$ 附近。然后模拟按以下步骤进行。

1. 用格点抽样（[3.7.5](/3.7.5)，算法 5.2.1）从后验抽取 1000 个 $\big(\log\frac\alpha\beta,\log(\alpha+\beta)\big)$ 的值。
2. 对 $l=1,\dots,1000$：
   1. 把第 $l$ 个样本变换回 $(\alpha,\beta)$ 的尺度，得到来自超参数边缘后验的一个样本；
   2. 对每个 $j=1,\dots,J$，从其条件后验 $\theta_j\mid\alpha,\beta,y\sim\mathrm{Beta}(\alpha+y_j,\beta+n_j-y_j)$ 抽取 $\theta_j$。

由这些样本算得的超参数后验均值，以富有启发性的方式依赖于超先验：

| 超先验 | $\mathbb{E}(\alpha\mid y)$ | $\mathbb{E}(\beta\mid y)$ | $\mathbb{E}\big(\frac{\alpha}{\alpha+\beta}\mid y\big)$ | $\mathbb{E}(\alpha+\beta\mid y)$ |
|---|---|---|---|---|
| $p(\alpha,\beta)\propto(\alpha+\beta)^{-5/2}$ | 2.4 | 14.3 | 0.144 | 16.7 |
| $\alpha\sim\mathrm{U}(0,40)$，$\beta\sim\mathrm{U}(0,100)$ | 3.5 | 20.7 | 0.143 | 24.2 |

正如预期，先验 $(\alpha+\beta)^{-5/2}$ 把 $\alpha+\beta$ 往下拉，而有界均匀先验让向大的 $\alpha+\beta$ 的长尾起了作用。总体分布的中心估计在两者下相同。§6.1 的经验贝叶斯估计 $\alpha+\beta\approx10$ 比两者都小，正如 §6.1 的第三条说明所预言的。

### 6.5.4. 收缩

我们真正想要的是肿瘤率 $\theta_j$：

$$
p(\theta\mid y)=\int p(\theta\mid\alpha,\beta,y)\,p(\alpha,\beta\mid y)\,\mathrm{d}\alpha\,\mathrm{d}\beta,
$$
它没有闭式，但由模拟的 $\theta_j$ 表示。对已观测的组 $j$，由**全期望公式**，

$$
\mathbb{E}(\theta_j\mid y)=\mathbb{E}\big[\mathbb{E}(\theta_j\mid\alpha,\beta,y)\bigm|y\big]=\mathbb{E}\Big[\frac{\alpha+y_j}{\alpha+\beta+n_j}\Bigm|y\Big],
\qquad
\frac{\alpha+y_j}{\alpha+\beta+n_j}=\frac{\alpha+\beta}{\alpha+\beta+n_j}\cdot\frac{\alpha}{\alpha+\beta}+\frac{n_j}{\alpha+\beta+n_j}\cdot\frac{y_j}{n_j}.
$$
每个估计都是该组自己的比率 $y_j/n_j$ 与总体均值 $\frac{\alpha}{\alpha+\beta}$ 的加权平均，权重为 $n_j$ 与 $\alpha+\beta$，再对超参数的后验取平均。这就是部分合并，而向总体均值的拉动，就是 [3.7.5](/3.7.5) §5.6 的**收缩估计**所说的收缩：每组都借用其他组的信息。$n_j$ 小的组与原始比率极端的组被拉得最多。在约 $20$ 只大鼠中有 $0$ 个肿瘤的实验，后验均值约为 $0.06$ 而不是 $0$，最高比率 $9/24=0.375$ 被拉到约 $0.28$。有效先验样本量 $\alpha+\beta$ 更大的有界均匀超先验，比 $(\alpha+\beta)^{-5/2}$ 把估计收缩得更多，尽管收缩到大致相同的位置。

![先验 p(α, β) ∝ (α + β)^(−5/2) 下的大鼠肿瘤例子。左图：(log(α/β), log(α + β)) 的边缘后验在格点上的等高线，以及 500 个模拟样本。右图：71 个肿瘤率 θj 的后验中位数与 95% 区间，对观测比率 yj/nj 作图（水平方向有扰动）；虚线是无合并，并标出了当前实验 4/14。](./plots/rat_tumor_hyperposterior.py)

对当前实验，$\theta_{71}$ 的后验均值为 $0.21$，$95\%$ 中心后验区间为 $[0.08,0.38]$，与 §6.1 的经验贝叶斯答案 $\mathrm{Beta}(5.4,18.6)$（均值 $0.223$，区间 $[0.08,0.41]$）接近。有 70 次信息丰富的实验时，关于 $(\alpha,\beta)$ 的不确定性对这一组影响很小，这解释了为什么经验贝叶斯捷径在这里效果尚可；层次模型使这成为结论而不是假设。

对尚未观测的新实验，比率 $\tilde\theta$ 是从总体分布中新抽取的，并且

$$
\mathbb{E}(\tilde\theta\mid y)=\mathbb{E}\big[\mathbb{E}(\tilde\theta\mid\alpha,\beta,y)\bigm|y\big]=\mathbb{E}\Big[\frac{\alpha}{\alpha+\beta}\Bigm|y\Big]=0.144,
$$
$95\%$ 区间为 $[0.02,0.36]$，比任何已观测的组宽得多，因为除总体之外对这一组一无所知。

## 6.6. 正态层次模型：八所学校

### 6.6.1. 八所学校的平行实验

**例 6.6.1（八所学校）** 一项为教育考试服务中心（Educational Testing Service）所做的研究，分析了特殊辅导项目对八所高中的 SAT 语文部分（SAT-V）的效果（Rubin，1981）。在每所学校中，学生被随机分配到辅导组或对照组，处理效应 $y_j$ 及其标准误 $\sigma_j$ 由各校单独的协方差分析估计：

| 学校 | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 估计的处理效应 $y_j$ | 28 | 8 | $-3$ | 7 | $-1$ | 1 | 18 | 12 |
| 标准误 $\sigma_j$ | 15 | 10 | 16 | 11 | 9 | 11 | 10 | 18 |

每所学校有三十多名学生，所以我们把 $y_j$ 当作八个独立的正态观测，$y_j\mid\theta_j\sim\mathcal{N}(\theta_j,\sigma_j^2)$，方差已知。SAT-V 的分数范围是 200 至 800，辅导项目旨在提高分数。

有些效应看起来很大：学校 A 的 $28$ 会不会只是偶然？两种简单的分析都不令人满意。

- *分别估计*（无合并）：学校 A 的效应估计为 $28$，标准误为 $15$。在平坦先验下，$\mathbb{P}(\theta_A>28\mid y)=0.5$，这似乎太高了：其他学校都没有显示这样的效应。
- *合并估计*（完全合并）：假设所有 $\theta_j$ 相等。取无信息先验，共同效应的后验均值等于按精度加权的平均 $\sum_jy_j/\sigma_j^2\big/\sum_j1/\sigma_j^2=7.7$，后验方差为 $\big(\sum_j1/\sigma_j^2\big)^{-1}=16.6$，标准误为 $4.1$，$95\%$ 后验区间为 $[-0.3,15.7]$。齐一性的卡方检验 $\sum_j(y_j-7.7)^2/\sigma_j^2=4.7$（7 个自由度）并不拒绝相等。但这样就有 $\mathbb{P}(\theta_A<7.7\mid y)=0.5$，甚至 $\mathbb{P}(\theta_A<\theta_C\mid y)=0.5$，尽管学校 A 估计为 $28$ 而学校 C 为 $-3$。

两种估计都不完全令人满意。我们想要一个折中，既结合全部八次实验的信息，又不假设所有 $\theta_j$ 相等：部分合并。

### 6.6.2. 模型及其后验

一般地，设 $y_{ij}\mid\theta_j\sim\mathcal{N}(\theta_j,\sigma^2)$，$i=1,\dots,n_j$，组 $j=1,\dots,J$，方差已知。各组均值 $\bar y_{\cdot j}=\frac1{n_j}\sum_iy_{ij}$ 是充分的，$\bar y_{\cdot j}\mid\theta_j\sim\mathcal{N}(\theta_j,\sigma_j^2)$，$\sigma_j^2=\sigma^2/n_j$；在八所学校中 $\bar y_{\cdot j}$ 就是 $y_j$。总体分布是带有未知超参数 $\mu$ 与 $\tau$ 的正态分布：

$$
\bar y_{\cdot j}\mid\theta_j\sim\mathcal{N}(\theta_j,\sigma_j^2),\qquad p(\theta_1,\dots,\theta_J\mid\mu,\tau)=\prod_{j=1}^J\mathcal{N}(\theta_j\mid\mu,\tau^2),\qquad(\mu,\tau)\sim p(\mu,\tau).
$$
三步给出下面的结果。

1. *联合后验。*
   $$
   p(\theta,\mu,\tau\mid y)\propto p(\mu,\tau)\,p(\theta\mid\mu,\tau)\,p(y\mid\theta)\propto p(\mu,\tau)\prod_{j=1}^J\mathcal{N}(\theta_j\mid\mu,\tau^2)\prod_{j=1}^J\mathcal{N}(\bar y_{\cdot j}\mid\theta_j,\sigma_j^2).
   $$
2. *各组均值的条件后验。* 对固定的 $(\mu,\tau)$，每个 $\theta_j$ 是方差已知、先验为正态的正态均值（[3.7.2](/3.7.2)，§2.3），所以各 $\theta_j$ 独立，且
   $$
   \theta_j\mid\mu,\tau,y\sim\mathcal{N}(\hat\theta_j,V_j),\qquad\hat\theta_j=\frac{\frac1{\sigma_j^2}\bar y_{\cdot j}+\frac1{\tau^2}\mu}{\frac1{\sigma_j^2}+\frac1{\tau^2}},\qquad V_j=\frac{1}{\frac1{\sigma_j^2}+\frac1{\tau^2}}.
   $$
3. *超参数的边缘后验。* 把 $\theta_j$ 积分掉，$\bar y_{\cdot j}\mid\mu,\tau\sim\mathcal{N}(\mu,\sigma_j^2+\tau^2)$ 相互独立，所以
   $$
   p(\mu,\tau\mid y)\propto p(\mu,\tau)\prod_{j=1}^J\mathcal{N}(\bar y_{\cdot j}\mid\mu,\sigma_j^2+\tau^2).
   $$

我们给 $\mu$ 取给定 $\tau$ 时无信息的均匀超先验，$p(\mu,\tau)=p(\mu\mid\tau)p(\tau)\propto p(\tau)$；给 $\mu$ 取正常的先验几乎没有影响，因为给定 $\tau$ 时数据能很好地确定 $\mu$。边缘后验进一步分解为 $p(\mu,\tau\mid y)=p(\mu\mid\tau,y)\,p(\tau\mid y)$。给定 $\tau$ 时，$\mu$ 是 $J$ 个方差为 $\sigma_j^2+\tau^2$ 的正态观测的共同均值，所以

$$
\mu\mid\tau,y\sim\mathcal{N}(\hat\mu,V_\mu),\qquad\hat\mu=\frac{\sum_{j=1}^J\frac{1}{\sigma_j^2+\tau^2}\bar y_{\cdot j}}{\sum_{j=1}^J\frac{1}{\sigma_j^2+\tau^2}},\qquad V_\mu^{-1}=\sum_{j=1}^J\frac{1}{\sigma_j^2+\tau^2}.
$$
由条件概率公式，对任何 $\mu$，

$$
p(\tau\mid y)=\frac{p(\mu,\tau\mid y)}{p(\mu\mid\tau,y)}\propto\frac{p(\tau)\prod_{j=1}^J\mathcal{N}(\bar y_{\cdot j}\mid\mu,\sigma_j^2+\tau^2)}{\mathcal{N}(\mu\mid\hat\mu,V_\mu)},
$$
取 $\mu=\hat\mu$，此时分母为 $(2\pi V_\mu)^{-1/2}$，

$$
p(\tau\mid y)\propto p(\tau)\,V_\mu^{1/2}\prod_{j=1}^J(\sigma_j^2+\tau^2)^{-1/2}\exp\Big(-\frac{(\bar y_{\cdot j}-\hat\mu)^2}{2(\sigma_j^2+\tau^2)}\Big),
$$
其中 $\hat\mu$ 与 $V_\mu$ 依赖于 $\tau$。这个一维密度在格点上计算。

### 6.6.3. $\tau$ 的超先验

似然因子在 $\tau$ 的取值范围两端的行为，决定了哪些超先验可行。

1. *均匀先验 $p(\tau)\propto1$：后验正常。* 当 $\tau\to0$ 时似然因子趋于正的常数（完全合并的似然），它在 $0$ 附近可积。当 $\tau\to\infty$ 时，$V_\mu^{1/2}\approx\tau/\sqrt J$，乘积表现为 $\tau^{-J}$，所以 $p(\tau\mid y)$ 按 $\tau^{1-J}$ 衰减，当 $J\ge3$ 时可积。
2. *$\log\tau$ 上的均匀先验 $p(\tau)\propto1/\tau$：后验不正常。* 在 $\tau=0$ 附近，后验表现为 $c/\tau$（$c>0$），其积分发散。这个先验在其他场合对尺度参数是自然的（[3.7.2](/3.7.2)，§2.8），但在这里不行，因为数据不能排除 $\tau=0$：它们与所有组有相同均值相容。
3. *正常的先验*，例如 $\tau^2$ 的尺度逆卡方分布，总是给出正常的后验。选取时必须小心，因为这个族的先验在 $\tau=0$ 附近放的质量很少，当 $J$ 很小时，它可能主导后验。在 $\tau=0$ 处保持正密度的正常弱信息先验，如 $\tau$ 的半正态分布或半 Cauchy 分布，是常见的替代选择。

我们对 $\tau$ 使用均匀先验，并对 $\mu$ 使用均匀先验。

### 6.6.4. 模拟

从联合后验 $p(\theta,\mu,\tau\mid y)$ 抽样，对 $k=1,\dots,S$：

1. 在格点上从 $p(\tau\mid y)$ 抽取 $\tau^k$；
2. 从 $p(\mu\mid\tau^k,y)=\mathcal{N}(\hat\mu^k,V_\mu^k)$ 抽取 $\mu^k$，其中 $\hat\mu^k$ 与 $V_\mu^k$ 是在 $\tau^k$ 处计算的 $\hat\mu$ 与 $V_\mu$；
3. 从 $p(\theta\mid\mu^k,\tau^k,y)$ 抽取 $\theta^k$。给定 $\mu^k$、$\tau^k$ 与 $y$，各分量条件独立，所以独立地抽取 $\theta_j^k\sim\mathcal{N}(\hat\theta_j^k,V_j^k)$，其中
   $$
   \hat\theta_j^k=\frac{\frac1{\sigma_j^2}\bar y_{\cdot j}+\frac1{(\tau^k)^2}\mu^k}{\frac1{\sigma_j^2}+\frac1{(\tau^k)^2}},\qquad V_j^k=\frac{1}{\frac1{\sigma_j^2}+\frac1{(\tau^k)^2}}.
   $$

### 6.6.5. 结果

边缘后验 $p(\tau\mid y)$ 的众数在 $\tau=0$ 处，那里数据与完全合并最一致，但它很宽：中位数约为 $5$，$97.5\%$ 分位数约为 $20$，$\mathbb{P}(\tau>10\mid y)=0.21$。使各学校相当不同的 $\tau$ 值远没有被排除。$\tau$ 的边际极大似然估计为 $0$，矩估计也是（$y_j$ 的样本方差 $109$ 小于平均抽样方差 $166$），所以经验贝叶斯分析会代入 $\tau=0$，并报告完全合并以及它过于自信的区间。

学校效应如何依赖于 $\tau$，可以从条件后验均值与标准差看出。把 $\hat\theta_j$ 与 $V_j$ 对 $\mu\mid\tau,y$ 取平均，

$$
\mathbb{E}(\theta_j\mid\tau,y)=\frac{\frac1{\sigma_j^2}\bar y_{\cdot j}+\frac1{\tau^2}\hat\mu}{\frac1{\sigma_j^2}+\frac1{\tau^2}},\qquad
\operatorname{Var}(\theta_j\mid\tau,y)=V_j+\Big(\frac{V_j}{\tau^2}\Big)^2V_\mu.
$$
在 $\tau=0$ 处，所有均值都等于合并估计 $7.7$，标准差为 $4.1$；随着 $\tau$ 增大，它们向分别的估计 $y_j$ 散开，标准差向 $\sigma_j$ 增长。集中在小到中等值上的 $\tau$ 的后验，决定了最终答案沿这条路径走了多远。

![μ 与 τ 取均匀先验的八所学校。左图：边缘后验密度 p(τ | y)。中图：八所学校效应的条件后验均值 E(θj | τ, y) 作为 τ 的函数；它们在 τ = 0 处都等于合并估计。右图：条件后验标准差 sd(θj | τ, y)。](./plots/eight_schools_tau.py)

对 $\tau$ 取平均，得到各学校效应的边缘后验。取自 $200{,}000$ 个模拟样本的分位数（取整）：

| 学校 | $y_j$ | $\sigma_j$ | $2.5\%$ | $25\%$ | 中位数 | $75\%$ | $97.5\%$ |
|---|---|---|---|---|---|---|---|
| A | 28 | 15 | $-2$ | 6 | 10 | 16 | 32 |
| B | 8 | 10 | $-5$ | 4 | 8 | 12 | 21 |
| C | $-3$ | 16 | $-11$ | 2 | 7 | 11 | 21 |
| D | 7 | 11 | $-6$ | 4 | 8 | 12 | 21 |
| E | $-1$ | 9 | $-9$ | 1 | 6 | 9 | 16 |
| F | 1 | 11 | $-9$ | 2 | 7 | 10 | 19 |
| G | 18 | 10 | $-1$ | 6 | 10 | 15 | 26 |
| H | 12 | 18 | $-7$ | 4 | 8 | 13 | 26 |

各估计强烈地向共同均值收缩。学校 A 的中位数是 $10$ 而不是 $28$，但它的区间延伸到 $32$；它的效应超过学校 C 的概率是 $0.68$，而不是完全合并下的 $0.5$，学校 A 的效应是八个中最大的概率约为 $0.25$。层次分析与“数据与相等的效应相容”这一观察一致，但没有强行得出这个结论。

### 6.6.6. 后验预测

预测可以纳入已经完成的模拟，对应 §6.4.1 的两种情形。

1. *来自已观测学校 $j$ 的新观测 $\tilde y$*（例如在学校 $j$ 重复这项研究时估计的效应，标准误为 $\sigma_j$）：对每个样本 $k$，抽取 $\tilde y_j^k\sim\mathcal{N}(\theta_j^k,\sigma_j^2)$。若需要 $m$ 个观测，则从同一分布抽取 $m$ 个值。
2. *来自新学校 $\tilde j$ 的观测*：对每个样本 $k$，首先从总体分布抽取新学校的效应，$\theta_{\tilde j}^k\sim\mathcal{N}(\mu^k,(\tau^k)^2)$，即给定超参数时 $\theta$ 的先验的一个样本，而不是任何已有 $\theta_j$ 的后验的样本；然后抽取 $\tilde y_{\tilde j}^k\sim\mathcal{N}(\theta_{\tilde j}^k,\tilde\sigma^2)$，$m$ 个观测的情形类似。

关键的区别在于是必须抽取新的 $\theta$，还是可以使用已有的。第二种情形导致变异更大的预测，因为关于相应的 $\theta$ 的信息更少：新学校的效应 $\theta_{\tilde j}$ 的 $95\%$ 预测区间约为 $[-12,29]$，比除 A 之外任何已有学校的后验区间都宽，加上 $\tilde\sigma=10$ 的抽样误差后，它增宽到约 $[-20,36]$。

## 小结

| 主题 | 要点 |
|---|---|
| 动机 | 由历史数据确定的先验（经验贝叶斯）忽略超参数的不确定性并把数据用了两次；完整的模型给它们取超先验（§6.1） |
| 合并 | 无合并（分别的 $\theta_j$）、完全合并（共同的 $\theta$）、部分合并（层次）（定义 6.2.1） |
| 可交换性 | 联合分布在置换下不变（定义 6.3.1）；不是独立性；反映的是信息而不是世界（例 6.3.1） |
| de Finetti | 无穷可交换序列是 i.i.d. 序列的混合（定理 6.3.1）：$\theta_j\mid\phi\overset{\text{iid}}{\sim}p(\theta\mid\phi)$ 的依据 |
| 结构 | $p(\theta,\phi\mid y)\propto p(\phi)\prod_jp(\theta_j\mid\phi)\prod_jp(y_j\mid\theta_j)$；超先验 $p(\phi)$（定义 6.4.1）；对已有组与新组的预测 |
| 三步 | 联合后验；条件分布 $p(\theta\mid\phi,y)$；边缘分布 $p(\phi\mid y)=p(\theta,\phi\mid y)/p(\theta\mid\phi,y)\propto p(\phi)p(y\mid\phi)$；按相反的顺序模拟 |
| Beta-二项 | $\theta_j\mid\alpha,\beta,y\sim\mathrm{Beta}(\alpha+y_j,\beta+n_j-y_j)$；$p(\alpha,\beta\mid y)\propto p(\alpha,\beta)\prod_j\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)/\mathrm{B}(\alpha,\beta)$ |
| 超先验（Beta） | 在 $(\alpha,\beta)$ 或 $(\log\frac\alpha\beta,\log(\alpha+\beta))$ 上平坦：后验不正常；在 $\big(\frac\alpha{\alpha+\beta},(\alpha+\beta)^{-1/2}\big)$ 上平坦，即 $(\alpha+\beta)^{-5/2}$：正常 |
| 收缩 | $\mathbb{E}(\theta_j\mid y)=\mathbb{E}\big[\frac{\alpha+\beta}{\alpha+\beta+n_j}\frac{\alpha}{\alpha+\beta}+\frac{n_j}{\alpha+\beta+n_j}\frac{y_j}{n_j}\bigm|y\big]$；新组：$\mathbb{E}\big[\frac{\alpha}{\alpha+\beta}\bigm|y\big]$ |
| 正态模型 | $\theta_j\mid\mu,\tau,y\sim\mathcal{N}(\hat\theta_j,V_j)$（按精度加权）；$\bar y_{\cdot j}\mid\mu,\tau\sim\mathcal{N}(\mu,\sigma_j^2+\tau^2)$；$\mu\mid\tau,y\sim\mathcal{N}(\hat\mu,V_\mu)$；$p(\tau\mid y)\propto p(\tau)V_\mu^{1/2}\prod_j(\sigma_j^2+\tau^2)^{-1/2}\mathrm{e}^{-(\bar y_{\cdot j}-\hat\mu)^2/(2(\sigma_j^2+\tau^2))}$ |
| 超先验（正态） | $p(\tau)\propto1$ 在 $J\ge3$ 时正常；$p(\log\tau)\propto1$ 不正常；$\tau$ 上的正常先验可用 |
| 八所学校 | $\tau=0$ 是众数，但 $\mathbb{P}(\tau>10\mid y)\approx0.2$；学校效应向 $7.7$ 收缩；对新学校的预测更宽 |

## 思考题

1. 用两种方法推导 Beta-二项层次模型的边缘后验 $p(\alpha,\beta\mid y)$：条件概率公式，以及把每个 $\theta_j$ 积分掉。

   **答** 比值法：把 §6.5.1 的联合后验除以 $p(\theta\mid\alpha,\beta,y)=\prod_j\frac{\theta_j^{\alpha+y_j-1}(1-\theta_j)^{\beta+n_j-y_j-1}}{\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)}$，$\theta_j$ 的所有幂都抵消，利用 $\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}=\frac1{\mathrm{B}(\alpha,\beta)}$，得 $p(\alpha,\beta\mid y)\propto p(\alpha,\beta)\prod_j\frac{\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)}{\mathrm{B}(\alpha,\beta)}$。积分法：对每个 $j$，$\int_0^1\frac{\theta^{\alpha+y_j-1}(1-\theta)^{\beta+n_j-y_j-1}}{\mathrm{B}(\alpha,\beta)}\,\mathrm{d}\theta=\frac{\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)}{\mathrm{B}(\alpha,\beta)}$；乘积再乘以 $p(\alpha,\beta)$ 就是同一个表达式。条件后验的归一化常数 $\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)$ 依赖于超参数，所以在比值中必须保留它们。
2. 证明在坐标 $\mu=\frac{\alpha}{\alpha+\beta}$，$s=\alpha+\beta$ 下，先验 $p(\alpha,\beta)\propto(\alpha+\beta)^{-5/2}$ 对应于 $p(\mu,s)\propto s^{-3/2}$，并解释为什么它给出正常的后验而 $p(\alpha,\beta)\propto1$ 不行。

   **答** $\alpha=\mu s$，$\beta=(1-\mu)s$，所以 $\big\lvert\frac{\partial(\alpha,\beta)}{\partial(\mu,s)}\big\rvert=\lvert\det\begin{bmatrix}s&\mu\\-s&1-\mu\end{bmatrix}\rvert=s$，$p(\mu,s)\propto s\cdot s^{-5/2}=s^{-3/2}$。当 $s\to\infty$ 时，边际似然趋于 $\mu$ 的正函数 $\prod_j\mu^{y_j}(1-\mu)^{n_j-y_j}$，所以后验在 $s$ 上的尾部表现得像先验：$\int^\infty s^{-3/2}\,\mathrm{d}s<\infty$，后验正常。在 $p(\alpha,\beta)\propto1$ 下，$(\mu,s)$ 中的密度 $\propto s$，而 $\int^\infty s\,\mathrm{d}s=\infty$。在 $s=0$ 附近似然趋于零（每个满足 $0<y_j<n_j$ 的组贡献一个量级为 $s$ 的因子），所以那里没有问题。
3. 对正态层次模型，证明 $\bar y_{\cdot j}\mid\mu,\tau\sim\mathcal{N}(\mu,\sigma_j^2+\tau^2)$，并证明 $p(\tau)\propto1/\tau$ 给出不正常的后验。

   **答** 记 $\bar y_{\cdot j}=\theta_j+\varepsilon_j$，其中 $\theta_j\mid\mu,\tau\sim\mathcal{N}(\mu,\tau^2)$，$\varepsilon_j\sim\mathcal{N}(0,\sigma_j^2)$ 与之独立；独立正态变量之和是正态的，均值为 $\mu$，方差为 $\tau^2+\sigma_j^2$。在 $p(\tau\mid y)\propto p(\tau)V_\mu^{1/2}\prod_j(\sigma_j^2+\tau^2)^{-1/2}\exp(\dots)$ 中，除 $p(\tau)$ 之外的每个因子在 $\tau\to0$ 时都有有限的正极限（完全合并的值）。因此 $p(\tau\mid y)\approx c/\tau$ 在 $0$ 附近成立，$c>0$，而 $\int_0^\varepsilon c/\tau\,\mathrm{d}\tau=\infty$。
4. 在八所学校中，当 $\tau=10$ 时，得 $\hat\mu=8.13$，$V_\mu=30.5$。计算 $\mathbb{E}(\theta_A\mid\tau=10,y)$ 与 $\operatorname{sd}(\theta_A\mid\tau=10,y)$ 并解释它们。

   **答** 由 $\sigma_A^2=225$，$\tau^2=100$，$V_A=\big(\frac1{225}+\frac1{100}\big)^{-1}=69.2$，$\mathbb{E}(\theta_A\mid\tau,y)=69.2\big(\frac{28}{225}+\frac{8.13}{100}\big)=14.2$：估计从 $28$ 向总体均值移动了约 $70\%$，因为学校 A 的标准误 $15$ 相对于 $\tau=10$ 较大。方差为 $V_A+(V_A/\tau^2)^2V_\mu=69.2+0.692^2\times30.5=83.8$，所以标准差为 $9.2$，小于 $\sigma_A=15$，但大于 $\sqrt{V_A}=8.3$，因为 $\mu$ 也是不确定的。
5. 判断可交换性作为先验假设是否合理，若不合理，如何修改模型：(a) 一项临床试验中 30 名患者的平均血压，除此之外没有记录其他信息；(b) 50 家医院的死亡率，已知床位数并认为它有影响；(c) 一名患者在节食的 30 天内的每日体重。

   **答** (a) 可交换：没有什么区分这些患者，所以采用共同的总体分布是合适的。(b) 无条件地说不可交换，因为规模携带信息；把死亡率建模为给定规模时可交换，例如 $\operatorname{logit}\theta_j\sim\mathcal{N}(\gamma_0+\gamma_1x_j,\tau^2)$，其中 $x_j$ 是床位数的对数，这就是层次回归。(c) 不可交换：天数的顺序有意义（预期有趋势，相邻的天更相似），所以需要时间序列或对时间的回归；对趋势的偏离可以当作可交换的。
6. 证明方差均为 $\sigma^2$、相关系数均为 $\rho$ 的等相关正态向量 $(\theta_1,\dots,\theta_J)$ 仅当 $\rho\ge-1/(J-1)$ 时存在，并证明有限方差的无穷可交换序列必须有 $\rho\ge0$。

   **答** 协方差矩阵 $\sigma^2[(1-\rho)I_J+\rho\boldsymbol{1}\boldsymbol{1}^{\mathsf T}]$ 的特征值为 $\sigma^2(1-\rho)$（重数 $J-1$）与 $\sigma^2(1+(J-1)\rho)$（特征向量为 $\boldsymbol{1}$），它半正定当且仅当 $-\frac{1}{J-1}\le\rho\le1$。对无穷可交换序列，每个有限片段都必须满足这个条件，所以对所有 $J$ 有 $\rho\ge-1/(J-1)$，即 $\rho\ge0$。等价地，对所有 $J$ 有 $0\le\operatorname{Var}\big(\sum_{j=1}^J\theta_j\big)=J\sigma^2+J(J-1)\rho\sigma^2$，也迫使 $\rho\ge0$。这与 de Finetti 定理一致，在该定理下 $\operatorname{Cov}(\theta_1,\theta_2)=\operatorname{Var}\big(\mathbb{E}(\theta_1\mid\phi)\big)\ge0$。
7. 在大鼠肿瘤的例子中，把后验均值 $\alpha=2.4$，$\beta=14.3$ 代入 $\frac{\alpha+y_j}{\alpha+\beta+n_j}$，近似 $0/20$ 的组与当前组 $4/14$ 的 $\theta_j$ 的后验均值。为什么这只是近似？

   **答** 对 $0/20$：$\frac{2.4}{16.7+20}=0.065$。对 $4/14$：$\frac{2.4+4}{16.7+14}=0.208$。两者都接近模拟结果（$0.06$ 与 $0.21$）。精确的后验均值是 $\mathbb{E}\big[\frac{\alpha+y_j}{\alpha+\beta+n_j}\bigm|y\big]$，即 $(\alpha,\beta)$ 的非线性函数的后验期望，它一般不同于在后验均值处计算的函数值；这里差别很小，因为 71 组数据把 $(\alpha,\beta)$ 确定得相当好。
8. 一位分析者用边际极大似然估计八所学校中的 $\tau$，得到 $\hat\tau=0$，并对每所学校都报告完全合并的结果。错在哪里？完全贝叶斯分析有何不同？

   **答** $\tau$ 的似然在边界值 $0$ 处最大，但在很宽的范围内是平坦的：直到约 $20$ 的 $\tau$ 值都与数据较为相容。代入 $\hat\tau=0$ 就把这个不确定的估计当作已知，并对每所学校报告以 $7.7$ 为中心、半宽约为 $8$ 的区间，这太窄了，并且排除了数据并没有排除的学校间差异。完全贝叶斯分析对 $p(\tau\mid y)$ 取平均：学校效应仍然强烈地向 $7.7$ 收缩，但它们的区间（学校 A 为 $[-2,32]$）同时反映了效应相等的可能性与存在实质差异的可能性。这是经验贝叶斯在组数很少时的典型失败，也是参数位于边界的一个例子（[3.7.5](/3.7.5)，§5.5.6）。
9. 解释为什么来自新学校的观测的预测分布比来自学校 B 的新观测的预测分布更宽，并用后验矩写出它的方差。

   **答** 对学校 B，$\theta_B$ 的后验由学校 B 自己的数据与其他学校提供信息，$\operatorname{Var}(\tilde y_B\mid y)=\sigma_B^2+\operatorname{Var}(\theta_B\mid y)$。对新学校，效应是从总体分布中新抽取的，所以由**全方差公式**，$\operatorname{Var}(\tilde\theta\mid y)=\mathbb{E}(\tau^2\mid y)+\operatorname{Var}(\mu\mid y)$，并且 $\operatorname{Var}(\tilde y\mid y)=\tilde\sigma^2+\mathbb{E}(\tau^2\mid y)+\operatorname{Var}(\mu\mid y)$。方差 $\operatorname{Var}(\theta_B\mid y)$ 被学校 B 的数据压缩，而 $\mathbb{E}(\tau^2\mid y)$ 是完整的学校间变异，没有数据能使它减小。
