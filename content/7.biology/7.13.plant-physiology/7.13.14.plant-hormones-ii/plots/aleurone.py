# Gibberellin induction of hydrolases in the cereal aleurone layer (left, schematic) and the
# dose-response of isolated aleurone layers to GA3 (right, Hill curves, illustrative; EC50 ~ 3 nM),
# with ABA shifting the curve to the right and lowering the maximum.
import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse
from wikibio import charts

fig, ax = bio.canvas(24, 10)
P = bio.P
# grain: outer aleurone ring and starchy endosperm
cx, cy, rx, ry = 6.2, 5.0, 5.4, 3.3
ax.add_patch(Ellipse((cx, cy), 2 * rx, 2 * ry, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.4, zorder=2))
ax.add_patch(Ellipse((cx, cy), 2 * rx - 0.9, 2 * ry - 0.9, facecolor=P.fill("bone"), edgecolor=P.edge("bone"),
                     lw=1.0, zorder=3))
# embryo at the left end
emb = bio.blob((1.7, 4.4), 1.25, 1.7, wobble=0.06, seed=4)
bio.shape(ax, emb, token="plant", lw=1.2, zorder=4)
bio.label(ax, (1.7, 4.2), "Embryo", size="small", color=P.on_fill(), zorder=6)
bio.label(ax, (7.0, 5.0), "Starchy endosperm", size="small", zorder=6, color=P.on_fill())
bio.callout(ax, (cx + 2.4, cy + ry - 0.25), (11.0, 9.4), "Aleurone layer")
bio.callout(ax, (2.9, 4.0), (3.0, 0.6), "Scutellum")
# GA diffusion and enzyme secretion
bio.arrow(ax, (2.6, 5.7), (5.4, 7.75), kind="process", bend=-0.15, color=P.edge("plant"))
bio.label(ax, (3.6, 7.2), "1–2 GA", size="small", color=P.on_fill(), zorder=6)
for x in (6.5, 8.6):
    bio.arrow(ax, (x, 7.75), (x - 0.4, 6.3), kind="process", color=P.edge("highlight"))
bio.label(ax, (11.9, 7.3), "3 α-amylase,\nprotease", size="small", ha="left")
bio.label(ax, (8.0, 3.6), "4 starch → sugars\nprotein → amino acids", size="tiny", zorder=6, color=P.on_fill())
bio.arrow(ax, (6.0, 3.2), (3.0, 3.4), kind="process", bend=0.12, color=P.on_fill())
bio.label(ax, (4.6, 2.25), "5 uptake", size="tiny", zorder=6, color=P.on_fill())

# dose-response panel
pax = charts.axes_at(ax, (15.0, 1.6, 8.0, 7.2))
c = np.logspace(-12, -5, 300)


def hill(c, ec50, emax, n=1.0):
    return emax * c ** n / (ec50 ** n + c ** n)


pax.plot(c, hill(c, 3e-9, 100), color=charts.line("plant"), lw=2.3, label="GA₃")
pax.plot(c, hill(c, 3e-8, 60), color=charts.line("negative"), lw=2.0, ls="--", label="GA₃ + ABA")
pax.set_xscale("log")
pax.set_ylim(0, 110)
pax.set_xlim(1e-12, 1e-5)
pax.axvline(3e-9, color=P.muted(), lw=0.8, ls=":")
pax.text(3.5e-9, 6, "EC₅₀", fontsize=8, color=P.muted())
pax.legend(frameon=False, fontsize=8.5, loc="upper left", labelcolor=P.ink())
charts.style_axes(pax, "[GA₃] / (mol L⁻¹)", "α-Amylase released / % of max")
