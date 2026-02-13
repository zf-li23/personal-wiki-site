# 2.4 偏微分方程：反应-扩散模型

在上一节中，我们讨论了常微分方程描述的种群动态，它们假设了空间是同质性的，仅关注时间变化，忽略了种群在空间中的分布与移动。然而，现实生态系统中的个体总是在空间中活动，种群密度不仅随时间变化，也随空间位置而改变，且空间为非均匀环境。为了刻画这种时空动态，我们需要引入偏微分方程（Partial Differential Equations，PDEs）。偏微分方程将时间导数和空间导数结合在一起，能够描述种群密度的演化过程，是空间生态学最重要的数学工具之一。楼元教授在综述《空间生态学中的一些反应扩散方程模型》中系统阐述了该领域的理论基础与应用，本章将结合该综述的内容，深入介绍反应-扩散模型及其数值方法。

## 2.4.1 偏微分方程的基本理论

### 2.4.1.1 从常微分方程到偏微分方程

常微分方程描述的是因变量（如种群密度）仅随时间的变化，忽略了空间维度。引入空间变量后，密度函数成为时间和空间的函数：$u(t,\boldsymbol{x})$，其中 $\boldsymbol{x}\in\Omega\subset\mathbb{R}^n$ 是空间坐标。一个典型的时空偏微分方程具有如下形式：

$$
F\left(t,\boldsymbol{x},u,\frac{\partial u}{\partial t},\frac{\partial u}{\partial x_1},\ldots,\frac{\partial^2 u}{\partial x_1^2},\ldots\right)=0.
$$

例如，在生态学中我们通常关注的 **反应-扩散方程（Reaction-Diffusion Equations）**，它由两项构成：
- **反应项** $f(u)$：描述局部种群动态（出生、死亡、种内与种间相互作用）；
- **扩散项** $D\nabla^2 u$：描述个体的随机移动，其中 $D>0$ 是扩散系数，$\nabla^2$ 是拉普拉斯算子，也写作 $\Delta$。

对于一维空间，方程写作
$$
\frac{\partial u}{\partial t}=D\frac{\partial^2 u}{\partial x^2}+f(u);
$$
对于二维空间，
$$
\frac{\partial u}{\partial t}=D\left(\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}\right)+f(u)=D\nabla^2 u+f(u).
$$

### 2.4.1.2 有限差分法基础

大多数反应-扩散方程无法求得解析解，必须借助数值方法。**有限差分法（Finite Difference Method）** 是最常用的离散化方法之一，其核心思想是用差商近似导数，将连续的偏微分方程转化为离散的代数方程组。

将空间区间 $[0,L]$ 划分为均匀网格，步长 $\Delta x$，网格点 $x_i=i\Delta x$（$i=0,1,\ldots,N$）。同样时间离散为 $t_n=n\Delta t$。记 $u_i^n\approx u(x_i,t_n)$。

一阶导数的差分近似：
- 向前差分：$\displaystyle \frac{\partial u}{\partial x}\approx\frac{u_{i+1}^n-u_i^n}{\Delta x}$，
- 向后差分：$\displaystyle \frac{\partial u}{\partial x}\approx\frac{u_i^n-u_{i-1}^n}{\Delta x}$，
- 中心差分：$\displaystyle \frac{\partial u}{\partial x}\approx\frac{u_{i+1}^n-u_{i-1}^n}{2\Delta x}$。

二阶导数的中心差分：
$$
\frac{\partial^2 u}{\partial x^2}\approx\frac{u_{i+1}^n-2u_i^n+u_{i-1}^n}{(\Delta x)^2}.
$$

对于二维情况，若空间步长 $\Delta x=\Delta y=h$，则拉普拉斯算子的 **五点差分格式** 为
$$
\nabla^2 u_{i,j}\approx\frac{u_{i+1,j}+u_{i-1,j}+u_{i,j+1}+u_{i,j-1}-4u_{i,j}}{h^2}.
$$

```python-plot
"""
plot_fd_scheme.py
绘制有限差分法网格与差分格式的示意图
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_fd_grid():
    """绘制时空计算网格示意图"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    nx = 6
    nt = 5
    dx = 1.0
    dt = 1.0
    
    # 绘制网格线
    for i in range(nx + 1):
        ax.axvline(x=i*dx, color='gray', linestyle='--', alpha=0.3)
    for n in range(nt + 1):
        ax.axhline(y=n*dt, color='gray', linestyle='--', alpha=0.3)
        
    # 绘制节点
    for i in range(nx + 1):
        for n in range(nt + 1):
            ax.plot(i*dx, n*dt, 'ko', markersize=4, alpha=0.5)
            
    # 标记重点计算分子 (Molecule) - 显式格式
    # u_i^{n+1} 取决于 u_{i-1}^n, u_i^n, u_{i+1}^n
    cx, cy = 3*dx, 3*dt  # 中心点 (i, n)
    
    # 下一层三个点 (n)
    ax.plot([cx-dx, cx, cx+dx], [cy-dt, cy-dt, cy-dt], 'ro-', markersize=8, label='known $t_n$')
    # 上一层一个点 (n+1)
    ax.plot(cx, cy, 'bo', markersize=8, label='unknown $t_{n+1}$')
    
    # 连线
    ax.plot([cx-dx, cx], [cy-dt, cy], 'g-', alpha=0.5)
    ax.plot([cx, cx], [cy-dt, cy], 'g-', alpha=0.5)
    ax.plot([cx+dx, cx], [cy-dt, cy], 'g-', alpha=0.5)
    
    # 文本标注
    offset = 0.15
    ax.text(cx, cy + offset, '$(x_i, t_{n+1})$', ha='center', color='blue', fontsize=12, fontweight='bold')
    ax.text(cx, cy-dt - offset, '$(x_i, t_n)$', ha='center', color='red', fontsize=12)
    ax.text(cx-dx, cy-dt - offset, '$(x_{i-1}, t_n)$', ha='center', color='red', fontsize=12)
    ax.text(cx+dx, cy-dt - offset, '$(x_{i+1}, t_n)$', ha='center', color='red', fontsize=12)
    
    # 坐标轴标签
    ax.set_xlabel('Space $x$', fontsize=14)
    ax.set_ylabel('Time $t$', fontsize=14)
    ax.set_title('Finite Difference Method: Schematic of the Explicit Euler Scheme', fontsize=16)
    
    # 自定义刻度
    ax.set_xticks([i*dx for i in range(nx+1)])
    ax.set_xticklabels([f'$x_{i}$' for i in range(nx+1)])
    ax.set_yticks([n*dt for n in range(nt+1)])
    ax.set_yticklabels([f'$t_{n}$' for n in range(nt+1)])
    
    # 移除顶部和右侧脊柱
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    ax.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('fd_grid_scheme.png', dpi=300)
    print("已保存: fd_grid_scheme.png")
    # plt.show() # 用户不要求运行

def plot_stencils():
    """绘制一维和二维导数的差分模版 (Stencil)"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # 1. 二阶导数中心差分 (1D Laplace)
    ax = axes[0]
    ax.set_aspect('equal')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 1)
    ax.axis('off')
    
    # 点
    points = [(-1, 0), (0, 0), (1, 0)]
    labels = ['$i-1$', '$i$', '$i+1$']
    coeffs = ['$1$', '$-2$', '$1$']
    
    # 连线
    ax.plot([-1, 1], [0, 0], 'k-', lw=2)
    
    for (x, y), label, coeff in zip(points, labels, coeffs):
        # 节点圆圈
        circle = patches.Circle((x, y), 0.2, facecolor='white', edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        # 节点索引
        ax.text(x, y - 0.4, label, ha='center', va='top', fontsize=14)
        # 系数
        ax.text(x, y, coeff, ha='center', va='center', fontsize=14, fontweight='bold')
        
    ax.text(0, 0.6, r'$\frac{\partial^2 u}{\partial x^2} \approx \frac{1}{\Delta x^2} \times$', 
            ha='center', fontsize=16)
    ax.set_title('One-dimensional second-order derivative central difference template', fontsize=14)
    
    # 2. 二维拉普拉斯算子五点差分 (2D Laplace)
    ax = axes[1]
    ax.set_aspect('equal')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.axis('off')
    
    # 网格线
    ax.plot([-1.5, 1.5], [0, 0], 'k--', lw=1, alpha=0.3)
    ax.plot([0, 0], [-1.5, 1.5], 'k--', lw=1, alpha=0.3)
    
    # 连线 (十字)
    ax.plot([-1, 1], [0, 0], 'k-', lw=2)
    ax.plot([0, 0], [-1, 1], 'k-', lw=2)
    
    points = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
    labels = ['$(i,j)$', '$(i-1,j)$', '$(i+1,j)$', '$(i,j+1)$', '$(i,j-1)$']
    coeffs = ['$-4$', '$1$', '$1$', '$1$', '$1$']
    
    for (x, y), label, coeff in zip(points, labels, coeffs):
        # 节点圆圈
        circle = patches.Circle((x, y), 0.25, facecolor='white', edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        # 节点索引
        # 对于中心点，标签放左下方一点，避免重叠
        if x==0 and y==0:
            ax.text(x + 0.3, y - 0.3, label, ha='left', va='top', fontsize=12)
        elif x == 0: # 垂直轴点
            ax.text(x + 0.3, y, label, ha='left', va='center', fontsize=12)
        else: # 水平轴点
            ax.text(x, y - 0.4, label, ha='center', va='top', fontsize=12)
            
        # 系数
        ax.text(x, y, coeff, ha='center', va='center', fontsize=14, fontweight='bold')

    ax.text(0, 1.6, r'$\nabla^2 u \approx \frac{1}{h^2} \times$', 
            ha='center', fontsize=16)
    ax.set_title('Two-dimensional Laplacian five-point difference template', fontsize=14)
    
    plt.tight_layout()
    plt.savefig('fd_stencils.png', dpi=300)
    print("已保存: fd_stencils.png")

plot_fd_grid()
plot_stencils()
```

以一维反应-扩散方程 $\partial_t u = D\partial_{xx}u+f(u)$ 为例，常见的时间推进格式有：

* **显式欧拉格式**（Explicit Euler）：
  $$
  u_i^{n+1}=u_i^n+\Delta t\left(D\frac{u_{i+1}^n-2u_i^n+u_{i-1}^n}{(\Delta x)^2}+f(u_i^n)\right).
  $$
  该格式简单易实现，但稳定性受 **CFL条件** 约束：$D\Delta t/(\Delta x)^2\leq 1/2$（一维）。若步长过大，数值解会发散。

* **隐式欧拉格式**（Implicit Euler）：
  $$
  u_i^{n+1}=u_i^n+\Delta t\left(D\frac{u_{i+1}^{n+1}-2u_i^{n+1}+u_{i-1}^{n+1}}{(\Delta x)^2}+f(u_i^{n+1})\right).
  $$
  隐式格式无条件稳定，但每步需解线性方程组（若 $f$ 非线性还需迭代），计算量较大。

* **Crank-Nicolson格式**：取显式与隐式的平均，时间精度为二阶：
  $$
  \begin{aligned}
  u_i^{n+1}=u_i^n+\frac{\Delta t}{2}&\left[D\frac{u_{i+1}^{n+1}-2u_i^{n+1}+u_{i-1}^{n+1}}{(\Delta x)^2}+D\frac{u_{i+1}^n-2u_i^n+u_{i-1}^n}{(\Delta x)^2}\right.\\
  &\left.+f(u_i^{n+1})+f(u_i^n)\right].
  \end{aligned}
  $$
  Crank-Nicolson格式也是无条件稳定且精度较高，但同样需要求解方程组。

* **IMEX方法**（Implicit-Explicit）：对扩散项用隐式处理，对反应项用显式处理，可在保证稳定性的同时避免非线性迭代。

在有限区域 $\Omega$ 上求解PDE时，必须指定边界条件，常见类型有：

* **狄利克雷边界条件（Dirichlet）**：直接给定边界上的函数值，如 $u(0,t)=g_1(t)$。
* **诺伊曼边界条件（Neumann）**：给定边界上的外法向导数（即通量），如 $\dfrac{\partial u}{\partial\nu}=h(t)$。特别地，**零流边界** $\dfrac{\partial u}{\partial\nu}=0$ 表示边界封闭，个体不能进出。
* **周期边界条件**：适用于空间环状区域，要求 $u(0,t)=u(L,t)$ 且 $\dfrac{\partial u}{\partial x}(0,t)=\dfrac{\partial u}{\partial x}(L,t)$。

## 2.4.2 扩散方程与反应-扩散方程

### 2.4.2.1 纯扩散方程

纯扩散方程 $\partial_t u = D\partial_{xx}u$ 描述热量传导或物质扩散过程，其解析解可通过傅里叶级数或分离变量法得到。在生态学中，它对应于没有局部增长、仅个体随机移动的情形。

扩散现象基于 **菲克定律（Fick’s law）**：扩散通量与密度梯度成正比，且方向从高密度指向低密度。在一维情形，通量 $J$ 可表示为
$$
J=-D\frac{\partial u}{\partial x}.
$$
负号表示扩散方向与梯度方向相反。结合 **连续性方程** $\dfrac{\partial u}{\partial t}=-\dfrac{\partial J}{\partial x}$，得到纯粹扩散方程
$$
\frac{\partial u}{\partial t}=D\frac{\partial^2 u}{\partial x^2}.
$$
该方程描述了种群因随机运动而逐渐均匀分布的过程。

在数值方法下，对于显式格式，一维扩散方程的稳定性条件为
$$
D\frac{\Delta t}{(\Delta x)^2}\le\frac{1}{2}.
$$
二维情形（$\Delta x=\Delta y=h$）条件更严格：
$$
D\Delta t\left(\frac{1}{h^2}+\frac{1}{h^2}\right)=\frac{2D\Delta t}{h^2}\le\frac{1}{2}\quad\Longrightarrow\quad\frac{D\Delta t}{h^2}\le\frac{1}{4}.
$$
当反应项存在时，稳定性条件可能更复杂，通常需通过线性化分析（如von Neumann分析）确定。

```python-plot
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Diffusion1D:
    """一维扩散方程求解器"""
    
    def __init__(self, D, L, T, nx=101, nt=1000):
        """
        参数:
            D: 扩散系数
            L: 空间区域长度
            T: 总时间
            nx: 空间网格点数
            nt: 时间步数
        """
        self.D = D
        self.L = L
        self.T = T
        self.nx = nx
        self.nt = nt
        
        # 空间和时间步长
        self.dx = L / (nx - 1)
        self.dt = T / nt
        
        # 网格
        self.x = np.linspace(0, L, nx)
        
        # 稳定性检查
        stability = D * self.dt / (self.dx ** 2)
        if stability > 0.5:
            print(f"警告：稳定性参数 s = {stability:.3f} > 0.5，解可能不稳定")
            print(f"建议：减小 dt 或增大 dx")
        
    def solve_explicit(self, u0_func, boundary_conditions):
        """
        显式有限差分法求解
        
        参数:
            u0_func: 初始条件函数 u0(x)
            boundary_conditions: 边界条件字典，如 {'left': 'dirichlet', 'right': 'neumann'}
        
        返回:
            u: 解数组 (nt+1, nx)
        """
        # 初始化
        u = np.zeros((self.nt + 1, self.nx))
        u[0, :] = u0_func(self.x)
        
        # 扩散常数
        s = self.D * self.dt / (self.dx ** 2)
        
        # 时间迭代
        for n in range(self.nt):
            # 内部点更新
            for i in range(1, self.nx - 1):
                u[n+1, i] = u[n, i] + s * (u[n, i+1] - 2*u[n, i] + u[n, i-1])
            
            # 边界条件
            if boundary_conditions.get('left') == 'dirichlet':
                u[n+1, 0] = boundary_conditions.get('left_value', 0)
            elif boundary_conditions.get('left') == 'neumann':
                # 一阶零通量边界条件
                u[n+1, 0] = u[n+1, 1]
            
            if boundary_conditions.get('right') == 'dirichlet':
                u[n+1, -1] = boundary_conditions.get('right_value', 0)
            elif boundary_conditions.get('right') == 'neumann':
                u[n+1, -1] = u[n+1, -2]
        
        return u
    
    def solve_diffusion_growth(self, u0_func, r, K, boundary_conditions):
        """
        求解扩散-生长方程
        """
        # 初始化
        u = np.zeros((self.nt + 1, self.nx))
        u[0, :] = u0_func(self.x)
        
        # 扩散常数
        s = self.D * self.dt / (self.dx ** 2)
        
        # 时间迭代
        for n in range(self.nt):
            # 内部点更新
            for i in range(1, self.nx - 1):
                diffusion = s * (u[n, i+1] - 2*u[n, i] + u[n, i-1])
                growth = self.dt * r * u[n, i] * (1 - u[n, i] / K)
                u[n+1, i] = u[n, i] + diffusion + growth
            
            # 边界条件
            if boundary_conditions.get('left') == 'dirichlet':
                u[n+1, 0] = boundary_conditions.get('left_value', 0)
            elif boundary_conditions.get('left') == 'neumann':
                u[n+1, 0] = u[n+1, 1]
            
            if boundary_conditions.get('right') == 'dirichlet':
                u[n+1, -1] = boundary_conditions.get('right_value', 0)
            elif boundary_conditions.get('right') == 'neumann':
                u[n+1, -1] = u[n+1, -2]
        
        return u

class Diffusion2D:
    """二维扩散方程求解器 (用于演示稳定性)"""
    
    def __init__(self, D, L, T, nx=51, nt=1000):
        self.D = D
        self.L = L
        self.nx = nx
        self.ny = nx
        self.nt = nt
        
        self.h = L / (nx - 1)
        self.dt = T / nt
        
        self.x = np.linspace(0, L, nx)
        self.y = np.linspace(0, L, nx)
        self.X, self.Y = np.meshgrid(self.x, self.y)
        
        # 稳定性参数
        self.nu = D * self.dt / (self.h ** 2)
        print(f"  [2D Setup] D={D}, dt={self.dt:.4f}, h={self.h:.4f}")
        print(f"  稳定性参数 nu = D*dt/h^2 = {self.nu:.4f}")
        if self.nu > 0.25:
            print("  -> 警告: 超过二维显式格式稳定性极限 (0.25)")
        else:
            print("  -> 稳定性条件满足 (<= 0.25)")

    def solve_explicit_initial_step(self, u0_func, steps=None):
        """仅运行指定步数，用于演示"""
        if steps is None:
            steps = self.nt
            
        u = u0_func(self.X, self.Y)
        nu = self.nu
        
        for n in range(steps):
            u_new = u.copy()
            
            # 使用切片计算拉普拉斯算子
            u_center = u[1:-1, 1:-1]
            u_left   = u[1:-1, :-2]
            u_right  = u[1:-1, 2:]
            u_top    = u[:-2, 1:-1]
            u_bottom = u[2:, 1:-1]
            
            laplacian = (u_left + u_right + u_top + u_bottom - 4 * u_center)
            u_new[1:-1, 1:-1] = u_center + nu * laplacian
            
            # Neumann边界
            u_new[0, :] = u_new[1, :]
            u_new[-1, :] = u_new[-2, :]
            u_new[:, 0] = u_new[:, 1]
            u_new[:, -1] = u_new[:, -2]
            
            u = u_new
            
            # 如果数值爆炸，提前停止并返回当前状态
            if np.max(np.abs(u)) > 1e10:
                # 归一化以便绘图看到模式
                return u
                
        return u

# 示例1：纯扩散过程 (1D)
print("示例1：一维纯扩散过程")
# 修改 D 以满足稳定性条件 s <= 0.5
# 原来 D=0.5, L=10, nx=201 -> dx=0.05, dx^2=0.0025. T=2, nt=500 -> dt=0.004
# s = 0.5 * 0.004 / 0.0025 = 0.8 > 0.5 ( unstable )
# 减小 dt: nt=1000 -> dt=0.002 -> s=0.4 < 0.5
L = 10.0  # 空间区域长度
T = 2.0   # 总时间
D = 0.5   # 扩散系数

# 初始条件：中心处的高斯分布
def u0_gaussian(x):
    return np.exp(-(x - L/2)**2 / 0.5)

# 增加时间步数以提高稳定性
solver1 = Diffusion1D(D, L, T, nx=201, nt=1000)
u1 = solver1.solve_explicit(u0_gaussian, {'left': 'neumann', 'right': 'neumann'})

# 可视化 1D
fig1, axes1 = plt.subplots(2, 2, figsize=(12, 10))
# 调整索引以匹配新的 nt
time_indices = [0, 100, 300, 999]
titles = ['Initial distribution', 't = 0.2', 't = 0.6', 't = 2.0']

for i, (idx, title) in enumerate(zip(time_indices, titles)):
    ax = axes1[i//2, i%2]
    ax.plot(solver1.x, u1[idx, :], 'b-', linewidth=2)
    ax.set_xlabel('Position $x$', fontsize=12)
    ax.set_ylabel('Density $u(x,t)$', fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.set_ylim([0, 1.1])

fig1.suptitle('1D Diffusion Equation: Diffusion of Gaussian Initial Condition', fontsize=16)
plt.tight_layout()
plt.show()

# ==========================================
# 2D 稳定性演示
# ==========================================
print("\n" + "="*50)
print("演示：二维扩散方程的数值稳定性分析")
print("="*50)
print("理论条件: D * dt / h^2 <= 0.25")

L_2d = 1.0
nx_2d = 31
h_2d = L_2d / (nx_2d - 1)  # 0.0333
D_2d = 1.0

# 初始条件: 中心高斯峰
def u0_2d(X, Y):
    return np.exp(-((X - L_2d/2)**2 + (Y - L_2d/2)**2) / 0.02)

# Case 1: 稳定 (Stable)
# D*dt/h^2 = 0.24 <= 0.25
dt_stable = 0.24 * (h_2d**2) / D_2d
T_stable = 0.1
nt_stable = int(T_stable / dt_stable) + 1
print("\nCase 1: 稳定参数 (nu = 0.24)")
solver_stable = Diffusion2D(D_2d, L_2d, T_stable, nx_2d, nt_stable)
u_stable = solver_stable.solve_explicit_initial_step(u0_2d)

# Case 2: 不稳定 (Unstable)
# D*dt/h^2 = 0.26 > 0.25
dt_unstable = 0.28 * (h_2d**2) / D_2d 
# 保持时间大致相同，但由于dt更大，这就足矣
nt_unstable = nt_stable  
T_unstable = dt_unstable * nt_unstable
print("\nCase 2: 不稳定参数 (nu = 0.28)")
solver_unstable = Diffusion2D(D_2d, L_2d, T_unstable, nx_2d, nt_unstable)
u_unstable = solver_unstable.solve_explicit_initial_step(u0_2d)

# 绘图对比
fig3, axes3 = plt.subplots(1, 3, figsize=(16, 5))

# 初始状态
u0 = u0_2d(solver_stable.X, solver_stable.Y)
im0 = axes3[0].imshow(u0, cmap='viridis', origin='lower', extent=[0, L_2d, 0, L_2d])
axes3[0].set_xlabel('x')
axes3[0].set_ylabel('y')
axes3[0].set_title("Initial State $u(x,y,0)$", fontsize=14)
plt.colorbar(im0, ax=axes3[0])

# 稳定结果
im1 = axes3[1].imshow(u_stable, cmap='viridis', origin='lower', extent=[0, L_2d, 0, L_2d])
axes3[1].set_xlabel('x')
axes3[1].set_title(f"Stable Evolution ($\\nu=0.24$)\n$t={T_stable:.3f}$", fontsize=14)
plt.colorbar(im1, ax=axes3[1])

# 不稳定结果
vmin, vmax = np.min(u_stable), np.max(u_stable)
# 限制显示范围，以便观察模式
im2 = axes3[2].imshow(u_unstable, cmap='viridis', origin='lower', extent=[0, L_2d, 0, L_2d], vmin=vmin, vmax=vmax)
axes3[2].set_xlabel('x')
axes3[2].set_title(f"Unstable Evolution ($\\nu=0.28$)\n$t={T_unstable:.3f}$", fontsize=14)
plt.colorbar(im2, ax=axes3[2])

# 添加文字说明
plt.figtext(0.5, 0.02, 
            r"Stability Condition: $\frac{D \Delta t}{h^2} \leq \frac{1}{4}$. Violation leads to numerical oscillations (Right).", 
            ha="center", fontsize=12, bbox={"facecolor":"orange", "alpha":0.2, "pad":5})

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig('diffusion_2d_stability_analysis.png', dpi=300)
plt.show()
```

### 2.4.2.2 生态学中的反应-扩散方程

回顾反应-扩散方程，对于一维空间，方程写作
$$
\frac{\partial u}{\partial t}=D\frac{\partial^2 u}{\partial x^2}+f(u);
$$
对于二维空间，
$$
\frac{\partial u}{\partial t}=D\left(\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}\right)+f(u)=D\nabla^2 u+f(u).
$$

反应项 $f(u)$ 体现了种群的局部动力学，常见形式包括：

* **指数增长**：$f(u)=ru$，对应于无限资源下的无界增长。
* **逻辑斯谛增长**：$f(u)=ru(1-u/K)$，其中 $r$ 为内禀增长率，$K$ 为环境容纳量。
* **Allee效应**：$f(u)=ru(u-a)(1-u/K)$，$0<a<K$ 为Allee阈值，当密度低于 $a$ 时种群负增长。
* **捕食者-猎物相互作用**：需用两个耦合方程描述。

### 2.4.2.3 反应-扩散方程的无量纲化

以带逻辑斯谛增长的反应-扩散方程为例进行无量纲化：
$$
\frac{\partial u}{\partial t}=ru\left(1-\frac{u}{K}\right)+D\frac{\partial^2 u}{\partial x^2}.
$$
引入无量纲变量：
$$
\bar{u}=\frac{u}{K},\quad \bar{x}=x\sqrt{\frac{r}{D}},\quad \bar{t}=rt,
$$
方程简化为
$$
\frac{\partial \bar{u}}{\partial \bar{t}}=\bar{u}(1-\bar{u})+\frac{\partial^2 \bar{u}}{\partial \bar{x}^2}.
$$
无量纲化减少了参数个数，突出了系统的本质特征。下文若无特别说明，尽可能采用无量纲形式。

## 2.4.3 Fisher-KPP 方程

### 2.4.3.1 模型与行波解

Fisher-KPP 方程（Fisher-Kolmogorov-Petrovsky-Piscounov）是反应-扩散方程最经典的例子：
$$
\frac{\partial u}{\partial t}=ru(1-u)+D\frac{\partial^2 u}{\partial x^2}.
$$
它描述了具有逻辑斯谛增长的种群在一维空间中的传播。该方程存在 **行波解（traveling wave solution）**：
$$
u(x,t)=U(z),\quad z=x-ct,
$$
其中 $c$ 为波速。代入方程得到关于 $U$ 的常微分方程：
$$
-cU' = rU(1-U)+DU''.
$$

### 2.4.3.2 最小波速与入侵速度

对于初始条件具有紧支集（局部化）的情形，行波最终以 **最小波速** 传播：
$$
c_{\text{min}}=2\sqrt{rD}.
$$
这个最小波速正是种群在均匀环境中的 **入侵速度（invasion speed）**。数值模拟可以验证这一理论结果：初始时刻在局部区域放置种群，随后形成向前传播的波形，波速趋近于 $2\sqrt{rD}$。

```python-plot
"""
invasive_species_model.py
入侵物种扩散模型
"""

import numpy as np
import matplotlib.pyplot as plt

class InvasiveSpeciesModel:
    """入侵物种扩散模型"""
    
    def __init__(self, D=10.0, r=0.5, K=1.0, L=500.0, T=50.0):
        """
        初始化入侵模型
        
        参数:
        D : 扩散系数 (km²/年)
        r : 年增长率
        K : 环境容纳量
        L : 空间域长度 (km)
        T : 模拟时间 (年)
        """
        self.D = D
        self.r = r
        self.K = K
        self.L = L
        self.T = T
        
        # 空间和时间离散化
        self.dx = 5.0  # 空间步长 (km)
        self.dt = 0.1  # 时间步长 (年)
        
        self.Nx = int(L / self.dx) + 1
        self.Nt = int(T / self.dt) + 1
        
        self.x = np.linspace(0, L, self.Nx)
        self.t = np.linspace(0, T, self.Nt)
    
    def simulate_invasion(self, initial_location=100.0, initial_radius=10.0):
        """模拟入侵过程"""
        # 初始条件：局部引入
        u0 = np.zeros(self.Nx)
        center_idx = np.argmin(np.abs(self.x - initial_location))
        radius_idx = int(initial_radius / self.dx)
        
        start_idx = max(0, center_idx - radius_idx)
        end_idx = min(self.Nx, center_idx + radius_idx)
        u0[start_idx:end_idx] = 0.1 * self.K
        
        # 数值求解
        u = u0.copy()
        u_history = [u.copy()]
        
        alpha = self.D * self.dt / (self.dx ** 2)
        
        for n in range(1, self.Nt):
            u_new = u.copy()
            
            # 显式更新
            for i in range(1, self.Nx-1):
                diffusion = alpha * (u[i+1] - 2*u[i] + u[i-1])
                reaction = self.dt * self.r * u[i] * (1 - u[i]/self.K)
                u_new[i] = u[i] + diffusion + reaction
            
            # 诺伊曼边界条件
            u_new[0] = u_new[1]
            u_new[-1] = u_new[-2]
            
            u = u_new.copy()
            
            # 每10年保存一次
            if n % int(10/self.dt) == 0:
                u_history.append(u.copy())
        
        return np.array(u_history)
    
    def plot_invasion_front(self, u_history):
        """绘制入侵前沿"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        # 空间分布随时间变化
        years = np.arange(0, self.T+1, 10)
        for i, u in enumerate(u_history):
            axes[0].plot(self.x, u, label=f'Year {years[i]}', alpha=0.7)
        
        axes[0].set_xlabel('Distance from origin (km)', fontsize=12)
        axes[0].set_ylabel('Population density', fontsize=12)
        axes[0].set_title('Invasion Front Propagation', fontsize=14)
        axes[0].legend(fontsize=10)
        axes[0].grid(True, alpha=0.3)
        
        # 计算波速
        threshold = 0.1 * self.K
        wave_positions = []
        times = []
        
        for i, u in enumerate(u_history):
            # 找到密度超过阈值的最远位置
            idx = np.where(u >= threshold)[0]
            if len(idx) > 0:
                wave_positions.append(self.x[idx[-1]])
                times.append(years[i])
        
        if len(wave_positions) > 2:
            # 线性拟合 (Numerical Speed)
            times_arr = np.array(times)
            coeffs = np.polyfit(times_arr, wave_positions, 1)
            numerical_speed = coeffs[0]
            intercept = coeffs[1]
            
            axes[1].plot(times, wave_positions, 'bo-', label='Wave front position')
            axes[1].plot(times, np.polyval(coeffs, times), 'r--', 
                        label=f'Numerical Speed: {numerical_speed:.2f} km/year')
            
            # 理论波速 (Theoretical Speed)
            theoretical_speed = 2 * np.sqrt(self.D * self.r)
            
            # 为了对比斜率，我们画一条具有理论斜率的直线
            # 让它通过数据的中间点，以便于视觉比较
            mid_time = times_arr[len(times)//2]
            mid_pos = wave_positions[len(times)//2]
            theoretical_line = mid_pos + theoretical_speed * (times_arr - mid_time)
            
            axes[1].plot(times, theoretical_line, 'g:', linewidth=2,
                        label=f'Theoretical Speed: {theoretical_speed:.2f} km/year')
            
            # 添加文本说明
            info_text = (
                f"$c_{{min}} = 2\\sqrt{{rD}} = {theoretical_speed:.2f}$\n"
                f"$c_{{num}} \\approx {numerical_speed:.2f}$"
            )
            axes[1].text(0.05, 0.95, info_text, transform=axes[1].transAxes, 
                        fontsize=12, verticalalignment='top',
                        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        axes[1].set_xlabel('Time (years)', fontsize=12)
        axes[1].set_ylabel('Wave front position (km)', fontsize=12)
        axes[1].set_title('Invasion Speed', fontsize=14)
        axes[1].legend(fontsize=10)
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('fisher_kpp_wave.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return numerical_speed if 'numerical_speed' in locals() else None

# 示例：斑马贻贝入侵模拟
def zebra_mussel_invasion():
    """模拟斑马贻贝入侵"""
    # 参数估计（基于文献数据）
    D = 15.0  # 扩散系数 (km²/年)，考虑船只运输
    r = 0.8   # 年增长率
    K = 1.0   # 相对容纳量
    
    print("\n" + "="*60)
    print("FISHER-KPP EQUATION: TRAVELING WAVE ANALYSIS")
    print("="*60)
    print(f"Model parameters:")
    print(f"  Diffusion coefficient (D): {D} km²/year")
    print(f"  Growth rate (r): {r} /year")
    print(f"  Carrying capacity (K): {K}")
    print("-" * 60)
    print("Theoretical Background:")
    print("  The Fisher-KPP equation admits traveling wave solutions of the form:")
    print("    u(x,t) = U(z), where z = x - ct")
    print("  For initial conditions with compact support (localized population),")
    print("  the wave front propagates asymptotically at the minimum wave speed:")
    print("    c_min = 2 * sqrt(r * D)")
    
    c_theoretical = 2 * np.sqrt(D * r)
    print(f"  Calculated c_min: {c_theoretical:.4f} km/year")
    print("-" * 60)
    
    model = InvasiveSpeciesModel(D=D, r=r, K=K, L=500.0, T=30.0)
    print("Running numerical simulation...")
    u_history = model.simulate_invasion(initial_location=100.0, initial_radius=20.0)
    
    print("Analyzing wave front propagation...")
    numerical_speed = model.plot_invasion_front(u_history)
    
    if numerical_speed:
        print(f"Numerical result:")
        print(f"  Estimated wave speed: {numerical_speed:.4f} km/year")
        error = abs(numerical_speed - c_theoretical) / c_theoretical * 100
        print(f"  Relative error: {error:.2f}%")
        print("Note: Numerical speed convergence requires long times and fine grids.")
        print("      Small discrepancies are expected in finite-time simulations.")

zebra_mussel_invasion()
```

## 2.4.4 非均匀环境中的单种群动态

自然环境中资源分布往往是不均匀的，考虑如下单种群模型：

$$
\begin{cases}
\dfrac{\partial u}{\partial t}=d\Delta u+u(m(x)-u), & (x,t)\in\Omega\times(0,T),\\[6pt]
\dfrac{\partial u}{\partial\nu}=0, & (x,t)\in\partial\Omega\times(0,T),\\[6pt]
u(x,0)=u_0(x), & x\in\Omega,
\end{cases}
$$
其中 $m(x)$ 是空间依赖的生长率（反映资源质量），$\Omega$ 是有界区域，$\partial u/\partial\nu=0$ 表示封闭边界。

该模型存在唯一正平衡解 $\theta(x)$，满足
$$
\begin{cases}
d\Delta\theta+\theta(m-\theta)=0,&x\in\Omega,\\[4pt]
\dfrac{\partial\theta}{\partial\nu}=0,&x\in\partial\Omega.
\end{cases}
$$
总生物量 $\int_\Omega\theta(x)\,\mathrm{d}x$ 如何依赖于扩散系数 $d$？一个很粗略的回答是：对所有 $d>0$，有 $\int_\Omega\theta > \int_\Omega m$，且
$$
\lim_{d\to0^+}\int_\Omega\theta = \lim_{d\to\infty}\int_\Omega\theta = \int_\Omega m.
$$
这意味着总生物量作为 $d$ 的函数是非单调的：在扩散极慢或极快时，总生物量等于总资源量；而在某个适中的扩散系数下，总生物量达到最大值（甚至可能出现多个局部最大值）。该结论表明，适度的扩散有助于种群更有效地利用空间异质性资源。

```python-plot
"""
heterogeneous_environment_single_species.py
非均匀环境中单个种群模型的有限差分求解
验证引理：物种数量与扩散系数的非单调关系
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
from scipy.optimize import fsolve

class HeterogeneousSingleSpeciesModel:
    """非均匀环境中单个种群模型求解器"""
    
    def __init__(self, L=10.0, Nx=201):
        """
        初始化模型参数
        
        参数:
        L : 空间域长度
        Nx : 空间网格点数
        """
        self.L = L
        self.Nx = Nx
        self.x = np.linspace(0, L, Nx)
        self.dx = self.x[1] - self.x[0]
        
        # 非均匀生长率函数 m(x) - 非常数函数
        self.m = self._growth_rate_function()
        
        # 计算总资源 (Manual trapezoidal integration for compatibility)
        self.total_resources = np.sum(self.m) * self.dx - 0.5 * self.dx * (self.m[0] + self.m[-1])
    
    def _growth_rate_function(self, type='sinusoidal'):
        """生长率函数 m(x)"""
        if type == 'sinusoidal':
            # 正弦函数，模拟周期性资源分布
            return 1.0 + 0.5 * np.sin(2 * np.pi * self.x / self.L)
        elif type == 'gaussian':
            # 高斯函数，模拟局部资源丰富区
            center = self.L / 2
            return 1.0 + 0.8 * np.exp(-(self.x - center)**2 / 2)
        elif type == 'step':
            # 阶梯函数，模拟碎片化栖息地
            m = np.ones_like(self.x)
            m[self.x < self.L/3] = 0.5
            m[self.x > 2*self.L/3] = 0.5
            return m
        else:
            raise ValueError(f"未知的生长率函数类型: {type}")
    
    def construct_laplacian_matrix(self, d):
        """构造拉普拉斯算子的矩阵表示"""
        N = self.Nx
        alpha = d / (self.dx ** 2)
        
        # 主对角线
        main_diag = -2 * alpha * np.ones(N)
        # 次对角线
        off_diag = alpha * np.ones(N-1)
        
        # 诺伊曼边界条件：零流边界
        main_diag[0] = -alpha  # 左边界
        main_diag[-1] = -alpha  # 右边界
        
        # 构造三对角矩阵
        A = diags([off_diag, main_diag, off_diag], [-1, 0, 1], format='csr')
        return A
    
    def solve_equilibrium(self, d, method='newton'):
        """求解平衡态方程 (2.2)"""
        N = self.Nx
        theta0 = np.ones(N)  # 初始猜测
        
        if method == 'newton':
            # 使用牛顿法求解非线性方程
            def F(theta):
                A = self.construct_laplacian_matrix(d)
                return A.dot(theta) + theta * (self.m - theta)
            
            def J(theta):
                # 雅可比矩阵
                A = self.construct_laplacian_matrix(d)
                diag_elements = self.m - 2 * theta
                J_matrix = A + diags([diag_elements], [0], format='csr')
                return J_matrix
            
            # 牛顿迭代
            theta = theta0.copy()
            for i in range(100):
                F_val = F(theta)
                if np.linalg.norm(F_val) < 1e-10:
                    break
                J_mat = J(theta)
                delta = spsolve(J_mat, -F_val)
                theta += delta
                theta = np.maximum(theta, 0)  # 确保非负
            return theta
        
        elif method == 'time_evolution':
            # 通过时间演化到平衡态
            dt = 0.01
            theta = theta0.copy()
            for _ in range(10000):
                A = self.construct_laplacian_matrix(d)
                reaction = theta * (self.m - theta)
                dtheta_dt = A.dot(theta) + reaction
                theta += dt * dtheta_dt
                theta = np.maximum(theta, 0)  # 确保非负
                if np.linalg.norm(dtheta_dt) < 1e-8:
                    break
            return theta
    
    def calculate_total_biomass(self, d_values):
        """计算不同扩散系数下的总生物量"""
        biomasses = []
        thetas = []
        
        for d in d_values:
            theta = self.solve_equilibrium(d)
            # Manual trapezoidal integration for compatibility
            biomass = np.sum(theta) * self.dx - 0.5 * self.dx * (theta[0] + theta[-1])
            biomasses.append(biomass)
            thetas.append(theta)
        
        return np.array(biomasses), thetas
    
    def analyze_dependence_on_d(self):
        """分析总生物量对扩散系数的依赖性"""
        # 扩散系数范围（对数尺度）
        d_values = np.logspace(-3, 3, 50)
        
        # 计算总生物量
        biomasses, thetas = self.calculate_total_biomass(d_values)
        
        # 绘制结果
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # 1. 总生物量 vs 扩散系数
        ax = axes[0, 0]
        ax.loglog(d_values, biomasses, 'b-', linewidth=2, label='Total biomass')
        ax.axhline(y=self.total_resources, color='r', linestyle='--', 
                  label=f'Total resources: {self.total_resources:.3f}')
        ax.set_xlabel('Diffusion coefficient (d)', fontsize=12)
        ax.set_ylabel('Total biomass', fontsize=12)
        ax.set_title('Biomass vs Diffusion Coefficient (Lemma 2.1)', fontsize=14)
        ax.legend(fontsize=12)
        ax.grid(True, alpha=0.3, which='both')
        
        # 2. 差值：总生物量 - 总资源
        ax = axes[0, 1]
        difference = biomasses - self.total_resources
        ax.semilogx(d_values, difference, 'g-', linewidth=2)
        ax.axhline(y=0, color='r', linestyle='--')
        ax.set_xlabel('Diffusion coefficient (d)', fontsize=12)
        ax.set_ylabel('Biomass - Resources', fontsize=12)
        ax.set_title('Excess Biomass (Lemma 2.1: ∫θ > ∫m)', fontsize=14)
        ax.grid(True, alpha=0.3, which='both')
        
        # 3. 不同扩散系数下的空间分布
        ax = axes[1, 0]
        selected_indices = [0, 10, 25, 40, 49]  # 选择几个扩散系数
        colors = plt.cm.viridis(np.linspace(0, 1, len(selected_indices)))
        
        for i, idx in enumerate(selected_indices):
            d = d_values[idx]
            theta = thetas[idx]
            ax.plot(self.x, theta, color=colors[i], 
                   label=f'd={d:.3f}', linewidth=1.5, alpha=0.8)
        
        # 绘制生长率函数
        ax.plot(self.x, self.m, 'k--', linewidth=2, label='m(x)')
        ax.set_xlabel('Position (x)', fontsize=12)
        ax.set_ylabel('Population density', fontsize=12)
        ax.set_title('Spatial Distribution for Different d', fontsize=14)
        ax.legend(fontsize=10, ncol=2)
        ax.grid(True, alpha=0.3)
        
        # 4. 寻找最大生物量对应的扩散系数
        ax = axes[1, 1]
        # 在原始网格上插值寻找最大值
        from scipy.interpolate import interp1d
        f = interp1d(np.log10(d_values), biomasses, kind='cubic')
        d_fine = np.logspace(-3, 3, 1000)
        bio_fine = f(np.log10(d_fine))
        
        max_idx = np.argmax(bio_fine)
        d_opt = d_fine[max_idx]
        bio_max = bio_fine[max_idx]
        
        ax.loglog(d_values, biomasses, 'bo', markersize=6, label='Calculated points')
        ax.loglog(d_fine, bio_fine, 'b-', linewidth=1, alpha=0.5, label='Interpolation')
        ax.loglog(d_opt, bio_max, 'r*', markersize=15, 
                 label=f'Maximum: d={d_opt:.4f}, biomass={bio_max:.4f}')
        ax.set_xlabel('Diffusion coefficient (d)', fontsize=12)
        ax.set_ylabel('Total biomass', fontsize=12)
        ax.set_title(f'Optimal Diffusion Coefficient\nMax biomass at d={d_opt:.3f}', fontsize=14)
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3, which='both')
        
        plt.tight_layout()
        plt.savefig('heterogeneous_single_species.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("\n" + "="*60)
        print("HETEROGENEOUS SINGLE SPECIES MODEL ANALYSIS")
        print("="*60)
        print(f"Total resources (∫m dx): {self.total_resources:.4f}")
        print(f"Minimum biomass (d→0): {biomasses[0]:.4f}")
        print(f"Minimum biomass (d→∞): {biomasses[-1]:.4f}")
        print(f"Maximum biomass: {bio_max:.4f} at d={d_opt:.4f}")
        print(f"Excess biomass at optimum: {bio_max - self.total_resources:.4f}")
        
        return d_opt, bio_max

def verify_lemma():
    """验证引理：物种数量与扩散系数的关系"""
    print("Verifying Lemma")
    
    # 创建模型
    model = HeterogeneousSingleSpeciesModel(L=10.0, Nx=201)
    
    # 分析总生物量对扩散系数的依赖性
    d_opt, bio_max = model.analyze_dependence_on_d()
    
    # 验证引理的极限情况
    d_values_extreme = np.logspace(-4, 4, 9)
    biomasses_extreme, _ = model.calculate_total_biomass(d_values_extreme)
    
    print("\n" + "="*60)
    print("VERIFICATION OF LEMMA")
    print("="*60)
    print("Lemma states:")
    print("1. For all d > 0, ∫θ > ∫m")
    print("2. lim_{d→0+} ∫θ = lim_{d→∞} ∫θ = ∫m")
    print("\nNumerical verification:")
    
    # 检查所有d>0时是否∫θ > ∫m
    all_greater = all(b > model.total_resources for b in biomasses_extreme)
    print(f"1. ∫θ > ∫m for all d > 0: {all_greater}")
    
    # 检查极限情况
    print(f"2. lim_{{d→0+}} ∫θ = {biomasses_extreme[0]:.6f}, ∫m = {model.total_resources:.6f}")
    print(f"   Relative error: {abs(biomasses_extreme[0] - model.total_resources)/model.total_resources*100:.2f}%")
    print(f"3. lim_{{d→∞}} ∫θ = {biomasses_extreme[-1]:.6f}, ∫m = {model.total_resources:.6f}")
    print(f"   Relative error: {abs(biomasses_extreme[-1] - model.total_resources)/model.total_resources*100:.2f}%")

verify_lemma()
```

## 2.4.5 空间中的竞争模型

### 2.4.5.1 均匀环境中的Lotka-Volterra竞争模型

经典的两种群竞争模型在均匀环境下可写作
$$
\begin{cases}
\dfrac{\partial u}{\partial t}=d_1\Delta u+u(a_1-b_1u-c_1v),\\[6pt]
\dfrac{\partial v}{\partial t}=d_2\Delta v+v(a_2-b_2u-c_2v),
\end{cases}
$$
并附加适当的边界条件。当系数满足 **弱竞争条件**
$$
\frac{b_1}{b_2}>\frac{a_1}{a_2}>\frac{c_1}{c_2}
$$
时，均匀环境中两物种可稳定共存。

### 2.4.5.2 非均匀环境中的竞争模型

考虑资源分布 $m(x)$ 相同的简化情形：
$$
\begin{cases}
u_t = d\Delta u + u(m - u - bv),\\[4pt]
v_t = D\Delta v + v(m - cu - v),\\[4pt]
\dfrac{\partial u}{\partial\nu}=\dfrac{\partial v}{\partial\nu}=0,
\end{cases}
$$
其中 $0<b,c<1$ 保证处处满足弱竞争条件。然而，由于扩散系数的差异，竞争结果可能变为排斥，定理指出：

设 $b,c\in(0,1)$，$u^*$ 是单物种平衡解。定义 $c^* = \inf_{d>0}\dfrac{\int_\Omega m}{\int_\Omega u^*}$。若 $c>c^*$，则存在一个非空区域 $\Sigma\subset\mathbb{R}^+\times\mathbb{R}^+$，使得对 $(d,D)\in\Sigma$，半平凡平衡态 $(u^*,0)$ 是稳定的（即物种 $v$ 灭绝）。

特别地，当竞争对称（$b=c=1$）时，有更简洁的结论：

若 $b=c=1$，则：
- 若 $d<D$，则 $(u^*,0)$ 稳定，$(0,v^*)$ 不稳定；
- 若 $d>D$，则 $(0,v^*)$ 稳定，$(u^*,0)$ 不稳定；
- 若 $d=D$，则存在连续统的共存平衡解。

该定理揭示了在对称竞争下，扩散较慢的物种具有竞争优势，这与非均匀环境中的资源利用策略有关。

```python-plot
"""
heterogeneous_competition_model.py
非均匀环境中竞争模型的数值模拟
验证定理：扩散系数对竞争结果的影响
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
from scipy.linalg import eigvals

class HeterogeneousCompetitionModel:
    """非均匀环境中竞争模型求解器"""
    
    def __init__(self, L=10.0, Nx=201, m_type='sinusoidal'):
        """
        初始化竞争模型参数
        
        参数:
        L : 空间域长度
        Nx : 空间网格点数
        m_type : 资源分布类型
        """
        self.L = L
        self.Nx = Nx
        self.x = np.linspace(0, L, Nx)
        self.dx = self.x[1] - self.x[0]
        
        # 资源分布函数 m(x)
        self.m = self._resource_function(m_type)
        
        # 默认参数
        self.b = 0.8  # 竞争系数
        self.c = 0.9  # 竞争系数
        
    def _resource_function(self, m_type):
        """资源分布函数 m(x)"""
        if m_type == 'sinusoidal':
            return 1.0 + 0.5 * np.sin(2 * np.pi * self.x / self.L)
        elif m_type == 'gaussian':
            center = self.L / 2
            return 1.0 + 0.8 * np.exp(-(self.x - center)**2 / 2)
        elif m_type == 'step':
            m = np.ones_like(self.x)
            m[self.x < self.L/3] = 0.5
            m[self.x > 2*self.L/3] = 0.5
            return m
        else:
            raise ValueError(f"未知的资源分布类型: {m_type}")
    
    def construct_laplacian_matrix(self, d):
        """构造拉普拉斯算子的矩阵表示（诺伊曼边界条件）"""
        N = self.Nx
        alpha = d / (self.dx ** 2)
        
        # 主对角线
        main_diag = -2 * alpha * np.ones(N)
        # 次对角线
        off_diag = alpha * np.ones(N-1)
        
        # 诺伊曼边界条件：零流边界
        main_diag[0] = -alpha  # 左边界
        main_diag[-1] = -alpha  # 右边界
        
        # 构造三对角矩阵
        A = diags([off_diag, main_diag, off_diag], [-1, 0, 1], format='csr')
        return A
    
    def single_species_equilibrium(self, d):
        """求解单个物种的平衡态 u* using Newton's method"""
        N = self.Nx
        # Initial guess
        u = np.ones(N) * np.mean(self.m)
        
        # Newton iterations
        for i in range(20):
            # A corresponds to d * d^2/dx^2
            A = self.construct_laplacian_matrix(d)
            
            # F(u) = A*u + u*(m-u) = 0
            F = A.dot(u) + u * (self.m - u)
            
            if np.linalg.norm(F, np.inf) < 1e-10:
                break                
            
            # Jacobian J = A + diag(m - 2u)
            diag_reaction = diags([self.m - 2*u], [0], format='csr')
            J = A + diag_reaction
            
            # Solve J * delta = -F
            try:
                delta = spsolve(J, -F)
                u += delta
                u = np.maximum(u, 1e-9) # Enforce positivity
            except Exception:
                break
        
        return u
    
    def _integrate(self, y, x):
        """数值积分 (Trapezoidal rule) helper"""
        dx = x[1] - x[0]
        # compatible with 2D array (axis 1) or 1D array
        if y.ndim == 1:
            return np.sum(y) * dx - 0.5 * dx * (y[0] + y[-1])
        else:
            return np.sum(y, axis=1) * dx - 0.5 * dx * (y[:, 0] + y[:, -1])

    def calculate_c_star(self, d_values):
        """计算 c* = inf_{d>0} ∫m / ∫u*"""
        ratios = []
        
        for d in d_values:
            u_star = self.single_species_equilibrium(d)
            total_m = self._integrate(self.m, self.x)
            total_u = self._integrate(u_star, self.x)
            ratios.append(total_m / total_u)
        
        c_star = min(ratios)
        d_opt = d_values[np.argmin(ratios)]
        
        return c_star, d_opt, ratios
    
    def stability_of_semi_trivial_solution(self, d, D, c):
        """计算半平凡解 (u*, 0) 的稳定性"""
        # 首先计算 u*
        u_star = self.single_species_equilibrium(d)
        
        # 构造线性化算子矩阵
        N = self.Nx
        A = self.construct_laplacian_matrix(D)
        
        # 添加反应项的对角部分
        diag_elements = self.m - c * u_star
        M = A + diags([diag_elements], [0], format='csr')
        
        # 使用稠密矩阵求解特征值（比ARPACK更稳健）
        M_dense = M.todense()
        evals = eigvals(M_dense)
        
        # 动力学稳定性：看实部最大值 (Max Lyapunov Exponent)
        # lambda > 0 => 不稳定 (v invades)
        # lambda < 0 => 稳定 (u wins)
        lambda_max = np.max(np.real(evals))
        
        # 为了适配原代码逻辑 (plot中 positive => stable)，我们返回 -lambda_max
        # 这样: metric > 0 -> Stable, metric < 0 -> Unstable
        metric = -lambda_max
        
        return metric, u_star
    
    def simulate_competition(self, d, D, b, c, T=100.0, dt=None):
        """
        模拟竞争动力学
        
        参数 dt: 如果为None，则根据稳定性条件自动计算
        """
        # 自动计算合适的时间步长以满足稳定性条件
        # d * dt / dx^2 <= 0.5  =>  dt <= 0.5 * dx^2 / max(d, D)
        max_diff = max(d, D)
        dt_stable = 0.45 * (self.dx ** 2) / max_diff
        
        if dt is None or dt > dt_stable:
            print(f"Adjusting time step for stability: {dt} -> {dt_stable:.6f} (max D={max_diff})")
            dt = dt_stable
            
        N = self.Nx
        Nt = int(T / dt)
        
        # 初始条件
        u = 0.5 * np.ones(N) + 0.1 * np.random.randn(N)
        v = 0.5 * np.ones(N) + 0.1 * np.random.randn(N)
        
        # 扩散矩阵
        A_u = self.construct_laplacian_matrix(d)
        A_v = self.construct_laplacian_matrix(D)
        
        # 预计算常数
        # 显式欧拉：u_new = u + dt * (A*u + f(u))
        # 矩阵A已经包含了 1/dx^2 因子
        
        u_history = []
        v_history = []
        
        # 记录每多少步保存一次，总共保存约200帧
        save_interval = max(1, int(Nt / 200))
        
        u_history.append(u.copy())
        v_history.append(v.copy())
        
        for n in range(1, Nt):
            # 反应项
            # 添加数值限制防止溢出
            u_safe = np.clip(u, 0, 1e5)
            v_safe = np.clip(v, 0, 1e5)
            
            reaction_u = u_safe * (self.m - u_safe - b * v_safe)
            reaction_v = v_safe * (self.m - c * u_safe - v_safe)
            
            # 更新 (A矩阵是 d * d2/dx2)
            # 注意: construct_laplacian_matrix 返回的是 d/dx^2 * [1, -2, 1]
            diff_u = A_u.dot(u)
            diff_v = A_v.dot(v)
            
            u = u + dt * (diff_u + reaction_u)
            v = v + dt * (diff_v + reaction_v)
            
            # 确保非负
            u = np.maximum(u, 0)
            v = np.maximum(v, 0)
            
            # 保存结果
            if n % save_interval == 0:
                u_history.append(u.copy())
                v_history.append(v.copy())
        
        # 确保最后一步也被保存
        u_history.append(u.copy())
        v_history.append(v.copy())
        
        return np.array(u_history), np.array(v_history)
    
    def analyze_competition_outcomes(self, d_values, D_values, b, c):
        """分析竞争结果：绘制Σ区域"""
        stability_matrix = np.zeros((len(d_values), len(D_values)))
        
        for i, d in enumerate(d_values):
            for j, D in enumerate(D_values):
                val, _ = self.stability_of_semi_trivial_solution(d, D, c)
                # val > 0: (u*, 0) 稳定 -> u wins
                # val < 0: (u*, 0) 不稳定 -> coexistence or v wins
                stability_matrix[i, j] = 1 if val > 0 else -1
        
        return stability_matrix
    
    def plot_competition_dynamics(self, d, D, b, c):
        """绘制竞争动力学"""
        print(f"Simulating dynamics for d={d}, D={D}...")
        u_history, v_history = self.simulate_competition(d, D, b, c, T=200.0)
        
        # 计算稳定性指标 (metric)
        # 使用最后时刻的积分值比较
        u_final_total = np.sum(u_history[-1]) * self.dx
        v_final_total = np.sum(v_history[-1]) * self.dx
        
        # 定义 metric: >0 表示 u 获胜, <0 表示 v 获胜
        metric = (u_final_total - v_final_total) / (u_final_total + v_final_total + 1e-10)
        
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        
        # 1. 最终空间分布
        ax = axes[0, 0]
        u_final = u_history[-1]
        v_final = v_history[-1]
        ax.plot(self.x, u_final, 'b-', linewidth=2, label='Species u (d={})'.format(d))
        ax.plot(self.x, v_final, 'r-', linewidth=2, label='Species v (D={})'.format(D))
        ax.plot(self.x, self.m, 'k:', linewidth=1.5, label='Resource m(x)', alpha=0.5)
        ax.set_xlabel('Position (x)', fontsize=12)
        ax.set_ylabel('Population density', fontsize=12)
        ax.set_title(f'Final Distribution (T=200)', fontsize=14)
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)
        
        # 2. 时间演化（空间平均）
        ax = axes[0, 1]
        # 只有在 history 非空时才绘制
        if len(u_history) > 0:
            time_points = np.linspace(0, 200, len(u_history))
            u_mean = np.mean(u_history, axis=1)
            v_mean = np.mean(v_history, axis=1)
            
            ax.plot(time_points, u_mean, 'b-', linewidth=2, label='Mean u')
            ax.plot(time_points, v_mean, 'r-', linewidth=2, label='Mean v')
            ax.set_xlabel('Time', fontsize=12)
            ax.set_ylabel('Mean Density', fontsize=12)
            ax.set_title('Mean Density Dynamics', fontsize=14)
            ax.legend(fontsize=10)
            ax.grid(True, alpha=0.3)
        
        # 3. 总生物量
        ax = axes[0, 2]
        if len(u_history) > 0:
            u_total = np.sum(u_history, axis=1) * self.dx
            v_total = np.sum(v_history, axis=1) * self.dx
            
            ax.plot(time_points, u_total, 'b-', linewidth=2, label='Total u')
            ax.plot(time_points, v_total, 'r-', linewidth=2, label='Total v')
            ax.set_xlabel('Time', fontsize=12)
            ax.set_ylabel('Total Biomass', fontsize=12)
            ax.set_title('Total Biomass Dynamics', fontsize=14)
            ax.legend(fontsize=10)
            ax.grid(True, alpha=0.3)

        # 4. 时空演化图 (Space-Time Plot) for u
        ax = axes[1, 0]
        if len(u_history) > 0:
            # 降采样以避免绘图过慢
            skip = max(1, len(u_history) // 100)
            im = ax.imshow(u_history[::skip], aspect='auto', cmap='Blues', 
                          extent=[0, self.L, 200, 0], vmin=0, vmax=np.max(self.m))
            ax.set_xlabel('Position', fontsize=12)
            ax.set_ylabel('Time', fontsize=12)
            ax.set_title('Spatiotemporal Dynamics of u', fontsize=14)
            plt.colorbar(im, ax=ax, label='Density')

        # 5. 时空演化图 (Space-Time Plot) for v
        ax = axes[1, 1]
        if len(v_history) > 0:
            skip = max(1, len(v_history) // 100)
            im = ax.imshow(v_history[::skip], aspect='auto', cmap='Reds', 
                          extent=[0, self.L, 200, 0], vmin=0, vmax=np.max(self.m))
            ax.set_xlabel('Position', fontsize=12)
            ax.set_ylabel('Time', fontsize=12)
            ax.set_title('Spatiotemporal Dynamics of v', fontsize=14)
            plt.colorbar(im, ax=ax, label='Density')
            
        # 6. 相图 (u vs v at center)
        ax = axes[1, 2]
        if len(u_history) > 0:
            center_idx = self.Nx // 2
            u_center = u_history[:, center_idx]
            v_center = v_history[:, center_idx]
            ax.plot(u_center, v_center, 'k-', alpha=0.6)
            ax.plot(u_center[0], v_center[0], 'go', label='Start') # Start
            ax.plot(u_center[-1], v_center[-1], 'ro', label='End') # End
            ax.set_xlabel('u(center)', fontsize=12)
            ax.set_ylabel('v(center)', fontsize=12)
            ax.set_title('Phase Portrait (Center point)', fontsize=14)
            ax.grid(True, alpha=0.3)
            ax.legend()
            
        plt.tight_layout()
        filename = f'competition_dynamics_d{d}_D{D}.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close() # Close to free memory
        print(f"Saved figure: {filename}")
        
        # 返回 u_final, v_final 和 metric
        return u_final, v_final, metric

        ax.set_xlabel('Time', fontsize=12)
        ax.set_ylabel('Total biomass', fontsize=12)
        ax.set_title('Total Biomass Over Time', fontsize=14)
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        
        # 4. 相图：总u vs 总v
        ax = axes[1, 0]
        ax.plot(u_total, v_total, 'k-', linewidth=1.5, alpha=0.7)
        ax.scatter(u_total[0], v_total[0], color='green', s=100, 
                  label='Start', zorder=5)
        ax.scatter(u_total[-1], v_total[-1], color='red', s=100, 
                  label='End', zorder=5)
        ax.set_xlabel('Total u', fontsize=12)
        ax.set_ylabel('Total v', fontsize=12)
        ax.set_title('Phase Portrait', fontsize=14)
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        
        # 5. 空间分布的时间序列（热图）
        ax = axes[1, 1]
        im = ax.imshow(u_history.T, aspect='auto', cmap='Blues',
                      extent=[0, 200, 0, self.L], origin='lower')
        ax.set_xlabel('Time', fontsize=12)
        ax.set_ylabel('Position (x)', fontsize=12)
        ax.set_title('Spatio-temporal Dynamics of u', fontsize=14)
        plt.colorbar(im, ax=ax, label='Density')
        
        # 6. 稳定性分析
        ax = axes[1, 2]
        lambda_val, u_star = self.stability_of_semi_trivial_solution(d, D, c)
        
        ax.plot(self.x, u_star, 'b-', linewidth=2, label='u* (semi-trivial)')
        ax.plot(self.x, self.m, 'g--', linewidth=1.5, label='m(x)', alpha=0.7)
        ax.fill_between(self.x, 0, u_star, alpha=0.3, color='blue')
        ax.set_xlabel('Position (x)', fontsize=12)
        ax.set_ylabel('Density', fontsize=12)
        ax.set_title(f'Semi-trivial Solution\nMetric = {lambda_val:.4f}', fontsize=14)
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        
        # 判断稳定性 (metric > 0 -> Stable)
        if lambda_val > 1e-6:
            stability = "Stable (u wins)"
            color = 'blue'
        elif lambda_val < -1e-6:
            stability = "Unstable (coexistence or v wins)"
            color = 'red'
        else:
            stability = "Neutral"
            color = 'gray'
        
        ax.text(0.05, 0.95, stability, transform=ax.transAxes, 
                fontsize=12, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor=color, alpha=0.3))
        
        plt.tight_layout()
        plt.savefig(f'competition_dynamics_d{d}_D{D}.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return u_final, v_final, lambda_val

def verify_theorem():
    """验证定理：非均匀环境中竞争结果"""
    print("Verifying Theorem...")
    
    # 创建模型
    model = HeterogeneousCompetitionModel(L=10.0, Nx=201, m_type='sinusoidal')
    
    # 计算 c*
    d_values = np.logspace(-2, 2, 50)
    c_star, d_opt, ratios = model.calculate_c_star(d_values)
    
    print(f"c* = inf_d ∫m/∫u* = {c_star:.4f} at d={d_opt:.4f}")
    
    # 选择不同的c值进行模拟
    b = 0.8  # 固定b
    # 我们选择三个代表性的值：
    # 1. c < c* (明显小于，此时 (u*,0) 应该大部分不稳定)
    # 2. c 略大于 c* (此时应该能观察到明显的稳定性分界线 d=D)
    # 3. c 明显大于 c* (强竞争，缓慢扩散者优势更明显)
    c_values = [0.8 * c_star, 1.05 * c_star, 1.3 * c_star]
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 5)) # 修改为1x3布局
    
    for i, c in enumerate(c_values):
        print(f"\nSimulating with c={c:.3f} (c*={c_star:.3f})")
        
        # 分析稳定性区域Σ
        d_test = np.logspace(-1, 1, 25) # 稍微增加分辨率
        D_test = np.logspace(-1, 1, 25)
        
        stability = model.analyze_competition_outcomes(d_test, D_test, b, c)
        
        # 绘制稳定性区域
        ax = axes[i]
        im = ax.imshow(stability, cmap='RdYlBu', extent=[np.log10(D_test[0]), np.log10(D_test[-1]), 
                                                         np.log10(d_test[0]), np.log10(d_test[-1])],
                      aspect='auto', origin='lower', vmin=-1, vmax=1)
        
        # 添加d=D线
        x_vals = np.linspace(np.log10(D_test[0]), np.log10(D_test[-1]), 10)
        ax.plot(x_vals, x_vals, 'k--', linewidth=1.5, alpha=0.6, label='d=D')
        
        ax.set_xlabel('log10(D)', fontsize=12)
        ax.set_ylabel('log10(d)', fontsize=12)
        ax.set_title(f'Stability Region Σ\nc={c:.3f} (ratio={c/c_star:.2f} c*)', fontsize=14)
        
        # 添加颜色条
        if i == 2:
            cbar = plt.colorbar(im, ax=ax)
            cbar.set_label('Stability of (u*,0)', fontsize=12)
            cbar.set_ticks([-1, 0, 1])
            cbar.set_ticklabels(['Unstable (v invades)', 'Neutral', 'Stable (u persistent)'])
        
        ax.legend(fontsize=10, loc='upper right')
        ax.grid(True, alpha=0.3)
        
        # 模拟一个特定点
        if c > c_star:
            # 在Σ内选择一个点
            d = 0.3
            D = 1.0
            print(f"  Testing point (d={d}, D={D}) in Σ")
        else:
            # 在Σ外选择一个点
            d = 1.0
            D = 0.3
            print(f"  Testing point (d={d}, D={D}) outside Σ")
        
        lambda_val, _ = model.stability_of_semi_trivial_solution(d, D, c)
        print(f"  Metric = {lambda_val:.4f} (positive means stable/u wins)")
    
    plt.tight_layout()
    plt.savefig('stability_regions_theorem.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 模拟定理的特殊情况：b=c=1
    print("\n" + "="*60)
    print("SIMULATING THEOREM: b=c=1")
    print("="*60)
    
    b = 1.0
    c = 1.0
    
    # 情况1: d < D
    d1, D1 = 0.5, 1.0
    print(f"\nCase 1: d={d1} < D={D1}")
    u_final1, v_final1, lambda1 = model.plot_competition_dynamics(d1, D1, b, c)
    print(f"  Metric = {lambda1:.4f}")
    
    # 情况2: d > D
    d2, D2 = 1.0, 0.5
    print(f"\nCase 2: d={d2} > D={D2}")
    u_final2, v_final2, lambda2 = model.plot_competition_dynamics(d2, D2, b, c)
    print(f"  Metric = {lambda2:.4f}")

    # 情况3: d = D
    d3, D3 = 1.0, 1.0
    print(f"\nCase 3: d={d3} = D={D3}")
    u_final3, v_final3, lambda3 = model.plot_competition_dynamics(d3, D3, b, c)
    print(f"  Metric = {lambda3:.4f}")

verify_theorem()
```

## 2.4.6 图灵不稳定性与空间格局形成

### 2.4.6.1 图灵机制

1952年，图灵提出：两种具有不同扩散速率的物质（形态发生素）通过反应-扩散相互作用，可以自发形成空间斑图。这一机制同样适用于生态学中的捕食者-猎物系统或竞争系统。

考虑一般两变量反应-扩散系统：
$$
\begin{aligned}
\frac{\partial u}{\partial t} &= f(u,v) + D_u\nabla^2 u,\\
\frac{\partial v}{\partial t} &= g(u,v) + D_v\nabla^2 v.
\end{aligned}
$$
设 $(u^*,v^*)$ 为无扩散时的稳定平衡点（即 $f(u^*,v^*)=g(u^*,v^*)=0$，且 Jacobian 矩阵的特征值均有负实部）。加入扩散后，线性稳定性分析表明，若 $D_v\neq D_u$，且满足一定条件（通常要求 $D_v>D_u$），则均匀稳态可能对某些空间扰动变得不稳定，从而产生空间斑图。这种现象称为 **图灵不稳定性**。

### 2.4.6.2 经典模型：Schnakenberg 系统

Schnakenberg 模型（Brusselator 的简化版）是产生图灵斑图的经典例子：
$$
\begin{aligned}
f(u,v) &= a - u + u^2 v,\\
g(u,v) &= b - u^2 v,
\end{aligned}
$$
其中 $a,b>0$。通过线性稳定性分析可导出图灵不稳定的参数区域。数值模拟显示，从均匀初值添加微小随机扰动后，系统会演化出点状、条纹状或迷宫状的空间斑图，其主导波长可通过傅里叶分析确定。

```python-plot
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class ReactionDiffusion2D:
    """二维反应-扩散方程求解器"""
    
    def __init__(self, Du, Dv, a, b, L, T, nx=101, ny=101, nt=10000):
        """
        参数:
            Du, Dv: 扩散系数
            a, b: 反应参数
            L: 正方形区域边长
            T: 总时间
            nx, ny: 空间网格点数
            nt: 时间步数
        """
        self.Du = Du
        self.Dv = Dv
        self.a = a
        self.b = b
        self.L = L
        self.T = T
        self.nx = nx
        self.ny = ny
        self.nt = nt
        
        # 空间和时间步长
        self.dx = L / (nx - 1)
        self.dy = L / (ny - 1)
        self.dt = T / nt
        
        # 空间网格
        self.x = np.linspace(0, L, nx)
        self.y = np.linspace(0, L, ny)
        self.X, self.Y = np.meshgrid(self.x, self.y)
        
        # 稳定性检查
        s_u = Du * self.dt / (self.dx ** 2 + self.dy ** 2)
        s_v = Dv * self.dt / (self.dx ** 2 + self.dy ** 2)
        if s_u > 0.25 or s_v > 0.25:
            print(f"警告：稳定性参数 s_u = {s_u:.3f}, s_v = {s_v:.3f}")
            print(f"建议：减小 dt")
    
    def laplacian_2d(self, u):
        """计算二维拉普拉斯算子（五点差分格式）"""
        # 使用零通量边界条件（Neumann边界）
        u_padded = np.pad(u, 1, mode='edge')
        
        # 五点差分格式
        laplacian = (u_padded[2:, 1:-1] + u_padded[:-2, 1:-1] + 
                     u_padded[1:-1, 2:] + u_padded[1:-1, :-2] - 4 * u_padded[1:-1, 1:-1])
        
        return laplacian / (self.dx * self.dy)
    
    def reaction_terms(self, u, v):
        """Schnakenberg模型反应项"""
        f = self.a - u + u**2 * v
        g = self.b - u**2 * v
        return f, g
    
    def solve_explicit(self, u0_func, v0_func):
        """
        显式方法求解反应-扩散方程
        
        参数:
            u0_func, v0_func: 初始条件函数
        """
        # 初始化
        u = np.zeros((self.nx, self.ny))
        v = np.zeros((self.nx, self.ny))
        
        for i in range(self.nx):
            for j in range(self.ny):
                u[i, j] = u0_func(self.x[i], self.y[j])
                v[i, j] = v0_func(self.x[i], self.y[j])
        
        # 存储时间演化
        u_history = [u.copy()]
        v_history = [v.copy()]
        
        # 时间迭代
        for n in range(self.nt):
            # 计算拉普拉斯算子
            laplacian_u = self.laplacian_2d(u)
            laplacian_v = self.laplacian_2d(v)
            
            # 计算反应项
            f, g = self.reaction_terms(u, v)
            
            # 更新
            u_new = u + self.dt * (self.Du * laplacian_u + f)
            v_new = v + self.dt * (self.Dv * laplacian_v + g)
            
            # 确保非负
            u_new = np.maximum(u_new, 0)
            v_new = np.maximum(v_new, 0)
            
            u, v = u_new, v_new
            
            # 每隔一定步数保存
            if n % 100 == 0:
                u_history.append(u.copy())
                v_history.append(v.copy())
        
        return np.array(u_history), np.array(v_history)

# 参数设置：图灵模式条件
L = 20.0          # 区域边长
T = 100.0         # 总时间

# 扩散系数：Dv远大于Du（图灵不稳定的必要条件）
Du = 0.1
Dv = 1.0

# 反应参数
a = 0.1
b = 0.9

# 初始条件：均匀稳态加微小随机扰动
u0_homog = a + b
v0_homog = b / (a + b)**2

def u0_perturbed(x, y):
    return u0_homog + 0.01 * np.random.randn()

def v0_perturbed(x, y):
    return v0_homog + 0.01 * np.random.randn()

# 创建求解器
solver_rd = ReactionDiffusion2D(Du, Dv, a, b, L, T, nx=101, ny=101, nt=20000)

# 求解
print("求解二维反应-扩散方程...")
u_history, v_history = solver_rd.solve_explicit(u0_perturbed, v0_perturbed)

# 可视化
fig3, axes3 = plt.subplots(2, 3, figsize=(15, 10))

# 计算正确的帧索引
# 每一帧代表的时间 = save_interval * dt = 100 * (100/20000) = 0.5
frames_per_unit_time = 1.0 / (100 * solver_rd.dt)
target_times = [0, 20, 40, 60, 80, 100]
time_indices = [int(t * frames_per_unit_time) for t in target_times]
# 修正最后一个索引防止越界
if time_indices[-1] >= len(u_history):
    time_indices[-1] = len(u_history) - 1

titles = [f't = {t}' for t in target_times]

for i, (idx, title) in enumerate(zip(time_indices, titles)):
    ax = axes3[i//3, i%3]
    
    # 确保索引有效
    idx = min(idx, len(u_history)-1)
    
    # 显示u的分布
    im = ax.imshow(u_history[idx], cmap='RdBu', origin='lower', 
                   extent=[0, L, 0, L], vmin=0.8*u0_homog, vmax=1.2*u0_homog)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title(title, fontsize=14)
    
    # 添加颜色条
    if i == 5:
        fig3.colorbar(im, ax=ax, shrink=0.8)

fig3.suptitle('Schnakenberg Model: Turing Pattern Formation', fontsize=16)
plt.tight_layout()
plt.savefig('turing_pattern.png', dpi=300)
plt.show()

# 绘制功率谱分析
fig4, axes4 = plt.subplots(1, 2, figsize=(12, 5))

# 最终状态的二维傅里叶变换
u_final = u_history[-1]
v_final = v_history[-1]

# 去除均值（直流分量），只分析波动模式
u_fluctuation = u_final - np.mean(u_final)

# 计算二维傅里叶变换
u_fft = np.fft.fft2(u_fluctuation)
# v_fft = np.fft.fft2(v_final - np.mean(v_final))

# 计算功率谱
u_power = np.abs(np.fft.fftshift(u_fft))**2
# v_power = np.abs(np.fft.fftshift(v_fft))**2

# 频率坐标
freq_x = np.fft.fftshift(np.fft.fftfreq(u_final.shape[0], d=solver_rd.dx))
freq_y = np.fft.fftshift(np.fft.fftfreq(u_final.shape[1], d=solver_rd.dy))

# 绘制u的功率谱
im1 = axes4[0].imshow(np.log10(u_power+1), cmap='viridis', origin='lower',
                      extent=[freq_x[0], freq_x[-1], freq_y[0], freq_y[-1]])
axes4[0].set_xlabel('Spatial frequency $k_x$', fontsize=12)
axes4[0].set_ylabel('Spatial frequency $k_y$', fontsize=12)
axes4[0].set_title('Power spectrum of $u$ (log scale)', fontsize=14)
fig4.colorbar(im1, ax=axes4[0])

# 绘制径向平均功率谱
kx_grid, ky_grid = np.meshgrid(freq_x, freq_y)
k_radial = np.sqrt(kx_grid**2 + ky_grid**2)

# 分箱计算径向平均
k_bins = np.linspace(0, np.max(k_radial), 50)
k_bin_centers = (k_bins[:-1] + k_bins[1:]) / 2
u_radial_mean = np.zeros(len(k_bin_centers))

for i in range(len(k_bin_centers)):
    mask = (k_radial >= k_bins[i]) & (k_radial < k_bins[i+1])
    if np.any(mask):
        u_radial_mean[i] = np.mean(u_power[mask])

axes4[1].plot(k_bin_centers, u_radial_mean, 'b-', linewidth=2)
axes4[1].set_xlabel('Wavenumber $k$', fontsize=12)
axes4[1].set_ylabel('Radially averaged power', fontsize=12)
axes4[1].set_title('Radial power spectrum', fontsize=14)
axes4[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('turing_pattern_spectrum.png', dpi=300)
plt.show()
```

### 2.4.6.3 捕食者-猎物模型中的图灵斑图

考虑具有逻辑斯谛增长的捕食者-猎物模型：
$$
\begin{aligned}
\frac{\partial N}{\partial t} &= rN\left(1-\frac{N}{K}\right)-aNP + D_N\nabla^2 N,\\
\frac{\partial P}{\partial t} &= caNP - mP + D_P\nabla^2 P,
\end{aligned}
$$
其中 $N$ 为猎物密度，$P$ 为捕食者密度。当捕食者扩散系数 $D_P$ 远大于猎物扩散系数 $D_N$ 时，系统可能产生图灵斑图，形成捕食者与猎物密度的空间异质性分布。

```python-plot
"""
turing_patterns.py
Simulation of Turing patterns in predator-prey systems
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import laplace

class TuringPatternSimulator:
    """2D Turing pattern simulator for predator-prey system"""
    
    def __init__(self, size=100, dt=0.1, dx=1.0):
        """
        Initialize Turing pattern simulator
        
        Parameters:
        -----------
        size : int
            Grid size (size x size)
        dt : float
            Time step
        dx : float
            Spatial step
        """
        self.size = size
        self.dt = dt
        self.dx = dx
        
        # Model parameters (predator-prey with Holling Type II and self-limitation)
        self.params = {
            'r': 1.0,      # Prey growth rate
            'K': 1.0,      # Carrying capacity
            'a': 1.0,      # Predation rate
            'c': 2.0,      # Conversion efficiency
            'm': 0.5,      # Predator mortality
            'H': 0.3,      # Half-saturation constant (Holling II)
            'delta': 0.1,  # Predator self-limitation (quadratic mortality)
            'D_N': 0.02,   # Prey diffusion coefficient
            'D_P': 1.0,    # Predator diffusion coefficient
        }
        
        # Initialize grids with Turing-friendly initial conditions
        # Start near the expected homogeneous equilibrium to facilitate pattern formation
        self.N = 0.3 * np.ones((size, size)) 
        self.P = 0.3 * np.ones((size, size))
        
        # Add random perturbations
        self.N += 0.02 * np.random.randn(size, size)
        self.P += 0.02 * np.random.randn(size, size)
        
        # Apply reflecting boundary conditions
        self.set_boundary_conditions()
    
    def set_boundary_conditions(self):
        """Set reflecting (Neumann) boundary conditions"""
        pass
    
    def reaction_terms(self, N, P):
        """Calculate local reaction terms with Holling Type II response"""
        r, K, a, c, m, H, delta = (self.params[k] for k in ['r', 'K', 'a', 'c', 'm', 'H', 'delta'])
        
        # Holling Type II functional response: a*N/(N+H)
        predation = a * N * P / (N + H)
        
        # Prey: Logistic growth - Predation
        f_N = r * N * (1 - N/K) - predation
        
        # Predator: Conversion * Predation - Mortality - Self-limitation
        f_P = c * predation - m * P - delta * P**2
        
        return f_N, f_P
    
    def diffusion_terms(self, grid, D):
        """Calculate diffusion term using discrete Laplacian"""
        # Using 5-point stencil for 2D Laplacian
        laplacian = laplace(grid, mode='reflect') / self.dx**2
        return D * laplacian
    
    def step(self):
        """Perform one time step using explicit Euler method"""
        # Calculate reaction terms
        f_N, f_P = self.reaction_terms(self.N, self.P)
        
        # Calculate diffusion terms
        diff_N = self.diffusion_terms(self.N, self.params['D_N'])
        diff_P = self.diffusion_terms(self.P, self.params['D_P'])
        
        # Update populations
        self.N += self.dt * (f_N + diff_N)
        self.P += self.dt * (f_P + diff_P)
        
        # Ensure non-negative values
        self.N = np.maximum(self.N, 0.0)
        self.P = np.maximum(self.P, 0.0)
        
        return self.N, self.P
    
    def simulate(self, steps=5000, save_interval=100):
        """Run simulation"""
        # Arrays to store snapshots
        n_snapshots = steps // save_interval + 1
        N_snapshots = np.zeros((n_snapshots, self.size, self.size))
        P_snapshots = np.zeros((n_snapshots, self.size, self.size))
        
        # Save initial state
        N_snapshots[0] = self.N.copy()
        P_snapshots[0] = self.P.copy()
        
        snapshot_idx = 1
        
        # Time stepping
        for i in range(1, steps + 1):
            self.step()
            
            if i % save_interval == 0 and snapshot_idx < n_snapshots:
                N_snapshots[snapshot_idx] = self.N.copy()
                P_snapshots[snapshot_idx] = self.P.copy()
                snapshot_idx += 1
        
        return N_snapshots[:snapshot_idx], P_snapshots[:snapshot_idx]
    
    def analyze_turing_conditions(self):
        """Analyze Turing instability conditions for Holling Type II model"""
        # Unpack parameters
        r, K, a, c, m, H, delta = (self.params[k] for k in ['r', 'K', 'a', 'c', 'm', 'H', 'delta'])
        D_N, D_P = self.params['D_N'], self.params['D_P']
        
        # Calculate homogeneous equilibrium numerically or analytically
        # N* is determined by P-isocline: c*a*N/(N+H) = m + delta*P
        # P* is determined by N-isocline: r(1-N/K) = a*P/(N+H) => P = r/a*(1-N/K)*(N+H)
        # Substitute P into first eq:
        # c*a*N/(N+H) - m - delta * [(r/a)*(1-N/K)*(N+H)] = 0
        
        def func(n):
            if n <= 0.001 or n >= K: return 1e9
            p = (r/a) * (1 - n/K) * (n + H)
            return c * a * n / (n + H) - m - delta * p
        
        # Scan to find root
        n_vals = np.linspace(0.01, K-0.01, 1000)
        y_vals = [func(n) for n in n_vals]
        idx = np.argmin(np.abs(y_vals))
        N_star = n_vals[idx]
        P_star = (r/a) * (1 - N_star/K) * (N_star + H)
        
        print(f"Homogeneous equilibrium:")
        print(f"  N* = {N_star:.4f}, P* = {P_star:.4f}")
        
        # Jacobian elements
        # fN = r*N*(1-N/K) - a*N*P/(N+H)
        # J11 = d(fN)/dN
        #     = r(1-2N/K) - a*P * [ ((N+H) - N) / (N+H)^2 ]
        J11 = r * (1 - 2*N_star/K) - a * P_star * H / ((N_star + H)**2)
        
        # J12 = d(fN)/dP = -a*N/(N+H)
        J12 = -a * N_star / (N_star + H)
        
        # fP = c*a*N*P/(N+H) - m*P - delta*P^2
        # J21 = d(fP)/dN = c*a*P * [ H / (N+H)^2 ]
        J21 = c * a * P_star * H / ((N_star + H)**2)
        
        # J22 = d(fP)/dP = c*a*N/(N+H) - m - 2*delta*P
        # At eq: c*a*N/(N+H) - m = delta*P
        # So J22 = delta*P - 2*delta*P = -delta*P
        J22 = -delta * P_star
        
        J = np.array([[J11, J12], [J21, J22]])
        
        print(f"\nJacobian at equilibrium:")
        print(f"  J = [[{J11:.4f}, {J12:.4f}],")
        print(f"       [{J21:.4f}, {J22:.4f}]]")
        
        # Eigenvalues without diffusion
        eigvals = np.linalg.eigvals(J)
        print(f"\nEigenvalues (without diffusion):")
        print(f"  λ1 = {eigvals[0]:.4f}, λ2 = {eigvals[1]:.4f}")
        print(f"  Real parts: {np.real(eigvals[0]):.4f}, {np.real(eigvals[1]):.4f}")
        
        # Turing conditions
        trace = np.trace(J) # J11 + J22
        det = np.linalg.det(J) # J11*J22 - J12*J21
        
        # Condition 1: Linear stability without diffusion (Trace < 0 and Det > 0)
        condition1 = (trace < 0) and (det > 0)
        
        # Condition 2: Instability with diffusion
        # D_P*J11 + D_N*J22 > 2*sqrt(D_N*D_P*det)
        lhs = D_P * J11 + D_N * J22
        rhs = 2 * np.sqrt(D_N * D_P * det) if det > 0 else 0
        condition2 = lhs > rhs
        
        print(f"\nTuring instability conditions:")
        print(f"  1. Stable w/o diffusion (Tr<0, Det>0): {condition1} (Tr={trace:.4f}, Det={det:.4f})")
        print(f"  2. Unstable w/ diffusion (LHS > RHS): {condition2} ({lhs:.4f} > {rhs:.4f})")
        
        turing_possible = condition1 and condition2
        
        if turing_possible:
            print(f"\n✅ Turing instability is expected!")
        else:
            print(f"\n❌ Turing instability conditions not satisfied")
        
        return condition1, turing_possible

def visualize_turing_patterns(N_snapshots, P_snapshots):
    """Visualize Turing pattern evolution"""
    n_snapshots = len(N_snapshots)
    
    # Create figure with multiple snapshots
    fig, axes = plt.subplots(2, min(4, n_snapshots), figsize=(15, 8))
    
    # Select snapshots to display
    step_indices = np.linspace(0, n_snapshots-1, min(4, n_snapshots), dtype=int)
    
    for idx, step_idx in enumerate(step_indices):
        # Prey patterns
        ax1 = axes[0, idx]
        im1 = ax1.imshow(N_snapshots[step_idx], cmap='viridis', 
                        vmin=0, vmax=1.5, origin='lower')
        ax1.set_title(f'Prey (t = {step_idx*100})', fontsize=12)
        ax1.axis('off')
        plt.colorbar(im1, ax=ax1, fraction=0.046, pad=0.04)
        
        # Predator patterns
        ax2 = axes[1, idx]
        im2 = ax2.imshow(P_snapshots[step_idx], cmap='plasma',
                        vmin=0, vmax=1.5, origin='lower')
        ax2.set_title(f'Predator (t = {step_idx*100})', fontsize=12)
        ax2.axis('off')
        plt.colorbar(im2, ax=ax2, fraction=0.046, pad=0.04)
    
    plt.tight_layout()
    
    # Add spatial spectrum analysis for the final pattern
    fig2, axes2 = plt.subplots(1, 3, figsize=(15, 5))
    
    # Final prey pattern
    ax1 = axes2[0]
    im1 = ax1.imshow(N_snapshots[-1], cmap='viridis', origin='lower')
    ax1.set_title('Final Prey Pattern', fontsize=14)
    ax1.axis('off')
    plt.colorbar(im1, ax=ax1)
    
    # Final predator pattern
    ax2 = axes2[1]
    im2 = ax2.imshow(P_snapshots[-1], cmap='plasma', origin='lower')
    ax2.set_title('Final Predator Pattern', fontsize=14)
    ax2.axis('off')
    plt.colorbar(im2, ax=ax2)
    
    # 2D Fourier transform of prey pattern
    ax3 = axes2[2]
    pattern_fft = np.fft.fft2(N_snapshots[-1])
    pattern_fft_shifted = np.fft.fftshift(pattern_fft)
    magnitude_spectrum = np.log(1 + np.abs(pattern_fft_shifted))
    
    im3 = ax3.imshow(magnitude_spectrum, cmap='hot', origin='lower')
    ax3.set_title('Fourier Spectrum (Prey)', fontsize=14)
    ax3.axis('off')
    plt.colorbar(im3, ax=ax3)
    
    # Add circle showing dominant wavelength
    center = (magnitude_spectrum.shape[0]//2, magnitude_spectrum.shape[1]//2)
    radius = 15  # This corresponds to pattern wavelength
    circle = plt.Circle(center, radius, color='cyan', fill=False, linewidth=2)
    ax3.add_patch(circle)
    
    plt.tight_layout()
    
    return fig, fig2

def explore_parameter_space():
    """Explore different parameter regimes for Turing patterns"""
    
    parameter_sets = [
        {
            'name': 'Standard Turing patterns',
            # Parameters tuned for Turing instability:
            # D_N reduced, D_P increased (Ratio 200)
            # delta increased to stabilize homogeneous equilibrium
            'params': {'D_N': 0.1, 'D_P': 20.0, 'r': 1.0, 'K': 1.0, 
                       'a': 1.0, 'c': 2.0, 'm': 0.55, 'H': 0.3, 'delta': 0.4},
            'expected': 'Spot/Labyrinth patterns'
        },
        {
            'name': 'Different Pattern Mode',
            # Varying delta slightly
            'params': {'D_N': 0.1, 'D_P': 20.0, 'r': 1.0, 'K': 1.0, 
                       'a': 1.0, 'c': 2.0, 'm': 0.55, 'H': 0.3, 'delta': 0.5},
            'expected': 'Alternative patterns'
        },
        {
            'name': 'No Turing (Low diffusion ratio)',
            # Set D_P close to D_N
            'params': {'D_N': 1.0, 'D_P': 2.0, 'r': 1.0, 'K': 1.0, 
                       'a': 1.0, 'c': 2.0, 'm': 0.55, 'H': 0.3, 'delta': 0.4},
            'expected': 'Homogeneous state'
        }
    ]
    
    all_results = []
    
    for i, ps in enumerate(parameter_sets):
        print(f"\n{'='*60}")
        print(f"Case {i+1}: {ps['name']}")
        print(f"{'='*60}")
        
        # Create simulator with given parameters
        # Adjust dt for stability: D * dt / dx^2 < 0.25
        # Max D is 20. dx=1. dt < 0.0125. Use 0.01
        simulator = TuringPatternSimulator(size=60, dt=0.01, dx=1.0)
        
        # Update parameters
        for key, value in ps['params'].items():
            if key in simulator.params:
                simulator.params[key] = value
        
        # Analyze Turing conditions
        stable_no_diff, turing_possible = simulator.analyze_turing_conditions()
        
        # Run simulation
        print("\nRunning simulation...")
        # Reduce steps but increase plot frequency since dt is small
        # Total T = 20000 * 0.005 = 100
        N_snapshots, P_snapshots = simulator.simulate(steps=20000, save_interval=1000)
        
        # Store results
        all_results.append({
            'name': ps['name'],
            'params': ps['params'],
            'turing_possible': turing_possible,
            'N_snapshots': N_snapshots,
            'P_snapshots': P_snapshots
        })
        
        # Visualize
        fig1, fig2 = visualize_turing_patterns(N_snapshots, P_snapshots)
        # Fix title and text
        plt.figure(fig1.number)
        fig1.suptitle(f"{ps['name']}\nD_N={ps['params']['D_N']}, D_P={ps['params']['D_P']}", 
                     fontsize=16)
        
        # Fix: visualize_turing_patterns uses step number to display time
        # The time is step_idx * save_interval * dt
        # Current logic: step_idx * 100. Let's fix axes titles in visualize_turing_patterns instead if possible
        # Or just accept it displays step number
        
        fig1.savefig(f'turing_patterns_case_{i+1}.png', dpi=300, bbox_inches='tight')
        fig2.savefig(f'turing_spectrum_case_{i+1}.png', dpi=300, bbox_inches='tight')
        plt.close('all') # Close figures to free memory
    
    return all_results

print("Turing Pattern Formation in Predator-Prey Systems")
print("="*60)

# Explore different parameter regimes
results = explore_parameter_space()

plt.show()
```

## 2.4.7 移流效应

除随机扩散外，许多生物还能沿环境梯度进行定向运动，即 **移流（advection）**。Belgacem 和 Cosner 提出的包含移流的模型：

### 2.4.7.1 单种群移流模型

$$
\begin{cases}
u_t = \nabla\cdot[d\nabla u - \alpha u\nabla m] + u(m - u), & (x,t)\in\Omega\times(0,\infty),\\[6pt]
\dfrac{\partial u}{\partial\nu} - \alpha u\dfrac{\partial m}{\partial\nu}=0, & (x,t)\in\partial\Omega\times(0,\infty),\\[6pt]
u(x,0)=u_0(x), & x\in\Omega,
\end{cases}
$$
其中 $\alpha$ 是移流系数，描述物种沿资源梯度 $\nabla m$ 的定向运动。边界条件意味着移流通量与扩散通量在边界上平衡。

### 2.4.7.2 包含移流的竞争模型

Cantrell 等人进一步研究了两种群的竞争，其中一种具有移流能力：
$$
\begin{cases}
u_t = \nabla\cdot[d\nabla u - \alpha u\nabla m] + u(m - u - v),\\[4pt]
v_t = D\Delta v + v(m - u - v),\\[4pt]
d\dfrac{\partial u}{\partial\nu} - \alpha u\dfrac{\partial m}{\partial\nu}=0,\quad \dfrac{\partial v}{\partial\nu}=0,
\end{cases}
$$
移流物种 $u$ 沿资源梯度运动，而非移流物种 $v$ 仅作随机扩散。一个重要结论是：

当移流系数 $\alpha$ 充分大时，两个半平凡平衡态 $(u^*,0)$ 和 $(0,v^*)$ 都不稳定，系统至少存在一个稳定的正平衡解，即两物种可以共存。

这揭示了一个反直觉的现象：过强的定向运动反而会削弱物种的竞争优势，促使共存。数值实验可验证：小 $\alpha$ 时移流物种占优；随着 $\alpha$ 增大，系统由竞争排除转变为共存。

```python-plot
"""
advection_competition_model.py
包含移流的竞争模型数值模拟
验证定理：移流系数对竞争结果的影响
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags, csr_matrix
from scipy.sparse.linalg import spsolve

class AdvectionCompetitionModel:
    """包含移流的竞争模型求解器"""
    
    def __init__(self, L=10.0, Nx=61):
        """
        初始化模型参数
        
        参数:
        L : 空间域长度
        Nx : 空间网格点数
        """
        self.L = L
        self.Nx = Nx
        self.x = np.linspace(0, L, Nx)
        self.dx = self.x[1] - self.x[0]
        
        # 资源分布函数 m(x)
        self.m = self._resource_function()
        
        # 计算资源梯度
        self.m_grad = np.gradient(self.m, self.dx)
        
        # 默认参数
        self.d = 1.0  # 物种u的扩散系数
        self.D = 1.0  # 物种v的扩散系数
    
    def _resource_function(self):
        """资源分布函数 m(x) - 非均匀分布"""
        # 多个局部最大值
        m = 1.0 + 0.5 * np.sin(2 * np.pi * self.x / self.L)
        m += 0.3 * np.exp(-(self.x - self.L/4)**2)
        m += 0.3 * np.exp(-(self.x - 3*self.L/4)**2)
        return m
    
    def construct_advection_diffusion_matrix(self, d, alpha):
        """构造包含移流的扩散-移流算子的矩阵表示
        使用守恒型迎风格式 (Conservative Upwind Scheme) 以保证数值稳定性
        """
        N = self.Nx
        dx = self.dx
        
        # 1. 扩散部分 (d * u_xx)
        # ------------------------------------------------
        alpha_diff = d / (dx ** 2)
        main_diag = -2 * alpha_diff * np.ones(N)
        upper_diag = alpha_diff * np.ones(N-1)
        lower_diag = alpha_diff * np.ones(N-1)
        
        # 2. 移流部分 (- div(alpha * u * grad(m)))
        # ------------------------------------------------
        
        # 初始化advection variables
        factor = 1.0 / dx
        v_plus = np.zeros(N-1)
        v_minus = np.zeros(N-1)
        
        if alpha > 1e-10:
            # 计算网格界面的速度 v = alpha * m'
            # m 是 N 个点，m[0]...m[N-1]
            # 界面有 N-1 个: 0.5, 1.5, ..., N-1.5
            # v_{i+1/2} 对应索引 i (0 到 N-2)
            
            m_diff = np.diff(self.m) # m[i+1] - m[i]
            v_interface = alpha * m_diff / dx
            
            # 迎风通量贡献到矩阵
            # J_{i+1/2} = max(v,0)*u_i + min(v,0)*u_{i+1}
            # term at i:   - J_{i+1/2} / dx  => -1/dx * (v+ u_i + v- u_{i+1})
            # term at i+1: + J_{i+1/2} / dx  => +1/dx * (v+ u_i + v- u_{i+1})
            
            v_plus = np.maximum(v_interface, 0)
            v_minus = np.minimum(v_interface, 0)
            
            factor = 1.0 / dx
            
            # 对主对角线的贡献 (u_i)
            # 来自 -J_{i+1/2}: -factor * v_plus[i]
            # 来自 +J_{i-1/2}: +factor * v_minus[i-1]
            main_diag[:-1] -= factor * v_plus
            main_diag[1:]  += factor * v_minus
            
            # 对上对角线的贡献 (u_{i+1})
            # 来自 -J_{i+1/2}: -factor * v_minus[i] (在第i行，第i+1列)
            upper_diag[:] -= factor * v_minus
            
            # 对下对角线的贡献 (u_{i-1})
            # 来自 +J_{i-1/2}: +factor * v_plus[i-1] (在第i行，第i-1列)
            lower_diag[:] += factor * v_plus
            
        # 3. 边界条件 (诺伊曼零流)
        # ------------------------------------------------
        # 扩散部分边界修正
        main_diag[0] += alpha_diff   # u_(-1) = u_1 (镜像) -> -2a u_0 + a u_1 + a u_(-1) -> -2a u_0 + 2a u_1 (Error in std logical?)
        # Std Neumann: (u_1 - u_(-1))/2dx = 0 => u_(-1) = u_1.
        # Laplacian at 0: (u_1 - 2u_0 + u_(-1))/dx^2 = (2u_1 - 2u_0)/dx^2.
        # Original code had: main_diag[0] = -alpha_diff, off_diag=alpha. (-1, 1).
        # This corresponds to forward difference u_xx ~ (u_1 - u_0)/dx^2 ? No.
        # Let's stick to the original diffusion boundary logic which was:
        # main_diag[0] = -alpha_diff (-1), off_diag (1). Sum = 0. Conservative.
        
        # Reset boundary elements for diffusion to match original simple implementation
        # The original implementation:
        # main_diag[0] = -alpha_diff
        # main_diag[-1] = -alpha_diff
        # This implies flux = 0 at boundary naturally?
        # J_diff = -d du/dx. 
        # Finite volume: div J at 0. J_{1/2} - J_{-1/2}. J_{-1/2}=0.
        # J_{1/2} = -d (u_1 - u_0)/dx.
        # -div J = - (J_{1/2} - 0)/dx = d(u_1-u_0)/dx^2 = alpha(u_1 - u_0).
        # Matrix row 0: -alpha u_0 + alpha u_1. Correct.
        
        # So we just need to ensure advection flux is also 0 at boundary.
        # J_adv_{-1/2} = 0, J_adv_{N-1/2} = 0.
        # My loops above for advection cover indices 0 to N-2 (interfaces).
        # Interface i=0 corresponds to x_{0.5}.
        # Wait, indices. v_interface has N-1 elements. 0..N-2.
        # i=0 is between node 0 and 1.
        # Node 0 update: - (J_{0.5} - J_{-0.5})/dx.
        # We assume J_{-0.5}=0 (BC).
        # So Node 0 gets -J_{0.5}/dx.
        # J_{0.5} = v+ u_0 + v- u_1.
        # Row 0: coeff u_0 is -v+_0/dx. coeff u_1 is -v-_0/dx.
        # This is handled by `main_diag[:-1] -= ...` (at i=0) and `upper_diag[:] -= ...` (at i=0).
        # Correct.
        
        # Node N-1 update: - (J_{N-1/2} - J_{N-1.5})/dx.
        # Assume J_{N-1/2}=0.
        # So Node N-1 gets +J_{N-1.5}/dx.
        # J_{N-1.5} corresponds to interface N-2 (last element of v).
        # Row N-1: coeff u_{N-1} is +v-_{N-2}/dx. coeff u_{N-2} is +v+_{N-2}/dx.
        # This is handled by `main_diag[1:] += ...` (at i=N-2 -> index N-1) and `lower_diag[:] += ...` (at i=N-2 -> index N-1).
        # Correct.
        
        # 重置扩散的边界条件 (覆盖掉上面的累加结果，因为我想保留扩散部分的原始逻辑，还是叠加？)
        # 上面的代码是累加的 (main_diag_diff + main_diag_adv).
        # 这里我直接初始化了 main/upper/lower 为扩散部分。
        # 只需要修正扩散部分的Boundary即可。
        # 扩散部分:
        main_diag[0] = -alpha_diff - factor * v_plus[0] 
        main_diag[-1] = -alpha_diff + factor * v_minus[-1]
        
        # 构造矩阵
        A = diags([lower_diag, main_diag, upper_diag], [-1, 0, 1], format='csr')
        
        return A
    
    def simulate_advection_competition(self, d, D, alpha, T=1000.0, dt=None):
        """模拟包含移流的竞争动力学"""
        # 估算最大梯度
        max_grad_m = np.max(np.abs(self.m_grad))
        
        # 自动计算合适的时间步长以满足稳定性条件 (CFL Condition)
        # 降低安全系数从 0.4 到 0.2 以防止极端情况下的数值溢出
        # 1. 扩散限制: dt <= 0.5 * dx^2 / D
        max_diff = max(d, D)
        dt_diff = 0.2 * (self.dx ** 2) / max_diff + 1e-12
        
        # 2. 移流限制: dt <= dx / v_max, 其中 v_max = alpha * |grad(m)|
        if alpha > 1e-6 and max_grad_m > 1e-6:
            v_max = alpha * max_grad_m
            dt_adv = 0.2 * self.dx / v_max
        else:
            dt_adv = 1.0 # 很大
            
        dt_stable = min(dt_diff, dt_adv)
        
        # 如果未指定dt或指定的dt太大，则使用稳定步长
        if dt is None or dt > dt_stable:
            dt = dt_stable
            
        N = self.Nx
        Nt = int(T / dt)
        
        # 初始条件
        u0 = 0.3 * np.ones(N) + 0.05 * np.random.randn(N)
        v0 = 0.3 * np.ones(N) + 0.05 * np.random.randn(N)
        u0 = np.maximum(u0, 0)
        v0 = np.maximum(v0, 0)
        
        # 构造算子矩阵
        A_u = self.construct_advection_diffusion_matrix(d, alpha)  # 包含移流
        A_v = self.construct_advection_diffusion_matrix(D, 0.0)    # 无移流
        
        # 时间演化
        u = u0.copy()
        v = v0.copy()
        
        u_history = [u.copy()]
        v_history = [v.copy()]
        
        # 记录每多少步保存一次，总共保存约200帧
        save_interval = max(1, int(Nt / 200))
        check_interval = max(100, int(Nt / 500)) # 每隔一定步数检查稳态/灭绝
        
        for n in range(1, Nt):
            # 反应项
            # 限制数值范围防止溢出
            u_safe = np.clip(u, 0, 1e5)
            v_safe = np.clip(v, 0, 1e5)
            
            reaction_u = u_safe * (self.m - u_safe - v_safe)
            reaction_v = v_safe * (self.m - u_safe - v_safe)
            
            # 更新
            u_new = u + dt * (A_u.dot(u) + reaction_u)
            v_new = v + dt * (A_v.dot(v) + reaction_v)
            
            # 确保非负
            u = np.maximum(u_new, 0)
            v = np.maximum(v_new, 0)
            
            # 检查是否满足提前停止条件
            if n % check_interval == 0:
                u_max = np.max(u)
                v_max = np.max(v)
                
                # 1. 灭绝检测
                if u_max < 1e-4 or v_max < 1e-4:
                    # 某个物种灭绝了，无需继续
                    # 继续填充剩下的历史记录以便绘图（用最后一帧填充）
                    remaining_frames = (Nt - n) // save_interval
                    for _ in range(remaining_frames):
                        u_history.append(u.copy())
                        v_history.append(v.copy())
                    break
                    
                # 2. 稳态检测 (可选，稍微复杂点，暂略以保证稳健)

            # 保存结果
            if n % save_interval == 0:
                u_history.append(u.copy())
                v_history.append(v.copy())
        
        # 确保最后一步也被保存
        u_history.append(u.copy())
        v_history.append(v.copy())
        
        return np.array(u_history), np.array(v_history)
    
    def analyze_alpha_dependence(self, d=1.0, D=1.0, alpha_values=np.logspace(-2, 2, 20)):
        """分析移流系数α对竞争结果的影响"""
        N_alpha = len(alpha_values)
        final_u_mean = np.zeros(N_alpha)
        final_v_mean = np.zeros(N_alpha)
        coexistence_indicator = np.zeros(N_alpha)
        
        for i, alpha in enumerate(alpha_values):
            print(f"Simulating with α={alpha:.3f} ({i+1}/{N_alpha})")
            
            # 使用较长的T=1000来确保竞争排除发生 (之前是100太短了)
            u_history, v_history = self.simulate_advection_competition(d, D, alpha, T=1000.0)
            
            # 计算最终平均密度
            u_final = u_history[-1]
            v_final = v_history[-1]
            
            final_u_mean[i] = np.mean(u_final)
            final_v_mean[i] = np.mean(v_final)
            
            # 判断共存：两个物种的最终密度都大于阈值
            threshold = 0.01
            coexistence_indicator[i] = 1 if (final_u_mean[i] > threshold and 
                                           final_v_mean[i] > threshold) else 0
        
        return alpha_values, final_u_mean, final_v_mean, coexistence_indicator
    
    def plot_alpha_dependence(self, d=1.0, D=1.0, show_plot=True):
        """绘制竞争结果对移流系数的依赖性"""
        alpha_values = np.logspace(-2, 2, 15)
        alpha_vals, u_mean, v_mean, coexistence = self.analyze_alpha_dependence(d, D, alpha_values)
        
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        
        # 1. 最终平均密度 vs α
        ax = axes[0, 0]
        ax.loglog(alpha_vals, u_mean, 'b-', linewidth=2, label='Species u (with advection)')
        ax.loglog(alpha_vals, v_mean, 'r-', linewidth=2, label='Species v (no advection)')
        ax.set_xlabel('Advection coefficient (α)', fontsize=12)
        ax.set_ylabel('Final mean density', fontsize=12)
        ax.set_title(f'Final Densities vs Advection Coefficient\n(d={d}, D={D})', fontsize=14)
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3, which='both')
        
        # 2. 密度比 u/v
        ax = axes[0, 1]
        ratio = np.zeros_like(u_mean)
        valid = v_mean > 1e-10
        ratio[valid] = u_mean[valid] / v_mean[valid]
        
        ax.loglog(alpha_vals[valid], ratio[valid], 'g-', linewidth=2)
        ax.axhline(y=1.0, color='k', linestyle='--', alpha=0.5)
        ax.set_xlabel('Advection coefficient (α)', fontsize=12)
        ax.set_ylabel('Final density ratio (u/v)', fontsize=12)
        ax.set_title('Competitive Advantage vs Advection', fontsize=14)
        ax.grid(True, alpha=0.3, which='both')
        
        # 3. 共存区域
        ax = axes[0, 2]
        # 寻找共存区域
        coexistence_start = None
        coexistence_regions = []
        
        for i in range(len(alpha_vals)):
            if coexistence[i] == 1:
                if coexistence_start is None:
                    coexistence_start = alpha_vals[i]
            else:
                if coexistence_start is not None:
                    coexistence_regions.append((coexistence_start, alpha_vals[i-1]))
                    coexistence_start = None
        
        if coexistence_start is not None:
            coexistence_regions.append((coexistence_start, alpha_vals[-1]))
        
        # 绘制共存区域
        for region in coexistence_regions:
            ax.axvspan(region[0], region[1], alpha=0.3, color='green', label='Coexistence')
        
        ax.loglog(alpha_vals, u_mean, 'b-', linewidth=2, label='Species u')
        ax.loglog(alpha_vals, v_mean, 'r-', linewidth=2, label='Species v')
        ax.set_xlabel('Advection coefficient (α)', fontsize=12)
        ax.set_ylabel('Final mean density', fontsize=12)
        ax.set_title('Coexistence Regions', fontsize=14)
        ax.grid(True, alpha=0.3, which='both')
        
        # 去重图例
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys(), fontsize=11)
        
        # 4-6. 不同α值的空间分布
        alpha_examples = [0.01, 1.0, 100.0]
        colors = ['blue', 'green', 'red']
        
        for i, alpha in enumerate(alpha_examples):
            ax = axes[1, i]
            
            u_history, v_history = self.simulate_advection_competition(d, D, alpha, T=100.0)
            u_final = u_history[-1]
            v_final = v_history[-1]
            
            ax.plot(self.x, u_final, color=colors[i], linestyle='-', 
                   linewidth=2, label=f'u (α={alpha})')
            ax.plot(self.x, v_final, color=colors[i], linestyle='--', 
                   linewidth=2, label=f'v (α={alpha})')
            ax.plot(self.x, self.m, 'k:', linewidth=1.5, label='m(x)', alpha=0.7)
            
            ax.set_xlabel('Position (x)', fontsize=12)
            ax.set_ylabel('Population density', fontsize=12)
            ax.set_title(f'α={alpha}', fontsize=14)
            ax.legend(fontsize=10)
            ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(f'advection_alpha_dependence_d{d}_D{D}.png', dpi=300, bbox_inches='tight')
        
        if show_plot:
            plt.show()
        else:
            plt.close(fig)
        
        # 分析定理：大α时的共存
        print("\n" + "="*60)
        print("ANALYSIS OF THEOREM")
        print("="*60)
        print("Theorem states that when α is sufficiently large,")
        print("both semi-trivial equilibria are unstable and there exists")
        print("at least one stable positive equilibrium (coexistence).")
        
        # 检查大α时是否共存
        large_alpha_idx = np.where(alpha_vals > 10)[0]
        if len(large_alpha_idx) > 0:
            coexists_at_large_alpha = any(coexistence[large_alpha_idx] == 1)
            print(f"\nCoexistence at large α (α > 10): {coexists_at_large_alpha}")
            
            if coexists_at_large_alpha:
                print("✓ Theorem is supported by simulation.")
            else:
                print("✗ Theorem is not supported by simulation.")
        
        return alpha_vals, u_mean, v_mean, coexistence

def explore_diffusion_advection_interaction():
    """探索扩散与移流的相互作用"""
    print("\n" + "="*60)
    print("EXPLORING DIFFUSION-ADVECTION INTERACTION")
    print("="*60)
    
    model = AdvectionCompetitionModel(L=10.0, Nx=101)
    
    # 不同扩散系数比的情况
    diffusion_ratios = [
        (0.5, 1.0, "D > d"),
        (1.0, 1.0, "D = d"),
        (1.0, 0.5, "D < d"),
    ]
    
    fig, axes = plt.subplots(3, 2, figsize=(14, 15))
    
    for idx, (d, D, label) in enumerate(diffusion_ratios):
        print(f"\nCase {idx+1}: {label} (d={d}, D={D})")
        
        # 分析α依赖性
        alpha_vals, u_mean, v_mean, coexistence = model.plot_alpha_dependence(d, D, show_plot=False)
        
        # 绘制竞争结果相图
        ax1 = axes[idx, 0]
        ax2 = axes[idx, 1]
        
        # 相图：u vs v
        ax1.loglog(alpha_vals, u_mean, 'b-', linewidth=2, label='Species u')
        ax1.loglog(alpha_vals, v_mean, 'r-', linewidth=2, label='Species v')
        ax1.set_xlabel('Advection coefficient (α)', fontsize=12)
        ax1.set_ylabel('Final mean density', fontsize=12)
        ax1.set_title(f'{label}\nFinal Densities vs α', fontsize=14)
        ax1.legend(fontsize=11)
        ax1.grid(True, alpha=0.3, which='both')
        
        # 竞争结果分类
        ax2.semilogx(alpha_vals, coexistence, 'g-', linewidth=2, drawstyle='steps-post')
        ax2.fill_between(alpha_vals, 0, coexistence, alpha=0.3, color='green')
        ax2.set_xlabel('Advection coefficient (α)', fontsize=12)
        ax2.set_ylabel('Coexistence (1) / Exclusion (0)', fontsize=12)
        ax2.set_title(f'{label}\nCoexistence Regions', fontsize=14)
        ax2.set_yticks([0, 1])
        ax2.set_yticklabels(['Exclusion', 'Coexistence'])
        ax2.grid(True, alpha=0.3, which='both')
        
        # 标记临界α值
        if len(alpha_vals) > 1:
            # 寻找从0到1的跳变点
            for i in range(1, len(coexistence)):
                if coexistence[i] != coexistence[i-1]:
                    alpha_crit = alpha_vals[i]
                    ax2.axvline(x=alpha_crit, color='k', linestyle='--', alpha=0.5)
                    ax2.text(alpha_crit, 0.5, f'α={alpha_crit:.2f}', 
                            fontsize=10, ha='center', va='center',
                            bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('diffusion_advection_interaction.png', dpi=300, bbox_inches='tight')
    plt.show()

explore_diffusion_advection_interaction()
```

**思考题**

1. **单种群引理数值验证**：取一维区域 $\Omega=[0,1]$，设资源函数 $m(x)=2+\sin(2\pi x)$，用有限差分法求解平衡态方程，计算总生物量 $\int_0^1\theta(x)\,\mathrm{d}x$ 随扩散系数 $d$ 的变化曲线，观察其非单调性。

2. **竞争模型的模拟**：在对称竞争 $b=c=1$ 下，分别取 $(d,D)=(0.5,1.0)$ 和 $(1.0,0.5)$，从随机初始条件出发，用显式或隐式格式求解，验证扩散较慢的物种获胜的结论。

3. **图灵斑图参数分析**：针对 Schnakenberg 模型，通过线性稳定性分析推导图灵不稳定的参数条件，并用数值模拟验证不同参数下斑图类型（点状、条纹状）的转变。

4. **移流系数的影响**：在模型(4.2)中固定 $d=D=1$，逐渐增大 $\alpha$，观察竞争结果从 $u$ 占优到共存的变化，验证定理4.1。

5. **环境异质性对入侵速度的影响**：考虑一维 Fisher-KPP 方程，但生长率 $r$ 为空间函数 $r(x)$，设计数值实验研究异质性如何改变最小波速。

6. **无量纲化练习**：将带有 Allee 效应的反应-扩散方程 $\partial_t u = D\partial_{xx}u + ru(u-a)(1-u/K)$ 无量纲化，并讨论无量纲参数的生态学含义。
