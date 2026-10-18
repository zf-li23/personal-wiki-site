"""Interaction plot of the bakery data and schematic patterns without and with interaction."""

import numpy as np
import matplotlib.pyplot as plt

# bakery data: sales[width][height] with two stores per cell
sales = {1: {1: [47, 43], 2: [62, 68], 3: [41, 39]},
         2: {1: [46, 40], 2: [67, 71], 3: [42, 46]}}
heights = [1, 2, 3]

fig, axes = plt.subplots(1, 3, figsize=(13, 4.2))
ax = axes[0]
for w, style, mk in [(1, "--", "o"), (2, "-", "s")]:
    means = [np.mean(sales[w][h]) for h in heights]
    pts = [(h, y) for h in heights for y in sales[w][h]]
    ax.scatter([p[0] + (0.05 if w == 2 else -0.05) for p in pts], [p[1] for p in pts],
               s=14, alpha=0.5, color=f"C{w - 1}")
    ax.plot(heights, means, ls=style, marker=mk, color=f"C{w - 1}", lw=1.8,
            label="regular width" if w == 1 else "wide")
ax.set_xticks(heights)
ax.set_xticklabels(["bottom", "middle", "top"])
ax.set_xlabel("shelf height (factor A)")
ax.set_ylabel("cases of bread sold")
ax.set_title("Bakery data: nearly parallel")
ax.legend(loc="upper right")
ax.grid(alpha=0.3)

x = np.array([1, 2, 3])
ax = axes[1]
ax.plot(x, [9, 11, 13], "o-", lw=1.8, label="B level 1")
ax.plot(x, [3, 5, 7], "s--", lw=1.8, label="B level 2")
ax.set_title("No interaction: parallel lines")
ax.set_ylim(0, 16)

ax = axes[2]
ax.plot(x, [4, 8, 12], "o-", lw=1.8, label="B level 1")
ax.plot(x, [12, 8, 4], "s--", lw=1.8, label="B level 2")
ax.plot(x, [8, 8, 8], ":", color="gray", lw=1.5, label="marginal means of A")
ax.set_title("Crossing interaction")
ax.set_ylim(0, 16)
for ax in axes[1:]:
    ax.set_xticks(x)
    ax.set_xlabel("level of factor A")
    ax.set_ylabel("mean response")
    ax.legend(loc="upper left")
    ax.grid(alpha=0.3)
fig.tight_layout()
