"""Golf experiment (GCBD): mean driving distance of each golfer at the three tee heights."""

import numpy as np
import matplotlib.pyplot as plt

# Rows: golfer (block) 1-9; columns: tee height 1-3; each entry is the mean of 5 drives
cell = np.array([[143.18, 141.64, 147.40], [173.18, 176.14, 188.04],
                 [141.64, 147.40, 143.18], [176.10, 178.04, 175.72],
                 [204.68, 213.20, 226.26], [137.10, 148.56, 146.70],
                 [171.18, 166.46, 173.14], [168.88, 187.38, 176.06],
                 [227.18, 241.72, 242.04]])
height = [1, 2, 3]

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
ax = axes[0]
for j, row in enumerate(cell):
    ax.plot(height, row, marker="o", ms=4, lw=1, alpha=0.8, label=f"golfer {j + 1}")
ax.plot(height, cell.mean(axis=0), "D-", color="black", ms=7, lw=2.2, label="mean")
ax.set_xticks(height)
ax.set_xlabel("tee height (level)")
ax.set_ylabel("mean distance")
ax.set_title("Cell means: blocks differ, profiles not parallel")
ax.legend(fontsize=7, ncol=2)

ax = axes[1]
centered = cell - cell.mean(axis=1, keepdims=True)
for j, row in enumerate(centered):
    ax.plot(height, row, marker="o", ms=4, lw=1, alpha=0.8)
ax.plot(height, centered.mean(axis=0), "D-", color="black", ms=7, lw=2.2)
ax.axhline(0, color="gray", ls="--", lw=1)
ax.set_xticks(height)
ax.set_xlabel("tee height (level)")
ax.set_ylabel("cell mean minus golfer mean")
ax.set_title("Golfer effects removed")
for ax in axes:
    ax.grid(alpha=0.3)
fig.tight_layout()
