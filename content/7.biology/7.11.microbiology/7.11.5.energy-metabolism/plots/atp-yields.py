"""ATP per glucose (theoretical, from pathway stoichiometry). Fermentations: heterolactic 1,
Zymomonas (ED, ethanol) 1, homolactic 2, yeast ethanol 2, bifid shunt 2.5, butyrate (C. butyricum) 3.
Aerobic respiration: E. coli with NDH-2 + cytochrome bd (24 H+ from 10 NADH and 2 QH2) about 11,
with NDH-1 + cytochrome bo3 (88 H+) about 30, both at 10/3 H+ per ATP plus 4 ATP from substrate-level
phosphorylation; mitochondria about 32 (P/O 2.5 and 1.5, malate-aspartate shuttle)."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
sl = 4
ec_low = sl + (10 * 2 + 2 * 2) / (10 / 3)
ec_high = sl + (10 * 8 + 2 * 4) / (10 / 3)
mito = 4 + 10 * 2.5 + 2 * 1.5
rows = [("heterolactic (phosphoketolase)", 1, "ferm"), (r"ethanol, $\it{Zymomonas}$ (ED)", 1, "ferm"),
        ("homolactic", 2, "ferm"), ("ethanol, yeast", 2, "ferm"), ("bifid shunt", 2.5, "ferm"),
        (r"butyrate, $\it{C.\ butyricum}$", 3, "ferm"), (r"$\it{E.\ coli}$, NDH-2 + cyt $\it{bd}$", ec_low, "resp"),
        (r"$\it{E.\ coli}$, NDH-1 + cyt $\it{bo}_3$", ec_high, "resp"), ("mitochondrion", mito, "mito")]
tok = {"ferm": "drug", "resp": "enzyme", "mito": "mitochondrion"}
fig, ax = bio.canvas(20.0, 9.6)
a = charts.axes_at(ax, (7.2, 1.3, 12.0, 7.6))
y = np.arange(len(rows))
for k, (name, v, g) in enumerate(rows):
    a.barh(k, v, color=P.fill(tok[g]), edgecolor=charts.line(tok[g]), height=0.62)
    a.text(v + 0.4, k, (f"{v:.1f}".rstrip("0").rstrip(".") if g == "ferm" else f"≈{v:.0f}"), va="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.set_yticks(y)
a.set_yticklabels([r[0] for r in rows])
a.set_ylim(len(rows) - 0.5, -0.5)
a.set_xlim(0, 36)
a.axhline(5.5, color=P.muted(), lw=0.6, ls="--")
a.text(35, 2.5, "fermentation\n(substrate-level\nphosphorylation)", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="right")
a.text(20, 6.0, "respiration (O₂)", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="left")
charts.style_axes(a, "ATP per glucose (theoretical)", None)
