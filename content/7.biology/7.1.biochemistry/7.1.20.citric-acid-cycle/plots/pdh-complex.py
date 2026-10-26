"""The pyruvate dehydrogenase complex: five reactions channelled by the lipoyllysyl arm of E2.

E1 (pyruvate dehydrogenase, with TPP) decarboxylates pyruvate to hydroxyethyl-TPP (1) and transfers the
hydroxyethyl group, oxidized to acetyl, to the disulfide of the lipoyl arm (2). E2 (dihydrolipoyl
transacetylase) transfers the acetyl group to CoA (3). E3 (dihydrolipoyl dehydrogenase, with FAD)
reoxidizes the dithiol (4) and passes the electrons from FADH2 to NAD+ (5). The lipoyl arm visits the
three active sites in turn: S-S (oxidized), S-acetyl/SH, SH/SH.
"""

import numpy as np
from matplotlib.patches import Circle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22.0, 12.0, scale=0.42)

E1, E2, E3 = np.array([4.2, 7.6]), np.array([11.0, 3.4]), np.array([17.8, 7.6])
bio.protein(ax, E1, 4.6, 3.4, "enzyme", text=None)
bio.protein(ax, E2, 5.4, 3.0, "carbohydrate", text=None)
bio.protein(ax, E3, 4.6, 3.4, "receptor", text=None)
bio.label(ax, E1 + (0, 2.25), "E1  pyruvate dehydrogenase", size="small", bold=True)
bio.label(ax, E2 + (0, -1.95), "E2  dihydrolipoyl transacetylase (core)", size="small", bold=True)
bio.label(ax, E3 + (0, 2.25), "E3  dihydrolipoyl dehydrogenase", size="small", bold=True)
bio.molecule(ax, E1 + (0.4, -0.3), "highlight", "TPP", r=0.42)
bio.molecule(ax, E3 + (-0.4, -0.3), "highlight", "FAD", r=0.42)

# the swinging lipoyllysyl arm: three positions
root = E2 + (0, 0.6)
tips = [E1 + (1.4, -1.25), E2 + (0, 2.7), E3 + (-1.4, -1.25)]
texts = ["S–S", "S–Ac  SH", "SH  SH"]
for k, (tip, t) in enumerate(zip(tips, texts)):
    pts = np.array([root, (root + tip) / 2 + np.array([0, 0.35]), tip])
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge("carbohydrate"), lw=2.2, ls="-" if k == 1 else (0, (3, 2)),
            solid_capstyle="round", zorder=11)
    ax.add_patch(Circle(tip, 0.3, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.9, zorder=13))
    bio.label(ax, tip + (0, -0.55) if k != 1 else tip + (0, 0.55), t, size="tiny", bold=True)
bio.label(ax, root + (0.25, -0.1), "Lys", size="tiny", ha="left", color=P.on_fill())
bio.label(ax, (16.2, 2.3), "lipoyllysyl arm (about 1.4 nm)\nvisits the three active sites", size="tiny",
          color=P.muted())

# substrates, products and steps
bio.label(ax, (0.6, 11.3), "Pyruvate", size="small", bold=True, ha="left")
bio.arrow(ax, (1.4, 10.95), E1 + (-0.1, -0.1), kind="process", bend=0.2)
bio.label(ax, (0.6, 3.6), "CO₂", size="small", ha="left")
bio.arrow(ax, E1 + (0.0, -0.7), (1.2, 4.0), kind="process", bend=-0.1)
bio.label(ax, (11.0, 8.0), "CoA-SH → acetyl-CoA", size="small", bold=True)
bio.label(ax, (21.4, 11.3), "NAD⁺ → NADH + H⁺", size="small", bold=True, ha="right")
bio.arrow(ax, E3 + (-0.2, 0.15), (20.3, 10.9), kind="process", bend=0.15)
steps = [((1.4, 9.0), "1"), ((7.4, 5.6), "2"), ((11.0, 7.35), "3"), ((14.6, 5.6), "4"), ((20.6, 9.6), "5")]
for xy, n in steps:
    ax.add_patch(Circle(xy, 0.3, facecolor=P.fill("drug"), edgecolor=P.edge("drug"), lw=0.9, zorder=14))
    bio.label(ax, xy, n, size="tiny", bold=True, color=P.on_fill(), zorder=15)
bio.arrow(ax, tips[0] + (0.45, 0.2), tips[1] + (-0.45, 0.0), kind="process", bend=-0.2, color=P.edge("drug"),
          dashed=True)
bio.arrow(ax, tips[1] + (0.45, 0.0), tips[2] + (-0.45, 0.2), kind="process", bend=-0.2, color=P.edge("drug"),
          dashed=True)
