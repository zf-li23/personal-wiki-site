"""Close-packed layers seen from above: A layer, B layer on top, and the tetrahedral and octahedral holes between them."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

r = 0.5  # sphere radius; neighboring centers are 1 apart
a1, a2 = np.array([1.0, 0.0]), np.array([0.5, np.sqrt(3) / 2])
shift_b = (a1 + a2) / 3
shift_c = 2 * (a1 + a2) / 3

lattice = np.array([i * a1 + j * a2 for i in range(-4, 5) for j in range(-4, 5)])
inside = lambda p: (abs(p[:, 0]) < 1.9) & (abs(p[:, 1]) < 1.7)
A = lattice[inside(lattice)]
B = (lattice + shift_b)[inside(lattice + shift_b)]
C = (lattice + shift_c)[inside(lattice + shift_c)]

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.8))

ax = axes[0]
for p in A:
    ax.add_patch(Circle(p, r, facecolor="C0", alpha=0.35, edgecolor="C0", lw=1))
ax.plot(*B.T, "^", color="C3", ms=7, label="B sites")
ax.plot(*C.T, "v", color="C2", ms=7, label="C sites")
ax.set_title("one close-packed layer A\nthe next layer sits over B (or C) sites", fontsize=10.5)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.02), fontsize=9, ncol=2, frameon=False)

ax = axes[1]
for p in A:
    ax.add_patch(Circle(p, r, facecolor="C0", alpha=0.30, edgecolor="C0", lw=1))
for p in B:
    ax.add_patch(Circle(p, r, facecolor="none", edgecolor="C3", lw=1.3))
# Tetrahedral holes: under each B sphere (above an A triangle) and above each A sphere (under a B triangle).
ax.plot(*B.T, "o", color="C3", ms=4, label="tetrahedral hole (under a B sphere)")
ax.plot(*A.T, "o", color="C0", ms=4, label="tetrahedral hole (over an A sphere)")
ax.plot(*C.T, "s", color="C2", ms=6, label="octahedral hole (C position)")
ax.set_title("two layers A + B\nholes between them", fontsize=10.5)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.02), fontsize=9, ncol=1, frameon=False)

for ax in axes:
    ax.set_aspect("equal")
    ax.set_xlim(-1.9, 1.9)
    ax.set_ylim(-1.7, 1.7)
    ax.axis("off")
fig.tight_layout()
