"""Run time of the sum of squares of n numbers: a Python loop over a list,
the built-in sum over a generator, and NumPy, measured on the build machine."""

import timeit

import numpy as np
import matplotlib.pyplot as plt


def best_time(func, target=0.05):
    """Best of 3 runs of `func`, each repeated until it takes about `target` s."""
    number = 1
    while timeit.timeit(func, number=number) < target / 10 and number < 10**6:
        number *= 10
    return min(timeit.repeat(func, number=number, repeat=3)) / number


def py_loop(xs):
    s = 0.0
    for v in xs:
        s += v * v
    return s


sizes = np.unique(np.logspace(1, 6, 11).astype(int))
results = {"Python for loop": [], "sum() over a generator": [], "NumPy (x * x).sum()": []}
for n in sizes:
    xs = [float(i) for i in range(n)]
    x = np.array(xs)
    results["Python for loop"].append(best_time(lambda: py_loop(xs)))
    results["sum() over a generator"].append(best_time(lambda: sum(v * v for v in xs)))
    results["NumPy (x * x).sum()"].append(best_time(lambda: (x * x).sum()))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
for (label, t), color in zip(results.items(), ["C3", "C1", "C0"]):
    t = np.array(t)
    ax1.loglog(sizes, t, "o-", color=color, ms=4, label=label)
    ax2.semilogx(sizes, t / sizes * 1e9, "o-", color=color, ms=4, label=label)
ax1.set_xlabel("n")
ax1.set_ylabel("time (s)")
ax1.set_title("total time")
ax1.grid(alpha=0.3, which="both")
ax1.legend()
ax2.set_yscale("log")
ax2.set_xlabel("n")
ax2.set_ylabel("time per element (ns)")
ax2.set_title("time per element: fixed overhead vs per-element cost")
ax2.grid(alpha=0.3, which="both")
fig.tight_layout()
