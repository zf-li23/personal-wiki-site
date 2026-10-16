"""Steady temperature in the unit disk with boundary values 1 (upper half) and 0 (lower half)."""

import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0, 0.999, 300)
th = np.linspace(0, 2 * np.pi, 400)
R, TH = np.meshgrid(r, th)
U = 0.5 + np.arctan(2 * R * np.sin(TH) / (1 - R**2)) / np.pi
X, Y = R * np.cos(TH), R * np.sin(TH)

fig, ax = plt.subplots(figsize=(6, 5.4))
cf = ax.contourf(X, Y, U, levels=np.linspace(0, 1, 21), cmap="coolwarm")
cs = ax.contour(X, Y, U, levels=np.linspace(0.1, 0.9, 9), colors="k", linewidths=0.7)
ax.clabel(cs, fmt="%.1f", fontsize=8)
phi = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(phi[:200]), np.sin(phi[:200]), color="C3", lw=3, label="u = 1")
ax.plot(np.cos(phi[200:]), np.sin(phi[200:]), color="C0", lw=3, label="u = 0")
ax.set_aspect("equal")
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_xlabel("x / a")
ax.set_ylabel("y / a")
ax.set_title("Dirichlet problem in a disk")
ax.legend(loc="upper right", fontsize=9)
fig.colorbar(cf, ax=ax, shrink=0.85, label="u")
fig.tight_layout()
