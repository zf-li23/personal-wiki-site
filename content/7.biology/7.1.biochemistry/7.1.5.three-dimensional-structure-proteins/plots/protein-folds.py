"""Topology diagrams of common motifs (sheet seen face-on; strands are arrows from N to C, helices
cylinders). A: beta-alpha-beta unit, two parallel strands joined by a crossover helix.
B: beta hairpin, two antiparallel strands joined by a beta turn. C: Greek key, four antiparallel
strands in the sheet order 4-1-2-3. D: up-and-down four-helix bundle (all-alpha)."""

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(20.0, 8.2)
yb, yt = 2.0, 6.0
L = bio.core.LINE * 1.3


def title(x, text, sub):
    bio.label(ax, (x, 7.55), text, size="normal", bold=True)
    bio.label(ax, (x, 1.0), sub, size="tiny", color=P.muted())


# A: beta-alpha-beta
bio.panel(ax, "A", (0.1, 8.1))
x1, x2, xh = 1.2, 3.6, 2.4
M.strand(ax, (x1, yb), (x1, yt), text="β1")
M.strand(ax, (x2, yb), (x2, yt), text="β2")
M.helix(ax, (xh, yt - 0.3), (xh, yb + 0.3), width=0.62, text="α", zorder=14)
M.loop(ax, [(x1, yt - 0.02), (x1 + 0.3, yt + 0.55), (xh - 0.2, yt + 0.5), (xh, yt - 0.25)])
M.loop(ax, [(xh, yb + 0.25), (xh + 0.25, yb - 0.5), (x2 - 0.3, yb - 0.55), (x2, yb + 0.02)])
M.loop(ax, [(x1, yb - 0.6), (x1, yb + 0.02)])
M.terminus(ax, (x1, yb - 0.85), "N")
M.loop(ax, [(x2, yt - 0.02), (x2 + 0.2, yt + 0.45), (x2 + 0.5, yt + 0.5)])
M.terminus(ax, (x2 + 0.75, yt + 0.5), "C")
title(2.4, "β-α-β unit", "crossover helix packs on the sheet")

# B: beta hairpin
bio.panel(ax, "B", (5.2, 8.1))
x1, x2 = 6.3, 7.5
M.strand(ax, (x1, yb), (x1, yt), text="β1")
M.strand(ax, (x2, yt), (x2, yb), text="β2")
M.loop(ax, [(x1, yt - 0.02), (x1 + 0.1, yt + 0.45), (x2 - 0.1, yt + 0.45), (x2, yt - 0.02)],
       color=P.edge("highlight"), lw=L * 1.5)
bio.label(ax, ((x1 + x2) / 2, yt + 0.8), "β turn", size="tiny", color=P.edge("highlight"), bold=True)
for y in (2.8, 3.8, 4.8):
    ax.plot([x1 + 0.25, x2 - 0.25], [y, y], color=P.muted(), lw=0.8, ls=(0, (1.5, 1.5)))
M.loop(ax, [(x1, yb - 0.6), (x1, yb + 0.02)])
M.terminus(ax, (x1, yb - 0.85), "N")
M.loop(ax, [(x2, yb + 0.02), (x2, yb - 0.6)])
M.terminus(ax, (x2, yb - 0.85), "C")
title(6.9, "β hairpin", "dotted: interstrand H bonds")

# C: Greek key, sheet order 4-1-2-3
bio.panel(ax, "C", (9.0, 8.1))
xs = {4: 9.9, 1: 11.1, 2: 12.3, 3: 13.5}
M.strand(ax, (xs[1], yb), (xs[1], yt), text="1")
M.strand(ax, (xs[2], yt), (xs[2], yb), text="2")
M.strand(ax, (xs[3], yb), (xs[3], yt), text="3")
M.strand(ax, (xs[4], yt), (xs[4], yb), text="4")
M.loop(ax, [(xs[1], yb - 0.6), (xs[1], yb + 0.02)])
M.terminus(ax, (xs[1], yb - 0.85), "N")
M.loop(ax, [(xs[1], yt - 0.02), (xs[1] + 0.1, yt + 0.4), (xs[2] - 0.1, yt + 0.4), (xs[2], yt - 0.02)])
M.loop(ax, [(xs[2], yb + 0.02), (xs[2] + 0.1, yb - 0.4), (xs[3] - 0.1, yb - 0.4), (xs[3], yb + 0.02)])
M.loop(ax, [(xs[3], yt - 0.02), (xs[3] + 0.1, yt + 0.6), (12.0, yt + 0.95), (10.3, yt + 0.95), (xs[4], yt + 0.4), (xs[4], yt - 0.02)],
       color=P.edge("highlight"), lw=L * 1.5)
M.loop(ax, [(xs[4], yb + 0.02), (xs[4], yb - 0.6)])
M.terminus(ax, (xs[4], yb - 0.85), "C")
title(11.7, "Greek key", "strand 4 returns to pair with strand 1")

# D: four-helix bundle
bio.panel(ax, "D", (14.6, 8.1))
hx = [15.6, 16.8, 18.0, 19.2]
for k, x in enumerate(hx):
    a, b = ((x, yb + 0.3), (x, yt - 0.3)) if k % 2 == 0 else ((x, yt - 0.3), (x, yb + 0.3))
    M.helix(ax, a, b, width=0.66, text=f"α{k + 1}")
for k in range(3):
    y0 = yt - 0.3 if k % 2 == 0 else yb + 0.3
    s = 1 if k % 2 == 0 else -1
    M.loop(ax, [(hx[k], y0 + s * 0.02), (hx[k] + 0.15, y0 + s * 0.6), (hx[k + 1] - 0.15, y0 + s * 0.6), (hx[k + 1], y0 + s * 0.02)])
M.loop(ax, [(hx[0], yb - 0.4), (hx[0], yb + 0.28)])
M.terminus(ax, (hx[0], yb - 0.65), "N")
M.loop(ax, [(hx[3], yb + 0.28), (hx[3], yb - 0.4)])
M.terminus(ax, (hx[3], yb - 0.65), "C")
title(17.4, "Four-helix bundle", "up-and-down; all-α class")
