"""Plasticity and adaptation to a new environment (after Futuyma and Kirkpatrick 2017, Fig. 15.28): reaction
norms of genotypes A, B, C share the optimum phenotype in environment 1; in environment 2 the plastic
response of A reaches the new optimum, B moves a little toward it, C moves away. Fitness functions shaded."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(14, 9)
pax = charts.axes_at(ax, (2.2, 1.6, 9.6, 6.8))
z1, z2 = 3.0, 7.0
zz = np.linspace(0, 10, 300)
for xe, opt in ((0.0, z1), (1.0, z2)):
    w = np.exp(-(zz - opt) ** 2 / 2.0)
    pax.fill_betweenx(zz, xe - 0.22 * w, xe, color=P.light("positive"), lw=0, zorder=0)
for name, end, tok in (("A", 7.0, "dna"), ("B", 4.0, "rna"), ("C", 1.6, "negative")):
    pax.plot([0, 1], [z1, end], color=charts.line(tok), lw=2.0)
    pax.text(1.04, end, name, color=charts.line(tok), fontsize=FT["small"], va="center", weight="bold")
pax.plot([0], [z1], marker="*", ms=14, color=P.ink(), zorder=6)
pax.plot([1], [z2], marker="^", ms=9, color=P.ink(), zorder=6)
pax.set_xlim(-0.3, 1.2)
pax.set_ylim(0, 10)
pax.set_xticks([0, 1])
pax.set_xticklabels(["environment 1", "environment 2"])
pax.set_yticks([])
charts.style_axes(pax, None, "phenotype")
pax.text(0.03, z1 - 0.7, "optimum in 1", fontsize=FT["tiny"], color=P.muted())
pax.text(0.97, z2 + 0.45, "optimum in 2", fontsize=FT["tiny"], color=P.muted(), ha="right")
