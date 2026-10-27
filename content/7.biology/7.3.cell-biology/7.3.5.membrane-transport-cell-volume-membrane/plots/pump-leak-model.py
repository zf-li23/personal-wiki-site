"""The pump-leak model of an animal cell, and what happens when the Na/K pump is blocked with ouabain.

State: amounts of Na+, K+, Cl- in the cell and the cell volume V; impermeant anions X (amount fixed,
mean charge -1.1, chosen so that the cell starts electroneutral and isotonic).
Leaks: Goldman-Hodgkin-Katz flux for each ion, P_K = 5e-9 m/s, P_Na = 0.05 P_K, P_Cl = 0.4 P_K,
membrane area 1000 um^2, 37 C. Pump: 3 Na out, 2 K in per cycle, J = Jmax (Na/(Na+10))^3 (Ko/(Ko+1.5))^2.
Membrane potential: the value at which the net current (leaks + pump) is zero at every instant.
Water: dV/dt = Lp A RT (osm_in - osm_out). Outside: Na 145, K 5, Cl 110, other 30 mOsm (fixed).
The pump is stopped at t = 10 min.
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
F, Rg, T = 96485.0, 8.314, 310.0
RT = Rg * T
A = 1e-9
No, Ko, Clo = 145.0, 5.0, 110.0
OSMO = No + Ko + Clo + 30
PK = 5e-9
PNa, PCl = 0.05 * PK, 0.4 * PK
LP = 2e-14
JMAX = 4e-16
V0 = 2e-15
NA0, K0, CL0 = 12.0, 140.0, 8.0
XM = (OSMO - NA0 - K0 - CL0) * V0


def ghk(p, z, ci, co, v):
    u = z * F * v / RT
    if abs(u) < 1e-9:
        return p * A * (ci - co)
    return p * A * u * (ci - co * np.exp(-u)) / (1 - np.exp(-u))


def pump(na, jm):
    return jm * (na / (na + 10)) ** 3 * (Ko / (Ko + 1.5)) ** 2


def vm(y, jm):
    n, k, c, vol = y
    na, kk, cl = n / vol, k / vol, c / vol
    return brentq(lambda v: ghk(PNa, 1, na, No, v) + ghk(PK, 1, kk, Ko, v) - ghk(PCl, -1, cl, Clo, v) + pump(na, jm), -0.2, 0.1)


def rhs(t, y, t_off):
    jm = 0.0 if t > t_off else JMAX
    n, k, c, vol = y
    v = vm(y, jm)
    na, kk, cl = n / vol, k / vol, c / vol
    p = pump(na, jm)
    return [-ghk(PNa, 1, na, No, v) - 3 * p, -ghk(PK, 1, kk, Ko, v) + 2 * p, -ghk(PCl, -1, cl, Clo, v),
            LP * A * RT * ((n + k + c + XM) / vol - OSMO)]


y0 = [NA0 * V0, K0 * V0, CL0 * V0, V0]
ss = solve_ivp(rhs, [0, 7200], y0, args=(1e9,), method="LSODA", rtol=1e-8, atol=1e-22, max_step=30).y[:, -1]
sol = solve_ivp(rhs, [-20 * 60, 6 * 3600], ss, args=(600.0,), method="LSODA", rtol=1e-8, atol=1e-22, max_step=20,
                dense_output=True)
t = np.linspace(-20 * 60, 6 * 3600, 700)
Y = sol.sol(t)
conc = Y[:3] / Y[3]
vols = Y[3] / V0
vms = np.array([vm(Y[:, i], 0.0 if t[i] > 600 else JMAX) for i in range(len(t))]) * 1e3
th = t / 3600

fig, ax = bio.canvas(22.0, 8.0)
bio.panel(ax, "A", (0.1, 7.8))
pa = charts.axes_at(ax, (1.7, 1.3, 8.2, 5.8))
for i, (name, tok) in enumerate((("Na⁺", "na"), ("K⁺", "k"), ("Cl⁻", "cl"))):
    pa.plot(th, conc[i], color=charts.line(tok), lw=1.9, label=name)
pa.axvline(600 / 3600, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pa.text(600 / 3600 + 0.08, 152, "ouabain", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="left")
pa.set_xlim(th[0], th[-1])
pa.set_ylim(0, 160)
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(pa, "time / h", "cytosolic concentration / mM")
charts.title(pa, "Ion gradients run down")

bio.panel(ax, "B", (11.3, 7.8))
pb = charts.axes_at(ax, (12.9, 1.3, 7.2, 5.8))
pb.plot(th, vols, color=charts.line("dna"), lw=1.9)
pb.set_ylim(0.9, 2.2)
pb.set_xlim(th[0], th[-1])
pb.axvline(600 / 3600, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
charts.style_axes(pb, "time / h", "relative volume V/V₀")
pc = pb.twinx()
pc.set_facecolor("none")
pc.plot(th, vms, color=charts.line("negative"), lw=1.9, ls=(0, (4, 2)))
pc.set_ylim(-80, 0)
charts.style_axes(pc, None, "membrane potential / mV")
pc.spines["right"].set_visible(True)
pc.spines["right"].set_color(P.muted())
pb.text(4.4, 1.62, "volume", fontsize=bio.core.FONT["tiny"], color=charts.line("dna"), ha="left")
pb.text(0.45, 2.08, "membrane potential (dashed)", fontsize=bio.core.FONT["tiny"], color=charts.line("negative"), ha="left")
charts.title(pb, "The cell swells and depolarizes")
