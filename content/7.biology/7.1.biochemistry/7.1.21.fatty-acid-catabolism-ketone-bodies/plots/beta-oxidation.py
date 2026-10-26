"""One turn of mitochondrial beta oxidation, drawn as a cycle that the acyl chain passes through repeatedly.

Acyl-CoA dehydrogenase (FAD; electrons via ETF to ubiquinone) introduces a trans-Delta2 double bond;
enoyl-CoA hydratase adds water to give L-3-hydroxyacyl-CoA; L-3-hydroxyacyl-CoA dehydrogenase (NAD+)
gives 3-ketoacyl-CoA; thiolase cleaves it with CoA into acetyl-CoA and an acyl-CoA two carbons shorter,
which re-enters the cycle. A C16 chain passes seven times and yields eight acetyl-CoA.
"""

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(21.0, 15.6, scale=0.42)
pw = M.Pathway(ax, size="small")
c, r = (10.0, 7.6), 5.6
names = [("acyl", "Fatty acyl-CoA (Cₙ)\nR–CH₂–CH₂–CO–SCoA"), ("enoyl", "trans-Δ²-Enoyl-CoA\nR–CH=CH–CO–SCoA"),
         ("hyd", "L-3-Hydroxyacyl-CoA\nR–CH(OH)–CH₂–CO–SCoA"), ("keto", "3-Ketoacyl-CoA\nR–CO–CH₂–CO–SCoA")]
pos = M.ring(c, r, 4, start=90, clockwise=True)
for (id, t), p in zip(names, pos):
    pw.node(id, p, t, h=1.0, token="lipid" if id == "acyl" else "metabolite")
steps = [("acyl", "enoyl", "1 Acyl-CoA\ndehydrogenase", ("FAD", "FADH₂ → ETF → Q"), False),
         ("enoyl", "hyd", "2 Enoyl-CoA\nhydratase", ("H₂O", None), True),
         ("hyd", "keto", "3 L-3-Hydroxyacyl-CoA\ndehydrogenase", ("NAD⁺", "NADH + H⁺"), True),
         ("keto", "acyl", "4 Thiolase", ("CoA", "Acetyl-CoA"), True)]
for a, b, e, side, rev in steps:
    pw.step(a, b, enzyme=e, side=side, reversible=rev, enzyme_offset=0.7, side_reach=0.75, side_span=0.9,
            bend=M.cycle_bend(pw.nodes[a][0], pw.nodes[b][0], c, clockwise=True))
bio.label(ax, (c[0], c[1] + 0.35), "β oxidation", size="normal", bold=True, color=P.edge("lipid"))
bio.label(ax, (c[0], c[1] - 0.35), "Cₙ₋₂-acyl-CoA re-enters;\nn/2 − 1 turns per chain", size="tiny", color=P.muted())
bio.label(ax, (0.4, 15.0), "Mitochondrial matrix", size="small", bold=True, ha="left", color=P.edge("mitochondrion"))
bio.label(ax, (0.4, 0.6), "Long chains (≥ C12): steps 2–4 on the trifunctional protein of the inner membrane",
          size="tiny", ha="left", color=P.muted())
