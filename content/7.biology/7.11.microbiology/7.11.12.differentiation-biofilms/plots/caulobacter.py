"""The asymmetric cell cycle of Caulobacter crescentus.
A: the life cycle. A flagellated swarmer cell cannot replicate its chromosome; it sheds the flagellum,
builds a stalk with an adhesive holdfast at the pole where the flagellum was, replicates and segregates
its chromosome, and divides asymmetrically into a stalked cell, which starts again at once, and a new
swarmer cell, which must differentiate first. The phases are named after the eukaryotic cell cycle.
B: the three master regulators (schematic time courses over one cycle). CtrA-P is high in the swarmer
and blocks the origin of replication and the genes of the stalked program; its proteolysis at the
G1-to-S transition lets DnaA rise and fire the origin; GcrA then drives replication elongation, the
divisome and stalk synthesis, and CtrA reappears late and is inherited by the swarmer compartment."""

import numpy as np
from matplotlib.patches import Circle

import wikibio as bio
from wikibio import charts
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(26.0, 11.4)
bio.panel(ax, "A", (0.2, 11.3))


def stalk(x, y, length=1.4, angle=180, holdfast=True):
    a = np.radians(angle)
    x1, y1 = x + length * np.cos(a), y + length * np.sin(a)
    ax.plot([x, x1], [y, y1], color=P.edge("bacterium"), lw=2.6, solid_capstyle="round", zorder=5)
    if holdfast:
        ax.add_patch(Circle((x1, y1), 0.18, facecolor=P.fill("carbohydrate"), edgecolor=P.edge("carbohydrate"),
                            lw=1.0, zorder=6))


def nucleoid(c, rx=0.5, ry=0.25, seed=1):
    bio.shape(ax, bio.blob(c, rx, ry, wobble=0.12, seed=seed), token="dna", lw=0.8, zorder=10)


ys = 7.4
# 1 swarmer
M.vibrio(ax, (3.0, ys), 2.2, 0.85, bend=0.22, flagella="monotrichous", flagellum_length=1.5, gram="-")
nucleoid((3.0, ys))
bio.label(ax, (3.0, ys - 1.5), "swarmer (G1)\nno replication", size="tiny", color=P.muted())
# 2 differentiating
M.vibrio(ax, (8.0, ys), 2.2, 0.85, bend=0.22, flagella=None, gram="-")
stalk(6.95, ys - 0.1, 1.3, angle=200)
nucleoid((8.0, ys))
bio.label(ax, (8.0, ys - 1.9), "flagellum shed, pili lost,\nstalk and holdfast built (G1/S)", size="tiny",
          color=P.muted())
# 3 replicating stalked cell
M.vibrio(ax, (13.4, ys), 3.0, 0.9, bend=0.2, flagella=None, gram="-")
stalk(11.9, ys - 0.15, 1.3, angle=200)
nucleoid((12.6, ys), 0.5, 0.25, 2)
nucleoid((14.2, ys), 0.5, 0.25, 3)
bio.label(ax, (13.4, ys - 1.7), "replication and segregation (S);\nnew flagellum at the far pole", size="tiny",
          color=P.muted())
# 4 predivisional
M.vibrio(ax, (19.4, ys), 3.6, 0.9, bend=0.18, flagella="monotrichous", flagellum_length=1.4, gram="-")
stalk(17.6, ys - 0.2, 1.3, angle=200)
nucleoid((18.4, ys), 0.5, 0.25, 4)
nucleoid((20.4, ys), 0.5, 0.25, 5)
ax.plot([19.4, 19.4], [ys - 0.5, ys + 0.5], color=P.edge("bacterium"), lw=2.0, zorder=12)
bio.label(ax, (19.4, ys - 1.7), "predivisional cell (G2):\ntwo different poles", size="tiny", color=P.muted())
# 5 products
M.vibrio(ax, (24.2, ys + 1.2), 2.1, 0.8, bend=0.2, flagella=None, gram="-")
stalk(23.25, ys + 1.1, 1.1, angle=200)
nucleoid((24.2, ys + 1.2), 0.45, 0.22, 6)
M.vibrio(ax, (24.2, ys - 1.4), 2.1, 0.8, bend=0.2, flagella="monotrichous", flagellum_length=1.3, gram="-")
nucleoid((24.2, ys - 1.4), 0.45, 0.22, 7)
bio.label(ax, (24.2, ys + 2.3), "stalked cell:\ndivides again", size="tiny", color=P.muted())
bio.label(ax, (24.2, ys - 2.3), "swarmer: disperses", size="tiny", color=P.muted())
for a, b in (((4.6, ys), (6.3, ys)), ((9.6, ys), (11.3, ys)), ((15.4, ys), (17.0, ys))):
    bio.arrow(ax, a, b, kind="process", lw=1.0, head=0.16)
bio.arrow(ax, (21.6, ys + 0.3), (22.7, ys + 1.0), kind="process", lw=1.0, head=0.16)
bio.arrow(ax, (21.6, ys - 0.3), (22.7, ys - 1.1), kind="process", lw=1.0, head=0.16)
bio.arrow(ax, (25.6, ys - 1.4), (3.0, ys - 3.0), kind="process", lw=1.0, head=0.2, bend=0.1)
bio.label(ax, (14.0, ys - 3.55), "the swarmer must differentiate before it can divide", size="tiny", color=P.muted())

# ---- B
bio.panel(ax, "B", (0.2, 2.9))
pax = charts.axes_at(ax, (3.4, 0.7, 19.0, 2.0))
t = np.linspace(0, 1, 600)
bell = lambda c, w: np.exp(-((t - c) / w) ** 2)
ctra = bell(0.0, 0.2) + bell(1.0, 0.2) + 0.8 * bell(0.86, 0.1)
dnaa = bell(0.33, 0.1)
gcra = bell(0.58, 0.14)
for y, tok, ls, name in ((ctra, "enzyme", "-", "CtrA-P"), (dnaa, "dna", "--", "DnaA"), (gcra, "plant", "-.", "GcrA")):
    pax.plot(t, y / y.max(), color=charts.line(tok), lw=1.8, ls=ls, label=name)
for x, lab in ((0.0, "swarmer"), (0.3, "G1/S"), (0.62, "S"), (0.9, "division")):
    pax.axvline(x, color=P.muted(), lw=0.7, ls=":")
    pax.text(x + 0.01, 1.02, lab, fontsize=6.6, color=P.muted())
pax.set_xlim(0, 1)
pax.set_ylim(0, 1.3)
pax.set_yticks([])
pax.legend(fontsize=6.8, frameon=False, loc="upper right", ncol=3, bbox_to_anchor=(1.0, 1.32))
charts.style_axes(pax, "fraction of the cell cycle", "activity (a.u.)")
