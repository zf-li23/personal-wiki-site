**内容**：PDE的直观引入（时间+空间）；扩散方程作为典型案例；有限差分法的基本思想。

## **引言：为什么需要偏微分方程？**

在前一节中，我们使用常微分方程（ODE）描述了系统状态随时间的变化。然而，ODE隐含了一个重要假设：系统是**均匀混合**的，空间异质性可以忽略。但在真实的生物系统中，**空间位置**往往至关重要：

- 形态发生中，细胞如何知道自己在胚胎中的位置并分化成特定类型？
- 神经信号如何沿轴突传播？
- 药物如何在组织中扩散分布？
- 生物膜中营养物质浓度如何随深度变化？

要描述这些同时依赖**时间和空间**的过程，我们需要偏微分方程（Partial Differential Equations, PDE）。PDE是包含多个自变量偏导数的方程，在生物建模中最常见的是时间 $t$ 和空间坐标 $(x, y, z)$。

本节将介绍PDE的基本概念、数值求解方法，以及三个在生物学中至关重要的PDE类型：扩散方程、反应-扩散方程和对流-扩散方程。

## **2.4.1 从ODE到PDE：空间维度的引入**

### **扩散过程：从Fick定律到扩散方程**

考虑一种物质在空间中的扩散。根据Fick第一定律，物质流 $J$ 与浓度梯度成正比：

$$
\mathbf{J} = -D \nabla c
$$

其中 $D$ 是扩散系数，$\nabla c$ 是浓度梯度。结合质量守恒（连续性方程）：

$$
\dfrac{\partial c}{\partial t} = -\nabla \cdot \mathbf{J}
$$

得到经典的扩散方程（Fick第二定律）：

$$
\dfrac{\partial c}{\partial t} = D \nabla^2 c
$$

在一维情况下：

$$
\dfrac{\partial c}{\partial t} = D \dfrac{\partial^2 c}{\partial x^2}
$$

这个简单的方程描述了从分子扩散到种群扩张的众多生物过程。

### **Python实现：一维扩散模拟**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from scipy.sparse.linalg import spsolve

def simulate_1d_diffusion():
    """模拟一维扩散过程"""
    
    # 空间和时间参数
    L = 1.0           # 区域长度 (m)
    D = 0.01          # 扩散系数 (m²/s)
    T = 10.0          # 总时间 (s)
    
    # 离散化参数
    Nx = 100          # 空间网格点数
    Nt = 1000         # 时间步数
    dx = L / (Nx - 1) # 空间步长
    dt = T / Nt       # 时间步长
    
    # 稳定性条件: D*dt/dx² ≤ 0.5
    stability = D * dt / dx**2
    print(f"稳定性参数 D*dt/dx² = {stability:.3f}")
    if stability > 0.5:
        print("警告: 数值稳定性可能不足，考虑减小dt")
    
    # 初始条件: 中心点脉冲
    x = np.linspace(0, L, Nx)
    c0 = np.zeros(Nx)
    c0[Nx//2] = 1.0  # 中心点初始浓度高
    
    # 边界条件: 两端浓度为零 (Dirichlet边界条件)
    c0[0] = 0.0
    c0[-1] = 0.0
    
    # 创建扩散矩阵（使用稀疏矩阵提高效率）
    alpha = D * dt / dx**2
    main_diag = (1 - 2*alpha) * np.ones(Nx)
    off_diag = alpha * np.ones(Nx-1)
    
    # 构建三对角矩阵
    A = sparse.diags([off_diag, main_diag, off_diag], 
                     [-1, 0, 1], format='csr')
    
    # 修正边界条件
    A[0, 0] = 1.0
    A[0, 1] = 0.0
    A[-1, -1] = 1.0
    A[-1, -2] = 0.0
    
    # 时间推进
    c = c0.copy()
    concentration_history = [c0.copy()]
    time_points = [0.0]
    
    for n in range(1, Nt+1):
        # 隐式欧拉法: A * c^{n+1} = c^n
        c = spsolve(A, c)
        
        # 记录特定时间点的浓度分布
        if n % (Nt//10) == 0:
            concentration_history.append(c.copy())
            time_points.append(n * dt)
    
    # 可视化
    plt.figure(figsize=(14, 5))
    
    # 子图1: 浓度分布随时间演化
    colors = plt.cm.viridis(np.linspace(0, 1, len(concentration_history)))
    
    plt.subplot(1, 2, 1)
    for i, (c_hist, t_val) in enumerate(zip(concentration_history, time_points)):
        plt.plot(x, c_hist, color=colors[i], linewidth=2, 
                label=f't={t_val:.1f}s' if i % 2 == 0 else None)
    
    plt.xlabel('位置 x (m)')
    plt.ylabel('浓度 c(x,t)')
    plt.title('一维扩散: 浓度分布随时间演化')
    plt.legend(loc='upper right', fontsize='small')
    plt.grid(True, alpha=0.3)
    
    # 子图2: 特定位置浓度随时间变化
    plt.subplot(1, 2, 2)
    
    # 重新模拟以记录特定点的历史
    c = c0.copy()
    positions = [Nx//4, Nx//2, 3*Nx//4]  # 左、中、右三点
    time_series = np.zeros((Nt+1, len(positions)))
    time_series[0, :] = c0[positions]
    
    for n in range(1, Nt+1):
        c = spsolve(A, c)
        time_series[n, :] = c[positions]
    
    t_vals = np.linspace(0, T, Nt+1)
    labels = ['x=L/4', 'x=L/2', 'x=3L/4']
    
    for i, pos in enumerate(positions):
        plt.plot(t_vals, time_series[:, i], linewidth=2, label=labels[i])
    
    plt.xlabel('时间 t (s)')
    plt.ylabel('浓度 c(x,t)')
    plt.title('特定位置浓度随时间变化')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # 验证质量守恒（考虑边界泄漏）
    initial_mass = np.trapz(c0, x)
    final_mass = np.trapz(c, x)
    mass_loss = (initial_mass - final_mass) / initial_mass * 100
    
    print(f"初始总质量: {initial_mass:.6f}")
    print(f"最终总质量: {final_mass:.6f}")
    print(f"质量损失率: {mass_loss:.2f}% (主要来自边界扩散)")
    
    return x, concentration_history, time_points

# 运行一维扩散模拟
x, conc_history, times = simulate_1d_diffusion()
```

## **2.4.2 反应-扩散方程：图灵斑图的数学基础**

### **图灵机制：对称性破缺与模式形成**

1952年，艾伦·图灵提出，两个或多个扩散速率不同的化学物质相互作用，可以从均匀状态自发产生空间模式。这一机制被称为**图灵不稳定性**，是许多生物模式形成（如动物皮毛图案、指纹、胚胎发育）的理论基础。

### **两组分反应-扩散系统**

最简单的图灵系统包含两个组分：激活剂 $u$ 和抑制剂 $v$：

$$
\begin{aligned}
\dfrac{\partial u}{\partial t} &= D_u \nabla^2 u + f(u, v) \\
\dfrac{\partial v}{\partial t} &= D_v \nabla^2 v + g(u, v)
\end{aligned}
$$

其中 $f(u,v)$ 和 $g(u,v)$ 描述局部反应动力学。图灵的关键发现是：当 $D_v \gg D_u$（抑制剂扩散更快）时，均匀稳态可能变得不稳定，从而产生空间模式。

### **Python实现：图灵斑图模拟**

```python
def simulate_turing_patterns():
    """模拟图灵斑图形成"""
    
    # 参数设置（经典Schnakenberg模型）
    params = {
        'a': 0.1,      # 基础激活剂产生率
        'b': 0.9,      # 基础抑制剂产生率
        'gamma': 1000, # 系统大小参数
        'Du': 0.05,    # 激活剂扩散系数
        'Dv': 1.0,     # 抑制剂扩散系数
    }
    
    # 空间网格
    N = 128  # 网格大小 N×N
    L = 1.0  # 区域大小
    dx = L / (N - 1)
    
    # 创建二维坐标网格
    x = np.linspace(0, L, N)
    y = np.linspace(0, L, N)
    X, Y = np.meshgrid(x, y)
    
    # 初始条件：均匀稳态 + 微小随机扰动
    u0 = params['a'] + params['b'] + 0.01 * np.random.randn(N, N)
    v0 = params['b'] / ((params['a'] + params['b'])**2) + 0.01 * np.random.randn(N, N)
    
    # 反应函数
    def reaction(u, v, a, b):
        """Schnakenberg动力学"""
        f = a - u + u**2 * v
        g = b - u**2 * v
        return f, g
    
    # 离散拉普拉斯算子（五点差分格式）
    def laplacian_2d(Z, dx):
        """计算二维拉普拉斯算子"""
        Z_center = Z[1:-1, 1:-1]
        Z_up = Z[:-2, 1:-1]
        Z_down = Z[2:, 1:-1]
        Z_left = Z[1:-1, :-2]
        Z_right = Z[1:-1, 2:]
        
        return (Z_up + Z_down + Z_left + Z_right - 4 * Z_center) / dx**2
    
    # 时间参数
    dt = 0.001  # 时间步长
    T = 5.0     # 总时间
    Nt = int(T / dt)
    
    # 记录中间结果用于可视化
    record_interval = Nt // 4
    u_history = []
    v_history = []
    time_points = []
    
    u = u0.copy()
    v = v0.copy()
    
    print("开始模拟图灵斑图形成...")
    for n in range(Nt + 1):
        # 计算反应项
        f, g = reaction(u, v, params['a'], params['b'])
        
        # 计算扩散项（内部点）
        lap_u = laplacian_2d(u, dx)
        lap_v = laplacian_2d(v, dx)
        
        # 时间推进（显式欧拉法）
        u_int = u[1:-1, 1:-1]
        v_int = v[1:-1, 1:-1]
        
        u_int_new = u_int + dt * (params['Du'] * lap_u + params['gamma'] * f[1:-1, 1:-1])
        v_int_new = v_int + dt * (params['Dv'] * lap_v + params['gamma'] * g[1:-1, 1:-1])
        
        # 更新内部点
        u[1:-1, 1:-1] = u_int_new
        v[1:-1, 1:-1] = v_int_new
        
        # 零流边界条件（Neumann边界条件）
        u[0, :] = u[1, :]    # 上边界
        u[-1, :] = u[-2, :]  # 下边界
        u[:, 0] = u[:, 1]    # 左边界
        u[:, -1] = u[:, -2]  # 右边界
        
        v[0, :] = v[1, :]
        v[-1, :] = v[-2, :]
        v[:, 0] = v[:, 1]
        v[:, -1] = v[:, -2]
        
        # 记录结果
        if n % record_interval == 0:
            u_history.append(u.copy())
            v_history.append(v.copy())
            time_points.append(n * dt)
    
    # 可视化
    fig = plt.figure(figsize=(15, 10))
    
    # 激活剂u的演化
    for i in range(len(u_history)):
        plt.subplot(2, 4, i+1)
        im = plt.imshow(u_history[i], cmap='RdYlBu_r', 
                       extent=[0, L, 0, L], origin='lower')
        plt.colorbar(im, fraction=0.046, pad=0.04)
        plt.title(f'激活剂 u, t={time_points[i]:.2f}')
        plt.xlabel('x')
        plt.ylabel('y')
    
    # 抑制剂v的演化
    for i in range(len(v_history)):
        plt.subplot(2, 4, i+5)
        im = plt.imshow(v_history[i], cmap='viridis', 
                       extent=[0, L, 0, L], origin='lower')
        plt.colorbar(im, fraction=0.046, pad=0.04)
        plt.title(f'抑制剂 v, t={time_points[i]:.2f}')
        plt.xlabel('x')
        plt.ylabel('y')
    
    plt.suptitle('图灵斑图形成: 激活剂与抑制剂的时空演化', fontsize=14)
    plt.tight_layout()
    plt.show()
    
    # 最终模式的统计分析
    u_final = u_history[-1]
    v_final = v_history[-1]
    
    print("\n最终模式统计:")
    print(f"激活剂 u: 均值={np.mean(u_final):.3f}, 标准差={np.std(u_final):.3f}")
    print(f"抑制剂 v: 均值={np.mean(v_final):.3f}, 标准差={np.std(v_final):.3f}")
    
    # 计算空间自相关
    from scipy.signal import correlate2d
    
    def spatial_autocorrelation(Z):
        """计算空间自相关函数"""
        Z_normalized = (Z - np.mean(Z)) / np.std(Z)
        corr = correlate2d(Z_normalized, Z_normalized, mode='same')
        corr = corr / np.max(corr)  # 归一化
        return corr
    
    corr_u = spatial_autocorrelation(u_final)
    corr_v = spatial_autocorrelation(v_final)
    
    # 绘制自相关函数
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    im1 = ax1.imshow(corr_u, cmap='RdBu_r', extent=[0, L, 0, L], origin='lower')
    plt.colorbar(im1, ax=ax1, fraction=0.046, pad=0.04)
    ax1.set_title('激活剂 u 的空间自相关')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    
    im2 = ax2.imshow(corr_v, cmap='RdBu_r', extent=[0, L, 0, L], origin='lower')
    plt.colorbar(im2, ax=ax2, fraction=0.046, pad=0.04)
    ax2.set_title('抑制剂 v 的空间自相关')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    
    plt.tight_layout()
    plt.show()
    
    return u_history, v_history, time_points, params

# 运行图灵斑图模拟
u_hist, v_hist, t_points, params = simulate_turing_patterns()
```

## **2.4.3 对流-扩散方程：流动介质中的传输**

### **生物系统中的对流与扩散**

在许多生物过程中，物质不仅通过扩散传输，还随着流体运动而**对流**。例如：
- 血液中的氧气输送（对流+扩散）
- 河流中的污染物传播
- 空气中的花粉传播
- 细胞内细胞质流动

对流-扩散方程结合了这两种传输机制：

$$
\dfrac{\partial c}{\partial t} = D \nabla^2 c - \mathbf{v} \cdot \nabla c + R(c)
$$

其中：
- $D \nabla^2 c$：扩散项
- $\mathbf{v} \cdot \nabla c$：对流项（$\mathbf{v}$ 是流速场）
- $R(c)$：反应项

### **Python实现：一维对流-扩散模拟**

```python
def simulate_advection_diffusion():
    """模拟一维对流-扩散过程"""
    
    # 参数
    L = 1.0           # 区域长度
    D = 0.01          # 扩散系数
    v = 0.1           # 流速（常数）
    T = 5.0           # 总时间
    
    # 离散化
    Nx = 200          # 空间网格数
    Nt = 1000         # 时间步数
    dx = L / (Nx - 1)
    dt = T / Nt
    
    # 稳定性检查
    peclet = v * dx / D          # Peclet数（对流/扩散比）
    courant = v * dt / dx        # Courant数
    
    print(f"Peclet数 (对流/扩散): {peclet:.3f}")
    print(f"Courant数: {courant:.3f}")
    print(f"稳定性条件: Courant数 < 1, Peclet数 < 2")
    
    # 初始条件：高斯脉冲
    x = np.linspace(0, L, Nx)
    x0 = L/4  # 初始脉冲位置
    sigma = 0.05  # 脉冲宽度
    
    c0 = np.exp(-(x - x0)**2 / (2 * sigma**2))
    
    # 边界条件：入口保持为零，出口为零梯度
    c = c0.copy()
    
    # 记录历史
    history = [c0.copy()]
    history_times = [0.0]
    
    # 主循环（迎风差分格式处理对流项）
    for n in range(1, Nt + 1):
        c_new = np.zeros_like(c)
        
        # 内部点使用迎风格式
        for i in range(1, Nx-1):
            # 对流项：迎风格式（取决于流速方向）
            if v >= 0:
                # 流速向右，使用向后差分
                adv = v * (c[i] - c[i-1]) / dx
            else:
                # 流速向左，使用向前差分
                adv = v * (c[i+1] - c[i]) / dx
            
            # 扩散项：中心差分
            diff = D * (c[i+1] - 2*c[i] + c[i-1]) / dx**2
            
            # 更新
            c_new[i] = c[i] + dt * (diff - adv)
        
        # 边界条件
        c_new[0] = 0.0  # 入口Dirichlet条件
        c_new[-1] = c_new[-2]  # 出口Neumann条件（零梯度）
        
        c = c_new.copy()
        
        # 记录
        if n % (Nt // 10) == 0:
            history.append(c.copy())
            history_times.append(n * dt)
    
    # 可视化
    plt.figure(figsize=(14, 5))
    
    # 子图1：浓度分布演化
    plt.subplot(1, 2, 1)
    colors = plt.cm.plasma(np.linspace(0, 1, len(history)))
    
    for i, (c_hist, t_val) in enumerate(zip(history, history_times)):
        plt.plot(x, c_hist, color=colors[i], linewidth=2, 
                alpha=0.8, label=f't={t_val:.1f}s')
    
    plt.xlabel('位置 x')
    plt.ylabel('浓度 c(x,t)')
    plt.title('对流-扩散：浓度分布演化')
    plt.legend(loc='upper right', fontsize='small')
    plt.grid(True, alpha=0.3)
    
    # 子图2：与纯扩散比较
    plt.subplot(1, 2, 2)
    
    # 重新计算纯扩散情况
    alpha = D * dt / dx**2
    main_diag = (1 - 2*alpha) * np.ones(Nx)
    off_diag = alpha * np.ones(Nx-1)
    
    A = sparse.diags([off_diag, main_diag, off_diag], 
                     [-1, 0, 1], format='csr')
    A[0, 0] = 1.0; A[0, 1] = 0.0
    A[-1, -1] = 1.0; A[-1, -2] = 0.0
    
    c_diff = c0.copy()
    for n in range(Nt):
        c_diff = spsolve(A, c_diff)
    
    plt.plot(x, c0, 'k--', linewidth=2, label='初始分布')
    plt.plot(x, c, 'b-', linewidth=2, label=f'对流-扩散 (v={v})')
    plt.plot(x, c_diff, 'r-', linewidth=2, alpha=0.7, label='纯扩散 (v=0)')
    
    plt.xlabel('位置 x')
    plt.ylabel('浓度 c(x,t)')
    plt.title(f'最终分布对比 (t={T}s)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # 计算质心位置（一阶矩）
    def centroid(Z, x_grid):
        """计算分布的质心位置"""
        return np.sum(Z * x_grid) / np.sum(Z)
    
    x_centroid_initial = centroid(c0, x)
    x_centroid_final = centroid(c, x)
    x_centroid_diff = centroid(c_diff, x)
    
    print(f"\n质心位置分析:")
    print(f"  初始质心: {x_centroid_initial:.3f}")
    print(f"  纯扩散后质心: {x_centroid_diff:.3f} (移动: {x_centroid_diff - x_centroid_initial:.3f})")
    print(f"  对流-扩散后质心: {x_centroid_final:.3f} (移动: {x_centroid_final - x_centroid_initial:.3f})")
    print(f"  理论对流位移: v*t = {v * T:.3f}")
    
    return x, history, history_times

# 运行对流-扩散模拟
x_ad, hist_ad, times_ad = simulate_advection_diffusion()
```

## **2.4.4 数值方法：有限差分法、有限元法与谱方法**

### **有限差分法（Finite Difference Method, FDM）**

我们前面的例子都使用了有限差分法，其核心思想是用差分近似导数。对于二阶导数：

$$
\dfrac{\partial^2 u}{\partial x^2} \approx \dfrac{u_{i+1} - 2u_i + u_{i-1}}{\Delta x^2}
$$

**优点**：简单直观，易于实现
**缺点**：对复杂几何形状处理困难

### **有限体积法（Finite Volume Method, FVM）**

FVM基于积分形式的守恒定律，在计算流体力学中广泛应用：

$$
\int_V \dfrac{\partial u}{\partial t} dV = -\oint_S \mathbf{F} \cdot d\mathbf{S} + \int_V Q dV
$$

### **有限元法（Finite Element Method, FEM）**

FEM将计算区域划分为小单元（三角形、四边形等），在每个单元上用简单函数近似解。

```python
def compare_numerical_methods():
    """比较不同数值方法求解PDE"""
    
    # 问题：求解稳态热传导方程
    # ∇²T = 0, 边界条件：左边界T=100，右边界T=0，上下绝热
    
    # 网格参数
    Nx, Ny = 50, 50
    Lx, Ly = 1.0, 1.0
    dx, dy = Lx/(Nx-1), Ly/(Ny-1)
    
    # 精确解（一维情况）：T(x) = 100*(1-x)
    x = np.linspace(0, Lx, Nx)
    y = np.linspace(0, Ly, Ny)
    X, Y = np.meshgrid(x, y)
    
    T_exact = 100 * (1 - X)  # 忽略y方向变化
    
    # 方法1：有限差分法（直接求解）
    print("方法1：有限差分法（直接求解）...")
    
    # 构建系数矩阵
    N = Nx * Ny
    A = sparse.lil_matrix((N, N))
    b = np.zeros(N)
    
    # 内部点：五点差分格式
    for i in range(1, Ny-1):
        for j in range(1, Nx-1):
            idx = i*Nx + j
            A[idx, idx] = -2/dx**2 - 2/dy**2
            A[idx, idx-1] = 1/dx**2  # 左
            A[idx, idx+1] = 1/dx**2  # 右
            A[idx, idx-Nx] = 1/dy**2 # 下
            A[idx, idx+Nx] = 1/dy**2 # 上
    
    # 边界条件
    # 左边界：T=100
    for i in range(Ny):
        idx = i*Nx
        A[idx, idx] = 1.0
        b[idx] = 100.0
    
    # 右边界：T=0
    for i in range(Ny):
        idx = i*Nx + (Nx-1)
        A[idx, idx] = 1.0
        b[idx] = 0.0
    
    # 上下边界：绝热（零梯度，使用虚拟点法）
    for j in range(1, Nx-1):
        # 下边界
        idx = j
        A[idx, idx] = -3/dy**2 - 2/dx**2
        A[idx, idx-1] = 1/dx**2
        A[idx, idx+1] = 1/dx**2
        A[idx, idx+Nx] = 2/dy**2  # 虚拟点法
        
        # 上边界
        idx = (Ny-1)*Nx + j
        A[idx, idx] = -3/dy**2 - 2/dx**2
        A[idx, idx-1] = 1/dx**2
        A[idx, idx+1] = 1/dx**2
        A[idx, idx-Nx] = 2/dy**2  # 虚拟点法
    
    # 求解线性系统
    A_csr = A.tocsr()
    T_flat = spsolve(A_csr, b)
    T_fd = T_flat.reshape(Ny, Nx)
    
    # 方法2：有限差分法（迭代求解 - Gauss-Seidel）
    print("方法2：有限差分法（Gauss-Seidel迭代）...")
    
    T_gs = np.zeros((Ny, Nx))
    
    # 设置边界条件
    T_gs[:, 0] = 100.0   # 左边界
    T_gs[:, -1] = 0.0    # 右边界
    
    # Gauss-Seidel迭代
    max_iter = 10000
    tolerance = 1e-6
    
    for iteration in range(max_iter):
        T_old = T_gs.copy()
        
        # 更新内部点
        for i in range(1, Ny-1):
            for j in range(1, Nx-1):
                T_gs[i, j] = 0.25 * (T_gs[i-1, j] + T_old[i+1, j] + 
                                    T_gs[i, j-1] + T_old[i, j+1])
        
        # 更新边界条件（绝热边界）
        T_gs[0, 1:-1] = T_gs[1, 1:-1]   # 下边界
        T_gs[-1, 1:-1] = T_gs[-2, 1:-1] # 上边界
        
        # 检查收敛
        residual = np.max(np.abs(T_gs - T_old))
        if residual < tolerance:
            print(f"  Gauss-Seidel在{iteration+1}次迭代后收敛")
            break
    
    # 计算误差
    error_fd = np.max(np.abs(T_fd - T_exact))
    error_gs = np.max(np.abs(T_gs - T_exact))
    
    print(f"\n最大绝对误差比较:")
    print(f"  直接求解FDM: {error_fd:.6f}")
    print(f"  Gauss-Seidel: {error_gs:.6f}")
    
    # 可视化
    fig = plt.figure(figsize=(15, 10))
    
    # 精确解
    plt.subplot(2, 3, 1)
    contour = plt.contourf(X, Y, T_exact, 20, cmap='hot')
    plt.colorbar(contour)
    plt.title('精确解 T(x) = 100(1-x)')
    plt.xlabel('x')
    plt.ylabel('y')
    
    # 有限差分法（直接求解）
    plt.subplot(2, 3, 2)
    contour = plt.contourf(X, Y, T_fd, 20, cmap='hot')
    plt.colorbar(contour)
    plt.title('有限差分法（直接求解）')
    plt.xlabel('x')
    plt.ylabel('y')
    
    # 有限差分法（迭代求解）
    plt.subplot(2, 3, 3)
    contour = plt.contourf(X, Y, T_gs, 20, cmap='hot')
    plt.colorbar(contour)
    plt.title('有限差分法（Gauss-Seidel迭代）')
    plt.xlabel('x')
    plt.ylabel('y')
    
    # 误差分布
    plt.subplot(2, 3, 4)
    error_contour = plt.contourf(X, Y, np.abs(T_fd - T_exact), 20, cmap='Reds')
    plt.colorbar(error_contour)
    plt.title('直接求解FDM的误差分布')
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.subplot(2, 3, 5)
    error_contour = plt.contourf(X, Y, np.abs(T_gs - T_exact), 20, cmap='Reds')
    plt.colorbar(error_contour)
    plt.title('Gauss-Seidel的误差分布')
    plt.xlabel('x')
    plt.ylabel('y')
    
    # x方向中心线的温度分布
    plt.subplot(2, 3, 6)
    center_y = Ny // 2
    plt.plot(x, T_exact[center_y, :], 'k-', linewidth=3, label='精确解')
    plt.plot(x, T_fd[center_y, :], 'b--', linewidth=2, label='直接求解FDM')
    plt.plot(x, T_gs[center_y, :], 'r-.', linewidth=2, label='Gauss-Seidel')
    plt.xlabel('x')
    plt.ylabel('温度 T')
    plt.title('y=0.5中心线的温度分布')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.suptitle('PDE数值方法比较：稳态热传导方程', fontsize=14)
    plt.tight_layout()
    plt.show()
    
    return T_exact, T_fd, T_gs

# 运行数值方法比较
T_exact, T_fd, T_gs = compare_numerical_methods()
```

## **2.4.5 生物学应用案例**

### **案例1：药物在组织中的扩散与吸收**

考虑药物在组织中扩散的同时被代谢吸收：

$$
\dfrac{\partial c}{\partial t} = D \dfrac{\partial^2 c}{\partial x^2} - kc
$$

其中 $-kc$ 表示一级代谢消除。

```python
def drug_diffusion_absorption():
    """药物在组织中的扩散与吸收"""
    
    # 参数
    L = 0.01          # 组织厚度 1cm = 0.01m
    D = 1e-9          # 扩散系数 m²/s（典型组织值）
    k = 0.1           # 代谢速率常数 1/s
    T = 3600          # 模拟时间 1小时 = 3600秒
    
    # 初始条件：表面给药（左边界）
    Nx = 100
    Nt = 1000
    dx = L / (Nx - 1)
    dt = T / Nt
    
    x = np.linspace(0, L, Nx)
    
    # 初始浓度为零
    c = np.zeros(Nx)
    
    # 边界条件
    c[0] = 1.0        # 左边界：恒定浓度（给药表面）
    c[-1] = 0.0       # 右边界：零浓度（深层组织）
    
    # 系数矩阵（隐式欧拉法）
    alpha = D * dt / dx**2
    beta = k * dt
    
    main_diag = (1 + 2*alpha + beta) * np.ones(Nx)
    off_diag = -alpha * np.ones(Nx-1)
    
    A = sparse.diags([off_diag, main_diag, off_diag], 
                     [-1, 0, 1], format='csr')
    
    # 边界条件修正
    A[0, 0] = 1.0
    A[0, 1] = 0.0
    A[-1, -1] = 1.0
    A[-1, -2] = 0.0
    
    # 时间推进
    history = []
    times = []
    
    for n in range(Nt + 1):
        # 右端项
        b = c.copy()
        b[0] = 1.0  # 左边界固定
        b[-1] = 0.0 # 右边界固定
        
        # 求解
        c = spsolve(A, b)
        
        # 记录
        if n % (Nt // 10) == 0:
            history.append(c.copy())
            times.append(n * dt)
    
    # 可视化
    plt.figure(figsize=(12, 10))
    
    # 子图1：浓度分布演化
    plt.subplot(2, 2, 1)
    colors = plt.cm.Blues(np.linspace(0.3, 1, len(history)))
    
    for i, (c_hist, t_val) in enumerate(zip(history, times)):
        plt.plot(x*100, c_hist, color=colors[i], linewidth=2, 
                label=f't={t_val/60:.0f}min')
    
    plt.xlabel('组织深度 (cm)')
    plt.ylabel('药物浓度 (归一化)')
    plt.title('药物在组织中的渗透')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 子图2：无吸收情况的对比
    plt.subplot(2, 2, 2)
    
    # 重新计算无吸收情况
    c_no_abs = np.zeros(Nx)
    c_no_abs[0] = 1.0
    c_no_abs[-1] = 0.0
    
    main_diag_no = (1 + 2*alpha) * np.ones(Nx)
    A_no = sparse.diags([off_diag, main_diag_no, off_diag], 
                        [-1, 0, 1], format='csr')
    A_no[0, 0] = 1.0; A_no[0, 1] = 0.0
    A_no[-1, -1] = 1.0; A_no[-1, -2] = 0.0
    
    history_no = []
    for n in range(Nt + 1):
        b_no = c_no_abs.copy()
        b_no[0] = 1.0
        b_no[-1] = 0.0
        c_no_abs = spsolve(A_no, b_no)
        
        if n % (Nt // 10) == 0:
            history_no.append(c_no_abs.copy())
    
    # 绘制最终分布对比
    plt.plot(x*100, history[-1], 'b-', linewidth=3, label=f'有吸收 (k={k} s⁻¹)')
    plt.plot(x*100, history_no[-1], 'r--', linewidth=3, label='无吸收 (k=0)')
    plt.xlabel('组织深度 (cm)')
    plt.ylabel('药物浓度 (归一化)')
    plt.title(f'最终分布对比 (t={T/60:.0f}min)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 子图3：渗透深度随时间变化
    plt.subplot(2, 2, 3)
    
    penetration_depths = []
    penetration_depths_no = []
    
    for c_hist, c_hist_no in zip(history, history_no):
        # 定义渗透深度为浓度降至表面浓度10%的位置
        threshold = 0.1
        idx = np.where(c_hist < threshold)[0]
        if len(idx) > 0:
            depth = x[idx[0]] * 100  # 转换为cm
            penetration_depths.append(depth)
        else:
            penetration_depths.append(L*100)
        
        idx_no = np.where(c_hist_no < threshold)[0]
        if len(idx_no) > 0:
            depth_no = x[idx_no[0]] * 100
            penetration_depths_no.append(depth_no)
        else:
            penetration_depths_no.append(L*100)
    
    times_min = [t/60 for t in times]
    plt.plot(times_min, penetration_depths, 'bo-', linewidth=2, label='有吸收')
    plt.plot(times_min, penetration_depths_no, 'rs--', linewidth=2, label='无吸收')
    plt.xlabel('时间 (分钟)')
    plt.ylabel('渗透深度 (cm)')
    plt.title('渗透深度随时间变化 (阈值=0.1)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 子图4：总药量随时间变化
    plt.subplot(2, 2, 4)
    
    total_drug = [np.trapz(c_hist, x) for c_hist in history]
    total_drug_no = [np.trapz(c_hist_no, x) for c_hist_no in history_no]
    
    plt.plot(times_min, total_drug, 'bo-', linewidth=2, label='有吸收')
    plt.plot(times_min, total_drug_no, 'rs--', linewidth=2, label='无吸收')
    plt.xlabel('时间 (分钟)')
    plt.ylabel('组织中药量 (归一化)')
    plt.title('总药量随时间变化')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # 药代动力学参数计算
    print("药代动力学参数分析:")
    print(f"扩散系数 D = {D:.2e} m²/s")
    print(f"代谢速率常数 k = {k:.3f} 1/s")
    print(f"特征扩散时间 τ_diff = L²/D = {(L**2/D):.0f} s = {(L**2/D/60):.1f} min")
    print(f"特征代谢时间 τ_met = 1/k = {1/k:.1f} s = {1/k/60:.1f} min")
    print(f"Damköhler数 Da = τ_diff/τ_met = {(L**2/D)/(1/k):.3f}")
    
    return x, history, times

# 运行药物扩散模拟
x_drug, hist_drug, times_drug = drug_diffusion_absorption()
```

### **案例2：种群空间扩张模型**

考虑种群在空间中的扩散与增长（Fisher-KPP方程）：

$$
\dfrac{\partial n}{\partial t} = D \dfrac{\partial^2 n}{\partial x^2} + r n \left(1 - \dfrac{n}{K}\right)
$$

这个方程结合了扩散（$D \nabla^2 n$）和逻辑斯蒂增长（$r n (1-n/K)$）。

```python
def fisher_kpp_equation():
    """Fisher-KPP方程：种群空间扩张"""
    
    # 参数
    L = 50.0          # 空间范围
    D = 0.1           # 扩散系数
    r = 0.5           # 增长率
    K = 1.0           # 环境承载力
    
    # 初始条件：局部引入种群
    Nx = 200
    Nt = 1000
    T = 20.0
    dx = L / (Nx - 1)
    dt = T / Nt
    
    x = np.linspace(-L/2, L/2, Nx)
    
    # 初始条件：中心区域有少量种群
    n0 = np.zeros(Nx)
    center_idx = Nx // 2
    width = 10
    n0[center_idx-width:center_idx+width] = 0.01 * K
    
    # 边界条件：零梯度（Neumann边界）
    n = n0.copy()
    
    # 记录历史
    history = [n0.copy()]
    history_times = [0.0]
    
    # 时间推进（显式方法）
    for step in range(1, Nt + 1):
        n_new = np.zeros_like(n)
        
        # 内部点
        for i in range(1, Nx-1):
            # 扩散项（中心差分）
            diffusion = D * (n[i+1] - 2*n[i] + n[i-1]) / dx**2
            
            # 增长项（逻辑斯蒂）
            growth = r * n[i] * (1 - n[i]/K)
            
            # 更新
            n_new[i] = n[i] + dt * (diffusion + growth)
        
        # 边界条件（零梯度）
        n_new[0] = n_new[1]
        n_new[-1] = n_new[-2]
        
        n = n_new.copy()
        
        # 记录
        if step % (Nt // 10) == 0:
            history.append(n.copy())
            history_times.append(step * dt)
    
    # 计算扩张波速（理论值：v = 2√(Dr)）
    v_theory = 2 * np.sqrt(D * r)
    
    # 从模拟中估计波速
    def estimate_wave_speed(history, x, threshold=0.5*K):
        """估计波前传播速度"""
        speeds = []
        
        for i in range(1, len(history)):
            # 找到阈值位置
            positions = []
            for pos_idx in [np.where(hist > threshold)[0] for hist in [history[i-1], history[i]]]:
                if len(pos_idx) > 0:
                    positions.append(x[pos_idx[0]])
                else:
                    positions.append(x[-1])
            
            if len(positions) == 2:
                dx_wave = positions[1] - positions[0]
                dt_wave = history_times[i] - history_times[i-1]
                if dt_wave > 0:
                    speeds.append(dx_wave / dt_wave)
        
        return np.mean(speeds) if speeds else 0.0
    
    v_estimated = estimate_wave_speed(history, x)
    
    # 可视化
    plt.figure(figsize=(14, 10))
    
    # 子图1：种群分布演化
    plt.subplot(2, 2, 1)
    colors = plt.cm.viridis(np.linspace(0, 1, len(history)))
    
    for i, (n_hist, t_val) in enumerate(zip(history, history_times)):
        plt.plot(x, n_hist/K, color=colors[i], linewidth=2, 
                label=f't={t_val:.1f}' if i % 2 == 0 else None)
    
    plt.xlabel('位置 x')
    plt.ylabel('相对种群密度 n/K')
    plt.title('Fisher-KPP方程：种群空间扩张')
    plt.legend(loc='upper left', fontsize='small')
    plt.grid(True, alpha=0.3)
    
    # 子图2：波前位置随时间变化
    plt.subplot(2, 2, 2)
    
    front_positions = []
    for n_hist in history:
        # 找到种群密度为0.5K的位置作为波前
        idx = np.where(n_hist > 0.5*K)[0]
        if len(idx) > 0:
            front_positions.append(x[idx[0]])
        else:
            front_positions.append(0.0)
    
    plt.plot(history_times, front_positions, 'bo-', linewidth=2)
    
    # 理论预测（从中心向两侧扩张）
    t_vals = np.array(history_times)
    x_theory = v_theory * t_vals
    plt.plot(t_vals, x_theory, 'r--', linewidth=2, 
            label=f'理论预测 v={v_theory:.3f}')
    
    # 线性拟合估计速度
    if len(front_positions) > 1:
        coeffs = np.polyfit(history_times, front_positions, 1)
        x_fit = np.polyval(coeffs, t_vals)
        plt.plot(t_vals, x_fit, 'g:', linewidth=2, 
                label=f'拟合速度 v={coeffs[0]:.3f}')
    
    plt.xlabel('时间 t')
    plt.ylabel('波前位置 x_front')
    plt.title('波前传播')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 子图3：时空密度图
    plt.subplot(2, 2, 3)
    
    # 创建时空矩阵
    space_time = np.zeros((len(history), Nx))
    for i, n_hist in enumerate(history):
        space_time[i, :] = n_hist/K
    
    plt.imshow(space_time, aspect='auto', extent=[x[0], x[-1], history_times[-1], 0],
              cmap='viridis', interpolation='bilinear')
    plt.colorbar(label='相对密度 n/K')
    plt.xlabel('位置 x')
    plt.ylabel('时间 t')
    plt.title('种群密度时空演化')
    
    # 子图4：不同参数的比较
    plt.subplot(2, 2, 4)
    
    # 测试不同扩散系数的影响
    D_values = [0.05, 0.1, 0.2]
    colors_d = ['b', 'g', 'r']
    
    for D_val, color in zip(D_values, colors_d):
        # 快速模拟
        n_test = n0.copy()
        n_final = np.zeros_like(n_test)
        
        # 少量时间步获取最终分布
        for step in range(200):
            n_new = np.zeros_like(n_test)
            for i in range(1, Nx-1):
                diffusion = D_val * (n_test[i+1] - 2*n_test[i] + n_test[i-1]) / dx**2
                growth = r * n_test[i] * (1 - n_test[i]/K)
                n_new[i] = n_test[i] + 0.1 * (diffusion + growth)
            
            n_new[0] = n_new[1]
            n_new[-1] = n_new[-2]
            n_test = n_new.copy()
        
        plt.plot(x, n_test/K, color=color, linewidth=2, 
                label=f'D={D_val}, v={2*np.sqrt(D_val*r):.3f}')
    
    plt.xlabel('位置 x')
    plt.ylabel('相对密度 n/K')
    plt.title('不同扩散系数的影响 (t=20)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    print(f"Fisher-KPP方程分析:")
    print(f"  理论波速: v = 2√(Dr) = 2√({D}×{r}) = {v_theory:.3f}")
    print(f"  估计波速: v_est = {v_estimated:.3f}")
    print(f"  相对误差: {abs(v_estimated - v_theory)/v_theory*100:.1f}%")
    
    return x, history, history_times, v_theory, v_estimated

# 运行Fisher-KPP方程模拟
x_fisher, hist_fisher, times_fisher, v_theory, v_est = fisher_kpp_equation()
```

## **2.4.6 高级主题与计算工具**

### **三维PDE与并行计算**

生物系统中的许多问题本质上是三维的，如器官发育、肿瘤生长、流体动力学等。三维PDE需要大量计算资源，通常需要并行计算。

```python
def intro_3d_pde():
    """三维扩散问题简介"""
    
    print("三维PDE计算简介")
    print("="*50)
    
    # 问题规模估计
    N = 100  # 每个方向的网格点数
    total_points = N**3
    print(f"网格大小: {N}×{N}×{N} = {total_points:,} 个点")
    
    # 内存需求估计（双精度浮点数）
    memory_mb = total_points * 8 / (1024**2)
    print(f"内存需求: ~{memory_mb:.1f} MB（单个场变量）")
    
    # 时间步数估计
    Nt = 1000
    print(f"时间步数: {Nt}")
    
    # 总计算量估计（每次迭代更新每个点）
    total_operations = total_points * Nt * 10  # 约10次操作/点/步
    print(f"总计算量: ~{total_operations:.2e} 次浮点运算")
    
    # 串行计算时间估计（假设10 GFLOP/s）
    serial_time = total_operations / 10e9
    print(f"串行计算时间估计: {serial_time:.1f} 秒")
    
    # 并行加速潜力
    print("\n并行计算潜力:")
    for p in [4, 16, 64]:
        parallel_time = serial_time / p
        print(f"  {p}个进程: ~{parallel_time:.1f} 秒")
    
    print("\n常用三维PDE求解工具:")
    print("  1. FEniCS: 基于有限元法的开源框架")
    print("  2. OpenFOAM: 计算流体动力学开源软件")
    print("  3. COMSOL: 多物理场商业软件")
    print("  4. 自定义CUDA/OpenMP代码")
    
    # 简化的3D扩散演示（小规模）
    print("\n简化3D扩散演示（小规模）...")
    
    N_small = 20
    L = 1.0
    dx = L / (N_small - 1)
    
    # 创建3D网格
    x = np.linspace(0, L, N_small)
    y = np.linspace(0, L, N_small)
    z = np.linspace(0, L, N_small)
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
    
    # 初始条件：中心点源
    c0 = np.zeros((N_small, N_small, N_small))
    center = N_small // 2
    c0[center, center, center] = 1.0
    
    # 几个时间步的扩散
    D = 0.01
    dt = 0.01
    alpha = D * dt / dx**2
    
    c = c0.copy()
    
    # 有限差分更新（6点模板）
    def update_3d_diffusion(c, alpha):
        c_new = c.copy()
        
        # 内部点
        for i in range(1, N_small-1):
            for j in range(1, N_small-1):
                for k in range(1, N_small-1):
                    laplacian = (c[i+1, j, k] + c[i-1, j, k] +
                                c[i, j+1, k] + c[i, j-1, k] +
                                c[i, j, k+1] + c[i, j, k-1] - 
                                6 * c[i, j, k])
                    c_new[i, j, k] = c[i, j, k] + alpha * laplacian
        
        return c_new
    
    # 运行几步
    for step in range(5):
        c = update_3d_diffusion(c, alpha)
    
    print(f"  初始中心浓度: {c0[center, center, center]:.3f}")
    print(f"  5步后中心浓度: {c[center, center, center]:.3f}")
    
    # 可视化一个切片
    plt.figure(figsize=(10, 4))
    
    plt.subplot(1, 2, 1)
    plt.imshow(c0[:, :, center], cmap='hot', extent=[0, L, 0, L])
    plt.colorbar()
    plt.title('初始条件 (z=中心平面)')
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.subplot(1, 2, 2)
    plt.imshow(c[:, :, center], cmap='hot', extent=[0, L, 0, L])
    plt.colorbar()
    plt.title('5步扩散后 (z=中心平面)')
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.tight_layout()
    plt.show()
    
    return c

# 运行3D PDE简介
c_3d = intro_3d_pde()
```

### **PDE求解器的选择指南**

| 问题类型 | 推荐方法 | 工具/库 | 适用场景 |
|---------|---------|--------|---------|
| 规则几何，简单方程 | 有限差分法 | NumPy, SciPy | 教学、快速原型 |
| 复杂几何，多物理场 | 有限元法 | FEniCS, COMSOL | 组织力学、器官建模 |
| 流体动力学 | 有限体积法 | OpenFOAM, ANSYS Fluent | 血流、呼吸、微流体 |
| 高精度需求 | 谱方法 | Dedalus, Chebfun | 波动、稳定性分析 |
| 大规模并行 | 自定义并行 | MPI, CUDA, OpenMP | 全脑模拟、生态系统 |

## **总结与展望**

本节系统介绍了偏微分方程在生物建模中的核心地位和应用方法：

### **核心要点回顾**
1. **从ODE到PDE的范式转变**：从均匀系统到空间异质系统，从常微分到偏微分
2. **三大基本方程类型**：
   - 扩散方程：描述随机运动导致的物质分布
   - 反应-扩散方程：解释模式形成和自组织
   - 对流-扩散方程：处理流动介质中的传输
3. **数值方法是实践基础**：有限差分法简单实用，有限元法灵活强大
4. **生物应用广泛而深刻**：从分子扩散到种群扩张，从药物输送到形态发生

### **关键数学洞察**
1. **扩散导致平滑化**：高浓度区域向低浓度区域流动，最终趋于均匀
2. **扩散系数差异产生模式**：图灵机制的核心是激活剂与抑制剂扩散速率不同
3. **对流主导快速传输**：当 Peclet 数 >> 1 时，对流效应压倒扩散
4. **非线性反应产生丰富动态**：逻辑斯蒂增长与扩散结合产生扩张波前

### **计算实践建议**
1. **稳定性是第一要务**：确保时间步长满足 CFL 条件
2. **边界条件决定解的性质**：Dirichlet（固定值）vs Neumann（零梯度）vs Robin（混合）
3. **稀疏矩阵提高效率**：PDE离散化产生稀疏矩阵，使用稀疏求解器
4. **可视化是理解的关键**：时空演化、相图、等高线图等多角度可视化

### **与iGEM项目的关联**

回顾历年iGEM优秀项目的建模部分，PDE应用广泛而深入：
- **2025 Peking**：微球胃内扩散（三维扩散）+ 穿透胃黏膜层（多物理场）
- **2024 BNUZH-CHINA**：微生物冲刷扰动模型（流体动力学）
- **2023 ZJU-China**：植物病毒湍流扩散（计算流体力学）

掌握PDE建模能力，将使你的iGEM项目能够：
1. 预测合成生物系统在空间中的行为
2. 优化生物反应器中的物质混合
3. 设计空间模式化的生物材料
4. 模拟生物膜、组织工程等复杂系统

### **展望下一章**

在第3章"分子生物物理模拟"中，我们将从宏观尺度深入到分子尺度，探索蛋白质结构、分子对接和分子动力学。有趣的是，分子动力学的基本方程（牛顿第二定律）是ODE，但模拟大量分子时需要考虑它们的空间分布，这自然联系到统计力学和PDE中的输运方程。

PDE不是建模的终点，而是连接不同尺度、整合不同过程的桥梁。从分子相互作用到细胞行为，从组织功能到器官系统，PDE提供了描述跨尺度生物过程的统一数学框架。

## **思考题**

1. 修改图灵斑图模拟的参数（扩散系数比、反应动力学参数），观察点状、条状、迷宫状等不同模式的形成条件。
2. 实现一个二维对流-扩散方程，模拟河流中的污染物扩散。考虑非均匀流速场的影响。
3. 扩展Fisher-KPP方程，考虑异质环境（如K随空间变化）。这对种群扩张有何影响？
4. 尝试使用FEniCS或COMSOL解决一个简单的生物传热问题（如组织中的热疗模拟）。
5. 设计一个简单的肿瘤生长模型，结合细胞增殖（反应项）、浸润（扩散项）和营养限制（非线性项）。

通过本章学习，你已掌握了用PDE描述空间生物过程的基本能力。在后续章节中，我们将看到这些方法如何与其他建模技术结合，解决更复杂的生物学问题。

---

*下一章，我们将深入分子世界，探索生物大分子的结构与动力学。*