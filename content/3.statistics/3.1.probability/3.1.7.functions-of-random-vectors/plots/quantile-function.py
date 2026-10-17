"""A distribution function with a jump and a flat part, and its generalized inverse (quantile function)."""

import numpy as np
import matplotlib.pyplot as plt


def F(x):
    # continuous on [0,1): F = 0.4 x; jump of 0.3 at x = 1; flat on [1, 2); then linear to 1 on [2, 3]
    x = np.asarray(x, dtype=float)
    out = np.where(x < 0, 0.0, 0.4 * x)
    out = np.where(x >= 1, 0.7, out)
    out = np.where(x >= 2, 0.7 + 0.3 * (x - 2), out)
    return np.clip(out, 0, 1)


def Finv(p):
    p = np.asarray(p, dtype=float)
    return np.where(p <= 0.4, p / 0.4, np.where(p <= 0.7, 1.0, 2 + (p - 0.7) / 0.3))


fig, axes = plt.subplots(1, 2, figsize=(10, 4))
ax = axes[0]
for a, b in [(-0.5, 0.999), (1.0, 3.5)]:
    xs = np.linspace(a, b, 300)
    ax.plot(xs, F(xs), color="C0", lw=2)
ax.plot([1], [0.4], "o", mfc="none", mec="C0")
ax.plot([1], [0.7], "o", color="C0")
ax.axhline(0.55, color="C3", ls=":", lw=1)
ax.text(-0.45, 0.58, "p = 0.55", color="C3", fontsize=8)
ax.set_xlabel("x")
ax.set_ylabel("F(x)")
ax.set_title("distribution function F")
ax.grid(alpha=0.3)

ax = axes[1]
for a, b in [(0.001, 0.4), (0.4001, 0.7), (0.7001, 0.999)]:
    ps = np.linspace(a, b, 200)
    ax.plot(ps, Finv(ps), color="C1", lw=2)
ax.plot([0.7], [1.0], "o", color="C1")
ax.plot([0.7], [2.0], "o", mfc="none", mec="C1")
ax.axvline(0.55, color="C3", ls=":", lw=1)
ax.set_xlabel("p")
ax.set_ylabel("F^{-1}(p)")
ax.set_title("quantile function: left-continuous, jumps where F is flat")
ax.grid(alpha=0.3)
fig.tight_layout()
