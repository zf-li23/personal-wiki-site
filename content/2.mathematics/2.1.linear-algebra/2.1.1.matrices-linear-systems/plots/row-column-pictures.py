"""Row picture and column picture of the system x1 + x2 = 8, 2 x1 + 4 x2 = 22 (Example 1.6.1)."""

import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([1.0, 2.0])
a2 = np.array([1.0, 4.0])
b = np.array([8.0, 22.0])
x = np.array([5.0, 3.0])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5.4), gridspec_kw={"width_ratios": [1.25, 1]})

# Row picture: each equation is a line in the (x1, x2) plane; the solution is their intersection
t = np.linspace(-1, 10, 200)
ax1.plot(t, 8 - t, color="C0", lw=1.8, label="$x_1 + x_2 = 8$")
ax1.plot(t, (22 - 2 * t) / 4, color="C2", lw=1.8, label="$2x_1 + 4x_2 = 22$")
ax1.plot(*x, "o", color="C3", ms=7, zorder=5)
ax1.annotate("$(5, 3)$", xy=x, xytext=(x[0] + 0.5, x[1] + 1.0), color="C3", fontsize=11)
ax1.axhline(0, color="0.6", lw=0.6)
ax1.axvline(0, color="0.6", lw=0.6)
ax1.set_xlim(-1, 10)
ax1.set_ylim(-1, 9)
ax1.set_aspect("equal")
ax1.set_xlabel("$x_1$")
ax1.set_ylabel("$x_2$")
ax1.set_title("Row picture: intersect the lines")
ax1.legend(loc="upper right", fontsize=9)


def arrow(ax, start, end, color, lw=1.8, ls="-"):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, linestyle=ls,
                                shrinkA=0, shrinkB=0, mutation_scale=14))


# Column picture: b is the combination 5 a1 + 3 a2 of the columns
ax2.plot([0, 5 * a1[0], b[0], 3 * a2[0], 0], [0, 5 * a1[1], b[1], 3 * a2[1], 0],
         color="0.6", lw=0.8, ls="--")
arrow(ax2, (0, 0), 5 * a1, "C0", lw=1.4)
arrow(ax2, 5 * a1, b, "C2", lw=1.4)
arrow(ax2, (0, 0), a1, "C0", lw=2.6)
arrow(ax2, (0, 0), a2, "C2", lw=2.6)
arrow(ax2, (0, 0), b, "C3", lw=2.0)
ax2.text(a1[0] + 0.4, a1[1] - 0.9, "$a_1$", color="C0", fontsize=12)
ax2.text(a2[0] - 0.9, a2[1] + 0.2, "$a_2$", color="C2", fontsize=12)
ax2.text(5 * a1[0] + 0.3, 5 * a1[1] - 0.8, "$5a_1$", color="C0", fontsize=11)
ax2.text(6.6, 15.6, "$3a_2$", color="C2", fontsize=11)
ax2.text(b[0] - 1.7, b[1] + 0.3, "$b = 5a_1 + 3a_2$", color="C3", fontsize=11)
ax2.axhline(0, color="0.6", lw=0.6)
ax2.axvline(0, color="0.6", lw=0.6)
ax2.set_xlim(-1, 11)
ax2.set_xticks([0, 5, 10])
ax2.set_ylim(-1, 24)
ax2.set_aspect("equal")
ax2.set_title("Column picture: combine the columns")
fig.tight_layout()
