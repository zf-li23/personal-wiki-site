# Chordate characters mapped on the deuterostome tree (topology as in 7.17.41): a character matrix
# beside the tree, with gains and losses marked on the branches.
import numpy as np
import wikibio as bio
from wikibio import phylo
from matplotlib.patches import Circle, Wedge

P = bio.P
NEWICK = ("((Echinodermata,(Enteropneusta,Pterobranchia)Hemichordata)Ambulacraria,"
          "(Cephalochordata,(Tunicata,Vertebrata)Olfactores)Chordata)Deuterostomia;")
TEXT = {"Enteropneusta": "Enteropneusta", "Cephalochordata": "Cephalochordata"}
ICONS = {"Echinodermata": "phylopic/starfish", "Enteropneusta": "phylopic/acorn-worm",
         "Pterobranchia": "phylopic/pterobranch", "Cephalochordata": "phylopic/amphioxus",
         "Tunicata": "phylopic/ciona", "Vertebrata": "phylopic/lamprey"}
COLS = ["Pharyngeal slits", "Notochord", "Dorsal hollow nerve cord", "Endostyle / thyroid", "Postanal tail",
        "Segmented myomeres", "Neural crest (-like cells)", "Placodes (-like ectoderm)", "Cranium"]
# 1 present (adult or at least larva), 0.5 rudimentary / only in part of the group, 0 absent
M = {
    "Echinodermata":   [0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Enteropneusta":   [1, 0, 0.5, 0, 0, 0, 0, 0, 0],
    "Pterobranchia":   [0.5, 0, 0.5, 0, 0, 0, 0, 0, 0],
    "Cephalochordata": [1, 1, 1, 1, 1, 1, 0, 0, 0],
    "Tunicata":        [1, 1, 1, 1, 1, 0, 0.5, 0.5, 0],
    "Vertebrata":      [1, 1, 1, 1, 1, 1, 1, 1, 1],
}
GAINS = [("Deuterostomia", "1"), ("Chordata", "2-6"), ("Olfactores", "7, 8"), ("Vertebrata", "9")]
MARKS = [dict(node=n, kind="trait", text=t, at=0.5, text_size="tiny", side=-1, offset=0.3, va="bottom")
         for n, t in GAINS]
MARKS += [dict(node="Echinodermata", kind="loss", text="1", at=0.6, text_size="tiny", side=-1, offset=0.3,
               va="bottom"),
          dict(node="Tunicata", kind="loss", text="6", at=0.45, text_size="tiny", side=-1, offset=0.3, va="bottom")]

fig, ax = bio.canvas(27.0, 10.8)
t = phylo.tree(ax, NEWICK, origin=(0.8, 1.2), width=7.0, height=6.4, root_edge=0.8, tip_text=TEXT, icons=ICONS,
               icon_size=0.7, icon_width=1.4, label_size="small",
               clades=[dict(node="Chordata", token="dna", style="bar", label="Chordata")], marks=MARKS)

x0, dx = 14.8, 1.25
tips = {n.name: n.xy for n in t.tips()}
for j, name in enumerate(COLS):
    x = x0 + j * dx
    bio.label(ax, (x - 0.1, 8.0), f"{j + 1}  {name}", size="small", ha="left", va="bottom", rotation=35)
fill, edge = P.fill("dna"), P.edge("dna")
for tip, row in M.items():
    y = tips[tip][1]
    ax.plot([x0 - 0.6, x0 + (len(COLS) - 1) * dx + 0.5], [y, y], color=P.mix(P.muted(), P.surface(), 0.6),
            lw=0.6, zorder=1)
    for j, v in enumerate(row):
        c = (x0 + j * dx, y)
        ax.add_patch(Circle(c, 0.24, facecolor=P.surface(), edgecolor=edge, lw=1.0, zorder=5))
        if v == 1:
            ax.add_patch(Circle(c, 0.24, facecolor=fill, edgecolor=edge, lw=1.0, zorder=6))
        elif v == 0.5:
            ax.add_patch(Wedge(c, 0.24, 90, 270, facecolor=fill, edgecolor=edge, lw=1.0, zorder=6))

# legend
ly = 0.35
for k, (v, txt) in enumerate(((1, "present (adult or larva)"), (0.5, "rudimentary or in part of the group"),
                              (0, "absent"))):
    cx = (14.4, 18.8, 24.4)[k]
    ax.add_patch(Circle((cx, ly), 0.2, facecolor=P.surface(), edgecolor=edge, lw=1.0, zorder=5))
    if v == 1:
        ax.add_patch(Circle((cx, ly), 0.2, facecolor=fill, edgecolor=edge, lw=1.0, zorder=6))
    elif v == 0.5:
        ax.add_patch(Wedge((cx, ly), 0.2, 90, 270, facecolor=fill, edgecolor=edge, lw=1.0, zorder=6))
    bio.label(ax, (cx + 0.35, ly), txt, size="small", ha="left")
phylo.marker(ax, (1.0, ly), "trait", direction=(1, 0))
bio.label(ax, (1.35, ly), "gain of characters (numbers)", size="small", ha="left")
phylo.marker(ax, (7.2, ly), "loss", direction=(1, 0))
bio.label(ax, (7.55, ly), "loss", size="small", ha="left")
