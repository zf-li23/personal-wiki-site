"""Two rules for sampling mates (after Janetos 1980; Real 1990).

Male quality X is normally distributed with mean 0 and standard deviation 1; inspecting each male costs a
female c (time, energy, predation risk) in the same units. Best-of-n: inspect n males and mate with the best,
net payoff E[max of n] - c n. Sequential threshold: inspect males one at a time and accept the first whose
quality exceeds T; the number inspected is geometric with mean 1 / (1 - Phi(T)), so the net payoff is
E[X | X > T] - c / (1 - Phi(T)) = [phi(T) - c] / (1 - Phi(T)).
A: best-of-n for c = 0.03 and c = 0.15. B: the sequential threshold rule; dots mark the best n and best T.
For both costs, the best threshold rule does better than the best best-of-n rule, and costlier sampling makes
females less choosy (fewer males sampled, lower threshold).
"""

import math

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
xg = np.linspace(-8, 8, 16001)
dx = xg[1] - xg[0]
phi = np.exp(-xg ** 2 / 2) / math.sqrt(2 * math.pi)
Phi = np.cumsum(phi) * dx


def emax(n):
    return float(np.sum(xg * n * Phi ** (n - 1) * phi) * dx)


def thr(T, c):
    pT = math.exp(-T * T / 2) / math.sqrt(2 * math.pi)
    tail = 0.5 * math.erfc(T / math.sqrt(2))
    return (pT - c) / tail


fig, ax = bio.canvas(30.0, 10.5)
pa = Ch.axes_at(ax, (2.6, 1.8, 10.8, 7.6))
pb = Ch.axes_at(ax, (18.0, 1.8, 10.8, 7.6))
ns = np.arange(1, 21)
Ts = np.linspace(-1.5, 2.6, 300)
for c, tok in ((0.03, "dna"), (0.15, "rna")):
    v = np.array([emax(n) - c * n for n in ns])
    pa.plot(ns, v, "o-", color=Ch.line(tok), lw=1.4, ms=3.2, label=f"c = {c}")
    k = int(v.argmax())
    pa.plot([ns[k]], [v[k]], "o", color=Ch.line(tok), ms=8, mfc="none", mew=1.5)
    w = np.array([thr(T, c) for T in Ts])
    pb.plot(Ts, w, color=Ch.line(tok), lw=1.8, label=f"c = {c}")
    j = int(w.argmax())
    pb.plot([Ts[j]], [w[j]], "o", color=Ch.line(tok), ms=7)
    pb.axhline(v[k], color=Ch.line(tok), lw=0.7, ls=(0, (2, 2)))
    pb.text(-1.45, v[k] + 0.03, f"best of n, c = {c}", fontsize=FS["tiny"], color=Ch.line(tok), va="bottom")
pa.set_xlim(0, 21)
pa.set_ylim(-0.5, 1.6)
pb.set_xlim(-1.5, 2.6)
pb.set_ylim(-0.5, 1.6)
Ch.style_axes(pa, "number of males inspected $n$", "net expected quality of mate")
Ch.title(pa, "Best-of-n: inspect n males, take the best")
Ch.style_axes(pb, "acceptance threshold $T$", "net expected quality of mate")
Ch.title(pb, "Sequential search: accept the first male above T")
for p in (pa, pb):
    leg = p.legend(fontsize=FS["tiny"], frameon=False, loc="lower right")
    for txt in leg.get_texts():
        txt.set_color(P.ink())
bio.panel(ax, "A", (0.3, 10.2))
bio.panel(ax, "B", (15.8, 10.2))
