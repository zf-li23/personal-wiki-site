"""Four kinds of distribution functions: discrete, continuous, mixed, and the singular Cantor function."""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(11, 7.5))

ax = axes[0, 0]
xs = np.array([1, 2, 3, 4])
ps = np.array([0.2, 0.5, 0.2, 0.1])
F = np.cumsum(ps)
edges = np.concatenate(([-0.5], xs, [5.5]))
levels = np.concatenate(([0], F))
for i in range(len(levels)):
    ax.plot([edges[i], edges[i + 1]], [levels[i], levels[i]], color="C0", lw=2)
ax.plot(xs, F, "o", color="C0")
ax.plot(xs, levels[:-1], "o", mfc="none", color="C0")
ax.set_title("Discrete: jumps p_k at x_k (right-continuous)")

ax = axes[0, 1]
x = np.linspace(-0.5, 5.5, 400)
a, b = 1, 4
ax.plot(x, np.clip((x - a) / (b - a), 0, 1), color="C0", lw=2, label="U(1, 4)")
ax.plot(x, np.clip((x - a) / (b - a), 0, 1) ** 2, color="C1", lw=2, label="density 2(x - 1)/9 on (1, 4)")
ax.legend(fontsize=8)
ax.set_title("Continuous: F(x) = integral of f")

ax = axes[1, 0]
x1 = np.linspace(-0.5, 0.5, 100)
x2 = np.linspace(0.5, 1.5, 100)
F1 = np.clip(x1, 0, 1) / 2
F2 = 0.5 + np.clip(x2, 0, 1) / 2
ax.plot(x1, F1, color="C0", lw=2)
ax.plot(x2, F2, color="C0", lw=2)
ax.plot([0.5], [0.25], "o", mfc="none", color="C0")
ax.plot([0.5], [0.75], "o", color="C0")
ax.set_title("Mixed: 0.5 w.p. 1/2, otherwise U(0, 1)")


def cantor(x, depth=30):
    x = np.clip(x, 0, 1)
    out = np.zeros_like(x)
    scale = 0.5
    y = x.copy()
    done = np.zeros_like(x, dtype=bool)
    for _ in range(depth):
        y3 = y * 3
        digit = np.floor(y3)
        mid = (digit == 1) & ~done
        out[mid] += scale
        done |= mid
        two = (digit >= 2) & ~done
        out[two] += scale
        y = np.where(done, y, y3 - digit)
        scale /= 2
    return out


ax = axes[1, 1]
x = np.linspace(-0.05, 1.05, 4000)
ax.plot(x, cantor(x), color="C0", lw=1.5)
ax.set_title("Singular: Cantor function (continuous, F' = 0 a.e.)")
for ax in axes.flat:
    ax.set_xlabel("x")
    ax.set_ylabel("F(x)")
    ax.set_ylim(-0.05, 1.05)
fig.tight_layout()
