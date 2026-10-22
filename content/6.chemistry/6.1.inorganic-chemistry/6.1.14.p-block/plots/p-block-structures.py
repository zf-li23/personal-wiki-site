"""Ball-and-stick sketches of B2H6 (two 3c-2e B-H-B bridges), P4, P4O6 and P4O10.
Geometries: B-B 177 pm, B-Ht 119 pm, B-Hb 133 pm, Ht-B-Ht 122 deg; P-P 221 pm in P4;
P-O(bridge) 165 pm with P-O-P 128 deg, terminal P=O 143 pm in P4O10. Distances in angstrom."""

import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(0, 2 * np.pi, 22)
v = np.linspace(0, np.pi, 12)
SPH = np.array([np.outer(np.cos(u), np.sin(v)), np.outer(np.sin(u), np.sin(v)), np.outer(np.ones_like(u), np.cos(v))])
COL = {"B": "C1", "H": "0.8", "P": "C3", "O": "C0"}
RAD = {"B": 0.28, "H": 0.17, "P": 0.33, "O": 0.26}


def ball(ax, c, el):
    r = RAD[el]
    ax.plot_surface(c[0] + r * SPH[0], c[1] + r * SPH[1], c[2] + r * SPH[2], color=COL[el], linewidth=0, shade=True)


def bond(ax, a, b, style="-"):
    ax.plot(*zip(a, b), color="0.45", lw=2.4, ls=style)


def draw(ax, atoms, bonds, title, lim, dashed=()):
    for i, j in bonds:
        bond(ax, atoms[i][1], atoms[j][1], "--" if (i, j) in dashed else "-")
    for el, c in atoms:
        ball(ax, c, el)
    ax.set_box_aspect((1, 1, 1))
    for f in (ax.set_xlim, ax.set_ylim, ax.set_zlim):
        f(-lim, lim)
    ax.set_axis_off()
    ax.set_title(title, fontsize=10)


fig = plt.figure(figsize=(11, 3.4))

# B2H6
yb = np.sqrt(1.33 ** 2 - 0.885 ** 2)
xt, zt = 0.885 + 1.19 * np.cos(np.radians(61)), 1.19 * np.sin(np.radians(61))
atoms = [("B", (-0.885, 0, 0)), ("B", (0.885, 0, 0)), ("H", (0, yb, 0)), ("H", (0, -yb, 0)),
         ("H", (-xt, 0, zt)), ("H", (-xt, 0, -zt)), ("H", (xt, 0, zt)), ("H", (xt, 0, -zt))]
bonds = [(0, 2), (1, 2), (0, 3), (1, 3), (0, 4), (0, 5), (1, 6), (1, 7)]
ax = fig.add_subplot(1, 4, 1, projection="3d")
draw(ax, atoms, bonds, "B$_2$H$_6$ (bridges dashed)", 1.6, dashed={(0, 2), (1, 2), (0, 3), (1, 3)})
ax.view_init(elev=35, azim=-70)

T = np.array([(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)], float)
edges = [(i, j) for i in range(4) for j in range(i + 1, 4)]

# P4
s4 = 2.21 / (2 * np.sqrt(2))
atoms = [("P", tuple(s4 * t)) for t in T]
ax = fig.add_subplot(1, 4, 2, projection="3d")
draw(ax, atoms, edges, "P$_4$", 1.7)
ax.view_init(elev=20, azim=30)

# P4O6 and P4O10
s = 2 * 1.65 * np.sin(np.radians(64)) / (2 * np.sqrt(2))
P = [s * t for t in T]
mid_out = s + 1.65 * np.cos(np.radians(64))
O = []
for i, j in edges:
    m = (P[i] + P[j]) / 2
    O.append(m / np.linalg.norm(m) * mid_out)
for k, title in enumerate(["P$_4$O$_6$", "P$_4$O$_{10}$"]):
    atoms = [("P", tuple(p)) for p in P] + [("O", tuple(o)) for o in O]
    bonds = []
    for e, (i, j) in enumerate(edges):
        bonds += [(i, 4 + e), (j, 4 + e)]
    if k == 1:
        for i, p in enumerate(P):
            atoms.append(("O", tuple(p + 1.43 * p / np.linalg.norm(p))))
            bonds.append((i, len(atoms) - 1))
    ax = fig.add_subplot(1, 4, 3 + k, projection="3d")
    draw(ax, atoms, bonds, title, 2.3)
    ax.view_init(elev=20, azim=30)
fig.subplots_adjust(left=0, right=1, top=0.92, bottom=0, wspace=0)
