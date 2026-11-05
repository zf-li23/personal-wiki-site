"""Dinoflagellate cell structure (schematic). A: ventral view of an armoured dinokont (Peridinium type): epitheca
and hypotheca made of thecal plates, the girdle (cingulum) round the cell with the ribbon-like transverse
flagellum, the sulcus on the ventral hypotheca with the longitudinal flagellum trailing behind. B: side view
showing the plate series (apical, precingular, cingular, postcingular, antapical). C: desmokont (Prorocentrum
type): two valves, two flagella from the anterior end. D: Ceratium with an apical horn and two antapical horns."""
import numpy as np
from matplotlib.patches import Ellipse, Polygon, PathPatch
from matplotlib.path import Path
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(32, 13)
D = "highlight"


def wave(p0, ang, L, amp=0.15, waves=2.5, lw=1.5):
    t = np.linspace(0, 1, 120)
    a = np.radians(ang)
    u, n = np.array([np.cos(a), np.sin(a)]), np.array([-np.sin(a), np.cos(a)])
    pts = p0 + np.outer(t * L, u) + np.outer(amp * np.sin(2 * np.pi * waves * t) * np.minimum(1, 5 * t), n)
    ax.plot(pts[:, 0], pts[:, 1], color=P.ink(), lw=lw, zorder=9)


def outline(cx, cy, rx, ry, k=100):
    t = np.linspace(0, 2 * np.pi, k)
    return np.c_[cx + rx * np.cos(t), cy + ry * np.sin(t)]


# A ventral view
bio.panel(ax, "A", (0.2, 12.8))
cx, cy = 5.2, 6.4
ax.add_patch(Ellipse((cx, cy), 5.6, 7.4, facecolor=P.light(D), edgecolor=P.edge(D), lw=1.4, zorder=3))
# plates: polygonal lines (Voronoi-like) on epitheca and hypotheca
rng = np.random.default_rng(1)
for yy, n in ((cy + 2.4, 4), (cy + 1.1, 6), (cy - 1.1, 5), (cy - 2.6, 2)):
    xs = np.linspace(cx - 2.6, cx + 2.6, n + 1)[1:-1]
    for x in xs:
        dy = 0.9
        ax.plot([x, x + rng.uniform(-0.2, 0.2)], [yy - dy, yy + dy], color=P.edge(D), lw=0.8, zorder=4)
for yy in (cy + 1.8, cy - 1.9):
    ax.plot([cx - 2.5, cx + 2.5], [yy, yy + 0.05], color=P.edge(D), lw=0.8, zorder=4)
# girdle
ax.add_patch(Polygon([[cx - 2.8, cy + 0.35], [cx + 2.8, cy + 0.1], [cx + 2.8, cy - 0.45], [cx - 2.8, cy - 0.2]],
                     facecolor=P.fill(D), edgecolor=P.edge(D), lw=1.0, zorder=5))
# sulcus
ax.add_patch(Polygon([[cx - 0.35, cy - 0.2], [cx + 0.35, cy - 0.3], [cx + 0.25, cy - 3.0], [cx - 0.25, cy - 3.0]],
                     facecolor=P.fill(D), edgecolor=P.edge(D), lw=1.0, zorder=5))
t = np.linspace(0, 1, 160)
xs = cx - 2.6 + 5.2 * t
ys = cy + 0.07 - 0.25 * t + 0.13 * np.sin(2 * np.pi * 10 * t)
ax.plot(xs, ys, color=P.ink(), lw=1.8, zorder=9)
wave(np.array([cx, cy - 0.5]), -90, 4.0)
bio.callout(ax, (cx + 1.5, cy + 2.6), (9.4, 10.6), "epitheca (plates)", size="tiny")
bio.callout(ax, (cx + 2.2, cy - 0.1), (9.4, 7.4), "girdle, transverse flagellum", size="tiny")
bio.callout(ax, (cx + 0.2, cy - 1.8), (9.4, 4.2), "sulcus", size="tiny")
bio.callout(ax, (cx + 1.6, cy - 2.4), (9.4, 2.6), "hypotheca", size="tiny")
bio.callout(ax, (cx + 0.1, cy - 4.2), (9.4, 1.0), "longitudinal flagellum", size="tiny")
bio.label(ax, (cx, 12.4), "ventral view", size="small", bold=True)

# B side view with plate series
bio.panel(ax, "B", (13.0, 12.8))
bx, by = 17.0, 6.6
ax.add_patch(Ellipse((bx, by), 4.4, 6.6, facecolor=P.light(D), edgecolor=P.edge(D), lw=1.4, zorder=3))
rows = [(by + 2.6, "apical"), (by + 1.3, "precingular"), (by, "cingular"), (by - 1.4, "postcingular"), (by - 2.6, "antapical")]
for yy, name in rows:
    w = 2.2 * np.sqrt(max(0.05, 1 - ((yy - by) / 3.3) ** 2))
    ax.plot([bx - w, bx + w], [yy - 0.55, yy - 0.55], color=P.edge(D), lw=0.8, zorder=4)
    bio.callout(ax, (bx + w * 0.6, yy), (bx + 3.4, yy), name, size="tiny")
ax.add_patch(Polygon([[bx - 2.2, by + 0.4], [bx + 2.2, by + 0.4], [bx + 2.2, by - 0.4], [bx - 2.2, by - 0.4]],
                     facecolor=P.fill(D), edgecolor="none", zorder=3.5, alpha=0.7))
bio.label(ax, (bx, 12.4), "plate series (Kofoid)", size="small", bold=True)

# C desmokont
bio.panel(ax, "C", (21.6, 12.8))
c2 = np.array([24.0, 5.6])
ax.add_patch(Ellipse(c2, 2.6, 3.8, facecolor=P.light(D), edgecolor=P.edge(D), lw=1.4, zorder=3))
ax.plot([c2[0], c2[0]], [c2[1] - 1.9, c2[1] + 1.9], color=P.edge(D), lw=1.0, zorder=4)
wave(c2 + np.array([0.0, 1.85]), 75, 2.8)
wave(c2 + np.array([0.1, 1.85]), 40, 2.4, amp=0.1, waves=4)
bio.label(ax, (24.0, 12.4), "desmokont", size="small", bold=True)
bio.label(ax, (24.0, 11.8), "Prorocentrum", size="tiny", italic=True, color=P.muted())
bio.label(ax, (24.0, 3.0), "two valves", size="tiny", color=P.muted())

# D Ceratium
bio.panel(ax, "D", (27.0, 12.8))
cxx, cyy = 29.6, 6.2
body = [[cxx - 1.0, cyy + 0.8], [cxx - 0.25, cyy + 1.2], [cxx - 0.1, cyy + 5.0], [cxx + 0.2, cyy + 5.0], [cxx + 0.5, cyy + 1.1],
        [cxx + 1.1, cyy + 0.6], [cxx + 1.0, cyy - 0.6], [cxx + 1.6, cyy - 3.6], [cxx + 1.3, cyy - 3.6], [cxx + 0.4, cyy - 1.2],
        [cxx - 0.3, cyy - 1.3], [cxx - 0.8, cyy - 4.4], [cxx - 1.1, cyy - 4.4], [cxx - 1.1, cyy - 0.8]]
ax.add_patch(Polygon(body, closed=True, facecolor=P.light(D), edgecolor=P.edge(D), lw=1.3, joinstyle="round", zorder=4))
ax.plot([cxx - 1.05, cxx + 1.05], [cyy + 0.1, cyy - 0.1], color=P.edge(D), lw=3, zorder=5)
bio.label(ax, (cxx + 1.3, cyy + 4.6), "apical horn", size="tiny", ha="left")
bio.label(ax, (cxx + 1.8, cyy - 3.2), "antapical\nhorns", size="tiny", ha="left")
bio.label(ax, (cxx, 12.4), "Ceratium", size="small", bold=True, italic=True)
