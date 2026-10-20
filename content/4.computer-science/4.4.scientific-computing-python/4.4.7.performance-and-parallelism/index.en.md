---
title: Performance and Parallelism
description: "Making scientific Python code fast: timing and profiling (cProfile, line_profiler, sampling profilers), vectorization revisited, just-in-time compilation with Numba, the global interpreter lock, process pools and joblib, multiprocessing start methods, free-threaded Python, Amdahl's law, and measured comparisons."
---

Python is slow at the level of individual operations and fast at the level of whole programs when the heavy work runs in compiled libraries. The previous chapters exploited this through **vectorization**: NumPy, SciPy and pandas do the arithmetic in compiled loops, and the interpreter only orchestrates. This chapter is about the cases where that is not enough: code that cannot be vectorized (a stochastic simulation in which each step depends on the previous one), code that is fast but must run thousands of times (parameter scans, bootstrap replicates, many samples), and code whose bottleneck is not where its author believes. The tools are measurement (timing and profiling), compilation (Numba) and parallel execution (processes, threads and the new free-threaded build of CPython). The numerical reasons why some computations are expensive or unstable are the subject of [3.5](/3.5); processes and threads as objects of the operating system are treated in [4.11](/4.11).

All measurements in this chapter were taken on one laptop (Intel Core Ultra 7 258V, 8 cores, Linux under WSL 2) with CPython 3.14.5, NumPy 2.5.4, Numba 0.68.0 and joblib 1.6.0. Absolute times depend on the machine, the versions and the load, and repeated runs differed by up to 20 %; the ratios are what matter, and even they should be measured again on the machine where the code will run.

## 7.1. Measuring Before Optimizing

> We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil. (Donald Knuth, 1974)

Optimization makes code longer, harder to read and easier to break, so it is worth doing only where it matters, and intuition about where that is is notoriously unreliable. The first step is always to measure; the second is to have tests ([4.1.5](/4.1.5)) that confirm that the faster code still computes the same result.

### 7.1.1. Timing

`time.perf_counter()` is the clock for measuring elapsed time. For short snippets, the `timeit` module (`python -m timeit "..."`, or `%timeit` in IPython and Jupyter) runs the code many times and reports statistics, which removes the noise of a single run. Good practice when timing:

- repeat the measurement and report the minimum or median; the first run is often slower (caches, lazy imports, compilation);
- use realistic input sizes: an algorithm with a better **time complexity** wins only beyond some size, and caches make small inputs unrepresentative;
- make sure the timed code actually computes its result (lazy objects, such as generators or a polars `LazyFrame`, do nothing until consumed);
- compare against a baseline that gives the same output, and check that it does.

### 7.1.2. Profiling

*Profiling* is the measurement of where a program spends its time (or memory), broken down by function or by line. Its result, a profile, directs optimization to the few places that dominate the running time. Consider a small pipeline that simulates a count matrix of 20000 genes and 50 samples, normalizes it, and ranks genes by variance; the variance is computed with a Python loop:

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

The standard library's deterministic profiler `cProfile` records every function call. It is run from the command line, and `pstats` sorts and filters the result:

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

`tottime` is the time spent in the function itself, `cumtime` includes the functions it calls. The simulation and the normalization, which are NumPy calls, take 0.06 s together; `gene_variances` takes 0.64 s, 89 % of `main`, and a million calls of a generator expression inside it show why. A line-by-line profile narrows this down further. The third-party `line_profiler` (version 5.1) times every line of the functions decorated with `@profile` when the script is run with `kernprof -l -v pipeline.py`:

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

(times in microseconds; the deterministic profilers slow the program down, so absolute times under a profiler are inflated, but the proportions are informative.) Replacing the function by the single NumPy call `logcpm.var(axis=1, ddof=1)` reduces its time from 0.36 s to 4.4 ms, with results equal up to $4.4 \times 10^{-16}$.

| Tool | Kind | Use |
|---|---|---|
| `cProfile` + `pstats`, SnakeViz | deterministic, per function | first overview; standard library |
| `line_profiler` (`kernprof`) | deterministic, per line | inside a hot function |
| `py-spy`, Scalene | sampling | attach to a running process; low overhead; native (C) frames; Scalene also profiles memory and separates Python from native time |
| `profiling.sampling` (Python 3.15) | sampling | built-in sampling profiler, with flame graphs and a live view |
| `tracemalloc`, memray | memory | where memory is allocated; leaks and peak usage |

A *deterministic* (tracing) profiler hooks every call and return, which is exact but adds overhead to every call, distorting programs with many small functions. A *sampling* profiler interrupts the program at regular intervals and records the call stack, which costs almost nothing and also sees time spent in compiled extensions. Python 3.15 (October 2026) collects the built-in profilers in a new `profiling` package: `profiling.tracing` is the former `cProfile` (which remains as an alias) and `profiling.sampling` is a new statistical profiler; the pure-Python `profile` module is deprecated.

## 7.2. Vectorization Revisited

The profile above shows the typical pattern: a Python loop over elements is slow because every iteration executes several bytecode instructions in the **interpreter**, each of which looks up types, creates and destroys Python objects and manages reference counts. A NumPy operation pays this overhead once per array and runs a compiled loop over raw machine numbers ([4.4.2](/4.4.2)). For a simple elementwise reduction, $\sum_i \log_2(x_i + 1)$ over $10^7$ Poisson counts:

| Implementation | Time | Relative |
|---|---|---|
| Python `for` loop with `math.log2` | 1075 ms | 16 |
| NumPy: `np.log2(x + 1.0).sum()` | 78 ms | 1.2 |
| Numba-compiled loop (§7.3) | 66 ms | 1 |

Vectorization has two limits. First, it creates temporary arrays: `np.log2(x + 1.0).sum()` allocates two arrays of 80 MB each, and for large data memory traffic rather than arithmetic becomes the cost (the compiled loop needs no temporaries, which is why it is slightly faster here). In-place operations (`out=`), `np.einsum` ([4.4.3](/4.4.3)) and processing in chunks reduce the problem. Second, and more fundamentally, some algorithms are sequential. The *Gillespie algorithm* (stochastic simulation algorithm) simulates a chemical reaction network exactly: in each step it draws the waiting time to the next reaction from an **exponential distribution** whose rate is the sum of the current reaction propensities, then chooses which reaction occurs with probabilities proportional to them, and updates the state. For a birth–death process of mRNA molecules (production at rate $k_b$, degradation at rate $k_d n$ when $n$ molecules are present), whose stationary distribution is the **Poisson distribution** with mean $k_b / k_d$:

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

Each step depends on the state after the previous one, so there is no array over which to vectorize; about half a million steps take 118 ms per run in CPython. Such code needs to be compiled or, if many independent runs are needed, run in parallel.

## 7.3. Compiling Python with Numba

Numba compiles Python functions that work on numbers and NumPy arrays to machine code with LLVM, at the moment they are first called with arguments of given types; this is just-in-time compilation ([4.1.1](/4.1.1)). The compiled function never touches the interpreter: variables become machine integers and floats, loops become machine loops.

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

Measured (best of five runs after compilation):

| Task | CPython | Numba | Speed-up |
|---|---|---|---|
| `log_sum`, $10^7$ elements | 1075 ms | 66 ms | 16 |
| one Gillespie run | 118 ms | 14 ms | 8.5 |
| 32 Gillespie runs, `prange` on 8 threads | 3730 ms (serial) | 81 ms | 46 |

The first call of `log_sum` took 0.80 s, almost all of it compilation; `@njit(cache=True)` stores the machine code on disk so that later processes skip this step. The rules for using Numba well:

- `@njit` (no-Python mode, the default of `@jit` since Numba 0.59) compiles the whole function or fails with a typing error; it supports scalars, NumPy arrays and a large part of the NumPy API, tuples, and typed lists and dictionaries, but not pandas objects or arbitrary Python classes. Pass arrays (`df["x"].to_numpy()`), not DataFrames.
- Write plain loops: inside a compiled function a loop is as fast as in C, and often faster than a chain of NumPy calls that creates temporaries.
- Keep types stable: a variable that is an integer in one branch and a float in another forces a slower common type or a compilation error.
- `parallel=True` with `prange` runs independent loop iterations on several threads; `@vectorize` turns a scalar function into a NumPy ufunc; `fastmath=True` permits reordering of floating-point operations (faster, but results change in the last digits).
- Random numbers inside compiled code come from Numba's own generator, with one state per thread, seeded inside compiled code (as above), not by NumPy's global seed.

Other routes to compiled speed serve different needs: Cython (Python with C type declarations, compiled ahead of time; good for wrapping C libraries), C++ extensions with pybind11 or nanobind (when the core is written in C++, [4.2](/4.2)), JAX (array programs compiled with XLA for CPU and GPU, with automatic differentiation), CuPy (a NumPy-compatible array library on NVIDIA GPUs), and PyPy (an alternative Python implementation with a tracing JIT, fast on pure-Python code but less compatible with C extensions). CPython itself contains an experimental JIT compiler since version 3.13; it is disabled by default and so far gives modest speed-ups, nothing comparable to Numba for numerical loops.

## 7.4. Parallelism

### 7.4.1. Processes, Threads and the GIL

A process is a running program with its own memory; a thread is a sequence of execution inside a process, sharing the memory of the process with its other threads ([4.11](/4.11)). Threads are cheap and communicate through shared objects; processes are isolated and must copy (serialize) data to exchange them. In CPython the choice between them is decided by one design element.

**Definition 7.4.1 (Global Interpreter Lock)** The **global interpreter lock** (GIL) of CPython is a mutual-exclusion lock that a thread must hold to execute Python bytecode. In a process with a GIL, at most one thread runs Python code at any moment.

The GIL makes the interpreter's internal state, above all the **reference counting** of every object (the basis of CPython's memory management and **garbage collection**, [4.2.12](/4.2.12)), safe without fine-grained locks, and it makes single-threaded code fast. Its consequence is that threads do not speed up CPU-bound Python code: in the measurement of §7.4.4, eight threads running the pure-Python Gillespie simulation took almost as long as one. Threads are still useful in two cases:

- I/O-bound work (downloads, database queries, reading many files): a thread waiting for I/O releases the GIL;
- calls into compiled code that release the GIL: NumPy, SciPy, scikit-learn, Numba (`@njit(nogil=True)`) and most compression and I/O libraries release it during long operations. Sorting 16 arrays of $4 \times 10^6$ floats took 1.2–1.6 s serially and 0.4–0.5 s with 8 threads.

Note that NumPy's linear algebra calls a multithreaded BLAS (OpenBLAS or MKL), which already uses all cores; running such calls in parallel threads or processes oversubscribes the machine and can be slower than serial execution. Environment variables such as `OMP_NUM_THREADS=1` (or the `threadpoolctl` package) limit the BLAS threads when parallelizing at a higher level.

### 7.4.2. Process Pools and joblib

Many computational tasks consist of independent pieces: simulation replicates, bootstrap resamples ([3.5.7](/3.5.7)), parameter sets, samples, chromosomes. A problem is *embarrassingly parallel* if it splits into tasks that need no communication with each other, only a final collection of the results. Such problems are parallelized with a *process pool*: a fixed set of worker processes that receive tasks from the parent, compute them and return the results.

```python
from concurrent.futures import ProcessPoolExecutor

from ssa import birth_death        # the function must be importable by the workers

if __name__ == "__main__":         # required: workers re-import the main module
    with ProcessPoolExecutor(max_workers=8) as pool:
        finals = list(pool.map(birth_death, range(32)))
```

Arguments and results are pickled and sent between processes, so the tasks should be coarse (seconds rather than microseconds each) and the data passed per task small; a large array is better written to a file, or shared via `multiprocessing.shared_memory`, than copied to every task. How the workers are created is the *start method*:

| Start method | How a worker starts | Default on |
|---|---|---|
| `fork` | copy of the parent process (memory shared copy-on-write) | Linux until Python 3.13 |
| `forkserver` | forked from a clean server process started early | Linux since Python 3.14 (and other POSIX systems except macOS) |
| `spawn` | fresh interpreter that imports the main module | Windows; macOS since Python 3.8 |

`fork` is fast but copies the state of all threads at the moment of the fork, which can deadlock when the parent runs threads (as libraries such as BLAS do); Python 3.12 started warning about forking a multithreaded process, and 3.14 changed the default on Linux to `forkserver`. Code that relied on workers inheriting global variables set up in the parent (configured loggers, data loaded at module level after the imports) behaves differently under the new default; explicit arguments, or `multiprocessing.get_context("fork")` where forking is known to be safe, fix it. Even under `fork`, CPython's **reference counting** writes to every object a worker touches, so the copy-on-write pages of the parent are gradually copied.

joblib, the parallel backend of scikit-learn, wraps this pattern in a compact API, uses the robust `loky` process pool by default (with cloudpickle, so that functions defined interactively in Jupyter also work), and adds a disk cache for expensive function calls (`joblib.Memory`):

```python
from joblib import Parallel, delayed

finals = Parallel(n_jobs=8)(delayed(birth_death)(seed) for seed in range(32))
```

Parallel random simulations need independent random streams. Using the seeds $0, 1, 2, \dots$ as above is common, but the reliable method with NumPy is to derive the streams from one seed, `rngs = np.random.default_rng(seed).spawn(n)` (or `np.random.SeedSequence(seed).spawn(n)`), and pass one generator or child seed to each task, so that the results are reproducible and do not depend on the number of workers ([4.4.3](/4.4.3), and **pseudorandom number generator** in [3.5.8](/3.5.8)).

### 7.4.3. Free-Threaded Python

PEP 703 (accepted in 2023) proposed to make the GIL optional, and CPython 3.13 shipped an experimental *free-threaded build*, a separate build of the interpreter (`python3.13t`) in which the GIL is disabled and threads execute Python code truly in parallel. Reference counts, the memory allocator (mimalloc), the garbage collector and the built-in containers were redesigned to be thread-safe without a global lock. PEP 779 set the criteria for the next phase, and in Python 3.14 (October 2025) the free-threaded build became officially supported, though still optional: the default interpreter keeps the GIL, and making the free-threaded build the default is a later phase without a fixed date. The free-threaded interpreter is selected by name (`python3.14t`; `uv python install 3.14t`), and `sys._is_gil_enabled()` reports whether the GIL is active.

On the free-threaded build, the measurement of §7.4.4 changes as expected: eight threads run the pure-Python simulation 4.2 times faster than one, slightly better than eight processes, because threads start faster and share memory. The single-threaded run is about 10 % slower than on the default build, the price of the thread-safe reference counting. Points to keep in mind:

- C extensions must be built for the free-threaded ABI. NumPy and much of the scientific stack provide such builds, but an extension that has not declared itself thread-safe re-enables the GIL for the whole process when imported (with a warning).
- Without the GIL, Python code that mutates shared objects from several threads can have race conditions that were masked before. Built-in containers stay internally consistent, but compound operations (`counts[k] += 1` from several threads) need a `threading.Lock` or a design in which each thread writes only its own data.
- Python 3.14 also added `concurrent.interpreters` (PEP 734) and `InterpreterPoolExecutor`: several interpreters in one process, each with its own GIL, a middle ground between threads and processes.

For scientific code in 2026, process pools remain the robust default for CPU-bound pure-Python work; free-threading is ready for experiments and for code whose dependencies support it, and it will matter more as the ecosystem follows.

### 7.4.4. Measured Comparison and Amdahl's Law

32 independent runs of the pure-Python Gillespie simulation of §7.2, with 8 workers each:

| Strategy | Default build (GIL) | Free-threaded build |
|---|---|---|
| serial loop | 3.73 s | 4.14 s |
| `ThreadPoolExecutor`, 8 threads | 3.41 s | 0.99 s |
| `ProcessPoolExecutor`, 8 processes | 1.07 s | 1.32 s |
| joblib (`loky`), 8 processes | 1.46 s | 1.75 s |
| Numba, compiled, `prange` on 8 threads (§7.3) | 0.08 s | — |

The times include starting the workers, which is part of the price of processes and explains why eight workers give a speed-up of about 3.5 rather than 8 (the laptop's eight cores are also of two kinds, four performance and four efficiency cores). The comparison carries the main lessons of this chapter: parallel threads help Python code only without the GIL; processes help but pay for starting and communicating; compiling the inner loop gains more than parallelizing it, and the two combine.

Parallelism also has a limit that no hardware removes. If a fraction $f$ of the running time can be parallelized and the rest is serial, then with $p$ workers the time is at best $(1 - f) + f/p$ of the original, so the speed-up is

$$
S(p) = \frac{1}{(1 - f) + f/p} \le \frac{1}{1 - f}.
$$

This bound is *Amdahl's law*: with $f = 0.9$, no number of workers achieves more than a tenfold speed-up, and 8 workers give at most $4.7$. The serial part (reading input, combining results, starting workers) therefore deserves as much attention as the parallel one.

## 7.5. Choosing a Strategy

1. Measure: time the whole program, profile it, and find the part that dominates.
2. Use a better algorithm or library: a lower complexity, a vectorized NumPy or pandas operation, a SciPy routine, a sparse matrix. This is usually the largest gain.
3. Compile what cannot be vectorized: Numba for numerical loops over arrays; Cython or C++ for larger components.
4. Parallelize independent tasks: a process pool or joblib for CPU-bound Python code; threads for I/O and for code that releases the GIL; free-threaded Python where the dependencies support it; a cluster scheduler or a workflow manager (Snakemake, Nextflow) when the tasks are whole programs on many samples.
5. Check after every step that the results are unchanged and that the gain is real on the machine where the code runs.

## Summary

- Measure before optimizing: `timeit` for snippets, `cProfile` and `line_profiler` for where the time goes, sampling profilers (`py-spy`, Scalene, `profiling.sampling` in Python 3.15) for running programs with low overhead.
- Vectorization moves loops into compiled code; its limits are temporary arrays and inherently sequential algorithms such as the Gillespie simulation.
- Numba compiles numerical Python functions just in time; plain loops in `@njit` functions run at the speed of C, and `prange` parallelizes them.
- The GIL lets only one thread run Python bytecode at a time: threads help with I/O and with compiled code that releases the GIL, process pools help with CPU-bound Python code.
- Process pools pickle tasks and results; keep tasks coarse, guard the main module, and know the start method (`forkserver` by default on Linux since Python 3.14).
- Embarrassingly parallel problems need independent random streams (`SeedSequence.spawn`) for reproducible results.
- Free-threaded CPython (officially supported since 3.14, still optional) runs threads in parallel, at a small single-thread cost and with new responsibilities for thread safety.
- Amdahl's law bounds the speed-up by the serial fraction of the work.
