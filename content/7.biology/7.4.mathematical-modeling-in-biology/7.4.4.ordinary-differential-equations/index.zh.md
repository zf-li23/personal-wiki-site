---
title: 常微分方程
---

**内容**：ODE的建立；数值求解（欧拉法，`scipy.integrate.odeint`）；相图与相轨迹的几何直观。

在前两节中，我们分别探讨了离散时间系统（Leslie矩阵、逻辑斯谛映射）和连续时间系统（逻辑斯谛增长）。这些模型都描述了生物系统中的动态行为。本节将进一步深入**连续时间动力系统**，重点介绍常微分方程（ODE）模型的建立、分析与可视化方法。我们将以生态学中的经典模型——Lotka-Volterra竞争模型和捕食者-猎物模型为例，展示ODE建模的全过程。

## 4.1. 常微分方程基本理论

### 4.1.1. 常微分方程的基本概念

常微分方程（Ordinary Differential Equations, ODEs）是描述系统状态随时间变化规律的数学工具。

**定义**：形如
$$
\frac{\mathrm{d}x}{\mathrm{d}t} = f(x, t)
$$
的方程称为一阶常微分方程，其中$x(t)$是未知函数，$f(x,t)$是已知函数。

**自治系统**：当$f$不显式依赖于时间$t$时，即
$$
\frac{\mathrm{d}x}{\mathrm{d}t} = f(x)
$$
称为自治系统。这是生态模型中常见的形式，反映了系统动态仅由当前状态决定。

**高阶系统**：对于多变量系统，我们有方程组
$$
\begin{cases}
\frac{\mathrm{d}x_1}{\mathrm{d}t} &= f_1(x_1, x_2, \ldots, x_n) \\
\frac{\mathrm{d}x_2}{\mathrm{d}t} &= f_2(x_1, x_2, \ldots, x_n) \\
&\vdots \\
\frac{dx_n}{dt} &= f_n(x_1, x_2, \ldots, x_n)
\end{cases}
$$

### 4.1.2. 平衡点与稳定性

**平衡点**：满足$f(x^*) = 0$的状态$x^*$称为平衡点，系统一旦达到该状态将保持不变。

**稳定性分析**：
1. **线性稳定性理论**：在平衡点$x^*$附近线性化系统
   $$
   \frac{\mathrm{d}(\delta x)}{\mathrm{d}t} = J(x^*) \delta x
   $$
   其中$J(x^*)$是雅可比矩阵$J_{ij} = \frac{\partial f_i}{\partial x_j}\big|_{x=x^*}$

2. **特征值判据**：对于二维系统$J = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$，特征值满足
   $$
   \lambda^2 - \operatorname{tr}(J)\lambda + \det(J) = 0
   $$
   其中$\operatorname{tr}(J) = a+d$，$\det(J) = ad-bc$

3. **稳定性分类**：
   - 稳定结点：$\lambda_1, \lambda_2 < 0$（实数）
   - 不稳定结点：$\lambda_1, \lambda_2 > 0$（实数）
   - 鞍点：$\lambda_1 < 0 < \lambda_2$（实数）
   - 稳定焦点：$\operatorname{Re}(\lambda_{1,2}) < 0$（复数）
   - 不稳定焦点：$\operatorname{Re}(\lambda_{1,2}) > 0$（复数）
   - 中心：$\operatorname{Re}(\lambda_{1,2}) = 0$（纯虚数）

### 4.1.3. 数值求解方法

#### 4.1.3.1. 欧拉法（Euler Method）
最简单的显式数值方法：
$$
x_{n+1} = x_n + h f(x_n, t_n)
$$
其中$h$为步长。全局误差$O(h)$，条件稳定。

#### 4.1.3.2. 龙格-库塔法（Runge-Kutta Methods）
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

#### 4.1.3.3. `scipy.integrate`模块
Python中常用的ODE求解器：
- `odeint`: 基于LSODA算法的通用求解器
- `solve_ivp`: 更灵活的接口，支持多种方法（RK45, RK23, BDF等）

### 4.1.4. 相图与相轨迹

**相空间**：以状态变量为坐标轴构成的空间。对于二维系统，相平面为$(x,y)$平面。

**向量场**：在每个点$(x,y)$处，向量$(f_1(x,y), f_2(x,y))$表示状态变化的方向和速率。

**轨迹（Trajectory）**：系统状态随时间在相空间中描绘的曲线，满足
$$
\frac{\mathrm{d}}{\mathrm{d}t} \begin{pmatrix} x(t) \\ y(t) \end{pmatrix} = \begin{pmatrix} f_1(x,y) \\ f_2(x,y) \end{pmatrix}
$$

**零增长线（Nullclines）**：满足$\mathrm{d}x/\mathrm{d}t=0$或$\mathrm{d}y/\mathrm{d}t=0$的曲线。零增长线的交点即为平衡点。

## 4.2. Lotka-Volterra种间竞争模型

### 4.2.1. 模型推导与归一化

在真实生态系统中，物种很少孤立存在，它们为有限资源而竞争。Lotka-Volterra竞争模型扩展了单物种逻辑斯谛增长，描述了两个物种竞争同一资源时的动态变化。

假设两个物种的种群数量分别为$N_1(t)$和$N_2(t)$。每个物种单独存在时遵循逻辑斯谛增长：

$$
\begin{split}
\frac{\mathrm{d}N_1}{\mathrm{d}t} &= r_1 N_1 \left(1 - \frac{N_1}{K_1}\right) \\
\frac{\mathrm{d}N_2}{\mathrm{d}t} &= r_2 N_2 \left(1 - \frac{N_2}{K_2}\right)
\end{split}
$$

其中$r_i$为物种$i$的内禀增长率，$K_i$为其环境容纳量。

当两个物种共存时，它们相互竞争资源。竞争效应通过**竞争系数**$\alpha_{12}$和$\alpha_{21}$量化：
- $\alpha_{12}$：每个$N_2$个体对物种1增长的抑制效应，相当于$\alpha_{12}$个$N_1$个体。
- $\alpha_{21}$：每个$N_1$个体对物种2增长的抑制效应，相当于$\alpha_{21}$个$N_2$个体。

完整的竞争模型为：

$$
\begin{aligned}
\frac{\mathrm{d}N_1}{\mathrm{d}t} &= r_1 N_1 \left(1 - \frac{N_1}{K_1} - \frac{\alpha_{12} N_2}{K_1}\right) \\
\frac{\mathrm{d}N_2}{\mathrm{d}t} &= r_2 N_2 \left(1 - \frac{N_2}{K_2} - \frac{\alpha_{21} N_1}{K_2}\right)
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
\frac{\mathrm{d}x}{\mathrm{d}\tau} &= x(1 - x - a y) \\
\frac{\mathrm{d}y}{\mathrm{d}\tau} &= \rho y(1 - y - b x)
\end{aligned}
$$

### 4.2.2. 平衡点与零增长线分析

**零增长线**（nullcline）是相平面中满足$\frac{\mathrm{d}x}{\mathrm{d}\tau} = 0$或$\frac{\mathrm{d}y}{\mathrm{d}\tau} = 0$的曲线：

1. $x$-零增长线：$\frac{\mathrm{d}x}{\mathrm{d}\tau} = 0 \Rightarrow x = 0$或$y = \frac{1-x}{a}$
2. $y$-零增长线：$\frac{\mathrm{d}y}{\mathrm{d}\tau} = 0 \Rightarrow y = 0$或$y = 1 - b x$

这些直线将相平面划分为不同区域，在每个区域内，$x$和$y$的变化方向是确定的。

**平衡点**是系统不再变化的状态，即同时满足$\frac{\mathrm{d}x}{\mathrm{d}\tau} = 0$和$\frac{\mathrm{d}y}{\mathrm{d}\tau} = 0$的点：

1. $(0,0)$：两个物种灭绝
2. $(1,0)$：物种1达到最大容量，物种2灭绝
3. $(0,1)$：物种2达到最大容量，物种1灭绝
4. $\left(\frac{1-a}{1-ab}, \frac{1-b}{1-ab}\right)$：共存平衡点（要求$0 < \frac{1-a}{1-ab} < 1$且$0 < \frac{1-b}{1-ab} < 1$）

### 4.2.3. 四种竞争结果及其普适规律

竞争模型的长期行为由参数$a$和$b$的相对大小决定，产生四种可能结果：

![竞争模型四种结果的零增长线示意图](./plots/competition-outcomes-schematic.py)

**运行结果说明**：上述代码生成的原理图清晰地展示了Lotka-Volterra竞争模型的四种可能结果。每个子图中：

1. 红色实线表示物种1的零增长线($\mathrm{d}x/\mathrm{d}\tau=0$)，蓝色实线表示物种2的零增长线($\mathrm{d}y/\mathrm{d}\tau=0$)
2. 关键点标注包括：
   - $K_1$: 物种1单独存在时的最大容量
   - $K_2$: 物种2单独存在时的最大容量
   - $K_1/\alpha$: 物种1零增长线与y轴的交点
   - $K_2/\beta$: 物种2零增长线与x轴的交点
3. 箭头指示了相平面不同区域的向量场方向
4. 文本框显示了每种情况对应的参数条件

这四种结果可以总结为：

1. **物种1获胜**：当$K_1 > K_2/\beta$且$K_2 < K_1/\alpha$（$a<1$且$b>1$）时，物种2无法在竞争中生存
2. **物种2获胜**：当$K_2 > K_1/\alpha$且$K_1 < K_2/\beta$（$a>1$且$b<1$）时，物种1无法在竞争中生存
3. **不稳定共存**：当$K_1 > K_2/\beta$且$K_2 > K_1/\alpha$（$a>1$且$b>1$）时，初始条件决定最终获胜者
4. **稳定共存**：当$K_1 < K_2/\beta$且$K_2 < K_1/\alpha$（$a<1$且$b<1$）时，两个物种可以长期共存

### 4.2.4. 竞争系数的生物学意义

竞争系数 $a$ 和 $b$ 反映了物种间的竞争强度：
- 当 $a < 1$ 时，种内竞争强于种间竞争，物种1对自身的影响大于物种2对它的影响
- 当 $\alpha > 1$ 时，种间竞争强于种内竞争，物种2对物种1的影响大于物种1对自身的影响
- $b$ 的意义与 $a$ 类似，但表示物种1对物种2的影响

竞争结果取决于相对竞争强度而非绝对数值。这种相对性体现了生态位理论的核心思想：生态位重叠越小（竞争系数越小），共存的可能性越大。

### 4.2.5. 稳定性分析

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

![竞争模型四种情况的相图与时间序列](./plots/competition-simulations.py)

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

## 4.3. Lotka-Volterra捕食者-猎物模型

### 4.3.1. 模型建立与归一化

捕食者-猎物相互作用是生态学中的另一经典场景。Lotka-Volterra捕食者-猎物模型描述了捕食者和猎物种群之间的振荡动态。

设$N(t)$为猎物种群数量，$P(t)$为捕食者种群数量。经典模型假设：

1. 没有捕食者时，猎物以指数速率$r$增长
2. 没有猎物时，捕食者以指数速率$-m$减少（$m>0$）
3. 捕食者与猎物的相遇导致猎物被捕食，同时促进捕食者增长

模型方程为：

$$
\begin{aligned}
\frac{\mathrm{d}N}{\mathrm{d}t} &= rN - \varepsilon NP \\
\frac{\mathrm{d}P}{\mathrm{d}t} &= -\mu P + \theta NP
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
\frac{\mathrm{d}x}{\mathrm{d}\tau} &= x(1 - y) \\
\frac{\mathrm{d}y}{\mathrm{d}\tau} &= \alpha y(x - 1)
\end{aligned}
$$

### 4.3.2. 零增长线与平衡点分析

**零增长线**：
1. 猎物零增长线：$\frac{\mathrm{d}x}{\mathrm{d}\tau} = 0 \Rightarrow x = 0$或$y = 1$
2. 捕食者零增长线：$\frac{\mathrm{d}y}{\mathrm{d}\tau} = 0 \Rightarrow y = 0$或$x = 1$

**平衡点**：
1. $(0,0)$：灭绝（鞍点）
2. $(1,1)$：共存平衡点（中心）

### 4.3.3. 稳定性分析：中心与极限环

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
特征值为 $\lambda = \pm \mathrm{i}\sqrt{r\mu}$，为纯虚数，表明该平衡点是**中心**。在非线性系统中，这通常意味着存在**周期解**。

在经典的Lotka-Volterra模型中，曲线是全闭的，但如果遇到其他类型的动力学（这在现实场景中是普遍现象）将会诱发**极限环**现象，即系统的震荡轨道会被汇聚到这个环上。

### 4.3.4. 捕食者-猎物模型的振荡行为

经典Lotka-Volterra模型具有保守量：

$$
V(x,y) = \alpha(x - \ln x) + (y - \ln y)
$$

满足$\mathrm{d}V/\mathrm{d}\tau = 0$，表明所有轨迹都是闭曲线，系统具有周期性解。这种周期性振荡反映了捕食者与猎物数量的相互制约关系。

![捕食者-猎物模型的零增长线、振荡与极限环示意图](./plots/predator-prey-schematic.py)

**运行结果说明**：上述代码生成了捕食者-猎物模型的四种原理图：

1. **经典Lotka-Volterra模型相平面**：
   - 红色水平线表示猎物零增长线($\mathrm{d}x/\mathrm{d}\tau=0$)
   - 蓝色垂直线表示捕食者零增长线($\mathrm{d}y/\mathrm{d}\tau=0$)
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

### 4.3.5. 带有密度制约的修正模型

更现实的模型包含猎物的密度制约（逻辑斯谛增长）：
$$
\begin{aligned}
\frac{\mathrm{d}x}{\mathrm{d}\tau} &= x(1 - x - y) \\
\frac{\mathrm{d}y}{\mathrm{d}\tau} &= \alpha y(x - \beta)
\end{aligned}
$$
其中$\beta = \mu/(rK\theta)$，$K$为猎物环境容纳量。

为什么不考虑捕食者的环境容纳量呢？因为在这个很简化的模型中，唯一影响捕食者生存的因子就是猎物的数量，所以捕食者也已经被猎物的环境容纳量所限制了。

该模型可能出现：
1. 捕食者灭绝（$\beta > 1$）
2. 稳定焦点（阻尼振荡趋向平衡点）
3. 稳定极限环（自持振荡）

![经典、阻尼与极限环捕食者-猎物模型的数值模拟](./plots/predator-prey-simulations.py)

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

### 4.3.6. 捕食者-猎物模型的生态学启示

捕食者-猎物模型揭示了几个重要生态学原理：

1. **种群振荡的必然性**：在没有外部干扰的情况下，捕食者-猎物系统倾向于呈现周期性振荡。
2. **时滞效应**：捕食者数量变化滞后于猎物数量变化，这是由捕食者需要时间将猎物转化为自身增长造成的。
3. **稳定性条件**：加入猎物密度制约（逻辑斯谛项）可以稳定系统，防止振幅无限扩大。
4. **生态平衡的动态性**：平衡不是静态的，而是动态振荡中的长期平均状态。

## 4.4. 复杂模型：竞争与捕食的结合

### 4.4.1. 统一框架下的生态模型

现实生态系统往往同时包含竞争和捕食等多种相互作用。考虑一个包含两个竞争物种和一个捕食者的系统：

$$
\begin{aligned}
\frac{\mathrm{d}x_1}{\mathrm{d}t} &= r_1 x_1 \left(1 - \frac{x_1}{K_1} - \alpha_{12}\frac{x_2}{K_1}\right) - \varepsilon_1 x_1 y \\
\frac{\mathrm{d}x_2}{\mathrm{d}t} &= r_2 x_2 \left(1 - \frac{x_2}{K_2} - \alpha_{21}\frac{x_1}{K_2}\right) - \varepsilon_2 x_2 y \\
\frac{\mathrm{d}y}{\mathrm{d}t} &= -\mu y + \theta_1 x_1 y + \theta_2 x_2 y
\end{aligned}
$$

其中$x_1$和$x_2$是两个竞争物种，$y$是捕食者。

### 4.4.2. 归一化与简化

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
\frac{\mathrm{d}u_1}{\mathrm{d}\tau} &= u_1(1 - u_1 - a u_2 - v) \\
\frac{\mathrm{d}u_2}{\mathrm{d}\tau} &= \rho u_2(1 - u_2 - b u_1 - \frac{c_2}{c_1} v) \\
\frac{\mathrm{d}v}{\mathrm{d}\tau} &= -d v + e_1 u_1 v + e_2 u_2 v
\end{aligned}
$$

由于这是一个新模型，可以先尝试一些数值模拟，探索其可能的行为：

![复杂生态模型的数值模拟、行为分类与参数敏感性](./plots/complex-ecosystem-simulations.py)

### 4.4.3. 动力学行为分类

三维及以上的动力系统可能展现混沌行为。以洛伦兹系统为例：
$$
\begin{aligned}
\frac{\mathrm{d}x}{\mathrm{d}t} &= \sigma(y - x) \\
\frac{\mathrm{d}y}{\mathrm{d}t} &= x(\rho - z) - y \\
\frac{\mathrm{d}z}{\mathrm{d}t} &= xy - \beta z
\end{aligned}
$$

**混沌的特征**：
1. 对初始条件敏感（蝴蝶效应）
2. 有界非周期运动
3. 具有分形结构（分岔图，上一节已经介绍过）

![洛伦兹吸引子及其对初始条件的敏感性](./plots/lorenz-chaos.py)

回到主题，这一复杂模型可能展现多种动力学行为，例如：

1. **竞争排斥**：一个猎物物种被淘汰，系统退化为简单的捕食者-猎物系统
2. **捕食者介导的共存**：捕食者通过抑制优势竞争者，为劣势物种创造生存空间
3. **周期振荡**：捕食者-猎物振荡与竞争相互作用耦合
4. **混沌**：三维系统中可能出现对初始条件敏感的非周期行为

![复杂生态系统（竞争+捕食）的三维状态空间示意图](./plots/complex-ecosystem-state-space.py)

**运行结果说明**：上述代码生成了复杂生态系统的原理图：

- 红色平面：$u_1=0$（物种1灭绝）
- 蓝色平面：$u_2=0$（物种2灭绝）
- 绿色平面：$v=0$（捕食者灭绝）
- 三条示例轨迹展示了不同动力学行为

### 4.4.4. 复杂模型的生态学启示

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
   \frac{\mathrm{d}N}{\mathrm{d}t} = rN\left(1-\frac{N}{K}\right) - \varepsilon NP
   $$
   $$
   \frac{\mathrm{d}P}{\mathrm{d}t} = -\mu P + \theta NP
   $$
   分析平衡点的稳定性。与经典模型相比，密度制约如何改变系统行为？绘制相图和时间序列。

**模型建立**

经典 Lotka-Volterra 捕食者-猎物模型为：
$$
\begin{aligned}
\frac{\mathrm{d}N}{\mathrm{d}t} &= rN - \varepsilon NP \\
\frac{\mathrm{d}P}{\mathrm{d}t} &= -\mu P + \theta NP
\end{aligned}
$$
其中 $N$ 为猎物种群，$P$ 为捕食者种群，$r$ 为猎物内禀增长率，$\varepsilon$ 为捕食效率，$\mu$ 为捕食者死亡率，$\theta$ 为捕食者将猎物转化为新生捕食者的效率。

现在考虑猎物增长受到环境容纳量 $K$ 的限制，即猎物遵循逻辑斯谛增长，修改后模型为：
$$
\begin{aligned}
\frac{\mathrm{d}N}{\mathrm{d}t} &= rN\left(1 - \frac{N}{K}\right) - \varepsilon NP \\
\frac{\mathrm{d}P}{\mathrm{d}t} &= -\mu P + \theta NP
\end{aligned}
$$

为了简化分析，引入无量纲变量：
$$
x = \frac{N}{K},\quad y = \frac{\varepsilon}{r}P,\quad \tau = rt,\quad \alpha = \frac{\mu}{r},\quad \beta = \frac{\theta K}{r}
$$
则系统化为：
$$
\begin{aligned}
\frac{\mathrm{d}x}{\mathrm{d}\tau} &= x(1 - x) - xy = x(1 - x - y) \\
\frac{\mathrm{d}y}{\mathrm{d}\tau} &= \alpha y(\beta x - 1)
\end{aligned}
$$
其中 $\alpha = \mu/r$，$\beta = \theta K / r$。这里 $\beta$ 可视为捕食者成功捕食并繁殖的效率与猎物承载力的综合参数。

**平衡点与稳定性分析**

1. **零增长线**：
   - 猎物零增长线：$x=0$ 或 $y = 1 - x$。
   - 捕食者零增长线：$y=0$ 或 $x = 1/\beta$。

2. **平衡点**：
   - $(0,0)$：灭绝平衡点。
   - $(1,0)$：猎物达到最大容量，捕食者灭绝。
   - 共存平衡点 $(x^*, y^*)$，满足 $x^* = 1/\beta$，$y^* = 1 - x^*$。要求 $x^* < 1$ 即 $\beta > 1$，且 $y^* > 0$。

3. **稳定性分析**：
   雅可比矩阵为：
   $$
   J(x,y) = \begin{pmatrix}
   1 - 2x - y & -x \\
   \alpha\beta y & \alpha(\beta x - 1)
   \end{pmatrix}
   $$
   代入各平衡点：

   - $(0,0)$：$J = \begin{pmatrix}1 & 0 \\ 0 & -\alpha\end{pmatrix}$，特征值 $\lambda_1=1>0$，$\lambda_2=-\alpha<0$，为**鞍点**（不稳定）。

   - $(1,0)$：$J = \begin{pmatrix}-1 & -1 \\ 0 & \alpha(\beta - 1)\end{pmatrix}$，特征值 $\lambda_1=-1$，$\lambda_2 = \alpha(\beta-1)$。当 $\beta < 1$ 时 $\lambda_2<0$，平衡点稳定（猎物独占且捕食者无法维持）；当 $\beta > 1$ 时 $\lambda_2>0$，为鞍点。

   - $(x^*, y^*) = \left(\frac{1}{\beta}, 1-\frac{1}{\beta}\right)$：代入雅可比矩阵：
     $$
     J^* = \begin{pmatrix}
     1 - \frac{2}{\beta} - (1-\frac{1}{\beta}) & -\frac{1}{\beta} \\
     \alpha\beta (1-\frac{1}{\beta}) & \alpha(\beta \cdot \frac{1}{\beta} - 1)
     \end{pmatrix}
     = \begin{pmatrix}
     -\frac{1}{\beta} & -\frac{1}{\beta} \\
     \alpha(\beta - 1) & 0
     \end{pmatrix}
     $$
     特征方程为：
     $$
     \lambda^2 + \frac{1}{\beta}\lambda + \frac{\alpha(\beta-1)}{\beta} = 0
     $$
     特征值：
     $$
     \lambda = \frac{-\frac{1}{\beta} \pm \sqrt{\frac{1}{\beta^2} - \frac{4\alpha(\beta-1)}{\beta}}}{2}
     $$
     稳定性由迹 $-\frac{1}{\beta}<0$ 和行列式 $\frac{\alpha(\beta-1)}{\beta}$ 决定：
     - 当 $\beta > 1$ 时，行列式 > 0，迹 < 0，因此若判别式 $\Delta = \frac{1}{\beta^2} - \frac{4\alpha(\beta-1)}{\beta} \ge 0$，则为稳定结点；若 $\Delta < 0$，则为稳定焦点（螺旋趋向平衡点）。
     - 当 $\beta = 1$ 时，行列式为 0，退化情况。
     - 当 $\beta < 1$ 时，共存点不存在。

     由此可见，加入密度制约后，经典模型的**中性稳定中心**变为**渐近稳定平衡点**（稳定结点或焦点），振荡逐渐衰减。这是密度制约引入的负反馈所致。

**数值模拟与对比**

下面使用 Python 代码对两种模型进行模拟，绘制相图和时间序列，直观展示密度制约对系统行为的影响。

![带密度制约的捕食者-猎物模型与经典模型的对比](./plots/density-dependent-predator-prey.py)

**与经典模型的对比讨论**

| 特性 | 经典 Lotka-Volterra | 带密度制约的模型 |
|------|---------------------|------------------|
| 猎物增长 | 指数增长 | 逻辑斯谛增长（受 K 限制） |
| 平衡点稳定性 | 中心（中性稳定） | 渐近稳定（稳定结点/焦点） |
| 振荡行为 | 等幅振荡（振幅由初始条件决定） | 阻尼振荡（振幅衰减至平衡点） |
| 对参数敏感性 | 轨迹始终闭合，周期固定 | 参数 β>1 时系统趋于平衡，β<1 时捕食者灭绝 |
| 生态学意义 | 理想化情形，缺乏稳定机制 | 更现实，密度制约提供负反馈，使系统稳定 |

密度制约的引入使捕食者-猎物系统从结构不稳定的中心变为结构稳定的焦点，解释了真实生态系统中振荡通常不会无限持续的原因。

3. 查找经典的哈德逊湾公司猞猁-雪兔数据（或其他捕食者-猎物时间序列数据，或自己生成一份数据），尝试用Lotka-Volterra模型拟合。估计参数并评估模型拟合优度。讨论模型的局限性。

**数据准备**

哈德逊湾公司记录的猞猁（捕食者）和雪兔（猎物）数量（单位：千只）如下：

| Year | Hares | Lynx |
|------|-------|------|
| 1900 | 30.0  | 4.0  |
| 1901 | 47.2  | 6.1  |
| 1902 | 70.2  | 9.8  |
| 1903 | 77.4  | 35.2 |
| 1904 | 36.3  | 59.4 |
| 1905 | 20.6  | 41.7 |
| 1906 | 18.1  | 19.0 |
| 1907 | 21.4  | 13.0 |
| 1908 | 22.0  | 8.3  |
| 1909 | 25.4  | 9.1  |
| 1910 | 27.1  | 7.4  |
| 1911 | 40.3  | 8.0  |
| 1912 | 57.0  | 12.3 |
| 1913 | 76.6  | 19.5 |
| 1914 | 52.3  | 45.7 |
| 1915 | 19.5  | 51.1 |
| 1916 | 11.2  | 29.7 |
| 1917 | 7.6   | 15.8 |
| 1918 | 14.6  | 9.7  |
| 1919 | 16.2  | 10.1 |
| 1920 | 24.7  | 8.6  |

**可视化原始数据**

首先绘制时间序列图，观察两者的周期性变化和相位关系。

![哈德逊湾公司雪兔与猞猁数量的时间序列](./plots/lynx-hare-data.py)

观察可见，两者呈现明显的周期性波动，且猞猁数量变化滞后于雪兔，符合捕食者-猎物模型的基本特征。

### 拟合 Lotka-Volterra 模型

经典 Lotka-Volterra 模型（原变量形式）为：
$$
\begin{aligned}
\frac{\mathrm{d}H}{\mathrm{d}t} &= a H - b H L \\
\frac{\mathrm{d}L}{\mathrm{d}t} &= -c L + d H L
\end{aligned}
$$
其中 $H$ 为雪兔数量，$L$ 为猞猁数量，$a$ 为兔子自然增长率，$b$ 为捕食率，$c$ 为猞猁死亡率，$d$ 为转化效率。

我们需要估计参数 $a,b,c,d$。拟合方法：使用数值积分求解 ODE，将模拟值与观测值的误差平方和最小化。

![Lotka-Volterra 模型拟合猞猁-雪兔数据](./plots/lynx-hare-fit.py)

#### 结果与评估

运行上述代码，可能得到类似如下的参数估计：
- $a \approx 0.55$（兔子年增长率约48%）
- $b \approx 0.028$（每只猞猁每年捕食兔子的比例）
- $c \approx 0.85$（猞猁自然死亡率约76%）
- $d \approx 0.027$（每捕食一只兔子转化为新生猞猁的效率）

**拟合优度**：拟合误差 (MSE): 36.07

#### 讨论模型的局限性

尽管 Lotka-Volterra 模型能再现基本振荡模式，但它存在诸多局限性：

1. **模型假设过于简化**：
   - 猎物无限增长（无密度制约），与真实生态系统中食物资源有限的事实不符。
   - 捕食者功能反应为线性（$bHL$），即捕食率与猎物密度成正比，忽略了捕食者饱和效应。
   - 环境参数恒定，未考虑气候、其他食物源、人类活动等因素。

2. **数据质量问题**：
   - 哈德逊湾公司的记录基于皮毛贸易数据，可能受狩猎强度、采样偏差等影响，并非真实的种群数量。
   - 时间跨度有限（仅21年），难以捕捉系统的长期行为。

3. **系统复杂性**：
   - 真实生态系统中，雪兔和猞猁的相互作用并非孤立，还受到其他物种（如雪兔的其他捕食者、猞猁的替代猎物）和环境随机性的影响。
   - 可能存在密度制约、时滞效应、年龄结构等复杂因素，这些在简单 LV 模型中均被忽略。

4. **参数可辨识性问题**：
   - 优化得到的参数可能不唯一，不同初始猜测可能导致不同结果。
   - 模型对初始条件敏感，而观测数据本身存在误差。

因此，尽管 Lotka-Volterra 模型是理解捕食者-猎物相互作用的基础，但用于实际数据拟合和预测时需谨慎。更现实的模型（如带密度制约、Holling 功能反应、随机微分方程等）可能提供更好的拟合，但也会引入更多参数，增加复杂性。

4. 考虑一个包含两个竞争物种和一个捕食者的三物种系统。设计数值实验，探究在什么条件下捕食者可以促进竞争物种的共存。绘制三维相图展示不同动力学状态。
