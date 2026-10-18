"""Mallows' Cp for all subsets of six simulated candidate predictors (three relevant)."""

import itertools
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n, k = 60, 6
cov = 0.3 * np.ones((k, k)) + 0.7 * np.eye(k)
Z = rng.multivariate_normal(np.zeros(k), cov, size=n)
y = 1 + 1.0 * Z[:, 0] + 0.8 * Z[:, 1] + 0.6 * Z[:, 2] + rng.normal(0, 1, n)


def sse(cols):
    X = np.column_stack([np.ones(n)] + [Z[:, j] for j in cols])
    b = np.linalg.lstsq(X, y, rcond=None)[0]
    r = y - X @ b
    return r @ r


P = k + 1
mse_full = sse(range(k)) / (n - P)
fig, ax = plt.subplots(figsize=(8, 5))
best = None
for size in range(0, k + 1):
    for cols in itertools.combinations(range(k), size):
        p = size + 1
        cp = sse(cols) / mse_full - (n - 2 * p)
        relevant = {0, 1, 2} <= set(cols)
        ax.plot(p, cp, "o", color="C2" if relevant else "C0", ms=6, alpha=0.8)
        if best is None or cp < best[0]:
            best = (cp, p, cols)
grid = np.array([1, P])
ax.plot(grid, grid, color="0.3", ls="--", lw=1.2, label="Cp = p")
ax.plot([], [], "o", color="C2", label="contains all relevant predictors")
ax.plot([], [], "o", color="C0", label="misses a relevant predictor")
cp, p, cols = best
ax.annotate("smallest Cp: X" + ", X".join(str(j + 1) for j in cols), xy=(p, cp),
            xytext=(p + 0.6, cp + 25), arrowprops=dict(arrowstyle="->"))
ax.set_yscale("log")
ax.set_xlabel("number of parameters p")
ax.set_ylabel("Mallows' Cp")
ax.set_title("All 64 subsets: biased models lie far above the line Cp = p")
ax.legend(fontsize=9, loc="upper right")
ax.grid(alpha=0.3)
fig.tight_layout()
