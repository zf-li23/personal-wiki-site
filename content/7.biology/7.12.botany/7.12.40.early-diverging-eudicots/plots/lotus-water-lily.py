# Lotus and water lily, a case of convergence. Top row, Nelumbo (Proteales, eudicots): emergent peltate
# leaf; free carpels sunk in the spongy obconical receptacle; tricolpate pollen. Bottom row, Nymphaea
# (Nymphaeales, ANA grade): floating leaf with a deep basal sinus; syncarpous, many-locular ovary;
# monosulcate pollen (leaf seen from above). Right: the two genera sit on distant branches of the angiosperm tree.
import math

import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, Polygon, Wedge
from wikibio import phylo, plant

P = bio.P
fig, ax = bio.canvas(36, 15)


def water(y, x0, x1):
    ax.plot([x0, x1], [y, y], color=P.edge("dna"), lw=1.2, ls=(0, (4, 3)), zorder=2)


def pollen(c, r, kind):
    ax.add_patch(Circle(c, r, facecolor=P.light("anther"), edgecolor=P.edge("anther"), lw=1.2, zorder=5))
    if kind == "tricolpate":
        for a in (90, 210, 330):
            t = math.radians(a)
            p, q = np.array(c) + 0.25 * r * np.array([math.cos(t), math.sin(t)]), np.array(c) + 0.95 * r * np.array([math.cos(t), math.sin(t)])
            ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge("anther"), lw=2.4, solid_capstyle="round", zorder=6)
    else:
        ax.add_patch(Ellipse(c, 1.5 * r, 0.22 * r, facecolor=P.edge("anther"), edgecolor="none", zorder=6))


# ---- Nelumbo
bio.label(ax, (0.4, 14.3), "Nelumbo (lotus)", size="title", italic=True, ha="left")
bio.panel(ax, "A", (0.3, 13.4))
water(9.2, 0.6, 6.6)
ax.plot([3.6, 3.6], [8.0, 11.6], color=P.edge("plant"), lw=2.2, zorder=3)
ax.add_patch(Ellipse((3.6, 11.9), 5.0, 1.2, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.2, zorder=4))
for a in np.linspace(0, 2 * math.pi, 13)[:-1]:
    ax.plot([3.6, 3.6 + 2.3 * math.cos(a)], [11.9, 11.9 + 0.52 * math.sin(a)], color=P.edge("plant"), lw=0.6, zorder=5)
bio.label(ax, (3.6, 7.4), "Peltate leaf held above water", size="small")

bio.panel(ax, "B", (7.4, 13.4))
cone = [(8.6, 12.4), (13.2, 12.4), (11.4, 8.8), (10.4, 8.8)]
ax.add_patch(Polygon(cone, closed=True, facecolor=P.light("plant"), edgecolor=P.edge("plant"), lw=1.2, zorder=4))
for x, y in [(9.4, 11.6), (10.4, 11.7), (11.4, 11.7), (12.4, 11.6), (9.9, 10.7), (10.9, 10.8), (11.9, 10.7),
             (10.4, 9.8), (11.4, 9.8)]:
    ax.add_patch(Ellipse((x, y), 0.55, 0.75, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=0.9, zorder=5))
ax.plot([10.9, 10.9], [8.8, 7.9], color=P.edge("plant"), lw=2.2, zorder=3)
bio.label(ax, (10.9, 7.4), "Free carpels sunk in receptacle", size="small")

bio.panel(ax, "C", (14.6, 13.4))
pollen((17.0, 10.6), 1.3, "tricolpate")
bio.label(ax, (17.0, 7.4), "Tricolpate pollen", size="small")

# ---- Nymphaea
bio.label(ax, (0.4, 6.4), "Nymphaea (water lily)", size="title", italic=True, ha="left")
bio.panel(ax, "D", (0.3, 5.5))
ax.add_patch(Wedge((3.6, 3.1), 2.4, 100, 440 - 20, width=None, facecolor=P.fill("plant"), edgecolor=P.edge("plant"),
                   lw=1.2, zorder=4))
ax.plot([3.6, 3.6], [3.1, 0.9], color=P.edge("plant"), lw=2.0, zorder=3)
bio.label(ax, (3.6, 0.3), "Floating leaf, deep basal sinus (top view)", size="small")

bio.panel(ax, "E", (7.4, 5.5))
plant.ovary(ax, (10.9, 3.4), 1.7, n=10, placentation="axile", ovules=2, token="ovary")
bio.label(ax, (10.9, 0.3), "Syncarpous many-locular ovary", size="small")

bio.panel(ax, "F", (14.6, 5.5))
pollen((17.0, 3.2), 1.3, "monosulcate")
bio.label(ax, (17.0, 0.3), "Monosulcate pollen", size="small")

# ---- tree
NEWICK = "(Amborella,(Nymphaea,(Magnoliids,(Monocots,(Ranunculales,(Nelumbo,Coreeudicots))))));"
t = phylo.tree(ax, NEWICK, origin=(21.5, 1.0), width=8.0, height=11.5, label_size="small", root_edge=0.4,
               tip_text={"Nymphaea": "Nymphaea (Nymphaeales)", "Nelumbo": "Nelumbo (Proteales)",
                         "Coreeudicots": "Other eudicots"},
               italic={"Amborella"},
               clades=[dict(tips=["Nymphaea"], token="dna", style="branch"),
                       dict(tips=["Nelumbo"], token="petal", style="branch"),
                       dict(tips=["Ranunculales", "Nelumbo", "Coreeudicots"], token="anther", style="bar",
                            label="Eudicots")])
