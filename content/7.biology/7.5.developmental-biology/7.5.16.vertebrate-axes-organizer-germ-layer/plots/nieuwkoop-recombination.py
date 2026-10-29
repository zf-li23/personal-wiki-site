# Nieuwkoop's recombination experiments (1969) and their interpretation. A: a late blastula is cut into animal cap
# (prospective ectoderm), marginal zone and vegetal mass. Cultured alone, the animal cap forms epidermis and the
# vegetal mass endoderm; neither forms mesoderm. B: an animal cap combined with a vegetal mass forms mesoderm from
# animal-cap cells (shown by lineage labels): the vegetal cells induce mesoderm. C: dorsal vegetal cells induce
# dorsal mesoderm (notochord, muscle), ventral vegetal cells ventral mesoderm (blood, mesenchyme): the vegetal mass
# is already patterned along the dorsal-ventral axis, and its dorsal part is the Nieuwkoop centre.
import numpy as np
import wikibio as bio
from matplotlib.patches import Wedge, Circle

fig, ax = bio.canvas(24.0, 9.6)
P = bio.P
ect, mes, endo = "channel", "muscle", "highlight"


def cap(c, r, tok=ect, label_cells=False):
    ax.add_patch(Wedge(c, r, 0, 180, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.1, zorder=8))
    if label_cells:
        for k in range(6):
            t = np.pi * (k + 0.5) / 6
            ax.add_patch(Circle((c[0] + 0.6 * r * np.cos(t), c[1] + 0.45 * r * np.sin(t)), 0.07, facecolor=P.edge("protein"),
                                edgecolor="none", zorder=9))


def veg(c, r, tok=endo, part=None):
    if part is None:
        ax.add_patch(Wedge(c, r, 180, 360, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.1, zorder=8))
    elif part == "dorsal":
        ax.add_patch(Wedge(c, r, 270, 360, facecolor=P.fill("drug"), edgecolor=P.edge("drug"), lw=1.1, zorder=8))
    else:
        ax.add_patch(Wedge(c, r, 180, 270, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.1, zorder=8))


bio.panel(ax, "A", (0.2, 9.4))
c = (3.0, 5.6)
r = 1.6
ax.add_patch(Wedge(c, r, 35, 145, facecolor=P.fill(ect), edgecolor=P.edge(ect), lw=1.1, zorder=8))
ax.add_patch(Wedge(c, r, -10, 35, facecolor=P.fill(mes), edgecolor=P.edge(mes), lw=1.1, zorder=8))
ax.add_patch(Wedge(c, r, 145, 190, facecolor=P.fill(mes), edgecolor=P.edge(mes), lw=1.1, zorder=8))
ax.add_patch(Wedge(c, r, 190, 350, facecolor=P.fill(endo), edgecolor=P.edge(endo), lw=1.1, zorder=8))
for a, txt, xy in [(90, "animal cap", (3.0, 8.0)), (10, "marginal zone", (5.6, 6.8)), (270, "vegetal mass", (3.0, 3.2))]:
    bio.label(ax, xy, txt, size="tiny", color=P.muted())
bio.arrow(ax, (3.9, 6.9), (6.8, 8.0), kind="process")
bio.arrow(ax, (3.9, 4.4), (6.8, 3.2), kind="process")
cap((8.0, 7.6), 0.9)
bio.label(ax, (9.4, 8.0), "→ epidermis", size="small", ha="left")
veg((8.0, 3.6), 0.9)
bio.label(ax, (9.4, 3.2), "→ endoderm", size="small", ha="left")
bio.label(ax, (8.0, 5.5), "cultured alone:\nno mesoderm", size="tiny", color=P.muted())

bio.panel(ax, "B", (12.0, 9.4))
cc = (14.0, 6.0)
cap((cc[0], cc[1] + 0.02), 1.1, label_cells=True)
veg((cc[0], cc[1] - 0.02), 1.1)
bio.label(ax, (14.0, 8.0), "animal cap (labelled)\n+ vegetal mass", size="tiny", color=P.muted())
bio.arrow(ax, (15.4, 6.0), (16.8, 6.0), kind="process")
ax.add_patch(Wedge((18.0, 6.0), 1.1, 0, 180, facecolor=P.fill(ect), edgecolor=P.edge(ect), lw=1.1, zorder=8))
ax.add_patch(Wedge((18.0, 6.0), 0.62, 0, 180, facecolor=P.fill(mes), edgecolor=P.edge(mes), lw=1.1, zorder=8.5))
for k in range(5):
    t = np.pi * (k + 0.5) / 5
    ax.add_patch(Circle((18.0 + 0.4 * np.cos(t), 6.0 + 0.3 * np.sin(t)), 0.07, facecolor=P.edge("protein"), edgecolor="none", zorder=9))
veg((18.0, 5.98), 1.1)
bio.label(ax, (19.4, 6.4), "mesoderm from\nlabelled animal cells", size="tiny", ha="left")

bio.panel(ax, "C", (12.0, 4.2))
for k, (part, txt) in enumerate([("dorsal", "dorsal vegetal → notochord, muscle"), ("ventral", "ventral vegetal → blood, mesenchyme")]):
    x = 14.0 + k * 0.0
    yy = 2.4 - 0.0
    cx = 13.8 + k * 5.0
    cap((cx, 2.5), 0.9, label_cells=True)
    veg((cx, 2.48), 0.9, part=part)
    bio.label(ax, (cx, 0.9), txt, size="tiny")
bio.label(ax, (21.8, 9.3), "lineage label", size="tiny", color=P.muted(), ha="right")
ax.add_patch(Circle((22.1, 9.3), 0.08, facecolor=P.edge("protein"), edgecolor="none"))
