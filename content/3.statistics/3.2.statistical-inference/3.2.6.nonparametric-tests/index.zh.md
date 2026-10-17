---
title: 非参数假设检验
description: 不假定总体分布形式的检验——符号检验、Wilcoxon 符号秩检验与秩和检验、Pearson χ² 拟合优度检验、列联表的独立性与齐一性检验，以及 Kolmogorov–Smirnov 检验与 Shapiro–Wilk 正态性检验。
source_hash: 41928860d21a
---

[3.2.5](/3.2.5) 中的检验都假定总体属于形式已知的分布族 $\{f(x;\theta)\colon \theta\in\Theta\}$，检验的是关于有限维参数 $\theta$ 的命题。其临界值来自统计量在该模型（通常是正态模型）下的精确分布；模型不对时，结论可能误导——一个异常值就足以改变 $t$ 检验的结论。本章讨论有效性不依赖于总体分布数学形式的检验，其中反复出现两种思路。第一种用观测值的符号或秩代替观测值本身，它们的零假设分布对一切连续总体都相同，由此得到符号检验和 Wilcoxon 检验（§6.2），即单样本与两样本 $t$ 检验的非参数对应。第二种把观测频数与零假设下的期望频数相比较，依靠大样本理论，特别是**中心极限定理**（[3.1.13](/3.1.13)），由此得到 Pearson $\chi^2$ 拟合优度检验（§6.3）及其在列联表上的应用（§6.4）。§6.5 讨论最常见的拟合优度问题——数据是否服从正态分布，介绍 Kolmogorov–Smirnov 检验、Shapiro–Wilk 检验和正态 QQ 图。非参数统计作为一门学科在 [3.6](/3.6) 中进一步展开。

## 6.1. 参数检验与非参数检验

[3.2.5](/3.2.5) 中的问题都是参数检验。例如：设样本 $\boldsymbol{X}=(X_1,\dots,X_n)$ 来自 $\mathcal{N}(\theta,\sigma^2)$，$\sigma^2$ 已知，检验 $H_0\colon\theta=\theta_0$ 对 $H_1\colon\theta\ne\theta_0$；样本来自 $\mathrm{Ber}(\theta)$，检验 $H_0\colon\theta\le\theta_0$ 对 $H_1\colon\theta>\theta_0$；样本来自 $\mathrm{Poi}(\theta)$，检验 $H_0\colon\theta\ge\theta_0$ 对 $H_1\colon\theta<\theta_0$。

**定义 6.1.1（参数检验与非参数检验）** 若总体的分布函数（或密度）除参数外已知，即属于 $\{f(x;\theta)\colon\theta\in\Theta\}$，$\Theta$ 为有限维，且假设陈述的是 $\theta$ 是否属于 $\Theta$ 的某个给定子集，则称该检验问题为**参数假设检验**。若总体分布的形式基本未知，则称为**非参数假设检验**；此时检验方法不能依赖总体分布的数学表达式。

非参数检验的假设可以涉及中位数等位置参数、两个分布是否相同、两个变量是否独立，或分布本身，例如"样本来自正态分布"。下面五个例子说明本章方法的用途，它们在后面各节中具体分析。

**例 6.1.1（两种安眠药）** $10$ 名受试者分别服用药物 1 和（在另一时间）药物 2，观测值为延长的睡眠小时数。

| 受试者 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| 药物 1（$X_i$） | 1.9 | −1.6 | −0.2 | −1.2 | −0.1 | 3.4 | 3.7 | 0.8 | 0.0 | 2.0 |
| 药物 2（$Y_i$） | 0.7 | 0.8 | 1.1 | 0.1 | −0.1 | 4.4 | 5.5 | 1.6 | 4.6 | 3.4 |
| $Z_i=Y_i-X_i$ | −1.2 | 2.4 | 1.3 | 1.3 | 0.0 | 1.0 | 1.8 | 0.8 | 4.6 | 1.4 |

哪种药物更有效？这是成对数据（成对比较）：$X_1,\dots,X_n$ 相互独立，$Y_1,\dots,Y_n$ 也相互独立，但 $X_i$ 与 $Y_i$ 来自同一受试者，彼此相关，因此不能用两样本 $t$ 检验。我们考虑差值 $Z_i$，它们独立同分布。若差值服从正态分布，可对 $H_0\colon\mathbb{E}Z_i=0$ 用单样本 $t$ 检验；若对其分布所知甚少，则用符号检验或 Wilcoxon 符号秩检验，零假设为"对每个受试者，差值为正与为负的可能性相同"。

**例 6.1.2（小鼠的存活时间）** 16 只小鼠接受手术，其中随机选出的 $7$ 只接受一种新疗法，其余 $9$ 只作为对照。存活天数如下：

| 治疗组（$X_i$） | 16 | 23 | 38 | 94 | 99 | 141 | 197 | | |
|---|---|---|---|---|---|---|---|---|---|
| 对照组（$Y_j$） | 10 | 27 | 31 | 40 | 46 | 50 | 52 | 104 | 146 |

设 $X_1,\dots,X_m\overset{\text{iid}}{\sim}F_X$，$Y_1,\dots,Y_n\overset{\text{iid}}{\sim}F_Y$，两组相互独立，检验新疗法是否改变存活时间。若 $F_X=\mathcal{N}(\mu_1,\sigma^2)$，$F_Y=\mathcal{N}(\mu_2,\sigma^2)$，可用两样本 $t$ 检验；若分布形式未知但 $m,n$ 都很大，可对 $\bar X-\bar Y$ 用正态近似作大样本检验。分布形式未知且样本量小时，用 Wilcoxon 秩和检验（§6.2.4）。

**例 6.1.3（孟德尔的豌豆）** 在孟德尔的杂交试验中，$556$ 粒豌豆按形状和颜色分类：

| 类型 | 圆、黄 | 皱、黄 | 圆、绿 | 皱、绿 |
|---|---|---|---|---|
| 观测数 | 315 | 101 | 108 | 32 |
| 理论比例 | 9 | 3 | 3 | 1 |

豌豆属于第 $i$ 类时记 $X=i$，理论给出 $H_0\colon \mathbb{P}(X=1)=\frac{9}{16}$，$\mathbb{P}(X=2)=\mathbb{P}(X=3)=\frac{3}{16}$，$\mathbb{P}(X=4)=\frac{1}{16}$。数据与这一分布是否相符？这需要拟合优度检验（§6.3）。

**例 6.1.4（吸烟与肺癌）** 100 人按是否吸烟（$X$）与是否患肺癌（$Y$）分类：

| | 肺癌 | 无肺癌 | 合计 |
|---|---|---|---|
| 吸烟 | 39 | 15 | 54 |
| 不吸烟 | 21 | 25 | 46 |
| 合计 | 60 | 40 | 100 |

吸烟者的患癌率为 $72.22\%$，不吸烟者为 $45.65\%$。吸烟与肺癌是否有关？零假设为 $X$ 与 $Y$ 独立；这种计数的二维表称为列联表（§6.4）。

**例 6.1.5（房价）** 正态性是许多分析的基本假定。一个大型房屋成交数据集（Ames 房价数据）中的售价 $Y_i$ 是否服从正态分布？其直方图明显右偏。零假设"存在 $\mu$ 与 $\sigma^2$ 使 $Y_i\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$"是关于整个分布的非参数假设，在 §6.5 中检验。

## 6.2. 符号检验与 Wilcoxon 检验

### 6.2.1. t 检验何时失效

单样本 $t$ 检验 $H_0\colon\mu=\mu_0$ 与两样本 $t$ 检验 $H_0\colon\mu_1-\mu_2=0$ 都是针对正态数据推导的。它们相当稳健，数据不严格正态时通常也表现良好，但并非总是如此：一个极端异常值会使样本方差膨胀，从而抹去原有的证据。

**例 6.2.1** 用（Welch）两样本 $t$ 检验比较两组样本。

| | 样本 1 | 样本 2 | 均值 | 方差 | $t$ | $p$ 值 |
|---|---|---|---|---|---|---|
| (a) | $1,2,\dots,10$ | $7,8,\dots,20$ | 5.5, 13.5 | 9.2, 17.5 | $-5.435$ | $0.000019$ |
| (b) | $1,2,\dots,10$ | $7,8,\dots,20,\ 200$ | 5.5, 25.9 | 9.2, 2335 | $-1.633$ | $0.12$ |

只添加一个值 $200$——它使第二组看起来更大——高度显著的差异反而变得不显著。基于秩的检验不受异常值极端程度的影响：§6.2.4 的 Wilcoxon 秩和检验在情形 (a) 中给出 $p\approx0.0003$，在情形 (b) 中给出 $p\approx0.0002$。

### 6.2.2. 符号检验

设 $Z_1,\dots,Z_n$ 独立同分布（例 6.1.1 中 $Z_i=Y_i-X_i$），定义符号

$$
S_i=\begin{cases}1, & Z_i>0,\\ -1, & Z_i<0,\\ 0, & Z_i=0.\end{cases}
$$
"两种药物效果相同"表述为：对每个受试者，差值为正与为负的可能性相同，即 $\mathbb{P}(S_i=1)=\mathbb{P}(S_i=-1)$。例如当 $Z_i$ 的分布关于 $0$ 对称时这成立；一般地，它表示 $0$ 是 $Z_i$ 的中位数。剔除 $Z_i=0$ 的观测，记正、负差值的个数为 $n_+$、$n_-$，$n_0=n_++n_-$。给定 $n_0$ 时 $n_+\sim\mathrm{Bin}(n_0,\theta)$，其中 $\theta=\mathbb{P}(Z_i>0\mid Z_i\ne0)$，问题化为二项检验

$$
H_0\colon\theta=0.5\quad\longleftrightarrow\quad H_1\colon\theta\ne0.5 .
$$

**定义 6.2.1（符号检验）** 水平为 $\alpha$ 的**符号检验**在 $n_+\ge c$ 或 $n_+\le d$ 时拒绝 $H_0$，其中 $c$ 是满足

$$
\sum_{i=c}^{n_0}\binom{n_0}{i}0.5^{n_0}\le\frac{\alpha}{2},\qquad d=n_0-c
$$
的最小整数。等价地，记 $x_0=\min\{n_+,\,n_0-n_+\}$，精确 $p$ 值为

$$
p=\sum_{i=0}^{x_0}\binom{n_0}{i}0.5^{n_0}+\sum_{i=n_0-x_0}^{n_0}\binom{n_0}{i}0.5^{n_0}
$$
（$n_0$ 为偶数且 $n_+=n_0/2$ 时规定 $p=1$），$p<\alpha$ 时拒绝 $H_0$。

$n_0$ 较大时，对 $H_0$ 下的 $n_+\sim\mathrm{Bin}(n_0,0.5)$ 应用**中心极限定理**，得

$$
U=\frac{n_+-\mathbb{E}n_+}{\sqrt{\operatorname{Var}(n_+)}}=\frac{n_+-0.5n_0}{\sqrt{n_0/4}}=\frac{2n_+-n_0}{\sqrt{n_0}}\xrightarrow[n_0\to\infty]{d}\mathcal{N}(0,1),
$$
于是拒绝域 $\{\lvert U\rvert>z_{\alpha/2}\}$ 的水平近似为 $\alpha$；记 $U$ 的观测值为 $u$，近似 $p$ 值为 $p=\mathbb{P}(\lvert \mathcal{N}(0,1)\rvert>\lvert u\rvert)=2\big(1-\Phi(\lvert u\rvert)\big)$，其中 $\Phi$ 是标准正态分布函数。

**例 6.2.2（药物数据）** 例 6.1.1 中受试者 5 的 $Z_5=0$，故 $n_0=9$，$n_+=8$。精确 $p$ 值是出现 $0,1,8$ 或 $9$ 个正号的概率：

$$
p=\frac{1+9+9+1}{2^9}=0.039<0.05,
$$
因此在水平 $0.05$ 下拒绝 $H_0$。正态近似给出 $u=(16-9)/3=2.33$，$p\approx0.020$。

**例 6.2.3（两种配方）** 某饮料有传统配方 A 和修改配方 B 两个品种。收回的 $10000$ 份意见函中，$5150$ 人认为 A 更好，$4850$ 人认为 B 更好。A 的支持率 $0.515$ 只比 $0.5$ 略大，差异是否显著？这里 $n_+=5150$，$n_0=10000$，样本量很大，

$$
U=\frac{2n_+-n_0}{\sqrt{n_0}}=\frac{10300-10000}{100}=3,\qquad p=\mathbb{P}(\lvert U\rvert>3\mid H_0)\approx0.0027<0.01 .
$$
在水平 $0.01$ 下拒绝"两种配方同样受欢迎"的假设：调查结果表明公众显著偏好传统配方。样本量很大时，比例上的微小差异也可能统计显著。

符号检验也可以检验单个总体的中位数 $m_{0.5}$：对 $Y_i=X_i-m_0$ 应用即可。

**例 6.2.4（维尼纶的纤度）** $100$ 根维尼纶纤维的纤度（粗细）分组如下。

| 纤度 | 1.26 | 1.29 | 1.32 | 1.35 | 1.38 | 1.41 | 1.44 | 1.47 | 1.50 | 1.53 |
|---|---|---|---|---|---|---|---|---|---|---|
| 频数 | 1 | 4 | 7 | 22 | 23 | 25 | 10 | 6 | 1 | 1 |

在 $\alpha=0.05$ 下检验 $H_0\colon m_{0.5}=1.40$ 对 $H_1\colon m_{0.5}\ne1.40$。令 $Y_i=X_i-1.40$，在 $H_0$ 下 $\mathbb{P}(Y_i>0)=\mathbb{P}(Y_i<0)=0.5$；没有 $Y_i$ 等于零，故 $n=n_++n_-=100$，$n_+\sim\mathrm{Bin}(100,\theta)$，检验 $\theta=0.5$。大样本拒绝域为 $\{\lvert 2n_+-n\rvert/\sqrt n>z_{0.025}=1.96\}$。这里 $n_+=25+10+6+1+1=43$，$\lvert 86-100\rvert/10=1.4<1.96$：没有足够证据拒绝 $H_0$。

单侧问题 $H_0\colon\theta\le0.5$ 对 $H_1\colon\theta>0.5$ 同理处理，在 $n_+$ 较大时拒绝。符号检验是检验总体中位数为零的最简单方法，是单样本 $t$ 检验的非参数对应。它的缺点是完全忽略了数值大小，因而效率低（功效低）。许多非参数方法转而用秩（观测值在排序样本中的位置）代替原始值：数据 $3.2, 2.4, 5, 3.8$ 的秩为 $2, 1, 4, 3$。有结（相等值）时取平均秩：数据 $105, 120, 120, 121$ 的秩为 $1, 2.5, 2.5, 4$。

### 6.2.3. Wilcoxon 符号秩检验

符号秩检验保留符号，并加入绝对值的秩。对例 6.1.1 的成对数据：计算 $Z_i=Y_i-X_i$ 及其符号 $S_i$；剔除 $Z_i=0$ 的观测，剩下 $n_0$ 个；记 $R_i$ 为 $\lvert Z_i\rvert$ 在 $\lvert Z_1\rvert,\dots,\lvert Z_{n_0}\rvert$ 中的秩；符号秩为 $S_iR_i$。

**定义 6.2.2（Wilcoxon 符号秩检验）** 检验"$Z_i$ 的分布关于 $0$ 对称"的 **Wilcoxon 符号秩检验**使用正符号秩之和

$$
W^+=\sum_{i=1}^{n_0}R_i\boldsymbol{1}_{\{S_i>0\}}
$$
（等价地用 $W=\sum_{i=1}^{n_0}S_iR_i=2W^+-\frac{n_0(n_0+1)}{2}$），在 $W^+\ge c$ 或 $W^+\le d$ 时拒绝 $H_0$，其中 $d=\frac{n_0(n_0+1)}{2}-c$，$c$ 由附表确定，使第一类错误不超过 $\alpha$。

**定理 6.2.1** 设 $Z_1,\dots,Z_{n_0}$ 独立同分布，分布连续且关于 $0$ 对称，则 $W^+$ 与 $\sum_{k=1}^{n_0}k\,I_k$ 同分布，其中 $I_1,\dots,I_{n_0}\overset{\text{iid}}{\sim}\mathrm{Ber}(1/2)$；特别地，$W^+$ 的分布与 $Z_i$ 的分布无关，且

$$
\mathbb{E}W^+=\frac{n_0(n_0+1)}{4},\qquad \operatorname{Var}(W^+)=\frac{n_0(n_0+1)(2n_0+1)}{24}.
$$

**证明** 对连续对称分布，$\operatorname{sgn}(Z_i)$ 与 $\lvert Z_i\rvert$ 独立，且 $\mathbb{P}(Z_i>0)=1/2$。因此各符号独立同分布，各以概率 $1/2$ 取 $\pm1$，并与绝对值向量独立，从而与秩独立。令 $I_k$ 表示秩为 $k$ 的观测为正，则 $I_1,\dots,I_{n_0}$ 独立同分布于 $\mathrm{Ber}(1/2)$，且 $W^+=\sum_k kI_k$。于是 $\mathbb{E}W^+=\frac12\sum_k k=\frac{n_0(n_0+1)}{4}$，$\operatorname{Var}(W^+)=\frac14\sum_k k^2=\frac{n_0(n_0+1)(2n_0+1)}{24}$。$\square$

$W^+$ 的精确零分布就是 $\{1,\dots,n_0\}$ 的随机子集之和的分布，它关于 $n_0(n_0+1)/4$ 对称。记观测值为 $w^+$，令 $a=\max\{w^+,\ \frac{n_0(n_0+1)}{2}-w^+\}$，精确 $p$ 值为

$$
p=\mathbb{P}\Big(W^+\ge a\ \text{或}\ W^+\le\frac{n_0(n_0+1)}{2}-a\ \Big|\ H_0\Big).
$$
$n_0$ 较大时，在 $H_0$ 下 $U=\big(W^+-\mathbb{E}W^+\big)/\sqrt{\operatorname{Var}(W^+)}\xrightarrow{d}\mathcal{N}(0,1)$；当 $\lvert U\rvert>z_{\alpha/2}$ 时拒绝，记 $u$ 为观测值，近似 $p$ 值为 $\mathbb{P}(\lvert\mathcal{N}(0,1)\rvert>\lvert u\rvert)$。用 $W$ 代替 $W^+$ 得到同一个检验。

**例 6.2.5（药物数据）** 例 6.1.1 中非零差值的绝对值为 $1.2, 2.4, 1.3, 1.3, 1.0, 1.8, 0.8, 4.6, 1.4$，秩为 $3, 8, 4.5, 4.5, 2, 7, 1, 9, 6$；只有第一个差值为负。因此 $W^+=45-3=42$，$W=42-3=39$。$n_0=9$ 时 $\mathbb{E}W^+=22.5$，$\operatorname{Var}(W^+)=71.25$，故 $u=19.5/\sqrt{71.25}=2.31$，近似 $p$ 值为 $0.021$（R 的 `wilcox.test` 对一对结修正了方差，报告 $0.0208$）。在水平 $0.05$ 下拒绝 $H_0$，结论是药物 2 比药物 1 更能延长睡眠。

```r
x <- c(1.9, -1.6, -0.2, -1.2, -0.1, 3.4, 3.7, 0.8, 0.0, 2.0)
y <- c(0.7, 0.8, 1.1, 0.1, -0.1, 4.4, 5.5, 1.6, 4.6, 3.4)
wilcox.test(y - x, correct = FALSE, exact = FALSE)   # V = 42, p-value = 0.02077
wilcox.test(y, x, correct = FALSE, exact = FALSE, paired = TRUE)   # the same test
```

符号秩检验假定差值的分布对称，检验的是对称中心（它既是均值也是中位数）是否为零。三种单样本方法利用数据的程度不同：$t$ 检验利用观测值本身，符号检验只用符号，符号秩检验介于两者之间，同时用符号和秩。

### 6.2.4. Wilcoxon 秩和检验

对例 6.1.2 那样的两个独立样本，进一步假定两分布形状相同，只是位置不同（平移模型）：$X_1,\dots,X_m\overset{\text{iid}}{\sim}F(x)$，$Y_1,\dots,Y_n\overset{\text{iid}}{\sim}F(x-\theta)$，即 $Y$ 与 $X+\theta$ 同分布，均值存在时 $\theta=\mathbb{E}Y-\mathbb{E}X$。由于 $F$ 未知，这是非参数问题。检验

$$
H_0\colon\theta=0\quad\longleftrightarrow\quad H_1\colon\theta\ne0 .
$$
记 $N=m+n$，$R_1,\dots,R_n$ 为 $Y_1,\dots,Y_n$ 在混合样本 $X_1,\dots,X_m,Y_1,\dots,Y_n$ 中的秩。

**定义 6.2.3（Wilcoxon 秩和检验）** **Wilcoxon 秩和检验**（Wilcoxon 1945；与 Mann–Whitney $U$ 检验等价，故也称 Wilcoxon–Mann–Whitney 检验）使用秩和统计量

$$
W=R_1+\cdots+R_n,
$$
在 $W\le c$ 或 $W\ge d$ 时拒绝 $H_0$，$c,d$ 使 $\mathbb{P}(W\le c\ \text{或}\ W\ge d\mid H_0)\le\alpha$。$m,n$ 较小时这些常数有表可查。

**定理 6.2.2** 在 $H_0$ 下且 $F$ 连续时，秩向量在 $\{1,\dots,N\}$ 中两两不同整数构成的 $N(N-1)\cdots(N-n+1)$ 个有序 $n$ 元组上均匀分布：

$$
\mathbb{P}(R_1=r_1,\dots,R_n=r_n)=\frac{1}{N(N-1)\cdots(N-n+1)}.
$$
因而

$$
\mathbb{E}W=\frac{n(N+1)}{2},\qquad \operatorname{Var}(W)=\frac{mn(N+1)}{12}.
$$

**证明** 在 $H_0$ 下 $N$ 个混合观测独立同分布且连续，故出现结的概率为零，$N!$ 种排列等可能，第一个结论成立。于是每个 $R_j$ 在 $\{1,\dots,N\}$ 上均匀分布，$\mathbb{E}R_j=\frac{N+1}{2}$，$\operatorname{Var}(R_j)=\frac{N^2-1}{12}$。由可交换性，任意两个不同秩的协方差相同，而全部 $N$ 个混合观测的秩之和是常数 $N(N+1)/2$，故 $0=N\operatorname{Var}(R_1)+N(N-1)\operatorname{Cov}(R_1,R_2)$，即 $i\ne j$ 时 $\operatorname{Cov}(R_i,R_j)=-\frac{N+1}{12}$。因此

$$
\operatorname{Var}(W)=n\frac{N^2-1}{12}-n(n-1)\frac{N+1}{12}=\frac{n(N+1)(N-n)}{12}=\frac{mn(N+1)}{12}. \qquad\square
$$

在 $H_0$ 下 $W$ 在均值 $n(N+1)/2$ 附近取值；正的平移 $\theta$ 使 $Y$ 偏大，从而 $W$ 偏大。$m,n$ 都较大时，由秩统计量的中心极限定理，在 $H_0$ 下

$$
W^*=\frac{W-n(N+1)/2}{\sqrt{mn(N+1)/12}}\xrightarrow[m,n\to\infty]{d}\mathcal{N}(0,1).
$$
拒绝域 $\{\lvert W^*\rvert>z_{\alpha/2}\}$ 的水平近似为 $\alpha$，记观测值为 $w^*$，近似 $p$ 值为 $\mathbb{P}(\lvert\mathcal{N}(0,1)\rvert>\lvert w^*\rvert)$。单侧问题同理：对 $H_0\colon\theta\le0$ 对 $H_1\colon\theta>0$，$W^*\ge z_\alpha$ 时拒绝；对 $H_0\colon\theta\ge0$ 对 $H_1\colon\theta<0$，$W^*\le -z_\alpha$ 时拒绝。

统计量的 Mann–Whitney 形式为 $W-\frac{n(n+1)}{2}$，即满足 $X_i<Y_j$ 的数对 $(X_i,Y_j)$ 的个数；它取值于 $0$ 到 $mn$，R 报告的 `W` 就是它。

**例 6.2.6（小鼠数据）** 例 6.1.2 中对照组 $n=9$，治疗组 $m=7$，$N=16$。在混合排序中，对照组存活时间的秩为 $1, 4, 5, 7, 8, 9, 10, 13, 15$，故 $W=72$（R 报告 $72-\frac{9\cdot10}{2}=27$）。在 $H_0$ 下 $\mathbb{E}W=76.5$。由精确零分布，水平 $0.05$ 的临界值为 $c=57$、$d=96$（$\mathbb{P}(W\le57)=\mathbb{P}(W\ge96)\approx0.021$）。由于 $57<72<96$，数据没有提供拒绝 $H_0$ 的足够证据；精确 $p$ 值为 $0.68$。

```r
x <- c(16, 23, 38, 94, 99, 141, 197)
y <- c(10, 27, 31, 40, 46, 50, 52, 104, 146)
wilcox.test(y, x)                  # W = 27, p-value = 0.6806 (exact)
wilcox.test(y, x, exact = FALSE)   # W = 27, p-value = 0.672 (normal approximation, continuity correction)
```

默认情况下，两组样本都少于 $50$ 个值且没有结时，R 计算精确 $p$ 值，否则使用正态近似。

总之，符号秩检验是单样本（或成对）$t$ 检验的替代，秩和检验是两样本 $t$ 检验的替代。当认为参数假定不成立时，秩检验很有吸引力。其缺点是，由于基于秩，它们对效应大小说明很少；当需要的只是一个 $p$ 值时，它们最为合用。

## 6.3. 拟合优度检验

### 6.3.1. 一般问题

设 $\boldsymbol{X}=(X_1,\dots,X_n)$ 是来自总体 $X$ 的样本，$F$ 是一个给定的分布函数（理论分布）。我们要检验

$$
H_0\colon X\sim F .
$$
在例 6.1.3 中，$F$ 是 $\{1,2,3,4\}$ 上概率为 $\frac{9}{16},\frac{3}{16},\frac{3}{16},\frac{1}{16}$ 的分布；又如对给定的 $\mu,\sigma^2$ 检验 $H_0\colon X\sim\mathcal{N}(\mu,\sigma^2)$。理论分布可以完全已知（如孟德尔试验），也可以含未知参数（如"存在 $\mu$ 与 $\sigma^2$ 使 $X_i\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$"）。

直观上，定义一个衡量数据与 $F$ 之间差异的统计量 $D=D(X_1,\dots,X_n;F)$，在 $D\ge c$ 时拒绝 $H_0$。实际上 $X$ 大概既不严格服从 $F$，也未必远离 $F$；与其只回答是或否，不如给出 $[0,1]$ 中的一个数，衡量数据与 $F$ 的吻合程度。

**定义 6.3.1（拟合优度）** 记差异统计量 $D$ 的观测值为 $d_0$。称

$$
p(d_0)=\mathbb{P}(D\ge d_0\mid H_0)
$$
为数据对 $F$ 的**拟合优度**。水平为 $\alpha$ 的**拟合优度检验**在 $p(d_0)<\alpha$ 时拒绝 $H_0$，在 $p(d_0)\ge\alpha$ 时接受 $H_0$。

拟合优度就是基于 $D$ 的检验的 $p$ 值。$D$ 的经典选择有 Pearson $\chi^2$ 统计量（K. Pearson，1900）和 Kolmogorov 统计量（A. N. Kolmogorov，1933；§6.5.1）。

### 6.3.2. Pearson χ² 检验

设理论分布是离散的，

$$
F\colon\ \mathbb{P}(X=a_i)=p_i,\quad i=1,\dots,r,\qquad p_i\ge0,\ \sum_{i=1}^r p_i=1,
$$
其中 $p_i$ 已知，检验 $H_0\colon\mathbb{P}(X=a_i)=p_i$，$i=1,\dots,r$。记 $v_i$ 为 $a_i$ 在样本中出现的频数，$\sum_i v_i=n$。在 $H_0$ 下，由**大数定律**，频率 $v_i/n$ 收敛到 $p_i$，因此自然的差异度量是加权平方和 $\sum_i c_i(v_i/n-p_i)^2$。Pearson 取 $c_i=n/p_i$：

$$
K_n=\sum_{i=1}^{r}\frac{(v_i-np_i)^2}{np_i}=\sum_{i=1}^r\frac{(\text{观测频数}-\text{期望频数})^2}{\text{期望频数}} .
$$

**定理 6.3.1（Pearson）** 在 $H_0$ 下，当 $n\to\infty$ 时 $K_n\xrightarrow{d}\chi^2_{r-1}$。

**证明**（$r=2$ 的情形）在 $H_0$ 下 $(v_1,\dots,v_r)\sim\mathrm{Mult}(n,\boldsymbol{p})$。当 $r=2$ 时，$v_1\sim\mathrm{Bin}(n,p_1)$，$v_2=n-v_1$，$p_2=1-p_1$，故 $v_2-np_2=-(v_1-np_1)$，

$$
K_n=\frac{(v_1-np_1)^2}{np_1}+\frac{(v_1-np_1)^2}{np_2}=\Big(\frac{v_1-np_1}{\sqrt{np_1p_2}}\Big)^2 .
$$
由**中心极限定理**，$(v_1-np_1)/\sqrt{np_1p_2}\xrightarrow{d}\mathcal{N}(0,1)$，再由连续映射定理得 $K_n\xrightarrow{d}\chi^2_1$。$\square$

$r>2$ 时用多元中心极限定理（或**特征函数**方法）证明：$\big((v_i-np_i)/\sqrt{np_i}\big)_{i=1}^r$ 收敛到一个正态向量，其协方差矩阵是秩为 $r-1$ 的投影矩阵 $I_r-\sqrt{\boldsymbol{p}}\sqrt{\boldsymbol{p}}^{\mathsf T}$，这样的向量的长度平方服从 $\chi^2_{r-1}$。自由度少一个，是因为频数满足约束 $\sum_i v_i=n$。

检验在 $K_n>\chi^2_{r-1,\alpha}$ 时拒绝 $H_0$；记 $K_n$ 的观测值为 $k_0$，拟合优度为 $p(k_0)=\mathbb{P}(K_n\ge k_0\mid H_0)\approx\mathbb{P}(\chi^2_{r-1}\ge k_0)$。

**例 6.3.1（孟德尔的豌豆）** 例 6.1.3 中 $v_1=315$，$v_2=101$，$v_3=108$，$v_4=32$，$n=556$，

$$
k_0=\frac{(315-556\cdot\frac{9}{16})^2}{556\cdot\frac{9}{16}}+\frac{(101-556\cdot\frac{3}{16})^2}{556\cdot\frac{3}{16}}+\frac{(108-556\cdot\frac{3}{16})^2}{556\cdot\frac{3}{16}}+\frac{(32-556\cdot\frac{1}{16})^2}{556\cdot\frac{1}{16}}=0.470 .
$$
自由度 $r-1=3$，$p(k_0)\approx\mathbb{P}(\chi^2_3\ge0.470)=0.925$：数据与孟德尔的理论吻合得很好。

```r
chisq.test(c(315, 101, 108, 32), p = c(9, 3, 3, 1) / 16)   # X-squared = 0.47002, df = 3, p-value = 0.9254
```

若 $F$ 是 $\mathbb{R}$ 上的连续分布，就把数据分组。取常数 $-\infty=a_0<a_1<\cdots<a_{r-1}<a_r=+\infty$，把直线分成区间

$$
I_1=(-\infty,a_1],\quad I_2=(a_1,a_2],\quad\dots,\quad I_r=(a_{r-1},+\infty),
$$
计算 $H_0$ 下的概率 $p_j=\mathbb{P}_F(X\in I_j)=F(a_j)-F(a_{j-1})$，检验 $H_0\colon\mathbb{P}(X\in I_j)=p_j$，$j=1,\dots,r$，其中 $v_j$ 为落入 $I_j$ 的观测个数。由定理 6.3.1，在 $H_0$ 下 $K_n=\sum_j(v_j-np_j)^2/(np_j)\xrightarrow{d}\chi^2_{r-1}$。

**注 6.3.1** (1) 近似要求期望频数较大：通常每个期望频数 $np_j$（最好每个观测频数也）不少于 $5$，否则合并相邻区间。(2) 分点 $a_1,\dots,a_{r-1}$ 不能依赖于样本，不能看了数据落在哪里之后再选。(3) 分组会损失信息，结果也依赖于所选的划分。

### 6.3.3. 含未知参数的理论分布

$H_0$ 往往只指定一个参数分布族：$H_0\colon X\sim F(x;\boldsymbol{\theta})$，$\boldsymbol{\theta}=(\theta_1,\dots,\theta_s)$ 未知。Pearson（1900）提出先估计 $\boldsymbol{\theta}$，再用估计出的概率 $\hat p_j=p_j(\hat{\boldsymbol{\theta}})$，并认为定理 6.3.1 仍然成立。Fisher 指出，每估计一个参数，自由度就要减少一个。

**定理 6.3.2（Fisher）** 若 $\hat{\boldsymbol{\theta}}$ 是基于分组频数 $v_1,\dots,v_r$ 的 $s$ 个参数的极大似然估计（更一般地，似然方程的任一相合根），且正则条件成立，则在 $H_0$ 下

$$
K_n=\sum_{j=1}^r\frac{(v_j-n\hat p_j)^2}{n\hat p_j}\xrightarrow{d}\chi^2_{r-1-s}.
$$

**例 6.3.2（混凝土的抗压强度）** $200$ 件混凝土制件的抗压强度（单位 $\mathrm{kg/cm^2}$）分组如下。抗压强度是否服从正态分布（$\alpha=0.05$）？

| 区间 | 190–200 | 200–210 | 210–220 | 220–230 | 230–240 | 240–250 |
|---|---|---|---|---|---|---|
| 频数 | 10 | 26 | 56 | 64 | 30 | 14 |

检验 $H_0$：存在 $\mu,\sigma^2$ 使 $X\sim\mathcal{N}(\mu,\sigma^2)$。用组中值计算，极大似然估计为

$$
\hat\mu=\bar x=\tfrac{1}{200}(195\cdot10+205\cdot26+\cdots+245\cdot14)=221,\qquad \hat\sigma^2=\tfrac{1}{200}\sum_{i=1}^{200}(x_i-\bar x)^2=12.33^2,
$$
问题化为检验 $H_0\colon X\sim\mathcal{N}(221,12.33^2)$。令 $u_j=(a_j-221)/12.33$，各组概率为 $\hat p_j=\Phi(u_j)-\Phi(u_{j-1})$，两端的组延伸到 $\pm\infty$：

| $j$ | 区间 | $v_j$ | $\hat p_j$ | $n\hat p_j$ | $(v_j-n\hat p_j)^2/(n\hat p_j)$ |
|---|---|---|---|---|---|
| 1 | $(-\infty,200]$ | 10 | 0.044 | 8.9 | 0.149 |
| 2 | $(200,210]$ | 26 | 0.142 | 28.4 | 0.199 |
| 3 | $(210,220]$ | 56 | 0.282 | 56.3 | 0.002 |
| 4 | $(220,230]$ | 64 | 0.300 | 59.9 | 0.277 |
| 5 | $(230,240]$ | 30 | 0.171 | 34.2 | 0.518 |
| 6 | $(240,+\infty)$ | 14 | 0.062 | 12.3 | 0.226 |

于是 $K_n=1.37$。估计了两个参数，自由度为 $6-1-2=3$，拟合优度为 $p\approx\mathbb{P}(\chi^2_3>1.37)=0.71>\alpha$，没有足够证据拒绝正态性。（严格地说，定理 6.3.2 要求由分组数据求估计；这里用组中值求估计是常用且相当接近的近似。）

## 6.4. 列联表的独立性与齐一性检验

### 6.4.1. 独立性检验

在例 6.1.4 中，令 $X=1$（吸烟）或 $2$（不吸烟），$Y=1$（肺癌）或 $2$（无肺癌）。一般地，设 $X$ 取值 $1,\dots,r$，$Y$ 取值 $1,\dots,s$，$p_{ij}=\mathbb{P}(X=i,Y=j)$，$\sum_i\sum_j p_{ij}=1$，边缘概率 $p_{i\cdot}=\sum_j p_{ij}$，$p_{\cdot j}=\sum_i p_{ij}$。容量为 $n$ 的样本交叉分类后得到 $r\times s$ 的频数表 $n_{ij}$，即列联表（contingency table），行和为 $n_{i\cdot}$，列和为 $n_{\cdot j}$：

| $X\backslash Y$ | $1$ | $\cdots$ | $j$ | $\cdots$ | $s$ | $\Sigma$ |
|---|---|---|---|---|---|---|
| $1$ | $n_{11}$ | $\cdots$ | $n_{1j}$ | $\cdots$ | $n_{1s}$ | $n_{1\cdot}$ |
| $\vdots$ | $\vdots$ | | $\vdots$ | | $\vdots$ | $\vdots$ |
| $r$ | $n_{r1}$ | $\cdots$ | $n_{rj}$ | $\cdots$ | $n_{rs}$ | $n_{r\cdot}$ |
| $\Sigma$ | $n_{\cdot1}$ | $\cdots$ | $n_{\cdot j}$ | $\cdots$ | $n_{\cdot s}$ | $n$ |

独立性检验（test of independence）检验

$$
H_0\colon p_{ij}=p_{i\cdot}\,p_{\cdot j},\qquad i=1,\dots,r,\ j=1,\dots,s,
$$
这是 $rs$ 个格子的多项分布的拟合优度问题，未知参数为 $p_{1\cdot},\dots,p_{r\cdot}$ 与 $p_{\cdot1},\dots,p_{\cdot s}$（满足 $\sum_ip_{i\cdot}=\sum_jp_{\cdot j}=1$）。在 $H_0$ 下似然函数为

$$
L=c\prod_{i=1}^r\prod_{j=1}^s(p_{i\cdot}p_{\cdot j})^{n_{ij}}=c\Big(\prod_{i=1}^r p_{i\cdot}^{n_{i\cdot}}\Big)\Big(\prod_{j=1}^s p_{\cdot j}^{n_{\cdot j}}\Big),\qquad c=\frac{n!}{\prod_i\prod_j n_{ij}!},
$$
它分解为两个多项似然的乘积，故极大似然估计为

$$
\hat p_{i\cdot}=\frac{n_{i\cdot}}{n},\qquad \hat p_{\cdot j}=\frac{n_{\cdot j}}{n}.
$$
格子 $(i,j)$ 的估计期望频数为 $n\hat p_{i\cdot}\hat p_{\cdot j}=n_{i\cdot}n_{\cdot j}/n$，Pearson 统计量为

$$
K_n=\sum_{i=1}^r\sum_{j=1}^s\frac{\big(n_{ij}-n_{i\cdot}n_{\cdot j}/n\big)^2}{n_{i\cdot}n_{\cdot j}/n}=n\Big(\sum_{i=1}^r\sum_{j=1}^s\frac{n_{ij}^2}{n_{i\cdot}n_{\cdot j}}-1\Big).
$$

**定理 6.4.1** 在 $H_0$ 下，当 $n\to\infty$ 时

$$
K_n\xrightarrow{d}\chi^2_{rs-1-(r+s-2)}=\chi^2_{(r-1)(s-1)} .
$$

这正是定理 6.3.2：共 $rs$ 个格子，估计了 $(r-1)+(s-1)$ 个参数。检验在 $K_n>\chi^2_{(r-1)(s-1),\alpha}$ 时拒绝 $H_0$，等价地在 $p(k_0)\approx\mathbb{P}(\chi^2_{(r-1)(s-1)}\ge k_0)<\alpha$ 时拒绝。

**例 6.4.1（吸烟与肺癌）** 对例 6.1.4 的 $2\times2$ 表，$K_n=7.307$，自由度为 $1$，$p=0.0069$。吸烟与肺癌显著相关。

```r
chisq.test(matrix(c(39, 21, 15, 25), ncol = 2), correct = FALSE)   # X-squared = 7.3068, df = 1, p-value = 0.00687
```

**例 6.4.2（年龄与电视节目）** 观众按喜爱的节目（$X$）与年龄段（$Y$）分类：

| $X\backslash Y$ | 老年 | 中年 | 青年 |
|---|---|---|---|
| 戏曲 | 20 | 10 | 2 |
| 歌舞 | 5 | 20 | 35 |
| 球赛 | 2 | 10 | 20 |

对这个 $3\times3$ 表，$K_n=47.82$，自由度为 $(3-1)(3-1)=4$，$p\approx1.0\times10^{-9}$：节目偏好强烈依赖于年龄。

### 6.4.2. 齐一性检验

现在考虑 $r$ 个总体 $X^{(1)},\dots,X^{(r)}$，每个都按同样的 $s$ 个类别 $a_1,\dots,a_s$ 分类，从第 $i$ 个总体抽取预先确定容量 $n_{i\cdot}$ 的样本，$n_{ij}$ 为第 $i$ 个总体落入类别 $a_j$ 的观测个数。表的形式与前面相同，但行和 $n_{i\cdot}$ 由设计固定，不是随机的。记 $p_i(j)=\mathbb{P}(X^{(i)}=a_j)$，齐一性检验（test of homogeneity）检验各总体是否同分布：

$$
H_0\colon p_1(j)=p_2(j)=\cdots=p_r(j),\qquad j=1,\dots,s .
$$

若公共分布完全已知，即 $H_0\colon p_i(j)=p_j^0$，$p_j^0$ 已知且 $\sum_jp_j^0=1$，则用

$$
K_n=\sum_{i=1}^r\sum_{j=1}^s\frac{(n_{ij}-n_{i\cdot}p_j^0)^2}{n_{i\cdot}p_j^0}\xrightarrow{d}\chi^2_{r(s-1)}\qquad(n_{i\cdot}\to\infty,\ i=1,\dots,r):
$$
$r$ 个内层和是相互独立的 Pearson 统计量，由定理 6.3.1 各有 $s-1$ 个自由度。

若公共分布 $p_j=p_i(j)$ 未知，用 $\hat p_j=n_{\cdot j}/n$ 估计其 $s-1$ 个自由参数，统计量与独立性检验相同：

$$
K_n=n\Big(\sum_{i=1}^r\sum_{j=1}^s\frac{n_{ij}^2}{n_{i\cdot}n_{\cdot j}}-1\Big)\xrightarrow{d}\chi^2_{(r-1)(s-1)}\qquad(n_{i\cdot}\to\infty,\ i=1,\dots,r),
$$
自由度为 $r(s-1)-(s-1)=(r-1)(s-1)$。$K_n>\chi^2_{(r-1)(s-1),\alpha}$ 时拒绝 $H_0$。因此独立性与齐一性用同样的计算来检验，区别在于抽样设计与解释。

**例 6.4.3（三个班次）** 某工厂分三班生产，产品分为 $1,\dots,6$ 共 6 个等级。为检验三个班的产品质量是否相同，从甲、乙、丙三班分别抽取 $83$、$95$、$83$ 个产品检查：

| | 1 | 2 | 3 | 4 | 5 | 6 | $\Sigma$ |
|---|---|---|---|---|---|---|---|
| 甲 | 11 | 23 | 8 | 5 | 18 | 18 | 83 |
| 乙 | 17 | 29 | 10 | 17 | 7 | 15 | 95 |
| 丙 | 6 | 21 | 8 | 24 | 15 | 9 | 83 |
| $\Sigma$ | 34 | 73 | 26 | 46 | 40 | 42 | 261 |

在 $\alpha=0.01$ 下检验 $H_0$：三个班的质量分布相同。这里 $r=3$，$s=6$，$(r-1)(s-1)=10$，$\chi^2_{10,0.01}=23.21$。统计量 $K_n=26.27>23.21$，故拒绝 $H_0$；$p(k_0)=\mathbb{P}(\chi^2_{10}\ge26.27)=0.0034<0.01$。

## 6.5. 正态性检验

检验正态性假定（例 6.1.5）是理论分布含未知参数 $\mu,\sigma^2$ 的拟合优度问题：$H_0$：存在 $\mu,\sigma^2$ 使 $X_i\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$。估计参数后的 Pearson 检验（例 6.3.2）是一种方法；本节介绍不需要分组的检验。

### 6.5.1. Kolmogorov–Smirnov 检验

设 $\boldsymbol{X}=(X_1,\dots,X_n)$ 来自未知分布函数 $F$，$F_0$ 是已知的连续分布函数，例如 $\mathcal{N}(0,1)$ 的分布函数。检验

$$
H_0\colon F(x)=F_0(x)\quad\text{对一切 }x\in\mathbb{R}.
$$
经验分布函数 $F_n(x)=\frac1n\#\{i\colon X_i\le x\}$（[3.2.1](/3.2.1)）是 $F$ 的良好估计。

**定义 6.5.1（Kolmogorov–Smirnov 检验）** **Kolmogorov–Smirnov 检验**使用统计量

$$
D_n=\sup_{-\infty<x<+\infty}\lvert F_n(x)-F_0(x)\rvert,
$$
在 $D_n>c$ 时拒绝 $H_0$。记 $D_n$ 的观测值为 $d_0$，拟合优度为 $p(d_0)=\mathbb{P}(D_n\ge d_0\mid H_0)$，$p(d_0)<\alpha$ 时拒绝 $H_0$。

在 $H_0$ 下，由 Glivenko–Cantelli 定理（定理 1.5.2），$D_n\xrightarrow{\text{a.s.}}0$；而在备择 $F\ne F_0$ 下，$D_n$ 收敛到 $\sup_x\lvert F(x)-F_0(x)\rvert>0$。因此 $D_n$ 较大是反对 $H_0$ 的证据。由于 $D_n$ 只在次序统计量处变化，计算时用 $D_n=\max_{1\le i\le n}\max\big\{\frac in-F_0(X_{(i)}),\ F_0(X_{(i)})-\frac{i-1}{n}\big\}$。

![Kolmogorov–Smirnov 统计量是样本经验分布函数与假设分布函数之间最大的竖直距离。](./plots/ks-statistic.py)

**定理 6.5.1** 设 $F_0$ 连续，则在 $H_0$ 下：

1. $D_n$ 的分布与 $F_0$ 无关；
2. （Kolmogorov，1933）对每个 $t>0$，

$$
\lim_{n\to\infty}\mathbb{P}\big(\sqrt n\,D_n\le t\big)=1-2\sum_{k=1}^\infty(-1)^{k-1}\mathrm{e}^{-2k^2t^2}.
$$

第 1 条来自概率积分变换：在 $H_0$ 下 $U_i=F_0(X_i)$ 独立同分布于 $\mathrm{U}(0,1)$，而 $D_n$ 等于 $U_1,\dots,U_n$ 相对于均匀分布的 Kolmogorov–Smirnov 统计量。因此该检验是精确地与分布无关的，临界值对一切连续 $F_0$ 只需造一张表；$n$ 较大时，水平 $0.05$ 的渐近临界值为 $1.358/\sqrt n$。

对一维连续的 $F_0$，Kolmogorov–Smirnov 检验一般优于 Pearson $\chi^2$ 检验：它使用未分组的数据，对小样本也是精确的。其弱点是难以处理含未知参数的理论分布：若用同一数据估计 $\mu,\sigma^2$，$D_n$ 的零分布会改变（临界值变小），上述表格不再适用。（Lilliefors 检验给出了正态族的修正临界值。）

**例 6.5.1（房价）** 对例 6.1.5 的房价检验 $H_0\colon Y_i\sim\mathcal{N}(180000,80000^2)$，得 $D=0.122$，$p<2.2\times10^{-16}$：这一正态分布被坚决拒绝。作为对照，对 $100$ 个模拟的标准正态值检验 $\mathcal{N}(0,1)$，得 $D=0.109$，$p=0.18$。

```r
ks.test(SalePrice, "pnorm", 180000, 80000)   # D = 0.12177, p-value < 2.2e-16
ks.test(rnorm(100), "pnorm")                 # e.g. D = 0.10913, p-value = 0.1846
```

### 6.5.2. Shapiro–Wilk 检验

Shapiro–Wilk 检验专门针对 $\mu,\sigma^2$ 未知的正态性复合假设。若 $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$，次序统计量为 $X_{(1)}\le\cdots\le X_{(n)}$，则 $Y_i=(X_i-\mu)/\sigma$ 独立同分布于 $\mathcal{N}(0,1)$，且 $Y_{(i)}=(X_{(i)}-\mu)/\sigma$。令

$$
m_i=\mathbb{E}Y_{(i)},\qquad e_i=X_{(i)}-\mathbb{E}X_{(i)},\qquad i=1,\dots,n .
$$
$m_i$ 与 $\mu,\sigma^2$ 无关，且

$$
X_{(i)}=\mu+\sigma m_i+e_i,\qquad i=1,\dots,n,
$$
其中 $(e_1,\dots,e_n)$ 均值为 $0$，协方差矩阵为 $\sigma^2V$，$V$ 是 $(Y_{(1)},\dots,Y_{(n)})$ 的（已知的）协方差矩阵。因此在 $H_0$ 下，点 $(m_1,X_{(1)}),\dots,(m_n,X_{(n)})$ 接近一条截距为 $\mu$、斜率为 $\sigma$ 的直线。它们的相关系数平方

$$
R^2=\frac{\Big(\sum_{i=1}^n(X_{(i)}-\bar X)(m_i-\bar m)\Big)^2}{\sum_{i=1}^n(X_{(i)}-\bar X)^2\sum_{i=1}^n(m_i-\bar m)^2}
$$
在 $H_0$ 下接近 $1$，$R^2<c$ 时拒绝正态性。Shapiro 与 Wilk 用考虑了次序统计量之间相关性的广义最小二乘权重代替 $\boldsymbol{m}$：

**定义 6.5.2（Shapiro–Wilk 检验）** 正态性的 **Shapiro–Wilk 检验**使用统计量

$$
W=\frac{\Big(\sum_{i=1}^{\lfloor n/2\rfloor}a_i\big(X_{(n+1-i)}-X_{(i)}\big)\Big)^2}{\sum_{i=1}^n(X_{(i)}-\bar X)^2},
$$
其中 $a_i=c_{n+1-i}$，$(c_1,\dots,c_n)=\boldsymbol{m}^{\mathsf T}V^{-1}/\lVert V^{-1}\boldsymbol{m}\rVert$（这是反对称向量，$c_{n+1-i}=-c_i$，故分子等于 $\big(\sum_{i=1}^nc_iX_{(i)}\big)^2$），$W$ 较小（$W\le c$，临界值查表或数值计算）时拒绝正态性。

统计量满足 $0<W\le1$，且对位置与尺度变换不变，因此其零分布与 $\mu,\sigma^2$ 无关。Shapiro–Wilk 检验专门针对正态性，对非正态备择的功效一般高于 Kolmogorov–Smirnov 检验和 Pearson $\chi^2$ 检验。

**例 6.5.2（房价）** 对房价，`shapiro.test(SalePrice)` 给出 $W=0.887$，$p<2.2\times10^{-16}$，拒绝正态性；对容量为 $100$ 的模拟正态样本，得 $W=0.982$，$p=0.197$。

### 6.5.3. 正态 QQ 图

图形检查是正式检验的补充。正态 QQ 图（normal Q–Q plot）把排序后的样本 $x_{(1)}\le\cdots\le x_{(n)}$ 对标准正态分位数 $\Phi^{-1}\big(\frac{i-0.5}{n}\big)$（$i=1,\dots,n$）作图（R 中的 `qqnorm`）。由于 $\Phi^{-1}\big(\frac{i-0.5}{n}\big)$ 近似于 $m_i=\mathbb{E}Y_{(i)}$，在正态性下这些点接近一条斜率为 $\sigma$、截距为 $\mu$ 的直线，这也正是 §6.5.2 中 $R^2$ 的想法。典型的偏离很容易辨认：异常值是远离直线的单个点；右偏分布给出一条凸曲线，两端都在直线上方（如房价数据）；厚尾使下端低于直线、上端高于直线（S 形）。

![容量为 50 的样本的正态 QQ 图：分别来自正态分布、带一个异常值的正态分布、右偏分布和厚尾分布；直线通过上下四分位点。](./plots/qq-patterns.py)

## 小结 {#summary}

| 检验 | 数据 | 零假设 | 假定 | 统计量与零分布 |
|---|---|---|---|---|
| 符号检验 | 单样本或成对差值 | 中位数 $=0$ | 连续（或剔除零值） | $n_+\sim\mathrm{Bin}(n_0,0.5)$ |
| Wilcoxon 符号秩检验 | 单样本或成对差值 | 对称中心 $=0$ | 分布对称 | $W^+$，均值 $\frac{n_0(n_0+1)}{4}$，方差 $\frac{n_0(n_0+1)(2n_0+1)}{24}$ |
| Wilcoxon 秩和检验 | 两个独立样本 | 无位置平移 | 形状相同（平移模型） | $W$，均值 $\frac{n(N+1)}{2}$，方差 $\frac{mn(N+1)}{12}$ |
| Pearson $\chi^2$ 拟合优度 | $r$ 类的频数 | 给定分布（估计 $s$ 个参数） | 频数较大（$np_j\ge5$） | $K_n\approx\chi^2_{r-1-s}$ |
| 列联表 $\chi^2$ | $r\times s$ 表 | 独立性或齐一性 | 频数较大 | $K_n\approx\chi^2_{(r-1)(s-1)}$ |
| Kolmogorov–Smirnov | 连续数据 | $F=F_0$，完全给定 | $F_0$ 连续 | $D_n$，与分布无关 |
| Shapiro–Wilk | 连续数据 | 正态性，$\mu,\sigma^2$ 未知 | — | $W$，值小时拒绝 |

何时使用非参数方法？在参数假定（如正态性）正确时，参数检验更有效、功效更高，但往往不像想象中那样高出很多：在正态性下，Wilcoxon 检验相对于 $t$ 检验的渐近相对效率为 $3/\pi\approx0.955$（符号检验为 $2/\pi\approx0.637$）。对连续的平移模型，Wilcoxon 检验相对于 $t$ 检验的效率从不低于 $0.864$；若正态性严重不成立（厚尾、异常值），它们的功效可以高得多。因此非参数检验适用范围广、稳健，大样本理论在其中起核心作用；而当所依据的模型正确时，参数检验的功效更高。
