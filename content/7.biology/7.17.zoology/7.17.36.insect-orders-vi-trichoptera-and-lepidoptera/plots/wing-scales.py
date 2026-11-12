# The scales of a butterfly wing (schematic, not to scale). (A) Scales are flattened setae inserted in
# sockets in rows on the wing membrane, overlapping like roof tiles: large cover scales over smaller ground
# scales. (B) An individual scale: a stalk (pedicel) in its socket and a lamina whose upper surface bears
# longitudinal ridges joined by cross-ribs, with windows between them; the lower lamina is flat. Pigments
# (melanins, ommochromes, pterins) lie in the cuticle. (C) Cross-section of the upper lamina: the ridges are
# built of overlapping lamellae, alternating layers of cuticle and air, whose spacing produces structural
# colour by multilayer interference (7.17.23).
import numpy as np
from matplotlib.patches import Ellipse, Polygon, Rectangle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27, 10)


def scale_shape(x, y, w, h, angle=90.0, teeth=3):
    """Outline of a scale with a toothed distal margin, base at (x, y), pointing along angle (deg)."""
    pts = [(-0.12 * w, 0)]
    pts += [(-0.5 * w, 0.25 * h), (-0.5 * w, 0.92 * h)]
    for k in range(teeth):
        x0 = -0.5 * w + k * w / teeth
        pts += [(x0 + 0.5 * w / teeth, h), (x0 + w / teeth, 0.92 * h)]
    pts += [(0.5 * w, 0.25 * h), (0.12 * w, 0)]
    a = np.deg2rad(angle - 90)
    R = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
    return [tuple(np.array([x, y]) + R @ np.array(p)) for p in pts]


# (A) rows of scales
bio.panel(ax, "A", (0.2, 9.8))
bio.label(ax, (4.6, 9.6), "Scales on the wing membrane", size="normal", bold=True)
ax.add_patch(Rectangle((0.6, 1.2), 8.2, 7.6, facecolor=P.light("er"), edgecolor=P.edge("er"), lw=0.8, zorder=1))
for row in range(6):
    y = 1.5 + row * 1.1
    for k in range(8):
        x = 1.1 + k * 1.0 + (0.5 if row % 2 else 0)
        if x > 7.9:
            continue
        ax.add_patch(Polygon(scale_shape(x, y, 0.75, 1.05), closed=True, facecolor=P.fill("bone"),
                             edgecolor=P.edge("bone"), lw=0.5, zorder=3 + row))
        if row % 2 == 0:
            ax.add_patch(Polygon(scale_shape(x + 0.5, y + 0.1, 0.9, 1.45), closed=True,
                                 facecolor=P.fill("antibody"), edgecolor=P.edge("antibody"), lw=0.6, zorder=3 + row + 0.5))
bio.callout(ax, (3.6, 4.4), (2.0, 0.5), "cover scale", size="small")
bio.callout(ax, (6.1, 3.15), (6.6, 0.5), "ground scale", size="small")

# (B) a single scale
bio.panel(ax, "B", (9.6, 9.8))
bio.label(ax, (13.6, 9.6), "One scale", size="normal", bold=True)
sc = scale_shape(13.6, 1.4, 4.2, 7.4, teeth=4)
ax.add_patch(Polygon(sc, closed=True, facecolor=P.fill("antibody"), edgecolor=P.edge("antibody"), lw=0.9, zorder=3))
for k in range(9):
    x = 11.85 + k * 0.44
    ax.plot([x, x], [2.6, 8.4], color=P.edge("antibody"), lw=1.3, zorder=5)
for j in range(14):
    y = 2.8 + j * 0.41
    ax.plot([11.85, 15.37], [y, y], color=P.edge("antibody"), lw=0.4, zorder=4)
ax.add_patch(Ellipse((13.6, 1.25), 0.9, 0.45, facecolor=P.fill("bone"), edgecolor=P.edge("bone"), lw=0.8, zorder=6))
bio.callout(ax, (13.37, 6.0), (17.4, 8.6), "longitudinal ridge", size="small")
bio.callout(ax, (14.0, 4.85), (17.4, 6.6), "cross-rib", size="small")
bio.callout(ax, (14.5, 3.6), (17.4, 4.6), "window", size="small")
bio.callout(ax, (13.6, 1.25), (17.4, 1.2), "pedicel in socket", size="small")

# (C) cross-section of ridges
bio.panel(ax, "C", (19.6, 9.8))
bio.label(ax, (23.2, 9.6), "Ridges in cross-section", size="normal", bold=True)
ax.add_patch(Rectangle((19.8, 2.0), 7.0, 0.35, facecolor=P.fill("antibody"), edgecolor=P.edge("antibody"), lw=0.8, zorder=3))
for r in range(3):
    xc = 21.0 + r * 2.3
    ax.plot([xc - 0.15, xc - 0.15], [2.35, 3.0], color=P.edge("antibody"), lw=1.0, zorder=4)
    ax.plot([xc + 0.15, xc + 0.15], [2.35, 3.0], color=P.edge("antibody"), lw=1.0, zorder=4)
    for L in range(6):
        y = 3.0 + L * 0.75
        ax.add_patch(Polygon([(xc - 0.9, y + 0.25), (xc + 0.9, y), (xc + 0.9, y + 0.18), (xc - 0.9, y + 0.43)], closed=True,
                             facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.6, zorder=5))
bio.callout(ax, (21.9, 4.6), (24.6, 8.4), "lamellae: cuticle layers\nseparated by air", size="small")
bio.callout(ax, (23.3, 2.17), (24.2, 1.0), "lamina (scale body)", size="small")
bio.label(ax, (26.8, 0.15), "Schematic; not to scale", size="tiny", color=P.muted(), ha="right")
