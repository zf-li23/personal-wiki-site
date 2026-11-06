# Electron transport in the inner membrane of a plant mitochondrion (schematic).
# (A) The chain shared with all eukaryotes: Complexes I-IV, ubiquinone, cytochrome c and ATP synthase, with
# 4 + 4 + 2 protons pumped per electron pair. (B) The plant-specific, non-proton-pumping components that feed
# the same ubiquinone pool or drain it: external NAD(P)H dehydrogenases (NDex, Ca2+-dependent, facing the
# intermembrane space), the internal rotenone-insensitive NADH dehydrogenase (NDin, matrix side), the
# alternative oxidase (AOX, ubiquinol -> O2, cyanide-insensitive, inhibited by SHAM) and the uncoupling
# protein (UCP), which lets protons return without ATP synthesis.
import wikibio as bio
from wikibio import bioenergetics as be

P = bio.P
fig, ax = bio.canvas(23, 19)

# A: classical chain
bio.panel(ax, "A", (0.3, 18.5))
bio.label(ax, (1.0, 18.5), "Standard respiratory chain", size="small", bold=True, ha="left")
be.respiratory_chain(ax, (0.5, 22.5), 13.6, ims=3.4, matrix=3.6)

# B: plant-specific bypasses
y = 4.6
bio.panel(ax, "B", (0.3, 9.4))
bio.label(ax, (1.0, 9.4), "Plant-specific non-phosphorylating components", size="small", bold=True, ha="left")
be.inner_membrane(ax, (0.5, 22.5), y, ims=3.4, matrix=3.6)
ec = be.line_color(be.COLOR["electron"])

# external NAD(P)H dehydrogenase on the P side
ndex = (4.0, y + 0.95)
bio.protein(ax, ndex, 1.9, 1.0, "enzyme", text="NDex", size="tiny")
bio.label(ax, (4.0, y + 2.25), "NAD(P)H → NAD(P)⁺", size="tiny")
bio.label(ax, (4.0, y + 1.85), "(cytosolic, Ca²⁺)", size="tiny", color=P.muted())
# internal NADH dehydrogenase on the N side
ndin = (7.6, y - 0.95)
bio.protein(ax, ndin, 1.9, 1.0, "enzyme", text="NDin", size="tiny")
bio.label(ax, (7.6, y - 2.2), "NADH → NAD⁺ (matrix)", size="tiny")
bio.label(ax, (7.6, y - 2.6), "rotenone-insensitive", size="tiny", color=P.muted())
# ubiquinone pool
q = (10.6, y)
be.ubiquinone(ax, q, reduced=True, text="UQ pool")
be.electron_arrow(ax, (ndex[0] + 0.9, ndex[1] - 0.3), (q[0] - 0.3, q[1] + 0.1), bend=-0.15)
be.electron_arrow(ax, (ndin[0] + 0.9, ndin[1] + 0.3), (q[0] - 0.3, q[1] - 0.1), bend=0.15)
# to complex III (cytochrome pathway) and to AOX
c3 = be.complex_iii(ax, 14.3, y)
be.electron_arrow(ax, (q[0] + 0.3, q[1] + 0.15), (c3["qp"][0] - 0.1, c3["qp"][1]), bend=-0.1)
bio.label(ax, (14.3, y + 2.6), "→ cyt c → IV (cytochrome pathway)", size="tiny", color=P.muted())
aox = (12.3, y - 1.1)
bio.protein(ax, aox, 1.5, 0.95, "positive", text="AOX", size="tiny")
be.electron_arrow(ax, (q[0] + 0.05, q[1] - 0.3), (aox[0] - 0.2, aox[1] + 0.45), bend=0.1)
bio.label(ax, (12.3, y - 2.2), "½O₂ → H₂O", size="tiny")
bio.label(ax, (12.3, y - 2.6), "CN⁻-insensitive; SHAM inhibits", size="tiny", color=P.muted())
# uncoupling protein
ux = 18.6
be.carrier(ax, ux, y, text="UCP", token="positive")
be.proton_arrow(ax, (ux, y + 1.6), (ux, y - 1.3), text="H⁺", side="right")
bio.label(ax, (ux, y - 2.2), "H⁺ return without ATP", size="tiny", color=P.muted())
bio.label(ax, (21.3, y + 1.9), "no H⁺ pumped:", size="tiny", color=P.muted())
bio.label(ax, (21.3, y + 1.5), "energy → heat", size="tiny", color=P.muted())
