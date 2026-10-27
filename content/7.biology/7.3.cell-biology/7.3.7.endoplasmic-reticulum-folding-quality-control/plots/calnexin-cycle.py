# Glycoprotein quality control in the ER. Lumen above the ER membrane, cytosol below. Trimming of two
# glucoses gives Glc1Man9, bound by calnexin/calreticulin (with the oxidoreductase ERp57). Glucosidase II
# removes the last glucose and releases the protein: a folded protein leaves the ER (cargo receptors,
# COPII); an incompletely folded one is re-glucosylated by UGGT, the folding sensor, and rebinds. Slow
# mannose trimming (ER mannosidase I, EDEMs) acts as a timer: Man7-5 glycans are read by OS-9/XTP3-B,
# the protein is retrotranslocated through the Hrd1-Sel1L complex, ubiquitinated, pulled out by p97
# (Cdc48), deglycosylated by N-glycanase and degraded by the proteasome.
import numpy as np
import wikibio as bio
from wikibio import traffic as T

fig, ax = bio.canvas(19, 10)
P = bio.P
my = 2.6
ax.add_patch(bio.core.FancyBboxPatch((0.2, my + T.MT / 2), 18.6, 7.1, boxstyle="round,pad=0,rounding_size=0.3",
                                     facecolor=P.fill("er"), edgecolor="none", alpha=0.35, zorder=0))
T.band(ax, [(0.2, my), (18.8, my)], zorder=3)
bio.label(ax, (0.5, 9.35), "ER lumen", size="small", bold=True, ha="left", color=P.muted())
bio.label(ax, (0.5, 0.45), "Cytosol", size="small", bold=True, ha="left", color=P.muted())

W, H = 3.2, 0.95
nodes = {
    "new": ((2.2, 7.9), "Glc3Man9 glycoprotein\n(from Sec61 + OST)", "neutral"),
    "cnx": ((7.0, 7.9), "Glc1Man9 · calnexin /\ncalreticulin · ERp57", "enzyme"),
    "rel": ((7.0, 4.9), "Man9, released", "protein"),
    "fold": ((12.2, 7.9), "Folded: exit\n(ERGIC-53, COPII)", "positive"),
    "erad": ((12.2, 4.4), "Man7–5: OS-9 / XTP3-B\n→ Hrd1–Sel1L", "negative"),
}
for k, (xy, txt, t) in nodes.items():
    bio.box(ax, xy, W, H, token=t, text=txt, size="small")
bio.arrow(ax, (3.7, 7.9), (5.5, 7.9), kind="process")
bio.label(ax, (4.6, 8.35), "glucosidase I, II", size="tiny")
bio.arrow(ax, (6.4, 7.4), (6.4, 5.4), kind="process")
bio.label(ax, (6.25, 6.4), "glucosidase II", size="tiny", ha="right")
bio.arrow(ax, (7.6, 5.4), (7.6, 7.4), kind="process")
bio.label(ax, (7.75, 6.65), "UGGT (+UDP-Glc)\nif still unfolded", size="tiny", ha="left")
bio.label(ax, (7.75, 6.0), "folding sensor", size="tiny", ha="left", color=P.muted())
bio.arrow(ax, (8.5, 5.2), (10.7, 7.55), kind="process", bend=-0.15)
bio.label(ax, (10.3, 6.15), "if folded", size="tiny", ha="left")
bio.arrow(ax, (8.5, 4.75), (10.7, 4.5), kind="process", dashed=True)
bio.label(ax, (9.6, 4.15), "slow: ER Man I, EDEMs\n(the timer)", size="tiny")
bio.arrow(ax, (13.7, 7.9), (16.3, 7.9), kind="process")
bio.label(ax, (17.5, 7.9), "to the\nGolgi", size="small")

# retrotranslocation through the membrane
hx = 14.6
bio.protein(ax, (hx, my), 0.9, 0.85, "enzyme", text="Hrd1")
bio.arrow(ax, (13.7, 4.1), (hx - 0.1, my + 0.5), kind="process", bend=0.1)
path = np.c_[np.linspace(hx + 0.5, hx + 2.4, 60), my - 0.9 - 0.25 * np.sin(np.linspace(0, 9, 60))]
ax.plot(path[:, 0], path[:, 1], color=P.edge("protein"), lw=1.6, zorder=8)
ax.plot([hx + 0.5, hx + 0.5], [my + 0.3, my - 0.9], color=P.edge("protein"), lw=1.6, zorder=11)
for k in range(4):
    bio.ion(ax, (hx + 0.55 + 0.27 * k, my - 0.35), "h", r=0.11, text=False)
bio.label(ax, (hx + 1.55, my - 0.35), "Ub", size="tiny", ha="left")
bio.box(ax, (hx - 1.6, my - 1.1), 1.4, 0.6, token="neutral", text="p97/Cdc48", size="tiny")
bio.arrow(ax, (hx - 0.9, my - 1.1), (hx + 0.45, my - 0.95), kind="catalysis", head=0.16)
bio.box(ax, (hx + 3.3, my - 1.0), 1.5, 0.75, token="neutral", text="Proteasome", size="tiny")
bio.arrow(ax, (hx + 2.4, my - 0.95), (hx + 2.5, my - 0.98), kind="process")
bio.label(ax, (hx + 1.3, my - 1.75), "N-glycanase removes the glycan", size="tiny", color=P.muted())
