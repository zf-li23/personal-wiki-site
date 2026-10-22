"""Unit cells of six ionic structure types: rock salt, CsCl, zinc blende, fluorite, rutile and perovskite."""

import itertools

import numpy as np
import matplotlib.pyplot as plt

corners = np.array(list(itertools.product([0, 1], repeat=3)), float)
fcc = np.vstack([corners, [[0.5, 0.5, 0], [0.5, 0.5, 1], [0.5, 0, 0.5], [0.5, 1, 0.5], [0, 0.5, 0.5], [1, 0.5, 0.5]]])
edge_mid = np.array([p for p in itertools.product([0, 0.5, 1], repeat=3) if sum(x == 0.5 for x in p) == 1], float)


def box(ax, scale=(1, 1, 1)):
    sc = np.asarray(scale)
    for a, b in itertools.combinations(range(8), 2):
        if np.sum(np.abs(corners[a] - corners[b])) == 1:
            ax.plot(*zip(corners[a] * sc, corners[b] * sc), color="0.55", lw=0.9)


def atoms(ax, pts, color, size):
    pts = np.asarray(pts, float)
    ax.scatter(pts[:, 0], pts[:, 1], pts[:, 2], s=size, color=color, edgecolors="black", linewidths=0.4, depthshade=True)


def bonds(ax, cations, anions, dmax):
    for c in np.asarray(cations, float):
        for a in np.asarray(anions, float):
            if np.linalg.norm(c - a) < dmax:
                ax.plot(*zip(c, a), color="0.55", lw=0.7)


def finish(ax, title, aspect=(1, 1, 1)):
    ax.set_box_aspect(aspect)
    ax.view_init(elev=16, azim=-60)
    ax.set_axis_off()
    ax.set_title(title, fontsize=10)


fig = plt.figure(figsize=(12, 7.6))

ax = fig.add_subplot(2, 3, 1, projection="3d")
box(ax)
cat = np.vstack([edge_mid, [[0.5, 0.5, 0.5]]])
bonds(ax, cat, fcc, 0.51)
atoms(ax, fcc, "C2", 230)
atoms(ax, cat, "C1", 110)
finish(ax, "rock salt (NaCl) type\nCl$^-$ ccp, Na$^+$ in all octahedral holes, 6:6")

ax = fig.add_subplot(2, 3, 2, projection="3d")
box(ax)
bonds(ax, [[0.5, 0.5, 0.5]], corners, 0.9)
atoms(ax, corners, "C2", 300)
atoms(ax, [[0.5, 0.5, 0.5]], "C1", 280)
finish(ax, "CsCl type\nCl$^-$ simple cubic, Cs$^+$ in the cubic hole, 8:8")

ax = fig.add_subplot(2, 3, 3, projection="3d")
box(ax)
zn = [[0.25, 0.25, 0.25], [0.75, 0.75, 0.25], [0.75, 0.25, 0.75], [0.25, 0.75, 0.75]]
bonds(ax, zn, fcc, 0.45)
atoms(ax, fcc, "C2", 230)
atoms(ax, zn, "C1", 110)
finish(ax, "zinc blende (cubic ZnS) type\nS$^{2-}$ ccp, Zn$^{2+}$ in half the tetrahedral holes, 4:4")

ax = fig.add_subplot(2, 3, 4, projection="3d")
box(ax)
f = np.array(list(itertools.product([0.25, 0.75], repeat=3)))
bonds(ax, fcc, f, 0.45)
atoms(ax, fcc, "C1", 200)
atoms(ax, f, "C2", 150)
finish(ax, "fluorite (CaF$_2$) type\nCa$^{2+}$ ccp, F$^-$ in all tetrahedral holes, 8:4")

ax = fig.add_subplot(2, 3, 5, projection="3d")
a, c, u = 459.4, 295.9, 0.305
sc = np.array([1, 1, c / a])
box(ax, sc)
ti = np.vstack([corners, [[0.5, 0.5, 0.5]]]) * sc
o = np.array([[u, u, 0], [1 - u, 1 - u, 0], [u, u, 1], [1 - u, 1 - u, 1],
              [0.5 + u, 0.5 - u, 0.5], [0.5 - u, 0.5 + u, 0.5]]) * sc
bonds(ax, ti, o, 0.45)
atoms(ax, o, "C2", 190)
atoms(ax, ti, "C1", 110)
finish(ax, "rutile (TiO$_2$) type, tetragonal\nO$^{2-}$ distorted hcp, Ti$^{4+}$ in half the octahedral holes, 6:3",
       aspect=(1, 1, c / a))

ax = fig.add_subplot(2, 3, 6, projection="3d")
box(ax)
ox = np.array([[0.5, 0.5, 0], [0.5, 0.5, 1], [0.5, 0, 0.5], [0.5, 1, 0.5], [0, 0.5, 0.5], [1, 0.5, 0.5]])
bonds(ax, [[0.5, 0.5, 0.5]], ox, 0.51)
atoms(ax, corners, "C0", 260)
atoms(ax, ox, "C2", 170)
atoms(ax, [[0.5, 0.5, 0.5]], "C1", 110)
finish(ax, "perovskite (ABX$_3$, e.g. SrTiO$_3$)\nA (corners) CN 12, B (center) CN 6")

fig.text(0.5, 0.01, "Green: anions (X);  orange: smaller cations;  blue: large A cations in perovskite.  Lines join nearest neighbors.",
         ha="center", fontsize=9.5)
fig.subplots_adjust(left=0, right=1, top=0.93, bottom=0.04, wspace=0.02, hspace=0.18)
