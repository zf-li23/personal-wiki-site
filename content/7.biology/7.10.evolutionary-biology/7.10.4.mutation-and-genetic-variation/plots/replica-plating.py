"""The replica-plating experiment of Joshua and Esther Lederberg (1952), which shows that mutations
for resistance arise before exposure to the selective agent. A master plate carries colonies grown from
a single sensitive cell of E. coli. A velvet pad transfers cells of every colony, in the same positions,
to replica plates containing phage T1. Top: if the phage induced resistance mutations (directed
mutation), surviving colonies would appear at different positions on different replicas. Bottom: if
resistance mutations arose at random before exposure, the resistant cells are already in particular
colonies of the master plate, and survivors appear at the same positions on every replica, as observed."""
import numpy as np
from matplotlib.patches import Circle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22.4, 13)
rng = np.random.default_rng(7)
ang = rng.uniform(0, 2 * np.pi, 34)
rad = 1.55 * np.sqrt(rng.uniform(0.02, 1, 34))
COL = np.c_[rad * np.cos(ang), rad * np.sin(ang)]
RESIST = [4, 17, 25]


def plate(c, survivors=None, label=None, phage=False, all_colonies=True):
    kw = dict(alpha=0.35) if phage else {}
    ax.add_patch(Circle(c, 2.0, facecolor=P.fill("virus") if phage else P.fill("extracellular"),
                        edgecolor=P.edge("neutral"), lw=1.2, zorder=3, **kw))
    ax.add_patch(Circle(c, 2.0, fill=False, edgecolor=P.edge("neutral"), lw=1.2, zorder=4))
    for k, (x, y) in enumerate(COL):
        if all_colonies:
            ax.add_patch(Circle((c[0] + x, c[1] + y), 0.13, facecolor=P.fill("bacterium"), edgecolor=P.edge("bacterium"),
                                lw=0.6, zorder=5))
        elif survivors is not None and k in survivors:
            ax.add_patch(Circle((c[0] + x, c[1] + y), 0.16, facecolor=P.fill("positive"), edgecolor=P.edge("positive"),
                                lw=0.8, zorder=5))
    if label:
        bio.label(ax, (c[0], c[1] - 2.45), label, size="small")


for row, (y, title, sets) in enumerate(((9.4, "Hypothesis 1: phage induces resistance (directed mutation)",
                                         ([2, 11, 30], [8, 21, 27], [5, 14, 33])),
                                        (3.2, "Hypothesis 2: resistance mutations arise at random beforehand (observed)",
                                         (RESIST, RESIST, RESIST)))):
    bio.label(ax, (0.4, y + 2.75), title, size="small", bold=True, ha="left")
    plate((2.6, y), label="master plate")
    if row == 1:
        for k in RESIST:
            x, yy = COL[k]
            ax.add_patch(Circle((2.6 + x, y + yy), 0.22, fill=False, edgecolor=P.edge("positive"), lw=1.2, zorder=6))
    bio.arrow(ax, (4.9, y), (7.3, y), kind="process", color=P.muted())
    bio.label(ax, (6.1, y + 0.45), "velvet pad", size="tiny", color=P.muted())
    for j, s in enumerate(sets):
        plate((9.8 + 5.0 * j, y), survivors=s, label=f"replica {j + 1} + phage T1", phage=True, all_colonies=False)
bio.label(ax, (2.6, 0.35), "green rings: colonies that already contain resistant mutants", size="tiny", color=P.muted())
