"""Lack's optimal clutch size and the cost of reproduction.

Each of n nestlings survives to recruit with probability s(n) = s0 (1 - n/N) (s0 = 0.5, N = 16): parents
cannot feed large broods. Recruits from one brood: n s(n), maximal at the Lack clutch n_L = N/2 = 8.
Cost of reproduction: the parent survives to breed again with probability P(n) = P0 - c n
(P0 = 0.6, c = 0.04) and a surviving parent is worth V = 2 recruits (its residual reproductive value).
Total fitness n s(n) + V P(n) is maximal at n* = (N/2)(1 - cV/s0) = 6.7.
A: offspring survival s(n) and parental survival P(n). B: recruits per brood, the parental component and
their sum, with the two optima. C: n* against the residual reproductive value V for three costs c.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)
s0, N, P0, c, V = 0.5, 16.0, 0.6, 0.04, 2.0
n = np.linspace(0, N, 400)
s = s0 * (1 - n / N)
Pn = P0 - c * n

pa = C.axes_at(ax, (2.0, 1.6, 7.0, 6.8))
pa.plot(n, s, color=Q.line_color("dna"), lw=1.6, label="survival of each nestling s(n)")
pa.plot(n, np.clip(Pn, 0, None), color=Q.line_color("negative"), lw=1.6, label="parental survival P(n)")
pa.set_xlim(0, N)
pa.set_ylim(0, 0.7)
C.style_axes(pa, "clutch size n", "probability")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Survival falls with brood size", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.0, 1.6, 7.0, 6.8))
rec = n * s
par = V * np.clip(Pn, 0, None)
tot = rec + par
pb.plot(n, rec, color=Q.line_color("dna"), lw=1.6, label="recruits n s(n)")
pb.plot(n, par, color=Q.line_color("negative"), lw=1.2, ls=(0, (4, 2)), label="parent V P(n)")
pb.plot(n, tot, color=Q.line_color("protein"), lw=1.8, label="total fitness")
nl = N / 2
ns = nl * (1 - c * V / s0)
pb.axvline(nl, color=Q.line_color("dna"), lw=0.8, ls=(0, (3, 2)))
pb.axvline(ns, color=Q.line_color("protein"), lw=0.8, ls=(0, (3, 2)))
pb.text(nl + 0.2, 0.15, f"Lack clutch {nl:.0f}", fontsize=FS["tiny"], color=Q.line_color("dna"))
pb.text(ns - 0.2, 0.15, f"optimum {ns:.1f}", fontsize=FS["tiny"], color=Q.line_color("protein"), ha="right")
pb.set_xlim(0, N)
pb.set_ylim(0, 3.5)
C.style_axes(pb, "clutch size n", "expected recruits")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (10.5, 9.6))
bio.label(ax, (12.0, 9.2), "A cost of reproduction", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.5, 1.6, 7.0, 6.8))
Vs = np.linspace(0, 6, 200)
for cc, tok in [(0.01, "dna"), (0.04, "protein"), (0.08, "negative")]:
    pc.plot(Vs, np.clip(nl * (1 - cc * Vs / s0), 0, None), color=Q.line_color(tok), lw=1.6, label=f"c = {cc}")
pc.axhline(nl, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pc.set_xlim(0, 6)
pc.set_ylim(0, 9)
C.style_axes(pc, "residual reproductive value V", "optimal clutch size n*")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "C", (21.0, 9.6))
bio.label(ax, (22.5, 9.2), "Long-lived parents lay fewer eggs", size="small", bold=True, ha="left")
