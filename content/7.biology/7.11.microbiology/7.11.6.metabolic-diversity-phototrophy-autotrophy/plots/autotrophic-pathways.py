"""Three autotrophic pathways of bacteria and archaea other than the Calvin cycle (simplified).

A: reverse (reductive) citric acid cycle of green sulfur bacteria. Starting at oxaloacetate the cycle runs
the citric acid cycle backwards: malate dehydrogenase, fumarase, fumarate reductase, succinyl-CoA
synthetase (ATP), 2-oxoglutarate:ferredoxin oxidoreductase (CO2, reduced ferredoxin), isocitrate
dehydrogenase (CO2, NAD(P)H), aconitase and ATP-citrate lyase, which splits citrate into oxaloacetate and
acetyl-CoA. Pyruvate:ferredoxin oxidoreductase adds a further CO2 to acetyl-CoA, giving pyruvate.
B: 3-hydroxypropionate bicycle of Chloroflexus (first cycle). Acetyl-CoA carboxylase and propionyl-CoA
carboxylase fix bicarbonate; malonyl-CoA is reduced through 3-hydroxypropionate to propionyl-CoA;
methylmalonyl-CoA is rearranged to succinyl-CoA, converted to malyl-CoA and cleaved into acetyl-CoA and
glyoxylate. A second cycle combines glyoxylate with propionyl-CoA and yields pyruvate (not drawn).
C: Wood-Ljungdahl (reductive acetyl-CoA) pathway. Methyl branch: formate dehydrogenase, formyl-
tetrahydrofolate synthetase (ATP) and the reduction of the C1 unit on tetrahydrofolate (THF) to methyl-THF,
whose methyl group goes to a corrinoid iron-sulfur protein (CoFeSP). Carbonyl branch: CO dehydrogenase
reduces CO2 to enzyme-bound CO. CO dehydrogenase/acetyl-CoA synthase joins methyl, CO and CoA.
[2H]: two electrons (NAD(P)H, reduced ferredoxin or H2).
"""
import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(33.0, 14.2, scale=0.4)

# A: reverse citric acid cycle ------------------------------------------------------------------
bio.panel(ax, "A", (0.3, 14.0))
bio.label(ax, (5.9, 13.6), "Reverse citric acid cycle", size="normal", bold=True)
pw = M.Pathway(ax, size="tiny")
c, r = (5.9, 6.9), 4.1
names = [("oaa", "Oxaloacetate"), ("mal", "Malate"), ("fum", "Fumarate"), ("suc", "Succinate"),
         ("scoa", "Succinyl-CoA"), ("og", "2-Oxoglutarate"), ("icit", "Isocitrate"), ("cit", "Citrate")]
for (k, t), p in zip(names, M.ring(c, r, 8, start=90, clockwise=False)):
    pw.node(k, p, t)
steps = [("oaa", "mal", ("[2H]", None)), ("mal", "fum", (None, "H₂O")), ("fum", "suc", ("[2H]", None)),
         ("suc", "scoa", ("ATP", "ADP")), ("scoa", "og", ("CO₂ + Fd", None)), ("og", "icit", ("CO₂ + [2H]", None)),
         ("icit", "cit", None), ("cit", "oaa", ("ATP", "acetyl-CoA"))]
for a, b, side in steps:
    pw.step(a, b, side=side, side_reach=0.5, bend=M.cycle_bend(pw.nodes[a][0], pw.nodes[b][0], c, clockwise=False))
bio.label(ax, (c[0], c[1] + 0.35), "3 CO₂ fixed\nper turn", size="small", color=P.muted())
pw.node("acoa", (10.6, 11.6), "Acetyl-CoA", token="highlight", bold=True)
pw.node("pyr", (10.6, 13.0), "Pyruvate", token="carbohydrate", bold=True)
pw.step("acoa", "pyr", enzyme="PFOR", side=("CO₂ + Fd", None), side_reach=0.45)
bio.arrow(ax, (7.3, 10.5), (9.3, 11.4), kind="process", dashed=True, bend=-0.15, color=P.muted())
bio.label(ax, (5.9, 1.6), "ATP-citrate lyase, fumarate reductase and the two\nferredoxin-dependent carboxylases replace\ncitrate synthase and the dehydrogenases",
          size="tiny", color=P.muted())

# B: 3-hydroxypropionate bicycle ----------------------------------------------------------------
bio.panel(ax, "B", (11.6, 14.0))
bio.label(ax, (17.1, 13.6), "3-Hydroxypropionate bicycle (cycle 1)", size="normal", bold=True)
pw2 = M.Pathway(ax, size="tiny")
c2, r2 = (17.1, 7.4), 3.9
names2 = [("ac", "Acetyl-CoA"), ("mcoa", "Malonyl-CoA"), ("hp", "3-Hydroxypropionate"), ("pcoa", "Propionyl-CoA"),
          ("mm", "Methylmalonyl-CoA"), ("sc", "Succinyl-CoA"), ("mlc", "Malyl-CoA")]
for (k, t), p in zip(names2, M.ring(c2, r2, 7, start=90, clockwise=True)):
    pw2.node(k, p, t, token="highlight" if k == "ac" else "metabolite")
steps2 = [("ac", "mcoa", ("HCO₃⁻ + ATP", None)), ("mcoa", "hp", ("2 [2H]", None)), ("hp", "pcoa", ("[2H] + ATP", None)),
          ("pcoa", "mm", ("HCO₃⁻ + ATP", None)), ("mm", "sc", None), ("sc", "mlc", None), ("mlc", "ac", (None, "glyoxylate"))]
for a, b, side in steps2:
    pw2.step(a, b, side=side, side_reach=0.5, bend=M.cycle_bend(pw2.nodes[a][0], pw2.nodes[b][0], c2, clockwise=True))
bio.label(ax, (c2[0], c2[1]), "2 HCO₃⁻ →\nglyoxylate", size="small", color=P.muted())
bio.label(ax, (17.1, 1.6), "Cycle 2: glyoxylate + propionyl-CoA (+ HCO₃⁻)\n→ pyruvate; biotin-dependent carboxylases,\noxygen-tolerant enzymes",
          size="tiny", color=P.muted())

# C: Wood-Ljungdahl pathway ---------------------------------------------------------------------
bio.panel(ax, "C", (23.0, 14.0))
bio.label(ax, (28.0, 13.6), "Wood–Ljungdahl pathway", size="normal", bold=True)
pw3 = M.Pathway(ax, size="tiny")
xm, xc = 25.4, 30.9
pw3.node("co2a", (xm, 12.4), "CO₂", token="neutral")
pw3.node("form", (xm, 10.6), "Formate")
pw3.node("fthf", (xm, 8.8), "Formyl-THF")
pw3.node("mthf", (xm, 7.0), "Methylene-THF")
pw3.node("methf", (xm, 5.2), "Methyl-THF")
pw3.node("cofesp", (xm, 3.4), "CH₃–CoFeSP")
pw3.node("co2b", (xc, 12.4), "CO₂", token="neutral")
pw3.node("co", (xc, 7.0), "[CO]", token="neutral")
pw3.node("acoa3", (28.15, 1.4), "Acetyl-CoA", token="highlight", bold=True)
pw3.step("co2a", "form", side=("[2H]", None))
pw3.step("form", "fthf", side=("ATP", "ADP"))
pw3.step("fthf", "mthf", side=("[2H]", "H₂O"))
pw3.step("mthf", "methf", side=("[2H]", None))
pw3.step("methf", "cofesp", side=(None, "THF"))
pw3.step("co2b", "co", side=("[2H]", "H₂O"), enzyme="CO\ndehydrogenase")
pw3.step("cofesp", "acoa3", bend=0.15)
pw3.step("co", "acoa3", side=("CoA", None), bend=-0.15, enzyme="CODH/ACS", enzyme_flip=True)
bio.label(ax, (xm, 13.3), "methyl branch", size="small", color=P.edge("dna"))
bio.label(ax, (xc, 13.3), "carbonyl branch", size="small", color=P.edge("rna"))
bio.label(ax, (28.15, 0.45), "linear, not a cycle; about 1 ATP per pyruvate; O₂-sensitive", size="tiny", color=P.muted())
