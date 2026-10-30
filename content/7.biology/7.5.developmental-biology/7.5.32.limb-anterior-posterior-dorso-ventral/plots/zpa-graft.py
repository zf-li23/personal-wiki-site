"""Polarizing activity (schematic). Wing buds in dorsal view (anterior up, ZPA posterior) and the digit patterns
that result. A: normal chick wing, digits 2-3-4. B: a ZPA grafted under the anterior margin: mirror-image
duplication 4-3-2-2-3-4. C: a bead releasing Sonic hedgehog protein or Shh-expressing cells in the same place:
the same duplication; with fewer Shh-producing cells only an extra digit 2 forms (2-2-3-4). D: a point mutation in
the ZRS (mouse Hx, human preaxial polydactyly) makes the enhancer active in the anterior mesenchyme as well: extra
anterior digits. Digits are numbered by identity.
"""

import numpy as np
import wikibio as bio
from wikibio import limbdev as LD
from matplotlib.patches import Circle, Ellipse

P = bio.P
fig, ax = bio.canvas(30.0, 12.0)
cols = [("A", "Normal", None, (2, 3, 4)), ("B", "ZPA graft (anterior)", "zpa", (4, 3, 2, 2, 3, 4)),
        ("C", "Shh bead (anterior)", "bead", (4, 3, 2, 2, 3, 4)), ("D", "ZRS mutation (Hx)", "zrs", (2, 2, 1, 2, 3, 4, 5))]
for k, (lt, title, op, digits) in enumerate(cols):
    x0 = 0.8 + 7.4 * k
    bio.panel(ax, lt, (x0 - 0.5, 11.8))
    bio.label(ax, (x0 + 2.8, 11.4), title, size="small", bold=True)
    b = LD.limb_bud(ax, (x0 + 0.6, 8.6), 3.2, 2.8, flank=True)
    if op == "zpa":
        ax.add_patch(Ellipse(b["at"](0.62, 0.74), 1.0, 0.55, angle=20, facecolor=P.fill("protein"),
                             edgecolor=P.edge("protein"), lw=0.8, zorder=12))
        bio.callout(ax, b["at"](0.62, 0.74), (x0 + 5.2, 10.6), "grafted ZPA", size="tiny")
    if op == "bead":
        ax.add_patch(Circle(b["at"](0.6, 0.6), 0.22, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.9, zorder=12))
        bio.callout(ax, b["at"](0.6, 0.6), (x0 + 5.2, 10.6), "Shh bead", size="tiny")
    if op == "zrs":
        ax.add_patch(Ellipse(b["at"](0.62, 0.7), 0.8, 0.45, angle=20, facecolor=P.light("protein"),
                             edgecolor=P.edge("protein"), lw=0.8, ls=(0, (2, 1.5)), zorder=12))
        bio.callout(ax, b["at"](0.62, 0.7), (x0 + 5.2, 10.6), "ectopic Shh", size="tiny")
    bio.callout(ax, b["zpa"], (x0 + 5.2, 6.6), "ZPA", size="tiny")
    bio.arrow(ax, (x0 + 2.6, 6.3), (x0 + 2.6, 5.4), kind="process", color=P.muted(), lw=1.0)
    LD.limb_skeleton(ax, (x0 + 0.1, 3.0), 5.3, digits=digits, digit_labels=True, colored="segment", width=0.4)
bio.label(ax, (0.6, 0.6), "anterior up, posterior down in all panels", size="tiny", color=P.muted(), ha="left")
