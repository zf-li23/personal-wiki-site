**内容**：ODE的建立；数值求解（欧拉法，`scipy.integrate.odeint`）；相图与相轨迹的几何直观。

在前两节中，我们分别探讨了离散时间系统（Leslie矩阵、逻辑斯谛映射）和连续时间系统（逻辑斯谛增长）。这些模型都描述了生物系统中的动态行为。本节将进一步深入**连续时间动力系统**，重点介绍常微分方程（ODE）模型的建立、分析与可视化方法。我们将以生态学中的经典模型——Lotka-Volterra竞争模型和捕食者-猎物模型为例，展示ODE建模的全过程。

## 2.3.1. 常微分方程基本理论

### 2.3.1.1. 常微分方程的基本概念

常微分方程（Ordinary Differential Equations, ODEs）是描述系统状态随时间变化规律的数学工具。

**定义**：形如
$$
\frac{dx}{dt} = f(x, t)
$$
的方程称为一阶常微分方程，其中$x(t)$是未知函数，$f(x,t)$是已知函数。

**自治系统**：当$f$不显式依赖于时间$t$时，即
$$
\frac{dx}{dt} = f(x)
$$
称为自治系统。这是生态模型中常见的形式，反映了系统动态仅由当前状态决定。

**高阶系统**：对于多变量系统，我们有方程组
$$
\begin{cases}
\frac{dx_1}{dt} &= f_1(x_1, x_2, \ldots, x_n) \\
\frac{dx_2}{dt} &= f_2(x_1, x_2, \ldots, x_n) \\
&\vdots \\
\frac{dx_n}{dt} &= f_n(x_1, x_2, \ldots, x_n)
\end{cases}
$$

### 2.3.1.2. 平衡点与稳定性

**平衡点（Equilibrium）**：满足$f(x^*) = 0$的状态$x^*$称为平衡点，系统一旦达到该状态将保持不变。

**稳定性分析**：
1. **线性稳定性理论**：在平衡点$x^*$附近线性化系统
   $$
   \frac{d(\delta x)}{dt} = J(x^*) \delta x
   $$
   其中$J(x^*)$是雅可比矩阵$J_{ij} = \frac{\partial f_i}{\partial x_j}\big|_{x=x^*}$

2. **特征值判据**：对于二维系统$J = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$，特征值满足
   $$
   \lambda^2 - \text{tr}(J)\lambda + \det(J) = 0
   $$
   其中$\text{tr}(J) = a+d$，$\det(J) = ad-bc$

3. **稳定性分类**：
   - 稳定结点：$\lambda_1, \lambda_2 < 0$（实数）
   - 不稳定结点：$\lambda_1, \lambda_2 > 0$（实数）
   - 鞍点：$\lambda_1 < 0 < \lambda_2$（实数）
   - 稳定焦点：$\text{Re}(\lambda_{1,2}) < 0$（复数）
   - 不稳定焦点：$\text{Re}(\lambda_{1,2}) > 0$（复数）
   - 中心：$\text{Re}(\lambda_{1,2}) = 0$（纯虚数）

### 2.3.1.3. 数值求解方法

#### 2.3.1.3.1. 欧拉法（Euler Method）
最简单的显式数值方法：
$$
x_{n+1} = x_n + h f(x_n, t_n)
$$
其中$h$为步长。全局误差$O(h)$，条件稳定。

#### 2.3.1.3.2. 龙格-库塔法（Runge-Kutta Methods）
**二阶（改进欧拉法/Heun方法）**：
$$
\begin{aligned}
k_1 &= h f(x_n, t_n) \\
k_2 &= h f(x_n + k_1, t_n + h) \\
x_{n+1} &= x_n + \frac{1}{2}(k_1 + k_2)
\end{aligned}
$$
全局误差$O(h^2)$。

**四阶经典RK方法**：
$$
\begin{aligned}
k_1 &= h f(x_n, t_n) \\
k_2 &= h f(x_n + \frac{k_1}{2}, t_n + \frac{h}{2}) \\
k_3 &= h f(x_n + \frac{k_2}{2}, t_n + \frac{h}{2}) \\
k_4 &= h f(x_n + k_3, t_n + h) \\
x_{n+1} &= x_n + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)
\end{aligned}
$$
全局误差$O(h^4)$，广泛应用于科学计算。

#### 2.3.1.3.3. `scipy.integrate`模块
Python中常用的ODE求解器：
- `odeint`: 基于LSODA算法的通用求解器
- `solve_ivp`: 更灵活的接口，支持多种方法（RK45, RK23, BDF等）

### 2.3.1.4. 相图与相轨迹

**相空间**：以状态变量为坐标轴构成的空间。对于二维系统，相平面为$(x,y)$平面。

**向量场**：在每个点$(x,y)$处，向量$(f_1(x,y), f_2(x,y))$表示状态变化的方向和速率。

**轨迹（Trajectory）**：系统状态随时间在相空间中描绘的曲线，满足
$$
\frac{d}{dt} \begin{pmatrix} x(t) \\ y(t) \end{pmatrix} = \begin{pmatrix} f_1(x,y) \\ f_2(x,y) \end{pmatrix}
$$

**零增长线（Nullclines）**：满足$dx/dt=0$或$dy/dt=0$的曲线。零增长线的交点即为平衡点。

## 2.3.2. Lotka-Volterra种间竞争模型

### 2.3.2.1. 模型推导与归一化

在真实生态系统中，物种很少孤立存在，它们为有限资源而竞争。Lotka-Volterra竞争模型扩展了单物种逻辑斯谛增长，描述了两个物种竞争同一资源时的动态变化。

假设两个物种的种群数量分别为$N_1(t)$和$N_2(t)$。每个物种单独存在时遵循逻辑斯谛增长：

$$
\begin{split}
\frac{dN_1}{dt} &= r_1 N_1 \left(1 - \frac{N_1}{K_1}\right) \\
\frac{dN_2}{dt} &= r_2 N_2 \left(1 - \frac{N_2}{K_2}\right)
\end{split}
$$

其中$r_i$为物种$i$的内禀增长率，$K_i$为其环境容纳量。

当两个物种共存时，它们相互竞争资源。竞争效应通过**竞争系数**$\alpha_{12}$和$\alpha_{21}$量化：
- $\alpha_{12}$：每个$N_2$个体对物种1增长的抑制效应，相当于$\alpha_{12}$个$N_1$个体。
- $\alpha_{21}$：每个$N_1$个体对物种2增长的抑制效应，相当于$\alpha_{21}$个$N_2$个体。

完整的竞争模型为：

$$
\begin{aligned}
\frac{dN_1}{dt} &= r_1 N_1 \left(1 - \frac{N_1}{K_1} - \frac{\alpha_{12} N_2}{K_1}\right) \\
\frac{dN_2}{dt} &= r_2 N_2 \left(1 - \frac{N_2}{K_2} - \frac{\alpha_{21} N_1}{K_2}\right)
\end{aligned}
$$

为了简化分析，我们引入无量纲变量：

$$
x = \frac{N_1}{K_1}, \quad y = \frac{N_2}{K_2}, \quad \tau = r_1 t
$$

并定义：

$$
a = \alpha_{12}\frac{K_2}{K_1}, \quad b = \alpha_{21}\frac{K_1}{K_2}, \quad \rho = \frac{r_2}{r_1}
$$

则系统简化为：

$$
\begin{aligned}
\frac{dx}{d\tau} &= x(1 - x - a y) \\
\frac{dy}{d\tau} &= \rho y(1 - y - b x)
\end{aligned}
$$

### 2.3.2.2. 平衡点与零增长线分析

**零增长线**（nullcline）是相平面中满足$\frac{dx}{d\tau} = 0$或$\frac{dy}{d\tau} = 0$的曲线：

1. $x$-零增长线：$\frac{dx}{d\tau} = 0 \Rightarrow x = 0$或$y = \frac{1-x}{a}$
2. $y$-零增长线：$\frac{dy}{d\tau} = 0 \Rightarrow y = 0$或$y = 1 - b x$

这些直线将相平面划分为不同区域，在每个区域内，$x$和$y$的变化方向是确定的。

**平衡点**（equilibrium）是系统不再变化的状态，即同时满足$\frac{dx}{d\tau} = 0$和$\frac{dy}{d\tau} = 0$的点：

1. $(0,0)$：两个物种灭绝
2. $(1,0)$：物种1达到最大容量，物种2灭绝
3. $(0,1)$：物种2达到最大容量，物种1灭绝
4. $\left(\frac{1-a}{1-ab}, \frac{1-b}{1-ab}\right)$：共存平衡点（要求$0 < \frac{1-a}{1-ab} < 1$且$0 < \frac{1-b}{1-ab} < 1$）

### 2.3.2.3. 四种竞争结果及其普适规律

竞争模型的长期行为由参数$a$和$b$的相对大小决定，产生四种可能结果：

```python-plot
"""
competition_phase_diagrams.py
绘制Lotka-Volterra竞争模型的四种结果的原理图
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_competition_schematic(a, b, case_name, ax):
    """绘制竞争模型原理图，标注关键阈值"""
    
    # 设置坐标轴范围
    x_max = max(1.5, 1.2 * max(1, 1/b if b > 0 else 0))
    y_max = max(1.5, 1.2 * max(1, 1/a if a > 0 else 0))
    
    # 绘制坐标轴
    ax.set_xlim(0, x_max)
    ax.set_ylim(0, y_max)
    
    # 去除坐标轴数字标注
    ax.set_xticks([])
    ax.set_yticks([])
    
    # 绘制零增长线
    # 物种1零增长线: x=0 或 y=(1-x)/a
    if a > 0:
        x_vals = np.linspace(0, x_max, 100)
        y_xnull = (1 - x_vals) / a
        valid = (y_xnull >= 0) & (y_xnull <= y_max)
        ax.plot(x_vals[valid], y_xnull[valid], 'r-', linewidth=2, label='$dx/dτ=0$')
    
    # 物种2零增长线: y=0 或 y=1-bx
    x_vals = np.linspace(0, x_max, 100)
    y_ynull = 1 - b * x_vals
    valid = (y_ynull >= 0) & (y_ynull <= y_max)
    ax.plot(x_vals[valid], y_ynull[valid], 'b-', linewidth=2, label='$dy/dτ=0$')
    
    # 标注关键点
    # (1, 0) - 物种1最大容量
    ax.plot(1, 0, 'ko', markersize=8)
    # 改为内侧标注 va='bottom'
    ax.text(1, 0.02*y_max, '$K_1$', ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    # (0, 1) - 物种2最大容量
    ax.plot(0, 1, 'ko', markersize=8)
    # 改为内侧标注 ha='left'
    ax.text(0.02*x_max, 1, '$K_2$', ha='left', va='center', fontsize=12, fontweight='bold')
    
    # 零增长线与坐标轴的交点
    # 物种1零增长线与y轴交点: (0, 1/a)
    if a > 0:
        ax.plot(0, 1/a, 'ro', markersize=6)
        # 改为内侧标注 ha='left'
        ax.text(0.02*x_max, 1/a, '$K_1/α$', ha='left', va='center', fontsize=12, color='red', fontweight='bold')
    
    # 物种2零增长线与x轴交点: (1/b, 0)
    if b > 0:
        ax.plot(1/b, 0, 'bo', markersize=6)
        # 改为内侧标注 va='bottom'
        ax.text(1/b, 0.02*y_max, '$K_2/β$', ha='center', va='bottom', fontsize=12, color='blue', fontweight='bold')
    
    # 标注共存平衡点（如果存在）
    denominator = 1 - a * b
    if abs(denominator) > 1e-10:
        x_star = (1 - a) / denominator
        y_star = (1 - b) / denominator
        
        if 0 <= x_star <= x_max and 0 <= y_star <= y_max:
            # 根据稳定性标注不同符号
            # 计算雅可比矩阵的特征值
            J11 = 1 - 2*x_star - a*y_star
            J12 = -a * x_star
            J21 = -b * y_star  # 注意：这里假设ρ=1
            J22 = 1 - 2*y_star - b*x_star
            
            # 特征值实部
            trace = J11 + J22
            det = J11 * J22 - J12 * J21
            
            # 判断稳定性
            if det > 0 and trace < 0:
                # 稳定节点或焦点
                ax.plot(x_star, y_star, 'go', markersize=10, markeredgecolor='black', markeredgewidth=1)
                ax.text(x_star+0.02*x_max, y_star+0.02*y_max, 'Stable', fontsize=10, color='green')
            elif det < 0:
                # 鞍点
                ax.plot(x_star, y_star, 'yo', markersize=10, markeredgecolor='black', markeredgewidth=1)
                ax.text(x_star+0.02*x_max, y_star+0.02*y_max, 'Saddle', fontsize=10, color='orange')
            else:
                ax.plot(x_star, y_star, 'ko', markersize=10)
    
    # 添加向量场方向指示 (铺满全图的相图箭头)
    nx, ny = 20, 20
    x_grid = np.linspace(0, x_max, nx)
    y_grid = np.linspace(0, y_max, ny)
    X, Y = np.meshgrid(x_grid, y_grid)
    
    # 竞争模型微分方程 (简化版 r1=r2=1)
    # dx/dt = x(1 - x - ay)
    # dy/dt = y(1 - y - bx)
    U = X * (1 - X - a * Y)
    V = Y * (1 - Y - b * X)
    
    # 归一化箭头长度以便观看
    N = np.sqrt(U**2 + V**2)
    # 避免除以零
    N[N==0] = 1
    U = U / N
    V = V / N
    
    # 绘制箭头
    ax.quiver(X, Y, U, V, color='gray', alpha=0.3, width=0.003, scale=30, headwidth=4)
    
    # 设置标题和标签
    ax.set_xlabel('Species 1 (x = $N_1/K_1$)', fontsize=12)
    ax.set_ylabel('Species 2 (y = $N_2/K_2$)', fontsize=12)
    ax.set_title(f'{case_name}\na = {a}, b = {b}', fontsize=14)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(fontsize=10, loc='upper right')
    
    # 添加文本说明
    conditions_text = f'Conditions:\n'
    if a < 1 and b > 1:
        conditions_text += '$K_1 > K_2/β$\n$K_2 < K_1/α$'
    elif a > 1 and b < 1:
        conditions_text += '$K_2 > K_1/α$\n$K_1 < K_2/β$'
    elif a < 1 and b < 1:
        conditions_text += '$K_1 < K_2/β$\n$K_2 < K_1/α$'
    elif a > 1 and b > 1:
        conditions_text += '$K_1 > K_2/β$\n$K_2 > K_1/α$'
    
    ax.text(0.02, 0.98, conditions_text, transform=ax.transAxes,
           fontsize=10, verticalalignment='top',
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# 创建四种情况的示意图
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Case 1: 物种1获胜 (a < 1, b > 1)
plot_competition_schematic(a=0.5, b=1.5, 
                          case_name='(a) Species 1 wins', 
                          ax=axes[0, 0])

# Case 2: 物种2获胜 (a > 1, b < 1)
plot_competition_schematic(a=1.5, b=0.5, 
                          case_name='(b) Species 2 wins', 
                          ax=axes[0, 1])

# Case 3: 不稳定共存 (a > 1, b > 1)
plot_competition_schematic(a=1.5, b=1.5, 
                          case_name='(c) Unstable coexistence', 
                          ax=axes[1, 0])

# Case 4: 稳定共存 (a < 1, b < 1)
plot_competition_schematic(a=0.5, b=0.5, 
                          case_name='(d) Stable coexistence', 
                          ax=axes[1, 1])

# 调整子图间距，增加高度方向的间距(h_pad)
plt.tight_layout(h_pad=3.0)
# plt.savefig('competition_four_cases_schematic.png', dpi=300, bbox_inches='tight')
plt.show()
```

**运行结果说明**：上述代码生成的原理图清晰地展示了Lotka-Volterra竞争模型的四种可能结果。每个子图中：

1. 红色实线表示物种1的零增长线($dx/dτ=0$)，蓝色实线表示物种2的零增长线($dy/dτ=0$)
2. 关键点标注包括：
   - $K_1$: 物种1单独存在时的最大容量
   - $K_2$: 物种2单独存在时的最大容量
   - $K_1/α$: 物种1零增长线与y轴的交点
   - $K_2/β$: 物种2零增长线与x轴的交点
3. 箭头指示了相平面不同区域的向量场方向
4. 文本框显示了每种情况对应的参数条件

这四种结果可以总结为：

1. **物种1获胜**：当$K_1 > K_2/β$且$K_2 < K_1/α$（$a<1$且$b>1$）时，物种2无法在竞争中生存
2. **物种2获胜**：当$K_2 > K_1/α$且$K_1 < K_2/β$（$a>1$且$b<1$）时，物种1无法在竞争中生存
3. **不稳定共存**：当$K_1 > K_2/β$且$K_2 > K_1/α$（$a>1$且$b>1$）时，初始条件决定最终获胜者
4. **稳定共存**：当$K_1 < K_2/β$且$K_2 < K_1/α$（$a<1$且$b<1$）时，两个物种可以长期共存

### 2.3.2.4. 竞争系数的生物学意义

竞争系数 $a$ 和 $b$ 反映了物种间的竞争强度：
- 当 $a < 1$ 时，种内竞争强于种间竞争，物种1对自身的影响大于物种2对它的影响
- 当 $α > 1$ 时，种间竞争强于种内竞争，物种2对物种1的影响大于物种1对自身的影响
- $b$ 的意义与 $a$ 类似，但表示物种1对物种2的影响

竞争结果取决于相对竞争强度而非绝对数值。这种相对性体现了生态位理论的核心思想：生态位重叠越小（竞争系数越小），共存的可能性越大。

### 2.3.2.5. 稳定性分析

平衡点的稳定性通过**雅可比矩阵**的特征值分析。对于二维系统，雅可比矩阵 $J$ 在平衡点 $(N_1^*, N_2^*)$ 处的特征值 $\lambda$ 满足特征方程：
$$
\det(J - \lambda I) = 0
$$
稳定性判据：
- 若两个特征值的实部均小于零，平衡点是**稳定**的（吸引子）。
- 若有特征值的实部大于零，平衡点是**不稳定**的。
- 若特征值为纯虚数，平衡点可能是**中心**（中性稳定）。

对于竞争模型，雅可比矩阵得到的四种可能的结果与前述方法得到的相同：
1. **物种1获胜**：$K_1 > K_2/\beta$ 且 $K_2 < K_1/\alpha$
2. **物种2获胜**：$K_2 > K_1/\alpha$ 且 $K_1 < K_2/\beta$
3. **不稳定共存**：$K_1 > K_2/\beta$ 且 $K_2 > K_1/\alpha$
4. **稳定共存**：$K_1 < K_2/\beta$ 且 $K_2 < K_1/\alpha$

四种情况的数值模拟：

```python-plot
"""
lotka_volterra_competition.py
Complete analysis of Lotka-Volterra competition model
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

class CompetitionModel:
    """Lotka-Volterra competition model with dimensionless variables"""
    
    def __init__(self, a=0.4, b=0.6, rho=1.0):
        """
        Initialize competition model
        
        Parameters:
        -----------
        a : float
            Effect of species 2 on species 1 (normalized)
        b : float
            Effect of species 1 on species 2 (normalized)
        rho : float
            Relative growth rate (r2/r1)
        """
        self.a = a
        self.b = b
        self.rho = rho
        
        # Calculate equilibria
        self.equilibria = self.calculate_equilibria()
    
    def equations(self, t, state):
        """Define the ODE system"""
        x, y = state
        dxdt = x * (1 - x - self.a * y)
        dydt = self.rho * y * (1 - y - self.b * x)
        return [dxdt, dydt]
    
    def jacobian(self, x, y):
        """Calculate Jacobian matrix at point (x, y)"""
        J11 = 1 - 2*x - self.a*y
        J12 = -self.a * x
        J21 = -self.rho * self.b * y
        J22 = self.rho * (1 - 2*y - self.b * x)
        return np.array([[J11, J12], [J21, J22]])
    
    def calculate_equilibria(self):
        """Calculate all equilibrium points"""
        eq_points = []
        
        # (0, 0)
        eq_points.append((0.0, 0.0))
        
        # (1, 0)
        eq_points.append((1.0, 0.0))
        
        # (0, 1)
        eq_points.append((0.0, 1.0))
        
        # Coexistence point
        denominator = 1 - self.a * self.b
        if abs(denominator) > 1e-10:
            x_star = (1 - self.a) / denominator
            y_star = (1 - self.b) / denominator
            if 0 <= x_star <= 1 and 0 <= y_star <= 1:
                eq_points.append((x_star, y_star))
        
        return eq_points
    
    def analyze_equilibrium(self, eq_point):
        """Analyze stability of an equilibrium point"""
        x, y = eq_point
        J = self.jacobian(x, y)
        eigvals, eigvecs = np.linalg.eig(J)
        
        # Classify stability
        real_parts = np.real(eigvals)
        
        if all(real_parts < 0):
            stability = "stable"
        elif any(real_parts > 0):
            stability = "unstable"
        else:
            # All real parts <= 0, some may be zero
            stability = "marginally stable"
        
        # Classify type
        if np.all(np.isreal(eigvals)):
            if stability == "stable":
                eq_type = "stable node"
            elif stability == "unstable":
                if eigvals[0] * eigvals[1] < 0:
                    eq_type = "saddle"
                else:
                    eq_type = "unstable node"
            else:
                eq_type = "degenerate"
        else:
            if stability == "stable":
                eq_type = "stable focus"
            elif stability == "unstable":
                eq_type = "unstable focus"
            else:
                eq_type = "center"
        
        return {
            'point': eq_point,
            'jacobian': J,
            'eigenvalues': eigvals,
            'eigenvectors': eigvecs,
            'stability': stability,
            'type': eq_type
        }
    
    def plot_nullclines(self, ax, x_max=2, y_max=2):
        """Plot nullclines on the given axes"""
        # x-nullcline: x=0 or y=(1-x)/a
        x_vals = np.linspace(0, x_max, 100)
        y_xnull = (1 - x_vals) / self.a
        valid_idx = (y_xnull >= 0) & (y_xnull <= y_max)
        ax.plot(x_vals[valid_idx], y_xnull[valid_idx], 
                'r-', linewidth=2.5, alpha=0.8, label='dx/dt=0')
        
        # y-nullcline: y=0 or y=1-bx
        y_ynull = 1 - self.b * x_vals
        valid_idx = (y_ynull >= 0) & (y_ynull <= y_max)
        ax.plot(x_vals[valid_idx], y_ynull[valid_idx], 
                'b-', linewidth=2.5, alpha=0.8, label='dy/dt=0')
        
        # Plot axes (x=0 and y=0)
        ax.axhline(0, color='r', linestyle='-', alpha=0.5, linewidth=1)
        ax.axvline(0, color='b', linestyle='-', alpha=0.5, linewidth=1)
    
    def plot_vector_field(self, ax, x_max=2, y_max=2, density=20):
        """Plot vector field on the given axes"""
        # Create grid
        x = np.linspace(0.05, x_max, density)
        y = np.linspace(0.05, y_max, density)
        X, Y = np.meshgrid(x, y)
        
        # Calculate derivatives
        DX, DY = np.zeros_like(X), np.zeros_like(Y)
        for i in range(len(x)):
            for j in range(len(y)):
                dstate = self.equations(0, [X[j,i], Y[j,i]])
                DX[j,i] = dstate[0]
                DY[j,i] = dstate[1]
        
        # Normalize for better visualization
        norm = np.sqrt(DX**2 + DY**2)
        mask = norm > 0
        DX[mask] = DX[mask] / norm[mask] * 0.1  # Scale arrows
        DY[mask] = DY[mask] / norm[mask] * 0.1
        
        # Plot vector field
        ax.quiver(X, Y, DX, DY, color='gray', alpha=0.6, 
                  angles='xy', scale_units='xy', scale=1, width=0.003)
    
    def plot_equilibria(self, ax):
        """Plot equilibrium points with stability information"""
        for eq in self.equilibria:
            x, y = eq
            if 0 <= x <= 2 and 0 <= y <= 2:
                analysis = self.analyze_equilibrium(eq)
                
                if analysis['type'] == 'stable node' or analysis['type'] == 'stable focus':
                    marker = 'o'
                    color = 'green'
                    size = 100
                    label = 'Stable'
                elif analysis['type'] == 'saddle':
                    marker = 's'
                    color = 'orange'
                    size = 100
                    label = 'Saddle'
                elif analysis['type'] == 'unstable node' or analysis['type'] == 'unstable focus':
                    marker = '^'
                    color = 'red'
                    size = 100
                    label = 'Unstable'
                else:
                    marker = 'x'
                    color = 'black'
                    size = 100
                    label = 'Degenerate'
                
                ax.scatter(x, y, s=size, c=color, marker=marker, 
                          edgecolors='black', linewidth=1, zorder=5,
                          label=label if 'label_added' not in locals() else "")
                locals()['label_added'] = True
    
    def simulate_trajectory(self, initial_state, t_span=(0, 50), n_points=1000):
        """Simulate a trajectory from given initial state"""
        t_eval = np.linspace(t_span[0], t_span[1], n_points)
        sol = solve_ivp(self.equations, t_span, initial_state, 
                       t_eval=t_eval, method='RK45', rtol=1e-8)
        return sol
    
    def plot_trajectory(self, ax, initial_state, t_span=(0, 50), color='purple'):
        """Plot a trajectory on the phase plane"""
        sol = self.simulate_trajectory(initial_state, t_span)
        ax.plot(sol.y[0], sol.y[1], '-', color=color, linewidth=2, alpha=0.8)
        ax.plot(initial_state[0], initial_state[1], 'o', 
                color=color, markersize=8, markeredgecolor='black', markeredgewidth=1)

def create_competition_figure(a, b, rho=1.0, case_name=""):
    """Create a complete figure for competition model analysis"""
    model = CompetitionModel(a, b, rho)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Phase portrait
    ax1 = axes[0]
    model.plot_vector_field(ax1, x_max=1.2, y_max=1.2, density=15)
    model.plot_nullclines(ax1, x_max=1.2, y_max=1.2)
    model.plot_equilibria(ax1)
    
    # Add threshold lines
    ax1.axvline(1, color='gray', linestyle='--', alpha=0.5)
    ax1.axhline(1, color='gray', linestyle='--', alpha=0.5)
    
    ax1.set_xlabel('Species 1 (x)', fontsize=12)
    ax1.set_ylabel('Species 2 (y)', fontsize=12)
    ax1.set_title(f'Phase Portrait: {case_name}\na={a}, b={b}, ρ={rho}', fontsize=14)
    ax1.set_xlim([-0.05, 1.2])
    ax1.set_ylim([-0.05, 1.2])
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper right', fontsize=10)
    
    # Time series for multiple trajectories
    ax2 = axes[1]
    
    # Different initial conditions
    initial_conditions = [
        [0.1, 0.4],
        [0.3, 0.7],
        [0.8, 0.2],
        [0.9, 0.6]
    ]
    
    colors = plt.cm.viridis(np.linspace(0, 1, len(initial_conditions)))
    
    for i, init_state in enumerate(initial_conditions):
        sol = model.simulate_trajectory(init_state, t_span=(0, 50))
        
        # Plot time series
        time = sol.t
        species1 = sol.y[0]
        species2 = sol.y[1]
        
        ax2.plot(time, species1, '-', color=colors[i], linewidth=1.5, 
                alpha=0.7, label=f'x(t), init={init_state}')
        ax2.plot(time, species2, '--', color=colors[i], linewidth=1.5, 
                alpha=0.7, label=f'y(t), init={init_state}')
    
    ax2.set_xlabel('Time (τ)', fontsize=12)
    ax2.set_ylabel('Population', fontsize=12)
    ax2.set_title('Time Series', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right', fontsize=9, ncol=2)
    
    plt.tight_layout()
    return fig, model

# Case 1: Species 1 wins (a < 1, b > 1)
print("Case 1: Species 1 wins")
fig1, model1 = create_competition_figure(a=0.5, b=1.5, case_name="Species 1 wins")
# plt.savefig('competition_case1.png', dpi=300, bbox_inches='tight')

# Case 2: Species 2 wins (a > 1, b < 1)
print("\nCase 2: Species 2 wins")
fig2, model2 = create_competition_figure(a=1.5, b=0.5, case_name="Species 2 wins")
# plt.savefig('competition_case2.png', dpi=300, bbox_inches='tight')

# Case 3: Stable coexistence (a < 1, b < 1)
print("\nCase 3: Stable coexistence")
fig3, model3 = create_competition_figure(a=0.4, b=0.6, case_name="Stable coexistence")
# plt.savefig('competition_case3.png', dpi=300, bbox_inches='tight')

# Case 4: Unstable coexistence (a > 1, b > 1)
print("\nCase 4: Unstable coexistence (competitive exclusion)")
fig4, model4 = create_competition_figure(a=1.4, b=1.6, case_name="Unstable coexistence")
# plt.savefig('competition_case4.png', dpi=300, bbox_inches='tight')

plt.show()
```

接以上代码：

```python
cases = [
    ("Species 1 wins", model1),
    ("Species 2 wins", model2),
    ("Stable coexistence", model3),
    ("Unstable coexistence", model4)
]

for case_name, model in cases:
    print(f"\n{case_name}:")
    print(f"  Parameters: a={model.a}, b={model.b}, ρ={model.rho}")
    print("  Equilibria:")
    for eq in model.equilibria:
        analysis = model.analyze_equilibrium(eq)
        print(f"    {eq}: {analysis['type']} (stability: {analysis['stability']})")
        print(f"      Eigenvalues: {analysis['eigenvalues']}")
```

运行结果：

```
Case 1: Species 1 wins

Case 2: Species 2 wins

Case 3: Stable coexistence

Case 4: Unstable coexistence (competitive exclusion)

============================================================
EQUILIBRIUM ANALYSIS
============================================================

Species 1 wins:
  Parameters: a=0.5, b=1.5, ρ=1.0
  Equilibria:
    (0.0, 0.0): unstable node (stability: unstable)
      Eigenvalues: [1. 1.]
    (1.0, 0.0): stable node (stability: stable)
      Eigenvalues: [-1.  -0.5]
    (0.0, 1.0): saddle (stability: unstable)
      Eigenvalues: [-1.   0.5]

Species 2 wins:
  Parameters: a=1.5, b=0.5, ρ=1.0
  Equilibria:
    (0.0, 0.0): unstable node (stability: unstable)
      Eigenvalues: [1. 1.]
    (1.0, 0.0): saddle (stability: unstable)
      Eigenvalues: [-1.   0.5]
    (0.0, 1.0): stable node (stability: stable)
      Eigenvalues: [-1.  -0.5]

Stable coexistence:
  Parameters: a=0.4, b=0.6, ρ=1.0
  Equilibria:
    (0.0, 0.0): unstable node (stability: unstable)
      Eigenvalues: [1. 1.]
    (1.0, 0.0): saddle (stability: unstable)
      Eigenvalues: [-1.   0.4]
    (0.0, 1.0): saddle (stability: unstable)
      Eigenvalues: [-1.   0.6]
    (0.7894736842105263, 0.5263157894736842): stable node (stability: stable)
      Eigenvalues: [-1.         -0.31578947]

Unstable coexistence:
  Parameters: a=1.4, b=1.6, ρ=1.0
  Equilibria:
    (0.0, 0.0): unstable node (stability: unstable)
      Eigenvalues: [1. 1.]
    (1.0, 0.0): stable node (stability: stable)
      Eigenvalues: [-1.  -0.6]
    (0.0, 1.0): stable node (stability: stable)
      Eigenvalues: [-1.  -0.4]
    (0.3225806451612903, 0.48387096774193566): saddle (stability: unstable)
      Eigenvalues: [ 0.19354839 -1.        ]
```

## 2.3.3. Lotka-Volterra捕食者-猎物模型

### 2.3.3.1. 模型建立与归一化

捕食者-猎物相互作用是生态学中的另一经典场景。Lotka-Volterra捕食者-猎物模型描述了捕食者和猎物种群之间的振荡动态。

设$N(t)$为猎物种群数量，$P(t)$为捕食者种群数量。经典模型假设：

1. 没有捕食者时，猎物以指数速率$r$增长
2. 没有猎物时，捕食者以指数速率$-m$减少（$m>0$）
3. 捕食者与猎物的相遇导致猎物被捕食，同时促进捕食者增长

模型方程为：

$$
\begin{aligned}
\frac{dN}{dt} &= rN - \varepsilon NP \\
\frac{dP}{dt} &= -\mu P + \theta NP
\end{aligned}
$$

其中：
- $r$：猎物的内禀增长率
- $\varepsilon$：捕食者的捕食效率（单位捕食者单位时间捕获的猎物数）
- $\mu$：捕食者的死亡率
- $\theta$：捕食者将猎物转化为自身繁殖的效率

引入无量纲变量进行归一化：

$$
x = \frac{\theta}{\mu} N, \quad y = \frac{\varepsilon}{r} P, \quad \tau = rt, \quad \alpha = \frac{\mu}{r}
$$

系统简化为：

$$
\begin{aligned}
\frac{dx}{d\tau} &= x(1 - y) \\
\frac{dy}{d\tau} &= \alpha y(x - 1)
\end{aligned}
$$

### 2.3.3.2. 零增长线与平衡点分析

**零增长线**：
1. 猎物零增长线：$\frac{dx}{d\tau} = 0 \Rightarrow x = 0$或$y = 1$
2. 捕食者零增长线：$\frac{dy}{d\tau} = 0 \Rightarrow y = 0$或$x = 1$

**平衡点**：
1. $(0,0)$：灭绝（鞍点）
2. $(1,1)$：共存平衡点（中心）

### 2.3.3.3. 稳定性分析：中心与极限环

计算雅可比矩阵：
$$
J(N, P) = \begin{pmatrix}
r - \varepsilon P & -\varepsilon N \\
\theta P & -\mu + \theta N
\end{pmatrix}
$$

在共存平衡点 $(\mu/\theta, r/\varepsilon)$ 处：
$$
J^* = \begin{pmatrix}
0 & -\varepsilon\mu/\theta \\
\theta r/\varepsilon & 0
\end{pmatrix}
$$
特征值为 $\lambda = \pm i\sqrt{r\mu}$，为纯虚数，表明该平衡点是**中心**。在非线性系统中，这通常意味着存在**周期解**。

在经典的Lotka-Volterra模型中，曲线是全闭的，但如果遇到其他类型的动力学（这在现实场景中是普遍现象）将会诱发**极限环**现象，即系统的震荡轨道会被汇聚到这个环上。

### 2.3.3.4. 捕食者-猎物模型的振荡行为

经典Lotka-Volterra模型具有保守量：

$$
V(x,y) = \alpha(x - \ln x) + (y - \ln y)
$$

满足$dV/d\tau = 0$，表明所有轨迹都是闭曲线，系统具有周期性解。这种周期性振荡反映了捕食者与猎物数量的相互制约关系。

```python-plot
"""
predator_prey_schematic.py
绘制捕食者-猎物模型的零增长线原理图和振荡行为
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_predator_prey_schematic(ax, alpha=1.0, beta=1.0, gamma=0.0):
    """绘制捕食者-猎物模型原理图"""
    
    # 设置坐标轴范围
    x_max = 2.5
    y_max = 2.5
    
    ax.set_xlim(0, x_max)
    ax.set_ylim(0, y_max)
    
    # 猎物零增长线: x=0 或 y=1-γx
    x_vals = np.linspace(0, x_max, 100)
    
    if gamma == 0:
        # 经典模型: y=1
        ax.axhline(1, 0, 1, color='red', linewidth=2, label='Prey nullcline ($dx/dτ=0$)')
    else:
        # 带有密度制约: y=1-γx
        y_prey_null = 1 - gamma * x_vals
        valid = (y_prey_null >= 0) & (y_prey_null <= y_max)
        ax.plot(x_vals[valid], y_prey_null[valid], 'r-', linewidth=2, label='Prey nullcline ($dx/dτ=0$)')
    
    # 捕食者零增长线: y=0 或 x=β
    ax.axvline(beta, 0, 1, color='blue', linewidth=2, label='Predator nullcline ($dy/dτ=0$)')
    
    # 标注平衡点
    if gamma == 0:
        # 经典模型: (1,1)
        ax.plot(1, 1, 'go', markersize=10, markeredgecolor='black', 
               markeredgewidth=1, label='Center equilibrium')
        ax.text(1.05, 1.05, '(1,1)', fontsize=11)
    else:
        # 带有密度制约: (β, 1-γβ)
        y_star = 1 - gamma * beta
        if y_star > 0:
            ax.plot(beta, y_star, 'go', markersize=10, markeredgecolor='black',
                   markeredgewidth=1, label='Equilibrium')
            ax.text(beta+0.05, y_star+0.05, f'({beta:.1f},{y_star:.1f})', fontsize=11)
    
    # 添加向量场箭头
    # 创建网格
    x_grid, y_grid = np.meshgrid(np.linspace(0.1, x_max-0.1, 12),
                                np.linspace(0.1, y_max-0.1, 12))
    
    # 计算方向
    dx = x_grid * (1 - gamma*x_grid - y_grid)
    dy = alpha * y_grid * (x_grid - beta)
    
    # 归一化
    norm = np.sqrt(dx**2 + dy**2)
    mask = norm > 0
    dx[mask] = dx[mask] / norm[mask] * 0.15
    dy[mask] = dy[mask] / norm[mask] * 0.15
    
    # 绘制向量场
    ax.quiver(x_grid, y_grid, dx, dy, color='gray', alpha=0.6,
              angles='xy', scale_units='xy', scale=1, width=0.004)
    
    # 绘制示例轨迹
    if gamma == 0:
        # 经典模型: 绘制闭合轨道
        # 使用参数方程: x = 1 + A*cos(ωt), y = 1 + B*sin(ωt)
        t = np.linspace(0, 2*np.pi, 200)
        A, B = 0.5, 0.5
        x_traj = 1 + A * np.cos(t)
        y_traj = 1 + B * np.sin(t)
        ax.plot(x_traj, y_traj, 'purple', linewidth=2, alpha=0.8, label='Periodic orbit')
    else:
        # 带有密度制约: 绘制螺旋轨迹
        from scipy.integrate import solve_ivp
        
        def equations(t, state):
            x, y = state
            dxdt = x * (1 - gamma*x - y)
            dydt = alpha * y * (x - beta)
            return [dxdt, dydt]
        
        # 从平衡点附近开始
        if gamma > 0:
            x0, y0 = beta, 1 - gamma*beta
            sol = solve_ivp(equations, [0, 50], [x0*1.2, y0*1.2], 
                           method='RK45', rtol=1e-8)
            ax.plot(sol.y[0], sol.y[1], 'purple', linewidth=2, alpha=0.8, label='Trajectory')
    
    # 标注关键区域
    # 区域I: 猎物增加，捕食者减少
    ax.text(0.05*x_max, 0.5*y_max, 'I: Prey↑, Predator↓', 
           fontsize=10, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
    
    # 区域II: 猎物增加，捕食者增加
    ax.text(0.5*x_max, 0.5*y_max, 'II: Prey↑, Predator↑', 
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
    
    # 区域III: 猎物减少，捕食者增加
    ax.text(0.5*x_max, 0.1*y_max, 'III: Prey↓, Predator↑', 
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    
    # 区域IV: 猎物减少，捕食者减少
    ax.text(0.05*x_max, 0.1*y_max, 'IV: Prey↓, Predator↓', 
           fontsize=10, bbox=dict(boxstyle='round', facecolor='pink', alpha=0.5))
    
    # 设置标题和标签
    ax.set_xlabel('Prey population (x)', fontsize=12)
    ax.set_ylabel('Predator population (y)', fontsize=12)
    
    if gamma == 0:
        title = 'Classic Lotka-Volterra Model\nα = {:.1f}'.format(alpha)
    else:
        title = f'Modified Model with Density Dependence\nα = {alpha:.1f}, β = {beta:.1f}, γ = {gamma:.1f}'
    
    ax.set_title(title, fontsize=14)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(fontsize=10, loc='upper right')

def plot_oscillation_diagram(ax):
    """绘制捕食者-猎物振荡的时间序列原理图"""
    
    # 生成示例振荡数据
    t = np.linspace(0, 40, 400)
    
    # 猎物种群: 正弦振荡
    prey_amp = 0.6
    prey_period = 10
    prey = 1 + prey_amp * np.sin(2*np.pi*t/prey_period - np.pi/4)
    
    # 捕食者种群: 余弦振荡（滞后于猎物）
    predator_amp = 0.4
    predator = 1 + predator_amp * np.cos(2*np.pi*t/prey_period - np.pi/4)
    
    # 绘制时间序列
    ax.plot(t, prey, 'b-', linewidth=2, label='Prey population')
    ax.plot(t, predator, 'r-', linewidth=2, label='Predator population')
    
    # 标注关键特征
    # 猎物峰值
    prey_max_idx = np.argmax(prey)
    ax.plot(t[prey_max_idx], prey[prey_max_idx], 'bo', markersize=8)
    # 移到左下
    ax.annotate('Prey peak', xy=(t[prey_max_idx], prey[prey_max_idx]),
               xytext=(t[prey_max_idx]-8, prey[prey_max_idx]-0.3),
               arrowprops=dict(arrowstyle='->', color='blue'),
               fontsize=10, color='blue', ha='center')
    
    # 捕食者峰值（滞后于猎物）
    predator_max_idx = np.argmax(predator)
    ax.plot(t[predator_max_idx], predator[predator_max_idx], 'ro', markersize=8)
    # 移到右下
    ax.annotate('Predator peak', xy=(t[predator_max_idx], predator[predator_max_idx]),
               xytext=(t[predator_max_idx]+8, predator[predator_max_idx]-0.3),
               arrowprops=dict(arrowstyle='->', color='red'),
               fontsize=10, color='red', ha='center')
    
    # 相位滞后标注 (移到下方)
    lag = t[predator_max_idx] - t[prey_max_idx]
    y_lag_pos = 0.9
    ax.annotate('', xy=(t[prey_max_idx], y_lag_pos),
               xytext=(t[predator_max_idx], y_lag_pos),
               arrowprops=dict(arrowstyle='<->', color='purple', linewidth=1.5))
    ax.text((t[prey_max_idx]+t[predator_max_idx])/2, y_lag_pos - 0.25,
           f'Phase lag\n{lag:.1f} time units',
           ha='center', fontsize=10, color='purple')
    
    # 添加区域着色显示周期
    period = prey_period
    for i in range(0, int(t[-1]), period):
        if i + period <= t[-1]:
            ax.axvspan(i, i+period, alpha=0.1, color='gray')
            if i == 0:
                ax.text(i+period/2, 0.2, 'One period', ha='center', fontsize=10)
    
    ax.set_xlabel('Time (τ)', fontsize=12)
    ax.set_ylabel('Population', fontsize=12)
    ax.set_title('Predator-Prey Oscillations', fontsize=14)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(fontsize=11, loc='upper right')
    
    # 添加说明文本
    ax.text(0.02, 0.98, 'Key observations:\n1. Predator lags behind prey\n2. Oscillations are periodic\n3. Amplitude depends on initial conditions',
           transform=ax.transAxes, fontsize=10, verticalalignment='top',
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# 创建捕食者-猎物模型原理图
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# 左上: 经典Lotka-Volterra模型
plot_predator_prey_schematic(axes[0, 0], alpha=1.0, beta=1.0, gamma=0.0)

# 右上: 带有密度制约的模型
plot_predator_prey_schematic(axes[0, 1], alpha=0.8, beta=0.7, gamma=0.3)

# 左下: 振荡时间序列
plot_oscillation_diagram(axes[1, 0])

# 右下: 相平面中的极限环
ax4 = axes[1, 1]
# 绘制极限环示意图
theta = np.linspace(0, 2*np.pi, 200)
# 定义极限环半径函数
def get_r_lc(th):
    return 0.6 + 0.1 * np.sin(5*th)

r = get_r_lc(theta)  # 非圆形极限环
x_lc = 1 + r * np.cos(theta)
y_lc = 1 + r * np.sin(theta)

ax4.plot(x_lc, y_lc, 'purple', linewidth=2, label='Limit cycle')

# 添加内外轨迹 - 使用构造法确保形状正确并趋向极限环
# 内部轨迹（从内向外趋向极限环）
t_vals = np.linspace(0, 4*np.pi, 500)
# 缩放因子从小变大趋向于1 (例如从0.2倍半径增长到1.0倍)
scale_inner = 1.0 - 0.8 * np.exp(-0.15 * t_vals)
r_inner_base = get_r_lc(t_vals)
r_inner = r_inner_base * scale_inner
x_inner = 1 + r_inner * np.cos(t_vals)
y_inner = 1 + r_inner * np.sin(t_vals)
ax4.plot(x_inner, y_inner, 'green', linewidth=1.5, alpha=0.7, label='Inner trajectory')

# 外部轨迹（从外向内趋向极限环）
t_vals_outer = np.linspace(0, 4*np.pi, 500)
theta_outer = t_vals_outer + np.pi  # 错开一点相位
# 缩放因子从大变小趋向于1 (例如从1.8倍半径减小到1.0倍)
scale_outer = 1.0 + 0.8 * np.exp(-0.15 * t_vals_outer)
r_outer_base = get_r_lc(theta_outer)
r_outer = r_outer_base * scale_outer
x_outer = 1 + r_outer * np.cos(theta_outer)
y_outer = 1 + r_outer * np.sin(theta_outer)
ax4.plot(x_outer, y_outer, 'orange', linewidth=1.5, alpha=0.7, label='Outer trajectory')

# 标注平衡点
ax4.plot(1, 1, 'ro', markersize=10, markeredgecolor='black', 
        markeredgewidth=1, label='Unstable equilibrium')

# 添加向量场箭头 - 修正为旋转且趋向极限环的流场
x_grid, y_grid = np.meshgrid(np.linspace(0.2, 1.8, 12), np.linspace(0.2, 1.8, 12))

for i in range(len(x_grid)):
    for j in range(len(y_grid)):
        x, y = x_grid[i, j], y_grid[i, j]
        u, v = x - 1, y - 1
        r_curr = np.sqrt(u**2 + v**2)
        if r_curr == 0: continue
        
        # 计算当前角度对应的极限环半径
        th = np.arctan2(v, u)
        r_target = get_r_lc(th)
        
        # 径向分量 (指向极限环)
        radial_strength = 0.8 * (r_target - r_curr)
        u_rad = radial_strength * np.cos(th)
        v_rad = radial_strength * np.sin(th)
        
        # 切向分量 (逆时针旋转)
        tangential_strength = 0.5 * r_curr 
        u_tan = -tangential_strength * np.sin(th)
        v_tan = tangential_strength * np.cos(th)
        
        dx = u_rad + u_tan
        dy = v_rad + v_tan
        
        norm = np.sqrt(dx**2 + dy**2) + 1e-10
        ax4.arrow(x, y, 0.08*dx/norm, 0.08*dy/norm, 
                 head_width=0.03, head_length=0.05, fc='gray', ec='gray', alpha=0.4)

ax4.set_xlim(0, 2)
ax4.set_ylim(0, 2)
ax4.set_xlabel('Prey population (x)', fontsize=12)
ax4.set_ylabel('Predator population (y)', fontsize=12)
ax4.set_title('Ideal Limit Cycle in Phase Plane (Not Lotka-Volterra)', fontsize=14)
ax4.grid(True, alpha=0.3, linestyle='--')
ax4.legend(fontsize=10, loc='upper right')

# 添加说明文本
ax4.text(0.02, 0.98, 'Limit cycle characteristics:\n1. Stable periodic solution\n2. Attracts nearby trajectories\n3. Independent of initial conditions',
        transform=ax4.transAxes, fontsize=10, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout(h_pad=3.0)
# plt.savefig('predator_prey_schematic_diagrams.png', dpi=300, bbox_inches='tight')
plt.show()
```

**运行结果说明**：上述代码生成了捕食者-猎物模型的四种原理图：

1. **经典Lotka-Volterra模型相平面**：
   - 红色水平线表示猎物零增长线($dx/dτ=0$)
   - 蓝色垂直线表示捕食者零增长线($dy/dτ=0$)
   - 绿色点表示中心平衡点(1,1)
   - 紫色闭合曲线表示周期性轨道

2. **带有密度制约的模型相平面**：
   - 红色斜线表示猎物零增长线（包含密度制约项）
   - 平衡点位置取决于参数β和γ（见下文）
   - 轨迹呈螺旋状趋向或远离平衡点

3. **振荡时间序列**：
   - 蓝色曲线表示猎物种群，红色曲线表示捕食者种群
   - 捕食者峰值滞后于猎物峰值，反映了生态学中的经典现象
   - 灰色背景区域标记了一个完整周期

4. **极限环示意图**：
   - 紫色闭合曲线表示稳定的极限环
   - 绿色和橙色轨迹分别从内部和外部趋向极限环
   - 红色点表示不稳定的平衡点
   - 箭头显示向量场方向，指向极限环

### 2.3.3.5. 带有密度制约的修正模型

更现实的模型包含猎物的密度制约（逻辑斯谛增长）：
$$
\begin{aligned}
\frac{dx}{d\tau} &= x(1 - x - y) \\
\frac{dy}{d\tau} &= \alpha y(x - \beta)
\end{aligned}
$$
其中$\beta = \mu/(rK\theta)$，$K$为猎物环境容纳量。

为什么不考虑捕食者的环境容纳量呢？因为在这个很简化的模型中，唯一影响捕食者生存的因子就是猎物的数量，所以捕食者也已经被猎物的环境容纳量所限制了。

该模型可能出现：
1. 捕食者灭绝（$\beta > 1$）
2. 稳定焦点（阻尼振荡趋向平衡点）
3. 稳定极限环（自持振荡）

```python-plot
"""
lotka_volterra_predator_prey.py
Complete analysis of Lotka-Volterra predator-prey models
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

class PredatorPreyModel:
    """Generalized predator-prey model with density dependence"""
    
    def __init__(self, alpha=1.0, beta=0.5, gamma=0.0, delta=0.0):
        """
        Initialize predator-prey model
        
        Parameters:
        -----------
        alpha : float
            Predator mortality relative to prey growth
        beta : float
            Predator half-saturation constant (or threshold prey density)
        gamma : float
            Prey density dependence (0 for classic model)
        delta : float
            Prey saturation constant (Holling Type II denominator coefficient)
            If 0, functional response is Type I (linear)
        """
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        
        # Calculate equilibria
        self.equilibria = self.calculate_equilibria()
    
    def equations(self, t, state):
        """Define the ODE system"""
        x, y = state  # x: prey, y: predator
        
        # Interaction term with functional response
        # Type I: xy (when delta=0)
        # Type II: xy / (1 + delta*x) (when delta>0)
        interaction = (x * y) / (1 + self.delta * x)
        
        # dxdt = x(1 - gamma*x) - interaction
        dxdt = x * (1 - self.gamma * x) - interaction
        
        # dydt = alpha * y * (predator_growth - beta)
        # Note: beta represents death/conversion ratio threshold
        if self.delta > 0:
            # For Holling II, typical form: dy/dt = alpha * (x/(1+delta*x)) * y - mu * y
            # Here we keep structure: alpha * y * (x/(1+delta*x) - beta)
            dydt = self.alpha * y * (x/(1 + self.delta * x) - self.beta)
        else:
            dydt = self.alpha * y * (x - self.beta)
        
        return [dxdt, dydt]
    
    def jacobian(self, x, y):
        """Calculate Jacobian matrix at point (x, y)"""
        if self.delta == 0:
            J11 = 1 - 2*self.gamma*x - y
            J12 = -x
            J21 = self.alpha * y
            J22 = self.alpha * (x - self.beta)
        else:
            denom = 1 + self.delta * x
            denom_sq = denom * denom
            
            # dxdt = x - gamma*x^2 - x*y/denom
            # dx/dx = 1 - 2*gamma*x - (y(1) - 0)/denom ... wait d(x/denom)/dx
            # d(x/(1+dx))/dx = (1+dx - xd)/(1+dx)^2 = 1/(1+dx)^2
            J11 = 1 - 2*self.gamma*x - y / denom_sq
            
            # dx/dy = -x/denom
            J12 = -x / denom
            
            # dydt = alpha*y*(x/denom - beta)
            # dy/dx = alpha*y * (1/denom_sq)
            J21 = self.alpha * y / denom_sq
            
            # dy/dy = alpha * (x/denom - beta)
            J22 = self.alpha * (x/denom - self.beta)
            
        return np.array([[J11, J12], [J21, J22]])
    
    def calculate_equilibria(self):
        """Calculate all equilibrium points"""
        eq_points = []
        
        # (0, 0) - extinction
        eq_points.append((0.0, 0.0))
        
        # Prey only (y=0) -> x(1 - gamma*x) = 0
        if self.gamma > 0:
            eq_points.append((1/self.gamma, 0.0))
        
        # Coexistence
        # From dy/dt=0 -> x/(1+delta*x) = beta  => x = beta(1+delta*x) => x(1 - beta*delta) = beta
        if self.delta > 0:
            if 1 - self.beta * self.delta > 0:
                x_star = self.beta / (1 - self.beta * self.delta)
                # From dx/dt=0 -> 1 - gamma*x - y/(1+delta*x) = 0 => y = (1-gamma*x)(1+delta*x)
                if self.gamma == 0 or x_star < 1/self.gamma:
                    y_star = (1 - self.gamma * x_star) * (1 + self.delta * x_star)
                    if y_star > 0:
                        eq_points.append((x_star, y_star))
        else:
            # Classic model: x = beta
            x_star = self.beta
            if self.gamma == 0:
                eq_points.append((x_star, 1.0))
            else:
                y_star = 1 - self.gamma * x_star
                if y_star > 0:
                    eq_points.append((x_star, y_star))
        
        return eq_points
    
    def analyze_equilibrium(self, eq_point):
        """Analyze stability of an equilibrium point"""
        x, y = eq_point
        J = self.jacobian(x, y)
        eigvals, eigvecs = np.linalg.eig(J)
        
        # Classify stability
        real_parts = np.real(eigvals)
        
        if all(real_parts < 0):
            stability = "stable"
        elif any(real_parts > 0):
            stability = "unstable"
        else:
            stability = "marginally stable"
        
        # Classify type
        if np.all(np.isreal(eigvals)):
            if stability == "stable":
                eq_type = "stable node"
            elif stability == "unstable":
                if eigvals[0] * eigvals[1] < 0:
                    eq_type = "saddle"
                else:
                    eq_type = "unstable node"
            else:
                eq_type = "degenerate"
        else:
            if stability == "stable":
                eq_type = "stable focus"
            elif stability == "unstable":
                eq_type = "unstable focus"
            elif real_parts[0] == 0 and real_parts[1] == 0:
                eq_type = "center"
            else:
                eq_type = "unknown"
        
        return {
            'point': eq_point,
            'jacobian': J,
            'eigenvalues': eigvals,
            'eigenvectors': eigvecs,
            'stability': stability,
            'type': eq_type
        }
    
    def plot_nullclines(self, ax, x_max=3.0, y_max=3.0):
        """Plot nullclines on the given axes"""
        # Prey nullcline: dx/dt = 0 => y = (1 - gamma*x)(1 + delta*x) (if delta>0)
        x_vals = np.linspace(0, x_max, 200)
        
        if self.delta > 0:
            y_prey_null = (1 - self.gamma * x_vals) * (1 + self.delta * x_vals)
        else:
            y_prey_null = 1 - self.gamma * x_vals
            
        # Clip purely for visualization convenience if needed, but plotting logic handles bounds
        valid_idx = (y_prey_null >= -0.5) & (y_prey_null <= y_max + 1)
        ax.plot(x_vals[valid_idx], y_prey_null[valid_idx], 
                'r-', linewidth=2.5, alpha=0.8, label='Prey nullcline (dx/dt=0)')
        
        # Predator nullcline: dy/dt = 0
        if self.delta > 0:
            if 1 - self.beta * self.delta > 0:
                threshold_x = self.beta / (1 - self.beta * self.delta)
            else:
                threshold_x = np.inf
        else:
            threshold_x = self.beta
        
        if 0 <= threshold_x <= x_max:
            ax.axvline(threshold_x, 0, y_max, 
                      color='b', linewidth=2.5, alpha=0.8, 
                      label='Predator nullcline (dy/dt=0)')
        
        # Plot axes (x=0 and y=0)
        ax.axhline(0, color='r', linestyle='-', alpha=0.5, linewidth=1)
        ax.axvline(0, color='b', linestyle='-', alpha=0.5, linewidth=1)
    
    def plot_vector_field(self, ax, x_max=3.0, y_max=3.0, density=20):
        """Plot vector field on the given axes"""
        # Create grid
        x = np.linspace(0.05, x_max, density)
        y = np.linspace(0.05, y_max, density)
        X, Y = np.meshgrid(x, y)
        
        # Calculate derivatives
        DX, DY = np.zeros_like(X), np.zeros_like(Y)
        for i in range(len(x)):
            for j in range(len(y)):
                dstate = self.equations(0, [X[j,i], Y[j,i]])
                DX[j,i] = dstate[0]
                DY[j,i] = dstate[1]
        
        # Normalize for better visualization
        norm = np.sqrt(DX**2 + DY**2)
        mask = norm > 0
        DX[mask] = DX[mask] / norm[mask] * 0.15  # Scale arrows
        DY[mask] = DY[mask] / norm[mask] * 0.15
        
        # Plot vector field
        ax.quiver(X, Y, DX, DY, color='gray', alpha=0.6, 
                  angles='xy', scale_units='xy', scale=1, width=0.003)
    
    def plot_equilibria(self, ax):
        """Plot equilibrium points with stability information"""
        for eq in self.equilibria:
            x, y = eq
            if 0 <= x <= 3.0 and 0 <= y <= 3.0:
                analysis = self.analyze_equilibrium(eq)
                
                if analysis['type'] == 'stable node' or analysis['type'] == 'stable focus':
                    marker = 'o'
                    color = 'green'
                    size = 100
                    label = 'Stable'
                elif analysis['type'] == 'saddle':
                    marker = 's'
                    color = 'orange'
                    size = 100
                    label = 'Saddle'
                elif analysis['type'] == 'center':
                    marker = 'D'
                    color = 'blue'
                    size = 80
                    label = 'Center'
                elif analysis['type'] == 'unstable node' or analysis['type'] == 'unstable focus':
                    marker = '^'
                    color = 'red'
                    size = 100
                    label = 'Unstable'
                else:
                    marker = 'x'
                    color = 'black'
                    size = 100
                    label = 'Degenerate'
                
                ax.scatter(x, y, s=size, c=color, marker=marker, 
                          edgecolors='black', linewidth=1, zorder=5,
                          label=label if 'label_added' not in locals() else "")
                locals()['label_added'] = True
    
    def simulate_trajectory(self, initial_state, t_span=(0, 100), n_points=2000):
        """Simulate a trajectory from given initial state"""
        t_eval = np.linspace(t_span[0], t_span[1], n_points)
        sol = solve_ivp(self.equations, t_span, initial_state, 
                       t_eval=t_eval, method='RK45', rtol=1e-8)
        return sol
    
    def plot_trajectory(self, ax, initial_state, t_span=(0, 100), color='purple'):
        """Plot a trajectory on the phase plane"""
        sol = self.simulate_trajectory(initial_state, t_span)
        ax.plot(sol.y[0], sol.y[1], '-', color=color, linewidth=2, alpha=0.8)
        ax.plot(initial_state[0], initial_state[1], 'o', 
                color=color, markersize=8, markeredgecolor='black', markeredgewidth=1)

def create_predator_prey_figure(alpha=1.0, beta=0.5, gamma=0.0, delta=0.0, case_name=""):
    """Create a complete figure for predator-prey model analysis"""
    model = PredatorPreyModel(alpha, beta, gamma, delta)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    
    # Phase portrait
    ax1 = axes[0, 0]
    model.plot_vector_field(ax1, x_max=3.0, y_max=2.0, density=20)
    model.plot_nullclines(ax1, x_max=3.0, y_max=2.0)
    model.plot_equilibria(ax1)
    
    # Add trajectories
    initial_conditions = [
        [0.5, 0.5],
        [1.5, 0.3],
        [0.8, 1.2],
        [2.0, 0.8]
    ]
    
    colors = plt.cm.viridis(np.linspace(0, 1, len(initial_conditions)))
    
    for i, init_state in enumerate(initial_conditions):
        model.plot_trajectory(ax1, init_state, t_span=(0, 100), color=colors[i])
    
    ax1.set_xlabel('Prey population (x)', fontsize=12)
    ax1.set_ylabel('Predator population (y)', fontsize=12)
    ax1.set_title(f'Phase Portrait: {case_name}\nα={alpha}, β={beta}, γ={gamma}, δ={delta}', fontsize=14)
    ax1.set_xlim([-0.1, 3.0])
    ax1.set_ylim([-0.1, 2.0])
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper right', fontsize=10)
    
    # Time series for first trajectory
    ax2 = axes[0, 1]
    sol = model.simulate_trajectory(initial_conditions[0], t_span=(0, 100))
    
    time = sol.t
    prey = sol.y[0]
    predator = sol.y[1]
    
    ax2.plot(time, prey, 'b-', linewidth=2, label='Prey (x)')
    ax2.plot(time, predator, 'r-', linewidth=2, label='Predator (y)')
    
    ax2.set_xlabel('Time (τ)', fontsize=12)
    ax2.set_ylabel('Population', fontsize=12)
    ax2.set_title('Time Series (single trajectory)', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right', fontsize=11)
    
    # State-space plot with time color coding
    ax3 = axes[1, 0]
    scatter = ax3.scatter(prey, predator, c=time, cmap='viridis', 
                         s=20, alpha=0.6, edgecolors='none')
    
    # Add nullclines for reference
    model.plot_nullclines(ax3, x_max=3.0, y_max=2.0)
    
    ax3.set_xlabel('Prey population (x)', fontsize=12)
    ax3.set_ylabel('Predator population (y)', fontsize=12)
    ax3.set_title('State Space with Time Color Coding', fontsize=14)
    ax3.set_xlim([0, 3.0])
    ax3.set_ylim([0, 2.0])
    ax3.grid(True, alpha=0.3)
    
    plt.colorbar(scatter, ax=ax3, label='Time (τ)')
    
    # Population ratio and conserved quantity (for classic model)
    ax4 = axes[1, 1]
    
    if gamma == 0 and delta == 0:
        # For classic model, plot conserved quantity
        V = alpha * (prey - np.log(prey + 1e-10)) + (predator - np.log(predator + 1e-10))
        ax4.plot(time, V, 'g-', linewidth=2, label='Conserved quantity V')
        ax4.set_ylabel('V(x,y)', fontsize=12)
        ax4.set_title('Conserved Quantity (Classic Model)', fontsize=14)
    else:
        # For other models
        ratio = prey / (predator + 1e-10)
        ax4.plot(time, ratio, 'm-', linewidth=2, label='Prey/Predator ratio')
        ax4.set_ylabel('Prey/Predator ratio', fontsize=12)
        ax4.set_title('Population Ratio', fontsize=14)
    
    ax4.set_xlabel('Time (τ)', fontsize=12)
    ax4.grid(True, alpha=0.3)
    ax4.legend(loc='upper right', fontsize=11)
    
    plt.tight_layout()
    return fig, model

# Analyze different predator-prey scenarios
# Case 1: Classic Lotka-Volterra (γ=0, center)
print("Case 1: Classic Lotka-Volterra model")
fig1, model1 = create_predator_prey_figure(
    alpha=1.0, beta=0.5, gamma=0.0, delta=0.0,
    case_name="Classic Lotka-Volterra (neutral cycles)"
)
# plt.savefig('predator_prey_classic.png', dpi=300, bbox_inches='tight')

# Case 2: With density dependence (damped oscillations)
print("\nCase 2: Model with prey density dependence")
fig2, model2 = create_predator_prey_figure(
    alpha=1.0, beta=0.5, gamma=0.2, delta=0.0,
    case_name="With density dependence (damped oscillations)"
)
# plt.savefig('predator_prey_damped.png', dpi=300, bbox_inches='tight')

# Case 3: Limit cycle (Hopf bifurcation) using Rosenzweig-MacArthur
# Parameters adjusted to ensure the interior equilibrium is unstable (left of hump)
# Peak of prey nullcline y=(1-0.3x)(1+x) is at x approx 1.16
# Predator nullcline is at x* = beta/(1-beta) (if delta=1)
# 0.35 / 0.65 = 0.53, which is < 1.16, creating instability.
print("\nCase 3: Model exhibiting limit cycle")
fig3, model3 = create_predator_prey_figure(
    alpha=1.0, beta=0.35, gamma=0.3, delta=1.0,
    case_name="Limit Cycle (Rosenzweig-MacArthur)"
)
# plt.savefig('predator_prey_limit_cycle.png', dpi=300, bbox_inches='tight')

plt.show()
```

接以上代码：

```python
cases = [
    ("Classic model", model1),
    ("Density dependence", model2),
    ("Limit cycle", model3)
]

for case_name, model in cases:
    print(f"\n{case_name}:")
    print(f"  Parameters: α={model.alpha}, β={model.beta}, γ={model.gamma}, δ={model.delta}")
    print("  Equilibria:")
    for eq in model.equilibria:
        analysis = model.analyze_equilibrium(eq)
        print(f"    {eq}: {analysis['type']} (stability: {analysis['stability']})")
        print(f"      Eigenvalues: {analysis['eigenvalues']}")
```

运行结果：

```
Case 1: Classic Lotka-Volterra model

Case 2: Model with prey density dependence

Case 3: Model exhibiting limit cycle

============================================================
EQUILIBRIUM ANALYSIS
============================================================

Classic model:
  Parameters: α=1.0, β=0.5, γ=0.0, δ=0.0
  Equilibria:
    (0.0, 0.0): saddle (stability: unstable)
      Eigenvalues: [ 1.  -0.5]
    (0.5, 1.0): center (stability: marginally stable)
      Eigenvalues: [0.+0.70710678j 0.-0.70710678j]

Density dependence:
  Parameters: α=1.0, β=0.5, γ=0.2, δ=0.0
  Equilibria:
    (0.0, 0.0): saddle (stability: unstable)
      Eigenvalues: [ 1.  -0.5]
    (5.0, 0.0): saddle (stability: unstable)
      Eigenvalues: [-1.   4.5]
    (0.5, 0.9): stable focus (stability: stable)
      Eigenvalues: [-0.05+0.66895441j -0.05-0.66895441j]

Limit cycle:
  Parameters: α=1.0, β=0.35, γ=0.3, δ=1.0
  Equilibria:
    (0.0, 0.0): saddle (stability: unstable)
      Eigenvalues: [ 1.   -0.35]
    (3.3333333333333335, 0.0): saddle (stability: unstable)
      Eigenvalues: [-1.          0.41923077]
    (0.5384615384615384, 1.2899408284023668): unstable focus (stability: unstable)
      Eigenvalues: [0.06596154+0.43173959j 0.06596154-0.43173959j]
```

### 2.3.3.6. 捕食者-猎物模型的生态学启示

捕食者-猎物模型揭示了几个重要生态学原理：

1. **种群振荡的必然性**：在没有外部干扰的情况下，捕食者-猎物系统倾向于呈现周期性振荡。
2. **时滞效应**：捕食者数量变化滞后于猎物数量变化，这是由捕食者需要时间将猎物转化为自身增长造成的。
3. **稳定性条件**：加入猎物密度制约（逻辑斯谛项）可以稳定系统，防止振幅无限扩大。
4. **生态平衡的动态性**：平衡不是静态的，而是动态振荡中的长期平均状态。

## 2.3.4. 复杂模型：竞争与捕食的结合

### 2.3.4.1. 统一框架下的生态模型

现实生态系统往往同时包含竞争和捕食等多种相互作用。考虑一个包含两个竞争物种和一个捕食者的系统：

$$
\begin{aligned}
\frac{dx_1}{dt} &= r_1 x_1 \left(1 - \frac{x_1}{K_1} - \alpha_{12}\frac{x_2}{K_1}\right) - \varepsilon_1 x_1 y \\
\frac{dx_2}{dt} &= r_2 x_2 \left(1 - \frac{x_2}{K_2} - \alpha_{21}\frac{x_1}{K_2}\right) - \varepsilon_2 x_2 y \\
\frac{dy}{dt} &= -\mu y + \theta_1 x_1 y + \theta_2 x_2 y
\end{aligned}
$$

其中$x_1$和$x_2$是两个竞争物种，$y$是捕食者。

### 2.3.4.2. 归一化与简化

引入无量纲变量进行归一化：

$$
\begin{aligned}
u_1 &= \frac{x_1}{K_1}, \quad u_2 = \frac{x_2}{K_2}, \quad v = \frac{\varepsilon_1}{r_1} y, \quad \tau = r_1 t \\
a &= \alpha_{12}\frac{K_2}{K_1}, \quad b = \alpha_{21}\frac{K_1}{K_2}, \quad \rho = \frac{r_2}{r_1} \\
c_1 &= \frac{\varepsilon_1 K_1}{r_1}, \quad c_2 &= \frac{\varepsilon_2 K_2}{r_1}, \quad d = \frac{\mu}{r_1} \\
e_1 &= \frac{\theta_1 K_1}{\varepsilon_1}, \quad e_2 &= \frac{\theta_2 K_2}{\varepsilon_1}
\end{aligned}
$$

简化后的系统：

$$
\begin{aligned}
\frac{du_1}{d\tau} &= u_1(1 - u_1 - a u_2 - v) \\
\frac{du_2}{d\tau} &= \rho u_2(1 - u_2 - b u_1 - \frac{c_2}{c_1} v) \\
\frac{dv}{d\tau} &= -d v + e_1 u_1 v + e_2 u_2 v
\end{aligned}
$$

由于这是一个新模型，可以先尝试一些数值模拟，探索其可能的行为：

```python-plot
"""
complex_ecological_model_enhanced.py
Enhanced analysis of complex ecological models with diverse dynamics
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D

class ComplexEcologicalModel:
    """Model combining competition and predation with enhanced analysis"""
    
    def __init__(self, a=0.5, b=0.5, rho=1.0, c1=0.5, c2=0.5, d=0.5, e1=1.0, e2=1.0):
        """
        Initialize complex ecological model
        
        Parameters:
        -----------
        a, b : float
            Competition coefficients
        rho : float
            Relative growth rate of species 2
        c1, c2 : float
            Predation rates on species 1 and 2
        d : float
            Predator mortality rate
        e1, e2 : float
            Conversion efficiencies
        """
        self.a = a
        self.b = b
        self.rho = rho
        self.c1 = c1
        self.c2 = c2
        self.d = d
        self.e1 = e1
        self.e2 = e2
    
    def equations(self, t, state):
        """Define the 3D ODE system"""
        u1, u2, v = state
        
        du1dt = u1 * (1 - u1 - self.a * u2 - v)
        du2dt = self.rho * u2 * (1 - u2 - self.b * u1 - (self.c2/self.c1) * v)
        dvdt = -self.d * v + self.e1 * u1 * v + self.e2 * u2 * v
        
        return [du1dt, du2dt, dvdt]
    
    def jacobian(self, u1, u2, v):
        """Calculate Jacobian matrix at point (u1, u2, v)"""
        J11 = 1 - 2*u1 - self.a*u2 - v
        J12 = -self.a * u1
        J13 = -u1
        
        J21 = -self.rho * self.b * u2
        J22 = self.rho * (1 - 2*u2 - self.b * u1 - (self.c2/self.c1) * v)
        J23 = -self.rho * (self.c2/self.c1) * u2
        
        J31 = self.e1 * v
        J32 = self.e2 * v
        J33 = -self.d + self.e1 * u1 + self.e2 * u2
        
        return np.array([[J11, J12, J13],
                         [J21, J22, J23],
                         [J31, J32, J33]])
    
    def analyze_equilibria(self):
        """Analyze all possible equilibria of the system"""
        equilibria = []
        
        # Extinction: (0, 0, 0)
        equilibria.append((0.0, 0.0, 0.0))
        
        # Prey 1 only: (1, 0, 0)
        equilibria.append((1.0, 0.0, 0.0))
        
        # Prey 2 only: (0, 1, 0)
        equilibria.append((0.0, 1.0, 0.0))
        
        # Both preys, no predator: coexistence without predation
        # Solve: 1 - u1 - a*u2 = 0 and 1 - u2 - b*u1 = 0
        denominator = 1 - self.a * self.b
        if abs(denominator) > 1e-10:
            u1_star = (1 - self.a) / denominator
            u2_star = (1 - self.b) / denominator
            if u1_star > 0 and u2_star > 0:
                equilibria.append((u1_star, u2_star, 0.0))
        
        # Predator with prey 1 only: (d/e1, 0, 1 - d/e1)
        if self.e1 > 0:
            u1_star = self.d / self.e1
            v_star = 1 - u1_star
            if u1_star > 0 and v_star > 0:
                equilibria.append((u1_star, 0.0, v_star))
        
        # Predator with prey 2 only: (0, d/e2, 1 - d/e2)
        if self.e2 > 0:
            u2_star = self.d / self.e2
            v_star = 1 - u2_star
            if u2_star > 0 and v_star > 0:
                equilibria.append((0.0, u2_star, v_star))
        
        # Coexistence of all three species
        # Solve the full system numerically
        from scipy.optimize import fsolve
        
        def full_system(vars):
            u1, u2, v = vars
            eq1 = u1 * (1 - u1 - self.a * u2 - v)
            eq2 = self.rho * u2 * (1 - u2 - self.b * u1 - (self.c2/self.c1) * v)
            eq3 = v * (-self.d + self.e1 * u1 + self.e2 * u2)
            return [eq1, eq2, eq3]
        
        # Try multiple starting points
        initial_guesses = [
            [0.3, 0.3, 0.3],
            [0.5, 0.2, 0.4],
            [0.2, 0.5, 0.4],
            [0.4, 0.4, 0.2]
        ]
        
        for guess in initial_guesses:
            try:
                solution = fsolve(full_system, guess, full_output=True)
                if solution[2] == 1:  # ier == 1 means solution found
                    u1_sol, u2_sol, v_sol = solution[0]
                    if (u1_sol > 0 and u2_sol > 0 and v_sol > 0 and 
                        u1_sol <= 1.5 and u2_sol <= 1.5 and v_sol <= 1.5):
                        # Check if this solution is significantly different from existing ones
                        is_new = True
                        for existing in equilibria:
                            dist = np.sqrt((u1_sol-existing[0])**2 + 
                                          (u2_sol-existing[1])**2 + 
                                          (v_sol-existing[2])**2)
                            if dist < 1e-3:
                                is_new = False
                                break
                        if is_new:
                            equilibria.append((u1_sol, u2_sol, v_sol))
            except:
                continue
        
        return equilibria
    
    def analyze_stability(self, equilibrium):
        """Analyze stability of an equilibrium point"""
        u1, u2, v = equilibrium
        J = self.jacobian(u1, u2, v)
        eigvals = np.linalg.eigvals(J)
        
        # Classify stability
        real_parts = np.real(eigvals)
        
        if all(real_parts < 0):
            stability = "asymptotically stable"
        elif any(real_parts > 0):
            stability = "unstable"
        else:
            stability = "marginally stable"
        
        # Classify type
        if np.all(np.isreal(eigvals)):
            if stability == "asymptotically stable":
                eq_type = "stable node"
            elif stability == "unstable":
                if np.sum(real_parts > 0) == 1:
                    eq_type = "saddle point (1D unstable)"
                elif np.sum(real_parts > 0) == 2:
                    eq_type = "saddle point (2D unstable)"
                else:
                    eq_type = "unstable node"
            else:
                eq_type = "degenerate"
        else:
            complex_eigs = eigvals[np.iscomplex(eigvals)]
            if stability == "asymptotically stable":
                eq_type = "stable focus"
            elif stability == "unstable":
                eq_type = "unstable focus"
            elif np.all(np.abs(real_parts) < 1e-10):
                eq_type = "center"
            else:
                eq_type = "unknown"
        
        return {
            'point': equilibrium,
            'jacobian': J,
            'eigenvalues': eigvals,
            'stability': stability,
            'type': eq_type
        }
    
    def simulate(self, initial_state, t_span=(0, 500), n_points=10000, method='RK45'):
        """Simulate the system"""
        t_eval = np.linspace(t_span[0], t_span[1], n_points)
        sol = solve_ivp(self.equations, t_span, initial_state,
                       t_eval=t_eval, method=method, rtol=1e-10, atol=1e-12)
        return sol
    
    def calculate_lyapunov_exponents(self, initial_state, t_span=(0, 1000), 
                                   perturbation=1e-8, n_trajectories=2):
        """Estimate Lyapunov exponents using nearby trajectories"""
        # This is a simplified method for demonstration
        # For accurate calculation, use specialized algorithms
        
        results = []
        
        # Reference trajectory
        sol_ref = self.simulate(initial_state, t_span, n_points=2000)
        t_ref = sol_ref.t
        u1_ref, u2_ref, v_ref = sol_ref.y
        
        # Perturbed trajectories
        perturbations = [
            [perturbation, 0, 0],
            [0, perturbation, 0],
            [0, 0, perturbation]
        ]
        
        exponents = []
        
        for i, pert in enumerate(perturbations):
            initial_pert = [initial_state[j] + pert[j] for j in range(3)]
            sol_pert = self.simulate(initial_pert, t_span, n_points=2000)
            
            # Calculate separation over time
            separation = []
            for j in range(min(len(t_ref), len(sol_pert.t))):
                idx_ref = j
                # Find closest time in perturbed solution
                idx_pert = np.argmin(np.abs(sol_pert.t - t_ref[idx_ref]))
                
                dist = np.sqrt(
                    (u1_ref[idx_ref] - sol_pert.y[0][idx_pert])**2 +
                    (u2_ref[idx_ref] - sol_pert.y[1][idx_pert])**2 +
                    (v_ref[idx_ref] - sol_pert.y[2][idx_pert])**2
                )
                separation.append(dist)
            
            separation = np.array(separation)
            # Filter out zero and very small separations
            valid = separation > 1e-12
            if np.any(valid):
                # Fit exponential to separation growth
                from scipy.stats import linregress
                slope, intercept, r_value, p_value, std_err = linregress(
                    t_ref[valid], np.log(separation[valid])
                )
                exponents.append(slope)
            else:
                exponents.append(0.0)
        
        return exponents
    
    def plot_3d_trajectory(self, initial_state, t_span=(0, 500), 
                          show_equilibria=True, show_vector_field=False):
        """Plot 3D trajectory with enhanced visualization"""
        sol = self.simulate(initial_state, t_span, n_points=10000)
        u1, u2, v = sol.y
        
        fig = plt.figure(figsize=(16, 12))
        
        # 3D trajectory
        ax1 = fig.add_subplot(231, projection='3d')
        
        # Color trajectory by time
        colors = plt.cm.viridis(np.linspace(0, 1, len(u1)))
        for i in range(len(u1)-1):
            ax1.plot(u1[i:i+2], u2[i:i+2], v[i:i+2], 
                    color=colors[i], linewidth=0.5, alpha=0.8)
        
        ax1.scatter(u1[0], u2[0], v[0], s=100, c='red', 
                   marker='o', label='Start', zorder=5)
        ax1.scatter(u1[-1], u2[-1], v[-1], s=100, c='green', 
                   marker='s', label='End', zorder=5)
        
        if show_equilibria:
            equilibria = self.analyze_equilibria()
            for eq in equilibria:
                u1_eq, u2_eq, v_eq = eq
                analysis = self.analyze_stability(eq)
                
                if analysis['stability'] == 'asymptotically stable':
                    color = 'green'
                    marker = 'o'
                    size = 80
                    label = 'Stable'
                elif analysis['stability'] == 'unstable':
                    if analysis['type'].startswith('saddle'):
                        color = 'orange'
                        marker = 's'
                        size = 80
                        label = 'Saddle'
                    else:
                        color = 'red'
                        marker = '^'
                        size = 80
                        label = 'Unstable'
                else:
                    color = 'blue'
                    marker = 'D'
                    size = 60
                    label = 'Center'
                
                ax1.scatter(u1_eq, u2_eq, v_eq, s=size, c=color, 
                           marker=marker, edgecolors='black', 
                           linewidth=1, zorder=10, label=label)
        
        ax1.set_xlabel('Species 1 (u1)', fontsize=12)
        ax1.set_ylabel('Species 2 (u2)', fontsize=12)
        ax1.set_zlabel('Predator (v)', fontsize=12)
        ax1.set_title('3D State Space Trajectory', fontsize=14)
        ax1.legend(fontsize=10)
        ax1.grid(True, alpha=0.3)
        
        # Projections with phase portraits
        projections = [
            (232, u1, u2, 'Species 1 (u1)', 'Species 2 (u2)', 'Prey Competition Plane'),
            (233, u1, v, 'Species 1 (u1)', 'Predator (v)', 'Species 1 vs Predator'),
            (234, u2, v, 'Species 2 (u2)', 'Predator (v)', 'Species 2 vs Predator'),
        ]
        
        for subplot_idx, x_data, y_data, xlabel, ylabel, title in projections:
            ax = fig.add_subplot(subplot_idx)
            
            # Color by density (2D histogram)
            hb = ax.hexbin(x_data, y_data, gridsize=30, cmap='viridis', 
                          alpha=0.7, bins='log')
            plt.colorbar(hb, ax=ax, label='Density')
            
            # Overlay trajectory
            ax.plot(x_data, y_data, 'k-', linewidth=0.5, alpha=0.5)
            
            ax.set_xlabel(xlabel, fontsize=11)
            ax.set_ylabel(ylabel, fontsize=11)
            ax.set_title(title, fontsize=13)
            ax.grid(True, alpha=0.3)
        
        # Time series
        ax5 = fig.add_subplot(235)
        t = sol.t
        ax5.plot(t, u1, 'b-', linewidth=1.5, alpha=0.8, label='Species 1')
        ax5.plot(t, u2, 'g-', linewidth=1.5, alpha=0.8, label='Species 2')
        ax5.plot(t, v, 'r-', linewidth=1.5, alpha=0.8, label='Predator')
        ax5.set_xlabel('Time (τ)', fontsize=12)
        ax5.set_ylabel('Population', fontsize=12)
        ax5.set_title('Time Series', fontsize=14)
        ax5.legend(fontsize=11)
        ax5.grid(True, alpha=0.3)
        
        # Frequency analysis (for oscillatory behavior)
        ax6 = fig.add_subplot(236)
        
        # Calculate power spectral density
        from scipy.signal import periodogram
        f1, P1 = periodogram(u1, fs=1/(t[1]-t[0]))
        f2, P2 = periodogram(u2, fs=1/(t[1]-t[0]))
        f3, P3 = periodogram(v, fs=1/(t[1]-t[0]))
        
        ax6.loglog(f1[f1>0], P1[f1>0], 'b-', alpha=0.7, label='Species 1')
        ax6.loglog(f2[f2>0], P2[f2>0], 'g-', alpha=0.7, label='Species 2')
        ax6.loglog(f3[f3>0], P3[f3>0], 'r-', alpha=0.7, label='Predator')
        
        ax6.set_xlabel('Frequency', fontsize=12)
        ax6.set_ylabel('Power', fontsize=12)
        ax6.set_title('Power Spectral Density', fontsize=14)
        ax6.legend(fontsize=11)
        ax6.grid(True, alpha=0.3, which='both')
        
        plt.tight_layout()
        return fig, sol

def explore_diverse_dynamics():
    """Explore different dynamical regimes with parameters tuned for diverse behaviors"""
    
    # Enhanced parameter sets for diverse behaviors
    parameter_sets = [
        {
            'name': 'Predator-mediated coexistence (stable equilibrium)',
            'params': {'a': 1.2, 'b': 1.2, 'rho': 1.0, 'c1': 0.3, 
                      'c2': 0.3, 'd': 0.3, 'e1': 0.8, 'e2': 0.8},
            'initial': [0.3, 0.4, 0.2],
            't_span': (0, 300)
        },
        {
            'name': 'Competitive exclusion (boundary equilibrium)',
            'params': {'a': 0.8, 'b': 1.5, 'rho': 1.0, 'c1': 0.8,
                      'c2': 0.2, 'd': 0.4, 'e1': 1.2, 'e2': 0.5},
            'initial': [0.4, 0.4, 0.3],
            't_span': (0, 300)
        },
        {
            'name': 'Stable limit cycle (periodic oscillations)',
            'params': {'a': 1.0, 'b': 1.0, 'rho': 1.0, 'c1': 0.5,
                      'c2': 0.5, 'd': 0.2, 'e1': 2.0, 'e2': 2.0},
            'initial': [0.5, 0.3, 0.4],
            't_span': (0, 500)
        },
        {
            'name': 'Complex oscillations (quasi-periodic or chaotic)',
            'params': {'a': 1.2, 'b': 1.2, 'rho': 1.2, 'c1': 0.6,
                      'c2': 0.6, 'd': 0.1, 'e1': 2.5, 'e2': 2.5},
            'initial': [0.6, 0.4, 0.5],
            't_span': (0, 1000)
        },
        {
            'name': 'Bistability (multiple attractors)',
            'params': {'a': 1.1, 'b': 1.1, 'rho': 1.0, 'c1': 0.4,
                      'c2': 0.4, 'd': 0.3, 'e1': 1.5, 'e2': 1.5},
            'initial': [0.7, 0.2, 0.4],
            't_span': (0, 400)
        },
        {
            'name': 'Stable coexistence (weak competition)',
            'params': {'a': 0.3, 'b': 0.3, 'rho': 1.0, 'c1': 0.2,
                      'c2': 0.2, 'd': 0.6, 'e1': 0.8, 'e2': 0.8},
            'initial': [0.5, 0.5, 0.3],
            't_span': (0, 300)
        }
    ]
    
    all_results = []
    
    for i, ps in enumerate(parameter_sets):
        print(f"\n{'='*80}")
        print(f"Case {i+1}: {ps['name']}")
        print(f"{'='*80}")
        
        model = ComplexEcologicalModel(**ps['params'])
        
        # Analyze equilibria
        print("\nEquilibrium Analysis:")
        equilibria = model.analyze_equilibria()
        for j, eq in enumerate(equilibria):
            analysis = model.analyze_stability(eq)
            print(f"  Equilibrium {j}: {eq}")
            print(f"    Type: {analysis['type']}")
            print(f"    Stability: {analysis['stability']}")
            print(f"    Eigenvalues: {analysis['eigenvalues']}")
        
        # Create figures
        fig, sol = model.plot_3d_trajectory(ps['initial'], t_span=ps['t_span'])
        fig.suptitle(f"{ps['name']}\nParameters: a={ps['params']['a']}, b={ps['params']['b']}, "
                    f"d={ps['params']['d']}, e1={ps['params']['e1']}, e2={ps['params']['e2']}", 
                    fontsize=16, y=1.05)
        
        # Calculate statistics
        u1, u2, v = sol.y
        t = sol.t
        
        # Remove transient (first 20%)
        n_transient = len(t) // 5
        u1_steady = u1[n_transient:]
        u2_steady = u2[n_transient:]
        v_steady = v[n_transient:]
        
        # Calculate mean and std
        mean_u1 = np.mean(u1_steady)
        mean_u2 = np.mean(u2_steady)
        mean_v = np.mean(v_steady)
        
        std_u1 = np.std(u1_steady)
        std_u2 = np.std(u2_steady)
        std_v = np.std(v_steady)
        
        print(f"\nSteady-state Statistics (after transient):")
        print(f"  Species 1: mean = {mean_u1:.4f}, std = {std_u1:.4f}")
        print(f"  Species 2: mean = {mean_u2:.4f}, std = {std_u2:.4f}")
        print(f"  Predator:  mean = {mean_v:.4f}, std = {std_v:.4f}")
        
        # Classify behavior based on statistics
        if std_u1 < 0.001 and std_u2 < 0.001 and std_v < 0.001:
            behavior = "Stable equilibrium"
        elif std_u1 > 0.01 or std_u2 > 0.01 or std_v > 0.01:
            # Check for periodicity
            from scipy.signal import find_peaks
            peaks_u1, _ = find_peaks(u1_steady, height=np.mean(u1_steady))
            peaks_u2, _ = find_peaks(u2_steady, height=np.mean(u2_steady))
            peaks_v, _ = find_peaks(v_steady, height=np.mean(v_steady))
            
            if len(peaks_u1) > 3 and len(peaks_u2) > 3 and len(peaks_v) > 3:
                # Calculate period consistency
                periods_u1 = np.diff(t[n_transient:][peaks_u1])
                period_std_u1 = np.std(periods_u1) / np.mean(periods_u1) if len(periods_u1) > 0 else np.inf
                
                if period_std_u1 < 0.1:  # Consistent periods
                    behavior = f"Periodic oscillations (period ≈ {np.mean(periods_u1):.1f})"
                else:
                    behavior = "Complex/chaotic oscillations"
            else:
                behavior = "Irregular oscillations"
        else:
            behavior = "Damped oscillations approaching equilibrium"
        
        print(f"\nSystem Behavior: {behavior}")
        
        # Estimate Lyapunov exponents for chaotic cases
        if "chaotic" in behavior.lower() or i == 3:  # Case 4 is tuned for chaos
            try:
                exponents = model.calculate_lyapunov_exponents(
                    ps['initial'], t_span=(0, min(ps['t_span'][1], 200))
                )
                print(f"Estimated Lyapunov exponents: {exponents}")
                max_exponent = max(exponents)
                if max_exponent > 0.01:
                    print(f"  Largest Lyapunov exponent: {max_exponent:.4f} > 0 → Chaotic behavior")
            except Exception as e:
                print(f"  Lyapunov exponent calculation failed: {e}")
        
        all_results.append({
            'name': ps['name'],
            'params': ps['params'],
            'means': (mean_u1, mean_u2, mean_v),
            'stds': (std_u1, std_u2, std_v),
            'behavior': behavior,
            'fig': fig
        })
        
        # Save figures
        # fig.savefig(f'complex_model_case_{i+1:02d}.png', dpi=300, bbox_inches='tight')
    
    # Create summary table
    print(f"\n{'='*80}")
    print("SUMMARY OF ALL CASES")
    print(f"{'='*80}")
    
    print("\nCase | Behavior | Species 1 (mean±std) | Species 2 (mean±std) | Predator (mean±std)")
    print("-" * 100)
    
    for i, result in enumerate(all_results):
        print(f"{i+1:2d} | {result['behavior'][:30]:30} | "
              f"{result['means'][0]:.3f}±{result['stds'][0]:.3f} | "
              f"{result['means'][1]:.3f}±{result['stds'][1]:.3f} | "
              f"{result['means'][2]:.3f}±{result['stds'][2]:.3f}")
    
    # Create behavior classification plot
    fig_summary, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    
    for i, result in enumerate(all_results):
        ax = axes[i]
        
        # Create a simple visualization of the behavior
        if "Stable equilibrium" in result['behavior']:
            # Show a point at the mean
            ax.scatter(result['means'][0], result['means'][1], 
                      s=100, c='green', marker='o')
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
        elif "Periodic" in result['behavior']:
            # Show a circle representing oscillations
            circle = plt.Circle((0.5, 0.5), 0.3, color='blue', 
                               fill=False, linewidth=2)
            ax.add_patch(circle)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
        elif "Chaotic" in result['behavior']:
            # Show a fractal-like pattern
            x = np.random.rand(100) * result['stds'][0] + result['means'][0]
            y = np.random.rand(100) * result['stds'][1] + result['means'][1]
            ax.scatter(x, y, s=10, c='red', alpha=0.5)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
        elif "Damped" in result['behavior']:
            # Show a spiral
            t_spiral = np.linspace(0, 4*np.pi, 100)
            x_spiral = 0.5 + 0.3*np.exp(-0.5*t_spiral)*np.cos(t_spiral)
            y_spiral = 0.5 + 0.3*np.exp(-0.5*t_spiral)*np.sin(t_spiral)
            ax.plot(x_spiral, y_spiral, 'orange', linewidth=2)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
        
        ax.set_title(f"Case {i+1}: {result['name'][:20]}...", fontsize=10)
        ax.set_xlabel('Species 1', fontsize=9)
        ax.set_ylabel('Species 2', fontsize=9)
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    fig_summary.suptitle('Behavior Classification of Different Cases', fontsize=16, y=1.05)
    # fig_summary.savefig('behavior_classification_summary.png', dpi=300, bbox_inches='tight')
    
    plt.show()
    
    return all_results

def parameter_sensitivity_analysis():
    """Perform sensitivity analysis on key parameters"""
    
    base_params = {'a': 1.0, 'b': 1.0, 'rho': 1.0, 'c1': 0.5, 
                   'c2': 0.5, 'd': 0.3, 'e1': 1.5, 'e2': 1.5}
    
    # Vary key parameters
    parameters_to_vary = ['d', 'e1', 'a']
    ranges = {
        'd': np.linspace(0.1, 0.8, 20),  # Predator mortality
        'e1': np.linspace(0.5, 3.0, 20),  # Conversion efficiency
        'a': np.linspace(0.1, 2.0, 20),   # Competition coefficient
    }
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    for idx, param_name in enumerate(parameters_to_vary):
        ax = axes[idx]
        param_values = ranges[param_name]
        final_u1 = []
        final_u2 = []
        final_v = []
        behaviors = []
        
        for param_value in param_values:
            params = base_params.copy()
            params[param_name] = param_value
            
            model = ComplexEcologicalModel(**params)
            sol = model.simulate([0.5, 0.3, 0.4], t_span=(0, 500))
            
            u1, u2, v = sol.y
            t = sol.t
            
            # Remove transient
            n_transient = len(t) // 5
            u1_steady = u1[n_transient:]
            u2_steady = u2[n_transient:]
            v_steady = v[n_transient:]
            
            # Calculate statistics
            std_u1 = np.std(u1_steady)
            std_u2 = np.std(u2_steady)
            std_v = np.std(v_steady)
            
            # Classify behavior
            if std_u1 < 0.001 and std_u2 < 0.001 and std_v < 0.001:
                behavior = 0  # Stable
            elif std_u1 > 0.01 or std_u2 > 0.01 or std_v > 0.01:
                behavior = 1  # Oscillatory
            else:
                behavior = 0.5  # Intermediate
            
            final_u1.append(np.mean(u1_steady))
            final_u2.append(np.mean(u2_steady))
            final_v.append(np.mean(v_steady))
            behaviors.append(behavior)
        
        # Plot results
        ax.plot(param_values, final_u1, 'b-', linewidth=2, label='Species 1')
        ax.plot(param_values, final_u2, 'g-', linewidth=2, label='Species 2')
        ax.plot(param_values, final_v, 'r-', linewidth=2, label='Predator')
        
        # Add background color for behavior regions
        for i in range(len(param_values)-1):
            if behaviors[i] == 0 and behaviors[i+1] == 0:
                ax.axvspan(param_values[i], param_values[i+1], 
                          alpha=0.2, color='green')
            elif behaviors[i] == 1 and behaviors[i+1] == 1:
                ax.axvspan(param_values[i], param_values[i+1], 
                          alpha=0.2, color='red')
        
        ax.set_xlabel(param_name, fontsize=12)
        ax.set_ylabel('Steady-state population', fontsize=12)
        ax.set_title(f'Sensitivity to {param_name}', fontsize=14)
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    # fig.savefig('parameter_sensitivity_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

print("Complex Ecological Model Analysis")
print("Exploring diverse dynamical behaviors in competition-predation systems\n")

# Explore diverse dynamics
results = explore_diverse_dynamics()

# Perform parameter sensitivity analysis
print("\n" + "="*80)
print("PARAMETER SENSITIVITY ANALYSIS")
print("="*80)
parameter_sensitivity_analysis()
```

### 2.3.4.3. 动力学行为分类

三维及以上的动力系统可能展现混沌行为。以洛伦兹系统为例：
$$
\begin{aligned}
\frac{dx}{dt} &= \sigma(y - x) \\
\frac{dy}{dt} &= x(\rho - z) - y \\
\frac{dz}{dt} &= xy - \beta z
\end{aligned}
$$

**混沌的特征**：
1. 对初始条件敏感（蝴蝶效应）
2. 有界非周期运动
3. 具有分形结构（分岔图，上一节已经介绍过）

```python-plot
"""
chaos_bifurcation.py
Demonstration of chaos and bifurcation in ecological models
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def lorenz_system(t, state, sigma=10.0, rho=28.0, beta=8/3):
    """Lorenz system - classic chaotic system"""
    x, y, z = state
    
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    
    return [dxdt, dydt, dzdt]

def plot_lorenz_attractor():
    """Plot Lorenz attractor"""
    # Initial conditions
    state0 = [1.0, 1.0, 1.0]
    
    # Time span
    t_span = (0, 100)
    t_eval = np.linspace(t_span[0], t_span[1], 10000)
    
    # Solve ODE
    sol = solve_ivp(lorenz_system, t_span, state0, 
                   t_eval=t_eval, method='RK45', rtol=1e-8)
    
    x, y, z = sol.y
    
    fig = plt.figure(figsize=(14, 10))
    
    # 3D plot
    ax1 = fig.add_subplot(221, projection='3d')
    ax1.plot(x, y, z, '-', linewidth=0.5, alpha=0.7)
    ax1.set_xlabel('X', fontsize=10)
    ax1.set_ylabel('Y', fontsize=10)
    ax1.set_zlabel('Z', fontsize=10)
    ax1.set_title('Lorenz Attractor (3D)', fontsize=12)
    
    # Projections
    ax2 = fig.add_subplot(222)
    ax2.plot(x, y, '-', linewidth=0.5, alpha=0.7)
    ax2.set_xlabel('X', fontsize=10)
    ax2.set_ylabel('Y', fontsize=10)
    ax2.set_title('X-Y Projection', fontsize=12)
    ax2.grid(True, alpha=0.3)
    
    ax3 = fig.add_subplot(223)
    ax3.plot(x, z, '-', linewidth=0.5, alpha=0.7)
    ax3.set_xlabel('X', fontsize=10)
    ax3.set_ylabel('Z', fontsize=10)
    ax3.set_title('X-Z Projection', fontsize=12)
    ax3.grid(True, alpha=0.3)
    
    ax4 = fig.add_subplot(224)
    ax4.plot(y, z, '-', linewidth=0.5, alpha=0.7)
    ax4.set_xlabel('Y', fontsize=10)
    ax4.set_ylabel('Z', fontsize=10)
    ax4.set_title('Y-Z Projection', fontsize=12)
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    # plt.savefig('lorenz_attractor.png', dpi=300, bbox_inches='tight')
    
    # Demonstrate sensitivity to initial conditions
    fig2, axes = plt.subplots(3, 1, figsize=(12, 10))
    
    # Slightly different initial conditions
    state1 = [1.0, 1.0, 1.0]
    state2 = [1.001, 1.0, 1.0]  # 0.1% difference
    
    sol1 = solve_ivp(lorenz_system, (0, 50), state1, 
                    t_eval=np.linspace(0, 50, 5000), method='RK45')
    sol2 = solve_ivp(lorenz_system, (0, 50), state2,
                    t_eval=np.linspace(0, 50, 5000), method='RK45')
    
    time = sol1.t
    
    # Plot comparison
    axes[0].plot(time, sol1.y[0], 'b-', linewidth=1.5, alpha=0.7, label='Initial: (1.0, 1.0, 1.0)')
    axes[0].plot(time, sol2.y[0], 'r--', linewidth=1.5, alpha=0.7, label='Initial: (1.001, 1.0, 1.0)')
    axes[0].set_ylabel('X', fontsize=12)
    axes[0].set_title('Sensitivity to Initial Conditions (X component)', fontsize=14)
    axes[0].legend(fontsize=10)
    axes[0].grid(True, alpha=0.3)
    
    axes[1].plot(time, sol1.y[1], 'b-', linewidth=1.5, alpha=0.7)
    axes[1].plot(time, sol2.y[1], 'r--', linewidth=1.5, alpha=0.7)
    axes[1].set_ylabel('Y', fontsize=12)
    axes[1].grid(True, alpha=0.3)
    
    axes[2].plot(time, sol1.y[2], 'b-', linewidth=1.5, alpha=0.7)
    axes[2].plot(time, sol2.y[2], 'r--', linewidth=1.5, alpha=0.7)
    axes[2].set_xlabel('Time', fontsize=12)
    axes[2].set_ylabel('Z', fontsize=12)
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    # plt.savefig('sensitivity_initial_conditions.png', dpi=300, bbox_inches='tight')
    
    plt.show()

plot_lorenz_attractor()
```

回到主题，这一复杂模型可能展现多种动力学行为，例如：

1. **竞争排斥**：一个猎物物种被淘汰，系统退化为简单的捕食者-猎物系统
2. **捕食者介导的共存**：捕食者通过抑制优势竞争者，为劣势物种创造生存空间
3. **周期振荡**：捕食者-猎物振荡与竞争相互作用耦合
4. **混沌**：三维系统中可能出现对初始条件敏感的非周期行为

```python-plot
"""
complex_ecosystem_schematic.py
绘制复杂生态系统（竞争+捕食）的原理图
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_ivp

def plot_3d_state_space(ax):
    """绘制三维状态空间示意图"""
    
    # 设置视角和比例
    ax.view_init(elev=25, azim=45)
    
    # 创建网格
    u1 = np.linspace(0, 1, 20)
    u2 = np.linspace(0, 1, 20)
    v = np.linspace(0, 1, 20)
    
    # 绘制坐标轴
    ax.set_xlabel('Species 1 ($u_1$)', fontsize=12, labelpad=10)
    ax.set_ylabel('Species 2 ($u_2$)', fontsize=12, labelpad=10)
    ax.set_zlabel('Predator ($v$)', fontsize=12, labelpad=10)
    ax.set_title('3D State Space of Complex Ecosystem', fontsize=16)
    
    # 绘制关键平面
    # 平面1: u1 = 0 (物种1灭绝)
    U2, V = np.meshgrid(u2, v)
    ax.plot_surface(np.zeros_like(U2), U2, V, alpha=0.1, color='red')
    
    # 平面2: u2 = 0 (物种2灭绝)
    U1, V = np.meshgrid(u1, v)
    ax.plot_surface(U1, np.zeros_like(U1), V, alpha=0.1, color='blue')
    
    # 平面3: v = 0 (捕食者灭绝)
    U1, U2 = np.meshgrid(u1, u2)
    ax.plot_surface(U1, U2, np.zeros_like(U1), alpha=0.1, color='green')
    
    # 绘制示例轨迹
    # 轨迹1: 竞争排斥（物种2灭绝）
    t1 = np.linspace(0, 4*np.pi, 200)
    u1_traj1 = 0.5 + 0.3 * np.tanh(t1/2) * np.sin(t1)
    # 收敛到 (u1,0,v) 平面
    u2_traj1 = 0.4 * np.exp(-0.5*t1) 
    v_traj1 = 0.3 + 0.2 * np.cos(t1)
    ax.plot(u1_traj1, u2_traj1, v_traj1, 'r-', linewidth=2.5, label='Competitive exclusion', alpha=0.9)
    # 标注重终点
    ax.scatter(u1_traj1[-1], u2_traj1[-1], v_traj1[-1], color='red', s=50)

    # 轨迹2: 捕食者介导的共存 (螺旋向内或闭合环)
    t2 = np.linspace(0, 6*np.pi, 300)
    # 缓慢收敛的螺旋
    decay = np.exp(-0.05*t2)
    u1_center, u2_center, v_center = 0.4, 0.4, 0.4
    u1_traj2 = u1_center + 0.2 * decay * np.sin(t2)
    u2_traj2 = u2_center + 0.2 * decay * np.sin(t2 + 2*np.pi/3)
    v_traj2 = v_center + 0.2 * decay * np.sin(t2 + 4*np.pi/3)
    ax.plot(u1_traj2, u2_traj2, v_traj2, 'b-', linewidth=2.5, label='Stable coexistence', alpha=0.9)
    # 标注中心点
    ax.scatter(u1_center, u2_center, v_center, color='blue', s=50, marker='*')

    # 轨迹3: 混沌轨迹 (基于 Hastings-Powell 三物种食物链模型)
    # 这也是广义 Lotka-Volterra 系统的一种，以其复杂的混沌吸引子著称
    def ecological_chaos_gen(t_max=5000):
        # 著名的 "Teacup" 混沌吸引子参数 (Hastings & Powell, 1991)
        # x: Resource, y: Consumer, z: Top predator
        
        # 参数
        a1, b1 = 5.0, 3.0    # 资源 -> 消费者
        a2, b2 = 0.1, 2.0    # 消费者 -> 顶层捕食者
        d1 = 0.4             # 消费者死亡率
        d2 = 0.01            # 顶层捕食者死亡率
        
        def equations(t, state):
            x, y, z = state
            # 保护非负性
            if x < 0: x = 0
            if y < 0: y = 0
            if z < 0: z = 0
            
            # 功能反应 (Holling Type II)
            func1 = a1 * x / (1 + b1 * x)
            func2 = a2 * y / (1 + b2 * y)
            
            # 动力学方程
            # dx/dt = x(1-x) - f1(x)y
            dxdt = x * (1 - x) - func1 * y
            # dy/dt = f1(x)y - f2(y)z - d1*y
            dydt = func1 * y - func2 * z - d1 * y
            # dz/dt = f2(y)z - d2*z
            dzdt = func2 * z - d2 * z
            
            return [dxdt, dydt, dzdt]

        # 增加时间跨度以确保能够画出密集的混沌轨道
        t_eval = np.linspace(0, t_max, 20000)
        sol = solve_ivp(equations, [0, t_max], [0.5, 0.1, 9.0], t_eval=t_eval, rtol=1e-8, atol=1e-8)
        
        # 处理数据用于绘图
        # 我们抛弃前 20% 作为瞬态，保留后面的吸引子形状
        start_idx = int(len(sol.t) * 0.2)
        
        x_raw = sol.y[0][start_idx:]
        y_raw = sol.y[1][start_idx:]
        z_raw = sol.y[2][start_idx:]
        
        # 缩放映射到当前绘图坐标系 (0-1)
        # Hastings-Powell 的 x 在 0-1, y 在 0-0.5 左右, z 在 7-10 左右
        u1_out = x_raw 
        u2_out = y_raw * 2.0  # 放大 y 以便看清
        v_out = (z_raw - 4.0) / 8.0 # 将 z 映射到 0-1 范围
        
        return u1_out, u2_out, v_out

    u1_traj3, u2_traj3, v_traj3 = ecological_chaos_gen(t_max=3000)
    ax.plot(u1_traj3, u2_traj3, v_traj3, 'g-', linewidth=0.6, alpha=0.7, label='Chaos')

    ax.legend(fontsize=10, loc='upper right', bbox_to_anchor=(1.1, 1.0))
    
    # 移除背景灰度，使其更干净
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    
    # 添加文本说明盒子
    ax.text2D(0.02, 0.1, 
              'System Behaviors:\n'
              '• Red: Exclusion ($u_2 \\to 0$)\n'
              '• Blue: Stable Point\n'
              '• Green: Strange Attractor',
              transform=ax.transAxes, fontsize=10,
              bbox=dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='gray'))

# 创建复杂生态系统原理图
fig = plt.figure(figsize=(10, 8))

# 三维状态空间
ax1 = fig.add_subplot(111, projection='3d')
plot_3d_state_space(ax1)

plt.tight_layout()
# plt.savefig('complex_ecosystem_schematic.png', dpi=300, bbox_inches='tight')
plt.show()
```

**运行结果说明**：上述代码生成了复杂生态系统的原理图：

- 红色平面：$u_1=0$（物种1灭绝）
- 蓝色平面：$u_2=0$（物种2灭绝）
- 绿色平面：$v=0$（捕食者灭绝）
- 三条示例轨迹展示了不同动力学行为

### 2.3.4.4. 复杂模型的生态学启示

复杂模型揭示了生态系统动力学的几个重要特征：

1. **高阶相互作用**：竞争和捕食的耦合可以产生非直观的结果，如捕食者促进竞争物种共存。
2. **参数敏感性**：系统行为对参数变化高度敏感，微小的参数变化可能导致定性行为改变。
3. **多稳态性**：相同参数下可能存在多个吸引子，最终状态取决于初始条件。
4. **混沌的可能性**：三维及以上系统可能展现混沌行为，对长期预测构成挑战。

## 思考题

1. 使用竞争模型代码，验证参考图中的四种结果。调整参数使得系统分别呈现：
   a) 物种1获胜
   b) 物种2获胜
   c) 不稳定共存
   d) 稳定共存
   对于每种情况，绘制相图并标注平衡点，解释参数条件如何导致该结果。

2. 修改捕食者-猎物模型，加入猎物密度制约（即猎物单独增长为逻辑斯谛型）：
   $$
   \frac{dN}{dt} = rN\left(1-\frac{N}{K}\right) - \varepsilon NP
   $$
   $$
   \frac{dP}{dt} = -\mu P + \theta NP
   $$
   分析平衡点的稳定性。与经典模型相比，密度制约如何改变系统行为？绘制相图和时间序列。

3. 查找经典的哈德逊湾公司猞猁-雪兔数据（或其他捕食者-猎物时间序列数据，或自己生成一份数据），尝试用Lotka-Volterra模型拟合。估计参数并评估模型拟合优度。讨论模型的局限性。

4. 考虑一个包含两个竞争物种和一个捕食者的三物种系统。设计数值实验，探究在什么条件下捕食者可以促进竞争物种的共存。绘制三维相图展示不同动力学状态。
