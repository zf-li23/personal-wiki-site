"""How one animal cell coordinates growth, division, movement, fate and death: an SBGN activity-flow map.

Inputs (left) are what the cell senses: nutrients, growth factors, the stiffness of the matrix,
contact with neighbours, Notch ligands on neighbours, DNA damage. Integrating modules (middle) are
the switches of 7.3.18-7.3.25: mTORC1 (an AND gate on the lysosome), Ras-ERK and PI3K-PKB, the
Rho GTPases, Hippo-YAP, Notch-Hes, p53 and the Rb-E2F switch. Outcomes (hexagons, right) are the
cell's decisions. Arrows with open heads activate, bars inhibit; dashed arcs are slower or indirect.
"""

import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(27.0, 14.0)
d = network.Diagram(ax)

W, Hh = 4.6, 1.0
inputs = [
    ("nut", 12.6, "amino acids, energy", "metabolite"),
    ("gf", 10.6, "growth factors (RTKs)", "receptor"),
    ("ecm", 8.4, "matrix, stiffness (integrins)", "receptor"),
    ("cad", 6.2, "cell–cell contact (cadherins)", "receptor"),
    ("dll", 4.3, "Delta on neighbours", "receptor"),
    ("dmg", 1.8, "DNA damage", "negative"),
]
for k, y, t, tok in inputs:
    d.activity(k, (2.6, y), t, w=W, h=Hh, token=tok, size="small")

mid = [
    ("mtor", (9.0, 12.6), "mTORC1 (lysosome)", "lysosome"),
    ("erk", (9.0, 10.6), "Ras–ERK, PI3K–PKB", "enzyme"),
    ("rho", (9.0, 8.4), "Rac / Rho GTPases", "enzyme"),
    ("hippo", (9.0, 6.2), "Hippo (MST, LATS)", "enzyme"),
    ("notch", (9.0, 4.3), "Notch → Hes1", "protein"),
    ("p53", (9.0, 1.8), "ATM/ATR → p53", "protein"),
    ("rb", (15.2, 10.6), "cyclin D → Rb ⊣ E2F", "protein"),
    ("yap", (15.2, 6.2), "YAP / TAZ", "protein"),
    ("bcl", (15.2, 0.8), "Bcl-2 family, caspases", "protein"),
]
for k, at, t, tok in mid:
    d.activity(k, at, t, w=W, h=Hh, token=tok, size="small")

outs = [
    ("grow", (22.6, 12.6), "growth (ribosomes)"),
    ("div", (22.6, 10.6), "division (Cdk1)"),
    ("move", (22.6, 8.4), "shape, migration"),
    ("fate", (22.6, 4.3), "fate choice"),
    ("arrest", (22.6, 2.6), "arrest, senescence"),
    ("die", (22.6, 0.8), "apoptosis"),
]
for k, at, t in outs:
    d.phenotype(k, at, t, w=4.4, h=1.05, size="small")

pos, neg = "positive", "negative"
d.connect("nut", "mtor", pos)
d.connect("gf", "erk", pos)
d.connect("erk", "mtor", pos, text="AND (Rag + Rheb)", text_offset=(1.45, 0.0))
d.connect("mtor", "grow", pos, via=[(15.2, 12.6)])
d.connect("erk", "rb", pos)
d.connect("rb", "div", pos, text="restriction point", text_offset=(0.0, 0.4))
d.connect("grow", "div", pos, dashed=True, bend=0.0, text="size (adder)", text_offset=(1.25, 0.0))
d.connect("ecm", "rho", pos)
d.connect("ecm", "erk", pos, dashed=True)
d.connect("rho", "move", pos)
d.connect("rho", "yap", pos, text="tension", text_offset=(-0.5, -0.2))
d.connect("cad", "hippo", pos)
d.connect("hippo", "yap", neg)
d.connect("yap", "div", pos)
d.connect("dll", "notch", pos)
d.connect("notch", "fate", pos, text="lateral inhibition", text_offset=(0.0, 0.35))
d.connect("dmg", "p53", pos)
d.connect("p53", "arrest", pos, text="p21 ⊣ Cdks", text_offset=(0.0, 0.4))
d.connect("p53", "bcl", pos, text="Puma, Noxa", text_offset=(-0.3, -0.55))
d.connect("bcl", "die", pos)

bio.label(ax, (2.6, 13.6), "what the cell senses", size="small", color=P.muted())
bio.label(ax, (12.1, 13.6), "integrating switches", size="small", color=P.muted())
bio.label(ax, (22.6, 13.6), "decisions", size="small", color=P.muted())
