"""Modes of growth and intrinsic versus extrinsic control of organ size (schematic).

A: three ways a tissue grows: proliferation (more cells), hypertrophy (larger cells), accretion (more extracellular
matrix, as in bone and cartilage). B: Twitty and Schwind's grafts between a small (Ambystoma punctatum) and a large
(A. tigrinum) salamander: a limb bud from the large species grafted onto the small one grows into a large limb, and
vice versa; limb size is intrinsic to the bud. C: grafts of several fetal organs into one mouse: each of several
thymus rudiments grows to the normal size of a thymus (intrinsic control), whereas several spleen rudiments together
grow only to the mass of one spleen (systemic, extrinsic control).
"""

import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch

P = bio.P
fig, ax = bio.canvas(30.0, 10.0)

bio.panel(ax, "A", (0.2, 9.8))


def cellrow(x0, y, n, w, h, tok, ecm=0.0):
    for i in range(n):
        cx = x0 + i * (w + ecm)
        ax.add_patch(FancyBboxPatch((cx, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.12",
                                    facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=5))
        ax.add_patch(Circle((cx + w / 2, y), min(w, h) * 0.18, facecolor=P.edge(tok), edgecolor="none", zorder=6))
    if ecm:
        ax.add_patch(FancyBboxPatch((x0 - 0.1, y - h / 2 - 0.15), n * (w + ecm) - ecm + 0.2, h + 0.3,
                                    boxstyle="round,pad=0,rounding_size=0.15", facecolor=P.light("bone"),
                                    edgecolor=P.edge("bone"), lw=0.6, zorder=4))


cellrow(0.8, 8.2, 3, 0.6, 0.6, "animal")
for y, name, kw in ((6.4, "Proliferation", dict(n=6, w=0.6, h=0.6)), (4.4, "Hypertrophy", dict(n=3, w=1.25, h=1.0)),
                    (2.4, "Accretion", dict(n=3, w=0.6, h=0.6, ecm=0.75))):
    bio.arrow(ax, (1.7, 7.75), (1.7, y + 0.55), kind="process", color=P.muted(), lw=0.8)
    cellrow(2.4, y, kw["n"], kw["w"], kw["h"], "animal", kw.get("ecm", 0.0))
    bio.label(ax, (2.4, y - 0.9), name, size="small", ha="left")
bio.label(ax, (0.8, 9.0), "Starting tissue", size="tiny", color=P.muted(), ha="left")

bio.panel(ax, "B", (9.0, 9.8))
for k, (lab, size, limb) in enumerate(((("A. punctatum (small)"), 1.0, "large"), (("A. tigrinum (large)"), 1.6, "small"))):
    x = 12.2 + 5.6 * k
    bio.icon(ax, "phylopic/axolotl", at=(x, 5.2), width=2.6 * size, color="animal")
    bio.label(ax, (x, 2.3), lab, size="small", italic=True)
    # grafted forelimb drawn as an ellipse below the body, size of the donor species
    L = 1.3 if limb == "large" else 0.6
    ax.add_patch(Ellipse((x - 0.15 * size, 5.0 - 0.3 * size - L / 2), 0.35, L, facecolor=P.fill("highlight"),
                         edgecolor=P.edge("highlight"), lw=0.9, zorder=12))
    bio.label(ax, (x, 1.6), f"grafted {limb} limb", size="tiny", color=P.muted())
bio.label(ax, (14.9, 8.8), "Exchange of limb buds", size="small", bold=True)
bio.arrow(ax, (12.6, 8.0), (17.2, 8.0), kind="process", lw=0.9, color=P.muted(), bend=-0.2)
bio.arrow(ax, (17.2, 7.7), (12.6, 7.7), kind="process", lw=0.9, color=P.muted(), bend=-0.2)

bio.panel(ax, "C", (21.0, 9.8))
bio.label(ax, (25.5, 8.8), "Several fetal rudiments grafted", size="small", bold=True)
for j, (name, sizes, note) in enumerate((("Thymus", [1.0, 1.0, 1.0, 1.0], "each grows to full size"),
                                         ("Spleen", [0.25, 0.25, 0.25, 0.25], "together: the mass of one spleen"))):
    y = 6.6 - 3.4 * j
    bio.label(ax, (21.6, y + 0.9), name, size="small", ha="left")
    for i, s in enumerate(sizes):
        r = 0.55 * np.sqrt(s)
        ax.add_patch(Ellipse((22.5 + 1.6 * i, y), 2 * r * 1.3, 2 * r, facecolor=P.fill("receptor" if j == 0 else "blood"),
                             edgecolor=P.edge("receptor" if j == 0 else "blood"), lw=0.8, zorder=5))
    bio.label(ax, (21.6, y - 1.0), note, size="tiny", color=P.muted(), ha="left")
