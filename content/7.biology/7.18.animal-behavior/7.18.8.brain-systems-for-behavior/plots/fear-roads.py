"""Two routes of fear (A) and the optimal flight criterion with asymmetric error costs (B, C; Example 8.3.1).

x_c* = d'/2 + ln((1 - pi) C_FA / (pi C_M)) / d',  pi = 0.05, C_M / C_FA = 100.
"""
import math

import wikibehav as wb
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(32, 11)

# A: pathways
bio.panel(ax, "A", (0.2, 10.8))
bio.box(ax, (2.0, 5.0), 3.0, 1.2, "neutral", text="Stimulus", size="small")
bio.box(ax, (6.6, 5.0), 3.2, 1.2, "receptor", text="Sensory thalamus", size="small")
bio.box(ax, (6.6, 8.6), 3.2, 1.2, "enzyme", text="Sensory cortex", size="small")
bio.box(ax, (11.2, 5.0), 3.0, 1.2, "drug", text="Lateral amygdala", size="small")
bio.box(ax, (11.2, 2.2), 3.0, 1.2, "drug", text="Central amygdala", size="small")
bio.box(ax, (6.6, 2.2), 3.2, 1.2, "positive", text="Defensive responses", size="small")
bio.arrow(ax, (3.6, 5.0), (4.9, 5.0))
bio.arrow(ax, (8.3, 5.0), (9.6, 5.0), color=P.edge("negative"), lw=2.2)
bio.label(ax, (8.95, 4.35), "low road", size="tiny", color=P.edge("negative"))
bio.label(ax, (8.95, 3.9), "fast, coarse", size="tiny", color=P.muted())
bio.arrow(ax, (6.6, 5.7), (6.6, 7.9))
bio.arrow(ax, (8.3, 8.4), (10.8, 5.7), color=P.edge("dna"), lw=2.2)
bio.label(ax, (10.9, 7.6), "high road", size="tiny", color=P.edge("dna"), ha="left")
bio.label(ax, (10.9, 7.15), "slow, detailed", size="tiny", color=P.muted(), ha="left")
bio.arrow(ax, (11.2, 4.3), (11.2, 2.9))
bio.arrow(ax, (9.6, 2.2), (8.3, 2.2))

# B: SDT panels
pi, ratio = 0.05, 100.0
pts = []
for k, (d, tok) in enumerate([(1.0, "negative"), (3.0, "dna")]):
    xc = d / 2 + math.log((1 - pi) / (pi * ratio)) / d
    p = quant.Plot(ax, (15.5, 6.3 - 4.9 * k, 8.0, 3.6), xlim=(-3.5, 6), ylim=(0, 0.48),
                   xlabel="sensory variable" if k == 1 else None, yticks=[])
    H, F = wb.sdt_panel(p, d=d, xc=xc, signal_token=tok, rates=False, labels=False)
    p.text(-3.3, 0.44, f"d' = {d:g}", size="small", ha="left")
    p.text(xc + 0.15, 0.44, f"criterion {xc:.2f}", size="tiny", ha="left")
    pts.append((F, H, tok))
bio.panel(ax, "B", (15.0, 10.8))
# C: ROC
q = quant.Plot(ax, (26.0, 1.4, 5.6, 8.0), xlim=(0, 1), ylim=(0, 1), xlabel="false-alarm rate", ylabel="hit rate",
               xticks=[0, 0.5, 1], yticks=[0, 0.5, 1])
wb.roc_panel(q, dprimes=(1.0, 3.0), tokens=("negative", "dna"), points=pts, labels=True)
bio.panel(ax, "C", (24.6, 10.8))
