---
title: 单因子实验：多重比较
description: 方差分析 F 检验显著之后怎么办；多重性问题、族错误率与错误发现率；Fisher 最小显著差数、Benjamini–Hochberg 方法、Bonferroni 校正、Tukey HSD 与 Tukey–Kramer 方法、对全部对照的 Scheffé 方法，以及与对照比较的 Dunnett 方法；它们的临界值、功效与软件输出。
source_hash: e05e86799160
---

[3.8.3](/3.8.3) 的方差分析 $F$ 检验回答了关于单因子实验的第一个问题：各处理均值是否全部相等？对等离子体刻蚀实验，回答是明确的否定（$F_0 = 66.8$，$p = 2.9\times10^{-9}$）。第二个问题是哪些均值有差异，差异多大。回答它需要在同一批数据上作许多比较，而每个比较都是又一次出现假阳性的机会；本章讨论如何控制这种风险，同时又不过分牺牲功效。我们先通过两种错误率，即**族错误率**与**错误发现率**，把多重性问题说精确，然后逐一研究各种标准方法：Fisher 最小显著差数、Benjamini–Hochberg、Bonferroni、Tukey、Scheffé 与 Dunnett，最后比较它们的临界值，并决定何时用哪一种。回归课程简要地接触过其中的几种方法（[3.3.13](/3.3.13)），多元分析课程接触过错误发现率（[3.4.12](/3.4.12)）；这里把它们放在一起展开，讲清统计量、各自控制的错误率以及报告它的软件输出。

本章始终使用单因子模型 $Y_{ij} = \mu_i + \varepsilon_{ij}$，$\varepsilon_{ij} \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2)$，$i = 1, \dots, a$，$j = 1, \dots, n_i$，$N = \sum_in_i$，自由度为 $N - a$ 的 $\mathrm{MS}_{\mathrm{E}}$ 是 $\sigma^2$ 的估计。对刻蚀数据，$a = 4$，$n = 5$，功率 $160$、$180$、$200$、$220\,\mathrm{W}$ 的水平均值为 $551.2$、$587.4$、$625.4$、$707.0$，$\mathrm{MS}_{\mathrm{E}} = 333.7$，自由度 $16$。

## 4.1. 多重比较问题

拒绝 $H_0\colon \mu_1 = \cdots = \mu_a$ 之后，自然的后续步骤是对每一对水平检验

$$
H_0\colon \mu_i = \mu_j \quad\text{对}\quad H_1\colon \mu_i \ne \mu_j,\qquad 1 \le i < j \le a,
$$
这是 $m = \binom a2$ 个检验；对刻蚀实验，$m = \binom42 = 6$。更一般地，多重比较（multiple comparisons）是对同一批数据所作的关于若干处理均值比较（成对比较、对照、与对照组的比较）的推断，而多重比较方法是按比较的个数调整这些推断的方法。

如果 $m$ 个检验中的每一个都在水平 $\alpha$ 下进行，则至少一次错误拒绝的概率随 $m$ 迅速增大。对 $m$ 个独立的、原假设都为真的检验，

$$
\mathbb{P}(\text{至少一次假阳性}) = 1 - \mathbb{P}(\text{无拒绝}) = 1 - (1 - \alpha)^m,
$$
当 $\alpha = 0.05$ 时，$m = 6$ 给出 $0.26$，$m = 20$ 给出 $0.64$：在二十个原假设为真的检验中，我们应当预期会发现"某些显著的东西"。方差分析中的各成对检验并不独立，因为它们共用均值与 $\mathrm{MS}_{\mathrm{E}}$，但膨胀的性质是一样的（4.3 节精确地算出了它）。

![m 个独立检验在水平 0.05 下至少出现一次假阳性的概率 1 - 0.95^m 对 m 的曲线，与每个检验都在 Bonferroni 水平 0.05/m 下进行时同一概率的比较。](./plots/fwer-growth.py)

当比较不是事先选定时，危险最大。稳妥的做法是在分析之前就关于某个潜在效应陈述一个假设，然后对它只作一次检验。数据窥探（data dredging），也称 data snooping 或 data fishing，则相反：它对数据作许多检验，只报告其中显著的，使得并不存在真实效应时也呈现出具有统计显著性的模式。把最大与最小的样本均值拿来比较，只因为它们看上去不同，就是对所有成对比较的一次隐蔽的多重比较，必须按这种方式来评判。

为描述可能出什么问题，把 $m$ 个假设 $H_{0,1}, \dots, H_{0,m}$ 按其真伪以及是否被拒绝分类：

| $H_{0,i}$ | 接受 | 拒绝 | 合计 |
|---|---|---|---|
| 真 | $U$ | $V$ | $m_0$ |
| 假 | $T$ | $S$ | $m - m_0$ |
| 合计 | $m - R$ | $R$ | $m$ |

只有 $m$ 与 $R$，即拒绝（"发现"）的个数，是可观测的。$V$ 是错误拒绝（**第一类错误**）的个数，$T$ 是漏检效应（**第二类错误**）的个数，$S$ 是正确发现的个数。

## 4.2. 族错误率与错误发现率

**定义 4.2.1（族错误率）** 多重检验方法的**族错误率**是该族检验中至少出现一次第一类错误的概率：

$$
\mathrm{FWER} = \mathbb{P}(V \ge 1).
$$
如果无论真假假设如何配置，都有 $\mathrm{FWER} \le \alpha$，则称某方法在水平 $\alpha$ 下控制了 FWER（强控制）；如果只在所有原假设都为真时才有此式，$\mathrm{FWER} = \mathbb{P}(\text{拒绝至少一个 } H_{0,i} \mid \text{所有 } H_{0,i} \text{ 为真})$，则是弱意义下的控制。

"族"的含义是"同时"。当 $a = 4$ 时有六个假设 $\mu_i = \mu_k$；在全局原假设 $\mu_1 = \cdots = \mu_4$ 下，如果六个假设中有任何一个被错误地拒绝，研究就犯了错误。设想把研究重复 $100$ 次。只检验 $\mu_1 = \mu_2$，水平 $0.05$，则大约在 $100$ 次研究中有 $5$ 次出现错误拒绝。检验全部六个，FWER $= 0.05$，则六者中任何一个被错误拒绝大约也在 $100$ 次研究中出现 $5$ 次：误差预算花在整个族上，而不是花在每个比较上。**逐比较错误率**（[3.3.13](/3.3.13)），即每个比较单独的第一类错误率，是未经调整的检验所控制的东西。

当检验了许多假设、少量的错误发现可以接受时，控制 FWER 过于严格。Benjamini 与 Hochberg（1995）提出改为控制拒绝中错误发现的期望比例。

**定义 4.2.2（错误发现率）** **错误发现率**是

$$
\mathrm{FDR} = \mathbb{E}\Bigl[\frac{V}{\max(R, 1)}\Bigr],
$$
即被拒绝的假设中错误发现的期望比例，没有拒绝时比值取 $0$。

**命题 4.2.1** 对每个方法都有 $\mathrm{FDR} \le \mathrm{FWER}$，所有原假设都为真（$m_0 = m$）时等号成立。因此在水平 $\alpha$ 下控制 FWER 蕴含着在水平 $\alpha$ 下控制 FDR，而控制 FWER 是更严格的要求。

**证明** 若 $V = 0$，则 $V/\max(R, 1) = 0$；若 $V \ge 1$，则 $R \ge V \ge 1$，$V/R \le 1$。于是 $V/\max(R, 1) \le \boldsymbol{1}_{\{V \ge 1\}}$，取期望得 $\mathrm{FDR} \le \mathbb{P}(V \ge 1) = \mathrm{FWER}$。若 $m_0 = m$，则每次拒绝都是错误的，$V = R$，$V/\max(R, 1) = \boldsymbol{1}_{\{V \ge 1\}}$ 精确成立。$\square$

当许多假设为假时，$S$ 往往很大，比值 $V/R$ 比 $\boldsymbol{1}_{\{V \ge 1\}}$ 小得多，控制 FDR 允许多得多的拒绝。控制哪种错误率，取决于假阳性相对于漏检效应的代价。

- 一项探索性研究考察一种新的抗癌药物，记录许多终点：代谢率、可测量病灶的个数与大小、非靶病灶的状态、肿瘤标志物、基线活检时的基因表达，等等。目的是找出有希望的信号，留待以后确认；在许多发现中夹杂几条错误线索是可以容忍的，而漏掉真实的效应代价高昂。控制 FDR 保持了使发现成为可能的功效。
- 一种针对极危险疾病的诊断方案由若干项检查组成，只有每项检查都这样说，患者才被宣布健康。"被宣布健康"意义上的一次假阳性，可能让病人回家，后果可能是致命的。这里连一次错误也不可接受，必须控制 FWER。

一般来说，控制 FWER 适合只有少数计划内比较的确证性研究，其中任何错误的论断都很严重；控制 FDR 适合有许多假设（基因、体素、终点）的筛选，其发现之后还要跟进。

## 4.3. Fisher 最小显著差数

### 4.3.1. 从多个 t 检验到 LSD

对一对 $(i, j)$，[3.8.2](/3.8.2) 的两样本 $t$ 检验只用第 $i$ 组与第 $j$ 组的数据：

$$
t_0 = \frac{\bar y_{i\cdot} - \bar y_{j\cdot}}{s_p\sqrt{\frac{1}{n_i} + \frac{1}{n_j}}} \sim t_{n_i + n_j - 2},\qquad s_p^2 = \frac{(n_i - 1)s_i^2 + (n_j - 1)s_j^2}{n_i + n_j - 2}.
$$
在方差分析模型下，所有 $a$ 个组有相同的方差，所以 $\sigma^2$ 的更好的估计是合并了全部 $N$ 个观测的 $\mathrm{MS}_{\mathrm{E}}$。

**定义 4.3.1（Fisher 最小显著差数）** **Fisher 最小显著差数**方法用

$$
t_0 = \frac{\bar y_{i\cdot} - \bar y_{j\cdot}}{\sqrt{\mathrm{MS}_{\mathrm{E}}\bigl(\frac{1}{n_i} + \frac{1}{n_j}\bigr)}} \sim t_{N-a}\quad\text{在 } H_0 \text{ 下}
$$
检验 $H_0\colon \mu_i = \mu_j$，当 $\lvert t_0\rvert > t_{N-a,\alpha/2}$ 时拒绝，即当 $\lvert\bar y_{i\cdot} - \bar y_{j\cdot}\rvert$ 超过最小显著差数

$$
\mathrm{LSD} = t_{N-a,\alpha/2}\sqrt{\mathrm{MS}_{\mathrm{E}}\Bigl(\frac{1}{n_i} + \frac{1}{n_j}\Bigr)}\qquad\Bigl(= t_{N-a,\alpha/2}\sqrt{2\mathrm{MS}_{\mathrm{E}}/n}\ \text{平衡时}\Bigr)
$$
时拒绝。

LSD 检验与分别作 $m$ 次两样本 $t$ 检验有两点不同。标准误用的是全部 $a$ 个组的合并方差，而不是被比较的两个组的；参照分布的自由度是 $N - a$，而不是 $n_i + n_j - 2$。这两处改变都来自方差相同的假定，并且都使检验更有功效：方差的估计更精确，临界值更小。（如果方差不等，合并的 $\mathrm{MS}_{\mathrm{E}}$ 对某一特定的对可能严重失真，这是检查该假定的一个理由，见 [3.8.5](/3.8.5)。）对刻蚀数据，比较 $160$ 与 $180\,\mathrm{W}$ 时，两样本 $t$ 检验给出自由度 $8$ 上的 $t_0 = 3.10$，$p = 0.015$；LSD 检验给出自由度 $16$ 上的 $t_0 = 36.2/\sqrt{333.7 \times 2/5} = 36.2/11.55 = 3.13$，$p = 0.0064$。

### 4.3.2. 作为一般线性检验的 LSD

LSD 检验是完全均值模型内对单一约束 $\mu_i = \mu_j$ 的一般线性检验（[3.8.3](/3.8.3)）。简化模型迫使这两个均值相等，在 [3.8.3](/3.8.3) 的几何图景中，它是模型空间 $\Omega$ 的一个 $a - 1$ 维子空间 $\omega_{ij}$，所以 $\Omega \ominus \omega_{ij}$ 是一维的，由这样的向量 $\boldsymbol{v}$ 张成：它在第 $i$ 组的分量为 $1/n_i$，在第 $j$ 组为 $-1/n_j$，其余为 $0$。误差平方和的减少量是 $\boldsymbol{y}$ 在 $\boldsymbol{v}$ 上的投影长度的平方：

$$
\mathrm{SS}_{\mathrm{E}}(R) - \mathrm{SS}_{\mathrm{E}}(F) = \frac{(\boldsymbol{v}^{\mathsf T}\boldsymbol{y})^2}{\boldsymbol{v}^{\mathsf T}\boldsymbol{v}} = \frac{(\bar y_{i\cdot} - \bar y_{j\cdot})^2}{\frac{1}{n_i} + \frac{1}{n_j}},
$$
所以

$$
F = \frac{[\mathrm{SS}_{\mathrm{E}}(R) - \mathrm{SS}_{\mathrm{E}}(F)]/1}{\mathrm{MS}_{\mathrm{E}}(F)} = \frac{(\bar y_{i\cdot} - \bar y_{j\cdot})^2}{\mathrm{MS}_{\mathrm{E}}\bigl(\frac{1}{n_i} + \frac{1}{n_j}\bigr)} = t_0^2 \sim F_{1,N-a}.
$$
整体的方差分析 $F$ 检验把 $\Omega$ 与 $\omega$ 比较（$a - 1$ 个自由度）；每个 LSD 检验把 $\Omega$ 与一个超平面 $\omega_{ij}$ 比较（一个自由度）。

### 4.3.3. LSD 不控制错误率

LSD 方法不对比较的个数作任何调整。每个检验的水平是 $\alpha$，所以它控制逐比较错误率，但既不控制 FWER 也不控制 FDR：在全局原假设下，所有拒绝都是错误的，FDR $=$ FWER（命题 4.2.1），而对 $a = 4$、$N - a = 16$，六个 LSD 检验中至少一个拒绝的概率是

$$
\mathbb{P}\Bigl(\max_{i<j}\lvert t_{ij}\rvert > t_{16,0.025}\Bigr) = \mathbb{P}\bigl(Q_{4,16} > \sqrt2 \times 2.120\bigr) = 0.19,
$$
其中 $Q_{4,16}$ 服从 4.6 节的学生化极差分布；对 $a = 6$ 则是 $0.34$。作为交换，LSD 的临界值最小，因此功效是本章所有方法中最高的。

一种常见的保护措施是受保护的 LSD：只有当整体 $F$ 检验显著时才作成对检验。在全局原假设下，到达成对检验的概率就是 $\alpha$，所以 FWER 在弱意义下得到控制；但一旦有一些均值不同，整体检验就很容易通过，对其余相等的均值，保护便不复存在。因此，受保护的 LSD 一般不是强意义下的 FWER 方法。LSD 适用于单个计划内的比较，或者用作初步筛选，其发现将被进一步确认。

### 4.3.4. 软件输出

R 用 `pairwise.t.test` 以合并标准差计算全部未经调整的成对检验：

```r
pairwise.t.test(etch.rate$rate, etch.rate$RF, p.adjust.method = "none")
```

```text
	Pairwise comparisons using t tests with pooled SD 

data:  etch.rate$rate and etch.rate$RF 

    160     180     200    
180 0.0064  -       -      
200 8.4e-06 0.0046  -      
220 3.7e-10 1.7e-08 2.7e-06

P value adjustment method: none 
```

每一对在 $0.05$ 水平下都有差异。商业软件会连同标准误打印同样的信息：每个水平均值的标准误是 $\sqrt{\mathrm{MS}_{\mathrm{E}}/n} = 18.27/\sqrt5 = 8.17$，每个均值之差的标准误是 $\sqrt{2\mathrm{MS}_{\mathrm{E}}/n} = 18.27\sqrt{2/5} = 11.55$；取 $t_{16,0.025} = 2.120$，最小显著差数是 $2.120 \times 11.55 = 24.5$，观测到的六个差（$36.2$ 到 $155.8$）都超过它。

## 4.4. 控制 FDR：Benjamini–Hochberg 方法

设用统计量检验 $m$ 个原假设 $H_{0,1}, \dots, H_{0,m}$（全局原假设是它们的交 $\bigcap_iH_{0,i}$），各统计量的 $p$ 值 $p_1, \dots, p_m$ 在各自的原假设下服从 $(0, 1)$ 上的均匀分布。

**算法 4.4.1（Benjamini–Hochberg 方法）** 取定 $\alpha \in (0, 1)$。

1. 把 $p$ 值排序，$p_{(1)} \le p_{(2)} \le \cdots \le p_{(m)}$。
2. 令 $i_0$ 为使 $p_{(i)} \le \frac{i}{m}\alpha$ 成立的最大的 $i$（若没有，则不拒绝任何假设）。
3. 拒绝 $H_{0,(1)}, \dots, H_{0,(i_0)}$。

用图表示，就是画出 $p_{(i)}$ 对 $i$ 的点，并画直线 $y = \alpha x/m$；直到最后一个低于该直线的 $p$ 值为止的所有假设都被拒绝，即使其中某些自己的 $p$ 值在直线之上。阈值从 Bonferroni 水平 $\alpha/m$ 开始，上升到 $\alpha$。软件报告的调整 $p$ 值是 $\tilde p_{(i)} = \min_{k \ge i}\min\bigl(1, \frac{m}{k}p_{(k)}\bigr)$，当 $\tilde p_{(i)} \le \alpha$ 时拒绝 $H_{0,(i)}$。

**定理 4.4.1** 若各 $p$ 值独立，则 Benjamini–Hochberg 方法满足

$$
\mathrm{FDR} = \frac{m_0}{m}\alpha \le \alpha.
$$

**证明** 若 $m_0 = 0$，则 $V = 0$，$\mathrm{FDR} = 0$。设 $m_0 \ge 1$，令 $\mathcal{H}_0$ 为真原假设的下标集，$V_i = \boldsymbol{1}\{H_{0,i} \text{ 被拒绝}\}$。则 $V/\max(1, R) = \sum_{i\in\mathcal{H}_0}X_i$，其中

$$
X_i = \frac{V_i}{\max(1, R)} = \sum_{k=1}^m\frac{V_i}{k}\boldsymbol{1}\{R = k\} = \sum_{k=1}^m\frac{\boldsymbol{1}\{p_i \le \frac{k}{m}\alpha\}}{k}\boldsymbol{1}\{R = k\},
$$
因为当恰有 $k$ 个假设被拒绝时，$H_{0,i}$ 在其中当且仅当 $p_i \le \frac{k}{m}\alpha$。设 $R(p_i \to 0)$ 是把 $p_i$ 换成 $0$、其他 $p$ 值不变时的拒绝个数。在事件 $p_i \le \frac km\alpha$ 上，$R = k$ 当且仅当 $R(p_i \to 0) = k$：记 $N_j$ 为不超过 $\frac jm\alpha$ 的 $p$ 值的个数，该方法拒绝 $R = \max\{j\colon N_j \ge j\}$ 个假设，而把 $p_i$ 移到 $0$ 对每个 $j \ge k$ 都不改变 $N_j$，所以满足 $N_j \ge j$ 的最大的 $j \ge k$ 在两种情形下相同。因此

$$
X_i = \sum_{k=1}^m\frac{\boldsymbol{1}\{p_i \le \frac{k}{m}\alpha\}}{k}\boldsymbol{1}\{R(p_i \to 0) = k\}.
$$
$R(p_i \to 0)$ 只依赖于其他 $p$ 值，它们独立于 $p_i \sim \mathrm{U}(0, 1)$。以它们为条件，

$$
\mathbb{E}[X_i \mid p_{-i}] = \sum_{k=1}^m\frac{\mathbb{P}(p_i \le \frac km\alpha)}{k}\boldsymbol{1}\{R(p_i \to 0) = k\} = \frac{\alpha}{m}\sum_{k=1}^m\boldsymbol{1}\{R(p_i \to 0) = k\} = \frac{\alpha}{m},
$$
因为 $R(p_i \to 0) \ge 1$ 恰取一个值。由全期望公式 $\mathbb{E}X_i = \alpha/m$，$\mathrm{FDR} = \sum_{i\in\mathcal{H}_0}\mathbb{E}X_i = m_0\alpha/m$。$\square$

在检验统计量正相依时，界 $\mathrm{FDR} \le \alpha$ 仍然成立（Benjamini 与 Yekutieli，2001），这包括方差分析的成对比较。该定理的另一种证明见 [3.4.12](/3.4.12)。

对刻蚀数据，4.3.4 节的六个未经调整的 $p$ 值可以手工处理，也可以用 `p.adjust`：

```r
# Obtain p-values for each pairwise comparison
pairwise_p <- pairwise.t.test(etch.rate$rate, etch.rate$RF,
                              p.adjust.method = "none")$p.value
p <- pairwise_p[lower.tri(pairwise_p, diag = TRUE)]
# Step 1: sort the p-values
sorted_p <- sort(p); ranked_p <- rank(p)
# Step 2: find the largest i such that p_(i) <= (i/m) * alpha
m <- length(p); critical_values <- (1:m / m) * 0.05
valid_indices <- sorted_p <= critical_values
if (any(valid_indices)) {
  largest_i <- max(which(valid_indices))
  threshold <- sorted_p[largest_i]
  # Step 3: determine significant hypotheses
  significant_pairs <- p <= threshold
} else {
  significant_pairs <- rep(FALSE, length(p))
}
significant_pairs
pairwise.t.test(etch.rate$rate, etch.rate$RF, p.adjust.method = "BH")
```

```text
> pairwise_p
             160          180          200
180 6.416224e-03           NA           NA
200 8.438627e-06 4.624381e-03           NA
220 3.728559e-10 1.693894e-08 2.683834e-06
> significant_pairs
[1] TRUE TRUE TRUE TRUE TRUE TRUE

	Pairwise comparisons using t tests with pooled SD 

data:  etch.rate$rate and etch.rate$RF 

    160     180     200    
180 0.0064  -       -      
200 1.3e-05 0.0055  -      
220 2.2e-09 5.1e-08 5.4e-06

P value adjustment method: BH 
```

最大的 $p$ 值 $0.0064$ 低于它的阈值 $\frac66 \times 0.05$，所以六个假设全部被拒绝。调整后的值显示了规则：第二大的 $0.0046$ 变成 $\frac65 \times 0.0046 = 0.0055$；最小的 $3.7\times10^{-10}$ 变成 $6 \times 3.7\times10^{-10} = 2.2\times10^{-9}$。

在大规模检验中，几种错误率的差别最为清楚。在下面的模拟中，每次重复进行 $m = 1000$ 个单侧 $z$ 检验，其中 $800$ 个原假设为真，$200$ 个的效应大小为 $2.5$，$\alpha = 0.05$，分别不作校正、用 BH 与用 Bonferroni。不作校正时，平均错误发现比例约为 $0.20$，每次重复都含有假阳性（FWER $= 1$）；BH 把 FDR 保持在约 $0.04 = \frac{m_0}{m}\alpha$，但仍有约 $98\%$ 的重复至少出现一次假阳性；Bonferroni 使 FWER 约为 $0.04$，FDR 几乎为零。代价体现在功效上：检出的 $200$ 个真实效应的比例分别约为 $0.80$、$0.47$ 与 $0.08$。

![1000 次重复、每次 1000 个单侧 z 检验的模拟，其中 80% 的原假设为真，alpha = 0.05。左：不作校正、用 Benjamini-Hochberg 与用 Bonferroni 时错误发现比例的分布。右：三种方法的平均 FDR、FWER 与功效。](./plots/fdr-fwer-simulation.py)

## 4.5. 控制 FWER：Bonferroni 校正

定义事件 $A_{ij} = \bigl\{\lvert t_{ij}\rvert > t_{N-a,\alpha/(2m)}\bigr\}$，其中 $t_{ij}$ 是第 $(i, j)$ 对的 LSD 统计量。由 Bonferroni 不等式（容斥原理的第一步），

$$
\mathbb{P}\Bigl(\bigcup_{(i,j)\colon\mu_i = \mu_j}A_{ij}\Bigr) \le \sum_{(i,j)\colon\mu_i = \mu_j}\mathbb{P}(A_{ij}) \le m\cdot\frac{\alpha}{m} = \alpha.
$$
所以把 $m$ 个比较中的每一个都在水平 $\alpha/m$ 下检验（**Bonferroni 校正**），无论检验之间如何相依，都在强意义下把 FWER 控制在水平 $\alpha$。等价地，经 Bonferroni 调整的 $p$ 值是 $\min(1, mp_i)$，低于 $\alpha$ 者显著。对 $m = 20$ 个独立检验，每个检验的水平是 $0.05/20 = 0.0025$，FWER 是 $1 - (1 - 0.0025)^{20} = 0.0488$。对独立检验，精确的每检验水平是 $1 - (1 - \alpha)^{1/m} = 0.00256$（**Šidák 校正**），仅略大：当检验独立时，Bonferroni 损失很小。

```r
pairwise.t.test(etch.rate$rate, etch.rate$RF, p.adjust.method = "bonferroni")
```

```text
	Pairwise comparisons using t tests with pooled SD 

data:  etch.rate$rate and etch.rate$RF 

    160     180     200    
180 0.038   -       -      
200 5.1e-05 0.028   -      
220 2.2e-09 1.0e-07 1.6e-05

P value adjustment method: bonferroni 
```

每一项都是未经调整值的六倍：$6 \times 0.0064 = 0.038$，$6 \times 0.0046 = 0.028$，$6 \times 8.4\times10^{-6} = 5.1\times10^{-5}$。这个恒定的比值就是在输出中认出 Bonferroni 调整的办法。六对在 $0.05$ 水平下仍然全部显著。

控制 FWER 的代价是功效：使假阳性变少，就使假阴性变多。下面的代码模拟 $1000$ 个单侧检验，其中 $900$ 个原假设为真，$100$ 个有 $3$ 个标准差的平移：

```r
x <- c(rnorm(900), rnorm(100, mean = 3))
p <- pnorm(x, lower.tail = F)
test <- p > 0.05
summary(test[1:900]); summary(test[901:1000])
```

```text
   Mode   FALSE    TRUE 
logical      46     854 
   Mode   FALSE    TRUE 
logical      88      12 
```

在这次运行中，$900$ 个真原假设中有 $46$ 个在水平 $0.05$ 下被拒绝，$100$ 个真实效应中有 $12$ 个被漏掉。在若干水平上并分别用两种校正重复计数，得到第一类错误（在 $900$ 个真原假设中）与第二类错误（在 $100$ 个假原假设中）的比例如下：

| 第一类错误率，$\alpha =$ | 0.0001 | 0.001 | 0.01 | 0.025 | 0.05 | 0.1 |
|---|---|---|---|---|---|---|
| 未校正 | 0.0011 | 0.0022 | 0.0144 | 0.0344 | 0.0511 | 0.1056 |
| Bonferroni | 0 | 0 | 0 | 0.0011 | 0.0011 | 0.0011 |
| BH | 0 | 0 | 0.0011 | 0.0022 | 0.0033 | 0.0122 |

| 第二类错误率，$\alpha =$ | 0.0001 | 0.001 | 0.01 | 0.025 | 0.05 | 0.1 |
|---|---|---|---|---|---|---|
| 未校正 | 0.70 | 0.45 | 0.20 | 0.13 | 0.12 | 0.07 |
| Bonferroni | 1 | 0.94 | 0.87 | 0.80 | 0.77 | 0.70 |
| BH | 1 | 0.81 | 0.57 | 0.39 | 0.30 | 0.20 |

在每个水平上，两种校正都几乎消除了第一类错误，Bonferroni 最彻底，同时两者都增加了第二类错误，Bonferroni 远多于 BH。Bonferroni 校正不要求独立性假定，这是它的巨大优点；它的缺点是当检验个数很多、或检验统计量正相关时偏保守，因为此时并集界高估了并集的概率。对方差分析的成对比较，统计量以已知的方式相关，利用这种结构可以得到更有功效的方法，即 Tukey 方法。

## 4.6. Tukey 的真实显著差

### 4.6.1. 学生化极差

**定义 4.6.1（学生化极差）** 设 $W_1, \dots, W_k$ 是一个样本，$s$ 是它们标准差的一个自由度为 $\nu$ 的估计。**学生化极差**是最大值与最小值之差，以 $s$ 为单位度量：

$$
q = \frac{W_{\max} - W_{\min}}{s}.
$$
当 $W_1, \dots, W_k \overset{\text{iid}}{\sim} \mathcal{N}(\mu, \sigma^2)$ 且 $\nu s^2/\sigma^2 \sim \chi^2_\nu$ 与各 $W_i$ 独立时，$q$ 的分布不依赖于 $\mu$ 或 $\sigma$；它就是**学生化极差分布** $Q_{k,\nu}$（[3.3.13](/3.3.13)），上 $\alpha$ 分位数为 $q_{k,\nu,\alpha}$。

在 Tukey 检验中，样本由 $a$ 个处理均值构成。如果从 $a$ 个同为 $\mathcal{N}(\mu, \sigma^2)$ 的正态总体中各抽样 $n$ 次，则

$$
q = \frac{\bar y_{\max} - \bar y_{\min}}{\sqrt{\mathrm{MS}_{\mathrm{E}}/n}} \sim Q_{a,N-a},
$$
其中 $\bar y_{\max}$ 是样本均值中最大的，$\bar y_{\min}$ 是最小的，$\mathrm{MS}_{\mathrm{E}}$ 是自由度为 $N - a$ 的合并样本方差。更多个均值的极差更大，所以 $q_{a,\nu,\alpha}$ 随 $a$ 增大。

![自由度 nu = 16 的学生化极差分布对 k = 2、3、4 与 6 个均值的密度；标出了上 5% 分位数。](./plots/studentized-range.py)

当 $k = 2$ 时密度在 $0$ 处最大，而当 $k \ge 3$ 时它在那里为零。原因是只有两个均值时，极差就是它们之差的绝对值：

$$
q = \frac{\lvert\bar y_1 - \bar y_2\rvert}{s/\sqrt n} = \sqrt2\,\frac{\lvert\bar y_1 - \bar y_2\rvert}{s\sqrt{2/n}} = \sqrt2\lvert t\rvert.
$$
在原假设下，$\bar y_1 - \bar y_2 \sim \mathcal{N}(0, 2\sigma^2/n)$，其绝对值服从半正态分布，而 $\lvert t\rvert$ 有折叠 $t$ 密度，它在 $(0, \infty)$ 上递减，最大值在 $0$。有三个或更多均值时，只有所有均值几乎重合，极差才会接近 $0$，这不太可能。恒等式 $q = \sqrt2\lvert t\rvert$ 还说明，当 $k = 2$ 时 Tukey 检验就是普通的 $t$ 检验：$q_{2,\nu,\alpha}/\sqrt2 = t_{\nu,\alpha/2}$。在 R 中，`qtukey(p = .95, nmeans = 2, df = 8)/sqrt(2)` 与 `qt(p = .975, df = 8)` 都返回 $2.306$。

### 4.6.2. Tukey 检验

Tukey 检验（也称 Tukey 极差检验、真实显著差检验，或 **Tukey HSD**）在平衡实验中用统计量

$$
q_0 = \frac{\lvert\bar y_{i\cdot} - \bar y_{j\cdot}\rvert}{\sqrt{\mathrm{MS}_{\mathrm{E}}/n}} = \sqrt2\lvert t_{ij}\rvert
$$
对每一对检验 $H_0\colon \mu_i = \mu_j$ 对 $H_1\colon \mu_i \ne \mu_j$，当 $q_0 > q_{a,N-a,\alpha}$ 时拒绝，即当 $\lvert\bar y_{i\cdot} - \bar y_{j\cdot}\rvert > \mathrm{HSD} = q_{a,N-a,\alpha}\sqrt{\mathrm{MS}_{\mathrm{E}}/n}$ 时拒绝。等价地，同时置信区间为

$$
\bar y_{i\cdot} - \bar y_{j\cdot} \pm q_{a,N-a,\alpha}\sqrt{\frac{\mathrm{MS}_{\mathrm{E}}}{n}},\qquad 1 \le i < j \le a.
$$

**定理 4.6.1** 在平衡的单因子实验中，Tukey 区间以恰好 $1 - \alpha$ 的概率同时覆盖所有差 $\mu_i - \mu_j$。特别地，Tukey 检验在强意义下把 FWER 控制在水平 $\alpha$，在全局原假设下等号成立：

$$
\mathbb{P}\Bigl(\text{断定至少有一对 } \mu_i \ne \mu_j \Bigm| H_0\colon \mu_1 = \cdots = \mu_a\Bigr) = \mathbb{P}\Bigl(\max_{i,j}\frac{\lvert\bar y_{i\cdot} - \bar y_{j\cdot}\rvert}{\sqrt{\mathrm{MS}_{\mathrm{E}}/n}} > q_{a,N-a,\alpha}\Bigr) = \mathbb{P}\Bigl(\frac{\bar y_{\max} - \bar y_{\min}}{\sqrt{\mathrm{MS}_{\mathrm{E}}/n}} > q_{a,N-a,\alpha}\Bigr) = \alpha.
$$

**证明** 设 $W_i = \bar Y_{i\cdot} - \mu_i \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2/n)$，与 $\mathrm{MS}_{\mathrm{E}}$ 独立。所有区间都覆盖，当且仅当对所有对有 $\lvert W_i - W_j\rvert \le q_{a,N-a,\alpha}\sqrt{\mathrm{MS}_{\mathrm{E}}/n}$，即当且仅当 $(W_{\max} - W_{\min})/\sqrt{\mathrm{MS}_{\mathrm{E}}/n} \le q_{a,N-a,\alpha}$，由定义 4.6.1，这个事件的概率为 $1 - \alpha$。对某个为真的 $\mu_i = \mu_j$ 的错误拒绝，意味着该对的区间不含 $\mu_i - \mu_j = 0$，所以它蕴含不覆盖，于是对均值的每种配置，FWER 至多为 $\alpha$。在全局原假设下，$W_i - W_j = \bar Y_{i\cdot} - \bar Y_{j\cdot}$，两个事件重合。$\square$

因此 Tukey 比较的 $p$ 值是 $\mathbb{P}\bigl(Q_{a,N-a} \ge \sqrt2\lvert t_{ij}\rvert\bigr)$，其中 $t_{ij}$ 是 LSD 统计量；它不是 $2\mathbb{P}(t_{N-a} \ge \lvert t_{ij}\rvert)$，后者是未经调整的 $p$ 值。

对刻蚀数据，$q_{4,16,0.05} = 4.046$，所以 $\mathrm{HSD} = 4.046 \times 8.17 = 33.05$，六个差都超过它。

```r
mod <- aov(rate ~ RF, data = etch.rate)
TukeyHSD(mod)
plot(TukeyHSD(mod))
```

```text
  Tukey multiple comparisons of means
    95% family-wise confidence level

Fit: aov(formula = rate ~ RF, data = etch.rate)

$RF
         diff        lwr       upr     p adj
180-160  36.2   3.145624  69.25438 0.0294279
200-160  74.2  41.145624 107.25438 0.0000455
220-160 155.8 122.745624 188.85438 0.0000000
200-180  38.0   4.945624  71.05438 0.0215995
220-180 119.6  86.545624 152.65438 0.0000001
220-200  81.6  48.545624 114.65438 0.0000146
```

每行给出估计的差 `diff` $= \bar y_{i\cdot} - \bar y_{j\cdot}$、同时 95% 的上下限 `lwr` 与 `upr` $= \mathrm{diff} \mp 33.05$，以及经 Tukey 调整的 $p$ 值 `p adj`。对 $180$ 与 $160\,\mathrm{W}$，$t_{ij} = 3.133$，$p = \mathbb{P}(Q_{4,16} \ge 4.431) = 0.029$，与未经调整的 $0.0064$ 和 Bonferroni 的 $0.038$ 相比：Tukey 的调整比 Bonferroni 温和，因为它考虑了六个比较的相关性。没有区间包含 $0$，所以四个功率水平彼此都有差异。

![刻蚀均值六个成对差的同时 95% 区间：Tukey 区间与各个 LSD 区间的比较。](./plots/tukey-intervals.py)

### 4.6.3. 样本量不等：Tukey–Kramer 方法

学生化极差的论证要求样本量相等，因为各均值必须有共同的方差。对于非平衡数据，改用每个差的标准误。

**定义 4.6.2（Tukey–Kramer 方法）** **Tukey–Kramer 方法**给出区间

$$
\bar y_{i\cdot} - \bar y_{j\cdot} \pm \frac{q_{a,N-a,\alpha}}{\sqrt2}\sqrt{\mathrm{MS}_{\mathrm{E}}\Bigl(\frac{1}{n_i} + \frac{1}{n_j}\Bigr)},\qquad 1 \le i < j \le a,
$$
当区间不含 $0$ 时断定 $\mu_i \ne \mu_j$。

当 $n_i = n$ 时，这就是 Tukey 区间，因为 $\frac{q}{\sqrt2}\sqrt{2\mathrm{MS}_{\mathrm{E}}/n} = q\sqrt{\mathrm{MS}_{\mathrm{E}}/n}$。对样本量不等的情形，覆盖概率不再恰好是 $1 - \alpha$，但至少是 $1 - \alpha$（Hayter，1984），所以该方法略偏保守。设计非平衡时，R 的 `TukeyHSD` 会自动应用 Tukey–Kramer 公式。

## 4.7. 对全部对照的 Scheffé 方法

### 4.7.1. 从成对比较到对照

成对差并不是仅有的感兴趣的问题。在刻蚀实验中，我们可能想问两个最低设置的平均速率是否与 $200\,\mathrm{W}$ 的速率不同，$H_0\colon (\mu_1 + \mu_2)/2 = \mu_3$，或者把 $(\mu_1 + \mu_3)/2$ 与 $\mu_4$ 比较。这类问题是**对照**（[3.3.13](/3.3.13)）：线性组合 $C = \sum_{i=1}^a c_i\mu_i$，$\sum_ic_i = 0$。一个消费者测试小组比较五款汽车的油耗：福特翼虎（混合动力）、丰田凯美瑞、丰田普锐斯（混合动力）、本田雅阁与本田思域（混合动力），每款规定 $n$ 次试驾，它可以对均值 $\mu_1, \dots, \mu_5$ 定义如下的对照：

| 问题 | $c_1$ | $c_2$ | $c_3$ | $c_4$ | $c_5$ |
|---|---|---|---|---|---|
| $C_1$：美国品牌对外国品牌 | 4 | −1 | −1 | −1 | −1 |
| $C_2$：丰田对本田 | 0 | −1 | −1 | 1 | 1 |
| $C_3$：混合动力对非混合动力 | 2 | −3 | 2 | −3 | 2 |
| $C_4$：丰田内部 | 0 | −1 | 1 | 0 | 0 |
| $C_5$：本田内部 | 0 | 0 | 0 | −1 | 1 |

对照用 $\hat C = \sum_ic_i\bar y_{i\cdot}$ 估计，$\operatorname{Var}(\hat C) = \sigma^2\sum_ic_i^2/n_i$，$H_0\colon C = 0$ 的 $t$ 统计量是

$$
t_0(C) = \frac{\hat C}{\operatorname{se}(\hat C)} = \frac{\sum_ic_i\bar y_{i\cdot}}{\sqrt{\mathrm{MS}_{\mathrm{E}}\sum_ic_i^2/n_i}},\qquad t_0(C)^2 = \frac{\mathrm{SS}_C}{\mathrm{MS}_{\mathrm{E}}},\quad \mathrm{SS}_C = \frac{\bigl(\sum_ic_i\bar y_{i\cdot}\bigr)^2}{\sum_ic_i^2/n_i},
$$
其中 $\mathrm{SS}_C$ 是**对照平方和**。对事先选定的一个对照，$\lvert t_0(C)\rvert > t_{N-a,\alpha/2}$ 是一个有效的检验。如果对照是由数据提示的，或者对要考察多少个对照没有限制，则这个族就是全体对照的集合，它是无穷的，Bonferroni 和 Tukey 都不适用。

### 4.7.2. Scheffé 检验

**定理 4.7.1（Scheffé 方法）** 对对照 $C = \sum_ic_i\mu_i$，令

$$
F_0(C) = \frac{t_0(C)^2}{a - 1} = \frac{\bigl(\sum_ic_i\bar y_{i\cdot}\bigr)^2}{(a - 1)\,\mathrm{MS}_{\mathrm{E}}\sum_ic_i^2/n_i}.
$$
当 $F_0(C) > F_{a-1,N-a,\alpha}$ 时拒绝 $H_0\colon C = 0$ 的检验，等价地，当 $\lvert\hat C\rvert > \sqrt{(a - 1)F_{a-1,N-a,\alpha}}\operatorname{se}(\hat C)$ 时拒绝的检验，在全体对照的族上把 FWER 控制在水平 $\alpha$。在全局原假设下，

$$
\sup_C F_0(C) = F_0 = \frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}},
$$
即方差分析的 $F$ 统计量，且上确界在 $c_i \propto n_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})$ 处取到。

**证明** 由于 $\sum_ic_i = 0$，$\hat C = \sum_ic_i\bar y_{i\cdot} = \sum_ic_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})$，其中 $\bar y_{\cdot\cdot} = \sum_in_i\bar y_{i\cdot}/N$。对向量 $(c_i/\sqrt{n_i})$ 与 $(\sqrt{n_i}(\bar y_{i\cdot} - \bar y_{\cdot\cdot}))$ 应用 **Cauchy–Schwarz 不等式**，

$$
\hat C^2 = \Bigl(\sum_i\frac{c_i}{\sqrt{n_i}}\sqrt{n_i}(\bar y_{i\cdot} - \bar y_{\cdot\cdot})\Bigr)^2 \le \sum_i\frac{c_i^2}{n_i}\cdot\sum_in_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})^2 = \sum_i\frac{c_i^2}{n_i}\cdot\mathrm{SS}_{\mathrm{Tr}},
$$
当 $c_i/\sqrt{n_i} \propto \sqrt{n_i}(\bar y_{i\cdot} - \bar y_{\cdot\cdot})$ 时取等号，这是一个对照。因此

$$
t_0(C)^2 = \frac{\hat C^2}{\mathrm{MS}_{\mathrm{E}}\sum_ic_i^2/n_i} \le \frac{\mathrm{SS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}} = (a - 1)F_0,\qquad\text{所以对每个对照 } F_0(C) \le F_0.
$$
在全局原假设下 $F_0 \sim F_{a-1,N-a}$，所以

$$
\mathrm{FWER} = \mathbb{P}\Bigl(\text{对某个 } C,\ F_0(C) > F_{a-1,N-a,\alpha}\Bigr) = \mathbb{P}\bigl(F_0 > F_{a-1,N-a,\alpha}\bigr) = \alpha.
$$
对均值的任意配置，对 $\bar y_{i\cdot} - \mu_i$ 代替 $\bar y_{i\cdot}$ 作同样的论证：量 $\sum_in_i\bigl((\bar y_{i\cdot} - \mu_i) - \overline{(\bar y - \mu)}\bigr)^2/((a - 1)\mathrm{MS}_{\mathrm{E}})$ 服从 $F_{a-1,N-a}$ 分布，并对每个对照同时界住 $(\hat C - C)^2/((a - 1)\widehat{\operatorname{Var}}(\hat C))$，所以区间

$$
\hat C \pm \sqrt{(a - 1)F_{a-1,N-a,\alpha}}\sqrt{\mathrm{MS}_{\mathrm{E}}\sum_i\frac{c_i^2}{n_i}}
$$
以概率 $1 - \alpha$ 覆盖所有对照，对任何为真的 $C = 0$ 的错误拒绝，概率至多为 $\alpha$。$\square$

证明确立了 Scheffé 方法与方差分析 $F$ 检验之间的精确关系。如果 $F$ 检验不拒绝，则对每个对照 $F_0(C) \le F_0 \le F_{a-1,N-a,\alpha}$，Scheffé 方法下没有对照显著。如果 $F$ 检验拒绝，则使 $c_i \propto n_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})$ 的那个对照是显著的；但这个对照可能毫无实际意义，特别是不一定有任何成对差显著。在这个意义上，Scheffé 方法与 $F$ 检验是"等价的"：$F$ 检验拒绝，当且仅当存在某个对照在 Scheffé 方法下显著。该方法对均值所有可能的对照都有效，因而对任何小的族都相当保守。

对刻蚀数据，$H_0\colon (\mu_1 + \mu_2)/2 = \mu_3$ 的 $\boldsymbol{c} = (0.5, 0.5, -1, 0)$：

```r
a <- 4; n1 <- n2 <- n3 <- n4 <- 5
N <- sum(n1 + n2 + n3 + n4)
df1 <- a - 1; df2 <- N - a
# Estimate
fit <- lm(rate ~ 0 + RF, data = etch.rate)
c <- c(0.5, 0.5, -1, 0)
est <- sum(c * coef(fit))
var <- sum(c^2 * diag(vcov(fit)))
F0 <- est^2 / var / (a - 1)
# p-value
1 - pf(F0, df1 = df1, df2 = df2)    # 0.00047
```

这里 $\hat C = (551.2 + 587.4)/2 - 625.4 = -56.1$，$\widehat{\operatorname{Var}}(\hat C) = 333.7 \times 1.5/5 = 100.1$，$F_0(C) = 56.1^2/100.1/3 = 10.48$，$p = \mathbb{P}(F_{3,16} > 10.48) = 0.00047$：即使考虑到所有可能的对照，$200\,\mathrm{W}$ 时的速率仍然超过两个较低设置的平均值。

### 4.7.3. Scheffé 定理

该方法可以推广到任何线性模型 $\boldsymbol{Y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon}$，$\boldsymbol{\varepsilon} \sim \mathcal{N}_n(\boldsymbol{0}, \sigma^2I)$，$X$ 的秩为 $r$。如果存在 $\boldsymbol{d}$ 使得对一切 $\boldsymbol{\beta}$ 有 $\mathbb{E}[\boldsymbol{d}^{\mathsf T}\boldsymbol{Y}] = \Psi$，则线性组合 $\Psi = \boldsymbol{c}^{\mathsf T}\boldsymbol{\beta}$ 是**可估函数**；它的最小二乘估计量 $\hat\Psi = \boldsymbol{d}^{\mathsf T}\boldsymbol{y}$（$\boldsymbol{d}$ 在 $X$ 的列空间中）的方差为 $\sigma^2\boldsymbol{d}^{\mathsf T}\boldsymbol{d}$，估计为 $\widehat{\operatorname{Var}}(\hat\Psi) = \hat\sigma^2\boldsymbol{d}^{\mathsf T}\boldsymbol{d}$。效应模型中的对照是可估的。

**定理 4.7.2（Scheffé 定理）** 设 $\mathcal{L}$ 是由可估函数构成的 $q$ 维空间。则

$$
\hat\Psi \pm \sqrt{qF_{q,n-r,\alpha}}\sqrt{\widehat{\operatorname{Var}}(\hat\Psi)} = \hat\Psi \pm \hat\sigma\sqrt{qF_{q,n-r,\alpha}}\sqrt{\boldsymbol{d}^{\mathsf T}\boldsymbol{d}}
$$
是对所有 $\Psi \in \mathcal{L}$ 的 $100(1 - \alpha)\%$ 同时置信区间。

证明就是定理 4.7.1 在 $q$ 维空间中的 Cauchy–Schwarz 论证。对单因子实验的对照，$q = a - 1$，$n - r = N - a$，该定理给出上面的区间。另一个特例在回归中已经熟悉：在 $\boldsymbol{y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ 中，设 $X$ 为 $n \times p$ 满秩，对所有 $\boldsymbol{x} \in \mathbb{R}^p$ 取 $\Psi = \boldsymbol{x}^{\mathsf T}\boldsymbol{\beta}$，则 $q = p$。此时 $\boldsymbol{d} = X(X^{\mathsf T}X)^{-1}\boldsymbol{x}$，$\boldsymbol{d}^{\mathsf T}\boldsymbol{d} = \boldsymbol{x}^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}$，而

$$
\boldsymbol{x}^{\mathsf T}\hat{\boldsymbol{\beta}} \pm \hat\sigma\sqrt{pF_{p,n-p,\alpha}}\sqrt{\boldsymbol{x}^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}}
$$
是整个回归曲面的同时带。对简单线性回归，$p = 2$，$\hat\mu_x = \boldsymbol{x}^{\mathsf T}\hat{\boldsymbol{\beta}}$，$\operatorname{Var}(\hat\mu_x) = \sigma^2\bigl(\frac1n + \frac{(x - \bar X)^2}{\sum_i(X_i - \bar X)^2}\bigr)$，这个带就是 [3.3.4](/3.3.4) 的 Working–Hotelling **置信带** $\hat\mu_x \pm W s(\hat\mu_x)$，$W = \sqrt{2F_{2,n-2,\alpha}}$。

## 4.8. Dunnett 检验：与对照的比较

### 4.8.1. 若干处理与一个对照

Tukey 与 Scheffé 的一般方法考虑所有成对比较，或所有对照。然而常常有一个水平是对照（标准处理、安慰剂、当前的过程设置），唯一感兴趣的比较，是每个新处理与对照的比较。这样的比较只有 $m = a - 1$ 个，而不是 $\binom a2$ 个，一般方法给出的区间不必要地宽。Dunnett 检验使用的正是这 $m$ 个比较的联合分布。

举例来说，四种毯子 $b_0$、$b_1$、$b_2$、$b_3$ 在手术病人身上进行了测试，以评估恢复时间；$b_0$ 是医院里已在使用的标准毯子。病人被随机分配到四种处理，结果是恢复时间（分钟）。数据是 R 包 `multcomp` 的 `recovery` 数据集：

```r
data("recovery", package = "multcomp")
summary(recovery)
```

```text
 blanket    minutes     
 b0:20   Min.   : 5.00  
 b1: 3   1st Qu.:12.00  
 b2: 3   Median :13.00  
 b3:15   Mean   :13.49  
         3rd Qu.:16.00  
         Max.   :19.00  
```

各组的大小相差很大（$n_0 = 20$，$n_1 = n_2 = 3$，$n_3 = 15$，$N = 41$）。箱线图显示观测值大致正态，各组方差相近，并且与 $b_0$ 相比，毯子 $b_2$ 似乎缩短了平均恢复时间。我们想在控制 FWER 的同时作出这样的论断。模型是非平衡的单因素布局 $Y_{ij} = \mu + \tau_i + \varepsilon_{ij}$，$i = 0, 1, 2, 3$，$j = 1, \dots, n_i$，$\varepsilon_{ij} \sim \mathcal{N}(0, \sigma^2)$ 相互独立，自然的问题是 $b_1$、$b_2$、$b_3$ 中是否有哪个缩短了恢复时间。这需要三个单侧假设，

$$
H_i\colon \mu_i \ge \mu_0 \quad\text{对}\quad K_i\colon \mu_i < \mu_0,\qquad i = 1, 2, 3,
$$
而不是方差分析的全局假设 $\mu_0 = \mu_1 = \mu_2 = \mu_3$。拒绝任何一个 $H_i$，就在族水平 $\alpha$ 上表明至少有一种新毯子优于标准毯子。这个多对一的问题由 Dunnett（1955）解决。

### 4.8.2. 检验统计量及其分布

设第 $0$ 组是对照，$1, \dots, m$ 是处理。比较基于 $m$ 个成对的 $t$ 统计量

$$
t_i = \frac{\bar y_i - \bar y_0}{s\sqrt{\frac{1}{n_i} + \frac{1}{n_0}}},\qquad i = 1, \dots, m,\qquad s^2 = \frac{1}{\nu}\sum_{i=0}^m\sum_{j=1}^{n_i}(y_{ij} - \bar y_i)^2,\quad \nu = N - (m + 1).
$$
当 $\mu_i = \mu_0$ 时，每个 $t_i$ 服从 $t_\nu$ 分布，但它们是相依的：它们共用 $s$，且每个差都含有 $\bar y_0$。由于对 $i \ne j$，$\operatorname{Cov}(\bar y_i - \bar y_0, \bar y_j - \bar y_0) = \operatorname{Var}(\bar y_0) = \sigma^2/n_0$，

$$
\operatorname{Corr}(\bar y_i - \bar y_0, \bar y_j - \bar y_0) = \frac{1/n_0}{\sqrt{\bigl(\frac{1}{n_i} + \frac{1}{n_0}\bigr)\bigl(\frac{1}{n_j} + \frac{1}{n_0}\bigr)}} = \sqrt{\frac{n_i}{n_i + n_0}}\sqrt{\frac{n_j}{n_j + n_0}} = \rho_{ij}.
$$
在平衡情形 $n_0 = n_1 = \cdots = n_m$ 下，对所有 $i \ne j$，$\rho_{ij} = 0.5$。

**定义 4.8.1（多元 t 分布）** 设 $\boldsymbol{Z} \sim \mathcal{N}_m(\boldsymbol{0}, R)$，其中 $R$ 是相关矩阵，$V \sim \chi^2_\nu$ 与 $\boldsymbol{Z}$ 独立。$\boldsymbol{T} = \boldsymbol{Z}/\sqrt{V/\nu}$ 的分布是自由度为 $\nu$、相关矩阵为 $R$ 的 $m$ 元**多元 t 分布**。

在 $\mu_0 = \mu_1 = \cdots = \mu_m$ 下，向量 $\boldsymbol{t} = (t_1, \dots, t_m)$ 服从自由度为 $\nu$、相关矩阵为 $R = (\rho_{ij})$ 的 $m$ 元 $t$ 分布：每个坐标是标准化的正态差除以共同的 $s/\sigma$，而 $\nu s^2/\sigma^2 \sim \chi^2_\nu$ 与之独立。

**定义 4.8.2（Dunnett 检验）** **Dunnett 检验**通过 $t_1, \dots, t_m$ 的联合分布，把 $m$ 个处理与一个对照比较：对单侧备择假设 $\mu_i < \mu_0$，第 $i$ 个比较的调整 $p$ 值为

$$
p_i = \mathbb{P}\Bigl(\min_{k=1,\dots,m}T_k \le t_i\Bigr),
$$
对双侧备择假设，$p_i = \mathbb{P}\bigl(\max_k\lvert T_k\rvert \ge \lvert t_i\rvert\bigr)$，其中 $\boldsymbol{T}$ 服从上述多元 $t$ 分布。等价地，当 $t_i < -d_{m,\nu,\alpha}$（单侧）或 $\lvert t_i\rvert > \lvert d\rvert_{m,\nu,\alpha}$（双侧）时拒绝 $H_i$，其中临界值满足 $\mathbb{P}(\min_kT_k > -d_{m,\nu,\alpha}) = 1 - \alpha$ 与 $\mathbb{P}(\max_k\lvert T_k\rvert \le \lvert d\rvert_{m,\nu,\alpha}) = 1 - \alpha$。

本质上，单侧 Dunnett 检验取这 $m$ 个成对 $t$ 检验的最小值（或最大值，取决于备择假设的方向），并把它与其精确的原假设分布比较；这精确地把 FWER 控制在水平 $\alpha$，论证与 Tukey 检验相同，只是把极差换成最小值。由多元 $t$ 分布的对称性，$\mathbb{P}(\min_iT_i \le t) = 1 - \mathbb{P}(T_1 > t, \dots, T_m > t) = 1 - \mathbb{P}(T_1 < -t, \dots, T_m < -t)$，即 1 减去一个多元 $t$ 分布函数，它可以数值计算，例如用 `1 - mnormt::pmt(rep(-t, m), mean = rep(0, m), S = R, df = nu)`。

### 4.8.3. multcomp 包

`multcomp` 包通过函数 `glht`（一般线性假设）执行 Dunnett 检验以及许多其他同时检验。先用 `aov` 拟合方差分析模型，再指定比较：

```r
mod <- aov(minutes ~ blanket, data = recovery)
library("multcomp")
mc <- glht(mod,
           linfct = mcp(blanket = "Dunnett"),
           alternative = "less")
summary(mc)
summary(mc, test = adjusted(type = "bonferroni"))
```

`mcp(blanket = "Dunnett")` 定义对照矩阵

$$
C = \begin{bmatrix} -1 & 1 & 0 & 0 \\ -1 & 0 & 1 & 0 \\ -1 & 0 & 0 & 1 \end{bmatrix}
$$
作用于 $(\mu_0, \mu_1, \mu_2, \mu_3)$，其估计的协方差矩阵为 $C\operatorname{diag}(\sigma^2/n_0, \dots, \sigma^2/n_3)C^{\mathsf T}$，这就是相关系数 $\rho_{ij}$ 的来源。两个汇总如下：

```text
	 Simultaneous Tests for General Linear Hypotheses

Multiple Comparisons of Means: Dunnett Contrasts

Fit: aov(formula = minutes ~ blanket, data = recovery)

Linear Hypotheses:
             Estimate Std. Error t value  Pr(<t)    
b1 - b0 >= 0  -2.1333     1.6038  -1.330  0.2411    
b2 - b0 >= 0  -7.4667     1.6038  -4.656  <0.001 ***
b3 - b0 >= 0  -1.6667     0.8848  -1.884  0.0925 .  
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
(Adjusted p values reported -- single-step method)
```

```text
	 Simultaneous Tests for General Linear Hypotheses

Multiple Comparisons of Means: Dunnett Contrasts

Fit: aov(formula = minutes ~ blanket, data = recovery)

Linear Hypotheses:
             Estimate Std. Error t value  Pr(<t)    
b1 - b0 >= 0  -2.1333     1.6038  -1.330   0.287    
b2 - b0 >= 0  -7.4667     1.6038  -4.656 6.1e-05 ***
b3 - b0 >= 0  -1.6667     0.8848  -1.884   0.101    
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
(Adjusted p values reported -- bonferroni method)
```

每行写出原假设（`b1 - b0 >= 0`，即 $\mu_1 \ge \mu_0$）、估计 $\bar y_i - \bar y_0$、它的标准误 $s\sqrt{1/n_i + 1/n_0}$（$s = 2.59$，$\nu = 41 - 4 = 37$；对 $b_1$：$2.59\sqrt{1/3 + 1/20} = 1.604$）以及 $t_i$。单步 $p$ 值是在相关矩阵 $\rho_{12} = 0.13$、$\rho_{13} = \rho_{23} = 0.24$ 下的 Dunnett 概率 $\mathbb{P}(\min_kT_k \le t_i)$。Bonferroni 的 $p$ 值是 $3\,\mathbb{P}(t_{37} \le t_i)$，在 R 中算作 `pt(c(-1.330, -4.656, -1.884), df = nu) * 3`。它们一致地更大（$0.287$ 对 $0.241$，$0.101$ 对 $0.0925$），因为 Bonferroni 忽略了三个比较之间的正相关。只有毯子 $b_2$ 显著缩短了平均恢复时间。

同时置信区间用 `confint` 得到：

```r
ci <- confint(mc, level = 0.95)
plot(ci, xlab = "Minutes")
```

```text
	 Simultaneous Confidence Intervals

Multiple Comparisons of Means: Dunnett Contrasts

Fit: aov(formula = minutes ~ blanket, data = recovery)

Quantile = 2.1829
95% family-wise confidence level
 

Linear Hypotheses:
             Estimate lwr     upr    
b1 - b0 >= 0 -2.1333     -Inf  1.3676
b2 - b0 >= 0 -7.4667     -Inf -3.9657
b3 - b0 >= 0 -1.6667     -Inf  0.2647
```

`Quantile = 2.1829` 是单侧 Dunnett 临界值 $d_{3,37,0.05}$，即 $\max_k(-T_k)$ 的 $0.95$ 分位数，由 `mvtnorm::qmvt(p = .95, tail = "lower.tail", corr = R, df = nu)` 算出。上限是估计值 $+\,2.1829 \times$ 标准误，例如 $-7.4667 + 2.1829 \times 1.6038 = -3.966$。在 95% 的族置信水平下，毯子 $b_2$ 至少使平均恢复时间缩短 $4$ 分钟；$b_1$ 与 $b_3$ 的区间包含 $0$。

## 4.9. 方法的比较与选择

### 4.9.1. 临界值与功效

对平衡实验中的成对比较 $H_0\colon \mu_i = \mu_j$，每种方法都计算同一个统计量 $t_0 = (\bar y_{i\cdot} - \bar y_{j\cdot})/\sqrt{2\mathrm{MS}_{\mathrm{E}}/n}$，区别只在于与之比较的临界值 $c$：

| 方法 | 统计量 | 拒绝域 | 控制的错误率 | 族 |
|---|---|---|---|---|
| Fisher LSD | $t_0$ | $\lvert t_0\rvert > t_{N-a,\alpha/2}$ | 仅逐比较 | — |
| Benjamini–Hochberg | $t_0$ 的 $p$ 值 | 逐步上升规则，算法 4.4.1 | FDR | 任意 $m$ 个检验 |
| Bonferroni | $t_0$ | $\lvert t_0\rvert > t_{N-a,\alpha/(2m)}$ | FWER | 任意 $m$ 个比较 |
| Tukey (HSD) | $q_0 = \sqrt2\lvert t_0\rvert$ | $q_0 > q_{a,N-a,\alpha}$ | FWER，精确 | 全部 $\binom a2$ 个对 |
| Scheffé | $F_0 = t_0^2/(a - 1)$ | $F_0 > F_{a-1,N-a,\alpha}$ | FWER | 全部对照 |
| Dunnett | $t_i$ 对对照 | $\lvert t_i\rvert > \lvert d\rvert_{a-1,N-a,\alpha}$ | FWER，精确 | $a - 1$ 个与对照的比较 |

在 $\lvert t_0\rvert$ 的尺度上，临界值分别为 $t_{N-a,\alpha/2}$、$t_{N-a,\alpha/(2m)}$、$q_{a,N-a,\alpha}/\sqrt2$ 与 $\sqrt{(a - 1)F_{a-1,N-a,\alpha}}$。对刻蚀实验，$a = 4$，$N - a = 16$：

| 方法 | $\lvert t_0\rvert$ 的临界值 | 最小显著差数 $c\sqrt{2\mathrm{MS}_{\mathrm{E}}/n}$ |
|---|---|---|
| LSD | $t_{16,0.025} = 2.120$ | 24.5 |
| Dunnett（双侧，3 个比较） | $2.593$ | 30.0 |
| Tukey | $q_{4,16,0.05}/\sqrt2 = 4.046/\sqrt2 = 2.861$ | 33.1 |
| Bonferroni（$m = 6$） | $t_{16,0.05/12} = 3.008$ | 34.8 |
| Scheffé | $\sqrt{3F_{3,16,0.05}} = \sqrt{3 \times 3.239} = 3.117$ | 36.0 |

临界值越小，拒绝越多，功效越高。对全部成对比较，顺序是 LSD（不作调整，功效最高），然后是 Tukey（对这个族精确控制 FWER），然后是 Bonferroni（有效但保守，因为它忽略了相关性），最后是 Scheffé（保护了一个这里并不需要的无穷族）。Tukey 与 Bonferroni 的顺序对每个 $a \ge 3$ 都成立；当 $a = 2$ 时，四者全都与 $t$ 检验重合。Dunnett 的临界值低于 Tukey 的，因为它只保护 $a - 1$ 个比较。

![在 alpha = 0.05、误差自由度 16 时，全部成对比较在 |t| 尺度上的临界值，作为水平数 a 的函数：LSD、Tukey、Bonferroni 与 Scheffe。](./plots/critical-values.py)

### 4.9.2. 何时用哪种方法

选择取决于比较的族，它应当在看数据之前决定。

- 只有一个比较，或初步的筛选实验：Fisher LSD，它始终使用同一把尺子，即未经调整的 $t$ 检验。它其实不是一种多重比较方法。
- 少数几个计划内的比较或对照：Bonferroni，略偏保守，但对任何固定大小的族都有效。
- 所有成对比较，且仅此而已：Tukey HSD（非平衡时用 Tukey–Kramer）。
- 事先未指定的任何种类的比较，包括由数据提示的对照：Scheffé，它防范所有这些比较。
- 若干处理与一个对照的比较：Dunnett。
- 筛选研究中的许多假设，其中被控制在一定比例内的错误发现是可以接受的：Benjamini–Hochberg。

相应的 R 函数是：

```r
aov(y ~ treatment, data = dataframe)                        # the ANOVA fit
pairwise.t.test(y, treatment, p.adjust.method = "none")      # Fisher's LSD
pairwise.t.test(y, treatment, p.adjust.method = "bonferroni")
pairwise.t.test(y, treatment, p.adjust.method = "BH")        # "BH", also called "fdr"
TukeyHSD(aov(y ~ treatment, data = dataframe))
library(agricolae)
LSD.test(fit, "treatment", group = FALSE, console = TRUE)    # fit: an lm or aov model
scheffe.test(fit, "treatment", group = FALSE, console = TRUE)
library(multcomp)
summary(glht(fit, linfct = mcp(treatment = "Dunnett")))
```

这里用 `pairwise.t.test` 而不是反复调用 `t.test`，是因为它对每个比较都用合并标准差 $\sqrt{\mathrm{MS}_{\mathrm{E}}}$ 与 $N - a$ 个自由度来计算，这正是 LSD 所要求的；`t.test` 只会用被比较的两个组。

### 4.9.3. 阅读软件输出

软件的输出常常不用文字说明作了哪种调整，但数字会说明。把调整后的 $p$ 值与同一数据未经调整的 $p$ 值作比较。

- 如果每个调整值都是未调整值的 $m$ 倍（上限为 $1$），则方法是 Bonferroni：对刻蚀数据，$0.0064 \to 0.038$，$0.0046 \to 0.028$，比值为 $6$。
- 如果第 $k$ 小的 $p$ 值的比值是 $m/k$（出现并列时从顶端起取逐步的最小值），则是 Benjamini–Hochberg：最大的 $p$ 值不变（$0.0064$），第二大的乘以 $6/5$（$0.0046 \to 0.0055$）。
- 如果调整值小于 Bonferroni 的、大于原始值，没有恒定的比值，并且输出给出所有对的区间且半宽相同，则方法是 Tukey：$0.0064 \to 0.029$，$8.4\times10^{-6} \to 4.5\times10^{-5}$。
- 如果只出现与某一个水平的比较，可能带有单侧假设与"单步"的多元 $t$ 调整，则是 Dunnett。

最后，成对比较的结论不具有传递性。如果 $A$ 与 $B$ 没有显著差异，$B$ 与 $C$ 也没有显著差异，则关于 $A$ 与 $C$ 什么也推不出：不显著的意思是数据无法区分这些均值，而不是它们相等，两个小的差可以叠加成显著的差。

## 小结

| 方法 | $\lvert t_0\rvert$ 的临界值（$a = 4$，$\nu = 16$） | 控制 | 对成对比较的功效 | 适用情形 |
|---|---|---|---|---|
| LSD（定义 4.3.1） | $t_{\nu,\alpha/2}$（2.120） | 仅逐比较错误率；既不控制 FWER 也不控制 FDR | 最高 | 单个计划内的比较，筛选 |
| BH（算法 4.4.1） | 依赖数据，在 $p$ 尺度上介于 $\alpha/m$ 与 $\alpha$ 之间 | FDR $= m_0\alpha/m$（定理 4.4.1） | 高 | 许多检验，发现之后要跟进 |
| Bonferroni | $t_{\nu,\alpha/(2m)}$（3.008） | FWER，任意相依 | 较低 | 少数几个计划内的比较 |
| Tukey（定理 4.6.1） | $q_{a,\nu,\alpha}/\sqrt2$（2.861） | FWER，对全部成对比较精确 | 仅次于 LSD | 所有成对比较 |
| Tukey–Kramer（定义 4.6.2） | 相同，带 $\sqrt{1/n_i + 1/n_j}$ | FWER，保守 | | 所有对，非平衡 |
| Scheffé（定理 4.7.1） | $\sqrt{(a - 1)F_{a-1,\nu,\alpha}}$（3.117） | 对全部对照的 FWER | 对成对比较最低 | 未计划的对照 |
| Dunnett（定义 4.8.2） | $\lvert d\rvert_{a-1,\nu,\alpha}$（2.593） | 对与对照的比较，FWER 精确 | 对它的族较高 | 处理对对照 |

- $\mathrm{FDR} \le \mathrm{FWER}$，在全局原假设下等号成立（命题 4.2.1）；控制 FWER 更严格，当许多假设为假时，控制 FDR 更有功效。
- 与两样本 $t$ 检验不同，LSD 使用 $\mathrm{MS}_{\mathrm{E}}$ 与 $N - a$ 个自由度，并且它是 $\mu_i = \mu_j$ 的一般线性检验。
- Tukey 的 $p$ 值是 $\mathbb{P}(Q_{a,N-a} \ge \sqrt2\lvert t_{ij}\rvert)$；对两个均值，$q = \sqrt2\lvert t\rvert$。
- Scheffé 与方差分析：$\sup_CF_0(C) = F_0$，所以 $F$ 检验拒绝，当且仅当某个对照在 Scheffé 方法下显著，这个对照不必是成对差。Scheffé 定理（定理 4.7.2）还给出 Working–Hotelling 带。
- 经 Bonferroni 调整的 $p$ 值是原始值的 $m$ 倍；经 BH 调整的是 $m/k$ 倍；Tukey 的介于原始值与 Bonferroni 值之间。

## 思考题

1. 进行二十个独立检验，每个的水平为 $0.05$，所有原假设都为真。至少出现一次第一类错误的概率是多少？用 Bonferroni 方法以及精确地，使 FWER 保持在 $0.05$ 的每检验水平分别是多少？

   **答** $1 - 0.95^{20} = 0.64$。Bonferroni 用 $0.05/20 = 0.0025$，给出 FWER $1 - 0.9975^{20} = 0.0488$；独立检验的精确水平解 $1 - (1 - x)^{20} = 0.05$，$x = 1 - 0.95^{1/20} = 0.00256$（Šidák）。

2. 在同一水平 $\alpha$ 下，控制 FDR 与控制 FWER，哪个更严格？两者在什么条件下重合？

   **答** 控制 FWER 更严格。由于 $V/\max(R, 1) \le \boldsymbol{1}_{\{V \ge 1\}}$，对每个方法都有 $\mathrm{FDR} \le \mathrm{FWER}$，所以 FWER $\le \alpha$ 蕴含 FDR $\le \alpha$，反之不然。当所有原假设都为真时两者重合，因为此时 $V = R$。

3. 对刻蚀数据，比较 $\mu_{160} = \mu_{180}$ 的两样本 $t$ 检验与 LSD 检验。两组的 $s_1 = 20.02$，$s_2 = 16.74$。

   **答** 两样本：$s_p^2 = (20.02^2 + 16.74^2)/2 = 340.5$，$t_0 = 36.2/\sqrt{340.5 \times 2/5} = 3.10$，自由度 $8$，$p = 0.015$。LSD：$\mathrm{MS}_{\mathrm{E}} = 333.7$ 合并了全部四个组，$t_0 = 36.2/11.55 = 3.13$，自由度 $16$，$p = 0.0064$。两个统计量相近，因为 $s_p^2 \approx \mathrm{MS}_{\mathrm{E}}$；主要的收益在自由度上（$t_{16,0.025} = 2.120$ 对 $t_{8,0.025} = 2.306$）。两者都没有对多重性作调整。

4. 在 $a = 4$ 个水平、$N - a = 16$ 的平衡实验中，某一对的 LSD 统计量为 $t_{ij} = 3.133$。计算未经调整的、Bonferroni 的与 Tukey 的 $p$ 值。

   **答** 未调整：$2\mathbb{P}(t_{16} \ge 3.133) = 0.0064$。Bonferroni：$6 \times 0.0064 = 0.038$。Tukey：$q_0 = \sqrt2 \times 3.133 = 4.431$，$\mathbb{P}(Q_{4,16} \ge 4.431) = 0.029$（R：`ptukey(4.431, 4, 16, lower.tail = FALSE)`）。这些是本章各输出中 $180$ 对 $160\,\mathrm{W}$ 的值。

5. 三种药物各给 $7$ 名患者服用；均值为 $5.54$、$5.03$、$5.93$，$\mathrm{MS}_{\mathrm{E}} = 0.25$，自由度 $18$。仅用这些汇总统计量，在 $\alpha = 0.05$ 下分别用 LSD、Bonferroni、Tukey 与 Scheffé 方法进行全部成对比较。

   **答** 差的标准误是 $\sqrt{0.25 \times 2/7} = 0.267$。$\lvert t_0\rvert$ 的临界值：LSD $t_{18,0.025} = 2.101$；Bonferroni $t_{18,0.05/6} = 2.639$；Tukey $q_{3,18,0.05}/\sqrt2 = 3.609/\sqrt2 = 2.552$；Scheffé $\sqrt{2F_{2,18,0.05}} = \sqrt{2 \times 3.555} = 2.666$。最小显著差数是 $0.561$、$0.705$、$0.682$ 与 $0.713$。观测到的差是 $\lvert\bar y_1 - \bar y_2\rvert = 0.51$，$\lvert\bar y_1 - \bar y_3\rvert = 0.39$，$\lvert\bar y_2 - \bar y_3\rvert = 0.90$。四种方法都只发现药物 3 优于药物 2；药物 1 与二者都无法区分。不需要原始数据：每种方法都只用均值、$n_i$ 与 $\mathrm{MS}_{\mathrm{E}}$。

6. 测量三个等级的土壤的土壤–水通量：等级 1：$-1.184$、$-1.103$、$-0.8278$；等级 2：$-0.2395$、$-0.1065$、$0.24059$、$0.35347$；等级 3：$0.49103$、$0.51998$、$1.6347$。为什么原始形式的 Tukey HSD 不适用？Tukey–Kramer 方法得出什么结论？

   **答** 样本量（$3, 4, 3$）不相等，所以各均值的方差不同，均值的极差不服从学生化极差分布。均值为 $-1.038$、$0.062$、$0.882$；$\mathrm{SS}_{\mathrm{E}} = 1.156$，自由度 $7$，$\mathrm{MS}_{\mathrm{E}} = 0.165$（方差分析给出 $F_0 = 16.9$，$p = 0.002$）。取 $q_{3,7,0.05}/\sqrt2 = 4.165/\sqrt2 = 2.945$，Tukey–Kramer 区间为：等级 2 − 等级 1：$1.100 \pm 2.945 \times 0.310 = [0.19, 2.01]$；等级 3 − 等级 1：$1.920 \pm 2.945 \times 0.332 = [0.94, 2.90]$；等级 3 − 等级 2：$0.820 \pm 2.945 \times 0.310 = [-0.09, 1.73]$。等级 1 与另外两个等级都有差异；等级 2 与 3 无法区分。（等级 3 的散布也比等级 1 大得多，$s = 0.65$ 对 $0.19$，所以方差相同的假定值得检查。）

7. 在刻蚀实验中，$160\,\mathrm{W}$ 是目前使用的功率。应用哪种方法来判断三个新设置是否改变了刻蚀速率？结论是什么？

   **答** 以 $160\,\mathrm{W}$ 为对照的 Dunnett 检验，由于没有指定变化的方向，取双侧：$m = 3$，$\nu = 16$，平衡所以 $\rho_{ij} = 0.5$，$\lvert d\rvert_{3,16,0.05} = 2.593$。临界差为 $2.593 \times 11.55 = 30.0$，与对照的差为 $36.2$、$74.2$ 与 $155.8$，都更大：每个新设置都改变了平均刻蚀速率（都使之增大）。Tukey 或 Scheffé 的临界差（$33.1$、$36.0$）会更大，因为它们保护了这个问题并不需要的族。

8. 在 $\alpha = 0.05$ 下，对六个 $p$ 值 $0.001$、$0.008$、$0.039$、$0.041$、$0.042$、$0.60$ 应用 Benjamini–Hochberg 方法，并与 Bonferroni 比较。

   **答** 阈值 $\frac i6 \times 0.05$ 为 $0.0083$、$0.0167$、$0.025$、$0.0333$、$0.0417$、$0.05$。从最大的往下：$0.60 > 0.05$，$0.042 > 0.0417$，$0.041 > 0.0333$，$0.039 > 0.025$，$0.008 \le 0.0167$；所以 $i_0 = 2$，前两个假设被拒绝。Bonferroni 把每个 $p$ 值与 $0.05/6 = 0.0083$ 比较，同样拒绝 $0.001$ 与 $0.008$；这里两者一致，尽管 $0.04$ 附近的三个 $p$ 值已接近 BH 的直线。

9. 某实验的整体方差分析 $F$ 检验在水平 $\alpha$ 下不显著。Scheffé 方法能找到显著的对照吗？如果 $F$ 检验显著，Scheffé 方法一定能找到显著的成对差吗？

   **答** 都不能。每个对照都满足 $F_0(C) \le F_0$（定理 4.7.1），所以如果 $F_0 \le F_{a-1,N-a,\alpha}$，没有对照超过 Scheffé 的临界值。如果 $F_0$ 显著，则 $c_i \propto n_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})$ 的对照在 Scheffé 方法下显著，但成对差是一个特殊的对照，它的 $F_0(C)$ 可能远低于 $F_0$，所以不一定显著。
