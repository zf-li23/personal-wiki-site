---
title: 基于实例的学习
description: 参数化与非参数化方法；基于实例的（惰性）学习；最近邻规则、Voronoi 图与 Cover–Hart 界；k 近邻的距离度量、属性归一化与加权、k 的选择与打破平局；维数灾难；kd 树的最近邻查询与近似最近邻搜索（LSH、HNSW、IVF-PQ、FAISS）；距离加权 k 近邻、核回归与局部加权回归。
---

前面几章的方法都遵循"三步走"：估计问题的特性，作出模型假设（线性函数、正态噪声、条件独立……），再找出最优的参数。本章介绍一种不走这条路的方法：不建立显式的模型，只把训练样例存下来，等到要预测新样例时，找出与它最相似的训练样例，用它们的输出作答。这就是"近朱者赤，近墨者黑"：思考即回忆与类比。最典型的方法是 $k$ 近邻，它在统计学的多元分析中已经出现过（[3.4.12](/3.4.12)）；本章系统地讨论它的各个设计选择——距离、属性的处理、$k$ 的选择——以及它的两个根本困难：高维空间中距离失去意义（维数灾难），以及预测时的计算开销。后者引出 kd 树（[4.3.7](/4.3.7)）与今天支撑向量检索的近似最近邻搜索。最后把"按距离加权"的思想推广到回归，得到核回归与局部加权回归，它们是统计学中非参数回归（[3.3.12](/3.3.12)，将在[非参数统计](/3.6)中系统讨论）的机器学习视角。

## 4.1. 基本概念

### 4.1.1. 参数化与非参数化

参数化方法设定一个特定的函数形式（如线性函数），学习就是估计其中有限个参数。它简单，容易估计和解释，但若真实的数据分布不符合所设的形式，就会有很大的偏差。非参数化方法对函数形式的假定少得多，估计由数据驱动；模型的复杂度随数据量增长，代价是需要更多的数据和计算。基于实例的学习是最典型的非参数化方法。

### 4.1.2. 基于实例的学习

**定义 4.1.1（基于实例的学习）** 训练时只存储训练样例，不构造对目标函数的全局近似；每当有新样例需要预测时，才检索与它相似的已存样例，并由它们局部地给出预测。这类方法称为**基于实例的学习**；由于把计算推迟到查询时，它又称为**惰性学习**。

它也称为基于记忆的学习、基于样例的学习、基于相似度的学习，在推理的语境中称为基于样例的推理。与惰性学习相对，线性回归、朴素 Bayes、神经网络等在训练时就构造好全局模型，称为急切学习。

在基于实例的观点下，一个概念 $c$ 可以由三样东西表示：一组样例 $\{e_1, e_2, \dots\}$，一个相似度函数 $f$，一个阈值 $\theta$。实例 $a$ 属于 $c$，当且仅当它与 $c$ 中的某个样例 $e_j$ 足够相似：$f(e_j, a) > \theta$。"找出与这张图片最相似的十张图片""找出两个基因组之间所有相似的基因片段"都是这类问题。

## 4.2. 最近邻与 k 近邻

### 4.2.1. 最近邻规则

相似度与距离相对应：距离越小越相似。最简单的规则是把新样例 $\boldsymbol{x}_q$ 判为离它最近的训练样例的类别，称为最近邻规则（1-NN）。

**例 4.2.1** 用两个特征评估信用：$L$ 为每年延迟还款的次数，$R$ 为收入与支出之比。已知 8 位客户的评级（G 为好，P 为差）：

| 客户 | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| $L$ | 0 | 25 | 5 | 20 | 30 | 11 | 7 | 15 |
| $R$ | 1.2 | 0.4 | 0.7 | 0.8 | 0.85 | 1.2 | 1.15 | 0.8 |
| 评级 | G | P | G | P | P | G | G | P |

新客户 I $(6, 1.15)$、J $(22, 0.45)$、K $(15, 1.2)$ 的评级如何？直接用欧氏距离，I 的最近邻是 G（距离 $1.0$），判为好；J 的最近邻是 D（距离约 $2.03$），判为差；K 的最近邻是 H（距离 $0.4$），判为差。但 $L$ 的取值范围（$0$ 到 $30$）比 $R$（$0.4$ 到 $1.2$）大得多，距离几乎完全由 $L$ 决定。把两个特征都按取值范围缩放到 $[0,1]$ 后，I 的最近邻仍是 G，J 的最近邻变为 B（仍判为差），而 K 的最近邻变为 F（距离约 $0.13$），判为好：K 的延迟次数中等，收支比却和好客户一样高。距离的定义直接决定答案，§4.2.4 再讨论。

**定义 4.2.1（Voronoi 图）** 设 $S = \{\boldsymbol{x}_1, \dots, \boldsymbol{x}_n\}$ 是欧氏空间中的有限点集。$\boldsymbol{x}_i$ 的 Voronoi 胞腔是比 $S$ 中任何其他点都更靠近 $\boldsymbol{x}_i$ 的点的集合，$\{\boldsymbol{x}\colon d(\boldsymbol{x}, \boldsymbol{x}_i) \le d(\boldsymbol{x}, \boldsymbol{x}_j)\ \forall j\}$；全部胞腔构成空间的一个剖分，称为 $S$ 的 **Voronoi 图**。

1-NN 的决策区域就是训练样例的 Voronoi 图：每个胞腔中的点都被判为该胞腔中心的类别，决策边界由不同类别的样例之间的胞腔边界组成。几乎所有的点都恰有一个最近的样例；胞腔边界上的点与两个或多个样例等距，这些点构成零测集。

最近邻规则如此简单，它的渐近表现却有一个漂亮的界。记 $R^*$ 为**贝叶斯分类器**的错误率，即**最优误判率**（[3.4.10](/3.4.10)），它是任何分类器都不可能低于的错误率。

**定理 4.2.1（Cover–Hart）** 设共有 $c$ 个类别，训练样例数 $n \to \infty$。在适当的正则条件下，1-NN 的渐近错误率 $R$ 满足

$$
R^* \le R \le R^*\Bigl(2 - \frac{c}{c-1}R^*\Bigr) \le 2R^*.
$$

证明较长（见 Duda、Hart 与 Stork 的《模式分类》）。直观地说：样例足够密时，$\boldsymbol{x}_q$ 的最近邻几乎与 $\boldsymbol{x}_q$ 重合，它的类别相当于从 $\boldsymbol{x}_q$ 处的类别后验分布中独立抽取的一个样本；1-NN 出错，当且仅当 $\boldsymbol{x}_q$ 自己的类别与这个独立样本不同。这与 [4.6.3](/4.6.3#sec-3.3.2) 中 Gibbs 算法"按后验抽样"的错误率至多两倍是同一类结论。所以在无穷多的数据下，即使最简单的最近邻规则，错误率也不超过最优值的两倍——可以说，任何分类问题中一半的信息都包含在最近的那个邻居里。但这只是渐近的结论：有限样本、高维空间中，最近邻可能离得很远（§4.3）。

### 4.2.2. k 近邻

如果最近的那个邻居恰好是噪声呢？自然的办法是看不止一个邻居，让它们投票。

**算法 4.2.1（k 近邻）** 给定训练样例 $(\boldsymbol{x}_i, y_i)$、距离 $d$ 与正整数 $k$。对查询 $\boldsymbol{x}_q$，找出离它最近的 $k$ 个训练样例 $\boldsymbol{x}_{(1)}, \dots, \boldsymbol{x}_{(k)}$：

- 分类：输出它们中出现最多的类别，$\hat y_q = \arg\max_{v}\sum_{j=1}^k \boldsymbol{1}(y_{(j)} = v)$；
- 回归：输出它们的平均值，$\hat y_q = \frac{1}{k}\sum_{j=1}^k y_{(j)}$。

这就是 **k 近邻**（KNN）。$k = 1$ 时就是最近邻规则。

**例 4.2.2** 根据年龄、收入（千元）与持有的信用卡数，预测客户 David 是否会响应一项推销：

| 客户 | 年龄 | 收入 | 卡数 | 响应 | 到 David 的距离 |
|---|---|---|---|---|---|
| John | 35 | 35 | 3 | 否 | $\sqrt{2^2 + 15^2 + 1^2} \approx 15.17$ |
| Mary | 22 | 50 | 2 | 是 | $\sqrt{15^2 + 0^2 + 0^2} = 15$ |
| Hannah | 63 | 200 | 1 | 否 | $\approx 152.23$ |
| Tom | 59 | 170 | 1 | 否 | $\approx 122.00$ |
| Nellie | 25 | 40 | 4 | 是 | $\sqrt{12^2 + 10^2 + 2^2} \approx 15.75$ |
| David | 37 | 50 | 2 | ? | |

3 个最近邻是 Mary（是）、John（否）、Nellie（是），投票结果为"是"。

```python
import numpy as np

names = ["John", "Mary", "Hannah", "Tom", "Nellie"]
X = np.array([[35, 35, 3], [22, 50, 2], [63, 200, 1], [59, 170, 1], [25, 40, 4]], dtype=float)
y = np.array(["No", "Yes", "No", "No", "Yes"])
q = np.array([37, 50, 2], dtype=float)                 # David: age, income (K), cards

def knn_predict(X, y, q, k=3):
    d = np.sqrt(((X - q) ** 2).sum(axis=1))           # Euclidean distances to the query
    nn = np.argsort(d)[:k]
    labels, votes = np.unique(y[nn], return_counts=True)
    return labels[np.argmax(votes)], nn, d

lo, hi = X.min(axis=0), X.max(axis=0)                 # min-max scaling fitted on training data
for name, A, b in [("raw", X, q), ("min-max", (X - lo) / (hi - lo), (q - lo) / (hi - lo))]:
    label, nn, d = knn_predict(A, y, b)
    print(f"{name:8}", [(names[i], round(float(d[i]), 2)) for i in nn], "->", label)
```

```text
raw      [('Mary', 15.0), ('John', 15.17), ('Nellie', 15.75)] -> Yes
min-max  [('John', 0.35), ('Mary', 0.37), ('Nellie', 0.73)] -> Yes
```

（Python 3.12，NumPy 2.5。）归一化之后结论不变，但最近邻的次序变了：原始距离中卡数几乎不起作用（取值只差 $1$ 到 $2$），归一化后它与年龄、收入同等重要。

### 4.2.3. 距离度量

设 $\boldsymbol{x}_i = (x_{i1}, \dots, x_{ip})$，$\boldsymbol{x}_j = (x_{j1}, \dots, x_{jp})$。

**定义 4.2.2（Minkowski 距离）** 对 $\lambda \ge 1$，

$$
d_\lambda(\boldsymbol{x}_i, \boldsymbol{x}_j) = \Bigl(\sum_{k=1}^p \lvert x_{ik} - x_{jk}\rvert^\lambda\Bigr)^{1/\lambda}
$$
称为 $L_\lambda$ 距离或 **Minkowski 距离**。$\lambda = 2$ 时是**欧氏距离**；$\lambda = 1$ 时是**曼哈顿距离** $\sum_k \lvert x_{ik} - x_{jk}\rvert$（又称城市街区距离、出租车距离）；$\lambda \to \infty$ 时是 **Chebyshev 距离** $\max_k \lvert x_{ik} - x_{jk}\rvert$（又称棋盘距离，$L_\infty$ 距离）。

其他常用的距离与相似度：

| 名称 | 公式 | 适用 |
|---|---|---|
| 加权欧氏距离 | $\sqrt{\sum_k w_k (x_{ik} - x_{jk})^2}$ | 各属性重要性不同（§4.2.4） |
| **马氏距离** | $\sqrt{(\boldsymbol{x}_i - \boldsymbol{x}_j)^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}_i - \boldsymbol{x}_j)}$ | 属性相关、尺度不同（[3.4.1](/3.4.1)） |
| Canberra 距离 | $\sum_k \frac{\lvert x_{ik} - x_{jk}\rvert}{\lvert x_{ik}\rvert + \lvert x_{jk}\rvert}$ | 取值在 $0$ 附近的数据，对小的差别敏感 |
| Bray–Curtis 相异度 | $\frac{\sum_k \lvert x_{ik} - x_{jk}\rvert}{\sum_k (x_{ik} + x_{jk})}$ | 非负的计数或丰度数据（生态学） |
| Hamming 距离 | 取值不同的属性个数 | 类别型属性 |
| **余弦相似度** | $\frac{x_i^{\mathsf T}\boldsymbol{x}_j}{\|\boldsymbol{x}_i\|\,\|\boldsymbol{x}_j\|}$ | 文本、嵌入向量：只看方向不看长度 |

对单位向量，$\|\boldsymbol{x}_i - \boldsymbol{x}_j\|^2 = 2 - 2\cos\theta$，所以先把向量归一化到单位长度，欧氏最近邻与余弦最近邻就相同。这在向量检索中很常用。

### 4.2.4. 属性的归一化与加权

邻居之间的距离可能被个别取值特别大的属性支配。例如 John（35 岁，年收入 95 千）与 Rachel（41 岁，年收入 215 千）之间，若收入以元计，距离几乎完全等于收入之差 $120\,000$，年龄与卡数毫无作用。因此对属性归一化是非常重要的：

- min–max 归一化：$x' = \frac{x - \min}{\max - \min} \in [0, 1]$（例 4.2.1、例 4.2.2 的做法）；
- **标准化**：$x' = \frac{x - \bar x}{s}$，均值为 $0$、标准差为 $1$，对离群点比 min–max 稳健一些；
- 对严重右偏的属性（收入、计数），先取对数再归一化。

归一化的参数（最小值、最大值、均值、标准差）只能在训练集上计算，再用于测试样例，否则就是[数据泄漏](/4.6.2#sec-2.5)。

$k$ 近邻还有一个更深的问题：一个样例的分类基于全部属性，与属性和类别是否相关无关。若一个样例由 $20$ 个属性描述而只有 $2$ 个与类别相关，在那 $2$ 个属性上相同的样例，在 $20$ 维空间中可能相距很远。解决办法是按相关性给属性加权，在距离中缩放各维：

$$
d_w(\boldsymbol{x}_i, \boldsymbol{x}_j) = \Bigl(\sum_{k=1}^p w_k (x_{ik} - x_{jk})^2\Bigr)^{1/2}.
$$
$w_k = 0$ 就是删去第 $k$ 个属性，即特征选择。一种可行的加权方法是取 $w_k$ 为属性与类别之间的互信息 $I(X_k; Y) = H(X_k) + H(Y) - H(X_k, Y)$，其中 $H$ 是熵，$H(X, Y) = -\sum_{x, y} p(x, y)\log p(x, y)$ 是联合熵；也可以把 $w_k$ 当作**超参数**用交叉验证选取，或者学习一个完整的线性变换（度量学习）。

### 4.2.5. k 的选择与打破平局

$k$ 控制模型的复杂度。$k = 1$ 时决策边界紧跟每个训练样例，对噪声敏感；$k$ 增大时边界变得光滑，预测更稳定，但会抹去真实的局部结构；$k = n$ 时总是预测多数类。这是又一个**偏差–方差权衡**。

![同一组含噪声的两类数据上 k = 1、15、75 时 k 近邻的决策区域，标题中是 10 折交叉验证的错误率：k = 1 过拟合，k = 75 过于光滑](./plots/knn-decision-boundary.py)

- 经验上 $k$ 常取 $3$ 到 $10$ 之间的小奇数，但合适的值取决于训练样例的数目与噪声水平，更大的 $k$ 不一定更好。
- 应当用**交叉验证**选择 $k$。对 $k$ 近邻，**留一交叉验证**几乎不需要额外计算：每次把一个样例拿出来作验证，在其余样例中找它的近邻即可，不需要重新"训练"。
- $k$ 近邻是稳定的：训练样例中的少量扰动不会使结果发生很大的变化（决策树则不稳定，见 [4.5.6](/4.5.6) 与 [4.6.6](/4.6.6)）。

平局（如二分类中 $k$ 取偶数，或 $k = 3$ 而三个邻居分属三类）的处理办法有：二分类时取奇数的 $k$；再看第 $k+1$ 个邻居；取最近的那个邻居的类别；随机选择；或者输出各类的比例作为概率（如 $1/3$）。更好的办法是让近的邻居票数更多，见 §4.5。

下面用 scikit-learn 在乳腺肿瘤数据集（569 个样例，30 个属性）上比较归一化前后的效果，并用 10 折交叉验证同时选择 $k$ 和是否按距离加权。

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import GridSearchCV, cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

X, y = load_breast_cancer(return_X_y=True)            # 569 tumours, 30 features
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)

raw = KNeighborsClassifier(n_neighbors=5)
scaled = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
for name, model in [("raw", raw), ("standardized", scaled)]:
    print(f"{name:13} 10-fold CV accuracy: {cross_val_score(model, X_tr, y_tr, cv=10).mean():.3f}")

grid = GridSearchCV(scaled, {"kneighborsclassifier__n_neighbors": range(1, 31, 2),
                             "kneighborsclassifier__weights": ["uniform", "distance"]}, cv=10)
grid.fit(X_tr, y_tr)
print("best:", grid.best_params_, f"CV={grid.best_score_:.3f}")
print(f"test accuracy of the chosen model: {grid.score(X_te, y_te):.3f}")
```

```text
raw           10-fold CV accuracy: 0.944
standardized  10-fold CV accuracy: 0.972
best: {'kneighborsclassifier__n_neighbors': 9, 'kneighborsclassifier__weights': 'uniform'} CV=0.974
test accuracy of the chosen model: 0.951
```

（Python 3.12，scikit-learn 1.9。）标准化放在 `Pipeline` 里，使交叉验证的每一折都只用训练部分来估计均值与标准差。被选中的配置的交叉验证准确率（$0.974$）略高于它在测试集上的准确率（$0.951$），这正是 [4.6.2](/4.6.2#sec-2.2.2) 所说的"选中最好结果"带来的乐观偏差，以及测试集上的随机波动。

## 4.3. 维数灾难

$k$ 近邻依赖一个假定：近的样例相似。高维空间中，"近"本身变得可疑。

**定义 4.3.1（维数灾难）** 随着空间维数 $d$ 增大，覆盖空间所需的样例数呈指数增长，固定数量的样例变得极其稀疏，点与点之间的距离趋于相等，依赖局部邻域或距离的方法随之失效。这些现象统称为**维数灾难**。

几个定量的例子（设数据在单位超立方体 $[0,1]^d$ 中均匀分布）：

- 邻域不再局部。要用一个小立方体框住全部数据的比例 $r$，它的边长须为 $e_d(r) = r^{1/d}$。$d = 10$ 时，框住 $10\%$ 的数据需要边长 $0.1^{1/10} \approx 0.80$，即每个坐标都要覆盖其取值范围的 $80\%$——这样的"邻域"已不再是局部的。
- 样例都在边缘。单位球中半径大于 $1 - \varepsilon$ 的薄壳所占的体积比例为 $1 - (1-\varepsilon)^d$，$d = 100$、$\varepsilon = 0.05$ 时已超过 $99\%$。
- 距离趋于集中。在相当一般的条件下，$d \to \infty$ 时从一个查询点到最远的点与到最近的点的距离之比趋于 $1$（Beyer 等，1999）：最近邻并不比其他点近多少。
- 保持同样的采样密度，所需样例数随 $d$ 指数增长：一维中 $100$ 个点达到的密度，在十维中需要 $100^{10}$ 个点。

![左：在 d 维单位立方体中框住比例 r 的数据所需的小立方体边长 r^(1/d)。右：随机查询点到 1000 个均匀随机点的最远距离与最近距离的相对差，随维数增大迅速趋于 0](./plots/curse-of-dimensionality.py)

对 $k$ 近邻的影响是：无关属性越多，最近邻的含义越弱；同样的错误率需要指数增长的训练样例；而且 §4.4 的 kd 树在高维中也失去了加速作用。应对的办法是降低有效维数：特征选择与属性加权（§4.2.4），**主成分分析**等降维方法（[3.4.5](/3.4.5)），或者用神经网络学出低维的表示（嵌入），再在嵌入空间中找近邻。实际数据的困难通常没有均匀分布那么严重：图像、文本等数据虽然维数很高，却往往集中在一个低维的结构附近（本征维数低），这是基于近邻的方法在实践中仍然有效的原因。

## 4.4. 高效的近邻搜索

$k$ 近邻把全部计算推迟到查询时：朴素的做法对每个查询计算到全部 $n$ 个训练样例的距离，代价为 $O(np)$。训练样例很多、查询很频繁时，这是主要的瓶颈。加速的思路是先检查邻近的点，并且跳过那些不可能比当前找到的最近点更近的点。

### 4.4.1. kd 树

**kd 树**（[4.3.7](/4.3.7)）递归地用与坐标轴垂直的超平面划分空间，每个节点对应一个轴平行的矩形区域。用于近邻搜索时，构造中的几个选择通常用启发式的方法决定：

- 沿哪一维划分：取值范围最宽的一维（[4.3.7](/4.3.7) 中按维循环也可以）；
- 划分的位置：该维的中位数。用中位数而不用均值，是为了使两侧的点数相等、树保持平衡，并且不受离群点的影响；
- 何时停止：区域中剩下的点少于 $m$ 个（如 $m = 8$），或者区域的宽度达到下限。每个叶节点存放一个点的列表；还可以在每个节点存放其下所有点的紧包围盒，以便更有效地剪枝。

**算法 4.4.1（kd 树最近邻查询）** 输入 kd 树与查询点 $q$，维护当前找到的最近点及其距离 $d_{\mathrm{best}}$（初值为 $+\infty$）。从根节点出发：

1. 在内部节点，先递归进入 $q$ 所在一侧的子树；
2. 到达叶节点时，计算 $q$ 到其中每个点的距离，必要时更新最近点与 $d_{\mathrm{best}}$；
3. 回溯时，检查每个访问过的节点的另一侧：若 $q$ 到划分超平面的距离（或到该子树包围盒的距离）不小于 $d_{\mathrm{best}}$，则另一侧不可能有更近的点，整棵子树被剪掉；否则也要进入另一侧搜索。

$k$ 近邻的查询相同，只是维护 $k$ 个最近点（用一个大小为 $k$ 的最大堆），以其中最远的距离作为剪枝的界。下面的实现用这个算法回答精确的最近邻查询，并统计每次查询实际计算了多少个距离。

```python
import numpy as np

LEAF_SIZE = 8

def build(points, idx):
    """Split on the widest dimension at its median until a leaf holds <= LEAF_SIZE points."""
    if len(idx) <= LEAF_SIZE:
        return {"leaf": idx}
    p = points[idx]
    dim = int(np.argmax(p.max(axis=0) - p.min(axis=0)))
    order = idx[np.argsort(p[:, dim])]
    mid = len(order) // 2
    return {"dim": dim, "split": points[order[mid], dim],
            "left": build(points, order[:mid]), "right": build(points, order[mid:])}

def nearest(node, points, q, best):
    """Depth-first search; best = [squared distance, index, visited points]."""
    if "leaf" in node:
        d2 = ((points[node["leaf"]] - q) ** 2).sum(axis=1)
        best[2] += len(d2)
        j = int(np.argmin(d2))
        if d2[j] < best[0]:
            best[0], best[1] = float(d2[j]), int(node["leaf"][j])
        return
    gap = q[node["dim"]] - node["split"]
    near, far = (node["right"], node["left"]) if gap >= 0 else (node["left"], node["right"])
    nearest(near, points, q, best)                    # first the side containing q
    if gap * gap < best[0]:                           # the far side can still hold a closer point
        nearest(far, points, q, best)

rng = np.random.default_rng(0)
n = 20_000
for d in [2, 5, 10, 20]:
    points = rng.random((n, d))
    tree = build(points, np.arange(n))
    visited = []
    for q in rng.random((200, d)):
        best = [np.inf, -1, 0]
        nearest(tree, points, q, best)
        assert best[1] == int(np.argmin(((points - q) ** 2).sum(axis=1)))   # exact answer
        visited.append(best[2])
    print(f"d={d:2}: distance computations per query = {np.mean(visited):7.0f} of {n}")
```

```text
d= 2: distance computations per query =      10 of 20000
d= 5: distance computations per query =     119 of 20000
d=10: distance computations per query =    3642 of 20000
d=20: distance computations per query =   19977 of 20000
```

（Python 3.12，NumPy 2.5。）低维时每次查询只需计算十几个距离，与 $\log n$ 同阶（Friedman、Bentley 与 Finkel，1977）；$d = 10$ 时已要检查近五分之一的点，$d = 20$ 时几乎检查了全部的点，比蛮力搜索还慢（多了遍历树的开销）。这是维数灾难的直接表现：高维中查询点周围半径为 $d_{\mathrm{best}}$ 的球几乎与所有的区域相交，剪枝失效。经验上，kd 树只在 $n \gg 2^d$ 时有效。kd 树占用 $O(n)$ 的空间，构造需要 $O(n \log n)$ 的时间。球树（ball tree）用超球代替矩形，在中等维数下表现稍好；scikit-learn 的 `KNeighborsClassifier` 默认的 `algorithm="auto"` 根据数据的维数与规模在蛮力、kd 树与球树之间选择。

### 4.4.2. 近似最近邻

高维中精确的最近邻搜索难以比蛮力快很多；而在图像检索、推荐、检索增强的大语言模型等应用中，数据是由神经网络产生的数百到数千维的嵌入向量，规模达到数亿乃至数十亿。这些应用并不需要严格的最近邻，找到足够近的点就够了。

**定义 4.4.1（近似最近邻）** 设 $p^*$ 是查询 $q$ 的最近邻，$\varepsilon > 0$。若返回的点 $p$ 满足 $d(q, p) \le (1 + \varepsilon)\,d(q, p^*)$，则称 $p$ 是 $q$ 的一个 $(1+\varepsilon)$-**近似最近邻**。以放宽精确性为代价换取查询速度的近邻搜索称为近似最近邻搜索。

实践中更常用的质量度量是召回率：返回的 $k$ 个点中有多少是真正的 $k$ 个最近邻。各种方法在"召回率–每秒查询数–内存"之间取舍。主要的几类方法：

| 方法 | 思想 | 代表 |
|---|---|---|
| 局部敏感哈希（LSH） | 设计一族哈希函数，使相近的点以高概率落入同一个桶；只在查询点所在的桶中找 | Indyk 与 Motwani（1998）；有理论保证 |
| 图索引 | 把每个点与它的若干近邻连成图，查询时从入口点出发贪心地走向更近的点 | HNSW（分层可导航小世界图，Malkov 与 Yashunin，2016）；面向磁盘的 DiskANN；面向 GPU 的 CAGRA |
| 倒排文件与量化 | 先用 k 均值把向量聚成若干簇，查询时只搜索最近的几个簇（IVF）；再用乘积量化（PQ）把每个向量压缩成几十个字节，用查表近似计算距离 | Jégou 等（2011）的乘积量化；IVF-PQ |

FAISS（Meta 的开源库）是最常用的实现，在 CPU 与 GPU 上提供精确搜索、IVF、PQ 与 HNSW 等索引，并可以组合使用；其 GPU 索引已集成 NVIDIA 的 cuVS 库。HNSW 在中等规模、内存充足时通常是召回率与速度兼顾的首选，hnswlib 与许多向量数据库（以及 PostgreSQL 的 pgvector 扩展）都以它为默认索引；数据规模超出内存时则用 IVF-PQ 一类的压缩索引或 DiskANN。不同方法与参数的比较可以参考公开的 ANN-Benchmarks 基准。

## 4.5. 距离加权 k 近邻与核回归

$k$ 近邻中，$k$ 个邻居的票数相同，无论它们离查询点多远。更合理的是让近的邻居贡献更大。

**定义 4.5.1（距离加权 k 近邻与核回归）** 取一个随距离增大而减小的非负函数 $K$，令权重 $w_i = K\bigl(d(\boldsymbol{x}_i, \boldsymbol{x}_q)\bigr)$。在 $\boldsymbol{x}_q$ 的 $k$ 个近邻上作加权投票（分类）或加权平均

$$
\hat y_q = \frac{\sum_i w_i\, y_i}{\sum_i w_i}
$$
（回归），称为**距离加权 k 近邻**。当求和遍及全部训练样例时，回归形式称为 Nadaraya–Watson **核回归**，$K$ 称为核函数。

常用的权重有 $1/d^2$、$\mathrm{e}^{-d}$、$1/(1+d)$，以及 Gauss 核 $w_i = \exp\bigl(-d(\boldsymbol{x}_i, \boldsymbol{x}_q)^2 / K_w^2\bigr)$，其中 $K_w$ 是核宽度。$1/d^2$ 在 $d = 0$ 处无定义：查询点与某个训练样例重合时，直接输出它的值，或者改用 $1/(d_0 + d)^2$。加权之后，用全部样例（而不只是 $k$ 个）也不再有问题，因为远处样例的权重几乎为零；这时 $k$ 的作用由核宽度 $K_w$ 代替。

核宽度非常重要。$K_w$ 太小，估计只依赖最近的一两个点，曲线抖动、拟合了噪声；$K_w$ 太大，估计接近全体样例的平均，抹去了真实的变化。选择合适的 $K_w$ 对所有局部加权的学习器都至关重要，通常用交叉验证选取。核回归与统计学中的核密度估计（[3.2.3](/3.2.3)）共用同一套核函数与带宽的思想。

## 4.6. 局部加权回归

核回归在每个查询点处用一个加权的常数拟合数据。若把常数换成线性函数，就得到局部加权回归：回归，是因为它估计实数值的目标函数；局部，是因为估计只依赖查询点附近的数据；加权，是因为每个样例的贡献由它到查询点的距离决定。

**定义 4.6.1（局部加权回归）** 对查询点 $\boldsymbol{x}_q$，记 $\tilde{\boldsymbol{x}} = (1, \boldsymbol{x}^{\mathsf T})^{\mathsf T}$，取权重 $w_i = K\bigl(d(\boldsymbol{x}_i, \boldsymbol{x}_q)\bigr)$（如 $\exp(-d^2/K_w^2)$），求

$$
\hat{\boldsymbol{\beta}}(\boldsymbol{x}_q) = \arg\min_{\boldsymbol{\beta}}\ \sum_{i=1}^n w_i\,\bigl(y_i - \boldsymbol{\beta}^{\mathsf T}\tilde{\boldsymbol{x}}_i\bigr)^2,
$$
并预测 $\hat y_q = \hat{\boldsymbol{\beta}}(\boldsymbol{x}_q)^{\mathsf T}\tilde{\boldsymbol{x}}_q$。这种方法称为**局部加权回归**。

每个查询点都要解一个**加权最小二乘**问题：设 $\tilde X$ 的第 $i$ 行为 $\tilde{\boldsymbol{x}}_i^{\mathsf T}$，$W = \operatorname{diag}(w_1, \dots, w_n)$，则 $\hat{\boldsymbol{\beta}}(\boldsymbol{x}_q) = (\tilde X^{\mathsf T}W\tilde X)^{-1}\tilde X^{\mathsf T}W\boldsymbol{y}$。局部线性拟合的主要好处在数据的边界和斜率较大处：核回归在边界上只能平均一侧的点，估计被拉向内部，局部线性则能沿斜率外推。统计学中的 LOESS / LOWESS（Cleveland，1979）就是局部加权的线性或二次回归，它用 tricube 权重和固定的近邻比例（span）代替固定的核宽度（[3.3.12](/3.3.12)）。

![同一组含噪声样本上的三种基于实例的回归：k 近邻平均（k = 1 拟合了噪声，k = 9 呈阶梯状），核回归（K_w 小时抖动，大时过于平滑并在两端有偏），局部加权线性回归（光滑且两端偏差更小）](./plots/local-regression.py)

上图在一个具体样例上比较各算法：全局的线性回归在函数明显非线性时有很大的偏差；1-NN 相当于把所有点连起来，拟合了噪声；$k = 9$ 的近邻平均光滑了噪声，但不可微、呈阶梯状；核回归得到光滑的曲线，但对核宽度敏感；局部加权回归在合适的核宽度下既光滑，又较好地刻画了两端的趋势。

## 4.7. 基于实例的学习器的四个要素

基于实例（基于记忆）的学习器由四个选择确定：

| 学习器 | 距离度量 | 邻居个数 | 加权函数 | 怎样使用邻居 |
|---|---|---|---|---|
| 1-NN | 欧氏距离 | 1 | 无 | 取邻居的输出 |
| $k$-NN | 欧氏距离 | $k$ | 无 | 投票或平均 |
| 距离加权 $k$-NN / 核回归 | 缩放的欧氏距离 | 全部或 $k$ 个 | $\exp(-d^2/K_w^2)$ 等 | 加权平均 |
| 局部加权回归 | 缩放的欧氏距离 | 全部或 $k$ 个 | $\exp(-d^2/K_w^2)$ 等 | 拟合局部线性模型 |

基于实例的方法的优点是：概念简单，却能逼近任意复杂的目标函数（如图像分类）；对 $k$ 个邻居平均，对噪声较稳健；预测可以解释（"因为它和这几个样例相似"）；训练样例中的信息不会丢失，新数据加入时无需重新训练；除 $k$ 或核宽度外几乎没有参数；留一交叉验证几乎免费。

缺点是：需要存储全部训练样例，内存开销为 $O(np)$；查询时要搜索近邻，计算开销大，所以早期多用于离线场合；很难确定合适的距离函数，特别是样例由复杂的符号结构表示时；无关属性严重影响距离（§4.2.4、§4.3）。

今天，前两个缺点由近似最近邻搜索（§4.4.2）大大缓解，后两个则由表示学习解决：先用神经网络把图像、文本、用户与物品映射为嵌入向量，在嵌入空间中距离有了语义，再在其上做近邻检索。图片搜索、推荐系统的召回阶段、检索增强的大语言模型都是这样工作的；把 $k$ 近邻检索与语言模型的输出插值的 kNN-LM（Khandelwal 等，2020）也属于这一思路。基于实例的学习因此并没有过时，而是成为了大规模系统中的一个基本组件。

## 小结

- 基于实例的学习存储样例、推迟计算，用与查询相似的样例局部地预测；它是非参数化的惰性学习。
- 1-NN 的决策区域是 Voronoi 图；渐近错误率不超过 Bayes 错误率的两倍（Cover–Hart）。
- $k$ 近邻的设计：距离（Minkowski、马氏、余弦……）；属性必须归一化，最好按相关性加权；$k$ 用交叉验证选取，控制偏差与方差的权衡。
- 维数灾难：高维中邻域不再局部、距离趋于集中；需要降维、特征选择或学到的嵌入。
- kd 树在低维中把查询降到对数级，高维中失效；大规模高维检索用近似最近邻（LSH、HNSW、IVF-PQ，FAISS 等库）。
- 距离加权 $k$ 近邻、核回归与局部加权回归把"近的样例更重要"推广到回归；核宽度是最关键的超参数。
