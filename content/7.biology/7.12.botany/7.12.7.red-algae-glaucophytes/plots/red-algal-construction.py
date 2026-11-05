"""Construction of red algae and pit connections (schematic). A: uniaxial construction, one axial filament
(dark) whose cells give off lateral branches that form the cortex. B: multiaxial construction, many axial
filaments form a medulla. C: cross-section of Polysiphonia: an axial (central) siphon cell surrounded by a
ring of pericentral cells. D: a primary pit connection in longitudinal section: the aperture in the cross
wall is plugged by a lens-shaped protein plug with caps; the plasma membrane runs continuously around it."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Rectangle, FancyBboxPatch
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(32, 13)
R = "negative"   # red algal cells


def cell(x, y, w, h, tok=R, strong=False, z=5):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.12",
                                facecolor=P.fill(tok) if strong else P.light(tok), edgecolor=P.edge(tok), lw=0.9, zorder=z))


def head(x, L, t):
    bio.panel(ax, L, (x, 12.8))
    bio.label(ax, (x + 0.6, 12.55), t, size="small", bold=True, ha="left", va="center")


# A uniaxial
head(0.2, "A", "Uniaxial")
x0 = 4.0
for k in range(9):
    y = 1.5 + k * 1.05
    cell(x0, y, 0.7, 0.95, strong=True)
    n = min(8 - k, 6)
    for sgn in (-1, 1):
        for j in range(1, 2 + n // 2):
            cell(x0 + sgn * (0.6 + 0.55 * j), y + 0.25 * j, 0.5, 0.42)
cell(x0, 1.5 + 9 * 1.05 - 0.1, 0.55, 0.5, strong=True)
bio.callout(ax, (x0, 10.85), (x0 + 2.6, 11.5), "apical cell", size="tiny")
bio.callout(ax, (x0, 4.6), (x0 + 3.5, 3.2), "axial filament", size="tiny")
bio.callout(ax, (x0 - 2.3, 8.3), (x0 - 3.2, 10.6), "cortex (laterals)", size="tiny")

# B multiaxial
head(8.2, "B", "Multiaxial")
for xa in (10.6, 11.3, 12.0, 12.7):
    for k in range(8):
        cell(xa, 1.5 + k * 1.1 + (xa * 3) % 0.5, 0.5, 0.95, strong=True)
for sgn, xa in ((-1, 10.6), (1, 12.7)):
    for k in range(1, 8):
        y = 1.6 + k * 1.1
        for j in range(1, 4):
            cell(xa + sgn * 0.5 * j, y + 0.22 * j, 0.42, 0.38)
bio.label(ax, (11.65, 0.6), "medulla of many axial filaments", size="tiny", color=P.muted())

# C Polysiphonia cross-section
head(16.2, "C", "Cross-section")
bio.label(ax, (19.8, 11.8), "Polysiphonia", size="small", italic=True, color=P.muted())
c = np.array([19.8, 7.0])
for k in range(8):
    a = 2 * np.pi * k / 8
    q = c + 1.55 * np.array([np.cos(a), np.sin(a)])
    ax.add_patch(Circle(q, 0.62, facecolor=P.light(R), edgecolor=P.edge(R), lw=1.0, zorder=5))
ax.add_patch(Circle(c, 0.95, facecolor=P.fill(R), edgecolor=P.edge(R), lw=1.2, zorder=6))
bio.callout(ax, c, (c[0] + 2.0, c[1] + 3.2), "axial (central) siphon", size="tiny")
bio.callout(ax, c + np.array([1.55, -0.0]), (c[0] + 3.0, c[1] - 2.8), "pericentral cells", size="tiny")

# D pit connection
head(24.2, "D", "Primary pit connection")
xc, yc = 28.2, 6.2
for yy, lab in ((yc + 2.2, "upper cell"), (yc - 2.2, "lower cell")):
    ax.add_patch(FancyBboxPatch((xc - 2.4, yy - 1.9), 4.8, 3.8, boxstyle="round,pad=0,rounding_size=0.3",
                                facecolor=P.fill("cytoplasm"), edgecolor=P.edge(R), lw=1.2, zorder=4))
    bio.label(ax, (xc - 2.1, yy + (1.2 if yy > yc else -1.2)), lab, size="tiny", ha="left", color=P.muted())
# cross wall with aperture
for x0_, x1_ in ((xc - 2.4, xc - 0.8), (xc + 0.8, xc + 2.4)):
    ax.add_patch(Rectangle((x0_, yc - 0.3), x1_ - x0_, 0.6, facecolor=P.fill("cell_wall"), edgecolor=P.edge("cell_wall"), lw=0.9, zorder=6))
ax.add_patch(Ellipse((xc, yc), 1.7, 0.75, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=1.2, zorder=7))
for sgn in (1, -1):
    ax.add_patch(Ellipse((xc, yc + sgn * 0.42), 1.3, 0.22, facecolor=P.fill("carbohydrate"), edgecolor=P.edge("carbohydrate"), lw=0.8, zorder=8))
# membrane continuity
t = np.linspace(0, 1, 50)
for sgn in (1, -1):
    xs = xc + sgn * (0.9 + 0.05 * np.sin(np.pi * t))
    ys = yc - 0.6 + 1.2 * t
    ax.plot(xs, ys, color=P.edge("membrane"), lw=1.4, zorder=9)
bio.callout(ax, (xc, yc), (xc + 3.3, yc + 0.9), "pit plug (protein)", size="tiny")
bio.callout(ax, (xc + 0.3, yc + 0.45), (xc + 3.3, yc + 1.9), "plug cap", size="tiny")
bio.callout(ax, (xc + 1.6, yc + 0.1), (xc + 3.3, yc - 0.6), "cross wall", size="tiny")
bio.callout(ax, (xc - 0.93, yc + 0.2), (xc - 3.2, yc + 0.0), "plasma membrane", size="tiny")
