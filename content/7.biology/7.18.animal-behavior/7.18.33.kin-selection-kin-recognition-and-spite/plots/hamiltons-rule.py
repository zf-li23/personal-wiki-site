"""Hamilton's rule in practice.

A: the (r, B/C) plane. Helping is favored above the curve B/C = 1/r (rB > C). Points are field estimates
discussed in the text: wild turkey coalitions (r = 0.42, B = 6.1, C = 0.9; Krakauer 2005) and primary helpers of
pied kingfishers (r = 0.32, B = 1.8 extra siblings, C = 0.43 own offspring; Reyer 1984). The dashed line marks the
minimum relatedness for the turkey values, r = C/B = 0.15.
B: the offspring-equivalent form of the rule, B/C > r(own offspring)/r(recipient's offspring): the number of extra
offspring the recipient must raise for each own offspring forgone, for several options of an outbred diploid
(and, for comparison, a haplodiploid female rearing full sisters instead of daughters).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.5)

pa = Ch.axes_at(ax, (2.6, 1.8, 10.5, 7.6))
r = np.linspace(0.06, 1.0, 300)
pa.fill_between(r, 1 / r, 12, color=P.mix(P.fill("positive"), P.surface(), 0.55), lw=0)
pa.plot(r, 1 / r, color=P.ink(), lw=1.5)
pa.text(0.55, 8.6, "helping favored\nrB > C", fontsize=FS["small"], color=P.ink(), ha="center")
pa.text(0.62, 0.55, "helping disfavored", fontsize=FS["small"], color=P.muted(), ha="center")
pa.text(0.095, 10.5, "B/C = 1/r", fontsize=FS["tiny"], color=P.ink())
pts = [(0.42, 6.1 / 0.9, "wild turkey coalitions", "dna"), (0.32, 1.8 / 0.43, "pied kingfisher primary helpers", "rna")]
for x, y, name, tok in pts:
    pa.plot([x], [y], "o", ms=6, color=Ch.line(tok))
    pa.text(x + 0.03, y + 0.25, name, fontsize=FS["tiny"], color=Ch.line(tok))
pa.plot([0.15, 0.15], [0, 6.1 / 0.9], color=Ch.line("dna"), lw=0.9, ls=(0, (3, 2)))
pa.plot([0.15, 0.42], [6.1 / 0.9, 6.1 / 0.9], color=Ch.line("dna"), lw=0.9, ls=(0, (3, 2)))
pa.text(0.155, 0.25, "r = 0.15", fontsize=FS["tiny"], color=Ch.line("dna"))
pa.set_xlim(0, 1.0)
pa.set_ylim(0, 12)
Ch.style_axes(pa, "relatedness r of actor to recipient", "benefit / cost, B/C")
bio.panel(ax, "A", (0.3, 10.1))

pb = Ch.axes_at(ax, (18.2, 1.8, 11.0, 7.6))
opts = [("help mother\n(full siblings)", 0.5 / 0.5, "dna"), ("help half siblings", 0.5 / 0.25, "rna"),
        ("help sister\n(nieces, nephews)", 0.5 / 0.25, "protein"), ("help cousin's\nbrood", 0.5 / 0.0625, "neutral"),
        ("haplodiploid:\nfull sisters only", 0.5 / 0.75, "highlight")]
y = np.arange(len(opts))[::-1]
for yy, (name, v, tok) in zip(y, opts):
    pb.barh(yy, v, height=0.6, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8)
    pb.text(v + 0.15, yy, f"{v:.2g}", va="center", fontsize=FS["tiny"], color=P.ink())
pb.set_yticks(y)
pb.set_yticklabels([o[0] for o in opts], fontsize=FS["tiny"])
pb.axvline(1, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.set_xlim(0, 9)
Ch.style_axes(pb, "extra offspring of recipient needed per own offspring forgone")
bio.panel(ax, "B", (12.2, 10.1))
