"""Root-shoot transition region in a seedling with a diarch root (schematic). Left: the seedling axis with
the levels of the sections. Right, from bottom to top: (1) root: two xylem strands (blue; protoxylem,
dark dot, at the outer ends: exarch) alternating with two phloem strands (orange); (2) lower hypocotyl:
each xylem strand forks; (3) middle hypocotyl: the halves swing sideways and the protoxylem turns inwards
while the phloem strands divide; (4) upper hypocotyl: four collateral bundles, phloem outside, xylem
inside with endarch protoxylem, a pith in the centre; the bundles pass in pairs into the two cotyledons.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 12.6)
XY, PH = "xylem", "phloem"

# ---- seedling axis ---------------------------------------------------------------------------------------
ax_x = 2.6
soil_y = 4.4
ax.plot([0.6, 4.8], [soil_y, soil_y], color=P.muted(), lw=1.0, ls=(0, (4, 3)), zorder=2)
ax.add_patch(Polygon([(ax_x - 0.18, 0.4), (ax_x + 0.18, 0.4), (ax_x + 0.24, 9.6), (ax_x - 0.24, 9.6)], closed=True,
                     facecolor=P.fill("bone"), edgecolor=P.edge("bone"), lw=1.0, zorder=4))
for sg in (-1, 1):
    ax.add_patch(Ellipse((ax_x + sg * 1.05, 10.1), 2.0, 0.8, angle=sg * 20, facecolor=P.fill("plant"),
                         edgecolor=P.edge("plant"), lw=1.0, zorder=5))
ax.add_patch(Ellipse((ax_x, 10.5), 0.35, 0.7, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=0.8, zorder=5.5))
for k in range(4):
    y = 1.5 + k * 0.6
    ax.plot([ax_x, ax_x + (0.9 if k % 2 else -0.9)], [y, y - 0.5], color=P.edge("bone"), lw=0.8, zorder=3)
bio.label(ax, (0.9, 1.0), "Root", size="small", ha="left")
bio.label(ax, (0.6, 7.0), "Hypocotyl", size="small", ha="left")
bio.label(ax, (4.6, 11.3), "Cotyledons", size="small")
levels = [2.2, 5.2, 7.0, 8.8]
SX = [8.0, 12.6, 17.2, 21.8]
for k, (y, sx) in enumerate(zip(levels, SX)):
    ax.plot([ax_x - 0.4, ax_x + 0.4], [y, y], color=P.ink(), lw=1.2, zorder=6)
    bio.label(ax, (ax_x + 0.6, y), str(k + 1), size="small", ha="left", va="center")
    bio.label(ax, (sx, 1.1), str(k + 1), size="title")

# ---- sections -------------------------------------------------------------------------------------------
R = 2.0
CY = 5.6


def stele(c):
    ax.add_patch(Circle(c, R, facecolor=P.light("cytoplasm"), edgecolor=P.edge("endodermis"), lw=1.6, zorder=3))


def xylem_strand(p_outer, p_inner, n=4):
    """A row of xylem cells from protoxylem (p_outer end, small dark) to metaxylem (larger)."""
    a = np.asarray(p_outer, float)
    b = np.asarray(p_inner, float)
    for i in range(n):
        q = a + (b - a) * i / max(1, n - 1)
        r = 0.12 + 0.07 * i
        ax.add_patch(Circle(q, r, facecolor=P.fill(XY), edgecolor=P.edge(XY), lw=0.7, zorder=5))
    ax.add_patch(Circle(a, 0.09, facecolor=P.edge(XY), edgecolor="none", zorder=5.5))


def phloem(p, rx=0.42, ry=0.28, ang=0):
    ax.add_patch(Ellipse(p, 2 * rx, 2 * ry, angle=ang, facecolor=P.fill(PH), edgecolor=P.edge(PH), lw=0.8, zorder=5))


def pol(c, r, a):
    return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))


for sx in SX:
    stele((sx, CY))
# 1 root: diarch
c = (SX[0], CY)
for a in (0, 180):
    xylem_strand(pol(c, 1.6, a), pol(c, 0.2, a), n=5)
for a in (90, 270):
    phloem(pol(c, 1.35, a), ang=a + 90)
# 2 lower hypocotyl: each strand forks
c = (SX[1], CY)
for a in (0, 180):
    for d in (-14, 14):
        xylem_strand(pol(c, 1.6, a + d), pol(c, 0.55, a + d * 2.2), n=4)
for a in (90, 270):
    for d in (-10, 10):
        phloem(pol(c, 1.45, a + d), rx=0.3, ry=0.22, ang=a + 90)
# 3 middle: halves swing towards the phloem, protoxylem turning inwards
c = (SX[2], CY)
for a in (0, 180):
    for d in (-1, 1):
        mid = a + d * 38
        xylem_strand(pol(c, 1.0, mid - d * 10), pol(c, 1.35, mid + d * 18), n=4)
for a in (90, 270):
    for d in (-1, 1):
        phloem(pol(c, 1.55, a + d * 22), rx=0.32, ry=0.22, ang=a + d * 22 + 90)
# 4 upper hypocotyl: four collateral bundles, endarch, pith
c = (SX[3], CY)
ax.add_patch(Circle(c, 0.75, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cytoplasm"), lw=0.6, zorder=4))
for a in (55, 125, 235, 305):
    phloem(pol(c, 1.6, a), rx=0.38, ry=0.25, ang=a + 90)
    xylem_strand(pol(c, 0.85, a), pol(c, 1.3, a), n=3)
bio.callout(ax, c, (24.6, 9.8), "Pith", size="small")
bio.callout(ax, pol(c, 0.85, 305), (24.6, 2.0), "Protoxylem (endarch)", size="small")
bio.callout(ax, pol((SX[0], CY), 1.6, 0), (9.6, 9.8), "Protoxylem (exarch)", size="small")
bio.callout(ax, pol((SX[0], CY), 1.35, 270), (6.4, 2.0), "Phloem", size="small")
bio.callout(ax, pol((SX[0], CY), 0.6, 180), (6.0, 9.8), "Xylem", size="small")
for x0, x1 in zip(SX[:-1], SX[1:]):
    ax.annotate("", xy=(x1 - R - 0.15, CY), xytext=(x0 + R + 0.15, CY),
                arrowprops=dict(arrowstyle="->", color=P.muted(), lw=1.0))
bio.label(ax, (14.9, 11.9), "upwards: root  →  stem", size="small", color=P.muted())
