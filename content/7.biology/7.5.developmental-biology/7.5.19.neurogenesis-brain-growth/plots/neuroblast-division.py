"""Asymmetric division of a fruit-fly neuroblast. (A) The neuroblast delaminates basally (inwards) from the
neuroectoderm. At mitosis the Par complex (Bazooka/Par-3, Par-6, aPKC) and Inscuteable-Pins-Mud form an apical
crescent; aPKC phosphorylates the fate determinants Numb, Prospero and Brat (with their adaptors Miranda and Pon)
so that they localize to the basal cortex, and Pins-Mud orients the spindle along the apical-basal axis. (B) The
division is unequal in size and in fate: the large apical daughter renews the neuroblast, the small basal daughter,
the ganglion mother cell (GMC), inherits Numb (which blocks Notch), Prospero (which enters the nucleus, stops
proliferation and activates neuronal genes) and Brat, and divides once more into two neurons or glia. (C) Successive
GMCs born from one neuroblast express a temporal series of transcription factors, so birth order gives each neuron
a distinct identity."""
import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, Wedge

fig, ax = bio.canvas(22, 8.2)
P = bio.P
ne = "protein"
bio.panel(ax, "A", (0.2, 8.0))
# neuroectoderm epithelium on top (apical = outside, up)
for k in range(9):
    bio.box(ax, (0.9 + k * 0.62, 6.6), 0.58, 1.0, token="channel", radius=0.08)
bio.label(ax, (3.4, 7.45), "neuroectoderm (apical side up)", size="tiny", color=P.muted())
c = (3.4, 3.8)
ax.add_patch(Circle(c, 1.55, facecolor=P.fill(ne), edgecolor=P.edge(ne), lw=1.2, zorder=4))
ax.add_patch(Wedge(c, 1.55, 55, 125, width=0.22, facecolor=P.fill("positive"), edgecolor=P.edge("positive"), lw=0.8, zorder=5))
ax.add_patch(Wedge(c, 1.55, 235, 305, width=0.22, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.8, zorder=5))
# spindle
for dx in (-0.5, -0.25, 0, 0.25, 0.5):
    ax.plot([c[0], c[0] + dx], [c[1] + 0.95, c[1]], color=P.edge("dna"), lw=0.6, zorder=6)
    ax.plot([c[0], c[0] + dx], [c[1] - 0.95, c[1]], color=P.edge("dna"), lw=0.6, zorder=6)
ax.add_patch(Ellipse(c, 0.9, 0.2, facecolor=P.fill("chromatin"), edgecolor=P.edge("chromatin"), lw=0.6, zorder=7))
for y in (c[1] + 0.95, c[1] - 0.95):
    ax.add_patch(Circle((c[0], y), 0.09, color=P.edge("dna"), zorder=7))
bio.callout(ax, (c[0] - 0.3, c[1] + 1.45), (0.8, 5.6), "Par-3/Par-6/aPKC, Insc, Pins")
bio.callout(ax, (c[0] + 0.3, c[1] - 1.45), (0.4, 1.3), "Numb, Prospero, Brat (Miranda)")
bio.callout(ax, (c[0] + 0.45, c[1] + 0.4), (5.9, 4.6), "spindle")
bio.label(ax, (c[0], 0.45), "neuroblast in mitosis", size="small", bold=True)
bio.arrow(ax, (6.0, 3.8), (7.6, 3.8), kind="process", head=0.18)

bio.panel(ax, "B", (8.0, 8.0))
nb = (10.0, 4.6)
ax.add_patch(Circle(nb, 1.3, facecolor=P.fill(ne), edgecolor=P.edge(ne), lw=1.2, zorder=4))
ax.add_patch(Circle(nb, 0.45, facecolor=P.light("nucleus"), edgecolor=P.edge("nucleus"), lw=0.7, zorder=5))
bio.label(ax, (nb[0], nb[1] + 1.7), "neuroblast (self-renews)", size="small")
g = (10.0, 2.55)
ax.add_patch(Circle(g, 0.6, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=1.1, zorder=4))
ax.add_patch(Circle(g, 0.25, facecolor=P.edge("negative"), edgecolor="none", zorder=5))
bio.label(ax, (g[0] + 1.0, g[1]), "GMC", size="small", ha="left")
for k, x in enumerate((9.2, 10.8)):
    ax.add_patch(Circle((x, 0.75), 0.42, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=1.0, zorder=4))
    bio.arrow(ax, (g[0] + (x - g[0]) * 0.3, g[1] - 0.6), (x, 1.2), kind="process", head=0.12, lw=0.9)
bio.label(ax, (12.0, 0.75), "2 neurons or glia", size="small", ha="left")
bio.arrow(ax, (12.2, 4.6), (13.2, 4.6), kind="process", head=0.15)
bio.label(ax, (12.7, 5.0), "repeat", size="tiny", color=P.muted())

bio.panel(ax, "C", (13.8, 8.0))
genes = [("Hb", "receptor"), ("Kr", "antibody"), ("Pdm", "enzyme"), ("Cas", "dna"), ("Grh", "k")]
for k, (gname, tok) in enumerate(genes):
    x = 14.8 + k * 1.45
    bio.box(ax, (x, 5.6), 1.25, 0.6, token=tok, text=gname, size="small")
    ax.add_patch(Circle((x, 4.2), 0.42, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0))
    bio.label(ax, (x, 3.4), f"GMC {k + 1}", size="tiny", color=P.muted())
    if k:
        bio.arrow(ax, (x - 1.45 + 0.65, 5.6), (x - 0.65, 5.6), kind="process", head=0.1, lw=0.8)
bio.arrow(ax, (14.4, 2.6), (20.8, 2.6), kind="process", head=0.16)
bio.label(ax, (17.6, 2.2), "time (birth order)", size="tiny", color=P.muted())
bio.label(ax, (17.6, 6.6), "temporal transcription factors in the neuroblast", size="small")
