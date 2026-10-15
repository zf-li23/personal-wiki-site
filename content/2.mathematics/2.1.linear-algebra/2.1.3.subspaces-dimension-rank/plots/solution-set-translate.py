"""Solution set of x1 + x2 + x3 = 1, x1 - x2 = 0 in R^3: the line k0 + N(A), parallel to the
null space N(A) (the solutions of the homogeneous system)."""

import numpy as np
import matplotlib.pyplot as plt

k0 = np.array([0.5, 0.5, 0.0])     # a particular solution
k1 = np.array([1.0, 1.0, -2.0])    # spans N(A)

fig = plt.figure(figsize=(6.4, 5.6))
ax = fig.add_subplot(projection="3d")

# The two planes of the row picture
u, v = np.meshgrid(np.linspace(-1.5, 1.5, 2), np.linspace(-1.5, 1.5, 2))
ax.plot_surface(u, v, 1 - u - v, color="C0", alpha=0.18, linewidth=0)
w = np.linspace(-2.5, 2.5, 2)
U, W = np.meshgrid(np.linspace(-1.5, 1.5, 2), w)
ax.plot_surface(U, U, W, color="C2", alpha=0.18, linewidth=0)

s = np.linspace(-1.1, 1.1, 2)
null_line = np.outer(s, k1)
sol_line = k0 + null_line
ax.plot(*null_line.T, color="C2", lw=2.4, ls="--", label="null space $\\mathcal{N}(A)$: $Ax = 0$")
ax.plot(*sol_line.T, color="C3", lw=2.6, label="solution set $k_0 + \\mathcal{N}(A)$: $Ax = b$")
ax.quiver(0, 0, 0, *k0, color="C1", lw=2.0, arrow_length_ratio=0.15)
ax.quiver(*k0, *(0.5 * k1), color="C4", lw=2.0, arrow_length_ratio=0.15)
ax.text(*(0.5 * k0 + np.array([0.0, -0.1, 0.12])), "$k_0$", color="C1", fontsize=12)
ax.text(*(k0 + 0.5 * k1 + np.array([0.08, 0.0, 0.0])), "$k_1$", color="C4", fontsize=12)
ax.scatter([0], [0], [0], color="0.5", s=12)

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-2.5, 2.5)
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_zlabel("$x_3$")
for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
    axis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.view_init(elev=18, azim=-58)
ax.legend(loc="upper left", fontsize=9)
ax.set_title("$x_1 + x_2 + x_3 = 1$ (blue plane), $x_1 - x_2 = 0$ (green plane)", fontsize=10)
fig.tight_layout()
