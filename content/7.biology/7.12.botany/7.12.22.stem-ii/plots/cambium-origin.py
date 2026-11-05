# Origin and activity of the vascular cambium in a eudicot stem (transverse sections; xylem blue,
# phloem orange, cambium yellow). (A) Primary structure: a ring of collateral bundles separated by pith
# rays, fascicular cambium between primary xylem and phloem. (B) Interfascicular cambium (dashed) arises
# in the pith rays and joins the fascicular cambium into a ring. (C) The cambium produces secondary xylem
# inwards and secondary phloem outwards; primary phloem is pushed outwards. (D) A three-year-old woody
# stem drawn tissue by tissue (wikibio.botany): pith, primary xylem, three growth rings, rays, cambium,
# secondary phloem and periderm.
import math

import numpy as np
from matplotlib.patches import Circle, Polygon, Wedge

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(34.0, 10.6)
NB = 8


def ann(c, r0, r1, a0, a1, tok, z=4, lw=0.6):
    w = Wedge(c, r1, a0, a1, width=r1 - r0, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=lw, zorder=z)
    ax.add_patch(w)


def stage(c, k):
    ax.add_patch(Circle(c, 3.6, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cell_wall"), lw=1.4, zorder=2))
    ax.add_patch(Circle(c, 3.6, facecolor="none", edgecolor=P.edge("plant"), lw=2.4, zorder=2.1))
    span = 26
    for i in range(NB):
        a = i * 360 / NB
        if k >= 3:
            ann(c, 1.15, 2.05, a - span / 2, a + span / 2, "xylem", z=4)
            ann(c, 2.12, 2.6, a - span / 2 - 2, a + span / 2 + 2, "phloem", z=4)
            ann(c, 2.62, 2.85, a - span / 2 + 3, a + span / 2 - 3, "phloem", z=4.1, lw=1.4)  # crushed primary phloem
        ann(c, 1.1, 1.65, a - span / 2, a + span / 2, "xylem", z=4.5)
        if k < 3:
            ann(c, 1.75, 2.45, a - span / 2, a + span / 2, "phloem", z=4)
        r_c = 1.7 if k < 3 else 2.08
        t = np.radians(np.linspace(a - span / 2, a + span / 2, 20))
        ax.plot(c[0] + r_c * np.cos(t), c[1] + r_c * np.sin(t), color=P.edge("cambium"), lw=2.6, zorder=6)
        if k >= 2:
            t2 = np.radians(np.linspace(a + span / 2, a + 360 / NB - span / 2, 20))
            ax.plot(c[0] + r_c * np.cos(t2), c[1] + r_c * np.sin(t2), color=P.edge("cambium"), lw=2.6, zorder=6,
                    ls=(0, (2, 1.2)) if k == 2 else "-")
        if k >= 3:
            ann(c, 1.15, 2.05, a + span / 2, a + 360 / NB - span / 2, "xylem", z=3.9)
            ann(c, 2.12, 2.45, a + span / 2, a + 360 / NB - span / 2, "phloem", z=3.9)
            tt = math.radians(a + 180 / NB)
            ax.plot([c[0] + 1.15 * math.cos(tt), c[0] + 2.45 * math.cos(tt)], [c[1] + 1.15 * math.sin(tt), c[1] + 2.45 * math.sin(tt)],
                    color=P.edge("lipid"), lw=1.6, zorder=5)


titles = ["Primary structure", "Interfascicular cambium", "Secondary growth begins", "Woody stem, 3 years"]
cs = [np.array([4.2, 4.8]), np.array([12.6, 4.8]), np.array([21.0, 4.8]), np.array([29.6, 4.8])]
for k, c in enumerate(cs):
    bio.panel(ax, "ABCD"[k], (c[0] - 4.0, 10.4))
    bio.label(ax, (c[0], 10.0), titles[k], size="normal", bold=True)
for k in range(3):
    stage(cs[k], k + 1)
w = B.woody_stem(ax, tuple(cs[3]), 4.0, years=3, heartwood=0)
c = cs[0]
bio.callout(ax, tuple(c + 2.1 * np.array([0, 1])), (c[0] - 1.2, 9.2), "Primary phloem", size="small")
bio.callout(ax, tuple(c + 1.7 * np.array([0.707, 0.707])), (c[0] + 1.4, 9.2), "Fascicular cambium", size="small")
bio.callout(ax, tuple(c + 1.35 * np.array([-0.707, -0.707])), (c[0] - 1.0, 0.4), "Primary xylem", size="small")
bio.callout(ax, tuple(c + 1.9 * np.array([math.cos(math.radians(22.5)), math.sin(math.radians(22.5))])), (c[0] + 1.2, 0.4),
            "Pith ray", size="small")
c = cs[1]
bio.callout(ax, tuple(c + 1.7 * np.array([math.cos(math.radians(22.5)), math.sin(math.radians(22.5))])), (c[0] + 1.0, 9.2),
            "Interfascicular cambium", size="small")
c = cs[2]
bio.callout(ax, tuple(c + 1.6 * np.array([0, 1])), (c[0] - 2.0, 8.6), "Secondary xylem", size="small")
bio.callout(ax, tuple(c + 2.3 * np.array([0.707, 0.707])), (c[0] + 1.2, 9.2), "Secondary phloem", size="small")
bio.callout(ax, tuple(c + 2.74 * np.array([0, -1])), (c[0] + 1.0, 0.4), "Crushed primary phloem", size="small")
bio.callout(ax, tuple(c + 1.8 * np.array([math.cos(math.radians(22.5)), math.sin(math.radians(-22.5 + 45))])), (c[0] - 1.2, 0.4),
            "Ray", size="small")
d = cs[3]
for key, txt, xy in (("cambium", "Vascular cambium", (d[0] + 1.6, 9.2)), ("annual_ring", "Growth ring", (d[0] - 1.6, 9.2)),
                     ("periderm", "Periderm", (d[0] + 1.6, 0.4)), ("pith", "Pith", (d[0] - 1.6, 0.4))):
    if w.get(key) is not None:
        bio.callout(ax, w[key], xy, txt, size="small")
