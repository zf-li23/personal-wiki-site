"""Auxiliary reactions of beta oxidation.

A: unsaturated fatty acids. Oleoyl-CoA (18:1 cis-Delta9) gives after three turns cis-Delta3-dodecenoyl-CoA,
which enoyl-CoA isomerase converts to trans-Delta2. Linoleoyl-CoA (18:2 cis-Delta9,12) gives, after three turns,
the isomerase, one more turn and the acyl-CoA dehydrogenase, a 2,4-dienoyl-CoA (trans-Delta2, cis-Delta4), which
2,4-dienoyl-CoA reductase (NADPH) reduces to trans-Delta3-enoyl-CoA; the isomerase converts it to trans-Delta2.
B: odd-chain fatty acids. The last thiolysis gives propionyl-CoA, which propionyl-CoA carboxylase (biotin)
carboxylates to D-methylmalonyl-CoA; methylmalonyl-CoA epimerase gives the L isomer, and methylmalonyl-CoA
mutase (coenzyme B12) rearranges it to succinyl-CoA, an intermediate of the citric acid cycle.
"""

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(26.0, 15.0, scale=0.4)
pw = M.Pathway(ax, size="small")
bio.panel(ax, "A", (0.3, 14.6))
bio.panel(ax, "B", (18.0, 14.6))

# oleate
X1 = 4.4
pw.node("ole", (X1, 13.4), "Oleoyl-CoA (18:1, cis-Δ⁹)", token="lipid", bold=True)
pw.node("c12", (X1, 10.6), "cis-Δ³-Dodecenoyl-CoA")
pw.node("t12", (X1, 7.8), "trans-Δ²-Dodecenoyl-CoA")
pw.node("bo1", (X1, 5.0), "β oxidation → 6 acetyl-CoA", token="neutral")
pw.step("ole", "c12", enzyme="3 turns of β oxidation\n(3 acetyl-CoA)", enzyme_offset=0.2)
pw.step("c12", "t12", enzyme="Δ³,Δ²-enoyl-CoA\nisomerase", enzyme_offset=0.2)
pw.step("t12", "bo1", enzyme="hydratase …", enzyme_offset=0.2)
bio.label(ax, (X1, 3.9), "oleate: 9 acetyl-CoA, one FADH₂ fewer", size="tiny", color=P.muted())

# linoleate
X2 = 12.4
pw.node("lin", (X2, 13.4), "Linoleoyl-CoA (18:2, cis-Δ⁹,¹²)", token="lipid", bold=True)
pw.node("die", (X2, 10.6), "trans-Δ², cis-Δ⁴-Dienoyl-CoA (C10)")
pw.node("t3", (X2, 7.8), "trans-Δ³-Decenoyl-CoA")
pw.node("t2", (X2, 5.0), "trans-Δ²-Decenoyl-CoA")
pw.node("bo2", (X2, 2.4), "β oxidation → 5 acetyl-CoA", token="neutral")
pw.step("lin", "die", enzyme="3 turns, isomerase, 1 turn,\nacyl-CoA dehydrogenase", enzyme_offset=0.2)
pw.step("die", "t3", enzyme="2,4-dienoyl-CoA\nreductase", side=("NADPH + H⁺", "NADP⁺"), enzyme_offset=0.2,
        flip=True)
pw.step("t3", "t2", enzyme="enoyl-CoA\nisomerase", enzyme_offset=0.2, flip=True)
pw.step("t2", "bo2", enzyme_offset=0.2)

# propionyl-CoA
X3 = 21.8
pw.node("odd", (X3, 13.4), "Odd-chain acyl-CoA", token="lipid", bold=True)
pw.node("prop", (X3, 11.0), "Propionyl-CoA")
pw.node("dmm", (X3, 8.2), "D-Methylmalonyl-CoA")
pw.node("lmm", (X3, 5.4), "L-Methylmalonyl-CoA")
pw.node("scoa", (X3, 2.6), "Succinyl-CoA", token="highlight", bold=True)
pw.step("odd", "prop", enzyme="β oxidation\n(last thiolysis)", enzyme_offset=0.2)
pw.step("prop", "dmm", enzyme="Propionyl-CoA\ncarboxylase (biotin)", side=("ATP + HCO₃⁻", "ADP + Pᵢ"),
        enzyme_offset=0.2, side_span=0.9)
pw.step("dmm", "lmm", enzyme="Methylmalonyl-CoA\nepimerase", reversible=True, enzyme_offset=0.2)
pw.step("lmm", "scoa", enzyme="Methylmalonyl-CoA\nmutase (coenzyme B₁₂)", reversible=True, enzyme_offset=0.2)
bio.label(ax, (X3, 1.4), "→ citric acid cycle", size="tiny", color=P.muted())
