"""The recurring three-step oxidation -CH2-CH2- -> -CH=CH- -> -CH(OH)- -> -C(=O)- in three pathways:
the citric acid cycle (succinate to oxaloacetate), beta oxidation of fatty acyl-CoA and, in the
reverse direction with NADPH, fatty acid synthesis on the acyl carrier protein (ACP)."""

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(23.0, 11.4)
pw = M.Pathway(ax, size="small")
cols = [
    ("General", 2.9, ["–CH₂–CH₂–", "–CH=CH–", "–CH(OH)–CH₂–", "–C(=O)–CH₂–"],
     [("FAD", "FADH₂"), ("H₂O", None), ("NAD⁺", "NADH + H⁺")], ["dehydrogenation", "hydration", "dehydrogenation"], False),
    ("Citric acid cycle", 8.6, ["Succinate", "Fumarate", "L-Malate", "Oxaloacetate"],
     [("FAD", "FADH₂"), ("H₂O", None), ("NAD⁺", "NADH + H⁺")],
     ["Succinate\ndehydrogenase", "Fumarase", "Malate\ndehydrogenase"], False),
    ("β Oxidation", 14.3, ["Acyl-CoA", "trans-Δ²-Enoyl-CoA", "L-3-Hydroxyacyl-CoA", "3-Ketoacyl-CoA"],
     [("FAD", "FADH₂"), ("H₂O", None), ("NAD⁺", "NADH + H⁺")],
     ["Acyl-CoA\ndehydrogenase", "Enoyl-CoA\nhydratase", "Hydroxyacyl-CoA\ndehydrogenase"], False),
    ("Fatty acid synthesis", 20.0, ["Acyl-ACP", "trans-Δ²-Enoyl-ACP", "D-3-Hydroxyacyl-ACP", "3-Ketoacyl-ACP"],
     [("NADPH + H⁺", "NADP⁺"), (None, "H₂O"), ("NADPH + H⁺", "NADP⁺")],
     ["Enoyl-ACP\nreductase", "Hydroxyacyl-ACP\ndehydratase", "Ketoacyl-ACP\nreductase"], True),
]
ys = [9.2, 6.7, 4.2, 1.7]
for title, x, names, sides, enz, rev in cols:
    bio.label(ax, (x, 10.85), title, size="title", bold=True)
    for k, n in enumerate(names):
        pw.node(f"{x}{k}", (x, ys[k]), n, token="highlight" if title == "General" else "metabolite")
    for k in range(3):
        a, b = f"{x}{k}", f"{x}{k + 1}"
        if rev:
            pw.step(b, a, enzyme=enz[k], side=sides[2 - k] if False else sides[k], side_span=0.8)
        else:
            pw.step(a, b, enzyme=enz[k], side=sides[k], side_span=0.8, reversible=(title != "General" and k > 0))
bio.label(ax, (20.0, 0.55), "runs upward: two reductions with NADPH", size="tiny", color=P.muted())
bio.label(ax, (14.3, 0.55), "then thiolase cleaves the 3-ketoacyl-CoA", size="tiny", color=P.muted())
