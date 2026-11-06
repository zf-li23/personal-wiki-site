# Lamiaceae and Oleaceae. A: bilabiate flower of Lamiaceae in longitudinal section (schematic): two-lipped
# calyx, corolla with a two-lobed upper and three-lobed lower lip, didynamous stamens under the upper lip,
# gynobasic style between the four ovary lobes, bifid stigma. B: floral diagram of Lamiaceae: zygomorphic,
# calyx 5, corolla 5 (upper lip 2, lower lip 3), four stamens (the adaxial median one missing), ovary of four
# locules with one ovule each. C: four nutlets (calyx removed), top view. D: floral diagram of Oleaceae:
# actinomorphic, calyx 4, corolla 4, two lateral stamens, two locules with two ovules each.
import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse, Polygon
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(36, 12.5)


def poly(pts, token, z=5, lw=1.0):
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(token), edgecolor=P.edge(token), lw=lw, zorder=z))


bio.panel(ax, "A", (0.3, 12.2))
bio.label(ax, (5.5, 11.8), "Bilabiate flower (section)", size="title")
poly([(1.6, 2.6), (3.6, 2.6), (4.0, 4.6), (3.3, 5.0), (2.6, 4.2), (1.9, 4.8), (1.3, 4.2)], "sepal", z=3)
poly([(2.0, 3.0), (3.2, 3.0), (5.0, 6.0), (6.0, 9.6), (7.6, 10.2), (8.4, 9.0), (6.8, 8.6), (5.8, 5.6),
      (8.6, 5.4), (10.2, 4.4), (9.6, 3.9), (7.0, 4.6), (4.6, 4.4), (3.0, 2.8)], "petal", z=4)
for x0, top, w in ((3.4, 8.6, 1.0), (3.0, 7.6, 1.0)):
    ax.plot([x0, x0 + 1.6, top - 2.5], [3.6, 5.2, top], color=P.edge("anther"), lw=1.3, zorder=6)
    ax.add_patch(Ellipse((top - 2.4, top + 0.15), 0.6, 0.35, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), zorder=7))
ax.plot([2.6, 3.6, 5.2, 6.4], [3.0, 5.0, 7.8, 9.5], color=P.edge("ovary"), lw=1.6, zorder=6)
ax.plot([6.4, 6.9], [9.5, 9.8], color=P.edge("ovary"), lw=1.4, zorder=6)
ax.plot([6.4, 6.6], [9.5, 9.1], color=P.edge("ovary"), lw=1.4, zorder=6)
for s in (-1, 1):
    ax.add_patch(Ellipse((2.6 + s * 0.38, 2.95), 0.6, 0.6, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), zorder=6))
bio.callout(ax, (7.3, 9.8), (9.6, 11.0), "Upper lip (2)", size="small")
bio.callout(ax, (9.0, 4.6), (10.2, 6.6), "Lower lip (3)", size="small")
bio.callout(ax, (4.7, 8.7), (1.0, 9.8), "Didynamous stamens", size="small")
bio.callout(ax, (6.7, 9.75), (8.8, 11.9), "Bifid stigma", size="small")
bio.callout(ax, (2.6, 2.7), (5.0, 1.2), "Four-lobed ovary, gynobasic style", size="small")
bio.callout(ax, (1.4, 4.2), (0.6, 6.2), "Calyx", size="small")

bio.panel(ax, "B", (12.6, 12.2))
bio.label(ax, (16.4, 11.8), "Lamiaceae", size="title")
plant.floral_diagram(ax, (16.4, 7.0), 2.9, [
    dict(organ="sepal", n=5, r=1.0, width=30, connate=True),
    dict(organ="petal", n=5, r=0.82, width=38, connate=True, phase=-36),
    dict(organ="stamen", n=5, r=0.56, phase=0, members=[dict(scale=0.0001), dict(scale=0.8), {}, {}, dict(scale=0.8)]),
    dict(organ="gynoecium", n=4, placentation="axile", ovules=1, size=0.3, phase=45)], symmetry="bilateral")
plant.floral_formula(ax, (16.4, 2.4), "↑ K(5) C(5) A4 G_(2:4:1)", style="cn", size="normal")

bio.panel(ax, "C", (21.4, 12.2))
bio.label(ax, (24.2, 11.8), "Four nutlets", size="title")
c = np.array([24.2, 7.0])
for k in range(4):
    a = np.radians(45 + 90 * k)
    ax.add_patch(Ellipse(c + 0.95 * np.array([np.cos(a), np.sin(a)]), 1.25, 1.6, angle=np.degrees(a) - 90,
                         facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=1.0, zorder=5))
ax.add_patch(Ellipse(c, 0.3, 0.3, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), zorder=6))
bio.callout(ax, c, (26.0, 3.6), "Scar of the gynobasic style", size="small")

bio.panel(ax, "D", (28.4, 12.2))
bio.label(ax, (32.2, 11.8), "Oleaceae", size="title")
plant.floral_diagram(ax, (32.2, 7.0), 2.9, [
    dict(organ="sepal", n=4, r=1.0, width=36, phase=45),
    dict(organ="petal", n=4, r=0.82, width=44, connate=True, phase=0),
    dict(organ="stamen", n=2, r=0.55, phase=90),
    dict(organ="gynoecium", n=2, placentation="axile", ovules=2, size=0.28, phase=0)], symmetry="radial")
plant.floral_formula(ax, (32.2, 2.4), "* K(4) C(4) A2 G_(2:2:2)", style="cn", size="normal")
