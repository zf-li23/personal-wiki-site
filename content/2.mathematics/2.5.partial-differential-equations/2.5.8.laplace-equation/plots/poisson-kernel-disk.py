"""Poisson kernel of the unit disk, and the harmonic function with boundary values 1 on the upper half circle."""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))

ax = axes[0]
th = np.linspace(-np.pi, np.pi, 1201)
for i, r in enumerate([0.3, 0.6, 0.8, 0.9]):
    P = (1 - r**2) / (2 * np.pi * (1 - 2 * r * np.cos(th) + r**2))
    ax.plot(th, P, color=f"C{i}", lw=1.8, label=f"r = {r}")
ax.set_xlim(-np.pi, np.pi)
ax.set_xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
ax.set_xticklabels(["-pi", "-pi/2", "0", "pi/2", "pi"])
ax.set_xlabel("theta - phi")
ax.set_title("Poisson kernel (1 - r^2) / (2 pi (1 - 2 r cos + r^2))")
ax.legend(fontsize=9)

ax = axes[1]
r = np.linspace(0, 0.999, 200)
t = np.linspace(0, 2 * np.pi, 361)
R, T = np.meshgrid(r, t)
X, Y = R * np.cos(T), R * np.sin(T)
U = 0.5 + np.arctan(2 * R * np.sin(T) / (1 - R**2)) / np.pi
pc = ax.pcolormesh(X, Y, U, cmap="coolwarm", vmin=0, vmax=1, shading="gouraud")
cs = ax.contour(X, Y, U, levels=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9], colors="k", linewidths=0.8)
ax.clabel(cs, fontsize=7, fmt="%.1f")
ax.plot(np.cos(t[t <= np.pi]), np.sin(t[t <= np.pi]), color="C3", lw=4)
ax.plot(np.cos(t[t >= np.pi]), np.sin(t[t >= np.pi]), color="C0", lw=4)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("u = 1 on the upper, u = 0 on the lower half circle")
fig.colorbar(pc, ax=ax, shrink=0.8)
fig.tight_layout()
