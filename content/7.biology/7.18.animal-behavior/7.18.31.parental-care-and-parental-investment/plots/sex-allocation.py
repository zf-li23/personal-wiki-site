"""Conditional sex allocation: the Trivers-Willard argument and the Seychelles warbler.

A: the expected fitness of a son increases more steeply with the condition c of his mother (0 to 1) than that
of a daughter: W_son = 0.2 + 1.8 c, W_daughter = 0.7 + 0.4 c (in a polygynous species, sons in good condition
win harems). A mother maximizes her fitness by producing the sex with the higher expected fitness, daughters
below the crossing point c* = 0.36 and sons above it. In a real population the crossing point is set by the
population sex ratio (Fisher's principle), because the value of sons falls as they become common.
B: sex ratios of Seychelles warbler (Acrocephalus sechellensis) offspring (proportion male) produced by pairs
on low- and high-quality territories, and by pairs translocated from low- to high-quality territories, before
and after the move (approximate values from Komdeur and colleagues 1997, as summarized by Davies, Krebs and West
2012). On high-quality territories, daughters stay and help (local resource enhancement); on poor territories,
daughters that stay compete for scarce food (local resource competition).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.5)

pa = Ch.axes_at(ax, (2.6, 1.8, 10.8, 7.6))
c = np.linspace(0, 1, 200)
ws, wd = 0.2 + 1.8 * c, 0.7 + 0.4 * c
cs = 0.5 / 1.4
pa.axvspan(0, cs, color=P.mix(P.fill("rna"), P.surface(), 0.7), lw=0)
pa.axvspan(cs, 1, color=P.mix(P.fill("dna"), P.surface(), 0.7), lw=0)
pa.plot(c, ws, color=Ch.line("dna"), lw=1.9)
pa.plot(c, wd, color=Ch.line("rna"), lw=1.9)
pa.axvline(cs, color=P.ink(), lw=0.8, ls=(0, (3, 2)))
pa.text(0.03, 1.85, "produce\ndaughters", fontsize=FS["small"], color=P.ink(), va="top")
pa.text(0.97, 0.35, "produce\nsons", fontsize=FS["small"], color=P.ink(), ha="right", va="bottom")
pa.text(0.8, 1.9, "son", fontsize=FS["tiny"], color=Ch.line("dna"), ha="right", va="bottom")
pa.text(0.95, 1.12, "daughter", fontsize=FS["tiny"], color=Ch.line("rna"), ha="right", va="bottom")
pa.set_xlim(0, 1)
pa.set_ylim(0, 2.2)
Ch.style_axes(pa, "maternal condition $c$", "expected fitness of offspring")
Ch.title(pa, "Trivers-Willard: the sex that gains more from condition")
bio.panel(ax, "A", (0.3, 10.2))

pb = Ch.axes_at(ax, (18.0, 1.8, 11.0, 7.6))
labels = ["low-quality\nterritory", "high-quality\nterritory", "translocated:\nbefore", "translocated:\nafter"]
vals = [0.8, 0.1, 0.9, 0.15]
toks = ["dna", "rna", "dna", "rna"]
for i, (v, t) in enumerate(zip(vals, toks)):
    pb.bar(i, v, 0.7, color=P.fill(t), edgecolor=P.edge(t), lw=0.8)
pb.axhline(0.5, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.set_xticks(range(4))
pb.set_xticklabels(labels, fontsize=FS["tiny"])
pb.set_ylim(0, 1)
Ch.style_axes(pb, None, "proportion of sons")
Ch.title(pb, "Seychelles warblers adjust sex ratio to territory")
bio.panel(ax, "B", (15.8, 10.2))
