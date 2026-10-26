# Oxidative phosphorylation. (A) The respiratory chain in the inner mitochondrial membrane, matrix (N side)
# below: Complex I passes electrons from NADH (via FMN and a chain of Fe-S clusters) to ubiquinone and pumps
# 4 H+; Complex II feeds electrons from succinate into the quinone pool without pumping; Complex III oxidizes
# ubiquinol in the Q cycle (2 H+ taken up at Qn, 4 H+ released at Qp) and reduces cytochrome c; Complex IV
# reduces O2 to water with substrate protons and pumps 2 H+ (all per pair of electrons). Protons return
# through ATP synthase (bovine c8 ring). (B) The binding-change mechanism: F1 seen from the membrane;
# each 120-degree step of gamma converts the tight (ATP), loose (ADP + Pi) and open (empty) beta sites into
# one another. (C) The c ring of Fo (8 subunits in mammals) with its essential carboxylates; (D) P/O ratios
# predicted from the c-ring size (10 H+ per NADH, 6 per succinate, 1 H+ per ATP for transport).
import numpy as np

import wikibio as bio
from wikibio import bioenergetics as be
from wikibio.quant import Plot, line_color

P = bio.P
fig, ax = bio.canvas(22.0, 17.6)

# ---- A: the chain -----------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 17.5))
A = be.respiratory_chain(ax, (0.4, 21.6), 12.9, ims=3.6, matrix=3.9)
bio.label(ax, (21.4, 12.9 + 2.5), "pH ≈ 7.0, +", size="small", ha="right", color=P.muted())
bio.label(ax, (21.4, 12.9 - 2.5), "pH ≈ 7.8, −", size="small", ha="right", color=P.muted())
for k, (text, col) in enumerate((("electrons", line_color(be.COLOR["electron"])), ("protons", line_color(be.COLOR["proton"])))):
    x0 = 9.2 + k * 2.6
    bio.arrow(ax, (x0, 8.75), (x0 + 0.7, 8.75), kind="process", color=col, lw=1.4, head=0.18)
    bio.label(ax, (x0 + 0.85, 8.75), text, size="tiny", ha="left")

# ---- B: binding change -------------------------------------------------------------------------------------
bio.panel(ax, "B", (0.1, 7.9))
seq = [("ATP", "empty", "ADP"), ("empty", "ADP", "ATP"), ("ADP", "ATP", "empty")]
for k, states in enumerate(seq):
    c = (1.9 + 3.5 * k, 4.6)
    be.f1_top(ax, c, 1.05, states=states)
    if k < 2:
        bio.arrow(ax, (c[0] + 1.3, c[1] + 0.9), (c[0] + 2.2, c[1] + 0.9), kind="process", color=P.ink(), head=0.18)
        bio.label(ax, (c[0] + 1.75, c[1] + 1.2), "120°", size="tiny")
bio.label(ax, (5.4, 2.35), "proton flow turns γ; each β site cycles loose → tight → open", size="tiny")

# ---- C: c ring ----------------------------------------------------------------------------------------------
bio.panel(ax, "C", (10.6, 7.9))
be.c_ring(ax, (12.3, 4.6), 0.95, n=8)
bio.label(ax, (12.3, 4.6), "c₈", size="small", bold=True)
bio.label(ax, (12.3, 3.05), "8 H⁺ per turn = 3 ATP", size="tiny")

# ---- D: P/O ratio ---------------------------------------------------------------------------------------------
bio.panel(ax, "D", (14.4, 7.9))
p = Plot(ax, (15.9, 1.2, 5.6, 5.6), xlim=(7, 16), ylim=(0, 3.2), xlabel="c subunits per ring", ylabel="P/O",
         xticks=[8, 10, 12, 14, 16], yticks=[0, 1, 2, 3])
c = np.arange(8, 16)
p.line(c, be.p_o(c, 10), be.COLOR["complex_i"], text="NADH", at=0.15)
p.line(c, be.p_o(c, 6), be.COLOR["complex_ii"], text="succinate", at=0.15)
p.points(c, be.p_o(c, 10), be.COLOR["complex_i"])
p.points(c, be.p_o(c, 6), be.COLOR["complex_ii"])
p.hline(2.5, text="2.5", side="right")
p.hline(1.5, text="1.5", side="right")
