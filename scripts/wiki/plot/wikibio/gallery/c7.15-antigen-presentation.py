# Antigen presentation: the MHC class I pathway (cytosolic protein -> proteasome -> TAP -> loading in the ER ->
# surface MHC I, read by a CD8+ T cell) and the MHC class II pathway (endocytosed antigen -> endolysosome ->
# MIIC, where peptide replaces the invariant-chain fragment CLIP -> surface MHC II, read by a CD4+ T cell).
import numpy as np
from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import immuno, neuro

P = bio.P
fig, ax = bio.canvas(25, 12.75)


def rounded(x0, y0, x1, y1, r=0.9, n=80):
    """Vertices of a rounded rectangle (counter-clockwise)."""
    t = np.linspace(0, np.pi / 2, n)
    c = [(x1 - r, y0 + r, -np.pi / 2), (x1 - r, y1 - r, 0), (x0 + r, y1 - r, np.pi / 2), (x0 + r, y0 + r, np.pi)]
    return np.vstack([np.c_[cx + r * np.cos(a + t), cy + r * np.sin(a + t)] for cx, cy, a in c])


y_apc, y_t = 6.2, 9.15
bio.membrane(ax, rounded(0.4, 0.2, 24.6, y_apc), inside="cytoplasm")
for x0, x1 in ((1.2, 11.6), (13.0, 22.8)):
    bio.membrane(ax, rounded(x0, y_t, x1, 12.5), inside="cytoplasm")
bio.label(ax, (3.3, 1.2), "Antigen-presenting cell\n(e.g. dendritic cell)", size="small", bold=True)
bio.label(ax, (6.4, 11.85), "CD8⁺ T cell (cytotoxic)", size="small", bold=True)
bio.label(ax, (17.9, 11.85), "CD4⁺ T cell (helper)", size="small", bold=True)
for x in (3.2, 20.8):
    bio.nucleus(ax, (x, 10.85), 0.8, pores=8)

# ---- synapse, class I: MHC I + peptide, TCR, CD8 (binds the alpha3 domain) ---------------------------------
m1 = immuno.mhc_i(ax, 8.65, y_apc)
immuno.tcr(ax, m1["center_x"], y_t, up=-1, cd3_side="right")
immuno.cd8(ax, 7.9, y_t, up=-1, reach=m1["alpha3"][1], label_side=-1)
bio.label(ax, (10.0, 6.75), "MHC I", size="small", ha="left")
bio.label(ax, (10.75, 8.2), "TCR", size="small", ha="left")
bio.callout(ax, (m1["top"][0] + 0.25, m1["top"][1]), (10.9, 7.55), "peptide\n(8–10 aa)", size="tiny")

# ---- synapse, class II: MHC II + peptide, TCR, CD4 (binds the beta2 domain) -----------------------------------
m2 = immuno.mhc_ii(ax, 16.3, y_apc)
immuno.tcr(ax, m2["center_x"], y_t, up=-1, cd3_side="left")
immuno.cd4(ax, 17.25, y_t, up=-1, reach=m2["beta2"][1] - 0.15)
bio.label(ax, (15.25, 6.75), "MHC II", size="small", ha="right")
bio.label(ax, (14.0, 8.2), "TCR", size="small", ha="right")
bio.callout(ax, (m2["top"][0] - 0.7, m2["top"][1]), (13.9, 7.55), "peptide\n(13–25 aa)", size="tiny")

# ---- ER shared by both pathways ------------------------------------------------------------------------------
er_y0, er_y1 = 0.75, 2.15
ax.add_patch(FancyBboxPatch((6.0, er_y0), 12.0, er_y1 - er_y0, boxstyle="round,pad=0,rounding_size=0.55",
                            facecolor=P.fill("er"), edgecolor=P.edge("er"), lw=1.4, zorder=6))
bio.label(ax, (12.0, 1.15), "Endoplasmic reticulum", size="small", color=P.on_fill(), zorder=8)

# ---- class I pathway (left) ----------------------------------------------------------------------------------
bio.label(ax, (1.0, 5.55), "Endogenous antigen → MHC I", size="small", bold=True, ha="left", color=P.edge("protein"))
bio.protein(ax, (1.9, 4.2), 1.2, 0.8, "virus", text="viral\nprotein", size="tiny")
bio.arrow(ax, (2.65, 4.2), (3.25, 4.2), kind="process")
bio.icon(ax, "bioicons/proteasome", at=(4.0, 4.2), height=1.2)
bio.label(ax, (4.0, 3.35), "Proteasome", size="tiny", va="top")
for k, (px, py) in enumerate(((5.2, 4.55), (5.35, 4.15), (5.1, 3.75))):
    immuno.peptide(ax, (px, py), (px + 0.5, py), n=5, r=0.05)
bio.arrow(ax, (5.9, 3.9), (6.8, 2.6), kind="process", bend=-0.15)
neuro.channel(ax, 7.0, er_y1, ion=None, token="enzyme", membrane_half=0.1, width=0.7)
bio.label(ax, (6.45, er_y1 + 0.05), "TAP", size="tiny", ha="right")
immuno.mhc_i(ax, 8.3, er_y0 + 0.02, h=0.36, labels=False)
bio.label(ax, (9.25, er_y0 + 0.65), "loading", size="tiny", ha="left", color=P.on_fill(), zorder=20)
bio.vesicle(ax, (9.0, 4.2), 0.62)
immuno.mhc_i(ax, 8.75, 3.62, h=0.3, labels=False)
bio.arrow(ax, (9.0, er_y1 + 0.1), (9.0, 3.5), kind="process")
bio.arrow(ax, (9.0, 4.85), (9.0, 5.75), kind="process")

# ---- class II pathway (right) ----------------------------------------------------------------------------------
bio.label(ax, (23.2, 5.55), "Exogenous antigen → MHC II", size="small", bold=True, ha="right", color=P.edge("enzyme"))
bio.cell(ax, (23.75, 7.1), 0.5, 0.26, kind="bacterium", zorder=8)
bio.label(ax, (23.75, 7.55), "bacterium", size="tiny", va="bottom")
bio.arrow(ax, (23.6, 6.55), (23.0, 5.05), kind="process", bend=0.1)
bio.vesicle(ax, (22.6, 4.45), 0.55, cargo="protein")
bio.label(ax, (22.6, 3.75), "Endosome", size="tiny", va="top")
bio.arrow(ax, (22.0, 4.35), (21.25, 4.1), kind="process")
bio.lysosome(ax, (20.45, 4.0), 0.72)
for k, (px, py) in enumerate(((20.0, 4.25), (20.3, 3.85), (20.0, 3.55))):
    immuno.peptide(ax, (px, py), (px + 0.6, py), n=6, r=0.045)
bio.label(ax, (20.55, 3.1), "Endolysosome:\nproteolysis", size="tiny", va="top")
bio.arrow(ax, (19.7, 4.05), (18.95, 4.05), kind="process")
bio.vesicle(ax, (18.1, 4.15), 0.78)
immuno.mhc_ii(ax, 18.1, 3.42, h=0.3, labels=False)
bio.label(ax, (18.1, 2.95), "MIIC: CLIP\n→ peptide", size="tiny", va="top")
bio.arrow(ax, (17.65, 4.85), (16.6, 5.8), kind="process", bend=0.1)
# MHC II with invariant chain leaves the ER
immuno.mhc_ii(ax, 15.4, er_y0 + 0.02, h=0.36, labels=False, peptide_on=False)
ax.add_patch(FancyBboxPatch((15.4 - 0.32, er_y0 + 0.02 + 0.14 + 0.72), 0.64, 0.12, boxstyle="round,pad=0,rounding_size=0.05",
                            facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8, zorder=15))
bio.label(ax, (16.1, er_y0 + 0.75), "MHC II + Ii", size="tiny", ha="left", color=P.on_fill(), zorder=20)
bio.arrow(ax, (15.3, er_y1 + 0.1), (17.3, 4.0), kind="process", bend=-0.2)
