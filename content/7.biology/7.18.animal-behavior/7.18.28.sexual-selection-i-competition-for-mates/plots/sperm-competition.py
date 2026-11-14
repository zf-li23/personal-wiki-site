"""Two models of male investment under sperm competition.

A: a sperm competition "raffle" (after Parker 1990). A male with a fixed reproductive budget pays c (the cost of
finding a female) plus s (ejaculate expenditure) per mating. With probability q a given mating is followed by a
mating of the female with a rival spending s*, and the eggs are shared in proportion to the numbers of sperm,
s / (s + s*). The evolutionarily stable expenditure is s* = q c / (4 - 3 q), which rises with the risk q; the
fraction of the reproductive budget spent on ejaculates is s*/(s* + c) = q/(4 - 2q).
B: when to guard a mate (after Dickinson 1995). A male who leaves a mated female finds a new female during the
guarding period with probability m; an unguarded female remates with probability r and the second male then
fertilizes a fraction P2 of her eggs. Guarding pays if P2 > m / [r (1 + m)]. The point marks the blue milkweed
beetle Chrysochus cobaltinus (m = 0.25, r = 0.5): guarding pays if P2 > 0.4.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT

fig, ax = bio.canvas(30.0, 10.5)

pa = Ch.axes_at(ax, (2.6, 1.8, 10.8, 7.6))
q = np.linspace(0, 1, 200)
pa.plot(q, q / (4 - 3 * q), color=Ch.line("dna"), lw=1.9)
pa.plot(q, q / (4 - 2 * q), color=Ch.line("rna"), lw=1.9, ls=(0, (4, 2)))
pa.text(0.62, 0.62, "ESS expenditure per mating $s^*/c$", fontsize=FS["tiny"], color=Ch.line("dna"), ha="right")
pa.text(0.98, 0.30, "share of budget on\nejaculates $s^*/(s^*+c)$", fontsize=FS["tiny"], color=Ch.line("rna"),
        ha="right", va="top")
pa.set_xlim(0, 1)
pa.set_ylim(0, 1.05)
Ch.style_axes(pa, "risk of sperm competition $q$", "relative ejaculate investment")
Ch.title(pa, "Sperm competition raffle")
bio.panel(ax, "A", (0.3, 10.2))

pb = Ch.axes_at(ax, (18.0, 1.8, 10.8, 7.6))
m = np.linspace(0, 1, 200)
for r, ls in ((0.25, (0, (1, 1.5))), (0.5, "-"), (1.0, (0, (4, 2)))):
    thr = m / (r * (1 + m))
    pb.plot(m, np.clip(thr, 0, 1.2), color=Ch.line("protein"), lw=1.7, ls=ls)
    k = np.searchsorted(thr, 0.95) if thr[-1] > 0.95 else len(m) - 1
    pb.text(m[k] + 0.01, min(thr[k], 0.95) - 0.02, f"r = {r:g}", fontsize=FS["tiny"], color=Ch.line("protein"),
            va="top")
pb.plot([0.25], [0.4], "o", color=P.ink(), ms=6, zorder=5)
pb.annotate("milkweed beetle:\nguard if $P_2$ > 0.4", (0.25, 0.4), (0.33, 0.12), fontsize=FS["tiny"],
            color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
pb.text(0.04, 0.9, "guard", fontsize=FS["small"], color=P.ink(), weight="bold")
pb.text(0.8, 0.05, "leave", fontsize=FS["small"], color=P.ink(), weight="bold")
pb.set_xlim(0, 1)
pb.set_ylim(0, 1)
Ch.style_axes(pb, "chance of finding a new female while guarding, $m$", "last-male fertilization $P_2$")
Ch.title(pb, "Guarding threshold: guard above the line")
bio.panel(ax, "B", (15.8, 10.2))
