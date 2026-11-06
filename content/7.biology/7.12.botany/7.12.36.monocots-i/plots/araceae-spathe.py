# Araceae inflorescences and duckweeds (schematic). A: Arisaema-type spathe and spadix in longitudinal
# section: the tubular lower part of the spathe encloses the spadix, the limb arches over it; female
# flowers at the base, a zone of sterile (neuter) flowers, male flowers above, and a sterile appendix.
# B: Zantedeschia (calla): a white funnel-shaped spathe and an erect yellow spadix. C: three duckweed
# genera to scale: Spirodela (several roots), Lemna (one root), Wolffia (rootless, about 1 mm).
import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch, Polygon
from matplotlib.path import Path
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(31, 14)


def poly(pts, token, z=5, light=False):
    ax.add_patch(Polygon(np.asarray(pts), closed=True, facecolor=P.light(token) if light else P.fill(token),
                         edgecolor=P.edge(token), lw=1.3, joinstyle="round", zorder=z))


# ---------------- A: Arisaema type, longitudinal section
bio.panel(ax, "A", (0.3, 13.6))
bio.label(ax, (4.6, 13.5), r"$\it{Arisaema}$ type (section)", size="title")
cx = 4.0
t = np.linspace(0, 1, 40)
left = [(cx - 1.25 - 0.15 * np.sin(np.pi * s), 1.2 + 7.0 * s) for s in t]
hood = [(cx - 1.4 + 4.6 * s, 8.2 + 3.4 * np.sin(np.pi * s * 0.9) - 0.6 * s) for s in t]
right = [(cx + 1.25 + 0.1 * np.sin(np.pi * s), 8.0 - 6.8 * s) for s in t]
outer = left + hood + [(cx + 3.3, 9.0), (cx + 2.6, 9.4)] + [(cx + 1.45, 8.3)] + right[1:]
inner = [(x + 0.22 if i < 40 else x, y) for i, (x, y) in enumerate(left)]
poly(outer, "plant", z=3)
poly([(cx - 1.0, 1.4), (cx - 1.05, 7.9), (cx + 1.05, 7.9), (cx + 1.0, 1.4)], "plant", z=4, light=True)
# spadix axis
ax.add_patch(PathPatch(Path([(cx - 0.18, 1.3), (cx - 0.18, 6.8), (cx + 0.18, 6.8), (cx + 0.18, 1.3)]),
                       facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=1.0, zorder=6))
for y in np.arange(1.7, 3.8, 0.42):
    for s in (-1, 1):
        ax.add_patch(Circle((cx + s * 0.45, y), 0.24, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=0.9, zorder=7))
for y in np.arange(4.0, 4.7, 0.3):
    for s in (-1, 1):
        ax.add_patch(Circle((cx + s * 0.32, y), 0.08, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.7, zorder=7))
for y in np.arange(5.0, 6.8, 0.3):
    for s in (-1, 1):
        ax.add_patch(Ellipse((cx + s * 0.4, y), 0.36, 0.22, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.8, zorder=7))
app = [(cx - 0.18, 6.8)] + [(cx - 0.18 - 0.25 * np.sin(np.pi * s), 6.8 + 3.0 * s) for s in t] + \
      [(cx + 0.18 + 0.25 * np.sin(np.pi * s), 9.8 - 3.0 * s) for s in t]
poly(app, "tepal", z=6)
bio.callout(ax, (cx + 2.4, 10.6), (cx + 4.0, 12.4), "Spathe limb")
bio.callout(ax, (cx + 1.3, 3.0), (cx + 3.4, 1.4), "Spathe tube")
bio.callout(ax, (cx + 0.2, 9.0), (cx + 4.0, 8.0), "Appendix (sterile)")
bio.callout(ax, (cx + 0.55, 6.0), (cx + 4.0, 6.4), "Male flowers")
bio.callout(ax, (cx + 0.35, 4.3), (cx + 4.0, 4.8), "Neuter flowers")
bio.callout(ax, (cx + 0.65, 2.6), (cx + 4.0, 3.2), "Female flowers")

# ---------------- B: Zantedeschia
bio.panel(ax, "B", (11.0, 13.6))
bio.label(ax, (14.6, 13.5), r"$\it{Zantedeschia}$", size="title")
bx = 14.6
ax.plot([bx, bx], [0.8, 4.0], color=P.edge("plant"), lw=4, solid_capstyle="round", zorder=3)
sp = [(bx - 0.4, 4.0), (bx - 1.6, 7.0), (bx - 2.6, 10.0), (bx - 1.8, 11.4), (bx - 0.2, 11.9), (bx + 1.4, 12.6),
      (bx + 2.6, 11.6), (bx + 2.2, 9.6), (bx + 1.4, 7.0), (bx + 0.4, 4.0)]
from wikibio.core import smooth_closed
ax.add_patch(PathPatch(Path(smooth_closed(sp, n=200), closed=True), facecolor=P.light("neutral"),
                       edgecolor=P.edge("neutral"), lw=1.4, zorder=4))
ax.add_patch(Ellipse((bx + 0.05, 7.4), 0.55, 4.4, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=1.0, zorder=6))
bio.callout(ax, (bx + 1.8, 10.2), (bx + 2.6, 13.0), "Spathe")
bio.callout(ax, (bx + 0.2, 8.6), (bx + 3.0, 7.4), "Spadix")

# ---------------- C: duckweeds to scale
bio.panel(ax, "C", (19.6, 13.6))
bio.label(ax, (25.2, 13.5), "Duckweeds (same scale)", size="title")
mm = 0.5
ax.plot([20.2, 30.6], [9.0, 9.0], color=P.edge("extracellular"), lw=1.0, ls=(0, (5, 3)), zorder=2)
bio.label(ax, (30.8, 9.75), "Water surface", size="tiny", ha="right")
# Spirodela
sx = 22.6
ax.add_patch(Ellipse((sx, 9.1), 7 * mm, 4.6 * mm, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.2, zorder=6))
for k, dx in enumerate(np.linspace(-0.7, 0.7, 7)):
    ax.plot([sx + dx * 0.4, sx + dx], [8.9, 8.9 - 3.0 - 0.3 * (k % 3)], color=P.edge("plant"), lw=0.9, zorder=5)
bio.label(ax, (sx, 4.6), r"$\it{Spirodela}$", size="small")
bio.label(ax, (sx, 3.9), "many roots", size="tiny")
# Lemna
lx = 26.0
ax.add_patch(Ellipse((lx, 9.1), 3.2 * mm, 2.2 * mm, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.2, zorder=6))
ax.plot([lx, lx + 0.1], [9.0, 5.6], color=P.edge("plant"), lw=0.9, zorder=5)
bio.label(ax, (lx, 4.6), r"$\it{Lemna}$", size="small")
bio.label(ax, (lx, 3.9), "one root", size="tiny")
# Wolffia
wx = 29.2
ax.add_patch(Ellipse((wx, 9.05), 0.9 * mm, 0.65 * mm, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=6))
bio.label(ax, (wx, 4.6), r"$\it{Wolffia}$", size="small")
bio.label(ax, (wx, 3.9), "rootless, ~1 mm", size="tiny")
bio.scale_bar(ax, (21.0, 2.2), 2 * mm, "2 mm")
