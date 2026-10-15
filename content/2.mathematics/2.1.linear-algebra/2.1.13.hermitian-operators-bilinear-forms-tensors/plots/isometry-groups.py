"""Three bilinear forms on R^2 and transformations preserving them:
rotations keep x^2 + y^2, Lorentz boosts keep x^2 - t^2 (units with c = 1),
and symplectic matrices (det M = 1) keep the oriented area."""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(13, 4.6))
lim = 2.2

# O(2): level sets x^2 + y^2 = c are circles; rotations move points along them
ax = axes[0]
g = np.linspace(-lim, lim, 300)
X, Y = np.meshgrid(g, g)
ax.contour(X, Y, X**2 + Y**2, levels=[0.5, 1, 2, 3, 4], colors="gray", linewidths=0.8)
p = np.array([1.0, 0.0])
for k, phi in enumerate(np.linspace(0, 4 * np.pi / 3, 5)):
    R = np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi), np.cos(phi)]])
    q = R @ p
    ax.plot(*q, "o", color="C0", markersize=8)
    ax.plot(*(R @ np.array([1.6, 0.6])), "s", color="C1", markersize=7)
ax.set_title(r"$O(2)$: rotations preserve $x^2 + y^2$", fontsize=10)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")

# O(1, 1): level sets x^2 - t^2 = c are hyperbolas; boosts move points along them
ax = axes[1]
X, T = np.meshgrid(g, g)
ax.contour(X, T, X**2 - T**2, levels=[-3, -1, 1, 3], colors="gray", linewidths=0.8,
           negative_linestyles="solid")
ax.plot(g, g, "--", color="gray", linewidth=1)
ax.plot(g, -g, "--", color="gray", linewidth=1)
for rapidity in np.linspace(-1.0, 1.0, 5):
    B = np.array([[np.cosh(rapidity), np.sinh(rapidity)], [np.sinh(rapidity), np.cosh(rapidity)]])
    ax.plot(*(B @ np.array([1.0, 0.0])), "o", color="C0", markersize=8)
    ax.plot(*(B @ np.array([0.0, 1.0])), "s", color="C1", markersize=7)
ax.text(1.35, 1.6, "light cone", fontsize=9, color="gray", rotation=45)
ax.set_title(r"$O(1, 1)$: boosts preserve $x^2 - t^2$", fontsize=10)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$t$")

# Sp(2, R) = SL(2, R): the unit disk is mapped to regions of equal area pi
ax = axes[2]
theta = np.linspace(0, 2 * np.pi, 4000)
disk = np.vstack([np.cos(theta), np.sin(theta)])
maps = [(np.eye(2), "identity"),
        (np.array([[1.0, 1.2], [0.0, 1.0]]), "shear"),
        (np.array([[2.0, 0.0], [0.0, 0.5]]), "squeeze diag(2, 1/2)")]
for i, (M, name) in enumerate(maps):
    pts = M @ disk
    area = 0.5 * np.sum(pts[0] * np.roll(pts[1], -1) - np.roll(pts[0], -1) * pts[1])
    ax.fill(pts[0], pts[1], color=f"C{i}", alpha=0.18)
    ax.plot(pts[0], pts[1], color=f"C{i}", linewidth=1.8, label=f"{name}: area {area:.3f}")
ax.set_title(r"$\operatorname{Sp}(2, \mathbb{R})$: $\det M = 1$ preserves area", fontsize=10)
ax.legend(fontsize=8, loc="lower right")

for ax in axes:
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
fig.tight_layout()
