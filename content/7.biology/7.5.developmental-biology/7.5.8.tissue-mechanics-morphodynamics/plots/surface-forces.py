"""Forces exerted by a surface tension that varies along a curved interface.

A: a patch of the surface of an aggregate, shaded by the local tension gamma (darker = higher).
The surface force per unit area has a normal part -gamma (1/R1 + 1/R2) n (the Laplace pressure,
directed towards the centre of curvature) and a tangential part, the surface gradient of gamma,
pointing towards higher tension (the Marangoni force).
B: consequence for a drop whose tension is highest at one pole: the surface is pulled towards that
pole, and the interior circulates (schematic streamlines of the Stokes flow).
"""

import numpy as np
from matplotlib.patches import Circle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 10.0)
bio.panel(ax, "A", (0.1, 9.9))
cx, cy, R = 6.5, -2.0, 9.0
th = np.linspace(np.pi * 0.68, np.pi * 0.32, 60)
x, y = cx + R * np.cos(th), cy + R * np.sin(th)
ax.fill(np.r_[x, x[-1], x[0]], np.r_[y, 0.5, 0.5], color=P.light("mesoderm"), zorder=1, lw=0)
cm = __import__("matplotlib").colormaps["Reds"]
for i in range(len(th) - 1):
    g = i / (len(th) - 2)
    ax.plot(x[i:i + 2], y[i:i + 2], color=cm(0.3 + 0.6 * g), lw=5, solid_capstyle="butt", zorder=3)
bio.label(ax, (x[0] - 0.3, y[0] + 0.6), "low γ", size="tiny")
bio.label(ax, (x[-1] + 0.3, y[-1] + 0.6), "high γ", size="tiny")
k = 30
px, py = x[k], y[k]
nx, ny = np.cos(th[k]), np.sin(th[k])
bio.arrow(ax, (px, py), (px - 2.4 * nx, py - 2.4 * ny), kind="process")
bio.label(ax, (px - 2.8 * nx + 1.9, py - 2.8 * ny + 0.2), "−γ(1/R1 + 1/R2) n", size="small")
tx, ty = np.sin(th[k]), -np.cos(th[k])
bio.arrow(ax, (px, py), (px + 2.4 * tx, py + 2.4 * ty), kind="process", color=P.edge("ectoderm"))
bio.label(ax, (px + 2.6 * tx, py + 2.6 * ty + 0.6), "∇s γ (Marangoni)", size="small", color=P.edge("ectoderm"))
ax.plot([px, px + 1.4 * nx], [py, py + 1.4 * ny], color=P.muted(), lw=0.8, ls=(0, (2, 1.5)))
bio.label(ax, (px + 1.7 * nx, py + 1.7 * ny), "n", size="small", italic=True)
bio.label(ax, (6.5, 1.0), "tissue", size="small", color=P.muted())
bio.label(ax, (2.0, 8.8), "medium", size="small", color=P.muted())

bio.panel(ax, "B", (13.6, 9.9))
c2, r2 = (19.5, 5.0), 3.6
ax.add_patch(Circle(c2, r2, facecolor=P.light("mesoderm"), edgecolor=P.edge("mesoderm"), lw=1.2, zorder=2))
bio.label(ax, (c2[0], c2[1] + r2 + 0.5), "high γ", size="tiny")
bio.label(ax, (c2[0], c2[1] - r2 - 0.5), "low γ", size="tiny")
for sgn in (-1, 1):
    for a in (np.pi * 1.35, np.pi * 1.0, np.pi * 0.65):
        a1 = a if sgn > 0 else np.pi - a
        a2 = a1 + sgn * (-0.28) if True else a1
        p1 = (c2[0] + (r2 + 0.35) * np.cos(a1), c2[1] + (r2 + 0.35) * np.sin(a1))
        a2 = a1 - 0.3 if sgn > 0 else a1 + 0.3
        p2 = (c2[0] + (r2 + 0.35) * np.cos(a2), c2[1] + (r2 + 0.35) * np.sin(a2))
        bio.arrow(ax, p1, p2, kind="process", bend=0.1 * sgn, color=P.edge("ectoderm"))
# interior circulation: two loops
for sgn in (-1, 1):
    t = np.linspace(0, 2 * np.pi, 200)
    ax.plot(c2[0] + sgn * 1.5 + 1.0 * np.cos(t), c2[1] + 2.2 * np.sin(t), color=P.muted(), lw=0.8, zorder=3)
    bio.arrow(ax, (c2[0] + sgn * 2.5, c2[1] + 0.1), (c2[0] + sgn * 2.5, c2[1] + 0.6), kind="process", color=P.muted())
    bio.arrow(ax, (c2[0] + sgn * 0.5, c2[1] + 0.1), (c2[0] + sgn * 0.5, c2[1] - 0.4), kind="process", color=P.muted())
bio.label(ax, (19.5, 0.3), "surface flows towards high tension; interior returns", size="tiny")
