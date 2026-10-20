---
title: 自助法
description: 自助样本与自助原理；重抽样何时有效（Hadamard 可微性）；标准误与偏差的自助估计；正态、基本、百分位与 BCa 置信区间；自助假设检验；参数自助法。
source_hash: 3bc5799d7c02
---

**自助法**用来度量一个估计量的不确定性，尤其是在它的**抽样分布**无法推导的时候。它的三个主要用途是：估计估计量的偏差与**标准误**，构造参数的**置信区间**，以及对参数作假设检验。想法很简单：把观测到的样本当作总体，从中有放回地重抽样，并在每个重抽样本上重新计算统计量。形式上，未知的分布函数 $F$ 被**经验分布函数** $F_n$ 代替，统计量在 $F$ 下的抽样分布用它在 $F_n$ 下的分布来近似，而后者由**蒙特卡洛方法**（[3.1.12](/3.1.12)）计算。回归模型的自助法（对观测或残差重抽样）已在 [3.3.12](/3.3.12) 出现；本章讲一般的方法及其理论。本章用到重抽样的逆变换解释（[3.1.7](/3.1.7)）与 [3.2.4](/3.2.4) 的区间估计；每次重抽样背后的随机数发生器是 [3.5.8](/3.5.8) 的主题，重抽样检验在非参数统计（[3.6](/3.6)）中继续讨论。

## 7.1. 预备知识：抽样变异性

统计推断用样本中的信息认识整个总体，并追问结论有多准确。频率学派把参数看作固定（通常未知）的数，而样本统计量随样本不同而变化。统计量估计参数的准确程度取决于这种变化：统计量在不同样本间的取值越接近，估计就越准确。

**例 7.1.1** 美国人口普查称，25 岁及以上的美国成年人中有 $27.5\%$ 拥有学士或更高学位。在 $200$ 名这样的居民的随机样本中，有 $58$ 人拥有学位。总体参数是 $p=0.275$，样本统计量是 $\hat p=58/200=0.29$。从总体中抽取 $10\,000$ 个容量为 $200$ 的样本并分别计算 $\hat p$，就得到 $\hat p$ 的**抽样分布**的近似：同一总体中同一样本量的各个样本上统计量的分布。

统计量的**标准误** $\operatorname{se}(\hat\theta)$ 是其抽样分布的标准差，即统计量与参数之间的典型距离。标准误小意味着统计量在样本间变化不大。样本量很重要：$n$ 增大时变异减小，统计量趋于接近参数。

区间估计的形式是"点估计 $\pm$ 误差界"，误差界反映点估计的精度。**置信区间**由数据按某种方法算出，这种方法在所有样本中按指定的比例（即**置信水平**）覆盖参数。参数是固定的，变化的是区间。若抽样分布大致对称、呈钟形，$95\%$ 区间近似为

$$
\text{statistic}\pm 2\operatorname{se}.
$$
对正态的抽样分布，因子 $2$ 来自 68–95–99.7 法则（更精确地是 $z_{0.025}=1.96$）。没有正态性时，**Chebyshev 不等式** $\mathbb{P}(\lvert X-\mu\rvert\ge k\sigma)\le 1/k^2$ 只在 $k=\sqrt{20}\approx4.47$ 时保证 $95\%$ 的覆盖。

| 术语 | 含义 |
|---|---|
| 误差界 | 区间中对估计值加减的量 |
| 标准误 | 同样本量的重复样本上统计量的标准差 |
| 样本标准差 | 一个样本中各个观测值的标准差 |

在简单情形中，抽样分布与标准误可以用数学推导：正态样本的均值仍是正态的。但在大多数实际问题中分布过于复杂，而我们只有一个样本，无法抽取成千上万个样本。自助法只用这一个样本中的信息来近似抽样分布并估计标准误；自助方法是一类非参数的蒙特卡洛方法，通过重抽样估计统计量的分布特征。

## 7.2. 自助法基础

名称来自短语 "to pull oneself up by one's bootstraps"（拽着自己的靴带把自己提起来），一般认为出自 Raspe 的《敏豪森男爵奇遇记》：男爵掉进深湖湖底，靠拉自己的靴带把自己救了上来。理想情况下我们应从总体中反复抽样；关键想法是暂时假设总体就是观测样本的许多份拷贝。从这个假想总体中抽样，等同于从样本本身有放回地抽样。

### 7.2.1. 自助样本与自助原理

**定义 7.2.1（自助样本）** 设 $\boldsymbol{x}=(x_1,\dots,x_n)$ 是来自分布函数为 $F$ 的分布的观测随机样本。若 $X^*$ 是从 $\boldsymbol{x}$ 中随机选取的一个值，则

$$
\mathbb{P}(X^*=x_i)=\frac1n,\qquad i=1,\dots,n.
$$
从 $\boldsymbol{x}$ 中有放回地抽取 $n$ 次，得到独立同分布、在集合 $\boldsymbol{x}$ 上均匀分布的随机变量 $X_1^*,\dots,X_n^*$；$\boldsymbol{x}^*=(x_1^*,\dots,x_n^*)$ 称为一个**自助样本**。它与原样本的容量相同。

$X^*$ 的分布函数是**经验分布函数** $F_n(x)=\frac1n\sum_{i=1}^n\boldsymbol{1}\{x_i\le x\}$，它是 $F$ 的估计（由 **Glivenko–Cantelli 定理**，它几乎必然一致收敛到 $F$）。这就是自助原理（bootstrap principle）的依据：由于 $F_n\approx F$，有理由认为 $X^*\overset{d}{\approx}X$，且统计量满足 $T(\boldsymbol{X}^*)\overset{d}{\approx}T(\boldsymbol{X})$。换言之，$F_n$ 与自助世界的关系模仿了 $F$ 与真实世界的关系。从 $F_n$ 中抽样，恰好是对阶梯函数的**逆变换法**（见 [3.1.7 中 §7.3 的最后一例](/3.1.7#ex-7.3.1)）。

### 7.2.2. 自助分布

**算法 7.2.1（非参数自助法）** 设 $\theta$ 是感兴趣的参数，$\hat\theta=T(\boldsymbol{x})$ 是它的估计量。

1. 对 $b=1,\dots,B$：从 $x_1,\dots,x_n$ 中有放回地抽样，得到第 $b$ 个自助样本 $\boldsymbol{x}^{*(b)}=(x_1^*,\dots,x_n^*)$，并计算第 $b$ 个复制 $\hat\theta^{(b)}=T(\boldsymbol{x}^{*(b)})$。
2. $\hat\theta^{(1)},\dots,\hat\theta^{(B)}$ 的经验分布就是 $\hat\theta$ 的分布的自助估计。

**定义 7.2.2（自助分布）** 由一个自助样本算出的统计量称为自助统计量，或自助复制 $\hat\theta^*$；许多自助样本上的复制的分布称为 $\hat\theta$ 的**自助分布**。

若原样本是总体的随机样本，自助分布一般能在形状和离散程度上很好地近似抽样分布。但它以样本统计量 $\hat\theta$ 而非参数 $\theta$ 为中心，因此它估计的是 $\hat\theta$ 通常离 $\theta$ 多远，而不能把 $\hat\theta$ 移得更接近 $\theta$。例如，$500$ 个通勤时间的 $1000$ 个自助样本的均值分布在样本均值两侧约 $\pm3$ 分钟内，于是我们有把握说样本均值与总体均值相差在三分钟左右以内。

在 R 中这个循环只需几行；程序包 `boot` 把它封装起来，要求统计量写成 `function(data, indices)` 的形式：

```r
# generic bootstrap of a statistic theta_hat = stat(x)
B <- 2000; n <- length(x)
theta_star <- numeric(B)
for (b in 1:B) {
  xb <- sample(x, size = n, replace = TRUE)   # bootstrap sample
  theta_star[b] <- stat(xb)                   # bootstrap replicate
}
hist(theta_star)                              # always look at the bootstrap distribution

library(boot)
obj <- boot(data = x, statistic = function(x, i) stat(x[i]), R = B)
```

### 7.2.3. 自助法何时有效？

样本越大，自助法越准确，但自助法并不总是有效。应当始终画出自助分布：若它形态不佳，例如严重偏斜或分裂成孤立的簇，那么由它得到的区间就不太可信。对常用的大多数统计量，自助分布表现良好。下面的理论（选读）解释何时有效以及为什么。

重抽样有效，要求 $F_n$ 在 $F$ 附近轻微波动时统计量"表现良好"。把统计量写成泛函 $T(\boldsymbol{X})=\phi(F_n)$，参数写成 $\phi(F)$；自助法需要 $\phi$ 对函数的导数。在无穷维空间上的几种导数中，Fréchet 导数（对所有有界方向一致）太强：中位数和其他分位数都不是 Fréchet 可微的。Gâteaux 导数（沿固定直线）又太弱，无法把中心极限定理传递到 $\phi$ 上。合适的折中是下面的概念。

**定义 7.2.3（Hadamard 可微性）** 设 $\mathcal{D}$ 是一个函数赋范空间（对分布函数，取带上确界范数的有界函数空间）。称映射 $\phi\colon\mathcal{D}_\phi\subseteq\mathcal{D}\to\mathbb{R}$ 在 $F$ 处 **Hadamard 可微**，如果存在连续线性映射 $\phi'_F\colon\mathcal{D}\to\mathbb{R}$，使得

$$
\frac{\phi(F+t h_t)-\phi(F)}{t}\to\phi'_F(h)\qquad\text{for all } t\to0,\ h_t\to h \text{ with } F+th_t\in\mathcal{D}_\phi.
$$
等价地，Fréchet 近似在方向 $h$ 的紧集上一致成立。

只要求在紧集上就够了，因为经验分布函数的随机波动在极限下本身是"紧"的。由 Donsker 定理，$\sqrt n(F_n-F)$ 依分布收敛到 Brown 桥 $G_F$。这个极限是胎紧的（Prohorov 定理）：对任意 $\varepsilon>0$，它的样本路径以至少 $1-\varepsilon$ 的概率落在一个固定的连续函数紧集中。因此只控制这类良好方向的导数就足够了。

**定理 7.2.1（泛函 Delta 方法）** 若 $\phi$ 在 $F$ 处 Hadamard 可微（相切于连续函数），则

$$
\sqrt n\bigl(\phi(F_n)-\phi(F)\bigr)\xrightarrow{d}\phi'_F(G_F),
$$
这是正态分布 $\mathcal{N}(0,\sigma^2)$，$\sigma^2=\operatorname{Var}(\phi'_F(G_F))$。此外非参数自助法是相合的：在给定数据的条件下，$\sqrt n(\phi(F_n^*)-\phi(F_n))$ 依概率地依分布收敛到同一极限，其中 $F_n^*$ 是自助样本的经验分布函数。

这是 **Delta 方法**的无穷维推广。Hadamard 可微性是自助法有效的充分条件而非必要条件，但它解释了三种典型情形。

| 情形 | 例子 | 标准自助法的表现 |
|---|---|---|
| 光滑（本质上线性）的泛函，Fréchet 可微 | 样本均值 $\bar X$，最小二乘系数 $\hat{\boldsymbol\beta}$ | 效果很好 |
| 在样本层面有折点的泛函，当 $F$ 连续且在目标处密度为正时 Hadamard 可微 | **样本中位数**、其他分位数、分位数回归系数 | 若 $F$ 有密度且在中位数 $M$ 处 $f(M)=F'(M)>0$，大样本下有效；小样本时自助分布呈块状 |
| 完全不 Hadamard 可微 | 极值 $\max X_i$、$\min X_i$；真值为 $0$ 的 **Lasso** 系数 | 失效；极限分布不是正态的 |

对中位数，示性函数 $\boldsymbol{1}\{X\le x\}$ 使样本层面的泛函不光滑；对密度满足 $f(M)>0$ 的连续 $F$ 积分后，折点在总体层面被抹平。对最大值，统计量由单个边界点决定；对 Lasso，惩罚项 $\lambda\lvert\beta\rvert$ 在 $0$ 处有一个数据无法抹平的尖角。

**例 7.2.1** 设 $X_1,\dots,X_n$ 独立同分布于 $\mathrm{U}(0,\theta)$，$\hat\theta=X_{(n)}$。只要自助样本中含有 $x_{(n)}$，就重现样本最大值，所以

$$
\mathbb{P}^*\bigl(\hat\theta^*=\hat\theta\bigr)=1-\Bigl(1-\frac1n\Bigr)^n\to1-\mathrm{e}^{-1}\approx0.632,
$$
而 $\mathbb{P}(\hat\theta=\theta)=0$，且 $n(\theta-X_{(n)})/\theta$ 收敛到 $\mathrm{Exp}(1)$。自助分布有一个质量约为 $0.63$ 的原子，无法近似连续的抽样分布。

![来自 U(0, 1) 的一个容量为 50 的样本的自助分布。自助均值（左）构成光滑的钟形直方图；自助最大值（右）只取少数几个最大的观测值，约 63% 的质量集中在样本最大值本身。](./plots/bootstrap-mean-vs-max.py)

如何诊断块状的自助分布图：大的 $n$ 并不会自动修复标准自助法。

- 先问泛函在总体层面是否 Hadamard 可微。若不是（最大值、最小值、Lasso），标准自助法从根本上失效。
- 对只在 $F$ 连续时才可微的泛函（中位数），再问数据是否来自离散总体或有大量结。若是，可微性因离散而失效；若不是，说明 $n$ 太小，还不足以抹平样本层面的折点，更多数据会有帮助。

对不光滑的统计量有两种补救办法。

- 平滑自助法（smoothed bootstrap）在每个重抽到的点上加一个小的连续噪声，例如带宽为 $h$ 的 $\mathcal{N}(0,h^2)$。这相当于从**核密度估计量** $\tilde f_n$ 而不是阶梯函数 $F_n$ 中抽样；连续密度 $\tilde f_n>0$ 恢复了可微性。
- m-out-of-n 自助法（m-out-of-n bootstrap）抽取容量为 $m$ 而不是 $n$ 的重抽样本，其中 $m\to\infty$、$m/n\to0$。它不依赖泛函的一阶展开；较慢的收敛速度吸收了离散的跳跃。它在弱得多的条件下相合，最大值也包括在内。

## 7.3. 应用

### 7.3.1. 标准误

**定义 7.3.1（自助标准误）** 估计量 $\hat\theta$ 的**标准误**的自助估计，是自助复制 $\hat\theta^{(1)},\dots,\hat\theta^{(B)}$ 的样本标准差：

$$
\widehat{\operatorname{se}}(\hat\theta^*)=\sqrt{\frac{1}{B-1}\sum_{b=1}^B\bigl(\hat\theta^{(b)}-\bar\theta^*\bigr)^2},\qquad \bar\theta^*=\frac1B\sum_{b=1}^B\hat\theta^{(b)}.
$$

按 Efron 与 Tibshirani 的经验，良好地估计标准误所需的复制数不多：$B=50$ 通常足够，很少需要 $B>200$。置信区间依赖自助分布的尾部，需要大得多的 $B$（至少 $1000$）。

**例 7.3.1** R 程序包 `bootstrap` 中的数据集 `law` 包含 $15$ 所法学院的平均 LSAT 分数与平均 GPA，它是 `law82` 中 $82$ 所学院的一个随机样本。样本相关系数为 $r=0.776$（全部 $82$ 所学院的总体值为 $0.76$）。对这 $15$ 对数据整体重抽样（而不是分别对两个变量重抽样，那样会破坏相关性），得到的自助标准误约为 $0.13$；其精确值随随机种子而变。

```r
library(bootstrap)   # data sets law and law82
B <- 200; n <- nrow(law)
R <- numeric(B)
for (b in 1:B) {
  i <- sample(1:n, size = n, replace = TRUE)   # resample whole cases
  R[b] <- cor(law$LSAT[i], law$GPA[i])
}
cor(law$LSAT, law$GPA)   # theta_hat = 0.776
sd(R)                    # bootstrap standard error, about 0.13

library(boot)
r <- function(x, i) cor(x[i, 1], x[i, 2])
boot(data = law, statistic = r, R = 2000)   # reports original, bias and std. error
```

### 7.3.2. 偏差

**定义 7.3.2（偏差）** 估计量 $\hat\theta$ 对 $\theta$ 的**偏差**是 $\operatorname{Bias}(\hat\theta)=\mathbb{E}[\hat\theta]-\theta$；若它为零，$\hat\theta$ 是**无偏估计**。例如方差的极大似然估计 $\frac1n\sum_i(X_i-\bar X)^2$ 是有偏的。偏差的自助估计把 $\mathbb{E}[\hat\theta]$ 换成复制的均值、把 $\theta$ 换成 $\hat\theta$：

$$
\widehat{\operatorname{Bias}}(\hat\theta)=\frac1B\sum_{b=1}^B\hat\theta^{(b)}-\hat\theta=\bar\theta^*-\hat\theta.
$$

纠偏后的估计是 $\hat\theta-\widehat{\operatorname{Bias}}(\hat\theta)=2\hat\theta-\bar\theta^*$。纠偏会增加变异，所以只有当偏差相对标准误较大时才值得做；常用的经验法则是忽略小于 $0.25\,\widehat{\operatorname{se}}$ 的偏差。下面的各种区间同样可以按 $\widehat{\operatorname{Bias}}(\hat\theta)$ 平移。

**例 7.3.2** 对法学院数据，$r$ 的自助偏差很小（约 $-0.005$ 到 $-0.01$，随运行而变），相对标准误 $0.13$ 可以忽略。

数据 `patch`（程序包 `bootstrap`）记录了 $8$ 名受试者分别佩戴安慰剂贴片、旧贴片和新贴片后血液中某种激素的测量值。感兴趣的参数是

$$
\theta=\frac{\mathbb{E}(\text{new})-\mathbb{E}(\text{old})}{\mathbb{E}(\text{old})-\mathbb{E}(\text{placebo})}.
$$
若 $\lvert\theta\rvert\le0.2$，就认为新旧贴片生物等效。记 $y_i=\text{new}_i-\text{old}_i$，$z_i=\text{old}_i-\text{placebo}_i$，统计量为 $\hat\theta=\bar y/\bar z=-0.0713$。对受试者重抽样得到的偏差约为 $0.007$，标准误约为 $0.10$；偏差很小，$\lvert\widehat{\operatorname{Bias}}\rvert/\widehat{\operatorname{se}}<0.1$。

```r
library(bootstrap)
n <- nrow(patch); B <- 2000
theta_hat <- mean(patch$y) / mean(patch$z)
theta_b <- numeric(B)
for (b in 1:B) {
  i <- sample(1:n, size = n, replace = TRUE)   # resample subjects: keep (y, z) pairs
  theta_b[b] <- mean(patch$y[i]) / mean(patch$z[i])
}
bias <- mean(theta_b) - theta_hat
se <- sd(theta_b)
c(theta_hat = theta_hat, bias = bias, se = se, ratio = bias / se)
```

### 7.3.3. 自助置信区间

记 $\hat\theta^*_q$ 为自助分布的（下侧）$q$ 分位数，$\mathbb{P}^*(\hat\theta^*\le\hat\theta^*_q)=q$，用复制的相应样本分位数估计；记 $z_{\alpha/2}=\Phi^{-1}(1-\alpha/2)$ 为 $\mathcal{N}(0,1)$ 的上 $\alpha/2$ 分位数。

**定义 7.3.3（正态自助区间）** 若 $\hat\theta$（近似）无偏且服从正态，$\hat\theta\overset{\cdot}{\sim}\mathcal{N}(\theta,\operatorname{se}(\hat\theta)^2)$，则近似 $100(1-\alpha)\%$ 的**正态自助区间**为

$$
\hat\theta\pm z_{\alpha/2}\,\widehat{\operatorname{se}}(\hat\theta^*).
$$

典型情形是样本均值（由**中心极限定理**）和误差独立同正态分布的线性回归系数 $\hat\beta$。函数 `boot.ci` 把这个区间的中心取为纠偏后的估计 $\hat\theta-\widehat{\operatorname{Bias}}$。

**定义 7.3.4（基本自助区间）** 设 $a_q$ 是 $\hat\theta-\theta$ 的 $q$ 分位数，即 $\mathbb{P}(\hat\theta-\theta\le a_q)=q$。则 $\mathbb{P}(\hat\theta-\theta>a_\alpha)=1-\alpha$，即 $\mathbb{P}(\theta<\hat\theta-a_\alpha)=1-\alpha$，于是 $(\hat\theta-a_{1-\alpha/2},\hat\theta-a_{\alpha/2})$ 是精确的 $100(1-\alpha)\%$ 区间。$\hat\theta-\theta$ 的分布未知；按自助原理用 $\hat\theta^*-\hat\theta$ 的分布近似它，后者的 $q$ 分位数是 $\hat\theta^*_q-\hat\theta$，因为 $q=\mathbb{P}^*(\hat\theta^*\le\hat\theta^*_q)=\mathbb{P}^*(\hat\theta^*-\hat\theta\le\hat\theta^*_q-\hat\theta)$。代入得到**基本自助区间**（也称经验自助区间）

$$
\bigl(2\hat\theta-\hat\theta^*_{1-\alpha/2},\ 2\hat\theta-\hat\theta^*_{\alpha/2}\bigr).
$$

**定义 7.3.5（百分位区间）** **百分位区间**直接取自助分布的分位数：

$$
\bigl(\hat\theta^*_{\alpha/2},\ \hat\theta^*_{1-\alpha/2}\bigr).
$$

百分位区间因简单而有吸引力，但它依赖于由某一个样本得到的自助分布能很好地近似 $\hat\theta$ 的真实分布。它具有变换不变性：对单调的 $g$，$g(\theta)$ 的百分位区间就是 $\theta$ 的百分位区间的像。它的弱点是中位数偏差：若 $\hat\theta$ 不是中位数无偏的，这个区间会"自信地"出错。

**定义 7.3.6（BCa 区间）** $100(1-\alpha)\%$ 的**偏差校正加速区间**（BCa 区间）为 $(\hat\theta^*_{\alpha_1},\hat\theta^*_{\alpha_2})$，其中调整后的水平为

$$
\alpha_1=\Phi\Bigl(\hat z_0+\frac{\hat z_0-z_{\alpha/2}}{1-\hat a(\hat z_0-z_{\alpha/2})}\Bigr),\qquad
\alpha_2=\Phi\Bigl(\hat z_0+\frac{\hat z_0+z_{\alpha/2}}{1-\hat a(\hat z_0+z_{\alpha/2})}\Bigr).
$$
这里偏差校正因子 $\hat z_0$ 度量复制的中位数偏差，加速因子 $\hat a$ 度量标准误随参数变化的速率（一种偏度），由刀切法复制估计：

$$
\hat z_0=\Phi^{-1}\Bigl(\frac1B\sum_{b=1}^B\boldsymbol{1}\{\hat\theta^{(b)}<\hat\theta\}\Bigr),\qquad
\hat a=\frac{\sum_{i=1}^n(\hat\theta_{(\cdot)}-\hat\theta_{(i)})^3}{6\Bigl(\sum_{i=1}^n(\hat\theta_{(\cdot)}-\hat\theta_{(i)})^2\Bigr)^{3/2}},
$$
其中 $\hat\theta_{(i)}$ 是去掉 $x_i$ 后算出的留一估计，$\hat\theta_{(\cdot)}=\frac1n\sum_{i=1}^n\hat\theta_{(i)}$。

留一估计 $\hat\theta_{(1)},\dots,\hat\theta_{(n)}$ 是刀切法（jackknife）的复制；刀切法是更早的重抽样方法（Quenouille、Tukey），它把统计量重算 $n$ 次，每次删去一个观测。当 $\hat z_0=\hat a=0$ 时 $\alpha_1=\alpha/2$、$\alpha_2=1-\alpha/2$，BCa 区间退化为百分位区间。BCa 区间保留了百分位区间的变换不变性，同时校正偏差与偏度：它的覆盖误差为 $O(n^{-1})$（二阶准确），而正态、基本与百分位区间为 $O(n^{-1/2})$。它是日常使用的推荐方法，也是 `boot.ci` 计算的类型之一；由于 $\alpha_1,\alpha_2$ 可能落在很远的尾部，它需要较大的 $B$（例如 $B\ge1000$）。

| 区间 | 公式 | 适用场合 | 弱点 |
|---|---|---|---|
| 正态 | $\hat\theta\pm z_{\alpha/2}\widehat{\operatorname{se}}$ | $n$ 很大且极限分布明显是正态（样本均值） | 分布不对称或 $\hat\theta$ 有偏时出错 |
| 基本 | $(2\hat\theta-\hat\theta^*_{1-\alpha/2},2\hat\theta-\hat\theta^*_{\alpha/2})$ | 假设 $\hat\theta-\theta$ 的波动可由 $\hat\theta^*-\hat\theta$ 的波动平移模仿，不要求正态 | 分位数位置颠倒，强偏态时朝相反方向过度修正，还可能越出参数空间 |
| 百分位 | $(\hat\theta^*_{\alpha/2},\hat\theta^*_{1-\alpha/2})$ | 数据偏态但估计量基本无偏；变换不变 | 中位数偏差大时自信地出错 |
| BCa | $(\hat\theta^*_{\alpha_1},\hat\theta^*_{\alpha_2})$ | 实践中的默认方法；校正偏差 $\hat z_0$ 与加速 $\hat a$ | 计算量较大（刀切法、大的 $B$） |

![法学院相关系数的自助分布（B = 2000）与四种 95% 区间。分布左偏；正态区间与基本区间越过了相关系数的上界 1，而百分位区间与 BCa 区间遵守这一上界，且 BCa 把区间进一步移向较长的左尾。](./plots/law-correlation-bootstrap.py)

```r
library(boot)
r <- function(x, i) cor(x[i, 1], x[i, 2])
obj <- boot(data = law, statistic = r, R = 2000)
boot.ci(obj, type = c("norm", "basic", "perc", "bca"))

# bootstrap intervals for regression coefficients: cat heart weight on body weight
library(MASS); data(cats)
coefs <- function(d, i) coef(lm(Hwt ~ Bwt, data = d[i, ]))   # resample cases
obj2 <- boot(data = cats, statistic = coefs, R = 2000)
boot.ci(obj2, type = "bca", index = 2)                       # slope
```

### 7.3.4. 自助假设检验

考虑单样本问题：观测到 $\boldsymbol{z}=(z_1,\dots,z_n)$，检验总体均值是否等于给定的 $\mu_0$，即 $H_0\colon\mu=\mu_0$ 对 $H_a\colon\mu\ne\mu_0$（双侧），检验统计量为

$$
T(\boldsymbol{z})=\frac{\bar z-\mu_0}{\widehat{\operatorname{se}}}=\frac{\bar z-\mu_0}{\hat\sigma/\sqrt n}.
$$
**p 值**是在原假设下得到至少与观测值一样极端的值的概率，即 $\mathbb{P}_{H_0}(\lvert T\rvert\ge\lvert T_{\mathrm{obs}}\rvert)$。问题在于如何从观测样本得到 $T$ 在原假设下的分布。有两种方法。

1. 通过置信区间：计算 $\mu$ 的自助区间，若 $\mu_0$ 落在 $100(1-\alpha)\%$ 区间之外，就在水平 $\alpha$ 下拒绝 $H_0$（检验与置信区间的对偶）。例如给 $8$ 名患者服用一种药物并测量病情的变化，若平均变化的 $95\%$ 自助区间覆盖 $0$，就在水平 $0.05$ 下不能认为药物有效。
2. 通过 p 值：平移数据使原假设成立，再从平移后的数据中重抽样。

**算法 7.3.1（单均值的自助检验）**

1. 平移数据：$\tilde z_i=z_i-\bar z+\mu_0$，$i=1,\dots,n$，使 $\tilde{\boldsymbol{z}}$ 的均值为 $\mu_0$。
2. 对 $b=1,\dots,B$，从 $\tilde{\boldsymbol{z}}$ 中抽取自助样本，计算 $\tilde T^{(b)}=\dfrac{\bar{\tilde z}^{(b)}-\mu_0}{\hat{\tilde\sigma}^{(b)}/\sqrt n}$。
3. p 值为 $\#\{b\colon\lvert\tilde T^{(b)}\rvert\ge\lvert T_{\mathrm{obs}}\rvert\}/B$。

统计量必须在每个重抽样本上用它自己的标准差 $\hat{\tilde\sigma}^{(b)}$ 重新计算；对学生化统计量重抽样比只对 $\bar z$ 重抽样更准确。一种常见的改进是报告 $(1+\#\{\cdot\})/(B+1)$，它永远不为零。

**算法 7.3.2（两均值的自助检验）** 观测到来自方差相同的两个总体的 $\boldsymbol{z}=(z_1,\dots,z_n)$ 与 $\boldsymbol{y}=(y_1,\dots,y_m)$，用

$$
T(\boldsymbol{z},\boldsymbol{y})=\frac{\bar z-\bar y}{\hat\sigma\sqrt{n^{-1}+m^{-1}}}
$$
检验 $H_0\colon\mu_z=\mu_y$ 对 $H_a\colon\mu_z\ne\mu_y$，其中 $\hat\sigma$ 是合并标准差。

1. 记合并样本 $\boldsymbol{x}$ 的均值为 $\bar x$，把两个样本都平移到它：$\tilde z_i=z_i-\bar z+\bar x$，$\tilde y_j=y_j-\bar y+\bar x$。
2. 对 $b=1,\dots,B$，从 $\tilde{\boldsymbol{z}}$ 中有放回地抽取 $n$ 个值、从 $\tilde{\boldsymbol{y}}$ 中抽取 $m$ 个值，计算 $\tilde T^{(b)}=\dfrac{\bar{\tilde z}^{(b)}-\bar{\tilde y}^{(b)}}{\hat{\tilde\sigma}^{(b)}\sqrt{n^{-1}+m^{-1}}}$。
3. p 值为 $\#\{b\colon\lvert\tilde T^{(b)}\rvert\ge\lvert T_{\mathrm{obs}}\rvert\}/B$。

**注 7.3.1** 同一问题的置换检验（在非参数统计 [3.6](/3.6) 中展开）把合并样本 $\boldsymbol{x}$ 放在一起，随机把其中 $n$ 个值分给第一组、其余 $m$ 个分给第二组，即无放回地抽取组标签，并重复 $M$ 次。自助检验则从平移后的样本中有放回地抽样。置换检验在"两个分布相等"这一更强的原假设下是精确的；自助检验只近似原假设分布，但针对的是均值相等的假设。

## 7.4. 参数自助法

自助法还有参数的版本。假设数据来自已知的分布族 $P_{\boldsymbol\theta}$，参数 $\boldsymbol\theta$ 未知。对 $P_{\boldsymbol\theta}$ 的最好猜测是 $P_{\hat{\boldsymbol\theta}}$，其中 $\hat{\boldsymbol\theta}$ 是估计值。

**算法 7.4.1（参数自助法）**

1. 由数据 $\boldsymbol{X}$ 估计 $\hat{\boldsymbol\theta}$。
2. 对 $b=1,\dots,B$：从 $P_{\hat{\boldsymbol\theta}}$ 中模拟一个与真实数据容量和"形状"相同的数据集 $\boldsymbol{X}^{*(b)}$，计算 $T^{*(b)}=T(\boldsymbol{X}^{*(b)})$，对模拟数据的处理与真实数据完全相同。
3. 用 $T^{*(1)},\dots,T^{*(B)}$ 的经验分布作为 $T$ 的抽样分布的估计。

**例 7.4.1** 设认为一个容量为 $n$ 的样本来自正态总体。计算 $\bar x$ 与 $s^2$，从 $\mathcal{N}(\bar x,s^2)$ 中生成 $1000$ 个容量为 $n$ 的样本并计算其均值。这 $1000$ 个均值估计了 $\bar X$ 的抽样分布；把它们排序，去掉最小与最大的各 $2.5\%$，就得到总体均值的 $95\%$（百分位）区间。

```r
n <- length(x); B <- 1000
means <- replicate(B, mean(rnorm(n, mean = mean(x), sd = sd(x))))   # simulate from N(xbar, s^2)
quantile(means, c(0.025, 0.975))
```

知道分布族 $P_{\boldsymbol\theta}$ 本身是很强的假设，实际中很少成立，所以最常用的是非参数自助法。参数自助法适用于模型可信、样本很小，以及非参数自助分布离散或退化的情形。

## 小结

自助法实现起来极其简单，但没有现代的计算能力就不可行。它的核心想法是在数据本身上做计算，来估计由同一批数据算出的统计量的变异："数据拽着自己的靴带把自己提起来"。重抽样的想法在 1979 年之前就已存在，但 Bradley Efron 拓宽了它的适用范围，展示了如何在计算机上有效地实现它，并创造了 bootstrap 这个名称。

| 任务 | 自助估计 |
|---|---|
| $\hat\theta$ 的抽样分布 | $\hat\theta^{(1)},\dots,\hat\theta^{(B)}$ 的经验分布；非参数（对数据重抽样，假设数据独立同分布）或参数（从 $P_{\hat\theta}$ 模拟，假设模型成立） |
| 标准误 | $\widehat{\operatorname{se}}=\bigl(\frac1{B-1}\sum_b(\hat\theta^{(b)}-\bar\theta^*)^2\bigr)^{1/2}$，$B=50$–$200$ |
| 偏差 | $\widehat{\operatorname{Bias}}=\bar\theta^*-\hat\theta$ |
| 置信区间 | 正态 $\hat\theta\pm z_{\alpha/2}\widehat{\operatorname{se}}$；基本 $(2\hat\theta-\hat\theta^*_{1-\alpha/2},2\hat\theta-\hat\theta^*_{\alpha/2})$，用 $\hat\theta^*-\hat\theta$ 代替 $\hat\theta-\theta$；百分位 $(\hat\theta^*_{\alpha/2},\hat\theta^*_{1-\alpha/2})$；BCa；$B\ge1000$ |
| 假设检验 | 若 $\theta_0$ 落在区间外则拒绝；或把数据平移到 $H_0$，对检验统计量重抽样得到 p 值 |

对 Hadamard 可微的泛函，自助法有理论保证（泛函 Delta 方法）；对极值以及在边界点处不光滑的估计量，它会失效，此时平滑自助法或 $m$-out-of-$n$ 自助法可能有帮助。在相信一个区间之前，务必先看自助分布。
