"""Cholesterol synthesis in four stages; the height of each intermediate rises with its number of carbons.

Stage 1 (cytosol and ER): thiolase and cytosolic HMG-CoA synthase condense three acetyl-CoA (C2) to
HMG-CoA (C6); HMG-CoA reductase (ER membrane; 2 NADPH) reduces it to mevalonate, the committed step.
Stage 2: three ATP phosphorylate mevalonate; decarboxylation gives isopentenyl pyrophosphate (IPP, C5),
which an isomerase converts to dimethylallyl pyrophosphate (DMAPP). Stage 3: head-to-tail condensations
give geranyl (C10) and farnesyl pyrophosphate (FPP, C15); squalene synthase joins two FPP head to head
(NADPH) to squalene (C30). Stage 4: squalene monooxygenase (O2, NADPH) forms 2,3-oxidosqualene, which
lanosterol synthase cyclizes to lanosterol (C30); about 19 further reactions remove three methyl carbons
and give cholesterol (C27). FPP is also the branch point to dolichols, ubiquinone, heme A and protein
prenylation (farnesyl and geranylgeranyl groups).
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(28.0, 14.6, scale=0.42)


def Y(c):
    return 1.2 + 0.38 * c


stages = [(1.3, 8.6, "Stage 1: acetyl-CoA → mevalonate"), (8.8, 13.2, "Stage 2: activated isoprenes"),
          (13.4, 20.4, "Stage 3: condensation to squalene"), (20.6, 27.8, "Stage 4: cyclization")]
for x0, x1, t in stages:
    ax.add_patch(FancyBboxPatch((x0, 0.3), x1 - x0, 13.9, boxstyle="round,pad=0,rounding_size=0.4",
                                         facecolor=P.mix(P.fill("neutral"), P.surface(), 0.8), edgecolor="none",
                                         zorder=0))
    bio.label(ax, ((x0 + x1) / 2, 13.75), t, size="tiny", bold=True, color=P.muted())

pw = M.Pathway(ax, size="small")
pw.node("ac", (2.6, Y(2)), "3 Acetyl-CoA")
pw.node("aac", (3.6, Y(4) + 1.6), "Acetoacetyl-CoA")
pw.node("hmg", (5.0, Y(6) + 3.4), "HMG-CoA")
pw.node("mev", (7.2, Y(6)), "Mevalonate", token="highlight", bold=True)
pw.node("ipp", (10.0, Y(5)), "IPP", token="lipid", bold=True)
pw.node("dmapp", (12.2, Y(5)), "DMAPP", token="lipid")
pw.node("gpp", (15.0, Y(10)), "Geranyl-PP (C10)")
pw.node("fpp", (17.6, Y(15)), "Farnesyl-PP (C15)", bold=True)
pw.node("sq", (18.9, Y(30)), "Squalene (C30)", token="lipid", bold=True)
pw.node("ox", (23.4, Y(30)), "2,3-Oxidosqualene")
pw.node("lan", (24.2, Y(30) - 2.4), "Lanosterol (C30)")
pw.node("chol", (26.2, Y(27) - 3.2), "Cholesterol (C27)", token="lipid", bold=True)
pw.step("ac", "aac", enzyme="thiolase", enzyme_offset=0.15, enzyme_flip=True)
pw.step("aac", "hmg", enzyme="HMG-CoA\nsynthase", enzyme_offset=0.15, enzyme_flip=True)
pw.step("hmg", "mev", side=("2 NADPH", "2 NADP⁺ + CoA"), side_span=0.8)
bio.label(ax, (5.2, Y(6) + 1.2), "HMG-CoA\nreductase", size="tiny", bold=True, color=P.edge("enzyme"))
pw.step("mev", "ipp", enzyme="3 ATP; − CO₂", enzyme_offset=0.15)
pw.step("ipp", "dmapp", reversible=True, enzyme="isomerase", enzyme_offset=0.15, enzyme_flip=True)
pw.step("dmapp", "gpp", side=("IPP", "PPᵢ"), flip=True)
pw.step("gpp", "fpp", side=("IPP", "PPᵢ"), flip=True)
pw.step("fpp", "sq", side=("FPP + NADPH", "2 PPᵢ"), flip=True)
bio.label(ax, (19.8, Y(22)), "squalene synthase\n(head to head)", size="tiny", bold=True, color=P.edge("enzyme"),
          ha="left")
pw.step("sq", "ox", side=("O₂ + NADPH", None))
bio.label(ax, (21.15, Y(30) - 0.85), "squalene\nmonooxygenase", size="tiny", bold=True, color=P.edge("enzyme"))
pw.step("ox", "lan", enzyme="lanosterol\nsynthase", enzyme_offset=0.15)
pw.step("lan", "chol", enzyme="~19 steps;\n− 3 C", enzyme_offset=0.15, enzyme_flip=True)

bio.arrow(ax, (17.6, Y(15) - 0.4), (17.6, Y(15) - 2.0), kind="process", color=P.muted(), dashed=True)
bio.label(ax, (17.6, Y(15) - 2.6), "dolichols, ubiquinone side chain,\nheme A, prenylated proteins (C15, C20)",
          size="tiny", color=P.muted())
bio.label(ax, (5.0, Y(6) - 0.9), "committed step;\ntarget of statins", size="tiny", bold=True,
          color=P.edge("negative"))
bio.label(ax, (24.2, 3.0), "per cholesterol: 18 acetyl-CoA,\n18 ATP (isoprenes), NADPH", size="tiny", color=P.muted())
