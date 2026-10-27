"""The mannose 6-phosphate pathway of lysosomal hydrolases (schematic; lumen of each compartment shaded).
(1) In the cis Golgi network GlcNAc-1-phosphotransferase recognizes a signal patch on the folded hydrolase
and transfers GlcNAc-1-phosphate from UDP-GlcNAc to C6 of mannose residues of its N-linked glycan.
(2) In the trans-Golgi network the uncovering enzyme removes the GlcNAc, exposing mannose 6-phosphate (M6P).
(3) M6P receptors bind the tag at about pH 6.5 and are collected with AP-1 and GGA adaptors into
clathrin-coated vesicles. (4) In the acidic endosome (pH below 6) the hydrolase dissociates and a phosphatase
removes the phosphate; (5) the empty receptors return to the TGN (retromer). Hydrolases that escape are
secreted and can be recaptured by M6P receptors at the plasma membrane. In I-cell disease (no phosphotransferase)
the hydrolases are not tagged and are secreted."""

import numpy as np
from matplotlib.patches import Rectangle, Wedge

import wikibio as bio

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(23.0, 10.5, scale=0.42)


def glycan(x, y, state, s=1):
    """N-glycan stub at (x, y) pointing up (s=1) or down (s=-1): two mannoses; 'cap' adds GlcNAc-P, 'm6p' P."""
    ax.plot([x, x], [y, y + s * 0.35], color=P.edge("carbohydrate"), lw=1.0, zorder=14)
    for dx in (-0.14, 0.14):
        ax.plot([x, x + dx], [y + s * 0.35, y + s * 0.55], color=P.edge("carbohydrate"), lw=1.0, zorder=14)
        ax.add_patch(bio.core.Circle((x + dx, y + s * 0.6), 0.075, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=0.6, zorder=15))
    if state in ("cap", "m6p"):
        px, py = x - 0.14, y + s * 0.78
        ax.add_patch(bio.core.Circle((px, py), 0.08, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.6, zorder=15))
        if state == "cap":
            ax.add_patch(Rectangle((px - 0.08, py + s * 0.1 - (0.16 if s < 0 else 0)), 0.16, 0.16, facecolor=P.fill("channel"),
                                   edgecolor=P.edge("channel"), lw=0.6, zorder=15))


def hydrolase(x, y, state="plain", s=1):
    bio.protein(ax, (x, y), 0.75, 0.55, "enzyme")
    glycan(x, y + s * 0.25, state, s)


def mpr(x, y, up=True, bound=False):
    """M6P receptor standing on a membrane at height y, binding site pointing into the lumen (up)."""
    s = 1 if up else -1
    ax.plot([x, x], [y - s * 0.2, y + s * 0.55], color=P.edge("receptor"), lw=2.4, zorder=12, solid_capstyle="round")
    ax.add_patch(Wedge((x, y + s * 0.62), 0.2, 0 if up else 180, 180 if up else 360, width=0.09,
                                facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.6, zorder=13))


def lumen(c, w, h, token="golgi", text=None):
    bio.box(ax, c, w, h, token=token, radius=0.4, zorder=3)
    if text:
        bio.label(ax, (c[0], c[1] + h / 2 + 0.3), text, size="small", bold=True)


# plasma membrane at the top
ax.plot([0.3, 22.7], [8.95, 8.95], color=P.edge("membrane"), lw=2.5, zorder=4)
bio.label(ax, (22.6, 8.6), "plasma membrane (extracellular fluid above)", size="tiny", ha="right", color=P.muted())

# 1: cis Golgi network
lumen((3.2, 6.3), 5.0, 2.0, text="cis Golgi network")
hydrolase(1.6, 5.9, "plain")
bio.protein(ax, (3.6, 5.95), 1.9, 0.75, "protein", text="GlcNAc-P-T", size="tiny")
hydrolase(5.0, 5.9, "cap")
bio.arrow(ax, (2.05, 5.9), (2.6, 5.9), kind="process", head=0.13, color=P.on_fill())
bio.arrow(ax, (4.58, 5.9), (4.62, 5.9), kind="process", head=0.13, color=P.on_fill())
bio.label(ax, (3.6, 6.85), "UDP-GlcNAc → UMP", size="tiny", color=P.on_fill())
bio.label(ax, (0.9, 4.9), "1", size="small", bold=True)

# 2-3: trans-Golgi network
lumen((10.0, 6.3), 5.4, 2.0, text="trans-Golgi network")
hydrolase(8.0, 5.9, "cap")
bio.protein(ax, (9.3, 6.75), 1.2, 0.55, "protein", text="uncovering", size="tiny")
bio.arrow(ax, (8.5, 6.15), (8.75, 6.4), kind="process", head=0.12, color=P.on_fill())
mpr(11.1, 5.35, up=True)
mpr(12.0, 5.35, up=True)
hydrolase(11.14, 7.05, "m6p", s=-1)
bio.label(ax, (7.5, 4.9), "2", size="small", bold=True)
bio.label(ax, (12.95, 4.95), "3", size="small", bold=True)
bio.arrow(ax, (5.75, 6.3), (7.25, 6.3), kind="process", head=0.16)

# clathrin-coated vesicle with receptor-bound hydrolase
cv = np.array([13.3, 3.0])
bio.vesicle(ax, cv, 0.75, token="golgi")
for t in np.linspace(0, 2 * np.pi, 24, endpoint=False):
    ax.add_patch(bio.core.Circle(cv + 0.86 * np.array([np.cos(t), np.sin(t)]), 0.05, color=P.edge("positive"), lw=0, zorder=9))
mpr(cv[0], cv[1] - 0.8, up=True)
hydrolase(cv[0] + 0.04, cv[1] + 0.55, "m6p", s=-1)
bio.arrow(ax, (12.2, 5.15), (12.8, 3.95), kind="process", head=0.16)
bio.label(ax, (cv[0], cv[1] - 1.25), "clathrin, AP-1, GGA", size="tiny", color=P.muted())

# 4: endosome, release and dephosphorylation
en = np.array([17.0, 3.4])
bio.vesicle(ax, en, 1.55, token="vesicle")
bio.label(ax, (en[0] + 0.6, en[1] + 1.85), "late endosome, pH < 6", size="small", bold=True)
mpr(en[0] - 0.9, en[1] - 1.25, up=True)
mpr(en[0] + 0.1, en[1] - 1.5, up=True)
hydrolase(en[0] - 0.45, en[1] + 0.35, "m6p")
hydrolase(en[0] + 0.75, en[1] + 0.05, "plain")
bio.arrow(ax, (en[0] - 0.02, en[1] + 0.25), (en[0] + 0.3, en[1] + 0.15), kind="process", head=0.11, color=P.on_fill())
bio.label(ax, (en[0] + 0.25, en[1] - 0.55), "phosphatase", size="tiny", color=P.on_fill())
bio.arrow(ax, (14.15, 3.1), (15.4, 3.3), kind="process", head=0.16)
bio.label(ax, (15.3, 1.3), "4", size="small", bold=True)

# 5: receptor recycling to the TGN
rv = np.array([14.9, 5.7])
bio.vesicle(ax, rv, 0.42, token="vesicle")
mpr(rv[0], rv[1] - 0.42, up=True)
bio.arrow(ax, (16.2, 4.85), (15.25, 5.45), kind="process", head=0.14, dashed=True)
bio.arrow(ax, (14.45, 5.95), (12.75, 6.4), kind="process", head=0.14, dashed=True)
bio.label(ax, (15.7, 6.55), "5  retromer", size="tiny", color=P.muted())

# lysosome
ly = np.array([21.0, 3.4])
bio.lysosome(ax, ly, 1.05)
bio.label(ax, (ly[0], ly[1] - 1.45), "lysosome, pH 4.5–5", size="small", bold=True)
bio.arrow(ax, (18.6, 3.4), (19.85, 3.4), kind="process", head=0.16)

# secretion and recapture
bio.arrow(ax, (11.9, 7.4), (12.9, 9.35), kind="process", head=0.15, dashed=True, color=P.muted())
hydrolase(13.6, 9.95, "m6p", s=-1)
mpr(16.5, 8.95, up=True)
bio.arrow(ax, (14.1, 9.95), (16.15, 9.6), kind="process", head=0.13, dashed=True, color=P.muted())
bio.arrow(ax, (16.6, 8.55), (16.95, 5.05), kind="process", head=0.15, dashed=True, color=P.muted())
bio.label(ax, (17.2, 7.3), "escaped hydrolases\nrecaptured by CI-MPR\n(endocytosis)", size="tiny", color=P.muted(), ha="left")

# legend and I-cell disease
lx, ly0 = 0.8, 2.9
ax.add_patch(bio.core.Circle((lx, ly0), 0.075, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=0.6, zorder=15))
bio.label(ax, (lx + 0.25, ly0), "mannose", size="tiny", ha="left")
ax.add_patch(Rectangle((lx - 0.08, ly0 - 0.58), 0.16, 0.16, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=0.6, zorder=15))
bio.label(ax, (lx + 0.25, ly0 - 0.5), "GlcNAc", size="tiny", ha="left")
ax.add_patch(bio.core.Circle((lx, ly0 - 1.0), 0.08, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.6, zorder=15))
bio.label(ax, (lx + 0.25, ly0 - 1.0), "phosphate", size="tiny", ha="left")
mpr(lx, ly0 - 2.05, up=True)
bio.label(ax, (lx + 0.3, ly0 - 1.5), "M6P receptor", size="tiny", ha="left")
bio.box(ax, (6.8, 1.9), 7.2, 1.9, token="extracellular", radius=0.2, zorder=3)
bio.label(ax, (6.8, 2.45), "I-cell disease (GNPTAB mutations)", size="small", bold=True)
bio.label(ax, (6.8, 1.65), "no phosphotransferase → no M6P → hydrolases secreted\ninto plasma; lysosomes of fibroblasts fill with inclusions",
          size="tiny")
