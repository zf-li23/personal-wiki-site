"""Microtubule structure (schematic).

A: the alpha/beta-tubulin heterodimer (8 nm; beta towards the plus end; the GTP on alpha is buried and never
hydrolysed, that on beta is exchangeable) and a protofilament of dimers stacked head to tail.
B: a cross-section: 13 protofilaments form a tube 25 nm across; the B lattice has one seam (dashed).
C: a growing microtubule with a cap of GTP-tubulin (gold) at its plus end and a slightly flared sheet of
protofilaments; behind the cap the beta-tubulin carries GDP (blue).
D: a shrinking microtubule after a catastrophe: the cap is lost and GDP protofilaments peel back in curls.
E: a gamma-tubulin ring complex (gold) templating the minus end of a new microtubule.
"""

import numpy as np

import wikibio as bio
from wikibio import cytoskel as C

P = bio.P
fig, ax = bio.canvas(24.0, 11.0)

bio.panel(ax, "A", (0.1, 10.9))
C.tubulin_dimer(ax, (1.3, 8.6), 1.3, angle=90, beta="GTP")
bio.label(ax, (2.2, 9.05), "β-tubulin (exchangeable GTP/GDP)", size="tiny", ha="left")
bio.label(ax, (2.2, 8.2), "α-tubulin (GTP buried)", size="tiny", ha="left")
for k in range(5):
    C.tubulin_dimer(ax, (6.8, 6.6 + k * 0.8), 0.8, angle=90, beta="GDP" if k < 4 else "GTP")
C.end_label(ax, (6.8, 10.75), "+", size="small")
C.end_label(ax, (6.8, 6.0), "-", size="small")
bio.label(ax, (7.4, 8.6), "protofilament", size="tiny", ha="left")

bio.panel(ax, "B", (9.6, 10.9))
C.mt_cross_section(ax, (11.8, 8.5), 1.2)
bio.label(ax, (11.8, 6.75), "13 protofilaments, 25 nm", size="tiny")
bio.label(ax, (12.9, 10.3), "seam", size="tiny", ha="left", color=P.muted())

bio.panel(ax, "E", (15.4, 10.9))
top = C.gamma_turc(ax, (18.3, 7.0), 1.6, mt_length=2.3)
bio.callout(ax, (19.1, 6.9), (20.6, 6.3), "γ-TuRC", size="tiny")
bio.label(ax, (18.3, 9.95), "+", size="small", bold=True)
bio.label(ax, (21.0, 8.6), "minus end\ncapped by\nthe template", size="tiny", ha="left", color=P.muted())

bio.panel(ax, "C", (0.1, 5.2))
C.microtubule_lattice(ax, (1.0, 3.9), (22.5, 3.9), width=1.5, rows=6, cap=0.12, plus_end="growing", dimer=0.62)
bio.label(ax, (20.3, 4.95), "GTP cap", size="tiny", color=P.muted())
bio.label(ax, (12.0, 4.95), "growing: GDP-tubulin lattice held straight by the cap", size="tiny", color=P.muted())

bio.panel(ax, "D", (0.1, 2.3))
C.microtubule_lattice(ax, (1.0, 1.1), (21.0, 1.1), width=1.5, rows=6, plus_end="shrinking", dimer=0.62, curl=1.2)
bio.label(ax, (12.0, 2.15), "shrinking: protofilaments curl outward and fall apart", size="tiny", color=P.muted())
C.nucleotide_legend(ax, (1.2, 5.85), kind="tubulin", step=1.8)
