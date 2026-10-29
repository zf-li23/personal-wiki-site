"""The three modes of cell specification (after the classification used by Gilbert).

A, autonomous: a cytoplasmic determinant (dots) localized in one region of the egg is inherited by the
blastomere formed from that region; isolated, that blastomere still forms its fate (muscle), and the embryo
lacking it lacks that fate. B, conditional: equivalent cells acquire fates from their neighbours and
position; a cell moved to a new position adopts the fate of its new position, and when cells are removed
the remaining ones regulate. C, syncytial: in a syncytium (an insect blastoderm before cellularization)
nuclei sit in shared cytoplasm with opposing gradients of determinants; each nucleus reads its position
from the ratio, and cell boundaries form only later.
"""

import numpy as np
from matplotlib.patches import Circle, Ellipse

import wikibio as bio
from wikibio import development as D

P = bio.P
fig, ax = bio.canvas(30, 10.5)
FATE = ["neutral", "muscle", "enzyme", "channel", "antibody"]

# ---------------------------------------------------------------- A autonomous
bio.panel(ax, "A", (0.2, 10.3))
bio.label(ax, (5.0, 9.7), "Autonomous specification", size="normal", bold=True)
rng = np.random.default_rng(1)


def egg_with_determinant(c, r, split=False):
    if not split:
        ax.add_patch(Circle(c, r, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=1.2, zorder=5))
    for _ in range(26):
        a = rng.uniform(-0.9, 0.9) - np.pi / 2
        d = rng.uniform(0.55, 0.9) * r
        p = (c[0] + d * np.cos(a) * 1.0, c[1] + d * np.sin(a))
        ax.add_patch(Circle(p, 0.06, facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=0.5, zorder=7))


egg_with_determinant((1.6, 6.8), 1.0)
bio.label(ax, (1.6, 5.4), "egg: determinant\nin one region", size="tiny")
bio.arrow(ax, (2.8, 6.8), (3.7, 6.8), kind="process")
# two-cell
for dx, tok in ((-0.52, "cytoplasm"), (0.52, "cytoplasm")):
    pass
c2 = (5.1, 6.8)
ax.add_patch(Ellipse((c2[0], c2[1] + 0.5), 1.9, 0.95, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=1.1, zorder=5))
ax.add_patch(Ellipse((c2[0], c2[1] - 0.5), 1.9, 0.95, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=1.1, zorder=5))
for _ in range(16):
    p = (c2[0] + rng.uniform(-0.7, 0.7), c2[1] - 0.5 + rng.uniform(-0.3, 0.25))
    ax.add_patch(Circle(p, 0.06, facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=0.5, zorder=7))
bio.arrow(ax, (6.3, 6.4), (7.6, 5.2), kind="process")
bio.arrow(ax, (6.3, 7.2), (7.6, 8.3), kind="process")
bio.label(ax, (8.95, 9.35), "isolated cell\nwithout determinant", size="tiny")
D.cell_row(ax, 7.9, 9.9, 8.45, [2, 2, 2], FATE, h=0.7)
bio.label(ax, (8.9, 7.75), "no muscle", size="tiny", color=P.muted())
bio.label(ax, (8.95, 3.75), "isolated cell\nwith determinant", size="tiny")
D.cell_row(ax, 7.9, 9.9, 5.0, [1, 1, 1], FATE, h=0.7)
bio.label(ax, (8.9, 4.4), "muscle in culture", size="tiny", color=P.muted())
bio.label(ax, (5.0, 1.55), "fate set by what the cell inherits;\nmosaic development; lineage invariant", size="small",
          color=P.muted())

# ---------------------------------------------------------------- B conditional
bio.panel(ax, "B", (10.6, 10.3))
bio.label(ax, (15.2, 9.7), "Conditional specification", size="normal", bold=True)
# a row of cells next to a signalling source; the signal falls off with distance
src = (11.3, 7.9)
ax.add_patch(Circle(src, 0.4, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=6))
bio.label(ax, (src[0], src[1] - 0.7), "source", size="tiny")
D.cell_row(ax, 12.0, 19.0, 7.9, [1, 1, 2, 2, 3, 3], FATE, h=0.75)
xs = np.linspace(12.0, 19.0, 60)
ax.fill_between(xs, 8.45, 8.45 + 0.55 * np.exp(-(xs - 12.0) / 2.2), color=P.fill("highlight"), lw=0, zorder=4)
bio.label(ax, (15.5, 9.2), "signal", size="tiny", color=P.edge("highlight"))
bio.label(ax, (15.5, 7.15), "normal: fates by distance from the source", size="tiny", color=P.muted())
# graft: the far cell (marked) is moved next to the source
row2 = D.cell_row(ax, 12.0, 19.0, 5.6, [1, 1, 2, 2, 3, 3], FATE, h=0.75)
ax.add_patch(Circle((row2[-1][0], row2[-1][1] + 0.55), 0.12, facecolor=P.ink(), edgecolor="none", zorder=12))
bio.arrow(ax, (row2[-1][0], 5.15), (12.2, 5.05), kind="process", bend=0.1, lw=1.0)
bio.label(ax, (15.5, 4.45), "graft the marked cell next to the source", size="tiny", color=P.muted())
row3 = D.cell_row(ax, 12.0 - 7.0 / 6, 19.0, 3.4, [1, 1, 1, 2, 2, 3, 3], FATE, h=0.75)
ax.add_patch(Circle((row3[0][0], row3[0][1] + 0.55), 0.12, facecolor=P.ink(), edgecolor="none", zorder=12))
bio.label(ax, (15.5, 2.65), "it adopts the fate of its new position", size="tiny", color=P.muted())
bio.label(ax, (15.5, 1.55), "fate set by signals and position;\nregulative development; lineage variable", size="small",
          color=P.muted())

# ---------------------------------------------------------------- C syncytial
bio.panel(ax, "C", (20.4, 10.3))
bio.label(ax, (25.2, 9.7), "Syncytial specification", size="normal", bold=True)
fly = D.FlyEmbryo(ax, (25.2, 7.0), length=8.0, height=2.8)
fly.gradients([(lambda f: np.exp(-f / 0.22), "receptor"), (lambda f: np.exp(-(1 - f) / 0.22), "dna")])
for k in range(15):
    f = 0.06 + 0.88 * k / 14
    x = fly.x(f)
    for yy in (7.95, 6.05):
        ax.add_patch(Circle((x, yy), 0.13, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.6, zorder=13))
bio.label(ax, (21.7, 8.75), "anterior determinant", size="tiny", color=P.edge("receptor"))
bio.label(ax, (28.7, 8.75), "posterior determinant", size="tiny", color=P.edge("dna"))
bio.label(ax, (25.2, 4.95), "nuclei share one cytoplasm and read their position", size="tiny", color=P.muted())
bio.arrow(ax, (25.2, 4.6), (25.2, 4.0), kind="process")
D.cell_row(ax, 21.4, 29.0, 3.4, [1, 1, 2, 2, 3, 3, 4, 4], FATE, h=0.7)
bio.label(ax, (25.2, 2.75), "cellularization: membranes enclose nuclei", size="tiny", color=P.muted())
bio.label(ax, (25.2, 1.55), "fate set by gradients in a syncytium;\nthen cells form", size="small", color=P.muted())
