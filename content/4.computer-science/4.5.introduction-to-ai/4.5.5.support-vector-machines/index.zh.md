---
title: 支持向量机
description: 统计学习的框架与经验风险、结构风险；函数间隔与几何间隔；硬间隔支持向量机与最大间隔超平面的存在唯一性；Lagrange 对偶、弱对偶与强对偶、KKT 条件；软间隔与合页损失；核技巧与常用核函数；SMO 算法及其实现；多类分类与文本分类。
---

[3.4.10](/3.4.10) 在判别分析的最后简要介绍了**支持向量机**：在所有把两类分开的超平面中，选择间隔最大的一个。本章把它完整地推导出来。支持向量机的思想有三个层次：两类可分时，最大化间隔得到一个凸二次规划；两类不可分时，引入松弛变量允许少量错误，等价于最小化合页损失加正则项；需要非线性边界时，借助对偶问题中"只出现内积"这一性质，用核函数代替内积，在高维甚至无穷维的特征空间中做线性分类而不必显式计算特征。推导中用到的 Lagrange 对偶与 KKT 条件是约束优化的基本工具，本章给出它们的一般形式。最后介绍求解对偶问题的 SMO 算法。支持向量机在 1990 年代中期到 2010 年前后是最有影响力的分类方法之一；今天在中小规模的表格数据和文本数据上仍是可靠的基线，而大规模的感知任务已由深度学习（[4.5.4](/4.5.4)、[4.7](/4.7)）主导。

## 5.1. 统计学习与线性分类

### 5.1.1. 统计学习的框架

Simon 说："如果一个系统能够通过执行某个过程改进它的性能，这就是学习。"统计学习是计算机系统运用数据和统计方法提高性能的机器学习：从数据出发，抽象出数据的模型，再用于对新数据的预测与分析。它的基本设定是：

- 输入 $\boldsymbol{x} \in \mathcal{X}$，输出 $y \in \mathcal{Y}$，存在一个未知的目标函数 $f\colon \mathcal{X} \to \mathcal{Y}$（或条件分布 $\mathbb{P}(y \mid \boldsymbol{x})$）；
- 训练集 $T = \{(\boldsymbol{x}_1, y_1), \dots, (\boldsymbol{x}_N, y_N)\}$ 由 $f$ 产生，可能带有噪声；
- 假设空间 $\mathcal{H}$ 是候选模型的集合；学习算法根据 $T$ 从 $\mathcal{H}$ 中选出一个 $g \approx f$。

于是一个统计学习方法由三部分组成：模型（假设空间是什么，如线性函数、决策树），策略（按什么准则选择模型），算法（怎样求解由策略得到的优化问题）。

**定义 5.1.1（经验风险最小化）** 给定**损失函数** $L(y, g(\boldsymbol{x}))$，模型 $g$ 在训练集上的平均损失 $R_{\mathrm{emp}}(g) = \frac1N\sum_{i=1}^{N} L(y_i, g(\boldsymbol{x}_i))$ 称为经验风险。在假设空间中选择使经验风险最小的模型的策略称为**经验风险最小化**；在经验风险上加一个惩罚模型复杂度的正则项 $\lambda J(g)$、选择使 $R_{\mathrm{emp}}(g) + \lambda J(g)$ 最小的模型的策略称为**结构风险最小化**。

样本少而模型复杂时，经验风险最小化容易**过拟合**；结构风险最小化通过正则项在拟合与复杂度之间权衡，岭回归（[3.3.12](/3.3.12)）就是一例。后面会看到，软间隔支持向量机正是以合页损失为损失、以 $\|\boldsymbol{w}\|^2$ 为正则项的结构风险最小化。按训练数据是否有标注，统计学习分为**有监督学习**、**无监督学习**与半监督学习等；本章与下一章都是有监督的分类。

### 5.1.2. 线性可分与间隔

考虑二分类：$\mathcal{X} = \mathbb{R}^n$，$\mathcal{Y} = \{+1, -1\}$，$+1$ 为正类，$-1$ 为负类。超平面 $\boldsymbol{w} \cdot \boldsymbol{x} + b = 0$ 把空间分成两半，相应的决策函数为 $g(\boldsymbol{x}) = \operatorname{sgn}(\boldsymbol{w} \cdot \boldsymbol{x} + b)$。

**定义 5.1.2（线性可分）** 若存在超平面 $(\boldsymbol{w}, b)$ 使所有正例满足 $\boldsymbol{w} \cdot \boldsymbol{x}_i + b > 0$、所有负例满足 $\boldsymbol{w} \cdot \boldsymbol{x}_i + b < 0$，即 $y_i(\boldsymbol{w} \cdot \boldsymbol{x}_i + b) > 0$ 对所有 $i$ 成立，则称训练集是**线性可分**的。

线性可分时，分开两类的超平面有无穷多个（感知机找到的是其中任意一个）。直观上，离两类样本都尽量远的超平面最可靠：新样本稍有扰动也不会被分错。点到超平面的远近有两种度量。

**定义 5.1.3（函数间隔与几何间隔）** 超平面 $(\boldsymbol{w}, b)$ 关于样本点 $(\boldsymbol{x}_i, y_i)$ 的**函数间隔**与**几何间隔**分别为

$$
\hat\gamma_i = y_i(\boldsymbol{w} \cdot \boldsymbol{x}_i + b), \qquad \gamma_i = y_i\Bigl(\frac{\boldsymbol{w}}{\|\boldsymbol{w}\|} \cdot \boldsymbol{x}_i + \frac{b}{\|\boldsymbol{w}\|}\Bigr) = \frac{\hat\gamma_i}{\|\boldsymbol{w}\|}.
$$
超平面关于训练集 $T$ 的函数间隔与几何间隔分别为 $\hat\gamma = \min_i \hat\gamma_i$ 与 $\gamma = \min_i \gamma_i$；几何间隔 $\gamma$ 简称超平面关于训练集的**间隔**。

样本被正确分类时，几何间隔就是点到超平面的距离；分错时为负的距离。函数间隔的大小没有意义：把 $(\boldsymbol{w}, b)$ 同乘以 $2$，超平面不变，函数间隔却加倍。几何间隔不受这种缩放的影响，$\gamma = \hat\gamma / \|\boldsymbol{w}\|$。

## 5.2. 硬间隔支持向量机

### 5.2.1. 间隔最大化

求几何间隔最大的分离超平面：

$$
\max_{\boldsymbol{w}, b}\ \frac{\hat\gamma}{\|\boldsymbol{w}\|} \quad \text{s.t.} \quad y_i(\boldsymbol{w} \cdot \boldsymbol{x}_i + b) \ge \hat\gamma, \quad i = 1, \dots, N.
$$
由于缩放 $(\boldsymbol{w}, b)$ 不改变问题，可以取 $\hat\gamma = 1$；而最大化 $1/\|\boldsymbol{w}\|$ 等价于最小化 $\frac12\|\boldsymbol{w}\|^2$。于是得到

**定义 5.2.1（硬间隔支持向量机）** 对线性可分的训练集，求解凸二次规划

$$
\min_{\boldsymbol{w}, b}\ \frac12\|\boldsymbol{w}\|^2 \quad \text{s.t.} \quad y_i(\boldsymbol{w} \cdot \boldsymbol{x}_i + b) \ge 1, \quad i = 1, \dots, N,
$$
得到最优解 $(\boldsymbol{w}^*, b^*)$，以分离超平面 $\boldsymbol{w}^* \cdot \boldsymbol{x} + b^* = 0$ 和决策函数 $g(\boldsymbol{x}) = \operatorname{sgn}(\boldsymbol{w}^* \cdot \boldsymbol{x} + b^*)$ 分类。这一模型称为线性可分支持向量机，或**硬间隔**支持向量机。使约束取等号 $y_i(\boldsymbol{w}^* \cdot \boldsymbol{x}_i + b^*) = 1$ 的样本点称为**支持向量**。

支持向量落在两个超平面 $\boldsymbol{w}^* \cdot \boldsymbol{x} + b^* = \pm 1$ 上，二者之间的带状区域宽度为 $2/\|\boldsymbol{w}^*\|$，称为间隔带。分离超平面只由支持向量决定：移动或删去间隔带以外的点，只要它不进入间隔带，解就不变。这与 LDA 不同，后者通过均值与协方差用到所有样本（[3.4.10](/3.4.10)）。

![线性可分数据上的最大间隔分离直线（实线）与间隔边界（虚线）；圆圈标出的是支持向量，它们恰好落在间隔边界上，其余样本不影响解](./plots/max-margin.py)

**定理 5.2.1（最大间隔分离超平面的存在唯一性）** 若训练集线性可分（且两类都非空），则定义 5.2.1 中的最优化问题的解存在且唯一。

**证明** 存在性：线性可分时，把分离超平面适当缩放就满足约束，可行域非空。目标函数 $\frac12\|\boldsymbol{w}\|^2$ 连续，下水平集 $\{\|\boldsymbol{w}\| \le r\}$ 中可行的 $b$ 也有界（取一个正例 $\boldsymbol{x}_p$ 和一个负例 $\boldsymbol{x}_q$，约束给出 $1 - \boldsymbol{w} \cdot \boldsymbol{x}_p \le b \le -1 - \boldsymbol{w} \cdot \boldsymbol{x}_q$），所以最小值可以在一个紧集上取得。又因为两类都非空，最优解中 $\boldsymbol{w}^* \ne \boldsymbol{0}$（$\boldsymbol{w} = \boldsymbol{0}$ 时约束要求 $b \ge 1$ 且 $-b \ge 1$，不可能）。

唯一性：设 $(\boldsymbol{w}_1, b_1)$、$(\boldsymbol{w}_2, b_2)$ 都是最优解，$\|\boldsymbol{w}_1\| = \|\boldsymbol{w}_2\| = c$。可行域是凸集，二者的中点 $(\boldsymbol{w}, b) = \bigl(\frac{\boldsymbol{w}_1 + \boldsymbol{w}_2}{2}, \frac{b_1 + b_2}{2}\bigr)$ 也可行，所以 $c \le \|\boldsymbol{w}\| \le \frac12\|\boldsymbol{w}_1\| + \frac12\|\boldsymbol{w}_2\| = c$。三角不等式取等号，说明 $\boldsymbol{w}_1 = \lambda \boldsymbol{w}_2$，$\lambda > 0$，而模长相等迫使 $\lambda = 1$，即 $\boldsymbol{w}_1 = \boldsymbol{w}_2 = \boldsymbol{w}^*$。再证 $b_1 = b_2$：对 $(\boldsymbol{w}^*, b_1)$，必有某个正例使约束取等号，否则把 $b_1$ 略微减小、再把 $(\boldsymbol{w}^*, b_1)$ 略微缩小仍可行，与 $\|\boldsymbol{w}^*\|$ 最小矛盾；同理必有某个负例取等号。于是 $b_1 = 1 - \min_{y_i = +1}\boldsymbol{w}^* \cdot \boldsymbol{x}_i = -1 - \max_{y_i = -1}\boldsymbol{w}^* \cdot \boldsymbol{x}_i$ 由 $\boldsymbol{w}^*$ 唯一确定，$b_2$ 也是如此。$\square$

### 5.2.2. Lagrange 对偶与 KKT 条件

硬间隔问题可以直接用二次规划求解，但转到对偶问题有两个好处：对偶问题更容易求解（§5.5），而且自然地引出核技巧（§5.4）。先看一般的约束优化问题（原始问题）：

$$
\min_{\boldsymbol{x}}\ f_0(\boldsymbol{x}) \quad \text{s.t.} \quad f_i(\boldsymbol{x}) \le 0\ (i = 1, \dots, m), \quad h_j(\boldsymbol{x}) = 0\ (j = 1, \dots, p),
$$
最优值记为 $p^*$。仿照 **Lagrange 乘子法**，对每个约束引入乘子，定义 Lagrange 函数

$$
L(\boldsymbol{x}, \boldsymbol{\alpha}, \boldsymbol{\beta}) = f_0(\boldsymbol{x}) + \sum_{i=1}^{m} \alpha_i f_i(\boldsymbol{x}) + \sum_{j=1}^{p} \beta_j h_j(\boldsymbol{x}), \qquad \alpha_i \ge 0.
$$
对固定的 $\boldsymbol{x}$，若它满足所有约束，则 $\max_{\boldsymbol{\alpha} \ge \boldsymbol{0}, \boldsymbol{\beta}} L = f_0(\boldsymbol{x})$（取 $\boldsymbol{\alpha} = \boldsymbol{0}$）；若它违反某个约束，相应的乘子可以任意大，$\max L = +\infty$。所以原始问题等价于极小极大问题 $p^* = \min_{\boldsymbol{x}} \max_{\boldsymbol{\alpha} \ge \boldsymbol{0}, \boldsymbol{\beta}} L(\boldsymbol{x}, \boldsymbol{\alpha}, \boldsymbol{\beta})$。交换 min 与 max 的次序，就得到

**定义 5.2.2（对偶问题）** 函数 $d(\boldsymbol{\alpha}, \boldsymbol{\beta}) = \inf_{\boldsymbol{x}} L(\boldsymbol{x}, \boldsymbol{\alpha}, \boldsymbol{\beta})$ 称为 Lagrange 对偶函数。问题

$$
\max_{\boldsymbol{\alpha}, \boldsymbol{\beta}}\ d(\boldsymbol{\alpha}, \boldsymbol{\beta}) \quad \text{s.t.} \quad \boldsymbol{\alpha} \ge \boldsymbol{0}
$$
称为原始问题的（Lagrange）**对偶问题**，最优值记为 $d^*$。

对偶函数是一族关于 $(\boldsymbol{\alpha}, \boldsymbol{\beta})$ 的仿射函数的下确界，因而总是凹函数；无论原始问题是否为凸，对偶问题都是凸优化问题。

**定理 5.2.2（弱对偶）** $d^* \le p^*$。

**证明** 对任意可行的 $\tilde{\boldsymbol{x}}$ 和任意 $\boldsymbol{\alpha} \ge \boldsymbol{0}$、$\boldsymbol{\beta}$，有 $\alpha_i f_i(\tilde{\boldsymbol{x}}) \le 0$、$h_j(\tilde{\boldsymbol{x}}) = 0$，所以 $d(\boldsymbol{\alpha}, \boldsymbol{\beta}) \le L(\tilde{\boldsymbol{x}}, \boldsymbol{\alpha}, \boldsymbol{\beta}) \le f_0(\tilde{\boldsymbol{x}})$。左边对 $(\boldsymbol{\alpha}, \boldsymbol{\beta})$ 取上确界、右边对 $\tilde{\boldsymbol{x}}$ 取下确界即得。$\square$

这正是一般的极大极小不等式 $\max_y \min_x L \le \min_x \max_y L$。$d^* = p^*$ 时称强对偶成立，这时可以通过求解对偶问题来求解原始问题。强对偶一般不成立，但对凸问题有一个简单的充分条件：

**定理 5.2.3（Slater 条件）** 设 $f_0, f_1, \dots, f_m$ 是凸函数，$h_j$ 是仿射函数。若存在严格可行点，即存在 $\tilde{\boldsymbol{x}}$ 使 $f_i(\tilde{\boldsymbol{x}}) < 0$ 对所有 $i$ 成立、$h_j(\tilde{\boldsymbol{x}}) = 0$ 对所有 $j$ 成立，则强对偶成立，且 $d^* > -\infty$ 时对偶问题的最优值可以取到。若不等式约束都是仿射的，只需可行域非空。

强对偶成立时，原始最优解与对偶最优解之间的关系由下面的条件刻画。

**定义 5.2.3（KKT 条件）** 设 $f_i$、$h_j$ 可微。称 $(\boldsymbol{x}^*, \boldsymbol{\alpha}^*, \boldsymbol{\beta}^*)$ 满足 **KKT 条件**（Karush–Kuhn–Tucker 条件），如果

$$
\begin{aligned}
& \nabla_{\boldsymbol{x}} L(\boldsymbol{x}^*, \boldsymbol{\alpha}^*, \boldsymbol{\beta}^*) = \boldsymbol{0} && \text{（稳定性）}\\
& f_i(\boldsymbol{x}^*) \le 0, \quad h_j(\boldsymbol{x}^*) = 0 && \text{（原始可行）}\\
& \alpha_i^* \ge 0 && \text{（对偶可行）}\\
& \alpha_i^* f_i(\boldsymbol{x}^*) = 0 && \text{（互补松弛）}
\end{aligned}
$$
对所有 $i = 1, \dots, m$、$j = 1, \dots, p$ 成立。

**定理 5.2.4** (1) 若强对偶成立，$\boldsymbol{x}^*$ 是原始最优解，$(\boldsymbol{\alpha}^*, \boldsymbol{\beta}^*)$ 是对偶最优解，且各函数可微，则它们满足 KKT 条件。(2) 若原始问题是凸的（$f_0, f_i$ 凸，$h_j$ 仿射），则满足 KKT 条件的 $\boldsymbol{x}^*$ 与 $(\boldsymbol{\alpha}^*, \boldsymbol{\beta}^*)$ 分别是原始与对偶最优解，且强对偶成立。

**证明** (1) 由强对偶与弱对偶证明中的不等式链，

$$
f_0(\boldsymbol{x}^*) = d(\boldsymbol{\alpha}^*, \boldsymbol{\beta}^*) \le L(\boldsymbol{x}^*, \boldsymbol{\alpha}^*, \boldsymbol{\beta}^*) = f_0(\boldsymbol{x}^*) + \sum_i \alpha_i^* f_i(\boldsymbol{x}^*) \le f_0(\boldsymbol{x}^*),
$$
所以两个不等号都取等号。第二个等号给出 $\sum_i \alpha_i^* f_i(\boldsymbol{x}^*) = 0$，而每一项都 $\le 0$，故每一项为零，即互补松弛；第一个等号说明 $\boldsymbol{x}^*$ 是 $L(\cdot, \boldsymbol{\alpha}^*, \boldsymbol{\beta}^*)$ 的极小值点，故梯度为零。可行性是已知的。(2) 凸问题中 $\alpha_i^* \ge 0$，$L(\cdot, \boldsymbol{\alpha}^*, \boldsymbol{\beta}^*)$ 是凸函数，梯度为零说明 $\boldsymbol{x}^*$ 是它的全局极小值点，于是 $d(\boldsymbol{\alpha}^*, \boldsymbol{\beta}^*) = L(\boldsymbol{x}^*, \boldsymbol{\alpha}^*, \boldsymbol{\beta}^*) = f_0(\boldsymbol{x}^*)$（由互补松弛与原始可行）。由弱对偶，$\boldsymbol{x}^*$ 的原始目标值等于 $(\boldsymbol{\alpha}^*, \boldsymbol{\beta}^*)$ 的对偶目标值，二者都是最优的。$\square$

互补松弛的含义是：若约束在最优解处不起作用（$f_i(\boldsymbol{x}^*) < 0$），相应的乘子为 0；乘子为正，约束必取等号。

### 5.2.3. 支持向量机的对偶问题

把硬间隔问题的约束写成 $1 - y_i(\boldsymbol{w} \cdot \boldsymbol{x}_i + b) \le 0$，Lagrange 函数为

$$
L(\boldsymbol{w}, b, \boldsymbol{\alpha}) = \frac12\|\boldsymbol{w}\|^2 + \sum_{i=1}^{N} \alpha_i\bigl(1 - y_i(\boldsymbol{w} \cdot \boldsymbol{x}_i + b)\bigr), \qquad \alpha_i \ge 0.
$$
约束是仿射的，可行域非空，由定理 5.2.3 强对偶成立。求对偶函数：对 $\boldsymbol{w}$、$b$ 求偏导并令其为零，

$$
\nabla_{\boldsymbol{w}} L = \boldsymbol{w} - \sum_{i=1}^{N} \alpha_i y_i \boldsymbol{x}_i = \boldsymbol{0}, \qquad \frac{\partial L}{\partial b} = -\sum_{i=1}^{N} \alpha_i y_i = 0.
$$
（若 $\sum_i \alpha_i y_i \ne 0$，$L$ 关于 $b$ 无下界，对偶函数为 $-\infty$，所以这是对偶问题的约束。）代回 $L$ 得

$$
d(\boldsymbol{\alpha}) = -\frac12 \sum_{i=1}^{N}\sum_{j=1}^{N} \alpha_i \alpha_j y_i y_j (\boldsymbol{x}_i \cdot \boldsymbol{x}_j) + \sum_{i=1}^{N} \alpha_i.
$$
把求极大改为求其相反数的极小，就得到硬间隔支持向量机的对偶问题：

$$
\min_{\boldsymbol{\alpha}}\ \frac12 \sum_{i=1}^{N}\sum_{j=1}^{N} \alpha_i \alpha_j y_i y_j (\boldsymbol{x}_i \cdot \boldsymbol{x}_j) - \sum_{i=1}^{N} \alpha_i \quad \text{s.t.} \quad \sum_{i=1}^{N} \alpha_i y_i = 0, \quad \alpha_i \ge 0. \tag{5.1}
$$

设 $\boldsymbol{\alpha}^*$ 是它的最优解。由 KKT 条件（定理 5.2.4）：

- 稳定性给出 $\boldsymbol{w}^* = \sum_i \alpha_i^* y_i \boldsymbol{x}_i$；
- 因为 $\boldsymbol{w}^* \ne \boldsymbol{0}$，至少有一个 $\alpha_j^* > 0$，由互补松弛 $y_j(\boldsymbol{w}^* \cdot \boldsymbol{x}_j + b^*) = 1$，两边乘以 $y_j$（$y_j^2 = 1$）得

$$
b^* = y_j - \sum_{i=1}^{N} \alpha_i^* y_i (\boldsymbol{x}_i \cdot \boldsymbol{x}_j).
$$

于是决策函数为

$$
g(\boldsymbol{x}) = \operatorname{sgn}\Bigl(\sum_{i=1}^{N} \alpha_i^* y_i (\boldsymbol{x}_i \cdot \boldsymbol{x}) + b^*\Bigr).
$$
由互补松弛，$\alpha_i^* > 0$ 的样本一定是支持向量；反之不一定成立：在退化的情形下，恰好落在间隔边界上的样本也可能有 $\alpha_i^* = 0$。所以通常把 $\alpha_i^* > 0$ 的样本称为支持向量，它们完全决定了 $\boldsymbol{w}^*$ 与 $b^*$。另外，训练和预测都只用到样本之间的内积 $\boldsymbol{x}_i \cdot \boldsymbol{x}_j$，这是 §5.4 的出发点。

### 5.2.4. 例

**例 5.2.1** 正例 $\boldsymbol{x}_1 = (2, 2)$、$\boldsymbol{x}_2 = (3, 3)$，负例 $\boldsymbol{x}_3 = (0, 1)$，求硬间隔支持向量机。

内积为 $\boldsymbol{x}_1 \cdot \boldsymbol{x}_1 = 8$，$\boldsymbol{x}_1 \cdot \boldsymbol{x}_2 = 12$，$\boldsymbol{x}_1 \cdot \boldsymbol{x}_3 = 2$，$\boldsymbol{x}_2 \cdot \boldsymbol{x}_2 = 18$，$\boldsymbol{x}_2 \cdot \boldsymbol{x}_3 = 3$，$\boldsymbol{x}_3 \cdot \boldsymbol{x}_3 = 1$。对偶问题 (5.1) 为

$$
\min_{\boldsymbol{\alpha}}\ \frac12\bigl(8\alpha_1^2 + 18\alpha_2^2 + \alpha_3^2 + 24\alpha_1\alpha_2 - 4\alpha_1\alpha_3 - 6\alpha_2\alpha_3\bigr) - \alpha_1 - \alpha_2 - \alpha_3
$$
约束为 $\alpha_1 + \alpha_2 - \alpha_3 = 0$，$\alpha_i \ge 0$。把 $\alpha_3 = \alpha_1 + \alpha_2$ 代入，目标化为

$$
s(\alpha_1, \alpha_2) = \frac52\alpha_1^2 + \frac{13}{2}\alpha_2^2 + 8\alpha_1\alpha_2 - 2\alpha_1 - 2\alpha_2.
$$
令偏导数为零：$5\alpha_1 + 8\alpha_2 = 2$，$8\alpha_1 + 13\alpha_2 = 2$，解得 $\alpha_1 = 10$、$\alpha_2 = -6$，不满足 $\alpha_2 \ge 0$，所以最小值在边界上。$\alpha_2 = 0$ 时 $s = \frac52\alpha_1^2 - 2\alpha_1$，在 $\alpha_1 = \frac25$ 处取最小值 $-\frac25$；$\alpha_1 = 0$ 时 $s = \frac{13}{2}\alpha_2^2 - 2\alpha_2$，在 $\alpha_2 = \frac{2}{13}$ 处取最小值 $-\frac{2}{13} > -\frac25$。所以

$$
\boldsymbol{\alpha}^* = \Bigl(\frac25, 0, \frac25\Bigr), \quad \boldsymbol{w}^* = \frac25(2, 2) - \frac25(0, 1) = \Bigl(\frac45, \frac25\Bigr), \quad b^* = 1 - \boldsymbol{w}^* \cdot \boldsymbol{x}_1 = -\frac75.
$$
分离超平面为 $\frac45 x^{(1)} + \frac25 x^{(2)} - \frac75 = 0$，即 $4x^{(1)} + 2x^{(2)} = 7$，支持向量是 $\boldsymbol{x}_1$ 与 $\boldsymbol{x}_3$。检验：$\boldsymbol{w}^* \cdot \boldsymbol{x}_3 + b^* = -1$，$\boldsymbol{w}^* \cdot \boldsymbol{x}_2 + b^* = \frac{11}{5} > 1$；间隔为 $1/\|\boldsymbol{w}^*\| = \sqrt5/2$，恰为 $\boldsymbol{x}_1$ 与 $\boldsymbol{x}_3$ 距离的一半，$\boldsymbol{w}^*$ 与 $\boldsymbol{x}_1 - \boldsymbol{x}_3 = (2, 1)$ 同方向。§5.5 的程序给出同样的结果。

## 5.3. 软间隔支持向量机

### 5.3.1. 松弛变量

实际数据常常不是线性可分的，或者虽然可分，却因为少数噪声点而只能得到很窄的间隔。允许一些样本不满足"函数间隔至少为 1"：为每个样本引入松弛变量 $\xi_i \ge 0$，约束放宽为 $y_i(\boldsymbol{w} \cdot \boldsymbol{x}_i + b) \ge 1 - \xi_i$，同时在目标中惩罚松弛的总量。

**定义 5.3.1（软间隔支持向量机）** 求解凸二次规划

$$
\min_{\boldsymbol{w}, b, \boldsymbol{\xi}}\ \frac12\|\boldsymbol{w}\|^2 + C\sum_{i=1}^{N} \xi_i \quad \text{s.t.} \quad y_i(\boldsymbol{w} \cdot \boldsymbol{x}_i + b) \ge 1 - \xi_i, \quad \xi_i \ge 0, \quad i = 1, \dots, N,
$$
其中 $C > 0$ 为惩罚参数，以 $g(\boldsymbol{x}) = \operatorname{sgn}(\boldsymbol{w}^* \cdot \boldsymbol{x} + b^*)$ 分类。这一模型称为线性支持向量机，或**软间隔**支持向量机。

$\xi_i = 0$ 的样本在间隔带外或边界上；$0 < \xi_i \le 1$ 的样本落在间隔带内但仍被正确分类；$\xi_i > 1$ 的样本被分错。所以 $\sum_i \xi_i$ 是训练误差个数的一个上界。$C$ 调节两个目标：$C$ 大时对违反间隔的惩罚重，间隔窄、训练误差少，$C \to \infty$ 就是硬间隔；$C$ 小时间隔宽，容忍更多误差。$C$ 是超参数，通常用**交叉验证**选择。软间隔问题总有可行解（取 $\xi_i$ 足够大），可以证明 $\boldsymbol{w}^*$ 唯一，而 $b^*$ 可能不唯一。

![重叠的两类数据上，C 取 0.02、1、100 时的线性软间隔支持向量机：C 小时间隔宽、支持向量多，C 大时间隔窄、支持向量少；圆圈标出支持向量（α > 0 的样本）](./plots/soft-margin.py)

### 5.3.2. 对偶问题

对两组约束分别引入乘子 $\alpha_i \ge 0$、$\mu_i \ge 0$，

$$
L = \frac12\|\boldsymbol{w}\|^2 + C\sum_i \xi_i + \sum_i \alpha_i\bigl(1 - \xi_i - y_i(\boldsymbol{w} \cdot \boldsymbol{x}_i + b)\bigr) - \sum_i \mu_i \xi_i.
$$
对 $\boldsymbol{w}$、$b$ 求偏导与硬间隔相同；对 $\xi_i$ 求偏导得 $C - \alpha_i - \mu_i = 0$。代回后 $\xi_i$ 与 $\mu_i$ 全部消去，对偶目标与 (5.1) 完全相同，唯一的变化是 $\mu_i = C - \alpha_i \ge 0$ 给出 $\alpha_i \le C$：

$$
\min_{\boldsymbol{\alpha}}\ \frac12 \sum_{i=1}^{N}\sum_{j=1}^{N} \alpha_i \alpha_j y_i y_j (\boldsymbol{x}_i \cdot \boldsymbol{x}_j) - \sum_{i=1}^{N} \alpha_i \quad \text{s.t.} \quad \sum_{i=1}^{N} \alpha_i y_i = 0, \quad 0 \le \alpha_i \le C. \tag{5.2}
$$

由 KKT 条件，记 $f(\boldsymbol{x}) = \boldsymbol{w}^* \cdot \boldsymbol{x} + b^*$，互补松弛 $\alpha_i(1 - \xi_i - y_i f(\boldsymbol{x}_i)) = 0$、$\mu_i \xi_i = (C - \alpha_i)\xi_i = 0$ 把样本分为三类：

| $\alpha_i^*$ | $\xi_i$ | $y_i f(\boldsymbol{x}_i)$ | 位置 |
|---|---|---|---|
| $0$ | $0$ | $\ge 1$ | 间隔带外或边界上，不是支持向量 |
| $(0, C)$ | $0$ | $= 1$ | 恰在间隔边界上（自由支持向量） |
| $C$ | $1 - y_i f(\boldsymbol{x}_i) \ge 0$ | $\le 1$ | 间隔带内或被分错（有界支持向量） |

这些条件在 §5.5 中用作停止准则。$\boldsymbol{w}^* = \sum_i \alpha_i^* y_i \boldsymbol{x}_i$ 照旧；$b^*$ 由任一自由支持向量（$0 < \alpha_j^* < C$）算出 $b^* = y_j - \sum_i \alpha_i^* y_i(\boldsymbol{x}_i \cdot \boldsymbol{x}_j)$，数值计算中常对所有自由支持向量取平均。

### 5.3.3. 合页损失

软间隔支持向量机还有一个等价的写法，它把支持向量机放进 §5.1.1 的结构风险最小化框架。

**定义 5.3.2（合页损失）** 对标签 $y \in \{+1, -1\}$ 和实值预测 $f(\boldsymbol{x})$，**合页损失**为

$$
L_{\mathrm{hinge}}(y, f(\boldsymbol{x})) = \max\bigl(0,\ 1 - y f(\boldsymbol{x})\bigr) = [1 - y f(\boldsymbol{x})]_+.
$$

**定理 5.3.1** 定义 5.3.1 的软间隔问题等价于无约束问题

$$
\min_{\boldsymbol{w}, b}\ \sum_{i=1}^{N} \bigl[1 - y_i(\boldsymbol{w} \cdot \boldsymbol{x}_i + b)\bigr]_+ + \lambda\|\boldsymbol{w}\|^2, \qquad \lambda = \frac{1}{2C}.
$$

**证明** 固定 $(\boldsymbol{w}, b)$，软间隔问题对 $\xi_i$ 的约束是 $\xi_i \ge 1 - y_i(\boldsymbol{w} \cdot \boldsymbol{x}_i + b)$ 且 $\xi_i \ge 0$，目标关于 $\xi_i$ 递增，所以最优的 $\xi_i = [1 - y_i(\boldsymbol{w} \cdot \boldsymbol{x}_i + b)]_+$。代入后目标为 $\frac12\|\boldsymbol{w}\|^2 + C\sum_i [\cdot]_+$，除以 $C$ 即得。$\square$

合页损失在 $yf \ge 1$ 时为零：分类正确且有足够把握的样本完全不产生损失，这正是解只依赖于支持向量的原因。它是 0-1 损失 $\boldsymbol{1}_{\{yf \le 0\}}$ 的一个凸上界。把它换成 $\log(1 + \mathrm{e}^{-yf})$ 就得到带 $L_2$ 正则的 **logistic 回归**，换成 $(1 - yf)^2$ 得到最小二乘分类；几种损失都是 0-1 损失的凸代理，区别在于对"分得很对"的样本是否还给出梯度。无约束形式也提供了另一种求解方法：对它做次梯度下降或**随机梯度下降**（如 Pegasos 算法），在样本很多的线性问题上比解对偶问题快得多。

## 5.4. 核方法

### 5.4.1. 非线性分类与特征映射

有些问题在原空间中用任何超平面都分不好，例如一类样本在圆内、另一类在圆外。这时可以先用一个变换 $\phi$ 把数据映射到新的特征空间，再在新空间中用线性方法。平面上取

$$
\phi(\boldsymbol{x}) = \bigl((x^{(1)})^2,\ \sqrt2\, x^{(1)} x^{(2)},\ (x^{(2)})^2\bigr),
$$
圆 $(x^{(1)})^2 + (x^{(2)})^2 = r^2$ 在新空间中就是平面 $z_1 + z_3 = r^2$，圆内外两类变成线性可分的。一般地，原空间中的二次曲线对应于特征 $\bigl(1, x^{(1)}, x^{(2)}, (x^{(1)})^2, x^{(1)}x^{(2)}, (x^{(2)})^2\bigr)$ 空间中的超平面，[3.4.10](/3.4.10) 的 §10.7.2 已用这一想法把 LDA 推广为二次分界。

问题在于维数：$n$ 维输入的全部 $d$ 次单项式有 $\binom{n+d-1}{d}$ 个，$n = 100$、$d = 3$ 时已有 17 万多个，显式计算 $\phi$ 代价很大，有时特征空间甚至是无穷维的。

### 5.4.2. 核技巧

对偶问题 (5.2) 与决策函数中，样本只以内积的形式出现。换到特征空间后，只需把 $\boldsymbol{x}_i \cdot \boldsymbol{x}_j$ 换成 $\phi(\boldsymbol{x}_i) \cdot \phi(\boldsymbol{x}_j)$。而这个内积往往可以不经过 $\phi$ 直接算出：对上面的 $\phi$，

$$
\phi(\boldsymbol{x}) \cdot \phi(\boldsymbol{z}) = (x^{(1)}z^{(1)})^2 + 2x^{(1)}x^{(2)}z^{(1)}z^{(2)} + (x^{(2)}z^{(2)})^2 = (\boldsymbol{x} \cdot \boldsymbol{z})^2.
$$
计算右边只需 $O(n)$ 次运算，而不是 $O(n^2)$。

**定义 5.4.1（核技巧）** 在只依赖于样本内积的算法中，把内积 $\boldsymbol{x} \cdot \boldsymbol{z}$ 换成核函数 $K(\boldsymbol{x}, \boldsymbol{z}) = \phi(\boldsymbol{x}) \cdot \phi(\boldsymbol{z})$，从而隐式地在特征空间中运行该算法而不显式计算特征映射 $\phi$，这种做法称为**核技巧**。

什么样的 $K$ 是某个特征映射的内积？答案是**正定核**（[3.4.6](/3.4.6)）：$K$ 对称，且对任意有限个点 $\boldsymbol{x}_1, \dots, \boldsymbol{x}_N$，矩阵 $[K(\boldsymbol{x}_i, \boldsymbol{x}_j)]$ 半正定。每个正定核都对应一个（可能无穷维的）Hilbert 空间中的特征映射（Mercer 定理，或再生核 Hilbert 空间的构造）。核矩阵半正定也保证了对偶问题仍是凸二次规划。常用的核有：

| 核 | $K(\boldsymbol{x}, \boldsymbol{z})$ | 特征空间 | 说明 |
|---|---|---|---|
| 线性核 | $\boldsymbol{x} \cdot \boldsymbol{z}$ | 原空间 | 即线性支持向量机 |
| **多项式核** | $(\boldsymbol{x} \cdot \boldsymbol{z} + c)^d$，$c \ge 0$ | 所有不超过 $d$ 次的单项式 | |
| **Gauss 核** | $\exp\bigl(-\|\boldsymbol{x} - \boldsymbol{z}\|^2 / (2\sigma^2)\bigr)$ | 无穷维 | 又称 RBF 核，最常用 |
| sigmoid 核 | $\tanh(a\,\boldsymbol{x} \cdot \boldsymbol{z} + r)$ | | 一般不是正定核 |

用核函数代替内积，就得到非线性支持向量机：求解

$$
\min_{\boldsymbol{\alpha}}\ \frac12 \sum_{i=1}^{N}\sum_{j=1}^{N} \alpha_i \alpha_j y_i y_j K(\boldsymbol{x}_i, \boldsymbol{x}_j) - \sum_{i=1}^{N} \alpha_i \quad \text{s.t.} \quad \sum_{i=1}^{N} \alpha_i y_i = 0, \quad 0 \le \alpha_i \le C,
$$
选一个 $0 < \alpha_j^* < C$，计算 $b^* = y_j - \sum_i \alpha_i^* y_i K(\boldsymbol{x}_i, \boldsymbol{x}_j)$，决策函数为

$$
g(\boldsymbol{x}) = \operatorname{sgn}\Bigl(\sum_{i=1}^{N} \alpha_i^* y_i K(\boldsymbol{x}_i, \boldsymbol{x}) + b^*\Bigr).
$$
$\boldsymbol{w}^* = \sum_i \alpha_i^* y_i \phi(\boldsymbol{x}_i)$ 在特征空间中，一般不显式计算。用 Gauss 核时，决策函数是以各支持向量为中心的 Gauss 函数的加权和。

Gauss 核的宽度 $\sigma$ 控制模型的复杂度：$\sigma$ 大时核函数变化平缓，每个支持向量影响很大的范围，决策边界接近线性，可能欠拟合；$\sigma$ 小时每个支持向量只影响很小的邻域，边界可以绕着单个样本弯曲，训练误差趋于零而泛化能力很差，即过拟合。$\sigma$ 与 $C$ 一起用交叉验证选择。

![Gauss 核支持向量机（C = 10）在两个交错的半月形数据上的决策边界：σ = 3 时边界几乎是直线（欠拟合）；σ = 0.4 时边界贴合数据的形状；σ = 0.05 时边界绕着每个样本弯曲，训练准确率为 1 而几乎所有样本都成为支持向量（过拟合）](./plots/rbf-width.py)

核技巧不限于支持向量机：核主成分分析（[3.4.6](/3.4.6)）、核岭回归、Gauss 过程都基于同样的想法。它的代价是需要 $N \times N$ 的核矩阵，样本数到几十万以上时，计算与存储都成为瓶颈，这也是深度学习在大数据上取代核方法的原因之一；随机特征（Rahimi 与 Recht，2007）等方法用显式的低维随机特征近似核函数，缓解了这一问题。

## 5.5. SMO 算法

对偶问题是一个凸二次规划，有全局最优解，通用的二次规划算法也能求解；但样本数 $N$ 大时，$N \times N$ 的核矩阵放不进内存，通用算法非常慢。Platt（1998）提出的序列最小最优化（SMO）算法每次只优化两个变量，固定其余变量，两变量的子问题有解析解。

为什么是两个？等式约束 $\sum_i \alpha_i y_i = 0$ 使得只改变一个 $\alpha_i$ 必然破坏约束，至少要同时改两个。设选中 $\alpha_1$、$\alpha_2$，其余固定，则

$$
\alpha_1 y_1 + \alpha_2 y_2 = -\sum_{i \ge 3} \alpha_i y_i = \text{常数},
$$
$(\alpha_1, \alpha_2)$ 只能在方框 $[0, C]^2$ 内的一条线段上移动，问题化为一元二次函数在区间上求极小。记 $f(\boldsymbol{x}) = \sum_i \alpha_i y_i K(\boldsymbol{x}_i, \boldsymbol{x}) + b$，$E_i = f(\boldsymbol{x}_i) - y_i$ 为预测误差，$\eta = K_{11} + K_{22} - 2K_{12}$（$K_{ij} = K(\boldsymbol{x}_i, \boldsymbol{x}_j)$，正定核下 $\eta \ge 0$）。沿线段求导可得未加约束的最优解

$$
\alpha_2^{\mathrm{new, unc}} = \alpha_2 + \frac{y_2(E_1 - E_2)}{\eta},
$$
再把它截断到线段的端点范围 $[L, H]$ 内：

$$
\begin{aligned}
y_1 \ne y_2: \quad & L = \max(0, \alpha_2 - \alpha_1), & H &= \min(C, C + \alpha_2 - \alpha_1),\\
y_1 = y_2: \quad & L = \max(0, \alpha_1 + \alpha_2 - C), & H &= \min(C, \alpha_1 + \alpha_2),
\end{aligned}
$$
然后由等式约束得 $\alpha_1^{\mathrm{new}} = \alpha_1 + y_1 y_2(\alpha_2 - \alpha_2^{\mathrm{new}})$，并更新 $b$，使取值在 $(0, C)$ 内的那个乘子对应的样本满足 $y f(\boldsymbol{x}) = 1$。

选择变量的启发式：第一个变量选违反 KKT 条件（§5.3.2 的表）最严重的样本；第二个变量选使 $\lvert E_1 - E_2 \rvert$ 最大的样本，使这一步的改变尽量大；若这样选不能使目标下降，再依次尝试其他样本。每一步都使对偶目标不增；所有样本都在容差内满足 KKT 条件时停止。

```python
import numpy as np

def smo(K, y, C, tol=1e-3, max_iter=10000):
    """Sequential minimal optimization for the SVM dual, given the kernel matrix K."""
    n = len(y)
    alpha, b = np.zeros(n), 0.0
    for it in range(max_iter):
        E = (alpha * y) @ K + b - y                      # prediction errors f(x_i) - y_i
        # KKT violations: alpha_i < C needs y_i f_i >= 1, alpha_i > 0 needs y_i f_i <= 1
        viol = ((y * E < -tol) & (alpha < C)) | ((y * E > tol) & (alpha > 0))
        if not viol.any():
            break                                       # all KKT conditions hold
        i = int(np.argmax(np.where(viol, np.abs(y * E), -1)))   # worst violator
        for j in np.argsort(-np.abs(E - E[i])):        # partner with largest |E_i - E_j| first
            if j == i:
                continue
            if y[i] != y[j]:
                L, H = max(0, alpha[j] - alpha[i]), min(C, C + alpha[j] - alpha[i])
            else:
                L, H = max(0, alpha[i] + alpha[j] - C), min(C, alpha[i] + alpha[j])
            eta = K[i, i] + K[j, j] - 2 * K[i, j]
            if L >= H or eta <= 0:
                continue
            aj = np.clip(alpha[j] + y[j] * (E[i] - E[j]) / eta, L, H)
            if abs(aj - alpha[j]) < 1e-12:
                continue
            ai = alpha[i] + y[i] * y[j] * (alpha[j] - aj)
            # update b so that a multiplier strictly inside (0, C) satisfies y f = 1
            b1 = b - E[i] - y[i] * (ai - alpha[i]) * K[i, i] - y[j] * (aj - alpha[j]) * K[i, j]
            b2 = b - E[j] - y[i] * (ai - alpha[i]) * K[i, j] - y[j] * (aj - alpha[j]) * K[j, j]
            b = b1 if 0 < ai < C else b2 if 0 < aj < C else (b1 + b2) / 2
            alpha[i], alpha[j] = ai, aj
            break
    return alpha, b, it

# Example 5.2.1: hard margin (a very large C).
X = np.array([[2.0, 2.0], [3.0, 3.0], [0.0, 1.0]])
y = np.array([1.0, 1.0, -1.0])
alpha, b, _ = smo(X @ X.T, y, C=1e6)
print("alpha =", np.round(alpha, 4), " w =", np.round((alpha * y) @ X, 4), " b =", round(b, 4))

# Two noisy concentric rings with a Gaussian kernel (sigma = 0.5).
rng = np.random.default_rng(0)
n = 200
r = np.r_[rng.normal(1.0, 0.25, n // 2), rng.normal(2.2, 0.25, n // 2)]
t = rng.uniform(0, 2 * np.pi, n)
X = np.c_[r * np.cos(t), r * np.sin(t)]
y = np.r_[np.ones(n // 2), -np.ones(n // 2)]
sq = np.sum(X**2, 1)
K = np.exp(-(sq[:, None] + sq[None, :] - 2 * X @ X.T) / (2 * 0.5**2))
alpha, b, iterations = smo(K, y, C=1.0)
pred = np.sign((alpha * y) @ K + b)
print("iterations:", iterations, " support vectors:", int(np.sum(alpha > 1e-8)),
      " training accuracy:", np.mean(pred == y))
```

```text
alpha = [0.4 0.  0.4]  w = [0.8 0.4]  b = -1.4
iterations: 304  support vectors: 61  training accuracy: 0.995
```

这里为简洁起见每一步都重新计算全部误差 $E$（$O(N^2)$），实际的实现只增量地更新它们。在圆环数据上，所得的对偶目标值与通用二次规划求解器的结果相差不到 $10^{-4}$。

SMO 及其改进是 LIBSVM 等软件的核心：Fan、Chen 与 Lin（2005）用二阶信息选择工作集，并结合缓存与"收缩"（暂时剔除很可能停在边界上的变量）；Keerthi 与 Gilbert（2002）证明了这类方法的收敛性。经验上，核支持向量机的训练时间介于 $O(N^2)$ 与 $O(N^3)$ 之间。对线性支持向量机，LIBLINEAR 的对偶坐标下降和基于合页损失的随机梯度方法可以处理上百万个样本与特征。

## 5.6. 多类分类与应用

支持向量机是二类分类器。处理 $K$ 类问题有几种组合方法：

- 一对多（one-vs-rest）：训练 $K$ 个分类器，第 $k$ 个以第 $k$ 类为正例、其余为负例；预测时取 $f_k(\boldsymbol{x})$ 最大的类。
- 一对一（one-vs-one）：每两类训练一个分类器，共 $K(K-1)/2$ 个，每个只用两类的数据；预测时投票。LIBSVM 默认采用这种方法。
- 层次法：先把所有类分成两组，每组再分成两组，形成一棵二叉树。

**例 5.6.1（文本分类）** 把文档 $j$ 表示为向量空间模型中的向量 $(w_{1j}, \dots, w_{nj})$，$w_{ij}$ 是词项 $i$ 在文档 $j$ 中的权重，最简单的取词频 $\mathrm{tf}_{ij}$。常用的 tf-idf 权重还考虑词项的区分能力：设训练集共 $N$ 篇文档，词项 $i$ 出现在 $\mathrm{df}_i$ 篇中，逆文档频率 $\mathrm{idf}_i = \log(N / \mathrm{df}_i)$，$w_{ij} = \mathrm{tf}_{ij} \cdot \mathrm{idf}_i$：在所有文档中都出现的词（"的""是"）权重接近零。预处理包括分词、去停用词、词干化（英文）和特征选择。文本向量维数高（数万到数十万）而稀疏，样本往往线性可分或接近线性可分，线性支持向量机在这类问题上效果很好（Joachims，1998），至今仍是文本分类的强基线。今天更常见的做法是用预训练语言模型（[4.7.7](/4.7.7)）把文档编码为稠密向量，再在其上训练线性分类器，或直接让大语言模型分类。

## 小结

| | 硬间隔 | 软间隔 | 核方法 |
|---|---|---|---|
| 适用 | 线性可分 | 近似线性可分 | 非线性 |
| 原始问题 | $\min \frac12\|\boldsymbol{w}\|^2$，$y_i f(\boldsymbol{x}_i) \ge 1$ | $\min \frac12\|\boldsymbol{w}\|^2 + C\sum\xi_i$，$y_i f(\boldsymbol{x}_i) \ge 1 - \xi_i$ | 在特征空间中的软间隔 |
| 对偶约束 | $\sum\alpha_i y_i = 0$，$\alpha_i \ge 0$ | $\sum\alpha_i y_i = 0$，$0 \le \alpha_i \le C$ | 同软间隔 |
| 对偶目标中的样本 | $\boldsymbol{x}_i \cdot \boldsymbol{x}_j$ | $\boldsymbol{x}_i \cdot \boldsymbol{x}_j$ | $K(\boldsymbol{x}_i, \boldsymbol{x}_j)$ |

- 支持向量机选择几何间隔最大的分离超平面；最大间隔超平面存在且唯一（定理 5.2.1），只由支持向量决定。
- Lagrange 对偶总给出原始最优值的下界（弱对偶）；凸问题满足 Slater 条件时强对偶成立，最优解由 KKT 条件刻画。互补松弛说明 $\alpha_i > 0$ 的样本都在间隔边界上（硬间隔）或违反间隔（软间隔，$\alpha_i = C$）。
- 软间隔支持向量机等价于合页损失加 $L_2$ 正则的结构风险最小化；$C$ 越大，越接近硬间隔。
- 对偶问题只依赖于内积，核技巧用正定核代替内积，隐式地在高维特征空间中做线性分类；Gauss 核的宽度与 $C$ 控制模型的复杂度，用交叉验证选择。
- SMO 每次解析地优化两个乘子，是核支持向量机的标准训练算法。
