"""Effective population size and the loss of genetic diversity.

A: expected heterozygosity in Wright-Fisher populations of N_e = 10, 50 and 250 diploids (mean of 2000
biallelic loci starting at p = 0.5, points every 5 generations) and the prediction
H_t = H_0 (1 - 1/(2 N_e))^t (lines).
B: effective size of a population with N_m breeding males and N_f breeding females, N_e = 4 N_m N_f /
(N_m + N_f), relative to N = N_m + N_f, against the proportion of males; at most N_e = N for an equal
sex ratio.
C: a population that fluctuates between 1000 and 1500 individuals except for a crash to 20 in generation
5 (bars, log scale): the arithmetic mean size over ten generations is 1182, the harmonic mean (the
effective size, line) only 175.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(0)
fig, ax = bio.canvas(30.0, 10.0)

pa = C.axes_at(ax, (2.0, 1.6, 7.0, 6.8))
T = 100
t = np.arange(T + 1)
for Ne, tok in [(10, "negative"), (50, "enzyme"), (250, "dna")]:
    p = np.full(2000, 0.5)
    H = [np.mean(2 * p * (1 - p))]
    for _ in range(T):
        p = rng.binomial(2 * Ne, p) / (2 * Ne)
        H.append(np.mean(2 * p * (1 - p)))
    H = np.array(H)
    pa.plot(t[::5], H[::5], "o", ms=3, color=Q.line_color(tok))
    pa.plot(t, 0.5 * (1 - 1 / (2 * Ne)) ** t, color=Q.line_color(tok), lw=1.4, label=f"N_e = {Ne}")
pa.set_xlim(0, T)
pa.set_ylim(0, 0.55)
C.style_axes(pa, "generation t", "expected heterozygosity H_t")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Drift erodes heterozygosity", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.0, 1.6, 7.0, 6.8))
q = np.linspace(0.005, 0.995, 400)
pb.plot(q, 4 * q * (1 - q), color=Q.line_color("protein"), lw=1.8)
for qq, lab in [(0.5, "1:1"), (0.1, "1 male : 9 females")]:
    pb.plot(qq, 4 * qq * (1 - qq), "o", ms=5, color=Q.line_color("protein"))
    pb.text(qq + 0.02, 4 * qq * (1 - qq) + 0.04, lab, fontsize=FS["tiny"], color=P.ink())
pb.set_xlim(0, 1)
pb.set_ylim(0, 1.12)
C.style_axes(pb, "proportion of breeders that are male", "N_e / N")
bio.panel(ax, "B", (10.5, 9.6))
bio.label(ax, (12.0, 9.2), "Unequal sex ratio", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.5, 1.6, 7.0, 6.8))
sizes = np.array([1200, 1400, 1000, 1500, 1300, 20, 1100, 1300, 1500, 1500])
gen = np.arange(1, 11)
pc.bar(gen, sizes, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.8)
hm = len(sizes) / np.sum(1 / sizes)
am = sizes.mean()
pc.axhline(am, color=P.muted(), lw=1.0, ls=(0, (4, 2)))
pc.axhline(hm, color=Q.line_color("negative"), lw=1.6)
pc.text(10.4, am * 1.08, f"arithmetic mean {am:.0f}", fontsize=FS["tiny"], color=P.ink(), ha="right")
pc.text(10.4, hm * 1.12, f"harmonic mean N_e = {hm:.0f}", fontsize=FS["tiny"], color=Q.line_color("negative"), ha="right")
pc.set_yscale("log")
pc.set_ylim(10, 3000)
pc.set_xlim(0.4, 10.6)
C.style_axes(pc, "generation", "census size N (log scale)")
bio.panel(ax, "C", (21.0, 9.6))
bio.label(ax, (22.5, 9.2), "Fluctuating size", size="small", bold=True, ha="left")
