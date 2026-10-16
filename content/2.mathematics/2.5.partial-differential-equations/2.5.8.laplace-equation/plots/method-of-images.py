"""Level curves of Dirichlet Green's functions in 2D built by the method of images."""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))
levels = [0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.6]

# half-plane y > 0, source at (0, 1), image at (0, -1)
ax = axes[0]
X, Y = np.meshgrid(np.linspace(-3, 3, 600), np.linspace(-2, 3, 500))
G = -(np.log(np.hypot(X, Y - 1)) - np.log(np.hypot(X, Y + 1))) / (2 * np.pi)
ax.contour(X, Y, np.where(Y >= 0, G, np.nan), levels=levels, colors="C0", linewidths=1.2)
ax.contour(X, Y, np.where(Y <= 0, -G, np.nan), levels=levels, colors="C0", linewidths=0.8, linestyles="dashed", alpha=0.5)
ax.axhline(0, color="k", lw=2)
ax.plot(0, 1, "o", color="C3", ms=7, label="source x")
ax.plot(0, -1, "o", mfc="none", mec="C3", ms=7, label="image x* (opposite sign)")
ax.set_aspect("equal")
ax.set_xlim(-3, 3)
ax.set_ylim(-2, 3)
ax.set_title("Half-plane: G = 0 on y = 0")
ax.legend(fontsize=8, loc="upper right")

# unit disk, source at x0, image at x0 / |x0|^2
ax = axes[1]
x0 = np.array([0.5, 0.2])
xs = x0 / np.dot(x0, x0)
X, Y = np.meshgrid(np.linspace(-1.6, 2.8, 701), np.linspace(-1.6, 1.8, 541))
rx = np.hypot(X - x0[0], Y - x0[1])
rs = np.hypot(X - xs[0], Y - xs[1])
G = -(np.log(rx) - np.log(np.linalg.norm(x0) * rs)) / (2 * np.pi)
inside = X**2 + Y**2 <= 1
ax.contour(X, Y, np.where(inside, G, np.nan), levels=levels, colors="C0", linewidths=1.2)
ax.contour(X, Y, np.where(~inside, -G, np.nan), levels=levels, colors="C0", linewidths=0.8, linestyles="dashed", alpha=0.5)
t = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(t), np.sin(t), color="k", lw=2)
ax.plot(*x0, "o", color="C3", ms=7, label="source x")
ax.plot(*xs, "o", mfc="none", mec="C3", ms=7, label="image x* = x / |x|^2")
ax.set_aspect("equal")
ax.set_xlim(-1.6, 2.8)
ax.set_ylim(-1.6, 1.8)
ax.set_title("Unit disk: G = 0 on |y| = 1")
ax.legend(fontsize=8, loc="upper right")
fig.tight_layout()
