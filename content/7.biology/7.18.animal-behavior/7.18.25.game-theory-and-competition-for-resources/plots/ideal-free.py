"""The ideal free distribution (Fretwell and Lucas 1969) in a continuous-input system.

A: intake per individual Q_i / n_i in a rich (Q = 2) and a poor (Q = 1) patch; with six competitors the only
distribution at which no one gains by moving is 4 : 2 (equal intake). B: an individual-based version of
Milinski's (1979) stickleback experiment: six fish, each occasionally compares its intake with what it would get
at the other end and moves if that is better (with small errors); input ratio 1 : 2, reversed at t = 60.
Mean of 400 runs. C: unequal competitors (Milinski and Parker 1991): six fish eat twice as fast as the other
six; the number of arrangements that equalize intake per competitive unit for each count of fish in the rich
patch (input 2 : 1). The most likely count, 8, equals the prediction for equal competitors.
"""

from math import comb

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(0)

fig, ax = bio.canvas(33.0, 10.0)

# ---- A ----------------------------------------------------------------------------------------------------
pa = Ch.axes_at(ax, (2.4, 1.7, 8.0, 7.2))
n = np.arange(1, 9)
for Q, tok, name in ((2.0, "rna", "rich patch, Q = 2"), (1.0, "dna", "poor patch, Q = 1")):
    pa.plot(n, Q / n, "o-", color=Ch.line(tok), lw=1.5, ms=3.5)
    pa.text(n[-1] + 0.3, Q / n[-1], name, color=Ch.line(tok), fontsize=FS["tiny"], va="center")
pa.axhline(0.5, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.plot([4, 2], [0.5, 0.5], "o", ms=7, mfc="none", mec=P.ink(), mew=1.1)
pa.text(4.2, 0.62, "4 fish", fontsize=FS["tiny"], color=P.ink())
pa.text(2.2, 0.62, "2 fish", fontsize=FS["tiny"], color=P.ink())
pa.text(8.4, 0.54, "equal intake 0.5", fontsize=FS["tiny"], color=P.muted())
pa.set_xlim(0.5, 11.8)
pa.set_ylim(0, 2.1)
pa.set_xticks(range(1, 9))
Ch.style_axes(pa, "number of competitors in the patch", "intake per individual")
bio.panel(ax, "A", (0.3, 9.8))

# ---- B ----------------------------------------------------------------------------------------------------
T, runs, nfish = 120, 400, 6
qa = np.where(np.arange(T) < 60, 1.0, 2.0)  # input at end A; end B gets the complement of 3
counts = np.zeros((runs, T))
for r in range(runs):
    at_a = rng.random(nfish) < 0.5
    for t in range(T):
        Qa, Qb = qa[t], 3.0 - qa[t]
        for i in rng.permutation(nfish):
            if rng.random() > 0.15:
                continue
            na = at_a.sum()
            nb = nfish - na
            here, there = (Qa / na, Qb / (nb + 1)) if at_a[i] else (Qb / nb, Qa / (na + 1))
            if (there > here and rng.random() < 0.9) or rng.random() < 0.02:
                at_a[i] = not at_a[i]
        counts[r, t] = at_a.sum()
pb = Ch.axes_at(ax, (13.6, 1.7, 8.0, 7.2))
pb.step(np.arange(T), np.where(np.arange(T) < 60, 2, 4), where="post", color=P.muted(), lw=1.0, ls=(0, (3, 2)))
pb.plot(np.arange(T), counts.mean(0), color=Ch.line("rna"), lw=1.6)
pb.text(3, 2.25, "predicted", fontsize=FS["tiny"], color=P.muted())
pb.text(66, 3.3, "mean of simulated\ngroups", fontsize=FS["tiny"], color=Ch.line("rna"))
pb.axvline(60, color=P.muted(), lw=0.7)
pb.text(61, 5.5, "input reversed", fontsize=FS["tiny"], color=P.muted())
pb.set_xlim(0, T)
pb.set_ylim(0, 6)
Ch.style_axes(pb, "time / steps", "fish at end A")
bio.panel(ax, "B", (11.5, 9.8))

# ---- C ----------------------------------------------------------------------------------------------------
pc = Ch.axes_at(ax, (24.6, 1.7, 7.6, 7.2))
ks, ways = [], []
for big in range(7):          # big fish (2 units) in the rich patch
    small = 12 - 2 * big      # rich patch must hold 12 of the 18 units
    if 0 <= small <= 6:
        ks.append(big + small)
        ways.append(comb(6, big) * comb(6, small))
cols = [Ch.line("rna") if k == 8 else P.fill("neutral") for k in ks]
pc.bar(ks, ways, color=cols, edgecolor=P.muted(), lw=0.6, width=0.7)
for k, w in zip(ks, ways):
    pc.text(k, w + 6, str(w), ha="center", fontsize=FS["tiny"], color=P.ink())
pc.set_xticks(ks)
pc.set_ylim(0, 260)
Ch.style_axes(pc, "fish in the rich patch (of 12)", "number of arrangements")
pc.text(6.0, 238, "8 : 4 = equal-competitor IFD", fontsize=FS["tiny"], color=Ch.line("rna"))
bio.panel(ax, "C", (22.6, 9.8))
