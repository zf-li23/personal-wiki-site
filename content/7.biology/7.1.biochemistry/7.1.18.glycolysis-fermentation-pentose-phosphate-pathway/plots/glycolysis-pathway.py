"""Glycolysis: ten steps from glucose to two pyruvate. Irreversible steps (far from equilibrium in
cells) have one head, near-equilibrium steps two; co-substrates on arcs; enzyme names on the left;
reaction class (7.1.17) on the right. From glyceraldehyde 3-phosphate on, every step runs twice."""

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(18.4, 19.6, scale=0.42)
pw = M.Pathway(ax, size="small")
X = 7.0
names = [("glc", "Glucose"), ("g6p", "Glucose 6-phosphate"), ("f6p", "Fructose 6-phosphate"),
         ("fbp", "Fructose 1,6-bisphosphate"), ("gap", "Glyceraldehyde 3-phosphate"), ("bpg", "1,3-Bisphosphoglycerate"),
         ("pg3", "3-Phosphoglycerate"), ("pg2", "2-Phosphoglycerate"), ("pep", "Phosphoenolpyruvate"), ("pyr", "Pyruvate")]
Y0, DY = 18.6, 1.95
for k, (id, text) in enumerate(names):
    pw.node(id, (X, Y0 - k * DY), text, bold=id in ("glc", "pyr"))
pw.node("dhap", (11.3, Y0 - 3.5 * DY), "Dihydroxyacetone\nphosphate", h=0.62)
steps = [
    ("glc", "g6p", "1 Hexokinase", ("ATP", "ADP"), False, "phosphoryl transfer"),
    ("g6p", "f6p", "2 Phosphohexose\nisomerase", None, True, "isomerization"),
    ("f6p", "fbp", "3 PFK-1", ("ATP", "ADP"), False, "phosphoryl transfer"),
    ("fbp", "gap", "4 Aldolase", None, True, "C–C cleavage (4)"),
    ("gap", "bpg", "6 GAPDH", ("NAD⁺ + Pᵢ", "NADH + H⁺"), True, "oxidation"),
    ("bpg", "pg3", "7 Phosphoglycerate\nkinase", ("ADP", "ATP"), True, "phosphoryl transfer"),
    ("pg3", "pg2", "8 Phosphoglycerate\nmutase", None, True, "group shift"),
    ("pg2", "pep", "9 Enolase", (None, "H₂O"), True, "dehydration"),
    ("pep", "pyr", "10 Pyruvate kinase", ("ADP", "ATP"), False, "phosphoryl transfer"),
]
for a, b, enz, side, rev, cls in steps:
    mid, tan, left = pw.step(a, b, enzyme=enz, side=side, reversible=rev, side_span=0.6, flip=True)
    bio.label(ax, (16.6, mid[1]), cls, size="tiny", color=P.muted())
pw.step("fbp", "dhap", bend=-0.08)
pw.step("dhap", "gap", reversible=True)
bio.label(ax, (11.3, Y0 - 3.5 * DY - 0.75), "5 Triose phosphate\nisomerase", size="tiny", bold=True, color=P.edge("enzyme"))
bio.label(ax, (16.6, Y0 - 3.5 * DY - 0.75), "isomerization (5)", size="tiny", color=P.muted())
bio.label(ax, (16.6, Y0 + 0.6), "reaction class", size="small", bold=True, color=P.muted())
for (y0, y1, t) in ((Y0 + 0.3, Y0 - 4 * DY + 0.4, "Preparatory\nphase\n(2 ATP used)"),
                    (Y0 - 4 * DY - 0.4, Y0 - 9 * DY - 0.3, "Payoff phase\n×2 per glucose\n(4 ATP, 2 NADH)")):
    ax.plot([0.5, 0.35, 0.35, 0.5], [y0, y0, y1, y1], color=P.muted(), lw=0.9)
    bio.label(ax, (0.55, (y0 + y1) / 2), t, size="tiny", ha="left", color=P.muted())
