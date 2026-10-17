"""Gaussian kernel density estimates of an N(0, 1) sample for three bandwidths."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
x = rng.standard_normal(100)
grid = np.linspace(-4, 4, 801)
true = np.exp(-grid**2 / 2) / np.sqrt(2 * np.pi)

iqr = np.subtract(*np.percentile(x, [75, 25]))
h_ref = 0.9 * min(x.std(ddof=1), iqr / 1.34) * len(x) ** (-0.2)


def kde(points, data, h):
    u = (points[:, None] - data[None, :]) / h
    return np.exp(-u**2 / 2).sum(axis=1) / (len(data) * h * np.sqrt(2 * np.pi))


fig, axes = plt.subplots(1, 3, figsize=(12, 3.6), sharey=True)
for ax, h, col in zip(axes, [0.05, h_ref, 2.0], ["C3", "C0", "C2"]):
    ax.plot(grid, true, "--", color="0.5", lw=1.2, label="true density")
    ax.plot(grid, kde(grid, x, h), color=col, lw=2, label="kernel estimate")
    ax.plot(x, np.full_like(x, -0.02), "|", color="0.3", ms=8)
    ax.set_title(f"h = {h:.2f}")
    ax.set_xlabel("x")
    ax.set_ylim(-0.05, 0.75)
axes[0].set_ylabel("density")
axes[0].legend(frameon=False, loc="upper left")
fig.tight_layout()
