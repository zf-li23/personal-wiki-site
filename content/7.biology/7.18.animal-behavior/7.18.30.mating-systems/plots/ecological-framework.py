"""The ecological framework of mating systems (after Emlen and Oring 1977; Davies, Krebs and West 2012).

A: when males give no care, resources determine how females are distributed (modified by predation and the
costs and benefits of grouping), and the distribution of females in space and time determines whether and how
males can monopolize them, directly (female defense) or indirectly (resource defense). The operational sex
ratio, set by the timing of female receptivity, determines how many females a male can monopolize.
B, C: the environmental potential for polygyny. Dots are females (or the resources they need) placed at random
(B) or in clumps (C); circles are the equal-sized areas that males can defend. When females are clumped, a few
males can defend many and the rest none.
"""

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

import wikibio as bio
from wikibio import quant

P = bio.P
rng = np.random.default_rng(4)
fig, ax = bio.canvas(32.0, 11.0)

bio.panel(ax, "A", (0.2, 10.8))
boxes = {
    "res": ((2.8, 6.0), "resources\n(food, nest sites)", "plant"),
    "fem": ((8.2, 6.0), "female\ndistribution", "rna"),
    "male": ((13.6, 6.0), "male\ndistribution", "dna"),
    "pred": ((8.2, 9.2), "predation, costs and\nbenefits of grouping", "neutral"),
    "time": ((8.2, 2.6), "timing of female\nreceptivity (OSR)", "neutral"),
}
for (c, t, tok) in boxes.values():
    bio.box(ax, c, 4.2, 1.9, tok, t, size="small")
bio.arrow(ax, (4.95, 6.0), (6.05, 6.0), kind="process")
bio.arrow(ax, (10.35, 6.0), (11.45, 6.0), kind="process")
bio.arrow(ax, (8.2, 8.2), (8.2, 7.05), kind="modulation")
bio.arrow(ax, (10.3, 2.9), (12.4, 4.95), kind="modulation")
bio.arrow(ax, (2.8, 5.05), (14.6, 5.05), kind="process", bend=-0.12, dashed=True)
bio.label(ax, (8.6, 1.0), "solid: female defense (direct);  dashed: resource defense (indirect)", size="tiny",
          color=P.muted())

for k, (x0, title, clumped) in enumerate(((17.6, "females dispersed", False), (25.0, "females clumped", True))):
    bio.panel(ax, "BC"[k], (x0 - 0.6, 10.8))
    bio.label(ax, (x0 + 3.2, 10.2), title, size="small", bold=True)
    w = 6.4
    if clumped:
        centers = np.array([[1.1, 1.1], [5.3, 3.2], [1.1, 5.3]])
        pts = np.vstack([c + rng.normal(0, 0.3, (6, 2)) for c in centers])
    else:
        pts = rng.uniform(0.3, 6.1, (18, 2))
    pts = np.clip(pts, 0.2, 6.2)
    ax.add_patch(FancyBboxPatch((x0, 1.6), w, w, boxstyle="round,pad=0,rounding_size=0.2",
                                         facecolor=P.mix(P.fill("plant"), P.surface(), 0.7), edgecolor=P.muted(), lw=0.8, zorder=2))
    terr = [(a, b) for a in (1.1, 3.2, 5.3) for b in (1.1, 3.2, 5.3)]
    for tx, ty in terr:
        n = int(np.sum(np.hypot(pts[:, 0] - tx, pts[:, 1] - ty) < 0.95))
        ax.add_patch(Circle((x0 + tx, 1.6 + ty), 0.95, fill=False, edgecolor=quant.line_color("dna"), lw=1.2,
                            zorder=4))
        bio.label(ax, (x0 + tx + 0.78, 1.6 + ty + 0.78), str(n), size="small", bold=True, color=quant.line_color("dna"))
    for px, py in pts:
        ax.add_patch(Circle((x0 + px, 1.6 + py), 0.15, facecolor=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.6,
                            zorder=5))
    bio.label(ax, (x0 + 3.2, 0.9), "numbers: females per defended area", size="tiny", color=P.muted())
