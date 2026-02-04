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

### 2.2.1.2.蛛网图（Cobweb plot）可视化

蛛网图是一种可视化离散映射迭代过程的工具。它通过绘制函数 $f(x) = rx(1-x)$ 和对角线 $f(x) = x$，并追踪迭代路径，帮助我们直观理解系统的动态。

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
    
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('f(x)', fontsize=14)
    ax.set_title(f'Logistic cobweb plot (r = {r}, x0 = {x0})', fontsize=16)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return ax

# 示例：绘制不同r值的蛛网图
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
r_vals = [0.75, 1.5, 2, 2.5]
x0 = 0.3
n_iter = 50

for i, (r, ax) in enumerate(zip(r_vals, axes.flat)):
    cobweb_plot(r, x0, n_iter, ax)
    # 标注平衡点（如果存在）
    if r > 1:
        x_eq = 1 - 1/r
        ax.plot(x_eq, x_eq, 'go', markersize=8, label='Equilibrium point')
        ax.legend()

plt.tight_layout()
plt.subplots_adjust(hspace=0.3)
plt.show()
```

可能需要稍加理解绘图逻辑：在每个迭代步骤，我们绘制从当前 $x_t$ 到下一个 $x_{t+1}$ ，即 $f(x_t)$ 的垂直线，再画水平线到 $f(x)=x$，从该点进行下一次迭代。这些线段构成了“蛛网”，显示了种群数量如何在每次迭代中沿着逻辑斯谛曲线移动。

通过改变 $r$ 的值，我们可以观察到：
- $r=0.75$（代表$0<r<1$）时，不存在平衡点，种群衰落
- $r=1.5$（代表$1<r<2$）时，在 $f(x)$ 的上升段有平衡点
- $r=2.0$ 时，在 $f(x)$ 的顶点有平衡点
- $r=2.5$（代表$2<r<3$）时，在 $f(x)$ 的下降段有平衡点振荡

```python-plot
import numpy as np
import matplotlib.pyplot as plt

def cobweb_plot(r, x0, n_iter, ax=None, n_skip=0):
    """
    绘制逻辑斯谛映射的蛛网图。
    
    参数:
        r: 增长率
        x0: 初始值
        n_iter: 绘图的迭代次数
        ax: matplotlib轴对象，若为None则创建新图
        n_skip: 绘图前忽略的瞬态迭代次数
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
    
    # 1. 瞬态迭代：不绘图，只更新状态，消除初始 transient
    for _ in range(n_skip):
        x_current = r * x_current * (1 - x_current)
        
    # 2. 稳态迭代：绘图
    for i in range(n_iter):
        y_current = r * x_current * (1 - x_current)
        # 垂直线
        ax.plot([x_current, x_current], [x_current, y_current], 'r-', lw=0.5)
        # 水平线
        ax.plot([x_current, y_current], [y_current, y_current], 'r-', lw=0.5)
        x_current = y_current
    
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('f(x)', fontsize=14)
    ax.set_title(f'Logistic cobweb plot (r = {r}, x0 = {x0})', fontsize=16)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return ax

# 示例：绘制不同r值的蛛网图
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
r_vals = [3.2, 3.5, 3.662117, 4]
x0 = 0.3
n_iter = 100  # 增加绘图轮数以展示完整轨迹
n_skip = 1000 # 忽略前1000次迭代，确保进入稳定状态

for i, (r, ax) in enumerate(zip(r_vals, axes.flat)):
    cobweb_plot(r, x0, n_iter, ax, n_skip=n_skip)
    # 标注平衡点（如果存在）
    if r > 1:
        x_eq = 1 - 1/r
        ax.plot(x_eq, x_eq, 'go', markersize=8, label='Equilibrium point')
        ax.legend()

plt.tight_layout()
plt.subplots_adjust(hspace=0.3)
plt.show()
```

$r>3$ 时，为了使系统达到稳定震荡状态，我们忽略前1000次迭代，然后记录100次迭代的过程：
- $r=3.2$（代表$3<r<1+\sqrt{6}$）时，系统出现周期 2 振荡
- $r=3.5$（代表$r>1+\sqrt{6}$）时，系统出现周期 4 振荡，相比之前呈现周期倍增
- $r=3.662117$时，系统出现周期 8 振荡，此后振荡周期数改变越来越密集
- $r=4$时，系统混沌，无法找出振荡现象的发生

### 2.2.1.3.分岔图与混沌

为了全面了解参数 $r$ 对系统行为的影响，我们可以绘制分岔图，即对于每个 $r$，将长期迭代后稳定的 $x_t$ 值绘制出来。以下代码生成逻辑斯谛映射的分岔图：

```python-plot
import numpy as np
import matplotlib.pyplot as plt

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
    plt.ylabel('$x$', fontsize=14)
    plt.title('Logistic bifurcation diagram', fontsize=16)
    plt.grid(True, alpha=0.3)
    plt.show()

bifurcation_diagram()
```

分岔图清晰地展示了从稳定平衡到倍周期分岔再到混沌的过程。在混沌区域（如 $r \approx 4$），系统对初始条件极其敏感，即著名的“蝴蝶效应”。这正是混沌系统的特征：确定性方程产生看似随机的输出，并且长期预测不可能。

类似地，$sin$ 曲线的混沌行为也可以通过类似的分岔图来展示，其中 $r$ 对应于频率或周期。两张图的形状几乎一模一样：
```python-plot
import numpy as np
import matplotlib.pyplot as plt

def bifurcation_diagram(r_min=0.6, r_max=1.0, n_r=1000, n_transient=500, n_iter=100, x0=0.3):
    """
    绘制正弦映射(Sine map)的分岔图。
    
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
            x = r * np.sin(np.pi * x)
        # 记录后续迭代
        for _ in range(n_iter):
            x = r * np.sin(np.pi * x)
            x_vals.append(x)
            r_plot.append(r)
    
    # 绘制散点图
    plt.figure(figsize=(10, 6))
    plt.scatter(r_plot, x_vals, s=0.01, c='k', alpha=0.5)
    plt.xlabel('$r$', fontsize=14)
    plt.ylabel('$x$', fontsize=14)
    plt.title('Sine Map bifurcation diagram', fontsize=16)
    plt.grid(True, alpha=0.3)
    plt.show()

bifurcation_diagram()
```

这种倍周期现象是如何产生的呢？在一定程度上，我们可以用重整化群来解释：

### 2.2.1.4.重整化群：从自相似到普适性

重整化群（Renormalization Group, RG）是一个强大的理论框架，帮助我们理解为什么逻辑斯蒂映射会表现出如此规则的分岔模式。让我们从数值实验开始，直观感受重整化群的核心思想。

通过数值实验，我们可以发现逻辑斯蒂映射中惊人的自相似性：

```python-plot
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# 1. 分岔图：展示全局模式
def logistic_bifurcation(r_min=2.5, r_max=4.0, n_r=1000):
    """绘制逻辑斯蒂映射的分岔图"""
    r_vals = np.linspace(r_min, r_max, n_r)
    n_transient = 500  # 丢弃瞬态
    n_record = 100     # 记录稳态
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # 左侧：完整分岔图
    ax1 = axes[0]
    x_vals = []
    r_plot = []
    
    for r in r_vals:
        x = 0.5  # 固定初始值
        # 丢弃瞬态
        for _ in range(n_transient):
            x = r * x * (1 - x)
        # 记录
        for _ in range(n_record):
            x = r * x * (1 - x)
            x_vals.append(x)
            r_plot.append(r)
    
    ax1.scatter(r_plot, x_vals, s=0.1, c='k', alpha=0.5)
    ax1.set_xlabel('r', fontsize=14)
    ax1.set_ylabel('x', fontsize=14)
    ax1.set_title('Logistic Bifurcation Diagram', fontsize=16)
    ax1.grid(True, alpha=0.3)
    
    # 右侧：局部放大 - 展示自相似结构
    ax2 = axes[1]
    # 放大到周期4区域
    r_min_zoom, r_max_zoom = 3.45, 3.57
    mask = (np.array(r_plot) >= r_min_zoom) & (np.array(r_plot) <= r_max_zoom)
    ax2.scatter(np.array(r_plot)[mask], np.array(x_vals)[mask], s=0.1, c='k', alpha=0.5)
    ax2.set_xlabel('r', fontsize=14)
    ax2.set_ylabel('x', fontsize=14)
    ax2.set_title('Zoom: Self-Similar Structure', fontsize=16)
    ax2.set_xlim(r_min_zoom, r_max_zoom)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

logistic_bifurcation()
```

**观察**：右侧的局部放大图看起来像是左侧整体图的缩小版，这就是**自相似性**——整体结构在局部重复出现。

这种自相似性在迭代函数中表现得更加明显。我们比较不同阶数的迭代函数（即 $f(x)$, $f(f(x))$, $f^{(4)}(x)$）：

```python-plot
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def plot_iterated_functions():
    """比较不同阶数的迭代函数"""
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    x = np.linspace(0, 1, 1000)
    
    # 第一列：f(x) for r=2
    r1 = 2.0
    ax1 = axes[0]
    f1 = r1 * x * (1 - x)
    ax1.plot(x, f1, 'b-', linewidth=2, label=f'$f(x)$, r={r1}')
    ax1.plot(x, x, 'k--', linewidth=1, label='$y=x$')
    ax1.set_xlabel('x', fontsize=12)
    ax1.set_ylabel('f(x)', fontsize=12)
    ax1.set_title('Original Map', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    
    # 第二列：f(f(x)) for r=3.2
    r2 = 3.2
    ax2 = axes[1]
    f2 = r2 * x * (1 - x)
    ff2 = r2 * f2 * (1 - f2)
    
    # 标记不动点（周期2轨道）
    # 求解 f(f(x)) = x 的非零解
    def fixed_points(r):
        """返回周期2轨道的两个点"""
        # 解方程 f(f(x)) - x = 0
        solutions = []
        for guess in [0.2, 0.4, 0.6, 0.8]:
            sol = fsolve(lambda y: r * (r * y * (1 - y)) * (1 - r * y * (1 - y)) - y, guess, full_output=True)
            if sol[2] == 1 and 0 < sol[0][0] < 1:
                solutions.append(sol[0][0])
        return np.unique(np.round(solutions, 6))
    
    period2_points = fixed_points(r2)
    
    ax2.plot(x, ff2, 'b-', linewidth=2, label=f'$f(f(x))$, r={r2}')
    ax2.plot(x, x, 'k--', linewidth=1, label='$y=x$')
    # 标记不动点
    for point in period2_points:
        ax2.plot([point], [point], 'ro', markersize=8)
    
    # 标记x=0.5附近的区域
    ax2.add_patch(plt.Rectangle((0.3, 0.3), 0.4, 0.4, 
                               edgecolor='red', facecolor='none', 
                               linestyle='--', linewidth=2))
    
    ax2.set_xlabel('x', fontsize=12)
    ax2.set_ylabel('f(f(x))', fontsize=12)
    ax2.set_title('Period-2: Two Fixed Points', fontsize=14)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    
    # 第三列：f^{(4)}(x) for r=3.5
    r3 = 3.5
    ax3 = axes[2]
    
    # 计算 f^{(4)}(x)
    def iterate(f, x, n):
        """迭代函数n次"""
        result = x
        for _ in range(n):
            result = r3 * result * (1 - result)
        return result
    
    f4 = iterate(lambda y: r3 * y * (1 - y), x, 4)
    
    ax3.plot(x, f4, 'b-', linewidth=2, label=f'$f^{(4)}(x)$, r={r3}')
    ax3.plot(x, x, 'k--', linewidth=1, label='$y=x$')
    
    # 标记x=0.5附近的区域（更小）
    ax3.add_patch(plt.Rectangle((0.425, 0.425), 0.15, 0.15,
                               edgecolor='red', facecolor='none',
                               linestyle='--', linewidth=2))
    
    ax3.set_xlabel('x', fontsize=12)
    ax3.set_ylabel(f'$f^{(4)}(x)$', fontsize=12)
    ax3.set_title('Period-4: Four Fixed Points', fontsize=14)
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    
    plt.tight_layout()
    plt.show()

plot_iterated_functions()
```

**关键观察**：
1. **r=3.2时**：$f(f(x))$在$x=0.5$附近区域（红色方框）看起来像是$f(x)$在$r=2$时的**倒置版本**。
2. **r=3.5时**：$f^{(4)}(x)$在$x=0.5$附近的小区域（红色方框）看起来又像是$f(f(x))$在某个参数下的缩小版。

这种自相似性正是重整化群的核心。让我们通过具体操作来理解：

```python-plot
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def renormalization_demo():
    """重整化群操作演示"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 参数设置
    r = 3.5  # 处于周期4区域
    x = np.linspace(0, 1, 1000)
    
    # 1. 原始函数 f(x)
    ax1 = axes[0, 0]
    f = r * x * (1 - x)
    ax1.plot(x, f, 'b-', linewidth=2)
    ax1.plot(x, x, 'k--', linewidth=1)
    ax1.set_xlabel('x', fontsize=12)
    ax1.set_ylabel('f(x)', fontsize=12)
    ax1.set_title(f'Original: f(x), r={r}', fontsize=14)
    ax1.grid(True, alpha=0.3)
    
    # 2. 两次迭代 f(f(x))
    ax2 = axes[0, 1]
    ff = r * f * (1 - f)
    ax2.plot(x, ff, 'b-', linewidth=2)
    ax2.plot(x, x, 'k--', linewidth=1)
    
    # 找出其中一个不动点区域（周期2轨道中的一个点）
    # 这里我们手动选取一个区域进行放大
    zoom_center = 0.5
    zoom_width = 0.2
    
    ax2.add_patch(plt.Rectangle((zoom_center-zoom_width/2, zoom_center-zoom_width/2),
                               zoom_width, zoom_width,
                               edgecolor='red', facecolor='none',
                               linestyle='--', linewidth=2))
    ax2.set_xlabel('x', fontsize=12)
    ax2.set_ylabel('f(f(x))', fontsize=12)
    ax2.set_title(f'First iteration: f(f(x))', fontsize=14)
    ax2.grid(True, alpha=0.3)
    
    # 3. 放大区域：展示自相似性
    ax3 = axes[1, 0]
    # 在红色框内采样
    x_zoom = np.linspace(zoom_center-zoom_width/2, zoom_center+zoom_width/2, 200)
    ff_zoom = r * (r * x_zoom * (1 - x_zoom)) * (1 - r * x_zoom * (1 - x_zoom))
    
    # 坐标变换：将区域映射到[0,1]
    x_normalized = (x_zoom - (zoom_center-zoom_width/2)) / zoom_width
    # 函数值也需要归一化
    ff_normalized = (ff_zoom - (zoom_center-zoom_width/2)) / zoom_width
    
    # 为了比较，绘制原始f(x)在r=2时的形状（但需要调整方向）
    r_comparison = 2.0
    f_comparison = r_comparison * x_normalized * (1 - x_normalized)
    
    ax3.plot(x_normalized, -ff_normalized + 1, 'r-', linewidth=2, label='Rescaled f(f(x))')
    ax3.plot(x_normalized, f_comparison, 'b--', linewidth=2, label=f'f(x) with r={r_comparison}')
    ax3.plot(x_normalized, x_normalized, 'k:', linewidth=1)
    
    ax3.set_xlabel('Rescaled x', fontsize=12)
    ax3.set_ylabel('Rescaled f', fontsize=12)
    ax3.set_title('Renormalization: Self-Similarity', fontsize=14)
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3)
    
    # 4. 数值计算Feigenbaum常数
    ax4 = axes[1, 1]
    ax4.axis('off')
    
    # 计算分岔点序列
    def bifurcation_points(order=6):
        """近似计算前n个分岔点"""
        # 已知的一些分岔点近似值
        # r1: 周期1->2 (r=3)
        # r2: 周期2->4 (r≈3.4494897)
        # r3: 周期4->8 (r≈3.544090)
        # r4: 周期8->16 (r≈3.564407)
        # r5: 周期16->32 (r≈3.568759)
        # r6: 周期32->64 (r≈3.569692)
        
        r_vals = [3.0, 3.4494897, 3.544090, 3.564407, 3.568759, 3.569692]
        return r_vals[:order]
    
    r_vals = bifurcation_points(6)
    
    # 计算Feigenbaum常数δ
    deltas = []
    for i in range(1, len(r_vals)-1):
        delta = (r_vals[i] - r_vals[i-1]) / (r_vals[i+1] - r_vals[i])
        deltas.append(delta)
    
    text = "Feigenbaum Constants:\n\n"
    text += "Bifurcation points:\n"
    for i, r_val in enumerate(r_vals):
        period = 2**i
        text += f"  Period {period} → {period*2}: r_{i+1} = {r_val:.6f}\n"
    
    text += "\nδ (interval ratio):\n"
    for i, delta in enumerate(deltas):
        text += f"  δ_{i+1} = {delta:.4f}\n"
    
    text += f"\nLimit δ∞ ≈ 4.669201609...\n"
    text += f"Our approx: {deltas[-1]:.4f}"
    
    ax4.text(0.1, 0.9, text, fontsize=11, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.show()

renormalization_demo()
```

上述观察可以形式化为**重整化群方程**。当我们进行尺度变换时，函数的行为满足：

$$
\mathcal{R}[f](x) = \alpha f\left(f\left(\frac{x}{\alpha}\right)\right) \approx f(x)
$$

其中 $\mathcal{R}$ 是重整化群算子，$g$ 是映射函数，$\alpha$ 是缩放因子。该变换描述了在倍周期分岔序列中，映射函数在尺度变换下的自相似行为。**不动点方程** $\mathcal{R}[g^*] = g^*$ 的解 $g^*$ 称为**普适函数（universal function）**，它决定了倍周期分岔的临界行为。

费根鲍姆（Feigenbaum）通过数值计算发现，在倍周期分岔序列中，两个关键常数具有普适性：

1. **分岔参数间隔比 $\delta$**：
   $$
   \delta = \lim_{n\to\infty} \frac{r_n - r_{n-1}}{r_{n+1} - r_n} \approx 4.669
   $$
   其中 $r_n$ 是第 $n$ 次倍周期分岔发生时的参数值。

2. **轨道尺度缩放比 $\alpha$**：
   $$
   \alpha = \lim_{n\to\infty} \frac{d_n}{d_{n+1}} \approx -2.5029
   $$
   其中 $d_n$ 是第 $n$ 周期轨道在分岔点处的特征间距。

这些常数不仅适用于逻辑斯谛映射，也适用于一大类单峰映射（unimodal maps），体现了混沌现象的**普适性（universality）**。

让我们尝试数值寻找普适函数：

```python-plot
import numpy as np
import matplotlib.pyplot as plt

def universal_function_search():
    """寻找普适函数的数值尝试"""
    
    # Feigenbaum常数
    alpha = -2.5029
    
    # 定义逻辑斯蒂族
    def f(r, x):
        return r * x * (1 - x)
    
    # 重整化群操作
    def renormalize(g, x):
        """对函数g应用一次重整化变换"""
        return alpha * g(g(x / alpha))
    
    # 选择一个接近混沌边界的r值
    r_inf = 3.5699456  # 累积分岔点
    n_iter = 10
    
    # 初始猜测：r_inf时的逻辑斯蒂映射
    x_domain = np.linspace(-0.5, 0.5, 1000)
    g_current = lambda x: f(r_inf, x + 0.5) - 0.5  # 中心化
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 绘制迭代过程
    colors = plt.cm.viridis(np.linspace(0, 1, n_iter))
    
    for i in range(n_iter):
        # 计算当前函数
        y_current = g_current(x_domain)
        
        # 绘制（跳过前几次，它们可能不稳定）
        if i >= 5:
            ax.plot(x_domain, y_current, color=colors[i], 
                   alpha=0.7, linewidth=2, 
                   label=f'Iteration {i}' if i % 2 == 0 else '')
        
        # 应用重整化
        # 关键修改：使用默认参数 g=g_current 来捕获当前的函数对象
        # 否则 lambda 会引用循环变量名，导致无限递归
        g_new = lambda x, g=g_current: renormalize(g, x)
        g_current = g_new
    
    ax.plot(x_domain, x_domain, 'k--', linewidth=1, label='y=x')
    ax.set_xlabel('x (rescaled)', fontsize=14)
    ax.set_ylabel('g(x)', fontsize=14)
    ax.set_title('Renormalization Group Flow to Universal Function', fontsize=16)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-0.5, 0.5)
    
    # 在图中添加文本显示 alpha 值，替代 print 输出
    ax.text(0.05, 0.95, f'Scaling factor $\\alpha \\approx {alpha}$', 
            transform=ax.transAxes, fontsize=12, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.tight_layout()
    plt.show()
    
universal_function_search()
```

即使看不懂重整化群的这一部分，我们至少可以得到一个感想：即使是逻辑斯谛方程这样简单的形式，也能衍生出非常复杂的混沌现象，可以借此体会为什么说生命系统以不可求解的非线性动力学为主，所以即使是把时间尺度分得再小，这样的模拟方法在解决生物问题时都是有可能行不通的，这也是为什么我们需要不断地对方法进行整合。接下来的内容可以视为把上述刻画逻辑斯谛方程的过程整合为导数与积分。

### 2.2.1.5.李雅普诺夫指数与混沌检测

对于非线性系统，长期行为可能极为复杂，包括混沌。**李雅普诺夫指数（Lyapunov Exponent）** 量化了相邻轨迹的发散速率，是检测混沌的重要指标。

对于一维离散映射 $x_{n+1} = f(x_n)$，考虑两个初始条件极其接近的轨道：$x_0$ 和 $x_0 + \delta_0$，其中 $\delta_0$ 极小。经过一次迭代后，它们的距离为：

$$
\delta_1 = |f(x_0 + \delta_0) - f(x_0)| \approx |f'(x_0)|\cdot|\delta_0|
$$

经过 $n$ 次迭代后：

$$
\delta_n \approx |f'(x_{n-1})f'(x_{n-2})\cdots f'(x_0)|\cdot|\delta_0|
$$

取对数并除以 $n$：

$$
\frac{1}{n} \ln\left|\frac{\delta_n}{\delta_0}\right| \approx \frac{1}{n} \sum_{i=0}^{n-1} \ln|f'(x_i)|
$$

当 $n \to \infty$ 时，得到**李雅普诺夫指数**：

$$
\lambda = \lim_{n\to\infty} \frac{1}{n} \sum_{i=0}^{n-1} \ln|f'(x_i)|
$$

- $\lambda > 0$：相邻轨道指数发散，系统对初始条件极度敏感 → **混沌**
- $\lambda = 0$：相邻轨道保持恒定距离 → **周期边界**（如临界分岔点）
- $\lambda < 0$：相邻轨道指数收敛 → **稳定周期或平衡点**

对于 $d$ 维系统，有 $d$ 个李雅普诺夫指数，按大小排列 $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_d$。若 $\lambda_1 > 0$，系统呈现混沌行为。

对于逻辑斯蒂映射 $x_{n+1} = rx_n(1-x_n)$，导数为 $f'(x) = r(1-2x)$，因此：

$$
\lambda(r) = \lim_{n\to\infty} \frac{1}{n} \sum_{i=0}^{n-1} \ln|r(1-2x_i)|
$$

将李雅普诺夫指数谱与分岔图结合，可以直观地看到混沌区域与周期区域：

```python-plot
import numpy as np
import matplotlib.pyplot as plt

def lyapunov_exponent_logistic(r, x0, n_iter=10000, n_transient=1000):
    """
    计算逻辑斯谛映射的李雅普诺夫指数。
    
    参数:
        r: 参数
        x0: 初始值
        n_iter: 总迭代次数
        n_transient: 抛弃的瞬态迭代次数
    
    返回:
        李雅普诺夫指数估计值
    """
    x = x0
    # 抛弃瞬态
    for _ in range(n_transient):
        x = r * x * (1 - x)
    
    # 计算李雅普诺夫指数
    lyap_sum = 0.0
    for _ in range(n_iter):
        # 计算导数 |f'(x)|
        df_dx = abs(r * (1 - 2*x))
        lyap_sum += np.log(df_dx)
        x = r * x * (1 - x)
    
    return lyap_sum / n_iter

# 计算不同r值的李雅普诺夫指数
# 增加分辨率以获得更好的分岔图效果
r_values = np.linspace(2.8, 4.0, 1000)
lyap_values = []
for r in r_values:
    # 适当减少迭代次数以平衡计算时间
    lyap = lyapunov_exponent_logistic(r, 0.5, n_iter=2000)
    lyap_values.append(lyap)

# 生成分岔图数据
x_vals_bif = []
r_vals_bif = []
n_transient_bif = 500
n_iter_bif = 100

for r in r_values:
    x = 0.5
    # 抛弃瞬态
    for _ in range(n_transient_bif):
        x = r * x * (1 - x)
    # 记录后续迭代
    for _ in range(n_iter_bif):
        x = r * x * (1 - x)
        x_vals_bif.append(x)
        r_vals_bif.append(r)

# 绘制图形：合二为一
plt.figure(figsize=(12, 8))

# 1. 绘制分岔图 (黑色散点)
# alpha设得很低以便在密集处看清结构
plt.scatter(r_vals_bif, x_vals_bif, s=0.05, c='k', alpha=0.2, label='Bifurcation ($x$)')

# 2. 绘制李雅普诺夫指数谱 (蓝色曲线)
plt.plot(r_values, lyap_values, 'b-', linewidth=1.5, alpha=0.9, label='Lyapunov ($\\lambda$)')

# 标记混沌区域（λ>0）
chaotic_region = np.array(lyap_values) > 0
plt.fill_between(r_values, 0, lyap_values, where=chaotic_region, 
                 color='red', alpha=0.3, label='Chaotic region (λ>0)')

# 0刻度线
plt.axhline(y=0, color='r', linestyle='--', linewidth=1.0)

plt.xlabel('$r$', fontsize=14)
plt.ylabel('$x$  and  $\\lambda$', fontsize=14)
plt.title('Bifurcation Diagram combined with Lyapunov Exponent', fontsize=16)
plt.grid(True, alpha=0.3)

# 限制Y轴范围，因为Lyapunov指数在超稳定周期轨道处可能趋向负无穷
# 同时也保证分岔图(0~1)清晰可见
plt.ylim(-2.5, 1.2)

# 优化图例显示 (markerscale用于放大散点图例图标)
plt.legend(loc='lower left', markerscale=40, fontsize=12)

plt.tight_layout()
plt.show()
```

## 2.2.2.连续的种群增长：导数与积分

当种群数量很大且世代重叠时，离散时间模型可能不再适用，我们需要连续时间模型。连续模型用微分方程描述种群瞬时变化率。

### 2.2.2.1.指数增长模型

设 $N(t)$ 表示时刻 $t$ 的种群数量。最简单的连续增长模型是指数增长：

$$
\frac{dN}{dt} = r N
$$

其中 $r$ 是瞬时增长率。这个微分方程表示种群变化率与当前数量成正比。方程的积分式为：

$$
N(t) = N_0 e^{rt}
$$

其中 $N_0 = N(0)$ 是初始数量。指数增长在资源无限时是合理的，但现实世界中资源有限，因此我们需要引入密度制约。

### 2.2.2.2.逻辑斯谛增长模型

在连续时间中，密度制约表现为增长率随种群数量增加而下降。逻辑斯谛方程是：

$$
\frac{dN}{dt} = r N \left(1 - \frac{N}{K}\right)
$$

其中 $K$ 是环境容纳量。当 $N$ 接近 $K$ 时，增长率趋近于零。这个方程可以解析求解（通过分离变量法），得到：

$$
N(t) = \frac{K}{1 + \left(\dfrac{K - N_0}{N_0}\right) e^{-rt}}
$$

逻辑斯谛增长曲线呈S形（Sigmoid），从初始指数增长逐渐减速，最终趋于 $K$。

求解步骤如下：

1. 分离变量，将方程改写为：
$$
\frac{dN}{N \left(1 - \frac{N}{K}\right)} = r \, dt
$$

2. 分解有理式，对左边分母进行部分分式分解：
$$
\frac{1}{N \left(1 - \frac{N}{K}\right)} = \frac{1}{N} + \frac{1}{K - N}
$$
代入得：
$$
\left( \frac{1}{N} + \frac{1}{K - N} \right) dN = r \, dt
$$

3. 两边积分：
$$
\int \left( \frac{1}{N} + \frac{1}{K - N} \right) dN = \int r \, dt
$$
计算积分：
$$
\ln |N| - \ln |K - N| = rt + C
$$
其中 $C$ 为积分常数。合并对数项：
$$
\ln \left| \frac{N}{K - N} \right| = rt + C
$$

4. 消去对数取指数：
$$
\left| \frac{N}{K - N} \right| = e^{rt + C} = A e^{rt}
$$
其中 $A = e^C > 0$。当 $0 < N < K$ 时，可去掉绝对值：
$$
\frac{N}{K - N} = A e^{rt}
$$

5. 整理方程，解出 $N(t)$：
：
$$
N = (K - N) A e^{rt} = K A e^{rt} - N A e^{rt}
$$
$$
N (1 + A e^{rt}) = K A e^{rt}
$$
$$
N(t) = \frac{K A e^{rt}}{1 + A e^{rt}}
$$

6. 由初始条件确定常数 $A$：
代入 $t = 0$，$N(0) = N_0$：
$$
N_0 = \frac{K A}{1 + A}
$$
解得：
$$
A = \frac{N_0}{K - N_0}
$$

7. 代入得最终解：
将 $A$ 代入 $N(t)$：
$$
N(t) = \frac{K \cdot \frac{N_0}{K - N_0} \cdot e^{rt}}{1 + \frac{N_0}{K - N_0} \cdot e^{rt}}
$$
分子分母同乘以 $K - N_0$：
$$
N(t) = \frac{K N_0 e^{rt}}{K - N_0 + N_0 e^{rt}}
$$
或等价地，分子分母同除以 $N_0 e^{rt}$：
$$
N(t) = \frac{K}{1 + \left( \frac{K - N_0}{N_0} \right) e^{-rt}}
$$

### 2.2.2.3.导数与积分的生物学意义

在连续模型中，导数 $\dfrac{dN}{dt}$ 表示种群数量在时刻 $t$ 的**瞬时变化率**。它告诉我们种群增长的速度。例如，在逻辑斯谛模型中，当 $N$ 很小时，$\dfrac{dN}{dt} \approx r N$，近似指数增长；当 $N$ 接近 $K$ 时，变化率趋近于零。

积分则是导数的逆运算。从变化率 $dN/dt$ 求种群数量 $N(t)$ 的过程就是积分。指数增长和逻辑斯谛增长模型的解析解就是通过积分得到的。在实际应用中，我们经常需要数值积分来求解无法解析求解的微分方程。

## 2.2.3.增长曲线拟合

在实际研究中，我们经常需要根据实验数据估计模型参数。例如，给定一组时间序列的种群数量数据，我们希望拟合逻辑斯谛曲线，估计参数 $r$ 和 $K$。

### 2.2.3.1.直接使用非线性最小二乘法

我们可以使用 `scipy.optimize.curve_fit` 函数直接拟合逻辑斯谛函数。假设我们有一组数据 $(t_i, N_i)$，定义逻辑斯谛函数：

```python-plot
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

# 绘制拟合曲线
t_fine = np.linspace(0, 20, 200)
N_fit = logistic_growth(t_fine, N0_fit, r_fit, K_fit)

plt.figure(figsize=(8, 6))
plt.scatter(t_data, N_data, label='Data Points', c='k')
plt.plot(t_fine, N_fit, 'r-', label='Fitted Curve')
plt.xlabel('Time', fontsize=14)
plt.ylabel('Population Size', fontsize=14)
plt.title('Logistic Growth Curve Fitting', fontsize=16)

# 将拟合参数显示在图中
param_text = f'$N_0 = {N0_fit:.2f}$\n$r = {r_fit:.4f}$\n$K = {K_fit:.2f}$'
plt.text(0.95, 0.15, param_text, transform=plt.gca().transAxes, 
         fontsize=12, verticalalignment='bottom', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))

plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
```

### 2.2.3.2.线性化后拟合

对于逻辑斯谛方程，我们可以通过变换将其线性化，然后使用线性回归。我们通常没有瞬时变化率 $r$ 的数据，而逻辑斯谛方程可以改写为：

$$
\ln\left(\dfrac{K - N}{N}\right) = \ln\left(\dfrac{K - N_0}{N_0}\right) - r t
$$

如果我们已知 $K$，则可以对 $\ln((K-N)/N)$ 关于 $t$ 进行线性回归得到 $r$。但 $K$ 通常是未知的，虽然可以目测，但如果种群尚未增长到环境容纳量附近，一种常用的方法是**三点法**，即有三个时间间隔相等的种群数量的数据点时，可以用如下公式计算得到 $K$：

$$
K = \frac{N_1^2 (N_0 + N_2) - 2 N_0 N_1 N_2}{N_1^2 - N_0 N_2}
$$

推导如下：设三个等距时间点 $t_0, t_1 = t_0 + \Delta t, t_2 = t_0 + 2\Delta t$ 对应的种群数量为 $N_0, N_1, N_2$。由解的形式可得：
$$
\begin{aligned}
\frac{K - N_0}{N_0} &= c, \\
\frac{K - N_1}{N_1} &= c e^{-r\Delta t}, \\
\frac{K - N_2}{N_2} &= c e^{-2r\Delta t}.
\end{aligned}
$$
消去 $c$ 和 $r$ 得：
$$
\left(\frac{K - N_1}{N_1}\right)^2 = \frac{K - N_0}{N_0} \cdot \frac{K - N_2}{N_2}.
$$
整理后解出 $K$：
$$
K = \frac{N_1^2 (N_0 + N_2) - 2 N_0 N_1 N_2}{N_1^2 - N_0 N_2}.
$$
求得 $K$ 后，代入下式计算 $r$：
$$
r = -\frac{1}{\Delta t} \ln\left( \frac{(K - N_1) N_0}{(K - N_0) N_1} \right).
$$

实际上，直接非线性拟合更为方便可靠，线性化方法可能会引入偏差（因为变换会改变误差结构）。但在某些情况下，线性化可以提供快速的参数估计。

## 思考题

1. （选做）取我们在文档中写下的重整化群变换。你会如何编写程序来数值计算普适函数？

回答可以参考文档中的作图代码。

2. 逻辑斯蒂映射的倍周期分岔与混沌

注：本题中已出现在文档中的部分将不再重新给出回答。

混沌通常与某种非线性动力学相关。我们在文档中已经看到，简单的逻辑斯蒂映射如何导致复杂的动力学行为。动力系统的研究通常关注长期行为（特别是稳态和其他"吸引子"）。我们可以通过改变系统参数 $r$ 来研究逻辑斯蒂映射中混沌的发生。

当处于某些参数范围时，逻辑斯蒂映射为我们提供了一个动力学"不可预测"的例子。在本练习中，我们将通过观察逻辑斯蒂映射在长时间下沿吸引子运动的行为来研究其动力学特性。
- **a)** 固定点与周期 8 吸引子

对于 $r = 0.75$，使用几个初始条件 $x_0$ 迭代映射。最终，所有解都应趋于零（固定点）。在同一图上绘制 $f(x) = rx(1-x)$ 与 $x$ 以及对角线 $y = x$。然后编写一个简短的程序来绘制"蛛网图"，正如我在黑板上的演示。通过多次迭代逻辑斯蒂映射，我们可以找到吸引子上的点。找到一个 $r$ 值，使得吸引子具有周期 8。提交图形（并标出 $r$ 的值）。

**解答：**

可以先尝试采用数值模拟的方式，得到的结果可能对模拟的初值有一定的敏感性：

```python-plot
import numpy as np
import matplotlib.pyplot as plt

def find_attractor_period(r, x0=0.5, n_transient=500, n_iterations=100, tol=1e-20):
    """
    找到给定r值下逻辑斯蒂映射的吸引子周期
    
    参数:
        r: 参数值
        x0: 初始值
        n_transient: 瞬态步数，让系统达到稳态
        n_iterations: 记录迭代步数，用于周期检测
        tol: 容差
    
    返回:
        吸引子的周期
    """
    # 瞬态迭代：让系统达到稳态
    x = x0
    for _ in range(n_transient):
        x = r * x * (1 - x)
    
    # 记录后续迭代
    attractor = np.zeros(n_iterations)
    for i in range(n_iterations):
        x = r * x * (1 - x)
        attractor[i] = x
    
    # 通过检查重复模式寻找周期
    period = 1
    for k in range(2, n_iterations+1):
        # 检查是否存在周期k
        if n_iterations - k + 1 > 0:
            # 比较前n-k+1个元素和后n-k+1个元素（偏移k）
            if np.all(np.abs(attractor[:n_iterations-k] - attractor[k:n_iterations]) < tol):
                period = k
                break
    
    return period

def cobweb_plot(r, x0=0.5, n_iter=50, ax=None):
    """
    绘制逻辑斯蒂映射的蛛网图
    
    参数:
        r: 参数值
        x0: 初始值
        n_iter: 迭代次数
        ax: matplotlib轴对象（可选）
    
    返回:
        ax: matplotlib轴对象
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    
    # 绘制函数曲线
    x = np.linspace(0, 1, 1000)
    f = r * x * (1 - x)
    ax.plot(x, f, 'b-', linewidth=2, label=f'$f(x) = {r}x(1-x)$')
    ax.plot(x, x, 'r--', linewidth=1.5, label='$y=x$')
    
    # 生成蛛网线
    x_vals = [x0]
    y_vals = [0]
    
    # 迭代
    for _ in range(n_iter):
        # 垂直线：从(x_t, x_t)到(x_t, f(x_t))
        x_vals.append(x_vals[-1])
        y_vals.append(r * x_vals[-1] * (1 - x_vals[-1]))
        
        # 水平线：从(x_t, f(x_t))到(f(x_t), f(x_t))
        x_vals.append(y_vals[-1])
        y_vals.append(y_vals[-1])
    
    # 绘制蛛网线
    ax.plot(x_vals, y_vals, 'g-', linewidth=1, alpha=0.7, label='Cobweb')
    
    # 标记起点
    ax.plot(x0, 0, 'go', markersize=8, label=f'Start $x_0={x0}$')
    
    ax.set_xlabel('$x$', fontsize=12)
    ax.set_ylabel('$f(x)$', fontsize=12)
    ax.set_title(f'Cobweb diagram for $r={r:.4f}$', fontsize=14)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    return ax

# 参数设置
r_min = 3.6  # 搜索起始r值
r_max = 3.7  # 搜索结束r值（缩小范围以提高效率）
delta_r = 0.000001  # r的步长
n_transient = 500  # 瞬态步数
n_iterations = 100  # 记录迭代步数
target_period = 8  # 目标周期

# 在r值范围内搜索周期8的吸引子
found = False
optimal_r = None
optimal_period = None

# 搜索r值
for r in np.arange(r_min, r_max + delta_r, delta_r):
    period = find_attractor_period(r, 0.5, n_transient, n_iterations)
    
    # 检查是否找到目标周期
    if period == target_period:
        optimal_r = r
        optimal_period = period
        found = True
        break

# 输出结果
if found:
    print(f"Found r = {optimal_r:.6f} with period-{optimal_period} attractor.")
    
    # 绘制蛛网图
    fig, ax = plt.subplots(figsize=(8, 8))
    cobweb_plot(optimal_r, 0.5, 50, ax)
    
    # 添加周期信息到标题
    ax.set_title(f'Cobweb diagram for $r={optimal_r:.6f}$ (period-{optimal_period})', 
                 fontsize=14)
    
    plt.tight_layout()
    plt.show()
else:
    print(f"No r found with period-{target_period} attractor in the range [{r_min:.2f}, {r_max:.2f}].")
    
    # 可选：绘制周期随r的变化图，帮助理解
    print("\nTrying to understand the period structure...")
    
    # 测试一组r值，查看其周期
    test_r_vals = np.linspace(3.6, 3.7, 100)
    periods = []
    
    for r in test_r_vals:
        period = find_attractor_period(r, 0.5, n_transient, n_iterations)
        periods.append(period)
    
    # 绘制周期图
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(test_r_vals, periods, 'b-', linewidth=2, alpha=0.7)
    ax.set_xlabel('$r$', fontsize=14)
    ax.set_ylabel('Period', fontsize=14)
    ax.set_title(f'Period vs $r$ in range [{r_min:.2f}, {r_max:.2f}]', fontsize=16)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, max(periods) + 2)
    
    # 标记目标周期
    ax.axhline(y=target_period, color='r', linestyle='--', linewidth=1.5, 
               label=f'Target period = {target_period}')
    ax.legend(fontsize=12)
    
    plt.tight_layout()
    plt.show()
```

对于逻辑斯蒂映射 $x_{n+1} = f(x_n) = r x_n (1 - x_n)$，周期8吸引子对应参数 $r$ 使得系统存在稳定的周期8轨道。寻找周期8吸引子可以通过最小化李雅普诺夫指数来实现，因为在周期窗口内，李雅普诺夫指数为负，且在窗口中心达到最小值（最负）。

李雅普诺夫指数定义为：
$$
\lambda(r) = \lim_{n\to\infty} \frac{1}{n} \sum_{i=0}^{n-1} \ln |f'(x_i)|
$$
其中 $f'(x) = r(1 - 2x)$。数值计算时，取充分大的 $n$，并舍弃瞬态过程。

在周期8窗口内，$\lambda(r)$ 为负值，且关于窗口中心对称，在中心处达到最小。因此，在给定区间 $[r_{\min}, r_{\max}]$ 上通过优化算法寻找 $\lambda(r)$ 的最小值点，即可找到周期8窗口中最稳定的参数。查找的区间来源于此前模拟出的经验值，此外再尝试在 $3.6<r<3.65$ 中进行查找，验证此方法的适用性。

```python
import numpy as np
from scipy.optimize import minimize_scalar

def logistic_map(r, x):
    return r * x * (1 - x)

def lyapunov_exponent(r, x0=0.5, n_transient=10000, n_iter=50000):
    """计算逻辑斯蒂映射的李雅普诺夫指数"""
    # 舍弃瞬态
    x = x0
    for _ in range(n_transient):
        x = logistic_map(r, x)
    
    # 计算李雅普诺夫指数
    lyap_sum = 0.0
    for _ in range(n_iter):
        x = logistic_map(r, x)
        df = abs(r * (1 - 2 * x))
        if df > 1e-12:  # 避免log(0)
            lyap_sum += np.log(df)
    return lyap_sum / n_iter

# 在区间 [3.6, 3.65] 内最小化李雅普诺夫指数
res = minimize_scalar(lyapunov_exponent, bounds=(3.6, 3.65), method='bounded')
r_opt = res.x
lyap_opt = res.fun

print(f"最小李雅普诺夫指数对应的 r = {r_opt:.6f}")
print(f"对应的李雅普诺夫指数 λ = {lyap_opt:.6f}")

# 验证周期8：检查最后若干次迭代是否呈现周期8
def check_period(r, x0=0.5, n_transient=10000, n_check=200, tol=1e-8):
    x = x0
    for _ in range(n_transient):
        x = logistic_map(r, x)
    
    # 记录轨迹
    trajectory = []
    for _ in range(n_check):
        x = logistic_map(r, x)
        trajectory.append(x)
    
    # 检查周期，从1到20
    for period in range(1, 21):
        if period < n_check:
            # 检查最后period个点是否与前面period个点一致
            diff = np.array(trajectory[-period:]) - np.array(trajectory[-2*period:-period])
            if np.max(np.abs(diff)) < tol:
                return period
    return None

period = check_period(r_opt)
print(f"在 r = {r_opt:.6f} 处检测到的周期为 {period}")

# 在区间 [3.66, 3.67] 内最小化李雅普诺夫指数
res = minimize_scalar(lyapunov_exponent, bounds=(3.66, 3.67), method='bounded')
r_opt = res.x
lyap_opt = res.fun

print(f"最小李雅普诺夫指数对应的 r = {r_opt:.6f}")
print(f"对应的李雅普诺夫指数 λ = {lyap_opt:.6f}")

period = check_period(r_opt)
print(f"在 r = {r_opt:.6f} 处检测到的周期为 {period}")
```

运行结果：

```
最小李雅普诺夫指数对应的 r = 3.627558
对应的李雅普诺夫指数 λ = -1.765538
在 r = 3.627558 处检测到的周期为 6
最小李雅普诺夫指数对应的 r = 3.662190
对应的李雅普诺夫指数 λ = -0.513869
在 r = 3.662190 处检测到的周期为 8
```

作图进行验证：
```python-plot
import numpy as np
import matplotlib.pyplot as plt

def cobweb_plot(r, x0, n_iter, ax=None, n_skip=0):
    """
    绘制逻辑斯谛映射的蛛网图。
    
    参数:
        r: 增长率
        x0: 初始值
        n_iter: 绘图的迭代次数
        ax: matplotlib轴对象，若为None则创建新图
        n_skip: 绘图前忽略的瞬态迭代次数
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
    
    # 1. 瞬态迭代：不绘图，只更新状态，消除初始 transient
    for _ in range(n_skip):
        x_current = r * x_current * (1 - x_current)
        
    # 2. 稳态迭代：绘图
    for i in range(n_iter):
        y_current = r * x_current * (1 - x_current)
        # 垂直线
        ax.plot([x_current, x_current], [x_current, y_current], 'r-', lw=0.5)
        # 水平线
        ax.plot([x_current, y_current], [y_current, y_current], 'r-', lw=0.5)
        x_current = y_current
    
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('f(x)', fontsize=14)
    ax.set_title(f'Logistic cobweb plot (r = {r}, x0 = {x0})', fontsize=16)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return ax

# 示例：绘制不同r值的蛛网图
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
r_vals = [3.627558, 3.662190]
x0 = 0.3
n_iter = 100  # 增加绘图轮数以展示完整轨迹
n_skip = 1000 # 忽略前1000次迭代，确保进入稳定状态

for i, (r, ax) in enumerate(zip(r_vals, axes.flat)):
    cobweb_plot(r, x0, n_iter, ax, n_skip=n_skip)
    # 标注平衡点（如果存在）
    if r > 1:
        x_eq = 1 - 1/r
        ax.plot(x_eq, x_eq, 'go', markersize=8, label='Equilibrium point')
        ax.legend()

plt.tight_layout()
plt.subplots_adjust(hspace=0.3)
plt.show()
```

- **b)** 稳态解的稳定性与周期 2 解

正如我们在文档中看到的，对于 $r > 3$，稳态解 $x^* = 1 - \frac{1}{r}$ 不再稳定。这可以通过证明导数 $\left|f^{\prime}\left(x^{*}\right)\right| > 1$ 来证明。可选练习：通过观察映射的第二次迭代并检查 $x = f(f(x))$ 的不动点。证明周期 2 解在 $3 < r < 1 + \sqrt{6}$ 时是稳定的。

**解答：**

对于逻辑斯蒂映射 $x_{n+1} = f(x) = r x (1 - x)$，稳态解满足 $x = f(x)$，解得 $x_0^* = 0$ 和 $x_1^* = 1 - 1/r$（当 $r > 1$ 时）。

稳态解的线性稳定性由导数 $f'(x^*) = r(1 - 2x^*)$ 的绝对值决定：
- 对于 $x_0^* = 0$，$f'(0) = r$，故当 $0 < r < 1$ 时稳定，$r > 1$ 时不稳定。
- 对于 $x_1^* = 1 - 1/r$，$f'(x_1^*) = r(1 - 2(1 - 1/r)) = 2 - r$。稳定性条件为 $|2 - r| < 1$，即 $1 < r < 3$。因此当 $r > 3$ 时，稳态解 $x_1^*$ 失稳。

当 $r > 3$ 时，系统出现周期2解，满足 $x = f^{(2)}(x) = f(f(x))$ 且 $x \neq f(x)$。周期2解对应方程 $f^{(2)}(x) - x = 0$ 的两个根（除去 $x_0^*$ 和 $x_1^*$）。记周期2解为 $p$ 和 $q$，满足 $q = f(p)$，$p = f(q)$。

周期2解的稳定性由复合函数 $f^{(2)}$ 在 $p$ 和 $q$ 处的导数乘积决定：
$$
\frac{d}{dx} f^{(2)}(x)\bigg|_{x=p} = f'(f(p)) f'(p) = f'(q) f'(p)
$$
同理在 $q$ 处相同。由于 $f'(x) = r(1 - 2x)$，故稳定性条件为 $|f'(p) f'(q)| < 1$。

通过求解 $f^{(2)}(x) - x = 0$，可得 $p$ 和 $q$ 满足二次方程：
$$
r^2 x^2 - r(r+1) x + (r+1) = 0
$$
利用韦达定理：$p + q = \frac{r+1}{r}$，$pq = \frac{r+1}{r^2}$。计算：
$$
f'(p) f'(q) = r^2 (1 - 2p)(1 - 2q) = r^2 \left[1 - 2(p+q) + 4pq\right] = -r^2 + 2r + 4
$$
稳定性条件 $| -r^2 + 2r + 4 | < 1$ 等价于：
1. $-r^2 + 2r + 4 < 1$ 即 $r^2 - 2r - 3 > 0$，解得 $r > 3$ 或 $r < -1$，结合 $r>0$ 得 $r>3$。
2. $-r^2 + 2r + 4 > -1$ 即 $r^2 - 2r - 5 < 0$，解得 $1 - \sqrt{6} < r < 1 + \sqrt{6}$。

综合得 $3 < r < 1 + \sqrt{6}$。证毕。

选取几个值进行模拟：
```python-plot
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# ========== 第一部分：计算稳态解的导数 ==========
r_values = np.linspace(2, 4, 10000)
derivative = np.zeros_like(r_values)

for i, r in enumerate(r_values):
    if r > 1:
        x_star = 1 - 1/r
        derivative[i] = abs(r * (1 - 2 * x_star))
    else:
        derivative[i] = abs(r)  # 对于r<=1，稳态解为0，导数为r

# 找到导数超过1的r值
unstable_r = r_values[derivative > 1]
if len(unstable_r) > 0:
    print(f'For r > {min(unstable_r):.4f}, the steady-state solution is unstable.')
else:
    print('No unstable solutions found in the given r range.')

# ========== 第二部分：分析二次迭代 f(f(x)) ==========
r_range = np.linspace(3, 1 + np.sqrt(6), 50)
tolerance = 1e-6

# 定义二次迭代函数
def ff_x(r, x):
    """f(f(x)) for logistic map"""
    f_x = r * x * (1 - x)
    return r * f_x * (1 - f_x)

# 用于存储结果的列表
fixed_points_list = []
derivatives_list = []

for r in r_range:
    # 定义方程 f(f(x)) - x = 0
    func = lambda x: ff_x(r, x) - x
    
    # 初始猜测值
    x_guess1, x_guess2 = 0.5, 0.8
    
    # 尝试找到固定点
    fixed_points_ff = []
    try:
        x1 = fsolve(func, x_guess1)[0]
        x2 = fsolve(func, x_guess2)[0]
        
        # 检查这些点是否不是f(x)的固定点
        if (abs(r * x1 * (1 - x1) - x1) > tolerance and 
            abs(r * x2 * (1 - x2) - x2) > tolerance):
            # 确保点在[0,1]区间内
            if 0 <= x1 <= 1:
                fixed_points_ff.append(x1)
            if 0 <= x2 <= 1 and abs(x2 - x1) > 1e-4:
                fixed_points_ff.append(x2)
    except:
        pass
    
    fixed_points_list.append(fixed_points_ff)
    
    # 计算f(f(x))在固定点处的导数
    derivatives_cell = []
    if fixed_points_ff:
        for x_val in fixed_points_ff:
            # f'(f(x)) * f'(x)
            df_dx = r * (1 - 2 * (r * x_val * (1 - x_val))) * r * (1 - 2 * x_val)
            derivatives_cell.append(df_dx)
    
    derivatives_list.append(derivatives_cell)

# ========== 第三部分：创建图形（两个子图横向排列） ==========
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# 子图1：绘制f(f(x))和y=x，以及固定点
ax1 = axes[0]
# 选择几个代表性的r值来绘图（避免图形过于拥挤）
selected_indices = [10, 20, 30, 40]  # 从r_range中选择4个点
colors = ['b', 'g', 'm', 'c']  # 不同曲线的颜色

x_plot = np.linspace(0, 1, 1000)
for idx, color in zip(selected_indices, colors):
    r = r_range[idx]
    ff_plot = ff_x(r, x_plot)
    ax1.plot(x_plot, ff_plot, color=color, linewidth=2, 
             label=f'$r={r:.2f}$', alpha=0.7)
    
    # 绘制固定点（如果存在）
    if fixed_points_list[idx]:
        for point in fixed_points_list[idx]:
            ax1.plot(point, point, 'ko', markersize=8, 
                     markerfacecolor='k', markeredgecolor='w', zorder=5)

# 添加对角线y=x
ax1.plot(x_plot, x_plot, 'r--', linewidth=1.5, alpha=0.5, label='$y=x$')

ax1.set_xlabel('$x$', fontsize=12)
ax1.set_ylabel('$f(f(x))$', fontsize=12)
ax1.set_title('$f(f(x))$ and $y=x$ for selected $r$ values', fontsize=14)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)

# 子图2：绘制周期2解的导数随r的变化
ax2 = axes[1]

# 提取所有r和导数数据点用于绘图
r_plot_points = []
df_plot_points = []

for i, r in enumerate(r_range):
    if derivatives_list[i]:
        for df_dx in derivatives_list[i]:
            r_plot_points.append(r)
            df_plot_points.append(df_dx)

# 绘制导数随r的变化
ax2.plot(r_plot_points, df_plot_points, 'b-', linewidth=2, alpha=0.7)

# 标记稳定区域（|导数|<1）
ax2.axhline(y=1, color='r', linestyle='--', linewidth=1.5, alpha=0.7, label='Stability bounds')
ax2.axhline(y=-1, color='r', linestyle='--', linewidth=1.5, alpha=0.7)

# 填充稳定区域
ax2.fill_between(r_range, -1, 1, alpha=0.2, color='green', label=r'Stable region ($|\lambda|<1$)')

# 标记理论稳定边界
r_stable_upper = 1 + np.sqrt(6)
ax2.axvline(x=3, color='k', linestyle=':', linewidth=1.5, alpha=0.5, label='$r=3$')
ax2.axvline(x=r_stable_upper, color='k', linestyle=':', linewidth=1.5, alpha=0.5, 
            label=fr'$r=1+\sqrt{{6}}\approx{r_stable_upper:.3f}$')

ax2.set_xlabel('$r$', fontsize=12)
ax2.set_ylabel('Derivative of $f(f(x))$ at fixed points', fontsize=12)
ax2.set_title('Stability analysis for period-2 solutions', fontsize=14)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)
ax2.set_xlim(3, r_stable_upper)

# 调整布局并显示图形
plt.tight_layout()
plt.show()
```

- **c)** 分岔图与自相似性
  - 让我们尝试构建逻辑斯蒂映射的分岔图。这里，分岔图是吸引子作为 $r$ 的函数的图，其中 $0 < r < 4$。一种方法是选取均匀间隔的 $\delta r$，运行 $n_{transient}$ 步，记录 $n_{period}$ 步，然后绘制记录的点。开始时使用较小的 $n_{transient}$ 和 $n_{period}$。确保你的 MATLAB 程序正常工作后，可以尝试 $\delta r < 0.01$ 且 $n_{transient}$ 和 $n_{period} > 100$。制作一个图形并提交。
  - 对于 $r = 3.2$，在同一图上绘制 $f(f(x))$ 和对角线 $y = x$。你能看出 $f(x)$ 的周期 2 解变成了 $f(f(x))$ 的一对稳定不动点吗？
  - 将此图与 $r = 2$ 时的 $f(x)$ 进行比较。注意，对于 $f(f(x))$，$x = \frac{1}{2}$ 附近的区域看起来像是 $r = 2$ 时映射的倒置版本。对于 $r = 3.5$，绘制 $f^{(4)}(x)$。注意在 $x = \frac{1}{2}$ 附近的相似映射。事实上，在我们改变 $r$ 以获得倍周期分岔后，单峰映射以缩放形式重新出现，这是每个后续倍周期分岔相互跟随的基本原因。普适性来自于这样一个事实：经过几次倍周期分岔后，这些单峰映射的形状变得与原始映射无关。
- **d)** 正弦映射的分岔图

绘制正弦映射的分岔图：
$$
x_{n + 1} = \mu \sin (\pi x_n)
$$
其中 $0 < \mu < 1$。它看起来与逻辑斯蒂映射的分岔图相似吗？

3. 在实验室中，研究人员对草履虫（*Paramecium caudatum*）种群的增长进行了监测。每隔24小时测量一次种群密度，得到以下数据：

| 时间 t (h)             | 0   | 1    | 2    | 3    | 4    | 5     | 6     | 7     | 8     |
| ---------------------- | --- | ---- | ---- | ---- | ---- | ----- | ----- | ----- | ----- |
| 种群密度 N (个体数/mL) | 9.6 | 18.3 | 29.0 | 47.2 | 71.1 | 119.1 | 174.6 | 257.3 | 350.7 |

| 9     | 10    | 11    | 12    | 13    | 14    | 15    | 16    | 17    | 18    |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 441.0 | 513.3 | 559.7 | 594.8 | 629.4 | 640.9 | 651.1 | 655.9 | 659.6 | 661.8 |

**一、问题描述**

使用以下两种方法拟合逻辑斯谛增长模型，并估计参数 $K$（环境容纳量）、$r$（内禀增长率）和 $N_0$（初始种群密度）：
1. **非线性最小二乘拟合**：直接最小化原始数据的残差平方和。
2. **线性化拟合（三点法）**：使用等间隔三点的数据计算 $K$，然后线性回归得到其他参数。

**二、模型与方法**

**1. 逻辑斯谛增长模型**

逻辑斯谛微分方程及其解析解为：
$$
\frac{dN}{dt} = r N \left(1 - \frac{N}{K}\right), \quad
N(t) = \frac{K}{1 + \left(\dfrac{K - N_0}{N_0}\right) e^{-rt}}.
$$

**2. 拟合方法**

**(1) 非线性最小二乘拟合**
直接使用 `scipy.optimize.curve_fit` 函数拟合 $N(t)$，最小化残差平方和：
$$
\min_{K, r, N_0} \sum_{i=1}^{n} \left[N_i - N(t_i; K, r, N_0)\right]^2.
$$

**(2) 线性化拟合（三点法）**
- **三点法计算 $K$**：选取等间隔的三个时间点 $t_0, t_1 = t_0 + \Delta t, t_2 = t_0 + 2\Delta t$，对应的种群数量为 $N_0, N_1, N_2$。由解析解的性质可得：
$$
K = \frac{N_1^2 (N_0 + N_2) - 2 N_0 N_1 N_2}{N_1^2 - N_0 N_2}.
$$
这里我们选择 $t_0 = 0$（$N_0 = 9.6$），$t_1 = 9$（$N_1 = 441.0$），$t_2 = 18$（$N_2 = 661.8$），$\Delta t = 9$ 小时。

- **线性回归求 $r$ 和 $N_0$**：对变换后的方程进行线性回归：
$$
\ln\left(\frac{K - N}{N}\right) = \ln\left(\frac{K - N_0}{N_0}\right) - r t.
$$
令 $y = \ln\left(\dfrac{K - N}{N}\right)$，则 $y = a - r t$，其中 $a = \ln\left(\dfrac{K - N_0}{N_0}\right)$。通过线性回归得到 $a$ 和 $r$，然后：
$$
N_0 = \frac{K}{1 + e^{a}}.
$$

**三、代码实现与结果**

```python-plot
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress
from sklearn.metrics import r2_score

# 设置英文字体 (Ensure English fonts are used/available)
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 实验数据
t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
N = np.array([9.6, 18.3, 29.0, 47.2, 71.1, 119.1, 174.6, 257.3, 350.7, 
              441.0, 513.3, 559.7, 594.8, 629.4, 640.9, 651.1, 655.9, 659.6, 661.8])

# ====================== 方法1：非线性最小二乘拟合 ======================
def logistic_model(t, K, r, N0):
    return K / (1 + ((K - N0) / N0) * np.exp(-r * t))

# 初始参数猜测（K ≈ 660, r ≈ 0.5, N0 ≈ 10）
initial_guess = [660, 0.5, 10]
params_nonlin, cov_nonlin = curve_fit(logistic_model, t, N, p0=initial_guess, maxfev=5000)
K_nonlin, r_nonlin, N0_nonlin = params_nonlin
# 计算参数的标准误差
params_err_nonlin = np.sqrt(np.diag(cov_nonlin))

# 计算预测值和拟合优度
N_pred_nonlin = logistic_model(t, K_nonlin, r_nonlin, N0_nonlin)
SSE_nonlin = np.sum((N - N_pred_nonlin)**2)
R2_nonlin = r2_score(N, N_pred_nonlin)
RMSE_nonlin = np.sqrt(SSE_nonlin / len(N))

# ====================== 方法2：线性化拟合（三点法） ======================
# 选择三个等间隔的点：t=0, t=9, t=18
idx0, idx1, idx2 = 0, 9, 18
N0_data, N1_data, N2_data = N[idx0], N[idx1], N[idx2]
Δt = t[idx1] - t[idx0]

# 三点法计算K
K_linear = (N1_data**2 * (N0_data + N2_data) - 2 * N0_data * N1_data * N2_data) / (N1_data**2 - N0_data * N2_data)

# 线性回归求 r 和 N0
# 注意：当 N 接近 K 时，(K-N)/N 可能为负或零，这里仅使用 N < K 的数据点进行回归
valid_mask = N < K_linear * 0.999  # 避免对数中出现非正数
t_valid = t[valid_mask]
N_valid = N[valid_mask]

# 计算 y = ln((K-N)/N)
y = np.log((K_linear - N_valid) / N_valid)

# 线性回归：y = a - r*t
slope, intercept, r_value, p_value, std_err = linregress(t_valid, y)
r_linear = -slope
a = intercept
# 计算 N0
N0_linear = K_linear / (1 + np.exp(a))

# 计算预测值和拟合优度
N_pred_linear = logistic_model(t, K_linear, r_linear, N0_linear)
SSE_linear = np.sum((N - N_pred_linear)**2)
R2_linear = r2_score(N, N_pred_linear)
RMSE_linear = np.sqrt(SSE_linear / len(N))

# ====================== 可视化 ======================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. 原始数据和拟合曲线
ax1 = axes[0, 0]
ax1.scatter(t, N, color='black', s=50, label='Observed Data', zorder=5)
t_fine = np.linspace(0, 20, 200)
ax1.plot(t_fine, logistic_model(t_fine, K_nonlin, r_nonlin, N0_nonlin), 
         'r-', linewidth=2, label='Non-linear Fit', alpha=0.8)
ax1.plot(t_fine, logistic_model(t_fine, K_linear, r_linear, N0_linear), 
         'b--', linewidth=2, label='Linearized Fit', alpha=0.8)
ax1.set_xlabel('Time t (h)', fontsize=12)
ax1.set_ylabel('Population Density N (ind./mL)', fontsize=12)
ax1.set_title('Logistic Model Fit of Paramecium Population Growth', fontsize=14)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# 2. 残差图
ax2 = axes[0, 1]
residuals_nonlin = N - N_pred_nonlin
residuals_linear = N - N_pred_linear
ax2.scatter(t, residuals_nonlin, color='red', s=40, alpha=0.7, label='Non-linear Fit Residuals')
ax2.scatter(t, residuals_linear, color='blue', s=40, alpha=0.7, label='Linearized Fit Residuals')
ax2.axhline(y=0, color='black', linestyle='--', alpha=0.5)
ax2.set_xlabel('Time t (h)', fontsize=12)
ax2.set_ylabel('Residuals', fontsize=12)
ax2.set_title('Residual Comparison', fontsize=14)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

# 3. 线性化拟合过程
ax3 = axes[1, 0]
ax3.scatter(t_valid, y, color='blue', s=40, label='Linearized Data')
# 绘制回归线
y_fit = intercept + slope * t_valid
ax3.plot(t_valid, y_fit, 'r-', linewidth=2, label=f'Linear Regression: y = {intercept:.3f} - {r_linear:.3f}t')
ax3.set_xlabel('Time t (h)', fontsize=12)
ax3.set_ylabel('ln((K-N)/N)', fontsize=12)
ax3.set_title(f'Linearization Process (3-point method K = {K_linear:.1f})', fontsize=14)
ax3.legend(fontsize=10)
ax3.grid(True, alpha=0.3)

# 4. 拟合优度统计
ax4 = axes[1, 1]
methods = ['Non-linear Fit', 'Linearized Fit']
SSE_values = [SSE_nonlin, SSE_linear]
R2_values = [R2_nonlin, R2_linear]
x = np.arange(len(methods))
width = 0.35

# Plot SSE on primary y-axis
bar1 = ax4.bar(x - width/2, SSE_values, width, label='SSE', color='skyblue')
ax4.set_xlabel('Fitting Method', fontsize=12)
ax4.set_ylabel('SSE', fontsize=12, color='steelblue')
ax4.tick_params(axis='y', labelcolor='steelblue')
ax4.set_title('Goodness of Fit Comparison', fontsize=14)
ax4.set_xticks(x)
ax4.set_xticklabels(methods)

# Plot R2 on secondary y-axis
ax4_twin = ax4.twinx()
bar2 = ax4_twin.bar(x + width/2, R2_values, width, label='R²', color='lightcoral')
ax4_twin.set_ylabel('R²', fontsize=12, color='indianred')
ax4_twin.set_ylim(0, 1.1)  # R² is usually <= 1
ax4_twin.tick_params(axis='y', labelcolor='indianred')

# Add legends
lines1, labels1 = [bar1], ['SSE']
lines2, labels2 = [bar2], ['R²']
ax4.legend(lines1 + lines2, labels1 + labels2, loc='upper center', fontsize=10)

ax4.grid(True, alpha=0.3, axis='y')

# 在柱状图上添加数值
for i, sse in enumerate(SSE_values):
    ax4.text(i - width/2, sse + max(SSE_values)*0.01, f'{sse:.1f}', 
             ha='center', va='bottom', fontsize=9, color='steelblue')

for i, r2 in enumerate(R2_values):
    ax4_twin.text(i + width/2, r2 + 0.01, f'{r2:.4f}', 
             ha='center', va='bottom', fontsize=9, color='indianred')

plt.tight_layout()
plt.show()
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress
from sklearn.metrics import r2_score

# 实验数据
t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
N = np.array([9.6, 18.3, 29.0, 47.2, 71.1, 119.1, 174.6, 257.3, 350.7, 
              441.0, 513.3, 559.7, 594.8, 629.4, 640.9, 651.1, 655.9, 659.6, 661.8])

# ====================== 方法1：非线性最小二乘拟合 ======================
def logistic_model(t, K, r, N0):
    """逻辑斯谛增长模型"""
    return K / (1 + ((K - N0) / N0) * np.exp(-r * t))

# 初始参数猜测（K ≈ 660, r ≈ 0.5, N0 ≈ 10）
initial_guess = [660, 0.5, 10]
params_nonlin, cov_nonlin = curve_fit(logistic_model, t, N, p0=initial_guess, maxfev=5000)
K_nonlin, r_nonlin, N0_nonlin = params_nonlin
# 计算参数的标准误差
params_err_nonlin = np.sqrt(np.diag(cov_nonlin))

# 计算预测值和拟合优度
N_pred_nonlin = logistic_model(t, K_nonlin, r_nonlin, N0_nonlin)
SSE_nonlin = np.sum((N - N_pred_nonlin)**2)
R2_nonlin = r2_score(N, N_pred_nonlin)
RMSE_nonlin = np.sqrt(SSE_nonlin / len(N))

# ====================== 方法2：线性化拟合（三点法） ======================
# 选择三个等间隔的点：t=0, t=9, t=18
idx0, idx1, idx2 = 0, 9, 18
N0_data, N1_data, N2_data = N[idx0], N[idx1], N[idx2]
Δt = t[idx1] - t[idx0]

# 三点法计算K
K_linear = (N1_data**2 * (N0_data + N2_data) - 2 * N0_data * N1_data * N2_data) / (N1_data**2 - N0_data * N2_data)
print(f"三点法计算的 K = {K_linear:.2f}")

# 线性回归求 r 和 N0
# 注意：当 N 接近 K 时，(K-N)/N 可能为负或零，这里仅使用 N < K 的数据点进行回归
valid_mask = N < K_linear * 0.999  # 避免对数中出现非正数
t_valid = t[valid_mask]
N_valid = N[valid_mask]

# 计算 y = ln((K-N)/N)
y = np.log((K_linear - N_valid) / N_valid)

# 线性回归：y = a - r*t
slope, intercept, r_value, p_value, std_err = linregress(t_valid, y)
r_linear = -slope
a = intercept
# 计算 N0
N0_linear = K_linear / (1 + np.exp(a))

# 计算预测值和拟合优度
N_pred_linear = logistic_model(t, K_linear, r_linear, N0_linear)
SSE_linear = np.sum((N - N_pred_linear)**2)
R2_linear = r2_score(N, N_pred_linear)
RMSE_linear = np.sqrt(SSE_linear / len(N))

# ====================== 结果输出 ======================
print("=" * 60)
print("非线性最小二乘拟合结果：")
print(f"  K = {K_nonlin:.2f} ± {params_err_nonlin[0]:.2f}")
print(f"  r = {r_nonlin:.4f} ± {params_err_nonlin[1]:.4f}")
print(f"  N0 = {N0_nonlin:.2f} ± {params_err_nonlin[2]:.2f}")
print(f"  SSE = {SSE_nonlin:.2f}, R² = {R2_nonlin:.6f}, RMSE = {RMSE_nonlin:.2f}")

print("\n" + "=" * 60)
print("线性化拟合（三点法）结果：")
print(f"  K = {K_linear:.2f} (由三点法直接计算)")
print(f"  r = {r_linear:.4f}")
print(f"  N0 = {N0_linear:.2f}")
print(f"  SSE = {SSE_linear:.2f}, R² = {R2_linear:.6f}, RMSE = {RMSE_linear:.2f}")

print("\n" + "=" * 60)
print("拟合效果比较：")
print(f"  非线性拟合SSE减少：{((SSE_linear - SSE_nonlin) / SSE_linear * 100):.2f}%")
print(f"  非线性拟合R²提高：{((R2_nonlin - R2_linear) * 100):.4f}%")
```

运行结果：

```
三点法计算的 K = 664.29
============================================================
非线性最小二乘拟合结果：
  K = 663.04 ± 1.70
  r = 0.5470 ± 0.0056
  N0 = 9.14 ± 0.38
  SSE = 194.23, R² = 0.999846, RMSE = 3.20

============================================================
线性化拟合结果：
  K = 664.29 (由三点法直接计算)
  r = 0.5386
  N0 = 9.79
  SSE = 231.70, R² = 0.999816, RMSE = 3.49

============================================================
拟合效果比较：
  非线性拟合SSE减少：16.18%
  非线性拟合R²提高：0.0030%
```

我们得到以下拟合结果：

**1. 非线性最小二乘拟合**
- $K = 663.04 \pm 1.70$（个体/mL）
- $r = 0.5470 \pm 0.0056$（/小时）
- $N_0 = 9.14 \pm 0.38$（个体/mL）
- $SSE = 194.23$，$R^2 = 0.999846$，$RMSE = 3.20$

**2. 线性化拟合**
- $K = 664.29$（个体/mL）（由三点法直接计算）
- $r = 0.5386$（/小时）
- $N_0 = 9.79$（个体/mL）
- $SSE = 231.70$，$R^2 = 0.999816$，$RMSE = 3.49$

**3. 拟合效果比较**
- 非线性拟合的 $SSE$ 比线性化拟合低 **16.18%**，$R^2$ 提高 **0.003%**。
- 从残差图可以看出，非线性拟合的残差略小，分布较随机，而线性化拟合在中段存在一定系统偏差。

**五、讨论与总结**

1. **参数估计的准确性**：
   - 非线性最小二乘拟合直接最小化原始数据的残差，通常更准确可靠，特别是当数据存在测量误差时。
   - 三点法对所选数据点较为敏感，如果选取的点受噪声影响较大，$K$ 的估计会产生较大偏差。本例中三点法得到的 $K$ 与非线性拟合相近，但 $r$ 和 $N_0$ 略有差异。

2. **方法适用性**：
   - **非线性拟合**：适用于具有完整增长曲线的数据，能够充分利用所有数据点信息，但需要较好的初始猜测。
   - **线性化拟合（+三点法）**：计算简单，适用于快速估算，但精度较低，且要求数据点等间隔、噪声小。

3. **生物学意义**：
   - 两种方法得到的 $K$ 均约为 660 个体/mL，表明培养环境的最大容纳量约为 660 个体/mL。
   - 内禀增长率 $r$ 约为 0.54/小时，意味着在无密度制约下，种群每小时增加约 54%。
   - 初始密度 $N_0$ 约为 9 个体/mL，与实验起始值一致。

**结论**：对于草履虫种群增长数据，非线性最小二乘拟合在统计指标上略优于线性化拟合，但线性拟合具有其便利性，可作为快速估算的辅助手段。