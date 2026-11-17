"""Ideal free and ideal despotic distributions between two habitats (Fretwell and Lucas 1970), simulated.

Basic suitability (expected reproductive success) declines with density: S1(d) = 4 - 0.1 d in habitat 1
and S2(d) = 2.5 - 0.1 d in habitat 2 (equal area). Ideal free: individuals settle where their expected
success is highest, so habitat 2 is used only once S1 has fallen to 2.5 (at d1 = 15), after which
realized success is equal in both. Ideal despotic: territory owners in habitat 1 exclude others once
12 territories are taken; later arrivals must settle in habitat 2 even though success in habitat 1
remains higher. A: realized success per individual in each habitat against total population size
(solid: free; dashed: despotic). B: number of individuals in each habitat. Under the despotic
distribution densities in good habitat are capped and do not reflect habitat quality; mean success
declines with N in both cases (density dependence at the population level).
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)
B1, B2, c, cap = 4.0, 2.5, 0.1, 12
N = np.linspace(0, 40, 401)


def free(n):
    t = (B1 - B2) / c
    if n <= t:
        return n, 0.0
    extra = n - t
    return t + extra / 2, extra / 2


def despot(n):
    return min(n, cap), max(n - cap, 0.0)


F = np.array([free(n) for n in N])
Dd = np.array([despot(n) for n in N])
c1, c2 = Q.line_color("positive"), Q.line_color("rna")

pa = C.axes_at(ax, (2.4, 1.8, 11.5, 8.6))
pa.plot(N, B1 - c * F[:, 0], color=c1, lw=1.8, label="habitat 1, free")
pa.plot(N[F[:, 1] > 0], B2 - c * F[F[:, 1] > 0, 1], color=c2, lw=1.8, label="habitat 2, free")
pa.plot(N, B1 - c * Dd[:, 0], color=c1, lw=1.6, ls=(0, (4, 2)), label="habitat 1, despotic")
m = Dd[:, 1] > 0
pa.plot(N[m], B2 - c * Dd[m, 1], color=c2, lw=1.6, ls=(0, (4, 2)), label="habitat 2, despotic")
pa.set_xlim(0, 40)
pa.set_ylim(0, 4.2)
C.style_axes(pa, "total number of individuals", "realized success per individual")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left", ncol=2)
bio.panel(ax, "A", (0.4, 11.6))
bio.label(ax, (2.4, 11.2), "Success in each habitat", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (17.0, 1.8, 11.5, 8.6))
pb.plot(N, F[:, 0], color=c1, lw=1.8, label="habitat 1, free")
pb.plot(N, F[:, 1], color=c2, lw=1.8, label="habitat 2, free")
pb.plot(N, Dd[:, 0], color=c1, lw=1.6, ls=(0, (4, 2)), label="habitat 1, despotic")
pb.plot(N, Dd[:, 1], color=c2, lw=1.6, ls=(0, (4, 2)), label="habitat 2, despotic")
pb.set_xlim(0, 40)
pb.set_ylim(0, 30)
C.style_axes(pb, "total number of individuals", "number in habitat")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left", ncol=2)
bio.panel(ax, "B", (15.0, 11.6))
bio.label(ax, (17.0, 11.2), "Distribution between habitats", size="small", bold=True, ha="left")
