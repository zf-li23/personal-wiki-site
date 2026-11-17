"""Sex ratio theory: Fisher's principle and two departures from it.

A: Shaw-Mohler argument. In a large random-mating population in which mothers produce a proportion s of
sons, a rare mutant mother producing a proportion s' has relative fitness (counting grandchildren)
W(s', s) = [(1 - s') / (1 - s) + s' / s] / 2. For s = 0.3 (few males) the mutant gains by producing more
sons, for s = 0.7 by producing more daughters; only at s = 1/2 is W independent of s': 1:1 is the ESS.
B: when a son costs c times as much as a daughter, the ESS proportion of sons among offspring is
1 / (1 + c), so that equal amounts are invested in the two sexes (dashed: investment in sons stays 1/2).
C: local mate competition (Hamilton 1967): when n foundresses lay eggs in a patch and their sons mate
only with the daughters there, the ESS proportion of sons is (n - 1) / (2n) in a diploid species
(haplodiploid species with full sib-mating: slightly lower; not shown).
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(33.0, 12.0)

pa = C.axes_at(ax, (2.4, 1.8, 8.8, 8.6))
sp = np.linspace(0, 1, 200)
for s, tok in [(0.3, "dna"), (0.5, "positive"), (0.7, "rna")]:
    pa.plot(sp, 0.5 * ((1 - sp) / (1 - s) + sp / s), color=Q.line_color(tok), lw=1.8, label=f"population s = {s}")
pa.axhline(1, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pa.set_xlim(0, 1)
pa.set_ylim(0.5, 1.75)
C.style_axes(pa, "mutant's proportion of sons s'", "relative fitness of mutant")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper center")
bio.panel(ax, "A", (0.4, 11.6))
bio.label(ax, (2.4, 11.2), "Fisher's principle (Shaw-Mohler)", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (13.6, 1.8, 8.4, 8.6))
c = np.linspace(0.25, 4, 300)
pb.plot(c, 1 / (1 + c), color=Q.line_color("dna"), lw=1.8, label="proportion of sons")
pb.plot(c, c / (1 + c) * 0 + 0.5, color=P.muted(), lw=1.0, ls=(0, (4, 2)), label="share of investment in sons")
pb.set_xscale("log")
pb.set_xticks([0.25, 0.5, 1, 2, 4])
pb.set_xticklabels(["1/4", "1/2", "1", "2", "4"])
pb.set_ylim(0, 1)
C.style_axes(pb, "cost of a son / cost of a daughter, c", "ESS")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (11.8, 11.6))
bio.label(ax, (13.6, 11.2), "Equal investment, not equal numbers", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (24.6, 1.8, 8.0, 8.6))
n = np.arange(1, 21)
pc.plot(n, (n - 1) / (2 * n), "o-", color=Q.line_color("rna"), lw=1.4, ms=3.5)
pc.axhline(0.5, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pc.text(20, 0.52, "Fisher: 1/2", fontsize=FS["tiny"], color=P.muted(), ha="right")
pc.set_xlim(0, 21)
pc.set_ylim(0, 0.6)
C.style_axes(pc, "number of foundresses per patch, n", "ESS proportion of sons")
bio.panel(ax, "C", (23.0, 11.6))
bio.label(ax, (24.6, 11.2), "Local mate competition", size="small", bold=True, ha="left")
