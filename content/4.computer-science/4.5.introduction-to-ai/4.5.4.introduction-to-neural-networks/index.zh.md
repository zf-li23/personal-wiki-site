---
title: 神经网络入门
description: 从数字识别的模板匹配出发理解神经元；激活函数（符号、sigmoid、tanh、ReLU、softmax）与全连接网络，万能逼近定理；损失函数（平方误差与交叉熵）、梯度下降的三种形式与反向传播算法的推导；用反向传播训练网络求解异或问题。
---

前两章的搜索方法要求人写出问题的规则与估值；上一章的 AlphaGo 则用神经网络从数据中学到了估值与走法。本章从一个具体问题出发介绍神经网络的基本概念：怎样让计算机认出手写的数字。我们会看到，单个神经元就是一次"模板匹配"，把许多神经元分层连接起来就能组合出复杂的模式；而模式（网络的权重）不是人设计的，是用梯度下降和反向传播从带标注的样本中自动学到的。本章只讲最基本的全连接网络和训练算法；卷积网络、训练技巧、循环网络与 Transformer 等深入内容见 [4.7 人工神经网络](/4.7)，优化方法的理论见 [3.5.5](/3.5.5)。

## 4.1. 从数字识别谈起

### 4.1.1. 模板匹配

设数字图像是 $15 \times 15$ 的黑白点阵，把它按行展开成向量 $\boldsymbol{x} = (x_1, \dots, x_n)$，$n = 225$，黑点为 $1$、白点为 $0$。怎样判断它是不是数字 3？一个朴素的想法是为数字 3 设计一个模板 $\boldsymbol{w} = (w_1, \dots, w_n)$：3 的笔画经过的位置取 $1$，3 的笔画一定不经过、而别的数字常经过的位置（例如 3 的左侧，8 在那里有笔画）取 $-1$，其余取 $0$。图像与模板的匹配程度用内积衡量：

$$
\mathrm{net} = w_1 x_1 + w_2 x_2 + \cdots + w_n x_n = \boldsymbol{w} \cdot \boldsymbol{x}.
$$
笔画与模板中 $1$ 的位置重合越多，$\mathrm{net}$ 越大；落在 $-1$ 的位置上会被扣分。于是一张 3 的图像得分较高，一张 8 的图像虽然也覆盖了 3 的全部笔画，但它左侧的笔画落在 $-1$ 的位置上，得分较低。

直接比较 $\mathrm{net}$ 有一个问题：它的大小与笔画多少有关。数字 1 的笔画少，即使完全匹配，得分也比不上笔画多的数字；不同的模板之间没有统一的尺度，"多大算匹配"无从判断。改进的办法是加一个偏置 $b$，再用一个单调函数把得分压缩到 $(0, 1)$ 之间：

$$
y = \sigma(\boldsymbol{w} \cdot \boldsymbol{x} + b), \qquad \sigma(z) = \frac{1}{1 + \mathrm{e}^{-z}}.
$$
$-b$ 相当于"及格线"：例如 3 的图像得分 143、8 的图像得分 115 时，取 $b = -129$，就有 $\sigma(14) \approx 0.999999$、$\sigma(-14) \approx 0.000001$，输出可以解释为"是 3 的程度"。

### 4.1.2. 从神经元到网络

上面的计算单元就是一个神经元。为每个数字各设一个模板，就得到 10 个并列的神经元，输出 $y_0, \dots, y_9$，第 $k$ 个输出最大时判为数字 $k$。这是网络在"宽度"上的扩展：增加模式的个数。同一个数字有不同的写法，也可以为它多设几个模板。

整体模板的缺点是不灵活：字写得稍微偏一点、斜一点，匹配就会失败。注意到 3 与 8 的右半部分相同、左半部分不同，可以先用一层神经元检测"局部模式"，如"右上的弧""左下的弧""中间的横"，再用下一层神经元把局部模式组合成整个数字：3 = 右上弧 + 右下弧 + 中间横，8 = 3 + 左上弧 + 左下弧。这是网络在"深度"上的扩展：层数越多，模式的组合越抽象。于是得到多层神经网络：输入层接收像素，若干隐含层逐层提取越来越抽象的模式，输出层给出分类结果。

最关键的一点是：模式由神经元的连接权重表示，而这些权重不是人工设计的，而是通过训练样本自动学习得到的。学到的模式是一种隐含的表示，一般并不像上面举例的"弧"和"横"那样清晰可读。

## 4.2. 神经元与神经网络

### 4.2.1. 神经元

**定义 4.2.1（神经元）** 一个**神经元**接收输入 $\boldsymbol{x} = (x_1, \dots, x_n)$，计算加权和

$$
\mathrm{net} = \sum_{i=1}^{n} w_i x_i + b,
$$
输出 $o = g(\mathrm{net})$。其中 $w_i$ 是连接权重，$b$ 是偏置，$g$ 是激活函数。

令 $x_0 = 1$、$w_0 = b$，偏置可以并入权重：$\mathrm{net} = \sum_{i=0}^{n} w_i x_i = \boldsymbol{w} \cdot \boldsymbol{x}$。这个模型源自 McCulloch 与 Pitts（1943）对生物神经元的抽象：树突接收信号，细胞体整合，超过阈值时轴突发放。取 $g$ 为符号函数就是 Rosenblatt（1958）的感知机，它的学习算法与局限见 [4.7.2](/4.7.2)。

### 4.2.2. 激活函数

**定义 4.2.2（激活函数）** 神经元中把加权和 $\mathrm{net}$ 映射为输出的函数 $g$ 称为**激活函数**。常用的有：

- 符号函数 $\operatorname{sgn}(z) = 1$（$z \ge 0$），$-1$（$z < 0$）；
- sigmoid 函数 $\sigma(z) = \dfrac{1}{1 + \mathrm{e}^{-z}}$，取值于 $(0, 1)$，$\sigma'(z) = \sigma(z)\bigl(1 - \sigma(z)\bigr)$；
- 双曲正切函数 $\tanh z = \dfrac{\mathrm{e}^{z} - \mathrm{e}^{-z}}{\mathrm{e}^{z} + \mathrm{e}^{-z}} = 2\sigma(2z) - 1$，取值于 $(-1, 1)$，$\tanh' z = 1 - \tanh^2 z$；
- 线性整流函数 $\operatorname{ReLU}(z) = \max(0, z)$，导数在 $z > 0$ 时为 1、$z < 0$ 时为 0。

![四种激活函数（实线）及其导数（虚线）：符号函数的导数几乎处处为 0，无法用于梯度下降；sigmoid 与 tanh 在 |z| 大时导数趋于 0（饱和）；ReLU 在正半轴上导数恒为 1](./plots/activations.py)

激活函数必须是非线性的：若 $g$ 是线性的，多层网络的复合仍是一个线性映射，加深网络不会增加表达能力。符号函数不连续、导数几乎处处为零，不能用梯度训练；sigmoid 与 tanh 光滑，但在 $\lvert z\rvert$ 较大时导数趋于零，误差信号经过很多层后会越来越弱（梯度消失，见 [4.7.4](/4.7.4)）。ReLU 计算简单、在正半轴上不饱和，自 2010 年代起成为隐含层的默认选择；今天的大模型多用它的光滑变体（GELU、SwiGLU 等）。

做分类时，输出层常用 softmax 把 $K$ 个输出神经元的加权和 $\mathrm{net}_1, \dots, \mathrm{net}_K$ 变为一个概率分布。

**定义 4.2.3（softmax 函数）** **softmax 函数**把向量 $(z_1, \dots, z_K)$ 映射为

$$
o_k = \frac{\mathrm{e}^{z_k}}{\sum_{j=1}^{K} \mathrm{e}^{z_j}}, \qquad k = 1, \dots, K.
$$
它满足 $0 < o_k < 1$、$\sum_k o_k = 1$，并保持大小次序。

softmax 是"最大值"的光滑版本：把所有 $z_k$ 同时乘以一个大的正数，它的输出趋于在最大分量处为 1 的独热向量。计算时先减去 $\max_k z_k$ 再取指数，结果不变而避免溢出。$K = 2$ 时，$o_1 = \sigma(z_1 - z_2)$，即 sigmoid。

### 4.2.3. 全连接网络

**定义 4.2.4（全连接网络）** 神经元分为若干层：输入层、一个或多个隐含层和输出层，每一层的每个神经元都与下一层的所有神经元相连，同层之间、跨层之间没有连接，信号只从输入向输出单向传播。这样的网络称为**全连接网络**，又称前馈网络、多层感知机（MLP）；其中的每一层称为全连接层或稠密层。

用矩阵写，第 $l$ 层的权重矩阵为 $W^{(l)}$（第 $j$ 行是第 $l$ 层第 $j$ 个神经元的权重），偏置向量为 $\boldsymbol{b}^{(l)}$，则

$$
\boldsymbol{z}^{(l)} = W^{(l)}\boldsymbol{o}^{(l-1)} + \boldsymbol{b}^{(l)}, \qquad \boldsymbol{o}^{(l)} = g\bigl(\boldsymbol{z}^{(l)}\bigr), \qquad l = 1, \dots, L,
$$
其中 $\boldsymbol{o}^{(0)} = \boldsymbol{x}$ 是输入，$g$ 逐分量作用，$\boldsymbol{o}^{(L)}$ 是网络的输出。一层就是一次矩阵乘法加一次逐分量的非线性变换，这也是神经网络适合在 GPU 上计算的原因。

一个隐含层就足以逼近任意连续函数：

**定理 4.2.1（万能逼近定理）** 设 $g$ 是连续函数且不是多项式，$K \subset \mathbb{R}^n$ 是紧集。则对任意连续函数 $f\colon K \to \mathbb{R}$ 和任意 $\varepsilon > 0$，存在 $N$ 以及 $a_j, b_j \in \mathbb{R}$、$\boldsymbol{w}_j \in \mathbb{R}^n$，使

$$
\Bigl\lvert f(\boldsymbol{x}) - \sum_{j=1}^{N} a_j\, g(\boldsymbol{w}_j \cdot \boldsymbol{x} + b_j)\Bigr\rvert < \varepsilon \quad \text{对所有 } \boldsymbol{x} \in K \text{ 成立}.
$$

sigmoid 激活的情形由 Cybenko（1989）证明，一般的非多项式激活由 Leshno 等人（1993）证明。这个定理只保证存在，不说明需要多少个神经元（可能随维数指数增长），也不说明能否通过训练找到这些参数。实践中，深而窄的网络往往比浅而宽的网络用更少的参数达到同样的效果，因为深层网络可以复用中间层的模式，这正是 §4.1.2 中"模式组合"的直观。

## 4.3. 神经网络的训练

### 4.3.1. 数据集

就像小朋友认识动物要先看很多动物并被告知名称，训练网络首先要有数据：收集大量样本（不同姿势、角度、大小的照片，不同人写的数字），并为每个样本标注正确答案。用带标注的样本训练模型属于**有监督学习**。数据一般分为训练集与测试集：在训练集上调整权重，在训练时没有见过的测试集上评价模型的效果；调节网络结构等超参数时还要再分出验证集，或使用**交叉验证**（[3.4.10](/3.4.10)）。只在训练集上表现好而在新数据上表现差，就是**过拟合**。实验方法与评价指标见 [4.6.2](/4.6.2)。

### 4.3.2. 损失函数

训练的目标是让网络的输出 $o_k$ 接近希望的输出 $t_k$（标注）。二者的差距用**损失函数**衡量，训练就是求使损失最小的权重 $\boldsymbol{w}$。最直接的是误差平方和：对样本 $d$，

$$
E_d(\boldsymbol{w}) = \frac12 \sum_{k=1}^{M} (t_{kd} - o_{kd})^2, \qquad E(\boldsymbol{w}) = \sum_{d=1}^{D} E_d(\boldsymbol{w}),
$$
其中 $M$ 是输出神经元的个数，$D$ 是样本数，$t_{kd}$、$o_{kd}$ 是样本 $d$ 的第 $k$ 个希望输出与实际输出。因子 $\frac12$ 只是为了求导后消去 2。

分类问题更常用交叉熵。

**定义 4.3.1（交叉熵损失）** 设网络输出 $\boldsymbol{o}_d$ 是一个概率分布（如 softmax 的输出），希望输出 $\boldsymbol{t}_d$ 也是概率分布。样本 $d$ 的**交叉熵损失**为

$$
H_d(\boldsymbol{w}) = -\sum_{k=1}^{M} t_{kd} \log o_{kd},
$$
总损失 $H(\boldsymbol{w}) = \sum_{d=1}^{D} H_d(\boldsymbol{w})$。

分类问题中，样本 $d$ 的希望输出只在正确类别 $c_d$ 处为 1、其余为 0（独热向量），交叉熵就化为 $H_d = -\log o_{c_d d}$：正确类别的预测概率越接近 1，损失越接近 0；预测概率接近 0 时损失趋于无穷大。最小化交叉熵等价于最大化训练数据的对数似然，即极大似然估计（[3.2.3](/3.2.3)）。

两种损失的分工：误差平方和用于输出是具体数值的回归问题，交叉熵用于分类问题。softmax 与交叉熵搭配还有一个计算上的好处：$H_d$ 对 softmax 的输入 $z_k$ 的偏导数恰为

$$
\frac{\partial H_d}{\partial z_k} = o_{kd} - t_{kd},
$$
简洁且不会因 sigmoid 饱和而变小（证明：$\partial o_j / \partial z_k = o_j(\delta_{jk} - o_k)$，代入并利用 $\sum_j t_{jd} = 1$）。

### 4.3.3. 梯度下降

损失函数最小化问题一般没有解析解，要迭代求解：从初始值出发，每次沿使损失下降的方向修改权重。负梯度方向是局部下降最快的方向，于是得到**梯度下降法**（[3.5.5](/3.5.5)）：

$$
\boldsymbol{w} \leftarrow \boldsymbol{w} - \eta\, \nabla_{\boldsymbol{w}} E(\boldsymbol{w}), \qquad \nabla_{\boldsymbol{w}} E = \Bigl(\frac{\partial E}{\partial w_1}, \dots, \frac{\partial E}{\partial w_n}\Bigr),
$$
其中 $\eta > 0$ 是学习率（步长）。修改量的方向由梯度决定，大小由 $\eta$ 控制：$\eta$ 太大会在谷底两侧来回振荡甚至发散，太小则收敛很慢。

按每次更新用到的样本数，有三种形式：

| 名称 | 每次更新用的样本 | 特点 |
|---|---|---|
| 批量梯度下降 | 全部 $D$ 个样本，$E = \sum_d E_d$ | 方向准确，但每步代价随数据量增长 |
| **随机梯度下降** | 1 个样本，$E_d$ | 每步便宜，方向有噪声，噪声有时有助于跳出差的局部极小 |
| **小批量梯度下降** | $B$ 个样本（如 32–4096） | 兼顾二者，便于在 GPU 上并行，是深度学习的标准做法 |

实践中"随机梯度下降"（SGD）一词也常指小批量的版本。动量、Adam 等改进的优化器与学习率调度见 [4.7.4](/4.7.4)。

### 4.3.4. 反向传播

梯度下降需要损失对每个权重的偏导数。网络有成千上万乃至上万亿个权重，逐个用差分近似偏导数，每个都要把网络重新算一遍，代价不可接受。反向传播利用链式法则，只用一次前向计算和一次反向计算就得到全部偏导数。

先以 sigmoid 激活、误差平方和损失、对单个样本 $d$ 的随机梯度下降为例推导（省略下标 $d$）。记 $x_{ji}$ 为神经元 $j$ 的第 $i$ 个输入，$w_{ji}$ 为相应的权重，$\mathrm{net}_j = \sum_i w_{ji} x_{ji}$，$o_j = \sigma(\mathrm{net}_j)$。权重 $w_{ji}$ 只通过 $\mathrm{net}_j$ 影响损失，所以

$$
\frac{\partial E}{\partial w_{ji}} = \frac{\partial E}{\partial \mathrm{net}_j} \cdot \frac{\partial \mathrm{net}_j}{\partial w_{ji}} = \frac{\partial E}{\partial \mathrm{net}_j}\, x_{ji}.
$$
令 $\delta_j = -\dfrac{\partial E}{\partial \mathrm{net}_j}$（称为神经元 $j$ 的误差项），则权重的修改量为

$$
\Delta w_{ji} = -\eta \frac{\partial E}{\partial w_{ji}} = \eta\, \delta_j\, x_{ji}.
$$
剩下的问题是计算 $\delta_j$，分两种情况。

输出层神经元 $k$：$E = \frac12\sum_k (t_k - o_k)^2$ 中只有一项含 $o_k$，

$$
\delta_k = -\frac{\partial E}{\partial o_k} \cdot \frac{\partial o_k}{\partial \mathrm{net}_k} = (t_k - o_k)\, o_k (1 - o_k).
$$

隐含层神经元 $h$：它通过所有后继神经元（下一层中与它相连的神经元）影响损失，记后继的集合为 $\operatorname{Ds}(h)$。由于 $\mathrm{net}_k = \sum_j w_{kj} o_j$，$\partial \mathrm{net}_k / \partial o_h = w_{kh}$，所以

$$
\delta_h = -\sum_{k \in \operatorname{Ds}(h)} \frac{\partial E}{\partial \mathrm{net}_k} \cdot \frac{\partial \mathrm{net}_k}{\partial o_h} \cdot \frac{\partial o_h}{\partial \mathrm{net}_h} = o_h (1 - o_h) \sum_{k \in \operatorname{Ds}(h)} \delta_k\, w_{kh}.
$$
隐含层的误差项由后一层的误差项加权求和得到：误差从输出层逐层向输入层"反向传播"。

**算法 4.3.1（反向传播，随机梯度下降版）** 把所有权重初始化为小的随机数（如 $[-0.05, 0.05]$ 中均匀分布）。在满足结束条件之前，对每个训练样本：

1. 前向：把样本输入网络，逐层计算每个神经元 $u$ 的输出 $o_u$；
2. 对每个输出神经元 $k$，计算 $\delta_k = (t_k - o_k)\, o_k(1 - o_k)$；
3. 从后向前，对每个隐含层神经元 $h$，计算 $\delta_h = o_h(1 - o_h)\sum_{k \in \operatorname{Ds}(h)} \delta_k w_{kh}$；
4. 更新每个权重：$w_{ji} \leftarrow w_{ji} + \eta\, \delta_j\, x_{ji}$。

这种用链式法则从后向前高效计算全部偏导数的方法称为反向传播（backpropagation），简称 BP，又称误差反向传播。它由多人独立提出，因 Rumelhart、Hinton 与 Williams（1986）的工作而广为人知。

上面的推导依赖于具体的条件：全连接网络、随机梯度下降、sigmoid 激活与误差平方和。换成别的激活函数，只需把 $o(1 - o)$ 换成 $g'(\mathrm{net})$；换成交叉熵与 softmax，输出层的误差项变为 $t_k - o_k$（§4.3.2）。用矩阵写，一般的形式是

$$
\boldsymbol{\delta}^{(L)} = -\nabla_{\boldsymbol{z}^{(L)}} E, \qquad \boldsymbol{\delta}^{(l)} = \bigl(W^{(l+1)\mathsf T}\boldsymbol{\delta}^{(l+1)}\bigr) \odot g'\bigl(\boldsymbol{z}^{(l)}\bigr), \qquad \frac{\partial E}{\partial W^{(l)}} = -\boldsymbol{\delta}^{(l)}\boldsymbol{o}^{(l-1)\mathsf T},
$$
其中 $\odot$ 是逐分量乘积。反向计算的代价与前向计算同阶，即与权重的个数成正比。现代深度学习框架（PyTorch、JAX 等）把任意由基本运算组成的计算表示成计算图，自动完成这一过程，称为自动微分（反向模式）；使用者只需写出前向计算。完整的推导、计算图与各种损失和激活函数见 [4.7.2](/4.7.2)。

### 4.3.5. 例：异或问题

异或 $a \oplus b = (\lnot a \land b) \lor (a \land \lnot b)$ 的四个样本 $(0,0) \mapsto 0$、$(0,1) \mapsto 1$、$(1,0) \mapsto 1$、$(1,1) \mapsto 0$ 不能被一条直线分开，单个神经元无法表示它（[4.7.2](/4.7.2)），至少需要一个隐含层。下面用 numpy 实现一个 2–3–1 的 sigmoid 网络，用算法 4.3.1 训练；先用中心差分检查反向传播得到的梯度。

```python
import numpy as np

rng = np.random.default_rng(0)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float).T   # one sample per column
T = np.array([[0, 1, 1, 0]], dtype=float)                       # XOR targets

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# A 2-3-1 fully connected network; W has shape (outputs, inputs).
W1, b1 = rng.uniform(-1, 1, (3, 2)), np.zeros((3, 1))
W2, b2 = rng.uniform(-1, 1, (1, 3)), np.zeros((1, 1))

def forward(x):
    h = sigmoid(W1 @ x + b1)
    o = sigmoid(W2 @ h + b2)
    return h, o

def loss(x, t):
    return 0.5 * np.sum((t - forward(x)[1]) ** 2)

def backprop(x, t):
    """Gradients of E = sum (t - o)^2 / 2 by the delta rule."""
    h, o = forward(x)
    delta_o = (t - o) * o * (1 - o)                   # output layer
    delta_h = h * (1 - h) * (W2.T @ delta_o)          # hidden layer
    return -delta_h @ x.T, -delta_h, -delta_o @ h.T, -delta_o   # dE/dW1, dE/db1, dE/dW2, dE/db2

# Gradient check against central finite differences.
x0, t0 = X[:, [1]], T[:, [1]]
analytic = backprop(x0, t0)[0]
numeric = np.zeros_like(W1)
eps = 1e-6
for idx in np.ndindex(W1.shape):
    old = W1[idx]
    W1[idx] = old + eps
    e_plus = loss(x0, t0)
    W1[idx] = old - eps
    e_minus = loss(x0, t0)
    W1[idx] = old
    numeric[idx] = (e_plus - e_minus) / (2 * eps)
print(f"max gradient error: {np.abs(analytic - numeric).max():.1e}")

# Stochastic gradient descent, one sample at a time.
eta = 0.5
for epoch in range(10001):
    for i in rng.permutation(4):
        gW1, gb1, gW2, gb2 = backprop(X[:, [i]], T[:, [i]])
        W1 -= eta * gW1
        b1 -= eta * gb1
        W2 -= eta * gW2
        b2 -= eta * gb2
    if epoch % 2500 == 0:
        print(f"epoch {epoch:5d}: E = {loss(X, T):.5f}")
print("outputs:", np.round(forward(X)[1], 3))
```

```text
max gradient error: 2.3e-11
epoch     0: E = 0.51101
epoch  2500: E = 0.00331
epoch  5000: E = 0.00112
epoch  7500: E = 0.00065
epoch 10000: E = 0.00046
outputs: [[0.015 0.985 0.985 0.015]]
```

![2–3–1 网络在异或问题上的训练结果：左图是网络输出在平面上的取值，黑线为 o = 0.5 的分界线，两条近似平行的边界之间判为 1；右图是训练损失随轮数的变化（对数坐标），开始时有一段平台期，之后迅速下降](./plots/xor-network.py)

训练开始时损失几乎不变，随后突然下降：初始时各隐含神经元的输出相近，要经过一段时间才"分工"为两个不同的线性边界。每个隐含神经元对应平面上的一条直线边界，输出神经元把它们组合起来，最终把平面分成三条带，中间的带判为 1。这一过程对初始值和学习率敏感，换一个随机种子，平台期的长度会不同，偶尔还会停在一个局部极小处；隐含神经元多一些时这种情况更少见。

## 4.4. 学到了什么

把训练好的数字识别网络中第一层每个神经元的权重画成 $15 \times 15$ 的图像，会看到一些笔画状、斑块状的模式，有的像某个数字的局部，有的难以解释；越往后的层，模式越抽象。这正是 §4.1 的直观：网络自动学到了"模板"和它们的组合，而不需要人去设计特征。

这一章的网络还很初级，用于图像、语音、文本时会遇到许多问题，它们是 [4.7](/4.7) 的内容：

- 全连接层的参数随输入尺寸迅速增长，也不利用图像的局部性与平移不变性，于是有卷积神经网络（[4.7.3](/4.7.3)）；
- 网络加深后梯度消失、训练不稳定、过拟合，需要 ReLU、归一化、残差连接、Dropout、更好的优化器等技巧（[4.7.4](/4.7.4)）；
- 文本、语音是变长的序列，需要词向量与循环网络（[4.7.5](/4.7.5)），以及今天的主流 Transformer（[4.7.6](/4.7.6)）。

## 小结

- 神经元计算加权和再经过激活函数，可以理解为一次带阈值的模板匹配；多个神经元并列增加模式的个数，分层连接组合出更抽象的模式。
- 激活函数必须非线性。sigmoid、tanh 光滑但会饱和，ReLU 是隐含层的默认选择；softmax 把输出变为概率分布。
- 全连接网络的每一层是矩阵乘法加逐分量的非线性；一个隐含层就能逼近任意连续函数（定理 4.2.1），但深层网络通常更高效。
- 训练 = 选择损失函数（回归用平方误差，分类用交叉熵）+ 梯度下降（批量、随机、小批量）。
- 反向传播用链式法则从输出层向输入层逐层计算误差项 $\delta$，代价与前向计算同阶；权重修改量 $\Delta w_{ji} = \eta\,\delta_j x_{ji}$。
