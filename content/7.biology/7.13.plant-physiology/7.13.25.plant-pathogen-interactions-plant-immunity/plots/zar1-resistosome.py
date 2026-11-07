# Activation of the ZAR1 resistosome (Wang et al. 2019 Science; Bi et al. 2021 Cell).
# Inactive: ZAR1 (CC-NB-LRR) is held in an ADP-bound monomer together with the pseudokinase RKS1.
# The Xanthomonas effector AvrAC uridylylates the decoy kinase PBL2 (PBL2^UMP), which binds RKS1; ZAR1 exchanges
# ADP for (d)ATP, and five ZAR1-RKS1-PBL2^UMP units assemble into a wheel-like pentamer. The N-terminal alpha1
# helices of the five CC domains form a funnel that inserts into the plasma membrane; the resistosome is a
# Ca2+-permeable channel, and the Ca2+ influx triggers cell death (HR).
import math

import wikibio as bio
from wikibio import cellbio as CB

P = bio.P
fig, ax = bio.canvas(25.0, 11.0)

bio.panel(ax, "A", (0.3, 10.8))
bio.label(ax, (5.6, 10.4), "Recognition of a modified decoy", size="normal", bold=True)


def zar1(cx, cy, nuc, s=1.0):
    bio.protein(ax, (cx, cy + 0.75 * s), 0.9 * s, 0.6 * s, "receptor", text="CC", size="tiny")
    bio.protein(ax, (cx, cy), 1.2 * s, 0.75 * s, "enzyme", text="NB-ARC", size="tiny")
    bio.protein(ax, (cx + 1.05 * s, cy - 0.25 * s), 0.95 * s, 0.9 * s, "protein", text="LRR", size="tiny")
    bio.molecule(ax, (cx - 0.85 * s, cy - 0.35 * s), token="atp", text=nuc, r=0.33 * s, size="tiny")


zar1(1.6, 7.6, "ADP")
bio.protein(ax, (3.05, 6.6), 0.95, 0.65, "metabolite", text="RKS1", size="tiny")
bio.label(ax, (2.2, 5.6), "inactive ZAR1-RKS1", size="small")
# AvrAC + PBL2
bio.protein(ax, (6.6, 8.8), 1.1, 0.6, "negative", text="AvrAC", size="tiny")
bio.protein(ax, (6.6, 7.2), 1.0, 0.65, "neutral", text="PBL2", size="tiny")
bio.arrow(ax, (6.6, 8.45), (6.6, 7.6), kind="catalysis")
bio.label(ax, (7.3, 8.05), "uridylylation", size="tiny", ha="left")
bio.molecule(ax, (7.35, 6.85), token="highlight", text="UMP", r=0.3, size="tiny")
bio.label(ax, (6.6, 6.2), "PBL2ᵁᴹᴾ (decoy)", size="small")
bio.arrow(ax, (3.8, 5.0), (9.4, 5.0), kind="process", bend=0.0)
bio.label(ax, (6.6, 4.55), "PBL2ᵁᴹᴾ binds RKS1; ADP → dATP exchange", size="tiny")

# pentamer top view
cx, cy = 12.2, 7.5
for k in range(5):
    a = math.pi / 2 + 2 * math.pi * k / 5
    x, y = cx + 1.2 * math.cos(a), cy + 1.2 * math.sin(a)
    bio.protein(ax, (x, y), 0.95, 0.95, "enzyme")
    x2, y2 = cx + 2.05 * math.cos(a), cy + 2.05 * math.sin(a)
    bio.protein(ax, (x2, y2), 0.6, 0.45, "metabolite")
bio.protein(ax, (cx, cy), 0.75, 0.75, "receptor")
bio.label(ax, (cx, cy - 2.75), "ZAR1 resistosome (pentamer, top view)", size="small")
bio.callout(ax, (cx + 1.95 * math.cos(math.pi / 2), cy + 2.0), (9.7, 10.0), "RKS1-PBL2ᵁᴹᴾ")
bio.callout(ax, (cx, cy + 0.1), (14.7, 9.4), "α1 funnel")

# B: membrane side view
bio.panel(ax, "B", (16.0, 10.8))
bio.label(ax, (20.5, 10.4), "A Ca²⁺-permeable channel", size="normal", bold=True)
ym = 6.6
CB.sides(ax, (16.2, 24.8), ym, height=(3.0, 5.6), top="Apoplast", bottom="Cytoplasm", label_x=16.4)
bio.bilayer(ax, [(16.2, ym), (24.8, ym)])
x0 = 20.5
for side in (-1, 1):
    for j in range(2):
        xx = x0 + side * (0.35 + 0.55 * j)
        ax.add_patch(__import__("matplotlib").patches.FancyBboxPatch((xx - 0.13, ym - 0.5), 0.26, 1.3,
                     boxstyle="round,pad=0,rounding_size=0.12", facecolor=P.fill("receptor"),
                     edgecolor=P.edge("receptor"), lw=1.1, zorder=12))
    bio.protein(ax, (x0 + side * 1.0, ym - 1.4), 1.3, 0.9, "enzyme", text="NB-ARC", size="tiny")
    bio.protein(ax, (x0 + side * 1.4, ym - 2.6), 1.2, 0.95, "protein", text="LRR", size="tiny")
    bio.protein(ax, (x0 + side * 2.6, ym - 2.9), 0.9, 0.7, "metabolite", text="RKS1", size="tiny")
for k in range(3):
    bio.ion(ax, (x0, ym + 2.0 - 0.6 * k), "ca", r=0.17, text=False, zorder=16)
bio.arrow(ax, (x0, ym + 0.6), (x0, ym - 3.2), kind="process", zorder=17)
bio.label(ax, (x0 + 0.35, ym + 2.0), "Ca²⁺", size="small", ha="left")
bio.label(ax, (x0, 0.6), "[Ca²⁺]cyt rises → ROS, transcription, cell death (HR)", size="small")
bio.callout(ax, (x0 + 0.9, ym + 0.6), (23.4, ym + 1.6), "α1 funnel")
