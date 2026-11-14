"""Parent-offspring conflict over investment per offspring (after Trivers 1974; Lazarus and Inglis 1986).

An offspring receiving investment x gains B(x) = 1 - exp(-x) (in units of its own survival); the investment is
withdrawn from its siblings, whose survival falls by C(x) = c x with c = 0.25. The parent, related by 1/2 to all
its offspring, maximizes (B - C)/2, optimal where B'(x) = c. An offspring values itself by 1 and its siblings
by r and maximizes B - r C, optimal where B'(x) = r c. A: the two fitness functions (rescaled to their maxima)
for full siblings (r = 1/2); between the two optima (shaded) the offspring is selected to demand more than the
parent is selected to give. B: the optimal investment from the parent's and the offspring's points of view as a
function of the relatedness r between siblings; the conflict is larger for half siblings (r = 1/4) and vanishes
only when r = 1 (clones).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
c = 0.25
x = np.linspace(0, 6, 600)
B = 1 - np.exp(-x)
xp = np.log(1 / c)

fig, ax = bio.canvas(30.0, 10.5)
pa = Ch.axes_at(ax, (2.6, 1.8, 10.8, 7.6))
fp = (B - c * x) / 2
r = 0.5
fo = B - r * c * x
xo = np.log(1 / (r * c))
pa.axvspan(xp, xo, color=P.mix(P.fill("highlight"), P.surface(), 0.7), lw=0)
pa.plot(x, fp / fp.max(), color=Ch.line("protein"), lw=1.9, label="parent: (B − C)/2")
pa.plot(x, fo / fo.max(), color=Ch.line("rna"), lw=1.9, label="offspring: B − rC, r = 1/2")
pa.axvline(xp, color=Ch.line("protein"), lw=0.8, ls=(0, (3, 2)))
pa.axvline(xo, color=Ch.line("rna"), lw=0.8, ls=(0, (3, 2)))
pa.text((xp + xo) / 2, 0.08, "zone of\nconflict", ha="center", fontsize=FS["tiny"], color=P.ink())
pa.set_xlim(0, 6)
pa.set_ylim(0, 1.08)
Ch.style_axes(pa, "investment in the current offspring $x$", "fitness (relative to maximum)")
Ch.title(pa, "Parent's and offspring's optima")
leg = pa.legend(fontsize=FS["tiny"], frameon=False, loc="lower right")
for t in leg.get_texts():
    t.set_color(P.ink())
bio.panel(ax, "A", (0.3, 10.2))

pb = Ch.axes_at(ax, (18.0, 1.8, 11.0, 7.6))
rs = np.linspace(0.1, 1, 200)
pb.fill_between(rs, xp, np.log(1 / (rs * c)), color=P.mix(P.fill("highlight"), P.surface(), 0.7), lw=0)
pb.plot(rs, np.full_like(rs, xp), color=Ch.line("protein"), lw=1.9)
pb.plot(rs, np.log(1 / (rs * c)), color=Ch.line("rna"), lw=1.9)
for rr, name in ((0.25, "half sibs"), (0.5, "full sibs")):
    pb.plot([rr], [np.log(1 / (rr * c))], "o", color=Ch.line("rna"), ms=5)
    pb.text(rr + 0.02, np.log(1 / (rr * c)) + 0.08, name, fontsize=FS["tiny"], color=Ch.line("rna"))
pb.text(0.98, xp - 0.1, "parent's optimum", fontsize=FS["tiny"], color=Ch.line("protein"), ha="right", va="top")
pb.text(0.35, 3.9, "offspring's optimum", fontsize=FS["tiny"], color=Ch.line("rna"))
pb.set_xlim(0.1, 1)
pb.set_ylim(0, 4.5)
Ch.style_axes(pb, "relatedness between siblings $r$", "optimal investment $x$")
Ch.title(pb, "Conflict shrinks as siblings are more related")
bio.panel(ax, "B", (15.8, 10.2))
