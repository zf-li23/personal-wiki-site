"""Venn diagrams for simple and multiple regression: which variation is used for which coefficient."""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, axes = plt.subplots(1, 2, figsize=(11, 5))


def circle(ax, xy, color, fill=False):
    if fill:
        ax.add_patch(Circle(xy, 1.0, color=color, alpha=0.18, lw=0))
    ax.add_patch(Circle(xy, 1.0, fill=False, color=color, lw=2))


ax = axes[0]
circle(ax, (0.0, 0.4), "C0", fill=True)
circle(ax, (-0.8, -0.65), "C1")
ax.text(0.0, 1.5, "y", ha="center", fontsize=13)
ax.text(-1.75, -1.6, "X", ha="center", fontsize=13)
ax.text(0.3, 0.7, "error:\nestimates sigma^2", ha="center", fontsize=10)
ax.text(-0.42, -0.2, "used\nfor b_X", ha="center", va="center", fontsize=9.5, color="C3")
ax.set_title("Simple regression")

ax = axes[1]
circle(ax, (0.0, 0.55), "C0", fill=True)
circle(ax, (-0.7, -0.5), "C1")
circle(ax, (0.7, -0.5), "C2")
ax.text(0.0, 1.65, "y", ha="center", fontsize=13)
ax.text(-1.75, -1.55, "X", ha="center", fontsize=13)
ax.text(1.75, -1.55, "W", ha="center", fontsize=13)
ax.text(0.0, 1.0, "error: estimates sigma^2", ha="center", fontsize=10)
ax.text(-0.6, 0.02, "unique\nto X:\nb_X", ha="center", va="center", fontsize=8.5, color="C3")
ax.text(0.6, 0.02, "unique\nto W:\nb_W", ha="center", va="center", fontsize=8.5, color="C3")
ax.text(0.0, -0.22, "shared:\nneither", ha="center", va="center", fontsize=8.5)
ax.set_title("Two explanatory variables")

for ax in axes:
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-1.8, 1.9)
    ax.set_aspect("equal")
    ax.axis("off")
fig.tight_layout()
