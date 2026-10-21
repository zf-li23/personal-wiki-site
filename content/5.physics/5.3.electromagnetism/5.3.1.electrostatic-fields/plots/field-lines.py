"""Electric field lines of an electric dipole and of two equal positive charges."""

import numpy as np
import matplotlib.pyplot as plt


def field(charges, X, Y):
    """Field of point charges (q, x, y) in units where q / (4 pi eps0) = q."""
    Ex = np.zeros_like(X)
    Ey = np.zeros_like(Y)
    for q, x0, y0 in charges:
        dx, dy = X - x0, Y - y0
        r3 = np.hypot(dx, dy) ** 3
        Ex += q * dx / r3
        Ey += q * dy / r3
    return Ex, Ey


x = np.linspace(-3, 3, 401)
X, Y = np.meshgrid(x, x)
cases = [
    ("Electric dipole (+q and -q)", [(1.0, 0.6, 0.0), (-1.0, -0.6, 0.0)]),
    ("Two equal charges (+q and +q)", [(1.0, 0.6, 0.0), (1.0, -0.6, 0.0)]),
]

fig, axes = plt.subplots(1, 2, figsize=(11, 5.2))
for ax, (title, charges) in zip(axes, cases):
    Ex, Ey = field(charges, X, Y)
    # seed the lines on small circles around the positive charges so that their density
    # near each charge is proportional to the charge
    seeds = []
    for q, x0, y0 in charges:
        if q > 0:
            for a in np.linspace(0, 2 * np.pi, 24, endpoint=False):
                seeds.append((x0 + 0.08 * np.cos(a), y0 + 0.08 * np.sin(a)))
    ax.streamplot(X, Y, Ex, Ey, start_points=np.array(seeds), color="C0", linewidth=1.0, density=3, arrowsize=0.9,
                  broken_streamlines=False)
    for q, x0, y0 in charges:
        color = "C3" if q > 0 else "C2"
        ax.plot(x0, y0, "o", ms=13, color=color, zorder=3)
        ax.text(x0, y0, "+" if q > 0 else "-", ha="center", va="center",
                color="white", fontsize=13, fontweight="bold", zorder=4)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect("equal")
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
fig.tight_layout()
