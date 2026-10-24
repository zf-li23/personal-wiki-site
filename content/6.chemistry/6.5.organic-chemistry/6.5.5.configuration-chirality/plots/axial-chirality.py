"""Axial chirality. Left: the two enantiomers of penta-2,3-diene (1,3-dimethylallene) in 3D; the
substituents of the two terminal carbons lie in perpendicular planes. Right: assigning Ra/Sa by
viewing along the axis: near groups (horizontal) outrank far groups (vertical); with 4 pointing
away, 1 -> 2 -> 3 clockwise is Ra. Descriptors are computed from the coordinates."""

import numpy as np
import matplotlib.pyplot as plt

ME, HC = "#dc2626", "#64748b"


def label(p1, p2, p3, p4):
    a, b, c = p1 - p4, p2 - p4, p3 - p4
    return "Ra" if np.dot(a, np.cross(b, c)) < 0 else "Sa"


def allene(mirror):
    C = np.array([[-1.31, 0, 0], [0, 0, 0], [1.31, 0, 0]])
    s = -1 if mirror else 1
    near = {"Me": C[0] + [-0.75, 1.2, 0], "H": C[0] + [-0.6, -0.95, 0]}  # in the xy plane
    far = {"Me": C[2] + [0.75, 0, 1.2 * s], "H": C[2] + [0.6, 0, -0.95 * s]}  # in the xz plane
    return C, near, far


fig = plt.figure(figsize=(12, 4))
ink = plt.rcParams["text.color"]
for k, mirror in enumerate((False, True)):
    ax = fig.add_subplot(1, 3, k + 1, projection="3d")
    C, near, far = allene(mirror)
    ax.plot(*C.T, color=ink, lw=3)
    for end, sub in ((C[0], near), (C[2], far)):
        for name, p in sub.items():
            col = ME if name == "Me" else HC
            ax.plot(*zip(end, p), color=col, lw=2.2)
            ax.scatter(*p, s=160 if name == "Me" else 50, color=col, depthshade=False)
    ax.scatter(*C.T, s=90, color="0.35", depthshade=False)
    lab = label(near["Me"], near["H"], far["Me"], far["H"])
    ax.set_title(f"({lab[0]}a)-penta-2,3-diene" if False else f"$({lab[0]}_{{\\mathrm{{a}}}})$-penta-2,3-diene", fontsize=11)
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.2, 2.2)
    ax.set_zlim(-2.2, 2.2)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=20, azim=-60)
    ax.text2D(0.05, 0.05, "red: CH$_3$, grey: H", transform=ax.transAxes, fontsize=8, color="0.45")
    ax.set_axis_off()

ax = fig.add_subplot(1, 3, 3)
ax.add_patch(plt.Circle((0, 0), 0.25, fill=False, color=ink))
ax.plot([-1.2, 1.2], [0, 0], color=ink, lw=2.2)
ax.plot([0, 0], [-1.2, 1.2], color=ink, lw=1.2, ls=(0, (3, 2)))
for (x, y), t in (((-1.75, 0), "1\n(near)"), ((1.75, 0), "2\n(near)"), ((0, 1.5), "3 (far)"), ((0, -1.5), "4 (far)")):
    ax.text(x, y, t, ha="center", va="center", fontsize=10)
th = np.linspace(np.radians(-5), np.radians(80), 40)
ax.plot(0.85 * np.cos(th), 0.85 * np.sin(th), color="#2563eb", lw=1.5)
ax.annotate("", xy=(0.85 * np.cos(th[-1]), 0.85 * np.sin(th[-1])), xytext=(0.85 * np.cos(th[-4]), 0.85 * np.sin(th[-4])),
            arrowprops=dict(arrowstyle="-|>", color="#2563eb"))
p1 = np.array([-1.0, 0, 1.0]); p2 = np.array([1.0, 0, 1.0]); p3 = np.array([0, 1.0, -1.0]); p4 = np.array([0, -1.0, -1.0])
ax.text(0, -2.1, f"1 $\\to$ 2 $\\to$ 3 anticlockwise: {label(p1, p2, p3, p4)}", ha="center", fontsize=10)
ax.set_aspect("equal")
ax.set_xlim(-2.4, 2.4)
ax.set_ylim(-2.5, 1.9)
ax.axis("off")
ax.set_title("view along the axis", fontsize=11)
fig.subplots_adjust(left=0, right=1, bottom=0.02, top=0.9, wspace=0.05)
