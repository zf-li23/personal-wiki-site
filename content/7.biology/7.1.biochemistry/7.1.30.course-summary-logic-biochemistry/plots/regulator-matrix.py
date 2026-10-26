"""Regulator x enzyme matrix of mammalian energy metabolism.

Rows: allosteric effectors (top block) and hormonal or covalent signals (bottom block).
Columns: the regulated enzymes, grouped by pathway. A green "+" cell means the regulator activates
the enzyme, a red "-" cell that it inhibits it; empty cells mean no major direct effect recorded in
the chapters. Hormone rows give the net effect in the liver through phosphorylation (glucagon and
epinephrine via PKA; insulin opposing it); the AMPK row is the effect of the active kinase.
Every entry is taken from the pathway cards of 7.1.18-7.1.26 and 7.1.29.
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio

P = bio.P

cols = [
    ("Hexokinase I–III", "Glycolysis"), ("PFK-1", "Glycolysis"), ("Pyruvate kinase L", "Glycolysis"),
    ("FBPase-1", "Gluconeogenesis"), ("Pyruvate carboxylase", "Gluconeogenesis"),
    ("Glycogen phosphorylase", "Glycogen"), ("Glycogen synthase", "Glycogen"),
    ("PDH complex", "Pyruvate, TCA"), ("Citrate synthase", "Pyruvate, TCA"),
    ("Isocitrate DH", "Pyruvate, TCA"), ("α-Ketoglutarate DH", "Pyruvate, TCA"),
    ("CPT1", "Fatty acids"), ("Acetyl-CoA carboxylase", "Fatty acids"),
    ("HMG-CoA reductase", "Sterols"),
]
C = {name: k for k, (name, _) in enumerate(cols)}

rows = [
    ("AMP", {"PFK-1": 1, "FBPase-1": -1, "Glycogen phosphorylase": 1, "PDH complex": 1}),
    ("ADP", {"PFK-1": 1, "Isocitrate DH": 1}),
    ("ATP", {"PFK-1": -1, "Pyruvate kinase L": -1, "Glycogen phosphorylase": -1, "PDH complex": -1,
             "Citrate synthase": -1, "Isocitrate DH": -1}),
    ("NADH", {"PDH complex": -1, "Isocitrate DH": -1, "α-Ketoglutarate DH": -1}),
    ("Ca²⁺", {"Glycogen phosphorylase": 1, "PDH complex": 1, "Isocitrate DH": 1, "α-Ketoglutarate DH": 1}),
    ("Glucose 6-phosphate", {"Hexokinase I–III": -1, "Glycogen phosphorylase": -1, "Glycogen synthase": 1}),
    ("Glucose (liver)", {"Glycogen phosphorylase": -1}),
    ("Fructose 1,6-bisphosphate", {"Pyruvate kinase L": 1}),
    ("Fructose 2,6-bisphosphate", {"PFK-1": 1, "FBPase-1": -1}),
    ("Citrate", {"PFK-1": -1, "Citrate synthase": -1, "Acetyl-CoA carboxylase": 1}),
    ("Acetyl-CoA", {"Pyruvate kinase L": -1, "Pyruvate carboxylase": 1, "PDH complex": -1}),
    ("Succinyl-CoA", {"Citrate synthase": -1, "α-Ketoglutarate DH": -1}),
    ("Fatty acids, acyl-CoA", {"Pyruvate kinase L": -1, "PDH complex": -1, "Acetyl-CoA carboxylase": -1}),
    ("Malonyl-CoA", {"CPT1": -1}),
    None,  # separator: covalent / hormonal block
    ("Insulin", {"PFK-1": 1, "FBPase-1": -1, "Pyruvate kinase L": 1, "Glycogen phosphorylase": -1,
                 "Glycogen synthase": 1, "PDH complex": 1, "Acetyl-CoA carboxylase": 1, "HMG-CoA reductase": 1}),
    ("Glucagon, epinephrine (PKA)", {"PFK-1": -1, "FBPase-1": 1, "Pyruvate kinase L": -1,
                                     "Glycogen phosphorylase": 1, "Glycogen synthase": -1,
                                     "Acetyl-CoA carboxylase": -1, "HMG-CoA reductase": -1}),
    ("AMPK (low energy charge)", {"Glycogen synthase": -1, "Acetyl-CoA carboxylase": -1, "HMG-CoA reductase": -1}),
]

cw, ch = 1.0, 0.72         # cell size
x0 = 7.4                   # left edge of the grid
nrow = sum(1 for r in rows if r is not None)
gap = 0.35                 # gap before the covalent block
top = 2.0 + nrow * ch + gap  # top edge of the grid
W = x0 + len(cols) * cw + 2.4
H = top + 4.3
fig, ax = bio.canvas(W, H, scale=0.5)

# column groups and headers
groups = []
for k, (_, g) in enumerate(cols):
    if not groups or groups[-1][0] != g:
        groups.append([g, k, k])
    else:
        groups[-1][2] = k
for gi, (g, a, b) in enumerate(groups):
    xa, xb = x0 + a * cw, x0 + (b + 1) * cw
    token = ["drug", "channel", "carbohydrate", "highlight", "lipid", "metabolite"][gi % 6]
    ax.add_patch(FancyBboxPatch((xa + 0.05, top + 0.12), xb - xa - 0.1, 0.42, boxstyle="round,pad=0,rounding_size=0.12",
                                facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.8, zorder=3))
    bio.label(ax, ((xa + xb) / 2, top + 0.33), g if b > a else g.replace("Gluconeogenesis", "GNG"),
              size="tiny", bold=True, color=P.on_fill())
for k, (name, _) in enumerate(cols):
    bio.label(ax, (x0 + (k + 0.5) * cw + 0.05, top + 0.75), name, size="small", rotation=55, ha="left", va="bottom")

# grid
y = top
for r in rows:
    if r is None:
        y -= gap
        ax.plot([0.4, x0 + len(cols) * cw], [y + gap / 2, y + gap / 2], color=P.muted(), lw=0.7, ls=(0, (3, 2)))
        continue
    name, eff = r
    yc = y - ch / 2
    bio.label(ax, (x0 - 0.2, yc), name, size="small", ha="right")
    for k in range(len(cols)):
        xc = x0 + (k + 0.5) * cw
        v = eff.get(cols[k][0], 0)
        if v:
            token = "positive" if v > 0 else "negative"
            ax.add_patch(FancyBboxPatch((xc - cw / 2 + 0.07, yc - ch / 2 + 0.07), cw - 0.14, ch - 0.14,
                                        boxstyle="round,pad=0,rounding_size=0.1", facecolor=P.fill(token),
                                        edgecolor=P.edge(token), lw=0.8, zorder=5))
            bio.label(ax, (xc, yc), "+" if v > 0 else "−", size="normal", bold=True, color=P.on_fill(), zorder=6)
        else:
            ax.add_patch(FancyBboxPatch((xc - cw / 2 + 0.07, yc - ch / 2 + 0.07), cw - 0.14, ch - 0.14,
                                        boxstyle="round,pad=0,rounding_size=0.1", fill=False,
                                        edgecolor=P.mix(P.muted(), P.surface(), 0.55), lw=0.6, zorder=4))
    y -= ch

bio.label(ax, (0.4, top - 0.05 + 0.33), "Allosteric effectors", size="small", bold=True, ha="left", color=P.muted())
ysep = top - 14 * ch - gap
bio.label(ax, (0.4, ysep - 0.02), "Hormones and kinases (liver)", size="small", bold=True, ha="left",
          color=P.muted(), va="top")

# legend
ly = 0.8
for k, (v, text) in enumerate([(1, "activates"), (-1, "inhibits")]):
    xc = x0 + 0.5 + k * 3.4
    token = "positive" if v > 0 else "negative"
    ax.add_patch(FancyBboxPatch((xc - 0.43, ly - 0.29), 0.86, 0.58, boxstyle="round,pad=0,rounding_size=0.1",
                                facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.8))
    bio.label(ax, (xc, ly), "+" if v > 0 else "−", size="normal", bold=True, color=P.on_fill())
    bio.label(ax, (xc + 0.6, ly), text, size="small", ha="left")
