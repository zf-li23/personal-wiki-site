---
title: SciPy
description: SciPy 的结构及其与 NumPy 的关系；scipy.linalg 与可重复使用的矩阵分解；用 scipy.optimize 做极小化、求根与曲线拟合；用 solve_ivp 求积分与初值问题，刚性与方法的选择；插值与样条；scipy.stats 中的分布对象与检验；稀疏数组、存储格式与稀疏求解器；快速 Fourier 变换。
source_hash: 184d988d6ba1
---

NumPy 提供数组及其上的基本运算；SciPy 提供建立在其上的数值算法：优化、函数与微分方程的积分、插值、统计、稀疏矩阵、信号处理与 Fourier 变换。这些算法大多已有几十年历史，由经过充分检验的 Fortran、C 和 C++ 库（QUADPACK、ODEPACK、FITPACK、ARPACK、SuperLU 等）或精心编写的 Python 代码实现，所以用户的任务仍然是：把问题表述成库所期望的形式，选择方法，并检验结果。本章对最常用的子包做一次导览。与 [4.4.3](/4.4.3) 一样，方法的理论在别处讲解，这里只给出链接：优化与求根见 [3.5.4](/3.5.4) 和 [3.5.5](/3.5.5)，微分方程见 2.4（[2.4.4](/2.4.4)），插值与条件数见 [3.5.1](/3.5.1)。示例使用 SciPy 1.18（2026 年 10 月）与 NumPy 2.5；数据表格是下一章 [4.4.5](/4.4.5) 的主题。

## 4.1. 概览

SciPy 按子包组织，每个子包需要单独导入（只写 `import scipy` 并不会全部加载）：

| 子包 | 内容 |
|---|---|
| `scipy.linalg` | 稠密线性代数：`numpy.linalg` 的全部功能，加上 LU、Schur、QZ、矩阵函数（`expm`、`sqrtm`）与结构化矩阵的求解器 |
| `scipy.optimize` | 极小化、求根、曲线拟合、最小二乘、线性规划 |
| `scipy.integrate` | 函数与样本的数值积分、常微分方程 |
| `scipy.interpolate` | 一维与多维插值、样条、平滑 |
| `scipy.stats` | 概率分布、描述统计、假设检验、bootstrap |
| `scipy.sparse` | 稀疏数组、稀疏线性求解器与特征值求解器（`scipy.sparse.linalg`）、图算法（`scipy.sparse.csgraph`） |
| `scipy.fft` | 快速 Fourier 变换及相关的变换 |
| `scipy.signal` | 滤波、卷积、谱分析、峰值检测 |
| `scipy.spatial` | k-d 树、距离、Delaunay 三角剖分、凸包、旋转 |
| `scipy.special` | 特殊函数：Gamma、Beta、Bessel、误差函数、`logsumexp`、`expit` |
| `scipy.ndimage` | n 维图像上的滤波与形态学运算 |
| `scipy.io`、`scipy.constants` | 文件格式（MATLAB、Matrix Market、WAV）、物理常数 |

约定是导入子包，而不是导入函数：写 `from scipy import optimize`，再用 `optimize.minimize`，这样每个函数的来源一目了然。

当某个子包与 NumPy 重叠时，SciPy 的版本通常更完整。`scipy.linalg` 总是使用 LAPACK，并提供例如只计算一次、可对许多右端项重复使用的矩阵分解，这是 `numpy.linalg.solve` 做不到的：

```python
import numpy as np
from scipy import linalg

rng = np.random.default_rng(0)
A = rng.standard_normal((500, 500))
lu, piv = linalg.lu_factor(A)              # O(n^3), once
for _ in range(10):
    b = rng.standard_normal(500)
    x = linalg.lu_solve((lu, piv), b)      # O(n^2) per right-hand side
print(linalg.expm(np.array([[0.0, 1.0], [-1.0, 0.0]])).round(4))
# [[ 0.5403  0.8415]
#  [-0.8415  0.5403]]   the rotation by 1 radian
```

`scipy.special` 值得一提，因为它包含了一些容易写错的函数的数值上讲究的版本：`gammaln` 计算 $\log\Gamma(x)$（$\Gamma(1000)$ 本身就会上溢），`logsumexp` 计算 $\log\sum_i \mathrm{e}^{a_i}$ 而不会上溢（`logsumexp([1000, 1000])` 得到 $1000 + \log 2$），`expit` 计算 logistic 函数，`comb(n, k, exact=True)` 精确计算二项式系数。

SciPy 正在逐步采用数组 API 标准（[4.4.2](/4.4.2#sec-2.8)）：设置环境变量 `SCIPY_ARRAY_API=1` 后，越来越多的函数接受 PyTorch、CuPy 或 JAX 数组，并在它们的设备上计算。这一支持在 SciPy 1.18 中仍处于实验阶段。

## 4.2. 优化

### 4.2.1. 极小化

`optimize.minimize(fun, x0, method=..., jac=..., bounds=..., constraints=...)` 从 `x0` 出发，对向量 $\boldsymbol{x}$ 的标量函数求极小，返回一个 `OptimizeResult` 对象，其属性包括解 `x`、极小值 `fun`、标志 `success`、信息 `message`，以及迭代次数 `nit` 与函数求值次数 `nfev`。应当根据对问题的了解选择方法：

| 方法 | 使用 | 约束 | 说明 |
|---|---|---|---|
| `Nelder-Mead` | 仅函数值 | 边界 | **Nelder–Mead 方法**（[3.5.4](/3.5.4#sec-4.2.3)）；稳健，较慢，适用于低维 |
| `Powell` | 仅函数值 | 边界 | 不用导数的共轭方向法 |
| `BFGS` | 梯度 | 无 | 拟 Newton 法（**BFGS 更新**，[3.5.5](/3.5.5#sec-5.1.4.4)）；无约束时的默认方法 |
| `L-BFGS-B` | 梯度 | 边界 | 有限内存 BFGS；适用于大规模问题；有边界时的默认方法 |
| `CG` | 梯度 | 无 | 非线性**共轭梯度法**（[3.5.5](/3.5.5#sec-5.3.2)） |
| `Newton-CG`、`trust-exact`、`trust-krylov` | 梯度与 Hesse 矩阵 | 无 | Newton 型方法与**置信域法**（[3.5.5](/3.5.5#sec-5.1.5.1)） |
| `SLSQP`、`trust-constr`、`COBYQA` | 梯度（COBYQA 不需要） | 一般约束 | 非线性等式与不等式约束 |

通过 `jac` 提供梯度，可以使基于梯度的方法更快、更精确；不提供时，SciPy 用有限差分近似梯度，在 $p$ 维情形下每个梯度要付出 $p + 1$ 次函数求值的代价。Rosenbrock 函数 $f(x, y) = (1 - x)^2 + 100(y - x^2)^2$ 有一道狭窄弯曲的山谷，极小点在 $(1, 1)$，是标准的测试函数：

```python
from scipy import optimize


def rosen(x):
    return (1 - x[0]) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2


def rosen_grad(x):
    return np.array([-2 * (1 - x[0]) - 400 * x[0] * (x[1] - x[0] ** 2),
                     200 * (x[1] - x[0] ** 2)])


x0 = np.array([-1.2, 1.0])
res = optimize.minimize(rosen, x0, method="BFGS", jac=rosen_grad)
print(res.x, res.nit, res.nfev, res.success)   # [1. 1.] 32 39 True
```

| 方法 | 梯度 | 解 | 迭代次数 | 函数求值次数 |
|---|---|---|---|---|
| Nelder–Mead | 无 | $(1.000022, 1.000042)$ | 85 | 159 |
| BFGS | 有限差分 | $(0.999996, 0.999991)$ | 32 | 117 |
| BFGS | 精确 | $(1, 1)$，精确到 6 位 | 32 | 39 |
| L-BFGS-B | 精确 | $(0.999999, 0.999998)$ | 36 | 44 |

用有限差分时，BFGS 每次迭代需要三次函数求值（一次函数值，二维情形下梯度需要两次），精度也较低。边界以 `(low, high)` 对的列表传入；例如取 `bounds=[(-2, 0.5), (-2, 2)]` 时，L-BFGS-B 返回位于边界上的约束极小点 $(0.5, 0.25)$。约束以字典传入，如 `{"type": "ineq", "fun": lambda x: 1 - x[0]**2 - x[1]**2}`，表示 $1 - x^2 - y^2 \ge 0$；有了它，SLSQP 求得位于单位圆上的极小点 $(0.7864, 0.6177)$。

所有这些方法找到的都是局部极小点。对于有许多局部极小点的函数，`optimize.differential_evolution`、`dual_annealing` 和 `basinhopping` 做全局搜索，代价要高得多；从许多个起点重新启动局部方法是一种简单的替代办法。一维函数用 `optimize.minimize_scalar` 求极小，它使用 **Brent 法**，把**黄金分割法**与抛物线插值结合起来（[3.5.4](/3.5.4#sec-4.2.1)）。

### 4.2.2. 求根

对于标量方程 $f(x) = 0$，`optimize.root_scalar` 提供两类方法：括号法需要一个符号发生改变的区间 $[a, b]$，总是收敛；开放法需要一个起点，收敛时速度更快：

```python
f = lambda x: x ** 3 - 2 * x - 5          # Newton's historical example
s = optimize.root_scalar(f, bracket=[2, 3], method="brentq")
print(s.root, s.iterations)               # 2.094551481542327 7
s = optimize.root_scalar(f, x0=2.0, fprime=lambda x: 3 * x ** 2 - 2, method="newton")
print(s.root, s.iterations)               # 2.0945514815423265 4
```

`brentq`（**Brent 法**，[3.5.4](/3.5.4#sec-4.3.6)）把**二分法**、**弦截法**与**逆二次插值**结合起来；只要知道一个括号区间，它就是首选的方法。**牛顿法**（[3.5.5](/3.5.5#sec-5.1.1)）从好的起点出发二次收敛，但从坏的起点出发可能发散。对于方程组 $\boldsymbol{F}(\boldsymbol{x}) = \boldsymbol{0}$，`optimize.root` 默认使用修正的 Powell 混合方法：

```python
def F(v):
    x, y = v
    return [x ** 2 + y ** 2 - 4, np.exp(x) + y - 1]

sol = optimize.root(F, [1.0, -1.0])
print(sol.x, sol.success)                 # [ 1.00416874 -1.72963729] True
```

### 4.2.3. 曲线拟合

用**最小二乘法**把非线性模型 $y \approx f(x; \boldsymbol{\theta})$ 拟合到数据，是实验科学中最常见的优化任务。`optimize.curve_fit(f, xdata, ydata, p0)` 用 **Levenberg–Marquardt 法**（[3.5.5](/3.5.5#sec-5.1.5.3)）极小化 $\sum_i (y_i - f(x_i; \boldsymbol{\theta}))^2$，返回估计值以及估计的**协方差矩阵**，由此可以得到近似的**标准误**。以酶动力学的 Michaelis–Menten 模型 $v = V_{\max} S / (K_{\mathrm{m}} + S)$ 为例：

```python
def michaelis_menten(S, Vmax, Km):
    return Vmax * S / (Km + S)


rng = np.random.default_rng(0)
S = np.array([0.5, 1, 2, 4, 8, 16, 32, 64])
v = michaelis_menten(S, 10.0, 4.0) * (1 + 0.05 * rng.standard_normal(S.size))   # 5% noise
p, cov = optimize.curve_fit(michaelis_menten, S, v, p0=[5, 1])
print(p.round(3), np.sqrt(np.diag(cov)).round(3))   # [10.554  4.468] [0.154 0.234]
```

![模拟的 Michaelis-Menten 数据，以及 curve_fit 拟合的曲线和真实曲线；图例中给出估计的参数及其标准误](./plots/michaelis-menten.py)

模型函数把自变量放在第一个，参数作为单独的实参。对于非线性问题，合理的起点 `p0` 很重要；这里它是从数据中读出的（$V_{\max}$ 接近最大的速率，$K_{\mathrm{m}}$ 接近速率达到其一半时的浓度）。标准误假定模型正确，误差相互独立且方差为常数；若测量误差已知，通过 `sigma` 传入（并设置 `absolute_sigma=True`）。更一般的底层函数是 `optimize.least_squares(residuals, x0)`，它还支持边界以及能减小离群值影响的稳健损失函数。若把模型线性化（Lineweaver–Burk 图，即 $1/v$ 对 $1/S$ 作图），则会扭曲误差结构、给出有偏的估计；有了计算机，非线性拟合才是正确的方法。

## 4.3. 积分

### 4.3.1. 数值积分

`integrate.quad(f, a, b)` 用自适应的 Gauss–Kronrod 求积（来自 Fortran 库 QUADPACK）计算 $\int_a^b f(x)\,\mathrm{d}x$，返回积分值及绝对误差的估计。允许无穷的积分限，`f` 的额外参数通过 `args` 传入：

```python
from scipy import integrate

val, err = integrate.quad(lambda x: np.exp(-x ** 2), -np.inf, np.inf)
print(val, err, np.sqrt(np.pi))            # 1.7724538509055159 1.42e-08 1.7724538509055159
val, err = integrate.quad(lambda x, a: x ** a, 0, 1, args=(2,))
print(val)                                 # 0.33333333333333337
```

误差估计对光滑的被积函数是可靠的；对于有奇点、间断点或尖峰的被积函数，应当用 `points=[...]` 给出它们的位置，或者把区间分开。**重积分**由 `dblquad`、`tplquad` 和 `nquad` 计算，`quad_vec` 对向量值函数积分。

当被积函数只在采样点上已知时，例如测得的时间序列，我们使用复合求积公式：`integrate.trapezoid(y, x=x)` 与 `integrate.simpson(y, x=x)` 给出积分，`integrate.cumulative_trapezoid(y, x=x, initial=0)` 给出累积积分。对 $\int_0^\pi \sin x\,\mathrm{d}x = 2$ 取 11 个点，梯形公式给出 $1.9835$，Simpson 公式给出 $2.0001$，反映出它们的误差分别为 $h^2$ 阶与 $h^4$ 阶。

### 4.3.2. 初值问题

**初值问题** $\boldsymbol{y}' = \boldsymbol{f}(t, \boldsymbol{y})$，$\boldsymbol{y}(t_0) = \boldsymbol{y}_0$，用 `integrate.solve_ivp(fun, t_span, y0, method=..., t_eval=..., ...)` 数值求解。解的存在性与唯一性是 [2.4.4](/2.4.4) 的主题；数值方法一步一步地构造近似解，最简单的是 [2.4.4](/2.4.4#sec-4.4.1) 的 **Euler 折线**。实用的求解器使用更高阶的方法，并自适应地选择步长，使估计的局部误差在每个分量上都小于 $\mathrm{atol} + \mathrm{rtol}\,\lvert y\rvert$。

接口遵循几条约定：

- `fun(t, y)` 的第一个参数是时间，第二个是状态向量，返回长度相同的序列 $\boldsymbol{y}'$。参数通过 `args` 传入。
- `t_span = (t0, tf)` 是求解区间；求解器自己选择步长。要在指定的时刻得到解，传入 `t_eval`，或者传入 `dense_output=True` 并计算连续的插值函数 `sol.sol(t)`。
- 结果包含时刻 `sol.t`、形状为 `(n_components, n_times)` 的解 `sol.y`（每个分量一行）、标志 `sol.success`，以及 `fun` 的求值次数 `sol.nfev`。
- 默认的容差 `rtol=1e-3`、`atol=1e-6` 较宽松。它们对作图已经够用，但不适合定量的结果。

Lotka–Volterra 方程描述被捕食者的种群 $x$ 与捕食者的种群 $y$：

$$
x' = ax - bxy, \qquad y' = -cy + dxy.
$$
它们有守恒量 $H(x, y) = dx - c\log x + by - a\log y$，因此精确的轨道是闭曲线，这提供了检验精度的办法。

```python
def lotka_volterra(t, z, a, b, c, d):
    x, y = z
    return [a * x - b * x * y, -c * y + d * x * y]


params = (1.0, 0.1, 1.5, 0.075)
sol = integrate.solve_ivp(lotka_volterra, (0, 30), [10, 5], args=params,
                          rtol=1e-8, atol=1e-10, dense_output=True)
print(sol.t.size, sol.nfev)            # 345 2174
print(sol.sol(10.0).round(4))          # [ 8.0066 11.4162]
```

在这些容差下，$H$ 沿计算出的解的变化为 $3 \times 10^{-8}$；用默认的容差时，求解器只走 44 步（350 次求值），$H$ 的变化为 $0.04$，表现为轨道的缓慢漂移。

![用 solve_ivp 求解的 Lotka-Volterra 模型：被捕食者与捕食者的种群随时间的变化（左），以及围绕平衡点 (c/d, a/b) 的三个初始条件在相平面上的闭轨道（右）](./plots/lotka-volterra.py)

事件用于定位解的某个函数过零的时刻，例如种群超过某个阈值。事件函数 `g(t, y)` 有可选的属性 `terminal`（终止积分）和 `direction`（只检测向上或向下的穿越）：

```python
def predator_peak(t, z, *args):
    return z[1] - 20          # predator population crosses 20
predator_peak.direction = 1   # upward crossings only

s = integrate.solve_ivp(lotka_volterra, (0, 30), [10, 5], args=params,
                        events=predator_peak, rtol=1e-8)
print(s.t_events[0].round(4))  # [ 3.0172  8.4969 13.9766 19.4563 24.936 ]
```

### 4.3.3. 刚性问题与方法的选择

`solve_ivp` 提供显式与隐式的方法：

| 方法 | 类型 | 阶 | 用途 |
|---|---|---|---|
| `RK45`（默认） | 显式 Runge–Kutta（Dormand–Prince） | 5(4) | 非刚性问题，中等精度 |
| `DOP853` | 显式 Runge–Kutta | 8 | 非刚性问题，高精度 |
| `RK23` | 显式 Runge–Kutta（Bogacki–Shampine） | 3(2) | 非刚性问题，宽松的容差 |
| `Radau` | 隐式 Runge–Kutta | 5 | 刚性问题 |
| `BDF` | 隐式多步法（向后差分） | 1–5 | 刚性问题 |
| `LSODA` | 在 Adams 法与 BDF 之间切换 | 可变 | 不知道是否刚性 |

这种困难称为刚性（stiffness）：一个问题是刚性的，是指它含有时间尺度相差很大的过程，例如快速的化学反应与缓慢的输运同时存在，因而即使解本身变化缓慢，显式方法为了稳定也必须取很小的步长。$\mu = 1000$ 的 van der Pol 振子 $u'' - \mu(1 - u^2)u' + u = 0$（[2.4.11](/2.4.11#sec-11.6.3)）是典型的例子：它的解在缓慢的漂移与突然的跳变之间交替。把它写成一阶方程组，在 $[0, 3000]$ 上积分，在测试机器上得到：

| 方法 | 步数 | `fun` 的求值次数 | 时间 |
|---|---|---|---|
| `RK45` | 1 687 436 | 11 859 590 | 101 s |
| `Radau` | 285 | 2 824 | 0.18 s |
| `BDF` | 539 | 1 902 | 0.14 s |
| `LSODA` | 728 | 1 803 | 0.01 s |

四种方法都成功了，但显式方法需要多 3000 倍的步数。隐式方法每一步都要借助 **Jacobi 矩阵** $\partial\boldsymbol{f}/\partial\boldsymbol{y}$ 求解一个非线性方程组；通过 `jac=` 提供它可以省去有限差分近似，而对于大型稀疏系统，例如离散化的**偏微分方程**，`jac_sparsity=` 会有帮助。实用的规则是：先用 `RK45`；若它出乎意料地慢或步数极多，就试试 `BDF`、`Radau` 或 `LSODA`。

## 4.4. 插值

插值构造一个通过给定点 $(x_i, y_i)$ 的函数。用一个全局多项式通过许多等距点时，函数在两端附近会振荡，这就是**多项式插值**的 **Runge 现象**，所以实际的插值使用分段多项式。`scipy.interpolate` 提供了几种，它们在光滑性与保形性上各不相同：

| 类或函数 | 方法 | 性质 |
|---|---|---|
| `np.interp(x, xp, fp)` | 分段线性 | 连续，保形，不光滑 |
| `CubicSpline(x, y)` | 三次样条 | 二阶连续可微；可能过冲 |
| `PchipInterpolator(x, y)` | 单调分段三次 Hermite | 一阶可微；数据单调之处它也单调 |
| `Akima1DInterpolator(x, y, method="makima")` | 修正的 Akima | 一阶可微；几乎不过冲 |
| `make_interp_spline(x, y, k)` | $k$ 次 B 样条 | 一般的样条插值 |
| `make_smoothing_spline(x, y, lam)` | 平滑样条 | 对有噪声的数据不做精确插值 |
| `RegularGridInterpolator`、`griddata` | 多维 | 规则网格、散乱数据 |

三次样条（cubic spline）是在每个区间 $[x_i, x_{i+1}]$ 上为三次多项式、在结点处二阶连续可微的函数；再加两个边界条件（默认是 not-a-knot 条件）就能使它唯一。它的光滑性对光滑数据是理想的，但在有阶跃的数据上会过冲，这对必须保持在某个范围内的量，如浓度或概率，是不可接受的。PCHIP 与修正的 Akima 插值保持单调性，代价是二阶导数不连续：

```python
from scipy import interpolate

x = np.array([0, 1, 2, 3, 4, 5.0])
y = np.array([0, 0, 0, 1, 1, 1.0])
cs = interpolate.CubicSpline(x, y)
pc = interpolate.PchipInterpolator(x, y)
print(cs([2.5, 3.5]), pc([2.5, 3.5]))   # [0.5   1.125] [0.5 1. ]: the spline overshoots to 1.125
print(cs.derivative()(2.5), cs.integrate(0, 5))   # 1.1666666666666665 2.5
```

![左：用 np.interp、CubicSpline、PchipInterpolator 和修正的 Akima 对阶跃形的数据插值；三次样条出现过冲。右：取 11 个等距结点的 Runge 函数；10 次插值多项式在两端附近振荡，三次样条则没有](./plots/interpolation.py)

插值对象都是可调用的，并有计算导数、原函数、积分与根的方法。较老的类 `interp1d` 现在被标为遗留（legacy）；上面的类可以取代它。

## 4.5. 统计

### 4.5.1. 分布对象

`scipy.stats` 含有约 110 个连续分布和 20 个离散分布。每个分布都是一个对象，有计算密度（`pdf`，离散分布用 `pmf`）、**分布函数**（`cdf`）、**生存函数**（`sf`，即 $1 - F$，在远尾部很精确）、**分位数**函数（`ppf`，分布函数的反函数）、**矩**、随机变量取值（`rvs`）与拟合（`fit`）的方法。所有连续分布都由形状参数与 `loc`、`scale` 一起参数化，使得对标准变量 $Z$ 有 $X = \mathrm{loc} + \mathrm{scale}\cdot Z$。和 NumPy 的 `Generator`（[4.4.3](/4.4.3#sec-3.4.2)）一样，这意味着对于**正态分布**，`scale` 是标准差，对于**指数分布**，`scale` 是均值 $1/\lambda$：

```python
from scipy import stats

X = stats.norm(loc=1.0, scale=2.0)           # N(1, 4), a "frozen" distribution
print(X.mean(), X.var(), X.cdf(1.0))         # 1.0 4.0 0.5
print(stats.norm.ppf(0.975))                 # 1.959963984540054, the quantile z_{0.025}
print(stats.expon(scale=1 / 2.0).mean())     # 0.5 for Exp(2)
print(stats.gamma(a=3.0, scale=1 / 2.0).var())   # 0.75 for Gamma(3, 2)
rng = np.random.default_rng(0)
print(X.rvs(size=3, random_state=rng))       # draws use a NumPy Generator
```

SciPy 1.15 引入了分布的新接口，其中分布是带有命名参数的类（`stats.Normal(mu=1.0, sigma=2.0)`，方法有 `pdf`、`cdf`、`icdf`、`sample`），并且**随机变量**可以做算术变换：`2 * stats.Normal(mu=1.0, sigma=2.0) + 1` 仍是一个分布对象，均值为 3，标准差为 4。`stats.make_distribution` 能把其他分布转换成这种形式。经典接口仍然得到完全的支持，大多数代码和文档仍在使用它。

### 4.5.2. 估计与检验

参数用**极大似然估计**通过 `fit` 估计；不需要估计的参数用 `floc=0` 之类的实参固定：

```python
data = stats.gamma(a=3.0, scale=0.5).rvs(size=500, random_state=rng)
print(stats.gamma.fit(data, floc=0))   # (3.213..., 0, 0.455...): shape, loc, scale
```

假设检验返回结果对象，其中有统计量、**p 值**，许多检验还有其他信息，如**自由度**或**置信区间**：

```python
a = rng.normal(0.0, 1.0, 30)
b = rng.normal(0.8, 1.0, 30)
t = stats.ttest_ind(a, b, equal_var=False)      # Welch's t-test
print(t.statistic, t.pvalue, t.df)              # -3.533 0.00085 53.58 (rounded)
print(t.confidence_interval(0.95))              # interval for the difference of the means
print(stats.mannwhitneyu(a, b).pvalue)          # 0.00289, the rank-based alternative
```

其他常用的函数有 `pearsonr`、`spearmanr`、`linregress`、`chi2_contingency`、`fisher_exact`、`shapiro`、`kstest`、`wilcoxon`、`kruskal`、`f_oneway`，以及重抽样方法 `bootstrap` 和 `permutation_test`。较新的函数通过名为 `rng` 的参数接受 NumPy 的 `Generator`，较老的则通过 `random_state`。检验的含义以及何时有效，是统计学课程的主题；对于带公式的回归模型、标准误与诊断，statsmodels 包比 `scipy.stats` 更方便。

## 4.6. 稀疏矩阵

### 4.6.1. 存储格式

科学中的许多大型矩阵以零元素为主：微分方程的离散化只耦合相邻的网格点，网络的**邻接矩阵**每条边对应一个元素，单细胞测序中基因乘细胞的计数矩阵通常有 90% 以上的零。稀疏矩阵（sparse matrix）是以只记录非零元素的格式存储的矩阵，因此内存与计算量随非零元素的个数而不是随 $mn$ 增长。`scipy.sparse` 提供了几种格式，各自适合不同的运算：

| 格式 | 存储 | 适用于 |
|---|---|---|
| COO（坐标格式） | 三个数组：行下标、列下标、值 | 构造；重复的元素被相加 |
| CSR（压缩稀疏行） | 逐行存储的值与列下标，加上行指针 `indptr` | 行切片、矩阵与向量的乘积、算术运算 |
| CSC（压缩稀疏列） | 按列存储，方式与 CSR 相同 | 列切片、直接求解器 |
| LIL、DOK | 每行一个列表、以键为索引的字典 | 逐个元素地改变稀疏模式 |
| DIA | 对角线 | 带状矩阵 |

在 CSR 格式中，第 $i$ 行的列下标与值分别是 `indices[indptr[i]:indptr[i+1]]` 与 `data[indptr[i]:indptr[i+1]]`。典型的流程是用 COO（或用 `diags_array`、`block_array`、`kron`）组装矩阵，转换一次成 CSR 或 CSC，然后再计算。

SciPy 有两套类：较老的稀疏矩阵类（sparse matrices，`csr_matrix` 等），它们模仿 `np.matrix`；较新的稀疏数组类（sparse arrays，`csr_array` 等），行为与 NumPy 数组一样。新代码应使用稀疏数组。两者的差别体现在 `*` 上：对稀疏矩阵它是矩阵乘法，对稀疏数组则是逐元素乘法，与稠密数组完全一样；`@` 对两者都是矩阵乘法。

```python
from scipy import sparse

n = 6
off, main = -np.ones(n - 1), 2 * np.ones(n)
L = sparse.diags_array([off, main, off], offsets=[-1, 0, 1], format="csr")
print(type(L).__name__, L.shape, L.nnz)    # csr_array (6, 6) 16
print(L.indptr)                            # [ 0  2  5  8 11 14 16]
print((L * L)[0, 0], (L @ L)[0, 0])        # 4.0 5.0: elementwise versus matrix product
coo = sparse.coo_array(([1.0, 2.0, 3.0], ([0, 1, 1], [2, 0, 0])), shape=(2, 3))
print(coo.toarray())                       # [[0. 0. 1.]  [5. 0. 0.]]: entry (1, 0) summed
```

### 4.6.2. 稀疏线性代数

`scipy.sparse.linalg` 含有利用稀疏性的求解器。上面的三对角矩阵除以 $h^2$，就是 $-u''$ 在间距为 $h$ 的网格上的离散化，所以求解 $L\boldsymbol{u} = \boldsymbol{f}$ 近似求解**边值问题** $-u'' = f$，$u(0) = u(1) = 0$，即一维的 **Poisson 方程**。对于 $f = 1$，精确解是 $u(x) = x(1 - x)/2$，离散化在舍入误差范围内精确地重现了它：

```python
from scipy.sparse import linalg as spla


def laplacian_1d(n):
    h = 1 / (n + 1)
    main, off = 2 * np.ones(n), -np.ones(n - 1)
    return sparse.diags_array([off, main, off], offsets=[-1, 0, 1], format="csr") / h ** 2


n = 100_000
A = laplacian_1d(n)
x = np.linspace(0, 1, n + 2)[1:-1]
u = spla.spsolve(A.tocsc(), np.ones(n))
print(np.abs(u - x * (1 - x) / 2).max())    # 2.3e-11
```

$n = 10^5$ 的稀疏矩阵占用 4 MB，求解用时 0.1 s；同样的矩阵若按稠密格式存储，则需要 80 GB。主要的工具有：

| 任务 | 函数 | 方法 |
|---|---|---|
| 直接求解 | `spsolve(A, b)`、`splu(A)`、`factorized(A)` | 稀疏 LU（SuperLU） |
| 迭代求解，对称正定 | `cg(A, b, rtol=...)` | **共轭梯度法**（[3.5.5](/3.5.5#sec-5.3.2)） |
| 迭代求解，一般 | `gmres`、`bicgstab`、`minres` | Krylov 子空间方法 |
| 少数几个特征值 | `eigsh(A, k, sigma=...)`、`eigs` | Lanczos 与 Arnoldi 方法（ARPACK） |
| 少数几个奇异值 | `svds(A, k)` | |
| 无矩阵算子 | `LinearOperator(shape, matvec=...)` | 迭代方法只需要乘积 $A\boldsymbol{v}$ |

迭代方法的收敛速度由**条件数**决定。对于 $n = 1000$，$\kappa(A) \approx 4 \times 10^5$，共轭梯度法需要 500 次迭代才能使相对残差达到 $10^{-10}$，而直接求解器只需 2 ms；对于这个一维问题，直接方法显然更好。对于大型的二维和三维问题，直接求解器受填充（fill-in）之害，带预条件子的迭代方法成为首选。对 $n = 1000$，用移位求逆模式的 `spla.eigsh(A, k=3, sigma=0)` 算出的 $A$ 的最小几个特征值，与精确值 $\frac{4}{h^2}\sin^2\frac{k\pi h}{2} \approx (k\pi)^2$（$k = 1, 2, 3$）在所有打印出的位数上都一致。稀疏邻接矩阵上的图算法（最短路径、**连通支**、**最小生成树**，见 [4.3.11](/4.3.11)）在 `scipy.sparse.csgraph` 中。

## 4.7. 快速 Fourier 变换

序列 $x_0, \dots, x_{N-1}$ 的离散 Fourier 变换（discrete Fourier transform），简记为 DFT，是

$$
X_k = \sum_{n=0}^{N-1} x_n\,\mathrm{e}^{-2\pi\mathrm{i}kn/N}, \qquad k = 0, 1, \dots, N - 1,
$$
它是 **Fourier 变换**的离散类比，把序列分解成频率为每个采样 $k/N$ 个周期的振荡。直接计算需要 $O(N^2)$ 次运算；快速 Fourier 变换（fast Fourier transform），简记为 FFT，通过递归地把它拆分成较小规模的变换，只需 $O(N \log N)$ 次运算，这是一种**分治**算法（[4.1.11](/4.1.11)）。FFT 是科学计算中最重要的算法之一：谱分析、快速**卷积**、图像处理和**偏微分方程**的数值求解都以它为基础。

`scipy.fft`（以及功能相似但较小的 `numpy.fft`）提供：

| 函数 | 用途 |
|---|---|
| `fft`、`ifft` | 复变换及其逆变换 |
| `rfft`、`irfft` | 对实输入：只输出 $N/2 + 1$ 个非负频率，约快一倍 |
| `fftfreq(N, d)`、`rfftfreq(N, d)` | 输出对应的频率，采样间隔为 `d` |
| `fft2`、`fftn`、`rfftn` | 多维变换 |
| `fftshift` | 重新排序，使零频率位于中间 |
| `dct`、`dst` | 离散余弦与正弦变换 |
| `next_fast_len(N)` | 不小于 $N$ 且素因子较小的长度，用于补零 |

归一化的约定是：正变换不带因子，逆变换带因子 $1/N$，如上面的公式；`norm="ortho"` 对两者都使用 $1/\sqrt{N}$，`norm="forward"` 则把 $1/N$ 放在正变换上。不同的库和教材约定不同，所以最好用一个小例子检验。速度取决于 $N$ 的素因子分解：只含较小素因子的长度最快，这就是 `next_fast_len(1009)`（1009 是素数）建议取 1024 的原因。

要估计采样信号的频率成分，我们对它做变换，再把输出换算成振幅。对于以采样率 $f_s$ 采样、持续时间为 $T$ 的信号，频率分辨率是 $1/T$，可表示的最大频率即 Nyquist 频率是 $f_s/2$：

```python
from scipy import fft

fs = 100.0                                        # samples per second
t = np.arange(0, 4, 1 / fs)                       # 4 seconds, N = 400
rng = np.random.default_rng(1)
signal = (np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 12 * t)
          + 0.8 * rng.standard_normal(t.size))
amplitude = 2 * np.abs(fft.rfft(signal)) / t.size  # one-sided amplitude spectrum
freq = fft.rfftfreq(t.size, d=1 / fs)              # 0, 0.25, ..., 50 Hz
```

![由 5 Hz 与 12 Hz 的正弦波组成的带噪声信号（左），以及用 rfft 算出的单边振幅谱，在 5 Hz 与 12 Hz 处有峰，振幅分别约为 1 与 0.5（右）](./plots/spectrum.py)

这两个分量在带噪声的信号中肉眼看不出来，却在谱中以高度约为 1 和 0.5 的峰凸显出来。由于 5 Hz 与 12 Hz 是分辨率 $0.25$ Hz 的整数倍，它们各自恰好落在一个输出上；一般地，位于两个输出之间的频率的能量会泄漏到相邻的输出中，在变换之前把信号乘以窗函数（`scipy.signal.windows`）可以减小这种泄漏。`scipy.signal.welch` 对重叠分段的谱取平均，给出更光滑的功率谱密度估计。卷积直接计算需要 $O(N^2)$，在频域中则变成逐点乘积；`scipy.signal.fftconvolve` 利用这一点，对长输入比 `np.convolve` 快得多。

## 小结

- SciPy 是建立在 NumPy 与成熟的编译库之上的一组子包；应导入子包（`from scipy import optimize`），并且优先使用 `scipy.linalg` 而不是 `numpy.linalg`。
- `optimize.minimize` 寻找局部极小点；按手头有什么（函数值、梯度、Hesse 矩阵）和约束选择方法，并尽可能提供梯度。标量方程用带括号的 `root_scalar`（`brentq`），**非线性回归**用 `curve_fit` 或 `least_squares`。
- `quad` 自适应地对函数积分并给出误差估计；`trapezoid` 与 `simpson` 对样本积分。
- `solve_ivp(fun(t, y), t_span, y0)` 以自适应步长求解初值问题；应明确设定容差，用 `dense_output` 或 `t_eval` 输出，用 `events` 定位穿越，刚性问题用隐式方法（`BDF`、`Radau`、`LSODA`）。
- 三次样条光滑但可能过冲；PCHIP 与修正的 Akima 保持单调性。`interp1d` 是遗留的。
- `scipy.stats` 的分布使用 `loc` 与 `scale`；检验返回含统计量、**p 值**以及常含**置信区间**的结果对象。
- 使用稀疏数组（`csr_array`）而不是稀疏矩阵；用 COO 组装，在 CSR 或 CSC 中计算；直接求解用 `spsolve`，迭代求解用 `cg` 或 `gmres`。
- FFT 以 $O(N \log N)$ 次运算计算离散 Fourier 变换；对实信号用 `rfft` 和 `rfftfreq`，并检查归一化的约定。
