"""Clonal analysis and compartments in the Drosophila wing (schematic adult wings, anterior up, distal right).

A: clones induced by mitotic recombination early in larval life (marked, e.g., multiple wing hairs) are long and
irregular but never cross the anterior-posterior compartment boundary, which does not coincide with any vein.
B: the Minute technique: a marked clone that is wild type for Minute (M+/M+) in a slowly growing M/+ background grows
faster and can fill most of its compartment, but still stops exactly at the boundary. C: clones induced before
the boundary forms can span both compartments; induced after, they respect it: the time of clonal restriction.
"""

import numpy as np
import wikibio as bio
from matplotlib.patches import PathPatch
from matplotlib.path import Path

P = bio.P
rng = np.random.default_rng(4)
fig, ax = bio.canvas(30.0, 8.6)


def wing(cx, cy, L=7.4, H=3.0):
    pts = [(cx - L / 2, cy + 0.05 * H), (cx - 0.25 * L, cy + 0.42 * H), (cx + 0.15 * L, cy + 0.52 * H), (cx + 0.45 * L, cy + 0.3 * H),
           (cx + 0.5 * L, cy - 0.02 * H), (cx + 0.38 * L, cy - 0.42 * H), (cx, cy - 0.5 * H), (cx - 0.33 * L, cy - 0.3 * H)]
    out = bio.smooth_closed(np.array(pts), 240)
    p = PathPatch(Path(out, closed=True), facecolor=P.mix(P.fill("neutral"), P.surface(), 0.7), edgecolor=P.edge("neutral"), lw=1.0, zorder=3)
    ax.add_patch(p)
    # AP boundary: a gently curved line from the hinge to the distal margin, slightly anterior of the L4 vein
    xb = np.linspace(cx - L / 2, cx + L / 2, 50)
    yb = cy - 0.02 * H + 0.06 * H * np.sin(np.linspace(0, np.pi, 50))
    ln = ax.plot(xb, yb, color=P.ink(), lw=1.0, ls=(0, (4, 2)), zorder=6)[0]
    ln.set_clip_path(p)
    for f in (0.28, 0.12, -0.2, -0.33):   # veins (schematic)
        yv = cy + f * H
        v = ax.plot([cx - 0.4 * L, cx + 0.47 * L], [yv * 0.0 + cy + f * 0.6 * H, yv], color=P.edge("neutral"), lw=0.6, zorder=4)[0]
        v.set_clip_path(p)
    return p, (xb, yb)


def clone(p, bnd, x0, y0, n, step, side, tok, z=5):
    xb, yb = bnd
    pts = [(x0, y0)]
    for _ in range(n):
        x, y = pts[-1]
        nx_, ny_ = x + step * rng.normal(0.8, 0.5), y + step * rng.normal(0, 0.6)
        yl = np.interp(nx_, xb, yb)
        if side > 0:
            ny_ = max(ny_, yl + 0.06)
        else:
            ny_ = min(ny_, yl - 0.06)
        pts.append((nx_, ny_))
    for (x, y) in pts:
        c = __import__("matplotlib").patches.Circle((x, y), step * 0.9, facecolor=P.fill(tok), edgecolor="none", zorder=z)
        c.set_clip_path(p)
        ax.add_patch(c)


bio.panel(ax, "A", (0.2, 8.4))
p, bnd = wing(4.6, 4.6)
clone(p, bnd, 1.6, 5.2, 18, 0.22, +1, "protein")
clone(p, bnd, 2.2, 3.6, 16, 0.22, -1, "drug")
clone(p, bnd, 4.0, 5.6, 12, 0.2, +1, "channel")
bio.label(ax, (4.6, 7.6), "Clones respect the AP boundary", size="small", bold=True)
bio.label(ax, (8.6, 6.0), "A", size="small", bold=True)
bio.label(ax, (8.6, 3.0), "P", size="small", bold=True)

bio.panel(ax, "B", (10.0, 8.4))
p, bnd = wing(14.4, 4.6)
for k in range(6):
    clone(p, bnd, 11.2 + 0.2 * k, 4.9 + 0.25 * k, 40, 0.3, +1, "protein")
bio.label(ax, (14.4, 7.6), "Minute⁺ clone fills its compartment", size="small", bold=True)

bio.panel(ax, "C", (19.8, 8.4))
p, bnd = wing(24.2, 4.6)
clone(p, bnd, 21.0, 5.0, 20, 0.22, +1, "drug")
clone(p, bnd, 21.4, 4.1, 18, 0.22, -1, "drug")
c2y = np.linspace(5.6, 3.4, 14)
for k, y in enumerate(c2y):
    c = __import__("matplotlib").patches.Circle((22.6 + 0.12 * k, y), 0.22, facecolor=P.fill("highlight"), edgecolor="none", zorder=5)
    c.set_clip_path(p)
    ax.add_patch(c)
bio.label(ax, (24.2, 7.6), "Early clone crosses; later ones do not", size="small", bold=True)
bio.label(ax, (24.2, 1.2), "yellow: induced in the embryo; red: induced in the larva", size="tiny", color=P.muted())
