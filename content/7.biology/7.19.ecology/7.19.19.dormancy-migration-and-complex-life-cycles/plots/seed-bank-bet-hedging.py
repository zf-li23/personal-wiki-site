"""Cohen's (1966) model of germination in a random environment.

Each year a fraction g of the seeds in the bank germinates; a year is good with probability p, when each
germinating seed yields Y = 10 seeds, and bad otherwise (yield 0). Seeds that stay in the bank survive
with probability s = 0.8. The bank multiplies by lambda = g Y + (1 - g) s in good and (1 - g) s in bad
years, and the long-run growth rate is E[ln lambda].
A: E[ln lambda] against g for p = 0.3, 0.5 and 0.8; points: the optimum g* = p - (1 - p) s / (Y - s).
B: g* against p for s = 0.5, 0.8 and 0.95 (lines) compared with g = p (dashed): germination is spread
over years, the more so the better seeds survive in the soil.
C: 60 years of the seed bank (log scale, same random sequence of years, p = 0.5) for g = 1 (all seeds
germinate; wiped out by the first bad year, cross), g = g* = 0.46 and g = 0.1.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(1)
fig, ax = bio.canvas(30.0, 10.0)
Y, s = 10.0, 0.8
g = np.linspace(0.001, 0.999, 500)


def growth(g, p, s=s):
    return p * np.log(g * Y + (1 - g) * s) + (1 - p) * np.log((1 - g) * s)


def gstar(p, s=s):
    return np.clip(p - (1 - p) * s / (Y - s), 0, 1)


pa = C.axes_at(ax, (2.0, 1.6, 7.0, 6.8))
for p, tok in [(0.3, "negative"), (0.5, "enzyme"), (0.8, "dna")]:
    pa.plot(g, growth(g, p), color=Q.line_color(tok), lw=1.6, label=f"p = {p}")
    gs = gstar(p)
    pa.plot(gs, growth(gs, p), "o", ms=5, color=Q.line_color(tok))
pa.axhline(0, color=P.muted(), lw=0.7)
pa.set_xlim(0, 1)
pa.set_ylim(-1.5, 1.5)
C.style_axes(pa, "fraction germinating each year g", "long-run growth E[ln lambda]")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Growth of the seed bank", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.0, 1.6, 7.0, 6.8))
pp = np.linspace(0, 1, 300)
for ss, tok in [(0.5, "dna"), (0.8, "enzyme"), (0.95, "negative")]:
    pb.plot(pp, gstar(pp, ss), color=Q.line_color(tok), lw=1.6, label=f"s = {ss}")
pb.plot([0, 1], [0, 1], color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.set_xlim(0, 1)
pb.set_ylim(0, 1)
C.style_axes(pb, "probability of a good year p", "optimal germination fraction g*")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (10.5, 9.6))
bio.label(ax, (12.0, 9.2), "Optimal germination", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.5, 1.6, 7.0, 6.8))
p = 0.5
good = rng.random(60) < p
for gg, tok, lab in [(1.0, "negative", "g = 1"), (gstar(p), "enzyme", f"g* = {gstar(p):.2f}"), (0.1, "dna", "g = 0.1")]:
    N = [1.0]
    for gd in good:
        lam = (gg * Y if gd else 0.0) + (1 - gg) * s
        N.append(N[-1] * lam)
    N = np.array(N)
    t = np.arange(61)
    ok = N > 0
    pc.semilogy(t[ok], N[ok], color=Q.line_color(tok), lw=1.5, label=lab)
    if not ok.all():
        k = np.argmin(ok)
        pc.plot(t[k - 1], N[k - 1], "x", ms=6, color=Q.line_color(tok))
pc.set_xlim(0, 60)
pc.set_ylim(1e-2, 1e12)
C.style_axes(pc, "year", "seeds in bank (log scale)")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "C", (21.0, 9.6))
bio.label(ax, (22.5, 9.2), "One random sequence of years", size="small", bold=True, ha="left")
