"""Anatomy of the limb bud and the sources of its cells (schematic).

A: early chick wing bud, dorsal view, with AER, progress zone and ZPA, and the three axes.
B: transverse section of the embryo at forelimb level: neural tube, notochord, somite with dermomyotome, the
somatic lateral plate bulging into the limb bud; muscle precursors migrating from the dermomyotome into the bud,
neural crest cells and motor axons. C: human arm skeleton with its three segments.
"""

import numpy as np
import wikibio as bio
from wikibio import limbdev as LD
from wikibio import zoomorph as zm
from matplotlib.patches import Circle, Ellipse

P = bio.P
fig, ax = bio.canvas(30.0, 12.0)

# A ---------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 11.8))
b = LD.limb_bud(ax, (2.2, 6.6), 4.6, 3.6)
bio.callout(ax, b["aer"], (7.9, 9.6), "AER")
bio.callout(ax, b["pz"], (7.9, 7.9), "Progress\nzone")
bio.callout(ax, b["zpa"], (7.9, 4.4), "ZPA")
bio.callout(ax, b["flank"], (0.9, 10.6), "Flank")
bio.callout(ax, b["at"](0.35, 0.3), (4.0, 10.9), "Lateral plate mesenchyme")
LD.axes_glyph(ax, (1.4, 2.0), 1.1)

# B ---------------------------------------------------------------------------------------------
bio.panel(ax, "B", (10.6, 11.8))
cx, cy = 14.6, 6.5
E = lambda t: P.mix(P.fill(t), P.surface(), 0.55 if P.is_dark() else 0.45)
# ectoderm outline of the body (left half shown) with the limb bud to the right
body = bio.smooth_closed(np.array([(cx - 2.6, cy + 2.8), (cx, cy + 3.3), (cx + 2.4, cy + 2.6), (cx + 3.6, cy + 1.0),
                                   (cx + 6.4, cy + 0.6), (cx + 7.3, cy - 0.4), (cx + 6.4, cy - 1.4), (cx + 3.6, cy - 1.6),
                                   (cx + 2.2, cy - 3.0), (cx, cy - 3.5), (cx - 2.4, cy - 3.0), (cx - 3.0, cy)]), 260)
bio.shape(ax, body, "ectoderm", lw=1.0, zorder=2, alpha=0.999)
ax.patches[-1].set_facecolor(E("mesoderm"))
# neural tube, notochord
ax.add_patch(Circle((cx, cy + 2.1), 0.85, facecolor=P.fill("ectoderm"), edgecolor=P.edge("ectoderm"), lw=1, zorder=5))
ax.add_patch(Circle((cx, cy + 2.1), 0.22, facecolor=P.surface(), edgecolor=P.edge("ectoderm"), lw=0.6, zorder=6))
ax.add_patch(Circle((cx, cy + 0.75), 0.33, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8, zorder=5))
# somite with dermomyotome
ax.add_patch(Ellipse((cx + 1.55, cy + 1.6), 1.6, 2.0, facecolor=P.fill("mesoderm"), edgecolor=P.edge("mesoderm"), lw=0.8, zorder=5))
dm = Ellipse((cx + 2.0, cy + 1.75), 0.45, 1.7, facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=0.8, zorder=6)
ax.add_patch(dm)
# coelom between somatic and splanchnic lateral plate
ax.add_patch(Ellipse((cx + 2.1, cy - 1.4), 2.4, 0.55, angle=-12, facecolor=P.fill("vacuole"), edgecolor=P.edge("vacuole"), lw=0.6, zorder=5))
# endoderm / gut
ax.add_patch(Ellipse((cx, cy - 1.7), 1.6, 0.8, facecolor=P.fill("endoderm"), edgecolor=P.edge("endoderm"), lw=0.8, zorder=5))
# muscle precursors migrating
rng = np.random.default_rng(3)
for k in range(9):
    t = k / 8
    p = (cx + 2.4 + 3.4 * t + rng.normal(0, 0.08), cy + 0.95 - 0.9 * t + rng.normal(0, 0.12))
    ax.add_patch(Ellipse(p, 0.34, 0.2, angle=-15, facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=0.6, zorder=7))
bio.arrow(ax, (cx + 2.3, cy + 1.1), (cx + 5.7, cy + 0.0), kind="process", color=P.edge("muscle"), lw=1.0, bend=-0.1, zorder=8)
# neural crest cells and motor axon
for k in range(5):
    ax.add_patch(Circle((cx + 0.9 + 0.32 * k, cy + 3.05 - 0.05 * k), 0.11, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.5, zorder=7))
ax.plot([cx + 0.6, cx + 3.0, cx + 5.6], [cy + 1.7, cy - 0.35, cy - 0.7], color=P.edge("neuron"), lw=1.2, zorder=6)
bio.callout(ax, (cx, cy + 2.5), (cx - 3.0, cy + 3.9), "Neural tube")
bio.callout(ax, (cx, cy + 0.75), (cx - 3.6, cy + 1.0), "Notochord")
bio.callout(ax, (cx + 2.05, cy + 2.4), (cx + 2.8, cy + 4.6), "Dermomyotome (Pax3)")
bio.callout(ax, (cx + 4.6, cy + 0.4), (cx + 6.2, cy + 3.4), "Myoblasts (c-Met)")
bio.callout(ax, (cx + 5.0, cy - 0.66), (cx + 5.6, cy - 3.6), "Motor axon")
bio.callout(ax, (cx + 1.6, cy + 3.0), (cx + 0.2, cy + 4.9), "Neural crest")
bio.callout(ax, (cx + 6.4, cy - 0.5), (cx + 8.6, cy - 2.4), "Lateral plate:\nbone, tendon,\nconnective tissue")
bio.callout(ax, (cx + 2.4, cy - 1.45), (cx - 1.0, cy - 4.4), "Coelom")
bio.callout(ax, (cx, cy - 1.7), (cx - 3.4, cy - 2.6), "Gut")
bio.label(ax, (cx + 6.4, cy + 1.2), "Limb bud", size="small", bold=True)

# C ---------------------------------------------------------------------------------------------
bio.panel(ax, "C", (24.0, 11.8))
h = zm.forelimb(ax, (26.4, 6.2), 10.0, "human", width=3.4)
xs = 28.6
for name, y0, y1 in (("Stylopod", h["shoulder"][1], h["elbow"][1]), ("Zeugopod", h["elbow"][1], h["wrist"][1]),
                     ("Autopod", h["wrist"][1], 1.2)):
    ax.plot([xs, xs + 0.15, xs + 0.15, xs], [y0 - 0.05, y0 - 0.05, y1 + 0.05, y1 + 0.05], color=P.muted(), lw=0.9)
    bio.label(ax, (xs + 0.3, (y0 + y1) / 2), name, size="small", ha="left")
