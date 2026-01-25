**内容**：矩阵与向量（用于种群结构、代谢流）；线性方程组；特征值的生物学意义（如种群增长率、结构稳定性）。

## 2.1.1.种群状态向量与投影矩阵：从斐波那契数列到年龄结构

### 2.1.1.1.以斐波那契数列为例

让我们从一个看似与生态学无关的数学序列——**斐波那契数列**开始思考。这个序列定义如下：

$$
F_0 = 0, \quad F_1 = 1, \quad F_{n+2} = F_{n+1} + F_n \quad (n \geq 0)
$$

它描述了兔子繁殖的理想化模型：每对成熟兔子每月生下一对新兔子，新生兔子需要一个月成熟。虽然这个模型过于简化，但它揭示了一个假定性的思想：**当前状态可以由前几个状态线性组合得到**。

将斐波那契数列改写为矩阵形式：

$$
\begin{pmatrix}
F_{n+2} \\
F_{n+1}
\end{pmatrix}
=
\begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}
\begin{pmatrix}
F_{n+1} \\
F_n
\end{pmatrix}
$$

令 $\boldsymbol{x}_n = (F_{n+1}, F_n)^\top$，则：

$$
\boldsymbol{x}_{n+1} = \boldsymbol{A} \boldsymbol{x}_n, \quad \boldsymbol{A} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}
$$

这就是一个**离散线性动力系统**。斐波那契数列的增长，本质上是矩阵 $\boldsymbol{A}$ 反复作用于初始向量的结果。

### 2.1.1.2.Leslie矩阵：年龄结构化种群的投影

在现实种群中，个体的繁殖和存活能力通常依赖于年龄。P.H. Leslie在1945年提出了一种优雅的矩阵模型来描述这种年龄结构化的种群动态。

考虑一个分为 $m$ 个年龄组的种群，每个年龄组的时间跨度相同（如一年）。令 $n_i(t)$ 表示时刻 $t$ 第 $i$ 个年龄组的个体数。种群状态可用向量表示：

$$
\boldsymbol{n}(t) = \begin{pmatrix}
n_1(t) \\
n_2(t) \\
\vdots \\
n_m(t)
\end{pmatrix}
$$

从时刻 $t$ 到 $t+1$，种群变化遵循两个基本过程：
1. **保持**：第 $i$ 组个体以概率 $k_i$ 存活并保持本组年龄。
2. **存活**：第 $i$ 组个体以概率 $s_i$ 存活并进入第 $i+1$ 组（$i = 1, \cdots, m-1$）。
3. **繁殖**：第 $i$ 组个体平均产生 $f_i$ 个新个体（这些新生个体进入第1组）。

这些过程可用 **Leslie矩阵** $\boldsymbol{L}$ 表示为：

$$
\boldsymbol{n}(t+1) = \boldsymbol{L} \boldsymbol{n}(t)
$$

其中 $\boldsymbol{L}$ 的形式为：

$$
\boldsymbol{L} = 
\begin{pmatrix}
f_1 & f_2 & \cdots & f_{m-1} & f_m \\
s_1 & k_2 & \cdots & 0 & 0 \\
0 & s_2 & \cdots & 0 & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \cdots & s_{m-1} & k_m
\end{pmatrix}
$$

这里 $f_i \geq 0$ 为**生育率**，$s_i \in [0, 1]$ 为**存活率**，$k_i \in [0, 1]$ 为**保持率**。注意矩阵的第一行包含所有年龄组的生育贡献，而次对角线包含存活率，对角线包含保持率。

### 2.1.1.3.一般化的年龄结构矩阵

实际种群有可能不如Leslie矩阵这么理想，在单个时间跨度内，个体的存活有可能跨越阶段，一些新繁殖的个体也可能会迅速长大，所以有推广到一个一般的矩阵的必要。另外，由于雌性个体的数量有时才是决定种群繁殖能力的主导因素，有时建模时还只考虑雌性个体，这里我们忽略这一细节。我们考虑一个一般化的矩阵：

$$
\boldsymbol{n}(t+1) = \boldsymbol{A} \boldsymbol{n}(t)
$$

其中 $\boldsymbol{A}$ 的形式为：

$$
\boldsymbol{A} = 
\begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1m} \\
a_{21} & a_{22} & \cdots & a_{2m}\\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mm}
\end{pmatrix}
$$

## 2.1.2.特征值与特征向量：长期行为分析

### 2.1.2.1.矩阵的特征值与特征向量

矩阵模型是线性系统：$\boldsymbol{n}(t) = \boldsymbol{A}^t \boldsymbol{n}(0)$。要理解长期行为，我们需要分析 $\boldsymbol{A}^t$。这由矩阵的**特征值和特征向量**决定。

对于矩阵 $\boldsymbol{A}$，若存在标量 $\lambda$ 和非零向量 $\boldsymbol{w}$ 使得：

$$
\boldsymbol{A} \boldsymbol{w} = \lambda \boldsymbol{w}
$$

则称 $\lambda$ 为 $\boldsymbol{L}$ 的特征值，$\boldsymbol{w}$ 为对应的右特征向量。特征值满足特征方程：

$$
\det(\boldsymbol{A} - \lambda \boldsymbol{I}) = 0
$$

若矩阵 $\boldsymbol{A}$ 有 $m$ 个线性无关的特征向量 $\boldsymbol{w}_1, \ldots, \boldsymbol{w}_m$，对应特征值 $\lambda_1, \ldots, \lambda_m$，则初始向量可表示为：

$$
\boldsymbol{n}(0) = c_1 \boldsymbol{w}_1 + c_2 \boldsymbol{w}_2 + \cdots + c_m \boldsymbol{w}_m
$$

进而得到：

$$
\boldsymbol{n}(t) = c_1 \lambda_1^t \boldsymbol{w}_1 + c_2 \lambda_2^t \boldsymbol{w}_2 + \cdots + c_m \lambda_m^t \boldsymbol{w}_m
$$

将特征值按模长排序：

$$
|\lambda_1| \geq |\lambda_2| \geq \cdots \geq |\lambda_m|
$$

则存在主特征值 $\lambda_1$ 满足当 $t \rightarrow \infin$ 时：

$$
\boldsymbol{n}(t) \approx c_1 \lambda_1^t \boldsymbol{w}_1
$$

即种群结构趋近于 $w_1$ 的方向，其增长或衰减速率由 $\lambda_1$ 决定。

根据 Perron–Frobenius 定理，若矩阵 $\boldsymbol{A}$ 为非负幂正方阵则：

- 其存在唯一的主特征值 $\lambda_1 > 0$；
- 其对应的特征向量 $\boldsymbol{w}_1$ 的所有分量均为正；

一个非负 $k \times k$ 矩阵 $A$ 是幂正的**充分必要条件**是：

$$
A^{k^2 - 2k + 2} > 0
$$

即 $A^{k^2 - 2k + 2}$ 为正矩阵。

### 2.1.2.2.Leslie矩阵特征值与特征向量的生物学意义

对于Leslie矩阵 $\boldsymbol{L}$，在合理的生物学假设下（即至少有一个年龄组具有生育能力 $f_i > 0$，且所有年龄组间的存活率 $s_i > 0$），存在大量 $\boldsymbol{L}$ 是非负且幂正的矩阵（但存在一定的特例），对于这些种群，其具备以下性质：
1. 存在唯一的**主正实特征值** $\lambda_1$，且 $|\lambda_1| > |\lambda_i|$（$i \neq 1$）。
2. $\lambda_1$ 决定了**长期增长率**：
   - $\lambda_1 > 1$：种群增长
   - $\lambda_1 = 1$：种群稳定
   - $\lambda_1 < 1$：种群衰退
3. 对应的**右特征向量** $\boldsymbol{w}_1$ 给出了**稳定年龄结构**：无论初始结构如何，长期而言各年龄组的比例将收敛于 $\boldsymbol{w}_1$ 的比例。
4. **左特征向量** $\boldsymbol{v}_1$（满足 $\boldsymbol{v}_1^\top \boldsymbol{L} = \lambda_1 \boldsymbol{v}_1^\top$）的各个分量则表示相应年龄组个体的**繁殖价值**，即该组个体对未来种群增长的贡献。

### 2.1.2.3.以斐波那契数列为例

回顾斐波那契数列的矩阵形式：
$$
\boldsymbol{A} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}, \quad \boldsymbol{x}_{n+1} = \boldsymbol{A} \boldsymbol{x}_n
$$

**步骤1：计算特征值与特征向量**

特征方程：
$$
\det(\boldsymbol{A} - \lambda \boldsymbol{I}) = \det\begin{pmatrix} 1-\lambda & 1 \\ 1 & -\lambda \end{pmatrix} = \lambda^2 - \lambda - 1 = 0
$$
解得：
$$
\lambda_1 = \frac{1+\sqrt{5}}{2} \approx 1.618, \quad \lambda_2 = \frac{1-\sqrt{5}}{2} \approx -0.618
$$
对应特征向量（取单位化形式）：
$$
\boldsymbol{w}_1 = \begin{pmatrix} \lambda_1 \\ 1 \end{pmatrix}, \quad \boldsymbol{w}_2 = \begin{pmatrix} \lambda_2 \\ 1 \end{pmatrix}
$$

**步骤2：验证非负性与幂正性**

- $\boldsymbol{A}$ 为非负矩阵。
- 计算 $\boldsymbol{A}^2 = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} > 0$，故 $\boldsymbol{A}$ 是幂正矩阵。

**步骤3：长期行为分析**

初始向量 $\boldsymbol{x}_0 = (F_1, F_0)^\top = (1, 0)^\top$，可表示为：
$$
\boldsymbol{x}_0 = c_1 \boldsymbol{w}_1 + c_2 \boldsymbol{w}_2
$$
解得 $c_1 = \frac{1}{\sqrt{5}} \lambda_1$，$c_2 = -\frac{1}{\sqrt{5}} \lambda_2$。

于是：
$$
\boldsymbol{x}_n = c_1 \lambda_1^n \boldsymbol{w}_1 + c_2 \lambda_2^n \boldsymbol{w}_2
$$
由于 $|\lambda_1| > 1 > |\lambda_2|$，当 $n \to \infty$ 时，$|\lambda_2|^n \to 0$，故：
$$
\boldsymbol{x}_n \approx c_1 \lambda_1^n \boldsymbol{w}_1
$$
即斐波那契数列的增长主要由 $\lambda_1$ 主导，长期增长率约为 $1.618$（黄金比例）。同时，相邻项比值趋近：
$$
\frac{F_{n+1}}{F_n} \approx \lambda_1 = \frac{1+\sqrt{5}}{2}
$$
这正是斐波那契数列著名的渐近性质。

斐波那契数列作为一个简化的年龄结构模型（仅两个“年龄组”：成熟与未成熟），其矩阵 $\boldsymbol{A}$ 满足Perron–Frobenius定理的条件。主特征值 $\lambda_1$ 决定了数列的长期指数增长率，而对应的特征向量 $\boldsymbol{w}_1$ 给出了“稳定状态”下两项的比例关系。这一例子生动展示了特征值与特征向量在刻画线性离散动力系统长期行为中的核心作用。

## 2.1.3.左特征向量与繁殖价值

对于投影矩阵 $\boldsymbol{L}$，除了右特征向量外，左特征向量也具有重要的生物学意义。左特征向量 $\boldsymbol{v}_1^\top$ 定义为满足下式的非零行向量：

$$
\boldsymbol{v}_1^\top \boldsymbol{L} = \lambda_1 \boldsymbol{v}_1^\top
$$

其各个分量表示相应年龄组个体的**繁殖价值**，即该组个体对未来种群增长的相对贡献。繁殖价值量化了不同年龄或阶段个体对种群长期增长的重要性，是种群生物学和进化生态学中的一个核心概念。

### 2.1.3.1.以斐波那契数列为例

回顾斐波那契模型的矩阵 $\boldsymbol{A} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$，现在计算对应于 $\lambda_1$ 的左特征向量 $\boldsymbol{v}_1^\top$。

设 $\boldsymbol{v}_1^\top = (x, y)$，由 $\boldsymbol{v}_1^\top \boldsymbol{A} = \lambda_1 \boldsymbol{v}_1^\top$ 得：

$$
(x, y) \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \lambda_1 (x, y)
$$

即：

$$
(x + y, x) = (\lambda_1 x, \lambda_1 y)
$$

得到方程组：

$$
\begin{cases}
x + y = \lambda_1 x \\
x = \lambda_1 y
\end{cases}
$$

由第二个方程 $x = \lambda_1 y$，代入第一个方程：

$$
\lambda_1 y + y = \lambda_1 (\lambda_1 y) \quad \Rightarrow \quad y(\lambda_1 + 1) = y \lambda_1^2
$$

由于 $y \neq 0$，化简得 $\lambda_1 + 1 = \lambda_1^2$，这正是特征方程，成立。取 $y = 1$，则 $x = \lambda_1$，于是：

$$
\boldsymbol{v}_1^\top = (\lambda_1, 1)
$$

为方便解释，通常将繁殖价值归一化，使得最小值为1。这里取第二个分量为1，则第一个分量为 $\lambda_1 \approx 1.618$。这意味着：
- “成熟”个体（对应第一个分量）的繁殖价值为 $1.618$，
- “未成熟”个体（对应第二个分量）的繁殖价值为 $1$。

即一个成熟个体对未来种群增长的贡献是未成熟个体的 $1.618$ 倍。直观上，成熟个体能立即繁殖，而未成熟个体需要等待一个时间步（成熟）后才能繁殖，因此成熟个体的繁殖价值更高。

### 2.1.3.2.繁殖价值的应用

左特征向量的计算方式：
1. 计算 $\boldsymbol{L}$ 的特征值和右特征向量。
2. 求解 $\boldsymbol{v}_1^\top$，使得：
  $$
  \boldsymbol{v}_1^\top \boldsymbol{L} = \lambda_1 \boldsymbol{v}_1^\top
  $$
3. 归一化 $\boldsymbol{v}_1^\top$，使得分量最小值为 $1$。

左特征向量（繁殖价值）与右特征向量（稳定年龄结构）共同揭示了种群动态的内在对偶性：

1. **预测长期增长幅度**：初始种群 $\boldsymbol{n}(0)$ 在主导模式上的系数 $c_1$ 可由左特征向量计算：
   $$
   c_1 = \frac{\boldsymbol{v}_1^\top \boldsymbol{n}(0)}{\boldsymbol{v}_1^\top \boldsymbol{w}_1}
   $$
   其中分母为归一化常数。长期种群数量为 $\boldsymbol{n}(t) \approx c_1 \lambda_1^t \boldsymbol{w}_1$。因此，繁殖价值高的年龄组对 $c_1$ 的贡献更大，即这些组别的初始数量对长期种群规模影响更大。

2. **指导种群管理**：在保护生物学中，繁殖价值指示了不同年龄组对种群长期存续的重要性。例如，若某个年龄组的繁殖价值很高，则保护该组个体对种群恢复更有效。繁殖价值依赖于矩阵 $\boldsymbol{L}$，可以通过生态学数据估计。

## 思考题
1. （选做）试讨论 $\boldsymbol{L}$ 在哪些约束下是非负且幂正的，能不能举出一个年龄比例不趋稳的反例并进行模拟？*提示：我们的 Leslie 矩阵定义考虑了保持当前年龄阶段的可能，与知乎和 AI 工具常见的回答稍有不同*
2. 虎鲸（Orcinus orca）是长寿的海洋哺乳动物，生活在被称为"群体"的稳定社会群体中。它们稳定的社会结构和个体可通过照片识别的特点使其特别适合科学研究。自1973年以来，已收集了不列颠哥伦比亚省和华盛顿州沿海水域虎鲸种群的统计数据。Brault和Caswell（1993）使用1973-1987年的数据和阶段结构矩阵模型研究了与鲸鱼有关的几个人口统计学问题。他们使用混合年龄阶段分类对雌性进行建模：幼崽、幼年（过了第一年但未成熟）、成熟和繁殖后。投影矩阵A如下所示：

$$
\boldsymbol{A} = 
\begin{bmatrix}
0 & 0.0043 & 0.1132 & 0 \\
0.9775 & 0.9111 & 0 & 0 \\
0 & 0.0736 & 0.9534 & 0 \\
0 & 0 & 0.0452 & 0.9804
\end{bmatrix}
$$

- **a)** 计算虎鲸种群的主特征值 $\lambda$ 和稳定阶段分布 $w$ ；
- **b)** 假设当前种群向量为 $x_0 = (10, 60, 110, 70)$，预测未来50年的种群动态；
- **c)** 在三张独立的图上绘制以下随时间变化的过程：
  - 第t年的总种群规模 $N(t)$，
  - 年种群增长率 $\lambda(t) = N(t+1)/N(t)$，
  - 每个阶段个体的比例。
- **d)** 使用以下初始种群向量重新运行虎鲸种群动态脚本：$x_0 = (250, 0, 0, 0), (0, 250, 0, 0), (0, 0, 250, 0), (0, 0, 0, 250)$。比较和对比四个种群预测：
  - 阶段分布及其稳定性，
  - 哪个阶段似乎对种群未来增长最重要？
- **e)** 考虑从虎鲸种群中进行可能的收获（捕鲸），收获个体来自单个阶段，例如所有幼年个体或所有繁殖个体。假设初始种群结构为稳定分布 $\boldsymbol{w}$，总个体数为250。
  - 每年最多可以收获多少幼年个体而不导致种群灭绝？
  - 最多可以收获多少繁殖成年个体？

*提示：假设收获发生在繁殖季节之后，因此模型变为 $\boldsymbol{x}(t+1) = \boldsymbol{A}\boldsymbol{x}(t) - \boldsymbol{h}$，其中 $\boldsymbol{h} = (h_1, h_2, h_3, h_4)$ 是每年从每个阶段收获的个体数向量。假设 $h$ 是常数：每年收获相同数量。*