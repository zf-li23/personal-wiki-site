"""The G-protein switch in beta-adrenergic signaling, in four steps from left to right.
1: the unoccupied receptor (seven transmembrane helices) and the heterotrimeric G protein Gs
(alpha with bound GDP, beta-gamma; alpha and gamma lipid-anchored) are inactive.
2: epinephrine binds; the occupied receptor acts as a guanine nucleotide-exchange factor:
GDP leaves alpha and GTP (abundant in the cytosol) binds.
3: Gs-alpha-GTP separates from beta-gamma and activates adenylyl cyclase, which converts ATP to cAMP.
4: the intrinsic GTPase of alpha, accelerated by RGS proteins, hydrolyses GTP; alpha-GDP leaves the
cyclase and reassociates with beta-gamma, returning to state 1.
"""

import numpy as np
from matplotlib.patches import FancyBboxPatch
import wikibio as bio
from wikibio import cellbio as CB

P = bio.P
fig, ax = bio.canvas(25.0, 9.0)
y = 5.4
MH = CB.MH
CB.sides(ax, (0.2, 24.8), y, height=(3.4, 4.5), top="Extracellular", bottom=None)
bio.bilayer(ax, [(0.2, y), (24.8, y)])


def g_alpha(xy, nuc, active=False):
    tok = "channel" if not active else "positive"
    bio.protein(ax, xy, 1.05, 0.85, tok, text="α", size="normal")
    bio.molecule(ax, (xy[0] + 0.35, xy[1] - 0.45), token="atp" if nuc == "GTP" else "neutral", text=nuc, r=0.3, size=5.0, zorder=16)


def g_betagamma(xy):
    bio.protein(ax, xy, 0.85, 0.7, "protein", text="β", size="small")
    bio.protein(ax, (xy[0] + 0.62, xy[1] + 0.12), 0.5, 0.5, "metabolite", text="γ", size="small")


def cyclase(x):
    for k in range(2):
        xx = x + (k - 0.5) * 0.6
        ax.add_patch(FancyBboxPatch((xx - 0.22, y - MH - 0.1), 0.44, 2 * MH + 0.2, boxstyle="round,pad=0,rounding_size=0.12",
                                    facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=1.1, zorder=11))
    bio.protein(ax, (x, y - MH - 0.75), 1.4, 0.75, "enzyme", text="AC", size="small")


def epi(xy):
    bio.molecule(ax, xy, token="drug", text="Epi", r=0.28, size=5.0, zorder=16)


def step(x, n, text):
    bio.label(ax, (x, 8.45), f"{n}", size="title", bold=True)
    bio.label(ax, (x, 0.45), text, size="small", color=P.muted())


# 1 inactive
x = 3.0
bio.receptor(ax, x - 0.6, y, "gpcr", membrane_half=MH)
g_alpha((x + 0.9, y - MH - 0.6), "GDP")
g_betagamma((x + 0.9, y - MH - 1.55))
cyclase(x + 2.9)
step(x + 0.8, "1", "resting: Gαβγ·GDP")

# 2 ligand binding, exchange
x = 9.2
bio.receptor(ax, x - 0.6, y, "gpcr", membrane_half=MH)
epi((x - 0.6, y + MH + 0.45))
g_alpha((x + 0.9, y - MH - 0.6), "GTP")
g_betagamma((x + 0.9, y - MH - 1.55))
bio.molecule(ax, (x + 2.3, y - 1.4), token="neutral", text="GDP", r=0.3, size=5.0)
bio.arrow(ax, (x + 1.45, y - 1.25), (x + 1.95, y - 1.35), kind="process", head=0.15)
bio.molecule(ax, (x + 2.3, y - 3.1), token="atp", text="GTP", r=0.3, size=5.0)
bio.arrow(ax, (x + 2.0, y - 2.95), (x + 1.55, y - 1.4), kind="process", head=0.15, bend=-0.2)
step(x + 0.6, "2", "receptor acts as GEF")

# 3 alpha-GTP activates adenylyl cyclase
x = 15.2
bio.receptor(ax, x - 1.6, y, "gpcr", membrane_half=MH)
epi((x - 1.6, y + MH + 0.45))
g_betagamma((x - 1.0, y - MH - 0.75))
cyclase(x + 1.2)
g_alpha((x + 1.2, y - MH - 1.7), "GTP", active=True)
bio.molecule(ax, (x + 2.9, y - 1.0), token="atp", text="ATP", r=0.3, size=5.0)
bio.molecule(ax, (x + 2.9, y - 3.3), token="highlight", text="cAMP", r=0.36, size=5.0)
bio.arrow(ax, (x + 2.9, y - 1.35), (x + 2.9, y - 2.9), kind="process")
step(x + 0.4, "3", "Gsα·GTP stimulates adenylyl cyclase")

# 4 GTP hydrolysis
x = 21.4
cyclase(x + 1.4)
g_alpha((x - 0.3, y - MH - 1.9), "GDP")
bio.molecule(ax, (x + 0.9, y - 3.5), token="neutral", text="Pᵢ", r=0.25, size=5.0)
bio.arrow(ax, (x + 0.25, y - 2.9), (x + 0.7, y - 3.3), kind="process", head=0.14)
bio.protein(ax, (x - 1.5, y - 3.1), 0.9, 0.6, "drug", text="RGS", size="tiny")
bio.arrow(ax, (x - 1.25, y - 2.75), (x - 0.75, y - 2.45), kind="activation", bg=P.fill("cytoplasm"))
g_betagamma((x - 1.7, y - MH - 0.75))
bio.arrow(ax, (x - 0.6, y - 2.1), (x - 1.3, y - 1.45), kind="process", dashed=True)
step(x, "4", "GTPase (± RGS) ends the signal")

for a, b in ((4.9, 7.0), (11.2, 12.6), (18.1, 19.4)):
    bio.arrow(ax, (a, 8.45), (b, 8.45), kind="process")
bio.arrow(ax, (23.0, 1.35), (2.2, 1.35), kind="process", dashed=True, bend=0.0, color=P.muted())
bio.label(ax, (12.5, 1.62), "α·GDP reassociates with βγ", size="tiny", color=P.muted())
