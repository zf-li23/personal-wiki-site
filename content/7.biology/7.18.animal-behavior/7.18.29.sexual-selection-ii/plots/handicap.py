"""A condition-dependent handicap: why costly ornaments can be honest (after Grafen 1990).

A male of quality q chooses ornament size s. His mating benefit b(s) = 1 - exp(-s) is the same function for
all males; the survival cost c(s, q) = s^2 / (2 q) is lower for males of high quality. His net payoff
b(s) - c(s, q) is maximal where b'(s) = s/q, that is at s*(q) solving exp(-s) = s/q.
A: benefit and cost curves for a low-quality (q = 0.6) and a high-quality (q = 2.0) male; the optimum is where
the slopes of benefit and cost are equal (dots), and a high-quality male's optimal ornament is larger.
B: the equilibrium signal s*(q) increases with quality, so receivers can read quality from the ornament.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT


def s_opt(q):
    lo, hi = 0.0, 10.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if np.exp(-mid) > mid / q:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


fig, ax = bio.canvas(30.0, 10.5)
pa = Ch.axes_at(ax, (2.6, 1.8, 11.0, 7.6))
s = np.linspace(0, 2.5, 300)
b = 1 - np.exp(-s)
pa.plot(s, b, color=P.ink(), lw=1.9)
pa.text(2.45, 0.93, "mating benefit $b(s)$", fontsize=FS["tiny"], color=P.ink(), ha="right", va="bottom")
for q, tok, name in ((0.6, "rna", "low quality"), (2.0, "dna", "high quality")):
    c = s ** 2 / (2 * q)
    pa.plot(s, c, color=Ch.line(tok), lw=1.6, ls=(0, (4, 2)))
    pa.plot(s, b - c, color=Ch.line(tok), lw=1.9)
    so = s_opt(q)
    pa.plot([so], [1 - np.exp(-so) - so ** 2 / (2 * q)], "o", color=Ch.line(tok), ms=6)
    pa.axvline(so, color=Ch.line(tok), lw=0.7, ls=(0, (1, 2)))
    pa.text(so + 0.03, -0.15 if q < 1 else 0.1, f"$s^*$ ({name})", fontsize=FS["tiny"], color=Ch.line(tok))
pa.text(1.0, 1.25, "cost, low quality", fontsize=FS["tiny"], color=Ch.line("rna"))
pa.text(1.9, 0.55, "cost, high quality", fontsize=FS["tiny"], color=Ch.line("dna"), ha="left")
pa.text(0.05, 0.47, "net payoff", fontsize=FS["tiny"], color=P.ink())
pa.set_xlim(0, 2.5)
pa.set_ylim(-0.2, 1.4)
Ch.style_axes(pa, "ornament size $s$", "fitness component")
Ch.title(pa, "The same benefit, a cost that depends on quality")
bio.panel(ax, "A", (0.3, 10.2))

pb = Ch.axes_at(ax, (18.2, 1.8, 10.8, 7.6))
qq = np.linspace(0.2, 4, 200)
pb.plot(qq, [s_opt(x) for x in qq], color=Ch.line("protein"), lw=1.9)
for q, tok in ((0.6, "rna"), (2.0, "dna")):
    pb.plot([q], [s_opt(q)], "o", color=Ch.line(tok), ms=6)
pb.set_xlim(0, 4)
pb.set_ylim(0, 1.4)
Ch.style_axes(pb, "male quality $q$", "optimal ornament $s^*(q)$")
Ch.title(pb, "Honest signaling: ornament size reveals quality")
bio.panel(ax, "B", (16.1, 10.2))
