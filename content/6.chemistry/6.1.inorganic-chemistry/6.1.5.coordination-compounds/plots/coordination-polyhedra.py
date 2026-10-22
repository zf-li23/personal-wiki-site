import numpy as np
import matplotlib.pyplot as plt

METAL = "#d97706"
LIGAND = "#2563eb"
BOND = "#94a3b8"
EDGE = "#64748b"

s3 = np.sqrt(3)
tri = [(np.cos(a), np.sin(a), 0.0) for a in np.radians([90, 210, 330])]
prism = [(0.8 * np.cos(a), 0.8 * np.sin(a), z) for z in (0.65, -0.65) for a in np.radians([90, 210, 330])]

shapes = [
    ("CN 2: linear", [(0, 0, 1), (0, 0, -1)], [(0, 1)]),
    ("CN 3: trigonal planar", tri, [(0, 1), (1, 2), (2, 0)]),
    (
        "CN 4: tetrahedral",
        [(1 / s3, 1 / s3, 1 / s3), (1 / s3, -1 / s3, -1 / s3), (-1 / s3, 1 / s3, -1 / s3), (-1 / s3, -1 / s3, 1 / s3)],
        [(i, j) for i in range(4) for j in range(i + 1, 4)],
    ),
    ("CN 4: square planar", [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0)], [(0, 1), (1, 2), (2, 3), (3, 0)]),
    (
        "CN 5: trigonal bipyramidal",
        [(0, 0, 1), (0, 0, -1)] + tri,
        [(0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (4, 2)],
    ),
    (
        "CN 5: square pyramidal",
        [(0, 0, 1), (1, 0, -0.2), (0, 1, -0.2), (-1, 0, -0.2), (0, -1, -0.2)],
        [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (2, 3), (3, 4), (4, 1)],
    ),
    (
        "CN 6: octahedral",
        [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)],
        [(i, j) for i in range(6) for j in range(i + 1, 6) if not (i // 2 == j // 2)],
    ),
    ("CN 6: trigonal prismatic", prism, [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3), (0, 3), (1, 4), (2, 5)]),
]

fig = plt.figure(figsize=(12, 6.4))
for k, (title, pts, edges) in enumerate(shapes):
    ax = fig.add_subplot(2, 4, k + 1, projection="3d")
    pts = np.array(pts, dtype=float)
    for i, j in edges:
        ax.plot(*zip(pts[i], pts[j]), color=EDGE, lw=1.0, ls="--")
    for p in pts:
        ax.plot([0, p[0]], [0, p[1]], [0, p[2]], color=BOND, lw=3)
    ax.scatter(*pts.T, s=180, color=LIGAND, depthshade=False, edgecolors="none")
    ax.scatter([0], [0], [0], s=320, color=METAL, depthshade=False, edgecolors="none")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=18, azim=-62)
    ax.set_axis_off()
    ax.set_title(title, fontsize=11)

fig.legend(
    handles=[
        plt.Line2D([], [], marker="o", ls="", color=METAL, markersize=11, label="central atom M"),
        plt.Line2D([], [], marker="o", ls="", color=LIGAND, markersize=9, label="donor atom"),
    ],
    loc="lower center",
    ncol=2,
    frameon=False,
)
fig.subplots_adjust(left=0, right=1, top=0.95, bottom=0.07, wspace=0, hspace=0.1)
