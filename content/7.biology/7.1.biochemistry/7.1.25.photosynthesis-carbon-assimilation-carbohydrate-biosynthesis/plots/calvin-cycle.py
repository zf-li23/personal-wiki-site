"""The Calvin cycle (reductive pentose phosphate pathway) in the chloroplast stroma, per three CO2 fixed.

Stage 1, fixation: rubisco carboxylates 3 ribulose 1,5-bisphosphate (RuBP) to 6 3-phosphoglycerate (3-PG).
Stage 2, reduction: 3-phosphoglycerate kinase (6 ATP) and NADP-glyceraldehyde 3-phosphate dehydrogenase
(6 NADPH) give 6 triose phosphates. One triose phosphate is the net product; the other five enter
stage 3, regeneration, in which aldolase, transketolase, FBPase, SBPase, ribose 5-phosphate isomerase and
ribulose 5-phosphate epimerase rearrange 15 carbons into 3 ribulose 5-phosphate, which phosphoribulokinase
phosphorylates (3 ATP) back to RuBP. Total: 3 CO2 + 9 ATP + 6 NADPH -> 1 glyceraldehyde 3-phosphate.
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(24.0, 15.4, scale=0.42)
ax.add_patch(FancyBboxPatch((0.3, 0.3), 23.4, 14.8, boxstyle="round,pad=0,rounding_size=0.8",
                            facecolor=P.fill("chloroplast"), edgecolor=P.edge("chloroplast"), lw=1.3, alpha=0.35,
                            zorder=0))
bio.label(ax, (0.8, 14.6), "Chloroplast stroma", size="small", bold=True, ha="left", color=P.edge("chloroplast"))

pw = M.Pathway(ax, size="small")
c, r = (11.4, 7.6), 5.0
names = [("rubp", "Ribulose 1,5-bisphosphate (3, C₅)"), ("pga", "3-Phosphoglycerate (6, C₃)"),
         ("bpg", "1,3-Bisphosphoglycerate (6)"), ("g3p", "Glyceraldehyde 3-phosphate (6, C₃)"),
         ("ru5p", "Ribulose 5-phosphate (3, C₅)")]
pos = M.ring(c, r, 5, start=90, clockwise=True)
for (id, t), p in zip(names, pos):
    pw.node(id, p, t, token="carbohydrate" if id in ("rubp", "g3p") else "metabolite", bold=id in ("rubp", "g3p"))


def bend(a, b):
    return M.cycle_bend(pw.nodes[a][0], pw.nodes[b][0], c, clockwise=True)


pw.step("rubp", "pga", enzyme="Rubisco", side=("3 CO₂ + 3 H₂O", None), bend=bend("rubp", "pga"),
        enzyme_offset=0.35, side_reach=0.8, side_span=0.9, enzyme_size="small")
pw.step("pga", "bpg", enzyme="Phosphoglycerate\nkinase", side=("6 ATP", "6 ADP"), bend=bend("pga", "bpg"),
        reversible=True, enzyme_offset=0.35, side_reach=0.8, side_span=0.9)
pw.step("bpg", "g3p", enzyme="NADP-GAPDH", side=("6 NADPH + 6 H⁺", "6 NADP⁺ + 6 Pᵢ"), bend=bend("bpg", "g3p"),
        reversible=True, enzyme_offset=0.35, side_reach=0.85, side_span=1.0)
pw.step("g3p", "ru5p", enzyme="5 C₃ → 3 C₅: aldolase,\ntransketolase, FBPase,\nSBPase, isomerase,\nepimerase", bend=bend("g3p", "ru5p"),
        enzyme_offset=0.3, flip=True)
pw.step("ru5p", "rubp", enzyme="Phosphoribulokinase", side=("3 ATP", "3 ADP"), bend=bend("ru5p", "rubp"),
        enzyme_offset=0.35, side_reach=0.8, side_span=0.9)

bio.label(ax, (c[0], c[1] + 0.5), "Calvin cycle", size="title", bold=True, color=P.edge("chloroplast"))
bio.label(ax, (c[0], c[1] - 0.35), "three turns:\n3 CO₂ → 1 triose phosphate", size="small", color=P.muted())

# stage labels just outside the arcs
for txt, xy in (("Stage 1\nfixation", (17.4, 12.2)), ("Stage 2\nreduction", (17.2, 1.6)),
                ("Stage 3\nregeneration", (3.0, 10.6))):
    bio.label(ax, xy, txt, size="small", bold=True, color=P.edge("enzyme"))

# net product leaves the cycle
g = pw.nodes["g3p"][0]
pw.node("out", (g[0] - 0.4, 0.95), "1 Glyceraldehyde 3-phosphate → starch (stroma), sucrose (cytosol)",
        token="highlight", bold=True)
bio.arrow(ax, g + (0, -0.42), pw.anchor("out", "t") + (0.4, 0.05), kind="process")

bio.label(ax, (18.4, 7.6), "Net, per triose phosphate:\n3 CO₂ + 9 ATP + 6 NADPH\n→ G3P + 9 ADP + 8 Pᵢ + 6 NADP⁺",
          size="small", ha="left", color=P.ink())
bio.label(ax, (18.4, 5.6), "ATP : NADPH = 3 : 2,\nsupplied by the light reactions", size="tiny", ha="left",
          color=P.muted())
