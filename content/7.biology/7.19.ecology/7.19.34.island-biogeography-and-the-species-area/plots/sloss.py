"""SLOSS: one large reserve or several small ones of the same total area.

A one-dimensional region of length 1 (a coastline or a mountain chain) holds 300 species. Species i occupies
an interval of length w_i (lognormal, median 0.05) at a uniformly random position, and persists in a
reserve only if the reserve contains a stretch of its range at least a_i long (the area it needs for a
viable population; a_i = f w_i' with w_i' lognormal, so that wide-ranging species tend to need more area).
Reserves of total length 0.1 are split into k equal pieces spaced evenly along the region; a species is
protected if at least one piece meets its requirement. A: protected species against k for three
requirement scenarios (median a_i = 0, 0.004 and 0.015), mean of 200 random communities (bands: central
90 %). B: protected species against the median requirement for k = 1 (single large) and k = 8 (several
small), mean of 80 communities; they cross where the typical requirement approaches the length of one small
reserve. C: 60 of the ranges of one community (gray) and the two configurations: for k = 8 the pieces
sample many independent parts of the region (beta diversity), but each piece is short and loses the
species whose requirement exceeds 0.1/8.
"""

import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(11)

NS, TOTAL = 300, 0.1
ks = np.array([1, 2, 3, 4, 6, 8, 12, 16, 24, 32])


def community():
    w = np.exp(rng.normal(np.log(0.05), 1.0, NS))
    w = np.minimum(w, 1.0)
    start = rng.random(NS)
    req = np.exp(rng.normal(0, 0.7, NS)) * np.sqrt(w / 0.05)
    return start, w, req


def overlap(s, w, a, b):
    """Length of the intersection of the circular range [s, s + w) with [a, b)."""
    tot = 0.0
    for shift in (-1.0, 0.0, 1.0):
        lo = np.maximum(s + shift, a)
        hi = np.minimum(s + shift + w, b)
        tot = tot + np.clip(hi - lo, 0, None)
    return tot


def protected(start, w, req, k, med):
    L = TOTAL / k
    best = np.zeros(NS)
    for j in range(k):
        a = (j + 0.5) / k - L / 2
        best = np.maximum(best, overlap(start, w, a, a + L))
    need = med * req
    return ((best > 0) & (best >= need)).sum()


comms = [community() for _ in range(200)]

fig, ax = bio.canvas(31.0, 10.0)
pa = C.axes_at(ax, (2.2, 1.6, 7.4, 6.8))
for med, tok in ((0.0, "plant"), (0.004, "protein"), (0.015, "negative")):
    R = np.array([[protected(*cm, k, med) for k in ks] for cm in comms])
    c = Q.line_color(tok)
    pa.fill_between(ks, np.percentile(R, 5, 0), np.percentile(R, 95, 0), color=c, alpha=0.15, lw=0)
    pa.plot(ks, R.mean(0), "-o", ms=3, color=c, lw=1.6, label=f"median requirement {med:g}")
pa.set_xscale("log", base=2)
pa.set_xticks(ks)
pa.set_xticklabels([str(k) for k in ks])
pa.set_xlim(0.9, 36)
pa.set_ylim(0, 300)
C.style_axes(pa, "number of reserves k (total area fixed)", "species protected")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.4, 9.6))
bio.label(ax, (2.2, 9.2), "Several small versus single large", size="small", bold=True, ha="left")

meds = np.linspace(0, 0.03, 16)
pb = C.axes_at(ax, (12.6, 1.6, 7.0, 6.8))
for k, tok, lab in ((1, "dna", "single large (k = 1)"), (8, "enzyme", "several small (k = 8)")):
    vals = [np.mean([protected(*cm, k, m) for cm in comms[:80]]) for m in meds]
    pb.plot(meds, vals, "-o", ms=3, color=Q.line_color(tok), lw=1.6, label=lab)
pb.axvline(TOTAL / 8, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.text(TOTAL / 8 + 0.0005, 185, "length of one\nsmall reserve", fontsize=FS["tiny"], color=P.muted(), va="top")
pb.set_xlim(0, 0.03)
pb.set_ylim(0, 200)
C.style_axes(pb, "median area requirement", "species protected")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "B", (11.1, 9.6))
bio.label(ax, (12.6, 9.2), "The answer depends on area requirements", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.8, 1.6, 7.4, 6.8))
start, w, req = comms[0]
sub = rng.choice(NS, 60, replace=False)
order = sub[np.argsort(start[sub])]
for row, i in enumerate(order):
    s0, ww = start[i], w[i]
    for shift in (0.0, -1.0):
        pc.plot([s0 + shift, s0 + shift + ww], [row, row], color=Q.line_color("muted"), lw=1.2, solid_capstyle="butt")
for k, y0, tok in ((1, -6, "dna"), (8, -10, "enzyme")):
    L = TOTAL / k
    for j in range(k):
        a = (j + 0.5) / k - L / 2
        pc.add_patch(Rectangle((a, y0), L, 2.5, color=Q.line_color(tok), lw=0))
        pc.axvspan(a, a + L, color=Q.line_color(tok), alpha=0.06, lw=0)
pc.text(1.0, -4.6, "k = 1", fontsize=FS["tiny"], color=Q.line_color("dna"), ha="right")
pc.text(1.0, -8.6, "k = 8", fontsize=FS["tiny"], color=Q.line_color("enzyme"), ha="right")
pc.set_xlim(0, 1)
pc.set_ylim(-11, 61)
pc.set_yticks([])
C.style_axes(pc, "position along the region", "species ranges (60 of 300)")
bio.panel(ax, "C", (21.3, 9.6))
bio.label(ax, (22.8, 9.2), "Ranges and reserves", size="small", bold=True, ha="left")
