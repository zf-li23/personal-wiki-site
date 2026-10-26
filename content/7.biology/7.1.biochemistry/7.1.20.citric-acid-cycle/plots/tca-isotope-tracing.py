"""Fate of a 14C label from acetyl-CoA in the citric acid cycle, by explicit atom mapping.

Oxaloacetate carbons C1 (carboxyl next to C=O), C2 (C=O), C3 (CH2), C4 (carboxyl). Citrate synthase joins the
acetyl methyl to C2. Aconitase acts on the oxaloacetate-derived arm (prochirality, Ogston), so isocitrate
dehydrogenase releases oxaloacetate C1 and alpha-ketoglutarate dehydrogenase oxaloacetate C4. Succinyl-CoA
carries (OAA C3, OAA C2, methyl, acetyl carboxyl); succinate and fumarate are symmetric, so each new
oxaloacetate has these four carbons in either order with probability 1/2. A single pulse of labelled
acetyl-CoA enters turn 1; later turns use unlabelled acetyl-CoA.
A: fraction of the label released as CO2 in each turn. B: cumulative fraction released."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P


def trace(label, turns=10):
    """label: 'methyl' or 'carboxyl'. Returns the fraction of the label released in each turn."""
    oaa = np.zeros(4)  # label probability on OAA C1..C4 (index 0..3)
    released = []
    for n in range(turns):
        methyl = 1.0 if (n == 0 and label == "methyl") else 0.0
        carb = 1.0 if (n == 0 and label == "carboxyl") else 0.0
        released.append(oaa[0] + oaa[3])  # C1 by isocitrate DH, C4 by alpha-KG DH
        succ = np.array([oaa[2], oaa[1], methyl, carb])  # succinate positions 0..3
        oaa = 0.5 * succ + 0.5 * succ[::-1]  # random orientation of the symmetric intermediates
    return np.array(released)


turns = np.arange(1, 11)
rm, rc = trace("methyl"), trace("carboxyl")
fig, ax = bio.canvas(22.0, 9.0)
A = charts.axes_at(ax, (1.9, 1.3, 8.2, 6.6))
w = 0.38
A.bar(turns - w / 2, rc, w, color=P.fill("drug"), edgecolor=P.edge("drug"), label="[1-¹⁴C]acetyl (carboxyl)")
A.bar(turns + w / 2, rm, w, color=P.fill("channel"), edgecolor=P.edge("channel"), label="[2-¹⁴C]acetyl (methyl)")
A.set_xticks(turns)
A.set_ylim(0, 1.05)
charts.style_axes(A, "turn of the cycle", "fraction of label released as CO₂")
A.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.4, 8.6))

B = charts.axes_at(ax, (13.0, 1.3, 8.2, 6.6))
B.plot(turns, np.cumsum(rc), "o-", color=charts.line("drug"), lw=2.0, ms=4, label="carboxyl label")
B.plot(turns, np.cumsum(rm), "s-", color=charts.line("channel"), lw=2.0, ms=4, label="methyl label")
B.set_xticks(turns)
B.set_ylim(0, 1.05)
charts.style_axes(B, "turn of the cycle", "cumulative fraction released")
B.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "B", (11.5, 8.6))
