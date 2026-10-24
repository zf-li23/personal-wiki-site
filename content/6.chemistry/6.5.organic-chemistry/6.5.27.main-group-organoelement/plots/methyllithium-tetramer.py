"""The methyllithium tetramer (CH3Li)4: four lithium atoms at the corners of a tetrahedron and a
methyl carbon above each of the four triangular faces, so each carbon is bonded to three lithium
atoms (mu3-CH3). Each Li3C unit holds one four-centre two-electron bond in the covalent picture;
the C-Li bonding is in fact largely ionic. Hydrogens are omitted."""

import itertools

import matplotlib.pyplot as plt
import numpy as np

li = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], dtype=float)
faces = list(itertools.combinations(range(4), 3))
carbons = []
for f in faces:
    centre = li[list(f)].mean(axis=0)
    carbons.append(centre / np.linalg.norm(centre) * 2.1)  # outside the face, along its normal

fig = plt.figure(figsize=(4.6, 4.2))
ax = fig.add_subplot(projection="3d")
for i, j in itertools.combinations(range(4), 2):
    ax.plot(*zip(li[i], li[j]), color="0.55", lw=1.2, ls="--")
for c, f in zip(carbons, faces):
    for k in f:
        ax.plot(*zip(c, li[k]), color="C0", lw=1.6)
ax.scatter(*li.T, s=150, color="C1", depthshade=False, zorder=3)
ax.scatter(*np.array(carbons).T, s=130, color="C0", depthshade=False, zorder=3)
for p in li:
    ax.text(*(p * 1.38), "Li", fontsize=11, ha="center", va="center")
for c in carbons:
    ax.text(*(c * 1.22), "CH$_3$", fontsize=11, ha="center", va="center")
ax.set_box_aspect((1, 1, 1))
ax.view_init(elev=18, azim=35)
ax.set_axis_off()
fig.tight_layout()
