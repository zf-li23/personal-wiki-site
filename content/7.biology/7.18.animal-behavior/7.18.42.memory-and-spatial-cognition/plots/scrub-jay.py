# Episodic-like memory in western scrub jays: the design and the shape of the result of Clayton and Dickinson
# (1998). A: in each trial a jay cached peanuts in one side of a sand-filled ice-cube tray and, on another
# occasion, wax-moth larvae (wax worms, its preferred food) in the other side of the same tray; the order
# of the two caching episodes was counterbalanced. Trays were edged with distinctive objects so that each
# could be recognized. After a retention interval of 4 h or 124 h the jay could search the tray (all food
# had been removed, so no cues from the food remained). "Degrade" jays had learned in training that worms
# were spoiled after 124 h but fresh after 4 h; "replenish" jays had always found fresh worms. B: proportion
# of first searches directed at the worm side (illustrative values of the reported pattern): degrade jays
# searched for worms after 4 h but for peanuts after 124 h; replenish jays searched for worms after both
# delays. The jays therefore remembered what they had cached, where, and how long ago.
import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(23.0, 9.6)
bio.panel(ax, "A", (0.2, 9.4))


def tray(x0, y0, left, right):
    for r in range(3):
        for c in range(6):
            tok = left if c < 3 else right
            ax.add_patch(Rectangle((x0 + c * 0.5, y0 + r * 0.5), 0.46, 0.46,
                                   facecolor=P.mix(P.fill(tok), P.surface(), 0.35) if tok else P.mix(P.fill("neutral"), P.surface(), 0.5),
                                   edgecolor=P.edge("neutral"), lw=0.6, zorder=5))
    ax.add_patch(Rectangle((x0 - 0.12, y0 - 0.12), 3.2, 1.74, facecolor="none", edgecolor=P.ink(), lw=1.0, zorder=6))


tray(0.9, 6.0, "atp", None)
bio.label(ax, (2.4, 8.2), "cache peanuts (one side)", size="tiny")
tray(5.0, 6.0, None, "rna")
bio.label(ax, (6.5, 8.2), "cache worms (other side)", size="tiny")
bio.arrow(ax, (4.25, 6.8), (4.75, 6.8), kind="process")
bio.arrow(ax, (6.5, 5.6), (6.5, 4.6), kind="process")
bio.label(ax, (6.7, 5.1), "4 h or 124 h", size="tiny", ha="left", color=P.muted())
tray(5.0, 2.6, None, None)
bio.label(ax, (6.5, 2.05), "search (food removed)", size="tiny")
bio.label(ax, (2.4, 4.7), "degrade group: worms", size="tiny", color=P.muted())
bio.label(ax, (2.4, 4.25), "spoil within 124 h", size="tiny", color=P.muted())
bio.label(ax, (2.4, 3.6), "replenish group:", size="tiny", color=P.muted())
bio.label(ax, (2.4, 3.15), "worms always fresh", size="tiny", color=P.muted())

pb = quant.Plot(ax, (12.6, 1.8, 9.4, 6.4), (0, 6.2), (0, 1.0), ylabel="First searches at worm sites",
                xticks=[(1.7, "degrade"), (4.5, "replenish")], yticks=[0, 0.5, 1])
bio.panel(ax, "B", (10.8, 9.4))
pb.hline(0.5, text="no preference", side="left")
vals = {("degrade", 4): 0.85, ("degrade", 124): 0.15, ("replenish", 4): 0.85, ("replenish", 124): 0.8}
for i, g in enumerate(("degrade", "replenish")):
    x0 = 0.9 + 2.8 * i
    pb.bars([x0, x0 + 0.8], [vals[(g, 4)]], "dna")
    pb.bars([x0 + 0.8, x0 + 1.6], [vals[(g, 124)]], "rna")
pb.legend([("4 h after caching", "dna", "-"), ("124 h after caching", "rna", "-")], at=(18.6, 8.3))
