"""The switch point of a conditional strategy (status-dependent selection, after Gross 1996).

Status s (body size or condition, scaled to 0..1) is uniformly distributed among males. A male of status s that
fights earns W_F(s) = 0.2 + 2 s; one that sneaks earns W_S(s). A: no frequency dependence, W_S(s) = 0.6 + 0.4 s.
The best rule is to sneak below the status s* where the two lines cross (s* = 0.25); the mean payoffs of the two
tactics differ greatly (dots), yet every male follows the rule that is best for him. B: frequency dependence,
W_S(s; x) = 1.2 (1 - x) + 0.4 s, where x is the proportion of males that sneak. Under the rule "sneak if s < s*"
x = s*, and the evolutionarily stable switch point solves W_F(s*) = W_S(s*; s*), giving s* = 1/2.8 = 0.357.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
s = np.linspace(0, 1, 200)
WF = 0.2 + 2 * s

fig, ax = bio.canvas(30.0, 10.5)

pa = Ch.axes_at(ax, (2.6, 1.8, 11.0, 7.6))
WS = 0.6 + 0.4 * s
ss = 0.25
pa.axvspan(0, ss, color=P.mix(P.fill("rna"), P.surface(), 0.7), lw=0)
pa.plot(s, WF, color=Ch.line("dna"), lw=1.9)
pa.plot(s, WS, color=Ch.line("rna"), lw=1.9)
pa.plot(s[s < ss], WS[s < ss], color=Ch.line("rna"), lw=4.0, alpha=0.5)
pa.plot(s[s >= ss], WF[s >= ss], color=Ch.line("dna"), lw=4.0, alpha=0.5)
pa.axvline(ss, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
mS = 0.6 + 0.4 * ss / 2
mF = 0.2 + 2 * (1 + ss) / 2
pa.plot([ss / 2], [mS], "o", color=Ch.line("rna"), ms=6)
pa.plot([(1 + ss) / 2], [mF], "o", color=Ch.line("dna"), ms=6)
pa.text(ss / 2, mS + 0.12, "mean of\nsneakers", fontsize=FS["tiny"], color=Ch.line("rna"), ha="center", va="bottom")
pa.text((1 + ss) / 2 + 0.03, mF - 0.05, "mean of fighters", fontsize=FS["tiny"], color=Ch.line("dna"), va="top")
pa.text(0.6, 1.62, "fight", fontsize=FS["small"], color=Ch.line("dna"), ha="right", va="bottom")
pa.text(0.97, 1.08, "sneak", fontsize=FS["small"], color=Ch.line("rna"), ha="right")
pa.text(ss + 0.01, 0.05, "switch point $s^*$", fontsize=FS["tiny"], color=P.muted())
pa.set_xlim(0, 1)
pa.set_ylim(0, 2.4)
Ch.style_axes(pa, "status $s$ (size or condition)", "expected mating success")
Ch.title(pa, "Fixed payoffs: switch where the lines cross")
bio.panel(ax, "A", (0.3, 10.2))

pb = Ch.axes_at(ax, (18.2, 1.8, 11.0, 7.6))
s_ess = 1 / 2.8
pb.plot(s, WF, color=Ch.line("dna"), lw=1.9)
for x, ls in ((0.15, (0, (4, 2))), (s_ess, "-"), (0.6, (0, (1, 1.5)))):
    pb.plot(s, 1.2 * (1 - x) + 0.4 * s, color=Ch.line("rna"), lw=1.6, ls=ls)
    pb.text(0.99, 1.2 * (1 - x) + 0.4 + 0.04, f"sneak, x = {x:.2f}", fontsize=FS["tiny"], color=Ch.line("rna"),
            ha="right", va="bottom")
pb.plot([s_ess], [0.2 + 2 * s_ess], "o", color=P.ink(), ms=6, zorder=5)
pb.annotate("ESS: $W_F(s^*) = W_S(s^*; x = s^*)$", (s_ess, 0.2 + 2 * s_ess), (0.42, 0.35),
            fontsize=FS["tiny"], color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
pb.text(0.7, 1.82, "fight", fontsize=FS["small"], color=Ch.line("dna"), ha="right", va="bottom")
pb.set_xlim(0, 1)
pb.set_ylim(0, 2.4)
Ch.style_axes(pb, "status $s$", "expected mating success")
Ch.title(pb, "Frequency dependence: sneaking pays less when common")
bio.panel(ax, "B", (16.0, 10.2))
