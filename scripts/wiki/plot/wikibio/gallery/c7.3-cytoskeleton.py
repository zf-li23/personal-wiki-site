# The cytoskeleton (wikibio.cytoskel). A: an actin filament with ATP, ADP-Pi and ADP subunits and myosin S1
# arrowheads pointing to the minus end; an Arp2/3 branch. B: a dendritic lamellipodium network, a filopodium
# and a stress fibre. C: microtubule lattices with a GTP cap (growing) and curling protofilaments (shrinking),
# a cross-section with 13 protofilaments, a gamma-TuRC template. D: a centrosome, a centriole cross-section
# and side view. E: motors (kinesin from physiology, dynein-dynactin-adaptor, myosin V). F: intermediate-
# filament assembly. G: axonemes 9+2 and 9+0. H: a metaphase and an anaphase spindle.
import wikibio as bio
from wikibio import cytoskel as C
from wikibio import physiology as phys

P = bio.P
fig, ax = bio.canvas(26, 34.4)
ax.set_ylim(-4.6, 29.8)

bio.panel(ax, "A", (0.2, 29.8))
C.actin_filament(ax, (1.0, 28.4), (9.5, 28.4), r=0.13, states="DDDDDPPTT", decorate=True)
C.nucleotide_legend(ax, (1.2, 27.4), kind="actin")
C.branch(ax, (11.0, 27.6), (17.5, 27.6), at=0.35, length=2.2, detailed=True, r=0.1, states="DDPT")

bio.panel(ax, "B", (0.2, 26.3))
C.lamellipodium(ax, 0.8, 9.5, front=25.6, depth=2.8, seed=3)
C.filopodium(ax, (12.0, 22.9), length=3.0, width=0.55, angle=80)
C.stress_fiber(ax, (14.5, 23.6), (24.5, 23.6), width=0.55, units=4)
C.myosin_minifilament(ax, (19.5, 25.4), 2.0)

bio.panel(ax, "C", (0.2, 21.8))
C.microtubule_lattice(ax, (1.0, 20.6), (9.0, 20.6), width=0.9, cap=0.18, plus_end="growing")
C.microtubule_lattice(ax, (1.0, 18.8), (9.0, 18.8), width=0.9, plus_end="shrinking")
C.nucleotide_legend(ax, (1.2, 17.6), kind="tubulin", step=1.6)
C.mt_cross_section(ax, (11.5, 19.8), 0.75)
C.tubulin_dimer(ax, (13.5, 19.8), 0.8, beta="GTP")
C.gamma_turc(ax, (16.0, 18.4), 1.1)
C.tube(ax, (18.0, 18.4), (24.5, 20.6), width=0.3, plus="dot")

bio.panel(ax, "D", (0.2, 16.6))
C.centrosome(ax, (4.0, 13.6), 0.8, microtubules=16, length=2.4)
C.centriole_section(ax, (10.5, 13.8), 1.3)
C.centriole(ax, (14.5, 13.8), 1.8, 0.7, angle=90)
C.centriole_section(ax, (18.0, 13.8), 1.0, kind="doublet", cartwheel=False)

bio.panel(ax, "E", (0.2, 11.0))
C.tube(ax, (0.8, 8.0), (12.0, 8.0), width=0.4)
phys.kinesin(ax, (2.6, 8.4), (3.6, 8.4), (3.4, 10.4), head=0.5)
C.dynein(ax, (7.5, 8.2), (7.6, 10.6), size=0.5)
C.actin_filament(ax, (13.0, 8.0), (24.5, 8.0), r=0.12, ends=True)
C.myosin_v(ax, (16.0, 8.2), (19.0, 8.2), (17.6, 10.6))
C.myosin_head(ax, (22.5, 8.15), size=0.55, lever=50, nucleotide="ADP")

bio.panel(ax, "F", (0.2, 6.6))
y = 5.8
for k, st in enumerate(("monomer", "dimer", "tetramer", "ulf", "filament")):
    C.if_assembly(ax, (1.0 + k * 2.6 if k < 4 else 11.0, y), st, length=1.5 if k < 4 else 1.8)
C.if_filament(ax, (1.0, 4.4), (12.0, 4.4), width=0.32)

bio.panel(ax, "G", (13.0, 6.6))
C.axoneme(ax, (16.2, 3.4), 1.7, kind="9+2", labels=True)
C.axoneme(ax, (21.8, 3.4), 1.7, kind="9+0", labels=True)

bio.panel(ax, "H", (0.2, -0.2))
C.spindle(ax, (4.5, -2.6), 3.0, 3.0, chromosomes=3)
C.spindle(ax, (16.0, -2.6), 3.6, 3.0, chromosomes=3, stage="anaphase", astral=3)
