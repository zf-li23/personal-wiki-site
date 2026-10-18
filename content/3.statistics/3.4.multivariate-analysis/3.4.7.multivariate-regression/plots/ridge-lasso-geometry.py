"""Lasso (l1 ball) versus ridge (l2 ball): first contact of the RSS ellipses with the constraint region."""

import numpy as np
import matplotlib.pyplot as plt

G = np.array([[1.0, 0.45], [0.45, 0.7]])  # X^T X
bhat = np.array([1.6, 0.75])  # OLS estimate
t = 1.0


def q(b):
    d = b - bhat
    return np.einsum("...i,ij,...j->...", d, G, d)


theta = np.linspace(0, 2 * np.pi, 20001)
circle = np.column_stack([np.cos(theta), np.sin(theta)])
diamond = circle / (np.abs(circle).sum(axis=1, keepdims=True))
grid = np.linspace(-1.5, 3.0, 400)
B1, B2 = np.meshgrid(grid, grid)
Q = q(np.stack([B1, B2], axis=-1))

fig, axes = plt.subplots(1, 2, figsize=(11, 5.2))
for ax, region, name in [(axes[0], diamond, "Lasso: |b1| + |b2| <= t"), (axes[1], circle * np.sqrt(t), "Ridge: b1^2 + b2^2 <= t")]:
    vals = q(region)
    best = region[np.argmin(vals)]
    c0 = vals.min()
    ax.contour(B1, B2, Q, levels=[c0, 2.2 * c0, 4 * c0], colors=["C0", "C0", "C0"], linewidths=[1.6, 1.0, 1.0])
    ax.fill(region[:, 0], region[:, 1], color="C1", alpha=0.25)
    ax.plot(region[:, 0], region[:, 1], color="C1", lw=1.5)
    ax.plot(*bhat, "o", color="C0")
    ax.annotate("OLS estimate", bhat, xytext=(8, 8), textcoords="offset points", color="C0")
    ax.plot(*best, "o", color="C3", ms=7)
    ax.annotate(f"solution ({best[0]:.2f}, {best[1]:.2f})", best, xytext=(10, -18), textcoords="offset points", color="C3")
    ax.axhline(0, color="0.5", lw=0.8)
    ax.axvline(0, color="0.5", lw=0.8)
    ax.set_aspect("equal")
    ax.set_xlim(-1.5, 3.0)
    ax.set_ylim(-1.5, 2.2)
    ax.set_xlabel("b1")
    ax.set_ylabel("b2")
    ax.set_title(name)
fig.tight_layout()
