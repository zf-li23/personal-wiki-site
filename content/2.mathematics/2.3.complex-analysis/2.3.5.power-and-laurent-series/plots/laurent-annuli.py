"""Regions in which f(z) = 1/((z-1)(z-2)) has a Laurent expansion,
centered at 0 (left) and at 1 (right)."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.6))

def setup(ax, title):
    ax.set_aspect("equal")
    ax.set_xlim(-3.2, 3.6)
    ax.set_ylim(-3.2, 3.2)
    ax.axhline(0, color="gray", lw=0.6)
    ax.axvline(0, color="gray", lw=0.6)
    ax.set_xlabel("Re z")
    ax.set_ylabel("Im z")
    ax.set_title(title)

setup(ax1, "Center 0: three Laurent expansions")
ax1.add_patch(Circle((0, 0), 1, color="C0", alpha=0.35, lw=0))
ax1.add_patch(Wedge((0, 0), 2, 0, 360, width=1, color="C1", alpha=0.35, lw=0))
ax1.add_patch(Wedge((0, 0), 4.9, 0, 360, width=2.9, color="C2", alpha=0.18, lw=0))
for r in (1, 2):
    ax1.add_patch(Circle((0, 0), r, fill=False, ls="--", lw=1.2, color="gray"))
ax1.text(-0.45, -0.45, "|z| < 1", fontsize=10)
ax1.text(-1.0, 1.25, "1 < |z| < 2", fontsize=10)
ax1.text(-2.95, 2.55, "|z| > 2", fontsize=10)

setup(ax2, "Center 1: two Laurent expansions")
ax2.add_patch(Circle((1, 0), 1, color="C3", alpha=0.35, lw=0))
ax2.add_patch(Wedge((1, 0), 5.5, 0, 360, width=4.5, color="C4", alpha=0.18, lw=0))
ax2.add_patch(Circle((1, 0), 1, fill=False, ls="--", lw=1.2, color="gray"))
ax2.text(0.35, -0.55, "0 < |z-1| < 1", fontsize=10)
ax2.text(-2.9, 2.55, "|z-1| > 1", fontsize=10)

for ax in (ax1, ax2):
    ax.plot([1, 2], [0, 0], "kx", ms=9, mew=2, label="poles z = 1, 2")
    ax.legend(loc="lower right")
fig.tight_layout()
