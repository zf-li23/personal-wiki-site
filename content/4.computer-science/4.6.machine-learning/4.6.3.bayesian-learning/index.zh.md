---
title: 贝叶斯学习
description: 机器学习中的贝叶斯观点：用 Bayes 公式计算假设的后验概率；MAP 假设与 ML 假设，正则化即先验，极大似然与最小二乘；Bayes 最优分类器与 Gibbs 算法；朴素 Bayes 分类器、拉普拉斯平滑与 Dirichlet 先验，三种事件模型，对数概率与实践要点；垃圾邮件过滤与词义消歧。
---

贝叶斯学习把"学习"看作概率推理：每个假设都有一个概率，观察到训练数据后，用 **Bayes 公式**（[3.1.2](/3.1.2)）把先验概率更新为后验概率，再据此选择假设或直接做预测。这一观点有两方面的用处。在理论上，它给许多学习算法提供了统一的解释——最小二乘、正则化、集成都可以看作某种贝叶斯推理的近似；在实践中，它直接给出了一类简单、快速而有效的算法，其中最重要的是朴素 Bayes 分类器，至今仍是文本分类的标准基线。本章侧重后者：怎样把贝叶斯原理变成能用的分类器，以及使用中要注意的数值、平滑与特征问题。先验、后验、共轭先验等统计概念已在[贝叶斯推断](/3.2.7)中定义，这里只在需要时引用；更系统、更理论的处理见[贝叶斯统计](/3.7)。[上一章](/4.6.2)的评价方法用于本章的分类器，[下一章](/4.6.4)的 $k$ 近邻则是另一种完全不同的思路：不对数据的分布作任何假设。

## 3.1. Bayes 公式与假设的后验

### 3.1.1. 用先验推断后验

设 $H$ 是假设空间，$D$ 是训练数据。对每个假设 $h \in H$，

$$
\mathbb{P}(h \mid D) = \frac{\mathbb{P}(D \mid h)\,\mathbb{P}(h)}{\mathbb{P}(D)},
$$
其中各项的含义是：

| 记号 | 名称 | 含义 |
|---|---|---|
| $\mathbb{P}(h)$ | 先验概率 | 观察数据之前对 $h$ 的信念，体现背景知识 |
| $\mathbb{P}(D \mid h)$ | 似然 | 若 $h$ 成立，观察到 $D$ 的概率 |
| $\mathbb{P}(h \mid D)$ | 后验概率 | 观察到 $D$ 之后对 $h$ 的信念 |
| $\mathbb{P}(D)$ | 证据 | $D$ 的边际概率，$\mathbb{P}(D) = \sum_{h \in H}\mathbb{P}(D \mid h)\,\mathbb{P}(h)$ |

这些量分别是统计学中的**先验分布**、**似然函数**与**后验分布**（[3.2.7](/3.2.7)），只是参数换成了假设。这里要求 $H$ 中的假设两两互斥、合起来完全详尽，即 $\sum_{h \in H}\mathbb{P}(h) = 1$。$\mathbb{P}(D)$ 不依赖于 $h$，比较不同的假设时可以忽略。似然常常是许多小概率之积，实际计算总是用对数似然 $\log \mathbb{P}(D \mid h)$。

**例 3.1.1** 某种癌症在人群中的患病率为 $0.008$。一项化验对患者给出阳性的概率为 $0.98$，对非患者给出阴性的概率为 $0.97$。某人化验结果为阳性，他患癌的概率是

$$
\mathbb{P}(\text{cancer} \mid +) = \frac{0.98 \times 0.008}{0.98 \times 0.008 + 0.03 \times 0.992} = \frac{0.00784}{0.03760} \approx 0.21.
$$

化验相当准确，阳性结果下患病的概率却只有约五分之一，原因是先验概率很小：非患者的人数是患者的一百多倍，其中 $3\%$ 的假阳性在数量上超过了患者中的真阳性。忽视先验（基础比率）是直觉推理中最常见的错误。

## 3.2. MAP 假设与 ML 假设

### 3.2.1. 两种假设

学习通常要在给定训练数据时找出最可能的假设。

**定义 3.2.1（MAP 假设与 ML 假设）** 使后验概率最大的假设

$$
h_{\mathrm{MAP}} = \arg\max_{h \in H}\ \mathbb{P}(h \mid D) = \arg\max_{h \in H}\ \mathbb{P}(D \mid h)\,\mathbb{P}(h)
$$
称为**极大后验假设**（MAP 假设）。使似然最大的假设

$$
h_{\mathrm{ML}} = \arg\max_{h \in H}\ \mathbb{P}(D \mid h)
$$
称为**极大似然假设**（ML 假设）。

假设由连续参数刻画时，两者就是统计学中的**最大后验估计**与**极大似然估计**（[3.2.7](/3.2.7)、[3.2.3](/3.2.3)）。若对假设一无所知，或者认为所有假设的先验概率相同，则 $\mathbb{P}(h)$ 是常数，$h_{\mathrm{MAP}} = h_{\mathrm{ML}}$。

**例 3.2.1** 例 3.1.1 中有两个假设，cancer 与 $\lnot$cancer。$\mathbb{P}(+ \mid \text{cancer})\,\mathbb{P}(\text{cancer}) = 0.0078$，$\mathbb{P}(+ \mid \lnot\text{cancer})\,\mathbb{P}(\lnot\text{cancer}) = 0.0298$，所以 $h_{\mathrm{MAP}} = \lnot\text{cancer}$。而 $\mathbb{P}(+ \mid \text{cancer}) = 0.98 > \mathbb{P}(+ \mid \lnot\text{cancer}) = 0.03$，所以 $h_{\mathrm{ML}} = \text{cancer}$。两者不同，差别完全来自先验。

**例 3.2.2** 有两枚硬币，正面朝上的概率分别为 $p$ 与 $q$；每次以概率 $a$ 选 1 号硬币、以概率 $1-a$ 选 2 号硬币，抛若干次。$a, p, q$ 都未知。观察到四组记录（数字是所选的硬币）：2HHHT，1HTHT，2HHHT，2HTTH。求 $a, p, q$ 的 ML 估计。

先看一枚硬币：抛 $m$ 次得到 $k$ 次正面，对数似然为 $\ell(p) = k\log p + (m-k)\log(1-p)$。令 $\ell'(p) = \frac{k}{p} - \frac{m-k}{1-p} = 0$，得 $\hat p = k/m$。三个参数的似然可以分开最大化，各自都是这种形式：4 组中 1 号硬币被选了 1 次，$\hat a = 1/4$；1 号硬币抛 4 次得 2 次正面，$\hat p = 2/4$；2 号硬币抛 12 次得 8 次正面，$\hat q = 8/12$。

若记录中没有硬币的编号，似然中就含有隐变量，不能再分开最大化；这正是 **EM 算法**处理的问题，[3.5.6](/3.5.6) 用的正是两枚硬币的例子。

### 3.2.2. 先验即正则化

取对数后，MAP 假设是

$$
h_{\mathrm{MAP}} = \arg\max_{h \in H}\ \bigl[\log \mathbb{P}(D \mid h) + \log \mathbb{P}(h)\bigr] = \arg\min_{h \in H}\ \bigl[-\log \mathbb{P}(D \mid h) - \log \mathbb{P}(h)\bigr].
$$
第一项是拟合数据的损失，第二项是对假设的惩罚。机器学习中常见的"损失 + 正则项"的目标函数，大多可以这样解释：

| 先验 $\mathbb{P}(\boldsymbol{w})$ | $-\log \mathbb{P}(\boldsymbol{w})$（相差常数） | 对应的方法 |
|---|---|---|
| 均匀（无信息） | 常数 | 极大似然，无正则化 |
| $\boldsymbol{w} \sim \mathcal{N}(\boldsymbol{0}, \tau^2 I)$ | $\frac{1}{2\tau^2}\|\boldsymbol{w}\|_2^2$ | $L_2$ 正则化（**岭回归**、权重衰减） |
| 各分量独立服从 Laplace 分布，尺度为 $b$ | $\frac{1}{b}\|\boldsymbol{w}\|_1$ | $L_1$ 正则化（**Lasso**） |

所以正则化系数是先验强度的体现：$\tau$ 越小，先验越集中于 $\boldsymbol{0}$，惩罚越重。实践中正则化系数由交叉验证（[4.6.2](/4.6.2#sec-2.2.2)）选取，而不是由真实的先验信念决定。

### 3.2.3. 极大似然与最小二乘

设训练数据为 $\langle x_i, d_i\rangle$，$i = 1, \dots, m$，其中 $d_i = f(x_i) + e_i$，$f$ 是无噪声的目标函数，噪声 $e_i$ 独立同分布于 $\mathcal{N}(0, \sigma^2)$。

**定理 3.2.1（极大似然与最小二乘）** 在上述假定下，

$$
h_{\mathrm{ML}} = \arg\min_{h \in H}\ \sum_{i=1}^m \bigl(d_i - h(x_i)\bigr)^2,
$$
即极大似然假设就是使平方误差和最小的假设。

**证明** 给定 $h$ 时 $d_i \sim \mathcal{N}(h(x_i), \sigma^2)$ 相互独立，故

$$
h_{\mathrm{ML}} = \arg\max_{h \in H}\ \prod_{i=1}^m \frac{1}{\sqrt{2\pi}\,\sigma}\exp\Bigl(-\frac{(d_i - h(x_i))^2}{2\sigma^2}\Bigr).
$$
$\ln$ 单调递增，取对数不改变最大值点：

$$
h_{\mathrm{ML}} = \arg\max_{h \in H}\ \sum_{i=1}^m \Bigl[-\ln(\sqrt{2\pi}\,\sigma) - \frac{(d_i - h(x_i))^2}{2\sigma^2}\Bigr].
$$
第一项与 $h$ 无关，去掉常数因子 $\frac{1}{2\sigma^2}$，最大化负的平方误差和就是最小化平方误差和。$\square$

这给 [4.6.1](/4.6.1) 的 LMS 规则和**最小二乘法**一个概率解释：它们在正态噪声下给出 ML 假设。换一种噪声就换一种损失：Laplace 噪声对应**最小绝对偏差**；二分类中把 $h(x)$ 解释为正例的概率、标签服从两点分布，对数似然的相反数就是交叉熵损失，由此得到 **logistic 回归**（[3.4.12](/3.4.12)）。

## 3.3. Bayes 最优分类器与 Gibbs 算法

### 3.3.1. Bayes 最优分类器

前面问的是"给定数据，最可能的假设是什么"。分类时真正要问的是"给定数据，新样例 $x$ 最可能的类别是什么"。这两个问题的答案可能不同。

**例 3.3.1** 设假设空间中只有三个假设，后验概率为 $\mathbb{P}(h_1 \mid D) = 0.4$，$\mathbb{P}(h_2 \mid D) = \mathbb{P}(h_3 \mid D) = 0.3$。$h_1$ 把 $x$ 判为正例，$h_2, h_3$ 把它判为反例。MAP 假设是 $h_1$，它说 $x$ 是正例；但 $x$ 为正例的后验概率只有 $0.4$，为反例的是 $0.6$。

**定义 3.3.1（Bayes 最优分类器）** 对类别集合 $\mathcal{V}$ 与新样例 $x$，按

$$
v^* = \arg\max_{v \in \mathcal{V}}\ \sum_{h \in H}\mathbb{P}(v \mid x, h)\,\mathbb{P}(h \mid D)
$$
分类的规则称为 **Bayes 最优分类器**。

它不选一个假设，而是让所有假设按后验概率加权投票。和式就是给定 $D$ 时 $x$ 的类别的**后验预测分布**（[3.2.7](/3.2.7)），所以 Bayes 最优分类器是对后验预测分布取众数，也就是以后验预测分布为类别概率的**贝叶斯分类器**（[3.4.10](/3.4.10)）。在相同的假设空间与先验下，没有别的分类方法的平均表现能超过它（平均是对先验与数据而言的）。它的组合结果甚至可能不属于 $H$ 中的任何一个假设。

代价是计算：要对整个假设空间求和或积分。除了共轭先验等少数情形，这是做不到的。

### 3.3.2. Gibbs 算法

**定义 3.3.2（Gibbs 算法）** 按后验分布 $\mathbb{P}(h \mid D)$ 随机抽取一个假设 $h$，用 $h$ 对新样例分类。这种方法称为 **Gibbs 算法**。

Gibbs 算法只需一次抽样，计算量远小于 Bayes 最优分类器，代价有限：若目标概念确实按先验分布随机产生，Gibbs 算法的期望错误率至多是 Bayes 最优分类器的两倍（Haussler、Kearns 与 Schapire，1994）。

现代机器学习中，对 Bayes 最优分类器的近似处处可见：用 Markov 链 Monte Carlo 方法从后验抽取若干个假设再平均（**Gibbs 抽样**是其中一种，[3.5.9](/3.5.9)）；训练若干个随机初始化不同的神经网络再平均其预测（深度集成）；更一般的集成学习（[4.6.6](/4.6.6)）也可以从这一角度理解。

## 3.4. 朴素 Bayes 分类器

### 3.4.1. 条件独立假设

设每个样例由 $n$ 个属性描述，$x = (a_1, \dots, a_n)$，类别 $v \in \mathcal{V}$。最可能的类别是

$$
v_{\mathrm{MAP}} = \arg\max_{v \in \mathcal{V}}\ \mathbb{P}(v \mid a_1, \dots, a_n) = \arg\max_{v \in \mathcal{V}}\ \mathbb{P}(a_1, \dots, a_n \mid v)\,\mathbb{P}(v).
$$
$\mathbb{P}(v)$ 容易从训练数据中估计：数一数每类有多少样例。$\mathbb{P}(a_1, \dots, a_n \mid v)$ 却不行：$n$ 个二值属性的联合分布在每一类中有 $2^n - 1$ 个参数，即使 $n = 30$，也需要十亿量级的样例才能把每种取值组合都看到几次。

**定义 3.4.1（朴素 Bayes 分类器）** 假定在给定类别时各属性条件独立，

$$
\mathbb{P}(a_1, \dots, a_n \mid v) = \prod_{i=1}^n \mathbb{P}(a_i \mid v),
$$
得到的分类规则

$$
v_{\mathrm{NB}} = \arg\max_{v \in \mathcal{V}}\ \mathbb{P}(v)\prod_{i=1}^n \mathbb{P}(a_i \mid v)
$$
称为**朴素 Bayes 分类器**。

条件独立假设把参数个数从指数级降到 $n \lvert\mathcal{V}\rvert$ 量级，每个 $\mathbb{P}(a_i \mid v)$ 只需一维的计数。若条件独立假设成立，则 $v_{\mathrm{NB}} = v_{\mathrm{MAP}}$。

这个假设在实际中几乎从不成立（文本中"机器"与"学习"显然不独立），朴素 Bayes 却常常分类得很好。原因是分类只要求正确的类别得分最高，不要求概率准确：属性之间的相关性使估计的后验概率过于极端（通常过于接近 $0$ 或 $1$），但不一定改变最大值所在的类别（Domingos 与 Pazzani，1997）。因此朴素 Bayes 的类别判断可以使用，它输出的概率却不宜直接当作可信的概率，需要时应先校准。

朴素 Bayes 是一种生成式分类器：它对 $\mathbb{P}(x \mid v)$ 与 $\mathbb{P}(v)$ 建模，再用 Bayes 公式得到 $\mathbb{P}(v \mid x)$。直接对 $\mathbb{P}(v \mid x)$ 建模的 logistic 回归则是判别式的。两者构成一对生成–判别模型：对二值属性，朴素 Bayes 的决策函数也是属性的线性函数。Ng 与 Jordan（2002）发现，朴素 Bayes 达到它的渐近错误率所需的样本少得多（与属性个数的对数同阶），而 logistic 回归的渐近错误率更低；所以训练数据少时朴素 Bayes 常常更好，数据多时 logistic 回归反超。

### 3.4.2. 参数估计与拉普拉斯平滑

参数的 ML 估计是相对频率。以文本分类为例：设词表有 $K$ 个词，$n_{v,j}$ 是第 $v$ 类所有训练文档中第 $j$ 个词出现的总次数，$n_v = \sum_j n_{v,j}$，则 $\hat{\mathbb{P}}(w_j \mid v) = n_{v,j}/n_v$。问题在于：只要某个词在某一类的训练文档中从未出现，它的估计概率就是 $0$，而乘积中的一个 $0$ 会让整个类别的后验概率为 $0$，无论其他证据多强。训练数据越少、词表越大，这种情况越常见。

**定义 3.4.2（拉普拉斯平滑）** 取 $\alpha > 0$，用

$$
\hat{\mathbb{P}}(w_j \mid v) = \frac{n_{v,j} + \alpha}{n_v + \alpha K}
$$
代替相对频率，称为加性平滑；$\alpha = 1$ 时称为**拉普拉斯平滑**（加一平滑）。

拉普拉斯平滑相当于每个词在每一类中都预先"见过"一次。$0 < \alpha < 1$ 时称为 Lidstone 平滑，平滑程度更轻，常常更好；$\alpha$ 是超参数，用验证集或交叉验证选取。Mitchell 教材中的 $m$-估计 $\frac{n_{v,j} + m p}{n_v + m}$ 是同一思想：$p$ 是先验估计（如均匀的 $1/K$），$m$ 是"等效样本量"，取 $p = 1/K$、$m = \alpha K$ 即得上式。

平滑有清楚的贝叶斯解释。$\boldsymbol{\theta}_v = (\theta_{v,1}, \dots, \theta_{v,K})$ 是第 $v$ 类的词分布，词的计数服从**多项分布**；它的**共轭先验**（[3.2.7](/3.2.7)）是 Dirichlet 分布。

**定义 3.4.3（Dirichlet 分布）** 设 $\alpha_1, \dots, \alpha_K > 0$。概率单纯形 $\{\boldsymbol{\theta}\colon \theta_j \ge 0,\ \sum_j \theta_j = 1\}$ 上密度为

$$
f(\boldsymbol{\theta}) = \frac{\Gamma(\alpha_1 + \cdots + \alpha_K)}{\Gamma(\alpha_1)\cdots\Gamma(\alpha_K)}\prod_{j=1}^K \theta_j^{\alpha_j - 1}
$$
的分布称为 **Dirichlet 分布** $\mathrm{Dir}(\alpha_1, \dots, \alpha_K)$。$K = 2$ 时它就是 **Beta 分布**。

取对称的先验 $\mathrm{Dir}(\alpha, \dots, \alpha)$，观察到计数 $n_{v,1}, \dots, n_{v,K}$ 后，后验是 $\mathrm{Dir}(n_{v,1} + \alpha, \dots, n_{v,K} + \alpha)$，其**后验均值**正是定义 3.4.2 中的估计。所以拉普拉斯平滑是均匀先验（$\alpha = 1$）下的后验均值估计；它也是先验 $\mathrm{Dir}(2, \dots, 2)$ 下的最大后验估计。$\alpha$ 越大，先验越强，估计越被拉向均匀分布。

### 3.4.3. 三种事件模型

"属性 $a_i$ 是什么、$\mathbb{P}(a_i \mid v)$ 取什么分布"有不同的选择，对应朴素 Bayes 的几种常用变体：

| 变体 | 属性 | $\mathbb{P}(a_i \mid v)$ | 参数估计 | 适用 |
|---|---|---|---|---|
| 多项式朴素 Bayes | 词在文档中出现的次数 | 多项分布中词 $w_i$ 的概率 | 定义 3.4.2 | 文本分类（长文档、大词表时通常最好） |
| Bernoulli 朴素 Bayes | 每个词是否出现（$0/1$） | $\theta_{v,i}^{a_i}(1-\theta_{v,i})^{1-a_i}$ | $\hat\theta_{v,i} = \frac{\text{含 } w_i \text{ 的 } v \text{ 类文档数} + \alpha}{v \text{ 类文档数} + 2\alpha}$ | 短文本、二值特征 |
| Gauss 朴素 Bayes | 连续属性 | $\mathcal{N}(\mu_{v,i}, \sigma_{v,i}^2)$ 的密度 | 各类各属性的样本均值与方差 | 连续特征的一般分类 |

Bernoulli 模型与多项式模型的区别在于：前者把"词没有出现"也当作证据（乘以 $1 - \theta_{v,i}$），后者只看出现的词，并计入出现的次数。McCallum 与 Nigam（1998）的比较表明，词表较大时多项式模型通常更好。Gauss 模型中，若各类共用同一组方差，决策边界是线性的，这与 [3.4.10](/3.4.10) 中协方差矩阵为对角阵的线性判别分析一致；为避免方差估计为 $0$，实现中通常给每个方差加一个小的常数。混合类型的属性可以各用合适的分布，再把对数概率相加。

### 3.4.4. 实践要点

**例 3.4.1** 用六封短邮件训练多项式朴素 Bayes 分类器（拉普拉斯平滑），再预测三封新邮件是垃圾邮件的概率。下面先用 NumPy 从头实现，计算全部在对数空间中进行。

```python
import numpy as np

docs = ["win cash now", "cheap pills win", "win a free prize now",
        "meeting at noon", "project meeting notes", "lunch at noon"]
labels = np.array([1, 1, 1, 0, 0, 0])                 # 1 = spam, 0 = ham

vocab = sorted({w for d in docs for w in d.split()})
index = {w: j for j, w in enumerate(vocab)}

def counts(doc):
    x = np.zeros(len(vocab))
    for w in doc.split():
        if w in index:                                # unseen words are ignored
            x[index[w]] += 1
    return x

X = np.array([counts(d) for d in docs])

def fit(X, y, alpha=1.0):
    classes = np.unique(y)
    log_prior = np.log(np.array([np.mean(y == c) for c in classes]))
    n_cw = np.array([X[y == c].sum(axis=0) for c in classes])          # word counts per class
    log_lik = np.log((n_cw + alpha) / (n_cw.sum(axis=1, keepdims=True) + alpha * X.shape[1]))
    return classes, log_prior, log_lik

def predict_log_proba(model, X):
    classes, log_prior, log_lik = model
    joint = X @ log_lik.T + log_prior                 # log P(c) + sum_j x_j log P(w_j | c)
    joint -= joint.max(axis=1, keepdims=True)         # log-sum-exp trick for normalization
    return joint - np.log(np.exp(joint).sum(axis=1, keepdims=True))

model = fit(X, labels)
for doc in ["win a prize", "notes for the meeting", "free lunch"]:
    p_spam = np.exp(predict_log_proba(model, counts(doc)[None, :]))[0, 1]
    print(f"{doc!r:26} P(spam | doc) = {p_spam:.3f}")
```

```text
'win a prize'              P(spam | doc) = 0.926
'notes for the meeting'    P(spam | doc) = 0.124
'free lunch'               P(spam | doc) = 0.458
```

scikit-learn 中同样的模型只需几行，结果相同：

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

docs = ["win cash now", "cheap pills win", "win a free prize now",
        "meeting at noon", "project meeting notes", "lunch at noon"]
labels = [1, 1, 1, 0, 0, 0]
clf = make_pipeline(CountVectorizer(token_pattern=r"\b\w+\b"), MultinomialNB(alpha=1.0))
clf.fit(docs, labels)
print(clf.predict_proba(["win a prize", "notes for the meeting", "free lunch"])[:, 1].round(3))
```

```text
[0.926 0.124 0.458]
```

（Python 3.12，NumPy 2.5，scikit-learn 1.9。）从这个例子可以归纳出使用朴素 Bayes 的几个要点。

1. 用对数概率。一封一千词的邮件，每个词的条件概率约为 $10^{-4}$，乘积约为 $10^{-4000}$，远小于双精度浮点数能表示的最小正数（约 $10^{-308}$），直接相乘会下溢为 $0$。取对数后乘积变为求和：$\log \mathbb{P}(v) + \sum_j x_j \log \mathbb{P}(w_j \mid v)$。只需分类时比较这个和即可；需要归一化的后验概率时，用 log-sum-exp 技巧 $\log\sum_k \mathrm{e}^{s_k} = m + \log\sum_k \mathrm{e}^{s_k - m}$（$m = \max_k s_k$）避免溢出，即上面程序中减去最大值的一步。
2. 必须平滑。没有平滑时，"free lunch"中的 free 从未在正常邮件中出现，会使正常邮件的概率为 $0$。
3. 训练时没见过的词不在词表中，最简单的做法是忽略它（上面程序中的 for、the）。
4. 特征工程比模型更重要（见 §3.5.1）：怎样切分词、是否区分大小写、是否加入二元词组、是否单独处理邮件头，往往比换一个模型影响更大。用 TF-IDF 加权的词频代替原始计数，在多项式模型中也常常有效。
5. 类别先验与阈值。$\mathbb{P}(v)$ 用训练集中的类别比例估计；若部署时的类别比例不同，或者两类错误的代价不同，应当调整先验或判决阈值，而不是只取后验最大的类别。
6. 训练是一次计数，可以增量更新：新邮件到来时只需更新计数，无需重新训练，适合在线的场合。

朴素 Bayes 适合以下情形：属性很多而样本较少（高维稀疏的文本）；需要很快的训练和预测；需要一个简单可靠的基线；数据流式到达。属性之间存在强相关（例如同一个特征重复多次，会被重复计算证据）、需要准确的概率、或者数据充足时，logistic 回归、梯度提升树或神经网络通常更好。

## 3.5. 应用

### 3.5.1. 垃圾邮件过滤

垃圾邮件过滤是朴素 Bayes 最成功的应用之一。1998 年的同一个学术会议上发表了两篇早期论文，作者分别是 Pantel 与 Lin，以及微软研究院的 Sahami 等人。Paul Graham 在 2002–2003 年的文章中报告，他自己实现的贝叶斯过滤器能拦截 $99.5\%$ 的垃圾邮件，假阳性率低于 $0.03\%$，而 Pantel 与 Lin 的方法只拦截 $92\%$，假阳性率为 $1.16\%$。他总结的差别几乎都与数据和特征有关，而不是与模型有关：

- 训练数据太少：只有 160 封垃圾邮件和 466 封正常邮件。
- 忽略了邮件头。邮件头中的发件地址、路由信息和主题行可能是最重要的证据，而且同一个词出现在主题中（`Subject*FREE`）和出现在正文中含义不同，应当作为不同的特征。
- 对词做了词干化，丢掉了有用的区别（`free` 与 `free!!` 的垃圾邮件概率相差很大）。
- 使用全部的词，而 Graham 只用最显著的 15 个词（概率最偏离 $0.5$ 的词）。
- 没有偏向减少假阳性。误删一封正常邮件比漏过一封垃圾邮件代价高得多；Graham 把正常邮件中的词频加倍计算，使过滤器更不愿意判为垃圾邮件。

这些经验与 [4.6.1](/4.6.1#sec-1.3.1) 中的设计问题一一对应：不要武断地丢弃任何信息；两类错误的代价不同，评价时要分开看假阳性与假阴性（[4.6.2](/4.6.2#sec-2.3.2)）。

### 3.5.2. 词义消歧

许多词有多个含义：bank 可以指银行，也可以指河岸；"A fly flies into the kitchen"中的两个 fly 一个是名词"苍蝇"，一个是动词"飞"。根据上下文判断一个词在句中取哪个含义，称为词义消歧。

**定义 3.5.1（词义消歧）** 设词 $w$ 有含义 $s_1, \dots, s_K$，它在一次出现中的上下文 $c$ 是它周围的一组词 $w_1, \dots, w_m$。根据 $c$ 判断 $w$ 在这次出现中取哪个含义的任务，称为**词义消歧**。

用朴素 Bayes 做词义消歧：把含义当作类别，把上下文中的词当作属性，并假定它们在给定含义时条件独立，

$$
s^* = \arg\max_{s_k}\ \Bigl[\log \mathbb{P}(s_k) + \sum_{w_j \in c}\log \mathbb{P}(w_j \mid s_k)\Bigr],
$$
其中 $\mathbb{P}(s_k)$ 与 $\mathbb{P}(w_j \mid s_k)$ 由标注了含义的语料中的计数估计（并作平滑）：$\mathbb{P}(s_k) = C(s_k)/C(w)$，$\mathbb{P}(w_j \mid s_k) = C(w_j, s_k)/C(s_k)$，$C$ 表示计数。bank 的上下文中出现 money、loan、account 时倾向于"银行"，出现 river、water、fishing 时倾向于"河岸"。Gale、Church 与 Yarowsky（1992）用这种方法取得了当时很好的结果。今天的做法是用预训练语言模型给出的上下文相关的词表示（[4.7](/4.7)），同一个词在不同上下文中的表示本身就不同，消歧的准确率远高于朴素 Bayes；但后者仍是理解这个问题的最好起点。

## 小结

| 概念 | 公式 | 要点 |
|---|---|---|
| 后验 | $\mathbb{P}(h \mid D) \propto \mathbb{P}(D \mid h)\,\mathbb{P}(h)$ | 先验很小时，强证据下的后验也可能很小 |
| MAP 假设 | $\arg\max_h \mathbb{P}(D \mid h)\,\mathbb{P}(h)$ | $-\log$ 先验就是正则项 |
| ML 假设 | $\arg\max_h \mathbb{P}(D \mid h)$ | 正态噪声下等价于最小二乘 |
| Bayes 最优分类器 | $\arg\max_v \sum_h \mathbb{P}(v \mid x, h)\,\mathbb{P}(h \mid D)$ | 平均意义下最优，计算困难 |
| Gibbs 算法 | 按后验抽一个 $h$ 来分类 | 期望错误率至多两倍 |
| 朴素 Bayes | $\arg\max_v \mathbb{P}(v)\prod_i \mathbb{P}(a_i \mid v)$ | 条件独立；对数概率；拉普拉斯平滑 = Dirichlet 先验下的后验均值 |
