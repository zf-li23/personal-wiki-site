---
title: NumPy：数组与向量化
description: 为什么 Python 列表不适合存放数值数据；ndarray 与 dtype；NumPy 2 中的类型提升；内存布局、步长与连续性；基本索引与视图；花式索引与布尔索引；通用函数、归约与成对求和；广播；以整个数组为单位思考；NumPy 与其他数组库（数组 API 标准、DLPack）。
source_hash: a5fc3aff82d4
---

NumPy 是科学计算 Python 栈的基础（[4.4.1](/4.4.1#sec-1.1.2)）：它提供一种数据结构，即 N 维数组，以及对整个数组的快速运算。生态系统中的其他一切，从 SciPy 到 pandas 和 scikit-learn，都以 NumPy 数组的形式交换数据。本章讲解数组在内存中是什么样子，因为 NumPy 中几乎所有令人意外的现象（赋值改变了另一个变量、某个运算出乎意料地慢、整数悄悄溢出）都源于内存模型。随后研究使 NumPy 快速的运算：通用函数、归约与广播，以及它们所支持的编程风格，即**向量化**。本章延续 [4.1.8](/4.1.8#sec-8.2.3) 对内存布局的讨论以及 [4.1.8](/4.1.8#sec-8.5) 对 Python 引用语义的讨论。线性代数与随机数见 [4.4.3](/4.4.3)。示例使用 NumPy 2.5（2026 年 10 月）；除少数注明的细节外，所述内容对 NumPy 2.0 及以后的版本同样成立。

## 2.1. 为什么需要 NumPy

Python 的数值列表是由引用构成的**数组**，每个引用指向堆上某处一个独立的 float 对象（[4.1.8](/4.1.8#sec-8.5)）。每个 float 对象除了 8 字节的数值外，还存储一个引用计数和一个指向其类型的**指针**，因此占 24 字节，而列表为每个元素再增加一个 8 字节的指针：

```python
import sys
import numpy as np

n = 1_000_000
lst = [float(i) for i in range(n)]
arr = np.arange(n, dtype=np.float64)
print(sys.getsizeof(lst) + sum(sys.getsizeof(v) for v in lst))  # 32448728 bytes
print(arr.nbytes)                                                # 8000000 bytes
```

NumPy 数组把同样的数存成一块连续的原始 8 字节数值，小了四倍。更重要的是，由于所有元素类型相同且彼此相邻，对整个数组的运算可以作为一个编译好的循环运行：不必逐元素检查类型，不必分配对象，内存访问是顺序的，CPU 缓存和 SIMD 指令能很好地处理。在测试机器上，对 $10^6$ 个数计算 $\sum_i x_i^2$，用 Python 的 `for` 循环遍历列表约需 20 ms，而 `(arr * arr).sum()` 约需 1 ms；系统的比较见 [4.4.3](/4.4.3#sec-3.5)。

代价是灵活性：数组大小固定，且只有一种元素类型。因此 NumPy 是同质数值数据（向量、矩阵、图像、时间序列、网格）的合适容器，而 Python 列表仍然是小型的、会增长的异质集合的合适容器（[4.2.10](/4.2.10)）。

## 2.2. ndarray

### 2.2.1. 创建数组

**定义 2.2.1（N 维数组）** **N 维数组**（`ndarray`）是由同一类型的元素构成的、大小固定的多维容器。它由一块内存，即数据缓冲区（data buffer），以及说明如何解释这块内存的元数据组成：元素类型（dtype）、形状（shape，一个给出各维长度的元组），以及步长（§2.3）。各维称为轴（axis），编号为 $0, 1, \dots, d - 1$；$d$ 是维数 `ndim`。

最常用的创建数组的方法有：

| 函数 | 结果 |
|---|---|
| `np.array([[1, 2], [3, 4]])` | 由嵌套序列创建；dtype 由内容推断 |
| `np.zeros((m, n))`、`np.ones(...)`、`np.full(shape, v)` | 以 0、1 或 `v` 填充（默认 float64） |
| `np.empty((m, n))` | 未初始化的内存：最快，但写入之前的值是任意的 |
| `np.arange(start, stop, step)` | 等间隔的值，不含 `stop`（与 `range` 相同） |
| `np.linspace(a, b, n)` | 从 `a` 到 `b`（含两端）的 `n` 个等间隔值 |
| `np.eye(n)`、`np.diag(v)` | 单位矩阵、对角矩阵 |
| `np.zeros_like(a)`、`np.empty_like(a)` | 与 `a` 形状和 dtype 相同 |
| `np.loadtxt`、`np.genfromtxt`、`np.load` | 从文本文件或 NumPy 的二进制 `.npy` 格式读取 |

对于浮点数范围，`np.linspace` 比 `np.arange` 更可取：步长为小数时，舍入可能使 `np.arange` 意外地包含或排除端点，而 `linspace` 固定了点的个数。

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.ndim, a.shape, a.size, a.dtype, a.itemsize, a.nbytes)  # 2 (2, 3) 6 int64 8 48
print(np.arange(0, 1, 0.25))   # [0.   0.25 0.5  0.75]
print(np.linspace(0, 1, 5))    # [0.   0.25 0.5  0.75 1.  ]
```

### 2.2.2. 轴

许多函数接受 `axis` 参数，指明沿哪个轴运算；该轴会从结果中消失。对矩阵而言，`axis=0` 沿行的方向向下，每列给出一个值，`axis=1` 沿每一行进行：

```python
print(a.sum(axis=0))   # [5 7 9]   column sums
print(a.sum(axis=1))   # [ 6 15]   row sums
print(a.sum())         # 21        all elements
print(a.sum(axis=1, keepdims=True).shape)   # (2, 1): the axis is kept with length 1
```

`keepdims=True` 把被归约的轴以长度 1 保留下来，使结果可以通过广播与原数组组合（§2.6）。数据分析中一个有用的约定是把观测沿轴 0 存放、变量沿轴 1 存放，这样含 $n$ 个观测、$p$ 个变量的**数据矩阵**形状为 `(n, p)`，与统计学教材一致。

### 2.2.3. dtype

**定义 2.2.2（dtype 对象）** 数组的 **dtype 对象**（数据类型）描述每个元素如何存储：它的种类（布尔、有符号或无符号整数、浮点、复数、字符串或 Python 对象）、字节数以及字节序。

| dtype | 大小 | 范围或精度 | 说明 |
|---|---|---|---|
| `bool` | 1 字节 | `True`、`False` | 比较运算的结果 |
| `int8`、`int16`、`int32`、`int64` | 1–8 字节 | $-2^{k-1}$ 到 $2^{k-1} - 1$ | `int64` 是 64 位 Linux、macOS 以及（自 NumPy 2 起）Windows 上的默认整数 |
| `uint8`、...、`uint64` | 1–8 字节 | $0$ 到 $2^k - 1$ | `uint8` 用于图像像素 |
| `float32` | 4 字节 | 约 7 位有效数字 | 单精度，用于 GPU 与机器学习 |
| `float64` | 8 字节 | 约 16 位有效数字 | 默认类型；IEEE 754 双精度 |
| `complex128` | 16 字节 | 两个 `float64` | |
| `StringDType()`、`<U10` | 可变 / 固定 | | 文本；`<U10` 至多容纳 10 个字符 |
| `object` | 8 字节 | 指向 Python 对象的引用 | 失去全部速度优势 |

NumPy 的整数类型是 C 的定宽整数，而不是 Python 的无界整数（[4.1.2](/4.1.2#sec-2.2.2)），因此数组的算术运算在**整数溢出**时会悄悄回绕：

```python
x = np.array([100, 120], dtype=np.int8)
print(x + x)                              # [-56 -16], no warning
print(np.iinfo(np.int8).max)              # 127
print(np.finfo(np.float32).eps, np.finfo(np.float64).eps)   # 1.1920929e-07 2.220446049250313e-16
```

`np.finfo` 给出浮点类型的**机器精度**与取值范围（[3.5.1](/3.5.1#sec-1.2.5)）。**溢出**在实践中是真实的危险：以 `uint8` 存储的图像在两个像素值相加时会回绕，大的 `int32` 计数的乘积很快就会溢出。运算之前用 `a.astype(np.float64)` 转换可以避免这两种情形。

当一个运算组合不同 dtype 的数组时，NumPy 按类型提升（type promotion）选择结果的 dtype：即能表示两个操作数的最小类型，所以 `int8 + int16` 得到 `int16`，`int64 + float64` 得到 `float64`。NumPy 2 改变了 Python 标量的规则（NEP 50）。Python 的 `int`、`float` 或 `complex` 现在是“弱”的：它采用与之组合的数组的 dtype，而不是依其数值影响结果类型。

```python
print(np.array([1, 2], dtype=np.float32) * 2.5)   # [2.5 5. ], still float32
print((np.array([1, 2], dtype=np.int8) + 1).dtype)  # int8
np.array([1, 2], dtype=np.int8) + 1000
# OverflowError: Python integer 1000 out of bounds for int8
print(np.float32(0.1) + 0.2)                       # 0.3, a float32
print(np.array([1, 2, 3]) / 2)                     # [0.5 1.  1.5]: true division gives float64
```

这一规则使结果可预测，代价是 `float32` 数据与 Python 浮点数组合时仍保持**单精度**。在精度要紧的场合，应显式转换。

## 2.3. 内存布局与步长

### 2.3.1. 步长

数组有形状，而内存是一维的。两者靠步长联系起来。

**定义 2.3.1（步长）** 数组的**步长**是一个整数元组 $(s_0, \dots, s_{d-1})$：$s_k$ 是沿轴 $k$ 的下标增加 1 时内存地址前进的字节数。下标为 $(i_0, \dots, i_{d-1})$ 的元素存放在距数组起点

$$
i_0 s_0 + i_1 s_1 + \cdots + i_{d-1} s_{d-1}
$$

字节的偏移处。

NumPy 创建的 $3 \times 4$ 的 `float64` 数组按**行主序**存储（称为 C 序，C 与 C++ 即如此，[4.1.8](/4.1.8#sec-8.2.3)）：同一行的相邻元素在内存中相邻，所以步长是 `(32, 8)`，即到下一行为 32 字节，到下一列为 8 字节。Fortran、MATLAB、R 和 Julia 按列主序（column-major order）存储矩阵（也称 Fortran 序），同样形状的步长为 `(8, 24)`。NumPy 两种都支持，而步长使许多运算无需代价：它们只改变元数据，从不改变数据缓冲区。

```python
b = np.arange(12, dtype=np.float64).reshape(3, 4)
print(b.strides)                    # (32, 8)
print(b.T.strides)                  # (8, 32): transposing swaps the strides
print(b[:, ::2].strides)            # (32, 16): every other column
print(b[::2].strides)               # (64, 8): every other row
print(np.asfortranarray(b).strides) # (8, 24): a copy in column-major order
```

C++ 中同样的想法是跨步视图（strided view）：指向已有数据的指针加上形状和步长，通过它可以用不同的模式读取数据而无需复制。C++23 把它标准化为 `std::mdspan`。下面的最小版本说明，NumPy 的转置和切片不过是对步长的算术运算：

```cpp tab
#include <cstddef>
#include <iostream>
#include <numeric>
#include <vector>

// A minimal 2-D strided view: a pointer to the data plus shape and strides
// (measured in elements here; NumPy measures strides in bytes).
struct View2D {
    double* data;
    std::ptrdiff_t shape[2];
    std::ptrdiff_t strides[2];
    double& operator()(std::ptrdiff_t i, std::ptrdiff_t j) const {
        return data[i * strides[0] + j * strides[1]];
    }
    View2D transposed() const {
        return {data, {shape[1], shape[0]}, {strides[1], strides[0]}};
    }
};

int main() {
    std::vector<double> buf(12);
    std::iota(buf.begin(), buf.end(), 0.0);  // 0, 1, ..., 11
    View2D a{buf.data(), {3, 4}, {4, 1}};    // 3 x 4, row-major
    View2D t = a.transposed();                // 4 x 3, no data copied
    View2D every_other{buf.data(), {3, 2}, {4, 2}};  // a[:, ::2]
    t(1, 2) = -1.0;                           // writes buf[2 * 4 + 1]
    std::cout << a(2, 1) << ' ' << every_other(1, 1) << '\n';  // -1 6
}
```

```python tab
import numpy as np

a = np.arange(12.0).reshape(3, 4)   # 3 x 4, row-major
t = a.T                             # 4 x 3, no data copied
t[1, 2] = -1.0                      # writes the element a[2, 1]
print(a[2, 1], a[:, ::2][1, 1])     # -1.0 6.0
print(a.strides, t.strides, a[:, ::2].strides)  # (32, 8) (8, 32) (32, 16)
```

### 2.3.2. 连续性与性能

如果数组的元素按**行主序**占据一整块内存，则称它是 C 连续的（C-contiguous）；如果按列主序占据，则称它是 F 连续的（F-contiguous）；`a.flags` 同时报告这两者。上面的 `b` 是 C 连续的，`b.T` 是 F 连续的，而 `b[:, ::2]` 两者都不是。

步长不改变运算的次数，但改变速度。内存以 64 字节的缓存行为单位传送到 CPU 缓存；沿最后一个轴（C 序下）遍历数组会用到每个缓存行的每个字节，而沿第一个轴遍历只用到每个缓存行的 8 字节，然后就要跳到别处。在测试机器上，对 $4000 \times 4000$ 的 `float64` 数组（128 MB）：

| 运算 | 时间 |
|---|---|
| 对每行求和，`[a[i, :].sum() for i in range(4000)]` | 20 ms |
| 对每列求和，`[a[:, j].sum() for j in range(4000)]` | 168 ms |
| `a.copy()` | 43 ms |
| `np.ascontiguousarray(a.T)`（转置并复制） | 220 ms |

诸如 `a.sum(axis=0)` 这样对整个数组的归约，其写法使它无论沿哪个轴都能高效地遍历内存，所以这一影响主要出现在我们自己对切片做循环、或把数组传给要求特定布局的编译代码时。一些库（以及通过它们调用的 C 或 Fortran 例程）要求输入是连续的，否则会悄悄复制；`np.ascontiguousarray` 把这次复制显式地表示出来。

## 2.4. 索引、视图与副本

### 2.4.1. 基本索引与切片

多维数组的索引每个轴一个下标，以逗号分隔：写 `m[i, j]`，而不是 `m[i][j]`（后者可行，但会创建中间数组）。每个下标可以是整数，这会去掉该轴；也可以是切片 `start:stop:step`，这会保留该轴。负下标从末尾数起，`...`（Ellipsis）代表所需数量的完整切片，`np.newaxis`（等于 `None`）插入一个长度为 1 的新轴：

```python
m = np.arange(12).reshape(3, 4)
print(m[1, 2])        # 6
print(m[1])           # [4 5 6 7]     row 1 (same as m[1, :])
print(m[:, 1])        # [1 5 9]       column 1, as a 1-D array
print(m[-1, ::-1])    # [11 10  9  8] last row reversed
print(m[..., 0])      # [0 4 8]       first entry along the last axis
print(m[:, None].shape)   # (3, 1, 4)
```

注意 `m[:, 1]` 是形状为 `(3,)` 的一维数组，而不是形状为 `(3, 1)` 的列；一维数组既不是行向量也不是列向量。要保持列的形状，写 `m[:, 1:2]` 或 `m[:, [1]]`。

### 2.4.2. 视图

**定义 2.4.1（视图）** 数组的**视图**是另一个与之共享数据缓冲区的数组对象，有自己的形状、步长和偏移。向视图写入会改变原数组，反之亦然。拥有缓冲区的数组可以通过视图的属性 `base` 得到。

基本切片、转置、`reshape`（在可能时）与 `np.newaxis` 返回视图，因为它们都可以用新的步长和偏移来表示（§2.3）。这与 Python 列表相反，列表的切片创建的是**浅拷贝**：

```python
a = np.arange(10)
s = a[2:8:2]          # a view: elements 2, 4, 6
s[0] = -1
print(a)              # [ 0  1 -1  3  4  5  6  7  8  9]
print(s.base is a, np.shares_memory(a, s))   # True True

lst = list(range(5))
t = lst[1:3]          # a new list
t[0] = 99
print(lst)            # [0, 1, 2, 3, 4], unchanged
```

视图使切片代价很小（无论多大都不复制数据），并允许原地更新数组的一部分，例如 `img[100:200, 50:150] = 0`。它们也是最常见的错误来源：接收切片并修改它的函数，修改的是调用者的数据。需要独立的数组时，用 `.copy()` 显式复制。一个运算返回的是视图还是副本，可以用 `np.shares_memory` 检查：

```python
m = np.arange(12).reshape(3, 4)
print(np.shares_memory(m, m.reshape(4, 3)))     # True: reshaping a contiguous array
print(np.shares_memory(m, m.T.reshape(12)))     # False: m.T is not contiguous, so reshape copies
print(np.shares_memory(m, m[:, 1:3].copy()))    # False
```

`np.asarray(x)` 在 `x` 已经是所要求 dtype 的数组时直接返回 `x` 本身，只在必要时复制，接受“类数组”输入的函数应当使用它。自 NumPy 2 起，`np.array(x, copy=False)` 的意思是“绝不复制”，在无法避免复制时抛出 `ValueError`；为 NumPy 1 写的代码中它的意思是“仅在需要时复制”，这样的代码应改用 `np.asarray`。

### 2.4.3. 花式索引与布尔索引

用整数数组或列表、或用布尔数组做索引，称为高级索引。

**定义 2.4.2（花式索引）** **花式索引**（又称整数数组索引）通过下标数组选取元素：`x[idx]` 是元素为 `x[idx[k]]` 的数组。**布尔索引** `x[mask]` 使用与 `x` 形状相同的布尔数组 `mask`，以一维数组的形式选取 `mask` 为 `True` 的元素。两者总是返回副本。

```python
x = np.array([10, 20, 30, 40, 50])
y = x[np.array([4, 0, 0])]     # indices may repeat and appear in any order
y[0] = 0
print(x, y)                    # [10 20 30 40 50] [ 0 10 10]: y is a copy
mask = x > 25
print(mask, x[mask])           # [False False  True  True  True] [30 40 50]
x[x > 25] = 0                  # assignment through an index works in place
print(x)                       # [10 20  0  0  0]
```

高级索引的结果是副本，但对高级索引*赋值*（`x[mask] = 0`）会写入 `x`。由此产生经典的链式索引错误：`x[[1, 3]][0] = -5` 先用 `x[[1, 3]]` 生成一个副本，再修改这个副本，因此 `x` 不变。应改写成单个索引表达式，例如 `x[1] = -5`。

当有多个整数数组时，这些数组是逐元素配对的，而不是组合成网格：`m[[0, 2], [1, 3]]` 给出 `m[0, 1]` 和 `m[2, 3]` 两个元素。第 0、2 行与第 1、3 列构成的子矩阵是 `m[np.ix_([0, 2], [1, 3])]`。函数 `np.nonzero(mask)` 返回 `True` 元素的下标数组，`np.where(cond, a, b)` 在两个数组之间逐元素选择：

```python
print(m[[0, 2], [1, 3]])                 # [ 1 11]
print(m[np.ix_([0, 2], [1, 3])])         # [[ 1  3]
                                         #  [ 9 11]]
print(np.where(m > 5, m, 0))             # entries <= 5 replaced by 0
```

下表总结何时得到视图：

| 运算 | 视图还是副本 |
|---|---|
| `a[2:8]`、`a[:, 1]`、`a[::2, ::-1]`、`a[..., None]` | 视图 |
| `a.T`、`a.transpose(...)`、`a.swapaxes(...)` | 视图 |
| `a.reshape(...)`、`a.ravel()` | 布局允许时为视图，否则为副本 |
| `a[[1, 3]]`、`a[a > 0]` | 副本 |
| `a.flatten()`、`a.copy()`、`a.astype(...)` | 副本 |
| 算术运算 `a + 1`、`np.sin(a)` | 新数组 |

## 2.5. 通用函数

### 2.5.1. 逐元素运算

**定义 2.5.1（通用函数）** **通用函数**（简称 ufunc）是逐元素作用于数组的函数，对每种受支持的 dtype 组合都实现为一个编译好的循环。它支持广播（§2.6）、类型提升、把结果写入已有数组的 `out` 参数，以及只计算选定元素的 `where` 参数。

数组上的算术运算符都是通用函数：`a + b` 调用 `np.add(a, b)`，`a * b` 调用 `np.multiply`，`a < b` 调用 `np.less`，等等。NumPy 有大约一百个通用函数（含别名），涵盖算术（`add`、`subtract`、`multiply`、`divide`、`floor_divide`、`power`、`mod`）、比较、逻辑（`logical_and`、`logical_not`）以及数学函数（`exp`、`log`、`log1p`、`expm1`、`sqrt`、`sin`、`arctan2`、`hypot`、`abs`、`maximum`、`isnan`、`isfinite`）。函数 `log1p` 与 `expm1` 对小的 $x$ 能精确地计算 $\log(1 + x)$ 与 $\mathrm{e}^x - 1$，避免了**灾难性抵消**（[3.5.1](/3.5.1#sec-1.3.3)）。

```python
print(np.add(1, [1, 2]))                      # [2 3]
out = np.empty(3)
np.exp([0, 1, 2], out=out)                    # no new array is allocated
print(out)                                    # [1.         2.71828183 7.3890561 ]
print(isinstance(np.sin, np.ufunc), np.add.nin)   # True 2
```

浮点异常不会引发错误。按照 IEEE 754，除以零得到 `inf` 或 `nan`（**非数**），并给出 `RuntimeWarning`；**上下文管理器** `np.errstate` 可以局部地改变这种行为，例如消除警告或抛出异常：

```python
with np.errstate(divide="ignore", invalid="ignore"):
    print(np.array([1.0, 0.0, -1.0]) / 0.0)   # [ inf  nan -inf]
with np.errstate(all="raise"):
    np.log(np.array([0.0]))                   # FloatingPointError: divide by zero encountered in log
```

### 2.5.2. 归约与累积

二元通用函数有一些方法，可以重复地施加该运算：

| 方法 | 例子 | 结果 |
|---|---|---|
| `reduce` | `np.add.reduce([1, 2, 3, 4])` | `10`（与 `np.sum` 相同） |
| `accumulate` | `np.add.accumulate([1, 2, 3, 4])` | `[1 3 6 10]`（与 `np.cumsum` 相同） |
| `outer` | `np.multiply.outer([1, 2, 3], [1, 10])` | $3 \times 2$ 的乘积表 |
| `at` | `np.add.at(c, idx, 1)` | 无缓冲的原地运算，对重复下标也正确 |

常用的归约有各自的函数和方法：`sum`、`prod`、`mean`、`std`、`var`、`min`、`max`、`argmin`、`argmax`、`any`、`all`、`cumsum`，它们都带 `axis` 参数。注意 `np.std` 和 `np.var` 默认除以 $n$；除数为 $n - 1$ 的无偏**样本方差**需要 `ddof=1`。`np.nanmean` 与 `np.nansum` 等函数忽略 `nan` 元素。

方法 `at` 解决了一个微妙的问题。在 `c[idx] += 1` 中，NumPy 先计算 `c[idx] + 1` 再赋值，所以在 `idx` 中出现多次的下标只增加一次：

```python
idx = np.array([0, 1, 1, 2, 1])
c = np.zeros(3, dtype=int); c[idx] += 1;          print(c)   # [1 1 1]
c = np.zeros(3, dtype=int); np.add.at(c, idx, 1); print(c)   # [1 3 1]
print(np.bincount(idx))                                       # [1 3 1]
```

对于计数，`np.bincount` 是最快的解法；`np.add.at` 是通用的解法（例如用于由单元贡献组装矩阵）。

**浮点数**求和不是精确的，且顺序有影响（[3.5.1](/3.5.1#sec-1.3.3)）。朴素的循环累积的**舍入误差**可以与 $n\varepsilon$ 成比例地增长。对浮点数据，`np.sum` 使用成对求和（pairwise summation）：把数组递归地分成两半（小块直接求和），这把误差界降到 $\varepsilon \log n$ 量级，而没有额外的代价。对于少数需要正确舍入的和，标准库提供 `math.fsum`。

## 2.6. 广播

### 2.6.1. 广播规则

数组与标量之间的算术运算 `a * 2.5` 把每个元素都乘以 2.5。广播把这一点推广到形状不同的数组。

**定义 2.6.1（广播）** **广播**是 NumPy 在逐元素运算中组合不同形状数组的规则。先在较短的形状左侧补 1，然后从最后一个轴向前逐个比较；两个长度相容，当且仅当它们相等或其中之一为 1。结果沿每个轴取两个长度中较大的一个，沿某个轴长度为 1 的操作数在该轴上被重复使用。如果有某一对长度不相容，运算失败。

| `a` 的形状 | `b` 的形状 | `a + b` 的形状 |
|---|---|---|
| `(3, 4)` | `()`（标量） | `(3, 4)` |
| `(3, 4)` | `(4,)` | `(3, 4)`：`b` 加到每一行 |
| `(3, 4)` | `(3, 1)` | `(3, 4)`：`b` 加到每一列 |
| `(3,)` | `(4, 1)` | `(4, 3)`：外和 |
| `(8, 1, 6, 1)` | `(7, 1, 5)` | `(8, 7, 6, 5)` |
| `(3, 2)` | `(3,)` | 错误：2 与 3 不相容 |

广播并不复制被重复的操作数：在内部，它是沿广播轴步长为 0 的视图。`np.broadcast_to(np.arange(3), (4, 3))` 的步长是 `(0, 8)` 且只读，因为它的 12 个元素共享 3 个内存位置。

```python
x = np.arange(3)                 # shape (3,)
y = np.arange(4).reshape(4, 1)   # shape (4, 1)
print(x + y)                     # shape (4, 3): entry (i, j) is y[i] + x[j]
# [[0 1 2]
#  [1 2 3]
#  [2 3 4]
#  [3 4 5]]
np.ones((3, 2)) + np.ones(3)
# ValueError: operands could not be broadcast together with shapes (3,2) (3,)
print((np.ones((3, 2)) + np.ones(3)[:, None]).shape)   # (3, 2)
```

最后一个例子给出典型的修正办法：要把长度为 3 的向量与 $3 \times 2$ 数组的各行组合，我们用 `[:, None]` 把它变成列，使末尾的轴对齐。

### 2.6.2. 例子

*数据矩阵各列的标准化。* 观测沿轴 0 时，`X.mean(axis=0)` 的形状为 `(p,)`，可以与形状为 `(n, p)` 的 `X` 广播：

```python
X = np.array([[1.0, 2.0], [3.0, 6.0], [5.0, 10.0]])
Z = (X - X.mean(axis=0)) / X.std(axis=0, ddof=1)
print(Z)
# [[-1. -1.]
#  [ 0.  0.]
#  [ 1.  1.]]
```

若改为对各行标准化，则需要 `keepdims=True`（或 `[:, None]`），使行统计量的形状为 `(n, 1)`。

*成对距离。* 对 $\mathbb{R}^d$ 中的点 $p_1, \dots, p_m$ 和 $q_1, \dots, q_k$，分别存为形状 `(m, d)` 的数组 `P` 和形状 `(k, d)` 的数组 `Q`，插入轴后形状变为 `(m, 1, d)` 和 `(1, k, d)`，它们的差的形状为 `(m, k, d)`：

```python
rng = np.random.default_rng(0)
P, Q = rng.random((5, 2)), rng.random((3, 2))
D = np.sqrt(((P[:, None, :] - Q[None, :, :]) ** 2).sum(axis=-1))
print(D.shape)     # (5, 3): D[i, j] is the distance from P[i] to Q[j]
```

中间数组有 $m k d$ 个元素。当 $m = k = 10^4$、$d = 3$ 时，这是 2.4 GB，所以对大的问题，`scipy.spatial.distance.cdist` 这样的专用函数或分块循环更可取。广播以内存换取速度；它并非没有代价。

*在网格上计算函数。* `x[None, :]` 与 `y[:, None]` 广播成二维网格，这在多数情形下可以代替 `np.meshgrid`。下图就是这样计算的：网格上的**复数** $c$ 按 $z \mapsto z^2 + c$ 迭代，用一个布尔数组记录尚未逃逸的点，于是整幅图只需对 60 次迭代做一个 Python 循环，而不是对 648 000 个像素做循环。

![用广播与布尔掩码计算的 Mandelbrot 集：点 c 的颜色是 z -> z^2 + c（从 z = 0 出发）迭代到 |z| > 2 所需的次数](./plots/mandelbrot.py)

## 2.7. 向量化

上面的例子有共同的风格：不对元素写循环，而是把计算表示成对整个数组的少数几个运算。这就是 [3.5.2](/3.5.2) 意义上的**向量化**，同样的想法在 R 中也出现过。在 NumPy 中，它的意思是：用通用函数、归约、广播和索引代替 Python 循环，使循环在编译代码中运行。以数组的方式思考需要练习；几种模式涵盖了大部分情形：

| 循环模式 | 向量化形式 |
|---|---|
| `for i: y[i] = f(x[i])`，其中是算术运算 | 数组上的算术运算、通用函数 |
| 循环内的 `if` | `np.where(cond, a, b)`、布尔索引、`np.clip` |
| 累积求和、最大值、计数 | `sum`、`max`、`np.count_nonzero`，配合 `axis` |
| 累计总和 | `cumsum`、`cumprod`、`np.maximum.accumulate` |
| 对数对的嵌套循环 | 用 `None` 做广播 |
| 直方图、按类别计数 | `np.bincount`、`np.histogram`、`np.unique(..., return_counts=True)` |
| 在有序数据中查找 | `np.searchsorted` |

*例：随机游走。* 我们模拟 1000 条各 1000 步的对称随机游走，希望得到最终位置。循环版本一次抽取一步：

```python
import random


def walks_loop(n_walkers, n_steps, seed=0):
    rnd = random.Random(seed)
    finals = []
    for _ in range(n_walkers):
        pos = 0
        for _ in range(n_steps):
            pos += 1 if rnd.random() < 0.5 else -1
        finals.append(pos)
    return finals


def walks_numpy(n_walkers, n_steps, seed=0):
    rng = np.random.default_rng(seed)
    steps = 2 * rng.integers(0, 2, size=(n_walkers, n_steps), dtype=np.int8) - 1
    paths = steps.cumsum(axis=1, dtype=np.int64)   # position after each step
    return paths[:, -1]
```

在测试机器上，循环版本需要 66 ms，NumPy 版本需要 12 ms。向量化版本计算了全部 $10^6$ 个位置，如果要画出路径就需要它们；如果只需要最终位置，用 `steps.sum(axis=1, dtype=np.int64)` 代替 `cumsum` 只需 6 ms。更好的是，用一点概率知识可以完全省去对每一步的模拟：向上的步数服从二项分布，所以 `2 * rng.binomial(n_steps, 0.5, size=n_walkers) - n_steps` 能以 0.05 ms 产生分布正确的最终位置。一般的教训是：向量化使给定的算法加速一个常数倍，但思考实际需要什么，往往能做得好得多。

*向量化不适用的情形。* 每一步依赖前一步的递推，例如 logistic 映射 $x_{n+1} = r x_n (1 - x_n)$，不能沿时间方向向量化。但往往可以沿相互独立的运行向量化：同时迭代整个参数数组，只保留一个沿时间的 Python 循环，而把对参数的循环交给 NumPy。

```python
def logistic_orbits(r, n_iter=1000, x0=0.2):
    x = np.full_like(r, x0)
    for _ in range(n_iter):          # sequential in time ...
        x = r * x * (1 - x)          # ... vectorized over all values of r
    return x


print(logistic_orbits(np.linspace(2.8, 4.0, 5)).round(4))
# [0.6429 0.7646 0.8422 0.7975 0.1382]
```

当两种办法都行不通，或向量化需要巨大的临时数组时，应当改为编译这个循环，例如用 Numba（[4.4.7](/4.4.7)）。

函数 `np.vectorize` 并不是向量化的办法。它包装一个 Python 函数，使其接受数组并进行广播，但在内部仍然对每个元素调用一次该 Python 函数。对 $10^6$ 个元素的分段函数，`np.vectorize(lambda v: v * v if v > 0 else 0.0)` 在测试机器上需要 160 ms，比对列表做的普通 Python 循环（76 ms）还慢，而 `np.where(x > 0, x * x, 0.0)` 只需 13 ms。它只是为不需要速度的代码提供的便利。

## 2.8. NumPy 与其他数组库

NumPy 数组存放在主存中，由 CPU 处理。PyTorch、JAX 和 TensorFlow 等深度学习框架，以及 CuPy 等 GPU 数组库，提供自己的数组类型，它们可以位于 GPU 上、记录运算以便自动微分，或被即时编译；它们的用法见 [4.7](/4.7)。它们都模仿 NumPy 的接口，所以 NumPy 的知识可以直接迁移。有两个标准把它们连接起来：

- 数组 API 标准（Python array API standard）由 Consortium for Python Data API Standards 发布，规定了一组公共的函数及其签名和语义（创建、逐元素函数、归约、线性代数、索引）。符合标准的库的数组通过 `x.__array_namespace__()` 返回它的命名空间，于是函数只需写一次，就能用于其中任何一个库：`xp = x.__array_namespace__()`，然后 `xp.exp(x)`、`xp.sum(x)`。自 NumPy 2.0 起，主命名空间 `numpy` 符合该标准（NumPy 2.5 报告 `np.__array_api_version__ == "2025.12"`）；对尚未完全符合的库，软件包 `array-api-compat` 提供包装器。SciPy 与 scikit-learn 利用这一机制，在其 API 的部分功能中接受 PyTorch 或 CuPy 数组，但仍是需要主动开启的实验性功能。
- DLPack 是在库之间无需复制地交换数组的协议：数组通过方法 `__dlpack__` 与 `__dlpack_device__` 暴露它的数据指针、形状、步长、dtype 和设备，`np.from_dlpack(x)`、`torch.from_dlpack(x)` 或 `jax.numpy.from_dlpack(x)` 包装的是同一块内存。只有位于同一设备上的数组才能共享内存；GPU 张量必须先复制到 CPU。

```python
a = np.arange(4.0)
print(a.__array_namespace__().__name__, np.__array_api_version__)   # numpy 2025.12
b = np.from_dlpack(a)        # zero-copy: b shares memory with a
b[0] = 9.0
print(a, np.shares_memory(a, b))   # [9. 1. 2. 3.] True
```

PyTorch 还提供 `torch.from_numpy(a)` 与 `t.numpy()`，它们以同样的方式在 NumPy 数组与 CPU 张量之间共享内存。共享的后果与视图相同（§2.4.2）：修改其一会修改另一个。有一点语义上的差别值得一提：JAX 数组是不可变的，所以不写 `x[i] = v`，而写 `x = x.at[i].set(v)`，它返回一个新数组。

## 小结

- ndarray 是带类型的数据缓冲区加上元数据：dtype、形状与步长。所有元素有同一个 dtype；整数宽度固定，溢出时回绕。
- 在 NumPy 2 的类型提升中，Python 标量是“弱”的：它们采用数组的 dtype。
- 步长把下标映射到字节偏移。转置、切片和广播只改变步长，因此没有代价；沿 C 序数组的最后一个轴遍历对缓存友好。
- 基本切片返回与原数组共享内存的视图；高级（整数或布尔）索引返回副本，但通过它赋值会原地写入。需要独立数组时用 `.copy()`，用 `np.shares_memory` 检查。
- 通用函数施行编译好的逐元素循环；它们的方法 `reduce`、`accumulate`、`outer` 和 `at` 涵盖归约与散射运算。`np.sum` 使用成对求和。
- 广播从右侧对齐形状并拉伸长度为 1 的轴；用 `None` 插入轴来控制它，并留意中间数组的大小。
- 向量化把循环从 Python 移入编译代码。它无法处理沿循环的顺序依赖，`np.vectorize` 不会使代码更快，而更好的算法胜过这两者。
- 数组 API 标准与 DLPack 使 NumPy 代码能够与 GPU 和深度学习数组库协同工作并共享内存。
