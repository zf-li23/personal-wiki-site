# Boraginaceae. A: a scorpioid cyme (monochasium branching on alternate sides), coiled at the tip where the
# youngest buds are, unrolling as flowers open from the base. B: flower of Trigonotis in face view: rotate
# five-lobed corolla with five faucal appendages. C: gynoecium in longitudinal section: ovary deeply
# four-lobed, the style arising from the base between the lobes (gynobasic). D: four nutlets in the
# persistent calyx, top view. E: floral diagram: five sepals, five corolla lobes, five stamens alternating
# with the lobes, two carpels divided by false septa into four locules with one ovule each.
import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, Polygon
from wikibio import botany, plant

P = bio.P
fig, ax = bio.canvas(34, 12)

bio.panel(ax, "A", (0.3, 11.7))
bio.label(ax, (4.0, 11.3), "Scorpioid cyme", size="title")
botany.inflorescence(ax, (4.0, 0.8), 9.5, kind="scorpioid cyme")

bio.panel(ax, "B", (8.6, 11.7))
bio.label(ax, (12.0, 11.3), "Corolla, face view", size="title")
c = np.array([12.0, 7.0])
for k in range(5):
    a = np.radians(90 - 72 * k)
    ax.add_patch(Ellipse(c + 1.6 * np.array([np.cos(a), np.sin(a)]), 2.2, 2.6, angle=np.degrees(a) - 90,
                         facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=1.0, zorder=4))
ax.add_patch(Circle(c, 1.0, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=1.0, zorder=5))
for k in range(5):
    a = np.radians(90 - 72 * k + 36)
    ax.add_patch(Ellipse(c + 0.7 * np.array([np.cos(a), np.sin(a)]), 0.42, 0.7, angle=np.degrees(a) - 90,
                         facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.9, zorder=6))
bio.callout(ax, c + [0.62, 0.35], (14.6, 10.3), "Faucal appendage", size="small")

bio.panel(ax, "C", (16.0, 11.7))
bio.label(ax, (19.2, 11.3), "Gynobasic style", size="title")
b = np.array([19.2, 3.2])
for s in (-1, 1):
    ax.add_patch(Ellipse(b + [s * 0.95, 0.9], 1.6, 2.0, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.1, zorder=5))
    ax.add_patch(Ellipse(b + [s * 0.95, 0.9], 0.45, 0.8, facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=0.8, zorder=6))
ax.plot([b[0], b[0]], [b[1] + 0.1, b[1] + 6.0], color=P.edge("ovary"), lw=2.4, zorder=6)
ax.add_patch(Ellipse(b + [0, 6.2], 0.7, 0.45, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), zorder=7))
ax.plot([b[0] - 2.2, b[0] + 2.2], [b[1] - 0.1, b[1] - 0.1], color=P.edge("plant"), lw=1.6, zorder=4)
bio.callout(ax, b + [0, 3.5], (21.6, 7.5), "Style from the base", size="small")
bio.callout(ax, b + [1.6, 1.2], (22.0, 2.0), "Ovary lobe (one ovule)", size="small")

bio.panel(ax, "D", (23.6, 5.0))
d = np.array([25.8, 2.3])
for k in range(5):
    a = np.radians(90 - 72 * k)
    ax.add_patch(Ellipse(d + 1.2 * np.array([np.cos(a), np.sin(a)]), 0.7, 1.6, angle=np.degrees(a) - 90,
                         facecolor=P.fill("sepal"), edgecolor=P.edge("sepal"), lw=0.9, zorder=4))
for k in range(4):
    a = np.radians(45 + 90 * k)
    ax.add_patch(Ellipse(d + 0.45 * np.array([np.cos(a), np.sin(a)]), 0.62, 0.8, angle=np.degrees(a) - 90,
                         facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.9, zorder=5))
bio.label(ax, (25.8, 0.4), "Four nutlets in the calyx", size="small")

bio.panel(ax, "E", (27.5, 11.7))
bio.label(ax, (30.8, 11.3), "Floral diagram", size="title")
plant.floral_diagram(ax, (30.8, 7.6), 2.5, [
    dict(organ="sepal", n=5, r=1.0, width=30),
    dict(organ="petal", n=5, r=0.82, width=38, connate=True),
    dict(organ="stamen", n=5, r=0.56, adnate=True),
    dict(organ="gynoecium", n=4, placentation="axile", ovules=1, size=0.3)], symmetry="radial")
plant.floral_formula(ax, (30.8, 2.6), "* K(5) C(5) A5 G_(2:4:1)", style="cn", size="normal")
