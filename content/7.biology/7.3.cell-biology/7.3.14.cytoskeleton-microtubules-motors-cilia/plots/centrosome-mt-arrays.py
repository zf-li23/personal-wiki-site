"""Microtubule-organizing centres and the arrangement of microtubules in different cells (schematic).

A: the centrosome of an animal cell: a mother and a daughter centriole at right angles in a cloud of
pericentriolar material containing gamma-tubulin ring complexes (gold dots); microtubules grow from it with
their minus ends in the PCM and their plus ends (dots) outward.
B: a centriole in cross-section: nine triplet microtubules (A, B and C tubules, A innermost) around a
cartwheel whose hub is a ring of SAS-6 dimers; a basal body has the same structure.
C: microtubule arrays (plus ends marked): a fibroblast (radial, from the centrosome), a columnar epithelial
cell (bundles from apical non-centrosomal sites, minus ends apical), a neuron (axon: uniformly plus end out;
mammalian dendrites: mixed), and a plant cell (cortical array parallel to the cellulose microfibrils,
nucleated on the cortex and the nuclear envelope; no centrosome).
"""

import math

import numpy as np

import wikibio as bio
from wikibio import cytoskel as C

P = bio.P
fig, ax = bio.canvas(26.0, 11.0)

bio.panel(ax, "A", (0.1, 10.9))
cs = C.centrosome(ax, (3.6, 6.9), size=1.0, microtubules=18, length=2.6, lw=1.3)
bio.callout(ax, (3.45, 7.3), (0.3, 10.2), "mother and daughter centrioles", size="tiny")
bio.callout(ax, (4.3, 6.3), (6.4, 3.8), "pericentriolar material (γ-TuRCs)", size="tiny")

bio.panel(ax, "B", (8.0, 10.9))
As = C.centriole_section(ax, (10.6, 7.3), 2.0)
bio.callout(ax, As[0] + (0.05, 0.0), (12.9, 10.3), "triplet: A, B, C tubules", size="tiny")
bio.callout(ax, (10.6, 7.3), (13.4, 4.9), "cartwheel hub (SAS-6 ring)", size="tiny")
bio.label(ax, (10.6, 4.75), "~250 nm", size="tiny", color=P.muted())

bio.panel(ax, "C", (14.6, 10.9))
# fibroblast
fb = bio.blob((17.2, 7.6), 2.2, 1.6, wobble=0.06, seed=3, k=10)
bio.membrane(ax, fb, "cytoplasm")
bio.nucleus(ax, (16.6, 7.5), 0.7, chromatin=False, nucleolus=False)
c0 = np.array([17.7, 7.9])
for an in np.linspace(0, 360, 14, endpoint=False):
    d = np.array([math.cos(math.radians(an)), math.sin(math.radians(an))])
    if np.linalg.norm(c0 + d * 0.8 - np.array([16.6, 7.5])) < 0.75:
        continue
    e = c0 + d * np.array([1.75, 1.25])
    C.mt_line(ax, c0, e, lw=1.0, plus=True, zorder=9)
C.centrosome(ax, c0, size=0.18, microtubules=0, centrioles=False, zorder=10)
bio.label(ax, (17.2, 5.65), "fibroblast", size="tiny")
# epithelial cell
ep = [(20.3, 9.8), (22.1, 9.8), (22.1, 5.9), (20.3, 5.9)]
bio.membrane(ax, bio.smooth_closed([(20.3, 9.6), (21.2, 9.85), (22.1, 9.6), (22.15, 7.8), (22.1, 6.0), (21.2, 5.85), (20.3, 6.0), (20.25, 7.8)]), "cytoplasm")
bio.nucleus(ax, (21.2, 6.75), 0.5, chromatin=False, nucleolus=False)
for x in np.linspace(20.55, 21.85, 5):
    C.mt_line(ax, (x, 9.5), (x + 0.02, 7.45 if abs(x - 21.2) < 0.45 else 6.2), lw=1.0, plus=True, zorder=9)
bio.label(ax, (21.2, 10.15), "apical", size="tiny", color=P.muted())
bio.label(ax, (21.2, 5.45), "epithelial cell", size="tiny")
# neuron
nx = np.array([15.4, 2.8])
bio.membrane(ax, bio.blob(nx, 0.65, 0.6, wobble=0.05, seed=5, k=9), "cytoplasm", zorder=3)
ax.plot([16.0, 24.6], [2.8, 2.8], color=P.edge("membrane"), lw=7, solid_capstyle="round", zorder=2)
ax.plot([16.0, 24.6], [2.8, 2.8], color=P.fill("cytoplasm"), lw=5, solid_capstyle="round", zorder=2.1)
for k, x in enumerate(np.arange(16.3, 24.0, 1.3)):
    y = 2.8 + (0.08 if k % 2 else -0.08)
    C.mt_line(ax, (x, y), (x + 1.1, y), lw=1.0, plus=True, zorder=9)
for ang, sgn in ((120, 1), (200, -1), (250, 1)):
    d = np.array([math.cos(math.radians(ang)), math.sin(math.radians(ang))])
    a, b = nx + d * 0.55, nx + d * 1.9
    ax.plot(*np.array([a, b]).T, color=P.edge("membrane"), lw=6, solid_capstyle="round", zorder=2)
    ax.plot(*np.array([a, b]).T, color=P.fill("cytoplasm"), lw=4, solid_capstyle="round", zorder=2.1)
    s, e = (a + d * 0.1, b - d * 0.2) if sgn > 0 else (b - d * 0.2, a + d * 0.1)
    C.mt_line(ax, s, e, lw=0.9, plus=True, zorder=9)
bio.label(ax, (20.2, 3.45), "axon: plus ends out", size="tiny")
bio.label(ax, (14.6, 0.55), "dendrites: mixed", size="tiny")
bio.label(ax, (15.4, 4.35), "neuron", size="tiny")
# plant cell
pc = [(22.9, 9.7), (25.7, 9.7), (25.7, 6.0), (22.9, 6.0)]
from matplotlib.patches import Rectangle
ax.add_patch(Rectangle((22.8, 5.9), 3.0, 3.9, facecolor=P.fill("cell_wall"), edgecolor=P.edge("cell_wall"), lw=1.0, zorder=2))
ax.add_patch(Rectangle((22.95, 6.05), 2.7, 3.6, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=1.0, zorder=2.1))
for y in np.linspace(6.3, 9.4, 9):
    C.mt_line(ax, (23.1, y + 0.1), (25.5, y - 0.1), lw=0.9, plus=True, zorder=9)
bio.label(ax, (24.3, 5.45), "plant cell (cortex)", size="tiny")
