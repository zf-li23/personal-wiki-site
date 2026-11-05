"""A dichotomous key to seven genera of Oleaceae drawn as a decision tree. Each numbered node is one
couplet of the key; its two branches carry the two contrasting leads, and each tip is the genus reached.
The same tree underlies the indented and the bracketed form of the key written out in the text: the
indented key lists the leads along the tree depth-first, the bracketed key lists the couplets in the
order of their numbers. The key is diagnostic, not phylogenetic: Fontanesia and Fraxinus are grouped by
their winged fruits, not by descent.
"""

import wikibio as bio
from matplotlib.patches import Circle

P = bio.P
fig, ax = bio.canvas(24.4, 12.4)

nodes = {1: (1.3, 6.2), 2: (6.0, 10.4), 3: (6.0, 4.0), 4: (11.0, 6.6), 5: (11.0, 2.0), 6: (16.0, 3.4)}
tips = {
    "Fontanesia": (11.0, 11.5), "Fraxinus": (11.0, 9.3),
    "Forsythia": (16.5, 7.6), "Syringa": (16.5, 5.6),
    "Osmanthus": (21.3, 4.4), "Ligustrum": (21.3, 2.4), "Jasminum": (16.0, 0.8),
}
edges = [
    (1, 2, "fruit a samara"), (1, 3, "fruit not a samara"),
    (2, "Fontanesia", "simple entire leaves; wing all round"), (2, "Fraxinus", "pinnate leaves; wing at apex"),
    (3, 4, "capsule"), (3, 5, "drupe or berry"),
    (4, "Forsythia", "flowers yellow; pith hollow/chambered"),
    (4, "Syringa", "purple, white, red; pith solid"),
    (5, 6, "simple opposite leaves"),
    (5, "Jasminum", "pinnate or trifoliolate leaves; berry"),
    (6, "Osmanthus", "corolla lobes imbricate; drupe"),
    (6, "Ligustrum", "corolla lobes valvate; berry-like drupe"),
]


def pos(k):
    return nodes[k] if k in nodes else tips[k]


for a, b, lead in edges:
    (x0, y0), (x1, y1) = pos(a), pos(b)
    xm = x0 + 0.9
    ax.plot([x0 + 0.35, xm, xm, x1 - 0.2], [y0, y0, y1, y1], color=P.muted(), lw=1.1, zorder=3)
    bio.label(ax, (xm + 0.2, y1 + 0.32), lead, size="tiny", ha="left", va="bottom")
for k, xy in nodes.items():
    ax.add_patch(Circle(
        xy, 0.36, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.1, zorder=5))
    bio.label(ax, xy, str(k), size="small", bold=True, color=P.on_fill())
for name, (x, y) in tips.items():
    bio.box(ax, (x + 1.25, y), 2.5, 0.72, token="positive")
    bio.label(ax, (x + 1.25, y), name, size="small", italic=True, color=P.on_fill())
bio.label(ax, (0.6, 12.0), "Key to seven genera of Oleaceae", size="normal", bold=True, ha="left")
bio.label(ax, (0.6, 11.35), "numbered circles: couplets", size="tiny", ha="left", color=P.muted())
