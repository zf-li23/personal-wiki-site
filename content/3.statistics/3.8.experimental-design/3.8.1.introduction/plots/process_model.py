"""General model of a process: controllable and uncontrollable inputs, response."""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

fig, ax = plt.subplots(figsize=(8, 4.6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

ax.add_patch(Rectangle((3.2, 2.2), 3.6, 1.6, fill=False, lw=1.8, ec="black"))
ax.text(5.0, 3.0, "Process", ha="center", va="center", fontsize=14)


def arrow(x0, y0, x1, y1, color="black"):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=16,
                                 lw=1.8, color=color))


arrow(0.8, 3.0, 3.2, 3.0)
ax.text(2.0, 3.25, "Inputs", ha="center", va="bottom", fontsize=11)
ax.text(2.0, 2.75, "experimental units", ha="center", va="top", fontsize=9)
arrow(6.8, 3.0, 9.2, 3.0)
ax.text(8.0, 3.25, "Output", ha="center", va="bottom", fontsize=11)
ax.text(8.0, 2.75, "response y", ha="center", va="top", fontsize=9)

xs = [3.8, 4.6, 6.2]
labels_x = ["$x_1$", "$x_2$", "$x_p$"]
labels_z = ["$z_1$", "$z_2$", "$z_q$"]
for x, lx, lz in zip(xs, labels_x, labels_z):
    arrow(x, 5.0, x, 3.8, color="C0")
    ax.text(x, 5.1, lx, ha="center", va="bottom", fontsize=12, color="C0")
    arrow(x, 1.0, x, 2.2, color="C3")
    ax.text(x, 0.9, lz, ha="center", va="top", fontsize=12, color="C3")
ax.text(5.4, 4.4, "...", ha="center", fontsize=14, color="C0")
ax.text(5.4, 1.5, "...", ha="center", fontsize=14, color="C3")
ax.text(5.0, 5.75, "Controllable factors", ha="center", fontsize=11, color="C0")
ax.text(5.0, 0.15, "Uncontrollable factors", ha="center", fontsize=11, color="C3")
ax.text(8.0, 1.4, r"$y = f(x_1, \ldots, x_p) + \varepsilon$", ha="center", fontsize=12)
ax.text(8.0, 0.9, "f: unknown, fixed function", ha="center", fontsize=9)
fig.tight_layout()
