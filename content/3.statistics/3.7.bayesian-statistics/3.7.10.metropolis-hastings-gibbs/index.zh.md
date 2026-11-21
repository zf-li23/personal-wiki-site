---
title: Metropolis–Hastings 与 Gibbs 抽样
description: 后验分布的 Markov 链模拟；Metropolis–Hastings 算法及其接受概率为何有效；独立提议与重尾的作用；随机游走 Metropolis 算法、调节参数、最优尺度与自适应；作为 Metropolis–Hastings 特例的二分量与 K 分量 Gibbs 抽样；用于层次模型的 Metropolis-within-Gibbs 算法、分块与折叠抽样；预烧期、潜在尺度缩减因子与有效样本量。
source_hash: e71039134794
---

[3.7.9](/3.7.9) 的非迭代方法（网格抽样、逆变换、**拒绝抽样**与**重要性抽样**）产生独立的抽样，但它们需要一个与整个后验相近的提议，而在维数稍高时这样的提议很难找到。**Markov 链 Monte Carlo**（MCMC）放弃独立性以换取通用性：它构造一条 **Markov 链** $\theta^{(1)},\theta^{(2)},\dots$，这条链只需做局部移动，其**平稳分布**就是后验 $p(\theta\mid y)$。经过一段初始阶段之后，链的各个状态是（相依的）后验抽样，沿链取平均即可估计后验期望。本章讲两个基本算法，**Metropolis–Hastings 算法**与 **Gibbs 抽样**，按它们在贝叶斯模型中的用法展开：实现、提议的选择与调节、它们在层次模型中的结合，以及收敛性的评估。

Markov 链、平稳分布、**细致平衡条件**与基本极限定理的理论在 [3.5.9](/3.5.9)，两种算法也在那里首次引入；本章使用这些结果，并以显式链接引用。例子重访前面各章的模型：带 **Jeffreys 先验**的二项模型（[3.7.2](/3.7.2)）、带半共轭先验的正态模型（[3.7.5](/3.7.5)，§5.2），以及老鼠肿瘤与正态组均值的层次模型（[3.7.6](/3.7.6)）。全章记 $p(\theta\mid y)=q(\theta\mid y)/p(y)$，其中未归一化后验 $q(\theta\mid y)=p(y\mid\theta)p(\theta)$ 可以计算，归一化常数 $p(y)$ 不能；$g(\theta^*\mid\theta)$ 是**提议分布**。（[3.5.9](/3.5.9) 把目标写作 $\tilde\pi$、提议写作 $q$。）与前几章一样，$\Gamma(\alpha,\beta)$ 与 $\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$ 的形状参数为 $\alpha$，速率或尺度参数为 $\beta$。

## 10.1. Metropolis–Hastings 算法

### 10.1.1. 算法

该算法由 Metropolis、Rosenbluth、Rosenbluth、Teller 与 Teller（1953）针对对称提议提出，用于统计物理中状态方程的计算，Hastings（1970）把它推广到任意提议。它被普遍认为是统计计算中最重要的贡献之一。

**算法 10.1.1（Metropolis–Hastings）** 设 $p(\theta\mid y)\propto q(\theta\mid y)$ 为目标分布，$\theta^{(t)}$ 为当前状态。一次迭代如下：

1. 提议 $\theta^*\sim g(\theta\mid\theta^{(t)})$；
2. 以概率 $\min\{1,r\}$ 接受，即令 $\theta^{(t+1)}=\theta^*$，其中
   $$
   r=r\big(\theta^{(t)},\theta^*\big)=\frac{p(\theta^*\mid y)/g(\theta^*\mid\theta^{(t)})}{p(\theta^{(t)}\mid y)/g(\theta^{(t)}\mid\theta^*)}=\frac{q(\theta^*\mid y)\,g(\theta^{(t)}\mid\theta^*)}{q(\theta^{(t)}\mid y)\,g(\theta^*\mid\theta^{(t)})};\tag{10.1}
   $$
3. 否则留在原处，$\theta^{(t+1)}=\theta^{(t)}$。

常数 $p(y)$ 在 $r$ 中消去，所以只需要未归一化的后验。每个因子 $p(\theta\mid y)/g(\theta\mid\cdot)$ 是一个重要性比（目标密度除以提议密度），而接受比 $r$ 就是提议点与当前点处两个重要性比的比值。实际计算时第 2 步在对数尺度上进行：抽取 $u\sim\mathrm{U}(0,1)$，当 $\log u<\log r$ 时接受，其中 $\log r$ 是对数似然与对数先验之差。这样可以避免下溢，因为几百个观测下的 $q(\theta\mid y)$ 常常比最小的正浮点数还小。

两类 $g$ 的选择覆盖了大多数应用：

- 独立提议，$g(\theta^*\mid\theta^{(t)})=g(\theta^*)$，不依赖当前状态（§10.2）；
- 对称提议，对所有 $\theta^*,\theta^{(t)}$ 有 $g(\theta^*\mid\theta^{(t)})=g(\theta^{(t)}\mid\theta^*)$，此时 $r=q(\theta^*\mid y)/q(\theta^{(t)}\mid y)$；这就是最初的 **Metropolis 算法**，而取 $\theta^*=\theta^{(t)}+\varepsilon$（$\varepsilon$ 为对称增量）时就是**随机游走 Metropolis 算法**，这是应用最广的一种（§10.3）。

### 10.1.2. 为什么有效

对连续参数，Metropolis–Hastings 链的转移核有两部分：移到 $\theta^*\ne\theta$ 的密度，以及在 $\theta$ 处因拒绝而产生的点质量。记

$$
\alpha(\theta,\theta^*)=\min\big\{1,r(\theta,\theta^*)\big\},\qquad\rho(\theta)=1-\int g(\theta^*\mid\theta)\,\alpha(\theta,\theta^*)\,\mathrm{d}\theta^*,
$$
于是 $\rho(\theta)$ 是在 $\theta$ 处拒绝的概率，对集合 $A$ 有

$$
\mathbb{P}(\theta,A)=\mathbb{P}\big(\theta^{(t+1)}\in A\mid\theta^{(t)}=\theta\big)=\int_Ag(\theta^*\mid\theta)\,\alpha(\theta,\theta^*)\,\mathrm{d}\theta^*+\rho(\theta)\boldsymbol{1}_A(\theta).
$$

**定理 10.1.1** Metropolis–Hastings 链关于 $p(\theta\mid y)$ 满足细致平衡：

$$
p(\theta\mid y)\,g(\theta^*\mid\theta)\,\alpha(\theta,\theta^*)=p(\theta^*\mid y)\,g(\theta\mid\theta^*)\,\alpha(\theta^*,\theta)\quad\text{对所有 }\theta,\theta^*\text{ 成立}.
$$
因此 $p(\theta\mid y)$ 是该链的平稳分布：若 $\theta^{(t)}\sim p(\theta\mid y)$，则 $\theta^{(t+1)}\sim p(\theta\mid y)$。

**证明** 记 $p(\theta)$ 为 $p(\theta\mid y)$。把最小值乘开，

$$
p(\theta)\,g(\theta^*\mid\theta)\min\Big\{1,\frac{p(\theta^*)g(\theta\mid\theta^*)}{p(\theta)g(\theta^*\mid\theta)}\Big\}=\min\big\{p(\theta)g(\theta^*\mid\theta),\ p(\theta^*)g(\theta\mid\theta^*)\big\},
$$
它关于 $\theta$ 与 $\theta^*$ 对称，这就是细致平衡。再证平稳性：设 $\theta^{(t)}\sim p$，$A$ 为任一集合。则

$$
\mathbb{P}\big(\theta^{(t+1)}\in A\big)=\int\!\!\int_Ap(\theta)g(\theta^*\mid\theta)\alpha(\theta,\theta^*)\,\mathrm{d}\theta^*\,\mathrm{d}\theta+\int_Ap(\theta)\rho(\theta)\,\mathrm{d}\theta.
$$
由细致平衡，第一项等于 $\int_A\int p(\theta^*)g(\theta\mid\theta^*)\alpha(\theta^*,\theta)\,\mathrm{d}\theta\,\mathrm{d}\theta^*=\int_Ap(\theta^*)\big(1-\rho(\theta^*)\big)\,\mathrm{d}\theta^*$。加上第二项，得 $\int_Ap(\theta)\,\mathrm{d}\theta$。$\square$

这是 [定理 9.4.1](/3.5.9#thm-9.4.1) 的连续情形。只有平稳性并不保证链能够到达平稳分布。若再有：链能从任一起点到达每个后验概率为正的集合（例如只要 $p(\theta^*\mid y)>0$ 就有 $g(\theta^*\mid\theta)>0$，正态随机游走即是如此），并且链非周期（只要拒绝以正概率发生就成立），则 $\theta^{(t)}$ 的分布在全变差距离下收敛到 $p(\theta\mid y)$，沿链的平均收敛到后验期望。这是基本极限定理与遍历定理（[定理 9.3.3](/3.5.9#thm-9.3.3)）在一般状态空间上的版本，见 Tierney（1994）。

接受概率为什么取 $\min\{1,r\}$？因为它是与细致平衡相容的最大选择。

**命题 10.1.1** 设 $a(\theta,\theta^*)\in[0,1]$ 是任一接受概率，使得"从 $g$ 提议、以概率 $a$ 接受"的链关于 $p$ 满足细致平衡。则对所有 $\theta\ne\theta^*$ 有 $a(\theta,\theta^*)\le\min\{1,r(\theta,\theta^*)\}$，且 Metropolis–Hastings 的选择达到这个上界。

**证明** 从 $\theta$ 到 $\theta^*$ 的移动要满足细致平衡，须有 $p(\theta)g(\theta^*\mid\theta)a(\theta,\theta^*)=p(\theta^*)g(\theta\mid\theta^*)a(\theta^*,\theta)$，即 $a(\theta,\theta^*)=r(\theta,\theta^*)\,a(\theta^*,\theta)$。由 $a(\theta^*,\theta)\le1$ 得 $a(\theta,\theta^*)\le r(\theta,\theta^*)$，又按假设 $a\le1$。对 Metropolis–Hastings 的选择，$r(\theta,\theta^*)$ 与 $r(\theta^*,\theta)=1/r(\theta,\theta^*)$ 中至少有一个不小于 $1$，所以两个接受概率中一个等于 $1$，另一个等于 $r$，都取到所允许的最大值。$\square$

其他接受规则也满足细致平衡，例如 Barker 规则 $a=r/(1+r)$，但它们拒绝得更频繁。Peskun（1973）证明：对同一提议，更常离开当前状态的可逆链对 $\theta$ 的每个函数给出渐近方差更小的 Monte Carlo 估计；在这个意义上 $\min\{1,r\}$ 是最优的。

## 10.2. 独立 Metropolis–Hastings 算法

### 10.2.1. 算法

取独立提议 $g(\theta^*\mid\theta^{(t)})=g(\theta^*)$，式 (10.1) 化为

$$
r=\frac{q(\theta^*\mid y)/g(\theta^*)}{q(\theta^{(t)}\mid y)/g(\theta^{(t)})}=\frac{w(\theta^*)}{w(\theta^{(t)})},\qquad w(\theta)=\frac{q(\theta\mid y)}{g(\theta)}.
$$
这个算法也称**独立抽样器**。权重 $w$ 就是以 $g$ 为提议的**重要性抽样**（[3.7.9](/3.7.9)）中未归一化的重要性权重：若提议点的权重大于当前点，链必然移到 $\theta^*$，否则以概率 $w(\theta^*)/w(\theta^{(t)})$ 移动。因此好的独立提议就是好的重要性抽样提议：与后验接近，且尾部更重。

**例 10.2.1（正态–Cauchy 模型）** 设 $y\mid\theta\sim\mathcal{N}(\theta,1)$，先验取标准 **Cauchy 分布**，$\theta\sim t_1$。后验不是标准形式，

$$
p(\theta\mid y)\propto p(y\mid\theta)p(\theta)\propto\frac{\exp\big(-(y-\theta)^2/2\big)}{1+\theta^2}.
$$
取似然作提议，$g(\theta)=\mathcal{N}(\theta\mid y,1)$。此时似然相消，

$$
r=\frac{\exp\big(-(y-\theta^*)^2/2\big)\big/(1+(\theta^*)^2)}{\exp\big(-(y-\theta^{(t)})^2/2\big)\big/(1+(\theta^{(t)})^2)}\cdot\frac{\exp\big(-(\theta^{(t)}-y)^2/2\big)}{\exp\big(-(\theta^*-y)^2/2\big)}=\frac{1+(\theta^{(t)})^2}{1+(\theta^*)^2},
$$
即先验密度之比。对 $y=1$，后验相对提议向 $0$ 偏移（先验把它拉向 $0$），但两者重合得很好。链的混合良好，即使从很差的起始值 $\theta=10$ 出发，一步就能逃出：靠近后验的提议有 $r=(1+100)/(1+(\theta^*)^2)>1$，被接受。

![正态–Cauchy 模型的独立 Metropolis–Hastings 算法，y = 1，提议为 N(1, 1)。左：目标后验密度与提议密度。中、右：从 θ = 0 与从较差的起始值 θ = 10 出发的前 100 次迭代，标题给出接受率。](./plots/independence_mh.py)

### 10.2.2. 重尾

拒绝抽样要求提议的尾部覆盖目标的尾部，重要性抽样只有在权重方差有限时才有效（[3.7.9](/3.7.9)）。独立抽样器有同样的要求，原因很简单。设链位于尾部的某点 $\theta^{(t)}$，那里 $p(\theta^{(t)}\mid y)\gg g(\theta^{(t)})$，于是 $w(\theta^{(t)})$ 很大。典型的提议 $\theta^*$ 来自 $g$ 的主体部分，那里 $p(\theta^*\mid y)\approx g(\theta^*)$，故

$$
r=\frac{g(\theta^{(t)})\,p(\theta^*\mid y)}{p(\theta^{(t)}\mid y)\,g(\theta^*)}\approx0.
$$
链会在 $\theta^{(t)}$ 停留很久。这样的点很少被提议，但一旦被提议就会被接受，随后把链困住；长时间的平台补偿了尾部提议的稀少，所以平稳分布是对的，但收敛缓慢且不规则。当权重有界时，从任何起点出发收敛都很快：

**定理 10.2.1** 设对所有 $\theta$ 有 $w(\theta)=p(\theta\mid y)/g(\theta)\le M$（密度已归一化）。则对 $\theta^{(0)}$ 的任一初始分布 $\mu$，$\theta^{(t)}$ 的分布 $\mu_t$ 满足

$$
\lVert\mu_t-p(\cdot\mid y)\rVert_{\mathrm{TV}}\le\Big(1-\frac1M\Big)^t,
$$
且在平稳状态下接受率至少为 $1/M$。

**证明** 因为 $w(\theta^{(t)})\le M$，接受概率满足 $\min\{1,w(\theta^*)/w(\theta^{(t)})\}\ge\min\{1,w(\theta^*)/M\}=w(\theta^*)/M$。于是对每个 $\theta$ 与每个集合 $A$，

$$
\mathbb{P}(\theta,A)\ge\int_Ag(\theta^*)\frac{w(\theta^*)}{M}\,\mathrm{d}\theta^*=\frac{p(A\mid y)}{M}.
$$
令 $\varepsilon=1/M$。则 $R=(P-\varepsilon\,p)/(1-\varepsilon)$ 仍是转移核，且 $P=\varepsilon\,p+(1-\varepsilon)R$，其中 $p$ 表示忽略当前状态、直接从 $p(\cdot\mid y)$ 抽取的核。因为 $p$ 对 $P$ 平稳，$p=pP=\varepsilon p+(1-\varepsilon)pR$，所以 $pR=p$。对任意初始分布 $\mu$，$\mu P=\varepsilon p+(1-\varepsilon)\mu R$，故 $\mu P-p=(1-\varepsilon)(\mu-p)R$，归纳得 $\mu_t-p=(1-\varepsilon)^t(\mu-p)R^t$。转移核不增加全变差距离，且 $\lVert\mu-p\rVert_{\mathrm{TV}}\le1$，于是得到所述界。平稳状态下的接受率是 $\int p(\theta\mid y)\int g(\theta^*)\min\{1,w(\theta^*)/w(\theta)\}\,\mathrm{d}\theta^*\,\mathrm{d}\theta\ge\int g\,w/M=1/M$。$\square$

常数 $M$ 与以 $g$ 为提议的拒绝抽样的包络常数相同，后者恰以概率 $1/M$ 接受。反过来，Mengersen 与 Tweedie（1996）证明：若 $w$ 无界，独立抽样器就不以几何速率收敛。无界权重恰好就是轻尾提议对应重尾目标的情形。

**例 10.2.2（尾部很重要）** 取目标为 $t_1$、提议为 $\mathcal{N}(0,1)$。则 $\log w(\theta)=\theta^2/2-\log(1+\theta^2)+\text{常数}$ 无界增长。在 $1000$ 次迭代的一次运行中约 $86\%$ 的提议被接受，但轨迹图在 $\theta\approx\pm3$ 处出现平台：离开状态 $\theta$ 的概率是 $\int g(\theta^*)\min\{1,w(\theta^*)/w(\theta)\}\,\mathrm{d}\theta^*$，在 $\theta=2$ 处为 $0.64$，在 $\theta=3.2$ 处为 $0.069$，在 $\theta=3.6$ 处为 $0.023$，所以链平均在 $3.2$ 处停留 $14$ 次迭代，在 $3.6$ 处停留 $44$ 次。超出 $\pm4$ 的取值，其目标概率为 $\mathbb{P}(\lvert t_1\rvert>4)=0.156$，却几乎从不被提议，链只能靠在少数几个这样的值处停留很久来表示它们。

![尾部很重要：以标准正态为提议、以 t1 为目标的独立抽样器。左：log p(θ)/g(θ) 在两侧尾部都无界。右：1000 次迭代；链在 ±3 附近的少数取值处停留许多次迭代。](./plots/tail_matters.py)

## 10.3. 随机游走 Metropolis 算法

### 10.3.1. 算法

对称提议，例如一维的 $\theta^*\sim\mathcal{N}(\theta^{(t)},v^2)$ 或多维的 $\mathcal{N}(\theta^{(t)},S)$，使提议密度在式 (10.1) 中相消，

$$
r=\frac{q(\theta^*\mid y)}{q(\theta^{(t)}\mid y)}.
$$
链总是向上走，有时也向下走：这是爬山法的随机版本，它探索后验，而不是收敛到后验的众数。

**例 10.3.1（随机爬山）** 取目标为 $\mathcal{N}(0,1)$，当前值 $\theta^{(t)}=1$，提议 $\theta^*\sim\mathcal{N}(1,1)$。满足 $\lvert\theta^*\rvert<1$ 的提议使密度增大，总是被接受，其概率为 $\Phi(0)-\Phi(-2)=0.477$。满足 $\lvert\theta^*\rvert>1$ 的提议以概率 $\exp\big((1-(\theta^*)^2)/2\big)$ 被接受，刚越过区间边界时接近 $1$，远处则极小。总的来说，从 $\theta^{(t)}=1$ 出发的移动被接受的概率为

$$
\int\mathcal{N}(\theta^*\mid1,1)\min\Big\{1,\mathrm{e}^{(1-(\theta^*)^2)/2}\Big\}\,\mathrm{d}\theta^*=0.710.
$$

:::

对例 10.2.1 的正态–Cauchy 模型，随机游走提议 $\mathcal{N}(\theta^{(t)},v^2)$ 给出 $r=p(y\mid\theta^*)p(\theta^*)/\big(p(y\mid\theta^{(t)})p(\theta^{(t)})\big)$；尺度 $v$（例如 $v=1$）要由使用者选定。

### 10.3.2. 调节参数

提议的尺度是一个**调节参数**：它不影响平稳分布，但决定链探索平稳分布的速度。设提议是尺度为 $v$ 的对称分布，且 $\theta^{(t)}$（近似）服从 $p(\theta\mid y)$。

- 若 $v\approx0$，则 $\theta^*\approx\theta^{(t)}$，$r\approx1$：几乎所有提议都被接受，但链只迈出很小的步子，相继的状态高度相关。
- 若 $v\to\infty$，则 $\theta^*$ 通常远离后验的质量集中处，$q(\theta^*\mid y)\approx0$，$r\approx0$：几乎所有提议都被拒绝，链会在原地停留很久。

两个极端都低效，所以中间存在最优的尺度。高接受率本身并不是目标。

![正态–Cauchy 模型的随机游走 Metropolis 算法，y = 1，从 θ = 0 出发，提议为 N(θ(t), v²)。v = 0.1 时几乎每个提议都被接受，但链移动缓慢；v = 10 时大多数被拒绝，轨迹长时间平坦；v = 2.4 时混合良好。](./plots/rw_tuning.py)

对正态目标，接受率可以精确计算。

**命题 10.3.1** 设目标为 $\mathcal{N}(\mu,\sigma^2)$，提议为 $\theta^*=\theta^{(t)}+\ell\sigma Z$，$Z\sim\mathcal{N}(0,1)$。平稳状态下，随机游走 Metropolis 算法的接受率为

$$
\bar a(\ell)=\frac2\pi\arctan\frac2\ell.
$$

**证明** 标准化，使 $\mu=0$，$\sigma=1$，令 $X=\theta^{(t)}\sim\mathcal{N}(0,1)$，$Y=X+\ell Z$，$p$ 为目标的密度。接受率是 $\mathbb{E}\min\{1,p(Y)/p(X)\}$。在事件 $\{p(Y)\ge p(X)\}$ 上被积函数为 $1$。在其补集上，贡献为 $\int\!\!\int_{p(y)<p(x)}p(y)\,\phi_\ell(y-x)\,\mathrm{d}x\,\mathrm{d}y$，其中 $\phi_\ell$ 是 $\ell Z$ 的对称密度；交换 $x\leftrightarrow y$ 并利用 $\phi_\ell(y-x)=\phi_\ell(x-y)$，它等于 $\mathbb{P}\big(p(Y)>p(X)\big)$。因此接受率为 $2\,\mathbb{P}\big(p(Y)>p(X)\big)=2\,\mathbb{P}(Y^2<X^2)$。现在 $Y^2-X^2=\ell Z(2X+\ell Z)$，而 $(Z,\,2X+\ell Z)$ 是二元正态，相关系数 $c=\ell/\sqrt{4+\ell^2}$。对中心化的二元正态对，$\mathbb{P}(UV<0)=\frac12-\frac1\pi\arcsin c$。所以

$$
\bar a(\ell)=1-\frac2\pi\arcsin\frac{\ell}{\sqrt{4+\ell^2}}=1-\frac2\pi\arctan\frac\ell2=\frac2\pi\arctan\frac2\ell.\qquad\square
$$

接受率随 $\ell$ 增大从 $1$ 降到 $0$。以每次迭代的**有效样本量**（§10.6.3）度量的效率在 $\ell\approx2.4$ 附近最大，此时 $\bar a=0.44$。对高维目标有一个关于最优尺度（optimal scaling）的一般结果：

**定理 10.3.1（Roberts、Gelman 与 Gilks，1997）** 设目标是 $d$ 个相同的光滑一维密度的乘积，在标准化坐标下取提议 $\theta^*\sim\mathcal{N}_d\big(\theta^{(t)},(\ell^2/d)I_d\big)$。当 $d\to\infty$ 时，经适当加速的链的每个坐标收敛到一个扩散过程，其速度在 $\ell\approx2.38$ 时最大，此时接受率为 $0.234$。

对正态目标 $\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$，经线性变换把 $\Sigma$ 变成单位阵后，同样的结果成立，因此推荐的提议是

$$
\theta^*\sim\mathcal{N}_d\Big(\theta^{(t)},\ \frac{2.4^2}{d}\operatorname{Var}(\theta\mid y)\Big),
$$
其接受率在 $d=1$ 时约为 $44\%$，随 $d\to\infty$ 降到约 $23\%$。有两点要紧：尺度按 $1/\sqrt d$ 缩小，所以随机游走 Metropolis 算法每得到一个有效独立的抽样约需 $d$ 量级的迭代次数；提议的形状应与后验协方差相匹配，而不只是尺度。

![N(0, 1) 目标的随机游走 Metropolis 算法，正态提议的尺度为 l。左：精确的接受率 (2/π) arctan(2/l)；点线标出 l = 2.4 与接受率 0.44。右：由 40000 次迭代的链估计的每次迭代有效样本量，在 l = 2.4 附近达到峰值。](./plots/rw_scaling.py)

### 10.3.3. 例：二项模型

**例 10.3.2（二项模型）** 设 $y\mid\theta\sim\mathrm{Bin}(n,\theta)$，取 Jeffreys 先验 $\theta\sim\mathrm{Beta}(\frac12,\frac12)$（[3.7.2](/3.7.2)）。后验为

$$
p(\theta\mid y)\propto\theta^{y-1/2}(1-\theta)^{n-y-1/2}\,\boldsymbol{1}\{0<\theta<1\},
$$
即 $\mathrm{Beta}(y+\frac12,n-y+\frac12)$，所以结果可以核对。取随机游走提议 $\theta^*\sim\mathcal{N}(\theta^{(t)},0.4^2)$，以概率 $\min\{1,r\}$ 接受，

$$
r=\frac{(\theta^*)^{y-1/2}(1-\theta^*)^{n-y-1/2}\,\boldsymbol{1}\{0<\theta^*<1\}}{(\theta^{(t)})^{y-1/2}(1-\theta^{(t)})^{n-y-1/2}\,\boldsymbol{1}\{0<\theta^{(t)}<1\}}.
$$
$(0,1)$ 之外的提议有 $r=0$，被拒绝，这是正确的：提议仍是对称的，而目标在那里为零。取人工数据 $n=10$，$y=3$，起始值 $\theta^{(1)}=0.5$，迭代 $K=10\,000$ 次：

```r
n <- 10; y <- 3
log_q <- function(theta) {
  if (theta <= 0 || theta >= 1) return(-Inf)
  (y - 0.5) * log(theta) + (n - y - 0.5) * log(1 - theta)
}
K <- 10000
samps <- numeric(K); samps[1] <- 0.5
for (t in 1:(K - 1)) {
  cand <- rnorm(1, samps[t], 0.4)
  if (log(runif(1)) < log_q(cand) - log_q(samps[t])) {   # compare log(r) with log(u)
    samps[t + 1] <- cand
  } else {
    samps[t + 1] <- samps[t]
  }
}
length(unique(samps))/K   # acceptance rate
```

连续提议被接受的取值以概率 $1$ 互不相同，所以不同取值的个数就是接受的次数。接受率约为 $0.37$–$0.38$，略低于命题 10.3.1 的 $0.44$，原因是后验标准差为 $0.134$，尺度 $0.4$ 相当于 $\ell\approx3$。抽样的均值为 $0.319$、标准差为 $0.132$，而后验的精确均值为 $3.5/11=0.318$、标准差为 $0.134$。

![二项模型的随机游走 Metropolis 算法，n = 10，y = 3，Jeffreys 先验。左：前 1000 次迭代。右：K = 10000 个抽样的直方图与精确的 Beta(3.5, 7.5) 后验密度。](./plots/binomial_rw.py)

### 10.3.4. 调节参数的自适应

最优的提议协方差 $2.4^2\operatorname{Var}(\theta\mid y)/d$ 含有未知的后验协方差矩阵，可以用初步运行得到的抽样来估计。这提示我们分轮对提议做自适应。

**算法 10.3.1（提议的自适应调节）**

1. 取初始协方差矩阵 $S_0$，令 $b=0$。
2. 以提议协方差 $2.4^2S_b/d$ 运行 $M$ 次随机游走 Metropolis 迭代。
3. 令 $S_{b+1}$ 为迄今所有抽样的样本协方差矩阵。
4. 若 $b<B$，令 $b=b+1$ 并回到第 2 步；否则丢弃迄今所有抽样，转第 5 步。
5. 以固定的提议协方差 $2.4^2S_B/d$ 运行 $K$ 次迭代；用这些抽样做推断。

自适应阶段的抽样要丢弃，因为提议依赖于链自身过去的链已经不是 Markov 链，定理 10.1.1 的不变性论证对它不适用。第 5 步的提议固定之后，最后一次运行是普通的 Metropolis 链，无论提议是怎样找到的，它都有正确的平稳分布。一直持续自适应的自适应 MCMC（adaptive MCMC）方法（Haario、Saksman 与 Tamminen，2001）确实存在，但只有在附加条件下才收敛到正确的分布，例如自适应随时间衰减（Roberts 与 Rosenthal，2009）。

**例 10.3.3（正态模型）** 设 $y_i\mid\mu,\sigma\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$，对 $\mu$ 取平坦先验，对 $\sigma$ 取半 Cauchy 先验，$p(\mu,\sigma)\propto\frac{1}{1+\sigma^2}\boldsymbol{1}\{\sigma>0\}$。后验

$$
p(\mu,\sigma\mid y)\propto\frac{1}{\sigma^n}\exp\Big(-\frac{1}{2\sigma^2}\Big[\sum_{i=1}^ny_i^2-2\mu n\bar y+n\mu^2\Big]\Big)\frac{1}{1+\sigma^2}\boldsymbol{1}\{\sigma>0\}
$$
不是标准形式。对 $(\mu,\sigma)$ 联合运行随机游走 Metropolis 算法，提议为 $(\mu^*,\sigma^*)\sim\mathcal{N}_2\big((\mu^{(t)},\sigma^{(t)}),\,2.4^2S/2\big)$，并按算法 10.3.1 自适应地调整 $S$，人工数据 $n=20$，$y_i\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$，$B=10$，$M=100$，$(\mu^{(1)},\sigma^{(1)})=(0,1)$，$S_0=I_2$。在我们的一次运行中，十轮的接受率依次为

$$
0.00,\ 0.98,\ 0.96,\ 0.88,\ 0.61,\ 0.27,\ 0.30,\ 0.26,\ 0.35,\ 0.19.
$$
初始提议的标准差 $2.4/\sqrt2=1.7$ 远大于后验标准差（$\mu$ 约为 $0.2$，$\sigma$ 约为 $0.15$），第一轮没有一个提议被接受。常数链的样本协方差为零，所以加了一个小的岭项 $10^{-6}I_2$ 以保持 $S_1$ 正定；第二轮于是迈出很小的步子，几乎全部被接受，协方差的估计随抽样的离散程度增大，直到稳定。最后的 $K=10\,000$ 次迭代的接受率为 $0.31$，接近 $d=2$ 时的最优值；后验均值 $\mathbb{E}(\mu\mid y)\approx-0.17$、$\mathbb{E}(\sigma\mid y)\approx0.91$ 与样本均值 $\bar y=-0.18$、样本标准差 $s=0.87$ 接近，这与对 $\mu$ 取平坦先验、对 $\sigma$ 取模糊先验相符。第一轮表明，起始矩阵 $S_0$ 应当与后验同一量级，例如取自众数处的**正态近似**（[3.7.5](/3.7.5)）。

![正态模型的自适应随机游走 Metropolis 算法，n = 20，p(μ, σ) ∝ 1/(1 + σ²)。左、中：十轮自适应（每轮 100 次迭代，以点线分隔）中 μ 与 σ 的轨迹。右：最后一次运行的 10000 个抽样。](./plots/normal_adaptive.py)

同一程序适用于任何可以逐点计算的后验。对 [3.7.6](/3.7.6)（§6.5）的老鼠肿瘤模型，$y_j\mid\theta_j\sim\mathrm{Bin}(n_j,\theta_j)$，$\theta_j\mid\alpha,\beta\overset{\text{iid}}{\sim}\mathrm{Beta}(\alpha,\beta)$，$p(\alpha,\beta)\propto(\alpha+\beta)^{-5/2}$，把 $\theta_j$ 积分掉，得到超参数的边缘后验，

$$
p(\alpha,\beta\mid y)\propto\prod_{j=1}^J\frac{\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)}{\mathrm{B}(\alpha,\beta)}\,(\alpha+\beta)^{-5/2}\,\boldsymbol{1}\{\alpha>0,\beta>0\},\tag{10.2}
$$
这是自适应随机游走 Metropolis 算法的一个二维目标。它的等高线是 $(\alpha,\beta)$ 平面上一条细长弯曲的脊，所以链在 $\big(\log\frac\alpha\beta,\log(\alpha+\beta)\big)$ 尺度上工作得更好，那里目标更接近正态且没有约束；该尺度上的密度含有 Jacobi 因子 $\alpha\beta$。例 10.6.2 把这个抽样器与 §10.5 的其他方案作了比较。

## 10.4. Gibbs 抽样

Gibbs 抽样由 Geman 与 Geman（1984）为图像复原提出，其名称来自物理学家 J. Willard Gibbs，因为被抽样的分布与统计物理中的 Gibbs 分布相类似。Gelfand 与 Smith（1990）展示了它在贝叶斯计算中的威力，它从根本上改变了这一领域。其思想是把高维抽样问题拆成一系列低维问题。

### 10.4.1. 二分量 Gibbs 抽样

**算法 10.4.1（二分量 Gibbs 抽样）** 设 $\theta=(\theta_1,\theta_2)$，并设我们能从 $p(\theta_1\mid\theta_2,y)$ 与 $p(\theta_2\mid\theta_1,y)$ 抽样。从 $(\theta_1^{(0)},\theta_2^{(0)})$ 出发，第 $t$ 次迭代包括

1. 抽取 $\theta_1^{(t)}\sim p\big(\theta_1\mid\theta_2^{(t-1)},y\big)$；
2. 抽取 $\theta_2^{(t)}\sim p\big(\theta_2\mid\theta_1^{(t)},y\big)$。

要运行 Gibbs 抽样，必须导出每个分量的**完全条件分布**，即它在其余一切给定下的分布。实际做法是：把联合后验写到差一个常数，保留含有该分量的因子，并把结果辨认为某个标准分布。

**例 10.4.1（协方差已知的二元正态）** 取目标为**二元正态分布**

$$
\theta\sim\mathcal{N}_2(\boldsymbol{0},\Sigma),\qquad\Sigma=\begin{bmatrix}1&\rho\\\rho&1\end{bmatrix}.
$$
完全条件分布为 $\theta_1\mid\theta_2\sim\mathcal{N}(\rho\theta_2,1-\rho^2)$ 与 $\theta_2\mid\theta_1\sim\mathcal{N}(\rho\theta_1,1-\rho^2)$（[3.1.15](/3.1.15)），所以第 $t$ 次迭代先抽 $\theta_1^{(t)}\sim\mathcal{N}(\rho\theta_2^{(t-1)},1-\rho^2)$，再抽 $\theta_2^{(t)}\sim\mathcal{N}(\rho\theta_1^{(t)},1-\rho^2)$。每一步都平行于一条坐标轴；对 $\rho=0.9$，从起始值 $(-3,3)$ 出发，路径是沿密度窄脊的阶梯（§10.5 图的左图，以及 [例 9.5.1](/3.5.9#ex-9.5.1)）。

:::

在这个例子中，链的分布在每次迭代都可以算出。

**命题 10.4.1** 在例 10.4.1 中，对给定的 $\theta_2^{(0)}$ 与 $t\ge1$，

$$
\begin{bmatrix}\theta_1^{(t)}\\\theta_2^{(t)}\end{bmatrix}\sim\mathcal{N}_2\left(\begin{bmatrix}\rho^{2t-1}\theta_2^{(0)}\\\rho^{2t}\theta_2^{(0)}\end{bmatrix},\begin{bmatrix}1-\rho^{4t-2}&\rho-\rho^{4t-1}\\\rho-\rho^{4t-1}&1-\rho^{4t}\end{bmatrix}\right).
$$
因此 $(\theta_1^{(t)},\theta_2^{(t)})$ 的联合分布当 $t\to\infty$ 时收敛到目标，几何速率为 $\rho^2$。

**证明** 记 $\theta_1^{(t)}=\rho\theta_2^{(t-1)}+\sqrt{1-\rho^2}\,\varepsilon_t$，$\theta_2^{(t)}=\rho\theta_1^{(t)}+\sqrt{1-\rho^2}\,\eta_t$，其中 $\varepsilon_t,\eta_t$ 是相互独立的标准正态。于是

$$
\theta_2^{(t)}=\rho^2\theta_2^{(t-1)}+\rho\sqrt{1-\rho^2}\,\varepsilon_t+\sqrt{1-\rho^2}\,\eta_t,
$$
这是系数为 $\rho^2$、新息方差为 $(1-\rho^2)(\rho^2+1)=1-\rho^4$ 的 AR(1) 递推。归纳可知 $\theta_2^{(t)}$ 服从正态分布，均值为 $\rho^{2t}\theta_2^{(0)}$，方差为 $(1-\rho^4)\sum_{k=0}^{t-1}\rho^{4k}=1-\rho^{4t}$。其次，$\theta_1^{(t)}=\rho\theta_2^{(t-1)}+\sqrt{1-\rho^2}\,\varepsilon_t$ 的均值为 $\rho\cdot\rho^{2t-2}\theta_2^{(0)}=\rho^{2t-1}\theta_2^{(0)}$，方差为 $\rho^2(1-\rho^{4t-4})+1-\rho^2=1-\rho^{4t-2}$。最后 $\operatorname{Cov}\big(\theta_1^{(t)},\theta_2^{(t)}\big)=\operatorname{Cov}\big(\theta_1^{(t)},\rho\theta_1^{(t)}\big)=\rho(1-\rho^{4t-2})=\rho-\rho^{4t-1}$。所有项都是独立正态变量的线性组合，所以该向量是二元正态。当 $t\to\infty$ 时均值趋于 $\boldsymbol{0}$，协方差趋于 $\Sigma$，误差与 $\rho^{2t}$ 成正比。$\square$

速率 $\rho^2$ 也是平稳链每个坐标的滞后 1 自相关。一般地，二分量 Gibbs 抽样的收敛速率等于目标下 $\theta_1$ 与 $\theta_2$ 的最大相关系数的平方，即任意函数 $f(\theta_1)$ 与 $h(\theta_2)$ 之间的最大相关系数（Liu、Wong 与 Kong，1994）；对二元正态它就是 $\lvert\rho\rvert$。后验中各分量之间的相依越强，收敛越慢，所需迭代也越多（例 10.6.1）。

### 10.4.2. 例：半共轭先验的正态模型

**例 10.4.2（均值与方差都未知的正态模型）** 设 $y_i\mid\mu,\sigma^2\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$，$i=1,\dots,n$，先验相互独立：

$$
\mu\sim\mathcal{N}(m,C),\qquad\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(\nu,s^2).
$$
这不是 [3.7.3](/3.7.3) 的共轭先验（那里 $\mu$ 的先验方差与 $\sigma^2$ 成正比），边缘后验也不是标准分布（[3.7.5](/3.7.5) 的 §5.2 在网格上处理了它）。联合后验为

$$
p(\mu,\sigma^2\mid y)\propto(\sigma^2)^{-n/2}\exp\Big(-\frac{1}{2\sigma^2}\sum_{i=1}^n(y_i-\mu)^2\Big)\exp\Big(-\frac{(\mu-m)^2}{2C}\Big)\,(\sigma^2)^{-(\nu/2+1)}\exp\Big(-\frac{\nu s^2}{2\sigma^2}\Big).
$$
*$\mu$ 的完全条件分布。* 保留含 $\mu$ 的因子，并利用 $\sum_i(y_i-\mu)^2=\sum_i(y_i-\bar y)^2+n(\bar y-\mu)^2$，

$$
p(\mu\mid\sigma^2,y)\propto\exp\Big(-\frac{(\mu-\bar y)^2}{2\sigma^2/n}-\frac{(\mu-m)^2}{2C}\Big)\propto\exp\Big(-\frac12\Big[\Big(\frac{1}{\sigma^2/n}+\frac1C\Big)\mu^2-2\mu\Big(\frac{\bar y}{\sigma^2/n}+\frac mC\Big)\Big]\Big),
$$
所以 $\mu\mid\sigma^2,y\sim\mathcal{N}(m',C')$，其中

$$
C'=\Big(\frac{1}{\sigma^2/n}+\frac1C\Big)^{-1},\qquad m'=C'\Big(\frac{\bar y}{\sigma^2/n}+\frac mC\Big),
$$
这是 [3.7.2](/3.7.2)（§2.3）的精度加权组合。*$\sigma^2$ 的完全条件分布。* 保留含 $\sigma^2$ 的因子，

$$
p(\sigma^2\mid\mu,y)\propto(\sigma^2)^{-((\nu+n)/2+1)}\exp\Big(-\frac{1}{2\sigma^2}\Big[\nu s^2+\sum_{i=1}^n(y_i-\mu)^2\Big]\Big),
$$
所以 $\sigma^2\mid\mu,y\sim\mathrm{Inv}\text{-}\chi^2(\nu',s'^2)$，其中 $\nu'=\nu+n$，$\nu's'^2=\nu s^2+\sum_i(y_i-\mu)^2$。两个条件分布都是标准的，而**尺度逆卡方分布**的一个抽样为 $\nu's'^2/X$，$X\sim\chi^2_{\nu'}$。取 $\mathcal{N}(0,1)$ 的 $10$ 个模拟观测，先验参数 $m=0$，$C=10$，$\nu=1$，$s=1$，起始值 $\mu^{(0)}=0$，$\sigma^{2(0)}=1$，迭代 $1000$ 次：

```r
gibbs_normal <- function(y, m = 0, C = 10, nu = 1, s2 = 1, T = 1000) {
  n <- length(y); ybar <- mean(y)
  mu <- numeric(T + 1); sig2 <- numeric(T + 1)
  mu[1] <- 0; sig2[1] <- 1
  for (t in 2:(T + 1)) {
    Cp <- 1 / (n / sig2[t - 1] + 1 / C)
    mp <- Cp * (n * ybar / sig2[t - 1] + m / C)
    mu[t] <- rnorm(1, mp, sqrt(Cp))                     # mu | sigma^2, y
    sig2[t] <- (nu * s2 + sum((y - mu[t])^2)) / rchisq(1, nu + n)   # sigma^2 | mu, y
  }
  data.frame(mu = mu, sigma2 = sig2)
}
fit <- gibbs_normal(rnorm(10))
```

在我们的一次运行中，样本均值为 $\bar y=0.085$，链给出 $\mathbb{E}(\mu\mid y)\approx0.086$，$\mu$ 的 $95\%$ 后验区间为 $[-0.46,0.66]$，$\mathbb{E}(\sigma^2\mid y)\approx0.81$。对 $\mu$ 的模糊先验（方差为 $10$）几乎不对估计产生收缩。轨迹图看不出对起始值的依赖：$\mu$ 与 $\sigma^2$ 在后验中近似独立，所以二分量抽样器的混合几乎与独立抽样一样快。

![半共轭先验 μ ~ N(0, 10)、σ² ~ Inv-χ²(1, 1) 与 10 个观测下正态模型的 Gibbs 抽样：μ 与 σ² 在 1000 次迭代中的轨迹，以及联合抽样。](./plots/gibbs_normal.py)

### 10.4.3. K 分量 Gibbs 抽样

**算法 10.4.2（K 分量 Gibbs 抽样）** 设 $\theta=(\theta_1,\dots,\theta_K)$，每个 $\theta_k$ 可以是标量或向量。第 $t$ 次迭代由 $K$ 步组成：

$$
\begin{aligned}
\theta_1^{(t)}&\sim p\big(\theta_1\mid\theta_2^{(t-1)},\dots,\theta_K^{(t-1)},y\big),\\
\theta_2^{(t)}&\sim p\big(\theta_2\mid\theta_1^{(t)},\theta_3^{(t-1)},\dots,\theta_K^{(t-1)},y\big),\\
&\ \,\vdots\\
\theta_k^{(t)}&\sim p\big(\theta_k\mid\theta_1^{(t)},\dots,\theta_{k-1}^{(t)},\theta_{k+1}^{(t-1)},\dots,\theta_K^{(t-1)},y\big),\\
&\ \,\vdots\\
\theta_K^{(t)}&\sim p\big(\theta_K\mid\theta_1^{(t)},\dots,\theta_{K-1}^{(t)},y\big).
\end{aligned}
$$
每一步都以其余所有分量的最新取值为条件。记 $\theta_{-k}$ 为去掉第 $k$ 个分量的 $\theta$，并记 $p(\theta_k\mid\cdots)$ 为 $p(\theta_k\mid\theta_{-k},y)$。

**定义 10.4.1（Gibbs 抽样的变体）** 算法 10.4.2 按固定顺序更新各分量，称为**系统扫描 Gibbs 抽样**。**随机扫描 Gibbs 抽样**则在每一步随机（例如均匀地）选取一个分量 $k$，并从 $p(\theta_k\mid\theta_{-k},y)$ 更新它。**分块 Gibbs 抽样**把若干分量并成一个向量，从该块在其余分量给定下的条件分布中联合抽取整块。**折叠 Gibbs 抽样**先把某些分量从后验中解析地积分掉，再对其余分量的边缘后验运行抽样器；被积掉的分量若有需要，事后再从其条件分布中抽取。

分块与折叠都会减弱被分别更新的各分量之间的相依，因此通常加快收敛（Liu、Wong 与 Kong，1994）。随机扫描更便于分析，因为每一步都是可逆的；系统扫描在实践中更常用。

**例 10.4.3（层次正态模型）** 设

$$
y_{ij}\mid\mu_i,\sigma^2\overset{\text{iid}}{\sim}\mathcal{N}(\mu_i,\sigma^2),\qquad\mu_i\mid\eta,\tau^2\overset{\text{iid}}{\sim}\mathcal{N}(\eta,\tau^2),\qquad i=1,\dots,I,\ j=1,\dots,n_i,
$$
$n=\sum_in_i$，对 $\eta$ 取平坦先验，对两个方差取相互独立的逆 Gamma 先验，$p(\eta,\tau^2,\sigma^2)\propto\mathrm{Inv}\text{-}\Gamma(\tau^2\mid a_\tau,b_\tau)\,\mathrm{Inv}\text{-}\Gamma(\sigma^2\mid a_\sigma,b_\sigma)$。（回忆 $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)=\mathrm{Inv}\text{-}\Gamma(\nu/2,\nu s^2/2)$，[3.7.2](/3.7.2)。）联合后验为

$$
p(\mu,\eta,\sigma^2,\tau^2\mid y)\propto\prod_{i=1}^I\prod_{j=1}^{n_i}\mathcal{N}(y_{ij}\mid\mu_i,\sigma^2)\prod_{i=1}^I\mathcal{N}(\mu_i\mid\eta,\tau^2)\,\mathrm{Inv}\text{-}\Gamma(\tau^2\mid a_\tau,b_\tau)\,\mathrm{Inv}\text{-}\Gamma(\sigma^2\mid a_\sigma,b_\sigma),
$$
每个完全条件分布只保留含该分量的因子：

- $\mu_i$ 出现在第 $i$ 组的 $n_i$ 个数据因子与 $\mathcal{N}(\mu_i\mid\eta,\tau^2)$ 中。与例 10.4.2 同理，记 $\bar y_i=\frac1{n_i}\sum_jy_{ij}$，
  $$
  \mu_i\mid\cdots\sim\mathcal{N}\bigg(\Big(\frac{n_i}{\sigma^2}+\frac1{\tau^2}\Big)^{-1}\Big(\frac{n_i\bar y_i}{\sigma^2}+\frac{\eta}{\tau^2}\Big),\ \Big(\frac{n_i}{\sigma^2}+\frac1{\tau^2}\Big)^{-1}\bigg),
  $$
  且在 $(\eta,\sigma^2,\tau^2,y)$ 给定下各 $\mu_i$ 条件独立，所以 $p(\mu\mid\eta,\sigma^2,\tau^2,y)=\prod_{i=1}^Ip(\mu_i\mid\eta,\sigma^2,\tau^2,y)$。
- $\eta$ 只出现在 $\prod_i\mathcal{N}(\mu_i\mid\eta,\tau^2)$ 中，它是 $I$ 个均值为 $\eta$ 的观测 $\mu_i$ 的似然；取平坦先验时，$\eta\mid\cdots\sim\mathcal{N}(\bar\mu,\tau^2/I)$，其中 $\bar\mu=\frac1I\sum_{i=1}^I\mu_i$。
- $\sigma^2\mid\cdots\sim\mathrm{Inv}\text{-}\Gamma\Big(a_\sigma+\frac n2,\ b_\sigma+\frac12\sum_{i=1}^I\sum_{j=1}^{n_i}(y_{ij}-\mu_i)^2\Big)$。
- $\tau^2\mid\cdots\sim\mathrm{Inv}\text{-}\Gamma\Big(a_\tau+\frac I2,\ b_\tau+\frac12\sum_{i=1}^I(\mu_i-\eta)^2\Big)$。

所有完全条件分布都是标准的，并且由条件独立性，向量 $\mu$ 可以作为一个块来更新：这是一个分块 Gibbs 抽样，三个块为 $\mu$、$\eta$ 与 $(\sigma^2,\tau^2)$（两个方差也是条件独立的）。

### 10.4.4. 作为 Metropolis–Hastings 特例的 Gibbs 抽样

**命题 10.4.2** Gibbs 抽样第 $t$ 次迭代的第 $k$ 步是一个 Metropolis–Hastings 步，其目标为 $p(\theta\mid y)$，提议为

$$
g_k\big(\theta^*\mid\theta^{(t-1)}\big)=p\big(\theta_k^*\mid\theta_{-k}^{(t-1)},y\big)\,\boldsymbol{1}\big\{\theta_{-k}^*=\theta_{-k}^{(t-1)}\big\},
$$
其中 $\theta^{(t-1)}$ 表示这一步之前的当前状态。它的接受比为 $r\equiv1$，所以每个提议都被接受。

**证明** 该提议只改变第 $k$ 个分量，所以 $\theta_{-k}^*=\theta_{-k}^{(t-1)}$，反向提议为 $g_k(\theta^{(t-1)}\mid\theta^*)=p(\theta_k^{(t-1)}\mid\theta_{-k}^*,y)=p(\theta_k^{(t-1)}\mid\theta_{-k}^{(t-1)},y)$。由式 (10.1)，

$$
r=\frac{p(\theta^*\mid y)\big/p\big(\theta_k^*\mid\theta_{-k}^{(t-1)},y\big)}{p(\theta^{(t-1)}\mid y)\big/p\big(\theta_k^{(t-1)}\mid\theta_{-k}^{(t-1)},y\big)}=\frac{p\big(\theta_{-k}^{(t-1)}\mid y\big)}{p\big(\theta_{-k}^{(t-1)}\mid y\big)}\equiv1,
$$
因为对 $\theta^*$ 与 $\theta^{(t-1)}$ 都有 $p(\theta\mid y)/p(\theta_k\mid\theta_{-k},y)=p(\theta_{-k}\mid y)$，而它们共有分量 $\theta_{-k}$。$\square$

所以 Gibbs 抽样恰是提议总被接受的 Metropolis–Hastings 算法（二分量情形见 [命题 9.5.1](/3.5.9#prop-9.5.1)）。由定理 10.1.1，每一步都使 $p(\theta\mid y)$ 不变；一次完整扫描是 $K$ 个这样的步骤的复合，因此也使它不变，尽管系统扫描本身不是可逆的。不变性并不蕴含收敛：例如，若后验的支撑是两个正方形 $(0,1)^2$ 与 $(2,3)^2$ 的并，则从一个正方形中的点出发，没有任何逐坐标的移动能到达另一个，Gibbs 抽样不是不可约的（思考题 8）。对支撑连通且密度为正的后验，这种失败很少见，但各分量之间的强相依会造成命题 10.4.1 的缓慢混合。

## 10.5. Metropolis-within-Gibbs 算法

### 10.5.1. 算法

Gibbs 抽样假定每个完全条件分布 $p(\theta_k\mid\theta_{-k},y)$ 都能直接抽样。当其中有些不能时，可以用一个以该完全条件分布为目标的 Metropolis–Hastings 步来代替。

**算法 10.5.1（Metropolis-within-Gibbs）** 在第 $t$ 次迭代中，对 $k=1,\dots,K$：若 $p(\theta_k\mid\theta_{-k},y)$ 是标准分布，就直接从中抽取 $\theta_k^{(t)}$；否则提议 $\theta_k^*\sim g_k(\cdot\mid\theta_k^{(t-1)})$，并以概率 $\min\{1,r_k\}$ 令 $\theta_k^{(t)}=\theta_k^*$，其中

$$
r_k=\frac{p(\theta_k^*\mid\theta_{-k},y)\,g_k(\theta_k^{(t-1)}\mid\theta_k^*)}{p(\theta_k^{(t-1)}\mid\theta_{-k},y)\,g_k(\theta_k^*\mid\theta_k^{(t-1)})}=\frac{p(\theta_k^*,\theta_{-k}\mid y)\,g_k(\theta_k^{(t-1)}\mid\theta_k^*)}{p(\theta_k^{(t-1)},\theta_{-k}\mid y)\,g_k(\theta_k^*\mid\theta_k^{(t-1)})},
$$
否则令 $\theta_k^{(t)}=\theta_k^{(t-1)}$。这里 $\theta_{-k}$ 取其余分量的最新值。

$r_k$ 的第二种形式表明，完全条件分布不必归一化：只需未归一化的联合后验作为 $\theta_k$ 的函数。一个 Metropolis–Hastings 步就够了，无需把它迭代到收敛于完全条件分布，原因是下面的事实。

**命题 10.5.1** 设 $K_k(\theta_k\to\theta_k';\theta_{-k})$ 是第 $k$ 个分量上的转移核，对每个固定的 $\theta_{-k}$，它使完全条件分布 $p(\theta_k\mid\theta_{-k},y)$ 不变。则用 $K_k$ 更新 $\theta_k$、保持 $\theta_{-k}$ 不变，使联合后验 $p(\theta\mid y)$ 不变。

**证明** 若 $\theta\sim p(\theta\mid y)$，且 $\theta_k'$ 取自 $K_k(\theta_k\to\cdot\,;\theta_{-k})$，则 $(\theta_k',\theta_{-k})$ 的密度为

$$
\int p(\theta_{-k}\mid y)\,p(\theta_k\mid\theta_{-k},y)\,K_k(\theta_k\to\theta_k';\theta_{-k})\,\mathrm{d}\theta_k=p(\theta_{-k}\mid y)\,p(\theta_k'\mid\theta_{-k},y)=p(\theta_k',\theta_{-k}\mid y).\qquad\square
$$

从完全条件分布的精确抽取（Gibbs 步）、Metropolis–Hastings 步与拒绝抽样步都使完全条件分布不变，所以它们可以在一次扫描中随意混用。

**例 10.5.1（再看二元正态）** 对例 10.4.1 的目标，取 $\rho=0.9$、起始值 $(-3,3)$，用 Gibbs 步更新 $\theta_1$，$\theta_1^{(t)}\sim\mathcal{N}(\rho\theta_2^{(t-1)},1-\rho^2)$，用随机游走 Metropolis 步更新 $\theta_2$，提议为 $\theta_2^*\sim\mathcal{N}\big(\theta_2^{(t-1)},2.4^2(1-\rho^2)\big)$，目标为 $p(\theta_2\mid\theta_1^{(t)},y)=\mathcal{N}(\rho\theta_1^{(t)},1-\rho^2)$。提议的尺度就是 §10.3.2 中标准差为 $\sqrt{1-\rho^2}$ 的正态目标的最优尺度，所以 $\theta_2$ 步的接受率应约为 $0.44$；在我们 $1000$ 次迭代的一次运行中为 $0.45$。被拒绝的 $\theta_2$ 步使路径只留下一条水平线段，链沿脊的探索比 Gibbs 抽样稍慢。

![ρ = 0.9 的二元正态目标，从起始值 (−3, 3)（方块）出发。折线：前 20 次迭代，每次迭代包含 θ1 方向与 θ2 方向各一次移动；点：1000 次迭代中其余的抽样。左：Gibbs 抽样。右：θ2 采用随机游走步的 Metropolis-within-Gibbs 算法。](./plots/mwg_bivariate.py)

### 10.5.2. 例：半 Cauchy 先验的层次正态模型

**例 10.5.2** 在例 10.4.3 的层次正态模型中，把逆 Gamma 先验换成对标准差的半 Cauchy 先验（[3.7.6](/3.7.6) 的 §6.6 提到这类先验可作为 $\tau$ 的弱信息替代），

$$
p(\eta,\tau,\sigma)\propto\frac{1}{1+\sigma^2}\boldsymbol{1}\{\sigma>0\}\cdot\frac{1}{1+\tau^2}\boldsymbol{1}\{\tau>0\}.
$$
$\mu$ 与 $\eta$ 的完全条件分布不变。对方差，$\sigma$ 的先验对应于 $\sigma^2$ 的密度 $p(\sigma^2)=p(\sigma)\frac{\mathrm{d}\sigma}{\mathrm{d}\sigma^2}\propto\frac{1}{\sigma(1+\sigma^2)}$，所以记 $\mathrm{SS}=\sum_i\sum_j(y_{ij}-\mu_i)^2$，

$$
p(\sigma^2\mid\cdots)\propto(\sigma^2)^{-n/2}\mathrm{e}^{-\mathrm{SS}/(2\sigma^2)}\cdot(\sigma^2)^{-1/2}\frac{1}{1+\sigma^2}\propto\mathrm{Inv}\text{-}\Gamma\Big(\sigma^2\Bigm|\frac{n-1}2,\frac{\mathrm{SS}}2\Big)\frac{1}{1+\sigma^2},
$$
同理

$$
p(\tau^2\mid\cdots)\propto\mathrm{Inv}\text{-}\Gamma\Big(\tau^2\Bigm|\frac{I-1}2,\ \frac12\sum_{i=1}^I(\mu_i-\eta)^2\Big)\frac{1}{1+\tau^2}.
$$
（多出的因子 $(\sigma^2)^{-1/2}$ 是从 $\sigma$ 到 $\sigma^2$ 变换的 Jacobi 因子：写成 $\sigma$ 的函数，$\sigma$ 的条件密度正比于 $\sigma^{-n}\mathrm{e}^{-\mathrm{SS}/(2\sigma^2)}/(1+\sigma^2)$，是在 $\sigma^2$ 处取值、形状参数为 $n/2-1$ 的逆 Gamma 核，但 $\sigma^2$ 的抽取必须使用形状参数 $(n-1)/2$。）这些都不是标准密度。形如 $\mathrm{Inv}\text{-}\Gamma(\tau^2\mid a,b)\cdot\frac{1}{1+\tau^2}$ 的目标可以用几种方式抽样：

1. 以 $\tau^{*2}\sim\mathrm{Inv}\text{-}\Gamma(a,b)$ 为提议做拒绝抽样。因为 $\frac{1}{1+\tau^2}\le1$，包络常数为 $c=1$，$\tau^{*2}$ 以概率 $\frac{\mathrm{Inv}\text{-}\Gamma(\tau^{*2}\mid a,b)/(1+\tau^{*2})}{c\cdot\mathrm{Inv}\text{-}\Gamma(\tau^{*2}\mid a,b)}=\frac{1}{1+\tau^{*2}}$ 被接受。这给出精确的抽样，所以该步是一个 Gibbs 步。
2. 用同一提议做独立 Metropolis–Hastings 步。重要性权重为 $w(\tau^2)=1/(1+\tau^2)$，移动以概率 $\min\Big\{1,\dfrac{1/(1+\tau^{*2})}{1/(1+\tau^{(t)2})}\Big\}$ 被接受。权重有界，所以由定理 10.2.1 这一步表现良好。
3. 对 $\tau$（更好的是对 $\log\tau$，并计入 Jacobi 因子）做随机游走 Metropolis 步，以概率 $\min\{1,q(\tau^*\mid\mu,\eta,\sigma,y)/q(\tau^{(t)}\mid\mu,\eta,\sigma,y)\}$ 接受。

当 $\tau^2$ 通常很大时第一种方案失效，因为接受概率 $1/(1+\tau^{*2})$ 此时很小；第二种从不浪费提议；第三种需要调节，但完全不要求认出某个核。

### 10.5.3. 例：Beta–二项层次模型

**例 10.5.3（老鼠肿瘤）** 回忆 [3.7.6](/3.7.6)（§6.5）中 $J=71$ 个老鼠肿瘤实验的层次模型，

$$
y_j\mid\theta_j\overset{\text{ind}}{\sim}\mathrm{Bin}(n_j,\theta_j),\qquad\theta_j\mid\alpha,\beta\overset{\text{iid}}{\sim}\mathrm{Beta}(\alpha,\beta),\qquad p(\alpha,\beta)\propto(\alpha+\beta)^{-5/2}.
$$
对 $(\theta_1,\dots,\theta_J,\alpha,\beta)$ 的 Gibbs 抽样需要 $J+2$ 个完全条件分布。联合后验正比于 $\prod_jp(y_j\mid\theta_j)\prod_jp(\theta_j\mid\alpha,\beta)\,p(\alpha,\beta)$，所以

$$
p(\theta_i\mid\cdots)\propto\prod_{j=1}^J\theta_j^{y_j}(1-\theta_j)^{n_j-y_j}\,\theta_j^{\alpha-1}(1-\theta_j)^{\beta-1}\propto\theta_i^{\alpha+y_i-1}(1-\theta_i)^{\beta+n_i-y_i-1},
$$
即 $\theta_i\mid\cdots\sim\mathrm{Beta}(\alpha+y_i,\beta+n_i-y_i)$。对超参数，只有 $p(\theta\mid\alpha,\beta)p(\alpha,\beta)$ 含有它们：

$$
p(\alpha\mid\cdots)\propto\frac{\prod_{j=1}^J\theta_j^{\alpha-1}}{\mathrm{B}(\alpha,\beta)^J}(\alpha+\beta)^{-5/2},\qquad p(\beta\mid\cdots)\propto\frac{\prod_{j=1}^J(1-\theta_j)^{\beta-1}}{\mathrm{B}(\alpha,\beta)^J}(\alpha+\beta)^{-5/2},
$$
它们不是已知的密度。Metropolis-within-Gibbs 抽样用 Gibbs 步抽取每个 $\theta_j$，用随机游走 Metropolis 步更新 $\alpha$ 与 $\beta$，例如取提议 $\mathcal{N}(\alpha^{(t-1)},1)$ 与 $\mathcal{N}(\beta^{(t-1)},1)$，并拒绝非正的提议。在对数尺度上，目标为

$$
\begin{aligned}
\log p(\alpha\mid\cdots)&=(\alpha-1)\sum_{j=1}^J\log\theta_j-J\log\mathrm{B}(\alpha,\beta)-\frac52\log(\alpha+\beta)+\text{常数},\\
\log p(\beta\mid\cdots)&=(\beta-1)\sum_{j=1}^J\log(1-\theta_j)-J\log\mathrm{B}(\alpha,\beta)-\frac52\log(\alpha+\beta)+\text{常数}.
\end{aligned}
$$
有两种改进：

- *分块。* 在 $(\alpha,\beta)$ 给定下各 $\theta_j$ 条件独立，$p(\theta\mid\alpha,\beta,y)=\prod_jp(\theta_j\mid\alpha,\beta,y_j)$，所以对 $\theta_1,\dots,\theta_J$ 的 $J$ 个 Gibbs 步其实就是从联合条件分布中一次抽取整块 $\theta$。上面的抽样器是分块 Gibbs 抽样，块为 $\theta$、$\alpha$、$\beta$。
- *折叠。* 可以把 $\theta_j$ 解析地积分掉，得到 $(\alpha,\beta)$ 的 Beta–二项边缘后验 (10.2)。折叠抽样器只对 $p(\alpha,\beta\mid y)$ 运行 Metropolis（§10.3.4），然后对 $(\alpha,\beta)$ 的每个保留抽样，抽取 $\theta_j\sim\mathrm{Beta}(\alpha+y_j,\beta+n_j-y_j)$。链生活在二维空间而不是 $J+2$ 维中，它在 $(\alpha,\beta)$ 中的移动也不受当前 $\theta$ 的牵制：给定 $71$ 个值 $\theta_j$，$\alpha$ 的条件分布很窄，所以 Metropolis-within-Gibbs 链每一步只能把 $\alpha$ 移动一点点。

:::

例 10.6.2 在这些数据上比较了这三个抽样器。

## 10.6. 收敛性的评估

定理 10.1.1 与命题 10.5.1 保证了正确的平稳分布，基本极限定理保证了 $t\to\infty$ 时的收敛，但不告诉我们需要多少次迭代。实践中必须处理两个问题：早期的迭代仍然反映起始值；即使收敛之后，抽样也是相关的，所以长度为 $n$ 的链所含的信息少于 $n$ 个独立抽样。因此，基于迭代模拟的推断遵循一套常规程序（Gelman 等，2013）：从分散的起始值运行多条链，丢弃每条链的前一部分，检查各链之间以及每条链内部是否已经混合，并估计它们共提供了多少个有效独立的抽样。

### 10.6.1. 预烧期与多条链

每条链的最初一段，是它从起点移向后验质量所在区域的过程，这一段要丢弃：这就是**预烧期**。常见的默认做法是丢弃每条链的前一半；在例 10.3.3 中，整个自适应阶段起这个作用。为了发现尚未收敛的链，运行 $m\ge2$ 条链（通常 $4$ 条），其起始值分散在后验的合理范围之内或之外，再相互比较。抽样值对迭代序号的轨迹图（trace plot）直接显示未收敛：没有混合的链占据不同的区域、带有趋势或被困住（例 10.6.2 的图）。轨迹图一致是必要条件而非充分条件：几条链可以彼此一致，却都错过了远处的某个众数。

每条链还要拆成前后两半，得到 $2m$ 个序列。链内的非平稳性，例如缓慢的漂移，于是表现为同一条链前后两半之间的不一致。

### 10.6.2. 潜在尺度缩减

对一个标量摘要 $\psi$（某个参数或参数的函数），设 $\psi_{ij}$，$i=1,\dots,n$，$j=1,\dots,m$，是预烧并拆分之后 $m$ 个长度为 $n$ 的序列的抽样。

**定义 10.6.1（潜在尺度缩减因子）** 序列间方差与序列内方差分别为

$$
B=\frac{n}{m-1}\sum_{j=1}^m\big(\bar\psi_{\cdot j}-\bar\psi_{\cdot\cdot}\big)^2,\qquad W=\frac1m\sum_{j=1}^ms_j^2,\qquad s_j^2=\frac1{n-1}\sum_{i=1}^n\big(\psi_{ij}-\bar\psi_{\cdot j}\big)^2,
$$
其中 $\bar\psi_{\cdot j}=\frac1n\sum_i\psi_{ij}$，$\bar\psi_{\cdot\cdot}=\frac1m\sum_j\bar\psi_{\cdot j}$。边缘后验方差 $\operatorname{Var}(\psi\mid y)$ 用加权平均

$$
\widehat{\operatorname{var}}^+(\psi\mid y)=\frac{n-1}{n}W+\frac1nB
$$
估计，而**潜在尺度缩减因子**（分割 $\hat R$）为

$$
\hat R=\sqrt{\frac{\widehat{\operatorname{var}}^+(\psi\mid y)}{W}}.
$$

其动机是下面这一对事实。

**命题 10.6.1** 设 $m$ 个序列相互独立，且每个都是平稳的，边缘分布为 $p(\psi\mid y)$，方差为 $\sigma^2=\operatorname{Var}(\psi\mid y)$，序列均值为 $\bar\psi_{\cdot j}$。则

$$
\mathbb{E}\,\widehat{\operatorname{var}}^+=\sigma^2,\qquad\mathbb{E}\,W=\frac{n}{n-1}\Big(\sigma^2-\operatorname{Var}(\bar\psi_{\cdot j})\Big).
$$
特别地，只要 $\operatorname{Var}(\bar\psi_{\cdot j})>\sigma^2/n$，就有 $\mathbb{E}\,W<\sigma^2$；正自相关的链正是如此。

**证明** 记 $\mu=\mathbb{E}\psi_{ij}$。由于 $\sum_i(\psi_{ij}-\bar\psi_{\cdot j})^2=\sum_i\psi_{ij}^2-n\bar\psi_{\cdot j}^2$，

$$
\mathbb{E}\sum_{i=1}^n(\psi_{ij}-\bar\psi_{\cdot j})^2=n(\sigma^2+\mu^2)-n\big(\operatorname{Var}(\bar\psi_{\cdot j})+\mu^2\big)=n\big(\sigma^2-\operatorname{Var}(\bar\psi_{\cdot j})\big),
$$
由此得到 $\mathbb{E}s_j^2$，从而得到 $\mathbb{E}W$。序列均值 $\bar\psi_{\cdot1},\dots,\bar\psi_{\cdot m}$ 独立同分布，所以它们的样本方差 $B/n$ 的期望为 $\operatorname{Var}(\bar\psi_{\cdot j})$。因此 $\mathbb{E}\,\widehat{\operatorname{var}}^+=\frac{n-1}{n}\cdot\frac{n}{n-1}\big(\sigma^2-\operatorname{Var}(\bar\psi_{\cdot j})\big)+\operatorname{Var}(\bar\psi_{\cdot j})=\sigma^2$。对自相关为 $\rho_t$ 的平稳序列（见下面的命题 10.6.2），$\operatorname{Var}(\bar\psi_{\cdot j})=\frac{\sigma^2}{n}\big[1+2\sum_{t=1}^{n-1}(1-\frac tn)\rho_t\big]$，当 $\rho_t$ 为正时它超过 $\sigma^2/n$。$\square$

所以即使在平稳状态下，$W$ 也低估后验方差，因为每个序列还没有探索完整个分布，而 $\widehat{\operatorname{var}}^+$ 是无偏的。若起始值过度分散，则在各链忘记起始值之前，$\widehat{\operatorname{var}}^+$ 会高估方差。因此 $\hat R$ 往往大于 $1$，并随 $n\to\infty$ 降到 $1$；它估计的是：若继续模拟，$\psi$ 当前分布的尺度还可能缩小的倍数。Gelman 等（2013）把 $\hat R<1.1$ 视为可接受；更近的做法（Vehtari、Gelman、Simpson、Carpenter 与 Bürkner，2021）用秩正态化的分割 $\hat R$，并采用更严格的阈值 $1.01$。$\hat R$ 接近 $1$ 只是摘要 $\psi$ 已混合的证据，所以要对所有关心的参数计算它。

### 10.6.3. 有效样本量

链一旦混合，由抽样估计的后验均值的精度就取决于它们的自相关。

**命题 10.6.2** 设 $\psi_1,\psi_2,\dots$ 是方差为 $\sigma^2$、自相关为 $\rho_t=\operatorname{Corr}(\psi_i,\psi_{i+t})$ 的平稳序列，$\bar\psi_n=\frac1n\sum_{i=1}^n\psi_i$。则

$$
\operatorname{Var}(\bar\psi_n)=\frac{\sigma^2}{n}\Big[1+2\sum_{t=1}^{n-1}\Big(1-\frac tn\Big)\rho_t\Big],
$$
且若 $\sum_t\lvert\rho_t\rvert<\infty$，则 $n\operatorname{Var}(\bar\psi_n)\to\sigma^2\tau$，其中 $\tau=1+2\sum_{t=1}^\infty\rho_t$。

**证明** $\operatorname{Var}\big(\sum_{i=1}^n\psi_i\big)=\sum_{i,k}\operatorname{Cov}(\psi_i,\psi_k)=\sigma^2\big[n+2\sum_{t=1}^{n-1}(n-t)\rho_t\big]$，因为滞后为 $t$ 的点对有 $n-t$ 个；再除以 $n^2$。极限由控制收敛定理得出。$\square$

因子 $\tau$ 是积分自相关时间（integrated autocorrelation time）：$n$ 个相关的抽样估计均值的精度与 $n/\tau$ 个独立抽样相当。这是重要性抽样中加权样本的有效样本量（[3.7.9](/3.7.9)）在 Markov 链上的对应。

**定义 10.6.2（MCMC 抽样的有效样本量）** 对 $m$ 个长度为 $n$ 的序列，有效独立抽样个数为

$$
\hat n_{\mathrm{eff}}=\frac{mn}{1+2\sum_{t=1}^T\hat\rho_t},\qquad\hat\rho_t=1-\frac{V_t}{2\,\widehat{\operatorname{var}}^+},\qquad V_t=\frac{1}{m(n-t)}\sum_{j=1}^m\sum_{i=t+1}^n\big(\psi_{ij}-\psi_{i-t,j}\big)^2,
$$
其中求和在第一个满足 $\hat\rho_{T+1}+\hat\rho_{T+2}<0$ 的奇数 $T$ 处截断（可逆链相邻两个自相关之和为正，所以出现负的一对就表明是噪声）。后验均值估计 $\bar\psi_{\cdot\cdot}$ 的 **Monte Carlo 标准误**为 $\sqrt{\widehat{\operatorname{var}}^+/\hat n_{\mathrm{eff}}}$。

估计 $\hat\rho_t$ 用的是变差函数 $V_t$，因为 $\mathbb{E}(\psi_i-\psi_{i-t})^2=2\sigma^2(1-\rho_t)$，并综合了所有序列的信息；用 $\widehat{\operatorname{var}}^+$ 而不是 $W$，使得链没有混合时 $\hat n_{\mathrm{eff}}$ 很小。经验上，几百个有效抽样足以估计后验均值与中心区间，Vehtari 等（2021）建议（对四条链）至少约 $400$ 个，之后才信任 $\hat R$ 与 Monte Carlo 标准误。尾部分位数需要更多。每隔 $k$ 个只保留一个抽样（稀疏化）可以减少存储，但保留下来的抽样的有效样本量绝不会超过保留全部抽样时的有效样本量。

**例 10.6.1（二元正态的 Gibbs 抽样）** 由命题 10.4.1 的证明，平稳 Gibbs 链的每个坐标是系数为 $\phi=\rho^2$ 的 AR(1) 过程，所以 $\rho_t=\phi^t$，

$$
\tau=1+2\sum_{t=1}^\infty\phi^t=\frac{1+\phi}{1-\phi}=\frac{1+\rho^2}{1-\rho^2}.
$$
对 $\rho=0.9$，$\tau=9.53$：$1000$ 次迭代约值 $105$ 个独立抽样。对 $\rho=0.99$，$\tau=99.5$，$1000$ 次迭代约值 $10$ 个。

**例 10.6.2（比较老鼠肿瘤的抽样器）** 对例 10.5.3 的老鼠肿瘤后验运行三个抽样器，每个运行四条链，起始值分散为 $(\alpha,\beta)=(1,1),(5,30),(0.5,10),(4,8)$，每条链 $4000$ 次迭代，丢弃前 $1000$ 次：

1. Metropolis-within-Gibbs：对 $\theta$ 用 Gibbs（分块）步，对 $\alpha$ 与 $\beta$ 用随机游走步 $\mathcal{N}(\cdot,1)$；
2. 折叠抽样器，对式 (10.2) 的 $p(\alpha,\beta\mid y)$ 使用同样的逐分量随机游走步；
3. 折叠抽样器，对 $\big(\log\frac\alpha\beta,\log(\alpha+\beta)\big)$ 做联合随机游走，其提议协方差由算法 10.3.1（$B=10$，$M=100$）自适应得到。

由 $4\times3000$ 个保留抽样得到的 $\alpha$ 与 $\beta$ 的分割 $\hat R$ 与有效样本量为：

| 抽样器 | $\hat R(\alpha)$ | $\hat n_{\mathrm{eff}}(\alpha)$ | $\hat R(\beta)$ | $\hat n_{\mathrm{eff}}(\beta)$ |
|---|---|---|---|---|
| Metropolis-within-Gibbs | $1.12$ | $41$ | $1.13$ | $40$ |
| 折叠，逐分量 | $1.02$ | $79$ | $1.02$ | $73$ |
| 折叠，变换尺度上联合 | $1.001$ | $1998$ | $1.001$ | $1914$ |

三条链都有正确的平稳分布，并集中在 $\alpha\approx2.4$、$\beta\approx14$ 附近，但效率相差约 $50$ 倍。按 $\hat R<1.1$ 的准则，Metropolis-within-Gibbs 链尚未收敛：它在 $\alpha$ 与 $\beta$ 方向上的移动既受当前 $\theta$ 的限制，也受 $\alpha$ 与 $\beta$ 之间强后验相关的限制，其脊沿着近似不变的先验均值 $\alpha/(\alpha+\beta)\approx0.14$ 延伸。折叠消除了第一种限制，使有效样本量翻倍；在后验近似正态的变换尺度上的联合移动沿着脊前进，消除了第二种限制。教训具有一般性：变换到无约束且近似正态的参数，把能解析积分的部分积分掉，并把强相依的参数放在一起联合更新。

![老鼠肿瘤例子：每个抽样器四条链的 α 轨迹，起始于分散的取值；点线标出预烧期的结束。上：Metropolis-within-Gibbs。中：逐分量随机游走步的折叠抽样器。下：在 (log(α/β), log(α + β)) 上采用自适应联合随机游走的折叠抽样器。标题给出 α 的分割 R-hat 与有效样本量。](./plots/rats_samplers.py)

## 小结

| 算法 | 提议 | 接受比 $r$ | 要求与陷阱 |
|---|---|---|---|
| Metropolis–Hastings（算法 10.1.1） | 任意 $g(\theta^*\mid\theta^{(t)})$ | $\dfrac{q(\theta^*\mid y)\,g(\theta^{(t)}\mid\theta^*)}{q(\theta^{(t)}\mid y)\,g(\theta^*\mid\theta^{(t)})}$ | 只需未归一化后验；在对数尺度上计算 |
| 独立抽样器（§10.2） | $g(\theta^*)$ | $w(\theta^*)/w(\theta^{(t)})$，$w=q/g$ | $g$ 的尾部要比后验更重；$w\le M$ 有界时速率为 $(1-1/M)^t$（定理 10.2.1） |
| 随机游走 Metropolis（§10.3） | 对称，$\mathcal{N}(\theta^{(t)},S)$ | $q(\theta^*\mid y)/q(\theta^{(t)}\mid y)$ | 调节 $S\approx2.4^2\operatorname{Var}(\theta\mid y)/d$，接受率 $0.44$（$d=1$）至 $0.23$；先自适应、再固定（算法 10.3.1） |
| Gibbs 抽样（§10.4） | 完全条件分布 $p(\theta_k\mid\theta_{-k},y)$ | $\equiv1$（命题 10.4.2） | 完全条件分布须为标准分布；强相依时很慢（速率 $\rho^2$，命题 10.4.1） |
| Metropolis-within-Gibbs（§10.5） | 能用 Gibbs 步处用 Gibbs 步，否则用 MH 步 | $r_k$，以完全条件分布为目标 | 每一步都使后验不变（命题 10.5.1） |

- Metropolis–Hastings 算法之所以有效，靠的是细致平衡（定理 10.1.1），而 $\min\{1,r\}$ 是与之相容的最大接受概率（命题 10.1.1）。独立提议与拒绝抽样、重要性抽样的提议一样受重尾问题困扰；随机游走提议需要调节，接受率过高或过低都不好。
- Gibbs 抽样把高维抽样问题拆成低维的完全条件分布。若其中有些不是标准分布，就对这些分量使用拒绝抽样或 Metropolis–Hastings 步。分块与折叠（定义 10.4.1）减弱被分别更新的分量之间的相依；在层次模型中，组参数在超参数给定下条件独立，并常常可以积分掉（例 10.5.3）。
- 用若干条过度分散的链、预烧期、轨迹图、分割 $\hat R$（定义 10.6.1）与有效样本量（定义 10.6.2）评估收敛，并报告 Monte Carlo 标准误。在老鼠肿瘤例子（例 10.6.2）中，抽样器的选择使有效样本量相差 $50$ 倍。

## 思考题

1. 证明 Barker 接受概率 $a(\theta,\theta^*)=r/(1+r)$（$r$ 如式 (10.1)）满足细致平衡，并对 $r=0.5$ 与 $r=2$ 把它与 $\min\{1,r\}$ 比较。

   **答** 记 $p=p(\theta\mid y)$，$p^*=p(\theta^*\mid y)$，$g=g(\theta^*\mid\theta)$，$g^*=g(\theta\mid\theta^*)$，则 $r=p^*g^*/(pg)$。于是 $p\,g\,\frac{r}{1+r}=p\,g\,\frac{p^*g^*}{pg+p^*g^*}=\frac{pg\,p^*g^*}{pg+p^*g^*}$，它关于两点对称，所以细致平衡成立。对 $r=0.5$：$\min\{1,r\}=0.5$，Barker 给出 $1/3$。对 $r=2$：$1$ 对 $2/3$。Barker 规则总是更少接受，这与命题 10.1.1 一致；由 Peskun 定理，它给出更大的渐近方差。
2. 用提议 $\mathrm{Exp}(\lambda)$ 的独立抽样器抽样目标 $\mathrm{Exp}(1)$。$\lambda$ 取何值时权重有界？写出定理 10.2.1 的收敛界，并描述 $\lambda=2$ 时的行为。

   **答** $w(\theta)=\mathrm{e}^{-\theta}/(\lambda\mathrm{e}^{-\lambda\theta})=\lambda^{-1}\mathrm{e}^{(\lambda-1)\theta}$，它在 $(0,\infty)$ 上有界当且仅当 $\lambda\le1$，此时 $M=1/\lambda$。于是 $\lVert\mu_t-p\rVert_{\mathrm{TV}}\le(1-\lambda)^t$，平稳接受率至少为 $\lambda$。$\lambda=1$ 时提议就是目标，每次移动都被接受。$\lambda=2$ 时提议的尾部更轻：$w(\theta)=\frac12\mathrm{e}^{\theta}$ 无界，链一旦处于较大的 $\theta$，只以概率 $\mathrm{e}^{\theta^*-\theta}$ 接受提议 $\theta^*$，因此在那里停留约 $\mathrm{e}^{\theta}/\mathbb{E}_g\mathrm{e}^{\theta^*}=\mathrm{e}^{\theta}/2$ 次迭代；收敛不是几何的（Mengersen 与 Tweedie）。
3. 对 $\mathcal{N}(\mu,\sigma^2)$ 目标与随机游走提议 $\mathcal{N}(\theta^{(t)},v^2)$，提议标准差 $v$ 取何值给出接受率 $0.44$，取何值给出 $0.234$？在例 10.3.2 中，提议尺度为 $0.4$ 时，你预期的接受率大约是多少？

   **答** 由命题 10.3.1，接受率为 $\frac2\pi\arctan\frac{2\sigma}{v}$。解得 $v=2\sigma/\tan(\pi\bar a/2)$：对 $\bar a=0.44$，$v=2\sigma/\tan(0.691)=2.42\sigma$；对 $\bar a=0.234$，$v=5.19\sigma$。$0.234$ 是高维时的最优值；在一维中它对应的提议宽度是最优值的两倍多。在例 10.3.2 中，后验标准差为 $0.134$，所以 $\ell=0.4/0.134\approx3.0$，公式给出 $\frac2\pi\arctan(0.67)\approx0.37$，与观察到的 $0.37$–$0.38$ 接近，尽管 Beta 后验并不是正态的。
4. 对例 10.4.1 的 Gibbs 抽样，当 $\rho=0.5$、$0.9$、$0.99$ 时，要得到有效样本量 $1000$ 分别需要多少次迭代？$\rho=0.9$ 时迭代 $10\,000$ 次后，$\mathbb{E}\theta_1$ 的估计的 Monte Carlo 标准误是多少？

   **答** 由例 10.6.1，$\tau=(1+\rho^2)/(1-\rho^2)$：$\tau=1.67$、$9.53$、$99.5$，所以分别约需 $1700$、$9500$、$99\,500$ 次迭代。$\rho=0.9$、迭代 $10\,000$ 次时，$n_{\mathrm{eff}}\approx10\,000/9.53=1050$，又因为 $\operatorname{Var}\theta_1=1$，Monte Carlo 标准误为 $1/\sqrt{1050}\approx0.031$，而 $10\,000$ 个独立抽样的标准误为 $0.010$。
5. 设 $y_j\mid\theta_j\overset{\text{ind}}{\sim}\mathrm{Poi}(\theta_j)$，$\theta_j\mid\beta\overset{\text{iid}}{\sim}\Gamma(\alpha,\beta)$，其中 $\alpha$ 已知，$\beta\sim\Gamma(a,b)$，$j=1,\dots,J$。导出完全条件分布并描述 Gibbs 抽样。它是分块抽样器吗？

   **答** 联合后验正比于 $\prod_j\theta_j^{y_j}\mathrm{e}^{-\theta_j}\prod_j\frac{\beta^\alpha}{\Gamma(\alpha)}\theta_j^{\alpha-1}\mathrm{e}^{-\beta\theta_j}\,\beta^{a-1}\mathrm{e}^{-b\beta}$。保留含 $\theta_i$ 的因子：$\theta_i^{\alpha+y_i-1}\mathrm{e}^{-(\beta+1)\theta_i}$，所以 $\theta_i\mid\cdots\sim\Gamma(\alpha+y_i,\beta+1)$。保留含 $\beta$ 的因子：$\beta^{a+J\alpha-1}\mathrm{e}^{-(b+\sum_j\theta_j)\beta}$，所以 $\beta\mid\cdots\sim\Gamma(a+J\alpha,b+\sum_j\theta_j)$。每次迭代先抽取所有 $\theta_j$（在 $\beta$ 给定下条件独立，因此是一个块），再抽取 $\beta$：这是两个块的 Gibbs 抽样，两个条件分布都是共轭的，不需要 Metropolis 步。
6. 对无信息先验 $p(\mu,\sigma^2)\propto1/\sigma^2$ 的正态模型，导出两个完全条件分布。为什么这个模型不需要 Gibbs 抽样？

   **答** $p(\mu,\sigma^2\mid y)\propto(\sigma^2)^{-n/2-1}\exp\big(-\frac{1}{2\sigma^2}\sum_i(y_i-\mu)^2\big)$。作为 $\mu$ 的函数，它是 $\exp\big(-\frac{n(\mu-\bar y)^2}{2\sigma^2}\big)$，所以 $\mu\mid\sigma^2,y\sim\mathcal{N}(\bar y,\sigma^2/n)$。作为 $\sigma^2$ 的函数，它是 $(\sigma^2)^{-n/2-1}\exp\big(-\frac{1}{2\sigma^2}\sum_i(y_i-\mu)^2\big)$，所以 $\sigma^2\mid\mu,y\sim\mathrm{Inv}\text{-}\chi^2\big(n,\frac1n\sum_i(y_i-\mu)^2\big)$。但边缘后验是已知的，$\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(n-1,s^2)$（[3.7.3](/3.7.3)），所以可以先从边缘分布抽取 $\sigma^2$，再从 $\mathcal{N}(\bar y,\sigma^2/n)$ 抽取 $\mu$，直接得到独立抽样。只要能分解成边缘分布与条件分布，就总比迭代抽样器更可取。
7. 某参数 $\psi$ 的两条链（预烧之后）长度均为 $n=100$，均值分别为 $1.0$ 与 $2.0$，样本方差分别为 $1.0$ 与 $1.2$。计算 $B$、$W$、$\widehat{\operatorname{var}}^+$ 与 $\hat R$（不拆分）。你得到什么结论？

   **答** $\bar\psi_{\cdot\cdot}=1.5$，所以 $B=\frac{100}{1}\big[(1-1.5)^2+(2-1.5)^2\big]=50$，$W=\frac12(1.0+1.2)=1.1$。于是 $\widehat{\operatorname{var}}^+=\frac{99}{100}\cdot1.1+\frac{50}{100}=1.589$，$\hat R=\sqrt{1.589/1.1}=1.20$。两条链相差约一个链内标准差；它们没有混合，在报告 $\psi$ 的任何摘要之前，必须继续模拟（或改进抽样器）。
8. 设目标是开正方形 $(0,1)^2$ 与 $(2,3)^2$ 的并集上的均匀分布。证明 Gibbs 抽样不是不可约的，并给出两种修复方法。

   **答** 若 $\theta=(\theta_1,\theta_2)\in(0,1)^2$，则给定 $\theta_2\in(0,1)$ 时 $\theta_1$ 的完全条件分布是 $(0,1)$ 上的均匀分布，因为直线 $\{\theta_2=\text{常数}\}$ 只与第一个正方形相交；$\theta_2$ 同理。所以每一步都留在第一个正方形内，概率为 $\frac12$ 的第二个正方形永远到不了：平稳分布不唯一，从一个正方形出发的链把 $\mathbb{P}(\theta\in(2,3)^2)$ 估计为 $0$。修复方法：重新参数化，例如取 $u=\theta_1+\theta_2$、$v=\theta_1-\theta_2$，此时直线 $v=0$ 穿过两个正方形，于是 $v$ 接近 $0$ 时 $u$ 的条件分布把它们连通；或者加入同时改变两个坐标的 Metropolis–Hastings 移动，例如在 $(0,3)^2$ 上均匀的独立提议或大步长的随机游走，由命题 10.5.1 这是合法的（每个移动都使目标不变）。
9. 在算法 10.3.1 中，为什么要丢弃自适应阶段的抽样？构造一个简单的例子，说明依赖于过去的提议会给出错误的平稳分布。

   **答** 当提议依赖于先前的抽样时，$\theta^{(t+1)}$ 依赖的不只是 $\theta^{(t)}$，序列不是 Markov 链，定理 10.1.1 不适用。例：取目标为 $\{1,2,3\}$ 上的均匀分布，考虑两个对称提议，$g_a$ 为"留在原处"，$g_b$ 为"随机移到另外两个状态之一"。二者各给出一个使均匀分布不变的合法 Metropolis 核（$g_b$ 总是被接受）。现在让一个自适应规则按链的历史选择提议，比如链位于状态 $1$ 时取 $g_a$（因为"上一次进入状态 $1$ 的移动被接受了，所以不要改变好的做法"），否则取 $g_b$。每一个单独的步骤都是针对目标的 Metropolis 步，但链被吸收在状态 $1$，其长期频率为 $(1,0,0)$。按链所在或曾在之处在各个不变核之间做选择，会破坏不变性。在推断运行之前把提议固定下来，就恢复了具有正确平稳分布的时齐 Markov 链；持续的自适应只有在自适应衰减等条件下才是合法的。
