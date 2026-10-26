"""The Post-Albers cycle of the Na+/K+-ATPase (a P-type ATPase).

Four states, clockwise from the lower left. E1 (ion sites open to the cytosol, high affinity for Na+,
ATP bound) binds 3 Na+; phosphoryl transfer from ATP to the conserved Asp residue occludes them
(E1-P(3Na), ADP released). The conformational change to E2-P opens the sites to the outside with low
affinity for Na+, so 3 Na+ leave and 2 K+ bind; this triggers dephosphorylation (Pi released) and
occludes the K+ ions (E2(2K)). Binding of ATP converts E2 back to E1 and releases 2 K+ into the
cytosol. Net per cycle: 3 Na+ out, 2 K+ in, one ATP hydrolysed, one positive charge moved out.
Outside is up in each panel.
"""

import numpy as np
from matplotlib.patches import FancyBboxPatch
import wikibio as bio
from wikibio import cellbio as CB

P = bio.P
fig, ax = bio.canvas(19.0, 13.0)
LW = bio.core.LINE
MH = CB.MH
tok = "enzyme"


def strip(cx, cy, w=5.2):
    CB.sides(ax, (cx - w / 2, cx + w / 2), cy, height=(1.5, 1.5), top=None, bottom=None)
    bio.bilayer(ax, [(cx - w / 2, cy), (cx + w / 2, cy)])


def occluded(cx, cy):
    for side in (-1, 1):
        h = 2 * MH + 0.45
        ax.add_patch(FancyBboxPatch((cx + side * 0.33 - 0.33, cy - h / 2), 0.66, h, boxstyle="round,pad=0,rounding_size=0.2",
                                    facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LW * 0.9, zorder=11))


def phospho(cx, cy):
    bio.molecule(ax, (cx + 0.55, cy - MH - 0.45), token="highlight", text="P", r=0.2, size=6.5, zorder=19)


def ions(kind, pts):
    for p in pts:
        bio.ion(ax, p, kind, r=0.14, text=False, zorder=18)


def state(cx, cy, name, sub):
    bio.label(ax, (cx, cy + 2.75), name, size="normal", bold=True)
    bio.label(ax, (cx, cy + 2.35), sub, size="tiny", color=P.muted())


# lower left: E1 inward open, ATP bound, 3 Na+ binding
c1 = (4.2, 3.2)
strip(*c1)
CB.carrier(ax, c1[0], c1[1], open="in", token=tok, width=1.5)
ions("na", [(c1[0] - 0.2, c1[1] - 0.15), (c1[0] + 0.2, c1[1] - 0.15), (c1[0], c1[1] - 0.45)])
bio.molecule(ax, (c1[0] + 1.25, c1[1] - 0.95), token="atp", text="ATP", r=0.28, size=5.2, zorder=19)
state(*c1, "E1·ATP", "sites face the cytosol; high Na⁺ affinity")

# upper left: E1-P occluded with 3 Na+
c2 = (4.2, 9.6)
strip(*c2)
occluded(*c2)
ions("na", [(c2[0], c2[1] + 0.22), (c2[0] - 0.0, c2[1] - 0.12), (c2[0], c2[1] - 0.46)])
phospho(*c2)
state(*c2, "E1–P(3Na⁺)", "Asp phosphorylated; Na⁺ occluded")

# upper right: E2-P outward open, Na+ leaving, K+ arriving
c3 = (14.8, 9.6)
strip(*c3)
CB.carrier(ax, c3[0], c3[1], open="out", token=tok, width=1.5)
phospho(*c3)
ions("na", [(c3[0] - 1.6, c3[1] + 1.15), (c3[0] - 1.25, c3[1] + 1.35), (c3[0] - 0.9, c3[1] + 1.15)])
ions("k", [(c3[0] + 1.05, c3[1] + 1.25), (c3[0] + 1.4, c3[1] + 1.25)])
bio.arrow(ax, (c3[0] - 0.25, c3[1] + 0.35), (c3[0] - 0.8, c3[1] + 0.95), kind="process", head=0.16)
bio.arrow(ax, (c3[0] + 0.95, c3[1] + 1.0), (c3[0] + 0.3, c3[1] + 0.4), kind="process", head=0.16)
bio.label(ax, (c3[0] - 1.25, c3[1] + 1.65), "3 Na⁺ out", size="tiny")
bio.label(ax, (c3[0] + 1.25, c3[1] + 1.6), "2 K⁺ in", size="tiny")
state(*c3, "E2–P", "sites face outside; low Na⁺, high K⁺ affinity")

# lower right: E2 occluded with 2 K+
c4 = (14.8, 3.2)
strip(*c4)
occluded(*c4)
ions("k", [(c4[0], c4[1] + 0.12), (c4[0], c4[1] - 0.25)])
state(*c4, "E2(2K⁺)", "dephosphorylated; K⁺ occluded")

# cycle arrows with exchanged species
bio.arrow(ax, (3.1, 6.4), (3.1, 7.5), kind="process")
bio.label(ax, (2.9, 6.95), "3 Na⁺ bind\nATP → ADP", size="small", ha="right")
bio.arrow(ax, (7.3, 10.7), (11.7, 10.7), kind="process")
bio.label(ax, (9.5, 11.05), "E1–P → E2–P", size="small")
bio.label(ax, (9.5, 10.35), "Na⁺ released outside", size="tiny", color=P.muted())
bio.arrow(ax, (15.9, 7.5), (15.9, 6.4), kind="process")
bio.label(ax, (16.1, 6.95), "2 K⁺ bind\nPᵢ released", size="small", ha="left")
bio.arrow(ax, (11.7, 2.1), (7.3, 2.1), kind="process")
bio.label(ax, (9.5, 2.45), "ATP binds: E2 → E1", size="small")
bio.label(ax, (9.5, 1.75), "2 K⁺ released into cytosol", size="tiny", color=P.muted())
bio.label(ax, (9.5, 6.9), "net per ATP:\n3 Na⁺ out, 2 K⁺ in\n(electrogenic)", size="normal", bold=True)
