"""Resource utilization curves, niche overlap and limiting similarity (MacArthur and Levins 1967; May 1973).

A: Gaussian utilization curves of width (standard deviation) w for three species with peaks d apart on a
one-dimensional resource axis, for d/w = 0.8 (upper, broad overlap) and d/w = 2 (lower). B: the
competition coefficient between adjacent species computed from the overlap of the curves,
a = exp(-d^2 / (4 w^2)) (Proposition 23.2.1), and between the outer species, a^4. C: the range of the
ratio K2/K1 of the carrying capacity of the middle species to that of the two outer ones (K3 = K1) for
which all three species have positive equilibrium densities, 2a/(1 + a^4) < K2/K1 < 1/a (shaded,
log scale). The range narrows steeply as d/w falls below about 1: very similar species can coexist only
if their environments suit them almost equally.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(33.0, 12.0)
toks = ["dna", "positive", "rna"]

pa = C.axes_at(ax, (2.2, 6.4, 8.8, 3.9))
pa2 = C.axes_at(ax, (2.2, 1.6, 8.8, 3.9))
x = np.linspace(-6, 6, 500)
for p, dw in [(pa, 0.8), (pa2, 2.0)]:
    for k, tok in zip((-1, 0, 1), toks):
        p.plot(x, np.exp(-(x - k * dw) ** 2 / 2), color=Q.line_color(tok), lw=1.6)
        p.fill_between(x, np.exp(-(x - k * dw) ** 2 / 2), color=P.mix(P.fill(tok), P.surface(), 0.75), lw=0)
    p.set_xlim(-6, 6)
    p.set_ylim(0, 1.15)
    p.set_yticks([])
    p.text(-5.8, 1.0, f"d/w = {dw}", fontsize=FS["tiny"], color=P.ink())
pa.set_xticks([])
C.style_axes(pa, None, "use")
C.style_axes(pa2, "resource (e.g. food size), units of w", "use")
bio.panel(ax, "A", (0.3, 11.6))
bio.label(ax, (2.2, 11.2), "Utilization curves", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (13.6, 1.6, 8.0, 8.7))
r = np.linspace(0, 4, 400)
a = np.exp(-r ** 2 / 4)
pb.plot(r, a, color=Q.line_color("dna"), lw=1.8, label="adjacent species, a")
pb.plot(r, a ** 4, color=Q.line_color("rna"), lw=1.4, ls=(0, (4, 2)), label="outer species, a^4")
pb.set_xlim(0, 4)
pb.set_ylim(0, 1.02)
C.style_axes(pb, "niche separation d/w", "competition coefficient")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (12.0, 11.6))
bio.label(ax, (13.6, 11.2), "Overlap and competition", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (24.8, 1.6, 8.0, 8.7))
r = np.linspace(0.2, 3, 500)
a = np.exp(-r ** 2 / 4)
lo, hi = 2 * a / (1 + a ** 4), 1 / a
pc.fill_between(r, lo, hi, color=P.mix(P.fill("positive"), P.surface(), 0.5), lw=0)
pc.plot(r, lo, color=P.ink(), lw=1.0)
pc.plot(r, hi, color=P.ink(), lw=1.0)
pc.set_yscale("log")
pc.set_xlim(0.2, 3)
pc.set_ylim(0.3, 10)
pc.text(2.2, 1.0, "three species\ncoexist", fontsize=FS["small"], color=P.ink(), ha="center")
pc.text(0.9, 0.45, "middle species excluded", fontsize=FS["tiny"], color=P.muted())
pc.text(0.9, 5.0, "outer species excluded", fontsize=FS["tiny"], color=P.muted())
C.style_axes(pc, "niche separation d/w", "K2 / K1 (log scale)")
bio.panel(ax, "C", (23.2, 11.6))
bio.label(ax, (24.8, 11.2), "Limiting similarity", size="small", bold=True, ha="left")
