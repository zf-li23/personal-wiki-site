"""Classes of membrane transport proteins.

Passive (down the electrochemical gradient): a uniporter (GLUT1: glucose), an antiporter that
exchanges anions electroneutrally (AE1 of erythrocytes: Cl- in, HCO3- out in the tissues) and an
ion channel (K+). Secondary active: a symporter using the Na+ gradient (SGLT1: 2 Na+ with one
glucose, glucose moving uphill). Primary active: a P-type ATPase (Na+/K+-ATPase, phosphorylated on
an Asp residue in each cycle), a rotary V-type ATPase (H+ into vacuoles and lysosomes; the F-type
ATP synthase has the same architecture and normally runs backwards) and an ABC transporter (two
transmembrane domains and two nucleotide-binding domains, here exporting a drug). Cytosol below.
"""

import numpy as np
from matplotlib.patches import Ellipse, FancyBboxPatch
import wikibio as bio
from wikibio import cellbio as CB

P = bio.P
fig, ax = bio.canvas(27.0, 9.4)
y = 4.9
MH = CB.MH
CB.sides(ax, (0.2, 26.8), y, height=(3.6, 3.1), top="Extracellular / lumen", bottom="Cytosol")
bio.bilayer(ax, [(0.2, y), (26.8, y)])
LW = bio.core.LINE


def title(x, a, b):
    bio.label(ax, (x, 8.05), a, size="small", bold=True)
    bio.label(ax, (x, 7.65), b, size="tiny", color=P.muted())


def glc(xy):
    bio.molecule(ax, xy, token="carbohydrate", text="Glc", r=0.24, size=5.2, zorder=18)


# uniport
x = 1.9
title(x, "Uniporter", "GLUT1")
site = CB.carrier(ax, x, y, open="out")
bio.arrow(ax, (x, 6.7), (x, 2.9), kind="process", zorder=16)
glc((x + 0.45, 6.85))
glc((x + 0.45, 2.75))

# symport
x = 12.5
title(x, "Symporter", "SGLT1 (secondary active)")
CB.carrier(ax, x, y, open="out", token="receptor", width=1.45)
bio.arrow(ax, (x - 0.35, 6.7), (x - 0.35, 2.9), kind="process", zorder=16)
bio.arrow(ax, (x + 0.35, 6.7), (x + 0.35, 2.9), kind="process", zorder=16)
for yy in (6.8, 7.2):
    bio.ion(ax, (x - 0.75, yy), "na", r=0.15, text=False)
bio.label(ax, (x - 1.0, 7.0), "2 Na⁺", size="tiny", ha="right")
glc((x + 0.8, 6.9))
bio.label(ax, (x + 0.8, 2.4), "glucose uphill", size="tiny", color=P.muted())

# antiport
x = 5.3
title(x, "Antiporter", "AE1 (Cl⁻/HCO₃⁻)")
CB.carrier(ax, x, y, open="out", token="enzyme", width=1.45)
bio.arrow(ax, (x - 0.35, 6.7), (x - 0.35, 2.9), kind="process", zorder=16)
bio.arrow(ax, (x + 0.35, 2.9), (x + 0.35, 6.7), kind="process", zorder=16)
bio.ion(ax, (x - 0.75, 6.85), "cl", r=0.15, text=False)
bio.label(ax, (x - 1.0, 6.85), "Cl⁻", size="tiny", ha="right")
bio.molecule(ax, (x + 0.85, 2.75), token="metabolite", text="HCO₃⁻", r=0.3, size=4.8)

# channel
x = 8.8
title(x, "Channel", "K⁺ channel")
CB.channel(ax, x, y)
bio.arrow(ax, (x, 2.9), (x, 6.7), kind="process", zorder=16)
for yy in (2.6, 3.6, y, 6.2):
    bio.ion(ax, (x + (0.0 if abs(yy - y) < 0.1 else 0.32), yy), "k", r=0.15, text=False, zorder=17)
bio.label(ax, (x + 0.55, 2.6), "K⁺", size="tiny", ha="left")

# P-type
x = 15.9
title(x, "P-type ATPase", "Na⁺/K⁺-ATPase")
atp = CB.pump(ax, x, y, width=1.6)
bio.arrow(ax, (x - 0.55, 2.9), (x - 0.55, 6.7), kind="process", zorder=16)
bio.arrow(ax, (x - 0.05, 6.7), (x - 0.05, 2.9), kind="process", zorder=16)
for k in range(3):
    bio.ion(ax, (x - 0.95, 6.5 + 0.33 * k), "na", r=0.14, text=False)
bio.label(ax, (x - 1.2, 6.85), "3 Na⁺", size="tiny", ha="right")
for k in range(2):
    bio.ion(ax, (x + 0.3, 2.65 + 0.33 * k), "k", r=0.14, text=False)
bio.label(ax, (x + 0.55, 2.8), "2 K⁺", size="tiny", ha="left")
bio.molecule(ax, atp + (0.25, 0.2), token="atp", text="ATP", r=0.26, size=5.0)

# V-type rotary pump
x = 20.0
title(x, "V-type ATPase", "H⁺ into vacuole / lysosome")
ring = Ellipse((x, y), 1.9, 2 * MH + 0.3, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=LW, zorder=12)
ax.add_patch(ring)
for k in range(6):
    xx = x - 0.75 + k * 0.3
    ax.plot([xx, xx], [y - MH, y + MH], color=P.light("channel"), lw=LW * 1.2, zorder=12.5)
ax.add_patch(FancyBboxPatch((x - 0.12, y - MH - 1.1), 0.24, 1.0, boxstyle="round,pad=0,rounding_size=0.1",
                            facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=LW * 0.8, zorder=12))
for dx in (-0.55, 0.0, 0.55):
    bio.protein(ax, (x + dx, y - MH - 1.55), 0.62, 0.75, "enzyme", wobble=0.05, text=None)
ax.add_patch(FancyBboxPatch((x + 1.0, y - MH - 1.4), 0.18, 2.0, boxstyle="round,pad=0,rounding_size=0.08",
                            facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=LW * 0.8, zorder=11.5))
bio.arrow(ax, (x - 1.25, 2.9), (x - 1.25, 6.7), kind="process", zorder=16)
bio.ion(ax, (x - 1.6, 2.75), "h", r=0.14, text=False)
bio.label(ax, (x - 1.85, 2.75), "H⁺", size="tiny", ha="right")
bio.arrow(ax, (x + 0.95, 5.55), (x + 0.4, 5.55), kind="process", head=0.13, bend=0.0, zorder=16)
bio.molecule(ax, (x + 0.05, 2.15), token="atp", text="ATP", r=0.26, size=5.0)
bio.label(ax, (x, 6.35), "rotor", size="tiny", color=P.muted())

# ABC transporter
x = 24.4
title(x, "ABC transporter", "MDR1 (drug export)")
CB.carrier(ax, x, y, open="out", token="drug", width=1.5)
for dx in (-0.45, 0.45):
    bio.protein(ax, (x + dx, y - MH - 0.9), 0.75, 0.7, "drug", wobble=0.06)
bio.molecule(ax, (x - 0.45, y - MH - 0.9), token="atp", text="ATP", r=0.22, size=4.6, zorder=18)
bio.molecule(ax, (x + 0.45, y - MH - 0.9), token="atp", text="ATP", r=0.22, size=4.6, zorder=18)
bio.arrow(ax, (x + 1.25, 2.9), (x + 1.25, 6.7), kind="process", zorder=16)
bio.molecule(ax, (x + 1.25, 7.0), token="metabolite", text="drug", r=0.27, size=4.6)
bio.label(ax, (x, 2.3), "2 NBDs", size="tiny", color=P.muted())

for (x0, x1), text, tok in (((0.6, 10.0), "Passive", "positive"), ((10.9, 14.0), "Secondary active", "highlight"),
                            ((14.8, 26.3), "Primary active (ATP hydrolysis)", "negative")):
    yy = 1.05
    ax.plot([x0, x0, x1, x1], [yy + 0.15, yy, yy, yy + 0.15], color=P.edge(tok), lw=1.1)
    bio.label(ax, ((x0 + x1) / 2, yy - 0.32), text, size="small", color=P.edge(tok), bold=True)
