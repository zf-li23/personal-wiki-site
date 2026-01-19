**内容**：矩阵与向量（用于种群结构、代谢流）；线性方程组；特征值的生物学意义（如种群增长率、结构稳定性）。

在生态学中，种群很少由完全相同的个体组成。个体在年龄、大小或发育阶段上的差异会显著影响其繁殖与生存能力。为了描述这种结构化种群的动态，我们需要超越简单的总数计数，转而关注**种群的结构分布**及其随时间的变化。

**Leslie矩阵模型**正是为此设计的经典工具。它用线性代数语言，优雅地刻画了种群年龄结构的年际变化。

## **2.1.1 种群状态向量与投影矩阵：从斐波那契数列到年龄结构**

让我们从一个看似与生态学无关的数学序列——**斐波那契数列**开始思考。这个序列定义如下：

$$
F_0 = 0, \quad F_1 = 1, \quad F_{n+2} = F_{n+1} + F_n \quad (n \geq 0)
$$

它描述了兔子繁殖的理想化模型：每对成熟兔子每月生下一对新兔子，新生兔子需要一个月成熟。虽然这个模型过于简化，但它揭示了一个深刻思想：**当前状态可以由前几个状态线性组合得到**。

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

令 $\mathbf{x}_n = (F_{n+1}, F_n)^\top$，则：

$$
\mathbf{x}_{n+1} = \mathbf{A} \mathbf{x}_n, \quad \mathbf{A} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}
$$

这就是一个**离散线性动力系统**。斐波那契数列的增长，本质上是矩阵 $\mathbf{A}$ 反复作用于初始向量的结果。

### **Leslie矩阵：年龄结构化种群的投影**

在现实种群中，个体的繁殖和存活能力通常依赖于年龄。P.H. Leslie在1945年提出了一种优雅的矩阵模型来描述这种年龄结构化的种群动态。

考虑一个分为 $m$ 个年龄组的种群，每个年龄组的时间跨度相同（如一年）。令 $n_i(t)$ 表示时刻 $t$ 第 $i$ 个年龄组的个体数。种群状态可用向量表示：

$$
\mathbf{n}(t) = \begin{pmatrix}
n_1(t) \\
n_2(t) \\
\vdots \\
n_m(t)
\end{pmatrix}
$$

从时刻 $t$ 到 $t+1$，种群变化遵循两个基本过程：
1. **存活**：第 $i$ 组个体以概率 $s_i$ 存活并进入第 $i+1$ 组（$i = 1, \cdots, m-1$）。
2. **繁殖**：第 $i$ 组个体平均产生 $f_i$ 个新个体（这些新生个体进入第1组）。

这些过程可用 **Leslie矩阵** $\mathbf{L}$ 表示为：

$$
\mathbf{n}(t+1) = \mathbf{L} \mathbf{n}(t)
$$

其中 $\mathbf{L}$ 的形式为：

$$
\mathbf{L} = 
\begin{pmatrix}
f_1 & f_2 & \cdots & f_{m-1} & f_m \\
s_1 & 0 & \cdots & 0 & 0 \\
0 & s_2 & \cdots & 0 & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \cdots & s_{m-1} & 0
\end{pmatrix}
$$

这里 $f_i \geq 0$ 为**生育率**，$s_i \in [0, 1]$ 为**存活率**。注意矩阵的第一行包含所有年龄组的生育贡献，而次对角线包含存活率。

**例1：三年龄组模型**
设一个物种分为幼年、青年、成年三组，参数如下：
- 生育率：幼年不繁殖（$f_1 = 0$），青年每个体产2崽（$f_2 = 2$），成年每个体产1崽（$f_3 = 1$）。
- 存活率：幼年存活到青年的概率为0.5（$s_1 = 0.5$），青年存活到成年的概率为0.8（$s_2 = 0.8$）。

则Leslie矩阵为：

$$
\mathbf{L} = 
\begin{pmatrix}
0 & 2 & 1 \\
0.5 & 0 & 0 \\
0 & 0.8 & 0
\end{pmatrix}
$$

若初始种群 $\mathbf{n}(0) = (100, 50, 30)^\top$，则一年后：

$$
\mathbf{n}(1) = \mathbf{L} \mathbf{n}(0) = 
\begin{pmatrix}
0\times100 + 2\times50 + 1\times30 \\
0.5\times100 + 0\times50 + 0\times30 \\
0\times100 + 0.8\times50 + 0\times30
\end{pmatrix}
= 
\begin{pmatrix}
130 \\
50 \\
40
\end{pmatrix}
$$

## **2.1.2 特征值与特征向量：长期行为分析**

Leslie矩阵模型是线性系统：$\mathbf{n}(t) = \mathbf{L}^t \mathbf{n}(0)$。要理解长期行为，我们需要分析 $\mathbf{L}^t$。这由矩阵的**特征值和特征向量**决定。

对于矩阵 $\mathbf{L}$，若存在标量 $\lambda$ 和非零向量 $\mathbf{w}$ 使得：

$$
\mathbf{L} \mathbf{w} = \lambda \mathbf{w}
$$

则称 $\lambda$ 为 $\mathbf{L}$ 的特征值，$\mathbf{w}$ 为对应的右特征向量。特征值满足特征方程：

$$
\det(\mathbf{L} - \lambda \mathbf{I}) = 0
$$

对于Leslie矩阵，可以证明在合理的生物学假设下（至少有一个 $f_i > 0$ 且 $s_i > 0$）：
1. 存在唯一的**主导正实特征值** $\lambda_1$，且 $|\lambda_1| > |\lambda_i|$（$i \neq 1$）。
2. $\lambda_1$ 决定了**长期增长率**：
   - $\lambda_1 > 1$：种群增长
   - $\lambda_1 = 1$：种群稳定
   - $\lambda_1 < 1$：种群衰退
3. 对应的右特征向量 $\mathbf{w}_1$ 给出了**稳定年龄结构**：无论初始结构如何，长期而言各年龄组的比例将收敛于 $\mathbf{w}_1$ 的比例。

**左特征向量** $\mathbf{v}_1$（满足 $\mathbf{v}_1^\top \mathbf{L} = \lambda_1 \mathbf{v}_1^\top$）的各个分量则表示相应年龄组个体的**繁殖价值**，即该组个体对未来种群增长的贡献。

**例2：计算特征值和稳定结构**
对于前面的三年龄组Leslie矩阵：

```python
import numpy as np

L = np.array([[0, 2, 1],
              [0.5, 0, 0],
              [0, 0.8, 0]])

# 计算特征值和特征向量
eigvals, eigvecs = np.linalg.eig(L)

# 找到主导特征值（最大模）
dominant_idx = np.argmax(np.abs(eigvals))
lambda1 = eigvals[dominant_idx]
w1 = eigvecs[:, dominant_idx]

print(f"特征值: {eigvals}")
print(f"主导特征值 λ₁ = {lambda1:.4f}")
print(f"对应的特征向量: {w1}")

# 归一化得到稳定年龄结构
stable_structure = w1 / np.sum(w1)
print(f"稳定年龄结构（比例）: {stable_structure}")
```

运行结果可能显示 $\lambda_1 \approx 1.1$，表明种群将缓慢增长，稳定结构中成年组比例最高。

## **2.1.3 Python实现与可视化**

下面我们实现一个更完整的年龄结构模型，并可视化其动态。

```python
import numpy as np
import matplotlib.pyplot as plt

class LeslieModel:
    """Leslie矩阵模型类"""
    
    def __init__(self, fecundities, survival_rates):
        """
        参数:
        fecundities: 各年龄组生育率列表
        survival_rates: 存活率列表（长度比fecundities少1）
        """
        self.m = len(fecundities)
        self.f = np.array(fecundities)
        self.s = np.array(survival_rates)
        
        # 构建Leslie矩阵
        self.L = np.zeros((self.m, self.m))
        self.L[0, :] = self.f
        for i in range(self.m - 1):
            self.L[i + 1, i] = self.s[i]
    
    def simulate(self, n0, T):
        """模拟T个时间步"""
        population = np.zeros((T, self.m))
        population[0, :] = n0
        
        for t in range(1, T):
            population[t, :] = self.L @ population[t - 1, :]
        
        return population
    
    def analyze(self):
        """分析长期行为"""
        eigvals, eigvecs = np.linalg.eig(self.L)
        dominant_idx = np.argmax(np.abs(eigvals))
        lambda1 = np.real(eigvals[dominant_idx])
        w1 = np.real(eigvecs[:, dominant_idx])
        w1 = w1 / np.sum(w1)  # 归一化
        
        return lambda1, w1

# 实例：五年龄组种群
fecundities = [0, 0, 1.5, 2.0, 0.5]  # 生育率
survival_rates = [0.3, 0.6, 0.8, 0.2]  # 存活率

model = LeslieModel(fecundities, survival_rates)

# 初始种群：大量幼年个体
n0 = np.array([200, 100, 50, 20, 10])
T = 30  # 模拟30年

# 模拟
population = model.simulate(n0, T)
total_pop = np.sum(population, axis=1)

# 分析
lambda1, stable_structure = model.analyze()

# 可视化
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. 总种群增长
axes[0, 0].plot(range(T), total_pop, 'b-', linewidth=2)
axes[0, 0].set_xlabel('时间（年）')
axes[0, 0].set_ylabel('总个体数')
axes[0, 0].set_title('总种群动态')
axes[0, 0].grid(True, alpha=0.3)

# 2. 各年龄组数量（对数坐标）
for i in range(model.m):
    axes[0, 1].semilogy(range(T), population[:, i], label=f'年龄组 {i+1}')
axes[0, 1].set_xlabel('时间（年）')
axes[0, 0].set_ylabel('个体数（对数）')
axes[0, 1].set_title('各年龄组动态（对数坐标）')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# 3. 年龄结构演变
time_points = [0, 5, 10, 20, 29]
for t in time_points:
    structure = population[t, :] / np.sum(population[t, :])
    axes[1, 0].plot(range(1, model.m + 1), structure, 'o-', label=f'第{t}年')
axes[1, 0].plot(range(1, model.m + 1), stable_structure, 'k--', linewidth=2, label='稳定结构')
axes[1, 0].set_xlabel('年龄组')
axes[1, 0].set_ylabel('比例')
axes[1, 0].set_title('年龄结构演变')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# 4. 增长率收敛
growth_rates = np.diff(np.log(total_pop))
axes[1, 1].plot(range(1, T), growth_rates, 'g-', linewidth=2)
axes[1, 1].axhline(y=np.log(lambda1), color='r', linestyle='--', label=f'ln(λ₁) = {np.log(lambda1):.3f}')
axes[1, 1].set_xlabel('时间（年）')
axes[1, 1].set_ylabel('瞬时增长率 ln[N(t+1)/N(t)]')
axes[1, 1].set_title('增长率向ln(λ₁)收敛')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"长期增长率 λ₁ = {lambda1:.4f}")
print(f"稳定年龄结构: {stable_structure}")
```

## **思考题：复杂年龄结构模型分析**

考虑一个分为6个年龄组的种群，其参数如下：

- **生育率**：$f = [0, 0, 0.5, 1.2, 1.8, 0.3]$
- **存活率**：$s = [0.2, 0.4, 0.7, 0.6, 0.1]$

**问题**：
1. **矩阵构建与特征分析**：
   - 写出该种群的Leslie矩阵 $\mathbf{L}$。
   - 计算 $\mathbf{L}$ 的所有特征值，确定主导特征值 $\lambda_1$。
   - 计算稳定年龄结构 $\mathbf{w}_1$ 和繁殖价值向量 $\mathbf{v}_1$（左特征向量）。

2. **动态模拟**：
   - 取初始种群 $\mathbf{n}(0) = (500, 200, 100, 50, 20, 10)^\top$，模拟50个时间步。
   - 计算每个时间步的总种群 $N(t)$ 和瞬时增长率 $r(t) = \ln[N(t+1)/N(t)]$。
   - 绘制 $r(t)$ 随时间变化图，验证其是否收敛到 $\ln(\lambda_1)$。

3. **弹性分析**：
   - 使用公式 $e_{p} = \dfrac{\partial \ln \lambda_1}{\partial \ln p}$ 计算 $\lambda_1$ 对每个参数（$f_i$ 和 $s_i$）的弹性。
   - 哪个参数的变化对种群长期增长影响最大？这对保护管理有何启示？

4. **密度制约效应**（进阶）：
   - 修改模型，使生育率随总种群密度下降：$f_i(N) = f_i^0 \exp(-0.001 N)$，其中 $N$ 为总个体数。
   - 模拟该非线性系统，观察种群是否趋于稳定平衡。平衡时的总种群数和年龄结构是多少？

**提示**：
- 使用`numpy.linalg.eig`计算特征值和特征向量，注意左特征向量是右特征向量矩阵的逆矩阵的行。
- 弹性可通过扰动参数并重新计算 $\lambda_1$ 来数值估算。

通过这个练习，你将深入掌握Leslie矩阵模型的构建、分析和应用，为后续学习更复杂的生态模型和生物网络模型奠定基础。