"""Stereographic projection from the north pole of the unit sphere onto the complex plane."""

import numpy as np
import matplotlib.pyplot as plt


def to_sphere(z):
    """Inverse stereographic projection of complex numbers z onto the unit sphere."""
    d = np.abs(z) ** 2 + 1
    return 2 * z.real / d, 2 * z.imag / d, (np.abs(z) ** 2 - 1) / d


fig = plt.figure(figsize=(11, 5.2))

# Left: the projection itself
ax = fig.add_subplot(1, 2, 1, projection="3d")
u = np.linspace(0, 2 * np.pi, 40)
v = np.linspace(0, np.pi, 20)
ax.plot_wireframe(np.outer(np.cos(u), np.sin(v)), np.outer(np.sin(u), np.sin(v)),
                  np.outer(np.ones_like(u), np.cos(v)), color="0.6", lw=0.4, alpha=0.6)
g = np.linspace(-2.5, 2.5, 11)
for c in g:
    ax.plot([c, c], [-2.5, 2.5], [0, 0], color="0.75", lw=0.5)
    ax.plot([-2.5, 2.5], [c, c], [0, 0], color="0.75", lw=0.5)
N = np.array([0, 0, 1])
for z, col in [(1.6 + 1.2j, "C0"), (0.35 - 0.3j, "C3")]:
    p = np.array(to_sphere(np.array(z)))
    end = (z.real, z.imag, 0.0) if abs(z) >= 1 else tuple(p)  # inside the unit circle the line goes on below the plane
    ax.plot([0, end[0]], [0, end[1]], [1, end[2]], color=col, lw=1.2, ls="--")
    ax.scatter([z.real], [z.imag], [0], color=col, s=25)
    ax.scatter(*p, color=col, s=25)
ax.scatter(*N, color="C1", s=40)
ax.text(0.05, 0.05, 1.12, "N (z = infinity)", fontsize=9)
ax.text(1.6, 1.2, -0.25, "z", color="C0", fontsize=10)
ax.text(0.35, -0.3, -0.25, "z", color="C3", fontsize=10)
ax.set_box_aspect((1, 1, 0.44))
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_zlim(-1, 1.2)
ax.set_axis_off()
ax.view_init(elev=22, azim=-60)
ax.set_title("The line through N and z meets the sphere once more")

# Right: images of a circle |z| = r (latitudes) and lines through 0 (meridians)
ax2 = fig.add_subplot(1, 2, 2, projection="3d")
ax2.plot_wireframe(np.outer(np.cos(u), np.sin(v)), np.outer(np.sin(u), np.sin(v)),
                   np.outer(np.ones_like(u), np.cos(v)), color="0.7", lw=0.3, alpha=0.4)
t = np.linspace(0, 2 * np.pi, 300)
for r, col in [(0.5, "C0"), (1.0, "C2"), (2.0, "C3")]:
    x, y, w = to_sphere(r * np.exp(1j * t))
    ax2.plot(x, y, w, color=col, lw=2, label=f"|z| = {r:g}")
s = np.linspace(-40, 40, 2000)
x, y, w = to_sphere(s + 0.5j)
ax2.plot(x, y, w, color="C4", lw=2, label="line Im z = 0.5 (circle through N)")
ax2.scatter(0, 0, 1, color="C1", s=40)
ax2.scatter(0, 0, -1, color="0.4", s=25)
ax2.text(0.05, 0.05, 1.12, "N", fontsize=9)
ax2.text(0.05, 0.05, -1.25, "S (z = 0)", fontsize=9)
ax2.set_box_aspect((1, 1, 1))
ax2.set_axis_off()
ax2.view_init(elev=18, azim=-60)
ax2.legend(loc="upper left", fontsize=8)
ax2.set_title("Circles and lines become circles on the sphere")
fig.tight_layout()
