"""Boundary bias of kernel regression: Nadaraya-Watson (local constant) and local linear fits
with tricube weights (LOESS, span 0.25, degree 1) for the simulated temperature series, compared
with the smooth trend; the right panel enlarges the first 25 years."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
x = np.linspace(1900, 2025, 80)
trend = 14 + 1.2 * (x - 1900) / (40 + (x - 1900))
y = trend + 0.15 * np.sin(x / 2) + rng.normal(0, 0.08, len(x))


def nw(x0, sd):
    w = np.exp(-((x0[:, None] - x[None, :]) / sd) ** 2 / 2)
    return (w * y).sum(axis=1) / w.sum(axis=1)


def loess(x0, span=0.25):
    q = int(np.ceil(span * len(x)))
    out = np.empty_like(x0)
    for j, t in enumerate(x0):
        d = np.abs(x - t)
        dq = np.sort(d)[q - 1]
        w = np.clip(1 - (d / dq) ** 3, 0, None) ** 3
        X = np.column_stack([np.ones_like(x), x - t])
        beta = np.linalg.solve(X.T @ (w[:, None] * X), X.T @ (w * y))
        out[j] = beta[0]
    return out


grid = np.linspace(1900, 2025, 400)
sd = 0.25 * 15 / 0.6745
fits = [(nw(grid, sd), "C0", "Nadaraya-Watson (local constant)"),
        (loess(grid), "C3", "local linear, tricube (LOESS)")]
fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), gridspec_kw={"width_ratios": [1.6, 1]})
for ax, (lo, hi) in zip(axes, [(1900, 2025), (1900, 1925)]):
    m = (x >= lo) & (x <= hi)
    g = (grid >= lo) & (grid <= hi)
    ax.plot(x[m], y[m], "o", color="0.55", ms=3.5)
    ax.plot(grid[g], (14 + 1.2 * (grid - 1900) / (40 + grid - 1900))[g],
            color="0.2", ls=":", lw=1.2, label="smooth trend (without the oscillation)")
    for fit, color, label in fits:
        ax.plot(grid[g], fit[g], color=color, lw=1.8, label=label)
    ax.set_xlabel("year")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("annual mean temperature / °C")
axes[0].set_title("A. whole series", fontsize=10)
axes[1].set_title("B. left boundary", fontsize=10)
axes[0].legend(fontsize=8, loc="upper left")
fig.tight_layout()
