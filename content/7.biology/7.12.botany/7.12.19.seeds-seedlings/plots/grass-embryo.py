# The grass embryo (wheat, Triticum aestivum), median longitudinal section through the base of the grain.
# The embryo lies at one side of the grain, its single cotyledon (scutellum) pressed against the
# endosperm; the scutellar epithelium (one layer of columnar cells) faces the endosperm and secretes
# hydrolytic enzymes at germination; a procambial strand runs up the scutellum. The embryo axis carries
# the plumule (shoot apex and leaf primordia) sheathed by the coleoptile, a very short mesocotyl, the
# scutellar node, the epiblast (a small flap opposite the scutellum; absent in maize) and the radicle
# (root apex and root cap) sheathed by the coleorhiza. The endosperm is covered by the aleurone layer,
# and the whole grain by the fused pericarp and seed coat.
import numpy as np
from matplotlib.patches import PathPatch, Polygon
from matplotlib.path import Path

import wikibio as bio
from wikibio import plantmorph as PM

P = bio.P
R = PM.ROLE
fig, ax = bio.canvas(25.0, 15.0)


def patch(pts, role, lw=0.9, z=6):
    pts = np.asarray(pts, float)
    return ax.add_patch(PathPatch(Path(np.vstack([pts, pts[:1]]), closed=True), facecolor=P.fill(R.get(role, role)),
                                  edgecolor=P.edge(R.get(role, role)), lw=lw, joinstyle="round", zorder=z))


sc = bio.smooth_closed
# grain outline (the embryo end only; the endosperm continues off the top right)
grain = [(10.0, 16.5), (7.4, 13.6), (6.0, 11.0), (5.2, 8.0), (5.3, 4.8), (6.2, 2.3), (8.0, 0.8), (10.4, 0.5),
         (13.0, 1.0), (16.0, 2.2), (19.5, 4.4), (21.0, 10.0), (19.0, 16.5)]
outer = sc(grain, n=300)
# build an open-topped region by clipping later; simpler: draw layered shapes inside a clipping rectangle
clip = Polygon([(0, 0), (19.0, 0), (19.0, 14.4), (0, 14.4)], closed=True, transform=ax.transData)

layers = [(1.0, "pericarp"), (0.955, "aleurone"), (0.925, "endosperm")]
c0 = np.array([12.2, 7.6])
for f, role in layers:
    p = patch(c0 + (outer - c0) * f, role, z=6 - f)
    p.set_clip_path(clip)
ax.plot([19.0, 19.0], [0.4, 14.4], color=P.muted(), lw=0.6, ls=(0, (3, 3)), zorder=8)
bio.label(ax, (19.2, 13.9), "endosperm continues", size="tiny", color=P.muted(), ha="left")

# the embryo pocket between the seed coat and the endosperm
pocket = sc([(9.0, 13.0), (7.3, 12.7), (6.15, 10.8), (5.65, 8.0), (5.7, 4.8), (6.35, 2.5), (7.9, 1.25), (9.4, 1.55),
             (10.1, 3.0), (10.85, 7.0), (10.6, 10.0), (9.9, 12.1)], n=240)
ax.add_patch(PathPatch(Path(np.vstack([pocket, pocket[:1]]), closed=True), facecolor=P.fill("cytoplasm"),
                       edgecolor=P.muted(), lw=0.5, zorder=6.5))
# scutellum: shield against the endosperm
scut = sc([(8.6, 12.6), (9.8, 11.6), (10.5, 9.6), (10.7, 7.0), (10.4, 4.4), (9.6, 2.4), (8.6, 1.6), (7.9, 2.6),
           (8.2, 5.0), (8.2, 9.0), (8.1, 11.5)], n=240)
patch(scut, "scutellum", z=7)
# epithelium: a row of columnar cells along the endosperm face of the scutellum
face = sc([(9.8, 11.6), (10.5, 9.6), (10.7, 7.0), (10.4, 4.4), (9.6, 2.4)], n=200)[:-1]
seg = np.linspace(0, len(face) - 1, 34).astype(int)
for i0, i1 in zip(seg[:-1], seg[1:]):
    a, b = face[i0], face[i1]
    t = b - a
    n = np.array([-t[1], t[0]]) / (np.hypot(*t) + 1e-9)
    if n[0] < 0:
        n = -n
    q = np.array([a, b, b - n * 0.32, a - n * 0.32])
    ax.add_patch(Polygon(q, closed=True, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=0.5, zorder=7.5))
# procambial strand in the scutellum
strand = np.array([(8.0, 7.0), (8.9, 7.6), (9.4, 9.0), (9.3, 10.8), (8.9, 11.9)])
ax.plot(strand[:, 0], strand[:, 1], color=P.edge("xylem"), lw=1.4, ls=(0, (4, 2)), zorder=8)

# coleoptile sheathing the plumule
cole = sc([(6.5, 7.3), (6.3, 9.6), (6.6, 11.4), (7.1, 12.3), (7.6, 11.4), (7.9, 9.6), (7.8, 7.3)], n=200)
patch(cole, "coleoptile", z=8)
inner = sc([(6.75, 7.5), (6.62, 9.5), (6.85, 11.0), (7.12, 11.7), (7.4, 11.0), (7.6, 9.5), (7.55, 7.5)], n=200)
patch(inner, "embryo", z=8.5)
# plumule: shoot apex dome and alternating leaf primordia
apex = sc([(6.95, 8.4), (7.0, 8.95), (7.15, 9.1), (7.3, 8.95), (7.35, 8.4)], n=60)
patch(apex, "positive", z=9.5)
for k, (y, sgn) in enumerate(((8.3, -1), (8.9, 1), (9.6, -1), (10.4, 1))):
    x0 = 7.15 + sgn * 0.18
    h = 0.6 + 0.4 * k
    leafp = sc([(x0, y), (x0 + sgn * 0.22, y + h * 0.5), (x0 + sgn * 0.05, y + h), (x0 - sgn * 0.08, y + h * 0.4)], n=60)
    patch(leafp, "plant", lw=0.6, z=9 + 0.01 * k)
# axis: mesocotyl + scutellar node + hypocotyl region
axis = sc([(6.6, 7.4), (6.5, 6.4), (6.6, 5.2), (7.0, 4.9), (7.6, 5.2), (7.9, 6.4), (7.8, 7.4)], n=160)
patch(axis, "embryo", z=8.2)
ax.plot([7.75, 8.3], [6.9, 6.9], color=P.edge(R["scutellum"]), lw=1.0, zorder=8.6)  # scutellar node
# epiblast: small flap on the outer side of the axis
epi = sc([(6.55, 6.6), (6.05, 6.9), (5.95, 6.4), (6.5, 6.1)], n=60)
patch(epi, "scutellum", z=8.4)
# coleorhiza sheathing the radicle
rhiza = sc([(6.6, 5.2), (6.4, 3.8), (6.6, 2.4), (7.1, 1.9), (7.6, 2.4), (7.8, 3.8), (7.6, 5.2)], n=200)
patch(rhiza, "pericarp", z=8)
rad = sc([(6.8, 5.0), (6.7, 3.9), (6.85, 3.0), (7.1, 2.7), (7.35, 3.0), (7.5, 3.9), (7.4, 5.0)], n=160)
patch(rad, "radicle", z=8.5)
cap = sc([(6.86, 3.2), (6.9, 2.85), (7.1, 2.62), (7.3, 2.85), (7.34, 3.2), (7.1, 3.35)], n=60)
patch(cap, "highlight", lw=0.6, z=9)

left = [((6.4, 11.0), "Coleoptile", "left"), ((7.0, 10.6), "Leaf primordia", "left"), ((7.15, 8.95), "Shoot apex", "left"),
        ((6.9, 7.6), "Mesocotyl", "left"), ((6.05, 6.6), "Epiblast", "left"), ((6.75, 4.4), "Radicle", "left"),
        ((7.1, 2.95), "Root cap", "left"), ((6.45, 2.8), "Coleorhiza", "left"), ((5.4, 5.4), "Pericarp + seed coat", "left")]
right = [((9.15, 11.6), "Procambial strand", "right"), ((9.0, 9.0), "Scutellum (cotyledon)", "right"),
         ((10.55, 5.5), "Epithelium", "right"), ((8.25, 6.9), "Scutellar node", "right"),
         ((15.8, 2.52), "Aleurone layer", "right"), ((14.0, 7.5), "Starchy endosperm", "right")]
PM.callouts(ax, left, left=3.6, gap=0.85)
PM.callouts(ax, right, right=20.0, gap=0.85)
