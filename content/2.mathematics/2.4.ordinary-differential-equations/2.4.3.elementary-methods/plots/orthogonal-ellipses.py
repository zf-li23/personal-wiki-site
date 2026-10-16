"""Orthogonal trajectories y = C x^4 of the ellipses x^2/4 + y^2 = C^2."""

import numpy as np
import matplotlib.pyplot as plt

a, b = 2.0, 1.0
fig, ax = plt.subplots(figsize=(7, 4.5))
phi = np.linspace(0, 2 * np.pi, 400)
for C in [0.25, 0.5, 0.75, 1.0, 1.25, 1.5]:
    ax.plot(a * C * np.cos(phi), b * C * np.sin(phi), color="0.6", lw=1.0)
x = np.linspace(-3.2, 3.2, 600)
for C in [-1.5, -0.5, -0.15, -0.04, 0.04, 0.15, 0.5, 1.5]:
    ax.plot(x, C * np.abs(x) ** (a**2 / b**2), color="C0", lw=1.5)
ax.axvline(0, color="C0", lw=1.5)
ax.axhline(0, color="C0", lw=1.5)
ax.set_xlim(-3.2, 3.2)
ax.set_ylim(-1.8, 1.8)
ax.set_aspect("equal")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Ellipses x^2/4 + y^2 = C^2 and orthogonal trajectories y = C x^4")
fig.tight_layout()
