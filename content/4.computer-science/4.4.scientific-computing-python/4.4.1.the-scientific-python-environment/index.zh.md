---
title: 科学计算的 Python 环境
description: 为什么 Python 主导科学计算；生态系统的层次；Python 版本与支持期限；包、wheel、虚拟环境与锁文件；用 uv 与 pyproject.toml 管理项目；conda、conda-forge 与 pixi；Jupyter 笔记本及其陷阱；项目布局、类型标注、代码检查与测试。
source_hash: 73612a852d6c
---

在开始计算之前，需要先有一个可用的环境：一个解释器，承担实际数值计算的库，以及一种能让整套配置在另一台机器上、或一年之后重现的办法。本章讲的就是这套基础设施：为什么一个运行缓慢的**解释器**成了科学领域的标准语言，科学 Python 生态如何分层，包、虚拟环境与锁文件如何工作，以及实践中用哪些工具（uv、conda、pixi、Jupyter）来管理它们。本章假定读者已有 4.1、4.2 的 Python 基础，特别是模块与包（[4.2.2](/4.2.2#sec-2.9)）以及 Python 变量的对象模型（[4.1.2](/4.1.2#sec-2.1.2)）。后续各章以本章为基础：NumPy 数组（[4.4.2](/4.4.2)、[4.4.3](/4.4.3)）、SciPy 的算法（[4.4.4](/4.4.4)）、pandas 表格数据（[4.4.5](/4.4.5)）、可视化（[4.4.6](/4.4.6)）与性能（[4.4.7](/4.4.7)）。

工具的版本更新很快。本章引用的版本号是 2026 年 10 月的当前版本；版本背后的概念变化要慢得多。

## 1.1. Python 科学计算栈

### 1.1.1. 为什么是 Python

纯 Python 做数值计算很慢。把一百万个**浮点数**相加的循环要逐条执行字节码，每次加法都要在运行时查询操作数的类型（**动态类型**，[4.1.2](/4.1.2#sec-2.1.2)），并分配一个新的 float 对象。编译后的 C++ 循环每个元素只需几条机器指令，通常快 30 到 100 倍。

Python 仍然主导科学计算，是因为它被用作胶水语言（glue language）：程序逻辑用 Python 编写，所有耗时的运算则交给用 C、C++ 或 Fortran 写成的编译代码。对两个 NumPy 矩阵写 `A @ B` 时，Python 只花一微秒分派这次调用，乘法本身在优化过的 BLAS 库（[4.4.3](/4.4.3#sec-3.1.2)）中运行，速度接近处理器的峰值。只要每次进入编译代码的调用都做足够多的工作，这种分工就行得通，这正是**向量化**（[4.4.2](/4.4.2#sec-2.7)）的思想。

研究者先用方便的语言做原型、再用快速的语言重写程序，这种局面称为双语言问题（two-language problem）。科学 Python 生态从三个方向应对它：预编译内核的库（NumPy、SciPy）、面向数值 Python 代码的编译器（Numba、Cython；[4.4.7](/4.4.7)），以及同时胜任两种角色的新语言（Julia）。Python 真正的优势在于库的广度、可读性，以及同一种语言可用于数据分析、机器学习、网络服务和自动化。

### 1.1.2. 生态系统的层次

科学 Python 的库形成若干层次，每一层建立在下面各层之上：

| 层次 | 库 | 作用 |
|---|---|---|
| 核心数组 | NumPy | `ndarray` 数据结构、向量化算术、线性代数、随机数（[4.4.2](/4.4.2)、[4.4.3](/4.4.3)） |
| 算法 | SciPy | 优化、积分与常微分方程、插值、统计、稀疏矩阵、信号处理、FFT（[4.4.4](/4.4.4)） |
| 数据 | pandas、Polars | 列类型可以不同的带标签表格（[4.4.5](/4.4.5)） |
| 可视化 | Matplotlib、seaborn、Plotly | 静态与交互式绘图（[4.4.6](/4.4.6)） |
| 统计与机器学习 | statsmodels、scikit-learn | 统计模型与经典机器学习（[4.6](/4.6)） |
| 领域库 | Biopython、scikit-image、AnnData 与 Scanpy、Astropy、SymPy | 序列、图像、单细胞数据、天文学、符号数学 |
| 深度学习 | PyTorch、JAX、TensorFlow | GPU 上的数组、自动微分、神经网络（[4.7](/4.7)） |

有两个事实把各层联系起来。第一，几乎所有库都接受并返回 NumPy 数组，因此数据在库之间流动无需转换。第二，深度学习框架有自己的数组类型（`torch.Tensor`、`jax.Array`），它们位于 GPU 上并记录运算以便自动微分，但刻意模仿 NumPy 的接口，并且可以与 NumPy 共享内存而不复制。这一公共接口现在已经标准化，将在 [4.4.2](/4.4.2#sec-2.8) 中回到这一点。

### 1.1.3. 解释器与版本

Python 的参考实现是用 C 写成的 CPython，也是科学计算栈唯一完整支持的实现。它把源代码编译为**字节码**，再由虚拟机执行（[4.1.1](/4.1.1)）。每年 10 月发布一个新的小版本（3.14、3.15 等），之后两年提供缺陷修复，再三年提供安全修复，共五年。2026 年 10 月的情况如下：

| 版本 | 发布时间 | 状态（2026 年 10 月） | 说明 |
|---|---|---|---|
| 3.15 | 2026 年 10 月 | 缺陷修复 | 显式惰性导入（`lazy import`）、UTF-8 成为默认文本编码、带采样分析器的 `profiling` 包 |
| 3.14 | 2025 年 10 月 | 缺陷修复 | 正式支持自由线程构建 |
| 3.13 | 2024 年 10 月 | 仅安全修复 | 实验性的自由线程构建与 JIT 编译器 |
| 3.12 | 2023 年 10 月 | 仅安全修复 | NumPy 2.5 与 SciPy 1.18 支持的最旧版本 |
| 3.10 及更早 | | 已终止支持 | 不再有任何修复 |

科学计算库遵循社区的政策（Scientific Python 项目的 SPEC 0）：在某个 Python 版本发布约三年后停止支持它。由此得到一条实用规则：使用所需的全部包都发布了二进制 wheel（§1.2.1）的最新 Python 版本，并且不要依赖已终止支持的版本。2026 年 10 月，NumPy、SciPy、Matplotlib 与 pandas 都已提供 Python 3.15 的 wheel。

自 3.13 起，CPython 还提供不带全局解释器锁的自由线程构建（`python3.14t`），其中多个线程可以并行执行 Python 代码；它与其他形式的并行一起在 [4.4.7](/4.4.7) 中讨论。

## 1.2. 包与环境

### 1.2.1. 包、wheel 与包索引

日常说的“包”，在 Python 的术语中对应三种不同的东西。导入包（import package）是可以 `import` 的模块目录（[4.2.2](/4.2.2#sec-2.9)）。分发包（distribution package）是安装一个或多个导入包的归档文件，带有元数据：名称、版本以及它所需要的其他分发包。包索引（package index）是托管分发包的服务器，公共的那个是 Python Package Index（PyPI，`pypi.org`）。安装时用的名字并不总是导入时用的名字：`pip install scikit-learn` 提供的是 `import sklearn`。

分发包有两种格式。源码分发包（source distribution），简称 sdist，即 `.tar.gz` 文件，包含源代码，必须在用户的机器上构建，对 NumPy 或 SciPy 来说意味着编译 C、C++ 和 Fortran 代码。wheel 包（wheel），即 `.whl` 文件，是针对特定 Python 版本与平台的预构建归档，例如 `numpy-2.5.4-cp314-cp314-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl`，安装它只需解压。正因为有了 wheel，今天安装科学计算栈只要几秒钟，而不必面对一个下午的编译器报错。

包管理器（package manager）负责安装分发包及其全部依赖，并负责卸载或升级。`pip` 是 Python 自带的经典安装器；uv（§1.3）与 conda（§1.4）是适用范围更广的包管理器。

### 1.2.2. 虚拟环境

不同项目需要同一个库的不同版本：旧的分析可能需要 NumPy 1.26，而新项目使用 NumPy 2.5。由于一个 Python 解释器只能导入某个包的一个版本，把所有东西都装进系统 Python 迟早会引起冲突，在 Linux 上甚至可能破坏同样用 Python 写成的操作系统工具。因此现代 Linux 发行版拒绝向系统解释器执行 `pip install`。

虚拟环境（virtual environment）是一个目录，其中有存放已安装包的专属 `site-packages` 目录，并链接到某个基础解释器；激活它之后，`python` 和 `pip` 就指向该目录。每个项目有自己的环境，删除该目录就移除了其中安装的一切。只用标准库即可：

```bash
python3 -m venv .venv            # create the environment in the directory .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install numpy scipy
python -c "import numpy; print(numpy.__version__)"
deactivate
```

虚拟环境创建成本低、可随时丢弃。它们不应被复制到另一台机器，也不应提交到版本控制；要共享的是环境的描述，据此可以重建出一个相同的环境。

### 1.2.3. 依赖解析与锁文件

项目用版本约束（如 `numpy>=2.0` 或 `scipy>=1.15,<2`）声明它的直接依赖。每个依赖又有自己的依赖，包管理器必须为这张图中的每个包选定一个版本，使所有约束同时满足。这个依赖解析（dependency resolution）问题在一般情形下是 NP 困难的（它可以编码布尔可满足性问题），但实用的解析器能很快解决真实的实例。

约束留有自由度：`numpy>=2.0` 被 2.0.0 满足，也被 2.5.4 满足，解析器会选取运行当天可用的最新版本。因此两个人相隔一个月安装同一个项目，可能得到不同的环境。锁文件（lock file）消除了这种自由度：它记录解析后环境中每个包（包括间接依赖）的确切版本、来源与加密哈希，从而可以精确复现环境。这两类文件的用途不同：

| | 依赖声明（`pyproject.toml`） | 锁文件（`uv.lock`、`pylock.toml`、`pixi.lock`） |
|---|---|---|
| 编写者 | 作者，手写或通过 `uv add` | 包管理器，从不手写 |
| 内容 | 直接依赖、版本范围 | 每个包、确切版本与哈希 |
| 回答的问题 | 项目需要什么 | 实际安装了什么 |
| 用途 | 发布给他人的库 | 应用、分析、论文 |

对科学分析而言，锁文件应与代码一起纳入版本控制：它是结果可复现的一部分。自 2025 年起还有一种标准化的、与工具无关的锁文件格式 `pylock.toml`（PEP 751）。

## 1.3. 用 uv 管理项目

### 1.3.1. 几条命令建立一个项目

uv 由 Astral 开发，用 Rust 编写，把过去需要 pip、venv、pip-tools、pipx 和 pyenv 的任务集于一身：安装 Python 解释器、创建虚拟环境、解析并锁定依赖、在环境中运行命令。它比 pip 快得多，因为并行解析依赖，并通过硬链接从全局缓存安装。下面的例子使用 uv 0.13。

```bash
uv init growth-curves        # new project: pyproject.toml, .python-version, src/, git repository
cd growth-curves
uv add numpy scipy matplotlib  # resolve, update pyproject.toml and uv.lock, install into .venv
uv add --dev pytest ruff     # development-only tools, in a dependency group
uv run python analysis.py    # run inside the project environment (synced automatically)
uv run pytest
uv sync                      # make .venv match uv.lock exactly (e.g. after git pull)
uv lock --upgrade            # re-resolve to the newest allowed versions
uv python install 3.14       # download a managed interpreter
uv python pin 3.14           # record it in .python-version
```

我们从不显式激活环境：`uv run` 会检查 `.venv` 与 `uv.lock` 是否一致，必要时更新，然后运行命令。因此环境不会偏离锁文件，而这正是“在我的机器上能跑”这类问题最常见的原因。

### 1.3.2. pyproject.toml

`pyproject.toml` 是 Python 项目的标准配置文件（PEP 518、PEP 621）。执行上面的命令之后，它的内容如下：

```toml
[project]
name = "growth-curves"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.14"
dependencies = [
    "matplotlib>=3.11.2",
    "numpy>=2.5.4",
    "scipy>=1.18.1",
]

[project.scripts]
growth-curves = "growth_curves:main"

[build-system]
requires = ["uv_build>=0.13.3,<0.14.0"]
build-backend = "uv_build"

[dependency-groups]
dev = [
    "pytest>=9.1.1",
    "ruff>=0.17.1",
]
```

`[project]` 表是标准元数据：`requires-python` 限定解释器版本，`dependencies` 以下界列出直接的运行时依赖（uv 把它安装的版本作为下界写入）。`[dependency-groups]`（PEP 735）存放只在开发时需要的依赖，例如测试与代码检查工具，包的使用者不会安装它们。`[build-system]` 指明把项目构建成 wheel 的工具；`[project.scripts]` 定义命令 `growth-curves`，它调用包 `growth_curves` 中的函数 `main`。各工具从同一文件的 `[tool.<name>]` 表中读取设置，例如 `[tool.ruff]` 或 `[tool.pytest.ini_options]`。

锁文件 `uv.lock` 生成在它旁边，记录环境中的全部 18 个包：我们指定的三个，Matplotlib 及其依赖引入的九个，以及开发工具和它们各自的依赖。它是 uv 自己的格式；`uv export --format pylock.toml` 把同样的信息写成标准的 `pylock.toml`。

### 1.3.3. 脚本与一次性工具

并非每个计算都值得建一个项目。单个脚本可以在文件顶部的注释块中声明依赖（内联脚本元数据（inline script metadata），PEP 723），`uv run` 会为它即时创建一个带缓存的环境：

```python
# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "numpy>=2.5.4",
# ]
# ///
import numpy as np

print(np.linspace(0, 1, 5))
```

```text
$ uv run quick.py
[0.   0.25 0.5  0.75 1.  ]
```

`uv add --script quick.py numpy` 会替我们写好这个注释块。类似地，`uv run --with numba python bench.py` 把一个包加入临时环境，只用于这一次运行；`uvx ruff check .` 在隔离的环境中运行命令行工具，而不把它安装进项目。这些临时环境带有缓存，重复运行时立即启动。

## 1.4. conda 与 pixi

### 1.4.1. pip 不够用的时候

PyPI 分发的是 Python 包。科学工作还依赖不是 Python 的软件：C 与 Fortran 库、CUDA 工具包、编译器、R，以及命令行工具，例如生物信息学程序 samtools、BLAST 或 STAR。wheel 可以打包编译好的库，但每个 wheel 带着自己的一份副本，也无法表达对非 Python 程序的依赖。

conda 解决这个问题的办法是：在包含完整软件栈（包括 Python 解释器本身）的环境中，管理任何语言的包。它的包来自频道（channel）。社区频道 conda-forge 提供数以万计彼此一致构建的包，建立在 conda-forge 之上的 bioconda 频道则分发大部分生物信息学软件。Anaconda 公司的 `defaults` 频道受 Anaconda 服务条款约束，较大的机构使用它需要付费许可；Miniforge 这类安装器只使用 conda-forge，从而回避了这个问题。

```bash
conda create -n rnaseq -c conda-forge -c bioconda python=3.14 numpy pandas samtools star
conda activate rnaseq
conda env export --from-history > environment.yml   # share the declaration
conda env create -f environment.yml                  # recreate it elsewhere
```

conda 环境位于一个集中的目录，通过激活来选用，而不由项目目录决定。在 conda 环境中混用 `pip install` 是可行的，但会绕过 conda 的解析器，最好只用于仅存在于 PyPI 的包。

### 1.4.2. pixi

pixi 来自 prefix.dev，同样用 Rust 编写，把 uv 以项目为单位的工作流应用于 conda 包。项目有清单（`pixi.toml`，或 `pyproject.toml` 中的 `[tool.pixi]` 部分）和锁文件 `pixi.lock`，环境位于项目目录中，并且可以在一次解析中把 conda-forge 的包与 PyPI 的包结合起来：

```bash
pixi init rnaseq --channel conda-forge --channel bioconda && cd rnaseq
pixi add python=3.14 numpy scipy samtools
pixi add --pypi some-pypi-only-package
pixi run python analysis.py
```

在这些工具之间如何选择，主要取决于是否涉及非 Python 软件：

| 工具 | 包的来源 | 环境 | 锁文件 | 典型用途 |
|---|---|---|---|---|
| venv + pip | PyPI | 每个项目一个，手动管理 | 无（`pip freeze` 可近似） | 最简配置、教学 |
| uv | PyPI | 每个项目一个，自动管理 | `uv.lock`、`pylock.toml` | 纯 Python 项目、脚本、库 |
| conda / mamba | conda 频道（及 pip） | 有名字，集中存放 | 默认无 | 已有的 conda 工作流、HPC 集群 |
| pixi | conda 频道与 PyPI | 每个项目一个，自动管理 | `pixi.lock` | 需要非 Python 工具的项目、多语言流水线 |

## 1.5. 用 Jupyter 进行交互式计算

### 1.5.1. 笔记本与内核

探索性的工作是一小步一小步推进的：加载数据，查看，尝试一种变换，绘图，调整。Jupyter 笔记本（Jupyter notebook）是由单元格组成的文档，每个单元格包含代码或 Markdown 文本；运行代码单元格就是把它发送给内核，即一个单独的进程，它执行代码并把所有变量保留在内存中，输出（文本、表格、图）则存储在文档中该单元格的下方。文件格式 `.ipynb` 是 JSON，包含各单元格及其输出。Jupyter 这个名字指最初的三种内核语言 Julia、Python 和 R；现在已有更多语言的内核。

JupyterLab（4.x 版）是主要的网页界面；经典的 Notebook 界面（7.x 版）现在建立在同样的组件之上。VS Code 等编辑器可以直接打开 `.ipynb` 文件，并连接所选环境的内核。在 uv 项目中：

```bash
uv add --dev ipykernel      # lets editors use .venv as a kernel
uv run --with jupyter jupyter lab   # or start JupyterLab without adding it to the project
```

IPython 是 Python 内核背后的交互式 shell，它给普通 Python 增加了许多便利：`x?` 显示文档，Tab 补全名称，魔术命令如 `%timeit expr`（重复计时，[4.4.3](/4.4.3#sec-3.5.1)）或 `%load_ext autoreload` 作用于会话本身。

### 1.5.2. 笔记本的陷阱

笔记本的灵活性是有代价的。内核状态是迄今所有已执行单元格按执行顺序（而不是单元格出现的顺序）累积的结果。乱序编辑并重新运行单元格之后，看到的代码可能不再产生看到的结果；从代码中删掉的变量仍然存在于内核中。对 GitHub 上公开的笔记本的研究发现，只有少数能从头到尾重新运行并得到相同的结果。

一些习惯可以避免大部分问题：

- 在信任或分享结果之前，重启内核并按顺序运行全部单元格。
- 笔记本用于探索和展示；把可复用的函数移入项目包的模块中，导入并测试它们（§1.6.3）。
- 通过单个 `Generator`（[4.4.3](/4.4.3#sec-3.4)）固定随机种子，并用锁文件记录环境。
- `.ipynb` 文件含有输出和元数据，其差异（diff）难以阅读。提交前清除输出（例如用 `nbstripout`），或者用 Jupytext 把每个笔记本与一个普通 Python 文件配对。Marimo 是较新的笔记本系统，它把笔记本存为 Python 文件并自动重新运行相关单元格，从而消除了隐藏状态。

## 1.6. 编写可维护的科学计算代码

### 1.6.1. 项目布局

科学计算代码往往从一个脚本开始，无结构地膨胀。把代码、数据、探索与结果分开的布局可以让它保持可控：

```text
growth-curves/
├── pyproject.toml          project metadata and dependencies
├── uv.lock                 exact environment (committed)
├── README.md
├── src/growth_curves/      importable package: the reusable code
│   ├── __init__.py
│   ├── models.py
│   └── fitting.py
├── tests/                  tests for the package (pytest)
│   └── test_fitting.py
├── notebooks/              exploration; imports from growth_curves
├── data/raw/               original data, never modified
├── data/processed/         generated by scripts, can be deleted
└── results/                figures and tables, generated by scripts
```

`uv init` 默认创建的 `src/` 布局保证测试和笔记本导入的是已安装的包，而不是当前目录里碰巧存在的文件。原始数据是只读的：每个派生文件都应能通过运行代码由它们重现，这样以后发现错误时，重新运行流水线就可以纠正。

### 1.6.2. 类型标注

Python 是**动态类型**的，但自 Python 3.5 起，可以为变量、参数和返回值附加类型标注（type annotation）。解释器在运行时忽略它们；mypy、Pyright 或较新的 ty 这样的外部类型检查器（type checker）读取标注，在程序运行之前报告不一致之处，编辑器则用它们做补全。泛型类型在 [4.2.9](/4.2.9#sec-9.7) 中引入过。

```python
from collections.abc import Sequence

import numpy as np
from numpy.typing import ArrayLike, NDArray


def logistic(t: ArrayLike, r: float, K: float, N0: float) -> NDArray[np.float64]:
    """Solution N(t) = K / (1 + (K / N0 - 1) exp(-r t)) of the logistic equation."""
    t = np.asarray(t, dtype=np.float64)
    return K / (1 + (K / N0 - 1) * np.exp(-r * t))


def mean_final_size(runs: Sequence[NDArray[np.float64]]) -> float:
    return float(np.mean([run[-1] for run in runs]))
```

`ArrayLike` 接受 NumPy 能转换为数组的任何东西（列表、标量、数组），`NDArray[np.float64]` 描述元素类型为 `float64` 的数组。标注目前还不能以类型检查器强制执行的方式表达数组的形状，不过较新的 NumPy 版本已经为许多函数返回的形状加了标注。对科学计算代码来说，标注在模块边界上最有价值：它记录了函数期望什么，检查器则能发现把字符串列表传给本应是浮点数组的参数这类调用。

### 1.6.3. 格式化、代码检查与测试

三个工具涵盖了大部分质量检查，它们都可以通过 `uv run` 运行：

- 格式化：`ruff format` 以统一的风格重写代码（与 Black 兼容），这终结了关于风格的争论，也让差异保持精简。
- 代码检查（linting）：`ruff check` 能发现未使用的导入与变量、未定义的名称、可变的**默认实参**，以及数百种其他常见错误；`ruff check --fix` 可以纠正其中许多。
- 测试：pytest 运行 `tests/` 目录中每个名为 `test_*` 的函数（**单元测试**，[4.1.5](/4.1.5)）。

数值测试不能用 `==` 比较**浮点数**（[4.1.2](/4.1.2#sec-2.2.3)）。NumPy 提供带容差的比较函数；好的测试对照已知答案的情形或数学性质来检查：

```python
# tests/test_fitting.py
import numpy as np
from numpy.testing import assert_allclose

from growth_curves.models import logistic


def test_logistic_limits():
    t = np.array([0.0, 1e3])
    assert_allclose(logistic(t, r=0.5, K=100.0, N0=5.0), [5.0, 100.0], rtol=1e-12)


def test_logistic_satisfies_ode():
    # dN/dt = r N (1 - N/K), checked with a central difference
    r, K, N0, h = 0.5, 100.0, 5.0, 1e-5
    t = np.linspace(0, 20, 50)
    dN = (logistic(t + h, r, K, N0) - logistic(t - h, r, K, N0)) / (2 * h)
    N = logistic(t, r, K, N0)
    assert_allclose(dN, r * N * (1 - N / K), rtol=1e-6)
```

`assert_allclose(actual, desired, rtol, atol)` 在逐元素满足 $\lvert a - d\rvert \le \mathrm{atol} + \mathrm{rtol}\,\lvert d\rvert$ 时通过。容差应当反映预期的精度：对精确公式，接近**机器精度**；对迭代或近似方法的结果，则要大得多（第二个测试受有限差分的截断误差与**舍入误差**限制，[3.5.1](/3.5.1#sec-1.5.2)）。

## 小结

- Python 是胶水语言：逻辑在 Python 中，繁重的计算在编译库中。当每次进入编译代码的调用都做大量工作时，这种方式才行得通。
- 生态系统围绕 NumPy 数组分层：SciPy、pandas、Matplotlib、scikit-learn 与领域库都建立在它之上；深度学习框架模仿它的接口。
- 使用有 wheel 可用的受支持的 CPython 版本（2026 年 10 月为 3.12 至 3.15）。
- 每个项目都有自己的虚拟环境；`pyproject.toml` 声明项目需要什么，锁文件记录实际安装了什么。
- uv 管理 PyPI 包的解释器、环境、依赖与锁文件；涉及生物信息学工具等非 Python 软件时，需要 conda 和 pixi。
- 笔记本用于探索；信任结果之前先重启并运行全部单元格，并把可复用的代码移入经过测试的包中。
- 类型标注、格式化工具、代码检查工具以及带容差的测试，使科学计算代码更值得信赖。
