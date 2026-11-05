"""Haustorium of dodder (Cuscuta) in a host stem, schematic transverse section. Left: host stem with
epidermis, cortex, a ring of vascular bundles (phloem outside, xylem inside) and pith. Right: section of
the dodder stem coiled on the host. The dodder forms an adhesive disc on the host surface; the haustorium
grows through the host epidermis and cortex; its searching cells reach a vascular bundle, some
differentiating into vessel elements joined to the host xylem (blue), others contacting the host phloem
(orange).
"""
import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch, Wedge
from matplotlib.path import Path

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(24.0, 14.0)
sc = bio.smooth_closed
HC, R = np.array([8.0, 7.0]), 5.6
DODDER = "atp"


def patch(pts, tok, lw=0.9, z=6, fill=None, alpha=None):
    pts = np.asarray(pts, float)
    ax.add_patch(PathPatch(Path(np.vstack([pts, pts[:1]]), closed=True), facecolor=fill or P.fill(tok),
                           edgecolor=P.edge(tok), lw=lw, joinstyle="round", zorder=z, alpha=alpha))


# host stem
ax.add_patch(Circle(HC, R, facecolor=P.fill(B.tok("cortex")), edgecolor=P.edge(B.tok("epidermis")), lw=2.4, zorder=3))
ax.add_patch(Circle(HC, R - 0.25, facecolor="none", edgecolor=P.edge(B.tok("epidermis")), lw=0.6, zorder=4))
ax.add_patch(Circle(HC, 2.6, facecolor=P.fill(B.tok("pith")), edgecolor=P.edge(B.tok("pith")), lw=0.6, zorder=4))
bundles = []
for a in np.linspace(0, 2 * np.pi, 10, endpoint=False):
    c = HC + 3.4 * np.array([np.cos(a), np.sin(a)])
    d = np.degrees(a)
    ax.add_patch(Wedge(HC, 4.15, d - 10, d + 10, width=0.7, facecolor=P.fill("phloem"), edgecolor=P.edge("phloem"),
                       lw=0.7, zorder=5))
    ax.add_patch(Wedge(HC, 3.45, d - 10, d + 10, width=0.75, facecolor=P.fill("xylem"), edgecolor=P.edge("xylem"),
                       lw=0.7, zorder=5))
    bundles.append(a)

# dodder stem on the right, touching the host
DC, r = HC + np.array([R + 2.0, 0.0]), 2.1
ax.add_patch(Circle(DC, r, facecolor=P.fill(DODDER), edgecolor=P.edge(DODDER), lw=1.4, zorder=6))
for a in np.linspace(0, 2 * np.pi, 8, endpoint=False):  # small reduced vascular strands of the dodder
    p = DC + 1.2 * np.array([np.cos(a), np.sin(a)])
    ax.add_patch(Circle(p, 0.2, facecolor=P.fill("xylem"), edgecolor=P.edge("xylem"), lw=0.5, zorder=7))
# adhesive disc (upper haustorium) pressed on the host epidermis
disc = sc([(HC[0] + R + 0.55, HC[1] + 1.3), (HC[0] + R - 0.15, HC[1] + 0.8), (HC[0] + R - 0.25, HC[1]),
           (HC[0] + R - 0.15, HC[1] - 0.8), (HC[0] + R + 0.55, HC[1] - 1.3), (DC[0] - r + 0.3, HC[1])], n=120)
patch(disc, DODDER, z=7)
# haustorium wedge through the cortex to the bundle at angle 0
tip = HC + np.array([4.25, 0.0])
haus = sc([(HC[0] + R, HC[1] + 0.55), (HC[0] + 4.9, HC[1] + 0.35), (tip[0] - 0.05, HC[1] + 0.12),
           (tip[0] - 0.05, HC[1] - 0.12), (HC[0] + 4.9, HC[1] - 0.35), (HC[0] + R, HC[1] - 0.55)], n=120)
patch(haus, DODDER, z=8)
# searching cells into the bundle: xylic (to host xylem) and phloic (to host phloem)
for dy in (-0.15, 0.0, 0.15):
    ax.plot([tip[0], HC[0] + 2.95], [HC[1] + dy, HC[1] + dy * 2.0], color=P.edge("xylem"), lw=2.2, zorder=9)
for s in (-1, 1):
    ax.plot([tip[0] + 0.05, HC[0] + 3.85, HC[0] + 3.75], [HC[1] + s * 0.1, HC[1] + s * 0.45, HC[1] + s * 0.62],
            color=P.edge("phloem"), lw=2.0, zorder=9)
ax.plot([HC[0] + R + 0.2, DC[0] - 1.0], [HC[1], HC[1]], color=P.edge("xylem"), lw=2.2, zorder=9)

def pol(ang, rad):
    t = np.radians(ang)
    return (HC[0] + rad * np.cos(t), HC[1] + rad * np.sin(t))


items = [(pol(160, R - 0.05), "Host epidermis"), (pol(170, 4.8), "Host cortex"), (pol(180, 3.8), "Host phloem"),
         (pol(186, 3.1), "Host xylem"), (pol(205, 1.5), "Pith")]
for k, (p, t) in enumerate(items):
    bio.callout(ax, p, (0.4, 10.0 - 1.4 * k), t)
bio.callout(ax, (HC[0] + 3.2, HC[1] + 0.15), (13.0, 12.6), "Xylic connection")
bio.callout(ax, (HC[0] + 3.8, HC[1] - 0.55), (13.0, 1.2), "Phloic connection")
bio.callout(ax, (HC[0] + 5.0, HC[1] - 0.3), (16.0, 2.4), "Haustorium")
bio.callout(ax, (HC[0] + R + 0.4, HC[1] + 1.1), (16.5, 12.0), "Adhesive disc")
bio.callout(ax, (DC[0] + 1.3, DC[1] + 1.4), (20.0, 11.0), "Dodder stem")
bio.label(ax, (HC[0], 0.6), "Host stem", size="normal", bold=True)
bio.label(ax, (DC[0], 0.6), "Cuscuta", size="normal", bold=True, italic=True)
