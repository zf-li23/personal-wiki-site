"""Siegel-Tukey ranking of the aligned tire-failure data: ranks run from both ends toward the middle."""

import numpy as np
import matplotlib.pyplot as plt

a = np.array([177, 200, 227, 230, 232, 268, 272, 297.])
b = np.array([47, 105, 126, 142, 158, 172, 197, 220, 225, 230, 262, 270.])
a = a - (np.median(a) - np.median(b))          # align: subtract 46.5 from type A
vals = np.concatenate([a, b])
lab = np.array(["A"] * len(a) + ["B"] * len(b))
order = np.argsort(vals, kind="stable")
n = len(vals)

# rank 1 to the smallest, 2 and 3 to the two largest, 4 and 5 to the next two smallest, ...
ranks = np.zeros(n, dtype=int)
lo, hi, r, side = 0, n - 1, 1, "high"
ranks[order[lo]] = r
lo, r = lo + 1, r + 1
while lo <= hi:
    for _ in range(2):
        if lo > hi:
            break
        if side == "high":
            ranks[order[hi]] = r
            hi -= 1
        else:
            ranks[order[lo]] = r
            lo += 1
        r += 1
    side = "low" if side == "high" else "high"

fig, ax = plt.subplots(figsize=(10, 2.5))
pos = np.arange(n)
for k, i in enumerate(order):
    col = "C3" if lab[i] == "A" else "C0"
    ax.scatter(k, 0, s=260, color=col, zorder=3)
    ax.text(k, 0, str(ranks[i]), ha="center", va="center", color="white", fontsize=9, zorder=4)
    ax.text(k, -0.55, f"{vals[i]:g}", ha="center", va="top", fontsize=7, rotation=60)
ax.annotate("", xy=(n / 2 - 1.2, 0.55), xytext=(0, 0.55),
            arrowprops=dict(arrowstyle="->", lw=1.2, color="gray"))
ax.annotate("", xy=(n / 2 + 0.2, 0.55), xytext=(n - 1, 0.55),
            arrowprops=dict(arrowstyle="->", lw=1.2, color="gray"))
ax.text(n / 2 - 0.5, 0.75, "ranks alternate between the two ends and move inward",
        ha="center", fontsize=9, color="gray")
ax.scatter([], [], s=80, color="C3", label="type A (shifted by -46.5)")
ax.scatter([], [], s=80, color="C0", label="type B")
ax.legend(frameon=False, loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=2, fontsize=9)
ax.set_xlim(-1, n)
ax.set_ylim(-1.05, 0.95)
ax.axis("off")
ax.set_title("Siegel-Tukey ranks of the pooled aligned sample (rank sum of A: 106)")
fig.tight_layout()
