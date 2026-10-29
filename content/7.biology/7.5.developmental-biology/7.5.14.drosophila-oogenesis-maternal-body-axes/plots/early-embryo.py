# The Drosophila life cycle at 25 C and the syncytial embryo. A: egg (about 0.5 mm), embryogenesis about 1 day,
# three larval instars (about 4 days), pupa (about 4 days), adult. B: the first 13 nuclear cycles are divisions of
# nuclei without cytokinesis; at cycle 8-9 the nuclei migrate to the cortex, the pole cells bud off at the posterior
# at cycle 9-10, and membranes enclose about 6000 nuclei during the long interphase of cycle 14 (cellularization).
import numpy as np
import wikibio as bio
from wikibio import development as D

fig, ax = bio.canvas(24.0, 9.6)
P = bio.P

# A: life cycle
bio.panel(ax, "A", (0.2, 9.4))
stages = [("dbcls/drosophila-egg", "Egg", (2.2, 6.4), 1.2), ("dbcls/drosophila-larva", "Larva (L1-L3)", (6.3, 7.4), 1.0),
          ("dbcls/drosophila-pupa", "Pupa", (6.3, 3.0), 1.4), ("dbcls/drosophila", "Adult", (2.2, 2.6), 1.9)]
bio.icon(ax, "dbcls/drosophila-egg", at=(2.2, 6.6), height=1.2)
bio.icon(ax, "dbcls/drosophila-larva", at=(6.4, 7.0), height=1.0)
bio.icon(ax, "dbcls/drosophila-pupa", at=(6.4, 2.9), height=1.4)
bio.icon(ax, "dbcls/drosophila", at=(2.2, 2.7), height=1.9)
for name, xy in [("Egg", (2.9, 6.6)), ("Larva (L1-L3)", (6.4, 8.0)), ("Pupa", (7.5, 2.9)), ("Adult", (2.2, 1.3))]:
    bio.label(ax, xy, name, size="small", bold=True, ha="left" if name in ("Egg", "Pupa") else "center")
bio.arrow(ax, (2.7, 7.4), (4.3, 7.4), kind="process", bend=-0.15)
bio.label(ax, (3.5, 8.0), "1 day", size="tiny", color=P.muted())
bio.arrow(ax, (6.6, 6.1), (6.6, 4.1), kind="process")
bio.label(ax, (7.5, 5.1), "4 days", size="tiny", color=P.muted())
bio.arrow(ax, (5.3, 2.5), (3.6, 2.3), kind="process", bend=-0.1)
bio.label(ax, (4.4, 1.6), "4 days", size="tiny", color=P.muted())
bio.arrow(ax, (1.6, 3.9), (1.6, 5.6), kind="process")
bio.label(ax, (2.5, 4.8), "mating,\negg laying", size="tiny", color=P.muted())
bio.label(ax, (4.3, 0.6), "about 10 days at 25 °C", size="small", color=P.muted())

# B: syncytial nuclear cycles
bio.panel(ax, "B", (9.6, 9.4))
rng = np.random.default_rng(1)
cols = [(11.8, "Cycle 2", "2 nuclei"), (16.0, "Cycle 8", "128 nuclei, migrating"),
        (20.2, "Cycle 10", "nuclei at the cortex,\npole cells"), (14.0, "Cycle 14", "cellular blastoderm,\nabout 6000 cells"),
        (19.8, "Gastrulation", "ventral furrow,\ngerm band")]
pos = [(11.9, 6.6), (16.0, 6.6), (20.4, 6.6), (14.0, 2.6), (19.8, 2.6)]
L, H = 3.6, 1.45
for k, ((x, title, sub), (cx, cy)) in enumerate(zip(cols, pos)):
    e = D.FlyEmbryo(ax, (cx, cy), L, H)
    if k == 0:
        for dx in (-0.25, 0.25):
            ax.add_patch(bio.core.Circle((cx + dx, cy), 0.08, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.6, zorder=14))
    elif k == 1:
        for _ in range(60):
            r, t = np.sqrt(rng.random()) * 0.72, rng.random() * 2 * np.pi
            ax.add_patch(bio.core.Circle((cx + r * L / 2 * np.cos(t) * 0.8, cy + r * H / 2 * np.sin(t) * 0.8), 0.05,
                                         facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.4, zorder=14))
    else:
        t = np.linspace(0, 2 * np.pi, 46 if k == 2 else 90, endpoint=False)
        for tt in t:
            ax.add_patch(bio.core.Circle((cx + 0.43 * L * np.cos(tt), cy + 0.4 * H * np.sin(tt)), 0.045 if k == 2 else 0.035,
                                         facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.3, zorder=14))
        if k >= 3:
            # cell membranes: a cortical layer
            from matplotlib.patches import Ellipse
            ax.add_patch(Ellipse((cx, cy), 0.8 * L, 0.72 * H, facecolor="none", edgecolor=P.edge("membrane"), lw=0.6, zorder=13))
        # pole cells
        for j in range(5):
            ax.add_patch(bio.core.Circle((cx + L / 2 + 0.08 + 0.05 * (j % 2), cy - 0.2 + 0.1 * j), 0.08, facecolor=P.fill("protein"),
                                         edgecolor=P.edge("protein"), lw=0.5, zorder=14))
        if k == 4:
            from matplotlib.patches import Ellipse
            ax.add_patch(Ellipse((cx - 0.1, cy - H / 2 + 0.1), 1.6, 0.18, facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=0.6, zorder=14))
    bio.label(ax, (cx, cy + H / 2 + 0.35), title, size="small", bold=True)
    bio.label(ax, (cx, cy - H / 2 - 0.55), sub, size="tiny", color=P.muted())
bio.arrow(ax, (13.75, 6.6), (14.15, 6.6), kind="process")
bio.arrow(ax, (18.0, 6.6), (18.4, 6.6), kind="process")
bio.arrow(ax, (18.9, 5.2), (15.8, 3.7), kind="process", bend=0.05)
bio.arrow(ax, (16.0, 2.6), (17.8, 2.6), kind="process")
bio.label(ax, (12.6, 0.6), "anterior left, dorsal up; pole cells (purple) are the germ line", size="tiny", color=P.muted(), ha="left")
