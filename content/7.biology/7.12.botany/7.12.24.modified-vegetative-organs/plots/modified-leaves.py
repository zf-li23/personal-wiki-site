"""Three leaf modifications (schematic). A: pea (Pisum sativum) leaf: pairs of leaflets below, the upper
leaflet pairs of the rachis replaced by branched tendrils, a pair of large leafy stipules at the base.
B: pitcher plant (Nepenthes) leaf: flat photosynthetic leaf base, the midrib continued as a tendril that
ends in a lidded pitcher. C: Acacia heteroblasty: successive seedling leaves from a bipinnate leaf,
through transitional leaves with a flattened petiole and reduced pinnae, to the sickle-shaped phyllode of
the adult plant with parallel veins.
"""

import math

import numpy as np
from matplotlib.patches import Ellipse, PathPatch, Polygon
from matplotlib.path import Path

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(27.0, 11.6)
EC, FC = P.edge("plant"), P.fill("plant")


def curve(pts, lw=1.4, color=None, z=6):
    p = np.asarray(pts, float)
    t = np.linspace(0, 1, len(p))
    tt = np.linspace(0, 1, 80)
    xs = np.interp(tt, t, p[:, 0])
    ys = np.interp(tt, t, p[:, 1])
    ax.plot(xs, ys, color=color or EC, lw=lw, zorder=z, solid_capstyle="round")


def coil(start, direction, r=0.25, turns=1.6, z=6):
    a0 = math.radians(direction)
    t = np.linspace(0, turns * 2 * math.pi, 80)
    rr = r * (1 - t / (turns * 2 * math.pi) * 0.7)
    cx = start[0] + r * math.cos(a0 + math.pi / 2)
    cy = start[1] + r * math.sin(a0 + math.pi / 2)
    xs = cx + rr * np.cos(a0 - math.pi / 2 + t)
    ys = cy + rr * np.sin(a0 - math.pi / 2 + t)
    ax.plot(xs, ys, color=EC, lw=1.0, zorder=z)


# ---- A pea leaf ---------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 11.4))
bio.label(ax, (0.85, 11.37), "Pea: leaflet tendrils", size="title", ha="left", va="top")
x0, y0 = 4.2, 0.8
for sg in (-1, 1):  # leafy stipules
    B.leaf(ax, (x0, y0 + 0.2), 1.8, 90 + sg * 55, shape="ovate", petiole=0, venation="pinnate", secondaries=3, zorder=5)
ax.plot([x0, x0], [y0, y0 + 9.0], color=EC, lw=1.6, zorder=6)
for k, y in enumerate((2.6, 4.2)):
    for sg in (-1, 1):
        B.leaf(ax, (x0, y), 1.6, 90 + sg * 62, shape="elliptic", petiole=0.15, venation="pinnate", secondaries=3, zorder=6)
for y in (5.7, 7.0, 8.2):
    for sg in (-1, 1):
        end = (x0 + sg * 1.5, y + 0.9)
        curve([(x0, y), (x0 + sg * 0.8, y + 0.65), end], lw=1.0)
        coil(end, 90 - sg * 45, r=0.22)
curve([(x0, y0 + 9.0), (x0 + 0.3, y0 + 9.6)], lw=1.0)
coil((x0 + 0.3, y0 + 9.6), 60, r=0.2)
bio.callout(ax, (x0 + 1.3, 7.8), (7.6, 9.6), "Tendrils (leaflets)", size="small")
bio.callout(ax, (x0 + 1.0, 3.2), (7.6, 4.6), "Leaflet", size="small")
bio.callout(ax, (x0 + 0.9, 1.6), (7.6, 1.6), "Leafy stipule", size="small")

# ---- B pitcher plant ---------------------------------------------------------------------------------
bio.panel(ax, "B", (9.2, 11.4))
bio.label(ax, (9.85, 11.37), "Nepenthes: pitcher leaf", size="title", ha="left", va="top")
sx = 10.2
ax.plot([sx, sx], [0.6, 10.6], color=EC, lw=4.0, zorder=4)
lf = B.leaf(ax, (sx, 6.0), 4.2, 20, shape="oblanceolate", petiole=0.0, venation="pinnate", secondaries=6)
tip = lf["apex"]
tend = [tip, (tip[0] + 0.8, tip[1] - 0.4), (tip[0] + 1.0, tip[1] - 1.6), (tip[0] + 0.5, tip[1] - 2.6)]
curve(tend, lw=1.4)
pb = np.array(tend[-1])
# pitcher body: urn shape opening upward
t = np.linspace(0, 1, 40)
w = 0.55 + 0.45 * np.sin(np.pi * t) * (1 - 0.3 * t)
yy = pb[1] - 0.2 - 3.0 * (1 - t)
left = np.c_[pb[0] - w, yy]
right = np.c_[pb[0] + w, yy][::-1]
body = np.vstack([left, right])
ax.add_patch(Polygon(body, closed=True, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.1, zorder=6))
ax.add_patch(Ellipse((pb[0], pb[1] - 0.2), 1.2, 0.35, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=1.1, zorder=6.5))
lid = Ellipse((pb[0] - 0.55, pb[1] + 0.35), 1.1, 0.4, angle=35, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
              lw=1.0, zorder=6.6)
ax.add_patch(lid)
fluid = np.vstack([np.c_[left[:12, 0], left[:12, 1]], np.c_[right[-12:, 0], right[-12:, 1]]])
ax.add_patch(Polygon(fluid, closed=True, facecolor=P.light("extracellular"), edgecolor="none", zorder=6.4))
bio.callout(ax, B.leaf_point(lf, 0.5, 0.3), (14.2, 10.6), "Flat leaf base (blade)", size="small")
bio.callout(ax, (tip[0] + 0.95, tip[1] - 1.2), (15.6, 8.6), "Tendril (midrib)", size="small")
bio.callout(ax, (pb[0] - 0.6, pb[1] + 0.4), (10.9, 2.6), "Lid", size="small")
bio.callout(ax, (pb[0] + 0.5, pb[1] - 0.2), (15.6, 6.4), "Peristome", size="small")
bio.callout(ax, (pb[0] + 0.6, pb[1] - 2.5), (15.4, 1.4), "Pitcher", size="small")

# ---- C Acacia heteroblasty ---------------------------------------------------------------------------
bio.panel(ax, "C", (17.2, 11.4))
bio.label(ax, (17.85, 11.37), "Acacia: from compound leaf to phyllode", size="title", ha="left", va="top")
xs = [18.8, 21.4, 24.0, 26.0]
for k, x in enumerate(xs):
    base = (x, 0.9)
    if k == 0:
        B.compound_leaf(ax, base, 5.0, 90, kind="bipinnate", leaflets=4, pinnae=2)
    elif k in (1, 2):
        wpet = 0.18 if k == 1 else 0.38
        L = 3.2 if k == 1 else 4.2
        pts = [(x, 0.9), (x - wpet, 0.9 + L * 0.5), (x - wpet * 0.6, 0.9 + L), (x + wpet * 0.6, 0.9 + L), (x + wpet, 0.9 + L * 0.5)]
        ax.add_patch(Polygon(pts, closed=True, facecolor=FC, edgecolor=EC, lw=0.9, zorder=6))
        B.compound_leaf(ax, (x, 0.9 + L), 2.6 if k == 1 else 1.6, 90, kind="bipinnate", leaflets=3, pinnae=1 if k == 2 else 2,
                        petiole=0.2)
    else:
        t = np.linspace(0, 1, 50)
        cxs = x + 0.6 * np.sin(t * 2.2) - 0.2
        cys = 0.9 + 7.0 * t
        hw = 0.45 * np.sin(np.pi * np.clip(t * 1.05, 0, 1)) + 0.02
        outline = np.vstack([np.c_[cxs - hw, cys], np.c_[cxs + hw, cys][::-1]])
        ax.add_patch(Polygon(outline, closed=True, facecolor=FC, edgecolor=EC, lw=1.0, zorder=6))
        for f in (-0.5, 0.0, 0.5):
            ax.plot(cxs[2:-3] + hw[2:-3] * f, cys[2:-3], color=EC, lw=0.6, zorder=6.2)
bio.label(ax, (18.8, 0.45), "seedling", size="tiny", color=P.muted())
bio.label(ax, (26.0, 0.45), "adult", size="tiny", color=P.muted())
ax.annotate("", xy=(26.6, 0.2), xytext=(18.2, 0.2), arrowprops=dict(arrowstyle="->", color=P.muted(), lw=0.9))
bio.callout(ax, (25.95, 5.5), (26.8, 9.8), "Phyllode", size="small")
bio.callout(ax, (24.0, 3.0), (22.6, 9.8), "Flattened petiole", size="small")
