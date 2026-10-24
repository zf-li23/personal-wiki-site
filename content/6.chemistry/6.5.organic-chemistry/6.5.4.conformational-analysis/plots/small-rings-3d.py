"""Non-planar conformations of small and medium rings (carbon skeletons only, seen nearly edge-on).
Cyclobutane: puckered "butterfly" (atoms alternately 0.13 A above and below the mean plane). Cyclopentane:
envelope (one carbon out of the plane of the other four) and half-chair (two adjacent carbons on opposite
sides of the plane of the other three), both from the Cremer-Pople puckering formula with amplitude
0.43 A; the two interconvert by pseudorotation. Cyclohexene: half-chair from an MMFF-optimised
RDKit structure, C1, C2, C3 and C6 coplanar, C4 and C5 on opposite sides. Red: above the reference
plane, blue: below, grey: in it."""

import numpy as np
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import AllChem

UP, DOWN, MID = "#dc2626", "#2563eb", "0.55"
ink = plt.rcParams["text.color"]


def ring(n, z, bond=1.54):
    r = bond / (2 * np.sin(np.pi / n))
    t = 2 * np.pi * np.arange(n) / n
    return np.c_[r * np.cos(t), r * np.sin(t), z]


def pucker5(phase, q=0.43):
    j = np.arange(5)
    return ring(5, np.sqrt(2 / 5) * q * np.cos(phase + 4 * np.pi * j / 5))


def colours(X, ref):
    """Colour each atom by its side of the plane through the atoms in ref."""
    P = X[ref] - X[ref].mean(0)
    n = np.linalg.svd(P)[2][2]
    if n[2] < 0:
        n = -n
    d = (X - X[ref].mean(0)) @ n
    return [UP if v > 0.08 else DOWN if v < -0.08 else MID for v in d]


def cyclohexene():
    m = Chem.AddHs(Chem.MolFromSmiles("C1=CCCCC1"))
    AllChem.EmbedMolecule(m, randomSeed=7)
    AllChem.MMFFOptimizeMolecule(m)
    X = m.GetConformer().GetPositions()[:6]
    X = X - X.mean(0)
    n = np.linalg.svd(X)[2][2]
    # rotate so that the mean plane normal is z
    z = n / np.linalg.norm(n)
    x = np.cross([0, 1, 0], z) if abs(z[1]) < 0.9 else np.cross([1, 0, 0], z)
    x /= np.linalg.norm(x)
    y = np.cross(z, x)
    return X @ np.c_[x, y, z]


rings = [
    ("cyclobutane: puckered", ring(4, 0.135 * np.array([1, -1, 1, -1])), [0, 1, 2, 3], None, -60),
    ("cyclopentane: envelope", pucker5(0.0), [1, 2, 3, 4], None, -90),
    ("cyclopentane: half-chair", pucker5(np.pi / 2), None, None, -90),
    ("cyclohexene: half-chair", cyclohexene(), [0, 1, 2, 5], (0, 1), -62),
]
fig = plt.figure(figsize=(12, 3.6))
for k, (title, X, ref, double, azim) in enumerate(rings):
    ax = fig.add_subplot(1, 4, k + 1, projection="3d")
    n = len(X)
    if ref is None:  # half-chair of cyclopentane: plane of the three atoms 2, 3, 4 (the coplanar ones)
        d = X[:, 2]
        ref = list(np.argsort(np.abs(d))[:3])
    cols = colours(X, ref)
    for i in range(n):
        j = (i + 1) % n
        lw = 5 if double == (i, j) else 2.6
        ax.plot(*zip(X[i], X[j]), color=ink, lw=lw)
    ax.scatter(*X.T, s=260, c=cols, depthshade=False, edgecolors=ink, linewidths=0.6)
    ax.set_box_aspect((1, 1, 0.48))
    ax.set_proj_type("ortho")
    lim = 1.25
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-0.6, 0.6)
    ax.view_init(elev=9, azim=azim)
    ax.set_axis_off()
    ax.set_title(title, fontsize=10)
