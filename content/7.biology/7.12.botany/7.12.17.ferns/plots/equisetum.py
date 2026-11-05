"""Equisetum (schematic). A: dimorphic shoots of E. arvense: an unbranched fertile shoot with a terminal
strobilus and a sterile shoot with whorled branches; nodes with leaf sheaths; rhizome with adventitious
roots and a tuber. B: strobilus in section and outside. C: one sporangiophore from the side and from
above. D: a spore with four elaters, spread when dry and coiled when wet. E: internode in transverse
section with vallecular canals, vascular bundles opposite the ridges with carinal canals, and the
central canal."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon, RegularPolygon

import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(34, 15.5)
GE, GF = P.edge("plant"), P.fill("plant")
SP, SPE = P.fill("animal"), P.edge("animal")
BR, BRE = P.fill("bone"), P.edge("bone")


def seg(p, q, w, c=None):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=c or GE, lw=w, solid_capstyle="butt", zorder=5)


def sheath(x, y, w, c=None):
    c = c or GE
    pts = [(x - w, y), (x + w, y)]
    for k in range(6):
        xx = x - w + (k + 0.5) * 2 * w / 6
        pts += []
    xs = np.linspace(x - w * 1.25, x + w * 1.25, 13)
    top = [(xx, y + (0.32 if k % 2 else 0.05)) for k, xx in enumerate(xs)]
    ax.add_patch(Polygon([(x - w * 1.1, y - 0.15)] + top + [(x + w * 1.1, y - 0.15)], closed=True, facecolor=P.mix(P.surface(), P.fill("plant"), 0.4),
                         edgecolor=c, lw=0.7, zorder=6))


# ---- A
bio.panel(ax, "A", (0.2, 15.2)); bio.label(ax, (4.6, 14.8), "E. arvense: fertile and sterile shoots", size="normal", bold=True, italic=False)
gy = 3.6
ax.plot([0.6, 8.6], [gy, gy], color=P.muted(), lw=0.8)
seg((0.8, gy - 0.9), (8.4, gy - 0.9), 3.0, P.edge("animal"))
for x in np.linspace(1.2, 8.0, 8):
    ax.plot([x, x - 0.1, x + 0.05], [gy - 0.95, gy - 1.3, gy - 1.6], color=P.muted(), lw=0.6)
ax.add_patch(Ellipse((6.8, gy - 1.5), 0.6, 0.45, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=0.8, zorder=6))
bio.label(ax, (7.6, gy - 1.5), "tuber", size="tiny", ha="left")
bio.label(ax, (4.3, gy - 1.95), "rhizome", size="tiny")
# fertile shoot
x = 2.4
seg((x, gy - 0.9), (x, 10.4), 4.0, P.edge("animal"))
for y in np.linspace(gy + 0.6, 9.8, 6):
    sheath(x, y, 0.16, P.edge("animal"))
plant.cone(ax, (x, 10.3), 2.6, kind="equisetum", section=False)
bio.label(ax, (x, gy - 0.4 + 0.0), "", size="tiny")
bio.callout(ax, (x + 0.4, 11.6), (0.9, 13.6), "strobilus")
# sterile shoot
x = 6.2
seg((x, gy - 0.9), (x, 12.6), 3.0)
for k, y in enumerate(np.linspace(gy + 0.8, 12.2, 8)):
    sheath(x, y, 0.12)
    L = 2.2 * (1 - 0.07 * k)
    for s in (-1, 1):
        a = np.radians(90 - s * 62)
        q = (x + L * np.cos(a), y + L * np.sin(a))
        seg((x, y + 0.1), q, 1.0)
        seg((x, y + 0.1), (x + 0.5 * L * np.cos(a + s * 0.25), y + 0.1 + 0.5 * L * np.sin(a + s * 0.25)), 0.7)
bio.callout(ax, (x + 0.15, 7.2), (8.8, 13.8), "leaf sheath at a node")
bio.label(ax, (2.4, 0.9), "fertile shoot (spring)", size="small")
bio.label(ax, (6.4, 0.9), "sterile shoot (summer)", size="small")

# ---- B strobilus
bio.panel(ax, "B", (10.2, 15.2)); bio.label(ax, (13.2, 14.8), "Strobilus", size="normal", bold=True)
c = plant.cone(ax, (12.0, 4.2), 7.0, kind="equisetum", section=True)
plant.cone(ax, (15.6, 4.2), 4.6, kind="equisetum", section=False)
bio.label(ax, (12.0, 3.6), "section", size="tiny")
bio.label(ax, (15.6, 3.6), "outside", size="tiny")
bio.callout(ax, c["sporangiophore"], (15.6, 12.8), "sporangiophore")
bio.callout(ax, c["sporangium"], (15.6, 11.6), "sporangium")
bio.callout(ax, c["axis"], (9.8, 12.5), "axis")

# ---- C sporangiophore
bio.panel(ax, "C", (17.6, 15.2)); bio.label(ax, (20.4, 14.8), "Sporangiophore", size="normal", bold=True)
x0, y0 = 18.6, 11.2
seg((x0 - 0.8, y0), (x0 + 0.6, y0), 2.4, BRE)
ax.add_patch(Polygon([(x0 + 0.6, y0 - 1.1), (x0 + 0.95, y0 - 1.2), (x0 + 0.95, y0 + 1.2), (x0 + 0.6, y0 + 1.1)], closed=True,
                     facecolor=GF, edgecolor=GE, lw=0.8, zorder=6))
for dy in (-0.7, 0.7):
    ax.add_patch(Ellipse((x0 + 0.05, y0 + dy), 0.85, 0.42, facecolor=SP, edgecolor=SPE, lw=0.8, zorder=7))
bio.label(ax, (x0, 9.4), "side view (axis to the left)", size="tiny")
x1 = 22.0
ax.add_patch(RegularPolygon((x1, y0), 6, radius=1.1, orientation=np.pi / 6, facecolor=GF, edgecolor=GE, lw=0.9, zorder=5))
for k in range(6):
    a = 2 * np.pi * k / 6
    ax.add_patch(Ellipse((x1 + 0.95 * np.cos(a), y0 + 0.95 * np.sin(a)), 0.5, 0.3, angle=np.degrees(a), facecolor=SP,
                         edgecolor=SPE, lw=0.6, zorder=4))
ax.add_patch(Circle((x1, y0), 0.12, facecolor=BR, edgecolor=BRE, lw=0.6, zorder=6))
bio.label(ax, (x1, 9.4), "from below: shield, stalk,\nsporangia around the stalk", size="tiny")

# ---- D spores
bio.panel(ax, "D", (17.6, 8.0)); bio.label(ax, (20.4, 7.6), "Spore with elaters", size="normal", bold=True)


def spore(x, y, dry):
    ax.add_patch(Circle((x, y), 0.45, facecolor=P.fill("plant"), edgecolor=GE, lw=0.9, zorder=7))
    for k in range(4):
        a = np.pi / 4 + k * np.pi / 2
        if dry:
            t = np.linspace(0.45, 1.9, 30)
            pts = np.c_[x + t * np.cos(a + 0.25 * np.sin(3 * t)), y + t * np.sin(a + 0.25 * np.sin(3 * t))]
            ax.plot(pts[:, 0], pts[:, 1], color=P.edge("animal"), lw=1.6, zorder=6, solid_capstyle="round")
            ax.add_patch(Ellipse(pts[-1], 0.28, 0.16, angle=np.degrees(a), facecolor=SP, edgecolor=SPE, lw=0.6, zorder=7))
        else:
            th = np.linspace(0, 2 * np.pi * 0.95, 40)
            r = 0.5 + 0.06 * k
            ax.plot(x + r * np.cos(th + k), y + r * np.sin(th + k), color=P.edge("animal"), lw=1.4, zorder=8)


spore(19.4, 4.4, True)
spore(23.0, 4.4, False)
bio.label(ax, (19.4, 2.1), "dry: elaters spread", size="tiny")
bio.label(ax, (23.0, 2.1), "wet: elaters coiled", size="tiny")

# ---- E transverse section
bio.panel(ax, "E", (25.0, 15.2)); bio.label(ax, (29.4, 14.8), "Internode, transverse section", size="normal", bold=True)
c = (29.4, 8.6)
R = 3.6
t = np.linspace(0, 2 * np.pi, 600)
rr = R * (1 + 0.05 * np.cos(12 * t))
ax.add_patch(Polygon(np.c_[c[0] + rr * np.cos(t), c[1] + rr * np.sin(t)], facecolor=P.mix(P.surface(), P.fill("parenchyma"), 0.35),
                     edgecolor=P.edge("parenchyma"), lw=1.0, zorder=2))
ax.add_patch(Circle(c, 1.35, facecolor=P.surface(), edgecolor=P.edge("parenchyma"), lw=0.8, zorder=3))
ax.add_patch(Circle(c, 2.05, fill=False, edgecolor=P.edge("endodermis"), lw=1.2, zorder=4))
for k in range(12):
    a = 2 * np.pi * k / 12
    bx, by = c[0] + 1.75 * np.cos(a), c[1] + 1.75 * np.sin(a)
    ax.add_patch(Circle((bx, by), 0.27, facecolor=P.fill("xylem"), edgecolor=P.edge("xylem"), lw=0.6, zorder=5))
    ax.add_patch(Ellipse((bx + 0.12 * np.cos(a), by + 0.12 * np.sin(a)), 0.3, 0.15, angle=np.degrees(a) + 90, facecolor=P.fill("phloem"),
                         edgecolor=P.edge("phloem"), lw=0.5, zorder=6))
    ax.add_patch(Circle((bx - 0.13 * np.cos(a), by - 0.13 * np.sin(a)), 0.09, facecolor=P.surface(), edgecolor=P.edge("xylem"), lw=0.5, zorder=6))
    a2 = a + np.pi / 12
    ax.add_patch(Circle((c[0] + 2.75 * np.cos(a2), c[1] + 2.75 * np.sin(a2)), 0.33, facecolor=P.surface(), edgecolor=P.edge("parenchyma"),
                        lw=0.6, zorder=4))
    ax.add_patch(Circle((c[0] + 3.35 * np.cos(a), c[1] + 3.35 * np.sin(a)), 0.2, facecolor=P.mix(P.surface(), P.fill("sclerenchyma"), 0.5),
                        edgecolor="none", zorder=3))
a = 0.0
bio.callout(ax, (c[0], c[1] + 0.4), (28.4, 2.2), "central canal (pith cavity)")
bio.callout(ax, (c[0] + 2.75 * np.cos(np.pi / 12), c[1] + 2.75 * np.sin(np.pi / 12)), (33.6, 4.0), "vallecular canal")
p = (c[0] + 1.62 * np.cos(np.pi / 2), c[1] + 1.62 * np.sin(np.pi / 2))
bio.callout(ax, p, (26.4, 13.6), "carinal canal")
bio.callout(ax, (c[0] + 1.95 * np.cos(np.pi / 3), c[1] + 1.95 * np.sin(np.pi / 3)), (32.8, 13.6), "vascular bundle")
bio.callout(ax, (c[0] + 2.05 * np.cos(-np.pi / 3), c[1] + 2.05 * np.sin(-np.pi / 3)), (32.4, 3.0), "endodermis")
