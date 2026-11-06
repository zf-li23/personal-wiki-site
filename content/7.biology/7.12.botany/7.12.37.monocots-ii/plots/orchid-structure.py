# Structure of an orchid flower (typical Orchidoideae / Epidendroideae, schematic). A: front view: dorsal
# and lateral sepals (outer whorl), two petals and the labellum (inner whorl) with a basal spur; the
# column in the centre. B: column in side view: anther cap with a pollinium, its stalk attached to the
# viscidium formed by the rostellum, and the sticky stigmatic cavity below. C: a pollinarium (two
# pollinia, stalks, viscidium). D: resupination: in the bud the labellum is uppermost; at anthesis the
# pedicel and ovary twist through 180 degrees and the labellum comes to lie below.
import numpy as np
from matplotlib.patches import Ellipse, Circle, PathPatch
from matplotlib.path import Path
import wikibio as bio
from wikibio.core import smooth_closed

P = bio.P
fig, ax = bio.canvas(32, 13)


def petal(c, L, W, ang, token, z=5, lobes=0):
    t = np.linspace(0, 2 * np.pi, 60, endpoint=False)
    r = 1 + (0.18 * np.cos(3 * t) if lobes else 0)
    x = W / 2 * np.sin(t) * r
    y = L / 2 * (1 - np.cos(t)) * (0.9 + 0.1 * np.cos(t))
    a = np.radians(ang - 90)
    X = c[0] + x * np.cos(a) - y * np.sin(a)
    Y = c[1] + x * np.sin(a) + y * np.cos(a)
    ax.add_patch(PathPatch(Path(np.c_[X, Y], closed=True), facecolor=P.fill(token), edgecolor=P.edge(token), lw=1.3,
                           zorder=z))
    return (c[0] + 0.6 * L * np.cos(np.radians(ang)), c[1] + 0.6 * L * np.sin(np.radians(ang)))


# ---- A: front view
bio.panel(ax, "A", (0.3, 12.7))
bio.label(ax, (5.2, 12.6), "Front view", size="title")
c = np.array([5.2, 6.6])
ds = petal(c, 4.3, 1.9, 90, "tepal", z=4)
ls1 = petal(c, 4.0, 1.7, 215, "tepal", z=4)
ls2 = petal(c, 4.0, 1.7, 325, "tepal", z=4)
p1 = petal(c, 3.6, 1.5, 150, "petal", z=5)
p2 = petal(c, 3.6, 1.5, 30, "petal", z=5)
lab = petal(c + [0, -0.2], 4.4, 3.0, 270, "highlight", z=6, lobes=1)
ax.add_patch(Ellipse(c + [0, 0.35], 0.75, 1.5, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.2, zorder=8))
bio.callout(ax, ds, (8.6, 11.8), "Dorsal sepal")
bio.callout(ax, p2, (9.6, 9.6), "Petal")
bio.callout(ax, ls2, (9.8, 4.4), "Lateral sepal")
bio.callout(ax, lab, (8.4, 1.0), "Labellum (lip)")
bio.callout(ax, c + [0, 0.6], (1.0, 10.4), "Column")

# ---- B: column side view
bio.panel(ax, "B", (11.4, 12.7))
bio.label(ax, (15.2, 12.6), "Column (side view)", size="title")
col = smooth_closed([(14.2, 2.4), (13.9, 6.0), (14.1, 9.4), (15.2, 10.6), (16.4, 10.1), (16.2, 6.0), (15.6, 2.4)], n=160)
ax.add_patch(PathPatch(Path(col, closed=True), facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.3, zorder=4))
ax.add_patch(Ellipse((15.3, 10.0), 1.9, 1.3, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=1.2, zorder=6))
ax.add_patch(Ellipse((15.4, 10.0), 0.9, 0.55, angle=20, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=1.0, zorder=7))
ax.plot([15.0, 14.6], [9.8, 8.9], color=P.edge("anther"), lw=1.2, zorder=7)
ax.add_patch(Circle((14.55, 8.75), 0.18, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=1.0, zorder=8))
ax.add_patch(Ellipse((14.55, 7.6), 0.55, 1.2, facecolor=P.light("ovary"), edgecolor=P.edge("ovary"), lw=1.0, zorder=6))
bio.callout(ax, (15.9, 10.4), (18.2, 11.6), "Anther cap")
bio.callout(ax, (15.6, 10.05), (18.4, 10.4), "Pollinium")
bio.callout(ax, (14.8, 9.35), (18.4, 9.2), "Stalk (caudicle)")
bio.callout(ax, (14.55, 8.75), (12.0, 9.6), "Viscidium")
bio.callout(ax, (14.3, 8.4), (12.0, 8.4), "Rostellum")
bio.callout(ax, (14.55, 7.4), (12.0, 6.8), "Stigma")
bio.callout(ax, (15.4, 4.0), (17.8, 3.4), "Column (stamen + style)")

# ---- C: pollinarium
bio.panel(ax, "C", (19.6, 12.7))
bio.label(ax, (22.0, 12.6), "Pollinarium", size="title")
for s in (-1, 1):
    ax.add_patch(Ellipse((22.0 + s * 0.7, 10.6), 0.9, 1.5, angle=s * 15, facecolor=P.fill("anther"),
                         edgecolor=P.edge("anther"), lw=1.1, zorder=6))
    ax.plot([22.0 + s * 0.6, 22.0], [9.9, 8.3], color=P.edge("anther"), lw=1.3, zorder=5)
ax.add_patch(Ellipse((22.0, 8.15), 0.8, 0.45, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=1.0, zorder=6))
bio.callout(ax, (22.7, 11.0), (24.4, 11.8), "Pollinia")
bio.callout(ax, (22.3, 9.1), (24.4, 9.4), "Stalks")
bio.callout(ax, (22.3, 8.1), (24.4, 7.6), "Viscidium")

# ---- D: resupination
bio.panel(ax, "D", (19.6, 6.2))
bio.label(ax, (25.6, 6.1), "Resupination", size="title")
for x0, twist, txt in ((22.0, False, "Bud"), (28.6, True, "Open flower")):
    ax.add_patch(PathPatch(Path([(x0 - 0.25, 0.8), (x0 - 0.25, 3.0), (x0 + 0.25, 3.0), (x0 + 0.25, 0.8)]),
                           facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=4))
    if twist:
        for y in np.arange(1.0, 2.9, 0.35):
            ax.plot([x0 - 0.25, x0 + 0.25], [y, y + 0.28], color=P.edge("plant"), lw=0.9, zorder=5)
        bio.label(ax, (x0 + 1.6, 1.9), "ovary twisted 180°", size="tiny", ha="left")
    ax.add_patch(Circle((x0, 3.9), 0.85, facecolor=P.fill("tepal"), edgecolor=P.edge("tepal"), lw=1.2, zorder=5))
    ly = 4.75 if not twist else 3.05
    ax.add_patch(Ellipse((x0, ly), 1.1, 0.55, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=6))
    bio.label(ax, (x0, 0.35), txt, size="small")
bio.label(ax, (22.0 + 1.3, 4.85), "labellum up", size="tiny", ha="left")
bio.label(ax, (28.6 - 1.3, 2.9), "labellum down", size="tiny", ha="right")
bio.arrow(ax, (23.8, 3.9), (26.8, 3.9), kind="process")
bio.icon(ax, "phylopic/orchid", at=(30.6, 10.8), height=3.2, color="petal")
