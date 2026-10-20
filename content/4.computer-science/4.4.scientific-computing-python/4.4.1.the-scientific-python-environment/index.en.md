---
title: The Scientific Python Environment
description: Why Python dominates scientific computing; the layers of the ecosystem; Python versions and support windows; packages, wheels, virtual environments and lock files; project management with uv and pyproject.toml; conda, conda-forge and pixi; Jupyter notebooks and their pitfalls; project layout, type annotations, linting and testing.
---

Before we compute anything, we need a working environment: an interpreter, the libraries that do the actual numerical work, and a way to make the whole setup reproducible on another machine or a year later. This chapter is about that infrastructure. It explains why a slow **interpreter** became the standard language of science, how the scientific Python ecosystem is layered, how packages, virtual environments and lock files work, and which tools (uv, conda, pixi, Jupyter) we use to manage them in practice. The chapter assumes the Python basics of 4.1 and 4.2, in particular modules and packages ([4.2.2](/4.2.2#sec-2.9)) and the object model of Python variables ([4.1.2](/4.1.2#sec-2.1.2)). The following chapters build on it: NumPy arrays ([4.4.2](/4.4.2), [4.4.3](/4.4.3)), the algorithms of SciPy ([4.4.4](/4.4.4)), tabular data with pandas ([4.4.5](/4.4.5)), visualization ([4.4.6](/4.4.6)) and performance ([4.4.7](/4.4.7)).

Tool versions change quickly. The version numbers quoted in this chapter are those current in October 2026; the concepts behind them change much more slowly.

## 1.1. The Scientific Python Stack

### 1.1.1. Why Python

Pure Python is slow for numerical work. A loop that adds a million **floating-point numbers** runs one bytecode instruction after another, and each addition must look up the types of its operands at run time (**dynamic typing**, [4.1.2](/4.1.2#sec-2.1.2)) and allocate a new float object. A compiled C++ loop does the same work in a few machine instructions per element and is typically 30 to 100 times faster.

Python nevertheless dominates scientific computing because it is used as a *glue language*: the program logic is written in Python, while every expensive operation is delegated to compiled code written in C, C++ or Fortran. When we write `A @ B` for two NumPy matrices, Python spends a microsecond dispatching the call; the multiplication itself runs in an optimized BLAS library ([4.4.3](/4.4.3#sec-3.1.2)) at nearly the peak speed of the processor. This division of labor works as long as each call into compiled code does a large amount of work, which is the idea behind **vectorization** ([4.4.2](/4.4.2#sec-2.7)).

The situation in which researchers prototype in a convenient language and then rewrite the program in a fast one is called the *two-language problem*. The scientific Python ecosystem addresses it from three directions: libraries of precompiled kernels (NumPy, SciPy), compilers for numerical Python code (Numba, Cython; [4.4.7](/4.4.7)), and alternative languages designed for both roles at once (Julia). Python's real advantages are the breadth of its libraries, its readability, and the fact that the same language is used for data analysis, machine learning, web services and automation.

### 1.1.2. The Layers of the Ecosystem

The scientific Python libraries form layers, each building on the ones below:

| Layer | Libraries | Role |
|---|---|---|
| Core array | NumPy | The `ndarray` data structure, vectorized arithmetic, linear algebra, random numbers ([4.4.2](/4.4.2), [4.4.3](/4.4.3)) |
| Algorithms | SciPy | Optimization, integration and ODEs, interpolation, statistics, sparse matrices, signal processing, FFT ([4.4.4](/4.4.4)) |
| Data | pandas, Polars | Labeled tables with mixed column types ([4.4.5](/4.4.5)) |
| Visualization | Matplotlib, seaborn, Plotly | Static and interactive plots ([4.4.6](/4.4.6)) |
| Statistics and machine learning | statsmodels, scikit-learn | Statistical models and classical machine learning ([4.6](/4.6)) |
| Domain libraries | Biopython, scikit-image, AnnData and Scanpy, Astropy, SymPy | Sequences, images, single-cell data, astronomy, symbolic mathematics |
| Deep learning | PyTorch, JAX, TensorFlow | Arrays on GPUs, automatic differentiation, neural networks ([4.7](/4.7)) |

Two facts tie the layers together. First, almost every library accepts and returns NumPy arrays, so data flows between them without conversion. Second, the deep learning frameworks have their own array types (`torch.Tensor`, `jax.Array`) that live on GPUs and record operations for automatic differentiation, but they deliberately imitate the NumPy interface and can exchange memory with NumPy without copying. The common interface is now standardized; we return to this in [4.4.2](/4.4.2#sec-2.8).

### 1.1.3. Interpreters and Versions

The reference implementation of Python, and the only one the scientific stack fully supports, is *CPython*, written in C. It compiles source code to **bytecode** and executes the bytecode in a virtual machine ([4.1.1](/4.1.1)). A new minor version (3.14, 3.15, ...) is released every October and receives bug fixes for two years and security fixes for another three, five years in total. In October 2026 the situation is:

| Version | Released | Status (October 2026) | Notes |
|---|---|---|---|
| 3.15 | October 2026 | bug fixes | explicit lazy imports (`lazy import`), UTF-8 as the default text encoding, the `profiling` package with a sampling profiler |
| 3.14 | October 2025 | bug fixes | free-threaded build officially supported |
| 3.13 | October 2024 | security fixes only | experimental free-threaded build and JIT compiler |
| 3.12 | October 2023 | security fixes only | oldest version supported by NumPy 2.5 and SciPy 1.18 |
| 3.10 and older | | end of life | no longer receive any fixes |

The scientific libraries follow a community policy (SPEC 0 of the Scientific Python project) under which they drop support for a Python version about three years after its release. A practical rule follows: use the newest Python version for which all the packages we need publish binary wheels (§1.2.1), and never rely on a version past its end of life. In October 2026, NumPy, SciPy, Matplotlib and pandas already ship wheels for Python 3.15.

Since 3.13, CPython also comes in a *free-threaded* build (`python3.14t`) without the global interpreter lock, in which several threads can execute Python code in parallel; it is discussed with other forms of parallelism in [4.4.7](/4.4.7).

## 1.2. Packages and Environments

### 1.2.1. Packages, Wheels and Package Indexes

Python's terminology distinguishes three things that everyday speech calls "a package". An *import package* is a directory of modules that we can `import` ([4.2.2](/4.2.2#sec-2.9)). A *distribution package* is an archive that installs one or more import packages, together with metadata: its name, version, and the other distributions it requires. A *package index* is a server that hosts distribution packages; the public one is the Python Package Index (PyPI, `pypi.org`). The name we install is not always the name we import: `pip install scikit-learn` provides `import sklearn`.

Distribution packages come in two formats. A *source distribution* (sdist, a `.tar.gz` file) contains the source code and must be built on the user's machine, which for NumPy or SciPy means compiling C, C++ and Fortran code. A *wheel* (a `.whl` file) is a prebuilt archive for a specific Python version and platform, for example `numpy-2.5.4-cp314-cp314-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl`, and installing it only means unpacking it. Wheels are the reason why installing the scientific stack today takes seconds rather than an afternoon of compiler errors.

A *package manager* installs distribution packages together with everything they depend on, and removes or upgrades them. `pip` is the classic installer that comes with Python; uv (§1.3) and conda (§1.4) are package managers with broader scopes.

### 1.2.2. Virtual Environments

Different projects need different versions of the same libraries: an old analysis may require NumPy 1.26, while a new project uses NumPy 2.5. Since a Python interpreter can import only one version of a package, installing everything into the system Python leads sooner or later to conflicts, and on Linux it can even break operating-system tools that are themselves written in Python. Modern Linux distributions therefore refuse `pip install` into the system interpreter.

A *virtual environment* is a directory that contains its own `site-packages` directory for installed packages and links to a base interpreter; activating it makes `python` and `pip` refer to that directory. Each project gets its own environment, and deleting the directory removes everything installed in it. With only the standard library:

```bash
python3 -m venv .venv            # create the environment in the directory .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install numpy scipy
python -c "import numpy; print(numpy.__version__)"
deactivate
```

Virtual environments are cheap and disposable. They are not meant to be copied to another machine or committed to version control; what we share instead is a description of the environment, from which an identical one can be recreated.

### 1.2.3. Dependency Resolution and Lock Files

A project states its direct dependencies with version constraints such as `numpy>=2.0` or `scipy>=1.15,<2`. Each dependency has its own dependencies, and the package manager must choose one version of every package in this graph such that all constraints are satisfied at once. This *dependency resolution* problem is NP-hard in general (it can encode Boolean satisfiability), but practical resolvers solve real instances quickly.

Constraints leave freedom: `numpy>=2.0` is satisfied by 2.0.0 and by 2.5.4, and the resolver picks the newest version available on the day it runs. Two people who install the same project a month apart can therefore obtain different environments. A *lock file* removes this freedom: it records the exact version, source and cryptographic hash of every package in the resolved environment, including indirect dependencies, so that the environment can be reproduced exactly. The two kinds of files have different purposes:

| | Dependency declaration (`pyproject.toml`) | Lock file (`uv.lock`, `pylock.toml`, `pixi.lock`) |
|---|---|---|
| Written by | the author, by hand or through `uv add` | the package manager, never by hand |
| Contains | direct dependencies, version ranges | every package, exact versions and hashes |
| Answers | what the project needs | exactly what was installed |
| Use | libraries published for others | applications, analyses, papers |

For a scientific analysis the lock file belongs in version control next to the code: it is part of what makes a result reproducible. Since 2025 there is also a standardized, tool-independent lock file format, `pylock.toml` (PEP 751).

## 1.3. Project Management with uv

### 1.3.1. A Project in a Few Commands

uv, developed by Astral and written in Rust, combines in one program the tasks that used to need pip, venv, pip-tools, pipx and pyenv: it installs Python interpreters, creates virtual environments, resolves and locks dependencies, and runs commands inside the environment. It is much faster than pip because it resolves in parallel and installs from a global cache through hard links. The examples below use uv 0.13.

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

We never activate the environment explicitly: `uv run` checks that `.venv` agrees with `uv.lock`, updates it if necessary, and then runs the command. The environment therefore cannot drift away from the lock file, which is the most common cause of "it worked on my machine".

### 1.3.2. pyproject.toml

`pyproject.toml` is the standard configuration file of a Python project (PEP 518, PEP 621). After the commands above it contains:

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

The `[project]` table is the standard metadata: `requires-python` restricts the interpreter versions, and `dependencies` lists the direct runtime dependencies with lower bounds (uv adds the version it installed as the lower bound). `[dependency-groups]` (PEP 735) holds dependencies needed only for development, such as test and lint tools, which users of the package do not install. `[build-system]` names the tool that turns the project into a wheel; `[project.scripts]` defines a command `growth-curves` that calls the function `main` in the package `growth_curves`. Tools read their settings from `[tool.<name>]` tables in the same file, for example `[tool.ruff]` or `[tool.pytest.ini_options]`.

The lock file `uv.lock` is generated next to it and records all eighteen packages of the environment: the three we asked for, the nine that Matplotlib and its dependencies pull in, and the development tools with their own dependencies. It is uv's own format; `uv export --format pylock.toml` writes the same information as a standard `pylock.toml`.

### 1.3.3. Scripts and One-Off Tools

Not every computation deserves a project. A single script can declare its dependencies in a comment block at its top (*inline script metadata*, PEP 723), and `uv run` creates a cached environment for it on the fly:

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

`uv add --script quick.py numpy` writes the block for us. Similarly, `uv run --with numba python bench.py` adds a package to a temporary environment for one run, and `uvx ruff check .` runs a command-line tool in an isolated environment without installing it into the project. These temporary environments are cached, so repeated runs start instantly.

## 1.4. conda and pixi

### 1.4.1. When pip Is Not Enough

PyPI distributes Python packages. Scientific work also depends on software that is not Python: C and Fortran libraries, the CUDA toolkit, compilers, R, and command-line tools such as the bioinformatics programs samtools, BLAST or STAR. Wheels can bundle compiled libraries, but each wheel carries its own copy and cannot express dependencies on non-Python programs.

conda solves this by managing packages of any language in environments that contain a complete software stack, including the Python interpreter itself. Its packages come from *channels*. The community channel *conda-forge* provides tens of thousands of packages built consistently against each other, and the *bioconda* channel, built on top of conda-forge, distributes most bioinformatics software. The `defaults` channel of the company Anaconda is subject to Anaconda's terms of service, which require a paid license for use in larger organizations; installers such as Miniforge use conda-forge only and avoid the issue.

```bash
conda create -n rnaseq -c conda-forge -c bioconda python=3.14 numpy pandas samtools star
conda activate rnaseq
conda env export --from-history > environment.yml   # share the declaration
conda env create -f environment.yml                  # recreate it elsewhere
```

A conda environment lives in a central directory and is selected by activation, not by the project directory. Mixing `pip install` into a conda environment works but bypasses conda's resolver; it is best limited to packages that exist only on PyPI.

### 1.4.2. pixi

pixi, from prefix.dev and also written in Rust, applies the project-based workflow of uv to conda packages. A project has a manifest (`pixi.toml`, or a `[tool.pixi]` section in `pyproject.toml`) and a lock file `pixi.lock`, the environment lives in the project directory, and it can combine conda-forge packages with PyPI packages in one resolution:

```bash
pixi init rnaseq --channel conda-forge --channel bioconda && cd rnaseq
pixi add python=3.14 numpy scipy samtools
pixi add --pypi some-pypi-only-package
pixi run python analysis.py
```

The choice among the tools depends mainly on whether non-Python software is involved:

| Tool | Packages from | Environments | Lock file | Typical use |
|---|---|---|---|---|
| venv + pip | PyPI | per project, manual | none (`pip freeze` approximates one) | minimal setups, teaching |
| uv | PyPI | per project, automatic | `uv.lock`, `pylock.toml` | pure-Python projects, scripts, libraries |
| conda / mamba | conda channels (+ pip) | named, central | none by default | existing conda workflows, HPC clusters |
| pixi | conda channels + PyPI | per project, automatic | `pixi.lock` | projects that need non-Python tools, multi-language pipelines |

## 1.5. Interactive Computing with Jupyter

### 1.5.1. Notebooks and Kernels

Exploratory work proceeds in small steps: load data, look at it, try a transformation, plot, adjust. A *Jupyter notebook* is a document made of cells, each containing code or Markdown text; running a code cell sends it to a kernel, a separate process that executes the code and keeps all variables in memory, and the output (text, tables, plots) is stored in the document below the cell. The file format `.ipynb` is JSON, containing the cells and their outputs. The name refers to the three original kernel languages Julia, Python and R; kernels exist for many more.

JupyterLab (version 4.x) is the main web interface; the classic Notebook interface (version 7.x) is now built on the same components. Editors such as VS Code open `.ipynb` files directly and connect to the kernel of a chosen environment. Inside a uv project:

```bash
uv add --dev ipykernel      # lets editors use .venv as a kernel
uv run --with jupyter jupyter lab   # or start JupyterLab without adding it to the project
```

IPython, the interactive shell underlying the Python kernel, adds conveniences to plain Python: `x?` shows documentation, Tab completes names, and *magic commands* such as `%timeit expr` (repeated timing, [4.4.3](/4.4.3#sec-3.5.1)) or `%load_ext autoreload` act on the session itself.

### 1.5.2. Pitfalls of Notebooks

The flexibility of notebooks comes at a price. The kernel state is the result of every cell executed so far, in the order in which it was executed, not the order in which the cells appear. After editing and rerunning cells out of order, the visible code may no longer produce the visible results; a variable deleted from the code still exists in the kernel. Studies of notebooks published on GitHub found that only a minority could be rerun from top to bottom with the same results.

Some habits avoid most problems:

- Before trusting or sharing results, restart the kernel and run all cells in order.
- Keep notebooks for exploration and presentation; move reusable functions into modules in the project package, import them, and test them (§1.6.3).
- Fix random seeds through a single `Generator` ([4.4.3](/4.4.3#sec-3.4)) and record the environment with a lock file.
- Since `.ipynb` files contain outputs and metadata, their diffs are hard to read. Clear outputs before committing (for example with `nbstripout`), or pair each notebook with a plain Python file using Jupytext. Marimo is a newer notebook system that stores notebooks as Python files and reruns dependent cells automatically, which eliminates hidden state.

## 1.6. Writing Maintainable Scientific Code

### 1.6.1. Project Layout

Scientific code tends to start as one script and grow without structure. A layout that separates code, data, exploration and results keeps it manageable:

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

The `src/` layout, which `uv init` creates by default, ensures that tests and notebooks import the installed package rather than whatever files happen to lie in the current directory. Raw data are read-only: every derived file should be reproducible from them by running code, so that an error found later can be corrected by rerunning the pipeline.

### 1.6.2. Type Annotations

Python is **dynamically typed**, but since Python 3.5 we can attach *type annotations* to variables, parameters and return values. The interpreter ignores them at run time; external *type checkers* such as mypy, Pyright or the newer ty read them and report inconsistencies before the program runs, and editors use them for completion. Generic types were introduced in [4.2.9](/4.2.9#sec-9.7).

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

`ArrayLike` accepts anything that NumPy can convert to an array (lists, scalars, arrays), and `NDArray[np.float64]` describes an array with element type `float64`. Annotations do not yet express array shapes in a way that type checkers enforce, although recent NumPy releases annotate the shapes returned by many functions. For scientific code, annotations are most valuable at the boundaries of modules: they document what a function expects, and the checker catches calls that pass a list of strings where an array of floats was meant.

### 1.6.3. Formatting, Linting and Testing

Three tools cover most quality checks, and all of them can be run through `uv run`:

- *Formatting*: `ruff format` rewrites code in a uniform style (compatible with Black), which ends discussions about style and keeps diffs small.
- *Linting*: `ruff check` finds unused imports and variables, undefined names, mutable **default arguments** and hundreds of other common mistakes; `ruff check --fix` corrects many of them.
- *Testing*: pytest runs every function named `test_*` in the `tests/` directory (**unit testing**, [4.1.5](/4.1.5)).

Numerical tests must not compare **floating-point numbers** with `==` ([4.1.2](/4.1.2#sec-2.2.3)). NumPy provides comparison functions with tolerances; good tests check against cases with known answers or against mathematical properties:

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

`assert_allclose(actual, desired, rtol, atol)` passes when $\lvert a - d\rvert \le \mathrm{atol} + \mathrm{rtol}\,\lvert d\rvert$ elementwise. The tolerances should reflect the expected accuracy: close to **machine epsilon** for exact formulas, much larger for results of iterative or approximate methods (the second test is limited by the truncation and **rounding error** of the finite difference, [3.5.1](/3.5.1#sec-1.5.2)).

## Summary

- Python is a glue language: the logic is in Python, the heavy computation in compiled libraries. This works when each call into compiled code does a lot of work.
- The ecosystem is layered around the NumPy array: SciPy, pandas, Matplotlib, scikit-learn and domain libraries build on it; deep learning frameworks imitate its interface.
- Use a supported CPython version for which wheels exist (3.12 to 3.15 in October 2026).
- Every project gets its own virtual environment; `pyproject.toml` declares what the project needs, and a lock file records exactly what was installed.
- uv manages interpreters, environments, dependencies and lock files for PyPI packages; conda and pixi are needed when non-Python software such as bioinformatics tools is involved.
- Notebooks are for exploration; restart and run all before trusting results, and move reusable code into a tested package.
- Type annotations, a formatter, a linter and tests with tolerances make scientific code easier to trust.
