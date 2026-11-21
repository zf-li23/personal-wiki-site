"""Adaptive rejection sampling: tangent (upper) and chord (lower) hulls of a log-concave density."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gammaln

a = 4.0                                   # target: Gamma(4, 1), log-concave


def h(x):
    return (a - 1) * np.log(x) - x - gammaln(a)


def dh(x):
    return (a - 1) / x - 1


def hulls(xs, grid):
    # upper hull: minimum of the tangents; lower hull: chords between neighbors, -inf outside
    tang = np.array([h(t) + dh(t) * (grid - t) for t in xs])
    upper = tang.min(axis=0)
    lower = np.full_like(grid, -np.inf)
    for t0, t1 in zip(xs[:-1], xs[1:]):
        inside = (grid >= t0) & (grid <= t1)
        lower[inside] = h(t0) + (h(t1) - h(t0)) * (grid[inside] - t0) / (t1 - t0)
    return upper, lower


grid = np.linspace(0.05, 14, 2000)
dx = grid[1] - grid[0]
fig, axes = plt.subplots(1, 3, figsize=(13, 4.0))
for k, (ax, xs, log_scale) in enumerate(zip(axes, [[1.0, 3.0, 7.0], [1.0, 3.0, 7.0], [0.8, 1.6, 3.0, 4.5, 7.0, 10.0]], [True, False, False])):
    xs = np.array(xs)
    upper, lower = hulls(xs, grid)
    if log_scale:
        ax.plot(grid, h(grid), color="C0", lw=1.8, label="log target h(x)")
        ax.plot(grid, upper, color="C3", lw=1.3, ls="--", label="upper hull (tangents)")
        ax.plot(grid, lower, color="C2", lw=1.3, ls=":", label="lower hull (chords)")
        ax.plot(xs, h(xs), "ko", ms=4)
        ax.set_ylim(-9, 0)
        ax.set_title("log scale, 3 abscissae", fontsize=11)
    else:
        accept = np.sum(np.exp(h(grid))) / np.sum(np.exp(upper))
        squeeze = np.sum(np.exp(lower)) / np.sum(np.exp(h(grid)))
        ax.fill_between(grid, np.exp(upper), color="C3", alpha=0.15)
        ax.plot(grid, np.exp(h(grid)), color="C0", lw=1.8, label="target f(x)")
        ax.plot(grid, np.exp(upper), color="C3", lw=1.3, ls="--", label="envelope exp(upper)")
        ax.plot(grid, np.exp(lower), color="C2", lw=1.3, ls=":", label="squeeze exp(lower)")
        ax.plot(xs, np.exp(h(xs)), "ko", ms=4)
        ax.set_ylim(0, 0.32)
        ax.set_title(f"{len(xs)} abscissae: acceptance {accept:.2f}, squeeze {squeeze:.2f}", fontsize=11)
    ax.set_xlim(0, 14)
    ax.set_xlabel("x")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
fig.tight_layout()
