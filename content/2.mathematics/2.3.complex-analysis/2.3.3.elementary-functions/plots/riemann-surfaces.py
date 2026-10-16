"""Riemann surfaces: Im(log z) over three sheets, and Re(sqrt z) over two sheets."""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 5.4))

r = np.linspace(0.05, 1.5, 25)

ax = fig.add_subplot(1, 2, 1, projection="3d")
th = np.linspace(-3 * np.pi, 3 * np.pi, 300)
R, T = np.meshgrid(r, th)
ax.plot_surface(R * np.cos(T), R * np.sin(T), T, cmap="viridis", linewidth=0, alpha=0.85,
                rstride=3, cstride=2)
ax.plot(np.zeros(2), np.zeros(2), [-3 * np.pi, 3 * np.pi], color="C3", lw=2)
ax.set_xlabel("Re z")
ax.set_ylabel("Im z")
ax.set_zlabel("Im log z")
ax.view_init(elev=20, azim=-55)
ax.set_title("log z: infinitely many sheets, branch point 0")

ax = fig.add_subplot(1, 2, 2, projection="3d")
th = np.linspace(0, 4 * np.pi, 400)
R, T = np.meshgrid(r, th)
ax.plot_surface(R * np.cos(T), R * np.sin(T), np.sqrt(R) * np.cos(T / 2), cmap="plasma", linewidth=0,
                alpha=0.85, rstride=4, cstride=2)
ax.set_xlabel("Re z")
ax.set_ylabel("Im z")
ax.set_zlabel("Re sqrt z")
ax.view_init(elev=25, azim=-60)
ax.set_title("sqrt z: two sheets; a loop around 0 changes the sign")
fig.tight_layout()
