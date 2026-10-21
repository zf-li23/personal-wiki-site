"""Field lines and equipotentials of an electric dipole and of the pair +2q, -q."""

import numpy as np
import matplotlib.pyplot as plt


def potential_and_field(charges, X, Y):
    """Potential and field of point charges (q, x, y), in units where q / (4 pi eps0) = q."""
    phi = np.zeros_like(X)
    Ex = np.zeros_like(X)
    Ey = np.zeros_like(X)
    for q, x0, y0 in charges:
        dx, dy = X - x0, Y - y0
        r = np.hypot(dx, dy)
        phi += q / r
        Ex += q * dx / r**3
        Ey += q * dy / r**3
    return phi, Ex, Ey


x = np.linspace(-3, 3, 601)
X, Y = np.meshgrid(x, x)
d = 0.6
cases = [
    ("Electric dipole (+q, -q)", [(1.0, d, 0.0), (-1.0, -d, 0.0)]),
    ("Charges +2q and -q", [(2.0, d, 0.0), (-1.0, -d, 0.0)]),
]

fig, axes = plt.subplots(1, 2, figsize=(11, 5.2))
for ax, (title, charges) in zip(axes, cases):
    phi, Ex, Ey = potential_and_field(charges, X, Y)
    seeds = []
    for q, x0, y0 in charges:
        if q > 0:
            n = int(16 * q)
            for a in np.linspace(0, 2 * np.pi, n, endpoint=False):
                seeds.append((x0 + 0.08 * np.cos(a), y0 + 0.08 * np.sin(a)))
    ax.streamplot(X, Y, Ex, Ey, start_points=np.array(seeds), color="0.55", linewidth=0.8,
                  density=3, arrowsize=0.7, broken_streamlines=False)
    levels = np.array([-4, -2, -1, -0.5, -0.25, 0.25, 0.5, 1, 2, 4])
    cs = ax.contour(X, Y, phi, levels=levels, cmap="coolwarm", linewidths=1.4)
    ax.contour(X, Y, phi, levels=[0.0], colors="C2", linewidths=2.2)
    for q, x0, y0 in charges:
        ax.plot(x0, y0, "o", ms=12, color="C3" if q > 0 else "C0", zorder=3)
        ax.text(x0, y0, "+" if q > 0 else "-", ha="center", va="center", color="white",
                fontsize=12, fontweight="bold", zorder=4)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect("equal")
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
axes[0].text(0.05, 2.6, r"$\varphi = 0$: midplane", color="C2", fontsize=9)
axes[1].text(-2.9, 2.6, r"$\varphi = 0$: a sphere around $-q$", color="C2", fontsize=9)
fig.tight_layout()
