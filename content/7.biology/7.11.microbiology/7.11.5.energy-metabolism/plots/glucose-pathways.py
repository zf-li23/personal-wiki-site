"""Four routes of glucose catabolism, simplified (key intermediates and enzymes only).
A glycolysis: Glc -> G6P -> F1,6BP (PFK) -> 2 GAP (aldolase) -> 2 pyruvate; net 2 ATP, 2 NADH.
B Entner-Doudoroff: G6P -> 6-phosphogluconate (G6PDH, NADPH) -> KDPG (dehydratase Edd) -> pyruvate +
GAP (KDPG aldolase Eda); GAP -> pyruvate (lower glycolysis, 2 ATP, NADH); net 1 ATP, 1 NADH, 1 NADPH.
C oxidative pentose phosphate pathway: G6P -> 6-PG (NADPH) -> ribulose 5-P + CO2 (NADPH).
D heterolactic phosphoketolase pathway: G6P -> 6-PG -> ribulose 5-P + CO2 -> xylulose 5-P ->
(phosphoketolase) GAP + acetyl-P; GAP -> lactate; acetyl-P -> ethanol (2 NADH); net 1 ATP."""

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(32.0, 15.0)
pw = M.Pathway(ax, size="small")
ys = [13.0, 10.9, 8.8, 6.7, 4.6, 2.5]

panels = [
    ("A  Glycolysis (EMP)", 3.6,
     ["Glucose", "Glucose 6-P", "Fructose 1,6-bisP", "2 Glyceraldehyde 3-P", "2 Pyruvate"],
     [("Hexokinase", ("ATP", "ADP")), ("PFK", ("ATP", "ADP")), ("Aldolase", None),
      ("lower glycolysis", ("4 ADP, 2 NAD⁺", "4 ATP, 2 NADH"))],
     "net: 2 ATP, 2 NADH"),
    ("C  Oxidative pentose phosphate", 19.4,
     ["Glucose", "Glucose 6-P", "6-Phosphogluconate", "Ribulose 5-P", "nonoxidative phase:\nribose 5-P, erythrose 4-P"],
     [("Hexokinase", ("ATP", "ADP")), ("G6PDH", ("NADP⁺", "NADPH")), ("6PGDH", ("NADP⁺", "NADPH + CO₂")),
      ("", None)],
     "2 NADPH per glucose 6-P"),
]
for title, x, names, steps, net in panels:
    bio.label(ax, (x, 14.4), title, size="small", bold=True)
    for k, n in enumerate(names):
        pw.node(f"{x}{k}", (x, ys[k]), n, token="highlight" if k == 0 else "metabolite")
    for k, (enz, side) in enumerate(steps):
        if title.startswith("C") and k == 3:
            pw.step(f"{x}{k}", f"{x}{k + 1}", dashed=True, color=P.muted())
            continue
        pw.step(f"{x}{k}", f"{x}{k + 1}", enzyme=enz or None, side=side, side_span=0.8)
    bio.box(ax, (x, 1.0), 6.2, 0.8, "positive", net, size="small")

# B Entner-Doudoroff
x = 11.5
bio.label(ax, (x, 14.4), "B  Entner–Doudoroff", size="small", bold=True)
for k, n in enumerate(["Glucose", "Glucose 6-P", "6-Phosphogluconate", "KDPG"]):
    pw.node(f"ed{k}", (x, ys[k]), n, token="highlight" if k == 0 else "metabolite")
pw.step("ed0", "ed1", enzyme="Hexokinase", side=("ATP", "ADP"), side_span=0.8)
pw.step("ed1", "ed2", enzyme="G6PDH", side=("NADP⁺", "NADPH"), side_span=0.8)
pw.step("ed2", "ed3", enzyme="Edd (dehydratase)", side=(None, "H₂O"), side_span=0.8)
pw.node("edpyr", (x - 2.0, ys[4]), "Pyruvate")
pw.node("edgap", (x + 2.0, ys[4]), "Glyceraldehyde 3-P")
pw.step("ed3", "edpyr")
pw.step("ed3", "edgap")
pw.node("edpyr2", (x + 2.0, ys[5]), "Pyruvate")
pw.step("edgap", "edpyr2", side=("2 ADP, NAD⁺", "2 ATP, NADH"), side_span=0.8)
bio.label(ax, (x + 0.6, (ys[3] + ys[4]) / 2 + 0.05), "KDPG aldolase", size="tiny", color=P.muted())
bio.box(ax, (x, 1.0), 6.2, 0.8, "positive", "net: 1 ATP, 1 NADH, 1 NADPH", size="small")

# D phosphoketolase
x = 27.6
bio.label(ax, (x, 14.4), "D  Phosphoketolase (heterolactic)", size="small", bold=True)
for k, n in enumerate(["Glucose 6-P", "Ribulose 5-P", "Xylulose 5-P"]):
    pw.node(f"pk{k}", (x, ys[k + 1]), n, token="metabolite")
pw.node("pkg", (x, ys[0]), "Glucose", token="highlight")
pw.step("pkg", "pk0", side=("ATP", "ADP"), side_span=0.8)
pw.step("pk0", "pk1", enzyme="via 6-PG", side=("2 NAD(P)⁺", "2 NAD(P)H + CO₂"), side_span=0.8)
pw.step("pk1", "pk2", enzyme="epimerase")
pw.node("pkgap", (x - 2.1, ys[4]), "Glyceraldehyde 3-P")
pw.node("pkacp", (x + 2.1, ys[4]), "Acetyl-P")
pw.step("pk2", "pkgap")
bio.label(ax, (x, (ys[3] + ys[4]) / 2 - 0.1), "phosphoketolase\n(+ Pᵢ)", size="tiny", color=P.edge("enzyme"))
pw.step("pk2", "pkacp")
pw.node("pklac", (x - 2.1, ys[5]), "Lactate")
pw.node("pketh", (x + 2.1, ys[5]), "Ethanol")
pw.step("pkgap", "pklac", side=("2 ADP", "2 ATP"), side_span=0.7)
pw.step("pkacp", "pketh", side=("2 NADH", "2 NAD⁺"), side_span=0.7)
bio.box(ax, (x, 1.0), 6.2, 0.8, "positive", "net: 1 ATP; lactate + ethanol + CO₂", size="small")
