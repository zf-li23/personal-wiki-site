"""Additive and compensatory mortality (Anderson and Burnham 1976; seasonal model in the spirit of Boyce et al. 1999).

A: total mortality from autumn to spring M against the mortality caused by predation or harvest h,
with natural mortality M0 = 1 - 1/lam = 0.6: fully additive (M = 1 - (1 - M0)(1 - h)), fully
compensatory up to a threshold equal to M0 (M = M0 for h <= M0, then M = h), and the partially
compensatory response of the seasonal model of B in the first year of predation, starting from the
unexploited equilibrium (circles). (At a new equilibrium total mortality returns to 1 - 1/lam, whatever
h, and the predation shows up instead as a lower density, panel B.) B: a seasonal model (simulated parameters): breeding multiplies the spring
population by lam = 2.5; predation removes a fraction h; winter survival is density dependent,
s(N) = s0 / (1 + b N) with s0 = 0.8, b = 0.005 per individual. If predation acts before the density-
dependent winter (autumn), survivors suffer less winter mortality and the equilibrium spring population
N* = (lam s0 (1 - h) - 1) / (b lam (1 - h)) declines slowly; if it acts after winter, just before
breeding, there is no compensation and N* = (lam s0 (1 - h) - 1) / (b lam) declines in proportion.
Both collapse at the same h = 1 - 1 / (lam s0) = 0.5. Dashed: a density-independent population
(no compensation at all), shown as the equilibrium of the after-winter case with the same growth.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)
lam, s0, b = 2.5, 0.8, 0.005

pb = C.axes_at(ax, (17.0, 1.8, 11.5, 8.6))
h = np.linspace(0, 0.6, 400)
g = lam * s0 * (1 - h) - 1
before = np.where(g > 0, g / (b * lam * (1 - h)), 0)
after = np.where(g > 0, g / (b * lam), 0)
n0 = before[0]
pb.plot(h, before / n0, color=Q.line_color("positive"), lw=1.8, label="predation before density-dependent winter")
pb.plot(h, after / n0, color=Q.line_color("negative"), lw=1.8, label="predation after winter")
pb.set_xlim(0, 0.6)
pb.set_ylim(0, 1.05)
C.style_axes(pb, "fraction killed by predators, h", "equilibrium spring density (relative)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (15.0, 11.6))
bio.label(ax, (17.0, 11.2), "Timing decides how much is compensated", size="small", bold=True, ha="left")

pa = C.axes_at(ax, (2.4, 1.8, 11.0, 8.6))
M0 = 1 - 1 / lam
hh = np.linspace(0, 0.8, 400)
pa.plot(hh, 1 - (1 - M0) * (1 - hh), color=Q.line_color("negative"), lw=1.8, label="additive")
pa.plot(hh, np.where(hh <= M0, M0, hh), color=Q.line_color("dna"), lw=1.8, label="fully compensatory")
# One year of predation before the density-dependent winter, starting from the unexploited equilibrium.
n_spring = (lam * s0 - 1) / (b * lam)
na = lam * n_spring
hs = np.linspace(0, 0.8, 17)
surv = (1 - hs) * s0 / (1 + b * (1 - hs) * na)
pa.plot(hs, 1 - surv, "o", color=Q.line_color("positive"), ms=4.5, label="seasonal model, first year")
pa.set_xlim(0, 0.8)
pa.set_ylim(0, 1.0)
C.style_axes(pa, "predation (or harvest) mortality, h", "total mortality from autumn to spring")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.4, 11.6))
bio.label(ax, (2.4, 11.2), "Additive versus compensatory mortality", size="small", bold=True, ha="left")
