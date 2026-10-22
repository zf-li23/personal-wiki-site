"""The 14 Bravais lattices drawn as conventional unit cells."""

import itertools
import numpy as np
import matplotlib.pyplot as plt


def cell_vectors(a, b, c, alpha, beta, gamma):
    al, be, ga = np.radians([alpha, beta, gamma])
    va = np.array([a, 0, 0])
    vb = b * np.array([np.cos(ga), np.sin(ga), 0])
    cx = np.cos(be)
    cy = (np.cos(al) - np.cos(be) * np.cos(ga)) / np.sin(ga)
    vc = c * np.array([cx, cy, np.sqrt(1 - cx**2 - cy**2)])
    return np.array([va, vb, vc])


CENTRING = {
    "P": [],
    "I": [(0.5, 0.5, 0.5)],
    "F": [(0.5, 0.5, 0), (0.5, 0.5, 1), (0.5, 0, 0.5), (0.5, 1, 0.5), (0, 0.5, 0.5), (1, 0.5, 0.5)],
    "C": [(0.5, 0.5, 0), (0.5, 0.5, 1)],
    "R": [],
}

LATTICES = [
    ("cubic P", (1, 1, 1, 90, 90, 90), "P"),
    ("cubic I", (1, 1, 1, 90, 90, 90), "I"),
    ("cubic F", (1, 1, 1, 90, 90, 90), "F"),
    ("tetragonal P", (1, 1, 1.5, 90, 90, 90), "P"),
    ("tetragonal I", (1, 1, 1.5, 90, 90, 90), "I"),
    ("orthorhombic P", (1, 1.3, 1.7, 90, 90, 90), "P"),
    ("orthorhombic C", (1, 1.3, 1.7, 90, 90, 90), "C"),
    ("orthorhombic I", (1, 1.3, 1.7, 90, 90, 90), "I"),
    ("orthorhombic F", (1, 1.3, 1.7, 90, 90, 90), "F"),
    ("hexagonal P", (1, 1, 1.6, 90, 90, 120), "P"),
    ("trigonal R", (1, 1, 1, 70, 70, 70), "R"),
    ("monoclinic P", (1.2, 1.3, 1.5, 90, 110, 90), "P"),
    ("monoclinic C", (1.2, 1.3, 1.5, 90, 110, 90), "C"),
    ("triclinic P", (1, 1.2, 1.4, 75, 100, 110), "P"),
]

corners = np.array(list(itertools.product([0, 1], repeat=3)), dtype=float)
edges = [(i, j) for i, j in itertools.combinations(range(8), 2)
         if np.sum(np.abs(corners[i] - corners[j])) == 1]

fig = plt.figure(figsize=(12, 9.6))
for k, (name, params, centring) in enumerate(LATTICES):
    ax = fig.add_subplot(3, 5, k + 1 + (1 if k >= 10 else 0), projection="3d")
    M = cell_vectors(*params)
    P = corners @ M
    for i, j in edges:
        ax.plot(*zip(P[i], P[j]), color="0.45", lw=1.0)
    ax.scatter(*P.T, s=28, color="0.55", depthshade=False)
    if CENTRING[centring]:
        Q = np.array(CENTRING[centring]) @ M
        ax.scatter(*Q.T, s=36, color="C3", depthshade=False)
    lo, hi = P.min(axis=0), P.max(axis=0)
    ax.set_box_aspect(hi - lo)
    ax.set_xlim(lo[0], hi[0]); ax.set_ylim(lo[1], hi[1]); ax.set_zlim(lo[2], hi[2])
    azim = {"hexagonal P": -105, "trigonal R": -35, "triclinic P": -40}.get(name, -60)
    ax.view_init(elev=18, azim=azim)
    ax.set_axis_off()
    ax.set_title(name, fontsize=10, pad=-4)

fig.subplots_adjust(left=0, right=1, bottom=0, top=0.97, wspace=0.0, hspace=0.05)
