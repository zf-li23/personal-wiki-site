# Asteraceae. A: radiate capitulum in longitudinal section (schematic): flat receptacle with many florets,
# ray florets at the margin, disc florets in the centre with paleae between them, phyllaries of the
# involucre outside. B: disc (tubular) floret: inferior ovary crowned by pappus, five-lobed corolla, anther
# tube around the style, bifid style branches emerging. C: ligulate floret (Taraxacum): strap with five
# teeth, beaked cypsela with capillary pappus. D: ray floret: strap with three teeth, female. E: floral
# diagram of a disc floret: calyx reduced to pappus, corolla five-lobed, five syngenesious stamens, ovary of
# one locule with one basal ovule.
import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse, Polygon
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(38, 13)


def poly(pts, token, z=5, lw=1.0, light=False):
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.light(token) if light else P.fill(token),
                         edgecolor=P.edge(token), lw=lw, zorder=z))


bio.panel(ax, "A", (0.3, 12.7))
bio.label(ax, (6.2, 12.3), "Radiate capitulum (section)", size="title")
poly([(1.0, 4.0), (11.4, 4.0), (10.6, 3.0), (6.2, 2.4), (1.8, 3.0)], "plant", light=True, z=3)
ax.plot([6.2, 6.2], [0.4, 2.4], color=P.edge("plant"), lw=3.0, zorder=2)
for k in range(5):
    for s in (-1, 1):
        x = 6.2 + s * (5.4 - 0.5 * k)
        poly([(x, 3.0 + 0.1 * k), (x + s * 0.9, 2.3 + 0.2 * k), (x + s * 0.4, 3.6 + 0.1 * k)], "plant", z=4)
for s in (-1, 1):
    poly([(6.2 + s * 4.6, 4.0), (6.2 + s * 5.1, 4.0), (6.2 + s * 8.0, 6.4), (6.2 + s * 7.6, 6.9)], "highlight", z=5)
xs = np.linspace(2.4, 10.0, 15)
for x in xs:
    h = 2.6 - 0.8 * abs(x - 6.2) / 3.8
    poly([(x - 0.18, 4.0), (x + 0.18, 4.0), (x + 0.22, 4.0 + h), (x - 0.22, 4.0 + h)], "highlight", z=5, lw=0.7)
    ax.plot([x + 0.27, x + 0.27], [4.0, 4.0 + 0.6 * h], color=P.edge("plant"), lw=0.8, zorder=6)
bio.callout(ax, (6.2 + 6.8, 5.8), (13.0, 8.6), "Ray floret", size="small")
bio.callout(ax, (6.2, 6.4), (6.2, 9.6), "Disc florets", size="small")
bio.callout(ax, (9.8, 4.6), (12.6, 6.6), "Palea", size="small")
bio.callout(ax, (10.9, 3.0), (12.6, 2.0), "Phyllaries (involucre)", size="small")
bio.callout(ax, (3.0, 3.4), (0.6, 1.2), "Receptacle", size="small")


def ovary(x, y, beak=False):
    ax.add_patch(Ellipse((x, y), 0.8, 1.6, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), zorder=5))
    top = y + 0.8
    if beak:
        ax.plot([x, x], [top, top + 1.6], color=P.edge("ovary"), lw=1.2, zorder=5)
        top += 1.6
    for a in np.linspace(-60, 60, 9):
        u = np.array([np.sin(np.radians(a)), np.cos(np.radians(a))])
        ax.plot([x, x + 1.0 * u[0]], [top, top + 1.0 * u[1]], color=P.muted(), lw=0.8, zorder=4)
    return top


bio.panel(ax, "B", (14.8, 12.7))
bio.label(ax, (17.0, 12.3), "Disc floret", size="title")
t = ovary(17.0, 2.4)
poly([(16.75, t), (17.25, t), (17.45, t + 3.0), (18.1, t + 4.0), (17.0, t + 3.6), (15.9, t + 4.0), (16.55, t + 3.0)], "highlight", z=6)
poly([(16.78, t + 2.0), (17.22, t + 2.0), (17.22, t + 3.6), (16.78, t + 3.6)], "anther", z=7)
ax.plot([17.0, 17.0], [t, t + 4.4], color=P.edge("ovary"), lw=1.2, zorder=8)
ax.plot([17.0, 16.6], [t + 4.4, t + 4.9], color=P.edge("ovary"), lw=1.2, zorder=8)
ax.plot([17.0, 17.4], [t + 4.4, t + 4.9], color=P.edge("ovary"), lw=1.2, zorder=8)
bio.callout(ax, (17.2, t + 2.8), (19.2, 6.4), "Anther tube", size="small")
bio.callout(ax, (17.4, t + 4.85), (19.0, 10.6), "Style branches", size="small")
bio.callout(ax, (17.6, t + 0.7), (19.2, 4.4), "Pappus", size="small")
bio.callout(ax, (17.35, 2.2), (19.2, 1.4), "Inferior ovary", size="small")

bio.panel(ax, "C", (21.0, 12.7))
bio.label(ax, (23.0, 12.3), "Ligulate floret", size="title")
t = ovary(23.0, 2.2, beak=True)
poly([(22.8, t), (23.2, t), (23.3, t + 1.0), (25.2, t + 1.5), (25.4, t + 3.2), (24.0, t + 3.1), (23.1, t + 1.6)], "highlight", z=6)
for k in range(5):
    y = t + 1.55 + 0.35 * k
    ax.plot([25.3, 25.55], [y, y + 0.17], color=P.edge("highlight"), lw=0.8, zorder=7)
bio.label(ax, (23.6, 0.8), "5 teeth; beaked cypsela", size="small")

bio.panel(ax, "D", (26.4, 12.7))
bio.label(ax, (28.2, 12.3), "Ray floret", size="title")
t = ovary(28.0, 2.4)
poly([(27.8, t), (28.2, t), (28.3, t + 1.0), (29.8, t + 1.4), (30.0, t + 4.6), (28.9, t + 4.5), (28.1, t + 1.6)], "highlight", z=6)
bio.label(ax, (28.6, 0.8), "3 teeth; female", size="small")

bio.panel(ax, "E", (31.0, 12.7))
bio.label(ax, (34.6, 12.3), "Disc floret diagram", size="title")
plant.floral_diagram(ax, (34.6, 7.4), 2.6, [
    dict(organ="petal", n=5, r=0.9, width=40, connate=True),
    dict(organ="stamen", n=5, r=0.58, connate=True, adnate=True),
    dict(organ="gynoecium", n=2, placentation="basal", ovules=1, size=0.28)], axis=True, bract=True, symmetry="radial")
plant.floral_formula(ax, (34.6, 2.8), "* K0 C(5) A(5) G^(2:1:1)", style="cn", size="normal")
bio.icon(ax, "phylopic/asteraceae", at=(36.8, 11.2), height=1.6)
