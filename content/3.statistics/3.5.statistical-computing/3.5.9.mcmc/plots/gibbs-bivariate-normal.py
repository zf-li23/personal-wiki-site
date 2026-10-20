"""Gibbs sampler for the standard bivariate normal with correlation rho: the first moves of
the chain over the density contours (each move changes one coordinate) and the trace of
the first coordinate for rho = 0.5 and rho = 0.99."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)


def gibbs(rho, n, start=(-3.0, 3.0)):
    s = np.sqrt(1 - rho ** 2)
    x, y = start
    path = [(x, y)]
    for _ in range(n):
        x = rng.normal(rho * y, s)   # X | Y = y ~ N(rho y, 1 - rho^2)
        path.append((x, y))
        y = rng.normal(rho * x, s)   # Y | X = x ~ N(rho x, 1 - rho^2)
        path.append((x, y))
    return np.array(path)


fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2), gridspec_kw={"width_ratios": (1, 1.5)})
ax = axes[0]
rho = 0.9
g = np.linspace(-3.5, 3.5, 200)
gx, gy = np.meshgrid(g, g)
dens = np.exp(-(gx ** 2 - 2 * rho * gx * gy + gy ** 2) / (2 * (1 - rho ** 2)))
ax.contour(gx, gy, dens, levels=6, colors="C7", linewidths=0.8)
path = gibbs(rho, 15)
ax.plot(path[:, 0], path[:, 1], "-o", ms=3, color="C0", lw=1)
ax.plot(*path[0], "s", color="C3", ms=6, label="start (-3, 3)")
ax.set_aspect("equal")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"First 15 sweeps, rho = {rho}", fontsize=10)
ax.legend(fontsize=8, loc="lower right")

ax = axes[1]
for rho, col in ((0.5, "C0"), (0.99, "C3")):
    path = gibbs(rho, 1000)
    ax.plot(path[::2, 0], color=col, lw=0.8, label=f"rho = {rho}")
ax.set_xlabel("sweep t")
ax.set_ylabel("X_t")
ax.set_title("Strong correlation slows the Gibbs sampler", fontsize=10)
ax.legend(fontsize=8)
for a in axes:
    a.grid(alpha=0.3)
fig.tight_layout()
