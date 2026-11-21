"""Genetic rescue in a model of a small, inbred population (loosely parameterized on the Florida panther).

Time step: one year; generation time G = 6 years, so drift raises F by 1/(2 N_e G) per year.
Demography: N_{t+1} ~ Poisson(N_t exp(r(F_t) - r0 N_t / K)), K = 150, with inbreeding depression in the
intrinsic growth rate r(F) = r0 - delta F, r0 = 0.30, delta = 1.0 (r < 0 for F > 0.30); equilibrium N* = K(1 - delta F / r0).
Inbreeding: with effective size N_e = 0.4 N, F_{t+1} = (1 - q_t)^2 [d + (1 - d) F_t], d = 1/(2 N_e G), where
q_t is the proportion of immigrants (outbred, F = 0, unrelated) among breeders that year; offspring with an
immigrant parent are not inbred, so with random mating a fraction (1 - q)^2 of matings are between residents
(the effect is applied in the year of release, a simplification of the spread of immigrant ancestry).
Start: N = 25, F = 0.25 (near its equilibrium, which declines as F rises). Rescue: 8 immigrants released in year 10.
A: population size, 30 replicates each without (gray) and with rescue (blue); thick lines: medians.
B: mean inbreeding coefficient F and expected heterozygosity relative to an outbred population, 1 - F.
C: probability of persistence for 100 years against the number of immigrants released once in year 10
(points), and with one immigrant every 5 years thereafter in addition (squares); 400 replicates each.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(17)
K, r0, delta, T, G = 150, 0.30, 1.0, 100, 6.0


def run(m, every=0):
    N, F = 25, 0.25
    Ns, Fs = [N], [F]
    for t in range(T):
        add = (m if t == 10 else 0) + (1 if every and t > 10 and t % every == 0 else 0)
        Nb = N + add
        if Nb == 0:
            Ns.append(0)
            Fs.append(F)
            continue
        q = add / Nb
        Ne = max(0.4 * Nb, 1.0)
        dF = 1 / (2 * Ne * G)
        F = (1 - q) ** 2 * (dF + (1 - dF) * F)
        N = rng.poisson(Nb * np.exp(r0 - delta * F - r0 * Nb / K))
        Ns.append(N)
        Fs.append(F)
    return np.array(Ns), np.array(Fs)


fig, ax = bio.canvas(32.0, 11.0)
pa = C.axes_at(ax, (2.2, 1.6, 9.2, 7.4))
pb = C.axes_at(ax, (13.6, 1.6, 7.4, 7.4))
tt = np.arange(T + 1)
for m, tok in ((0, "neutral"), (8, "dna")):
    sims = [run(m) for _ in range(30)]
    Ns = np.array([s[0] for s in sims])
    Fs = np.array([s[1] for s in sims])
    for row in Ns:
        pa.plot(tt, row, color=Q.line_color(tok), lw=0.5, alpha=0.35)
    pa.plot(tt, np.median(Ns, 0), color=Q.line_color(tok), lw=2.0, label="8 immigrants in year 10" if m else "no immigration")
    Fm = np.array([f[n > 0].mean() if (n > 0).any() else np.nan for f, n in zip(Fs.T, Ns.T)])
    pb.plot(tt, Fm, color=Q.line_color(tok), lw=1.7, label=("rescue" if m else "no rescue") + ": F")
    pb.plot(tt, 1 - Fm, color=Q.line_color(tok), lw=1.2, ls=(0, (4, 2)), label=("rescue" if m else "no rescue") + ": 1 - F")
pa.axvline(10, color=P.muted(), lw=0.8, ls=(0, (2, 2)))
pa.set_xlim(0, T)
pa.set_ylim(0, 200)
C.style_axes(pa, "year", "population size N")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.5, 10.6))
bio.label(ax, (2.2, 10.2), "Demographic recovery after gene flow", size="small", bold=True, ha="left")
pb.axhline(r0 / delta, color=Q.line_color("negative"), lw=0.8, ls=(0, (1, 1.5)))
pb.text(98, r0 / delta + 0.02, f"r(F) = 0 at F = {r0 / delta:.2f}", ha="right", fontsize=FS["tiny"], color=Q.line_color("negative"))
pb.set_xlim(0, T)
pb.set_ylim(0, 1.3)
pb.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
C.style_axes(pb, "year", "inbreeding F, heterozygosity 1 - F")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper center", ncol=2)
bio.panel(ax, "B", (12.2, 10.6))
bio.label(ax, (13.6, 10.2), "Inbreeding reset", size="small", bold=True, ha="left")

ms = [0, 1, 2, 4, 8, 16]
pc = C.axes_at(ax, (24.0, 1.6, 7.0, 7.4))
for every, mk, tok, lab in ((0, "o-", "dna", "single release"), (5, "s--", "plant", "plus 1 immigrant every 5 years")):
    pers = [np.mean([run(m, every)[0][-1] > 0 for _ in range(400)]) for m in ms]
    pc.plot(ms, pers, mk, color=Q.line_color(tok), lw=1.5, ms=4, label=lab)
pc.set_ylim(0, 1.05)
C.style_axes(pc, "immigrants released in year 10", "P(persist 100 years)")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "C", (22.4, 10.6))
bio.label(ax, (24.0, 10.2), "How many migrants?", size="small", bold=True, ha="left")
