---
title: 优化与训练技巧
description: 神经网络的损失曲面；二次函数上的梯度下降与条件数；带动量的 SGD 与 Nesterov 加速；AdaGrad、RMSProp、带偏差修正的 Adam 与 AdamW；Lion、Muon 等近期优化器；学习率调度（阶梯、余弦、预热–稳定–衰减）与预热；梯度消失与梯度爆炸、梯度裁剪；数据、批、层、实例、组归一化与 RMSNorm；随机失活等正则化方法；超参数选择的实用流程；NumPy 与 PyTorch 实现。
source_hash: f730d40484c6
---

**反向传播**（[4.7.2](/4.7.2)）给出了损失对每个权重的梯度，本章讨论如何使用这些梯度。训练深度网络，就是利用带噪声的梯度估计，极小化一个高维的非凸函数。对这样的函数，朴素的**随机梯度下降**很慢：它在狭窄的沟谷中来回震荡，沿平坦方向缓慢爬行，还需要精心选择学习率。三类技术使训练又快又稳。其一是更好的优化器，它们跨步累积信息，或是行进的方向（动量），或是各坐标的尺度（AdaGrad、RMSProp、Adam），Muon 等新方法甚至利用了权重的矩阵结构。其二是学习率调度，开头预热、结尾衰减，使步长适应训练的不同阶段。其三是改造网络本身，即归一化层与对梯度流的细致控制，使损失曲面从一开始就更易于优化。本章最后讨论随机失活等正则化方法，并给出选择**超参数**的实用流程。

**梯度下降**、线搜索与随机梯度下降的数学理论见 [3.5.4](/3.5.4) 与 [3.5.5](/3.5.5)；**正则化**、**权重衰减**、**早停**与超参数等概念来自 [4.7.1](/4.7.1)。这里的归一化与优化选择会在之后各章反复出现：层归一化与带预热的 Adam 是 Transformer（[4.7.6](/4.7.6)）不可分割的部分，优化器状态的内存开销则是大模型必须考虑的问题（[4.7.8](/4.7.8)）。

## 4.1. 作为优化问题的训练

### 4.1.1. 损失曲面

训练就是在参数 $\boldsymbol{\theta} \in \mathbb{R}^p$ 上极小化**训练误差** $E(\boldsymbol{\theta}) = \frac{1}{m}\sum_{i=1}^m E_i(\boldsymbol{\theta})$，其中 $p$ 从数千到数万亿不等。这个函数的若干特点决定了本章各种方法的设计。

- 非凸性。$E$ 不是权重的**凸函数**：置换某一层的隐藏单元不改变网络函数，所以每个极小点都有许多等价的副本，而两个副本之间的线段通常经过更高的损失。因此梯度方法只能找到临界点，问题在于找到的是哪一类临界点。
- 是**鞍点**而不是糟糕的局部极小点。在临界点处，除非它是局部极小点，**Hesse 矩阵** $\nabla^2 E$ 的特征值有正有负。启发式地看，在 $p$ 维空间中，随机临界点的 $p$ 个特征值全为正的概率极小；Dauphin 等人（2014）的实验发现，损失较高的临界点几乎都是**鞍点**，而局部极小点的损失往往接近全局极小值。梯度在鞍点附近很小，朴素的**梯度下降法**会因此变慢；噪声与动量有助于逃离鞍点。
- 病态性。即使在极小点附近，不同方向上的曲率也相差数个数量级：训练好的网络的 **Hesse 矩阵**有少数很大的特征值，其余的大量特征值接近零。在陡峭方向上稳定的步长，在平坦方向上就显得微不足道（§4.1.2）。
- 平坦极小点与尖锐极小点。训练损失相同的不同极小点，宽度可以不同。位于宽而平坦的盆地中的极小点，其泛化往往好于尖锐的极小点（Hochreiter 与 Schmidhuber 1997；Keskar 等 2017），锐度感知最小化（Foret 等 2021）即基于这一观察；不过锐度在重新参数化下并不不变，这一联系也不是定理。

Li 等人（2018）将损失曲面可视化：在训练得到的解 $\boldsymbol{\theta}^*$ 附近沿两个随机方向画出 $E(\boldsymbol{\theta}^* + \alpha\boldsymbol{d}_1 + \beta\boldsymbol{d}_2)$，方向按滤波器逐个归一化到权重的尺度。对于 ResNet-56，曲面在极小点附近光滑且近似凸；去掉**跳跃连接**后曲面变得混乱，出现许多尖锐的局部极小点，网络越深越明显。因此，架构设计（**残差连接**、归一化）同时也是对损失曲面的设计。另一个出人意料的发现是，**随机梯度下降** 从不同初始化出发找到的极小点，通常可以用损失几乎恒定且很低的简单曲线连接起来（模式连通性（mode connectivity），Garipov 等 2018；Draxler 等 2018）。

### 4.1.2. 二次函数上的梯度下降

在极小点附近，$E$ 近似为二次函数，这个二次模型解释了一阶方法的大部分困难。设 $E(\boldsymbol{w}) = \frac12\boldsymbol{w}^{\mathsf T}H\boldsymbol{w}$，其中 $H$ 对称正定，特征值满足 $0 < \mu = \lambda_{\min} \le \dots \le \lambda_{\max} = L$，**条件数**为 $\kappa = L/\mu$。学习率为 $\eta$ 的**梯度下降法**迭代 $\boldsymbol{w}_{t+1} = \boldsymbol{w}_t - \eta H\boldsymbol{w}_t = (I - \eta H)\boldsymbol{w}_t$。

**命题 4.1.1** 对 $E(\boldsymbol{w}) = \frac12\boldsymbol{w}^{\mathsf T}H\boldsymbol{w}$，梯度下降从任意初始点出发都收敛到 $\boldsymbol{0}$，当且仅当 $0 < \eta < 2/L$。最优收敛速率在 $\eta = 2/(L + \mu)$ 时取到，此时
$$
\|\boldsymbol{w}_t\| \le \left(\frac{\kappa - 1}{\kappa + 1}\right)^t\|\boldsymbol{w}_0\| .
$$

**证明** 在 $H$ 的标准正交特征基下写 $\boldsymbol{w}_0 = \sum_i c_i\boldsymbol{u}_i$，其中 $H\boldsymbol{u}_i = \lambda_i\boldsymbol{u}_i$。则 $\boldsymbol{w}_t = \sum_i(1 - \eta\lambda_i)^tc_i\boldsymbol{u}_i$，它对所有 $c_i$ 都趋于 $\boldsymbol{0}$，当且仅当对每个 $i$ 有 $\lvert 1 - \eta\lambda_i\rvert < 1$，即 $0 < \eta\lambda_i < 2$；起约束作用的是 $\eta < 2/L$。范数的压缩因子为 $\rho(\eta) = \max_i\lvert 1 - \eta\lambda_i\rvert = \max(\lvert 1 - \eta\mu\rvert, \lvert 1 - \eta L\rvert)$，即 $I - \eta H$ 的**谱半径**。这是 $\eta$ 的一个递减函数与一个递增函数的最大值，在 $1 - \eta\mu = \eta L - 1$ 处最小，即 $\eta = 2/(L + \mu)$，最小值为 $(L - \mu)/(L + \mu) = (\kappa - 1)/(\kappa + 1)$。$\square$

学习率受最陡方向限制，沿最平坦方向的进展则由 $1 - 2/(\kappa + 1) \approx 1 - 2/\kappa$ 决定：误差缩小到原来的 $1/\mathrm{e}$ 大约需要 $\kappa/2$ 步。神经网络中常见 $\kappa = 10^4$，这意味着每缩小一个因子就要数千步。在陡峭方向上，迭代会越过极小点，并在每一步都改变符号（当 $\eta > 1/L$ 时），即 §4.3.6 的图中可见的沟谷中的锯齿形路径。下面的每种方法都针对这一点：或是平滑震荡（动量），或是重新缩放坐标（自适应方法、归一化），或是重塑损失曲面（架构与初始化）。在真实的网络中，曲率在训练中也会变化：学习率固定时，全批量梯度下降倾向于使 Hessian 的最大特征值增大，直到在 $2/\eta$ 附近徘徊，即稳定性边缘（edge of stability）（Cohen 等 2021），此时损失长期来看仍在下降，只是不再单调。

### 4.1.3. SGD 的实践

**随机梯度下降**（[3.5.5](/3.5.5)）以**小批量梯度下降**的形式，用随机批 $\mathcal{B}_t$（含 $B$ 个样例）上的平均梯度代替 $\nabla E$：
$$
\boldsymbol{g}_t = \frac{1}{B}\sum_{i \in \mathcal{B}_t}\nabla E_i(\boldsymbol{\theta}_{t-1}), \qquad \boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta_t\boldsymbol{g}_t .
$$
$\boldsymbol{g}_t$ 是 $\nabla E$ 的无偏估计，其协方差是单个样例梯度协方差的 $1/B$（有放回抽样时）。与全批量梯度下降相比，SGD 每步的计算量为其 $B/m$，只需为一个批存储内存，可以在流数据上在线使用，其噪声还有助于逃离鞍点与尖锐极小点。它的弱点是 §4.1.2 的沟谷行为（现在还带着噪声），以及为了收敛必须减小学习率：学习率 $\eta$ 恒定时，迭代点会在极小点周围的一个区域内波动，区域大小随 $\eta/B$ 增大。

样例的顺序很重要。若数据按某种有意义的顺序存放（按类别、日期或来源排序），连续的批就缺乏代表性，梯度会在很长一段时间内有偏，足以破坏收敛；在按数字排序的 MNIST 上训练的分类器，学到的只是预测当前的数字而忘掉其他数字。标准的补救办法是每个轮次前打乱**训练集**，并无放回地取批。对于只在数万亿**词元**上训练一遍的语言模型，数据混合只打乱一次，而各数据来源的先后顺序本身就是设计选择（以高质量数据收尾的课程学习很常见，[4.7.9](/4.7.9)）。

## 4.2. 动量

### 4.2.1. 指数移动平均

本章所有的优化器都保存梯度统计量的滑动平均。对序列 $\boldsymbol{x}_1, \boldsymbol{x}_2, \dots$ 与 $\beta \in [0, 1)$，指数移动平均（exponential moving average）定义为 $\boldsymbol{a}_0 = \boldsymbol{0}$ 与
$$
\boldsymbol{a}_t = \beta\boldsymbol{a}_{t-1} + (1 - \beta)\boldsymbol{x}_t = (1 - \beta)\sum_{k=1}^t\beta^{t-k}\boldsymbol{x}_k .
$$
权重随时间远近几何衰减，平均实际覆盖最近的 $1/(1 - \beta)$ 项：$\beta = 0.9$ 大约平均 $10$ 步，$\beta = 0.999$ 大约平均 $1000$ 步。权重之和是 $1 - \beta^t$ 而不是 $1$，所以在最初的 $1/(1 - \beta)$ 步内，平均值偏向初始值 $\boldsymbol{0}$；Adam 修正了这一偏差（§4.3.3）。

### 4.2.2. 动量法

**梯度下降法**没有记忆：每一步只取决于当前梯度。在沟谷中，相邻的梯度在横跨沟谷的方向上几乎相反，沿沟谷的方向则一致。将它们平均，可以抵消震荡，累积一致的分量，就像一个沉重的球滚下山坡。

**定义 4.2.1（动量法）** 学习率为 $\eta$、动量系数为 $\beta \in [0, 1)$ 的带**动量**的梯度下降（Polyak 1964 的重球法）保存一个速度 $\boldsymbol{v}$，初值 $\boldsymbol{v}_0 = \boldsymbol{0}$，迭代
$$
\boldsymbol{v}_t = \beta\boldsymbol{v}_{t-1} + \boldsymbol{g}_t, \qquad \boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta\boldsymbol{v}_t ,
$$
其中 $\boldsymbol{g}_t$ 是 $\boldsymbol{\theta}_{t-1}$ 处的（随机）梯度。等价地，$\boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta\boldsymbol{g}_t + \beta(\boldsymbol{\theta}_{t-1} - \boldsymbol{\theta}_{t-2})$。

常用的取值是 $\beta = 0.9$。速度是梯度的指数移动平均的 $1/(1 - \beta)$ 倍，所以在恒定梯度 $\boldsymbol{g}$ 下，步长趋于 $\eta\boldsymbol{g}/(1 - \beta)$：沿一致的方向，动量把有效学习率放大为 $\beta = 0.9$ 时的 $10$ 倍，而震荡的分量则大多相互抵消。（有些库写成 $\boldsymbol{v}_t = \beta\boldsymbol{v}_{t-1} + (1 - \beta)\boldsymbol{g}_t$，这只是改变了 $\eta$ 的尺度；PyTorch 的 `SGD(momentum=0.9)` 使用上面的形式。）在二次函数上，收益可以定量计算。

**定理 4.2.1** 设 $E(\boldsymbol{w}) = \frac12\boldsymbol{w}^{\mathsf T}H\boldsymbol{w}$ 的特征值在 $[\mu, L]$ 内，$\kappa = L/\mu$。取
$$
\eta = \frac{4}{(\sqrt L + \sqrt\mu)^2}, \qquad \beta = \left(\frac{\sqrt\kappa - 1}{\sqrt\kappa + 1}\right)^2
$$
则重球法满足 $\|\boldsymbol{w}_t\| \le C_t\left(\frac{\sqrt\kappa - 1}{\sqrt\kappa + 1}\right)^t\|\boldsymbol{w}_0\|$，其中 $C_t$ 至多随 $t$ 线性增长（Polyak 1964）。

每步的压缩因子从约 $1 - 2/\kappa$ 改善为约 $1 - 2/\sqrt\kappa$：对于 $\kappa = 10^4$，误差每缩小一个因子 $\mathrm{e}$ 所需的步数约从 $5000$ 降到 $50$。证明与命题 4.1.1 一样先对角化 $H$，再对每个特征值分析关于 $(w_t, w_{t-1})$ 的 $2 \times 2$ 线性递推，在这组参数下它的特征值模长都是 $\sqrt\beta$。对一般的非二次函数，重球法没有这样的保证，但它在**深度学习**中表现稳健；取 $\beta = 0.9$ 并配合衰减的学习率，它仍是许多卷积网络的首选优化器。

### 4.2.3. Nesterov 加速梯度法

动量法先计算梯度再加上速度。Nesterov 的变体颠倒了顺序：既然参数反正要移动 $-\eta\beta\boldsymbol{v}_{t-1}$，就在这个前瞻点处计算梯度，这样是在越过极小点之前而不是之后修正速度。

**定义 4.2.2（Nesterov 加速梯度法）** **Nesterov 加速梯度法**（NAG）迭代
$$
\boldsymbol{v}_t = \beta\boldsymbol{v}_{t-1} + \nabla E\bigl(\boldsymbol{\theta}_{t-1} - \eta\beta\boldsymbol{v}_{t-1}\bigr), \qquad \boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta\boldsymbol{v}_t .
$$

对于梯度为 $L$-Lipschitz 的光滑**凸函数**，Nesterov（1983）证明，取 $\beta_t = (t - 1)/(t + 2)$ 的调度可得 $E(\boldsymbol{\theta}_t) - E^* = O(L\|\boldsymbol{\theta}_0 - \boldsymbol{\theta}^*\|^2/t^2)$，而梯度下降只有 $O(1/t)$，并且在最坏情形下，只用梯度的方法都不能做得更好；对强凸函数，它无需二次性就达到定理 4.2.1 的 $1 - 1/\sqrt\kappa$ 速率。Sutskever 等人（2013）表明，动量与 Nesterov 动量配合适当的调度，训练深度网络与循环网络的效果远好于朴素的 **随机梯度下降**。实现中通过变量替换避免第二次梯度计算：PyTorch 的 `SGD(nesterov=True)` 先算 $\boldsymbol{v}_t = \beta\boldsymbol{v}_{t-1} + \boldsymbol{g}_t$，再以 $-\eta(\boldsymbol{g}_t + \beta\boldsymbol{v}_t)$ 更新，这正是用前瞻点表示的 NAG。

## 4.3. 自适应学习率

动量法仍对所有参数使用同一个学习率。但参数的梯度大小差别极大：罕见词的嵌入只在该词出现时才有梯度，不同层的权重尺度不同，而 §4.1.2 的病态性在一定程度上就是坐标尺度的问题。自适应方法把每个坐标的步长除以其梯度大小的滑动估计。

### 4.3.1. AdaGrad

**定义 4.3.1（AdaGrad）** **AdaGrad**（Duchi、Hazan 与 Singer 2011）累积梯度的平方，$\boldsymbol{s}_0 = \boldsymbol{0}$，
$$
\boldsymbol{s}_t = \boldsymbol{s}_{t-1} + \boldsymbol{g}_t \odot \boldsymbol{g}_t, \qquad \boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \frac{\eta}{\sqrt{\boldsymbol{s}_t} + \varepsilon} \odot \boldsymbol{g}_t ,
$$
其中平方根与除法逐分量进行，$\varepsilon$（例如 $10^{-10}$）用来避免除以零。

第 $i$ 个坐标的有效学习率为 $\eta/\sqrt{\sum_{k \le t}g_{k,i}^2}$：梯度小或罕见的参数迈出更大的步子。这对稀疏问题很理想，例如词袋特征上的线性模型或词嵌入，而且 AdaGrad 对在线凸优化有遗憾界保证。对深度网络而言，它的弱点是 $\boldsymbol{s}_t$ 只增不减，有效学习率按 $1/\sqrt t$ 衰减，即使曲面已经变化、更大的步长本来有用，训练也会过早停滞。

### 4.3.2. RMSProp

**定义 4.3.2（RMSProp）** **RMSProp**（Hinton，课程讲义 2012）将 AdaGrad 的求和换成衰减率为 $\rho$（通常取 $0.9$ 或 $0.99$）的指数移动平均：
$$
\boldsymbol{s}_t = \rho\boldsymbol{s}_{t-1} + (1 - \rho)\,\boldsymbol{g}_t \odot \boldsymbol{g}_t, \qquad \boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \frac{\eta}{\sqrt{\boldsymbol{s}_t} + \varepsilon} \odot \boldsymbol{g}_t .
$$

分母现在是近期梯度的滑动均方根，所以有效学习率适应每个坐标当前的尺度，在梯度变小时还能重新增大。除以均方根使更新近似不受损失缩放的影响，且无论梯度尺度如何，每个坐标的更新幅度大致都是 $\eta$；在 $\rho \to 0$ 的极限下，更新变为 $\eta\operatorname{sgn}(\boldsymbol{g}_t)$，即符号下降。RMSProp 从未以论文发表，它是在 Hinton 的 Coursera 课程中提出的，后来成为循环网络和**强化学习**的标准方法（最初的 DQN 就是用它训练的）。

### 4.3.3. Adam

Adam 结合了两种思想：用动量确定方向，用 RMSProp 确定尺度，并修正两个滑动平均的初始化偏差。

**算法 4.3.1（Adam）** Adam（adaptive moment estimation；Kingma 与 Ba 2015）的学习率为 $\eta$，衰减率为 $\beta_1, \beta_2 \in [0, 1)$，另有 $\varepsilon > 0$（默认值 $\beta_1 = 0.9$，$\beta_2 = 0.999$，$\varepsilon = 10^{-8}$）。从 $\boldsymbol{m}_0 = \boldsymbol{v}_0 = \boldsymbol{0}$ 出发，在第 $t = 1, 2, \dots$ 步，设梯度为 $\boldsymbol{g}_t$，计算

$$
\begin{aligned}
\boldsymbol{m}_t &= \beta_1\boldsymbol{m}_{t-1} + (1 - \beta_1)\boldsymbol{g}_t, &\qquad \hat{\boldsymbol{m}}_t &= \frac{\boldsymbol{m}_t}{1 - \beta_1^t}, \\
\boldsymbol{v}_t &= \beta_2\boldsymbol{v}_{t-1} + (1 - \beta_2)\,\boldsymbol{g}_t \odot \boldsymbol{g}_t, &\qquad \hat{\boldsymbol{v}}_t &= \frac{\boldsymbol{v}_t}{1 - \beta_2^t}, \\
\boldsymbol{\theta}_t &= \boldsymbol{\theta}_{t-1} - \eta\,\frac{\hat{\boldsymbol{m}}_t}{\sqrt{\hat{\boldsymbol{v}}_t} + \varepsilon} . && 
\end{aligned}
$$

$\boldsymbol{m}_t$ 估计每个梯度分量的一阶矩（均值），$\boldsymbol{v}_t$ 估计二阶矩（未中心化的方差）。

**命题 4.3.1** 若梯度 $\boldsymbol{g}_1, \dots, \boldsymbol{g}_t$ 有共同的均值 $\mathbb{E}[\boldsymbol{g}_k] = \bar{\boldsymbol{g}}$ 与共同的二阶矩 $\mathbb{E}[\boldsymbol{g}_k \odot \boldsymbol{g}_k] = \bar{\boldsymbol{s}}$，则 $\mathbb{E}[\boldsymbol{m}_t] = (1 - \beta_1^t)\bar{\boldsymbol{g}}$，$\mathbb{E}[\boldsymbol{v}_t] = (1 - \beta_2^t)\bar{\boldsymbol{s}}$，因而 $\hat{\boldsymbol{m}}_t$ 与 $\hat{\boldsymbol{v}}_t$ 是无偏的。

**证明** 展开递推式得 $\boldsymbol{m}_t = (1 - \beta_1)\sum_{k=1}^t\beta_1^{t-k}\boldsymbol{g}_k$，由线性性及等比数列求和，$\mathbb{E}[\boldsymbol{m}_t] = (1 - \beta_1)\bar{\boldsymbol{g}}\sum_{j=0}^{t-1}\beta_1^j = (1 - \beta_1^t)\bar{\boldsymbol{g}}$。对 $\boldsymbol{v}_t$ 作同样的计算即可。$\square$

没有这一修正，最初几步会被扭曲，而且不只是差一个小因子：在 $t = 1$ 时，$\boldsymbol{m}_1 = (1 - \beta_1)\boldsymbol{g}_1$，$\boldsymbol{v}_1 = (1 - \beta_2)\boldsymbol{g}_1^2$，所以用默认值时，未修正的步长是每个坐标 $\eta(1 - \beta_1)/\sqrt{1 - \beta_2} \approx 3.16\eta$，因为 $\boldsymbol{v}$ 的偏差比 $\boldsymbol{m}$ 大得多。修正后第一步为 $\eta\operatorname{sgn}(\boldsymbol{g}_1)$（至多差 $\varepsilon$），这可以在 §4.3.5 的输出中看到。下面几条性质说明了 Adam 为什么成为**深度学习**的默认优化器。

- 尺度：无论梯度的尺度如何，每个坐标每步的移动量大致不超过 $\eta$，所以 $\eta$ 是参数空间中的步长，一个取值（小网络约 $10^{-3}$，大型 Transformer 为 $10^{-4}$ 到 $3 \times 10^{-4}$）就能适用于许多问题。
- 不变性：损失乘以常数，更新不变（至多差 $\varepsilon$），而且方法对参数的对角缩放也不变。
- 信噪比：对梯度主要是噪声的坐标，比值 $\hat{\boldsymbol{m}}/\sqrt{\hat{\boldsymbol{v}}}$ 很小，对梯度一致的坐标则接近 $\pm 1$，这在极小点附近起到自动退火的作用。

Adam 并非万能。Reddi、Kale 与 Kumar（2018）构造了 Adam 不收敛的凸问题，原因是一个大梯度离开平均窗口后，有效学习率 $\eta/\sqrt{\hat v}$ 可能增大；AMSGrad 通过使用 $\boldsymbol{v}_t$ 的历史最大值解决了这个问题，不过实践中原始的 Adam 通常同样有效。在 **卷积神经网络** 的图像分类上，调好的带动量 **随机梯度下降** 往往泛化得略好一些（Wilson 等 2017），而对 Transformer，Adam 必不可少：它们的梯度是重尾的，且不同参数块之间尺度不同，SGD 训练它们的效果很差。对于大语言模型，常用的设置是 $\beta_1 = 0.9$，$\beta_2 = 0.95$（二阶矩窗口更短，对梯度尖峰反应更快），$\varepsilon = 10^{-8}$，以及 $0.1$ 的解耦**权重衰减**。Adam 为每个参数多存两个数；对于采用混合精度训练、有 $N$ 个参数的模型，这占训练状态约 $16N$ 字节中的 $8N$（[4.7.8](/4.7.8)）。

### 4.3.4. AdamW 与解耦权重衰减

对于**梯度下降法**，在损失中加上惩罚项 $\frac{\lambda}{2}\|\boldsymbol{\theta}\|^2$，与每步把权重乘以 $1 - \eta\lambda$ 收缩，是一回事（**权重衰减**，[4.7.1](/4.7.1)）。对自适应方法则不然。在 Adam 归一化之前把 $\lambda\boldsymbol{\theta}$ 加到梯度上，惩罚项会被除以 $\sqrt{\hat{\boldsymbol{v}}}$，于是梯度大的参数几乎不受正则化，梯度小的参数却被强烈正则化，这并不符合惩罚项的本意；实验上，Adam 中的 $L^2$ **正则化**远不如 SGD 中有效。

**定义 4.3.3（AdamW）** **AdamW**（Loshchilov 与 Hutter 2019）把权重衰减直接作用于参数，放在自适应归一化之外：
$$
\boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta_t\left(\frac{\hat{\boldsymbol{m}}_t}{\sqrt{\hat{\boldsymbol{v}}_t} + \varepsilon} + \lambda\boldsymbol{\theta}_{t-1}\right),
$$
其中 $\boldsymbol{m}_t$、$\boldsymbol{v}_t$ 由未正则化损失的梯度按算法 4.3.1 计算。

现在每个参数都以相同的相对速率 $\eta_t\lambda$ 逐步收缩，与其梯度历史无关，最优的 $\lambda$ 也基本不再依赖学习率。AdamW 是 Transformer 的标准优化器。在 PyTorch 中，`torch.optim.AdamW(params, lr, weight_decay=λ)` 在 Adam 步之前先把权重乘以 $1 - \eta_t\lambda$，所以衰减随学习率调度而变化。偏置、归一化的增益参数，通常还有嵌入，一般不做权重衰减，做法是把它们放进另一个 `weight_decay=0` 的参数组。

### 4.3.5. 实现

下面的类实现带可选解耦权重衰减的一步 Adam，并在 Rosenbrock 函数 $f(x, y) = (1 - x)^2 + 100(y - x^2)^2$ 上运行，它的极小点 $(1, 1)$ 位于一条弯曲狭窄的山谷底部。

```python
import numpy as np


class Adam:
    """Adam with decoupled weight decay (AdamW when weight_decay > 0)."""

    def __init__(self, params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=0.0):
        self.params, self.lr, self.eps, self.wd = params, lr, eps, weight_decay
        self.b1, self.b2 = betas
        self.m = [np.zeros_like(p) for p in params]   # first moment (mean of gradients)
        self.v = [np.zeros_like(p) for p in params]   # second moment (mean of squared gradients)
        self.t = 0

    def step(self, grads):
        self.t += 1
        for p, g, m, v in zip(self.params, grads, self.m, self.v):
            m *= self.b1
            m += (1 - self.b1) * g
            v *= self.b2
            v += (1 - self.b2) * g * g
            m_hat = m / (1 - self.b1 ** self.t)        # bias correction
            v_hat = v / (1 - self.b2 ** self.t)
            p -= self.lr * self.wd * p                 # decoupled weight decay (in place)
            p -= self.lr * m_hat / (np.sqrt(v_hat) + self.eps)


def rosenbrock(w):
    x, y = w
    f = (1 - x) ** 2 + 100 * (y - x ** 2) ** 2
    g = np.array([-2 * (1 - x) - 400 * x * (y - x ** 2), 200 * (y - x ** 2)])
    return f, g


for lr in (0.01, 0.05):
    w = np.array([-1.5, 2.0])
    opt = Adam([w], lr=lr)
    for t in range(1, 5001):
        f, g = rosenbrock(w)
        opt.step([g])
        if t in (1, 100, 1000, 5000):
            print(f"lr {lr}  step {t:4d}  w = ({w[0]: .4f}, {w[1]: .4f})  f = {rosenbrock(w)[0]:.2e}")
```

```text
lr 0.01  step    1  w = (-1.4900,  2.0100)  f = 1.06e+01
lr 0.01  step  100  w = (-1.4050,  1.9804)  f = 5.79e+00
lr 0.01  step 1000  w = ( 0.0674,  0.0040)  f = 8.70e-01
lr 0.01  step 5000  w = ( 1.0000,  1.0000)  f = 1.68e-17
lr 0.05  step    1  w = (-1.4500,  2.0500)  f = 6.28e+00
lr 0.05  step  100  w = (-1.2673,  1.6125)  f = 5.14e+00
lr 0.05  step 1000  w = ( 0.9818,  0.9638)  f = 3.33e-04
lr 0.05  step 5000  w = ( 0.9962,  0.9923)  f = 1.56e-05
```

第一步使每个坐标恰好移动一个学习率，正如命题 4.3.1 之后计算的那样。较大的学习率更快到达谷底，但随后在极小点附近持续波动，较小的学习率则收敛到机器精度：学习率恒定时，最终精度受步长限制，这正是学习率衰减（§4.4）要解决的问题。同一个类在浮点舍入误差范围内复现了 PyTorch 的 `AdamW`（PyTorch 2.14，CPU）：

```python
import numpy as np
import torch

torch.manual_seed(0)
model = torch.nn.Linear(10, 1)
X, y = torch.randn(256, 10), torch.randn(256, 1)
ref = [p.detach().numpy().copy() for p in model.parameters()]   # NumPy copy of the weights
opt_t = torch.optim.AdamW(model.parameters(), lr=1e-2, weight_decay=0.1)
opt_n = Adam(ref, lr=1e-2, weight_decay=0.1)                      # the class defined above
for step in range(100):
    loss = torch.nn.functional.mse_loss(model(X), y)
    opt_t.zero_grad()
    loss.backward()
    opt_n.step([p.grad.numpy().astype(np.float64) for p in model.parameters()])
    opt_t.step()
diff = max(np.abs(p.detach().numpy() - r).max() for p, r in zip(model.parameters(), ref))
print(f"loss {loss.item():.4f}, max |torch - numpy| = {diff:.1e}")
```

```text
loss 0.8104, max |torch - numpy| = 4.0e-07
```

### 4.3.6. 比较

下图在一个病态二次函数和 Rosenbrock 函数上运行本节的各种方法，每种方法的学习率都针对该问题手工调好。

![五种优化器在两个测试函数上的轨迹。左：在条件数为 25 的二次函数上，梯度下降在谷中锯齿形前进，动量法与 Nesterov 法越过极小点后螺旋收敛，RMSProp 与 Adam 重新缩放坐标，几乎径直走向极小点。中、右：在 Rosenbrock 函数上，所有方法都先下降到弯曲的山谷中；沿谷底前进时 Adam 收敛最快，动量法与 Nesterov 法其次，学习率恒定的 RMSProp 停在噪声底，梯度下降最慢](./plots/optimizer-trajectories.py)

图像与上面的分析吻合：动量沿山谷方向有帮助，自适应缩放消除了病态性中与坐标轴对齐的部分，而 Adam 兼具二者。但这只是网络训练的一幅漫画：真实训练中梯度带噪声，维数极高，病态性也不与坐标轴对齐。精心调参的基准测试（Schmidt 等 2021；AlgoPerf 竞赛，Dahl 等 2023）发现，调好的各优化器之间的差异，往往小于调节学习率及其调度的效果，并且 Adam 类方法在各类任务上最为稳健。实践中：若愿意调节调度，卷积网络用动量 $0.9$ 的 SGD；Transformer 以及一般情形默认用 AdamW。

### 4.3.7. Lion

优化器的研究依然活跃，因为优化器的效率直接决定大模型的训练成本。2026 年有四个突出的方向：基于符号的方法、正交化更新、矩阵预条件子与无调度平均。Chen 等人（2023）通过符号程序搜索发现了如下更新：
$$
\boldsymbol{c}_t = \beta_1\boldsymbol{m}_{t-1} + (1 - \beta_1)\boldsymbol{g}_t, \qquad \boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta\bigl(\operatorname{sgn}(\boldsymbol{c}_t) + \lambda\boldsymbol{\theta}_{t-1}\bigr), \qquad \boldsymbol{m}_t = \beta_2\boldsymbol{m}_{t-1} + (1 - \beta_2)\boldsymbol{g}_t ,
$$
其中 $\beta_1 = 0.9$，$\beta_2 = 0.99$，符号函数逐分量取。Lion（"evolved sign momentum"）只保存一个状态向量，而 Adam 要保存两个，并且每个坐标恰好移动 $\pm\eta$（外加衰减），所以它需要比 AdamW 小 $3$ 到 $10$ 倍的学习率，权重衰减则相应更大。它在最初的视觉与语言实验中持平或略优于 AdamW；后来的大规模比较发现收益很小。

### 4.3.8. Muon

Adam 把权重矩阵看作一堆相互独立的数。Muon（"MomentUm Orthogonalized by Newton–Schulz"；Jordan 等 2024）则把它看作线性映射。对每个二维权重矩阵 $W$，设其梯度为 $G_t$，先计算动量矩阵 $M_t = \mu M_{t-1} + G_t$（$\mu = 0.95$，通常取 Nesterov 形式），把 $M_t$ 换成它的正交极因子，再沿其方向更新：
$$
O_t = \operatorname{orth}(M_t) = UV^{\mathsf T} \quad\text{where } M_t = U\Sigma V^{\mathsf T}, \qquad W_t = W_{t-1} - \eta\,(s\,O_t + \lambda W_{t-1}),
$$
其中 $U\Sigma V^{\mathsf T}$ 是约化的**奇异值分解**，$s$ 是与形状有关的尺度（例如 $0.2\sqrt{\max(n_{\mathrm{out}}, n_{\mathrm{in}})}$，它使更新的均方根与 AdamW 的相当，因而可以沿用 AdamW 的学习率与权重衰减，Liu 等 2025）。正交化把更新的所有**奇异值**都置为 $1$：梯度小但一致的方向被放大，占主导的方向被抑制。它有一个干净的解释：谱范数下的最速下降。

**命题 4.3.2** 设 $G \in \mathbb{R}^{m \times n}$ 的约化**奇异值分解**为 $G = U\Sigma V^{\mathsf T}$，其中 $\Sigma = \operatorname{diag}(\sigma_1, \dots, \sigma_r)$，$\sigma_i > 0$。在所有谱范数 $\|\Delta\|_2 \le 1$ 的 $\Delta \in \mathbb{R}^{m \times n}$ 中，**Frobenius 内积** $\langle G, \Delta\rangle = \operatorname{tr}(G^{\mathsf T}\Delta)$ 在 $\Delta = -UV^{\mathsf T}$ 处取得最小值 $-\sum_i\sigma_i$。

**证明** 设 $U$ 的列为 $\boldsymbol{u}_i$，$V$ 的列为 $\boldsymbol{v}_i$，则 $\langle G, \Delta\rangle = \sum_i\sigma_i\langle\boldsymbol{u}_i\boldsymbol{v}_i^{\mathsf T}, \Delta\rangle = \sum_i\sigma_i\,\boldsymbol{u}_i^{\mathsf T}\Delta\boldsymbol{v}_i$。每一项都满足 $\lvert\boldsymbol{u}_i^{\mathsf T}\Delta\boldsymbol{v}_i\rvert \le \|\boldsymbol{u}_i\|\,\|\Delta\boldsymbol{v}_i\| \le \|\Delta\|_2 \le 1$，所以 $\langle G, \Delta\rangle \ge -\sum_i\sigma_i$。对 $\Delta = -UV^{\mathsf T}$（它的谱范数为 $1$），由标准正交性，$\boldsymbol{u}_i^{\mathsf T}\Delta\boldsymbol{v}_i = -\boldsymbol{u}_i^{\mathsf T}UV^{\mathsf T}\boldsymbol{v}_i = -1$，界被取到。$\square$

梯度下降是 Frobenius 范数下类似的最速下降（步长 $-G/\|G\|_{\mathrm{F}}$），而符号下降，即 Adam 的极限情形，是最大范数下的最速下降（Bernstein 与 Newhouse 2024）。谱范数是权重矩阵的自然范数，因为它界定了该层最多能把输出改变多少，$\|\Delta\boldsymbol{x}\| \le \|\Delta\|_2\|\boldsymbol{x}\|$。在 GPU 上每步计算 SVD 太慢，所以 Muon 用奇多项式 $X \leftarrow aX + b(XX^{\mathsf T})X + c(XX^{\mathsf T})^2X$ 的几次迭代来近似 $UV^{\mathsf T}$，该多项式分别作用于每个奇异值，把它推向 $1$（这是一种 Newton–Schulz 迭代，系数经过调节，以收敛得快而不是收敛得精确为目标）：

```python
import numpy as np


def newton_schulz(G, steps=5, coeffs=(3.4445, -4.7750, 2.0315), eps=1e-7):
    """Approximate the orthogonal polar factor U V^T of G = U S V^T (as in Muon)."""
    a, b, c = coeffs
    X = G / (np.linalg.norm(G) + eps)          # Frobenius normalization: singular values <= 1
    transposed = X.shape[0] > X.shape[1]
    if transposed:                              # iterate on the wide orientation (cheaper)
        X = X.T
    for _ in range(steps):
        A = X @ X.T
        X = a * X + (b * A + c * A @ A) @ X     # odd quintic polynomial applied to singular values
    return X.T if transposed else X


rng = np.random.default_rng(0)
G = rng.standard_normal((64, 32)) @ np.diag(np.logspace(0, -3, 32))   # ill-conditioned "gradient"
O = newton_schulz(G)
U, s, Vt = np.linalg.svd(G, full_matrices=False)
print("singular values of G:      ", np.round(s[[0, 8, 16, 24, 31]], 4))
print("singular values of NS5(G): ", np.round(np.linalg.svd(O, compute_uv=False)[[0, 8, 16, 24, 31]], 3))
print("relative distance to U V^T:", round(np.linalg.norm(O - U @ Vt) / np.linalg.norm(U @ Vt), 3))
```

```text
singular values of G:       [7.3526e+00 1.1990e+00 1.9210e-01 2.7800e-02 6.2000e-03]
singular values of NS5(G):  [1.176 1.073 0.783 0.708 0.249]
relative distance to U V^T: 0.303
```

五次迭代把跨越三个数量级的奇异值压缩到约 $0.25$ 至 $1.2$ 的范围；结果并不严格正交，但事实证明这无关紧要。Muon 只用于隐藏层的矩阵；嵌入、输出层、偏置与归一化的增益参数仍用 AdamW 训练。它于 2024 年提出，用来刷新小型语言模型的训练速度纪录，并由月之暗面（Moonshot AI；Liu 等 2025）证明可以扩展到大规模，他们报告其计算效率约为 AdamW 的两倍；月之暗面 2025 年发布的 Kimi K2 是一个拥有一万亿参数的混合专家模型，它用 Muon 的一个变体（MuonClip）训练，该变体还重新缩放查询与键的投影，以防止注意力 logit 爆炸。PyTorch 内置了 `torch.optim.Muon`（本章使用 2.14 版），默认使用动量 $0.95$、Nesterov 动量与上面的系数。

### 4.3.9. 预条件方法与无调度方法

Shampoo（Gupta、Koren 与 Singer 2018）用累积矩阵 $\sum G_tG_t^{\mathsf T}$ 与 $\sum G_t^{\mathsf T}G_t$ 的逆四次方根对每个权重矩阵做预条件，是全矩阵 AdaGrad 的 Kronecker 分解近似；去掉累积后，它就退化为 Muon 的正交化更新。SOAP（Vyas 等 2024）在 Shampoo 预条件子的特征基下运行 Adam。Shampoo 的一个分布式实现赢得了 2024 年 AlgoPerf 竞赛的外部调参赛道。

无调度方法（Defazio 等 2024）用迭代平均与插值的组合取代学习率调度，无需预先指定训练长度，就能达到调好的衰减调度的性能；无调度 AdamW 赢得了 AlgoPerf 的自调参赛道。

尽管有这些进展，2026 年 AdamW 仍是大模型最常用的优化器，Muon 是它最有力的挑战者。

## 4.4. 学习率调度

### 4.4.1. 衰减调度

学习率是最重要的**超参数**，并且最佳取值在训练过程中会变化。训练初期，较大的学习率进展快，能逃出糟糕的区域，并且由于它引入的噪声，还能避免拟合数据中的噪声；训练后期，则需要较小的学习率，才能稳定在极小点内而不是绕着它跳动（§4.3.5 输出的后半部分），并拟合更精细的模式。You 等人（2019）发现，最初的大学习率抑制了对带噪数据的记忆，而衰减则改善了对复杂模式的学习。

**定义 4.4.1（学习率调度）** **学习率调度**是一个函数 $t \mapsto \eta_t$，给出一次共 $T$ 步的训练中第 $t$ 步的学习率，通常是峰值学习率 $\eta_{\max}$ 乘以一条曲线。常见的曲线有：

| 调度 | $\eta_t / \eta_{\max}$ | 典型用途 |
|---|---|---|
| 阶梯衰减 | $\gamma^{\lfloor t/s\rfloor}$，例如每 $s$ 步（或在固定轮次）乘以 $\gamma = 0.1$ | ImageNet 上的 ResNet：在第 30、60、90 轮 $\times 0.1$ |
| 指数衰减 | $\gamma^t$ | 较早的模型、小问题 |
| 余弦 | $r + \frac12(1 - r)\bigl(1 + \cos(\pi t/T)\bigr)$，衰减到比例 $r$（常取 $0.1$ 或 $0$） | 2017 年以来的多数视觉模型与 Transformer |
| 逆平方根 | 经过 $w$ 步预热后取 $\min\bigl(t/w,\ \sqrt{w/t}\bigr)$ | 最初的 Transformer；没有固定终点的训练 |
| 预热–稳定–衰减（WSD） | 预热，然后恒为 $1$，最后 10%–20% 的步数内快速衰减（线性、余弦或 $1 - \sqrt{\cdot}$）到接近 $0$ | 2024 年以来的语言模型预训练 |
| 平台期衰减 | 验证损失不再改善时乘以 $\gamma$ | 小实验 |

余弦调度（Loshchilov 与 Hutter 2017，他们还提出了周期性重启）平滑衰减，大部分时间处于较高的学习率。它用于大规模训练的缺点是曲线形状依赖于 $T$：想训练得更久就必须从头开始，而且中间检查点没有充分退火。预热-稳定-衰减调度（warmup-stable-decay）（Hu 等 2024，MiniCPM；此前已有类似的梯形调度）避免了这一点：很长的恒定阶段可以无限延续，从其中任一检查点出发做一小段衰减，就得到一个退火后的模型，衰减期间损失会急剧下降。WSD 在相同计算量下持平或优于余弦，并使得研究损失如何依赖训练长度变得廉价；一种常见的解释是"河谷"地形：较高的学习率使模型在两侧山坡间弹跳的同时沿河流快速前进，而衰减使它下降到河床（Wen 等 2024）。最初的 Transformer 使用 $\eta_t = d_{\mathrm{model}}^{-1/2}\min(t^{-1/2}, t\,w^{-3/2})$，其中 $w = 4000$，即线性预热后接逆平方根衰减。

![10000 步内的学习率调度，峰值学习率为 1，预热 500 步（左）：阶梯衰减、指数衰减、线性预热后余弦衰减到 10%、最后 20% 线性衰减的预热–稳定–衰减，以及最初的 Transformer 的逆平方根调度；右为前 1500 步的细节](./plots/lr-schedules.py)

### 4.4.2. 预热

**定义 4.4.2（学习率预热）** **学习率预热**在训练的前 $w$ 步内把学习率从（接近）零增加到峰值，通常是线性增加，$t \le w$ 时 $\eta_t = \eta_{\max}\,t/w$，之后由衰减调度接手。

典型的预热持续几百到几千步（长训练的 1% 左右）。预热成为标准做法有三个相关的原因。

- 大批量。Goyal 等人（2017）将学习率随批大小线性放大（$\eta = 0.1 \cdot B/256$），以 $8192$ 张图像的批在一小时内训练完 ImageNet 上的 ResNet-50；这只有在前五个轮次中逐步预热才行得通，因为初始化时网络变化很快，大学习率会发散。
- 自适应优化器。最初几步中，Adam 的二阶矩估计 $\hat{\boldsymbol{v}}_t$ 只平均了少数几个梯度，方差很大，所以自适应学习率 $\eta/\sqrt{\hat{\boldsymbol{v}}_t}$ 不可靠；预热起到降低方差的作用（Liu 等 2020，他们提出了 RAdam，这是一种用解析方法修正该方差的 Adam）。
- Transformer。后归一化的 Transformer（[4.7.6](/4.7.6)）在初始化时输出附近的梯度很大，没有预热就会发散（Xiong 等 2020）；前归一化的 Transformer 容忍度更高，但实践中仍使用预热。

预热使训练稳定，允许更高的峰值学习率，从而常常加快收敛并改善最终结果。

### 4.4.3. 学习率与批大小

**随机梯度下降** 的噪声尺度正比于 $\eta/B$，即学习率乘以批梯度的方差。批大小加倍则噪声减半，所以一阶近似下，学习率加倍可以得到同样的轨迹，这就是 Goyal 等人的线性缩放规则；等价地，也可以在训练中增大批大小而不是衰减学习率（Smith 等 2018）。该规则在临界批大小之内成立，超过之后更大的批不再减少所需步数，只是浪费计算（McCandlish 等 2018）；对自适应优化器，在此之前学习率更接近按 $\sqrt B$ 缩放。临界批大小随损失下降而增大，这就是大语言模型用数百万**词元**的批训练，并且常在训练中逐步增大的原因。

## 4.5. 梯度消失与梯度爆炸

### 4.5.1. Jacobi 矩阵的乘积

对 **多层感知机**，**反向传播**方程（定理 2.4.1）给出 $\boldsymbol{\delta}^{(l)} = D^{(l)}W^{(l+1)\mathsf T}\boldsymbol{\delta}^{(l+1)}$，其中 $D^{(l)} = \operatorname{diag}\bigl(\varphi'(\boldsymbol{z}^{(l)})\bigr)$，因此
$$
\boldsymbol{\delta}^{(l)} = D^{(l)}W^{(l+1)\mathsf T}D^{(l+1)}W^{(l+2)\mathsf T}\cdots D^{(L-1)}W^{(L)\mathsf T}\boldsymbol{\delta}^{(L)} .
$$
到达第 $l$ 层的误差信号是输出误差乘以 $L - l$ 个 Jacobi 矩阵，而许多矩阵的乘积往往指数地增大或缩小。

**命题 4.5.1** 若 $\lvert\varphi'\rvert \le \gamma$ 且对所有层 $\|W^{(k)}\|_2 \le \omega$，则 $\|\boldsymbol{\delta}^{(l)}\| \le (\gamma\omega)^{L-l}\|\boldsymbol{\delta}^{(L)}\|$。

**证明** 谱范数是次可乘的，且 $\|D^{(k)}\|_2 = \max_j\lvert\varphi'(z^{(k)}_j)\rvert \le \gamma$，$\|W^{(k)\mathsf T}\|_2 = \|W^{(k)}\|_2 \le \omega$；对乘积中的每个因子应用这些不等式即可。$\square$

对 sigmoid，$\gamma = \frac14$，所以除非权重的范数超过 $4$，梯度会随深度几何级数地缩小；这就是 1990 年代层数很多的深层 sigmoid 网络如此难以训练的原因。反过来，如果各因子通常使向量变长，梯度就会几何级数地增大。

**定义 4.5.1（梯度消失与梯度爆炸）** 深度网络（或沿时间展开的循环网络）出现**梯度消失**，是指较早的层（或较早的时间步）的参数梯度比较晚的小指数倍，导致早期的层学习极慢；出现**梯度爆炸**，是指它们大指数倍，导致梯度步变得巨大，训练发散。

两者都是同一种乘法结构的症状，并且都会影响前向传播：激活值在同样的乘积下爆炸或消失。梯度消失使早期层的学习变慢甚至无法进行，但不会表现为错误；梯度爆炸则造成损失尖峰、溢出与 `NaN` 值。循环网络是极端情形，因为每个时间步都乘以同一个矩阵（[4.7.5](/4.7.5)）。

### 4.5.2. 补救办法

本章与前面各章的技术，都可以看作使 Jacobi 矩阵的乘积保持接近保范的办法。

| 办法 | 如何控制乘积 | 出处 |
|---|---|---|
| **线性整流单元** 及其变体 | 在激活的那一半上 $\varphi' = 1$，而不是 $\le \frac14$ | [4.7.2](/4.7.2) §2.6 |
| 保持方差的**权重初始化**（Xavier、He） | 初始化时每一层保持激活值与梯度的方差 | [4.7.2](/4.7.2) §2.7 |
| 残差连接 | $\boldsymbol{x} + F(\boldsymbol{x})$ 的 Jacobi 矩阵为 $I + J_F$，梯度因此有一条恒等路径 | [4.7.3](/4.7.3) §3.6.5 |
| 归一化层 | 在每一层重新缩放激活值，使相继各层的尺度解耦 | §4.6 |
| 门控（LSTM、GRU） | 加性的记忆通路，其 Jacobi 矩阵是接近 $I$ 的、学习得到的对角矩阵 | [4.7.5](/4.7.5) |
| 梯度裁剪 | 梯度爆炸时限制步长 | §4.5.3 |
| 正交初始化 | $W$ 的所有奇异值都为 $1$ | 循环网络、极深线性网络的分析 |

### 4.5.3. 梯度裁剪

梯度消失需要靠架构来补救；梯度爆炸也可以在优化器层面处理。在损失曲面的"悬崖"附近，梯度极大，沿它迈出一步就会把参数抛得很远，使此前的进展付诸东流；只需限制步长的长度即可。

**定义 4.5.2（梯度裁剪）** 阈值为 $c > 0$ 的按范数**梯度裁剪**，在优化器更新之前，把所有参数的梯度 $\boldsymbol{g}$ 替换为
$$
\tilde{\boldsymbol{g}} = \boldsymbol{g}\cdot\min\left(1, \frac{c}{\|\boldsymbol{g}\|}\right)
$$
它保持梯度的方向，并把范数限制在 $c$ 以内。按值裁剪则把每个分量截断到 $[-c, c]$ 内，这也会改变方向。

按全局范数（对所有参数一起计算）裁剪，最早用于循环网络（Mikolov 2012；Pascanu、Mikolov 与 Bengio 2013），是训练 Transformer 的标准做法，通常取 $c = 1.0$；在 PyTorch 中只需一次调用，`torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)`，放在 `loss.backward()` 与 `opt.step()` 之间，其返回值即裁剪前的范数，是值得记录的量。频繁裁剪说明学习率过高，或数据或模型存在问题。在大模型训练中，损失尖峰还可以通过跳过梯度范数异常的批、回滚到更早的检查点，以及架构上的措施（如对注意力的查询与键做归一化）来处理。

## 4.6. 归一化

### 4.6.1. 数据归一化

改善损失条件数最简单的办法是预处理输入。对于平方损失的线性回归，**Hesse 矩阵**为 $\frac{1}{m}X^{\mathsf T}X$，其元素是各特征的二阶矩。如果一个特征以米为单位而另一个以毫米为单位，或者一个特征的均值是 $1000$ 而标准差是 $1$，那么 Hessian 的特征值大小悬殊，损失的水平集是拉长的椭圆，梯度主要指向横穿山谷的方向，而不是指向极小点。对每个特征做标准化，
$$
x'_j = \frac{x_j - \mu_j}{\sigma_j},
$$
其中均值 $\mu_j$ 与标准差 $\sigma_j$ 在**训练集**上计算（并把同样的值用于验证数据与测试数据），使特征中心化且具有单位尺度，并把 Hessian 变成各特征的相关矩阵。白化则更进一步，例如用**主成分分析**使各特征去相关，于是 Hessian 变成单位矩阵；高维输入很少这样做。对图像，通常的归一化是减去训练集上每个通道的均值，再除以每个通道的标准差。

### 4.6.2. 批归一化

对输入做归一化只对第一层有帮助。每个隐藏层的输入都来自它下面的各层，这些输入的分布在下层权重改变时随之改变，而在深度网络中，低层的一个小改变可能被放大为高层输入分布的大改变，使高层不得不重新适应。Ioffe 与 Szegedy（2015）称之为**内部协变量偏移**（internal covariate shift），并提出在小批量上对每一层的输入做归一化。

**定义 4.6.1（批归一化）** 参数为 $\boldsymbol{\gamma}, \boldsymbol{\beta} \in \mathbb{R}^d$ 的**批归一化**层把小批量 $\boldsymbol{x}_1, \dots, \boldsymbol{x}_m \in \mathbb{R}^d$（某一层的预激活值，每个样例一行）映到
$$
\hat{\boldsymbol{x}}_i = \frac{\boldsymbol{x}_i - \boldsymbol{\mu}_{\mathcal{B}}}{\sqrt{\boldsymbol{\sigma}^2_{\mathcal{B}} + \varepsilon}}, \qquad \boldsymbol{y}_i = \boldsymbol{\gamma} \odot \hat{\boldsymbol{x}}_i + \boldsymbol{\beta}, \qquad \boldsymbol{\mu}_{\mathcal{B}} = \frac{1}{m}\sum_{i=1}^m\boldsymbol{x}_i, \quad \boldsymbol{\sigma}^2_{\mathcal{B}} = \frac{1}{m}\sum_{i=1}^m(\boldsymbol{x}_i - \boldsymbol{\mu}_{\mathcal{B}})^2,
$$
所有运算逐分量进行，$\varepsilon$（例如 $10^{-5}$）是一个小常数。在推断时，$\boldsymbol{\mu}_{\mathcal{B}}$ 与 $\boldsymbol{\sigma}^2_{\mathcal{B}}$ 被替换为总体估计，通常是训练中累积的批统计量的指数移动平均，于是该层成为一个固定的仿射映射。

每个特征在批上被归一化为均值 $0$、方差 $1$，可学习的缩放 $\boldsymbol{\gamma}$ 与平移 $\boldsymbol{\beta}$ 恢复了表达能力：取 $\boldsymbol{\gamma} = \sqrt{\boldsymbol{\sigma}^2 + \varepsilon}$ 与 $\boldsymbol{\beta} = \boldsymbol{\mu}$，该层可以撤销归一化。改变的是参数化：该层输出的均值与尺度现在由两个参数直接控制，而不是由其下所有权重之间微妙的相互作用决定。BN 放在线性层或**卷积层**之后、激活函数之前；该层的偏置变得多余，因为 $\boldsymbol{\beta}$ 取代了它的作用。在**卷积神经网络**中，**特征图**的形状为 $(N, C, H, W)$，统计量按通道在批与全部空间位置上计算（每个通道 $N \cdot H \cdot W$ 个值），使归一化与**卷积**的平移等变性相容，且 $\boldsymbol{\gamma}, \boldsymbol{\beta} \in \mathbb{R}^C$。

由于 $\boldsymbol{\mu}_{\mathcal{B}}$ 与 $\boldsymbol{\sigma}_{\mathcal{B}}$ 依赖批中的所有样例，反向传播必须对它们求导。

**命题 4.6.1** 对一个特征，设 $\boldsymbol{g} = \partial E/\partial\boldsymbol{y} \in \mathbb{R}^m$ 为批上的上游梯度，$s = \sqrt{\sigma^2_{\mathcal{B}} + \varepsilon}$，则
$$
\frac{\partial E}{\partial\gamma} = \sum_{i=1}^m g_i\hat x_i, \qquad \frac{\partial E}{\partial\beta} = \sum_{i=1}^m g_i, \qquad \frac{\partial E}{\partial x_i} = \frac{\gamma}{ms}\Bigl(m g_i - \sum_{j=1}^m g_j - \hat x_i\sum_{j=1}^m g_j\hat x_j\Bigr).
$$

**证明** 前两个公式由 $y_i = \gamma\hat x_i + \beta$ 得到。对第三个，$\partial E/\partial\hat x_j = \gamma g_j$，而 $\hat x_j = (x_j - \mu)/s$ 既直接依赖于 $x_i$，又通过 $\mu$ 与 $s$ 依赖于 $x_i$。由 $\partial\mu/\partial x_i = 1/m$ 与 $\partial\sigma^2/\partial x_i = \frac{2}{m}(x_i - \mu)$（来自 $\partial\mu/\partial x_i$ 的项因 $\sum_j(x_j - \mu) = 0$ 而消失）得 $\partial s/\partial x_i = (x_i - \mu)/(ms) = \hat x_i/m$，从而
$$
\frac{\partial\hat x_j}{\partial x_i} = \frac{1}{s}\Bigl(\boldsymbol{1}\{i = j\} - \frac1m\Bigr) - \frac{x_j - \mu}{s^2}\cdot\frac{\hat x_i}{m} = \frac{1}{ms}\bigl(m\boldsymbol{1}\{i = j\} - 1 - \hat x_j\hat x_i\bigr).
$$
乘以 $\gamma g_j$ 并对 $j$ 求和，即得公式。$\square$

对输入的梯度，是把上游梯度去掉其均值及其沿 $\hat{\boldsymbol{x}}$ 的分量后得到的：BN 使损失对某个特征输入的平移或缩放不变，所以梯度在这些方向上没有分量。下面的代码用有限差分检验该公式。

```python
import numpy as np


def batchnorm_forward(X, gamma, beta, eps=1e-5):
    """X: (m, d) mini-batch. Normalizes each feature over the batch."""
    mu = X.mean(axis=0)
    var = X.var(axis=0)                       # biased variance, as in training mode
    inv_std = 1.0 / np.sqrt(var + eps)
    X_hat = (X - mu) * inv_std
    return gamma * X_hat + beta, (X_hat, inv_std, gamma)


def batchnorm_backward(G, cache):
    """G = dE/dY. Returns dE/dX, dE/dgamma, dE/dbeta (Proposition 4.6.1)."""
    X_hat, inv_std, gamma = cache
    m = G.shape[0]
    dgamma = (G * X_hat).sum(axis=0)
    dbeta = G.sum(axis=0)
    dX = gamma * inv_std / m * (m * G - dbeta - X_hat * dgamma)
    return dX, dgamma, dbeta


rng = np.random.default_rng(0)
X = rng.normal(3.0, 2.0, size=(16, 4))
gamma, beta = rng.normal(size=4), rng.normal(size=4)
C = rng.normal(size=(16, 4))                      # E = sum(C * Y), so dE/dY = C
Y, cache = batchnorm_forward(X, gamma, beta)
print(f"max |batch mean of Y - beta| = {np.abs((Y - beta).mean(axis=0)).max():.1e}")
dX, dgamma, dbeta = batchnorm_backward(C, cache)
h, num = 1e-6, np.zeros_like(X)
for idx in np.ndindex(X.shape):                    # central differences
    Xp, Xm = X.copy(), X.copy()
    Xp[idx] += h
    Xm[idx] -= h
    num[idx] = (np.sum(C * batchnorm_forward(Xp, gamma, beta)[0])
                - np.sum(C * batchnorm_forward(Xm, gamma, beta)[0])) / (2 * h)
print(f"max |analytic - numerical| = {np.abs(dX - num).max():.1e}")
print(f"max |column sum of dE/dX|  = {np.abs(dX.sum(axis=0)).max():.1e}")
```

```text
max |batch mean of Y - beta| = 4.2e-16
max |analytic - numerical| = 2.8e-09
max |column sum of dE/dX|  = 9.4e-16
```

批归一化使很深的网络容易训练得多。它稳定梯度，允许使用十倍高的学习率，使训练对初始化远不敏感，并有轻微的正则化作用，因为每个样例的归一化依赖于批中其他随机样例；带 BN 的 Inception 网络只用 $1/14$ 的步数就达到了前代网络的精度。BN 为什么有效，比它有效这一事实更不清楚。Santurkar 等人（2018）表明，BN 实际上并没有在可度量的意义上降低内部协变量偏移，它的主要作用是使损失曲面更平滑：损失及其梯度的 Lipschitz 性更好，所以较大的步长是安全的。一个相关的解释是尺度不变性：BN 层的输出在其下方权重被缩放时不变，所以这些权重的有效学习率是 $\eta/\|\boldsymbol{w}\|^2$，并由**权重衰减**自动调节。

BN 也有缺点，都源于它对批的依赖。批很小时（检测、分割和视频中很常见，一张图像就占满一块 GPU），批统计量噪声很大，精度下降。训练与推断计算的是不同的函数，这会引起难以察觉的错误：忘记切换到评估模式，或者训练批与测试数据之间存在分布偏移。分布式训练中还必须在设备之间同步统计量。而对变长的序列模型，对各位置求批统计量也很别扭。这些问题促使人们提出了对单个样例起作用的归一化。

### 4.6.3. 层归一化

**定义 4.6.2（层归一化）** **层归一化**（Ba、Kiros 与 Hinton 2016）把每个样例在其特征上归一化：对 $\boldsymbol{x} \in \mathbb{R}^d$，
$$
\mu = \frac1d\sum_{j=1}^d x_j, \qquad \sigma^2 = \frac1d\sum_{j=1}^d(x_j - \mu)^2, \qquad \operatorname{LN}(\boldsymbol{x}) = \boldsymbol{\gamma} \odot \frac{\boldsymbol{x} - \mu\boldsymbol{1}}{\sqrt{\sigma^2 + \varepsilon}} + \boldsymbol{\beta},
$$
其中 $\boldsymbol{\gamma}, \boldsymbol{\beta} \in \mathbb{R}^d$ 可学习。

统计量是按样例（在序列模型中按位置）计算的，所以层归一化在训练与推断中行为一致，批大小为一也能工作，并能处理任意长度的序列。它是为循环网络设计的，在每个时间步作用于加权求和后的输入，缓解梯度消失与爆炸（[4.7.5](/4.7.5)），也是 Transformer 的核心组件，在其中对每个**词元**的 $d_{\mathrm{model}}$ 维向量做归一化（[4.7.6](/4.7.6)）。它在卷积网络中不如 BN 有效，因为在那里它要把一张图像的所有通道与位置放在一起归一化，不过 ConvNeXt 与视觉 Transformer 成功地使用了它（[4.7.3](/4.7.3)）。

### 4.6.4. 实例归一化与组归一化

对形状为 $(N, C, H, W)$（批、通道、高、宽）的张量，各种归一化方法的区别在于计算均值与方差所用的元素集合。

**定义 4.6.3（实例归一化与组归一化）** **实例归一化**（Ulyanov、Vedaldi 与 Lempitsky 2016）对每个样例的每个通道分别计算统计量，在 $H \times W$ 个空间位置上求。**组归一化**（Wu 与 He 2018）把 $C$ 个通道分成 $G$ 组，每组 $C/G$ 个相邻通道，对每个样例的每一组计算统计量，在 $(C/G) \times H \times W$ 个元素上求。两者随后都像定义 4.6.1 那样施加按通道的可学习缩放与平移。

| 方法 | 统计量的计算范围 | 在其间共享 | 典型用途 |
|---|---|---|---|
| 批归一化 | $N, H, W$（按通道） | 整个批 | 大批量的分类 CNN |
| 层归一化 | $C, H, W$（按样例），或一个词元的特征向量 | — | RNN、Transformer |
| 实例归一化 | $H, W$（按样例与通道） | — | 风格迁移、图像生成 |
| 组归一化 | $C/G, H, W$（按样例与组） | — | 检测、分割、小批量、扩散模型的 U-Net |

组归一化在两种按样例的方法之间插值：$G = 1$ 时是层归一化，$G = C$ 时是实例归一化；通常默认 $G = 32$。实例归一化去掉每张图像的对比度与整体颜色统计，这正是风格迁移所需要的，因为在那里这些统计量承载着风格。组归一化与批大小无关，在批大小为 $2$ 时，它在 ImageNet 上大幅优于批归一化（Wu 与 He 2018）。

### 4.6.5. RMSNorm

**定义 4.6.4（RMSNorm）** **RMSNorm**（均方根层归一化；Zhang 与 Sennrich 2019）用向量 $\boldsymbol{x} \in \mathbb{R}^d$ 的均方根对它重新缩放，而不做中心化：
$$
\operatorname{RMSNorm}(\boldsymbol{x}) = \boldsymbol{\gamma} \odot \frac{\boldsymbol{x}}{\operatorname{RMS}(\boldsymbol{x})}, \qquad \operatorname{RMS}(\boldsymbol{x}) = \sqrt{\frac1d\sum_{j=1}^d x_j^2 + \varepsilon},
$$
其中增益 $\boldsymbol{\gamma} \in \mathbb{R}^d$ 可学习，没有平移。

Zhang 与 Sennrich 认为，层归一化的成功来自它对输入缩放的不变性，而不是中心化，去掉均值可以节省计算与一个参数向量，而质量没有损失。RMSNorm 是自 LLaMA（2023）以来几乎所有大语言模型所用的归一化，包括 Qwen、DeepSeek、Gemma 与 Mistral 系列。一些变体把它用在更多的位置，例如在注意力乘积之前对查询与键做归一化（QK-norm，用于 Qwen3、OLMo 2 与 Gemma 3），以防止注意力 logit 增长。Zhu 等人（2025）表明，把归一化层换成逐元素的 $\boldsymbol{\gamma} \odot \tanh(\alpha\boldsymbol{x}) + \boldsymbol{\beta}$（其中 $\alpha$ 是可学习的标量，称为动态 tanh），Transformer 甚至可以不用归一化层训练，它模拟了层归一化对离群值的压缩作用。

### 4.6.6. PyTorch 中的归一化

下面的代码（PyTorch 2.14，CPU）对照库中的模块检验层归一化与 RMSNorm 的定义，并展示批归一化在训练模式与评估模式下的区别。

```python
import torch
from torch import nn

torch.manual_seed(0)
x = torch.randn(2, 5, 8) * 3 + 1                 # (batch, sequence, features)
ln, rms = nn.LayerNorm(8), nn.RMSNorm(8, eps=1e-6)
mu, var = x.mean(-1, keepdim=True), x.var(-1, unbiased=False, keepdim=True)
print(torch.allclose(ln(x), (x - mu) / torch.sqrt(var + 1e-5), atol=1e-6))
print(torch.allclose(rms(x), x / torch.sqrt((x ** 2).mean(-1, keepdim=True) + 1e-6), atol=1e-6))

bn = nn.BatchNorm1d(8)                            # expects (batch, features) or (batch, features, length)
h = torch.randn(32, 8) * 2 + 5
bn.train()
y_train = bn(h)                                   # batch statistics; updates running estimates
bn.eval()
y_eval = bn(h)                                    # running estimates: different output
print(f"|mean| in train mode {y_train.mean().abs():.3f}, mean in eval mode {y_eval.mean():.3f}")
print("running mean after one batch:", bn.running_mean[:3])
```

```text
True
True
|mean| in train mode 0.000, mean in eval mode 4.084
running mean after one batch: tensor([0.4716, 0.5170, 0.4862])
```

滑动均值从 $0$ 开始，按 $0.9 \cdot \text{旧值} + 0.1 \cdot \text{批均值}$ 更新（PyTorch 把 $0.1$ 称为该层的 `momentum`），所以在一个均值约为 $5$ 的批之后它约为 $0.5$，评估模式的输出远未归一化。滑动统计量需要许多批才能收敛，并且评估前必须调用 `model.eval()`；这两点都是常见的错误来源。

## 4.7. 正则化

### 4.7.1. 惩罚项、早停与数据增强

一个有数百万参数的网络可以完美地拟合其**训练集**，连同其中的噪声，而**过拟合**由**正则化**来控制（[4.7.1](/4.7.1)）。**深度学习**中的主要技术有：

- **早停**：返回验证损失最小时的参数（[4.7.1](/4.7.1) §1.4.3）。它几乎没有代价，总是值得监控，不过现代实践常常转而用衰减的学习率训练到固定的预算。
- 参数范数惩罚：$L^2$ 惩罚 $\frac\lambda2\|\boldsymbol{\theta}\|^2$，实现为（解耦的）**权重衰减**，$\lambda$ 取 $10^{-5}$ 到 $0.1$；$L^1$ 惩罚 $\lambda\|\boldsymbol{\theta}\|_1$，产生稀疏的权重（如 **Lasso**），但很少用于整个网络；以及弹性网，即两者的组合。最大范数约束在每步之后把每个单元的输入权重向量投影回球 $\|\boldsymbol{w}\| \le c$ 内，与随机失活配合良好（Srivastava 等 2014）。
- 数据增强（data augmentation）：在随机变换后的训练样例副本上训练，变换保持标签不变，使模型学到相应的不变性，等效于看到了更多数据。对图像：随机裁剪、翻转、缩放、颜色抖动，以及更强的策略，如 RandAugment、Cutout、Mixup（在成对样例及其标签的凸组合上训练）与 CutMix。对文本有回译与改写；对语音有 SpecAugment。
- 标签平滑（Szegedy 等 2016）：对 $k$ 个类别，把独热目标换成 $(1 - \alpha)\boldsymbol{y} + \alpha/k$，其中 $\alpha \approx 0.1$，它防止 logit 为了精确拟合目标而无限增长，并改善校准。
- 噪声：小批量 **随机梯度下降** 的梯度噪声、加在输入或权重上的噪声，以及下面的随机失活。

### 4.7.2. 随机失活

大网络可以靠脆弱的共适应来拟合训练数据，即某个单元只有在特定的其他单元存在时才有用。随机失活通过在训练中随机移除单元来打破这种共适应。

**定义 4.7.1（随机失活）** 失活率为 $p \in [0, 1)$ 的**随机失活**（Hinton 等 2012；Srivastava 等 2014）在训练时把某一层的每个激活值乘以一个独立的随机掩码：对激活向量 $\boldsymbol{a}$，
$$
\tilde{\boldsymbol{a}} = \frac{1}{1 - p}\,\boldsymbol{r} \odot \boldsymbol{a}, \qquad r_j \overset{\text{iid}}{\sim} \mathrm{Ber}(1 - p),
$$
每个样例、每一步都重新抽取掩码；推断时该层是恒等映射。因子 $1/(1 - p)$ 是所有现代库使用的"反向"形式，它使 $\mathbb{E}[\tilde{\boldsymbol{a}}] = \boldsymbol{a}$；最初的表述则是训练时不做缩放，而在测试时把输出权重乘以 $1 - p$。

在反向传播中，同一个掩码也作用于梯度，所以被丢弃的单元在该步不接收梯度。典型的失活率是：全连接隐藏层 $p = 0.5$，输入层以及 Transformer 中 $0.1$ 到 $0.2$，**卷积层**中则更低，因为空间上相关的激活使逐单元的失活效果较差（丢弃整个通道更好）。

```python
import numpy as np


def dropout(A, p, rng, training=True):
    """Inverted dropout: drop each unit with probability p, scale survivors by 1/(1-p)."""
    if not training or p == 0.0:
        return A, None
    mask = (rng.random(A.shape) >= p) / (1.0 - p)    # the same mask is reused in the backward pass
    return A * mask, mask


rng = np.random.default_rng(0)
A = rng.random((1000, 256))
D, mask = dropout(A, 0.5, rng)
print(f"fraction zeroed {np.mean(D == 0):.3f}, mean before {A.mean():.4f}, after {D.mean():.4f}")
G = np.ones_like(D)            # upstream gradient dE/dD
print("backward = G * mask:", np.allclose(G * mask, np.where(D == 0, 0.0, 2.0)))
```

```text
fraction zeroed 0.500, mean before 0.4999, after 0.5007
backward = G * mask: True
```

对随机失活为什么起正则化作用，有两种互补的看法。一是集成：含 $n$ 个可失活单元的网络包含 $2^n$ 个共享权重的子网络，每个训练步在一个样例上训练其中之一，而测试时的网络近似于它们预测的几何平均（对单个 **softmax 函数** 层是精确的）。二是自适应噪声：对线性模型，随机失活在期望意义下等价于一个依赖于数据的 $L^2$ 惩罚。

**命题 4.7.1** 设 $\hat y = \frac{1}{1-p}\sum_{j=1}^n w_jr_jx_j$，其中 $r_j \sim \mathrm{Ber}(1 - p)$ 相互独立（对线性模型的输入做随机失活）。则
$$
\mathbb{E}\bigl[(y - \hat y)^2\bigr] = \bigl(y - \boldsymbol{w}^{\mathsf T}\boldsymbol{x}\bigr)^2 + \frac{p}{1 - p}\sum_{j=1}^n w_j^2x_j^2 .
$$

**证明** 由于 $\mathbb{E}[r_j] = 1 - p$，有 $\mathbb{E}[\hat y] = \boldsymbol{w}^{\mathsf T}\boldsymbol{x}$，再由独立性，$\operatorname{Var}(\hat y) = \frac{1}{(1-p)^2}\sum_j w_j^2x_j^2\operatorname{Var}(r_j) = \frac{p(1 - p)}{(1 - p)^2}\sum_j w_j^2x_j^2$。结论即分解式 $\mathbb{E}[(y - \hat y)^2] = (y - \mathbb{E}\hat y)^2 + \operatorname{Var}(\hat y)$。$\square$

对训练集取平均，惩罚项为 $\frac{p}{1-p}\sum_j w_j^2\,\overline{x_j^2}$：这是一个岭惩罚，其中每个权重所受的惩罚正比于其输入特征的二阶矩（Wager、Wang 与 Liang 2013），所以随机失活对罕见特征的正则化比权重衰减更轻。在 MNIST 上，Srivastava 等人（2014）用随机失活把标准 **多层感知机** 的错误率从 1.60% 降到 1.25%，与最大范数约束及更宽的层结合后降到 0.95%；全连接层中的随机失活也是 AlexNet 成功的关键之一。

随机失活使收敛变慢（梯度噪声更大，训练通常需要两到三倍的步数），并且与批归一化相互干扰：当随机失活位于 BN 之前时，BN 的统计量在训练与推断之间会发生偏移。它的变体有 DropConnect（丢弃权重而非单元）、空间随机失活（整个通道），以及随机深度（stochastic depth）或 DropPath（Huang 等 2016），后者丢弃整个残差块，是训练视觉 Transformer 的标准做法。在测试时保持随机失活开启并对多次随机前向传播取平均（Monte Carlo 随机失活；Gal 与 Ghahramani 2016），可得到预测不确定性的近似 Bayes 估计。在大语言模型的预训练中，通常只对海量数据过一遍，**过拟合**不是瓶颈，随机失活一般被关闭；它在小数据集上的微调中仍然常见。

## 4.8. 超参数的实际选择

### 4.8.1. 六步流程

深度网络有许多**超参数**（[4.7.1](/4.7.1)）：架构（层数、宽度）、优化器及其学习率、动量与**权重衰减**、调度、批大小、失活率和数据增强。架构最好从已知在类似数据与任务上有效的模型出发来选，并根据样例数量以及输入的规模与复杂度加以调整；其余**超参数**可以系统地确定。下面的流程改编自斯坦福 CS231n 课程（Li、Johnson 与 Yeung 2019）与 Google 的 *Deep Learning Tuning Playbook*（Godbole 等 2023）。

1. 检查初始损失。关闭权重衰减时，初始化时的损失应与其理论值吻合：对输出为 **softmax 函数**、权重为小随机数的 $k$ 类分类器，预测近似均匀，**交叉熵损失**约为 $\ln k$（十类时为 $2.30$）。数值不符说明损失或初始化有错误。
2. 过拟合一个小子集。在不加**正则化**的情况下，在几个批（比如 100 个样例）上训练，达到 100% 的训练准确率。这检验了从数据加载到输出的整个流程。若损失不下降，说明学习率太低、初始化不佳或模型太小；若损失爆炸成 `inf` 或 `NaN`，说明学习率太高或初始化不佳。
3. 找到使损失下降的学习率。在完整**训练集**上，取一个较小的权重衰减，在对数网格上尝试学习率（**随机梯度下降** 从 $0.1$ 开始逐次除以 $10$；Adam 在 $10^{-3}$ 附近），保留那些在最初一百次迭代内损失显著下降的值。
4. 粗网格，短训练。在第 3 步找到的学习率与权重衰减附近取几个值，训练 1–5 个轮次（权重衰减如 $10^{-4}$、$10^{-5}$、$0$）。
5. 细化网格，延长训练。取最好的设置训练更久，约 10–20 个轮次，不做学习率衰减。
6. 观察损失曲线，诊断问题，并回到相应的步骤。

超参数较多时，在对数尺度上随机搜索比网格搜索更有效（[4.7.1](/4.7.1) §1.4.3），诊断问题时一次只应改变一两个超参数。对大模型，超参数在小的代理模型上调好后再迁移，这与为迁移而设计的参数化（如 μP，[4.7.2](/4.7.2) §2.7）配合最好。

### 4.8.2. 解读损失曲线

训练损失在批与批之间有噪声，通常画成滑动平均；验证损失与准确率则定期评估。常见的模式及其通常的原因：

| 模式 | 可能的原因 | 对策 |
|---|---|---|
| 损失长时间持平，然后突然下降 | 初始化不佳（如单元饱和） | 更好的初始化、归一化 |
| 损失快速下降后停在较高的值 | 学习率过高，无法稳定下来 | 加入学习率衰减 |
| 损失过早停滞，离良好性能还很远 | 停在鞍点附近或糟糕的区域；模型太小 | 更高的学习率、动量、更大的模型 |
| 训练与验证准确率差距很大，验证损失上升 | 过拟合 | 更多数据或增强、更强的正则化、更小的模型、早停 |
| 没有差距，两者的准确率仍在上升 | 欠拟合，训练太短 | 训练更久、更大的模型 |
| 损失出现尖峰或 `NaN` | 学习率过高、梯度爆炸、坏数据 | 降低学习率、预热、梯度裁剪、检查该批数据 |

较大的模型更容易在小数据集上过拟合；当验证准确率与训练准确率一起仍在上升时，可以增加容量。最后，不同训练的曲线应在相同的计算量下比较，而不仅仅是在相同的步数下比较。

## 小结

- 神经网络的损失是非凸且病态的；多数有问题的临界点是**鞍点**，而架构（**跳跃连接**、归一化）决定曲面的光滑程度。二次函数上的**梯度下降法**在 $\eta < 2/\lambda_{\max}$ 时收敛，速率由**条件数** $\kappa$ 决定。
- 动量 $\boldsymbol{v}_t = \beta\boldsymbol{v}_{t-1} + \boldsymbol{g}_t$ 抑制震荡并累积一致的方向，使二次函数上的速率从 $1 - 2/\kappa$ 改善到 $1 - 2/\sqrt\kappa$；Nesterov 动量在前瞻点处计算梯度，对光滑**凸函数**是最优的。
- AdaGrad、RMSProp 与 Adam 把每个坐标除以其梯度平方历史的平方根。Adam 将其与动量结合，并用 $1/(1 - \beta^t)$ 修正两个平均的初始化偏差；AdamW 把**权重衰减**与自适应缩放解耦，是 Transformer 的默认选择。Lion 使用动量的符号，Muon 对每个权重矩阵的动量做正交化，即谱范数下的最速下降。
- 学习率先线性预热（稳定 Adam 与大批量训练），再按阶梯、余弦或预热–稳定–衰减调度衰减；在临界批大小之内，学习率随批大小缩放。
- 穿过许多层或时间步的梯度是 Jacobi 矩阵的乘积，会指数地消失或爆炸；**线性整流单元**、初始化、残差连接、归一化与门控使它们保持稳定，按全局范数的梯度裁剪则在梯度爆炸时限制步长。
- 批归一化在小批量上对每个特征做标准化（推断时使用滑动统计量）；层归一化与 RMSNorm 在每个样例的特征上归一化，用于 RNN 与 Transformer；实例归一化与组归一化服务于小批量的视觉任务。
- 随机失活以概率 $p$ 把单元置零，并把其余单元乘以 $1/(1-p)$，相当于训练一个隐式的集成；对线性模型，它是按特征缩放的 $L^2$ 惩罚。**超参数**的确定方法是：检查初始损失，**过拟合**一个小子集，找到可用的学习率，在由粗到细的网格上细化，并同时观察损失曲线。
