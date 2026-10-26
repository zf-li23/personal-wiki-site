"""The Z scheme of oxygenic photosynthesis. Carriers of linear electron flow on a midpoint-potential axis
(reducing at the top; values from Blankenship, Molecular Mechanisms of Photosynthesis, 2nd ed., and
Rappaport and Diner 2008). Two photochemical steps, one in each photosystem, raise an electron from the
oxidizing P680+ / water level to the reducing NADP+ level; the excited states P680* and P700* lie 1.82 and
1.77 eV (680 and 700 nm photons) above the ground states. Dark electron transfer runs downhill between the
two photosystems through plastoquinone, the cytochrome b6f complex and plastocyanin, where it pumps protons.
Dashed: cyclic electron flow from ferredoxin back to the plastoquinone pool."""

import wikibio as bio
from wikibio import photosynthesis as ps
from wikibio.quant import line_color

P = bio.P
fig, ax = bio.canvas(27.0, 10.4)
zp, pos = ps.z_scheme(ax, (2.6, 0.8, 24.0, 8.0))
EC = line_color(ps.COLOR["electron"])
fdx, fdy = pos["Fd"]
bio.label(ax, ((pos["PQ pool"][0] + fdx) / 2 + 1.5, pos["PQ pool"][1] + 1.05), "cyclic electron flow", size="tiny",
          color=EC, italic=True)
bio.label(ax, (pos["H₂O"][0], pos["H₂O"][1] + 0.4), "O₂/H₂O", size="tiny", va="top", color=P.muted())
bio.label(ax, (pos["NADP⁺"][0], pos["NADP⁺"][1] - 0.38), "NADP⁺/NADPH", size="tiny", va="bottom", color=P.muted())
bio.label(ax, (2.8, 8.65), "more reducing", size="tiny", ha="left", va="top", color=P.muted())
bio.label(ax, (2.8, 0.95), "more oxidizing", size="tiny", ha="left", va="bottom", color=P.muted())
# overall span and the proton-pumping step
h2o, nadp = pos["H₂O"], pos["NADP⁺"]
bio.label(ax, (14.0, 9.9), "H₂O → NADP⁺: ΔE′° ≈ −1.14 V (uphill, +219 kJ per 2 e⁻), driven by 2 photons per electron", size="small")
pq, cytf = pos["PQ pool"], pos["Cyt f"]
bio.label(ax, ((pq[0] + cytf[0]) / 2, cytf[1] - 0.75), "Q cycle: H⁺ into lumen", size="tiny",
          color=line_color(ps.COLOR["proton"]), bold=True)
bio.label(ax, (pos["H₂O"][0] - 0.3, pos["H₂O"][1] + 1.0), "2 H₂O → O₂ + 4 H⁺\n(into the lumen)", size="tiny",
          color=line_color(ps.COLOR["proton"]), ha="left", va="bottom")
