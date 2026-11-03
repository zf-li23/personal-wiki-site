"""Beadle's estimate (Example 19.4.1): expected number of F2 plants out of 50 000 resembling one parent,
50000 (1/4)^n, for n = 1..8, against the observed ~100 (1 in 500); inset sketches of teosinte and maize
plant architecture."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(22, 9)
pax = charts.axes_at(ax, (2.0, 1.6, 10.5, 6.8))
n = np.arange(1, 9)
exp = 50000 * 0.25 ** n
pax.bar(n, exp, color=P.fill("plant"), edgecolor=P.edge("plant"), width=0.65)
pax.axhline(100, color=charts.line("negative"), lw=1.4, ls=(0, (4, 2)))
pax.text(8.4, 120, "observed: about 100 (1 in 500)", fontsize=FT["tiny"], color=charts.line("negative"), ha="right")
for k, v in zip(n, exp):
    pax.text(k, v * 1.25, f"{v:,.0f}" if v >= 1 else f"{v:.2f}", ha="center", fontsize=FT["tiny"], color=P.ink())
pax.set_yscale("log")
pax.set_ylim(0.3, 3e4)
pax.set_xticks(n)
charts.style_axes(pax, "number of independent loci n", "expected F2 plants like one parent (of 50 000)")


def plant(x0, y0, kind):
    """Schematic plant: stem, lateral branches, tassels (male) and ears (female)."""
    stem = P.edge("plant")
    ax.plot([x0, x0], [y0, y0 + 5.2], color=stem, lw=2.2)
    bio.box(ax, (x0, y0 + 5.6), 0.35, 0.8, "highlight", radius=0.1, lw=0.6)
    for k, (yy, side) in enumerate(((y0 + 1.4, -1), (y0 + 2.4, 1), (y0 + 3.4, -1), (y0 + 4.2, 1))):
        if kind == "teosinte":
            L = 1.7 - 0.25 * k
            xe = x0 + side * L
            ax.plot([x0, xe], [yy, yy + 0.9], color=stem, lw=1.5)
            bio.box(ax, (xe, yy + 1.2), 0.25, 0.55, "highlight", radius=0.08, lw=0.5)
            bio.box(ax, (x0 + side * 0.6, yy + 0.25), 0.18, 0.35, "plant", radius=0.06, lw=0.5)
        elif k in (1, 2):
            xe = x0 + side * 0.45
            ax.plot([x0, xe], [yy, yy + 0.3], color=stem, lw=1.5)
            bio.box(ax, (xe + side * 0.25, yy + 0.55), 0.45, 1.1, "plant", radius=0.15, lw=0.6)
    bio.label(ax, (x0, y0 - 0.45), kind, size="small", italic=False)


plant(15.6, 2.0, "teosinte")
plant(19.6, 2.0, "maize")
bio.label(ax, (17.6, 8.6), "tassels (male): yellow; ears (female): green", size="tiny", color=P.muted())
