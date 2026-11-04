"""Heterocyst differentiation in a filament of Anabaena.
A: the filament. Under nitrogen starvation about one cell in ten becomes a heterocyst: it degrades
photosystem II and the phycobilisomes, adds glycolipid and polysaccharide layers that slow the entry of
oxygen, respires strongly, and fixes nitrogen. Fixed nitrogen (glutamine) moves to the vegetative cells
through the septal junctions, and fixed carbon (sucrose) moves the other way. Akinetes, thick-walled
resting cells, form in the same filament under other conditions.
B: the regulatory circuit. Nitrogen starvation raises 2-oxoglutarate, which activates NtcA; NtcA and
HetR activate each other, and HetR activates its own gene -- local self-activation. HetR also induces
the small peptides PatS and HetN, whose processed product (the pentapeptide RGSGR) moves to the
neighbouring cells and promotes the degradation of HetR there -- lateral inhibition. The spacing of the
heterocysts follows from the two feedbacks; the pattern is modelled in 7.6.36."""

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(25.0, 9.0)
bio.panel(ax, "A", (0.2, 8.9))

y0 = 6.4
n = 13
w = 1.55
het = {2, 11}
for k in range(n):
    x = 1.6 + k * w
    if k in het:
        ax.add_patch(Ellipse((x, y0), w * 0.95, 1.5, facecolor=P.fill("carbohydrate"),
                             edgecolor=P.edge("carbohydrate"), lw=2.6, zorder=8))
        ax.add_patch(Ellipse((x, y0), w * 0.75, 1.15, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("bacterium"),
                             lw=1.2, zorder=9))
        bio.label(ax, (x, y0), "N₂ → NH₃", size="tiny", zorder=12)
    else:
        ax.add_patch(FancyBboxPatch((x - w * 0.46, y0 - 0.6), w * 0.92, 1.2,
                                    boxstyle="round,pad=0,rounding_size=0.18", facecolor=P.fill("chloroplast"),
                                    edgecolor=P.edge("chloroplast"), lw=1.2, zorder=8))
        if k in (5, 8):
            bio.label(ax, (x, y0), "CO₂ → CH₂O", size="tiny", color=P.on_fill(), zorder=12)
bio.callout(ax, (1.6 + 2 * w, y0 - 0.8), (1.6 + 2 * w - 0.6, y0 - 2.2), "heterocyst: no photosystem II,\nthick envelope, micro-oxic", size="tiny")
bio.callout(ax, (1.6 + 8 * w, y0 + 0.65), (1.6 + 9 * w, y0 + 2.1), "vegetative cells: oxygenic photosynthesis", size="tiny")
xa, xb = 1.6 + 2 * w, 1.6 + 11 * w
bio.arrow(ax, (xa + 0.7, y0 + 0.95), (xb - 0.7, y0 + 0.95), kind="process", lw=1.0, head=0.18,
          color=P.edge("metabolite"))
bio.label(ax, ((xa + xb) / 2, y0 + 1.35), "glutamine (fixed N)", size="tiny", color=P.edge("metabolite"))
bio.arrow(ax, (xb - 0.7, y0 - 0.95), (xa + 0.7, y0 - 0.95), kind="process", lw=1.0, head=0.18,
          color=P.edge("plant"))
bio.label(ax, ((xa + xb) / 2, y0 - 1.35), "sucrose (fixed C)", size="tiny", color=P.edge("plant"))
bio.label(ax, (23.0, y0), "about 1 cell\nin 10", size="tiny", color=P.muted())

# ---- B circuit
bio.panel(ax, "B", (0.2, 3.3))
cy = 1.6
ax.add_patch(FancyBboxPatch((2.4, cy - 1.2), 7.0, 2.6, boxstyle="round,pad=0,rounding_size=0.3",
                            facecolor=P.fill("cytoplasm"), edgecolor=P.edge("bacterium"), lw=1.4, zorder=2))
bio.label(ax, (5.9, cy + 1.65), "differentiating cell", size="tiny", color=P.muted())
ax.add_patch(FancyBboxPatch((11.4, cy - 1.2), 7.0, 2.6, boxstyle="round,pad=0,rounding_size=0.3",
                            facecolor=P.fill("chloroplast"), edgecolor=P.edge("bacterium"), lw=1.4, zorder=2))
bio.label(ax, (14.9, cy + 1.65), "neighbouring vegetative cell", size="tiny", color=P.muted())

bio.box(ax, (3.9, cy + 0.5), 2.0, 0.7, token="metabolite", text="2-oxoglutarate", size="tiny", radius=0.22, zorder=10)
bio.box(ax, (6.6, cy + 0.5), 1.4, 0.7, token="positive", text="NtcA", size="tiny", radius=0.22, zorder=10)
bio.box(ax, (6.6, cy - 0.7), 1.4, 0.7, token="enzyme", text="HetR", size="tiny", radius=0.22, zorder=10)
bio.box(ax, (8.8, cy - 0.7), 1.4, 0.7, token="drug", text="PatS,\nHetN", size="tiny", radius=0.22, zorder=10)
bio.arrow(ax, (4.9, cy + 0.5), (5.9, cy + 0.5), kind="activation", lw=1.0, head=0.18)
bio.arrow(ax, (6.4, cy + 0.15), (6.4, cy - 0.35), kind="activation", lw=1.0, head=0.18)
bio.arrow(ax, (6.8, cy - 0.35), (6.8, cy + 0.15), kind="activation", lw=1.0, head=0.18)
bio.arrow(ax, (6.4, cy - 1.05), (7.2, cy - 1.05), kind="activation", lw=1.0, head=0.16, bend=0.4)
bio.label(ax, (6.9, cy - 1.55), "self-activation", size="tiny", color=P.muted())
bio.arrow(ax, (7.3, cy - 0.7), (8.1, cy - 0.7), kind="activation", lw=1.0, head=0.18)
bio.box(ax, (13.0, cy - 0.7), 1.8, 0.7, token="drug", text="RGSGR", size="tiny", radius=0.22, zorder=10)
bio.box(ax, (16.4, cy - 0.7), 1.4, 0.7, token="enzyme", text="HetR", size="tiny", radius=0.22, zorder=10)
bio.arrow(ax, (9.5, cy - 0.7), (12.1, cy - 0.7), kind="process", lw=1.1, head=0.2)
bio.label(ax, (10.8, cy - 0.25), "diffuses through\nthe septal junctions", size="tiny", color=P.muted())
bio.arrow(ax, (13.9, cy - 0.7), (15.7, cy - 0.7), kind="inhibition", lw=1.1, head=0.2)
bio.label(ax, (16.4, cy + 0.5), "degraded: no differentiation", size="tiny", color=P.muted())
bio.label(ax, (21.4, cy + 0.2), "local self-activation\n+ lateral inhibition\n= regular spacing", size="tiny")
