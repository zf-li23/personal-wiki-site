"""The four kinds of discontinuity at x = 0: removable, jump, infinite, oscillating."""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 4, figsize=(13, 3.4))
left = np.linspace(-1, -1e-4, 4000)
right = np.linspace(1e-4, 1, 4000)

ax = axes[0]
for x in (left, right):
    ax.plot(x, np.sin(3 * x) / x, color="C0", lw=2)
ax.plot([0], [3], "o", ms=7, mfc="none", mec="C0", mew=1.5)
ax.plot([0], [1.5], "o", ms=6, color="C0")
ax.set_title("Removable: $\\sin 3x / x$, $f(0) = 1.5$", fontsize=10)
ax.set_ylim(-0.5, 3.6)

ax = axes[1]
ax.plot(left, -1 + 0.5 * left, color="C0", lw=2)
ax.plot(right, 1 + 0.5 * right, color="C0", lw=2)
ax.plot([0], [-1], "o", ms=7, mfc="none", mec="C0", mew=1.5)
ax.plot([0], [1], "o", ms=6, color="C0")
ax.set_title("Jump: left and right limits differ", fontsize=10)
ax.set_ylim(-1.8, 1.8)

ax = axes[2]
ax.plot(left[left < -0.08], 1 / left[left < -0.08], color="C0", lw=2)
ax.plot(right[right > 0.08], 1 / right[right > 0.08], color="C0", lw=2)
ax.set_title("Infinite: $1/x$", fontsize=10)
ax.set_ylim(-12, 12)

ax = axes[3]
x = np.linspace(-1, 1, 40001)
x = x[x != 0]
ax.plot(x, np.sin(1 / x), color="C0", lw=0.6)
ax.set_title("Oscillating: $\\sin(1/x)$", fontsize=10)
ax.set_ylim(-1.4, 1.4)

for ax in axes:
    ax.axhline(0, color="0.8", lw=0.8)
    ax.axvline(0, color="0.8", lw=0.8, ls="--")
    ax.set_xlim(-1, 1)
    ax.set_xticks([-1, 0, 1])
fig.text(0.27, 0.01, "first kind: both one-sided limits exist", ha="center", fontsize=10)
fig.text(0.76, 0.01, "second kind: some one-sided limit does not exist", ha="center", fontsize=10)
fig.tight_layout(rect=(0, 0.05, 1, 1))
