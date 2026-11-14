"""Vigilance and group size.

A: many eyes and dilution. If each of N group members independently has its head up a fraction p of the time,
the probability that at least one is scanning is 1 - (1 - p)^N (Pulliam 1973); if an undetected predator takes
one victim, an individual's share of the risk is 1/N (dilution).
B: an ESS model of vigilance (illustrative): an individual scanning a fraction v_i of the time feeds at rate
(1 - v_i) and survives with probability exp(-k (1 - v_i)(1 - v)^(N - 1) / N), where k is the predation hazard and
the others scan v; the ESS is v* = 1 - (N/k)^(1/N) for N < k. Individual vigilance falls steeply with N; the
probability that the group detects the predator, 1 - N/k, falls too. k = 10.
C: optimal and stable group sizes (Sibly 1983): with individual fitness W(n) = n exp(-n/7) (illustrative), fitness
peaks at n = 7, but solitary animals gain by joining groups until W(n) falls to W(1), at n = 22.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(33.0, 10.0)

pa = Ch.axes_at(ax, (2.4, 1.7, 7.6, 7.2))
N = np.arange(1, 21)
for p_, tok in ((0.1, "dna"), (0.3, "rna")):
    pa.plot(N, 1 - (1 - p_) ** N, "o-", ms=3, lw=1.4, color=Ch.line(tok))
    pa.text(20.3, 1 - (1 - p_) ** 20 - 0.03, f"p = {p_:g}", fontsize=FS["tiny"], color=Ch.line(tok), va="top",
            ha="right")
pa.plot(N, 1 / N, color=P.muted(), lw=1.2, ls=(0, (3, 2)))
pa.text(4.5, 0.27, "individual share of risk, 1/N", fontsize=FS["tiny"], color=P.muted())
pa.set_xlim(0, 21)
pa.set_ylim(0, 1.05)
Ch.style_axes(pa, "group size N", "probability")
Ch.title(pa, "at least one member scanning")
bio.panel(ax, "A", (0.3, 9.8))

pb = Ch.axes_at(ax, (13.4, 1.7, 7.6, 7.2))
k = 10.0
n = np.arange(1, 11)
v = np.clip(1 - (n / k) ** (1 / n), 0, 1)
pb.plot(n, v, "o-", ms=3.5, lw=1.5, color=Ch.line("rna"))
pb.plot(n, 1 - n / k, "o-", ms=3.5, lw=1.5, color=Ch.line("dna"))
pb.text(3.3, 0.36, "ESS vigilance of an individual", fontsize=FS["tiny"], color=Ch.line("rna"))
pb.text(4.2, 1 - 4 / k + 0.04, "probability the group detects an attack", fontsize=FS["tiny"], color=Ch.line("dna"))
pb.set_xlim(0.5, 10.5)
pb.set_ylim(0, 1.0)
Ch.style_axes(pb, "group size N", "fraction of time / probability")
bio.panel(ax, "B", (11.3, 9.8))

pc = Ch.axes_at(ax, (24.4, 1.7, 7.8, 7.2))
g = np.arange(1, 31)
W = g * np.exp(-g / 7)
stable = int(g[W >= W[0]].max())
pc.plot(g, W, "o-", ms=3, lw=1.4, color=Ch.line("protein"))
pc.axhline(W[0], color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pc.text(29.5, W[0] + 0.05, "fitness alone", fontsize=FS["tiny"], color=P.muted(), ha="right", va="bottom")
for x, name in ((7, "optimal"), (stable, "stable")):
    pc.annotate(name, (x, W[x - 1]), (x + 1.5, W[x - 1] + 0.45), fontsize=FS["tiny"], color=P.ink(),
                arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
pc.set_xlim(0, 31)
pc.set_ylim(0, 3.2)
Ch.style_axes(pc, "group size n", "fitness of a member W(n)")
bio.panel(ax, "C", (22.3, 9.8))
