---
title: 性能与并行
description: 让科学计算的 Python 代码变快：计时与性能分析（cProfile、line_profiler、采样分析器），再谈向量化，用 Numba 做即时编译，全局解释器锁，进程池与 joblib，multiprocessing 的启动方式，自由线程 Python，Amdahl 定律，以及实测比较。
source_hash: 737f58329692
---

Python 在单个运算的层面上很慢，而当繁重的工作在编译库中运行时，在整个程序的层面上却很快。前面几章通过**向量化**利用了这一点：NumPy、SciPy 和 pandas 在编译的循环中做算术，解释器只负责调度。本章讨论这还不够的情形：无法向量化的代码（每一步依赖前一步的随机模拟），本身很快但必须运行成千上万次的代码（参数扫描、**自助法**重复、大量样本），以及瓶颈并不在作者所以为之处的代码。所用的工具是测量（计时与性能分析）、编译（Numba）和并行执行（进程、线程以及 CPython 新的自由线程构建）。某些计算为何昂贵或不稳定的数值原因是 [3.5](/3.5) 的主题；作为操作系统对象的进程与线程在 [4.11](/4.11) 中讨论。

本章的所有测量都在同一台笔记本电脑上进行（Intel Core Ultra 7 258V，8 核，WSL 2 下的 Linux），使用 CPython 3.14.5、NumPy 2.5.4、Numba 0.68.0 和 joblib 1.6.0。绝对时间取决于机器、版本和负载，重复运行之间相差可达 20 %；重要的是比值，而且即使是比值，也应在代码将要运行的机器上重新测量。

## 7.1. 先测量，后优化

> 我们应当忘掉小的效率问题，比如在大约 97 % 的时间里：过早优化是万恶之源。（Donald Knuth，1974）

优化会使代码变长、更难读、更容易出错，所以只值得在要紧之处进行，而人们对要紧之处在哪里的直觉出了名地不可靠。第一步永远是测量；第二步是准备好测试（[4.1.5](/4.1.5)），确认变快后的代码计算出的结果仍然相同。

### 7.1.1. 计时

`time.perf_counter()` 是测量经过时间的时钟。对于短小的代码片段，`timeit` 模块（`python -m timeit "..."`，或 IPython 和 Jupyter 中的 `%timeit`）把代码运行许多次并报告统计量，从而消除单次运行的噪声。计时时的良好做法：

- 重复测量并报告最小值或中位数；第一次运行往往较慢（缓存、惰性导入、编译）；
- 使用真实的输入规模：**时间复杂度**更好的算法只有在超过某个规模后才占优，而缓存使小输入不具代表性；
- 确保被计时的代码真的算出了结果（生成器或 polars 的 `LazyFrame` 之类的惰性对象在被消费之前什么也不做）；
- 与给出相同输出的基准做比较，并检查输出确实相同。

### 7.1.2. 性能分析

性能分析（profiling）是测量程序把时间（或内存）花在哪里，按函数或按行分解。它的结果，即性能剖析，把优化引向少数几个决定运行时间的地方。考虑一条小流水线，它模拟 20000 个基因、50 个样本的计数矩阵，对其归一化，并按方差给基因排序；方差用 Python 循环计算：

```python
import numpy as np


def simulate_counts(n_genes, n_samples, rng):
    means = rng.lognormal(mean=3.0, sigma=1.5, size=n_genes)
    return rng.poisson(means[:, None], size=(n_genes, n_samples))


def cpm(counts):
    return counts / counts.sum(axis=0) * 1e6


def gene_variances(x):
    out = []
    for row in x:                      # one Python-level iteration per gene
        m = sum(row) / len(row)
        out.append(sum((v - m) ** 2 for v in row) / (len(row) - 1))
    return np.array(out)


def main():
    rng = np.random.default_rng(0)
    counts = simulate_counts(20_000, 50, rng)
    logcpm = np.log2(cpm(counts) + 1.0)
    var = gene_variances(logcpm)
    top = np.argsort(var)[::-1][:500]
    print(top[:5])


if __name__ == "__main__":
    main()
```

标准库的确定性分析器 `cProfile` 记录每一次函数调用。它从命令行运行，由 `pstats` 对结果排序和过滤：

```bash
python -m cProfile -o prof.out pipeline.py
python -c "import pstats; pstats.Stats('prof.out').strip_dirs().sort_stats('cumulative').print_stats('pipeline')"
```

```text
         1224039 function calls (1221830 primitive calls) in 0.840 seconds

   Ordered by: cumulative time
   List reduced from 876 to 6 due to restriction <'pipeline'>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.840    0.840 pipeline.py:1(<module>)
        1    0.007    0.007    0.722    0.722 pipeline.py:21(main)
        1    0.024    0.024    0.642    0.642 pipeline.py:13(gene_variances)
  1020000    0.307    0.000    0.307    0.000 pipeline.py:17(<genexpr>)
        1    0.052    0.052    0.052    0.052 pipeline.py:4(simulate_counts)
        1    0.010    0.010    0.011    0.011 pipeline.py:9(cpm)
```

`tottime` 是花在函数自身的时间，`cumtime` 则包括它所调用的函数。模拟和归一化是 NumPy 调用，合计用时 0.06 s；`gene_variances` 用时 0.64 s，占 `main` 的 89 %，其中对生成器表达式的一百万次调用说明了原因。逐行性能分析可以进一步缩小范围。第三方的 `line_profiler`（5.1 版）在用 `kernprof -l -v pipeline.py` 运行脚本时，对以 `@profile` 装饰的函数的每一行计时：

```text
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    13                                           @profile
    14                                           def gene_variances(x):
    15         1          1.4      1.4      0.0      out = []
    16     20001       6581.9      0.3      1.0      for row in x:                      # one Python-level iteration per gene
    17     20000     105261.5      5.3     15.4          m = sum(row) / len(row)
    18     20000     571883.3     28.6     83.6          out.append(sum((v - m) ** 2 for v in row) / (len(row) - 1))
```

（时间以微秒计；确定性分析器会使程序变慢，所以分析器下的绝对时间是被夸大的，但比例仍有参考价值。）把该函数换成单个 NumPy 调用 `logcpm.var(axis=1, ddof=1)`，用时从 0.36 s 降到 4.4 ms，结果在 $4.4 \times 10^{-16}$ 的范围内相等。

| 工具 | 类型 | 用途 |
|---|---|---|
| `cProfile` + `pstats`、SnakeViz | 确定性，按函数 | 初步概览；标准库 |
| `line_profiler`（`kernprof`） | 确定性，按行 | 在热点函数内部 |
| `py-spy`、Scalene | 采样 | 附加到正在运行的进程；开销低；能看到原生（C）栈帧；Scalene 还分析内存，并区分 Python 与原生代码的用时 |
| `profiling.sampling`（Python 3.15） | 采样 | 内置的采样分析器，带火焰图和实时视图 |
| `tracemalloc`、memray | 内存 | 内存在何处分配；泄漏与峰值用量 |

*确定性*（跟踪式）分析器挂钩每一次调用和返回，结果精确，但给每次调用增加开销，使有许多小函数的程序失真。*采样*分析器以固定间隔中断程序并记录**调用栈**，几乎没有开销，也能看到编译扩展中花费的时间。Python 3.15（2026 年 10 月）把内置的分析器收入一个新的 `profiling` 包：`profiling.tracing` 就是原来的 `cProfile`（后者仍作为别名保留），`profiling.sampling` 是新的统计式分析器；纯 Python 的 `profile` 模块已被弃用。

## 7.2. 再谈向量化

上面的性能剖析显示了典型的模式：对元素的 Python 循环很慢，因为每次迭代都要在**解释器**中执行若干条**字节码**指令，每条指令都要查找类型、创建和销毁 Python 对象并管理引用计数。NumPy 运算则对整个数组只付一次这样的开销，并在原始机器数上运行编译的循环（[4.4.2](/4.4.2)）。对于简单的逐元素归约，例如对 $10^7$ 个 Poisson 计数求 $\sum_i \log_2(x_i + 1)$：

| 实现 | 时间 | 相对值 |
|---|---|---|
| 使用 `math.log2` 的 Python `for` 循环 | 1075 ms | 16 |
| NumPy：`np.log2(x + 1.0).sum()` | 78 ms | 1.2 |
| Numba 编译的循环（§7.3） | 66 ms | 1 |

向量化有两个局限。第一，它会创建临时数组：`np.log2(x + 1.0).sum()` 分配两个各 80 MB 的数组，对于大数据，代价就由内存流量而不是算术决定（编译的循环不需要临时数组，所以这里略快）。就地运算（`out=`）、`np.einsum`（[4.4.3](/4.4.3)）和分块处理可以缓解这一问题。第二，也更根本的是，有些算法本质上是顺序的。Gillespie 算法（Gillespie algorithm），又称随机模拟算法，能精确模拟化学反应网络：每一步从**指数分布**中抽取到下一次反应的等待时间，该分布的速率是当前各反应倾向（propensity）之和；然后以与倾向成正比的概率选择发生哪一个反应，并更新状态。考虑 mRNA 分子的生灭过程（以速率 $k_b$ 产生，有 $n$ 个分子时以速率 $k_d n$ 降解），其**平稳分布**是均值为 $k_b / k_d$ 的 **Poisson 分布**：

```python
import math
import random


def birth_death(seed, k_birth=10.0, k_death=0.1, t_end=25000.0):
    rng = random.Random(seed)
    t, n = 0.0, 0
    while True:
        a_birth = k_birth
        a_death = k_death * n
        a_total = a_birth + a_death
        t += -math.log(1.0 - rng.random()) / a_total     # exponential waiting time
        if t > t_end:
            return n
        if rng.random() * a_total < a_birth:
            n += 1
        else:
            n -= 1
```

每一步都依赖前一步之后的状态，所以没有可供向量化的数组；约五十万步在 CPython 中每次运行需要 118 ms。这样的代码需要编译，或者在需要许多独立运行时并行运行。

## 7.3. 用 Numba 编译 Python

Numba 用 LLVM 把处理数和 NumPy 数组的 Python 函数编译成**机器语言**，时机是函数第一次以给定类型的参数被调用时；这就是**即时编译**（[4.1.1](/4.1.1)）。编译后的函数从不接触解释器：变量成为机器整数和浮点数，循环成为机器循环。

```python
import math
import numpy as np
from numba import njit, prange


@njit
def log_sum(x):
    s = 0.0
    for i in range(x.shape[0]):
        s += math.log2(x[i] + 1.0)
    return s


@njit
def birth_death_nb(seed, k_birth=10.0, k_death=0.1, t_end=25000.0):
    np.random.seed(seed)                 # seeds Numba's own generator
    t, n = 0.0, 0
    while True:
        a_total = k_birth + k_death * n
        t += -math.log(1.0 - np.random.random()) / a_total
        if t > t_end:
            return n
        if np.random.random() * a_total < k_birth:
            n += 1
        else:
            n -= 1


@njit(parallel=True)
def many_runs(n_rep):
    out = np.empty(n_rep, dtype=np.int64)
    for i in prange(n_rep):              # iterations distributed over threads
        out[i] = birth_death_nb(i)
    return out
```

实测（编译后五次运行中的最佳值）：

| 任务 | CPython | Numba | 加速比 |
|---|---|---|---|
| `log_sum`，$10^7$ 个元素 | 1075 ms | 66 ms | 16 |
| 一次 Gillespie 运行 | 118 ms | 14 ms | 8.5 |
| 32 次 Gillespie 运行，`prange` 用 8 个线程 | 3730 ms（串行） | 81 ms | 46 |

`log_sum` 的第一次调用用了 0.80 s，几乎全部是编译时间；`@njit(cache=True)` 把机器码存到磁盘上，使以后的进程跳过这一步。用好 Numba 的规则如下：

- `@njit`（无 Python 模式，自 Numba 0.59 起是 `@jit` 的默认模式）编译整个函数，否则以类型错误失败；它支持标量、NumPy 数组和 NumPy API 的大部分、元组，以及带类型的列表和字典，但不支持 pandas 对象或任意的 Python 类。传入数组（`df["x"].to_numpy()`），不要传入**数据框**。
- 写朴素的循环：在编译函数内部，循环与 C 一样快，常常比创建临时数组的一串 NumPy 调用更快。
- 保持类型稳定：一个变量在某个分支中是整数、在另一个分支中是浮点数，会迫使它采用较慢的公共类型或导致编译错误。
- `parallel=True` 配合 `prange` 把相互独立的循环迭代放在多个线程上运行；`@vectorize` 把标量函数变成 NumPy 的**通用函数**；`fastmath=True` 允许对**浮点运算**重新排序（更快，但结果在最后几位数字上会改变）。
- 编译代码内部的随机数来自 Numba 自己的生成器，每个线程一个状态，要在编译代码内部设置**种子**（如上），而不是由 NumPy 的全局种子设置。

获得编译速度的其他途径服务于不同的需要：Cython（带 C 类型声明的 Python，提前编译；适合包装 C 库）、用 pybind11 或 nanobind 写的 C++ 扩展（核心用 C++ 写成时，[4.2](/4.2)）、JAX（用 XLA 为 CPU 和 GPU 编译数组程序，带自动微分）、CuPy（NVIDIA GPU 上与 NumPy 兼容的数组库）以及 PyPy（采用跟踪式 JIT 的另一种 Python 实现，对纯 Python 代码很快，但与 C 扩展的兼容性较差）。CPython 本身自 3.13 版起包含一个实验性的 JIT 编译器；它默认关闭，目前只带来有限的加速，对数值循环而言远不能与 Numba 相比。

## 7.4. 并行

### 7.4.1. 进程、线程与 GIL

进程是有自己内存的运行中的程序；线程是进程内部的一条执行序列，与该进程的其他线程共享进程的内存（[4.11](/4.11)）。线程开销小，通过共享对象通信；进程相互隔离，必须复制（序列化）数据才能交换。在 CPython 中，两者的取舍由一个设计要素决定。

**定义 7.4.1（全局解释器锁）** CPython 的**全局解释器锁**（GIL）是一把互斥锁，线程必须持有它才能执行 Python **字节码**。在有 GIL 的进程中，任何时刻至多只有一个线程在运行 Python 代码。

GIL 使解释器的内部状态，首先是每个对象的**引用计数**（CPython 内存管理和**垃圾回收**的基础，[4.2.12](/4.2.12)），无需细粒度的锁就是安全的，并使单线程代码很快。它的后果是线程不能加速受 CPU 限制的 Python 代码：在 §7.4.4 的测量中，八个线程运行纯 Python 的 Gillespie 模拟，用时几乎与一个线程相同。线程在两种情形下仍然有用：

- 受 I/O 限制的工作（下载、数据库查询、读取许多文件）：等待 I/O 的线程会释放 GIL；
- 调用会释放 GIL 的编译代码：NumPy、SciPy、scikit-learn、Numba（`@njit(nogil=True)`）以及大多数压缩和 I/O 库在长时间运算期间都会释放它。对 16 个各含 $4 \times 10^6$ 个浮点数的数组排序，串行用时 1.2–1.6 s，8 个线程用时 0.4–0.5 s。

请注意，NumPy 的线性代数调用多线程的 **BLAS**（OpenBLAS 或 MKL），它本来就用满了所有核；在并行的线程或进程中运行这类调用会使机器超额订阅，可能比串行执行更慢。在更高层次上并行时，可用 `OMP_NUM_THREADS=1` 之类的环境变量（或 `threadpoolctl` 包）限制 BLAS 的线程数。

### 7.4.2. 进程池与 joblib

许多计算任务由相互独立的部分组成：模拟重复、**自助法**重抽样（[3.5.7](/3.5.7)）、参数组、样本、染色体。若问题能拆成无需彼此通信、只在最后收集结果的任务，则称其易并行（embarrassingly parallel）。这类问题用进程池（process pool）并行化：一组固定的工作进程从父进程接收任务，计算并返回结果。

```python
from concurrent.futures import ProcessPoolExecutor

from ssa import birth_death        # the function must be importable by the workers

if __name__ == "__main__":         # required: workers re-import the main module
    with ProcessPoolExecutor(max_workers=8) as pool:
        finals = list(pool.map(birth_death, range(32)))
```

参数和结果要经过 pickle 序列化并在进程之间传送，所以任务应当粗粒度（每个任务几秒而不是几微秒），每个任务传递的数据应当少；大数组最好写入文件，或通过 `multiprocessing.shared_memory` 共享，而不是复制到每个任务。工作进程如何创建，称为*启动方式*：

| 启动方式 | 工作进程如何启动 | 默认用于 |
|---|---|---|
| `fork` | 父进程的副本（内存以写时复制方式共享） | Python 3.13 及以前的 Linux |
| `forkserver` | 从早先启动的干净服务进程派生 | Python 3.14 起的 Linux（以及除 macOS 外的其他 POSIX 系统） |
| `spawn` | 导入主模块的全新解释器 | Windows；自 Python 3.8 起的 macOS |

`fork` 很快，但会复制 fork 时刻所有线程的状态，当父进程运行着线程（BLAS 等库就会这样）时可能死锁；Python 3.12 开始对 fork 多线程进程发出警告，3.14 把 Linux 上的默认值改为 `forkserver`。依赖工作进程继承父进程中设置的**全局变量**（已配置的日志记录器、在导入之后于模块级别载入的数据）的代码，在新的默认值下行为不同；显式传参，或在确知 fork 安全的地方使用 `multiprocessing.get_context("fork")`，可以解决这一问题。即使在 `fork` 下，CPython 的**引用计数**也会写入工作进程触及的每个对象，所以父进程的**写时复制**页面会被逐渐复制。

joblib 是 scikit-learn 的并行后端，它把这种模式包装成紧凑的 API，默认使用稳健的 `loky` 进程池（配合 cloudpickle，因此在 Jupyter 中交互式定义的函数也能用），并为昂贵的函数调用增加磁盘缓存（`joblib.Memory`）：

```python
from joblib import Parallel, delayed

finals = Parallel(n_jobs=8)(delayed(birth_death)(seed) for seed in range(32))
```

并行的随机模拟需要相互独立的随机数流。像上面那样使用**种子** $0, 1, 2, \dots$ 很常见，但 NumPy 中可靠的方法是从一个种子派生出各个流，`rngs = np.random.default_rng(seed).spawn(n)`（或 `np.random.SeedSequence(seed).spawn(n)`），并给每个任务传入一个生成器或子种子，使结果可复现且不依赖于工作进程的个数（[4.4.3](/4.4.3)，以及 [3.5.8](/3.5.8) 中的**伪随机数发生器**）。

### 7.4.3. 自由线程 Python

PEP 703（2023 年通过）提议使 GIL 成为可选项，CPython 3.13 随附了一个实验性的*自由线程构建*，这是解释器的一个单独构建（`python3.13t`），其中 GIL 被禁用，线程真正并行地执行 Python 代码。引用计数、内存分配器（mimalloc）、垃圾回收器和内置容器被重新设计为无需全局锁即线程安全。PEP 779 规定了下一阶段的标准，在 Python 3.14（2025 年 10 月）中，自由线程构建成为正式支持的版本，但仍是可选的：默认的解释器保留 GIL，使自由线程构建成为默认则是更晚的阶段，没有确定的日期。自由线程的解释器按名称选择（`python3.14t`；`uv python install 3.14t`），`sys._is_gil_enabled()` 报告 GIL 是否处于激活状态。

在自由线程构建上，§7.4.4 的测量结果如预期那样改变：八个线程运行纯 Python 模拟比一个线程快 4.2 倍，略优于八个进程，因为线程启动更快并且共享内存。单线程运行比默认构建慢约 10 %，这是线程安全的引用计数的代价。需要记住的几点：

- C 扩展必须针对自由线程的 ABI 构建。NumPy 和科学计算栈的大部分提供了这样的构建，但没有声明自己线程安全的扩展，在被导入时会为整个进程重新启用 GIL（并给出警告）。
- 没有 GIL 时，从多个线程修改共享对象的 Python 代码可能出现以前被掩盖的竞态条件。内置容器的内部保持一致，但复合运算（多个线程执行 `counts[k] += 1`）需要 `threading.Lock`，或者采用每个线程只写自己数据的设计。
- Python 3.14 还增加了 `concurrent.interpreters`（PEP 734）和 `InterpreterPoolExecutor`：一个进程中有多个解释器，各有自己的 GIL，介于线程与进程之间。

对于 2026 年的科学计算代码，进程池仍是受 CPU 限制的纯 Python 工作的稳健默认选择；自由线程适用于实验，以及依赖项都支持它的代码，随着生态系统跟进，它会变得更重要。

### 7.4.4. 实测比较与 Amdahl 定律

§7.2 中纯 Python 的 Gillespie 模拟，独立运行 32 次，每种方案使用 8 个工作单元：

| 策略 | 默认构建（有 GIL） | 自由线程构建 |
|---|---|---|
| 串行循环 | 3.73 s | 4.14 s |
| `ThreadPoolExecutor`，8 个线程 | 3.41 s | 0.99 s |
| `ProcessPoolExecutor`，8 个进程 | 1.07 s | 1.32 s |
| joblib（`loky`），8 个进程 | 1.46 s | 1.75 s |
| Numba 编译，`prange` 用 8 个线程（§7.3） | 0.08 s | — |

时间包括启动工作单元，这是使用进程的代价的一部分，也说明了为什么八个工作单元给出约 3.5 倍而不是 8 倍的加速（这台笔记本电脑的八个核也分为两种，四个性能核和四个能效核）。这一比较包含了本章的主要教训：只有在没有 GIL 时，并行线程才对 Python 代码有帮助；进程有帮助，但要为启动和通信付出代价；编译内层循环比并行化它收益更大，而两者可以结合。

并行还有一个任何硬件都无法消除的极限。若运行时间中有比例 $f$ 可以并行化，其余是串行的，那么用 $p$ 个工作单元时，时间至多降到原来的 $(1 - f) + f/p$，因此加速比为

$$
S(p) = \frac{1}{(1 - f) + f/p} \le \frac{1}{1 - f}.
$$

这个界就是 Amdahl 定律（Amdahl's law）：当 $f = 0.9$ 时，无论多少工作单元都无法获得超过十倍的加速，8 个工作单元至多给出 $4.7$ 倍。因此，串行部分（读取输入、合并结果、启动工作单元）与并行部分同样值得关注。

## 7.5. 选择策略

1. 测量：给整个程序计时，对它做性能分析，找出占主导的部分。
2. 采用更好的算法或库：更低的复杂度、向量化的 NumPy 或 pandas 运算、SciPy 的例程、**稀疏矩阵**。这通常是最大的收益。
3. 编译无法向量化的部分：数组上的数值循环用 Numba；较大的组件用 Cython 或 C++。
4. 并行化相互独立的任务：受 CPU 限制的 Python 代码用进程池或 joblib；I/O 以及会释放 GIL 的代码用线程；依赖项支持的地方用自由线程 Python；任务是许多样本上的整个程序时，用集群调度器或工作流管理器（Snakemake、Nextflow）。
5. 每一步之后都检查结果是否不变，以及收益在代码运行的机器上是否真实。

## 小结

- 先测量后优化：片段用 `timeit`，查看时间花在哪里用 `cProfile` 和 `line_profiler`，对运行中的程序用开销低的采样分析器（`py-spy`、Scalene、Python 3.15 的 `profiling.sampling`）。
- 向量化把循环移入编译代码；它的局限是临时数组和 Gillespie 模拟这类本质上顺序的算法。
- Numba 对数值 Python 函数做即时编译；`@njit` 函数中的朴素循环以 C 的速度运行，`prange` 使之并行。
- GIL 一次只允许一个线程运行 Python 字节码：线程对 I/O 和会释放 GIL 的编译代码有帮助，进程池对受 CPU 限制的 Python 代码有帮助。
- 进程池对任务和结果做 pickle 序列化；任务要粗粒度，要保护主模块，并了解启动方式（自 Python 3.14 起 Linux 默认为 `forkserver`）。
- 易并行问题需要相互独立的随机数流（`SeedSequence.spawn`）才能得到可复现的结果。
- 自由线程的 CPython（自 3.14 起正式支持，仍是可选的）使线程并行运行，付出少量单线程代价，并在线程安全上带来新的责任。
- Amdahl 定律用工作中串行部分的比例给出加速比的上界。
