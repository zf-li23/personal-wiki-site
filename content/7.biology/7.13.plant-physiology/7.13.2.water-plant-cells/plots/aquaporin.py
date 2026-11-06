# Two routes for water across a plant plasma membrane, and the gating of aquaporins.
# Left: a few water molecules diffuse slowly through the lipid bilayer itself.
# Middle: an open plasma-membrane intrinsic protein (PIP aquaporin): water passes in single file through
# the pore of each subunit (a tetramer; two subunits drawn); phosphorylation of serines in the
# cytosolic loops favours the open state.
# Right: a closed aquaporin: dephosphorylation, or protonation of a conserved histidine in loop D when the
# cytosol acidifies (anoxia, flooding), and Ca2+ binding fold the loop over the pore.
# The direction of water flow is always set by the water potential difference (here outside -> inside).
from matplotlib.patches import Polygon

import wikibio as bio
from wikibio import cellbio

P = bio.P
fig, ax = bio.canvas(18.0, 8.6)
Y = 4.0
cellbio.sides(ax, (0.2, 17.8), Y, top="Apoplast (Ψ higher)", bottom="Cytosol (Ψ lower)", height=(3.4, 3.2))
bio.bilayer(ax, [(0.2, Y), (17.8, Y)])
W = "dna"

# ---- lipid bilayer route ---------------------------------------------------------------------------------
bio.label(ax, (2.6, 7.95), "Through the bilayer", size="small", bold=True)
for x, y in ((1.6, 5.6), (2.9, 6.2), (3.7, 5.4), (2.2, 4.05), (3.3, 2.5)):
    bio.molecule(ax, (x, y), W, r=0.17)
bio.arrow(ax, (2.6, 5.1), (2.6, 2.9), kind="process", dashed=True, lw=1.0, color=P.edge(W))
bio.label(ax, (2.6, 1.6), "slow diffusion", size="tiny", color=P.muted())

# ---- open aquaporin --------------------------------------------------------------------------------------
bio.label(ax, (8.0, 7.95), "Open aquaporin (PIP)", size="small", bold=True)
for x in (7.0, 9.0):
    cellbio.channel(ax, x, Y, token="channel", width=1.3)
    for k in range(5):
        bio.molecule(ax, (x, Y + 1.0 - 0.5 * k), W, r=0.14, zorder=14)
    bio.arrow(ax, (x, Y + 1.9), (x, Y + 1.25), kind="process", color=P.edge(W), lw=1.4)
    bio.arrow(ax, (x, Y - 1.2), (x, Y - 1.9), kind="process", color=P.edge(W), lw=1.4)
    bio.molecule(ax, (x + 0.85, Y - 1.0), "atp", text="P", r=0.2)
bio.label(ax, (8.0, 1.6), "fast, single file; phosphorylated", size="tiny", color=P.muted())
bio.label(ax, (8.0, 6.6), "NPA filter in each subunit", size="tiny", color=P.muted())

# ---- closed aquaporin ------------------------------------------------------------------------------------
bio.label(ax, (14.2, 7.95), "Closed (gated)", size="small", bold=True)
for x in (13.2, 15.2):
    cellbio.channel(ax, x, Y, token="neutral", width=1.3)
    lid = [(x - 0.45, Y - 0.62), (x + 0.45, Y - 0.62), (x + 0.3, Y - 1.05), (x - 0.3, Y - 1.05)]
    ax.add_patch(Polygon(lid, closed=True, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.9, zorder=13))
    bio.ion(ax, (x - 0.75, Y - 1.45), "h", r=0.16, text=False)
    bio.molecule(ax, (13.2 + 1.0, Y + 1.3), W, r=0.15)
bio.label(ax, (12.2, Y - 1.45), "H⁺", size="tiny", ha="right")
bio.callout(ax, (15.2, Y - 0.85), (16.9, 2.2), "loop D\nover pore", size="tiny")
bio.label(ax, (14.2, 1.6), "dephosphorylated, low cytosolic pH, Ca²⁺", size="tiny", color=P.muted())
