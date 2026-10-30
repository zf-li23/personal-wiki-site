"""Thyroid hormone and amphibian metamorphosis (Xenopus; schematic).

A: the endocrine axis: hypothalamic CRH (in frogs the main TSH-releasing hormone) stimulates pituitary TSH, which
stimulates the thyroid to release T4; in target cells type II deiodinase (D2) converts T4 to the active T3, type III
deiodinase (D3) inactivates T3 to T2; T3 binds the thyroid hormone receptor (TR with RXR) on DNA, which without
hormone recruits corepressors and with hormone coactivators; TR-beta is a direct target, a positive feedback.
B: plasma thyroid hormone over the Nieuwkoop-Faber stages (schematic, peak at metamorphic climax, stage 62) and the
order of responses: limb growth at low hormone (premetamorphosis), tail resorption at the peak.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(30.0, 10.0)
bio.panel(ax, "A", (0.2, 9.8))
N = {"crh": (2.4, 8.6, "Hypothalamus: CRH", "neuron"), "tsh": (2.4, 6.6, "Pituitary: TSH", "protein"),
     "thy": (2.4, 4.6, "Thyroid: T4", "highlight"), "t3": (7.2, 4.6, "Target cell: T3", "drug"),
     "t2": (12.0, 4.6, "T2 (inactive)", "neutral"), "tr": (7.2, 2.0, "TR/RXR on DNA", "dna")}
for k, (x, y, t, tk) in N.items():
    bio.box(ax, (x, y), 3.6, 1.0, tk, t, size="small")
bio.arrow(ax, (2.4, 8.05), (2.4, 7.15), kind="activation", lw=1.0)
bio.arrow(ax, (2.4, 6.05), (2.4, 5.15), kind="activation", lw=1.0)
bio.arrow(ax, (4.25, 4.6), (5.35, 4.6), kind="process", lw=1.0)
bio.label(ax, (4.8, 5.0), "D2", size="tiny", color=P.muted())
bio.arrow(ax, (9.05, 4.6), (10.15, 4.6), kind="process", lw=1.0)
bio.label(ax, (9.6, 5.0), "D3", size="tiny", color=P.muted())
bio.arrow(ax, (7.2, 4.05), (7.2, 2.55), kind="activation", lw=1.0)
bio.arrow(ax, (9.05, 2.0), (10.6, 2.0), kind="process", lw=1.0)
bio.label(ax, (10.8, 2.0), "TRβ, MMPs,\ncaspases, …", size="tiny", ha="left")
bio.arrow(ax, (11.0, 1.55), (8.4, 1.45), kind="activation", bend=0.4, lw=0.9, dashed=True)
bio.label(ax, (9.7, 0.6), "TRβ autoinduction", size="tiny", color=P.muted())
bio.label(ax, (7.2, 0.15), "no T3: corepressors; T3: coactivators", size="tiny", color=P.muted())

bio.panel(ax, "B", (15.6, 9.8))
pa = C.axes_at(ax, (17.2, 1.8, 11.8, 6.8))
st = np.linspace(45, 66, 300)
th = 0.05 + np.exp(-((st - 62) / 3.0) ** 2) * (st < 62) + np.exp(-((st - 62) / 1.6) ** 2) * (st >= 62)
pa.plot(st, th, color=Q.line_color("highlight"), lw=2.0)
for x0, x1, txt, y in ((51, 57, "hindlimb growth", 0.18), (57, 60, "forelimb emergence", 0.45), (60, 63, "gut, skin, brain remodelling", 0.86),
                       (62, 66, "tail resorption", 1.0)):
    pa.plot([x0, x1], [y, y], color=P.muted(), lw=2.4, solid_capstyle="butt")
    pa.text((x0 + x1) / 2, y + 0.04, txt, fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="center", va="bottom")
for x0, x1, nm in ((45, 54, "premetamorphosis"), (54, 58, "prometamorphosis"), (58, 66, "climax")):
    pa.text((x0 + x1) / 2, -0.12, nm, fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="center", va="top")
pa.set_xlim(45, 66)
pa.set_ylim(0, 1.2)
pa.set_yticks([])
C.style_axes(pa, "Nieuwkoop–Faber stage", "plasma thyroid hormone")
pa.xaxis.labelpad = 24
