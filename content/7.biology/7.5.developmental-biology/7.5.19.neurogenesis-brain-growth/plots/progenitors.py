"""Neural progenitors of the developing neocortex. (A) Interkinetic nuclear migration: in a neuroepithelial or
apical radial glial cell, which spans the whole wall, the nucleus moves basally in G1, replicates its DNA (S) at
the basal side of the ventricular zone, returns in G2 and divides (M) at the apical, ventricular surface. (B) Lineage
relations: neuroepithelial cells (NE) divide symmetrically to expand the pool, then become apical radial glia (aRG).
aRG divide asymmetrically, renewing themselves and producing a neuron directly or an intermediate progenitor (IP),
which divides once or a few times in the subventricular zone to make neurons. Outer radial glia (oRG), abundant in
primates, keep only the basal fibre and divide repeatedly in the outer SVZ; at the end of neurogenesis radial glia
make astrocytes and oligodendrocyte precursors and the remaining cells become ependymal cells."""
import numpy as np
import wikibio as bio
from wikibio import neurodev as N
from matplotlib.patches import Circle, Ellipse

fig, ax = bio.canvas(23.2, 9.0)
P = bio.P
ne = N.TISSUE["neural"]
bio.panel(ax, "A", (0.2, 8.9))
y0, y1 = 1.2, 7.6
ax.add_patch(__import__("matplotlib").patches.Rectangle((0.8, y0), 9.0, y1 - y0, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("neutral"), lw=0.6))
bio.label(ax, (5.3, y0 - 0.35), "apical (ventricle)", size="tiny", color=P.muted())
bio.label(ax, (5.3, y1 + 0.3), "basal (pia)", size="tiny", color=P.muted())
phases = [("G1", 0.25), ("S", 0.75), ("G2", 0.4), ("M", 0.0), ("G1", 0.25)]
for k, (ph, f) in enumerate(phases):
    x = 1.7 + k * 1.85
    yc = y0 + 0.4 + f * (y1 - y0 - 1.2)
    if ph == "M":
        # rounded mitotic cell at the apical surface, two daughters of chromatin
        ax.add_patch(Circle((x, y0 + 0.55), 0.5, facecolor=P.fill(ne), edgecolor=P.edge(ne), lw=1.0, zorder=5))
        for dx in (-0.18, 0.18):
            ax.add_patch(Ellipse((x + dx, y0 + 0.55), 0.12, 0.5, facecolor=P.fill("chromatin"), edgecolor=P.edge("chromatin"), lw=0.6, zorder=6))
        ax.plot([x, x], [y0 + 1.05, y1], color=P.edge(ne), lw=0.9, zorder=4)
    else:
        ax.plot([x - 0.18, x - 0.18], [y0, y1], color=P.edge(ne), lw=0.9, zorder=4)
        ax.plot([x + 0.18, x + 0.18], [y0, y1], color=P.edge(ne), lw=0.9, zorder=4)
        ax.add_patch(Ellipse((x, yc), 0.5, 0.9, facecolor=P.fill(ne), edgecolor=P.edge(ne), lw=1.0, zorder=5))
        ax.add_patch(Ellipse((x, yc), 0.3, 0.55, facecolor=P.light("nucleus"), edgecolor=P.edge("nucleus"), lw=0.6, zorder=6))
    bio.label(ax, (x, y1 + 0.75), ph, size="small", bold=True)
    if k:
        bio.arrow(ax, (x - 1.55, y1 + 0.75), (x - 0.3, y1 + 0.75), kind="process", head=0.13, lw=0.9)

# (B) lineage diagram
bio.panel(ax, "B", (11.0, 8.9))
nodes = {"NE": (12.6, 6.8, ne), "NE2": (11.9, 4.9, ne), "NE3": (13.3, 4.9, ne), "aRG": (16.2, 6.8, "protein"),
         "aRG2": (15.2, 4.9, "protein"), "IP": (16.6, 4.9, "metabolite"), "N1": (16.1, 3.0, "neuron"), "N2": (17.2, 3.0, "neuron"),
         "oRG": (19.6, 6.8, "k"), "oRG2": (19.0, 4.9, "k"), "N3": (20.3, 4.9, "neuron"), "Glia": (22.0, 4.9, "carbohydrate")}
labels = {"NE2": "NE", "NE3": "NE", "aRG2": "aRG", "N1": "N", "N2": "N", "oRG2": "oRG", "N3": "N", "Glia": "astro/OPC"}
for k, (x, y, tok) in nodes.items():
    w = 1.15 if k != "Glia" else 1.7
    bio.box(ax, (x, y), w, 0.62, token=tok, text=labels.get(k, k), size="small")
for a, b in (("NE", "NE2"), ("NE", "NE3"), ("aRG", "aRG2"), ("aRG", "IP"), ("IP", "N1"), ("IP", "N2"), ("oRG", "oRG2"), ("oRG", "N3")):
    xa, ya, _ = nodes[a]
    xb, yb, _ = nodes[b]
    bio.arrow(ax, (xa, ya - 0.33), (xb, yb + 0.35), kind="process", head=0.12, lw=0.9)
bio.arrow(ax, (13.25, 6.8), (15.55, 6.8), kind="process", head=0.13, lw=0.9)
bio.label(ax, (14.4, 7.15), "RA, FGF10", size="tiny", color=P.muted())
bio.arrow(ax, (16.85, 6.8), (18.95, 6.8), kind="process", head=0.13, lw=0.9, dashed=True)
bio.label(ax, (17.9, 7.15), "oblique division", size="tiny", color=P.muted())
bio.arrow(ax, (20.15, 6.5), (21.7, 5.25), kind="process", head=0.13, lw=0.9, dashed=True)
bio.label(ax, (12.6, 4.2), "symmetric,", size="tiny", color=P.muted())
bio.label(ax, (12.6, 3.85), "proliferative", size="tiny", color=P.muted())
bio.label(ax, (15.2, 4.2), "asymmetric", size="tiny", color=P.muted())
bio.label(ax, (16.65, 2.3), "symmetric, neurogenic (SVZ)", size="tiny", color=P.muted())
bio.label(ax, (22.0, 4.2), "late: gliogenic switch", size="tiny", color=P.muted())
bio.label(ax, (12.6, 7.7), "VZ", size="small", bold=True)
bio.label(ax, (16.2, 7.7), "VZ", size="small", bold=True)
bio.label(ax, (19.6, 7.7), "outer SVZ", size="small", bold=True)
