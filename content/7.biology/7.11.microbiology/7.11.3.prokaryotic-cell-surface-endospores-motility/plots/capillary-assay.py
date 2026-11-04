"""Capillary assay for chemotaxis. A: schematic. B: attractant profile outside the capillary mouth,
modelled as a sphere of radius a held at concentration c0 in an infinite medium:
c(r, t) = c0 (a / r) erfc((r - a) / (2 sqrt(D t)))."""
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle
from scipy.special import erfc

import wikibio as bio
from wikibio import charts
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(28, 11)
bio.panel(ax, "A", (0.2, 10.8))
# suspension chamber
ax.add_patch(FancyBboxPatch((1.0, 1.0), 11.5, 4.2, boxstyle="round,pad=0,rounding_size=0.3",
                            facecolor=P.fill("extracellular"), edgecolor=P.ink(), lw=1.2, zorder=2))
bio.label(ax, (6.7, 0.5), "suspension of motile bacteria", size="tiny", color=P.muted())
rng = np.random.default_rng(1)
mouth = (6.7, 3.4)


def capillary(xm, tok, n_in, crowd):
    # tube rising from the mouth at xm, angled
    ax.add_patch(Rectangle((xm - 0.28, 3.4), 0.56, 6.6, facecolor=P.light(tok) if tok else P.surface(),
                           edgecolor=P.ink(), lw=1.0, zorder=4))
    for _ in range(n_in):
        M.bacillus(ax, (xm + rng.uniform(-0.12, 0.12), rng.uniform(3.6, 5.6)), 0.28, 0.1, angle=rng.uniform(0, 180),
                   token="bacterium", zorder=6)
    for _ in range(crowd):
        a, r = rng.uniform(np.pi, 2 * np.pi), rng.uniform(0.3, 1.3)
        M.bacillus(ax, (xm + r * np.cos(a), 3.4 + 0.7 * r * np.sin(a)), 0.28, 0.1, angle=rng.uniform(0, 180),
                   token="bacterium", zorder=6)


for _ in range(70):
    M.bacillus(ax, (rng.uniform(1.4, 12.1), rng.uniform(1.3, 4.9)), 0.28, 0.1, angle=rng.uniform(0, 180),
               token="bacterium", zorder=3)
capillary(4.0, None, 2, 0)
capillary(9.4, "highlight", 22, 14)
bio.label(ax, (4.0, 10.4), "buffer", size="small")
bio.label(ax, (9.4, 10.4), "attractant", size="small")
bio.label(ax, (9.9, 4.6), "cells\naccumulate", size="tiny", color=P.muted(), ha="left")
# B: profiles
bio.panel(ax, "B", (14.2, 10.8))
pax = charts.axes_at(ax, (16.2, 1.8, 11.0, 8.0))
D = 5e-4          # mm^2 s^-1 (5e-10 m^2 s^-1)
a = 0.1           # mm, inner radius of the capillary
r = np.linspace(a, 3.0, 400)
toks = ["neutral", "enzyme", "dna", "negative"]
for tmin, tok in zip((1, 5, 15, 60), toks):
    t = tmin * 60.0
    c = (a / r) * erfc((r - a) / (2 * np.sqrt(D * t)))
    pax.plot(r, c, color=charts.line(tok), lw=1.6, label=f"{tmin} min")
pax.set_yscale("log")
pax.set_ylim(1e-3, 1.2)
pax.set_xlim(0, 3.0)
leg = pax.legend(loc="upper right", fontsize=6.8, frameon=False)
for tx in leg.get_texts():
    tx.set_color(P.ink())
charts.style_axes(pax, "distance from the capillary mouth r / mm", "c / c₀ (log scale)")
