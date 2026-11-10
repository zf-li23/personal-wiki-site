"""Boundary bias at a hard boundary: 500 observations from Exp(1). The kernel estimate leaks
mass below 0 and is about half the true density at the origin; the local linear estimate
(computed from finely binned data on [0, inf)) removes most of the bias at the boundary."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 500
x = rng.exponential(1.0, n)
h = 0.3
grid = np.linspace(-1, 4, 501)


def kde(t, data, h):
    u = (t[:, None] - data[None, :]) / h
    return np.exp(-u**2 / 2).sum(axis=1) / (len(data) * h * np.sqrt(2 * np.pi))


def local_linear_density(t, data, h, delta=0.02):
    edges = np.arange(0.0, data.max() + 2 * delta, delta)    # bins start at the boundary
    counts, _ = np.histogram(data, bins=edges)
    centers = (edges[:-1] + edges[1:]) / 2
    heights = counts / (len(data) * delta)
    out = np.empty_like(t)
    for j, t0 in enumerate(t):
        d = centers - t0
        w = np.exp(-(d / h) ** 2 / 2)
        s0, s1, s2 = w.sum(), (w * d).sum(), (w * d * d).sum()
        out[j] = ((s2 * w - s1 * w * d) * heights).sum() / (s0 * s2 - s1**2)
    return out


pos = grid[grid >= 0]
fig, ax = plt.subplots(figsize=(7.8, 4.4))
ax.plot(pos, np.exp(-pos), color="0.2", lw=1.4, ls="--", label="true density Exp(1)")
ax.plot(grid, kde(grid, x, h), color="C0", lw=1.8, label=f"kernel estimate, h = {h}")
ax.plot(pos, local_linear_density(pos, x, h), color="C3", lw=1.8,
        label=f"local linear estimate, h = {h}")
ax.axvline(0, color="0.5", lw=0.8)
ax.plot(x, np.full_like(x, -0.03), "|", color="0.4", ms=5, alpha=0.4)
ax.annotate("mass leaked below 0", xy=(-0.25, 0.2), xytext=(-0.95, 0.55), fontsize=8,
            arrowprops=dict(arrowstyle="->", color="0.4"))
ax.set_xlim(-1, 4)
ax.set_ylim(-0.06, 1.15)
ax.set_xlabel("x")
ax.set_ylabel("density")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)
fig.tight_layout()
