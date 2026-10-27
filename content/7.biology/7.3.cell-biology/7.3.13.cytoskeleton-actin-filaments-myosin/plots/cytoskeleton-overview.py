"""The three filament systems in a crawling fibroblast (schematic, top view) and the three filaments to scale.

A: actin (red) forms the dendritic network of the lamellipodium at the leading edge, bundles in filopodia,
contractile stress fibres ending in focal adhesions and a thin cortex under the whole membrane; microtubules
(blue) radiate from the centrosome, which sits between the nucleus and the leading edge; intermediate
filaments (green) form a cage around the nucleus and extend towards the cell periphery.
B: an actin filament (about 7 nm), a microtubule (25 nm) and an intermediate filament (10 nm), all at the
same scale (100 nm segments).
"""

import math

import numpy as np
from matplotlib.path import Path

from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Rectangle

import wikibio as bio
from wikibio import cytoskel as C

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(25, 11.5)

# ---- A: the cell --------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 11.4))
ctrl = [(1.2, 5.2), (2.2, 4.4), (4.5, 3.4), (7.5, 2.1), (10.2, 1.5), (12.4, 2.6), (13.4, 5.3), (12.6, 8.4),
        (10.3, 9.6), (7.4, 8.9), (4.6, 7.2), (2.2, 6.1)]
outline = bio.smooth_closed(ctrl, n=400)
bio.membrane(ax, outline, "cytoplasm", zorder=2)
path = Path(outline)
cen = np.array([7.6, 5.4])


def inside(p, margin=0.0):
    return path.contains_point(p, radius=-margin) if margin else path.contains_point(p)


def ray_end(p, d, margin=0.25, step=0.05, maxlen=10):
    q = np.array(p, float)
    for _ in range(int(maxlen / step)):
        nq = q + d * step
        if not path.contains_point(nq) or not path.contains_point(nq + d * margin):
            break
        q = nq
    return q


# leading edge: the right-hand arc of the outline
pts = outline[:-1]
front = [(i, p) for i, p in enumerate(pts) if p[0] > 9.6 and (p[0] - 8.0) ** 2 + (p[1] - 5.4) ** 2 > 9]
for i, p in front[::3]:
    j = (i + 1) % len(pts)
    t = pts[j] - pts[i - 1]
    t = t / np.linalg.norm(t)
    nrm = np.array([t[1], -t[0]])  # outward for counter-clockwise outline
    if not path.contains_point(p - nrm * 0.3):
        nrm = -nrm
    for k in range(3):
        ang = math.radians(rng.choice([-35, 35]) + rng.uniform(-8, 8))
        d = nrm * math.cos(ang) + np.array([-nrm[1], nrm[0]]) * math.sin(ang)
        tip = p - nrm * rng.uniform(0.05, 0.15)
        base = tip - d * rng.uniform(0.35, 0.9)
        ax.plot([base[0], tip[0]], [base[1], tip[1]], color=P.edge("actin"), lw=0.8, zorder=6)
# filopodia
for i, p in front[10::22]:
    t = pts[(i + 1) % len(pts)] - pts[i - 1]
    t = t / np.linalg.norm(t)
    nrm = np.array([t[1], -t[0]])
    if not path.contains_point(p - nrm * 0.3):
        nrm = -nrm
    C.filopodium(ax, p - nrm * 0.45, length=1.2, width=0.22, angle=math.degrees(math.atan2(nrm[1], nrm[0])), n=3,
                 fascin=False, tip=False, lw=0.8, zorder=3)
# cortex
q, nrm, _ = bio.polyline(outline, n=500, closed=True)
inner = []
for p, nn in zip(q, nrm):
    s = p - nn * 0.18 if path.contains_point(p - nn * 0.18) else p + nn * 0.18
    inner.append(s)
inner = np.array(inner)
ax.plot(inner[:, 0], inner[:, 1], color=P.edge("actin"), lw=1.0, zorder=5)
# stress fibres with focal adhesions
for a, b in (((2.6, 4.9), (10.6, 2.4)), ((2.6, 5.6), (11.0, 8.6)), ((3.8, 4.5), (12.0, 4.0)), ((4.2, 6.6), (12.2, 6.9))):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge("actin"), lw=2.2, solid_capstyle="round", zorder=4)
    for e in (a, b):
        ax.add_patch(Circle(e, 0.17, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.7, zorder=4.5))
# nucleus and intermediate filaments
nuc = bio.nucleus(ax, (5.8, 5.4), 1.25, nucleolus=True, zorder=7)
for k in range(9):
    th = 2 * math.pi * k / 9 + 0.2
    p0 = np.array([5.8, 5.4]) + 1.3 * np.array([math.cos(th), math.sin(th)])
    d = np.array([math.cos(th + 0.4), math.sin(th + 0.4)])
    end = ray_end(p0, d, margin=0.5, maxlen=4)
    s = np.linspace(0, 1, 40)[:, None]
    wig = np.sin(s * 9 + k) * 0.12
    line = p0 + (end - p0) * s + np.c_[-d[1], d[0]] * wig
    ax.plot(line[:, 0], line[:, 1], color=P.edge(C.tok("if")), lw=1.1, zorder=6.5)
th = np.linspace(0, 2 * math.pi, 120)
ax.plot(5.8 + 1.38 * np.cos(th), 5.4 + 1.27 * np.sin(th), color=P.edge(C.tok("if")), lw=1.1, zorder=6.6)
# centrosome and microtubules
csm = np.array([7.8, 5.6])
for k, an in enumerate(np.linspace(0, 360, 26, endpoint=False) + 4):
    d = np.array([math.cos(math.radians(an)), math.sin(math.radians(an))])
    s = csm + d * 0.3
    # microtubules bend around the nucleus: skip rays that hit it
    if np.linalg.norm(s + d * 1.2 - np.array([5.8, 5.4])) < 1.6:
        continue
    e = ray_end(s, d, margin=0.2, maxlen=8)
    if np.linalg.norm(e - s) < 0.6:
        continue
    C.mt_line(ax, s, e, lw=1.0, plus=True, zorder=8)
C.centrosome(ax, csm, size=0.3, microtubules=0, centrioles=False, zorder=9)
# labels
bio.callout(ax, (12.95, 5.3), (14.2, 10.8), "Lamellipodium", size="tiny")
bio.callout(ax, (13.3, 6.9), (14.2, 10.2), "Filopodium", size="tiny")
bio.callout(ax, (6.0, 3.85), (5.6, 0.6), "Stress fibre", size="tiny")
bio.callout(ax, (10.6, 2.4), (12.4, 0.6), "Focal adhesion", size="tiny")
bio.callout(ax, (2.0, 5.2), (0.4, 2.6), "Cortex", size="tiny")
bio.callout(ax, (7.8, 5.45), (9.6, 0.6), "Centrosome", size="tiny")
bio.callout(ax, (4.7, 6.7), (3.6, 9.6), "Intermediate filaments", size="tiny")
bio.callout(ax, (10.0, 7.6), (11.6, 10.8), "Microtubule", size="tiny")
bio.label(ax, (5.8, 4.0), "Nucleus", size="tiny", color=P.on_fill(), zorder=12)
bio.arrow(ax, (13.4, 3.3), (14.5, 3.0), kind="process")
bio.label(ax, (13.6, 2.4), "direction of\nmigration", size="tiny", ha="left")

# ---- B: filaments to scale (0.1 unit per nm) --------------------------------------------------------
bio.panel(ax, "B", (15.3, 11.4))
x0, x1 = 15.9, 25.0 - 0.6
C.actin_filament(ax, (x0, 9.6), (x1, 9.6), r=0.23, ends=True)
bio.label(ax, (x0, 10.6), "Actin filament: ~7 nm, two strands of G-actin (ATP/ADP)", size="tiny", ha="left")
C.microtubule_lattice(ax, (x0, 6.1), (x1, 6.1), width=2.5, rows=7, cap=0.0, plus_end="blunt", ends=True,
                      dimer=0.8)
bio.label(ax, (x0, 7.75), "Microtubule: 25 nm, 13 protofilaments of αβ-tubulin (GTP/GDP)", size="tiny", ha="left")
C.if_filament(ax, (x0, 2.7), (x1, 2.7), width=1.0, strands=4)
bio.label(ax, (x0, 3.75), "Intermediate filament: ~10 nm, rope of fibrous subunits (no NTP, no polarity)",
          size="tiny", ha="left")
bio.scale_bar(ax, (x0, 1.0), 5.0, "50 nm")
