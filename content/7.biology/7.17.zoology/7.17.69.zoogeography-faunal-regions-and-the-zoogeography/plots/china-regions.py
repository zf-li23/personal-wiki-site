"""Schematic of the zoogeographic regionalization of China (after Zhang Rongzu): two realms, three
subrealms, seven regions. A topological diagram, not a map: the shapes show which regions adjoin
and where the Palearctic-Oriental boundary runs, not true outlines or coastlines.
"""

import wikibio as bio
from matplotlib.patches import Polygon, Ellipse

P = bio.P

fig, ax = bio.canvas(18, 12.6)

REG = {
    "MX": ([(0.4, 7.2), (11, 7.2), (11, 8.2), (9.2, 10.8), (0.4, 10.8)], "lipid",
           "Mongolia-Xinjiang", "temperate steppe and desert fauna", (5.0, 9.0)),
    "NE": ([(11, 7.2), (16.2, 7.2), (16.2, 11.6), (10.2, 11.6), (9.2, 10.8), (11, 8.2)], "dna2",
           "Northeast", "boreal conifer-forest fauna", (13.3, 9.6)),
    "NC": ([(7.4, 6.6), (8.6, 5.4), (16.2, 5.4), (16.2, 7.2), (7.4, 7.2)], "bone",
           "North China", "temperate forest, steppe and farmland fauna", (12.0, 6.6)),
    "QT": ([(0.4, 3.8), (5.2, 3.8), (5.2, 5.6), (7.4, 6.6), (7.4, 7.2), (0.4, 7.2)], "metabolite",
           "Qinghai-Tibet", "alpine meadow and cold-desert fauna", (2.7, 5.0)),
    "SW": ([(5.2, 2.4), (8.6, 2.4), (8.6, 5.4), (7.4, 6.6), (5.2, 5.6)], "carbohydrate",
           "Southwest", "montane: Palearctic above,\nOriental below", (6.9, 4.2)),
    "CC": ([(8.6, 3.1), (16.2, 3.1), (16.2, 5.4), (8.6, 5.4)], "positive",
           "Central China", "subtropical forest and farmland fauna", (12.4, 4.25)),
    "SC": ([(5.2, 1.2), (16.2, 1.2), (16.2, 3.1), (8.6, 3.1), (8.6, 2.4), (5.2, 2.4)], "plant",
           "South China", "tropical forest fauna", (12.4, 2.15)),
}
for key, (pts, tok, name, fauna, c) in REG.items():
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.2, zorder=3))
    bio.label(ax, (c[0], c[1] + 0.28), name, size="normal", bold=True, color=P.on_fill())
    bio.label(ax, (c[0], c[1] - 0.3), fauna, size="tiny", color=P.on_fill())

# islands of the South China region
for xy, w, h, name in [((17.1, 2.2), 0.55, 1.3, "Taiwan"), ((11.0, 0.45), 1.1, 0.6, "Hainan")]:
    ax.add_patch(Ellipse(xy, w, h, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=3))
bio.label(ax, (17.1, 3.2), "Taiwan", size="tiny")
bio.label(ax, (12.1, 0.45), "Hainan", size="tiny", ha="left")

# realm boundary
bound = [(0.4, 3.8), (5.2, 3.8), (5.2, 5.6), (7.4, 6.6), (8.6, 5.4), (16.2, 5.4)]
xs, ys = zip(*bound)
ax.plot(xs, ys, color=P.edge("negative"), lw=3.0, ls=(0, (4, 2)), zorder=6)
# broad transition in the east
ax.add_patch(Polygon([(9.5, 5.0), (16.2, 5.0), (16.2, 5.8), (9.5, 5.8)], closed=True,
                     facecolor="none", edgecolor=P.edge("negative"), lw=0.8, ls=":", zorder=6))
bio.label(ax, (2.8, 3.45), "Himalaya (south slope)", size="tiny", color=P.edge("negative"))
bio.callout(ax, (7.35, 6.6), (3.4, 6.55), "Hengduan Mts, north end (~30° N)", size="tiny", color=P.edge("negative"))
bio.label(ax, (10.3, 5.65), "Qinling", size="tiny", color=P.edge("negative"))
bio.label(ax, (14.0, 5.65), "Huai River (wide transition)", size="tiny", color=P.edge("negative"))

# realms and subrealms
bio.label(ax, (0.4, 12.2), "PALEARCTIC REALM", size="small", bold=True, ha="left")
bio.label(ax, (0.4, 11.5), "Central Asian subrealm: Mongolia-Xinjiang, Qinghai-Tibet", size="tiny", ha="left")
bio.label(ax, (10.2, 12.2), "Northeast Asian subrealm:", size="tiny", ha="left")
bio.label(ax, (10.2, 11.85), "Northeast, North China", size="tiny", ha="left")
bio.label(ax, (0.4, 1.6), "ORIENTAL REALM", size="small", bold=True, ha="left")
bio.label(ax, (0.4, 1.0), "Sino-Indian subrealm:", size="tiny", ha="left")
bio.label(ax, (0.4, 0.6), "Southwest, Central, South China", size="tiny", ha="left")
bio.label(ax, (17.6, 12.2), "Schematic, not to scale", size="tiny", ha="right", color=P.muted())
