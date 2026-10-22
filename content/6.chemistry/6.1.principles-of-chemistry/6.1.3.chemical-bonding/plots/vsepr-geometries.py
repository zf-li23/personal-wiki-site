"""VSEPR: electron-pair geometries and the molecular shapes derived from them (AXmEn), as 3D ball-and-stick sketches."""

import numpy as np
import matplotlib.pyplot as plt

s3 = np.sqrt(3) / 2
DIRS = {
    2: [(0, 0, 1), (0, 0, -1)],
    3: [(1, 0, 0), (-0.5, s3, 0), (-0.5, -s3, 0)],
    4: [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)],
    # trigonal bipyramid: three equatorial positions first, then the two axial ones
    5: [(1, 0, 0), (-0.5, s3, 0), (-0.5, -s3, 0), (0, 0, 1), (0, 0, -1)],
    6: [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)],
}

# (pairs, lone-pair positions, formula, shape, example)
CASES = [
    (2, [], "AX2", "linear", "BeCl2, CO2"),
    (3, [], "AX3", "trigonal planar", "BF3, SO3"),
    (3, [0], "AX2E", "bent", "SO2, O3"),
    (4, [], "AX4", "tetrahedral", "CH4"),
    (4, [0], "AX3E", "trigonal pyramidal", "NH3"),
    (4, [0, 1], "AX2E2", "bent", "H2O"),
    (5, [], "AX5", "trigonal bipyramidal", "PCl5"),
    (5, [0], "AX4E", "seesaw", "SF4"),
    (5, [0, 1], "AX3E2", "T-shaped", "ClF3"),
    (5, [0, 1, 2], "AX2E3", "linear", "XeF2, I3-"),
    (6, [], "AX6", "octahedral", "SF6"),
    (6, [0], "AX5E", "square pyramidal", "BrF5"),
    (6, [0, 1], "AX4E2", "square planar", "XeF4"),
]

u = np.linspace(0, 2 * np.pi, 24)
v = np.linspace(0, np.pi, 12)
SPH = np.array([np.outer(np.cos(u), np.sin(v)), np.outer(np.sin(u), np.sin(v)), np.outer(np.ones_like(u), np.cos(v))])


def lobe(ax, d):
    """A lone pair drawn as a translucent ellipsoid along direction d."""
    d = np.asarray(d, float) / np.linalg.norm(d)
    a = np.cross(d, [0.3, 0.5, 0.8])
    a /= np.linalg.norm(a)
    b = np.cross(d, a)
    pts = 0.45 * SPH[2][..., None] * d + 0.22 * SPH[0][..., None] * a + 0.22 * SPH[1][..., None] * b + 0.5 * d
    ax.plot_surface(pts[..., 0], pts[..., 1], pts[..., 2], color="C1", alpha=0.35, linewidth=0, shade=True)


def ball(ax, c, r, color):
    ax.plot_surface(c[0] + r * SPH[0], c[1] + r * SPH[1], c[2] + r * SPH[2], color=color, linewidth=0, shade=True)


layout = [[0, 1, 2, None], [3, 4, 5, None], [6, 7, 8, 9], [10, 11, 12, None]]
fig = plt.figure(figsize=(10, 10.5))
for row, items in enumerate(layout):
    for col, idx in enumerate(items):
        if idx is None:
            continue
        n, lone, formula, shape, example = CASES[idx]
        ax = fig.add_subplot(4, 4, row * 4 + col + 1, projection="3d")
        ball(ax, (0, 0, 0), 0.22, "0.35")
        for k, d in enumerate(DIRS[n]):
            d = np.asarray(d, float) / np.linalg.norm(d)
            if k in lone:
                lobe(ax, d)
            else:
                ax.plot([0, d[0]], [0, d[1]], [0, d[2]], color="0.45", lw=2.5)
                ball(ax, d, 0.16, "C0")
        ax.set_box_aspect((1, 1, 1))
        lim = 1.05
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.set_zlim(-lim, lim)
        ax.view_init(elev=24, azim=28)
        ax.set_axis_off()
        ax.set_title(f"{formula}: {shape}\n{example}", fontsize=9.5)
fig.subplots_adjust(left=0.0, right=1.0, top=0.97, bottom=0.01, wspace=0.0, hspace=0.12)
