"""Lorenz's psychohydraulic model, redrawn schematically: tap, reservoir, spring-loaded valve, scale pan, trough."""

import numpy as np
from matplotlib.patches import Polygon, Rectangle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(18.0, 16.0)
ink, mut = P.ink(), P.muted()
water = P.fill("dna")
wedge = P.edge("dna")
lw = 1.6

# tap
ax.add_patch(Rectangle((2.0, 14.2), 2.6, 0.5, facecolor=P.mix(P.fill("neutral"), P.surface(), 0.7), edgecolor=ink, lw=lw, zorder=6))
ax.add_patch(Rectangle((4.2, 13.6), 0.4, 0.6, facecolor=P.mix(P.fill("neutral"), P.surface(), 0.7), edgecolor=ink, lw=lw, zorder=6))
ax.plot([4.4, 4.4], [13.6, 11.3], color=wedge, lw=2.2, zorder=4)
bio.label(ax, (1.6, 14.45), "T", size="normal", bold=True, ha="right")
bio.label(ax, (2.0, 15.3), "action-specific energy", size="small", ha="left", color=mut)

# reservoir: a vertical vessel narrowing into an outlet at the bottom right
res = [(3.0, 12.2), (3.0, 5.6), (6.2, 5.6), (6.2, 6.4), (5.2, 6.4), (5.2, 12.2)]
ax.add_patch(Polygon([(3.0, 11.0), (3.0, 5.6), (6.2, 5.6), (6.2, 6.4), (5.2, 6.4), (5.2, 11.0)],
                     closed=True, facecolor=water, edgecolor="none", alpha=0.7, zorder=3))
ax.plot(*zip(*res), color=ink, lw=lw, zorder=5)
ax.plot([3.0, 5.2], [11.0, 11.0], color=wedge, lw=1.0, zorder=4)
bio.label(ax, (2.6, 8.6), "R", size="normal", bold=True, ha="right")

# valve (a cone) at the outlet, on a rod to the spring
ax.add_patch(Polygon([(6.2, 6.0), (7.0, 6.45), (7.0, 5.55)], closed=True, facecolor=P.fill("neutral"),
                     edgecolor=ink, lw=lw, zorder=6))
bio.label(ax, (6.9, 4.9), "V", size="normal", bold=True)
ax.plot([7.0, 9.0], [6.0, 6.0], color=ink, lw=lw, zorder=6)
# spring
xs = np.linspace(9.0, 11.6, 200)
ax.plot(xs, 6.0 + 0.35 * np.sin((xs - 9.0) * 2 * np.pi * 3.5), color=ink, lw=1.2, zorder=6)
ax.plot([11.6, 11.6], [5.2, 6.8], color=ink, lw=2.4, zorder=6)
bio.label(ax, (10.3, 7.0), "S", size="normal", bold=True)
bio.label(ax, (12.0, 7.4), "spring: inhibition", size="small", ha="left", color=mut)
# string over pulley to scale pan
ax.plot([8.0, 8.0], [6.0, 2.9], color=ink, lw=1.0, zorder=5)
ax.add_patch(Polygon([(7.0, 2.9), (9.0, 2.9), (8.7, 2.5), (7.3, 2.5)], closed=True, facecolor=P.mix(P.fill("neutral"), P.surface(), 0.7),
                     edgecolor=ink, lw=lw, zorder=6))
for xw, h in [(7.6, 0.5), (8.25, 0.35)]:
    ax.add_patch(Rectangle((xw - 0.25, 2.9), 0.5, h, facecolor=P.fill("rna"), edgecolor=P.edge("rna"), lw=1, zorder=7))
bio.label(ax, (9.4, 2.7), "Sp", size="normal", bold=True, ha="left")
bio.label(ax, (9.4, 1.9), "scale pan: weights = sign stimulus", size="small", ha="left", color=mut)

# outflow jet into trough
xj = np.linspace(7.0, 10.4, 50)
ax.plot(xj, 6.0 - 0.112 * (xj - 7.0) ** 2, color=wedge, lw=2.2, zorder=4)
tr = [(9.0, 3.6 + 0.0), (9.0, 2.9 + 1.6)]
# trough: a sloping channel with holes 1..6
x0, y0 = 10.0, 4.4
ax.plot([x0, x0 + 6.6], [y0, y0 - 1.2], color=ink, lw=lw, zorder=5)
ax.plot([x0, x0], [y0, y0 + 0.9], color=ink, lw=lw, zorder=5)
for i in range(6):
    xh = x0 + 0.6 + 1.0 * i
    yh = y0 - 1.2 * (xh - x0) / 6.6
    ax.plot([xh], [yh - 0.15], "o", ms=5, mfc=P.surface(), mec=ink, zorder=7)
    bio.label(ax, (xh, yh + 0.35), str(i + 1), size="small")
    if i < 3:
        ax.plot([xh, xh], [yh - 0.3, yh - 1.0 - 0.0], color=wedge, lw=1.6, zorder=4)
bio.label(ax, (14.6, 4.6), "Tr", size="normal", bold=True)
bio.label(ax, (12.6, 1.0), "trough: response intensity 1 (weak) to 6 (full)", size="small", color=mut)
