"""Feeder pathways for glycolysis: glycogen and starch (phosphorolysis), disaccharides (hydrolysis),
fructose (muscle: hexokinase; liver: fructokinase, aldolase B, triose kinase), galactose (Leloir
pathway), mannose and glycerol. Inherited defects marked in red at their enzymes."""

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(24.0, 14.4, scale=0.42)
pw = M.Pathway(ax, size="small")
# glycolytic spine (x = 12)
X = 12.0
spine = [("glc", 12.6, "Glucose"), ("g6p", 10.6, "Glucose 6-phosphate"), ("f6p", 8.4, "Fructose 6-phosphate"),
         ("fbp", 6.2, "Fructose 1,6-bisphosphate"), ("gap", 2.2, "Glyceraldehyde 3-phosphate"), ("pyr", 0.5, "→ pyruvate")]
for id, y, t in spine:
    pw.node(id, (X, y), t, token="highlight" if id != "pyr" else "neutral", bold=id == "glc")
pw.node("dhap", (16.2, 4.4), "Dihydroxyacetone phosphate")
pw.step("glc", "g6p", enzyme="hexokinase", enzyme_flip=True)
pw.step("g6p", "f6p", reversible=True)
pw.step("f6p", "fbp", enzyme="PFK-1", enzyme_flip=True)
pw.step("fbp", "gap", reversible=True, enzyme="aldolase", enzyme_flip=True)
pw.step("fbp", "dhap", bend=-0.1)
pw.step("dhap", "gap", reversible=True, bend=-0.1)
pw.step("gap", "pyr")

# glycogen / starch (top left)
pw.node("gly", (4.2, 13.6), "Glycogen, starch")
pw.node("g1p", (4.2, 11.6), "Glucose 1-phosphate")
pw.step("gly", "g1p", enzyme="glycogen\nphosphorylase", side=("Pᵢ", None))
pw.step("g1p", "g6p", enzyme="phosphoglucomutase", reversible=True)
# disaccharides (top centre)
pw.node("dis", (12.0, 14.0), "Lactose, sucrose, maltose (gut: lactase, sucrase, maltase)", token="carbohydrate")
pw.step("dis", "glc")
# galactose (left)
pw.node("gal", (1.9, 9.8), "Galactose")
pw.node("gal1p", (1.9, 7.2), "Galactose 1-phosphate")
pw.step("gal", "gal1p", side=("ATP", "ADP"), flip=True)
bio.label(ax, (0.1, 9.15), "galactokinase", size="tiny", bold=True, ha="left", color=P.edge("enzyme"))
pw.step("gal1p", "g1p")
bio.label(ax, (4.2, 8.7), "uridylyltransferase\n(UDP-Glc in, UDP-Gal out)", size="tiny", bold=True, ha="left", color=P.edge("enzyme"))
bio.label(ax, (4.2, 8.0), "galactosemia", size="tiny", color=P.edge("negative"), bold=True, ha="left")
bio.label(ax, (0.4, 6.1), "UDP-Gal ⇌ UDP-Glc (4-epimerase, NAD⁺)", size="tiny", ha="left", color=P.muted())
# mannose (left middle)
pw.node("man", (4.4, 4.6), "Mannose")
pw.node("m6p", (7.4, 4.6), "Mannose 6-P")
pw.step("man", "m6p", side=("ATP", "ADP"))
pw.step("m6p", "f6p", enzyme="phosphomannose\nisomerase", enzyme_flip=True)
# fructose (right)
pw.node("fruM", (20.0, 9.6), "Fructose (muscle, kidney)")
pw.step("fruM", "f6p", enzyme="hexokinase", side=("ATP", "ADP"))
pw.node("fruL", (20.0, 7.4), "Fructose (liver)")
pw.node("f1p", (20.0, 5.9), "Fructose 1-phosphate")
pw.step("fruL", "f1p", enzyme="fructokinase", side=("ATP", "ADP"))
pw.node("gald", (21.0, 2.2), "Glyceraldehyde")
pw.step("f1p", "dhap", enzyme="aldolase B", enzyme_flip=True)
pw.step("f1p", "gald")
pw.step("gald", "gap", enzyme="triose kinase", side=("ATP", "ADP"))
bio.label(ax, (22.4, 4.4), "hereditary fructose\nintolerance", size="tiny", color=P.edge("negative"), bold=True)
# glycerol (bottom left): to dihydroxyacetone phosphate, then GAP by triose phosphate isomerase
pw.node("glyc", (2.2, 2.2), "Glycerol")
pw.node("g3p", (6.4, 2.2), "Glycerol 3-P")
pw.step("glyc", "g3p", side=("ATP", "ADP"), enzyme="glycerol kinase")
pw.step("g3p", "gap", enzyme="G3P DH, TPI\n(via DHAP)", side=("NAD⁺", "NADH"))
