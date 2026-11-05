# Spiral phyllotaxis and the golden angle. (A) Vogel's model (primordium k at angle k * 137.5 degrees and
# radius proportional to sqrt(k), youngest in the centre) with the 8 and 13 contact parastichies
# (wikibio.botany). (B) Divergence angles of the Schimper-Braun fractions F(n)/F(n+2) converging on the
# golden angle from alternate sides. (C) The same model with a divergence of 135 degrees: primordia line
# up in straight radial rows (orthostichies) and leave gaps.
import math

import numpy as np

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(33.0, 12.0)
bio.panel(ax, "A", (0.2, 11.8))
bio.label(ax, (0.85, 11.77), "Golden angle (137.5°)", size="title", ha="left", va="top")
B.phyllotaxis(ax, (5.6, 5.6), 4.6, n=90, numbers=8, parastichies=(8, 13))
bio.label(ax, (5.6, 0.4), "8 and 13 parastichies", size="small", color=P.muted())

# B: convergence chart in canvas coordinates
bio.panel(ax, "B", (11.6, 11.8))
bio.label(ax, (12.25, 11.77), "Schimper-Braun series", size="title", ha="left", va="top")
x0, y0, w, h = 13.6, 2.2, 7.6, 8.0
amin, amax = 100.0, 185.0
Y = lambda a: y0 + (a - amin) / (amax - amin) * h
ax.plot([x0, x0], [y0, y0 + h], color=P.ink(), lw=0.8)
ax.plot([x0, x0 + w], [y0, y0], color=P.ink(), lw=0.8)
for a in (120, 140, 160, 180):
    ax.plot([x0 - 0.12, x0], [Y(a), Y(a)], color=P.ink(), lw=0.8)
    bio.label(ax, (x0 - 0.2, Y(a)), f"{a}°", size="tiny", ha="right")
ga = 360 / ((1 + math.sqrt(5)) / 2) ** 2
ax.plot([x0, x0 + w], [Y(ga), Y(ga)], color=P.edge("negative"), lw=1.0, ls=(0, (4, 3)))
bio.label(ax, (x0 + 1.4, Y(ga) - 0.4), "137.508°", size="tiny", ha="left", color=P.edge("negative"))
F = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
pts = []
for i in range(1, 8):
    frac = F[i - 1] / F[i + 1]
    a = 360 * frac
    x = x0 + 0.6 + (i - 1) * (w - 1.0) / 6
    pts.append((x, Y(a)))
    ax.add_patch(__import__("matplotlib.patches", fromlist=["Circle"]).Circle((x, Y(a)), 0.14, color=P.edge("dna"), zorder=5))
    bio.label(ax, (x, Y(a) + (0.5 if a > ga else -0.5)), f"{F[i - 1]}/{F[i + 1]}", size="tiny")
pts = np.array(pts)
ax.plot(pts[:, 0], pts[:, 1], color=P.edge("dna"), lw=0.8, zorder=4)
bio.label(ax, (x0 + w / 2, y0 - 0.6), "phyllotactic fraction", size="small")
bio.label(ax, (x0 - 1.3, y0 + h / 2), "divergence", size="small", rotation=90)

bio.panel(ax, "C", (22.2, 11.8))
bio.label(ax, (22.85, 11.77), "Divergence 135°", size="title", ha="left", va="top")
B.phyllotaxis(ax, (27.6, 5.6), 4.6, n=90, divergence=135.0, parastichies=(8,), numbers=0, angle_arc=False)
bio.label(ax, (27.6, 0.4), "orthostichies, uneven packing", size="small", color=P.muted())
