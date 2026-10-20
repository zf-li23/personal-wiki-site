"""Joint density of two iid normal mixtures 0.7 N(0, 1) + 0.3 N(3, 1): surface plot and contour plot with a simulated sample."""

import numpy as np
import matplotlib.pyplot as plt

p1 = 0.7


def phi(t, mu):
    return np.exp(-0.5 * (t - mu) ** 2) / np.sqrt(2 * np.pi)


def mix(t):
    return p1 * phi(t, 0.0) + (1 - p1) * phi(t, 3.0)


grid = np.linspace(-3, 6, 121)
gx, gy = np.meshgrid(grid, grid)
dens = mix(gx) * mix(gy)  # X and Y are independent

rng = np.random.default_rng(0)
n = 500
xs = np.where(rng.random(n) < p1, 0.0, 3.0) + rng.standard_normal(n)
ys = np.where(rng.random(n) < p1, 0.0, 3.0) + rng.standard_normal(n)

fig = plt.figure(figsize=(11, 4.8))
ax = fig.add_subplot(1, 2, 1, projection="3d")
ax.plot_surface(gx, gy, dens, cmap="viridis", rstride=3, cstride=3, linewidth=0, antialiased=True)
ax.view_init(elev=30, azim=-60)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")
ax.set_title("Surface plot (persp)", fontsize=10)

ax = fig.add_subplot(1, 2, 2)
ax.scatter(xs, ys, s=5, color="0.55", alpha=0.6, label="sample, n = 500")
levels = [0.002, 0.005, 0.01, 0.02, 0.03, 0.05, 0.07]
cs = ax.contour(gx, gy, dens, levels=levels, cmap="viridis")
ax.clabel(cs, fontsize=7, fmt="%.3f")
ax.set_aspect("equal")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Contour plot: low levels reveal the minor modes", fontsize=10)
ax.legend(fontsize=8, loc="upper left")
fig.tight_layout()
