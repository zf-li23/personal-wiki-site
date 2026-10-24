"""Hydride attack on conformationally locked 4-tert-butylcyclohexanone, drawn on the chair. Small
hydride donors (LiAlH4, NaBH4) approach the carbonyl carbon from the axial direction (top): the
forming C-H bond is then staggered with the axial C-H bonds on C2 and C6, and the product has an
equatorial OH (trans alcohol, about 90%). Equatorial approach (bottom) eclipses the forming bond with
those C-H bonds (torsional strain), but avoids the axial hydrogens on C3 and C5 that lie on the axial
side; the bulky L-Selectride therefore attacks equatorially and gives the axial alcohol (cis, about
93%). Only the axial hydrogen on C3 is drawn; the one on C5 lies directly behind it."""

import math

import matplotlib.pyplot as plt
import numpy as np

from wikichem import Scheme

H, R = 0.3, math.sqrt(1 - 4 * 0.3 ** 2)  # pucker height and ring radius for unit bonds
TILT, SPIN = 0.42, 0.0


def proj(p):
    """Project a 3D point (ring roughly in the xy plane, z up) onto the drawing plane."""
    x, y, z = p
    x, y = x * math.cos(SPIN) - y * math.sin(SPIN), x * math.sin(SPIN) + y * math.cos(SPIN)
    return (1.3 * x, z + TILT * y)


ring3 = [np.array([R * math.cos(math.radians(60 * k)), R * math.sin(math.radians(60 * k)), H * (-1) ** k]) for k in range(6)]
up = [1 if (-1) ** k > 0 else -1 for k in range(6)]  # axial direction of each ring atom
c1 = 3  # carbonyl carbon index in ring3 (left side of the drawing)


def radial(k, length=1.0, dz=0.0):
    v = np.array([ring3[k][0], ring3[k][1], 0.0])
    v = v / np.linalg.norm(v)
    return ring3[k] + length * (v * math.sqrt(1 - dz ** 2) + np.array([0, 0, dz]))


order = [c1, (c1 + 1) % 6, (c1 + 2) % 6, (c1 + 3) % 6, (c1 + 4) % 6, (c1 + 5) % 6]  # C1..C6
pts = [ring3[k] for k in order]
o = radial(c1, 1.0)
c4 = order[3]
tbu = radial(c4, 1.0, dz=-0.33 * up[c4])
hs = [ring3[order[i]] + np.array([0, 0, 0.9 * up[order[i]]]) for i in (1, 2, 4, 5)]  # axial H on C2, C3, C5, C6
coords = [proj(p) for p in pts] + [proj(o), proj(tbu)] + [proj(p) for p in hs]
s = Scheme(scale=0.6)
mol = s.molecule("C1(=O)CC([H])C(*)CC1",
                 coords=[coords[0], coords[6], coords[1], coords[2], coords[9], coords[3], coords[7], coords[4], coords[5]],
                 labels={6: "$t$Bu"})
fig, ax = s.draw(margin=1.6)
ink = plt.rcParams["text.color"]
c = np.array(coords[0])
ax_dir = np.array([0.0, 1.0]) * up[c1]
for start, text, where in ((c + 1.9 * ax_dir + np.array([0.15, 0]), "axial attack\n(LiAlH$_4$, NaBH$_4$)", "top"),
                           (c - 1.7 * ax_dir + np.array([-1.0, 0]), "equatorial attack\n(L-Selectride)", "bottom")):
    ax.annotate("", xy=c + 0.25 * (start - c) / np.linalg.norm(start - c), xytext=start,
                arrowprops=dict(arrowstyle="-|>", color=ink, lw=1.3, ls=(0, (4, 3))))
    ax.text(*(start + np.array([-0.25 if where == "top" else 0.25, 0.0])), text, ha="right" if where == "top" else "left", va="center",
            fontsize=10, color=ink)
