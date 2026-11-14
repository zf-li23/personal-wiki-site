"""Two models of reproductive skew.

A, B: the concession (transactional) model (Vehrencamp 1983; Reeve and Ratnieks 1993). A dominant breeding alone
produces 1 unit of offspring, a subordinate breeding alone x; together they produce k = 1.5. The dominant controls
reproduction and concedes to the subordinate just the share that makes staying worthwhile, the staying incentive
p = max(0, (x - r (k - 1)) / (k (1 - r))), where r is their relatedness. A: p against r for three values of x. B: p
against x for unrelated (r = 0) and related (r = 1/2) partners: skew is high (p small) when relatedness is high and
when solitary breeding is poor (strong ecological constraints).
C: a tug-of-war model (after Reeve, Emlen and Keller 1998). Neither party controls reproduction; each invests a
fraction y of the group's output in competition, the group produces 1 - y_d - y_s, and the subordinate's share
is y_s / (a y_d + y_s), where a is the dominant's competitive advantage. At the Nash equilibrium (found numerically)
the share depends mainly on a, while relatedness reduces the output wasted in competition.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
k = 1.5


def inc(x, r):
    return np.clip((x - r * (k - 1)) / (k * (1 - r)), 0, 1)


fig, ax = bio.canvas(33.0, 10.0)
pa = Ch.axes_at(ax, (2.4, 1.8, 7.8, 7.0))
r = np.linspace(0, 0.9, 200)
for x, tok in ((0.1, "dna"), (0.25, "protein"), (0.4, "rna")):
    pa.plot(r, inc(x, r), color=Ch.line(tok), lw=1.6)
    pa.text(0.02, inc(x, 0) + 0.015, f"x = {x:g}", fontsize=FS["tiny"], color=Ch.line(tok), va="bottom")
pa.set_xlim(0, 0.9)
pa.set_ylim(0, 0.3)
Ch.style_axes(pa, "relatedness r", "subordinate's share p")
Ch.title(pa, "concession model")
bio.panel(ax, "A", (0.3, 9.8))

pb = Ch.axes_at(ax, (13.2, 1.8, 7.8, 7.0))
xs = np.linspace(0, 0.45, 200)
for rr, tok in ((0.0, "rna"), (0.5, "dna")):
    pb.plot(xs, inc(xs, rr), color=Ch.line(tok), lw=1.6)
    pb.text(0.44, inc(0.44, rr) + 0.01, f"r = {rr:g}", fontsize=FS["tiny"], color=Ch.line(tok), ha="right", va="bottom")
pb.set_xlim(0, 0.45)
pb.set_ylim(0, 0.3)
Ch.style_axes(pb, "solitary output of subordinate x", None)
Ch.title(pb, "ecological constraints")
bio.panel(ax, "B", (11.2, 9.8))


def br(f):
    y = np.linspace(1e-4, 0.999, 3000)
    return y[np.argmax(f(y))]


def nash(rr, a):
    yd = ys = 0.1
    for _ in range(60):
        yd = br(lambda y: np.where(y < 1 - ys, (1 - y - ys) * ((a * y / (a * y + ys)) * (1 - rr) + rr), -1))
        ys = br(lambda y: np.where(y < 1 - yd, (1 - yd - y) * ((1 - a * yd / (a * yd + y)) * (1 - rr) + rr), -1))
    return yd, ys


pc = Ch.axes_at(ax, (24.2, 1.8, 8.2, 7.0))
rs = np.linspace(0, 0.8, 9)
for a, tok in ((1.0, "protein"), (2.0, "dna")):
    sh, wst = [], []
    for rr in rs:
        yd, ys = nash(rr, a)
        sh.append(ys / (a * yd + ys))
        wst.append(yd + ys)
    pc.plot(rs, sh, "o-", ms=3, color=Ch.line(tok), lw=1.5)
    pc.plot(rs, wst, "s--", ms=3, color=Ch.line(tok), lw=1.2)
    pc.text(0.81, sh[-1], f"share, a = {a:g}", fontsize=FS["tiny"], color=Ch.line(tok), va="center")
    pc.text(0.81, wst[-1] + (0.02 if a == 1 else -0.02), f"wasted, a = {a:g}", fontsize=FS["tiny"],
            color=Ch.line(tok), va="center")
pc.set_xlim(0, 1.05)
pc.set_ylim(0, 0.6)
Ch.style_axes(pc, "relatedness r", "fraction")
Ch.title(pc, "tug of war")
bio.panel(ax, "C", (22.0, 9.8))
