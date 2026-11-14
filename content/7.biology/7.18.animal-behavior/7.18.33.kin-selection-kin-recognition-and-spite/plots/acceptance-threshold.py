"""Kin recognition as signal detection: the acceptance threshold model (Reeve 1989).

A: a recognizer compares a cue of each individual it meets with its template. The perceived dissimilarity
(arbitrary units) is distributed around 1 for kin and around 3 for non-kin (normal, s.d. 0.8). It accepts
individuals whose dissimilarity is below a threshold t = 2: kin above t are wrongly rejected, non-kin below t
are wrongly accepted.
B: the threshold that maximizes the expected payoff, when accepting kin gains 1, accepting non-kin costs c and
rejection gives 0, against the proportion of non-kin among the individuals met. The optimum solves
p f_kin(t) = (1 - p) c f_nonkin(t): recognizers should become less permissive (lower t) when non-kin are common or
costly to accept.
"""

import math
import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
mk, mn, sd = 1.0, 3.0, 0.8


def pdf(x, m):
    return np.exp(-0.5 * ((x - m) / sd) ** 2) / (sd * math.sqrt(2 * math.pi))


fig, ax = bio.canvas(30.0, 10.0)
pa = Ch.axes_at(ax, (2.2, 1.8, 11.5, 7.2))
x = np.linspace(-1.5, 5.5, 400)
t = 2.0
fk, fn = pdf(x, mk), pdf(x, mn)
pa.plot(x, fk, color=Ch.line("positive"), lw=1.6)
pa.plot(x, fn, color=Ch.line("negative"), lw=1.6)
pa.fill_between(x[x >= t], fk[x >= t], color=P.mix(P.fill("positive"), P.surface(), 0.35), lw=0)
pa.fill_between(x[x <= t], fn[x <= t], color=P.mix(P.fill("negative"), P.surface(), 0.35), lw=0)
pa.axvline(t, color=P.ink(), lw=1.0, ls=(0, (4, 2)))
pa.text(t + 0.08, 0.40, "acceptance\nthreshold t", fontsize=FS["tiny"], color=P.ink(), va="top")
pa.text(mk - 0.9, 0.47, "kin", fontsize=FS["small"], color=Ch.line("positive"), ha="center")
pa.text(mn + 0.9, 0.47, "non-kin", fontsize=FS["small"], color=Ch.line("negative"), ha="center")
pa.annotate("kin rejected", (2.25, 0.04), (3.6, 0.3), fontsize=FS["tiny"], color=P.ink(),
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
pa.annotate("non-kin accepted", (1.75, 0.04), (-1.2, 0.3), fontsize=FS["tiny"], color=P.ink(),
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
pa.text(t - 0.1, 0.565, "accept", fontsize=FS["tiny"], color=P.muted(), ha="right")
pa.text(t + 0.1, 0.565, "reject", fontsize=FS["tiny"], color=P.muted())
pa.set_xlim(-1.5, 5.5)
pa.set_ylim(0, 0.6)
pa.set_yticks([])
Ch.style_axes(pa, "dissimilarity between cue and template")
bio.panel(ax, "A", (0.3, 9.8))

pb = Ch.axes_at(ax, (18.0, 1.8, 11.0, 7.2))
q = np.linspace(0.02, 0.98, 200)
for c, tok in ((0.5, "dna"), (1.0, "protein"), (3.0, "rna")):
    # log(fk / fn) = log(q c / (1 - q)) is linear in t
    k = np.log(q * c / (1 - q))
    tt = (mn ** 2 - mk ** 2 - 2 * sd ** 2 * k) / (2 * (mn - mk))
    pb.plot(q, tt, color=Ch.line(tok), lw=1.6)
    pb.text(q[-1] + 0.01, tt[-1], f"c = {c:g}", fontsize=FS["tiny"], color=Ch.line(tok), va="center")
pb.axhline((mk + mn) / 2, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pb.text(0.03, (mk + mn) / 2 + 0.08, "midpoint", fontsize=FS["tiny"], color=P.muted())
pb.set_xlim(0, 1.12)
pb.set_ylim(0, 4)
Ch.style_axes(pb, "proportion of non-kin among individuals met", "optimal threshold t*")
bio.panel(ax, "B", (15.6, 9.8))
