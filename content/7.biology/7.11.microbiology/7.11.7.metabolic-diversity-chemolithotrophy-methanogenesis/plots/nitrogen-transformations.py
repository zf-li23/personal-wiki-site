"""The microbial transformations of inorganic nitrogen, placed by the oxidation state of N.

Nitrification: ammonia monooxygenase (AMO) gives hydroxylamine, hydroxylamine oxidoreductase (HAO) nitrite
(ammonia-oxidizing bacteria, Nitrosomonas, and archaea, Nitrosopumilus); nitrite oxidoreductase (NXR) gives
nitrate (nitrite-oxidizing bacteria, Nitrobacter, Nitrospira). Comammox Nitrospira carry out both steps.
Denitrification: nitrate -> nitrite -> nitric oxide -> nitrous oxide -> N2 (Nar/Nap, Nir, Nor, Nos).
Anammox: nitrite is reduced to NO, NO and ammonium form hydrazine (hydrazine synthase), hydrazine is oxidized
to N2. DNRA: dissimilatory nitrate (nitrite) reduction to ammonium. Nitrogen fixation: nitrogenase reduces N2
to ammonia. Aerobic processes in blue-green, anaerobic ones in red-brown.
"""
import wikibio as bio
from wikibio import metabolism as M
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(20.0, 13.6)
pl = quant.Plot(ax, (1.6, 1.0, 0.01, 11.2), xlim=(0, 1), ylim=(-3.5, 5.5), ylabel="oxidation state of N",
                yticks=[(-3, "−3"), (-2, "−2"), (-1, "−1"), (0, "0"), (1, "+1"), (2, "+2"), (3, "+3"), (5, "+5")])


def Y(v):
    return float(pl.Y(v))


pw = M.Pathway(ax, size="small")
pw.node("nh4", (4.0, Y(-3)), "NH₄⁺ / NH₃", token="enzyme", bold=True)
pw.node("nh2oh", (4.0, Y(-1)), "NH₂OH")
pw.node("no2", (7.0, Y(3)), "NO₂⁻", token="highlight", bold=True)
pw.node("no3", (7.0, Y(5)), "NO₃⁻", token="highlight", bold=True)
pw.node("no", (13.0, Y(2)), "NO")
pw.node("n2o", (15.6, Y(1)), "N₂O")
pw.node("n2", (13.0, Y(0)), "N₂", token="neutral", bold=True)
pw.node("n2h4", (10.0, Y(-2)), "N₂H₄")

aer, ana = P.edge("enzyme"), P.edge("rna")
pw.step("nh4", "nh2oh", enzyme="AMO (O₂)", color=aer)
pw.step("nh2oh", "no2", enzyme="HAO", color=aer, bend=-0.15, enzyme_flip=True)
pw.step("no2", "no3", enzyme="NXR", color=aer, enzyme_flip=True)
pw.step("nh4", "no3", color=aer, dashed=True, bend=0.35, start=pw.anchor("nh4", "l") + (0, 0.2), end=pw.anchor("no3", "l"))
bio.label(ax, (2.3, Y(2.0)), "comammox\n($\\it{Nitrospira}$)", size="tiny", color=aer)
bio.label(ax, (4.9, Y(1.3)), "ammonia\noxidizers\n(AOB, AOA)", size="tiny", color=aer)
bio.label(ax, (8.6, Y(4.0)), "nitrite\noxidizers", size="tiny", color=aer, ha="left")

pw.step("no3", "no2", color=ana, bend=0.45, start=pw.anchor("no3", "r"), end=pw.anchor("no2", "r") + (0.0, 0.1))
pw.step("no2", "no", color=ana, enzyme="Nir", enzyme_flip=True)
pw.step("no", "n2o", color=ana, enzyme="Nor")
pw.step("n2o", "n2", color=ana, enzyme="Nos", bend=-0.2)
bio.label(ax, (14.8, Y(3.2)), "denitrification", size="small", color=ana, bold=True)
bio.label(ax, (8.6, Y(4.8)), "nitrate reduction", size="tiny", color=ana, ha="left")

pw.step("no", "n2h4", color=P.edge("protein"), bend=0.15, end=pw.anchor("n2h4", "t") + (0.2, 0))
pw.step("nh4", "n2h4", color=P.edge("protein"), bend=-0.1)
pw.step("n2h4", "n2", color=P.edge("protein"), enzyme="HDH", start=pw.anchor("n2h4", "r"))
bio.label(ax, (10.0, Y(-2.75)), "anammox (hydrazine synthase)", size="tiny", color=P.edge("protein"))

pw.step("no2", "nh4", color=P.muted(), dashed=True, bend=0.25, start=pw.anchor("no2", "b"), end=pw.anchor("nh4", "r") + (0, 0.15))
bio.label(ax, (6.8, Y(-0.9)), "DNRA", size="tiny", color=P.muted())

pw.step("n2", "nh4", color=P.edge("positive"), bend=0.35, start=pw.anchor("n2", "b"), end=pw.anchor("nh4", "r") + (0, -0.15))
bio.label(ax, (8.6, Y(-3.4)), "N₂ fixation (nitrogenase)", size="tiny", color=P.edge("positive"))
pl.legend([("aerobic", "enzyme", "-"), ("anaerobic respiration", "rna", "-"), ("anammox", "protein", "-"),
           ("assimilation / fixation", "positive", "-")], at=(15.2, 12.6))
