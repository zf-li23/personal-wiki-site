"""Heterometry in Darwin's finches: beak depth and length as two developmental axes (schematic).

Beak profiles are drawn as a family of shapes y = D (1 - x / L)^0.8 (upper bill) and a shallower lower bill,
varying depth D and length L; Campas et al. (2011) showed that the beak shapes of the ground and cactus finches
are related by such scaling transformations. Abzhanov and colleagues found that earlier and stronger BMP4
expression in the mesenchyme of the embryonic upper beak correlates with deeper and broader beaks
(experimentally, more BMP4 in the chick frontonasal mesenchyme deepens the beak), and higher calmodulin (CaM)
expression with longer beaks. Species are placed qualitatively: Geospiza magnirostris (large ground finch,
deep), G. fortis (medium ground finch), G. fuliginosa (small ground finch), G. scandens (common cactus finch,
long and narrow), G. conirostris (large cactus finch, long and deep).
"""

import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22.0, 14.0)


def beak(x0, y0, L, D, tok):
    x = np.linspace(0, L, 80)
    up = y0 + D * (1 - x / L) ** 0.8
    lo = y0 - 0.55 * D * (1 - x / L) ** 1.1
    ax.fill_between(x0 + x, lo, up, color=P.fill(tok), lw=0, zorder=6)
    ax.plot(x0 + x, up, color=P.edge(tok), lw=1.0, zorder=7)
    ax.plot(x0 + x, lo, color=P.edge(tok), lw=1.0, zorder=7)
    ax.plot([x0, x0 + L], [y0, y0], color=P.edge(tok), lw=0.6, zorder=7)
    ax.plot([x0, x0], [lo[0], up[0]], color=P.edge(tok), lw=1.0, zorder=7)


species = [("G. fuliginosa", 1.3, 0.6, (3.0, 2.8)), ("G. fortis", 1.6, 1.0, (3.0, 6.3)),
           ("G. magnirostris", 2.0, 1.6, (3.0, 10.2)), ("G. scandens", 3.0, 0.75, (12.0, 3.6)),
           ("G. conirostris", 2.9, 1.35, (12.0, 9.6))]
for name, L, D, (x0, y0) in species:
    beak(x0, y0, L, D, "bone")
    bio.label(ax, (x0 + L / 2, y0 - 0.55 * D - 0.6), name, size="tiny", italic=True)
bio.arrow(ax, (1.0, 1.2), (1.0, 12.8), kind="process")
bio.label(ax, (0.55, 7.0), "deeper beak: earlier, stronger BMP4", size="small", rotation=90)
bio.arrow(ax, (1.6, 0.6), (20.8, 0.6), kind="process")
bio.label(ax, (11.2, 0.15), "longer beak: higher calmodulin", size="small")
bio.label(ax, (7.5, 13.4), "ground finches", size="small", bold=True)
bio.label(ax, (16.5, 13.4), "cactus finches", size="small", bold=True)
