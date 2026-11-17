"""Non-consumptive (fear) effects of predators on prey populations (model in the spirit of Wang, Zanette and Zou 2016).

Prey: dN/dt = N (b / (1 + f P) - d - c N) - a N P with a fixed predator density P. Simulated parameters:
birth rate b = 1, death rate d = 0.1, crowding c = 0.01 (carrying capacity 90 without predators),
attack rate a = 0.05; fear reduces births by the factor 1 / (1 + f P). A: equilibrium prey density
against predator density for killing only (f = 0), fear only (a = 0, f = 0.1) and both: fear alone,
without a single prey being eaten, lowers the prey equilibrium, and together the two effects
eliminate the prey at less than half the predator density needed by killing alone. B: prey dynamics
when a 40 % reduction in births, as measured by Zanette et al. (2011) for song sparrows exposed to
playbacks of predator calls, starts at time 20 (no prey killed): the population settles at a lower level.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)
b, d, c, a = 1.0, 0.1, 0.01, 0.05


def neq(Pd, a_, f_):
    return np.clip((b / (1 + f_ * Pd) - d - a_ * Pd) / c, 0, None)


Pd = np.linspace(0, 20, 400)
pa = C.axes_at(ax, (2.4, 1.8, 11.5, 8.6))
pa.plot(Pd, neq(Pd, a, 0), color=Q.line_color("negative"), lw=1.8, label="killing only")
pa.plot(Pd, neq(Pd, 0, 0.1), color=Q.line_color("dna"), lw=1.8, label="fear only")
pa.plot(Pd, neq(Pd, a, 0.1), color=P.ink(), lw=1.8, label="killing and fear")
pa.set_xlim(0, 20)
pa.set_ylim(0, 95)
C.style_axes(pa, "predator density P", "equilibrium prey density N*")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.4, 11.6))
bio.label(ax, (2.4, 11.2), "Consumptive and non-consumptive effects", size="small", bold=True, ha="left")


def rhs(t, y):
    bb = b * (0.6 if t >= 20 else 1.0)
    return [y[0] * (bb - d - c * y[0])]


t = np.linspace(0, 60, 600)
s = solve_ivp(rhs, (0, 60), [90.0], t_eval=t, max_step=0.1)
pb = C.axes_at(ax, (17.0, 1.8, 11.5, 8.6))
pb.plot(t, s.y[0], color=Q.line_color("dna"), lw=1.8)
pb.axvline(20, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.text(20.5, 30, "predator calls\nplayed from here", fontsize=FS["tiny"], color=P.muted())
pb.set_xlim(0, 60)
pb.set_ylim(0, 100)
C.style_axes(pb, "time", "prey density")
bio.panel(ax, "B", (15.0, 11.6))
bio.label(ax, (17.0, 11.2), "Births reduced by 40 % through fear alone", size="small", bold=True, ha="left")
