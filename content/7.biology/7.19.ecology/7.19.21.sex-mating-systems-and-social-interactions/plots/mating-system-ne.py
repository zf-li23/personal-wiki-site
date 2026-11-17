"""Population consequences of mating systems: effective population size and mate-finding Allee effects.

A: effective population size Ne = 4 Nm Nf / (Nm + Nf) relative to the number of adults N = Nm + Nf, for
50 breeding females and an increasing number of breeding males (polygyny when Nm < Nf): with 5 harem
males Ne = 18.2, a third of the 55 breeders. B: Ne / N against the variance Vk of lifetime offspring number per individual,
Ne = (4N - 2) / (Vk + 2) (stable population, equal sex ratio; Vk = 2 for Poisson variation): high variance
in mating success, as in lekking and harem species, lowers Ne. C: a mate-finding Allee effect: per capita
growth rate g(N) = b N / (N + theta) - d - c N with b = 1, d = 0.2, c = 0.004 (simulated parameters), where
N / (N + theta) is the probability that a female finds a mate; for theta > 0 the per capita rate rises
at low density and is negative below an Allee threshold (open circles), which increases with theta.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(33.0, 12.0)

pa = C.axes_at(ax, (2.4, 1.8, 8.6, 8.6))
Nf = 50
Nm = np.arange(1, 101)
ne = 4 * Nm * Nf / (Nm + Nf)
pa.plot(Nm, ne / (Nm + Nf), color=Q.line_color("dna"), lw=1.8)
pa.axvline(Nf, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pa.text(52, 0.15, "equal sex ratio", fontsize=FS["tiny"], color=P.muted())
pa.set_xlim(0, 100)
pa.set_ylim(0, 1.05)
C.style_axes(pa, "breeding males (with 50 breeding females)", "Ne / N")
bio.panel(ax, "A", (0.4, 11.6))
bio.label(ax, (2.4, 11.2), "Unequal numbers of breeders", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (13.6, 1.8, 8.6, 8.6))
N = 200
Vk = np.linspace(0, 40, 300)
pb.plot(Vk, (4 * N - 2) / (Vk + 2) / N, color=Q.line_color("rna"), lw=1.8)
pb.axvline(2, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pb.text(2.6, 1.7, "Poisson", fontsize=FS["tiny"], color=P.muted())
pb.set_xlim(0, 40)
pb.set_ylim(0, 2.1)
C.style_axes(pb, "variance in lifetime offspring number, Vk", "Ne / N")
bio.panel(ax, "B", (11.8, 11.6))
bio.label(ax, (13.6, 11.2), "Variance in reproductive success", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (24.6, 1.8, 8.0, 8.6))
n = np.linspace(0.5, 220, 500)
b, d, c = 1.0, 0.2, 0.004
for th, tok in [(0, "positive"), (10, "dna"), (30, "enzyme"), (60, "rna")]:
    g = b * n / (n + th) - d - c * n
    pc.plot(n, g, color=Q.line_color(tok), lw=1.6, label=f"theta = {th}")
    roots = n[:-1][np.sign(g[:-1]) != np.sign(g[1:])]
    if th > 0 and len(roots) == 2:
        pc.plot(roots[0], 0, "o", mfc=P.surface(), mec=Q.line_color(tok), ms=5, mew=1.2)
pc.axhline(0, color=P.muted(), lw=0.8)
pc.set_xlim(0, 220)
pc.set_ylim(-0.25, 0.85)
C.style_axes(pc, "population density N", "per capita growth rate")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (23.0, 11.6))
bio.label(ax, (24.6, 11.2), "Mate-finding Allee effect", size="small", bold=True, ha="left")
