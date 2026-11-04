"""Cell inclusions (schematic) and a buoyancy model for gas vesicles: mean cell density
rho = (1 - f) rho_c + f rho_v against the vesicle volume fraction f (Eq. 3.1)."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, RegularPolygon

import wikibio as bio
from wikibio import charts
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(28, 11)
# ---- A: cell with inclusions
bio.panel(ax, "A", (0.2, 10.8))
cx, cy, L, W = 7.6, 5.6, 12.0, 6.0
M.bacillus(ax, (cx, cy), L, W, token="cytoplasm", zorder=3)
rng = np.random.default_rng(4)
# nucleoid
ax.add_patch(Ellipse((cx + 0.3, cy + 0.2), 3.4, 1.8, facecolor=P.light("dna"), edgecolor=P.edge("dna"), lw=0.8,
                     ls="--", zorder=5))
bio.label(ax, (cx + 0.3, cy + 0.2), "nucleoid", size="tiny", color=P.on_fill(), zorder=8)
# PHB granules
for x, y, r in [(3.6, 6.6, 0.55), (4.6, 7.3, 0.42), (4.2, 5.4, 0.5)]:
    ax.add_patch(Circle((x, y), r, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=1.0, zorder=6))
# glycogen: many small dots
for _ in range(26):
    ax.plot(rng.uniform(8.8, 10.8), rng.uniform(3.4, 4.6), "o", ms=2.6, color=P.fill("carbohydrate"),
            markeredgecolor=P.edge("carbohydrate"), markeredgewidth=0.4, zorder=6)
# polyphosphate
for x, y in [(6.3, 4.1), (7.15, 3.85)]:
    ax.add_patch(Circle((x, y), 0.38, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=1.0, zorder=6))
# sulfur globules at the periphery
for x, y in [(11.2, 7.6), (12.3, 6.9)]:
    ax.add_patch(Circle((x, y), 0.4, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=6))
# magnetosome chain
for k in range(8):
    ax.add_patch(RegularPolygon((3.8 + 0.42 * k, 3.0 + 0.0 * k), 6, radius=0.17, facecolor=P.ink(), edgecolor=P.ink(),
                                zorder=7))
ax.plot([3.6, 7.0], [3.0, 3.0], color=P.muted(), lw=0.8, zorder=6)
# gas vesicles: cluster of spindles
for k in range(9):
    x, y = 9.4 + 0.55 * (k % 3), 6.9 + 0.45 * (k // 3)
    ax.add_patch(Ellipse((x, y), 0.85, 0.28, angle=15, facecolor=P.surface(), edgecolor=P.edge("neutral"), lw=1.0,
                         zorder=6))
# carboxysomes: hexagons
for x, y in [(12.4, 4.6), (11.6, 4.0)]:
    ax.add_patch(RegularPolygon((x, y), 6, radius=0.4, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=1.0,
                                zorder=6))
c = 14.4
bio.callout(ax, (3.6, 7.15), (1.4, 9.6), "PHB granules")
bio.callout(ax, (9.9, 4.6), (9.4, 1.4), "glycogen")
bio.callout(ax, (7.15, 3.5), (5.4, 1.4), "polyphosphate")
bio.callout(ax, (4.6, 2.85), (1.6, 1.4), "magnetosome chain")
bio.callout(ax, (11.2, 8.0), (11.0, 9.8), "sulfur globules")
bio.callout(ax, (9.95, 7.95), (7.2, 9.8), "gas vesicles")
bio.callout(ax, (12.8, 4.4), (13.6, 1.6), "carboxysomes")
# ---- B: buoyancy model
bio.panel(ax, "B", (15.6, 10.8))
pax = charts.axes_at(ax, (17.6, 1.6, 9.6, 8.2))
f = np.linspace(0, 0.25, 200)
rv = 0.12
for rc, tok in [(1.05, "positive"), (1.10, "neutral"), (1.15, "negative")]:
    rho = (1 - f) * rc + f * rv
    pax.plot(f * 100, rho, color=charts.line(tok), lw=1.6)
    fs = (rc - 1.0) / (rc - rv)
    pax.plot([fs * 100], [1.0], "o", ms=4.5, color=charts.line(tok))
    pax.plot([], [], color=charts.line(tok), lw=1.6, label=f"rest of cell {rc:.2f} g cm⁻³")
pax.axhline(1.0, color=P.muted(), lw=0.9, ls="--")
pax.text(0.5, 1.005, "density of water", fontsize=6.8, color=P.muted(), va="bottom")
pax.text(13, 0.90, "floats", fontsize=7.5, color=P.ink())
pax.text(2, 1.12, "sinks", fontsize=7.5, color=P.ink())
pax.set_xlim(0, 25)
leg = pax.legend(loc="upper right", fontsize=6.8, frameon=False)
for t in leg.get_texts():
    t.set_color(P.ink())
pax.set_ylim(0.85, 1.17)
pax.set_xticks([0, 5, 10, 15, 20, 25])
charts.style_axes(pax, "gas-vesicle volume fraction f / %", "mean cell density / (g cm⁻³)")
