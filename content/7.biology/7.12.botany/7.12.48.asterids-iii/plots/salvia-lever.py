# The staminal lever of Salvia (schematic). A: resting position: short filament, connective elongated into
# a lever hinged on the filament; the upper arm carries the fertile theca inside the upper lip, the lower
# arm ends in a sterile theca that blocks the corolla throat. B: a bee pushing the lower arm turns the
# lever about the hinge; the upper arm swings down and the fertile theca dusts pollen on the bee's back.
# C: mechanics: a push F on the short lower arm (length b) turns the lever by theta; the tip of the long
# upper arm (length a) moves by about a * theta, more than the lower arm (b * theta).
import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, Polygon

P = bio.P
fig, ax = bio.canvas(34, 12)


def flower(x0):
    ax.add_patch(Polygon([(x0, 2.0), (x0 + 1.2, 2.0), (x0 + 3.0, 5.0), (x0 + 3.6, 9.4), (x0 + 5.8, 10.2),
                          (x0 + 6.6, 9.0), (x0 + 4.8, 8.4), (x0 + 4.2, 5.2), (x0 + 7.8, 4.4), (x0 + 8.4, 3.6),
                          (x0 + 4.2, 3.6), (x0 + 1.4, 1.6)], closed=True, facecolor=P.light("petal"),
                         edgecolor=P.edge("petal"), lw=1.0, zorder=2))


def lever(hinge, ang, label=True):
    h = np.array(hinge)
    u = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
    up, lo = h + 4.2 * u, h - 1.6 * u
    ax.plot([h[0], h[0] - 0.2], [h[1], h[1] - 1.3], color=P.edge("anther"), lw=2.4, zorder=5)
    ax.plot([lo[0], up[0]], [lo[1], up[1]], color=P.edge("anther"), lw=2.0, zorder=6)
    ax.add_patch(Circle(h, 0.16, facecolor=P.surface(), edgecolor=P.ink(), lw=1.0, zorder=7))
    ax.add_patch(Ellipse(up, 0.9, 0.45, angle=ang, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), zorder=7))
    ax.add_patch(Ellipse(lo, 0.7, 0.9, angle=ang, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), zorder=7))
    return h, up, lo


bio.panel(ax, "A", (0.3, 11.8))
bio.label(ax, (5.5, 11.4), "Resting", size="title")
flower(1.0)
h, up, lo = lever((5.0, 4.8), 62)
bio.callout(ax, up, (8.6, 10.6), "Fertile theca", size="small")
bio.callout(ax, lo, (8.4, 2.0), "Sterile theca (plate)", size="small")
bio.callout(ax, h, (1.0, 7.8), "Hinge", size="small")
bio.callout(ax, (4.85, 4.0), (1.0, 5.8), "Short filament", size="small")

bio.panel(ax, "B", (11.6, 11.8))
bio.label(ax, (17.0, 11.4), "Bee visiting", size="title")
flower(12.3)
h, up, lo = lever((16.3, 4.8), 20)
ax.add_patch(Ellipse((20.6, 4.4), 3.6, 1.6, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=8))
ax.add_patch(Ellipse((18.6, 4.5), 1.2, 1.0, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=9))
bio.arrow(ax, (19.0, 3.1), (17.3, 3.7), kind="process")
bio.arrow(ax, (18.8, 8.6), (20.0, 6.0), kind="process", bend=-0.3)
bio.label(ax, (21.8, 7.4), "theca swings down\nonto the bee's back", size="small")
bio.label(ax, (20.8, 2.1), "bee pushes the lower arm", size="small")

bio.panel(ax, "C", (24.6, 11.8))
bio.label(ax, (29.2, 11.4), "Lever mechanics", size="title")
h = np.array([28.0, 5.6])
for ang, ls in ((62, "-"), (32, "--")):
    u = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
    ax.plot([h[0] - 1.6 * u[0], h[0] + 4.2 * u[0]], [h[1] - 1.6 * u[1], h[1] + 4.2 * u[1]], color=P.edge("anther"),
            lw=2.0, ls=ls, zorder=5)
ax.add_patch(Circle(h, 0.16, facecolor=P.surface(), edgecolor=P.ink(), lw=1.0, zorder=7))
t = np.radians(np.linspace(32, 62, 30))
ax.plot(h[0] + 3.4 * np.cos(t), h[1] + 3.4 * np.sin(t), color=P.muted(), lw=1.0, zorder=4)
bio.label(ax, (h[0] + 3.0, h[1] + 3.0), r"$\theta$", size="normal")
bio.label(ax, (h[0] + 1.2, h[1] + 2.6), "a (upper arm)", size="small", ha="right")
bio.label(ax, (h[0] - 1.0, h[1] - 2.2), "b (lower arm)", size="small")
bio.arrow(ax, (h[0] + 0.4, h[1] - 2.2), (h[0] - 0.4, h[1] - 1.0), kind="process")
bio.label(ax, (h[0] + 1.2, h[1] - 2.6), r"$F$", size="normal")
bio.label(ax, (29.4, 1.2), r"tip displacement $\approx a\,\theta > b\,\theta$", size="small")
