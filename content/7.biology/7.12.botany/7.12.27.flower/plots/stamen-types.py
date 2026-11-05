# Stamen types. A: by connation and relative length: monadelphous (filaments fused into one tube),
# diadelphous (9 fused + 1 free), polyadelphous (several bundles), syngenesious (anthers fused into a
# tube, filaments free), didynamous (2 long + 2 short) and tetradynamous (4 long + 2 short).
# B: attachment of the anther to the filament: basifixed, dorsifixed and versatile (attached at one
# point of the back, the anther can swing). C: anther dehiscence: longitudinal slits, transverse slits,
# apical pores (poricidal) and valves (flaps lifting upwards).
import numpy as np
from matplotlib.patches import Ellipse, Polygon, FancyBboxPatch
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(23.0, 13.0)
FC, EC = P.fill("anther"), P.edge("anther")
FIL = P.edge("stem") if "stem" in P.TOKENS else P.edge("plant")


def anther(x, y, w=0.32, h=0.6, angle=0, z=8):
    ax.add_patch(Ellipse((x, y), w, h, angle=angle, facecolor=FC, edgecolor=EC, lw=1.0, zorder=z))


def filament(p, q, lw=1.6, z=6):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=FIL, lw=lw, solid_capstyle="round", zorder=z)


bio.panel(ax, "A", (0.2, 12.8))
bio.label(ax, (11.0, 12.6), "Connation and length of stamens", size="normal", bold=True)
base_y, top = 7.2, 11.2
# monadelphous
cx = 1.9
ax.add_patch(FancyBboxPatch((cx - 0.45, base_y), 0.9, 2.6, boxstyle="round,pad=0,rounding_size=0.15",
                            facecolor=P.light("anther"), edgecolor=FIL, lw=1.2, zorder=5))
for dx in np.linspace(-0.4, 0.4, 5):
    filament((cx + dx * 0.9, base_y + 2.6), (cx + dx * 2.2, top - 0.3))
    anther(cx + dx * 2.2, top)
# diadelphous
cx = 5.6
ax.add_patch(FancyBboxPatch((cx - 0.55, base_y), 0.9, 2.4, boxstyle="round,pad=0,rounding_size=0.15",
                            facecolor=P.light("anther"), edgecolor=FIL, lw=1.2, zorder=5))
for dx in np.linspace(-0.5, 0.3, 9):
    filament((cx + dx, base_y + 2.4), (cx + dx * 1.8 - 0.1, top - 0.3))
    anther(cx + dx * 1.8 - 0.1, top, w=0.22, h=0.45)
filament((cx + 0.75, base_y), (cx + 0.95, top - 0.3))
anther(cx + 0.95, top, w=0.22, h=0.45)
# polyadelphous
cx = 9.4
for k, ang in enumerate((-0.9, 0.0, 0.9)):
    b = (cx + ang * 0.35, base_y)
    m = (cx + ang * 0.9, base_y + 1.6)
    filament(b, m, lw=3.2)
    for t in (-0.35, 0.0, 0.35):
        e = (m[0] + t + ang * 0.4, top - 0.3)
        filament(m, e)
        anther(e[0], top, w=0.22, h=0.45)
# syngenesious
cx = 13.2
for dx in np.linspace(-0.6, 0.6, 5):
    filament((cx + dx * 1.2, base_y), (cx + dx * 0.75, top - 1.6))
ax.add_patch(FancyBboxPatch((cx - 0.6, top - 1.7), 1.2, 1.9, boxstyle="round,pad=0,rounding_size=0.2",
                            facecolor=FC, edgecolor=EC, lw=1.0, zorder=8))
for dx in np.linspace(-0.3, 0.3, 3):
    ax.plot([cx + dx, cx + dx], [top - 1.6, top + 0.1], color=EC, lw=0.7, zorder=9)
# didynamous
cx = 17.0
for dx, h in ((-0.8, 3.9), (-0.3, 2.7), (0.3, 2.7), (0.8, 3.9)):
    filament((cx + dx * 0.4, base_y), (cx + dx, base_y + h))
    anther(cx + dx, base_y + h + 0.3)
# tetradynamous
cx = 20.8
for dx, h in ((-1.0, 2.5), (-0.45, 3.9), (-0.15, 3.9), (0.15, 3.9), (0.45, 3.9), (1.0, 2.5)):
    filament((cx + dx * 0.35, base_y), (cx + dx, base_y + h))
    anther(cx + dx, base_y + h + 0.3, w=0.24, h=0.5)
for cx, name, note in ((1.9, "Monadelphous", "one bundle"), (5.6, "Diadelphous", "(9) + 1"),
                       (9.4, "Polyadelphous", "several bundles"), (13.2, "Syngenesious", "anthers fused"),
                       (17.0, "Didynamous", "2 long + 2 short"), (20.8, "Tetradynamous", "4 long + 2 short")):
    bio.label(ax, (cx, 6.6), name, size="small", bold=True)
    bio.label(ax, (cx, 6.1), note, size="tiny", color=P.muted())

bio.panel(ax, "B", (0.2, 5.4))
bio.label(ax, (5.4, 5.2), "Anther attachment", size="normal", bold=True)
y0 = 1.3
filament((1.6, y0), (1.6, y0 + 2.0))
anther(1.6, y0 + 2.6, w=0.55, h=1.2)
filament((5.0, y0), (5.0, y0 + 2.4))
anther(5.25, y0 + 2.5, w=0.55, h=1.6)
ax.plot([5.0, 5.0], [y0 + 1.9, y0 + 3.1], color=FIL, lw=1.6, zorder=9)
filament((8.6, y0), (8.6, y0 + 2.5))
anther(8.6, y0 + 2.75, w=0.5, h=1.6, angle=-62)
ax.add_patch(Ellipse((8.6, y0 + 2.6), 0.14, 0.14, facecolor=FIL, edgecolor=FIL, zorder=10))
for x, n in ((1.6, "Basifixed"), (5.0, "Dorsifixed"), (8.6, "Versatile")):
    bio.label(ax, (x, 0.6), n, size="small", bold=True)

bio.panel(ax, "C", (11.6, 5.4))
bio.label(ax, (17.6, 5.2), "Anther dehiscence", size="normal", bold=True)
y = 3.1
for k, (name, kind) in enumerate((("Longitudinal", "long"), ("Transverse", "trans"), ("Poricidal", "pore"),
                                  ("Valvular", "valve"))):
    x = 13.2 + 3.4 * k
    filament((x, 1.2), (x, y - 1.0))
    ax.add_patch(Ellipse((x - 0.33, y), 0.62, 1.9, facecolor=FC, edgecolor=EC, lw=1.0, zorder=8))
    ax.add_patch(Ellipse((x + 0.33, y), 0.62, 1.9, facecolor=FC, edgecolor=EC, lw=1.0, zorder=8))
    ink = P.ink()
    if kind == "long":
        for s in (-0.33, 0.33):
            ax.plot([x + s, x + s], [y - 0.75, y + 0.75], color=ink, lw=1.4, zorder=9)
    elif kind == "trans":
        for s in (-0.33, 0.33):
            ax.plot([x + s - 0.22, x + s + 0.22], [y, y], color=ink, lw=1.4, zorder=9)
    elif kind == "pore":
        for s in (-0.33, 0.33):
            ax.add_patch(Ellipse((x + s, y + 0.8), 0.18, 0.14, facecolor=ink, edgecolor=ink, zorder=9))
    else:
        for s in (-0.33, 0.33):
            ax.add_patch(Polygon([(x + s - 0.2, y + 0.1), (x + s + 0.2, y + 0.1), (x + s + 0.28, y + 0.85),
                                  (x + s - 0.28, y + 0.85)], closed=True, facecolor=P.light("anther"),
                                 edgecolor=ink, lw=1.0, zorder=9))
    bio.label(ax, (x, 0.6), name, size="small", bold=True)
