"""Sliding-interval sequence: Y_n is the indicator of the n-th piece when [0,1] is cut into 2, 3, 4, ... pieces."""

import numpy as np
import matplotlib.pyplot as plt

intervals = []
for m in range(2, 9):
    for j in range(m):
        intervals.append((j / m, (j + 1) / m, m))

fig, ax = plt.subplots(figsize=(8, 5))
for n, (a, b, m) in enumerate(intervals, start=1):
    ax.plot([a, b], [n, n], lw=4, color=f"C{m % 10}", solid_capstyle="butt")
for w in [0.3, 0.71]:
    ax.axvline(w, color="0.4", lw=1, ls="--")
    hits = [n for n, (a, b, m) in enumerate(intervals, start=1) if a <= w <= b]
    ax.plot([w] * len(hits), hits, "o", color="black", ms=4)
ax.invert_yaxis()
ax.set_xlim(0, 1)
ax.set_xlabel("omega in [0, 1]")
ax.set_ylabel("n")
ax.set_title("Y_n = 1 on the bar in row n: widths 1/m -> 0, yet every omega is hit in every round")
ax.grid(alpha=0.3)
fig.tight_layout()
