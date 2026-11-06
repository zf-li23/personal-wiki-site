# Apocynaceae, Asclepiadoideae (schematic after Asclepias). A: flower in side view, corolla lobes reflexed,
# five hooded corona lobes with horns around the central gynostegium. B: top view of the gynostegium: five
# anthers fused with the style head; between neighbouring anther wings a slit (guide rail) with a dark
# corpusculum at its upper end; dashed outlines mark the pollinia in the anther sacs. C: a pollinarium:
# corpusculum, two translator arms and two pollinia from adjacent anthers. D: Periplocoideae translator:
# a spoon-shaped carrier holding pollen tetrads, with an adhesive disc at its base. E: floral diagram of
# Apocynaceae: five sepals, contorted corolla of five lobes, five stamens alternating with the lobes,
# two free carpels.
import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, Polygon
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(36, 13)


def poly(pts, token, z=5, lw=1.0):
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(token), edgecolor=P.edge(token), lw=lw, zorder=z))


# A: side view
bio.panel(ax, "A", (0.3, 12.7))
bio.label(ax, (4.6, 12.2), "Flower (side view)", size="title")
cx, by = 4.6, 3.0
ax.plot([cx, cx], [0.8, by], color=P.edge("plant"), lw=2.2, zorder=3)
for s in (-1, 1):
    for k, dx in enumerate((0.9, 2.1)):
        poly([(cx + s * 0.3, by + 0.3), (cx + s * (dx + 0.9), by - 1.4 - k * 0.3), (cx + s * (dx + 0.3), by - 1.7 - k * 0.3)],
             "petal", z=3)
poly([(cx - 0.9, by), (cx + 0.9, by), (cx + 0.6, by + 0.6), (cx - 0.6, by + 0.6)], "sepal", z=4)
for s, dx in ((-1, 1.3), (0, 0), (1, 1.3)):
    x0 = cx + s * dx
    poly([(x0 - 0.45, by + 0.6), (x0 + 0.45, by + 0.6), (x0 + 0.55, by + 3.0), (x0, by + 3.3), (x0 - 0.55, by + 3.0)],
         "highlight", z=6 if s == 0 else 5)
    ax.plot([x0 + 0.1, x0 + 0.35 * (s if s else 1) + 0.2, x0 + 0.5 * (s if s else 1)],
            [by + 2.2, by + 3.6, by + 4.3], color=P.edge("highlight"), lw=2.0, zorder=7)
poly([(cx - 0.75, by + 3.0), (cx + 0.75, by + 3.0), (cx + 0.9, by + 4.5), (cx - 0.9, by + 4.5)], "anther", z=4)
ax.add_patch(Ellipse((cx, by + 4.6), 2.0, 0.6, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.0, zorder=5))
bio.callout(ax, (cx + 1.6, by + 1.6), (8.2, 6.0), "Corona hood", size="small")
bio.callout(ax, (cx + 1.85, by + 4.2), (8.2, 8.0), "Horn", size="small")
bio.callout(ax, (cx + 0.6, by + 4.65), (8.2, 9.6), "Gynostegium", size="small")
bio.callout(ax, (cx - 2.6, by - 1.6), (1.0, 6.5), "Reflexed corolla", size="small")

# B: top view of the gynostegium
bio.panel(ax, "B", (10.5, 12.7))
bio.label(ax, (14.3, 12.2), "Gynostegium (top view)", size="title")
c = np.array([14.3, 6.6])
ax.add_patch(Circle(c, 3.2, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=1.2, zorder=4))
ax.add_patch(Circle(c, 1.5, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.0, zorder=6))
bio.label(ax, c, "Style\nhead", size="tiny")
for k in range(5):
    a = np.radians(90 - 72 * k)
    u = np.array([np.cos(a), np.sin(a)])
    v = np.array([-u[1], u[0]])
    p0, p1 = c + 1.6 * u, c + 3.3 * u
    ax.plot(*np.array([p0, p1]).T, color=P.ink(), lw=1.6, zorder=7)
    ax.add_patch(Circle(c + 1.75 * u, 0.24, facecolor=P.edge("anther"), edgecolor=P.ink(), lw=0.8, zorder=8))
    for s in (-1, 1):
        q = c + 2.35 * u + s * 0.75 * v
        ax.add_patch(Ellipse(q, 0.55, 1.2, angle=np.degrees(a) - 90 + s * 25, fill=False, ls="--",
                             edgecolor=P.edge("anther"), lw=0.9, zorder=7))
bio.callout(ax, c + 3.2 * np.array([0, 1]), (17.9, 11.3), "Guide rail (slit)", size="small")
bio.callout(ax, c + 1.75 * np.array([0, 1]) + [0.2, 0], (18.6, 9.6), "Corpusculum", size="small")
bio.callout(ax, c + np.array([1.2, 2.0]), (18.6, 8.2), "Pollinium (in sac)", size="small")

# C: pollinarium
bio.panel(ax, "C", (21.0, 12.7))
bio.label(ax, (24.0, 12.2), "Pollinarium", size="title")
k0 = np.array([24.0, 9.6])
poly([k0 + [-0.25, 0.5], k0 + [0.25, 0.5], k0 + [0.2, -0.5], k0 + [-0.2, -0.5]], "neutral", z=6)
ax.add_patch(Polygon([k0 + [-0.25, 0.5], k0 + [0.25, 0.5], k0 + [0.2, -0.5], k0 + [-0.2, -0.5]], closed=True,
                     facecolor=P.ink(), edgecolor=P.ink(), zorder=7))
for s in (-1, 1):
    arm = np.array([k0 + [0, -0.4], k0 + [s * 0.9, -1.0], k0 + [s * 1.4, -1.8]])
    ax.plot(arm[:, 0], arm[:, 1], color=P.edge("anther"), lw=2.0, zorder=5)
    ax.add_patch(Ellipse(k0 + [s * 1.6, -3.6], 1.1, 3.4, angle=-s * 8, facecolor=P.fill("anther"),
                         edgecolor=P.edge("anther"), lw=1.1, zorder=6))
bio.callout(ax, k0 + [0.2, 0.3], (26.5, 11.3), "Corpusculum", size="small")
bio.callout(ax, k0 + [1.0, -1.1], (27.0, 8.6), "Translator arm", size="small")
bio.callout(ax, k0 + [2.1, -4.0], (27.0, 5.0), "Pollinium", size="small")
bio.label(ax, (24.0, 3.5), "from two adjacent anthers", size="small")

# D: Periploca translator
bio.panel(ax, "D", (21.0, 2.8))
d0 = np.array([22.6, 1.3])
poly([d0 + [-0.5, 0.6], d0 + [0.5, 0.6], d0 + [0.3, -0.2], d0 + [-0.3, -0.2]], "petal", z=5)
ax.plot([d0[0], d0[0]], [d0[1] - 0.2, d0[1] - 0.9], color=P.edge("petal"), lw=1.6, zorder=5)
ax.add_patch(Ellipse(d0 + [0, -1.0], 0.7, 0.3, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), zorder=6))
for i in range(4):
    ax.add_patch(Circle(d0 + [-0.25 + 0.17 * i, 0.85], 0.12, facecolor=P.fill("anther"), edgecolor=P.edge("anther"),
                        lw=0.6, zorder=6))
bio.label(ax, (25.5, 1.0), "Periplocoideae: tetrads\non a spoon-shaped translator", size="small")

# E: floral diagram
bio.panel(ax, "E", (29.0, 12.7))
bio.label(ax, (32.6, 12.2), "Floral diagram", size="title")
plant.floral_diagram(ax, (32.6, 7.4), 2.7, [
    dict(organ="sepal", n=5, r=1.0, width=30),
    dict(organ="petal", n=5, r=0.82, width=40, connate=True),
    dict(organ="stamen", n=5, r=0.55),
    dict(organ="gynoecium", n=2, fused=False, size=0.22)], symmetry="radial")
plant.floral_formula(ax, (32.6, 2.0), "* K(5) C(5) A5 G_2:1:∞", style="cn", size="normal")
