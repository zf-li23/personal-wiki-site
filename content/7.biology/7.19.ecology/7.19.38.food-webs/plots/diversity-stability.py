"""Diversity and the variability of populations and communities (Tilman 1999; Doak et al. 1998).

S equally abundant species share a total mean abundance m = 1; each species' variance follows the
mean-variance scaling s^2 = c mu^z (c = 0.04). With independent fluctuations
CV_population = sqrt(c) (1/S)^(z/2 - 1) and CV_community = sqrt(c) S^((1 - z)/2).
A: CV of the community total (solid) and of single populations (dashed) against S for z = 1.0, 1.5
and 2.0: within the usual range 1 < z < 2 community variability falls and population variability rises
with richness. B: the role of synchrony for equal species with pairwise correlation rho:
CV_community / CV_population = sqrt(rho + (1 - rho)/S); positive correlation limits the averaging,
negative covariance (compensatory dynamics, possible only for rho >= -1/(S - 1)) strengthens it.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)

S = np.arange(1, 33)
c = 0.04
pa = C.axes_at(ax, (2.6, 1.9, 11.4, 8.4))
for z, tok in [(1.0, "rna"), (1.5, "dna"), (2.0, "positive")]:
    cvc = np.sqrt(c) * S ** ((1 - z) / 2)
    cvp = np.sqrt(c) * (1 / S) ** (z / 2 - 1)
    pa.plot(S, cvc, color=Q.line_color(tok), lw=1.8, label=f"community, z = {z}")
    pa.plot(S, cvp, color=Q.line_color(tok), lw=1.2, ls="--", label=f"population, z = {z}")
pa.set_xlim(1, 32)
pa.set_ylim(0, 0.8)
C.style_axes(pa, "number of species S", "coefficient of variation")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right", ncol=2)
bio.panel(ax, "A", (0.5, 11.6))
bio.label(ax, (2.6, 11.2), "Statistical averaging with mean-variance scaling", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (17.4, 1.9, 11.4, 8.4))
for rho, tok in [(0.6, "negative"), (0.3, "rna"), (0.0, "dna"), (-0.03, "positive")]:
    Ss = S[S <= (1 + 1 / -rho if rho < 0 else 99)]
    pb.plot(Ss, np.sqrt(rho + (1 - rho) / Ss), color=Q.line_color(tok), lw=1.6, label=f"rho = {rho}")
pb.set_xlim(1, 32)
pb.set_ylim(0, 1.05)
C.style_axes(pb, "number of species S", "CV community / CV population")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (15.3, 11.6))
bio.label(ax, (17.4, 11.2), "The portfolio effect depends on synchrony", size="small", bold=True, ha="left")
