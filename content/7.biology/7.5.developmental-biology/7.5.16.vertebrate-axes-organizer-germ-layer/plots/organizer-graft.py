# The organizer graft of Spemann and Mangold (1924), in the design of the original experiment and with the
# interpretation of its outcome. A: the dorsal blastopore lip of an early gastrula of a lightly pigmented newt
# species (donor, outlined) is grafted into the ventral side of a gastrula of a pigmented species (host). B: the host
# develops a second body axis; in a cross-section of the resulting twin, the primary axis (top) is entirely host tissue,
# while in the secondary axis (bottom) the notochord and part of the somites derive from the graft (dashed outline)
# and the neural tube, most of the somites and the gut lining are host tissue: the graft differentiated according
# to its origin (self-differentiation) and induced neighbouring host cells to form axial structures (induction).
import numpy as np
import wikibio as bio
from wikibio import bodyaxes as BA
from matplotlib.patches import Circle, Ellipse

fig, ax = bio.canvas(23.0, 10.0)
P = bio.P
bio.panel(ax, "A", (0.2, 9.8))
d = BA.amphibian(ax, (3.0, 6.2), 1.8, stage="gastrula")
bio.label(ax, (3.0, 8.6), "donor (unpigmented species)", size="small")
h = BA.amphibian(ax, (8.6, 6.2), 1.8, stage="gastrula")
bio.label(ax, (8.6, 8.6), "host (pigmented species)", size="small")
ax.add_patch(Circle(d["dorsal_lip"], 0.45, facecolor="none", edgecolor=P.ink(), lw=1.2, ls=(0, (3, 2)), zorder=30))
target = h["ventral_mesoderm"]
ax.add_patch(Circle(target, 0.45, facecolor="none", edgecolor=P.ink(), lw=1.2, ls=(0, (3, 2)), zorder=30))
bio.arrow(ax, (d["dorsal_lip"][0] + 0.3, d["dorsal_lip"][1] - 0.5), (target[0] - 0.1, target[1] - 0.55), kind="process", bend=-0.25)
bio.label(ax, (5.8, 2.6), "graft dorsal lip\ninto ventral side", size="small")
bio.callout(ax, h["dorsal_lip"], (11.2, 4.0), "host's own\ndorsal lip")

bio.panel(ax, "B", (12.0, 9.8))
c = (17.4, 5.2)
ax.add_patch(Ellipse(c, 8.4, 8.6, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=1.2, zorder=5))
ax.add_patch(Ellipse(c, 7.8, 8.0, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cytoplasm"), lw=0.8, zorder=5.1))
ax.add_patch(Ellipse(c, 3.2, 1.8, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=5.2))
ax.add_patch(Ellipse(c, 1.6, 0.5, facecolor=P.fill("vacuole"), edgecolor=P.edge("vacuole"), lw=0.8, zorder=5.3))


def axis_set(y0, s, graft):
    # neural tube (host ectoderm), notochord, somites
    nt = (c[0], y0)
    ax.add_patch(Circle(nt, 0.6, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=1.1, zorder=7))
    ax.add_patch(Circle(nt, 0.18, facecolor=P.fill("vacuole"), edgecolor=P.edge("vacuole"), lw=0.6, zorder=7.1))
    no = (c[0], y0 - s * 0.95)
    ax.add_patch(Circle(no, 0.32, facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=1.1, zorder=7,
                        ls=(0, (3, 2)) if graft else "-"))
    for side in (-1, 1):
        sm = (c[0] + side * 1.35, y0 - s * 0.6)
        ax.add_patch(Ellipse(sm, 0.95, 1.2, facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=1.0, zorder=7))
        if graft and side == 1:
            ax.add_patch(Ellipse((sm[0] - 0.15, sm[1]), 0.45, 0.6, facecolor=P.light("muscle"), edgecolor=P.ink(), lw=0.9,
                                 ls=(0, (3, 2)), zorder=7.2))
    return nt, no


nt1, no1 = axis_set(c[1] + 2.9, 1, False)
nt2, no2 = axis_set(c[1] - 2.9, -1, True)
bio.callout(ax, nt1, (21.9, 9.2), "primary neural tube (host)")
bio.callout(ax, no1, (22.2, 7.4), "notochord (host)")
bio.callout(ax, nt2, (22.0, 1.0), "secondary neural tube (host)")
bio.callout(ax, no2, (22.6, 3.0), "notochord (graft)")
bio.callout(ax, (c[0] + 1.2, c[1] - 2.3), (22.8, 5.2), "somite: graft + host")
bio.callout(ax, (c[0], c[1] + 0.6), (13.2, 5.2), "gut")
bio.label(ax, (17.4, 0.25), "dashed: graft-derived", size="tiny", color=P.muted())
