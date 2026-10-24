"""Hyperconjugation in the ethyl cation. Left: a C-H bond of the methyl group lies parallel to the
empty p orbital of the cationic carbon, so the sigma(C-H) orbital overlaps with it. Right: the
two-orbital interaction; the filled sigma orbital is lowered (stabilization) and the empty p
orbital is raised, so the two electrons are partly delocalized onto the cationic carbon. A C-H bond
perpendicular to the p orbital (in the nodal plane) cannot interact."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

ink = plt.rcParams["text.color"]
fill = "#2563eb"
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.5, 4.2), gridspec_kw={"width_ratios": [1.1, 1]})

# Left: geometry. Cationic carbon at (1.2, 0) with a vertical empty p orbital; methyl carbon at (0, 0).
cp = np.array([1.2, 0.0])
cm = np.array([0.0, 0.0])
for sgn in (1, -1):
    a1.add_patch(Ellipse(cp + [0, sgn * 0.62], 0.55, 1.05, fill=False, ec=ink, lw=1.4))
a1.plot(*zip(cm, cp), color=ink, lw=2)
# The C-H bond parallel to the p orbital, with its sigma orbital drawn as a shaded lobe.
h_up = cm + [-0.15, 1.15]
a1.add_patch(Ellipse((cm + h_up) / 2 + [0, 0.05], 0.42, 1.25, angle=np.degrees(np.arctan2(0.15, 1.15)), color=fill, alpha=0.35, lw=0))
a1.plot(*zip(cm, h_up), color=ink, lw=2)
# Two other C-H bonds pointing back and down.
for d in ([-0.9, -0.55], [-0.35, -0.95]):
    a1.plot(*zip(cm, cm + d), color=ink, lw=2)
# Cation substituents in the plane.
for d in ([0.75, 0.45], [0.75, -0.45]):
    a1.plot(*zip(cp, cp + d), color=ink, lw=2)
for p, t in ((cm, "C"), (cp, "C"), (h_up, "H")):
    a1.text(*p, t, ha="center", va="center", fontsize=13, bbox=dict(fc=plt.rcParams["axes.facecolor"], ec="none", pad=1))
a1.text(cp[0] + 0.55, cp[1], "+", ha="center", va="center", fontsize=14)
for d in ([-0.9, -0.55], [-0.35, -0.95], [0.75, 0.45], [0.75, -0.45]):
    end = (cm if d[0] < 0 else cp) + d
    a1.text(*(end + 0.12 * np.array(d) / np.linalg.norm(d)), "H", ha="center", va="center", fontsize=11)
a1.annotate("", xy=(cp[0] - 0.3, 0.75), xytext=(-0.05, 1.0), arrowprops=dict(arrowstyle="->", color=ink, ls="--", connectionstyle="arc3,rad=-0.35"))
a1.text(0.55, 1.45, r"$\sigma_{\mathrm{C-H}} \rightarrow p$ overlap", ha="center", fontsize=10)
a1.text(1.2, -1.45, "empty p", ha="center", fontsize=10)
a1.set_xlim(-1.3, 2.4)
a1.set_ylim(-1.7, 1.75)
a1.set_aspect("equal")
a1.axis("off")

# Right: orbital interaction diagram.
lev = dict(sigma=(0.0, -1.0), p=(3.0, 0.6), low=(1.5, -1.45), high=(1.5, 1.05))
for key, (x, y) in lev.items():
    a2.plot([x - 0.4, x + 0.4], [y, y], color=ink, lw=2)
for a, b in (("sigma", "low"), ("p", "low"), ("sigma", "high"), ("p", "high")):
    (xa, ya), (xb, yb) = lev[a], lev[b]
    a2.plot([xa + (0.4 if xb > xa else -0.4), xb + (-0.4 if xb > xa else 0.4)], [ya, yb], color="0.55", lw=1, ls="--")
for x, y in (lev["sigma"], lev["low"]):
    for dx, sym in ((-0.1, r"$\uparrow$"), (0.1, r"$\downarrow$")):
        a2.text(x + dx, y + 0.02, sym, ha="center", va="center", fontsize=13)
a2.text(0.0, -1.35, r"$\sigma_{\mathrm{C-H}}$", ha="center", va="top", fontsize=11)
a2.text(3.0, 0.75, "empty p", ha="center", va="bottom", fontsize=11)
a2.annotate("", xy=(0.75, -1.45), xytext=(0.75, -1.0), arrowprops=dict(arrowstyle="<->", color=ink))
a2.text(0.85, -1.22, "stabilization", ha="left", va="center", fontsize=9)
a2.set_xlim(-0.8, 3.8)
a2.set_ylim(-1.9, 1.5)
a2.set_ylabel("energy")
a2.set_xticks([])
a2.set_yticks([])
for side in ("top", "right"):
    a2.spines[side].set_visible(False)
fig.tight_layout()
