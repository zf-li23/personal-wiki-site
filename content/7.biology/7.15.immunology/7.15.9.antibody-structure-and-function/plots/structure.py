# Antibody structure.
# A: IgG drawn domain by domain: two heavy chains (VH, CH1, CH2, CH3) and two light chains (VL, CL), the hinge,
#    inter-chain disulfide bonds, the six CDR loops at the tips, and the Fab / Fc fragments.
# B: the five classes: IgG, IgD and IgE monomers, secreted IgA (dimer with J chain and secretory component)
#    and IgM (pentamer with J chain).
import math

from matplotlib.patches import Circle, Ellipse, Wedge

import wikibio as bio
from wikibio import immuno, quant
from wikibio.structures import antibody

P = bio.P
fig, ax = bio.canvas(21.0, 10.0)

# --- A  IgG domains -------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 9.8))
bio.label(ax, (5.0, 9.65), "IgG", size="title", bold=True)
W, Hh = 1.05, 1.05
HV, LV = "antibody", "protein"      # heavy chain colour, light chain colour (palette tokens)
xs_arm = {"L": (3.2, 1.95), "R": (6.8, 8.05)}   # (heavy, light) column of each Fab arm
for side, (xh, xl) in xs_arm.items():
    s = -1 if side == "L" else 1
    immuno.domain(ax, (xh, 5.1), W, Hh, HV, "CH1")
    immuno.domain(ax, (xh, 6.25), W, Hh, HV, "VH")
    immuno.domain(ax, (xl, 5.1), W, Hh, LV, "CL")
    immuno.domain(ax, (xl, 6.25), W, Hh, LV, "VL")
    # hinge: heavy chain leaves CH1 and runs to the CH2 domain of the stem
    xst = 4.35 if side == "L" else 5.65
    ax.plot([xh, xst], [4.55, 3.3], color=P.edge(HV), lw=2.0, zorder=11, solid_capstyle="round")
    # interchain disulfide CH1-CL
    ax.plot([xh + s * W / 2, xl - s * W / 2], [4.95, 4.95], color=P.ink(), lw=1.1, zorder=13)
    immuno.domain(ax, (xst, 2.55), W, Hh, HV, "CH2")
    immuno.domain(ax, (xst, 1.35), W, Hh, HV, "CH3")
    # CDR loops: red caps on the variable domains
    for xx in (xh, xl):
        ax.add_patch(Wedge((xx, 6.78), 0.42, 0, 180, width=0.1, facecolor=P.fill("negative"),
                           edgecolor=P.edge("negative"), lw=0.8, zorder=14))
# hinge disulfides
for yy in (3.65, 3.85):
    ax.plot([4.5, 5.5], [yy, yy], color=P.ink(), lw=1.1, zorder=13)
# brackets and labels
quant.bracket(ax, (1.1, 4.45), (1.1, 6.95), None, side=1)
bio.label(ax, (0.5, 5.7), "Fab", size="small")
quant.bracket(ax, (3.7, 0.7), (6.3, 0.7), None, side=-1)
bio.label(ax, (5.0, 0.25), "Fc", size="small")
bio.callout(ax, (3.3, 3.95), (1.0, 3.2), "hinge", size="small")
bio.callout(ax, (3.2, 6.9), (2.5, 8.3), "CDRs (3 on VH,\n3 on VL)", size="small")
bio.callout(ax, (4.95, 3.75), (8.3, 3.2), "inter-chain\ndisulfides", size="small")
bio.label(ax, (5.0, 9.0), "antigen-binding sites at the tips of the two Fab arms", size="tiny", color=P.muted())
for k, (tok, txt) in enumerate(((HV, "heavy chain"), (LV, "light chain"))):
    ax.add_patch(Circle((8.2, 1.65 + k * 0.5), 0.14, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=12))
    bio.label(ax, (8.45, 1.65 + k * 0.5), txt, size="tiny", ha="left")

# --- B  five classes ------------------------------------------------------------------------------------------
bio.panel(ax, "B", (10.6, 9.8))
bio.label(ax, (15.8, 9.65), "Five classes", size="title", bold=True)
rows = [("IgG", "γ", "antibody", 8.6), ("IgD", "δ", "drug", 7.3), ("IgE", "ε", "enzyme", 6.0)]
for name, chain, tok, y in rows:
    antibody(ax, (12.2, y), size=1.0, token=tok, light_token="neutral")
    bio.label(ax, (11.0, y), name, size="normal", bold=True)
    bio.label(ax, (13.1, y + 0.25), f"heavy chain {chain}", size="tiny", ha="left", color=P.muted())
    bio.label(ax, (13.1, y - 0.15), {"IgG": "monomer, 150 kDa", "IgD": "monomer; B-cell receptor", "IgE": "monomer; bound by mast cells"}[name],
              size="tiny", ha="left", color=P.muted())
# IgA dimer with J chain and secretory component
yA = 4.4
for sgn in (-1, 1):
    antibody(ax, (12.2 + sgn * 0.62, yA), size=0.95, angle=0, token="positive", light_token="neutral")
ax.add_patch(Circle((12.2, yA - 0.5), 0.17, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.8, zorder=14))
ax.add_patch(Ellipse((12.2, yA - 0.28), 2.1, 0.95, facecolor="none", edgecolor=P.edge("receptor"), lw=1.6, ls=(0, (3, 2)), zorder=15))
bio.label(ax, (11.0, yA), "IgA", size="normal", bold=True)
bio.label(ax, (13.5, yA + 0.25), "secretory IgA: dimer + J chain", size="tiny", ha="left", color=P.muted())
bio.label(ax, (13.5, yA - 0.15), "+ secretory component (mucosa)", size="tiny", ha="left", color=P.muted())
# IgM pentamer: five antibodies radiating from the J chain, stems towards the centre
cx, cy = 12.7, 1.75
for k in range(5):
    th = 72 * k
    d = 0.9
    antibody(ax, (cx - d * math.sin(math.radians(th)), cy + d * math.cos(math.radians(th))), size=0.7, angle=th,
             token="negative", light_token="neutral")
ax.add_patch(Circle((cx, cy), 0.17, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.8, zorder=14))
bio.label(ax, (11.0, cy), "IgM", size="normal", bold=True)
bio.label(ax, (14.6, cy + 0.25), "pentamer + J chain, 970 kDa", size="tiny", ha="left", color=P.muted())
bio.label(ax, (14.6, cy - 0.15), "10 antigen-binding sites", size="tiny", ha="left", color=P.muted())
