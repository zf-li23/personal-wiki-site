**内容**：变化率（导数）与累积量（积分）的生物学对应（如生长速率、总生物量）；作为线性近似的导数。

在上一节中，我们利用Leslie矩阵研究了年龄结构化种群的离散时间动态。矩阵的主导特征值 $\lambda_1$ 给出了种群的长期增长率。若 $\lambda_1 > 1$，种群增长；若 $\lambda_1 < 1$，种群衰退。然而，这种线性模型假设增长率恒定，忽略了资源有限性导致的密度制约效应。本节将引入密度制约，并由此过渡到连续时间模型，介绍导数与积分的基本概念及其在种群增长中的应用。

## 2.2.1.密度制约的种群增长：从离散到混沌

考虑一个简单的离散时间种群模型，其中种群数量 $n_t$ 随时间 $t$ 变化。假设增长率依赖于种群密度，即存在密度制约。最经典的模型是**逻辑斯谛映射**（Logistic map）：

$$
n_{t+1} = r n_t \left(1 - \frac{n_t}{K}\right)
$$

其中 $r$ 是内禀增长率，$K$ 是环境容纳量。为了简化，我们通常将种群数量标准化为 $x_t = n_t / K$，从而得到：

$$
x_{t+1} = r x_t (1 - x_t), \quad 0 \leq x_t \leq 1
$$

这个简单的二次映射能够产生极其丰富的动态行为，包括稳定平衡、周期振荡和混沌。

### 2.2.1.1.导数的直观：变化率的线性近似

在离散系统中，我们通常关心 $x_{t+1}$ 相对于 $x_t$ 的变化。定义函数 $f(x) = r x (1 - x)$，则 $x_{t+1} = f(x_t)$。在平衡点 $\overline{x}$（即满足 $\overline{x} = f(\overline{x})$）附近，我们可以用导数来近似函数的行为。导数 $f'(\overline{x})$ 表示 $f$ 在 $\overline{x}$ 处的线性近似系数，即当 $x_t$ 偏离平衡点一个小量 $\delta$ 时，下一时刻的偏离约为 $f'(\overline{x}) \delta$。

平衡点的稳定性由导数 $f'(\overline{x})$ 的绝对值决定：

- 若 $|f'(\overline{x})| < 1$，平衡点稳定，小偏离会衰减；
- 若 $|f'(\overline{x})| > 1$，平衡点不稳定，小偏离会放大。

对于逻辑斯谛映射，平衡点有两个：$\overline{x}_0 = 0$ 和 $\overline{x}_1 = 1 - 1/r$（当 $r > 1$ 时）。计算导数 $f'(x) = r(1 - 2x)$，于是：

- 在 $\overline{x}_0 = 0$ 处，$f'(0) = r$，因此当 $0 < r < 1$ 时稳定，$r > 1$ 时不稳定。
- 在 $\overline{x}_1 = 1 - 1/r$ 处，$f'(\overline{x}_1) = 2 - r$，因此当 $1 < r < 3$ 时稳定（因为 $|2 - r| < 1$）。

当 $r$ 超过 3 时，平衡点 $\overline{x}_1$ 失稳，系统出现周期 2 振荡。随着 $r$ 进一步增大，周期倍增（倍周期分岔）发生，最终进入混沌状态。

### 蛛网图（Cobweb plot）可视化

蛛网图是一种可视化离散映射迭代过程的工具。它通过绘制函数 $y = f(x)$ 和对角线 $y = x$，并追踪迭代路径，帮助我们直观理解系统的动态。

以下Python代码绘制逻辑斯谛映射的蛛网图：

```python-plot
import numpy as np
import matplotlib.pyplot as plt

def cobweb_plot(r, x0, n_iter, ax=None):
    """
    绘制逻辑斯谛映射的蛛网图。
    
    参数:
        r: 增长率
        x0: 初始值
        n_iter: 迭代次数
        ax: matplotlib轴对象，若为None则创建新图
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    
    # 绘制函数曲线
    x = np.linspace(0, 1, 1000)
    f = r * x * (1 - x)
    ax.plot(x, f, 'b-', lw=2, label=f'$f(x) = r x (1 - x)$')
    ax.plot(x, x, 'k--', lw=1, label='$y = x$')
    
    # 迭代并绘制蛛网线
    x_current = x0
    for i in range(n_iter):
        y_current = r * x_current * (1 - x_current)
        # 垂直线
        ax.plot([x_current, x_current], [x_current, y_current], 'r-', lw=0.5)
        # 水平线
        ax.plot([x_current, y_current], [y_current, y_current], 'r-', lw=0.5)
        x_current = y_current
    
    ax.set_xlabel('$x_t$', fontsize=14)
    ax.set_ylabel('$x_{t+1}$', fontsize=14)
    ax.set_title(f'逻辑斯谛映射蛛网图 (r = {r}, x0 = {x0})', fontsize=16)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return ax

# 示例：绘制不同r值的蛛网图
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
r_vals = [2.5, 3.2, 3.5, 4.0]
x0 = 0.3
n_iter = 50

for i, (r, ax) in enumerate(zip(r_vals, axes.flat)):
    cobweb_plot(r, x0, n_iter, ax)
    # 标注平衡点（如果存在）
    if r > 1:
        x_eq = 1 - 1/r
        ax.plot(x_eq, x_eq, 'go', markersize=8, label='平衡点')
        ax.legend()

plt.tight_layout()
plt.show()
```

通过改变 $r$ 的值，我们可以观察到稳定平衡（$r=2.5$）、周期2（$r=3.2$）、周期4（$r=3.5$）以及混沌（$r=4.0$）的蛛网图。在混沌状态下，轨迹似乎随机地填充了函数曲线和对角线之间的区域。

### 分岔图与混沌

为了全面了解参数 $r$ 对系统行为的影响，我们可以绘制分岔图，即对于每个 $r$，将长期迭代的 $x_t$ 值绘制出来。以下代码生成逻辑斯谛映射的分岔图：

```python
def bifurcation_diagram(r_min=2.5, r_max=4.0, n_r=1000, n_transient=500, n_iter=100, x0=0.3):
    """
    绘制逻辑斯谛映射的分岔图。
    
    参数:
        r_min, r_max: r的取值范围
        n_r: r的采样点数
        n_transient: 抛弃的瞬态迭代次数
        n_iter: 记录迭代的次数
        x0: 初始值（每个r都从x0开始）
    """
    r_vals = np.linspace(r_min, r_max, n_r)
    # 初始化存储数组
    x_vals = []
    r_plot = []
    
    for r in r_vals:
        x = x0
        # 抛弃瞬态
        for _ in range(n_transient):
            x = r * x * (1 - x)
        # 记录后续迭代
        for _ in range(n_iter):
            x = r * x * (1 - x)
            x_vals.append(x)
            r_plot.append(r)
    
    # 绘制散点图
    plt.figure(figsize=(10, 6))
    plt.scatter(r_plot, x_vals, s=0.01, c='k', alpha=0.5)
    plt.xlabel('$r$', fontsize=14)
    plt.ylabel('$x$ (长期值)', fontsize=14)
    plt.title('逻辑斯谛映射分岔图', fontsize=16)
    plt.grid(True, alpha=0.3)
    plt.show()

bifurcation_diagram()
```

分岔图清晰地展示了从稳定平衡到倍周期分岔再到混沌的过程。在混沌区域（如 $r \approx 4$），系统对初始条件极其敏感，即著名的“蝴蝶效应”。这正是混沌系统的特征：确定性方程产生看似随机的输出，并且长期预测不可能。

## 2.2.2. 连续的种群增长：导数与积分

当种群数量很大且世代重叠时，离散时间模型可能不再适用，我们需要连续时间模型。连续模型用微分方程描述种群瞬时变化率。

### 指数增长模型

设 $N(t)$ 表示时刻 $t$ 的种群数量。最简单的连续增长模型是指数增长：

$$
\frac{dN}{dt} = r N
$$

其中 $r$ 是瞬时增长率。这个微分方程表示种群变化率与当前数量成正比。方程的解为：

$$
N(t) = N_0 e^{rt}
$$

其中 $N_0 = N(0)$ 是初始数量。指数增长在资源无限时是合理的，但现实世界中资源有限，因此我们需要引入密度制约。

### 逻辑斯谛增长模型

在连续时间中，密度制约表现为增长率随种群数量增加而下降。逻辑斯谛方程是：

$$
\frac{dN}{dt} = r N \left(1 - \frac{N}{K}\right)
$$

其中 $K$ 是环境容纳量。当 $N$ 接近 $K$ 时，增长率趋近于零。这个方程可以解析求解（通过分离变量法），得到：

$$
N(t) = \frac{K}{1 + \left(\dfrac{K - N_0}{N_0}\right) e^{-rt}}
$$

逻辑斯谛增长曲线呈S形（Sigmoid），从初始指数增长逐渐减速，最终趋于 $K$。

### 导数与积分的生物学意义

在连续模型中，导数 $\dfrac{dN}{dt}$ 表示种群数量在时刻 $t$ 的**瞬时变化率**。它告诉我们种群增长的速度。例如，在逻辑斯谛模型中，当 $N$ 很小时，$\dfrac{dN}{dt} \approx r N$，近似指数增长；当 $N$ 接近 $K$ 时，变化率趋近于零。

积分则是导数的逆运算。从变化率 $dN/dt$ 求种群数量 $N(t)$ 的过程就是积分。指数增长和逻辑斯谛增长模型的解析解就是通过积分得到的。在实际应用中，我们经常需要数值积分来求解无法解析求解的微分方程。

## 2.2.3. 增长曲线拟合

在实际研究中，我们经常需要根据实验数据估计模型参数。例如，给定一组时间序列的种群数量数据，我们希望拟合逻辑斯谛曲线，估计参数 $r$ 和 $K$。

### 方法一：直接使用非线性最小二乘法

我们可以使用 `scipy.optimize.curve_fit` 函数直接拟合逻辑斯谛函数。假设我们有一组数据 $(t_i, N_i)$，定义逻辑斯谛函数：

```python
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def logistic_growth(t, N0, r, K):
    """逻辑斯谛增长函数"""
    return K / (1 + (K - N0) / N0 * np.exp(-r * t))

# 生成模拟数据（带噪声）
np.random.seed(42)
t_data = np.linspace(0, 20, 21)
N0_true, r_true, K_true = 10, 0.5, 500
N_data = logistic_growth(t_data, N0_true, r_true, K_true) + np.random.normal(0, 20, len(t_data))

# 拟合参数
p0 = [5, 0.3, 300]  # 初始猜测值
params, params_cov = curve_fit(logistic_growth, t_data, N_data, p0=p0)
N0_fit, r_fit, K_fit = params
print(f"拟合参数: N0 = {N0_fit:.2f}, r = {r_fit:.4f}, K = {K_fit:.2f}")

# 绘制拟合曲线
t_fine = np.linspace(0, 20, 200)
N_fit = logistic_growth(t_fine, N0_fit, r_fit, K_fit)

plt.figure(figsize=(8, 6))
plt.scatter(t_data, N_data, label='数据点', c='k')
plt.plot(t_fine, N_fit, 'r-', label='拟合曲线')
plt.xlabel('时间', fontsize=14)
plt.ylabel('种群数量', fontsize=14)
plt.title('逻辑斯谛增长曲线拟合', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
```

### 方法二：线性化后拟合

对于逻辑斯谛方程，我们可以通过变换将其线性化，然后使用线性回归。逻辑斯谛方程可以改写为：

$$
\frac{1}{N} \frac{dN}{dt} = r - \frac{r}{K} N
$$

然而，我们通常没有瞬时变化率的数据。另一种方法是利用积分式的变形。从逻辑斯谛解：

$$
\ln\left(\dfrac{K - N}{N}\right) = \ln\left(\dfrac{K - N_0}{N_0}\right) - r t
$$

如果我们已知 $K$，则可以对 $\ln((K-N)/N)$ 关于 $t$ 进行线性回归得到 $r$。但 $K$ 通常是未知的。一种常用的方法是**三点法**，或者采用非线性拟合。

实际上，直接非线性拟合更为方便可靠，线性化方法可能会引入偏差（因为变换会改变误差结构）。但在某些情况下，线性化可以提供快速的参数估计。

## 思考题

1. **离散逻辑斯谛映射的稳定性分析**：
   - 对于逻辑斯谛映射 $x_{n+1} = r x_n (1 - x_n)$，验证当 $r = 2.5$ 时，非零平衡点 $\overline{x} = 1 - 1/r$ 是稳定的。计算 $f'(\overline{x})$，并利用蛛网图展示收敛过程。
   - 当 $r = 3.2$ 时，系统出现周期2振荡。通过计算二阶复合映射 $f(f(x))$ 的导数，验证周期2轨道的稳定性。

2. **连续逻辑斯谛增长拟合**：
   - 使用上面提供的代码生成不同噪声水平的模拟数据，分别用直接拟合和线性化方法拟合逻辑斯谛曲线，比较两种方法的参数估计误差。
   - 尝试用指数增长模型拟合逻辑斯谛增长数据，比较残差，说明密度制约的重要性。

3. **混沌与敏感性**：
   - 取 $r = 4.0$，选择两个非常接近的初始值（如 $x_0 = 0.3$ 和 $x_0 = 0.3001$），迭代100次，计算两个序列的差异随时间的变化。绘制差异的对数随时间的变化图，并估计李雅普诺夫指数（近似为差异对数的平均斜率）。

4. **实际数据拟合**：
   - 查找一组实际种群增长数据（例如，微生物培养、昆虫种群等），尝试用逻辑斯谛模型进行拟合。讨论模型的适用性和局限性。

通过本节的学习，你应掌握离散和连续种群增长模型的基本概念，理解导数与积分在描述动态过程中的作用，并能够使用Python进行模型模拟和参数拟合。这些技能将为后续学习更复杂的生物动力系统奠定基础。