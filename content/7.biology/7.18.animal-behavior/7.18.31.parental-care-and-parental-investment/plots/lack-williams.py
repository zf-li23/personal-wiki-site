"""Lack's clutch size and Williams's trade-off between current and future reproduction.

Each chick in a brood of n survives to independence with probability s(n) = 1 - n/10 (parents cannot feed
large broods adequately). A: survival per chick falls with brood size, while the number of surviving young
n s(n) is maximal at n = 5, the Lack clutch size. B: if raising a brood of n also reduces the parent's own
expected future reproductive success, V(n) = V0 (1 - c n) with V0 = 4 young and c = 0.06, the brood size that
maximizes lifetime success n s(n) + V(n) is smaller, here 3.8 (the integer optimum is 4). The more the parent
can expect from the future, the smaller its optimal current brood.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
n = np.linspace(0, 10, 400)
ni = np.arange(0, 11)


def s(x):
    return np.clip(1 - x / 10, 0, 1)


fig, ax = bio.canvas(30.0, 10.5)
pa = Ch.axes_at(ax, (2.6, 1.8, 10.6, 7.6))
pa.plot(n, n * s(n), color=Ch.line("dna"), lw=1.9)
pa.plot(ni, ni * s(ni), "o", color=Ch.line("dna"), ms=4)
pr = pa.twinx()
pr.plot(n, s(n), color=Ch.line("rna"), lw=1.5, ls=(0, (4, 2)))
pr.set_ylim(0, 1.05)
Ch.style_axes(pr, None, "survival per chick $s(n)$", box=True)
pr.spines["left"].set_visible(False)
pa.axvline(5, color=P.muted(), lw=0.8, ls=(0, (1, 2)))
pa.text(5.1, 0.2, "Lack clutch size", fontsize=FS["tiny"], color=P.muted())
pa.text(1.0, 2.9, "surviving young per brood", fontsize=FS["tiny"], color=Ch.line("dna"))
pa.text(8.4, 0.95, "survival per chick", fontsize=FS["tiny"], color=Ch.line("rna"), ha="right")
pa.set_xlim(0, 10)
pa.set_ylim(0, 2.8 * 1.15)
Ch.style_axes(pa, "brood size $n$", "surviving young $n\\,s(n)$")
Ch.title(pa, "Productivity per brood")
bio.panel(ax, "A", (0.3, 10.2))

pb = Ch.axes_at(ax, (18.2, 1.8, 10.8, 7.6))
V0, c = 4.0, 0.06
cur = n * s(n)
fut = V0 * (1 - c * n)
pb.plot(n, cur, color=Ch.line("dna"), lw=1.4, ls=(0, (4, 2)), label="current brood")
pb.plot(n, fut, color=Ch.line("protein"), lw=1.4, ls=(0, (1, 1.5)), label="future reproduction")
pb.plot(n, cur + fut, color=P.ink(), lw=1.9, label="lifetime success")
nopt = 5 * (1 - 10 * V0 * c / 10)
pb.axvline(nopt, color=P.ink(), lw=0.8, ls=(0, (3, 2)))
pb.axvline(5, color=P.muted(), lw=0.8, ls=(0, (1, 2)))
pb.text(nopt - 0.1, 0.25, "optimum with\ncost of reproduction", fontsize=FS["tiny"], color=P.ink(), ha="right")
pb.text(5.1, 0.25, "Lack", fontsize=FS["tiny"], color=P.muted())
pb.set_xlim(0, 10)
pb.set_ylim(0, 7.5)
Ch.style_axes(pb, "brood size $n$", "young (current + expected future)")
Ch.title(pb, "Williams: current against future reproduction")
leg = pb.legend(fontsize=FS["tiny"], frameon=False, loc="upper right")
for t in leg.get_texts():
    t.set_color(P.ink())
bio.panel(ax, "B", (16.0, 10.2))
