"""3D angular surfaces |Y| of the real p and d orbitals, coloured by the sign of Y."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba

th, ph = np.meshgrid(np.linspace(0, np.pi, 121), np.linspace(0, 2 * np.pi, 241), indexing="ij")
x, y, z = np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)
cp, cd, cd0 = np.sqrt(3 / (4 * np.pi)), np.sqrt(15 / (4 * np.pi)), np.sqrt(5 / (16 * np.pi))
ORBITALS = [
    ("p$_x$", cp * x), ("p$_y$", cp * y), ("p$_z$", cp * z),
    ("d$_{z^2}$", cd0 * (3 * z**2 - 1)),
    ("d$_{xy}$", cd * x * y), ("d$_{xz}$", cd * x * z), ("d$_{yz}$", cd * y * z),
    ("d$_{x^2-y^2}$", cd / 2 * (x**2 - y**2)),
]
red, blue = to_rgba("C3", 0.9), to_rgba("C0", 0.9)

fig = plt.figure(figsize=(11, 6))
for k, (name, Y) in enumerate(ORBITALS):
    ax = fig.add_subplot(2, 4, k + 1, projection="3d")
    r = np.abs(Y)
    colors = np.where((Y >= 0)[..., None], red, blue)
    ax.plot_surface(r * x, r * y, r * z, facecolors=colors, rstride=2, cstride=2,
                    linewidth=0, antialiased=True, shade=True)
    m = 0.62
    for v in ([m, 0, 0], [0, m, 0], [0, 0, m]):
        ax.plot([-v[0], v[0]], [-v[1], v[1]], [-v[2], v[2]], color="0.55", lw=0.7)
    ax.text(m * 1.08, 0, 0, "x", fontsize=8)
    ax.text(0, m * 1.08, 0, "y", fontsize=8)
    ax.text(0, 0, m * 1.08, "z", fontsize=8)
    ax.set_xlim(-m, m); ax.set_ylim(-m, m); ax.set_zlim(-m, m)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=60 if name in ("d$_{xy}$", "d$_{x^2-y^2}$") else 30, azim=35)
    ax.set_axis_off()
    ax.set_title(name, fontsize=11, pad=-6)
fig.subplots_adjust(left=0, right=1, bottom=0, top=0.95, wspace=0, hspace=0.05)
