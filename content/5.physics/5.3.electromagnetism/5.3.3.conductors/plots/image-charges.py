"""Method of images: a point charge near a grounded plane and near a grounded sphere,
and the induced surface charge density on the plane."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


def potential_and_field(charges, X, Y):
    """Potential and field of point charges (q, x, y); units with q / (4 pi eps0) = q."""
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


def draw(ax, charges, mask, seeds, levels):
    x = np.linspace(-3, 3, 600)
    X, Y = np.meshgrid(x, x)
    phi, Ex, Ey = potential_and_field(charges, X, Y)
    inside = mask(X, Y)
    Ex = np.ma.masked_where(inside, Ex)
    Ey = np.ma.masked_where(inside, Ey)
    phi = np.ma.masked_where(inside, phi)
    ax.streamplot(X, Y, Ex, Ey, start_points=seeds, color="0.55", linewidth=0.8,
                  density=4, arrowsize=0.7, broken_streamlines=False)
    ax.contour(X, Y, phi, levels=levels, cmap="viridis", linewidths=1.3)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect("equal")
    ax.set_xlabel("x / a" if ax is axes[0] else "x / R")


def ring(x0, y0, n=28, r=0.08):
    a = np.linspace(0, 2 * np.pi, n, endpoint=False)
    return np.column_stack([x0 + r * np.cos(a), y0 + r * np.sin(a)])


levels = [0.1, 0.2, 0.35, 0.6, 1.0, 2.0]
fig, axes = plt.subplots(1, 3, figsize=(15, 4.9))

# (a) charge q at (0, a) above the grounded plane y = 0; image -q at (0, -a)
a = 1.0
draw(axes[0], [(1.0, 0.0, a), (-1.0, 0.0, -a)], lambda X, Y: Y < 0, ring(0.0, a), levels)
axes[0].add_patch(Rectangle((-3, -3), 6, 3, color="0.8", zorder=2))
axes[0].plot(0, -a, "o", ms=9, mfc="none", mec="C0", mew=1.5, zorder=3)
axes[0].text(0.2, -a, r"image $-q$", color="C0", va="center", zorder=3)
axes[0].text(-2.8, -2.7, "grounded conductor", fontsize=9, zorder=3)
axes[0].plot(0, a, "o", ms=10, color="C3", zorder=3)
axes[0].set_title("Point charge above a grounded plane")
axes[0].set_ylabel("y / a")

# (b) charge q at distance l from the center of a grounded sphere of radius R
R, l = 1.0, 2.0
qi, li = -R / l, R**2 / l
draw(axes[1], [(1.0, l, 0.0), (qi, li, 0.0)], lambda X, Y: X**2 + Y**2 < R**2, ring(l, 0.0),
     levels)
axes[1].add_patch(Circle((0, 0), R, color="0.8", zorder=2))
axes[1].plot(li, 0, "o", ms=7, mfc="none", mec="C0", mew=1.5, zorder=3)
axes[1].annotate(r"image $-qR/l$ at $R^2/l$", xy=(li, 0), xytext=(-2.6, 1.6), fontsize=9,
                 color="C0", arrowprops=dict(arrowstyle="->", color="C0", lw=0.8), zorder=3)
axes[1].plot(l, 0, "o", ms=10, color="C3", zorder=3)
axes[1].set_title("Point charge near a grounded sphere (l = 2R)")
axes[1].set_ylabel("y / R")

# (c) induced surface charge density on the plane
s = np.linspace(-4, 4, 801)
sigma = -1.0 / (1 + s**2) ** 1.5   # in units of q / (2 pi a^2)
ax = axes[2]
ax.plot(s, sigma, lw=2)
ax.axhline(0, color="0.6", lw=0.8)
ax.set_xlabel("distance from the foot of the charge  s / a")
ax.set_ylabel(r"$\sigma\,/\,[q/(2\pi a^2)]$")
ax.set_title("Induced charge on the plane (total = -q)")
ax.set_xlim(-4, 4)
ax.set_ylim(-1.1, 0.1)
fig.tight_layout()
