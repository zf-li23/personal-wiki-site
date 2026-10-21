"""Three-track position encoder disks: with natural binary several tracks
can change at one boundary (e.g. 011 -> 100), with the reflected Gray code
exactly one track changes at every boundary."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge


def gray(k):
    return k ^ (k >> 1)


fig, axes = plt.subplots(1, 2, figsize=(9, 4.6))
for ax, code, title in zip(axes, (lambda k: k, gray), ("natural binary", "reflected Gray code")):
    for k in range(8):
        word = code(k)
        theta1, theta2 = 90 - 45 * (k + 1), 90 - 45 * k
        for bit in range(3):
            r_out = 1.0 - 0.25 * (2 - bit)
            on = (word >> bit) & 1
            ax.add_patch(Wedge((0, 0), r_out, theta1, theta2, width=0.25,
                               facecolor="C0" if on else "none",
                               edgecolor="gray", lw=0.8))
        mid = np.deg2rad((theta1 + theta2) / 2)
        ax.text(1.17 * np.cos(mid), 1.17 * np.sin(mid), format(word, "03b"),
                ha="center", va="center", fontsize=9, family="monospace")
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.35, 1.35)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title + "\n(outer track = MSB)")
fig.tight_layout()
