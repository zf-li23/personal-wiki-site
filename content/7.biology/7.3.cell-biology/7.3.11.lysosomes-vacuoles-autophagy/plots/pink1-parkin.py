"""A minimal model of PINK1-Parkin signaling on one mitochondrion (illustrative parameters, time in minutes).
PINK1 is made at rate sigma = 0.05 and either imported (and then cleaved and degraded) with a rate constant
that depends on the membrane potential, k_imp = 1/(1 + exp(-(dpsi - 100 mV)/10 mV)), or, when it stays on
the outer membrane, removed slowly (delta = 0.05):  dP/dt = sigma - (k_imp + delta) P.
Phospho-ubiquitin U on the outer membrane is made by PINK1 and amplified by Parkin, which is recruited and
activated by phospho-ubiquitin (feed-forward loop), and removed by deubiquitylases and turnover:
dU/dt = P (a0 + a1 U^2/(K^2 + U^2)) - gamma U, with a0 = 0.1, a1 = 1, K = 1, gamma = 0.4.
(A) Steady-state PINK1 on the outer membrane as a function of the membrane potential.
(B) Steady states of phospho-ubiquitin reached from low and from high initial U: a sharp threshold near 65 mV
(the two branches almost coincide, so the hysteresis is narrow). (C) Response to depolarization (CCCP, dpsi from 160 to 20 mV at t = 0) and
recovery when the potential is restored at t = 60 min."""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
sigma, delta, a0, a1, K, gamma = 0.05, 0.05, 0.1, 1.0, 1.0, 0.4


def kimp(psi):
    return 1 / (1 + np.exp(-(psi - 100) / 10))


def rhs(t, y, psi_of_t):
    p, u = y
    psi = psi_of_t(t)
    return [sigma - (kimp(psi) + delta) * p, p * (a0 + a1 * u ** 2 / (K ** 2 + u ** 2)) - gamma * u]


psis = np.linspace(0, 180, 181)
pstar = sigma / (kimp(psis) + delta)
lo, hi = [], []
for psi in psis:
    for start, store in ((0.0, lo), (5.0, hi)):
        s = solve_ivp(rhs, (0, 3000), [sigma / (kimp(psi) + delta), start], args=(lambda t, v=psi: v,), rtol=1e-8)
        store.append(s.y[1, -1])
lo, hi = np.array(lo), np.array(hi)

fig, ax = bio.canvas(22.0, 7.6)
bio.panel(ax, "A", (0.1, 7.5))
a = charts.axes_at(ax, (1.7, 1.3, 5.0, 5.6))
a.plot(psis, pstar, color=charts.line("enzyme"), lw=1.8)
a.axvspan(140, 180, color=P_.fill("positive"), alpha=0.25, lw=0)
a.text(160, 0.9, "healthy", ha="center", fontsize=FT["tiny"], color=P_.ink())
a.text(28, 0.6, "depolarized", ha="center", fontsize=FT["tiny"], color=P_.ink())
a.set_xlim(0, 180)
a.set_ylim(0, 1.05)
charts.style_axes(a, "Δψ / mV", "PINK1 on outer membrane (P*)")

bio.panel(ax, "B", (7.6, 7.5))
b = charts.axes_at(ax, (9.2, 1.3, 5.0, 5.6))
b.plot(psis, lo, color=charts.line("negative"), lw=1.8, label="from low U")
b.plot(psis, hi, color=charts.line("highlight"), lw=1.8, ls="--", label="from high U")
b.set_xlim(0, 180)
b.set_ylim(0, 2.7)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper right")
charts.style_axes(b, "Δψ / mV", "phospho-ubiquitin U (steady state)")

bio.panel(ax, "C", (15.1, 7.5))
c = charts.axes_at(ax, (16.7, 1.3, 5.0, 5.6))
psi_t = lambda t: 20.0 if 0 <= t < 60 else 160.0
y0 = [sigma / (kimp(160) + delta), lo[160]]
sol = solve_ivp(rhs, (0, 180), y0, args=(psi_t,), t_eval=np.linspace(0, 180, 900), max_step=0.5, rtol=1e-8)
c.plot(sol.t, sol.y[0], color=charts.line("enzyme"), lw=1.8, label="PINK1 (P)")
c.plot(sol.t, sol.y[1] / 2.5, color=charts.line("negative"), lw=1.8, label="pUb (U/2.5)")
c.axvspan(0, 60, color=P_.fill("neutral"), alpha=0.3, lw=0)
c.text(30, 1.0, "CCCP", ha="center", fontsize=FT["tiny"], color=P_.ink())
c.set_xlim(0, 180)
c.set_ylim(0, 1.08)
c.set_xticks([0, 60, 120, 180])
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="center right")
charts.style_axes(c, "t / min", "level (relative)")
