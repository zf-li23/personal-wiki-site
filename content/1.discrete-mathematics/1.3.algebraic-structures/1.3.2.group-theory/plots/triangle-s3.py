"""The six symmetries of an equilateral triangle and the Cayley table of the group they form, S_3
(Example 2.4.1). Top: the image of the labelled triangle under each symmetry; r is the rotation by
120 degrees, the cycle (1 2 3), and s_i the reflection in the axis through vertex i. Bottom: the
Cayley table, entry xy in row x and column y, where xy means "first y, then x"; each element has its
own colour, every row and column contains each element once, and the table is not symmetric about its
diagonal because the group is not commutative."""

import numpy as np
import matplotlib.pyplot as plt

# permutations of the vertices {1, 2, 3}, written as tuples (image of 1, image of 2, image of 3)
elems = {"e": (1, 2, 3), "r": (2, 3, 1), "r^2": (3, 1, 2), "s_1": (1, 3, 2), "s_2": (3, 2, 1), "s_3": (2, 1, 3)}
names = list(elems)
by_perm = {v: k for k, v in elems.items()}


def compose(x, y):
    """xy: apply y first, then x."""
    px, py = elems[x], elems[y]
    return by_perm[tuple(px[py[i] - 1] for i in range(3))]


label = {"e": "$e$", "r": "$r$", "r^2": "$r^2$", "s_1": "$s_1$", "s_2": "$s_2$", "s_3": "$s_3$"}
colors = {n: f"C{i}" for i, n in enumerate(names)}
corners = {1: (0.0, 1.0), 2: (-0.87, -0.5), 3: (0.87, -0.5)}

fig = plt.figure(figsize=(9, 9.2))
for k, n in enumerate(names):
    ax = fig.add_axes([0.03 + k * 0.16, 0.74, 0.15, 0.2])
    tri = np.array([corners[1], corners[2], corners[3], corners[1]])
    ax.fill(tri[:, 0], tri[:, 1], color=colors[n], alpha=0.25)
    ax.plot(tri[:, 0], tri[:, 1], color=colors[n], lw=1.5)
    perm = elems[n]
    for v in (1, 2, 3):                       # vertex v is carried to the position of vertex perm[v - 1]
        x, y = corners[perm[v - 1]]
        ax.text(1.28 * x, 1.28 * y, str(v), ha="center", va="center", fontsize=11)
    if n.startswith("s"):
        i = int(n[-1])
        x, y = corners[i]
        ax.plot([1.2 * x, -0.65 * x], [1.2 * y, -0.65 * y], color="0.5", lw=1.0, ls="--")
    ax.set_title(label[n], fontsize=13)
    ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.0, 1.5); ax.set_aspect("equal"); ax.axis("off")

ax = fig.add_axes([0.18, 0.04, 0.64, 0.62])
for i, x in enumerate(names):
    for j, y in enumerate(names):
        z = compose(x, y)
        ax.add_patch(plt.Rectangle((j, -i), 1, 1, fc=colors[z], alpha=0.35, ec="0.6", lw=0.6))
        ax.text(j + 0.5, -i + 0.5, label[z], ha="center", va="center", fontsize=13)
    ax.text(-0.35, -i + 0.5, label[x], ha="center", va="center", fontsize=13)
    ax.text(i + 0.5, 1.35, label[x], ha="center", va="center", fontsize=13)
ax.text(-0.35, 1.35, r"$x\backslash y$", ha="center", va="center", fontsize=11)
ax.set_xlim(-0.8, 6.05); ax.set_ylim(-5.05, 1.8); ax.set_aspect("equal"); ax.axis("off")
