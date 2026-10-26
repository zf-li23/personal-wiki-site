"""The inner mitochondrial membrane: the respiratory chain (Complexes I-IV, the ubiquinone pool and
cytochrome c), ATP synthase with a bovine c8 ring, and the two carriers that exchange cytosolic ADP and Pi
for matrix ATP (adenine nucleotide translocase, ANT, electrogenic; phosphate carrier, PiC, H+ symport).
Stoichiometries per pair of electrons from NADH: 10 H+ out; 8/3 H+ through Fo plus 1 H+ for transport per ATP."""

import wikibio as bio
from wikibio import bioenergetics as be
from wikibio.quant import line_color

P = bio.P
fig, ax = bio.canvas(26.0, 9.6)
y = 4.6
A = be.respiratory_chain(ax, (0.3, 25.7), y, ims=3.9, matrix=4.2, synthase=False)
s = be.atp_synthase(ax, 18.2, y, c_ring=8)
ch = s["channel"]
be.proton_arrow(ax, (ch[0], y + be.MH + 1.3), (ch[0], y - be.MH - 0.3), text="8/3 H⁺ per ATP", side="right", lw=1.8)
hd = s["head"]
bio.arrow(ax, (hd[0] - 1.4, hd[1] + 0.4), (hd[0] - 1.4, hd[1] - 0.55), kind="process", color=P.ink(), lw=1.1, head=0.16)
bio.label(ax, (hd[0] - 1.4, hd[1] + 0.62), "ADP + Pᵢ", size="tiny")
bio.label(ax, (hd[0] - 1.4, hd[1] - 0.8), "ATP", size="tiny", bold=True)

# adenine nucleotide translocase and phosphate carrier
ant = be.carrier(ax, 22.0, y, text="ANT", token="metabolite")
pic = be.carrier(ax, 24.2, y, text="PiC", token=be.COLOR["carrier"])
ink = P.ink()
bio.arrow(ax, (ant[0] - 0.25, y + 1.6), (ant[0] - 0.25, y - 1.3), kind="process", color=ink, lw=1.1, head=0.16)
bio.label(ax, (ant[0] - 0.3, y + 1.85), "ADP³⁻", size="tiny", ha="right")
bio.arrow(ax, (ant[0] + 0.25, y - 1.3), (ant[0] + 0.25, y + 1.6), kind="process", color=ink, lw=1.1, head=0.16)
bio.label(ax, (ant[0] + 0.3, y - 1.55), "ATP⁴⁻", size="tiny", ha="left")
bio.arrow(ax, (pic[0] - 0.25, y + 1.6), (pic[0] - 0.25, y - 1.3), kind="process", color=ink, lw=1.1, head=0.16)
bio.label(ax, (pic[0] - 0.3, y + 1.85), "H₂PO₄⁻", size="tiny", ha="right")
be.proton_arrow(ax, (pic[0] + 0.3, y + 1.6), (pic[0] + 0.3, y - 1.3), text="H⁺", side="right", lw=1.2)
bio.label(ax, (23.1, y - 2.6), "+1 H⁺ per ATP", size="tiny", color=line_color(be.COLOR["proton"]))

# key and balance
for k, (text, col) in enumerate((("electrons", line_color(be.COLOR["electron"])), ("protons", line_color(be.COLOR["proton"])))):
    x0 = 9.4 + k * 2.6
    bio.arrow(ax, (x0, 0.75), (x0 + 0.7, 0.75), kind="process", color=col, lw=1.4, head=0.18)
    bio.label(ax, (x0 + 0.85, 0.75), text, size="tiny", ha="left")
bio.label(ax, (25.5, y + 3.4), "NADH → ½O₂: 10 H⁺ out  ·  3.7 H⁺ in per ATP  ·  ≈ 2.7 ATP", size="small",
          ha="right", color=P.ink())
