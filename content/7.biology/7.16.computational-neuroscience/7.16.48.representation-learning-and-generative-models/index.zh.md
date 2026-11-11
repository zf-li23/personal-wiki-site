---
title: 表征学习与生成模型
description: 作为生成模型之逆的知觉：识别模型与生成模型、Helmholtz 机与醒–睡算法；隐变量密度估计与 EM；自编码器、变分自编码器及其证据下界、β-VAE 与解缠，以及线性情形作为率–失真的精确解；解缠的隐变量与面孔区神经元；Rao–Ballard 预测编码、误差单元与端点抑制、失配信号与自由能原理；作为皮层目标函数的对比与联合嵌入自监督学习；扩散模型与采样假说。
source_hash: 6cd363afcbd4
---

感觉皮层接收高维输入 $\boldsymbol{x}$，如视网膜上的图像或耳蜗中的声音，并必须表示其成因：物体、它们的位置、它们的照明。前面的章节描述了表征的样子（感受野见 [7.16.18](/7.16.18)，层级见 [7.16.19](/7.16.19)），并从高效编码原理（[7.16.20](/7.16.20)）和 Hebb 学习（[7.16.22](/7.16.22)）推导了其中一些。本章讨论大脑怎样能从无标签的输入中*学习*好的表征。这里发展的答案可以追溯到 Helmholtz 的"无意识推断"：大脑学习其输入的生成模型，即成因如何产生感觉的模型，而知觉就是对它求逆；[7.16.27](/7.16.27) 的贝叶斯观察者是同一想法在模型已知时的情形。我们讨论经典模型（Helmholtz 机、因子分析与混合模型）、变分自编码器及其与面孔区解缠编码的关系、作为回路实现的预测编码、自监督目标，以及作为一种采样方式的扩散模型。机器学习方法本身（网络训练、Transformer、预训练）见 [4.7](/4.7)；这里只讨论它们与大脑的关系。存储并补全记忆的吸引子网络（[7.16.43](/7.16.43)）是相关但不同的一种无监督学习，大脑怎样计算这些模型所需的梯度则是 [7.16.50](/7.16.50) 的主题。

我们像机器学习文献中那样，把输入记作 $\boldsymbol{x}$、隐含的成因记作 $\boldsymbol{z}$（在神经解释中，$\boldsymbol{x}$ 是输入层的活动，$\boldsymbol{z}$ 是更高区域的活动）。

## 48.1. 推断与生成

### 48.1.1. 识别模型与生成模型

**定义 48.1.1（生成模型与识别模型）** 含隐变量 $\boldsymbol{z}$ 的数据 $\boldsymbol{x}$ 的**生成模型**是联合分布 $p_{\boldsymbol{\theta}}(\boldsymbol{x}, \boldsymbol{z}) = p_{\boldsymbol{\theta}}(\boldsymbol{z})\,p_{\boldsymbol{\theta}}(\boldsymbol{x} \mid \boldsymbol{z})$，即成因的先验与描述成因如何产生数据的似然的乘积；其边缘分布 $p_{\boldsymbol{\theta}}(\boldsymbol{x}) = \int p_{\boldsymbol{\theta}}(\boldsymbol{x}, \boldsymbol{z})\,\mathrm{d}\boldsymbol{z}$ 是模型对数据的密度。**识别模型**是把输入映射到其成因（的分布）、并近似后验 $p_{\boldsymbol{\theta}}(\boldsymbol{z} \mid \boldsymbol{x})$ 的分布 $q_{\boldsymbol{\phi}}(\boldsymbol{z} \mid \boldsymbol{x})$。

两个方向的难度不同。生成很容易：抽样 $\boldsymbol{z}$，再抽样 $\boldsymbol{x}$。识别则需要 Bayes 公式 $p(\boldsymbol{z} \mid \boldsymbol{x}) = p(\boldsymbol{x} \mid \boldsymbol{z})p(\boldsymbol{z})/p(\boldsymbol{x})$，其归一化因子是对所有成因的积分，对有意思的模型是难以处理的。判别式分类器直接从有标签的样本学习 $p(\text{标签} \mid \boldsymbol{x})$；生成模型学习 $\boldsymbol{x}$ 本身的结构，可以通过最大化所观察数据的似然 $\sum_i \log p_{\boldsymbol{\theta}}(\boldsymbol{x}_i)$ 而无需标签地拟合。隐空间在维数较低（$\dim\boldsymbol{z} \ll \dim\boldsymbol{x}$）、且其坐标对应于世界的独立成因时才有用：好的表征使下游任务（分类、控制、记忆）变得简单，例如可以线性解码。

神经上的动机有三点。第一，标签很少：婴儿看到的物体很少有人告诉它名称。第二，皮层中充满反馈：在视觉系统中，从高级区域到低级区域的连接与前向的连接一样多（[7.16.18](/7.16.18#sec-18.4)），如果高级区域对低级区域的活动生成预测，这是很自然的。第三，知觉受期望塑造，如 [7.16.27](/7.16.27#sec-27.3) 的先验与错觉所示，而意象与梦表明大脑可以在没有输入时产生类似感觉的活动。

### 48.1.2. Helmholtz 机与醒–睡算法

**定义 48.1.2（Helmholtz 机）** **Helmholtz 机**（Dayan, Hinton, Neal and Zemel, 1995）是由随机二值单元组成的分层网络，有两组连接：自下而上的识别权重 $\boldsymbol{\phi}$，逐层计算 $q_{\boldsymbol{\phi}}(\boldsymbol{z} \mid \boldsymbol{x})$；以及自上而下的生成权重 $\boldsymbol{\theta}$，从顶层的先验出发逐层定义 $p_{\boldsymbol{\theta}}(\boldsymbol{x}, \boldsymbol{z})$。

**算法 48.1.1（醒–睡算法）** 醒–睡算法（Hinton, Dayan, Frey and Neal, 1995）交替训练两组权重，每组都用局部的 delta 规则。

1. *醒相。* 呈现真实输入 $\boldsymbol{x}$，用识别权重抽样成因 $\boldsymbol{z} \sim q_{\boldsymbol{\phi}}(\boldsymbol{z} \mid \boldsymbol{x})$，并改变生成权重使 $\log p_{\boldsymbol{\theta}}(\boldsymbol{x}, \boldsymbol{z})$ 增大：每个单元学习由上一层预测下一层的活动。
2. *睡相。* 自上而下生成一个"幻想" $(\boldsymbol{z}, \boldsymbol{x}) \sim p_{\boldsymbol{\theta}}$，并改变识别权重使 $\log q_{\boldsymbol{\phi}}(\boldsymbol{z} \mid \boldsymbol{x})$ 增大：识别网络学习恢复成因，这些成因是已知的，因为它们是被生成出来的。

对于从相邻层接收输入 $\boldsymbol{y}$ 的 sigmoid 单元 $j$，两种更新都具有 $\Delta w_{jk} = \eta\,(s_j - p_j)\,y_k$ 的形式，其中 $s_j$ 是单元 $j$ 的抽样状态，$p_j$ 是它在另一条通路下的概率：突触前活动与突触后预测误差的乘积，这是局部的。醒相最大化 $\log p_{\boldsymbol{\theta}}(\boldsymbol{x})$ 的一个下界（即 48.3 节引入的量）；睡相在幻想上最小化的是反向的散度 $D_{\mathrm{KL}}(p_{\boldsymbol{\theta}}(\boldsymbol{z} \mid \boldsymbol{x})\,\Vert\,q_{\boldsymbol{\phi}}(\boldsymbol{z} \mid \boldsymbol{x}))$，而不是正确的那个，所以该算法并不遵循单一目标的梯度，但对简单模型有效。它对神经科学的意义在于由世界驱动的相与由模型本身驱动的离线相之间的分工，这使人想到与睡眠的比较，睡眠中的**重放**与自发活动在 [7.16.35](/7.16.35) 和 [7.16.42](/7.16.42) 中讨论；这一比较仍是假说。

## 48.2. 含隐变量的密度估计

最简单的生成模型是统计学的隐变量模型，受大脑启发的模型是对它们的推广。

- 在**因子分析**（[定义 28.3.2](/7.16.28#def-28.3.2)）中，$\boldsymbol{z} \sim \mathcal{N}(\boldsymbol{0}, I)$，$\boldsymbol{x} \mid \boldsymbol{z} \sim \mathcal{N}(W\boldsymbol{z} + \boldsymbol{\mu}, \Psi)$，$\Psi$ 为对角阵；取 $\Psi = \sigma^2 I$ 就是概率 PCA（Tipping and Bishop, 1999），其极大似然解张成前几个主成分（[3.4.5](/3.4.5)）。识别是线性的：$\mathbb{E}[\boldsymbol{z} \mid \boldsymbol{x}] = (W^{\mathsf T}\Psi^{-1}W + I)^{-1}W^{\mathsf T}\Psi^{-1}(\boldsymbol{x} - \boldsymbol{\mu})$。
- 在**高斯混合模型**中，$z \in \{1, \dots, K\}$ 是先验概率为 $\pi_k$ 的类别，$\boldsymbol{x} \mid z = k \sim \mathcal{N}(\boldsymbol{\mu}_k, \Sigma_k)$；识别给出责任度 $p(z = k \mid \boldsymbol{x}) \propto \pi_k\,\mathcal{N}(\boldsymbol{x}; \boldsymbol{\mu}_k, \Sigma_k)$，这是类别之间的软竞争，网络用对输入取指数后的**除法归一化**来实现它。
- 在**稀疏编码**（[定义 20.5.1](/7.16.20#def-20.5.1)）中，$\boldsymbol{z}$ 的先验是重尾的，推断是非线性的；学到的字典类似于 V1 的感受野。

三者都用 **EM 算法**（[3.5.6](/3.5.6)）拟合，它交替地进行推断与学习：E 步在当前参数下计算每个数据点上 $\boldsymbol{z}$ 的后验，M 步由期望的完全数据对数似然重新估计参数。用神经语言说，E 步是活动对输入作出响应的快速稳定过程，M 步是利用稳定后的活动的缓慢突触变化，这种时间尺度的分离在下面所有的模型中反复出现。EM 算法需要精确的后验，它只对这些简单模型可得；48.3 节的方法用近似的识别模型代替它，识别模型与生成模型一起学习。

## 48.3. 自编码器与变分自编码器

### 48.3.1. 自编码器

**定义 48.3.1（自编码器）** **自编码器**是这样的网络：它把输入 $\boldsymbol{x}$ 经编码器 $\boldsymbol{z} = f_{\boldsymbol{\phi}}(\boldsymbol{x})$ 映射为较低维的编码（瓶颈），再经解码器 $\hat{\boldsymbol{x}} = g_{\boldsymbol{\theta}}(\boldsymbol{z})$ 映射回去，并在没有标签的情况下训练以使重建误差 $\mathbb{E}\Vert\boldsymbol{x} - \hat{\boldsymbol{x}}\Vert^2$ 最小。

具有 $k$ 维瓶颈的线性自编码器学到前 $k$ 个主成分张成的子空间（Baldi and Hornik, 1989），所以非线性自编码器是一种非线性 PCA。它的编码对压缩和去噪有用（去噪自编码器从被破坏的副本重建 $\boldsymbol{x}$），但它不是生成模型：没有任何东西约束训练数据的编码去充满隐空间，所以对两个编码之间的点或随机点解码，产生的是无意义的东西，而且相近的编码未必意味着相似的输入。

### 48.3.2. 变分自编码器

变分自编码器（Kingma and Welling, 2014；Rezende, Mohamed and Wierstra, 2014）通过给编码一个先验、给编码器概率性的输出，使自编码器成为生成模型。

**定理 48.3.1（证据分解）** 对任意分布 $q(\boldsymbol{z} \mid \boldsymbol{x})$，

$$
\log p_{\boldsymbol{\theta}}(\boldsymbol{x}) = \underbrace{\mathbb{E}_{q}\bigl[\log p_{\boldsymbol{\theta}}(\boldsymbol{x} \mid \boldsymbol{z})\bigr] - D_{\mathrm{KL}}\bigl(q(\boldsymbol{z} \mid \boldsymbol{x})\,\Vert\,p_{\boldsymbol{\theta}}(\boldsymbol{z})\bigr)}_{\mathcal{L}(\boldsymbol{\theta}, q;\,\boldsymbol{x})} + D_{\mathrm{KL}}\bigl(q(\boldsymbol{z} \mid \boldsymbol{x})\,\Vert\,p_{\boldsymbol{\theta}}(\boldsymbol{z} \mid \boldsymbol{x})\bigr). \tag{48.1}
$$

由于最后一项非负，$\mathcal{L} \le \log p_{\boldsymbol{\theta}}(\boldsymbol{x})$，当且仅当 $q$ 是真实后验时取等号。

**证明** 写 $\log p_{\boldsymbol{\theta}}(\boldsymbol{x}) = \mathbb{E}_q[\log p_{\boldsymbol{\theta}}(\boldsymbol{x}, \boldsymbol{z}) - \log p_{\boldsymbol{\theta}}(\boldsymbol{z} \mid \boldsymbol{x})]$，它对每个 $\boldsymbol{z}$ 成立，因而在期望下也成立。加上并减去 $\mathbb{E}_q\log q(\boldsymbol{z} \mid \boldsymbol{x})$，得 $\mathbb{E}_q[\log p_{\boldsymbol{\theta}}(\boldsymbol{x}, \boldsymbol{z}) - \log q] + \mathbb{E}_q[\log q - \log p_{\boldsymbol{\theta}}(\boldsymbol{z} \mid \boldsymbol{x})]$；第二项是后验散度，第一项分解为 $\mathbb{E}_q\log p_{\boldsymbol{\theta}}(\boldsymbol{x} \mid \boldsymbol{z}) + \mathbb{E}_q[\log p_{\boldsymbol{\theta}}(\boldsymbol{z}) - \log q]$。**Kullback–Leibler 散度**的非负性给出这个下界。$\square$

**定义 48.3.2（变分自编码器与证据下界）** 式 (48.1) 中的量 $\mathcal{L}$ 是**证据下界**（ELBO）。**变分自编码器**（VAE）是这样的生成模型：$p(\boldsymbol{z}) = \mathcal{N}(\boldsymbol{0}, I)$，$p_{\boldsymbol{\theta}}(\boldsymbol{x} \mid \boldsymbol{z})$ 由解码器网络给出，并配以输出 Gauss 分布 $q_{\boldsymbol{\phi}}(\boldsymbol{z} \mid \boldsymbol{x}) = \mathcal{N}(\boldsymbol{\mu}_{\boldsymbol{\phi}}(\boldsymbol{x}), \operatorname{diag}\boldsymbol{\sigma}^2_{\boldsymbol{\phi}}(\boldsymbol{x}))$ 的编码器网络；两者都通过最大化数据上的平均 ELBO 来训练。

ELBO 的两项是熟悉的损失的两部分：期望对数似然是重建误差（对方差为 $\sigma^2$ 的 Gauss 解码器，它相差一个常数地等于 $-\mathbb{E}_q\Vert\boldsymbol{x} - g_{\boldsymbol{\theta}}(\boldsymbol{z})\Vert^2/(2\sigma^2)$），而与先验的散度是正则项，它把每个编码拉向 $\mathcal{N}(\boldsymbol{0}, I)$，使编码充满隐空间、随机样本解码为合理的输入。对 $\boldsymbol{\theta}$ 最大化 ELBO 提高似然的下界（学习）；对 $\boldsymbol{\phi}$ 最大化它使识别模型成为后验的更好近似（推断）。对 $\boldsymbol{\phi}$ 的梯度通过*重参数化* $\boldsymbol{z} = \boldsymbol{\mu}_{\boldsymbol{\phi}}(\boldsymbol{x}) + \boldsymbol{\sigma}_{\boldsymbol{\phi}}(\boldsymbol{x}) \odot \boldsymbol{\varepsilon}$、$\boldsymbol{\varepsilon} \sim \mathcal{N}(\boldsymbol{0}, I)$ 穿过抽样步骤，网络用**反向传播**训练（[4.7.2](/4.7.2#sec-2.4)）。算法 48.1.1 的醒相最大化同一个下界；VAE 的不同之处在于，识别模型也在 ELBO 上训练，而不是在幻想上训练。

### 48.3.3. β-VAE 与解缠

**定义 48.3.3（β-VAE 与解缠表示）** **β-VAE**（Higgins 及其同事，2017）在 $\beta > 1$ 时最大化 $\mathbb{E}_q\log p_{\boldsymbol{\theta}}(\boldsymbol{x} \mid \boldsymbol{z}) - \beta\,D_{\mathrm{KL}}(q_{\boldsymbol{\phi}}(\boldsymbol{z} \mid \boldsymbol{x})\,\Vert\,p(\boldsymbol{z}))$。当每个隐坐标随数据的一个生成因子（位置、大小、身份、光照）变化、并对其他因子近乎不变时，表征是**解缠**的。

当 $\beta > 1$ 时，KL 项起容量限制的作用：只有当重建的增益能抵偿时，每个隐变量才携带关于 $\boldsymbol{x}$ 的信息，而对角后验偏向坐标相互独立的编码。在因子独立变化的物体图像上，β-VAE 学到对应于单个因子的隐变量，普通自编码器则不能。无监督的解缠一般并无保证（Locatello 及其同事，2019 证明了没有对模型与数据的归纳偏置时这是不可能的），但偏向独立而经济的隐变量，与**高效编码假说**相同。线性情形可以精确求解，并显示容量限制起什么作用。

**命题 48.3.1（线性 β-VAE）** 设数据的协方差具有本征值 $\lambda_1 \ge \dots \ge \lambda_d$ 与本征向量 $\boldsymbol{e}_i$，解码器为 $p(\boldsymbol{x} \mid \boldsymbol{z}) = \mathcal{N}(W\boldsymbol{z}, \sigma^2 I)$，$\sigma^2$ 固定，编码器是线性的、后验为对角 Gauss 分布。则 β-VAE 的最优解是噪声方差 $s^2 = \beta\sigma^2$ 的概率 PCA：不计隐变量的符号或排列，第 $i$ 个解码器列为 $\sqrt{\max(\lambda_i - s^2, 0)}\,\boldsymbol{e}_i$，隐变量 $i$ 携带

$$
D_{\mathrm{KL}}^{(i)} = \tfrac12\log^+\frac{\lambda_i}{\beta\sigma^2}\ \text{nats}, \tag{48.2}
$$

并且沿 $\boldsymbol{e}_i$ 的期望重建误差为 $\min(\lambda_i, \beta\sigma^2)$。

**证明** β 目标函数的负值为 $\mathbb{E}_q\Vert\boldsymbol{x} - W\boldsymbol{z}\Vert^2/(2\sigma^2) + \beta D_{\mathrm{KL}} + \text{常数}$；除以 $\beta$ 后，它相差一个常数地是同一模型在噪声方差 $\beta\sigma^2$ 下的负 ELBO。所以最优解就是 $s^2 = \beta\sigma^2$ 时普通线性 VAE 的最优解，也就是概率 PCA 的极大似然解（其后验是 Gauss 分布，列沿正交的 $\boldsymbol{e}_i$ 时后验是对角的，所以下界是紧的）。沿 $\boldsymbol{e}_i$，若 $w_i^2 = \lambda_i - s^2 > 0$，后验方差为 $s^2/\lambda_i$，其均值 $w_ix_i/\lambda_i$ 在数据上的方差为 $w_i^2/\lambda_i$，所以 $D_{\mathrm{KL}}^{(i)} = \frac12[s^2/\lambda_i + (\lambda_i - s^2)/\lambda_i - 1 - \log(s^2/\lambda_i)] = \frac12\log(\lambda_i/s^2)$；重建误差为 $\lambda_i(s^2/\lambda_i)^2 + w_i^2s^2/\lambda_i = s^2$。对 $\lambda_i \le s^2$，该隐变量未被使用，误差为 $\lambda_i$。$\square$

![线性 β-VAE 的精确解（命题 48.3.1）。A：二维数据，沿旋转后的主轴的方差为 $4$ 和 $0.25$，解码器噪声 $\sigma^2 = 0.3$；重建 $W\mathbb{E}[\boldsymbol{z} \mid \boldsymbol{x}]$（线段把 12 个数据点与其重建相连）落在主轴上，因为次要方向（$0.25 < \sigma^2$）没有被编码，并且向均值收缩，$\beta = 6$ 时比 $\beta = 1$ 时更强。B：五维数据的每个隐变量的信息，式 (48.2)，方差为 $6, 3, 1.5, 0.6, 0.2$，$\sigma^2 = 0.4$：隐变量 $i$ 在 $\beta = \lambda_i/\sigma^2$ 处关闭（点线），所以增大 $\beta$ 只保留最强的因子。C：随 $\beta$ 变化的总率对总失真，即 Gauss 源率–失真理论的反向注水曲线。](./plots/linear-vae.py)

这一结果有两点启示。第一，$\beta$ 设定了水位 $\beta\sigma^2$：方差低于它的数据方向完全不被编码，高于它的则以固定的误差编码，这是 Gauss 源的率–失真理论的解（Cover and Thomas）。这种容量受限的编码器是 [7.16.20](/7.16.20) 的高效编码，每比特有代价，而 $\beta$ 就是信息的价格。第二，对角后验选出主轴，而概率 PCA 的普通似然对隐空间的任何旋转都是不变的：打破对称性、使隐变量与坐标轴对齐的是识别模型的形式，而不是似然，这一机制在非线性 VAE 中同样起作用（Rolinek, Zietlow and Martius, 2019）。

### 48.3.4. 解缠的隐变量与面孔细胞

猕猴下颞叶皮层的**面孔区**（[定义 18.6.1](/7.16.18#def-18.6.1)）含有这样的神经元，其反应在面孔空间的少数几个轴上是线性的（轴模型，[公式 18.6.1](/7.16.18#fml-18.6.1)）。Higgins 及其同事（2021）在没有标签的面孔图像上训练了 β-VAE，并把它的隐变量与面孔区 ML/MF 和 AM 中 159 个神经元对 2100 幅面孔图像的反应记录作比较。少数几个 β-VAE 隐变量就能解释单个神经元的反应，往往是一一对应的（一个隐变量预测一个神经元），比有监督的面孔识别网络或普通自编码器的单元更接近，而且这些隐变量可以读作头发、年龄或肤色等因子。解缠的隐变量还使得可以由十几个神经元解码新的面孔。该研究提示，IT 神经元的轴就是在信息约束下学到的因子化生成模型的轴，但这种吻合只是若干种吻合之一，并不表明 IT 计算了 ELBO；同样的数据与其他单元相互独立的模型也是相容的。

## 48.4. 预测编码

### 48.4.1. Rao–Ballard 模型

生成模型可以用递归网络求逆：其中每一层预测下一层的活动，只有预测误差向上传递。这一想法由 Srinivasan、Laughlin 和 Dubs（1982）在视网膜中作为去除可预测信号而提出（[7.16.20](/7.16.20#sec-20.3)），由 Mumford（1992）在皮层层级中提出，并由 Rao 和 Ballard（1999）表述为学习模型。

**定义 48.4.1（预测编码）** **预测编码**是在生成模型中进行推断的层级方案：每一层 $\ell$ 持有一个表征 $\boldsymbol{r}_\ell$，向下一层发送对其表征 $\boldsymbol{r}_{\ell - 1}$ 的自上而下的预测 $U_\ell\boldsymbol{r}_\ell$（$\boldsymbol{r}_0 = \boldsymbol{x}$），并从它接收由单独的误差单元携带的预测误差 $\boldsymbol{e}_{\ell - 1} = \boldsymbol{r}_{\ell - 1} - U_\ell\boldsymbol{r}_\ell$；表征的改变使加权误差减小。

**公式 48.4.1（Rao–Ballard 动力学与学习）** 对方差为 $\sigma_\ell^2$ 的 Gauss 层，对负对数后验 $\sum_\ell\Vert\boldsymbol{e}_\ell\Vert^2/(2\sigma_\ell^2)$ 加上先验项做梯度下降，得

$$
\tau\frac{\mathrm{d}\boldsymbol{r}_\ell}{\mathrm{d}t} = \frac{U_\ell^{\mathsf T}\boldsymbol{e}_{\ell - 1}}{\sigma_{\ell - 1}^2} - \frac{\boldsymbol{e}_\ell}{\sigma_\ell^2}, \qquad \Delta U_\ell = \eta\,\frac{\boldsymbol{e}_{\ell - 1}\boldsymbol{r}_\ell^{\mathsf T}}{\sigma_{\ell - 1}^2}. \tag{48.3}
$$

每个表征被其下方的误差（经其预测权重的转置）推动上升，并被拉向来自上方的预测；权重按下方误差与上方表征的 Hebb 乘积学习。

平衡时，表征是成因的 MAP 估计，学习规则与**稀疏编码**（定义 20.5.1）的字典更新相同，后者是式 (48.3) 在稀疏先验下的单层情形。Rao 和 Ballard 在自然图像上训练了一个三层网络。第 1 层单元学到有朝向的局部感受野，第 1 层*误差*单元表现出经典感受野之外的效应：当条形延伸到经典感受野之外时，它们对有朝向的条形的反应被抑制。解释是由解释导致的端点抑制：长条形是自然图像中边缘的典型统计，被上一层预测，所以剩下的误差很少，而短条形则是出乎意料的（见下图）。周边抑制，归一化模型把它解释为除法式的增益控制（[7.16.18](/7.16.18)），在这里是预测的结果。

![手工连线的两层模型中的预测编码与端点抑制（公式 48.4.1）。输入是 15 个像素上 1 至 5 段的条形；五个第 1 层单元各预测一个三像素的段，一个第 2 层单元代表"边缘会延续"这一规律，同等地预测全部五段（$\sigma_0^2 = 1$，$\sigma_1^2 = 0.15$，第 2 层单元的先验方差 $4$，$\tau = 10\,\mathrm{ms}$）。A：输入出现后中心段的表征 $r_1$ 与误差单元 $e_1$ 的时间进程：对单段（实线），误差保持较高；对长条形（虚线），误差是暂时的，第 2 层推断出这条线后降到几乎为零。B：稳态活动对条形长度：表征与第 2 层单元随长度增长，而误差单元是端点抑制的，在恰好充满其经典感受野的条形上最大。](./plots/predictive-coding.py)

### 48.4.2. 证据与开放问题

预测编码作出具体的预测：发出误差信号的神经元对出乎意料的输入的反应应当大于对预期输入的反应，反应应被自上而下的预测所抑制，误差与表征应由不同的细胞或层携带。若干观察与之相符。

- *重复抑制与失配。* 感觉皮层对重复或可预测刺激的反应下降，序列中的偏离刺激引起更大的反应（EEG 的失配负波）；在小鼠中，控制了刺激特异性适应之后，偏离反应仍有一部分保留。
- *感觉运动失配。* 在视觉流与运动耦合的虚拟走廊中奔跑的小鼠，V1 第 2/3 层的一个神经元子集在动物奔跑期间对视觉流的短暂停止作出反应，这是预测输入与实际输入的失配（Keller, Bonhoeffer and Hübener, 2012）；预测经由自上而下的轴突，从前扣带皮层等运动相关区域到达。
- *分层组织。* 向前投射的浅层与向后投射的深层分别被提出携带误差与预测（Bastos 及其同事，2012），在许多研究中，前向信号由 gamma 频段携带，反馈由 alpha/beta 频段携带（[7.16.15](/7.16.15#sec-15.5)）。

关于存在单独误差神经元的证据好坏参半：多数神经元把对输入的反应与对其违反的反应结合在一起，许多期望效应可以用适应或注意（[7.16.18](/7.16.18#sec-18.7)）解释而无需显式的生成模型。预测编码最好看作实现推断的一族回路假说，其细节（哪些细胞计算误差、误差是否有符号、精度 $\sigma_\ell^{-2}$ 如何由**神经调质**设定）正在用细胞类型特异的记录检验。

### 48.4.3. 自由能原理

Friston（2005, 2010）把预测编码推广为*自由能原理*：负 ELBO 类比统计物理称为*变分自由能*，$F = -\mathcal{L} \ge -\log p(\boldsymbol{x})$，它界定感觉输入的意外程度，该原理提出知觉、学习与行动都使它最小。知觉对识别密度最小化 $F$（推断），学习对生成模型的参数最小化它，行动则对输入本身最小化它，即改变世界使之符合预测（"主动推断"）。误差的精度（方差的倒数）加权被等同于注意与神经调制。该原理统一了许多模型，但就其表述而言它非常一般，具体的预测只来自具体的生成模型；因此它是一个框架，其本身不是可检验的理论。

## 48.5. 作为皮层目标的自监督学习

生成模型重建输入的每一个细节，包括没有行为需要的细节（噪声的纹理、精确的像素）。**自监督学习**（[4.7.7](/4.7.7#sec-7.1.3)）在由数据本身定义的前置任务上训练表征。有两族与大脑的理论相关。

**定义 48.5.1（对比学习）** **对比学习**训练编码器 $f$，使同一事物的两个视图 $\boldsymbol{x}, \boldsymbol{x}^+$（图像的两种增广、视频的两个时刻、图像及其说明文字）的表征相似，而无关输入 $\boldsymbol{x}^-_1, \dots, \boldsymbol{x}^-_K$ 的表征不相似，通常通过最小化 InfoNCE 损失

$$
\ell = -\log\frac{\exp\bigl(\operatorname{sim}(f(\boldsymbol{x}), f(\boldsymbol{x}^+))/T\bigr)}{\exp\bigl(\operatorname{sim}(f(\boldsymbol{x}), f(\boldsymbol{x}^+))/T\bigr) + \sum_{k=1}^K\exp\bigl(\operatorname{sim}(f(\boldsymbol{x}), f(\boldsymbol{x}^-_k))/T\bigr)}, \tag{48.4}
$$

其中 $\operatorname{sim}$ 是余弦相似度，$T$ 是温度；$\log(K + 1) - \ell$ 是两个视图表征之间互信息的下界（van den Oord, Li and Vinyals, 2018）。

**定义 48.5.2（联合嵌入预测架构）** **联合嵌入预测架构**（JEPA）对上下文 $\boldsymbol{x}$ 和目标 $\boldsymbol{y}$（图像被遮挡的部分、下一帧）编码，并训练预测器由 $\boldsymbol{x}$ 的表征预测 $\boldsymbol{y}$ 的表征，损失在表征空间而不是输入空间中；对表征方差与协方差的正则项（VICReg、Barlow Twins）或不对称的目标编码器防止塌缩为常数表征。

例子有 SimCLR 与 CLIP（对比式的，后者跨图像与文本）、本着 Barlow 的冗余削减精神使表征各分量去相关的 Barlow Twins（[7.16.20](/7.16.20#sec-20.3)），以及 I-JEPA（LeCun, 2022；Assran 及其同事，2023）。JEPA 预测可以预测的东西而忽略其余，这正是感觉系统所需要的；它也是"世界模型"，即在抽象空间中预测时间与行动后果的模型。

有三条证据把这些目标与皮层联系起来。第一，如 [7.16.19](/7.16.19#sec-19.5) 所讨论的，在无标签图像（包括儿童头戴摄像机拍摄的视频）上训练的对比网络，对 V4 和 IT 反应的预测与有监督网络一样好。第二，大脑有正样本对的天然来源：物体随时间持续，而视网膜图像在变化。把时间上相邻的视图映射为相似表征的学习，即*慢性*原理（Földiák, 1991；Wiskott and Sejnowski, 2002 的慢特征分析），是对比学习的时间形式，IT 的不变性依赖于它：当 Li 和 DiCarlo（2008）在猴子扫视期间交换物体的身份，使某个视网膜位置上的一个物体总被另一个物体替换时，IT 神经元在暴露后一小时之内就开始对该位置上的这两个物体作出相似的反应。第三，对下一个输入的预测是无处不在的训练信号；48.4.2 的失配反应就是这种预测误差。大脑所没有的是式 (48.4) 的巨大负样本批次，或过去表征的存储副本；生物上合理的变体使用局部的、逐层的对比损失（Illing, Ventura, Bellec and Gerstner, 2021），或清醒相与离线（睡眠）相之间的对比，这又回到算法 48.1.1。

## 48.6. 扩散模型与采样假说

扩散模型（Sohl-Dickstein 及其同事，2015；Ho, Jain and Abbeel, 2020）通过逆转逐渐加噪的过程来生成数据。前向过程是固定的 Ornstein–Uhlenbeck 扩散 $\mathrm{d}\boldsymbol{x} = -\tfrac12 b\,\boldsymbol{x}\,\mathrm{d}t + \sqrt{b}\,\mathrm{d}\boldsymbol{W}$，它把任何数据分布 $p_0$ 变为 $\mathcal{N}(\boldsymbol{0}, I)$。它的时间反演（Anderson, 1982）又是一个扩散，

$$
\mathrm{d}\boldsymbol{x} = \bigl[-\tfrac12 b\,\boldsymbol{x} - b\,\nabla_{\boldsymbol{x}}\log p_t(\boldsymbol{x})\bigr]\mathrm{d}t + \sqrt{b}\,\mathrm{d}\bar{\boldsymbol{W}}, \tag{48.5}
$$

从噪声出发反向运行，它只需要加噪分布的得分 $\nabla\log p_t$。为给有噪样本去噪而训练的网络学到这个得分（Song 及其同事，2021），对式 (48.5) 积分就把噪声变为数据分布的样本（见下图）。训练目标又是变分下界，与 VAE 一样，只是编码器固定（加噪过程）、解码器是学习得到的。在自编码器的隐空间中、以对比编码器的文本表征为条件的扩散模型，是当前图像生成器的基础；它们的方法这里不再讨论。

![用逆转扩散进行生成，式 (48.5)，一维数据分布为 $\pm 2$ 处两个标准差为 $0.3$ 的 Gauss 分布的混合（$t \in [0, 1]$ 上 $b = 6$；$p_t$ 的得分是精确计算的，因为 $p_t$ 仍是 Gauss 混合；1000 步的 Euler–Maruyama 方法，4000 个粒子）。A：加噪密度 $p_t(x)$（阴影）与 25 条反向轨迹：粒子在 $t = 1$ 从 $\mathcal{N}(0, 1)$ 出发，随 $t \to 0$ 被得分驱向两个峰之一；峰的选择作出得较晚，约在 $t \approx 0.3$。B：生成样本的分布与数据分布吻合。](./plots/diffusion-sampling.py)

对神经科学而言，扩散模型的意义与其说在于架构，不如说在于这样的想法：有噪声的递归网络的动力学可以实现采样。沿对数密度的梯度加噪声运动的随机系统，即 [7.6.5](/7.6.5) 的 **Langevin 方程**，以该密度为其平稳分布。*采样假说*（Hoyer and Hyvärinen, 2003；Fiser, Berkes, Orbán and Lengyel, 2010）提出，神经变异不只是噪声，而是表示不确定性：感觉群体在相继时刻的活动是来自成因后验的一串样本，所以反应的方差报告后验的宽度，这与 [定义 27.5.1](/7.16.27#def-27.5.1) 的**概率群体编码**不同，后者在平均反应中表示后验。一个预测是：没有输入时的自发活动对先验抽样：Berkes、Orbán、Lengyel 和 Fiser（2011）发现，雪貂 V1 自发活动期间多单元活动模式的分布，在发育过程中越来越类似于自然影片诱发的平均分布，而不类似于人工光栅诱发的分布。意象会激活早期视觉区，梦也是如此，它们是由**内部模型**生成的天然例子，但大脑是否使用扩散型的、噪声驱动的去噪动力学，尚不得而知。

## 小结

- 知觉可以表述为用识别模型 $q(\boldsymbol{z} \mid \boldsymbol{x})$ 对生成模型 $p(\boldsymbol{z})p(\boldsymbol{x} \mid \boldsymbol{z})$ 求逆（定义 48.1.1）；学习模型无需标签。Helmholtz 机用局部的醒–睡规则训练二者（定义 48.1.2，算法 48.1.1）。
- 经典的隐变量模型（因子分析、混合模型、稀疏编码）用 EM 拟合，其快速的推断与缓慢的学习步骤对应于活动与突触的变化（48.2）。

| 模型 | 识别 | 目标 | 神经对应（假说） |
|---|---|---|---|
| Helmholtz 机 | 自下而上的网络，在睡眠中训练 | 近似似然 | 醒相与离线相 |
| VAE、β-VAE | 编码器网络，Gauss 后验 | ELBO，式 (48.1)，容量 $\beta$ | 面孔细胞的解缠轴 |
| 预测编码 | 对误差的递归稳定 | Gauss 层级的后验，式 (48.3) | 误差单元、失配反应、反馈 |
| 对比 / JEPA | 仅编码器 | 视图的一致性，式 (48.4) | 慢性、IT 中的不变性学习 |
| 扩散 / 采样 | 去噪动力学 | 得分匹配，式 (48.5) | 作为样本的变异、作为先验的自发活动 |

- ELBO 等于对数证据减去后验散度（定理 48.3.1）。VAE（定义 48.3.2）联合学习生成模型与摊销的识别模型；β-VAE（定义 48.3.3）偏向解缠的隐变量。在线性情形下，最优解是噪声为 $\beta\sigma^2$ 的概率 PCA，$\beta$ 起率与失真的水位作用（命题 48.3.1）。
- 预测编码（定义 48.4.1，公式 48.4.1）通过向前传递预测误差、向后传递预测来实现推断；它解释端点抑制与失配反应，但专门的误差神经元是否存在尚有争论。自由能原理是建立在同一下界上的一般框架。
- 自监督目标（定义 48.5.1 与 48.5.2）学到能预测腹侧通路反应的表征；时间上的慢性是正样本对的生物来源。

## 思考题

1. 证明醒相更新 $\Delta w_{jk} = \eta(s_j - p_j)y_k$ 是 sigmoid 单元的 $\log p_{\boldsymbol{\theta}}(\boldsymbol{x}, \boldsymbol{z})$ 的梯度，并解释为什么睡相不对识别权重最大化 ELBO。

   **答** 在生成通路中，单元 $j$ 以概率 $p_j = \sigma(\sum_k w_{jk}y_k)$ 处于开启状态，其中 $y_k$ 是上一层的状态；它对 $\log p$ 的贡献是 $s_j\log p_j + (1 - s_j)\log(1 - p_j)$，因为 $\mathrm{d}\sigma(a)/\mathrm{d}a = \sigma(1 - \sigma)$，其对 $w_{jk}$ 的导数为 $(s_j - p_j)y_k$。对 $\boldsymbol{z} \sim q(\boldsymbol{z} \mid \boldsymbol{x})$ 取平均，这是 $\mathbb{E}_q\log p_{\boldsymbol{\theta}}(\boldsymbol{x}, \boldsymbol{z})$ 的梯度，即 ELBO 中依赖于 $\boldsymbol{\theta}$ 的部分。ELBO 对 $\boldsymbol{\phi}$ 的依赖来自 $-D_{\mathrm{KL}}(q\,\Vert\,p(\boldsymbol{z} \mid \boldsymbol{x}))$，它是对 $q$ 的期望，对二值单元难以求导。睡相转而最小化在幻想 $\boldsymbol{x} \sim p_{\boldsymbol{\theta}}$ 上平均的 $D_{\mathrm{KL}}(p(\boldsymbol{z} \mid \boldsymbol{x})\,\Vert\,q)$，即自变量颠倒的散度，并且以模型的数据而不是真实数据加权。两者只有在 $q$ 能精确匹配后验时才一致；否则，反向散度使 $q$ 覆盖后验的所有峰，而不是集中于一个。

2. 在命题 48.3.1 中，取数据方差 $\lambda = (6, 3, 1.5, 0.6, 0.2)$、$\sigma^2 = 0.4$。$\beta = 1$ 和 $\beta = 4$ 时各有多少个隐变量活跃？总率与总失真是多少？

   **答** 水位是 $\beta\sigma^2$。$\beta = 1$ 时为 $0.4$：四个本征值超过它，率为 $\frac12[\ln 15 + \ln 7.5 + \ln 3.75 + \ln 1.5] = \frac12\ln 632.8 \approx 3.23$ nats，失真为 $4 \times 0.4 + 0.2 = 1.8$。$\beta = 4$ 时水位为 $1.6$：两个本征值超过它，率为 $\frac12[\ln 3.75 + \ln 1.875] \approx 0.98$ nats，失真为 $2 \times 1.6 + 1.5 + 0.6 + 0.2 = 5.5$。这些是 48.3.3 图中 C 面板的标记点。

3. 在公式 48.4.1 的预测编码模型中，具有 Gauss 先验 $\boldsymbol{r} \sim \mathcal{N}(\boldsymbol{0}, \sigma_{\mathrm{p}}^2I)$ 的单层的稳态是什么？它与因子分析相比如何？毁损自上而下的连接会对误差单元产生什么影响？

   **答** 稳态时 $U^{\mathsf T}(\boldsymbol{x} - U\boldsymbol{r})/\sigma^2 = \boldsymbol{r}/\sigma_{\mathrm{p}}^2$，所以 $\boldsymbol{r} = (U^{\mathsf T}U + (\sigma^2/\sigma_{\mathrm{p}}^2)I)^{-1}U^{\mathsf T}\boldsymbol{x}$，这是线性 Gauss 模型的后验均值，也就是 48.2 节在 $W = \sigma_{\mathrm{p}}U$ 且噪声各向同性时的因子分析（概率 PCA）识别公式。网络通过递归松弛而不是矩阵求逆来计算同一个量。若去掉自上而下的预测，下一层的误差单元等于表征本身（$\boldsymbol{e}_{\ell - 1} = \boldsymbol{r}_{\ell - 1}$），所以预期与非预期的输入诱发相同的反应：端点抑制、周边抑制和失配反应应当消失，低级区域的活动应当增加。在一些研究中，沉默来自更高视觉区的反馈确实降低了 V1 的周边抑制，这个预测与其他反馈模型共有。

4. 有批评者认为对比学习不可能发生在大脑中，因为它需要负样本。给出生物系统获得"推开"项或避开它的两种方式。

   **答** (a) 负样本隐含在竞争中：群体内的侧向抑制与除法归一化，以及使每个神经元平均活动与反应方差保持固定的稳态可塑性，防止所有输入映射到同一个表征；这是 VICReg 和 Barlow Twins 的方差–协方差正则化，而不是显式的负样本。(b) 时间结构提供对比：相隔很长时间或隔着扫视与场景变化的输入平均而言互不相关，所以加强相继表征之间的一致性（慢性）、削弱时间上相距很远的表征之间的一致性的规则，就是以记忆痕迹中的样本作负样本的对比规则；两相方案则在由网络自身自发活动驱动的离线相中使可塑性符号相反（如醒–睡算法和对比 Hebb 学习），由模型本身提供负样本。
