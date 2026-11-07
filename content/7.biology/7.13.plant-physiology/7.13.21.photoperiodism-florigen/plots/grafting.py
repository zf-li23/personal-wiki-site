# Classic grafting experiments on the floral stimulus (schematic).
# A: Xanthium (SDP): five plants joined by approach grafts are kept in long days; only one leaf of the
#    first plant receives short days (dark box). All five plants flower: the stimulus made in the
#    induced leaf crosses the graft unions.
# B: Perilla (SDP): a leaf induced in short days, grafted onto a non-induced stock in long days, makes
#    the stock flower; a leaf from a long-day plant does not.
# C: a long-day plant (Hyoscyamus) grafted onto the short-day tobacco Maryland Mammoth in long days:
#    the tobacco stock flowers too, so the stimuli of LDPs and SDPs are interchangeable.
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import botany

fig, ax = bio.canvas(30, 10.5)
P = bio.P


def plant(x, y, h, flowers, nleaf=3, lean=0.0, leaf_len=1.1):
    """A simple upright plant: stem, alternate leaves, and flowers or a vegetative apex."""
    ax.plot([x, x + lean], [y, y + h], color=P.edge("plant"), lw=2.6, solid_capstyle="round", zorder=6)
    for k in range(nleaf):
        yy = y + h * (0.25 + 0.55 * k / max(1, nleaf - 1))
        xx = x + lean * (yy - y) / h
        botany.leaf(ax, (xx, yy), leaf_len, angle=30 if k % 2 == 0 else 150, shape="ovate", zorder=7)
    tip = (x + lean, y + h)
    if flowers:
        for dx, dy in ((0, 0.3), (-0.35, 0.05), (0.35, 0.05)):
            botany.flower(ax, (tip[0] + dx, tip[1] + dy), 0.28, zorder=9)
    else:
        botany.bud(ax, tip, 0.35, zorder=9)
    return tip


def ground(x0, x1, y):
    ax.plot([x0, x1], [y, y], color=P.muted(), lw=1.0, zorder=3)


# A: chain of approach-grafted Xanthium plants
bio.panel(ax, "A", (0.2, 10.3))
y0 = 1.6
xs = [1.5, 3.3, 5.1, 6.9, 8.7]
ground(0.6, 9.6, y0)
for i, x in enumerate(xs):
    plant(x, y0, 5.2, flowers=True)
    if i < len(xs) - 1:
        ax.plot([x + 0.05, xs[i + 1] - 0.05], [y0 + 2.2, y0 + 2.2], color=P.edge("plant"), lw=1.4, zorder=5)
        ax.add_patch(FancyBboxPatch((x + 0.75, y0 + 2.05), 0.3, 0.3, boxstyle="round,pad=0.02",
                                    facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.6, zorder=6))
ax.add_patch(FancyBboxPatch((0.1, y0 + 2.5), 1.6, 1.3, boxstyle="round,pad=0.05", facecolor=P.ink(), alpha=0.35,
                            edgecolor=P.ink(), lw=0.8, zorder=8))
bio.label(ax, (0.9, y0 + 4.3), "short days", size="small")
bio.label(ax, (5.1, 0.8), "rest of the plants in long days: all flower", size="small")
bio.label(ax, (5.1, 0.2), "graft unions (squares)", size="tiny", color=P.muted())

# B: Perilla leaf grafts
bio.panel(ax, "B", (10.6, 10.3))
ground(11.0, 19.6, y0)
for x, induced in ((12.8, True), (17.4, False)):
    tip = plant(x, y0, 5.2, flowers=induced, nleaf=2)
    botany.leaf(ax, (x, y0 + 3.0), 1.5, angle=20, shape="ovate", token="highlight" if induced else "leaf", zorder=8)
    ax.add_patch(FancyBboxPatch((x + 0.0, y0 + 2.85), 0.25, 0.3, boxstyle="round,pad=0.02",
                                facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.6, zorder=9))
    bio.label(ax, (x + 0.2, y0 - 0.5), "leaf from SD plant" if induced else "leaf from LD plant", size="small")
    bio.label(ax, (x + 0.2, y0 - 1.1), "stock flowers" if induced else "stock vegetative", size="small",
              bold=induced)
bio.label(ax, (15.1, 9.3), "stocks in long days", size="small", color=P.muted())

# C: LDP grafted onto SDP tobacco
bio.panel(ax, "C", (21.0, 10.3))
ground(21.6, 29.6, y0)
x = 25.6
tip = plant(x, y0, 4.0, flowers=False, nleaf=3)
ax.plot([x, x + 1.0], [y0 + 2.2, y0 + 3.0], color=P.edge("plant"), lw=1.6, zorder=6)
for dx, dy in ((1.0, 3.25), (1.35, 3.0), (0.75, 3.05)):
    botany.flower(ax, (x + dx, y0 + dy), 0.26, zorder=9)
bio.label(ax, (x + 1.8, y0 + 1.2), "Maryland Mammoth\ntobacco (SDP) stock", size="small", ha="left")
scion_base = (x, y0 + 4.0)
ax.add_patch(FancyBboxPatch((x - 0.2, y0 + 3.85), 0.4, 0.3, boxstyle="round,pad=0.02",
                            facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.6, zorder=9))
plant(x, y0 + 4.0, 2.8, flowers=True, nleaf=2, leaf_len=0.8)
bio.label(ax, (x - 2.0, y0 + 5.6), "Hyoscyamus\n(LDP) scion", size="small", ha="right")
bio.label(ax, (25.6, 0.8), "long days: both flower", size="small")
