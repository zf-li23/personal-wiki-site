"""The nitrogenase complex and the energy cost of reduced nitrogen.

A: electron path. Reduced ferredoxin or flavodoxin reduces the [4Fe-4S] cluster of the Fe protein
(dinitrogenase reductase, a gamma2 dimer with two MgATP sites). The Fe protein with bound MgATP docks on
the MoFe protein (dinitrogenase, alpha2beta2); ATP binding lowers the reduction potential of the cluster
from about -300 to -420 mV, and one electron passes to the P cluster ([8Fe-7S]) and then to the FeMo
cofactor ([MoFe7S9C]-homocitrate), where N2 binds; the two ATP are hydrolysed and the Fe protein (with
MgADP) dissociates. Eight such cycles reduce one N2 to two NH3 and two protons to H2.
B: cost of one NH4+ incorporated into glutamate, counting a pair of electrons as one NAD(P)H and one
NAD(P)H as 2.5 ATP equivalents: fixation of N2 (8 ATP and 4 electrons per NH3, including H2 formation),
assimilatory reduction of nitrate (8 electrons, no ATP), and assimilation by glutamine synthetase and
glutamate synthase (1 ATP and 1 NAD(P)H).
"""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(27.0, 10.6, scale=0.42)
bio.panel(ax, "A", (0.2, 10.4))

# reductant
bio.box(ax, (2.0, 7.6), 3.0, 1.2, "ferredoxin", text="ferredoxin or\nflavodoxin (red.)", size="tiny")
# Fe protein
bio.box(ax, (6.6, 7.6), 2.6, 1.3, "enzyme", text="Fe protein (γ₂)\n[4Fe–4S]", size="tiny", radius=0.5)
bio.box(ax, (6.6, 9.4), 3.8, 0.7, "atp", text="2 MgATP → 2 MgADP + 2 Pᵢ", size="tiny")
bio.arrow(ax, (6.6, 9.0), (6.6, 8.5), kind="link", color=P.muted())
bio.label(ax, (6.6, 6.1), "E′° −300 → −420 mV\nwith MgATP bound", size="tiny", color=P.muted())
# MoFe protein
bio.box(ax, (13.4, 7.0), 6.0, 2.6, "protein", radius=0.8, zorder=5)
bio.label(ax, (13.4, 8.75), "MoFe protein (α₂β₂)", size="small", bold=True)
bio.box(ax, (11.9, 7.0), 1.8, 0.9, "highlight", text="P cluster\n[8Fe–7S]", size="tiny")
bio.box(ax, (14.9, 7.0), 2.2, 1.1, "drug", text="FeMo-co\nMoFe₇S₉C–\nhomocitrate", size="tiny")
for a, b in (((3.55, 7.6), (5.05, 7.6)), ((7.95, 7.4), (10.95, 7.1)), ((12.85, 7.0), (13.75, 7.0))):
    bio.arrow(ax, a, b, kind="process", color=P.edge("dna"), lw=2.0)
bio.label(ax, (9.4, 7.85), "1 e⁻ per\ncycle", size="tiny", color=P.edge("dna"))
bio.arrow(ax, (16.0, 7.0), (18.2, 7.0), kind="process", color=P.edge("dna"), lw=2.0)
bio.box(ax, (19.4, 8.0), 2.2, 0.8, "neutral", text="N₂ + 8 H⁺", size="tiny")
bio.box(ax, (19.4, 6.0), 2.4, 0.8, "positive", text="2 NH₃ + H₂", size="tiny")
bio.arrow(ax, (19.4, 7.55), (19.4, 6.45), kind="process")
bio.label(ax, (9.8, 4.3), "Fe protein binds, transfers one electron, hydrolyses 2 ATP and dissociates;\n"
          "dissociation is rate-limiting; 8 cycles: N₂ + 8 H⁺ + 8 e⁻ + 16 MgATP → 2 NH₃ + H₂ + 16 MgADP + 16 Pᵢ",
          size="tiny", color=P.muted())
bio.label(ax, (9.8, 3.1), "O₂ inactivates the Fe protein (half-life ≈ 30 s in air)", size="tiny",
          color=P.edge("negative"))

# B: costs
bio.panel(ax, "B", (21.0, 10.4))
c = charts.axes_at(ax, (22.4, 1.6, 4.3, 7.6))
names = ["N₂\nfixation", "NO₃⁻\nreduction"]
atp = np.array([8.0, 0.0])
red = np.array([2.0 * 2.5, 4.0 * 2.5])
gs = np.array([3.5, 3.5])
x = np.arange(2)
c.bar(x, atp, 0.6, color=P.fill("atp"), edgecolor=P.edge("atp"), label="ATP")
c.bar(x, red, 0.6, bottom=atp, color=P.fill("dna"), edgecolor=P.edge("dna"), label="electrons")
c.bar(x, gs, 0.6, bottom=atp + red, color=P.fill("enzyme"), edgecolor=P.edge("enzyme"), label="GS–GOGAT")
c.set_xticks(x, names)
c.set_ylim(0, 20)
charts.style_axes(c, None, "ATP equivalents per N")
c.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
