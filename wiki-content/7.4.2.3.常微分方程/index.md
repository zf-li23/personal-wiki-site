**内容**：ODE的建立（质量作用定律）；数值求解（欧拉法，`scipy.integrate.odeint`）；相图与相轨迹的几何直观。

在前两节中，我们分别探讨了离散时间系统（Leslie矩阵、逻辑斯谛映射）和连续时间系统（逻辑斯谛增长）。这些模型都描述了生物系统中的动态行为。本节将进一步深入**连续时间动力系统**，重点介绍常微分方程（ODE）模型的建立、分析与可视化方法。我们将以生态学中的经典模型——Lotka-Volterra竞争模型和捕食者-猎物模型为例，展示ODE建模的全过程。

## 2.3.1.Lotka-Volterra种间竞争模型

在真实生态系统中，物种很少孤立存在。它们为有限资源而竞争。Lotka-Volterra竞争模型扩展了单物种逻辑斯谛增长，描述了两个物种竞争同一资源时的动态。

### 模型建立

假设两个物种的种群数量分别为 $N_1(t)$ 和 $N_2(t)$。每个物种单独存在时遵循逻辑斯谛增长：
$$
\begin{split}
\frac{dN_1}{dt} = r_1 N_1 \left(1 - \frac{N_1}{K_1}\right) \\
\frac{dN_2}{dt} = r_2 N_2 \left(1 - \frac{N_2}{K_2}\right)
\end{split}
$$
其中 $r_i$ 为物种 $i$ 的内禀增长率，$K_i$ 为其环境容纳量。

当两个物种共存时，它们相互竞争资源。竞争效应通过**竞争系数** $\alpha$ 和 $\beta$ 量化：
- $\alpha$：每个 $N_2$ 个体对物种1增长的抑制效应，相当于 $\alpha$ 个 $N_1$ 个体。
- $\beta$：每个 $N_1$ 个体对物种2增长的抑制效应，相当于 $\beta$ 个 $N_2$ 个体。

完整的竞争模型为：
$$
\begin{aligned}
\frac{dN_1}{dt} &= r_1 N_1 \left(1 - \frac{N_1}{K_1} - \frac{\alpha N_2}{K_1}\right) \\
\frac{dN_2}{dt} &= r_2 N_2 \left(1 - \frac{N_2}{K_2} - \frac{\beta N_1}{K_2}\right)
\end{aligned}
$$

### 平衡点与零增长线

平衡点（稳态）是系统不再变化的状态，即满足 $\frac{dN_1}{dt} = \frac{dN_2}{dt} = 0$。从上述方程，我们可以得到四个可能的平衡点：
1. $(0, 0)$：两个物种均灭绝。
2. $(K_1, 0)$：物种1达到容纳量，物种2灭绝。
3. $(0, K_2)$：物种2达到容纳量，物种1灭绝。
4. $\left(\frac{K_1 - \alpha K_2}{1 - \alpha\beta}, \frac{K_2 - \beta K_1}{1 - \alpha\beta}\right)$：两个物种共存（要求该点各分量为正）。

为了直观理解系统动态，我们绘制**零增长线**（nullcline），即满足 $\frac{dN_1}{dt} = 0$ 或 $\frac{dN_2}{dt} = 0$ 的曲线。对于物种1，$\frac{dN_1}{dt} = 0$ 给出：
$$
N_1 = 0 \quad \text{或} \quad N_1 = K_1 - \alpha N_2
$$
同样，物种2的零增长线为：
$$
N_2 = 0 \quad \text{或} \quad N_2 = K_2 - \beta N_1
$$
这些直线将相平面划分为不同区域，在每个区域内，$N_1$ 和 $N_2$ 的变化方向（增加或减少）是确定的。

### Python实现：相图与动态模拟

以下代码实现Lotka-Volterra竞争模型，绘制相图（包括零增长线、向量场和轨迹），并分析平衡点稳定性。

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
    
    def __init__(self, a=0.5, b=0.5, rho=1.0):
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
    
    def plot_nullclines(self, ax, x_max=1.2, y_max=1.2):
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
    
    def plot_vector_field(self, ax, x_max=1.2, y_max=1.2, density=20):
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
            if 0 <= x <= 1.2 and 0 <= y <= 1.2:
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
        [0.2, 0.2],
        [0.8, 0.2],
        [0.2, 0.8],
        [0.6, 0.6]
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
plt.savefig('competition_case1.png', dpi=300, bbox_inches='tight')

# Case 2: Species 2 wins (a > 1, b < 1)
print("\nCase 2: Species 2 wins")
fig2, model2 = create_competition_figure(a=1.5, b=0.5, case_name="Species 2 wins")
plt.savefig('competition_case2.png', dpi=300, bbox_inches='tight')

# Case 3: Stable coexistence (a < 1, b < 1)
print("\nCase 3: Stable coexistence")
fig3, model3 = create_competition_figure(a=0.5, b=0.5, case_name="Stable coexistence")
plt.savefig('competition_case3.png', dpi=300, bbox_inches='tight')

# Case 4: Unstable coexistence (a > 1, b > 1)
print("\nCase 4: Unstable coexistence (competitive exclusion)")
fig4, model4 = create_competition_figure(a=1.5, b=1.5, case_name="Unstable coexistence")
plt.savefig('competition_case4.png', dpi=300, bbox_inches='tight')

plt.show()

# Print equilibrium analysis for each case
print("\n" + "="*60)
print("EQUILIBRIUM ANALYSIS")
print("="*60)

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

### 稳定性分析

平衡点的稳定性通过**雅可比矩阵**的特征值分析。对于二维系统，雅可比矩阵 $J$ 在平衡点 $(N_1^*, N_2^*)$ 处的特征值 $\lambda$ 满足特征方程：
$$
\det(J - \lambda I) = 0
$$
稳定性判据：
- 若两个特征值的实部均小于零，平衡点是**稳定**的（吸引子）。
- 若有特征值的实部大于零，平衡点是**不稳定**的。
- 若特征值为纯虚数，平衡点可能是**中心**（中性稳定）。

对于竞争模型，四种可能的结果（如参考图片所示）取决于参数关系：
1. **物种1获胜**：$K_1 > K_2/\beta$ 且 $K_2 < K_1/\alpha$
2. **物种2获胜**：$K_2 > K_1/\alpha$ 且 $K_1 < K_2/\beta$
3. **不稳定共存**：$K_1 > K_2/\beta$ 且 $K_2 > K_1/\alpha$
4. **稳定共存**：$K_1 < K_2/\beta$ 且 $K_2 < K_1/\alpha$

## 2.3.2.Lotka-Volterra捕食者-猎物模型

捕食者-猎物相互作用是生态学中的另一经典场景。Lotka-Volterra捕食者-猎物模型描述了捕食者和猎物种群之间的振荡动态。

### 模型建立

设 $N(t)$ 为猎物种群数量，$P(t)$ 为捕食者种群数量。模型假设：
1. 没有捕食者时，猎物以指数速率 $r$ 增长。
2. 没有猎物时，捕食者以指数速率 $-m$ 减少（$m>0$）。
3. 捕食者与猎物的相遇导致猎物被捕食，同时促进捕食者增长。

模型方程为：
$$
\begin{aligned}
\frac{dN}{dt} &= rN - \varepsilon NP \\
\frac{dP}{dt} &= -\mu P + \theta NP
\end{aligned}
$$
其中：
- $r$：猎物的内禀增长率。
- $\varepsilon$：捕食者的捕食效率（单位捕食者单位时间捕获的猎物数）。
- $\mu$：捕食者的死亡率。
- $\theta$：捕食者将猎物转化为自身繁殖的效率。

### 平衡点与零增长线

零增长线：
- 猎物：$\frac{dN}{dt} = 0 \Rightarrow N = 0$ 或 $P = \frac{r}{\varepsilon}$
- 捕食者：$\frac{dP}{dt} = 0 \Rightarrow P = 0$ 或 $N = \frac{\mu}{\theta}$

平衡点：
1. $(0, 0)$：灭绝。
2. $\left(\frac{\mu}{\theta}, \frac{r}{\varepsilon}\right)$：共存平衡点。

### 稳定性分析：极限环与中心

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
特征值为 $\lambda = \pm i\sqrt{r\mu}$，为纯虚数，表明该平衡点是**中心**。在非线性系统中，这通常意味着存在**周期解**（极限环）。

### Python实现：捕食者-猎物模型的相图与时间序列

```python
class PredatorPreyLV:
    """Lotka-Volterra捕食者-猎物模型"""
    
    def __init__(self, r, epsilon, mu, theta):
        self.r = r
        self.epsilon = epsilon
        self.mu = mu
        self.theta = theta
    
    def equations(self, t, NP):
        """定义微分方程"""
        N, P = NP
        dNdt = self.r * N - self.epsilon * N * P
        dPdt = -self.mu * P + self.theta * N * P
        return [dNdt, dPdt]
    
    def plot_phase_portrait(self, N_max=None, P_max=None, n_grid=25, trajectories=None):
        """绘制相图"""
        if N_max is None:
            N_max = 2 * self.mu / self.theta
        if P_max is None:
            P_max = 2 * self.r / self.epsilon
        
        # 创建网格
        N = np.linspace(0.1, N_max, n_grid)
        P = np.linspace(0.1, P_max, n_grid)
        N_grid, P_grid = np.meshgrid(N, P)
        
        # 计算向量场
        dN, dP = np.zeros_like(N_grid), np.zeros_like(P_grid)
        for i in range(n_grid):
            for j in range(n_grid):
                dNP = self.equations(0, [N_grid[i,j], P_grid[i,j]])
                dN[i,j] = dNP[0]
                dP[i,j] = dNP[1]
        
        # 归一化
        norm = np.sqrt(dN**2 + dP**2)
        mask = norm > 0
        dN[mask] = dN[mask] / norm[mask]
        dP[mask] = dP[mask] / norm[mask]
        
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))
        
        # 左图：相图
        ax1 = axes[0]
        ax1.quiver(N_grid, P_grid, dN, dP, color='gray', alpha=0.6, 
                   angles='xy', scale_units='xy', scale=15, width=0.005)
        
        # 零增长线
        # 猎物零增长线: N = 0 或 P = r/epsilon
        P_nullcline = np.full_like(N, self.r/self.epsilon)
        ax1.plot(N, P_nullcline, 'r-', linewidth=2, label='Prey nullcline ($dN/dt=0$)')
        
        # 捕食者零增长线: P = 0 或 N = mu/theta
        N_nullcline = np.full_like(P, self.mu/self.theta)
        ax1.plot(N_nullcline, P, 'b-', linewidth=2, label='Predator nullcline ($dP/dt=0$)')
        
        # 平衡点
        N_star = self.mu / self.theta
        P_star = self.r / self.epsilon
        ax1.plot(N_star, P_star, 'go', markersize=10, label='Equilibrium')
        ax1.text(N_star+0.02*N_max, P_star+0.02*P_max, 
                f'({N_star:.1f}, {P_star:.1f})', fontsize=10)
        
        # 绘制轨迹
        if trajectories:
            colors = plt.cm.viridis(np.linspace(0, 1, len(trajectories)))
            for i, (NP0, t_span) in enumerate(trajectories):
                sol = solve_ivp(self.equations, t_span, NP0, 
                                t_eval=np.linspace(t_span[0], t_span[1], 1000),
                                method='RK45')
                ax1.plot(sol.y[0], sol.y[1], '-', color=colors[i], linewidth=1.5, 
                        label=f'Trajectory {i+1}')
                ax1.plot(NP0[0], NP0[1], 'o', color=colors[i], markersize=6)
        
        ax1.set_xlabel('Prey population ($N$)', fontsize=14)
        ax1.set_ylabel('Predator population ($P$)', fontsize=14)
        ax1.set_title('Predator-Prey Phase Portrait', fontsize=16)
        ax1.set_xlim([0, N_max])
        ax1.set_ylim([0, P_max])
        ax1.grid(True, alpha=0.3)
        ax1.legend(fontsize=12)
        
        # 右图：时间序列
        ax2 = axes[1]
        if trajectories:
            for i, (NP0, t_span) in enumerate(trajectories):
                sol = solve_ivp(self.equations, t_span, NP0, 
                                t_eval=np.linspace(t_span[0], t_span[1], 1000),
                                method='RK45')
                time = sol.t
                N_t, P_t = sol.y
                ax2.plot(time, N_t, '-', color='blue', alpha=0.7, linewidth=1.5, 
                        label='Prey' if i==0 else None)
                ax2.plot(time, P_t, '-', color='red', alpha=0.7, linewidth=1.5,
                        label='Predator' if i==0 else None)
        
        ax2.set_xlabel('Time', fontsize=14)
        ax2.set_ylabel('Population', fontsize=14)
        ax2.set_title('Population Time Series', fontsize=16)
        ax2.legend(fontsize=12)
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig, axes

# 示例：经典捕食者-猎物模型
print("Predator-Prey Model")
model_pp = PredatorPreyLV(r=1.0, epsilon=0.1, mu=0.5, theta=0.05)

# 模拟不同初始条件的轨迹
trajectories_pp = [
    ([10, 5], [0, 100]),
    ([20, 15], [0, 100]),
    ([5, 20], [0, 100])
]

fig_pp, axes_pp = model_pp.plot_phase_portrait(N_max=60, P_max=30, trajectories=trajectories_pp)
plt.show()

# 计算平衡点处的雅可比矩阵和特征值
N_star = model_pp.mu / model_pp.theta
P_star = model_pp.r / model_pp.epsilon
J_star = np.array([[0, -model_pp.epsilon*N_star],
                   [model_pp.theta*P_star, 0]])
eigvals = np.linalg.eigvals(J_star)
print(f"Equilibrium: ({N_star:.1f}, {P_star:.1f})")
print(f"Jacobian at equilibrium:\n{J_star}")
print(f"Eigenvalues: {eigvals}")
print(f"Period of oscillation: {2*np.pi/np.abs(np.imag(eigvals[0])):.2f} time units")
```

## 思考题

1. **竞争模型的四种结果**：
   - 使用竞争模型代码，验证参考图片中的四种结果。调整参数使得系统分别呈现：
     a) 物种1获胜
     b) 物种2获胜
     c) 不稳定共存
     d) 稳定共存
   - 对于每种情况，绘制相图并标注平衡点，解释参数条件如何导致该结果。

2. **捕食者-猎物模型的周期振荡**：
   - 修改捕食者-猎物模型，加入猎物密度制约（即猎物单独增长为逻辑斯谛型）：
     $$
     \frac{dN}{dt} = rN\left(1-\frac{N}{K}\right) - \varepsilon NP
     $$
     $$
     \frac{dP}{dt} = -\mu P + \theta NP
     $$
   - 分析平衡点的稳定性。与经典模型相比，密度制约如何改变系统行为？绘制相图和时间序列。

3. **李雅普诺夫指数与混沌**：
   - 对于逻辑斯谛映射，计算 $r = 3.5$ 和 $r = 4.0$ 时的李雅普诺夫指数。哪个是混沌的？
   - 尝试计算Hénon映射（二维离散系统）的李雅普诺夫指数。代码框架如下：
     $$
     \begin{cases}
     x_{n+1} = 1 - a x_n^2 + y_n \\
     y_{n+1} = b x_n
     \end{cases}
     $$
     取 $a=1.4, b=0.3$。提示：需要计算雅可比矩阵并沿轨道乘积。

4. **实际数据拟合**：
   - 查找经典的哈德逊湾公司猞猁-雪兔数据（或其他捕食者-猎物时间序列数据），尝试用Lotka-Volterra模型拟合。估计参数并评估模型拟合优度。讨论模型的局限性。

通过本节，你应掌握常微分方程模型的建立、相图分析、平衡点稳定性判断，以及混沌检测的基本方法。