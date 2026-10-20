---
title: NumPy：线性代数与随机数
description: 用 @、matmul、vecdot 计算矩阵乘积与成批数组；BLAS 与 LAPACK；numpy.linalg 中的线性方程组、最小二乘、矩阵分解与特征值；为什么不要求逆矩阵；einsum 与缩并顺序；随机数的 Generator 接口、分布的参数化、随机种子与并行随机数流；Monte Carlo 误差；循环与向量化代码的速度测量。
source_hash: 466ea6db1c01
---

本章讲解 NumPy 中仅次于基本数组运算、科学计算程序最常用的两个部分：稠密线性代数与随机数生成。两者中的 NumPy 都只是一层接口，背后是精心设计的编译代码：线性代数用 BLAS 与 LAPACK 库，随机数用现代伪随机数发生器。因此主要的技能是正确地调用它们：选对函数（解方程组用 solve 而不是求逆，对称矩阵用 `eigh` 而不是 `eig`），遵守接口的约定（形状、分布的参数化、设定种子），并知道能指望多高的精度。算法背后的理论不在这里重复，而见统计计算课程：浮点运算与条件数见 [3.5.1](/3.5.1)，数值线性代数见 [3.5.3](/3.5.3)，随机数生成见 [3.5.8](/3.5.8)。本章最后测量 Python 循环与向量化代码的速度差异，这解释了 [4.4.2](/4.4.2#sec-2.7) 所述的编程风格。示例使用 NumPy 2.5（2026 年 10 月）。

## 3.1. 矩阵乘积

### 3.1.1. @ 运算符

数组上的运算符 `*` 是逐元素乘法。**矩阵乘法**写作 `@`（PEP 465），它调用 `np.matmul`：

```python
import numpy as np

A = np.array([[1.0, 2.0], [3.0, 4.0]])
v = np.array([1.0, 1.0])
print(A @ A)        # [[ 7. 10.]  [15. 22.]]  matrix product
print(A * A)        # [[ 1.  4.]  [ 9. 16.]]  elementwise product
print(A @ v)        # [3. 7.]   matrix times vector
print(v @ A)        # [4. 6.]   vector times matrix
print(v @ v)        # 2.0       inner product
print(np.outer(v, v))   # [[1. 1.]  [1. 1.]]
```

一维数组既不是行向量也不是列向量（[4.4.2](/4.4.2#sec-2.4.1)）：在 `A @ v` 中它被当作列向量，在 `v @ A` 中被当作行向量，而 `v.T` 与原数组是同一个一维数组。需要区分时，我们使用形状为 `(n, 1)` 或 `(1, n)` 的二维数组。

`matmul` 也适用于成批的矩阵：对于形状为 `(..., m, k)` 和 `(..., k, n)` 的数组，它对最后两个轴上的矩阵做乘法，并对前面的轴做广播。这种批量运算在统计学（每组一个**协方差矩阵**）和机器学习中很常见。NumPy 2 又增加了一些同类的函数：

| 函数 | 对最后几个轴的运算 | 形状 |
|---|---|---|
| `a @ b`、`np.matmul(a, b)` | 矩阵乘积 | `(..., m, k) @ (..., k, n) -> (..., m, n)` |
| `np.vecdot(x, y)` | 向量的内积（对 `x` 取共轭） | `(..., n), (..., n) -> (...)` |
| `np.matvec(A, x)`、`np.vecmat(x, A)` | 矩阵与向量的乘积 | `(..., m, n), (..., n) -> (..., m)` |
| `a.mT`、`np.linalg.matrix_transpose(a)` | 最后两个轴的转置 | `(..., m, n) -> (..., n, m)` |
| `np.dot(a, b)` | 较老的函数；二维数组时是矩阵乘积，更高维时遵循另一条（很少用到的）规则 | |

```python
S = np.arange(24.0).reshape(2, 3, 4)
T = np.ones((2, 4, 5))
print((S @ T).shape, S.mT.shape)                  # (2, 3, 5) (2, 4, 3)
print(np.vecdot(np.ones((3, 4)), np.arange(4.0))) # [6. 6. 6.]: one inner product per row
```

类 `np.matrix`（其中 `*` 表示矩阵乘法）已被弃用，不应再使用；用普通数组加 `@` 即可取代它。

### 3.1.2. BLAS 与 LAPACK

NumPy 自己并不实现矩阵乘法，而是调用 BLAS（Basic Linear Algebra Subprograms）。这是一个在 20 世纪 70—80 年代定义的向量与矩阵运算的标准接口，各个处理器系列都有对应的优化实现。BLAS 分为三级：第 1 级是向量运算（内积、$y \leftarrow \alpha x + y$），在 $O(n)$ 的数据上做 $O(n)$ 的运算；第 2 级是矩阵与向量的运算，运算量为 $O(n^2)$；第 3 级是矩阵与矩阵的运算，在 $O(n^2)$ 的数据上做 $O(n^3)$ 的运算。只有第 3 级对每个从内存读入的字节执行许多次运算，所以只有它能接近处理器的峰值速度；这就是 [3.5.3](/3.5.3#sec-3.1.1) 中的算法要重新组织成分块、以使用矩阵乘积的原因。LAPACK（Linear Algebra PACKage）建立在 BLAS 之上，提供矩阵分解、线性方程组求解、最小二乘与特征值的例程；`numpy.linalg` 和 `scipy.linalg` 都是它的封装。

PyPI 上的 NumPy 与 SciPy 的 wheel 包内含 OpenBLAS；conda-forge 还提供 Intel MKL，在 Apple 处理器上 NumPy 可以使用 Apple 的 Accelerate 框架。`np.show_config()` 会显示正在使用哪个库。这些库是多线程的，线程数可以用环境变量限制，如 `OPENBLAS_NUM_THREADS=1` 或 `OMP_NUM_THREADS=1`，也可以在运行时用 threadpoolctl 包限制。当我们自己在更高的层次上并行时，例如同时运行许多进程（[4.4.7](/4.4.7)），就必须限制线程数，否则每个进程都会启动与核数一样多的 BLAS 线程。

编译的、分块的、向量化的实现与朴素实现之间的差距很大。在测试机器（配备 8 核 Intel 处理器的笔记本）上，两个 $2000 \times 2000$ 矩阵的乘积需要 $2n^3 = 1.6 \times 10^{10}$ 次**浮点运算**：

| 实现 | 时间 | 速度 |
|---|---|---|
| 纯 Python 三重循环（$n = 200$，浮点数列表） | 0.37 s | 0.04 GFLOP/s |
| `A @ B`，OpenBLAS，1 个线程 | 0.81 s | 20 GFLOP/s |
| `A @ B`，OpenBLAS，4 或 8 个线程 | 0.31 s | 52 GFLOP/s |

纯 Python 循环比单线程的 BLAS 慢约 500 倍，对 $n = 2000$ 需要约 6 分钟。另一方面，多线程只对大规模的第 3 级运算有帮助：对于长度为 $10^6$ 的两个向量的内积这类第 1 级运算，启动线程的开销超过收益，在测试机器上多线程的 `a @ a` 甚至比单线程的更慢。

## 3.2. numpy.linalg

### 3.2.1. 求解线性方程组

求解 $A\boldsymbol{x} = \boldsymbol{b}$ 时调用 `np.linalg.solve(A, b)`，它计算带**列主元**的 **LU 分解**（LAPACK 的 `gesv`），再求解两个三角方程组（[3.5.3](/3.5.3#sec-3.1.3)）。看似方便的 `np.linalg.inv(A) @ b` 应当避免：它的运算量约为前者的三倍，而且精度更低。

```python
from scipy.linalg import hilbert   # H[i, j] = 1 / (i + j + 1), a classic ill-conditioned matrix

for n in (6, 10, 13):
    H = hilbert(n)
    x_true = np.ones(n)
    b = H @ x_true
    x1 = np.linalg.solve(H, b)
    x2 = np.linalg.inv(H) @ b
    # condition number, relative errors, residual norms (see the table)
```

| $n$ | $\kappa_2(H)$ | `solve` 的误差 | `inv` 的误差 | 残差 $\Vert H\hat{\boldsymbol{x}} - \boldsymbol{b}\Vert$，`solve` | 残差，`inv` |
|---|---|---|---|---|---|
| 6 | $1.5 \times 10^{7}$ | $1.4 \times 10^{-10}$ | $5.3 \times 10^{-10}$ | $5.2 \times 10^{-16}$ | $2.6 \times 10^{-10}$ |
| 10 | $1.6 \times 10^{13}$ | $8.7 \times 10^{-5}$ | $2.8 \times 10^{-3}$ | $5.7 \times 10^{-16}$ | $4.8 \times 10^{-5}$ |
| 13 | $1.5 \times 10^{18}$ | $3.6$ | $3.0 \times 10^{2}$ | $4.8 \times 10^{-16}$ | $5.2$ |

这张表说明了 [3.5.1](/3.5.1#sec-1.4.4) 的两点教训。第一，解的相对误差大致是**条件数**乘以**机器精度**：对 $n = 13$，双精度下任何方法都无法恢复 $\boldsymbol{x}$，而 `np.linalg.cond(A)` 可以事先告诉我们这一点。第二，即使误差很大，`solve` 的残差仍保持在舍入误差的量级。这就是**后向稳定性**：算出的解是某个邻近方程组的精确解。显式求逆失去了这一性质，所以它的残差和误差都更大。对于 $2000 \times 2000$ 的方程组，在测试机器上 `solve` 用时 0.39 s，`inv(A) @ b` 用时 1.29 s。

同一个矩阵要配合许多右端项时，可以把它们作为矩阵 `B` 的各列一次传入（`np.linalg.solve(A, B)`），也可以只分解一次、再用 `scipy.linalg.lu_factor` 与 `lu_solve` 重复使用这个分解（[4.4.4](/4.4.4#sec-4.1)）。对于对称正定矩阵，例如协方差矩阵，**Cholesky 分解**的速度是 LU 分解的两倍，并且不选主元也是数值稳定的（`scipy.linalg.cho_factor`、`cho_solve`）。

### 3.2.2. 最小二乘

对于超定方程组 $A\boldsymbol{\beta} \approx \boldsymbol{y}$，其中 $A \in \mathbb{R}^{n \times p}$，$n > p$，**最小二乘法**的解使 $\Vert \boldsymbol{y} - A\boldsymbol{\beta} \Vert_2$ 最小。`np.linalg.lstsq(A, y)` 通过**奇异值分解**计算它，返回解、**残差平方和**、数值秩与奇异值。若改为构造**正规方程** $A^{\mathsf T}A\boldsymbol{\beta} = A^{\mathsf T}\boldsymbol{y}$，条件数会被平方（[3.5.3](/3.5.3#sec-3.2.8)）。在 $[0, 1]$ 上取 50 个等距点拟合 12 次多项式，可以清楚地看出两者的差别：

```python
x = np.linspace(0, 1, 50)
A = np.vander(x, 13, increasing=True)       # columns 1, x, ..., x^12
beta_true = np.ones(13)
y = A @ beta_true                           # exact data, no noise
b_ls, rss, rank, sv = np.linalg.lstsq(A, y)
b_ne = np.linalg.solve(A.T @ A, A.T @ y)
print(f"{np.linalg.cond(A):.1e} {np.linalg.cond(A.T @ A):.1e}")  # 6.8e+08 1.0e+18
print(f"{np.abs(b_ls - beta_true).max():.1e}")                  # 1.9e-08
print(f"{np.abs(b_ne - beta_true).max():.1e}")                  # 1.6e+00
```

对于无噪声的数据，`lstsq` 恢复系数的精度约为 8 位数字，与 $\kappa(A) \approx 7 \times 10^8$ 的预期一致；而正规方程的 $\kappa(A^{\mathsf T}A) \approx 10^{18}$，一位有效数字也无法恢复。实际中，多项式拟合还应避免使用单项式基：`np.polynomial.Polynomial.fit(x, y, deg)` 在拟合之前先把数据映射到区间 $[-1, 1]$，条件数因此大为改善，而 `numpy.polynomial` 包还提供 Chebyshev 基与 Legendre 基。较老的函数 `np.polyfit` 仍然可用，但新代码不再推荐使用。

### 3.2.3. 矩阵分解与特征值

`numpy.linalg` 的主要函数，以及 [3.5.3](/3.5.3) 中讲解相应算法的小节：

| 任务 | 函数 | 说明 |
|---|---|---|
| Cholesky 分解 $A = LL^{\mathsf T}$ | `cholesky(A)` | 返回下三角因子 $L$；若 $A$ 不是正定的，抛出 `LinAlgError`（[3.5.3](/3.5.3#sec-3.1.5)） |
| QR 分解 | `qr(A)` | 默认为简化形式：$Q$ 是 $n \times p$ 的（[3.5.3](/3.5.3#sec-3.2.3)） |
| 奇异值分解 $A = U\Sigma V^{\mathsf T}$ | `svd(A, full_matrices=False)` | 返回 $U$、作为一维数组的奇异值，以及 $V^{\mathsf T}$（不是 $V$）（[3.5.3](/3.5.3#sec-3.2.7)） |
| 对称 / Hermite 特征值问题 | `eigh(A)`、`eigvalsh(A)` | 实特征值按升序排列，特征向量标准正交 |
| 一般特征值问题 | `eig(A)`、`eigvals(A)` | 结果为复数；特征向量是第二个输出的各列（[3.5.3](/3.5.3#sec-3.3.3)） |
| 行列式 | `det(A)`、`slogdet(A)` | `slogdet` 返回符号与 $\log\lvert\det A\rvert$，避免上溢与下溢 |
| 范数、条件数、秩 | `norm(x, ord)`、`cond(A)`、`matrix_rank(A)` | `norm(A)` 是 Frobenius 范数，`norm(A, 2)` 是谱范数 |
| 伪逆 | `pinv(A)` | 通过奇异值分解计算 |

有几个细节容易被忽略：

- 对称矩阵一律使用 `eigh`。它更快，返回按升序排列的实特征值，特征向量精确地标准正交；而 `eig` 把矩阵当作一般矩阵处理，舍入可能使结果带有微小的虚部。自 NumPy 2.5 起，`eig` 与 `eigvals` 总是返回复数数组，即使特征值恰好全为实数；早期版本在可能时返回实数组，结果的 dtype 因此取决于数值本身。
- 数值计算中很少需要行列式本身。`np.linalg.det(0.1 * np.eye(500))` 返回 `0.0`，因为 $10^{-500}$ 下溢，而 `slogdet` 能正确返回对数 $-1151.29$。**多元正态分布**的对数似然需要 $\log\det\Sigma$，应当使用 `slogdet` 或 Cholesky 因子（$\log\det\Sigma = 2\sum_i \log L_{ii}$）。
- 所有函数都接受成批的矩阵：`A` 的形状为 `(k, n, n)` 时，`np.linalg.solve` 一次求解 $k$ 个方程组。

`scipy.linalg` 包含 `numpy.linalg` 的全部功能并有所扩充：可以访问因子的 LU 分解、三角方程组求解（`solve_triangular`）、Schur 与 QZ 分解、矩阵指数 `expm` 等矩阵函数，以及结构化矩阵（带状、Toeplitz、循环矩阵）的求解器。在能使用 SciPy 时，它通常是更好的选择（[4.4.4](/4.4.4#sec-4.1)）。

## 3.3. Einstein 求和

### 3.3.1. 记号

许多数组运算是对某些指标求乘积之和：矩阵乘积 $C_{ik} = \sum_j A_{ij}B_{jk}$，**迹** $\sum_i A_{ii}$，二次型 $\sum_{i,j} x_i A_{ij} x_j$。在源于物理学中张量分析的 Einstein 求和约定（Einstein summation convention）中，求和号被省略，出现两次的指标即对其求和。`np.einsum` 实现了这一约定的一个版本：用一个字符串列出每个操作数的指标，`->` 之后列出结果的指标；没有出现在结果中的指标被求和。

| 运算 | 公式 | `einsum` |
|---|---|---|
| 迹 | $\sum_i A_{ii}$ | `np.einsum("ii", A)` |
| 对角线 | $A_{ii}$ | `np.einsum("ii->i", A)` |
| 转置 | $A_{ji}$ | `np.einsum("ij->ji", A)` |
| 矩阵乘积 | $\sum_j A_{ij}B_{jk}$ | `np.einsum("ij,jk->ik", A, B)` |
| 批量矩阵乘积 | $\sum_j A_{bij}B_{bjk}$ | `np.einsum("bij,bjk->bik", A, B)` |
| 二次型 | $\sum_{i,j} x_i A_{ij} x_j$ | `np.einsum("i,ij,j", x, A, x)` |
| 逐行内积 | $\sum_j X_{ij}X_{ij}$ | `np.einsum("ij,ij->i", X, X)` |
| 叉积矩阵 $X^{\mathsf T}X$ | $\sum_n X_{ni}X_{nj}$ | `np.einsum("ni,nj->ij", X, X)` |

```python
A = np.arange(9.0).reshape(3, 3)
x = np.array([1.0, 2.0, 3.0])
print(np.einsum("ii", A), np.einsum("ii->i", A))   # 12.0 [0. 4. 8.]
print(np.einsum("i,ij,j", x, A, x), x @ A @ x)     # 192.0 192.0
X = np.arange(6.0).reshape(3, 2)
print(np.einsum("ij,ij->i", X, X))                 # [ 1. 13. 41.]: squared row norms
```

`einsum` 的价值在于它精确地说明了对哪些指标做缩并，因此论文中的公式很容易翻译成代码，也避免了一连串的转置与 reshape。对于已有专用函数的运算（`@`、`trace`、`sum`），专用函数通常至少一样快。

### 3.3.2. 缩并顺序

操作数多于两个时，缩并的顺序很重要，这与**动态规划**（[4.1.13](/4.1.13)）中的矩阵链乘法问题相同。对于形状为 $10 \times 100$、$100 \times 5$ 和 $5 \times 1000$ 的三个矩阵，计算 $(AB)C$ 约需 $10 \cdot 100 \cdot 5 + 10 \cdot 5 \cdot 1000 = 55\,000$ 次乘法，而 `einsum` 对 $j$ 和 $k$ 同时求和的朴素做法需要 $10 \cdot 100 \cdot 5 \cdot 1000 = 5 \times 10^6$ 次。使用 `optimize=True` 时，`einsum` 会搜索较好的顺序，并把成对的缩并交给 BLAS；`np.einsum_path` 可以显示这个计划：

```python
rng = np.random.default_rng(0)
a, b, c = rng.random((10, 100)), rng.random((100, 5)), rng.random((5, 1000))
path, info = np.einsum_path("ij,jk,kl->il", a, b, c, optimize="optimal")
print(path)    # ['einsum_path', (0, 1), (0, 1)]: first a with b, then the result with c
# info reports: Naive FLOP count 1.500e+07, Optimized FLOP count 1.100e+05
```

在测试机器上，`np.einsum("ij,jk,kl->il", a, b, c)` 不优化时用时 3.2 ms，使用 `optimize=True` 时为 0.04 ms。对于许多张量的缩并，opt_einsum 包提供了更精细的路径搜索。

## 3.4. 随机数

### 3.4.1. Generator 接口

计算机用**伪随机数发生器**（[3.5.8](/3.5.8#sec-8.1.1)）生成随机数：这是一种确定性的算法，其输出能通过随机性的统计检验，并且完全由初始状态即**随机种子**决定。NumPy 把它分成两层。位发生器（bit generator）产生随机比特流，默认的是 PCG64，一种带 128 位状态的置换**线性同余发生器**（[3.5.8](/3.5.8#sec-8.1.2)），它速度快、统计性质好，并支持相互独立的并行随机数流。[3.5.8](/3.5.8#sec-8.1.4) 的 Mersenne Twister 以 `MT19937` 的名字提供，用于兼容。`Generator` 再把这些比特变成服从各种分布的数。

自 NumPy 1.17 起推荐的接口，是由 `np.random.default_rng` 创建的 `Generator` 对象：

```python
rng = np.random.default_rng(12345)       # Generator(PCG64), seeded
print(rng.random(3))                     # uniform on [0, 1): [0.22733602 0.31675834 0.79736546]
print(rng.integers(1, 7, size=10))       # dice: integers from 1 to 6 (the upper bound is excluded)
print(rng.normal(loc=0.0, scale=2.0, size=3))
print(rng.choice(["A", "C", "G", "T"], size=12))   # random DNA sequence
print(rng.permutation(5))                # random permutation of 0, ..., 4
print(rng.choice(10, size=4, replace=False))       # sampling without replacement
```

较老的接口先调用 `np.random.seed(0)`，再使用 `np.random.rand` 或 `np.random.normal` 等函数，它使用一个隐藏的、基于 Mersenne Twister 的全局 `RandomState` 对象。保留它是为了向后兼容（它的随机数流是冻结的，不同版本之间永不改变），但新代码不应使用：全局状态意味着任何抽取随机数的库函数都会改变程序其他部分的随机数流，结果因此难以复现，也无法安全地并行。`Generator` 的方法使用的算法也更好（例如生成正态变量的 ziggurat 方法，比 [3.5.8](/3.5.8#sec-8.4.2) 的 **Box–Muller 方法**更快）。一个好的约定是，每个需要随机性的函数都接受一个 `rng` 参数：

```python
def bootstrap_means(data, n_boot, rng):
    idx = rng.integers(0, data.size, size=(n_boot, data.size))
    return data[idx].mean(axis=1)
```

### 3.4.2. 分布与参数化

`Generator` 提供约 35 种分布。它们的参数化遵循底层算法的约定，在某些地方与概率论课程的记号（本站的记号：速率为 $\lambda$ 的 $\mathrm{Exp}(\lambda)$，方差为 $\sigma^2$ 的 $\mathcal{N}(\mu, \sigma^2)$）不同。这些不一致是常见的出错来源：

| 分布 | 记号 | NumPy 调用 | 陷阱 |
|---|---|---|---|
| 均匀分布 | $\mathrm{U}(a, b)$ | `rng.uniform(a, b)` | |
| 正态分布 | $\mathcal{N}(\mu, \sigma^2)$ | `rng.normal(loc=mu, scale=sigma)` | `scale` 是标准差，不是方差 |
| 指数分布 | $\mathrm{Exp}(\lambda)$ | `rng.exponential(scale=1/lam)` | `scale` 是均值 $1/\lambda$，不是速率 |
| Gamma 分布 | $\Gamma(\alpha, \lambda)$ | `rng.gamma(shape=alpha, scale=1/lam)` | 是尺度，不是速率 |
| 二项分布 | $\mathrm{Bin}(n, p)$ | `rng.binomial(n, p)` | |
| Poisson 分布 | $\mathrm{Poi}(\lambda)$ | `rng.poisson(lam)` | |
| 几何分布 | $\mathrm{Geo}(p)$ | `rng.geometric(p)` | 取值 $1, 2, \dots$（直到首次成功的试验次数） |
| 负二项分布 | $\mathrm{NB}(r, p)$ | `rng.negative_binomial(r, p)` | 第 $r$ 次成功之前的失败次数 |
| 多元正态分布 | $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ | `rng.multivariate_normal(mu, Sigma)` | 是协方差矩阵，不是它的平方根 |
| 多项分布 | $\mathrm{Mult}(n, \boldsymbol{p})$ | `rng.multinomial(n, pvals)` | |

检验参数化是否正确，最好的办法是做一次快速的模拟：

```python
lam = 2.0
rng = np.random.default_rng(1)
print(rng.exponential(scale=1/lam, size=1_000_000).mean())    # 0.499..., the mean is 1/lambda
g = rng.gamma(shape=3.0, scale=1/lam, size=1_000_000)
print(g.mean(), g.var())                                       # about 1.5 and 0.75 = alpha/lambda^2
```

`scipy.stats`（[4.4.4](/4.4.4#sec-4.5)）也是如此，它处处使用 `loc` 与 `scale`。还要注意，`Generator` 的随机数流在 NumPy 的不同版本之间并不冻结：算法被改进或纠正时，同一个种子可能产生不同的数。例如 NumPy 2.5 纠正了 `Generator.binomial` 与 `multinomial` 算法中的一个错误。因此，要做到逐比特的可复现，需要把 NumPy 的版本与种子一起记录下来，锁文件就能做到这一点（[4.4.1](/4.4.1#sec-1.2.3)）。

### 3.4.3. 种子、可复现性与并行随机数流

设定了种子的发生器能精确地重现它的随机数流，这使模拟可以重复、错误可以复现：

```python
print(np.random.default_rng(2026).random() == np.random.default_rng(2026).random())   # True
```

不带种子的 `np.random.default_rng()` 从操作系统获取新的熵。为了使分析可复现，我们可以只做一次这样的调用，记录下这个值，之后用它设定种子：`np.random.SeedSequence().entropy` 返回这样一个 128 位整数。

并行模拟需要若干条互不重叠、互不相关的随机数流。给各个工作进程分别用 `0, 1, 2, ...` 作种子是常见的习惯；在 NumPy 的种子设定机制（对种子做哈希的 `SeedSequence`）下这样并不算错，但干净的做法是从同一个父发生器派生（spawn）出相互独立的子发生器：

```python
rng = np.random.default_rng(2026)
children = rng.spawn(3)                    # three independent Generators
print([int(g.integers(100)) for g in children])   # [62, 74, 8]
```

`np.random.SeedSequence(2026).spawn(3)` 在种子的层面做同样的事，便于传给工作进程。`Generator` 对象不加锁就不能在线程之间共享；给每个线程或进程各配一个子发生器，既正确又快速（[4.4.7](/4.4.7)）。

### 3.4.4. 例：Monte Carlo 估计

**蒙特卡洛方法**把某个量估计为随机样本的平均值。要估计 $\pi$，我们在单位正方形内均匀地抽取 $n$ 个点，统计落在四分之一圆盘 $x^2 + y^2 \le 1$ 内的比例，这个圆盘的面积是 $\pi/4$：

```python
def estimate_pi(n, rng):
    pts = rng.random((n, 2))
    return 4.0 * np.mean((pts ** 2).sum(axis=1) <= 1.0)


rng = np.random.default_rng(2026)
print([round(float(estimate_pi(n, rng)), 4) for n in (100, 10_000, 1_000_000)])
# [3.28, 3.1304, 3.142]
```

四分之一圆盘的示性函数是 $p = \pi/4$ 的 Bernoulli 变量，所以估计量 $4\bar X$ 的**标准差**为 $4\sqrt{p(1-p)/n} = \sqrt{\pi(4 - \pi)/n} \approx 1.64/\sqrt{n}$。由**中心极限定理**，误差近似服从以此为标准差的正态分布：要多得到一位小数，需要多 100 倍的样本。下图对每个 $n$ 给出 100 次独立的估计；它们的均方根误差与预测的直线一致。

![对每个点数 n 各做 100 次独立的 Monte Carlo 估计 pi，所得的绝对误差，以及均方根误差与理论标准误 sqrt(pi (4 - pi) / n)](./plots/monte-carlo-error.py)

收敛速度 $n^{-1/2}$ 与维数无关，这就是为什么**蒙特卡洛方法**是高维积分和统计学模拟研究的首选方法；在一维或二维的情形，同样的工作量下，确定性的数值积分（[4.4.4](/4.4.4#sec-4.3.1)）要精确得多。

## 3.5. 向量化与循环

### 3.5.1. 测量运行时间

关于速度的论断必须靠测量，而不是靠猜测。标准库模块 `timeit` 把一条语句运行许多次并报告总时间；测量期间它关闭**垃圾回收**，并使用最精确的时钟。在 IPython 和 Jupyter 中，`%timeit stmt` 自动完成这件事，并自行选择重复的次数：

```python
import timeit

x = np.random.default_rng(0).random(1_000_000)
t = min(timeit.repeat(lambda: (x * x).sum(), number=100, repeat=5)) / 100
print(f"{t * 1e3:.2f} ms per call")
```

有几条规则能使测量有意义：

- 重复测量并取最小值（或中位数），因为其他进程只会增加噪声，而不会使代码变快。
- 测量真实的规模：两种方法的相对速度往往取决于 $n$，如下图所示。
- 把准备工作（如创建输入数据）排除在计时的代码之外，除非它也是被比较的内容。
- 注意缓存与惰性求值：函数的第二次调用可能比第一次快得多（编译后的代码被缓存，数据进入了 CPU 缓存）。
- 对于整个程序，在代码块前后调用 `time.perf_counter()` 可以测得实际经过的时间；性能分析器（[4.4.7](/4.4.7)）则显示时间花在哪里。

### 3.5.2. 结果

我们比较计算 $\sum_i x_i^2$ 的三种方法：对列表的 Python `for` 循环、对生成器表达式使用内置的 `sum`，以及 NumPy 的 `(x * x).sum()`。

![平方和的运行时间随 n 的变化，比较 Python for 循环、对生成器使用 sum() 与 NumPy（左），以及每个元素的时间（右），在构建机器上测得](./plots/loop-vs-vectorized.py)

在测试机器（Python 3.14，NumPy 2.5）上的结果如下；图是在构建本站的机器上重新生成的，版本不同，所以数值会略有差异：

| $n$ | Python `for` 循环 | 对生成器使用 `sum` | NumPy `(x * x).sum()` |
|---|---|---|---|
| $10$ | 0.22 µs | 0.37 µs | 0.69 µs |
| $10^3$ | 16 µs | 22 µs | 1.2 µs |
| $10^6$ | 24 ms | 23 ms | 1.1 ms |

### 3.5.3. 差异的原因

一个简单的模型可以解释这张图：对 $n$ 个元素的运算，时间约为 $a + bn$，其中 $a$ 是固定的开销，$b$ 是每个元素的代价。

- 对于 Python 循环，$a$ 很小，但 $b$ 约为 20 ns：每次迭代执行若干条**字节码**指令，每个 `v * v` 与 `s += ...` 都要根据操作数的类型分派（**动态类型**），每个中间结果都是新分配的 float 对象，之后由**引用计数**释放。生成器表达式还要为每个元素增加恢复生成器的开销。
- 对于 NumPy，$a$ 约为 1 µs：解析参数、确定 dtype、为 `x * x` 的结果分配数组。但 $b$ 约为 1 ns，因为编译后的循环直接处理原始的 `float64` 数值，使用一条指令处理多个元素的 SIMD 指令，并顺序地读取内存。

因此，NumPy 在很小的数组（少于几十个元素）上落后，在大数组上快约 20 倍。由此得到几条设计数值 Python 代码的指导原则：

- 对大数组上最内层、执行最频繁的循环做向量化；围绕向量化运算的 60 次 Python 循环（如 [4.4.2](/4.4.2#sec-2.6.2) 的 Mandelbrot 例子）几乎没有代价。
- 不要在很长的 Python 循环里对微小的运算做向量化：对 3 个元素的数组调用一百万次 NumPy，比直接用 Python 做算术更慢。应当重组计算，使循环在 NumPy 内部沿大的维度进行，或者把循环编译（[4.4.7](/4.4.7)）。
- 临时数组消耗内存带宽：`(x * x).sum()` 要写入并读取一个大小为 $n$ 的中间数组；`x @ x` 或 `np.einsum("i,i", x, x)` 可以避免它，而通用函数的 `out` 参数（[4.4.2](/4.4.2#sec-2.5.1)）可以重用已有的内存。
- 最大的收益来自算法而不是实现：§3.1.2 的矩阵乘积在 BLAS 中比在 Python 中快 500 倍，而 [4.4.2](/4.4.2#sec-2.7) 的随机游走例子通过更好的表述又快了一百倍。

## 小结

- `@` 是矩阵乘法，`*` 是逐元素乘法；`matmul`、`vecdot`、`matvec` 与 `.mT` 适用于成批的矩阵。一维数组既不是行向量也不是列向量。
- 稠密线性代数在 BLAS 与 LAPACK 中运行；只有矩阵与矩阵的运算能达到很高的速度，在更高层次上并行时应当限制 BLAS 的线程数。
- 求解线性方程组用 `solve`（或可重复使用的矩阵分解），绝不用 `inv`；用 `lstsq` 或 QR 分解代替正规方程；对称矩阵用 `eigh`，用 `slogdet` 代替 `det`。**条件数**预示了能达到的精度。
- `einsum` 用指标字符串表示乘积之和；`optimize=True` 选择缩并顺序。
- 用 `np.random.default_rng(seed)` 创建一个 `Generator`，并把它传给每个需要随机性的函数；检查参数化（尺度与速率，标准差与方差）；为并行的随机数流派生子发生器；要精确复现，须记录 NumPy 的版本。
- Monte Carlo 误差按 $n^{-1/2}$ 的速度下降。
- 用 `timeit` 测量；运算的时间大致是开销加每个元素的代价，这解释了何时值得做**向量化**。
