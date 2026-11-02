"""One-factor-at-a-time versus a full factorial design on a response surface with interaction."""

import numpy as np
import matplotlib.pyplot as plt

g = np.linspace(0, 1, 200)
A, B = np.meshgrid(g, g)
# response with a strong A x B interaction; the optimum is at low A and high B
Y = 50 + 10 * A + 20 * B - 40 * A * B

levels = [0, 0.5, 1]
fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.0), sharey=True)
for ax in axes:
    cs = ax.contour(A, B, Y, levels=np.arange(42, 72, 4), colors="gray", linewidths=0.8)
    ax.clabel(cs, fontsize=7, fmt="%d")
    ax.plot(0, 1, "*", ms=16, color="C3", label="true optimum (Y = 70)")
    ax.set_xlabel("factor A")
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 1.1)
axes[0].set_ylabel("factor B")

# OFAT: vary A with B at its baseline, keep the best A (high), then vary B there
pts = [(v, 0.0) for v in levels] + [(1.0, v) for v in levels[1:]]
ax = axes[0]
ax.plot(*zip(*pts), "o", ms=8, color="C0", label="OFAT runs (a + b - 1 = 5)")
ax.plot(1, 0, "D", ms=11, mfc="none", color="C1", mew=2, label="OFAT choice (Y = 60)")
ax.set_title("One factor at a time")
ax.legend(fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2)

ax = axes[1]
grid_pts = [(u, v) for u in levels for v in levels]
ax.plot(*zip(*grid_pts), "o", ms=8, color="C0", label="factorial runs (ab = 9)")
ax.set_title("Full factorial design")
ax.legend(fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2)
fig.tight_layout()
