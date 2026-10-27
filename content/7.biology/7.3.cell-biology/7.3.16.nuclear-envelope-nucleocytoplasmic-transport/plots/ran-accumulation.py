"""A minimal model of Ran-driven nuclear import (Proposition 16.5.1).
Species in nucleus (n) and cytoplasm (c): free cargo C, free importin I, importin-cargo IC, importin-Ran-GTP IG;
Ran-GTP G is held fixed (G_n = 1, G_c = G_n / gradient). Binding I + C <-> IC (K1 = 1) and I + G <-> IG
(K2 = 100), mutually exclusive, with fast mass-action kinetics. I, IC and IG cross the pore with permeability 1,
free C with permeability k_p. Volumes V_n = 0.2, V_c = 1; total cargo and importin 1 each (concentration units).
(A) Ratio of free cargo C_n/C_c after the gradient is switched on (k_p = 0) for gradients 10, 100, 1000.
(B) Steady-state ratio against the gradient: k_p = 0 (simulation, points; Eq. (16.3), line) and k_p = 0.01, 0.05
(dashed); gray: the bound C_n/C_c = G_n/G_c."""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
Vn, Vc = 0.2, 1.0
K1, K2 = 1.0, 100.0
kon = 2000.0
Gn = 1.0


def rhs(t, y, Gc, kp):
    Cn, In, ICn, IGn, Cc, Ic, ICc, IGc = y
    out = np.zeros(8)
    # binding in each compartment
    for off, G in ((0, Gn), (4, Gc)):
        C, I, IC, IG = y[off:off + 4]
        r1 = kon * (K1 * I * C - IC)
        r2 = kon * (K2 * I * G - IG)
        out[off + 0] += -r1
        out[off + 1] += -r1 - r2
        out[off + 2] += r1
        out[off + 3] += r2
    # transport (flux from cytoplasm to nucleus, amount per time)
    for k, perm in ((0, kp), (1, 1.0), (2, 1.0), (3, 1.0)):
        J = perm * (y[4 + k] - y[k])
        out[k] += J / Vn
        out[4 + k] -= J / Vc
    return out


def initial():
    # uniform concentrations of total cargo and importin (1 each), unbound
    return np.array([1.0, 1.0, 0, 0, 1.0, 1.0, 0, 0])


def run(grad, kp, T=60.0):
    sol = solve_ivp(rhs, (0, T), initial(), args=(Gn / grad, kp), method="LSODA", rtol=1e-8, atol=1e-10, dense_output=True)
    return sol


fig, ax = bio.canvas(19.0, 7.4)
bio.panel(ax, "A", (0.1, 7.3))
a = charts.axes_at(ax, (1.9, 1.3, 6.6, 5.6))
t = np.linspace(0, 30, 400)
for g, tok in ((10, "channel"), (100, "positive"), (1000, "negative")):
    s = run(g, 0.0, T=30)
    y = s.sol(t)
    a.plot(t, y[0] / y[4], color=charts.line(tok), lw=1.8, label=rf"$G_\mathrm{{n}}/G_\mathrm{{c}}$ = {g}")
    a.axhline((1 + K2 * Gn) / (1 + K2 * Gn / g), color=charts.line(tok), lw=0.8, ls=":")
a.set_yscale("log")
a.set_xlim(0, 30)
a.set_ylim(0.8, 200)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(a, "time (arbitrary units)", "free cargo, nucleus / cytoplasm")

bio.panel(ax, "B", (9.9, 7.3))
b = charts.axes_at(ax, (11.6, 1.3, 6.9, 5.6))
gr = np.logspace(0, 4, 200)
b.plot(gr, gr, color=P.muted(), lw=1.0, label=r"limit $G_\mathrm{n}/G_\mathrm{c}$")
b.plot(gr, (1 + K2 * Gn) / (1 + K2 * Gn / gr), color=charts.line("positive"), lw=1.8, label=r"Eq. (16.3), $k_\mathrm{p} = 0$")
pts = np.logspace(0, 4, 9)
ss = []
for g in pts:
    y = run(g, 0.0, T=400).y[:, -1]
    ss.append(y[0] / y[4])
b.plot(pts, ss, "o", color=charts.line("positive"), ms=4)
for kp, ls in ((0.01, "--"), (0.05, (0, (1.5, 1.5)))):
    vals = []
    for g in pts:
        y = run(g, kp, T=600).y[:, -1]
        vals.append(y[0] / y[4])
    b.plot(pts, vals, color=charts.line("negative"), lw=1.5, ls=ls, label=rf"leak $k_\mathrm{{p}}$ = {kp}")
b.set_xscale("log")
b.set_yscale("log")
b.set_xlim(1, 1e4)
b.set_ylim(0.8, 1.5e4)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, r"Ran-GTP gradient $G_\mathrm{n}/G_\mathrm{c}$", r"steady-state $C_\mathrm{n}/C_\mathrm{c}$")
