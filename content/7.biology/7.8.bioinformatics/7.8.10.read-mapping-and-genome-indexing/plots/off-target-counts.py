# How many sites resemble a guide by chance. For a 20-nt protospacer followed by an NGG PAM, the number
# of 20-mers within Hamming distance d of the guide is N(d) = sum_j C(20, j) 3^j; in a random genome of
# 3.1 Gb (both strands, a PAM at 1/16 of positions) the expected number of matching sites with at most d
# mismatches is 2G/16 * N(d)/4^20 (A). B: the expected number of candidate sites with at most 3
# mismatches as a function of the guide length, and the length of exact seed guaranteed by the
# pigeonhole principle for d = 3 (the guide split into d + 1 = 4 pieces).
import numpy as np
from math import comb
import wikibio as bio
from wikibio import charts as C

G = 3.1e9
sites = 2 * G / 16
d = np.arange(0, 7)
N = np.array([sum(comb(20, j) * 3 ** j for j in range(k + 1)) for k in d], dtype=float)
E = sites * N / 4.0 ** 20
fig, ax = bio.canvas(24.0, 9.0)
a = C.axes_at(ax, (2.0, 1.5, 9.0, 6.6))
a.bar(d, E, color=C.line("dna"), width=0.6)
for x_, y_ in zip(d, E):
    a.text(x_, y_ * 1.4, f"{y_:.3g}", ha="center", fontsize=bio.core.FONT["tiny"], color=bio.P.ink())
a.set_yscale("log")
a.set_ylim(1e-4, 1e6)
C.style_axes(a, "mismatches allowed, d", "expected chance sites (NGG PAM)")
C.title(a, "A  20-nt guide, random 3.1 Gb genome")
b = C.axes_at(ax, (14.5, 1.5, 8.5, 6.6))
Ls = np.arange(14, 25)
E3 = [sites * sum(comb(l, j) * 3 ** j for j in range(4)) / 4.0 ** l for l in Ls]
b.plot(Ls, E3, "o-", color=C.line("negative"), ms=4)
b.axhline(1.0, color=C.line("neutral"), lw=0.8, ls="--")
b.set_yscale("log")
C.style_axes(b, "guide length (nt)", "expected sites with d <= 3")
C.title(b, "B  Longer guides are more specific")
print(list(zip(d.tolist(), E.round(4).tolist())))
print(list(zip(Ls.tolist(), np.round(E3, 3).tolist())))
