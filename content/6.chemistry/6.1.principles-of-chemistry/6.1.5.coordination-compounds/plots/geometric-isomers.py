import numpy as np
import matplotlib.pyplot as plt

METAL = "#d97706"
BOND = "#94a3b8"
EDGE = "#64748b"
LABELS = {"Cl": "Cl", "NH3": r"NH$_3$", "A": "A", "B": "B"}
COLORS = {"Cl": "#16a34a", "NH3": "#2563eb", "A": "#dc2626", "B": "#7c3aed"}

SQUARE = [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0)]
OCTA = [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

panels = [
    (r"$cis$-[PtCl$_2$(NH$_3$)$_2$]", SQUARE, ["Cl", "Cl", "NH3", "NH3"]),
    (r"$trans$-[PtCl$_2$(NH$_3$)$_2$]", SQUARE, ["Cl", "NH3", "Cl", "NH3"]),
    (r"$fac$-MA$_3$B$_3$", OCTA, ["A", "A", "B", "B", "A", "B"]),
    (r"$cis$-[CoCl$_2$(NH$_3$)$_4$]$^+$", OCTA, ["Cl", "Cl", "NH3", "NH3", "NH3", "NH3"]),
    (r"$trans$-[CoCl$_2$(NH$_3$)$_4$]$^+$", OCTA, ["NH3", "NH3", "NH3", "NH3", "Cl", "Cl"]),
    (r"$mer$-MA$_3$B$_3$", OCTA, ["A", "A", "A", "B", "B", "B"]),
]


def edges(pts):
    out = []
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            if abs(np.linalg.norm(pts[i] - pts[j]) - np.sqrt(2)) < 1e-6:
                out.append((i, j))
    return out


fig = plt.figure(figsize=(11, 7.4))
for k, (title, pts, kinds) in enumerate(panels):
    ax = fig.add_subplot(2, 3, k + 1, projection="3d")
    pts = np.array(pts, dtype=float)
    for i, j in edges(pts):
        ax.plot(*zip(pts[i], pts[j]), color=EDGE, lw=0.9, ls="--")
    for p, kind in zip(pts, kinds):
        ax.plot([0, p[0]], [0, p[1]], [0, p[2]], color=BOND, lw=3)
        ax.scatter(*p, s=260, color=COLORS[kind], depthshade=False, edgecolors="none")
        ax.text(*(1.32 * p), LABELS[kind], ha="center", va="center", fontsize=10)
    ax.scatter([0], [0], [0], s=360, color=METAL, depthshade=False, edgecolors="none")
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_zlim(-1.1, 1.1)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=34 if len(pts) == 4 else 22, azim=-58)
    ax.set_axis_off()
    ax.set_title(title, fontsize=12)

fig.subplots_adjust(left=0, right=1, top=0.95, bottom=0.02, wspace=0, hspace=0.08)
