"""Three ways animals digest food (schematic, not to scale; germ-layer colours as in 7.17.3).

A: intracellular digestion. A choanocyte of a sponge (or a placozoan cell) engulfs a particle by
phagocytosis; digestion takes place in a food vacuole inside the cell. B: a gastrovascular cavity with a
single opening, the mouth, which also serves as anus (cnidarian polyp, here with tentacles). Food is
digested extracellularly in the cavity and the fragments are taken up and finished intracellularly by the
gastrodermis. C: a complete digestive tract with mouth and anus. Food passes in one direction through
regions specialized in sequence (pharynx, esophagus, crop or stomach, intestine, rectum), so feeding and
defecation do not interfere and each region can work continuously.
"""

import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse, Polygon

P = bio.P
fig, ax = bio.canvas(26.0, 8.6)
ECTO, ENDO = "ectoderm", "endoderm"

# A: intracellular digestion
bio.panel(ax, "A", (0.4, 8.1))
bio.label(ax, (3.9, 8.1), "Intracellular digestion", size="small", bold=True)
ax.add_patch(Ellipse((3.9, 3.6), 3.4, 3.0, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cytoplasm"), lw=1.2, zorder=5))
for k in range(9):  # collar of microvilli
    x = 3.1 + k * 0.2
    ax.plot([x, x - 0.1 + 0.025 * k], [4.9, 6.6], color=P.edge("cytoplasm"), lw=1.0, zorder=6)
ax.plot([3.9, 3.7, 4.1, 3.9], [4.9, 6.0, 6.8, 7.6], color=P.ink(), lw=1.2, zorder=7)
ax.add_patch(Ellipse((3.6, 3.1), 1.0, 0.9, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=1.0, zorder=7))
for (x, y, r) in ((4.6, 4.0, 0.42), (4.7, 2.8, 0.32)):
    ax.add_patch(Ellipse((x, y), 2 * r, 2 * r, facecolor=P.fill("lysosome"), edgecolor=P.edge("lysosome"), lw=1.0, zorder=7))
    ax.add_patch(Ellipse((x, y), r, r * 0.8, facecolor=P.fill("bacterium"), edgecolor=P.edge("bacterium"), lw=0.6, zorder=8))
ax.add_patch(Ellipse((6.4, 5.2), 0.5, 0.35, facecolor=P.fill("bacterium"), edgecolor=P.edge("bacterium"), lw=0.8, zorder=8))
bio.arrow(ax, (6.2, 5.0), (5.4, 4.4), kind="process", color=P.muted())
bio.callout(ax, (4.6, 4.0), (6.6, 2.4), "Food vacuole", size="tiny")
bio.callout(ax, (3.6, 3.1), (1.2, 1.6), "Nucleus", size="tiny")
bio.callout(ax, (3.4, 5.7), (1.4, 6.6), "Collar", size="tiny")
bio.label(ax, (3.9, 0.7), "Sponge choanocyte", size="tiny", color=P.muted())

# B: gastrovascular cavity (polyp in longitudinal section)
bio.panel(ax, "B", (8.6, 8.1))
bio.label(ax, (12.6, 8.1), "Gastrovascular cavity", size="small", bold=True)
outer = [(11.2, 1.2), (14.0, 1.2), (14.2, 5.6), (13.5, 6.2), (11.7, 6.2), (11.0, 5.6)]
inner = [(11.7, 1.8), (13.5, 1.8), (13.6, 5.4), (12.9, 5.7), (12.9, 6.2), (12.3, 6.2), (12.3, 5.7), (11.6, 5.4)]
ax.add_patch(Polygon(outer, closed=True, facecolor=P.fill(ECTO), edgecolor=P.edge(ECTO), lw=1.2, zorder=5))
gd = [(11.5, 1.6), (13.7, 1.6), (13.85, 5.5), (12.9, 5.95), (12.9, 6.2), (12.3, 6.2), (12.3, 5.95), (11.35, 5.5)]
ax.add_patch(Polygon(gd, closed=True, facecolor=P.fill(ENDO), edgecolor=P.edge(ENDO), lw=1.0, zorder=6))
ax.add_patch(Polygon(inner, closed=True, facecolor=P.surface(), edgecolor=P.edge(ENDO), lw=1.0, zorder=7))
for sx in (-1, 1):
    for k in range(2):
        x0 = 12.6 + sx * (0.9 + 0.5 * k)
        ax.plot([x0, x0 + sx * (0.9 + 0.4 * k)], [6.1, 7.6 - 0.3 * k], color=P.edge(ECTO), lw=5, solid_capstyle="round", zorder=4)
bio.arrow(ax, (12.6, 7.4), (12.6, 6.0), kind="process", color=P.muted())
bio.arrow(ax, (12.9, 5.3), (13.2, 6.6), kind="process", color=P.negative() if hasattr(P, "negative") else P.muted(), dashed=True)
bio.callout(ax, (12.6, 6.1), (15.2, 7.0), "Mouth = anus", size="tiny")
bio.callout(ax, (12.6, 3.5), (15.2, 3.6), "Gastrovascular\ncavity", size="tiny")
bio.callout(ax, (11.15, 3.0), (9.4, 2.2), "Epidermis", size="tiny")
bio.callout(ax, (11.6, 4.5), (9.4, 5.0), "Gastrodermis", size="tiny")
bio.label(ax, (12.6, 0.7), "Cnidarian polyp", size="tiny", color=P.muted())

# C: complete digestive tract
bio.panel(ax, "C", (16.8, 8.1))
bio.label(ax, (21.4, 8.1), "Complete digestive tract", size="small", bold=True)
body = [(17.4, 3.2), (17.9, 4.8), (19.5, 5.4), (24.6, 5.2), (25.6, 4.3), (24.6, 3.3), (19.5, 3.0)]
ax.add_patch(Polygon(body, closed=True, facecolor=P.fill(ECTO), edgecolor=P.edge(ECTO), lw=1.2, zorder=5))
SEG = [((17.6, 4.1), (18.6, 4.15), 0.16, "Mouth"), ((18.6, 4.15), (19.5, 4.2), 0.3, "Pharynx"),
       ((19.5, 4.2), (20.4, 4.2), 0.14, "Esophagus"), ((20.4, 4.2), (21.6, 4.2), 0.42, "Crop / stomach"),
       ((21.6, 4.2), (24.2, 4.2), 0.24, "Intestine"), ((24.2, 4.2), (25.3, 4.25), 0.18, "Rectum, anus")]
for k, (a, b, w, name) in enumerate(SEG):
    ax.add_patch(Polygon([(a[0], a[1] - w), (b[0], b[1] - w), (b[0], b[1] + w), (a[0], a[1] + w)], closed=True,
                         facecolor=P.fill(ENDO), edgecolor=P.edge(ENDO), lw=0.9, zorder=6))
    xm, ym = (a[0] + b[0]) / 2, a[1]
    up = k % 2 == 0
    bio.callout(ax, (xm, ym + (w if up else -w)), (xm, 6.4 if up else 1.9), name, size="tiny")
bio.arrow(ax, (19.6, 7.2), (22.2, 7.2), kind="process", color=P.muted())
bio.label(ax, (22.4, 7.2), "one-way flow", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (21.4, 0.7), "Most bilaterians", size="tiny", color=P.muted())
