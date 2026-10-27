"""Apoptosis and necrosis compared (schematic, after electron micrographs of dying cells).

Top row, apoptosis: a normal cell shrinks, its chromatin condenses against the nuclear envelope and the
nucleus fragments (karyorrhexis) while the plasma membrane stays intact and forms blebs; the cell breaks up
into membrane-enclosed apoptotic bodies that display phosphatidylserine and are engulfed by a macrophage,
without inflammation. Bottom row, necrosis: the cell and its organelles swell, the plasma membrane ruptures,
the contents (including DAMPs) leak out and attract neutrophils, causing inflammation.
"""

import numpy as np
from matplotlib.patches import Circle, PathPatch
from matplotlib.path import Path

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 13.4)


def dense_nucleus(c, r, seed=0):
    o = bio.core.blob(c, r, r * 0.9, wobble=0.12, seed=seed, k=7)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill("chromatin"), edgecolor=P.edge("chromatin"),
                           lw=1.0, zorder=9))


def bleb_cell(c, r, nb=6, seed=2):
    rng = np.random.default_rng(seed)
    th = np.linspace(0, 2 * np.pi, 120)
    rr = r * (1 + 0.04 * np.sin(5 * th))
    for k in range(nb):
        a0 = 2 * np.pi * k / nb + rng.uniform(-0.2, 0.2)
        rr += r * 0.22 * np.exp(-((np.angle(np.exp(1j * (th - a0)))) / 0.18) ** 2)
    pts = np.c_[c[0] + rr * np.cos(th), c[1] + rr * np.sin(th)]
    bio.membrane(ax, pts, "cytoplasm", zorder=3)


def row_label(y, text):
    bio.label(ax, (0.3, y), text, size="title", bold=True, ha="left")


# ---------------------------------------------------------------- apoptosis
yA = 9.2
row_label(12.9, "Apoptosis")
bio.cell(ax, (2.4, yA), 1.9, 1.6, seed=3)
bio.nucleus(ax, (2.3, yA), 0.8, seed=4)
bio.mitochondrion(ax, (3.4, yA - 0.9), 0.8, 0.32, angle=20, cristae=3)
bio.label(ax, (2.4, yA - 2.3), "normal cell", size="small")

bio.arrow(ax, (4.6, yA), (5.6, yA), kind="process")
bio.cell(ax, (7.2, yA), 1.3, 1.15, seed=6)
o = bio.core.blob((7.1, yA + 0.05), 0.62, 0.55, wobble=0.04, seed=8, k=9)
ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=1.8, zorder=8))
for a in np.linspace(0, 2 * np.pi, 7, endpoint=False):
    ax.add_patch(Circle((7.1 + 0.42 * np.cos(a), yA + 0.05 + 0.36 * np.sin(a)), 0.14, color=P.fill("chromatin"),
                        ec=P.edge("chromatin"), lw=0.6, zorder=9))
bio.mitochondrion(ax, (7.75, yA - 0.7), 0.6, 0.26, angle=30, cristae=3)
bio.label(ax, (7.2, yA - 2.3), "shrinkage, chromatin\ncondensation", size="small")

bio.arrow(ax, (8.9, yA), (9.9, yA), kind="process")
bleb_cell((11.6, yA), 1.05, nb=6)
for c in [(11.35, yA + 0.2), (11.8, yA - 0.15), (11.5, yA - 0.35), (11.95, yA + 0.3)]:
    dense_nucleus(c, 0.2, seed=int(c[0] * 10))
bio.label(ax, (11.6, yA - 2.3), "blebbing, nuclear\nfragmentation", size="small")

bio.arrow(ax, (13.2, yA), (14.2, yA), kind="process")
rng = np.random.default_rng(5)
bodies = [(15.2, yA + 0.8, 0.5), (16.2, yA + 0.2, 0.42), (15.3, yA - 0.5, 0.45), (16.4, yA - 0.9, 0.36)]
for x, y, r in bodies:
    bio.membrane(ax, bio.core.blob((x, y), r, r * 0.9, wobble=0.05, seed=int(x * 7), k=8), "cytoplasm", zorder=3)
    dense_nucleus((x + 0.05, y), r * 0.45, seed=int(y * 9 + 20))
    for a in np.linspace(0.3, 2 * np.pi, 5, endpoint=False):
        ax.add_patch(Circle((x + r * 1.07 * np.cos(a), y + r * 0.97 * np.sin(a)), 0.05, color=P.fill("lipid_head"),
                            ec=P.edge("lipid_head"), lw=0.4, zorder=8))
bio.callout(ax, (15.62, yA + 1.18), (17.4, yA + 1.9), "phosphatidylserine\n(\"eat me\")", size="tiny")
bio.label(ax, (15.8, yA - 2.3), "apoptotic bodies", size="small")

bio.arrow(ax, (17.2, yA), (18.4, yA), kind="process")
bio.icon(ax, "servier/macrophage", at=(21.2, yA), height=3.6)
for x, y, r in [(20.9, yA + 0.15, 0.32), (21.6, yA - 0.35, 0.26)]:
    ax.add_patch(Circle((x, y), r + 0.12, facecolor=P.fill("lysosome"), edgecolor=P.edge("lysosome"), lw=0.9, zorder=30))
    dense_nucleus((x, y), r * 0.55, seed=int(x * 3))
    ax.patches[-1].set_zorder(31)
bio.label(ax, (21.2, yA - 2.3), "engulfed by a macrophage\n(efferocytosis), no inflammation", size="small")
bio.label(ax, (24.6, yA + 0.3), "membrane\nintact\nthroughout", size="tiny", color=P.muted())

# ---------------------------------------------------------------- necrosis
yN = 3.2
row_label(6.0, "Necrosis")
bio.cell(ax, (2.4, yN), 1.9, 1.6, seed=3)
bio.nucleus(ax, (2.3, yN), 0.8, seed=4)
bio.mitochondrion(ax, (3.4, yN - 0.9), 0.8, 0.32, angle=20, cristae=3)
bio.label(ax, (2.4, yN - 2.3), "normal cell", size="small")

bio.arrow(ax, (4.6, yN), (5.6, yN), kind="process")
bio.cell(ax, (8.0, yN), 2.25, 1.95, seed=11)
bio.nucleus(ax, (7.7, yN + 0.1), 0.95, seed=12, chromatin=False)
for c, ang in [((9.2, yN - 0.9), 15), ((8.9, yN + 1.1), -25), ((6.8, yN - 1.1), 40)]:
    o = bio.core.blob(c, 0.5, 0.36, wobble=0.05, seed=int(c[0] * 5), k=8, angle=np.radians(ang))
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill("mitochondrion"), edgecolor=P.edge("mitochondrion"),
                           lw=1.0, zorder=9))
bio.label(ax, (8.0, yN - 2.6), "swelling of cell\nand organelles", size="small")

bio.arrow(ax, (10.6, yN), (11.6, yN), kind="process")
o = bio.core.blob((14.0, yN), 2.2, 1.9, wobble=0.06, seed=13, k=11)
ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=2, alpha=0.6))
n = len(o)
gaps = [(int(0.06 * n), int(0.13 * n)), (int(0.22 * n), int(0.28 * n)), (int(0.88 * n), int(0.94 * n))]
keep = np.ones(n, bool)
for a, b in gaps:
    keep[a:b] = False
seg = []
for i in range(n):
    if keep[i]:
        seg.append(o[i])
    elif seg:
        s = np.array(seg); ax.plot(s[:, 0], s[:, 1], color=P.edge("membrane"), lw=2.2, zorder=4); seg = []
if seg:
    s = np.array(seg); ax.plot(s[:, 0], s[:, 1], color=P.edge("membrane"), lw=2.2, zorder=4)
o = bio.core.blob((13.7, yN + 0.1), 0.9, 0.8, wobble=0.1, seed=14, k=9)
ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=1.0, zorder=8,
                       ls=(0, (3, 2))))
for a, b in gaps:
    m = bio.core.blob((14.0, yN), 2.2, 1.9, wobble=0.06, seed=13, k=11)[(a + b) // 2]
    d = (m - np.array([14.0, yN]))
    d = d / np.linalg.norm(d)
    for j in range(7):
        q = m + d * rng.uniform(0.15, 0.8) + rng.normal(0, 0.15, 2)
        ax.add_patch(Circle(q, rng.uniform(0.05, 0.11), color=P.fill(["protein", "metabolite", "enzyme"][j % 3]),
                            ec=P.edge(["protein", "metabolite", "enzyme"][j % 3]), lw=0.4, zorder=12))
bio.label(ax, (14.0, yN - 2.6), "membrane rupture,\ncontents (DAMPs) leak", size="small")

bio.arrow(ax, (16.6, yN), (17.6, yN), kind="process")
bio.icon(ax, "servier/neutrophil", at=(19.4, yN + 0.6), height=2.0)
bio.icon(ax, "servier/macrophage", at=(22.2, yN - 0.2), height=2.6)
for j in range(14):
    q = (20.8 + rng.uniform(-2.8, 2.6), yN + rng.uniform(-1.6, 1.8))
    ax.add_patch(Circle(q, rng.uniform(0.05, 0.1), color=P.fill(["protein", "metabolite"][j % 2]), lw=0, zorder=5))
bio.label(ax, (20.8, yN - 2.6), "neutrophils and macrophages:\ninflammation, tissue damage", size="small")
