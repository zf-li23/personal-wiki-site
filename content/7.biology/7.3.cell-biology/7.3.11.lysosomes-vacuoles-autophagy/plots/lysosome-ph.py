"""Pump-leak model of lysosomal acidification (illustrative parameters, after Grabe and Oster 2001).
A lysosome of radius 0.25 um (volume 0.065 fL, membrane capacitance 1 uF cm^-2, buffer capacity
40 mM per pH unit) carries N = 300 V-ATPases of maximal turnover 30 H+ s^-1. The pump slows linearly as
the proton electrochemical gradient approaches its stall value dG_ATP/n = 25 kJ mol^-1 (n = 2 H+ per ATP).
Protons leak out with permeability P_H = 2e-5 cm s^-1 (Goldman-Hodgkin-Katz flux); Cl- enters through a
counter-ion conductance G_Cl = 0.2 pS (lumenal Cl- 60 mM, cytosolic 40 mM, cytosolic pH 7.2).
(A) Lumenal pH after the pumps are switched on at t = 0 (pH 7.2): with counter-ion conductance; without it;
with a third of the pumps; and with bafilomycin A1 (pumps off) added at t = 30 min.
(B) Membrane potential (lumen relative to cytosol) for the same cases.
(C) Steady-state pH as a function of the proton permeability for three pump numbers."""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

F, R, T = 96485.0, 8.314, 310.0
NA = 6.022e23
r = 0.25e-6
A = 4 * np.pi * r ** 2
V = 4 / 3 * np.pi * r ** 3
C = 1e-2 * A
beta = 40.0  # mol m^-3 per pH unit
pHc = 7.2
stall = 25e3
E_cl = R * T / F * np.log(60 / 40)


def rhs(t, y, n_pump, P_H, G_cl, baf_at=None):
    pHl, psi = y
    on = 0.0 if (baf_at is not None and t >= baf_at * 60) else 1.0
    jmax = on * n_pump * 30.0 / NA
    dmu = F * psi + np.log(10) * R * T * (pHc - pHl)
    jv = jmax * max(0.0, 1 - dmu / stall)
    u = F * psi / (R * T)
    hl, hc = 1e3 * 10 ** (-pHl), 1e3 * 10 ** (-pHc)
    if abs(u) < 1e-6:
        jl = P_H * A * (hl - hc)
    else:
        jl = P_H * A * u * (hl - hc * np.exp(-u)) / (1 - np.exp(-u))
    jcl = G_cl * (psi - E_cl) / F
    return [-(jv - jl) / (beta * V), F * (jv - jl - jcl) / C]


def run(n_pump=300, P_H=2e-7, G_cl=2e-13, baf_at=None, tmax=60):
    t = np.linspace(0, tmax * 60, 1500)
    sol = solve_ivp(rhs, (0, t[-1]), [pHc, 0.0], t_eval=t, args=(n_pump, P_H, G_cl, baf_at), method="LSODA",
                    rtol=1e-7, atol=[1e-8, 1e-8], max_step=2.0)
    return sol.t / 60, sol.y[0], sol.y[1] * 1e3


cases = [("control", dict(), "lysosome", "-"),
         ("no counter-ion", dict(G_cl=0.0), "negative", "--"),
         ("1/3 of pumps", dict(n_pump=100), "channel", "-."),
         ("bafilomycin at 30 min", dict(baf_at=30), "drug", ":")]

fig, ax = bio.canvas(22.0, 7.6)
bio.panel(ax, "A", (0.1, 7.5))
a = charts.axes_at(ax, (1.7, 1.3, 5.4, 5.6))
bio.panel(ax, "B", (7.9, 7.5))
b = charts.axes_at(ax, (9.5, 1.3, 5.0, 5.6))
for name, kw, tok, ls in cases:
    t, ph, psi = run(**kw)
    a.plot(t, ph, color=charts.line(tok), lw=1.8, ls=ls, label=name)
    b.plot(t, psi, color=charts.line(tok), lw=1.8, ls=ls)
a.set_xlim(0, 60)
a.set_ylim(4.0, 9.0)
a.set_yticks([4.0, 5.0, 6.0, 7.0])
a.set_xticks([0, 15, 30, 45, 60])

a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right", ncol=2)
charts.style_axes(a, "t / min", "lumenal pH")
b.set_xlim(0, 60)
b.set_xticks([0, 15, 30, 45, 60])
b.set_ylim(-20, 280)
charts.style_axes(b, "t / min", "Δψ (lumen − cytosol) / mV")

bio.panel(ax, "C", (15.2, 7.5))
c = charts.axes_at(ax, (16.8, 1.3, 4.9, 5.6))
perm = np.logspace(-8, -5.5, 18)
for n, tok in ((100, "channel"), (300, "lysosome"), (900, "enzyme")):
    ss = [run(n_pump=n, P_H=p, tmax=120)[1][-1] for p in perm]
    c.plot(perm * 100, ss, color=charts.line(tok), lw=1.7, label=f"N = {n} pumps")
c.set_xscale("log")
c.set_ylim(3.5, 7.4)

c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(c, r"$P_{\mathrm{H}}$ / (cm s$^{-1}$)", "steady-state pH")
