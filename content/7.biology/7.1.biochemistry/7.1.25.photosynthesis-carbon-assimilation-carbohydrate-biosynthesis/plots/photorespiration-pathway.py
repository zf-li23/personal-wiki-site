"""Photorespiration: the C2 (glycolate) pathway through chloroplast, peroxisome and mitochondrion.

Chloroplast: rubisco oxygenates RuBP to 3-phosphoglycerate and 2-phosphoglycolate; phosphoglycolate
phosphatase (PGLP) gives glycolate. Peroxisome: glycolate oxidase (O2 -> H2O2, destroyed by catalase)
gives glyoxylate, which glutamate:glyoxylate aminotransferase (GGAT) converts to glycine. Mitochondrion:
the glycine decarboxylase complex (GDC) and serine hydroxymethyltransferase (SHMT) convert two glycine to
serine, CO2 and NH3 with reduction of NAD+. Peroxisome: serine:glyoxylate aminotransferase (SGAT) gives
hydroxypyruvate, hydroxypyruvate reductase (HPR) glycerate. Chloroplast: glycerate kinase (GLYK, ATP)
returns 3-phosphoglycerate to the Calvin cycle; the NH3 is refixed by glutamine synthetase and
ferredoxin-dependent glutamate synthase. Of the four carbons of two phosphoglycolates, three return as
3-phosphoglycerate and one is lost as CO2.
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import metabolism as M
from wikibio import photosynthesis as ps

P = bio.P
fig, ax = bio.canvas(27.0, 14.6, scale=0.4)
for (x0, x1), tok, txt in (((0.3, 8.7), "chloroplast", "Chloroplast"), ((9.2, 17.6), "peroxisome", "Peroxisome"),
                           ((18.1, 26.7), "mitochondrion", "Mitochondrion")):
    ax.add_patch(FancyBboxPatch((x0, 0.3), x1 - x0, 13.9, boxstyle="round,pad=0,rounding_size=0.7",
                                facecolor=ps.tint(tok), edgecolor=P.edge(tok), lw=1.3, zorder=1))
    bio.label(ax, (x0 + 0.4, 13.75), txt, size="small", bold=True, ha="left", color=P.edge(tok))

pw = M.Pathway(ax, size="small")
# chloroplast
pw.node("rubp", (4.4, 12.6), "Ribulose 1,5-bisphosphate", token="carbohydrate", bold=True)
pw.node("pg2", (2.4, 10.2), "2-Phosphoglycolate", token="negative", bold=True)
pw.node("pga", (6.6, 10.2), "3-Phosphoglycerate")
pw.node("glc", (2.4, 7.4), "Glycolate")
pw.node("glyc_c", (6.6, 1.6), "Glycerate")
pw.node("pga2", (6.6, 4.6), "3-Phosphoglycerate", token="carbohydrate", bold=True)
pw.step(None, "pg2", start=pw.anchor("rubp", "b") + (-0.6, -0.05))
bio.label(ax, (4.45, 10.95), "+ O₂\nrubisco\n(oxygenase)", size="tiny", bold=True, color=P.edge("enzyme"))
pw.step(None, "pga", start=pw.anchor("rubp", "b") + (0.6, -0.05))
pw.step("pg2", "glc", enzyme="PGLP", side=("H₂O", "Pᵢ"), enzyme_offset=0.2, flip=True)
pw.step("glyc_c", "pga2", enzyme="GLYK", side=("ATP", "ADP"), enzyme_offset=0.2)
bio.label(ax, (6.6, 5.55), "→ Calvin cycle", size="tiny", color=P.muted())
# peroxisome
pw.node("glc_p", (11.2, 7.4), "Glycolate")
pw.node("glx", (15.4, 7.4), "Glyoxylate")
pw.node("gly_p", (15.4, 10.6), "Glycine")
pw.node("ser_p", (15.4, 4.6), "Serine")
pw.node("hp", (11.2, 4.6), "Hydroxypyruvate")
pw.node("glyc_p", (11.2, 1.6), "Glycerate")
pw.step("glc_p", "glx", enzyme="Glycolate\noxidase", side=("O₂", "H₂O₂"), enzyme_offset=0.2)
bio.label(ax, (13.3, 5.9), "catalase: H₂O₂ → H₂O + ½ O₂", size="tiny", color=P.muted())
pw.step("glx", "gly_p", enzyme="GGAT", side=("Glu", "α-KG"), enzyme_offset=0.2, flip=True)
pw.step("ser_p", "hp", enzyme="SGAT", side=("glyoxylate", "glycine"), enzyme_offset=0.2, flip=True)
pw.step("hp", "glyc_p", enzyme="HPR", side=("NADH + H⁺", "NAD⁺"), enzyme_offset=0.2)
# mitochondrion
pw.node("gly_m", (21.4, 10.6), "2 Glycine", bold=True)
pw.node("ser_m", (21.4, 4.6), "Serine")
pw.step("gly_m", "ser_m", side=("NAD⁺", "NADH + H⁺"), flip=True)
bio.label(ax, (19.9, 9.2), "GDC + SHMT\n(tetrahydrofolate)", size="tiny", bold=True, color=P.edge("enzyme"))
bio.box(ax, (24.6, 7.6), 2.8, 1.0, "negative", text="CO₂ + NH₃", size="small")
bio.arrow(ax, (22.0, 7.6), (23.15, 7.6), kind="process", head=0.2)
# transport between organelles
for a, b in (("glc", "glc_p"), ("gly_p", "gly_m"), ("ser_m", "ser_p"), ("glyc_p", "glyc_c")):
    pw.step(a, b, color=P.muted(), dashed=True)
# ammonia refixation in the chloroplast
bio.arrow(ax, (24.6, 7.05), (24.6, 0.7), kind="link", color=P.muted(), dashed=True)
bio.arrow(ax, (24.6, 0.7), (2.4, 0.7), kind="link", color=P.muted(), dashed=True)
bio.arrow(ax, (2.4, 0.7), (2.4, 3.55), kind="process", color=P.muted(), dashed=True)
bio.label(ax, (21.4, 1.1), "NH₃ returns to the chloroplast", size="tiny", color=P.muted())
bio.box(ax, (2.4, 4.4), 3.6, 1.5, "enzyme", text="GS–GOGAT:\nNH₃ refixed\n(ATP, ferredoxin)", size="tiny")
