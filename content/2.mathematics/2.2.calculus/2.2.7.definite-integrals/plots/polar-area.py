"""Area in polar coordinates: a region bounded by r = r(theta) is approximated
by circular sectors of area r(xi)^2 * dtheta / 2."""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))

# Left: cardioid r = 1 + cos(theta) with sector approximation on [0, pi]
ax = axes[0]
r = lambda t: 1 + np.cos(t)
t = np.linspace(0, 2 * np.pi, 600)
ax.plot(r(t) * np.cos(t), r(t) * np.sin(t), color="C0", linewidth=1.6)
n = 12
edges = np.linspace(0, np.pi, n + 1)
for a, b in zip(edges[:-1], edges[1:]):
    rho = r((a + b) / 2)
    arc = np.linspace(a, b, 20)
    xs = np.concatenate([[0], rho * np.cos(arc), [0]])
    ys = np.concatenate([[0], rho * np.sin(arc), [0]])
    ax.fill(xs, ys, color="C1", alpha=0.35, edgecolor="C1", linewidth=0.7)
ax.set_title(r"cardioid $r = a(1+\cos\theta)$: sectors $\frac{1}{2}r(\xi_i)^2\Delta\theta_i$", fontsize=10)
ax.text(0.9, -1.2, r"$S = \frac{3}{2}\pi a^2$", fontsize=11)

# Right: lemniscate r^2 = 2 a^2 cos(2 theta), a = 1
ax = axes[1]
for lo in (-np.pi / 4, 3 * np.pi / 4):
    th = np.linspace(lo, lo + np.pi / 2, 400)
    rho = np.sqrt(np.clip(2 * np.cos(2 * th), 0, None))
    ax.fill(rho * np.cos(th), rho * np.sin(th), color="C2", alpha=0.35)
    ax.plot(rho * np.cos(th), rho * np.sin(th), color="C2", linewidth=1.6)
for ang in (np.pi / 4, -np.pi / 4):
    ax.plot([-1.6 * np.cos(ang), 1.6 * np.cos(ang)], [-1.6 * np.sin(ang), 1.6 * np.sin(ang)],
            color="gray", linewidth=0.8, linestyle="--")
ax.set_title(r"lemniscate $r^2 = 2a^2\cos 2\theta$: $S = 2a^2$", fontsize=10)

for ax in axes:
    ax.axhline(0, color="gray", linewidth=0.6)
    ax.axvline(0, color="gray", linewidth=0.6)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
fig.tight_layout()
