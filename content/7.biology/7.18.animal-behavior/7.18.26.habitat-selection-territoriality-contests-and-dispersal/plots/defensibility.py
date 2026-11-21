"""Economic defensibility of a territory (Brown 1964; graphical model after Schoener 1983) and the energy budget of
golden-winged sunbirds (Gill and Wolf 1975).

A: benefit B(x) = B_max (1 - exp(-x / x0)) of a territory of size x in a rich and a poor habitat (the benefit
saturates when the owner cannot use more food), and the cost of defense C(x) = c x^1.5, which accelerates as the
boundary lengthens and intrusions increase. Defense is economical where B > C; net benefit B - C is greatest
where the slopes are equal (dots). Illustrative parameters.
B: sunbirds need T(n) = 8/n hours of foraging per day at n microliters of nectar per flower (Gill and Wolf's
measurements: 8 h at 1, 4 h at 2, 2.7 h at 3). Excluding other nectar feeders raises the standing crop by 1
microliter; the bird saves T(n) - T(n + 1) hours of foraging (1000 cal/h) that it spends perched (400 cal/h).
Defense costs 0.28 h/day at 3000 instead of 400 cal/h, 728 cal. Defense pays only when nectar is scarce.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(32.0, 10.0)

pa = Ch.axes_at(ax, (2.4, 1.7, 11.0, 7.4))
x = np.linspace(0, 10, 400)
cost = 0.09 * x ** 1.5
pa.plot(x, cost, color=P.ink(), lw=1.6)
pa.text(9.95, cost[-1] - 0.35, "cost of defense", fontsize=FS["tiny"], color=P.ink(), ha="right")
for bmax, x0, tok, name in ((3.0, 1.2, "positive", "benefit, rich habitat"), (2.4, 3.0, "plant", "benefit, poor habitat")):
    b = bmax * (1 - np.exp(-x / x0))
    col = Ch.line(tok)
    pa.plot(x, b, color=col, lw=1.6)
    net = b - cost
    i = int(np.argmax(net))
    pa.plot([x[i]], [b[i]], "o", color=col, ms=5)
    pa.plot([x[i], x[i]], [cost[i], b[i]], color=col, lw=0.9, ls=(0, (2, 2)))
    ok = net > 0
    pa.fill_between(x, cost, b, where=ok, color=col, alpha=0.15, lw=0)
    pa.text(*((0.4, bmax + 0.08) if tok == "positive" else (6.0, 2.25)), name, fontsize=FS["tiny"], color=col)
pa.set_xlim(0, 10)
pa.set_ylim(0, 3.4)
pa.set_xticks([])
pa.set_yticks([])
Ch.style_axes(pa, "territory size", "energy per day")
bio.panel(ax, "A", (0.3, 9.8))

pb = Ch.axes_at(ax, (18.0, 1.7, 12.6, 7.4))
n = np.linspace(0.8, 4.0, 300)
T = lambda v: 8.0 / v  # noqa: E731
saving = (1000 - 400) * (T(n) - T(n + 1))
pb.plot(n, saving, color=Ch.line("rna"), lw=1.7)
pb.axhline(728, color=P.ink(), lw=1.0, ls=(0, (4, 2)))
pb.text(3.95, 760, "cost of defense, 728 cal/day", fontsize=FS["tiny"], color=P.ink(), ha="right", va="bottom")
pb.text(1.35, 2300, "energy saved by\nforaging less", fontsize=FS["tiny"], color=Ch.line("rna"), va="top")
for v in (1, 2, 3):
    s = 600 * (T(v) - T(v + 1))
    pb.plot([v], [s], "o", color=Ch.line("rna"), ms=4)
    pb.text(v + 0.06, s + 70, f"{s:.0f}", fontsize=FS["tiny"], color=Ch.line("rna"))
cross = 0.5 * (-1 + np.sqrt(1 + 4 * 8 * 600 / 728))
pb.axvspan(0.8, cross, color=Ch.line("positive"), alpha=0.12, lw=0)
pb.text(1.5, 120, "defense pays", fontsize=FS["tiny"], color=Ch.line("positive"))
pb.set_xlim(0.8, 4.0)
pb.set_ylim(0, 2600)
Ch.style_axes(pb, "nectar per flower without defense / $\\mu$L", "energy / (cal per day)")
bio.panel(ax, "B", (15.9, 9.8))
