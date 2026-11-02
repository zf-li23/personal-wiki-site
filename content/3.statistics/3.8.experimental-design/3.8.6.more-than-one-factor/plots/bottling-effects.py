"""Soft drink bottling: main effect plots and two-factor interaction plots."""

import numpy as np
import matplotlib.pyplot as plt

carb = [10, 12, 14]
press = [25, 30]
speed = [200, 250]
# y[carbonation][pressure][speed] -> two replicates
y = np.zeros((3, 2, 2, 2))
data = {(0, 0, 0): [-3, -1], (0, 0, 1): [-1, 0], (0, 1, 0): [-1, 0], (0, 1, 1): [1, 1],
        (1, 0, 0): [0, 1], (1, 0, 1): [2, 1], (1, 1, 0): [2, 3], (1, 1, 1): [6, 5],
        (2, 0, 0): [5, 4], (2, 0, 1): [7, 6], (2, 1, 0): [7, 9], (2, 1, 1): [10, 11]}
for k, v in data.items():
    y[k] = v

fig, axes = plt.subplots(2, 3, figsize=(13, 7), sharey=True)
mains = [("Percent carbonation (A)", carb, y.mean((1, 2, 3)), 0),
         ("Pressure (B)", press, y.mean((0, 2, 3)), 1),
         ("Line speed (C)", speed, y.mean((0, 1, 3)), 2)]
for ax, (title, lev, m, axis) in zip(axes[0], mains):
    obs = np.moveaxis(y, axis, 0).reshape(len(lev), -1)
    for i, v in enumerate(lev):
        ax.scatter([i] * obs.shape[1], obs[i], s=14, alpha=0.5, color="C0")
    ax.plot(range(len(lev)), m, "o-", color="C3", lw=1.8)
    ax.set_xticks(range(len(lev)))
    ax.set_xticklabels([str(v) for v in lev])
    ax.set_title(title)

ab = y.mean((2, 3))
ac = y.mean((1, 3))
bc = y.mean((0, 3))
ax = axes[1, 0]
for j, ls in enumerate(["-", "--"]):
    ax.plot(range(3), ab[:, j], ls=ls, marker="o", label=f"pressure {press[j]}")
ax.set_xticks(range(3)); ax.set_xticklabels([str(v) for v in carb])
ax.set_title("Interaction of A and B")
ax = axes[1, 1]
for k, ls in enumerate(["-", "--"]):
    ax.plot(range(2), bc[:, k], ls=ls, marker="o", label=f"speed {speed[k]}")
ax.set_xticks(range(2)); ax.set_xticklabels([str(v) for v in press])
ax.set_title("Interaction of B and C")
ax = axes[1, 2]
for k, ls in enumerate(["-", "--"]):
    ax.plot(range(3), ac[:, k], ls=ls, marker="o", label=f"speed {speed[k]}")
ax.set_xticks(range(3)); ax.set_xticklabels([str(v) for v in carb])
ax.set_title("Interaction of A and C")
for ax in axes[1]:
    ax.legend(fontsize=8)
for ax in axes.ravel():
    ax.grid(alpha=0.3)
axes[0, 0].set_ylabel("fill height deviation")
axes[1, 0].set_ylabel("mean deviation")
fig.tight_layout()
