# The cyathium of Euphorbia (schematic). A: longitudinal section: a cup-shaped involucre of five fused
# bracts with thick nectar glands on the rim; inside, many male flowers each reduced to a single stamen
# jointed to its pedicel; in the centre one stalked female flower with a three-locular ovary and three
# bifid styles. B: top view: glands alternating with the involucral lobes. C: poinsettia: red bracts
# below a cluster of cyathia, each with one large yellow gland.
import math

import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, Polygon
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(34, 14)

bio.panel(ax, "A", (0.3, 13.8))
cx, by = 6.5, 2.0
cup = [(cx - 3.0, by + 6.0), (cx - 2.6, by + 1.0), (cx - 1.0, by), (cx + 1.0, by), (cx + 2.6, by + 1.0),
       (cx + 3.0, by + 6.0), (cx + 2.5, by + 6.0), (cx + 2.1, by + 1.4), (cx + 0.8, by + 0.5), (cx - 0.8, by + 0.5),
       (cx - 2.1, by + 1.4), (cx - 2.5, by + 6.0)]
ax.add_patch(Polygon(cup, closed=True, facecolor=P.fill("bract"), edgecolor=P.edge("bract"), lw=1.2, zorder=4))
for s in (-1, 1):
    ax.add_patch(Ellipse((cx + s * 3.15, by + 6.2), 1.4, 0.7, facecolor=P.fill("highlight"),
                         edgecolor=P.edge("highlight"), lw=1.1, zorder=5))
ax.plot([cx, cx], [by - 1.6, by], color=P.edge("plant"), lw=3, zorder=3)
for k, (dx, h) in enumerate([(-1.7, 3.6), (-1.1, 4.4), (-0.6, 3.2), (0.6, 3.4), (1.1, 4.6), (1.7, 3.8)]):
    x0, y0 = cx + dx * 0.7, by + 0.6
    xj, yj = cx + dx * 0.9, by + 0.6 + h * 0.45
    ax.plot([x0, xj], [y0, yj], color=P.edge("plant"), lw=1.0, zorder=6)
    ax.add_patch(Circle((xj, yj), 0.09, facecolor=P.ink(), edgecolor="none", zorder=7))
    xt, yt = cx + dx * 1.15, by + 0.6 + h
    ax.plot([xj, xt], [yj, yt], color=P.edge("anther"), lw=1.0, zorder=6)
    ax.add_patch(Ellipse((xt, yt + 0.15), 0.42, 0.32, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.8,
                         zorder=7))
ax.plot([cx, cx + 0.3, cx + 1.2], [by + 0.6, by + 6.5, by + 8.0], color=P.edge("plant"), lw=1.4, zorder=6)
ax.add_patch(Ellipse((cx + 1.35, by + 8.5), 1.1, 1.0, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.1,
                     zorder=8))
for a in (60, 100, 140):
    t = math.radians(a)
    p = np.array([cx + 1.35, by + 9.0])
    q = p + 0.8 * np.array([math.cos(t), math.sin(t)])
    ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge("ovary"), lw=1.1, zorder=8)
    for d in (-15, 15):
        u = math.radians(a + d)
        ax.plot([q[0], q[0] + 0.3 * math.cos(u)], [q[1], q[1] + 0.3 * math.sin(u)], color=P.edge("ovary"), lw=1.0)
bio.callout(ax, (cx + 3.4, by + 6.2), (cx + 4.6, 12.6), "Nectar gland", size="small")
bio.callout(ax, (cx - 2.6, by + 3.0), (0.6, 1.0), "Involucre (5 fused bracts)", size="small")
bio.callout(ax, (cx - 1.0, by + 2.5), (0.6, 10.6), "Joint: pedicel / filament", size="small")
bio.callout(ax, (cx - 1.9, by + 4.5), (0.6, 12.4), "Male flower = 1 stamen", size="small")
bio.callout(ax, (cx + 1.8, by + 8.6), (cx + 4.6, 10.8), "Female flower (stalked, 3-locular)", size="small")

bio.panel(ax, "B", (13.6, 13.8))
c = np.array([17.5, 7.0])
ax.add_patch(Circle(c, 2.6, facecolor=P.light("bract"), edgecolor=P.edge("bract"), lw=1.2, zorder=3))
for k in range(5):
    a = math.radians(90 + 72 * k)
    ax.add_patch(Polygon([c + 2.0 * np.array([math.cos(a - 0.25), math.sin(a - 0.25)]),
                          c + 2.9 * np.array([math.cos(a), math.sin(a)]),
                          c + 2.0 * np.array([math.cos(a + 0.25), math.sin(a + 0.25)])], closed=True,
                         facecolor=P.fill("bract"), edgecolor=P.edge("bract"), lw=1.0, zorder=4))
    b = a + math.radians(36)
    ax.add_patch(Ellipse(c + 2.75 * np.array([math.cos(b), math.sin(b)]), 1.0, 0.55, angle=math.degrees(b) + 90,
                         facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=5))
for k in range(12):
    a = 2 * math.pi * k / 12
    ax.add_patch(Ellipse(c + 1.35 * np.array([math.cos(a), math.sin(a)]), 0.32, 0.24, facecolor=P.fill("anther"),
                         edgecolor=P.edge("anther"), lw=0.6, zorder=6))
plant.ovary(ax, tuple(c), 0.6, n=3, placentation="axile", ovules=1, token="ovary")
bio.label(ax, (17.5, 3.2), "Top view: glands alternate with lobes", size="small")

bio.panel(ax, "C", (22.8, 13.8))
c = np.array([28.2, 6.8])
for k in range(7):
    a = math.radians(90 + 360 / 7 * k)
    tip = c + 4.2 * np.array([math.cos(a), math.sin(a)])
    nrm = np.array([-math.sin(a), math.cos(a)]) * 0.9
    ax.add_patch(Polygon([c + nrm * 0.3, c + 1.8 * (tip - c) / 4.2 * 1.6 + nrm, tip, c + 1.8 * (tip - c) / 4.2 * 1.6 - nrm,
                          c - nrm * 0.3], closed=True, facecolor=P.fill("negative"), edgecolor=P.edge("negative"),
                         lw=1.0, zorder=4))
for k in range(6):
    a = 2 * math.pi * k / 6
    p = c + 0.7 * np.array([math.cos(a), math.sin(a)])
    ax.add_patch(Circle(p, 0.32, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=0.8, zorder=6))
    ax.add_patch(Ellipse(p + np.array([0.18, 0.18]), 0.28, 0.18, facecolor=P.fill("highlight"),
                         edgecolor=P.edge("highlight"), lw=0.7, zorder=7))
bio.callout(ax, (28.2 + 2.6, 6.8 + 1.4), (31.0, 12.6), "Red bracts", size="small")
bio.callout(ax, (28.2, 7.5), (25.2, 12.6), "Cyathia with yellow glands", size="small")
bio.label(ax, (28.2, 1.6), r"$\it{Euphorbia\ pulcherrima}$", size="small")
