---
title: 无监督学习与聚类
description: 无监督学习的任务；聚类的目标与各类数据的相似度；k 均值的初始化（k-means++）与大规模改进（mini-batch）；k 中心聚类（PAM、CLARA、CLARANS）；分裂式层次聚类；聚类数目的选择与评价；DBSCAN。
---

前面几章的学习都有"老师"：每个训练样例都带着类别或目标值。本章转向没有标注的数据，讨论其中最基本的任务：聚类，即把相似的对象归为一组。聚类的统计理论已在 [3.4.11](/3.4.11) 讲过，那里给出了**层次聚类**、**k 均值聚类**及其目标函数与收敛性、**轮廓系数**，以及用 **EM 算法**拟合的**高斯混合模型**；本章只简述这些内容，重点补充机器学习中常用而统计学课程没有展开的部分：各类数据的相似度、k 均值的初始化与面向大规模数据的改进、以中心点代表类的 k 中心聚类（PAM、CLARA、CLARANS）、分裂式层次聚类、聚类的评价，以及能发现任意形状类的密度聚类 DBSCAN。距离度量沿用 [4.6.4](/4.6.4) 基于实例的学习。

## 5.1. 无监督学习

**有监督学习**从带标注的样例 $(x_i, y_i)$ 中学习，关心的是条件分布 $P(Y \mid X)$：$X$ 是用特征表示的样例，通常很复杂；$Y$ 是类别或目标值，相对简单。**无监督学习**只有样例 $x_1, \dots, x_n$ 而没有标注，关心的是 $X$ 本身的联合分布 $P(X) = P(X_1, \dots, X_d)$，即数据自身的结构。介于两者之间的是半监督学习（semi-supervised learning）：用少量有标注的数据和大量无标注的数据共同学习 $P(Y \mid X)$；标注昂贵而无标注数据廉价时（医学影像、语音、网页），它很有用。

数据的结构本身蕴含大量信息：把一张照片的像素位置随机打乱，每个像素的颜色值都没有变，图像却变得毫无意义。无标注数据可以用来做以下几件事：

| 任务 | 做什么 | 例子 |
|---|---|---|
| 聚类 | 在没有预先定义的类别时，把数据分成若干组 | 客户分群、新闻聚合 |
| 降维 | 减少需要考虑的变量个数 | **主成分分析**（[3.4.5](/3.4.5)）、**多维标度**（[3.4.6](/3.4.6)） |
| 离群点检测 | 识别错误、噪声，或训练中没有见过的新信号 | 欺诈检测、设备故障 |
| 密度估计 | 刻画数据的分布 | **核密度估计**、**高斯混合模型** |
| 表示学习 | 发现数据中隐含的规律，作为后续任务的特征 | 自监督预训练（[4.7.7](/4.7.7)） |

## 5.2. 聚类与相似度

### 5.2.1. 聚类的目标

**聚类**把相似的对象归入同一个类（簇，cluster），使同一类中的对象彼此相似，不同类中的对象差异明显，即"物以类聚，人以群分"。好的聚类类内距离小、类间距离大。因此核心问题是相似度的定义：对象之间的相似度，以及（有时需要的）类与类之间的相似度。一个聚类方法由三部分组成：无标注的数据、相似度或距离度量、聚类算法。

聚类结果按两个维度分类：

- **硬聚类**中每个对象只属于一个类；**软聚类**中一个对象可以以不同程度属于多个类（如高斯混合模型给出的后验概率）。
- 层次聚类给出类的一棵树（**树状图**），可以在不同粒度上解释数据；非层次聚类（**划分聚类**）只给出一层平的划分。

聚类的应用很广：生物学中把同源序列归入基因家族、用基因数据推断种群结构；图像处理中按人物自动整理相册；商业中发现不同的客户群体；网络中聚合同一事件的新闻、从访问日志中发现相似的用户与访问模式。

### 5.2.2. 数据类型与相似度

样例是向量 $x \in D_1 \times D_2 \times \cdots \times D_d$，每个分量的取值域可以是：

| 类型 | 取值域 | 例子 |
|---|---|---|
| 实数 | $D = \mathbb{R}$ | 身高、温度 |
| 二值 | $D = \{v_1, v_2\}$ | 性别 |
| 名义（无序） | $D = \{v_1, \dots, v_M\}$ | 星期几、城市 |
| 有序 | $D \subseteq \mathbb{R}$ 或有序的 $\{v_1, \dots, v_M\}$ | 排名、"小、中、大" |

相似度与距离反向变化，常用 $\operatorname{sim} = 1/(1 + d)$ 或 $\operatorname{sim} = \mathrm{e}^{-d}$ 互相转换。

1. 实数值数据：内积 $\langle x, y\rangle$、**余弦相似度**、基于核函数的相似度 $\exp(-\|x - y\|^2 / 2\sigma^2)$；距离用 [4.6.4](/4.6.4) 中的 Minkowski 距离 $\big(\sum_j \lvert x_j - y_j\rvert^p\big)^{1/p}$，$p = 1, 2, \infty$ 分别是 Manhattan、Euclid 与 Chebyshev 距离。各分量量纲不同时先标准化，分量相关时可用**马氏距离**。
2. 二值与名义数据：最简单的是"相同为 1、不同为 0"，$\operatorname{sim}(x_j, y_j) = \boldsymbol{1}\{x_j = y_j\}$，对所有分量平均即简单匹配系数；稀疏的二值数据（购物篮、文档中出现的词）常用 Jaccard 系数 $\lvert A \cap B\rvert / \lvert A \cup B\rvert$，它忽略两者都为 0 的分量。也可以借助取值的语义属性，例如用两座城市之间的地理距离或人口规模之差定义城市的相似度；或者直接给出一个相似度矩阵。
3. 有序数据：把取值按顺序归一化到 $[0, 1]$（最小值为 0，最大值为 1，其余等距插值，如"小、中、大、特大"为 $0, 0.33, 0.67, 1$），再用实数值的度量；也可以用相似度矩阵。

**例 5.2.1** 尺寸等级的相似度矩阵（只写上三角）：

| | Tiny | Little | Small | Medium | Large | Huge |
|---|---|---|---|---|---|---|
| Tiny | 1.0 | 0.8 | 0.7 | 0.5 | 0.2 | 0.0 |
| Little | | 1.0 | 0.9 | 0.7 | 0.3 | 0.1 |
| Small | | | 1.0 | 0.7 | 0.3 | 0.2 |
| Medium | | | | 1.0 | 0.5 | 0.3 |
| Large | | | | | 1.0 | 0.8 |
| Huge | | | | | | 1.0 |

相似度矩阵应当对称、对角线为 1，但不需要线性插值的假设：Little 与 Small 的相似度（0.9）可以远高于 Medium 与 Large（0.5），这是等距归一化做不到的。

不同类型的分量混在一起时，可以对每个分量分别按上述方法算出 $[0,1]$ 中的相似度，再加权平均（Gower 系数）。

## 5.3. k 均值聚类

### 5.3.1. 算法与收敛性

**k 均值聚类**（[3.4.11](/3.4.11#alg-11.3.1)）交替执行两步：给定类的分配，把每类的中心更新为该类对象的均值 $g_1, \dots, g_k$；给定中心，把每个对象分配给最近的中心。用二值指示变量 $r_{iv} \in \{0, 1\}$ 表示对象 $u_i$ 是否属于类 $v$（每个 $i$ 恰有一个 $r_{iv} = 1$），算法最小化

$$
J(r, g) = \sum_{i=1}^n \sum_{v=1}^k r_{iv}\,\|u_i - g_v\|^2 .
$$
分配步固定 $g$ 对 $r$ 最小化 $J$，更新步固定 $r$ 对 $g$ 最小化 $J$（最优解就是类均值），所以 $J$ 单调不增；划分只有有限多个，算法在有限步内收敛，但只保证到达局部极小（[3.4.11](/3.4.11#prop-11.3.1)）。求 $J$ 的全局极小是 NP 难的，即使在平面上也是如此。k 均值的特点可以概括为：向量空间模型，最小化类内欧氏距离平方和，迭代求解，硬聚类，非层次。

每次迭代的代价是 $O(nkd)$（$d$ 是维数）。k 均值也用于聚类以外的任务，例如图像压缩（颜色量化）：把所有像素的 $(R, G, B)$ 值（不含位置）聚成 $k$ 类，每个像素改用所属类中心的颜色重画，图像就只需要 $k$ 种颜色。

### 5.3.2. 初始化：k-means++

k 均值的结果强烈依赖初始中心。随机选 $k$ 个对象作初始中心时，可能有两个中心落在同一个真实的类里，算法从此陷入很差的局部极小；要求初始种子两两距离大于某个阈值 $d_{\min}$ 是一种朴素的补救。Arthur 与 Vassilvitskii（2007）提出的 k-means++ 按距离的平方随机播种，既分散又不被离群点左右：

**算法 5.3.1（k-means++）** 设 $D(u)$ 是对象 $u$ 到已选中心中最近者的距离。

1. 从数据中均匀随机地选出第一个中心；
2. 以概率 $D(u)^2 / \sum_{u'} D(u')^2$ 选出下一个中心 $u$；
3. 重复第 2 步直到选出 $k$ 个中心，再运行通常的 k 均值迭代。

可以证明，k-means++ 播种得到的目标值在期望意义下满足 $\mathbb{E}[J] \le 8(\ln k + 2)\,J_{\mathrm{opt}}$，播种本身就已是 $O(\log k)$ 近似。它是 scikit-learn 中 `KMeans` 的默认初始化；实践中仍从多组初值出发运行（`n_init`），保留 $J$ 最小的结果。

### 5.3.3. 大规模数据

数据量很大时，每次迭代都要扫描全部 $n$ 个对象。常用的改进有：

- Mini-batch k 均值（Sculley，2010）：每步只取一个随机小批量 $B$（如 1024 个对象），把其中每个对象 $u$ 分给最近的中心 $g$，记该中心累计分到的对象数为 $v_g$，再以学习率 $\eta = 1/v_g$ 更新 $g \leftarrow (1 - \eta)\,g + \eta\,u$。这相当于对 $J$ 做**随机梯度下降**，与**小批量梯度下降**同理；每步代价与 $n$ 无关，目标值通常只比完整的 k 均值略差。
- 利用**三角不等式**跳过不必要的距离计算（Elkan，2003）：若 $d(g, g') \ge 2\,d(u, g)$，则 $g'$ 不可能比 $g$ 更近，结果与原算法完全相同而快得多。
- 先在随机样本上聚类，再把其余对象分给最近的中心；这一思路也用于下面的 CLARA。

### 5.3.4. 局限

k 均值在数据呈几团紧凑且彼此分离的"云"时效果很好；它隐含地寻找大小与散布相近的球形类，所以对非凸形状的类、大小或密度相差悬殊的类效果不好，并且对噪声与离群点非常敏感：一个远离所有类的点就能把某个类均值拉偏。下面两节分别处理这两个问题：k 中心聚类提高对离群点的稳健性，DBSCAN 处理任意形状的类。

## 5.4. k 中心聚类

### 5.4.1. 中心点

均值容易被离群点拉偏，而且只对向量数据有意义。k 中心聚类用类中的一个实际对象代表这个类。

**定义 5.4.1（k 中心聚类）** 给定 $n$ 个对象及任意的相异度 $d$，类 $C$ 的**中心点**（medoid）是 $C$ 中使 $\sum_{u \in C} d(u, m)$ 最小的对象 $m$。**k 中心聚类**选出 $k$ 个对象 $m_1, \dots, m_k$ 作为中心点，把每个对象分给最近的中心点，以最小化总代价

$$
\operatorname{cost}(m_1, \dots, m_k) = \sum_{i=1}^n \min_{1 \le v \le k} d(u_i, m_v).
$$

与 k 均值相比，k 中心聚类有三个好处：中心总是真实的对象，便于解释；只需要相异度矩阵，可以用于名义数据、字符串、图上的对象等任何能定义相异度的场合；代价是距离之和而不是距离平方之和，离群点的影响小得多。最朴素的算法照搬 k 均值的交替：随机选 $k$ 个代表对象，把其他对象分给最近的代表，再在每个类里重新选使代价最小的对象作中心，重复到不再变化。这种交替很快，但容易停在差的局部极小。

### 5.4.2. PAM

**算法 5.4.1（PAM）** PAM（Partitioning Around Medoids；Kaufman 与 Rousseeuw，1987）分两个阶段。

1. BUILD：先选使总代价最小的一个对象，再逐个贪心地加入使总代价下降最多的对象，直到有 $k$ 个中心点。
2. SWAP：对每一对（中心点 $m$，非中心点 $h$），计算用 $h$ 替换 $m$ 后的总代价；若最好的替换能降低代价就执行它，然后重复，直到没有任何替换能降低代价。

课件中的版本是 SWAP 的随机化：每次随机选一个非中心点 $O_{\mathrm{random}}$ 与某个中心点交换，代价降低就保留交换，否则不交换。例如在一个 $k = 2$ 的例子中，以 Manhattan 距离计算的当前总代价为 20，随机交换后总代价为 26，于是不交换。

SWAP 阶段停止时的划分是"交换一个中心点不能再改进"的局部最优；只有穷举所有 $\binom{n}{k}$ 种中心点组合才能保证全局最优。朴素实现中每轮要评估 $k(n-k)$ 个交换，每个交换要 $O(n-k)$ 的时间重新计算代价，合计 $O(k(n-k)^2)$，比 k 均值慢得多，所以原始的 PAM 只适合小数据集。Schubert 与 Rousseeuw（2021）的 FastPAM 通过共享计算把每轮代价降低约 $k$ 倍，结果不变。

下面是一个 PAM 的直接实现。数据是两团各 20 个点，外加一个远处的离群点：

```python
import numpy as np


def pam(D, k, max_iter=100):
    """PAM (BUILD + SWAP) on a precomputed dissimilarity matrix D."""
    n = D.shape[0]
    # BUILD: greedily add the medoid that lowers the total cost most
    medoids = [int(np.argmin(D.sum(axis=1)))]
    while len(medoids) < k:
        nearest = D[:, medoids].min(axis=1)
        gains = [np.maximum(nearest - D[:, c], 0).sum() if c not in medoids else -1
                 for c in range(n)]
        medoids.append(int(np.argmax(gains)))
    cost = D[:, medoids].min(axis=1).sum()
    # SWAP: try every (medoid, non-medoid) pair, apply the best improving swap
    for _ in range(max_iter):
        best = (cost, None, None)
        for i in range(k):
            for h in range(n):
                if h in medoids:
                    continue
                trial = medoids[:i] + [h] + medoids[i + 1:]
                c = D[:, trial].min(axis=1).sum()
                if c < best[0]:
                    best = (c, i, h)
        if best[1] is None:
            break
        cost, i, h = best
        medoids[i] = h
    labels = D[:, medoids].argmin(axis=1)
    return medoids, labels, cost


rng = np.random.default_rng(0)
X = np.vstack([rng.normal([0, 0], 0.5, (20, 2)),
               rng.normal([4, 4], 0.5, (20, 2)),
               [[30.0, 30.0]]])                      # one gross outlier
D = np.abs(X[:, None, :] - X[None, :, :]).sum(axis=2)  # Manhattan distance
medoids, labels, cost = pam(D, k=2)
print("medoids:", X[medoids].round(2).tolist())
print("cluster sizes:", np.bincount(labels).tolist(), "total cost:", round(cost, 2))

# k-means (Lloyd) on the same data for comparison
centers = X[[0, 20]].copy()
for _ in range(100):
    lab = ((X[:, None, :] - centers) ** 2).sum(axis=2).argmin(axis=1)
    centers = np.array([X[lab == j].mean(axis=0) for j in range(2)])
print("k-means centers:", centers.round(2).tolist())
```

```text
medoids: [[4.21, 4.35], [-0.23, 0.11]]
cluster sizes: [21, 20] total cost: 81.32
k-means centers: [[-0.14, 0.07], [5.43, 5.33]]
```

离群点被分到右上的类，但中心点仍在 $(4, 4)$ 附近；k 均值的类均值则被它拉到了 $(5.4, 5.3)$。

### 5.4.3. CLARA 与 CLARANS

**算法 5.4.2（CLARA）** CLARA（Clustering LARge Applications；Kaufman 与 Rousseeuw，1990）面向大样本：

1. 从数据中随机抽取一个小样本（原作者建议 $40 + 2k$ 个对象），在样本上运行 PAM 得到 $k$ 个中心点；
2. 把全部对象分给最近的中心点，计算在全部数据上的总代价；
3. 重复抽样若干次（如 5 次），取总代价最小的一组中心点作为结果。

CLARA 每次的代价与 $n$ 成线性关系，但最优的中心点若没有被抽进任何样本，就不可能被找到。CLARANS（Ng 与 Han，1994）不固定样本，而在"所有 $k$ 个中心点组合"构成的图上做随机局部搜索：两个组合只差一个中心点时相邻；从一个组合出发，随机检查至多 `maxneighbor` 个邻居，遇到代价更低的就移动过去，没有就认为到达局部极小；重复 `numlocal` 次取最好的结果。它比 CLARA 更灵活，通常也更准确。

## 5.5. 层次聚类

### 5.5.1. 凝聚式

凝聚式（自底向上）层次聚类已在 [3.4.11](/3.4.11#alg-11.2.1) 详细讨论：每个对象先自成一类，反复合并最相似的两类 $c_i, c_j$，用 $c_i \cup c_j$ 代替它们并重新计算新类与其他类的相似度，直到只剩 $k$ 类（$k$ 可以为 1）。类间相似度由连接方式决定：**单连接**取两类中最相似的一对点，**全连接**取最不相似的一对点，**平均连接**取所有点对相似度的平均。合并的过程记录为树状图，在不同高度切开就得到不同粒度的聚类。

一个经典的例子是用欧氏距离和单连接对意大利六座城市（都灵、米兰、佛罗伦萨、罗马、那不勒斯、巴里）聚类：每一轮在距离矩阵中找出最近的两类合并，再按单连接更新距离矩阵（新类到其他类的距离取两个旧类距离的较小者），矩阵每轮缩小一行一列，五轮之后得到完整的树状图。

层次聚类在科学数据分析中很常用。例如 Mesgarani 等（2014）记录了癫痫患者颞上回各电极对不同英语音素的反应，对电极与音素分别做层次聚类，发现音素首先分成阻塞音与响音两大组，再按发音方式细分，电极也相应地分组：听觉皮层对语音的编码以发音特征为单位。

### 5.5.2. 分裂式

分裂式（自顶向下）层次聚类从包含全部对象的一个类出发，每次把一个类一分为二。最常用的是 DIANA（DIvisive ANAlysis；Kaufman 与 Rousseeuw，1990）：

**算法 5.5.1（DIANA）** 重复以下步骤，直到每类只含一个对象（或已有 $k$ 类）：

1. 选出直径（类内最大相异度）最大的类 $C$；
2. 在 $C$ 中找出到其他对象平均相异度最大的对象，让它单独组成"分裂组"（splinter group），$C$ 中其余对象组成"原组"；
3. 对原组中的每个对象 $u$，计算它到原组其他对象的平均相异度与到分裂组的平均相异度之差；若最大的差为正，把对应的对象移入分裂组，重复这一步，直到没有对象更接近分裂组；
4. 用分裂组与原组代替 $C$。

两种方式的比较：

| | 分裂式 | 凝聚式 |
|---|---|---|
| 所用信息 | 每次分裂都能利用整个类的全局信息 | 每次合并只看两类之间的局部信息 |
| 粒度 | 可以只做最上面几层的粗分 | 必须一直合并到最后才得到顶层结构 |
| 实现 | 寻找最佳分裂点较复杂，常借助划分聚类（如每次做 $k = 2$ 的 k 均值，即二分 k 均值） | 合并相近的类简单，不需要其他算法 |
| 错误能否纠正 | 一旦分开不会再合并 | 一旦合并不会再分开 |

层次聚类可以从不同粒度观察数据，适用于各种相似度定义，因而适用于各种属性类型；缺点是停止条件（在哪里切开树状图）不确定，计算开销大（凝聚式需要 $O(n^2)$ 的内存和至少 $O(n^2)$ 的时间），很难直接用于大数据集。

## 5.6. 聚类数目与聚类质量

### 5.6.1. 选择聚类数目

聚类数目 $k$ 最好由问题本身决定：例如服装按 S、M、L 三个尺码分组，就取 $k = 3$。只有在数据不稀疏、各维度没有明显噪声时，才适合完全由数据决定 $k$。数据驱动的方法都考察类内不相似度 $W_k$（如 k 均值的目标 $J$）随 $k$ 的变化；$W_k$ 随 $k$ 增大而单调下降，$k = n$ 时为 0，所以不能直接取最小值。

- **肘部法则**：$W_k$ 在真实的类数之前急剧下降，之后变化平缓，取曲线的拐点。
- **间隙统计量**：在不含聚类结构的参照数据（如数据范围内的均匀分布）上用同一算法聚类，比较 $\ln W_k$ 与参照数据上的期望值之间的间隔，取间隔大的 $k$。
- **轮廓系数**：取使全部对象平均轮廓系数最大的 $k$。它只依赖相异度，所以也适用于 k 中心聚类和层次聚类。
- 基于模型的聚类用 BIC 等信息准则选择 $k$（[3.4.11](/3.4.11#def-11.4.2)）。

![在四团数据上选择 k：左为数据；中为 k 均值的类内平方和 W_k，在 k = 4 处出现肘部；右为平均轮廓系数，在 k = 4 处最大](./plots/choose-k.py)

### 5.6.2. 评价聚类结果

评价聚类比评价分类难，因为通常没有正确答案。评价指标分为两类：

- 内部指标只用数据本身：类内平方和、平均轮廓系数、Davies–Bouldin 指数（越小越好）、Calinski–Harabasz 指数（类间与类内散布之比，越大越好）。它们大多偏爱凸的、球形的类。
- 外部指标把聚类结果与已知的类别比较（用于在有标注的数据上评价算法）：纯度、调整 Rand 指数（ARI，两个划分完全一致时为 1，随机划分的期望为 0，与类的编号无关）、归一化互信息（NMI）。

最终还要回到应用：聚类可能给出"意外"的结果，如各类大小严重不平衡、与人的传统认知不符、难以解释。这些结果不一定是错的，但需要结合领域知识检查数据预处理、相似度与算法的选择。

## 5.7. 基于密度的聚类：DBSCAN

k 均值和 k 中心聚类都把类看成围绕中心的一团，无法发现环形、月牙形等任意形状的类，也会把每个噪声点强行分进某个类。基于密度的方法把类看成被低密度区域隔开的高密度区域。

**定义 5.7.1（DBSCAN）** 给定半径 $\varepsilon > 0$ 与整数 $\mathrm{minPts}$，对象 $p$ 的 $\varepsilon$ 邻域是 $N_\varepsilon(p) = \{q : d(p, q) \le \varepsilon\}$（含 $p$ 自身）。**DBSCAN**（Density-Based Spatial Clustering of Applications with Noise；Ester 等，1996）把一个类定义为由某个核心点密度可达的全部对象；类中不是核心点的对象称为**边界点**，不属于任何类的对象称为**噪声点**。其中：

- 若 $\lvert N_\varepsilon(p)\rvert \ge \mathrm{minPts}$，称 $p$ 为**核心点**；
- 若 $q \in N_\varepsilon(p)$ 且 $p$ 是核心点，称 $q$ 由 $p$ **直接密度可达**；若存在一串对象 $p = p_1, p_2, \dots, p_m = q$，每一个都由前一个直接密度可达，称 $q$ 由 $p$ **密度可达**；
- 若 $p, q$ 都由某个对象 $o$ 密度可达，称 $p, q$ **密度相连**。同一个类中的任意两个对象都是密度相连的。

算法很简单：依次取一个尚未归类的核心点，从它出发做图搜索（广度或深度优先），把所有密度可达的对象归入一个新类；所有核心点处理完后，剩下的对象就是噪声。DBSCAN 不需要指定类的个数，能发现任意形状的类，并能识别噪声；结果除了边界点可能同时与两个类相邻外，与处理对象的顺序无关。主要的计算是邻域查询，借助 **kd 树**等空间索引在低维数据上很快，最坏情况为 $O(n^2)$。

参数的经验选择：$\mathrm{minPts}$ 至少取维数加一，二维数据常取 4 或 5；$\varepsilon$ 可以从 $k$ 距离图中读出：把每个对象到第 $\mathrm{minPts} - 1$ 个近邻的距离从大到小排序作图，取曲线明显拐弯处的值。DBSCAN 的主要弱点是只有一个全局的密度阈值，当各类密度相差很大时，没有一个 $\varepsilon$ 能同时适合所有的类；HDBSCAN（Campello 等，2013）在所有 $\varepsilon$ 上构造密度的层次结构，再从中选出最稳定的类，缓解了这个问题，scikit-learn 1.3 起也提供了它。

![两个交错的半月形加上背景噪声。左：k 均值（k = 2）沿一条直线把数据切成两半；右：DBSCAN 找出了两个月牙（实心为核心点，空心为边界点），并把散落的点标为噪声（叉号）](./plots/kmeans-vs-dbscan.py)

## 5.8. 实践

scikit-learn 中的聚类算法有统一的接口：`fit` 之后从 `labels_` 读出类标号（DBSCAN 用 $-1$ 表示噪声）。下面的例子用肘部法则与轮廓系数选择 $k$，比较 mini-batch 与完整的 k 均值，并在月牙形数据上比较 k 均值与 DBSCAN：

```python
import numpy as np
from sklearn.cluster import DBSCAN, KMeans, MiniBatchKMeans
from sklearn.datasets import make_blobs, make_moons
from sklearn.metrics import adjusted_rand_score, silhouette_score

# choose k for k-means by inertia (elbow) and silhouette
X, y = make_blobs(n_samples=600, centers=4, cluster_std=1.0, random_state=0)
for k in range(2, 7):
    km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
    print(f"k={k}  inertia={km.inertia_:8.1f}  silhouette={silhouette_score(X, km.labels_):.3f}")

# mini-batch k-means on a large data set
Xbig, _ = make_blobs(n_samples=200_000, centers=4, random_state=0)
mbk = MiniBatchKMeans(n_clusters=4, batch_size=1024, n_init=3, random_state=0).fit(Xbig)
km = KMeans(n_clusters=4, n_init=3, random_state=0).fit(Xbig)
print(f"inertia: mini-batch {mbk.inertia_:.0f}, full {km.inertia_:.0f}")

# non-convex clusters: k-means vs DBSCAN
Xm, ym = make_moons(n_samples=400, noise=0.06, random_state=0)
km_labels = KMeans(n_clusters=2, n_init=10, random_state=0).fit_predict(Xm)
db_labels = DBSCAN(eps=0.2, min_samples=5).fit_predict(Xm)
print("ARI k-means:", round(adjusted_rand_score(ym, km_labels), 3))
print("ARI DBSCAN: ", round(adjusted_rand_score(ym, db_labels), 3),
      "clusters:", len(set(db_labels) - {-1}), "noise points:", int((db_labels == -1).sum()))
```

```text
k=2  inertia=  2922.1  silhouette=0.463
k=3  inertia=  1682.3  silhouette=0.467
k=4  inertia=  1043.8  silhouette=0.500
k=5  inertia=   918.9  silhouette=0.436
k=6  inertia=   809.7  silhouette=0.402
inertia: mini-batch 358349, full 358327
ARI k-means: 0.274
ARI DBSCAN:  1.0 clusters: 2 noise points: 0
```

类内平方和（`inertia_`）在 $k = 4$ 之后下降变缓，轮廓系数在 $k = 4$ 处最大，两者都指向真实的类数。在 20 万个点上，mini-batch k 均值的目标值与完整算法只差不到万分之一。在月牙形数据上，k 均值的 ARI 只有 0.27，DBSCAN 则完全恢复了两个类。

## 小结

| 方法 | 类的代表 | 需要的输入 | 类的形状 | 对离群点 | 规模 |
|---|---|---|---|---|---|
| k 均值 | 均值 | 向量、$k$ | 凸、球形、大小相近 | 敏感 | 大（mini-batch 更大） |
| k 中心（PAM） | 中心点（真实对象） | 任意相异度、$k$ | 凸 | 稳健 | 小；CLARA、CLARANS 用于大数据 |
| 层次聚类 | 树状图 | 任意相异度、连接方式 | 取决于连接方式 | 单连接敏感 | 小（$O(n^2)$） |
| DBSCAN | 密度相连的区域 | 相异度、$\varepsilon$、$\mathrm{minPts}$ | 任意 | 标为噪声 | 中到大（借助空间索引） |
| 高斯混合（EM） | 概率模型 | 向量、$k$ | 椭球形，软聚类 | 敏感 | 中 |

聚类的结果取决于相似度、算法与聚类数目三个选择，没有放之四海而皆准的答案：先根据数据类型确定相似度，根据类的形状与噪声选择算法，再用内部指标、外部指标和领域知识检查结果。
