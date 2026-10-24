"""Fischer projections of the stereoisomers of tartaric acid (two like stereocentres: a pair of
enantiomers and a meso form) and of 2,3,4-trihydroxyglutaric acid (C3 is pseudoasymmetric: r/s).
Descriptors are computed from the projections ("-": C3 is not a stereocentre when C2 and C4 match); the pseudoasymmetric centre ranks an R branch
above an S branch (CIP rule 5)."""

import numpy as np
import matplotlib.pyplot as plt

POS = {"top": (0, 1, -1), "bottom": (0, -1, -1), "left": (-1, 0, 1), "right": (1, 0, 1)}


def sense(positions):
    """positions: list of four Fischer positions in CIP order 1..4; returns R or S."""
    p = [np.array(POS[q], float) for q in positions]
    a, b, c = p[0] - p[3], p[1] - p[3], p[2] - p[3]
    return "R" if np.dot(a, np.cross(b, c)) < 0 else "S"


def centre(oh_right, up_rank_higher):
    """A Fischer centre with OH and H horizontal. CIP order: OH, then the higher-ranked vertical
    neighbour, the lower one, H."""
    oh, h = ("right", "left") if oh_right else ("left", "right")
    hi, lo = ("top", "bottom") if up_rank_higher else ("bottom", "top")
    return sense([oh, hi, lo, h])


def draw(ax, x0, ohs, labels, title):
    ink = plt.rcParams["text.color"]
    n = len(ohs)
    ys = [0.9 * (n - 1) / 2 - 0.9 * i for i in range(n)]
    ax.plot([x0, x0], [ys[0] + 0.75, ys[-1] - 0.75], color=ink, lw=1.5)
    ax.text(x0, ys[0] + 1.0, "COOH", ha="center", fontsize=10)
    ax.text(x0, ys[-1] - 1.0, "COOH", ha="center", fontsize=10)
    for y, right, lab in zip(ys, ohs, labels):
        ax.plot([x0 - 0.55, x0 + 0.55], [y, y], color=ink, lw=1.5)
        ax.text(x0 - 0.62, y, "H" if right else "HO", ha="right", va="center", fontsize=10)
        ax.text(x0 + 0.62, y, "OH" if right else "H", ha="left", va="center", fontsize=10)
        ax.text(x0 + 1.45, y, lab, ha="left", va="center", fontsize=9, color="#2563eb")
    ax.text(x0 + 0.3, ys[-1] - 1.75, title, ha="center", fontsize=10)


def tartaric(ohs):
    # C2: COOH (top) outranks C3; C3: COOH (bottom) outranks C2
    return [centre(ohs[0], True), centre(ohs[1], False)]


def trihydroxy(ohs):
    c2 = centre(ohs[0], True)
    c4 = centre(ohs[2], False)
    if c2 == c4:
        return [c2, "$-$", c4]
    up_higher = c2 == "R"  # the R branch outranks the S branch
    return [c2, centre(ohs[1], up_higher).lower(), c4]


fig, axs = plt.subplots(1, 2, figsize=(12, 4.2), gridspec_kw={"width_ratios": [3, 4]})
for k, (ohs, name) in enumerate([((True, False), "(+)-tartaric acid"), ((False, True), "($-$)-tartaric acid"), ((True, True), "meso-tartaric acid")]):
    labs = tartaric(ohs)
    draw(axs[0], 3.2 * k, ohs, labs, name)
axs[0].plot([1.6, 1.6], [-1.6, 1.6], ls="--", color="0.6")
axs[0].text(1.6, 1.75, "mirror", ha="center", fontsize=8, color="0.5")
axs[0].plot([6.1, 7.3], [0, 0], ls=":", color="#dc2626")
axs[0].text(7.0, 0.15, "$\\sigma$", color="#dc2626", fontsize=11)
for ax in axs:
    ax.set_aspect("equal")
    ax.axis("off")
axs[0].set_xlim(-1.2, 8.4)
axs[0].set_ylim(-3.0, 2.0)
iso = [((True, True, False), "chiral"), ((False, False, True), "chiral (enantiomer)"),
       ((True, True, True), "meso"), ((True, False, True), "meso")]
for k, (ohs, name) in enumerate(iso):
    draw(axs[1], 3.4 * k, ohs, trihydroxy(ohs), name)
axs[1].set_xlim(-1.2, 3.4 * 3 + 3.2)
axs[1].set_ylim(-3.4, 2.4)
fig.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0.05)
