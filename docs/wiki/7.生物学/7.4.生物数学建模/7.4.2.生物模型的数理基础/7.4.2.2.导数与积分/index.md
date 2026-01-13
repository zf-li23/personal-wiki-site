**内容**：变化率（导数）与累积量（积分）的生物学对应（如生长速率、总生物量）；作为线性近似的导数。

## **为什么需要微积分？**

在上一节中，我们处理了离散时间下的线性系统，通过矩阵乘法描述了一年一度的种群变化。然而，许多生物过程是连续发生的：酶促反应中底物浓度的瞬时变化、神经元的膜电位在毫秒间的波动、细胞在培养基中的持续生长。要描述这种**连续变化**，我们需要微积分的语言。

微积分的核心是两个互逆的操作：
- **导数**：描述变化的**速率**（如何变化）
- **积分**：描述变化的**累积**（变化多少）

这一对概念如此基本，以至于生物学家几乎每天都在使用它们，即使没有明确意识到。当你谈论"生长速率"时，你在使用导数的思想；当你计算"总生物量"时，你在使用积分的思想。

## **2.2.1 导数：变化率的精确描述**

### **生物实例：细菌生长**

假设在富营养培养基中，细菌种群数量 $N(t)$ 随时间 $t$ 指数增长：

$$
N(t) = N_0 e^{rt}
$$

其中 $N_0$ 是初始数量，$r$ 是生长速率。那么，在时刻 $t$ 的**瞬时生长速率**是多少？

**导数的定义**：函数 $f(t)$ 在点 $t$ 的导数 $f'(t)$（或 $\dfrac{df}{dt}$）定义为：

$$
f'(t) = \lim_{\Delta t \to 0} \dfrac{f(t + \Delta t) - f(t)}{\Delta t}
$$

这个极限（如果存在）给出了函数在 $t$ 点的瞬时变化率。

### **Python实现：数值导数**

```python
import numpy as np
import matplotlib.pyplot as plt

# 定义细菌生长函数
def bacterial_growth(t, N0=100, r=0.5):
    """指数生长模型"""
    return N0 * np.exp(r * t)

# 计算数值导数
def numerical_derivative(f, t, dt=1e-6):
    """使用中心差分法计算导数"""
    return (f(t + dt) - f(t - dt)) / (2 * dt)

# 在时间区间上评估
time_points = np.linspace(0, 5, 100)  # 0到5小时
N_values = bacterial_growth(time_points)

# 计算理论导数和数值导数
r = 0.5
N0 = 100
theoretical_derivative = r * N0 * np.exp(r * time_points)  # dN/dt = rN

# 数值导数
numerical_derivatives = np.array([numerical_derivative(lambda t: bacterial_growth(t, N0, r), t) 
                                   for t in time_points])

# 可视化
plt.figure(figsize=(12, 4))

# 子图1：种群数量
plt.subplot(1, 2, 1)
plt.plot(time_points, N_values, 'b-', linewidth=2, label='$N(t) = N_0 e^{rt}$')
plt.xlabel('时间 (小时)')
plt.ylabel('细菌数量 $N(t)$')
plt.title('细菌指数生长')
plt.grid(True, alpha=0.3)
plt.legend()

# 子图2：生长速率
plt.subplot(1, 2, 2)
plt.plot(time_points, theoretical_derivative, 'r-', linewidth=2, label='理论导数 $rN(t)$')
plt.plot(time_points, numerical_derivatives, 'go', markersize=4, label='数值导数')
plt.xlabel('时间 (小时)')
plt.ylabel('生长速率 $dN/dt$')
plt.title('生长速率（导数）')
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()

# 比较理论值与数值值的差异
max_error = np.max(np.abs(theoretical_derivative - numerical_derivatives))
print(f"最大数值误差: {max_error:.2e}")
```

运行这段代码，你会发现：
1. 细菌数量呈指数增长
2. 生长速率（导数）同样呈指数增长，且与种群数量成正比：$\dfrac{dN}{dt} = rN$
3. 数值导数与理论导数高度一致

### **导数的生物学解释**

在生物学中，导数可以表示各种变化率：

1. **代谢速率**：$\dfrac{d[\text{底物}]}{dt}$，底物浓度的变化率
2. **膜电位变化**：$\dfrac{dV}{dt}$，神经元膜电位的变化率
3. **基因表达速率**：$\dfrac{d[\text{mRNA}]}{dt}$，mRNA浓度的变化率

### **高阶导数：变化率的变化率**

有时我们需要考虑变化率本身如何变化。例如，在种群生态学中，**加速度**（增长速率的变化率）可以指示种群是否接近环境承载力：

$$
\text{生长加速度} = \dfrac{d^2N}{dt^2}
$$

```python
# 计算二阶导数（加速度）
def numerical_second_derivative(f, t, dt=1e-4):
    """计算二阶导数"""
    return (f(t + dt) - 2*f(t) + f(t - dt)) / (dt**2)

# 逻辑斯蒂增长模型（考虑环境承载力）
def logistic_growth(t, N0=100, r=0.5, K=1000):
    """逻辑斯蒂增长：dN/dt = rN(1-N/K)"""
    return K / (1 + (K/N0 - 1) * np.exp(-r * t))

# 计算逻辑斯蒂增长的一阶和二阶导数
time_points = np.linspace(0, 20, 200)
N_logistic = logistic_growth(time_points)

# 数值导数
dN_dt = np.array([numerical_derivative(lambda t: logistic_growth(t), t) for t in time_points])
d2N_dt2 = np.array([numerical_second_derivative(lambda t: logistic_growth(t), t) for t in time_points])

# 找到拐点（加速度为零的点）
inflection_idx = np.where(np.diff(np.sign(d2N_dt2)))[0]

plt.figure(figsize=(10, 6))
plt.plot(time_points, N_logistic, 'b-', linewidth=2, label='种群数量 $N(t)$')
plt.plot(time_points, dN_dt, 'r-', linewidth=2, label='生长速率 $dN/dt$')
plt.plot(time_points, d2N_dt2, 'g-', linewidth=2, label='加速度 $d^2N/dt^2$')

# 标记拐点
if len(inflection_idx) > 0:
    t_inflection = time_points[inflection_idx[0]]
    N_inflection = N_logistic[inflection_idx[0]]
    plt.plot(t_inflection, N_inflection, 'ko', markersize=10, label='拐点')
    plt.axvline(t_inflection, color='k', linestyle='--', alpha=0.3)
    plt.axhline(N_inflection, color='k', linestyle='--', alpha=0.3)
    print(f"拐点: t = {t_inflection:.1f}, N = {N_inflection:.0f} (K/2 = 500)")

plt.xlabel('时间')
plt.ylabel('数量 / 速率')
plt.title('逻辑斯蒂增长及其导数')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

逻辑斯蒂增长的拐点出现在 $N = K/2$ 处，此时种群增长最快。二阶导数为零标志着增长从加速转为减速。

## **2.2.2 积分：累积量的精确计算**

### **生物实例：药物暴露总量**

如果患者静脉注射某种药物，血药浓度 $C(t)$ 随时间指数衰减：

$$
C(t) = C_0 e^{-kt}
$$

其中 $C_0$ 是初始浓度，$k$ 是清除率常数。那么，在时间区间 $[0, T]$ 内的**总药物暴露量**（药时曲线下面积，AUC）是多少？

**积分的定义**：函数 $f(t)$ 在区间 $[a, b]$ 上的定积分定义为：

$$
\int_a^b f(t) dt = \lim_{n \to \infty} \sum_{i=1}^n f(t_i^*) \Delta t
$$

其中 $\Delta t = (b-a)/n$，$t_i^*$ 是第 $i$ 个小区间中的某个点。这一定义对应着"曲线下面积"的直观概念。

### **Python实现：数值积分**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# 定义药物浓度函数
def drug_concentration(t, C0=100, k=0.3):
    """指数衰减的血药浓度"""
    return C0 * np.exp(-k * t)

# 计算理论积分（解析解）
def theoretical_integral(T, C0=100, k=0.3):
    """∫C0*exp(-kt)dt = (C0/k)(1 - exp(-kT))"""
    return (C0 / k) * (1 - np.exp(-k * T))

# 数值积分方法比较
def rectangle_integral(f, a, b, n=100):
    """矩形法数值积分"""
    t = np.linspace(a, b, n+1)
    dt = (b - a) / n
    # 左端点矩形法
    integral = sum(f(t[i]) * dt for i in range(n))
    return integral

def trapezoidal_integral(f, a, b, n=100):
    """梯形法数值积分"""
    t = np.linspace(a, b, n+1)
    y = f(t)
    integral = integrate.trapz(y, t)
    return integral

# 比较不同方法
T = 10  # 积分上限
C0, k = 100, 0.3

# 理论值
theoretical = theoretical_integral(T, C0, k)

# 数值方法
rect_10 = rectangle_integral(lambda t: drug_concentration(t, C0, k), 0, T, n=10)
rect_100 = rectangle_integral(lambda t: drug_concentration(t, C0, k), 0, T, n=100)
trap_10 = trapezoidal_integral(lambda t: drug_concentration(t, C0, k), 0, T, n=10)
trap_100 = trapezoidal_integral(lambda t: drug_concentration(t, C0, k), 0, T, n=100)

print(f"理论积分值 (AUC): {theoretical:.2f}")
print(f"\n数值积分结果:")
print(f"矩形法 (n=10): {rect_10:.2f}, 误差: {abs(rect_10-theoretical):.2f}")
print(f"矩形法 (n=100): {rect_100:.2f}, 误差: {abs(rect_100-theoretical):.2f}")
print(f"梯形法 (n=10): {trap_10:.2f}, 误差: {abs(trap_10-theoretical):.2f}")
print(f"梯形法 (n=100): {trap_100:.2f}, 误差: {abs(trap_100-theoretical):.2f}")

# 可视化积分过程
def plot_integration_method(f, a, b, n=10, method='rectangle'):
    """可视化数值积分方法"""
    t = np.linspace(a, b, 1000)
    y = f(t)
    
    # 积分点
    t_points = np.linspace(a, b, n+1)
    y_points = f(t_points)
    
    plt.figure(figsize=(10, 6))
    plt.plot(t, y, 'b-', linewidth=2, label='函数 $C(t)$')
    
    if method == 'rectangle':
        # 绘制矩形
        for i in range(n):
            left = t_points[i]
            right = t_points[i+1]
            height = y_points[i]  # 左端点高度
            plt.fill_between([left, right], 0, height, alpha=0.3, color='red')
            plt.plot([left, right], [height, height], 'r-', linewidth=1)
            plt.plot([right, right], [0, height], 'r-', linewidth=1)
        plt.title(f'矩形法积分 (n={n})')
    elif method == 'trapezoidal':
        # 绘制梯形
        for i in range(n):
            left = t_points[i]
            right = t_points[i+1]
            y_left = y_points[i]
            y_right = y_points[i+1]
            
            # 填充梯形
            vertices = [(left, 0), (left, y_left), (right, y_right), (right, 0)]
            from matplotlib.patches import Polygon
            polygon = Polygon(vertices, alpha=0.3, color='green')
            plt.gca().add_patch(polygon)
            
            # 绘制梯形边
            plt.plot([left, left], [0, y_left], 'g-', linewidth=1)
            plt.plot([right, right], [0, y_right], 'g-', linewidth=1)
            plt.plot([left, right], [y_left, y_right], 'g-', linewidth=1)
        plt.title(f'梯形法积分 (n={n})')
    
    plt.xlabel('时间 (小时)')
    plt.ylabel('药物浓度')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

# 可视化两种积分方法
plot_integration_method(lambda t: drug_concentration(t, C0, k), 0, T, n=10, method='rectangle')
plot_integration_method(lambda t: drug_concentration(t, C0, k), 0, T, n=10, method='trapezoidal')
```

### **积分的生物学应用**

积分在生物学中有广泛应用：

1. **总暴露量**：药时曲线下面积（AUC）是药效学的重要指标
2. **总生物量**：生长速率对时间的积分得到总生物量
3. **累积突变**：突变速率对时间的积分得到总突变数
4. **能量消耗**：代谢率对时间的积分得到总能量消耗

### **微积分基本定理：导数与积分的统一**

微积分基本定理建立了导数与积分的深刻联系：

$$
\int_a^b f'(t) dt = f(b) - f(a)
$$

以及

$$
\dfrac{d}{dx} \int_a^x f(t) dt = f(x)
$$

这意味着**积分是导数的逆运算**。在生物学中，这对应着：
- 总变化量 = 变化率的累积
- 瞬时变化率 = 总量函数的变化率

```python
# 验证微积分基本定理
def verify_fundamental_theorem():
    """验证微积分基本定理：积分和导数是互逆运算"""
    
    # 定义一个任意生物学相关的函数
    def f(t):
        # 类似于种群增长函数
        return 100 + 50 * np.sin(0.5 * t) + 20 * np.exp(-0.1 * t)
    
    def f_derivative(t, dt=1e-6):
        """f的数值导数"""
        return numerical_derivative(f, t, dt)
    
    # 区间 [a, b]
    a, b = 0, 10
    
    # 计算 ∫[a,b] f'(t) dt
    n_points = 1000
    t_points = np.linspace(a, b, n_points)
    f_prime_values = np.array([f_derivative(t) for t in t_points])
    
    # 数值积分
    integral_f_prime = trapezoidal_integral(lambda t: f_derivative(t), a, b, n=100)
    
    # 计算 f(b) - f(a)
    difference = f(b) - f(a)
    
    print(f"验证微积分基本定理:")
    print(f"∫[{a},{b}] f'(t) dt = {integral_f_prime:.6f}")
    print(f"f(b) - f(a) = {difference:.6f}")
    print(f"差异: {abs(integral_f_prime - difference):.6f}")
    
    # 第二部分：验证导数是积分的逆运算
    def F(x):
        """f的积分函数"""
        return trapezoidal_integral(f, a, x, n=200)
    
    # 在几个点验证 dF/dx = f(x)
    test_points = [2, 5, 8]
    print(f"\n验证 dF/dx = f(x):")
    for x in test_points:
        F_prime = numerical_derivative(F, x)
        print(f"在 x={x}: dF/dx = {F_prime:.4f}, f(x) = {f(x):.4f}, 差异 = {abs(F_prime - f(x)):.6f}")

verify_fundamental_theorem()
```

## **2.2.3 偏导数：多变量系统的变化率**

在生物学中，我们经常遇到依赖于多个变量的系统。例如，酶促反应速率可能同时依赖于底物浓度和温度。**偏导数** $\dfrac{\partial f}{\partial x}$ 描述了当其他变量保持不变时，函数 $f$ 关于变量 $x$ 的变化率。

### **生物实例：微生物生长速率**

微生物生长速率 $\mu$ 可能同时依赖于底物浓度 $S$ 和温度 $T$：

$$
\mu = \mu_{\max} \dfrac{S}{K_S + S} \cdot \dfrac{(T - T_{\min})(T_{\max} - T)}{(T_{\text{opt}} - T_{\min})(T_{\max} - T_{\text{opt}})}
$$

我们需要计算：
- $\dfrac{\partial \mu}{\partial S}$：底物浓度对生长速率的影响
- $\dfrac{\partial \mu}{\partial T}$：温度对生长速率的影响

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def growth_rate(S, T, mu_max=0.8, Ks=0.5, T_min=10, T_max=45, T_opt=35):
    """微生物生长速率作为底物浓度和温度的函数"""
    # Monod项
    monod_term = S / (Ks + S)
    
    # 温度项（简化的Ratkowsky模型）
    if T < T_min or T > T_max:
        temp_term = 0
    else:
        temp_term = ((T - T_min) * (T_max - T)) / ((T_opt - T_min) * (T_max - T_opt))
    
    return mu_max * monod_term * temp_term

def partial_derivative(f, var_idx, point, delta=1e-6):
    """计算多元函数的偏导数（数值方法）"""
    point = np.array(point, dtype=float)
    point_plus = point.copy()
    point_minus = point.copy()
    
    point_plus[var_idx] += delta
    point_minus[var_idx] -= delta
    
    return (f(*point_plus) - f(*point_minus)) / (2 * delta)

# 创建网格
S_vals = np.linspace(0, 5, 50)
T_vals = np.linspace(15, 40, 50)
S_grid, T_grid = np.meshgrid(S_vals, T_vals)

# 计算生长速率
mu_grid = np.array([[growth_rate(S, T) for S in S_vals] for T in T_vals])

# 计算偏导数在某点的值
point = [1.0, 25.0]  # S=1.0, T=25°C
dmu_dS = partial_derivative(lambda S, T: growth_rate(S, T), 0, point)
dmu_dT = partial_derivative(lambda S, T: growth_rate(S, T), 1, point)

print(f"在 S={point[0]}, T={point[1]}°C 时:")
print(f"生长速率 μ = {growth_rate(*point):.4f}")
print(f"∂μ/∂S = {dmu_dS:.4f} (底物浓度敏感度)")
print(f"∂μ/∂T = {dmu_dT:.4f} (温度敏感度)")

# 可视化生长速率曲面
fig = plt.figure(figsize=(14, 5))

# 3D曲面图
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
surf = ax1.plot_surface(S_grid, T_grid, mu_grid, cmap='viridis', alpha=0.8)
ax1.scatter(point[0], point[1], growth_rate(*point), color='red', s=100, label='分析点')
ax1.set_xlabel('底物浓度 S')
ax1.set_ylabel('温度 T (°C)')
ax1.set_zlabel('生长速率 μ')
ax1.set_title('微生物生长速率曲面')
fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=5)

# 等高线图
ax2 = fig.add_subplot(1, 2, 2)
contour = ax2.contourf(S_grid, T_grid, mu_grid, levels=20, cmap='viridis')
ax2.scatter(point[0], point[1], color='red', s=100, label=f'S={point[0]}, T={point[1]}')
ax2.set_xlabel('底物浓度 S')
ax2.set_ylabel('温度 T (°C)')
ax2.set_title('生长速率等高线')
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=10)

# 绘制梯度向量（偏导数指示方向）
ax2.quiver(point[0], point[1], dmu_dS * 0.5, dmu_dT * 0.5, 
           color='white', scale=20, width=0.005, label='梯度方向')

plt.legend()
plt.tight_layout()
plt.show()
```

偏导数在系统生物学中有重要应用：
1. **代谢控制分析**：通量控制系数是偏导数的形式
2. **敏感性分析**：参数变化对系统行为的影响
3. **优化问题**：寻找函数最大值/最小值（梯度下降法）

## **2.2.4 积分在生物建模中的应用**

### **应用1：计算总代谢产物**

在发酵过程中，代谢产物的累积量是生产速率的积分：

$$
P_{\text{total}} = \int_0^T q_P X dt
$$

其中 $q_P$ 是比生产速率，$X$ 是细胞浓度。

```python
def batch_fermentation_simulation():
    """模拟分批发酵过程"""
    # 模拟参数
    T = 48  # 发酵时间 (小时)
    time_points = np.linspace(0, T, 100)
    
    # 模拟细胞生长（逻辑斯蒂增长）
    X_max = 50  # 最大细胞浓度 (g/L)
    mu_max = 0.2  # 最大比生长速率 (1/h)
    X0 = 0.1  # 初始细胞浓度
    
    X = X_max / (1 + (X_max/X0 - 1) * np.exp(-mu_max * time_points))
    
    # 模拟产物形成（生长偶联型）
    Y_px = 0.3  # 产物对生物量的得率系数
    qP = Y_px * mu_max * (1 - X/X_max)  # 比生产速率
    
    # 计算产物浓度（积分）
    # P(t) = ∫₀ᵗ qP(s)X(s) ds
    P = np.zeros_like(time_points)
    for i, t in enumerate(time_points):
        # 数值积分计算到时间t的产物累积
        if i > 0:
            # 使用梯形法则
            dt = time_points[1] - time_points[0]
            production_rate = qP[:i+1] * X[:i+1]
            P[i] = np.trapz(production_rate, dx=dt)
    
    # 可视化
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10), sharex=True)
    
    ax1.plot(time_points, X, 'b-', linewidth=2)
    ax1.set_ylabel('细胞浓度 X (g/L)')
    ax1.set_title('分批发酵过程模拟')
    ax1.grid(True, alpha=0.3)
    
    ax2.plot(time_points, qP, 'r-', linewidth=2)
    ax2.set_ylabel('比生产速率 qP (g/g/h)')
    ax2.grid(True, alpha=0.3)
    
    ax3.plot(time_points, P, 'g-', linewidth=2)
    ax3.set_xlabel('时间 (小时)')
    ax3.set_ylabel('产物浓度 P (g/L)')
    ax3.grid(True, alpha=0.3)
    
    # 计算总产量
    total_product = P[-1]
    ax3.text(0.7, 0.7, f'总产量: {total_product:.1f} g/L', 
             transform=ax3.transAxes, fontsize=12,
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.show()
    
    return time_points, X, qP, P

# 运行发酵模拟
time_points, X, qP, P = batch_fermentation_simulation()
```

### **应用2：剂量-反应关系中的AUC**

在药理学中，效应-时间曲线下面积（AUEC）是药物效应持续时间的度量：

$$
\text{AUEC} = \int_0^T E(t) dt
$$

其中 $E(t)$ 是时间 $t$ 的药效强度。

```python
def pharmacodynamic_simulation():
    """模拟药物动力学-药效学(PK-PD)"""
    
    # PK模型：静脉注射后的血药浓度
    def C(t, D=100, V=10, ke=0.2):
        """一室模型"""
        return (D/V) * np.exp(-ke * t)
    
    # PD模型：Hill方程描述效应
    def E(t, Emax=100, EC50=5, n=2):
        """药效模型"""
        c = C(t)
        return (Emax * c**n) / (EC50**n + c**n)
    
    # 时间范围
    t = np.linspace(0, 48, 200)
    
    # 计算浓度和效应
    concentration = C(t)
    effect = E(t)
    
    # 计算AUC和AUEC
    auc = np.trapz(concentration, t)
    auec = np.trapz(effect, t)
    
    # 可视化
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    # PK曲线
    ax1.plot(t, concentration, 'b-', linewidth=2, label='血药浓度')
    ax1.fill_between(t, 0, concentration, alpha=0.3, color='blue')
    ax1.set_ylabel('浓度 (mg/L)')
    ax1.set_title('药物动力学 (PK)')
    ax1.text(0.7, 0.8, f'AUC = {auc:.1f} mg·h/L', 
             transform=ax1.transAxes, fontsize=12,
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # PD曲线
    ax2.plot(t, effect, 'r-', linewidth=2, label='药效强度')
    ax2.fill_between(t, 0, effect, alpha=0.3, color='red')
    ax2.set_xlabel('时间 (小时)')
    ax2.set_ylabel('效应强度 (%)')
    ax2.set_title('药效学 (PD)')
    ax2.text(0.7, 0.8, f'AUEC = {auec:.1f} %·h', 
             transform=ax2.transAxes, fontsize=12,
             bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.show()
    
    return auc, auec

# 运行PK-PD模拟
auc, auec = pharmacodynamic_simulation()
```

## **2.2.5 数值微积分的实用技巧**

### **处理噪声数据**

实验数据通常带有噪声，直接数值微分会放大噪声。解决方案包括：
1. **平滑后再微分**：使用移动平均或Savitzky-Golay滤波器
2. **拟合函数后解析微分**：先拟合平滑函数，再对拟合函数求导

```python
def noisy_data_differentiation():
    """处理噪声数据的微分"""
    
    # 生成带噪声的生长数据
    np.random.seed(42)
    t = np.linspace(0, 10, 50)
    true_growth = 100 * np.exp(0.3 * t)  # 真实生长曲线
    noisy_growth = true_growth + 10 * np.random.randn(len(t))  # 添加噪声
    
    # 方法1：直接数值微分（会放大噪声）
    dt = t[1] - t[0]
    direct_derivative = np.gradient(noisy_growth, dt)
    
    # 方法2：平滑后微分
    from scipy.signal import savgol_filter
    window_size = 11  # 滑动窗口大小（必须为奇数）
    polyorder = 3     # 多项式阶数
    smoothed = savgol_filter(noisy_growth, window_size, polyorder)
    smoothed_derivative = np.gradient(smoothed, dt)
    
    # 方法3：拟合指数函数后解析微分
    from scipy.optimize import curve_fit
    
    def exp_func(t, A, r):
        return A * np.exp(r * t)
    
    # 拟合指数函数
    params, _ = curve_fit(exp_func, t, noisy_growth, p0=[100, 0.3])
    A_fit, r_fit = params
    fit_growth = exp_func(t, A_fit, r_fit)
    fit_derivative = r_fit * fit_growth  # 解析导数
    
    # 可视化比较
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    # 原始数据和平滑
    ax1.plot(t, true_growth, 'k--', linewidth=2, label='真实曲线')
    ax1.plot(t, noisy_growth, 'bo', alpha=0.5, markersize=4, label='噪声数据')
    ax1.plot(t, smoothed, 'r-', linewidth=2, label='平滑后')
    ax1.plot(t, fit_growth, 'g-', linewidth=2, label='拟合曲线')
    ax1.set_ylabel('种群数量')
    ax1.set_title('噪声数据处理')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 导数比较
    true_derivative = 0.3 * true_growth
    ax2.plot(t, true_derivative, 'k--', linewidth=2, label='真实导数')
    ax2.plot(t, direct_derivative, 'bo', alpha=0.3, markersize=3, label='直接微分')
    ax2.plot(t, smoothed_derivative, 'r-', linewidth=2, label='平滑后微分')
    ax2.plot(t, fit_derivative, 'g-', linewidth=2, label='拟合后解析微分')
    ax2.set_xlabel('时间')
    ax2.set_ylabel('生长速率')
    ax2.set_title('导数计算比较')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # 计算误差
    errors = {
        '直接微分': np.mean((direct_derivative - true_derivative)**2),
        '平滑后微分': np.mean((smoothed_derivative - true_derivative)**2),
        '拟合后微分': np.mean((fit_derivative - true_derivative)**2)
    }
    
    print("均方误差比较:")
    for method, error in errors.items():
        print(f"  {method}: {error:.4f}")
    
    return errors

# 运行噪声数据处理示例
errors = noisy_data_differentiation()
```

### **自适应积分方法**

对于变化剧烈的函数，固定步长的积分可能效率低下或精度不足。自适应积分方法（如`scipy.integrate.quad`）会根据函数特性自动调整步长。

```python
def adaptive_integration_demo():
    """演示自适应积分的优势"""
    
    # 定义一个变化剧烈的生物学函数（如脉冲式基因表达）
    def pulse_expression(t):
        """模拟脉冲式基因表达"""
        return 100 * np.exp(-((t-5)**2) / 0.5) + 50 * np.exp(-((t-12)**2) / 1.0)
    
    # 积分区间
    a, b = 0, 20
    
    # 固定步长积分（梯形法）
    def fixed_step_integral(f, a, b, n):
        t = np.linspace(a, b, n+1)
        y = f(t)
        return np.trapz(y, t)
    
    # 自适应积分（使用SciPy）
    from scipy import integrate
    adaptive_result, adaptive_error = integrate.quad(pulse_expression, a, b)
    
    # 比较不同步长的结果
    n_values = [10, 20, 50, 100, 200, 500]
    fixed_results = []
    fixed_errors = []
    
    for n in n_values:
        result = fixed_step_integral(pulse_expression, a, b, n)
        fixed_results.append(result)
        fixed_errors.append(abs(result - adaptive_result))
    
    # 可视化
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # 函数图像
    t_fine = np.linspace(a, b, 1000)
    ax1.plot(t_fine, pulse_expression(t_fine), 'b-', linewidth=2)
    ax1.fill_between(t_fine, 0, pulse_expression(t_fine), alpha=0.3)
    ax1.set_xlabel('时间')
    ax1.set_ylabel('表达水平')
    ax1.set_title('脉冲式基因表达模式')
    ax1.grid(True, alpha=0.3)
    ax1.text(0.05, 0.9, f'自适应积分结果: {adaptive_result:.4f}', 
             transform=ax1.transAxes, fontsize=12,
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    # 误差比较
    ax2.semilogy(n_values, fixed_errors, 'ro-', linewidth=2, markersize=8)
    ax2.axhline(adaptive_error, color='k', linestyle='--', label=f'自适应积分误差估计: {adaptive_error:.2e}')
    ax2.set_xlabel('固定步长积分的分割数 n')
    ax2.set_ylabel('与自适应积分的绝对误差')
    ax2.set_title('积分精度比较')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.show()
    
    print(f"自适应积分结果: {adaptive_result:.6f} ± {adaptive_error:.2e}")
    print("\n固定步长积分结果:")
    for n, result, error in zip(n_values, fixed_results, fixed_errors):
        print(f"  n={n:3d}: 结果={result:.6f}, 误差={error:.2e}")

# 运行自适应积分演示
adaptive_integration_demo()
```

## **总结与展望**

本节介绍了微积分的两个核心操作——**导数**与**积分**，并展示了它们在生物学中的广泛应用：

### **关键概念回顾**
1. **导数**描述瞬时变化率，应用于生长速率、反应速率等
2. **积分**描述累积量，应用于总暴露量、总产量等
3. **微积分基本定理**统一了微分与积分：变化率的累积等于总变化
4. **偏导数**处理多变量系统，应用于敏感性分析
5. **数值方法**使微积分计算可行，即使对于复杂函数或噪声数据

### **生物学意义**
- 导数让我们能**量化变化**：不只是"种群在增长"，而是"以每小时5%的速率增长"
- 积分让我们能**从速率回到总量**：从生长速率计算总生物量，从生产速率计算总产量
- 微积分提供了**连接机制与现象**的数学框架：从分子相互作用的速率方程到宏观可观测的动态

### **计算实现要点**
- 数值导数：使用中心差分法提高精度
- 数值积分：梯形法通常比矩形法更准确
- 处理噪声：平滑或拟合后再微分
- 自适应积分：对变化剧烈的函数更高效

### **展望下一节**

在下一节（2.3 常微分方程）中，我们将把这些工具组合起来，建立描述生物系统动态演化的微分方程模型。导数和积分不再是孤立的操作，而是微分方程求解的基础：

- 导数出现在方程中描述变化率
- 积分出现在解中描述状态演化

例如，简单的指数增长模型 $\dfrac{dN}{dt} = rN$ 将导数与函数本身联系起来，而其解 $N(t) = N_0 e^{rt}$ 则通过积分得到。

**思考题**：
1. 如果一个细胞的体积以恒定速率增长，其表面积的增长速率如何变化？这对物质交换有何影响？
2. 在药物多次给药方案中，如何用积分计算稳态血药浓度？
3. 对于振荡系统（如昼夜节律），导数与函数值有怎样的相位关系？
4. 如何用微积分描述捕食者-猎物系统中能量的流动与转化？

通过掌握导数与积分，你不仅获得了分析生物动态的工具，更获得了一种新的思维方式——从静态描述到动态理解，从瞬时快照到过程追踪。这正是数学建模赋予生物学的独特视角。

---

*在下一节中，我们将把这些工具整合到常微分方程框架中，开始构建真正的动态生物系统模型。*