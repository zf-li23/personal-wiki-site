"""Run time of three ways to fill a vector of n results: growing it inside a loop, filling a preallocated vector, and one vectorized call."""

import time

import numpy as np
import matplotlib.pyplot as plt


def grow(x):
    out = np.empty(0)
    for v in x:
        out = np.append(out, v * v)  # copies the whole vector every time, like x <- c(x, y) in R
    return out


def prealloc(x):
    out = np.empty(len(x))
    for i, v in enumerate(x):
        out[i] = v * v
    return out


def vectorized(x):
    return x * x


def best_time(f, x, reps=3):
    best = np.inf
    for _ in range(reps):
        t0 = time.perf_counter()
        f(x)
        best = min(best, time.perf_counter() - t0)
    return best


ns = np.unique(np.logspace(2, 5, 10).astype(int))
rng = np.random.default_rng(0)
times = {"grow inside the loop": [], "preallocated loop": [], "vectorized": []}
for n in ns:
    x = rng.random(n)
    times["grow inside the loop"].append(best_time(grow, x, reps=1 if n > 20000 else 3))
    times["preallocated loop"].append(best_time(prealloc, x))
    times["vectorized"].append(best_time(vectorized, x))

fig, ax = plt.subplots(figsize=(7.5, 4.8))
for (name, t), m in zip(times.items(), ["o", "s", "^"]):
    ax.loglog(ns, t, marker=m, ms=5, lw=1.2, label=name)
ref = np.array([ns[0], ns[-1]], dtype=float)
ax.loglog(ref, times["preallocated loop"][0] * (ref / ref[0]), color="0.5", ls=":", lw=1, label="slope 1 (linear)")
ax.loglog(ref, times["grow inside the loop"][-1] * (ref / ref[-1]) ** 2, color="0.5", ls="--", lw=1, label="slope 2 (quadratic)")
ax.set_xlabel("vector length n")
ax.set_ylabel("seconds (best of repeated runs)")
ax.set_title("Computing x_i^2 for i = 1, ..., n: growing a vector costs O(n^2) copies", fontsize=10)
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3, which="both")
fig.tight_layout()
