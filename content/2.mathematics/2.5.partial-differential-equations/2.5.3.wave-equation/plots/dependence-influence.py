"""Domain of dependence, domain of determinacy and range of influence for u_tt = c^2 u_xx."""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(11, 3.8), sharey=True)
c = 1.0
T = 2.0

ax = axes[0]
x0, t0 = 0.0, 1.5
ax.fill([x0 - c * t0, x0 + c * t0, x0], [0, 0, t0], color="C0", alpha=0.25)
ax.plot([x0 - c * t0, x0, x0 + c * t0], [0, t0, 0], color="C0", lw=1.8)
ax.plot([x0 - c * t0, x0 + c * t0], [0, 0], color="C3", lw=4, label="[x0 - c t0, x0 + c t0]")
ax.plot([x0], [t0], "o", color="C0")
ax.text(x0 + 0.1, t0 + 0.08, "(x0, t0)", fontsize=9)
ax.set_title("Domain of dependence")
ax.legend(loc="upper right", fontsize=8)

ax = axes[1]
a, b = -1.5, 1.5
ax.fill([a, b, (a + b) / 2], [0, 0, (b - a) / (2 * c)], color="C2", alpha=0.25)
ax.plot([a, (a + b) / 2, b], [0, (b - a) / (2 * c), 0], color="C2", lw=1.8)
ax.plot([a, b], [0, 0], color="C3", lw=4, label="[a, b]")
ax.text(a, 1.15, "x - ct = a", fontsize=9, color="C2")
ax.text(0.45, 1.15, "x + ct = b", fontsize=9, color="C2")
ax.set_title("Domain of determinacy")
ax.legend(loc="upper right", fontsize=8)

ax = axes[2]
a, b = -0.5, 0.5
ax.fill([a, b, b + c * T, a - c * T], [0, 0, T, T], color="C1", alpha=0.25)
ax.plot([a - c * T, a], [T, 0], color="C1", lw=1.8)
ax.plot([b, b + c * T], [0, T], color="C1", lw=1.8)
ax.plot([a, b], [0, 0], color="C3", lw=4, label="[a, b]")
ax.text(-1.3, 1.0, "x = a - ct", fontsize=9, color="C1", ha="left")
ax.text(1.3, 1.0, "x = b + ct", fontsize=9, color="C1", ha="right")
ax.set_title("Range of influence")
ax.legend(loc="upper right", fontsize=8)

for ax in axes:
    ax.set_xlim(-2.6, 2.6)
    ax.set_ylim(0, T)
    ax.set_xlabel("x")
axes[0].set_ylabel("t")
fig.tight_layout()
