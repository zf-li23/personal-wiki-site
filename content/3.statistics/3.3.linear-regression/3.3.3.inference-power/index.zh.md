---
title: 统计推断与功效
description: 正态误差简单线性回归中的推断：斜率与截距估计量的抽样分布、t 检验与置信区间、零相关检验、Gauss–Markov 定理（BLUE）、用 Bonferroni 校正的联合推断，以及由非中心 t 分布计算的斜率检验的功效、功效曲线与样本量的确定。
source_hash: 89f43fb9aebe
---

最小二乘给出一条直线，但换一个样本就会得到另一条直线。估计的斜率 $b_1$ 可能离真实斜率 $\beta_1$ 多远？$\beta_1\ne0$ 的证据是否令人信服？本章在 [3.3.2](/3.3.2) 的正态误差回归模型下回答这些问题。先以正态均值为例回顾 [3.2.2](/3.2.2)–[3.2.5](/3.2.5) 的三个基本工具（**抽样分布**、检验与置信区间），再把它们用于 $\beta_1$ 和 $\beta_0$，建立最小二乘的最优性（**Gauss–Markov 定理**），并讨论一旦作出不止一个陈述或要规划一项研究就会出现的两个问题：关于 $(\beta_0,\beta_1)$ 的联合置信陈述，以及检验的功效，它决定研究需要多大的规模。平均响应的估计、预测与方差分析见 [3.3.4](/3.3.4)。

## 3.1. 回顾：统计推断的基础

### 3.1.1. 抽样分布

以正态均值为例。设 $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$。**样本均值**与**样本方差**

$$
\hat\mu=\bar X=\frac1n\sum_{i=1}^nX_i,\qquad\hat\sigma^2=s^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2
$$
分别估计中心（位置）与散布（变异性、离散程度）；$s^2$ 有 $n-1$ 个**自由度**，$\hat\sigma=s=\sqrt{s^2}$。作为估计量，$\bar X$ 随样本而变，因而是随机变量。它的分布，即对给定的样本量、统计量所有可能取值的概率分布，是它的**抽样分布**：$\bar X\sim\mathcal{N}(\mu,\sigma^2/n)$，均值相同，方差却小得多，$\sigma^2(\bar X)=\mathbb{E}(\bar X-\mu)^2=\sigma^2/n$。$\bar X$ 的抽样分布中的样本量是每个样本的容量 $n$，而不是抽取的样本个数。

**定义 3.1.1** 估计量 $\hat\theta$ 的**标准误**是其抽样分布的标准差的估计。对样本均值，$\hat\sigma^2(\bar X)=s^2/n$，

$$
\operatorname{SE}(\bar X)=s(\bar X)=\frac{s}{\sqrt n}.
$$

标准误是 $\bar X$ 偏离其目标 $\mu$ 的典型程度，说明 $\bar X$ 的精确程度。两个导出分布描述 $s^2$ 和标准化的均值。若 $Z_1,\dots,Z_k\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$，则 $U=Z_1^2+\cdots+Z_k^2$ 服从自由度为 $k$ 的**卡方分布** $\chi^2_k$，$\mathbb{E}(U)=k$，$\operatorname{Var}(U)=2k$。若再有 $Z_0\sim\mathcal{N}(0,1)$ 与 $U$ 独立，则 $T=Z_0/\sqrt{U/k}$ 服从自由度为 $k$ 的 **t 分布** $t_k$。

**定理 3.1.1** 设 $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$，则

1. $\bar X\sim\mathcal{N}(\mu,\sigma^2/n)$；
2. $(n-1)s^2/\sigma^2\sim\chi^2_{n-1}$；
3. $\bar X$ 与 $s^2$ 相互独立。

因此

$$
T=\frac{\bar X-\mu}{\operatorname{SE}(\bar X)}=\frac{\bar X-\mu}{s/\sqrt n}=\frac{(\bar X-\mu)/(\sigma/\sqrt n)}{\sqrt{\dfrac{(n-1)s^2}{\sigma^2(n-1)}}}\sim t_{n-1}.
$$

这就是 3.2.2 的[定理 2.1.3](/3.2.2#thm-2.1.3)，那里给出了证明；第 3 条中的独立性是正态分布的特殊性质。统计量 $T$ 以标准误为单位衡量 $\bar X$ 离其目标有多远。

### 3.1.2. 假设检验

检验在**原假设** $H_0$ 与**备择假设** $H_1$ 之间作出判断，可能犯两类错误：**第一类错误**（$H_0$ 为真时拒绝 $H_0$），其概率为 $\alpha=\mathbb{P}(\text{拒绝 }H_0\mid H_0\text{ 为真})$；以及**第二类错误**（$H_1$ 为真时未拒绝 $H_0$）。经典的原则是选择这样的判决规则：先把 $\alpha$ 控制在给定的**显著性水平**，再使犯第二类错误的概率尽可能小。检验的功效 $1-\mathbb{P}(\text{第二类错误})$ 依赖于 $H_1$ 中哪个参数值为真（第 3.6 节）。许多教材用 $\beta$ 表示犯第二类错误的概率；这里不这样写，因为 $\beta_0,\beta_1$ 表示回归系数。

**例 3.1.1** 清华男生的平均身高是否超过 $174$ cm？普查代价高昂，也没有必要；我们改为抽样并检验。随机抽取的 $15$ 名男生的身高（cm）为

$$
174,\ 171,\ 175,\ 174,\ 176,\ 177,\ 175,\ 171,\ 178,\ 177,\ 175,\ 179,\ 176,\ 174,\ 177,
$$
视为来自 $\mathcal{N}(\mu,\sigma^2)$ 的样本，$\bar x=175.27$，$s^2=5.21$，$s=2.28$。在 $\alpha=0.05$ 下检验 $H_0\colon\mu=174$ 对 $H_1\colon\mu>174$。观测到的统计量为

$$
t_0=\frac{175.27-174}{2.28/\sqrt{15}}=2.15.
$$
临界值法：上 $0.05$ 分位数为 $t_{14,0.05}=1.761$，$t_0>1.761$，故拒绝 $H_0$。$p$ 值法：对 $T\sim t_{14}$，$\mathbb{P}(T>t_0)=0.025$，小于 $0.05$，故拒绝 $H_0$。检验是显著的：数据支持清华男生的平均身高超过 $174$ cm。

对双侧问题 $H_0\colon\mu=\mu_0$ 对 $H_1\colon\mu\ne\mu_0$，检验统计量为 $T=(\bar X-\mu_0)/(s/\sqrt n)\overset{H_0}{\sim}t_{n-1}$。记 $t_0$ 为其观测值，

- 临界值法：若 $\lvert t_0\rvert>t_{n-1,\alpha/2}$，拒绝 $H_0$；
- **p 值**法：若 $\mathbb{P}(T\ge\lvert t_0\rvert)+\mathbb{P}(T\le-\lvert t_0\rvert)<\alpha$，拒绝 $H_0$。

### 3.1.3. 置信区间

满足 $\mathbb{P}\big(\mu\in(\bar X-c,\bar X+c)\big)=1-\alpha$ 的区间估计量 $(\bar X-c,\bar X+c)$ 是 $\mu$ 的**置信区间**，其**置信水平**为 $1-\alpha$。置信度是对程序而言的，描述它的长期表现：在许多样本中，比例为 $1-\alpha$ 的区间覆盖 $\mu$，而任何一个具体的区间要么覆盖 $\mu$，要么不覆盖。若数据不服从正态分布，该程序只是近似的（依据**中心极限定理**），实际的覆盖概率可能与名义水平不同。

由 $(\bar X-\mu)/(s/\sqrt n)\sim t_{n-1}$，

$$
\mathbb{P}\left(-t_{n-1,\alpha/2}<\frac{\bar X-\mu}{s/\sqrt n}<t_{n-1,\alpha/2}\right)=1-\alpha
\ \Longrightarrow\ 
\mathbb{P}\left(\bar X-t_{n-1,\alpha/2}\frac{s}{\sqrt n}<\mu<\bar X+t_{n-1,\alpha/2}\frac{s}{\sqrt n}\right)=1-\alpha,
$$
所以 $\mu$ 的 $100(1-\alpha)\%$ 置信区间为

$$
\left(\bar X-t_{n-1,\alpha/2}\frac{s}{\sqrt n},\ \bar X+t_{n-1,\alpha/2}\frac{s}{\sqrt n}\right).
$$
其中心是点估计 $\bar X$，半宽 $t_{n-1,\alpha/2}\operatorname{SE}(\bar X)$ 是误差界（margin of error），置信水平为 $1-\alpha$。

**例 3.1.2** 对例 3.1.1 的身高数据，$t_{14,0.025}=2.145$，平均身高的 $95\%$ 置信区间为

$$
175.27\pm2.145\times\frac{2.28}{\sqrt{15}}=(174.00,\ 176.53).
$$
我们有 $95\%$ 的把握认为清华男生的平均身高在 $174.00$ 到 $176.53$ cm 之间。

检验与区间是同一枚硬币的两面（[3.2.5](/3.2.5)）。对 $H_0\colon\mu=\mu_0$ 对 $H_1\colon\mu\ne\mu_0$，构造 $100(1-\alpha)\%$ 置信区间：若它包含 $\mu_0$，不拒绝 $H_0$；否则拒绝。这与双侧假设的临界值法和 $p$ 值法等价。对水平 $\alpha$ 的单侧假设，同样的临界点由 $100(1-2\alpha)\%$ 的双侧区间给出：在例 3.1.1 中，$90\%$ 区间的下限为 $175.27-1.761\times2.28/\sqrt{15}=174.23>174$，所以在 $\mu>174$ 的备择下拒绝 $H_0\colon\mu=174$，与例 3.1.1 一致；而 $95\%$ 区间只是勉强排除了 $174$（其双侧 $p$ 值为 $0.0496$）。

## 3.2. 关于斜率的推断

斜率通常是我们关心的参数。当 $\beta_1=0$ 时回归直线是水平的，对每个 $X$ 都有 $\mathbb{E}(Y)=\beta_0$，$Y$ 与 $X$ 之间没有线性关联；在方差相等的正态误差下，$Y$ 在 $X$ 各水平上的分布此时完全相同。

### 3.2.1. $b_1$ 的抽样分布

由 [3.3.2](/3.3.2)，最小二乘估计量 $b_1=S_{XY}/S_{XX}$ 无偏，且关于响应是线性的：

$$
b_1=\sum_{i=1}^n\frac{X_i-\bar X}{S_{XX}}Y_i=\sum_{i=1}^n\frac{X_i-\bar X}{S_{XX}}(\beta_0+\beta_1X_i+\varepsilon_i)=\beta_1+\sum_{i=1}^n\frac{X_i-\bar X}{S_{XX}}\varepsilon_i.
$$

**定理 3.2.1** 在正态误差回归模型下，

1. $b_1\sim\mathcal{N}\big(\beta_1,\sigma^2(b_1)\big)$，$\sigma^2(b_1)=\operatorname{Var}(b_1)=\sigma^2/S_{XX}$；
2. $(n-2)s^2/\sigma^2=\mathrm{SSE}/\sigma^2\sim\chi^2_{n-2}$，且 $s^2$ 与 $(b_0,b_1)$ 独立；
3. 记标准误 $s(b_1)=s/\sqrt{S_{XX}}$，其中 $s=\sqrt{\mathrm{MSE}}$，则

$$
\frac{b_1-\beta_1}{s(b_1)}\sim t_{n-2}.
$$

**证明** 第 1 条成立，因为 $b_1$ 是独立正态误差的线性组合，其均值与方差已在 [3.3.2](/3.3.2) 中算出。第 2 条是正态线性模型分布理论在 $p=2$ 时的特例，在 [3.3.7](/3.3.7) 中用矩阵方法证明（另见 [3.4.7](/3.4.7)）。对第 3 条，

$$
\frac{b_1-\beta_1}{s(b_1)}=\frac{(b_1-\beta_1)/\sigma(b_1)}{s(b_1)/\sigma(b_1)}=\frac{(b_1-\beta_1)/\sigma(b_1)}{\sqrt{\mathrm{SSE}/[\sigma^2(n-2)]}},
$$
即一个标准正态变量除以一个与之独立的 $\chi^2_{n-2}$ 变量除以其自由度后的平方根。$\square$

与正态均值相比，这里损失两个而不是一个自由度，因为在形成残差之前要估计两个参数。

### 3.2.2. 斜率的 t 检验

为检验 $H_0\colon\beta_1=0$ 对 $H_1\colon\beta_1\ne0$，关于 $\beta_1$ 的证据由 $b_1$ 概括，其不确定性由 $\sigma(b_1)=\sigma/\sqrt{S_{XX}}$ 描述，用 $s(b_1)=s/\sqrt{S_{XX}}$ 估计，其中 $s=\sqrt{\sum_i(Y_i-\hat Y_i)^2/(n-2)}$。关于 $H_0$ 的证据由检验统计量

$$
T=\frac{b_1-0}{s(b_1)}\overset{H_0}{\sim}t_{n-2}
$$
概括。在水平 $\alpha$ 下，若观测值满足 $\lvert t_0\rvert>t_{n-2,\alpha/2}$，则拒绝 $H_0$；等价地，若双侧 $p$ 值小于 $\alpha$。对单侧备择，或对 $H_0\colon\beta_1=c$（用 $T=(b_1-c)/s(b_1)$），检验统计量与判决规则作相应修改。在 `summary(lm(...))` 的 R 输出中，`t value` 一列是 $b_1/s(b_1)$，`Pr(>|t|)` 是双侧 $p$ 值；对 [3.3.2](/3.3.2) 的比萨数据，$t_0=9.3187/0.3099=30.07$，自由度 $11$，$p=6.5\times10^{-12}$。

检验的结论必须谨慎解读。若不拒绝 $H_0$，以下三种实际情况都有可能：

1. 我们犯了第二类错误：实际上 $\beta_1\ne0$，只是样本没有提供足够的证据；
2. $X$ 与 $Y$ 之间确实没有多少线性关系；
3. $X$ 与 $Y$ 之间有关系，但不是线性的。

若拒绝 $H_0$，以下三种实际情况都有可能：

1. 我们犯了第一类错误：实际上 $\beta_1=0$，但我们得到了一个不寻常的样本；
2. $X$ 与 $Y$ 之间的关系确实是线性的；
3. 线性函数对数据拟合得尚可，但曲线函数会拟合得更好。

因此，显著的斜率并不能证明线性模型是对的；其余的可能性要靠 [3.3.5](/3.3.5) 的诊断来处理。

### 3.2.3. 斜率的置信区间

由定理 3.2.1，$\mathbb{P}\big(\lvert b_1-\beta_1\rvert/s(b_1)<t_{n-2,\alpha/2}\big)=1-\alpha$，所以 $\beta_1$ 的 $100(1-\alpha)\%$ 置信区间为

$$
\big(b_1-t_{n-2,\alpha/2}\,s(b_1),\ b_1+t_{n-2,\alpha/2}\,s(b_1)\big).
$$

### 3.2.4. 零相关的检验

现在设 $(X_i,Y_i)$，$i=1,\dots,n$，是来自**二元正态分布**的随机样本，于是 $X$ 也是随机的。这时

$$
\mathbb{E}(Y\mid X=x)=\left(\mu_Y-\rho\frac{\sigma_Y}{\sigma_X}\mu_X\right)+\rho\frac{\sigma_Y}{\sigma_X}x=\beta_0+\beta_1x,\qquad\beta_1=\rho\frac{\sigma_Y}{\sigma_X},
$$
且给定各 $X_i$ 时正态误差回归模型成立。由于 $\sigma_X,\sigma_Y>0$，检验 $H_0\colon\rho=0$ 等价于检验 $H_0\colon\beta_1=0$；相应地，$b_1=r\,s_Y/s_X$，其中 $r$ 是样本**相关系数**。用 $r$ 表示，$t$ 统计量成为

$$
t=\frac{r\sqrt{n-2}}{\sqrt{1-r^2}}\overset{H_0}{\sim}t_{n-2},
$$
其证明见 [3.3.4](/3.3.4)。在 R 中这个检验是 `cor.test(x, y)`。当不清楚哪个变量是响应时，这种表述更自然，因为它对称地对待 $X$ 与 $Y$。

## 3.3. 关于截距的推断

类似地，$b_0=\bar Y-b_1\bar X$ 是各 $Y_i$ 的线性组合；由于 $\operatorname{Cov}(\bar Y,b_1)=0$（[3.3.2](/3.3.2)），

$$
b_0\sim\mathcal{N}\big(\beta_0,\sigma^2(b_0)\big),\qquad\sigma^2(b_0)=\sigma^2\left(\frac1n+\frac{\bar X^2}{S_{XX}}\right),\qquad s(b_0)=s\sqrt{\frac1n+\frac{\bar X^2}{S_{XX}}},
$$
且 $(b_0-\beta_0)/s(b_0)\sim t_{n-2}$。因此：

- $H_0\colon\beta_0=0$ 对 $H_1\colon\beta_0\ne0$ 的显著性检验：若 $\lvert b_0\rvert/s(b_0)>t_{n-2,\alpha/2}$，拒绝 $H_0$；单侧检验与 $H_0\colon\beta_0=c$ 的检验可相应导出；
- $\beta_0$ 的 $100(1-\alpha)\%$ 置信区间为 $\big(b_0-t_{n-2,\alpha/2}\,s(b_0),\ b_0+t_{n-2,\alpha/2}\,s(b_0)\big)$。

**注 3.3.1** 由这些公式可以得到几点实际结论。

1. 设计（即在哪里收集数据）很重要。模型的适用范围（scope）是数据所覆盖的解释变量的取值范围。方差 $\sigma^2(b_1)=\sigma^2/\sum_i(X_i-\bar X)^2$ 在各 $X_i$ 尽可能分散时最小，这为 $X_1,\dots,X_n$ 的配置和样本量的选择提供了依据；但所有点都放在范围两端的设计无法发现弯曲，因此实践中会保留一些中间水平。
2. 关于 $\beta_0$ 的推断通常没有意义：$X$ 的原点平移会改变 $\beta_0$，而 $X=0$ 可能不在模型的适用范围内。
3. 若误差不服从正态分布，但其分布大致对称，检验与区间是合理的近似，并随样本量增大而改善。

**例 3.3.1** 对 [3.3.2](/3.3.2) 的比萨数据，`confint(bc)` 给出 $95\%$ 置信限（标为 `2.5 %` 与 `97.5 %`）：

| | 2.5 % | 97.5 % |
|---|---|---|
| 截距 | $-116.43$ | $-5.81$ |
| year | $8.637$ | $10.001$ |

以 $95\%$ 的置信度，倾斜度每年增加 $0.86$ 到 $1.00$ 毫米。截距的区间没有意义：它说的是 1900 年的倾斜度，远在数据的适用范围之外。

## 3.4. Gauss–Markov 定理

现在建立最小二乘估计量的基本最优性。对来自均值为 $\mu=\mathbb{E}(Y)$、方差有限的总体的独立随机样本 $Y_1,\dots,Y_n$，样本均值 $\bar Y$ 在 $\mu$ 的所有线性无偏估计量 $\sum_ic_iY_i$ 中方差最小（无偏性要求 $\sum_ic_i=1$，而 $\sum_ic_i^2$ 在 $c_i=1/n$ 时最小）。

**定义 3.4.1** 若某参数的估计量关于观测 $Y_1,\dots,Y_n$ 是线性的、无偏的，并且在所有线性无偏估计量中方差最小，则称它为**最佳线性无偏估计**（BLUE）。

线性无偏估计量是无偏估计量的一个子类，因此 BLUE 不一定是所有无偏估计量中方差最小的；不过在正态误差下，最小二乘估计量确实也是如此（[3.2.3](/3.2.3)）。

**定理 3.4.1（Gauss–Markov 定理）** 在简单线性回归模型下（误差不相关，均值为 $0$，方差同为 $\sigma^2$，不要求正态性），最小二乘估计量 $b_0$ 和 $b_1$ 分别是 $\beta_0$ 和 $\beta_1$ 的最佳线性无偏估计。

**证明** 对 $b_1$ 证明。设 $\tilde\beta_1=\sum_ic_iY_i$ 是线性估计量。则 $\mathbb{E}(\tilde\beta_1)=\beta_0\sum_ic_i+\beta_1\sum_ic_iX_i$，因此 $\tilde\beta_1$ 对所有 $\beta_0,\beta_1$ 无偏当且仅当

$$
\sum_{i=1}^nc_i=0,\qquad\sum_{i=1}^nc_iX_i=1,
$$
而它的方差为 $\sigma^2\sum_ic_i^2$。最小二乘系数 $k_i=(X_i-\bar X)/S_{XX}$ 满足这两个约束。写 $c_i=k_i+d_i$，则 $\sum_id_i=0$，$\sum_id_iX_i=0$，从而 $\sum_ik_id_i=\big(\sum_id_iX_i-\bar X\sum_id_i\big)/S_{XX}=0$，并且

$$
\operatorname{Var}(\tilde\beta_1)=\sigma^2\sum_ic_i^2=\sigma^2\sum_ik_i^2+\sigma^2\sum_id_i^2\ge\sigma^2\sum_ik_i^2=\operatorname{Var}(b_1),
$$
等号仅当所有 $d_i=0$，即 $\tilde\beta_1=b_1$ 时成立。对 $b_0$ 的证明相同，约束换成 $\sum_ic_i=1$ 与 $\sum_ic_iX_i=0$。$\square$

从几何上看，$\beta_1$ 的线性无偏估计量的系数向量 $\boldsymbol{c}=(c_1,\dots,c_n)^{\mathsf T}$ 构成 $\mathbb{R}^n$ 中两个超平面 $\sum_ic_i=0$ 与 $\sum_ic_iX_i=1$ 的交，方差为 $\sigma^2\|\boldsymbol{c}\|^2$。BLUE 对应于这个仿射子空间中离原点最近的点，即垂足，也就是 $k_i=(X_i-\bar X)/\sum_j(X_j-\bar X)^2$ 构成的 $\boldsymbol{k}$。这个定理是最小二乘最有力的理由；多个预测变量时的矩阵形式是 3.2.3 的[定理 3.5.1](/3.2.3#thm-3.5.1)。

## 3.5. 截距与斜率的联合推断

置信区间是关于单个参数的陈述。对两个或更多参数，我们需要满足 $\mathbb{P}\big((\beta_0,\beta_1)\in S\big)=1-\alpha$ 的**置信域** $S\subset\mathbb{R}^2$。由于 $(b_0,b_1)^{\mathsf T}$ 服从均值为 $(\beta_0,\beta_1)^{\mathsf T}$、协方差矩阵与 $\sigma^2$ 成正比的二元正态分布，自然的（最小的）置信域是一个椭圆，

$$
\begin{bmatrix}b_0-\beta_0\\b_1-\beta_1\end{bmatrix}^{\mathsf T}\begin{bmatrix}n&\sum_iX_i\\\sum_iX_i&\sum_iX_i^2\end{bmatrix}\begin{bmatrix}b_0-\beta_0\\b_1-\beta_1\end{bmatrix}\le2\,\mathrm{MSE}\,F_{2,n-2,\alpha},
$$
其矩阵形式在 [3.3.7](/3.3.7) 中展开。更简单的做法是用矩形，即两个单独置信区间的乘积，

$$
S=\mathrm{CI}_0\times\mathrm{CI}_1=\{(\beta_0,\beta_1)\colon\beta_0\in\mathrm{CI}_0\text{ 且 }\beta_1\in\mathrm{CI}_1\}.
$$
若每个区间的水平都是 $1-\alpha$，矩形的水平就达不到：记 $A_j=\{\beta_j\in\mathrm{CI}_j\}$，

$$
\mathbb{P}(A_0\cap A_1)=1-\mathbb{P}(A_0^{\mathsf c}\cup A_1^{\mathsf c})\le1-\mathbb{P}(A_0^{\mathsf c})=1-\alpha,
$$
一般是严格不等式。必须调整每个区间的置信水平。由 Bonferroni 不等式，

$$
\mathbb{P}(A_0\cap A_1)\ge1-\mathbb{P}(A_0^{\mathsf c})-\mathbb{P}(A_1^{\mathsf c}),
$$
所以若每个区间的水平为 $1-\alpha/2$，矩形的水平至少为 $1-\alpha$。这就是 **Bonferroni 校正**（[3.2.4](/3.2.4)）：联合区间

$$
b_0\pm t_{n-2,\alpha/4}\,s(b_0),\qquad b_1\pm t_{n-2,\alpha/4}\,s(b_1)
$$
取代单独的区间 $b_j\pm t_{n-2,\alpha/2}\,s(b_j)$，它们的乘积是 $(\beta_0,\beta_1)$ 的水平至少为 $1-\alpha$ 的置信域。有 $g$ 个参数时，每个区间用 $\alpha/g$。

**例 3.5.1** 对比萨数据，用 $t_{11,0.0125}=2.593$ 代替 $t_{11,0.025}=2.201$，Bonferroni $95\%$ 联合置信区间为 $-126.3<\beta_0<4.0$ 与 $8.515<\beta_1<10.122$。两者都比例 3.3.1 的单独区间宽：联合陈述的代价是精度的损失。

## 3.6. 功效

### 3.6.1. 定义

显著性检验的功效（power）是在备择假设 $H_1$ 实际为真时拒绝原假设的概率，

$$
\text{功效}=1-\mathbb{P}(\text{第二类错误}).
$$
这个概率依赖于 $H_1$ 中参数的具体取值，作为该取值的函数，它就是检验的**功效函数**（[3.2.5](/3.2.5)），通常画成一条曲线。指导原则是：一旦设定了显著性水平，检验还应对 $H_1$ 中最关心的参数值具有恰当的功效：既不功效不足（很可能漏掉真实的效应），也不功效过度（浪费资源，并使可以忽略的效应变得显著）。

### 3.6.2. 斜率检验的功效与非中心 t 分布

对当 $\lvert b_1\rvert/s(b_1)>t_{n-2,\alpha/2}$ 时拒绝的 $H_0\colon\beta_1=0$ 对 $H_1\colon\beta_1\ne0$ 的检验，

$$
\operatorname{Power}(\beta_1)=\mathbb{P}\left(\frac{\lvert b_1\rvert}{s(b_1)}>t_{n-2,\alpha/2}\ \Big|\ \beta_1\right).
$$
在 $\beta_1=0$ 处，$\operatorname{Power}(0)=\alpha$，即犯第一类错误的概率。对 $\beta_1\ne0$ 出现了一个困难：$b_1\sim\mathcal{N}(\beta_1,\sigma^2(b_1))$ 的中心不在 $0$，$T=b_1/s(b_1)$ 不服从 $t_{n-2}$。

**定义 3.6.1** 设 $Z\sim\mathcal{N}(0,1)$ 与 $U\sim\chi^2_k$ 独立，$\delta\in\mathbb{R}$。

$$
T=\frac{Z+\delta}{\sqrt{U/k}}
$$
的分布称为自由度为 $k$、**非中心参数**为 $\delta$ 的**非中心 t 分布** $t_k(\delta)$。$\delta=0$ 时它就是通常的 $t_k$。

当 $\delta>0$ 时，密度向右移动且有偏斜，右尾更重。

**定理 3.6.1** 在正态误差回归模型下，

$$
T=\frac{b_1}{s(b_1)}\sim t_{n-2}(\delta),\qquad\delta=\frac{\beta_1}{\sigma(b_1)}=\frac{\beta_1\sqrt{S_{XX}}}{\sigma}.
$$

**证明** 写

$$
T=\frac{(b_1-\beta_1)+\beta_1}{s(b_1)}=\frac{\big[(b_1-\beta_1)+\beta_1\big]/\sigma(b_1)}{s(b_1)/\sigma(b_1)}=\frac{Z+\delta}{\sqrt{\mathrm{SSE}/[\sigma^2(n-2)]}},
$$
其中由定理 3.2.1，$Z=(b_1-\beta_1)/\sigma(b_1)\sim\mathcal{N}(0,1)$ 与 $\mathrm{SSE}/\sigma^2\sim\chi^2_{n-2}$ 独立。$\square$

因此

$$
\operatorname{Power}(\beta_1)=\mathbb{P}(T>t_{n-2,\alpha/2})+\mathbb{P}(T<-t_{n-2,\alpha/2}),\qquad T\sim t_{n-2}\big(\beta_1/\sigma(b_1)\big).
$$
要对不同的 $\beta_1$ 计算功效，需要知道或假定 $\sigma^2(b_1)=\sigma^2/\sum_i(X_i-\bar X)^2$，即设计 $X_1,\dots,X_n$ 和误差方差 $\sigma^2$，它们来自先验知识或预试验；然后用表或软件求出概率（在 R 中，`pt(q, df, ncp)` 是 $t_{df}(\mathrm{ncp})$ 的分布函数）。

为什么需要一个新的分布，而不是平移后的 $t$？诚然 $T-\beta_1/s(b_1)=(b_1-\beta_1)/s(b_1)\sim t_{n-2}$，于是

$$
\operatorname{Power}(\beta_1)=\mathbb{P}\left(T-\frac{\beta_1}{s(b_1)}>t_{n-2,\alpha/2}-\frac{\beta_1}{s(b_1)}\right)+\mathbb{P}\left(T-\frac{\beta_1}{s(b_1)}<-t_{n-2,\alpha/2}-\frac{\beta_1}{s(b_1)}\right).
$$
但平移量 $\beta_1/s(b_1)$ 含有随机的 $s$，所以这些并不是 $t_{n-2}$ 下固定事件的概率。像下例中那样代入估计值 $\beta_1/s(b_1)=1.5\sqrt{19800}/48.82=4.32$，只是对精确的非中心计算的近似，后者使用固定的 $\delta=\beta_1/\sigma(b_1)$。

**例 3.6.1（Toluca 公司）** 一家制冷设备制造商分批生产一种替换零件，批量大小不一，它想研究批量 $X$ 与工时 $Y$ 之间的关系。批量在 $20$ 到 $120$ 个单位之间，$n=25$，$S_{XX}=\sum_i(X_i-\bar X)^2=19800$，误差标准差的估计为 $s=48.82$；为作规划，假定 $\sigma^2=50^2=2500$。于是

$$
\sigma^2(b_1)=\frac{2500}{19800}=0.1263,\qquad\sigma(b_1)=0.355.
$$
设关心的斜率为 $\beta_1=1.5$（每单位的工时）。则 $\delta=1.5/0.355=4.22$，临界值为 $t_{23,0.025}=2.069$，

```r
c <- qt(1 - 0.025, df = 23)                                  # 2.0687
pt(-c, df = 23, ncp = 4.225) + 1 - pt(c, df = 23, ncp = 4.225)   # 0.981
```

所以 $\operatorname{Power}(1.5)=0.981$。汇总如下：

| $n$ | $\sigma^2$ | $S_{XX}$ | $\alpha$ | $\sigma^2(b_1)$ | 自由度 | $\beta_1$ | $\delta$ | $t_{23,0.025}$ | 功效 |
|---|---|---|---|---|---|---|---|---|---|
| $25$ | $2500$ | $19800$ | $0.05$ | $0.1263$ | $23$ | $1.5$ | $4.22$ | $2.0687$ | $0.981$ |

![左图：自由度为 23 的中心 t 分布与非中心参数为 4.22 的非中心 t 分布的密度；非中心密度下超出临界值正负 2.069 的阴影面积就是功效 0.981；右图：不同自由度与非中心参数的非中心 t 分布密度](./plots/noncentral-t-power.py)

### 3.6.3. 功效曲线

为了看出一系列斜率上的功效，选定一个范围（比如从 $-2$ 到 $2$），让 $\beta_1$ 取等间隔的值，对每个值计算 $\operatorname{Power}(\beta_1)$，并对 $\beta_1$ 作图：这就是检验的功效曲线（power curve）。

```r
find_power <- function(n, sig2, ssx, beta1, alpha) {
  sig2b1 <- sig2 / ssx                     # variance of b1
  df <- n - 2
  delta <- beta1 / sqrt(sig2b1)            # noncentrality parameter
  c <- qt(1 - alpha / 2, df)               # critical value
  1 - pt(c, df, delta) + pt(-c, df, delta)
}
beta1 <- seq(-2, 2, by = 0.05)
power <- sapply(beta1, function(b) find_power(25, 2500, 19800, b, 0.05))
plot(power ~ beta1, type = "l", ylab = "Power",
     main = "Power for the slope in simple linear regression")
```

曲线关于 $0$ 对称，在 $\beta_1=0$ 处等于 $\alpha=0.05$，随 $\lvert\beta_1\rvert$ 增大而增至 $1$。

![Toluca 情形（sigma^2 = 2500）下水平 0.05 的双侧 t 检验 beta_1 = 0 的功效曲线：n = 25、S_XX = 19800 时 beta_1 = 1 处的功效为 0.77，n = 45、S_XX = 35800 时为 0.96；两条曲线在 beta_1 = 0 处都等于 0.05](./plots/power-curve-slope.py)

### 3.6.4. 样本量的确定

在 Toluca 的例子中，$n=25$ 给出 $\operatorname{Power}(1.5)=0.98$，对实际应用已足够高。若关心的斜率改为 $\beta_1=1.0$，同样的计算给出 $\operatorname{Power}(1.0)=0.77$：研究的功效不足。设我们希望 $\operatorname{Power}(1)=0.95$。提高功效的主要途径是增大样本量 $n$ 并配合好的设计 $X_1,\dots,X_n$：两者都会增大 $S_{XX}=\sum_i(X_i-\bar X)^2$，从而增大 $\delta=\beta_1\sqrt{S_{XX}}/\sigma$。以同样的批量分布增加批次，每增加一批 $S_{XX}$ 增加 $800$：

| 样本量 | $S_{XX}$ | $\sigma^2$ | $\operatorname{Power}(1)$ |
|---|---|---|---|
| $30$ | $23800$ | $2500$ | $0.846$ |
| $35$ | $27800$ | $2500$ | $0.899$ |
| $40$ | $31800$ | $2500$ | $0.935$ |
| $45$ | $35800$ | $2500$ | $0.959$ |

因此合适的样本量是 $45$，设计使 $S_{XX}=35800$。

**例 3.6.2** 对来自已知方差为 $1$ 的正态总体的单个样本，在水平 $0.05$ 下检验 $H_0\colon\mu=0$ 对 $H_1\colon\mu=1$，要求功效为 $0.90$。基于 $n$ 个观测的 **Z 检验**在 $\sqrt n\bar X\ge z_{0.05}=1.645$ 时拒绝。它在 $\mu=1$ 处的功效为

$$
0.90=\mathbb{P}\big(\sqrt n\bar X\ge1.645\mid\mu=1\big)=\mathbb{P}\big(\sqrt n(\bar X-1)\ge1.645-\sqrt n\big)=1-\Phi(1.645-\sqrt n),
$$
所以 $1.645-\sqrt n=-z_{0.10}=-1.282$，$\sqrt n=2.927$，$n=8.56$：取 $n=9$。一般地，要用水平 $\alpha$ 的单侧 Z 检验以功效 $1-\gamma$ 检出均值偏移 $\Delta$，需要 $n\ge\big[(z_\alpha+z_\gamma)\sigma/\Delta\big]^2$。

### 3.6.5. 几点说明

- 双侧 $t$ 检验的公式、步骤和 R 代码很容易改用于单侧检验和关于 $\beta_0$ 的检验。
- 功效计算与样本量的确定是研究或试验设计的一部分，必须在实施之前仔细完成。研究重要时，应就功效计算、样本量和设计向有经验的应用统计学家咨询。
- 统计显著不等于实际显著。模型通常只是现实的近似，在许多情况下不看数据我们就知道点原假设是错的；不能拒绝它可能只是因为数据不够，按这种观点，检验变成了对样本量的检验。样本越大，$p$ 值越小，功效越大，越容易得到统计显著的结果，即使实际效应并不重要。
- 即使原假设没有被拒绝，置信区间也有用，因为它显示真实效应可能离原假设的值有多近。由于这些原因，置信区间一般比单纯的检验更可取。

## 小结

- 回顾：对正态样本，$\bar X\sim\mathcal{N}(\mu,\sigma^2/n)$ 与 $(n-1)s^2/\sigma^2\sim\chi^2_{n-1}$ 相互独立，所以 $(\bar X-\mu)/\operatorname{SE}(\bar X)\sim t_{n-1}$；由此得到 $t$ 检验、$p$ 值和置信区间 $\bar X\pm t_{n-1,\alpha/2}s/\sqrt n$。
- 斜率：$b_1\sim\mathcal{N}(\beta_1,\sigma^2/S_{XX})$，$s(b_1)=s/\sqrt{S_{XX}}$，$(b_1-\beta_1)/s(b_1)\sim t_{n-2}$；用 $\lvert b_1\rvert/s(b_1)>t_{n-2,\alpha/2}$ 检验 $H_0\colon\beta_1=0$，区间为 $b_1\pm t_{n-2,\alpha/2}s(b_1)$。对二元正态数据，这也是 $\rho=0$ 的检验。
- 截距：$b_0\sim\mathcal{N}\big(\beta_0,\sigma^2(1/n+\bar X^2/S_{XX})\big)$，有同类的检验和区间；通常不太重要。
- Gauss–Markov 定理：在误差不相关、同方差、均值为零时，$b_0,b_1$ 是 BLUE。
- 联合推断：两个单独的 $1-\alpha$ 区间的乘积的水平低于 $1-\alpha$；Bonferroni 校正对每个区间用 $t_{n-2,\alpha/4}$。
- 功效：$b_1/s(b_1)\sim t_{n-2}(\delta)$，$\delta=\beta_1\sqrt{S_{XX}}/\sigma$；功效随 $\lvert\beta_1\rvert$、$n$ 和 $X_i$ 的分散程度增大。应在研究之前规划样本量，并优先使用置信区间而不是单纯的显著性陈述。
