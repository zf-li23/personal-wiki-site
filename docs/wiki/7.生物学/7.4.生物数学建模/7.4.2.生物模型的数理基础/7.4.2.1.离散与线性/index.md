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

**选做题**：TODO

**a)** 对于投影矩阵$A$，主特征值$\lambda_1$满足$| \lambda_1 | > | \lambda_i | (i \neq 1)$，对应的右特征向量$w$给出稳定阶段分布。

```python
import numpy as np

# 定义虎鲸矩阵
A = np.array([
    [0, 0.0043, 0.1132, 0],
    [0.9775, 0.9111, 0, 0],
    [0, 0.0736, 0.9534, 0],
    [0, 0, 0.0452, 0.9804]
])

# 计算特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)

# 找到主特征值（模最大的特征值）
dominant_idx = np.argmax(np.abs(eigenvalues))
lambda1 = eigenvalues[dominant_idx].real
w = eigenvectors[:, dominant_idx].real

# 归一化稳定阶段分布
w = w / np.sum(w)

print("Dominant eigenvalue λ = {:.6f}".format(lambda1))
print("Stable stage distribution w:")
stage_names = ['Calf', 'Juvenile', 'Mature', 'Post-reproductive']
for i, (name, val) in enumerate(zip(stage_names, w)):
    print(f"  {name}: {val:.6f} ({val*100:.2f}%)")
```

运行结果：

```
Dominant eigenvalue λ = 1.025441
Stable stage distribution w:
  Calf: 0.036972 (3.70%)
  Juvenile: 0.316071 (31.61%)
  Mature: 0.322910 (32.29%)
  Post-reproductive: 0.324047 (32.40%)
```

即主特征值 $\lambda_1 \approx 1.0254$，对应稳定阶段分布为：
$$
\boldsymbol{w} = \begin{pmatrix} 0.036972 & 0.316071 & 0.322910 & 0.324047 \end{pmatrix}^\top
$$

**b)** 预测未来50年的种群动态：
```python-plot
import numpy as np
import matplotlib.pyplot as plt

# 定义虎鲸矩阵
A = np.array([
    [0, 0.0043, 0.1132, 0],
    [0.9775, 0.9111, 0, 0],
    [0, 0.0736, 0.9534, 0],
    [0, 0, 0.0452, 0.9804]
])

# 初始向量
x0 = np.array([10, 60, 110, 70])

# 模拟50年
years = 50
population = np.zeros((4, years+1))
population[:, 0] = x0

for t in range(years):
    population[:, t+1] = A @ population[:, t]

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(population[0, :], 'c-', label='Calf', linewidth=2)
plt.plot(population[1, :], 'g-', label='Juvenile', linewidth=2)
plt.plot(population[2, :], 'b-', label='Mature', linewidth=2)
plt.plot(population[3, :], 'r-', label='Post-reproductive', linewidth=2)
plt.plot(np.sum(population, axis=0), 'k-', label='Total', linewidth=2)
plt.xlabel('Time (years)')
plt.ylabel('Population size')
plt.title('Killer whale population dynamics (50 years)')
plt.legend()
plt.grid(True)
plt.show()
```

**c)** 绘制总种群规模、年种群增长率和每个阶段个体的比例。增加一个对数比例图，展示各阶段个体数的对数尺度变化，以更清晰观察增长趋势：
```python-plot
import numpy as np
import matplotlib.pyplot as plt

# 定义虎鲸矩阵
A = np.array([
    [0, 0.0043, 0.1132, 0],
    [0.9775, 0.9111, 0, 0],
    [0, 0.0736, 0.9534, 0],
    [0, 0, 0.0452, 0.9804]
])

x0 = np.array([10, 60, 110, 70])
years = 50
population = np.zeros((4, years+1))
population[:, 0] = x0

for t in range(years):
    population[:, t+1] = A @ population[:, t]

N = np.sum(population, axis=0)
growth_rate = N[1:] / N[:-1]
proportions = population / N

# 计算主特征值
eigenvalues, _ = np.linalg.eig(A)
lambda1 = np.max(np.real(eigenvalues))

# 创建四个子图
plt.figure(figsize=(16, 10))

# 子图1：总种群规模
plt.subplot(2, 2, 1)
plt.plot(N, 'k-', linewidth=2)
plt.xlabel('Time (years)')
plt.ylabel('Total population N(t)')
plt.title('Total population size over time')
plt.grid(True)

# 子图2：年增长率
plt.subplot(2, 2, 2)
plt.plot(range(1, years+1), growth_rate, 'b-', linewidth=2)
plt.axhline(y=lambda1, color='r', linestyle='--', label=f'λ={lambda1:.4f}')
plt.xlabel('Time (years)')
plt.ylabel('Annual growth rate λ(t)')
plt.title('Annual growth rate over time')
plt.legend()
plt.grid(True)

# 子图3：各阶段比例
plt.subplot(2, 2, 3)
plt.plot(proportions[0, :], 'c-', label='Calf', linewidth=2)
plt.plot(proportions[1, :], 'g-', label='Juvenile', linewidth=2)
plt.plot(proportions[2, :], 'b-', label='Mature', linewidth=2)
plt.plot(proportions[3, :], 'r-', label='Post-reproductive', linewidth=2)
plt.xlabel('Time (years)')
plt.ylabel('Proportion')
plt.title('Stage proportions over time')
plt.legend()
plt.grid(True)

stage_names = ['Calf', 'Juvenile', 'Mature', 'Post-reproductive']

# 子图4：对数种群规模
plt.subplot(2, 2, 4)
for i in range(4):
    plt.semilogy(population[i, :], label=stage_names[i], linewidth=2)
plt.semilogy(N, 'k-', label='Total', linewidth=2)
plt.xlabel('Time (years)')
plt.ylabel('Log population size')
plt.title('Log population size over time')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
```

**d)** 绘制种群规模随时间变化的累积分布图：
```python-plot
import numpy as np
import matplotlib.pyplot as plt

# 定义虎鲸矩阵
A = np.array([
    [0, 0.0043, 0.1132, 0],
    [0.9775, 0.9111, 0, 0],
    [0, 0.0736, 0.9534, 0],
    [0, 0, 0.0452, 0.9804]
])

stage_names = ['Calf', 'Juvenile', 'Mature', 'Post-reproductive']

# 四个初始向量
initial_vectors = [
    np.array([250, 0, 0, 0]),    # All calves
    np.array([0, 250, 0, 0]),    # All juveniles
    np.array([0, 0, 250, 0]),    # All mature
    np.array([0, 0, 0, 250])     # All post-reproductive
]
labels = ['All calves', 'All juveniles', 'All mature', 'All post-reproductive']
years = 50

# 模拟并绘图
plt.figure(figsize=(10, 8))

for i, (x0, label) in enumerate(zip(initial_vectors, labels)):
    # 模拟
    population = np.zeros((4, years+1))
    population[:, 0] = x0
    for t in range(years):
        population[:, t+1] = A @ population[:, t]
    
    N = np.sum(population, axis=0)
    proportions = population / N
    
    # 绘制各阶段比例
    plt.subplot(2, 2, i+1)
    colors = ['c', 'g', 'b', 'r']
    for stage in range(4):
        plt.plot(proportions[stage, :], color=colors[stage], 
                 label=stage_names[stage], linewidth=2)
    plt.xlabel('Time (years)')
    plt.ylabel('Proportion')
    plt.title(f'{label} - Stage proportions')
    if i == 0:
        plt.legend(loc='upper right')
    plt.grid(True)

plt.tight_layout()
plt.show()
```

还可以使用左特征向量的方法：

对于投影矩阵$A$，左特征向量$v$满足：
$$
v^T A = \lambda v^T
$$
等价于：
$$
A^T v = \lambda v
$$
因此，左特征向量是$A^T$对应于特征值 $\lambda$ 的右特征向量。

```python
import numpy as np
import matplotlib.pyplot as plt

# 定义虎鲸矩阵
A = np.array([
    [0, 0.0043, 0.1132, 0],
    [0.9775, 0.9111, 0, 0],
    [0, 0.0736, 0.9534, 0],
    [0, 0, 0.0452, 0.9804]
])

# 计算右特征向量和主特征值
eigenvalues, eigenvectors = np.linalg.eig(A)
dominant_idx = np.argmax(np.real(eigenvalues))
lambda1 = np.real(eigenvalues[dominant_idx])
w = np.real(eigenvectors[:, dominant_idx])

# 归一化右特征向量（稳定阶段分布）
w = w / np.sum(w)
stage_names = ['Calf', 'Juvenile', 'Mature', 'Post-reproductive']
# 计算左特征向量（繁殖价值）
# 注意：左特征向量满足 A^T v = λ v，因此计算A^T的特征向量
A_T = A.T
eigenvalues_T, eigenvectors_T = np.linalg.eig(A_T)

# 找到对应于主特征值λ的左特征向量
# 由于数值误差，特征值可能不完全相等，我们找最接近的那个
idx_T = np.argmin(np.abs(eigenvalues_T - lambda1))
v = eigenvectors_T[:, idx_T]

# 取实部并确保所有分量非负
v = np.real(v)

# 处理可能的符号问题：确保主要分量是正的
# 如果大多数分量为负，则乘以-1
if np.sum(v < 0) > len(v) / 2:
    v = -v

# 归一化左特征向量：使最小正分量为1
# 首先找出所有非零分量
non_zero_mask = np.abs(v) > 1e-10
if np.any(non_zero_mask):
    # 找到非零分量的最小值
    min_nonzero = np.min(np.abs(v[non_zero_mask]))
    v = v / min_nonzero
else:
    # 所有分量都接近0，使用另一种归一化
    v = v / np.linalg.norm(v)

print("\nReproductive value vector v (normalized):")
for i, (name, val) in enumerate(zip(stage_names, v)):
    print(f"  {name}: {val:.6f}")

# 验证左特征向量条件：v^T A ≈ λ v^T
left_side = v.T @ A
right_side = lambda1 * v.T
error = np.linalg.norm(left_side - right_side)
print(f"\nVerification error: ||v^T A - λ v^T|| = {error:.6e}")
print("(Should be close to zero)")

# 验证左右特征向量的点积不为零
vTw = np.dot(v, w)
print(f"\nv^T w = {vTw:.6f}")
print("(Should not be zero)")

# 四个初始向量
initial_vectors = [
    np.array([250, 0, 0, 0]),    # All calves
    np.array([0, 250, 0, 0]),    # All juveniles
    np.array([0, 0, 250, 0]),    # All mature
    np.array([0, 0, 0, 250])     # All post-reproductive
]
labels = ['All calves', 'All juveniles', 'All mature', 'All post-reproductive']
years = 50

# 计算每个初始向量的主导模式系数c1
print("\n" + "="*60)
print("Coefficient c1 for each initial condition:")
print("c1 = (v^T * x0) / (v^T * w)")

for i, (x0, label) in enumerate(zip(initial_vectors, labels)):
    c1 = np.dot(v, x0) / np.dot(v, w)
    print(f"\n{label}:")
    print(f"  c1 = {c1:.2f}")
    print(f"  Long-term population after {years} years ≈ {c1 * lambda1**years:.2f}")

# 繁殖价值分析
print("\n" + "="*60)
print("Reproductive value analysis:")
print("(Higher reproductive value means greater contribution to long-term growth)")

# 计算每个阶段对主导模式系数c1的贡献
print("\nContribution of each stage to c1 for different initial conditions:")
print("Stage".ljust(20) + "Reproductive value".ljust(20) + "Contribution to c1".ljust(20))
print("-" * 60)

# 计算归一化因子
norm_factor = np.dot(v, w)

for i, name in enumerate(stage_names):
    # 繁殖价值
    reproductive_value = v[i]
    
    # 计算该阶段对c1的贡献权重
    # 对于单位数量的该阶段个体，对c1的贡献为 v[i] / norm_factor
    contribution_per_individual = v[i] / norm_factor
    
    print(f"{name.ljust(20)} {reproductive_value:.4f}".ljust(40) + 
          f"{contribution_per_individual:.6f}")
```

运行结果：

```
Reproductive value vector v (normalized):
  Calf: 1.000000
  Juvenile: 1.049045
  Mature: 1.571320
  Post-reproductive: -0.000000

Verification error: ||v^T A - λ v^T|| = 9.155134e-16
(Should be close to zero)

v^T w = 0.875939
(Should not be zero)

============================================================
Coefficient c1 for each initial condition:
c1 = (v^T * x0) / (v^T * w)

All calves:
  c1 = 285.41
  Long-term population after 50 years ≈ 1002.32

All juveniles:
  c1 = 299.41
  Long-term population after 50 years ≈ 1051.48

All mature:
  c1 = 448.47
  Long-term population after 50 years ≈ 1574.97

All post-reproductive:
  c1 = 0.00
  Long-term population after 50 years ≈ 0.00

============================================================
Reproductive value analysis:
(Higher reproductive value means greater contribution to long-term growth)

Contribution of each stage to c1 for different initial conditions:
Stage               Reproductive value  Contribution to c1
------------------------------------------------------------
Calf                 1.0000             1.141632
Juvenile             1.0490             1.197623
Mature               1.5713             1.793869
Post-reproductive    -0.0000            -0.000000
```

左特征向量计算的补充说明：

对于主特征值 $\lambda$ 和对应的右特征向量$w$（满足$Aw = \lambda w$），左特征向量$v$满足$v^T A = \lambda v^T$。

由于$v^T A = \lambda v^T$等价于$A^T v = \lambda v$，我们可以通过求解$A^T$的特征值问题来获得$v$。

在数值计算中，需要注意以下数值稳定性问题：

1. **特征值匹配**：由于数值误差，$A$和$A^T$计算出的特征值可能不完全相等。我们需要找到最接近的特征值。

2. **特征向量符号**：特征向量的符号是任意的。我们通常选择使主要分量为正的方向。

3. **归一化**：左特征向量可以任意缩放。我们通常将其归一化，使得最小正分量为1，或者使其范数为1。

计算完成后，应验证：
$$
\| v^T A - \lambda v^T \| < \epsilon
$$
其中$\epsilon$是一个小的容差（如$10^{-10}$）。

同时，应验证$v^T w \neq 0$，因为$v$和$w$需要是非正交的（根据Perron-Frobenius定理，对于本原矩阵，左右特征向量都是正向量，因此点积为正）。


**结果分析**：

1. **阶段分布稳定性**：除了初始全部为繁殖后个体的情形外，其他初始种群的阶段分布最终都趋于稳定分布。初始全部为繁殖后个体的种群最终会灭绝，因为该阶段没有繁殖能力。
2. **最重要阶段**：基于繁殖价值分析，成熟阶段对种群未来增长最重要，因为其繁殖价值最高（1.1521）。
3. **系数$c_1$的意义**：$c_1$反映了初始种群在主导模式上的"强度"。成熟阶段初始种群的$c_1$最大（288.02），验证了其重要性。

**e)** 最大可持续收获量分析的两种方法：

**方法1：特征值灵敏度公式**

**数学原理**：
特征值$ \lambda $对矩阵元素$a_{ij}$的灵敏度为：
$$
\frac{\partial \lambda}{\partial a_{ij}} = \frac{v_i w_j}{v^T w}
$$
其中$v$和$w$分别是左、右特征向量。

对于对角线元素$a_{ii}$，收获相当于减少该元素。设收获率为$h_i$（占该阶段个体数的比例），则修改后的特征值为：
$$
\lambda' \approx \lambda - h_i \cdot \frac{\partial \lambda}{\partial a_{ii}}
$$
要求$\lambda' \geq 1$（种群不衰退），解得：
$$
h_i \leq (\lambda - 1) / \left( \frac{\partial \lambda}{\partial a_{ii}} \right)
$$
最大可持续收获个体数：$H_i = h_i \cdot x_i$，其中$x_i$为该阶段在稳定分布下的个体数。

**推导**：
由特征值定义：$A w = \lambda w$，对$a_{ij}$求偏导：
$$
\frac{\partial}{\partial a_{ij}} (A w) = \frac{\partial}{\partial a_{ij}} (\lambda w)
$$
展开：
$$
\frac{\partial A}{\partial a_{ij}} w + A \frac{\partial w}{\partial a_{ij}} = \frac{\partial \lambda}{\partial a_{ij}} w + \lambda \frac{\partial w}{\partial a_{ij}}
$$
两边左乘$v^T$，利用$v^T A = \lambda v^T$：
$$
v^T \frac{\partial A}{\partial a_{ij}} w = \frac{\partial \lambda}{\partial a_{ij}} v^T w
$$
由于$\frac{\partial A}{\partial a_{ij}}$仅在$(i,j)$位置为1，其余为0，故：
$$
v_i w_j = \frac{\partial \lambda}{\partial a_{ij}} v^T w
$$
即得灵敏度公式。

**方法2：二分搜索法**

直接模拟收获过程，通过二分搜索找到最大可持续收获量。

```python
import numpy as np

# 定义虎鲸矩阵
A = np.array([
    [0, 0.0043, 0.1132, 0],
    [0.9775, 0.9111, 0, 0],
    [0, 0.0736, 0.9534, 0],
    [0, 0, 0.0452, 0.9804]
])

# 计算稳定分布
eigenvalues, eigenvectors = np.linalg.eig(A)
dominant_idx = np.argmax(np.abs(eigenvalues))
lambda1 = eigenvalues[dominant_idx].real
w = eigenvectors[:, dominant_idx].real
w = w / np.sum(w)

# 总个体数
N_total = 250
x_stable = w * N_total

print("Population at stable distribution (total=250):")
stage_names = ['Calf', 'Juvenile', 'Mature', 'Post-reproductive']
for i, (name, val) in enumerate(zip(stage_names, x_stable)):
    print(f"  {name}: {val:.2f}")

print("\n" + "="*60)
print("Method 1: Using eigenvalue sensitivity formula")

# 计算左特征向量
A_T = A.T
eigenvalues_T, eigenvectors_T = np.linalg.eig(A_T)
idx_T = np.argmin(np.abs(eigenvalues_T - lambda1))
v = eigenvectors_T[:, idx_T].real

# 计算灵敏度
vTw = np.dot(v, w)
sensitivity = np.zeros(4)
for i in range(4):
    sensitivity[i] = (v[i] * w[i]) / vTw

print("\nSensitivity of λ to diagonal elements:")
for i, (name, sens) in enumerate(zip(stage_names, sensitivity)):
    print(f"  ∂λ/∂a_{{{i+1}{i+1}}} = {sens:.6f}")

# 计算最大可持续收获率
max_harvest_rate = np.zeros(4)
for i in range(4):
    if sensitivity[i] > 0:
        max_harvest_rate[i] = min(1.0, (lambda1 - 1) / sensitivity[i])
    else:
        max_harvest_rate[i] = float('inf')

print("\nMaximum sustainable harvest rate (fraction of stage population):")
for i, (name, rate) in enumerate(zip(stage_names, max_harvest_rate)):
    if rate == float('inf'):
        print(f"  {name}: infinite (harvest does not affect λ)")
    else:
        print(f"  {name}: {rate:.4f}")

# 计算最大可持续收获个体数
max_harvest_individuals = np.zeros(4)
for i in range(4):
    if max_harvest_rate[i] == float('inf'):
        max_harvest_individuals[i] = float('inf')
    else:
        max_harvest_individuals[i] = max_harvest_rate[i] * x_stable[i]

print("\nMaximum sustainable harvest (individuals per year):")
for i, (name, harvest) in enumerate(zip(stage_names, max_harvest_individuals)):
    if harvest == float('inf'):
        print(f"  {name}: infinite")
    else:
        print(f"  {name}: {harvest:.2f}")

print("\n" + "="*60)
print("Method 2: Binary search method")

# 模拟函数，给定收获向量h，模拟T年，返回是否可持续（最终总个体数不下降）
def is_sustainable(h, T=100):
    x = x_stable.copy()
    for t in range(T):
        x = A @ x - h
        x = np.maximum(x, 0)  # 确保非负
        if np.sum(x) < 1:  # 种群灭绝
            return False
    # 检查最终种群是否稳定或增长
    final_pop = np.sum(x)
    initial_pop = np.sum(x_stable)
    return final_pop >= initial_pop

# 对于每个阶段，二分搜索最大收获量
max_harvest_binary = np.zeros(4)
for i in range(4):
    if x_stable[i] == 0:
        max_harvest_binary[i] = 0
        continue
    
    # 二分搜索
    low = 0
    high = x_stable[i]  # 最多不能超过该阶段个体数
    for _ in range(50):  # 二分50次
        mid = (low + high) / 2
        h = np.zeros(4)
        h[i] = mid
        if is_sustainable(h):
            low = mid
        else:
            high = mid
    max_harvest_binary[i] = low

print("\nMaximum sustainable harvest (binary search, individuals per year):")
for i, (name, harvest) in enumerate(zip(stage_names, max_harvest_binary)):
    print(f"  {name}: {harvest:.2f}")

# 比较两种方法
print("\n" + "="*60)
print("Comparison of two methods:")
print("Stage          Method 1     Method 2     Difference")
print("-" * 50)
for i, name in enumerate(stage_names):
    if max_harvest_individuals[i] == float('inf'):
        m1_str = "inf"
    else:
        m1_str = f"{max_harvest_individuals[i]:.2f}"
    m2_str = f"{max_harvest_binary[i]:.2f}"
    if max_harvest_individuals[i] == float('inf'):
        diff_str = "N/A"
    else:
        diff = abs(max_harvest_individuals[i] - max_harvest_binary[i])
        diff_str = f"{diff:.2f}"
    print(f"{name:15} {m1_str:12} {m2_str:12} {diff_str:12}")
```

运行结果：

```
Population at stable distribution (total=250):
  Calf: 9.24
  Juvenile: 79.02
  Mature: 80.73
  Post-reproductive: 81.01

============================================================
Method 1: Using eigenvalue sensitivity formula

Sensitivity of λ to diagonal elements:
  ∂λ/∂a_{11} = 0.042208
  ∂λ/∂a_{22} = 0.378534
  ∂λ/∂a_{33} = 0.579258
  ∂λ/∂a_{44} = -0.000000

Maximum sustainable harvest rate (fraction of stage population):
  Calf: 0.6028
  Juvenile: 0.0672
  Mature: 0.0439
  Post-reproductive: infinite (harvest does not affect λ)

Maximum sustainable harvest (individuals per year):
  Calf: 5.57
  Juvenile: 5.31
  Mature: 3.55
  Post-reproductive: infinite

============================================================
Method 2: Binary search method

Maximum sustainable harvest (binary search, individuals per year):
  Calf: 5.80
  Juvenile: 5.52
  Mature: 3.65
  Post-reproductive: 81.01

============================================================
Comparison of two methods:
Stage          Method 1     Method 2     Difference
--------------------------------------------------
Calf            5.57         5.80         0.23
Juvenile        5.31         5.52         0.21
Mature          3.55         3.65         0.10
Post-reproductive inf          81.01        N/A
```

可见特征值灵敏度法和二分搜索法结果非常接近，均为幼年阶段5.6只左右，成熟阶段3.6只左右，验证了灵敏度公式的有效性。对于最后一个阶段，由于其对λ的灵敏度为零（理论上不影响λ），所以该方法认为该阶段的最大可持续收获为无限。二分搜索法在这种情况下给出了一个近似值作为上限。