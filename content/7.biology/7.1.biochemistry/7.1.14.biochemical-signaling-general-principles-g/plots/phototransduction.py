"""Phototransduction in the outer segment of a vertebrate rod cell.

Top: the membrane of a disk (disk lumen above). A photon isomerizes 11-cis-retinal in rhodopsin;
activated rhodopsin (R*) catalyses GDP/GTP exchange on many molecules of transducin; transducin-alpha-GTP
removes the inhibitory gamma subunits of cGMP phosphodiesterase (PDE6), which hydrolyses cGMP to
5'-GMP. Bottom: the plasma membrane (extracellular space below). In the dark, cGMP holds
cGMP-gated cation channels open (the dark current carries Na+ and Ca2+ in); when [cGMP] falls they
close, while the Na+/Ca2+,K+ exchanger (NCKX: 4 Na+ in, 1 Ca2+ and 1 K+ out) keeps exporting Ca2+, so
the cell hyperpolarizes and [Ca2+] falls. Recovery: rhodopsin kinase (GRK1) phosphorylates R* and
arrestin caps it; the GTPase of transducin, accelerated by RGS9, ends PDE activation; the fall of
[Ca2+] releases Ca2+ from guanylyl-cyclase-activating proteins (GCAPs), which then stimulate guanylyl
cyclase (GC) to restore cGMP (negative feedback).
"""

import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle
import wikibio as bio
from wikibio import cellbio as CB

P = bio.P
fig, ax = bio.canvas(22.0, 11.0)
yd, yp = 7.6, 2.4
MH = CB.MH
ax.add_patch(Rectangle((0.2, yd + MH), 21.6, 2.9, facecolor=P.fill("vacuole"), edgecolor="none", zorder=0))
ax.add_patch(Rectangle((0.2, yp + MH), 21.6, yd - yp - 2 * MH, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=0))
ax.add_patch(Rectangle((0.2, 0.2), 21.6, yp - MH - 0.2, facecolor=P.fill("extracellular"), edgecolor="none", zorder=0))
bio.bilayer(ax, [(0.2, yd), (21.8, yd)])
bio.bilayer(ax, [(0.2, yp), (21.8, yp)])
bio.label(ax, (6.0, 10.25), "Disk lumen", size="small", bold=True, ha="left", color=P.muted())
bio.label(ax, (0.5, 3.4), "Cytosol (outer segment)", size="small", bold=True, ha="left", color=P.muted())
bio.label(ax, (0.5, 0.55), "Extracellular", size="small", bold=True, ha="left", color=P.muted())

# photon and rhodopsin
x = 2.6
bio.receptor(ax, x, yd, "gpcr", membrane_half=MH)
t = np.linspace(0, 1, 200)
ax.plot(x - 1.6 + 1.4 * t, 10.3 - 2.0 * t + 0.12 * np.sin(2 * np.pi * 6 * t), color=P.edge("highlight"), lw=1.6, zorder=16)
bio.arrow(ax, (x - 0.3, 8.45), (x - 0.12, 8.2), kind="process", color=P.edge("highlight"), head=0.18)
bio.label(ax, (x - 1.7, 10.5), "hν", size="normal", bold=True)
bio.label(ax, (x, yd - 0.85), "R*", size="small", bold=True)
bio.label(ax, (x + 0.5, yd + 0.85), "11-cis → all-trans retinal", size="tiny", ha="left")

# transducin
x = 5.6
bio.protein(ax, (x, yd - MH - 0.55), 1.0, 0.75, "positive", text="Tα", size="small")
bio.molecule(ax, (x + 0.55, yd - MH - 0.95), token="atp", text="GTP", r=0.26, size=4.6, zorder=16)
bio.protein(ax, (x - 0.25, yd - MH - 1.75), 0.9, 0.6, "protein", text="Tβγ", size="tiny")
bio.arrow(ax, (3.3, yd - 0.9), (4.9, yd - 0.9), kind="catalysis", bg=P.fill("cytoplasm"))
bio.label(ax, (4.1, yd - 1.25), "GTP/GDP exchange\non ~10²–10³ Tα", size="tiny", color=P.muted())

# PDE6
x = 9.0
ax.add_patch(FancyBboxPatch((x - 0.12, yd - MH - 0.05), 0.24, MH + 0.05, boxstyle="round,pad=0,rounding_size=0.08",
                            facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=1.0, zorder=11))
bio.protein(ax, (x, yd - MH - 0.65), 1.5, 0.85, "enzyme", text="PDE6", size="small")
bio.protein(ax, (x + 1.15, yd - MH - 1.45), 0.5, 0.4, "negative", text="γ", size="tiny")
bio.arrow(ax, (6.2, yd - MH - 0.55), (8.15, yd - MH - 0.6), kind="activation", bg=P.fill("cytoplasm"))
bio.label(ax, (x + 1.6, yd - MH - 1.45), "inhibitory γ removed", size="tiny", ha="left", color=P.muted())
bio.molecule(ax, (x - 0.8, 4.9), token="highlight", text="cGMP", r=0.33, size=4.8)
bio.molecule(ax, (x + 1.0, 4.9), token="neutral", text="GMP", r=0.3, size=4.8)
bio.arrow(ax, (x - 0.4, 4.9), (x + 0.6, 4.9), kind="process", head=0.16)
bio.arrow(ax, (x, yd - MH - 1.1), (x + 0.1, 5.05), kind="catalysis", bg=P.fill("cytoplasm"))

# CNG channel on the plasma membrane
x = 12.6
CB.channel(ax, x, yp, token="channel")
ax.plot([x - 0.25, x + 0.25], [yp + 0.05, yp + 0.05], color=P.edge("negative"), lw=3.0, zorder=14)
for k, xx in enumerate((x - 0.8, x - 0.3, x + 0.3)):
    bio.molecule(ax, (xx, yp + MH + 0.55 + 0.25 * (k % 2)), token="highlight", text="", r=0.14, zorder=15)
bio.label(ax, (x, yp + MH + 1.3), "cGMP falls: channel closes", size="tiny")
bio.label(ax, (x, yp - MH - 0.45), "CNG channel", size="small", bold=True)
bio.ion(ax, (x - 0.35, yp - MH - 1.05), "na", r=0.13, text=False)
bio.ion(ax, (x + 0.05, yp - MH - 1.05), "ca", r=0.13, text=False)
bio.label(ax, (x - 0.6, yp - MH - 1.05), "dark current blocked", size="tiny", ha="right", color=P.muted())

# NCKX exchanger
x = 16.6
CB.carrier(ax, x, yp, open="in", token="receptor", width=1.4)
bio.arrow(ax, (x - 0.3, 0.9), (x - 0.3, 4.0), kind="process", zorder=16)
bio.arrow(ax, (x + 0.3, 4.0), (x + 0.3, 0.9), kind="process", zorder=16)
bio.ion(ax, (x - 0.7, 0.95), "na", r=0.13, text=False)
bio.label(ax, (x - 0.9, 0.95), "4 Na⁺", size="tiny", ha="right")
bio.ion(ax, (x + 0.7, 4.0), "ca", r=0.13, text=False)
bio.ion(ax, (x + 0.7, 3.65), "k", r=0.13, text=False)
bio.label(ax, (x + 0.95, 3.85), "Ca²⁺ + K⁺ out", size="tiny", ha="left")
bio.label(ax, (x, yp - MH - 0.45), "NCKX", size="small", bold=True)

# guanylyl cyclase and GCAP on the disk
x = 19.4
ax.add_patch(FancyBboxPatch((x - 0.13, yd - MH - 0.1), 0.26, 2 * MH + 0.2, boxstyle="round,pad=0,rounding_size=0.08",
                            facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=1.0, zorder=11))
bio.protein(ax, (x, yd - MH - 0.7), 1.2, 0.8, "enzyme", text="GC", size="small")
bio.protein(ax, (x + 1.25, yd - MH - 1.35), 0.8, 0.55, "ca", text="GCAP", size="tiny")
bio.arrow(ax, (x + 1.0, yd - MH - 1.1), (x + 0.55, yd - MH - 0.85), kind="activation", bg=P.fill("cytoplasm"))
bio.molecule(ax, (x - 0.5, 4.9), token="atp", text="GTP", r=0.3, size=4.8)
bio.molecule(ax, (x + 0.8, 4.9), token="highlight", text="cGMP", r=0.33, size=4.8)
bio.arrow(ax, (x - 0.15, 4.9), (x + 0.42, 4.9), kind="process", head=0.16)
bio.arrow(ax, (x, yd - MH - 1.15), (x + 0.1, 5.05), kind="catalysis", bg=P.fill("cytoplasm"))
bio.arrow(ax, (17.7, 3.9), (20.6, yd - MH - 1.7), kind="activation", dashed=True, bend=-0.12, bg=P.fill("cytoplasm"))
bio.label(ax, (20.0, 3.55), "[Ca²⁺] falls:\nGCAP activates GC", size="tiny", color=P.muted())

# shutoff of R*
bio.protein(ax, (2.0, 5.2), 1.0, 0.6, "drug", text="GRK1", size="tiny")
bio.protein(ax, (3.4, 5.2), 1.1, 0.6, "antibody", text="arrestin", size="tiny")
bio.arrow(ax, (2.3, 5.55), (2.5, yd - MH - 0.25), kind="inhibition")
bio.label(ax, (2.7, 4.6), "shutoff of R*", size="tiny", color=P.muted())
