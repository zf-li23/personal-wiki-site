"""Vascular graft experiment (RCBD): yield by extrusion pressure, one profile per resin batch."""

import numpy as np
import matplotlib.pyplot as plt

psi = [8500, 8700, 8900, 9100]
# Rows: pressure; columns: resin batch (block) 1-6
y = np.array([[90.3, 89.2, 98.2, 93.9, 87.4, 97.9],
              [92.5, 89.5, 90.6, 94.7, 87.0, 95.8],
              [85.5, 90.8, 89.6, 86.2, 88.0, 93.4],
              [82.5, 89.5, 85.6, 87.4, 78.9, 90.7]])
a, b = y.shape

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2))
ax = axes[0]
for j in range(b):
    ax.plot(psi, y[:, j], marker="o", ms=4, lw=1, alpha=0.75, label=f"batch {j + 1}")
ax.plot(psi, y.mean(axis=1), "D-", color="black", ms=7, lw=2.2, label="pressure mean")
ax.set_xticks(psi)
ax.set_xlabel("extrusion pressure (psi)")
ax.set_ylabel("yield (%)")
ax.set_title("Profiles of the six batches")
ax.legend(fontsize=8, ncol=2)

ax = axes[1]
markers = ["o", "s", "^", "v"]
for i in range(a):
    ax.scatter(np.arange(1, b + 1) + (i - 1.5) * 0.08, y[i], marker=markers[i], s=30,
               label=f"{psi[i]} psi")
ax.plot(np.arange(1, b + 1), y.mean(axis=0), "_", color="black", ms=26, mew=2.2,
        label="batch mean")
ax.axhline(y.mean(), color="gray", ls="--", lw=1)
ax.set_xticks(np.arange(1, b + 1))
ax.set_xlabel("batch of resin (block)")
ax.set_ylabel("yield (%)")
ax.set_title("Variation between batches")
ax.legend(fontsize=8, ncol=2)
for ax in axes:
    ax.grid(alpha=0.3)
fig.tight_layout()
