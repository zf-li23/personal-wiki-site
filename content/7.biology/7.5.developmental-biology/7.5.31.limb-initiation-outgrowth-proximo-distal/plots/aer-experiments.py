"""Classical experiments on the chick wing bud (schematic outcomes; skeletons coloured by segment).

A: removal of the AER at three stages and the unoperated control. B: Summerbell and Lewis's exchanges of the
progress zone (with its AER) between young and old buds.
"""

import numpy as np
import wikibio as bio
from wikibio import limbdev as LD

P = bio.P
fig, ax = bio.canvas(25.0, 14.0)


def bud(xy, L=1.8, W=1.5, aer=True, **kw):
    return LD.limb_bud(ax, xy, L, W, aer=aer, zpa=False, **kw)


def cross(p, r=0.22):
    for s in (1, -1):
        ax.plot([p[0] - r, p[0] + r], [p[1] - s * r, p[1] + s * r], color=P.edge("negative"), lw=2.0, zorder=20,
                solid_capstyle="round")


# A ------------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 13.8))
bio.label(ax, (1.0, 13.5), "AER removed at stage", size="small", bold=True, ha="left", va="top")
rows = [("HH18", "stylopod"), ("HH20", "zeugopod"), ("HH24", "carpals"), ("control", "autopod")]
for i, (st, upto) in enumerate(rows):
    y = 11.4 - 3.0 * i
    b = bud((1.0, y), aer=(st == "control"))
    if st != "control":
        cross(b["tip"])
    bio.label(ax, (2.6, y + 1.05), st, size="tiny", color=P.muted(), ha="left")
    bio.arrow(ax, (3.3, y), (4.3, y), kind="process", color=P.muted(), lw=1.0)
    LD.limb_skeleton(ax, (4.7, y), 5.4, upto=upto)

# B ------------------------------------------------------------------------------------------------
bio.panel(ax, "B", (11.4, 13.8))
bio.label(ax, (12.2, 13.5), "Progress zone exchanges", size="small", bold=True, ha="left", va="top")
# young PZ onto old bud
y = 10.6
bio.label(ax, (12.2, y + 1.4), "Young PZ + AER on an old bud", size="tiny", ha="left")
LD.limb_skeleton(ax, (12.4, y), 4.6, upto="zeugopod", colored="neutral")
LD.limb_skeleton(ax, (12.4 + 0.66 * 4.6 + 0.2, y), 5.2, start="zeugopod")
bio.label(ax, (21.0, y), "extra zeugopod", size="tiny", color=P.muted(), ha="left")
y = 6.6
bio.label(ax, (12.2, y + 1.4), "Old PZ + AER on a young bud", size="tiny", ha="left")
LD.limb_skeleton(ax, (12.4, y), 4.6, upto="stylopod", colored="neutral")
s = LD.limb_skeleton(ax, (12.4 + 0.34 * 4.6 + 0.05, y), 5.0, start="zeugopod", proportions=(0.0, 0.0, 0.5))
bio.label(ax, (21.0, y), "zeugopod missing", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (12.2, 4.2), "grey: host stump; coloured: from the grafted tip", size="tiny", color=P.muted(), ha="left")

